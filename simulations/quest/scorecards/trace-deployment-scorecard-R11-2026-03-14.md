## trace-deployment R11 Scoring

**Rubric**: v9 | **Criteria**: 27 | **Total**: 185 pts | **Variations received**: V-01 (complete), V-02 (complete), V-03 (incomplete — cut before rollback), V-04/V-05 (not in input)

---

### Trace Artifact

*Not required for prompt-scoring mode — variations are prompts, not outputs.*

---

## V-01 — Interrogative + bare labels + minimum rollback

**Hypothesis**: C-26 ∩ C-22 ∩ C-27 jointly satisfiable → 160/185

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | check-1 through check-4; 4 named pre-deploy checks |
| C-02 | PASS | step-1 through step-5; 5 ordered steps |
| C-03 | PASS | val-1 through val-3; 3 post-deploy validations |
| C-04 | PASS | undo-trigger + undo-1 + confirmed-back; trigger/step/verify present |
| C-05 | PASS | skeleton has 4 phase rows; one gap slot per phase |
| C-06 | PASS | order-dep-1 field; explicit ordering dependency |
| C-07 | PASS | domain vocabulary in role block anchors output register |
| C-08 | PASS | "Why" column + comparative return instruction structurally forces actionable gap content; "a gap that blocks rollback outranks a gap that only delays detection" is the actionability frame |
| C-09 | PASS | Severity column + "compare all gaps against each other before finalizing ranks" → severity-ranked output |
| C-10 | PASS | hook-1 field present |
| C-11 | PASS | vocabulary list in role block: catalog sync, order pipeline drain, inventory lock, tenant provisioning, schema migration, service mesh cutover, feature flag gate, blast radius, rollback window |
| C-12 | PASS | "Current practice:" + "Known failure mode:" in role block |
| C-13 | PASS | skeleton is cross-phase (Phase column), has Severity + Why; comparative instruction forces rank ordering; Severity column is functional Rank proxy |
| C-14 | PASS | skeleton is front-loaded before first interrogative header; "Do not pre-fill" guard present; return instruction with cross-gap comparison mandate |
| C-15 | FAIL | template fields present; C-15 requires "without structural template apparatus" |
| C-16 | PASS | field counts satisfy all five essentials + C-10; no GATE enforcement text present |
| C-17 | FAIL | requires C-15 |
| C-18 | PASS | C-14 ✓ + C-16 ✓ |
| C-19 | FAIL | requires C-15 |
| C-20 | FAIL | requires C-19 |
| C-21 | PASS | C-14/C-16/C-18 pass + colloquial register confirmed: "what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?" |
| C-22 | PASS | template path passes; field labels are bare identifiers only (check-1:, step-1:, val-1:, undo-trigger:); no inline prose within fields; no extra guards beyond skeleton |
| C-23 | FAIL | no inertia narrative in role block |
| C-24 | PASS | C-21 ✓ + C-22 ✓ |
| C-25 | PASS | "Current practice:" + "Known failure mode:" in role block; no first-person incident narrative present |
| C-26 | PASS | C-21 passes via interrogative-question sub-form; all four headers are interrogative questions — distinguishing condition satisfied |
| C-27 | PASS | C-16 ✓ + C-22 ✓; rollback section has exactly 3 fields: undo-trigger, undo-1, confirmed-back — minimum-viable-rollback-field-count satisfied |

**Composite**: Essential 60 + Recommended 30 + Aspirational 70 (14 × 5) = **160 / 185**

All essential: **PASS** | Golden threshold (≥80): **PASS** (86%)

---

## V-02 — Dual role-block voice (C-23 + C-25 simultaneous)

**Hypothesis**: C-23 ∩ C-25 jointly satisfiable on template path → 16 criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Check-01 through Check-04 |
| C-02 | PASS | Step-01 through Step-06 |
| C-03 | PASS | Validation-01 through Validation-03 |
| C-04 | PASS | Trigger + Rollback-01 through Rollback-03 + Verification |
| C-05 | PASS | 4 phase rows in skeleton |
| C-06 | PASS | Ordering-dep-01 field |
| C-07 | PASS | domain vocabulary in role block |
| C-08 | PASS | "Why" column + comparative return instruction; same structural pressure as V-01 |
| C-09 | PASS | Severity column + cross-gap comparison mandate |
| C-10 | PASS | Hook-01 + Hook-02 |
| C-11 | PASS | vocabulary list in role block |
| C-12 | PASS | "Current practice:" + "Known failure mode:" in role block |
| C-13 | PASS | cross-phase skeleton table, Severity + Why columns, comparative instruction |
| C-14 | PASS | front-loaded skeleton + do-not-pre-fill + cross-gap comparison return instruction |
| C-15 | FAIL | template fields present; C-15 requires prose path without structural template apparatus |
| C-16 | PASS | field counts satisfy all essentials + C-10; no GATE text |
| C-17 | FAIL | requires C-15 |
| C-18 | PASS | C-14 ✓ + C-16 ✓ |
| C-19 | FAIL | requires C-15 |
| C-20 | FAIL | requires C-19 → requires C-15; template path blocks this chain |
| C-21 | FAIL | formal headers ("## PHASE 1 — PRE-DEPLOY CHECKS"); colloquial register not present |
| C-22 | PASS | template path passes (C-14/C-16/C-18); field labels bare (Check-01:, Step-01:, etc.); no inline prose within fields; "Do not pre-fill" is skeleton-structural, not an additional guard |
| C-23 | FAIL | requires C-20 → FAIL; **hypothesis error**: C-23 is prose-path-exclusive via C-20→C-19→C-15 chain |
| C-24 | FAIL | requires C-21 |
| C-25 | FAIL | requires C-20 → FAIL; **hypothesis error**: same chain |
| C-26 | FAIL | requires C-21 |
| C-27 | FAIL | rollback has 5 fields (Trigger, Rollback-01, -02, -03, Verification); C-27 requires exactly 3 |

**Composite**: Essential 60 + Recommended 30 + Aspirational 45 (9 × 5: C-09–C-14, C-16, C-18, C-22) = **135 / 185**

All essential: **PASS** | Golden threshold: **PASS** (73%)

**Hypothesis diagnosis**: C-20, C-23, and C-25 cannot be achieved on the template path. All three require C-20, which requires C-19, which requires C-15 — and C-15 explicitly disqualifies "structural template apparatus." The dual-voice role block pattern (both "Current practice/Known failure mode" framing and inertia narrative in the same role block) is structurally valid and compatible, but can only be scored on a prose-path variation where C-15 passes. A V-02 rerun on a prose-path variation (role block with both voices, prose instructions satisfying C-15) is the correct test for C-23 ∩ C-25.

---

## V-03 — Prose path + question-form disqualifiers

**Status**: INCOMPLETE — input cuts off after post-deploy prose instruction; rollback section absent. C-04 (rollback path) is an essential criterion. Without rollback content, C-04 fails essential → composite = 0 regardless of other scores.

**Partial analysis before cutoff**:
- Pre-deploy prose instruction: names what is verified + what failure looks like + disqualifier ("a check that asks 'is everything ready?' names no specific condition and does not qualify") → C-01 direction PASS
- Sequence prose: numbered steps + ordering dependency instruction → C-02/C-06 direction PASS
- Post-deploy prose: "name the probe and the pass/fail threshold. 'Did it come back up?' is not a validation action — it names no probe, no threshold, and no observable system state." → question-form negation disqualifier is contextual, domain-vocabulary-only, no incident narrative → C-19/C-20 direction PASS **if rollback + gap sections are present and C-15 is achieved**
- Role block: "Current practice:" + "Known failure mode:", no inertia narrative → C-25 direction PASS if C-20 passes

**Unconfirmable**: C-04, C-05, C-13, C-14, C-15. **Score withheld pending complete input.**

---

## V-04, V-05 — Not in input

Not scored.

---

## Ranking

| Rank | Variation | Score | Hypothesis result |
|------|-----------|-------|-------------------|
| 1 | V-01 | 160/185 | Confirmed: 160/185 ceiling achieved; C-26 ∩ C-22 ∩ C-27 jointly satisfiable |
| 2 | V-02 | 135/185 | Hypothesis error: C-20/C-23/C-25 prose-path-exclusive |
| — | V-03 | unscored | Incomplete input; C-04 essential absent |
| — | V-04 | unscored | Not in input |
| — | V-05 | unscored | Not in input |

---

## Excellence Signals

**V-01 (top scorer — 160/185)**:

1. **Three rollback fields is sufficient**: `undo-trigger:` + `undo-1:` + `confirmed-back:` satisfies trigger/step/verify with exactly the minimum structure. Prior variations included `undo-2:` (4 fields), which prevented C-27. Stripping to three fields costs nothing on C-04 or C-16 while unlocking C-27.

2. **Interrogative headers as register signal, not style**: The four section headers ("what needs to be true before we touch this?", "what's the deployment order?", "did it land?", "what do we do if it didn't?") do double duty — they are colloquial (C-21) AND interrogative (C-26) simultaneously. Register choice adds 5 pts to C-26 with zero structural cost.

3. **Comparative rank instruction replaces a Rank column**: "Compare all gaps against each other before finalizing ranks — a gap that blocks rollback outranks a gap that only delays detection" satisfies C-09 and C-13's Rank requirement without requiring an explicit `Rank` column in the skeleton. Instruction-based forcing is lighter than structural column-based forcing.

**R11 structural finding (from V-02 failure)**:

C-20, C-23, and C-25 are **prose-path-exclusive**. The chain C-23→C-20→C-19→C-15 means these criteria can only be reached through prose-instruction variations that satisfy C-15 ("without structural template apparatus"). Template-path variations are permanently blocked from these three criteria. Future round design testing C-23/C-25 must use a prose-path variation with a role block containing both voices (operational baseline + inertia narrative) and a domain-contextual disqualifier (no incident narrative) in the prose body.

---

## Round Summary

| Criteria | R10 ceiling | R11 V-01 |
|----------|-------------|----------|
| C-26 | ✓ (via V-01, non-min rollback) | ✓ |
| C-27 | ✓ (via V-02, non-interrogative) | ✓ |
| C-26 ∩ C-27 | ✗ (never simultaneous) | ✓ |
| Score | 155/185 | **160/185** |

Predicted ceiling 160/185 confirmed. The next ceiling is determined by whether C-15/C-17/C-19/C-20/C-23 can co-exist with the template-path cluster — they cannot (mutual exclusion at C-15). The absolute ceiling is therefore capped at 160 on template path and requires a separate calculation for the prose path.

---

```json
{"top_score": 160, "all_essential_pass": false, "new_patterns": ["c20-c23-c25-prose-path-exclusive"]}
```

*(all_essential_pass: false — V-03 cut before rollback; C-04 essential unverifiable. V-01 and V-02 both pass all essential.)*
