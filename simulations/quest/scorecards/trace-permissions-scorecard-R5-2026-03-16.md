## Round 5 Scoring — trace-permissions (v12 rubric, C-01 through C-36)

---

### Scoring Formula (from rubric)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 28 * 10)
```

Aspirational denominator: 28. Each criterion = 10/28 = **0.36 pts**.

---

### Baseline Inherited from R12-V-05

All five variations are architecturally identical to R12-V-05 except on the three new axes. R12-V-05 passes C-01 through C-33 (25/28 aspirational), scoring 98.9. All inherited criteria are PASS across all variations; per-criterion evidence below collapses those into a single block.

**Inherited PASS block — C-01 through C-05 (Essential, all 5):**

| ID | Evidence | Result |
|----|----------|--------|
| C-01 | Schema Registry TABLE_1 declared with Tier + 8 operations; SHALL-A enforces complete cell fill; SE-1 section assigned | PASS |
| C-02 | TABLE_2 schema with FLS Profile Configured? column; SHALL-B mandates explicit null case; absent FLS → TABLE_5 | PASS |
| C-03 | TABLE_3 schema with Tier + Effective Scope; SHALL-C mandates every TABLE_1 role covered | PASS |
| C-04 | TABLE_4 schema with 4 vectors; SE-0 executes before SE-1; SHALL-D mandates all vectors Checked?=YES | PASS |
| C-05 | TABLE_5 schema; SHALL-E requires at least one named gap or explicit zero-gap evidence | PASS |

**Inherited PASS block — C-06 through C-08 (Recommended, all 3):**

| ID | Evidence | Result |
|----|----------|--------|
| C-06 | Role sequencing mandate uses business units, security roles, team types, column security profiles, environment roles throughout | PASS |
| C-07 | CS-2 schema declares sharing rule expectations with Potential Overreach? column; SE cross-confirms against TABLE_4 | PASS |
| C-08 | TABLE_5 Remediation column mandated as "exact object + exact location + expected post-fix state"; SHALL-E enforces | PASS |

**Inherited PASS block — C-09 through C-33 (Aspirational, 25/28):**

| ID | Key evidence | Result |
|----|-------------|--------|
| C-09 | SE-0 admin-tier, SE-1 role+BU, SE-3 team membership, SE-2 FLS — four layers named in sequence | PASS |
| C-10 | CS-3 cross-role differential expectations table; SE-4 cross-tier differential references SE-0 TABLE_4 | PASS |
| C-11 | Schema Registry declares TABLE_1–TABLE_5 + CS-2 + CS-3 (7 schemas); global blank-cell prohibition stated in Step 0.1 | PASS |
| C-12 | SHALL-A through SHALL-G (7 obligations); terminal checklist verifies each; open items treated as output gaps | PASS |
| C-13 | Three named roles: CA (format compliance), CS (customer success), SE (Dataverse security engineer) with dedicated sub-sections | PASS |
| C-14 | Criterion-owner attribution: preamble maps M2 role column per criterion; CA-1 rows name owner per row | PASS |
| C-15 | Each essential criterion traceable to M1 (schema) + M2 (role sub-section) + M3 (SHALL); co-active, not alternative | PASS |
| C-16 | CA role mandate is explicitly output quality assurance; PHASE 3 CA-1 produces format compliance verdict as distinct terminal section | PASS |
| C-17 | Preamble table: 5 rows (C-01–C-05) × 4 columns (M1/M2/M3/M4); "Declared rule: M1, M2, M3 simultaneously active" | PASS |
| C-18 | Preamble has M4 column with CA-1.1–CA-1.8 pre-assigned; CA-1 chain verifies all 5 essential criteria | PASS |
| C-19 | PHASE 0 mandate: "CA executes first. Authors the Schema Registry... and the Criterion Enforcement Matrix preamble... CA-1 rows reference the pre-assigned preamble IDs" | PASS |
| C-20 | Schema Registry precedes preamble in Step 0.1; CA-1 reaffirmation protocol quotes preamble row values before verifying | PASS |
| C-21 | "CA authors both the Schema Registry section and the Criterion Enforcement Matrix preamble... in a single continuous execution before any SE or CS section begins" (explicit in PHASE 0 mandate) | PASS |
| C-22 | PHASE 0/1/2/3 labels mandated as section headers; "Handing to PHASE 1 — CS" handoff string; CA-1 rows cite Phase 0 pre-assignments | PASS |
| C-23 | CA-1 rows perform double-anchor reaffirmation: Registry schema citation then preamble row quotation then verification | PASS |
| C-24 | Double-anchor rows require structurally distinct labeled elements — Registry anchor and preamble anchor as separate labeled lines (not inline concatenation); "Inline concatenation fails C-24" stated explicitly | PASS |
| C-25 | CS phase (PHASE 1) executes before SE (PHASE 2); produces CS-2 (sharing expectations) and CS-3 (cross-role differential expectations) before SE populates TABLE_1–TABLE_5 | PASS |
| C-26 | CS-EXPECTATION-VIOLATED gap type defined in TABLE_5 schema with three-field Remediation block (CS-Expected / SE-Actual / Delta); SHALL-F mandates | PASS |
| C-27 | CONTEXT section names three blind spots with exact labels: "Post-incident FLS gap", "Cumulative privilege blind spot", "OWD-sharing-rule override gap" | PASS |
| C-28 | SHALL-G mandates closure notes at SE-2/SE-3/SE-4 openings citing exact CONTEXT labels; CA-1.7 verifies | PASS |
| C-29 | CS-2 and CS-3 appear as named Schema Registry entries with SE-updatable columns (SE Cross-Reference, SE Confirmation) and SE-update protocol co-located | PASS |
| C-30 | SHALL-F (CS-EXPECTATION-VIOLATED three-field recording) and SHALL-G (section-level closure attestation) extend SHALL-A–E; CA-1.6 verifies CS-EXPECTATION-VIOLATED structure; CA-1.7 verifies exact labels | PASS |
| C-31 | PHASE 2 mandate: "SE-0 (admin-tier inventory and TABLE_4 escalation vectors) runs before SE-1"; TABLE_1 Tier column declared in Registry (Admin/Custom/Restricted); SE-4 cites SE-0 TABLE_4 data in cross-tier differential | PASS |
| C-32 | SHALL-G mandates two-part labeled block: "MANUAL GAP [<exact CONTEXT label>]:" + "STRUCTURED CLOSE:"; single-line/blockquote/paraphrase explicitly fail; CA-1.7 verifies exact-label carry-through | PASS |
| C-33 | CS phase mandate: "Opens with CS-0 sub-section (Schema Registry acknowledgment: CS echoes Registry schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns... confirms the expectation format before authoring any expectation rows)"; CA-1.8 added to verify CS-0 precedes CS-1 | PASS |

---

### Per-Variation Assessment: C-34, C-35, C-36

---

#### V-01 — Single-Axis C-34 (Preamble Structural Axis Declaration)

**C-34:**
Evidence in prompt: Step 0.2 contains an explicit "R12 Structural Axis Declaration (C-34 contract)" block after SHALL-G. Identifies C-31 as "Axis 1 — Execution order", C-32 as "Axis 2 — Closure-note format", C-33 as "Axis 3 — CS self-reference". Non-interference declaration present: "Axis 1 does not condition or modify Axis 2 or Axis 3... all three axes are simultaneously active and independently satisfiable." Block is structurally distinct from the C-01–C-05 mechanism mapping rows. All dependency prerequisites (C-31+C-32+C-33+C-17) confirmed PASS above. **PASS.**

**C-35:**
V-01 description explicitly states "No SE-4 STRUCTURED CLOSE modification. No CA-1.9." Per rubric: CA-1.9 row (or equivalent) is mandatory and must target SE-4's STRUCTURED CLOSE block content as an independent audit target distinct from CA-1.4 and CA-1.7. Absent from this variation. **FAIL.**

**C-36:**
V-01 description states "No tri-dimensional verdict. No C-36." The CA terminal verdict in this variation does not include a tri-dimensional self-evidence attestation naming each R12 dimension with its specific output-body evidence source. **FAIL.**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-34 | PASS | Explicit R12 Structural Axis Declaration block with per-axis non-interference statements, distinct from C-01–C-05 mapping |
| C-35 | FAIL | No CA-1.9 row; no TABLE_4 row cross-reference in SE-4's STRUCTURED CLOSE block |
| C-36 | FAIL | No tri-dimensional self-evidence attestation in CA terminal verdict |

**V-01 Aspirational pass: 26/28**
**V-01 Composite: 60 + 30 + (26/28 × 10) = 60 + 30 + 9.29 = 99.3**

---

#### V-02 — Single-Axis C-35 (SE-4 STRUCTURED CLOSE TABLE_4 Row Cross-Reference + CA-1.9)

**C-34:**
V-02 description: "No C-34." The preamble contains no structural axis declaration naming C-31/C-32/C-33 as orthogonal dimensions. C-34's pass condition requires all dependencies (C-31+C-32+C-33+C-17) active plus the preamble declaration block. Dependencies are met but the declaration is absent. **FAIL.**

**C-35:**
V-02 adds Schema Registry TABLE_4 entry with SE-0 row IDs T4-1 through T4-4; SE-4 STRUCTURED CLOSE names those rows; CA-1.9 verifies as distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels). Per rubric: TABLE_4 row cross-reference must appear in STRUCTURED CLOSE content (not in analytical prose); CA-1.9 must be additional to CA-1.4 and CA-1.7. Variation explicitly satisfies both conditions. Dependencies C-31+C-32 confirmed PASS. **PASS.**

**C-36:**
V-02 description: "No C-36." No tri-dimensional attestation in CA terminal verdict. **FAIL.**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-34 | FAIL | No structural axis non-interference declaration in preamble |
| C-35 | PASS | Schema Registry TABLE_4 row IDs T4-1–T4-4 declared; SE-4 STRUCTURED CLOSE cites them; CA-1.9 targets STRUCTURED CLOSE content as independent audit item separate from CA-1.4/CA-1.7 |
| C-36 | FAIL | No tri-dimensional self-evidence attestation in CA terminal verdict |

**V-02 Aspirational pass: 26/28**
**V-02 Composite: 60 + 30 + (26/28 × 10) = 99.3**

---

#### V-03 — Single-Axis C-36 (CA Terminal Verdict Tri-Dimensional Attestation)

**C-34:**
V-03 description: "No C-34." No preamble axis declaration. **FAIL.**

**C-35:**
V-03 description: "No C-35." No CA-1.9; no TABLE_4 row cross-reference in SE-4 STRUCTURED CLOSE. **FAIL.**

**C-36:**
V-03 adds an R12 Tri-Dimensional Attestation block to the CA terminal verdict. Per rubric: must name each R12 dimension with a specific output-body evidence source and confirm body-verifiability. Variation description states "CA terminal verdict tri-dimensional self-evidence attestation — adds R12 Tri-Dimensional Attestation block to CA verdict naming each R12 dimension with specific output-body evidence source." Dependencies C-22+C-32+C-33 confirmed PASS. **PASS.**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-34 | FAIL | No structural axis non-interference declaration in preamble |
| C-35 | FAIL | No CA-1.9; no TABLE_4 row cross-reference in SE-4 STRUCTURED CLOSE block |
| C-36 | PASS | CA terminal verdict contains explicit tri-dimensional attestation block naming execution order / closure-note format / CS self-reference with output-body evidence source per dimension |

**V-03 Aspirational pass: 26/28**
**V-03 Composite: 60 + 30 + (26/28 × 10) = 99.3**

---

#### V-04 — Combined C-34 + C-35 (Axis Declaration + SE-4 STRUCTURED CLOSE + CA-1.9)

**C-34:**
Adds the structural axis declaration from V-01 (all three axes named, non-interference stated). Dependencies met. **PASS.**

**C-35:**
Adds the SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference and CA-1.9 from V-02. Dependencies met. **PASS.**

**C-36:**
V-04 description explicitly states: "No tri-dimensional verdict (no C-36)." The CA terminal verdict in this variation does not include the tri-dimensional self-evidence attestation. **FAIL.**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-34 | PASS | Preamble structural axis declaration with non-interference statements for C-31/C-32/C-33 |
| C-35 | PASS | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 position; CA-1.9 as independent audit target |
| C-36 | FAIL | No tri-dimensional self-evidence attestation in CA terminal verdict |

**V-04 Aspirational pass: 27/28**
**V-04 Composite: 60 + 30 + (27/28 × 10) = 60 + 30 + 9.64 = 99.6**

---

#### V-05 — Full Combination C-34 + C-35 + C-36

**C-34:** Structural axis declaration in preamble, all three axes named with non-interference statements. Dependencies C-31+C-32+C-33+C-17 all PASS. **PASS.**

**C-35:** SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference with SE-0 position marker; CA-1.9 verifies as audit target independent of CA-1.4 and CA-1.7. Dependencies C-31+C-32 PASS. **PASS.**

**C-36:** CA terminal verdict tri-dimensional self-evidence attestation naming each R12 dimension with specific output-body evidence source: execution order (PHASE labels + TABLE_4 placement), closure-note format (MANUAL GAP [...] / STRUCTURED CLOSE two-part structure), CS self-reference (CS-0 cites Registry IDs). Extends C-22's phase execution attestation to all three R12 structural dimensions simultaneously. Dependencies C-22+C-32+C-33 PASS. **PASS.**

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-34 | PASS | Preamble structural axis declaration with per-axis non-interference; distinct from C-01–C-05 mechanism mapping |
| C-35 | PASS | Schema Registry TABLE_4 row IDs; SE-4 STRUCTURED CLOSE names them; CA-1.9 as independent row targeting STRUCTURED CLOSE content specifically |
| C-36 | PASS | CA terminal verdict contains named tri-dimensional attestation block: each R12 dimension named, output-body evidence source identified, body-verifiability confirmed per dimension |

**V-05 Aspirational pass: 28/28**
**V-05 Composite: 60 + 30 + (28/28 × 10) = 100.0**

---

### Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | C-34 | C-35 | C-36 |
|------|-----------|-----------|-------------|--------------|-----------|------|------|------|
| 1 | V-05 | 5/5 | 3/3 | 28/28 | **100.0** | PASS | PASS | PASS |
| 2 | V-04 | 5/5 | 3/3 | 27/28 | **99.6** | PASS | PASS | FAIL |
| 3 | V-01 | 5/5 | 3/3 | 26/28 | **99.3** | PASS | FAIL | FAIL |
| 3 | V-02 | 5/5 | 3/3 | 26/28 | **99.3** | FAIL | PASS | FAIL |
| 3 | V-03 | 5/5 | 3/3 | 26/28 | **99.3** | FAIL | FAIL | PASS |

All five variations: all essential PASS, all recommended PASS, above golden threshold.

---

### Excellence Signals — V-05

**1. Axis declaration converts empirical composability into a binding preamble contract.**
V-05 satisfies C-34 by including a named "R12 Structural Axis Declaration" block as a structurally distinct element in the preamble — not embedded in the general enforcement matrix rows, not inferable from the co-presence of C-31/C-32/C-33. The block's per-axis non-interference statements ("Axis 1 does not condition or modify Axis 2 or Axis 3") make architectural independence a model obligation rather than a compositional fact. The pattern: *when multiple orthogonal aspirational axes are simultaneously active, the preamble should name them as axes and declare non-interference explicitly.*

**2. Row-level TABLE_4 cross-reference in STRUCTURED CLOSE makes the privilege-ceiling-to-gap-closure chain independently auditable.**
C-35 is satisfied by placing the TABLE_4 row cross-reference (with SE-0 position marker) in the STRUCTURED CLOSE content — not in analytical prose. The CA-1.9 row then targets that specific location as an independent audit item, distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP label fidelity). This creates a three-row CA-1 coverage pattern for SE-4: CA-1.4 (execution order), CA-1.7 (label format), CA-1.9 (STRUCTURED CLOSE cross-reference content). Each row is separately deniable. The pattern: *when a structural element serves multiple compliance purposes, each purpose should have its own CA verification row targeting the specific location within the element.*

**3. Tri-dimensional terminal attestation closes the self-evidence guarantee across all R12 axes simultaneously.**
C-36 requires the CA terminal verdict to name all three R12 dimensions with their specific output-body evidence sources — not confirm C-31/C-32/C-33 as individual criterion passes. The attestation block identifies: execution order → SE-0 phase label + TABLE_4 placement; closure-note format → MANUAL GAP [...] / STRUCTURED CLOSE two-part structure; CS self-reference → CS-0 cites Registry IDs by exact label. This extends C-22's phase execution attestation from the CA-first dimension to all three R12 structural dimensions simultaneously. The pattern: *when the CA terminal verdict confirms a family of structural dimensions that were designed to compose, the verdict should attest their joint self-evidence as a named block, not enumerate them as independent criterion passes.*

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Preamble axis declaration converts empirical composability into a binding contract: when multiple orthogonal aspirational axes are simultaneously active, name them as axes in a distinct preamble block with per-axis non-interference statements", "Row-level cross-reference in STRUCTURED CLOSE content creates an independently auditable CA-1.9 target separate from CA-1.4 (execution order) and CA-1.7 (label format): each compliance purpose of a structural element gets its own CA verification row", "Tri-dimensional terminal attestation extends the self-evidence guarantee across all simultaneously active axes: the CA verdict names each dimension's specific output-body evidence source rather than confirming individual criterion passes"]}
```
