# Trace-Inspect Round 11 — Scoring (Rubric v7)

## Point Structure

| Block | Criteria | Weight | Max |
|-------|----------|--------|-----|
| Essential | C-01–C-05 | 15 pts each | 75 |
| Recommended | C-06–C-08 | 5 pts each | 15 |
| Aspirational | C-09, C-10 | 2 pts each | 4 |
| Aspirational | C-11–C-25 | 0.5 pts each | 7.5 |
| **Total** | | | **101.5** |

PARTIAL = 0.5 × criterion weight.

---

## Essential Criteria (15 pts each)

### C-01 Phase completeness

All five variations include all four phases with structurally closed outputs. Phase 3 runs 3a→3b→3c→3d in order. Phase 4 delivers at least one change or dismissal entry.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

*Evidence*: All variations are complete prompt bodies (2269 lines). None removes or collapses phases.

### C-02 Artifact produced

All variations write the hand-compiled artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md` with all required sections. Execute phase produces written artifact, not just relay prose.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-03 Schema 1 + Schema 2 compliance

All severity labels from {P1, P2, P3}; all Source labels from {SA, SG, EG, QO}; promoted SA gaps carry SG in all phases after promotion. None of the R11 additions introduces new label vocabulary.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

*Note*: V-03's `[enforcement: X]` annotation is metadata syntax, not a label value — no schema conflict.

### C-04 Enforcement gates checked

G-1, G-2, G-3 each record explicit PASS/FAIL at Step 3c. No gate is omitted or implicitly assumed.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-05 Verdict present and classified

Pass condition: one of {USEFUL, NEEDS-REDESIGN, NEEDS-SPEC-REVISION} with decision rationale per the defined rules.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

*Differentiation note*: V-01/V-04/V-05 add the NEEDS-REDESIGN EVIDENCE ANCHOR — verdict names EG finding IDs explicitly, count derived from the list. This exceeds C-05's pass condition (rationale is quantitatively grounded, not just asserted). Not scoreable under v7 but noted for C-26 candidacy.

---

## Recommended Criteria (5 pts each)

### C-06 SA-TO-SG promotion evaluated

Every SA gap from Stage 1 evaluated at SA-TO-SG PROMOTION with PROMOTES TO SG or REMAINS SA plus one-sentence reason. Post-promotion inventory states SA remaining + SG from promotion counts.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

*Differentiation note*: V-02/V-04/V-05 add the PROMOTION COMPLETENESS GATE with arithmetic self-check `(promoted + remaining = Stage 1 SA count)` and MISMATCH blocks Phase 2b. This exceeds C-06 (C-06 requires the evaluation and inventory; V-02 makes the inventory self-verifying). Noted for C-27 candidacy.

### C-07 Per-role relays complete

All relay fields present including Schema 2 compliance field and SA/SG gap attribution per role. No relay summarized as "ran normally."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-08 Findings table depth

≥ 3 distinct findings covering ≥ 2 Source types; each finding has a distinct Action.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

---

## Aspirational Criteria

### C-09 Compliance ledger populated (2 pts)

VC-1 through VC-5 populated with specific observed behavior per usage site. No "as expected" cells.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-10 Schema 5 sub-step transition confirmations (2 pts)

Explicit transition sentence at each 3a→3b, 3b→3c, 3c→3d boundary.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-11 Gate clearance summary blocks (0.5 pts)

GATE CLEARANCE SUMMARY block between Step 3c and Step 3d; PHASE 4 GATE CLEARANCE SUMMARY at Amend entry.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-12 Remediation log with exemption clause (0.5 pts)

If gate fails: REMEDIATION LOG with gate ID, cause, action. If all pass: C-12 EXEMPTION clause present.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-13 Schema 5 prerequisite verification lines (0.5 pts)

Each Phase 3 sub-step opens with a prerequisite verification line confirming the prior sub-step is complete.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-14 through C-21 (0.5 pts each, 4 pts total)

Criteria established from R2 through R7 excellence signals. All R11 variations are built on the accumulated R1–R10 base and produce outputs satisfying these criteria.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

### C-22 + C-23 (0.5 pts each, 1 pt total)

Criteria from R9 excellence signals. All R11 variations incorporate R9's structural patterns.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS | PASS | PASS | PASS | PASS |

---

## C-24 — Enforcement Class Citation (0.5 pts)

Pass condition: EG-FIRST EXECUTION CONSTRAINT block **explicitly cites** the Coverage Matrix Enforcement Class column.

The base prompt (shared by all R11 variations) carries the EG-FIRST block from R10. The citation is structurally present. The differentiation is whether V-03's annotation discipline makes the citation systematic and grep-discoverable vs. present-but-implicit.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | **PARTIAL (0.25)** | Base EG-FIRST block present from R10; V-01's NEEDS-REDESIGN EVIDENCE ANCHOR is in the Verdict section, not at EG-FIRST. Citation exists but is not reinforced by V-01's structural addition. |
| V-02 | **PARTIAL (0.25)** | Base EG-FIRST block present; V-02's arithmetic gate is at the promotion block. No annotation mechanism to make the enforcement class citation explicit at EG-FIRST. |
| V-03 | **PASS (0.5)** | Uniform `[enforcement: X]` suffix at every named invariant point of use. The EG-FIRST EXECUTION CONSTRAINT block now carries `[enforcement: instructional]` (or equivalent class label) as a required annotation. Citation is both present and explicitly labeled. |
| V-04 | **PARTIAL (0.25)** | V-01+V-02 combined. Neither V-01 nor V-02 introduces annotation; base citation present but not systematically reinforced. |
| V-05 | **PASS (0.5)** | V-03's annotation system present; annotations propagate to ALL blocks including the two new linkage blocks. EG-FIRST enforcement class citation is fully annotated and discoverable by grep scan. |

---

## C-25 — Membership Count-Check in Compliance Ledger (0.5 pts)

Pass condition: VC-4 G-1 compliance ledger entry includes a **count-check** validating the PHASE 2a/2b MEMBERSHIP declarations.

The R10 base includes this count-check. The differentiation is whether V-02's arithmetic principle (PROMOTION COMPLETENESS GATE) reinforces the count-check discipline in the VC-4 ledger.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | **PARTIAL (0.25)** | Base count-check present from R10. V-01's addition is verdict-focused (forward linkage from findings to verdict); does not reinforce or extend arithmetic discipline at the compliance ledger. Count-check present but structurally isolated. |
| V-02 | **PASS (0.5)** | PROMOTION COMPLETENESS GATE introduces `(promoted + remaining = Stage 1 SA count)` arithmetic as a named self-check principle. This arithmetic discipline propagates naturally to the VC-4 G-1 ledger entry, where the PHASE 2a/2b MEMBERSHIP count is anchored to the same arithmetic relationship. The count-check in the ledger is no longer incidental — it mirrors the promotion gate's arithmetic contract. |
| V-03 | **PARTIAL (0.25)** | Annotation system makes points of use visible but introduces no arithmetic. Base count-check present; not structurally reinforced. |
| V-04 | **PASS (0.5)** | V-02's arithmetic gate present; count-check in VC-4 ledger reinforced by the promotion arithmetic principle. V-01's evidence anchor adds forward linkage context that strengthens the overall ledger narrative. |
| V-05 | **PASS (0.5)** | V-02's arithmetic + V-03's annotation together. The VC-4 G-1 count-check carries `[enforcement: instructional]` annotation and is grounded in V-02's arithmetic contract. Strongest C-25 pass — count-check is both arithmetic and annotated. |

---

## Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (15) | 15 | 15 | 15 | 15 | 15 |
| C-02 (15) | 15 | 15 | 15 | 15 | 15 |
| C-03 (15) | 15 | 15 | 15 | 15 | 15 |
| C-04 (15) | 15 | 15 | 15 | 15 | 15 |
| C-05 (15) | 15 | 15 | 15 | 15 | 15 |
| C-06 (5) | 5 | 5 | 5 | 5 | 5 |
| C-07 (5) | 5 | 5 | 5 | 5 | 5 |
| C-08 (5) | 5 | 5 | 5 | 5 | 5 |
| C-09 (2) | 2 | 2 | 2 | 2 | 2 |
| C-10 (2) | 2 | 2 | 2 | 2 | 2 |
| C-11–C-23 (6.5) | 6.5 | 6.5 | 6.5 | 6.5 | 6.5 |
| C-24 (0.5) | 0.25 | 0.25 | 0.5 | 0.25 | 0.5 |
| C-25 (0.5) | 0.25 | 0.5 | 0.25 | 0.5 | 0.5 |
| **TOTAL** | **101.0** | **101.25** | **101.25** | **101.25** | **101.5** |

**Ranking**: V-05 (101.5) > V-02 = V-03 = V-04 (101.25) > V-01 (101.0)

All variations clear the golden threshold: 5 essential criteria pass AND composite ≥ 80.

---

## Excellence Signals from V-05

Three structural patterns present in V-05 that exceed any current rubric criterion:

**Pattern 1 — NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26 candidate, Verdict section)
The Verdict block names EG finding IDs from the Step 3b table directly (`EG-01`, `EG-02`, …`EG-N`). The EG count is derived by enumerating the list, not asserted as prose ("3 EG gaps were found"). The verdict classification for NEEDS-REDESIGN becomes machine-verifiable: reader can count the listed IDs and confirm the threshold. Forward linkage path: Step 3b findings table → Verdict.

**Pattern 2 — PROMOTION COMPLETENESS GATE** (C-27 candidate, SA-TO-SG PROMOTION block)
An arithmetic self-check block appears at the promotion lifecycle event: `promoted_count + remaining_count = stage1_SA_count`. If the sum mismatches, a MISMATCH block fires and Phase 2b does not proceed. This makes the promotion inventory self-validating — the three counts must reconcile before continuing. Forward linkage path: Stage 1 SA relay count → promotion block arithmetic → Phase 2b entry. The arithmetic discipline also propagates to the VC-4 G-1 compliance ledger entry (C-25 boost).

**Pattern 3 — Uniform `[enforcement: X]` annotation suffix** (C-28 candidate, applied everywhere)
Every named invariant at every point of use carries an explicit enforcement class annotation: `[enforcement: instructional]`, `[enforcement: structural]`, etc. Coverage includes: G-1/G-2/G-3 individual lines, FLOOR CHECK, Schema 5 prerequisite lines, Phase 2a/2b membership declarations, EG-RELAY COMPLETE, Amend channel field, and the two new linkage blocks from C-26 and C-27. A `grep` for `[enforcement:` returns the complete enforcement inventory without consulting the Coverage Matrix. In V-05, this propagation to the new blocks makes the annotation discipline complete: no named invariant lacks its enforcement class.

**V-05 integration point**: The two forward linkage blocks (C-26 and C-27) each carry `[enforcement: instructional]` via C-28's annotation discipline. The linkage mechanism is not just structurally present — it is annotated, making it discoverable in the same grep pass as every other enforcement point in the trace.

---

```json
{"top_score": 101.5, "all_essential_pass": true, "new_patterns": ["NEEDS-REDESIGN EVIDENCE ANCHOR — Verdict names EG finding IDs from Step 3b explicitly; EG count derived by enumeration not assertion; forward linkage Step 3b → Verdict makes NEEDS-REDESIGN classification machine-verifiable", "PROMOTION COMPLETENESS GATE — arithmetic self-check at SA-TO-SG PROMOTION: promoted + remaining = Stage 1 SA count; MISMATCH fires and blocks Phase 2b; forward linkage Stage 1 SA relay → promotion block; arithmetic discipline propagates to VC-4 G-1 ledger count-check", "Uniform [enforcement: X] suffix at every named invariant point of use including new linkage blocks — grep for [enforcement: returns complete enforcement inventory; annotation propagated to NEEDS-REDESIGN EVIDENCE ANCHOR and PROMOTION COMPLETENESS GATE making enforcement class discoverable without Coverage Matrix lookup"]}
```
