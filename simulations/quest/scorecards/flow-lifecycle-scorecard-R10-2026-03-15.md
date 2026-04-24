## flow-lifecycle — Round 10 Scoring (v10: C-31, C-32, C-33)

### Floor Assessment

Before scoring variations, mapping what the R10-v10 floor already satisfies:

- **C-01 to C-08** (essential + recommended): All PASS across all variations — State Table, Exception Catalog, Terminal Declaration, Bottleneck/Gap Registers, Role Registry, Decision Table, and Edge Case Catalog all present with adequate schema enforcement.
- **C-09 to C-29**: All PASS — Cross-Process Handoff, SLA, Role-First Anchoring, inline anti-patterns, sequential gates (GATE A + GATE B + production gate), terminal verification, decision fallback, Phase Index, quantified thresholds (taxonomy form), schema-inline placement, production gate with failure declaration + remediation + causal mechanism + defect taxonomy, Handler column backward-trace rule + co-located fail language, Decision Condition taxonomy.
- **C-30 (Exception-Catalog Boundary Gate)**: **NOT in floor** — confirmed by V-02 design note: "the existing floor places Terminal Declaration before Exception Catalog." Both V-01 and V-03 inherit this defect.
- **C-31, C-32, C-33**: Not in floor — these are the three variation axes.

---

### Criterion-by-Criterion Evaluation

| Criterion | V-01 (C-33) | V-02 (C-32) | V-03 (C-31) | V-04 (C-33+C-32) | V-05 (all three) |
|-----------|:-----------:|:-----------:|:-----------:|:-----------------:|:----------------:|
| **C-01** Essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** Essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** Essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** Essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** Essential | PASS | PASS | PASS | PASS | PASS |
| **C-06** Recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** Recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** Recommended | PASS | PASS | PASS | PASS | PASS |
| **C-09–C-20** Aspirational | PASS×12 | PASS×12 | PASS×12 | PASS×12 | PASS×12 |
| **C-21** Handler role | PASS | PASS | PASS | PASS | PASS |
| **C-22** Gate failure decl. | PASS | PASS | PASS | PASS | PASS |
| **C-23** Authority pre-cert | PASS | PASS | PASS | PASS | PASS |
| **C-24** Remediation instruction | PASS | PASS | PASS | PASS | PASS |
| **C-25** Causal mechanism | PASS | PASS | PASS | PASS | PASS |
| **C-26** Authority inline schema | PASS | PASS | PASS | PASS | PASS |
| **C-27** Defect taxonomy | PASS (5 entries) | PASS (5 entries) | PASS (6 entries) | PASS (6 entries) | PASS (8 entries) |
| **C-28** Handler fail co-location | PASS | PASS | PASS | PASS | PASS |
| **C-29** Threshold-type taxonomy | PASS | PASS | PASS | PASS | PASS |
| **C-30** Exception-catalog boundary gate | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-31** Dual-mechanism threshold | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |
| **C-32** Bidirectional exception gates | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-33** Pre-schema lifecycle inventory | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |

**Evidence notes for failures:**

- **V-01 C-30/C-32**: Terminal Declaration appears at lines 348–357, Exception Catalog at lines 359–376 — wrong ordering, no boundary gates.
- **V-01 C-31**: Decision Table Condition header has taxonomy only ("dollar amount, day count, retry count") — no quoted example with operator+unit.
- **V-02 C-31**: Decision Table Condition header same as floor ("dollar amount, day count, retry count; qualitative alone does not count") — taxonomy only.
- **V-02 C-33**: No Step 0 block; STATUS-QUO PROCESS DECLARATION is the first section.
- **V-03 C-30/C-32**: Terminal Declaration at lines 1169–1175 precedes Exception Catalog at lines 1177–1190 — no boundary gates.
- **V-03 C-33**: No Step 0 block.
- **V-04 C-31**: Decision Table note at line 1399 explicitly reads "(note: C-31 not targeted; Condition column uses C-29 threshold-type taxonomy only)" — deliberate hold.

**Evidence notes for passes (key items):**

- **V-02 C-30 + C-32**: UPSTREAM GATE at lines 773–780 names source ("State Tables and Decision Tables, all phases") and target ("EXCEPTION CATALOG"). DOWNSTREAM GATE at lines 806–813 names source ("EXCEPTION CATALOG") and target ("TERMINAL DECLARATION"). Exception Catalog precedes Terminal Declaration in document order. AC-17 in coverage scan confirms both gates with per-field verification.
- **V-03 C-31**: Decision Table Condition header at line 1141: `"measurable threshold -- dollar amount, day count, retry count, percentage threshold; qualitative condition alone does not count; e.g., "Invoice total > $5,000", "Days past due > 30"; format: [measure] [operator] [quantity+unit]"` — taxonomy (4 categories) AND quoted examples (2) with comparison operators and units, both in the same column header. Defect taxonomy adds "Taxonomy-only decision condition" and "Example-only decision condition" entries.
- **V-01 C-33**: STEP 0 block at lines 88–104 precedes STATUS-QUO PROCESS DECLARATION; GATE 0 at lines 90–95 requires ≥3 LT-IDs with Trigger Source and Initial State before any other section opens. LT-ID trace propagates to GATE A (Role Registry), Phase Index Entry Trigger column, and Phase Entry Contract LT-ID trace field. Inertia Summary adds "Entry triggers incumbent cannot initiate" row.
- **V-05 C-33 + C-32 + C-31**: All three mechanisms present; AC-17/18/19 each defined with distinct pass/fail conditions; Coverage Scan explicitly requires non-overlapping evidence across these three rows ("no cell sharing the same coverage claim").

---

### Composite Score Calculation

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/25 * 10)
```

| Variation | Essential (5/5) | Recommended (3/3) | Aspirational (n/25) | Score |
|-----------|:--------------:|:-----------------:|:-------------------:|------:|
| V-01 | 60 | 30 | 22/25 = 8.8 | **98.8** |
| V-02 | 60 | 30 | 23/25 = 9.2 | **99.2** |
| V-03 | 60 | 30 | 22/25 = 8.8 | **98.8** |
| V-04 | 60 | 30 | 24/25 = 9.6 | **99.6** |
| **V-05** | **60** | **30** | **25/25 = 10** | **100** |

All variations pass the essential gate (5/5) and the golden threshold (composite ≥ 80).

**Ranking**: V-05 > V-04 > V-02 > V-01 = V-03

---

### Excellence Signals — V-05

V-05 scores 100/100 and contributes three distinct excellence signals beyond what C-29/C-30 already captured:

**Signal 1 — Orthogonal failure surface coverage with explicit naming**

V-05's hypothesis section explicitly identifies three orthogonal structural failure surfaces — schema-entry defects (C-33: unanchored roles, phases with no real trigger), lifecycle-structure defects (C-32: untraceable exception references, unverifiable terminal entries), and decision-quality defects (C-31: format-ambiguous thresholds, category-boundary ambiguous conditions). Naming the failure surfaces explicitly before the schema is designed means the practitioner understands what damage each gate prevents, not just that a gate exists. This framing is absent in V-01 through V-04 individually because each targets only its own surface.

**Signal 2 — Non-overlapping AC evidence mandate on the coverage scan**

V-05 adds a structural constraint to the Coverage Scan itself: AC-17, AC-18, and AC-19 "must each enumerate distinct evidence with no cell sharing the same coverage claim across these three rows." This means the coverage scan cannot satisfy all three with a single claim — each gate must be verified by a different piece of schema evidence. This prevents a practitioner from writing one scan row and bulk-attesting to three criteria. It is the coverage-scan analog of the schema-inline enforcement pattern already established for section-level criteria.

**Signal 3 — Step 0 traceability cascade through three downstream sections**

V-01 introduced Step 0, but V-05 shows the full cascading effect: LT-IDs propagate a new column into the Role Registry (`LT-ID Trace or SECONDARY:rationale`), a new column into the Phase Index (`Entry Trigger must trace to LT-ID or carry DERIVED:rationale`), and a new field into each Phase Entry Contract (`LT-ID trace: LT-ID(s) or DERIVED:rationale`). Step 0 is not a standalone block — it imposes a traceability chain that makes roles and phases verifiable against known initiation conditions across three downstream artifacts. A role that doesn't appear in any LT-ID's initial state is structurally unanchored; this violation is now detectable via backward trace from the registry.

---

### Defect Taxonomy Growth

V-05's Scan Summary defect taxonomy reaches 8 entries (vs. 5 in V-01, 5 in V-02, 6 in V-03, 6 in V-04), adding "Taxonomy-only decision condition" and "Example-only decision condition" — the two single-mechanism variants of the C-31 pattern. This means the production gate's causal mechanism claim (C-25) is maximally specific: an artifact that violates AC-19 carries a defect that can be named by type, not just flagged as a scan failure.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Three orthogonal structural failure surfaces named explicitly and enforced by independent gates — schema-entry (C-33), lifecycle-structure (C-32), decision-quality (C-31) — each verified by a distinct AC with non-overlapping evidence, preventing any single mechanism from satisfying multiple criteria", "Step 0 LT-ID traceability cascade: lifecycle entry triggers propagate a new field through Role Registry, Phase Index, and Phase Entry Contract, making roles and phases verifiable against known initiation conditions across three downstream sections rather than existing as standalone vocabulary", "Coverage scan non-overlapping evidence mandate: AC-17/18/19 must each enumerate distinct evidence with no cell sharing, extending the schema-inline enforcement pattern to the scan layer itself and preventing bulk attestation across orthogonal criteria"]}
```
