---
skill: flow-lifecycle
round: 5
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v24-2026-03-15.md
---

# flow-lifecycle -- Round 5 Variations

Round 5 targets C-18 (SLA-Absent Escape Valve), the new aspirational criterion extracted from R4 V-03 excellence signals.

**C-18 pattern**: The breach-link field (C-16) has a hard dependency on C-10/C-11 SLA evidence. Without an escape valve, authors confronting a legitimately SLA-free lifecycle either leave the field empty (fail) or write a general statement (fail). C-18 requires the prompt to provide a third outcome: the declared-absent token (`SLA-ABSENT`) that earns absence credit and distinguishes intentional omission from negligence.

**Three-way outcome model**:
- Typed reference (`BV-ID`, `SLA-ID`, `Ph-ID`) -- full credit
- Named absent token (`SLA-ABSENT: [reason]`) -- earned-absence credit
- Empty cell or general statement -- fail

Single-axis variations: V-01 (Token-First Vocabulary Block), V-02 (Conversational Escape Valve Framing), V-03 (SLA-Block-Level Declaration).
Combined variations: V-04 (V-01 + V-03: Token Vocabulary + SLA-First), V-05 (all R5 axes + R4 breach-link typed IDs + gap three-field schema).

---

## V-01 -- Output Format Axis: Token-First Vocabulary Block

**Variation axis:** A "Defined Tokens" block is placed at the top of STEP 9 (Bottleneck Register) before the table schema appears. `SLA-ABSENT` is formally defined as a named constant with its exact use condition: applies when and only when no C-10 or C-11 evidence was traced for this lifecycle. The three-way outcome for the Breach Link column is declared in the same block. The token appears as vocabulary before the author encounters the breach-link column.

**Hypothesis:** The primary failure mode for C-18 is vocabulary drift: the author knows they need to indicate SLA absence but invents ad-hoc phrasing ("N/A," "no SLA data," left blank) instead of using the named token. Placing the token definition before the schema means the author reads the token name before they read the column. This establishes the constant in working memory at the moment it is needed rather than requiring recall from a later note.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step. The Bottleneck Register (Step 9) carries a mandatory **Breach Link** column governed by the token rules declared in that step.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Declare domain-specific roles before opening the lifecycle trace. Generic labels (User, Approver, System, Finance team) are a fail.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Every decision gate in the trace must cite an R-ID from this table.

---

**STEP 2 -- PHASE MAP**

List all lifecycle phases before tracing any states. Every state belongs to exactly one phase.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

At least 6 distinct named states. Every state must carry an explicit entry condition and an explicit exit trigger. "Then X happens" without naming a cause is a fail.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name: condition, owner role, all outcome branches, and a fallback path.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- trace at least one fork-join with an explicit join condition:
```
Fork (S-ID):    [branching state]
Branch A:       [path]
Branch B:       [path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```
If no parallel activity applies, state so explicitly and give the reason.

---

**STEP 4 -- PHASE EXIT GATES**

Declare the exit gate for each phase. The `SLA envelope` field is required -- it will be referenced in Step 8 breach verdicts and Step 9 Breach Link entries.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions. The `SLA Impact` field is required on every row.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**SLA Impact rule:** state the timing consequence directionally (e.g., "adds 3+ days to PO approval phase; triggers breach threshold"). "May cause delays" is a fail.

---

**STEP 6 -- TERMINAL DECLARATION**

Every traced path and every exception must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

At least 2 edge cases distinct from Step 5 exceptions. Include why the current lifecycle has no step for each case and the SLA risk if it fires.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**SLA Risk rule:** name the specific phase SLA or timing threshold at risk and give a directional consequence (e.g., "puts Day-3 PO approval SLA at risk; likely breach if concurrent with volume peak"). "May affect timing" is a fail.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

Annotate at least 3 states or phases with timing expectations, then render a per-phase breach verdict.

**SLA Annotations:**

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

**Breach Verdicts:**

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- trace to a specific bottleneck or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck condition or exception.

---

**STEP 9 -- BOTTLENECK REGISTER**

**DEFINED TOKENS -- read before completing this table:**

| Token | Meaning | Use condition |
|-------|---------|---------------|
| `SLA-ABSENT` | No SLA evidence was traced for this lifecycle; the breach-link dependency cannot be satisfied by design | Use when and only when Step 8 produced no SLA annotations (C-10 not satisfied) and no breach verdicts (C-11 not satisfied). Must be followed by a reason: `SLA-ABSENT: [reason]`. |

**Breach Link column -- three-way outcome:**
1. **Typed reference** (`BV-01`, `SLA-02`, `PH-03: [what it documents]`) -- full credit. Use when Step 8 evidence exists.
2. **Declared-absent token** (`SLA-ABSENT: [reason]`) -- earned-absence credit. Use when no Step 8 evidence was traced.
3. **Empty cell or general statement** ("causes delays here", "see SLA section") -- **fail**. No credit.

At least 2 bottlenecks required.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Each gap must name the cause and a specific harm consequence.

| G-ID | Phase (Ph-ID) | Gap Name | Cause | Harm from Absence |
|------|--------------|---------|-------|------------------|
| G-01 | | | | |

**Harm from Absence** must name a specific consequence (e.g., "invoice may be posted against a closed period; triggers audit finding"). "May cause issues" is a fail.

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency. Name the recipient process, the fields passed, and the coupling state.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

If all phases have exception handlers, declare full coverage explicitly.

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). If only a single process state applies, declare it explicitly with a reason.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] Step 9: Every Breach Link cell carries either a typed ID reference OR the `SLA-ABSENT: [reason]` token. No cell is empty or a general statement.
- [ ] Step 8: At least 3 SLA annotations and at least 1 breach = Y verdict (unless `SLA-ABSENT` is declared in Step 9).
- [ ] Step 4: Every Phase Exit Gate declares an SLA envelope.
- [ ] Step 5: Every exception row has an SLA Impact field with a directional timing consequence.
- [ ] Step 7: Every edge case has an SLA Risk field naming a specific threshold.
- [ ] Step 10: Every gap has a specific Harm from Absence.
- [ ] Step 11: At least 1 cross-lifecycle handoff identified.
- [ ] Step 12: Every phase accounted for; uncovered phases named with risk consequence.
- [ ] Step 13: Bottleneck trajectory complete or absence declared with reason.

Any unchecked item is a fail.

---

## V-02 -- Phrasing Register Axis: Conversational Escape Valve Framing

**Variation axis:** The escape valve mechanism is introduced in conversational language at the point of use in STEP 9 rather than as a formal token-definition block. The instruction addresses the author's decision directly: "If you didn't trace any SLA evidence for this lifecycle, you can't link to what doesn't exist -- use `SLA-ABSENT: [why no SLA data]` instead of leaving the cell blank. That's an honest answer; blank is not." The three-way outcome is explained in plain prose rather than a table.

**Hypothesis:** The formal token-definition approach (V-01) is correct but assumes the author reads the vocabulary block before the column. Authors who skip to the table first see a required column with no memory of the token name. Conversational framing at the point of use addresses the actual decision moment: "I need to fill this cell and I have no SLA evidence." The conversational instruction is more likely to be read because it is narrative, and the human framing of "honest answer vs. blank" creates a memorable decision rule that does not require recall of a formal constant.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step. Each step specifies what is required and why vague or empty entries are rejected.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Before tracing a single state, declare every role involved in this lifecycle. If a role you assign is generic -- "User," "Approver," "Admin," "Finance team" -- replace it with the specific function title this lifecycle actually uses. A process owner who approves invoices is an AP Supervisor, not an Approver.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Every decision gate later in the trace must name the R-ID of the role that makes the decision.

---

**STEP 2 -- PHASE MAP**

Name every major phase before writing any states. Phases give the trace its structure and will be referenced as Ph-IDs throughout.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Every state needs to answer three questions: (1) how did I get here? (2) what happens while I am here? (3) how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. A decision point without an owner role (who decides?) and without named outcome branches is incomplete.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- if two or more activities happen concurrently, show them as parallel lanes:
```
Fork (S-ID):    [state where paths split]
Branch A:       [what happens concurrently in lane A]
Branch B:       [what happens concurrently in lane B]
Join condition: [both A and B must reach what state before the main sequence resumes]
Merge owner:    [R-ID who confirms the join]
```
If there are no concurrent activities in this lifecycle, say so explicitly and explain why.

---

**STEP 4 -- PHASE EXIT GATES**

For each phase in Step 2, declare the conditions that allow the lifecycle to exit the phase. Also name what typically blocks the exit -- this is where bottlenecks live.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [how long this phase is expected to take, e.g., "2 business days"]
Success:        [next Ph-ID or T-ID]
Failure:        [T-ID or exception branch that fires]
Blocked by:     [the role, system, or condition most likely to hold up the exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions, each named for this lifecycle specifically. For every exception, include how it affects timing -- vague impact language is rejected.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

The SLA Impact field wants things like "adds 4-6 days to the goods receipt phase and pushes PO approval past its 3-day SLA." It does not want "may delay processing."

---

**STEP 6 -- TERMINAL DECLARATION**

Every branch in your trace, including exception paths, must end somewhere named. List all terminals here.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

You need at least one success terminal and at least one failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Edge cases are different from exceptions: an exception is a path the lifecycle handles (badly or otherwise); an edge case is a scenario the lifecycle has no path for at all. Name at least 2 of these and explain what goes wrong if they fire.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

For SLA Risk: tell me which phase SLA is at risk and how bad the timing impact is. "May affect timing" is not useful.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

Annotate at least 3 states or phases with their timing targets, then make an active call: did this scenario breach the SLA or not?

**SLA Annotations:**

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

**Breach Verdicts** -- for each phase you annotated, make the call:

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | What caused the breach (if Y -- name a specific bottleneck or exception) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least one BV-ID must be breach = Y and the cause must trace back to a specific bottleneck or exception you have already documented.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. Each row needs a `Breach Link` -- a pointer to the SLA or breach evidence that shows why this bottleneck matters to timing.

**How to fill Breach Link:** There are three acceptable states for this cell and only three:

1. **You have SLA evidence from Step 8.** Write the ID of the breach verdict or SLA annotation row that documents this bottleneck's timing consequence: e.g., `BV-01: approval phase breach, caused by this manual queue`. Full credit.

2. **You have no SLA evidence at all for this lifecycle.** That happens -- some processes genuinely have no SLA targets. Write `SLA-ABSENT: [one sentence explaining why no SLA data was established for this lifecycle]`. That is an honest and acceptable answer. It earns absence credit; you will not be penalized for missing evidence that does not exist.

3. **You leave the cell blank or write something vague** like "causes delays" or "see timing section." That is a fail. It tells the reader nothing and leaves the bottleneck's impact unresolvable.

The three outcomes are: typed reference (full credit), `SLA-ABSENT: [reason]` (earned-absence credit), or empty/vague (fail).

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap -- a step the lifecycle design does not include but real-world execution requires. Name the harm clearly.

| G-ID | Phase (Ph-ID) | Gap Name | Cause | Harm from Absence |
|------|--------------|---------|-------|------------------|
| G-01 | | | | |

Harm from Absence means something specific, like "supplier's bank account is never validated before payment release; payment may be sent to a fraudulent account." Not "may cause issues."

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

Name at least one point where this lifecycle hands off to or receives from a different business process.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

Go back through the phases in Step 2 and check: does each phase have at least one exception handler in Step 5? Name the risk for any phase that does not.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

If every phase is covered, say that explicitly rather than leaving the audit implied.

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck, note whether it changes if you are comparing an as-is process to a to-be process. If this simulation covers only one state of the process, say so and explain.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

**Completion checklist before writing:**
- [ ] Step 9: Every Breach Link cell has either a typed ID reference or `SLA-ABSENT: [reason]`. No blank cells. No vague statements.
- [ ] Step 8: At least 3 SLA annotations; at least 1 breach = Y (unless `SLA-ABSENT` was declared in Step 9).
- [ ] Step 4: Every Phase Exit Gate declares an SLA envelope.
- [ ] Step 5: Every exception row's SLA Impact is directional and specific.
- [ ] Step 7: Every edge case names a specific SLA threshold at risk.
- [ ] Step 10: Every gap's Harm from Absence is specific.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for in coverage audit.
- [ ] Step 13: Trajectory complete or absence declared with reason.

---

## V-03 -- Lifecycle Emphasis Axis: SLA-Block-Level Escape Valve Declaration

**Variation axis:** The escape valve is declared at the top of STEP 8 (SLA Annotation and Breach Verdicts) -- the first point where SLA evidence is established -- rather than at STEP 9 (Bottleneck Register) where it is consumed. At Step 8, the author decides once whether SLA evidence exists for this lifecycle. If not, they write `SLA-ABSENT` into a dedicated header field, and the Step 9 instruction directs them to carry that token forward to all Breach Link cells. The declaration is made before the bottleneck table is opened.

**Hypothesis:** In V-01 and V-02, the escape valve appears at Step 9, the consumption point. Authors who legitimately have no SLA data still reach Step 8, write nothing, and only encounter the escape valve instructions at Step 9 -- after they have already formed the expectation that they have nothing to offer. Declaring the escape valve at Step 8 shifts the decision upstream: "Before I write a single annotation, am I tracing SLA evidence or not?" That earlier decision point prevents the author from building up cognitive debt across Step 8 and arriving at Step 9 in a state of uncertainty. A single header field in Step 8 also makes the no-SLA case visible to reviewers scanning the output: `SLA status: SLA-ABSENT: [reason]` is a first-class declaration, not a footnote in a column.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Step 8 (SLA Annotation) is a decision point: you will declare whether SLA evidence applies before opening any SLA table. That declaration carries forward to Step 9.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Declare domain-specific roles before opening the lifecycle trace. Generic labels are a fail.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Every decision gate must cite an R-ID.

---

**STEP 2 -- PHASE MAP**

List all lifecycle phases before tracing any states.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

At least 6 distinct named states. Every state must carry an explicit entry condition and an explicit exit trigger.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name: condition, owner role, all outcome branches, fallback path.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- at least one fork-join. State absence explicitly if none applies.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true]
SLA envelope:   [target duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception]
Blocked by:     [specific role, system, or condition]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions. SLA Impact required on every row.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

SLA Impact: state timing consequence directionally. "May cause delays" is a fail.

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success and 1 failure/cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

At least 2 edge cases distinct from Step 5. SLA Risk required.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

SLA Risk: name the specific phase SLA threshold at risk and give a directional consequence. "May affect timing" is a fail.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

**SLA STATUS DECLARATION -- complete this first:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [state in one sentence why no SLA envelopes exist for
                              this lifecycle -- e.g., "This is an internal triage flow
                              with no contractual SLA targets defined."]
```

If `SLA-ABSENT` is declared: skip Tables 8a and 8b, and in Step 9 every Breach Link cell receives the token `SLA-ABSENT` (carried from this declaration). Do not leave Breach Link cells blank.

If SLA evidence applies: complete both tables.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- trace to a specific bottleneck or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck condition or exception.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. The `Breach Link` column carries the SLA status from Step 8:

- **If Step 8 SLA evidence applies:** each Breach Link cell must reference a specific Phase Exit Gate (Ph-ID), SLA annotation row (SLA-ID), or breach verdict row (BV-ID). Empty cell = fail. General statement without a typed ID = fail.
- **If Step 8 declared `SLA-ABSENT`:** each Breach Link cell carries `SLA-ABSENT` (the token you established in Step 8). Do not repeat the reason in each cell -- one reference is sufficient.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Three required fields: Gap Name, Cause, and Harm from Absence (specific consequence).

| G-ID | Phase (Ph-ID) | Gap Name | Cause | Harm from Absence |
|------|--------------|---------|-------|------------------|
| G-01 | | | | |

"May cause issues" is a fail for Harm from Absence.

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency with direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, check whether a handler exists and name the risk for any uncovered phase.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

Full coverage must be explicitly declared if it applies.

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

If no variant comparison applies, declare it explicitly with a reason.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

**Completion checklist before writing:**
- [ ] Step 8: SLA Status Declaration filled (applies or SLA-ABSENT with reason).
- [ ] Step 9: Every Breach Link cell carries either a typed ID reference or the `SLA-ABSENT` token. No blank cells.
- [ ] Step 4: Every Phase Exit Gate declares an SLA envelope.
- [ ] Step 5: Every exception row has a directional SLA Impact.
- [ ] Step 7: Every edge case names a specific SLA threshold at risk.
- [ ] Step 10: Every gap names a specific Harm from Absence.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase in the coverage audit.
- [ ] Step 13: Trajectory complete or absence declared.

Any unchecked item is a fail.

---

## V-04 -- Combined: Token Vocabulary Block + SLA-First Declaration (V-01 + V-03)

**Variation axis:** Combines the named-constant token vocabulary block (V-01) with the SLA-block-level escape valve declaration (V-03). The token is formally defined as a named constant in a "Defined Tokens" block at the top of Step 8. The author makes the SLA Status Declaration in Step 8 using that token. Step 9 Breach Link instructions reference the token by name and direct the author to carry it forward from the Step 8 header. The token is established before the SLA tables are opened and is available by name when the breach-link column is encountered.

**Hypothesis:** V-01 establishes the token at the consumption point (Step 9) but assumes recall from a prior encounter. V-03 establishes the declaration at the source point (Step 8) but uses prose to introduce the token rather than a formal definition. Combining them: a formal token definition appears in Step 8 before the declaration, and the Step 9 instructions reference the same token by name. Authors who read Step 8 see the token defined and then immediately use it; authors who skip to Step 9 see the token cited and know to look back. Both reading patterns converge on the same token name, eliminating vocabulary drift.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Step 8 establishes your SLA vocabulary and status declaration. Step 9 consumes the tokens produced in Step 8.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Declare domain-specific roles before the lifecycle trace. Generic labels are a fail.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Every decision gate must cite an R-ID.

---

**STEP 2 -- PHASE MAP**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

At least 6 distinct named states. Every state must carry an explicit entry condition and an explicit exit trigger.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name: condition, owner role, all outcome branches, fallback path.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- at least one fork-join. State absence explicitly if none applies.

---

**STEP 4 -- PHASE EXIT GATES**

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true]
SLA envelope:   [target duration]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception]
Blocked by:     [specific role, system, or condition]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions. SLA Impact required on every row.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type | Reached From |
|------|--------------|------|--------------|
| T-01 | | | |
| T-02 | | | |

At least 1 success and 1 failure/cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

At least 2 edge cases distinct from exceptions. SLA Risk required.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS -- establish these before completing any SLA table:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | C-10 not traceable: no SLA envelopes were defined for this lifecycle. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

`SLA-ABSENT` declared here carries forward to every Breach Link cell in Step 9. If declared, skip Tables 8a and 8b.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with causal reference to a bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- specific bottleneck or E-ID) |
|-------|--------------|---------------|--------------|---------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y with a traceable cause.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. Breach Link column -- three-way outcome:

| Token / Value | Outcome | Requirement |
|---------------|---------|-------------|
| Typed reference: `BV-01`, `SLA-02`, `PH-03: [what]` | Full credit | Use when Step 8 produced SLA evidence |
| `SLA-ABSENT` (carried from Step 8 declaration) | Earned-absence credit | Use when Step 8 declared `SLA-ABSENT` |
| Empty cell or general statement | **Fail** | Never acceptable |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Harm from Absence must name a specific consequence.

| G-ID | Phase (Ph-ID) | Gap Name | Cause | Harm from Absence |
|------|--------------|---------|-------|------------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

Declare full coverage explicitly if it applies.

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

**Completion checklist before writing:**
- [ ] Step 8: `SLA-ABSENT` token defined; SLA Status Declaration filled.
- [ ] Step 9: Every Breach Link cell carries a typed ID reference or `SLA-ABSENT`. No blank cells. No general statements.
- [ ] Step 4: Every Phase Exit Gate has an SLA envelope.
- [ ] Step 5: Every exception has a directional SLA Impact.
- [ ] Step 7: Every edge case names a specific SLA threshold.
- [ ] Step 10: Every gap names a specific Harm from Absence.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase in coverage audit.
- [ ] Step 13: Trajectory complete or absence declared.

Any unchecked item is a fail.

---

## V-05 -- Full Combination: All R5 Axes + R4 Breach Link Typed IDs + Gap Three-Field Schema

**Variation axis (V-01 + V-02 + V-03 + R4 C-16 enforcement + R4 C-17 three-field schema):** Combines all three R5 axes -- token vocabulary block (V-01), conversational framing (V-02), and SLA-block-level declaration (V-03) -- with the R4 carry-forward of explicit breach-link typed-ID enforcement and the three-field gap schema (Missing Step / Why Required / Risk if Absent). The prompt establishes the escape valve via a formal token definition in Step 8, makes the SLA Status Declaration in Step 8 using that token, and repeats a conversational explanation at Step 9 for authors who reach the breach-link column without having read Step 8 carefully. The Gap Register enforces the three-field schema. The breach-link typed-ID rule is restated explicitly in Step 9.

**Hypothesis:** V-01 through V-04 each address one or two failure modes. V-05 addresses all five failure modes simultaneously: (a) vocabulary drift -- formal token definition at Step 8; (b) skip-to-table reading -- conversational explanation at Step 9; (c) upstream ordering failure -- SLA Status Declaration at Step 8 before the annotation tables; (d) breach-link ambiguity -- typed-ID enforcement restated at Step 9; (e) vague gap risk -- three-field gap schema. The cost is prompt length and density; the gain is that no single author failure mode goes unaddressed. This is the candidate for maximum-composite scoring.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Step 8 establishes SLA vocabulary and your lifecycle's SLA status. Step 9 consumes the tokens from Step 8 and enforces the breach-link typed-ID rule. Step 10 uses a three-field gap schema. These rules interact: read the instructions for each step before filling it.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Before tracing any state, declare the domain-specific roles this lifecycle uses. Replace every generic label with the named functional title the process actually uses.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. Every decision gate must cite an R-ID.

---

**STEP 2 -- PHASE MAP**

Name every lifecycle phase before writing any states.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|------------|---------|---------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|-----------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| ... | | | | | | |

**Parallel Paths** -- trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 -- PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration -- e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions. SLA Impact required on every row and must be directional (e.g., "adds 3+ days to PO approval phase; triggers breach threshold") -- "may cause delays" is a fail.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

---

**STEP 6 -- TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 -- EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for -- distinct from the exception flows in Step 5. At least 2 required. SLA Risk must name the specific phase SLA threshold at risk and give a directional consequence.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

"May affect timing" in the SLA Risk column is a fail.

---

**STEP 8 -- SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration -- complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies -- complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT` is declared here: skip Tables 8a and 8b. In Step 9, every Breach Link cell receives the token `SLA-ABSENT`. Do not leave Breach Link cells blank -- carry the declaration forward.
- If SLA evidence applies: complete both tables.

**Table 8a -- SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b -- Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y -- name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck condition or exception.

---

**STEP 9 -- BOTTLENECK REGISTER**

At least 2 bottlenecks.

**Breach Link column -- three outcomes only:**

If you have SLA evidence from Step 8 (Tables 8a and 8b completed): every Breach Link cell must reference a specific Phase Exit Gate (Ph-ID), SLA annotation row (SLA-ID), or breach verdict row (BV-ID) by typed ID. Format: `[type][ID]: [brief what it documents]`. Example: `BV-01: Approval phase breach = Y, caused by manual queue`. A typed reference is the only way to earn full credit.

If Step 8 declared `SLA-ABSENT`: carry the token forward to each Breach Link cell. Write `SLA-ABSENT` -- you established the reason in Step 8, you do not need to repeat it in every cell. This earns absence credit. It is an honest answer for a lifecycle where SLA evidence genuinely does not exist.

Empty cell, or a general statement like "causes delays in approval" or "see SLA section": fail, no credit. If you have SLA evidence and leave the cell general, it fails C-16. If you have no SLA evidence and leave the cell blank instead of using `SLA-ABSENT`, it also fails.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. All three fields must be populated with specific, non-vague content.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule or regulation), handoff precondition (name the downstream state that requires the step's output), or system dependency (name the system that fails without the step). "Best practice" does not qualify.
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" is a **fail**. A vague Risk if Absent is a **partial fail** (0.5 credit on C-17).

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not the same as coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). If only a single process state applies, say so explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] Step 8: `SLA-ABSENT` token defined in the Defined Tokens block.
- [ ] Step 8: SLA Status Declaration filled -- either Tables 8a/8b complete, or `SLA-ABSENT: [reason]` declared.
- [ ] Step 9: Every Breach Link cell carries either a typed ID reference OR the `SLA-ABSENT` token. No blank cells. No general statements.
- [ ] Step 4: Every Phase Exit Gate declares an SLA envelope.
- [ ] Step 5: Every exception row has a directional SLA Impact (not "may cause delays").
- [ ] Step 7: Every edge case names a specific SLA threshold at risk.
- [ ] Step 10: Every gap has all three fields (Missing Step, Why Required, Risk if Absent). Risk if Absent is specific.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase in coverage audit; full coverage declared if it applies.
- [ ] Step 13: Trajectory complete or absence declared with reason.

Any unchecked item is a fail.
