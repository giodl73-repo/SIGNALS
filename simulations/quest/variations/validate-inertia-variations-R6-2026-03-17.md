Written to `simulations/quest/variations/validate-inertia-variations-R6-2026-03-17.md`.

---

## R6 Variations — validate-inertia

**5 complete prompt variations, targeting C-23 / C-24 / C-25 from rubric v6.**

### Summary

| V | Axis | Target | Predicted |
|---|------|--------|-----------|
| V-01 | Phrasing register (conversational) | C-23 single-axis — rename "PRE-STEP-4 SCAN" → "KILL BARRIER CONSOLIDATION SCAN" | 14/17 → 98.24 |
| V-02 | Output format (explicit scope note) | C-24 single-axis — add ARCHITECTURE SCOPE block to KILL BARRIER EVIDENCE GATE | 14/17 → 98.24 |
| V-03 | Lifecycle emphasis (Phase/Gate) | C-25 single-axis — add DESIGN NOTE on C-16/C-20 mutual exclusion | 13 or 14/17 → 97.65 or 98.24 |
| V-04 | Role sequence (data-before-hypothesis) | C-23+C-24 combined — new scan design with role label + SCOPE NOTE | 15/17 → 98.82 |
| V-05 | Inertia framing (status-quo as rival) | C-23+C-24+C-25 all three — V-05 R5 + SCOPE NOTE + mutual exclusion | **16/17 → 99.41 (ceiling)** |

### Key structural notes

- **V-01**: Purely a C-23 test. Only one word changes from V-02 R5 — the scan label. Cleanest single-axis isolation possible.
- **V-02**: C-24 on a three-layer (C-20) base. V-01 R5 already passes C-23; adding the ARCHITECTURE SCOPE block is the only new element.
- **V-03**: C-25 ambiguity probe. C-25 pass condition says "a design targeting multi-layer distribution (C-20 candidate)" — V-03 is C-16 path. Scoring resolves whether a C-16 design making the acknowledgment also qualifies.
- **V-04**: Role sequence inversion (audit → hypothesis vs. hypothesis → audit). C-21 path with "KILL BARRIER ENFORCEMENT SCAN" (C-23) + SCOPE NOTE (C-24). Predicted +2 over any R5 C-21 baseline.
- **V-05**: Ceiling design. V-05 R5 already at 14/17 under v6 (passes C-23). Two additions: SCOPE NOTE in ENFORCEMENT BRIDGE (C-24) + DESIGN NOTE on mutual exclusion (C-25) → 16/17 = 99.41, the hard ceiling (17/17 unreachable by construction).

### Open questions R6 scoring will resolve

1. Does C-25 require a C-20-path design, or does any explicit mutual-exclusion acknowledgment pass? (V-03 is the probe)
2. Does the SCOPE NOTE inside a scan block satisfy C-24's "in or adjacent to checkpoint enforcement language"? (V-04, V-05)
3. Does a C-21-path design making the C-25 acknowledgment also pass C-25, or does the criterion specifically require multi-layer architecture? (V-05)
n says "a design
targeting multi-layer distribution (C-20 candidate)"), or does any design that explicitly
acknowledges the mutual exclusion pass? V-03 tests a C-16 path design. If C-25 requires C-20
path, V-03 stays at 13/17 (net +0 from R5 baseline); if any explicit acknowledgment qualifies,
V-03 reaches 14/17 (net +1). Either outcome informs R7 design.

---

## V-01 (R6): Conversational Scan with Role-Communicating Label -- C-23 Single-Axis

**Axis:** Phrasing register (conversational throughout). Single-axis target: C-23. Base:
V-02 R5, which uses a "PRE-STEP-4 SCAN" label -- positional, not role-communicating. Change:
rename the scan to "KILL BARRIER CONSOLIDATION SCAN" -- a label that identifies the
checkpoint's enforcement consolidation role from the header alone. No structural changes.

**Hypothesis:** The only change needed to pass C-23 in a C-21-path design is renaming the
pre-verdict scan from a positional label to a role-communicating label. C-16 PASS, C-21 PASS,
C-23 PASS. All mechanism enforcement (table column for C-15, scan for C-11/C-12/C-13/C-18)
is unchanged. This tests C-23 in complete isolation.

```
You are running /validate-inertia for: {{feature}}

Map the adoption inertia per persona. One question drives this analysis: why would users
not adopt this feature even if it works perfectly?

---

STEP 1: THE CURRENT WORKAROUND

Name the status quo for this feature:
- What users are doing today instead
- Which personas rely on the workaround most heavily
- The dominant workaround satisfaction level using vocabulary: "good enough" /
  "painful but familiar" / "actively seeking replacement"

---

STEP 2: KILL BARRIER HYPOTHESIS

Before analyzing each persona, commit to a kill barrier hypothesis:

> "The single barrier most likely to block adoption regardless of quality is: ___"

You will confirm or revise this hypothesis after the per-persona analysis.

---

STEP 3: PER-PERSONA INERTIA TABLE

For each persona, complete the table below. The Kill Barrier Confirmation column is
required -- a blank cell is a structural gap visible at fill time.

| Persona | Workaround + Satisfaction | Switching Cost (with estimate) | Habit Lock-In Mechanism | Social Proof Threshold | Inertia Reduction Condition | Kill Barrier: CONFIRM / PARTIAL / DISCONFIRM | Inertia Score + Rationale |
|---------|--------------------------|-------------------------------|------------------------|----------------------|-----------------------------|----------------------------------------------|--------------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Fill rules:
- Workaround satisfaction: use vocabulary ("good enough" / "painful but familiar" /
  "actively seeking replacement") -- do not proxy with relationship level or adoption stage
- Switching cost: give a concrete estimate (time, training, disruption) -- not just HIGH/LOW
- Inertia score: write one sentence of rationale -- bare HIGH/MED/LOW does not qualify
- Kill barrier confirmation: CONFIRM / PARTIAL / DISCONFIRM for every persona -- no blanks

---

KILL BARRIER CONSOLIDATION SCAN -- verify all enforcement requirements before writing verdict:
- [ ] Every persona has an explicit workaround satisfaction using satisfaction vocabulary,
  not relationship level or adoption stage as a proxy
- [ ] Every inertia score carries a one-sentence rationale -- no bare HIGH / MED / LOW
- [ ] The kill barrier hypothesis has been confirmed, partially confirmed, or disconfirmed
  for at least one persona with explicit per-persona evidence from the table
- [ ] Each AMEND option in Step 4 will require (a) a named persona and (b) a specific
  gap from the Step 3 table, enforced at the Step 4 check

---

STEP 4: OVERALL ADOPTION INERTIA RISK + AMEND

Label the synthesis section "Overall Adoption Inertia Risk." State:
1. Overall inertia risk level (HIGH / MED / LOW)
2. Kill barrier conclusion -- name the single barrier most likely to kill adoption,
   supported by per-persona confirmation evidence from the Step 3 table
3. The highest-inertia persona and the primary inertia driver

STEP 4 CHECK: Before writing AMEND options, verify that each option names (a) a specific
persona AND (b) a specific gap from Step 3. Write options only after verification.

- AMEND A: [Persona] / [gap]
- AMEND B: [Persona] / [gap]
- AMEND C: [Persona] / [gap]
```

---

## V-02 (R6): Competitor-First with Explicit Architecture Scope -- C-24 Single-Axis

**Axis:** Output format (explicit architecture scope note embedded in the evidence gate).
Single-axis target: C-24. Base: V-01 R5 -- three-layer architecture, competitor-first
framing, "KILL BARRIER EVIDENCE GATE" (already passes C-23 as a role label, C-22 as
architecture-agnostic min-patch). V-01 R5 fails C-24 because it does not explicitly declare
the minimum-patch scope in the design's own checkpoint language. Change: add an ARCHITECTURE
SCOPE block inside the evidence gate stating that block-to-table is the complete local repair
without gate restructuring.

**Hypothesis:** Adding a single architecture-agnostic scope declaration to the C-18-carrying
evidence gate achieves C-24 PASS in a three-layer (C-20 path) design. C-22 confirms the rule
is applied correctly by the evaluator; C-24 asks whether the design makes the rule legible
within its own checkpoint language without requiring external inference.

```
You are running /validate-inertia.

This feature has a competitor that will not appear in any roadmap review: it is whatever
users do today. The status-quo competitor does not need to ship, does not need funding,
and does not need a team. It is already deployed. Your job is to assess whether this
feature can displace it.

---

PRE-FLIGHT CHECK

Before proceeding, confirm:
- [ ] At least 2 distinct user personas are identified
- [ ] Workaround satisfaction will be assessed using vocabulary: "good enough" /
  "painful but familiar" / "actively seeking replacement" -- do not proxy satisfaction
  by relationship level (Heavy/Occasional/Rare) or adoption stage alone
- [ ] No dimension will be left blank or labeled "unknown" without specifying the
  exact information needed and why it matters for the inertia verdict

---

STEP 1: COMPETITOR AUDIT

For each persona, audit the current workaround as if it were a competing product:

- What is the persona doing today instead of using this feature?
- How satisfied are they with it? (use satisfaction vocabulary above)
- What makes the workaround sticky -- habit, team dependency, tool integration, sunk
  cost in existing workflows?
- Switching cost estimate: what would adopting this feature actually cost this persona
  in time, training, or workflow disruption? Give a concrete estimate, not just HIGH/LOW.
- Social proof threshold: early adopter / wait-and-see / mandate-required
- Habit lock-in: what specific muscle memory, tool, or process makes the current
  behavior self-reinforcing?
- Inertia reduction condition: what would have to change in this persona's environment,
  team, or incentives for inertia to lose?

---

STEP 2: KILL BARRIER HYPOTHESIS

Before filling the per-persona table, state one hypothesis:

> "The single barrier most likely to block adoption regardless of feature quality is: ___"

Commit to a hypothesis. You will test it persona by persona in Step 3 and confirm or
revise it in Step 4.

---

KILL BARRIER EVIDENCE GATE

[ ] Kill barrier hypothesis is stated above
[ ] Each persona in Step 3 includes a Kill Barrier Confirmation column with value
    CONFIRM / PARTIAL / DISCONFIRM -- no blank cells
[ ] NOTE: Each AMEND option in the AMEND DIRECTIVE will require (a) a named persona
    and (b) a specific gap from the Step 3 table, enforced at Gate 4

ARCHITECTURE SCOPE: This gate carries the C-18 forward reference and requires no
modification when structural gaps elsewhere are repaired. If the per-persona section
(Step 3) were the only gap -- blocks instead of a structured table -- converting to table
is the complete local repair. This gate and Gate 4 are preserved verbatim. No gate
restructuring is required.

---

STEP 3: PER-PERSONA INERTIA TABLE

Complete all columns for each persona. A blank cell is a gap introduced mid-fill --
the table structure makes omissions visible. Fill every cell.

| Dimension | [Persona A] | [Persona B] | [Persona C] |
|-----------|-------------|-------------|-------------|
| Current workaround | | | |
| Workaround satisfaction | | | |
| Switching cost (concrete estimate) | | | |
| Habit lock-in mechanism | | | |
| Social proof threshold | | | |
| Inertia reduction condition | | | |
| Kill barrier: CONFIRM / PARTIAL / DISCONFIRM | | | |
| Inertia score (HIGH / MED / LOW + rationale) | | | |

---

STEP 4: OVERALL ADOPTION INERTIA RISK

Label this section "Overall Adoption Inertia Risk." Synthesize the Step 3 table. State:
1. Overall inertia risk level (HIGH / MED / LOW)
2. Kill barrier conclusion -- confirm or revise the Step 2 hypothesis based on
   per-persona confirmation evidence from the table
3. The highest-inertia persona and the primary inertia driver

---

GATE 4 -- AMEND DIRECTIVE

Before writing AMEND options, verify: does each option name (a) a specific persona AND
(b) a specific gap from the Step 3 table? Generic scope expansions do not qualify.

Offer 2-3 AMEND options:
- AMEND A: [Persona] / [specific gap]
- AMEND B: [Persona] / [specific gap]
- AMEND C: [Persona] / [specific gap]
```

---

## V-03 (R6): Phase/Gate Canonical with Structural Ceiling Note -- C-25 Single-Axis

**Axis:** Lifecycle emphasis (explicit Phase/Gate structure with named boundaries). Single-axis
target: C-25. Base: V-03 R5 -- canonical Phase/Gate design, passes C-16 and C-23. Fails C-25
(no mutual exclusion acknowledgment). Change: add a DESIGN NOTE at the opening explicitly
stating that C-16 PASS and C-20 PASS are mutually exclusive and that 16/17 is the structural
ceiling for either path.

**Hypothesis:** A Phase/Gate (C-16-path) design that explicitly acknowledges the C-16/C-20
mutual exclusion in its own framing achieves C-25 PASS. Open question: C-25 Pass condition
says "a design targeting multi-layer distribution (C-20 candidate)" -- does C-25 require a
C-20 architecture, or does any design making the acknowledgment pass? If C-25 requires C-20
path, this variation stays at 13/17. If any explicit acknowledgment qualifies, V-03 reaches
14/17. Either outcome resolves a genuine rubric ambiguity.

```
You are running /validate-inertia for: {{feature}}

Stress-test the adoption case. Map per-persona inertia and identify the kill barrier --
the one thing that would prevent adoption even if the feature is perfect.

DESIGN NOTE -- STRUCTURAL CEILING: This skill uses a single consolidating gate (C-16
path). The alternative architecture distributes enforcement across multiple layers without
a consolidating gate (C-20 path). These two paths are mutually exclusive by construction:
a design cannot simultaneously consolidate all aspirational enforcement under one gate
and distribute it across layers without that gate. The structural ceiling for either path
is 16/17 aspirational criteria. C-16 PASS and C-20 PASS cannot both contribute to the
same design's score. 17/17 is unreachable.

---

PHASE 1: SETUP + KILL BARRIER HYPOTHESIS

1. Name the feature and the 2-4 primary user personas.
2. For the highest-inertia persona, identify the current workaround and assess
   workaround satisfaction using vocabulary: "good enough" / "painful but familiar" /
   "actively seeking replacement."
3. State the kill barrier hypothesis:
   > "The single barrier most likely to block adoption regardless of quality is: ___"

---

GATE 1: EVIDENCE COMPLETENESS

Before Phase 2, confirm:
- [ ] At least 2 distinct personas identified
- [ ] Workaround identified for the highest-inertia persona
- [ ] Workaround satisfaction uses required vocabulary (not bare relationship level)
- [ ] Kill barrier hypothesis is stated and will be tested per-persona in Phase 2
- [ ] Social proof threshold and habit lock-in mechanism will be assessed per-persona

---

PHASE 2: PER-PERSONA INERTIA TABLE

Complete the table for all personas. The Kill Barrier Confirmation column is required --
a blank cell is a visible gap at fill time.

| Persona | Workaround + Satisfaction | Switching Cost (estimate) | Habit Lock-In | Social Proof Threshold | Inertia Reduction Condition | Kill Barrier: CONFIRM / PARTIAL / DISCONFIRM | Inertia Score + Rationale |
|---------|--------------------------|--------------------------|---------------|----------------------|----------------------------|----------------------------------------------|--------------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

---

GATE 2: ASPIRATIONAL ENFORCEMENT

Before Phase 3, verify:
- [ ] Every persona has an explicit workaround satisfaction using vocabulary, not
  relationship level or adoption stage as a proxy
- [ ] Every inertia score has a one-sentence rationale -- no bare HIGH / MED / LOW
- [ ] Every kill barrier confirmation is CONFIRM / PARTIAL / DISCONFIRM -- no blank cells
- [ ] Each AMEND option in Gate 4 will require (a) a named persona and (b) a specific
  gap from the Phase 2 table, enforced at Gate 4

---

PHASE 3: OVERALL ADOPTION INERTIA RISK

Label this section "Overall Adoption Inertia Risk." Synthesize the Phase 2 table. State:
1. Overall inertia risk level (HIGH / MED / LOW)
2. Kill barrier conclusion -- confirm or revise the Phase 1 hypothesis, supported by
   per-persona confirmation evidence from the Phase 2 table
3. The highest-inertia persona and the primary inertia driver

---

GATE 4: AMEND DIRECTIVE

Each AMEND option must name (a) a specific persona AND (b) a specific gap from the
Phase 2 table. Verify before writing.

- AMEND A: [Persona] / [gap]
- AMEND B: [Persona] / [gap]
- AMEND C: [Persona] / [gap]
```

---

## V-04 (R6): Data-Before-Hypothesis Sequence -- C-23 + C-24 Combined

**Axis:** Role sequence (data-before-hypothesis). All R5 designs commit to the kill barrier
hypothesis before the per-persona table. V-04 inverts this: the competitor audit runs first
across all personas, and the kill barrier hypothesis is formed from evidence rather than
speculatively. Combined target: C-23 (named "KILL BARRIER ENFORCEMENT SCAN") + C-24
(explicit SCOPE NOTE in the scan body declaring the minimum-patch rule in the design's own
checkpoint language).

**Hypothesis:** A scan-based (C-21 path) design with data-before-hypothesis sequencing passes
C-23 (role-communicating label on the scan) and C-24 (architecture-agnostic scope declaration
in the scan body) simultaneously. The enforcement structure is mechanically identical to V-02
R5 and V-05 R5; the distinguishing properties are naming, scope declaration, and the inversion
of when the kill barrier hypothesis is committed.

```
You are running /validate-inertia for: {{feature}}

Map adoption inertia per persona. Sequence: audit the status-quo competitor first per
persona, then form the kill barrier hypothesis from evidence. A hypothesis grounded in
per-persona data is more defensible than a speculative commit made before analysis.

---

STEP 1: COMPETITOR AUDIT

For each identified persona, audit the current workaround as if it were a competing
product:

- Current workaround: what are they doing today instead of using this feature?
- Workaround satisfaction: "good enough" / "painful but familiar" / "actively seeking
  replacement" (required vocabulary -- do not proxy with relationship level or adoption stage)
- Switching cost estimate: concrete value in time, training, or workflow disruption --
  not just HIGH/LOW
- Habit lock-in: the specific muscle memory, tool, or team dependency that makes the
  current behavior self-reinforcing
- Social proof threshold: early adopter / wait-and-see / mandate-required

---

STEP 2: KILL BARRIER HYPOTHESIS

After auditing the workarounds, commit to a kill barrier hypothesis:

> "Based on the above audit, the single barrier most likely to block adoption regardless
> of feature quality is: ___"

This hypothesis is evidence-grounded, not speculative. It will be tested per-persona in
Step 3 and confirmed or revised in Step 4.

---

STEP 3: PER-PERSONA INERTIA TABLE

Complete all columns. The Kill Barrier Confirmation column is required -- a blank cell
is a visible structural gap at fill time. Fill every cell with a substantive value.

| Persona | Workaround + Satisfaction | Switching Cost (estimate) | Habit Lock-In | Social Proof Threshold | Inertia Reduction Condition | Kill Barrier: CONFIRM / PARTIAL / DISCONFIRM | Inertia Score + Rationale |
|---------|--------------------------|--------------------------|---------------|----------------------|----------------------------|----------------------------------------------|--------------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Fill rules:
- Satisfaction vocabulary required: "good enough" / "painful but familiar" /
  "actively seeking replacement" -- relationship level or adoption stage is not a proxy
- Switching cost: concrete estimate -- bare HIGH/LOW does not qualify
- Kill barrier confirmation: CONFIRM / PARTIAL / DISCONFIRM -- no blank cells
- Inertia score: HIGH / MED / LOW with one sentence of rationale -- bare label insufficient

---

KILL BARRIER ENFORCEMENT SCAN -- aspirational consolidation checkpoint before verdict

Before writing the verdict, verify all of the following:
- [ ] Every persona has an explicit workaround satisfaction using satisfaction vocabulary,
  not relationship level or adoption stage as a proxy
- [ ] Every inertia score carries a one-sentence rationale -- no bare HIGH / MED / LOW
- [ ] The kill barrier hypothesis has been confirmed, partially confirmed, or disconfirmed
  for at least one persona with explicit per-persona evidence from the Step 3 table
- [ ] Each AMEND option in Step 4 will require (a) a named persona and (b) a specific
  gap from the Step 3 table, enforced at the Step 4 check

SCOPE NOTE: This scan carries the C-18 forward reference to Step 4's AMEND enforcement
rule and requires no modification when other structural repairs are made. If Step 3
per-persona output were the only structural gap -- blocks instead of the structured table
-- converting to table is the complete local repair. This scan is preserved verbatim.
No structural changes beyond Step 3 output format are required.

---

STEP 4: OVERALL ADOPTION INERTIA RISK + AMEND

Label the synthesis section "Overall Adoption Inertia Risk." State:
1. Overall inertia risk level (HIGH / MED / LOW)
2. Kill barrier conclusion -- confirm or revise the Step 2 hypothesis, supported by
   per-persona confirmation evidence from the Step 3 table
3. The highest-inertia persona and the primary inertia driver

STEP 4 CHECK: Each AMEND option must name (a) a specific persona AND (b) a specific
gap from the Step 3 table. Verify before writing.

- AMEND A: [Persona] / [gap]
- AMEND B: [Persona] / [gap]
- AMEND C: [Persona] / [gap]
```

---

## V-05 (R6): Status-Quo-as-Rival -- C-23 + C-24 + C-25 Combined (Ceiling Design)

**Axis:** Inertia framing (the status quo is characterized as "the incumbent" throughout --
it has 100% adoption by default, requires no budget, and wins by inertia if the feature fails
to displace it). Combined target: C-23 (ENFORCEMENT BRIDGE, already present in V-05 R5) +
C-24 (SCOPE NOTE added to ENFORCEMENT BRIDGE) + C-25 (DESIGN NOTE on mutual exclusion added
to framing). Base: V-05 R5 with two additions; all mechanism depth preserved verbatim.

**Hypothesis:** V-05 R5 already passes C-23. Adding a SCOPE NOTE to the ENFORCEMENT BRIDGE
achieves C-24 PASS (the scan explicitly declares min-patch rule in its own checkpoint
language). Adding a DESIGN NOTE on C-16/C-20 mutual exclusion achieves C-25 PASS. Together
these reach 16/17 -- the structural ceiling for v6. 17/17 is unreachable by construction.

```
You are running /validate-inertia for: {{feature}}

Stress-test the adoption case. The question is: why would users not adopt this feature
even if it works perfectly? The status quo is the incumbent. It requires no deployment,
no budget approval, and no change management. It already has 100% adoption among current
users. Every persona who does not switch is a retention win for the incumbent. Map the
inertia per persona and name the kill barrier.

DESIGN NOTE -- STRUCTURAL CEILING: This skill uses the C-21 path -- a single scan-based
consolidation point (ENFORCEMENT BRIDGE) that simultaneously achieves C-16 gate
consolidation and C-18 forward reference via one announcement sentence. This path is
architecturally incompatible with C-20 multi-layer distribution. No design can
simultaneously consolidate all enforcement under one scan and distribute enforcement
across layers without a consolidation point. The structural ceiling is 16/17 aspirational
criteria for either path. C-16 PASS and C-20 PASS cannot both contribute to the same
design's score. 17/17 is unreachable.

---

PHASE 1: SITUATE THE INCUMBENT

Establish the status quo:
- What users are currently doing instead of this feature (name the incumbent behavior
  or tool)
- Which personas rely on the incumbent most and why
- Workaround satisfaction for the highest-inertia persona: "good enough" /
  "painful but familiar" / "actively seeking replacement"

---

PHASE 2: KILL BARRIER HYPOTHESIS

Before running the per-persona table, name the kill barrier:

> "The single barrier most likely to block adoption regardless of feature quality is: ___"

This hypothesis will be tested in the Phase 3 table and confirmed or revised in
the Phase 4 verdict.

---

PHASE 3: PER-PERSONA INERTIA TABLE

Complete the table for all personas. The Kill Barrier Confirmation column is required --
a blank cell is a structural gap visible at fill time.

| Persona | Workaround + Satisfaction | Switching Cost (estimate) | Habit Lock-In | Social Proof Threshold | Inertia Reduction Condition | Kill Barrier: CONFIRM / PARTIAL / DISCONFIRM | Inertia Score + Rationale |
|---------|--------------------------|--------------------------|---------------|----------------------|----------------------------|----------------------------------------------|--------------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Fill rules:
- Workaround satisfaction: vocabulary required ("good enough" / "painful but familiar" /
  "actively seeking replacement") -- relationship level or adoption stage is not a proxy
- Switching cost: concrete estimate (time, training, workflow disruption) -- not just HIGH/LOW
- Inertia score: one sentence of rationale required -- bare HIGH/MED/LOW does not qualify
- Kill barrier confirmation: CONFIRM / PARTIAL / DISCONFIRM -- no blank cells

---

ENFORCEMENT BRIDGE (scan before Phase 4)

Before writing the verdict, verify:
- [ ] Every persona has an explicit workaround satisfaction using satisfaction vocabulary,
  not relationship level or adoption stage as a proxy
- [ ] Every inertia score carries a one-sentence rationale -- no bare labels
- [ ] The kill barrier has been confirmed, partially confirmed, or disconfirmed for at
  least one persona with explicit table evidence
- [ ] Each AMEND option in Phase 4 will require (a) a named persona and (b) a specific
  gap from the Phase 3 table, enforced at the Phase 4 check

SCOPE NOTE: This bridge carries the C-18 forward reference to Phase 4's AMEND enforcement
rule and requires no modification when structural gaps elsewhere are repaired. If Phase 3
per-persona output were the only gap -- blocks instead of a structured table -- converting
to table is the complete local repair. This bridge is preserved verbatim. No structural
changes beyond Phase 3 output format are required.

---

PHASE 4: OVERALL ADOPTION INERTIA RISK + AMEND

Label the synthesis "Overall Adoption Inertia Risk." State:
1. Overall inertia risk level (HIGH / MED / LOW)
2. Kill barrier conclusion -- confirm or revise the Phase 2 hypothesis, supported by
   per-persona confirmation evidence from the Phase 3 table
3. The highest-inertia persona and the primary driver

PHASE 4 CHECK: Each AMEND option must name (a) a specific persona AND (b) a specific
gap from the Phase 3 table. Verify before writing.

- AMEND A: [Persona] / [gap]
- AMEND B: [Persona] / [gap]
- AMEND C: [Persona] / [gap]
```

---

### Aspirational coverage by variation (v6 rubric, 17 criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Inertia reduction conditions | PASS | PASS | PASS | PASS | PASS |
| C-10 AMEND persona-specific + actionable | PASS | PASS | PASS | PASS | PASS |
| C-11 Kill barrier grounded in per-persona evidence | PASS | PASS | PASS | PASS | PASS |
| C-12 Workaround satisfaction per-persona (vocab) | PASS | PASS | PASS | PASS | PASS |
| C-13 No required field blank or bare label | PASS | PASS | PASS | PASS | PASS |
| C-14 Each AMEND names persona AND gap | PASS | PASS | PASS | PASS | PASS |
| C-15 Kill barrier as table column | PASS | PASS | PASS | PASS | PASS |
| C-16 Single gate bundles C-11..C-14 | PASS | PARTIAL | PASS | PASS | PASS |
| C-17 Enforcement through mechanism not labels | PASS | PASS | PASS | PASS | PASS |
| C-18 Gate includes forward reference | PASS | PASS | PASS | PASS | PASS |
| C-19 Structural + procedural co-occur | PASS | PASS | PASS | PASS | PASS |
| C-20 Distributed achieves C-19 without C-16 | FAIL | PASS | FAIL | FAIL | FAIL |
| C-21 One-sentence scan closes C-16+C-18 | PASS | FAIL | FAIL | PASS | PASS |
| C-22 Block-to-table minimum sufficient repair | PASS | PASS | PASS | PASS | PASS |
| C-23 Named consolidation checkpoint | PASS | PASS | PASS | PASS | PASS |
| C-24 Architecture-agnostic min-patch declaration | FAIL | PASS | FAIL | PASS | PASS |
| C-25 Mutual exclusion acknowledged | FAIL | FAIL | PASS? | FAIL | PASS |
| **Pass count** | **14/17** | **14/17** | **13 or 14/17** | **15/17** | **16/17** |

Notes:
- C-16 PARTIAL in V-02 = FAIL for scoring (three-layer, no single consolidation point)
- C-25 for V-03: open question -- Pass condition says "a design targeting multi-layer
  distribution (C-20 candidate)"; V-03 is C-16 path with explicit acknowledgment; if C-25
  requires C-20 architecture V-03 stays 13/17; if any acknowledgment qualifies V-03 = 14/17
- V-05 targets 16/17 (ceiling); 17/17 unreachable (C-16 and C-20 mutually exclusive)

### Predicted composite scores (v6 rubric)

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-05 Rival incumbent (C-23+C-24+C-25) | 60 | 30 | 9.41 | **99.41** |
| V-04 Data-before-hypothesis (C-23+C-24) | 60 | 30 | 8.82 | **98.82** |
| V-01 Conversational scan (C-23) | 60 | 30 | 8.24 | **98.24** |
| V-02 Competitor-first + scope note (C-24) | 60 | 30 | 8.24 | **98.24** |
| V-03 Phase/Gate + ceiling note (C-25) | 60 | 30 | 7.65 or 8.24 | **97.65 or 98.24** |

**R6 ceiling: 99.41** (V-05). This is the hard structural ceiling for the v6 rubric:
- C-16 PASS and C-20 PASS are mutually exclusive (C-25)
- Maximum achievable aspirational: 16/17 = 9.41 points
- Top composite: 60 + 30 + 9.41 = 99.41

Open questions scoring will resolve:
1. Does C-25 Pass require a C-20-path design, or does any explicit acknowledgment qualify?
   If C-25 requires C-20 path: V-03 = 13/17 -> 97.65; if any acknowledgment qualifies:
   V-03 = 14/17 -> 98.24.
2. Does V-04's SCOPE NOTE in the scan body satisfy C-24? C-24 requires declaration "in or
   adjacent to that checkpoint's enforcement language" -- the SCOPE NOTE is inside the scan
   block, which should qualify.
3. Does the DESIGN NOTE framing of C-25 in V-05 satisfy the Pass condition given V-05 is a
   C-21 path (C-16 PASS) design, not a C-20 candidate?
