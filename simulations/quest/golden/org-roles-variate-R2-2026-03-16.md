---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R2
rubric_version: v2
status: variate
---

# org-roles Variate — Round 2

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v2 (C-01 through C-13; essential C-01–C-05; aspirational additions C-11, C-12, C-13)
**Round:** R2 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 2 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | role-sequence | Context analysis and domain expert derivation are placed in Step 1 as the sole deliverable; stock roles load in Step 2 only after domain experts are named | Structurally enforces C-11 by making it physically impossible for the model to encounter PM/Architect/Strategy archetypes before it has committed to domain-specific concerns in writing — if the ordering constraint holds, domain expert `frame` fields cannot be generic archetypes with domain labels pasted in |
| V-02 | output-format | A fill-in-the-blank file template with every field and sub-field pre-named as a required slot is provided at the step where role files are written | Pre-specifying all six top-level fields plus sub-fields as template slots makes C-01 failures (missing fields) structurally impossible and satisfies C-13 (step defines output format) because the template is the format definition — omission requires active deletion, not passive oversight |
| V-03 | phrasing-register | Every schema field instruction includes a `FAILURE MODE:` line naming the exact collapse pattern to avoid, not just the positive requirement | Directly targets C-12: naming failure modes converts implicit constraints to explicit prohibitions; secondary benefit to C-06 (frame/serves collapse) and C-07 (verify/simplify collapse) because the exact collapse pattern is named — "serves restates frame" is actionably different from "frame and serves must differ" |
| V-04 | role-sequence + output-format | Context-first ordering (V-01) combined with explicit role file template per step (V-02) | Closes the most common essential+aspirational failure cluster: domain expert derivation anchored by context (C-11) AND schema completeness enforced by template (C-01, C-13); the combination removes both ordering and omission failure paths simultaneously |
| V-05 | phrasing-register + lifecycle-emphasis | Explicit four-phase lifecycle with per-phase completion conditions combined with DO/DO NOT failure-mode-named instructions on every schema field | Combines C-12 coverage (negative field constraints throughout schema) with C-13 coverage (every phase names its output and defines its format fields); per-phase completion conditions prevent advancing without the output being structurally correct, not just present |

---

## V-01 — Role Sequence: Context-Analysis-First Domain Expert Derivation

**axis:** role-sequence
**hypothesis:** Placing context analysis and domain expert derivation in Step 1 as the sole deliverable — before any stock role archetype is named — prevents template anchoring at generation time. If the model commits to domain-specific concerns in Step 1 prose before encountering PM/Architect/Strategy in Step 2, domain expert `frame` fields will contain language from the context, not from the stock archetypes. Falsifiable: if domain expert frames remain generic despite the ordering constraint (i.e., they use language that could apply to any domain), the ordering change alone does not defeat the anchoring failure.

---

You are running `/org-roles {topic}`.

---

STEP 1 — CONTEXT ANALYSIS (domain experts only; stock roles not yet loaded)

Read the available context for `{topic}`: product description, spec files, codebase, or any input provided.

Your task in Step 1 is to surface domain-specific concerns — the things that could go wrong or go unnoticed in this domain that a generic reviewer would miss. Write a DOMAIN-CONCERNS block:

```
DOMAIN-CONCERNS for {topic}:
  - [concern 1: name a specific failure mode, artifact risk, or blind spot unique to this domain]
  - [concern 2]
  - [concern 3]
  (list at least three; more if warranted by context)
```

From the domain concerns, derive domain expert roles. Each concern should suggest the kind of expert who would catch it:

```
DOMAIN-EXPERTS-DERIVED:
  - Expert name: [name specific to this domain, not "Domain Expert"]
    Derived from concern: [which concern above]
    Frame (one sentence, written in this domain's vocabulary): [...]
  - (repeat for each derived expert; at minimum one)
```

Do not load PM, Architect, Strategy, or inertia-advocate in this step.
Do not write role files yet.

Step 1 complete when: DOMAIN-CONCERNS block and DOMAIN-EXPERTS-DERIVED block are both written.

---

STEP 2 — LOAD STOCK ROLES

After Step 1 is complete, add the four stock roles that always appear regardless of domain:

```
STOCK-ROLES-LOADED:
  - pm (product manager — go/no-go decisions, commitment thresholds)
  - architect (software/systems architect — technical feasibility, boundary definition)
  - strategy (business/strategic lens — market, positioning, investment sizing)
  - inertia-advocate (devil-advocate — argues the status quo is sufficient; challenges every proposal)
```

The inertia-advocate's `lens.verify_questions` must include at least one question of the form: "Why is the current approach insufficient — what specific failure does the status quo produce that this feature resolves?"

Step 2 complete when: STOCK-ROLES-LOADED block is written with all four entries.

---

STEP 3 — DETERMINE OUTPUT AREA

Derive the area name from `{topic}` context. The area name must:
- Be a short slug (lowercase, hyphen-separated)
- Reflect the actual domain (not `default`, `generic`, or `roles`)
- Match the subdirectory that downstream skills will read

Write: `OUTPUT-AREA: .roles/{area}/`

---

STEP 4 — WRITE ROLE FILES

Write one `.md` file per role to `.roles/{area}/`. Each file must contain all six required fields:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific}

orientation:
  frame: "{epistemic viewpoint — how this role sees the world; must use domain vocabulary from DOMAIN-CONCERNS if this is a derived expert}"
  serves: "{stakeholder or system concern that depends on this role's signal — not a restatement of frame}"

lens:
  verify_questions:
    - "{actionable question answerable by reading an artifact or running code}"
    - "{a second question; both must be specific enough to produce different answers for different artifacts}"
  simplify_rules:
    - "{opinionated constraint that excludes or reduces scope — not a description, a rule}"

expertise:
  depth: "{specific skills and knowledge this role applies}"
  relevance: "{which Signal namespaces or skill types this role appears in}"

scope: workspace
collaborates_with:
  - {area}:{role-name-of-collaborator}
---
```

Write domain-expert roles first (from Step 1 DOMAIN-EXPERTS-DERIVED), then stock roles (from Step 2 STOCK-ROLES-LOADED).

---

STEP 5 — REGISTRY SUMMARY

After all role files are written, emit a `REGISTRY.md` file to `.roles/{area}/REGISTRY.md`:

```
# Role Registry — {area}

Area: {area}
Total roles: {N}
Stock roles: pm, architect, strategy, inertia-advocate
Domain experts: {list each by name with the concern it was derived from}
Coverage gaps: {any domain concern from Step 1 that no role fully covers, or "none detected"}

Generated by: /org-roles {topic} — {date}
```

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} — {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-02 — Output Format: Explicit Role File Template with Required Slots

**axis:** output-format
**hypothesis:** Providing a fill-in-the-blank template at the step where role files are written makes omission of any field structurally visible — the model must actively delete a slot to fail C-01, rather than passively forget it. The template also satisfies C-13 by definition: the step defines the output's exact fields, format, and minimum content in the template structure itself. Falsifiable: if fields are still omitted or left empty despite the template (e.g., `verify_questions: []`), template structure alone does not fix content depth failures — C-07 may still fail even when C-01 passes.

---

You are running `/org-roles {topic}`.

Generate a typed role registry for `{topic}`. Read available context (product description, spec, codebase) to determine which domain expert roles are needed. Always include PM, Architect, Strategy, and inertia-advocate.

---

STEP 1 — READ CONTEXT AND DERIVE ROLES

Read the available context for `{topic}`. Identify which expert perspectives are needed to evaluate work in this domain. Produce a ROLES-PLAN:

```
ROLES-PLAN for {topic}:

Domain experts (derived from context):
  - [role name specific to this domain]
  - [additional derived roles as warranted]

Stock roles (always included):
  - pm
  - architect
  - strategy
  - inertia-advocate

Output area: .roles/{derived-area-name}/
```

---

STEP 2 — WRITE ROLE FILES

Write one `.md` file per role to `.roles/{area}/`. Use this exact template for every file. Fill in every slot. Do not omit any field or sub-field.

```
---
name: {role-name}
  # Required. Lowercase slug. For domain experts, use domain vocabulary (e.g., "signal-fidelity-analyst"),
  # not generic labels (e.g., "domain-expert").
  # Failure: name is "domain-expert" or "role-1" — use a name specific to this role's concern.

version: "1.0"

archetype: {archetype}
  # Required. Choose one: product | technical | business | challenger | [domain-specific label]
  # Failure: omitting archetype makes role type ambiguous for downstream filtering.

orientation:
  frame: |
    {Epistemic viewpoint — how this role sees the work. Must be a perspective statement: "Sees X through
    the lens of Y." For domain experts, must reference a concern specific to this domain that could
    not apply verbatim to an unrelated product.}
    # Failure: frame is a task list ("responsible for reviewing specs") — frame is how this role sees
    # the world, not what it does.

  serves: |
    {Stakeholder or system concern that depends on this role's signal. Must identify who benefits
    and what they get from this role's perspective — not a restatement of frame.}
    # Failure: serves restates frame ("ensures specs are reviewed") — serves names a beneficiary,
    # not a responsibility.

lens:
  verify_questions:
    - "{Question 1: answerable by reading an artifact or running code. References a specific
       artifact, behavior, or measurable outcome. Not rhetorical.}"
    - "{Question 2: must surface a concern no other role in this registry would surface first.}"
    # Failure: questions are rhetorical ("Is this good?") or unmeasurable ("Is the quality high?").
    # Minimum two questions per role.

  simplify_rules:
    - "{Rule that excludes or constrains scope — not a description of good practice. Must be
       phrased as a prohibition or elimination: 'Remove X if Y', 'Do not include Z unless W'.}"
    # Failure: simplify_rules restate the scope description ("focus on signal fidelity") rather
    # than constraining it. Minimum one rule per role.

expertise:
  depth: |
    {Specific knowledge and methods this role applies. Name techniques, frameworks, or
    domain concepts — not just "expertise in X."  }
    # Failure: depth is a one-word label ("security") with no method or technique named.

  relevance: |
    {Which Signal namespaces, skill types, or artifact types this role should be applied to.
    Be specific: "scout-feasibility, draft-spec" not "all skills".}
    # Failure: relevance is "all namespaces" — that is the stock PM's role, not a domain expert's.

scope: workspace

collaborates_with:
  - {area}:{role-name-of-collaborator}
  # Required. List roles this role hands off to or receives from. Must reference names
  # of other roles in this registry. Do not list every role (failure: "works with everyone").
---
```

---

STEP 3 — WRITE REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` using this template. Fill every slot:

```
---
area: {area}
date: {date}
---

# Role Registry — {area}

**Area:** {area}
**Total roles:** {N}
**Stock roles:** pm, architect, strategy, inertia-advocate
**Domain experts:** {name each with one-line derivation source — e.g., "signal-fidelity-analyst (derived from: signal namespace correctness concerns in spec)"}
**Coverage gaps:** {any concern not covered by any role, or "none detected"}
```

---

FINAL LINE

End `REGISTRY.md` with:

```
Generated by: /org-roles {topic} — {date}
```

---

## V-03 — Phrasing Register: Failure-Mode-Named Field Constraints

**axis:** phrasing-register
**hypothesis:** Schema field instructions that name the specific failure mode for each field produce more reliable field content than instructions that state only the positive requirement. Naming the failure converts an abstract constraint ("frame and serves must differ") into a recognizable pattern to avoid ("serves restates frame — both fields carry the same sentence with different words"). C-12 is directly satisfied by construction. Secondary benefit: C-06 and C-07 improve because the collapse patterns for those criteria are explicitly named for the model to check before writing. Falsifiable: if fields still exhibit the named failure mode despite the explicit prohibition, naming failure modes alone does not prevent them — the failure is either execution-depth or context-load.

---

You are running `/org-roles {topic}`.

---

STEP 1 — ANALYZE CONTEXT

Read available context for `{topic}`. Write a CONTEXT-SUMMARY:
- What product or system is being built?
- What are the highest-risk failure modes for this domain (not generic — specific to `{topic}`)?
- Which expert perspectives would catch those failures?

Do not name PM, Architect, Strategy, or inertia-advocate in this step.

---

STEP 2 — DERIVE DOMAIN EXPERTS

From Step 1, name at least one domain expert role specific to `{topic}`. State the domain concern each expert addresses.

---

STEP 3 — COMPILE FULL ROLE SET

Add the four stock roles: pm, architect, strategy, inertia-advocate.

Full role set = domain experts (Step 2) + stock roles (Step 3).

---

STEP 4 — WRITE ROLE FILES

Write one `.md` file per role to `.roles/{area}/`.

Use the following schema. Every field instruction includes a FAILURE MODE that names the exact collapse pattern — read each FAILURE MODE before filling in the field.

---

**Field: `name`**
Requirement: A lowercase slug that names this role's specific concern.
FAILURE MODE: Generic label — "domain-expert", "role-1", "reviewer". If the name could apply to any product, it is too generic. Use domain vocabulary from Step 1.

---

**Field: `orientation.frame`**
Requirement: An epistemic viewpoint — how this role sees work in `{topic}`. Must be a perspective statement ("Sees X through the lens of Y") that references domain-specific concerns from Step 1.
FAILURE MODE: Task list — "responsible for reviewing specs and ensuring quality". Frame is *how this role sees*, not *what it does*. If you could replace the domain name with any other domain and the frame would still make sense, it is too generic.

---

**Field: `orientation.serves`**
Requirement: Names the stakeholder or system concern that benefits from this role's perspective. Must name a beneficiary and what they receive ("Teams that need to know whether X is safe to ship").
FAILURE MODE: Frame restatement — "ensures that X is reviewed from the lens of Y". If `serves` is a paraphrase of `frame`, delete it and write a beneficiary sentence instead. Two fields that carry the same information provide zero additional signal.

---

**Field: `lens.verify_questions`**
Requirement: Actionable questions answerable by reading an artifact or running code. At minimum two questions. Each must reference a specific artifact, behavior, or measurable outcome. At least one must surface a concern unique to this role's frame that no other role in this registry would prioritize.
FAILURE MODE (type 1): Rhetorical question — "Is the design appropriate?" cannot be answered by reading an artifact.
FAILURE MODE (type 2): Universal question — "Does the spec cover edge cases?" every role could ask this; it does not belong to this role's frame.
FAILURE MODE (type 3): Unmeasurable question — "Is the team aligned?" cannot be answered without a meeting.

---

**Field: `lens.simplify_rules`**
Requirement: At minimum one opinionated rule that excludes, constrains, or eliminates scope. Must be phrased as a prohibition or elimination.
FAILURE MODE: Scope description — "focus on signal fidelity concerns" is a description of what to do, not a constraint on what to remove. A simplify rule removes something. If the rule does not reduce scope, it is not a simplify rule.
FAILURE MODE: Restatement of frame — "only consider issues relevant to this role's perspective" applies to every role and constrains nothing.

---

**Field: `expertise.depth`**
Requirement: Specific techniques, frameworks, or methods this role applies. Names things a practitioner would recognize.
FAILURE MODE: Label without method — "security expertise" names a domain but not a technique. "Threat modeling, attack surface enumeration, auth boundary verification" names methods.

---

**Field: `expertise.relevance`**
Requirement: Specific Signal namespaces, skill types, or artifact types this role should be applied to.
FAILURE MODE: Universal relevance — "all namespaces" or "all skills". Domain expert roles have narrower relevance than stock roles; over-broad relevance is a signal that the role is actually a stock archetype in disguise.

---

**Field: `collaborates_with`**
Requirement: List roles this role hands off to or receives input from. Every entry must exist in the full role set from Step 3.
FAILURE MODE (type 1): Phantom role — names a role not in the output set. Downstream skills read these entries by name; phantom names silently break integration.
FAILURE MODE (type 2): Everyone listed — "collaborates with all roles" is not a collaboration model. At most three to four specific roles; the pairing should reflect a real handoff or dependency.

---

STEP 5 — WRITE REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` with: area, total role count, stock role names, domain expert names and their derivation source, and any coverage gaps detected.

FAILURE MODE: Heading-only stub — "## Registry Summary" with no content below it. The summary must contain the five fields listed above; a heading with no content fails C-10.

---

FINAL LINE

End `REGISTRY.md` with:

```
Generated by: /org-roles {topic} — {date}
```

---

## V-04 — Role Sequence + Output Format: Context-First with Role File Templates

**axes:** role-sequence + output-format
**hypothesis:** Context-first ordering (V-01) combined with an explicit file template (V-02) closes the two structural failure paths that most commonly co-occur: domain expert frames anchored to stock archetypes (C-11 fail) and schema fields omitted from role files (C-01 fail, C-13 fail). The ordering constraint forces domain-specific language to be committed in Step 1 prose before the stock archetypes appear; the template constraint forces all six schema fields to be present in every file. Neither constraint alone closes both paths. Falsifiable: if domain expert frames are still generic despite context-first ordering, anchoring failure is vocabulary-depth (the model read context but summarized it generically), not ordering-structure — and the template cannot fix it.

---

You are running `/org-roles {topic}`.

---

PHASE 1 — CONTEXT ANALYSIS (domain experts only — stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; drawn from actual context, not generic):
  1. [concern: specific failure mode, blind spot, or risk unique to this domain]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary — not "domain-expert"]
    Concern addressed: [which concern above]
    Candidate frame: [one sentence using this domain's vocabulary]
    Candidate verify focus: [what artifact or behavior this role checks]
```

Phase 1 complete when: DOMAIN-ANALYSIS is written with at least one derived expert and its candidate frame references domain vocabulary from the concerns list.

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

---

PHASE 2 — STOCK ROLES

After Phase 1 is written, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate must include at least one verify question of the form:
"Why is the current approach insufficient — what specific failure does the status quo produce?"

Phase 2 complete when: STOCK-ROLES block is written.

---

PHASE 3 — DETERMINE OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .roles/{area}/
```

Area must be a domain-specific slug, not `default` or `roles`.

---

PHASE 4 — WRITE ROLE FILES

Write one `.md` file per role to `.roles/{area}/`. Write domain-expert roles first (from Phase 1), then stock roles (from Phase 2).

Use this exact template for every file. Fill in every slot. Do not leave any field empty or omit any field:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement — how this role sees work in this domain. Domain experts must
    reference language from their DOMAIN-ANALYSIS candidate frame (Phase 1). Stock roles
    use their standard frames but may reference domain context.}

  serves: |
    {Beneficiary statement — who depends on this role's signal and what they get.
    Must name a beneficiary, not restate frame.}

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact. References specific artifact
       type, behavior, or outcome. Not rhetorical or universal.}"
    - "{Second question: surfaces a concern unique to this role's frame.}"

  simplify_rules:
    - "{Opinionated constraint that excludes or constrains — phrased as a prohibition
       or elimination, not a description of good practice.}"

expertise:
  depth: |
    {Specific methods, techniques, and frameworks this role applies. Names things
    a practitioner would recognize — not just a domain label.}

  relevance: |
    {Specific Signal namespaces or artifact types this role applies to.
    Domain experts: narrow; stock roles: can be broad.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # Every listed role must exist in the full role set. No phantom names.
---
```

Phase 4 complete when: all role files are written with every slot filled.

---

PHASE 5 — REGISTRY SUMMARY

Write `.roles/{area}/REGISTRY.md` using this template:

```
---
area: {area}
total_roles: {N}
date: {date}
---

# Role Registry — {area}

**Area:** {area}
**Total roles:** {N}
**Stock roles:** pm, architect, strategy, inertia-advocate
**Domain experts:**
  - {name}: derived from concern "{concern}" (Phase 1 DOMAIN-ANALYSIS)
  - (repeat for each domain expert)
**Coverage gaps:** {concerns from Phase 1 not fully addressed by any role, or "none detected"}
```

Phase 5 complete when: all five fields (area, count, stock names, domain expert names+source, gaps) are present.

---

FINAL LINE

End `REGISTRY.md` with:

```
Generated by: /org-roles {topic} — {date}
```

---

## V-05 — Phrasing Register + Lifecycle Emphasis: DO/DO NOT Steps with Completion Conditions

**axes:** phrasing-register + lifecycle-emphasis
**hypothesis:** A four-phase lifecycle with per-phase completion conditions enforces C-13 (every step defines its output format and completion state) while DO/DO NOT failure-mode-named instructions throughout the schema enforce C-12 (field instructions name failure modes). The combination prevents two distinct failure modes from co-occurring: structural omission (no output definition = C-13 fail) and constraint ambiguity (positive-only instructions = C-12 fail). Per-phase completion conditions act as internal gates — the model cannot claim a phase is done without satisfying the named output requirement. Falsifiable: if C-07 (lens quality) still fails despite named failure modes for verify/simplify collapse, the failure is content-depth at execution time, not instruction structure.

---

You are running `/org-roles {topic}`.

Complete the following four phases in order. Do not begin a phase until the previous phase's completion condition is met.

---

PHASE 1 — ANALYZE AND DERIVE

**Purpose:** Surface domain concerns and derive domain experts. Stock roles are not named in this phase.

DO read available context for `{topic}` (spec, product description, codebase, or input provided).
DO write a DOMAIN-CONCERNS list with at least three specific failure modes, blind spots, or risks unique to `{topic}`.
DO NOT list concerns that apply to any software product (e.g., "scalability", "testing coverage") — list concerns specific to `{topic}`.
DO derive at least one domain expert role from the concerns. For each derived expert, write:
  - name (in domain vocabulary — DO NOT use "domain-expert" or "expert-1")
  - one-sentence frame using language from the concerns list
  - one verify focus area (what artifact or behavior this expert checks)
DO NOT name PM, Architect, Strategy, or inertia-advocate in this phase.

**Completion condition:** DOMAIN-CONCERNS list is written with at least three items AND at least one derived expert with name, frame, and verify focus is written.

---

PHASE 2 — LOAD STOCK ROLES

**Purpose:** Add the four universal roles after domain experts are established.

DO write a STOCK-ROLES-LOADED block listing: pm, architect, strategy, inertia-advocate.
DO confirm the inertia-advocate's lens will include at least one question of the form: "Why is the current approach insufficient — what specific failure does the status quo produce that justifies this change?"
DO NOT skip the inertia-advocate. A registry without a devil-advocate role fails C-02 unconditionally.
DO NOT introduce new domain experts in this phase — domain derivation is complete after Phase 1.

**Completion condition:** STOCK-ROLES-LOADED block is written with all four stock role names.

---

PHASE 3 — WRITE ROLE FILES

**Purpose:** Emit one `.md` file per role to `.roles/{area}/`. Write domain experts first (Phase 1), then stock roles (Phase 2).

DO determine the area slug from `{topic}` context before writing files.
DO NOT use `default`, `generic`, or `roles` as the area name.
DO write domain-expert files before stock role files. This sequence is required — it enforces that domain frames are written without stock archetype influence.

For each role file, apply the following DO/DO NOT instructions:

**`orientation.frame`**
DO write a perspective statement: how this role sees work — not what it does.
DO NOT write a task list ("responsible for reviewing X") — FAILURE MODE: frame becomes a job description.
DO NOT write a statement that applies equally to any product — domain expert frames must use vocabulary from Phase 1 DOMAIN-CONCERNS.

**`orientation.serves`**
DO name a stakeholder or system concern that depends on this role's perspective.
DO NOT restate `frame` in different words — FAILURE MODE: two fields carry identical information; downstream skills that read `serves` separately from `frame` receive no additional signal.

**`lens.verify_questions`**
DO write at least two questions. Each must be answerable by reading an artifact, running code, or inspecting a measurable outcome.
DO NOT write rhetorical questions ("Is this good?") — FAILURE MODE: unanswerable, provides no review guidance.
DO NOT write universal questions that every role would ask — FAILURE MODE: question is not owned by this role's frame.
DO ensure at least one question per role surfaces a concern unique to this role that no other role in the registry would prioritize.

**`lens.simplify_rules`**
DO write at least one rule as a prohibition or elimination: "Remove X if Y", "Do not include Z unless W".
DO NOT write a description of good practice ("focus on signal quality") — FAILURE MODE: scope description masquerading as a constraint. A simplify rule reduces scope; a scope description does not.

**`expertise.depth`**
DO name specific methods, techniques, or frameworks.
DO NOT write a domain label only ("security expertise") — FAILURE MODE: label without method cannot distinguish two roles in the same domain.

**`expertise.relevance`**
DO name specific Signal namespaces or artifact types.
DO NOT write "all namespaces" for domain expert roles — FAILURE MODE: domain experts have narrower relevance than the PM by definition; universal relevance is a stock-role claim.

**`collaborates_with`**
DO list two to four roles this role has a specific handoff or dependency with.
DO NOT list every role — FAILURE MODE: "works with everyone" carries no structural information and breaks directed graph reasoning over collaborations.
DO NOT list a role that does not exist in the full role set — FAILURE MODE: phantom names silently fail integration with downstream skills that resolve collaboration links.

**Completion condition:** Every role file exists at `.roles/{area}/` AND every file contains all six top-level fields with all required sub-fields filled (not empty strings or placeholder text).

---

PHASE 4 — EMIT REGISTRY SUMMARY

**Purpose:** Write `REGISTRY.md` giving the caller a single-glance audit of the role set.

DO write `.roles/{area}/REGISTRY.md` containing all five required fields:
  1. `area` — the area slug
  2. `total_roles` — exact count
  3. `stock_roles` — names: pm, architect, strategy, inertia-advocate
  4. `domain_experts` — each name plus the Phase 1 concern it was derived from
  5. `coverage_gaps` — any Phase 1 concern not addressed by any role, or "none detected"

DO NOT write a heading-only stub — FAILURE MODE: "## Registry Summary" with no content below fails C-10 unconditionally; the heading is not the summary.
DO NOT omit any of the five fields — each field serves a distinct audit function that the caller cannot reconstruct by inspecting individual role files.

**Completion condition:** `REGISTRY.md` exists and all five fields are present with non-empty content.

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} — {date}
```

Replace `{topic}` and `{date}` with actual values. DO NOT emit literal placeholder text in the final line.
