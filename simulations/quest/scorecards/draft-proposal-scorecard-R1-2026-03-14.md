---

## Round 1 Results -- draft-proposal

| Variation | Composite | Band | Failing Criteria |
|-----------|-----------|------|-----------------|
| V-01 Inertia-First | 90 | Golden | C-05 (scout surfacing) |
| V-02 Architect-First | 100 | Golden | none |
| V-03 Slot-Structure | 100 | Golden | none |
| V-04 Conversational | 100 | Golden | none |
| V-05 Combo Ceiling | 100 | Golden | none |

**All 5 variations are Golden.** All pass all 4 essential criteria.

**V-01 is the only sub-100 score.** C-05 fails because scout artifacts are only mentioned conditionally in the recommendation phase — no dedicated inventory step, no required fallback to inline assessment. The inertia-first axis correctly closed C-01 and C-04, but the single-axis focus left C-05 uncovered.

**Golden candidate: V-05** — highest enforcement density across all 9 criteria. V-03 is the practical backup if V-05 proves too verbose.

**Discriminator correction:** The rubric predicted C-02 (option anatomy) as the most common failure. Scoring found C-05 (scout surfacing) was the actual discriminating criterion across variations. Every variation covered C-02 reliably with explicit field lists. C-05 failed only in V-01, where it was structurally absent rather than just weakly enforced.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-05 (scout surfacing) was more discriminating than C-02 (option anatomy) -- V-01 proved this by failing C-05 while passing all four essential criteria; conditional mention of scout artifacts in recommendation phase does not satisfy the criterion", "Per-category amend taxonomy (one MISSING OPTION + one UNWEIGHTED CRITERION + one FOLLOW-UP required) converts C-09 from optional depth signal to structural self-audit inside generation"]}
```
 2-3 conditions |
| C-04 | Decision framing | PASS | Phase 1 (PM): THE QUESTION + WHY NOW (explicit deadline, "do not write 'soon' or 'eventually'") + COST OF INACTION (consequence framing) -- explicitly required before any options |
| C-05 | Scout artifact surfacing | FAIL | Scout artifacts mentioned conditionally in Phase 5 only ("if a scout artifact exists..."); no dedicated inventory step; no required fallback to inline assessment if absent -- model may skip entirely |
| C-06 | Dual-role participation | PASS | PM: Phase 1 framing + Phase 5 recommendation; Architect: technical notes per option (Phase 3) -- distinct named contributions, not interchangeable |
| C-07 | Structured comparison | PASS | Phase 4: dimension table with all options as columns (including Option 0), shared rows, every cell filled |
| C-08 | Assumption and risk registers | PASS | Phase 6: assumption register (min 2, A-NN with validation plans) + risk register (min 2, PROBABILITY + IMPACT) |
| C-09 | Amend phase self-critique | PASS | Phase 7: 1-3 gaps across three explicit categories -- missing options, unweighted criteria, follow-up work |

Essential: 4/4 | Recommended: 2/3 (C-05 FAIL) | Aspirational: 2/2
`composite = (4/4 * 60) + (2/3 * 30) + (2/2 * 10) = 60 + 20 + 10 = 90` **Golden.**

---

### V-02 — Architect-First Role Sequence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | "One must be a do-nothing / status-quo option" + minimum 3 options |
| C-02 | Option anatomy complete | PASS | All fields listed; "Omitting any field fails the proposal" + per-option Architect constraint check |
| C-03 | Recommendation with rationale | PASS | Step 6: PM leads (chosen option, rationale, conditions, confidence) + Architect confirms; "both roles must speak" |
| C-04 | Decision framing | PASS | Step 3 PM Decision Frame after Architect envelope, before options: THE QUESTION + WHY NOW ("Name it explicitly") + COST OF INACTION |
| C-05 | Scout artifact surfacing | PASS | Step 1 Scout Artifact Inventory; recommendation references artifact or notes absence |
| C-06 | Dual-role participation | PASS | Architect owns Step 2 (constraint envelope); PM owns Step 3 (decision frame); both required in Step 6; "incomplete if signed by only one role" |
| C-07 | Structured comparison | PASS | Step 5 joint PM + Architect matrix; 4-6 dimensions, every cell filled |
| C-08 | Assumption and risk registers | PASS | Step 7: A-NN + validation plan, R-NN + probability/impact/mitigation, min 2 each |
| C-09 | Amend phase self-critique | PASS | Step 8: at least one missing option / unweighted criterion / follow-up action |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 2/2
`composite = 100` **Golden.**

---

### V-03 — Slot-Structure Output Format

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | Option A (Do Nothing, always first, required) + B + C + D+ ("Minimum total: 4 options") |
| C-02 | Option anatomy complete | PASS | Strongest enforcement: slot template requires `RISK: [named] | PROBABILITY | IMPACT` and `EFFORT: [N weeks] | TEAM | DEPENDENCIES` -- model cannot produce structure without filling fields |
| C-03 | Recommendation with rationale | PASS | PM RECOMMENDATION slot (CHOSEN OPTION, RATIONALE, CONDITIONS, CONFIDENCE) + ARCHITECT CONFIRMATION slot (TECHNICAL CONFIDENCE, PRECONDITIONS, QUALIFICATIONS) |
| C-04 | Decision framing | PASS | Decision Context SLOT is first: QUESTION / URGENCY / INACTION COST / SCOUT ARTIFACTS all labeled, before any options |
| C-05 | Scout artifact surfacing | PASS | SCOUT ARTIFACTS field in Decision Context slot; SCOUT SUPPORT field in Recommendation slot |
| C-06 | Dual-role participation | PASS | ARCHITECT NOTE slot per option B/C/D+ (technical constraint check); ARCHITECT CONFIRMATION slot in recommendation -- structurally separate from PM slots |
| C-07 | Structured comparison | PASS | Comparison Matrix SLOT with explicit table template, all options as columns, every cell filled |
| C-08 | Assumption and risk registers | PASS | Assumption Register SLOT (min 2 A-NN entries) + Risk Register SLOT (min 2 R-NN entries) |
| C-09 | Amend phase self-critique | PASS | AMEND SLOT with min 1 entry (rubric requires only 1 actionable item -- passes) |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 2/2
`composite = 100` **Golden.**

Note: Strongest C-02 enforcement of any variation. C-09 is minimally compliant (1 entry required vs. V-05's 3 categories).

---

### V-04 — Conversational Register + Compressed Lifecycle

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | "Minimum 4. One must be 'do nothing.'" |
| C-02 | Option anatomy complete | PASS | Fields listed explicitly; "skipping risk or effort turns this into a list of ideas, not a proposal." Risk format specifies both probability and impact. Weaker structural enforcement than V-03 -- relies on instruction, not template slot |
| C-03 | Recommendation with rationale | PASS | Name the option, why it beats alternatives (2-3 sentences), 2-3 conditions, confidence, Architect confirms or adds caveat |
| C-04 | Decision framing | PASS | "Frame the decision. Three sentences max. PM writes this -- it goes first." Three required elements before options |
| C-05 | Scout artifact surfacing | PASS | Scout artifact check at top; "Reference any scout artifact you found" in recommendation |
| C-06 | Dual-role participation | PASS | "Architect adds a note per option"; "Architect confirms or adds a caveat" in recommendation -- distinct, not interchangeable |
| C-07 | Structured comparison | PASS | "Comparison table. All options as columns. Pick 4-6 dimensions. Fill every cell." |
| C-08 | Assumption and risk registers | PASS | Hypothesis flagged C-08 at risk; actual prompt explicitly includes "Assumptions (at least 2): A-NN" and "Risks (at least 2): R-NN" -- passes |
| C-09 | Amend phase self-critique | PASS | "Before closing, name 1-3 things this proposal doesn't yet handle well" with three example gap types |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 2/2
`composite = 100` **Golden.**

Note: Lowest enforcement density of all golden variations. C-02 has highest generation-time compliance risk -- warning-based, not slot-based. Functions as expected lower-bound baseline; hypothesis that C-08 would fail was incorrect.

---

### V-05 — Inertia-First + Architect-First + Formal Register (Combo)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Options coverage | PASS | "Option 0: Do Nothing / Status Quo (Mandatory, Always First)" + "Minimum 3" alternatives Phase 5 |
| C-02 | Option anatomy complete | PASS | Table format + "Any omitted field disqualifies the proposal." Per-option Architect constraint check required |
| C-03 | Recommendation with rationale | PASS | PM leads (CHOSEN OPTION, RATIONALE, CONDITIONS, CONFIDENCE) + Architect (TECHNICAL CONFIDENCE, PRECONDITIONS, QUALIFICATIONS); "both roles must contribute" |
| C-04 | Decision framing | PASS | Phase 3 PM Decision Frame before options: THE QUESTION (interrogative sentence), WHY NOW ("Do not use 'soon,' 'eventually,' or 'in the near future'"), COST OF INACTION (consequence framing) |
| C-05 | Scout artifact surfacing | PASS | Phase 1 Inventory with file name + date + single most relevant finding; fallback noted; required in Phase 7 |
| C-06 | Dual-role participation | PASS | Architect owns Phase 2 (C-NN constraint inventory) + per-option constraint check; PM owns Phase 3 (decision frame); both required in Phase 7; "incomplete if signed by only one role" |
| C-07 | Structured comparison | PASS | Phase 6 matrix; required dimensions specified (effort, team control, adoption friction, time to value) + domain-specific |
| C-08 | Assumption and risk registers | PASS | Phase 8 (A-NN with "concrete action, not a monitoring posture") + Phase 9 (R-NN with "Specific action or contingency, not 'monitor closely'") -- highest specificity enforcement |
| C-09 | Amend phase self-critique | PASS | Phase 10: three mandatory categories -- MISSING OPTION + UNWEIGHTED CRITERION + FOLLOW-UP -- at least one per category; converts C-09 from post-hoc criterion to in-prompt self-check |

Essential: 4/4 | Recommended: 3/3 | Aspirational: 2/2
`composite = 100` **Golden. Highest enforcement quality.**

---

## Excellence Signals

Patterns from top-scoring variations that elevated output quality beyond rubric compliance:

### 1. Mandatory amend taxonomy with named categories (V-05)
Phase 10 requires at least one entry per: MISSING OPTION / UNWEIGHTED CRITERION / FOLLOW-UP. This converts C-09 from a post-generation scoring criterion into a structural self-check the model performs during generation. Other variations allow a vague amend entry and technically pass. V-05 cannot produce C-09 without covering all three gap types.

### 2. Dual-role recommendation lock with explicit incompleteness clause (V-02, V-05)
"A recommendation signed by only one role is incomplete." This makes PM/Architect separation in C-06 a generation-time rule rather than a stylistic suggestion. Without this clause, a model can produce interchangeable prose under two role labels. The clause forces the Architect section to add distinct technical content or be explicitly absent.

### 3. Temporal specificity prohibition in WHY NOW (V-05)
"Do not use 'soon,' 'eventually,' or 'in the near future.'" Enforces C-04's urgency framing at the lexical level -- preventing the most common C-04 degradation pattern where the framing is formally present but vague enough to be useless.

### 4. Constraint envelope before options (V-02, V-05)
Architect locks C-NN constraints before PM names any options. Per-option Architect constraint check verifies compliance. This prevents C-02 effort fields from being theoretical and forces the Architect role in C-06 to contribute substantive technical content rather than a generic endorsement.

---

## Hypothesis Verification

| Hypothesis | Result |
|------------|--------|
| V-05 most likely golden candidate | Confirmed -- highest enforcement quality |
| V-04 C-08 at risk (registers may be omitted in lighter framing) | **Incorrect** -- V-04 explicitly lists registers with A-NN/R-NN format; C-08 passed |
| V-03 structural safety net if V-05 too verbose | Confirmed -- V-03 is strongest C-02 defense; practical alternative |
| C-02 most discriminating criterion | **Incorrect** -- C-05 (scout surfacing) was the actual discriminating criterion; V-01 failed C-05, not C-02 or C-04; all variations reliably covered C-02 with their field lists |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-05 (scout surfacing) was more discriminating than C-02 (option anatomy) -- V-01 proved this by failing C-05 while passing all four essential criteria; conditional mention of scout artifacts in recommendation phase does not satisfy the criterion", "Per-category amend taxonomy (one MISSING OPTION + one UNWEIGHTED CRITERION + one FOLLOW-UP required) converts C-09 from optional depth signal to structural self-audit inside generation"]}
```
