
#!/usr/bin/env python3
"""Record assessment results and update Synapse mastery."""

import argparse
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def update_mastery(topic, concept, kind, result, task_id, note):
    slug_pattern = r"[a-z0-9]+(?:-[a-z0-9]+)*"
    for value in (topic, concept):
        if not re.fullmatch(slug_pattern, value):
            raise ValueError("Invalid topic or concept slug")

    path = Path.home() / "notes" / topic / ".synapse" / "state.json"

    if not path.is_file():
        raise FileNotFoundError("Initialize memory with init_state.py first")

    state = json.loads(path.read_text(encoding="utf-8"))

    if (
        not isinstance(state, dict)
        or state.get("schema_version") != 1
        or state.get("topic_slug") != topic
        or not isinstance(state.get("concepts"), dict)
    ):
        raise ValueError("Invalid or unsupported learning state")

    concepts = state["concepts"]
    record = concepts.setdefault(concept, {
        "mastery": 0,
        "attempts": 0,
        "successful_attempts": 0,
        "misconceptions": [],
        "evidence": []
    })

    if any(e.get("task_id") == task_id for e in record["evidence"]):
        raise ValueError("This assessment was already recorded")

    today = datetime.now(timezone.utc).date().isoformat()

    evidence = {
        "task_id": task_id,
        "type": kind,
        "result": result,
        "date": today,
        "note": note
    }

    record["evidence"].append(evidence)
    record["attempts"] += 1
    record["last_reviewed_at"] = today

    if result == "success":
        record["successful_attempts"] += 1
    else:
        record["misconceptions"].append(note)

    successful = [
        e for e in record["evidence"]
        if e.get("result") == "success"
    ]

    independent = {
        e["task_id"] for e in successful
        if e.get("type") in ("independent", "transfer")
    }

    transfer = {
        e["task_id"] for e in successful
        if e.get("type") == "transfer"
    }

    level = 0

    if successful:
        level = 1

    if any(e.get("type") == "guided" for e in successful):
        level = max(level, 2)

    if len(independent) >= 2:
        level = 3

    if len(transfer) >= 2 and len(independent) >= 3:
        level = 4

    # Update mastery based on assessment evidence.
    record["mastery"] = max(record["mastery"], level)

    # Remember the most recently assessed concept.
    state["current_concept_id"] = concept



    # Save atomically to avoid partially written JSON.
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            suffix=".tmp",
            delete=False
        ) as tmp:
            temp_path = Path(tmp.name)
            json.dump(state, tmp, indent=2, ensure_ascii=False)
            tmp.write("\n")
            tmp.flush()
            os.fsync(tmp.fileno())

        os.replace(temp_path, path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

    print(f"{concept}: mastery M{record['mastery']}")
    print("Assessment saved successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("concept")
    parser.add_argument("--kind", required=True, choices=[
        "recognition", "guided", "independent", "transfer"
    ])
    parser.add_argument("--result", required=True,
                        choices=["success", "failure"])
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--note", required=True)

    args = parser.parse_args()

    try:
        update_mastery(
            args.topic, args.concept, args.kind,
            args.result, args.task_id, args.note
        )
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.exit(1, f"Error: {error}\n")