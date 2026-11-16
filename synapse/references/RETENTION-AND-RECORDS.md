# Phase 6 Reference: Teach-Before-Test Socratic Loop, Learning Records & `wait-what`

---

## 1. Adaptive Teaching & Retrieval Protocol

Read `MASTERY-ENGINE.md` before teaching or assessment.

### New Concepts (M0)
1. Explain the concept from first principles.
2. Demonstrate a concrete worked example.
3. Explain formulas and symbols where applicable.
4. Ask one guided question.
5. Evaluate the learner's reasoning.
6. Adjust difficulty based on the response.

### Previously Taught Concepts (M1–M4)
1. Begin with unaided retrieval practice.
2. Ask one question without revealing the answer.
3. Evaluate correctness, reasoning, and confidence.
4. If successful, increase difficulty appropriately.
5. If unsuccessful, diagnose the misconception.
6. Revisit missing prerequisites when necessary.
7. Provide targeted instruction and reassess.

### Mastery Verification
- Never equate recognition with mastery.
- Never rely solely on self-reported confidence.
- Require repeated independent success.
- Verify M4 with unfamiliar transfer problems.
- Record assessment evidence and misconceptions.
- Advance only when prerequisite understanding is sufficient.

### Teaching Principle
Optimize for demonstrated understanding and durable
retention, not explanation length or note volume.


---

## 2. Baseline-Calibrated Socratic Grilling (Beginner-Safe Question 1)

Calibrate Question 1 strictly to the user's baseline recorded in `00-MISSION.md`:

- **For `0 knowledge` / `Beginner` baselines:**
  - *Mandatory Rule:* Start Question 1 with a concrete **1-number scalar trace** (plugging 1 simple number into the mechanism or formula to see what comes out) before introducing 2D geometry, vectors/matrices, or multi-variable edge cases.
  - Only escalate to 2D geometry or multi-feature interactions in Question 2+ once the 1-number trace succeeds.
- **For `Intermediate` / `Advanced` baselines:**
  - Start Question 1 with a targeted diagnostic, invariant check, or failure-mode prediction scenario.

### Pedagogical Rules (Storage Strength vs. Retrieval Fluency)
- **Test Storage, Not Recognition:** Never ask `"Do you understand X?"` or simple definition lookups. Ask trace, diagnostic, transfer, or failure-prediction questions.
- **One Question at a Time:** Wait for the user's response before moving on.
- **Evaluate & Calibrate:**
  - Identify what the user nailed accurately.
  - Pinpoint any subtle misconception or missing invariant without lecturing.
  - Adjust difficulty dynamically (step up to edge cases if they ace it; scaffold down to a simpler 1-number trace if they struggle).
  - When a subtopic is mastered, check it off (`- [x]`) in `~/notes/<topic-slug>/00-MOC-INDEX.md`.

---

## 3. Inline `wait-what` Protocol

If at any point the user replies with **`wait what`**, **`/wait-what`**, **`I'm lost`**, or **`simplify`**:
1. **Pause the grill immediately**—do not judge or test them.
2. **Diagnose the Jargon/Abstraction Jump:** Identify the exact concept or unstated assumption that caused friction.
3. **Re-Pitch in Plain English:** Explain the concept from scratch using:
   - Strictly canonical terms defined in `04-GLOSSARY.md` (defining any new word inline).
   - A concrete **1-number scalar trace** or simpler step-by-step mental model.
4. **Update the Vault:** Append the clearer explanation or analogy to `~/notes/<topic-slug>/05-MENTAL-MODELS.md` so the permanent notes improve alongside the user's understanding.
5. **Resume Gently:** Check that the re-pitch clicks before asking a lighter verification question.

---

## 4. ADR-Style Learning Records (`learning-records/000N-<slug>.md`)

Maintain a chronological log of breakthroughs, corrected misconceptions, and mission changes inside `~/notes/<topic-slug>/learning-records/` (numbered `0001-<slug>.md`, `0002-<slug>.md`, etc.). Never delete old records; if a later insight supersedes an earlier understanding or goal, mark the old record `Status: superseded by LR-000N`.

### Template: `~/notes/<topic-slug>/learning-records/0001-<slug>.md`

```markdown
# LR-0001: <Short Title of Breakthrough, Misconception Fix, or Mission Shift>

- **Date:** <YYYY-MM-DD>
- **Status:** active
- **Milestone:** <Milestone # from 00-MISSION.md>

## Context
<What question, scenario, or confusion triggered this learning moment.>

## Insight / Mastery Demonstrated
<What was clarified, proven, or decided—using canonical terms from 04-GLOSSARY.md.>

## Vault Updates Made
- Updated `<filename>` with <specific addition or correction>.
```

---

## 5. Continuous Note Enrichment

Whenever the user shares a new insight, real-world war story, voice transcript, or sharp follow-up question during Phase 6:
- Cleanly format and append it under `## Living Session Notes & Insights` in `~/notes/<topic-slug>/03-CORNELL-STUDY-GUIDE.md`.
- If it introduces a new core term, add a 1-2 sentence entry to `~/notes/<topic-slug>/04-GLOSSARY.md`.
- Confirm briefly in chat what was persisted to the vault.
