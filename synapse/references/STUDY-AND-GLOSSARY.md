# Phases 3, 4 & 5 Reference: First-Principles Synthesis, Glossary, Derivations, MOC, Cornell Notes, Subtopic Deep-Dives, Flashcards & Zettelkasten

---

## 1. Phase 3A: First-Principles & Adversarial Models (`05-MENTAL-MODELS.md`)

Combine Feynman translation with divergent-to-convergent first-principles deconstruction, ASCII architecture diagrams, and adversarial pre-mortem inversion:

````markdown
# Mental Models & First-Principles Breakdown: <Topic Title>

## 1. Zero-Jargon Feynman Core
<Explain the entire mechanism in 2-3 paragraphs of plain everyday English using one concrete, physical analogy. Highlight both where the analogy holds and where it breaks down.>

## 2. First-Principles Axiom Stack
Rebuild `<topic>` from irreducible truths:
1. **Axiom 1 (<Fundamental Constraint/Truth>):** <Why this must be true regardless of implementation.>
2. **Axiom 2 (<Derived Necessity>):** <How combining Axiom 1 with the core problem constraint forces the design.>
3. **Axiom 3 (<Architectural Consequence>):** <Why the system takes its canonical shape.>

## 3. System Architecture & Flow Diagram (ASCII)
```text
<Clean ASCII diagram showing components, data/control flow, and state transitions>
```

## 4. Adversarial Pre-Mortem (How to Break It)
Assume the system just caused a catastrophic production outage or subtle data corruption. How did it happen?
1. **Failure Mode 1 (<Name>):**
   - *Trigger:* <Exact condition or workload that triggers the failure>
   - *Blast Radius:* <Silent corruption, latency spike, deadlock, or crash>
   - *Defensive Invariant:* <How to prevent, detect, or mitigate it>
2. **Failure Mode 2 (<Name>):**
   - *Trigger:* <Exact condition or workload>
   - *Blast Radius:* <Impact>
   - *Defensive Invariant:* <Mitigation>
3. **Failure Mode 3 (<Name>):**
   - *Trigger:* <Exact condition or workload>
   - *Blast Radius:* <Impact>
   - *Defensive Invariant:* <Mitigation>
````

---

## 2. Phase 3B: Canonical Domain Glossary (`04-GLOSSARY.md`)

Keep `04-GLOSSARY.md` lean, authoritative, and strictly focused on **what each term IS** (never dump implementation tutorials or usage guides into the glossary):

```markdown
# Canonical Glossary: <Topic Title>

> **Rule:** Every definition is 1-2 sentences stating *what the term IS*. Use the canonical term consistently across all notes and discussions.

- **<Canonical Term 1>:** <1-2 sentence crisp definition stating what the term IS.>
  _Avoid:_ <Sloppy or overloaded synonym/alias to avoid>.
- **<Canonical Term 2>:** <1-2 sentence crisp definition stating what the term IS.>
  _Avoid:_ <Sloppy or overloaded synonym/alias to avoid>.
```

---

## 3. Phase 3C: Step-by-Step Derivations Appendix (`06-DERIVATIONS-AND-PROOFS.md`)

Ensure zero "magic formulas" appear anywhere in the vault by deriving every major equation, complexity bound, and theorem step-by-step from base axioms:

```markdown
# Step-by-Step Derivations & Proofs: <Topic Title>

> **Rule:** Every major equation, complexity bound, and theorem is derived from base axioms with explicit step-by-step justifications.

## 1. Derivation of <Formula / Theorem Name>
- **Target Formula:**
$$
<Target LaTeX Equation>
$$
- **Starting Axioms / Premises:** <Explicit base definitions, axioms, or assumptions from `04-GLOSSARY.md` / `05-MENTAL-MODELS.md`>.
- **Cross-References:** [[topics/<nn>-<subtopic-slug>]] | [[04-GLOSSARY#<term>]]

### Step-by-Step Proof
1. **Step 1:**
   $$<Starting expression>$$
   *Why this holds:* <1-sentence justification>.
2. **Step 2:**
   $$<Intermediate algebraic or logical transition>$$
   *Why this holds:* <1-sentence justification>.
3. **Step 3 (Final Form):**
   $$<Target LaTeX Equation>$$
   *Why this holds:* <1-sentence justification>.
```

---

## 4. Mandatory Formula Anatomy Breakdown Standard (Zero Black-Box Formulas)

**Non-Negotiable Rule:** Across `02-DEEP-RESEARCH.md`, `03-CORNELL-STUDY-GUIDE.md`, and **every** `topics/<nn>-<subtopic-slug>.md` file, **no mathematical formula, equation, recurrence, objective/loss function, or complexity bound** may appear without an immediate **Formula Anatomy Breakdown** following this exact structure:

```markdown
$$
<Display LaTeX Equation>
$$

- **Plain-English Intuition:** <1–2 sentences explaining what the equation actually measures, balances, or optimizes.>

| Symbol / Operator | Name & Exact Role in the Equation | Units / Domain / Shape | Directional Sensitivity |
|---|---|---|---|
| `$x$` | <Name & exact role> | <e.g., $\mathbb{R}^d$, scalar $>0$, bytes> | <What happens to the output when $x$ increases or decreases> |
| `$\sum_{i=1}^{n}$` | <Summation operator over all $n$ items> | <Dimensionless aggregator> | <More terms / larger positive terms increase the sum linearly> |
| ... | ... | ... | ... |

- **Boundary & Limiting Cases:**
  - As `<var> -> 0`: <Exact mathematical & physical/system behavior>.
  - As `<var> -> 1` (if applicable): <Exact behavior>.
  - As `<var> -> \infty`: <Exact behavior / asymptote / saturation>.
- **Worked Numerical Walkthrough:**
  1. **Inputs:** <Concrete, realistic numbers with units/shapes>.
  2. **Substitution:** <Plug numbers step-by-step into the equation>.
  3. **Evaluation & Interpretation:** <Final number + what it means in plain English>.
```

*Every single variable, subscript, superscript, constant, and mathematical operator ($\sum$, $\prod$, $\nabla$, $\log$, $\arg\max$, $\mathbb{E}$, norms, matrices, etc.) in the equation MUST have a row in the Component & Operator Breakdown Table.*

---

## 5. Phase 4A: Master Cornell Study Guide (`03-CORNELL-STUDY-GUIDE.md`)

Synthesize `00-MISSION.md`, `02-DEEP-RESEARCH.md`, `04-GLOSSARY.md`, `05-MENTAL-MODELS.md`, `06-DERIVATIONS-AND-PROOFS.md`, and every `topics/<nn>-<subtopic-slug>.md` file into a comprehensive Markdown study guide. Its syllabus index and sections MUST explicitly link to **every single** `[[topics/<nn>-<subtopic-slug>]]` file created.

````markdown
# Cornell Study Guide: <Topic Title>

- **Date:** <YYYY-MM-DD>
- **Map of Content:** [[00-MOC-INDEX]]
- **Mission:** [[00-MISSION]] | **Research:** [[02-DEEP-RESEARCH]] | **Glossary:** [[04-GLOSSARY]] | **Models:** [[05-MENTAL-MODELS]] | **Derivations:** [[06-DERIVATIONS-AND-PROOFS]] | **Flashcards:** [[08-FLASHCARDS]]
- **Executive Thesis:** <2-sentence synthesis capturing the core mechanism and why it matters.>

---

## Complete Syllabus Index
> Every subtopic below has a dedicated, full-length deep-dive file in `topics/`.

1. [[topics/01-<subtopic-slug>]] — <1-line summary of what this subtopic covers>
2. [[topics/02-<subtopic-slug>]] — <1-line summary>
...
NN. [[topics/<nn>-<subtopic-slug>]] — <1-line summary>

---

## 1. <Milestone 1 Title>
*Deep-dive files:* [[topics/01-<subtopic-slug>]], [[topics/02-<subtopic-slug>]]

<Thorough, structured explanation using **bold terms** from `04-GLOSSARY.md` on first appearance, bullet points, and inline [Source] citations. Any formula here MUST include its full Formula Anatomy Breakdown.>

### Worked Example / Annotated Code
```<language>
// Concrete, realistic, annotated example (never foo/bar placeholders)
```

### Active-Recall Cue Questions (Milestone 1)
- **Cue 1:** <Diagnostic or mechanism-tracing question?>
  <details><summary>Reveal Answer</summary>
  <Crisp, complete answer grounded in first principles and primary sources.>
  </details>
- **Cue 2:** <Edge-case or failure-prediction question?>
  <details><summary>Reveal Answer</summary>
  <Crisp, complete answer explaining what breaks and why.>
  </details>

---

## 2. <Milestone 2 Title>
*Deep-dive files:* [[topics/03-<subtopic-slug>]], ...

<Thorough, structured explanation of internal architecture, state transitions, and invariants [Source], with Formula Anatomy Breakdowns for any equations.>

### Active-Recall Cue Questions (Milestone 2)
- **Cue 1:** <Why does invariant X hold under condition Y?>
  <details><summary>Reveal Answer</summary>
  <Complete explanation.>
  </details>

---

## 3. Trade-Offs, Edge Cases & Comparative Matrix
| Criterion | <Topic> | <Alternative A> | <Alternative B> |
|---|---|---|---|
| **Mechanism** | ... | ... | ... |
| **Latency / Throughput** | ... | ... | ... |
| **Failure Mode** | ... | ... | ... |
| **When to Choose** | ... | ... | ... |

### Active-Recall Cue Questions (Milestone 3 & 4)
- **Cue 1:** <Scenario-based design trade-off question?>
  <details><summary>Reveal Answer</summary>
  <Complete trade-off analysis.>
  </details>

---

## Cornell Summary Synthesis (Bottom-Line Takeaways)
1. **Core Problem Solved:** <1-sentence takeaway>
2. **Key Architectural Mechanism:** <1-sentence takeaway>
3. **Critical Invariant:** <1-sentence takeaway>
4. **Sharpest Edge / Failure Mode:** <1-sentence takeaway>
5. **Decision Rule:** <When to use `<topic>` vs. when to reach for an alternative.>

---

## Living Session Notes & Insights
- *[<YYYY-MM-DD>]* <Initial vault synthesis completed. Ongoing Socratic insights, war stories, and follow-up Q&A are appended here automatically.>
````

---

## 6. Phase 4B: Dedicated Per-Subtopic Deep-Dive Files (`topics/<nn>-<subtopic-slug>.md`)

For **every single topic and subtopic** in the Phase 2 exhaustive syllabus (no arbitrary file cap; never compress, merge, or skip subtopics), generate a full-length, standalone Markdown file inside `~/notes/<topic-slug>/topics/<nn>-<subtopic-slug>.md` numbered sequentially (`01-...`, `02-...`, etc.):

````markdown
---
topic: "<Topic Title>"
subtopic: "<Subtopic Title>"
order: <nn>
prerequisites:
  - "[[<prereq-subtopic-or-none>]]"
parent: "[[03-CORNELL-STUDY-GUIDE]]"
---

# <nn>. <Subtopic Title>

## 1. Core Concept & Why It Exists
<First-principles intuition, what bottleneck or problem this subtopic solves, **bolded canonical terms** from `04-GLOSSARY.md`, and inline [Source] citations.>

## 2. Internal Mechanics & Step-by-Step Walkthrough
<Complete technical breakdown with zero hand-waving: exact data structures, state transitions, control flow, and invariants [Source].>

## 3. Mathematical Formulations & Complete Formula Anatomy
<Every formula, recurrence, objective/loss function, or complexity bound for this subtopic rendered in `$$...$$` and immediately followed by its full **Formula Anatomy Breakdown** (Plain-English Intuition, Component & Operator Breakdown Table for every symbol/operator, Boundary & Limiting Cases, and Worked Numerical Walkthrough). If a purely non-mathematical subtopic has no equations, explicitly note "No formal equations govern this mechanism" and provide exact complexity/capacity bounds with full breakdown if applicable.>

## 4. Worked Examples / Annotated Code
```<language>
// Realistic, end-to-end annotated example (never foo/bar placeholders)
```

## 5. Edge Cases, Failure Modes & Trade-offs
- **Edge Case / Failure Mode 1:** <Trigger, blast radius, and mitigation> [Source].
- **Trade-offs:** <What this design optimizes for vs. what it sacrifices>.

## 6. Subtopic Self-Check Questions
- **Question 1:** <Diagnostic, mechanism-tracing, or failure-prediction question?>
  <details><summary>Reveal Answer</summary>
  <Complete answer grounded in first principles and primary sources.>
  </details>
- **Question 2:** <Transfer or edge-case question?>
  <details><summary>Reveal Answer</summary>
  <Complete answer.>
  </details>

---
**Navigation:** ← [[<prev-subtopic>|Previous]] | [[03-CORNELL-STUDY-GUIDE|Study Guide]] | [[<next-subtopic>|Next]] →
````

---

## 7. Phase 4C: Master Map of Content (`00-MOC-INDEX.md`)

Create `~/notes/<topic-slug>/00-MOC-INDEX.md` as the central navigation dashboard so Obsidian and Markdown navigation stays effortless regardless of vault size:

````markdown
# Map of Content (MOC): <Topic Title>

## Vault Navigation
- [[00-MISSION]] — Target outcome, success criteria & scope boundaries
- [[01-RESOURCES]] — Primary Knowledge, practitioner Wisdom, exhaustive syllabus & gaps
- [[02-DEEP-RESEARCH]] — Primary-source research dossier & benchmarks
- [[03-CORNELL-STUDY-GUIDE]] — Master synthesized study guide
- [[04-GLOSSARY]] — Canonical 1–2 sentence domain definitions
- [[05-MENTAL-MODELS]] — Feynman analogies, axioms, ASCII architecture & pre-mortem
- [[06-DERIVATIONS-AND-PROOFS]] — Step-by-step axiom-to-formula derivations
- [[07-PRACTICE-PROBLEMS]] — Applied problem sets & scenarios (if generated)
- [[08-FLASHCARDS]] — Spaced-repetition & cloze active-recall deck
- [[09-CHEAT-SHEET]] — Distilled 1-page executive cheat sheet (via `/teachme distill`)

---

## Comparisons
- <Cross-vault comparisons linked here automatically by `/teachme compare`, e.g. `[[../comparisons/<topic-a>-vs-<topic-b>]]`>

---

## Prerequisite & Dependency Graph

```mermaid
graph TD
  T01["01: <Subtopic A>"] --> T02["02: <Subtopic B>"]
  T02 --> T03["03: <Subtopic C>"]
```

### ASCII Dependency Tree (Plain-Text Fallback)
```text
01: <Subtopic A>
└── 02: <Subtopic B>
    └── 03: <Subtopic C>
```

---

## Complete Subtopic Syllabus Tracker (`topics/`)
> Check off `- [x]` as each subtopic is mastered during Phase 6.

- [ ] **01.** [[topics/01-<subtopic-slug>]] `[Beginner]` — *Prereqs: None*
- [ ] **02.** [[topics/02-<subtopic-slug>]] `[Intermediate]` — *Prereqs: [[topics/01-<subtopic-slug>]]*
- [ ] **03.** [[topics/03-<subtopic-slug>]] `[Advanced]` — *Prereqs: [[topics/02-<subtopic-slug>]]*

---

## Atomic Zettelkasten Concept Index (`atomic/`)
- [ ] [[atomic/<concept-slug-1>]] `[Beginner]` — *Parent:* [[topics/01-<subtopic-slug>]]
- [ ] [[atomic/<concept-slug-2>]] `[Intermediate]` — *Parent:* [[topics/02-<subtopic-slug>]]
````

---

## 8. Phase 4D: Spaced-Repetition Cloze & Flashcard Deck (`08-FLASHCARDS.md`)

Generate `~/notes/<topic-slug>/08-FLASHCARDS.md` formatted cleanly for **Obsidian Spaced Repetition** (`#flashcards/<topic-slug>`) and **Anki** import:

```markdown
# Spaced-Repetition Flashcards: <Topic Title>

#flashcards/<topic-slug>

## 1. Conceptual & Mechanism Cards

<Single-line question testing an invariant, trade-off, or failure mode> :: <Crisp, exact answer>

<Multi-line diagnostic question>
?
<Complete, structured answer grounded in `04-GLOSSARY.md` and `05-MENTAL-MODELS.md`.>

---

## 2. Formula & Symbol Cloze Cards

For `<Formula Name>` ($$<Equation>$$): the term ==`<symbol>`== represents ==<exact name, role, and units>==; as ==`<symbol>`== $\to \infty$, the output ==<limiting behavior>==.

For `<Formula Name>`: increasing ==`<variable>`== causes the output to ==<increase / decrease / saturate>== because ==<1-clause mathematical reason>==.
```

---

## 9. Phase 5: Atomic Zettelkasten Cards (`atomic/`)

Create standalone Markdown cards inside `~/notes/<topic-slug>/atomic/<concept-slug>.md` for every key mechanism, theorem, invariant, and failure mode (no arbitrary card cap). Each card must express **one atomic concept** in 150-300 words so it is reusable across vaults:

```markdown
---
tags:
  - <topic-slug>
  - evergreen
created: <YYYY-MM-DD>
status: evergreen
parent: "[[03-CORNELL-STUDY-GUIDE]]"
---

# <Atomic Concept Title>

<150-300 words explaining this single concept clearly in your own words, grounded in 04-GLOSSARY.md terminology and citing primary sources [Source]. Include a brief concrete example or invariant.>

## Related Concepts
- [[<sibling-concept-1>]] — <Explicit explanation of how or why it connects (e.g., "Enforces the invariant required by...")>
- [[<sibling-concept-2>]] — <Explicit explanation of dependency or contrast>
```
