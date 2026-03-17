# Quest Score — scout-size R1

## Evaluation Method

Five variations scored against the 10-criterion rubric. V-01's full prompt text was not included in the provided artifact (only hypothesis + description available); it is evaluated from described structure. V-02 through V-05 scored from full prompt text.

---

## V-01 — Inertia-First

*Note: Full prompt not available — assessed from described structure: INERTIA CHECK FIRST → surface area → complexity tier → team+timeline → confidence → signal boundary.*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Surface area section explicitly in flow; named integration points implied |
| C-02 | Complexity tier on-scale | PASS | Complexity tier section; LOW/MEDIUM/HIGH/XL vocabulary expected in standard section |
| C-03 | Inertia check present | PASS | Structural opening requirement — strongest C-03 of all variants |
| C-04 | Confidence with basis | PARTIAL | Confidence section closes prompt; basis requirement not confirmed from description alone |
| C-05 | Signal boundary respected | PASS | Signal boundary warning closes prompt |
| C-06 | Specialist types named | UNCERTAIN | Team section present; whether specialist-not-headcount is explicit is unknown |
| C-07 | Timeline as sprint range | UNCERTAIN | Timeline section present; whether sprint range is explicit is unknown |
| C-08 | Primary driver identified | UNCERTAIN | Complexity section present; whether primary driver is explicit is unknown |
| C-09 | Sensitivity: tier up/down | FAIL | Not described as part of this variant |
| C-10 | Confidence calibration | FAIL | Not described as part of this variant |

**Scoring (conservative, single-axis ordering variant):**
- Essential: 5/5 = 60 (C-04 given benefit of doubt)
- Recommended: 2/3 = 20 (C-08 likely missing as explicit requirement)
- Aspirational: 0/2 = 0
- **Composite: 80**

*Golden: passes essential ✓, composite ≥ 80 ✓ — but at minimum threshold.*

---

## V-02 — Table-Centric

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | TABLE 1 explicitly requires "Final row: Total: N integration points" |
| C-02 | Complexity tier on-scale | PASS | Column definition: "Tier (must be exactly LOW / MEDIUM / HIGH / XL)" — vocabulary is a column contract |
| C-03 | Inertia check present | PASS | INERTIA STATEMENT required before tables; names workaround + cost direction |
| C-04 | Confidence with basis | PASS | TABLE 4 columns: Level \| Basis \| Gap \| What Would Raise It |
| C-05 | Signal boundary respected | PASS | Explicit SIGNAL BOUNDARY section |
| C-06 | Specialist types named | PASS | TABLE 3 column "Specialist Type" — headcount-only would fail the column contract |
| C-07 | Timeline as sprint range | PASS | TABLE 3 column "Sprint Range" — point estimate can't hide in a column |
| C-08 | Primary driver identified | PASS | TABLE 2 columns: "Primary Driver \| Secondary Driver (optional)" |
| C-09 | Sensitivity: tier up/down | FAIL | TABLE 2 has no tier-up / tier-down rows; sensitivity not present |
| C-10 | Confidence calibration | PASS | TABLE 4 column "What Would Raise It" directly maps to C-10 |

**Scoring:**
- Essential: 5/5 = 60
- Recommended: 3/3 = 30
- Aspirational: 1/2 = 5
- **Composite: 95**

*Golden: yes.*

---

## V-03 — Driver-First Role Sequence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | STEP 2: "enumerate every integration point... Name each one. Total the count" |
| C-02 | Complexity tier on-scale | PASS | STEP 1: "Rate the tier: LOW / MEDIUM / HIGH / XL — exactly this vocabulary" |
| C-03 | Inertia check present | PASS | STEP 4: "Name the current workaround... cheaper, comparable, or more expensive" |
| C-04 | Confidence with basis | PASS | STEP 5: "HIGH / MEDIUM / LOW, with the basis... and the gap" |
| C-05 | Signal boundary respected | PASS | Explicit SIGNAL BOUNDARY section |
| C-06 | Specialist types named | PASS | STEP 3: "specialist disciplines required (not headcount — discipline names)" |
| C-07 | Timeline as sprint range | PASS | STEP 3: "sprint range" explicitly required |
| C-08 | Primary driver identified | PASS | STEP 1: "Name the one or two factors that most drive implementation complexity" |
| C-09 | Sensitivity: tier up/down | PARTIAL→FAIL | STEP 3 asks for sprint-range sensitivity (up/down), NOT tier sensitivity. Rubric requires tier up/down. Wrong dimension. |
| C-10 | Confidence calibration | PASS | STEP 5: "what specific information would materially raise the confidence level" |

**Scoring:**
- Essential: 5/5 = 60
- Recommended: 3/3 = 30
- Aspirational: 1/2 = 5 (C-09 fails on dimension mismatch)
- **Composite: 95**

*Golden: yes. Notable: C-09 is the closest near-miss — sprint sensitivity is present but wrong axis.*

---

## V-04 — Interrogative Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | Q2: "Name each one. How many total integration points?" |
| C-02 | Complexity tier on-scale | PASS | Q3: "(Use exactly this vocabulary.)" |
| C-03 | Inertia check present | PASS | Q1: "Name it specifically. Is building this feature cheaper, comparable, or more expensive?" |
| C-04 | Confidence with basis | PASS | Q6: "What do you know that supports that rating? What is unverified?" |
| C-05 | Signal boundary respected | PASS | Explicit SIGNAL BOUNDARY section |
| C-06 | Specialist types named | PASS | Q5: "(Name types, not headcount — e.g., '1 backend engineer, 1 frontend engineer, 0.5 PM')" |
| C-07 | Timeline as sprint range | PASS | Q5: "What is the sprint range for delivery?" |
| C-08 | Primary driver identified | PASS | Q3: "What one or two factors most drive that rating?" |
| C-09 | Sensitivity: tier up/down | PASS | Q4: "What single condition would push this tier one step up? What single condition would push it one step down?" — explicit, tier-specific |
| C-10 | Confidence calibration | PASS | Q6: "What specific investigation result would change it?" |

**Scoring:**
- Essential: 5/5 = 60
- Recommended: 3/3 = 30
- Aspirational: 2/2 = 10
- **Composite: 100**

*Golden: yes. Only variant (with V-05) to achieve full aspirational coverage.*

---

## V-05 — Inertia-First + Table + Sensitivity Block

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | PASS | TABLE 1: "Final row must be: \| Total \| — \| N integration points \|" |
| C-02 | Complexity tier on-scale | PASS | TABLE 2 row: "Complexity tier \| LOW / MEDIUM / HIGH / XL \| Primary driver" |
| C-03 | Inertia check present | PASS | REQUIRED OPENING with "mandatory; omitting it fails the signal" — strongest structural enforcement |
| C-04 | Confidence with basis | PASS | TABLE 3 rows: Confidence level, Basis, Open gap, What would raise it |
| C-05 | Signal boundary respected | PASS | Explicit SIGNAL BOUNDARY section |
| C-06 | Specialist types named | PASS | TABLE 2 row: "Team composition \| Specialist types + FTE signal \| e.g., '1 backend engineer, 0.5 PM'" |
| C-07 | Timeline as sprint range | PASS | TABLE 2 row: "Timeline signal \| Sprint range \| e.g., '3–5 sprints' — no calendar dates" |
| C-08 | Primary driver identified | PASS | TABLE 2 row: "Complexity tier... \| Primary driver (the factor most responsible)" |
| C-09 | Sensitivity: tier up/down | PASS | TABLE 2 rows: "Tier UP condition \| Required" and "Tier DOWN condition \| Required" — structurally mandatory |
| C-10 | Confidence calibration | PASS | TABLE 3 row: "What would raise it \| Specific investigation or result..." |

**Scoring:**
- Essential: 5/5 = 60
- Recommended: 3/3 = 30
- Aspirational: 2/2 = 10
- **Composite: 100**

*Golden: yes. C-09 promoted from aspirational to structurally required.*

---

## Rankings

| Rank | Variation | Composite | Golden | C-09 | C-10 |
|------|-----------|-----------|--------|------|------|
| 1 (tie) | V-04 Interrogative | 100 | ✓ | PASS | PASS |
| 1 (tie) | V-05 Combination | 100 | ✓ | PASS | PASS |
| 3 (tie) | V-02 Table-Centric | 95 | ✓ | FAIL | PASS |
| 3 (tie) | V-03 Driver-First | 95 | ✓ | PARTIAL | PASS |
| 5 | V-01 Inertia-First | ~80 | ✓ (est.) | FAIL | FAIL |

---

## Excellence Signals

**From V-04 — Interrogative Register:**
- **Question-as-criterion mapping** makes omission structurally impossible. Q4 maps directly to C-09 (tier up/down); you cannot answer Q4 without producing tier sensitivity. No other single-axis variant achieves this.
- **Wrong-dimension block**: interrogative phrasing forces specificity — "What single condition would push this *tier* one step up?" cannot be answered with sprint-range sensitivity (the failure mode V-03 hits).

**From V-05 — Combination:**
- **Aspirational criteria promoted to required table rows**: "Tier UP condition \| Required" in TABLE 2 makes C-09 impossible to skip — it's a row in a required table, not a section the model might include if it feels generous.
- **Explicit failure language at the opening**: "This section is mandatory; omitting it fails the signal" directly names the consequence. This is the strongest C-03 enforcement of any variant.
- **Multi-axis combination closes all four named failure modes simultaneously**: inertia-first (C-03), table structure (C-02 vocabulary + C-05 plan creep), sensitivity rows (C-09), calibration rows (C-04).

**Cross-variant pattern:**
- The gap between V-02/V-03 (95) and V-04/V-05 (100) is entirely C-09. The only way to reliably get C-09 is either (a) an explicit question naming the tier axis (V-04 Q4) or (b) a required table row naming tier-up and tier-down (V-05). Generic "sensitivity" language without naming the tier axis produces sprint sensitivity (V-03's failure mode) or silence (V-01/V-02).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Question-as-criterion mapping: each question targets one rubric criterion, making omission structurally impossible", "Aspirational criteria promoted to required table rows: embedding C-09 as labeled table rows with 'Required' annotation removes optionality", "Wrong-dimension sensitivity failure: prompts that ask for sensitivity without naming the tier axis get sprint-range sensitivity instead (V-03), not tier sensitivity"]}
```
