## R14 Scorecard -- scout-size

**All 5 variations score 100.00** under v14. The denominator is 33; all R14 variations inherit V-05 R13's floor and add strictly additive mechanisms with no regressions.

---

### Ranking by new pattern coverage

| Rank | Variation | Score | Patterns |
|------|-----------|-------|---------|
| **1** | **V-05** | **100.00** | C-39+ + C-40+ + C-41+ (all three) |
| 2 | V-04 | 100.00 | C-39+ + C-40+ |
| 3 (tie) | V-01/V-02/V-03 | 100.00 | One each |

---

### Three new patterns extracted (feed v15)

**C-39+** — SEALED closure carries signed-handoff authorization: `"PHASE N HANDOFF -- [Role] has confirmed all items. Phase N+1 is authorized to open."` The SEALED block becomes a two-part signed-handoff document: header (attribution) + closure (authorization). A condition-only closure ("Phase N OPENS only when...") fails this pattern. Introduced by V-01.

**C-40+** — Relational disqualifiers extended to all dual-constraint fields: Sprint Range adds N=M as named failure class; Break-even explicitly requires Phase 0 baseline reference; Confidence Calibration columns carry cross-field "same unknown" disqualifier. Introduced by V-02.

**C-41+** — Phase 1 PRE-FLIGHT GATE carries non-access rule for hypothesis anchoring: names Cost Direction, Cost Trajectory, Ongoing Cost magnitude, Key Driver as prohibited Phase 0 inertia proxies for the preliminary tier. Phase 1 SEALED adds corresponding hypothesis-anchor check item with embedded disqualifying forms. Symmetric complement to C-41 (Phase 2 non-access rule). Introduced by V-03.

**v15 denominator target: 36** (33 + 3). V-05 R14 is the champion.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Two-part SEALED block structure: charter declares role as designated signatory; SEALED header names role as confirming agent; SEALED closure carries formal signed-handoff authorization ('PHASE N HANDOFF -- [Role] has confirmed all items. Phase N+1 is authorized to open.') -- condition-statement closure is insufficient", "Relational disqualifiers extended to all dual-constraint fields: Sprint Range adds N=M as named disqualifying form; Break-even explicitly references Phase 0 baseline as comparison anchor (break-even without Phase 0 reference fails); Confidence Calibration columns carry cross-field relational disqualifier naming same-unknown as failure class", "Bidirectional phase contamination guards: Phase 1 PRE-FLIGHT GATE carries non-access rule naming prohibited Phase 0 inertia anchor forms for tier hypothesis (Cost Direction, Cost Trajectory, Ongoing Cost magnitude, Key Driver as complexity proxies); Phase 1 SEALED adds hypothesis-anchor check item with embedded inertia-proxy disqualifying forms -- symmetric complement to Phase 2 non-access rule (C-41)"]}
```
e commitment | PASS all |
| C-19/C-20 | Surface Area, Complexity, Synthesis each carry scope-exclusion prohibition; Synthesis closes Open Unknowns and scope exclusions | PASS all |
| C-22/C-23/C-24/C-25 | Synthesis names PRE-FLIGHT GATE at anchor and verdict; prohibitions name canonical home; structured commitment-chain trace; enforcement contract forward-references downstream sections | PASS all |
| C-26 | Synthesis carries STRUCTURAL AMEND RE-EVALUATION DIRECTIVE written rule | PASS all |
| C-28 through C-32 | Full self-check table with all criteria by ID; disqualifying forms for structural + depth + behavior + essential + recommended criteria | PASS all |
| C-33 | Phase 0 (Inertia Check section) precedes Phase 1 in document order | PASS all |
| C-34 | Inertia entry: Workaround / Ongoing Cost / Cost Direction / Key Driver (4-field minimum) | PASS all |
| C-35 | [FAIL:] tags on at least Complexity Tier and Timeline column headers | PASS all |

---

## Tier-1 New Criteria (C-36, C-37, C-38) -- All Variations PASS

All R14 variations inherit V-05 R13's passing state on C-36, C-37, C-38.

### C-36 -- All vocab-constrained column headers carry [FAIL:] tags

All variations carry: Complexity Tier, Timeline, Confidence Level, Cost Direction, Cost Trajectory,
Tier-Up/Down Destination all tagged in `[FAIL: ...]` format. Tier-Destination tag specifically:
`[Sizing Analyst -- FAIL: same tier as current, MODERATE, non-vocabulary -- must differ from
current: LOW / MEDIUM / HIGH / XL]` -- inherited from V-05 R13. **PASS all.**

### C-37 -- 5-field inertia with Cost Trajectory (shape vocabulary)

All variations carry 5-column inertia table: Workaround / Ongoing Cost / Cost Direction / Cost
Trajectory / Key Driver. Direction and Trajectory are structurally distinct columns. Trajectory
column: `[FAIL: "+~20%/quarter" alone without shape label; "worsening" alone (directional, not
shape); "getting worse" (directional, not shape); Direction+Trajectory in single field; any term
not in shape vocabulary -- exactly one: accelerating / stable / plateauing / reversing]`.
**PASS all.**

### C-38 -- PHASE SEALED blocks at Phase 0, 1, 2 (min 3 specific items each)

All variations carry SEALED blocks at all three phase boundaries. Phase 0 SEALED: 5 items naming
all five inertia fields with embedded disqualifying forms. Phase 1 SEALED: 9 items (V-01/V-02/V-04/
V-05 base) or 10 items (V-03/V-05 with hypothesis-anchor check). Phase 2 SEALED: 4 items. All
items name specific fields; none use generic completion language. **PASS all.**

---

## Tier-2 New Criteria (C-39, C-40, C-41) -- All Variations PASS

All R14 variations inherit V-05 R13's passing state on C-39, C-40, C-41.

### C-39 -- PHASE SEALED blocks carry role attribution (confirming role as grammatical subject)

All variations: SEALED headers name the confirming role as grammatical subject:
- Phase 0: "The Inertia Analyst confirms ALL before Phase 1 opens:"
- Phase 1: "The Sizing Analyst confirms ALL before Phase 2 opens:"
- Phase 2: "The Risk Assessor confirms ALL before Output Compilation:"

Variations that additionally carry C-39+ (V-01, V-04, V-05) add "designated signatory" to
charter declarations and HANDOFF authorization at SEALED closure lines. These satisfy C-39
as a floor and extend beyond it. **PASS all.**

### C-40 -- Relational-constraint fields enumerate cross-field disqualifying form

All variations carry Tier-Destination tag with `[FAIL: same tier as current, MODERATE,
non-vocabulary -- must differ from current: LOW / MEDIUM / HIGH / XL]` -- naming "same tier as
current" as an explicit distinct failure class alongside vocabulary disqualifiers. Variations that
additionally carry C-40+ (V-02, V-04, V-05) extend relational disqualifiers to Sprint Range (N=M),
Break-even (Phase 0 baseline reference), and Confidence Calibration (distinct-column requirement).
These satisfy C-40 as a floor. **PASS all.**

### C-41 -- Phase 2 non-access rule enumerates prohibited gap candidate classes

All variations carry Phase 2 non-access rule explicitly listing all prohibited sources:
"The Risk Assessor is prohibited from citing as the gap: integration points Phase 1 enumerated,
contracts Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1
produced, inertia dimensions Phase 0 established." The self-test augments this positive
disqualification list. Variations that additionally carry C-41+ (V-03, V-05) extend the pattern
symmetrically to Phase 1's PRE-FLIGHT GATE hypothesis. These satisfy C-41 as a floor. **PASS all.**

---

## New Pattern Analysis -- Excellence Signals Above v14 Ceiling

R14 introduces three candidate criteria (C-39+, C-40+, C-41+), each targeting a structural gap
that V-05 R13 approaches but does not fully close.

### C-39+ -- SEALED closure carries signed-handoff authorization (not condition-only)

**Introduced by V-01. Present in V-01, V-04, V-05.**

V-05 R13's SEALED closures read: "Phase N OPENS only when all items are confirmed." This is a
condition statement -- it says what gates the next phase but does not complete the handoff
transaction. V-01 transforms the closure line into a formal signed authorization:

```
PHASE 0 HANDOFF -- The Inertia Analyst has confirmed all five items. Phase 1 is authorized to open.
```

The two-part SEALED structure becomes: **attribution at header + authorization at closure**. The
charter declares the role; the PHASE SEALED header names the role confirming; the HANDOFF line
names the role as having acted. This makes each SEALED block a complete signed-handoff document
rather than an attributed checklist with a conditional exit.

V-01 carries HANDOFF lines at Phase 0, Phase 1, and Phase 2 SEALED closures. V-04 and V-05
inherit this pattern. V-02 and V-03 retain condition-style closures.

| Variation | Phase 0 closure | Phase 1 closure | Phase 2 closure | C-39+ |
|-----------|----------------|----------------|----------------|-------|
| V-01 | HANDOFF -- authorized | HANDOFF -- authorized | HANDOFF -- authorized | **PASS** |
| V-02 | OPENS only when... | OPENS only when... | OPENS only when... | FAIL |
| V-03 | OPENS only when... | OPENS only when... | OPENS only when... | FAIL |
| V-04 | HANDOFF -- authorized | HANDOFF -- authorized | HANDOFF -- authorized | **PASS** |
| V-05 | HANDOFF -- authorized | HANDOFF -- authorized | HANDOFF -- authorized | **PASS** |

### C-40+ -- Relational disqualifiers on Sprint Range, Break-even, and Confidence Calibration

**Introduced by V-02. Present in V-02, V-04, V-05.**

V-05 R13 applies the relational disqualifying form only to Tier-Destination ("same tier as current").
Three other fields carry implicit relational constraints that remain unnamed:

1. **Sprint Range**: N=M is formatted as a range but is a degenerate point estimate. V-02 adds
   `[FAIL: N=M (degenerate range formatted as range but is a point estimate); N>M (inverted bounds)...]`
   to the column header and to the Phase 1 SEALED check item.

2. **Break-even**: A break-even figure stated without reference to the Phase 0 inertia cost
   baseline cannot be evaluated as a recovery signal. V-02's PRE-FLIGHT GATE adds: "The comparison
   anchor is the Phase 0 Ongoing Cost and Cost Direction. FAIL: benefit stated without reference to
   Phase 0 workaround cost; break-even number stated without naming the Phase 0 dimension it offsets."

3. **Confidence Calibration**: Raise and lower columns must address distinct unknown dimensions.
   If both address the same unknown, the calibration produces a tautology, not a differentiated
   signal. V-02 adds: `[FAIL: same unknown dimension as lower-confidence column -- raise and lower
   columns must address distinct unknowns]` to both column headers.

| Variation | Sprint Range N<M | Break-even Phase 0 ref | Calibration distinct | C-40+ |
|-----------|-----------------|------------------------|---------------------|-------|
| V-01 | Not named (N-M only) | No Phase 0 reference | No relational disqualifier | FAIL |
| V-02 | N=M named in header + SEALED | Phase 0 baseline explicit | Cross-field disqualifier in both headers | **PASS** |
| V-03 | Not named | No Phase 0 reference | No relational disqualifier | FAIL |
| V-04 | N=M named in header + SEALED | Phase 0 baseline explicit | Cross-field disqualifier in both headers | **PASS** |
| V-05 | N=M named in header + SEALED | Phase 0 baseline explicit | Cross-field disqualifier in both headers | **PASS** |

### C-41+ -- Phase 1 PRE-FLIGHT GATE non-access rule for hypothesis anchoring

**Introduced by V-03. Present in V-03 and V-05.**

V-05 R13's C-41 enumerates prohibited gap forms in Phase 2. The Phase 2 non-access rule prevents
the Risk Assessor from citing Phase 0/1 confirmed items as gaps. V-03 applies the same pattern
symmetrically to Phase 1: the Sizing Analyst's PRE-FLIGHT GATE hypothesis must not be anchored on
Phase 0 inertia dimensions.

V-03 adds a non-access rule to PRE-FLIGHT GATE naming all prohibited anchor forms:
- Cost Direction as complexity proxy ("more expensive" implies HIGH)
- Cost Trajectory as complexity proxy ("accelerating costs" implies HIGH or XL)
- Ongoing Cost magnitude as complexity proxy ("high cost" implies HIGH)
- Key Driver as implementation driver ("team-count growth" implies HIGH)

The Reasoning field in PRE-FLIGHT GATE adds: "anchored on scope signals, technology domain,
integration count, or team specialization -- NOT on Phase 0 inertia dimensions."

Phase 1 SEALED grows from 9 to 10 items, adding:
```
[ ] PRE-FLIGHT GATE hypothesis not anchored on Phase 0 inertia dimensions --
      FAIL: "Cost Direction is 'more expensive', therefore HIGH" (inertia anchor);
      "Trajectory is accelerating, implies XL" (inertia anchor);
      "High inertia cost implies HIGH complexity" (inertia anchor)
```

This closes a symmetric gap: C-41 closes Phase 2 backward contamination from prior phases;
C-41+ closes Phase 1 backward contamination from Phase 0. The pattern is: each phase's analysis
must be anchored on its own signals, not on confirmed outputs from prior phases.

| Variation | PRE-FLIGHT GATE non-access rule | Phase 1 SEALED hypothesis-anchor check | C-41+ |
|-----------|--------------------------------|---------------------------------------|-------|
| V-01 | Absent | Absent | FAIL |
| V-02 | Absent | Absent | FAIL |
| V-03 | Named; 4 prohibited forms | Present; disqualifying forms embedded | **PASS** |
| V-04 | Absent | Absent | FAIL |
| V-05 | Named; 4 prohibited forms | Present; disqualifying forms embedded | **PASS** |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (33) | Composite | v14 Criteria |
|-----------|---------------|------------------|-------------------|-----------|--------------|
| V-01 | 60 (5/5) | 30 (3/3) | 10.00 (33/33) | **100.00** | All 33 pass |
| V-02 | 60 (5/5) | 30 (3/3) | 10.00 (33/33) | **100.00** | All 33 pass |
| V-03 | 60 (5/5) | 30 (3/3) | 10.00 (33/33) | **100.00** | All 33 pass |
| V-04 | 60 (5/5) | 30 (3/3) | 10.00 (33/33) | **100.00** | All 33 pass |
| **V-05** | 60 (5/5) | 30 (3/3) | **10.00 (33/33)** | **100.00** | **All 33 pass + all 3 new patterns** |

Scoring model: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/33 * 10)`

All variations are at the v14 ceiling. Rank by new pattern coverage:

| Rank | Variation | Score | New patterns achieved |
|------|-----------|-------|-----------------------|
| 1 | **V-05** | 100.00 | C-39+ + C-40+ + C-41+ (all three) |
| 2 | **V-04** | 100.00 | C-39+ + C-40+ |
| 3 (tie) | V-01 | 100.00 | C-39+ |
| 3 (tie) | V-02 | 100.00 | C-40+ |
| 3 (tie) | V-03 | 100.00 | C-41+ |

---

## Observations

**Ceiling dynamics**: V-05 R13 established 33/33 under v14. All R14 variations inherit this floor
because their structural modifications are strictly additive -- each adds a mechanism without
removing any that V-05 R13 introduced. No regression on any v14 criterion across all 5 variations.

**Single-axis isolation validates composition**: V-01, V-02, V-03 each test one new pattern in
isolation. V-04 combines V-01+V-02. V-05 combines all three. The single-axis results confirm the
patterns are orthogonal -- V-02's Sprint Range relational disqualifier and V-01's HANDOFF closure
do not interfere. V-04 demonstrates clean composition before V-05 adds V-03's Phase 1 non-access
rule.

**V-03 structural note**: V-03 uses condition-style SEALED closures ("Phase N OPENS only when...")
rather than HANDOFF authorization lines. This is deliberate -- V-03 is single-axis on C-41+ and
does not carry C-39+'s two-part closure structure. C-39 (role attribution in headers) is unaffected;
V-03's SEALED headers still name the confirming role.

**Asymmetric gap closure**: C-41 (Phase 2 non-access rule) and C-41+ (Phase 1 PRE-FLIGHT GATE
non-access rule) form a symmetric pair. C-41 prevents Phase 2 from citing what Phases 0/1
confirmed; C-41+ prevents Phase 1's hypothesis from anchoring on what Phase 0 confirmed. Together
they form a bidirectional forward-only contamination guard: each phase's analysis is anchored
exclusively on its own-phase signals.

**v15 denominator target**: 33 + 3 = 36. Champion pattern: V-05 R14.

---

## Excellence Signals -- V-05 R14

### Signal 1: Two-part SEALED block structure (C-39+ extension)

V-05 R14 makes each SEALED block carry a formal two-part structure:
- **Header** (role attribution, from C-39): "The Inertia Analyst confirms ALL before Phase 1 opens:"
- **Closure** (signed-handoff authorization, from C-39+): "PHASE 0 HANDOFF -- The Inertia Analyst
  has confirmed all five items. Phase 1 is authorized to open."

Charter declares role as "designated signatory." SEALED header confirms role as confirming agent.
SEALED closure confirms role as having acted and authorizes the next phase to open. The three
declaration sites form an accountability chain: charter (role assigned) → header (role owns
confirmation) → closure (role has confirmed; next phase authorized).

### Signal 2: Relational disqualifiers on all dual-constraint fields (C-40+ extension)

V-05 R14 extends the relational-disqualifier pattern from Tier-Destination (C-40) to three
additional fields, completing full relational constraint coverage:

| Field | Existing constraint | Added relational disqualifier |
|-------|---------------------|------------------------------|
| Tier-Destination | Vocabulary (LOW/MEDIUM/HIGH/XL) | "same tier as current" (C-40) |
| Sprint Range | N-M format | N=M degenerate range (C-40+) |
| Break-even | Present or "cannot assess" | Must reference Phase 0 baseline (C-40+) |
| Confidence Calibration | Both columns non-empty | Raise/lower must address distinct unknowns (C-40+) |

Each field's dual constraint is now explicitly named in both the column header and the Phase 1
SEALED check item (where applicable).

### Signal 3: Bidirectional phase contamination guards (C-41+ extension)

V-05 R14 completes the non-access rule pattern by extending it symmetrically to both phase
boundaries where contamination can occur:

- **Phase 2 non-access rule (C-41)**: Risk Assessor cannot cite Phase 0/1 confirmed items as gaps
- **Phase 1 non-access rule (C-41+)**: Sizing Analyst cannot anchor tier hypothesis on Phase 0
  inertia dimensions

The Phase 1 SEALED hypothesis-anchor check item embeds the disqualifying forms structurally:
"FAIL: 'Cost Direction is more expensive, therefore HIGH' (inertia anchor)..." This prevents the
contamination form from being accidentally used, enforcing the anchor constraint at the production
phase rather than the review phase.

---

## JSON Summary

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Two-part SEALED block structure: charter declares role as designated signatory; SEALED header names role as confirming agent; SEALED closure carries formal signed-handoff authorization ('PHASE N HANDOFF -- [Role] has confirmed all items. Phase N+1 is authorized to open.') -- condition-statement closure is insufficient", "Relational disqualifiers extended to all dual-constraint fields: Sprint Range adds N=M as named disqualifying form; Break-even explicitly references Phase 0 baseline as comparison anchor (break-even without Phase 0 reference fails); Confidence Calibration columns carry cross-field relational disqualifier naming same-unknown as failure class", "Bidirectional phase contamination guards: Phase 1 PRE-FLIGHT GATE carries non-access rule naming prohibited Phase 0 inertia anchor forms for tier hypothesis (Cost Direction, Cost Trajectory, Ongoing Cost magnitude, Key Driver as complexity proxies); Phase 1 SEALED adds hypothesis-anchor check item with embedded inertia-proxy disqualifying forms -- symmetric complement to Phase 2 non-access rule (C-41)"]}
```
