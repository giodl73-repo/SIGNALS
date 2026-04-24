`topic-report-rubric-v7-2026-03-14.md` written.

**What changed from v6:**

| ID | Criterion | Failure mode addressed |
|----|-----------|----------------------|
| **C-23** | Criterion-tagged violation example in `[RULE]` annotation | Violation names bad output pattern only; tag makes it criterion-recoverable (model knows *which* invariant, not just *what* is wrong) |
| **C-24** | Contract label chaining for single-position output invariants | C-19 covers bidirectional list invariants (three-level chain); NEXT STEP is a single-position invariant without a scan step -- G-9 INERTIA pattern gives it a two-level chain (register → annotation) |
| **C-25** | Branch B independent THREE-LAYER WRITE POINT header | Main-branch C-22 header requires cross-branch lookup on `--format teams` path; own Branch B header closes that gap independently |

**Formula:** `aspirational_pass/17 * 10` (was `/14`)

**R6 golden re-scores under v7:**

| Variation | v6 score | New criteria | v7 score |
|-----------|----------|-------------|---------|
| V-03 Inertia propagated | 100 | C-23 NO, C-24 NO, C-25 NO | **98.2** |
| V-04 Minimal golden | 100 | C-23 YES, C-24 NO, C-25 NO | **98.8** |
| V-05 Ceiling | 100 | C-23 NO, C-24 YES, C-25 YES | **98.8** |

V-04 and V-05 tie at 98.8 but discriminate cleanly: V-04 holds C-23, V-05 holds C-24+C-25. No R6 variation achieves 17/17 -- all three new criteria are live R7 discriminators.
lation example pair within each `[RULE]` annotation. C-23 is a sub-property of the violation half: the violation example explicitly identifies which criterion ID is being violated -- e.g., `(no stall cost -- C-21 violation)` -- making the failure mode criterion-traceable rather than only contrast-demonstrative. A spec with a correct violation example that does not name the criterion ID passes C-20 but not C-23. Round 6 finding: V-04 is the first design to carry this tag; the pattern is more reliable because a model encountering the violation knows which invariant is at stake, not merely which output form is wrong.

**Design note on C-24:** C-19 covers contract label chaining for bidirectional list invariants (COMPLETENESS / EXCLUSIVITY) that propagate through a pre-computation block and verification scan. NEXT STEP phrasing is a single-position invariant: it does not have a pre-computation block or a two-direction scan. Assigning a named register entry (G-9 INERTIA) and propagating that exact label to the inline `[RULE G-9 INERTIA]` annotation makes the invariant chain-traceable at two structural levels (register, annotation) without requiring a scan step. Round 6 finding: V-05 is the first design to apply the C-19 chaining pattern to a single-position invariant; earlier designs (V-04) use `[RULE NEXT-CONCRETE C-21]` annotation labels that are locally correct but not register-linked.

**Design note on C-25:** C-22 requires an explicit `=== THREE-LAYER WRITE POINT ===` header at SLOT 3 for the default execution path. A model executing Branch B (`--format teams`) must locate the default-branch header or reconstruct the layer sequence from surrounding spec context, introducing a cross-branch lookup step. A self-contained `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header within Branch B itself eliminates this step: the Branch B header enumerates LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY independently of the main branch header. Round 6 finding: V-05 is the only R6 design to carry a Branch B independent header; V-02, V-03, and V-04 pass C-22 via the main-branch header only. Scored separately from C-22 because the mechanism (branch-local recovery point vs. shared header) addresses a different failure mode: cross-branch attention loss on the `--format teams` path vs. mid-generation layer forgetting on the default path.

---

## Criterion Rationale

- **C-09 (readiness statement references blocking signals)** is aspirational -- a generic
  "Not ready" sentence passes C-04 (calibrated) but gives no actionable signal. Naming the
  specific blocking signals in the readiness sentence ("Not ready -- missing prove-analysis
  and review-design") is the minimal useful output for a developer deciding what to work on
  next.
- **C-10 (explicit enumeration of prohibited characters)** is aspirational -- a catch-all
  phrase such as "no markdown syntax" or "plain text only" passes on structural grounds but
  the output still contains backticks or angle brackets. Round 1 finding: catch-all
  prohibitions leave this gap open; explicit enumeration does not.
- **C-11 (BLOCKERS pre-computation block)** is aspirational -- a model asked to name
  blocking signals in a readiness sentence may hallucinate signal names or drop real ones if
  it must recall them from context mid-sentence. A dedicated pre-computation step that
  enumerates the essential OPEN signals before any sentence is written makes the BLOCKERS
  list a first-class artifact that subsequent phases must cite, not reconstruct.
- **C-12 (Teams card passes character-level scan)** is aspirational -- C-10 verifies the
  *specification* prohibits the characters; C-12 verifies the *output* contains none. Both
  are required because a model can correctly read a prohibition and still produce a
  non-compliant output under format pressure.
- **C-13 (COMPLETENESS/EXCLUSIVITY named invariants)** is aspirational -- compound
  phrasing ("every name ... and only names") is functionally equivalent for the rubric
  criterion but less reliable in live runs where a model may fail each direction
  independently. Naming COMPLETENESS and EXCLUSIVITY as separate invariants makes each
  direction independently verifiable and closes the "used verbatim" ambiguity gap.
  Scored separately from C-11 because the mechanism (two named sub-rules vs. one
  compound constraint) is structurally distinct.
- **C-14 (branch sealing instruction)** is aspirational -- explicit character
  prohibition (C-10) is necessary but not sufficient; a model reading both format
  branches may carry patterns across without a structural isolation directive. Round 2
  finding: the sealed-branches instruction ("do not reference the other branch's format
  descriptions") is the mechanism that makes C-12 achievable reliably, not merely the
  absence of a known contamination source.
- **C-15 (BLOCKERS LOCK directive)** is aspirational -- COMPLETENESS and EXCLUSIVITY
  (C-13) constrain how the BLOCKERS list is *used*, but neither prevents the list from
  being silently revised between the pre-computation step and the write step. A
  standalone named LOCK directive ("The BLOCKERS list is now frozen -- no additions,
  removals, or revisions permitted in subsequent phases") makes list immutability a
  first-class obligation that cannot be conflated with the bidirectionality rule. Scored
  separately from C-13 because the mechanism (mutation guard vs. citation constraint)
  addresses a different failure mode: drift rather than omission or injection.
- **C-16 (in-render verification scan)** is aspirational -- declarative rules
  (C-13, C-14, C-15) tell the model what is required but do not force it to check
  compliance at the moment of generation. An in-render verification scan (explicit
  COMPLETENESS CHECK and EXCLUSIVITY CHECK steps executed *before* writing the
  readiness sentence) converts a passive constraint into an active procedure: the model
  must enumerate BLOCKERS names, confirm each is present in the draft sentence, then
  enumerate draft names and confirm each is present in the BLOCKERS list. Round 3
  finding: the scan is the mechanism that makes C-13 robust across live runs, not merely
  the presence of the named sub-rules.
- **C-17 (inline [RULE] annotation style)** is aspirational -- gathering rules into a
  preamble section keeps the specification readable but introduces distance between each
  rule and the template position it governs; a model may skip the preamble or fail to
  map preamble rules to the correct output slot. Embedding [RULE] markers at the exact
  template position they govern reduces this mapping gap to zero. Round 3 finding:
  zero-distance enforcement (rule co-located with governed text) is a distinct
  structural property from branch sealing (C-14) or explicit enumeration (C-10); a
  spec can satisfy either without the other.
- **C-18 (three-layer co-location at the write point)** is aspirational -- C-17
  requires that each rule appear at its governed output slot, but does not require that
  all three enforcement layers (declaration, LOCK anchor, verification scan) converge at
  the same position. When [RULE] declares the constraint, the LOCKED list reference
  anchors immutability, and the verification scan executes -- all at SLOT 3 / Branch B
  Section 3 -- no cross-phase recall is required for any enforcement layer. Round 4
  finding: V-04 demonstrates this as the minimal golden design; V-03 achieves scan +
  inline (two layers at the write point) without the LOCK anchor, showing the third
  layer is a distinct structural contribution. Scored separately from C-17 because
  three-layer convergence is a stronger property than per-slot co-location alone.
- **C-19 (contract label chaining)** is aspirational -- inline [RULE] annotations
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
- **C-20 (worked example within each `[RULE]` annotation)** is aspirational -- a [RULE]
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
- **C-21 (inertia framing at NEXT STEP)** is aspirational -- C-05 requires a concrete
  next step and C-17 requires its governing rule to appear at the SLOT 4 position, but
  neither requires the rule to communicate the readiness consequence of deferring the
  action. A `[RULE NEXT-CONCRETE]` that states "Run /scout:feasibility (scout). Leaving
  this open holds the topic at Not Ready." converts the next step from a navigation label
  into a commitment statement: the model encodes both the action and the inertia cost of
  not taking it. Round 5 finding: V-05 is the only R5 design to carry this framing; V-04
  names the skill without the stall cost, confirming the pattern is a real design
  distinction. Scored separately from C-05 because inertia framing (action + consequence)
  is structurally distinct from concreteness (action + no generic fallback).
- **C-22 (explicit THREE-LAYER WRITE POINT header)** is aspirational -- C-18 requires
  all three enforcement layers to converge at the write point structurally, but structural
  convergence and named convergence are distinct reliability properties. An explicit
  `=== THREE-LAYER WRITE POINT ===` header that enumerates LAYER 1 DECLARE / LAYER 2
  ANCHOR / LAYER 3 VERIFY before the model encounters any enforcement layer creates a
  named recovery point: a model whose attention degrades mid-generation can re-read the
  header and reconstruct the expected layer sequence without searching the surrounding
  spec. Round 5 finding: V-02 and V-05 both carry this header; V-01, V-03, and V-04
  achieve structural C-18 without it and score identically under binary layer-presence
  scoring. The explicit header is a reliability mechanism (lower live-run variance) not
  captured by C-18's binary pass condition. Scored separately from C-18 because the
  mechanism (named checklist at the entry point) addresses attention recovery, a different
  failure mode from layer absence.
- **C-23 (criterion-tagged violation example in `[RULE]` annotation)** is aspirational --
  C-20 requires a correct/violation example pair within each `[RULE]` annotation, but
  does not require the violation example to name the criterion ID being violated. A
  violation example that states only the bad output pattern (e.g., "Run /scout:feasibility
  (scout).") is contrast-demonstrative; a violation example that appends the criterion tag
  (e.g., "(no stall cost -- C-21 violation)") is criterion-recoverable: a model
  encountering the violation knows which invariant is at stake and can trace it back to
  the register and governing rule without a scan. Round 6 finding: V-04 is the first
  design to carry this tag; the tagging pattern applies wherever C-20 is satisfied with
  a named invariant that has a rubric ID. Scored separately from C-20 because the
  mechanism (criterion ID embedded in violation text vs. contrast pair without ID)
  addresses a different failure mode: invariant traceability rather than format
  demonstration alone.
- **C-24 (contract label chaining for single-position output invariants)** is aspirational
  -- C-19 applies the register-to-annotation-to-scan-header chaining pattern to
  bidirectional list invariants (COMPLETENESS / EXCLUSIVITY), which have a pre-computation
  block and a two-direction scan step. NEXT STEP phrasing is a single-position invariant:
  it constrains one output slot without a pre-computation phase or scan. Assigning a named
  register entry (e.g., G-9 INERTIA) and propagating that exact label to the inline
  `[RULE G-9 INERTIA]` annotation makes the invariant chain-traceable at two structural
  levels (register, annotation) without requiring a scan step, which is the correct
  structural treatment for single-position invariants. Round 6 finding: V-05 is the first
  design to apply C-19's chaining pattern to a single-position invariant; V-04 uses
  `[RULE NEXT-CONCRETE C-21]` which is locally correct but not register-linked. Scored
  separately from C-19 because the mechanism (two-level chaining without a scan step vs.
  three-level chaining through a scan step) is structurally appropriate to a different
  class of invariant.
- **C-25 (Branch B independent THREE-LAYER WRITE POINT header)** is aspirational -- C-22
  requires an explicit `=== THREE-LAYER WRITE POINT ===` header at the default execution
  path write point (SLOT 3), but does not require Branch B (`--format teams`) to carry
  its own equivalent header. A model executing Branch B must either locate the
  main-branch header across a branch boundary or reconstruct the layer sequence from
  surrounding spec context, both of which require a cross-branch lookup step. A
  self-contained `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header within Branch B
  enumerates LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY independently, so a
  model in Branch B reconstructs the enforcement sequence without any cross-branch
  reference. Round 6 finding: V-05 is the only R6 design to carry a Branch B independent
  header; V-02, V-03, and V-04 pass C-22 via the main-branch header only. Scored
  separately from C-22 because the mechanism (branch-local recovery point vs. shared
  header) addresses a different failure mode: cross-branch attention loss on the
  `--format teams` path vs. mid-generation layer forgetting on the default path.

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
| C-21 | **Inertia framing at NEXT STEP** | depth | aspirational | The `[RULE]` annotation governing the recommended next step names both the concrete action *and* the readiness consequence of deferring it -- e.g., "Run /scout:feasibility (scout). Leaving this open holds the topic at Not Ready." -- converting the next step from a navigation label into a commitment statement; a rule that names only the skill or action without a stall-cost statement does not satisfy this criterion; C-05's concreteness requirement (no generic fallback steps) is necessary but not sufficient |
| C-22 | **Explicit THREE-LAYER WRITE POINT header present** | format | aspirational | The spec contains an explicit named header at the readiness write point (e.g., `=== THREE-LAYER WRITE POINT ===`) that enumerates all three enforcement layers -- LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY -- before the model encounters any of them, creating a named checklist that enables attention recovery mid-generation without a cross-spec search; structural C-18 (all three layers present without explicit labeling) does not satisfy this criterion; the header must appear at the write point itself, not in a preamble |
| C-23 | **Criterion-tagged violation example in `[RULE]` annotation** | format | aspirational | Within each `[RULE]` annotation that carries a correct/violation example pair (C-20), the violation example explicitly names the criterion ID being violated -- e.g., "(no stall cost -- C-21 violation)" -- making the failure mode criterion-traceable rather than only contrast-demonstrative; a violation example that shows an incorrect output pattern without naming the criterion ID does not satisfy this criterion even if it satisfies C-20; C-23 requires C-20 as a precondition but is not implied by it |
| C-24 | **Contract label chaining for single-position output invariants** | depth | aspirational | Single-position output invariants -- those that constrain one output slot without a pre-computation block or bidirectional scan (e.g., NEXT STEP phrasing) -- are assigned named register entries (e.g., G-9 INERTIA) at the top-of-specification contract register, and those exact labels are propagated to the inline `[RULE G-9 INERTIA]` annotation at the governed slot, making the invariant chain-traceable at two structural levels (register, annotation) without requiring a scan step; a `[RULE]` annotation whose label is not linked to a named register entry does not satisfy this criterion; C-19 covers bidirectional list invariants (register to annotation to scan header); C-24 covers single-position invariants (register to annotation only); both can be present independently |
| C-25 | **Branch B independent THREE-LAYER WRITE POINT header** | format | aspirational | The `--format teams` execution path contains its own self-contained `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header that enumerates LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY independently of the main-branch C-22 header, so that a model executing Branch B reconstructs the enforcement layer sequence without any cross-branch lookup; the main-branch C-22 header alone does not satisfy this criterion; the Branch B header must appear within Branch B itself, not in a shared preamble; C-22 (main branch) and C-25 (Branch B) are independent -- a spec can satisfy either without satisfying the other |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-25 that pass   (max 17)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/17 * 10)

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
  C-17 but not C-19. C-19 applies to bidirectional list invariants (three-level chain:
  register, annotation, scan header). C-24 applies to single-position invariants
  (two-level chain: register, annotation). Both can be present independently.
- C-20 (worked examples) is orthogonal to C-17, C-18, and C-19 -- a spec can embed
  examples without co-location, or co-locate rules without examples. V-01 demonstrated
  both C-17 and C-20 while failing C-15 and C-16, confirming independence.
- C-21 (inertia framing) is orthogonal to C-05 -- C-05 tests that the next step is
  concrete (not "gather more signals"); C-21 tests that the rule governing the next step
  also states the stall cost of deferral. V-04 passes C-05 and C-20 without C-21,
  confirming the distinction.
- C-22 (explicit header) is a reliability extension of C-18, not a replacement. A spec
  that passes C-22 necessarily passes C-18 (all three layers must be present to name them),
  but C-18 does not imply C-22 (structural convergence without naming).
- C-23 (criterion-tagged violation) requires C-20 as a precondition -- a spec cannot
  carry a criterion-tagged violation without first carrying a violation example. C-23 is
  not implied by C-20: any spec satisfying C-20 with an untagged violation passes C-20
  only. Round 6 finding: V-04 is the only R6 design with a criterion-tagged violation;
  the pattern applies wherever C-20 is satisfied with a named invariant that has a
  rubric ID.
- C-24 (single-position invariant chaining) is orthogonal to C-19 -- C-19 requires a
  pre-computation block and scan step as the third chain level; C-24 applies to invariants
  without those structures. A spec can satisfy C-19 without C-24 (bidirectional invariants
  chained, single-position invariants not) or C-24 without C-19 (single-position chained,
  list invariants unchained). V-05 is the first design to satisfy both.
- C-25 (Branch B independent header) is a reliability extension of C-22, not a
  replacement. A spec can pass C-22 (main branch header) without C-25 (no Branch B
  header), or pass both. C-22 and C-25 together close the attention-recovery gap for
  both execution paths independently. Round 6 finding: V-05 is the only R6 design
  achieving both; V-02, V-03, V-04 pass C-22 only.
- Under v7 the R6 goldens score differently: V-04 (15/17, gains C-23) scores 98.8;
  V-05 (15/17, gains C-24 + C-25) scores 98.8; V-03 (14/17) scores 98.2. C-23, C-24,
  and C-25 are live discriminators for Round 7. No R6 variation achieves 17/17.

---

## R7 Discriminator Candidates

| ID | Design question | V-isolation needed |
|----|-----------------|-------------------|
| C-23 vs C-20 | Does criterion-tagging the violation example reduce live-run criterion confusion beyond an untagged violation pair? | V-A: C-20 with untagged violation; V-B: C-20 + C-23 with tagged violation |
| C-24 vs C-21 | Does register-linking a single-position invariant (G-9 INERTIA) reduce stall-cost omission rate beyond a locally-correct `[RULE C-21]` annotation? | V-C: C-21 with unregistered annotation; V-D: C-21 + C-24 with G-9 register entry |
| C-25 vs C-22 | Does Branch B own header reduce Teams card layer-omission rate relative to main-branch-only header? | V-E: C-22 main header only; V-F: C-22 + C-25 both headers |
