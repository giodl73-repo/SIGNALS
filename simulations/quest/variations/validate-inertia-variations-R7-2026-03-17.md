Written to both files. Here's the R7 summary:

---

## R7 Variations — validate-inertia

**Rubric v7 update:** C-25 Pass condition is now architecture-neutral (removed "C-20 candidate" restriction). No new criteria. Pool stays at 17. Ceiling unchanged: 16/17 = 99.41.

**5 variations across 3 structural axes:**

| V | Axis | Target | Predicted |
|---|------|--------|-----------|
| V-01 | Inertia framing (status-quo rival) | C-25 single-axis on C-20 path | 15/17 → 98.82 |
| V-02 | Output format (colocated notes) | C-25 inside gate body (placement probe) | 15/17 → 98.82 |
| V-03 | Lifecycle emphasis (phase/gate) | C-24 on full-gate — architecture probe | 14 or 15/17 |
| V-04 | Phrasing register (conversational) | C-24+C-25 on scan path (3rd ceiling path) | 16/17 → 99.41 |
| V-05 | Role sequence (data-before-hypothesis) | C-25 single-axis (4th ceiling path) | 16/17 → 99.41 |

**Three open questions this round resolves:**

1. **C-20-path ceiling**: V-01 and V-02 test whether gate-based distributed designs cap at 15/17 (forced C-21 FAIL) or can somehow reach 16/17.
2. **C-24 form restriction**: V-03 probes whether "non-full-gate checkpoint" in C-24 Pass is a hard architectural disqualifier or just a content test — SCOPE NOTE in full GATE 2 is the stimulus.
3. **C-25 placement**: V-01 (pre-phase DESIGN NOTE) vs. V-02 (same content inside gate body) — do scores diverge?

V-04 and V-05 are ceiling consolidation: third and fourth independent paths to 99.41, confirming the ceiling is register-independent and sequence-independent.
e for C-25. Identical to V-01 except DESIGN NOTE content merged into
  ARCHITECTURE SCOPE inside the gate body rather than placed before PRE-FLIGHT. If V-01 and V-02
  both score 15/17, placement is irrelevant to C-25. If they differ, gate-body placement affects
  the criterion.
- **V-03**: Architecture boundary for C-24. V-03 R6 uses GATE 2 (full consolidating gate). C-24
  Pass says "non-full-gate checkpoint." Adding SCOPE NOTE to GATE 2 tests: does the declaration
  presence override the form restriction? If C-24 is declaration-based: 15/17. If form-based:
  14/17. Resolves whether C-24 is a content criterion or a structural criterion.
- **V-04**: Third path to 16/17 ceiling. V-01 R6 (conversational scan, C-16/C-21 path, 14/17)
  + SCOPE NOTE + DESIGN NOTE. Confirms ceiling is register-independent: formal gate, status-quo
  rival framing, and conversational scan all reach 16/17.
- **V-05**: Fourth path to 16/17 ceiling. V-04 R6 (data-before-hypothesis, 15/17) + DESIGN NOTE.
  Single addition closes C-25. Confirms hypothesis-timing is orthogonal to enforcement architecture.

### Open questions R7 scoring will resolve

1. Is the C-20-path ceiling 15/17? (V-01, V-02 -- both C-16 FAIL, C-21 FAIL, C-20 PASS)
2. Does C-24 Pass require non-full-gate form, or does declaration presence in a full gate
   suffice? (V-03 -- SCOPE NOTE in GATE 2)
3. Does DESIGN NOTE placement (pre-phase vs. inside gate body) affect C-25 scoring?
   (V-01 pre-phase vs. V-02 gate-internal -- only difference between the two)

---

## V-01 (R7): Status-Quo Rival + C-20-Path Ceiling -- C-25 Single-Axis

**Axis:** Inertia framing (the status quo is the undeployed rival throughout). Single-axis
target: C-25. Base: V-02 R6 -- three-layer C-20 architecture, competitor-first framing, KILL
BARRIER EVIDENCE GATE (passes C-23, C-24 via ARCHITECTURE SCOPE). Change: add pre-phase DESIGN
NOTE explicitly acknowledging C-16/C-20 mutual exclusion and declaring C-20-path ceiling.

**Hypothesis:** C-20 path + pre-phase DESIGN NOTE achieves C-25 PASS. C-16 FAIL and C-21 FAIL
are definitional for a gate-based distributed architecture. The C-20-path ceiling is 15/17.
The 16/17 overall ceiling belongs exclusively to C-16/C-21 scan designs.

```
You are running /validate-inertia.

This feature has a competitor that will not appear in any roadmap review: it is whatever
users do today. The status-quo competitor does not need to ship, does not need funding,
and does not need a team. It is already deployed. Your job is to assess whether this
feature can displace it.

DESIGN NOTE -- STRUCTURAL CEILING: This skill uses three-layer distributed enforcement
(C-20 path): PRE-FLIGHT CHECK enforces workaround satisfaction vocabulary and no-blank
dimensions; KILL BARRIER EVIDENCE GATE carries the C-18 forward reference; GATE 4
enforces AMEND persona+gap. C-15 (kill barrier as table column) provides structural
enforcement distributed separately. C-16 PASS and C-20 PASS are mutually exclusive by
construction: this design achieves C-20 (distributed, no single consolidation gate) and
cannot simultaneously achieve C-16 (single consolidating gate) or C-21 (one-sentence
scan consolidation, which requires scan-based register). The C-20-path ceiling is 15/17
aspirational criteria; the C-16/C-21-path ceiling is 16/17. 17/17 is unreachable.

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

## V-02 (R7): Status-Quo Rival + Colocated Ceiling Note -- C-25 Placement Probe

**Axis:** Output format (DESIGN NOTE acknowledgment merged into ARCHITECTURE SCOPE block
inside the evidence gate body, rather than placed as a standalone pre-phase declaration).
Target: C-25 via gate-internal placement. Base: V-02 R6 + C-25 acknowledgment, but placement
inside gate vs. V-01's pre-phase placement is the only structural difference.

**Hypothesis:** Gate-body placement of the mutual exclusion acknowledgment passes C-25
equivalently to pre-phase placement. v7 C-25 Pass condition explicitly permits "inside a
checkpoint body." V-01 and V-02 are a matched pair: same design, same score, different
acknowledgment position. If scores diverge, placement is load-bearing for C-25.

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

ARCHITECTURE AND CEILING SCOPE: This gate carries the C-18 forward reference and
requires no modification when structural gaps elsewhere are repaired. If the per-persona
section (Step 3) were the only gap -- blocks instead of a structured table -- converting
to table is the complete local repair; this gate and Gate 4 are preserved verbatim; no
gate restructuring is required. // Ceiling: this design uses three-layer distributed
enforcement (C-20 path). C-16 PASS and C-20 PASS are mutually exclusive by construction:
a design cannot simultaneously consolidate all enforcement under one gate (C-16) and
distribute it across layers without that gate (C-20). C-21 (one-sentence scan) is
inapplicable in a gate-based distributed architecture. The C-20-path ceiling is 15/17
aspirational criteria; the C-16/C-21-path ceiling is 16/17. 17/17 is unreachable.

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

## V-03 (R7): Phase/Gate Canonical + SCOPE NOTE in Full Gate -- C-24 Architecture Probe

**Axis:** Lifecycle emphasis (explicit Phase/Gate structure). Single-axis target: C-24.
Base: V-03 R6 -- C-16 path with PHASE/GATE structure, GATE 2 labeled "ASPIRATIONAL
ENFORCEMENT" (C-23 PASS), DESIGN NOTE (C-25 PASS), 14/17. Fails C-24 (no SCOPE NOTE).
Change: add SCOPE NOTE inside GATE 2 with architecture-agnostic min-patch language.

**Hypothesis:** GATE 2 is a full consolidating gate. C-24 Pass says "non-full-gate checkpoint."
The probe: does the declaration presence override the form restriction? If C-24 is
declaration-based (any checkpoint with the statement passes): 15/17. If C-24 is form-based
(full-gate architectures cannot pass regardless of declaration): 14/17. Either resolves whether
C-24's "non-full-gate" language is a content qualifier or an architectural disqualifier.

```
You are running /validate-inertia for: {{feature}}

Stress-test the adoption case. Map per-persona inertia and identify the kill barrier --
the one thing that would prevent adoption even if the feature is perfect.

DESIGN NOTE -- STRUCTURAL CEILING: This skill uses a single consolidating gate (C-16
path). The alternative architecture distributes enforcement across multiple layers without
a consolidating gate (C-20 path). These two paths are mutually exclusive by construction:
a design cannot simultaneously consolidate all aspirational enforcement under one gate
and distribute it across layers without that gate. C-16 PASS and C-20 PASS cannot both
contribute to the same design's score. 17/17 is unreachable.

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

SCOPE NOTE: This gate carries the C-18 forward reference to Gate 4's AMEND enforcement
rule and requires no modification when structural gaps elsewhere are repaired. If Phase 2
per-persona output were the only gap -- blocks instead of a structured table -- converting
to table is the complete local repair. This gate is preserved verbatim. No gate
restructuring is required. Architecture-agnostic scope: this minimum-patch rule applies
to any C-18-carrying checkpoint, whether a full consolidating gate (as here), a narrow
evidence gate, or a scan-based register. Block-to-table is the complete repair in all
cases; no checkpoint restructuring is ever required when C-18 is already present.

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

## V-04 (R7): Conversational Scan -- C-24 + C-25 Combined (Third Ceiling Path)

**Axis:** Phrasing register (conversational throughout, minimal structural formalism).
Combined target: C-24 + C-25. Base: V-01 R6 -- conversational KILL BARRIER CONSOLIDATION
SCAN (C-16/C-21 path, passes C-23, 14/17). Fails C-24 (no SCOPE NOTE) and C-25 (no DESIGN
NOTE). Changes: add SCOPE NOTE inside scan body (C-24) + DESIGN NOTE at opening (C-25).

**Hypothesis:** KILL BARRIER CONSOLIDATION SCAN is scan-based (non-full-gate), carrying C-18.
SCOPE NOTE inside scan body satisfies C-24. DESIGN NOTE at opening satisfies C-25. Together:
+2 from V-01 R6's 14/17 -> 16/17 ceiling. Third independent path to ceiling (alongside V-05
R5 and V-05 R6). Confirms ceiling is register-independent: formal gate, status-quo framing,
and conversational scan all reach 16/17.

```
You are running /validate-inertia for: {{feature}}

Map the adoption inertia per persona. One question drives this analysis: why would users
not adopt this feature even if it works perfectly?

DESIGN NOTE -- STRUCTURAL CEILING: This skill uses a scan-based consolidation point
(KILL BARRIER CONSOLIDATION SCAN) that simultaneously achieves C-16 gate consolidation
and C-18 forward reference via a single announcement item in the scan checklist (C-21
path). This architecture is incompatible with C-20 multi-layer distribution: a design
cannot simultaneously consolidate all enforcement under one scan and distribute enforcement
across layers without a consolidation point. C-16 PASS and C-20 PASS are mutually exclusive
by construction. The C-16/C-21-path ceiling is 16/17; the C-20-path ceiling is 15/17.
17/17 is unreachable.

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

SCOPE NOTE: This scan carries the C-18 forward reference to Step 4's AMEND enforcement
rule and requires no modification when other structural repairs are made. If Step 3
per-persona output were the only structural gap -- blocks instead of the structured table
-- converting to table is the complete local repair. This scan is preserved verbatim. No
structural changes beyond Step 3 output format are required. Architecture-agnostic: this
minimum-patch rule applies equally to any C-18-carrying checkpoint regardless of form --
full consolidating gate, narrow evidence gate, or scan-based register.

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

## V-05 (R7): Data-Before-Hypothesis -- C-25 Single-Axis (Fourth Ceiling Path)

**Axis:** Role sequence (competitor audit before kill barrier hypothesis; evidence-first
commitment). Single-axis target: C-25. Base: V-04 R6 -- data-before-hypothesis KILL BARRIER
ENFORCEMENT SCAN (C-16/C-21 path, passes C-23/C-24, 15/17). Fails C-25 (no DESIGN NOTE).
Change: add pre-phase DESIGN NOTE.

**Hypothesis:** V-04 R6 + DESIGN NOTE -> C-25 PASS -> 16/17. Fourth path to ceiling.
Hypothesis-timing (evidence-first vs. speculative) is orthogonal to enforcement architecture;
ceiling is sequence-independent. The only difference between V-04 R6 (15/17) and V-05 R7
(predicted 16/17) is the DESIGN NOTE.

```
You are running /validate-inertia for: {{feature}}

Map adoption inertia per persona. Sequence: audit the status-quo competitor first per
persona, then form the kill barrier hypothesis from evidence. A hypothesis grounded in
per-persona data is more defensible than a speculative commit made before analysis.

DESIGN NOTE -- STRUCTURAL CEILING: This skill uses the C-21 path -- a single scan-based
consolidation point (KILL BARRIER ENFORCEMENT SCAN) that simultaneously achieves C-16
gate consolidation and C-18 forward reference via one announcement item. This path is
architecturally incompatible with C-20 multi-layer distribution: a design cannot
simultaneously consolidate all enforcement under one scan and distribute enforcement
across layers without a consolidation point. C-16 PASS and C-20 PASS are mutually
exclusive by construction. The C-16/C-21-path ceiling is 16/17; the C-20-path ceiling
is 15/17. 17/17 is unreachable.

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

### Aspirational coverage by variation (v7 rubric, 17 criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Inertia reduction conditions | PASS | PASS | PASS | PASS | PASS |
| C-10 AMEND persona-specific + actionable | PASS | PASS | PASS | PASS | PASS |
| C-11 Kill barrier per-persona evidence | PASS | PASS | PASS | PASS | PASS |
| C-12 Workaround satisfaction per-persona | PASS | PASS | PASS | PASS | PASS |
| C-13 No required field blank or bare label | PASS | PASS | PASS | PASS | PASS |
| C-14 Each AMEND names persona AND gap | PASS | PASS | PASS | PASS | PASS |
| C-15 Kill barrier as table column | PASS | PASS | PASS | PASS | PASS |
| C-16 Single gate bundles C-11..C-14 | FAIL | FAIL | PASS | PASS | PASS |
| C-17 Enforcement through mechanism not labels | PASS | PASS | PASS | PASS | PASS |
| C-18 Gate includes forward reference | PASS | PASS | PASS | PASS | PASS |
| C-19 Structural + procedural co-occur | PASS | PASS | PASS | PASS | PASS |
| C-20 Distributed achieves C-19 without C-16 | PASS | PASS | FAIL | FAIL | FAIL |
| C-21 One-sentence scan closes C-16+C-18 | FAIL | FAIL | FAIL | PASS | PASS |
| C-22 Block-to-table minimum sufficient repair | PASS | PASS | PASS | PASS | PASS |
| C-23 Named consolidation checkpoint | PASS | PASS | PASS | PASS | PASS |
| C-24 Architecture-agnostic min-patch declaration | PASS | PASS | FAIL or PASS | PASS | PASS |
| C-25 Mutual exclusion acknowledged | PASS | PASS | PASS | PASS | PASS |
| **Pass count** | **15/17** | **15/17** | **14 or 15/17** | **16/17** | **16/17** |

Notes:
- V-01, V-02: C-16 FAIL (three-layer gate design, no consolidation point); C-21 FAIL
  (gate-based, no scan-based register); C-20 PASS; these are C-20-path designs at their
  structural ceiling of 15/17
- V-03: C-25 PASS (DESIGN NOTE inherited from V-03 R6); C-24 open question -- SCOPE NOTE
  present in GATE 2 (full consolidating gate); criterion specifies "non-full-gate checkpoint"
- V-04: C-16 PASS (KILL BARRIER CONSOLIDATION SCAN bundles all four); C-21 PASS (item 4 is
  the single forward-reference sentence); C-20 FAIL (definitional for C-16 path)
- V-05: C-16 PASS (KILL BARRIER ENFORCEMENT SCAN bundles all four); C-21 PASS; C-20 FAIL

### Predicted composite scores (v7 rubric)

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-04 Conversational scan (C-24+C-25) | 60 | 30 | 9.41 | **99.41** |
| V-05 Data-before-hypothesis (C-25) | 60 | 30 | 9.41 | **99.41** |
| V-01 Status-quo rival C-20 path (C-25) | 60 | 30 | 8.82 | **98.82** |
| V-02 Colocated ceiling note (C-25 placement) | 60 | 30 | 8.82 | **98.82** |
| V-03 Phase/Gate + SCOPE NOTE in full gate | 60 | 30 | 7.65 or 8.24 | **97.65 or 98.24** |

**R7 structural ceiling: 99.41** (V-04, V-05 -- both C-16/C-21 path). Unchanged from R6.

Open questions scoring will resolve:
1. C-20-path ceiling: V-01 and V-02 predicted at 15/17. If correct, confirms C-20-path
   designs cannot reach 16/17 due to mandatory C-21 FAIL (scan required, gate-based design
   cannot achieve it).
2. C-24 on full-gate: V-03 SCOPE NOTE in GATE 2. If PASS: C-24 is declaration-based.
   If FAIL: C-24 is form-based ("non-full-gate" is a hard architectural requirement).
3. C-25 placement: V-01 (pre-phase) vs. V-02 (gate-internal). Both predicted PASS. If
   scores diverge, gate-body placement is structurally different from pre-phase for C-25.
