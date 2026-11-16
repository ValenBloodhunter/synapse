# `/synapse` — Primary-Source Research & Mastery Agent Skill

An AI agent skill (`/synapse`) that deeply researches any topic from primary sources, builds a complete, interlinked Obsidian/Markdown study vault at `~/notes/<topic-slug>/`, and teaches it to you step by step from first principles.

Works out of the box with **Claude Code**, **Cursor**, **Windsurf**, **Antigravity**, **Cline**, **Codex**, and any `SKILL.md`-compatible AI coding or research assistant.

---

## Why `/synapse`?

Standard LLM explanations dump a wall of text you forget five minutes later. `/synapse` acts as an end-to-end learning OS:

1. **Frontier Grilling First:** Starts every new session with 3–4 calibrated `❓` questions (with `➡️` defaults) to lock your baseline, concrete goal, and scope boundaries before researching.
2. **Primary-Source Research Toolchain:** Separates vetted **Knowledge** (RFCs, papers, official docs, textbooks) from practitioner **Wisdom** (post-mortems, talks, benchmarks) and logs unresolved gaps explicitly.
3. **Zero-Omission Subtopic Files:** Generates a dedicated deep-dive `.md` file inside `topics/` for **every** subtopic in topological prerequisite order—no arbitrary caps or skipped sections.
4. **Complete Formula Anatomy:** Every equation is broken down symbol-by-symbol (variables, subscripts, operators, units/domain, directional sensitivity, edge cases, and a worked numerical walkthrough) alongside step-by-step derivations from axioms.
5. **Obsidian-Ready Central Vault:** Outputs a Master Map of Content (`00-MOC-INDEX.md` with Mermaid + ASCII dependency graphs), Cornell study notes, atomic Zettelkasten cards (`atomic/`), graded practice problems, spaced-repetition flashcards (`08-FLASHCARDS.md`), and ADR-style `learning-records/`.
6. **Teach-Before-Test Socratic Loop:** Explains each subtopic thoroughly in chat (including every formula component) before quizzing you, starts 0-knowledge beginners with a concrete 1-number trace, and includes an inline `wait what` / `simplify` escape hatch.

---

## Generated Vault Architecture

Every `/synapse <topic>` run creates and maintains a pure-Markdown vault inside `~/notes/<topic-slug>/`:

```text
~/notes/<topic-slug>/
├── 00-MOC-INDEX.md                # Master Map of Content, Mermaid + ASCII dependency graph & checkboxes
├── 00-MISSION.md                  # Target outcome, success criteria, milestones & scope boundaries
├── 01-RESOURCES.md                # Primary sources (Knowledge), practitioner signal (Wisdom) & Gaps
├── 02-DEEP-RESEARCH.md            # Primary-source cited research dossier with full formula anatomy
├── 03-CORNELL-STUDY-GUIDE.md      # Master synthesis notes & <details> active-recall cues
├── 04-GLOSSARY.md                 # Crisp 1–2 sentence definitions + "_Avoid_:" aliases
├── 05-MENTAL-MODELS.md            # Feynman analogies, first-principles axioms & failure pre-mortems
├── 06-DERIVATIONS-AND-PROOFS.md   # Step-by-step algebraic & logical derivations from base axioms
├── 07-PRACTICE-PROBLEMS.md        # Graded Tier 1–3 problems with hidden step-by-step solutions
├── 08-FLASHCARDS.md               # Obsidian Spaced Repetition / Anki-ready Q&A & cloze cards
├── 09-CHEAT-SHEET.md              # Single-page executive cheat sheet (generated via /synapse distill)
├── topics/                        # Dedicated deep-dive .md file for EVERY subtopic
├── atomic/                        # Interlinked evergreen Zettelkasten cards ([[wikilinks]])
└── learning-records/              # ADR-style chronological mastery & misconception logs
```

---

## Installation

Clone this repository and copy `skills/synapse` into your AI tool's global or project-local skills directory:

```bash
git clone https://github.com/ValenBloodhunter/synapse.git
cd synapse
```

| Agent / Tool | Global Skills Path | Project-Local Path |
|---|---|---|
| **Claude Code** | `~/.claude/skills/synapse/` | `.claude/skills/synapse/` |
| **Cursor** | `~/.cursor/skills/synapse/` | `.cursor/skills/synapse/` |
| **Antigravity / Gemini** | `~/.gemini/antigravity/skills/synapse/` | `.agent/skills/synapse/` |
| **Codex / Generic Agents** | `~/.agents/skills/synapse/` | `.agents/skills/synapse/` |

### Quick Install Examples

```bash

# Claude Code (Global)
mkdir -p ~/.claude/skills/synapse
cp -r synapse/* ~/.claude/skills/synapse/

# Cursor (Global)
mkdir -p ~/.cursor/skills/synapse
cp -r synapse/* ~/.cursor/skills/synapse/


# Antigravity
./install.sh
```

---

## Commands & Lifecycle Workflows

Open a new session in your agent and invoke `/synapse`:

### Core Learning & Vault Creation
| Command | What It Does |
|---|---|
| `/synapse <topic>` | Starts Phase 1 Frontier Grilling, builds the full vault at `~/notes/<topic-slug>/`, teaches Subtopic 1 in detail, and starts the Socratic quiz loop. |
| `/synapse <topic> --auto` | Skips Phase 1 grilling using sensible defaults and builds the complete vault immediately. |
| `wait what` / `simplify` | Pauses quizzing during Phase 6, re-explains the sticking point from scratch using a 1-number trace, and saves the clearer analogy to `05-MENTAL-MODELS.md`. |

### Ingestion, Retention & Synthesis Subcommands
| Command | What It Does |
|---|---|
| `/synapse ingest <path-or-url> into <topic>` | Parses a PDF, paper, YouTube transcript, GitHub repo, or raw notes; extracts new claims & formulas with inline citations; updates `topics/` & `00-MOC-INDEX.md`; and flags contradictions against existing notes. |
| `/synapse distill <topic>` | Compresses an entire multi-file vault into a single-page executive cheat sheet (`09-CHEAT-SHEET.md`) with core invariants, critical formulas, and failure modes. |
| `/synapse review <topic>` | Scans `00-MOC-INDEX.md` and `learning-records/` for unchecked subtopics or past misconceptions and runs a targeted spaced-repetition quiz without regenerating the vault. |
| `/synapse feynman <topic> [subtopic]` | Flips the roles: asks *you* to explain a concept and its formulas in plain English, grades your explanation for hidden jargon or skipped steps, and logs progress to `learning-records/`. |
| `/synapse drill <topic> [--tier 1\|2\|3]` | Generates fresh quantitative or diagnostic edge-case problems, grades your step-by-step math/reasoning, and appends solved problems to `07-PRACTICE-PROBLEMS.md`. |
| `/synapse compare <topic-a> vs <topic-b>` | Cross-reads two vaults (or researches a challenger), generates a side-by-side Trade-Off & Architecture Matrix at `~/notes/comparisons/<a-vs-b>.md`, and links both MOC indexes. |
| `/synapse audit <topic>` | Checks an existing vault for missing `topics/*.md` files, formulas lacking symbol-by-symbol breakdowns, or broken `[[wikilinks]]`, and repairs them in place. |

*(If your agent does not support `/slash` skill commands natively, prompt: `"Use the synapse skill to research and teach me <topic>."`)*

---

## Repository Structure

```text
synapse-skill/
├── README.md
├── LICENSE
├── install.sh
└── synapse/
    ├── SKILL.md                       # Master router, operating laws & 6-phase state machine
    └── references/
        ├── MISSION-AND-GRILL.md       # Frontier grilling protocol & 00-MISSION.md template
        ├── RESEARCH-TOOLCHAIN.md      # Knowledge vs. Wisdom sourcing & primary-source chaser
        ├── STUDY-AND-GLOSSARY.md      # Formula anatomy, MOC index, Cornell guide, derivations & flashcards
        ├── RETENTION-AND-RECORDS.md   # Teach-before-test Socratic loop, wait-what & ADR learning records
        └── SUBCOMMANDS.md             # Workflows & templates for ingest, distill, review, feynman, drill, compare & audit
```

---

## Acknowledgments

Inspired by workflow patterns from [`mattpocock/skills`](https://github.com/mattpocock/skills), [`rohankgeorge/the-researcher`](https://github.com/rohankgeorge/the-researcher), and [`rohankgeorge/thinking-tools`](https://github.com/rohankgeorge/thinking-tools).

## License

MIT
