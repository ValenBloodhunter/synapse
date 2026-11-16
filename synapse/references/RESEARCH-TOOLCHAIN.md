# Phase 2 Reference: Primary-Source Research Toolchain

Combine rigorous research scoping, exhaustive syllabus decomposition, source-tier separation (`Knowledge` vs. `Wisdom`), primary-source chasing, and mandatory **Formula Anatomy Breakdowns** so zero hallucinated, shallow, or black-box content enters the vault.

---

## 1. Research Brief & Exhaustive Syllabus Decomposition
Before executing web searches or reading files, define a structured **Research Brief** at the top of `01-RESOURCES.md`:
- **Core Research Questions (4-6+):** Specific, falsifiable questions aligned with `00-MISSION.md` milestones.
- **Exhaustive Syllabus Decomposition (No Caps):** Decompose `<topic>` into a complete, numbered syllabus covering **every single topic, subtopic, algorithm, theorem, and mechanism** required for full mastery. Never compress, merge, or skip subtopics to save space. Every item in this syllabus will become a dedicated `topics/<nn>-<subtopic-slug>.md` file in Phase 4.
- **Inclusion Criteria:** Canonical specs, RFCs, peer-reviewed papers, official documentation, benchmarks with reproducible methodology, post-mortems from primary authors.
- **Exclusion Criteria:** SEO listicles, AI-generated summaries, undated tutorials without version numbers, unverified claims.

---

## 2. Source Hierarchy: Knowledge vs. Wisdom

Organize all discovered sources inside `~/notes/<topic-slug>/01-RESOURCES.md` into two distinct buckets plus the exhaustive syllabus and an explicit gap log:

- **Knowledge (Primary & Authoritative):** Official documentation, RFCs/standards, academic papers, canonical textbooks, source code repositories, release notes.
- **Wisdom (High-Signal Practitioner Experience):** Engineering post-mortems, talks by creators/maintainers, vetted community discussions (Hacker News, GitHub Issues, specialized forums) highlighting real-world sharp edges.
- **Exhaustive Syllabus:** Numbered list (`01` .. `NN`) of every subtopic to be researched in `02-DEEP-RESEARCH.md` and written to `topics/<nn>-<subtopic-slug>.md`.
- **Gaps:** Specific questions where primary sources conflict, are paywalled/unavailable, or lack empirical benchmarks.

### Template: `~/notes/<topic-slug>/01-RESOURCES.md`

```markdown
# Research Resources & Provenance Index: <Topic Title>

## Research Brief
- **Mission Alignment:** <Link to target outcome in 00-MISSION.md>
- **Core Questions:**
  1. <Question 1>
  2. <Question 2>
  3. <Question 3>
  4. <Question 4>
- **Inclusion / Exclusion:** Prioritize primary specs, official docs, and empirical benchmarks; exclude derivative blog summaries.

## Exhaustive Syllabus (1 Subtopic = 1 `topics/<nn>-<subtopic-slug>.md` File)
1. `01-<subtopic-slug>` — <Subtopic Title & scope>
2. `02-<subtopic-slug>` — <Subtopic Title & scope>
...
NN. `<nn>-<subtopic-slug>` — <Subtopic Title & scope>

## Knowledge (Primary Sources)
1. **[<Source Title>](<URL>)** — *Type: Official Spec / Paper / Docs* — Covers: <specific mechanism or claim>.
2. **[<Source Title>](<URL>)** — *Type: Canonical Reference* — Covers: <specific mechanism or claim>.

## Wisdom (Practitioner & Community Signal)
1. **[<Source Title>](<URL>)** — *Type: Post-Mortem / Maintainer Talk* — Covers: <real-world failure mode or operational trade-off>.

## Gaps & Unverified Claims
- **Gap 1:** <What could not be verified from primary sources and why.>
```

---

## 3. Primary-Source Chasing & Deep Research Dossier (`02-DEEP-RESEARCH.md`)

Never cite a secondary blog post when the primary paper, RFC, or source code is reachable. Trace every claim back to its origin and document exact mechanisms, invariants, benchmarks, and conflicts in `~/notes/<topic-slug>/02-DEEP-RESEARCH.md`.

### Mandatory Rule: Zero Black-Box Formulas
Every mathematical formula, equation, recurrence, objective/loss function, or complexity bound in `02-DEEP-RESEARCH.md` MUST be rendered in display LaTeX (`$$...$$`) and immediately followed by a complete **Formula Anatomy Breakdown** (see `references/STUDY-AND-GLOSSARY.md` §3 for the exact schema: Plain-English Intuition, Component & Operator Breakdown Table covering every variable/subscript/superscript/constant/operator, Boundary & Limiting Cases, and Worked Numerical Walkthrough).

### Template: `~/notes/<topic-slug>/02-DEEP-RESEARCH.md`

```markdown
# Deep Primary-Source Research Dossier: <Topic Title>

## 1. Origin & Problem Statement
- **Historical Context & Catalyst:** <What existed before, why it was created, and the exact bottleneck it solved> [Source].
- **Core Design Constraints:** <Fundamental constraints that shaped its architecture> [Source].

## 2. Architecture & Internal Mechanics
- **System Components:** <Detailed breakdown of each component and its responsibility> [Source].
- **Execution Flow / Lifecycle:** <Exact step-by-step mechanics under the hood> [Source].
- **Invariants & Guarantees:** <What the system strictly guarantees and under what preconditions> [Source].

## 3. Mathematical Formulations & Complexity Bounds
<Every equation, recurrence, objective function, or bound rendered in `$$...$$` and immediately followed by its full Formula Anatomy Breakdown (Plain-English Intuition, Component & Operator Breakdown Table, Boundary & Limiting Cases, Worked Numerical Walkthrough) [Source].>

## 4. Empirical Benchmarks, Trade-offs & Failure Modes
- **Complexity & Performance Characteristics:** <Verified time/space/network bounds and benchmarks> [Source].
- **Where It Breaks (Edge Cases & Failure Modes):** <Specific conditions causing correctness bugs, operational pain, or performance degradation> [Source].

## 5. Comparative Landscape
| Dimension | <Topic> | <Alternative A> | <Alternative B> |
|---|---|---|---|
| **Core Mechanism** | ... [Source] | ... [Source] | ... [Source] |
| **Primary Strength** | ... | ... | ... |
| **Critical Weakness** | ... | ... | ... |
| **Best-Fit Scenario** | ... | ... | ... |

## 6. Contested Claims & Open Questions
- <Any conflicting benchmarks, version differences, or unresolved edge cases discovered during research.>
```
