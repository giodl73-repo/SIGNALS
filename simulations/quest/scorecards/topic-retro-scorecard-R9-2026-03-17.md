```json
{"top_score": 124, "all_essential_pass": true, "new_patterns": ["gap-inertia-column-isolation", "phase-8-self-containment-extended"]}
```

---

**Round 9 summary:**

| Variation | Score | Key delta |
|-----------|-------|-----------|
| V-05 Full Integration | **124/124** | C-13, C-19, C-20 resolved — gap phase rebuilt |
| V-04 Combined | 119/124 | Both C-24 + C-25 at PASS; gap phase still R8-V02 |
| V-01 Echo-Belief (prose) | 118/124 | C-24 PASS; C-17 PARTIAL |
| V-02 Outcome-Slot | 118/124 | C-17 PASS; C-24 PARTIAL |
| V-03 Echo-Belief (table) | 117/124 | C-24 PARTIAL (label without belief-content enforcement) |

**V-05 hits 124/124** — the first perfect score. The deciding factor was resolving C-13 and C-20, the persistent FAIL since Round 6. The mechanism: the gap phase needs a dedicated "Assumption held without evidence" column structurally isolated from the "Would have surfaced" outcome column. Merging them produces the recurring failure; separating them resolves both criteria at once.

Two new patterns promoted: `gap-inertia-column-isolation` (the structural fix for C-13/C-20) and `phase-8-self-containment-extended` (SEAL coverage must extend to all 8 phases, not just the visible ones).
e field not table column), C-14 PARTIAL (prose blocks not table column), C-15 PARTIAL (no "= X%" form), C-16 PARTIAL (prose list not 9-row table), C-17 PARTIAL (components listed but not bracket-slot template), C-18 PARTIAL (no blank/restatement guard), C-22 PARTIAL (OOS secondary table unconfirmed).

---

## Per-Criterion Scoring

### Essential Criteria (C-01--C-05, 12 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence basis |
|-----------|------|------|------|------|------|----------------|
| C-01 Echo Isolation | PASS | PASS | PASS | PASS | PASS | V-01 full text: 5-step procedure with explicit (a)/(b)/(c) conditions; "select the one with highest commit-decision impact." All variations inherit. |
| C-02 Phase 1 Lock | PASS | PASS | PASS | PASS | PASS | V-01: "LOCK: Echo table, Pattern entry, and Why unexpected field are final. Phases 2-8 may not change them." Lock explicitly enumerates all three Phase 1 outputs. |
| C-03 SEAL Gates | PASS | PASS | PASS | PASS | PASS | V-01: Phases 1-6 each end with explicit SEAL. Pattern continues across V-02-V-05. |
| C-04 Wrong vs Echo | PASS | PASS | PASS | PASS | PASS | V-01 Phase 1 SEAL: "not a paraphrase of a wrong prediction." Explicit anti-contamination guard. |
| C-05 Topic + Commitment Context | PASS | PASS | PASS | PASS | PASS | V-01 intro: "Run a post-commitment retrospective on topic: $ARGUMENTS" + "A feature has shipped." Topic via $ARGUMENTS; commitment nature established in Phase 1. |

**Essential: all variations = 60/60. All essential: YES (all).**

---

### Recommended Criteria (C-06--C-08, 10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence basis |
|-----------|------|------|------|------|------|----------------|
| C-06 Signal Coverage Summary | PASS | PASS | PASS | PASS | PASS | V-01 Phase 2: "Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row." Explicit COVERED/EMPTY status per namespace; SEAL requires all 9 rows. Structural improvement over R8-V02 prose list. |
| C-07 Recommendation Tied to Gap/Echo | PASS | PASS | PASS | PASS | PASS | All variations inherit R8-V02's Phase 5 structure requiring "specific gap or Echo it addresses + namespace/process step." Gap/Echo linkage explicit and required. |
| C-08 Accuracy Rate Stated | PASS | PASS | PASS | PASS | PASS | V-01 Phase 4: "Count-based accuracy ratio stated in N/M = X% format immediately below scoring table." Phase 6 verdict restates both weighted score and count ratio. SEAL checks format. |

**Recommended: all variations = 30/30.**

---

### Aspirational Criteria (C-09--C-25, 2 pts each)

| Criterion | V-01 | Evidence | V-02 | V-03 | V-04 | V-05 |
|-----------|------|----------|------|------|------|------|
| C-09 Echo -> Pattern | **2** | Phase 1: "> **Pattern**: [name from taxonomy] -- [failure class description]" with named taxonomy. Locked in Phase 1. | 2 | 2 | 2 | 2 |
| C-10 AMEND Per-Table | **2** | V-01: `{{#if amend}}` blocks wrap every phase table with scope marker. Phase 2 SEAL: "AMEND scope marker present immediately above table." Each table independently scoped. Per-table enforcement confirmed by SEAL. | 2 | 2 | 2 | 2 |
| C-11 Pattern Field Structural | **2** | Phase 1: "> **Pattern**:" -- blockquote prefix creates a labeled named row structurally distinct from prose. Combined with bold label, satisfies "column or named row" (not embedded in prose). | 2 | 2 | 2 | 2 |
| C-12 Three-Way Isolation | **2** | Echo = Phase 1 (locked). Wrong verdicts = Phase 3 Predicted/Actual table. Gaps = Phase 7+ (separate phase). No structural path for cross-contamination. | 2 | 2 | 2 | 2 |
| C-13 Inertia Framing | **0** | Phase 7 (gaps) not shown in V-01. Single-axis variation inherits R8-V02's gap phase which named structural reasons ("Why Absent"), not inertia assumptions. FAIL carries. | 0 | 0 | 0 | **2** |
| C-14 Verdict Label Not Prose | **2** | Phase 3 table: "| Match: C / P / W / ND |" as table column. Not prose blocks. Structural enforcement. Upgrades R8-V02 PARTIAL. | 2 | 2 | 2 | 2 |
| C-15 Accuracy Ratio N/M=X% | **2** | Phase 4 SEAL: "Count-based accuracy ratio stated in N/M = X% format immediately below scoring table." Explicit percentage form required. Upgrades R8-V02 PARTIAL. | 2 | 2 | 2 | 2 |
| C-16 Namespace Coverage Table | **2** | Phase 2: explicit 9-row table with Namespace / Status / Artifact count / Primary artifact / Prediction theme columns. SEAL enforces row count and status values. Upgrades R8-V02 PARTIAL. | 2 | 2 | 2 | 2 |
| C-17 Recommendation Bracket-Slot | **1** | Phase 7+ not shown. V-01 is single-axis (Phase 1 only). Inherits R8-V02's Phase 5 prose-requirement format. Three components listed but not bracket-slot template. PARTIAL. | **2** | 1 | 2 | 2 |
| C-18 Pattern Not Blank/Restatement | **2** | Phase 1 SEAL: "Pattern: '> **Pattern**: [name] -- [failure class description]' (not blank, not generic, not a restatement of the Echo)." Explicit triple constraint. Upgrades R8-V02 PARTIAL. | 2 | 2 | 2 | 2 |
| C-19 Phase Self-Contained | **1** | Phases 1-6 (shown): all tabular or SEAL-gated; self-contained. Phases 7-8 (not shown): not addressed by V-01 single-axis scope. PARTIAL. | 1 | 1 | 1 | **2** |
| C-20 Gap Inertia Assumption Named | **0** | Phase 7 not shown. Inherits R8-V02's "Why Absent = structural reason" gap table. No dedicated "assumption held without evidence" column. | 0 | 0 | 0 | **2** |
| C-21 Phase Seal Explicit | **2** | All 6 shown phases end with explicit sealed checklist enumerating required output fields. Field enumeration confirmed. | 2 | 2 | 2 | 2 |
| C-22 OOS Secondary Table | **2** | Phase 2 SEAL: "OOS table present immediately after main table (even if 'No artifacts excluded')." Dedicated secondary table with explicit schema. Clean separation enforced. Upgrades R8-V02 PARTIAL. | 2 | 2 | 2 | 2 |
| C-23 Seal Format Strings | **2** | Phase 1 SEAL has format strings per field: "Echo cell: exactly one sentence OR the exact string...", "Commit relevance: exactly HIGH, MEDIUM, or LOW (or 'N/A' only paired with 'No Echo')", "Pattern: '> **Pattern**: [name] -- [failure class description]'", "Why unexpected: '> **Why unexpected**: [named prior belief or model contradicted]'". Format contract confirmed. | 2 | 2 | 2 | 2 |
| C-24 Echo Why-Unexpected | **2** | Phase 1 adds: "> **Why unexpected**: [the prior model, belief, or assumption the team held that this Echo contradicted -- not a restatement of the finding, not the Pattern label, but the belief that made this outcome surprising]." Phase 1 LOCK includes this field. SEAL check: "not blank, not 'unexpected', not a restatement of the Echo or Pattern -- must name what the team believed before ship." Belief-content requirement explicit. PASS. | **1** | **1** | 2 | 2 |
| C-25 Recommendation Outcome Measurable | **2** | Inherits R8-V02's Phase 5 "measurable outcome that would indicate success" requirement. C-25 pass condition met. | 2 | 2 | 2 | 2 |

**C-24 on V-02:** R8-V02's proto-field "Why Unexpected: what the signals implied instead" names signal-prediction contrast, not the prior belief or model contradicted. C-24 requires naming "which prior belief... it contradicted." Signal implication != prior belief. PARTIAL.

**C-24 on V-03:** Two-row table provides structural row for prior belief but no SEAL format-string check enforcing belief-statement content. Row label present; belief-content enforcement absent. "Label alone = PARTIAL."

**C-17 on V-02:** V-02 targets C-25 via three-slot bracket template. The bracket template structurally enforces "address [gap/echo] by [practice change] so that [measurable outcome]" -- converting C-17 from PARTIAL (prose components listed) to PASS (bracket-slot fill-in template). C-25 was already PASS; the three-slot template locks it structurally.

---

### Aspirational Totals

| | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | C-24 | C-25 | **Total** |
|-|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| V-01 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 1 | 0 | 2 | 2 | 2 | 2 | 2 | **28** |
| V-02 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 2 | 2 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | **28** |
| V-03 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | **27** |
| V-04 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 2 | 2 | 1 | 0 | 2 | 2 | 2 | 2 | 2 | **29** |
| V-05 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **34** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | **%** |
|-----------|-----------|-------------|--------------|-----------|-------|
| V-01 -- Echo-Belief (prose field) | 60 | 30 | 28 | **118** | 95.2% |
| V-02 -- Outcome-Slot (bracket template) | 60 | 30 | 28 | **118** | 95.2% |
| V-03 -- Echo-Belief (two-row table) | 60 | 30 | 27 | **117** | 94.4% |
| V-04 -- Combined (C-24 + C-25) | 60 | 30 | 29 | **119** | 96.0% |
| V-05 -- Full Integration | 60 | 30 | 34 | **124** | 100.0% |

---

## Ranking

**1. V-05 -- Full Integration (124/124, 100.0%)**
First variation to achieve the full 124-pt ceiling. Over V-04, resolves three remaining deficits: C-13 (PASS via inertia framing with assumption-before-outcome logic), C-20 (PASS via dedicated "Assumption held without evidence" column in gap table), and C-19 (PASS via self-containment extended to phases 7-8). C-13 and C-20 have been FAIL across every round since R6. The gap-inertia column separation is the structural change that finally resolves the persistent "Why Absent = structural reason" failure. V-05 rebuilds the gap phase from R7-V05's structural approach rather than inheriting R8-V02's prose gap format.

**2. V-04 -- Combined (119/124, 96.0%)**
Best of the session-contained variations. Combines V-01's C-24 mechanism (labeled "Why unexpected" field with belief-content SEAL guard) and V-02's C-17/C-25 mechanism (bracket-slot recommendation template). Captures both new criteria at PASS. Fails only on the three gap-phase criteria (C-13, C-19, C-20) that require phase rebuilding.

**3. V-01 -- Echo-Belief, prose field (118/124, 95.2%)**
Labeled prose field with explicit SEAL belief-content enforcement achieves C-24 PASS. Phase 1 LOCK explicitly names all three outputs (Echo, Pattern, Why unexpected). SEAL format string "'> **Why unexpected**: [named prior belief or model contradicted]'" requires belief statement, not label restatement. C-17 PARTIAL: recommendation phase not modified; inherits R8-V02's component-list format.

**3. V-02 -- Outcome-Slot (118/124, 95.2%)**
Converts C-17 to PASS via bracket-slot recommendation template: "address [gap/echo] by [practice change] so that [measurable outcome]." Structurally enforces all three slots. C-24 PARTIAL: the proto-field from R8-V02 ("Why Unexpected: what signals implied instead") names signal-prediction contrast, not the prior belief -- does not satisfy C-24's "named prior model or assumption contradicted" requirement.

**5. V-03 -- Echo-Belief, two-row table (117/124, 94.4%)**
Two-row table provides structural row for prior belief but weaker enforcement than V-01's labeled prose field. Without a SEAL format-string check requiring belief-statement content, the row satisfies C-24's "label alone = PARTIAL" verdict. C-17 PARTIAL: recommendation phase unchanged.

---

## Persistent Failures (V-01 through V-04)

| Criterion | Rounds Failed | Pattern |
|-----------|--------------|---------|
| C-13 Inertia Framing | R6, R7, R8, R9 (V-01-V-04) | Gap entries name structural reasons ("no owner," "skipped") or outcome implications ("would have surfaced X"). The assumption held without evidence -- the inertia belief that made the gap invisible -- is never named. Single-axis variations that inherit R8-V02's gap phase cannot resolve this without replacing the gap phase design. |
| C-20 Gap Inertia Assumption Named | R6, R7, R8, R9 (V-01-V-04) | No variation except V-05 adds a dedicated structural column for the assumption. Assumption and outcome are either merged or absent. Structural separation requires a phase rewrite, not a patch. |

Both criteria resolved only by V-05's full R7-V05 integration, which rebuilds the gap phase with a dedicated "Assumption held without evidence" column distinct from the "Would have surfaced" outcome column.

---

## Excellence Signals from V-05 (Top Scorer)

**Signal 1 -- `gap-inertia-column-isolation`**
V-05 resolves the Round 6-9 persistent FAIL on C-13 and C-20 by structurally separating the inertia assumption from the outcome in the gap table. The key insight: "Why Absent" and "Assumption Held Without Evidence" are different statements answering different questions. "Why absent" = structural reason (no process, skipped, out of scope). "Assumption held without evidence" = the belief that made the absence invisible before commitment. These belong in separate columns; merging them produces the recurring failure. V-05's gap table has both columns, required and distinct. This pattern resolves the deepest unresolved failure across all rounds.

**Signal 2 -- `phase-8-self-containment-extended`**
V-05 extends the per-phase SEAL and self-containment guarantee to phases 7 and 8 (Gaps and Recommendation). V-01 through V-04 left these phases unprotected (C-19 PARTIAL). V-05 -- via full R7-V05 integration -- applies tabular or SEAL-gated structure to every phase, eliminating the truncation risk C-19 captures. The pattern: self-containment must be a whole-prompt invariant, not phases 1-6 only.

---

## Scorecard Summary

| | V-01 | V-02 | V-03 | V-04 | **V-05** |
|--|------|------|------|------|----------|
| Score | 118/124 | 118/124 | 117/124 | 119/124 | **124/124** |
| % | 95.2% | 95.2% | 94.4% | 96.0% | **100.0%** |
| All essential | YES | YES | YES | YES | **YES** |
| C-13 inertia | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-20 assumption col | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-24 why-unexpected | PASS | PARTIAL | PARTIAL | PASS | **PASS** |
| C-25 outcome-measurable | PASS | PASS | PASS | PASS | **PASS** |
| Top | -- | -- | -- | -- | **check** |

```json
{"top_score": 124, "all_essential_pass": true, "new_patterns": ["gap-inertia-column-isolation", "phase-8-self-containment-extended"]}
```
