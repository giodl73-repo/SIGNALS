## Quest Score — corps-pr R8

### Scoring Summary

| Variation | Axis | Essential | Recommended | Aspirational | Composite |
|-----------|------|-----------|-------------|--------------|-----------|
| V-01 | C-25 only | 5/5 | 3/3 | 11/19 | **95.8** |
| V-02 | C-26 only | 5/5 | 3/3 | 14/19 | **97.4** |
| V-03 | C-27 only | 5/5 | 3/3 | 12/19 | **96.3** |
| V-04 | C-25 + C-26 | 5/5 | 3/3 | 14/19 | **97.4** |
| V-05 | C-25 + C-26 + C-27 | 5/5 | 3/3 | 16/19 | **98.4** |

Golden threshold: all 5 essential pass AND composite >= 80. **All variations clear threshold.**

---

### Per-Criterion Detail

#### Essential (C-01 – C-05) — all variations PASS all 5

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|----|------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Routing table present in all; coverage gap block required |
| C-02 | PASS | PASS | PASS | PASS | PASS | Source files field + domain-lens gate enforces code mechanism naming |
| C-03 | PASS | PASS | PASS | PASS | PASS | Consensus template: Agreement, Divergence + Mechanism, Critical |
| C-04 | PASS | PASS | PASS | PASS | PASS | Delegated/hedged decisions explicitly banned; sign-off role per condition |
| C-05 | PASS | PASS | PASS | PASS | PASS | Binary test (Step A) + rewrite consequence + drop (Step B) in all |

#### Recommended (C-06 – C-08) — all variations PASS all 3

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|----|------|------|------|------|------|------|
| C-06 | PASS | PASS | PASS | PASS | PASS | COVERAGE GAP named block in all routing sections |
| C-07 | PASS | PASS | PASS | PASS | PASS | `Summary: [N] findings — [x] P1, [y] P2, [z] P3` per role in all |
| C-08 | PASS | PASS | PASS | PASS | PASS | AMEND named-field block with 5 mandatory fields in all |

#### Aspirational (C-09 – C-27) — where variations diverge

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|--------------|
| C-09 | PASS | PASS | PASS | PASS | PASS | Mechanism field names structural reason, not perspective |
| C-10 | PASS | PASS | PASS | PASS | PASS | Sign-off: [role] per condition in all GO WITH CONDITIONS templates |
| C-11 | PASS | PASS | PASS | PASS | PASS | IA explicit first in all; "structural and non-configurable" in V-01/V-03 |
| C-12 | PASS | PASS | PASS | PASS | PASS | Mechanism field + ban-to-fix enforcement in all |
| C-13 | PASS | PASS | PASS | PASS | PASS | 5 enumerated banned phrases in V-01/V-02/V-03; ban-to-fix table in V-04/V-05 |
| C-14 | PART | PART | PART | PART | PART | IA cost anchor present but is a standalone section — no finding text explicitly names IA as counterpoint |
| C-15 | PASS | PASS | PASS | PASS | PASS | Binary test + rewrite gate + drop consequence: all have the explicit two-step structure |
| C-16 | PASS | PASS | PASS | PASS | PASS | AMEND block uses named template slots, not prose instructions |
| C-17 | PASS | PASS | PASS | PASS | PASS | Cost ledger with magnitude labels per row; IA framed as budget authority in all |
| C-18 | FAIL | PASS | FAIL | PASS | PASS | V-01/V-03 use step-based structure without formal Entry/Exit fields per phase |
| C-19 | PASS | PASS | PASS | PASS | PASS | 4-row × 2-column ledger + Budget strength terminal field in all |
| C-20 | FAIL | PASS | FAIL | PASS | PASS | V-01/V-03 lack pipeline declaration; V-02/V-04/V-05 have C1 (Phase B pre-flight) + C2 (per-role read prerequisite) as named entry conditions |
| C-21 | PASS | PASS | PASS | PASS | PASS | Net column in all; Budget verdict cites WORSE/BETTER row names as derivation basis |
| C-22 | FAIL | PASS | FAIL | PASS | PASS | V-01/V-03 no pipeline; V-02/V-04/V-05 structure Phase C entry as two named sub-conditions (C1 pre-flight + C2 per-role) |
| C-23 | PART | PART | PART | PART | PART | V-01: cost anchor present but not a named READ RECEIPT. V-02/V-04: C2 block present but not a READ RECEIPT. V-03/V-05: READ RECEIPT present but fields (d) cost row and (e) initial position live in PRE-COMMITMENT per C-27 design |
| C-24 | FAIL | FAIL | FAIL | FAIL | PASS | V-05 only: `\| ID \| Severity \| Finding \| Domain-Lens \| Owner \| Resolution \|` with explicit Domain-Lens column required |
| C-25 | PASS | PASS | PASS | PASS | PASS | Three separate labeled lines at line boundary in all; R8 axis strips sub-label nesting |
| C-26 | FAIL | PASS | FAIL | PASS | PASS | V-01/V-03 no C1/C2 tokens. V-02/V-04/V-05 use exact token strings with no suffix; double-dash diagnostic boundary |
| C-27 | FAIL | FAIL | PASS | FAIL | PASS | PRE-COMMITMENT block only in V-03 and V-05; sealed after writing; structurally precedes findings |

**Aspirational pass counts:**
- V-01: 11/19 (C-18, C-20, C-22, C-24, C-26, C-27 fail; C-14, C-23 partial)
- V-02: 14/19 (C-24, C-27 fail; C-14, C-23 partial)
- V-03: 12/19 (C-18, C-20, C-22, C-24, C-26 fail; C-14, C-23 partial)
- V-04: 14/19 (C-24, C-27 fail; C-14, C-23 partial)
- V-05: 16/19 (C-14, C-23 partial only)

---

### Score Calculation

```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 19 * 10)

V-01: (5/5 * 60) + (3/3 * 30) + (11/19 * 10) = 60 + 30 + 5.79  = 95.8
V-02: (5/5 * 60) + (3/3 * 30) + (14/19 * 10) = 60 + 30 + 7.37  = 97.4
V-03: (5/5 * 60) + (3/3 * 30) + (12/19 * 10) = 60 + 30 + 6.32  = 96.3
V-04: (5/5 * 60) + (3/3 * 30) + (14/19 * 10) = 60 + 30 + 7.37  = 97.4
V-05: (5/5 * 60) + (3/3 * 30) + (16/19 * 10) = 60 + 30 + 8.42  = 98.4
```

**Rank: V-05 (98.4) > V-02 = V-04 (97.4) > V-03 (96.3) > V-01 (95.8)**

---

### Excellence Signals — from V-05

**1. Three-clause labeled formula at line boundary closes string-matchability gap completely.**
Each of `WORSE rows:`, `BETTER rows:`, `Conclusion:` appears on its own line at a consistent indent. A scan tool retrieves each clause independently. The prohibition is stated as a structural contract (not a content contract): a verdict naming all rows in prose fails C-25 even if the content is correct. V-01 established this axis; V-05 carries it cleanly.

**2. PRE-COMMITMENT as a distinct named output block separates pre-commitment from findings structurally.**
V-05 extracts the initial position from the READ RECEIPT template into a standalone `PRE-COMMITMENT: [Role Name]` element that is sealed before the diff is read. The ordering receipt → PRE-COMMITMENT → findings is independently verifiable by reading the output text top-to-bottom. A reviewer needs no process knowledge to confirm timing — position in the output text is the evidence.

**3. Domain-Lens column in the findings table makes gate compliance per-finding auditable.**
V-05 requires `| ID | Severity | Finding | Domain-Lens | Owner | Resolution |` for all findings tables. The Domain-Lens cell must carry a gate compliance value (`Passed`) per row, making each finding's domain-lens gate result checkable by column scan without re-running the gate. No prior variation required a table structure; all used numbered list format.

**4. Phase C entry condition makes PRE-COMMITMENT a structural pipeline gate, not just an instruction.**
V-05's pipeline declaration explicitly names PRE-COMMITMENT blocks as part of Phase C's exit condition: `PRE-COMMITMENT blocks precede findings tables`. This makes C-27 a phase-gate compliance item alongside C-26 tokens — absence of a PRE-COMMITMENT block is a phase violation, not a format issue.

**Residual gap (C-14, C-23):** All variations are PARTIAL on C-14 — the IA anchor is a standalone section, never a finding-level reference to IA as counterpoint. C-23 is PARTIAL because the READ RECEIPT fields (d) cost row and (e) initial position are structurally correct but distributed to PRE-COMMITMENT by C-27 design. These are the two criteria left open for R9.

---

```json
{"top_score": 98.4, "all_essential_pass": true, "new_patterns": ["Three-clause Budget verdict at line boundary: each clause on its own labeled line makes WORSE rows, BETTER rows, and Conclusion independently string-matchable by clause — a verdict embedding rows in prose fails even if content is correct", "PRE-COMMITMENT as a distinct sealed output block before findings: structural ordering receipt→PRE-COMMITMENT→findings makes timing independently verifiable from output text without process knowledge", "Domain-Lens column in findings table: per-finding gate compliance value makes domain-lens gate results auditable by column scan without re-running the gate", "Phase C pipeline gate names PRE-COMMITMENT block as a phase exit condition: C-27 becomes a structural violation rather than a format issue when codified in the pipeline declaration"]}
```
