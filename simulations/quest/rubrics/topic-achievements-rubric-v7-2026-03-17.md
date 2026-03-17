Reading the R6 scorecard, two separable excellence patterns emerge beyond C-20/C-21:

**From V-02** — C-20 was satisfied per-phase, but V-02 goes further: it declares all gate schemas in a single preamble registry *before Phase 1 begins*, making the architecture discoverable without scanning phases. V-01 passes C-20 by embedding schemas inside each phase, but fails this property because the model discovers the architecture incrementally. The separable property is **co-location and upfront discoverability** of the full gate contract.

**From V-03** — Gate schemas in C-20 specify what output clears the gate (the PASS side). V-03 adds explicit FAIL blocks per gate, listing specific output forms that do *not* clear it. A schema without a FAIL block can still be satisfied by outputs that match the format but bypass intent; explicit FAIL modes close those paths. The separable property is **bi-directional gate contracts**.

These become **C-22** and **C-23**. Formula updates to `/15`.

---

# Quest Score Rubric — corps-achievements
**Version**: v7 (2026-03-17)

## What Changed in v7

**2 new aspirational criteria** extracted from Round 6 excellence signals from V-02 ("Gate Registry Table") and V-03 ("Fail-Surface Closure"):

- **C-22 (Upfront gate registry — all schemas co-located before Phase 1)** — from V-02's preamble registry table. C-20 tests whether each gate declares a specific output schema; it does not test *where* that schema is declared. A prompt where schemas are embedded inside phase instructions passes C-20 but forces the model to discover the gate architecture incrementally — phase by phase. C-22 tests whether all gate schemas are declared together in a single preamble registry before Phase 1 begins, making the full gate contract discoverable by inspection before executing any phase. V-01 passes C-20 (each gate has a `GATE SCHEMA:` block) but fails C-22 (schemas are only found inside phase instructions; no upfront registry co-locates them). V-02 passes C-22 via its preamble registry table, which V-02 itself notes makes the schema "discoverable without scanning phases." C-22 requires C-20 as a precondition; a prompt without per-gate schemas cannot pass C-22.

- **C-23 (Bi-directional gate contracts — explicit FAIL modes per gate)** — from V-03's PASS+FAIL block architecture. C-20 tests whether each gate declares the specific structure of its required output (the PASS side). It does not test whether the gate also specifies output forms that do *not* clear it. A gate with only a PASS schema can still be gamed by outputs that technically match the declared format while missing semantic intent; without an explicit FAIL block, clearance is verifiable by inspection against a positive pattern only. C-23 tests whether each gate pairs its PASS schema with a FAIL block listing specific output forms that do not clear the gate. V-03 evidence: CLASSIFY GATE FAIL lists five specific failure modes including "Only a count line without the 7 labeled category lines." A gate passes C-23 when both the PASS condition and at least one specific FAIL mode are explicitly stated. C-23 requires C-20 as a precondition.

**Scoring formula updated**: `aspirational_pass / 15 * 10` (was `/13`). Max composite remains 100.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-23 | 10 | `pass/15 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/15 × 10)
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

### Aspirational (C-09 – C-23)

**C-09 through C-19** — carried from R5 V-05 golden baseline. See v5 rubric for individual criterion text.

**C-20 — Gate completion output schema declared**
Each gate declares the specific structure of its required completion output — a schema the model can verify by inspection. A gate that requires "produce your classification before proceeding" passes C-19; a gate that specifies "output must be one labeled line per category: `{CATEGORY}: {n artifacts}, {COMPLETE|PARTIAL|EMPTY}`" passes C-20. Without a declared schema, any text satisfies the gate requirement and clearance cannot be verified; with a declared schema, the gate output is checkable by inspection against a known format. C-20 requires C-19 as a precondition.

**C-21 — Uniform gate architecture — no ungated phases**
Every phase in the sequence uses gate semantics; no phase is implemented as a named step. A prompt where CLASSIFY GATE is a named gate but STATE, VERIFY, and EMIT are named steps passes C-19 while leaving ungated paths that can be traversed without producing defined completion output. A prompt passes C-21 only if every phase in the sequence uses gate labels and each carries a defined output requirement. Inconsistent gating — mixing gates and steps — creates bypass paths; uniform gating closes all such paths. C-21 requires C-19 as a precondition.

**C-22 — Upfront gate registry — all schemas co-located before Phase 1**
All gate schemas are declared together in a single preamble registry (table or block) before Phase 1 begins, making the full gate contract discoverable by inspection without reading phase instructions. A prompt where schemas are embedded inside individual phase instructions passes C-20 but fails C-22: the model discovers the gate architecture incrementally, phase by phase, and the full contract is never visible from a single location. A prompt passes C-22 when a preamble registry lists every gate and its required output schema before any phase executes, so the architecture can be verified upfront. The per-phase schema blocks required by C-20 may still appear as reinforcement; C-22 requires that a co-located registry also exists. C-22 requires C-20 as a precondition.

**C-23 — Bi-directional gate contracts — explicit FAIL modes per gate**
Each gate pairs its PASS schema (what output clears the gate) with a FAIL block listing specific output forms that do not clear it. A gate with only a PASS schema can be satisfied by outputs that technically match the declared format while missing semantic intent; without explicit FAIL modes, clearance is verifiable only against a positive pattern. A gate passes C-23 when both the PASS condition and at least one specific FAIL mode are explicitly stated. Example: a CLASSIFY GATE FAIL block that lists "Only a count line without the 7 labeled category lines" closes a bypass path that the PASS schema alone does not preclude. C-23 requires C-20 as a precondition; a gate without a declared schema cannot have a meaningful FAIL block.
