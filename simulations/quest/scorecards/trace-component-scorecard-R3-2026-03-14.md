## Round 3 Scorecard — trace-component

### Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Event Anchor (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-02 Tree Traversal (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-03 State Update Map (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-04 Re-render Inventory (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-05 Final UI State (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-06 Side Effects (10) | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-07 Issue Detection (10) | **PARTIAL 5** | **PARTIAL 5** | PASS 10 | PASS 10 | PASS 10 |
| C-08 Framework Vocab (10) | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-09 Fix Recs (2) | PASS 2 | PASS 2 | PASS 2 | PASS 2 | PASS 2 |
| C-10 Render Quant (2) | PASS 2 | PASS 2 | PASS 2 | PASS 2 | PASS 2 |
| C-11 Phase-Close Gates (2) | PASS 2 | PASS 2 | PASS 2 | PASS 2 | PASS 2 |
| C-12 Comparison Column (2) | FAIL 0 | FAIL 0 | FAIL 0 | PASS 2 | PASS 2 |
| C-13 Gate Family (2) | FAIL 0 | FAIL 0 | FAIL 0 | FAIL 0 | **PASS 2** |
| C-14 Column Header (2) | FAIL 0 | FAIL 0 | FAIL 0 | PASS 2 | PASS 2 |
| C-15 Do-Nothing Cost (2) | FAIL 0 | FAIL 0 | PASS 2 | PASS 2 | PASS 2 |
| **Total** | **91** | **91** | **98** | **102** | **104** |

### Ranking

| Rank | V | Score |
|------|---|-------|
| 1 | V-05 | 104 — ceiling |
| 2 | V-04 | 102 — misses C-13 only |
| 3 | V-03 | 98 — misses C-12, C-13, C-14 |
| 4 | V-01 = V-02 | 91 — misses C-07, C-12, C-13, C-14, C-15 |

### Key findings

**R3 baselines absorbed from R2:** C-08 (vocabulary) and C-11 (phase gates) now pass for all five variations. Both were discriminators in R2 — V-01 had no vocabulary list; V-02 was a wide-table template with no phases. R3 fixed both.

**C-07 discriminator:** V-01/V-02 stay partial — advisory FINDINGS sections with single-block escape. V-03/V-04/V-05 pass — mandatory FINDINGS tables with N/A-prohibited columns. The staged roles in V-01 add analytical depth but don't change the structural escape path.

**C-13 is the ceiling criterion:** V-04 scores 102 with every other criterion satisfied. The FINDINGS gate (naming "no impact" / "minor issue" / "low risk" as non-closers) is the single mechanism that separates V-04 from V-05.

**New patterns confirmed:**
1. Gate family completeness requires FINDINGS coverage — phase gates leave do-nothing cost failure strings unintercepted at the consolidation step
2. Triple structural lock (mandatory column + column-header instruction + per-row gate) is the complete pattern for mandatory column enforcement

```json
{"top_score": 104, "all_essential_pass": true, "new_patterns": ["Gate family completeness requires FINDINGS coverage — phase gates prevent generic escape strings during trace phases, but FINDINGS is where 'no impact' and 'low risk' survive unintercepted without a FINDINGS gate; a gate family that covers phases but not the closing consolidation section leaves the last enforcement gap open", "Triple structural lock for mandatory columns: mandatory column + column-header instruction + per-row exact-phrase gate are three independent mechanisms each catching what the others miss — column prevents omission, header embedding provides constraint at cell-write time, gate intercepts the specific strings a model produces when clearing the first two"]}
```
te changes in response to the action' does not close this phase. 'the store is modified' without naming the key or slice does not close this phase." Three exact-phrase intercepts. |
| V-02 | **PASS** | Step 3: Owner / Key / Old / New / Mechanism / Timing per mutation. "'State updates' doesn't pass. 'State changes in response to the action' doesn't pass. 'The store is modified' without naming the slice doesn't pass." Same three phrases in imperative register. [STEP 3 DONE]. |
| V-03 | **PASS** | Phase 3: same mutation fields. Gate: same three exact phrases. No role header. |
| V-04 | **PASS** | Phase 3 [Performance Engineer — handoff from Frontend Engineer]: same mutation fields + gate. Role transition explicitly named in header. |
| V-05 | **PASS** | Phase 3: same mutation fields. Gate: same three exact phrases. |

All PASS.

---

#### C-04 · Re-render Inventory (essential, 12 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | Phase 4 [Performance Engineer]: Component / Re-render cause / Count x verdict table. Gate: "'several components re-render' without naming them does not close this phase." Pre-printed row examples at three levels (justified / unnecessary / 0x). |
| V-02 | **PASS** | Step 4: same three-column table with pre-printed examples. "Rules for the Count x verdict cell" subsection. "'Several components re-render' without naming them doesn't pass." [STEP 4 DONE]. |
| V-03 | **PASS** | Phase 4: same three-column table + "Minimum one row." Gate: "'several components re-render' without naming them does not close this phase." |
| V-04 | **PASS** | Phase 4 [Performance Engineer]: four-column table (adds "What this adds vs. ad-hoc" column). Gate: "Writing 'several components re-render' without naming them does not close this phase." |
| V-05 | **PASS** | Phase 4: same four-column table as V-04. Gate: "Writing 'several components re-render' without naming them does not close this phase. Writing 'components re-render as expected' without naming them does not close this phase." |

All PASS.

---

#### C-05 · Final UI State (essential, 12 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | Phase 5 [A11y Specialist — handoff]: sync state + post-async success/error. Gate: "'UI updates accordingly' does not close this phase. 'the UI reflects the state changes' does not close this phase. 'success and error states are handled' without describing what the user sees does not close this phase." Three exact-phrase intercepts. |
| V-02 | **PASS** | Step 5: sync state + async success/error paths. "'UI updates accordingly' doesn't pass. 'The UI reflects the state changes' doesn't pass. 'Success and error states handled' without describing what the user sees doesn't pass." Same three phrases in imperative register. [STEP 5 DONE]. |
| V-03 | **PASS** | Phase 5: sync + async. Gate: "'UI updates accordingly' does not close this phase. 'the UI reflects the state changes' does not close this phase." |
| V-04 | **PASS** | Phase 5 [A11y Specialist — handoff]: same structure as V-01. Gate matches V-03. |
| V-05 | **PASS** | Phase 5: sync + async. Gate: "Writing 'UI updates accordingly' does not close this phase. Writing 'the UI reflects the state changes' does not close this phase. Writing 'success and error states are handled' without describing what the user sees does not close this phase." Three exact-phrase intercepts. |

All PASS.

---

#### C-06 · Side Effect Coverage (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | Phase 5: Type / Detail / Mechanism per effect. "If none: 'No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation triggered by this action.'" Silence structurally rejected. |
| V-02 | **PASS** | Step 5: Type / Detail / Mechanism. "If none: say it — 'No side effects — confirmed synchronous...' Silence doesn't pass." Imperative anti-silence enforcement. |
| V-03 | **PASS** | Phase 5: same structure. "If none: 'No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation.'" |
| V-04 | **PASS** | Phase 5 [A11y Specialist]: same structure. "If none: 'No side effects — confirmed synchronous.'" |
| V-05 | **PASS** | Phase 5: same structure. "No side effects — confirmed synchronous: no API calls, timers, subscriptions, or navigation." |

All PASS.

---

#### C-07 · Issue Detection (recommended, 10 pts)

Pass condition: At least one issue named with its component or state path. "May have performance issues" does not pass.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PARTIAL** | FINDINGS [A11y Specialist]: per-role checks for Phase 4 unnecessary re-renders, async without loading state, error path gaps, ARIA failures, unused vocabulary terms. Format requires specific Problem. Escape: "No issues across all five phases. Justification: [per-role summary — name why each role's check came back clean]." Single-statement clearance. No mandatory column forcing per-row engagement. Score: 5 pts. |
| V-02 | **PARTIAL** | FINDINGS: imperative checklist with 5 specific check types. Per-finding format requires specific Problem. Escape: "No issues across all five steps. Here's why each check came back clean: [per-step summary — name the specific check for each step, not just 'implementation looks correct']." Single-statement clearance with per-step justification required — stronger than V-01's advisory escape, but still clears in one block. No mandatory column. Score: 5 pts. |
| V-03 | **PASS** | FINDINGS: structured as a mandatory table. Problem column instruction: "Name the component and the exact issue. 'May have performance issues' does not pass — name the component, the cause, and the mechanism." Do-nothing cost is a mandatory N/A-prohibited column — forces explicit engagement with each issue. Table structure prevents vague single-statement escape. Score: 10 pts. |
| V-04 | **PASS** | FINDINGS [A11y Specialist]: mandatory table with Problem column ("specific — component + mechanism + cause, not 'may have issues'") and Do-nothing cost as mandatory N/A-prohibited column in header. Phase 4's "What this adds vs. ad-hoc" column feeds into FINDINGS with source citation required. Score: 10 pts. |
| V-05 | **PASS** | Phase 4 "What this adds vs. ad-hoc" column (N/A not allowed) + FINDINGS table with mandatory do-nothing cost column + FINDINGS gate naming weak strings. Strongest C-07 enforcement in R3 set. Score: 10 pts. |

**C-07 discriminator (R3):** V-03/V-04/V-05 pass via mandatory FINDINGS table with N/A-prohibited column(s). V-01/V-02 are partial — advisory FINDINGS sections that clear with a single block. The structural insight from R2 holds: mandatory column beats advisory section for issue specificity enforcement. Role assignment (V-01 staged roles) adds depth but does not change the structural escape path.

---

#### C-08 · Framework Vocabulary (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | Phase 0: vocabulary list required (3-5 terms, each defined in one clause). Threading mandate: "must appear in phases below." Framework Vocabulary Check section at end with per-term citation. Pre-declaration + mandate + post-check. (Upgrade from R2 V-01 PARTIAL — R3 V-01 added the vocabulary list and check section.) Score: 10 pts. |
| V-02 | **PASS** | Step 0: "Declare 3-5 framework-specific terms you'll use. These terms must show up in your trace below — if you don't use a term, the trace is incomplete." Threading mandate explicit. Score: 10 pts. |
| V-03 | **PASS** | Phase 0: "Framework vocabulary declared (3-5 terms that must appear in phases below):" with one-clause definitions. Threading mandate present. Score: 10 pts. |
| V-04 | **PASS** | Phase 0 vocabulary declaration + threading mandate + Framework Vocabulary Check section with per-term phase citation + correction sentence if term unused. Score: 10 pts. |
| V-05 | **PASS** | Phase 0 vocabulary declaration + threading mandate + Framework Vocabulary Check section at end. Score: 10 pts. |

All PASS in R3. R2 V-01's C-08 gap (no vocabulary list) has been corrected in R3 V-01.

---

#### C-09 · Fix Recommendations (aspirational, 2 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | FINDINGS Fix field: "One concrete, minimal fix — specific hook, attribute, or boundary. Not general advice." |
| V-02 | **PASS** | FINDINGS Fix: "one concrete fix — name the hook, boundary, or ARIA attribute." |
| V-03 | **PASS** | FINDINGS Fix column: "One concrete, minimal fix — name the specific hook, boundary, ARIA attribute, or API. 'Add error handling' does not pass — name the specific handler location or pattern." Exact anti-phrase named. |
| V-04 | **PASS** | FINDINGS Fix column: "concrete — hook, boundary, or ARIA attribute." |
| V-05 | **PASS** | FINDINGS Fix column: "concrete — hook, boundary, or ARIA attribute." |

All PASS. Uniform baseline.

---

#### C-10 · Render Quantification (aspirational, 2 pts)

Pass condition: At least one component has a numeric render annotation AND verdict co-located in the same table row or sentence.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | Phase 4 "Count x verdict" column with pre-printed examples. Gate: "Writing count in one place and verdict in a separate subsection does not close this phase — count x verdict must be in the same cell for every row." |
| V-02 | **PASS** | Step 4 "Count x verdict" column. "Rules for the Count x verdict cell" block. "Count and verdict in separate places doesn't pass — same cell, same writing act." |
| V-03 | **PASS** | Phase 4 count x verdict with "[Count x verdict must be in the same cell — count in one column and verdict in a separate subsection does not satisfy this table.]" Gate also catches separation. |
| V-04 | **PASS** | Phase 4 count x verdict column header contains the full requirement: "both in this cell, same writing act — count and verdict in separate columns or a subsection does not satisfy this column." Constraint embedded in the header cell. |
| V-05 | **PASS** | Phase 4 count x verdict column header: "[both pieces in this cell, same writing act — co-location required]". Gate: "Writing count in one column and verdict in a separate subsection does not close this phase." |

All PASS.

---

#### C-11 · Inline Phase-Close Gates (aspirational, 2 pts)

Pass condition: At least two phase boundaries carry an inline close condition naming the exact failure mode.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | Phase 0 gate (vocabulary/roles). Phase 1 gate: "'the button fires a click event' without naming the handler." Phase 2 gate: flat-list phrase. Phase 3 gate: three phrases. Phase 4 gate: "several components re-render." Phase 5 gate: three phrases. 6 phase boundaries, multiple exact phrases each. |
| V-02 | **PASS** | Steps 0-5 each carry [STEP N DONE] markers with inline exact-phrase enforcement throughout. "'An event fires' doesn't pass. 'The event handler' doesn't pass. 'State updates' doesn't pass. 'Several components re-render' doesn't pass. 'UI updates accordingly' doesn't pass." Sequential step structure allows gate placement. (Unlike R2 V-02 which was table-format with no phases.) |
| V-03 | **PASS** | Phases 1-5 all gated with exact phrases. Same baseline as R2 V-05. |
| V-04 | **PASS** | Phases 0-5, all gated. Phase 4 gate adds: "Leaving a 'What this adds vs. ad-hoc' cell blank or writing 'N/A' does not close this phase." Additional gate condition for the comparison column. |
| V-05 | **PASS** | Phases 0-5 all gated. Phase 4 gate adds N/A-prohibited condition. FINDINGS section also carries a gate (C-13). |

All PASS in R3. The R2 format-gating effect (table templates fail C-11) no longer applies — R3's table-adjacent variations (V-02, V-03) are sequential-phase based.

---

#### C-12 · Mandatory Comparison Column (aspirational, 2 pts)

Pass condition: At least one column prohibits N/A by instruction, has per-row entries, and demonstrates the escape pattern per-row.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **FAIL** | No comparison column. Phase 4 table has 3 columns: Component / Re-render cause / Count x verdict. FINDINGS is advisory. Score: 0 pts. |
| V-02 | **FAIL** | Step 4 table has 3 columns. No comparison column. No N/A-prohibited column in any table. Score: 0 pts. |
| V-03 | **FAIL** | Phase 4 table has 3 columns. Do-nothing cost is in FINDINGS, not a Phase 4 comparison column. Score: 0 pts. |
| V-04 | **PASS** | Phase 4: "What this adds vs. ad-hoc [N/A not allowed — fill every cell: write 'Invisible: [...]' OR 'Observable: [...]. Exception — [specific structural reason...]']" — instruction embedded in the column header cell. Per-row enforcement with escape pattern in pre-printed example rows. Score: 2 pts. |
| V-05 | **PASS** | Phase 4: same "What this adds vs. ad-hoc" column with instruction in header cell. Phase 4 GATE: "Leaving a 'What this adds vs. ad-hoc' cell blank or writing 'N/A' does not close this phase." Header instruction + gate. Score: 2 pts. |

V-04 and V-05 pass. V-01, V-02, V-03 fail — all three use 3-column Phase 4 tables.

---

#### C-13 · Exact-Phrase Gate Family (aspirational, 2 pts)

Pass condition: The gate family covers FINDINGS in addition to phases — exact failure strings for do-nothing cost are named as non-closers.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **FAIL** | Gates on Phases 1-5 only. No FINDINGS gate. Weak do-nothing cost strings can clear FINDINGS unchallenged. Score: 0 pts. |
| V-02 | **FAIL** | [STEP N DONE] gates on Steps 1-5 only. No FINDINGS gate. Score: 0 pts. |
| V-03 | **FAIL** | Phase gates on Phases 1-5 only. No FINDINGS gate. Column definition block provides escape clause guidance but does not name failure strings in gate format. Score: 0 pts. |
| V-04 | **FAIL** | Phase gates on Phases 0-5. No FINDINGS gate with exact failure phrases. Mandatory columns provide structural pressure but no gate names "no impact" / "minor issue" / "low risk" as non-closers. Score: 0 pts. |
| V-05 | **PASS** | "[FINDINGS GATE: Writing 'no impact' as a do-nothing cost does not close this section. Writing 'minor issue' as a do-nothing cost does not close this section. Writing 'low risk' as a do-nothing cost does not close this section. Writing 'no user-facing consequence' without naming why does not close this section. ... Mark: FINDINGS COMPLETE.]" Four exact failure strings named. Gate family now covers both trace phases and the closing consolidation section. Score: 2 pts. |

**C-13 is the single differentiator between V-04 (102) and V-05 (104).** All other aspirational criteria are identical between them. The FINDINGS gate closes the last gap in the gate family.

---

#### C-14 · Column-Header Escape Instruction (aspirational, 2 pts)

Pass condition: The escape instruction is embedded in the literal Markdown column header cell syntax — not in a preceding block or definition section.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **FAIL** | No comparison column. No column-header embedded instruction. Score: 0 pts. |
| V-02 | **FAIL** | No comparison column. Score: 0 pts. |
| V-03 | **FAIL** | Do-nothing cost escape instruction is in a "Column instructions:" block preceding the FINDINGS table header — not embedded in the column header cell itself. Encountered before table construction, not at header-write time. Score: 0 pts. |
| V-04 | **PASS** | Phase 4: "What this adds vs. ad-hoc [N/A not allowed — fill every cell: write 'Invisible: [...]' OR 'Observable: [...]. Exception — [specific structural reason...] Exception requires justification — not just asserting it.']" — full escape instruction is part of the header cell text. Also: "Count x verdict [both in this cell, same writing act — ...]" instruction in count x verdict header. FINDINGS "Do-nothing cost" column header also embeds N/A-not-allowed instruction. Score: 2 pts. |
| V-05 | **PASS** | Phase 4: same "What this adds vs. ad-hoc [N/A not allowed...]" header embedding. Count x verdict header also contains instruction. FINDINGS: "Do-nothing cost [N/A not allowed — fill every row; write 'Ships: [...]' OR 'Deferred: [...]. Exception — [...]']" — in header cell. Multiple columns, all with header-embedded instructions. Score: 2 pts. |

Key distinction between V-03 (FAIL) and V-04/V-05 (PASS): V-03 puts the instruction in a preceding `Column instructions:` block — the model encounters it before writing the table. V-04/V-05 put the instruction inside `| Column Name [...] |` — the model encounters it at the structural moment of writing the header row.

---

#### C-15 · Do-Nothing Cost (aspirational, 2 pts)

Pass condition: Do-nothing cost is a mandatory column with per-row enforcement — N/A-prohibited, not an advisory per-finding field.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **FAIL** | Do-nothing cost is an advisory per-finding field: "Do-nothing cost: [What ships to production without this fix...]" Not a mandatory column. No N/A-prohibited enforcement. Score: 0 pts. |
| V-02 | **FAIL** | Same advisory pattern: "Do-nothing cost: what ships to production if this finding is not addressed?" Per-finding field, not mandatory column. Score: 0 pts. |
| V-03 | **PASS** | FINDINGS table with "Do-nothing cost" as a mandatory column. Column instruction: "[N/A not allowed — fill every row. Write one of: (a) 'Ships: [specific user-visible consequence...]' (b) 'Deferred: [specific future engineering cost...]. Exception — [specific structural reason...]. Exception requires justification.'] A blank cell or 'N/A' fails this column." Mandatory, N/A-prohibited, with structured escape clause. Score: 2 pts. |
| V-04 | **PASS** | FINDINGS table: "Do-nothing cost [N/A not allowed — fill every row: write 'Ships: [...]' OR 'Deferred: [...]. Exception — [specific structural reason...]. Exception requires justification — not just asserting no consequence.]" embedded in column header. Score: 2 pts. |
| V-05 | **PASS** | FINDINGS table: same do-nothing cost column with N/A-not-allowed in header. FINDINGS gate also intercepts weak strings ("no impact" / "minor issue" / "low risk" do not close section). Column + gate = two independent enforcement mechanisms. Score: 2 pts. |

---

### Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Event Anchor (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-02 Tree Traversal (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-03 State Update Map (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-04 Re-render Inventory (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-05 Final UI State (12) | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-06 Side Effects (10) | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-07 Issue Detection (10) | PARTIAL 5 | PARTIAL 5 | **PASS 10** | **PASS 10** | **PASS 10** |
| C-08 Framework Vocab (10) | **PASS 10** | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-09 Fix Recs (2) | PASS 2 | PASS 2 | PASS 2 | PASS 2 | PASS 2 |
| C-10 Render Quant (2) | PASS 2 | PASS 2 | PASS 2 | PASS 2 | PASS 2 |
| C-11 Phase-Close Gates (2) | **PASS 2** | **PASS 2** | PASS 2 | PASS 2 | PASS 2 |
| C-12 Comparison Column (2) | FAIL 0 | FAIL 0 | FAIL 0 | **PASS 2** | **PASS 2** |
| C-13 Gate Family (2) | FAIL 0 | FAIL 0 | FAIL 0 | FAIL 0 | **PASS 2** |
| C-14 Column Header (2) | FAIL 0 | FAIL 0 | FAIL 0 | **PASS 2** | **PASS 2** |
| C-15 Do-Nothing Cost (2) | FAIL 0 | FAIL 0 | **PASS 2** | PASS 2 | PASS 2 |
| **Total** | **91** | **91** | **98** | **102** | **104** |
| All essential pass | YES | YES | YES | YES | YES |
| Result | PASS | PASS | PASS | PASS | **PASS (ceiling)** |

---

### Ranking

| Rank | V | Score | Key wins over prior rank | Key misses |
|------|---|-------|--------------------------|------------|
| 1 | **V-05** | **104** | C-13 (FINDINGS gate) | — |
| 2 | **V-04** | **102** | C-12, C-14, C-15 vs. V-03 | C-13 only |
| 3 | **V-03** | **98** | C-15 vs. V-01/V-02 | C-12, C-13, C-14 |
| 4 | **V-01** | **91** | staged roles (depth, not structural score) | C-07 partial, C-12, C-13, C-14, C-15 |
| 4 | **V-02** | **91** | imperative register (register test) | C-07 partial, C-12, C-13, C-14, C-15 |

---

### The Discriminators

**C-07 (Issue Detection) — the FINDINGS table threshold:**
V-03, V-04, V-05 all pass C-07 because their FINDINGS sections are structured as mandatory tables with N/A-prohibited columns. A mandatory column prevents section-level advisory clearance — every finding row must explicitly engage with issue specificity and production consequence. V-01 and V-02 remain partial because their FINDINGS sections are advisory: a single "No issues" block + justification clears the section without per-issue column enforcement. The role assignment in V-01 (staged A11y Specialist for FINDINGS) adds analytical depth but does not change the structural escape path — it's not a structural discriminator.

**C-08 (Framework Vocabulary) — all PASS in R3:**
R2's C-08 discriminator was V-01's absence of a vocabulary list. R3 V-01 adds the vocabulary declaration + threading mandate + Framework Vocabulary Check section. All five R3 variations now pass C-08. The discriminator has been absorbed into the R3 baseline.

**C-11 (Inline Phase-Close Gates) — all PASS in R3:**
R2's C-11 discriminator was format: table-format templates (V-02, V-04 in R2) had no phase boundaries. R3 V-02 is a sequential step-based template (not a wide table), so it passes C-11. All five R3 variations pass C-11. The R2 format-gating effect no longer applies.

**C-12 through C-15 — the new aspirational tier:**
The three new criteria form a structural progression. C-15 (mandatory do-nothing cost) is the entry point: V-03 achieves it without C-12 or C-14. C-14 (column-header embedding) requires a comparison column to embed in — adding C-14 gives C-12 + C-14 together (V-04). C-13 (FINDINGS gate) extends the gate family beyond phases to cover do-nothing cost failure strings — the single mechanism V-04 lacks. V-05 stacks all three on the R2 V-05 proven base.

**C-13 is the ceiling criterion:**
V-04 scores 102/104 with all other aspirational criteria satisfied. The only path from 102 to 104 is the FINDINGS gate. A phase gate family that covers Phases 1-5 but not FINDINGS leaves weak do-nothing cost strings ("no impact," "low risk") unintercepted at the consolidation step where findings are written.

---

### Excellence Signals from V-05

**Signal 1 — Gate family completeness requires FINDINGS coverage.**
V-04 has gates on Phases 0-5 and mandatory columns in Phase 4 and FINDINGS — but no gate that fires in FINDINGS. A model that writes "Do-nothing cost: no impact" in a FINDINGS row passes V-04's structural checks even though "no impact" is a canonical weak escape string. V-05's FINDINGS gate names four specific strings that do not close the section. The gate family is complete only when it covers the closing consolidation step, not just the trace phases.

**Signal 2 — Triple structural lock: mandatory column + column-header instruction + per-row gate.**
V-05's do-nothing cost column has three independent enforcement mechanisms: (1) mandatory N/A-prohibited column, (2) constraint embedded in the column header cell, (3) FINDINGS gate intercepts specific weak strings. Each catches what the others might miss: mandatory column prevents omission; header embedding ensures the constraint is visible at cell-write time; the gate names the specific strings a model is most likely to produce when clearing the first two mechanisms.

**Signal 3 — Column-header embedding (C-14) beats preceding-block instruction (V-03 pattern).**
V-03 puts the do-nothing cost escape instruction in a "Column instructions:" block before the FINDINGS table. This block is processed before table construction begins — at cell-fill time, the model must recall the constraint from preceding text. V-04/V-05 embed the instruction in the literal column header cell. The constraint is part of the Markdown syntax the model writes at table-construction time — encountered at write-time, not recalled from preamble.

---

```json
{"top_score": 104, "all_essential_pass": true, "new_patterns": ["Gate family completeness requires FINDINGS coverage — phase gates prevent generic escape strings during trace phases, but FINDINGS is where 'no impact' and 'low risk' survive unintercepted without a FINDINGS gate; a gate family that covers phases but not the closing consolidation section leaves the last enforcement gap open", "Triple structural lock for mandatory columns: mandatory column + column-header instruction + per-row exact-phrase gate are three independent mechanisms each catching what the others miss — column prevents omission, header embedding provides constraint at cell-write time, gate intercepts the specific strings a model produces when clearing the first two"]}
```
