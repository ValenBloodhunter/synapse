
# Synapse Persistent Learner State

## Purpose
Preserve learning progress across sessions so Synapse
can resume teaching without starting from scratch.

## State Location
~/notes/<topic-slug>/.synapse/state.json

Initialize from:
assets/state.template.json

## Concept State Schema

Each concept is identified by a stable concept ID.

Example:

{
  "mastery": 2,
  "attempts": 3,
  "successful_attempts": 2,
  "last_reviewed_at": "2026-11-16",
  "next_review_at": "2026-11-19",
  "misconceptions": [
    "Confuses derivatives with gradients"
  ],
  "evidence": [
    {
      "type": "guided_explanation",
      "result": "success",
      "date": "2026-11-16"
    }
  ]
}

## Mastery Rules

- M0: No demonstrated knowledge.
- M1: Recognition.
- M2: Guided understanding.
- M3: Independent application.
- M4: Transfer to unfamiliar problems.

Mastery changes must be supported by assessment evidence.

A single correct answer does not establish M4.

## Session Resume Protocol

1. Check whether state.json exists.
2. If absent, initialize from the template.
3. If present, load and validate existing state.
4. Identify the current concept.
5. Check pending reviews.
6. Resume from the most appropriate learning activity.
7. Save updated progress after assessment.

## State Safety Rules

- Never silently reset learner progress.
- Never overwrite state without reading it first.
- Preserve unknown fields for forward compatibility.
- Store dates in ISO 8601 format.
- Keep concept IDs stable.
- Reject invalid mastery levels.
- Save changes atomically when supported.
- Never claim state was saved unless the write succeeded.

## Review Queue

Each scheduled review should reference:
- concept_id
- due_at

Avoid duplicate pending reviews for the same concept.

## Privacy

Store only information needed for learning.
Never store credentials or unnecessary personal data.