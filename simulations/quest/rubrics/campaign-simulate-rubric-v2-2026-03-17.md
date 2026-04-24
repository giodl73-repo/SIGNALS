Written to `simulations/quest/rubrics/campaign-simulate-rubric-v2-2026-03-17.md`.

---

**What changed from v1 to v2:**

Three new aspirational criteria extracted from V-05's winning pattern:

| ID | New Criterion | Source Pattern |
|----|---------------|----------------|
| C-11 | CRITICAL/HIGH budget met per trace sub-skill | V-05 severity budgets structurally close C-09 by construction |
| C-12 | Structured findings table, no blank cells | V-02/V-05 mandatory table; makes C-03/C-07 failures structurally visible |
| C-13 | Flow findings explicitly reference trace context | V-01/V-05 trace-first ordering, measurable in the output |

**Scoring adjustment:** aspirational tier expanded from 2 to 5 criteria; each is now worth 2 pts (was 5). Max score stays 100.

**The key insight encoded in C-11:** the Round 1 discriminating failure (C-09) was caused by missing *inputs*, not a missing output section. V-05 proved that severity budgets on the three trace sub-skills guarantee >= 3 HIGH/CRITICAL findings upstream — the test scenario baseline derives from what the budgets already forced. C-11 makes that structural guarantee a rubric target rather than just a prompt technique.
ce-contract, and trace-permissions. Each must produce distinct findings, not be silently skipped or collapsed into one pass.
- **Pass condition**: Output contains a labeled section or findings block for each of the five sub-skills by name. Absence of any one sub-skill = fail.

---

### C-02 . Findings Ranked by Blast Radius
- **Weight**: essential
- **Category**: format
- **Text**: The final findings report must present findings in ranked order using blast radius as the sort key. Blast radius must be explicit -- not implied by placement -- and must distinguish at minimum high / medium / low (or equivalent severity tiers).
- **Pass condition**: A ranked findings list exists with an explicit blast-radius or severity column/label. Unranked flat lists = fail.

---

### C-03 . System Boundary and Severity per Finding
- **Weight**: essential
- **Category**: correctness
- **Text**: Every finding must identify (a) the system boundary where it was detected (e.g., state machine, contract surface, permission check, lifecycle phase) and (b) a severity rating. These must appear per finding, not as a summary average.
- **Pass condition**: Each finding entry includes both a boundary label and a severity. Findings missing either field = fail.

---

### C-04 . At Least One Spec Gap or Contract Violation Surfaced
- **Weight**: essential
- **Category**: coverage
- **Text**: The primary use case of campaign-simulate is to find what breaks before writing code. The output must contain at least one concrete spec gap (underspecified behavior, missing precondition) or contract violation (expected vs. actual mismatch) with enough detail to act on.
- **Pass condition**: At least one finding is classified as a spec gap or contract violation with a description of what is missing or mismatched. A report with only "all clear" findings = fail.

---

### C-05 . Single Synthesized Report (Not Five Separate Outputs)
- **Weight**: essential
- **Category**: format
- **Text**: The output must be one unified simulation findings report, not five disconnected sub-skill outputs pasted together. Sub-skill results are inputs to synthesis; the artifact is the synthesized document.
- **Pass condition**: Output has a single report structure (header, findings table or list, summary section) that integrates all five sub-skills. Raw concatenation of five separate outputs with no integration = fail.

---

## Recommended Criteria (30 points)

### C-06 . Exception Paths and Edge Cases Identified
- **Weight**: recommended
- **Category**: depth
- **Text**: The simulation should go beyond the happy path. flow-lifecycle and flow-conversation findings should include at least one exception flow, dead-end, loop risk, or edge case per sub-skill that ran.
- **Pass condition**: At least two exception paths or edge cases are named across the report (not just implied). A report covering only normal operation = does not pass.

---

### C-07 . Findings Cross-Reference Source Sub-Skill
- **Weight**: recommended
- **Category**: coverage
- **Text**: Each finding should cite which sub-skill surfaced it (e.g., [trace-state], [flow-lifecycle]). This allows readers to trace a finding back to its simulation context and helps prioritize re-runs.
- **Pass condition**: >= 80% of findings carry a sub-skill citation. Findings without any attribution = does not pass.

---

### C-08 . State Machine Anomalies Explicitly Called Out
- **Weight**: recommended
- **Category**: depth
- **Text**: The trace-state sub-skill should produce findings about state machine behavior -- unreachable states, invalid transitions, or violated invariants -- not just a confirmation that the state machine was traversed.
- **Pass condition**: At least one state machine anomaly (unreachable state, invalid transition, invariant violation, or missing guard) is named in the trace-state findings. "No anomalies found" is acceptable only if the rationale is given.

---

## Aspirational Criteria (10 points)

### C-09 . Test Scenario Baseline Derived from Findings
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The report derives a set of test scenarios (or scenario seeds) directly from its findings. Each high or medium blast-radius finding becomes a named test scenario with a brief description of what to exercise. This converts simulation output into implementation test scaffolding.
- **Pass condition**: The report includes a "Test Scenario Baseline" section with >= 3 named scenarios linked to specific findings.

---

### C-10 . Finding IDs Assigned (F-NN Pattern)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Findings use the F-NN identifier pattern (F-01, F-02, ...) to enable cross-referencing in downstream artifacts (spec amendments, test plans, topic-echo). IDs make findings traceable through the full finding lifecycle (finding -> DCR/amendment -> spec update -> scenario update).
- **Pass condition**: All findings in the report carry an F-NN ID. Findings without IDs = does not pass this criterion.

---

### C-11 . At Least One CRITICAL or HIGH Finding per Trace Sub-Skill
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each of the three trace sub-skills (trace-state, trace-contract, trace-permissions) contributes at least one CRITICAL or HIGH severity finding to the report. When all three trace budgets are met, >= 3 HIGH/CRITICAL findings exist in the corpus upstream of the test scenario baseline -- C-09 passes by construction without requiring an explicit scenario count floor. Guarantee the inputs; the output floor follows.
- **Pass condition**: trace-state, trace-contract, and trace-permissions each have at least one finding rated CRITICAL or HIGH attributed to them. Missing severity budget on any one trace sub-skill = does not pass.

---

### C-12 . Findings Presented in Structured Table (No Blank Cells)
- **Weight**: aspirational
- **Category**: format
- **Text**: All findings appear in a structured table with explicit columns for at minimum: Finding ID, Sub-skill, System Boundary, Severity, Description. No cell in any finding row is blank. The table format makes C-03 and C-07 failures structurally visible -- a missing boundary label or sub-skill citation cannot be buried in prose.
- **Pass condition**: A findings table exists with all required columns populated for every row. Prose-only findings lists or a table with blank cells = does not pass.

---

### C-13 . Flow Findings Explicitly Reference Trace Context
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one flow sub-skill finding (flow-lifecycle or flow-conversation) explicitly references or builds on a specific trace finding -- e.g., a lifecycle finding cites a state invariant violation from trace-state, or a conversation finding references a contract mismatch from trace-contract. This cross-reference is the measurable output signature of trace-first execution ordering: trace context fed into flow simulations rather than five sub-skills running in isolation.
- **Pass condition**: At least one flow finding explicitly names a trace finding by ID or by content description. Flow findings that are fully isolated from trace context = does not pass.

---

## Scoring Summary Table

| ID   | Criterion                                     | Weight       | Category    | Points |
|------|-----------------------------------------------|--------------|-------------|--------|
| C-01 | All five sub-skills execute                   | essential    | correctness | 12     |
| C-02 | Findings ranked by blast radius               | essential    | format      | 12     |
| C-03 | System boundary + severity per finding        | essential    | correctness | 12     |
| C-04 | At least one spec gap or contract violation   | essential    | coverage    | 12     |
| C-05 | Single synthesized report                     | essential    | format      | 12     |
| C-06 | Exception paths and edge cases                | recommended  | depth       | 10     |
| C-07 | Findings cross-reference source sub-skill     | recommended  | coverage    | 10     |
| C-08 | State machine anomalies called out            | recommended  | depth       | 10     |
| C-09 | Test scenario baseline derived from findings  | aspirational | behavior    | 2      |
| C-10 | Finding IDs assigned (F-NN pattern)           | aspirational | behavior    | 2      |
| C-11 | CRITICAL/HIGH budget met per trace sub-skill  | aspirational | depth       | 2      |
| C-12 | Structured findings table, no blank cells     | aspirational | format      | 2      |
| C-13 | Flow findings reference trace context         | aspirational | depth       | 2      |

**Max score**: 100
**Golden threshold**: all of C-01--C-05 pass AND composite >= 80

---

## Usage Notes

- Run this rubric against outputs from /quest-variate to compare prompt variations.
- A run that passes C-01--C-05 but scores 60--79 is useful but shallow -- C-06 through C-08 are the depth signal.
- C-09 through C-13 are the structural markers. C-11 is the upstream guarantee: when all three trace sub-skills each have a CRITICAL/HIGH finding, C-09 closes by construction.
- C-12 is the format enforcement criterion. A findings table with no blank cells makes C-03 and C-07 failures structurally impossible to hide.
- C-13 measures cross-skill synthesis. If flow findings never reference trace findings, the sub-skills ran in isolation rather than in sequence.
- Common failure modes: silent sub-skill skipping (fails C-01), five separate outputs with no synthesis (fails C-05), findings without severity labels (fails C-03).
- v2 change: aspirational criteria expanded from 2 to 5; per-criterion points reduced from 5 to 2. Max score unchanged at 100.
