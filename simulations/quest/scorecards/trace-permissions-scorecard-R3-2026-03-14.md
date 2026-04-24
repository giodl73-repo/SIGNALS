## Round 3 Results — trace-permissions

**V-04 scores 125/125 (GOLDEN). V-01/V-02 score 120/125. V-03/V-05 score 115/125.**

The rubric v3 ceiling is 125. Only V-04 hits it.

### Score Table

| Variation | Score | C-13 | C-14 |
|-----------|-------|------|------|
| V-04 (H-flag + Phase Gates) | **125/125** GOLDEN | PASS | PASS |
| V-01 (H-flag only) | 120/125 | PASS | FAIL |
| V-02 (Phase Gates only) | 120/125 | FAIL | PASS |
| V-03 (CS-first ordering) | 115/125 | FAIL | FAIL |
| V-05 (Inertia framing) | 115/125 | FAIL | FAIL |

All variations pass C-01 through C-12.

### What determined the spread

**C-13 (5 pts):** Requires H-flag column as a table column spec in every evidence table, not just prose evidence references in findings. V-01 and V-04 pass. V-02/V-03/V-05 have row-citation requirements but no column-level enforcement — rubric says "hypothesis section connected to findings only by prose, with no table-level tracing, does not pass."

**C-14 (5 pts):** Requires "PHASE N COMPLETE" as an explicit output line before the next section begins. V-02 and V-04 pass. V-01/V-03/V-05 use section headers and `---` dividers — structurally invisible.

### Key finding

C-13 and C-14 are genuinely independent. V-01 proves C-13 without C-14; V-02 proves C-14 without C-13. V-03 and V-05 confirm that content quality (CS-first ordering, inertia framing) doesn't substitute for structural mechanism. The only path to 125 is V-04's dual-mechanism design.

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["Dual-layer structural enforcement: H-flag columns enforce hypothesis tracing at table-cell granularity while phase completion gates enforce sequencing at section-transition granularity — two independent mechanisms operating at different levels create a ceiling that neither mechanism achieves alone"]}
```
justification |
| C-06 Sharing Rule Conflict | PASS | Table E: Rule / Widens Baseline / Conflict / Description / H-flag; null result requires specific rules named |
| C-07 Team Membership Gap | PASS | Table F: Team / Scenario / Gap Type (Excess/Missing) / Access Impact / H-flag; "Include at least one row" |
| C-08 Risk-Ranked Summary | PASS | Table G includes Severity (H/M/L); Phase 4 risk-ranked list ordered High → Low with one-line justification per gap |
| C-09 Remediation Per Gap | PASS | Phase 4: "name the role, field, rule, or team, and state the specific action"; acceptable/not-acceptable examples |
| C-10 Hypothesis Pre-commitment | PASS | Phase 1: "Do not produce any evidence tables until all hypotheses are committed here"; H1/H2 required with gap type and role/operation; Hypothesis Resolution Table in Phase 4 |
| C-11 Null-Finding Accountability | PASS | Table D: "For every No: name specific controls + one-sentence null justification"; Table E: null result row with specific rules named; Table F: "Include at least one row" |
| C-12 Four-Vector Escalation Sweep | PASS | Table D pre-printed with all four vectors (Record Reassignment, Team Promotion, Sharing Rule Bypass, Impersonation/Delegation) |
| C-13 Hypothesis-Anchored Evidence Tables | PASS | H-flag column in every table (A through G); column spec enforced at table header level; Hypothesis Resolution requires "cite a specific table and row (e.g., Table B, Row 2 — AccountNumber, Customer Service, Read = Allow)" |
| C-14 Explicit Phase Completion Gate | FAIL | No "PHASE N COMPLETE" markers. Phases separated by section headers and "---" dividers. No required state transition assertion before next phase begins. |

Score: **120/125**

---

#### V-02: Lifecycle Emphasis — Phase Completion Gates

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | "For each security role, map: Create / Read / Update / Delete / Assign / Share"; table format required; values specified |
| C-02 FLS Named Per Role | PASS | "For each role, name every field where FLS differs from the table default. State field name, role, and access type." If no override: explicit statement required; "Absence of FLS configuration is itself a finding" |
| C-03 Record Access Scope | PASS | "For each role, state the access scope." "State each role's scope explicitly. Do not group roles unless scopes are identical and reason is documented." |
| C-04 Gap Identified | PASS | Phase 3 gap analysis sections require finding at least one conflict or gap per section type |
| C-05 Escalation Path | PASS | All four vectors listed in sequence; each requires named exploitation path or named controls with one-sentence null justification |
| C-06 Sharing Rule Conflict | PASS | Criteria-based, owner-based, manual sharing rules required; "Identify at least one case"; null: "name specific rules examined and explain why each is safe" |
| C-07 Team Membership Gap | PASS | "Identify at least one of: [missing access] or [combined permissions exceed intent]"; null: "name the teams and their membership configuration examined" |
| C-08 Risk-Ranked Summary | PASS | Phase 4: "ordered High → Medium → Low severity. For each gap: One-line risk justification" |
| C-09 Remediation Per Gap | PASS | Phase 4: "Concrete remediation: name the role, field, rule, or team, and state the exact action"; acceptable/not-acceptable examples |
| C-10 Hypothesis Pre-commitment | PASS | Phase 1 gate: "Write all hypotheses before the marker." "PHASE 1 COMPLETE" must appear before Phase 2 begins; Hypothesis Resolution in Phase 4 with cited specific evidence |
| C-11 Null-Finding Accountability | PASS | Each Phase 3 subsection: "If no [X] exists: name specific [items] examined and explain why each is safe"; "None found without naming what was checked does not satisfy this requirement" |
| C-12 Four-Vector Escalation Sweep | PASS | All four vectors named in sequence with explicit instructions per vector; prose-template format requires path or blocking controls per vector |
| C-13 Hypothesis-Anchored Evidence Tables | FAIL | No H-flag columns in tables. Hypothesis Resolution requires citing "table row, field name, rule name, or vector finding" — but row citations without H-flag columns is prose-level tracing, not table-level mechanical tracing. No column-spec in any table header forces hypothesis linkage. |
| C-14 Explicit Phase Completion Gate | PASS | "PHASE 1 COMPLETE — proceeding to Phase 2." / "PHASE 2 COMPLETE — proceeding to Phase 3." / "PHASE 3 COMPLETE — proceeding to Phase 4." / "PHASE 4 COMPLETE." required as output lines; "The marker is not a heading. It is a state transition assertion. The next phase does not begin until this line appears." |

Score: **120/125**

---

#### V-03: Role Sequence — CS-First, Least-Privilege Ascending

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | Per-role trace block covers all operations; Cross-Role Matrix consolidates into table |
| C-02 FLS Named Per Role | PASS | Per-role block: "Every field where this role's access differs from the table default. If none: 'No FLS exceptions'"; FLS Summary consolidates |
| C-03 Record Access Scope | PASS | Per-role block includes record scope; Record Scope Summary table; "State each role's scope explicitly" |
| C-04 Gap Identified | PASS | "Gaps observed" row in every role trace block; Phase 4 gap summary table required |
| C-05 Escalation Path | PASS | All four vectors in Phase 3, framed from CS perspective; each requires named path or specific controls with one-sentence justification |
| C-06 Sharing Rule Conflict | PASS | Sharing Rule Conflicts section; framed as "was this rule intended for CS users?"; null: "name rules examined and why safe" |
| C-07 Team Membership Gap | PASS | CS perspective: "Which teams should a CS user be on?"; both excess and missing gap types; null: name teams and explain |
| C-08 Risk-Ranked Summary | PASS | Phase 4: "ranked High → Medium → Low. For each gap: One-sentence risk justification" |
| C-09 Remediation Per Gap | PASS | Phase 4: "Specific remediation: name the role, field, rule, or team, and state the action"; acceptable/not-acceptable examples |
| C-10 Hypothesis Pre-commitment | PASS | "Do not proceed to Phase 2 until hypotheses are written"; H1/H2 required with gap type and role/operation; Hypothesis Resolution in Phase 4 |
| C-11 Null-Finding Accountability | PASS | Each Phase 3 subsection has null protocol: "If none: name [what] and explain why [it is safe]"; team gaps: "Name the teams examined, their membership rules, and explain why the combination is safe" |
| C-12 Four-Vector Escalation Sweep | PASS | All four vectors explicitly listed in Phase 3 with framing questions per vector; null requires naming specific controls |
| C-13 Hypothesis-Anchored Evidence Tables | FAIL | No H-flag columns in any table. Cross-Role Matrix, FLS Summary, Record Scope Summary have no H-flag column. Hypothesis resolution cites "role block, matrix row, FLS table row, or escalation vector" — prose reference, no table-level mechanical tracing. |
| C-14 Explicit Phase Completion Gate | FAIL | No "PHASE N COMPLETE" markers. Phases use "---" separators and section headers. No required state transition assertion. |

Score: **115/125**

---

#### V-04: Combined — H-flag Columns + Phase Completion Gates

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | Table 1: Create/Read/Update/Delete/Assign/Share + H-flag; "Fill every cell. If cannot be determined, write Unknown and note what is missing" |
| C-02 FLS Named Per Role | PASS | Table 2: Role / Field Name / Access / Default Override / H-flag; "Do not omit roles"; explicit no-exception placeholder row |
| C-03 Record Access Scope | PASS | Table 3: Role / Scope / Condition / H-flag; "One row per role. State the explicit scope assignment — do not infer from privilege level" |
| C-04 Gap Identified | PASS | Table 7 gap summary required; every gap from Tables 4, 5, 6 must appear; "Do not introduce gaps in Phase 4 that do not appear in this table" |
| C-05 Escalation Path | PASS | Table 4: pre-printed 4-row table + H-flag; "For every No: name specific controls and provide one-sentence null justification in column 3" |
| C-06 Sharing Rule Conflict | PASS | Table 5: Rule / Widens Baseline / Conflict / Description / H-flag; "include at least one row identifying a conflict or confirming null result with specific rules examined" |
| C-07 Team Membership Gap | PASS | Table 6: Team / Scenario / Gap Type / Access Impact / H-flag; "Include at least one row. If no gap exists, name teams examined and justify null result" |
| C-08 Risk-Ranked Summary | PASS | Phase 4: "Risk-Ranked Gap List (High → Medium → Low)"; one-line risk justification "given the operation and data" per gap |
| C-09 Remediation Per Gap | PASS | Phase 4: "Concrete remediation: name the role / field / rule / team + exact action"; acceptable/not-acceptable examples |
| C-10 Hypothesis Pre-commitment | PASS | "Do not produce any evidence tables until all hypotheses are written here"; "PHASE 1 COMPLETE — proceeding to Phase 2." gate enforces this structurally; Hypothesis Resolution Table in Phase 4 |
| C-11 Null-Finding Accountability | PASS | Table 4: "For every No: name specific controls + one-sentence null justification"; Tables 5/6: null result requires specific items named; "do not leave the table empty" |
| C-12 Four-Vector Escalation Sweep | PASS | Table 4 pre-printed with all four vectors; "For every No in column 2: name controls and provide null justification — do not write No without naming what was checked" |
| C-13 Hypothesis-Anchored Evidence Tables | PASS | "Requirement A — H-flag columns" stated upfront as global requirement. H-flag column in all 7 tables (Tables 1–7). Hypothesis Resolution Table requires "Evidence Reference must cite a specific table and row (e.g., 'Table 2, Row 3 — AccountNumber, Customer Service, Read = Allow')." Column-spec-level enforcement plus row-citation-level resolution. |
| C-14 Explicit Phase Completion Gate | PASS | "Requirement B — Phase completion gates" stated upfront. "PHASE 2 COMPLETE — proceeding to Phase 3." / "PHASE 3 COMPLETE — proceeding to Phase 4." / "PHASE 4 COMPLETE." required output lines. "The next phase does not begin until this line appears. Placing the marker before the section content is complete does not satisfy this requirement." |

Score: **125/125** GOLDEN

---

#### V-05: Phrasing Register + Inertia Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | Step 2: role-operation matrix with all six operations; "Every cell gets a value" |
| C-02 FLS Named Per Role | PASS | Step 3: FLS table per field with "What breaks if this access changes?"; no FLS exception = finding, not null; "Do not leave this table blank for any role" |
| C-03 Record Access Scope | PASS | Step 4: record scope table with "What breaks if scope narrows by one level?"; "State the explicit scope — do not infer from privilege level" |
| C-04 Gap Identified | PASS | Step 8 gap table collects all gaps from Steps 5/6/7; "List every gap found" |
| C-05 Escalation Path | PASS | Step 5: all four vectors with specific questions per vector; inertia framing surfaces change-induced paths; null requires naming what was checked |
| C-06 Sharing Rule Conflict | PASS | Step 6: all rule types; inertia question: "What happens when this sharing rule fires on a record a CS rep should not see?"; null: name rules and explain |
| C-07 Team Membership Gap | PASS | Step 7: both questions (missing access, excess combined permissions); null: name teams, membership rules, and explain |
| C-08 Risk-Ranked Summary | PASS | Step 8 table has Severity (H/M/L) column and "Why it matters at this severity" column |
| C-09 Remediation Per Gap | PASS | Step 8 "Fix: do exactly this" column with explicit examples; "'Tighten security on sensitive fields' is not a fix" |
| C-10 Hypothesis Pre-commitment | PASS | Step 1: "Do this before Step 2. Hypotheses written after seeing the evidence are not hypotheses — they are summaries. The value is the pre-commitment."; Step 9 resolves with cited specific evidence |
| C-11 Null-Finding Accountability | PASS | Steps 5/6/7 each have null accountability: "'None found' with no evidence does not close the vector"; "name what you checked and say in one sentence why it is blocked"; Step 7: "name the teams examined, their membership rules, and explain why the combination is safe" |
| C-12 Four-Vector Escalation Sweep | PASS | Step 5: all four vectors with specific probing questions per vector; prose format requires path or controls for each |
| C-13 Hypothesis-Anchored Evidence Tables | FAIL | No H-flag columns. Tables have inertia columns ("What breaks if...?") instead. Step 9 resolves hypotheses by referencing "specific row, table, or vector finding" — prose-level citation, no column-spec enforcement. No mechanism guarantees cell-to-hypothesis linkage in any table. |
| C-14 Explicit Phase Completion Gate | FAIL | No phase completion markers. Step format has no "STEP N COMPLETE" or equivalent. Step 9 resolution is the final step but no gate assertion precedes it. No structurally visible state transition. |

Score: **115/125**

---

### Variation Ranking

| Rank | Variation | Score | C-13 | C-14 | Notes |
|------|-----------|-------|------|------|-------|
| 1 | V-04 | 125/125 | PASS | PASS | Dual-mechanism: H-flag + phase gates together |
| 2 (tie) | V-01 | 120/125 | PASS | FAIL | H-flag enforced; no phase gate |
| 2 (tie) | V-02 | 120/125 | FAIL | PASS | Phase gate enforced; no H-flag |
| 4 (tie) | V-03 | 115/125 | FAIL | FAIL | CS-first ordering; no structural guarantee for C-13/C-14 |
| 4 (tie) | V-05 | 115/125 | FAIL | FAIL | Inertia framing improves content; no structural guarantee for C-13/C-14 |

---

### Excellence Signals

**Signal 1 — Dual-layer structural enforcement (V-04)**
H-flag columns operate at table-cell granularity; phase completion gates operate at section-transition granularity. These are independent mechanisms targeting different failure modes: a model can produce all required sections in wrong order (C-14 fails), or produce sections in correct order but fail to tie evidence cells to hypotheses (C-13 fails). Combining both creates a cross-granularity guarantee — the only path to 125/125. Neither mechanism can compensate for the other's absence.

**Signal 2 — C-13 and C-14 are genuinely independent criteria**
V-01 proves C-13 is achievable without C-14. V-02 proves C-14 is achievable without C-13. V-03 and V-05 prove neither is satisfied by content quality alone (CS-first ordering and inertia framing both score 115 regardless of how well-structured their evidence is). The two criteria require two structurally distinct prompt mechanisms; no single-axis design can satisfy both.

**Signal 3 — Inertia framing (V-05) improves content but not structural guarantees**
The "what breaks if this changes?" framing in V-05 produces richer escalation paths and more specific null accounting than a static-snapshot frame. But it does not create any mechanism for C-13 or C-14. Inertia framing is a content-quality enhancer, not a structural guarantee tool. It could be layered onto V-04 without conflict — adding "What breaks if this changes?" columns alongside H-flag columns would improve content within the same structural framework. Not a new structural pattern, but a candidate content enhancement for the production skill.

---

### R3 Key Findings

**Design question answered:** The rubric v3 ceiling is only reachable by combining both new mechanisms. Single-axis variations (V-01, V-02) confirm that each mechanism individually contributes 5 pts but that only their combination hits the ceiling. V-03 and V-05 confirm that content framing (role-sequence ordering, inertia questions) does not substitute for structural mechanism.

**V-04 as production target confirmed:** Phase gate (C-14) + H-flag columns (C-13) + null-accountability blocks (C-11) + pre-printed four-vector table (C-12), without V-05's redundant "what breaks?" columns. V-04 is the minimum-overhead path to 125/125.

**Rubric discriminating power restored:** R2 ended with all variations at 115/115 and no numeric separation. R3 achieves a 10-point spread (125 vs 115) and a clear ranking. C-13 and C-14 are earning their presence in the rubric.

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["Dual-layer structural enforcement: H-flag columns enforce hypothesis tracing at table-cell granularity while phase completion gates enforce sequencing at section-transition granularity — two independent mechanisms operating at different levels create a ceiling that neither mechanism achieves alone"]}
```
