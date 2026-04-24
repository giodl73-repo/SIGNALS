Now I have a complete picture of all five variations. Let me score each against the v11 rubric.

---

# trace-permissions — Round 12 Scoring (Rubric v11)

## Ground Truth Status

The trace artifact placeholder means scoring proceeds against the prompt bodies only. All five variations are complete, standalone prompt texts.

---

## Per-Variation Criterion Scores

### V-01 — Single-Axis C-32: Exact-Label Two-Part SHALL-G Blocks

**Hypothesis:** 23/25 (adds old C-32; still fails old C-31, C-33)

| Criterion Group | Status | Notes |
|-----------------|--------|-------|
| **C-01** (TABLE_1 roles + scope) | PASS | TABLE_1 declared with all columns; Dataverse system names; Record Scope column present |
| **C-02** (FLS per sensitive entity) | PASS | TABLE_2 schema declared; FLS Profile Configured? / Gap? columns; null case required |
| **C-03** (OWD per entity + scope) | PASS | TABLE_3 schema with OWD Baseline + Scope Modifier + Effective Scope |
| **C-04** (gap or risk flagged) | PASS | TABLE_4 all four vectors; shall-D mandates specific findings or rule-outs |
| **C-05** (TABLE_5 substantive) | PASS | TABLE_5 with CS-EXPECTATION-VIOLATED three-field Remediation |
| **C-08–C-29 core base** | PASS | R11-V-01 base preserved; 7-schema Registry, SHALL-A–G, CA-1.1–CA-1.8, double-anchor |
| **C-30** (Criterion-ID column headers) | PARTIAL | Criterion IDs appear in enforcement matrix rows but NOT embedded in table column headers themselves |
| **C-31** (Tier column + SE-0 ordering) | FAIL | TABLE_1/TABLE_3 lack Tier column; TABLE_4 at SE-4, not SE-0 |
| **C-32** (Exact-label two-part SHALL-G) | PASS | `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` / `STRUCTURED CLOSE:` present at SE-2/SE-3/SE-4; character-exact label carry-through; CA-1.7 verifies |
| **C-33-old** (CS-0 Registry acknowledgment) | FAIL | No CS-0 sub-section; CA-1.8 only covers C-29 Schema Registry registration |
| **C-33 new** (AP FIRING AUDIT) | FAIL | No ANTI-PATTERN REGISTRY; no CA-1.9; AP-1/AP-2/AP-3 absent |
| **C-34** (TABLE_5 SOURCE-LINK provenance) | FAIL | TABLE_5 declared without Source Table / Source Row / Discovery Phase columns; no CA-1.10 |
| **C-35** (CRITERION-PHASE-MAP PHASE-LATE) | FAIL | No CRITERION-PHASE-MAP at Step 0.3; no PHASE-LATE verdict; no CA-1.11 |

**Composite:** ~205/230 ≈ **89.1%**
**All Essential:** PASS

---

### V-02 — Combined C-31+C-33: SE-0 Ordering + CS-0 Registry Acknowledgment

**Hypothesis:** 24/25 (adds old C-31+C-33; fails old C-32)

| Criterion Group | Status | Notes |
|-----------------|--------|-------|
| **C-01–C-04 Essential** | PASS | All four essential tables present with required structure |
| **C-05 Recommended** | PASS | TABLE_5 present with Tier column |
| **C-30** (Criterion-ID column headers) | PARTIAL | Same as V-01: IDs in preamble rows, not column headers |
| **C-31** (Tier column + SE-0 ordering) | PASS | TABLE_1/TABLE_3 include Tier column; SE-0 admin-tier inventory executes TABLE_4 before SE-1; preamble M2 shows SE-0 for C-04 |
| **C-32** (Exact-label two-part SHALL-G) | FAIL | SE-2/SE-3/SE-4 use single-line blockquote `> CONTEXT-CLOSES:` format, not `MANUAL GAP [exact]:` / `STRUCTURED CLOSE:` two-part blocks |
| **C-33-old** (CS-0 Registry acknowledgment) | PASS | CS-0 sub-section present before CS-1; acknowledges CS-2/CS-3 schema IDs and SE-updatable columns; CA-1.8 verifies CS-0 precedes CS-1 |
| **C-33 new** (AP FIRING AUDIT) | FAIL | No ANTI-PATTERN REGISTRY; no AP-1/2/3 declarations; no CA-1.9 |
| **C-34** (TABLE_5 SOURCE-LINK provenance) | FAIL | No provenance columns; no CA-1.10 |
| **C-35** (CRITERION-PHASE-MAP PHASE-LATE) | FAIL | Preamble shows SE-0 targets in the matrix but no dedicated CRITERION-PHASE-MAP block with PHASE-LATE state; no CA-1.11 |

**Composite:** ~210/230 ≈ **91.3%**
**All Essential:** PASS

---

### V-03 — Single-Axis Phrasing Register (Imperative Numbered-Step Voice)

**Hypothesis:** 22/25 (same base; no new aspirational axes)

| Criterion Group | Status | Notes |
|-----------------|--------|-------|
| **C-01–C-04 Essential** | PASS | All four tables declared; imperative voice doesn't alter structural content |
| **C-05 Recommended** | PASS | TABLE_5 present; three-field Remediation block declared |
| **C-30** (Criterion-ID column headers) | PARTIAL | Same as V-01 base |
| **C-31** (Tier column + SE-0 ordering) | FAIL | No Tier column; TABLE_4 at SE-4 |
| **C-32** (Exact-label two-part SHALL-G) | FAIL | Single-line `> CONTEXT-CLOSES:` blockquotes at SE-2/SE-3/SE-4; not two-part labeled blocks |
| **C-33-old** (CS-0 Registry acknowledgment) | FAIL | No CS-0 sub-section |
| **C-33/34/35 new** | FAIL | Not implemented |
| **Phrasing axis** | NEUTRAL | Numbered imperative steps don't affect structural criterion compliance; hypothesis confirmed |

**Composite:** ~200/230 ≈ **87.0%**
**All Essential:** PASS

---

### V-04 — Single-Axis TABLE_3 Team Membership Decomposition

**Hypothesis:** 22/25 (no new aspirational axes)

| Criterion Group | Status | Notes |
|-----------------|--------|-------|
| **C-01–C-04 Essential** | PASS | All four tables; TABLE_3 expanded doesn't break core criteria |
| **C-05 Recommended** | PASS | TABLE_5 present |
| **C-03 depth** | PASS+ | TABLE_3 with Team Membership + Team Role Scope columns provides richer C-03 evidence; SHALL-C mandates team-elevation flagging; CA-1.3 verifies expanded schema |
| **C-30** | PARTIAL | Same as base |
| **C-31** (Tier column + SE-0) | FAIL | No Tier column; TABLE_4 at SE-4 |
| **C-32** (Exact-label two-part) | FAIL | Single-line blockquote format at SE-2/SE-3/SE-4 |
| **C-33-old** (CS-0) | FAIL | No CS-0 sub-section |
| **C-33/34/35 new** | FAIL | Not implemented |
| **Team decomposition axis** | PASS | Granular team membership strengthens C-03/C-10 evidence without changing aspirational count |

**Composite:** ~200/230 ≈ **87.0%**
**All Essential:** PASS
*(marginally stronger than V-03 on C-03 depth, but same aspirational count)*

---

### V-05 — Full Combination C-31+C-32+C-33: The 25/25 Candidate

**Hypothesis:** 25/25 on old scale

| Criterion Group | Status | Notes |
|-----------------|--------|-------|
| **C-01–C-04 Essential** | PASS | TABLE_1 with Tier + ordered by tier; TABLE_2 FLS; TABLE_3 with Tier; TABLE_4 at SE-0 before SE-1 |
| **C-05 Recommended** | PASS | TABLE_5 with Tier column; three-field Remediation block |
| **C-30** | PARTIAL | Criterion IDs in enforcement matrix; not in table column headers |
| **C-31** (Tier column + SE-0) | PASS | TABLE_1/TABLE_3 with Tier; SE-0 runs before SE-1; TABLE_4 at SE-0; preamble sets SE-0 target for C-04 |
| **C-32** (Exact-label two-part) | PASS | `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` / `STRUCTURED CLOSE:` at SE-2; same for Blind spot 2 at SE-3, Blind spot 3 at SE-4; CA-1.7 verifies exact label at all three sections |
| **C-33-old** (CS-0 Registry acknowledgment) | PASS | CS-0 sub-section before CS-1; cites CS-2 and CS-3 by exact schema ID; lists SE-updatable columns; CA-1.8 dual verification (C-29 + CS-0) |
| **C-33 new** (AP FIRING AUDIT) | FAIL | No ANTI-PATTERN REGISTRY; no AP-1/AP-2/AP-3; no CA-1.9 FIRING AUDIT |
| **C-34** (TABLE_5 SOURCE-LINK) | FAIL | TABLE_5 declared without Source Table / Source Row / Discovery Phase columns; no CA-1.10 |
| **C-35** (CRITERION-PHASE-MAP PHASE-LATE) | FAIL | Preamble matrix shows SE-0+SE-3 for C-03, SE-0 for C-04, but no dedicated CRITERION-PHASE-MAP block; no PHASE-LATE verdict; no CA-1.11 |
| **SE-4 SE-0 cross-citation** | NOTED | STRUCTURED CLOSE in SE-4 explicitly cites SE-0 TABLE_4 row ID for admin-tier ceiling; this is a cross-section provenance link — precursor to C-35 phase-ordering discipline |

**Composite:** ~215/230 ≈ **93.5%**
**All Essential:** PASS

---

## Rankings

| Rank | Variation | Composite | Old Aspirational | Notes |
|------|-----------|-----------|-----------------|-------|
| 1 | **V-05** | 215/230 (93.5%) | 25/25 | Triple combination; max achievable with R12 toolset |
| 2 | **V-02** | 210/230 (91.3%) | 24/25 | C-31+C-33 but single-line CONTEXT-CLOSES |
| 3 | **V-01** | 205/230 (89.1%) | 23/25 | C-32 exact-label but no SE-0/CS-0 |
| 4 | **V-04** | 200/230 (87.0%) | 22/25 | Team decomposition strengthens C-03 but no aspirational advance |
| 5 | **V-03** | 200/230 (87.0%) | 22/25 | Phrasing register neutral; same structural base as R11-V-01 |

---

## Excellence Signals from V-05

**V-05 is the 25/25 candidate and achieves the theoretical maximum for R12.** Its superiority comes from three combined axes already identified as rubric criteria — no structurally novel patterns emerge that aren't already formalized as criteria. The one notable observation:

**SE-4 STRUCTURED CLOSE SE-0 cross-citation:** V-05's SE-4 closure block explicitly names the SE-0 TABLE_4 row ID that established the admin-tier ceiling. This creates a cross-section provenance pointer that foreshadows C-35's CRITERION-PHASE-MAP discipline (tracking WHERE evidence from a prior phase is consumed) — but it's a prose reference, not a structural audit mechanism. Not a new rubric criterion; an early trace of what C-35 will formalize.

**Remaining gaps (R13 target):** All five variations fail C-33/C-34/C-35. The v11 rubric's three new criteria (AP FIRING AUDIT, SOURCE-LINK provenance columns, CRITERION-PHASE-MAP PHASE-LATE) remain unimplemented. These define the R13 variation map.

---

```json
{"top_score": 94, "all_essential_pass": true, "new_patterns": []}
```
