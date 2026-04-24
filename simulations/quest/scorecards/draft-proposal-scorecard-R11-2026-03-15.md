# draft-proposal Scorecard — Round 11

**Rubric version**: v11 · **Denominator**: /30 aspirational · **Date**: 2026-03-15
**New criteria**: C-36 (PREREQUISITE GATE anatomy contract binary), C-37 (dual-contract co-presence)

---

## Prediction Calibration Note

The per-variation hypotheses (V-01: "27/30 → 99.00") conflict with the round summary
("V-01 → 99.33"). The detailed hypotheses are authoritative: V-01 and V-02 are each
designed to fail **3 aspirational criteria** (27/30 = 9.00 pts), not 2. The 99.33 figure
corresponds to 28/30 = 9.33 pts and is a carry-over error from a prior draft of the
prediction table. Scores below reflect the correct 3-failure counts for V-01 and V-02.

---

## Variation Scorecards

### V-01 — Architect-First | Axis: Role Sequence | Designed fail: C-34, C-36, C-37

**Hypothesis**: Phase 0 CAUSAL CHAIN CONTRACT declared; gate holds causal chain binary;
PM FRAMING: is the first typed field in every option entry. No Phase 0 OPTION ANATOMY
CONTRACT. Gate holds no anatomy contract binary. Fails C-34 (no anatomy contract), C-36
(no anatomy gate binary), C-37 (only one gate binary). PM sign-off first (C-28 PASS).
T-GUARD listed first in amendment table (C-25 PASS).

| ID | Category | Result | Evidence |
|----|----------|--------|----------|
| C-01 | Essential | PASS | Three or more labeled options including do-nothing; option template present |
| C-02 | Essential | PASS | All anatomy fields present per option: PM FRAMING, ARCHITECT VALIDATION, PROS, CONS, RISK, EFFORT, RATIONALE |
| C-03 | Essential | PASS | Phase 11 recommendation with rationale and qualifying conditions |
| C-04 | Essential | PASS | PROBLEM + TEMPORAL ANCHOR + INACTION CONSEQUENCE + DECISION REQUIRED appear before options |
| C-05 | Recommended | PASS | Phase 2 SCOUT INVENTORY is a dedicated step listing found/absent artifacts |
| C-06 | Recommended | PASS | Architect leads option framing and gate audit; PM leads business framing and amend phase |
| C-07 | Recommended | PASS | Phase 7 COMPARISON MATRIX with typed dimensions across all options |
| C-08 | Aspirational | PASS | Phase 4 assumption register (A-NN + VALIDATION PLAN); Phase 5 risk register (R-NN + P×I) |
| C-09 | Aspirational | PASS | Phase 8 AMEND PHASE self-audit with three categories |
| C-10 | Aspirational | PASS | Phase 2 is a discrete scout inventory step before option generation |
| C-11 | Aspirational | PASS | Three amend categories (missing option, unweighted criterion, follow-up) with OWNER per entry |
| C-12 | Aspirational | PASS | OWNER typed slot in amend template for all three category types |
| C-13 | Aspirational | PASS | TEMPORAL ANCHOR and INACTION CONSEQUENCE as separate typed fields; vague language prohibited |
| C-14 | Aspirational | PASS | DEADLINE typed slot in amend template for all three category types |
| C-15 | Aspirational | PASS | Phase 6 failure mode register (F-NN); recommendation CONDITIONS reference F-row by ID |
| C-16 | Aspirational | PASS | Phase 5 P=1..5 and I=1..5 project-specific anchors defined; P×I compound score per entry |
| C-17 | Aspirational | PASS | Phases 4, 5, 6 precede Phase 11 in phase manifest and document sequence |
| C-18 | Aspirational | PASS | Amendment tracking table initialized at Phase 0 with T-GUARD and T-01..T-37 trigger rows |
| C-19 | Aspirational | PASS | Phase 6 uses FAILURE MODE / TRIGGER CONDITION / MITIGATION as exact column headers |
| C-20 | Aspirational | PASS | Phase 10 PREREQUISITE GATE block with named binary items confirming register completion |
| C-21 | Aspirational | PASS | PM and Architect sign-off blocks each carry independent F-ROW ANCHOR typed slot |
| C-22 | Aspirational | PASS | T-GUARD and T-01..T-37 have stable named IDs; amendment rows cite source trigger ID |
| C-23 | Aspirational | PASS | T-GUARD defined at Phase 0 initialization with catch-all scope vocabulary |
| C-24 | Aspirational | PASS | COMPLETION STATUS updated at document completion with explicit enforcement declaration |
| C-25 | Aspirational | PASS | T-GUARD listed as first entry in trigger table before T-01..T-37 |
| C-26 | Aspirational | PASS | COMPLETION STATUS typed slot initialized at Phase 0 with "PENDING" value |
| C-27 | Aspirational | PASS | Do-nothing carries numeric INERTIA COST (P×I); alternatives carry INERTIA OFFSET |
| C-28 | Aspirational | PASS | PM sign-off block is first signatory in Phase 11; Architect block follows |
| C-29 | Aspirational | PASS | All three registers use structured table format with typed column headers |
| C-30 | Aspirational | PASS | PHASE MANIFEST block lists all 12 phases by number and name at Phase 0 |
| C-31 | Aspirational | PASS | Phase 9 computes DECISION LEAD TIME per alternative; ESCALATION FLAG on non-positive result |
| C-32 | Aspirational | PASS | PM FRAMING: is the first typed field in the option anatomy template; ARCHITECT VALIDATION: is second |
| C-33 | Aspirational | PASS | Phase 0 CAUSAL CHAIN CONTRACT declares formula, source attribution, and T-GUARD routing rule |
| C-34 | Aspirational | **FAIL** | No Phase 0 OPTION ANATOMY CONTRACT block; anatomy slots embedded in template without prospective contract |
| C-35 | Aspirational | PASS | Gate includes binary for Phase 0 causal chain contract presence and completeness |
| C-36 | Aspirational | **FAIL** | C-34 fails → no anatomy contract to verify → gate holds no anatomy contract binary |
| C-37 | Aspirational | **FAIL** | Gate holds one Phase 0 contract binary (causal); anatomy binary absent → not dual-contract |

**Essential**: 4/4 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 27/30

```
composite = (4/4 × 60) + (3/3 × 30) + (27/30 × 10)
          = 60.00 + 30.00 + 9.00
          = 99.00
```

**Band**: Golden (all essential pass; composite ≥ 80) · **Score**: **99.00**

---

### V-02 — Compact Tables, PM-First | Axis: Output Format | Designed fail: C-33, C-35, C-37

**Hypothesis**: PM-first role sequence throughout. Phase 0 OPTION ANATOMY CONTRACT
declared with PM FRAMING: first, ARCHITECT VALIDATION: second, named T-NN trigger
(C-34 PASS, C-36 PASS). No Phase 0 CAUSAL CHAIN CONTRACT (C-33 FAIL). Gate holds
no causal chain binary (C-35 FAIL). Gate holds one Phase 0 contract binary (anatomy
only) — asymmetric auditability → C-37 FAIL.

| ID | Category | Result | Evidence |
|----|----------|--------|----------|
| C-01 | Essential | PASS | Three or more labeled options including do-nothing; compact table anatomy present |
| C-02 | Essential | PASS | All anatomy fields present per option; compact format preserves required slots |
| C-03 | Essential | PASS | Phase 11 recommendation with rationale and qualifying conditions |
| C-04 | Essential | PASS | Decision framing with typed fields before option generation |
| C-05 | Recommended | PASS | Dedicated scout inventory step listing found/absent artifacts |
| C-06 | Recommended | PASS | PM leads business framing and option anatomy; Architect validates technical constraints |
| C-07 | Recommended | PASS | Comparison matrix with typed dimensions across all options |
| C-08 | Aspirational | PASS | Assumption register (A-NN) and risk register (R-NN) with P×I |
| C-09 | Aspirational | PASS | Amend phase self-audit with at least one actionable item |
| C-10 | Aspirational | PASS | Discrete scout inventory step before option generation |
| C-11 | Aspirational | PASS | Three amend categories with OWNER in format template |
| C-12 | Aspirational | PASS | OWNER typed slot in all three amend category templates |
| C-13 | Aspirational | PASS | TEMPORAL ANCHOR and INACTION CONSEQUENCE as separate typed fields |
| C-14 | Aspirational | PASS | DEADLINE typed slot in all three amend category templates |
| C-15 | Aspirational | PASS | Failure mode register with F-ROW reference in sign-off CONDITIONS |
| C-16 | Aspirational | PASS | Project-specific P=1..5, I=1..5 anchors defined; P×I per risk entry |
| C-17 | Aspirational | PASS | Registers precede recommendation in phase sequence |
| C-18 | Aspirational | PASS | Amendment table initialized at Phase 0 with trigger IDs and T-GUARD |
| C-19 | Aspirational | PASS | FAILURE MODE / TRIGGER CONDITION / MITIGATION as exact column headers |
| C-20 | Aspirational | PASS | PREREQUISITE GATE block immediately before recommendation |
| C-21 | Aspirational | PASS | PM and Architect sign-off blocks each carry independent F-ROW ANCHOR slot |
| C-22 | Aspirational | PASS | Stable trigger IDs; amendment rows cite source trigger ID |
| C-23 | Aspirational | PASS | T-GUARD defined at initialization with catch-all scope |
| C-24 | Aspirational | PASS | Explicit completion-state declaration at document completion |
| C-25 | Aspirational | PASS | T-GUARD listed first in trigger table |
| C-26 | Aspirational | PASS | COMPLETION STATUS typed slot initialized at Phase 0 |
| C-27 | Aspirational | PASS | Do-nothing INERTIA COST (P×I); alternatives INERTIA OFFSET sprint crossover |
| C-28 | Aspirational | PASS | PM sign-off block is first signatory |
| C-29 | Aspirational | PASS | All three registers use structured table format |
| C-30 | Aspirational | PASS | Phase manifest at Phase 0 listing all phases |
| C-31 | Aspirational | PASS | DECISION LEAD TIME computed per alternative; ESCALATION FLAG where non-positive |
| C-32 | Aspirational | PASS | PM FRAMING: first typed field in option anatomy; ARCHITECT VALIDATION: second |
| C-33 | Aspirational | **FAIL** | No Phase 0 CAUSAL CHAIN CONTRACT block; formula not declared prospectively |
| C-34 | Aspirational | PASS | Phase 0 OPTION ANATOMY CONTRACT with PM FRAMING: first, ARCHITECT VALIDATION: second, named trigger |
| C-35 | Aspirational | **FAIL** | C-33 fails → no causal contract to verify → gate holds no causal chain binary |
| C-36 | Aspirational | PASS | Gate includes binary for Phase 0 option anatomy contract presence and completeness |
| C-37 | Aspirational | **FAIL** | Gate holds one Phase 0 contract binary (anatomy); causal binary absent → not dual-contract |

**Essential**: 4/4 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 27/30

```
composite = (4/4 × 60) + (3/3 × 30) + (27/30 × 10)
          = 60.00 + 30.00 + 9.00
          = 99.00
```

**Band**: Golden · **Score**: **99.00**

---

### V-03 — Split-Gate | Axis: Lifecycle Emphasis | Designed fail: C-37 alone

**Hypothesis**: Both Phase 0 contracts declared (C-33 PASS, C-34 PASS). PREREQUISITE
GATE contains two lifecycle-oriented sub-sections: sub-section A holds the causal chain
contract binary (C-35 PASS); sub-section B holds the anatomy contract binary (C-36 PASS).
The binaries exist within the gate block but are separated by sub-section structure.
C-37 requires co-presence — both binaries in the same undivided gate block. Sub-section
separation breaks co-presence → C-37 FAIL. Single failure.

| ID | Category | Result | Evidence |
|----|----------|--------|----------|
| C-01 | Essential | PASS | Three or more labeled options including do-nothing |
| C-02 | Essential | PASS | All anatomy fields present per option |
| C-03 | Essential | PASS | Recommendation with rationale and qualifying conditions |
| C-04 | Essential | PASS | Decision framing with typed fields before options |
| C-05 | Recommended | PASS | Dedicated scout inventory step |
| C-06 | Recommended | PASS | Dual-role participation with distinct named perspectives |
| C-07 | Recommended | PASS | Comparison matrix with consistent dimensions |
| C-08 | Aspirational | PASS | Assumption and risk registers with required entries |
| C-09 | Aspirational | PASS | Amend phase with at least one actionable item |
| C-10 | Aspirational | PASS | Discrete scout inventory step |
| C-11 | Aspirational | PASS | Three amend categories with OWNER |
| C-12 | Aspirational | PASS | OWNER typed slot in all three amend templates |
| C-13 | Aspirational | PASS | Split TEMPORAL ANCHOR + INACTION CONSEQUENCE fields |
| C-14 | Aspirational | PASS | DEADLINE typed slot in all three amend templates |
| C-15 | Aspirational | PASS | F-row register with F-ROW reference in sign-off CONDITIONS |
| C-16 | Aspirational | PASS | Project-specific scoring anchors; numeric P×I per entry |
| C-17 | Aspirational | PASS | Registers precede recommendation |
| C-18 | Aspirational | PASS | Amendment table initialized at Phase 0 |
| C-19 | Aspirational | PASS | Canonical F-row column labels |
| C-20 | Aspirational | PASS | PREREQUISITE GATE block present before recommendation |
| C-21 | Aspirational | PASS | Independent F-ROW ANCHOR slot in PM and Architect sign-off blocks |
| C-22 | Aspirational | PASS | Stable T-NN IDs; amendment rows cite trigger ID |
| C-23 | Aspirational | PASS | T-GUARD with catch-all scope at initialization |
| C-24 | Aspirational | PASS | Explicit completion-state declaration |
| C-25 | Aspirational | PASS | T-GUARD listed first in trigger table |
| C-26 | Aspirational | PASS | COMPLETION STATUS typed slot at Phase 0 |
| C-27 | Aspirational | PASS | INERTIA COST on do-nothing; INERTIA OFFSET on alternatives |
| C-28 | Aspirational | PASS | PM sign-off first in recommendation |
| C-29 | Aspirational | PASS | All three registers in table format |
| C-30 | Aspirational | PASS | Phase manifest at Phase 0 |
| C-31 | Aspirational | PASS | DECISION LEAD TIME computed per alternative |
| C-32 | Aspirational | PASS | PM FRAMING: first typed field in option anatomy |
| C-33 | Aspirational | PASS | Phase 0 CAUSAL CHAIN CONTRACT with formula, source attribution, T-GUARD routing rule |
| C-34 | Aspirational | PASS | Phase 0 OPTION ANATOMY CONTRACT with PM FRAMING: first, ARCHITECT VALIDATION: second, named trigger |
| C-35 | Aspirational | PASS | Causal chain contract binary present in gate sub-section A |
| C-36 | Aspirational | PASS | Anatomy contract binary present in gate sub-section B |
| C-37 | Aspirational | **FAIL** | Binaries exist in separate lifecycle sub-sections within gate; not co-present in same undivided gate block |

**Essential**: 4/4 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 29/30

```
composite = (4/4 × 60) + (3/3 × 30) + (29/30 × 10)
          = 60.00 + 30.00 + 9.67
          = 99.67
```

**Band**: Golden · **Score**: **99.67**

---

### V-04 — Conversational Register | Axis: Phrasing Register | Designed fail: C-25 alone

**Hypothesis**: All C-33, C-34, C-35, C-36, C-37 pass — both Phase 0 contracts declared
and both gate binaries co-present. T-GUARD defined with correct catch-all scope (C-23
PASS) but appears as the last entry in the trigger table, after T-01 through T-37.
Conversational phrasing does not affect any structural criterion. Single failure: C-25
(T-GUARD not first).

| ID | Category | Result | Evidence |
|----|----------|--------|----------|
| C-01 | Essential | PASS | Three or more labeled options including do-nothing |
| C-02 | Essential | PASS | All anatomy fields present per option |
| C-03 | Essential | PASS | Recommendation with rationale and qualifying conditions |
| C-04 | Essential | PASS | Decision framing with typed fields before options |
| C-05 | Recommended | PASS | Dedicated scout inventory step |
| C-06 | Recommended | PASS | Dual-role participation with distinct named perspectives |
| C-07 | Recommended | PASS | Comparison matrix with consistent dimensions |
| C-08 | Aspirational | PASS | Assumption and risk registers |
| C-09 | Aspirational | PASS | Amend phase with at least one actionable item |
| C-10 | Aspirational | PASS | Discrete scout inventory step |
| C-11 | Aspirational | PASS | Three amend categories with OWNER |
| C-12 | Aspirational | PASS | OWNER typed slot in all three amend templates |
| C-13 | Aspirational | PASS | Split TEMPORAL ANCHOR + INACTION CONSEQUENCE fields |
| C-14 | Aspirational | PASS | DEADLINE typed slot in all three amend templates |
| C-15 | Aspirational | PASS | F-row register with F-ROW reference in sign-off CONDITIONS |
| C-16 | Aspirational | PASS | Project-specific anchors; numeric P×I per entry |
| C-17 | Aspirational | PASS | Registers precede recommendation |
| C-18 | Aspirational | PASS | Amendment table initialized at Phase 0 |
| C-19 | Aspirational | PASS | Canonical F-row column labels |
| C-20 | Aspirational | PASS | PREREQUISITE GATE block present |
| C-21 | Aspirational | PASS | Independent F-ROW ANCHOR slot in both sign-off blocks |
| C-22 | Aspirational | PASS | Stable T-NN IDs; amendment rows cite trigger ID |
| C-23 | Aspirational | PASS | T-GUARD defined at initialization with correct scope vocabulary |
| C-24 | Aspirational | PASS | Explicit completion-state declaration |
| C-25 | Aspirational | **FAIL** | T-GUARD listed last (after T-01..T-37); enforcement direction is backstop not frontline |
| C-26 | Aspirational | PASS | COMPLETION STATUS typed slot at Phase 0 |
| C-27 | Aspirational | PASS | INERTIA COST on do-nothing; INERTIA OFFSET on alternatives |
| C-28 | Aspirational | PASS | PM sign-off first in recommendation |
| C-29 | Aspirational | PASS | All three registers in table format |
| C-30 | Aspirational | PASS | Phase manifest at Phase 0 |
| C-31 | Aspirational | PASS | DECISION LEAD TIME computed per alternative |
| C-32 | Aspirational | PASS | PM FRAMING: first typed field in option anatomy |
| C-33 | Aspirational | PASS | Phase 0 CAUSAL CHAIN CONTRACT with formula, source attribution, T-GUARD routing rule |
| C-34 | Aspirational | PASS | Phase 0 OPTION ANATOMY CONTRACT with PM FRAMING: first, ARCHITECT VALIDATION: second, named trigger |
| C-35 | Aspirational | PASS | Causal chain contract binary in gate |
| C-36 | Aspirational | PASS | Anatomy contract binary in gate |
| C-37 | Aspirational | PASS | Both Phase 0 contract binaries co-present in same gate block |

**Essential**: 4/4 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 29/30

```
composite = (4/4 × 60) + (3/3 × 30) + (29/30 × 10)
          = 60.00 + 30.00 + 9.67
          = 99.67
```

**Band**: Golden · **Score**: **99.67**

---

### V-05 — Inertia Framing + Motivated | Axis: Inertia Narrative | Designed pass: C-28–C-37 all pass

**Hypothesis**: All ten v8–v11 aspirational criteria pass. Both Phase 0 contracts
(C-33, C-34) declared; both gate binaries co-present in a single gate block (C-35,
C-36, C-37). T-GUARD listed first (C-25). Inertia-first framing makes the TEMPORAL
ANCHOR − INERTIA OFFSET = DECISION LEAD TIME contract feel earned by narrative
rather than mechanical. PM-first sign-off (C-28). All C-08–C-27 pass from cumulative
prior rounds.

| ID | Category | Result | Evidence |
|----|----------|--------|----------|
| C-01 | Essential | PASS | Three or more labeled options including do-nothing |
| C-02 | Essential | PASS | All anatomy fields present per option |
| C-03 | Essential | PASS | Recommendation with rationale and qualifying conditions |
| C-04 | Essential | PASS | Decision framing with typed fields before options |
| C-05 | Recommended | PASS | Dedicated scout inventory step |
| C-06 | Recommended | PASS | Dual-role participation with distinct named perspectives |
| C-07 | Recommended | PASS | Comparison matrix with consistent dimensions |
| C-08 | Aspirational | PASS | Assumption and risk registers with required entries |
| C-09 | Aspirational | PASS | Amend phase with at least one actionable item |
| C-10 | Aspirational | PASS | Discrete scout inventory step |
| C-11 | Aspirational | PASS | Three amend categories with OWNER |
| C-12 | Aspirational | PASS | OWNER typed slot in all three amend templates |
| C-13 | Aspirational | PASS | Split TEMPORAL ANCHOR + INACTION CONSEQUENCE fields |
| C-14 | Aspirational | PASS | DEADLINE typed slot in all three amend templates |
| C-15 | Aspirational | PASS | F-row register with F-ROW reference in sign-off CONDITIONS |
| C-16 | Aspirational | PASS | Project-specific anchors; numeric P×I per entry |
| C-17 | Aspirational | PASS | Registers precede recommendation |
| C-18 | Aspirational | PASS | Amendment table initialized at Phase 0 |
| C-19 | Aspirational | PASS | Canonical F-row column labels |
| C-20 | Aspirational | PASS | PREREQUISITE GATE block present |
| C-21 | Aspirational | PASS | Independent F-ROW ANCHOR slot in both sign-off blocks |
| C-22 | Aspirational | PASS | Stable T-NN IDs; amendment rows cite trigger ID |
| C-23 | Aspirational | PASS | T-GUARD with catch-all scope at initialization |
| C-24 | Aspirational | PASS | Explicit completion-state declaration |
| C-25 | Aspirational | PASS | T-GUARD listed first in trigger table |
| C-26 | Aspirational | PASS | COMPLETION STATUS typed slot at Phase 0 |
| C-27 | Aspirational | PASS | INERTIA COST on do-nothing; INERTIA OFFSET on alternatives |
| C-28 | Aspirational | PASS | PM sign-off first in recommendation |
| C-29 | Aspirational | PASS | All three registers in table format |
| C-30 | Aspirational | PASS | Phase manifest at Phase 0 |
| C-31 | Aspirational | PASS | DECISION LEAD TIME computed per alternative |
| C-32 | Aspirational | PASS | PM FRAMING: first typed field in option anatomy |
| C-33 | Aspirational | PASS | Phase 0 CAUSAL CHAIN CONTRACT with formula, source attribution, T-GUARD routing rule |
| C-34 | Aspirational | PASS | Phase 0 OPTION ANATOMY CONTRACT with PM FRAMING: first, ARCHITECT VALIDATION: second, named trigger |
| C-35 | Aspirational | PASS | Causal chain contract binary in gate |
| C-36 | Aspirational | PASS | Anatomy contract binary in gate |
| C-37 | Aspirational | PASS | Both Phase 0 contract binaries co-present in same undivided gate block |

**Essential**: 4/4 PASS · **Recommended**: 3/3 PASS · **Aspirational**: 30/30

```
composite = (4/4 × 60) + (3/3 × 30) + (30/30 × 10)
          = 60.00 + 30.00 + 10.00
          = 100.00
```

**Band**: Golden · **Score**: **100.00**

---

## Round Summary

| Rank | Variation | Axis | Designed Fails | Aspirational | Composite | Band |
|------|-----------|------|----------------|--------------|-----------|------|
| 1 | V-05 | Inertia framing + motivated | none | 30/30 | 100.00 | Golden |
| 2 | V-03 | Split-gate lifecycle | C-37 | 29/30 | 99.67 | Golden |
| 2 | V-04 | Conversational register | C-25 | 29/30 | 99.67 | Golden |
| 4 | V-01 | Architect-first role sequence | C-34, C-36, C-37 | 27/30 | 99.00 | Golden |
| 4 | V-02 | Compact tables, PM-first | C-33, C-35, C-37 | 27/30 | 99.00 | Golden |

All five variations Golden. **All essential criteria pass across all variations.**

---

## Discrimination Analysis

**C-37 appears in 3 of 5 failure sets (V-01, V-02, V-03)** — it is the R11
discriminator. This is expected: C-37 requires the conjunction of C-35 and C-36, so
any variation that supplies only one Phase 0 contract also supplies only one gate
binary and automatically fails C-37.

**Asymmetric cascade pattern confirmed:**
- V-01 (anatomy absent): C-34 FAIL → C-36 FAIL → C-37 FAIL (3 cascading failures on
  the anatomy axis)
- V-02 (causal absent): C-33 FAIL → C-35 FAIL → C-37 FAIL (3 cascading failures on
  the causal axis)
- V-03 (split-gate): C-35 PASS, C-36 PASS → C-37 FAIL (co-presence violation without
  cascade; the cleanest single-axis C-37 failure)

**V-03 is the structurally interesting failure.** V-01 and V-02 fail C-37 because a
required Phase 0 contract is absent. V-03 has BOTH contracts AND both gate binaries —
it fails C-37 only because the binaries are in separate lifecycle sub-sections rather
than co-present. This is a subtle distinction: a reviewer can confirm each binary
individually (C-35 PASS, C-36 PASS) but cannot confirm dual-contract coverage from a
single block read (C-37 FAIL). The split-gate pattern is the purest illustration of why
C-37 is an independent criterion rather than a derivative of C-35 + C-36.

**V-04 confirms register orthogonality.** Conversational phrasing affects zero
structural criteria. C-25 fails purely from trigger table ordering, not from phrasing.
Register choice is orthogonal to structural completeness — the R2 finding holds through
R11.

**Prediction table error.** The per-variation hypotheses correctly predict 99.00 for
V-01 and V-02 (3 failures → 27/30). The round summary prediction of "99.33" for V-01
and V-02 is incorrect; 99.33 corresponds to 28/30 (2 failures). The discrepancy is a
carry-over from a prior draft before the V-01/V-02 designs settled on 3-failure counts.
My scores use the per-variation hypotheses as the authoritative prediction source.

---

## Excellence Signals from V-05

**1. Dual-contract gate completeness (C-37 pattern).**
Declaring both Phase 0 contracts AND placing both gate binaries in the same undivided
gate block creates what might be called the "minimal-scroll auditability model." A
reviewer can confirm both initialization contracts — causal chain and option anatomy —
with two single-block reads (Phase 0 and Phase 10) and zero cross-document navigation.
The improvement from V-03 to V-05 is purely structural: same content, different gate
layout, one more criterion satisfied.

**2. Inertia-first narrative coherence.**
When INERTIA COST/OFFSET is the organizing frame of the document, the Phase 0 causal
chain contract reads as a natural declaration of the document's decision logic:
TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME is earned by the inertia
framing setup. Contrast with variations where the contract appears as a mechanical
initialization checklist item. The formula is the same; the document's internal
motivation differs. Narrative coherence does not score against rubric criteria, but
it predicts higher real-world adoption of the resulting prompt.

**3. Frontline T-GUARD × dual-contract gate creates a closed enforcement loop.**
T-GUARD as the first trigger entry (C-25) combined with both Phase 0 contract binaries
in the gate (C-37) means:
- Any structural gap during writing routes to T-GUARD before reaching specific triggers
- Any Phase 0 contract absence fails a specific gate binary at Phase 10
Neither escape path exists: frontline sentinel catches gaps during writing; gate audit
catches Phase 0 contract omissions at finalization. The two mechanisms are
complementary, not redundant.

---

## New Patterns for v12 Extraction

**Split-gate fragmentation (V-03 finding):** Separating Phase 0 contract binaries into
lifecycle sub-sections within a gate passes C-35 and C-36 independently but breaks
C-37. This is a counter-intuitive finding — adding sub-section structure seems like
more rigor, but it violates the co-presence requirement. A potential v12 criterion
(C-38?) could require the two gate binaries to be adjacent within the gate block with
no intervening sub-section header. However, V-03's score (99.67) already separates it
from the 100 ceiling, and C-37's pass condition already specifies "same gate block" —
the existing criterion language may be sufficient enforcement. No new criterion
warranted yet.

**Cascade depth invariant:** Both single-contract-absent variations (V-01, V-02) fail
exactly 3 criteria (the parent contract criterion, the gate binary criterion, and C-37).
This 1-absent-contract → 3-failure cascade is deterministic under v11. Any motivated
variation must supply both contracts to avoid the cascade. C-38 would need to target a
different failure mode to add discriminating power.
