---
skill: quest-rubric
skill_target: campaign-simulate
date: 2026-03-17
version: 1
---

# Scoring Rubric — campaign-simulate

**Skill**: `simulate`
**Description**: Run the full technical simulation campaign. Orchestrates flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions in sequence. Output: simulation findings report ranked by blast radius. Use before implementation to find spec gaps and contract violations.

---

## Composite Score Formula

```
composite = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 points — all must pass)

### C-01 · All Five Sub-Skills Execute
- **Weight**: essential
- **Category**: correctness
- **Text**: The output must show evidence that all five sub-skills ran: flow-lifecycle, flow-conversation, trace-state, trace-contract, and trace-permissions. Each must produce distinct findings, not be silently skipped or collapsed into one pass.
- **Pass condition**: Output contains a labeled section or findings block for each of the five sub-skills by name. Absence of any one sub-skill = fail.

---

### C-02 · Findings Ranked by Blast Radius
- **Weight**: essential
- **Category**: format
- **Text**: The final findings report must present findings in ranked order using blast radius as the sort key. Blast radius must be explicit — not implied by placement — and must distinguish at minimum high / medium / low (or equivalent severity tiers).
- **Pass condition**: A ranked findings list exists with an explicit blast-radius or severity column/label. Unranked flat lists = fail.

---

### C-03 · System Boundary and Severity per Finding
- **Weight**: essential
- **Category**: correctness
- **Text**: Every finding must identify (a) the system boundary where it was detected (e.g., state machine, contract surface, permission check, lifecycle phase) and (b) a severity rating. These must appear per finding, not as a summary average.
- **Pass condition**: Each finding entry includes both a boundary label and a severity. Findings missing either field = fail.

---

### C-04 · At Least One Spec Gap or Contract Violation Surfaced
- **Weight**: essential
- **Category**: coverage
- **Text**: The primary use case of campaign-simulate is to find what breaks before writing code. The output must contain at least one concrete spec gap (underspecified behavior, missing precondition) or contract violation (expected vs. actual mismatch) with enough detail to act on.
- **Pass condition**: At least one finding is classified as a spec gap or contract violation with a description of what is missing or mismatched. A report with only "all clear" findings = fail.

---

### C-05 · Single Synthesized Report (Not Five Separate Outputs)
- **Weight**: essential
- **Category**: format
- **Text**: The output must be one unified simulation findings report, not five disconnected sub-skill outputs pasted together. Sub-skill results are inputs to synthesis; the artifact is the synthesized document.
- **Pass condition**: Output has a single report structure (header, findings table or list, summary section) that integrates all five sub-skills. Raw concatenation of five separate outputs with no integration = fail.

---

## Recommended Criteria (30 points)

### C-06 · Exception Paths and Edge Cases Identified
- **Weight**: recommended
- **Category**: depth
- **Text**: The simulation should go beyond the happy path. flow-lifecycle and flow-conversation findings should include at least one exception flow, dead-end, loop risk, or edge case per sub-skill that ran.
- **Pass condition**: At least two exception paths or edge cases are named across the report (not just implied). A report covering only normal operation = does not pass.

---

### C-07 · Findings Cross-Reference Source Sub-Skill
- **Weight**: recommended
- **Category**: coverage
- **Text**: Each finding should cite which sub-skill surfaced it (e.g., `[trace-state]`, `[flow-lifecycle]`). This allows readers to trace a finding back to its simulation context and helps prioritize re-runs.
- **Pass condition**: >= 80% of findings carry a sub-skill citation. Findings without any attribution = does not pass.

---

### C-08 · State Machine Anomalies Explicitly Called Out
- **Weight**: recommended
- **Category**: depth
- **Text**: The trace-state sub-skill should produce findings about state machine behavior — unreachable states, invalid transitions, or violated invariants — not just a confirmation that the state machine was traversed.
- **Pass condition**: At least one state machine anomaly (unreachable state, invalid transition, invariant violation, or missing guard) is named in the trace-state findings. "No anomalies found" is acceptable only if the rationale is given.

---

## Aspirational Criteria (10 points)

### C-09 · Test Scenario Baseline Derived from Findings
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The report derives a set of test scenarios (or scenario seeds) directly from its findings. Each high or medium blast-radius finding becomes a named test scenario with a brief description of what to exercise. This converts simulation output into implementation test scaffolding.
- **Pass condition**: The report includes a "Test Scenario Baseline" section with >= 3 named scenarios linked to specific findings.

---

### C-10 · Finding IDs Assigned (F-NN Pattern)
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Findings use the F-NN identifier pattern (F-01, F-02, ...) to enable cross-referencing in downstream artifacts (spec amendments, test plans, topic-echo). IDs make findings traceable through the full finding lifecycle (finding → DCR/amendment → spec update → scenario update).
- **Pass condition**: All findings in the report carry an F-NN ID. Findings without IDs = does not pass this criterion.

---

## Scoring Summary Table

| ID   | Criterion                                   | Weight        | Category    | Points |
|------|---------------------------------------------|---------------|-------------|--------|
| C-01 | All five sub-skills execute                 | essential     | correctness | 12     |
| C-02 | Findings ranked by blast radius             | essential     | format      | 12     |
| C-03 | System boundary + severity per finding      | essential     | correctness | 12     |
| C-04 | At least one spec gap or contract violation | essential     | coverage    | 12     |
| C-05 | Single synthesized report                   | essential     | format      | 12     |
| C-06 | Exception paths and edge cases              | recommended   | depth       | 10     |
| C-07 | Findings cross-reference source sub-skill   | recommended   | coverage    | 10     |
| C-08 | State machine anomalies called out          | recommended   | depth       | 10     |
| C-09 | Test scenario baseline derived              | aspirational  | behavior    | 5      |
| C-10 | Finding IDs assigned (F-NN)                 | aspirational  | behavior    | 5      |

**Max score**: 100
**Golden threshold**: all of C-01–C-05 pass AND composite >= 80

---

## Usage Notes

- Run this rubric against outputs from `/quest-variate` to compare prompt variations.
- A run that passes C-01–C-05 but scores 60–79 is useful but shallow — C-06 through C-08 are the depth signal.
- C-09 and C-10 are the "ready to implement" markers — when these appear consistently, the simulation output is directly wiring into test infrastructure.
- Common failure mode: skill produces five separate sub-skill outputs without synthesis (fails C-05), or skips trace-permissions silently (fails C-01).
