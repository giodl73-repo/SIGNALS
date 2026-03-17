## flow-lifecycle — Round 19 Scorecard (rubric v19)

---

### Scoring Basis

Denominator: 56 | Aspirational: 48 | All essential must PASS

Scoring: PASS = 1pt · PARTIAL = 0.5pt · FAIL = 0pt

---

### Key Discriminating Criteria (where variations differ)

**C-11 (Role-First Anchoring):** C-11 requires roles established before states are named + ≥1 domain-title example in column header. All variations place Role Registry before State Trace (Step 1 precedes Step 3) and all column headers include concrete examples. → **PASS all**.

**C-34 (Pre-Declaration Role Registry):** AC-03 checks whether a role registry appears before FM-ID PROTOCOL, with domain-qualified titles and Exception Handler designations locked in before the SQ Declaration is authored.
- V-01: Pre-Declaration Pass block present before FM-ID PROTOCOL → **PASS**
- V-02: No pre-declaration block; Role Registry first appears at STEP 1 (after SQ Declaration) → **FAIL**
- V-03: No pre-declaration block; Role Registry at STEP 1 → **FAIL**
- V-04: "Start Here: Domain Role Registry" appears before FM-ID Guidance → **PASS**
- V-05: Pre-Declaration Pass block present → **PASS**

**C-29 (Decision Condition Threshold-Type Taxonomy):** Header must operationalize qualifying value types by naming ≥2 category names or providing a quoted example with operator + unit.
- V-01: Full list ("dollar amount, day count, retry count, unit quantity") + quoted example → **PASS**
- V-02: Full list + quoted example → **PASS**
- V-03: Abbreviated: "threshold-type category AND quoted example" — no named category list, no quoted example inline → **PARTIAL**
- V-04: Full list + quoted example ("Invoice value > $10,000") → **PASS**
- V-05: Full list + quoted example → **PASS**

**C-31 (Dual-Mechanism Threshold Operationalization):** Requires BOTH named category list AND quoted example in same header.
- V-01/V-02/V-04/V-05: Both mechanisms present → **PASS**
- V-03: Neither present inline in header → **FAIL**

**C-55 (Gate Defect Inline Enumeration — TARGET):**
- V-01: Gate enumerates: "an unterminated path (D-01), an uncertified exception handler (D-02), an unresolvable decision owner (D-03)…" — ≥3 named categories with D-IDs → **PASS**
- V-02: Same gate structure → **PASS**
- V-03: Same gate structure → **PASS**
- V-04: Conversational gate: "an unterminated path, an uncertified exception handler, an unresolvable decision owner…" — plain prose, no D-IDs, ≥3 named categories → **PASS**
- V-05: Same as V-01 structure → **PASS**

**C-56 (Escape Code Column Eligibility Operationalization — TARGET):**

Step 1 LT-ID Trace header:
- V-01: "SECONDARY (use only when role has no LT-bound trigger, naming why this role exists without any LT anchor)" — eligibility condition present → **PASS**
- V-02: "SECONDARY (use only when role exists outside all LT scopes, naming why this role exists without any LT-bound trigger)" → **PASS**
- V-03: "SECONDARY (use only when role exists outside all LT scopes, naming why this role exists without any LT-bound trigger)" → **PASS**
- V-04: "write SECONDARY -- but only when role has no LT-bound trigger at all, and explain why it exists outside any trigger scope" → **PASS**
- V-05: Same as V-01 → **PASS**

Step 2 Entry Trigger header:
- All five variations: "DERIVED (use only when this phase boundary results from multiple LT-IDs combining, naming which LT-IDs and combination logic)" → **PASS all**

---

### Per-Variation Full Scores

#### V-01 (Role Sequence: Pre-Declaration + C-55 TARGET)

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 1/1 PASS |
| C-35–C-41 (prior floor) | 7/7 PASS |
| C-42–C-54 (prior floor) | 13/13 PASS |
| **C-55** | 1/1 PASS |
| **C-56** | 1/1 PASS |
| **Total** | **56/56** |

Notable: Clean single-axis test — gate enumeration change does not perturb pre-declaration axis. C-56 holds stable from R18 V-01 (eligibility conditions already present in column headers). AC-29/AC-30 both PASS.

---

#### V-02 (Column Contract + C-55 TARGET + C-56 TARGET)

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 0/1 **FAIL** — no pre-declaration block |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 | 13/13 PASS |
| **C-55** | 1/1 PASS |
| **C-56** | 1/1 PASS |
| **Total** | **55/56** |

Note: Column Contract Field column carries leading-clause tokens in definition layer — C-51/C-53 PASS at definition level. Fill Table SQ-Field cells are bare labels but criterion scope applies to the definition cells. AC-03 absent because pre-declaration structure is absent.

---

#### V-03 (Phase-First Framing + GATE SQ + C-55 TARGET + C-56 TARGET)

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 (excl. C-29, C-31) | 23/23 PASS |
| C-29 (threshold taxonomy) | 0.5/1 **PARTIAL** — "threshold-type category AND quoted example" without named list |
| C-31 (dual-mechanism) | 0/1 **FAIL** — no category list, no quoted example inline in header |
| C-34 (pre-declaration) | 0/1 **FAIL** |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 (C-54 enhanced via GATE SQ) | 13/13 PASS |
| **C-55** | 1/1 PASS |
| **C-56** | 1/1 PASS |
| **Total** | **53.5/56** |

Note: Phase Framing block does not interact with C-55/C-56 (confirmed). GATE SQ is a C-54 enhancement. Decision Condition header abbreviation is the only structural regression from R18 V-03.

---

#### V-04 (Conversational Register + Role Sequence + C-55 TARGET + C-56 TARGET)

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 1/1 PASS |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 | 13/13 PASS |
| **C-55** | 1/1 PASS — plain prose enumeration satisfies criterion |
| **C-56** | 1/1 PASS — "use this when..." phrasing satisfies criterion |
| **Total** | **56/56** |

Key finding: Conversational phrasing is criterion-neutral. The gate text ("an unterminated path, an uncertified exception handler, an unresolvable decision owner…") satisfies C-55 because the criterion requires named categories, not formal D-ID notation. Eligibility conditions in "use only when…" plain English satisfy C-56. Gate D "An uncertified handler means the artifact must be discarded" satisfies C-45 via semantic equivalence.

---

#### V-05 (Full Combination: R18 Floor + AC-29/AC-30/D-19/D-20 Formalization)

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 1/1 PASS |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 | 13/13 PASS (GATE SQ + inertia-first + dual-position C-53) |
| **C-55** | 1/1 PASS — HOLD/PASS confirmed; R18 V-05 gate already enumerated inline |
| **C-56** | 1/1 PASS — HOLD/PASS confirmed; column headers already carried eligibility |
| **Total** | **56/56** |

Hypothesis confirmed: AC-29 and AC-30 formalization is score-neutral for the full floor. The explicit taxonomy entries D-19/D-20 close the gap between "passes these criteria" and "schema explicitly verifies them." No structural changes needed to reach full denominator.

---

### Ranking

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| **1** | **V-05** | **56/56** | YES | Full floor + explicit C-55/C-56 formalization; richest implementation |
| **1** | **V-01** | **56/56** | YES | Clean single-axis C-55 probe; minimal change from R18 V-01 |
| **1** | **V-04** | **56/56** | YES | Confirms register-neutrality of C-55/C-56 |
| 4 | V-02 | 55/56 | YES | Loses C-34; Column Contract format otherwise clean |
| 5 | V-03 | 53.5/56 | YES | Loses C-34 + C-29 PARTIAL + C-31 FAIL; Decision Condition header abbreviation is the regression |

Three-way tie at 56/56. V-05 ranked first among equals by implementation depth (GATE SQ, inertia-first ordering, dual-position C-53 coverage, field-type taxonomy in Protocol).

---

### Excellence Signals from Top-Scoring Variations

**1. C-55 inline enumeration is register-neutral.** V-04's conversational gate — listing categories in plain prose without D-ID codes — satisfies C-55 identically to V-01/V-05's formal enumeration. The criterion is scoped to "named categories inline within the gate sentence," not to notation format. Implication: any future variation can satisfy C-55 regardless of phrasing register, provided ≥3 category names appear inside the gate sentence itself.

**2. C-56 eligibility conditions are column-header-scoped and format-independent.** All three structural formats (pre-declaration row, Column Contract, conversational plain-English header) successfully carry escape code eligibility conditions without interaction with surrounding SQ Declaration format. The eligibility condition is a header-level property only — it depends on what the specific column header says, not on what precedes or follows it in the document. V-02 confirms Column Contract format does not disrupt this; V-04 confirms plain-English "use this when…" phrasing is valid.

**3. The full-floor formalization pattern is proven score-neutral.** V-05 confirms that explicitly adding AC-29/AC-30 to Coverage Scan and D-19/D-20 to the Defect Type Taxonomy neither adds nor removes passing behavior from a variation that already structurally satisfies the criteria. This validates the formalization strategy: prior round winners can be upgraded to explicitly verify new criteria without structural regression.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate defect inline enumeration is register-neutral — plain prose category names satisfy C-55 as effectively as formal D-ID notation; criterion is scoped to named categories inside the gate sentence, not to notation format", "escape code eligibility conditions are fully column-header-scoped and format-independent from surrounding SQ Declaration structure — any format carrying the eligibility clause in the column header satisfies C-56"]}
```
