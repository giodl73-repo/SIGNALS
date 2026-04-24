Reading V-03's title and the pattern established by C-18/C-19 extraction, two new separable properties emerge from gate architecture:

1. **C-19 gap — gate output schema**: C-19 tests whether a gate requires completion output before proceeding. It does not test whether the gate declares the specific structure of that output. A gate requiring "produce your classification" passes C-19; a gate specifying "output must be one labeled line per category in format `{CATEGORY}: {n artifacts}, {STATUS}`" goes further. Without a schema, any text clears the gate; with a declared schema, clearance is verifiable by inspection.

2. **C-21 gap — uniform gate architecture**: C-19 tests that specific phases are gated. It does not test whether all phases in the sequence are gated. A prompt where CLASSIFY GATE is a named gate but STATE and EMIT are named steps passes C-19 while leaving ungated paths that can be traversed without producing defined output.

These become **C-20** and **C-21**. Formula updates to `/13`.

---

# Quest Score Rubric — corps-achievements
**Version**: v6 (2026-03-17)

## What Changed in v6

**2 new aspirational criteria** extracted from Round 5 excellence signals from V-03 ("Gate Architecture with Defined Completion Output per Gate"):

- **C-20 (Gate completion output schema declared)** — from V-03's defined-output-per-gate architecture. C-19 tests whether phase labels use gate semantics and each gate defines that output is required to clear it. C-20 tests whether each gate declares the specific structure of that output — a schema the model can verify by inspection. A gate that requires "produce your classification before proceeding" passes C-19; a gate that specifies "output must be one labeled line per category: `{CATEGORY}: {n artifacts}, {COMPLETE|PARTIAL|EMPTY}`" passes C-20. Without a declared schema, any text satisfies the gate requirement and clearance cannot be verified; with a declared schema, the gate output is checkable by inspection against a known format. C-20 requires C-19 as a precondition; a prompt without gate labels cannot pass C-20.

- **C-21 (Uniform gate architecture — no ungated phases)** — from V-03's consistent application of gate semantics across the entire phase sequence. C-19 tests whether specific phases use gate labels with defined output requirements. C-21 tests whether the entire phase architecture is uniformly gated — every phase in the sequence uses gate semantics, with no phases implemented as named steps. A prompt where CLASSIFY GATE is a named gate but STATE, VERIFY, and EMIT are named steps passes C-19 while leaving ungated paths that can be traversed without producing defined completion output. A prompt passes C-21 only if every phase in the sequence uses gate labels and each carries a defined output requirement. Inconsistent gating — mixing gates and steps — creates bypass paths through the prompt; uniform gating closes all such paths. C-21 requires C-19 as a precondition.

**Scoring formula updated**: `aspirational_pass / 13 * 10` (was `/11`). Max composite remains 100.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-21 | 10 | `pass/13 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/13 × 10)
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

### Aspirational (C-09 – C-21)

**C-09 — CLASSIFY precedes STATE**
The classify phase appears before the state-assignment phase in the prompt structure. Any prompt where state assignment can occur before classification is attempted fails.

**C-10 — Explicit classify intermediate output**
The classify phase produces labeled intermediate output — one line or block per category — before any state assignment occurs. A classify phase that instructs without requiring visible output fails.

**C-11 – C-15 — R4 V-05 baseline**
Criteria established in Round 4 V-05. Preserved as a block; individual definitions not reproduced here. A prompt that met the R4 V-05 aspirational baseline passes this criterion block.

**C-16 — Compliance text pre-printed in skeleton**
Compliance-critical text (e.g., the Falsified Achievement Contract) is pre-printed verbatim in the prompt skeleton, not generated by the model at runtime. Text that the model is expected to produce or interpolate during output generation fails.

**C-17 — Floor criterion independent of conditional labels**
The minimum-qualification rule for the Falsified achievement is stated independently as a standing floor, not only as a conditional clause within a labeled block. A floor declared only inside a conditionally-applied block fails; a floor declared as a named invariant that holds regardless of other conditions passes.

**C-18 — Preservation directive in instruction body**
The prompt includes an explicit instruction — stated in the instruction body, outside and governing the pre-printed block — directing the model not to rewrite, rephrase, or restructure the pre-printed compliance text. C-16 tests structural embedding (the text is pre-printed); C-18 tests behavioral closure (the model is instructed to leave it unchanged). A brief inline note inside or adjacent to the block does not satisfy C-18; the directive must appear as a named rule or invariant in the governing instruction body. C-18 requires C-16 as a precondition.

**C-19 — Gate-enforced phase completion**
Phase labels in the prompt use gate semantics — named barriers (e.g., "CLASSIFY GATE") that require explicit completion output before the subsequent phase can proceed — rather than named steps that instruct without enforcing. A named step ("Step 2: Classify") can be followed without producing visible output; a named gate cannot be cleared without it. A prompt passes C-19 only if phase labels use gate semantics and each gate explicitly defines the output required to clear it.

**C-20 — Gate completion output schema declared**
Each gate in the prompt declares the specific structure of the output required to clear it — a schema the model can verify by inspection — not merely that output is required. A gate requiring "produce your classification before proceeding" passes C-19; a gate specifying "output must be one labeled line per category: `{CATEGORY}: {n artifacts}, {COMPLETE|PARTIAL|EMPTY}`" passes C-20. Without a declared schema, any text satisfies the gate requirement and clearance cannot be checked; with a declared schema, gate output is verifiable against a known format. C-20 requires C-19 as a precondition.

**C-21 — Uniform gate architecture — no ungated phases**
Every phase in the prompt sequence uses gate semantics; no phases are implemented as named steps. A prompt where CLASSIFY GATE is a named gate but STATE, VERIFY, and EMIT are named steps passes C-19 while leaving ungated paths through which phases can be traversed without producing defined completion output. A prompt passes C-21 only if every phase in the sequence uses gate labels and each carries a defined output requirement. Inconsistent gating — mixing gates and steps in the same sequence — creates bypass paths that gate enforcement is intended to close. C-21 requires C-19 as a precondition.
