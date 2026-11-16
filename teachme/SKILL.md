---
name: teachme
description: Unified end-to-end learning, deep primary-source research, frontier grilling, Socratic teaching, and structured Markdown note-taking pipeline. Invoke with `/teachme <topic>` or when the user asks to deeply research, learn, build a study guide, generate Cornell notes, create Zettelkasten cards, or master any topic from first principles into a central vault (`~/notes/<topic-slug>/`).
---

# Unified `/teachme` Master Pipeline

When invoked as `/teachme <topic>` (or when the user asks to deeply research, learn, and take complete notes on a topic), execute this **6-Phase Stateful Pipeline** inside the user's **central knowledge vault** (`~/notes/<topic-slug>/`).

Do NOT dump everything in a single wall of chat text. Write clean, pure Markdown files into `~/notes/<topic-slug>/` while guiding the user interactively in chat.

---

## Non-Negotiable Operating Laws

1. **Central Vault Only:** Always write all generated files to `~/notes/<topic-slug>/` (expanding `~` to the user's home directory), regardless of which workspace is currently open. Never scatter notes inside random project folders.
2. **Adaptive Session Initialization:** Before starting a learning session, check whether the topic already has an existing learning vault and saved mission. For a new topic, begin with Phase 1 Frontier Grilling (3–4 calibrated questions), unless the user passes `--auto` or requests defaults. For an existing topic, preserve the previous mission and use the Persistent Learner Memory protocol to resume from saved progress. Skip completed research and note-generation phases unless the user explicitly requests regeneration or a mission change. If the existing vault is incomplete, resume only the unfinished phases. Never unnecessarily restart the curriculum or overwrite existing learning progress.
3. **Markdown Notes & Persistent Learning State:** Keep all human-readable study notes in pure Markdown (`.md`) for compatibility with Obsidian and Git. Permit one machine-readable JSON file at `~/notes/<topic-slug>/.synapse/state.json` to store learner progress, mastery levels, assessment evidence, misconceptions, current position, and review schedules. Create the state file only when filesystem access is available. Never overwrite existing learning state without reading and preserving prior progress. Do not store passwords, credentials, or unnecessary personal information.
4. **Never Trust Parametric Knowledge Alone:** Treat pre-trained knowledge as untrusted until grounded in primary sources during Phase 2.
5. **Progressive Reference Loading:** Read the supporting reference files in `references/` at the exact phase or subcommand they govern so instructions stay crisp and complete:
   - Phase 1: `references/MISSION-AND-GRILL.md`
   - Phase 2: `references/RESEARCH-TOOLCHAIN.md`
   - Phases 3, 4 & 5: `references/STUDY-AND-GLOSSARY.md`
   - Phase 6: `references/RETENTION-AND-RECORDS.md`
   - Subcommands (`ingest`, `distill`, `review`, `feynman`, `drill`, `compare`, `audit`): `references/SUBCOMMANDS.md`
6. **Exhaustive Subtopic Coverage (1 Topic / Subtopic = 1 Dedicated `.md` File, No Caps):** Never compress, merge, or skip subtopics or cards to save space. Decompose the subject into an exhaustive syllabus in Phase 2, and generate a full-length, standalone `topics/<nn>-<subtopic-slug>.md` file for **every single topic and subtopic** in that syllabus, plus as many `atomic/` Zettelkasten cards as needed for full mastery.
7. **Zero Black-Box Formulas (Mandatory Formula Anatomy Breakdown):** Across `02-DEEP-RESEARCH.md`, `03-CORNELL-STUDY-GUIDE.md`, and every `topics/<nn>-<subtopic-slug>.md` file, **no mathematical formula, equation, recurrence, objective/loss function, or complexity bound** may appear without an immediate **Formula Anatomy Breakdown** (display LaTeX `$$...$$`, Plain-English Intuition, complete Component & Operator Breakdown Table, Boundary & Limiting Cases, and Worked Numerical Walkthrough).
8. **Adaptive Teach-Before-Test Rule:** For concepts the learner has never studied, provide a clear explanation before graded assessment. For previously taught concepts, begin with unaided retrieval practice to measure retention. Never repeat a full lesson unnecessarily. If retrieval fails, identify the misconception, revisit missing prerequisites, provide targeted instruction, and reassess using a different question. Follow `references/MASTERY-ENGINE.md` for mastery evaluation and difficulty adjustment.
9. **Adaptive Mastery Engine:** Read `references/MASTERY-ENGINE.md` before Phase 6 teaching, assessment, or review. Use its M0–M4 mastery levels to adapt explanations, question difficulty, and remediation. Teach new concepts before testing; use unaided recall for previously taught concepts. Assess mastery using demonstrated reasoning rather than self-reported understanding. Diagnose missing prerequisites when learners struggle, and never mark a concept as mastered without sufficient evidence.
10. **Persistent Learner Memory:** Read `references/LEARNER-STATE.md` before initializing, resuming, or reviewing a learning session. When filesystem access is available, load learner progress from `~/notes/<topic-slug>/.synapse/state.json`. If the file does not exist, initialize it using `assets/state.template.json`. Track mastery levels, assessment evidence, misconceptions, current concept, and scheduled reviews. Preserve existing progress and update state after assessments. Never claim progress was saved unless the write succeeds. If persistent storage is unavailable, explain the limitation and continue without claiming cross-session memory.
11. **Automatic Mastery Persistence:** When filesystem and Python execution are available, use the bundled scripts to maintain learner progress.

   - After successful initialization, run `python3 <skill-root>/scripts/resume_state.py <topic-slug>` and parse its JSON output.
   - If `next_action` is `review`, prioritize concepts in `due_reviews` using unaided retrieval practice.
   - If `next_action` is `continue`, resume teaching from `current_concept` using its recorded mastery level.
   - If `next_action` is `select_concept`, choose the next appropriate concept from the prerequisite syllabus.
   - Never restart an existing learning curriculum unnecessarily.
   - If resumption fails, report the error and preserve existing state rather than resetting it.
   - At session start, run `python3 <skill-root>/scripts/init_state.py <topic-slug>` to initialize or preserve existing memory.
   - After each graded assessment, evaluate the learner's actual reasoning and classify the attempt as `recognition`, `guided`, `independent`, or `transfer`.
   - Record the outcome using `python3 <skill-root>/scripts/update_mastery.py <topic-slug> <concept-id> --kind <kind> --result <success|failure> --task-id <unique-id> --note "<brief feedback>"`.
   - Generate a unique task ID for each assessment to prevent duplicate records.
   - Never record an assessment that did not actually occur.
   - Never invent successful assessment results.
   - Only confirm mastery updates after successful script execution.
   - If execution fails, disclose the failure instead of pretending progress was saved.
   - Before resuming a session, read and validate existing state. Do not reset progress.
   - If scripts cannot be executed, continue teaching without claiming persistent memory.


---

## Central Vault File Architecture

For any `<topic>`, create and maintain this exact directory tree at `~/notes/<topic-slug>/`:

```text
~/notes/<topic-slug>/
├── 00-MISSION.md                  # Concrete goals, success criteria, constraints, out-of-scope
├── 00-MOC-INDEX.md                # Master Map of Content, Mermaid+ASCII prereq graph & progress tracker
├── 01-RESOURCES.md                # Vetted Knowledge (primary) + Wisdom (communities) + Exhaustive Syllabus + Gaps
├── 02-DEEP-RESEARCH.md            # Primary-source chased dossier with claim provenance, Formula Anatomy & conflicts
├── 03-CORNELL-STUDY-GUIDE.md      # Master index linking all topics/<nn>-*.md, comparison tables, worked examples, <details> cues
├── 04-GLOSSARY.md                 # Canonical 1-2 sentence definitions + "_Avoid_:" aliases
├── 05-MENTAL-MODELS.md            # Feynman analogies, first-principles axioms, ASCII diagrams, failure modes
├── 06-DERIVATIONS-AND-PROOFS.md   # Step-by-step axiom-to-formula derivations with justifications
├── 07-PRACTICE-PROBLEMS.md        # Tiered quantitative/diagnostic drill problems & solutions
├── 08-FLASHCARDS.md               # Obsidian Spaced Repetition & Anki active-recall + cloze deck
├── 09-CHEAT-SHEET.md              # Distilled 1-page review sheet (/teachme distill)
├── topics/                        # 01-<subtopic-slug>.md ... 1 dedicated full deep-dive per subtopic (no cap)
├── learning-records/              # 000N-<slug>.md ADR-style mastery & misconception logs
└── atomic/                        # Interlinked 150-300 word Zettelkasten cards with [[wikilinks]] (no arbitrary cap)
```
*(Cross-vault comparisons are stored at `~/notes/comparisons/<topic-a-slug>-vs-<topic-b-slug>.md`.)*

---

## Subcommand Router

Route any subcommand invocation directly to its dedicated workflow in `references/SUBCOMMANDS.md` without rebuilding the entire vault from scratch:

| Invocation | Mode | Target Path |
|---|---|---|
| `/teachme <topic>` | **Full Pipeline** | `~/notes/<topic-slug>/` (Runs Phases 1–6, starting with Frontier Grilling) |
| `/teachme <topic> --auto` | **Fast-Track Pipeline** | `~/notes/<topic-slug>/` (Skips Phase 1 grilling with defaults; runs Phases 2–6) |
| `/teachme ingest <path-or-url> into <topic>` | **Source Ingestion & Merge** | `~/notes/<topic-slug>/` |
| `/teachme distill <topic>` | **Executive Cheat Sheet** | `~/notes/<topic-slug>/09-CHEAT-SHEET.md` |
| `/teachme review <topic>` | **Spaced-Repetition Quiz** | `~/notes/<topic-slug>/` |
| `/teachme feynman <topic> [subtopic]` | **Reverse-Teaching Audit** | `~/notes/<topic-slug>/` |
| `/teachme drill <topic> [--tier 1\|2\|3]` | **Problem Generator & Grader** | `~/notes/<topic-slug>/07-PRACTICE-PROBLEMS.md` |
| `/teachme compare <topic-a> vs <topic-b>` | **Cross-Vault Synthesis** | `~/notes/comparisons/<a-vs-b>.md` |
| `/teachme audit <topic>` | **Vault Integrity & Repair** | `~/notes/<topic-slug>/` |

---

## 6-Phase Execution Pipeline

### Phase 1: Frontier Grilling & Mission Lock (`references/MISSION-AND-GRILL.md`)

1. **Check Existing Progress:** Before beginning Frontier Grilling, check whether `~/notes/<topic-slug>/00-MISSION.md` already exists. If it exists, preserve the mission, load the learner's saved state, and resume the appropriate unfinished learning activity. Do not repeat onboarding questions.

2. **Initialize New Learners:** If no saved mission exists, read `references/MISSION-AND-GRILL.md`. Unless `--auto` or `defaults` was provided, ask 3–4 calibrated questions to establish the learner's baseline, target outcome, scope boundaries, and available learning materials.

3. **Save the Mission:** For new learners, create `00-MISSION.md` with observable success criteria and curriculum milestones. Never overwrite an existing mission without explicit user approval.

4. **Resume Safely:** For returning learners, skip completed phases. If stored progress is missing or invalid, explain the issue and preserve existing files rather than silently restarting.


### Phase 2: Primary-Source Research Toolchain & Exhaustive Syllabus (`references/RESEARCH-TOOLCHAIN.md`)
1. Read `references/RESEARCH-TOOLCHAIN.md`.
2. Formulate a falsifiable Research Brief, decompose the subject into a **complete, exhaustive syllabus** covering every topic, subtopic, algorithm, theorem, and mechanism required for full mastery, and execute deep web/primary-source searches.
3. Write `~/notes/<topic-slug>/01-RESOURCES.md` separating **Knowledge** (specs, papers, official docs), **Wisdom** (post-mortems, maintainer talks, practitioner insights), the **Exhaustive Syllabus**, and **Gaps**.
4. Chase primary sources and write `~/notes/<topic-slug>/02-DEEP-RESEARCH.md` with inline `[Source]` citations, internal mechanics, empirical benchmarks, failure modes, a comparative landscape table, and a **Formula Anatomy Breakdown** for every formula.

### Phase 3: First-Principles Mental Models, Glossary & Derivations (`references/STUDY-AND-GLOSSARY.md`)
1. Read `references/STUDY-AND-GLOSSARY.md`.
2. Generate `~/notes/<topic-slug>/05-MENTAL-MODELS.md` containing:
   - Zero-jargon Feynman core analogy (including where the analogy holds and where it breaks).
   - First-principles axiom stack.
   - Clean ASCII architecture and state-transition diagram.
   - Adversarial pre-mortem (how to break it, silent failure modes, and defensive invariants).
3. Generate `~/notes/<topic-slug>/04-GLOSSARY.md` with strict 1-2 sentence definitions of what each canonical term IS, plus `_Avoid_:` lines for overloaded synonyms.
4. Generate `~/notes/<topic-slug>/06-DERIVATIONS-AND-PROOFS.md` deriving every major equation, complexity bound, and theorem step-by-step from base axioms with 1-sentence justifications and cross-references to `topics/*.md` and `04-GLOSSARY.md`.

### Phase 4: Master Cornell Guide, Subtopic Files, MOC Index & Flashcards (`references/STUDY-AND-GLOSSARY.md`)
1. Generate a dedicated, full-length file `~/notes/<topic-slug>/topics/<nn>-<subtopic-slug>.md` for **every single topic and subtopic** in the Phase 2 exhaustive syllabus (no compressing, merging, or skipping), complete with YAML frontmatter, step-by-step mechanics, **Formula Anatomy Breakdowns** for every equation, realistic worked examples, edge cases, `<details>` self-check questions, and navigation footers.
2. Synthesize `00-MISSION.md`, `02-DEEP-RESEARCH.md`, `04-GLOSSARY.md`, `05-MENTAL-MODELS.md`, and all `topics/` files into `~/notes/<topic-slug>/03-CORNELL-STUDY-GUIDE.md`, explicitly linking **every** `[[topics/<nn>-<subtopic-slug>]]` file in its syllabus index and sections, with **Formula Anatomy Breakdowns**, trade-off tables, `<details>` active-recall cues, a 5-bullet synthesis summary, and `## Living Session Notes & Insights`.
3. Generate `~/notes/<topic-slug>/00-MOC-INDEX.md` as the master navigation dashboard with vault header links, a dual-format **Prerequisite & Dependency Graph** (Mermaid `graph TD` + ASCII tree), a complete `topics/` syllabus checklist with difficulty/prereq tags, and an `atomic/` concept index.
4. Generate `~/notes/<topic-slug>/08-FLASHCARDS.md` formatted for Obsidian Spaced Repetition (`#flashcards/<topic-slug>`) and Anki with conceptual/mechanism cards (`::` and `?`) and formula/symbol cloze deletions (`==...==`).

### Phase 5: Atomic Zettelkasten Cards (`references/STUDY-AND-GLOSSARY.md`)
1. Extract standalone atomic concept cards into `~/notes/<topic-slug>/atomic/<concept-slug>.md` covering every key mechanism, theorem, and invariant (no arbitrary cap).
2. Each card must be 150-300 words, include YAML frontmatter (`tags`, `created`, `status: evergreen`, `parent: "[[03-CORNELL-STUDY-GUIDE]]"`), ground terms in `04-GLOSSARY.md`, cite `[Source]`, and interlink via `[[wikilinks]]` under `## Related Concepts`.

### Phase 6: Teach-Before-Test Socratic Loop & Learning Records (`references/RETENTION-AND-RECORDS.md`)
1. Read `references/RETENTION-AND-RECORDS.md`.
2. Present a crisp executive summary (<250 words) in chat and list all created vault files (highlighting `00-MOC-INDEX.md` and `topics/*.md`).
3. **Adaptive Teaching & Assessment:** Read `references/MASTERY-ENGINE.md` and follow the adaptive protocol in `references/RETENTION-AND-RECORDS.md`. For new concepts (M0), teach from first principles using clear explanations, worked examples, and formula breakdowns before asking a guided question. For previously taught concepts (M1–M4), begin with unaided retrieval practice. Evaluate reasoning, adapt difficulty, diagnose misconceptions, and revisit missing prerequisites as needed. Ask one question at a time and require demonstrated evidence before advancing mastery.
   - **Automatic Lesson Position Tracking:** Before beginning or switching to any concept, save the active lesson by running `python3 <skill-root>/scripts/set_current_concept.py <topic-slug> <concept-id>` when filesystem and Python execution are available. Use stable concept IDs from the syllabus. Run this before the first explanation or assessment so unfinished lessons can be resumed. Preserve existing mastery and review data. If the script fails, report the failure and continue teaching without claiming the lesson position was saved.
4. **Calibrate Question 1 to Baseline:** For `0 knowledge` / `Beginner` baselines in `00-MISSION.md`, start Question 1 with a concrete **1-number scalar trace** before any 2D geometry, vectors/matrices, or multi-variable edge cases. For `Intermediate` / `Advanced`, start with a targeted diagnostic or failure-mode prediction.
5. Honor the inline `wait-what` / `simplify` protocol immediately if the user hits friction—re-pitch from scratch using `04-GLOSSARY.md` terms and a 1-number trace, and append the clearer explanation to `05-MENTAL-MODELS.md`.
6. Check off mastered subtopics (`- [x]`) in `00-MOC-INDEX.md`, log breakthroughs/misconceptions/mission shifts in `learning-records/000N-<slug>.md` (`Status: active` or `superseded by LR-000N`), and append user insights to `03-CORNELL-STUDY-GUIDE.md` (`## Living Session Notes & Insights`) and `04-GLOSSARY.md`.
