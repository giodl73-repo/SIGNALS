Written to `simulations/quest/variations/draft-proposal-variations-R6-2026-03-14.md`.

---

## R6 Summary

| ID | Axis | Predicted Score | Designed Fail |
|----|------|-----------------|---------------|
| V-01 | C-23 single-axis: T-GUARD exact scope vocabulary, no completion declaration | 99.41 | C-24 |
| V-02 | C-24 single-axis: exact completion declaration, T-GUARD scope generic | 99.41 | C-23 |
| V-03 | Baseline contrast: generic scope + no declaration | 98.82 | C-23, C-24 |
| V-04 | C-23 + C-24 + inertia-forward framing (INERTIA COST / INERTIA OFFSET) | 100.00 | -- |
| V-05 | Sentinel-first ordering + COMPLETION STATUS as Phase 0 typed slot | 100.00 | -- |

**Key structural decisions:**

**C-23 discriminator (V-01 vs V-02).** V-01 has exact scope vocabulary ("any required typed slot, phase block, or gate item absent from the document") but no completion declaration — C-23 passes, C-24 fails. V-02 flips: completion declaration is exact but T-GUARD scope uses "any structural block or item not covered by enumerated triggers" — C-24 passes, C-23 fails. The two criteria are fully decoupled.

**V-03 baseline.** Uses the R5 V-05 completion text ("GATE CLEAR -- T-GUARD enforced all structural requirements...") and generic scope. Both C-23 and C-24 fail, establishing the 98.82 lower bound for R6. This confirms the discriminator weight of the two new criteria.

**V-04 inertia axis.** Both C-23 and C-24 pass. The new axis is computable do-nothing cost: Option 0 gets `INERTIA COST` (P*I per sprint from Phase 4 anchors) and alternatives must name `INERTIA OFFSET` (sprint crossover point). An extra PREREQUISITE GATE item confirms the INERTIA COST field is present. This seeds a quality metric not yet in the rubric.

**V-05 sentinel-first + COMPLETION STATUS slot.** T-GUARD moves to the top of the trigger table (before T-01). The `COMPLETION STATUS` field is defined in Phase 0 at initialization (`PENDING`), then updated in Phase 13 — so the C-24 declaration is structurally in the amendment table from document creation, not retroactively appended. This is a stronger structural guarantee than V-04's Phase 13 prose statement for the same criterion.
 anchors) and an INERTIA OFFSET requirement for all alternatives (the sprint count at which an alternative's cumulative cost crosses below the do-nothing curve). This is not a rubric criterion but seeds a quality metric for do-nothing quantification analogous to V-03 from R4.

**Sentinel-first ordering (V-05)**: T-GUARD appears as the first entry in the trigger definition table, before T-01 through T-06. C-23 only requires T-GUARD to appear "in the trigger definition section at table initialization" -- not at any specific position. Sentinel-first ordering changes the enforcement semantics: the catch-all fires first, before any specific trigger, which means unenumerated gaps are surfaced at the earliest possible point. This is a structural property not tested in prior rounds.

**Predicted scorecards under v6** (formula: essential_pass/4*60 + recommended_pass/3*30 + aspirational_pass/17*10, max 100):

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total | Fails |
|-----------|---------------|-----------------|-------------------|-------|-------|
| V-01 | 60.0 (4/4) | 30.0 (3/3) | 9.41 (16/17) | **99.41** | C-24 |
| V-02 | 60.0 (4/4) | 30.0 (3/3) | 9.41 (16/17) | **99.41** | C-23 |
| V-03 | 60.0 (4/4) | 30.0 (3/3) | 8.82 (15/17) | **98.82** | C-23, C-24 |
| V-04 | 60.0 (4/4) | 30.0 (3/3) | 10.0 (17/17) | **100.00** | -- |
| V-05 | 60.0 (4/4) | 30.0 (3/3) | 10.0 (17/17) | **100.00** | -- |

---

## V-01: T-GUARD Scope Pinned (C-23 single-axis)

**Axis**: C-23 exact scope vocabulary at initialization (single-axis)
**Hypothesis**: C-23 requires the T-GUARD scope to use the exact vocabulary "any required typed slot, phase block, or gate item absent from the document." R5 V-05 used "Any required typed slot, phase block, or gate item is missing or empty" -- close but not vocabulary-pinned to C-23's pass condition. V-01 tests whether nailing the exact scope language satisfies C-23 independently of any completion declaration. C-24 fails by design: Phase 13 contains no explicit completion-state declaration. An empty table at Phase 13 reads as ambiguous state.

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
| T-05 | F-row linkage absent | Sign-off block references no F-row by ID, or F-ROW ANCHOR slot missing from either signatory | C-15, C-21 |
| T-06 | Sequence inverted | Assumption or risk register appears after recommendation in document | C-17 |
| T-GUARD | Sentinel -- catch-all | Any required typed slot, phase block, or gate item absent from the document | All aspirational |

**Amendment Rows** (populate during writing -- cite the TRIGGER field for each row):

| TRIGGER | Criterion | Phase | Amendment Type | Gap Description | OWNER | NEXT ACTION | DEADLINE |
|---------|-----------|-------|----------------|-----------------|-------|-------------|---------|
| | | | | | | | |

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

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. These are the exact field names. Do not substitute synonyms. "Observable Event" fails for TRIGGER CONDITION. "Fallback" fails for MITIGATION. Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 10.5: PREREQUISITE GATE

Complete before Phase 11. Each item is a named binary -- "complete" or "not complete." No prose summaries. If any item is "not complete," fire T-GUARD and add amendment row with TRIGGER: T-GUARD.

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

Both sign-off blocks required. F-ROW ANCHOR is a typed slot independently required in both the PM block and the Architect block. Neither block is complete without naming an F-row ID in its own F-ROW ANCHOR slot. Omitting F-ROW ANCHOR from either block fires T-05 -- add amendment row with TRIGGER: T-05.

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

All three sections required. Each entry carries OWNER, NEXT ACTION, and DEADLINE as typed slots, plus a TRIGGER field citing the T-NN that generated it. DEADLINE must be specific (sprint name, named date, or milestone) -- "TBD" and blank fail.

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

Review the Phase 0 Amendment Rows. For each populated row, confirm the gap is addressed or escalated. Write the final table reconciliation status.

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

## V-02: Completion Declaration Exact (C-24 single-axis)

**Axis**: C-24 exact completion declaration (single-axis)
**Hypothesis**: C-24 requires the amendment table to carry an explicit completion-state declaration reading "T-GUARD enforced all requirements successfully -- no violations detected" (or vocabulary-pinned equivalent). V-02 tests whether this declaration satisfies C-24 independently of T-GUARD scope precision. T-GUARD scope uses generic language ("any structural block or item not covered by T-01 through T-06") that omits the required "typed slot / phase block / gate item" vocabulary. C-23 fails by design: the T-GUARD scope is descriptive but not vocabulary-pinned to C-23's pass condition. C-24 passes because Phase 13 contains the exact declaration.

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
| T-05 | F-row linkage absent | Sign-off block references no F-row by ID, or F-ROW ANCHOR slot missing from either signatory | C-15, C-21 |
| T-06 | Sequence inverted | Assumption or risk register appears after recommendation in document | C-17 |
| T-GUARD | Catch-all | Any structural block or item not covered by T-01 through T-06 is absent or empty | All aspirational |

**Amendment Rows** (populate during writing -- cite the TRIGGER field for each row):

| TRIGGER | Criterion | Phase | Amendment Type | Gap Description | OWNER | NEXT ACTION | DEADLINE |
|---------|-----------|-------|----------------|-----------------|-------|-------------|---------|
| | | | | | | | |

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

Minimum 2 A-NN entries. If fewer, fire T-04. Validation plan requires a concrete action.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. If fewer, fire T-04. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register. Failure modes are conditions that invalidate the recommendation.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise, not a risk category]
  TRIGGER CONDITION:  [Observable event confirming activation -- who observes it,
                       what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback option -- name the option
                       letter or next action; "reconsider" and "revisit" fail]
```

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. Exact field names only. No synonym substitution. Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 10.5: PREREQUISITE GATE

Complete before Phase 11. Named binaries only. If any item is "not complete," fire T-GUARD and add amendment row with TRIGGER: T-GUARD.

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

Both sign-off blocks required. F-ROW ANCHOR independently required in both PM and Architect blocks. Omitting F-ROW ANCHOR from either block fires T-05 -- add amendment row with TRIGGER: T-05.

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

All three sections required. Each entry carries OWNER, NEXT ACTION, DEADLINE, and TRIGGER as typed slots. DEADLINE must be specific.

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

Review the Phase 0 Amendment Rows. For each populated row, confirm the gap is addressed or escalated. If the Amendment Rows table is empty, state: **"T-GUARD enforced all requirements successfully -- no violations detected."**

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

## V-03: Baseline Contrast (Neither C-23 nor C-24)

**Axis**: Baseline contrast -- generic T-GUARD scope, no completion declaration
**Hypothesis**: Establishes the R6 baseline score when neither C-23 nor C-24 is addressed. This is structurally equivalent to R5 V-05 before R6 criteria are applied: T-GUARD is present with generic scope and C-22's traceable chain works, but the scope vocabulary does not pin to C-23's pass condition and Phase 13 contains no completion-state declaration. Both C-23 and C-24 fail by design. This variation provides the empirical lower bound for R6 -- the score a prompt achieves when its amendment table machinery is complete (C-18, C-22) but the two new R6 criteria are absent.

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
| T-05 | F-row linkage absent | Sign-off block references no F-row by ID, or F-ROW ANCHOR slot missing from either signatory | C-15, C-21 |
| T-06 | Sequence inverted | Assumption or risk register appears after recommendation in document | C-17 |
| T-GUARD | Catch-all | Any structural gap not covered by T-01 through T-06 | All aspirational |

**Amendment Rows** (populate during writing -- cite the TRIGGER field for each row):

| TRIGGER | Criterion | Phase | Amendment Type | Gap Description | OWNER | NEXT ACTION | DEADLINE |
|---------|-----------|-------|----------------|-----------------|-------|-------------|---------|
| | | | | | | | |

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none found, fire T-01 and add row with TRIGGER: T-01. Provide 2-3 sentence inline assessment as fallback.

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
  1 (rare):      [Named condition -- specific to this project]
  3 (plausible): [Named typical-trouble condition -- specific to this project]
  5 (likely):    [Named near-certain condition -- specific to this project]

IMPACT ANCHORS (this project, this decision):
  1 (negligible): [Named concrete low-impact outcome for this project]
  3 (moderate):   [Named medium-impact consequence for this project]
  5 (severe):     [Named high-impact outcome -- not a severity label]
```

All risk fields use separate P and I numeric scores. Holistic L/M/H labels fail.

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

Minimum 2 A-NN entries. If fewer, fire T-04.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. If fewer, fire T-04. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise, not a risk category]
  TRIGGER CONDITION:  [Observable event confirming activation -- who observes it,
                       what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback option -- name the option
                       letter or next action; "reconsider" and "revisit" fail]
```

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. Exact field names only. Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 10.5: PREREQUISITE GATE

Complete before Phase 11. Named binaries only. If any item is "not complete," fire T-GUARD and add amendment row with TRIGGER: T-GUARD.

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

Both sign-off blocks required. F-ROW ANCHOR independently required in both PM and Architect blocks. Omitting F-ROW ANCHOR from either block fires T-05 -- add amendment row with TRIGGER: T-05.

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

All three sections required. Each entry carries OWNER, NEXT ACTION, DEADLINE, and TRIGGER as typed slots. DEADLINE must be specific.

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

Review the Phase 0 Amendment Rows. For each populated row, confirm the gap is addressed or escalated. Write the final table reconciliation status.

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

## V-04: Inertia-Forward Framing (C-23 + C-24 + inertia axis)

**Axis**: C-23 + C-24 combined, with inertia-forward framing for Option 0 (variation axis)
**Hypothesis**: C-23 and C-24 pass together cleanly when combined with an orthogonal framing axis. The inertia-forward axis quantifies the do-nothing option as a computable cost rather than a qualitative risk: INERTIA COST is the P*I-weighted cost-of-staying per sprint using Phase 4 anchors, and every alternative must name its INERTIA OFFSET -- the sprint count at which its cumulative investment crosses below the do-nothing drift curve. This is not a rubric criterion but operationalizes the Accumulation field from Phase 5 into a decision-relevant number. T-GUARD uses exact C-23 scope vocabulary; Phase 13 uses exact C-24 completion declaration. Both new criteria pass; no other criteria are compromised.

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
| T-05 | F-row linkage absent | Sign-off block references no F-row by ID, or F-ROW ANCHOR slot missing from either signatory | C-15, C-21 |
| T-06 | Sequence inverted | Assumption or risk register appears after recommendation in document | C-17 |
| T-GUARD | Sentinel -- catch-all | Any required typed slot, phase block, or gate item absent from the document | All aspirational |

**Amendment Rows** (populate during writing -- cite the TRIGGER field for each row):

| TRIGGER | Criterion | Phase | Amendment Type | Gap Description | OWNER | NEXT ACTION | DEADLINE |
|---------|-----------|-------|----------------|-----------------|-------|-------------|---------|
| | | | | | | | |

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none found, fire T-01 and add row with TRIGGER: T-01. Provide 2-3 sentence inline assessment as fallback.

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

Define project-specific anchors before writing any options. INERTIA COST in Phase 5 uses these same anchors.

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

Option 0 receives two quantification fields in addition to the standard anatomy. These fields make the do-nothing cost computable and comparable across alternatives.

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they address or avoid the problem |
| Pros | Low switching cost, familiarity, zero migration risk |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [Metric that degrades per sprint -- name metric and rate of drift] |
| **INERTIA COST** | [P*I per sprint: the risk-weighted cost of remaining on Option 0 for one sprint. Use Phase 4 P and I scores for the primary accumulation risk. Format: P=[N] x I=[N] = [N] per sprint. Name the accumulation metric.] |

**Architect note**: Deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 6: Alternatives (Minimum 3)

All fields required. Missing any field fires T-02 -- add amendment row with TRIGGER: T-02. Each alternative must name its INERTIA OFFSET: the sprint count at which the alternative's cumulative implementation cost crosses below the Option 0 inertia curve.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size assumption + key dependencies |
| **INERTIA OFFSET** | [Sprint N: the crossover point at which this option's cumulative cost falls below Option 0's INERTIA COST curve. Compute as: Effort cost / (Option 0 INERTIA COST per sprint). State the sprint number and the assumption about team velocity.] |

**Architect constraint check**: C-NN compliance or named exception with justification.

---

### Phase 7: Comparison Matrix

Joint PM/Architect table. Columns = all options including Option 0. Rows = 4-6 dimensions. No empty cells. Required dimensions: effort, team control, adoption friction, time to value, risk P*I, inertia offset (sprint crossover).

---

### Phase 8: Assumption Register

Minimum 2 A-NN entries. If fewer, fire T-04. Validation plan requires a concrete action.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. If fewer, fire T-04. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register. Failure modes are conditions that invalidate the recommendation.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise, not a risk category]
  TRIGGER CONDITION:  [Observable event confirming activation -- who observes it,
                       what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback option -- name the option
                       letter or next action; "reconsider" and "revisit" fail]
```

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. Exact field names only. No synonym substitution. Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 10.5: PREREQUISITE GATE

Complete before Phase 11. Named binaries only. If any item is "not complete," fire T-GUARD and add amendment row with TRIGGER: T-GUARD.

```
PREREQUISITE GATE
  [ ] Assumption register: >= 2 A-NN entries with validation plans   [complete / not complete]
  [ ] Risk register: >= 2 R-NN entries with P, I, P*I scores         [complete / not complete]
  [ ] Failure mode register: >= 2 F-NN entries with MITIGATION named  [complete / not complete]
  [ ] Assumption register precedes this gate in document sequence     [complete / not complete]
  [ ] Risk register precedes this gate in document sequence           [complete / not complete]
  [ ] F-row labels canonical (FAILURE MODE / TRIGGER CONDITION /
      MITIGATION -- no synonyms used)                                 [complete / not complete]
  [ ] Option 0 INERTIA COST field present with P*I per sprint stated  [complete / not complete]

GATE STATUS: [OPEN -- proceed to Phase 11 | BLOCKED -- resolve items above first]
```

---

### Phase 11: Recommendation -- Independent Dual Signature

Both sign-off blocks required. F-ROW ANCHOR independently required in both PM and Architect blocks. Omitting F-ROW ANCHOR from either block fires T-05 -- add amendment row with TRIGGER: T-05.

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

All three sections required. Each entry carries OWNER, NEXT ACTION, DEADLINE, and TRIGGER as typed slots. DEADLINE must be specific.

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

Review the Phase 0 Amendment Rows. For each populated row, confirm the gap is addressed or escalated. If the Amendment Rows table is empty, state: **"T-GUARD enforced all requirements successfully -- no violations detected."**

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

## V-05: Sentinel-First + COMPLETION STATUS Typed Slot (Full Integration)

**Axis**: Sentinel-first trigger ordering + COMPLETION STATUS as Phase 0 typed slot
**Hypothesis**: Two structural advances beyond V-04. First: T-GUARD appears as the first entry in the trigger definition table, before T-01 through T-06. C-23 requires the sentinel to appear "in the trigger definition section at table initialization" -- not at any specific position -- but sentinel-first ordering changes enforcement semantics: unenumerated gaps route to T-GUARD before specific triggers are consulted, surfacing unknown structural absences at the earliest opportunity. Second: COMPLETION STATUS is a typed slot defined in Phase 0 at initialization (PENDING) and updated to the exact C-24 vocabulary at Phase 13. The declaration is structurally in the amendment table from initialization -- not appended at completion -- which means C-24's "amendment table includes an explicit completion-state declaration" is satisfied at document structure level, not just at review time. Both C-23 and C-24 pass; all 17 aspirational criteria pass.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Initialize the Amendment Tracking Table (Phase 0) before writing Phase 1. Complete the PREREQUISITE GATE before Phase 11. Role labels mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 0: Amendment Tracking Table

Initialize before writing any other phase. Each trigger rule carries a stable named ID. T-GUARD is listed first: unenumerated gaps route to T-GUARD before any specific trigger is consulted. When a trigger fires, add a row to the Amendment Rows section citing the trigger ID in the TRIGGER field. Do not assemble rows retrospectively -- populate during writing.

**Trigger Rules:**

| ID | Trigger Rule | Fires When | Criterion(s) |
|----|--------------|-----------|--------------|
| T-GUARD | Sentinel -- catch-all | Any required typed slot, phase block, or gate item absent from the document | All aspirational |
| T-01 | Scout gap | No scout artifact found in any search path | C-10 |
| T-02 | Option incomplete | Required field absent in any option (Description / Pros / Cons / Risk / Effort) | C-02 |
| T-03 | Decision frame gap | TEMPORAL ANCHOR or INACTION CONSEQUENCE field missing | C-13 |
| T-04 | Register thin | Assumption or risk register has fewer than 2 entries | C-08 |
| T-05 | F-row linkage absent | Sign-off block references no F-row by ID, or F-ROW ANCHOR slot missing from either signatory | C-15, C-21 |
| T-06 | Sequence inverted | Assumption or risk register appears after recommendation in document | C-17 |

**Amendment Rows** (populate during writing -- cite the TRIGGER field for each row):

| TRIGGER | Criterion | Phase | Amendment Type | Gap Description | OWNER | NEXT ACTION | DEADLINE |
|---------|-----------|-------|----------------|-----------------|-------|-------------|---------|
| | | | | | | | |

**COMPLETION STATUS**: PENDING -- updated at Phase 13 to either "T-GUARD enforced all requirements successfully -- no violations detected." (if Amendment Rows is empty) or "Amendment rows populated; see rows above." (if any rows were added).

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none found, fire T-01 (specific trigger) and add row with TRIGGER: T-01. Provide 2-3 sentence inline assessment as fallback.

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

Minimum 2 A-NN entries. If fewer, fire T-04. Validation plan requires a concrete action.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 R-NN entries. If fewer, fire T-04. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Failure Mode Register

Minimum 2 F-NN entries. Distinct from Risk Register. Failure modes are conditions that invalidate the recommendation.

```
F-NN:
  FAILURE MODE:       [Named failure -- precise, not a risk category]
  TRIGGER CONDITION:  [Observable event confirming activation -- who observes it,
                       what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback option -- name the option
                       letter or next action; "reconsider" and "revisit" fail]
```

Canonical labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION. Exact field names only. No synonym substitution. Each F-NN cross-references its A-NN or R-NN entry.

---

### Phase 10.5: PREREQUISITE GATE

Complete before Phase 11. Named binaries only. If any item is "not complete," fire T-GUARD (first in trigger table) and add amendment row with TRIGGER: T-GUARD.

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

Both sign-off blocks required. F-ROW ANCHOR independently required in both PM and Architect blocks. Omitting F-ROW ANCHOR from either block fires T-05 -- add amendment row with TRIGGER: T-05.

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

All three sections required. Each entry carries OWNER, NEXT ACTION, DEADLINE, and TRIGGER as typed slots. DEADLINE must be specific.

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

Review the Phase 0 Amendment Rows. For each populated row, confirm the gap is addressed or escalated. Update the Phase 0 COMPLETION STATUS slot:

- If Amendment Rows is empty: set COMPLETION STATUS to **"T-GUARD enforced all requirements successfully -- no violations detected."**
- If Amendment Rows contains rows: set COMPLETION STATUS to **"Amendment rows populated; [N] enforcement failures recorded -- see rows above."**

The COMPLETION STATUS field in Phase 0 is the authoritative completion record. Phase 13 updates it; it is not a separate statement.

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
