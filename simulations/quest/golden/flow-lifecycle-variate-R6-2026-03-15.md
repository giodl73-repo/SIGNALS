---
skill: flow-lifecycle
round: 6
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v25-2026-03-15.md
---

# flow-lifecycle -- Round 6 Variations

Round 6 targets the two new v25 aspirational criteria extracted from R5 excellence signals:
- **C-19 Per-Field Dimensional Enforcement** -- every structured field in a required multi-field output carries both positive bounds (what category of answer qualifies) and a negative boundary (what is insufficient). R5 V-01-V-04 had C-17 partial passes because "Why Required" lacked category guidance; V-05 fixed this for Gap Register. C-19 generalizes the pattern: dimensional enforcement must extend to every structured field across all steps -- Step 5 SLA Impact, Step 7 SLA Risk, Step 9 Cause and Downstream Impact, Step 13 Net Change.
- **C-20 Escape Valve Dual-Failure Path Declaration** -- the escape valve section names both failure modes explicitly: (a) has SLA evidence but used general language, (b) lacks SLA evidence but left blank. R5 V-01-V-04 merged these into a single "empty or general = fail" bucket; V-05 bifurcated them in prose. R6 explores alternate formats for expressing the bifurcation.

**R5 V-05 baseline under v25**: 150/150. C-19 PASS (Gap Register Why Required and Risk if Absent have dimensional bounds; Missing Step has positive example). C-20 PASS (Step 9 prose names both failure modes co-located in one block). Other fields (Step 5 SLA Impact, Step 7 SLA Risk, Step 9 Cause and Downstream Impact, Step 13 Net Change) have partial dimensional guidance but no consistent negative-example enforcement -- potential ceiling under stricter C-19 application.

**R6 challenge**: Apply C-19 dimensional enforcement to all structured fields, not only Gap Register. Explore whether C-20 dual-failure is clearer as a formal table vs. prose bifurcation. All 5 variations should target 150/150 under v25.

Single-axis variations: V-01 (C-19 Global Field Catalog), V-02 (C-20 Two-Failure-Mode Table), V-03 (C-19 Per-Step Inline Expansion).
Combined variations: V-04 (V-01 + V-02: Global Catalog + Dual-Failure Table), V-05 (all R6 axes + full R5 carry-forward: complete R6 maximum candidate).

---

## V-01 -- C-19 Axis: Global Field Content Catalog

**Variation axis:** A **FIELD CONTENT RULES** reference block is placed immediately before Step 1. It catalogs every structured field across all steps that carries dimensional constraints -- listing the positive category bounds ("qualifies when...") and at least one disqualifying example for each. Steps that own those fields carry a back-reference: "See FIELD CONTENT RULES." Dimensional enforcement moves out of the step body into a single front-loaded reference that authors consult once and carry through.

**Hypothesis:** C-19's partial-pass trap is that some fields get dimensional guidance and others do not -- an author reading step-by-step encounters inconsistent instruction density. A global catalog ensures no field can be missed: every constrained field is listed before any table is opened. The catalog also makes C-19 auditable: an evaluator can check the catalog against the criterion in one pass. C-20 dual-failure is preserved from R5 V-05 via prose bifurcation at Step 9.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below -- it defines the content standards for every structured field that carries dimensional constraints. Steps that use those fields include a back-reference.

---

**FIELD CONTENT RULES**

The following fields carry explicit dimensional constraints. Every field listed here requires both a positive answer (the category of content that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days or hours), and whether the breach threshold is triggered (e.g., "adds 3+ days to PH-02 PO Approval; triggers breach threshold") | "May cause delays" -- no phase named, no magnitude |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level (e.g., "puts PH-03 Day-5 SLA at risk; breach likely if concurrent with volume peak") | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name the gate), role dependency (name the role), external system (name the system), or data dependency (name the data object) | "Approval takes too long" -- type not named, element not named |
| Downstream Impact | Step 9 | Names the specific subsequent states or phases affected (by S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states or phases named, no consequence type |
| Breach Link | Step 9 | Typed reference to a specific BV-ID, SLA-ID, or Ph-ID from Step 8 (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`), OR the token `SLA-ABSENT: [reason]` when no Step 8 evidence was traced | Empty cell or "causes delays in this phase" -- no typed reference, no token |
| Why Required | Step 10 | Cites a regulatory rule (name the rule), a handoff precondition (name the downstream state that requires the step's output), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no specific rule or dependency cited |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state) | "May cause issues" or "could lead to problems" -- no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name the new location) / residual (state why it persists) / or "Single-state: [reason]" if no variant comparison applies | "Improved" or "better" -- no classification, no location for shifted |

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

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path.

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

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

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

At least 2 edge cases distinct from Step 5 exceptions. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

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

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link column -- three outcomes only:**

If you have SLA evidence from Step 8 (Tables 8a and 8b completed): every Breach Link cell must reference a specific Phase Exit Gate (Ph-ID), SLA annotation row (SLA-ID), or breach verdict row (BV-ID) by typed ID. Example: `BV-01: PH-02 breach = Y, caused by manual queue`. A typed reference is the only way to earn full credit.

If Step 8 declared `SLA-ABSENT`: carry the token to each Breach Link cell. Write `SLA-ABSENT` -- the reason is in Step 8. This earns absence credit.

Empty cell, or a general statement like "causes delays in approval" or "see SLA section": fail, no credit. If you have SLA evidence and leave the cell general, it fails C-16. If you have no SLA evidence and leave the cell blank instead of using `SLA-ABSENT`, it also fails.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). See FIELD CONTENT RULES for `Net Change`. If only a single process state applies, declare it explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Every Breach Link cell carries a typed ID OR `SLA-ABSENT`. No blank cells, no general statements.
- [ ] Step 9: Every Cause entry names a root-cause type. Every Downstream Impact names specific phases.
- [ ] Step 5: Every SLA Impact satisfies FIELD CONTENT RULES (phase, magnitude, breach flag).
- [ ] Step 7: Every SLA Risk satisfies FIELD CONTENT RULES (specific threshold, directional consequence).
- [ ] Step 10: Every gap has all three fields with specific content per FIELD CONTENT RULES.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; uncovered phases named with risk consequence.

Any unchecked item is a fail.

---

## V-02 -- C-20 Axis: Two-Failure-Mode Outcome Table at Step 9

**Variation axis:** The three-way outcome prose at Step 9 (Breach Link) is replaced with a formal **Outcome Conditions** table with four rows: two failure modes (FM-A, FM-B) and two passing modes (PM-1, PM-2). Each row states the SLA-evidence condition that determines which mode applies. FM-A names the over-specific failure (has evidence, used general language). FM-B names the under-specific failure (no evidence, left blank). Both failure modes are co-located in the table -- an author filling in the column sees both paths in a single glance rather than searching prose.

**Hypothesis:** R5 V-05 passes C-20 via prose bifurcation at the bottom of the Step 9 instruction block. Authors who skim the step and open the table without reading the full block may miss the bifurcation. A four-row table forces both failure modes into a scannable format inseparable from the schema. The structural pairing (FM-A above FM-B) directly mirrors C-20's co-location requirement. C-19 is met via Gap Register field rules from R5 V-05 (minimum viable: Why Required and Risk if Absent carry bounds).

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Step 8 establishes SLA vocabulary and your lifecycle's SLA status. Step 9 consumes those tokens and enforces the Breach Link column via the Outcome Conditions table. Step 10 uses a three-field gap schema with per-field content rules. These rules interact: read each step's instructions before filling it.

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

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path.

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

For each phase, declare the exit gate. SLA envelope is required and will be referenced in Step 8 breach verdicts and Step 9 Breach Link entries.

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

At least 3 exceptions. The `SLA Impact` field is required on every row. State the timing consequence directionally (e.g., "adds 3+ days to PH-02 PO Approval; triggers breach threshold"). "May cause delays" is a fail.

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

At least 2 edge cases distinct from Step 5 exceptions. The `SLA Risk` field must name the specific phase SLA or timing threshold at risk and give a directional consequence (e.g., "puts PH-03 Day-5 SLA at risk; breach likely if concurrent with volume peak"). "May affect timing" is a fail.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

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

**Breach Link -- Outcome Conditions:**

Before filling the Breach Link column, identify your SLA evidence status from Step 8, then follow the matching row:

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: evidence present, not cited |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: token available, not used |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, manual queue cause`) | **Full credit** |
| **PM-2** (pass) | No -- Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

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
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" is a fail.

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). If only a single process state applies, declare it explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Identified SLA evidence status. No FM-A or FM-B conditions apply to any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase and magnitude. "May cause delays" does not appear.
- [ ] Step 7: Every SLA Risk names a specific threshold and directional consequence.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; uncovered phases named with risk consequence.
- [ ] Step 13: Trajectory complete or absence declared with reason.

Any unchecked item is a fail.

---

## V-03 -- C-19 Axis: Per-Step Inline Dimensional Expansion

**Variation axis:** C-19 dimensional enforcement is expanded inline within every step that contains structured multi-field outputs -- not consolidated in a global block. Steps 5, 7, 9, and 13 each receive a **Field rules** subsection directly beneath the table schema, mirroring the treatment already present at Step 10. This ensures every structured field carries both positive bounds and a disqualifying example at the point of authoring, without requiring recall from a front-loaded block read earlier in the session.

**Hypothesis:** Authors who read step-by-step never encounter a globally-declared rule for a field they haven't reached yet. Inline placement activates dimensional guidance at the exact moment of authoring -- the author reads the table schema, then immediately reads the field rule for the column being filled. This prevents the partial-pass pattern (some fields have guidance, others don't) by making guidance inseparable from the schema. The trade-off is per-step density; the gain is that the prompt is self-contained at every step. C-20 dual-failure is preserved from R5 V-05 via prose bifurcation at Step 9.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Step 8 establishes SLA vocabulary and your lifecycle's SLA status. Step 9 consumes those tokens. Step 10 uses a three-field gap schema. Each step contains the field rules for its own outputs.

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

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path.

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

At least 3 exceptions.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase affected (Ph-ID), the timing magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered (e.g., "adds 3+ days to PH-02 PO Approval; triggers breach threshold"). All three elements are required. Example fail: "may cause delays" -- no phase, no magnitude, no breach flag.

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

At least 2 edge cases distinct from Step 5 exceptions.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level (e.g., "puts PH-03 Day-5 SLA at risk; breach likely if concurrent with volume peak"). Example fail: "may affect timing" -- no Ph-ID, no magnitude.

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

If you have SLA evidence from Step 8 (Tables 8a and 8b completed): every Breach Link cell must reference a specific Phase Exit Gate (Ph-ID), SLA annotation row (SLA-ID), or breach verdict row (BV-ID) by typed ID. Example: `BV-01: PH-02 breach = Y, caused by manual queue`. A typed reference is the only way to earn full credit.

If Step 8 declared `SLA-ABSENT`: carry the token to each Breach Link cell. Write `SLA-ABSENT` -- the reason is in Step 8. This earns absence credit.

Empty cell, or a general statement like "causes delays in approval" or "see SLA section": fail, no credit. If you have SLA evidence and leave the cell general, it fails C-16. If you have no SLA evidence and leave the cell blank instead of using `SLA-ABSENT`, it also fails.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate or approval step), role dependency (name the role that creates the dependency), external system (name the system), or data dependency (name the data object). Example fail: "approval takes too long" -- no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and state the directional consequence (delayed / blocked / skipped). Example fail: "delays the process" -- no states or phases named, no consequence type.

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule or regulation), handoff precondition (name the downstream state that requires the step's output), or system dependency (name the system that fails without the step). "Best practice" does not qualify -- example fail: "improves audit trail" (no specific rule or dependency cited).
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). Example fail: "may cause issues" (no named consequence).

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). If only a single process state applies, declare it explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify the bottleneck outcome as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. Example fail: "improved" -- no classification, no location for shifted.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Every Breach Link cell carries a typed ID OR `SLA-ABSENT`. No blank cells, no general statements.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific states or phases.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; uncovered phases named with risk consequence.

Any unchecked item is a fail.

---

## V-04 -- Combined: V-01 + V-02 (Global Field Catalog + Two-Failure-Mode Table)

**Variation axis (V-01 + V-02):** Combines the FIELD CONTENT RULES global catalog from V-01 -- which covers all structured fields across all steps with both positive bounds and a disqualifying example -- with the formal Outcome Conditions table from V-02 at Step 9. The global catalog satisfies C-19 by making dimensional enforcement complete and exhaustive before Step 1. The Outcome Conditions table satisfies C-20 by placing both failure modes (FM-A and FM-B) in a co-located, scannable structure at the point of authoring the Breach Link column.

**Hypothesis:** V-01 alone closes C-19 but retains prose bifurcation at Step 9 (C-20 passes but the format is less immediately scannable). V-02 alone formalizes C-20 as a table but does not close C-19 for fields outside Step 10. The combination targets both criteria directly: the FIELD CONTENT RULES catalog ensures every constrained field has both positive bounds and a disqualifying example, and the FM-A/FM-B table makes both failure modes impossible to miss at Step 9. Two distinct high-signal reading points (catalog before Step 1, table at Step 9) rather than guidance scattered through step bodies.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below -- it catalogs dimensional constraints for every structured field. Step 9's Breach Link column also uses the **Outcome Conditions** table, which requires you to identify your SLA evidence status before filling that column.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown). Back-references in each step confirm where these rules apply.

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record) | "May cause issues" -- no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

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

**Decision Points** -- at least 3. Each must name condition, owner role, all outcome branches, and a fallback path.

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

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

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

At least 2 edge cases distinct from Step 5 exceptions. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

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

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause` and `Downstream Impact`.

**Breach Link -- Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: evidence present, not cited |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: token available, not used |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, manual queue cause`) | **Full credit** |
| **PM-2** (pass) | No -- Step 8 declared `SLA-ABSENT` | `SLA-ABSENT` (reason declared in Step 8; do not repeat per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). See FIELD CONTENT RULES for `Net Change`. If only a single process state applies, declare it explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 8: `SLA-ABSENT` token defined. SLA Status Declaration filled.
- [ ] Step 9: Identified SLA evidence status. No FM-A or FM-B conditions apply to any Breach Link cell.
- [ ] Step 5: Every SLA Impact satisfies FIELD CONTENT RULES.
- [ ] Step 7: Every SLA Risk satisfies FIELD CONTENT RULES.
- [ ] Step 9: Every Cause and Downstream Impact satisfies FIELD CONTENT RULES.
- [ ] Step 10: Every gap has all three fields per FIELD CONTENT RULES.
- [ ] Step 13: Net Change satisfies FIELD CONTENT RULES for every row.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; uncovered phases named with risk consequence.

Any unchecked item is a fail.

---

## V-05 -- Full Combination: All R6 Axes + Full R5 V-05 Carry-Forward

**Variation axis (V-01 + V-02 + V-03 + R5 V-05 carry-forward):** Combines all three R6 axes -- FIELD CONTENT RULES global catalog (V-01), formal Outcome Conditions table at Step 9 (V-02), and per-step inline Field Rules at Steps 5, 7, 9, 13 (V-03) -- with the complete R5 V-05 carry-forward: token vocabulary block and SLA Status Declaration at Step 8, typed-ID breach link enforcement at Step 9, and the three-field gap schema with field rules at Step 10.

Three layers of C-19 reinforcement: the global catalog sets expectations before any table; the per-step inline rules activate at the moment of authoring; the checklist provides a final self-audit gate. C-20 is expressed via the Outcome Conditions table at Step 9 (FM-A and FM-B co-located, scannable) AND the checklist item requiring the author to confirm no FM-A or FM-B condition applies.

**Hypothesis:** Addresses every possible failure mode for C-19 and C-20 simultaneously: (a) global catalog prevents any field from being unconstrained before Step 1; (b) per-step inline rules prevent recall-failure at authoring time; (c) FM-A/FM-B table makes both failure modes scannable and unavoidable at Step 9; (d) checklist provides a final gate against skipped items. No single failure mode goes unaddressed. Maximum-composite scoring target: 150/150 under v25.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work through every numbered step in order. Before opening any table, read the **FIELD CONTENT RULES** block below -- it catalogs dimensional constraints for every structured field. Steps that own those fields also include inline field rules. Step 8 establishes SLA vocabulary and your lifecycle's SLA status. Step 9 consumes those tokens via the Outcome Conditions table. These rules interact: read each step's instructions before filling it.

---

**FIELD CONTENT RULES**

Every field listed here requires both a positive answer (the category that qualifies) and will fail on a negative answer (the disqualifying example shown).

| Field | Step | Qualifies when... | Does NOT qualify -- example fail |
|-------|------|-------------------|----------------------------------|
| SLA Impact | Step 5 | Names the affected phase (Ph-ID), the timing magnitude (days/hours), and whether the breach threshold is triggered | "May cause delays" -- no phase, no magnitude, no breach flag |
| SLA Risk | Step 7 | Names the specific phase SLA threshold at risk (Ph-ID), states the directional magnitude, and classifies breach level | "May affect timing" -- no Ph-ID, no magnitude |
| Cause | Step 9 | Names the root-cause type: manual gate (name it), role dependency (name the role), external system (name it), or data dependency (name the data object) | "Approval takes too long" -- no type, no named element |
| Downstream Impact | Step 9 | Names the specific states or phases affected (S-ID or Ph-ID) and states the directional consequence (delayed / blocked / skipped) | "Delays the process" -- no states named, no consequence type |
| Breach Link | Step 9 | See Outcome Conditions table in Step 9 | See Outcome Conditions table |
| Why Required | Step 10 | Cites a regulatory rule (name it), a handoff precondition (name the downstream state), or a system dependency (name the system that fails without the step) | "Best practice" or "improves audit trail" -- no rule or dependency |
| Risk if Absent | Step 10 | Names the specific consequence: SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation), or state inconsistency (name the erroneous record or system state) | "May cause issues" -- no named consequence |
| Net Change | Step 13 | Classifies as: eliminated (state why) / shifted (name new location) / residual (state why it persists) / or "Single-state: [reason]" | "Improved" -- no classification, no location for shifted |

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

At least 3 exceptions. See FIELD CONTENT RULES for `SLA Impact`.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | SLA Impact | Terminal or Recovery |
|------|--------------|----------------|---------|--------------------------|------------|---------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |

**Field rules:**
- **SLA Impact**: name the phase (Ph-ID), the magnitude (e.g., "adds 3+ days"), and whether the breach threshold is triggered (e.g., "adds 3+ days to PH-02 PO Approval; triggers breach threshold"). "May cause delays" is a fail -- no phase, no magnitude.

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

Edge cases are scenarios the lifecycle design has no path for -- distinct from Step 5 exceptions. At least 2 required. See FIELD CONTENT RULES for `SLA Risk`.

| EC-ID | Edge Case | Phase (Ph-ID) | Why Unhandled | SLA Risk | Correct Handling |
|-------|-----------|--------------|---------------|----------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |

**Field rules:**
- **SLA Risk**: name the specific phase SLA threshold at risk (Ph-ID), state the directional magnitude, and classify breach level (e.g., "puts PH-03 Day-5 SLA at risk; breach likely if concurrent with volume peak"). "May affect timing" is a fail -- no Ph-ID, no magnitude.

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

At least 2 bottlenecks. See FIELD CONTENT RULES for `Cause`, `Downstream Impact`, and `Breach Link`.

**Breach Link -- Outcome Conditions** (identify your SLA evidence status from Step 8, then follow the matching row):

| Mode | SLA Evidence Present? | Author Action in Breach Link Cell | Verdict |
|------|-----------------------|-----------------------------------|---------|
| **FM-A** (fail) | Yes -- Tables 8a/8b completed | Used general language ("causes delays in approval", "see SLA section") instead of a typed ID | **Fail** -- C-16 violation: you have evidence and did not cite it |
| **FM-B** (fail) | No -- Step 8 declared `SLA-ABSENT` | Left cell blank or empty instead of writing `SLA-ABSENT` | **Fail** -- C-18 violation: you had the token and did not use it |
| **PM-1** (pass) | Yes -- Tables 8a/8b completed | Wrote typed ID reference: `BV-ID`, `SLA-ID`, or `Ph-ID` + brief description (e.g., `BV-01: PH-02 breach = Y, caused by manual queue`) | **Full credit** |
| **PM-2** (pass) | No -- Step 8 declared `SLA-ABSENT` | Wrote `SLA-ABSENT` (reason declared in Step 8; do not repeat it per cell) | **Earned-absence credit** |

| B-ID | Phase (Ph-ID) | Bottleneck Name | Cause | Downstream Impact | Breach Link |
|------|--------------|-----------------|-------|-------------------|-------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Field rules:**
- **Cause**: name the root-cause type: manual gate (name the specific gate), role dependency (name the role), external system (name the system), or data dependency (name the data object). "Approval takes too long" is a fail -- no type, no named element.
- **Downstream Impact**: name the specific states or phases affected (S-ID or Ph-ID) and the directional consequence (delayed / blocked / skipped). "Delays the process" is a fail -- no states named, no consequence type.

---

**STEP 10 -- GAP REGISTER**

At least 1 gap. Every gap entry uses a three-field schema. See FIELD CONTENT RULES for `Why Required` and `Risk if Absent`.

| G-ID | Phase (Ph-ID) | Missing Step | Why Required | Risk if Absent |
|------|--------------|-------------|--------------|----------------|
| G-01 | | | | |

**Field rules:**
- **Missing Step**: name the specific step, check, or control the lifecycle omits (e.g., "Duplicate invoice detection check before AP posting").
- **Why Required**: name the specific dependency -- regulatory rule (cite the rule or regulation), handoff precondition (name the downstream state that requires the step's output), or system dependency (name the system that fails without the step). "Best practice" does not qualify -- example fail: "improves audit trail" (no specific rule or dependency cited).
- **Risk if Absent**: name the consequence -- SLA breach exposure (name the phase), compliance failure (name the audit finding or regulation violated), or state inconsistency (name the erroneous record or system state). "May cause issues" is a fail.

---

**STEP 11 -- CROSS-LIFECYCLE HANDOFF**

At least 1 cross-lifecycle dependency: direction, recipient, fields, and acceptance condition.

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

---

**STEP 12 -- EXCEPTION COVERAGE AUDIT**

For every phase in Step 2, confirm whether an exception handler exists and name the risk consequence for any uncovered phase. If every phase is covered, declare full coverage explicitly -- silence is not coverage.

| Ph-ID | Phase Name | Handler Exists (Y/N) | Risk if Uncovered |
|-------|------------|----------------------|------------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |

---

**STEP 13 -- BOTTLENECK TRAJECTORY**

For each bottleneck in Step 9, trace its status across process variants (as-is vs. to-be). See FIELD CONTENT RULES for `Net Change`. If only a single process state applies, declare it explicitly and explain why.

| B-ID | As-Is State | Target State (or "Single-state: [reason]") | Net Change |
|------|-------------|-------------------------------------------|------------|
| B-01 | | | |
| B-02 | | | |

**Field rules:**
- **Net Change**: classify as: eliminated (state why), shifted (name the new location by S-ID or Ph-ID), residual (state why it persists), or "Single-state: [reason]" if no variant comparison applies. "Improved" is a fail -- no classification, no location for shifted.

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > SLA Annotation > Bottleneck Register > Gap Register > Cross-Lifecycle Handoff > Exception Coverage Audit > Bottleneck Trajectory.

**Completion checklist before writing:**
- [ ] FIELD CONTENT RULES consulted before opening any table.
- [ ] Step 8: `SLA-ABSENT` token defined in Defined Tokens block.
- [ ] Step 8: SLA Status Declaration filled -- either Tables 8a/8b complete, or `SLA-ABSENT: [reason]` declared.
- [ ] Step 9: Identified SLA evidence status. No FM-A or FM-B conditions apply to any Breach Link cell.
- [ ] Step 5: Every SLA Impact names a phase (Ph-ID), magnitude, and breach flag.
- [ ] Step 7: Every SLA Risk names a specific threshold (Ph-ID) and directional consequence.
- [ ] Step 9: Every Cause names a root-cause type and element. Every Downstream Impact names specific phases or states.
- [ ] Step 10: Every gap has all three fields. Why Required cites a rule or dependency (not best practice). Risk if Absent names a consequence.
- [ ] Step 13: Net Change classifies as eliminated / shifted (location named) / residual / or single-state declared.
- [ ] Step 11: At least 1 cross-lifecycle handoff.
- [ ] Step 12: Every phase accounted for; full coverage declared if it applies.

Any unchecked item is a fail.
