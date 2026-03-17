---

## Round 2 Results -- draft-proposal

| Variation | Composite | Band | Failing Criteria |
|-----------|-----------|------|-----------------|
| V-01 Amend Headers + Owner | 100 | Golden | none |
| V-02 Dual-Signature Form | 97.5 | Golden | C-11 |
| V-03 Split Temporal Anchor | 97.5 | Golden | C-11 |
| V-04 Conversational Combo | 100 | Golden | none |
| V-05 Full Integration | 100 | Golden | none |

**All 5 Golden.** Three at 100, two at 97.5.

**C-11 is the R2 discriminator.** V-02 and V-03 list three amend categories but don't structurally enforce the OWNER field. Without a format template requiring `-- OWNER: [role]`, the model can produce FOLLOW-UP entries with no owner named. V-01, V-04, and V-05 all added OWNER fields to the amend sub-header format templates — they pass. Three categories listed is not sufficient; the OWNER field is load-bearing.

**Surprise finding:** V-04's conversational register reaches 100. The assessed risk (C-11 without an incompleteness clause) did not materialize — OWNER format templates are sufficient without a dual-signature gate. Register is orthogonal to structural completeness when templates are properly placed.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Structural OWNER fields in amend sub-headers are load-bearing for C-11 -- listing three amend categories without OWNER format templates fails C-11 even when all categories are present (V-02, V-03 demonstrated this)", "Register is orthogonal to structural completeness -- V-04 conversational register reaches the same 100 ceiling as V-05 when format templates with OWNER fields are properly placed", "Split temporal anchor (TEMPORAL ANCHOR + INACTION CONSEQUENCE as separate fields) prevents the consequence-free framing failure that a single WHY NOW field allows -- valid enforcement upgrade for C-04 quality beyond its pass condition"]}
```

| C-03 | Recommendation with rationale | PASS | PM: CHOSEN OPTION, RATIONALE, CONDITIONS, CONFIDENCE. Architect: TECHNICAL CONFIDENCE, PRECONDITIONS, QUALIFICATIONS. Incompleteness clause present. |
| C-04 | Decision framing | PASS | Phase 3 PM Decision Frame before options: THE QUESTION + WHY NOW (no vague temporal language) + COST OF INACTION |
| C-05 | Scout artifact surfacing | PASS | Phase 1 dedicated Scout Artifact Inventory: scan all 4 types, record file name + date + most relevant finding, explicit fallback if absent |
| C-06 | Dual-role participation | PASS | Architect owns Phase 2 + per-option constraint check; PM owns Phase 3; both required in Phase 7 |
| C-07 | Structured comparison | PASS | Phase 6 comparison matrix with required dimensions: effort, team control, adoption friction, time to value |
| C-08 | Assumption and risk registers | PASS | Phase 8: A-NN with concrete validation plans; Phase 9: R-NN with PROBABILITY + IMPACT + MITIGATION |
| C-09 | Amend phase self-critique | PASS | Phase 10 mandatory sub-headers; at least one entry per category required |
| C-10 | Scout artifact inventory step | PASS | Phase 1 is a discrete structural step before any options; lists found artifacts by file name, states absence explicitly |
| C-11 | Per-category amend taxonomy | PASS | Phase 10 has three mandatory sub-headers (MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP); each entry requires OWNER and NEXT ACTION or DEADLINE field structurally |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 4/4
composite = (4/4 * 60) + (3/3 * 30) + (4/4 * 10) = 100 -- Golden.

---

### V-02 -- Recommendation Dual-Signature Form

Axis: Recommendation section structure (single-axis upgrade)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | Phase 4 Option 0 mandatory + Phase 5 minimum 3 alternatives |
| C-02 | Option anatomy complete | PASS | Table format + "Any omitted field disqualifies the proposal." |
| C-03 | Recommendation with rationale | PASS | Dual-signature form: PM block + Architect block + INCOMPLETE STATUS: COMPLETE required. Interchangeable prose explicitly blocked. |
| C-04 | Decision framing | PASS | Phase 3: THE QUESTION + WHY NOW + COST OF INACTION before options |
| C-05 | Scout artifact surfacing | PASS | Phase 1 Scout Artifact Inventory; RATIONALE field requires artifact reference or "none found" |
| C-06 | Dual-role participation | PASS | Architect owns Phase 2 + per-option constraint check + CONSTRAINT VERIFIED in sign-off; INCOMPLETE STATUS gate prevents single-voice output |
| C-07 | Structured comparison | PASS | Phase 6 comparison matrix with required dimensions |
| C-08 | Assumption and risk registers | PASS | Phase 8 + Phase 9 registers with concrete action enforcement |
| C-09 | Amend phase self-critique | PASS | Phase 10 lists three amend categories; at least one entry per category required |
| C-10 | Scout artifact inventory step | PASS | Phase 1 is a dedicated pre-option inventory step with explicit fallback |
| C-11 | Per-category amend taxonomy | FAIL | Phase 10 lists three categories (MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP) but no structural OWNER field in amend entries. Model can produce FOLLOW-UP items without naming an owner or next step. Category coverage satisfies C-09; owner requirement not enforced. |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 3/4 (C-11 FAIL)
composite = (4/4 * 60) + (3/3 * 30) + (3/4 * 10) = 97.5 -- Golden.

---

### V-03 -- Temporal Anchor as Separate Typed Fields

Axis: Decision frame field granularity (single-axis upgrade)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | Phase 4 Option 0 mandatory + Phase 5 minimum 3 alternatives |
| C-02 | Option anatomy complete | PASS | Table format + "Any omitted field disqualifies the proposal." |
| C-03 | Recommendation with rationale | PASS | PM leads + Architect confirms; "both roles must contribute" |
| C-04 | Decision framing | PASS | Phase 3 now has four required fields: THE QUESTION + WHY NOW + TEMPORAL ANCHOR (specific named date/sprint/event, no vague language) + INACTION CONSEQUENCE (concrete outcome, not a missed feature). Stronger than minimum. |
| C-05 | Scout artifact surfacing | PASS | Phase 1 Scout Artifact Inventory with dedicated scan and fallback |
| C-06 | Dual-role participation | PASS | Architect owns Phase 2 + per-option constraint check; PM leads Phase 3 and recommendation |
| C-07 | Structured comparison | PASS | Phase 6 comparison matrix |
| C-08 | Assumption and risk registers | PASS | Phase 8 + Phase 9 registers |
| C-09 | Amend phase self-critique | PASS | Phase 10 lists three categories; at least one entry per category required |
| C-10 | Scout artifact inventory step | PASS | Phase 1 is a dedicated pre-option inventory step |
| C-11 | Per-category amend taxonomy | FAIL | Phase 10 lists three categories (MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP) without structural OWNER field requirement. Same gap as V-02. |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 3/4 (C-11 FAIL)
composite = (4/4 * 60) + (3/3 * 30) + (3/4 * 10) = 97.5 -- Golden.

Note: V-03's temporal anchor split is the strongest C-04 quality upgrade across all variations. TEMPORAL ANCHOR forces a specific named date; INACTION CONSEQUENCE forces a concrete named outcome. Neither field can be satisfied with vague temporal language. This structural split pre-empts C-12 (not yet in rubric) and elevates C-04 quality beyond its pass condition.

---

### V-04 -- Amend Headers + Temporal Anchor in Conversational Register (Combo)

Axis: Amend phase structure + temporal anchor, conversational register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | "Minimum 4. One must be 'do nothing.'" -- higher floor than minimum |
| C-02 | Option anatomy complete | PASS | All fields listed; "skipping risk or effort turns this into a list of ideas, not a proposal." Risk requires probability and impact named. |
| C-03 | Recommendation with rationale | PASS | Name the option, why it beats alternatives in 2-3 sentences, 2-3 conditions, confidence, Architect confirms or adds a caveat. Both roles named. |
| C-04 | Decision framing | PASS | Four required fields before options: QUESTION + WHY NOW + TEMPORAL ANCHOR (specific date/sprint/event, explicit prohibition) + INACTION CONSEQUENCE (teams will lose/be blocked -- not a feature they miss). |
| C-05 | Scout artifact surfacing | PASS | "Start by looking for scout work... Note what you found at the top of the output. If nothing exists, say so and add a quick inline assessment." Discrete step, not conditional mention. |
| C-06 | Dual-role participation | PASS | "Architect adds a note per option: technical feasibility, constraints, or blockers not visible from pros/cons alone" + "Architect confirms or adds a caveat" in recommendation. Distinct contributions. |
| C-07 | Structured comparison | PASS | "Comparison table. All options as columns. Pick 4-6 dimensions. Fill every cell." |
| C-08 | Assumption and risk registers | PASS | Assumptions (at least 2) A-NN + Risks (at least 2) R-NN with probability, impact, mitigation |
| C-09 | Amend phase self-critique | PASS | "Before closing, use these three headers. Write at least one entry under each." |
| C-10 | Scout artifact inventory step | PASS | Scout work check at top of execution sequence before decision frame and options. "Note what you found at the top of the output" -- discrete listing step. |
| C-11 | Per-category amend taxonomy | PASS | All three amend headers mandatory (MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP). Each has explicit format template requiring OWNER. Cannot satisfy format without naming an owner. |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 4/4
composite = (4/4 * 60) + (3/3 * 30) + (4/4 * 10) = 100 -- Golden.

Note: V-04 reaches the 100 ceiling in conversational register. The assessed risk (C-11 without incompleteness clause) did not materialize -- OWNER format templates are sufficient without a dual-signature gate. Register is orthogonal to structural completeness when templates are properly placed.

---

### V-05 -- Full Integration (All Three R2 Enforcement Mechanisms)

Axis: Amend headers + dual-signature form + split temporal anchor + V-05 R1 base

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | Phase 4 Option 0 mandatory + Phase 5 minimum 3 alternatives; Architect note on status quo stability required |
| C-02 | Option anatomy complete | PASS | Table format + "Any omitted field disqualifies the proposal." + per-option Architect constraint check. Highest structural density. |
| C-03 | Recommendation with rationale | PASS | Dual-signature form with INCOMPLETE STATUS gate. "A recommendation signed by only one role is incomplete. Interchangeable prose under two role headers is a fail." |
| C-04 | Decision framing | PASS | Phase 3 four required fields: THE QUESTION + WHY NOW + TEMPORAL ANCHOR (examples provided, vague language prohibited) + INACTION CONSEQUENCE (teams will lose/incur/be blocked). Strongest C-04 enforcement of all variations. |
| C-05 | Scout artifact surfacing | PASS | Phase 1 dedicated inventory scan (all 4 artifact types), file name + date + most relevant finding, explicit fallback; RATIONALE in PM sign-off requires artifact reference or "none found" |
| C-06 | Dual-role participation | PASS | Architect owns Phase 2 + per-option constraint check + CONSTRAINT VERIFIED field; INCOMPLETE STATUS gate prevents single-voice output; interchangeable prose explicitly blocked |
| C-07 | Structured comparison | PASS | Phase 6 matrix with required dimensions named + domain-specific; no empty cells |
| C-08 | Assumption and risk registers | PASS | Phase 8: A-NN with "concrete action, not a monitoring posture"; Phase 9: R-NN with "Specific action or contingency, not 'monitor closely'" -- highest specificity |
| C-09 | Amend phase self-critique | PASS | Phase 10 mandatory sub-headers; at least one entry per category required |
| C-10 | Scout artifact inventory step | PASS | Phase 1 is a dedicated structural phase before options; scan + record + fallback all required |
| C-11 | Per-category amend taxonomy | PASS | Phase 10 has three mandatory sub-headers (MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP); each requires OWNER field; cannot be omitted without violating format |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 4/4
composite = (4/4 * 60) + (3/3 * 30) + (4/4 * 10) = 100 -- Golden. Highest enforcement density.

---

## Excellence Signals (R2)

### 1. Structural OWNER fields in amend sub-headers (V-01, V-04, V-05)

Adding OWNER field to each amend entry's required format converts C-11 from an instructional requirement into a form-filling requirement. V-02 and V-03 listed three categories without OWNER fields and failed C-11 as a result. Three categories listed is not the ceiling -- OWNER enforcement is load-bearing.

### 2. Split temporal anchor (V-03, V-04, V-05)

Separating WHY NOW into TEMPORAL ANCHOR (specific named date/sprint/event) and INACTION CONSEQUENCE (concrete named outcome) prevents the "present but consequence-free" C-04 failure mode. A single WHY NOW field can satisfy the vague-language prohibition with an empty anchor ("the Q2 window opens"). Two separate mandatory fields cannot -- each requires distinct content. C-12 is not yet in the rubric but this pattern strengthens C-04 quality beyond its pass condition.

### 3. INCOMPLETE STATUS gate in dual-signature form (V-02, V-05)

The INCOMPLETE STATUS footer makes dual-role participation a mechanical gate. A model producing interchangeable content under two role headers cannot set status to COMPLETE without distinct PRECONDITIONS and CONSTRAINT VERIFIED content in the Architect block. Highest-specificity C-06 enforcement across all rounds.

### 4. Register is orthogonal to structural completeness (V-04)

V-04's conversational register reaches the same 100 ceiling as V-05's formal register when format templates with OWNER fields are properly placed. Register choice does not constrain structural enforcement when form templates are used.

---

## Hypothesis Verification

| Hypothesis | Result |
|------------|--------|
| V-05 most likely golden | Confirmed -- perfect score, highest enforcement density |
| V-01 safest single-axis upgrade | Confirmed -- 100 with minimal change from R1 |
| V-04 C-11 at risk without incompleteness clause | Incorrect -- OWNER format templates are sufficient; incompleteness clause is not required for C-11 |
| V-02 and V-03 golden (single-axis upgrades) | Partial -- both golden at 97.5; C-11 fails because neither adds OWNER to amend entries |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Structural OWNER fields in amend sub-headers are load-bearing for C-11 -- listing three amend categories without OWNER format templates fails C-11 even when all categories are present (V-02, V-03 demonstrated this)", "Register is orthogonal to structural completeness -- V-04 conversational register reaches the same 100 ceiling as V-05 when format templates with OWNER fields are properly placed", "Split temporal anchor (TEMPORAL ANCHOR + INACTION CONSEQUENCE as separate fields) prevents the consequence-free framing failure that a single WHY NOW field allows -- valid enforcement upgrade for C-04 quality beyond its pass condition"]}
```