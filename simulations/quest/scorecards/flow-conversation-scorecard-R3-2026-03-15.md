## flow-conversation Round 3 Scoring — Rubric v3

---

### Variation-by-Variation Scoring

---

#### V-01 — Inertia Framing

**Mechanism:** Global status-quo foil opens the prompt; every section begins with "A first-pass X would say..." naming the inadequate pattern, then positions the simulation as the alternative.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Section 2 requires turn-by-turn trace with active topic node, user intent + utterance, exact agent response, redirect target, session variable delta. Terminal state required explicitly. |
| C-02 Defect report present | PASS | Section 4 requires all four defect types, each with "Found: [specific]" or "Not found: checked [specific nodes]." "A single combined 'no issues' statement is the inadequate pattern this simulation exists to replace." |
| C-03 Intent-response pairing | PASS | Five-item turn structure requires both user intent label + utterance AND exact agent response or action text in every turn. |
| C-04 Fallback handling shown | PASS | Section 1 flags missing fallback nodes. Section 3 traces exception path. Section 4 covers missing fallback as defect type. |
| C-05 Session state tracked | PASS | Turn structure item 5: "Any session variable set or read at this turn (variable name and value)." Named variable with value required per turn. |
| C-06 Multi-path coverage | PASS | Sections 2 and 3 are separate. Section 3 requires: "Diverges from happy path at [topic node], condition: [what triggers the branch]." Must reach a different terminal state. |
| C-07 Topic graph completeness | PASS | Section 1 inventory (per-node name, trigger phrases, no-match status, reachability) + Section 6 coverage map with traced/untraced/unreachable labels. |
| C-08 CS vocabulary | PASS | Role priming names: topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), entities (closed list, regex, system), condition branches, redirect nodes, session variables. Used throughout section instructions. |
| C-09 Actionable remediation | PASS | Section 5: names topic node by name, specifies "which branch to add, which trigger phrase to remove, which redirect to wire." Example: "In topic Order Status, add a condition branch on `no-match` that redirects to the Fallback system topic." |
| C-10 Named failure-mode prohibition | PASS | Opening names two bad forms by instance. Every section names its inadequate output: "A first-pass inventory would say: 'The agent covers Order Status, Account Management, and Escalation.'"; "The status-quo defect report says: 'No significant issues found. Consider adding error handling.'"; "'Add better error handling to affected topics'"; "'Most main topics were covered in the trace.'" Seven named bad forms total. |
| C-11 Structural domain-vocab enforcement | **FAIL** | Turn structure is a prose numbered list, not a table. No output tables defined in V-01. No CS-specific column headers enforce vocabulary by schema. Role priming + named prohibitions only — neither satisfies C-11's structural pass condition. |
| C-12 Phase exit conditions | **FAIL** | Numbered sections, not phases with gated exit conditions. Inline constraints ("The trace MUST end at a named terminal state") are phrased within sections, not as hard MAY NOT gates blocking phase advancement. Zero dedicated exit-condition blocks. |

**V-01 Score: 105/115**
(C-01 through C-10 all PASS: 60+30+5+5+5 = 105. C-11 FAIL, C-12 FAIL.)

**Prediction delta:** Predicted 110, actual 105. The variation map overestimated by 5 pts. C-11 was correctly predicted as FAIL, but that FAIL costs 5 pts against a baseline of 110 that assumed only C-10 contributes above the 100-pt floor — the map miscounted the baseline.

---

#### V-02 — Scoring Register (Criteria-First)

**Mechanism:** Nine-criterion evaluation table with "Full credit" and "Zero points" columns appears before any task instruction. Zero-point examples are named as bad forms. Output tables use CS-specific column headers.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Section 2 table with final-row terminal-state requirement. Criteria table: zero points for "trace ending on active topic node." |
| C-02 Defect report present | PASS | Section 4 table with four required rows. Criteria table: zero points for "'No significant issues found' as single statement; omitting any type; using 'possible' or 'unclear'." "Possible and unclear are not valid verdicts." |
| C-03 Intent-response pairing | PASS | Criteria table C-03: zero points for any turn showing only one side. Table columns include both "Trigger Phrase / User Utterance" and "Agent Response (Message Node Text)." |
| C-04 Fallback handling shown | PASS | Section 1 flags missing fallback. Section 3 exception path. Section 4 missing fallback row. Criteria table C-04 explicit. |
| C-05 Session state tracked | PASS | "Session Variable Delta" column in trace table. Criteria table C-05: zero points for "'Session variables are managed as needed' — no specific names or values." |
| C-06 Multi-path coverage | PASS | Sections 2 and 3 separate. Section 3: "Must reach a different terminal state than Section 2, or branch at a different topic node under a different condition. See C-06 in the scoring table." |
| C-07 Topic graph completeness | PASS | Section 1 inventory + Section 6 coverage table requiring every Section 1 node. Criteria table C-07 explicit. |
| C-08 CS vocabulary | PASS | Full CS role priming. Output tables use "Topic Node (Copilot Studio)," "Redirect Target / System Topic," "Copilot Studio Object to Edit." |
| C-09 Actionable remediation | PASS | Section 5 table with "Exact Change Required" and "Copilot Studio Object to Edit" columns. Criteria table: "'Add better error handling' — zero points on this criterion." |
| C-10 Named failure-mode prohibition | PASS | Criteria table names degenerate output by instance for every criterion: "A list of topic names with no turn-by-turn trace," "'No significant issues found' as a single statement," "'Session variables are managed as needed,'" "'Add better error handling,'" "'The conversation covers several topics.'" Temporal framing: these are positioned as what earned zero points, not merely prohibited. |
| C-11 Structural domain-vocab enforcement | PASS | Trace tables define "Topic Node (Copilot Studio)," "Trigger Phrase / User Utterance," "Agent Response (Message Node Text)," "Redirect Target / System Topic," "Session Variable Delta." Defect table: "Topic Node (Copilot Studio)." Remediation table: "Copilot Studio Object to Edit." Vocabulary enforced by column schema, not role priming alone. |
| C-12 Phase exit conditions | **FAIL** | Numbered sections 1–6, not phases with dedicated exit conditions. Section instructions say "See C-06 in the scoring table" — this is a criterion reference, not a phase exit gate. No MAY NOT blocks. |

**V-02 Score: 110/115**
(C-01–C-11 PASS: 60+30+5+5+5+5 = 110. C-12 FAIL.)

**Prediction match:** 110/115 as predicted. ✓

**Key finding:** Scoring register achieves C-10 and C-11 simultaneously via a single mechanism (the criteria table). No R2 single-axis variation achieved two aspirational criteria; V-02 does. This is the primary R3 discovery.

---

#### V-03 — Minimalist Compression

**Mechanism:** R2 V-05's three mechanisms compressed to ~40% word count. Five phases with explicit MAY NOT exit conditions. CS column headers throughout. Named prohibitions embedded in exit conditions.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Phase 2 exit: "MAY NOT end the trace on an active topic node — final row must name a terminal state." Table with CS headers. |
| C-02 Defect report present | PASS | Phase 4 exit: "MAY NOT produce fewer than four verdict rows, one per defect type. MAY NOT write a combined 'no issues found' statement in place of four individual verdicts. MAY NOT use 'possible' or 'unclear' as verdicts." |
| C-03 Intent-response pairing | PASS | Phase 2 exit: "MAY NOT write 'Agent responds appropriately' or leave the Agent Response column as a placeholder; actual message text required in every row." Table has both user and agent columns. |
| C-04 Fallback handling shown | PASS | Phase 3 exception trace; Phase 4 missing fallback row; Phase 5 coverage table. Phase 4 exit blocks "no issues found." |
| C-05 Session state tracked | PASS | "Session Variable Delta" column in Phase 2 and Phase 3 trace tables. Structural enforcement via column schema. |
| C-06 Multi-path coverage | PASS | Phase 3 exit: "MAY NOT trace the same path as Phase 2 with a different utterance and call it an exception path. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different set of nodes." |
| C-07 Topic graph completeness | PASS | Phase 1 exit: "MAY NOT replace the table with a summary statement — every topic node must appear as a named row." Phase 5: "every Phase 1 node gets a row" in coverage table. |
| C-08 CS vocabulary | PASS | Column headers: "Topic Node (Copilot Studio)," "Trigger Phrase / User Utterance," "Agent Response (Message Node Text)," "Redirect Target / System Topic," "Copilot Studio Object to Edit." Role priming present. |
| C-09 Actionable remediation | PASS | Phase 5 exit: "MAY NOT write 'Add better error handling' — name the Copilot Studio object to edit." Table has "Exact Change Required" and "Copilot Studio Object to Edit" columns. |
| C-10 Named failure-mode prohibition | PASS | Exit conditions embed named bad forms: "MAY NOT write 'Agent responds appropriately'," "MAY NOT write a combined 'no issues found' statement," "MAY NOT use 'possible' or 'unclear' as verdicts," "MAY NOT write 'Add better error handling'," "MAY NOT replace the table with a summary statement." Five named prohibitions. |
| C-11 Structural domain-vocab enforcement | PASS | CS-specific column headers appear across all five phases. "Copilot Studio Object to Edit" in remediation table; "Topic Node (Copilot Studio)" in all major tables. |
| C-12 Phase exit conditions | PASS | Every phase has explicit MAY NOT exit conditions naming specific blocked failures: Phase 1 (empty cells, summary substitution), Phase 2 (active-node terminal, placeholder response), Phase 3 (same-path rehash), Phase 4 (fewer than four rows, combined "no issues," "possible"/"unclear"), Phase 5 (generic remediation, omitted coverage nodes). Five phases, five sets of hard constraints. |

**V-03 Score: 115/115**
**Prediction match:** 115/115 as predicted. ✓

**Key finding:** Ceiling retained at ~40% word count. Confirms the mechanisms (MAY NOT constraints, CS column headers, named bad forms) are the enforcement work; the explanatory scaffolding around them in R2 V-05 was not load-bearing.

---

#### V-04 — Inertia Framing + Scoring Register

**Mechanism:** V-01's global opening frame + V-02's criteria table (compressed, 7 criteria). Numbered sections with inline named prohibitions at each section. CS column headers throughout.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Section 2 table with "Final row must show a named terminal state. See Dialog path traced criterion." |
| C-02 Defect report present | PASS | Section 4: four-row table required. "The inadequate form — 'No significant issues found. Consider improving fallback handling.' — earns zero points." |
| C-03 Intent-response pairing | PASS | "Trigger Phrase / User Utterance" and "Agent Response (Message Node Text)" columns. Section 2: "'Agent responds with the requested information' — earns zero points on Intent-response pairing." |
| C-04 Fallback handling shown | PASS | Section 1 flags missing fallbacks; Section 3 exception path; Section 4 covers missing fallback. |
| C-05 Session state tracked | PASS | "Session Variable Delta" column in Section 2 and 3 traces. Criteria table: zero points for "no names or values." |
| C-06 Multi-path coverage | PASS | Sections 2 and 3 separate. "Must reach a different terminal state or branch at a different decision point. See Multi-path coverage criterion." |
| C-07 Topic graph completeness | PASS | Section 1 inventory + Section 6 coverage table. Section 6: "'Most main topics were traced.' — earns zero points." |
| C-08 CS vocabulary | PASS | Full CS role priming + CS-specific column headers. |
| C-09 Actionable remediation | PASS | "Copilot Studio Object to Edit" column. "'Improve the fallback behavior for the affected topics.' — earns zero points." |
| C-10 Named failure-mode prohibition | PASS | Double-layer: inertia frame names two bad forms at opening + criteria table names zero-point instances per criterion + per-section inline prohibitions ("The inadequate form — [example] — earns zero points"). Strongest C-10 implementation across all five R3 variations. |
| C-11 Structural domain-vocab enforcement | PASS | CS column headers: "Topic Node (Copilot Studio)," "Agent Response (Message Node Text)," "Redirect Target / System Topic," "Session Variable Delta," "Copilot Studio Object to Edit." |
| C-12 Phase exit conditions | **FAIL** | Numbered sections, not phases. Inline "earns zero points" notes are criteria backreferences, not dedicated exit-condition gates. No MAY NOT blocks gating phase advancement. |

**V-04 Score: 110/115**
**Prediction match:** 110/115 as predicted. ✓

---

#### V-05 — Inertia Framing + Scoring Register + Minimalist Compression

**Mechanism:** V-01's compressed opening frame + V-02's criteria table (4 criteria, "Zero points if you write" column) + V-03's compressed phase exit conditions. All three mechanisms operating simultaneously.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Phase 2 exit: "MAY NOT end on an active topic node — final row must name a terminal state." Table with CS headers. Criteria table: zero points for "trace ending on active node." |
| C-02 Defect report present | PASS | Phase 4 exit: "MAY NOT produce fewer than four verdict rows. MAY NOT write 'No significant issues found.' MAY NOT use 'possible' or 'unclear'." Criteria table: zero points for single "no significant issues" statement. |
| C-03 Intent-response pairing | PASS | Phase 2 exit: "MAY NOT write 'Agent responds appropriately' or leave Agent Response blank; actual message text required." Both trace columns present. |
| C-04 Fallback handling shown | PASS | Phase 3 exception path; Phase 4 missing fallback row; Phase 5 coverage. |
| C-05 Session state tracked | PASS | "Session Variable Delta" column in Phase 2/3 tables. |
| C-06 Multi-path coverage | PASS | Phase 3 exit: "MAY NOT trace the same path as Phase 2 with a different utterance." Named divergence label required. Criteria table: zero points for "trace ending on active node" (covers collapse). |
| C-07 Topic graph completeness | PASS | Phase 1 exit: "MAY NOT replace the table with a summary statement." Phase 5: every Phase 1 node required. Criteria table: zero points for "'The agent covers several topics.'" |
| C-08 CS vocabulary | PASS | CS column headers throughout. Role priming: "Copilot Studio domain expert." |
| C-09 Actionable remediation | PASS | Phase 5 exit: "MAY NOT write 'Add better error handling'... name the topic node and exact CS object." Criteria table: zero points for same. |
| C-10 Named failure-mode prohibition | PASS | Three-layer named bad forms: (1) opening inertia frame names "topic list without trace" and "'No significant issues found'"; (2) criteria table names zero-point outputs per criterion; (3) phase exit conditions embed MAY NOT prohibitions. Phase 3 also names: "The inadequate form — 'User provides wrong input and the agent re-prompts' without naming the node or condition — earns zero points on Multi-path coverage." |
| C-11 Structural domain-vocab enforcement | PASS | CS column headers: "Topic Node (Copilot Studio)," "Trigger Phrase / User Utterance," "Agent Response (Message Node Text)," "Redirect Target / System Topic," "Session Variable Delta," "Copilot Studio Object to Edit." |
| C-12 Phase exit conditions | PASS | Five phases with hard MAY NOT exit conditions, same as V-03. Criteria table adds a sixth layer of blocking above the phase gates. |

**V-05 Score: 115/115**
**Prediction match:** 115/115 as predicted. ✓

---

### Round 3 Score Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | Score | Predicted |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|-------|-----------|
| V-01 Inertia | P | P | P | P | P | P | P | P | P | P | **F** | **F** | **105** | 110 |
| V-02 Scoring reg. | P | P | P | P | P | P | P | P | P | P | P | **F** | **110** | 110 |
| V-03 Minimalist | P | P | P | P | P | P | P | P | P | P | P | P | **115** | 115 |
| V-04 Inertia+Scoring | P | P | P | P | P | P | P | P | P | P | P | **F** | **110** | 110 |
| V-05 All three | P | P | P | P | P | P | P | P | P | P | P | P | **115** | 115 |

All variations pass all 4 essential criteria. All variations are golden (all essential PASS AND composite >= 80).

**Prediction accuracy:** 4/5 exact matches. V-01 missed by 5 pts — the variation map predicted 110 but V-01 scores 105 because inertia framing does not enforce C-11 (no table schema), making the C-11 FAIL cost 5 pts against a baseline the map had wrong.

---

### Ranking

1. **V-03 / V-05 (tied, 115/115)** — both hit the ceiling
2. **V-02 / V-04 (tied, 110/115)** — C-12 the only miss
3. **V-01 (105/115)** — C-11 and C-12 both fail

**Between V-03 and V-05:** V-03 is preferable for production (fewer tokens, same ceiling). V-05 adds robustness layers but does not raise the score. V-05 is the more fault-tolerant prompt if model attention wanders; V-03 is the more efficient one.

---

### Excellence Signals from Top-Scoring Variations

**From V-03 (Minimalist Compression — ceiling at ~40% word count):**
- The load-bearing enforcement is entirely in the MAY NOT exit condition lines. Everything else is scaffolding.
- Compressed form: "MAY NOT write 'Agent responds appropriately'" does the same work as three sentences of explanation in R2 V-05. Word count around the mechanism is not correlated with enforcement strength.
- Implication for production prompts: trim the setup, keep the MAY NOT lines verbatim.

**From V-02 (Scoring Register — dual criterion capture):**
- A criteria-first table that shows "Zero points if you write: [bad form]" achieves C-10 (named bad forms) and C-11 (CS column headers) with a single structural element. No R2 variation achieved two aspirational criteria with one mechanism.
- Temporal framing ("this earns zero points") and structural framing ("this is a column header") are different cognitive operations but both activate in V-02's criteria table. This is the first mechanism to close two escape routes simultaneously.

**From V-05 (Ceiling robustness):**
- Three-layer named bad-form coverage (opening frame → criteria table → phase exit conditions) means degenerate completion is blocked at three different processing stages: prompt-read, section-start, and phase-completion. No single escape route can survive all three.
- Compression survives framing overhead: adding V-01's opening frame and V-02's criteria table to V-03 does not lower the score. The mechanisms are non-interfering.

**Cross-variation finding (C-11 discriminator):**
- V-01 achieves C-10 via prose-level inertia framing but fails C-11. V-02 achieves both via table schema. This confirms the rubric's structural distinction: prose-level named bad forms satisfy C-10; only column-header schema satisfies C-11. These are genuinely different mechanisms requiring different implementation choices.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["Scoring-register criteria table achieves C-10 and C-11 simultaneously: zero-point examples satisfy C-10 while CS-specific column headers in the same table satisfy C-11 — first single mechanism to close two aspirational escape routes", "Inertia framing at the section level achieves C-10 via comparison-based prose priming but fails C-11 because prose-level negative examples do not enforce table column schema — confirms C-11 requires structural (column header) not rhetorical enforcement", "Minimalist compression confirms the ceiling is a property of the MAY NOT exit condition lines themselves; elaboration and setup paragraphs around those lines are scaffolding, not load-bearing enforcement"]}
```
