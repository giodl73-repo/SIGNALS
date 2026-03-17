Written to `simulations/quest/variations/validate-inertia-variations-R5-2026-03-17.md`.

---

## R5 Variation Summary

| V | Axis | C-16 | C-20 | C-21 | C-22 | Predicted |
|---|------|------|------|------|------|-----------|
| **V-01** | C-20 single-axis: three-layer distributed, competitor-first | PARTIAL | PASS | FAIL | PASS | 12/14 → 98.57 |
| **V-02** | C-21 single-axis: scan-forward-ref, conversational register | PASS | FAIL | PASS | PASS | 13/14 → 99.29 |
| **V-03** | C-22 single-axis: gate-2-canonical, lifecycle emphasis | PASS | FAIL | FAIL | PASS | 13/14 → 99.29 |
| **V-04** | C-20+C-22 combined: evidence gate as explicit Gate-2-equivalent | PARTIAL | PASS | FAIL | PASS | 12/14 → 98.57 |
| **V-05** | C-21+C-22 combined: scan as consolidation AND Gate-2-equivalent | PASS | FAIL | PASS | PASS | 13/14 → 99.29 |

---

**R5 ceiling: 99.29.** C-16 PASS (single consolidating gate) and C-20 PASS (distributed, no single consolidating gate) are mutually exclusive by definition. C-21 PASS requires C-16 PASS. Therefore C-20 and C-21 can never both pass — the 14th criterion is always either C-20 or C-21 depending on strategy.

**Key open questions scoring will resolve:**

1. Does C-22 apply to narrow evidence gates (V-01/V-04 where the gate carries C-18 but bundles only C-11, not C-12/C-13)? If not, V-01/V-04 drop to 11/14 → 97.86.
2. Is a scan a valid Gate-2-equivalent for C-22 (V-02/V-05)? If not, they drop to 12/14 → 98.57.
3. If the ceiling is structurally confirmed at 13/14, what does R6 look like — new criteria targeting the C-16/C-20 tension as a named design tradeoff?
sign explicitly architected for C-20 pass all 14 where applicable? Is the evidence gate in a three-layer design a valid Gate-2-equivalent for C-22?

2. **C-21 PASS as a named criterion** -- V-02/V-05: V-03 from R4 demonstrated C-21 before it was a criterion. Does a design explicitly targeting C-21 also pass C-22, and is a scan-based Gate-2-equivalent sufficient for C-22?

3. **C-22 single-axis isolation** -- V-03: Can C-22 be confirmed in isolation from C-20/C-21? Does the canonical gate-2 design (V-04 from R3/R4) pass C-22 as written, without any additional structural element?

4. **C-22 applicability to C-16 PARTIAL designs** -- V-01/V-04: C-22's source example (V-05(R3) repaired in R4) was a C-16 PASS design. Does C-22 also hold when the Gate-2-equivalent is a narrow evidence gate (C-11+C-18 only), not a full C-16 consolidating gate?

5. **R5 ceiling confirmation** -- Do V-02, V-03, V-05 all reach 13/14 → 99.29, confirming the ceiling? Do V-01/V-04 reach 12/14 → 98.57 as predicted?

---

### Design decision notes

**V-01 vs V-04 (both C-16 PARTIAL):** Both use a three-layer architecture (pre-flight for C-12/C-13, evidence gate for C-11+C-18, Gate 4 for C-14). V-01 uses competitor-first role sequence -- the workaround audit precedes the kill barrier hypothesis. V-04 uses hypothesis-first sequence with the evidence gate explicitly named as "Kill Barrier Gate 2" to invoke the C-22 minimum-patch rule directly. The structural difference is naming and framing, not architecture.

**V-02 vs V-05 (both C-21):** Both use a scan-based register with one-sentence forward reference. V-02 is purely conversational throughout; the table is the only formal structure. V-05 uses explicit step labels and lifecycle boundaries -- the scan is a named enforcement bridge between Phase 3 and Phase 4, making the Gate-2-equivalent role of the scan visible.

**C-22 in three-layer designs (V-01, V-04):** C-22 requires a "Gate-2-equivalent checkpoint carries C-18 (forward reference already present)." In V-01/V-04, the evidence gate carries C-18 (forward reference to Gate 4). If Phase 3 blocks were converted to a table, C-15 would repair without touching the evidence gate (C-18 stays verbatim), pre-flight (C-12/C-13 unchanged), or Gate 4 (C-14 unchanged). C-19 would auto-derive. This meets the C-22 Pass condition. The open question: does C-22 distinguish between a full C-16 consolidating gate and a narrow evidence gate?

---

## V-01 (R5): Three-Layer Distributed Architecture -- C-20 Single-Axis

**Axis:** Role sequence -- competitor-first. Three enforcement layers: pre-flight (C-12/C-13),
evidence gate (C-11 + C-18 forward reference), Gate 4 AMEND (C-14). C-15 in per-persona
table (structural layer). No single gate bundles all four aspirationals.

**Hypothesis:** A design explicitly architected for multi-layer distribution -- with C-15 in
the table, C-18 in the evidence gate, and C-12/C-13 isolated in a pre-flight -- achieves
C-20 PASS and C-19 PASS with C-16 PARTIAL. The evidence gate is a valid Gate-2-equivalent
for C-22. Competitor-first framing preserves the status-quo-as-rival voice while keeping
all enforcement mechanics structurally independent.

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
- AMEND A: [Persona] / [specific gap -- e.g., quantify switching cost / re-assess
  workaround satisfaction / confirm kill barrier]
- AMEND B: [Persona] / [specific gap]
- AMEND C: [Persona] / [specific gap]
```

---

## V-02 (R5): Scan-Forward-Ref -- C-21 Single-Axis

**Axis:** Phrasing register -- conversational throughout. Scan-based enforcement: a
pre-Step-4 scan covers C-11/C-12/C-13, and a single announcement sentence chains to
Step 4's AMEND rule. The scan becomes both the C-16 consolidation point and the C-18
forward reference via one sentence. Per-persona table with kill barrier column present
for C-15.

**Hypothesis:** A fully conversational design with a scan-based register and a
single announcement sentence explicitly targeting C-21 achieves C-16 PASS, C-18 PASS,
C-19 PASS, and C-21 PASS simultaneously. The scan is also the Gate-2-equivalent for
C-22 purposes: a design with scan(C-18) + table(C-15) has C-22 PASS because block-to-
table conversion would repair C-15 without modifying the scan.

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

PRE-STEP-4 SCAN -- before writing the verdict, verify:
- [ ] Every persona has an explicit workaround satisfaction using satisfaction vocabulary,
  not relationship level or adoption stage as a proxy
- [ ] Every inertia score has a one-sentence rationale -- no bare HIGH / MED / LOW
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

## V-03 (R5): Gate-2-Canonical -- C-22 Single-Axis

**Axis:** Lifecycle emphasis -- Phase/Gate structure throughout. This is the canonical
Gate-2 design from R3/R4 (V-04/V-05), now framing Gate 2 explicitly around the C-22
minimum-patch principle: Phase 2 is a table (C-15), Gate 2 carries C-18 (forward
reference to Gate 4), and the co-occurrence of C-15 + C-18 makes C-19 automatic.
The design is intentionally structured so that block-to-table in Phase 2 would be
the one and only repair if C-15 were the failing criterion.

**Hypothesis:** The canonical gate-2 design passes C-22 as written, without additional
structural elements. C-22 is a derived property: in a Gate-2-carrying design with a
Phase 2 table, block-to-table is demonstrably the minimum complete repair because Gate 2
verbatim already carries C-18 and C-19 derives from C-15+C-18 co-occurrence.

```
You are running /validate-inertia for: {{feature}}

Stress-test the adoption case. Map per-persona inertia and identify the kill barrier --
the one thing that would prevent adoption even if the feature is perfect.

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

## V-04 (R5): Three-Layer + Gate-2-Equivalent -- C-20 + C-22 Combined

**Axis:** Combination -- three-layer distribution (C-20) with evidence gate explicitly
labeled "Kill Barrier Gate 2" to invoke the C-22 minimum-patch principle directly.
Pre-flight holds C-12/C-13; Kill Barrier Gate 2 holds C-11 + C-18; Phase 3 table holds
C-15; Gate 4 holds C-14. No single gate bundles all four (C-16 PARTIAL). The Gate-2-
equivalent label makes the C-22 derivation traceable: if Phase 3 were blocks, the repair
would be local to Phase 3 output structure only.

**Hypothesis:** Explicitly naming the evidence gate as "Gate 2" makes C-22 legible in
a C-16 PARTIAL design -- the minimum-patch rule applies whenever a gate carries C-18,
regardless of whether that gate is also the C-16 consolidation point. C-20 and C-22
are independently achievable in the same design without gate consolidation.

```
You are running /validate-inertia for: {{feature}}

Stress-test the adoption case by mapping per-persona inertia. Identify the kill barrier:
the one thing that would block adoption even if the feature works perfectly.

---

PRE-FLIGHT CHECK

Before proceeding, confirm:
- [ ] At least 2 distinct user personas are identified
- [ ] Workaround satisfaction will use vocabulary: "good enough" / "painful but familiar" /
  "actively seeking replacement" -- do not use relationship level (Heavy/Occasional/Rare)
  or adoption stage as a proxy for satisfaction
- [ ] No required dimension will be left blank: if a value is genuinely unavailable, name
  the specific information needed and why it matters for the inertia verdict

---

STEP 1: FEATURE CONTEXT + KILL BARRIER HYPOTHESIS

Brief the analysis:
- Feature name and purpose in one sentence
- Persona set: name 2-4 distinct user personas
- Kill barrier hypothesis: "The single barrier most likely to block adoption regardless
  of feature quality is: ___"

The hypothesis will be confirmed, partially confirmed, or disconfirmed per-persona in
Step 2, then synthesized in Step 3.

---

STEP 2: PER-PERSONA INERTIA TABLE

Complete all columns. The Kill Barrier Confirmation column is required -- a blank cell
is a structural gap visible at fill time. Fill every cell with a substantive value.

| Persona | Workaround + Satisfaction | Switching Cost (concrete estimate) | Habit Lock-In | Social Proof Threshold | Inertia Reduction Condition | Kill Barrier: CONFIRM / PARTIAL / DISCONFIRM | Inertia Score + Rationale |
|---------|--------------------------|-----------------------------------|---------------|----------------------|----------------------------|----------------------------------------------|--------------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

---

KILL BARRIER GATE 2

[ ] Kill barrier hypothesis confirmed, partially confirmed, or disconfirmed for at least
    one persona via explicit table evidence
[ ] Each AMEND option in the AMEND DIRECTIVE will require (a) a named persona and (b) a
    specific gap from the Step 2 table, enforced at Gate 4

Note: Gate 2 carries the forward reference forward verbatim. If Step 2 per-persona output
were the only structural gap (blocks instead of table), converting to table is the
complete repair -- Gate 2 and Gate 4 do not change.

---

STEP 3: OVERALL ADOPTION INERTIA RISK

Label this section "Overall Adoption Inertia Risk." State:
1. Overall inertia risk level (HIGH / MED / LOW)
2. Kill barrier conclusion -- confirm or revise the Step 1 hypothesis based on
   per-persona evidence from the Step 2 table
3. The highest-inertia persona and the primary driver

---

GATE 4 -- AMEND DIRECTIVE

Each AMEND option must name (a) a specific persona AND (b) a specific gap from the
Step 2 table. Verify before writing.

- AMEND A: [Persona] / [gap]
- AMEND B: [Persona] / [gap]
- AMEND C: [Persona] / [gap]
```

---

## V-05 (R5): Scan-Table Hybrid -- C-21 + C-22 Combined

**Axis:** Combination -- scan-forward-ref (C-21) with a Phase 3 table (C-15) and the
scan serving dual roles: C-16 consolidation point AND Gate-2-equivalent for C-22. The
scan bundles C-11/C-12/C-13 and announces C-14 via the forward-reference sentence (C-21).
The table in Phase 3 provides C-15. The scan carries C-18 forward to Phase 4, making it
the Gate-2-equivalent: if Phase 3 were blocks, converting to table would be the only
repair needed (C-22). Explicit step labels make the scan's enforcement role legible.

**Hypothesis:** A design where the scan is explicitly named as the enforcement bridge
between Phase 3 and Phase 4 achieves C-21 PASS (one-sentence forward ref in scan-based
register) and C-22 PASS (scan as Gate-2-equivalent carrying C-18, table as minimum
structural element for C-15) simultaneously. C-16 PASS follows from the scan consolidation.
C-19 follows from C-15 + C-18 co-occurrence. Three criteria from the same enforcement
sentence.

```
You are running /validate-inertia for: {{feature}}

Stress-test the adoption case. The question is: why would users not adopt this feature
even if it works perfectly? Map the inertia per persona and name the kill barrier.

---

PHASE 1: SITUATE THE WORKAROUND

Establish the status quo:
- What users are currently doing instead of this feature
- Which personas rely on the workaround most and why
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

### Aspirational coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Inertia reduction conditions | PASS | PASS | PASS | PASS | PASS |
| C-10 AMEND persona-specific + actionable | PASS | PASS | PASS | PASS | PASS |
| C-11 Kill barrier grounded in per-persona evidence | PASS | PASS | PASS | PASS | PASS |
| C-12 Workaround satisfaction per-persona (vocab) | PASS | PASS | PASS | PASS | PASS |
| C-13 No required field blank or bare label | PASS | PASS | PASS | PASS | PASS |
| C-14 Each AMEND names persona AND gap | PASS | PASS | PASS | PASS | PASS |
| C-15 Kill barrier as table column | PASS | PASS | PASS | PASS | PASS |
| C-16 Single gate bundles C-11..C-14 | PARTIAL | PASS | PASS | PARTIAL | PASS |
| C-17 Enforcement through mechanism not labels | PASS | PASS | PASS | PASS | PASS |
| C-18 Gate includes forward reference | PASS | PASS | PASS | PASS | PASS |
| C-19 Structural + procedural co-occur | PASS | PASS | PASS | PASS | PASS |
| C-20 Distributed achieves C-19 without C-16 | PASS | FAIL | FAIL | PASS | FAIL |
| C-21 One-sentence scan closes C-16+C-18 | FAIL | PASS | FAIL | FAIL | PASS |
| C-22 Block-to-table minimum sufficient repair | PASS | PASS | PASS | PASS | PASS |
| **Pass count** | **12/14** | **13/14** | **13/14** | **12/14** | **13/14** |

### Predicted composite scores (v5 rubric)

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-02 Scan-forward-ref (C-21) | 60 | 30 | 9.29 | **99.29** |
| V-03 Gate-2-canonical (C-22) | 60 | 30 | 9.29 | **99.29** |
| V-05 Scan-table hybrid (C-21+C-22) | 60 | 30 | 9.29 | **99.29** |
| V-01 Three-layer distributed (C-20) | 60 | 30 | 8.57 | **98.57** |
| V-04 Gate-2-equivalent + distributed (C-20+C-22) | 60 | 30 | 8.57 | **98.57** |

**R5 ceiling: 99.29.** C-16 PASS and C-20 PASS are mutually exclusive; C-21 PASS requires
C-16 PASS; therefore no single variation can pass all 14 aspirationals.

Open questions that scoring will resolve:
- Does C-22 apply to narrow evidence gates (V-01, V-04) or only full C-16 consolidating gates?
- Is the scan in V-02/V-05 a valid Gate-2-equivalent for C-22, or does C-22 require a gate-format checkpoint?
- If C-22 FAIL in V-01/V-04, they drop to 11/14 → 97.86.
- If C-22 FAIL in V-02/V-05, they drop to 12/14 → 98.57.
