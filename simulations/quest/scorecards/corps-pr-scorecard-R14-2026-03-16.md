## Round 14 Scorecard — corps-pr

---

### Baseline Summary

R13 V-05 against v12 fails exactly three criteria:
- **C-39**: UNSATISFIED path in a separate code fence — per-field verdicts and terminal verdict split across two blocks
- **C-40**: Format rules allow "or" inline-cell path — slot compliance is O(cell-content), not O(1) column-count
- **C-41**: No structural enforcement levels table in pipeline declaration

---

### Per-Variation Scoring

#### V-01 — C-39 Self-Contained Block

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-41) | 31/33 | 9.39 |
| **Total** | | **99.39** |

**Aspirational detail — new criteria only:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-39 | PASS | STEP 2 block replaces separate UNSATISFIED fence with conditional derivation line inside `## C2 RESULT`: `All five PRESENT: C2 RESULT: SATISFIED` / `Any ABSENT: C2 RESULT: UNSATISFIED -- field (x): [label]` — both paths produce terminal verdict within the same named block |
| C-40 | FAIL | Format rules retain "or" alternative path: "Alternative form (C-38 compliant only): `[IA-VERDICT: X] \| [ROLE-MECHANISM: Y]` in a single Description cell." Column headers appear in the primary template but the "or" path is still present, making slot compliance O(cell-content) via that path |
| C-41 | FAIL | No `Structural enforcement levels` section in pipeline declaration. C-36/C-37/C-38 criterion families are not assigned to named structural layers |

C-09 through C-38: all PASS (inherited from R13 V-05).

---

#### V-02 — C-40 Column-Header Promotion

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-41) | 31/33 | 9.39 |
| **Total** | | **99.39** |

**Aspirational detail — new criteria only:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-39 | FAIL | STEP 2 still uses separate `If any field is ABSENT:` code fence for the UNSATISFIED terminal verdict — per-field rows in the main block, terminal verdict in an adjacent fence; cross-block reading required in the failure case |
| C-40 | PASS | "or" path explicitly removed: "The 'or' path (inline labels within a single Description cell) is C-38 compliant but C-40 noncompliant -- do not use it. Only separate column headers satisfy C-40." Column headers are the only valid form; slot compliance is O(1) column-count |
| C-41 | FAIL | No `Structural enforcement levels` section in pipeline declaration |

C-09 through C-38: all PASS.

---

#### V-03 — C-41 Three-Level Structural Partition

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-41) | 31/33 | 9.39 |
| **Total** | | **99.39** |

**Aspirational detail — new criteria only:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-39 | FAIL | STEP 2 retains separate UNSATISFIED fence — same structure as R13 V-05 baseline; variation description explicitly states "C-39 and C-40 are not active in V-03 output" |
| C-40 | FAIL | "or" path retained with note: "the alternative form satisfies C-38 but does not satisfy C-40." Note labels it C-40-noncompliant but does not remove it; path remains available, making slot compliance still O(cell-content) via that route |
| C-41 | PASS | `Structural enforcement levels [C-41]` section present in pipeline declaration: exit-condition level → C-36; block level → C-37/C-39; table-column level → C-38/C-40. Each level independently auditable without reading output. No two criterion families share a level |

C-09 through C-38: all PASS.

---

#### V-04 — C-39 + C-41 (Block + Declaration)

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-41) | 32/33 | 9.70 |
| **Total** | | **99.70** |

**Aspirational detail — new criteria only:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-39 | PASS | STEP 2 uses conditional derivation inside the C2 RESULT block (V-01 change): `All five PRESENT: C2 RESULT: SATISFIED -- all five fields PRESENT` / `Any ABSENT: C2 RESULT: UNSATISFIED -- field (x): [label of absent field]` — terminal verdict is derived from per-field rows within the same block; no separate fence |
| C-40 | FAIL | Format rules retain "or" path with note: "alternative form does not satisfy C-40." The path is still present in the template rules, making slot compliance O(cell-content) via that route; the structural enforcement levels section DECLARES C-40 at the table-column level but the output template does not enforce it |
| C-41 | PASS | Same `Structural enforcement levels [C-41]` section as V-03: exit-condition → C-36, block → C-37/C-39, table-column → C-38/C-40. C-41 requires the DECLARATION to name the partition, which V-04 does; it does not require C-40 to pass in output to satisfy C-41 independently |

C-09 through C-38: all PASS.

**Note on C-41 + C-40 interaction:** V-04 tests the rubric's flagged edge case — does block self-containment + declared partition (without column enforcement) satisfy C-41? Answer: yes. The declaration correctly assigns C-40 to the table-column level. C-41 audits the declaration; C-40 audits the output table. They are orthogonal.

---

#### V-05 — Full Integration: C-39 + C-40 + C-41

| Band | Pass | Score |
|------|------|-------|
| Essential (C-01–C-05) | 5/5 | 60.00 |
| Recommended (C-06–C-08) | 3/3 | 30.00 |
| Aspirational (C-09–C-41) | 33/33 | 10.00 |
| **Total** | | **100.00** |

**Aspirational detail — new criteria only:**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-39 | PASS | STEP 2: `[derive terminal verdict from per-field lines above -- write exactly one:] All five PRESENT: C2 RESULT: SATISFIED -- all five fields PRESENT / Any ABSENT: C2 RESULT: UNSATISFIED -- field (x): [label of absent field]`. C-37/C-39 compliance note: "terminal verdict is in this same block, derived from the per-field rows above; no separate fence carries the verdict; a reviewer reads one block to find evidence + conclusion." |
| C-40 | PASS | "[IA-VERDICT] and [ROLE-MECHANISM] MUST be column headers -- no inline-cell alternative." Format rules: "There is no inline-cell 'or' path -- the alternative form ... satisfies C-38 but fails C-40 and must not be used." Column headers are mandatory; slot compliance is O(1) column-count by column-header structure |
| C-41 | PASS | `Structural enforcement levels [C-41]` section: exit-condition level → C-36 (ordering as Phase C exit-condition violation); block level → C-37/C-39 (per-field enumeration and self-containment within C2 RESULT block); table-column level → C-38/C-40 (named schema slots as column headers, no inline-cell path). "Each level is independently auditable without reading adjacent levels. No two criterion families share a level." |

**Full aspirational pass trace (all 33):**

| C | Pass? | Key evidence |
|---|-------|-------------|
| C-09 | PASS | Phase D: "Mechanism: [architectural property of the code -- not perspective difference]" |
| C-10 | PASS | Phase E: "sign-off: [role who confirms before merge]" |
| C-11 | PASS | Phase B (IA) precedes Phase C (technical roles) in pipeline |
| C-12 | PASS | Perspective-label ban requires architectural mechanism in Mechanism lines |
| C-13 | PASS | 5-item ban-to-fix table with banned phrases enumerated |
| C-14 | PASS | F-01 IA-RESPONSE forces IA counterpoint in every technical role findings table |
| C-15 | PASS | Domain-lens gate: binary test "Would only [this role] raise this finding?" + rewrite (Step B) + drop consequence |
| C-16 | PASS | AMEND SCOPE structured block with 5 named fields |
| C-17 | PASS | Phase B cost ledger frames status quo in cost terms with maintenance/incident/integration/regression rows |
| C-18 | PASS | 5-phase pipeline with named entry/exit/gates per phase |
| C-19 | PASS | 4-row × 3-column cost ledger + Budget verdict + Budget strength terminal fields |
| C-20 | PASS | Phase C C1 pre-flight verifies Phase B exit; READ RECEIPT ensures per-role IA read before findings |
| C-21 | PASS | Net direction column (WORSE/BETTER/NEUTRAL) per row; Budget verdict three-clause formula names rows |
| C-22 | PASS | Phase C entry: exactly two named sub-conditions C1 (phase-level) + C2 (per-role) |
| C-23 | PASS | STEP 1 READ RECEIPT block with 5 named fields, required before any C2 RESULT |
| C-24 | PASS | Findings table includes Domain-Lens column with gate compliance per finding |
| C-25 | PASS | Budget verdict: "WORSE rows:" / "BETTER rows:" / "Conclusion:" on separate labeled lines |
| C-26 | PASS | C1 RESULT: ALL CLEAR / BLOCKED; C2 RESULT: SATISFIED / UNSATISFIED — exact result tokens |
| C-27 | PASS | STEP 3 PRE-COMMITMENT precedes STEP 4 findings; "before reading diff" |
| C-28 | PASS | Each Budget verdict clause on its own line, label at line start |
| C-29 | PASS | "[PRE-COMMITMENT SEALED]" as distinct closing line before diff content |
| C-30 | PASS | Phase C exit item (5): "PRE-COMMITMENT blocks precede findings tables [C-27]" |
| C-31 | PASS | F-01 IA-RESPONSE Description cell requires IA verdict AND role mechanism in same finding entry |
| C-32 | PASS | READ RECEIPT field (e): "valid: inline value OR cross-reference 'see PRE-COMMITMENT block: [row]'" |
| C-33 | PASS | "C2 scope is receipt completeness -- not Phase B" stated in STEP 2; C-33 scope check note present |
| C-34 | PASS | F-01 Type = IA-RESPONSE mandatory; visible Type column in findings table |
| C-35 | PASS | STEP 1 (READ RECEIPT) must precede STEP 2 (C2 RESULT); C-36 compliance note enforces this |
| C-36 | PASS | Phase C exit item (3): READ RECEIPT before C2 RESULT ordering named as Phase C exit-condition failure |
| C-37 | PASS | C2 RESULT block enumerates (a)–(e) with PRESENT/ABSENT per field as separate labeled lines |
| C-38 | PASS | [IA-VERDICT] and [ROLE-MECHANISM] as named schema slots visible in output (as column headers) |
| C-39 | PASS | Conditional derivation in same block; no separate fence for UNSATISFIED path |
| C-40 | PASS | Column headers mandatory; "or" path removed and explicitly prohibited |
| C-41 | PASS | Three-level partition declared: exit-condition/block/table-column with criterion family assignments |

---

### Ranking

| Rank | Variation | Score | Fails |
|------|-----------|-------|-------|
| 1 | **V-05** | **100.00** | none |
| 2 | V-04 | 99.70 | C-40 |
| 3 | V-01 | 99.39 | C-40, C-41 |
| 3 | V-02 | 99.39 | C-39, C-41 |
| 3 | V-03 | 99.39 | C-39, C-40 |

---

### Excellence Signals (from V-05)

**Signal 1 — Conditional derivation eliminates the dual-block UNSATISFIED split.**
The C2 RESULT block always produces its terminal verdict inline via a single conditional line: `All five PRESENT: C2 RESULT: SATISFIED -- all five fields PRESENT / Any ABSENT: C2 RESULT: UNSATISFIED -- field (x): [label]`. This means a reviewer always finds per-field evidence + conclusion in one named block regardless of outcome. The SATISFIED path and UNSATISFIED path are structurally identical from the auditor's perspective.

**Signal 2 — "Or" path removal with explicit prohibition language.**
V-02 and V-04 mark the inline alternative as "C-40-noncompliant" but retain it in the format rules. V-05 removes it entirely and adds "There is no inline-cell 'or' path — the alternative form... must not be used." Prohibition by removal + explicit disqualification is stronger than prohibition by labeling. The template becomes unambiguous: column headers are the only possible form.

**Signal 3 — Structural enforcement levels as an independently auditable declaration.**
The three-level partition (`Structural enforcement levels [C-41]` block) names each criterion family, its structural layer, AND its audit procedure: "Auditable by reading exit item (3) alone" / "Auditable by reading the C2 RESULT block alone" / "Auditable by counting table columns alone." This makes each layer's compliance procedure self-contained within the declaration — a reviewer audits the declaration without running the skill.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Conditional derivation in C2 RESULT block handles both SATISFIED and UNSATISFIED paths inline, eliminating the dual-block split and making the block self-contained regardless of outcome", "Complete removal of the inline-cell alternative path with explicit prohibition language is stronger than labeling it noncompliant while retaining it", "Structural enforcement levels declaration names each level's audit procedure inline, making the partition independently verifiable without reading skill output"]}
```
