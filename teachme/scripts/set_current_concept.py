
#!/usr/bin/env python3
"""Save the current Synapse lesson without changing mastery."""

import argparse
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def set_current_concept(topic: str, concept: str) -> None:
    pattern = r"[a-z0-9]+(?:-[a-z0-9]+)*"

    if not re.fullmatch(pattern, topic):
        raise ValueError("Invalid topic slug")

    if not re.fullmatch(pattern, concept):
        raise ValueError("Invalid concept ID")

    path = (
        Path.home()
        / "notes"
        / topic
        / ".synapse"
        / "state.json"
    )

    if not path.is_file():
        raise FileNotFoundError(
            "Initialize memory with init_state.py first"
        )

    state = json.loads(path.read_text(encoding="utf-8"))

    if (
        not isinstance(state, dict)
        or state.get("schema_version") != 1
        or state.get("topic_slug") != topic
        or not isinstance(state.get("concepts"), dict)
        or not isinstance(state.get("review_queue"), list)
    ):
        raise ValueError("Invalid learning state")

    state["current_concept_id"] = concept
    state["last_session_at"] = datetime.now(
        timezone.utc
    ).isoformat()

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            suffix=".tmp",
            delete=False
        ) as file:
            temp_path = Path(file.name)
            json.dump(state, file, indent=2, ensure_ascii=False)
            file.write("\n")
            file.flush()
            os.fsync(file.fileno())

        os.replace(temp_path, path)

    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

    print(f"Current lesson saved: {concept}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("concept")
    args = parser.parse_args()

    try:
        set_current_concept(args.topic, args.concept)
    except (OSError, ValueError, TypeError) as error:
        parser.exit(1, f"Error: {error}\n")
