Written to `simulations/quest/variations/roles-create-variations-R1-2026-03-17.md`.

---

## Variations: roles-create R1

**Test invocations**: name-only (`backend:healthcare`), description (`"healthcare compliance officer who reviews HIPAA"`), interactive (no arg).

| ID | Axis | Primary Rubric Target | Key Bet |
|----|------|-----------------------|---------|
| **V-01** | Mode-routing-first | C-03, C-05 | Mode detection is an explicit Step 1 that gates all generation; inertia check is Step 2. No ambiguity before content begins. |
| **V-02** | Template-anchored | C-02, C-06, C-09 | Shows the exact file shape with per-field format contracts and inline good/bad examples. Eliminates missing fields and vague verify items by showing not describing. |
| **V-03** | Inertia-gated | C-05, C-08 | Inertia-advocate check is a hard Phase 2 gate with explicit ABSENT/PRESENT branches. Absent = companion role generated first. Targets the silent-skip failure directly. |
| **V-04** | Conversational register | C-04, C-09 | Descriptive, second-person prompt rather than imperative. Tests whether modeling the conversational voice produces more naturalistic orientation and expertise content. |
| **V-05** | Full integration | All 9 criteria | 5-phase lifecycle with phase contracts: mode detection → inertia gate → field template → body → AMEND. Highest composite ceiling; highest verbosity risk. |

**Three single-axis variations**: V-01 (sequence), V-02 (format), V-03 (inertia framing). V-04 adds register. V-05 combines all four.
e from the phrase.
                Do NOT prompt for more information.

  INTERACTIVE   No argument provided.
                Action: ask the user for three fields in sequence:
                  1. area (e.g. backend, finance, discovery)
                  2. subrole name (e.g. healthcare, performance-analyst)
                  3. orientation description (one sentence)
                Then generate from those answers.

If the input fits NAME-ONLY or DESCRIPTION, do not ask any clarifying questions.

## Step 2 -- Inertia-advocate check

Before generating the requested role, check whether an inertia-advocate already exists
in .craft/roles/{area}/.

If NOT present: tell the user "Note: no inertia-advocate exists for area {area}. Run
/roles-create {area}:inertia-advocate to add it." Include this message in the response
before writing the requested role.

If PRESENT: proceed silently.

## Step 3 -- Generate role content

Generate domain-specific content for the detected mode. Every field must draw from
the input domain -- not from adjacent or generic templates.

orientation:
  frame:  Self-directed. How this role sees the domain and what they optimize for.
  serves: Receiver-directed. Who benefits from this role's presence and why.

lens:
  verify: At least 4 boolean checks. Each must reference a specific condition, artifact,
          system, or configuration element from the domain. Phrasing: "Is X configured
          before Y?", "Does Z produce artifact A?", "Are N items set to...?"
          Avoid: "Check configuration", "Review security", "Ensure compliance".
  simplify: At least 2 imperative rules that encode the role's heuristics.

expertise:
  depth:     Domain-specific systems, tools, regulations, or patterns. Not generic
             "software engineering depth".
  relevance: Why this perspective is essential for this domain specifically.

archetype:  Match the area's established pattern (craft for technical areas,
            process-specific for governance/discovery areas).

scope: workspace | component | service | cross-team | org-wide

collaborates_with: List roles that exist in this area or adjacent areas.

artifacts: Standard review artifact pointing to reviews/ with naming
           review-{area}-{subrole}-{subject}.md

workflow: 3 steps -- trace/empathize/walkthrough, review/evaluate, produce/report.

## Step 4 -- Write body section

Below the frontmatter, write a markdown body with:
1. One paragraph explaining the role's philosophy (what they optimize, who they block for).
2. At least one structured table mapping domain-specific entities to their purpose.
   (Examples: Regulation -> guard command -> artifact, Command -> user tier -> what they see,
   Constraint -> enforcement point -> failure mode)
3. Optional: a checklist or failure pattern list relevant to the domain.

## Step 5 -- Write the file

Write the complete role to: .craft/roles/{area}/{subrole}.md

## Step 6 -- AMEND section

After writing, print an AMEND block with 3 targeted suggestions:
1. Archetype adjustment (if the current archetype may not match the area's tier pattern)
2. One specific lens.verify question to sharpen (name the item and the sharper version)
3. One domain specialization to add to the body table
```

---

## V-02: Template-Anchored (single axis: output format)

Axis: Output format -- provide the exact expected file structure with per-field format contracts and inline examples. No prose description of what to do; show the shape of the output instead.

Hypothesis: Anchoring generation to a concrete template with format contracts per field (not just field names) eliminates the most common failure modes: missing frontmatter fields (C-02), generic expertise (C-04), vague verify items (C-06), and register mismatch (C-09). Showing the shape is more reliable than describing it.

```
You are running /roles-create. Detect the input mode, then write a role file.

## Mode detection

NAME-ONLY  -- input is `area:subrole` (no spaces, no quotes). Derive from name.
DESCRIPTION -- input is a quoted phrase. Parse domain, function, audience.
INTERACTIVE -- no input. Ask: area, subrole name, one-sentence orientation. Then generate.

## Inertia-advocate check

Before writing, check if .craft/roles/{area}/inertia-advocate.md exists.
If absent: output "Suggestion: run /roles-create {area}:inertia-advocate" before the role file.

## Write the role file using this exact template

File path: .craft/roles/{area}/{subrole}.md

---
name: {subrole}
version: "1.0"
archetype: {craft | process | governance | ...}
  # craft = technical/developer areas (backend, astro, flash)
  # process = discovery/governance/ops areas
  # Use the archetype that matches other roles in this area

orientation:
  frame: "{How this role sees the domain. Self-directed. 'Sees every interaction through
           the lens of...' or 'Treats every X as a Y to verify...' -- first-person perspective.}"
  serves: "{Who benefits. Receiver-directed. Name the beneficiary explicitly:
           'PMs and analysts who need...', 'Compliance officers who must...'}"

lens:
  verify:
    - "{Falsifiable boolean check. Reference a specific artifact, config, or state.
       Good: 'Is the posting profile mapped to GL accounts before transaction posting?'
       Bad: 'Check posting configuration.'}"
    - "{Falsifiable boolean check. Reference a specific threshold, field, or sequence.}"
    - "{Falsifiable boolean check. Name a specific command, output, or export format.}"
    - "{Falsifiable boolean check. Reference a concrete user action or failure condition.}"
  simplify:
    - "{Imperative rule. Starts with a verb. 'Treat X as Y.', 'Never Z unless W.'}"
    - "{Imperative rule.}"

expertise:
  depth: "{Specific systems, regulations, tools, or patterns in this domain. If healthcare:
          name specific regulations (HIPAA, HITECH), specific audit types, specific artifact
          formats. No generic 'software engineering depth'.}"
  relevance: "{Why this role's perspective is essential. What it catches that technical
              roles miss. What failure it prevents that others cannot.}"

scope: {workspace | component | service | cross-team | org-wide}

collaborates_with:
  - {area}
  - {area:another-subrole-in-this-area}

artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-{subrole}-{subject}.md"

workflow:
  - step: {empathize | trace | walkthrough}
    description: "{Step the reviewer takes to enter the domain perspective.}"
  - step: {review | evaluate | assess}
    description: "{What the reviewer examines from their lens.}"
  - step: {produce | report | flag}
    description: "{What artifact or output they generate.}"
---

# {Role Title}

{One paragraph: the role's philosophy. What they optimize for. What they block.
 What question they ask that no other role in the area asks.}

## {Domain Entity Table -- name this section for the domain, not "Entities"}

| {Column 1 relevant to domain} | {Column 2} | {Column 3} |
|-------------------------------|------------|------------|
| {Specific domain item}        | {Purpose}  | {Failure mode or note} |

{Add checklist, evidence chain, or verification sequence if relevant to the domain.}

## AMEND

1. Archetype: {current value} -- consider {alternative} if area follows {pattern}.
2. Sharpen verify item N: "{current}" -> "{sharper version with specific condition}"
3. Add to table: {specific domain entity not yet listed}
```

---

## V-03: Inertia-Gated (single axis: inertia framing)

Axis: Inertia framing -- the inertia-advocate check is elevated to a hard gate that runs immediately after mode detection, with explicit decide-and-act semantics. Not a footnote; a required decision point.

Hypothesis: The silent-inertia-advocate-skip (C-05) failure happens when the skill treats the check as optional or low-priority. Making it a hard gate with explicit "present / absent" branches forces an affirmative decision. The most common fail is not a wrong decision but a skipped one.

```
You are running /roles-create. Generate a role file and surface the inertia-advocate
status for the target area before writing anything.

## Phase 1 -- Classify input

Classify the invocation as one of three modes:

  NAME-ONLY     `area:subrole` pattern -- derive all content from name. No questions.
  DESCRIPTION   Quoted natural language -- parse domain, function, audience. No questions.
  INTERACTIVE   No argument -- ask area, subrole name, orientation in sequence.

## Phase 2 -- Inertia-advocate gate (required before file generation)

Check: does .craft/roles/{area}/inertia-advocate.md exist?

  ABSENT  --> Output this line before the role file:
              "Area {area} has no inertia-advocate. The inertia-advocate challenges every
               role's assumptions by asking why the current state is sufficient. Run
               /roles-create {area}:inertia-advocate to add it."

              Then generate the inertia-advocate role first (as a secondary output),
              followed by the originally requested role.

  PRESENT --> Note silently. Continue to Phase 3.

The inertia-advocate for any area has:
  orientation.frame: Sees every proposal through the lens of what the existing system
                     already handles -- and what migration costs it would impose.
  lens.verify: At least one question naming the specific existing system, process, or
               pattern that would be displaced.

## Phase 3 -- Generate the requested role

Build content from the input domain. All fields must be domain-specific:

  orientation.frame    -- how this role perceives the domain (self-directed)
  orientation.serves   -- who benefits and why (receiver-directed, name the beneficiary)
  lens.verify          -- 4+ boolean checks naming specific artifacts, configs, or states
  lens.simplify        -- 2+ imperative heuristics
  expertise.depth      -- specific systems/regulations/tools, not generic depth
  expertise.relevance  -- what failure this role prevents that others cannot
  archetype            -- match the area's established archetype tier
  scope                -- workspace | component | service | cross-team | org-wide
  collaborates_with    -- roles in the same or adjacent areas
  artifacts            -- review artifact with naming review-{area}-{subrole}-{subject}.md
  workflow             -- 3 steps: enter perspective, examine, produce

## Phase 4 -- Write body section

Below the frontmatter:
1. Philosophy paragraph: what the role optimizes, what question it asks, what failure it prevents.
2. Domain specializations table: at minimum one table mapping domain-specific entities
   (commands, regulations, modules, components) to their purpose and failure mode.

## Phase 5 -- Write file

Write to: .craft/roles/{area}/{subrole}.md
(Write the inertia-advocate file first if it was absent in Phase 2.)

## Phase 6 -- AMEND block

Print three targeted amendments:
1. Archetype check: does current archetype match the area's tier pattern? If uncertain, say so.
2. Sharpen one lens.verify item: quote the current item, propose a more specific version.
3. One entity missing from the domain table: name it and its role.
```

---

## V-04: Conversational-Register (single axis: phrasing register)

Axis: Phrasing register -- the prompt is written in a descriptive, second-person, explanatory register rather than imperative technical language. Describe what the skill does and what the output should achieve; let the model infer the execution.

Hypothesis: A conversational register may produce more naturalistic role content -- the model may write orientation and expertise in a more grounded voice when the prompt itself models that voice. Tests whether imperative vs descriptive prompts trade off structural precision against content authenticity (C-04, C-09).

```
You are running /roles-create, which creates a single role or sub-role file in a
craftworks project's .craft/roles/ directory.

The skill has three ways it can be invoked:

When someone types /roles-create followed by a colon-separated pair like `backend:healthcare`,
that's the name-only mode. You should infer everything from the area name and subrole name --
no clarifying questions needed.

When someone types /roles-create followed by a quoted phrase like "a healthcare compliance
officer who reviews HIPAA audit trails", that's description mode. Parse the domain, the
function, and the audience from the phrase and generate accordingly.

When someone types /roles-create with no argument at all, that's interactive mode. Ask the
user three things in sequence: what area they're working in, what the subrole should be
called, and one sentence describing what the role sees or cares about. Then generate.

Before you write anything, check whether .craft/roles/{area}/inertia-advocate.md exists.
If it doesn't, mention it -- something like "I notice there's no inertia-advocate in the
{area} area yet. That role challenges proposals by asking why the current system is already
good enough. You might want to run /roles-create {area}:inertia-advocate after this."
Then proceed to create the requested role.

The file goes in .craft/roles/{area}/{subrole}.md and follows a standard YAML frontmatter
structure. The frontmatter has: name, version (always "1.0"), archetype (pick the one that
fits the area's established pattern -- craft for technical areas, process-specific for
governance/ops areas), orientation (frame and serves fields), lens (verify and simplify
sublists), expertise (depth and relevance), scope, collaborates_with, artifacts, and workflow.

The orientation.frame should read as if the role is speaking about itself -- how it sees
the domain, what it's always watching for. The orientation.serves should name the people
who benefit from having this perspective in the room.

For the lens.verify items, write them as specific boolean checks -- things an LLM or a
person could actually answer yes or no to about a real system. "Is the audit log timestamped
with timezone before export?" is good. "Check audit logging" is not useful. Aim for at least
four of these.

The expertise.depth field is where you name the actual systems, regulations, tools, or
domain-specific patterns the role knows about. Don't write "deep software engineering
knowledge" -- name what specifically is in scope for this role in this domain.

After the frontmatter, write a markdown body. Include at least one table that maps
domain-specific entities (commands, regulations, modules, components, processes) to what
they do and where they can fail. The role file is more useful when it grounds the reader
in the domain's specific vocabulary, not just the role's abstract purpose.

End with a short AMEND section offering three suggestions: one about whether the archetype
is the right choice for this area, one specific lens.verify item to tighten up, and one
domain entity that should be added to the body table.
```

---

## V-05: Integrated (combined: mode routing + template + inertia gate + lifecycle phases)

Axis: Full integration -- V-01's crisp mode detection, V-02's field-level template with format contracts, V-03's inertia gate as a hard phase, and explicit lifecycle phase boundaries with defined outputs per phase.

Hypothesis: Combining crisp mode branching, concrete template, mandatory inertia gate, and phase contracts addresses all 9 rubric criteria in a single pass. Expected highest composite score. Primary risk is verbosity -- the prompt is long enough that the model may truncate late phases under token pressure.

```
You are running /roles-create. Generate one role file at .craft/roles/{area}/{subrole}.md.
Run all five phases in order. Do not skip ahead.

---

PHASE 1 -- MODE DETECTION
Classify the invocation exactly once:

  NAME-ONLY     Input matches `area:subrole` (colon, no spaces, no quotes).
                Extract: area = left of colon. subrole = right of colon.
                Proceed immediately. No questions.

  DESCRIPTION   Input is a quoted phrase.
                Extract: domain, role function, intended audience.
                Proceed immediately. No questions.

  INTERACTIVE   No argument given.
                Ask in sequence:
                  (1) "What area? (e.g. backend, finance, compliance)"
                  (2) "What should the subrole be called? (e.g. healthcare, cost-analyst)"
                  (3) "One sentence: what does this role see or care about?"
                Wait for answers before proceeding.

Output of Phase 1: area string, subrole string, orientation seed.

---

PHASE 2 -- INERTIA-ADVOCATE GATE
Check: does .craft/roles/{area}/inertia-advocate.md exist?

ABSENT:
  Output before writing anything:
  "No inertia-advocate found for area '{area}'. The inertia-advocate is the role that
   challenges every proposal by asking why the current system is already good enough.
   Generating it now as a companion to {subrole}."

  Then generate the inertia-advocate as a first output:
    orientation.frame: Sees every change proposal through the cost of the migration
                       it requires and the habits it disrupts.
    orientation.serves: Teams deciding whether to adopt a new approach -- surfaces
                        the true price of switching away from the status quo.
    lens.verify: At least one question naming the specific existing system or pattern
                 that would be displaced by the requested role's domain.
    expertise.depth: Status quo patterns, migration risk, switching costs, user habit lock-in.

PRESENT:
  Proceed silently.

---

PHASE 3 -- ROLE CONTENT GENERATION
Build domain-specific content for the role identified in Phase 1. Every field must draw
from the input domain -- not from adjacent, generic, or neighboring-role templates.

Use this exact field structure:

---
name: {subrole}
version: "1.0"
archetype: {value}
  # craft      = technical/builder areas (backend, astro, flows, flash, craft)
  # process    = governance/ops/compliance areas (discovery, admin, compliance)
  # Use the archetype present in other roles in this area, if any exist.

orientation:
  frame: "{Self-directed. How the role perceives the domain. What they always watch for.
           Register: first-person observational. 'Sees every X as a Y...',
           'Treats every decision through the lens of...'}"
  serves: "{Receiver-directed. Who benefits and why. Name the beneficiary explicitly.
           Register: third-person recipient. 'Compliance officers who must...',
           'Developers who need...' Not a self-description.}"

lens:
  verify:
    - "{Boolean check. Name a specific artifact, state, or configuration. Min 4 items.
       Good: 'Is the HIPAA audit log exported in FHIR-compliant format before submission?'
       Bad: 'Check audit log configuration.'}"
    - "{Boolean check. Reference a threshold, sequence, or command output.}"
    - "{Boolean check. Name a specific failure condition or boundary case.}"
    - "{Boolean check. Reference a user action, field value, or system state.}"
  simplify:
    - "{Imperative rule. Verb first. 'Treat X as Y.', 'Never Z unless W.', 'Flag any...'}"
    - "{Imperative rule.}"

expertise:
  depth: "{Specific domain systems, regulations, tools, or patterns. No generic language.
           Healthcare: HIPAA, HITECH, HL7, FHIR, covered entity obligations, BAAs.
           Finance: GAAP, GL account structure, period close, reconciliation workflows.}"
  relevance: "{What this role catches that technical roles miss. What failure it prevents.
              Why the domain needs this perspective specifically.}"

scope: {workspace | component | service | cross-team | org-wide}

collaborates_with:
  - {area}
  - {area:subrole-that-exists-or-is-being-created}

artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-{area}-{subrole}-{subject}.md"

workflow:
  - step: {empathize | trace | walkthrough}
    description: "{How the reviewer enters the domain's perspective.}"
  - step: {review | assess | evaluate}
    description: "{What they examine from their specific lens.}"
  - step: {produce | report | flag}
    description: "{What artifact or output they generate.}"
---

---

PHASE 4 -- BODY SECTION
Write the markdown body below the frontmatter.

Required elements:
1. Philosophy paragraph (2-4 sentences): what the role optimizes, what question it asks
   that no other role in the area asks, what failure it exists to prevent.
2. Domain specializations table: at least one table mapping domain-specific entities
   (regulations, commands, modules, audit types, configurations) to their purpose and
   failure mode. Column names should reflect the domain, not generic "Entity / Purpose".
3. Optional: checklist, evidence chain, or decision tree if the role's workflow is sequential.

---

PHASE 5 -- OUTPUT AND AMEND
Write files:
  - .craft/roles/{area}/inertia-advocate.md  (if generated in Phase 2)
  - .craft/roles/{area}/{subrole}.md

After writing, print an AMEND block:

## AMEND
1. Archetype: {current value} -- {reason this fits or should be reconsidered for this area}
2. Sharpen verify item: "{current item}" -> "{version with specific condition or artifact named}"
3. Add to specializations table: {domain entity not yet listed and why it belongs}
```

---

## Variation Summary

| ID | Axis | Primary Rubric Target | Expected Strength | Expected Risk |
|----|------|-----------------------|-------------------|---------------|
| V-01 | Mode routing first | C-03, C-05 | No mode ambiguity; inertia check is step 2 | Template absent; C-02/C-06 depend on model initiative |
| V-02 | Field template with format contracts | C-02, C-06, C-09 | No missing fields; register contracts enforced per field | Mode routing implicit; C-03 may drift on edge cases |
| V-03 | Inertia as hard gate with companion generation | C-05, C-08 | Silent-skip failure eliminated; inertia-advocate gets a spec | Phase structure loose; C-02 field completeness varies |
| V-04 | Conversational register | C-04, C-09 | Naturalistic domain content; orientation voice more grounded | Structural precision lower; C-02/C-07 may be incomplete |
| V-05 | Full integration | All 9 criteria | Highest composite ceiling; phase contracts prevent late-phase drop | Longest prompt; model may truncate Phase 4-5 under token pressure |
