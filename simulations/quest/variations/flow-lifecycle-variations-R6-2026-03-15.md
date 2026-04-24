Now I have the full R5 context. Let me see what the R6 rubric is specifically targeting before writing.

Key R6 targets:
- **C-23**: Role Registry must pre-certify exception handler authority (Y/N flag) AND exception catalog handlers must trace only to Y-marked roles (backward verification direction)
- **C-24**: Production gate must include both failure consequence (C-22) AND a remediation action ("must be discarded") inline

R5 V-02 already had the Exception Handler column in the registry. The new pressure is the backward trace enforcement (catalog → registry Y flag). R5 V-03 had "must be discarded" — C-24 is the formalization of that pattern.

---

```markdown
---
skill: flow-lifecycle
round: 6
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v6-2026-03-15.md
---

# flow-lifecycle -- Round 6 Variations

Round 6 targets the two new v6 aspirational criteria, extracted from R5 V-02 and V-03
excellence signals:

- **C-23** Exception Handler Authority Pre-Certification -- the role registry carries an
  explicit exception-handling authority designation for each role (e.g., "Exception Handler
  Y/N" column); handler R-IDs assigned in the exception catalog must trace to roles carrying
  that designation; enables backward verification (registry → exception catalog) rather than
  only forward assignment (exception catalog → registry lookup)
- **C-24** Gate Violation Remediation Instruction -- the production gate failure declaration
  (satisfying C-22) includes an explicit remediation action naming what must be done with
  the violating artifact (e.g., "must be discarded," "must be rerun from the scan step");
  distinct from C-22 (consequence named) by additionally requiring the corrective action

**R5 learning applied to R6 design:**
- R5 V-02 passed C-23 incidentally: Role Registry included an "Exception Handler Y/N"
  column, and exception catalog's Handler (R-ID) column cited only those roles. The backward
  verification direction was implied by the column pair — the registry pre-certified which
  roles were eligible before the catalog was authored. R5 V-01 had no Handler column at all;
  R5 V-03 used prose "Owner: [R-ID]" without registry-level designation.
- R5 V-03 passed C-24 incidentally: "Writing the artifact when Scan Summary is OPEN is a
  structural fail -- the output is an incomplete lifecycle trace where at least one path has
  no named terminal, and it must be discarded." The phrase "must be discarded" is the
  remediation action. R5 V-01 gate stated condition only; R5 V-02 gate stated condition only.
- R6 primary risk for C-23: having the Exception Handler Y/N column in the registry but not
  enforcing the backward trace — the exception catalog may cite any R-ID, not exclusively
  roles marked Y. C-23 requires the catalog to be constrained to Y-marked roles, not just
  require any R-ID from the registry. C-21 handles the forward direction (exception flow
  names an R-ID from the registry); C-23 closes the backward direction (that R-ID must carry
  Y in the handler authority column).
- R6 primary risk for C-24: naming the failure consequence ("is a structural fail") without
  naming the corrective action. A gate that says "is invalid" satisfies C-22. A gate that
  says "is invalid and must not be filed" satisfies C-24. The remediation instruction must
  specify what happens to the artifact — not just characterize the violation.

Single-axis: V-01 (Role sequence: backward handler trace enforcement, C-23 target),
V-02 (Phrasing register: gate remediation instruction, C-24 target),
V-03 (Output format: inline column backward-trace rule, C-23 via schema enforcement).
Combined: V-04 (Role sequence + Phrasing register: C-23 + C-24),
V-05 (all three new axes + full C-18 through C-22 carry-through).

---

## V-01 -- Role Sequence Axis: Backward Handler Trace Enforcement

**Variation axis:** Role sequence. The Role Registry is the first artifact produced and
carries an "Exception Handler" column (Y / N) that pre-certifies which roles hold
exception-handling authority before any exception is authored. A backward trace requirement
is stated explicitly before the Exception Catalog: every Handler (R-ID) cell in the catalog
must resolve to a role marked Y in the registry; citing an N-marked role as an exception
handler is a structural fail. Sequential gates: one gate before the phase table (role
registry completion), one gate before the artifact write (scan CLOSED). The production gate
states the CLOSED requirement without naming a remediation action (C-24 absent).

**Hypothesis:** C-23 requires two conditions: (1) the registry pre-certifies handler
authority via an explicit flag, and (2) the exception catalog is constrained to cite only
Y-marked roles. R5 V-02 demonstrated both conditions incidentally. The risk is that a prompt
with a registry Y/N column but no backward trace enforcement produces a catalog that cites
any R-ID — satisfying C-21 (R-ID from registry) but failing C-23 (R-ID must be from Y row
only). V-01 makes the backward trace constraint explicit immediately before the Exception
Catalog is authored. C-24 is absent (production gate names condition only) to isolate the
C-23 axis.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal.

---

**ROLE REGISTRY**

Domain-qualified roles are established before any phase, state, decision, or exception is
named. This registry pre-certifies which roles may act as exception handlers — that
designation must be recorded here before the Exception Catalog is authored.

| R-ID | Role Name [Mandatory. "Approver," "Owner," "Manager," and "Finance team" are fails -- name the function at a specific desk: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | Decision Authority (measurable threshold -- dollar amount, day count, retry limit; "owns approvals" does not count) | Exception Handler (Y / N) |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles. At least one role must be marked Exception Handler Y. The Y flag means
this role is pre-certified to own exception flows -- only Y-marked roles may appear in the
Handler column of the Exception Catalog.

**Gate 1 [Role Registry -> Phase Table]. Do not proceed to PHASE TABLE until Role Registry
is complete, every role has a domain-qualified title, and the Exception Handler column is
fully populated with Y or N for every row.**

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|-----------|--------------|---------------------|--------------|------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases. Each aggregates >=2 states -- a 1:1 phase-to-state mapping does not
count. At least one At-Risk Threshold names a causal bottleneck.

---

**STATE TABLE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger | Exit Trigger | SLA Window | Risk |
|------|-----------|-------------|-------------|--------------|-------------|-----------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states. Every R-ID cited must exist in the Role Registry.

---

**DECISION TABLE**

| D-ID | Decision Condition (measurable threshold) | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback (owner unavailable / system down / config missing) |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state with rationale and propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Before filling this catalog: verify the Role Registry. Every Handler (R-ID) cell below
must resolve to a role with Exception Handler = Y in the registry. A Handler R-ID that
traces to a role marked N is a structural fail -- that role is not pre-certified for
exception handling authority and cannot own an exception flow.

Minimum 3 exceptions spanning at least 2 distinct phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Divergence S-ID | Handler (R-ID) [Mandatory. Must trace to Exception Handler = Y in the Role Registry. An R-ID from an N-marked role is a structural fail.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact (phase SLA + magnitude + breach-or-delay) |
|------|--------------|---------------|------------------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific) | Downstream Impact |
|------|------|--------------|------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State (S-ID or Ph-ID) | SLA Dependency |
|-------------------|-----------|----------------|-------------------------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate 2 [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

---

## V-02 -- Phrasing Register Axis: Gate Remediation Instruction

**Variation axis:** Phrasing register. The production gate failure declaration (satisfying
C-22) includes an explicit remediation instruction alongside the failure consequence --
naming what must be done with the violating artifact. The gate text template is:
"[Writing condition] is a structural fail -- [what the output is / why it is defective],
and [remediation action for the violating artifact]." The Exception Handler column is absent
from the Role Registry (C-23 absent) -- roles are domain-qualified but no pre-certification
flag is carried. Sequential gates: one gate at artifact production only.

**Hypothesis:** C-24 is the downstream criterion from C-22: a rubric cannot pass C-24
without first passing C-22. Among C-22-passing prompts, C-24 distinguishes those that
include a corrective action from those that only declare a failure. R5 V-03 demonstrated
C-24 incidentally: "and it must be discarded" follows "is a structural fail." V-02 makes
this explicit as a three-part gate template: (1) condition trigger, (2) failure consequence,
(3) remediation action. C-23 is absent to isolate the C-24 phrasing axis.

---

You are a business-process simulation expert. Simulate the complete lifecycle of the
document or process named in the signal.

---

**ROLE REGISTRY**

Domain-qualified roles are the first artifact. No phase, state, or exception may reference
a role not declared here.

| R-ID | Role Name [Mandatory. "Approver," "Owner," "Manager," and "Finance team" are fails -- name the function at a specific desk: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | Decision Authority (measurable threshold) | SLA Accountable |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles.

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope | At-Risk Threshold |
|-------|-----------|--------------|---------------------|--------------|------------------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases, each aggregating >=2 states. At least one At-Risk Threshold names a
causal bottleneck.

---

**STATE TABLE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) | Entry Trigger | Exit Trigger | SLA Window | Risk |
|------|-----------|-------------|-------------|--------------|-------------|-----------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states. Every R-ID cited must exist in the Role Registry.

---

**DECISION TABLE**

| D-ID | Decision Condition (measurable threshold) | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback (owner unavailable / system down / config missing) |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state with rationale and propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 distinct phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition | Divergence S-ID | Handler (R-ID) [Mandatory. Cite a domain-qualified R-ID from the Role Registry. Blank Handler is a fail.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact (phase SLA + magnitude + breach-or-delay) |
|------|--------------|---------------|------------------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific) | Downstream Impact |
|------|------|--------------|------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State (S-ID or Ph-ID) | SLA Dependency |
|-------------------|-----------|----------------|-------------------------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED. Writing the artifact when Scan Summary is OPEN is a structural fail -- the
output is an incomplete lifecycle trace where at least one traced path reaches no named
terminal, and it must be discarded.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

---

## V-03 -- Output Format Axis: Inline Column Backward-Trace Rule

**Variation axis:** Output format. The Exception Catalog schema embeds the backward-trace
rule inline within the Handler column header itself -- not in a preamble block before the
table. The column header text declares that the R-ID cited must trace to a role carrying
Exception Handler Y in the Role Registry, using "is a structural fail" language adjacent to
the cell being constrained. This is C-18-compatible enforcement at the column definition
level. The Role Registry carries the Exception Handler Y/N column (pre-certification is
present). Production gate states condition without remediation action (C-24 absent) to
isolate the C-23-via-schema-enforcement axis from the phrasing axis.

**Hypothesis:** C-23 has two structural components: (a) registry pre-certification via Y/N
flag, and (b) exception catalog constrained to cite only Y-marked roles. V-01 enforces (b)
via a prose instruction block before the catalog. V-03 enforces (b) via the column header
itself -- the constraint is visible at the point of use, not in a preceding paragraph. The
question this variation answers: does inline column-level enforcement (C-18 pattern) produce
stronger C-23 compliance than a pre-table prose instruction, when the registry pre-cert
column is present in both?

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal.

---

**ROLE REGISTRY**

Domain-qualified roles are established before any phase, state, decision, or exception is
named. The Exception Handler column records which roles hold exception-handling authority --
this registry entry pre-certifies handler eligibility before the Exception Catalog is
authored.

| R-ID | Role Name [Mandatory. Generic labels (User, Approver, Owner, Finance team, Management) are fails -- do not use them. Name the specific function: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | Decision Authority [Mandatory. Name decision type and measurable threshold: "PO approval up to $50K," "Invoice exception hold <=3 business days." "Owns approvals" does not count.] | Exception Handler (Y / N) |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles. At least one role marked Exception Handler Y.

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger [Mandatory. "After prior phase" does not count -- name the specific event or artifact state.] | Completion Condition [Mandatory. "When complete" does not count -- name the observable completion signal.] | SLA Envelope | At-Risk Threshold |
|-------|-----------|------|------|------|------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases, each aggregating >=2 states. At least one At-Risk Threshold names a
causal bottleneck.

---

**STATE TABLE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) [Mandatory. Blank is a fail -- every state needs an accountable role.] | Entry Trigger [Mandatory. "Then it moves to" is a fail -- name the actor or system event.] | Exit Trigger [Mandatory. "Then it moves to" is a fail -- name the actor or system event.] | SLA Window | Risk |
|------|-----------|-------------|------|------|------|------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states. Every R-ID cited must exist in the Role Registry.

---

**DECISION TABLE**

| D-ID | Decision Condition [Mandatory. "Large amount" and "needs review" do not count -- name the measurable threshold: dollar amount, day count, retry limit.] | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback [Mandatory. Blank is a structural fail -- name the holding state or escalation path for: owner unavailable, system down, configuration missing.] |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state with rationale and propose one parallelization opportunity naming
roles and states.

---

**EXCEPTION CATALOG**

Minimum 3 exceptions spanning at least 2 distinct phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition [Mandatory. "System error" and "data issue" do not count -- name the specific failure mode in domain terms.] | Divergence S-ID | Handler (R-ID) [Mandatory. Must trace to a role with Exception Handler = Y in the Role Registry. Citing an R-ID marked N is a structural fail -- that role is not pre-certified for exception-handling authority.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact |
|------|--------------|---------------|------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific -- "resource constraints" does not count) | Downstream Impact |
|------|------|--------------|------|----------------------------------------------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State (S-ID or Ph-ID) | SLA Dependency |
|-------------------|-----------|----------------|-------------------------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED.**

---

**OUTPUT**

Only after Scan Summary is CLOSED: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

---

## V-04 -- Combined: Backward Handler Trace + Gate Remediation (C-23 + C-24)

**Variation axes combined:**
1. Role sequence (C-23) -- Role Registry Exception Handler Y/N column pre-certifies handler
   authority; a pre-catalog backward trace check is stated explicitly (catalog Handler R-IDs
   must resolve to Y-marked roles); combines V-01's pre-table instruction with V-03's inline
   column header enforcement
2. Phrasing register (C-24) -- production gate failure declaration names both the failure
   consequence and the corrective remediation action; gate template: condition + "is a
   structural fail" + "and [artifact] must be [remediation action]"

**Hypothesis:** V-01 achieves C-23 via pre-table backward trace instruction (no inline
column enforcement). V-02 achieves C-24 via gate remediation instruction (no registry
pre-certification). V-03 achieves C-23 via inline column backward-trace rule (no remediation
instruction). Combining the pre-table instruction (V-01), the inline column header rule
(V-03), and the gate remediation instruction (V-02) creates two-layer enforcement for C-23
and closes C-24 simultaneously. The combination may produce stronger C-23 compliance than
either V-01 or V-03 alone because the backward trace constraint is enforced at two points:
before the author opens the catalog, and at the cell being filled.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal.

---

**ROLE REGISTRY**

Domain-qualified roles are the first artifact. This registry pre-certifies which roles hold
exception-handling authority. No exception flow may assign a handler to a role not pre-
certified here.

| R-ID | Role Name [Mandatory. Generic labels (User, Approver, Owner, Manager, Finance team) are fails. Name the function at a specific desk: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | Decision Authority [Mandatory. Name the decision type and measurable threshold. "Owns approvals" does not count.] | Exception Handler (Y / N) [Mandatory. Populate Y or N for every role. At least one Y required. Only Y-marked roles may appear in the Handler column of the Exception Catalog.] |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles.

**Gate 1 [Role Registry -> Phase Table]. Do not proceed to PHASE TABLE until Role Registry
is complete: every role has a domain-qualified title, a measurable decision authority, and
the Exception Handler column is fully populated with Y or N. An incomplete registry is a
structural fail -- phases written before roles are anchored produce uncitable R-IDs
downstream.**

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger [Mandatory. "After prior phase" does not count -- name the specific triggering event or artifact state.] | Completion Condition [Mandatory. "When complete" does not count -- name the observable signal.] | SLA Envelope | At-Risk Threshold |
|-------|-----------|------|------|------|------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases, each aggregating >=2 states. At least one At-Risk Threshold names a
causal bottleneck.

**Gate 2 [Phase Table -> State Table]. Do not proceed to STATE TABLE until every phase has
a named entry trigger, completion condition, and SLA envelope.**

---

**STATE TABLE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) [Mandatory. Blank owner is a fail.] | Entry Trigger [Mandatory. "Then it moves" is a fail -- name actor or system event.] | Exit Trigger [Mandatory. "Then it moves" is a fail -- name actor or system event.] | SLA Window | Risk |
|------|-----------|-------------|------|------|------|------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states. Every R-ID cited must exist in the Role Registry.

---

**DECISION TABLE**

| D-ID | Decision Condition [Mandatory. Qualitative conditions do not count -- name a measurable threshold: dollar amount, day count, retry limit, policy code.] | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback [Mandatory. Blank is a structural fail -- name holding state or escalation for owner unavailable / system down / config missing.] |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state with rationale and propose one parallelization opportunity.

---

**EXCEPTION CATALOG**

Before filling this catalog: verify the Role Registry. Every Handler (R-ID) cell below
must resolve to a role with Exception Handler = Y. A handler R-ID that traces to a role
marked N is a structural fail -- that role has not been pre-certified for exception-handling
authority and cannot own an exception flow.

Minimum 3 exceptions spanning at least 2 distinct phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition [Mandatory. "System error" does not count -- name the specific failure mode.] | Divergence S-ID | Handler (R-ID) [Mandatory. Must trace to Exception Handler = Y in the Role Registry. An R-ID from an N-marked role is a structural fail -- that role is not pre-certified for exception-handling authority.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact (phase SLA + magnitude + breach-or-delay) |
|------|--------------|---------------|------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason | Consequence |
|-------|--------------|---------|-----------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific) | Downstream Impact |
|------|------|--------------|------|------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State (S-ID or Ph-ID) | SLA Dependency |
|-------------------|-----------|----------------|-------------------------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate 3 [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED. Writing the artifact when Scan Summary is OPEN is a structural fail -- the
output is an incomplete lifecycle trace where at least one traced path has no named terminal,
and it must be discarded.**

---

**OUTPUT**

Only after Gate 3 is satisfied: write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

---

## V-05 -- Full Lock: C-23 + C-24 + C-18 through C-22 Carry-Through

**Variation axes combined:**
1. Role sequence (C-23) -- Role Registry Exception Handler Y/N column; two-layer backward
   trace enforcement (pre-table instruction + inline column header rule); gate after Role
   Registry blocks forward progress until Y/N column is fully populated; satisfies C-23
2. Phrasing register (C-24) -- production gate names consequence ("is a structural fail")
   and remediation action ("must be discarded"); satisfies C-24 (and C-22)
3. Gate saturation at >=4 distinct boundaries -- role registry, phase table, exception
   catalog, artifact production; each gate names section locked and section unlocked;
   satisfies C-20
4. Exception ownership column -- exception catalog Handler (R-ID) column with inline
   mandatory enforcement; gate after exception catalog blocks until every handler cell is
   populated; satisfies C-21
5. C-18 carry-through -- >=2 anti-pattern negation rules embedded inline within schema
   section column headers (not preamble); point-of-use enforcement language
6. C-19 carry-through -- two-table scan (per-state + per-exception) with explicit CLOSED
   status condition on the production gate

**Hypothesis:** V-04 combines C-23 and C-24 without the full gate saturation of C-20 or the
post-catalog gate that enforces C-21. V-05 is the explicit reference implementation for all
six criteria from C-19 through C-24: each has a named structural decision, not an emergent
property of the register. The pre-table backward trace instruction (V-01 pattern), the
inline column header backward-trace rule (V-03 pattern), the gate after the exception catalog
(R5 V-04/V-05 pattern), and the gate remediation instruction (R5 V-03 pattern) are all
present simultaneously. V-05 answers: what does a prompt look like when C-23 and C-24 are
deliberately engineered alongside the full C-19 through C-22 scaffold?

---

You are a business-process simulation expert. Simulate the full lifecycle of the document
or process named in the signal. Work through every section in order. Each gate must be
satisfied before the next section opens.

---

**ROLE REGISTRY**

Domain-qualified roles are the first artifact. This registry pre-certifies exception-handling
authority -- the Exception Handler column designates which roles may own exception flows.
Only roles marked Y may appear in the Handler column of the Exception Catalog. This is a
registry-level authority designation, not a per-exception assignment: pre-certification
happens here, before any exception is authored.

| R-ID | Role Name [Mandatory. "Approver," "Owner," "Manager," and "Finance team" are fails -- do not use them. Name the function at a specific desk: "AP Clerk," "Revenue Accountant," "Procurement Category Manager," "Senior Credit Analyst."] | Functional Area | Decision Authority [Mandatory. "Owns approvals" does not count -- name the decision type and measurable threshold: "PO approval up to $50K," "Invoice exception hold <=3 business days."] | Exception Handler (Y / N) [Mandatory. Populate Y or N for every role. At least one Y required. Only Y-marked roles may appear as Handler in the Exception Catalog -- citing an N-marked role as an exception handler is a structural fail.] |
|------|------|------|------|------|
| R-01 | | | | Y / N |
| R-02 | | | | Y / N |
| R-03 | | | | Y / N |

Minimum 3 roles. At least one marked Exception Handler Y.

**Gate 1 [Role Registry -> Phase Table]. Do not proceed to PHASE TABLE until Role Registry
is complete: every role has a domain-qualified title, a measurable decision authority, and
the Exception Handler column is fully populated. An incomplete Role Registry is a structural
fail -- phases written before roles are anchored produce uncitable R-IDs downstream.**

---

**PHASE TABLE**

| Ph-ID | Phase Name | Entry Trigger [Mandatory. "After prior phase ends" does not count -- name the specific triggering event or artifact state that causes entry.] | Completion Condition [Mandatory. "When everything is done" does not count -- name what done looks like in observable terms.] | SLA Envelope | At-Risk Threshold |
|-------|-----------|------|------|------|------|
| PH-01 | | | | | |
| PH-02 | | | | | |
| PH-03 | | | | | |
| PH-04 | | | | | |

Minimum 4 phases. Each aggregates >=2 states -- a 1:1 phase-to-state mapping does not
count. At least one At-Risk Threshold names a causal bottleneck.

**Gate 2 [Phase Table -> State Table]. Do not proceed to STATE TABLE until Phase Table is
complete: every phase has a named entry trigger, completion condition, SLA envelope, and at
least one AT-RISK phase is marked with a causal bottleneck. Writing states before phases
are fully defined produces states that cannot be correctly phase-attributed.**

---

**STATE TABLE**

| S-ID | State Name | Phase (Ph-ID) | Owner (R-ID) [Mandatory. Blank owner is a fail -- every state needs an accountable role.] | Entry Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event causing entry.] | Exit Trigger [Mandatory. "Then X happens" is a fail -- name the actor or system event causing exit.] | SLA Window | Risk |
|------|-----------|-------------|------|------|------|------|------|
| | | | | | | | NORMAL / AT-RISK |

Minimum 6 states total across all phases.

---

**DECISION TABLE**

| D-ID | Decision Condition [Mandatory. "Large amount" and "needs review" do not count -- state a measurable threshold: dollar amount, day count, retry limit, or policy code.] | Owner (R-ID) | Branch A (condition met: S-ID) | Branch B (condition not met: S-ID) | Fallback [Mandatory. Blank is a structural fail -- name the holding state or escalation path for: owner unavailable, system down, configuration missing.] |
|------|------|------|------|------|------|
| | | | | | |

Minimum 3 decision points.

---

**PARALLEL PATH TABLE**

| Fork S-ID | Branch A (activity + R-ID) | Branch B (activity + R-ID) | Join Condition | Join Owner (R-ID) | Downstream S-ID |
|-----------|---------------------------|---------------------------|---------------|------------------|----------------|
| | | | | | |

If sequential: state with rationale. Propose one parallelization opportunity naming roles
and states.

---

**EXCEPTION CATALOG**

Before filling this catalog: verify the Role Registry. Every Handler (R-ID) cell below must
resolve to a role with Exception Handler = Y. A handler R-ID that traces to a role marked N
is a structural fail -- that role has not been pre-certified for exception-handling authority
and cannot own an exception flow. Verify backward: for each handler you intend to cite,
confirm it appears in the registry as Y before writing the row.

Minimum 3 exceptions spanning at least 2 distinct phases.

| E-ID | Phase (Ph-ID) | Exception Name | Trigger Condition [Mandatory. "System error" and "data issue" do not count -- name the specific failure mode in domain terms.] | Divergence S-ID | Handler (R-ID) [Mandatory. Must trace to Exception Handler = Y in the Role Registry. An R-ID from an N-marked role is a structural fail -- that role is not pre-certified for exception-handling authority.] | Recovery (S-IDs) or Terminal (T-ID) | SLA Impact [Mandatory. "May cause delays" does not count -- name the phase SLA, magnitude (e.g., "+3 business days"), and whether this is a breach or a delay.] |
|------|--------------|---------------|------|----------------|------|-------------------------------------|------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |

**Gate 3 [Exception Catalog -> Terminals]. Do not proceed to TERMINAL DECLARATION until
every exception row has a Handler (R-ID) that traces to a Y-marked role in the registry.
An exception without a pre-certified handler is a structural fail -- it produces an
exception path with no accountable owner, which is a process gap, not an edge case.**

---

**EDGE CASE TABLE**

| EC-ID | Phase (Ph-ID) | Scenario | Gap Reason (why the lifecycle has no existing handler for this) | Consequence |
|-------|--------------|---------|---------------------------------------------------------------|------------|
| EC-01 | | | | |
| EC-02 | | | | |

---

**BOTTLENECK AND GAP TABLE**

| B-ID | Type | Phase (Ph-ID) | Name | Cause (domain-specific -- "resource constraints" does not count) | Downstream Impact |
|------|------|--------------|------|----------------------------------------------------------------|------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | |

Minimum 2 bottlenecks (cause + downstream impact). Minimum 1 gap (missing step +
consequence of absence).

---

**CROSS-LIFECYCLE DEPENDENCY**

| Adjacent Lifecycle | Direction | Handoff Trigger | Coupling State (S-ID or Ph-ID) | SLA Dependency |
|-------------------|-----------|----------------|-------------------------------|---------------|
| | sends to / receives from | | | |

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (SUCCESS / FAILURE / CANCEL) | SLA Outcome | Reached From (S-IDs and E-IDs) |
|------|--------------|----------------------------------|------------|-------------------------------|
| T-01 | | | | |
| T-02 | | | | |

Minimum: 1 SUCCESS, 1 FAILURE.

---

**SCAN TABLE A -- Per-State Path Closure**

For every S-ID in the State Table, confirm it continues to a named state or appears in a
terminal's Reached From column.

| S-ID | State Name | Next S-ID (if continuing) or Terminal T-ID | Status (CLOSED / OPEN) |
|------|-----------|---------------------------------------------|----------------------|
| | | | |

---

**SCAN TABLE B -- Per-Exception Path Closure**

For every E-ID in the Exception Catalog, confirm the recovery path or terminal is named.

| E-ID | Exception Name | Recovery S-ID or Terminal T-ID | Status (CLOSED / OPEN) |
|------|---------------|-------------------------------|----------------------|
| | | | |

---

**SCAN SUMMARY**

| Scan | Total Rows | CLOSED | OPEN |
|------|-----------|--------|------|
| Scan Table A (states) | | | |
| Scan Table B (exceptions) | | | |
| **Overall Status** | | | **[OPEN / CLOSED]** |

**Gate 4 [Scan Summary -> Artifact]. Artifact may not be written until Scan Summary shows
status CLOSED. Writing the artifact when Scan Summary is OPEN is a structural fail -- the
output is an incomplete lifecycle trace where at least one traced path has no named terminal,
and it must be discarded.**

---

**OUTPUT**

Only after Gate 4 is satisfied (Scan Summary CLOSED): write the lifecycle artifact to
`simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Table > State Table > Decision Table > Parallel Path Table
> Exception Catalog > Edge Case Table > Bottleneck and Gap Table > Cross-Lifecycle
Dependency > Terminal Declaration > Scan Table A > Scan Table B > Scan Summary.

Pre-write checklist (confirm before writing):
- Every R-ID cited in the body traces back to the Role Registry
- Every Exception Handler R-ID in the catalog traces to a Y-marked role in the registry
- Every Entry/Exit Trigger in State Table names an actor or system event (not "then X happens")
- Every Decision Condition names a measurable threshold (not a qualitative condition)
- Every Decision Fallback cell is populated
- Scan Summary Overall Status is CLOSED
```

---

**R6 variation map:**

| Variate | C-23 mechanism | C-24 mechanism | C-20 | C-21 | C-22 |
|---------|---------------|---------------|------|------|------|
| V-01 | Registry Y/N + pre-table instruction | absent | no (1 gate) | yes (handler column) | absent |
| V-02 | absent | consequence + remediation | no (1 gate) | yes (handler column) | yes |
| V-03 | Registry Y/N + inline column rule | absent | no (1 gate) | yes (handler column) | absent |
| V-04 | Registry Y/N + pre-table + inline rule | consequence + remediation | yes (3 gates) | yes (handler column + post-catalog gate) | yes |
| V-05 | Registry Y/N + pre-table + inline rule + post-exception gate | consequence + remediation | yes (4 gates) | yes (handler column + post-catalog gate) | yes |

**Primary questions R6 answers:**
- Does a pre-table backward trace instruction (V-01) produce stronger C-23 compliance than inline column enforcement alone (V-03)?
- Does adding the remediation action to the gate text (V-02 vs R5 V-02's condition-only gate) change output quality?
- Does two-layer C-23 enforcement (pre-table + column header) in V-04/V-05 outperform single-layer in V-01/V-03?
- Can C-23 and C-24 be achieved together without the full C-20 gate saturation scaffold (V-04 answer)?
