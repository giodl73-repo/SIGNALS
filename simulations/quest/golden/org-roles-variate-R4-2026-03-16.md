---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R4
rubric_version: v4
status: variate
---

# org-roles Variate — Round 4

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v4 (C-01 through C-20; new in v4: C-18 contrastive worked example pairs, C-19
enumerated multi-item completion gate, C-20 domain-specific registry extension)
**Round:** R4 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 4 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | inertia framing | C-20 PASS, C-19 PASS, C-18 PASS | A dedicated Inertia Specification phase produces a domain-specific status-quo claim that becomes the registry's named extension field — grounding C-20 in an earlier step output by construction; each domain expert also carries an inertia-response question that directly falsifies the Phase 2 challenge |
| V-02 | output format | C-18 PASS, C-19 PASS, C-20 PASS | Separating the role file template (structure only) from a standalone FIELD GUIDE (contrastive BAD/GOOD pairs per field) makes both directions present in every field annotation without annotating inside YAML; this maximizes C-18 coverage while keeping the template scannable |
| V-03 | lifecycle emphasis | C-20 PASS, C-19 PASS, C-18 PASS | A Phase 0 Extension Contract step commits to a named registry extension field before any context is read — satisfying C-20's "named in the step spec before role writing begins" requirement unconditionally; subsequent phases build toward that contract |
| V-04 | phrasing-register + lifecycle-emphasis | C-18 PASS, C-19 PASS, C-20 PASS | R3 V-04 scored approximately 98.75 — the only missing new criterion against v4 is C-20; adding an "Inertia surface" extension field to the Phase 5 registry template closes the gap while preserving all contrastive worked examples (C-18) and multi-item gates (C-19) from the R3 V-04 body |
| V-05 | all four axes | C-18, C-19, C-20 all PASS | Maximum integration: Phase 0 extension contract grounded in Phase 1 (C-20) + two-column BAD/GOOD field guide format (C-18) + 4-item GATE checklists at every phase (C-19) + dedicated inertia specification phase (C-02) + context-first ordering (C-11) + typed dual-failure on collaborates_with (C-14) |

---

## V-01 — Inertia Framing: Dedicated Inertia Specification Phase

**axis:** inertia framing
**hypothesis:** In all R3 variates, the inertia-advocate is one of four stock roles loaded after domain
analysis — it receives less structural attention than domain experts derived from context. This
variate dedicates a full phase (Phase 2) to specifying the status-quo claim and challenge surface
before stock roles are loaded. The Phase 2 output — a named, domain-specific status-quo claim —
becomes the "Inertia surface" extension field in the Phase 6 registry summary. This grounds C-20 in
an earlier step output by construction: the extension field is the Phase 2 INERTIA-SURFACE block's
status-quo claim, and it is named in the Phase 6 output template before any role file is written
in Phase 5. Each domain expert must include an inertia-response question that directly falsifies
the Phase 2 status-quo claim for their concern area. Multi-item GATE checklists (3+ items per
phase) achieve C-19. Contrastive worked examples in three field annotations achieve C-18.
Falsifiable: if inertia-advocate verify_questions still default to generic skepticism despite the
dedicated Phase 2 specification, domain-specific inertia framing is a content-depth problem that
structural phase separation alone cannot solve.

---

You are running `/org-roles {topic}`.

---

PHASE 1 -- CONTEXT ANALYSIS (domain experts only -- stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; drawn from actual context, not generic templates):
  1. [concern: specific failure mode, blind spot, or risk unique to this domain]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary -- not "domain-expert" or "expert-1"]
    Concern addressed: [which concern above by number]
    Candidate frame: [one sentence using vocabulary from the concern]
    Candidate verify focus: [what artifact or behavior this expert checks]
    (repeat for each derived expert; at minimum one)
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE -- Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a populated Domain concerns list
2. At least three domain concerns are listed using vocabulary specific to `{topic}`
3. At least one domain expert is derived with name, concern link, candidate frame using domain vocabulary, and verify focus
4. No stock role names (pm, architect, strategy, inertia-advocate) appear in this block

---

PHASE 2 -- INERTIA SPECIFICATION

Before loading stock roles, use Phase 1 domain concerns to write a domain-specific status-quo claim.
This is the challenge the inertia-advocate will mount. It must argue that the existing approach is
sufficient and that the proposed feature addresses a problem that does not exist or is already
handled.

Write an INERTIA-SURFACE block:

```
INERTIA-SURFACE for {topic}:

Status-quo claim: [one sentence stating what the status quo already does that makes the
  proposed feature redundant -- derived from Phase 1 concerns, not a generic "it works fine"]

Challenge questions (at minimum three; domain-specific, not rhetorical):
  1. Why is the current approach insufficient -- what specific failure does the status quo
     produce that this feature resolves? (Name the failure; do not assume it.)
  2. [domain-specific challenge derived from Phase 1 concern 2]
  3. [domain-specific challenge derived from Phase 1 concern 3]
```

The status-quo claim will be written verbatim into the registry summary as the "Inertia surface"
extension field. It must be a complete sentence derived from Phase 1 domain concerns.

GATE -- Phase 2 complete when ALL of the following are TRUE:
1. INERTIA-SURFACE block is written
2. Status-quo claim is a complete sentence using vocabulary from Phase 1 domain concerns (not a
   generic "the current approach is sufficient")
3. At least three challenge questions are listed, each referencing a specific Phase 1 concern

---

PHASE 3 -- STOCK ROLES

After Phase 2 GATE passes, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate (verify_questions sourced from Phase 2 INERTIA-SURFACE challenge questions)
```

The inertia-advocate's role file (written in Phase 5) must use Phase 2's challenge questions as its
verify_questions. Its orientation.frame must describe the challenge posture using the status-quo
claim from Phase 2, not a generic "challenges every proposal."

GATE -- Phase 3 complete when ALL of the following are TRUE:
1. STOCK-ROLES block lists all four names
2. inertia-advocate is listed
3. Phase 2 INERTIA-SURFACE block is available as the source for inertia-advocate verify_questions

---

PHASE 4 -- OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .roles/{area}/
```

GATE -- Phase 4 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug uses domain-specific vocabulary derived from `{topic}` (not `default`, `generic`, `roles`)
3. Path format is exactly `.roles/{area}/`

---

PHASE 5 -- WRITE ROLE FILES

Write one `.md` file per role to `.roles/{area}/`. Write domain-expert roles first (Phase 1),
then stock roles (Phase 3). For the inertia-advocate, source verify_questions from Phase 2.

Use this template for every file. Read the FAILURE MODE and paired examples for annotated fields
before filling them in:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement -- how this role sees work in this domain. Must be phrased as
    an epistemic viewpoint. Domain experts must use vocabulary from their Phase 1 candidate
    frame. Inertia-advocate must use the Phase 2 status-quo claim as its perspective anchor.}

    FAILURE MODE: task list -- frame becomes a job description rather than an epistemic viewpoint.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec artifacts and ensuring requirements
    are captured before engineering handoff."
    WORKED EXAMPLE (good): "Sees every draft spec through the question of whether the stated
    requirements will survive contact with the actual system boundary -- looking for the gap
    between what the spec assumes and what the system enforces."

  serves: |
    {Beneficiary statement -- who depends on this role's perspective and what they receive.
    Must name a beneficiary, not restate frame.}

    FAILURE MODE: frame restatement -- serves carries the same information as frame in different words.
    WORKED EXAMPLE (bad):  "Ensures spec artifacts are evaluated through a boundary-correctness lens
    to identify system constraint mismatches." (same idea as frame, different words -- zero new signal)
    WORKED EXAMPLE (good): "Engineers who receive the spec as a handoff artifact -- they get a
    boundary-gap verdict before the artifact becomes load-bearing in the implementation."

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact, running code, or inspecting a
       measurable outcome. References a specific artifact type, behavior, or outcome.}"
    - "{Second question unique to this role's frame -- no other role in this registry would
       prioritize this question first.}"
    - "{Domain experts only: inertia-response question that directly falsifies the Phase 2
       status-quo claim for this role's concern. Form: 'What artifact evidence shows that
       [Phase 2 status-quo claim as it applies to this concern] is wrong?'}"

  simplify_rules:
    - "{Opinionated constraint -- a prohibition or elimination that reduces scope.
       'Remove X if Y' or 'Do not include Z unless W'.}"

    FAILURE MODE: scope description masquerading as a constraint -- rule describes priority without removing anything.
    WORKED EXAMPLE (bad):  "Focus on boundary correctness and constraint-gap concerns relevant to this role."
    (names a priority area -- does not exclude or constrain anything)
    WORKED EXAMPLE (good): "Remove any verify question that cannot be answered by reading an artifact or
    running a command -- exclude questions that require a stakeholder interview to answer."

expertise:
  depth: |
    {Specific methods, techniques, or frameworks this role applies. Name things a practitioner
    would recognize -- not just a domain label.}

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow. Stock roles: broader.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # Every listed name must exist in the full role set from Phases 1 and 3.
  # FAILURE MODE (type 1): phantom role -- a name not present in the output role set.
  #   Phantom names silently break downstream skills that resolve collaboration links by name.
  # FAILURE MODE (type 2): universalist listing -- "collaborates with all roles" or listing
  #   every role in the registry. List only two to four roles with a genuine handoff or dependency.
---
```

GATE -- Phase 5 complete when ALL of the following are TRUE:
1. One `.md` file exists per role at `.roles/{area}/`
2. Every file has all six top-level fields with required sub-fields (`orientation.frame`,
   `orientation.serves`, `lens.verify_questions` with 2+ items, `lens.simplify_rules`,
   `expertise.depth`, `expertise.relevance`)
3. No `orientation.frame` field contains a task list or job description
4. No `orientation.serves` field restates `orientation.frame`
5. Every `simplify_rules` entry is phrased as a prohibition or elimination, not a scope description
6. Every domain expert file contains an inertia-response question that references the Phase 2
   status-quo claim
7. No `collaborates_with` entry names a role absent from the full role set (Phases 1 + 3)

---

PHASE 6 -- REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` using this template. Fill every slot. The "Inertia surface"
field below is the domain extension field -- copy the status-quo claim from Phase 2 verbatim:

```
---
area: {area}
total_roles: {N}
date: {date}
---

# Role Registry -- {area}

**Area:** {area}
**Total roles:** {N}
**Stock roles:** pm, architect, strategy, inertia-advocate
**Domain experts:**
  - {name}: derived from concern "{concern}" (Phase 1 DOMAIN-ANALYSIS);
    inertia-response question targets: "{Phase 2 status-quo claim as it applies to this expert}"
  - (repeat for each domain expert)
**Coverage gaps:** {any Phase 1 concern not addressed by any role, or "none detected"}
**Inertia surface:** {the status-quo claim from Phase 2 INERTIA-SURFACE -- one complete sentence}
```

FAILURE MODE: heading-only stub -- a section header with no required content beneath it is not
a complete registry entry and fails C-10 unconditionally.

GATE -- Phase 6 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. All five required fields are present and non-empty: area, total_roles, stock roles, domain
   experts with Phase 1 derivation source, coverage gaps
3. "Inertia surface" extension field is present with the Phase 2 status-quo claim as its value
4. `total_roles` count matches the actual number of role files written in Phase 5
5. The last line is: `Generated by: /org-roles {topic} -- {date}` with actual values

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} -- {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-02 -- Output Format: Standalone Field Guide with BAD/GOOD Pairs

**axis:** output format
**hypothesis:** In R3 variates, contrastive worked examples are embedded inside the YAML code
block as annotation text after each field. This forces the model to context-switch between
"reading a template slot" and "reading a calibration example" within the same code block. This
variate separates the role file template (structure only -- field names and content specs, no
examples) from a standalone FIELD GUIDE that presents every annotated constraint as a compact
BAD/GOOD pair in prose outside the YAML block. The model reads the template for structure, then
reads the Field Guide for calibration before writing. This separation makes contrastive pairs the
unit of instruction rather than an annotation on a positive requirement. C-18 is maximized by
including BAD/GOOD pairs for four fields (frame, serves, simplify_rules, collaborates_with phantom,
collaborates_with universalist). A domain extension field in the registry template achieves C-20.
Multi-item GATE checklists achieve C-19. Falsifiable: if the two-document approach (template +
field guide) causes the model to consult the template but not the field guide at write time, the
format separation degrades calibration rather than improving it.

---

You are running `/org-roles {topic}`.

---

PHASE 1 -- CONTEXT ANALYSIS (domain experts only -- stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; drawn from actual context, not generic):
  1. [concern: specific failure mode, blind spot, or risk unique to this domain]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary -- not "domain-expert"]
    Concern addressed: [which concern above by number]
    Candidate frame: [one sentence using vocabulary from this domain's concerns]
    Candidate verify focus: [what artifact or behavior this expert checks]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE -- Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written
2. At least three domain concerns are present, each using vocabulary specific to `{topic}`
3. At least one domain expert is derived with name, concern link, and candidate frame using
   domain vocabulary
4. No stock role names appear in this block

---

PHASE 2 -- STOCK ROLES

After Phase 1 GATE passes, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate must include at least one verify question explicitly framed as:
"Why is the current approach insufficient -- what specific failure does the status quo produce
that this feature resolves?"

GATE -- Phase 2 complete when ALL of the following are TRUE:
1. STOCK-ROLES block is written with all four names
2. inertia-advocate is listed
3. The inertia-advocate's status-quo question pattern is confirmed

---

PHASE 3 -- OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .roles/{area}/
```

GATE -- Phase 3 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug is domain-specific (not `default`, `generic`, or `roles`)
3. Full path is `.roles/{area}/`

---

PHASE 4 -- WRITE ROLE FILES

STEP A -- Read the FIELD GUIDE below before writing any file.
STEP B -- Write one `.md` file per role using the ROLE FILE TEMPLATE below.
         Domain-expert roles first (Phase 1), then stock roles (Phase 2).

---

ROLE FILE TEMPLATE

Fill every slot. Leave no field empty. Use exact field names (`verify_questions`,
`simplify_rules`) -- downstream skills read these by name.

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement -- how this role sees work in this domain.
    Domain experts: use vocabulary from Phase 1 candidate frame.}

  serves: |
    {Beneficiary statement -- who depends on this role's perspective and what they receive.}

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact or running code.}"
    - "{Second question unique to this role's frame.}"

  simplify_rules:
    - "{Opinionated constraint -- a prohibition or elimination that reduces scope.}"

expertise:
  depth: |
    {Specific methods, techniques, or frameworks -- not a domain label only.}

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
---
```

---

FIELD GUIDE (read this before writing any field; each entry shows both the failure form and the
correct form for the same field)

orientation.frame
  FAILURE MODE: task list -- frame describes what the role does, not how it sees.
  BAD:  "Responsible for reviewing spec artifacts and ensuring quality before engineering
         handoff." -- this is a job description; replace the role name and it still makes sense.
  GOOD: "Sees every spec artifact through the question of whether stated requirements will
         survive contact with the actual system boundary -- looking for the gap between what
         the spec assumes and what the system will enforce."

orientation.serves
  FAILURE MODE: frame restatement -- serves paraphrases frame in different words.
  BAD:  "Ensures spec artifacts are evaluated through a boundary-correctness lens." -- same
         idea as frame; the caller learns nothing new by reading serves separately.
  GOOD: "Teams deciding whether a spec is safe to hand to engineering -- they receive a
         boundary-gap verdict before the artifact becomes load-bearing."

lens.simplify_rules
  FAILURE MODE: scope description -- rule describes what to prioritize, not what to remove.
  BAD:  "Focus on boundary correctness and spec-system gap concerns." -- names a priority
         but does not exclude or constrain anything; the scope is not smaller after reading this.
  GOOD: "Remove any verify question that cannot be answered by reading an artifact or running
         a command -- exclude questions requiring a stakeholder interview to answer."

collaborates_with (phantom role)
  FAILURE MODE (type 1): phantom role -- a name not present in the output role set.
  BAD:  "- signal:data-quality-monitor"  -- not derived in Phase 1 and not in Phase 2 STOCK-ROLES;
         downstream skills that resolve collaboration links by name will silently fail.
  GOOD: "- signal:pm"  -- pm is in STOCK-ROLES from Phase 2; the link resolves.

collaborates_with (universalist listing)
  FAILURE MODE (type 2): universalist listing -- every role in the registry is listed.
  BAD:  "- signal:pm\n  - signal:architect\n  - signal:strategy\n  - signal:inertia-advocate\n
         - signal:signal-fidelity-analyst"  -- every role listed; no structural information.
  GOOD: "- signal:pm\n  - signal:architect"  -- two roles with a genuine handoff dependency.

---

GATE -- Phase 4 complete when ALL of the following are TRUE:
1. One `.md` file exists per role at `.roles/{area}/`
2. Every file has all six top-level fields with required sub-fields
3. No `orientation.frame` field could be mistaken for a task list or job description
4. No `orientation.serves` field restates `orientation.frame`
5. Every `simplify_rules` entry is a prohibition or elimination, not a scope description
6. No `collaborates_with` entry names a role absent from the full role set
7. No `collaborates_with` lists every role in the registry

---

PHASE 5 -- REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` using this template. Fill every slot. The "Domain risk
anchor" field below is the registry's domain extension field -- derive its value from the highest-
risk Phase 1 concern:

```
---
area: {area}
total_roles: {N}
date: {date}
---

# Role Registry -- {area}

**Area:** {area}
**Total roles:** {N}
**Stock roles:** pm, architect, strategy, inertia-advocate
**Domain experts:**
  - {name}: derived from concern "{concern}" (Phase 1 DOMAIN-ANALYSIS)
  - (repeat for each domain expert)
**Coverage gaps:** {any Phase 1 concern not addressed by any role, or "none detected"}
**Domain risk anchor:** {the highest-risk domain concern from Phase 1 -- one complete sentence
  stating the failure mode this registry is designed to catch}
```

FAILURE MODE: heading-only stub -- a section header with no required content beneath it is not
a complete registry entry and fails C-10 unconditionally. The heading `# Role Registry` is
structural scaffolding; all seven fields above are the content.

GATE -- Phase 5 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. All five required fields are present and non-empty (area, total_roles, stock roles, domain
   experts with derivation source, coverage gaps)
3. "Domain risk anchor" extension field is present with a complete sentence derived from Phase 1
4. `total_roles` count matches the actual number of role files written in Phase 4
5. The last line is: `Generated by: /org-roles {topic} -- {date}` with actual values

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} -- {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-03 -- Lifecycle Emphasis: Phase 0 Extension Contract

**axis:** lifecycle-emphasis
**hypothesis:** C-20 requires that the domain extension field be "named in the step spec before
role writing begins." All R3 variates defined the extension field (if at all) inside Phase 5 or
Phase 6 -- after domain expert roles were already written in Phase 4 or Phase 5. This variate
resolves the ambiguity by adding a Phase 0 Extension Contract step that commits to a named
extension field slot before any context is read. The field name is drawn from a fixed set of
domain-extension candidates; its value is derived in Phase 1 and written into the Phase 6
registry template. Because Phase 0 runs before Phase 1 (domain analysis), the extension field is
unconditionally named before role writing begins, satisfying C-20 by construction. Each subsequent
phase ends with a numbered GATE checklist with 4+ independently verifiable items (C-19).
Contrastive worked examples in three field annotations achieve C-18. Falsifiable: if the Phase 0
commitment is disconnected from Phase 1 content (the model picks a field name in Phase 0 but fills
it with generic content in Phase 6), the commitment is nominal and does not demonstrate that the
extension reaches into the domain.

---

You are running `/org-roles {topic}`.

---

PHASE 0 -- EXTENSION CONTRACT

Before reading context, commit to the domain extension field that the registry will include beyond
the five required fields. Choose one field name from the candidates below; the value will be filled
from Phase 1 domain analysis.

Extension field candidates (choose the most relevant to `{topic}`, or derive one in domain vocabulary):
- "Inertia surface" -- the status-quo claim the registry must falsify
- "Primary failure mode" -- the highest-severity domain risk surfaced by Phase 1
- "Evidence gap" -- the most critical concern not covered by any derived expert
- Or: [derive a field name from `{topic}` vocabulary -- must not duplicate any required field]

Write:

```
EXTENSION-COMMITMENT:
  Field name: [chosen field name]
  Will be populated from: Phase 1 DOMAIN-ANALYSIS [concern number or section]
  Purpose: [one sentence stating what this field tells the caller that no required field does]
```

GATE -- Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT block is written
2. Field name is one of the candidates above or uses domain vocabulary from `{topic}`
3. Field name does not duplicate any required field (area, total_roles, stock roles, domain
   experts, coverage gaps)
4. "Will be populated from" names a Phase 1 section, not a post-Phase-5 artifact

---

PHASE 1 -- CONTEXT ANALYSIS (domain experts only -- stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block. Include the content that
will populate the Phase 0 extension field:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; drawn from actual context, not generic):
  1. [concern: specific failure mode, blind spot, or risk unique to this domain]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary -- not "domain-expert"]
    Concern addressed: [which concern above by number]
    Candidate frame: [one sentence using vocabulary from that concern]
    Candidate verify focus: [what artifact or behavior this expert checks]

Extension field value: [content for the Phase 0 committed field -- derived from the
  concern or concern synthesis above; one complete sentence]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE -- Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written with a Domain concerns list
2. At least three domain concerns are listed using vocabulary specific to `{topic}`
3. At least one domain expert is derived with name, concern link, and candidate frame
4. "Extension field value" entry is present with a complete sentence
5. No stock role names appear in this block

---

PHASE 2 -- STOCK ROLES

Add the four stock roles after Phase 1 GATE passes:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate must include at least one verify question explicitly framed as:
"Why is the current approach insufficient -- what specific failure does the status quo produce
that this feature resolves?"

GATE -- Phase 2 complete when ALL of the following are TRUE:
1. STOCK-ROLES block is written with all four names
2. inertia-advocate is listed
3. inertia-advocate's status-quo question pattern is confirmed
4. No new domain experts are introduced in this phase

---

PHASE 3 -- OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .roles/{area}/
```

Area must be a domain-specific slug (not `default`, `generic`, or `roles`).

GATE -- Phase 3 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug uses domain vocabulary (not a generic placeholder)
3. Full path is `.roles/{area}/`

---

PHASE 4 -- WRITE ROLE FILES

Write one `.md` file per role to `.roles/{area}/`. Domain-expert roles first (Phase 1),
then stock roles (Phase 2).

Use this template for every file. Read each FAILURE MODE and paired example before filling
the annotated fields:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement -- how this role sees work in this domain. Domain experts must
    use vocabulary from their Phase 1 candidate frame. Must be an epistemic viewpoint.}

    FAILURE MODE: task list -- frame describes the role's duties rather than its viewpoint.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec artifacts and ensuring all
    requirements are captured before engineering handoff."
    WORKED EXAMPLE (good): "Sees every spec artifact through the question of whether the
    stated requirements will survive contact with the actual system boundary -- looking for
    the gap between what the spec assumes and what the system enforces."

  serves: |
    {Beneficiary statement -- who depends on this role's perspective and what they receive.
    Must not restate frame.}

    FAILURE MODE: frame restatement -- serves paraphrases frame in different words.
    WORKED EXAMPLE (bad):  "Ensures spec artifacts are evaluated through a boundary-correctness
    lens to identify constraint mismatches." (same information as frame; zero additional signal)
    WORKED EXAMPLE (good): "Teams deciding whether a spec is safe to hand to engineering --
    they receive a boundary-gap verdict before the artifact becomes load-bearing."

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact or running code.}"
    - "{Second question unique to this role's frame.}"

  simplify_rules:
    - "{Opinionated constraint -- a prohibition or elimination that reduces scope.}"

    FAILURE MODE: scope description masquerading as a constraint.
    WORKED EXAMPLE (bad):  "Focus on boundary correctness and constraint-gap concerns."
    (names a priority -- does not remove or constrain anything)
    WORKED EXAMPLE (good): "Remove any verify question that cannot be answered by reading an
    artifact or running a command -- exclude questions that require a stakeholder meeting."

expertise:
  depth: |
    {Specific methods, techniques, or frameworks. Not a domain label only.}

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # FAILURE MODE (type 1): phantom role -- a name not in the output role set.
  # FAILURE MODE (type 2): universalist listing -- do not list every role in the registry.
  #   List two to four roles with a genuine handoff or dependency.
---
```

GATE -- Phase 4 complete when ALL of the following are TRUE:
1. One `.md` file exists per role at `.roles/{area}/`
2. Every file has all six top-level fields with required sub-fields
3. No `orientation.frame` contains a task list or job description
4. No `orientation.serves` restates `orientation.frame`
5. Every `simplify_rules` entry is a prohibition or elimination
6. No `collaborates_with` entry names a role absent from the full role set (phantom prohibition)
7. No `collaborates_with` lists every role (universalist prohibition)

---

PHASE 5 -- REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` using this template. The extension field below uses the
Phase 0 committed field name and the Phase 1 extension field value:

```
---
area: {area}
total_roles: {N}
date: {date}
---

# Role Registry -- {area}

**Area:** {area}
**Total roles:** {N}
**Stock roles:** pm, architect, strategy, inertia-advocate
**Domain experts:**
  - {name}: derived from concern "{concern}" (Phase 1 DOMAIN-ANALYSIS)
  - (repeat for each domain expert)
**Coverage gaps:** {any Phase 1 concern not addressed by any role, or "none detected"}
**{Phase 0 committed field name}:** {Phase 1 extension field value -- one complete sentence}
```

FAILURE MODE: heading-only stub -- a section header with no required content beneath it fails
C-10 unconditionally. The heading is structural scaffolding; all six fields (five required plus
the Phase 0 extension) are the content.

GATE -- Phase 5 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. All five required fields are present and non-empty
3. Extension field (from Phase 0 commitment) is present with Phase 1 derived value
4. Extension field name matches the Phase 0 EXTENSION-COMMITMENT exactly
5. `total_roles` count matches actual role file count from Phase 4
6. Last line is: `Generated by: /org-roles {topic} -- {date}` with actual values

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} -- {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-04 -- Combined: Phrasing Register + Lifecycle Emphasis (R3 V-04 + C-20 Fix)

**axes:** phrasing-register + lifecycle-emphasis
**hypothesis:** R3 V-04 scored approximately 98.75 against v4 rubric -- the highest of all R3
variates. Its gaps against v4 are: C-20 UNKNOWN (registry template had no extension field). This
variate preserves R3 V-04's full body (contrastive worked examples on four fields, multi-item GATE
checklists at every phase, inertia-response questions per domain expert, typed dual-failure labels
on collaborates_with, heading-stub failure mode named) and adds exactly one structural change: the
Phase 5 registry template gains an "Inertia surface" extension field derived from Phase 1's inertia
objection content. This field is grounded in Phase 1 (where each domain expert records the inertia
objection their concern must pre-answer), satisfying C-20's requirement that the extension field
reference a concern identified in the context/domain analysis step. Falsifiable: if C-20 cannot be
satisfied by adding the extension field to the Phase 5 template alone (because the rubric requires
it to be "named before role writing begins"), a Phase 0 commitment step is needed -- at which point
V-03 or V-05 becomes the appropriate variate.

---

You are running `/org-roles {topic}`.

**Design contract:** This registry will be used by downstream skills (org-review, org-chart,
org-committee) that read role files by exact field name. Field name errors, phantom collaboration
references, and empty fields silently break downstream integration. Complete every slot. Apply
every constraint before writing.

---

PHASE 1 -- CONTEXT ANALYSIS (domain experts only -- stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; drawn from actual context -- not generic):
  1. [concern: specific failure mode, blind spot, or risk unique to this domain]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary -- not "domain-expert" or "expert-1"]
    Concern addressed: [which concern above by number]
    Candidate frame: [one sentence using vocabulary from that concern]
    Candidate verify focus: [artifact or behavior this expert checks]
    Inertia objection this expert must pre-answer: [what the devil-advocate would say to claim
      this concern is already handled adequately by the status quo]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE -- Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written
2. At least three domain concerns are listed using vocabulary specific to `{topic}`
3. At least one domain expert is derived with name, concern link, candidate frame using domain
   vocabulary, and inertia objection
4. No stock role names appear in this block

---

PHASE 2 -- STOCK ROLES

After Phase 1 GATE passes, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate's lens must include at least one verify question explicitly framed as:
"Why is the current approach insufficient -- what specific failure does the status quo produce
that this feature resolves?"

GATE -- Phase 2 complete when ALL of the following are TRUE:
1. STOCK-ROLES block lists all four names
2. inertia-advocate is listed
3. inertia-advocate's status-quo question pattern is confirmed

---

PHASE 3 -- OUTPUT AREA

Derive the area slug from `{topic}`. Write:

```
OUTPUT-AREA: .roles/{area}/
```

Area must be a domain-specific slug (not `default`, `generic`, or `roles`).

GATE -- Phase 3 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug is domain-specific and derived from `{topic}` context
3. Path follows the `.roles/{area}/` format

---

PHASE 4 -- WRITE ROLE FILES

Write one `.md` file per role to `.roles/{area}/`. Domain-expert roles first (Phase 1),
then stock roles (Phase 2).

Use this template for every file. For annotated fields, read the FAILURE MODE and WORKED
EXAMPLE pair before writing:

```yaml
---
name: {role-name}
  # Required. Lowercase slug. Domain experts: use domain vocabulary.
  # FAILURE MODE: generic label -- "domain-expert", "expert-1", "reviewer".
  # If the name could apply to any product domain unchanged, it is too generic.

version: "1.0"

archetype: {product | technical | business | challenger | domain-specific-label}
  # Required. Choose one. Failure: omitting archetype breaks downstream role filtering.

orientation:
  frame: |
    {Perspective statement -- how this role sees work in this domain. Domain experts must
    use vocabulary from Phase 1 candidate frame.}

    FAILURE MODE: task list -- frame becomes a job description rather than an epistemic viewpoint.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec completeness and ensuring all
    requirements are captured before engineering handoff."
    WORKED EXAMPLE (good): "Sees every draft spec artifact through the question of whether the
    requirements written will survive contact with actual system constraints -- looking for the
    gap between what authors assumed and what the system will enforce."

  serves: |
    {Beneficiary statement -- names who depends on this role's perspective and what they receive.
    Must not restate frame.}

    FAILURE MODE: frame restatement -- serves carries the same information as frame in different words.
    WORKED EXAMPLE (bad):  "Ensures that draft specs are evaluated through a constraint-gap lens
    to identify system boundary mismatches." (same idea as frame; zero additional signal)
    WORKED EXAMPLE (good): "Engineers who receive the spec as a handoff artifact -- they get a
    boundary-gap verdict that tells them which assumptions need to be negotiated before coding."

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact, running code, or inspecting a
       measurable outcome. References a specific artifact type, behavior, or outcome.}"
    - "{Second question unique to this role's frame -- no other role in this registry would
       prioritize this question first.}"
    - "{For domain experts only: inertia-response question -- pre-answers the Phase 1 inertia
       objection for this role's concern. Form: 'What artifact evidence shows that [inertia
       objection] is wrong -- which artifact, which field, which measurable outcome?'}"
    # FAILURE MODE (type 1): rhetorical question -- "Is the design appropriate?" cannot be
    #   answered by reading an artifact; it provides no review guidance.
    # FAILURE MODE (type 2): universal question -- "Does the spec cover edge cases?" every role
    #   could ask this; it does not belong to any specific role's frame.

  simplify_rules:
    - "{Opinionated constraint -- a prohibition or elimination that reduces scope.
       'Remove X if Y' or 'Do not include Z unless W'. Not a description of good practice.}"

    FAILURE MODE: scope description masquerading as a constraint.
    WORKED EXAMPLE (bad):  "Focus on constraint-gap and system-boundary concerns relevant
    to this role." (describes priority -- does not remove or constrain anything)
    WORKED EXAMPLE (good): "Remove any verify question that cannot be answered by reading
    an artifact or running a command -- exclude questions that require a stakeholder interview
    or meeting to answer."

expertise:
  depth: |
    {Specific methods, techniques, or frameworks this role applies. Name things a practitioner
    would recognize -- not just a domain label.}

    FAILURE MODE: label without method -- "security expertise" names a domain but not a technique.
    Name the method: "threat modeling, attack surface enumeration, auth boundary verification."

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow. Stock roles: broader.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # Required. Every listed name must exist in the full role set from Phases 1-2.
  # List two to four roles with a genuine handoff or dependency.
  #
  # FAILURE MODE (type 1): phantom role -- a name not present in the output role set.
  #   Phantom names silently break downstream skills that resolve collaboration links by name.
  #   WORKED EXAMPLE (bad):  "- signal:data-quality-monitor" (role not in the output set)
  #   WORKED EXAMPLE (good): "- signal:pm" (pm is in STOCK-ROLES from Phase 2)
  #
  # FAILURE MODE (type 2): universalist listing -- "collaborates with all roles" or listing
  #   every role in the registry. A universalist entry carries no structural information and
  #   breaks directed graph reasoning over collaborations.
  #   WORKED EXAMPLE (bad):  every role in the registry listed under one collaborates_with
  #   WORKED EXAMPLE (good): two to four roles with a named handoff or dependency reason
---
```

GATE -- Phase 4 complete when ALL of the following are TRUE:
1. One file per role exists at `.roles/{area}/`
2. Every file has all six top-level fields with required sub-fields
3. Every field uses exact names: `verify_questions` (not `verify`), `simplify_rules` (not `simplify`)
4. No `orientation.frame` contains a task list or job description
5. No `orientation.serves` restates `orientation.frame`
6. Every `simplify_rules` entry is a prohibition or elimination, not a scope description
7. Every `expertise.depth` names a method or technique, not a domain label only
8. No `collaborates_with` entry names a role absent from the full role set (no phantom names)
9. No `collaborates_with` lists every role in the set (no universalist entries)
10. Every domain expert has at least one inertia-response question in verify_questions

---

PHASE 5 -- REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` using this template. Fill every slot. The "Inertia
surface" field below is the domain extension field -- its value is the synthesis of the inertia
objections recorded in Phase 1 for the derived domain experts:

```
---
area: {area}
total_roles: {N}
date: {date}
---

# Role Registry -- {area}

**Area:** {area}
**Total roles:** {N}
**Stock roles:** pm, architect, strategy, inertia-advocate
**Domain experts:**
  - {name}: derived from concern "{concern}" (Phase 1 DOMAIN-ANALYSIS);
    inertia objection pre-answered: "{inertia objection from Phase 1 for this expert}"
  - (repeat for each domain expert)
**Coverage gaps:** {concerns from Phase 1 not fully addressed by any role, or "none detected"}
**Inertia surface:** {one sentence synthesizing the status-quo claim the registry must falsify --
  derived from Phase 1 inertia objections; states what the status quo supposedly already handles
  that makes the proposed feature appear unnecessary}
```

FAILURE MODE (C-15): heading-only stub -- a section header (`## Registry Summary`) with no
required content beneath it is not a complete registry entry and fails C-10 unconditionally.
The heading is structural scaffolding; all six fields (five required plus "Inertia surface")
are the content. A registry that contains only headings provides no audit information to the caller.

GATE -- Phase 5 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. `area` field is present and non-empty
3. `total_roles` count matches the actual number of role files written in Phase 4
4. Stock roles section lists all four names: pm, architect, strategy, inertia-advocate
5. Domain experts section names each expert with its Phase 1 derivation source and inertia objection
6. Coverage gaps field is present with a non-empty value (even if "none detected")
7. "Inertia surface" extension field is present and contains a complete sentence derived from
   Phase 1 inertia objection content

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} -- {date}
```

Replace `{topic}` and `{date}` with actual values. Do not emit literal placeholder text.

---

## V-05 -- Combined: All Four Axes

**axes:** phrasing-register + lifecycle-emphasis + inertia framing + output format
**hypothesis:** Each new v4 criterion requires a different structural intervention: C-18 requires
contrastive examples in field annotations (phrasing-register), C-19 requires multi-item GATE
checklists (lifecycle-emphasis), C-20 requires the extension field to be named before role writing
begins (lifecycle-emphasis + inertia framing via the inertia surface as extension). No single-axis
variate in R4 achieves all three simultaneously at maximum strength. V-04 is the strongest
combination for C-18 and C-19 (inherited from R3 V-04) but relies on Phase 1 inertia objections
to ground C-20 after the fact. This variate adds a Phase 0 Extension Contract (from V-03) to V-04's
full body, plus the two-column BAD/GOOD format for the FIELD GUIDE (from V-02) applied to
`collaborates_with`. The combination provides: Phase 0 unconditional C-20 grounding, four-field
contrastive examples for C-18, 4+ item GATE checklists for C-19, typed dual-failure labels for
C-14, heading-stub failure mode for C-15, inertia-response questions for C-02 quality, and
context-first ordering for C-11. Falsifiable: if the Phase 0 extension field (committed before
Phase 1) cannot incorporate Phase 1 domain vocabulary (because the field name is set before
context is read), the Phase 0 commitment produces a generic extension rather than a
domain-grounded one -- and C-20 requires domain grounding.

---

You are running `/org-roles {topic}`.

**Design contract:** This registry will be used by downstream skills (org-review, org-chart,
org-committee) that read role files by exact field name. Field name errors, phantom collaboration
references, and empty fields silently break downstream integration. Complete every slot. Apply
every constraint before writing.

---

PHASE 0 -- EXTENSION CONTRACT

Before reading context, commit to the extension field that the registry will include. Choose one
from the candidates; its value will be derived from Phase 1:

Extension field candidates:
- "Inertia surface" -- the status-quo claim the registry must falsify (recommended for most domains)
- "Primary failure mode" -- the highest-severity domain risk from Phase 1 analysis
- "Domain evidence gap" -- the concern from Phase 1 not addressed by any derived expert
- Or: derive a field name using `{topic}` vocabulary (must not duplicate the five required fields)

Write:

```
EXTENSION-COMMITMENT:
  Field name: [chosen field name]
  Will be populated from: Phase 1 DOMAIN-ANALYSIS [specify which section: concern list /
    derived expert inertia objections / coverage gaps]
  Purpose: [one sentence stating what this field tells the caller that no required field captures]
```

GATE -- Phase 0 complete when ALL of the following are TRUE:
1. EXTENSION-COMMITMENT block is written
2. Field name does not duplicate any required field (area, total_roles, stock roles, domain
   experts, coverage gaps)
3. "Will be populated from" names a Phase 1 section or concern number
4. "Purpose" is a complete sentence that could not apply to any of the five required fields

---

PHASE 1 -- CONTEXT ANALYSIS (domain experts only -- stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block. Populate the "Extension
field value" entry using the Phase 0 commitment:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; drawn from actual context -- not generic):
  1. [concern: specific failure mode, blind spot, or risk unique to this domain]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary -- not "domain-expert" or "expert-1"]
    Concern addressed: [which concern above by number]
    Candidate frame: [one sentence using vocabulary from that concern]
    Candidate verify focus: [artifact or behavior this expert checks]
    Inertia objection this expert must pre-answer: [what the devil-advocate would say to
      claim this concern is already handled adequately by the status quo]

Extension field value ({Phase 0 committed field name}): [one complete sentence derived from
  the domain concerns or inertia objections above -- grounds the Phase 0 commitment in this
  domain's actual analysis]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE -- Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written
2. At least three domain concerns are present using vocabulary specific to `{topic}`
3. At least one domain expert is derived with name, concern link, candidate frame, and inertia objection
4. Extension field value is present as a complete sentence grounded in Phase 1 domain concerns
5. No stock role names appear in this block

---

PHASE 2 -- STOCK ROLES

After Phase 1 GATE passes, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate's lens must include at least one verify question explicitly framed as:
"Why is the current approach insufficient -- what specific failure does the status quo produce
that this feature resolves?"

GATE -- Phase 2 complete when ALL of the following are TRUE:
1. STOCK-ROLES block lists all four names
2. inertia-advocate is listed
3. inertia-advocate's status-quo question pattern is confirmed
4. No new domain experts are introduced in Phase 2

---

PHASE 3 -- OUTPUT AREA

Derive the area slug from `{topic}`. Write:

```
OUTPUT-AREA: .roles/{area}/
```

Area must be a domain-specific slug (not `default`, `generic`, or `roles`).

GATE -- Phase 3 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug is domain-specific and derived from `{topic}` context
3. Path follows the `.roles/{area}/` format

---

PHASE 4 -- WRITE ROLE FILES

STEP A -- Read the FIELD GUIDE below before writing any file.
STEP B -- Write one `.md` file per role. Domain-expert roles first (Phase 1), then stock
          roles (Phase 2).

---

ROLE FILE TEMPLATE

Fill every slot. Use exact field names (`verify_questions`, `simplify_rules`).

```yaml
---
name: {role-name}
  # Lowercase slug using domain vocabulary. Not "domain-expert", "expert-1", "reviewer".

version: "1.0"

archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement -- how this role sees work in this domain. Domain experts must
    use vocabulary from Phase 1 candidate frame.}

    FAILURE MODE: task list -- frame describes duties, not an epistemic viewpoint.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec completeness and ensuring all
    requirements are captured before engineering handoff."
    WORKED EXAMPLE (good): "Sees every draft spec artifact through the question of whether the
    requirements written will survive contact with actual system constraints -- looking for the
    gap between what authors assumed and what the system will enforce."

  serves: |
    {Beneficiary statement -- who depends on this role's perspective and what they receive.
    Must not restate frame.}

    FAILURE MODE: frame restatement -- serves paraphrases frame in different words.
    WORKED EXAMPLE (bad):  "Ensures draft specs are evaluated through a constraint-gap lens
    to identify system boundary mismatches." (same idea as frame; no new information)
    WORKED EXAMPLE (good): "Engineers who receive the spec as a handoff artifact -- they get
    a boundary-gap verdict that tells them which assumptions need negotiation before coding."

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact, running code, or inspecting a
       measurable outcome.}"
    - "{Second question unique to this role's frame -- no other role would prioritize this first.}"
    - "{Domain experts only: inertia-response question. Form: 'What artifact evidence shows that
       [Phase 1 inertia objection for this role's concern] is wrong?'}"
    # FAILURE MODE (type 1): rhetorical -- "Is the design appropriate?" cannot be answered
    #   by reading an artifact.
    # FAILURE MODE (type 2): universal -- "Does the spec cover edge cases?" every role could
    #   ask this; it does not belong to any specific frame.

  simplify_rules:
    - "{Opinionated constraint -- 'Remove X if Y' or 'Do not include Z unless W'.}"

    FAILURE MODE: scope description masquerading as constraint.
    WORKED EXAMPLE (bad):  "Focus on constraint-gap and system-boundary concerns relevant
    to this role." (names priority -- removes nothing)
    WORKED EXAMPLE (good): "Remove any verify question that cannot be answered by reading an
    artifact or running a command -- exclude questions requiring a stakeholder interview."

expertise:
  depth: |
    {Specific methods, techniques, or frameworks. Not a domain label only.}

    FAILURE MODE: label without method -- "security expertise" names a domain, not a technique.
    WORKED EXAMPLE (bad):  "Security expertise and system boundary knowledge."
    WORKED EXAMPLE (good): "Threat modeling, attack surface enumeration, auth boundary
    verification via contract diff analysis."

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # FAILURE MODE (type 1): phantom role -- a name not present in the output role set.
  # FAILURE MODE (type 2): universalist listing -- every role in the registry is listed.
---
```

---

FIELD GUIDE (supplemental contrastive reference for collaborates_with)

collaborates_with phantom role
  FAILURE MODE (type 1): phantom role -- name not in Phase 1 + Phase 2 role sets.
  BAD:  "- signal:data-quality-monitor"  (not derived in Phase 1, not in Phase 2 STOCK-ROLES)
  GOOD: "- signal:pm"  (pm is in STOCK-ROLES from Phase 2; the link resolves)

collaborates_with universalist listing
  FAILURE MODE (type 2): universalist listing -- every role in the registry is listed.
  BAD:  every role from Phase 1 + Phase 2 listed under one collaborates_with block
  GOOD: two to four roles that share a specific handoff or dependency with this role

---

GATE -- Phase 4 complete when ALL of the following are TRUE:
1. One `.md` file exists per role at `.roles/{area}/`
2. Every file has all six top-level fields with required sub-fields
3. Every field uses exact names: `verify_questions`, `simplify_rules`
4. No `orientation.frame` contains a task list or job description
5. No `orientation.serves` restates `orientation.frame`
6. Every `simplify_rules` entry is a prohibition or elimination, not a scope description
7. Every `expertise.depth` names a method or technique, not a domain label only
8. No `collaborates_with` entry names a role absent from the full role set (no phantom names)
9. No `collaborates_with` lists every role in the registry (no universalist entries)
10. Every domain expert has at least one inertia-response question addressing its Phase 1 inertia objection

---

PHASE 5 -- REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` using this template. The extension field uses the Phase 0
committed name and the Phase 1 derived value:

```
---
area: {area}
total_roles: {N}
date: {date}
---

# Role Registry -- {area}

**Area:** {area}
**Total roles:** {N}
**Stock roles:** pm, architect, strategy, inertia-advocate
**Domain experts:**
  - {name}: derived from concern "{concern}" (Phase 1 DOMAIN-ANALYSIS);
    inertia objection pre-answered: "{Phase 1 inertia objection for this expert}"
  - (repeat for each domain expert)
**Coverage gaps:** {any Phase 1 concern not fully addressed by any role, or "none detected"}
**{Phase 0 committed field name}:** {Phase 1 extension field value -- complete sentence derived
  from domain analysis, not a placeholder}
```

FAILURE MODE (C-15): heading-only stub -- a section header with no required content beneath it
fails C-10 unconditionally. The heading `# Role Registry -- {area}` is structural scaffolding;
all six fields (five required plus Phase 0 extension) are the content.

GATE -- Phase 5 complete when ALL of the following are TRUE:
1. `REGISTRY.md` exists at `.roles/{area}/REGISTRY.md`
2. All five required fields are present and non-empty
3. Phase 0 committed extension field is present with Phase 1 derived value (non-placeholder sentence)
4. Extension field name matches the Phase 0 EXTENSION-COMMITMENT exactly (no renaming)
5. `total_roles` count matches the actual number of role files written in Phase 4
6. Domain experts section includes both derivation source and inertia objection for each expert
7. Last line is: `Generated by: /org-roles {topic} -- {date}` with actual values

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} -- {date}
```

Replace `{topic}` and `{date}` with actual values. Do not emit literal placeholder text.
