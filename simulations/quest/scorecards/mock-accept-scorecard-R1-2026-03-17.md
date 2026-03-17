---

## mock-accept R1 Scorecard

### Per-Variation Results

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Score | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 Role Sequence | PARTIAL | PASS | **FAIL** | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | **71** | NO |
| V-02 Table-First | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | **95** | YES |
| V-03 Inertia | PARTIAL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | **83** | NO |
| V-04 Lifecycle | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | **95** | YES |
| V-05 Checklist | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | **95** | YES |

### Key Findings

**C-03 killed V-01**: Phase 3 defines structural slots but never mentions reason codes at all. `STRUCTURAL-COVERAGE-SUFFICIENT` / `DOMAIN-KNOWLEDGE-CONSISTENT` are absent from the prompt — a field you can't omit can't be satisfied.

**C-01 partial on V-01 and V-03**: Both rely on implicit phase coverage. A namespace missing from the mock artifact would pass through silently. V-02 has a `count rows = 9` self-check; V-04 has a `N+M=total` sum assertion; V-05 names all 9 explicitly in Question 1.

**C-09 fails uniformly**: No variation instructs for artifact-as-subject grammar. This is a gap in the variation set — not a differentiator but a universal ceiling at 95.

### Excellence Signals

1. **Inline completeness gate** — count check or sum assertion as a named checkpoint (not implicit phase coverage)
2. **Reason-code enforcement at point of use** — constraint inside the table column rule or checkbox, not in preamble
3. **Phase exit assertions** (V-04): entry/exit conditions prevent auto-flag and evaluation logic from interleaving
4. **Blank-line failure signal** (V-05): checklist format makes slot violations visible without parsing prose

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["inline-completeness-gate: count-rows=9 or N+M=total assertion as named checkpoint prevents silent namespace omission", "reason-code-field-enforcement: exact-code constraint placed inside table column rule or checklist checkbox at point of use, not in preamble", "phase-exit-assertion: explicit N+M=total sum check before phase transition prevents collapse of auto-flag and evaluation logic", "blank-line-failure-signal: checklist item left blank is structurally visible without prose parsing — turns semantic completeness test into structural one"]}
```
e namespaces appear in the Decision Grid as MOCK-ACCEPTED, return to Step 1 and correct before continuing." |
| C-03 exact reason codes | essential | PASS | Step 1 rules: "write exactly one or both of: STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT. No paraphrases. No invented codes. No prose summaries in this column." |
| C-04 edit + canary | essential | PASS | Step 5: Edit tool, re-read, count verification, verbatim Canary, suppression with field listing |
| C-05 structural slots | essential | PASS | Step 4 Structural Slot Table with explicit SLOT-VIOLATION and CONTRAST-INCOMPLETE pattern examples; both slots required |
| C-06 named role verdicts | recommended | PASS | Step 3: three-role verdict blocks with exact verdict strings for each role |
| C-07 review artifact | recommended | PASS | Step 6: canonical path, Decision Grid copy + Structural Slot Table copy + cross-namespace risk |
| C-08 next-steps format | recommended | PASS | Step 7: /{skill-id} {topic} format with three groups |
| C-09 artifact-as-subject | aspirational | FAIL | No artifact-as-subject grammar instruction |
| C-10 single highest-risk gap | aspirational | PASS | Step 6: "A list of risks without a single selection does not satisfy this requirement." + urgency required |

**Essential pass**: 5/5
**Recommended pass**: 3/3
**Aspirational pass**: 1/2
**Composite**: 5/5×60 + 3/3×30 + 1/2×10 = 60 + 30 + 5 = **95**
**Golden**: YES

---

### V-03 — Inertia Framing (single-axis)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 completeness | essential | PARTIAL | Pass 1 closes non-starters, Pass 2 builds cases for remaining; no explicit 9-namespace count check or enumeration — a missing namespace would not be caught |
| C-02 auto-flag integrity | essential | PASS | Pass 1: "REAL-REQUIRED regardless of mock quality" + "Note: 'No evaluation performed. Auto-flag is unconditional.'" Inertia framing reinforces this |
| C-03 exact reason codes | essential | PASS | Pass 3: "Reason codes (exact enumeration only — no paraphrases): STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT" |
| C-04 edit + canary | essential | PASS | Pass 4: Edit tool, re-read, count verification, verbatim Canary, suppression |
| C-05 structural slots | essential | PASS | Pass 3: templates for Slot 1 and Slot 2; "if either slot cannot be completed, the defense fails and the decision reverts to REAL-REQUIRED" |
| C-06 named role verdicts | recommended | PASS | Pass 2: three dimensions with labeled verdicts (CONSISTENT-WITH-ARCHITECTURE, ADEQUATE FOR TIER 1, REPRESENTATIVE) |
| C-07 review artifact | recommended | PASS | Pass 5: canonical path, Coverage Review table, defense records, cross-namespace risk |
| C-08 next-steps format | recommended | PASS | Pass 6: /{skill-id} {topic} format with three groups |
| C-09 artifact-as-subject | aspirational | FAIL | No artifact-as-subject grammar instruction |
| C-10 single highest-risk gap | aspirational | PASS | Pass 5: "Single highest-risk gap: name the namespace, the specific tier decision at risk, urgency: BLOCKING \| HIGH \| MEDIUM" |

**Essential pass**: 4/5 (C-01 partial)
**Recommended pass**: 3/3
**Aspirational pass**: 1/2
**Composite**: 4/5×60 + 3/3×30 + 1/2×10 = 48 + 30 + 5 = **83**
**Golden**: NO — C-01 partial (no completeness gate)

---

### V-04 — Role Sequence + Lifecycle Emphasis (combination)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 completeness | essential | PASS | Phase 0 builds explicit working set; Phase 1 exit assertion: "[N] AUTO-FLAGGED, [M] EVALUATION-ELIGIBLE. Sum = [total]. Matches working set. Phase 1 complete." |
| C-02 auto-flag integrity | essential | PASS | Phase 1: "Evaluation-eligible check skipped — auto-flag is unconditional." Phase 2 restricted to EVALUATION-ELIGIBLE only by entry condition |
| C-03 exact reason codes | essential | PASS | Phase 3: "Select from exact enumeration only. No paraphrases. No invented codes. Code must appear in labeled field, not buried in prose." |
| C-04 edit + canary | essential | PASS | Phase 4 with entry condition (Phase 3 assertion written), Edit tool, re-read, count, Canary or suppression; exit assertion is the Canary line |
| C-05 structural slots | essential | PASS | Phase 3: Slot 1 SLOT-VIOLATION check + Slot 2 CONTRAST-INCOMPLETE check, both revert to REAL-REQUIRED; Phase 3 exit assertion counts slot confirmations and reversions |
| C-06 named role verdicts | recommended | PASS | Phase 2 role sequence with exact verdict strings; early-exit logic ensures each role result is recorded |
| C-07 review artifact | recommended | PASS | Phase 5: canonical path, Coverage Review table, structural records per MOCK-ACCEPTED, cross-namespace risk |
| C-08 next-steps format | recommended | PASS | Phase 5 next steps: /{skill-id} {topic} format with Group 1/2/3 |
| C-09 artifact-as-subject | aspirational | FAIL | No artifact-as-subject grammar instruction |
| C-10 single highest-risk gap | aspirational | PASS | Phase 5: "Exactly one highest-risk gap: namespace name + tier decision at risk + urgency classification: BLOCKING \| HIGH \| MEDIUM" |

**Essential pass**: 5/5
**Recommended pass**: 3/3
**Aspirational pass**: 1/2
**Composite**: 5/5×60 + 3/3×30 + 1/2×10 = 60 + 30 + 5 = **95**
**Golden**: YES

---

### V-05 — Interrogative Register + Checklist Format (combination)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 completeness | essential | PASS | Question 1: explicitly lists all 9 — "scout, draft, review, flow, trace, prove, listen, program, topic. You need all nine to proceed." + "All nine still need a decision." |
| C-02 auto-flag integrity | essential | PASS | Question 2: closes auto-flagged with "These are closed. Skip them in Questions 3-5." Three-property check is explicit and sequential |
| C-03 exact reason codes | essential | PASS | Question 6 checklist: "choose from exact list only — no paraphrasing: STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT." Blank line = failure |
| C-04 edit + canary | essential | PASS | Question 7: Edit tool, re-read, count, "Your count: ___", verbatim Canary, suppression |
| C-05 structural slots | essential | PASS | Question 6: Slot 1 "(If you wrote 'supports tier-1 decision-making' without a named decision → blank)" + Slot 2 "(If you named no structural factor → blank)"; blank = failure = reverts |
| C-06 named role verdicts | recommended | PASS | Questions 3, 4, 5 each name a role (Architect, Strategy, PM) with exact verdict strings |
| C-07 review artifact | recommended | PASS | Question 8: canonical path, Coverage Review table, completed checklists, cross-namespace risk |
| C-08 next-steps format | recommended | PASS | Question 9: /{skill-id} {topic} format with three groups |
| C-09 artifact-as-subject | aspirational | FAIL | No artifact-as-subject grammar instruction |
| C-10 single highest-risk gap | aspirational | PASS | Question 8: "which single namespace represents the highest-risk gap, which tier decision is at stake, and is it BLOCKING / HIGH / MEDIUM?" |

**Essential pass**: 5/5
**Recommended pass**: 3/3
**Aspirational pass**: 1/2
**Composite**: 5/5×60 + 3/3×30 + 1/2×10 = 60 + 30 + 5 = **95**
**Golden**: YES

---

## Rankings

| Rank | Variation | Composite | Golden | Essential | Failure Modes |
|------|-----------|-----------|--------|-----------|---------------|
| 1 (tie) | V-02 Table-First | 95 | YES | 5/5 | C-09 only |
| 1 (tie) | V-04 Lifecycle | 95 | YES | 5/5 | C-09 only |
| 1 (tie) | V-05 Checklist | 95 | YES | 5/5 | C-09 only |
| 4 | V-03 Inertia | 83 | NO | 4/5 | C-01 partial, C-09 |
| 5 | V-01 Gate-First | 71 | NO | 3/5 | C-01 partial, C-03, C-09 |

---

## Failure Analysis

**C-01 (V-01, V-03)**: Both fail because they rely on implicit phase coverage of namespaces rather than explicit enumeration or count verification. A mock artifact missing a namespace would not trigger any warning.

**C-03 (V-01 only)**: V-01 Phase 3 defines structural slots but omits reason codes entirely. The concepts STRUCTURAL-COVERAGE-SUFFICIENT and DOMAIN-KNOWLEDGE-CONSISTENT are not mentioned anywhere in V-01. This is the sharpest essential failure: the criterion can't be satisfied by a prompt that doesn't include the field.

**C-09 (all)**: No variation instructs for artifact-as-subject grammar in SQ answers. All fail uniformly — this is a gap in the variation set as a whole, not a differentiator.

---

## Excellence Signals

Patterns from the three top-scoring variations that distinguish them from V-01 and V-03:

### Signal 1 — Inline Completeness Gate
V-02: "Self-check before proceeding: count rows. Must equal 9."
V-04: Phase 1 exit assertion — "Sum = [total]. Matches working set."
V-05: Question 1 — "You need all nine to proceed. All nine still need a decision."

All three enforce completeness as a named checkpoint, not as an implicit consequence of phases. This is what V-01 and V-03 lack.

### Signal 2 — Reason-Code Field Enforcement at Point of Use
V-02 places the exact-code constraint inside the table column rule: "write exactly one or both of… No paraphrases. No invented codes. No prose summaries in this column."
V-04 adds the field-locality requirement: "Code must appear in labeled field, not buried in prose."
V-05 uses a checkbox that can be left blank as the failure signal — the code must appear in the answer line or the item is visibly incomplete.

All three enforce at the point where the code is written, not in a documentation preamble. V-01 omits the field entirely; V-03 has the instruction but no structural enforcement.

### Signal 3 — Phase Exit Assertions (V-04 unique)
V-04's entry/exit conditions on each phase create explicit handshakes: "Do not proceed to Phase N+1 until this assertion is written." This prevents phase collapse — the condition where auto-flag logic and evaluation logic interleave and auto-flag decisions become subject to evaluation reasoning.

### Signal 4 — Blank-Line Failure Signal (V-05 unique)
V-05's checklist format makes slot violations visible as blank answer lines rather than requiring the model to parse prose. "(If you wrote X → blank)" turns a semantic test into a structural one. The checklist can be scanned for completeness without reading every answer.

---

## Golden Candidates

**V-02, V-04, V-05** are all golden at 95.

V-04 has the strongest structural guarantees (phase exit assertions prevent logic interleaving).
V-02 has the most scannable output format (decision table first, all codes visible at a glance).
V-05 has the most accessible register and the checklist-blank failure signal.

For the next round, the gap to close is C-09: no variation instructs for artifact-as-subject grammar. Adding this instruction to any golden variation would raise the ceiling to 100.
