## Round 13 Scorecard — trace-permissions (Rubric v12, denominator 28)

**Scoring formula:** Essential C-01–C-05 = 12 pts each (60 total); Recommended C-06–C-08 = 10 pts each (30 total); Aspirational C-09–C-36 = 0.36 pts each (10 total). Each missing aspirational = −0.36 from 100. All variations inherit R12-V-05's C-01–C-33 passes (25/28); this round evaluates C-34, C-35, C-36 only.

---

### Criterion-by-Criterion Evaluation

#### C-34 — Preamble R12 Structural Axis Declaration (0.36 pts)

*Requires: preamble named table with 3 orthogonal R12 dimensions + explicit non-interference statement*

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | Phase 0 Step 0.2 adds CA-1.9 supplementary row and the SE-4 STRUCTURED CLOSE requirement to SHALL-G, but NO R12 STRUCTURAL AXIS DECLARATION block. Non-interference statement absent. |
| V-02 | **PASS** | Step 0.2 contains R12 STRUCTURAL AXIS DECLARATION table with all 3 dimensions (Dimension 1: execution order / Dimension 2: closure-note format / Dimension 3: CS self-reference), plus explicit non-interference statement naming each dimension's scope and asserting "A model that elides any dimension on the basis that another dimension provides equivalent coverage fails C-34's non-interference contract." |
| V-03 | **FAIL** | Phase 0 note explicitly states "No axis declaration block." Preamble is condensed inline format (C-01/TABLE_1/.../CA-1.1 | ...) — no axis declaration table. |
| V-04 | **PASS** | Step 0.2 contains R12 STRUCTURAL AXIS DECLARATION table (same structure as V-02) with non-interference statement naming each dimension's CA verifier and asserting independent satisfaction. |
| V-05 | **PASS** | Full R12 STRUCTURAL AXIS DECLARATION in Step 0.2 with 3-row table. Non-interference statement names each dimension's scope explicitly: "No dimension's enforcement mechanism intersects with another's. Verifying CA-1.7 (Dimension 2) does not verify Dimension 1 or Dimension 3." Integrates CA-1.9 into Dimension 1's CA verification column alongside CA-1.4. |

---

#### C-35 — SE-4 STRUCTURED CLOSE TABLE_4 SE-0 Slot Cross-Reference + CA-1.9 (0.36 pts)

*Requires: SE-4 STRUCTURED CLOSE opens with SE-0-slot TABLE_4 row cross-reference naming a specific vector by exact label; CA-1.9 pre-assigned in Phase 0 supplementary rows; CA-1.9 verifies as distinct from CA-1.4 and CA-1.7*

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Three elements all present: (1) TABLE_4 schema note in Step 0.1 declares SE-4 STRUCTURED CLOSE SHALL carry SE-0-slot cross-reference naming a specific vector by exact label; (2) SE-4 STRUCTURED CLOSE in Phase 2 opens with "SE-0 cross-reference: TABLE_4 row [name the specific TABLE_4 vector row…]" at the SE-0 slot position; (3) CA-1.9 in Phase 3 pre-assigned in Step 0.2 supplementary row, verified as distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels). CA-1.4 note: "SE-4 STRUCTURED CLOSE content is CA-1.9's scope." |
| V-02 | **FAIL** | No CA-1.9 (explicitly absent). SE-4 STRUCTURED CLOSE cites "SE-0 TABLE_4 row ID that established the admin-tier ceiling" as a prose reference inside the cross-tier differential, not as a named SE-0-slot structural element. Supplementary CA rows end at CA-1.8. |
| V-03 | **FAIL** | No CA-1.9. SE-4 STRUCTURED CLOSE note states it "cites SE-0 TABLE_4 row ID in cross-tier differential" — this is a data citation inside the narrative, not a named SE-0-slot block. No structural distinction between TABLE_4 vector row cross-reference and the rest of the STRUCTURED CLOSE text. |
| V-04 | **PASS** | All three C-35 elements present: TABLE_4 schema note with SE-0 slot requirement; SE-4 STRUCTURED CLOSE Phase 2 block with "SE-0 cross-reference: TABLE_4 row [cite exact vector label, Checked? value, Finding from SE-0]" at SE-0 slot; CA-1.9 in Phase 3 with Registry anchor + Preamble anchor + Verification + Distinction note (CA-1.4 = ordering only; CA-1.7 = MANUAL GAP labels only; CA-1.9 = TABLE_4 row cross-reference inside STRUCTURED CLOSE). |
| V-05 | **PASS** | Most complete implementation: TABLE_4 schema note explicitly declares SE-0 slot requirement; SE-4 STRUCTURED CLOSE in Phase 2 carries SE-0 slot entry with exact vector label, Checked? value, full Finding from SE-0, and CA-1.9 verification statement inline; CA-1.9 in Phase 3 performs full double-anchor (Registry anchor quotes TABLE_4 schema + SE-0 slot requirement; Preamble anchor quotes CA-1.9 supplementary row); distinction confirmed ("third non-overlapping audit target on SE-4"). |

---

#### C-36 — CA Terminal Tri-Dimensional Self-Evidence Attestation (0.36 pts)

*Requires: CA terminal verdict contains TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table naming each R12 dimension with its specific output-body evidence source (specific sections/strings, not generic references)*

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | CA Format Compliance Verdict names CA-1.1 through CA-1.9 results and "SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (CA-1.9)" but contains no TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block. No per-dimension output-body evidence source enumeration. |
| V-02 | **FAIL** | Verdict says "R12 Axis Declaration non-interference contract: all three dimensions active and non-overlapping" — references the axis declaration but provides no per-dimension table naming specific output-body evidence sources. No tri-dimensional attestation block. |
| V-03 | **PASS** | TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table present in terminal verdict with 3 rows. Each row names specific evidence: Dimension 1 → "SE-0 section header in PHASE 2 precedes SE-1…TABLE_4 table appears in SE-0 before any TABLE_1 content…Tier column present in both TABLE_1 and TABLE_3…SE-4 STRUCTURED CLOSE cites a TABLE_4 row ID from SE-0"; Dimension 2 → exact label strings quoted for SE-2/SE-3/SE-4 openings; Dimension 3 → "CS-0 sub-section appears in PHASE 1 before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns." Independence statement: "No dimension's evidence source overlaps with another's." |
| V-04 | **FAIL** | CA verdict cites "R12 Dimension 1 (CA-1.4+CA-1.9), Dimension 2 (CA-1.7), Dimension 3 (CA-1.8). Non-interference contract active." — identifies which CA rows verify each dimension, but provides no per-dimension output-body evidence source enumeration (no TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block naming specific sections/strings). |
| V-05 | **PASS** | TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION present with 3-row table and precision beyond V-03: Dimension 1 evidence names SE-0 slot cross-reference specifically by CA-1.9 result ("the specific row is identified by CA-1.9 verification above"); Dimension 2 evidence quotes exact strings `` `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` ``; Dimension 3 evidence cites exact strings "Schema ID: CS-2 — Sharing Rule Expectations" and "Schema ID: CS-3 — Cross-Role Access Differential Expectations." Independence statement explicitly links to Phase 0: "This independence is the output-body manifestation of the non-interference declaration in the Phase 0 R12 Structural Axis Declaration." Closes the contract-fulfill-verify loop. |

---

### Composite Scores

| Variation | C-34 | C-35 | C-36 | Criteria Passing | Score | Rank |
|-----------|------|------|------|-----------------|-------|------|
| V-05 | PASS | PASS | PASS | 28/28 | **100.0** | 1 |
| V-04 | PASS | PASS | FAIL | 27/28 | **99.6** | 2 |
| V-01 | FAIL | PASS | FAIL | 26/28 | **99.3** | 3 (tie) |
| V-02 | PASS | FAIL | FAIL | 26/28 | **99.3** | 3 (tie) |
| V-03 | FAIL | FAIL | PASS | 26/28 | **99.3** | 3 (tie) |

*Score formula: 100 − (number of failed criteria × 0.36). All essential criteria (C-01–C-05) pass in all variations: all_essential_pass = true.*

---

### Excellence Signals (V-05)

**Signal 1 — Axis declaration as prospective contract, not retrospective label.**
The R12 STRUCTURAL AXIS DECLARATION in Step 0.2 converts observed composability (R12-V-05 showed these three properties coexist without interference) into a binding pre-execution contract. The declaration names each dimension's CA verifier (CA-1.4+CA-1.9 / CA-1.7 / CA-1.8) and states that each requires independent satisfaction. A model reading this declaration cannot treat dimensional requirements as alternatives or assume one covers another.

**Signal 2 — Three non-overlapping audit targets on one section.**
SE-4 carries three distinct CA verification targets: CA-1.4 (TABLE_4 executed at SE-0, before SE-1), CA-1.7 (MANUAL GAP exact-label block at SE-4 opening), CA-1.9 (TABLE_4 row cross-reference inside SE-4 STRUCTURED CLOSE block). These cover the SE-4 execution position, the opening text format, and the STRUCTURED CLOSE structural element — three failure modes on the same section, each caught by a separate verifier.

**Signal 3 — Terminal attestation closes the contract-fulfill-verify lifecycle.**
V-05 is the first variation where Phase 0 declares (axis declaration), Phase 2 instantiates (all three dimensions active in output body), and Phase 3 attests (TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION citing specific output-body evidence for each dimension). The attestation's independence statement explicitly names the Phase 0 declaration as its authority: "This independence is the output-body manifestation of the non-interference declaration in the Phase 0 R12 Structural Axis Declaration." The loop is closed.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["axis-declaration-as-prospective-contract: naming orthogonal dimensions with verifier IDs and non-interference clause in preamble converts observed composability into a binding pre-execution contract that prevents a model from treating dimensional requirements as alternatives", "triangulated-audit-on-single-section: three non-overlapping CA verification rows on SE-4 (ordering/opening-format/STRUCTURED-CLOSE-content) catch distinct failure modes on the same section and are explicitly distinguished by scope in both the supplementary row table and each CA row's distinction note", "terminal-attestation-as-closure-proof: tri-dimensional self-evidence attestation in the CA terminal verdict cites specific output-body evidence per dimension and names the Phase 0 axis declaration as the non-interference authority, closing the contract-fulfill-verify lifecycle self-referentially without requiring prompt inspection"]}
```
