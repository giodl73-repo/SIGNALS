Written to `simulations/quest/variations/draft-proposal-variations-R5-2026-03-14.md`.

---

## R5 Variations Summary

| ID | Axis | Predicted Score | Designed Fail |
|----|------|-----------------|---------------|
| V-01 | C-19 + C-21 cluster: canonical labels + dual-signatory anchors | 98.00 | C-18, C-20, C-22 |
| V-02 | C-20 single-axis: machine-checkable PREREQUISITE GATE binary checklist | 98.67 | C-21, C-22 |
| V-03 | C-21 single-axis: dual-signatory F-ROW ANCHOR + front-loaded table | 98.67 | C-20, C-22 |
| V-04 | C-19 + C-20 + C-21 combined: prose trigger descriptions only | 99.33 | C-22 only |
| V-05 | Full integration: T-01 through T-GUARD + TRIGGER back-reference | 100.00 | -- |

**Key R5 structural decisions:**

**Single-cluster axis (V-01)**: C-19 and C-21 test the same register/sign-off surface — canonical label precision and dual-signatory anchors are naturally adjacent. Testing them together without any table machinery isolates the F-row cluster from gate and trigger-ID infrastructure.

**C-20 discriminator (V-02 vs V-03)**: Both have front-loaded tables and canonical labels. V-02 adds the PREREQUISITE GATE (C-20 passes, C-21 fails via shared CONDITIONS only). V-03 adds dual-signatory anchors (C-21 passes, C-20 fails — no gate). This pair tests C-20 and C-21 in clean isolation with identical baselines.

**C-22 as final discriminator (V-04 vs V-05)**: V-04 passes C-19 + C-20 + C-21 with prose trigger conditions — trigger rules are named but carry no stable IDs, and amendment rows have no TRIGGER back-reference field. V-05 adds `T-01` through `T-GUARD` IDs and the `TRIGGER:` field in every amend entry. C-22 is the single controlled gap between the two.

**T-GUARD cascade (V-05)**: Each amend entry in Phase 12 now carries a `TRIGGER:` field citing the T-NN that fired it — or `TRIGGER: MANUAL` for editorially-identified gaps. An empty Phase 0 table at document completion means T-GUARD enforced all structure successfully. This creates the traceable chain C-22 requires.
se without stable IDs, and amendment rows had no TRIGGER back-reference field. R5 V-05 adds named IDs (T-01 through T-GUARD) to all trigger rules and adds a TRIGGER field to every amendment row, creating the traceable chain required by C-22.

**Predicted scorecard under v5** (formula: essential_pass/4*60 + recommended_pass/3*30 + aspirational_pass/15*10, max 100):

| Variation | Essential (60) | Recommended (30) | Aspirational (/15, 10) | Total | Fails |
|-----------|---------------|-----------------|----------------------|-------|-------|
| V-01 | 60.0 (4/4) | 30.0 (3/3) | 8.00 (12/15) | **98.00** | C-18, C-20, C-22 |
| V-02 | 60.0 (4/4) | 30.0 (3/3) | 8.67 (13/15) | **98.67** | C-21, C-22 |
| V-03 | 60.0 (4/4) | 30.0 (3/3) | 8.67 (13/15) | **98.67** | C-20, C-22 |
| V-04 | 60.0 (4/4) | 30.0 (3/3) | 9.33 (14/15) | **99.33** | C-22 only |
| V-05 | 60.0 (4/4) | 30.0 (3/3) | 10.00 (15/15) | **100.00** | -- |

---

## V-01: F-Row Precision Cluster

**Axis**: C-19 + C-21 combined (canonical F-row labels + dual-signatory F-ROW ANCHOR); no front-loaded amendment table; no PREREQUISITE GATE
**Hypothesis**: The two F-row structural criteria cluster naturally: canonical label alignment (C-19) and dual-signatory F-ROW ANCHOR (C-21) both concern the failure mode register and its connection to the recommendation sign-off. A variation can implement both axes without any amendment table machinery or gate verification. C-18 fails by design (no front-loaded table initialized before Phase 1); C-20 fails by design (no PREREQUISITE GATE block); C-22 fails by design (no amendment table, no trigger IDs, no TRIGGER back-reference field). Tests whether the F-row precision cluster is structurally self-consistent before adding gate and trigger ID machinery.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact with: name, date, and key finding relevant to this decision. If none exist, state the gap and provide a 2-3 sentence inline assessment substituting for the absent artifact.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options are named:
- Stack: language, runtime, platform, OS compatibility
- Integration: APIs, protocols, dependency limits
- Timeline: achievable windows at current team size
- Known failure modes: technical risks that could invalidate an option regardless of other merits

Label each constraint C-NN. These are fixed. Any option violating a constraint must include explicit justification.

---

### Phase 3: PM -- Decision Frame

**PM** fills all four fields before writing options. All four are required; omitting any field fails the artifact.

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, event, or deadline that closes the window.
                       Do not write "soon," "eventually," "shortly," or "in the near future."]
INACTION CONSEQUENCE: [What teams lose, incur, or are blocked by if the TEMPORAL ANCHOR
                       passes without a decision -- name it, do not assert generic risk.]
```

---

### Phase 4: Risk Scoring Guide

Define project-specific scoring anchors before writing any options. Each anchor must describe a named outcome in this project's context -- not a generic severity label. These anchors apply to all Risk fields and register entries.

```
PROBABILITY ANCHORS (this project, this decision):
  1 (rare):      [Named condition that makes this outcome unlikely for this specific project]
  3 (plausible): [Named typical-trouble outcome specific to this project -- not a generic category]
  5 (likely):    [Named condition making this outcome near-certain for this project]

IMPACT ANCHORS (this project, this decision):
  1 (negligible): [Named concrete example of low impact in this project's context]
  3 (moderate):   [Named specific consequence representing medium impact here]
  5 (severe):     [Named outcome representing high impact -- not a severity label]
```

Every risk field and register entry uses separate P and I numeric scores grounded in these anchors. Holistic L/M/H labels fail.

---

### Phase 5: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they address or avoid this problem |
| Pros | Low switching cost, familiarity, zero migration risk -- specific to this domain |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [The metric that degrades per sprint/month/quarter -- name metric and rate of drift] |

**Architect note**: Deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 6: Alternatives (Minimum 3)

For each alternative, all fields are required. Omitting any field fails the artifact.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: Compliance with all C-NN constraints from Phase 2. Name any violation and justification.

---

### Phase 7: Comparison Matrix

Joint PM/Architect table. Columns = all options. Rows = 4-6 dimensions. No empty cells. Required dimensions: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 entries. Validation plan must name a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 entries. Use Phase 4 anchors for all P and I scores.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

### Phase 10: Failure Mode Register

Minimum 2 entries. Distinct from the Risk Register (Phase 9). Failure modes describe conditions that would invalidate the recommendation -- not risk events that may occur during implementation.

Each entry uses the following exact field labels. These labels are canonical: do not substitute synonyms. "Observable Event" is not TRIGGER CONDITION. "Fallback" is not MITIGATION. The field names must match verbatim.

```
F-NN:
  FAILURE MODE:       [What goes wrong -- the specific failure, named precisely]
  TRIGGER CONDITION:  [The observable event or threshold that confirms this failure mode has
                       activated -- name who observes it, what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback -- name an option letter or
                       next action; "reconsider" and "revisit" are not acceptable]
```

Each F-NN must cross-reference the assumption (A-NN) or risk (R-NN) entry it would invalidate.

---

### Phase 11: Recommendation -- Independent Dual Signature

Both signature blocks are required. F-ROW ANCHOR is a typed slot independently required in both the PM block and the Architect block. Neither signatory can complete their block without naming an F-row ID. F-ROW ANCHOR is not a shared field: it appears once in the PM block and independently once in the Architect block. The two signatories may reference the same or different F-rows -- structural independence is the requirement, not content divergence.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name, or state "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  F-ROW ANCHOR:     [F-NN: the failure mode whose activation most directly invalidates
                     this recommendation from a business or adoption perspective.
                     This slot is required in the PM block. Do not omit.]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named, or "none" only if
                         Architect fully concurs with zero reservations]
  CONSTRAINT VERIFIED:  [Confirm chosen option satisfies all Phase 2 C-NN constraints,
                         or name the exception with justification]
  F-ROW ANCHOR:         [F-NN: the failure mode whose activation would cause Architect to
                         reassess or DISSENT. Required slot in the Architect block --
                         independent of PM's F-ROW ANCHOR. Cannot be deferred to PM block.]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 12: Amend Phase

All three sections required. Each entry carries all three typed slots: OWNER, NEXT ACTION, and DEADLINE. DEADLINE must be a specific sprint name, named date, or named milestone -- "TBD," "soon," or blank fails.

#### MISSING OPTION

```
[Unexplored approach and why it matters]
OWNER:       [role/team]
NEXT ACTION: [specific investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted decision dimension and why it should be recalibrated]
OWNER:       [role/team]
NEXT ACTION: [specific recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite that must be resolved]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-02: Machine-Checkable PREREQUISITE GATE

**Axis**: C-20 single-axis (PREREQUISITE GATE as binary checklist); front-loaded amendment table with prose trigger conditions; canonical F-row labels; shared F-ROW ANCHOR in CONDITIONS only
**Hypothesis**: R4 V-02's PREREQUISITE GATE used PASS/FAIL labels. C-20 requires machine-checkable named binaries ("complete / not complete") confirming three things: assumption register complete, risk register complete, and both registers precede this gate. R5 V-02 upgrades the gate format to satisfy C-20 exactly. V-02 retains the front-loaded amendment table (C-18 passes) with prose trigger conditions but no named IDs (C-22 fails). V-02 deliberately uses F-row references only in the shared CONDITIONS block of the PM sign-off -- C-15 passes, C-21 fails because neither signatory has an independent F-ROW ANCHOR typed slot.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Initialize the Amendment Tracking Table before writing Phase 1. Complete the PREREQUISITE GATE before writing Phase 11. Role labels are mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 0: Amendment Tracking Table

Initialize this table before writing any other phase. Add rows during writing when a trigger condition fires. Do not assemble this table retrospectively after the document is complete.

| Criterion | Trigger Condition | Phase | Amendment Type | Gap Description | Status |
|-----------|------------------|-------|----------------|-----------------|--------|
| C-10 | No scout artifact found in any search path | Phase 1 | MISSING ARTIFACT | | |
| C-02 | Required option field absent (Description / Pros / Cons / Risk / Effort) | Phase 5-6 | OPTION ANATOMY | | |
| C-13 | TEMPORAL ANCHOR or INACTION CONSEQUENCE field missing from decision frame | Phase 3 | DECISION FRAME GAP | | |
| C-08 | Assumption or risk register has fewer than 2 entries | Phase 8-9 | REGISTER GAP | | |
| C-15 | Sign-off CONDITIONS references no F-row by ID | Phase 11 | LINKAGE GAP | | |
| C-17 | Assumption or risk register appears after recommendation in document sequence | Phase 11 | SEQUENCE VIOLATION | | |

Add rows for any additional gap caught during writing.

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding relevant to this decision. If none found, state the gap and provide a 2-3 sentence inline assessment. If no artifact is found, add a row to the Phase 0 table.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options are named:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed. Any option violating a constraint requires explicit justification.

---

### Phase 3: PM -- Decision Frame

All four fields required. If TEMPORAL ANCHOR or INACTION CONSEQUENCE is omitted, add a row to the Phase 0 table.

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, event, or deadline -- no vague temporal language]
INACTION CONSEQUENCE: [Named concrete outcome -- teams blocked, capability lost, or window
                       closed -- missed-feature statements do not qualify]
```

---

### Phase 4: Risk Scoring Guide

Define project-specific scoring anchors before writing any options.

```
PROBABILITY ANCHORS (this project, this decision):
  1 (rare):      [Named condition -- project-specific]
  3 (plausible): [Named typical-trouble condition -- project-specific]
  5 (likely):    [Named near-certain condition -- project-specific]

IMPACT ANCHORS (this project, this decision):
  1 (negligible): [Named concrete low-impact outcome -- project-specific]
  3 (moderate):   [Named medium-impact consequence -- project-specific]
  5 (severe):     [Named high-impact outcome -- not a severity label]
```

All risk fields use separate P and I numeric scores. Holistic L/M/H labels fail.

---

### Phase 5: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

| Field | Content |
|-------|---------|
| Description | What teams do today |
| Pros | Low switching cost, familiarity, zero migration risk |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [Metric that degrades per sprint -- name metric and rate] |

---

### Phase 6: Alternatives (Minimum 3)

All fields required. Missing any field triggers C-02 -- add row to Phase 0 table.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 7: Comparison Matrix

Joint PM/Architect table. Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 A-NN entries. If fewer, add a row to the Phase 0 table. Validation plan requires a concrete action.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. If fewer, add a row to the Phase 0 table. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register. Failure modes are conditions that invalidate the recommendation, not implementation risk events.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise, not a risk category]
  TRIGGER CONDITION:  [Observable event confirming activation -- who observes it,
                       what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback option -- name an option
                       letter or action; "reconsider" and "revisit" fail]
```

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. No synonym substitution. Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 10.5: PREREQUISITE GATE

Complete this gate before writing Phase 11. Each item is a named binary: "complete" or "not complete." Do not use prose summaries. Do not proceed if any item reads "not complete" -- resolve the gap first and add an amendment row.

```
PREREQUISITE GATE
  [ ] Assumption register: >= 2 A-NN entries with validation plans   [complete / not complete]
  [ ] Risk register: >= 2 R-NN entries with P, I, P*I scores         [complete / not complete]
  [ ] Failure mode register: >= 2 F-NN entries with MITIGATION named  [complete / not complete]
  [ ] Assumption register precedes this gate in document sequence     [complete / not complete]
  [ ] Risk register precedes this gate in document sequence           [complete / not complete]

GATE STATUS: [OPEN -- proceed to Phase 11 | BLOCKED -- resolve items above first]
```

---

### Phase 11: Recommendation

Both signature blocks are required. The PM sign-off CONDITIONS must reference at least one F-row by ID -- this is the sign-off linkage requirement. If CONDITIONS references no F-row, add a row to the Phase 0 table.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name, or state "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid.
                     At least one condition must reference an F-row by ID,
                     e.g., "remains valid unless F-01 activates."]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [C-NN compliance confirmed, or exception named with justification]
  CONDITIONS:           [Technical conditions -- at least one must reference an F-row by ID]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 12: Amend Phase

All three sections required. Each entry carries OWNER, NEXT ACTION, and DEADLINE as typed slots. DEADLINE must be specific.

#### MISSING OPTION

```
[Unexplored approach and why it matters]
OWNER:       [role/team]
NEXT ACTION: [specific investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted decision dimension and why it should be recalibrated]
OWNER:       [role/team]
NEXT ACTION: [specific recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite that must be resolved]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

---

### Phase 13: Amendment Table Review

Review the Phase 0 table. For each populated row, confirm the gap was addressed or escalated. For each empty row, confirm the prompt enforced the criterion successfully. State amendment table final status.

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-03: Dual-Signatory F-ROW ANCHOR with Front-Loaded Table

**Axis**: C-21 single-axis (structural independence of F-ROW ANCHOR per signatory); front-loaded amendment table with prose trigger conditions; canonical F-row labels; no PREREQUISITE GATE
**Hypothesis**: C-21 requires structural independence: each sign-off block independently carries an F-ROW ANCHOR typed slot that cannot be omitted or deferred. V-02 uses F-row references only in the shared CONDITIONS block -- satisfying C-15 but not C-21. V-03 tests whether making F-ROW ANCHOR independently required in each signatory block is achievable without a PREREQUISITE GATE (C-20 fails by design) or named trigger IDs (C-22 fails by design). The front-loaded amendment table (C-18 passes) carries trigger conditions as prose descriptions without stable named IDs. Tests C-21 in isolation from C-20 and C-22.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Initialize the Amendment Tracking Table before writing Phase 1. Role labels are mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 0: Amendment Tracking Table

Initialize before Phase 1. Populate when a trigger fires. Do not assemble retrospectively.

| Criterion | Trigger Condition | Phase | Amendment Type | Gap Description | Status |
|-----------|------------------|-------|----------------|-----------------|--------|
| C-10 | No scout artifact found in any search path | Phase 1 | MISSING ARTIFACT | | |
| C-02 | Required option field absent | Phase 5-6 | OPTION ANATOMY | | |
| C-13 | TEMPORAL ANCHOR or INACTION CONSEQUENCE missing | Phase 3 | DECISION FRAME GAP | | |
| C-08 | Register has fewer than 2 entries | Phase 8-9 | REGISTER GAP | | |
| C-15 | Sign-off block references no F-row by ID | Phase 11 | LINKAGE GAP | | |
| C-17 | Assumption or risk register appears after recommendation | Phase 11 | SEQUENCE VIOLATION | | |
| C-21 | PM or Architect F-ROW ANCHOR slot omitted from sign-off block | Phase 11 | ANCHOR ABSENT | | |

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none, state gap and provide 2-3 sentence inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed. Options violating a constraint require justification.

---

### Phase 3: PM -- Decision Frame

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- no vague temporal language]
INACTION CONSEQUENCE: [Named concrete outcome of not deciding -- teams blocked, capability
                       lost, or window closed -- missed-feature statements do not qualify]
```

---

### Phase 4: Risk Scoring Guide

```
PROBABILITY ANCHORS (this project, this decision):
  1 (rare):      [Named condition -- project-specific]
  3 (plausible): [Named condition -- project-specific]
  5 (likely):    [Named condition -- project-specific]

IMPACT ANCHORS (this project, this decision):
  1 (negligible): [Named outcome -- project-specific]
  3 (moderate):   [Named outcome -- project-specific]
  5 (severe):     [Named outcome -- project-specific]
```

Separate P and I numeric scores required. Holistic labels fail.

---

### Phase 5: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

| Field | Content |
|-------|---------|
| Description | What teams do today |
| Pros | Low switching cost, familiarity, zero migration risk |
| Cons | Capability gaps or maintenance burdens |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [Metric + rate of drift per sprint] |

---

### Phase 6: Alternatives (Minimum 3)

All fields required. Missing any field triggers C-02 amendment.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 7: Comparison Matrix

Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 A-NN entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise]
  TRIGGER CONDITION:  [Observable event confirming activation -- who, what signal, when]
  MITIGATION:         [Specific escalation path or fallback option]
```

Canonical labels only: FAILURE MODE / TRIGGER CONDITION / MITIGATION. No synonym substitution. Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 11: Recommendation -- Independent Dual Signature

Both sign-off blocks are required. F-ROW ANCHOR is a typed slot independently required in both the PM block and the Architect block. The F-ROW ANCHOR slot is not shared between signatories -- it exists once in the PM block and once in the Architect block as separate independent entries. Neither signatory can complete their block without naming an F-row ID. If either block omits the F-ROW ANCHOR slot, fire the C-21 trigger in Phase 0.

The two signatories may name the same or different F-rows. Structural independence -- not content divergence -- is the requirement.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name, or state "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  F-ROW ANCHOR:     [F-NN: the failure mode whose activation most directly invalidates
                     this recommendation from a business or adoption perspective.
                     Required slot in PM block. Cannot be omitted or deferred.]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named, or "none" with justification]
  CONSTRAINT VERIFIED:  [C-NN compliance confirmed, or exception named with justification]
  F-ROW ANCHOR:         [F-NN: the failure mode whose activation would cause Architect to
                         reassess or DISSENT. Required slot in Architect block -- independent
                         of PM's F-ROW ANCHOR. Architect cannot defer to PM's anchor entry.]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 12: Amend Phase

All three sections required. Each entry: OWNER, NEXT ACTION, DEADLINE typed slots. DEADLINE must be specific.

#### MISSING OPTION

```
[Unexplored approach and why it matters]
OWNER:       [role/team]
NEXT ACTION: [specific investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted decision dimension and why it should be recalibrated]
OWNER:       [role/team]
NEXT ACTION: [specific recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite that must be resolved]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

---

### Phase 13: Amendment Table Review

Review Phase 0. Confirm populated rows addressed or escalated. Confirm empty rows reflect successful prompt enforcement.

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-04: F-Row Precision + PREREQUISITE GATE + Dual-Signatory (No Trigger IDs)

**Axis**: C-19 + C-20 + C-21 combined; C-22 fails by design (front-loaded table has prose trigger descriptions without named IDs)
**Hypothesis**: The three structural advances from C-19, C-20, and C-21 combine cleanly with a front-loaded amendment table (C-18). C-22 is orthogonal to the F-row and gate machinery: it lives in the amendment table trigger rules, not in the failure mode register or sign-off blocks. A variation can implement canonical labels, a machine-checkable gate, and dual-signatory anchors without assigning stable named IDs to trigger rules. C-22 fails because Phase 0 trigger conditions are described in prose without stable IDs, and amendment rows carry no TRIGGER back-reference field. This is the single controlled discriminator between V-04 and V-05.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Initialize the Amendment Tracking Table before Phase 1. Complete the PREREQUISITE GATE before Phase 11. Role labels mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 0: Amendment Tracking Table

Initialize before Phase 1. Populate when a trigger fires. Do not assemble retrospectively.

| Criterion | Trigger Condition | Phase | Amendment Type | Gap Description | Status |
|-----------|------------------|-------|----------------|-----------------|--------|
| C-10 | No scout artifact found in any search path | Phase 1 | MISSING ARTIFACT | | |
| C-02 | Required option field absent (Description / Pros / Cons / Risk / Effort) | Phase 5-6 | OPTION ANATOMY | | |
| C-13 | TEMPORAL ANCHOR or INACTION CONSEQUENCE field missing | Phase 3 | DECISION FRAME GAP | | |
| C-08 | Assumption or risk register has fewer than 2 entries | Phase 8-9 | REGISTER GAP | | |
| C-15 | Sign-off block references no F-row by ID | Phase 11 | LINKAGE GAP | | |
| C-17 | Assumption or risk register appears after recommendation in document | Phase 11 | SEQUENCE VIOLATION | | |
| C-21 | PM or Architect F-ROW ANCHOR slot missing from sign-off block | Phase 11 | ANCHOR ABSENT | | |

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none, state gap and provide 2-3 sentence inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed. Options violating a constraint require justification.

---

### Phase 3: PM -- Decision Frame

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- no vague temporal language]
INACTION CONSEQUENCE: [Named concrete outcome -- teams blocked, capability lost, window
                       closed -- missed-feature statements do not qualify]
```

---

### Phase 4: Risk Scoring Guide

```
PROBABILITY ANCHORS (this project, this decision):
  1 (rare):      [Named condition -- project-specific]
  3 (plausible): [Named condition -- project-specific]
  5 (likely):    [Named condition -- project-specific]

IMPACT ANCHORS (this project, this decision):
  1 (negligible): [Named outcome -- project-specific]
  3 (moderate):   [Named outcome -- project-specific]
  5 (severe):     [Named outcome -- project-specific]
```

Separate P and I numeric scores. Holistic L/M/H labels fail.

---

### Phase 5: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

| Field | Content |
|-------|---------|
| Description | What teams do today |
| Pros | Low switching cost, familiarity, zero migration risk |
| Cons | Capability gaps or maintenance burdens |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [Metric + rate of drift per sprint] |

---

### Phase 6: Alternatives (Minimum 3)

All fields required. Missing any field triggers C-02 amendment.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 7: Comparison Matrix

Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 A-NN entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise, not a risk category]
  TRIGGER CONDITION:  [Observable event confirming activation -- who, what signal, when]
  MITIGATION:         [Specific escalation path or fallback option]
```

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. These are the exact field names -- no synonym substitution. "Observable Event" fails for TRIGGER CONDITION. "Fallback" fails for MITIGATION. Label precision makes scoring deterministic. Each F-NN cross-references its A-NN or R-NN.

---

### Phase 10.5: PREREQUISITE GATE

Complete before Phase 11. Each item is a named binary: "complete" or "not complete." No prose summaries. Do not proceed if GATE STATUS is BLOCKED.

```
PREREQUISITE GATE
  [ ] Assumption register: >= 2 A-NN entries with validation plans   [complete / not complete]
  [ ] Risk register: >= 2 R-NN entries with P, I, P*I scores         [complete / not complete]
  [ ] Failure mode register: >= 2 F-NN entries with MITIGATION named  [complete / not complete]
  [ ] Assumption register precedes this gate in document sequence     [complete / not complete]
  [ ] Risk register precedes this gate in document sequence           [complete / not complete]
  [ ] F-row labels canonical (FAILURE MODE / TRIGGER CONDITION /
      MITIGATION -- no synonyms)                                      [complete / not complete]

GATE STATUS: [OPEN -- proceed to Phase 11 | BLOCKED -- resolve items above first]
```

If any item is "not complete," add a row to the Phase 0 amendment table before proceeding.

---

### Phase 11: Recommendation -- Independent Dual Signature

Both sign-off blocks required. F-ROW ANCHOR is independently required in both the PM block and the Architect block. Neither block is complete without it. Omitting F-ROW ANCHOR from either block fires the C-21 trigger in Phase 0. The two signatories may name the same or different F-rows.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name, or state "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  F-ROW ANCHOR:     [F-NN: the failure mode whose activation most directly invalidates
                     this recommendation from a business or adoption perspective.
                     Required slot -- cannot be omitted or deferred to Architect block.]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [C-NN compliance confirmed, or exception named with justification]
  F-ROW ANCHOR:         [F-NN: the failure mode whose activation would cause Architect to
                         reassess or DISSENT. Required slot -- independent of PM's anchor.
                         Architect cannot defer to PM's F-ROW ANCHOR entry.]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 12: Amend Phase

All three sections required. Each entry: OWNER, NEXT ACTION, DEADLINE typed slots. DEADLINE must be specific.

#### MISSING OPTION

```
[Unexplored approach and why it matters]
OWNER:       [role/team]
NEXT ACTION: [specific investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted decision dimension and why it should be recalibrated]
OWNER:       [role/team]
NEXT ACTION: [specific recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite that must be resolved]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

---

### Phase 13: Amendment Table Review

Review Phase 0. Confirm each populated row addressed or escalated. Confirm empty rows reflect enforcement success.

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-05: Full Integration -- Named Trigger ID Cascade

**Axis**: All four new criteria combined (C-19 + C-20 + C-21 + C-22); named trigger IDs T-01 through T-GUARD with row-level TRIGGER back-reference field in every amendment row
**Hypothesis**: Named trigger IDs in the front-loaded amendment table -- one stable ID per trigger rule, one TRIGGER field per amendment row -- close the criterion-ID drift risk identified in R3. The traceable chain (criterion -> trigger ID -> amendment row) is stable across rubric versions: trigger IDs do not shift when new criteria are added, so accumulated mislabeling cannot occur silently. T-GUARD provides a single cascade covering all structural block absences. Combined with canonical F-row labels (C-19), machine-checkable PREREQUISITE GATE binary checklist (C-20), and dual-signatory F-ROW ANCHOR independently required in each sign-off block (C-21), all 15 aspirational criteria are satisfied. Golden candidate.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Initialize the Amendment Tracking Table (Phase 0) before writing Phase 1. Complete the PREREQUISITE GATE before Phase 11. Role labels mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 0: Amendment Tracking Table

Initialize before writing any other phase. Each trigger rule carries a stable named ID. When a trigger fires, add a row to the Amendment Rows section citing the trigger ID in the TRIGGER field. Do not assemble rows retrospectively -- populate during writing.

**Trigger Rules:**

| ID | Trigger Rule | Fires When | Criterion(s) |
|----|--------------|-----------|--------------|
| T-01 | Scout gap | No scout artifact found in any search path | C-10 |
| T-02 | Option incomplete | Required field absent in any option (Description / Pros / Cons / Risk / Effort) | C-02 |
| T-03 | Decision frame gap | TEMPORAL ANCHOR or INACTION CONSEQUENCE field missing | C-13 |
| T-04 | Register thin | Assumption or risk register has fewer than 2 entries | C-08 |
| T-05 | F-row linkage absent | Sign-off block references no F-row by ID, or F-ROW ANCHOR slot missing | C-15, C-21 |
| T-06 | Sequence inverted | Assumption or risk register appears after recommendation in document | C-17 |
| T-GUARD | Structural block absent | Any required typed slot, phase block, or gate item is missing or empty | All aspirational |

**Amendment Rows** (populate during writing -- cite the TRIGGER field for each row):

| TRIGGER | Criterion | Phase | Amendment Type | Gap Description | OWNER | NEXT ACTION | DEADLINE |
|---------|-----------|-------|----------------|-----------------|-------|-------------|---------|
| | | | | | | | |

Empty table at document completion means T-GUARD enforced all structural requirements successfully. Populated rows must each cite a T-NN ID.

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding relevant to this decision. If none found, fire T-01 and add row to Amendment Rows with TRIGGER: T-01. Provide 2-3 sentence inline assessment as fallback.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options:
- Stack: language, runtime, platform, OS compatibility
- Integration: APIs, protocols, dependency limits
- Timeline: achievable windows at current team size
- Known failure modes: technical risks that invalidate options regardless of other merits

Label each C-NN. Fixed. Options violating a constraint require explicit justification.

---

### Phase 3: PM -- Decision Frame

All four fields required. If TEMPORAL ANCHOR or INACTION CONSEQUENCE is absent, fire T-03.

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, event, or deadline that closes the window.
                       Vague language prohibited: "soon," "eventually," "in the near future."]
INACTION CONSEQUENCE: [Named concrete outcome -- teams blocked, capability lost, window closed.
                       Missed-feature statements do not qualify.]
```

---

### Phase 4: Risk Scoring Guide

Define project-specific anchors before writing any options.

```
PROBABILITY ANCHORS (this project, this decision):
  1 (rare):      [Named condition -- specific to this project, not a generic category]
  3 (plausible): [Named typical-trouble condition -- specific to this project]
  5 (likely):    [Named near-certain condition -- specific to this project]

IMPACT ANCHORS (this project, this decision):
  1 (negligible): [Named concrete low-impact outcome for this project]
  3 (moderate):   [Named medium-impact consequence for this project]
  5 (severe):     [Named high-impact outcome -- not a severity label]
```

All risk fields use separate P and I numeric scores from these anchors. Holistic L/M/H labels fail.

---

### Phase 5: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they address or avoid the problem |
| Pros | Low switching cost, familiarity, zero migration risk |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [Metric that degrades per sprint -- name metric and rate of drift] |

**Architect note**: Deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 6: Alternatives (Minimum 3)

All fields required. Missing any field fires T-02 -- add amendment row with TRIGGER: T-02.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: C-NN compliance or named exception with justification.

---

### Phase 7: Comparison Matrix

Joint PM/Architect table. Columns = all options. Rows = 4-6 dimensions. No empty cells. Required dimensions: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 A-NN entries. If fewer, fire T-04. Validation plan requires a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. If fewer, fire T-04. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register. Failure modes are conditions that invalidate the recommendation -- not implementation risk events.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise, not a risk category]
  TRIGGER CONDITION:  [Observable event confirming activation -- who observes it,
                       what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback option -- name the option
                       letter or next action; "reconsider" and "revisit" fail]
```

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. These are the exact field names. Do not substitute synonyms. "Observable Event" fails for TRIGGER CONDITION. "Fallback" fails for MITIGATION. Label precision makes C-19 scoring deterministic: the field name is either present with the canonical label or it is not.

Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 10.5: PREREQUISITE GATE

Complete before Phase 11. Each item is a named binary -- "complete" or "not complete." No prose summaries. If any item is "not complete," do not proceed: fire T-GUARD and add amendment row with TRIGGER: T-GUARD.

```
PREREQUISITE GATE
  [ ] Assumption register: >= 2 A-NN entries with validation plans   [complete / not complete]
  [ ] Risk register: >= 2 R-NN entries with P, I, P*I scores         [complete / not complete]
  [ ] Failure mode register: >= 2 F-NN entries with MITIGATION named  [complete / not complete]
  [ ] Assumption register precedes this gate in document sequence     [complete / not complete]
  [ ] Risk register precedes this gate in document sequence           [complete / not complete]
  [ ] F-row labels canonical (FAILURE MODE / TRIGGER CONDITION /
      MITIGATION -- no synonyms used)                                 [complete / not complete]

GATE STATUS: [OPEN -- proceed to Phase 11 | BLOCKED -- resolve items above first]
```

---

### Phase 11: Recommendation -- Independent Dual Signature

Both sign-off blocks required. F-ROW ANCHOR is a typed slot independently required in both the PM block and the Architect block. Neither block is complete without naming an F-row ID in its own F-ROW ANCHOR slot. Omitting F-ROW ANCHOR from either block fires T-05 -- add amendment row with TRIGGER: T-05. The two signatories may name the same or different F-rows: structural independence, not content divergence, is the requirement.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name, or state "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  F-ROW ANCHOR:     [F-NN: the failure mode whose activation most directly invalidates
                     this recommendation from a business or adoption perspective.
                     Required slot in PM block. Cannot be omitted or deferred.]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named, or "none" with full justification]
  CONSTRAINT VERIFIED:  [Confirms chosen option satisfies all Phase 2 C-NN constraints,
                         or names the exception with justification]
  F-ROW ANCHOR:         [F-NN: the failure mode whose activation would cause Architect to
                         reassess or DISSENT. Required slot in Architect block -- independent
                         of PM's F-ROW ANCHOR. Architect cannot defer to PM's anchor entry.]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 12: Amend Phase

All three sections required. Each entry carries OWNER, NEXT ACTION, and DEADLINE as typed slots, plus a TRIGGER field citing the T-NN that generated it. Manual additions (not triggered by Phase 0 rules) cite TRIGGER: MANUAL. DEADLINE must be specific.

#### MISSING OPTION

```
[Unexplored approach and why it matters]
TRIGGER:     [T-NN from Phase 0, or MANUAL]
OWNER:       [role/team]
NEXT ACTION: [specific investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted decision dimension and why it should be recalibrated]
TRIGGER:     [T-NN from Phase 0, or MANUAL]
OWNER:       [role/team]
NEXT ACTION: [specific recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite that must be resolved]
TRIGGER:     [T-NN from Phase 0, or MANUAL]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

---

### Phase 13: Amendment Table Reconciliation

Review the Phase 0 Amendment Rows. For each populated row, confirm the gap is addressed or escalated. If the Amendment Rows table is empty, state explicitly: "GATE CLEAR -- T-GUARD enforced all structural requirements; no enforcement failures during writing." Write the final table reconciliation status.

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```
