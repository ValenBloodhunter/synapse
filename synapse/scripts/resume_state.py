
#!/usr/bin/env python3
"""Read Synapse learner progress and identify the next activity."""

import argparse
import json
import re
from datetime import date
from pathlib import Path


def resume_state(topic: str) -> dict:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", topic):
        raise ValueError("Invalid topic slug")

    path = Path.home() / "notes" / topic / ".synapse" / "state.json"

    if not path.is_file():
        raise FileNotFoundError(
            "No learning memory found. Run init_state.py first."
        )

    state = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(state, dict):
        raise ValueError("Invalid learning state")

    if state.get("schema_version") != 1:
        raise ValueError("Unsupported state version")

    if state.get("topic_slug") != topic:
        raise ValueError("Topic does not match stored state")

    concepts = state.get("concepts")
    reviews = state.get("review_queue")

    if not isinstance(concepts, dict) or not isinstance(reviews, list):
        raise ValueError("Invalid learning state structure")

    today = date.today()
    due_reviews = []

    for review in reviews:
        if not isinstance(review, dict):
            raise ValueError("Invalid review entry")

        concept_id = review.get("concept_id")
        due_at = review.get("due_at")

        if not isinstance(concept_id, str) or not isinstance(due_at, str):
            raise ValueError("Invalid review fields")

        if date.fromisoformat(due_at) <= today:
            due_reviews.append(concept_id)

    current = state.get("current_concept_id")

    if current is not None and not isinstance(current, str):
        raise ValueError("Invalid current concept")

    if due_reviews:
        next_action = "review"
    elif current:
        next_action = "continue"
    else:
        next_action = "select_concept"

    return {
        "topic": topic,
        "current_concept": current,
        "due_reviews": sorted(set(due_reviews)),
        "next_action": next_action,
        "mastery": {
            concept_id: record.get("mastery", 0)
            for concept_id, record in concepts.items()
            if isinstance(record, dict)
        }
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    args = parser.parse_args()

    try:
        result = resume_state(args.topic)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, TypeError) as error:
        parser.exit(1, f"Error: {error}\n")
