## campaign-simulate — Round 2 Scorecard

**Ranking:**

| Variation | Score | All Essentials | Notes |
|-----------|-------|----------------|-------|
| V-05 (All Three Combined) | **100** | PASS | First perfect score — all 13 criteria |
| V-01 (Trace-First) | **95** | PASS | Wins essentials; no budget enforcement |
| V-03 (No-Blank-Cell) | **95** | PASS | Best format enforcement; flow-first kills C-11 + C-13 |
| V-04 (Trace-First + Budgets) | **93** | partial | Missing System Boundary column drops C-03 to PARTIAL |
| V-02 (Severity Budgets) | **91** | partial | Flow-first execution makes C-13 structurally impossible |

**Key discriminating failure in V-02 and V-04:** Neither includes a `System Boundary` column in the finding schema. The freeform schema `(F-ID, Sub-skill, Type, Spec location, Summary, Severity, Blast radius, Remediation)` leaves boundary inference to the model — that's the Round 2 C-03 gap V-05 closes by pre-assigning labels (`"state machine"` / `"contract surface"` / `"permission check"` / `"lifecycle phase"` / `"conversation state"`) directly in the prompt.

**V-05 excellence signals (5 new patterns):**
1. System boundary labels pre-assigned per sub-skill — mechanical transcription, not model judgment
2. Universal sentinel rule — "none not blank" extended from Trace Link to every column
3. No-findings sentinel rows — clean sub-skills still get a fully populated table row
4. Pre-output blank-cell verification gate — a named final step before writing the file
5. 10-column unified schema closes C-03/C-07/C-10/C-13 simultaneously — one table serves all five aspirational criteria

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["System boundary labels pre-assigned per sub-skill in prompt -- moves boundary labeling from model judgment to mechanical transcription, making C-03 failure require deliberate override", "Universal sentinel rule extends 'none not blank' from Trace Link to all optional columns, generalizing V-01's partial enforcement into a complete no-blank contract across every column", "No-findings sentinel rows: clean sub-skills still populate a full table row (Summary = No findings detected, all other cells filled), preventing execution log gaps and making absence of findings as explicit as presence", "Pre-output blank-cell verification gate as a named final step before writing the file, converting the no-blank contract from a style instruction into a checklist item", "Single 10-column schema closes C-03/C-07/C-10/C-13 simultaneously -- adding System Boundary column to the unified table makes all five aspirational criteria feed into one artifact rather than separate mechanisms"]}
```
 by blast radius, then severity within tier" |
| C-03 | PARTIAL 6 | Finding schema (`F-ID, Sub-skill, Type, Spec location, Summary, Severity, Blast radius, Remediation`) has Severity but no System Boundary field; sub-skill attribution infers context but pass condition requires an explicit boundary label per finding |
| C-04 | PASS 12 | Type field includes "spec-gap" and "contract-violation"; both flow and trace sections ask for these |
| C-05 | PASS 12 | SYNTHESIS: UNIFIED FINDINGS REPORT + Execution Log + Test Scenario Baseline + Cross-Skill Patterns |
| C-06 | PASS 10 | flow-lifecycle: "exception recovery gaps, undeclared terminal states"; flow-conversation: "dead ends, loops, ambiguous transitions" |
| C-07 | PASS 10 | Sub-skill in all finding schemas; Unified Report has Sub-Skill column |
| C-08 | PASS 10 | trace-state: exit-less states, early-firing transitions, unenforced invariants, unreachable states |
| C-09 | PASS 2 | "Baseline must contain at least as many scenarios as CRITICAL/HIGH findings in the corpus"; severity budgets guarantee >= 3 CRITICAL/HIGH upstream; baseline >= 3 by construction |
| C-10 | PASS 2 | F-ID field in schema throughout |
| C-11 | PASS 2 | Explicit severity budget per trace sub-skill; "NOT MET" halts campaign; widened-scope re-run required |
| C-12 | PARTIAL 1 | Unified report table defined; no explicit no-blank-cell contract or sentinel rules stated |
| C-13 | FAIL 0 | Execution order is flow-first (flow-lifecycle -> flow-conversation -> trace-state -> trace-contract -> trace-permissions). Flow runs before trace. No Trace Findings Brief. No Trace Link column. C-13 structurally impossible |

**V-02 Total: 54 + 30 + 7 = 91**
C-03 partial: 54/60 on essentials.

---

### V-03 -- No-Blank-Cell Table Contract

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS 12 | All five named in execution sequence; each has a dedicated section |
| C-02 | PASS 12 | RANKED FINDINGS: "Re-sort by blast radius (system-wide first) then severity within each tier" |
| C-03 | PASS 12 | System Boundary is an explicit column in the table schema; Severity explicit column; no-blank-cell rule enforces both; column definitions enumerate "state machine / contract surface / permission check / lifecycle phase / conversation state" |
| C-04 | PASS 12 | Type column includes "spec-gap" and "contract-violation"; both flow and trace sections ask for these |
| C-05 | PASS 12 | Single growing table + Ranked Findings + Execution Log + Test Scenario Baseline |
| C-06 | PASS 10 | flow-lifecycle: "exception paths without recovery, orphaned terminal paths"; flow-conversation: "dead ends (no valid next action), loops, ambiguous transitions" |
| C-07 | PASS 10 | Sub-Skill column in table; required field; no-blank-cell rule means it cannot be omitted |
| C-08 | PASS 10 | trace-state: exit-less states, early-firing transitions, unenforced invariants, unreachable states |
| C-09 | PARTIAL 1 | Test Scenario Baseline present; "From all HIGH and CRITICAL findings" -- but no severity budget guarantees CRITICAL/HIGH findings; section could yield 0-2 scenarios |
| C-10 | PASS 2 | F-ID column required in all rows; no-blank-cell rule enforces it |
| C-11 | FAIL 0 | No severity budget per trace sub-skill; Severity column exists but no budget gate |
| C-12 | PASS 2 | Full no-blank-cell contract: "No cell in any finding row may be blank -- use 'N/A -- [reason]'"; four explicit sentinel rules; pre-output verification step stated |
| C-13 | FAIL 0 | Execution order is flow-first. Findings table schema has no Trace Link column. Flow runs before trace; no Trace Findings Brief. C-13 structurally impossible |

**V-03 Total: 60 + 30 + 5 = 95**
All essentials PASS.

---

### V-04 -- Combined (Trace-First + Severity Budgets)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS 12 | All five in trace-first order; each has a dedicated section |
| C-02 | PASS 12 | Unified Findings Report: "Rank by blast radius (system-wide > cross-skill > component-wide > isolated), then severity within tier" |
| C-03 | PARTIAL 6 | Unified Findings Report table has Sub-Skill, Type, Spec Location, Severity but no System Boundary column; freeform per-skill schema also lacks it; Type infers context but doesn't satisfy explicit label requirement |
| C-04 | PASS 12 | Type includes contract-violation and spec-gap; trace-contract and trace-state sections target these |
| C-05 | PASS 12 | SYNTHESIS: UNIFIED FINDINGS REPORT + Execution Log + Test Scenario Baseline + Cross-Skill Patterns |
| C-06 | PASS 10 | flow-lifecycle: "exception recovery gaps"; flow-conversation: "dead ends, loops, ambiguous transitions" |
| C-07 | PASS 10 | Sub-Skill in all finding schemas; Unified Report has Sub-Skill column |
| C-08 | PASS 10 | trace-state: exit-less states, early-firing transitions, unenforced invariants, unreachable states |
| C-09 | PASS 2 | "All CRITICAL and HIGH findings become named test scenarios"; budget gate guarantees >= 3 CRITICAL/HIGH from trace sub-skills; baseline >= 3 by construction |
| C-10 | PASS 2 | F-ID in all schemas |
| C-11 | PASS 2 | Severity budget per trace sub-skill; Severity Budget Gate table; halting mechanism if NOT MET |
| C-12 | PARTIAL 1 | Unified report table defined; no no-blank-cell contract; freeform per-sub-skill schemas; no sentinel rules |
| C-13 | PASS 2 | Trace-first + Trace Findings Brief + Trace link check + explicit "At least one flow finding must carry a Trace Link" + "Campaign does not complete without... at least one flow finding carrying a Trace Link" |

**V-04 Total: 54 + 30 + 9 = 93**
C-03 partial: 54/60 on essentials.

---

### V-05 -- All Three Combined

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS 12 | All five in trace-first execution order; each has a dedicated section |
| C-02 | PASS 12 | RANKED FINDINGS section with blast-radius sort; blast radius rationale required for top-tier findings |
| C-03 | PASS 12 | System Boundary is an explicit column in the 10-column table; labels pre-assigned per sub-skill in the prompt ("state machine" / "contract surface" / "permission check" / "lifecycle phase" / "conversation state"); no-blank-cell rule enforces both System Boundary and Severity per row |
| C-04 | PASS 12 | Type column includes contract-violation and spec-gap; trace-contract and trace-state sections target these |
| C-05 | PASS 12 | Single 10-column findings table (grows incrementally) + Ranked Findings + Execution Log + Test Scenario Baseline + Cross-Skill Patterns; cohesive integrated structure |
| C-06 | PASS 10 | flow-lifecycle: "exception paths without recovery, undeclared terminal states"; flow-conversation: "dead ends, loops, ambiguous transitions" |
| C-07 | PASS 10 | Sub-Skill column in table; no-blank-cell rule makes omission a named failure |
| C-08 | PASS 10 | trace-state: exit-less states, early-firing transitions, unenforced invariants, unreachable states |
| C-09 | PASS 2 | "Baseline must have at least as many scenarios as there are CRITICAL/HIGH findings in the table"; budget gate guarantees >= 3 CRITICAL/HIGH from trace sub-skills; baseline >= 3 by construction |
| C-10 | PASS 2 | F-ID column in table; no-blank-cell rule makes omission a named failure |
| C-11 | PASS 2 | Severity budget per trace sub-skill; Severity Budget Gate table; halting if NOT MET without rationale |
| C-12 | PASS 2 | Full no-blank-cell contract: "Every row has all ten columns populated; N/A -- [reason] if not applicable"; sentinel rules for all columns; explicit pre-output blank-cell verification gate before writing the file |
| C-13 | PASS 2 | Trace-first + Trace Findings Brief + Trace Link column in 10-col table + "At least one flow-lifecycle finding must have a non-'none' Trace Link" + same requirement for flow-conversation |

**V-05 Total: 60 + 30 + 10 = 100**
All essentials PASS. All recommended PASS. All aspirational PASS.

---

## Score Summary

| Variation | Essentials /60 | Recommended /30 | Aspirational /10 | Total /100 | Rank |
|-----------|---------------|-----------------|-----------------|-----------|------|
| V-05 | 60 | 30 | 10 | **100** | 1st |
| V-01 | 60 | 30 | 5 | **95** | 2nd (tie) |
| V-03 | 60 | 30 | 5 | **95** | 2nd (tie) |
| V-04 | 54 | 30 | 9 | **93** | 4th |
| V-02 | 54 | 30 | 7 | **91** | 5th |

---

## Discriminating Failures

**V-02 and V-04 (C-03 partial, -6 pts each):** Neither includes a System Boundary column in the finding schema. The freeform block schema omits the field the criterion requires by name. Sub-skill attribution implies context but doesn't satisfy the explicit boundary label pass condition. This is the Round 2 C-03 gap: the prompt needs to pre-assign System Boundary labels per sub-skill, not leave them to model judgment.

**V-02 (C-13 = 0, fatal):** Executing flow before trace makes cross-referencing impossible by construction. The variation wins C-11 but loses C-13 entirely. Single-axis severity budget without trace-first ordering cannot close both criteria.

**V-03 (C-11 = 0, C-13 = 0):** Wins C-12 (best no-blank-cell enforcement of single-axis variations) but sacrifices both C-11 and C-13 entirely. The format enforcement is excellent; the causal chain runs backwards. No-blank-cell contract is compatible with any execution order -- this is the pattern to absorb into combined variations.

**V-01 (C-11 = 0, C-12 PARTIAL, C-13 PARTIAL):** Wins all essentials with trace-first + boundary-specific table columns, but the trace link mechanism is soft (guides rather than requires at least one non-"none"), no severity budget, and no universal no-blank-cell enforcement. The structural bones are correct; the enforcement is missing.

---

## Excellence Signals from V-05

**1. System Boundary labels pre-assigned per sub-skill in the prompt**
V-05 writes "System Boundary = 'state machine'" directly in the trace-state section instructions, not as a guideline but as a fill-in. This moves boundary labeling from model judgment to mechanical transcription. C-03 cannot fail silently; the model would have to actively override an explicit instruction.

**2. Universal sentinel rule: "none" not blank extended to all columns**
V-01 established "none" not blank for Trace Link. V-05 generalizes this to every column: `N/A -- [reason]` required across all cells. No column receives special treatment. This is the pattern that makes C-12 close by construction -- the contract is stated once and applies everywhere.

**3. No-findings sentinel rows required for clean sub-skills**
"A sub-skill with 'no findings' still gets a row in the findings table: Summary = 'No findings detected', Remediation = 'None required -- [reason]', all other cells populated." Prevents gaps in the execution record. A clean sub-skill is as explicit as a failing one.

**4. Pre-output blank-cell verification gate as a named final step**
The final instruction before writing the file: "run a blank-cell check: every row, every column. Any blank found -- fill it or mark N/A with a reason." This is a post-composition verification step, not just a rule at the top. It converts the no-blank contract from a style instruction into a checklist item the model must act on.

**5. Single 10-column schema closes multiple criteria simultaneously**
The unified table covers: F-ID (C-10), Sub-Skill (C-07), System Boundary (C-03), Severity (C-03), Trace Link (C-13). The budget gate before flow sub-skills guarantees C-11. All five aspirational criteria feed into one schema rather than separate mechanisms. The table is both the primary artifact and the enforcement surface.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["System boundary labels pre-assigned per sub-skill in prompt -- moves boundary labeling from model judgment to mechanical transcription, making C-03 failure require deliberate override", "Universal sentinel rule extends 'none not blank' from Trace Link to all optional columns, generalizing V-01's partial enforcement into a complete no-blank contract across every column", "No-findings sentinel rows: clean sub-skills still populate a full table row (Summary = No findings detected, all other cells filled), preventing execution log gaps and making absence of findings as explicit as presence", "Pre-output blank-cell verification gate as a named final step before writing the file, converting the no-blank contract from a style instruction into a checklist item", "Single 10-column schema closes C-03/C-07/C-10/C-13 simultaneously -- adding System Boundary column to the unified table makes all five aspirational criteria feed into one artifact rather than separate mechanisms"]}
```
