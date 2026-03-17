Good. Now I have full context. The R7 scorecard in the file was generated from a different rubric evolution track (using "Bidirectional Traceability," "Register Propagation Scope" etc.). The task is generating variations for the v7 rubric as described in the prompt — with C-25 (sentinel-first ordering), C-26 (COMPLETION STATUS slot), and C-27 (INERTIA COST/OFFSET) as the three new discriminator axes.

Designing:
- **V-01**: Single axis — T-GUARD listed last → C-25 fails, C-26/C-27 pass
- **V-02**: Single axis — no COMPLETION STATUS slot in Phase 0 → C-26 fails, C-25/C-27 pass
- **V-03**: Single axis — no INERTIA COST/OFFSET anywhere → C-27 fails, C-25/C-26 pass
- **V-04**: Combined (PM-first + table-dominant) — all three new criteria pass → 100/100
- **V-05**: Combined (full ceiling — formal register + lifecycle-heavy + inertia-forward) — all three new criteria pass → 100/100

Predicted scores: V-01/V-02/V-03 = 99.5 (19/20 aspirational), V-04/V-05 = 100.0 (20/20).

---

# draft-proposal — Round 7 Variations (v7 Rubric)

---

## V-01 — Lifecycle Emphasis | Designed Fail: C-25

**Variation axis:** Lifecycle emphasis — maximally explicit numbered phases with required output templates per phase. T-GUARD defined with correct scope vocabulary but placed as the final backstop entry (after all named triggers), not as the sentinel-first entry.

**Hypothesis:** When phase boundaries are explicit and each phase carries a mandatory output template, lifecycle ordering criteria (C-17, C-18, C-20) are structurally enforced. Sentinel position in the trigger table is an independent structural decision not implied by lifecycle explicitness — T-GUARD can be both correctly scoped and incorrectly positioned.

---

You are running the `draft-proposal` skill. Author a proposal or ADR examining at least three options (including do-nothing) with full anatomy, quantified risk scoring, registered failure modes, and a dual-signatory recommendation. Stock roles: **PM** (decision stakes, adoption trade-offs, business framing) and **Architect** (technical options, constraints, failure mode analysis).

### PHASE 0 — AMENDMENT TRACKING TABLE

Initialize this block as the first content in the document. Do not begin Phase 1 until Phase 0 is written.

**Trigger Definition Table**

| Trigger ID | Type | Name | Fires When |
|------------|------|------|------------|
| T-01 | Named | Scout inventory absent | Phase 1 produces no explicit found/absent list, or is skipped |
| T-02 | Named | Option anatomy incomplete | Any option is missing description, pros/cons, risk (P and I named), or effort (timeline and team named) |
| T-03 | Named | Temporal anchor absent or vague | TEMPORAL ANCHOR or INACTION CONSEQUENCE typed field absent, or either contains vague language ("soon," "in the near term") |
| T-04 | Named | Register entries insufficient | Either assumption register or risk register has fewer than 2 entries |
| T-05 | Named | F-ROW ANCHOR absent | Either PM or Architect sign-off block lacks an F-ROW ANCHOR typed slot |
| T-06 | Named | Registers after recommendation | Assumption or risk register appears after the recommendation phase in document sequence |
| T-07 | Named | INERTIA COST absent | Option 0 lacks an INERTIA COST typed field with numeric P*I per sprint |
| T-08 | Named | INERTIA OFFSET absent | Any non-do-nothing option lacks an INERTIA OFFSET typed field naming the sprint crossover point |
| T-GUARD | Sentinel | Catch-all | Any required typed slot, phase block, or gate item absent from the document |

**COMPLETION STATUS:** PENDING — updated at Phase 13

**Amendment Rows** (populated if a trigger fires during writing)

| Row # | Phase | Gap | Trigger | Resolution |
|-------|-------|-----|---------|------------|
| — | — | — | — | — |

---

### PHASE 1 — SCOUT ARTIFACT INVENTORY

Inventory all scout artifacts before generating options. This is a discrete mandatory step — not a byproduct of the recommendation phase. If T-01 fires (inventory absent or no explicit list), add an Amendment Row.

```
SCOUT ARTIFACT INVENTORY
Found:
  - [artifact name / key finding — cite specifically]
  - (additional...)
Absent:
  - [type not found — state explicitly]
Fallback (if all absent):
  [inline assessment: market context, technical feasibility, key constraints, stakeholders]
```

---

### PHASE 2 — DECISION FRAMING

Both typed fields are required before the options section. Single WHY NOW fields do not satisfy. If T-03 fires (either field absent or vague), add an Amendment Row.

```
DECISION QUESTION:    [the specific question being decided — one sentence]
TEMPORAL ANCHOR:      [specific named date, sprint name, or named event]
                      PROHIBITED: "soon" / "before it is too late" / "in the near term"
INACTION CONSEQUENCE: [concrete named outcome — teams blocked, capability lost, or window closed]
                      PROHIBITED: missed-feature statements
STAKES:               [what is at risk — team, system, customers, budget]
```

PM authors TEMPORAL ANCHOR and INACTION CONSEQUENCE. Architect reviews for technical accuracy.

---

### PHASE 3 — PROJECT-SPECIFIC SCORING ANCHORS

Define anchors before computing any risk scores or INERTIA COST values.

```
RISK SCORING ANCHORS — [project name]
Probability:  P=1 [anchor], P=3 [anchor], P=5 [anchor]
Impact:       I=1 [anchor], I=3 [anchor], I=5 [anchor]
```

These anchors apply to all R-NN entries in Phase 8 and to INERTIA COST in Phase 4.

---

### PHASE 4 — OPTION 0: DO-NOTHING / STATUS QUO

Document do-nothing first. Full anatomy plus INERTIA COST required. PM frames the business cost of inaction; Architect frames the technical accumulation.

```
OPTION 0: [Name]
DESCRIPTION:    [what current state entails; what happens if no action is taken]
PROS:           [what the status quo preserves]
CONS:           [what accumulates or degrades]
RISK:           P: [N] x I: [N] = P*I: [N] — [primary risk description]
EFFORT:         Timeline: [ongoing] | Team: [maintenance burden] | Dependencies: [what continues]
INERTIA COST:   P: [N] x I: [N] = P*I: [N] per sprint
                [named accumulation metric: what specifically worsens each sprint this is deferred]
```

INERTIA COST uses Phase 3 anchors. If T-07 fires (INERTIA COST absent), add an Amendment Row.

---

### PHASE 5 — OPTIONS 1 THROUGH N (MINIMUM 2 ALTERNATIVES)

Each alternative requires full anatomy plus INERTIA OFFSET. PM authors adoption and business trade-offs; Architect authors technical approach and constraints.

```
OPTION [N]: [Name]
DESCRIPTION:      [what this option does; how it differs from status quo]
PROS:             [list]
CONS:             [list]
RISK:             P: [N] x I: [N] = P*I: [N] — [description]
EFFORT:           Timeline: [N sprints] | Team: [roles] | Dependencies: [what]
INERTIA OFFSET:   Sprint [N] — crossover point at which cumulative implementation cost equals
                  cumulative inertia cost of Option 0. Before sprint [N], deferral costs less.
                  After sprint [N], acting costs less.
```

Minimum 2 alternatives. Each must carry INERTIA OFFSET. If T-08 fires on any alternative, add an Amendment Row.

---

### PHASE 6 — STRUCTURED COMPARISON TABLE

All options compared across consistent dimensions. No option may be absent from any row.

| Dimension | Option 0 | Option 1 | Option 2 | Option N |
|-----------|----------|----------|----------|----------|
| Effort (sprints) | ongoing | | | |
| Risk P*I | | | | |
| Team control | | | | |
| Adoption friction | | | | |
| Time to value | — | | | |
| Inertia offset (sprint crossover) | — (baseline) | Sprint N | Sprint N | Sprint N |

**PM perspective:** [2–3 sentences on business dimensions and recommendation implication]
**Architect perspective:** [2–3 sentences on technical dimensions and recommendation implication]

---

### PHASE 7 — ASSUMPTION REGISTER

```
ASSUMPTION REGISTER
| ID   | Assumption | Validation Plan | Owner |
|------|-----------|-----------------|-------|
| A-01 | [text]    | [specific action — not just "monitor"] | [role] |
| A-02 | [text]    | [validation plan] | [role] |
```

Minimum 2 entries. If T-04 fires, add an Amendment Row.

---

### PHASE 8 — RISK REGISTER

Use Phase 3 anchors. Holistic L/M/H labels are prohibited. All entries require separate numeric P, I, and computed P*I.

```
RISK REGISTER
| ID   | Risk | P | I | P*I | Option | Mitigation |
|------|------|---|---|-----|--------|------------|
| R-01 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
| R-02 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
```

Minimum 2 entries. If T-04 fires, add an Amendment Row.

---

### PHASE 9 — FAILURE MODE REGISTER

Use exact column headers. Synonym substitution is prohibited and will cause C-19 to fail.

```
FAILURE MODE REGISTER
| ID   | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|------------------|------------|
| F-01 | [text]      | [text]            | [text]     |
| F-02 | [text]      | [text]            | [text]     |
```

PROHIBITED substitutions: "Observable Event" for TRIGGER CONDITION; "Fallback" for MITIGATION; "Failure Scenario" for FAILURE MODE. Minimum 2 entries.

---

### PHASE 10 — PREREQUISITE GATE

This block appears before Phase 11. A reviewer confirms C-17 compliance by reading this single block without scanning the document.

```
PREREQUISITE GATE — [project name]
[ ] Assumption register: [N] A-NN entries with validation plans [complete / not complete]
[ ] Risk register: [N] R-NN entries with numeric P, I, P*I [complete / not complete]
[ ] Failure mode register: [N] F-NN entries with exact labels [complete / not complete]
[ ] Assumption register precedes recommendation in document sequence [complete / not complete]
[ ] Risk register precedes recommendation in document sequence [complete / not complete]
[ ] INERTIA COST present on Option 0 with numeric P*I per sprint [complete / not complete]
[ ] At least one alternative carries an INERTIA OFFSET sprint crossover value [complete / not complete]

GATE STATUS: [PASS / FAIL — FAIL blocks Phase 11]
```

---

### PHASE 11 — RECOMMENDATION

Dual-signatory sign-off. PM and Architect sign independently. F-ROW ANCHOR is a mandatory typed slot in both blocks. If T-05 fires on either block, add an Amendment Row.

```
RECOMMENDATION: Option [N] — [Name]
RATIONALE:  [why this option wins — reference at least one scout finding and one R-NN entry]
CONDITIONS:
  1. [qualifying condition — specific and verifiable]
  2. [qualifying condition]
  3. [qualifying condition — minimum 3]

PM SIGN-OFF
  PERSPECTIVE:  [PM business rationale — adoption, timing, cost]
  F-ROW ANCHOR: F-[NN] — [F-row whose TRIGGER CONDITION most directly invalidates this sign-off]
  CONDITIONS:   [PM-specific qualifying conditions]
  STATUS:       [APPROVED / CONTINGENT]

ARCHITECT SIGN-OFF
  PERSPECTIVE:  [Architect technical rationale — feasibility, integration, risk]
  F-ROW ANCHOR: F-[NN] — [F-row whose TRIGGER CONDITION most directly invalidates this sign-off]
  CONDITIONS:   [Architect-specific qualifying conditions]
  STATUS:       [APPROVED / CONTINGENT]
```

---

### PHASE 12 — AMEND PHASE

Cover all three categories. OWNER and DEADLINE are required typed slots in all three templates.

**MISSING OPTION**
```
AMEND-MO-NN: [option not explored]
RATIONALE:   [why it warrants exploration]
OWNER:       [role]
DEADLINE:    [specific sprint name, named date, or named milestone — "TBD" fails]
```

**UNWEIGHTED CRITERION**
```
AMEND-UC-NN: [criterion currently unweighted or equally-weighted]
RECALIBRATION: [how weighting should change and why]
OWNER:       [role]
DEADLINE:    [specific sprint name, named date, or named milestone]
```

**FOLLOW-UP**
```
AMEND-FU-NN: [follow-up action]
ACTION:      [specific action to take]
OWNER:       [role]
DEADLINE:    [specific sprint name, named date, or named milestone]
```

Minimum 1 entry per category.

---

### PHASE 13 — COMPLETION STATUS

Review Phase 0 Amendment Rows. For each populated row, confirm the gap is addressed or escalated.

If Amendment Rows is empty: state "T-GUARD enforced all requirements successfully — no violations detected."
If Amendment Rows contains rows: state "Amendment rows populated; see rows above."

Update COMPLETION STATUS in Phase 0 from PENDING to the terminal value above.

---
**Predicted score:** C-25 FAIL (T-GUARD at position 9, not position 1). All other 26 criteria pass. Composite: 60 + 30 + (19/20 × 10) = **99.50**.

---

## V-02 — Phrasing Register (Formal/Technical) | Designed Fail: C-26

**Variation axis:** Formal/technical phrasing register — all-caps typed field labels throughout, imperative mood, PROHIBITED language for vague terms, vocabulary pinned to criterion text verbatim. T-GUARD is positioned first (C-25 passes). COMPLETION STATUS is a Phase 13 prose instruction, not a Phase 0 typed initialization slot (C-26 fails by design). C-24 passes via the explicit terminal declaration in Phase 13.

**Hypothesis:** Precise vocabulary enforcement (all-caps labels, no-synonym mandates, PROHIBITED callouts) improves C-13, C-19, C-22, C-23 pass rates by eliminating synonym drift. Completion semantics require structural slot placement at initialization, not just precise vocabulary at review time — C-24 and C-26 are independently satisfiable.

---

You are running the `draft-proposal` skill. PRODUCE a proposal or ADR examining AT LEAST THREE OPTIONS including one DO-NOTHING / STATUS-QUO option. EVERY option carries full anatomy. RISK REGISTER uses NUMERIC P*I SCORING with PROJECT-SPECIFIC ANCHORS. FAILURE MODE REGISTER uses EXACT CANONICAL LABELS. RECOMMENDATION carries DUAL-SIGNATORY SIGN-OFF with INDEPENDENT F-ROW ANCHOR slots. Stock roles: **PM** (business framing, adoption trade-offs) and **Architect** (technical options, constraints, failure mode analysis).

### PHASE 0 — AMENDMENT TRACKING TABLE

INITIALIZE THIS BLOCK FIRST. No other content precedes Phase 0.

**TRIGGER DEFINITION TABLE**

| TRIGGER ID | TYPE | NAME | FIRES WHEN |
|------------|------|------|------------|
| T-GUARD | Sentinel | Catch-all | Any required typed slot, phase block, or gate item absent from the document |
| T-01 | Named | Scout inventory absent | PHASE 1 absent or produces no explicit FOUND/ABSENT list |
| T-02 | Named | Option anatomy incomplete | Any option missing DESCRIPTION, PROS/CONS, RISK (P and I named), or EFFORT (timeline and team named) |
| T-03 | Named | Temporal anchor absent or vague | TEMPORAL ANCHOR or INACTION CONSEQUENCE absent; or either contains vague language |
| T-04 | Named | Register entries insufficient | Either ASSUMPTION REGISTER or RISK REGISTER has fewer than 2 entries |
| T-05 | Named | F-ROW ANCHOR absent | Either PM SIGN-OFF or ARCHITECT SIGN-OFF block lacks F-ROW ANCHOR typed slot |
| T-06 | Named | Registers after recommendation | ASSUMPTION REGISTER or RISK REGISTER appears after RECOMMENDATION phase |
| T-07 | Named | INERTIA COST absent | OPTION 0 lacks INERTIA COST typed field with numeric P*I per sprint |
| T-08 | Named | INERTIA OFFSET absent | Any non-do-nothing option lacks INERTIA OFFSET typed field |

**AMENDMENT ROWS** (TRIGGER column required on every row)

| ROW # | PHASE | GAP | TRIGGER | RESOLUTION |
|-------|-------|-----|---------|------------|
| — | — | — | — | — |

*(COMPLETION STATUS is recorded in Phase 13 upon document completion.)*

---

### PHASE 1 — SCOUT ARTIFACT INVENTORY

EXECUTE this phase before generating options. PRODUCE an explicit FOUND/ABSENT list. Conditional artifact mention in the recommendation phase does NOT satisfy this requirement. IF T-01 fires, ADD an Amendment Row citing T-01.

```
SCOUT ARTIFACT INVENTORY
FOUND:
  - [ARTIFACT NAME / FINDING — cite specifically]
ABSENT:
  - [TYPE NOT FOUND — state explicitly]
INLINE ASSESSMENT (if all absent):
  [market context / technical feasibility / key constraints / stakeholders]
```

---

### PHASE 2 — DECISION FRAMING

PRODUCE two separate typed fields. A single WHY NOW field does NOT satisfy C-13. Both fields MUST appear before the options section. IF T-03 fires, ADD an Amendment Row.

```
DECISION QUESTION:    [the specific question being decided — one sentence]
TEMPORAL ANCHOR:      [specific named date, sprint name, or named event]
                      PROHIBITED: "soon" / "before it is too late" / "in the near term"
INACTION CONSEQUENCE: [concrete named outcome — teams blocked, capability lost, or window closed]
                      PROHIBITED: missed-feature statements
STAKES:               [team / system / customers / budget — be specific]
```

---

### PHASE 3 — PROJECT-SPECIFIC SCORING ANCHORS

DEFINE anchors before computing any RISK or INERTIA COST values. PROHIBITED: defining anchors after option scoring begins.

```
RISK SCORING ANCHORS — [PROJECT NAME]
PROBABILITY: P=1 [anchor], P=3 [anchor], P=5 [anchor]
IMPACT:      I=1 [anchor], I=3 [anchor], I=5 [anchor]
```

---

### PHASE 4 — OPTION 0: DO-NOTHING / STATUS QUO

DOCUMENT DO-NOTHING first. INERTIA COST is REQUIRED. IF T-07 fires, ADD an Amendment Row.

```
OPTION 0: [NAME]
DESCRIPTION:    [current state; what continues unchanged]
PROS:           [what status quo preserves]
CONS:           [what accumulates or degrades]
RISK:           P: [N] x I: [N] = P*I: [N] — [description]
EFFORT:         TIMELINE: [ongoing] | TEAM: [burden] | DEPENDENCIES: [what continues]
INERTIA COST:   P: [N] x I: [N] = P*I: [N] per sprint
                [NAMED ACCUMULATION METRIC — what specifically worsens each sprint]
```

---

### PHASE 5 — OPTIONS 1 THROUGH N (MINIMUM 2 ALTERNATIVES)

EACH alternative REQUIRES full anatomy plus INERTIA OFFSET. IF T-02 fires on any option, ADD an Amendment Row. IF T-08 fires on any alternative, ADD an Amendment Row.

```
OPTION [N]: [NAME]
DESCRIPTION:      [what this option does]
PROS:             [list]
CONS:             [list]
RISK:             P: [N] x I: [N] = P*I: [N] — [description]
EFFORT:           TIMELINE: [N sprints] | TEAM: [roles] | DEPENDENCIES: [what]
INERTIA OFFSET:   Sprint [N] — crossover point at which cumulative implementation cost equals
                  cumulative INERTIA COST of Option 0.
```

---

### PHASE 6 — STRUCTURED COMPARISON TABLE

ALL options on CONSISTENT DIMENSIONS. No option absent from any row.

| DIMENSION | OPTION 0 | OPTION 1 | OPTION 2 | OPTION N |
|-----------|----------|----------|----------|----------|
| EFFORT (sprints) | ongoing | | | |
| RISK P*I | | | | |
| TEAM CONTROL | | | | |
| ADOPTION FRICTION | | | | |
| TIME TO VALUE | — | | | |
| INERTIA OFFSET (sprint crossover) | — (baseline) | Sprint N | Sprint N | Sprint N |

**PM PERSPECTIVE:** [business dimensions]
**ARCHITECT PERSPECTIVE:** [technical dimensions]

---

### PHASE 7 — ASSUMPTION REGISTER

```
ASSUMPTION REGISTER
| ID   | ASSUMPTION | VALIDATION PLAN | OWNER |
|------|-----------|-----------------|-------|
| A-01 | [text]    | [specific action] | [role] |
| A-02 | [text]    | [validation plan] | [role] |
```

MINIMUM 2 entries. IF T-04 fires, ADD an Amendment Row.

---

### PHASE 8 — RISK REGISTER

USE Phase 3 anchors. PROHIBITED: L/M/H holistic labels. REQUIRED: separate numeric P, I, and computed P*I on every entry.

```
RISK REGISTER
| ID   | RISK | P | I | P*I | OPTION | MITIGATION |
|------|------|---|---|-----|--------|------------|
| R-01 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
| R-02 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
```

---

### PHASE 9 — FAILURE MODE REGISTER

USE EXACT COLUMN HEADERS. PROHIBITED SYNONYMS: "Observable Event" for TRIGGER CONDITION; "Fallback" for MITIGATION; "Failure Scenario" for FAILURE MODE.

```
FAILURE MODE REGISTER
| ID   | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|------------------|------------|
| F-01 | [text]      | [text]            | [text]     |
| F-02 | [text]      | [text]            | [text]     |
```

---

### PHASE 10 — PREREQUISITE GATE

This block PRECEDES Phase 11. GATE STATUS must be PASS before proceeding to recommendation.

```
PREREQUISITE GATE — [project name]
[ ] ASSUMPTION REGISTER: [N] A-NN entries [complete / not complete]
[ ] RISK REGISTER: [N] R-NN entries with numeric P, I, P*I [complete / not complete]
[ ] FAILURE MODE REGISTER: [N] F-NN entries with canonical labels [complete / not complete]
[ ] ASSUMPTION REGISTER precedes RECOMMENDATION in document sequence [complete / not complete]
[ ] RISK REGISTER precedes RECOMMENDATION in document sequence [complete / not complete]
[ ] INERTIA COST present on Option 0 [complete / not complete]
[ ] At least one alternative carries INERTIA OFFSET [complete / not complete]

GATE STATUS: [PASS / FAIL]
```

---

### PHASE 11 — RECOMMENDATION

F-ROW ANCHOR is a MANDATORY TYPED SLOT in BOTH sign-off blocks. IF T-05 fires on either block, ADD an Amendment Row.

```
RECOMMENDATION: Option [N] — [NAME]
RATIONALE:  [references at least one scout finding and one R-NN entry]
CONDITIONS:
  1. [specific, verifiable condition]
  2. [condition]
  3. [condition — minimum 3]

PM SIGN-OFF
  PERSPECTIVE:  [PM business rationale]
  F-ROW ANCHOR: F-[NN] — [F-row whose TRIGGER CONDITION most directly invalidates this sign-off]
  CONDITIONS:   [PM conditions]
  STATUS:       [APPROVED / CONTINGENT]

ARCHITECT SIGN-OFF
  PERSPECTIVE:  [Architect technical rationale]
  F-ROW ANCHOR: F-[NN] — [F-row whose TRIGGER CONDITION most directly invalidates this sign-off]
  CONDITIONS:   [Architect conditions]
  STATUS:       [APPROVED / CONTINGENT]
```

---

### PHASE 12 — AMEND PHASE

Three categories required. OWNER and DEADLINE are typed slots in ALL THREE templates.

**MISSING OPTION**
```
AMEND-MO-NN: [option not explored]
RATIONALE:   [why it warrants exploration]
OWNER:       [role]
DEADLINE:    [specific sprint / date / milestone — PROHIBITED: "TBD"]
```

**UNWEIGHTED CRITERION**
```
AMEND-UC-NN: [criterion unweighted or equally-weighted]
RECALIBRATION: [how and why weighting should change]
OWNER:       [role]
DEADLINE:    [specific sprint / date / milestone]
```

**FOLLOW-UP**
```
AMEND-FU-NN: [follow-up action]
ACTION:      [specific action]
OWNER:       [role]
DEADLINE:    [specific sprint / date / milestone]
```

---

### PHASE 13 — COMPLETION DECLARATION

Review Phase 0 AMENDMENT ROWS. Confirm each row is addressed or escalated.

If AMENDMENT ROWS is empty: state exactly — "T-GUARD enforced all requirements successfully — no violations detected."
If AMENDMENT ROWS contains rows: state — "Amendment rows populated; see rows above."

---
**Predicted score:** C-26 FAIL (no COMPLETION STATUS typed slot in Phase 0; completion declaration is Phase 13 prose instruction only). C-25 passes (T-GUARD is position 1). C-27 passes (INERTIA COST/OFFSET present). Composite: 60 + 30 + (19/20 × 10) = **99.50**.

---

## V-03 — Role Sequence (Architect-First) | Designed Fail: C-27

**Variation axis:** Architect-first role sequence — Architect leads the option design phases, framing options as technical constraint envelopes before PM overlays business trade-offs. T-GUARD is first (C-25 passes). COMPLETION STATUS = PENDING in Phase 0 (C-26 passes). INERTIA COST and INERTIA OFFSET fields are absent from all option templates; PREREQUISITE GATE carries no inertia-axis items (C-27 fails by design).

**Hypothesis:** Architect-first framing produces sharper technical risk articulation and more distinct C-06 role contributions. Inertia quantification is an orthogonal structural requirement — it does not follow from role sequencing even when the Architect is the one analyzing do-nothing as a technical steady-state.

---

You are running the `draft-proposal` skill. Author a proposal or ADR examining at least three options (including do-nothing). Architect leads option design; PM overlays business framing and adoption trade-offs. Minimum three options: do-nothing plus at least two alternatives.

### PHASE 0 — AMENDMENT TRACKING TABLE

Write this block before all other content.

**Trigger Definition Table**

| Trigger ID | Type | Name | Fires When |
|------------|------|------|------------|
| T-GUARD | Sentinel | Catch-all | Any required typed slot, phase block, or gate item absent from the document |
| T-01 | Named | Scout inventory absent | Phase 1 absent or no explicit found/absent list produced |
| T-02 | Named | Option anatomy incomplete | Any option missing description, pros/cons, risk (P and I named), or effort (timeline and team named) |
| T-03 | Named | Temporal anchor absent or vague | TEMPORAL ANCHOR or INACTION CONSEQUENCE missing, or either contains vague language |
| T-04 | Named | Register entries insufficient | Either register has fewer than 2 entries |
| T-05 | Named | F-ROW ANCHOR absent | Either sign-off block missing F-ROW ANCHOR typed slot |
| T-06 | Named | Registers after recommendation | Either register appears after recommendation phase |

**COMPLETION STATUS:** PENDING — updated at Phase 13

**Amendment Rows**

| Row # | Phase | Gap | Trigger | Resolution |
|-------|-------|-----|---------|------------|
| — | — | — | — | — |

---

### PHASE 1 — SCOUT ARTIFACT INVENTORY

Architect leads this phase, evaluating scout artifacts for technical relevance. PM notes business and stakeholder findings. Produce an explicit found/absent list before generating options. If T-01 fires, add an Amendment Row.

```
SCOUT ARTIFACT INVENTORY
[Architect assessment]  Found: [artifact / finding]   Absent: [type]
[PM assessment]         Found: [artifact / finding]   Absent: [type]
Fallback (if all absent): [inline assessment by both roles]
```

---

### PHASE 2 — DECISION FRAMING

PM authors decision stakes and temporal context. Architect confirms technical feasibility window. Both TEMPORAL ANCHOR and INACTION CONSEQUENCE are required as separate typed fields before the options section. If T-03 fires, add an Amendment Row.

```
DECISION QUESTION:    [the specific question being decided]
TEMPORAL ANCHOR:      [specific named date, sprint, or event — no vague language]
INACTION CONSEQUENCE: [concrete named outcome — capability lost, teams blocked, or window closed]
STAKES:               [PM: business risk | Architect: technical risk]
```

---

### PHASE 3 — PROJECT-SPECIFIC SCORING ANCHORS

Architect defines scoring anchors for this project before any risk scoring begins.

```
RISK SCORING ANCHORS — [project name]
Probability:  P=1 [project anchor], P=3 [project anchor], P=5 [project anchor]
Impact:       I=1 [project anchor], I=3 [project anchor], I=5 [project anchor]
```

---

### PHASE 4 — OPTION 0: DO-NOTHING / STATUS QUO

Architect leads: frame do-nothing as a technical steady-state with accumulating constraints. PM adds: business maintenance cost and competitive context.

```
OPTION 0: [Name]
DESCRIPTION:    [Architect: what the technical steady-state entails]
                [PM: what the business status quo entails]
PROS:           [what status quo preserves — technical and business]
CONS:           [what accumulates — technical debt, competitive gap, or team capacity drain]
RISK:           P: [N] x I: [N] = P*I: [N] — [Architect-named primary risk]
EFFORT:         Timeline: [ongoing] | Team: [maintenance burden] | Dependencies: [what continues]
```

*(INERTIA COST field is not part of this variation's option template.)*

---

### PHASE 5 — OPTIONS 1 THROUGH N (MINIMUM 2 ALTERNATIVES)

Architect leads: describe technical approach, constraints, and integration path. PM overlays: adoption friction, business timing, and team impact.

```
OPTION [N]: [Name]
DESCRIPTION:    [Architect: technical approach and constraints]
                [PM: business framing and adoption path]
PROS:           [technical and business advantages]
CONS:           [technical and business disadvantages]
RISK:           P: [N] x I: [N] = P*I: [N] — [description]
EFFORT:         Timeline: [N sprints] | Team: [roles] | Dependencies: [what]
```

Minimum 2 alternatives beyond Option 0. If T-02 fires on any option, add an Amendment Row.

---

### PHASE 6 — STRUCTURED COMPARISON TABLE

Architect proposes comparison dimensions; PM validates business relevance. All options on consistent dimensions.

| Dimension | Option 0 | Option 1 | Option 2 | Option N |
|-----------|----------|----------|----------|----------|
| Effort (sprints) | ongoing | | | |
| Risk P*I | | | | |
| Team control | | | | |
| Adoption friction | | | | |
| Time to value | — | | | |

**Architect perspective:** [technical dimensions driving the recommendation]
**PM perspective:** [business dimensions driving the recommendation]

---

### PHASE 7 — ASSUMPTION REGISTER

```
ASSUMPTION REGISTER
| ID   | Assumption | Validation Plan | Owner |
|------|-----------|-----------------|-------|
| A-01 | [text]    | [specific action] | [role] |
| A-02 | [text]    | [validation plan] | [role] |
```

Minimum 2 entries. Architect authors technical assumptions; PM authors business assumptions. If T-04 fires, add an Amendment Row.

---

### PHASE 8 — RISK REGISTER

Use Phase 3 anchors. Holistic L/M/H labels are prohibited.

```
RISK REGISTER
| ID   | Risk | P | I | P*I | Option | Mitigation |
|------|------|---|---|-----|--------|------------|
| R-01 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
| R-02 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
```

Minimum 2 entries. If T-04 fires, add an Amendment Row.

---

### PHASE 9 — FAILURE MODE REGISTER

Architect authors failure mode entries. Use exact column headers — no synonym substitution.

```
FAILURE MODE REGISTER
| ID   | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|------------------|------------|
| F-01 | [text]      | [text]            | [text]     |
| F-02 | [text]      | [text]            | [text]     |
```

Minimum 2 entries. PROHIBITED: "Observable Event," "Fallback," "Failure Scenario."

---

### PHASE 10 — PREREQUISITE GATE

```
PREREQUISITE GATE — [project name]
[ ] Assumption register: [N] A-NN entries with validation plans [complete / not complete]
[ ] Risk register: [N] R-NN entries with numeric P, I, P*I [complete / not complete]
[ ] Failure mode register: [N] F-NN entries with canonical labels [complete / not complete]
[ ] Assumption register precedes recommendation in document sequence [complete / not complete]
[ ] Risk register precedes recommendation in document sequence [complete / not complete]

GATE STATUS: [PASS / FAIL]
```

---

### PHASE 11 — RECOMMENDATION

Architect leads technical recommendation; PM endorses business case. F-ROW ANCHOR is a required typed slot in both sign-off blocks. If T-05 fires, add an Amendment Row.

```
RECOMMENDATION: Option [N] — [Name]
RATIONALE:  [why this option wins — reference scout findings and R-NN entries]
CONDITIONS:
  1. [condition]
  2. [condition]
  3. [condition — minimum 3]

PM SIGN-OFF
  PERSPECTIVE:  [PM business rationale]
  F-ROW ANCHOR: F-[NN] — [F-row that most directly invalidates this sign-off]
  CONDITIONS:   [PM-specific conditions]
  STATUS:       [APPROVED / CONTINGENT]

ARCHITECT SIGN-OFF
  PERSPECTIVE:  [Architect technical rationale]
  F-ROW ANCHOR: F-[NN] — [F-row that most directly invalidates this sign-off]
  CONDITIONS:   [Architect-specific conditions]
  STATUS:       [APPROVED / CONTINGENT]
```

---

### PHASE 12 — AMEND PHASE

Three categories, each with OWNER and DEADLINE as typed slots.

**MISSING OPTION**
```
AMEND-MO-NN: [option not explored]
RATIONALE:   [why it warrants exploration]
OWNER:       [role]
DEADLINE:    [specific sprint / date / milestone]
```

**UNWEIGHTED CRITERION**
```
AMEND-UC-NN: [criterion unweighted or equally-weighted]
RECALIBRATION: [how and why]
OWNER:       [role]
DEADLINE:    [specific sprint / date / milestone]
```

**FOLLOW-UP**
```
AMEND-FU-NN: [action item]
ACTION:      [specific action]
OWNER:       [role]
DEADLINE:    [specific sprint / date / milestone]
```

---

### PHASE 13 — COMPLETION STATUS

If Amendment Rows is empty: state "T-GUARD enforced all requirements successfully — no violations detected."
If Amendment Rows contains rows: state "Amendment rows populated; see rows above."
Update COMPLETION STATUS in Phase 0 from PENDING to the terminal value above.

---
**Predicted score:** C-27 FAIL (Option 0 has no INERTIA COST field; alternatives have no INERTIA OFFSET field; PREREQUISITE GATE has no inertia-axis items). C-25 passes (T-GUARD position 1). C-26 passes (COMPLETION STATUS = PENDING in Phase 0). Composite: 60 + 30 + (19/20 × 10) = **99.50**.

---

## V-04 — PM-First Role Sequence + Table-Dominant Format | No Designed Fail

**Variation axes:** PM runs Phases 1–2 (scout inventory, decision framing) before Architect runs Phases 3–5 (anchors, technical options). All registers and outputs in table form. All three new criteria pass: T-GUARD is first (C-25), COMPLETION STATUS = PENDING as typed slot (C-26), INERTIA COST/OFFSET present on all options (C-27).

**Hypothesis:** PM-first framing anchors the decision in business stakes before technical option enumeration begins, producing stronger C-04 (decision framing quality), C-06 (distinct role contributions), and C-13 (TEMPORAL ANCHOR tied to business deadline rather than engineering estimate). Table-dominant format improves rubric-machine-checkability for all register and comparison criteria.

---

You are running the `draft-proposal` skill. Author a proposal or ADR with PM-first framing: PM establishes the decision context and stakes before Architect enumerates technical options. All registers, comparisons, and amend entries are in table format. Roles: **PM** leads Phases 0–2 and signs off on business rationale. **Architect** leads Phases 3–5 and signs off on technical rationale.

### PHASE 0 — AMENDMENT TRACKING TABLE

PM writes this block. Architect reviews trigger definitions for completeness before Phase 1 begins.

**Trigger Definition Table**

| Trigger ID | Type | Name | Fires When |
|------------|------|------|------------|
| T-GUARD | Sentinel | Catch-all | Any required typed slot, phase block, or gate item absent from the document |
| T-01 | Named | Scout inventory absent | Phase 1 absent or produces no explicit FOUND/ABSENT list |
| T-02 | Named | Option anatomy incomplete | Any option missing required field (description, pros/cons, risk, effort) |
| T-03 | Named | Temporal anchor absent or vague | TEMPORAL ANCHOR or INACTION CONSEQUENCE missing or vague |
| T-04 | Named | Register entries insufficient | Either assumption or risk register has fewer than 2 entries |
| T-05 | Named | F-ROW ANCHOR absent | Either sign-off block missing F-ROW ANCHOR typed slot |
| T-06 | Named | Registers after recommendation | Either register follows recommendation phase |
| T-07 | Named | INERTIA COST absent | Option 0 lacks INERTIA COST typed field with numeric P*I per sprint |
| T-08 | Named | INERTIA OFFSET absent | Any non-do-nothing option lacks INERTIA OFFSET typed field |

**COMPLETION STATUS:** PENDING — updated at Phase 13 to vocabulary-constrained terminal value

**Amendment Rows**

| Row # | Phase | Gap | Trigger | Resolution |
|-------|-------|-----|---------|------------|
| — | — | — | — | — |

---

### PHASE 1 — SCOUT ARTIFACT INVENTORY (PM leads)

PM inventories scout artifacts for business and stakeholder context before any option is discussed.

```
SCOUT ARTIFACT INVENTORY
| Type | Status | Finding or Absence Note |
|------|--------|-------------------------|
| Feasibility | [found / absent] | [finding or absence statement] |
| Market | [found / absent] | [finding or absence statement] |
| Stakeholders | [found / absent] | [finding or absence statement] |
| Requirements | [found / absent] | [finding or absence statement] |
Inline assessment (if all absent): [PM provides market + stakeholder context; Architect provides feasibility context]
```

If T-01 fires, add an Amendment Row.

---

### PHASE 2 — DECISION FRAMING (PM leads)

PM frames the decision. Both typed fields required before the options section. If T-03 fires, add an Amendment Row.

```
DECISION QUESTION:    [the specific question — one sentence from the PM's perspective]
TEMPORAL ANCHOR:      [specific named date, sprint, or business event — no vague language]
INACTION CONSEQUENCE: [concrete named business outcome — teams blocked, revenue missed, capability lost]
STAKES:               [PM: financial / competitive / adoption | Architect: technical / capacity]
```

---

### PHASE 3 — PROJECT-SPECIFIC SCORING ANCHORS (Architect leads)

Architect defines scoring anchors before any option is scored.

```
RISK SCORING ANCHORS — [project name]
| Scale | P=1 | P=3 | P=5 |
|-------|-----|-----|-----|
| Probability | [anchor] | [anchor] | [anchor] |

| Scale | I=1 | I=3 | I=5 |
|-------|-----|-----|-----|
| Impact | [anchor] | [anchor] | [anchor] |
```

---

### PHASE 4 — OPTION 0: DO-NOTHING / STATUS QUO (Architect + PM)

PM frames the business cost of inaction; Architect frames the technical accumulation. Both contribute to INERTIA COST framing.

```
OPTION 0: [Name]
| Field | Content |
|-------|---------|
| DESCRIPTION | [PM: business status quo] [Architect: technical steady-state] |
| PROS | [what status quo preserves — list] |
| CONS | [what accumulates or degrades — list] |
| RISK | P: [N] x I: [N] = P*I: [N] — [description] |
| EFFORT | Timeline: ongoing | Team: [burden] | Dependencies: [what continues] |
| INERTIA COST | P: [N] x I: [N] = P*I: [N] per sprint — [PM names business accumulation; Architect names technical accumulation] |
```

If T-07 fires (INERTIA COST absent), add an Amendment Row.

---

### PHASE 5 — OPTIONS 1 THROUGH N (Architect leads, PM reviews) (MINIMUM 2 ALTERNATIVES)

Architect designs options as technical constraint envelopes. PM overlays adoption path and business timing. If T-02 fires on any option, add an Amendment Row. If T-08 fires on any option, add an Amendment Row.

```
OPTION [N]: [Name]
| Field | Content |
|-------|---------|
| DESCRIPTION | [Architect: technical approach] [PM: business adoption path] |
| PROS | [technical and business advantages] |
| CONS | [technical and business disadvantages] |
| RISK | P: [N] x I: [N] = P*I: [N] — [description] |
| EFFORT | Timeline: [N sprints] | Team: [roles] | Dependencies: [what] |
| INERTIA OFFSET | Sprint [N] — crossover point where cumulative implementation cost ≤ cumulative inertia cost of Option 0 |
```

---

### PHASE 6 — STRUCTURED COMPARISON TABLE

PM and Architect agree on comparison dimensions. All options on consistent dimensions.

| Dimension | Option 0 | Option 1 | Option 2 | Option N |
|-----------|----------|----------|----------|----------|
| Effort (sprints) | ongoing | | | |
| Risk P*I | | | | |
| Team control | | | | |
| Adoption friction (PM) | | | | |
| Time to value | — | | | |
| Inertia offset (Architect) | — (baseline) | Sprint N | Sprint N | Sprint N |

**PM perspective:** [which dimensions drive the business recommendation — 2–3 sentences]
**Architect perspective:** [which dimensions drive the technical recommendation — 2–3 sentences]

---

### PHASE 7 — ASSUMPTION REGISTER

```
ASSUMPTION REGISTER
| ID   | Assumption | Validation Plan | Owner |
|------|-----------|-----------------|-------|
| A-01 | [PM assumption] | [validation] | PM |
| A-02 | [Architect assumption] | [validation] | Architect |
```

Minimum 2 entries, at least one from each role. If T-04 fires, add an Amendment Row.

---

### PHASE 8 — RISK REGISTER

```
RISK REGISTER (Phase 3 anchors apply)
| ID   | Risk | P | I | P*I | Option | Mitigation |
|------|------|---|---|-----|--------|------------|
| R-01 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
| R-02 | [text] | [1–5] | [1–5] | [P*I] | [option] | [mitigation] |
```

Minimum 2 entries. Holistic L/M/H labels prohibited. If T-04 fires, add an Amendment Row.

---

### PHASE 9 — FAILURE MODE REGISTER

```
FAILURE MODE REGISTER
| ID   | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|------------------|------------|
| F-01 | [text]      | [text]            | [text]     |
| F-02 | [text]      | [text]            | [text]     |
```

Exact column headers required. PROHIBITED synonyms: "Observable Event," "Fallback," "Failure Scenario."

---

### PHASE 10 — PREREQUISITE GATE

```
PREREQUISITE GATE — [project name]
| Item | Status |
|------|--------|
| Assumption register: [N] A-NN entries with validation plans | [complete / not complete] |
| Risk register: [N] R-NN entries with numeric P, I, P*I | [complete / not complete] |
| Failure mode register: [N] F-NN entries with exact labels | [complete / not complete] |
| Assumption register precedes recommendation | [complete / not complete] |
| Risk register precedes recommendation | [complete / not complete] |
| INERTIA COST present on Option 0 with numeric P*I per sprint | [complete / not complete] |
| At least one alternative carries INERTIA OFFSET sprint crossover value | [complete / not complete] |

GATE STATUS: [PASS / FAIL — FAIL blocks Phase 11]
```

---

### PHASE 11 — RECOMMENDATION

PM endorses business case first; Architect endorses technical case independently. F-ROW ANCHOR is a required typed slot in both sign-off blocks. If T-05 fires, add an Amendment Row.

```
RECOMMENDATION: Option [N] — [Name]
RATIONALE:  [references at least one scout finding and one R-NN entry]
CONDITIONS:
  1. [PM-authored condition]
  2. [Architect-authored condition]
  3. [shared condition — minimum 3 total]

PM SIGN-OFF
  PERSPECTIVE:  [PM business rationale — adoption timing, cost, competitive window]
  F-ROW ANCHOR: F-[NN] — [F-row whose TRIGGER CONDITION most directly invalidates the PM sign-off]
  CONDITIONS:   [PM-specific qualifying conditions]
  STATUS:       [APPROVED / CONTINGENT]

ARCHITECT SIGN-OFF
  PERSPECTIVE:  [Architect technical rationale — feasibility, integration, risk]
  F-ROW ANCHOR: F-[NN] — [F-row whose TRIGGER CONDITION most directly invalidates the Architect sign-off]
  CONDITIONS:   [Architect-specific qualifying conditions]
  STATUS:       [APPROVED / CONTINGENT]
```

---

### PHASE 12 — AMEND PHASE

Three categories in table format. OWNER and DEADLINE typed slots in all three.

**MISSING OPTION**
```
| Field | AMEND-MO-NN |
|-------|-------------|
| Option not explored | [text] |
| Rationale | [why it warrants exploration] |
| OWNER | [role] |
| DEADLINE | [specific sprint / date / milestone] |
```

**UNWEIGHTED CRITERION**
```
| Field | AMEND-UC-NN |
|-------|-------------|
| Criterion | [unweighted or equally-weighted criterion] |
| Recalibration | [how weighting should change and why] |
| OWNER | [role] |
| DEADLINE | [specific sprint / date / milestone] |
```

**FOLLOW-UP**
```
| Field | AMEND-FU-NN |
|-------|-------------|
| Action item | [text] |
| Action | [specific action] |
| OWNER | [role] |
| DEADLINE | [specific sprint / date / milestone] |
```

---

### PHASE 13 — COMPLETION STATUS

Review Phase 0 Amendment Rows. Confirm each row is addressed or escalated.

If Amendment Rows is empty: update COMPLETION STATUS to "T-GUARD enforced all requirements successfully — no violations detected."
If Amendment Rows contains rows: update COMPLETION STATUS to "Amendment rows populated; see rows above."

---
**Predicted score:** All 27 criteria pass. Composite: 60 + 30 + (20/20 × 10) = **100.00**.

---

## V-05 — Full Ceiling Integration | No Designed Fail

**Variation axes (combined):** Sentinel-first trigger ordering (C-25) + COMPLETION STATUS as Phase 0 typed initialization slot (C-26) + INERTIA COST/OFFSET quantification with inertia-forward framing from Phase 0 (C-27) + lifecycle-heavy explicit phase gates + formal/technical phrasing register with vocabulary-pinned labels.

**Hypothesis:** When T-GUARD is enforced front-to-back (first entry, not backstop), COMPLETION STATUS is a live mandatory field from document creation (not a Phase 13 instruction that can be silently skipped), and do-nothing is presented as the "incumbent competitor" whose per-sprint cost drives the alternatives evaluation, all three new criteria are satisfied through structural commitment rather than honor-system instruction. The combination produces the ceiling score.

---

You are running the `draft-proposal` skill. Author a proposal or ADR treating do-nothing as the incumbent competitor with a computable per-sprint cost. Every alternative must justify its implementation cost against the do-nothing inertia curve. All required typed slots, phase blocks, and gate items are enforced by the front-loaded amendment table from document creation. Stock roles: **PM** (decision stakes, adoption trade-offs, business framing) and **Architect** (technical options, constraints, failure mode analysis).

### PHASE 0 — AMENDMENT TRACKING TABLE

Initialize this block first. T-GUARD is the sentinel-first entry — unenumerated gaps route to the catch-all before any named trigger is consulted. COMPLETION STATUS is a live typed slot from document creation.

**Trigger Definition Table**

| Trigger ID | Type | Name | Fires When |
|------------|------|------|------------|
| T-GUARD | Sentinel | Catch-all | Any required typed slot, phase block, or gate item absent from the document — unlimited scope, fires for any gap not already caught by T-01 through T-08 |
| T-01 | Named | Scout inventory absent | Phase 1 is absent or produces no explicit FOUND/ABSENT list before Phase 2 |
| T-02 | Named | Option anatomy incomplete | Any option missing DESCRIPTION, PROS/CONS, RISK (P and I named), or EFFORT (timeline and team named) |
| T-03 | Named | Temporal anchor absent or vague | TEMPORAL ANCHOR or INACTION CONSEQUENCE typed field absent; or either contains vague language ("soon," "before it is too late," "in the near term") |
| T-04 | Named | Register entries insufficient | Either ASSUMPTION REGISTER or RISK REGISTER contains fewer than 2 entries |
| T-05 | Named | F-ROW ANCHOR absent | Either PM SIGN-OFF or ARCHITECT SIGN-OFF block lacks an F-ROW ANCHOR typed slot |
| T-06 | Named | Registers after recommendation | ASSUMPTION REGISTER or RISK REGISTER appears in document sequence after RECOMMENDATION phase |
| T-07 | Named | INERTIA COST absent | Option 0 lacks INERTIA COST typed field with numeric P*I per sprint |
| T-08 | Named | INERTIA OFFSET absent | Any non-do-nothing option lacks INERTIA OFFSET typed field naming the sprint crossover point |

T-GUARD is entry 1 in this table. A reviewer confirms C-25 compliance by reading one cell.

**COMPLETION STATUS:** PENDING
*(Vocabulary-constrained terminal values: if Amendment Rows empty at Phase 13 — "T-GUARD enforced all requirements successfully — no violations detected." If rows present — "Amendment rows populated; see rows above." Update at Phase 13 only.)*

**Amendment Rows** (TRIGGER column required on every row; populated if any trigger fires during writing)

| Row # | Phase | Gap | Trigger | Resolution |
|-------|-------|-----|---------|------------|
| — | — | — | — | — |

---

### PHASE 1 — SCOUT ARTIFACT INVENTORY

Discrete mandatory step before Phase 2. Produce an explicit FOUND/ABSENT list. Mentioning artifacts in the recommendation phase does not satisfy this phase. If T-01 fires, add an Amendment Row citing T-01.

```
SCOUT ARTIFACT INVENTORY
FOUND:
  - [artifact name / key finding — specific, not generic]
ABSENT:
  - [type not found — state explicitly]
INLINE ASSESSMENT (if all absent):
  [PM: market context and stakeholder landscape]
  [Architect: technical feasibility and constraint assessment]
```

---

### PHASE 2 — DECISION FRAMING

TEMPORAL ANCHOR and INACTION CONSEQUENCE are independent typed fields. A combined WHY NOW field satisfies C-04 but not C-13. Both fields must appear before Phase 4. If T-03 fires, add an Amendment Row citing T-03.

```
DECISION QUESTION:    [the specific question being decided — one sentence]
TEMPORAL ANCHOR:      [specific named date, sprint name, or named event]
                      PROHIBITED: "soon" / "before it is too late" / "in the near term" / any language
                      without a named deadline — vague language causes T-03 to fire
INACTION CONSEQUENCE: [concrete named outcome — teams blocked, capability lost, or window closed]
                      PROHIBITED: missed-feature statements — a feature statement does not name
                      the consequence of not deciding
STAKES:               [PM: business impact | Architect: technical impact]
```

---

### PHASE 3 — PROJECT-SPECIFIC SCORING ANCHORS

Define project-specific anchors before computing any risk scores or INERTIA COST values. These anchors are the reference frame for all R-NN entries in Phase 8 and for INERTIA COST in Phase 4.

```
RISK SCORING ANCHORS — [project name]
PROBABILITY:  P=1 [project-specific anchor — what "rare" means in this context]
              P=3 [project-specific anchor — what "plausible" means in this context]
              P=5 [project-specific anchor — what "expected" means in this context]
IMPACT:       I=1 [project-specific anchor — what "negligible" means in this context]
              I=3 [project-specific anchor — what "moderate disruption" means in this context]
              I=5 [project-specific anchor — what "blocking" means in this context]
```

Holistic L/M/H labels are prohibited throughout this document.

---

### PHASE 4 — OPTION 0: DO-NOTHING / STATUS QUO (THE INCUMBENT COMPETITOR)

Do-nothing is not a neutral baseline — it is the incumbent competitor with a computable per-sprint cost. INERTIA COST quantifies what every sprint of deferral costs in Phase 3 terms. PM names the business accumulation; Architect names the technical accumulation.

```
OPTION 0: [Name — treat as "the option that wins if nothing is decided"]
DESCRIPTION:    [PM: what business status quo entails]
                [Architect: what technical steady-state entails — what accumulates each sprint]
PROS:           [what status quo preserves — be specific]
CONS:           [what accumulates or degrades — list each item]
RISK:           P: [N] x I: [N] = P*I: [N] — [primary risk; use Phase 3 anchors]
EFFORT:         TIMELINE: [ongoing] | TEAM: [maintenance burden] | DEPENDENCIES: [what continues]
INERTIA COST:   P: [N] x I: [N] = P*I: [N] per sprint
                PM accumulation:       [named business cost per sprint — competitive gap, revenue exposure, adoption window shrinkage]
                Architect accumulation: [named technical cost per sprint — debt added, coupling tightened, migration cost increased]
```

INERTIA COST uses Phase 3 anchors. If T-07 fires (INERTIA COST absent), add an Amendment Row citing T-07.

---

### PHASE 5 — OPTIONS 1 THROUGH N (ALTERNATIVES THAT MUST BEAT OPTION 0)

Each alternative must justify its existence against the Option 0 inertia curve. INERTIA OFFSET is the answer to: "at what sprint does acting become cheaper than continuing to pay INERTIA COST?" PM frames adoption path; Architect frames technical implementation. Minimum 2 alternatives. If T-02 fires, add an Amendment Row. If T-08 fires, add an Amendment Row.

```
OPTION [N]: [Name]
DESCRIPTION:      [Architect: technical approach and constraints]
                  [PM: adoption path and business framing]
PROS:             [list — include how this beats Option 0's inertia curve]
CONS:             [list — include upfront cost that delays break-even]
RISK:             P: [N] x I: [N] = P*I: [N] — [description; use Phase 3 anchors]
EFFORT:           TIMELINE: [N sprints] | TEAM: [roles required] | DEPENDENCIES: [external requirements]
INERTIA OFFSET:   Sprint [N] — the sprint at which cumulative implementation cost equals cumulative
                  INERTIA COST of Option 0. The decision imperative: act before sprint [N] or pay
                  P: [N] x I: [N] = P*I: [N] per sprint thereafter.
```

---

### PHASE 6 — STRUCTURED COMPARISON TABLE

All options on consistent dimensions. INERTIA OFFSET is a required comparison dimension, making the break-even analysis machine-checkable across options.

| Dimension | Option 0 | Option 1 | Option 2 | Option N |
|-----------|----------|----------|----------|----------|
| Effort (sprints) | ongoing | | | |
| Risk P*I | | | | |
| Team control | | | | |
| Adoption friction | | | | |
| Time to value | — | | | |
| Inertia offset (sprint crossover) | — (baseline, P*I/sprint) | Sprint N | Sprint N | Sprint N |

**PM perspective:** [which dimensions and inertia analysis drive the PM's recommendation — 2–3 sentences]
**Architect perspective:** [which dimensions and inertia analysis drive the Architect's recommendation — 2–3 sentences]

---

### PHASE 7 — ASSUMPTION REGISTER

```
ASSUMPTION REGISTER
| ID   | Assumption | Validation Plan | Owner |
|------|-----------|-----------------|-------|
| A-01 | [text]    | [specific action — not just "monitor"] | [role] |
| A-02 | [text]    | [validation plan] | [role] |
```

Minimum 2 entries. Validation plans are required — "monitor" or "observe" do not satisfy. If T-04 fires, add an Amendment Row citing T-04.

---

### PHASE 8 — RISK REGISTER

Phase 3 anchors apply. Holistic L/M/H labels are prohibited. Separate numeric P, I, and computed P*I required on every entry.

```
RISK REGISTER
| ID   | Risk | P | I | P*I | Option | Mitigation |
|------|------|---|---|-----|--------|------------|
| R-01 | [text] | [1–5] | [1–5] | [P*I] | [option affected] | [mitigation] |
| R-02 | [text] | [1–5] | [1–5] | [P*I] | [option affected] | [mitigation] |
```

Minimum 2 entries. If T-04 fires, add an Amendment Row citing T-04.

---

### PHASE 9 — FAILURE MODE REGISTER

Use exact column headers. Synonym substitution causes C-19 to fail — a reviewer cannot confirm alignment without inference.

```
FAILURE MODE REGISTER
| ID   | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|------------------|------------|
| F-01 | [text]      | [text]            | [text]     |
| F-02 | [text]      | [text]            | [text]     |
```

PROHIBITED: "Observable Event" for TRIGGER CONDITION. PROHIBITED: "Fallback" or "Response" for MITIGATION. PROHIBITED: "Failure Scenario" or "Risk Event" for FAILURE MODE. Minimum 2 entries.

---

### PHASE 10 — PREREQUISITE GATE

This block appears before Phase 11. A reviewer confirms C-17 and C-20 compliance by reading this single block. GATE STATUS must be PASS before proceeding.

```
PREREQUISITE GATE — [project name]
[ ] ASSUMPTION REGISTER: [N] A-NN entries with validation plans [complete / not complete]
[ ] RISK REGISTER: [N] R-NN entries with numeric P, I, P*I [complete / not complete]
[ ] FAILURE MODE REGISTER: [N] F-NN entries with exact canonical labels [complete / not complete]
[ ] ASSUMPTION REGISTER precedes RECOMMENDATION in document sequence [complete / not complete]
[ ] RISK REGISTER precedes RECOMMENDATION in document sequence [complete / not complete]
[ ] INERTIA COST present on Option 0 with numeric P*I per sprint stated [complete / not complete]
[ ] At least one alternative carries INERTIA OFFSET sprint crossover value [complete / not complete]

GATE STATUS: [PASS / FAIL — FAIL means Phase 11 cannot proceed; resolve failing items first]
```

---

### PHASE 11 — RECOMMENDATION

Dual-signatory sign-off. PM and Architect sign independently. F-ROW ANCHOR is a mandatory typed slot in both blocks. Neither block can be completed without naming an F-row. The two anchors may reference the same or different F-rows — structural independence, not divergence, is the requirement. If T-05 fires on either block, add an Amendment Row citing T-05.

```
RECOMMENDATION: Option [N] — [Name]
RATIONALE:  [why this option wins over alternatives — reference at least one scout artifact finding
             and at least one R-NN entry; state the sprint at which Option 0's INERTIA COST
             makes this option the cheaper choice]
CONDITIONS:
  1. [qualifying condition — specific and verifiable, not vague]
  2. [qualifying condition]
  3. [qualifying condition — minimum 3]

PM SIGN-OFF
  PERSPECTIVE:  [PM business rationale — adoption timing, competitive window, cost trade-offs]
  F-ROW ANCHOR: F-[NN] — [the F-row whose TRIGGER CONDITION most directly invalidates this sign-off if it fires]
  CONDITIONS:   [PM-specific qualifying conditions]
  STATUS:       [APPROVED / CONTINGENT]

ARCHITECT SIGN-OFF
  PERSPECTIVE:  [Architect technical rationale — feasibility, integration, inertia offset justification]
  F-ROW ANCHOR: F-[NN] — [the F-row whose TRIGGER CONDITION most directly invalidates this sign-off if it fires]
  CONDITIONS:   [Architect-specific qualifying conditions]
  STATUS:       [APPROVED / CONTINGENT]
```

---

### PHASE 12 — AMEND PHASE

Three categories required. OWNER and DEADLINE are typed slots in ALL THREE templates — not only in FOLLOW-UP. DEADLINE values must be specific (sprint name, named date, or milestone) — "TBD" and blank fail.

**MISSING OPTION** (at least 1 entry)
```
AMEND-MO-NN: [option not explored in this proposal]
RATIONALE:   [why it warrants exploration — include inertia-curve implications if relevant]
OWNER:       [role responsible for exploring this option]
DEADLINE:    [specific sprint name / named date / named milestone]
```

**UNWEIGHTED CRITERION** (at least 1 entry)
```
AMEND-UC-NN: [decision criterion currently unweighted or equally-weighted across options]
RECALIBRATION: [how the weighting should change and why — reference comparison dimensions]
OWNER:       [role responsible for recalibration]
DEADLINE:    [specific sprint name / named date / named milestone]
```

**FOLLOW-UP** (at least 1 entry)
```
AMEND-FU-NN: [follow-up action required after this proposal is accepted]
ACTION:      [specific action — not a re-statement of the option]
OWNER:       [role responsible for execution]
DEADLINE:    [specific sprint name / named date / named milestone]
```

---

### PHASE 13 — COMPLETION STATUS

Review Phase 0 Amendment Rows. Every row must be addressed or escalated before the document is complete.

Update COMPLETION STATUS in Phase 0 from PENDING to the vocabulary-constrained terminal value defined at initialization:

- If Amendment Rows is empty: "T-GUARD enforced all requirements successfully — no violations detected."
- If Amendment Rows contains rows: "Amendment rows populated; see rows above."

The COMPLETION STATUS slot was defined at Phase 0 initialization as a live mandatory field. Updating it here is completing the field, not appending a new instruction.

---
**Predicted score:** All 27 criteria pass. C-25: T-GUARD at position 1 in trigger table. C-26: COMPLETION STATUS typed slot with PENDING initial value in Phase 0; vocabulary-constrained terminal values defined at initialization. C-27: INERTIA COST on Option 0; INERTIA OFFSET on every alternative; PREREQUISITE GATE includes two inertia-axis binary items. Composite: 60 + 30 + (20/20 × 10) = **100.00**.

---

## Summary

| Variation | Axis | Designed Fail | Predicted Score |
|-----------|------|---------------|-----------------|
| V-01 | Lifecycle emphasis | C-25 (T-GUARD last in trigger table) | 99.50 |
| V-02 | Phrasing register (formal/technical) | C-26 (no COMPLETION STATUS Phase 0 slot) | 99.50 |
| V-03 | Role sequence (Architect-first) | C-27 (no INERTIA COST/OFFSET) | 99.50 |
| V-04 | PM-first + table-dominant format | None | 100.00 |
| V-05 | Full ceiling integration (all axes) | None | 100.00 |

**C-25, C-26, C-27 structural decoupling:** V-01 nails C-26 and C-27 but fails C-25 (T-GUARD at wrong position). V-02 nails C-25 and C-27 but fails C-26 (no initialization slot). V-03 nails C-25 and C-26 but fails C-27 (no inertia fields). The three new criteria are independently satisfiable — satisfying any two does not satisfy the third.

**V-05 ceiling pattern:** Sentinel-first position shifts enforcement direction (unenumerated gaps caught before named triggers). COMPLETION STATUS as Phase 0 typed slot converts completion semantics from a Phase 13 instruction (skippable) to a mandatory live field from creation (not skippable). Inertia-forward framing converts do-nothing from a descriptive baseline into a computable cost curve that every alternative must justify crossing.
