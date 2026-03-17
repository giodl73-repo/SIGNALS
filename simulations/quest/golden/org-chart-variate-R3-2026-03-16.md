---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R3
rubric_version: v3
status: variate
---

# org-chart Variate -- Round 3

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v3 (C-01--C-05 essential; A-01--A-07 aspirational /7)
**Round:** R3 -- single-axis V-01/V-02/V-03, combined V-04/V-05

**R2 ceiling:** V-05/R2 scored 100/100 under v2. Under v3, A-06 and A-07 are new targets:
- A-06: contract items carry explicit section codes (CF-NN) that downstream steps cite back to
- A-07: role type annotation register published as explicit lookup table with "Used In" tracking column

R3 adds both signals at their natural anchor points. All variations preserve the complete
essential+recommended+aspirational A-01--A-05 structure from R2.

---

## Round 3 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | section-code traceability | Pre-flight contract assigns CF-NN codes; each downstream section header cites the code(s) it satisfies | Back-citation turns coverage into a structural property: any uncited CF code is a visible missing section; any section missing a citation is orphaned output. A-06 becomes self-enforcing at the point of production |
| V-02 | annotation register with Used-In column | ROLE-TYPE-CLASSIFICATION emits an ANNOTATION-REGISTER table (Role / Domain Type / Used In) that downstream sections must reference by register row | Propagation gaps surface as empty Used-In cells rather than silent omissions; the model must declare downstream use before producing it, creating a forward-declared dependency map |
| V-03 | inertia framing adversarial-first | Adversarial burden statement placed BEFORE the pre-flight contract and BEFORE the roles block; sub-sections framed as evidence-loading not checklist-filling | Adversarial framing at the prompt top (not only inside the inertia section) primes the model to treat the flat case as a genuine competitor throughout the entire run, improving the steelman quality |
| V-04 | combined A-06 + A-07 | Pre-flight contract with CF codes + ANNOTATION-REGISTER with Used-In column | Both traceability mechanisms address independent layers; combining them creates fully auditable output: no criterion can silently fail and no annotation can silently propagate without a register reference |
| V-05 | full integration | R2-V-05 foundation (adversarial framing + flat-branch investment note + exclusion clause + DO/DO NOT register) + A-06 CF codes at contract header + A-07 ANNOTATION-REGISTER after classification | R2-V-05 placed all five v2 aspirational signals at natural anchors. Adding A-06 and A-07 at their natural anchors (pre-flight header and classification block) targets 7/7 aspirational under v3 while preserving 5/5 essential |

---

## V-01 -- Section-Code Traceability: Pre-Flight Contract with CF Back-Citations

**axis:** section-code traceability (A-06)
**hypothesis:** A pre-flight contract that assigns a CF-NN code to each structural requirement,
combined with a rule that each downstream section header MUST cite the code it satisfies, makes
coverage auditable inside the output itself. An uncited CF code is a visible missing section. A
section header without a citation is orphaned output. This makes A-06 self-enforcing at the point
of production rather than relying on the model remembering each criterion globally. Falsifiable:
if downstream section headers still appear without CF citations despite the rule, structural
back-citation cannot be enforced through prompt design alone.

---

You are running `/org-chart {topic}`.

---

PRE-FLIGHT CONTRACT

The following contract codes govern this output. Every major section MUST cite the CF code(s)
it satisfies in its section header in the format `(satisfies CF-NN)` or `(satisfies CF-NN, CF-MM)`.
A section header without a citation is incomplete. A CF code with no citing section is a missing
section.

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all other types third |
| CF-03 | Inertia: Case for Staying Flat -- mechanism evidence table >= 2 data rows + FLAT-CASE-CLOSED separator |
| CF-04 | Inertia: How We Coordinate Today -- distinct content, no duplication from mechanism table |
| CF-05 | Inertia: Rebuttal naming one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE line (closed-set rating) + verdict declaration + re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount table: Decides and Escalates as separate columns (NOT merged); >= 2 area rows + Total |
| CF-09 | Operating rhythm table >= 3 distinct rows: one ROB, one shiproom, one governance |
| CF-10 | Committee Charters: all 5 fields; Quorum as N-of-M fraction; Escalates names specific destination |
| CF-11 | ORG-ELEMENT REGISTER with all 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citations in every Why-It-Applies cell |

DO NOT begin any section until you have identified which CF codes it satisfies.
DO write the citing CF codes in the section header before writing that section's content.
DO NOT produce any section that cannot be mapped to at least one CF code.

---

SECTION 1 -- ROLES (satisfies CF-01, CF-02)

Check `.craft/roles/` for role files relevant to {topic} or the domain.

If roles exist, write before any other section:
```
ROLES-LOADED:
- [role name] -- [one-line description from role file]
```

If no roles exist, write:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
- [role name] -- [description]
```

DO NOT write any other section until this block exists.

Immediately after, produce ROLE-TYPE-CLASSIFICATION in strict three-tier order:
Engineering types first, then Operations types, then PM / Design / Research / Other types.
Format each entry as `- [role name] -- [domain type]`.
Domain type from closed set: Engineering / PM / Design / Operations / Research / Other.
DO NOT interleave tiers.
DO annotate each Key Roles cell in the headcount table as `[role name] ([domain type])`.
DO annotate each Membership field in committee charters as `[role name] ([domain type])`.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate line is present.

---

SECTION 2 -- INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

DO write this section before any org diagram.

**Sub-section 2a -- Case for Staying Flat (satisfies CF-03)**

Produce a three-column mechanism evidence table:

| Mechanism Name | Type | Frequency / Participants |
|----------------|------|--------------------------|

Type column values: Channel / Informal Role / Recurring Cadence / Shared Artifact (closed set).
Include >= 2 data rows. Name a specific, observable mechanism in each row.

After writing the table, count data rows (header excluded).
If count < 2: add missing rows.
Then emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2b before this separator.

**Sub-section 2b -- How We Coordinate Today (satisfies CF-04)**

Inventory coordination patterns currently in active use: channels, cadences, informal roles,
artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 2a mechanism table.

**Sub-section 2c -- Rebuttal (satisfies CF-05)**

Name the coordination failure the flat-team case cannot answer.
Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

**Sub-section 2d -- VERDICT (satisfies CF-06)**

Open with:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing mechanism count and failure mode]`
Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1).

Then choose exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating by name.
Write a re-assessment trigger naming a concrete threshold.
DO NOT write "revisit as the team grows."

DO NOT proceed until pressure line, verdict declaration, and re-assessment trigger are all written.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

SECTION 3 -- ASCII ORG DIAGRAM (satisfies CF-07) [STRUCTURE-WARRANTED only]

DO draw an ASCII hierarchy. DO show >= 2 levels. DO show committees as distinct labeled nodes.
DO use role names from ROLES-LOADED. DO NOT produce a flat list.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

SECTION 4 -- HEADCOUNT BY AREA (satisfies CF-08) [STRUCTURE-WARRANTED only]

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

DO NOT use a single Decision Scope column. Decides and Escalates are separate and both required.
Annotate Key Roles as `[role name] ([domain type])`.
Include >= 2 area rows plus a `**Total**` row.
Decides: decision types owned at this level.
Escalates: decision types referred upward, naming the destination role or forum.

---

SECTION 5 -- OPERATING RHYTHM TABLE (satisfies CF-09)

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Include >= 3 distinct rows: one ROB, one shiproom or gate, one governance meeting.
DO NOT combine two meetings into one row.

---

SECTION 6 -- COMMITTEE CHARTERS (satisfies CF-10)

Write a charter for each governance meeting in the rhythm table.

```
**[Name] Charter**
Purpose: [one sentence]
Membership: [role name] ([domain type]) -- minimum two roles
Decides: [decision types in scope]
Escalates: [named destination] -- NOT "everything not listed under Decides"
Quorum: [N] of [M] member roles required for binding decisions
```

Short-form Quorum "N roles required" does NOT satisfy CF-10. N-of-M fraction required.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

SECTION 7 -- ORG-ELEMENT REGISTER (satisfies CF-11)

```
ORG-ELEMENT REGISTER:
cat-1 (Areas): - [area name] -- headcount: [N]
cat-2 (Committees/Cadences): - [name]
cat-3 (Headcount): - Total headcount: [N]
cat-4 (DRI Roles): - [DRI role]
```

---

SECTION 8 -- ORG EVOLUTION ROADMAP (satisfies CF-12)

| Trigger | Structural Change | Type |
|---------|-------------------|------|

>= 2 rows from different trigger categories.
Row 1: headcount threshold.
Row 2: workload signal, structural symptom, or milestone event.

---

SECTION 9 -- ANTI-PATTERN WATCH (satisfies CF-13)

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|

Open each "Why It Applies Here" cell with: `[element name] (cat-N) -- [one sentence]`.
DO NOT write a cell without the (cat-N) typed syntax. Include >= 2 rows.

---

SECTION ORDER: 1 through 9. DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Annotation Register with Used-In Tracking Column (A-07)

**axis:** annotation register with Used-In column (A-07)
**hypothesis:** Publishing the ROLE-TYPE-CLASSIFICATION as an explicit ANNOTATION-REGISTER lookup
table with a "Used In" tracking column makes role-type propagation gaps visible as empty register
entries rather than silent omissions. The model must declare which downstream sections will
reference each annotation before writing those sections -- creating a forward-declared dependency
map. If a role appears in the Headcount Key Roles cell but is not in its register "Used In" column,
the gap surfaces as a register inconsistency. Falsifiable: if the "Used In" column remains
unpopulated despite the register instruction, the forward-declaration mechanism is not preventing
silent omissions.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ AND REGISTER FIRST

Check `.craft/roles/` for role files relevant to {topic} or the domain.

If roles exist, write before any other section:
```
ROLES-LOADED:
- [role name] -- [one-line description from role file]
```

If no roles exist, write:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
- [role name] -- [description]
```

DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- classify in strict three-tier order: Engineering types first, then Operations
types, then PM / Design / Research / Other types. Complete all entries in one tier before writing
any from the next. DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION:
DO assign each role exactly one type from: Engineering / PM / Design / Operations / Research / Other.
Format: `- [role name] -- [domain type]`.

Immediately after ROLE-TYPE-CLASSIFICATION, emit the ANNOTATION-REGISTER as a lookup table:

```
ANNOTATION-REGISTER:
| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [comma-separated: Headcount-Key-Roles, Charter-Membership, Diagram-Node, Rhythm-DRI] |
```

Rules for the ANNOTATION-REGISTER:
- Every role from ROLE-TYPE-CLASSIFICATION MUST appear as a row.
- The "Used In" column MUST list every downstream section that will reference this role with its
  domain-type annotation. Declare this BEFORE writing those sections.
- Valid Used-In values: Headcount-Key-Roles, Charter-Membership, Diagram-Node, Rhythm-DRI
  (list all that apply, comma-separated).
- A role that will appear in no downstream section must still appear with "Used In: none -- [reason]".
- A downstream annotation not matching a register row is a propagation error.

DO NOT proceed to INERTIA ASSESSMENT until every role has an ANNOTATION-REGISTER entry with
a populated Used-In column.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write this before any org diagrams. DO structure in this exact order:
Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

**Case for Staying Flat**

Produce a three-column mechanism evidence table:

| Mechanism Name | Type | Frequency / Participants |
|----------------|------|--------------------------|

Type values: Channel / Informal Role / Recurring Cadence / Shared Artifact (closed set).
Include >= 2 data rows naming specific, observable mechanisms.
After writing the table, count data rows.
If count < 2: add missing rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin How We Coordinate Today before this separator.

**How We Coordinate Today**

Inventory active coordination patterns: channels, cadences, informal roles, artifacts.
DO NOT re-list entries from the mechanism table above.

**Rebuttal**

Name the coordination failure the flat-team case cannot answer.
Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap.

**VERDICT and Re-assessment Trigger**

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and failure mode]`
Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1).
Choose exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning must reference FLAT-CASE-PRESSURE by name.
Write a re-assessment trigger naming a concrete threshold.
DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia phase gate.
DO show >= 2 levels. DO show committees as distinct labeled nodes.
DO use role names from ROLES-LOADED.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

Annotate Key Roles as `[role name] ([domain type])` -- MUST match a row in ANNOTATION-REGISTER.
Include >= 2 area rows + Total. Separate Decides and Escalates -- DO NOT merge.

---

OPERATING RHYTHM TABLE

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Include >= 3 distinct rows: one ROB, one shiproom, one governance.

---

COMMITTEE CHARTERS

Annotate Membership roles as `[role name] ([domain type])` -- MUST match a row in ANNOTATION-REGISTER.

```
**[Name] Charter**
Purpose: [one sentence]
Membership: [role name] ([domain type]) -- minimum two roles
Decides: [scope]
Escalates: [named destination -- NOT "everything not listed under Decides"]
Quorum: [N] of [M] member roles required for binding decisions
```

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ANNOTATION-REGISTER RECONCILIATION: After completing all charters, verify every Used-In
declaration was honored. Flag any role annotated in a section not listed in its register row.
Flag any register Used-In entry not realized in the actual output.

---

ORG-ELEMENT REGISTER

```
ORG-ELEMENT REGISTER:
cat-1 (Areas): - [area name] -- headcount: [N]
cat-2 (Committees/Cadences): - [name]
cat-3 (Headcount): - Total headcount: [N]
cat-4 (DRI Roles): - [DRI role]
```

---

ORG EVOLUTION ROADMAP

| Trigger | Structural Change | Type |
|---------|-------------------|------|

>= 2 rows from different categories. Row 1: headcount threshold. Row 2: different category.

---

ANTI-PATTERN WATCH

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|

Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`. >= 2 rows.

---

SECTION ORDER: ROLES-LOADED / ROLE-TYPE-CLASSIFICATION / ANNOTATION-REGISTER / Phase Gate /
Inertia Assessment / Phase Gate / ASCII Org / Phase Gate / Headcount / Rhythm / Charters /
Phase Gate / ANNOTATION-REGISTER RECONCILIATION / ORG-ELEMENT REGISTER / Org Evolution Roadmap /
Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Inertia Framing: Adversarial-First Before Any Mechanics

**axis:** inertia framing -- adversarial statement placed before roles block and contract
**hypothesis:** Placing an explicit adversarial burden-of-proof statement at the very top of
the prompt -- before roles, before the contract, before any mechanics -- primes the model to
treat the flat case as a genuine competitor throughout the entire run, not just inside one
section. In R2, adversarial framing appeared inside the inertia section opener. When it appears
at the prompt top, it establishes the operating posture for everything that follows. The four
sub-section structure and FLAT-CASE-CLOSED separator are preserved in full -- this variation
changes where the adversarial frame is set, not what the inertia section contains. Falsifiable:
if the mechanism table and How We Coordinate Today content are no richer under V-03 than the
baseline despite the opening adversarial statement, placement has no measurable effect on
content quality.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness.**
Flatness has inertia advantage. Every org element you propose must earn its existence against a
team that already coordinates informally. The default verdict is CAN-OPERATE-FLAT.
STRUCTURE-WARRANTED is correct only when you can name a specific observable failure that
informal coordination cannot prevent. If you cannot name that failure concretely, the verdict
is wrong.

---

ROLES -- READ FIRST

Check `.craft/roles/` for role files relevant to {topic} or the domain.

If roles exist, write before any other section:
```
ROLES-LOADED:
- [role name] -- [one-line description from role file]
```

If no roles exist, write:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
- [role name] -- [description]
```

DO NOT write any other section until this block exists.

Immediately after, produce ROLE-TYPE-CLASSIFICATION in strict three-tier order:
Engineering types first, then Operations types, then PM / Design / Research / Other types.
Format: `- [role name] -- [domain type]`.
Domain type from: Engineering / PM / Design / Operations / Research / Other.
DO NOT interleave tiers.
DO annotate each Key Roles cell in the headcount table as `[role name] ([domain type])`.
DO annotate each Membership field in committee charters as `[role name] ([domain type])`.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

You are about to make the strongest possible case for flatness. Exhaust the evidence before
you rebut it. If you find yourself writing the rebuttal before the steelman is complete, stop
and return to the steelman.

**Sub-section 1 -- Case for Staying Flat**

Load the evidence for flatness. Produce a three-column mechanism evidence table:

| Mechanism Name | Type | Frequency / Participants |
|----------------|------|--------------------------|

Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact.
Mechanism Name MUST name a specific, observable mechanism -- not "ad-hoc communication."
Include >= 2 data rows.

After writing the table, count data rows.
If count < 2: write missing rows until count >= 2.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator.

**Sub-section 2 -- How We Coordinate Today**

Describe the coordination patterns in active use: channels, cadences, informal leads, artifacts
with frequency and participants. Name what the team actually does.
DO NOT duplicate entries from the mechanism table.

**Sub-section 3 -- Rebuttal**

Only now: name the coordination failure Sub-sections 1 and 2 cannot prevent.
Name a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap.
DO NOT name "team growth" as the failure -- growth is a condition; name the failure mode it causes.

**Sub-section 4 -- VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count from Sub-section 1
and the specific failure from Sub-section 3]`
Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1).
Choose exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning must reference FLAT-CASE-PRESSURE by name.
Write a re-assessment trigger naming a concrete threshold.
DO NOT write "revisit as the team grows."

DO NOT proceed until pressure line, verdict declaration, and re-assessment trigger are all written.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM [STRUCTURE-WARRANTED only]

Draw an ASCII hierarchy. >= 2 levels. Committees as distinct labeled nodes.
Use role names from ROLES-LOADED. DO NOT produce a flat list.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA [STRUCTURE-WARRANTED only]

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

Annotate Key Roles as `[role name] ([domain type])`.
Separate Decides and Escalates -- DO NOT merge into Decision Scope.
>= 2 area rows + Total. Name specific decision types.

---

OPERATING RHYTHM TABLE

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

>= 3 distinct rows: one ROB, one shiproom, one governance.
DO NOT combine two meetings into one row.

---

COMMITTEE CHARTERS

Write a charter for each governance meeting in the rhythm table.

```
**[Name] Charter**
Purpose: [one sentence]
Membership: [role name] ([domain type]) -- minimum two roles
Decides: [scope]
Escalates: [named destination -- NOT "everything not listed under Decides"]
Quorum: [N] of [M] member roles required for binding decisions
```

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ORG-ELEMENT REGISTER

```
ORG-ELEMENT REGISTER:
cat-1 (Areas): - [area name] -- headcount: [N]
cat-2 (Committees/Cadences): - [name]
cat-3 (Headcount): - Total headcount: [N]
cat-4 (DRI Roles): - [DRI role]
```

---

ORG EVOLUTION ROADMAP

| Trigger | Structural Change | Type |
|---------|-------------------|------|

>= 2 rows from different categories. Row 1: headcount threshold.
Row 2: workload signal, structural symptom, or milestone event.

---

ANTI-PATTERN WATCH

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|

Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`.
DO NOT use a cat-N code that doesn't match the REGISTER schema. >= 2 rows.

---

SECTION ORDER: ROLES / ROLE-TYPE-CLASSIFICATION / Phase Gate / Inertia Assessment / Phase Gate /
ASCII Org / Phase Gate / Headcount / Rhythm / Charters / Phase Gate / ORG-ELEMENT REGISTER /
Org Evolution Roadmap / Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Combined: Pre-Flight Contract + Annotation Register (A-06 + A-07)

**axis:** section-code traceability + annotation register with Used-In column
**hypothesis:** A-06 and A-07 address independent traceability layers: A-06 traces structural
criterion coverage (CF codes to output sections), A-07 traces role-type annotation propagation
(register rows to downstream references). Both mechanisms convert silent omissions into visible
gaps at their respective levels. Combining them creates fully auditable output: the CF code layer
exposes missing sections and uncited criteria; the annotation register layer exposes missing type
annotations and propagation gaps. Neither mechanism conflicts with the other (CF-02 governs the
classification step, while CF-codes govern structural sections). Falsifiable: if either layer
still shows silent gaps despite the combined constraint, the two mechanisms are interfering or
one is being dropped in favor of the other.

---

You are running `/org-chart {topic}`.

---

PRE-FLIGHT CONTRACT

Each major section MUST cite its CF code(s) in the header as `(satisfies CF-NN)`.
Uncited CF codes = missing sections.

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order + ANNOTATION-REGISTER with Used-In column |
| CF-03 | Inertia: Case for Staying Flat -- mechanism table >= 2 rows + FLAT-CASE-CLOSED separator |
| CF-04 | Inertia: How We Coordinate Today -- distinct from mechanism table |
| CF-05 | Inertia: Rebuttal -- names specific observable failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 levels; committees as distinct nodes |
| CF-08 | Headcount: separate Decides and Escalates columns; >= 2 areas + Total |
| CF-09 | Rhythm table: >= 3 rows (ROB, shiproom, governance) |
| CF-10 | Committee Charters: 5 fields; Quorum N-of-M; Escalates names destination |
| CF-11 | ORG-ELEMENT REGISTER: all 4 categories |
| CF-12 | Org Evolution Roadmap: >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch: typed (cat-N) citations in every Why-It-Applies cell |

---

SECTION 1 -- ROLES (satisfies CF-01, CF-02)

Check `.craft/roles/` for role files relevant to {topic} or the domain.

Write:
```
ROLES-LOADED:
- [role name] -- [one-line description]
```
or:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
- [role name] -- [description]
```

DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, all other types third.
DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION:
`- [role name] -- [domain type]`
Domain type: Engineering / PM / Design / Operations / Research / Other.

Immediately after ROLE-TYPE-CLASSIFICATION, emit the ANNOTATION-REGISTER:

```
ANNOTATION-REGISTER:
| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [Headcount-Key-Roles, Charter-Membership, Diagram-Node, Rhythm-DRI -- all that apply] |
```

Rules:
- Every role from ROLE-TYPE-CLASSIFICATION MUST appear as a row.
- "Used In" MUST list every section that will reference this role+type annotation.
  Declare this before writing those sections.
- A downstream annotation not matching an ANNOTATION-REGISTER row is a propagation error.
- After completing all downstream sections, reconcile: verify every Used-In declaration was honored.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

SECTION 2 -- INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

DO write before any org diagrams.

**Sub-section 2a -- Case for Staying Flat (satisfies CF-03)**

| Mechanism Name | Type | Frequency / Participants |
|----------------|------|--------------------------|

Type: Channel / Informal Role / Recurring Cadence / Shared Artifact.
>= 2 data rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

**Sub-section 2b -- How We Coordinate Today (satisfies CF-04)**

Inventory active coordination patterns. DO NOT duplicate mechanism table entries.

**Sub-section 2c -- Rebuttal (satisfies CF-05)**

Name the coordination failure. Reference a specific observable.

**Sub-section 2d -- VERDICT (satisfies CF-06)**

`FLAT-CASE-PRESSURE: [rating] -- [justification]`
Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1).
`CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning references FLAT-CASE-PRESSURE.
Re-assessment trigger: concrete threshold.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

SECTION 3 -- ASCII ORG DIAGRAM (satisfies CF-07) [STRUCTURE-WARRANTED only]

>= 2 levels. Committees as distinct labeled nodes. Role names from ROLES-LOADED.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

SECTION 4 -- HEADCOUNT BY AREA (satisfies CF-08) [STRUCTURE-WARRANTED only]

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

Key Roles: `[role name] ([domain type])` -- MUST match ANNOTATION-REGISTER row.
>= 2 area rows + Total. Separate Decides and Escalates. DO NOT merge.

---

SECTION 5 -- OPERATING RHYTHM TABLE (satisfies CF-09)

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

>= 3 rows: one ROB, one shiproom, one governance.

---

SECTION 6 -- COMMITTEE CHARTERS (satisfies CF-10)

```
**[Name] Charter**
Purpose: [one sentence]
Membership: [role name] ([domain type]) -- MUST match ANNOTATION-REGISTER; minimum two roles
Decides: [scope]
Escalates: [named destination -- NOT "everything not listed under Decides"]
Quorum: [N] of [M] member roles required for binding decisions
```

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ANNOTATION-REGISTER RECONCILIATION: Confirm every Used-In declaration was honored.
Flag any propagation gaps.

---

SECTION 7 -- ORG-ELEMENT REGISTER (satisfies CF-11)

```
ORG-ELEMENT REGISTER:
cat-1 (Areas): - [area name] -- headcount: [N]
cat-2 (Committees/Cadences): - [name]
cat-3 (Headcount): - Total headcount: [N]
cat-4 (DRI Roles): - [DRI role]
```

---

SECTION 8 -- ORG EVOLUTION ROADMAP (satisfies CF-12)

| Trigger | Structural Change | Type |
|---------|-------------------|------|

>= 2 rows from different categories. Row 1: headcount threshold. Row 2: different category.

---

SECTION 9 -- ANTI-PATTERN WATCH (satisfies CF-13)

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|

Each "Why It Applies Here": `[element name] (cat-N) -- [one sentence]`. >= 2 rows.

---

SECTION ORDER: 1 through 9 in sequence.
ANNOTATION-REGISTER RECONCILIATION follows Section 6 Phase Gate.
DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: R2-V-05 Foundation + A-06 CF Codes + A-07 Annotation Register

**axis:** all seven aspirational signals at natural anchor points
**hypothesis:** R2-V-05 scored 100/100 under v2 by placing all five aspirational signals at their
natural anchor points -- adversarial framing at the inertia opener, flat-branch investment note
inside the CAN-OPERATE-FLAT block, exclusion clause inside the Escalates field template, all via
DO/DO NOT imperative register. Under v3, A-06 and A-07 are the two additional signals. Their
natural anchors are: CF codes belong in the pre-flight contract header (one-time, before any
section); the ANNOTATION-REGISTER belongs immediately after ROLE-TYPE-CLASSIFICATION (its
natural production point). Adding both at their natural anchors without disturbing any existing
R2 signal placement should achieve 7/7 aspirational under v3 while preserving 5/5 essential and
3/3 recommended. Falsifiable: if composite score is not 100 under v3, at least one of the seven
aspirational signals is not self-executing at its current anchor and needs a different mechanism.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness.**
Flatness has inertia advantage. Every structural element must earn its place by naming a specific
coordination failure it prevents. If you cannot name that failure, the element should not exist.

---

PRE-FLIGHT CONTRACT

Each major section in this output MUST cite the CF code(s) it satisfies in its section header
as `(satisfies CF-NN)`. A section without a CF citation is incomplete.
A CF code not cited by any section is a missing section.

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order + ANNOTATION-REGISTER with Used-In column |
| CF-03 | Inertia: Case for Staying Flat -- mechanism table >= 2 rows + FLAT-CASE-CLOSED separator |
| CF-04 | Inertia: How We Coordinate Today -- distinct content, no duplication |
| CF-05 | Inertia: Rebuttal -- names one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Rhythm table: >= 3 rows (one ROB, one shiproom, one governance) |
| CF-10 | Committee Charters: all 5 fields; Quorum N-of-M fraction; Escalates names specific destination |
| CF-11 | ORG-ELEMENT REGISTER: all 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch: typed (cat-N) citations in every Why-It-Applies cell |

---

ROLES -- DO THIS FIRST (satisfies CF-01, CF-02)

DO check `.craft/roles/` before writing anything.
DO write a ROLES-LOADED block listing every role found: `- [role name] -- [one-line description]`.
DO NOT invent role names that contradict roles already defined.
If no roles exist: DO write `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:`
followed by inferred role entries.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER: Engineering types first, then Operations types, then PM / Design / Research / Other.
DO NOT interleave tiers. Complete all entries in one tier before writing any from the next.

ROLE-TYPE-CLASSIFICATION:
DO assign each role exactly one type from: Engineering / PM / Design / Operations / Research / Other.
Format: `- [role name] -- [domain type]`.
DO NOT skip any role from ROLES-LOADED.

Immediately after ROLE-TYPE-CLASSIFICATION, emit the ANNOTATION-REGISTER:

```
ANNOTATION-REGISTER:
| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [Headcount-Key-Roles, Charter-Membership, Diagram-Node, Rhythm-DRI -- all that apply] |
```

DO include every role as a register row.
DO populate Used-In BEFORE writing downstream sections -- this is a forward declaration.
A downstream annotation NOT matching a register row is a propagation error.
A register Used-In entry not realized in the actual output is an unfulfilled declaration.
DO NOT proceed to INERTIA ASSESSMENT until every role has a populated ANNOTATION-REGISTER entry.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present.

---

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS (satisfies CF-03, CF-04, CF-05, CF-06)

DO write this section before any org diagrams.
DO NOT write an org diagram as the first section.
DO structure in this exact four-sub-section order:
Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

**Sub-section 1 -- Case for Staying Flat (satisfies CF-03)**

DO produce a three-column mechanism evidence table:

| Mechanism Name | Type | Frequency / Participants |
|----------------|------|--------------------------|

Type column MUST contain only: Channel / Informal Role / Recurring Cadence / Shared Artifact.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO include >= 2 data rows.
DO NOT move mechanism-typed table content into Sub-section 2.

After the table, count data rows (header excluded).
If count < 2: write missing rows until count >= 2.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator.

**Sub-section 2 -- How We Coordinate Today (satisfies CF-04)**

DO inventory coordination patterns currently in active use: channels, cadences, informal roles,
artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 mechanism table.

**Sub-section 3 -- Rebuttal (satisfies CF-05)**

DO name the coordination failure the flat-team case cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

**Sub-section 4 -- VERDICT (satisfies CF-06)**

MUST open with:
`FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and specific failure mode]`
Rating MUST be exactly one of: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1).
DO NOT omit this line. DO NOT emit the verdict declaration before this line is present.

After the pressure line, choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference FLAT-CASE-PRESSURE by name.
DO write a re-assessment trigger naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past VERDICT until pressure line, verdict declaration, and re-assessment trigger
are all written.

---

VERDICT BRANCH -- READ AND FOLLOW EXACTLY

```
IF VERDICT IS CAN-OPERATE-FLAT:

  DO SKIP the org diagram section. The org diagram is ABSENT.
  DO SKIP the headcount table section. The headcount table is ABSENT.
  DO NOT draw any ASCII hierarchy.
  DO NOT produce a "simplified" or "compact" org chart.
  DO NOT produce a headcount table in any form.
  A reduced org diagram still fails -- these sections must not exist.

  DO produce a coordination investment note:
    For each mechanism in the Sub-section 1 table, name:
    - What the team invests to preserve it (time, tooling, explicit ownership)
    - What signal would indicate the investment is failing
  DO state the re-assessment trigger from Sub-section 4 prominently.
  DO produce an ownership map (who owns which workstream) and sync cadence.

IF VERDICT IS STRUCTURE-WARRANTED:

  DO proceed to ASCII ORG DIAGRAM.
  DO complete all remaining sections.
```

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present.

---

ASCII ORG DIAGRAM (satisfies CF-07) [STRUCTURE-WARRANTED only]

DO draw an ASCII hierarchy after the inertia phase gate.
DO show >= 2 levels.
DO NOT produce a flat list.
DO show committees as distinct labeled nodes -- NOT embedded in one area's subtree.
DO use role names from ROLES-LOADED.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present.

---

HEADCOUNT BY AREA (satisfies CF-08) [STRUCTURE-WARRANTED only]

DO produce a headcount table: Area | Headcount | Key Roles | Decides | Escalates.
DO NOT use a single Decision Scope column. Decides and Escalates are separate and BOTH REQUIRED.
DO NOT write "owns the area" in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination.
DO annotate Key Roles as `[role name] ([domain type])` -- MUST match ANNOTATION-REGISTER.
DO include >= 2 area rows plus a `**Total**` row.
DO NOT produce only a single aggregate total.

---

OPERATING RHYTHM TABLE (satisfies CF-09)

DO produce a cadence table: Cadence | Frequency | DRI / Owner | Purpose.
DO include >= 3 distinct rows: one ROB, one shiproom or gate, one governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in DRI / Owner where possible.

---

COMMITTEE CHARTERS (satisfies CF-10)

DO write a charter for each governance meeting in the rhythm table.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO include all five fields in every charter.
DO annotate Membership roles as `[role name] ([domain type])` -- MUST match ANNOTATION-REGISTER.

```
**[Name] Charter**
Purpose: [one sentence]
Membership: [role name] ([domain type]) -- minimum two roles
Decides: [decision types in scope]
Escalates: [named destination] -- the text "everything not listed under Decides" does not satisfy CF-10
Quorum: [N] of [M] member roles required for binding decisions
```

Short-form Quorum "N roles required" does NOT satisfy CF-10. N-of-M fraction required.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present.

ANNOTATION-REGISTER RECONCILIATION:
After completing all charters, verify every Used-In declaration was honored.
Flag any role annotated in a section not listed in its register row.
Flag any register Used-In entry not realized in the actual output.

---

ORG-ELEMENT REGISTER (satisfies CF-11)

MUST produce immediately after the charters phase gate. DO NOT skip.

```
ORG-ELEMENT REGISTER:
cat-1 (Areas):
  - [area name] -- headcount: [N]
cat-2 (Committees/Cadences):
  - [name]
cat-3 (Headcount):
  - Total headcount: [N]
cat-4 (DRI Roles):
  - [DRI role]
```

DO NOT proceed to Org Evolution Roadmap until all four categories are populated.

---

ORG EVOLUTION ROADMAP (satisfies CF-12)

DO produce a trigger table: Trigger | Structural Change | Type.
DO NOT label it optional.
DO include >= 2 rows from different trigger categories.
Row 1: headcount threshold trigger.
Row 2: workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

---

ANTI-PATTERN WATCH (satisfies CF-13)

DO produce: Anti-Pattern | Why It Applies Here | Mitigation.
MUST open each "Why It Applies Here" cell with: `[element name] (cat-N) -- [one sentence]`.
DO NOT write a cell without the (cat-N) typed syntax.
DO NOT use a cat-N code that does not match the ORG-ELEMENT REGISTER schema.
DO include >= 2 rows.

---

SECTION ORDER -- DO NOT REORDER, DO NOT OMIT:
1. ROLES-LOADED or ROLES-NOTE (CF-01)
2. ROLE-TYPE-CLASSIFICATION in three-tier order (CF-02)
3. ANNOTATION-REGISTER with Used-In column (CF-02)
4. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5. Inertia Assessment: Case for Staying Flat [FLAT-CASE-CLOSED] / How We Coordinate Today /
   Rebuttal / VERDICT [FLAT-CASE-PRESSURE] (CF-03/04/05/06)
6. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7. ASCII Org Diagram (CF-07)
8. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9. Headcount by Area (CF-08)
10. Operating Rhythm Table (CF-09)
11. Committee Charters (CF-10)
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. ANNOTATION-REGISTER RECONCILIATION
14. ORG-ELEMENT REGISTER (CF-11)
15. Org Evolution Roadmap (CF-12)
16. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

*Generated by: /quest:variate org-chart R3 -- 2026-03-16*
