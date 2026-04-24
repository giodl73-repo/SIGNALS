Now I have the complete rubric context. Let me score all five variations.

---

## Quest Score — topic-retro (Round 6, Rubric v4)

**Total available**: 112 (C-10 non-applicable for non-AMEND runs → effective denominator = 110)
**Rubric version**: v4 — adds C-18 (echo-systemic-pattern-named) and C-19 (phase-completion-self-contained), 2 pts each

---

## Scoring Key

| Tier | Criteria | Points Each | Total |
|------|----------|-------------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-19 | 2 | 22 |
| **Total** | | | **112** |

PARTIAL on essential = FAIL for "All essential: YES".
PARTIAL on recommended or aspirational = 1 pt.
C-10 non-applicable when no AMEND topic (excluded from denominator).

---

## V-01 — Pattern-Taxonomy

### Essential (60 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Signal Accuracy Section Present | **PASS** | Phase 3 PREDICTED VS ACTUAL table requires Namespace + Predicted + Actual + Match column per row. |
| C-02 Correct/Wrong Verdict Per Signal | **PASS** | Match column constrained to "C / P / W / ND" — column enforcement, no prose escape. |
| C-03 Gaps Section Present and Actionable | **PASS** | Phase 7 gap table requires "Would have surfaced" and "Changed commit? YES / NO" per row. |
| C-04 Echo Present (One Unexpected Finding) | **PASS** | Phase 1: four-step elimination procedure, "select exactly one," explicit "not a wrong prediction" framing. |
| C-05 Topic and Commitment Context | **PASS** | Topic stated via $ARGUMENTS header; "A feature has shipped" establishes commitment context in intro. |

**Essential: 60 / 60**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 Signal Coverage Summary | **PASS** | Phase 2 ends with "Namespaces with signals: [list] / Empty namespaces (from: scout…topic): [list] / Total: N signals across M namespaces." All 9 namespaces accounted. |
| C-07 Recommendation Tied to Gaps/Echo | **PASS** | Phase 9 template: "> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change]." |
| C-08 Accuracy Rate or Ratio Stated | **PASS** | Phase 4 scoring table with formula (C×100 + P×50) ÷ (C+P+W) and TOTAL row. Phase 6 verdict "[TOTAL score]/100." |

**Recommended: 30 / 30**

### Aspirational (22 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 Echo Linked to Systemic Pattern | **PASS** | Pattern taxonomy embedded in Phase 1; pattern linked to Echo. (2/2) |
| C-10 AMEND Handled Correctly | **PARTIAL** | `{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only.{{/if}}` — scope declared but no per-table out-of-scope notation. (1/2) |
| C-11 Systemic Pattern Echo Field | **PASS** | Phase 1 table has labeled column "Pattern: [name] — [recurring failure mode description]." Named structural field. (2/2) |
| C-12 Three-Way Wrong/Gap/Echo Isolation | **PASS** | Echo locked in Phase 1 table, wrong verdicts in Phase 3 match column, gaps in Phase 7 — distinct structural sections. (2/2) |
| C-13 Inertia Framing for Gaps | **FAIL** | Phase 7 gap table has no assumption/inertia column. "Would have surfaced" names outcomes, not the assumption held without evidence. (0/2) |
| C-14 Verdict Label Explicit Not Prose | **PASS** | Phase 3 Match column with enumerated values "C / P / W / ND." Table column cannot drift to prose. (2/2) |
| C-15 Accuracy Ratio Not Count | **PARTIAL** | Phase 4 weighted formula score; Phase 6 "[TOTAL score]/100." Weighted ratio but not the explicit N/M=X% count format. (1/2) |
| C-16 Namespace Coverage Table Not Implied | **PARTIAL** | Phase 2 coverage uses text list form ("Namespaces with signals: [list]"), not a 9-row status table. (1/2) |
| C-17 Recommendation Addresses Template | **PASS** | Phase 9 exact template with bracket slots enforced. (2/2) |
| C-18 echo-systemic-pattern-named | **PASS** | Phase 1 Pattern column with taxonomy + format "[name] — [recurring failure mode description]" + "not blank, not a restatement" constraint; propagates to Phase 9. Primary target of this variation. (2/2) |
| C-19 phase-completion-self-contained | **PARTIAL** | Table-row structure makes populated rows self-contained but no per-phase seal. Non-tabular phases (6, 8) can silently truncate. (1/2) |

**Aspirational: 16 / 22**

### **V-01 Total: 106 / 112 (94.6%)**

---

## V-02 — Phase-Seal

### Essential (60 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Signal Accuracy Section Present | **PASS** | Phase 3 table requires Namespace + Predicted + Actual + verdict per row; Phase 3 SEAL confirms no blank cells. |
| C-02 Correct/Wrong Verdict Per Signal | **PASS** | Phase 3 verdict column "C / P / W / ND"; SEAL confirms "every row has a verdict label." |
| C-03 Gaps Section Present and Actionable | **PASS** | Phase 7 gap table + decision-impact "Changed commit?" column; Phase 7 SEAL confirms completion. |
| C-04 Echo Present (One Unexpected Finding) | **PASS** | Phase 1: four-step procedure + Phase 1 SEAL confirms "Echo cell: one sentence (or explicit 'No Echo' statement — not a restatement of a wrong prediction)." |
| C-05 Topic and Commitment Context | **PASS** | Topic via $ARGUMENTS; "A feature has shipped" in intro. |

**Essential: 60 / 60**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 Signal Coverage Summary | **PASS** | Phase 2 ends with namespaces-with-signals list + empty namespace list + total count; Phase 2 SEAL confirms all 9 accounted. |
| C-07 Recommendation Tied to Gaps/Echo | **PASS** | Phase 7 template: "> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change]." |
| C-08 Accuracy Rate or Ratio Stated | **PASS** | Phase 4 formula table + TOTAL row; Phase 6 verdict "[TOTAL score]/100 — [tier]." |

**Recommended: 30 / 30**

### Aspirational (22 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 Echo Linked to Systemic Pattern | **PASS** | Phase 1: "> **Pattern**: [name] — [description of recurring failure mode]" present immediately after Echo table. (2/2) |
| C-10 AMEND Handled Correctly | **PARTIAL** | AMEND scope declared but no per-table out-of-scope notation. (1/2) |
| C-11 Systemic Pattern Echo Field | **PASS** | Phase 1 has explicit labeled field "> **Pattern**: [name] — [description]" in the required format. (2/2) |
| C-12 Three-Way Wrong/Gap/Echo Isolation | **PASS** | Echo in Phase 1 (locked), wrong verdicts in Phase 3 columns, gaps in Phase 7 — phase-sealed separation. (2/2) |
| C-13 Inertia Framing for Gaps | **FAIL** | Phase 7 gap table has no assumption column. No inertia statement per gap entry. (0/2) |
| C-14 Verdict Label Explicit Not Prose | **PASS** | Phase 3 table column + Phase 3 SEAL confirming "every row has a verdict label (C / P / W / ND)." (2/2) |
| C-15 Accuracy Ratio Not Count | **PARTIAL** | Weighted formula + "[TOTAL score]/100" — not the N/M=X% count format. (1/2) |
| C-16 Namespace Coverage Table Not Implied | **PARTIAL** | Phase 2 text-list form confirmed by seal; not a 9-row status table. (1/2) |
| C-17 Recommendation Addresses Template | **PASS** | Phase 7 exact template with bracket slots. (2/2) |
| C-18 echo-systemic-pattern-named | **PASS** | Phase 1 SEAL requires "Pattern entry: uses > **Pattern**: [name] — [description] format (not blank, not generic)." Seal-enforced. (2/2) |
| C-19 phase-completion-self-contained | **PASS** | Every phase (1–9) ends with a named-field SEAL checklist. "A phase that cannot pass its own seal is incomplete: do not proceed until it passes." Structural enforcement at every phase boundary. (2/2) |

**Aspirational: 17 / 22**

### **V-02 Total: 107 / 112 (95.5%)**

---

## V-03 — Conversational + [REQUIRED] Markers

### Essential (60 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Signal Accuracy Section Present | **PASS** | Comparison section has table with "[REQUIRED — every row must have non-blank Predicted, Actual, and Match before continuing]." |
| C-02 Correct/Wrong Verdict Per Signal | **PASS** | Match column "[C / P / W / ND]" in table; [REQUIRED] on row level. |
| C-03 Gaps Section Present and Actionable | **PASS** | Gap table with "Would have surfaced" + "Changed commit?" enforced; "No generic skill names." |
| C-04 Echo Present (One Unexpected Finding) | **PASS** | "Echo: [REQUIRED — one sentence... Not a paraphrase of a wrong prediction.]" Conversational but structurally explicit. |
| C-05 Topic and Commitment Context | **PASS** | Topic via $ARGUMENTS; "A feature shipped" in intro. |

**Essential: 60 / 60**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 Signal Coverage Summary | **PASS** | "Namespaces with signals: [REQUIRED — list them] / Empty namespaces: [REQUIRED — list which of the 9…] / Total: [REQUIRED — N signals across M namespaces]." |
| C-07 Recommendation Tied to Gaps/Echo | **PASS** | "> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change]." Template present. |
| C-08 Accuracy Rate or Ratio Stated | **PASS** | "[REQUIRED — every namespace row and TOTAL row before continuing]" + verdict "Signal accuracy for [topic]: [TOTAL]/100." |

**Recommended: 30 / 30**

### Aspirational (22 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 Echo Linked to Systemic Pattern | **PASS** | "Pattern: [REQUIRED — use this format exactly: **Pattern**: [name] — [description of recurring failure mode...]" (2/2) |
| C-10 AMEND Handled Correctly | **PARTIAL** | Minimal: "Scope this retro to: {{amend}} only." No per-table scope notation. (1/2) |
| C-11 Systemic Pattern Echo Field | **PASS** | Labeled Pattern field with [REQUIRED] marker and exact format instruction. (2/2) |
| C-12 Three-Way Wrong/Gap/Echo Isolation | **PASS** | Conversational sections are separately headed: Echo entry, signal inventory, comparison, gaps — distinct headers with different framing rules. (2/2) |
| C-13 Inertia Framing for Gaps | **FAIL** | Gap table: "Gap (signal type) / Namespace / Skill to run / Would have surfaced / Changed commit?" — no assumption/inertia field. (0/2) |
| C-14 Verdict Label Explicit Not Prose | **PASS** | Match column "[C / P / W / ND]" in table — structural column, not prose-inferred even in conversational register. (2/2) |
| C-15 Accuracy Ratio Not Count | **PARTIAL** | Formula scoring table + "[TOTAL]/100" verdict — not N/M=X% count format. (1/2) |
| C-16 Namespace Coverage Table Not Implied | **PARTIAL** | [REQUIRED]-enforced text lists for coverage — explicit but not a 9-row status table. (1/2) |
| C-17 Recommendation Addresses Template | **PASS** | Exact template present with bracket slots. (2/2) |
| C-18 echo-systemic-pattern-named | **PASS** | Inline [REQUIRED] marker at Pattern field with format instruction and examples: "Name your own if none fit." (2/2) |
| C-19 phase-completion-self-contained | **PARTIAL** | "[REQUIRED] field must be populated in the section where it appears. A retro with blank [REQUIRED] fields is incomplete regardless of where truncation occurs." Inline markers reduce silent omission but don't create structural seal visibility — a model can skip [REQUIRED] markers without producing an empty checklist. (1/2) |

**Aspirational: 16 / 22**

### **V-03 Total: 106 / 112 (94.6%)**

---

## V-04 — Role+Pattern (5 Roles, Dedicated Pattern Classifier)

### Essential (60 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Signal Accuracy Section Present | **PASS** | Role 4 Step A: namespace comparison table with Predicted + Actual + Match per row. |
| C-02 Correct/Wrong Verdict Per Signal | **PASS** | "Match: C / P / W / ND" column; "A verdict without both sides is invalid." |
| C-03 Gaps Section Present and Actionable | **PASS** | Role 4 Step C gap table with "Would have surfaced" + "Changed commit? YES / NO." |
| C-04 Echo Present (One Unexpected Finding) | **PASS** | Role 2 Echo Finder: five-step procedure, "select the one with highest commit-decision impact," locked Echo Record before Role 3. |
| C-05 Topic and Commitment Context | **PASS** | Topic via $ARGUMENTS; commitment established in intro. |

**Essential: 60 / 60**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 Signal Coverage Summary | **PASS** | Role 1 Archivist: "Namespaces with artifacts: [list] / Namespaces with no artifacts (scout…topic): [list empty] / Total artifacts: N." |
| C-07 Recommendation Tied to Gaps/Echo | **PASS** | Role 4 Step C: "> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change]." |
| C-08 Accuracy Rate or Ratio Stated | **PASS** | Role 4 Step B formula table + TOTAL row + "Signal accuracy for [topic]: [total]/100 — [verdict]." |

**Recommended: 30 / 30**

### Aspirational (22 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 Echo Linked to Systemic Pattern | **PASS** | Role 3 Pattern Classifier: named taxonomy, locked Pattern Classification artifact. (2/2) |
| C-10 AMEND Handled Correctly | **PARTIAL** | "SCOPE: {{amend}} — all roles stay within this constraint." Declared but no per-table notation. (1/2) |
| C-11 Systemic Pattern Echo Field | **PASS** | Role 3 produces labeled "> **Pattern**: [name] — [description]" with EVIDENCE and DESIGN IMPLICATION sub-fields. Strongest labeling of any variation. (2/2) |
| C-12 Three-Way Wrong/Gap/Echo Isolation | **PASS** | Echo in Role 2 (locked), Pattern Classification in Role 3 (locked), accuracy + gaps in Role 4, conflict in Role 5 — role-boundary separation. (2/2) |
| C-13 Inertia Framing for Gaps | **FAIL** | Role 4 Step C gap table: same structure as V-01 — no assumption column. (0/2) |
| C-14 Verdict Label Explicit Not Prose | **PASS** | Role 4 Step A verdict column + "Both columns must be explicit. A verdict without both sides is invalid." (2/2) |
| C-15 Accuracy Ratio Not Count | **PARTIAL** | Weighted formula + accuracy verdict format. Not N/M=X%. (1/2) |
| C-16 Namespace Coverage Table Not Implied | **PARTIAL** | Role 1 uses text/list form for coverage; not a 9-row status table. (1/2) |
| C-17 Recommendation Addresses Template | **PASS** | Role 4 Step C exact template. (2/2) |
| C-18 echo-systemic-pattern-named | **PASS** | Dedicated Role 3 (Pattern Classifier) is structurally absent if skipped — a missing role block is visible as a gap in the output sequence. Taxonomy enforces naming. (2/2) |
| C-19 phase-completion-self-contained | **PARTIAL** | Role handoff protocol prevents inter-role deferral (Role 4 cannot start without Role 3's locked Pattern Classification), but within Role 4 (the most complex role), fields can still be deferred. No per-field seal within roles. (1/2) |

**Aspirational: 16 / 22**

### **V-04 Total: 106 / 112 (94.6%)**

---

## V-05 — Seal+Inertia (Phase Seals + Baseline Comparison)

### Essential (60 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Signal Accuracy Section Present | **PASS** | Phase 2 Step A table: Signal prediction + Baseline assumption + Actual outcome + Signal match + Baseline match per row. |
| C-02 Correct/Wrong Verdict Per Signal | **PASS** | "Signal match: C/P/W/ND" column; Phase 2 SEAL confirms "no Signal prediction, Baseline assumption, or Actual outcome cell is blank." |
| C-03 Gaps Section Present and Actionable | **PASS** | Phase 3 gap table with "Changed commit? YES/NO" per row; tier classification (Tier 1/2/3) adds decision-impact specificity. |
| C-04 Echo Present (One Unexpected Finding) | **PASS** | Phase 0: three-test elimination procedure + Phase 0 SEAL confirms "Echo: one sentence (or 'No Echo' statement)." |
| C-05 Topic and Commitment Context | **PASS** | Topic via $ARGUMENTS; "A feature has shipped. This retro is structured against a counterfactual" establishes commitment. |

**Essential: 60 / 60**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 Signal Coverage Summary | **PASS** | Phase 1 SEAL confirms "Empty namespace list accounts for all 9"; explicit lists of covered and empty namespaces. |
| C-07 Recommendation Tied to Gaps/Echo | **PASS** | Phase 3: "> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change]." |
| C-08 Accuracy Rate or Ratio Stated | **PASS** | Phase 2 Step C verdict: "Signal accuracy for [topic]: [signal total]/100 — [tier]. Baseline: [baseline total]/100. Net lift: Δ[lift]." |

**Recommended: 30 / 30**

### Aspirational (22 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 Echo Linked to Systemic Pattern | **PASS** | Phase 0: "> **Pattern**: [name] — [description of recurring failure mode]" immediately after Echo table. (2/2) |
| C-10 AMEND Handled Correctly | **PARTIAL** | "AMEND: {{amend}} — all phases stay within this constraint." Declared but no per-table out-of-scope notation. (1/2) |
| C-11 Systemic Pattern Echo Field | **PASS** | Phase 0 has labeled "> **Pattern**: [name] — [description]" field; Phase 0 SEAL confirms "Pattern entry: present in > **Pattern**: [name] — [description] format (not blank)." (2/2) |
| C-12 Three-Way Wrong/Gap/Echo Isolation | **PASS** | Echo in Phase 0 (Revision log column as conflict record), accuracy in Phase 2, gaps in Phase 3 — phase-sealed separation. (2/2) |
| C-13 Inertia Framing for Gaps | **PARTIAL** | Phase 1 Signal Inventory has "Baseline assumption (what team assumed without this signal)" column per signal. Phase 3 gap table has "Baseline missed? YES/NO" per row linking back to Phase 1 assumptions. Assumptions are on the record and referenced in Phase 3, though not explicitly repeated verbatim per gap entry. (1/2) |
| C-14 Verdict Label Explicit Not Prose | **PASS** | "Signal match: C/P/W/ND" table column; Phase 2 SEAL confirms completeness. (2/2) |
| C-15 Accuracy Ratio Not Count | **PARTIAL** | Weighted formula + "[signal total]/100" verdict — more sophisticated than N/M=X% but not the count-ratio format. (1/2) |
| C-16 Namespace Coverage Table Not Implied | **PARTIAL** | Phase 1 SEAL confirms all 9 namespaces accounted; text-list form not a 9-row status table. (1/2) |
| C-17 Recommendation Addresses Template | **PASS** | Phase 3 exact template with bracket slots. (2/2) |
| C-18 echo-systemic-pattern-named | **PASS** | Phase 0 SEAL requires "Pattern entry: present in > **Pattern**: [name] — [description] format (not blank)"; Phase 5 SEAL confirms "Pattern matches Phase 0 Pattern entry (same named category)." Dual-seal enforcement: entry required and propagation required. (2/2) |
| C-19 phase-completion-self-contained | **PASS** | Every phase (0–5) has a named-field SEAL checklist. "Each phase seal is a self-containedness contract — the phase cannot defer required fields to a later phase or continuation turn." Baseline columns add a second required output per accuracy row — two visibly blank cells if truncated. (2/2) |

**Aspirational: 18 / 22**

### **V-05 Total: 108 / 112 (96.4%)**

---

## Rankings

| Rank | Variation | Score | % | All Essential Pass |
|------|-----------|-------|---|--------------------|
| **1** | **V-05 Seal+Inertia** | **108/112** | **96.4%** | **Yes** |
| 2 | V-02 Phase-Seal | 107/112 | 95.5% | Yes |
| 3 | V-01 Pattern-Taxonomy | 106/112 | 94.6% | Yes |
| 3 | V-03 Conversational | 106/112 | 94.6% | Yes |
| 3 | V-04 Role+Pattern | 106/112 | 94.6% | Yes |

**Score range**: 106–108. Tight cluster — 2 points separate first from last.

---

## Detailed Score Comparison

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (E) | 12 | 12 | 12 | 12 | 12 |
| C-02 (E) | 12 | 12 | 12 | 12 | 12 |
| C-03 (E) | 12 | 12 | 12 | 12 | 12 |
| C-04 (E) | 12 | 12 | 12 | 12 | 12 |
| C-05 (E) | 12 | 12 | 12 | 12 | 12 |
| C-06 (R) | 10 | 10 | 10 | 10 | 10 |
| C-07 (R) | 10 | 10 | 10 | 10 | 10 |
| C-08 (R) | 10 | 10 | 10 | 10 | 10 |
| C-09 (A) | 2 | 2 | 2 | 2 | 2 |
| C-10 (A) | 1 | 1 | 1 | 1 | 1 |
| C-11 (A) | 2 | 2 | 2 | 2 | 2 |
| C-12 (A) | 2 | 2 | 2 | 2 | 2 |
| C-13 (A) | **0** | **0** | **0** | **0** | **1** |
| C-14 (A) | 2 | 2 | 2 | 2 | 2 |
| C-15 (A) | 1 | 1 | 1 | 1 | 1 |
| C-16 (A) | 1 | 1 | 1 | 1 | 1 |
| C-17 (A) | 2 | 2 | 2 | 2 | 2 |
| C-18 (A) | **2** | **2** | **2** | **2** | **2** |
| C-19 (A) | **1** | **2** | **1** | **1** | **2** |
| **Total** | **106** | **107** | **106** | **106** | **108** |

**Key differentiators:**
- C-18: All variations PASS — the new criterion is well-targeted across all axes
- C-19: V-02 and V-05 PASS (phase seals); V-01, V-03, V-04 PARTIAL — confirms hypothesis that seals outperform inline markers and role boundaries for self-containedness
- C-13: Only V-05 scores PARTIAL — the baseline assumption column in Phase 1 is the sole mechanism that approaches inertia framing

---

## Excellence Signals from V-05

**seal-beats-inline-marker-for-phase-completeness** — Phase seal checklists (V-02, V-05) earn C-19 PASS; inline [REQUIRED] markers (V-03) and table-row structure (V-01) earn only PARTIAL; role boundaries (V-04) earn PARTIAL. The seal mechanism's structural visibility as an *unchecked item* makes truncation observable at any phase boundary without requiring tabular content. This confirms the V-03 design hypothesis: structural enforcement outperforms inline markers.

**baseline-assumption-column-as-inertia-anchor** — V-05's Phase 1 Signal Inventory includes a "Baseline assumption (what team assumed without this signal)" column, and Phase 3 gap table includes "Baseline missed? YES/NO." Together these partially satisfy C-13 inertia framing — assumptions are on the record per signal and referenced per gap row, even if not explicitly re-stated verbatim in gap entries. This is the only mechanism in R6 that moves C-13 from FAIL to PARTIAL. Insight: capturing assumptions in the inventory phase (not just the gap phase) is the path to full C-13 compliance.

---

```json
{"top_score": 108, "all_essential_pass": true, "new_patterns": ["seal-beats-inline-marker-for-phase-completeness", "baseline-assumption-column-as-inertia-anchor"]}
```
