Written to `simulations/quest/variations/scout-inertia-variations-R13-2026-03-17.md`.

---

## scout-inertia -- Quest Variate R13

**Rubric**: v13 (C-series) | **Formula**: aspirational_pass / 36 * 10
**New criteria**: C-41, C-42, C-43, C-44

---

### Variation Summary

| Variation | Axis | Threading Vocabulary | Gate Heading | Key Hypothesis |
|-----------|------|---------------------|--------------|----------------|
| **V-01** | Inertia framing (single) | STATUS QUO | `PASS BEFORE ADVANCING -- HAVE BOTH STATUS QUO BRIDGES BEEN POPULATED?` | "STATUS QUO" is the most semantically precise domain-axis term for C-42; visually distinct from scaffold-management vocabulary |
| **V-02** | Output format (single) | INERTIA THREAT | `STOP BEFORE PROCEEDING -- HAVE BOTH INERTIA THREAT BRIDGES BEEN POPULATED?` | "INERTIA THREAT" draws from the skill's own canonical terminology, making C-42 threading feel native; "STOP BEFORE PROCEEDING" tests an alternative C-44 imperative |
| **V-03** | Phrasing register (single) | DEFAULT OPTION | `DO NOT ADVANCE UNTIL -- HAVE BOTH Q3 AND Q4 DEFAULT OPTION BRIDGES BEEN POPULATED?` | "BOTH Q3 AND Q4" is the strongest C-43 form per rubric note — names artifact identities, count determinable from heading alone without reading gate body |
| **V-04** | Role sequence + Lifecycle (combined) | INCUMBENT | `PASS BEFORE ADVANCING -- HAVE BOTH INCUMBENT BRIDGES BEEN POPULATED?` | Reversed role sequence (threat score declared in Stage 0 before failure modes) primes author to write evidence for a pre-stated verdict; numbered stages enforce gate position |
| **V-05** | All axes combined | STATUS QUO COMPETITOR | `PASS BEFORE ADVANCING -- HAVE BOTH STATUS QUO COMPETITOR BRIDGES BEEN POPULATED?` | Compound domain term combines axis framing (STATUS QUO) + structural role (COMPETITOR); passes C-42 identification test as an unambiguous domain term |

---

### R13 Structural Decisions

**C-41** — All five variations add `[VOCAB Q3 COMMAND]` co-located with the Q3 table and `[VOCAB Q4 COMMAND]` co-located with the Q4 table, independent of the gate-level `[VOCAB BRIDGE COMPLETION COMMAND]` (C-37). Both must be present for C-41 to pass; partial coverage fails.

**C-42** — The three canonical C-36 bracket elements in each variation (`[VOCAB PRIMARY KEY RULE]`, `[VOCAB CITATION INTEGRITY RULE]`, `[VOCAB BRIDGE COMPLETION COMMAND]`) all share the threading vocabulary term. C-41's per-artifact commands extend the thread but are not the three counted for C-36/C-42.

**C-43** — V-01/V-02/V-04/V-05 use bare `"BOTH"` (compact, unambiguous count of two). V-03 uses `"BOTH Q3 AND Q4"` — the explicit enumeration form listed in the rubric note as the strongest C-43 satisfier.

**C-44** — Three distinct imperative forms tested across five variations: `"PASS BEFORE ADVANCING"` (enforcement directive), `"STOP BEFORE PROCEEDING"` (alternative enforcement), `"DO NOT ADVANCE UNTIL"` (conditional prohibition). The prior baseline `"BRIDGE COMPLETION GATE"` fails C-44 — it names the gate's type, not the author's required action.
 three distinct bracket-labeled obligations; C-42 requires
those three to share a domain-axis word drawn from inertia domain terms ("STATUS QUO",
"INERTIA THREAT", "DEFAULT OPTION", "INCUMBENT") -- not from scaffold management vocabulary
("BRIDGE", "GATE", "COMMAND" alone do not satisfy C-42).

The three canonical C-36 elements in every variation:
1. Primary key rule label (C-34): `[VOCAB PRIMARY KEY RULE]`
2. Citation integrity label (C-35): `[VOCAB CITATION INTEGRITY RULE]`
3. Bridge completion command (C-37): `[VOCAB BRIDGE COMPLETION COMMAND]`

All three share the threading vocabulary term. The C-41 per-artifact commands
(`[VOCAB Q3 COMMAND]`, `[VOCAB Q4 COMMAND]`) are additional bracket elements extending
the vocabulary thread but are not the three counted for C-36/C-42.

### C-43 -- Explicit count quantifier in gate heading interrogative

The interrogative component must name an exact count:
- V-01/V-02/V-04/V-05: bare "BOTH" (exactly two artifacts)
- V-03: "BOTH Q3 AND Q4" (explicit enumeration -- strongest C-43 form; artifact names in
  heading make count determinable without reading gate body)

### C-44 -- Action-imperative structural marker before `--`

The marker component must command the author's behavior, not describe the gate's type:
- V-01/V-04/V-05: "PASS BEFORE ADVANCING" -- enforcement directive
- V-02: "STOP BEFORE PROCEEDING" -- alternative enforcement form
- V-03: "DO NOT ADVANCE UNTIL" -- conditional prohibition form (rubric lists this as passing)

"BRIDGE COMPLETION GATE" (prior baseline) fails C-44: it names the gate's structural type,
not the author's required action.

---

## V-01 -- Inertia framing axis

**Axis**: Inertia framing (single)
**Threading vocabulary**: STATUS QUO
**Gate heading**: `PASS BEFORE ADVANCING -- HAVE BOTH STATUS QUO BRIDGES BEEN POPULATED?`
**C-41**: `[STATUS QUO Q3 COMMAND]` at Q3; `[STATUS QUO Q4 COMMAND]` at Q4
**C-42 elements**: `[STATUS QUO PRIMARY KEY RULE]` + `[STATUS QUO CITATION INTEGRITY RULE]`
+ `[STATUS QUO BRIDGE COMPLETION COMMAND]`
**Hypothesis**: "STATUS QUO" is the most semantically precise domain-axis term for C-42
vocabulary threading. It names the competitor axis directly, passes the C-42 identification
test ("can a reader identify this as a scout-inertia scaffold from the shared vocabulary
element alone?"), and is visually distinct from scaffold-management vocabulary.

---

```
## FAIL-FIRST DECLARATION -- THE STATUS QUO

[FAIL-FIRST RULE]: The status quo is the competitor. It does not need a product manager,
a demo, or a roadmap to win -- it wins by default. Every team that does not adopt this
feature is actively choosing the status quo. Map the status quo's failure modes first.
Every defeat condition and switching cost threshold derives from a documented failure mode.
No defeat condition is valid without a traceable failure mode behind it.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> C-01): maps each FM-[N] to the role
  experiencing the failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): maps each FM-[N] to its triggering
  condition and measurable threshold

---

## SECTION 1 -- THE STATUS QUO'S STRUCTURAL WEAKNESSES: FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the status quo workaround breaks,
produces errors, causes rework, or hits a scale ceiling. REJECT generic descriptions --
"slow" or "manual" alone fails. "CSV export silently truncates rows at 65,536 with no
error message" passes. ASSIGN FM-[N] identifiers to each row. MINIMUM 2 rows required.

[STATUS QUO PRIMARY KEY RULE]: Assign all FM-[N] identifiers here first. No FM-[N] may
appear in any downstream section of this scaffold without a corresponding row assigned in
this table. Every defeat condition in Section 5 must trace back to a row in this inventory.

| FM-[N] | Failure description (specific mechanism, e.g., CSV truncates silently at 65,536 rows) | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|--------------------------------------------------------------------------------------|------------------------------------|-----------------------------|-----------------------------|
| FM-1   |                                                                                      |                                    |                             |                             |
| FM-2   |                                                                                      |                                    |                             |                             |

---

## Q3 -- FM->ACTOR BRIDGE

[STATUS QUO Q3 COMMAND]: For each FM-[N] in Section 1, name the specific role experiencing
the failure. REJECT "users" or "the team" -- role names must be specific job titles or
functional team names. Populate this table completely before authoring Q4.

| FM-[N] | Role experiencing the failure (specific job title / team) | Role-level consequence (e.g., 2 hours manual rework per incident) |
|--------|----------------------------------------------------------|-------------------------------------------------------------------|
| FM-1   |                                                          |                                                                   |
| FM-2   |                                                          |                                                                   |

---

## Q4 -- FM->TRIGGER BRIDGE

[STATUS QUO Q4 COMMAND]: For each FM-[N] in Section 1, name the triggering condition and
measurable threshold. REJECT subjective descriptions -- thresholds must carry a number and
a unit. Populate this table completely before the completion gate.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## PASS BEFORE ADVANCING -- HAVE BOTH STATUS QUO BRIDGES BEEN POPULATED?

[STATUS QUO BRIDGE COMPLETION COMMAND]: Confirm Q3 and Q4 are fully populated before
proceeding to Sections 2 through 5. Do not author the workaround profile or defeat
conditions while any bridge row is empty. An incomplete bridge leaves defeat conditions
without actor attribution and trigger chain traceability.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> C-01)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

If either shows N: return to Section 1 and complete the missing bridge before proceeding.

---

## SECTION 2 -- STATUS QUO WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific status quo -- the exact tool name, file type, or manual
procedure currently in use. NOT "a manual process." NAME the specific role performing it.
QUANTIFY the ongoing cost with a number and a unit (e.g., 2 hours/week, $400/month).

| Workaround (specific: tool / file type / procedure) | Role performing it | Ongoing cost (number + unit, e.g., 2 hours/week) | In active use since (e.g., 18 months) |
|-----------------------------------------------------|--------------------|--------------------------------------------------|---------------------------------------|
|                                                     |                    |                                                  |                                       |

---

## SECTION 3 -- SWITCHING COST ANALYSIS

[C-02 COMMAND]: QUANTIFY the cost for a team to switch away from the status quo. MINIMUM
2 cost categories. Each row must carry a number and a unit. NAME the role bearing each
cost. REJECT ranges without specifics.

| Cost category (e.g., training time, migration effort, disruption window) | Role bearing it | Estimated cost (number + unit, e.g., 3 days, $1,200) | One-time or recurring |
|-------------------------------------------------------------------------|-----------------|------------------------------------------------------|-----------------------|
|                                                                         |                 |                                                      |                       |
|                                                                         |                 |                                                      |                       |

---

## SECTION 4 -- INERTIA THREAT SCORE

[C-03 COMMAND]: DECLARE the inertia threat score. Default is HIGH. Deviation from HIGH
requires quantified evidence -- cite switching cost totals, workaround duration, or team
size from Sections 2-3. A qualitative judgment alone does not justify deviation.

| Threat score (HIGH / MEDIUM / LOW) | Justification (cite numbers; if HIGH: "default HIGH -- no evidence of low switching cost or short workaround duration") |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------|
|                                    |                                                                                                                        |

---

## SECTION 5 -- DEFEAT CONDITIONS

[STATUS QUO CITATION INTEGRITY RULE]: Every defeat condition must cite an FM-[N] from
Section 1. A defeat condition row without an FM-[N] citation is invalid and must be
removed or corrected. Verify: each row's FM-[N] cell must match a row assigned in
Section 1's inventory.

[C-04 COMMAND]: NAME at least 2 falsifiable defeat conditions -- specific, observable
conditions under which teams would abandon the status quo. Each condition must cite
FM-[N] from Section 1 and a measurable threshold from Q4. "Teams switch when they see
the value" fails -- every row must name a testable, observable condition.

| DC-[N] | Defeat condition (falsifiable: observable event or threshold crossing) | FM-[N] cited | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type / segment |
|--------|-----------------------------------------------------------------------|--------------|------------------------------------------------------|---------------------|
| DC-1   |                                                                       |              |                                                      |                     |
| DC-2   |                                                                       |              |                                                      |                     |

---

## SECTION 6 -- COMPLETENESS CHECKLIST

| Item | Criterion | Satisfied? (Y / N) |
|------|-----------|---------------------|
| C-01: Workaround mapped | Status quo tool/procedure named; specific role named; ongoing cost has a number and a unit | |
| C-02: Switching costs quantified | >=2 cost categories; each has a number and unit; role bearing each cost named | |
| C-03: Threat score declared | Score declared; HIGH is default; deviation requires cited quantified evidence | |
| C-04: Defeat conditions authored | >=2 falsifiable conditions; each cites FM-[N] from Section 1; each has a measurable threshold | |
| C-05: Failure modes inventoried | >=2 specific failure modes in Section 1; no generic descriptions accepted | |
```

---

## V-02 -- Output format axis

**Axis**: Output format (single) -- all-tabular with explicit column-level quantification cues
**Threading vocabulary**: INERTIA THREAT
**Gate heading**: `STOP BEFORE PROCEEDING -- HAVE BOTH INERTIA THREAT BRIDGES BEEN POPULATED?`
**C-41**: `[INERTIA THREAT Q3 COMMAND]` at Q3; `[INERTIA THREAT Q4 COMMAND]` at Q4
**C-42 elements**: `[INERTIA THREAT PRIMARY KEY RULE]` + `[INERTIA THREAT CITATION INTEGRITY RULE]`
+ `[INERTIA THREAT BRIDGE COMPLETION COMMAND]`
**Hypothesis**: "INERTIA THREAT" draws from the skill description's canonical terminology
("inertia threat score" appears in the skill definition), making C-42 vocabulary threading
feel native rather than applied. "STOP BEFORE PROCEEDING" is an alternative C-44 imperative
form that tests whether the action-imperative criterion is vocabulary-agnostic.

---

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

[FAIL-FIRST RULE]: The inertia threat is the option to do nothing. It competes without a
name, a vendor, a champion, or a deadline. Its switching cost is the total cost of adopting
the feature. Map the inertia threat's structural weaknesses before deriving any defeat
condition. Every DC row must trace to a failure mode documented in Section 1. Failure modes
first; defeat conditions follow from them, never precede them.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> C-01): actor role per failure mode
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): trigger and measurable threshold per
  failure mode

---

## SECTION 1 -- INERTIA THREAT FAILURE MODE INVENTORY

[C-05 COMMAND]: NAME every specific failure mode where the inertia threat (current
workaround) produces errors, causes rework, or hits a scale ceiling. Each failure mode
must be concrete -- name the specific mechanism, not the category. "Slow" fails;
"CSV export silently truncates at 65,536 rows with no error message" passes.
MINIMUM 2 rows. ASSIGN FM-[N] identifiers here.

[INERTIA THREAT PRIMARY KEY RULE]: All FM-[N] identifiers are assigned in this table and
only here. No FM-[N] may be referenced in Section 5 or any downstream section without a
corresponding row in this inventory. The inventory is the sole source of FM identifiers.

| FM-[N] | Failure description (mechanism-level, observable) | Actor / role | Trigger condition | Frequency |
|--------|--------------------------------------------------|--------------|-------------------|-----------|
| FM-1   |                                                  |              |                   |           |
| FM-2   |                                                  |              |                   |           |

---

## Q3 -- FM->ACTOR BRIDGE

[INERTIA THREAT Q3 COMMAND]: Map each FM-[N] to the specific role experiencing the
failure. Specific job title or functional team required. Do not author Q4 until this
table is fully populated.

| FM-[N] | Specific role experiencing failure (job title / team name) | Consequence to that role |
|--------|-----------------------------------------------------------|--------------------------|
| FM-1   |                                                           |                          |
| FM-2   |                                                           |                          |

---

## Q4 -- FM->TRIGGER BRIDGE

[INERTIA THREAT Q4 COMMAND]: Map each FM-[N] to its triggering condition and measurable
threshold. Quantify every threshold -- a number and a unit are required for each row. Do
not proceed to the completion gate until this table is fully populated.

| FM-[N] | Triggering condition | Measurable threshold (number + unit, e.g., >10MB, >3 failures/week) |
|--------|---------------------|---------------------------------------------------------------------|
| FM-1   |                     |                                                                     |
| FM-2   |                     |                                                                     |

---

## STOP BEFORE PROCEEDING -- HAVE BOTH INERTIA THREAT BRIDGES BEEN POPULATED?

[INERTIA THREAT BRIDGE COMPLETION COMMAND]: Do not author Sections 2 through 5 until both
bridge artifacts show Y below. Return to Section 1 if either shows N. Defeat conditions
authored without bridge completion lack actor attribution or trigger chain traceability.

| Bridge artifact                                | Complete? (Y / N) |
|------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> C-01)  |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## SECTION 2 -- WORKAROUND PROFILE

[C-01 COMMAND]: NAME the specific inertia threat -- the exact tool, file type, or procedure
currently in use. NAME the role performing it. QUANTIFY the ongoing cost with a number and
a unit. Not "a manual process" -- name the actual tool or workflow.

| Specific workaround (tool / file type / procedure) | Role performing it | Ongoing cost (number + unit, e.g., 2 hours/week) | Duration (e.g., 18 months) |
|----------------------------------------------------|--------------------|--------------------------------------------------|----------------------------|
|                                                    |                    |                                                  |                            |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: Quantify the cost of switching away from the inertia threat. MINIMUM 2
cost categories. Each category must carry a number and a unit. Name the role bearing each
cost. Ranges without a specific estimate are rejected.

| Cost category | Role bearing it | Estimated cost (number + unit, e.g., 3 days) | One-time or recurring |
|---------------|-----------------|---------------------------------------------|-----------------------|
|               |                 |                                             |                       |
|               |                 |                                             |                       |

---

## SECTION 4 -- THREAT SCORE

[C-03 COMMAND]: Declare the inertia threat score. Default is HIGH. Deviation from HIGH
requires cited quantified evidence from Sections 2-3. A qualitative judgment alone fails.

| Threat score (HIGH / MEDIUM / LOW) | Evidence base (cite numbers from Sections 2-3; or state "default HIGH") |
|------------------------------------|-------------------------------------------------------------------------|
|                                    |                                                                         |

---

## SECTION 5 -- DEFEAT CONDITIONS

[INERTIA THREAT CITATION INTEGRITY RULE]: Every defeat condition must cite an FM-[N] from
Section 1. No FM-[N] may appear in this table that was not assigned in Section 1. Verify
each row's FM-[N] citation before proceeding to Section 6.

[C-04 COMMAND]: Name at least 2 falsifiable defeat conditions -- specific, observable events
or threshold crossings under which the inertia threat loses. Each must cite FM-[N] from
Section 1 and a measurable threshold from Q4. Generic conditions are rejected.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] cited | Measurable threshold | Team type |
|--------|------------------------------------------|--------------|---------------------|-----------|
| DC-1   |                                          |              |                     |           |
| DC-2   |                                          |              |                     |           |

---

## SECTION 6 -- COMPLETENESS CHECKLIST

| Item | Criterion | Satisfied? (Y / N) |
|------|-----------|---------------------|
| C-01: Workaround mapped | Specific tool/role named; ongoing cost quantified (number + unit) | |
| C-02: Switching costs quantified | >=2 categories; each has number + unit; role named | |
| C-03: Threat score declared | Score present; HIGH default; deviation requires cited evidence | |
| C-04: Defeat conditions authored | >=2 falsifiable; each cites FM-[N] from Section 1; each has threshold | |
| C-05: Failure modes inventoried | >=2 specific failure modes in Section 1; no generic descriptions | |
```

---

## V-03 -- Phrasing register axis

**Axis**: Phrasing register (single) -- full imperative register; explicit artifact enumeration
in gate heading for maximum C-43 strength
**Threading vocabulary**: DEFAULT OPTION
**Gate heading**: `DO NOT ADVANCE UNTIL -- HAVE BOTH Q3 AND Q4 DEFAULT OPTION BRIDGES BEEN POPULATED?`
**C-41**: `[DEFAULT OPTION Q3 COMMAND]` at Q3; `[DEFAULT OPTION Q4 COMMAND]` at Q4
**C-42 elements**: `[DEFAULT OPTION PRIMARY KEY RULE]` + `[DEFAULT OPTION CITATION INTEGRITY RULE]`
+ `[DEFAULT OPTION BRIDGE COMPLETION COMMAND]`
**Hypothesis**: "BOTH Q3 AND Q4" is the strongest C-43 form per rubric note -- it names the
specific artifacts, making the count determinable from the heading alone without reading the
gate body. "DO NOT ADVANCE UNTIL" is a conditional prohibition form listed in the rubric as a
passing C-44 imperative. "DEFAULT OPTION" names the structural role the workaround plays and
passes C-42's domain-vocabulary identification test.

---

```
## FAIL-FIRST DECLARATION -- THE DEFAULT OPTION

[FAIL-FIRST RULE]: The default option is not doing nothing -- it is choosing the current
workaround over the total cost of switching. Teams keep their default option because the
failure modes are tolerable, invisible, or below the threshold where switching is worth
the disruption. This analysis surfaces those failure modes and the measurable thresholds
that make them intolerable. Failure modes come first. Defeat conditions are derived from
them, never invented independently.

Bridge artifacts required before defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> C-01): role bearing each failure mode
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): trigger and threshold per failure mode

---

## SECTION 1 -- THE DEFAULT OPTION'S BREAKING POINTS: FAILURE MODE INVENTORY

[C-05 COMMAND]: IDENTIFY every specific failure mode where the default option (current
workaround) breaks, produces incorrect results, or causes manual rework. ASSIGN FM-[N]
identifiers to each row. Name the mechanism, not the category -- "data loss" fails;
"silent row truncation at 65,536 with no error" passes. MINIMUM 2 failure modes required.

[DEFAULT OPTION PRIMARY KEY RULE]: Assign all FM-[N] identifiers here and only here.
No FM-[N] identifier may appear in Section 5 without a corresponding row in this table.
Downstream references are citations; this table is the sole assignment authority.

| FM-[N] | Failure description (mechanism-level, not category) | Role experiencing it | Trigger condition | Frequency |
|--------|-----------------------------------------------------|----------------------|-------------------|-----------|
| FM-1   |                                                     |                      |                   |           |
| FM-2   |                                                     |                      |                   |           |

---

## Q3 -- FM->ACTOR BRIDGE

[DEFAULT OPTION Q3 COMMAND]: For each FM-[N] above, identify the specific role experiencing
the failure. Name a specific function or job title -- not "users" or "the team." Complete
this table fully before proceeding to Q4.

| FM-[N] | Role experiencing failure (specific job title / function) | Role-level impact |
|--------|----------------------------------------------------------|-------------------|
| FM-1   |                                                          |                   |
| FM-2   |                                                          |                   |

---

## Q4 -- FM->TRIGGER BRIDGE

[DEFAULT OPTION Q4 COMMAND]: For each FM-[N] above, name the triggering condition and
measurable threshold. Every threshold must carry a number and a unit. Complete this table
before the completion gate.

| FM-[N] | Triggering condition | Measurable threshold (number + unit, e.g., >10MB, >3 failures/week) |
|--------|---------------------|---------------------------------------------------------------------|
| FM-1   |                     |                                                                     |
| FM-2   |                     |                                                                     |

---

## DO NOT ADVANCE UNTIL -- HAVE BOTH Q3 AND Q4 DEFAULT OPTION BRIDGES BEEN POPULATED?

[DEFAULT OPTION BRIDGE COMPLETION COMMAND]: Do not proceed to Sections 2 through 5 until
both Q3 and Q4 show Y below. Both bridges must be complete for defeat conditions to have
valid actor attribution and trigger chain traceability. If either is N, stop and return to
Section 1 to complete the missing bridge artifact.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> C-01)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## SECTION 2 -- DEFAULT OPTION WORKAROUND PROFILE

[C-01 COMMAND]: Name the specific default option -- the exact tool, file type, or manual
procedure. Name the specific role performing it. Quantify the ongoing cost as a number
with a unit. Do not use open-ended ranges.

| Default option (exact tool / file type / procedure) | Role performing it | Ongoing cost (number + unit) | In use since |
|-----------------------------------------------------|--------------------|------------------------------|--------------|
|                                                     |                    |                              |              |

---

## SECTION 3 -- SWITCHING COST

[C-02 COMMAND]: Identify at least 2 switching cost categories. Quantify each as a number
with a unit. Name the role bearing each cost. This section establishes why the default
option persists despite its failure modes.

| Cost category | Role bearing it | Estimated cost (number + unit) | One-time or recurring |
|---------------|-----------------|--------------------------------|-----------------------|
|               |                 |                                |                       |
|               |                 |                                |                       |

---

## SECTION 4 -- INERTIA THREAT SCORE

[C-03 COMMAND]: Declare the threat score for the default option. Default is HIGH. If not
HIGH, cite specific quantified evidence from Sections 2-3. Qualitative framing alone is
rejected.

| Threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH (cite specific numbers from Sections 2-3) |
|------------------------------------|---------------------------------------------------------------------|
|                                    |                                                                     |

---

## SECTION 5 -- DEFEAT CONDITIONS

[DEFAULT OPTION CITATION INTEGRITY RULE]: Every DC row must cite an FM-[N] from Section 1.
A DC row without an FM-[N] citation is structurally invalid and must be removed or
corrected. Verify that each cited FM-[N] exists in Section 1 before submitting.

[C-04 COMMAND]: Name at least 2 specific, falsifiable conditions under which the default
option loses. Each condition must cite FM-[N] from Section 1 and a measurable threshold
from Q4. Conditions that cannot be objectively verified are rejected.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] cited | Threshold (from Q4) | Segment |
|--------|------------------------------------------|--------------|---------------------|---------|
| DC-1   |                                          |              |                     |         |
| DC-2   |                                          |              |                     |         |

---

## SECTION 6 -- COMPLETENESS CHECKLIST

| Item | Criterion | Satisfied? (Y / N) |
|------|-----------|---------------------|
| C-01: Workaround mapped | Specific default option named; specific role named; ongoing cost has number + unit | |
| C-02: Switching costs quantified | >=2 cost categories; each has number + unit; role bearing each cost named | |
| C-03: Threat score declared | Score declared; HIGH is default; deviation requires quantified evidence | |
| C-04: Defeat conditions authored | >=2 falsifiable conditions; each cites FM-[N] from Section 1; each has measurable threshold | |
| C-05: Failure modes inventoried | >=2 mechanism-level failure modes in Section 1; no generic descriptions | |
```

---

## V-04 -- Role sequence + Lifecycle combined

**Axis**: Role sequence (threat score declared before failure modes) + Lifecycle emphasis
(numbered stages with explicit authoring sequence)
**Threading vocabulary**: INCUMBENT
**Gate heading**: `PASS BEFORE ADVANCING -- HAVE BOTH INCUMBENT BRIDGES BEEN POPULATED?`
**C-41**: `[INCUMBENT Q3 COMMAND]` at Q3 subsection; `[INCUMBENT Q4 COMMAND]` at Q4 subsection
**C-42 elements**: `[INCUMBENT PRIMARY KEY RULE]` + `[INCUMBENT CITATION INTEGRITY RULE]`
+ `[INCUMBENT BRIDGE COMPLETION COMMAND]`
**Hypothesis**: Reversing the standard role sequence (threat score in Stage 0 before failure
modes in Stage 1) primes the author to write failure modes as evidence for a pre-stated
severity verdict. Stage-numbered lifecycle makes bridge gate position structurally mandatory.
"INCUMBENT" tests C-42 with an anthropomorphic domain term connoting tenure, integration
depth, and organizational lock-in.

---

```
## FAIL-FIRST DECLARATION -- THE INCUMBENT WORKAROUND

[FAIL-FIRST RULE]: The incumbent workaround is the competitor with the longest tenure, the
deepest integration, and the most scar tissue. It does not lose because a new feature exists
-- it loses only when a specific, documented failure mode crosses a measurable threshold and
the switching cost is justified. Declare the threat posture first. Then surface the failure
modes that justify or challenge that posture. Every defeat condition traces to a failure mode.

Bridge artifacts required before Stage 5 defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> C-01): actor role per failure mode
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): trigger and threshold per failure mode

Authoring sequence:
- Stage 0: Threat posture (C-03) -- declare score before collecting evidence
- Stage 1: Failure mode inventory (C-05) -- evidence base for the declared posture
- Stage 2: Bridge stage -- Q3 + Q4 + completion gate
- Stage 3: Workaround profile (C-01) -- name the incumbent concretely
- Stage 4: Switching cost (C-02) -- quantify what keeps teams with the incumbent
- Stage 5: Defeat conditions (C-04) -- conditions under which the incumbent loses
- Stage 6: Completeness checklist

---

## STAGE 0 -- INCUMBENT THREAT POSTURE

[C-03 COMMAND]: Declare the incumbent threat score before collecting evidence. Default is
HIGH -- the incumbent always starts with maximum inertia. If you anticipate deviation from
HIGH, state a PROVISIONAL score with a hypothesis now; verify or revise it after Stage 4
evidence is complete. Any non-HIGH score without Stage 4 evidence must be marked PROVISIONAL.

| Threat score (HIGH / MEDIUM / LOW) | Posture (if HIGH: "default HIGH -- evidence collection in Stage 1"; if PROVISIONAL: state hypothesis) |
|------------------------------------|-------------------------------------------------------------------------------------------------------|
|                                    |                                                                                                       |

---

## STAGE 1 -- INCUMBENT FAILURE MODE INVENTORY

[C-05 COMMAND]: Name every specific failure mode where the incumbent workaround breaks,
produces errors, causes rework, or hits a scale ceiling. Each row must describe a mechanism,
not a category. ASSIGN FM-[N] identifiers here. MINIMUM 2 rows.

[INCUMBENT PRIMARY KEY RULE]: All FM-[N] identifiers are assigned in this table and only
here. No FM-[N] may appear in Stage 5 without a corresponding row assigned in this table.
The FM Inventory is the sole assignment authority for failure mode identifiers.

| FM-[N] | Failure description (mechanism, e.g., CSV truncates silently at 65,536 rows) | Role affected | Trigger condition | Frequency |
|--------|-----------------------------------------------------------------------------|---------------|-------------------|-----------|
| FM-1   |                                                                             |               |                   |           |
| FM-2   |                                                                             |               |                   |           |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE

[INCUMBENT Q3 COMMAND]: Map each FM-[N] from Stage 1 to the specific role experiencing the
failure. Specific job title or functional team required. Complete Q3 before Q4.

| FM-[N] | Specific role (job title or team name) | Role-level consequence (e.g., 2 hours rework per incident) |
|--------|---------------------------------------|------------------------------------------------------------|
| FM-1   |                                       |                                                            |
| FM-2   |                                       |                                                            |

### Q4 -- FM->TRIGGER BRIDGE

[INCUMBENT Q4 COMMAND]: Map each FM-[N] from Stage 1 to its triggering condition and
measurable threshold. Number + unit required for every threshold. Complete Q4 before the
completion gate.

| FM-[N] | Triggering condition | Measurable threshold (number + unit, e.g., >10MB, >3 failures/week) |
|--------|---------------------|---------------------------------------------------------------------|
| FM-1   |                     |                                                                     |
| FM-2   |                     |                                                                     |

### PASS BEFORE ADVANCING -- HAVE BOTH INCUMBENT BRIDGES BEEN POPULATED?

[INCUMBENT BRIDGE COMPLETION COMMAND]: Both Q3 and Q4 must show Y before Stage 3 is
authored. Incomplete bridges leave defeat conditions in Stage 5 without actor attribution
or trigger chain traceability.

| Bridge artifact                                | Populated? (Y / N) |
|------------------------------------------------|--------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> C-01)  |                    |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                    |

---

## STAGE 3 -- INCUMBENT WORKAROUND PROFILE

[C-01 COMMAND]: Name the specific incumbent workaround -- the exact tool, file type, or
manual procedure. Name the specific role performing it. Quantify the ongoing cost with a
number and a unit.

| Incumbent workaround (specific: tool / file type / procedure) | Role performing it | Ongoing cost (number + unit, e.g., 2 hours/week) | In use since |
|--------------------------------------------------------------|--------------------|--------------------------------------------------|--------------|
|                                                              |                    |                                                  |              |

---

## STAGE 4 -- SWITCHING COST

[C-02 COMMAND]: Quantify the cost for a team to switch from the incumbent. Minimum 2 cost
categories. Each row requires a number and a unit. Name the role bearing the cost. After
completing this table, revisit Stage 0 and revise any PROVISIONAL threat score.

| Cost category | Role bearing it | Estimated cost (number + unit) | One-time or recurring |
|---------------|-----------------|--------------------------------|-----------------------|
|               |                 |                                |                       |
|               |                 |                                |                       |

---

## STAGE 5 -- DEFEAT CONDITIONS

[INCUMBENT CITATION INTEGRITY RULE]: Every defeat condition must cite an FM-[N] from Stage
1's inventory. A defeat condition without FM-[N] citation is invalid. Verify each row's
FM-[N] cell matches a row assigned in Stage 1 before proceeding to Stage 6.

[C-04 COMMAND]: Name at least 2 falsifiable defeat conditions -- specific, observable
conditions under which the incumbent loses. Each must cite FM-[N] from Stage 1 and a
measurable threshold from Q4.

| DC-[N] | Defeat condition (specific, falsifiable) | FM-[N] cited | Threshold (from Q4) | Segment |
|--------|------------------------------------------|--------------|---------------------|---------|
| DC-1   |                                          |              |                     |         |
| DC-2   |                                          |              |                     |         |

---

## STAGE 6 -- COMPLETENESS CHECKLIST

| Item | Criterion | Satisfied? (Y / N) |
|------|-----------|---------------------|
| C-01: Workaround mapped | Specific incumbent tool/procedure named; specific role named; ongoing cost has number + unit | |
| C-02: Switching costs quantified | >=2 categories; each has number + unit; role bearing each cost named | |
| C-03: Threat score declared | Score declared in Stage 0; HIGH is default; non-HIGH requires quantified evidence from Stage 4 | |
| C-04: Defeat conditions authored | >=2 falsifiable; each cites FM-[N] from Stage 1; each has measurable threshold from Q4 | |
| C-05: Failure modes inventoried | >=2 mechanism-level failure modes in Stage 1; no generic descriptions | |
```

---

## V-05 -- All axes combined

**Axis**: All axes -- inertia framing + output format + phrasing register + role sequence +
lifecycle emphasis
**Threading vocabulary**: STATUS QUO COMPETITOR
**Gate heading**: `PASS BEFORE ADVANCING -- HAVE BOTH STATUS QUO COMPETITOR BRIDGES BEEN POPULATED?`
**C-41**: `[STATUS QUO COMPETITOR Q3 COMMAND]` at Q3; `[STATUS QUO COMPETITOR Q4 COMMAND]` at Q4
**C-42 elements**: `[STATUS QUO COMPETITOR PRIMARY KEY RULE]` + `[STATUS QUO COMPETITOR
CITATION INTEGRITY RULE]` + `[STATUS QUO COMPETITOR BRIDGE COMPLETION COMMAND]`
**Hypothesis**: "STATUS QUO COMPETITOR" is a compound domain term combining both axes of
identification -- STATUS QUO names the axis (option to do nothing), COMPETITOR names the
structural role in the feature decision. C-42's domain-vocabulary identification test passes
because a reader can identify this as a scout-inertia scaffold from "STATUS QUO COMPETITOR"
alone. The compound form is unambiguously domain-derived, not scaffold management vocabulary.
All five axis variations combined: (1) inertia framing with STATUS QUO COMPETITOR as central
naming axis; (2) all-tabular output; (3) imperative register throughout; (4) threat posture
declared in Stage 0 before failure modes; (5) numbered stages with explicit authoring sequence.

---

```
## FAIL-FIRST DECLARATION -- THE STATUS QUO COMPETITOR

[FAIL-FIRST RULE]: The status quo competitor is the current workaround positioned as an
explicit competitor in the feature decision. It wins every evaluation where the team cannot
name a specific reason to switch -- which is every evaluation where failure modes are
invisible, thresholds are untested, and switching costs are unknown. This scaffold makes all
three visible. Map the status quo competitor's failure surface first. Every other section is
evidence for or against the conclusion that it loses. No defeat condition is authored before
its source failure mode is documented.

Bridge artifacts required before Stage 5 defeat conditions:
- **Q3 -- FM->ACTOR BRIDGE** (closes C-05 -> C-01): who experiences each failure
- **Q4 -- FM->TRIGGER BRIDGE** (closes C-05 -> C-04): when each failure activates

Authoring sequence:
- Stage 0: Status quo competitor threat posture (C-03) -- state the default verdict first
- Stage 1: Failure mode inventory (C-05) -- surface the evidence
- Stage 2: Bridge stage -- Q3 + Q4 + completion gate
- Stage 3: Workaround profile (C-01) -- name the competitor concretely
- Stage 4: Switching cost (C-02) -- quantify what keeps teams loyal
- Stage 5: Defeat conditions (C-04) -- conditions under which it loses
- Stage 6: Completeness checklist

---

## STAGE 0 -- STATUS QUO COMPETITOR THREAT POSTURE

[C-03 COMMAND]: DECLARE the threat score for the status quo competitor before collecting
evidence. DEFAULT IS HIGH -- the status quo competitor always starts with maximum inertia.
If prior evidence suggests lower switching cost, state a PROVISIONAL score with a specific
citation. Verify and finalize after Stage 4. Any non-HIGH score without Stage 4 evidence
remains PROVISIONAL at submission.

| Threat score (HIGH / MEDIUM / LOW) | Posture statement (e.g., "default HIGH -- evidence collection in Stage 1" or cite specific prior evidence) |
|------------------------------------|------------------------------------------------------------------------------------------------------------|
|                                    |                                                                                                            |

---

## STAGE 1 -- STATUS QUO COMPETITOR FAILURE SURFACE: FAILURE MODE INVENTORY

[C-05 COMMAND]: IDENTIFY every specific failure mode where the status quo competitor breaks,
produces incorrect results, causes manual rework, or hits a ceiling. Each row must describe
the failure mechanism at a specific level -- "slow" fails; "batch job silently skips records
above 50,000 rows with no log entry" passes. ASSIGN FM-[N] identifiers. MINIMUM 2 rows.

[STATUS QUO COMPETITOR PRIMARY KEY RULE]: All FM-[N] identifiers are assigned in this table
and nowhere else. Any FM-[N] in Stage 5 without a row in this table is invalid. This
inventory is the sole authority for failure mode identifier assignment in this scaffold.

| FM-[N] | Failure description (mechanism-level, observable) | Role affected | Trigger condition | Frequency |
|--------|--------------------------------------------------|---------------|-------------------|-----------|
| FM-1   |                                                  |               |                   |           |
| FM-2   |                                                  |               |                   |           |

---

## STAGE 2 -- BRIDGE STAGE

### Q3 -- FM->ACTOR BRIDGE

[STATUS QUO COMPETITOR Q3 COMMAND]: Map each FM-[N] from Stage 1 to the specific role
experiencing the failure. REJECT generic role labels -- name the specific function or job
title. Complete this table fully before proceeding to Q4.

| FM-[N] | Specific role (function / job title) | Consequence to that role (quantified if possible) |
|--------|--------------------------------------|---------------------------------------------------|
| FM-1   |                                      |                                                   |
| FM-2   |                                      |                                                   |

### Q4 -- FM->TRIGGER BRIDGE

[STATUS QUO COMPETITOR Q4 COMMAND]: Map each FM-[N] from Stage 1 to its triggering
condition and measurable threshold. Every threshold must carry a number and a unit. Complete
this table before the completion gate.

| FM-[N] | Triggering condition | Measurable threshold (number + unit, e.g., >10MB, >3 failures/week) |
|--------|---------------------|---------------------------------------------------------------------|
| FM-1   |                     |                                                                     |
| FM-2   |                     |                                                                     |

### PASS BEFORE ADVANCING -- HAVE BOTH STATUS QUO COMPETITOR BRIDGES BEEN POPULATED?

[STATUS QUO COMPETITOR BRIDGE COMPLETION COMMAND]: Both bridge artifacts must be complete
before Stages 3 through 5 are authored. A partial bridge produces defeat conditions with no
actor chain or no trigger chain. Do not proceed if either row shows N.

| Bridge artifact                                | Complete? (Y / N) |
|------------------------------------------------|-------------------|
| Q3 -- FM->Actor bridge (closes C-05 -> C-01)  |                   |
| Q4 -- FM->Trigger bridge (closes C-05 -> C-04)|                   |

---

## STAGE 3 -- STATUS QUO COMPETITOR PROFILE

[C-01 COMMAND]: NAME the specific status quo competitor -- the exact tool, file type, or
manual procedure. NAME the specific role performing it. QUANTIFY the ongoing cost with a
number and a unit. Not "a manual process" -- name the actual tool or workflow.

| Status quo competitor (exact tool / file type / procedure) | Role performing it | Ongoing cost (number + unit, e.g., 2 hours/week) | In use since (e.g., 18 months) |
|------------------------------------------------------------|--------------------|-------------------------------------------------|-------------------------------|
|                                                            |                    |                                                 |                               |

---

## STAGE 4 -- SWITCHING COST ANALYSIS

[C-02 COMMAND]: QUANTIFY the cost for a team to switch away from the status quo competitor.
MINIMUM 2 categories. Number + unit required for each. Name the role bearing each cost.
After completing this table, revisit Stage 0 and finalize any PROVISIONAL threat score.

| Cost category | Role bearing it | Estimated cost (number + unit) | One-time or recurring |
|---------------|-----------------|--------------------------------|-----------------------|
|               |                 |                                |                       |
|               |                 |                                |                       |

---

## STAGE 5 -- DEFEAT CONDITIONS

[STATUS QUO COMPETITOR CITATION INTEGRITY RULE]: Every defeat condition must cite an FM-[N]
from Stage 1's inventory. No FM-[N] may appear in this table that was not assigned in Stage
1. Verify the FM-[N] citation for each row before final submission.

[C-04 COMMAND]: NAME at least 2 falsifiable defeat conditions -- specific, observable events
or threshold crossings under which the status quo competitor loses. Each must cite FM-[N]
from Stage 1 and a measurable threshold from Q4.

| DC-[N] | Defeat condition (specific, observable) | FM-[N] cited | Threshold (from Q4) | Evidence type | Team segment |
|--------|----------------------------------------|--------------|---------------------|---------------|--------------|
| DC-1   |                                        |              |                     |               |              |
| DC-2   |                                        |              |                     |               |              |

---

## STAGE 6 -- COMPLETENESS CHECKLIST

| Item | Criterion | Satisfied? (Y / N) |
|------|-----------|---------------------|
| C-01: Workaround mapped | Specific status quo competitor named (exact tool/procedure); role named; ongoing cost has number + unit | |
| C-02: Switching costs quantified | >=2 categories; each has number + unit; role bearing each cost named | |
| C-03: Threat score declared | Score declared in Stage 0; HIGH is default; non-HIGH requires quantified evidence from Stage 4 | |
| C-04: Defeat conditions authored | >=2 falsifiable conditions; each cites FM-[N] from Stage 1; each has measurable threshold from Q4 | |
| C-05: Failure modes inventoried | >=2 mechanism-level failure modes in Stage 1; no generic descriptions | |
```

---

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Workaround prompt with specific/role/number+unit in all |
| C-02 | PASS | PASS | PASS | PASS | PASS | Switching cost prompt with >=2 categories in all |
| C-03 | PASS | PASS | PASS | PASS | PASS | Threat score section; default HIGH stated; deviation rule present |
| C-04 | PASS | PASS | PASS | PASS | PASS | Defeat conditions with FM-[N] citation requirement in all |
| C-05 | PASS | PASS | PASS | PASS | PASS | FM Inventory with >=2 rows and mechanism-level requirement |
| C-34 | PASS | PASS | PASS | PASS | PASS | [VOCAB PRIMARY KEY RULE] in Section/Stage 1 in all |
| C-35 | PASS | PASS | PASS | PASS | PASS | [VOCAB CITATION INTEGRITY RULE] at defeat conditions in all |
| C-36 | PASS | PASS | PASS | PASS | PASS | Three distinct bracket elements present in all |
| C-37 | PASS | PASS | PASS | PASS | PASS | [VOCAB BRIDGE COMPLETION COMMAND] in gate block body in all |
| C-38 | PASS | PASS | PASS | PASS | PASS | FAIL-FIRST heading has domain subtitle in all |
| C-39 | PASS | PASS | PASS | PASS | PASS | Gate heading is binary question form in all |
| C-40 | PASS | PASS | PASS | PASS | PASS | All checklist items have C-NN: prefix in all |
| C-41 | PASS | PASS | PASS | PASS | PASS | [VOCAB Q3 COMMAND] at Q3 and [VOCAB Q4 COMMAND] at Q4 in all |
| C-42 | PASS | PASS | PASS | PASS | PASS | Three C-36 elements share domain vocabulary in all |
| C-43 | PASS | PASS | PASS* | PASS | PASS | *V-03 uses "BOTH Q3 AND Q4" (strongest form) |
| C-44 | PASS | PASS | PASS | PASS | PASS | Imperative marker before -- in all |

**C-43 vocabulary comparison**:
- V-01/V-02/V-04/V-05: "BOTH" -- names exact count (two), compact form
- V-03: "BOTH Q3 AND Q4" -- names exact count AND artifact names; rubric explicitly lists this
  form; count is determinable from heading alone without reading gate body

**C-44 vocabulary comparison**:
- V-01/V-04/V-05: "PASS BEFORE ADVANCING" -- enforcement directive
- V-02: "STOP BEFORE PROCEEDING" -- alternative enforcement form
- V-03: "DO NOT ADVANCE UNTIL" -- conditional prohibition form (rubric lists as passing)
  All three command the author's behavior rather than describing the gate's structural type.

**C-42 threading vocabulary comparison**:
- STATUS QUO: precise axis term; two words; maximum semantic clarity; non-scaffold vocabulary
- INERTIA THREAT: drawn from skill description canonical language; single compound noun
- DEFAULT OPTION: names structural role (path of least resistance); two-word noun phrase
- INCUMBENT: anthropomorphic; shortest; connotes tenure and lock-in; single word
- STATUS QUO COMPETITOR: compound; combines axis identification + structural role; longest;
  passes C-42 test as compound-but-unambiguous domain term
