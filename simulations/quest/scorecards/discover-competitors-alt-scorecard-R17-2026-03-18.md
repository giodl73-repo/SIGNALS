# /quest:score — discover-competitors-alt R17 Scorecard

## Scoring Parameters

- **Essential:** C-01–C-05 | 12 pts each | 60 pts max
- **Recommended:** C-06–C-08 | 10 pts each | 30 pts max
- **Aspirational:** C-09–C-44 | 10/36 ≈ 0.278 pts each | 10 pts max
- **New criterion this round:** C-44 (bijective element-to-item mapping, exactly 4 items)

---

## Per-Variation Scoring

### V-01 — 4-Item Checklist, Item 1 Bundles Elements 1+4

**Architecture block form:** 4 items. Item 1 = manifest column name (element 1) + "Substitution/inheritance site" verbatim (element 4). Item 2 = element 2. Item 3 = element 3. Item 4 = independence confirmation note (non-C-42). Count = 4.

#### Essential Criteria (all shared gate structure)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | C0 introduced in dedicated section before any competitor row |
| C-02 | PASS | 3+ named competitors, each with explicit HIGH/MEDIUM/LOW threat |
| C-03 | PASS | C0 at row 0 in native markdown table |
| C-04 | PASS | Every finding references a named competitor row by table label |
| C-05 | PASS | AMEND section present and non-empty |

**Essential subtotal: 60/60**

#### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | TOKEN field names switching-cost/habit/workaround mechanism tied to specific C0 behavior |
| C-07 | PASS | WebSearch inline citation within at least one competitor entry |
| C-08 | PASS | AMEND entries each name input change + output effect |

**Recommended subtotal: 30/30**

#### Aspirational Criteria — Key Differentials

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Cross-dimensional whitespace requires competitive map + focus lens simultaneously |
| C-10 | PASS | Findings reference named competitor rows |
| C-11 | PASS | TOKEN propagates into downstream findings via `vs [TOKEN]:` lines |
| C-12 | PASS | AMEND evaluates inertia stability |
| C-13 | PASS | TOKEN assigned as copyable domain-specific identifier |
| C-14 | PASS | Every AMEND entry carries stability verdict |
| C-15 | PASS | TOKEN pre-declared before C0 mechanism prose (GATE-0 unconditional) |
| C-16 | PASS | Every stability verdict accompanied by distinct evidence |
| C-17 | PASS | TOKEN embeds at least one domain-specific term |
| C-18 | PASS | DOMAIN-TERMS artifact closed before TOKEN declaration |
| C-19 | PASS | TOKEN is literal first output — no conditional logic precedes it |
| C-20 | PASS | AMEND schema enumerates all four components by name |
| C-21 | PASS | GATE-0 declared unconditional; GATE-1 named as first conditional gate |
| C-22 | PASS | AMEND schema component names are domain-neutral |
| C-23 | PASS | Pre-execution manifest enumerates all gates with execution-mode labels |
| C-24 | PASS | Manifest rendered as native markdown table outside code fence |
| C-25 | PASS | TOKEN named as required in every gate's output spec |
| C-26 | PASS | Each gate has dedicated REQUIRED OUTPUTS block |
| C-27 | PASS | REQUIRED OUTPUTS blocks are sole output spec — no parallel completion conditions |
| C-28 | PASS | REQUIRED OUTPUTS blocks rendered as native markdown tables |
| C-29 | PASS | TOKEN marked as required in REQUIRED OUTPUTS table column |
| C-30 | PASS | `[TOKEN]` bracket-notation substitution rule declared for column headers |
| C-31 | PASS | GATE-0 retains `[TOKEN] required?` template header; Propagation contract row present and self-contained |
| C-32 | PASS | Manifest includes `[TOKEN] propagation` column with per-gate inheritance state |
| C-33 | PASS | Manifest column cells use "Declaration site" / "Substitution/inheritance site" verbatim |
| C-34 | PASS | TOKEN-PROPAGATION ARCHITECTURE block precedes manifest table as separate closed artifact |
| C-35 | PASS | Manifest column header uses `[TOKEN] propagation` bracket-notation |
| C-36 | PASS | Manifest column and GATE-0 REQUIRED OUTPUTS each independently self-contained |
| C-37 | PASS | Triple-mechanism hardening: C-33 + C-34 + C-35 all active simultaneously |
| C-38 | PASS | Architecture block explicitly names both manifest column and GATE-0 REQUIRED OUTPUTS table as targets |
| C-39 | PASS | Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim |
| C-40 | PASS | Propagation declaration occupies dedicated structurally distinct row in GATE-0 REQUIRED OUTPUTS |
| C-41 | PASS | C-36 (dual-layer independence) + C-37 (triple-mechanism hardening) simultaneously satisfied |
| C-42 | PASS | Architecture block is vocabulary-consistent dual-primer: C-38 + C-39 simultaneously, all four elements present |
| C-43 | **PASS** | 4 labeled items; all four C-42 elements readable by label scan; count = 4 satisfies "completeness verifiable by item count alone" — C-43 does not enforce per-item cardinality, only structural form and element presence |
| C-44 | **FAIL** | Item 1 maps to two C-42 elements (manifest column name + "Substitution/inheritance site" verbatim); item 4 maps to zero C-42 elements; element distribution is 2+1+1+0, not 1+1+1+1; a reader counting 4 items cannot confirm each item carries exactly one element without reading content — bijective constraint violated |

**Aspirational: 35/36 = 9.722 pts**

**V-01 Composite: 60 + 30 + 9.722 = 99.722**

---

### V-02 — 3-Item Checklist, Elements 1+2 Bundled in Item 1

**Architecture block form:** 3 items. Item 1 = "Named targets — manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table" (bundles elements 1+2). Item 2 = element 3 ("Declaration site"). Item 3 = element 4 ("Substitution/inheritance site"). Count = 3.

#### Essential / Recommended: All pass (same as V-01) — 90/90

#### Aspirational Differentials

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-42 | PASS | All 34 pre-C-43 criteria satisfied — gate structure and architecture block content identical to V-01 |
| C-43 | **FAIL** | Count = 3; a reader counting labeled items finds 3, not 4 — cannot confirm all four C-42 elements are present without reading item 1's content to discover it contains two artifact names; "completeness verifiable by item count alone" fails at count = 3 |
| C-44 | **FAIL (chain)** | C-43 fails → C-44 scored 0 by chain dependency; additionally count = 3 ≠ 4 breaks bijective constraint from below |

**Aspirational: 34/36 = 9.444 pts**

**V-02 Composite: 60 + 30 + 9.444 = 99.444**

---

### V-03 — 5-Item Checklist, Items 1–4 Each Carry One Element, Item 5 Non-C-42

**Architecture block form:** 5 items. Items 1–4 each carry exactly one C-42 element (bijective within that range). Item 5 = explicitly labeled independence confirmation note (non-C-42). Count = 5.

#### Essential / Recommended: All pass — 90/90

#### Aspirational Differentials

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-42 | PASS | All 34 pre-C-43 criteria satisfied |
| C-43 | **FAIL** | Count = 5; C-43's operative test states "a reader can identify **four** labeled items and match each to one of the four C-42 required elements." With 5 items, a reader consulting only structure cannot identify which four of the five carry C-42 elements without reading item 5's content to confirm it is non-C-42. Over-cardinality breaks count-verification symmetrically with under-cardinality — the bijective test collapses in both directions. C-43 requires that item count **is** element count as a structural invariant; 5 ≠ 4 breaks that invariant. |
| C-44 | **FAIL (chain)** | C-43 fails → C-44 = 0; additionally count = 5 ≠ 4 |

**Aspirational: 34/36 = 9.444 pts**

**V-03 Composite: 60 + 30 + 9.444 = 99.444**

> **Decisive question answered:** V-03 scores 99.444 (same as V-02, not 99.722 as V-01). C-43's "completeness verifiable by item count alone" is **symmetric on cardinality** — over-cardinality (5 items) breaks the count-verification invariant exactly as under-cardinality (3 items) does. The C-43 boundary is count = 4 with all four elements present.

---

### V-04 — Standard 4-Item Bijective Labeled Checklist

**Architecture block form:** Exactly 4 items. Item 1 = element 1 (manifest column). Item 2 = element 2 (GATE-0 REQUIRED OUTPUTS). Item 3 = element 3 ("Declaration site"). Item 4 = element 4 ("Substitution/inheritance site"). Count = 4. One element per item, no bundling.

#### Essential / Recommended: All pass — 90/90

#### Aspirational Differentials

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-42 | PASS | All 34 pre-C-43 criteria satisfied |
| C-43 | **PASS** | 4 labeled items; all four C-42 elements each occupy their own dedicated item; count = 4 satisfies structural form; completeness verifiable by item count alone |
| C-44 | **PASS** | Bijective constraint satisfied: exactly 4 items, exactly one C-42 element per item; distribution is 1+1+1+1; a reader counting 4 items can confirm all four elements are independently present without reading any item's content |

**Aspirational: 36/36 = 10.000 pts**

**V-04 Composite: 60 + 30 + 10.000 = 100.000**

---

### V-05 — V-04 Bijective Checklist + Explicit C-44 Bijective Pre-Declaration Header

**Architecture block form:** Same 4-item bijective structure as V-04, preceded by an explicit declaration: "C-44 BIJECTIVE — 4 ITEMS, 1 ELEMENT PER ITEM." The header commits the cardinality rule structurally before the items are rendered.

#### Essential / Recommended: All pass — 90/90

#### Aspirational Differentials

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09–C-43 | PASS | All 35 criteria satisfied; bijective checklist form identical to V-04 |
| C-44 | **PASS** | Same bijective 4-item structure as V-04; the pre-declaration header does not affect criterion outcome but explicitly names the constraint being satisfied — cardinality rule is declared before the items render, structurally preventing drift where items are added mid-construction |

**Aspirational: 36/36 = 10.000 pts**

**V-05 Composite: 60 + 30 + 10.000 = 100.000**

---

## Rankings

| Rank | Variation | C-43 | C-44 | Aspirational | Composite |
|------|-----------|------|------|--------------|-----------|
| 1 | **V-04** | PASS | PASS | 36/36 | **100.000** |
| 1 | **V-05** | PASS | PASS | 36/36 | **100.000** |
| 3 | V-01 | PASS | FAIL | 35/36 | 99.722 |
| 4 | V-02 | FAIL | FAIL (chain) | 34/36 | 99.444 |
| 4 | V-03 | FAIL | FAIL (chain) | 34/36 | 99.444 |

---

## Decisive Questions — Verdicts

**Q1: Does V-01 score exactly 99.722 (C-43 PASS / C-44 FAIL), confirming they are distinct criteria?**
YES. V-01 passes C-43 (count = 4, all elements present) while failing C-44 (item 1 bundles elements 1+4, bijective constraint violated). The one-criterion gap places V-01 at 35/36, distinct from V-02's 34/36. C-43 and C-44 are confirmed as independent criteria at independent score levels: C-43 tests structural form with element presence; C-44 tests bijective distribution within that form.

**Q2: Does V-03 (count=5) score 99.444 or 99.722?**
99.444 (C-43 FAIL, same tier as V-02). C-43's "completeness verifiable by item count alone" is symmetric on cardinality — count = 3 and count = 5 both break the invariant that item count equals element count. The over-cardinality path (V-03) and under-cardinality path (V-02) land at the same score. C-44 fails by chain in both cases. The C-43 pass boundary is count = 4 with bijective-or-better element distribution.

**Q3: Does V-05's bijective pre-declaration header add scoring advantage over V-04?**
No scoring advantage — both are 100.000. The header contributes multi-run **drift resistance** (cardinality rule is structurally declared before items render, making mid-construction element addition structurally wrong) but does not move any criterion. V-04 and V-05 are equivalent by rubric; V-05 is a reliability hedge, not a score gain.

---

## Excellence Signals (top-scoring variations V-04 / V-05)

**1. Bijective element-to-item mapping as the verification mechanism**
The canonical C-44-compliant form distributes exactly one C-42 element per item with no extras and no bundling. Count = item count = element count = 4. A reader performs a single count operation; no content inspection needed. This is structurally different from C-43's weaker form, which only requires labeled items to contain all elements — C-44 makes item count the sole oracle.

**2. Explicit bijective pre-declaration (V-05 pattern)**
Placing "C-44 BIJECTIVE — 4 ITEMS, 1 ELEMENT PER ITEM" as a header before the checklist items commits the cardinality constraint before the construction begins. This prevents the drift path where a model adding an independence-confirmation note as a fifth labeled item breaks C-44 inadvertently. The declaration is a structural commitment, not a post-hoc description.

**3. Non-C-42 content belongs outside the checklist, not inside it as item N**
V-01 demonstrated the failure mode: placing an independence confirmation as item 4 creates a zero-element item that breaks bijective mapping. V-04/V-05 demonstrate the correct form: independence confirmation either (a) lives in the architecture block prose outside the checklist, or (b) is omitted from the checklist entirely. The checklist's scope is strictly the four C-42 elements.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["bijective element-to-item mapping: exactly 4 checklist items each carrying exactly one C-42 element makes item count the sole completeness verification mechanism without content inspection", "C-43 cardinality is symmetric -- count=3 and count=5 both fail count-verification just as count<4 fails; the C-43 pass boundary requires count=4 with all four elements independently distributed", "explicit C-44 bijective pre-declaration header before checklist items commits cardinality constraint structurally before construction begins preventing inadvertent extra-item drift that breaks bijective mapping at no scoring cost"]}
```
