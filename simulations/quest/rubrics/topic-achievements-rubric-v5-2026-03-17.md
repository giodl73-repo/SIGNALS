Reading the scorecard carefully to extract the new patterns before writing the rubric.

Two signals surface that go beyond C-01 through C-17:

**From V-02**: The evidence note for C-16 reads "Verbatim compliance block pre-printed in instruction body; model told not to rewrite." C-16 tests whether compliance text is pre-printed in the skeleton. It does not test whether the prompt includes a preservation directive — an explicit instruction telling the model to leave the pre-printed block unchanged. Pre-printing alone creates structural embedding; the preservation instruction closes the remaining gap where a model might still paraphrase or restructure the block. These are separable properties: a prompt can pre-print (C-16 pass) without instructing the model not to rewrite (C-18 fail).

**From V-03**: The evidence note for C-10 reads "CLASSIFY GATE requires explicit intermediate classification before state assignment." V-01 and V-02 both PARTIAL on C-10 because their classify phases are named steps, not gates. C-09 tests ordering (CLASSIFY before STATE). C-10 tests whether explicit classify output exists. Neither tests whether the phase is architecturally a gate — a labeled barrier that requires completion output before the next phase can proceed. A named step can exist without forcing visible output; a gate by definition cannot be cleared without it. V-03's gate architecture is what causes C-10 to pass where V-01 and V-02 fail.

These become **C-18** and **C-19**. Formula updates to `/11`.

---

# Quest Score Rubric — corps-achievements
**Version**: v5 (2026-03-17)

## What Changed in v5

**2 new aspirational criteria** extracted from Round 4 excellence signals:

- **C-18 (Preservation directive for pre-printed text)** — from V-02's "model told not to rewrite" evidence note. C-16 tests whether compliance-critical text is pre-printed in the skeleton. C-18 tests whether the prompt includes an explicit instruction to leave that pre-printed block unchanged — a preservation directive. Pre-printing (C-16) creates structural embedding; the preservation directive closes the remaining gap where a model might still paraphrase or restructure the block during output generation. A prompt passes C-18 only if it contains an explicit directive — stated in the instruction body — telling the model not to rewrite, rephrase, or restructure the pre-printed compliance block. C-18 requires C-16 as a precondition; a prompt without pre-printed text cannot pass C-18.

- **C-19 (Gate-enforced phase completion)** — from V-03's CLASSIFY GATE architecture. C-09 tests ordering (CLASSIFY precedes STATE). C-10 tests whether the classify phase produces explicit intermediate output. C-19 tests whether the phases are architecturally labeled as gates — named barriers requiring explicit completion output before the subsequent phase can proceed — rather than named steps that instruct but do not enforce. A named step ("Step 2: Classify") can be followed without producing visible output; a named gate ("CLASSIFY GATE") cannot be cleared without it. V-01 and V-02 both PARTIAL on C-10 precisely because their classify phases are steps, not gates. A prompt passes C-19 only if phase labels use gate semantics and each gate explicitly defines the output required to clear it.

**Scoring formula updated**: `aspirational_pass / 11 * 10` (was `/9`). Max composite remains 100.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-19 | 10 | `pass/11 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/11 × 10)
```

| Score | Grade |
|-------|-------|
| 100 | Platinum |
| 90–99 | Gold |
| 75–89 | Silver |
| < 75 | Bronze |

---

## Criteria

### Essential (C-01 – C-05)

**C-01 — One state per achievement**
Each achievement entry carries exactly one state value: EARNED, IN-PROGRESS, or LOCKED. Multi-state rows, ambiguous state, or missing state fail. Applies to both table and prose output formats.

**C-02 — Falsified named as honesty signal**
The Falsified achievement is present as a named entry. Its description frames falsification as evidence of investigative rigor ("followed evidence over assumptions" or equivalent), not as failure or absence.

**C-03 — Artifact-grounded classification**
State assignments cite source artifacts from Step 1 by namespace or skill. EARNED entries cite a specific artifact; IN-PROGRESS entries cite the partially-completed artifact or its count. Classification that cannot be traced to an artifact fails.

**C-04 — In-progress shows numeric progress**
IN-PROGRESS achievements express progress in `n of m` form (e.g., "3 of 5 namespaces covered"). Qualitative-only descriptions ("partially done", "underway") fail.

**C-05 — Next recommended action is specific**
Step 4 (or equivalent) names the next skill, the artifact it produces, and the achievement(s) it advances. Generic instructions ("continue the investigation") fail.

---

### Recommended (C-06 – C-08)

**C-06 — All 7 categories represented**
Every achievement category appears in the output. Categories with no earned or in-progress achievements are listed as LOCKED or explicitly noted as empty. Omitting a category fails.

**C-07 — Earned achievements carry dates**
EARNED entries include the date on which the achievement was earned. Date format may vary; absence of a date on an EARNED entry fails.

**C-08 — Falsified contract completeness**
The Falsified achievement contract contains all three required components: a consequence clause (what happens when falsification is detected), an evasion surface (the mechanism by which falsification occurs), and a floor declaration (the minimum acceptable state). Absence of any one component fails.

---

### Aspirational (C-09 – C-19)

**C-09 — CLASSIFY before STATE**
The prompt enforces that the CLASSIFY phase precedes the STATE assignment phase. A prompt that assigns states before or during classification, or that conflates the two phases into a single step, fails.

**C-10 — Explicit classify output**
The CLASSIFY phase produces explicit intermediate output — a visible list of classifications — before state assignment begins. A classify phase that is named but produces no visible artifact before states are assigned fails.

**C-11 — Evasion surface named**
The evasion surface is explicitly named in the Falsified contract — the mechanism by which falsification occurs is stated inline, not implied. A contract that references an evasion surface only by number or category fails.

**C-12 — Table columns complete**
The output achievement table includes all required columns: achievement name, state (EARNED / IN-PROGRESS / LOCKED), evidence or artifact citation, and progress expression for IN-PROGRESS entries. A table missing any required column fails.

**C-13 — State count summary visible**
The output includes a state count summary — the number of achievements in each state (earned, in-progress, locked) — either in a frontmatter block or as an explicit summary line. Output that contains only the table without a count summary fails.

**C-14 — Consequence clause present**
The Falsified contract states a consequence clause: a specific declaration of what follows when the Falsified state is assigned. A contract that describes falsification without naming a consequence fails.

**C-15 — Floor sentence unconditional**
The floor declaration sentence is unconditional in its phrasing. Sentences containing "if," "when," "unless," "only if," or equivalent conditional qualifiers fail. The sentence must state the floor as an invariant, not as a conditional outcome.

**C-16 — Structural compliance embedding**
Compliance-critical text (consequence clause, evasion surface, floor declaration) is pre-printed in the prompt skeleton as fixed text the model fills around, not as rule-stated text the model must generate. Rule-stated requirements are generative — the model produces them during output. Template-embedded requirements are structural — the text exists in the prompt before the model begins. A prompt passes C-16 only if the compliance block is pre-printed verbatim in the skeleton.

**C-17 — Section-label unconditional consistency**
No conditional section label or trigger phrase governs the section, block, or callout containing the floor declaration. A floor sentence that is unconditional in phrasing (C-15) fails C-17 if the section label that introduces it is conditional ("When evidence is uncertain:", "If no artifacts exist:", etc.). The conditional frame imposed by the label contaminates the declaration regardless of the body's phrasing.

**C-18 — Preservation directive for pre-printed text**
When compliance-critical text is pre-printed in the skeleton (C-16), the prompt includes an explicit preservation directive — an instruction telling the model not to rewrite, rephrase, or restructure the pre-printed block. Pre-printing creates structural embedding; the preservation directive closes the residual gap where a model might still paraphrase the block during output generation. A prompt with pre-printed compliance text but no preservation directive fails C-18. C-16 is a precondition: a prompt without pre-printed text cannot pass C-18.

**C-19 — Gate-enforced phase completion**
Sequential phases are defined as architecturally-labeled gates — named barriers that require explicit completion output before the subsequent phase can proceed — rather than named steps that instruct sequence without enforcing it. A named step ("Step 2: Classify") instructs ordering; a named gate ("CLASSIFY GATE") prevents advancement without visible output. A prompt passes C-19 only if phase labels use gate semantics and each gate explicitly defines the output required to clear it. A prompt with correctly-ordered named steps but no gate architecture fails.
