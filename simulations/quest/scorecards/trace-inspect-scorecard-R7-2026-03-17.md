# Quest Score — trace-inspect R7 (Rubric v4)

## Per-Criterion Evaluation

### V-01 — Lifecycle emphasis (mandatory execution-evidence citation)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Phase completeness | PASS | All four phases present; Coverage Matrix declares all five schemas before Stage 1 |
| C-02 | Artifact produced | PASS | Phase 2 artifact write section with path template and section confirmation table |
| C-03 | Schema 1+2 compliance | PASS | Schemas declared in Coverage Matrix; label-lock invariant stated explicitly |
| C-04 | Enforcement gates checked | PASS | G-1/G-2/G-3 defined in Schema 4; PREREQUISITE CHECKPOINT before Step 3c names FLOOR CHECK block |
| C-05 | Verdict present and classified | PASS | Inherited from R6 V-05 architecture; verdict rules intact |
| C-06 | SA-TO-SG promotion evaluated | PASS | SA-TO-SG PROMOTION section with per-gap template; post-promotion inventory required |
| C-07 | Per-role relays complete | PASS | Role relay template with all required fields including Schema 2 compliance check |
| C-08 | Findings table depth | PASS | PREREQUISITE CHECKPOINT gates Step 3b; FLOOR CHECK enforces >= 3 findings |
| C-09 | Compliance ledger populated | PARTIAL | Ledger inherited; VC columns in Coverage Matrix present but ledger body not pre-printed |
| C-10 | Schema 5 sub-step transitions | PASS | Schema 5 table with prerequisite/transition columns; CHECKPOINT requirement before each sub-step |
| C-11 | Phase-entry gate-clearance summary | PASS | Inherited from R6 V-05; GATE CLEARANCE SUMMARY at phase boundaries |
| C-12 | Gate-failure remediation loop | PASS | Inherited from R6 V-05 |
| C-13 | Sub-step prerequisite checkboxes | PASS | "Requirement A — PREREQUISITE CHECKPOINT" explicitly required with named-artifact check |
| C-14 | Remediation-to-summary coherence | PASS | Inherited from R6 V-05 |
| **C-15** | Post-table FLOOR CHECK | **PASS** | "Requirement B — FLOOR CHECK" names all four checks: finding IDs, row count >= 3, Source types >= 2, Action uniqueness; emits PASS/FAIL; FAIL blocks Step 3c |
| **C-16** | Execution-evidence mandatory citation | **PASS** | EVIDENCE CLASSIFICATION block requires EVIDENCE-GROUNDED/SPEC-INFERENCE state; "citing spec inference when execution evidence is available is a structural violation" |
| **C-17** | G-1 cross-role attribution in ledger | **PARTIAL** | No new attribution table structure; inherits R6 V-05 prose entry in VC-4 |
| **C-18** | Remediation entry precision | **PARTIAL** | No precision template; inherits R6 V-05 "name the ID" instruction without enforced format |

**V-01 score**: 94 (base) + 0.75 + 0.75 + 0.38 + 0.38 = **96**

---

### V-02 — Output format (C-17 + C-18 pre-printed templates)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | Essential | PASS × 5 | Inherited from R6 V-05 |
| C-06–C-08 | Recommended | PASS × 3 | Inherited from R6 V-05 |
| C-09 | Compliance ledger | PARTIAL | Pre-print templates added; ledger header rows present but body observations not pre-populated |
| C-10–C-14 | Aspirational (v3) | PASS × 5 | Inherited from R6 V-05 |
| **C-15** | FLOOR CHECK | **PARTIAL** | No new FLOOR CHECK improvements; axis focused on Phase 4/5 templates |
| **C-16** | Execution-evidence citation | **PARTIAL** | No mandatory classification; "cite if available" conditional language inherited |
| **C-17** | G-1 cross-role attribution | **PASS** | Pre-printed two-column table: Source type → contributing roles; structured fill-in forces named attribution |
| **C-18** | Remediation entry precision | **PASS** | Pre-printed template requires `added F-NN (Source: XX, Action: [text])` format; bare ID fails template validation |

**V-02 score**: 94 + 0.38 + 0.38 + 0.75 + 0.75 = **96**

---

### V-03 — Phrasing register (MUST/VIOLATION obligation pairs for C-16 + C-18)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | Essential | PASS × 5 | Inherited |
| C-06–C-08 | Recommended | PASS × 3 | Inherited |
| C-09–C-14 | Aspirational (v3) | PASS × 5 + PARTIAL × 1 | C-09 PARTIAL (obligation statements don't restructure ledger body) |
| **C-15** | FLOOR CHECK | **PARTIAL** | Axis targets C-16 and C-18; no MUST/VIOLATION pair added for FLOOR CHECK blocking assertion |
| **C-16** | Execution-evidence citation | **PASS** | MUST: cite execution observation / VIOLATION: citing spec inference when execution has run; removes permissive conditional |
| **C-17** | G-1 cross-role attribution | **PARTIAL** | No attribution table; MUST statement may appear for VC-4 but no structured two-column template |
| **C-18** | Remediation entry precision | **PASS** | MUST: include finding ID + Action text / VIOLATION: "added a finding" fails; obligation pair enforces artifact reference format |

**V-03 score**: 94 + 0.38 + 0.75 + 0.38 + 0.75 = **96**

---

### V-04 — Combined: lifecycle emphasis + EG-first role sequence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | Essential | PASS × 5 | Inherited |
| C-06 | SA-TO-SG evaluation | PASS | Execution-first ordering guarantees evidence is always available before promotion decision; structural enforcement |
| C-07 | Per-role relays complete | PASS | EG-producing roles run first; relay sequence unambiguous |
| C-08 | Findings table depth | PASS | Inherited FLOOR CHECK |
| C-09–C-14 | Aspirational (v3) | PASS × 5 + PARTIAL × 1 | C-09 PARTIAL inherited |
| **C-15** | FLOOR CHECK | **PASS** | Inherits V-01's "Requirement B" FLOOR CHECK with all four checks and blocking FAIL |
| **C-16** | Execution-evidence citation | **PASS** | Structural: EG roles always run before promotion evaluation → EVIDENCE-GROUNDED state is architectural default, not just a rule |
| **C-17** | G-1 cross-role attribution | **PARTIAL** | Role ordering improves relay detail but no pre-printed attribution table for ledger |
| **C-18** | Remediation entry precision | **PARTIAL** | No precision template; role ordering does not address remediation entry format |

**V-04 score**: 94 + 0.75 + 0.75 + 0.38 + 0.38 = **96**
*Note: V-04's C-16 is structurally enforced (architecture) vs. V-01's rule-stated enforcement — same score, higher robustness.*

---

### V-05 — Full integration (all four new criteria)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | Essential | PASS × 5 | Pre-printed phase skeletons enforce structural completeness |
| C-06–C-08 | Recommended | PASS × 3 | Inherited and reinforced by inertia framing |
| C-09 | Compliance ledger | PASS | Pre-printed VC table with named-attribute rows; C-17 attribution table wired directly into VC-4 G-1 row |
| C-10–C-14 | Aspirational (v3) | PASS × 5 | Inherited and named in inertia registry |
| **C-15** | FLOOR CHECK | **PASS** | Full FLOOR CHECK block: names every finding ID, count >= 3, Source types >= 2, Action uniqueness assertion; FAIL hard-blocks Step 3c |
| **C-16** | Execution-evidence citation | **PASS** | EVIDENCE-GROUNDED/SPEC-INFERENCE binary classification + EG-first ordering; inertia framing names C-16 explicitly |
| **C-17** | G-1 cross-role attribution | **PASS** | Pre-printed two-column attribution skeleton in VC-4: Source type | Roles producing that type; structured fill-in, not prose |
| **C-18** | Remediation entry precision | **PASS** | Precision template enforced: `F-NN (Source: XX, Action: [text])` format; "added a finding" explicitly marked VIOLATION |

**V-05 score**: 94 + 0.75 + 0.75 + 0.75 + 0.75 = **97**

---

## Score Summary

| Variation | C-15 | C-16 | C-17 | C-18 | New pts | Composite | Golden? |
|-----------|------|------|------|------|---------|-----------|---------|
| V-05 | PASS | PASS | PASS | PASS | +3.00 | **97** | YES |
| V-04 | PASS | PASS | PARTIAL | PARTIAL | +2.26 | **96** | YES |
| V-01 | PASS | PASS | PARTIAL | PARTIAL | +2.26 | **96** | YES |
| V-03 | PARTIAL | PASS | PARTIAL | PASS | +2.26 | **96** | YES |
| V-02 | PARTIAL | PARTIAL | PASS | PASS | +2.26 | **96** | YES |

**Rank**: V-05 (97) > V-04 (96†) ≥ V-01 (96) > V-03 (96) ≥ V-02 (96)
*† V-04 edges V-01: C-16 is structurally enforced (role ordering) rather than rule-stated — same score, higher failure resistance.*

---

## Excellence Signals from V-05

**Signal 1 — Evidence state naming (binary classification over conditional instruction)**
V-05 replaces "cite execution evidence if post-execution" with a named state machine: EVIDENCE-GROUNDED / SPEC-INFERENCE. The state is declared before the promotion decision, not after. A named state is machine-checkable; a conditional instruction is not. This pattern generalizes: any criterion that depends on the presence of a precondition (prior evidence, prior relay, prior phase) should introduce a named state classification at the precondition boundary, not a conditional instruction at the output boundary. *Not captured by C-16, which requires mandatory citation but does not require the named-state pattern itself.*

**Signal 2 — Architecture over instruction for structural enforcement**
V-04's role ordering (absorbed into V-05) resequences execution so the rule becomes structurally impossible to violate: EG roles always run before promotion evaluation, so execution evidence is always available when the EVIDENCE-GROUNDED/SPEC-INFERENCE classification is resolved. V-05 extends this: the four new criteria are pre-printed as sequential skeletons in phase order, making omission require active deletion rather than passive omission. *Not captured by any existing criterion — all C-11 through C-18 govern what must appear in the output, none govern whether the prompt structure makes omission structurally harder than compliance.*

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["evidence state naming: replacing conditional citation instructions with a named binary state (EVIDENCE-GROUNDED / SPEC-INFERENCE) declared before the decision point makes the evidence basis machine-checkable and removes the escape hatch from permissive conditionals", "architecture over instruction: resequencing execution so evidence is always available at decision time, combined with pre-printed sequential skeletons, makes criterion omission require active deletion rather than passive omission — structural enforcement outperforms rule-statement for aspirational criteria"]}
```
