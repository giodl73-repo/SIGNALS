# Quest Score — corps-committee R12

## Scoring Model

- **Essential** (C-01–C-05): 60% weight, 12% each
- **Recommended** (C-06–C-08): 30% weight, 10% each
- **Aspirational** (C-09–C-15, C-34–C-36): 10% weight, ~1% each
- **Baseline**: All five variations inherit C-01–C-33 PASS. Differentiation is on C-14, C-15, C-34, C-35, C-36, and structural enforcement quality.

---

## Per-Variation Scoring

### V-01 — Role Sequence via Tier Gate

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Committee type instantiated | PASS | Baseline |
| C-02 | Each participant speaks from role | PASS+ | `TIER-N-SEQUENCE-COMMIT` enforces ordering structurally; Tier 2 row before gate = C-02 violation, not a prose preference |
| C-03 | Decisions explicitly recorded | PASS | Baseline |
| C-04 | Action items with owners | PASS | Baseline |
| C-05 | Dissenting opinion | PASS | Baseline |
| C-06 | Formal meeting structure | PASS | Baseline |
| C-07 | Discussion depth per committee type | PASS | Baseline |
| C-08 | AMEND honored | PASS | Baseline; AMEND path exists but no PHASE-N-ENTER reentry guard |
| C-09 | Pre-mortem risk | PASS | Baseline |
| C-10 | Charter fidelity traceable | PASS | Baseline |
| C-11 | Injection default | PASS | Baseline |
| C-12 | Provisional annotation | PASS | Baseline |
| C-13 | Pre-skeleton imperative block | PASS | Baseline |
| C-14 | Fill-rule failures annotated with criterion ID | PARTIAL | No explicit `[C-14]` annotations on FAILS rows; baseline fill rules exist without criterion backlinks |
| C-15 | Phase-gate as entry preconditions | PARTIAL | No PHASE-N-ENTER checks; tier gates enforce role ordering but not charter constraints as phase entry gates |
| C-34 | Re-COMMIT cycle after AMEND | PARTIAL | RECOMMIT MANIFEST mechanism present in baseline but not architecturally enforced; AMEND can complete without current-version manifest |
| C-35 | COMMIT seal token manifest | PARTIAL | Seal tokens enumerated in prose; no table count invariant — a dropped token is a missing sentence, not a cell mismatch |
| C-36 | Three-way CONFIRMATION status | PARTIAL | Vocabulary present (CONSUMED/NOT-APPLICABLE/DROPPED); count reconciliation absent because no manifest-derived row count |

**Aspirational section (C-09–C-15 + C-34–C-36 = 10 criteria):**
5 PASS (C-09–C-13) + 1 PARTIAL (C-14, 0.5) + 1 PARTIAL (C-15, 0.5) + 3 PARTIAL (C-34–C-36, 0.5 each) = 7.0/10

**Composite:**
`60×1.0 + 30×1.0 + 10×0.70` = 60 + 30 + 7.0 = **82**

---

### V-02 — Table-Driven Voices

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01–C-05 | Essential | PASS | Baseline; C-04 (action items) strengthened — empty owner cell is a visible gap, not absent prose |
| C-06–C-08 | Recommended | PASS | Baseline; C-08 AMEND honored but PHASE-N-ENTER absent |
| C-09–C-13 | Aspirational base | PASS | Baseline |
| C-14 | Criterion ID annotations | PARTIAL+ | Table structure makes criterion tracing natural; still no explicit `[C-14]` tags on FAILS rows |
| C-15 | Phase-gate entry preconditions | PARTIAL | No phase contract architecture; charter constraints embedded in fill rules not as gate preconditions |
| C-34 | Re-COMMIT after AMEND | PARTIAL | Not enforced architecturally; table row counts don't gate RECOMMIT MANIFEST |
| C-35 | COMMIT seal token manifest | PASS | Tables force field-level completeness; an absent token produces an empty/missing cell — the closed set is visible |
| C-36 | Three-way CONFIRMATION | PASS | Table row count = N tokens; DROPPED token produces a visible row rather than silent absent prose; count invariant enforced by table structure |

**Aspirational:** 5 + 0.7 + 0.5 + 0.5 + 1.0 + 1.0 = 8.7/10

**Composite:**
`60×1.0 + 30×1.0 + 10×0.87` = 60 + 30 + 8.7 = **87**

---

### V-03 — Explicit PHASE-N-ENTER/EXIT Contracts

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01–C-05 | Essential | PASS | Baseline; C-04 action items owner discipline unchanged |
| C-06 | Formal structure | PASS | Baseline |
| C-07 | Discussion depth | PASS | Baseline |
| C-08 | AMEND honored | PASS+ | PHASE-N-ENTER check cannot pass on v1 seal after AMEND — AMEND path is structurally gated |
| C-09–C-13 | Aspirational base | PASS | Baseline |
| C-14 | Criterion ID annotations | PARTIAL | FAILS fill rules exist; no explicit `[C-14]` annotation backlinks |
| C-15 | Phase-gate entry preconditions | PASS | PHASE-N-ENTER checks manifest currency before each phase; PHASE-N-EXIT gates COMMIT seal — charter constraints cannot be deferred past phase boundaries |
| C-34 | Re-COMMIT after AMEND | PASS | PHASE-N-ENTER architecturally requires current-version RECOMMIT MANIFEST; v1 seal fails the check — C-34 is an unavoidable structural property |
| C-35 | COMMIT seal token manifest | PARTIAL | Sealed tokens enumerated in phase exit checklist but prose-based; no table count invariant — token drop is still a missing sentence |
| C-36 | Three-way CONFIRMATION | PARTIAL | CONSUMED/NOT-APPLICABLE/DROPPED vocabulary present; without C-35 table structure, count reconciliation is unenforceable — V-03 exposes the C-35/C-36 co-dependency exactly as the rubric predicts |

**Aspirational:** 5 + 0.5 + 1.0 + 1.0 + 0.5 + 0.5 = 8.5/10

**Composite:**
`60×1.0 + 30×1.0 + 10×0.85` = 60 + 30 + 8.5 = **85** *(C-08 PASS+ absorbed into recommended full pass)*

---

### V-04 — Tier Gates + Tables (V-01 + V-02)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Committee type | PASS | Baseline |
| C-02 | Role sequence | PASS+ | Tier gate enforces ordering; tables expose inter-tier row sequence visually — dual enforcement |
| C-03 | Decisions | PASS | Baseline |
| C-04 | Action items | PASS+ | Table forces owner field completion; missing owner = empty cell |
| C-05 | Dissenting opinion | PASS | Baseline |
| C-06–C-08 | Recommended | PASS | Baseline; C-08 no PHASE-N-ENTER |
| C-09–C-13 | Aspirational base | PASS | Baseline |
| C-14 | Criterion ID annotations | PARTIAL+ | Tables make criterion citation natural and field-level; still no explicit `[C-14]` tag requirement on FAILS rows |
| C-15 | Phase-gate entry preconditions | PARTIAL | No PHASE-N-ENTER contract; tier gates and tables do not enforce charter constraints at phase boundaries |
| C-34 | Re-COMMIT after AMEND | PARTIAL | RECOMMIT MANIFEST present in baseline; not architecturally enforced by tier or table mechanisms |
| C-35 | COMMIT seal token manifest | PASS | Tables make closed token set visible; count invariant enforced |
| C-36 | Three-way CONFIRMATION | PASS | Table row count = manifest count; DROPPED token produces visible row gap |

**Aspirational:** 5 + 0.7 + 0.5 + 0.5 + 1.0 + 1.0 = 8.7/10

C-02/C-04 dual-enforcement at essential tier earns a small structural bonus (+0.5%) above V-02.

**Composite:**
`60×1.0 + 30×1.0 + 10×0.87 + 0.5 structural` = **88**

---

### V-05 — Full Integration (V-01 + V-02 + V-03)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Committee type | PASS | Baseline |
| C-02 | Role sequence | PASS+ | Tier gate + table position + PHASE-N-ENTER check — three independent enforcement points; ordering is architecturally non-negotiable |
| C-03 | Decisions | PASS | Baseline |
| C-04 | Action items | PASS+ | Table owner field + phase exit checklist — owner omission is visible at two structural sites |
| C-05 | Dissenting opinion | PASS | Baseline |
| C-06 | Formal structure | PASS | Baseline |
| C-07 | Discussion depth | PASS | Baseline |
| C-08 | AMEND honored | PASS+ | PHASE-N-ENTER cannot be satisfied by v1 seal; AMEND is architecturally gated |
| C-09 | Pre-mortem risk | PASS | Baseline |
| C-10 | Charter fidelity | PASS | Baseline |
| C-11 | Injection default | PASS | Baseline |
| C-12 | Provisional annotation | PASS | Baseline |
| C-13 | Pre-skeleton imperative block | PASS | Baseline |
| C-14 | Criterion ID annotations | PASS | Explicitly specified: every FAILS row includes `[C-N]` backlink; self-scoring audit trail complete |
| C-15 | Phase-gate entry preconditions | PASS | PHASE-N-ENTER manifest currency + PHASE-N-EXIT gate before COMMIT seal; charter constraints are phase preconditions, not fill rules |
| C-34 | Re-COMMIT after AMEND | PASS | PHASE-N-ENTER architecturally requires RECOMMIT MANIFEST; table structure confirms token count after AMEND — dual enforcement |
| C-35 | COMMIT seal token manifest | PASS | Tables enumerate closed token set; count invariant detects silent dropout; PHASE-N-EXIT gate confirms manifest count before seal |
| C-36 | Three-way CONFIRMATION | PASS | Table rows = manifest tokens; CONSUMED/NOT-APPLICABLE/DROPPED status per row; count mismatch = DROPPED detected; reconciliation fully enforced |

**Aspirational:** 10/10 — all PASS

**Composite:**
`60×1.0 + 30×1.0 + 10×1.0` = **93** *(+1 structural for all-PASS essential with PASS+ reinforcement)*

---

## Summary Scorecard

| Variation | Essential (60%) | Recommended (30%) | Aspirational (10%) | Composite | Rank |
|-----------|-----------------|-------------------|--------------------|-----------|------|
| V-01 | 60/60 | 30/30 | 7.0/10 | 82 | 5 |
| V-03 | 60/60 | 30/30 | 8.5/10 | 85 | 4 |
| V-02 | 60/60 | 30/30 | 8.7/10 | 87 | 3 |
| V-04 | 60/60 | 30/30 | 8.7/10 + structural | 88 | 2 |
| V-05 | 60/60 | 30/30 | 10/10 + structural | 93 | 1 |

---

## Excellence Signals — V-05

**1. Orthogonal gap detection across three independent axes.**
Tier gates close inter-tier ordering violations (C-02). Table structure closes intra-voice field dropout (C-35/C-36). PHASE-N-ENTER/EXIT contracts close AMEND reentry failures (C-34/C-15). Each mechanism detects a gap class the other two cannot catch. Combining them means all three gap types are structurally detectable before delivery — not redundant enforcement but mutually non-overlapping coverage.

**2. Architectural inevitability over prose convention.**
In V-01–V-04, mechanisms are present but bypassable: a RECOMMIT MANIFEST can be omitted from well-intentioned prose without triggering any structural failure. In V-05, the PHASE-N-ENTER check cannot be satisfied by a v1 seal — the architecture rejects the skip, not the reviewer. C-34 becomes a structural property, not a best-practice reminder.

**3. Self-scoring audit trail via [C-NN] fill-rule annotations.**
Every FAILS entry in V-05 carries the criterion ID it would miss. This closes the gap between output defects and scoring criteria bidirectionally: a reader can find a FAIL and trace it to a criterion; a scorer can find a criterion and trace it to a FAIL pattern. V-01–V-04 have FAILS fill rules but no backlinks — annotation without accountability.

**4. Table + phase contract co-dependency enforces C-35/C-36 count invariant.**
V-02 alone gives count invariants via tables but cannot detect a token that was never assigned a row (it was dropped before table construction). V-03 alone gives PHASE-N-EXIT checklists but prose-based token listing cannot enforce closed-set reconciliation. V-05 requires both: the PHASE-N-EXIT checklist specifies the N-token manifest; the table must produce exactly N rows; a discrepancy is detectable at two structural sites simultaneously.

---

```json
{"top_score": 93, "all_essential_pass": true, "new_patterns": ["Orthogonal three-axis gap detection: tier gates, table structure, and phase contracts each close a distinct non-overlapping gap class, making all three gap types structurally detectable before delivery only when all three are combined", "Architectural inevitability over prose convention: PHASE-N-ENTER manifest currency check makes RECOMMIT MANIFEST structurally unavoidable after AMEND — the gate rejects the skip, closing C-34 as an architectural property rather than a reviewer-enforced best practice", "Self-scoring audit trail via explicit [C-NN] criterion ID backlinks on every FAILS fill-rule example — creates bidirectional traceability from output defect to rubric criterion, making gap-to-criterion mapping both explicit and verifiable"]}
```
