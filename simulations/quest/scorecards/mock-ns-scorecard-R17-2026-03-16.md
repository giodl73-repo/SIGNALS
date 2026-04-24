Now I have all five variations. Let me score each one.

---

## R17 Scoring — mock-ns (rubric v17, max 154)

### Criteria Key (C-44/C-45 focus)

| Criterion | What it tests | Points |
|-----------|---------------|--------|
| C-15 | 3+ operation types anywhere in CONSTRAINT block | 2 (aspirational) |
| C-21 | 4+ operation types in CONSTRAINT block | 2 (aspirational) |
| C-24 | 5 operation types in CONSTRAINT block | 2 (aspirational) |
| C-44 | Each step ID paired inline with operation-type annotation (adjacent parenthetical or equivalent co-located form) | 2 (aspirational) |
| C-45 | S-3 sub-steps enumerated individually (S-3.1, S-3.2, S-3.3) — not collapsed to S-3 | 2 (aspirational) |

---

### V-01 — CONSTRAINT form: step-IDs-only

**CONSTRAINT text:** `Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is written.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-44 | **FAIL** | Step IDs S-1, S-2, S-3.1, S-3.2, S-3.3 present; zero per-ID operation-type annotations. No parenthetical, no em-dash, no equivalent co-located form. |
| C-15 | **FAIL** | 0 operation-type names in CONSTRAINT block; 0 < 3. |
| C-21 | **FAIL** | 0 < 4. Co-fires with C-15, C-24, C-44. |
| C-24 | **FAIL** | 0 < 5. |
| C-45 | **PASS** | S-3.1, S-3.2, S-3.3 each appear as separately named step IDs. |
| All other criteria | **PASS** | Lifecycle complete, propagation table correct, flag immutability chain present, P-0 tokens intact. |

**Score: 154 − 2(C-44) − 2(C-15) − 2(C-21) − 2(C-24) = 142/154**
Hypothesis confirmed.

---

### V-02 — CONSTRAINT annotation placement: trailing group

**CONSTRAINT text:** `Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is written. Operations blocked: skill selection, category lookup, carry, compliance detection, flag computation.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-44 | **FAIL** | Five operation types are present in the CONSTRAINT block, but they appear in a trailing sentence ("Operations blocked: …") — not co-located inline per step ID. None of S-1/S-2/S-3.1/S-3.2/S-3.3 carries its own adjacent annotation. Trailing group ≠ adjacent parenthetical or equivalent co-located form. |
| C-15 | **PASS** | 5 operation-type names present in CONSTRAINT block (skill selection, category lookup, carry, compliance detection, flag computation). 5 ≥ 3. |
| C-21 | **PASS** | 5 ≥ 4. |
| C-24 | **PASS** | 5 ≥ 5. |
| C-45 | **PASS** | S-3.1, S-3.2, S-3.3 each named individually in step-ID list. |
| All other criteria | **PASS** | Lifecycle complete, propagation table correct. |

**Score: 154 − 2(C-44) = 152/154**
Hypothesis confirmed. **Key finding: C-44 fires independently of C-15/C-21/C-24.** Five types present, count criteria pass — but form criterion fails because co-location is not per-ID inline.

---

### V-03 — CONSTRAINT S-3 granularity: collapsed

**CONSTRAINT text:** `Do not perform S-1 (skill selection), S-2 (category lookup), or S-3 (flag computation) until this step's emit is written.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-44 | **PASS** | Each named step ID (S-1, S-2, S-3) carries an adjacent parenthetical: "(skill selection)", "(category lookup)", "(flag computation)". Per-ID co-location satisfied for all three present IDs. |
| C-45 | **FAIL** | S-3 appears as a single collapsed reference; S-3.1 (carry), S-3.2 (compliance detection), and S-3.3 (flag computation) are not separately enumerated. PROPAGATION table marks all three sub-step CONSTRAINT references as "S-3 (flag computation) [collapsed]". |
| C-15 | **PASS** | 3 operation types (skill selection, category lookup, flag computation). 3 ≥ 3. |
| C-21 | **FAIL** | 3 < 4. S-3 collapse reduces visible type count from 5 to 3. |
| C-24 | **FAIL** | 3 < 5. |
| All other criteria | **PASS** | S-5.0 verification table updated to use "S-3 (flag computation)" check strings — internally consistent for this variation; lifecycle otherwise complete. |

**Score: 154 − 2(C-45) − 2(C-21) − 2(C-24) = 148/154**
Hypothesis confirmed. **Key finding: S-3 collapse cascades — C-45 FAIL forces 3-type count, co-firing C-21 and C-24. C-15 survives (3 ≥ 3). C-44 passes because the three IDs that are named each carry annotations.**

---

### V-04 — CONSTRAINT annotation punctuation: em-dash

**CONSTRAINT text:** `Do not perform S-1 -- skill selection, S-2 -- category lookup, S-3.1 -- carry, S-3.2 -- compliance detection, or S-3.3 -- flag computation until this step's emit is written.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-44 | **PASS** | Each step ID is paired inline with its operation-type annotation via `--` (em-dash). The rubric admits "adjacent parenthetical **or equivalent co-located form**." Em-dash annotation is syntactically adjacent, immediately follows the step ID, and structurally binds annotation to ID in the same clause — satisfies equivalent co-located form. All five IDs annotated per-ID. |
| C-45 | **PASS** | S-3.1, S-3.2, S-3.3 each appear as individually annotated entries. |
| C-15 | **PASS** | 5 operation types named (carry, compliance detection, flag computation, skill selection, category lookup). |
| C-21 | **PASS** | 5 ≥ 4. |
| C-24 | **PASS** | 5 ≥ 5. |
| All other criteria | **PASS** | S-5.0 verification check table uses "S-3.1 -- carry", "S-3.2 -- compliance detection", "S-3.3 -- flag computation" — internally consistent. Lifecycle complete. |

**Score: 154/154**
Hypothesis confirmed. **Key finding: Em-dash satisfies the "equivalent co-located form" clause in C-44. The criterion tests per-ID pairing proximity, not parenthetical punctuation specifically. Punctuation form is flexible; structural adjacency is the requirement.**

---

### V-05 — Combined: golden CONSTRAINT + prose S-1/S-2 + declarative phrasing

**CONSTRAINT text:** `Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.`

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-44 | **PASS** | Golden parenthetical form — five step IDs each with adjacent parenthetical annotation. Canonical form. |
| C-45 | **PASS** | S-3.1 (carry), S-3.2 (compliance detection), S-3.3 (flag computation) individually enumerated. |
| C-15 | **PASS** | 5 types present. |
| C-21 | **PASS** | 5 ≥ 4. |
| C-24 | **PASS** | 5 ≥ 5. |
| All other criteria | **PASS** | S-1 uses prose format (namespace defaults listed in paragraph); S-2 uses paragraph form for skill lists; steps use "The step emits/reads/resolves…" declarative phrasing throughout. All these format and register variations are orthogonal to CONSTRAINT criteria. P-0 tokens intact. Propagation verification table uses "S-3.1 (carry)", "S-3.2 (compliance detection)", "S-3.3 (flag computation)" — MATCH on all fields. |

**Score: 154/154**
Hypothesis confirmed. Prose format and declarative phrasing register are confirmed independent of CONSTRAINT correctness. Format variations in step bodies do not affect C-44/C-45 or count criteria.

---

## Rankings

| Rank | Variation | Score | Failures |
|------|-----------|-------|---------|
| 1 | V-04 | **154/154** | none |
| 1 | V-05 | **154/154** | none |
| 3 | V-02 | 152/154 | C-44 |
| 4 | V-03 | 148/154 | C-45, C-21, C-24 |
| 5 | V-01 | 142/154 | C-44, C-15, C-21, C-24 |

---

## Questions Answered by R17

| Question | Answer |
|----------|--------|
| Can C-44 fire independently of C-15/C-21/C-24? | **Yes** (V-02). Five types present in CONSTRAINT block → count passes; all in trailing sentence → C-44 fails alone. |
| What is the first isolated canonical C-45 failure? | **V-03** — first variation where C-45 is the primary axis and C-44 passes. |
| Does S-3 collapse cascade to count failures? | **Yes** — collapse reduces type count from 5 to 3; C-45 + C-21 + C-24 co-fire; C-15 survives. |
| Does em-dash satisfy C-44? | **Yes** (V-04) — "equivalent co-located form" admits em-dash. |
| Are prose/declarative axes orthogonal to CONSTRAINT criteria? | **Confirmed** (V-05) — step body format and phrasing register do not affect C-44/C-45. |

---

## Excellence Signals (from V-04 and V-05)

**From V-04:** Punctuation flexibility in co-location — C-44's "equivalent co-located form" clause provides real coverage. Em-dash produces a distinct CONSTRAINT surface appearance from the golden parenthetical, yet satisfies the structural requirement (inline adjacency per ID). The criterion is form-agnostic at the punctuation level; what it enforces is proximity and pairing.

**From V-05:** Format-CONSTRAINT independence is total — prose paragraph format for S-1 and S-2, declarative "The step emits/reads/resolves…" register throughout, and the golden parenthetical CONSTRAINT are structurally separable. A variation can change any formatting axis without touching CONSTRAINT correctness.

---

```json
{"top_score": 154, "all_essential_pass": true, "new_patterns": ["Trailing-group annotation fails C-44 independently: when all 5 operation types appear in a follow-on sentence rather than paired per-ID inline, C-44 fires even though C-15/C-21/C-24 pass -- the count and co-location criteria are orthogonal", "S-3 collapse cascades to count failures: collapsing S-3.1/S-3.2/S-3.3 into a single S-3 entry reduces the visible type count from 5 to 3, co-firing C-45 with C-21 and C-24 while C-15 survives (3 >= 3 passes)", "Punctuation flexibility in co-location: em-dash satisfies C-44 equivalent co-located form clause -- the criterion enforces per-ID inline adjacency, not specifically parenthetical punctuation"]}
```
