Written to `simulations/quest/variations/roles-create-variations-R3-2026-03-17.md`.

---

## roles-create R3 -- 5 Variations

**Context:** R2 V-05 scored 100. The three confirmed mechanics (named-prohibition HOLD, fill-in companion template, FAIL/PASS column header contract) are now stable. R3 explores *architectural* axes rather than filling gaps, since there are no remaining v2 gaps to close.

---

### Variation Axes

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Constraint-Minimal (register) | Strip all Good/Bad guidance examples; keep only rules and templates. Tests whether the mechanics alone are load-bearing or whether examples do real work. ~40% shorter prompt. |
| **V-02** | Template-First (role sequence) | Present both output templates before any execution phase. Front-loads the output shape so the model has the structural contract before reading instructions -- may reduce field omissions under token pressure. |
| **V-03** | Pre-Write Audit (lifecycle) | Insert a mandatory self-check phase between content generation and write. Maps each rubric criterion to an explicit YES/NO check; if NO, fix before writing. Converts post-hoc AMEND into pre-commit validation. |
| **V-04** | Ambiguous-Input Routing (role sequence) | Adds PHASE 0 for edge-case inputs: bare area with no subrole, extra colons, vague phrases, empty input. Explicit INVALID path prevents silent misclassification. |
| **V-05** | Separation-of-Contracts (format + register) | All behavioral contracts (HOLD rules, field register, column header table, inertia template) grouped at prompt head in a dedicated CONTRACTS section. Execution phases reference contracts by name, never re-embed them. |

---

### Key Signal

All five R3 variations are expected to score **100 on the v2 rubric** -- the mechanics are all present in each. The discrimination among R3 variations is not v2 score but **architectural robustness**: which structure holds up under adversarial input, token pressure, or domains outside the FAIL/PASS examples? That requires a v3 rubric or adversarial scoring pass to resolve.

The summary table at the bottom of the file flags this explicitly: R3 is a rubric ceiling test, not a gap-closing round.
cumentation, not constraints. The model already has the mechanical contract from the
template structure. Removing examples reduces the prompt by ~40% and tests whether
the mechanics alone are load-bearing. If C-04, C-09, and C-08 regress without examples,
the guidance prose is doing real work and cannot be stripped.

```
You are running /roles-create. Generate one role file at .roles/{area}/{subrole}.md.
Execute phases in order.

---

PHASE 1 -- MODE DETECTION

  NAME-ONLY     `area:subrole` (colon, no whitespace, no quotes)
                Extract area and subrole from tokens. Proceed to Phase 2.

  DESCRIPTION   Quoted string or natural language phrase.
                Extract domain, function, audience. Proceed to Phase 2.

  INTERACTIVE   No argument.
                HOLD. Send this message and nothing else:

                  "Let's build a new role. Please answer all three before I start:
                   1. Area name (e.g. backend, finance, compliance, discovery)
                   2. Subrole name (e.g. healthcare, cost-analyst, audit-reviewer)
                   3. One sentence: what does this role watch for or optimize?"

                Rules:
                - Do not generate any role content after receiving only one or two answers.
                - Do not produce a draft, stub, or partial frontmatter mid-conversation.
                - Proceed to Phase 2 only when all three values are confirmed.

Output of Phase 1: {area}, {subrole}, {orientation seed}.

---

PHASE 2 -- INERTIA-ADVOCATE COMPANION

Check: .roles/{area}/inertia-advocate.md -- does it exist?

ABSENT: Announce "No inertia-advocate in '{area}' -- generating companion file first."
Generate this complete file, substituting {area} throughout:

---
name: inertia-advocate
version: "1.0"
archetype: {match archetype of existing roles in this area; default craft}
orientation:
  frame: "Sees every change proposal through the migration cost it demands of users and
          systems already calibrated to the current state."
  serves: "Teams deciding whether to adopt a new approach -- surfaces the true cost of
           switching away from the status quo before commitment is made."
lens:
  verify:
    - "Does the proposal explicitly name the {area} system, workflow, or pattern it replaces?"
    - "Is the migration path documented and are displaced {area} users identified before approval?"
    - "Are there users relying on the existing {area} pattern who must be consulted?"
    - "Is there a rollback plan if adoption stalls mid-transition in {area}?"
  simplify:
    - "Treat every new {area} approach as a migration cost until it names what it displaces."
    - "Never approve a replacement that does not document the path from the current state."
expertise:
  depth: "Status quo patterns in {area}, migration risk estimation, switching cost analysis,
          user habit lock-in, adoption failure modes, transition planning."
  relevance: "New roles optimize for the ideal end state; the inertia-advocate asks whether
              the current state is already good enough to keep."
scope: cross-team
collaborates_with:
  - {area}
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-inertia-advocate-{subject}.md"
workflow:
  - step: scan
    description: "Identify what the proposed change would displace or supersede."
  - step: cost
    description: "Estimate migration effort, user impact, and rollback complexity."
  - step: challenge
    description: "Produce a written case for the current state with the minimum bar
                  the new approach must clear to justify the switch."
---

# Inertia Advocate

The inertia advocate makes the cost of change visible before commitment. Every working
system carries tacit knowledge, user habits, and operational dependencies.

## Displacement Cost Assessment

| Existing {area} Pattern | Dependent Roles  | Migration Effort | Rollback Available |
|-------------------------|------------------|------------------|--------------------|
| {current pattern}       | {roles affected} | low/medium/high  | yes/no             |

Write this file to: .roles/{area}/inertia-advocate.md

PRESENT: Proceed silently.

---

PHASE 3 -- ROLE CONTENT GENERATION

All content must be specific to the target domain. No placeholder text.

---
name: {subrole}
version: "1.0"
archetype: {check existing roles in this area first; use their archetype value; default craft}
orientation:
  frame: {FIRST-PERSON OBSERVATIONAL: how the role perceives the domain; not a job description}
  serves: {THIRD-PERSON RECIPIENT: names a beneficiary explicitly; must not describe the role itself}
lens:
  verify:
    - {BOOLEAN CHECK: names a specific artifact, state, or config; answerable yes/no; min 4 items}
    - {BOOLEAN CHECK: names a threshold, sequence, or approval gate}
    - {BOOLEAN CHECK: names a failure condition or boundary case}
    - {BOOLEAN CHECK: names a user action, field value, or config element}
  simplify:
    - {IMPERATIVE RULE: verb first}
    - {IMPERATIVE RULE: verb first}
expertise:
  depth: {specific regulations, systems, tools, or patterns -- not genre names}
  relevance: {what specific failure this role prevents that domain-general roles miss}
scope: {workspace | component | service | cross-team | org-wide}
collaborates_with:
  - {area}
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-{subrole}-{subject}.md"
workflow:
  - step: {enter perspective}
    description: {how the reviewer enters the domain view}
  - step: {examine}
    description: {what they assess through their lens}
  - step: {produce}
    description: {what artifact or decision they generate}
---

---

PHASE 4 -- BODY SECTION

1. Philosophy paragraph: what the role optimizes, what failure it prevents.

2. Domain specializations table. Column headers must come from domain vocabulary:

   FAIL: | Entity     | Purpose     | Notes        |
   FAIL: | Item       | Description | Impact       |

   PASS (healthcare):   | Regulation  | Scope             | Penalty Trigger    |
   PASS (backend/CLI):  | Command     | Failure Mode      | Recovery Path      |
   PASS (finance):      | Entry Type  | GL Impact         | Close Dependency   |
   PASS (discovery):    | Method      | Signal Type       | Confidence Level   |
   PASS (governance):   | Control     | Enforcement Point | Evidence Required  |

---

PHASE 5 -- WRITE FILES

  1. .roles/{area}/inertia-advocate.md  (only if generated in Phase 2)
  2. .roles/{area}/{subrole}.md

---

PHASE 6 -- AMEND

## AMEND
1. **Archetype**: `{current}` -- {reason it matches or diverges from the area's established pattern}
2. **Sharpen verify item {N}**: "{current text}" -> "{version naming a specific artifact or state}"
3. **Add to table**: {domain entity not yet listed} -- column `{domain column name}`
```

---

## V-02: Template-First (single axis: role sequence)

Axis: Role sequence -- both output file templates (inertia-advocate and main role) are
presented before the execution phases. The model sees the complete output shape at the
start of the prompt before any instructions.

Hypothesis: V-05 R2 introduces the inertia-advocate template in Phase 2 and the main role
template in Phase 3 -- the model first reads instructions, then encounters the template it
must fill in. Under token pressure, late-phase details get compressed. Presenting both
templates as a REFERENCE block before any instructions front-loads the structural contract
so the model cannot miss a field regardless of which phase it's in. If C-02 and C-11
are stable across all input types, the template-first architecture may be marginally more
robust than phase-embedded templates.

```
You are running /roles-create. Generate one role file at .roles/{area}/{subrole}.md.

---

REFERENCE TEMPLATES

These are the two output files you may need to write. Study them before execution.

Template A: inertia-advocate companion (generate only if .roles/{area}/inertia-advocate.md
does not exist; substitute {area} throughout)

---
name: inertia-advocate
version: "1.0"
archetype: {match area's established archetype; default craft}
orientation:
  frame: "Sees every change proposal through the migration cost it demands of users and
          systems already calibrated to the current state. The highest-trust pattern is
          the one the team already depends on."
  serves: "Teams deciding whether to adopt a new approach -- surfaces the true cost of
           switching away from the status quo before commitment is made."
lens:
  verify:
    - "Does the proposal explicitly name the {area} system, workflow, or pattern it replaces?"
    - "Is the migration path documented and are displaced {area} users identified before approval?"
    - "Are there users currently relying on the existing {area} pattern who must be consulted?"
    - "Is there a rollback plan if adoption stalls mid-transition in {area}?"
  simplify:
    - "Treat every new {area} approach as a migration cost until it names what it displaces."
    - "Never approve a replacement that does not document the path from the current state."
expertise:
  depth: "Status quo patterns in {area}, migration risk estimation, switching cost analysis,
          user habit lock-in, adoption failure modes, transition planning."
  relevance: "New roles optimize for the ideal end state; the inertia-advocate asks whether
              the current state is already good enough to keep. Without this lens, migration
              costs are invisible until they manifest as churn."
scope: cross-team
collaborates_with:
  - {area}
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-inertia-advocate-{subject}.md"
workflow:
  - step: scan
    description: "Identify what the proposed change would displace or supersede."
  - step: cost
    description: "Estimate migration effort, user impact, and rollback complexity."
  - step: challenge
    description: "Produce a written case for the current state with the minimum bar
                  the new approach must clear to justify the switch."
---

# Inertia Advocate

The inertia advocate makes the cost of change visible before commitment.

## Displacement Cost Assessment

| Existing {area} Pattern | Dependent Roles  | Migration Effort | Rollback Available |
|-------------------------|------------------|------------------|--------------------|
| {current pattern}       | {roles affected} | low/medium/high  | yes/no             |

---

Template B: main role (generate for every invocation; substitute all {placeholders} with
domain-specific content; no placeholder text in the written file)

---
name: {subrole}
version: "1.0"
archetype: {value -- check existing roles in the area first; use their archetype}
orientation:
  frame: {first-person observational: how this role perceives its domain}
  serves: {third-person recipient: who benefits; must name a beneficiary, not describe
           the role itself}
lens:
  verify:
    - {boolean check naming a specific artifact, state, or config; min 4}
    - {boolean check naming a threshold, sequence, or system state}
    - {boolean check naming a failure condition, boundary case, or approval gate}
    - {boolean check naming a user action, field value, or config element}
  simplify:
    - {imperative rule; verb first}
    - {imperative rule; verb first}
expertise:
  depth: {specific domain regulations, systems, tools, or patterns}
  relevance: {what this role prevents that domain-general roles cannot}
scope: {workspace | component | service | cross-team | org-wide}
collaborates_with:
  - {area}
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-{subrole}-{subject}.md"
workflow:
  - step: {enter perspective}
    description: {how the reviewer enters the domain view}
  - step: {examine}
    description: {what they assess through their lens}
  - step: {produce}
    description: {artifact or decision produced}
---

{philosophy paragraph: what the role optimizes and what failure it exists to prevent}

{domain specializations table with domain-named column headers -- not "Entity / Purpose"}

Examples of domain-named headers:
  Healthcare/compliance:  | Regulation | Scope             | Penalty Trigger    |
  Backend/CLI:            | Command    | Failure Mode      | Recovery Path      |
  Finance/GL:             | Entry Type | GL Impact         | Close Dependency   |
  Discovery/research:     | Method     | Signal Type       | Confidence Level   |
  Governance/ops:         | Control    | Enforcement Point | Evidence Required  |

Generic headers (Entity, Item, Area, Purpose, Description, Notes, Impact) = FAIL.
Domain-named headers = PASS.

---

EXECUTION

Step 1 -- Mode detection

  NAME-ONLY     `area:subrole` -- extract tokens. No questions. Proceed immediately.

  DESCRIPTION   Quoted or natural language phrase -- extract domain, function, audience.
                No questions. Proceed immediately.

  INTERACTIVE   No argument -- HOLD. Ask all three in a single message:

                  "Let's build a new role. Please answer all three before I start:
                   1. Area name
                   2. Subrole name
                   3. One sentence: what does this role watch for?"

                - Do not generate any content after receiving only one or two answers.
                - Do not produce a draft, stub, or partial frontmatter mid-conversation.
                - Proceed only when all three are confirmed.

Step 2 -- Inertia-advocate check

  Does .roles/{area}/inertia-advocate.md exist?
  ABSENT:  Generate Template A (from REFERENCE above), substituting {area} throughout.
           Announce: "No inertia-advocate in '{area}' -- generating companion file first."
           Write to: .roles/{area}/inertia-advocate.md
  PRESENT: Proceed silently.

Step 3 -- Generate main role

  Fill in Template B (from REFERENCE above) with domain-specific content.
  Every {placeholder} must be replaced with content specific to the named domain.
  Verify: no placeholder text remains in the written output.

Step 4 -- Write files

  1. .roles/{area}/inertia-advocate.md  (if generated in Step 2)
  2. .roles/{area}/{subrole}.md

Step 5 -- AMEND

## AMEND
1. **Archetype**: `{current}` -- {match to area's established pattern, or alternative}
2. **Sharpen verify item {N}**: "{current}" -> "{version with specific artifact or threshold}"
3. **Add to table**: {entity not yet represented} -- column `{domain column name}`
```

---

## V-03: Pre-Write Audit (single axis: lifecycle emphasis)

Axis: Lifecycle emphasis -- a mandatory AUDIT PHASE is inserted between content generation
and writing. The audit lists one explicit yes/no check per rubric criterion. If any check
returns NO, the model fixes in place before proceeding to write.

Hypothesis: V-05 R2's AMEND block catches issues post-write, when the file already exists.
A pre-write audit shifts detection earlier: the model runs a self-check against the same
criteria the rubric uses, then fixes before writing. This converts post-hoc correction into
pre-commit validation and may catch C-04, C-08, C-09, C-10 regressions that the AMEND block
only flags for later human review. If the audit phase materially reduces regressions under
adversarial or long-context runs, it represents a new high-value phase pattern.

```
You are running /roles-create. Generate one role file at .roles/{area}/{subrole}.md.
Execute all seven phases in order. Do not write files before completing Phase 6.

---

PHASE 1 -- MODE DETECTION

  NAME-ONLY     `area:subrole` (colon, no whitespace, no quotes)
                Extract area and subrole. Proceed to Phase 2.

  DESCRIPTION   Quoted string or natural language phrase.
                Extract domain, function, audience. Proceed to Phase 2.

  INTERACTIVE   No argument.
                HOLD. Send this message and nothing else:

                  "Let's build a new role. Please answer all three before I start:
                   1. Area name (e.g. backend, finance, compliance, discovery)
                   2. Subrole name (e.g. healthcare, cost-analyst, audit-reviewer)
                   3. One sentence: what does this role watch for or optimize?"

                Rules:
                - Do not generate any role content after receiving only one or two answers.
                - Do not produce a draft, stub, or partial frontmatter mid-conversation.
                - Proceed to Phase 2 only when all three values are confirmed.

Output of Phase 1: {area}, {subrole}, {orientation seed}.

---

PHASE 2 -- INERTIA-ADVOCATE COMPANION

Check: .roles/{area}/inertia-advocate.md -- does it exist?

ABSENT: Announce "No inertia-advocate in '{area}' -- generating companion file first."
Generate this complete file, substituting {area} throughout:

---
name: inertia-advocate
version: "1.0"
archetype: {match archetype of existing roles in this area; default craft}
orientation:
  frame: "Sees every change proposal through the migration cost it demands of users and
          systems already calibrated to the current state. The highest-trust pattern is
          the one the team already depends on."
  serves: "Teams deciding whether to adopt a new approach -- surfaces the true cost of
           switching away from the status quo before commitment is made."
lens:
  verify:
    - "Does the proposal explicitly name the {area} system, workflow, or pattern it replaces?"
    - "Is the migration path documented and are displaced {area} users identified before approval?"
    - "Are there users currently relying on the existing {area} pattern who must be consulted?"
    - "Is there a rollback plan if adoption stalls mid-transition in {area}?"
  simplify:
    - "Treat every new {area} approach as a migration cost until it names what it displaces."
    - "Never approve a replacement that does not document the path from the current state."
expertise:
  depth: "Status quo patterns in {area}, migration risk estimation, switching cost analysis,
          user habit lock-in, adoption failure modes, transition planning."
  relevance: "New roles optimize for the ideal end state; the inertia-advocate asks whether
              the current state is already good enough to keep. Without this lens, migration
              costs are invisible until they manifest as churn."
scope: cross-team
collaborates_with:
  - {area}
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-inertia-advocate-{subject}.md"
workflow:
  - step: scan
    description: "Identify what the proposed change would displace or supersede."
  - step: cost
    description: "Estimate migration effort, user impact, and rollback complexity."
  - step: challenge
    description: "Produce a written case for the current state with the minimum bar
                  the new approach must clear to justify the switch."
---

# Inertia Advocate

The inertia advocate makes the cost of change visible before commitment.

## Displacement Cost Assessment

| Existing {area} Pattern | Dependent Roles  | Migration Effort | Rollback Available |
|-------------------------|------------------|------------------|--------------------|
| {current pattern}       | {roles affected} | low/medium/high  | yes/no             |

(Store this draft; write to disk in Phase 7.)

PRESENT: Proceed silently.

---

PHASE 3 -- ROLE CONTENT GENERATION

Generate domain-specific content for every field. No generic language.

  archetype           -- check existing roles in {area}; match their archetype value
                         craft = technical/builder areas (backend, flows, astro)
                         process = governance/ops areas (compliance, admin, discovery)
  orientation.frame   -- first-person observational: what this role always watches for
  orientation.serves  -- third-person recipient: name the beneficiary; must not be
                          a self-description of the role
  lens.verify         -- 4+ boolean checks; each names a specific artifact, state,
                          config, or command; each answerable yes/no about a real system
  lens.simplify       -- 2+ imperative rules; verb first
  expertise.depth     -- specific domain regulations, systems, tools, or patterns
  expertise.relevance -- what specific failure this role prevents that others miss
  scope               -- workspace | component | service | cross-team | org-wide
  collaborates_with   -- roles in this area or adjacent areas
  artifacts           -- review artifact with naming convention
  workflow            -- 3 steps: enter perspective / examine / produce

(Store this draft; write to disk in Phase 7.)

---

PHASE 4 -- BODY SECTION

Write the markdown body below the frontmatter:

1. Philosophy paragraph: what the role optimizes, what question it asks that no other
   role in the area asks, what failure it exists to prevent.

2. Domain specializations table with domain-named column headers:

   FAIL: | Entity     | Purpose     | Notes        |
   FAIL: | Item       | Description | Impact       |

   PASS (healthcare):   | Regulation  | Scope             | Penalty Trigger    |
   PASS (backend/CLI):  | Command     | Failure Mode      | Recovery Path      |
   PASS (finance):      | Entry Type  | GL Impact         | Close Dependency   |
   PASS (discovery):    | Method      | Signal Type       | Confidence Level   |
   PASS (governance):   | Control     | Enforcement Point | Evidence Required  |

(Store this draft; write to disk in Phase 7.)

---

PHASE 5 -- BODY SECTION (INERTIA-ADVOCATE)

If inertia-advocate was generated in Phase 2, ensure its body also contains a domain
specializations table with domain-named column headers (same FAIL/PASS rule as Phase 4).

---

PHASE 6 -- PRE-WRITE AUDIT

Before writing any file, verify each item below. Answer YES or NO for each.
If NO: fix the issue in the stored draft before proceeding to Phase 7.

  [A] Does .roles/{area}/{subrole}.md exist as the output path? (not current dir, not simulations/)
  [B] Does the main role frontmatter contain all 12 fields: name, version, archetype,
      orientation.frame, orientation.serves, lens.verify (list), lens.simplify (list),
      expertise.depth, expertise.relevance, scope, collaborates_with, artifacts, workflow?
  [C] Is orientation.frame written in first-person observational register
      (not "This role monitors..." or "Reviews X for the team.")?
  [D] Does orientation.serves name a specific beneficiary
      (not "Serves the team" or a self-description of the role)?
  [E] Does each lens.verify item reference a specific artifact, state, or config
      (not "Check X" or "Review Y" without concrete conditions)?
  [F] Do the domain specializations table column headers use domain vocabulary
      (not "Entity", "Item", "Purpose", "Description", "Notes")?
  [G] If interactive mode: were all three inputs (area, subrole, orientation seed)
      confirmed before any content was generated? (skip if non-interactive)
  [H] If inertia-advocate was generated: does its file include all 12 required
      frontmatter fields with {area} values substituted (not literal {area})?

For any NO answer: quote the problematic text and the corrected version before Phase 7.

---

PHASE 7 -- WRITE FILES

Write in this order:
  1. .roles/{area}/inertia-advocate.md  (only if generated in Phase 2)
  2. .roles/{area}/{subrole}.md

---

PHASE 8 -- AMEND

## AMEND
1. **Archetype**: `{current}` -- {reason it matches the area's established pattern, or alternative}
2. **Sharpen verify item {N}**: "{current text}" -> "{version naming a specific artifact or state}"
3. **Add to table**: {entity not yet listed} -- column `{domain column name}`
```

---

## V-04: Ambiguous-Input Routing (single axis: role sequence)

Axis: Role sequence -- promote edge-case input handling to PHASE 0, before the three-mode
detection gate. The three clean modes (NAME-ONLY, DESCRIPTION, INTERACTIVE) do not cover:
bare area with no subrole, extra colons, descriptions that are too vague to extract a domain,
or single-word inputs. An explicit INVALID INPUT path prevents silent misclassification.

Hypothesis: V-05 R2 assumes three clean input shapes. Real invocations include partial names,
typos, and under-specified descriptions. Silent misclassification (e.g., "backend" treated as
a description and generating a generic role with no sub-role name) produces a file at an
incorrect path that passes no essential criteria. An explicit INVALID path asks one targeted
clarifying question per missing piece instead of misclassifying and proceeding. This adds
robustness on C-01 (correct path) and C-03 (correct routing) for real-world inputs that
the current rubric does not stress-test.

```
You are running /roles-create. Generate one role file at .roles/{area}/{subrole}.md.

---

PHASE 0 -- INPUT VALIDATION

Before mode detection, check for these edge cases:

  BARE AREA      Input is a single word with no colon and no natural-language structure.
                 Example: `backend` or `finance`
                 Action: treat as INTERACTIVE. Proceed to Phase 1 INTERACTIVE path.

  EXTRA COLONS   Input contains more than one colon.
                 Example: `backend:healthcare:v2` or `a:b:c`
                 Action: use the first two tokens only (area = before first colon,
                         subrole = between first and second colon). Proceed to Phase 1
                         NAME-ONLY path.

  VAGUE PHRASE   Input is quoted or natural language but shorter than 6 words OR contains
                 no identifiable domain noun (no area-relevant nouns, no functional role
                 description).
                 Example: `"create a role"` or `"something for compliance"`
                 Action: ask one targeted clarifying question:
                   "I can see this is a [compliance/unclear] role -- could you name the
                    specific area (e.g. `finance:tax-analyst`) or describe what this role
                    reviews in one sentence?"
                 Wait for a revised input before continuing.

  EMPTY          Input is blank or whitespace only.
                 Action: treat as INTERACTIVE.

If none of these edge cases apply, proceed directly to Phase 1.

---

PHASE 1 -- MODE DETECTION

  NAME-ONLY     `area:subrole` (colon, no whitespace, no quotes)
                Extract area and subrole. Proceed to Phase 2.

  DESCRIPTION   Quoted string or natural language phrase (5+ words with domain noun).
                Extract domain, function, audience. Proceed to Phase 2.

  INTERACTIVE   No argument (or routed from Phase 0).
                HOLD. Send this message and nothing else:

                  "Let's build a new role. Please answer all three before I start:
                   1. Area name (e.g. backend, finance, compliance, discovery)
                   2. Subrole name (e.g. healthcare, cost-analyst, audit-reviewer)
                   3. One sentence: what does this role watch for or optimize?"

                Rules:
                - Do not generate any role content after receiving only one or two answers.
                - Do not produce a draft, stub, or partial frontmatter mid-conversation.
                - Proceed to Phase 2 only when all three values are confirmed.

Output of Phase 1: {area}, {subrole}, {orientation seed}.

---

PHASE 2 -- INERTIA-ADVOCATE COMPANION

Check: .roles/{area}/inertia-advocate.md -- does it exist?

ABSENT: Announce "No inertia-advocate in '{area}' -- generating companion file first."
Generate this complete file, substituting {area} throughout:

---
name: inertia-advocate
version: "1.0"
archetype: {match archetype of existing roles in this area; default craft}
orientation:
  frame: "Sees every change proposal through the migration cost it demands of users and
          systems already calibrated to the current state. The highest-trust pattern is
          the one the team already depends on."
  serves: "Teams deciding whether to adopt a new approach -- surfaces the true cost of
           switching away from the status quo before commitment is made."
lens:
  verify:
    - "Does the proposal explicitly name the {area} system, workflow, or pattern it replaces?"
    - "Is the migration path documented and are displaced {area} users identified before approval?"
    - "Are there users currently relying on the existing {area} pattern who must be consulted?"
    - "Is there a rollback plan if adoption stalls mid-transition in {area}?"
  simplify:
    - "Treat every new {area} approach as a migration cost until it names what it displaces."
    - "Never approve a replacement that does not document the path from the current state."
expertise:
  depth: "Status quo patterns in {area}, migration risk estimation, switching cost analysis,
          user habit lock-in, adoption failure modes, transition planning."
  relevance: "New roles optimize for the ideal end state; the inertia-advocate asks whether
              the current state is already good enough to keep. Without this lens, migration
              costs are invisible until they manifest as churn."
scope: cross-team
collaborates_with:
  - {area}
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-inertia-advocate-{subject}.md"
workflow:
  - step: scan
    description: "Identify what the proposed change would displace or supersede."
  - step: cost
    description: "Estimate migration effort, user impact, and rollback complexity."
  - step: challenge
    description: "Produce a written case for the current state with the minimum bar
                  the new approach must clear to justify the switch."
---

# Inertia Advocate

The inertia advocate makes the cost of change visible before commitment.

## Displacement Cost Assessment

| Existing {area} Pattern | Dependent Roles  | Migration Effort | Rollback Available |
|-------------------------|------------------|------------------|--------------------|
| {current pattern}       | {roles affected} | low/medium/high  | yes/no             |

Write to: .roles/{area}/inertia-advocate.md

PRESENT: Proceed silently.

---

PHASE 3 -- ROLE CONTENT GENERATION

Generate domain-specific content for every field. No generic language.

  archetype           -- check existing roles in {area}; match their archetype value
                         craft = technical/builder areas | process = governance/ops areas
  orientation.frame   -- first-person observational: what this role perceives in the domain
                         Good: "Sees every patient data boundary as a PHI exposure surface
                                requiring documented access justification before approval."
                         Bad:  "Reviews healthcare compliance for the team."
  orientation.serves  -- third-person recipient: who benefits; must name a beneficiary
                         Good: "Compliance officers who must certify PHI handling satisfies
                                HIPAA requirements before system approval."
                         Bad:  "Serves the team by ensuring compliance."
  lens.verify         -- 4+ boolean checks naming specific artifacts or system states
                         Good: "Is PHI encrypted at rest using an approved algorithm before
                                HIPAA Security Rule compliance review?"
                         Bad:  "Check audit log configuration."
  lens.simplify       -- 2+ imperative rules; verb first
  expertise.depth     -- specific regulations, systems, tools, or patterns
  expertise.relevance -- what specific failure this role prevents that others miss
  scope, collaborates_with, artifacts, workflow -- standard fields

---

PHASE 4 -- BODY SECTION

1. Philosophy paragraph: what the role optimizes, what failure it prevents.

2. Domain specializations table:

   FAIL: | Entity     | Purpose     | Notes        |
   FAIL: | Item       | Description | Impact       |

   PASS (healthcare):   | Regulation  | Scope             | Penalty Trigger    |
   PASS (backend/CLI):  | Command     | Failure Mode      | Recovery Path      |
   PASS (finance):      | Entry Type  | GL Impact         | Close Dependency   |
   PASS (discovery):    | Method      | Signal Type       | Confidence Level   |
   PASS (governance):   | Control     | Enforcement Point | Evidence Required  |

---

PHASE 5 -- WRITE FILES

  1. .roles/{area}/inertia-advocate.md  (only if generated in Phase 2)
  2. .roles/{area}/{subrole}.md

---

PHASE 6 -- AMEND

## AMEND
1. **Archetype**: `{current}` -- {match to area's established pattern or specific alternative}
2. **Sharpen verify item {N}**: "{current text}" -> "{version naming specific artifact or state}"
3. **Add to table**: {entity not yet listed} -- column `{domain column name}`
```

---

## V-05: Separation-of-Contracts (combined: output format + phrasing register)

Axis: Output format + phrasing register -- all behavioral contracts (field register rules,
interactive hold prohibitions, column header FAIL/PASS table, inertia-advocate fill-in
template) are grouped into a dedicated CONTRACTS section at the prompt head. The execution
phases that follow reference these contracts by name rather than embedding them inline.

Hypothesis: V-05 R2 embeds contracts within phases (HOLD rules in Phase 1, template in
Phase 2, FAIL/PASS table in Phase 4). Under long-context execution, early-phase contracts
may have diminished salience by the time late phases run. Surfacing all contracts at the
head of the prompt -- before any execution instruction -- ensures they remain independently
consultable throughout execution. This tests whether contract salience is position-dependent
in the model's attention, and whether a dedicated contracts section produces more consistent
C-08/C-09/C-10 compliance across domain inputs not covered by the examples.

```
You are running /roles-create. Generate one role file at .roles/{area}/{subrole}.md.

---

CONTRACTS

All behavioral constraints for this skill. Execution phases reference these by name.

---

CONTRACT: INTERACTIVE HOLD

When no argument is provided, ask all three questions in a single message before proceeding.

  Questions to send:
    "Let's build a new role. Please answer all three before I start:
     1. Area name (e.g. backend, finance, compliance, discovery)
     2. Subrole name (e.g. healthcare, cost-analyst, audit-reviewer)
     3. One sentence: what does this role watch for or optimize?"

  Rules -- these are categorical prohibitions, not preferences:
    - Do not generate any role content after receiving only one or two answers.
    - Do not produce a draft, stub, or partial frontmatter mid-conversation.
    - Proceed to execution only when all three values are confirmed.

---

CONTRACT: FIELD REGISTER

Each frontmatter field has a required register. Content outside this register fails C-04/C-09.

| Field              | Register         | Good example                                              | Anti-pattern |
|--------------------|------------------|-----------------------------------------------------------|--------------|
| orientation.frame  | First-person observational | "Sees every API boundary as a contract that either holds under failure or becomes an operational liability." | "Reviews API compliance for the team." |
| orientation.serves | Third-person recipient -- names beneficiary | "Engineers who need confirmed contract stability before deploying clients across versions." | "Serves the team by reviewing APIs." |
| lens.verify (each) | Boolean check naming specific artifact | "Is the idempotency key validated server-side before the transaction commits?" | "Check idempotency." |
| expertise.depth    | Specific systems/regulations/tools | "HIPAA Privacy Rule, HITECH, HL7 v2/v3, FHIR R4, BAA scope, covered entity obligations" | "Healthcare compliance standards." |
| archetype          | Match area's established value | Check existing roles in the area first; use their value | Applying craft/process without checking |

---

CONTRACT: COLUMN HEADER

Every body table MUST use domain-vocabulary column headers.

  FAIL: | Entity     | Purpose     | Notes        |
  FAIL: | Item       | Description | Impact       |
  FAIL: | Area       | Value       | Consideration|

  PASS (healthcare/compliance): | Regulation  | Scope             | Penalty Trigger    |
  PASS (backend/CLI):           | Command     | Failure Mode      | Recovery Path      |
  PASS (finance/GL):            | Entry Type  | GL Impact         | Close Dependency   |
  PASS (discovery/research):    | Method      | Signal Type       | Confidence Level   |
  PASS (governance/ops):        | Control     | Enforcement Point | Evidence Required  |
  PASS (any domain):            Use nouns from the domain's own vocabulary in every column.

Rule: generic headers ("Entity", "Item", "Purpose", "Description") = FAIL regardless of
what the rows contain. Domain-named headers = PASS regardless of row count.

---

CONTRACT: INERTIA-ADVOCATE TEMPLATE

When .roles/{area}/inertia-advocate.md is absent, generate this complete file.
Substitute {area} throughout. Do not leave literal {area} in the written file.

---
name: inertia-advocate
version: "1.0"
archetype: {match archetype of existing roles in this area; default craft}
orientation:
  frame: "Sees every change proposal through the migration cost it demands of users and
          systems already calibrated to the current state. The highest-trust pattern is
          the one the team already depends on."
  serves: "Teams deciding whether to adopt a new approach -- surfaces the true cost of
           switching away from the status quo before commitment is made."
lens:
  verify:
    - "Does the proposal explicitly name the {area} system, workflow, or pattern it replaces?"
    - "Is the migration path documented and are displaced {area} users identified before approval?"
    - "Are there users currently relying on the existing {area} pattern who must be consulted?"
    - "Is there a rollback plan if adoption stalls mid-transition in {area}?"
  simplify:
    - "Treat every new {area} approach as a migration cost until it names what it displaces."
    - "Never approve a replacement that does not document the path from the current state."
expertise:
  depth: "Status quo patterns in {area}, migration risk estimation, switching cost analysis,
          user habit lock-in, adoption failure modes, transition planning."
  relevance: "New roles optimize for the ideal end state; the inertia-advocate asks whether
              the current state is already good enough to keep. Without this lens, migration
              costs are invisible until they manifest as churn."
scope: cross-team
collaborates_with:
  - {area}
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-inertia-advocate-{subject}.md"
workflow:
  - step: scan
    description: "Identify what the proposed change would displace or supersede."
  - step: cost
    description: "Estimate migration effort, user impact, and rollback complexity."
  - step: challenge
    description: "Produce a written case for the current state with the minimum bar
                  the new approach must clear to justify the switch."
---

# Inertia Advocate

The inertia advocate makes the cost of change visible before commitment.

## Displacement Cost Assessment

  (Use CONTRACT: COLUMN HEADER -- domain-named headers required)

| Existing {area} Pattern | Dependent Roles  | Migration Effort | Rollback Available |
|-------------------------|------------------|------------------|--------------------|
| {current pattern}       | {roles affected} | low/medium/high  | yes/no             |

---

EXECUTION PHASES

---

PHASE 1 -- MODE DETECTION

  NAME-ONLY     `area:subrole` (colon, no whitespace, no quotes)
                Extract area and subrole. Proceed to Phase 2.

  DESCRIPTION   Quoted string or natural language phrase.
                Extract domain, function, audience. Proceed to Phase 2.

  INTERACTIVE   No argument.
                Apply CONTRACT: INTERACTIVE HOLD before proceeding.

Output of Phase 1: {area}, {subrole}, {orientation seed}.

---

PHASE 2 -- INERTIA-ADVOCATE COMPANION

Check: .roles/{area}/inertia-advocate.md

ABSENT: Announce "No inertia-advocate in '{area}' -- generating companion file first."
        Apply CONTRACT: INERTIA-ADVOCATE TEMPLATE. Substitute all {area} slots.
        Write to: .roles/{area}/inertia-advocate.md

PRESENT: Proceed silently.

---

PHASE 3 -- ROLE CONTENT GENERATION

Generate domain-specific content for every field. Apply CONTRACT: FIELD REGISTER for
orientation.frame, orientation.serves, lens.verify, expertise.depth, and archetype.

  ---
  name: {subrole}
  version: "1.0"
  archetype: {value -- see CONTRACT: FIELD REGISTER}
  orientation:
    frame: {see CONTRACT: FIELD REGISTER}
    serves: {see CONTRACT: FIELD REGISTER}
  lens:
    verify:
      - {see CONTRACT: FIELD REGISTER -- min 4 items}
      - ...
    simplify:
      - {imperative; verb first}
      - {imperative; verb first}
  expertise:
    depth: {see CONTRACT: FIELD REGISTER}
    relevance: {what specific failure this role prevents that others miss}
  scope: {workspace | component | service | cross-team | org-wide}
  collaborates_with:
    - {area}
  artifacts:
    - type: review
      directory: reviews/
      format: markdown
      naming: "review-{area}-{subrole}-{subject}.md"
  workflow:
    - step: {enter perspective}
      description: {how the reviewer enters the domain view}
    - step: {examine}
      description: {what they assess through their lens}
    - step: {produce}
      description: {artifact or decision produced}
  ---

---

PHASE 4 -- BODY SECTION

1. Philosophy paragraph: what this role optimizes, what failure it prevents.

2. Domain specializations table. Apply CONTRACT: COLUMN HEADER.

3. Optional: checklist or decision tree if the workflow is sequential.

---

PHASE 5 -- WRITE FILES

  1. .roles/{area}/inertia-advocate.md  (only if generated in Phase 2)
  2. .roles/{area}/{subrole}.md

---

PHASE 6 -- AMEND

## AMEND
1. **Archetype**: `{current}` -- {match to area's established pattern or alternative}
2. **Sharpen verify item {N}**: "{current text}" -> "{version with specific artifact or threshold}"
3. **Add to table**: {domain entity not yet listed} -- column `{domain column name}`
```

---

## Variation Summary

| ID | Axis | What it tests | New capability | Risk |
|----|------|---------------|----------------|------|
| V-01 | Constraint-minimal (register) | Can mechanics without Good/Bad examples maintain 100? | ~40% shorter prompt; tests whether examples are load-bearing | C-04, C-09 may regress without per-field anchors |
| V-02 | Template-first (role sequence) | Does pre-loading both templates before instructions reduce field omissions? | Output shape visible before execution; model can look back at templates during generation | May be redundant if token attention doesn't benefit from front-loading |
| V-03 | Pre-write audit (lifecycle) | Does a self-check phase before writing catch issues earlier than AMEND? | Shifts error detection from post-write to pre-write; fix-in-place loop | Adds one full phase; under token pressure, audit items may be skimmed |
| V-04 | Ambiguous-input routing (role sequence) | Does explicit edge-case handling improve robustness on malformed input? | Explicit INVALID path for bare area, extra colons, vague phrases, empty input | Phase 0 overhead irrelevant for clean inputs; may over-trigger on natural descriptions |
| V-05 | Separation-of-contracts (format + register) | Does grouping all contracts at prompt head make them more consistently applied? | Contracts independently consultable; phases reference by name | Cross-reference structure may fragment attention vs inline embedding |

Expected R3 scoring (v2 rubric):

| ID | C-01..C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | Est. Score |
|----|-----------|------|------|------|------|------|------|------|------------|
| V-01 | P | P | P | P | P | P | P | P | **100** |
| V-02 | P | P | P | P | P | P | P | P | **100** |
| V-03 | P | P | P | P | P | P | P | P | **100** |
| V-04 | P | P | P | P | P | P | P | P | **100** |
| V-05 | P | P | P | P | P | P | P | P | **100** |

All expected at 100 on v2. The discrimination among R3 variations is not v2 score but
architectural robustness: which prompt structure is most reliable under adversarial input,
token pressure, or domains not covered by the FAIL/PASS examples? That question requires
a v3 rubric or adversarial scoring to resolve.
