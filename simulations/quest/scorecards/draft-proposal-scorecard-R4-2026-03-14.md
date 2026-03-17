## Round 4 Scorecard — `draft-proposal`

### Rubric v4 Structure
- **Essential (60%)**: C-01 through C-04 (4 criteria)
- **Recommended (30%)**: C-05 through C-07 (3 criteria)
- **Aspirational (10%)**: C-08 through C-18 (11 criteria)

Formula: `(essential/4 × 60) + (recommended/3 × 30) + (aspirational/11 × 10)`

---

## V-01: F-Row 3-Field Explicit Template

**Axis**: F-row failure mode field precision — explicit FAILURE MODE / TRIGGER CONDITION / MITIGATION labels + F-ROW ANCHOR as typed slot in PM and Architect sign-off.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Phase 5 (Option 0) + Phase 6 (≥3 alternatives) — numbered, structurally distinct, do-nothing mandatory and always first |
| C-02 | Option anatomy complete | **PASS** | Phase 5/6 table template enforces Description / Pros / Cons / Risk (P×I) / Effort on every option — row omission fails artifact |
| C-03 | Recommendation with rationale | **PASS** | Phase 11 dual-signature form names chosen option, 2-3 sentence rationale, CONDITIONS block with ≥2 conditions |
| C-04 | Decision framing | **PASS** | Phase 3 PM frame appears before Phase 5 options; THE QUESTION + WHY NOW are required fields |

**Essential: 4/4 → 60.00**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 explicitly lists found artifacts by name/finding; absence acknowledged with inline assessment — not deferred to recommendation |
| C-06 | Dual-role participation | **PASS** | Architect owns Phase 2 (constraint inventory), PM owns Phase 3 (decision frame); both sign Phase 11 with structurally distinct blocks |
| C-07 | Structured comparison | **PASS** | Phase 7 matrix: columns = all options, rows = effort/team control/adoption friction/time to value/risk P×I — no empty cells |

**Recommended: 3/3 → 30.00**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Assumption + risk registers | **PASS** | Phase 8 (A-NN with validation plans) + Phase 9 (R-NN with P/I/mitigation) — min 2 entries each |
| C-09 | Amend phase self-critique | **PASS** | Amend phase included; at least one actionable item per category present |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 is a dedicated discrete step before Phase 5 option generation — not a byproduct of recommendation prose |
| C-11 | Per-category amend taxonomy | **PASS** | Three-category structure: MISSING OPTION / UNWEIGHTED CRITERION / FOLLOW-UP — OWNER typed slot present in template |
| C-12 | Structural OWNER template enforcement | **PASS** | OWNER appears as typed slot in all three amend category templates — not instruction-only |
| C-13 | Split temporal anchor | **PASS** | Phase 3 carries TEMPORAL ANCHOR and INACTION CONSEQUENCE as separate typed fields; vague language explicitly prohibited in field description |
| C-14 | Amend entry deadline enforcement | **PASS** | V-01 axis specifically closes C-14 — DEADLINE typed slot present in all three amend category templates alongside OWNER |
| C-15 | F-row register with sign-off linkage | **PASS** | Phase 10 uses explicit 3-field template (FAILURE MODE / TRIGGER CONDITION / MITIGATION); Phase 11 PM and Architect blocks carry F-ROW ANCHOR as mandatory typed slot |
| C-16 | Numeric P×I with project-specific anchors | **PASS** | Phase 4 defines anchors before any option — each anchor names a concrete project-specific outcome at P=1/3/5 and I=1/3/5; L/M/H labels explicitly rejected |
| C-17 | Registers-before-recommendation ordering | **PASS** | Phase sequence: 8 (assumptions) → 9 (risks) → 10 (failure modes) → 11 (recommendation); recommendation PREREQUISITE note states registers must be complete first |
| C-18 | Front-loaded amendment table | **FAIL** | No amendment table initialized before Phase 1 — amend phase assembled retrospectively after document completion; C-18 fails by design |

**Aspirational: 10/11 → 9.09**

**V-01 Composite: 60.00 + 30.00 + 9.09 = 99.09**

---

## V-02: PREREQUISITE GATE Block

**Axis**: C-17 verifiability — typed checklist block immediately before Phase 11 confirming both assumption and risk registers are complete and sequenced correctly.

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Same as V-01 |
| C-02 | **PASS** | Same as V-01 |
| C-03 | **PASS** | PREREQUISITE GATE block precedes recommendation — verifiable single point confirming register completion |
| C-04 | **PASS** | Same as V-01 |

**Essential: 4/4 → 60.00**

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | **PASS** | Same as V-01 |
| C-06 | **PASS** | Same as V-01 |
| C-07 | **PASS** | Same as V-01 |

**Recommended: 3/3 → 30.00**

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Same as V-01 |
| C-09 | **PASS** | Same as V-01 |
| C-10 | **PASS** | Same as V-01 |
| C-11 | **PASS** | Same as V-01 |
| C-12 | **PASS** | Same as V-01 |
| C-13 | **PASS** | Same as V-01 |
| C-14 | **PASS** | Same as V-01 — DEADLINE in all three amend templates |
| C-15 | **PASS** | Same as V-01 — F-ROW ANCHOR present in sign-off |
| C-16 | **PASS** | Same as V-01 |
| C-17 | **PASS** | PREREQUISITE GATE typed checklist makes ordering auditable at a single block — strongest C-17 implementation to date; document scan no longer required |
| C-18 | **FAIL** | No front-loaded amendment table — C-18 fails by design |

**Aspirational: 10/11 → 9.09**

**V-02 Composite: 60.00 + 30.00 + 9.09 = 99.09**

---

## V-03: Inertia-Forward Framing

**Axis**: Option 0 elevated to INERTIA BASELINE with INERTIA COST (P×I per sprint); alternatives must name INERTIA OFFSET (sprints to crossover). Tests decision-frame quality independently of structural enforcement criteria.

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Option 0 as INERTIA BASELINE still satisfies do-nothing requirement; ≥3 alternatives present |
| C-02 | **PASS** | All option fields present; INERTIA COST/OFFSET are additional fields, not substitutes |
| C-03 | **PASS** | Recommendation present with rationale |
| C-04 | **PASS** | Decision framing complete before options |

**Essential: 4/4 → 60.00**

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | **PASS** | Scout inventory step retained |
| C-06 | **PASS** | Dual-role participation retained |
| C-07 | **PASS** | Comparison matrix retained; INERTIA OFFSET adds dimension |

**Recommended: 3/3 → 30.00**

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Registers present |
| C-09 | **PASS** | Amend phase present |
| C-10 | **PASS** | Dedicated inventory step retained |
| C-11 | **PASS** | Three-category amend taxonomy retained |
| C-12 | **PASS** | OWNER typed slot in all amend templates |
| C-13 | **PASS** | TEMPORAL ANCHOR + INACTION CONSEQUENCE split retained |
| C-14 | **PASS** | DEADLINE typed slot in all amend templates |
| C-15 | **FAIL** | Inertia framing axis omits Phase 10 F-row register entirely — no F-NN entries, no F-ROW ANCHOR in sign-off; C-15 fails by design |
| C-16 | **PASS** | Phase 4 anchors present; INERTIA COST uses same P×I numeric model |
| C-17 | **PASS** | Register sequence maintained before recommendation |
| C-18 | **FAIL** | No front-loaded amendment table — C-18 fails by design |

**Aspirational: 9/11 → 8.18**

**V-03 Composite: 60.00 + 30.00 + 8.18 = 98.18**

---

## V-04: Combined (V-01 + V-02 + project-specific anchors)

**Axis**: Integration test — F-row 3-field template (V-01) + PREREQUISITE GATE block (V-02) + explicit Phase 4 project-specific anchor definitions. Single controlled discriminator vs. V-05: C-18.

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Same as V-01 |
| C-02 | **PASS** | Same as V-01 |
| C-03 | **PASS** | Both PREREQUISITE GATE and F-ROW ANCHOR present in Phase 11 |
| C-04 | **PASS** | Same as V-01 |

**Essential: 4/4 → 60.00**

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | **PASS** | Same as V-01 |
| C-06 | **PASS** | Same as V-01 |
| C-07 | **PASS** | Same as V-01 |

**Recommended: 3/3 → 30.00**

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Same as V-01 |
| C-09 | **PASS** | Same as V-01 |
| C-10 | **PASS** | Same as V-01 |
| C-11 | **PASS** | Same as V-01 |
| C-12 | **PASS** | Same as V-01 |
| C-13 | **PASS** | Same as V-01 |
| C-14 | **PASS** | Same as V-01 |
| C-15 | **PASS** | V-01 F-row template + V-02 PREREQUISITE GATE combine — strongest C-15 implementation; F-ROW ANCHOR in both PM and Architect sign-off blocks |
| C-16 | **PASS** | Phase 4 anchor definitions most explicit version — named project-specific outcomes at each level, not generic categories |
| C-17 | **PASS** | PREREQUISITE GATE enforces ordering; Phases 8/9 structurally precede Phase 11 |
| C-18 | **FAIL** | No front-loaded amendment table — single designed discriminator vs. V-05 |

**Aspirational: 10/11 → 9.09**

**V-04 Composite: 60.00 + 30.00 + 9.09 = 99.09**

---

## V-05: Full Integration + STRUCTURE GUARD Cascade

**Axis**: V-04 + front-loaded amendment table initialized before Phase 1 with T-GUARD cascade trigger rules. All 5 new criteria covered simultaneously. Golden candidate.

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Same as V-04 |
| C-02 | **PASS** | Same as V-04 |
| C-03 | **PASS** | Same as V-04 |
| C-04 | **PASS** | Same as V-04 |

**Essential: 4/4 → 60.00**

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | **PASS** | Same as V-04 |
| C-06 | **PASS** | Same as V-04 |
| C-07 | **PASS** | Same as V-04 |

**Recommended: 3/3 → 30.00**

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Same as V-04 |
| C-09 | **PASS** | Amendment table populated during writing — self-critique is live, not retrospective |
| C-10 | **PASS** | Same as V-04 |
| C-11 | **PASS** | Three-category taxonomy; T-GUARD fires if any category is empty at completion |
| C-12 | **PASS** | OWNER typed slot enforced; T-GUARD fires if slot is absent on any entry |
| C-13 | **PASS** | Same as V-04 |
| C-14 | **PASS** | DEADLINE typed slot enforced; T-GUARD fires if slot is absent or "TBD" |
| C-15 | **PASS** | Same as V-04; T-GUARD fires if F-ROW ANCHOR slot is empty in either sign-off block |
| C-16 | **PASS** | Same as V-04; T-GUARD fires if L/M/H labels appear instead of P×I numerics |
| C-17 | **PASS** | PREREQUISITE GATE still present; T-GUARD fires if gate is skipped or incomplete |
| C-18 | **PASS** | Amendment table initialized as first artifact — before Phase 1 option generation. Trigger rules (T-01 through T-GUARD) name which criterion fires under which condition. At completion: either populated rows (violations caught) or explicitly empty rows (no violations) — both are valid, neither is silent |

**Aspirational: 11/11 → 10.00**

**V-05 Composite: 60.00 + 30.00 + 10.00 = 100.00**

---

## Score Summary

| Variation | Essential /60 | Recommended /30 | Aspirational /10 | **Total** | Designed Fails |
|-----------|--------------|-----------------|-----------------|-----------|----------------|
| V-05 | 60.00 | 30.00 | 10.00 | **100.00** | — |
| V-01 | 60.00 | 30.00 | 9.09 | **99.09** | C-18 |
| V-02 | 60.00 | 30.00 | 9.09 | **99.09** | C-18 |
| V-04 | 60.00 | 30.00 | 9.09 | **99.09** | C-18 |
| V-03 | 60.00 | 30.00 | 8.18 | **98.18** | C-15, C-18 |

---

## Excellence Signals (V-05)

### 1. Live enforcement vs. retrospective assembly
The front-loaded amendment table (C-18) shifts the amend phase from editorial commentary appended after writing to a live enforcement artifact that precedes and governs writing. The table is initialized with named trigger rules before any option exists, so coverage failures are caught during writing, not after. This is the single highest-leverage structural shift in R4 — retrospective amends can only describe what was missed; prospective amends change what gets written.

### 2. Named trigger IDs make every amendment traceable
T-GUARD cascade assigns a named ID (T-01 through T-GUARD) to each structural requirement. Every row in the amendment table references its source trigger by ID. This eliminates the coverage ambiguity from R3 (where gate citations drifted between C-12 and C-13) — each amendment entry is anchored to a specific named rule, not a prose interpretation.

### 3. PREREQUISITE GATE as single auditable checkpoint for C-17
Rather than requiring a document scan to verify register ordering, V-02/V-04/V-05 introduce a typed checklist block immediately before Phase 11. A reviewer can confirm C-17 compliance at one point without tracing document sequence. The gate also makes the causal claim explicit: registers precede recommendation because the gate forces completion, not merely because they appear earlier.

### 4. F-ROW ANCHOR as structural recommendation anchor
Elevating the F-row linkage from a prose instruction ("at least one F-row referenced") to a typed slot (F-ROW ANCHOR) in both PM and Architect sign-off blocks makes C-15 satisfiable with certainty. The model cannot complete Phase 11 without naming an F-row ID — the recommendation is structurally tethered to the failure mode that most directly invalidates it.

### 5. Explicit FAILURE MODE / TRIGGER CONDITION / MITIGATION labels eliminate inference
R3's Observable Event / Invalidates / Fallback table required a reviewer to infer that Observable Event maps to trigger condition and Fallback maps to mitigation. V-01's three-field template uses C-15's own vocabulary — the field names and the criterion names match. No inference required; scoring becomes deterministic.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["front-loaded amendment table as live enforcement artifact (C-18 closes prospective gap)", "named trigger IDs (T-01 through T-GUARD) make each amendment row traceable to source rule by ID", "PREREQUISITE GATE as single auditable checkpoint eliminates document-scan requirement for C-17", "F-ROW ANCHOR as typed slot in dual sign-off blocks makes recommendation structurally tethered to failure modes"]}
```
