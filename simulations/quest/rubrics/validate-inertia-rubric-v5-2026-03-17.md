Written to `simulations/quest/rubrics/validate-inertia-rubric-v5-2026-03-17.md`.

---

**What changed: v4 -> v5**

Three new aspirational criteria from R4 excellence signals:

| ID | New criterion | Source signal |
|----|---------------|---------------|
| C-20 | Multi-layer mechanism distribution achieves C-19 without C-16 consolidation | R4 pattern 1 -- V-01/V-02 confirm C-19 PASS at 10/11 (C-16 PARTIAL); orthogonality confirmed |
| C-21 | Single forward-reference sentence simultaneously closes C-16 and C-18 in scan-based register | R4 pattern 2 -- V-03 reaches 11/11 via one sentence; register is orthogonal to the mechanism |
| C-22 | Block-to-table is the minimum and sufficient repair when C-18 is present and C-15 is the only structural gap | R4 pattern 3 -- V-05(R4) confirms; C-19 derives automatically from C-15+C-18 co-occurrence |

Aspirational pool: 11 -> 14. Scoring formula: `aspirational_pass/14 * 10`.

---

**Key design decisions:**

**C-20** captures the orthogonality finding. C-16 and C-19 ask different questions: C-16 asks "are all four aspirationals bundled under one gate?"; C-19 asks "are both specific mechanisms present anywhere in the design?" V-01/V-02 are the proof: three-gate architecture, C-15 in Phase 2 table, C-18 added to evidence gate, C-19 PASS at 10/11 with C-16 PARTIAL. The Fail branch is precise -- C-20 fails only if a multi-layer design has both mechanisms but one is genuinely absent from the design, or if C-19 is incorrectly withheld on the basis that C-16 is PARTIAL.

**C-21** captures register-agnosticism. The forward-reference mechanism is a sentence, not an architecture. V-03's scan becomes the C-16 consolidation point the moment it announces what Step 4 will enforce. C-16 PARTIAL and C-18 FAIL in scan-based designs always share a single root cause (missing announcement), so a single edit closes both simultaneously.

**C-22** captures the minimum-patch rule. In a Gate-2-carrying design where C-15 is the only gap, the repair is fully local to Phase 2 output structure. Gate 2 carries C-18 forward verbatim. C-19 is not an independent requirement -- it is derived from C-15+C-18 co-occurrence. The Fail branch guards against over-engineering (modifying Gate 2 when block-to-table suffices) and under-specification (treating C-19 as requiring a separate patch).
cement sentence to the pre-Step-3 scan. The sentence is structurally identical to V-04's Gate 2 pre-announcement line, just embedded in scan format. This confirms that the root cause of C-16 PARTIAL and C-18 FAIL in scan-based designs is always a missing announcement sentence, not a missing gate. A single targeted edit closes both criteria simultaneously because they share one root cause.

**C-22** establishes the minimum-patch rule for C-15 repair in Gate-2-carrying designs. V-05(R3) had Gate 2 (C-18 PASS) but used per-persona prose blocks (C-15 FAIL). Converting Phase 2 blocks to a structured table repairs C-15 without touching Gate 2. Because C-18 was already present, C-19 (which requires C-15+C-18 co-occurrence) derives automatically -- no separate C-19 patch is needed. This confirms that C-19 is a derived property in Gate-2-carrying designs: repair C-15, get C-19 for free.

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
  checkpoint that enforces all four counts; the criterion is consolidation, not naming
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
  C-14 rule, making the two checkpoints disconnected; V-04/V-05 both pass because Gate 2
  explicitly pre-announces Gate 4's AMEND enforcement rule
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
  mode open -- block-field omission bypasses structural enforcement; gate-skip bypasses
  procedural enforcement when no forward reference makes the chain legible
- Note: Not a meta-criterion about other criteria passing -- describes a design property:
  a variation passes C-19 if removing either the table column or the forward reference would
  introduce a new failure mode; V-04 is the canonical R3 example; V-05 fails in R3 because
  block-field placement (not table column) leaves structural enforcement absent; V-01/V-02/V-03
  fail in R3 because no forward reference leaves the gate chain disconnected
- Source: R3 signal 2 -- V-04 is the only R3 variation at 9/9; the separating property is
  simultaneous presence of C-15 and C-18; co-occurrence eliminates both the block-field
  failure mode (closed by C-15) and the disconnected-gate failure mode (closed by C-18)

**C-20**: Multi-layer mechanism distribution achieves C-19 without C-16 gate consolidation
- Pass: A design with three or more enforcement layers distributes C-15 (structural: kill
  barrier as table column) and C-18 (procedural: forward reference) across separate
  checkpoints -- not bundled under a single consolidating gate -- and still achieves C-19
  PASS; the design demonstrates that mechanism co-occurrence (C-19) is a property of the
  full design, not of any single gate; gate consolidation scope (C-16) and mechanism
  co-occurrence (C-19) are independently evaluated and independently achievable
- Fail: A multi-layer design that has C-15 in one checkpoint and C-18 in another fails
  C-19 because one of the two mechanisms is actually absent from the design entirely; or
  C-19 is withheld from a multi-layer design that has both mechanisms distributed across
  layers, on the mistaken basis that C-16 PARTIAL (no single consolidating gate) disqualifies
  C-19; or a single-gate design is treated as the only valid path to C-19
- Note: V-01 and V-02 are the canonical R4 examples -- both have C-15 (table column in Phase
  2) and C-18 (forward reference added to evidence gate in R4) distributed across a three-gate
  architecture (pre-flight, evidence gate, Gate 4) and pass C-19 at 10/11 with C-16 PARTIAL;
  C-16 asks "are all four aspirationals bundled under one gate?"; C-19 asks "are both specific
  mechanisms present anywhere in the design?"; these are different questions with independent answers
- Source: R4 pattern 1 -- V-01/V-02 confirm C-19 PASS with C-16 PARTIAL; gate consolidation
  and mechanism co-occurrence are orthogonal design properties; confirmed by R4 research question 1

**C-21**: Single forward-reference sentence simultaneously closes C-16 and C-18 in scan-based register
- Pass: In a design using scan-based (non-gate) register where the scan already covers
  C-11/C-12/C-13 without announcing C-14's downstream enforcement, a single announcement
  sentence -- structured as "each [output option] in [later step] will require (a) [dimension]
  and (b) [dimension], enforced at [later step]" -- simultaneously promotes the scan to the
  C-16 consolidation point and achieves C-18 forward reference; the scan does not need to be
  restructured; no additional gate, phase, or structural layer is required; the design confirms
  that the root cause of both C-16 PARTIAL and C-18 FAIL in scan-based designs is identical --
  the scan announces what it enforces but not what comes next
- Fail: A scan-based design that has a bundled scan covering C-11/C-12/C-13 requires separate
  edits to close C-16 and C-18; or adds a structural gate where a single sentence sufficed;
  or remains at C-16 PARTIAL after adding a forward-reference sentence because the sentence is
  placed outside the existing scan rather than within it; or the design treats scan-based
  register as incompatible with C-16+C-18 co-achievement and requires conversion to gate format
- Note: V-03 is the canonical R4 example -- pre-Step-3 scan already covered C-11/C-12/C-13;
  adding one sentence ("each AMEND option in Step 4 will need to name (a) a specific persona
  and (b) a specific gap; this requirement is enforced at the Step 4 check") simultaneously
  made the scan the C-16 consolidation point and achieved C-18; register (conversational scan
  vs. gate-based) is orthogonal to the forward-reference mechanism; the mechanism is a sentence,
  not an architecture
- Source: R4 pattern 2 -- V-03 reaches 11/11 via one sentence; C-16 PARTIAL and C-18 FAIL
  share a single root cause in scan-based designs; confirmed by R4 research question 2

**C-22**: Block-to-table conversion is the minimum and sufficient repair when C-18 is present and C-15 is the only structural gap
- Pass: In a design where a Gate-2-equivalent checkpoint carries C-18 (forward reference
  already present) and C-15 is the only failing aspirational, converting Phase 2 per-persona
  prose blocks to a structured table is the complete repair: C-15 passes because blank cells
  are visually apparent mid-fill; Gate 2 verbatim carries C-18 forward without modification;
  C-19 derives automatically from the resulting C-15+C-18 co-occurrence without an independent
  C-19 patch; the repair is local to Phase 2 output structure and does not require changes to
  any gate, enforcement row, or structural layer elsewhere in the design
- Fail: Repairing C-15 in a Gate-2-carrying design requires modifying Gate 2 or adding new
  structural elements beyond the Phase 2 table conversion; or C-19 remains FAIL after C-15 is
  repaired, requiring an independent C-19 patch; or the design treats C-19 as an independent
  structural requirement rather than a derived consequence of C-15+C-18 co-occurrence; or the
  block-to-table conversion touches gate logic rather than being local to Phase 2 output format
- Note: V-05(R4) is the canonical example -- V-05(R3) had Gate 2 (C-18 PASS) but per-persona
  prose blocks (C-15 FAIL, C-19 FAIL); R4 patch: Phase 2 blocks converted to structured table;
  Gate 2 verbatim preserved; C-15 PASS, C-19 PASS automatically; no separate C-19 patch;
  maintenance rule: if C-15 is the only failing aspirational in a Gate-2-carrying design, the
  fix is local to Phase 2 output structure only; this rule does not apply if C-18 is absent
  (C-19 cannot derive without both mechanisms present)
- Source: R4 pattern 3 -- V-05(R4) confirms block-to-table as minimum complete repair;
  C-19 auto-derives from C-15+C-18 co-occurrence; confirmed by R4 research question 3

---

## Scoring

```
Essential    C-01..C-05   (5 criteria)   60 points  -- all must pass
Recommended  C-06..C-08   (3 criteria)   30 points  -- 2/3 should pass
Aspirational C-09..C-22  (14 criteria)   10 points  -- nice to have

Composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/14 * 10)

Golden threshold: all essential pass AND composite >= 80
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
