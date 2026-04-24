I now have everything needed. Let me score all five variations.

---

## listen-support Round 16 — Scoring Report

**Rubric version:** v15 (C-01 through C-46, 280 pt ceiling)
**Base:** V-05 R15 — 280/280 on all prior criteria
**Probe ceiling:** 295 pts (C-47 + C-48 + C-49 candidate, 5 pts each)

---

### Scoring Method

All R16 variations are built on V-05 R15 as the explicit base ("all other mechanisms from V-05 R15 are preserved exactly"). V-05 R15 scores 280/280 under v15 — C-01 through C-46 all at ceiling. The R16 variations therefore inherit 280/280 and compete only on the three probe criteria. Each variation is checked for:

1. Any modification that **breaks** an inherited criterion  
2. Which probe criteria (C-47, C-48, C-49) are structurally satisfied

---

### Inherited Criteria Audit (C-01 through C-46)

All five variations preserve the full V-05 R15 machinery:

| Check | Verdict | Evidence |
|-------|---------|----------|
| Essential C-01 through C-05 (60 pts) | **PASS all** | No variation removes ticket fields, vocab, personas, gap sub-sections, or ticket count |
| Recommended C-06 through C-08 (30 pts) | **PASS all** | Phase-map table, persona-authentic bodies, differentiated severity/volume preserved |
| C-20 vocabulary pre-commitment table | **PASS all** | Step 5 with locked cells present in all variations |
| C-38 dual-field Step-4 gate | **PASS all** | All prompts: "all three items" with own-words restatement + verbatim anchor + PHASE DISTRIBUTION block |
| C-41 imperative gate language | **PASS all** | "Do not fill any cell" — imperative prohibition form in all five |
| C-42 cell-level prohibition | **PASS all** | "any cell" granularity in all five Step 5 gates |
| C-43 triple verbatim-prohibition clause | **PASS all** | "do not paraphrase, do not summarize, copy it verbatim word-for-word" in exception blocks for all |
| C-44 no-exception path triple-clause | **PASS V-01/V-04/V-05** | V-01 axis preserved: Phase 1 + Phase 3 no-exception paths carry triple-clause |
| C-44 for V-02/V-03 | **PASS** | V-02 and V-03 inherit from V-05 R15 which already satisfies C-44 — description confirms "all other mechanisms preserved" |
| C-45 phase distribution pre-commitment | **PASS all** | PHASE DISTRIBUTION committed block as third required item in Step 5 for all five |
| C-46 switching-friction min-count gate | **PASS all** | All carry SWITCHING-FRICTION COUNT pre-declaration; V-01/V-02/V-04 floor ≥ 2 (satisfies C-46), V-03/V-05 floor ≥ 3 (strictly stronger, also satisfies C-46) |
| C-35 paraphrase consistency confirmation | **PASS all** | Inherited from V-05 R15 |
| C-36 exception block paraphrase-clause field | **PASS all** | Inherited from V-05 R15 |
| C-39 scope confirmation | **PASS all** | "Confirmation: this rule applies to every severity assignment in the table below" present in all |

**Result:** No variation breaks any criterion C-01 through C-46. All five start at 280/280.

---

### Probe Criteria Scoring

#### C-47 — Phase-2 No-Exception Triple-Clause

**Definition:** The Phase 2 no-exception confirmation path in Pass 2C carries the same triple-clause verbatim form ("do not paraphrase, do not summarize, copy it verbatim word-for-word") as the Phase 1 and Phase 3 paths required by C-44.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS** | Pass 2C explicitly adds a Phase 2 scan: "No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback). Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated) at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]." Triple-clause present on all three phase scan paths. |
| V-02 | **FAIL** | V-02 only adds Sub-check 3 (post-generation re-verify). Pass 2C has Phase 1 and Phase 3 scans but no Phase 2 scan path. Phase 2 is a blind spot. |
| V-03 | **FAIL** | V-03 only adds lifecycle pre-declaration and switching-friction floor ≥ 3. Pass 2C has Phase 1 and Phase 3 no-exception paths only. |
| V-04 | **PASS** | Inherits V-01 axis. Pass 2C Sub-check 1 has all three phase scans — Phase 1, Phase 2, Phase 3 — each with triple-clause verbatim form. Phase-organized output format (V-02 axis) does not disturb the Pass 2C structure. |
| V-05 | **PASS** | Full synthesis inherits V-01 axis. Pass 2C Sub-check 1 includes the Phase 2 scan: "No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback). Governing paraphrase clause: [do not paraphrase, do not summarize, copy it verbatim word-for-word]." Triple-clause uniform across all three scan paths. Paraphrase consistency confirmation confirms: "All three phase Paraphrase clause fields carry triple-clause verbatim: YES." |

---

#### C-48 — Post-Generation Phase Distribution Re-Verify

**Definition:** After body generation, Part C Sub-check 3 counts actual Phase 1/2/3 card bodies and compares to the committed block from Step 5. A mismatch at Sub-check 3 that was not present at Step 5B constitutes generation-drift, named explicitly.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Pass 2C has Sub-checks 1 and 2 only. No Sub-check 3 post-generation count. Generation-drift window remains open. |
| V-02 | **PASS** | Explicitly adds Sub-check 3 in Part C: "Post-generation phase distribution: Phase 1 bodies generated: [n]. Committed: [n]. MATCH / MISMATCH. Phase 2 … Phase 3 … Total …" Names discrepancy as generation-time drift. Phase-organized output format (section headers mark phase boundaries) makes the count self-confirming without ticket-ID parsing. |
| V-03 | **FAIL** | No Sub-check 3 in Pass 2C. V-03 adds lifecycle pre-declaration and switching-friction floor only. |
| V-04 | **PASS** | Inherits V-02 axis. Sub-check 3 present. Notably, V-04's phase-organized output (V-02 axis) combined with SRE-first role ordering (V-01 axis) means the Phase 2 section in Step 6 reflects non-trivial operational escalation patterns, making the post-generation count verification meaningful rather than trivially passing. V-05 R15 target referenced in three-way comparison: body count vs Step 5 committed vs Step 1 target. |
| V-05 | **PASS** | Sub-check 3 present with three-way comparison (generated / Step 5 committed / Step 1 target per phase). States final: "Post-generation phase distribution matches committed block and Step 1 target." Generation-drift detection is architecturally complete: pre-generation commitment (Step 5) + pre-body audit (Step 5B Constraint 0) + post-generation re-verify (Sub-check 3) close all temporal windows. |

---

#### C-49 — Switching-Friction Count Floor ≥ 3

**Definition:** The switching-friction sub-section requires SWITCHING-FRICTION COUNT ≥ 3, with the third entry structurally constrained to cover a Phase 2 migration barrier (surfaces after partial commitment, not on day one). Pass 2B item 4 verifies count compliance. Pass 2 Sub-check 2 restates the count and confirms the third entry covers a Phase 2 barrier.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | Step 5C item 4: "N must be ≥ 2." Step 8: "N must be ≥ 2." Two-entry floor; no third-entry type constraint. C-46 PASS but C-49 FAIL. |
| V-02 | **FAIL** | Step 5C item 4: "N must be ≥ 2." Same two-entry floor. C-46 PASS but C-49 FAIL. |
| V-03 | **PASS** | Step 5C item 4: "N must be ≥ 3. Do not proceed to Step 6 if N < 3." Step 8: "N must be ≥ 3." Third entry structural constraint: "Cover a Phase 2 migration barrier — a friction that only surfaces after partial commitment, when the user has started migrating workflows but not fully detached from the competitor. Prohibited: a barrier that day-one users would also encounter." Pass 2 Sub-check 2 restates: "SWITCHING-FRICTION COUNT: [N]. N ≥ 3: YES/NO." and confirms "Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO." All three structural elements present: floor gate, third-entry type constraint, post-generation compliance confirmation. |
| V-04 | **FAIL** | Combines V-01 + V-02 axes. No V-03 axis. Step 5C item 4: "N must be ≥ 2." Two-entry floor. C-46 PASS, C-49 FAIL. |
| V-05 | **PASS** | Full synthesis includes V-03 axis. Step 5C item 4: "N must be ≥ 3. Do not proceed to Step 6 if N < 3. Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment, not on day one)." Step 8 entry guidance: Entry 1 = primary day-one friction, Entry 2 = second most prominent barrier, Entry 3 = Phase 2 barrier only (explicitly prohibited: "a barrier that day-one users would also encounter"). Sub-check 2: "N ≥ 3: YES/NO … Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO." Final statement includes "SWITCHING-FRICTION COUNT ≥ 3 confirmed. Third entry covers Phase 2 barrier: YES." |

---

### Composite Scores

| Variation | C-01..C-46 | C-47 | C-48 | C-49 | Score | Delta from base |
|-----------|-----------|------|------|------|-------|-----------------|
| V-01 | 280 | PASS (+5) | FAIL | FAIL | **285 / 295** | +5 |
| V-02 | 280 | FAIL | PASS (+5) | FAIL | **285 / 295** | +5 |
| V-03 | 280 | FAIL | FAIL | PASS (+5) | **285 / 295** | +5 |
| V-04 | 280 | PASS (+5) | PASS (+5) | FAIL | **290 / 295** | +10 |
| V-05 | 280 | PASS (+5) | PASS (+5) | PASS (+5) | **295 / 295** | +15 |

---

### Rankings

1. **V-05 — 295/295** — Full synthesis: all three probes. Zero failures.
2. **V-04 — 290/295** — C-47 + C-48 PASS; C-49 FAIL (two-entry switching-friction floor).
3. **V-01 — 285/295** — C-47 only; no post-generation re-verify, no ≥3 friction floor.
4. **V-02 — 285/295** — C-48 only; no Phase 2 no-exception triple-clause, no ≥3 friction floor.
5. **V-03 — 285/295** — C-49 only; no Phase 2 scan, no post-generation re-verify.

V-01/V-02/V-03 are tied at 285. Within the three-way tie, V-01 and V-02 are architecturally more composable (they combine cleanly into V-04), while V-03 introduces the most structurally novel probe (third-entry type constraint adds semantic coverage requirement, not just a count floor).

---

### Excellence Signals from V-05

**Signal 1: Phase-scan symmetry — all three phases under the same verbatim standard**

C-44 (R15) closed the condensation path on Phase 1 and Phase 3 no-exception paths. C-47 (V-05 R16) closes the same path on Phase 2. The quality upgrade is not incremental — it makes the verbatim standard *uniform* across the entire phase-scan surface. When SRE-first role ordering produces non-trivial Phase 2 escalation patterns (operational concerns surface earlier), the Phase 2 scan has real content to audit rather than trivially empty confirmation. Symmetry is both a structural and epistemic gain: a model cannot compress a Phase 2 commitment while being held to strict verbatim on Phase 1 and Phase 3.

**Signal 2: Temporal closure — pre-generation commitment + pre-body audit + post-generation re-verify**

V-05 combines three temporal verification gates for phase distribution: Step 5 commitment (before cells are filled), Step 5B Constraint 0 (before card bodies are written), and Sub-check 3 (after card bodies are generated). Each gate closes a distinct drift window. Phase-organized output (section headers marking Phase 1 / Phase 2 / Phase 3 boundaries) converts the post-generation count from a ticket-ID-parsing task into a section-header-counting task — the output format is structurally aligned with its own verification mechanism. This is a design principle: verification gates are strongest when the output structure makes violations visible without prose parsing.

**Signal 3: Third-entry type specification — count floor + content constraint**

Raising the switching-friction floor from 2 to 3 closes the dual-entry surface-coverage gap. But the more extractable signal is the *type constraint* on the third entry: it must cover a Phase 2 migration barrier, not a day-one friction point. A count floor alone (even ≥ 3) permits three day-one friction points, achieving count compliance while concentrating entries in Phase 1 and missing the qualitatively different friction that only surfaces after partial workflow commitment. The type constraint forces lifecycle-distributed coverage: the switching-friction inventory must span adoption phases, not pile into the entry-level barrier space. This generalizes: entry-type constraints close the surface-coverage gap that minimum-count floors leave open.

---

### C-47/C-48/C-49 Signal Logic Confirmation

The three probes are structurally independent and composable:

- **C-47** targets Pass 2C scan coverage (new phase scan location)
- **C-48** targets verification timing (new post-generation temporal gate)  
- **C-49** targets switching-friction surface coverage (new minimum threshold + content type constraint)

V-05 demonstrates zero structural interference between the three probes when combined: the Phase 2 scan in Sub-check 1, the post-generation count in Sub-check 3, and the three-entry friction inventory in Step 8 / Sub-check 2 operate on non-overlapping output surfaces and can be verified independently.

---

```json
{"top_score": 295, "all_essential_pass": true, "new_patterns": ["Phase-2 no-exception triple-clause closes the verbatim-standard asymmetry C-44 leaves open — all three phase scan paths now held to the same standard, making the SRE-first role ordering meaningful by producing non-trivial Phase 2 escalation content to audit", "Post-generation phase distribution re-verification paired with phase-organized output creates a self-confirming structural gate where section header counting replaces ticket-ID parsing, aligning output format with its own verification mechanism", "Switching-friction third-entry type constraint (Phase 2 migration barrier only) forces lifecycle-distributed surface coverage that a count floor alone cannot — three day-one entries satisfy a floor-of-3 without capturing transition-zone friction, so the entry-type specification is the load-bearing mechanism"]}
```
