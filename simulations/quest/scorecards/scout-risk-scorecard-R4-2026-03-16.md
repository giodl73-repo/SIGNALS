## scout-risk R4 — Quest Score Evaluation

### Scoring Methodology

Each criterion evaluated on prompt text alone (no trace artifact). Aspirational: 2=PASS, 1=PARTIAL, 0=FAIL.

---

## V-01 — Lifecycle Emphasis (C-17: FROM/TO prose template)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia first, mandatory | **PASS** | Phase 1 explicitly first, "Do not skip it. Do not move it." |
| C-02 | ≥3 dimensions | **PASS** | "at least one risk each from 3 or more of these dimensions" |
| C-03 | Risk anatomy complete | **PASS** | Severity + specific condition likelihood + concrete mitigation required for both inertia and dimensional |
| C-04 | Severity scale correct | **PASS** | "HIGH, MEDIUM, or LOW — nothing else" stated twice |
| C-05 | Mitigations specific | **PASS** | Read-back gate: "If two or more are generic non-actions, replace them" |
| C-06 | Dimension-labeled | **PASS** | "Dimension: which of the five it belongs to" per entry |
| C-07 | Likelihood qualified | **PASS** | "what specific condition or scenario triggers this risk — not just 'possible'" |
| C-08 | Priority ordered | **PASS** | "Sort dimensional risks from highest to lowest severity" |
| C-09 | ≥1 interdependency | **PASS (2)** | Phase 3 mandatory section, ≥3 named pairs required |
| C-10 | AMEND behavior | **PARTIAL (1)** | Phase 4 handles AMEND correctly; no live directive in base prompt |
| C-11 | Zero-generic | **PARTIAL (1)** | Gate replaces only if ≥2 generic — one generic may survive |
| C-12 | All likelihoods trigger-qualified | **PARTIAL (1)** | Direction to specify conditions but no syntactic enforcement for every entry |
| C-13 | Dedicated section ≥2 pairs | **PASS (2)** | "## Risk Interdependencies" heading mandatory, ≥3 pairs |
| C-14 | IF-THEN syntax | **FAIL (0)** | Likelihood is prose "what specific condition" — no IF-THEN template |
| C-15 | Type declared + contract fulfilled | **FAIL (0)** | No mitigation type vocabulary mentioned |
| C-16 | ≥3 named pairs | **PASS (2)** | "at least 3 named compound-risk pairings" enforced |
| C-17 | FROM/TO labels | **PASS (2)** | "escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY]" — explicit FROM/TO with enforcement note |
| C-18 | ≥3 distinct type classes | **FAIL (0)** | No type vocabulary or diversity gate |

**V-01 Composite: 60 + 30 + (2+1+1+1+2+0+0+2+2+0) = 101** — GOLDEN

---

## V-02 — Output Format (C-18: type diversity gate)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia first, mandatory | **PASS** | Step 1 mandatory, "Do not skip it. Do not move it." |
| C-02 | ≥3 dimensions | **PASS** | "Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline" |
| C-03 | Risk anatomy complete | **PASS** | Table schema enforces all fields; inertia format complete |
| C-04 | Severity scale correct | **PASS** | "Severity: HIGH / MEDIUM / LOW — no other values" in column definition |
| C-05 | Mitigations specific | **PASS** | Forbidden words list + "replace before proceeding" |
| C-06 | Dimension-labeled | **PASS** | Dimension column in table + "Dimension: Inertia" for row 0 |
| C-07 | Likelihood qualified | **PASS** | IF-THEN column header forces condition-qualified entries |
| C-08 | Priority ordered | **PASS** | "Sort rows by severity descending" |
| C-09 | ≥1 interdependency | **PARTIAL (1)** | Step 3 says "Note at least one interdependency" but body reads "note any risks that compound each other" — conditional phrasing, no enforcement heading |
| C-10 | AMEND behavior | **PARTIAL (1)** | Step 4 AMEND present; no live directive |
| C-11 | Zero-generic | **PARTIAL (1)** | Forbidden word list catches named phrases; other generic hedges outside the list could survive |
| C-12 | All likelihoods trigger-qualified | **PASS (2)** | "every cell in this column starts with 'IF' and ends with a concrete triggering scenario" — column header syntactically enforces all rows |
| C-13 | Dedicated section ≥2 pairs | **FAIL (0)** | Step 3 is a post-table note, no "## Risk Interdependencies" heading, no ≥2 count requirement |
| C-14 | IF-THEN syntax | **PASS (2)** | Column header "IF [condition], THEN risk activates" is the syntactic template for every likelihood cell |
| C-15 | Type declared + contract fulfilled | **FAIL (0)** | Type definitions provided but no sub-field contract enforcement — "Spike: [action sentence]" satisfies the column without Unknown/Time-box |
| C-16 | ≥3 named pairs | **FAIL (0)** | No dedicated section with count requirement |
| C-17 | FROM/TO labels | **FAIL (0)** | Step 3 format "escalates to [severity]" — only destination, no origin severity |
| C-18 | ≥3 distinct type classes | **PASS (2)** | Step 2b diversity gate: count distinct classes, replace entries if <3, explicit repair instruction |

**V-02 Composite: 60 + 30 + (1+1+1+2+0+2+0+0+0+2) = 99** — GOLDEN

---

## V-03 — Phrasing Register (C-17: tabular FROM/TO columns)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia first, mandatory | **PASS** | Step 1, mandatory, first |
| C-02 | ≥3 dimensions | **PASS** | "at least one risk each from 3 or more of these dimensions" |
| C-03 | Risk anatomy complete | **PASS** | Inertia and each dimensional risk require all fields |
| C-04 | Severity scale correct | **PASS** | "HIGH, MEDIUM, or LOW — nothing else" |
| C-05 | Mitigations specific | **PASS** | Type contract sub-fields make generic hedges "structurally impossible" |
| C-06 | Dimension-labeled | **PASS** | "Dimension: which of the five it belongs to" |
| C-07 | Likelihood qualified | **PASS** | "what specific condition or scenario triggers this risk — not just 'possible'" |
| C-08 | Priority ordered | **PASS** | "Sort dimensional risks from highest to lowest severity" |
| C-09 | ≥1 interdependency | **PASS (2)** | Step 4: "This section must contain at least one compound-risk pairing" with enforcement: "If you cannot find any... revise Step 2" |
| C-10 | AMEND behavior | **PARTIAL (1)** | Step 5 AMEND correct; no live directive |
| C-11 | Zero-generic | **PASS (2)** | Type contract rule: "fulfilling the sub-fields makes generic hedges structurally impossible" + Step 3 read-back verifies every contract |
| C-12 | All likelihoods trigger-qualified | **PARTIAL (1)** | "what specific condition or scenario" — directional, not IF-THEN syntactically enforced for every cell |
| C-13 | Dedicated section ≥2 pairs | **FAIL (0)** | Only "at least one" pairing required — below C-13's ≥2 threshold |
| C-14 | IF-THEN syntax | **FAIL (0)** | Likelihood is prose; no IF-THEN template in column header |
| C-15 | Type declared + contract fulfilled | **PASS (2)** | Sub-fields required as named outputs; "A Spike without a named unknown and time-box is incomplete"; Step 3 read-back enforces compliance |
| C-16 | ≥3 named pairs | **FAIL (0)** | Only ≥1 pair required in interdependency section |
| C-17 | FROM/TO labels | **PASS (2)** | Interdependency table has separate "From Severity" and "To Severity" columns — structural split makes empty cells visible; "From Severity and To Severity are separate required fields — a row without both is incomplete" |
| C-18 | ≥3 distinct type classes | **FAIL (0)** | No diversity gate; no count requirement |

**V-03 Composite: 60 + 30 + (2+1+2+1+0+0+2+0+2+0) = 100** — GOLDEN

> **Deviation from author projection**: Author scores V-03 at 98, setting C-09=0. My reading: Step 4 uses "must contain" language with explicit back-pressure enforcement, which satisfies C-09 PASS. Score is 100, not 98.

---

## V-04 — Lifecycle + Output Format (C-17 + C-18 + C-15 fix)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia first, mandatory | **PASS** | Step 1 mandatory, first |
| C-02 | ≥3 dimensions | **PASS** | "Cover at least 3 of" |
| C-03 | Risk anatomy complete | **PASS** | All fields enforced by table + inertia format |
| C-04 | Severity scale correct | **PASS** | "only HIGH, MEDIUM, or LOW — no numbers, percentages, or invented labels" |
| C-05 | Mitigations specific | **PASS** | Type contract + forbidden words gate |
| C-06 | Dimension-labeled | **PASS** | Dimension column in table |
| C-07 | Likelihood qualified | **PASS** | IF-THEN column header |
| C-08 | Priority ordered | **PASS** | "Sort rows by severity descending" |
| C-09 | ≥1 interdependency | **PASS (2)** | Step 3 mandatory, ≥3 pairs |
| C-10 | AMEND behavior | **PARTIAL (1)** | Step 5 handles AMEND; no live directive |
| C-11 | Zero-generic | **PASS (2)** | Type contract sub-fields make generic structurally impossible + forbidden words gate |
| C-12 | All likelihoods trigger-qualified | **PASS (2)** | IF-THEN column header; "every cell begins with 'IF'" — scanning enforced in Step 4 self-check |
| C-13 | Dedicated section ≥2 pairs | **PASS (2)** | "## Risk Interdependencies" heading, ≥3 pairs |
| C-14 | IF-THEN syntax | **PASS (2)** | IF-THEN column header enforces syntactic form |
| C-15 | Type declared + contract fulfilled | **PASS (2)** | Sub-fields promoted to required named outputs: "A Spike without a named unknown and time-box is incomplete" — same V-05 wording that proved C-15 PASS in R3 |
| C-16 | ≥3 named pairs | **PASS (2)** | "at least 3 named compound-risk pairings" in Step 3 |
| C-17 | FROM/TO labels | **PASS (2)** | "escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY]" + self-check item 11: "Every interdependency pair states both FROM severity and TO severity" |
| C-18 | ≥3 distinct type classes | **PASS (2)** | Step 2b diversity gate with explicit repair instruction + self-check item 9 |

**V-04 Composite: 60 + 30 + (2+1+2+2+2+2+2+2+2+2) = 109** — GOLDEN

---

## V-05 — Full Integration (R3 V-05 base + FROM/TO + diversity gate)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia first, mandatory | **PASS** | STEP 1 first, "Write the inertia risk before anything else" |
| C-02 | ≥3 dimensions | **PASS** | "Cover at least 3 of the 5 dimensions" |
| C-03 | Risk anatomy complete | **PASS** | All fields required via format spec and table |
| C-04 | Severity scale correct | **PASS** | "Severity values are only HIGH, MEDIUM, or LOW — no numbers, percentages" in self-check |
| C-05 | Mitigations specific | **PASS** | Type contract + forbidden text gate — sub-fields make generic structurally impossible |
| C-06 | Dimension-labeled | **PASS** | Dimension column; Dimension: Inertia for row 0 |
| C-07 | Likelihood qualified | **PASS** | IF-THEN column header |
| C-08 | Priority ordered | **PASS** | "sorted by severity descending after inertia" |
| C-09 | ≥1 interdependency | **PASS (2)** | STEP 3 mandatory, ≥3 pairs, enforcement rule |
| C-10 | AMEND behavior | **PARTIAL (1)** | STEP 5 AMEND correct; no live directive |
| C-11 | Zero-generic | **PASS (2)** | Type contract sub-fields + diversity rule + forbidden text gate — "monitor closely cannot satisfy any type contract" explicit |
| C-12 | All likelihoods trigger-qualified | **PASS (2)** | "Likelihood rule — column header is the template" with explicit: "Bare probability labels cannot satisfy a column that begins with 'IF'" |
| C-13 | Dedicated section ≥2 pairs | **PASS (2)** | "## Risk Interdependencies" heading, ≥3 pairs, enforcement |
| C-14 | IF-THEN syntax | **PASS (2)** | Column header is the template; bare labels explicitly excluded |
| C-15 | Type declared + contract fulfilled | **PASS (2)** | "A mitigation is only complete when its named sub-fields are filled in"; each type's sub-fields listed as required outputs |
| C-16 | ≥3 named pairs | **PASS (2)** | "List at least 3 compound-risk pairings" in STEP 3 |
| C-17 | FROM/TO labels | **PASS (2)** | "escalates from [CURRENT SEVERITY of Risk B] to [NEW SEVERITY]" + "A pairing stating only 'escalates to HIGH' without naming the origin severity is incomplete" + self-check item 11 |
| C-18 | ≥3 distinct type classes | **PASS (2)** | "Type diversity rule" in STEP 2 — count after table, replace if <3 distinct classes, with repair logic |

**V-05 Composite: 60 + 30 + (2+1+2+2+2+2+2+2+2+2) = 109** — GOLDEN

---

## Score Summary

| Rank | ID | Essential | Rec | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | **Total** | Golden |
|------|-----|-----------|-----|------|------|------|------|------|------|------|------|------|------|-----------|--------|
| 1 | **V-04** | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **109** | YES |
| 1 | **V-05** | 60 | 30 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **109** | YES |
| 3 | V-01 | 60 | 30 | 2 | 1 | 1 | 1 | 2 | 0 | 0 | 2 | 2 | 0 | **101** | YES |
| 4 | V-03 | 60 | 30 | 2 | 1 | 2 | 1 | 0 | 0 | 2 | 0 | 2 | 0 | **100** | YES |
| 5 | V-02 | 60 | 30 | 1 | 1 | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 2 | **99** | YES |

All five variations are GOLDEN. All essential criteria pass across all variations.

**Score deviations from author projection:**
- V-02: 99 vs projected 98 — C-09 scored PARTIAL (1) vs FAIL (0): "Note at least one interdependency" is instructed, but "note any" body is conditional; PARTIAL is more accurate than FAIL
- V-03: 100 vs projected 98 — C-09 scored PASS (2) vs FAIL (0): Step 4 uses "must contain" + "revise Step 2" back-pressure; this is mandatory, not optional

---

## Excellence Signals (V-04 and V-05)

**1. Sub-field promotion to required named outputs (C-15 → C-11 chain)**
Both variations state "A Spike without a named unknown and time-box is incomplete" as a structural rule, not a description. This transforms sub-fields from optional context into enforced outputs — and as a side effect makes generic hedges structurally impossible (generic text cannot fill "Unknown: [what]").

**2. FROM/TO severity-transition pair with incompleteness rule**
The enforcement note "A pairing stating only 'escalates to HIGH' without naming the origin severity is incomplete" signals to the model exactly what partial compliance looks like and names it as a failure. This asymmetric negative example is what distinguishes V-04/V-05 from V-01's prose template (which only describes the desired form, not the failing form).

**3. Post-generation detect-and-repair gate (C-18)**
The diversity gate fires after the table is fully generated — count, then repair. This is a different pattern than up-front constraints: the model commits to a table, then audits it, then corrects. This separates generation from verification, which reduces backpressure during the generation pass and lets the repair pass operate on a complete register.

**4. Self-check as constraint closure**
The numbered checklist in STEP 4 / Step 4 captures every structural obligation in one scannable location. C-17 and C-18 each appear as explicit self-check items, so any failure on either is surfaced by the model's own verification step before the artifact is written.

---

```json
{"top_score": 109, "all_essential_pass": true, "new_patterns": ["FROM/TO severity-transition pair with named-failure incompleteness rule: stating only the destination is explicitly labeled incomplete, not just absent from the template", "Post-generation detect-and-repair gate: generate the full table first, count distinct type classes, replace entries if below threshold — separates generation from verification"]}
```
