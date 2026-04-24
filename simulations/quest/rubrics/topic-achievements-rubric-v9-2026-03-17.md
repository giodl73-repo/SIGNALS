Reading the scorecard, one new excellence pattern emerges beyond C-24/C-25:

**From V-05** — V-05 edges V-04 by one aspirational pass from explicit phase barrier language ("STOP. Phase N complete."). The scorecard explicitly flags this as a C-26 candidate: "Architecturally stronger than phase-do-not-begin instructions. It seals prior-phase outputs before next-phase context exists, preventing retroactive reframing." Phase-do-not-begin instructions operate prospectively (don't start Phase N+1 yet); barrier language operates retrospectively at the moment of phase completion (Phase N is now closed). A prompt using only the former allows a model to retroactively reframe Phase N output once Phase N+1 context is introduced. The separable property is **explicit phase-completion sealing via barrier language**.

This becomes **C-26**. Formula updates to `/18`.

---

# Quest Score Rubric — corps-achievements
**Version**: v9 (2026-03-17)

## What Changed in v9

**1 new aspirational criterion** extracted from Round 8 excellence signal from V-05 ("Lifecycle Phase Barrier Language"):

- **C-26 (Explicit lifecycle phase barrier language — "STOP. Phase N complete." seals prior-phase outputs before next-phase context is introduced)** — from V-05's phase barrier pattern. Prior versions of the prompt use phase-do-not-begin language: instructions that gate entry to Phase N+1 on completion of Phase N. This operates prospectively — it prevents premature advancement but does not lock Phase N's outputs. A prompt that uses only phase-do-not-begin instructions allows the model to retroactively reframe Phase N output once Phase N+1 context arrives (new artifacts discovered in Phase 2 casting doubt on Phase 1 classifications; next-phase task framing altering prior-phase schema interpretation). C-26 tests whether each phase boundary carries explicit barrier language ("STOP. Phase N complete." or equivalent declarative seal) at the point of phase completion, before the next phase's inputs are introduced. The barrier closes the prior phase's output set; subsequent context cannot reopen it. V-05 evidence: explicit "STOP. Phase N complete." language at each phase boundary; V-04 uses phase-do-not-begin instructions without barrier seals and does not pass C-26. A prompt with only phase ordering instructions (begin Phase 2 only after Phase 1 scan is complete) satisfies phase-ordering criteria but fails C-26. C-26 does not require C-22, C-23, C-24, or C-25 as preconditions; it is structurally independent and addresses retroactive reframing rather than gate-contract definition or FAIL-mode coverage.

**Scoring formula updated**: `aspirational_pass / 18 * 10` (was `/17`). Max composite remains 100.

---

**Prior version notes (carried forward for traceability)**

*v8 added C-24 and C-25 from Round 7 excellence signals:*

- **C-24** — from V-02/V-04's REGISTRY PRIMACY declaration. C-22 tests schema co-location and self-sufficiency; C-24 tests whether the registry is explicitly declared the sole authoritative gate contract, with phase instructions subordinate to it. C-24 requires C-22 as a precondition.

- **C-25** — from V-03's severity-stratified FAIL block architecture. C-23 tests presence of at least one specific FAIL mode per gate; C-25 tests whether FAIL modes are stratified into Tier 1 (structural), Tier 2 (completeness), Tier 3 (semantic bypass) with explicit tier labels. Tier 3 is the most consequential: all required fields present, intent circumvented. C-25 requires C-23 as a precondition.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-26 | 10 | `pass/18 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/18 × 10)
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

**C-08 — Frontmatter includes state counts**
Output includes a frontmatter or summary block with numeric counts for earned, in_progress, and locked achievements. Missing any of the three counts fails.

---

### Aspirational (C-09 – C-26)

**C-09 through C-21 — Established patterns (carried forward from prior rounds, unchanged)**
These thirteen criteria encode structural, formatting, and behavioral patterns established in Rounds 1–6. They cover gate architecture, phase ordering, schema completeness, cross-reference integrity, and output determinism. See v7 for full definitions.

**C-22 — Gate schemas co-located in a preamble registry**
All gate schemas (both SCAN GATE and CLASSIFY GATE) appear together in a single preamble registry block before Phase 1 begins. The registry entry for each gate is self-sufficient for inspection: it contains the complete schema without requiring cross-reference to the phase instruction that uses it. A gate schema that must be reconstructed by reading a phase instruction fails C-22.

**C-23 — Each gate pairs PASS schema with at least one specific FAIL mode**
Each gate definition includes both a PASS schema and a FAIL block listing at least one concrete output form that does not clear the gate. Generic FAIL descriptions ("output is insufficient") fail. FAIL modes must be specific enough that an example of failing output could be constructed from them.

**C-24 — Registry primacy declaration — registry is sole authoritative gate contract**
The prompt contains an explicit declaration that the registry is the sole authoritative source for gate contracts and that phase instructions implement these contracts without redefining, qualifying, or supplementing them. C-22 is a precondition: a registry without complete schemas cannot carry contractual authority over them. A prompt where the registry has complete schemas but phase instructions could plausibly be treated as parallel definitions passes C-22 but fails C-24. V-04 evidence: "REGISTRY PRIMACY: These schemas are the sole authoritative gate contracts. Phase instructions implement these contracts. They do not redefine, qualify, or supplement achievement conditions."

**C-25 — Severity-stratified FAIL blocks — three tiers with explicit semantic-bypass tier**
Each gate's FAIL block organizes failure modes into at least three severity tiers with explicit tier labels: Tier 1 (structural — required labels or fields absent), Tier 2 (completeness — required fields present but insufficiently populated), Tier 3 (semantic bypass — all required fields present but intent is circumvented). The Tier 3 (semantic-bypass) tier is the most consequential and must be named explicitly; a flat FAIL list that mixes structural and semantic failures without tier labels fails C-25 even if it enumerates the same failure modes. C-23 is a precondition: ungrouped FAIL modes cannot be stratified.

**C-26 — Explicit lifecycle phase barrier language — "STOP. Phase N complete." seals prior-phase outputs**
Each phase boundary carries an explicit declarative seal ("STOP. Phase N complete." or equivalent) at the point of phase completion, before the next phase's inputs or context are introduced. This is architecturally distinct from phase-do-not-begin instructions: the barrier closes the prior phase's output set at phase completion, preventing retroactive reframing by subsequent context. A prompt that uses only phase-do-not-begin instructions (gating Phase N+1 entry on Phase N completion) satisfies phase-ordering criteria but fails C-26, because it does not seal Phase N's outputs before Phase N+1 context arrives. C-26 is structurally independent of C-22 through C-25; it addresses a separate failure class (retroactive reframing) rather than gate-contract definition or FAIL-mode coverage. V-05 evidence: explicit "STOP. Phase N complete." at each phase boundary; V-04 uses phase-do-not-begin instructions without barrier seals.
