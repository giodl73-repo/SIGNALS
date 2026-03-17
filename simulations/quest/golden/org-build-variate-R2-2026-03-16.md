---
skill: quest-variate
skill_target: org-build
date: 2026-03-16
round: R2
rubric_version: v2
status: variate
---

# org-build Variate -- Round 2 (Rubric v2)

**Date:** 2026-03-16
**Skill:** org-build
**Rubric:** v2 (C-01 through C-13; C-10 tightened, C-11/C-12/C-13 new from v2)
**Round:** R2

**R1 ceiling under v1 rubric:**
V-05/R1 scores well on essential + recommended criteria (C-01 through C-08). Three
gaps persist across all R1 variations under the v2 rubric:

1. **C-10 MUST-language gap:** R1 anti-pattern instructions use descriptive format
   guidance ("each cell opens with...") without an imperative MUST. Variations that
   describe the cat-N citation syntax without forbidding deviation produce cells that
   follow the format loosely but are not constrained to it.

2. **C-11 IA scope template gap:** No R1 variation wires the inertia-advocate `scope`
   field to the FLAT-CASE-PRESSURE rating. The IA scope is written generically;
   the C-11 criterion requires pre-written level-specific templates (one per rating)
   and explicit derivation from the rated verdict.

3. **C-12 anti-pattern derivation gap:** R1 variations generate anti-patterns
   independently of the structural decision (CAN-OPERATE-FLAT vs STRUCTURE-WARRANTED).
   C-12 requires the anti-pattern category selection to be explicitly derived from that
   choice: flat -> cat-3/cat-2; deep -> cat-1/cat-4.

4. **C-13 single-verdict guard gap:** R1 uses "choose one" or permissive framing.
   C-13 requires explicit error framing: "Only one verdict. Both is an error. Neither
   is an error."

**R2 target:** Close all four v2 gaps. V-01/V-02/V-03 are single-axis; V-04/V-05
are combined.

---

## Variation Map

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Inertia framing | Making the status quo the structural protagonist causes the FLAT-CASE-PRESSURE rating to become a named first-class output, which naturally wires C-11 IA scope templates and C-13 error framing because both depend on the rated verdict as an input |
| V-02 | Phrasing register | Full MUST/FORBIDDEN/REQUIRED language throughout makes C-10 MUST constraint natural, C-13 error framing expected, and C-12 derivation feel like a constraint rather than a suggestion |
| V-03 | Lifecycle emphasis | Explicit consumption-contract phase gates force C-11 derivation by naming FLAT-CASE-PRESSURE as a required gate output consumed by the IA scope template selection step |
| V-04 | Inertia framing + Lifecycle emphasis | FLAT-CASE-PRESSURE drives an explicit template-selection gate before role files are written, directly implementing C-11 and C-12 in the phase contract |
| V-05 | Phrasing register + Role sequence | Starting with structural analysis, deriving anti-pattern categories from the structural decision, then generating roles implements C-12 derivation as the default sequence; imperative register closes C-10 and C-13 |

---

## V-01 -- Inertia Framing

**axis:** inertia-as-protagonist
**hypothesis:** When the status quo is framed as the structural protagonist -- the
thing with the first turn -- the FLAT-CASE-PRESSURE rating becomes a named first-class
output before any role or diagram is produced. This framing naturally wires C-11
(IA scope templates) because the IA role's whole purpose is to defend the rated status
quo, and C-13 (error framing) because the protagonist-vs-challenger binary makes
"only one verdict" feel structurally inevitable.

---

```
You are running `/org-build {topic}`.

STATUS QUO HAS THE FIRST TURN.

Before drawing an org or writing a single role file, argue the case for staying flat.
The inertia-advocate speaks first. Formal structure is the challenger. The challenger
needs to earn its place by naming a specific failure the status quo cannot answer.

---

TURN 1: STATUS QUO SPEAKS -- INERTIA ASSESSMENT

The inertia-advocate makes the steelman case for operating without formal org structure.
Structure this in four sub-sections in exact order.

Sub-section 1 -- Mechanisms the Flat Team Already Has

Produce a mechanism evidence table. Fill with real, observable coordination mechanisms:

  | Mechanism Name | Type | Frequency / Participants |

Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact

Minimum two data rows. After writing the table, count data rows (header excluded).
If count < 2, add missing rows until count reaches 2. Then emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today

Describe coordination patterns in active use. Do not repeat Sub-section 1 entries.
Name channels, cadences, informal roles, and shared artifacts with frequency and
participants.

Sub-section 3 -- The One Thing This Cannot Answer

Name the single coordination failure the Sub-section 1 mechanisms cannot resolve.
Name an observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
competing roadmap. Do not write "the team is growing" without naming the failure mode.

Sub-section 4 -- VERDICT

FLAT-CASE-PRESSURE LINE (opens this sub-section -- appears before the verdict):

  FLAT-CASE-PRESSURE: [rating] -- [one sentence citing mechanism count + named failure]
  Rating closed set: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

SINGLE-VERDICT GUARD: Write exactly one of the two verdicts below.
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED
Only one verdict. Both is an error. Neither is an error.

The verdict reasoning MUST reference the FLAT-CASE-PRESSURE rating by name.

Re-assessment trigger: name a concrete, measurable threshold. Not "revisit as the team
grows."

Emit: === [PHASE GATE: INERTIA COMPLETE -- IA SCOPE DERIVATION BEGINS] ===

---

TURN 2: IA SCOPE DERIVATION -- RATING-DRIVEN TEMPLATES

The inertia-advocate role will be written in TURN 3. But the scope of that role is
determined now, by the FLAT-CASE-PRESSURE rating, using the template below.

IMPORTANT: Do not write the IA role file until you have read and applied the correct
scope template for the FLAT-CASE-PRESSURE rating you recorded above.

IA SCOPE TEMPLATES (select exactly one by rating):

  Strong (5):
    "Monitor adoption of new structure; flag within 60 days if team reverts to
    pre-structural coordination patterns. Escalate any sign of structure-as-theater."

  Moderate (4):
    "Surface coordination overhead at quarterly review; propose structural refinements
    if decision latency exceeds 2 weeks in any area. Escalate unresolved latency to
    program lead."

  Weak (3):
    "Document the flat-team alternative in program context; revisit this assessment if
    headcount crosses the threshold named in the re-assessment trigger."

  Negligible (2):
    "Archive this inertia assessment; revisit if any documented flat-team coordination
    mechanism fails or atrophies below functional threshold."

  Insufficient (1):
    "Collect evidence of flat-team coordination patterns; defer structure decision until
    at least 2 mechanisms are documented and confirmed operational."

Record which template was selected:
  IA-SCOPE-TEMPLATE-APPLIED: [rating level selected]

Emit: === [PHASE GATE: IA SCOPE DERIVED -- ROLE GENERATION BEGINS] ===

---

TURN 3: LOAD OR BUILD ROLES

Check .craft/roles/ for existing role files.

If files exist, produce ROLES-LOADED:
  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:
  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

All role names used anywhere in this document must be declared here.

INERTIA-ADVOCATE ROLE (always required):
The inertia-advocate MUST appear in ROLES-LOADED or ROLES-NOTE. If not present,
add it explicitly. Its scope field comes from the IA-SCOPE-TEMPLATE-APPLIED above.

Classify roles in three-tier order -- ROLE-TYPE-CLASSIFICATION:
  Tier 1 (Engineering) -- complete all Engineering entries before Tier 2
  Tier 2 (Operations)  -- complete all Operations entries before Tier 3
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Emit: === [PHASE GATE: ROLES CLASSIFIED -- ROLE FILES BEGIN] ===

---

TURN 4: WRITE ROLE FILES

Write one .craft/roles/{area}/{role}.md file per role declared in ROLES-LOADED or
ROLES-NOTE.

Standard depth: 20-30 role files. Deep depth (--depth deep): 50+ role files.
Role files MUST be grouped under area subdirectories: .craft/roles/{area}/{role}.md
Minimum 2 area subdirectories.

Every role file MUST contain all five fields:
  orientation: [frame: what this role is for | serves: whose decisions it supports]
  lens:        [verify: questions this role asks | simplify: rules this role applies]
  expertise:   [depth: how deeply this role knows the domain | relevance: why it matters here]
  scope:       [what this role decides, investigates, and escalates]
  collaborates_with: [list of role names this role works with]

INERTIA-ADVOCATE SCOPE FIELD: The scope field for the inertia-advocate role MUST use
the exact text from the IA-SCOPE-TEMPLATE-APPLIED in TURN 2. Do not paraphrase the
template. The scope field is derived, not composed.

Count role files after writing. Verify count is within depth range (20-30 standard,
50+ deep). If below lower bound, add missing roles until count reaches the lower bound.

Record:
  ROLE-FILE-COUNT: [N] files written

Emit: === [PHASE GATE: ROLE FILES COMPLETE -- ORG CHART BEGINS] ===

---

TURN 5: BUILD ORG-CHART.MD

Write org-chart.md with sections in this exact order:

ANTI-PATTERN CATEGORY DERIVATION (before drawing any diagram):

  IF VERDICT = CAN-OPERATE-FLAT:
    Anti-pattern categories for this artifact are derived from the flat-org decision.
    ANTI-PATTERN-CATEGORIES: cat-3 (Headcount), cat-2 (Committees/Cadences)
    Reasoning: flat org primary risks are over-counting and over-meeting.

  IF VERDICT = STRUCTURE-WARRANTED:
    Anti-pattern categories for this artifact are derived from the layered-org decision.
    ANTI-PATTERN-CATEGORIES: cat-1 (Areas), cat-4 (DRI Roles)
    Reasoning: layered org primary risks are area proliferation and DRI concentration.

Record: ANTI-PATTERN-CATEGORIES-SET: [category pair selected]

Section 1 -- ASCII Org Diagram
Draw hierarchy with minimum two levels. Committees as distinct labeled nodes.
Role names from ROLES-LOADED or ROLES-NOTE only. Do not introduce new names.

Section 2 -- Headcount by Area

Columns: Area | Headcount | Key Roles | Decides | Escalates

Decides and Escalates are ALWAYS separate columns. Do not merge into "Decision Scope."
Annotate Key Roles as [role name] ([domain type]).
Minimum two area rows plus **Total** row.

Section 3 -- Operating Rhythm Table

Columns: Cadence | Frequency | DRI / Owner | Purpose
Minimum three distinct rows: ROB + shiproom or gate + governance meeting.
Do not combine two meetings into one row.

Section 4 -- Committee Charters

One charter per governance meeting. Five fields required per charter:

  Purpose:
  Membership:   [role name] ([domain type]) -- minimum 2 roles
  Decides:
  Escalates:    [named destination -- not "everything not in Decides"]
  Quorum:       [N] of [M] member roles required for binding decisions

Quorum uses full fraction format. Short form "N roles required" is not acceptable.

Section 5 -- ORG-ELEMENT REGISTER

  cat-1 (Areas):           [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount):       Total headcount: [N]
  cat-4 (DRI Roles):       [DRI role from rhythm table]

Section 6 -- Org Evolution Roadmap

Two rows from distinct trigger categories:
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone event (not another headcount)

Section 7 -- Anti-Pattern Watch

Columns: Anti-Pattern | Why It Applies Here | Mitigation
Minimum two rows.

ANTI-PATTERN WATCH MUST CONSTRAINT:
Each "Why It Applies Here" cell MUST open with typed citation syntax:
  [element name] (cat-N) -- [one sentence of specific relevance to this org]

Only cat codes from ANTI-PATTERN-CATEGORIES-SET defined above are valid in this table.
MUST: do not write a cell that names an element without the (cat-N) typed syntax.
MUST: do not use a cat-N code outside the ANTI-PATTERN-CATEGORIES-SET for this verdict.

End org-chart.md with: `Generated by: /org-build {topic} -- {date}`
```

---

## V-02 -- Phrasing Register

**axis:** imperative/FORBIDDEN/REQUIRED register throughout
**hypothesis:** When every constraint is expressed as MUST/FORBIDDEN/REQUIRED rather
than descriptive guidance, C-10's MUST requirement and C-13's error framing emerge
as natural properties of the register rather than special-case additions. The model
cannot satisfy the letter of "each cell opens with" while violating the spirit; it
can only satisfy "MUST open with" or it has not complied.

---

```
You are running `/org-build {topic}`.

CONSTRAINT REGISTER: All rules below use MUST (required), FORBIDDEN (prohibited),
and REQUIRED (mandatory field). "Should" and "consider" do not appear. Each constraint
is a binary: satisfied or violated.

---

PHASE 1: INERTIA ASSESSMENT

REQUIRED before any role files or org diagram.

Sub-section 1 -- Case for Staying Flat

MUST produce a mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |

Type MUST be exactly one value from this closed set: Channel / Informal Role /
Recurring Cadence / Shared Artifact. FORBIDDEN: type values outside this set.

MUST include minimum two data rows. After writing, count rows excluding header.
FORBIDDEN: proceeding to Sub-section 2 before count >= 2.
When count >= 2, MUST emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today

MUST inventory coordination patterns in active use not already in Sub-section 1.
FORBIDDEN: repeating entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

MUST name the specific failure mode the Sub-section 1 mechanisms cannot answer.
MUST name an observable from this closed set: blocked decision / missed SLA /
time-zone gap / knowledge silo / competing roadmap.
FORBIDDEN: writing "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT

FLAT-CASE-PRESSURE LINE:
MUST be the first sentence in this sub-section.
FORBIDDEN: writing the verdict declaration before the FLAT-CASE-PRESSURE line appears.

  FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + named failure]
  Rating MUST be exactly one value from: Strong (5) / Moderate (4) / Weak (3) /
  Negligible (2) / Insufficient (1). FORBIDDEN: ratings outside this closed set.

SINGLE-VERDICT GUARD:
MUST write exactly one of:
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED

Only one verdict. Both is an error. Neither is an error.

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

MUST follow with a re-assessment trigger naming a concrete, measurable threshold.
FORBIDDEN: "revisit as the team grows" without a concrete threshold.

Emit: === [PHASE GATE: INERTIA COMPLETE -- ROLE FILES BEGIN] ===

---

PHASE 2: INERTIA-ADVOCATE SCOPE SELECTION

REQUIRED before writing the inertia-advocate role file.
MUST select exactly one scope template based on the FLAT-CASE-PRESSURE rating:

  Strong (5) -- SCOPE:
    "Monitor adoption of new structure; flag within 60 days if team reverts to
    pre-structural coordination patterns. Escalate any sign of structure-as-theater."

  Moderate (4) -- SCOPE:
    "Surface coordination overhead at quarterly review; propose structural refinements
    if decision latency exceeds 2 weeks in any area."

  Weak (3) -- SCOPE:
    "Document the flat-team alternative in program context; revisit if headcount
    crosses the threshold named in the re-assessment trigger."

  Negligible (2) -- SCOPE:
    "Archive this inertia assessment; revisit if any documented flat-team mechanism
    fails or atrophies."

  Insufficient (1) -- SCOPE:
    "Collect evidence of flat-team coordination patterns; defer structure decision
    until at least 2 mechanisms are documented and confirmed operational."

MUST record: IA-SCOPE-SELECTED: [rating] -- [first five words of scope text]

FORBIDDEN: writing the inertia-advocate scope field with any text other than the
template corresponding to the FLAT-CASE-PRESSURE rating.

---

PHASE 3: LOAD OR BUILD ROLES

Glob .craft/roles/. MUST produce ROLES-LOADED:
  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, MUST produce ROLES-NOTE instead:
  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

FORBIDDEN: inventing role names without either loading from files or declaring them
in ROLES-NOTE.

INERTIA-ADVOCATE: REQUIRED in ROLES-LOADED or ROLES-NOTE. If absent, MUST add it.

MUST classify all roles in ROLE-TYPE-CLASSIFICATION, three-tier order:
  Tier 1 (Engineering) -- MUST complete before writing Tier 2
  Tier 2 (Operations)  -- MUST complete before writing Tier 3
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type MUST be exactly one value from: Engineering / PM / Design / Operations /
Research / Other. FORBIDDEN: domain types outside this set.

Emit: === [PHASE GATE: ROLES CLASSIFIED -- ROLE FILES BEGIN] ===

---

PHASE 4: WRITE ROLE FILES

MUST write one .craft/roles/{area}/{role}.md file per role in ROLES-LOADED or ROLES-NOTE.

REQUIRED fields in every role file:
  orientation: [frame: what this role is for | serves: whose decisions it supports]
  lens:        [verify: questions this role asks | simplify: rules this role applies]
  expertise:   [depth: how deeply | relevance: why it matters here]
  scope:       [what this role decides, investigates, escalates]
  collaborates_with: [list of role names]

FORBIDDEN: writing any role file without all five fields present.

INERTIA-ADVOCATE SCOPE CONSTRAINT:
MUST use the exact scope template text from IA-SCOPE-SELECTED.
FORBIDDEN: paraphrasing, summarizing, or substituting generic scope text for the
inertia-advocate role.

MUST group role files under area subdirectories: .craft/roles/{area}/{role}.md
REQUIRED: minimum 2 area subdirectories.

ROLE-COUNT CONSTRAINT:
Standard depth: MUST produce 20-30 role files.
Deep (--depth deep): MUST produce 50+ role files.
FORBIDDEN: producing fewer files than the lower bound for the selected depth.

MUST record: ROLE-FILE-COUNT: [N]
FORBIDDEN: emitting ROLE FILES COMPLETE gate before ROLE-FILE-COUNT >= lower bound.

Emit: === [PHASE GATE: ROLE FILES COMPLETE -- ORG CHART BEGINS] ===

---

PHASE 5: ANTI-PATTERN CATEGORY DERIVATION

REQUIRED before writing org-chart.md. The verdict from Phase 1 determines which
org-element categories are valid in the Anti-Pattern Watch table.

IF VERDICT = CAN-OPERATE-FLAT:
  MUST set: ANTI-PATTERN-CATEGORIES: cat-3 (Headcount), cat-2 (Committees/Cadences)
  FORBIDDEN: using cat-1 or cat-4 in the Anti-Pattern Watch table.

IF VERDICT = STRUCTURE-WARRANTED:
  MUST set: ANTI-PATTERN-CATEGORIES: cat-1 (Areas), cat-4 (DRI Roles)
  FORBIDDEN: using cat-2 or cat-3 as primary anti-pattern categories.

MUST record: ANTI-PATTERN-CATEGORIES-SET: [categories]

---

PHASE 6: WRITE ORG-CHART.MD

Write org-chart.md in this exact section order.

SECTION 1 -- ASCII ORG DIAGRAM
MUST draw after Phase 1 inertia phase gate. MUST show minimum two hierarchy levels.
FORBIDDEN: flat list of names without visual hierarchy.
MUST show committees as distinct labeled nodes -- FORBIDDEN: embedding committees
inside area boxes.
MUST use only role names from ROLES-LOADED or ROLES-NOTE.

SECTION 2 -- HEADCOUNT BY AREA

MUST use columns: Area | Headcount | Key Roles | Decides | Escalates
FORBIDDEN: merging Decides and Escalates into a single "Decision Scope" column.
MUST annotate Key Roles as [role name] ([domain type]).
MUST include minimum two area rows plus **Total** row.
FORBIDDEN: single-row tables without area breakdown.

SECTION 3 -- OPERATING RHYTHM TABLE

MUST use columns: Cadence | Frequency | DRI / Owner | Purpose
MUST include minimum three distinct rows: ROB + shiproom or gate + governance.
FORBIDDEN: combining two cadences into one row.

SECTION 4 -- COMMITTEE CHARTERS

MUST write one charter per governance meeting in the rhythm table.
REQUIRED fields per charter:
  Purpose:
  Membership:   [role name] ([domain type]) -- REQUIRED: minimum 2 roles
  Decides:
  Escalates:    REQUIRED: named destination (FORBIDDEN: "everything not in Decides")
  Quorum:       [N] of [M] member roles required for binding decisions

QUORUM CONSTRAINT:
MUST use full fraction format. FORBIDDEN: short form "Quorum: [N] roles required."
FORBIDDEN: emitting a charter without a Quorum field.

SECTION 5 -- ORG-ELEMENT REGISTER

MUST populate all four categories:
  cat-1 (Areas):           [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount):       Total headcount: [N]
  cat-4 (DRI Roles):       [DRI role]

SECTION 6 -- ORG EVOLUTION ROADMAP

MUST include minimum two rows from DISTINCT trigger categories:
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone event
FORBIDDEN: two rows both typed as headcount threshold.

SECTION 7 -- ANTI-PATTERN WATCH

MUST include minimum two rows:
  | Anti-Pattern | Why It Applies Here | Mitigation |

CITATION CONSTRAINT:
MUST open each "Why It Applies Here" cell with:
  [element name] (cat-N) -- [one sentence of specific relevance]
FORBIDDEN: writing any "Why It Applies Here" cell without the (cat-N) typed syntax.
FORBIDDEN: using a cat-N code not present in ANTI-PATTERN-CATEGORIES-SET.
FORBIDDEN: descriptive format guidance in Mitigation cells -- each Mitigation cell
MUST contain an imperative action, not descriptive advice.

End org-chart.md with: `Generated by: /org-build {topic} -- {date}`
```

---

## V-03 -- Lifecycle Emphasis

**axis:** consumption-contract phase gates
**hypothesis:** When each phase gate explicitly names what output it requires
and what the next phase consumes, the FLAT-CASE-PRESSURE rating becomes a typed
artifact that the IA scope selection phase must consume. This implements C-11 as
a structural contract rather than an instruction, making derivation a phase pre-condition
rather than an aspirational note.

---

```
You are running `/org-build {topic}`.

This skill runs in six phases. Each phase gate names its required inputs and outputs.
No phase begins before its predecessor produces the named output.

---

PHASE 1: INERTIA ASSESSMENT
Output contract: [FLAT-CASE-PRESSURE rating] [VERDICT] [re-assessment trigger]

Sub-section 1 -- Case for Staying Flat

Produce mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count. When count >= 2, emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns in active use not already in Sub-section 1. Name frequency
and participants.

Sub-section 3 -- Rebuttal
The single observable failure the Sub-section 1 mechanisms cannot answer.

Sub-section 4 -- VERDICT

Open with (required before verdict declaration):
  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then write exactly one verdict:
  CAN-OPERATE-FLAT  or  STRUCTURE-WARRANTED
Only one verdict. Both is an error. Neither is an error.

Re-assessment trigger: concrete measurable threshold. "Revisit as the team grows"
is not concrete.

=== [PHASE 1 GATE: INERTIA COMPLETE]
  Input consumed: [topic]
  Output produced: FLAT-CASE-PRESSURE=[rating] | VERDICT=[verdict] | TRIGGER=[trigger]
  Consumed by: Phase 2 (IA scope selection) and Phase 4 (anti-pattern derivation)
===

---

PHASE 2: IA SCOPE TEMPLATE SELECTION
Input contract: consumes FLAT-CASE-PRESSURE rating from Phase 1 gate
Output contract: [IA-SCOPE-TEXT] bound to the rating level

Map FLAT-CASE-PRESSURE rating to scope template:

  Strong (5):
    SCOPE = "Monitor adoption of new structure; flag within 60 days if team reverts
    to pre-structural coordination patterns. Escalate any sign of structure-as-theater."

  Moderate (4):
    SCOPE = "Surface coordination overhead at quarterly review; propose structural
    refinements if decision latency exceeds 2 weeks in any area."

  Weak (3):
    SCOPE = "Document the flat-team alternative in program context; revisit if
    headcount crosses the threshold named in the re-assessment trigger."

  Negligible (2):
    SCOPE = "Archive this inertia assessment; revisit if any documented flat-team
    coordination mechanism fails or atrophies."

  Insufficient (1):
    SCOPE = "Collect evidence of flat-team coordination patterns; defer structure
    decision until at least 2 mechanisms are documented and confirmed operational."

Record the selection:
  IA-SCOPE-BOUND: [rating] -> [first 8 words of selected scope text]

=== [PHASE 2 GATE: IA SCOPE BOUND]
  Input consumed: FLAT-CASE-PRESSURE=[rating] from Phase 1 gate
  Output produced: IA-SCOPE-BOUND=[rating] | IA-SCOPE-TEXT=[selected template]
  Consumed by: Phase 3 (inertia-advocate role file)
===

---

PHASE 3: LOAD OR BUILD ROLES
Input contract: consumes IA-SCOPE-BOUND from Phase 2 gate
Output contract: [ROLES-LOADED or ROLES-NOTE] [ROLE-TYPE-CLASSIFICATION] [ROLE-FILES]

Glob .craft/roles/. If files found, produce ROLES-LOADED:
  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:
  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

INERTIA-ADVOCATE: Must appear in ROLES-LOADED or ROLES-NOTE. Add if absent.

Classify in ROLE-TYPE-CLASSIFICATION, three-tier order:
  Engineering types first (complete tier before next)
  Operations types second (complete tier before next)
  PM / Design / Research / Other types third

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Write one .craft/roles/{area}/{role}.md per role. Five fields required in every file:
  orientation: [frame | serves]
  lens:        [verify questions | simplify rules]
  expertise:   [depth | relevance]
  scope:       [decisions, investigations, escalations]
  collaborates_with: [role name list]

INERTIA-ADVOCATE SCOPE FIELD:
The scope field for inertia-advocate MUST use the exact IA-SCOPE-TEXT from Phase 2.
The scope is not composed at this phase -- it is read from Phase 2 output.

Role count: Standard 20-30 files. Deep (--depth deep): 50+ files.
Group under area subdirectories: .craft/roles/{area}/{role}.md (minimum 2 subdirs).

Record: ROLE-FILE-COUNT: [N]

=== [PHASE 3 GATE: ROLE FILES COMPLETE]
  Input consumed: IA-SCOPE-BOUND from Phase 2 | ROLES-LOADED/NOTE declared above
  Output produced: [N] role files in .craft/roles/
  Consumed by: Phase 4 (org-chart.md sections -- role names and domain types)
===

---

PHASE 4: ANTI-PATTERN CATEGORY DERIVATION
Input contract: consumes VERDICT from Phase 1 gate
Output contract: [ANTI-PATTERN-CATEGORIES] binding valid cat codes for Phase 5

Derive anti-pattern categories from the structural decision:

  IF VERDICT = CAN-OPERATE-FLAT:
    Primary risks of flat org: uncontrolled headcount growth, meeting proliferation.
    ANTI-PATTERN-CATEGORIES: cat-3 (Headcount), cat-2 (Committees/Cadences)

  IF VERDICT = STRUCTURE-WARRANTED:
    Primary risks of layered org: area proliferation, DRI bottleneck.
    ANTI-PATTERN-CATEGORIES: cat-1 (Areas), cat-4 (DRI Roles)

Record: ANTI-PATTERN-CATEGORIES-SET: [category pair]

=== [PHASE 4 GATE: CATEGORIES BOUND]
  Input consumed: VERDICT=[verdict] from Phase 1 gate
  Output produced: ANTI-PATTERN-CATEGORIES-SET=[categories]
  Consumed by: Phase 5 (Anti-Pattern Watch cat-N citations)
===

---

PHASE 5: ORG-ELEMENT REGISTER
Input contract: consumes role names, areas, rhythm entries from org-chart.md sections

Write org-chart.md. Sections in exact order after Phase 3 gate:

1. ASCII Org Diagram: minimum two levels, committees as distinct nodes, role names
   from ROLES-LOADED or ROLES-NOTE only.

2. Headcount by Area: columns Area | Headcount | Key Roles | Decides | Escalates.
   Separate Decides and Escalates columns required. Key Roles annotated [role] ([type]).
   Two area rows minimum plus Total row.

3. Operating Rhythm Table: columns Cadence | Frequency | DRI / Owner | Purpose.
   Minimum three distinct rows: ROB + shiproom or gate + governance meeting.

4. Committee Charters: one per governance meeting. Five fields per charter:
   Purpose / Membership [min 2 roles with domain type] / Decides /
   Escalates [named destination] / Quorum [N of M member roles required]

5. ORG-ELEMENT REGISTER (all four categories):
   cat-1 (Areas):           [area name] -- headcount: [N]
   cat-2 (Committees/Cadences): [name]
   cat-3 (Headcount):       Total headcount: [N]
   cat-4 (DRI Roles):       [DRI role]

6. Org Evolution Roadmap: two rows from distinct trigger categories.
   Row 1: headcount threshold. Row 2: workload signal, symptom, or milestone.

7. Anti-Pattern Watch: minimum two rows.
   Columns: Anti-Pattern | Why It Applies Here | Mitigation

   CITATION BINDING (Phase 4 output consumed here):
   Each "Why It Applies Here" cell MUST open with:
     [element name] (cat-N) -- [one sentence]
   Only cat codes from ANTI-PATTERN-CATEGORIES-SET are valid here.
   Any cell that names an element without (cat-N) typed syntax fails this binding.
   Any cell that uses a cat code outside ANTI-PATTERN-CATEGORIES-SET fails this binding.

=== [PHASE 5 GATE: ORG-CHART.MD COMPLETE]
  Input consumed: ROLE-FILE-COUNT from Phase 3 | ANTI-PATTERN-CATEGORIES-SET from Phase 4
  Output produced: org-chart.md
===

End org-chart.md with: `Generated by: /org-build {topic} -- {date}`
```

---

## V-04 -- Inertia Framing + Lifecycle Emphasis

**axis:** inertia-as-protagonist + consumption-contract phase gates
**hypothesis:** Combining the status-quo-first framing with explicit phase gates that
name FLAT-CASE-PRESSURE as a typed output consumed by downstream phases creates a
double-lock on C-11 and C-12: the inertia framing makes the rating feel like the
protagonist's score, and the consumption contract makes derivation a structural
pre-condition that cannot be skipped.

---

```
You are running `/org-build {topic}`.

THE STATUS QUO SPEAKS FIRST. RATED VERDICT FEEDS EVERYTHING DOWNSTREAM.

This skill runs four turns. Turn 1 produces a FLAT-CASE-PRESSURE rating and VERDICT
that are consumed as typed inputs by all remaining turns. No role file is written
and no org diagram is drawn until the rated verdict is recorded.

---

TURN 1: INERTIA ADVOCATE MAKES THE CASE
[Output contract: FLAT-CASE-PRESSURE=[rating] | VERDICT=[one of two] | TRIGGER=[threshold]]

The inertia-advocate goes first. Argue the steelman case for staying flat.
Structure in four sub-sections.

Sub-section 1 -- Mechanisms the Team Already Uses

  | Mechanism Name | Type | Frequency / Participants |
  Type: Channel / Informal Role / Recurring Cadence / Shared Artifact

  Minimum two rows. Count. Emit when count >= 2:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns in active use. Do not repeat Sub-section 1 entries.

Sub-section 3 -- The Failure Mode This Cannot Answer
Name an observable: blocked decision / missed SLA / time-zone gap / knowledge silo /
competing roadmap.

Sub-section 4 -- VERDICT (opens with FLAT-CASE-PRESSURE)

The FLAT-CASE-PRESSURE line is the opening sentence of this sub-section. It is
produced before the verdict declaration.

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then declare the verdict:
  CAN-OPERATE-FLAT  or  STRUCTURE-WARRANTED
Only one verdict. Both is an error. Neither is an error.

Re-assessment trigger: concrete measurable threshold.

TURN 1 OUTPUT RECORD:
  T1-PRESSURE: [rating]
  T1-VERDICT:  [verdict]
  T1-TRIGGER:  [threshold text]

---

TURN 2: IA ROLE SCOPED FROM VERDICT
[Input: T1-PRESSURE | Output: IA-SCOPE-TEXT]

The inertia-advocate role scope is not written from scratch. It is selected from the
template table below using T1-PRESSURE as the key.

  T1-PRESSURE = Strong (5) ->
    IA-SCOPE-TEXT: "Monitor adoption of new structure; flag within 60 days if team
    reverts to pre-structural coordination patterns. Escalate structure-as-theater."

  T1-PRESSURE = Moderate (4) ->
    IA-SCOPE-TEXT: "Surface coordination overhead at quarterly review; propose
    refinements if decision latency exceeds 2 weeks in any area."

  T1-PRESSURE = Weak (3) ->
    IA-SCOPE-TEXT: "Document the flat-team alternative in program context; revisit
    if headcount crosses the T1-TRIGGER threshold."

  T1-PRESSURE = Negligible (2) ->
    IA-SCOPE-TEXT: "Archive this inertia assessment; revisit if any flat-team
    mechanism fails or atrophies below functional threshold."

  T1-PRESSURE = Insufficient (1) ->
    IA-SCOPE-TEXT: "Collect flat-team coordination evidence; defer structure decision
    until at least 2 mechanisms are documented and confirmed operational."

Record: T2-IA-SCOPE: [T1-PRESSURE key] -> [selected IA-SCOPE-TEXT]

The inertia-advocate scope field in the role file is T2-IA-SCOPE. Not paraphrased.
Not adapted. The template text, verbatim.

---

TURN 3: ANTI-PATTERN CATEGORIES DERIVED FROM VERDICT
[Input: T1-VERDICT | Output: T3-CATEGORIES]

T1-VERDICT drives anti-pattern category selection. This derivation must happen
before the Anti-Pattern Watch table is written in Turn 4.

  T1-VERDICT = CAN-OPERATE-FLAT:
    Primary org risks come from over-counting and over-meeting.
    T3-CATEGORIES: cat-3 (Headcount), cat-2 (Committees/Cadences)

  T1-VERDICT = STRUCTURE-WARRANTED:
    Primary org risks come from area proliferation and DRI bottleneck.
    T3-CATEGORIES: cat-1 (Areas), cat-4 (DRI Roles)

Record: T3-CATEGORIES-SET: [categories]

Anti-Pattern Watch cells in Turn 4 MUST cite only elements from T3-CATEGORIES-SET.
Anti-pattern rows citing elements from categories outside T3-CATEGORIES-SET are
a derivation failure.

---

TURN 4: BUILD THE ORG ARTIFACT
[Input: T2-IA-SCOPE, T3-CATEGORIES-SET, T1-VERDICT]

Step 4a -- Load or build roles.

Glob .craft/roles/. Produce ROLES-LOADED or ROLES-NOTE.
Inertia-advocate MUST be present. If absent, add.
Classify all roles: ROLE-TYPE-CLASSIFICATION in three-tier order:
  Engineering first | Operations second | PM / Design / Research / Other third

Write .craft/roles/{area}/{role}.md for every role:
  Required fields: orientation, lens, expertise, scope, collaborates_with
  Inertia-advocate scope field = T2-IA-SCOPE (exact, not paraphrased)
  Standard: 20-30 files. Deep: 50+ files. Min 2 area subdirs.

Step 4b -- Write org-chart.md.

Sections in exact order:

  1. ASCII Org Diagram (two levels minimum, committees as distinct nodes)

  2. Headcount by Area (columns: Area | Headcount | Key Roles | Decides | Escalates)
     Decides and Escalates always separate. Key Roles annotated [role] ([type]).
     Two area rows plus Total.

  3. Operating Rhythm Table (ROB + shiproom/gate + governance, minimum 3 rows)

  4. Committee Charters (one per governance meeting, 5 fields):
     Purpose / Membership [>=2 roles with type] / Decides /
     Escalates [named destination] / Quorum [N of M member roles required]

  5. ORG-ELEMENT REGISTER:
     cat-1 (Areas): [area] -- headcount: [N]
     cat-2 (Committees/Cadences): [name]
     cat-3 (Headcount): Total headcount: [N]
     cat-4 (DRI Roles): [DRI role]

  6. Org Evolution Roadmap (two rows, distinct trigger categories):
     Row 1: headcount threshold. Row 2: workload signal, symptom, or milestone.

  7. Anti-Pattern Watch (2+ rows):

     Columns: Anti-Pattern | Why It Applies Here | Mitigation

     DERIVATION BINDING [T3-CATEGORIES-SET consumed here]:
     Each "Why It Applies Here" MUST open with:
       [element name] (cat-N) -- [one sentence specific to this org]
     Only cat codes in T3-CATEGORIES-SET are valid in this table.

     IMPERATIVE MITIGATION: Each Mitigation cell MUST prescribe an action.
     "Consider..." and "Think about..." are not mitigations.

End org-chart.md with: `Generated by: /org-build {topic} -- {date}`
```

---

## V-05 -- Phrasing Register + Role Sequence

**axis:** MUST/FORBIDDEN register + structural-decision-first role sequence
**hypothesis:** Beginning with the structural decision (flat vs layered), then deriving
anti-pattern categories, then generating roles means C-12 is the first derivation step
before any creative work begins. Imperative register throughout means C-10 MUST syntax
and C-13 error framing are properties of the vocabulary, not special-case additions.
The combination makes derivation a prerequisite and compliance a property of the register.

---

```
You are running `/org-build {topic}`.

CONSTRAINT ARCHITECTURE: Every rule is MUST (required) or FORBIDDEN (prohibited).
STRUCTURAL DECISION COMES FIRST: the flat-vs-layered verdict drives role scope and
anti-pattern selection before roles or diagrams are produced.

---

STEP 1: STRUCTURAL DECISION -- INERTIA ASSESSMENT

MUST produce this section before any role file or diagram.
MUST produce all four sub-sections in exact order.

Sub-section 1 -- Case for Staying Flat

MUST produce mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type MUST be one of: Channel / Informal Role / Recurring Cadence / Shared Artifact.
FORBIDDEN: Type values outside this set.
MUST include minimum two data rows.
After writing, count data rows (header excluded).
FORBIDDEN: proceeding before count >= 2.
When count >= 2, MUST emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
MUST inventory active coordination patterns not already in Sub-section 1.
FORBIDDEN: repeating Sub-section 1 table entries.

Sub-section 3 -- Rebuttal
MUST name the specific observable failure Sub-section 1 mechanisms cannot answer.
Observable MUST come from: blocked decision / missed SLA / time-zone gap / knowledge
silo / competing roadmap.
FORBIDDEN: "the team is growing" without naming the specific failure mode.

Sub-section 4 -- VERDICT

MUST open with FLAT-CASE-PRESSURE before any verdict word appears:
  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure]
  Rating MUST be one of: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) /
  Insufficient (1).

SINGLE-VERDICT GUARD:
MUST write exactly one verdict:
  CAN-OPERATE-FLAT  or  STRUCTURE-WARRANTED
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts.
FORBIDDEN: omitting both verdicts.

MUST write re-assessment trigger with concrete measurable threshold.
FORBIDDEN: "revisit as the team grows" without a concrete threshold.

MUST record:
  STRUCTURAL-DECISION: VERDICT=[verdict] | PRESSURE=[rating]

---

STEP 2: ANTI-PATTERN CATEGORY DERIVATION (immediately after verdict)

MUST derive before any role is written or diagram drawn.
MUST apply exactly the derivation rule for the recorded STRUCTURAL-DECISION.

  IF STRUCTURAL-DECISION VERDICT = CAN-OPERATE-FLAT:
    ANTI-PATTERN-CATEGORIES: cat-3 (Headcount), cat-2 (Committees/Cadences)
    DERIVATION-RATIONALE: flat org primary failure modes are headcount drift and
    meeting proliferation -- cat-3 and cat-2 elements carry the risk.
    FORBIDDEN: using cat-1 or cat-4 as primary anti-pattern categories.

  IF STRUCTURAL-DECISION VERDICT = STRUCTURE-WARRANTED:
    ANTI-PATTERN-CATEGORIES: cat-1 (Areas), cat-4 (DRI Roles)
    DERIVATION-RATIONALE: layered org primary failure modes are area proliferation
    and DRI concentration -- cat-1 and cat-4 elements carry the risk.
    FORBIDDEN: using cat-2 or cat-3 as primary anti-pattern categories.

MUST record: ANTI-PATTERN-CATEGORIES-SET: [categories]

---

STEP 3: IA SCOPE SELECTION (immediately after verdict)

MUST select IA scope template using STRUCTURAL-DECISION PRESSURE as key.
FORBIDDEN: writing inertia-advocate scope from scratch.
MUST use the template text exactly, without paraphrase.

  PRESSURE = Strong (5):
    IA-SCOPE = "Monitor adoption of new structure; flag within 60 days if team
    reverts to pre-structural coordination patterns. Escalate structure-as-theater."

  PRESSURE = Moderate (4):
    IA-SCOPE = "Surface coordination overhead at quarterly review; propose
    refinements if decision latency exceeds 2 weeks in any area."

  PRESSURE = Weak (3):
    IA-SCOPE = "Document the flat-team alternative in program context; revisit
    if headcount crosses the threshold named in the re-assessment trigger."

  PRESSURE = Negligible (2):
    IA-SCOPE = "Archive this inertia assessment; revisit if any flat-team
    coordination mechanism fails or atrophies."

  PRESSURE = Insufficient (1):
    IA-SCOPE = "Collect flat-team coordination evidence; defer structure decision
    until at least 2 mechanisms are documented and confirmed operational."

MUST record: IA-SCOPE-SELECTED: [pressure key] | [first 8 words of scope text]

FORBIDDEN: proceeding to Step 4 without both ANTI-PATTERN-CATEGORIES-SET and
IA-SCOPE-SELECTED recorded above.

Emit: === [PHASE GATE: STRUCTURAL DECISIONS COMPLETE -- ROLE SEQUENCE BEGINS] ===

---

STEP 4: LOAD OR BUILD ROLES

Glob .craft/roles/. MUST produce ROLES-LOADED if files found:
  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files, MUST produce ROLES-NOTE:
  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

FORBIDDEN: using any role name not declared in ROLES-LOADED or ROLES-NOTE.

INERTIA-ADVOCATE: MUST appear in ROLES-LOADED or ROLES-NOTE. MUST add if absent.

ROLE SEQUENCE (three-tier strict order):
MUST classify in ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles (MUST complete before Tier 2)
  Tier 2: Operations roles (MUST complete before Tier 3)
  Tier 3: PM / Design / Research / Other

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type MUST be one of: Engineering / PM / Design / Operations / Research / Other.
FORBIDDEN: domain types outside this closed set.

Emit: === [PHASE GATE: ROLES CLASSIFIED -- ROLE FILES BEGIN] ===

---

STEP 5: WRITE ROLE FILES

MUST write one .craft/roles/{area}/{role}.md per role in ROLES-LOADED or ROLES-NOTE.

REQUIRED fields in every role file (FORBIDDEN: any role file missing any field):
  orientation: [frame: what this role is for | serves: whose decisions it supports]
  lens:        [verify: questions it asks | simplify: rules it applies]
  expertise:   [depth: how deeply it knows the domain | relevance: why here]
  scope:       [what it decides, investigates, escalates]
  collaborates_with: [role name list]

INERTIA-ADVOCATE SCOPE CONSTRAINT:
MUST set scope = IA-SCOPE-SELECTED text (exact).
FORBIDDEN: using any other text for the inertia-advocate scope field.

MUST group under area subdirs: .craft/roles/{area}/{role}.md
REQUIRED: minimum 2 area subdirectories.
FORBIDDEN: all roles in a flat .craft/roles/ directory with no area grouping.

ROLE-COUNT CONSTRAINT:
Standard: MUST produce 20-30 files. Deep (--depth deep): MUST produce 50+.
FORBIDDEN: producing fewer than the lower bound.
MUST record: ROLE-FILE-COUNT: [N]

Emit: === [PHASE GATE: ROLE FILES COMPLETE -- ORG CHART BEGINS] ===

---

STEP 6: WRITE ORG-CHART.MD

Sections in exact order:

SECTION 1 -- ASCII ORG DIAGRAM
MUST show minimum two hierarchy levels.
FORBIDDEN: flat name list without visual hierarchy.
MUST show committees as distinct nodes.
MUST use only role names from ROLES-LOADED or ROLES-NOTE.

SECTION 2 -- HEADCOUNT BY AREA
MUST use: Area | Headcount | Key Roles | Decides | Escalates
FORBIDDEN: single Decision Scope column merging Decides and Escalates.
MUST annotate Key Roles as [role name] ([domain type]).
MUST include minimum two area rows plus **Total** row.

SECTION 3 -- OPERATING RHYTHM TABLE
MUST use: Cadence | Frequency | DRI / Owner | Purpose
MUST include minimum three distinct rows (ROB + shiproom/gate + governance).
FORBIDDEN: combining two cadences in one row.

SECTION 4 -- COMMITTEE CHARTERS
MUST write one charter per governance meeting in the rhythm table.
REQUIRED fields per charter:
  Purpose:
  Membership:   [role name] ([domain type]) -- REQUIRED: minimum 2 roles
  Decides:
  Escalates:    REQUIRED: named destination
  Quorum:       [N] of [M] member roles required for binding decisions
FORBIDDEN: short Quorum form "N roles required."
FORBIDDEN: any charter missing a Quorum field.

SECTION 5 -- ORG-ELEMENT REGISTER
MUST populate all four categories:
  cat-1 (Areas):               [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount):           Total headcount: [N]
  cat-4 (DRI Roles):           [DRI role]

SECTION 6 -- ORG EVOLUTION ROADMAP
MUST include two rows from DISTINCT trigger categories:
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone event
FORBIDDEN: two rows both typed as headcount threshold.

SECTION 7 -- ANTI-PATTERN WATCH

MUST include minimum two rows:
  | Anti-Pattern | Why It Applies Here | Mitigation |

CITATION CONSTRAINT (ANTI-PATTERN-CATEGORIES-SET consumed here):
MUST open each "Why It Applies Here" cell with:
  [element name] (cat-N) -- [one sentence of specific relevance to this org]
FORBIDDEN: any "Why It Applies Here" cell without (cat-N) typed syntax.
FORBIDDEN: cat-N codes outside ANTI-PATTERN-CATEGORIES-SET for this verdict.

MITIGATION CONSTRAINT:
Each Mitigation cell MUST state an imperative action.
FORBIDDEN: "Consider..." or "Think about..." framing in any Mitigation cell.

End org-chart.md with: `Generated by: /org-build {topic} -- {date}`
```
