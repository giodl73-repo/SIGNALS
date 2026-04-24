---
skill: quest-rubric
skill_target: quest-variate
date: 2026-03-15
version: 5
prior_version: quest-rubric-variate-R4-2026-03-15.md
---

# Rubric: quest-variate (v5)

Evaluates output from the `quest-variate` skill, which generates N distinct prompt variations
of a skill body. Each variation must be complete and runnable, vary along exactly one axis,
and carry a labeled hypothesis.

**v5 changes**: Added C-25 through C-27 from Round 4 excellence signals. No essential or
recommended criteria changed. Aspirational denominator updated from /16 to /19.

---

## Criteria

### Essential (must all pass -- without these the output is not useful)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Runnable completeness** | correctness | essential | Every variation is a full, standalone skill body. Each V-NN block can be copied into a skill file and executed without referencing any other variation. No "same as V-01 except..." constructs. All declared steps and sections are written out in full -- not placeholders, not ellipses. |
| C-02 | **Count and labeling** | format | essential | Output contains exactly the requested N variations (default 5 when N is unspecified), labeled V-01 through V-0N in sequence with no gaps. Fewer than N is a fail; extra unlabeled content does not substitute for missing labeled variations. |
| C-03 | **Axis declaration** | format | essential | Every V-NN header or preamble includes an `axis:` field naming one of the defined axes, and a `hypothesis:` field stating the expected behavioral effect. Both fields must be present and non-empty. |
| C-04 | **Single-axis isolation** | correctness | essential | Each variation changes exactly one axis relative to a shared baseline. Reading two variations side-by-side, the structural difference maps to exactly one named axis. Changes that bleed across axes are a fail. Exception: variations explicitly labeled as combination passes. |
| C-05 | **Genuine distinctness** | correctness | essential | No two variations are superficially equivalent (e.g., minor synonym substitution that does not actually change the axis). Each variation must be distinguishable by its axis choice in a way that would produce observably different model behavior. |

---

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Axis spread across the full axis vocabulary** | coverage | recommended | The N variations cover at least 3 distinct axes from the axis vocabulary (role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity). Not all variations on the same axis. |
| C-07 | **Hypotheses are falsifiable** | depth | recommended | Every hypothesis is specific enough to be testable: it predicts a directional outcome (e.g., "V-03 will produce more granular scoring because..."), not a vague preference ("this might be better"). |
| C-08 | **Baseline is explicit or inferable** | format | recommended | The output either states the baseline skill body once up front, or makes the stable baseline clearly inferable from the variation set so a reviewer can reason about what changed. |

---

### Aspirational (raise the bar once essential/recommended are stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Combination roadmap appended** | depth | aspirational | After the single-axis variations, the output includes a brief combination matrix or table identifying the most promising axis pairings for a follow-up pass, with rationale. |
| C-10 | **Hypothesis tension surfaced** | depth | aspirational | At least one variation explicitly notes a trade-off or tension between axes (e.g., "increasing scoring granularity in V-04 conflicts with the concise output format in V-02"), demonstrating awareness of interaction effects. |
| C-11 | **Explicit failure condition on every hypothesis** | depth | aspirational | Every hypothesis includes a stated failure condition: a specific, observable outcome that would refute the mechanism if it occurred (e.g., "if V-03 does not improve X, the mechanism is refuted"). Enables a negative experimental result to be recovered cleanly rather than explained away. |
| C-12 | **Evaluation order guidance** | depth | aspirational | After the variation bodies, the output includes a ranking or table ordering the variations by evaluation priority -- incorporating cost, independence from other variations, and dependency relationships -- to support a multi-run experimental plan. |
| C-13 | **Hypothesis tension note pre-combination** | depth | aspirational | At least one axis-pair conflict is explicitly named *before* the combination roadmap, with a prediction of which variable will dominate the outcome if the combination is run. Prevents a confounded round-2 result by forcing a phase-priority choice before the combination is designed. |
| C-14 | **Criterion-targeted axis selection** | depth | aspirational | At least one variation names the specific rubric criterion its declared axis is designed to improve. The mechanism connecting the axis to the criterion must be explicit (e.g., "annotated-rationale constraints cause mechanism-citing hypotheses, improving C-07 pass rates"). Naming an outcome-level effect without connecting it to a criterion ID does not pass. |
| C-15 | **Inline generation loop gate** | correctness | aspirational | At least one variation embeds a self-check gate *inside* the variation-generation loop -- fired after each variation body, before advancing to the next -- with an explicit "fix before advancing" or equivalent instruction. A gate that appears only as a post-generation review step does not pass. The gate must name which criteria it is checking. |
| C-16 | **Per-axis pole declaration before generation** | format | aspirational | Before any variation body is generated, the output includes a structured declaration of the current (baseline) pole for every axis in the axis vocabulary. A champion table or equivalent qualifies; a single "the baseline skill body is [X]" reference does not -- each axis must have its current pole named individually. Directly enables C-04 isolation checks by making the stable element visible per axis. |
| C-17 | **Pre-generation axis lock** | correctness | aspirational | Combination passes (or any variation where axis isolation is a risk) include an explicit instruction declaring axis assignments immutable once the generation phase begins ("do not revise axis assignments after Phase N begins" or equivalent). Converts C-04 single-axis isolation from an intention to an enforced protocol constraint. Only evaluated for combination passes; single-axis-only outputs pass by default. |
| C-18 | **Single-axis comparison denominator in combination failure conditions** | depth | aspirational | Combination pass failure conditions name the most relevant single-axis variation as the comparison baseline rather than the bare unvaried skill (e.g., "if the combination does not exceed V-01 alone..." rather than "if the outcome does not improve..."). The named variation must be the one that most directly tests the dominant axis of the combination. Only evaluated for combination passes; single-axis-only outputs pass by default. |
| C-19 | **Structured four-part hypothesis schema** | format | aspirational | At least one variation's hypothesis field is composed of all four named parts: (1) criterion-target (C-NN by ID), (2) directional prediction (increases / decreases), (3) causal mechanism (because...), and (4) explicit failure condition (if...). Passing C-11 + C-14 individually does not imply passing C-19 -- C-19 requires all four parts to be present and structurally labeled within a single hypothesis entry. |
| C-20 | **Dual mechanistically-distinct failure conditions** | depth | aspirational | At least one hypothesis states two failure conditions that are mechanistically distinct: one for *outcome failure* (the axis produced no measurable effect on the target criterion) and one for *implementation failure* (the mechanism was instantiated incorrectly even if the outcome metric is met, producing a result that independently violates a separate criterion). The second failure condition must name the separate criterion it would fail. Single-failure-condition hypotheses (C-11 passes) do not satisfy C-20. |
| C-21 | **Rubric-ID exception citation for combination passes** | format | aspirational | When a combination pass invokes the C-04 single-axis isolation exception, the variation body cites the criterion ID being excepted by number (e.g., "C-04 exception explicitly invoked") rather than using an informal label ("combination pass" or equivalent). Converts the exception from an implied permission to a traceable protocol citation with a clear audit trail. Only evaluated for outputs that include at least one combination pass. |
| C-22 | **Criterion-keyed combination roadmap rows** | depth | aspirational | Each entry in the combination roadmap names the specific rubric criterion IDs the combination is designed to improve, not just a narrative rationale. A row qualifies only if it maps the axis pairing to at least two criterion IDs and includes a mechanism sentence explaining why the pairing addresses those criteria jointly. Exceeds C-09 (which requires rationale) -- this maps each planned combination to an experimentally verifiable criterion goal. |
| C-23 | **Phased prompt architecture** | correctness | aspirational | The variation output uses an explicitly numbered, labeled phase structure -- at minimum: a commitment/planning phase (declare axes, lock assignments), a generation phase (produce bodies with embedded gate), and a findings phase (compare results) -- each with its declared responsibility stated in the prompt. Exceeds C-15 (which requires only an inline gate) by requiring a complete phased container with named transition points between phases. Evaluated when any loop gate is present; single-axis-only outputs with no gate pass by default. |
| C-24 | **Pre-generation variation score predictions** | depth | aspirational | Before the generation phase begins, the output includes a variation map that predicts, for each planned variation, which rubric criteria are expected to improve and in which direction. Constitutes a quantitative pre-commitment that can be evaluated against the actual findings. A champion inventory without per-variation criterion predictions does not pass. Evaluated for any output that includes a planning or commitment phase. |
| C-25 | **Dual failure condition sub-fields as separately labeled keys** | format | aspirational | When a hypothesis contains two failure conditions (satisfying C-20), each condition appears as a distinct named key -- `failure-condition-outcome:` and `failure-condition-implementation:` -- rather than two sentences embedded within a single `failure-condition:` field. The separation makes C-20 compliance structurally detectable by field presence: a scorecard can check for the `failure-condition-implementation:` key without parsing prose. A variation that satisfies C-20 by content (two distinct mechanisms stated in one field) does not satisfy C-25. Only evaluated for hypotheses that claim or target C-20. |
| C-26 | **Per-body axis-freeze protocol inside the generation loop** | correctness | aspirational | Inside the generation phase, before writing each variation body, the prompt instructs the generator to: (1) read the committed axis from the pre-generation declaration; (2) explicitly name every other axis that could tempt drift and freeze each by name; (3) proceed to write only the committed axis change. Converts C-04 single-axis isolation from a post-body audit (did anything else change?) into a per-body pre-write checklist (what else might change -- freeze it now), surfacing contamination risk before it occurs rather than catching it after. Exceeds C-17 (a document-level axis lock at the start of generation) by requiring the freeze to execute per-body inside the generation loop. Only evaluated when a generation phase with multiple variation bodies is present; single-variation outputs pass by default. |
| C-27 | **Pre-generation variation map as a standalone top-level artifact** | format | aspirational | The pre-generation variation map (satisfying C-24) is placed as a distinct, independently labeled section at document scope -- not embedded inside a phase body, planning sub-stage, or preamble block -- and carries an explicit immutability instruction at the section level ("Do not revise after Phase N begins" or equivalent). A C-24-compliant map that lives inside a planning phase block without its own top-level section header and a freeze instruction does not satisfy C-27. C-24 requires the *content* (per-variation per-criterion directional predictions); C-27 requires the *artifact structure* (separate header, document-scope placement, named immutability). |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 19 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential pass | Ship-ready variation set |
| Silver | >= 65, all essential pass | Usable with minor gaps |
| Bronze | >= 50, >= 4 essential pass | Needs revision before use |
| Fail | any essential fails | Not usable |

---

## Quick Checklist (for manual scoring)

- [ ] C-01: Every variation is a complete, standalone, runnable skill body
- [ ] C-02: Exactly N variations, labeled V-01 through V-0N with no gaps
- [ ] C-03: Each variation has `axis:` and `hypothesis:` fields, both non-empty
- [ ] C-04: Each variation changes exactly one axis (combination passes labeled explicitly)
- [ ] C-05: No two variations are superficially equivalent
- [ ] C-06: At least 3 distinct axes from the axis vocabulary represented
- [ ] C-07: Every hypothesis predicts a directional, testable outcome
- [ ] C-08: Baseline stated explicitly or clearly inferable from the variation set
- [ ] C-09: Combination roadmap present with axis-pair rationale
- [ ] C-10: At least one hypothesis surfaces an axis tension or trade-off
- [ ] C-11: Every hypothesis includes an explicit failure condition
- [ ] C-12: Evaluation order table or ranking provided
- [ ] C-13: Axis-pair tension named before combination roadmap, with dominance prediction
- [ ] C-14: At least one variation names the rubric criterion ID its axis targets
- [ ] C-15: At least one variation has a self-check gate inside the generation loop
- [ ] C-16: Per-axis baseline pole declared before any variation body is generated
- [ ] C-17: Combination passes include an explicit pre-generation axis lock instruction
- [ ] C-18: Combination failure conditions name a single-axis variation as comparison denominator
- [ ] C-19: At least one hypothesis contains all four parts: criterion-target, direction, mechanism, failure condition
- [ ] C-20: At least one hypothesis states two mechanistically-distinct failure conditions (outcome + implementation)
- [ ] C-21: Combination passes cite the excepted criterion ID by number (e.g., "C-04 exception")
- [ ] C-22: Every combination roadmap row maps to specific criterion IDs being targeted
- [ ] C-23: Output uses an explicitly numbered, labeled phase structure with named transition points
- [ ] C-24: Planning phase includes per-variation criterion score predictions before generation begins
- [ ] C-25: C-20 hypotheses express failure conditions as two separately named keys, not two sentences in one field
- [ ] C-26: Generation loop includes a per-body axis-freeze step (name axes at risk, freeze each before writing)
- [ ] C-27: Pre-generation variation map has its own top-level section header and an explicit immutability instruction

---

## Evaluator Notes

- C-01 is the hardest essential to fake: spot-check by asking "could I paste V-02 directly into a skill file and run it?" If no, C-01 fails.
- C-04 failures are common when a skill body is complex -- authors tend to fix two things at once. One axis change per variation is a strict constraint.
- **C-14 vs C-07**: C-07 requires a falsifiable hypothesis. C-14 requires that the axis was *chosen* to target a specific rubric criterion, with the mechanism stated. A variation can pass C-07 and fail C-14 if the axis-to-criterion connection is never made explicit.
- **C-15 vs C-08**: C-08 checks whether a baseline is present. C-15 checks whether a correctness gate fires inside the loop. They are independent -- a variation can pass C-08 and fail C-15.
- **C-16 vs C-08**: C-08 passes if the baseline is "inferable." C-16 requires a structured per-axis declaration of current poles before generation begins. A set can pass C-08 and fail C-16.
- **C-17 and C-18**: Only evaluated for outputs that include at least one combination pass. If all variations are single-axis, both criteria are vacuously true and score as full passes.
- **C-19 vs C-11 + C-14**: A variation can pass both C-11 (has a failure condition) and C-14 (names a criterion ID) while still failing C-19 if those elements live in separate variations or all four parts are not present in a single, compositionally structured hypothesis entry.
- **C-20 vs C-11**: C-11 requires one explicit failure condition. C-20 requires two failure conditions that are mechanistically *different*: one tests whether the axis produced its claimed outcome, the second tests whether the mechanism was implemented in a way that would independently violate another named criterion. If both failure conditions describe the same mechanism failure, C-20 does not pass.
- **C-21**: Only evaluated for combination passes. The criterion ID must appear verbatim or in an unambiguous form (e.g., "C-04 exception explicitly invoked"). A phrase like "per the combination rule" does not pass.
- **C-22 vs C-09**: C-09 passes with a narrative rationale per roadmap row. C-22 requires criterion IDs in addition. A roadmap that says "combining role-sequence with inertia-framing should improve completion quality" fails C-22; one that says "targets C-01, C-04, C-07" passes.
- **C-23 vs C-15**: C-15 requires a gate inside the loop. C-23 requires an explicitly labeled, numbered phase structure with declared responsibilities per phase. A prompt with a loop gate but no phase labeling passes C-15 and fails C-23. A prompt with phases but no inline gate fails C-15 and may pass C-23.
- **C-24**: The variation map must be directional per criterion per variation -- not a single summary claim. "V-03 is expected to improve C-07 pass rates" per row qualifies. "These variations will improve output quality overall" does not.
- **C-25 vs C-20**: C-20 requires two mechanistically-distinct failure conditions by *content*. C-25 requires they appear as *two separately named keys* in the hypothesis structure. A hypothesis can pass C-20 and fail C-25 if both conditions are written as prose sentences within a single `failure-condition:` field. C-25 only activates for hypotheses that contain or target C-20.
- **C-26 vs C-17**: C-17 is a one-time document-level axis lock at the start of generation ("do not revise after Phase N begins"). C-26 requires the freeze to execute inside the loop, once per variation body -- naming the specific axes at risk for *that body* before writing it. A prompt with a C-17-compliant document lock but no per-body freeze step passes C-17 and fails C-26.
- **C-27 vs C-24**: C-24 passes if per-variation per-criterion directional predictions exist anywhere before generation begins, including inside a planning sub-stage. C-27 requires those predictions to live in a section with its own top-level header and an explicit immutability declaration at the section level. A table embedded inside "PHASE 1B: Score Predictions" without a separate named artifact heading fails C-27.

---

## Criterion Genealogy

| Criterion | Source | Round introduced |
|-----------|--------|-----------------|
| C-01 | Design | v1 |
| C-02 | Design | v1 |
| C-03 | Design | v1 |
| C-04 | Design (single-axis isolation -- theoretical core) | v1 |
| C-05 | Design (genuine distinctness -- prevents synonym-swap degenerate output) | v1 |
| C-06 | Design | v1 |
| C-07 | Design (falsifiability distinguishes testable from trivial hypotheses) | v1 |
| C-08 | Design | v1 |
| C-09 | Design | v1 |
| C-10 | Design | v1 |
| C-11 | R1 excellence: explicit failure condition enables clean negative results | v2 |
| C-12 | R1 excellence: evaluation order guidance supports multi-run experimental plans | v2 |
| C-13 | R1 excellence: pre-combination tension note with dominance prediction prevents confounded R2 | v2 |
| C-14 | R2 excellence: V-01 axis chosen to target C-07 pass rates -- "annotated-rationale constraints cause mechanism-citing hypotheses" -- first criterion-targeted axis in the set | v3 |
| C-15 | R2 excellence: V-02 self-score gate fires after each body while context is active -- "strongest C-01 targeting mechanism in the set" -- gate-inside-loop pattern | v3 |
| C-16 | R2 excellence: V-03 champion table declared per-axis before generation -- "converts baseline from inferable to explicitly declared per axis" -- strongest C-08 in the set | v3 |
| C-17 | R2 excellence: V-04 PLAN-phase immutability -- "most operationally specific axis-isolation mechanism in the set" -- axis lock enforced as protocol constraint | v3 |
| C-18 | R2 excellence: V-04 and V-05 combination failure conditions named single-axis comparison denominator (V-01, V-03) rather than bare baseline -- compound comparison rigor | v3 |
| C-19 | R3 excellence: V-01 hypothesis field composed of all four parts (criterion ID, direction, mechanism, failure condition) as a single structured entry -- four-part schema codified as criterion | v4 |
| C-20 | R3 excellence: V-02 hypothesis states two mechanistically-distinct failure conditions -- outcome failure (no C-01 improvement vs R2) and implementation failure (gate in wrong position, independently failing C-15) | v4 |
| C-21 | R3 excellence: V-04 and V-05 cite "C-04 exception explicitly invoked" by criterion ID -- converts combination exception from implicit permission to rubric-traceable protocol citation | v4 |
| C-22 | R3 excellence: C-09 roadmap rows name specific criterion IDs per entry (C-01, C-04, C-07 / C-03, C-07, C-14) -- converts narrative rationale to criterion-keyed experimental plan | v4 |
| C-23 | R3 excellence: V-04 three-phase structure (PHASE 1 commitment, PHASE 2 generation+gate, PHASE 3 findings) -- phased container promotes loop gate from mechanism to architectural protocol | v4 |
| C-24 | R3 excellence: V-05 PHASE 1 includes champion inventory + variation map with score predictions -- quantitative pre-commitment before generation creates verifiable hypothesis record | v4 |
| C-25 | R4 excellence (E-01): V-04 introduces `failure-condition-outcome:` and `failure-condition-implementation:` as distinct named keys -- separates C-20 content requirement from structural detectability, making dual-failure omission visible by field presence alone | v5 |
| C-26 | R4 excellence (E-02): V-05 Phase 2 per-body pre-write protocol -- read committed axis, name and freeze every other axis at risk, then write -- converts C-04 isolation from post-body audit to per-body contamination prevention | v5 |
| C-27 | R4 excellence (E-03): V-05 variation map placed as standalone top-level artifact with explicit "Do not revise after Phase 2 begins" instruction -- separates C-24 content requirement from document-scope structural placement and immutability | v5 |
