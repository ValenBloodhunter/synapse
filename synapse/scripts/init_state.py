
#!/usr/bin/env python3
"""Initialize persistent learning memory for Synapse."""

import argparse
import json
import re
from pathlib import Path


def initialize_state(topic_slug: str) -> Path:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", topic_slug):
        raise ValueError("Use a lowercase topic slug, e.g. machine-learning")

    skill_dir = Path(__file__).resolve().parent.parent

    template_path = skill_dir / "assets" / "state.template.json"

    state_path = (
        Path.home()
        / "notes"
        / topic_slug
        / ".synapse"
        / "state.json"
    )

    # Never overwrite existing progress.
    if state_path.exists():
        existing = json.loads(state_path.read_text(encoding="utf-8"))

        if not isinstance(existing, dict) or existing.get("schema_version") != 1:
            raise ValueError("Existing state has an unsupported format")

        print(f"Existing memory preserved: {state_path}")
        return state_path

    # Load the official template.
    state = json.loads(template_path.read_text(encoding="utf-8"))
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        raise ValueError("Invalid state template")

    state["topic_slug"] = topic_slug

    state_path.parent.mkdir(parents=True, exist_ok=True)

    # Exclusive creation prevents overwriting an existing file.
    try:
        with state_path.open("x", encoding="utf-8") as file:
            json.dump(state, file, indent=2, ensure_ascii=False)
            file.write("\n")
    except FileExistsError:
        print("Memory already exists; not overwritten")
        return state_path

    print(f"Synapse memory initialized: {state_path}")
    return state_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", help="Topic slug, e.g. machine-learning")
    args = parser.parse_args()

    try:
        initialize_state(args.topic)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(1, f"Error: {error}\n")
