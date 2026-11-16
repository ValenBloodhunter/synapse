# Phase 1 Reference: Frontier Grilling & Mission Lock

## 1. Dependency-Tree Frontier Grilling Protocol

Never dump a 10-question form on the user, and never ask questions you can answer yourself via research.

### Step A: Separate Facts from Decisions
- **Facts (Agent Responsibility):** Technical specs, history, benchmarks, standard architectures, best practices. *Never ask the user about facts—research them in Phase 2.*
- **Decisions & Context (User Responsibility):**
  1. **Current Baseline:** What they already know or adjacent domains they are fluent in (used to calibrate the Zone of Proximal Development).
  2. **Concrete Outcome:** What "done" looks like (e.g., passing an interview, shipping a system, teaching others, deep theoretical mastery).
  3. **Scope & Constraints:** Specific sub-areas to prioritize or explicitly exclude, time/depth budget, or specific stack/language context.
  4. **Raw Seed Material:** Any existing notes, transcripts, links, or burning questions to weave in.

### Step B: Present Only the Unblocked Frontier
Ask **3-4 numbered questions** in a single clean turn. Format every question with `❓` and provide a concrete recommended default prefixed with `➡️`:

```markdown
Before I launch primary-source research and build your vault at `~/notes/<topic-slug>/`, let's lock the mission (reply with numbers, e.g. `1 intermediate, 2 defaults`, or type `defaults`):

1. ❓ **What is your current baseline with <topic> and adjacent areas?**
   ➡️ *Default: Familiar with core fundamentals, looking for deep architectural and first-principles mastery.*

2. ❓ **What concrete outcome are you aiming for?**
   ➡️ *Default: Complete conceptual mastery + ability to reason through trade-offs, failure modes, and real-world design scenarios.*

3. ❓ **Are there specific subtopics, tools, or angles to prioritize—or anything explicitly out of scope?**
   ➡️ *Default: Cover core mechanics, primary alternatives, and production edge cases; exclude peripheral historical trivia.*

4. ❓ **Do you have any raw notes, transcripts, or specific questions you want woven into the study guide?**
   ➡️ *Default: None—start fresh from primary sources.*
```

---

## 2. Mission Lock (`00-MISSION.md`)

Once the user answers (or selects `defaults` / `--auto`), create `~/notes/<topic-slug>/00-MISSION.md` using this exact structure:

### Template: `~/notes/<topic-slug>/00-MISSION.md`

```markdown
# Mission: <Topic Title>

- **Vault Path:** `~/notes/<topic-slug>/`
- **Created:** <YYYY-MM-DD>
- **Baseline Level:** <Beginner | Intermediate | Advanced — with adjacent strengths>
- **Status:** Active

## 1. Target Outcome
<1-2 concrete sentences describing what the learner will be able to build, explain, debug, or decide after completing this vault.>

## 2. Success Criteria (Observable Proof of Mastery)
- [ ] Explain the core mechanism from first principles without jargon.
- [ ] Compare `<topic>` against its top 2-3 alternatives across latency, complexity, and failure trade-offs.
- [ ] Diagnose and resolve at least 3 real-world edge cases or failure scenarios.
- [ ] <Topic-specific observable criterion>

## 3. Curriculum Milestones
1. **Milestone 1:** <Origin, Problem Space & Core Mental Model>
2. **Milestone 2:** <Internal Architecture & Step-by-Step Mechanics>
3. **Milestone 3:** <Trade-offs, Edge Cases & Failure Modes>
4. **Milestone 4:** <Comparative Landscape & Applied Patterns>

## 4. Explicit Scope Boundaries
- **In Scope:** <Specific mechanisms, versions, specifications, or applications>
- **Out of Scope:** <Explicit exclusions to protect focus and ZPD>

## 5. User Seed Questions & Raw Inputs
- <List any specific questions, raw notes, or constraints provided by the user, or "None provided.">
```
