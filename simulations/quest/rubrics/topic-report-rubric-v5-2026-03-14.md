Here is the complete updated rubric, written to `simulations/quest/rubrics/topic-report-rubric-v5-2026-03-14.md`.

---

**Three new aspirational criteria added from Round 4 excellence signals:**

| ID | Criterion | Source |
|----|-----------|--------|
| **C-18** | Three-layer co-location at the write point | E-1 / V-04 minimal golden, V-05 ceiling |
| **C-19** | Contract label chaining from register to annotation to scan header | E-2 / V-05 only |
| **C-20** | Worked example embedded within each `[RULE]` annotation | E-3 / V-01 isolation finding |

**What each one captures that C-17 does not:**

- **C-18** — C-17 requires rule-to-slot co-location. C-18 requires that *all three enforcement layers* (declare, anchor LOCK, verify) converge at the same write-point position. V-03 passes C-17 + C-16 but fails C-18 because the LOCK anchor is absent at SLOT 3.

- **C-19** — C-17 allows generic labels like `[RULE COMPLETENESS]`. C-19 requires those labels to be propagated from a named contract register at the top of the spec through the inline annotation and into the scan header — giving the invariant three independent recovery points. V-04 uses locally correct but unlinked labels; V-05 is the only design that chains them.

- **C-20** — C-17 puts the rule at the governed slot. C-20 puts a correct/violation example at the same position. V-01 showed this sub-pattern is real and distinct — it doesn't compensate for missing C-15/C-16, but it is an independent compliance mechanism.

**Formula update:**

```
aspirational_pass/12 * 10   (was /9)
```

The v4 golden designs (V-04, V-05) now score 9/12 aspirational under v5 — the new criteria are live discriminators for Round 5.
sses on structural grounds but the output still contains backticks
  or angle brackets. Round 1 finding: catch-all prohibitions leave this gap open;
  explicit enumeration does not.
- **C-13 (COMPLETENESS/EXCLUSIVITY named invariants)** is aspirational — compound
  phrasing ("every name ... and only names") is functionally equivalent for the rubric
  criterion but less reliable in live runs where a model may fail each direction
  independently. Naming COMPLETENESS and EXCLUSIVITY as separate invariants makes each
  direction independently verifiable and closes the "used verbatim" ambiguity gap.
  Scored separately from C-11 because the mechanism (two named sub-rules vs. one
  compound constraint) is structurally distinct.
- **C-14 (branch sealing instruction)** is aspirational — explicit character
  prohibition (C-10) is necessary but not sufficient; a model reading both format
  branches may carry patterns across without a structural isolation directive. Round 2
  finding: the sealed-branches instruction ("do not reference the other branch's format
  descriptions") is the mechanism that makes C-12 achievable reliably, not merely the
  absence of a known contamination source.
- **C-15 (BLOCKERS LOCK directive)** is aspirational — COMPLETENESS and EXCLUSIVITY
  (C-13) constrain how the BLOCKERS list is *used*, but neither prevents the list from
  being silently revised between the pre-computation step and the write step. A
  standalone named LOCK directive ("The BLOCKERS list is now frozen -- no additions,
  removals, or revisions permitted in subsequent phases") makes list immutability a
  first-class obligation that cannot be conflated with the bidirectionality rule. Scored
  separately from C-13 because the mechanism (mutation guard vs. citation constraint)
  addresses a different failure mode: drift rather than omission or injection.
- **C-16 (in-render verification scan)** is aspirational — declarative rules
  (C-13, C-14, C-15) tell the model what is required but do not force it to check
  compliance at the moment of generation. An in-render verification scan (explicit
  COMPLETENESS CHECK and EXCLUSIVITY CHECK steps executed *before* writing the
  readiness sentence) converts a passive constraint into an active procedure: the model
  must enumerate BLOCKERS names, confirm each is present in the draft sentence, then
  enumerate draft names and confirm each is present in the BLOCKERS list. Round 3
  finding: the scan is the mechanism that makes C-13 robust across live runs, not merely
  the presence of the named sub-rules.
- **C-17 (inline [RULE] annotation style)** is aspirational — gathering rules into a
  preamble section keeps the specification readable but introduces distance between each
  rule and the template position it governs; a model may skip the preamble or fail to
  map preamble rules to the correct output slot. Embedding [RULE] markers at the exact
  template position they govern reduces this mapping gap to zero. Round 3 finding:
  zero-distance enforcement (rule co-located with governed text) is a distinct
  structural property from branch sealing (C-14) or explicit enumeration (C-10); a
  spec can satisfy either without the other.
- **C-18 (three-layer co-location at the write point)** is aspirational — C-17
  requires that each rule appear at its governed output slot, but does not require that
  all three enforcement layers (declaration, LOCK anchor, verification scan) converge at
  the same position. When [RULE] declares the constraint, the LOCKED list reference
  anchors immutability, and the verification scan executes -- all at SLOT 3 / Branch B
  Section 3 -- no cross-phase recall is required for any enforcement layer. Round 4
  finding: V-04 demonstrates this as the minimal golden design; V-03 achieves scan +
  inline (two layers at the write point) without the LOCK anchor, showing the third
  layer is a distinct structural contribution. Scored separately from C-17 because
  three-layer convergence is a stronger property than per-slot co-location alone.
- **C-19 (contract label chaining)** is aspirational — inline [RULE] annotations
  (C-17) and three-layer co-location (C-18) make each write-point self-contained, but
  do not guarantee that the rule names used at the write point are recoverable from a
  top-level contract register. A model whose attention degrades mid-generation may
  correctly apply a rule locally while losing the connection to the contract guarantee
  that motivated it. Assigning named labels at the contract register (e.g., G-7a,
  G-7b) and propagating those exact labels through inline [RULE G-7a/G-7b] annotations
  and scan headers (G-7a COMPLETENESS SCAN / G-7b EXCLUSIVITY SCAN) makes each
  invariant independently recoverable at three structural levels -- register, annotation,
  scan header -- without any cross-position lookup. Round 4 finding: V-05 is the only
  R4 design that achieves this chaining; V-04 uses generic [RULE COMPLETENESS] /
  [RULE EXCLUSIVITY] labels that are locally correct but not contract-linked. Scored
  separately from C-17 and C-18 because the mechanism (label propagation across
  structural levels) addresses a different failure mode: invariant-context loss rather
  than mapping distance or phase drift.
- **C-20 (worked example within [RULE] annotation)** is aspirational — a [RULE]
  annotation at the governed position (C-17) tells the model what the constraint
  requires but does not show what a compliant or non-compliant output looks like at
  that slot. Embedding compact correct/violation examples inside each inline annotation
  (e.g., "[RULE COMPLETENESS: ... correct: 'Not ready -- missing prove-analysis and
  review-design.' violation: 'Not ready -- missing signals.' (omits signal names)]")
  reduces translation distance from rule to output action beyond co-location alone: the
  model encounters both the constraint declaration and a sample output format at the same
  position. Round 4 finding: V-01 isolated this sub-pattern; it does not compensate for
  missing C-15 or C-16 (V-01 scored 97.8, not 100) but is a distinct compliance
  mechanism independent of LOCK and scan. Scored separately from C-17 because the
  mechanism (rule + example at governed position) is structurally distinct from
  co-location without an example.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Artifact written and path echoed** | completeness | essential | Output includes a write instruction that lands the report at a deterministic path and echoes that path after write; artifact must exist on disk |
| C-02 | **Progress table present with accurate counts** | correctness | essential | Table with one row per namespace, total/complete/open columns, counts from actual discovered signals, includes a completion percentage or status symbol |
| C-03 | **Open signals listed with owners** | coverage | essential | Every incomplete signal enumerated with an owner field (even if "unassigned"); no open signal silently omitted |
| C-04 | **Readiness statement present and calibrated** | correctness | essential | Single sentence or labeled field states ready/not ready/conditionally ready; consistent with signal counts in the progress table |
| C-05 | **Recommended next step present** | depth | essential | Output concludes with one concrete next action; next step matches the most critical open signal |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **`--format teams` produces compact ASCII card** | format | recommended | Single ASCII block, all four sections, <= 40 lines and <= 80 chars wide |
| C-07 | **Content matches topic-status output** | correctness | recommended | Signal counts, readiness state, and next step identical to `topic-status` for the same topic at the same point in time |
| C-08 | **Open signals include signal type and namespace** | coverage | recommended | Each open signal entry names both namespace and signal type, not just a freeform description |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Readiness statement references blocking signals** | depth | aspirational | Readiness statement names the specific signals that are blocking (e.g., "Not ready -- missing prove-analysis and review-design") rather than a generic message |
| C-10 | **Teams card prohibition is explicitly enumerated** | format | aspirational | The spec explicitly prohibits backtick characters, angle brackets (`<`, `>`), and markdown emphasis markers *by name* -- not satisfied by a catch-all phrase such as "no markdown syntax" |
| C-11 | **Output includes BLOCKERS pre-computation block** | depth | aspirational | Before the readiness statement, the output contains an explicit enumeration of essential OPEN signals (a BLOCKERS block); the readiness sentence references signal-type names drawn from that block and cannot introduce new names or omit names present in the block |
| C-12 | **Teams card passes character-level scan** | format | aspirational | Independent of C-10's specification check, the `--format teams` output contains zero backtick characters and zero angle-bracket characters when scanned character by character |
| C-13 | **Bidirectionality stated as two named invariants** | depth | aspirational | The BLOCKERS constraint is expressed as two separately named sub-rules -- COMPLETENESS (the readiness sentence must cite every name in the BLOCKERS block) and EXCLUSIVITY (the readiness sentence must not introduce any name absent from the BLOCKERS block) -- each verifiable independently; compound phrasing such as "every name ... and only names" does not satisfy this criterion |
| C-14 | **Branch sealing instruction present** | format | aspirational | The spec contains an explicit directive that separates the default and `--format teams` rendering paths -- e.g., "the branches are sealed; do not reference the other branch's format descriptions when executing" -- so that format patterns cannot bleed across branches even when a model processes both in a single pass; explicit character prohibition (C-10) alone does not satisfy this criterion |
| C-15 | **BLOCKERS LOCK directive present** | depth | aspirational | The spec contains a standalone named directive that explicitly freezes the BLOCKERS list after its pre-computation step -- e.g., "The BLOCKERS list is now frozen. No additions, removals, or revisions are permitted in subsequent phases." -- making list immutability a first-class obligation distinct from the COMPLETENESS/EXCLUSIVITY bidirectionality rules (C-13); the embedded clause "this list is closed" within the pre-computation step does not satisfy this criterion because it does not name the directive or assert it as a phase-spanning constraint |
| C-16 | **In-render verification scan present** | depth | aspirational | The spec instructs the model to execute an explicit two-step compliance scan *before* writing the readiness sentence: (1) COMPLETENESS CHECK -- enumerate every name in the BLOCKERS list and confirm each appears in the draft sentence; (2) EXCLUSIVITY CHECK -- enumerate every name in the draft sentence and confirm each appears in the BLOCKERS list; declarative statements of COMPLETENESS/EXCLUSIVITY (C-13) alone do not satisfy this criterion because they do not require active verification at generation time |
| C-17 | **Rules co-located with governed template positions** | format | aspirational | Constraint rules are embedded as inline markers (e.g., `[RULE ...]`) at the exact template position they govern -- not collected in a separate preamble or appendix -- so that zero mapping distance exists between each rule and the output slot it constrains; branch isolation achieved by two independently placed seal markers (one at the branch dispatch point, one at the Branch B entry point) rather than a single preamble directive; C-14's sealed-branch requirement and C-17's co-location requirement are independent: a spec can satisfy either without satisfying the other |
| C-18 | **Three-layer co-location at the write point** | depth | aspirational | At the readiness sentence write point (SLOT 3 and its `--format teams` equivalent), all three enforcement layers converge at the same structural position: (1) `[RULE]` annotation declares the COMPLETENESS/EXCLUSIVITY constraint; (2) an explicit reference to the LOCKED BLOCKERS list anchors list immutability at that position; (3) the in-render verification scan (C-16) executes immediately before writing -- so no cross-phase recall is required for any enforcement layer at the moment of generation; satisfying C-15, C-16, and C-17 independently does not satisfy this criterion if the LOCK anchor is absent at the write point itself; V-03 (scan + inline, no write-point LOCK anchor) demonstrates the gap |
| C-19 | **Contract label chaining from register to annotation to scan header** | depth | aspirational | Invariant names are assigned at a top-of-specification contract register (e.g., G-7a COMPLETENESS, G-7b EXCLUSIVITY) and those exact labels are propagated to the inline `[RULE G-7a/G-7b]` annotations at governed template positions and to the scan step headers (e.g., "G-7a COMPLETENESS SCAN") -- making the invariant independently recoverable at three structural levels (register, annotation, scan header) without any cross-position lookup; generic annotation labels such as `[RULE COMPLETENESS]` that are not linked to a named contract register entry do not satisfy this criterion |
| C-20 | **Worked example embedded within each `[RULE]` annotation** | format | aspirational | Each inline `[RULE]` annotation governing output phrasing (readiness sentence, next step) includes a compact correct/violation example immediately after the rule statement at the same position -- e.g., "[RULE COMPLETENESS: ... correct: 'Not ready -- missing prove-analysis and review-design.' violation: 'Not ready -- missing signals.' (omits signal names)]" -- so that the model encounters both the constraint declaration and a sample output format at the governed slot; a worked example collected in a separate section or preamble does not satisfy this criterion; structural-format rules (table borders, character counts) are exempt from this requirement |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-20 that pass   (max 12)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/12 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

**Notes**:
- Aspirational criteria are independent -- any combination can pass.
- C-15 (LOCK) and C-16 (scan) both address list integrity but via different mechanisms:
  C-15 guards against mutation between steps; C-16 guards against omission or injection
  at write time. A spec can include either without the other.
- C-17 (co-location) and C-14 (sealing) are orthogonal format properties.
  Co-location concerns rule-to-slot distance; sealing concerns branch-to-branch
  contamination. Both can be present, absent, or mixed independently.
- C-18 (three-layer co-location) requires C-15, C-16, and C-17 all to be satisfied *and*
  the LOCK anchor to appear at the write point itself -- not merely at the phase level.
  V-03 (scan + inline, no LOCK) demonstrates that C-16 + C-17 without a write-point
  LOCK anchor does not satisfy C-18.
- C-19 (contract label chaining) requires a named contract register -- a structurally
  distinct section before execution begins that assigns canonical label names to each
  invariant. Generic inline labels that happen to be consistent across positions satisfy
  C-17 but not C-19.
- C-20 (worked examples) is orthogonal to C-17, C-18, and C-19 -- a spec can embed
  examples without co-location, or co-locate rules without examples. V-01 demonstrated
  both C-17 and C-20 while failing C-15 and C-16, confirming independence.
- Under v5 the R4 golden designs (V-04, V-05) score 9/12 aspirational (75%), not 12/12,
  because C-18, C-19, C-20 are newly live. V-04 passes C-18 but not C-19 or C-20;
  V-05 passes C-18 and C-19 but not C-20; no R4 variation was designed to pass C-20
  in isolation without also testing it against the full rubric.
