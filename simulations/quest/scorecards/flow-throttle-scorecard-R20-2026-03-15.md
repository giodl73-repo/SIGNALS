## flow-throttle — Round 20 Scoring

**Rubric:** v20 | **Max composite:** 325 | **Variants scored:** V-01 through V-05

---

### Baseline

R19 all variants: 310/325 — C-53/C-54/C-55 FAIL across the board.
R20 task: add all three simultaneously without disrupting C-01–C-52 coverage.

---

## Criterion-by-Criterion Evaluation

### C-53 — "Cannot skip because" causal consequence clause per atomized sub-step

Each G-step must carry a co-located clause naming the specific structural failure of collapsing that step. Global non-collapsibility assertion does not satisfy.

| Variant | Evidence | Verdict |
|---------|----------|---------|
| V-01 | G-1: `Consequence of skipping:` — bypass-gate detection omitted, bypass invisible after fact. G-2: SIG-01 presence gate unchecked, error propagates silently. G-3: count unchecked, SIG-02 issued without count confirmation. G-4: handoff undeclared, Role 2 cannot verify activation condition. 4 clauses, each names specific failure per step. | **PASS** |
| V-02 | GATE-B G-1–G-4 each carry `Cannot skip because:` inline clauses. G-1: structural bridge between GATE-A bypass detection and GATE-B count — skipping leaves bypass undetected at count steps. G-2: upstream phase dependency unverified. G-3: only step that verifies count = 7 vs. assumed. G-4: explicit handoff absent, Role 2 self-activates. 4 clauses, each per-step. | **PASS** |
| V-03 | P0-A through P0-D each carry `Cannot collapse because:` clauses arguing from phase-contract semantics. P0-A: bypass-attempt lifecycle artifact absent if collapsed. P0-B: upstream phase boundary unverifiable. P0-C: only checkpoint dedicated to count, collapsing into P0-D removes block. P0-D: phase exit artifact absent, transition implicit. 4 clauses, phase-boundary-property framing. | **PASS** |
| V-04 | G-1–G-4 each carry `SHALL NOT COLLAPSE — Consequence of collapse:` blocks in SHALL-register. Consequence clause linguistically co-equal with the prohibition, not parenthetical. G-1: bypass-gate verdict unconfirmed at count boundary. G-2: collapse conflates two non-overlapping failure modes (sections absent vs. count short). G-3: count verification and signal issuance merge, removes structural separation. G-4: boundary artifact absent. 4 blocks, SHALL-class. | **PASS** |
| V-05 | GATE-B G-1–G-4 `Cannot skip because:` clauses each name the specific inertia bypass path the step defeats: G-1 defeats `GATE-A complete = bypass detected` path. G-2 defeats `GA-COMPLETE present = upstream complete` path. G-3 defeats `7 rows visibly present` visual-inspection path. G-4 defeats `count passed = INVENTORY VERIFIED implied` path. Consequence clause precision elevated from structural-failure naming to executor-pattern naming. | **PASS** |

---

### C-54 — Multi-criterion joint evidence row for inertia-bypass detection

Field 5 audit table must contain one row that jointly cites C-44 + C-47 + C-48 artifacts simultaneously. Individual artifact rows do not satisfy; joint co-presence must be a single-row column-scan task.

| Variant | Evidence | Verdict |
|---------|----------|---------|
| V-01 | Row 9 in Field 5 table: "Bypass-detection co-presence: bypass register row AND G-1 gate fill AND SIG-01 presence all confirmed in a single audit row" / C-44+C-47+C-48 (C-54) / "Bypass register Attempt type cell cited AND G-1 fill field value cited AND SIG-01 Handoff cell cited — all three artifacts cited simultaneously in this single row, not across separate rows." Three-artifact joint row present. | **PASS** |
| V-02 | Row 9 in Field 5: "Bypass-detection co-presence: GATE-A bypass register row AND GATE-A bypass gate field AND Role 1 SIG-01 — all three artifacts cited simultaneously" / C-44+C-47+C-48 (C-54) / "Bypass register Attempt type cell... AND GATE-A BYPASS GATE FIELD fill value... AND SIG-01 Handoff cell... — cite all three in this single row; joint citation in one scan confirms co-presence." Three-artifact joint row present. | **PASS** |
| V-03 | Row 9 in Field 5: "Phase 0 co-presence gate: P0-A gate field AND Phase 0 bypass register row AND SIG-01 phase-exit record — all three lifecycle artifacts cited simultaneously" / C-44+C-47+C-48 (C-54) / "P0-A gate field value... AND Phase 0 bypass register Attempt type cell... AND SIG-01 Phase 0 Exit signal cell... — cite all three artifacts in this single row; joint citation confirms Phase 0.1–0.4 bypass-detection lifecycle stack intact as co-presence condition." Three-artifact joint row, lifecycle framing. | **PASS** |
| V-04 | Row 9 labeled `SHALL-JOINT-AUDIT`: "bypass-detection co-presence: bypass register row AND bypass gate fill AND SIG-01 SHALL all be cited simultaneously in this single row; citing them in separate rows SHALL FAIL" / C-44+C-47+C-48 (C-54) / "SHALL cite bypass register Attempt type cell AND bypass gate fill value AND SIG-01 Handoff cell simultaneously in this row entry; a response that cites each in its individual row above without this joint row SHALL be assessed as FAIL for C-54 regardless of individual row correctness." Strongest obligation form — explicitly names separate-row citation as failing evidence. | **PASS** |
| V-05 | Row 9 labeled "Inertia-bypass confirmation: bypass-detection mechanism defeated": "GATE-A bypass register Attempt type cell AND GATE-A BYPASS GATE FIELD fill value AND SIG-01 GATE-B Handoff cell — cite all three artifacts in this single row simultaneously; a response that cites them in separate rows above without this joint row confirms individual artifacts but does not confirm co-presence; separate-row citation fails C-54." Joint row framed as inertia-bypass defeat confirmation, not just co-presence check. | **PASS** |

---

### C-55 — Non-conflation verbatim quote in contracted blockquote format with obligation label

Verbatim "Does NOT confirm" cell citation must be blockquoted and carry an obligation-class label naming the quote as contracted/authoritative. Inline verbatim quote fails.

| Variant | Evidence | Verdict |
|---------|----------|---------|
| V-01 | `> **SHALL-authoritative cell value:** "That Section C annotation count = declared count of 7"` — blockquoted, label `SHALL-authoritative cell value:`, obligation-class named. Surrounding text states "not merely evidential — it is the contractual artifact." | **PASS** |
| V-02 | `> **quoted-artifact citation (SHALL-authoritative):** "That Section C annotation count = declared count of 7"` — blockquoted in GATE-A, label `quoted-artifact citation (SHALL-authoritative)`. Surrounding text: "not a summary or paraphrase." | **PASS** |
| V-03 | `> **Phase 0 contracted lifecycle referent (phase-boundary non-conflation):** "That Section C annotation count = declared count of 7"` — blockquoted, label names the phase-boundary obligation. Surrounding text: "non-collapsible boundary between Phase 0 and Phase 1 readiness." | **PASS** |
| V-04 | `> **SHALL-authoritative contracted cell value:** "That Section C annotation count = declared count of 7"` — blockquoted, preceded by `SHALL-REPRODUCE-VERBATIM` directive. Label `SHALL-authoritative contracted cell value:` in SHALL-register. Field 5 row confirms: "Separate inline quote without blockquote SHALL FAIL this check." | **PASS** |
| V-05 | `> **SHALL-authoritative cell value (inertia-bypass detection anchor):** "That Section C annotation count = declared count of 7"` — blockquoted in GATE-A, label names both obligation class AND the specific inertia path the citation defeats. Surrounding text: "This is not a summary of the column... the inertia path would have paraphrased; this clause prevents paraphrase." | **PASS** |

---

## Full Composite Scores

All variants inherit C-01–C-52 fully from R19 baseline (310/310 under v19 = 310 pts under v20). R20 adds C-53+C-54+C-55 (3 × 5 = 15 pts).

| Criterion band | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|------|------|------|------|------|
| C-01–C-05 (essential, 12 pts each) | 60 | 60 | 60 | 60 | 60 |
| C-06–C-08 (recommended, 10 pts each) | 30 | 30 | 30 | 30 | 30 |
| C-09–C-52 (aspirational × 44, 5 pts each) | 220 | 220 | 220 | 220 | 220 |
| C-53 | 5 | 5 | 5 | 5 | 5 |
| C-54 | 5 | 5 | 5 | 5 | 5 |
| C-55 | 5 | 5 | 5 | 5 | 5 |
| **Composite** | **325** | **325** | **325** | **325** | **325** |
| All essential PASS? | Yes | Yes | Yes | Yes | Yes |

---

## Variant Ranking

All five variants score 325/325. Ranking is by implementation richness of the three new criteria:

| Rank | Variant | Distinguishing quality |
|------|---------|------------------------|
| 1 | **V-05** | Named inertia path per consequence clause (executor-pattern framing, not just structural-failure framing); inertia path defeated in header Responsibility column (header-scannable); blockquote label names what the citation defeats `(inertia-bypass detection anchor)`; joint audit row titled as "Inertia-bypass confirmation: bypass-detection mechanism defeated" |
| 2 | **V-04** | SHALL-register consequence clauses (`SHALL NOT COLLAPSE — Consequence of collapse:`) make prohibition and consequence co-equal mandates; Field 5 Evidence column renamed `SHALL cite`; joint audit row explicitly states separate-row citation "SHALL be assessed as FAIL for C-54 regardless of individual row correctness" — strongest disambiguation |
| 3 | **V-02** | Five-role chain gives GATE-A single-responsibility for signal distinction + bypass, GATE-B single-responsibility for count — consequence clauses argue from role-contract semantics |
| 4 | **V-03** | Lifecycle-phase framing makes consequence clauses argue from phase-boundary semantics; Phase 0 contracted lifecycle referent label names the phase-transition condition |
| 5 | **V-01** | Clean four-role baseline; `Consequence of skipping:` sub-field co-located inside each step block; most minimal C-53/C-54/C-55 implementation — clear reference form |

---

## Excellence Signals from V-05 (Top-Ranked)

**Signal ES-01 — Named inertia path per consequence clause**

V-05's G-steps name the specific rational-executor inertia bypass path each sub-step defeats rather than only naming the structural failure:

- G-1 defeats: `` `GATE-A complete = bypass detected` inertia path ``
- G-2 defeats: `` `GA-COMPLETE present = upstream complete` inertia path ``
- G-3 defeats: `` `7 rows visibly present` visual-inspection inertia path ``
- G-4 defeats: `` `count passed = INVENTORY VERIFIED implied` inertia path ``

This is a precision upgrade over C-53's baseline: C-53 requires a structural failure to be named; V-05 names the executor-pattern that generates that failure. The consequence clause connects to the bypass-detection register rather than standing alone as an independent annotation.

**Signal ES-02 — Inertia-bypass framing in the header table Responsibility column**

V-05 adds "defeat inertia path: SIG-01 ≠ analysis-ready" to GATE-A's Responsibility cell and "with inertia-bypass consequence clauses" to GATE-B's Responsibility. The three-level bypass framing (header-scannable + gate-internal + per-step consequence) becomes fully layered — inertia-bypass architecture is declared at the same structural level as signal chains and bypass conditions. This applies the C-46/C-51 visibility pattern (make role architecture header-scannable) to the inertia-bypass framing layer.

**Signal ES-03 — Blockquote obligation label names the defeated inertia path**

V-05: `**SHALL-authoritative cell value (inertia-bypass detection anchor):**`

The `(inertia-bypass detection anchor)` suffix names what the contracted artifact defeats — the executor who merges SIG-01 and SIG-02 because "the distinction is obviously clear from context." The label is not just an obligation-class marker; it is a bypass-pattern pointer. The blockquote becomes the precise artifact that prevents the merger-inertia error, and the label names that connection explicitly.

---

## Round 20 Summary

All five variants achieve 325/325. R20 closes the three gaps left by R19 simultaneously across five structural axes (output format, role sequence, lifecycle framing, SHALL-register, combined). No partial scores; no variance in composite.

The dominant precision upgrade in R20: consequence clauses can carry either structural-failure framing (what breaks) or executor-pattern framing (which rational-executor path is defeated). V-05 demonstrates that the two are composable — each sub-step can name both the structural failure and the inertia path that would produce it, connecting the per-step argument to the bypass-detection register at the same level of specificity.

---

```json
{"top_score": 325, "all_essential_pass": true, "new_patterns": ["Named inertia path per consequence clause — each Cannot-skip-because clause names the specific rational-executor bypass path the sub-step defeats (not just the structural failure), connecting the per-step argument to the bypass-detection register pattern", "Inertia-bypass framing in header table Responsibility column — the defeated inertia path is declared in the header role-chain Responsibility cell, making inertia-bypass architecture header-scannable at the same level as signal chains and bypass conditions", "Blockquote obligation label names the defeated inertia path — the obligation-class label carries a parenthetical anchor naming which merge-inertia error the contracted artifact prevents, connecting the citation to the bypass-pattern it structurally defeats"]}
```
