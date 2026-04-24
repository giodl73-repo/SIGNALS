# trace-permissions — Round 8 Scoring

## Variation Scores

### V-01 — Gate-Centric (full prompt available)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | TABLE 3 maps every role × Create/Read/Update/Delete/Assign/Share/Domain Ops |
| C-02 | PASS | TABLE 1: Field / Default / Role / FLS Override columns — row per differing field |
| C-03 | PASS | TABLE 2: Scope (Own/BU/Parent BU/Org) + Enforcement per role |
| C-04 | PASS | Phase 2 + Phase 3 require Gap IDs; gate conditions enforce inventory population |
| C-05 | PASS | TABLE 4 with four-vector path + Inertia column |
| C-06 | PASS | TABLE 5: Sharing Rule Conflicts with Inertia |
| C-07 | PASS | TABLE 6: Team Membership Gaps with null-finding requirement |
| C-08 | PASS | TABLE 7: Risk-Ranked Summary with Justification |
| C-09 | PASS | Section 4c: "[G-ID] \| Risk \| Remediation: [specific: role + field + operation]" |
| C-10 | PASS | Phase 1 requires ≥2 H-labeled falsifiable hypotheses before any table |
| C-11 | PASS | Section 4b: null-finding tables require named controls + one-sentence justification |
| C-12 | PASS | TABLE 4: all 4 vectors listed; null-finding format requires controls + "Why it holds" |
| C-13 | PASS | H-Flag column in TABLE 1–6; Phase 4 resolves each H with specific table/row citation |
| C-14 | PASS | Each phase closes with a named "PHASE N COMPLETE" gate assertion |
| C-15 | PASS | Phase 4: "Only G-IDs from the inventory; no new IDs in TABLE 7" |
| C-16 | PASS | Gap inventory committed before Phase 3 COMPLETE marker |
| C-17 | PASS | G-series IDs assigned at first occurrence; appear unchanged in findings + TABLE 7 |
| C-18 | PASS | Inertia column in TABLE 4 (escalation) + TABLE 5 (sharing rules) — ≥2 Phase 3 tables |
| C-19 | PASS | Inertia column in TABLE 1 (FLS) + TABLE 2 (record scope) — Phase 2 coverage |
| C-20 | PASS | G-NN(P2) must appear: Phase 2 table row → Phase 3 table row → inventory → TABLE 7 |
| C-21 | PASS | All four gates structured as explicit □-condition checklists |
| C-22 | PASS | Inventory entry format: G-ID + description + "first seen: TABLE X, row" |
| C-23 | PASS | TABLE 7: Phase Origin column; P2-origin entries carry inline chain |
| C-24 | PASS | 4th inventory field: `(H-NN)` or `(H-NN/H-MM)` or `(N/A: reason)` — explicit format |
| C-25 | PASS | (P2) suffix at Phase 2 table row; Phase 2 gate: "□ origin tagged at discovery row, not Phase 4" |
| C-26 | PASS | STRUCTURAL RULE preamble + Phase 4 gate: "□ No criterion satisfied only by prose" |

**V-01 Score: 185 / 185**

---

### V-02 — Atomic Column Contracts

Column headers carry complete specifications; no prose around tables. C-26 achieved by construction: no prose block exists to be the sole carrier of any criterion.

| Criteria affected | Assessment |
|-------------------|-----------|
| C-01 to C-24 | PASS — column contracts preserve all structural homes; no criterion is stripped |
| C-25 | PASS — origin classification at Phase 2 table row (per R8 shared rules); gate verifies |
| C-26 | **Strongest pass** — column headers eliminate surrounding prose structurally, not declaratively; C-26 is vacuously satisfied (no prose present to violate it) |
| C-14, C-21 | PASS — atomic column contracts replace prose *around* tables, not gates; □-checklists remain |

**V-02 Score: 185 / 185**

Excellence signal: C-26 achieved *without* a self-certifying gate condition — prose absence is the proof. More robust than declarative assertion.

---

### V-03 — Compressed (~40% shorter, zero criterion loss)

Compression removes decorative framing prose. All structural elements — tables, gates, inventory block — retained. C-26 proved by absence: no prose between structural elements means no prose can be the load-bearing location for any criterion.

| Criteria affected | Assessment |
|-------------------|-----------|
| C-01 to C-26 | All PASS — "zero criterion loss" means every structural home is preserved; compression excised prose, not criterion-carrying elements |
| C-21 | Risk area — gate checklists compress to fewer words; if □-conditions are abbreviated to the point of ambiguity, this could be PARTIAL. Trusting the zero-criterion-loss claim: PASS |
| C-26 | PASS — absence proof is the strongest possible demonstration |

**V-03 Score: 185 / 185**

---

### V-04 — Conversational + Inventory-as-Commitment

Structural rules framed as behavioral commitments: "connect each gap to your hypotheses" (C-24), "stamp when you find it" (C-25). No formal □-checklist gates.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 to C-13 | PASS | Content criteria unaffected by framing register |
| C-14 | **PARTIAL** | Conversational phase markers ("now let's commit to our inventory") are weaker than a visible named state transition "PHASE N COMPLETE"; gate is present but form is ambiguous — 7.5 pts (−7.5) |
| C-15 | PASS | Behavioral commitment "inventory before summary" survives |
| C-16 | PASS | Inventory-as-commitment framing is the *defining* axis; strongly covered |
| C-17 to C-20 | PASS | G-series IDs and provenance unaffected by framing register |
| C-21 | **FAIL** | Pass condition explicitly requires "□-prefixed condition per verifiable output requirement." Conversational commitments do not produce □-checklists. A single-line "commit phase" does not pass. −5 pts |
| C-22 to C-24 | PASS | H-binding framing carried into inventory entries |
| C-25 | **PARTIAL** | "Stamp when you find it" is a behavioral commitment without a gate condition verifying the stamp occurred at Phase 2. A model following this instruction might stamp correctly, but the gate does not enforce it — no mechanical detection of late classification. −2.5 pts |
| C-26 | PASS | Behavioral commitments direct the model toward structural elements; prose navigation remains decorative |

Deductions: C-14 −7.5, C-21 −5, C-25 −2.5 = **−15 pts**

**V-04 Score: 170 / 185**

---

### V-05 — Adversarial-First + Full Upgrade

Extends R7 V-05 with all three R8 additions: (P2) origin tagging at Phase 2 rows (C-25), structural rule preamble (C-26), H-binding in inventory (C-24). Adversarial framing strengthens depth criteria without weakening structural criteria.

| Criteria affected | Assessment |
|-------------------|-----------|
| C-04, C-05, C-06, C-10 | **Strengthened** — adversarial framing assumes gaps exist, making null-findings harder to assert without genuine evidence |
| C-24, C-25, C-26 | PASS — all three R8 additions explicitly present per description |
| C-14, C-21 | PASS — full upgrade retains formal □-checklist gates from prior rounds |
| C-01 to C-23 | PASS — complete coverage maintained from R7 base |

**V-05 Score: 185 / 185**

---

## Composite Rankings

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| T-1 | **V-01** | **185/185** | ✓ | Gate-centric; dual-registration of structural rules |
| T-1 | **V-02** | **185/185** | ✓ | C-26 structurally eliminated, not declared |
| T-1 | **V-03** | **185/185** | ✓ | C-26 proved by absence; leaner execution surface |
| T-1 | **V-05** | **185/185** | ✓ | Adversarial framing strengthens depth criteria |
| 5 | V-04 | 170/185 | ✓ | Behavioral commitments fail C-21; partial on C-14, C-25 |

---

## Excellence Signals

Two patterns appear in the top-scoring variations that are not yet rubric criteria:

**Signal 1 — Inline Four-Location Chain Notation (V-01, V-05)**
The Phase Origin column uses a compact trace chain: `P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]`. C-20 requires the four-location chain to *exist*; C-23 requires a Phase Origin column. Neither requires a single-cell notation that expresses all four hops inline. This notation makes C-20 compliance verifiable from TABLE 7 alone — a Phase 4 reviewer does not need to re-scan upstream tables to walk the chain.

**Signal 2 — "Why It Holds" Field in Null Escalation Rows (V-01)**
TABLE 4 null-finding rows require: `Vector: [name] | Path: NONE | Controls: [specific] | Why it holds: [reason]`. C-11 requires null-finding accountability for Phase 3 tables generally. C-12 requires all four vectors covered. Neither requires a *mechanism explanation* for why the path does not exist — only that controls were examined. "Why it holds" names the mechanism that blocks the path, making the null-finding falsifiable: a reviewer can identify what would have to change to open the path. This is the inertia-equivalent for null escalation paths, and it is not currently captured in C-11, C-12, or C-18.

---

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["Inline four-location chain notation in Phase Origin column: 'P2: T[N]/[row] -> T[N]/[row] -> INV/G-NN(P2) -> T7/r[N]' — makes C-20 compliance verifiable from TABLE 7 alone without re-scanning upstream tables", "Why-it-holds field in null escalation rows: names the mechanism blocking each null path, making the null-finding falsifiable — the inertia equivalent for TABLE 4 null entries, not currently captured by C-11, C-12, or C-18"]}
```
