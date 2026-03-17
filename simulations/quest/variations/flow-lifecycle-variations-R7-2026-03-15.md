Generated and saved to `simulations/quest/golden/flow-lifecycle-variate-R8-2026-03-15.md` (R8 to preserve existing R7 file which targeted a different rubric version).

---

## Round 7 — flow-lifecycle Variations

**Target criteria:** C-25 (Gate Failure Causal Mechanism) and C-26 (Exception Authority Inline Schema Enforcement)

---

## V-01 — Output Format Axis: Scan Table Architecture

**Variation axis:** The completion checklist is replaced by a structured Scan Table (SC-01 through SC-05) with columns: Section, Verification Criterion, **Defect Type if OPEN**, **Artifact Consequence**, Status. Every row commits the author to a defect-consequence pair before marking CLOSED. The production gate references the Defect Type column for its causal clause.

**Hypothesis:** A checklist requires only a boolean decision (done/not done); a scan table requires the author to name the structural harm before marking CLOSED. The Defect Type column satisfies C-25 by reference without requiring the author to re-read the gate sentence. C-26 absent (Handler constraint in preamble) to isolate the output-format axis.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below — it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify — example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" — no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" — no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" — no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" — no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" — no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" — no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" — no classification, no location for shifted |

---

**STEP 1 — DOMAIN ROLE REGISTRY**

Name every domain role this lifecycle requires. Use the functional title the process actually uses — not org-chart categories. Every decision gate in Step 3, every Handler cell in Step 5, and every owner in Step 12 references R-IDs from this table.

Every Handler (R-ID) entry in the Exception Catalog must resolve to a role carrying Exception Handler = Y in this table. Roles carrying N may not be assigned as exception handlers.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned | Exception Handler (Y/N) |
|------|------------------------------|--------|-----------------|------------------------|
| R-01 | | | | |
| R-02 | | | | |
| ... | | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. Every decision gate must cite an R-ID. At least one role must carry Exception Handler = Y.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete and at least one role carries Exception Handler = Y.

---

**STEP 2 — PHASE MAP**

Name every lifecycle phase before writing any states. Each phase has a named entry trigger and a named completion condition.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

> **GATE B**: Do not open the State Trace until the Phase Map is complete with a named entry trigger and completion condition per phase.

---

**STEP 3 — STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** — at least 3. Each must name condition, owner role, measurable threshold, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** — trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 — PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration — e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 — EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`. Every Handler (R-ID) must resolve to a role carrying Exception Handler = Y in the Role Registry (Step 1). A Handler cell that references a role carrying N, or that is blank, is a fail.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|----------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered (e.g., "adds 3+ days to PH-02 PO Approval; triggers breach threshold"). "May cause delays" is a fail — no phase, no magnitude.

---

**STEP 6 — TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 — EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for — distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level (e.g., "puts PH-03 Day-5 SLA at risk; breach likely if concurrent with volume peak"). "May affect timing" is a fail — no Ph-ID, no magnitude.

---

**STEP 8 — SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration — complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies — complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT` is declared here: skip Tables 8a and 8b. In Step 9, every Breach Link cell receives the token `SLA-ABSENT`. Do not leave Breach Link cells blank — carry the declaration forward.
- If SLA evidence applies: complete both tables.

**Table 8a — SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b — Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y — name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck condition or exception.

---

**STEP 9 — BOTTLENECK REGISTER**

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link — Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes — Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** — you have evidence and did not cite it |
| **FM-B** (fail) | No — Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** — you had the token and did not use it |
| **PM-1** (pass) | Yes — Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`) | **Full credit** |
| **PM-2** (pass) | No — Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate), role dependency (name the role), external system (name the system), or data dependency (name the data object). "Approval takes too long" is a fail — no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail — no states named, no consequence type.

---

**STEP 10 — GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency — regulatory rule (cite the rule or regulation), handoff precondition (name the downstream state that requires the step's output), or system dependency (name the system that fails without the step). "Best practice" does not qualify — example fail: "improves audit trail" (no specific rule or dependency cited).
- **Risk if Absent**: name the consequence — SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" is a fail.

---

**STEP 11 — CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 — EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists. If every phase is covered, declare full coverage explicitly — silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 — BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). See FIELD CONTENT RULES for `Net Change`. If only a single process state applies, declare it explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. "Improved" is a fail — no classification, no location for shifted.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary — complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status |
|-------|---------|------------------------|---------------------|---------------------|--------|
| SC-01 | Role Registry | Every role has a domain-qualified title; ≥3 R-IDs; at least one Exception Handler = Y | Generic role present (e.g., "Approver" — no functional title) or no Y-certified handler | Decision gates in the artifact cite unresolvable owners; exception paths have no certified handler | OPEN / CLOSED |
| SC-02 | Exception Catalog | Every Handler (R-ID) traces to a role with Exception Handler = Y | Uncertified exception handler (role carries N or is absent from registry) | At least one exception path in the artifact has no accountable handling owner | OPEN / CLOSED |
| SC-03 | Terminal Declaration | Every traced path (S-ID and E-ID) ends at a named T-ID | Unterminated branch (state or exception with no terminal) | At least one path in the artifact reaches no named conclusion — the trace is operationally incomplete | OPEN / CLOSED |
| SC-04 | Bottleneck Register | Every Breach Link is PM-1 or PM-2; no FM-A or FM-B | FM-A: has SLA evidence, used general language; FM-B: declared SLA-ABSENT, left cell blank | Breach analysis in the artifact is disconnected from SLA evidence | OPEN / CLOSED |
| SC-05 | Gap Register | Every Why Required cites a specific rule, dependency, or regulation | "Best practice" in Why Required (no specific rule or dependency named) | Gap requirement in the artifact is unverifiable — no named rule or dependency an auditor can check | OPEN / CLOSED |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail — it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unterminated path, an uncertified exception handler, an unresolvable decision owner, or a breach analysis disconnected from SLA evidence) — and that artifact must be discarded and rebuilt from the failing step.

---

## V-02 — Role Sequence Axis: Exception Handler Column-Header Pre-Certification

**Variation axis:** The Handler column header in the Exception Catalog (Step 5) embeds the backward-trace rule inline: `Handler (R-ID) — Must trace to a role with Exception Handler = Y in the Role Registry — Mandatory; blank or uncertified role is a fail`. The rule appears at the exact point where Handler values are entered, not in a preamble block. The production gate has failure consequence and remediation but no causal mechanism — C-25 is absent to isolate the Handler-header axis.

**Hypothesis:** Embedding the backward-trace constraint in the column header makes it impossible to fill a Handler cell without reading the constraint. Preamble enforcement (C-23 baseline) is spatially separated from the column it governs; an author who skims to the table sees the header before any cell. If C-26 alone improves handler-certification compliance, it is a superior placement to preamble enforcement even without the causal gate mechanism.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below — it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify — example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" — no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" — no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" — no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" — no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" — no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" — no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" — no classification, no location for shifted |

---

**STEP 1 — DOMAIN ROLE REGISTRY**

Name every domain role this lifecycle requires. Use the functional title the process actually uses — not org-chart categories. Every decision gate in Step 3, every Handler cell in Step 5, and every owner in Step 12 references R-IDs from this table.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned | Exception Handler (Y/N) |
|------|------------------------------|--------|-----------------|------------------------|
| R-01 | | | | |
| R-02 | | | | |
| ... | | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. Every decision gate must cite an R-ID. At least one role must carry Exception Handler = Y — this designation authorizes that role to appear in the Handler column of the Exception Catalog.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete and at least one role carries Exception Handler = Y.

---

**STEP 2 — PHASE MAP**

Name every lifecycle phase before writing any states. Each phase has a named entry trigger and a named completion condition.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

> **GATE B**: Do not open the State Trace until the Phase Map is complete with a named entry trigger and completion condition per phase.

---

**STEP 3 — STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** — at least 3. Each must name condition, owner role, measurable threshold, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** — trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 — PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration — e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 — EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) — Must trace to a role with Exception Handler = Y in the Role Registry — Mandatory; blank or uncertified role is a fail | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered. "May cause delays" is a fail — no phase, no magnitude.

---

**STEP 6 — TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 — EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for — distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level. "May affect timing" is a fail — no Ph-ID, no magnitude.

---

**STEP 8 — SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration — complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies — complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT` is declared here: skip Tables 8a and 8b. In Step 9, every Breach Link cell receives the token `SLA-ABSENT`. Do not leave Breach Link cells blank.
- If SLA evidence applies: complete both tables.

**Table 8a — SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b — Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y — name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a cause traceable to a specific bottleneck or exception.

---

**STEP 9 — BOTTLENECK REGISTER**

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link — Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes — Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** — you have evidence and did not cite it |
| **FM-B** (fail) | No — Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** — you had the token and did not use it |
| **PM-1** (pass) | Yes — Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description | **Full credit** |
| **PM-2** (pass) | No — Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object). "Approval takes too long" is a fail.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail.

---

**STEP 10 — GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits.
- **Why Required**: cite a regulatory rule, handoff precondition (name the downstream state), or system dependency. "Best practice" does not qualify — example fail: "improves audit trail."
- **Risk if Absent**: name the consequence — SLA breach exposure (name the phase), compliance failure (name the regulation), or state inconsistency. "May cause issues" is a fail.

---

**STEP 11 — CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 — EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists. Declare full coverage explicitly if it applies — silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 — BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). See FIELD CONTENT RULES for `Net Change`.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]." "Improved" is a fail.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 1: All roles domain-qualified. At least one Exception Handler = Y.
- [ ] Step 5: Every Handler (R-ID) traces to a role with Exception Handler = Y. Column header constraint read before filling any Handler cell.
- [ ] Step 6: Every S-ID and E-ID ends at a named T-ID. No unterminated branches.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: No FM-A or FM-B conditions in any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency. Risk if Absent names a consequence.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff with acceptance condition named.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.

**Production gate**: Writing this artifact while any checklist item is unchecked is a structural fail, and that artifact must be discarded.

---

## V-03 — Phrasing Register Axis: Three-Element Causal Gate Sentence

**Variation axis:** The production gate is written as a single declarative sentence with three explicit inline elements: failure consequence, domain-specific causal clause naming what the violating artifact contains or lacks, and remediation action. C-26 is absent — Handler constraint appears in a preamble block (not in the column header) to isolate the causal-gate-language axis from the Handler-header axis.

**Hypothesis:** V-01 satisfies C-25 by reference to a scan table's Defect Type column; V-03 satisfies it by direct inline statement in the gate sentence. If an author reads the gate before writing, V-03's causal clause is immediately visible without requiring a scan table lookup. If an author writes first and reviews the gate as a post-hoc check, V-01's scan table delivers more per-check specificity. Testing both delivery mechanisms determines whether inline gate language or structured scan table architecture produces higher compliance.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below — it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify — example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" — no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" — no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" — no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" — no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" — no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" — no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" — no classification, no location for shifted |

---

**STEP 1 — DOMAIN ROLE REGISTRY**

Name every domain role this lifecycle requires. Use the functional title the process actually uses — not org-chart categories. Every decision gate in Step 3, every Handler cell in Step 5, and every owner in Step 12 references R-IDs from this table.

Every Handler (R-ID) entry in the Exception Catalog must resolve to a role carrying Exception Handler = Y in this table. Pre-certify which roles hold exception-handling authority here so that backward verification is possible: if a Handler cell names a role, that role must carry Y or the entry is a fail.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned | Exception Handler (Y/N) |
|------|------------------------------|--------|-----------------|------------------------|
| R-01 | | | | |
| R-02 | | | | |
| ... | | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. At least one role must carry Exception Handler = Y.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete and at least one role carries Exception Handler = Y.

---

**STEP 2 — PHASE MAP**

Name every lifecycle phase before writing any states. Each phase has a named entry trigger and a named completion condition.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

> **GATE B**: Do not open the State Trace until the Phase Map is complete with a named entry trigger and completion condition per phase.

---

**STEP 3 — STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** — at least 3. Each must name condition, owner role, measurable threshold, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** — trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 — PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration — e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 — EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`. Every Handler (R-ID) must resolve to a role carrying Exception Handler = Y in the Role Registry (Step 1). A Handler cell that references a role carrying N, or that is blank, is a fail.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|----------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered. "May cause delays" is a fail — no phase, no magnitude.

---

**STEP 6 — TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 — EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for — distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level. "May affect timing" is a fail — no Ph-ID, no magnitude.

---

**STEP 8 — SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration — complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies — complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT`: skip Tables 8a and 8b. Carry the token to every Breach Link cell in Step 9. Do not leave those cells blank.
- If SLA evidence applies: complete both tables.

**Table 8a — SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b — Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y — name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a traceable cause.

---

**STEP 9 — BOTTLENECK REGISTER**

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link — Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes — Tables 8a/8b completed | Used general language instead of a typed ID | **Fail** — you have evidence and did not cite it |
| **FM-B** (fail) | No — `SLA-ABSENT` declared | Left cell blank instead of writing `SLA-ABSENT` | **Fail** — you had the token and did not use it |
| **PM-1** (pass) | Yes — Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description | **Full credit** |
| **PM-2** (pass) | No — `SLA-ABSENT` declared | Wrote `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object). "Approval takes too long" is a fail.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail.

---

**STEP 10 — GAP REGISTER**

At least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits.
- **Why Required**: cite a regulatory rule, handoff precondition (name the downstream state), or system dependency. "Best practice" does not qualify — example fail: "improves audit trail."
- **Risk if Absent**: name the consequence — SLA breach exposure (name the phase), compliance failure (name the regulation), or state inconsistency. "May cause issues" is a fail.

---

**STEP 11 — CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 — EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists. Declare full coverage explicitly if it applies — silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 — BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants. See FIELD CONTENT RULES for `Net Change`.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]." "Improved" is a fail.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 1: All roles domain-qualified. At least one Exception Handler = Y.
- [ ] Step 5: Every Handler (R-ID) traces to a role with Exception Handler = Y. No blank Handler cells.
- [ ] Step 6: Every S-ID and E-ID ends at a named T-ID. No unterminated branches.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: No FM-A or FM-B conditions in any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency. Risk if Absent names a consequence.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.

**Production gate**: Writing this artifact while any checklist item is unchecked is a structural fail — it produces a lifecycle trace where at least one path reaches no named terminal state or at least one exception flow maps to a handler not pre-certified in the Role Registry — and that artifact must be discarded and rebuilt from the failing step.

---

## V-04 — Combined: Scan Table + Handler Header Embedding

**Variation axis:** Combines V-01 (Scan Table Architecture) and V-02 (Exception Handler Column-Header Pre-Certification). The completion checklist is replaced by the SC-01 through SC-05 Scan Table; the Handler column header embeds the backward-trace enforcement rule inline. Both C-25 (via scan table gate reference) and C-26 (via Handler column header) are present. Formal register throughout.

**Hypothesis:** V-01 satisfies C-25 (scan table provides defect-type specificity at gate time) but leaves C-26 as preamble-only enforcement. V-02 satisfies C-26 (Handler header at point-of-use) but leaves C-25 absent from the gate. V-04 tests whether the two mechanisms are complementary — the scan table making the artifact-consequence chain visible at completion time, the Handler header making the certification constraint visible at authoring time. If both produce higher compliance than either alone, the combination is the preferred structural form.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below — it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify — example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" — no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" — no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" — no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" — no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" — no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" — no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" — no classification, no location for shifted |

---

**STEP 1 — DOMAIN ROLE REGISTRY**

Name every domain role this lifecycle requires. Use the functional title the process actually uses — not org-chart categories. Every decision gate in Step 3, every Handler cell in Step 5, and every owner in Step 12 references R-IDs from this table.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned | Exception Handler (Y/N) |
|------|------------------------------|--------|-----------------|------------------------|
| R-01 | | | | |
| R-02 | | | | |
| ... | | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. At least one role must carry Exception Handler = Y — this designation is what authorizes an R-ID to appear in the Handler column of the Exception Catalog.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete and at least one role carries Exception Handler = Y.

---

**STEP 2 — PHASE MAP**

Name every lifecycle phase before writing any states.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

> **GATE B**: Do not open the State Trace until the Phase Map is complete with a named entry trigger and completion condition per phase.

---

**STEP 3 — STATE TRACE**

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** — at least 3. Each must name condition, owner role, measurable threshold, all outcome branches, and a fallback path.

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** — trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 — PHASE EXIT GATES**

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration — e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 — EXCEPTION CATALOG**

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) — Must trace to a role with Exception Handler = Y in the Role Registry — Mandatory; blank or uncertified role is a fail | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered. "May cause delays" is a fail — no phase, no magnitude.

---

**STEP 6 — TERMINAL DECLARATION**

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 — EDGE CASE CATALOG**

Edge cases are scenarios the lifecycle design has no path for — distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), the directional magnitude, and breach level classification. "May affect timing" is a fail.

---

**STEP 8 — SLA ANNOTATION AND BREACH VERDICTS**

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration — complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies — complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT`: skip Tables 8a and 8b. Carry the token to every Breach Link cell in Step 9.
- If SLA evidence applies: complete both tables.

**Table 8a — SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b — Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y — name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a traceable cause.

---

**STEP 9 — BOTTLENECK REGISTER**

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link — Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes — Tables 8a/8b completed | Used general language instead of a typed ID | **Fail** — you have evidence and did not cite it |
| **FM-B** (fail) | No — `SLA-ABSENT` declared | Left cell blank instead of writing `SLA-ABSENT` | **Fail** — you had the token and did not use it |
| **PM-1** (pass) | Yes — Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description | **Full credit** |
| **PM-2** (pass) | No — `SLA-ABSENT` declared | Wrote `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object). "Approval takes too long" is a fail.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail.

---

**STEP 10 — GAP REGISTER**

At least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits.
- **Why Required**: cite a regulatory rule, handoff precondition (name the downstream state), or system dependency. "Best practice" does not qualify.
- **Risk if Absent**: name the consequence — SLA breach exposure (name the phase), compliance failure (name the regulation), or state inconsistency. "May cause issues" is a fail.

---

**STEP 11 — CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 — EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists. Declare full coverage explicitly if it applies — silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 — BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants. See FIELD CONTENT RULES for `Net Change`.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]." "Improved" is a fail.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Scan Summary — complete every row before writing the artifact:**

| SC-ID | Section | Verification Criterion | Defect Type if OPEN | Artifact Consequence | Status |
|-------|---------|------------------------|---------------------|---------------------|--------|
| SC-01 | Role Registry | Every role has a domain-qualified title; ≥3 R-IDs; at least one Exception Handler = Y | Generic role present or no Y-certified handler | Decision gates in the artifact cite unresolvable owners; exception paths have no certified handler | OPEN / CLOSED |
| SC-02 | Exception Catalog | Every Handler (R-ID) traces to a role with Exception Handler = Y — verified against Role Registry | Uncertified handler (carries N or absent from registry) | At least one exception path in the artifact has no accountable handling owner | OPEN / CLOSED |
| SC-03 | Terminal Declaration | Every traced path (S-ID and E-ID) ends at a named T-ID | Unterminated branch | At least one path in the artifact reaches no named conclusion — the trace is operationally incomplete | OPEN / CLOSED |
| SC-04 | Bottleneck Register | Every Breach Link is PM-1 or PM-2; no FM-A or FM-B | FM-A or FM-B violation | Breach analysis in the artifact is disconnected from SLA evidence | OPEN / CLOSED |
| SC-05 | Gap Register | Every Why Required cites a specific rule, dependency, or regulation | "Best practice" in Why Required | Gap requirement in the artifact is unverifiable | OPEN / CLOSED |

**Production gate**: Writing this artifact while any Scan Summary row shows OPEN status is a structural fail — it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unterminated path, an uncertified exception handler, an unresolvable decision owner, or a breach analysis disconnected from SLA evidence) — and that artifact must be discarded and rebuilt from the failing step.

---

## V-05 — Combined All Three + Lifecycle Emphasis: Per-Step Scope Annotations

**Variation axis:** Combines V-02 (Handler Column-Header Pre-Certification), V-03 (Three-Element Causal Gate Sentence), and a fourth axis — per-step **SCOPE** annotations. Each step opens with a blockquote that names: the minimum output this step produces, which downstream steps depend on it, and what structural defect appears in the artifact if this step is under-filled. The SCOPE annotations make the inter-step dependency chain explicit at each authoring moment rather than concentrating all enforcement at the production gate.

**Hypothesis:** V-03's causal gate sentence and V-02's Handler header each enforce at a single point (gate write time and Handler cell fill time respectively). The SCOPE annotations propagate awareness of artifact consequences to every step boundary, creating a distributed enforcement effect. An author who reads the Step 5 SCOPE before opening the Exception Catalog already knows that uncertified Handler cells produce an artifact with unaccountable exception paths — the same warning that SC-02 delivers in V-01/V-04 and the same warning the Handler header delivers in V-02/V-04. V-05 tests whether distributed SCOPE enforcement produces higher per-step compliance than concentrated gate enforcement alone.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below — it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step before filling it.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify — example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" — no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" — no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" — no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" — no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" — no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" — no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" — no classification, no location for shifted |

---

**STEP 1 — DOMAIN ROLE REGISTRY**

> **SCOPE**: Produces the role vocabulary for the entire trace. Every decision gate in Step 3, every Handler cell in Step 5, and every owner in Steps 4, 9, and 12 references R-IDs from this table. Roles that are not domain-qualified produce a trace where decision ownership is unverifiable and exception authority is uncertified.

Name every domain role this lifecycle requires. Use the functional title the process actually uses — not org-chart categories.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned | Exception Handler (Y/N) |
|------|------------------------------|--------|-----------------|------------------------|
| R-01 | | | | |
| R-02 | | | | |
| ... | | | | |

Generic labels (User, Approver, Admin, Finance team) are a fail. At least one role must carry Exception Handler = Y.

> **GATE A**: Do not open the Phase Map until the Role Registry is complete and at least one role carries Exception Handler = Y.

---

**STEP 2 — PHASE MAP**

> **SCOPE**: Produces the phase vocabulary that the State Trace (Step 3), Phase Exit Gates (Step 4), Bottleneck Register (Step 9), Gap Register (Step 10), and Exception Coverage Audit (Step 12) all reference by Ph-ID. A phase without a named entry trigger produces a State Trace where the first state in that phase cannot be verified as correctly reached. A phase without a named completion condition produces exit gates that cannot be evaluated.

Name every lifecycle phase before writing any states.

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|------------|---------------|---------------------|--------------|-------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| ... | | | | | |

> **GATE B**: Do not open the State Trace until the Phase Map is complete with a named entry trigger and completion condition per phase.

---

**STEP 3 — STATE TRACE**

> **SCOPE**: Produces the named states and decision points that the Terminal Declaration (Step 6), Exception Catalog (Step 5), and Bottleneck Register (Step 9) cite by S-ID. States without named entry conditions produce a trace where transition logic is incomplete. Decision points without named owners produce an artifact where accountability cannot be verified.

Trace at least 6 distinct named states. Every state answers three questions: how did I get here, what happens here, and how do I leave?

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) |
|------|--------------|------------|-----------------|---------------------------|--------------|
| S-01 | | | | | |
| S-02 | | | | | |
| ... | | | | | |

**Decision Points** — at least 3. Each must name condition, owner role, measurable threshold, all outcome branches, and a fallback path. A decision point that omits the owner role is a partial fail.

| D-ID | Decision | Condition (measurable threshold) | Owner (R-ID) | Branch A | Branch B | Fallback |
|------|----------|---------------------------------|--------------|----------|----------|----------|
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |

**Parallel Paths** — trace at least one fork-join with an explicit join condition. State absence explicitly if none applies.

```
Fork (S-ID):    [branching state]
Branch A:       [concurrent path]
Branch B:       [concurrent path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
```

---

**STEP 4 — PHASE EXIT GATES**

> **SCOPE**: Produces the SLA envelopes that Step 8 annotates and Step 9 cites via Breach Link. A phase exit gate without a named SLA envelope produces an artifact where the Bottleneck Register cannot establish whether a delay constitutes a breach.

For each phase, declare the exit gate.

```
Phase:          [Ph-ID: Phase Name]
Exit condition: [what must be true for this phase to complete]
SLA envelope:   [target duration — e.g., "2 business days"]
Success:        [Ph-ID or T-ID]
Failure:        [T-ID or exception name]
Blocked by:     [specific role, system, or condition most likely to prevent exit]
```

---

**STEP 5 — EXCEPTION CATALOG**

> **SCOPE**: Produces the exception record that the Terminal Declaration (Step 6) and Exception Coverage Audit (Step 12) verify against. Exception flows without a certified Handler (R-ID) produce an artifact where at least one exception path has no accountable owner — every E-ID that reaches a terminal must trace back through a Handler role carrying Exception Handler = Y in the Role Registry.

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Handler (R-ID) — Must trace to a role with Exception Handler = Y in the Role Registry — Mandatory; blank or uncertified role is a fail | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|---------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered. "May cause delays" is a fail — no phase, no magnitude.

---

**STEP 6 — TERMINAL DECLARATION**

> **SCOPE**: Produces the terminal registry. Every S-ID and E-ID in the trace must reach a T-ID named here. An artifact written before every path is terminated produces a lifecycle trace with open-ended branches — operationally incomplete. The production gate blocks writing until this step is fully closed.

Every branch in the trace, including all exception paths, must reach a named terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| T-02 | | | |
| ... | | | |

At least 1 success terminal and 1 failure or cancel terminal.

---

**STEP 7 — EDGE CASE CATALOG**

> **SCOPE**: Produces the catalog of unhandled scenarios distinct from Step 5 exceptions. Edge cases without named SLA Risk produce an artifact where the process design's exposure to timing failure is underreported. These entries inform Gap Register (Step 10) and Cross-Lifecycle Handoff (Step 11).

Edge cases are scenarios the lifecycle design has no path for — distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level. "May affect timing" is a fail — no Ph-ID, no magnitude.

---

**STEP 8 — SLA ANNOTATION AND BREACH VERDICTS**

> **SCOPE**: Produces the SLA evidence record that Step 9 Breach Link cells must cite. Declaring `SLA-ABSENT` here authorizes that token in Step 9. Having SLA evidence here without completing Tables 8a and 8b produces an FM-A failure in Step 9. This step must be completed before Step 9 can be filled correctly.

**DEFINED TOKENS:**

| Token | Meaning | Applies when |
|-------|---------|--------------|
| `SLA-ABSENT` | No SLA envelopes are defined for this lifecycle; the breach-link dependency in Step 9 cannot be satisfied by design | Use when this lifecycle has no contractual, operational, or regulatory SLA targets. Must include a reason: `SLA-ABSENT: [reason]`. |

**SLA Status Declaration — complete before opening any SLA table:**

```
SLA status:  [ ] SLA evidence applies — complete Tables 8a and 8b below
             [ ] SLA-ABSENT: [one sentence: why no SLA envelopes are defined for this lifecycle]
```

- If `SLA-ABSENT`: skip Tables 8a and 8b. Carry the token to every Breach Link cell in Step 9. Do not leave those cells blank.
- If SLA evidence applies: complete both tables.

**Table 8a — SLA Annotations** (complete only if SLA evidence applies):

| SLA-ID | S-ID or Ph-ID | Node Name | Target Duration | At-Risk? (Y/N) | Risk Cause |
|--------|--------------|-----------|-----------------|----------------|------------|
| SLA-01 | | | | | |
| SLA-02 | | | | | |
| SLA-03 | | | | | |

At least 3 rows; at least 1 At-Risk = Y with a causal reference to a specific bottleneck.

**Table 8b — Breach Verdicts** (complete only if SLA evidence applies):

| BV-ID | Phase (Ph-ID) | SLA Threshold | Breach (Y/N) | Cause (if Y — name a specific bottleneck condition or E-ID) |
|-------|--------------|---------------|--------------|-------------------------------------------------------------|
| BV-01 | | | | |
| BV-02 | | | | |

At least 1 breach = Y verdict with a traceable cause.

---

**STEP 9 — BOTTLENECK REGISTER**

> **SCOPE**: Produces the bottleneck record that Step 13 Bottleneck Trajectory extends. Breach Link cells that use general language instead of typed IDs (FM-A) or that are blank when `SLA-ABSENT` was declared (FM-B) produce an artifact where breach analysis is disconnected from SLA evidence. Every B-ID in this table must appear in Step 13.

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link — Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes — Tables 8a/8b completed | Used general language instead of a typed ID | **Fail** — you have evidence and did not cite it |
| **FM-B** (fail) | No — `SLA-ABSENT` declared | Left cell blank instead of writing `SLA-ABSENT` | **Fail** — you had the token and did not use it |
| **PM-1** (pass) | Yes — Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description | **Full credit** |
| **PM-2** (pass) | No — `SLA-ABSENT` declared | Wrote `SLA-ABSENT` | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object). "Approval takes too long" is a fail.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail.

---

**STEP 10 — GAP REGISTER**

> **SCOPE**: Produces the gap record identifying missing controls, checks, or steps in the lifecycle design. Why Required cells that cite "best practice" produce an artifact where the gap requirement is unverifiable — there is no named rule or dependency an auditor can check. Risk if Absent cells that use general language produce an artifact where the consequence cannot be tied to a specific compliance or SLA exposure.

At least 1 gap.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits.
- **Why Required**: cite a regulatory rule, handoff precondition (name the downstream state), or system dependency. "Best practice" does not qualify — example fail: "improves audit trail."
- **Risk if Absent**: name the consequence — SLA breach exposure (name the phase), compliance failure (name the regulation), or state inconsistency. "May cause issues" is a fail.

---

**STEP 11 — CROSS-LIFECYCLE HANDOFF**

> **SCOPE**: Produces the handoff record identifying where this lifecycle passes control or data to another process. Missing acceptance conditions produce an artifact where the receiving process cannot verify it received complete inputs — the handoff is structurally open-ended.

At least 1 cross-lifecycle dependency.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 — EXCEPTION COVERAGE AUDIT**

> **SCOPE**: Produces the phase-level exception coverage map. Phases with Handler Exists = N produce an artifact where that phase has no recovery path for exceptions — any exception in that phase terminates without resolution. If every phase is covered, declare full coverage explicitly; silence is not a declaration of coverage.

For every phase in Step 2, confirm whether an exception handler exists.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Handler R-ID | Risk if Uncovered |
|-------|------------|----------------------|--------------|------------------|
| PH-01 | | | | |
| PH-02 | | | | |
| ... | | | | |

---

**STEP 13 — BOTTLENECK TRAJECTORY**

> **SCOPE**: Produces the bottleneck trajectory record closing the loop on Step 9. Net Change cells that classify as "Improved" without naming a location or mechanism produce an artifact where bottleneck resolution cannot be verified against a future process state. Every B-ID from Step 9 must appear here.

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). See FIELD CONTENT RULES for `Net Change`. If only a single process state applies, declare it explicitly.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]." "Improved" is a fail.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 1: All roles domain-qualified. At least one Exception Handler = Y.
- [ ] Step 5: Every Handler (R-ID) traces to a role with Exception Handler = Y. Column header constraint read before filling any Handler cell. No blank Handler cells.
- [ ] Step 6: Every S-ID and E-ID ends at a named T-ID. No unterminated branches.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: No FM-A or FM-B conditions in any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency. Risk if Absent names a consequence.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared. Every B-ID from Step 9 is present.
- [ ] Step 11: At least 1 cross-lifecycle handoff with acceptance condition named.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.

**Production gate**: Writing this artifact while any checklist item is unchecked is a structural fail — it produces a lifecycle trace where at least one path reaches no named terminal state or at least one exception flow maps to a handler not pre-certified in the Role Registry — and that artifact must be discarded and rebuilt from the failing step.

---

## Variation matrix

| Variation | Axis | C-25 | C-26 | Key structural change |
|-----------|------|------|------|-----------------------|
| V-01 | Output Format | PRESENT | ABSENT | Scan Table (SC-01–SC-05) replaces completion checklist; gate names defect types via table reference |
| V-02 | Role Sequence | ABSENT | PRESENT | Handler column header embeds backward-trace rule; plain gate (consequence + remediation only) |
| V-03 | Phrasing Register | PRESENT | ABSENT | Three-element causal gate sentence: consequence + two named defect types + remediation |
| V-04 | V-01 + V-02 | PRESENT | PRESENT | Scan Table + Handler header; two enforcement mechanisms at different authoring moments |
| V-05 | All three + Lifecycle Emphasis | PRESENT | PRESENT | Handler header + causal gate + per-step SCOPE annotations at all 13 steps |

**C-25 delivery methods across passing variations:**
- V-01/V-04: via scan table reference ("defect named in the Defect Type column")
- V-03/V-05: via direct inline causal clause ("produces a trace where at least one path reaches no named terminal state or at least one exception flow maps to a handler not pre-certified")

**C-26 delivery:** consistent across V-02/V-04/V-05 — `Handler (R-ID) — Must trace to a role with Exception Handler = Y in the Role Registry — Mandatory; blank or uncertified role is a fail` embedded as the column header label.

---

*Saved: `simulations/quest/golden/flow-lifecycle-variate-R8-2026-03-15.md`* (R8 designation used to preserve the existing R7 file, which targets a different internal rubric version.)
