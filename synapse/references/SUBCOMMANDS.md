# Subcommand Router Reference: Lifecycle, Ingestion, Retention & Synthesis Commands

When invoked with a subcommand, execute its dedicated workflow directly without rebuilding the entire vault from scratch. All outputs remain 100% pure Markdown inside `~/notes/` and strictly enforce **Zero Black-Box Formulas** (Mandatory Formula Anatomy Breakdown) and **Teach-Before-Test**.

---

## A. Ingestion & Source-Driven Commands

### 1. `/teachme ingest <path-or-url> into <topic>` (Source Ingestion & Merge)

1. **Read Existing Vault First:** Load `00-MOC-INDEX.md`, `01-RESOURCES.md`, `02-DEEP-RESEARCH.md`, and `04-GLOSSARY.md` inside `~/notes/<topic-slug>/`. If the vault does not exist yet, initialize it first (using Phase 1 defaults if `--auto` or after a quick Mission Lock).
2. **Extract & Verify:** Parse the provided local file (PDF, lecture notes, code, transcript) or URL (research paper, YouTube transcript, GitHub repository, official docs). Extract every new claim, mechanism, benchmark, and mathematical equation with inline `[Source]` citations.
3. **Apply Mandatory Formula Anatomy:** For every new formula extracted, generate the complete Formula Anatomy Breakdown (`$$...$$`, Plain-English Intuition, 4-column Component & Operator Breakdown Table, Boundary & Limiting Cases, and Worked Numerical Walkthrough).
4. **Update Vault Files:**
   - Add the source under `## Knowledge` or `## Wisdom` in `01-RESOURCES.md`.
   - Append synthesized findings to `02-DEEP-RESEARCH.md` and `03-CORNELL-STUDY-GUIDE.md`.
   - Generate new dedicated `topics/<nn>-<subtopic-slug>.md` files for any newly uncovered subtopics and register them in `00-MOC-INDEX.md` (updating both the Mermaid `graph TD` and ASCII dependency tree).
   - Add any new canonical terms to `04-GLOSSARY.md` (strictly 1–2 sentences stating what each term IS + `_Avoid_:` aliases).
5. **Contradiction Detection:** Explicitly flag any claims, benchmarks, or definitions in the ingested source that conflict with existing vault notes under a `## Contradictions & Version Deltas` alert block in `02-DEEP-RESEARCH.md` and report them in chat:

```markdown
## Contradictions & Version Deltas
> [!WARNING] Conflict Detected — [<Source Title>] vs. Existing Vault Notes
> - **Topic / Claim:** <Exact mechanism, benchmark, or definition>
> - **Existing Vault Claim:** <What the vault currently states> [Existing Source]
> - **Newly Ingested Claim:** <What the new source states> [New Source]
> - **Resolution / Context:** <Version difference, workload assumption, or unresolved open question>
```

---

### 2. `/teachme distill <topic>` (Executive Cheat Sheet)

1. **Read Full Vault:** Scan `00-MOC-INDEX.md`, `02-DEEP-RESEARCH.md`, `03-CORNELL-STUDY-GUIDE.md`, `04-GLOSSARY.md`, `05-MENTAL-MODELS.md`, and `topics/*.md` inside `~/notes/<topic-slug>/`.
2. **Generate `~/notes/<topic-slug>/09-CHEAT-SHEET.md`:** Compress the entire topic into a high-density, single-page last-minute review sheet containing ONLY these 4 sections:

```markdown
# Executive Cheat Sheet: <Topic Title>

- **Vault:** [[00-MOC-INDEX]] | **Study Guide:** [[03-CORNELL-STUDY-GUIDE]] | **Glossary:** [[04-GLOSSARY]]

## 1. Core Axioms & Invariants
1. **<Axiom / Invariant 1>:** <1-sentence non-negotiable truth>.
2. ... (5–8 total)

## 2. Critical Formula Reference Table
| Formula Name | Equation | Compact Symbol Key | Limiting Behavior |
|---|---|---|---|
| **<Name>** | `$$...$$` | `$x$: ...; $y$: ...` | As $x \to 0$: ...; as $x \to \infty$: ... |

## 3. Decision & Trade-Off Matrix
| Scenario / Requirement | Choose `<Topic>` When... | Avoid `<Topic>` / Choose Alternative When... |
|---|---|---|
| **<Dimension 1>** | ... | ... |

## 4. Top Failure Modes & Gotchas
| Symptom | Root Cause | Immediate Fix / Invariant |
|---|---|---|
| **<Symptom 1>** | <Exact mechanism that broke> | <Preventive invariant or mitigation> |
```

3. **Link in MOC:** Ensure `[[09-CHEAT-SHEET]]` is linked in the Vault Navigation header of `~/notes/<topic-slug>/00-MOC-INDEX.md`.

---

## B. Retention & Active-Recall Commands

### 3. `/teachme review <topic>` (Spaced-Repetition Quiz)

1. **Scan State (Read-Only on Notes):** Read `00-MOC-INDEX.md` (looking for unchecked `- [ ]` subtopics), `learning-records/` (looking for past misconceptions or `superseded` records), and `08-FLASHCARDS.md`. Do NOT regenerate or overwrite existing vault notes.
2. **Teach-Before-Test & ZPD Quiz:** Briefly recap the weakest or next unchecked subtopic in topological order—including plain-English mechanics and a full component breakdown of any formulas involved—then run a targeted spaced-repetition Socratic quiz **one question at a time** (respecting Beginner-Safe 1-number scalar traces for `0 knowledge` / `Beginner` baselines).
3. **Persist Progress:** Check off mastered subtopics (`- [x]`) in `00-MOC-INDEX.md` and log breakthroughs or corrected gaps in `learning-records/000N-<slug>.md`.

---

### 4. `/teachme feynman <topic> [subtopic]` (Reverse-Teaching Audit)

1. **Role Reversal:** Pick the specified `[subtopic]` (or the next unchecked subtopic in `00-MOC-INDEX.md`) and prompt the user to explain the concept—and its core formula(s)—from scratch in plain English as if teaching a complete beginner.
2. **Strict 4-Axis Grading Rubric:** Wait for the user's explanation, then evaluate it across:
   1. **Plain-English Clarity:** Did they explain without hiding behind unstated jargon instead of `04-GLOSSARY.md` definitions?
   2. **First-Principles Accuracy:** Are the causal steps and invariants sound?
   3. **Formula Intuition:** Did they accurately explain what each variable, subscript, and operator does?
   4. **Edge-Case Awareness:** Did they note where the intuition or analogy breaks down?
3. **Patch & Record:** Point out exact gaps gently, provide a refined model explanation if needed, save the session outcome to `~/notes/<topic-slug>/learning-records/000N-feynman-<slug>.md`, and check off `- [x]` in `00-MOC-INDEX.md` if passed.

---

### 5. `/teachme drill <topic> [--tier 1|2|3]` (Problem Generator & Grader)

1. **Read Existing Problems:** Check `~/notes/<topic-slug>/07-PRACTICE-PROBLEMS.md` (if it exists) so no duplicate problems are generated.
2. **Generate Fresh Problems:** Create 1–3 new quantitative or diagnostic problems calibrated to the requested tier (defaulting to the user's current ZPD tier if `--tier` is omitted):
   - **Tier 1:** Direct formula substitution & symbol sensitivity.
   - **Tier 2:** Multi-step derivation or cross-subtopic synthesis.
   - **Tier 3:** Adversarial edge cases, failure diagnosis, and boundary limits ($\to 0$, $\to \infty$).
3. **Interactive Grading & Persistence:** Present **one problem at a time** in chat, grade the user's step-by-step math and reasoning, and append all newly solved problems with full step-by-step solutions into `~/notes/<topic-slug>/07-PRACTICE-PROBLEMS.md`:

```markdown
## Problem <N> [Tier <1|2|3>] — <Subtopic Title>
- **Prompt:** <Concrete quantitative or diagnostic problem statement>
- **Step-by-Step Solution:**
  1. <Formula / setup with variable values>
  2. <Intermediate calculation / reasoning>
  3. **Final Answer & Interpretation:** <Result + plain-English meaning>
```

---

## C. Synthesis & Applied Mastery Commands

### 6. `/teachme compare <topic-a> vs <topic-b>` (Cross-Vault Synthesis)

1. **Cross-Vault & Primary-Source Lookup:** Check if `~/notes/<topic-a-slug>/` and `~/notes/<topic-b-slug>/` already exist in the central vault. For whichever vault is missing, run targeted primary-source research (Phase 2) first so all claims are grounded.
2. **Generate `~/notes/comparisons/<topic-a-slug>-vs-<topic-b-slug>.md`:**

```markdown
# Comparison: <Topic A> vs. <Topic B>

- **Vault A:** [[../<topic-a-slug>/00-MOC-INDEX|<Topic A>]] | **Vault B:** [[../<topic-b-slug>/00-MOC-INDEX|<Topic B>]]

## 1. Executive Verdict & Selection Rule
- **Choose <Topic A> when:** <Concrete workload, scale, or invariant conditions>.
- **Choose <Topic B> when:** <Concrete workload, scale, or invariant conditions>.

## 2. Side-by-Side Architecture & Mechanics Matrix
| Dimension | <Topic A> | <Topic B> |
|---|---|---|
| **Core Mechanism** | ... [Source] | ... [Source] |
| **Time / Space / Network Complexity** | `$$...$$` (with symbol key) | `$$...$$` (with symbol key) |
| **Consistency / Guarantees** | ... | ... |
| **Operational Overhead** | ... | ... |
| **Primary Failure Modes** | ... | ... |

## 3. Mathematical & Quantitative Contrast
<Compare governing equations, bounds, or objective functions side-by-side with complete symbol keys and crossover points.>

## 4. Migration, Hybrid Patterns & Pitfalls
- **Migrating A → B / B → A:** <Key impedance mismatches and hidden costs>.
- **Hybrid Pattern:** <When and how they compose together>.
```

3. **Bidirectional Linking:** Add a `## Comparisons` section with `[[../comparisons/<topic-a-slug>-vs-<topic-b-slug>]]` inside both `00-MOC-INDEX.md` files (where those vaults exist).

---

### 7. `/teachme audit <topic>` (Vault Integrity & Repair)

1. **Comprehensive Vault Inspection:** Scan every file inside `~/notes/<topic-slug>/` and check:
   1. **Subtopic Completeness:** Every subtopic listed in `00-MOC-INDEX.md` and `03-CORNELL-STUDY-GUIDE.md` has a corresponding, non-empty `topics/<nn>-<subtopic-slug>.md` file.
   2. **Formula Anatomy Completeness:** Every mathematical formula across `02-DEEP-RESEARCH.md`, `03-CORNELL-STUDY-GUIDE.md`, and `topics/*.md` has a complete component-by-component Formula Anatomy breakdown (no unexplained symbols or operators).
   3. **Wikilink Integrity:** All `[[wikilinks]]` across `00-MOC-INDEX.md`, `topics/*.md`, and `atomic/*.md` resolve to real files on disk.
   4. **Source Provenance:** `01-RESOURCES.md` has primary-source citations and no unlogged gaps.
2. **Auto-Repair & Report:**
   - Print a concise **Pass/Fail audit table** in chat.
   - Automatically generate any missing `topics/*.md` files, patch any incomplete Formula Anatomy blocks, and fix broken `[[wikilinks]]`.
   - Re-verify and confirm once the vault passes 100%.
