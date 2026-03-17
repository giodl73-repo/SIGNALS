# topic-retro — Quest Score R13

## Scoring Setup

**Rubric**: v11 | **Denominator**: 136 (non-AMEND: C-10 and C-22 N/A)
**Base**: R12-V-05 inherits PASS on C-01–C-31 (C-10, C-22 N/A) = 132 pts
**New criteria targeted**: C-32 (per-field independent verification) and C-33 (mechanism-keyed table)

---

## Per-Variation Criterion Analysis

### C-32 Focus: Phase 8 SEAL independent verification
- **V-01**: Three CHECK/HOW blocks (lines 286–299), each explicitly names its own source ("read this cell directly / Do not read Phase 6 or Phase 4" / "Open Phase 6 only. Do not read Phase 4" / "Read 'This score' cell label only. Do not read any other field"). Fully independent. **PASS**
- **V-02**: Phase 8 SEAL unchanged from R12-V-05 (lines 578–585 sequential chain format: COPY-VERIFIED says "the 'This score' value was traced..." — references prior item). **FAIL**
- **V-03**: Receipt format ITEM/VERIFY/SOURCE/FORMAT/RESULT (lines 861–899). Each ITEM has its own SOURCE with explicit isolation ("Do not read Phase 6 or Phase 4 to verify this item" / "Do not open Phase 4 for this check" / "Do not read any other field to verify this item"). Named fields, per-field independent. **PASS**
- **V-04**: Same CHECK/HOW blocks as V-01 (lines 1181–1194). **PASS**
- **V-05**: Same CHECK/HOW blocks as V-01 + each SEAL item adds `Cross-reference: PRE-EXECUTION CONTRACT ...` (lines 1494–1510). **PASS**

### C-33 Focus: Mechanism-keyed table in design guarantees section
- **V-01**: PRE-EXECUTION CONTRACT unchanged from R12-V-05: two-column `Mechanism | Structural guarantee` table with mechanism names as row keys. Trailing "Design guarantees" is a bullet list but PRE-EXECUTION CONTRACT table satisfies C-33. **PASS**
- **V-02**: Three-column `Mechanism | Structural guarantee | Verified in` table (lines 357–368). Mechanism names remain row keys. Three columns exceed minimum — still satisfies. **PASS**
- **V-03**: Two-column table with ENFORCE IN: inline annotations embedded in second column (lines 641–651). Mechanism names remain independently addressable row keys. **PASS**
- **V-04**: Three-column table from V-02 (lines 955–966). **PASS**
- **V-05**: Three-column table + expanded 12-row split (Copy guard split into three rows) + trailing `## DESIGN GUARANTEES` section (lines 1534–1552). Two mechanism-keyed tables, both navigable. **PASS**

---

## Criterion-by-Criterion Table (C-01 to C-33)

All variations inherit R12-V-05 base. Only differences from base are shown; all other criteria carry forward as-is.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-01 Essential: One Echo named, unexpected, actionable | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-02 Essential: Wrong verdicts identified | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-03 Essential: Gap analysis present | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-04 Essential: One Echo, framed as unexpected | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-05 Essential: Topic/commitment context | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-06 Recommended: Signal coverage summary | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-07 Recommended: Recommendation tied to gaps/Echo | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-08 Recommended: Accuracy ratio stated | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-09 Echo linked to systemic pattern | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-10 AMEND scope declared/enforced | N/A | N/A | N/A | N/A | N/A | Non-AMEND run |
| C-11 Systemic Pattern Echo field | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-12 Three-way isolation | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-13 Inertia framing for gaps | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-14 Verdict label explicit | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-15 Accuracy ratio not just count | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-16 Namespace coverage table | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-17 Recommendation bracket-slot template | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-18 Echo systemic pattern named | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-19 Phase completion self-contained | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-20 Gap inertia assumption named | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-21 Phase seal explicit | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-22 OOS secondary table | N/A | N/A | N/A | N/A | N/A | Non-AMEND run |
| C-23 Phase seal format strings per field | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-24 Echo why-unexpected explained | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-25 Recommendation outcome measurable | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-26 Gap inertia column structurally isolated | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-27 Phase self-containment extended | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-28 Recommendation slot completeness guard | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-29 Phase 8 score copy guard | PASS | PASS | PASS | PASS | PASS | Inherited |
| C-30 Phase 8 SEAL copy-verified label + source | PASS | PASS | PASS | PASS | PASS | Inherited; all three fields present |
| C-31 Design guarantees summary explicit | PASS | PASS | PASS | PASS | PASS | Inherited; PRE-EXECUTION CONTRACT section |
| C-32 Phase 8 SEAL fields independent verification | **PASS** | **FAIL** | **PASS** | **PASS** | **PASS** | V-02 unchanged from R12-V-05 sequential chain |
| C-33 Design guarantees mechanism-keyed table | PASS | PASS | PASS | PASS | PASS | All carry two-column table; V-02/V-04/V-05 enhance to three-column |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (46 applicable) | Raw | / 136 |
|-----------|---------------|-----------------|------------------------------|-----|-------|
| V-01 | 60 | 30 | 44 (21×2 + C-32:2 + C-33:2) | **136** | 100% |
| V-02 | 60 | 30 | 42 (21×2 + C-32:0 + C-33:2) | **134** | 98.5% |
| V-03 | 60 | 30 | 44 (21×2 + C-32:2 + C-33:2) | **136** | 100% |
| V-04 | 60 | 30 | 44 (21×2 + C-32:2 + C-33:2) | **136** | 100% |
| V-05 | 60 | 30 | 44 (21×2 + C-32:2 + C-33:2) | **136** | 100% |

**Rank**: V-01 = V-03 = V-04 = V-05 (136) > V-02 (134)

---

## Ranking Detail

**Tier 1 (all at 136/136):**
- **V-05** — Most complete integration: three-column contract, bidirectional cross-references, extended CHECK/HOW to Phase 1 and Phase 7, trailing 12-row DESIGN GUARANTEES with one row per SEAL field. Every feature that scores points is present; extra structure creates audit navigation that doesn't yet have a scoring criterion.
- **V-04** — Zero-interference combination: V-01 CHECK/HOW + V-02 three-column table. Clean structural separation (Phase 8 SEAL vs. PRE-EXECUTION CONTRACT). Simplest path to full marks.
- **V-03** — Phrasing register test: ITEM/VERIFY/SOURCE/FORMAT/RESULT receipt format achieves per-field independence at flatter structural depth. Confirms independence is the scoring variable, not the CHECK/HOW token format.
- **V-01** — Minimal single-axis fix: only Phase 8 SEAL changes. PRE-EXECUTION CONTRACT stays two-column (already meets C-33). Clean isolation.

**Tier 2:**
- **V-02 (134)** — C-32 FAIL is unavoidable given the unchanged sequential-chain SEAL. Three-column enhancement to the contract doesn't compensate.

---

## Excellence Signals from Top-Scoring Variations

**V-05 differentiator — Bidirectional audit cross-linking:**
Each Phase 8 SEAL item's CHECK/HOW block cites its PRE-EXECUTION CONTRACT row by name ("Cross-reference: PRE-EXECUTION CONTRACT 'Copy guard -- This score' row"). Each PRE-EXECUTION CONTRACT row's "Verified in" cell names the corresponding SEAL item. The audit trail is navigable in both directions: contract → enforcement point, and enforcement point → contract. This pattern closes the gap where a guarantee exists in the contract but its SEAL location requires phase tracing, or a SEAL item exists without a named contract basis.

**V-05 differentiator — Per-field row granularity in DESIGN GUARANTEES:**
The trailing DESIGN GUARANTEES section splits "Copy guard -- SEAL" (which was one row in R12-V-05) into three independent rows: `Copy guard -- body`, `Copy guard -- This score`, `Copy guard -- COPY-VERIFIED`, `Copy guard -- COPY-SOURCE`. Each field becomes independently locatable without decomposing a compound row. A reviewer auditing any one field finds it directly by row key without reading a compound row and inferring which sub-item applies.

**V-03 differentiator — Format-independent independence confirmation:**
The receipt format (ITEM/VERIFY/SOURCE/FORMAT/RESULT) achieves C-32 PASS without the CHECK/HOW structural tokens, confirming that per-field independence is the substantive criterion and the token vocabulary is incidental. This is a design signal: the rubric criterion should specify "each field has its own source and isolation instruction" rather than prescribing CHECK/HOW syntax.

---

## JSON Output

```json
{"top_score": 136, "all_essential_pass": true, "new_patterns": ["Bidirectional audit cross-linking: each Phase 8 SEAL item cites its PRE-EXECUTION CONTRACT row by name, and each contract row names its SEAL enforcement item -- audit trail navigable in both directions without tracing phases", "Per-field row granularity in design guarantees: compound rows (Copy guard -- SEAL) split into one row per field, making each field independently locatable by mechanism name without decomposing compound rows during audit"]}
```
