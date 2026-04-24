# Quest Score — org-chart Round 10 (Rubric v10)

## Baseline

R9-V-05 scored 210/210 on v9. On v10 it carries forward all 34 criteria passes except C-33 and C-34, which were not present in v9. All five variations share the R9-V-05 base and differ only within GATE 3's CHECKPOINT-3 block.

---

## Criterion-by-Criterion Evaluation

### Essential (12 pts each)

All five variations are identical to R9-V-05 on GATE 0 through GATE 2 and on the GATE 3 production steps (3.1–3.5). Essential criteria are unaffected by CHECKPOINT-3 modifications.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Inertia Assessment complete | PASS | PASS | PASS | PASS | PASS |
| C-02 | Roles block grounded in .roles/ | PASS | PASS | PASS | PASS | PASS |
| C-03 | ASCII org diagram >= 2 levels | PASS | PASS | PASS | PASS | PASS |
| C-04 | Operating rhythm table >= 3 distinct rows | PASS | PASS | PASS | PASS | PASS |
| C-05 | Committee charters with all 5 fields | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 all variations.**

---

### Recommended (10 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Headcount by area with Decides/Escalates + Key Roles annotated | PASS | PASS | PASS | PASS | PASS |
| C-07 | All 4 phase gate lines in correct sequence | PASS | PASS | PASS | PASS | PASS |
| C-08 | ROLE-TYPE-CLASSIFICATION immediately after roles; all typed from closed set | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 all variations.**

---

### Aspirational (5 pts each — C-09 through C-32 unchanged from v9)

C-09 through C-32 all carry forward as PASS from R9-V-05. No variation touches the structures those criteria govern. Subtotal: 120/120 for all variations.

---

### New Aspirational — C-33 and C-34 (5 pts each)

#### C-33 — GATE 3 field-format verification coverage

**What it requires:** CHECKPOINT-3 must verify (1) Quorum field matches `N of M member roles` fraction pattern (prohibiting fractional, percentage, prose, and bare-number forms explicitly), and (2) each Membership entry carries a `(TYPE)` annotation from the closed set `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}`. A count-only checkpoint fails.

| V | Evidence | Result |
|---|----------|--------|
| **V-01** | Replaces generic items with FORMAT-VERIFY QUORUM (names fractional, percentage, prose, bare number as explicitly NOT acceptable) and FORMAT-VERIFY MEMBERSHIP TYPE (names the closed set; flags unannotated entries or out-of-set values as rejected). Both prohibited patterns are explicitly enumerated — the checkpoint can no longer pass a charter with `"majority"` Quorum or an `(OWNER)` annotation. Meets the "names the closed set" and "prohibited Quorum patterns" requirements of C-33. | **PASS** |
| **V-02** | Only adds the ROLE-CONTINUITY item to CHECKPOINT-3. CHECKPOINT-3 items for Quorum and Membership remain the R9-V-05 generic presence checks (`Quorum in form` / `Membership >= 2 roles with annotation`). Does not name the closed set or prohibited Quorum patterns. | **FAIL** |
| **V-03** | Inserts a pre-CHECKPOINT `CHARTER-FORMAT-AUDIT` loop that iterates per charter with `REJECT: QUORUM` (names prohibited forms) and `REJECT: MEMBERSHIP TYPE` (names closed set) conditions plus a DO NOT advance guard. The loop structure satisfies "every produced charter" and names every rejection condition. CHECKPOINT-3 item 4 references the completed audit as its evidence. The dedicated-loop format is stronger than inline items: each charter is visited individually before the aggregate count check closes. | **PASS** |
| **V-04** | Same FORMAT-VERIFY items as V-01 in CHECKPOINT-3. Meets all C-33 conditions. | **PASS** |
| **V-05** | Same CHARTER-FORMAT-AUDIT loop as V-03, plus ROLE-CONTINUITY from V-02. Loop satisfies C-33 at the per-charter level. | **PASS** |

#### C-34 — Cross-gate role continuity assertion in GATE 3 checkpoint

**What it requires:** CHECKPOINT-3 must include an explicit step: every Membership role name must be present in the GATE 0 typed role list. If absent, CHECKPOINT-3 FAILS and remediation (add role to GATE 0, re-emit GATE 0 STATUS) must precede GATE 3 STATUS.

| V | Evidence | Result |
|---|----------|--------|
| **V-01** | No ROLE-CONTINUITY item added. C-02 and C-25 satisfy declaration-scope and handoff-naming requirements respectively, but CHECKPOINT-3 has no step that consumes the GATE 0 typed role list as a lookup table during execution. A Membership entry with an undeclared role name passes V-01's checkpoint undetected. | **FAIL** |
| **V-02** | Adds `ROLE-CONTINUITY` item that names GATE 0 as the lookup authority and states: "If any Membership role name is absent from GATE 0: CHECKPOINT-3 FAILS. Remediation: add the undeclared role to GATE 0 and re-emit GATE 0 STATUS before GATE 3 STATUS can emit." Converts declaration-scope constraint (C-02) into checkpoint-execution lookup with named FAIL condition and named remediation path. Satisfies C-34. | **PASS** |
| **V-03** | No ROLE-CONTINUITY item. CHARTER-FORMAT-AUDIT loop checks field format per charter but does not cross-reference role names against GATE 0. Same gap as V-01. | **FAIL** |
| **V-04** | Includes V-02's ROLE-CONTINUITY item alongside FORMAT-VERIFY items. Named lookup authority, explicit FAIL directive, and named remediation present. Satisfies C-34. | **PASS** |
| **V-05** | Includes V-02's ROLE-CONTINUITY item alongside CHARTER-FORMAT-AUDIT loop. Same C-34 satisfaction as V-02 and V-04. | **PASS** |

---

## Composite Scores

| Criterion Group | Max | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|-----|------|------|------|------|------|
| Essential (C-01–05) | 60 | 60 | 60 | 60 | 60 | 60 |
| Recommended (C-06–08) | 30 | 30 | 30 | 30 | 30 | 30 |
| Aspirational (C-09–32) | 120 | 120 | 120 | 120 | 120 | 120 |
| C-33 | 5 | 5 | 0 | 5 | 5 | 5 |
| C-34 | 5 | 0 | 5 | 0 | 5 | 5 |
| **Total** | **220** | **215** | **215** | **215** | **220** | **220** |
| **%** | | **97.7%** | **97.7%** | **97.7%** | **100%** | **100%** |
| All essential pass? | | Yes | Yes | Yes | Yes | Yes |
| Golden? (>=176) | | Yes | Yes | Yes | Yes | Yes |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tie) | **V-04** | 220/220 | Inline FORMAT-VERIFY + ROLE-CONTINUITY; minimal CHECKPOINT-3 growth |
| 1 (tie) | **V-05** | 220/220 | Dedicated CHARTER-FORMAT-AUDIT loop + ROLE-CONTINUITY; strongest per-charter coverage |
| 3 (tie) | V-01 | 215/220 | C-33 closed; C-34 open |
| 3 (tie) | V-02 | 215/220 | C-34 closed; C-33 open |
| 3 (tie) | V-03 | 215/220 | C-33 closed via loop; C-34 open |

**V-05 is the preferred R11 base** if future rubric signals probe per-charter format enforcement granularity. V-04 is preferred if checkpoint compactness is the optimization target.

---

## Excellence Signals (from V-04 and V-05)

**1. Named rejection conditions convert presence checks into compliance enforcement.**
R9-V-05's `Quorum in form` checkpoint item confirms that some Quorum value exists; it cannot detect `"majority of 5"` as invalid because the prohibited alternatives are not named. V-04/V-05 enumerate the prohibited patterns explicitly (`fractional "3/5"`, `percentage "60%"`, `prose quorum`, `bare number` are NOT acceptable). The checkpoint becomes falsifiable: a model encountering a `"majority"` Quorum has an instruction that names it as a rejection condition, not merely guidance toward a correct form.

**2. Lookup-authority naming converts declaration-scope grounding into execution-time verification.**
C-02 establishes that roles must be declared in GATE 0. C-25 names the typed role list as the GATE 0 handoff artifact. Neither step instructs the GATE 3 checkpoint to *use* that list. V-04/V-05's ROLE-CONTINUITY item names GATE 0 explicitly as the lookup authority and frames the check as a query ("is this name present?") rather than a re-read of a prior rule. The distinction matters at execution time: a model following V-04/V-05 encounters a concrete lookup instruction at the moment charter Membership fields are verified, not a general grounding rule stated earlier.

**3. Named FAIL+remediation directives make checkpoints actionable.**
V-04/V-05's ROLE-CONTINUITY item does not stop at naming the failure condition; it specifies the corrective path: add the undeclared role to GATE 0, re-emit GATE 0 STATUS, then return to GATE 3. This is structurally different from a blocking checkpoint that detects a violation and halts without direction. A checkpoint with named remediation closes the loop: detection, halt, and recovery path are all co-located at the checkpoint instruction, preventing a model from silently omitting the cross-gate correction.

**4. C-33 and C-34 are orthogonal and combinable without structural conflict.**
The two new criteria govern distinct dimensions of the same checkpoint: C-33 verifies format within each charter (field shape), C-34 verifies cross-gate name integrity (name presence). V-04 demonstrates that both can be satisfied by adding two logically independent items to CHECKPOINT-3 without restructuring any upstream gate. The orthogonality means future criteria in this family can be added by the same pattern: identify the checkpoint gap, name the lookup authority or rejection conditions, embed a FAIL+remediation path.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named rejection conditions in FORMAT-VERIFY items convert presence checks into falsifiable format compliance — prohibited alternatives enumerated explicitly, not implied by positive examples", "Lookup-authority naming in ROLE-CONTINUITY item converts declaration-scope constraint (C-02) into checkpoint-execution verification by instructing the model to query GATE 0 as a lookup table at the moment charter Membership fields are verified", "Named FAIL+remediation directive co-located at the checkpoint (detect → halt → named corrective path) prevents silent bypass where a checkpoint detects a violation but provides no recovery instruction"]}
```
