Written to `simulations/quest/rubrics/validate-inertia-rubric-v6-2026-03-17.md`.

---

**What changed: v5 -> v6**

Three new aspirational criteria from R5 `new_patterns`:

| ID | Pattern | Criterion |
|----|---------|-----------|
| C-23 | V-05 Enforcement Bridge vs. V-02 unlabeled scan — naming is the only structural difference | Named Gate-2-equivalent checkpoint makes enforcement consolidation role legible from header alone |
| C-24 | C-22 scope confirmed architecture-agnostic — any C-18-carrying checkpoint qualifies | Gate-2-equivalent role declared architecture-agnostically in minimum-patch scope statement |
| C-25 | 13/14 ceiling provable by construction — C-16 PASS and C-20 PASS logically mutually exclusive | Structural mutual exclusion acknowledged, preventing ceiling prediction errors |

**Aspirational pool: 14 → 17. Scoring formula: `aspirational_pass/17 * 10`.**

Two existing criteria also got note updates:
- **C-16** note: added mutual exclusion statement ("C-16 PASS and C-20 PASS are mutually exclusive by construction")
- **C-20** note: same mutual exclusion statement added
- **C-22** note: updated to state architecture-agnostic scope explicitly

**New structural ceiling block in scoring section:**
```
Maximum achievable: 16/17 aspirational (C-16 or C-20, never both)
17/17 unreachable; top composite ceiling: 60 + 30 + 9.41 = 99.41
```
 scan achieve identical C-16/C-18 coverage; the only difference is that V-05
names the checkpoint and V-02 does not. No existing criterion distinguishes these designs. The Fail
branch is precise: structural equivalence is present but role identification requires tracing the
checkpoint body rather than reading the label.

**C-24** extends C-22's minimum-patch rule from full Gate-2 designs to any C-18-carrying
checkpoint, and requires the design to make this scope explicit in its own language. R4 confirmed
the rule for full gates; R5 closes the architecture question: narrow evidence gates (V-01) and
scan-based registers (V-02, V-05) both carry C-18 and satisfy C-22 under the architecture-agnostic
scope. C-24 captures whether a non-full-gate design declares the minimum-patch scope explicitly --
stating that block-to-table is the complete repair without requiring gate restructuring -- rather
than relying on the evaluator to apply the scope extension. A design can pass C-22 (rule applied
correctly) and fail C-24 (rule unstated in the design itself).

**C-25** encodes the ceiling proof as a rubric criterion. C-16 PASS requires all four aspirationals
bundled under one gate; C-20 PASS requires multi-layer distribution without that consolidation.
No design can simultaneously be and not be gate-consolidated. The mutual exclusion is definitional,
not empirical. C-25 verifies that rubric users apply this correctly during score prediction, not
only during final scoring. The Fail branch uses the V-03 prediction error as the canonical example:
the coverage table correctly showed C-20+C-21 both FAIL (= 12/14), but the pass count row stated
13/14, ignoring the mutual exclusion. The ceiling for v6 is 16/17 -- C-16 or C-20, never both.

---

## Criteria Detail

### Essential (must pass)

**C-01**: Per-persona inertia analysis present
- Pass: Output analyzes at least 2 distinct personas, each with at least 1 named
  inertia dimension (e.g., switching cost, habit lock-in, social proof requirement)
- Fail: Single persona analyzed; or multiple personas mentioned but no dimension
  breakdown per persona

**C-02**: Per-persona inertia score with rationale
- Pass: Each analyzed persona receives an inertia score (numeric, HIGH/MED/LOW, or
  equivalent) with at least one sentence explaining why that score was assigned
- Fail: Scores listed without rationale; or rationale present but no score

**C-03**: Overall adoption inertia risk verdict
- Pass: Output explicitly synthesizes per-persona findings into a single overall
  verdict on adoption inertia risk -- labeled as the conclusion, not buried in a
  per-persona block
- Fail: Per-persona scores present but no synthesis; or synthesis present but
  not labeled as the overall adoption risk conclusion

**C-04**: Kill barrier explicitly named and prioritized
- Pass: Output explicitly names the single barrier most likely to block adoption
  regardless of feature quality -- the one thing that, if unresolved, means the
  feature ships but is never used
- Fail: Multiple barriers listed equally with no prioritization; or barriers framed
  only as "risks to mitigate" without naming the adoption killer

**C-05**: Workaround satisfaction addressed
- Pass: Output identifies what the current workaround is for at least the
  highest-inertia persona, and explicitly assesses how satisfied that persona is
  with it (e.g., "good enough," "painful but familiar," "actively seeking replacement")
- Fail: Inertia discussed in the abstract without grounding in what users are
  currently doing instead

---

### Recommended (should pass)

**C-06**: Switching cost quantified or estimated
- Pass: At least one persona's switching cost is given a concrete estimate --
  time, training, workflow disruption, or team coordination overhead -- not just
  labeled HIGH/LOW
- Fail: Switching costs named but described only in qualitative terms with no
  effort to anchor magnitude

**C-07**: Social proof requirements assessed
- Pass: Output addresses whether adoption requires seeing others succeed first
  (social proof threshold) for at least one persona -- early adopter vs.
  wait-and-see vs. mandate-required
- Fail: Social proof not mentioned, or addressed only in a single parenthetical
  without per-persona differentiation

**C-08**: Habit lock-in mechanism named
- Pass: Output identifies the specific habit or workflow that inertia is anchoring --
  what muscle memory, tool, or process makes the current behavior self-reinforcing
- Fail: "Habit lock-in" mentioned as a category but no specific habit named;
  or habit named without explaining why it is self-reinforcing

---

### Aspirational (raise the bar)

**C-09**: Inertia reduction conditions stated
- Pass: Output identifies the specific conditions under which each HIGH-inertia
  persona would voluntarily adopt -- what would have to change in their environment,
  team, or incentives for inertia to lose
- Fail: Barriers identified but no "inertia loses when..." framing; output stops
  at diagnosis without prescription

**C-10**: AMEND options are persona-specific and actionable
- Pass: Skill offers at least two AMEND options that are concrete adjustments --
  focus on a specific persona, quantify a specific switching cost, or identify the
  one kill barrier -- not generic "expand scope" suggestions
- Fail: AMEND offered as "you could also look at X" without tying the adjustment
  to a named persona or a specific gap in the current output

**C-11**: Kill barrier grounded in per-persona confirmation evidence
- Pass: The kill barrier conclusion is supported by explicit per-persona evidence --
  at least one persona is shown to confirm, partially confirm, or disconfirm the
  kill barrier, and the final verdict reflects that confirmation rather than being
  asserted as a terminal synthesis guess
- Fail: Kill barrier stated as a synthesis conclusion without any per-persona
  confirmation step; or hypothesis stated but no persona evidence collected
- Source: V-05 kill barrier hypothesis-test loop (surface in PHASE 1, test per-
  persona in PHASE 2, confirm/revise in dedicated PHASE 3)

**C-12**: Workaround satisfaction assessed per-persona even when feature-level or competitor-level data exists
- Pass: Each persona block includes an explicit workaround satisfaction assessment
  using satisfaction vocabulary (e.g., "good enough," "painful but familiar,"
  "actively seeking replacement") even when feature-level or competitor-level
  satisfaction is already established elsewhere in the output; the per-persona
  assessment is not proxied by relationship level (Heavy/Occasional/Rare) or
  adoption stage alone
- Fail: Workaround satisfaction established only at feature or competitor level,
  with per-persona blocks relying on relationship level as a proxy; or per-persona
  satisfaction omitted on the assumption that feature-level data is sufficient
- Source: V-03 gap confirmed -- competitor satisfaction at feature level does not
  propagate to per-persona blocks

**C-13**: No required field left blank, "unknown," or satisfied with a bare label
- Pass: Every required dimension (inertia score, switching cost, workaround
  satisfaction) has a substantive value for all assessed personas -- not "unknown,"
  "N/A," or an unlabeled blank; if a dimension is genuinely unavailable, the output
  names the specific information needed to fill it and why it matters
- Fail: Any required dimension left blank; marked "unknown" without a note on what
  would resolve it; or satisfied with a bare label ("HIGH") that passes nominal
  inspection without conveying actual information
- Source: V-01 visible blank enforcement -- pre-printed table rows make
  dimension-skipping legible mid-fill; anti-vague instruction at column level
  closes the nominal-satisfaction escape hatch

**C-14**: Each AMEND option names a persona AND a specific gap
- Pass: Every AMEND option explicitly identifies (a) a named persona and (b) a
  specific dimension or gap (e.g., "quantify switching cost for [Persona X],"
  "confirm kill barrier for [Persona Y]," "re-assess workaround satisfaction for
  [Persona Z] using satisfaction vocabulary"); generic scope expansions do not qualify
- Fail: Any AMEND option lacks a named persona; or names a persona but not a gap;
  or is framed as "you could also look at X" without anchoring to output content
- Source: V-05 AMEND gate -- gate checks that each option references a named
  persona or specific gap before the artifact writes; catches generic drift at
  output time

**C-15**: Kill barrier confirmation embedded as a per-persona table column
- Pass: The kill barrier confirmation field is a required column in the structured
  per-persona table -- not a separate verdict block, not a per-block prose field
  outside the table; a skipped or blank confirmation is visually apparent as an
  empty cell during fill, making omission impossible to hide without a structural gap
- Fail: Kill barrier confirmation handled in a separate verdict section or per-persona
  prose block that is not part of the primary table structure; blank enforcement
  depends on post-hoc review rather than structural column visibility
- Note: Represents the strongest implementation of C-11 -- C-11 requires evidence
  exist; C-15 requires the evidence slot be structurally impossible to skip silently
- Source: R2 signal 1 -- V-04 and V-05 both hit 100 in R2; the decisive mechanism was
  confirmation as a table column where blank = visible failure mid-fill

**C-16**: Single gate bundles all four aspirational checks simultaneously
- Pass: A single gate checkpoint (or named gate phase) enforces C-11 kill barrier
  confirmation, C-12 per-persona satisfaction vocabulary, C-13 no-bare-labels, and
  C-14 AMEND persona+gap in one enforced output pass; all four aspirational requirements
  checked at one structural point rather than across four separate layers or instructions
- Fail: Aspirational criteria enforced by separate instructions, separate gates, or
  separate phases with no consolidation point; enforcement depth equivalent but
  cognitive overhead higher and a model skip of any one layer leaves a gap
- Note: Does not require the gate to be labeled "Gate 2" -- any consolidated
  checkpoint that enforces all four counts; the criterion is consolidation, not naming.
  C-16 PASS and C-20 PASS are mutually exclusive by construction: a design cannot
  simultaneously consolidate all four aspirationals under one gate (C-16) and distribute
  them across multiple layers without a consolidation point (C-20); see C-25 for the
  ceiling implication
- Source: R2 signal 2 -- Gate 2 in V-04/V-05 bundles C-11/C-12/C-13/C-14 into one
  checkpoint; more efficient than four separate enforcement layers at equivalent depth

**C-17**: Aspirational enforcement achieved through mechanism, not explicit labels
- Pass: The variation achieves full enforcement of C-11 through C-14 through
  structural mechanisms (table columns, gate sequence, ENFORCEMENT rows) that
  are self-enforcing independent of whether aspirational labels such as (A), (B),
  (C), (D) are present; removing the labels would not allow any of C-11..C-14 to slip
- Fail: Aspirational compliance depends on explicit labels to trigger model attention;
  without the labels the structural mechanisms would permit C-11..C-14 to be satisfied
  only nominally or skipped; the labels are load-bearing rather than additive
- Note: V-04 is the canonical form (no labels; mechanism sufficient); V-05 also passes
  because its labels are additive, not load-bearing -- removing them leaves the mechanism
  intact; a variation where labels are the primary enforcement mechanism fails this criterion
- Source: R2 signal 3 -- convergence ceiling confirmed: V-04 reaches 100 without
  explicit aspirational labels; mechanism integration is load-bearing; labeling is not

**C-18**: Consolidated gate includes explicit forward reference to downstream enforcement gate
- Pass: The consolidation checkpoint not only enforces its immediate criteria (C-11/C-12/C-13)
  but also pre-announces the enforcement rule of any downstream gate (e.g., "each AMEND option
  in Phase N will require (a) a named persona and (b) a specific gap, enforced at Gate N+1");
  the chain between early and late gates is legible from the first checkpoint
- Fail: Each gate enforces its own criteria in isolation; all aspirational criteria may be
  covered across separate gates but no gate announces what a downstream gate will enforce;
  the relationship between checkpoints requires the reader to trace the design, not read it
- Note: Distinguishes C-16 PASS from C-16 PARTIAL -- V-01/V-02/V-03 cover all four
  aspirational criteria across separate gates but fail C-18 because no gate pre-announces
  another; V-03's pre-Step-3 scan covers C-11/C-12/C-13 but does not announce Step 4's
  C-14 rule; V-04/V-05 both pass because Gate 2 explicitly pre-announces Gate 4's AMEND
  enforcement rule
- Source: R3 signal 1 -- forward reference is the load-bearing mechanism for C-16 consolidation;
  PARTIAL on C-16 always traces to absent forward reference, not absent coverage

**C-19**: Structural enforcement and procedural enforcement co-occur in the same design
- Pass: The variation contains both (a) a table-column placement for the kill barrier
  confirmation field (C-15: structural enforcement -- a blank cell is visible mid-fill)
  and (b) a consolidated gate with explicit forward reference (C-18: procedural enforcement --
  the gate chain is legible from the first checkpoint); neither alone is sufficient and both
  must be present in the same artifact
- Fail: Either structural enforcement is absent (kill barrier confirmation is in a prose block,
  not a table column) or procedural enforcement is absent (gate checkpoints are disconnected
  with no forward reference); a design that achieves one without the other leaves one failure
  mode open
- Note: Not a meta-criterion about other criteria passing -- describes a design property:
  a variation passes C-19 if removing either the table column or the forward reference would
  introduce a new failure mode; V-04 is the canonical R3 example; the separating property is
  simultaneous presence of C-15 and C-18
- Source: R3 signal 2 -- V-04 is the only R3 variation at 9/9; co-occurrence eliminates both
  the block-field failure mode (closed by C-15) and the disconnected-gate failure mode (closed
  by C-18)

**C-20**: Multi-layer mechanism distribution achieves C-19 without C-16 gate consolidation
- Pass: A design with three or more enforcement layers distributes C-15 (structural: kill
  barrier as table column) and C-18 (procedural: forward reference) across separate
  checkpoints -- not bundled under a single consolidating gate -- and still achieves C-19
  PASS; the design demonstrates that mechanism co-occurrence (C-19) is a property of the
  full design, not of any single gate
- Fail: A multi-layer design that has C-15 in one checkpoint and C-18 in another fails
  C-19 because one of the two mechanisms is actually absent from the design entirely; or
  C-19 is withheld from a multi-layer design that has both mechanisms distributed across
  layers on the mistaken basis that C-16 PARTIAL disqualifies C-19; or a single-gate design
  is treated as the only valid path to C-19
- Note: V-01 and V-02 are the canonical R4 examples -- both distribute C-15 and C-18 across
  a three-gate architecture and pass C-19 with C-16 PARTIAL; C-16 asks "are all four
  aspirationals bundled under one gate?"; C-19 asks "are both specific mechanisms present
  anywhere in the design?"; these are different questions with independent answers.
  C-20 PASS and C-16 PASS are mutually exclusive by construction -- a design cannot
  simultaneously distribute and consolidate; see C-25 for the ceiling implication
- Source: R4 pattern 1 -- V-01/V-02 confirm C-19 PASS with C-16 PARTIAL; gate consolidation
  and mechanism co-occurrence are orthogonal design properties

**C-21**: Single forward-reference sentence simultaneously closes C-16 and C-18 in scan-based register
- Pass: In a design using scan-based (non-gate) register where the scan already covers
  C-11/C-12/C-13 without announcing C-14's downstream enforcement, a single announcement
  sentence -- structured as "each [output option] in [later step] will require (a) [dimension]
  and (b) [dimension], enforced at [later step]" -- simultaneously promotes the scan to the
  C-16 consolidation point and achieves C-18 forward reference; no additional gate, phase,
  or structural layer is required
- Fail: A scan-based design requires separate edits to close C-16 and C-18; or adds a
  structural gate where a single sentence sufficed; or remains at C-16 PARTIAL after adding
  a forward-reference sentence because the sentence is placed outside the existing scan
  rather than within it; or the design treats scan-based register as incompatible with
  C-16+C-18 co-achievement
- Note: V-03 is the canonical R4 example -- pre-Step-3 scan covered C-11/C-12/C-13; one
  announcement sentence simultaneously made the scan the C-16 consolidation point and
  achieved C-18; register (conversational scan vs. gate-based) is orthogonal to the
  forward-reference mechanism; the mechanism is a sentence, not an architecture
- Source: R4 pattern 2 -- V-03 reaches 11/11 via one sentence; C-16 PARTIAL and C-18 FAIL
  share a single root cause in scan-based designs

**C-22**: Block-to-table conversion is the minimum and sufficient repair when C-18 is present and C-15 is the only structural gap
- Pass: In a design where any Gate-2-equivalent checkpoint carries C-18 (forward reference
  already present) and C-15 is the only failing aspirational, converting Phase-N per-persona
  prose blocks to a structured table is the complete repair: C-15 passes; the C-18-carrying
  checkpoint is preserved verbatim without modification; C-19 derives automatically from
  the resulting C-15+C-18 co-occurrence without an independent C-19 patch; the repair is
  local to Phase-N output structure only. The Gate-2-equivalent is any checkpoint carrying
  C-18 -- full consolidating gate, narrow evidence gate, or scan-based register
- Fail: Repairing C-15 in a C-18-carrying design requires modifying the checkpoint or adding
  new structural elements beyond the Phase-N table conversion; or C-19 remains FAIL after
  C-15 is repaired; or the minimum-patch rule is applied only to full-consolidating-gate
  designs and not to narrow evidence gates or scan-based checkpoints carrying C-18
- Note: V-05(R4) is the canonical full-gate example; V-01 (narrow evidence gate) and
  V-02/V-05 (scan-based) in R5 confirm the rule is architecture-agnostic -- block-to-table
  is the complete local repair regardless of checkpoint form; this rule does not apply if
  C-18 is absent (C-19 cannot derive without both mechanisms present)
- Source: R4 pattern 3 + R5 pattern 2 -- V-05(R4) confirms for full gates; R5 confirms for
  narrow gates and scans; C-22 scope is architecture-agnostic

**C-23**: Named Gate-2-equivalent checkpoint makes enforcement consolidation role legible from header alone
- Pass: The design's C-18-carrying checkpoint -- whether a full gate, narrow evidence gate,
  or scan-based register -- carries an explicit header name or label that identifies its role
  as the enforcement consolidation point (e.g., "Enforcement Bridge," "Kill Barrier Gate 2,"
  "Consolidation Scan"); a reader encountering the design for the first time understands the
  checkpoint's consolidation function from the label alone, without reading the checkpoint
  body or tracing the enforcement chain
- Fail: The checkpoint achieves structural enforcement equivalence -- carries C-18, covers
  relevant aspirational checks -- but is unlabeled or named only by its position (e.g.,
  "pre-Step-4 scan," "Gate 2" with no role label); role identification requires the reader
  to trace the checkpoint body; V-02's unlabeled pre-Step-4 scan is the canonical fail case:
  structurally identical to V-05's Enforcement Bridge in C-16/C-18 coverage and enforcement
  depth, but the consolidation role is implicit rather than declared
- Note: Captures a legibility dimension orthogonal to enforcement depth; C-16 and C-18 verify
  that consolidation and forward reference are present; C-23 verifies that the consolidation
  role is immediately legible from the checkpoint header; naming is the separating variable
  between V-02 (C-23 FAIL) and V-05 (C-23 PASS) at equivalent enforcement depth; V-04's
  "Kill Barrier Gate 2" also passes; the criterion is label presence, not any specific text
- Source: R5 pattern 1 -- V-05 Enforcement Bridge vs. V-02 unlabeled scan; identical
  enforcement structure; naming is the only structural difference; legibility-from-header
  not captured by any existing criterion

**C-24**: Gate-2-equivalent role declared architecture-agnostically in minimum-patch scope statement
- Pass: A design that carries C-18 in a non-full-gate checkpoint (narrow evidence gate or
  scan-based register) explicitly states, in or adjacent to that checkpoint's enforcement
  language, that block-to-table is the complete repair for C-15 when C-18 is already present
  -- without requiring gate restructuring; the minimum-patch scope declaration uses
  architecture-neutral framing (e.g., "converting Phase-N blocks to a structured table is
  the complete local repair; this checkpoint is unchanged") that makes the rule legible within
  the design itself rather than requiring the evaluator to apply the scope extension
- Fail: A non-full-gate design carrying C-18 omits explicit minimum-patch scope declaration;
  whether block-to-table is the complete repair requires external inference rather than being
  stated in the design; or the design's enforcement language implies gate modification is
  required for C-15 repair when the C-18-carrying checkpoint already exists and needs no
  change; or the Gate-2-equivalent concept is invoked only for full-consolidating-gate designs
- Note: Extends C-22's scope declaration requirement to non-full-gate architectures; a design
  can pass C-22 (minimum-patch rule applied correctly by the evaluator) and fail C-24 (rule
  unstated in the design itself); V-01 is the canonical borderline case -- narrow evidence gate
  carries C-18, block-to-table is local repair, C-22 PASS; C-24 requires the design to declare
  this explicitly in its own checkpoint language
- Source: R5 pattern 2 -- C-22 scope confirmed architecture-agnostic; any C-18-carrying
  checkpoint qualifies as Gate-2-equivalent; C-24 captures whether the design makes this
  legible internally; R4 open question closed

**C-25**: Structural mutual exclusion between C-16 PASS and C-20 PASS acknowledged, preventing ceiling prediction errors
- Pass: A design targeting multi-layer distribution (C-20 candidate) explicitly acknowledges --
  through its architecture, coverage table, or score commentary -- that C-16 PASS and C-20 PASS
  are mutually exclusive by construction; if the design achieves multi-layer distribution (no
  single consolidation gate), it does not claim C-16 PASS; any score prediction for the design
  correctly reflects that C-16 and C-20 cannot both contribute, and treats 16/17 as the
  structural ceiling for multi-layer designs rather than an empirical observation
- Fail: A multi-layer design claims or implies C-16 PASS alongside C-20 PASS in the same
  coverage assessment; or a coverage table assigns a pass count that includes both without
  subtracting the mutual exclusion; or the ceiling is treated as an empirical finding rather
  than a logical consequence of the C-16/C-20 definitions; V-03 prediction error is the
  canonical fail case -- coverage table correctly showed C-20+C-21 both FAIL (= 12/14) but
  the pass count row stated 13/14, failing to apply the mutual exclusion to the counting step
- Note: Ceiling proof: C-16 PASS requires "all four aspirationals bundled under one gate";
  C-20 PASS requires "multi-layer distribution without that consolidation"; no design can
  simultaneously have and not have a single consolidation gate; this is a definitional
  constraint, not an empirical pattern; the v6 ceiling for C-21 designs (C-16 PASS, C-20 FAIL)
  is 16/17; the v6 ceiling for C-20 designs (C-20 PASS, C-16 FAIL) is also 16/17; 17/17 is
  unreachable by construction in any aspirational pool containing both C-16 and C-20
- Source: R5 pattern 3 -- 13/14 ceiling provable by construction; C-16 PASS and C-20 PASS
  logically mutually exclusive; V-03 prediction error confirmed (coverage table correct,
  count row wrong); 17/17 unreachable established for v6 aspirational pool

---

## Scoring

```
Essential    C-01..C-05   (5 criteria)   60 points  -- all must pass
Recommended  C-06..C-08   (3 criteria)   30 points  -- 2/3 should pass
Aspirational C-09..C-25  (17 criteria)   10 points  -- nice to have

Composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/17 * 10)

Golden threshold: all essential pass AND composite >= 80

Structural ceiling notes:
  - C-16 PASS and C-20 PASS are mutually exclusive by construction (see C-25)
  - Maximum achievable: 16/17 aspirational (either C-16 or C-20, never both)
  - 17/17 is unreachable; 16/17 = 9.41 aspirational points
  - Top composite ceiling: 60 + 30 + 9.41 = 99.41
```

---

## Rubric Change Log

| Version | Change | Source |
|---------|--------|--------|
| v1 | Initial -- 5E, 3R, 2A (10 criteria) | Skill description + validate namespace spec |
| v2 | Add C-11..C-14 (4 new aspirational) from R1 excellence signals; aspirational pool 2 -> 6 | R1 scorecard (validate-inertia-scorecard-R1-2026-03-17.md) |
| v3 | Add C-15..C-17 (3 new aspirational) from R2 excellence signals; aspirational pool 6 -> 9 | R2 scorecard (validate-inertia-scorecard-R2-2026-03-17.md) |
| v4 | Add C-18..C-19 (2 new aspirational) from R3 excellence signals; aspirational pool 9 -> 11 | R3 scorecard (validate-inertia-scorecard-R3-2026-03-17.md) |
| v5 | Add C-20..C-22 (3 new aspirational) from R4 excellence signals; aspirational pool 11 -> 14 | R4 scorecard (validate-inertia-scorecard-R4-2026-03-17.md) |
| v6 | Add C-23..C-25 (3 new aspirational) from R5 excellence signals; aspirational pool 14 -> 17; update C-16 and C-20 notes with mutual exclusion; update C-22 note with architecture-agnostic scope; add structural ceiling to scoring block | R5 scorecard (validate-inertia-scorecard-R5-2026-03-17.md) |
