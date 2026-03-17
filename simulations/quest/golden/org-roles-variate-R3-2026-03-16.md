---
skill: quest-variate
skill_target: org-roles
date: 2026-03-16
round: R3
rubric_version: v3
status: variate
---

# org-roles Variate — Round 3

**Date:** 2026-03-16
**Skill:** org-roles
**Rubric:** v3 (C-01 through C-17; new in v3: C-14 typed dual-failure, C-15 heading-stub failure mode, C-16 step completion condition, C-17 worked examples)
**Round:** R3 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 3 Variation Map

| V | Axis | Primary C targets | Hypothesis |
|---|------|------------------|------------|
| V-01 | phrasing-register (worked examples) | C-17 PASS, C-14 PASS, C-15 PASS | Concrete before/after examples in three or more field constraints let the model calibrate the pass/fail boundary by pattern rather than rule — the label names the failure, the example shows it |
| V-02 | lifecycle-emphasis (binary completion gates) | C-16 PASS, C-14 PASS, C-15 PASS | Explicit GATE checklists at every step close the structural omission path — the model must assert each condition is TRUE before advancing, not merely format-complete |
| V-03 | inertia framing (devil-advocate as first-class anchor) | C-02 quality, C-14 PASS | Introducing the inertia-advocate in the skill preamble as a mandatory design constraint, and requiring every domain expert to include one "inertia-response" verify question, elevates the devil-advocate from stock afterthought to structural counterweight that improves all role lenses |
| V-04 | phrasing-register + lifecycle-emphasis | C-16 PASS, C-17 PASS | Worked examples (show the boundary) combined with binary completion gates (enforce the boundary) close both calibration failure and structural omission simultaneously |
| V-05 | all four axes | C-14, C-15, C-16, C-17 all PASS | Full integration of typed dual-failure labels + heading-stub failure mode + per-step completion conditions + worked examples on four or more fields in a context-first + fill-in template structure; the aspirational ceiling for v3 |

---

## V-01 — Phrasing Register: Worked Examples in Field Constraints

**axis:** phrasing-register
**hypothesis:** Embedding before/after worked examples in the three field constraints most prone to collapse (`frame`, `serves`, `simplify_rules`) lets the model recognize bad content by pattern match rather than rule inference. Naming the failure mode (C-12) tells the model what to avoid; a worked example of the failure shows it so the model can compare its own output directly. Falsifiable: if fields still exhibit the named collapse pattern despite the worked example (e.g., `serves` still restates `frame`), the failure is execution-depth rather than instruction structure — the model read the example but did not apply it at generation time.

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

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

Phase 1 complete when: DOMAIN-ANALYSIS is written with at least one derived expert whose candidate frame uses vocabulary from the concerns list.

---

PHASE 2 — STOCK ROLES

After Phase 1, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate must include at least one verify question of the form:
"Why is the current approach insufficient — what specific failure does the status quo produce that this feature resolves?"

Phase 2 complete when: STOCK-ROLES block is written with all four names.

---

PHASE 3 — OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area must be a domain-specific slug, not `default` or `roles`.

---

PHASE 4 — WRITE ROLE FILES

Write one `.md` file per role to `.craft/roles/{area}/`. Write domain-expert roles first (Phase 1), then stock roles (Phase 2).

Use this template for every file. Fill every slot. Read the FAILURE MODE and WORKED EXAMPLE for each annotated field before filling it in.

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement — how this role sees work in this domain. Must be phrased as
    "Sees X through the lens of Y" or an equivalent viewpoint construction. Domain experts
    must reference language from their Phase 1 candidate frame.}

    FAILURE MODE: task list — frame describes what this role does, not how it sees.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec artifacts and ensuring they
    meet quality standards before milestone commits."
    WORKED EXAMPLE (good): "Sees every spec artifact through the question of whether the
    stated requirements will survive contact with the actual system boundary — looking for
    the gap between what the spec assumes and what the system will enforce."

  serves: |
    {Stakeholder or system concern that benefits from this role's perspective. Name a
    beneficiary and what they receive. Must not restate frame.}

    FAILURE MODE: frame restatement — serves paraphrases frame in different words.
    WORKED EXAMPLE (bad):  "Ensures that spec artifacts are evaluated through a boundary
    correctness lens before milestone commits." (same idea as frame, different words)
    WORKED EXAMPLE (good): "Teams deciding whether a spec is safe to hand to engineering —
    they receive a boundary-gap verdict before the artifact becomes load-bearing."

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact, running code, or inspecting
       a measurable outcome. References a specific artifact type, behavior, or outcome.}"
    - "{Second question: surfaces a concern unique to this role's frame — no other role
       in this registry would prioritize this question first.}"

  simplify_rules:
    - "{Opinionated rule that removes, excludes, or constrains scope. Must be phrased as
       a prohibition or elimination: 'Remove X if Y' or 'Do not include Z unless W'.}"

    FAILURE MODE: scope description — the rule describes what to prioritize, not what to remove.
    WORKED EXAMPLE (bad):  "Focus on boundary correctness and spec-system gap concerns."
    (describes the role's focus area — does not reduce scope or eliminate anything)
    WORKED EXAMPLE (good): "Remove any verify question that cannot be answered by reading
    an artifact or running a command — exclude questions that require a meeting, interview,
    or stakeholder judgment call to answer."

expertise:
  depth: |
    {Specific methods, techniques, or frameworks this role applies. Name things a
    practitioner would recognize — not just a domain label.}

  relevance: |
    {Specific Signal namespaces or artifact types this role applies to.
    Domain experts: narrow. Stock roles: can be broader.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # Every listed name must exist in the full role set from Phases 1–2.
  # FAILURE MODE (type 1): phantom role — a name not present in the output role set.
  #   Phantom names silently break downstream skills that resolve collaboration links by name.
  # FAILURE MODE (type 2): universalist listing — "collaborates with all roles" or listing
  #   every role in the set. List only two to four roles with a genuine handoff or dependency.
---
```

Phase 4 complete when: every role file exists with all six top-level fields and required sub-fields filled — no empty strings, no placeholder text, no task-list frames, no phantom names in collaborates_with.

---

PHASE 5 — REGISTRY SUMMARY

Write `.craft/roles/{area}/REGISTRY.md` using this template. Fill every slot:

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
**Coverage gaps:** {concerns from Phase 1 not addressed by any role, or "none detected"}
```

FAILURE MODE: heading-only stub — a section header with no required content beneath it is not a complete registry entry and fails C-10 unconditionally.

Phase 5 complete when: REGISTRY.md exists with all five fields present and non-empty (area, total_roles, stock role names, domain expert names with derivation source, coverage gaps).

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} — {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-02 — Lifecycle Emphasis: Binary Completion Gates Per Step

**axis:** lifecycle-emphasis
**hypothesis:** A GATE block at the end of every output-producing step functions as a required self-audit: the model must check each condition is TRUE before advancing to the next step. This is distinct from a format template (which defines what the output must look like) — the gate defines when the output is done. R2's V-04 had completion conditions in some phases but not all, and none used an explicit checklist form. A numbered checklist that the model evaluates forces it to inspect its own output structurally, not just produce it. Falsifiable: if outputs still contain empty fields or stub sections despite the gate (the model asserts TRUE without checking), the failure is execution fidelity at inference time — the gate structure alone cannot enforce honest self-evaluation.

---

You are running `/org-roles {topic}`.

---

PHASE 1 — CONTEXT ANALYSIS (domain experts only — stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; specific to this domain, not generic):
  1. [concern: failure mode, blind spot, or risk unique to {topic}]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary — not "domain-expert" or "expert-1"]
    Concern addressed: [which concern above]
    Candidate frame: [one sentence using vocabulary from this domain's concerns]
    Candidate verify focus: [what artifact or behavior this expert checks]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE — Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written
2. At least three domain concerns are listed
3. At least one domain expert is derived with name, concern link, and candidate frame
4. No stock role names appear in this block

---

PHASE 2 — STOCK ROLES

Add the four stock roles after Phase 1 GATE passes:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate must have at least one verify question explicitly framed as:
"Why is the current approach insufficient — what specific failure does the status quo produce that this feature resolves?"

GATE — Phase 2 complete when ALL of the following are TRUE:
1. STOCK-ROLES block is written
2. All four role names are present
3. inertia-advocate is listed
4. The inertia-advocate's status-quo question pattern is confirmed

---

PHASE 3 — OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .craft/roles/{area}/
```

GATE — Phase 3 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug is a domain-specific term derived from context (not `default`, `generic`, or `roles`)
3. Full path is `.craft/roles/{area}/`

---

PHASE 4 — WRITE ROLE FILES

Write one `.md` file per role to `.craft/roles/{area}/`. Domain-expert roles first (Phase 1), then stock roles (Phase 2).

Use this template for every file:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement — how this role sees work in this domain.
    Domain experts: must use vocabulary from Phase 1 candidate frame.
    Must not be a task list or job description.}

  serves: |
    {Beneficiary statement — names who depends on this role's signal and what they receive.
    Must not restate frame.}

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact or running code.}"
    - "{Second question unique to this role's frame.}"

  simplify_rules:
    - "{Opinionated constraint — phrased as a prohibition or elimination, not a description.}"

expertise:
  depth: |
    {Specific methods and techniques — not just a domain label.}

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # FAILURE MODE (type 1): phantom role — name not present in the full role set.
  # FAILURE MODE (type 2): universalist listing — do not list every role; list two to four
  #   roles with a genuine handoff or dependency.
---
```

GATE — Phase 4 complete when ALL of the following are TRUE:
1. One file exists per role at `.craft/roles/{area}/`
2. Every file has all six top-level fields: name, version, archetype, orientation, lens, expertise
3. Every file has all required sub-fields: orientation.frame, orientation.serves, lens.verify_questions (2+), lens.simplify_rules (1+), expertise.depth, expertise.relevance
4. No field contains an empty string, placeholder text, or task-list content in frame
5. No collaborates_with entry names a role absent from the full role set

---

PHASE 5 — REGISTRY SUMMARY

Write `.craft/roles/{area}/REGISTRY.md` containing all five required fields:

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
**Coverage gaps:** {any Phase 1 concern not addressed by any role, or "none detected"}
```

FAILURE MODE: heading-only stub — a section header with no content beneath it is not a summary. The heading is not the summary; all five fields are.

GATE — Phase 5 complete when ALL of the following are TRUE:
1. REGISTRY.md exists at `.craft/roles/{area}/REGISTRY.md`
2. `area` field is present and non-empty
3. `total_roles` count is present and matches actual file count
4. `stock_roles` names all four stock roles
5. `domain_experts` names each domain expert with its Phase 1 derivation source
6. `coverage_gaps` is present (even if "none detected")

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} — {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-03 — Inertia Framing: Devil-Advocate as First-Class Registry Anchor

**axis:** inertia framing
**hypothesis:** The inertia-advocate role in Signal exists to defeat motivated reasoning — the tendency to build a registry that justifies the feature rather than challenges it. When the devil-advocate is listed as the fourth stock role (as in all R2 variates), the model treats it as an afterthought with generic skepticism. When the inertia-advocate is introduced in the skill preamble as a mandatory structural counterweight, and other roles are required to include an "inertia-response" verify question (one question that pre-answers the devil-advocate's anticipated objection), the registry becomes a genuine dialogue rather than a justification. Falsifiable: if inertia-advocate verify_questions still default to generic skepticism ("Is the status quo adequate?") rather than domain-specific failure-mode framing despite the structured preamble, inertia quality is a content-depth problem that framing prominence alone cannot solve.

---

You are running `/org-roles {topic}`.

**Registry design contract:** Every role registry generated by this skill must include a devil-advocate (inertia-advocate) role whose job is not generic skepticism but a specific challenge: arguing that the status quo is sufficient and that the proposed feature addresses a problem that does not exist or is adequately handled already. The inertia-advocate exists to be falsified — if the other roles cannot answer its questions with artifact evidence, the feature proposal is not ready. All domain expert roles must include one verify question that pre-answers the inertia-advocate's anticipated objection for their concern area.

---

STEP 1 — CONTEXT ANALYSIS

Read available context for `{topic}`. Write a DOMAIN-CONCERNS block:

```
DOMAIN-CONCERNS for {topic}:
  - [concern 1: specific failure mode or blind spot unique to this domain]
  - [concern 2]
  - [concern 3]
  (at minimum three; drawn from actual context)
```

From the domain concerns, derive domain expert roles. For each derived expert, also write the anticipated inertia objection for their concern:

```
DOMAIN-EXPERTS-DERIVED:
  - Expert name: [slug in domain vocabulary]
    Derived from concern: [which concern above]
    Frame: [one sentence using this domain's vocabulary]
    Inertia objection this expert must pre-answer: [what the devil-advocate would say about
      why this concern is already handled adequately by the status quo]
```

Do not name PM, Architect, Strategy, or inertia-advocate in this step.

Step 1 complete when: DOMAIN-CONCERNS and DOMAIN-EXPERTS-DERIVED blocks are written, each derived expert has a named inertia objection.

---

STEP 2 — INERTIA-ADVOCATE SPECIFICATION

Before loading stock roles, define the inertia-advocate's challenge surface for `{topic}`:

```
INERTIA-ADVOCATE for {topic}:
  Status-quo claim: [what the status quo does that makes the proposed feature unnecessary —
    derive this from Step 1 domain concerns, not a generic "it works fine" claim]
  Challenge questions (at minimum three, domain-specific):
    - Why is the current approach insufficient — what specific failure does the status quo
      produce that this feature resolves? (Name the failure; do not assume it.)
    - [domain-specific challenge 2]
    - [domain-specific challenge 3]
```

Step 2 complete when: INERTIA-ADVOCATE block is written with a domain-specific status-quo claim and at least three challenge questions.

---

STEP 3 — LOAD STOCK ROLES

Add the remaining three stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate (specified in Step 2)
```

Step 3 complete when: STOCK-ROLES block is written with all four entries.

---

STEP 4 — DETERMINE OUTPUT AREA

Write: `OUTPUT-AREA: .craft/roles/{area}/`

Area must be a domain-specific slug derived from context (not `default`, `generic`, or `roles`).

---

STEP 5 — WRITE ROLE FILES

Write one `.md` file per role to `.craft/roles/{area}/`. Write domain-expert roles first, then stock roles.

Apply this schema for every file. Every field is required:

```yaml
---
name: {role-name}
version: "1.0"
archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement — how this role sees work. Domain experts: use vocabulary
    from Step 1 DOMAIN-CONCERNS. Must be an epistemic viewpoint, not a task list.}

  serves: |
    {Beneficiary statement — who depends on this role's signal. Must not restate frame.}

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact or running code.}"
    - "{Second question unique to this role's frame.}"
    - "{Inertia-response question: pre-answers the devil-advocate's anticipated objection
       for this role's concern area. Domain experts only; stock roles may omit.
       Form: 'What artifact evidence shows that [inertia objection from Step 1] is wrong?'}"

  simplify_rules:
    - "{Opinionated constraint — prohibition or elimination, not a description of good practice.}"

expertise:
  depth: |
    {Specific methods, techniques, or frameworks — not just a domain label.}

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # FAILURE MODE (type 1): phantom role — a name not in the output role set.
  #   Phantom names silently break downstream skills that resolve collaboration links.
  # FAILURE MODE (type 2): universalist listing — "collaborates with all roles."
  #   List two to four specific roles with a genuine handoff or dependency.
---
```

The inertia-advocate file must use Step 2's INERTIA-ADVOCATE block as its verify_questions source. Its `orientation.frame` must describe the challenge posture, not a generic "plays devil's advocate" description.

Step 5 complete when: every role file exists with all six top-level fields and required sub-fields filled; every domain expert file contains an inertia-response question in verify_questions.

---

STEP 6 — REGISTRY SUMMARY

Write `.craft/roles/{area}/REGISTRY.md`:

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
  - {name}: derived from concern "{concern}"; inertia objection pre-answered: "{objection}"
**Coverage gaps:** {any Step 1 concern not addressed by any role, or "none detected"}
**Inertia surface:** {the status-quo claim from Step 2 — one sentence}
```

FAILURE MODE: heading-only stub — a section header with no content beneath it fails C-10 unconditionally.

Step 6 complete when: REGISTRY.md exists with all six fields present (area, count, stock roles, domain experts with concern and inertia objection, coverage gaps, inertia surface).

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} — {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-04 — Combined: Worked Examples + Completion Gates

**axes:** phrasing-register + lifecycle-emphasis
**hypothesis:** V-01 (worked examples) shows the model where the pass/fail boundary is for each field. V-02 (completion gates) forces the model to assert its output meets a binary condition before advancing. These two interventions target different failure modes: calibration failure (the model produces a task-list frame because it cannot tell the difference from a perspective statement) and structural omission failure (the model advances past a phase without all required fields). Neither alone closes both paths. Together, worked examples prevent calibration failures and completion gates catch any omission that slipped through. Falsifiable: if content-quality failures persist despite worked examples, the model's generation depth is the bottleneck; if structural omissions persist despite gates, honest self-evaluation at inference time cannot be enforced by structure alone.

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
    Candidate verify focus: [what artifact or behavior this expert checks]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE — Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written
2. At least three domain concerns are present
3. At least one domain expert is present with name, concern link, and candidate frame using domain vocabulary
4. No stock role names appear in the block

---

PHASE 2 — STOCK ROLES

After Phase 1 GATE passes, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate must include at least one verify question explicitly framed as:
"Why is the current approach insufficient — what specific failure does the status quo produce that this feature resolves?"

GATE — Phase 2 complete when ALL of the following are TRUE:
1. STOCK-ROLES block is written with all four names
2. inertia-advocate is listed
3. The inertia-advocate's status-quo question pattern is confirmed

---

PHASE 3 — OUTPUT AREA

Derive the area slug from `{topic}` context. Write:

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area must be a domain-specific slug (not `default`, `generic`, or `roles`).

GATE — Phase 3 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area is a domain-specific slug
3. Full path is `.craft/roles/{area}/`

---

PHASE 4 — WRITE ROLE FILES

Write one `.md` file per role to `.craft/roles/{area}/`. Domain-expert roles first (Phase 1), then stock roles (Phase 2).

Use this template for every file. Fill every slot. Read the FAILURE MODE and WORKED EXAMPLE for annotated fields before filling them in:

```yaml
---
name: {role-name}
  # Required. Lowercase slug. Domain experts: use domain vocabulary.
  # FAILURE MODE: generic label — "domain-expert" or "expert-1".

version: "1.0"

archetype: {product | technical | business | challenger | domain-specific-label}

orientation:
  frame: |
    {Perspective statement — how this role sees work in this domain. Must be phrased as
    "Sees X through the lens of Y" or equivalent. Domain experts must reference language
    from Phase 1 candidate frame.}

    FAILURE MODE: task list — frame becomes a job description.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec artifacts and ensuring correctness
    before engineering handoff."
    WORKED EXAMPLE (good): "Sees every spec artifact through the question of whether the
    stated requirements will survive contact with the actual system boundary — looking for
    the gap between what the spec assumes and what the system will enforce."

  serves: |
    {Beneficiary statement — who depends on this role's signal. Must name a beneficiary
    and what they receive. Must not restate frame.}

    FAILURE MODE: frame restatement — serves paraphrases frame in different words.
    WORKED EXAMPLE (bad):  "Ensures that spec artifacts are evaluated through a boundary
    correctness lens." (same idea as frame, different words)
    WORKED EXAMPLE (good): "Teams deciding whether a spec is safe to hand to engineering —
    they receive a boundary-gap verdict before the artifact becomes load-bearing."

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact or running code. References
       a specific artifact type, behavior, or measurable outcome. Not rhetorical.}"
    - "{Second question: surfaces a concern unique to this role's frame — no other role
       in this registry would prioritize this question first.}"

  simplify_rules:
    - "{Opinionated rule that removes, excludes, or constrains scope. Phrased as a
       prohibition or elimination: 'Remove X if Y' or 'Do not include Z unless W'.}"

    FAILURE MODE: scope description — rule describes what to prioritize, not what to remove.
    WORKED EXAMPLE (bad):  "Focus on boundary correctness and spec-system gap concerns."
    (describes priority — does not reduce or eliminate scope)
    WORKED EXAMPLE (good): "Remove any verify question that cannot be answered by reading
    an artifact or running a command — exclude questions that require a stakeholder interview."

expertise:
  depth: |
    {Specific methods, techniques, or frameworks — not a domain label only.}

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # FAILURE MODE (type 1): phantom role — name not in the output role set.
  #   Phantom names silently break downstream skills that resolve collaboration links by name.
  # FAILURE MODE (type 2): universalist listing — do not list every role.
  #   List two to four roles with a genuine handoff or dependency.
---
```

GATE — Phase 4 complete when ALL of the following are TRUE:
1. One file per role exists at `.craft/roles/{area}/`
2. Every file has all six top-level fields with required sub-fields
3. No frame field contains a task list or job description
4. No serves field restates frame
5. Every simplify_rules entry is phrased as a prohibition or elimination
6. No collaborates_with entry names a role absent from the full role set
7. No collaborates_with lists every role in the set

---

PHASE 5 — REGISTRY SUMMARY

Write `.craft/roles/{area}/REGISTRY.md` using this template. Fill every slot:

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
**Coverage gaps:** {concerns from Phase 1 not addressed by any role, or "none detected"}
```

FAILURE MODE: heading-only stub — "## Registry Summary" with no required content beneath it fails C-10 unconditionally. The heading is not the summary; all five fields are the summary.

GATE — Phase 5 complete when ALL of the following are TRUE:
1. REGISTRY.md exists at `.craft/roles/{area}/REGISTRY.md`
2. `area` field is present and non-empty
3. `total_roles` count is present and matches file count
4. Stock roles section names all four stock roles
5. Domain experts section names each expert with its derivation source
6. Coverage gaps field is present (even if "none detected")

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} — {date}
```

Replace `{topic}` and `{date}` with actual values.

---

## V-05 — Combined: All Four New Criteria Integrated

**axes:** phrasing-register + lifecycle-emphasis + inertia framing + output format
**hypothesis:** C-14 (typed dual-failure labels), C-15 (heading-stub failure mode named), C-16 (binary completion condition every step), and C-17 (worked examples on three or more fields) are independent requirements that no R2 variate achieved simultaneously. V-03 R2 PASSED C-14 and C-15 but FAILED C-16 and C-17. V-04 R2 PASSED C-16 PARTIAL and was GOLDEN but FAILED C-17. This variate integrates all four: typed labels on every dual-prohibition field, heading-stub failure mode named explicitly, a GATE checklist after every phase, and worked before/after examples on four fields (frame, serves, simplify_rules, collaborates_with). The combination also includes context-first ordering (C-11) and a fill-in template (C-01, C-13). Falsifiable: if this variate scores below V-04 R2 on the essential criteria (C-01 through C-05), the additional instruction density introduced overhead that degraded essential-criteria compliance.

---

You are running `/org-roles {topic}`.

**Design contract:** This registry will be used by downstream skills (org-review, org-chart, org-committee) that read role files by field name. Field name errors, phantom collaboration references, and empty fields silently break downstream integration. Complete every slot. Apply every constraint before writing.

---

PHASE 1 — CONTEXT ANALYSIS (domain experts only — stock roles not yet named)

Read available context for `{topic}`. Write a DOMAIN-ANALYSIS block:

```
DOMAIN-ANALYSIS for {topic}:

Domain concerns (at minimum three; drawn from actual context — not generic):
  1. [concern: specific failure mode, blind spot, or risk unique to this domain]
  2. [concern]
  3. [concern]

Domain experts derived from concerns:
  - Expert name: [slug in domain vocabulary — not "domain-expert" or "expert-1"]
    Concern addressed: [which concern above]
    Candidate frame: [one sentence using this domain's vocabulary]
    Candidate verify focus: [artifact or behavior this expert checks]
    Inertia objection this expert must pre-answer: [what the devil-advocate would say to
      claim this concern is already handled adequately by the status quo]
```

Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1.

GATE — Phase 1 complete when ALL of the following are TRUE:
1. DOMAIN-ANALYSIS block is written
2. At least three domain concerns are listed
3. At least one domain expert is derived with name, concern link, candidate frame (domain vocabulary), and inertia objection
4. No stock role names appear in this block

---

PHASE 2 — STOCK ROLES

After Phase 1 GATE passes, add the four stock roles:

```
STOCK-ROLES:
  - pm
  - architect
  - strategy
  - inertia-advocate
```

The inertia-advocate's lens must include at least one verify question explicitly framed as:
"Why is the current approach insufficient — what specific failure does the status quo produce that this feature resolves?"

GATE — Phase 2 complete when ALL of the following are TRUE:
1. STOCK-ROLES block lists all four names
2. inertia-advocate is listed
3. inertia-advocate's status-quo question pattern is confirmed

---

PHASE 3 — OUTPUT AREA

Derive the area slug from `{topic}`. Write:

```
OUTPUT-AREA: .craft/roles/{area}/
```

Area must be a domain-specific slug (not `default`, `generic`, or `roles`).

GATE — Phase 3 complete when ALL of the following are TRUE:
1. OUTPUT-AREA line is written
2. Area slug is domain-specific and derived from `{topic}` context
3. Path follows the `.craft/roles/{area}/` format

---

PHASE 4 — WRITE ROLE FILES

Write one `.md` file per role to `.craft/roles/{area}/`. Domain-expert roles first (Phase 1), then stock roles (Phase 2).

Use this template for every file. Fill every slot. For annotated fields, read the FAILURE MODE and WORKED EXAMPLE before writing:

```yaml
---
name: {role-name}
  # Required. Lowercase slug. Domain experts: use domain vocabulary.
  # FAILURE MODE: generic label — "domain-expert", "expert-1", "reviewer".
  # If the name could apply to any product domain unchanged, it is too generic.

version: "1.0"

archetype: {product | technical | business | challenger | domain-specific-label}
  # Required. Choose one. Failure: omitting archetype breaks downstream role filtering.

orientation:
  frame: |
    {Perspective statement — how this role sees work in this domain. Domain experts must
    use vocabulary from Phase 1 candidate frame.}

    FAILURE MODE: task list — frame becomes a job description rather than an epistemic viewpoint.
    WORKED EXAMPLE (bad):  "Responsible for reviewing spec completeness and ensuring all
    requirements are captured before engineering handoff."
    WORKED EXAMPLE (good): "Sees every draft spec artifact through the question of whether
    the requirements written will survive contact with actual system constraints — looking for
    the gap between what authors assumed and what the system will enforce."

  serves: |
    {Beneficiary statement — names who depends on this role's perspective and what they receive.
    Must not restate frame.}

    FAILURE MODE: frame restatement — serves carries the same information as frame in different words.
    WORKED EXAMPLE (bad):  "Ensures that draft specs are evaluated through a constraint-gap
    lens to identify system boundary mismatches." (same idea as frame; zero additional signal)
    WORKED EXAMPLE (good): "Engineers who receive the spec as a handoff artifact — they get a
    boundary-gap verdict that tells them which assumptions need to be negotiated before coding."

lens:
  verify_questions:
    - "{Actionable question answerable by reading an artifact, running code, or inspecting a
       measurable outcome. References a specific artifact type, behavior, or outcome.}"
    - "{Second question unique to this role's frame — no other role in this registry would
       prioritize this question first.}"
    - "{For domain experts only: inertia-response question — pre-answers the Phase 1 inertia
       objection for this role's concern. Form: 'What artifact evidence shows that [inertia
       objection] is wrong — which artifact, which field, which measurable outcome?'}"
    # FAILURE MODE (type 1): rhetorical question — "Is the design appropriate?" cannot be
    #   answered by reading an artifact; it provides no review guidance.
    # FAILURE MODE (type 2): universal question — "Does the spec cover edge cases?" every role
    #   could ask this; it does not belong to any specific role's frame.

  simplify_rules:
    - "{Opinionated constraint — a prohibition or elimination that reduces scope.
       'Remove X if Y' or 'Do not include Z unless W'. Not a description of good practice.}"

    FAILURE MODE: scope description masquerading as a constraint.
    WORKED EXAMPLE (bad):  "Focus on constraint-gap and system-boundary concerns relevant
    to this role." (describes priority — does not remove or constrain anything)
    WORKED EXAMPLE (good): "Remove any verify question that cannot be answered by reading
    an artifact or running a command — exclude questions that require a stakeholder interview
    or meeting to answer."

expertise:
  depth: |
    {Specific methods, techniques, or frameworks this role applies. Name things a practitioner
    would recognize — not just a domain label.}

    FAILURE MODE: label without method — "security expertise" names a domain but not a technique.
    Name the method: "threat modeling, attack surface enumeration, auth boundary verification."

  relevance: |
    {Specific Signal namespaces or artifact types. Domain experts: narrow. Stock roles: broader.}

scope: workspace

collaborates_with:
  - {area}:{collaborator-role-name}
  # Required. Every listed name must exist in the full role set from Phases 1–2.
  # List two to four roles with a genuine handoff or dependency.
  #
  # FAILURE MODE (type 1): phantom role — a name not present in the output role set.
  #   Phantom names silently break downstream skills that resolve collaboration links by name.
  #   WORKED EXAMPLE (bad):  "- signal:data-quality-monitor" (role not in the output set)
  #   WORKED EXAMPLE (good): "- signal:pm" (pm is in STOCK-ROLES from Phase 2)
  #
  # FAILURE MODE (type 2): universalist listing — "collaborates with all roles" or listing
  #   every role in the registry. A universalist entry carries no structural information and
  #   breaks directed graph reasoning over collaborations.
  #   WORKED EXAMPLE (bad):  "- signal:pm\n  - signal:architect\n  - signal:strategy\n
  #     - signal:inertia-advocate\n  - signal:signal-fidelity-analyst" (every role listed)
  #   WORKED EXAMPLE (good): "- signal:pm\n  - signal:architect" (genuine handoff pair)
---
```

GATE — Phase 4 complete when ALL of the following are TRUE:
1. One file per role exists at `.craft/roles/{area}/`
2. Every file has all six top-level fields with required sub-fields
3. Every field uses exact names: `verify_questions` (not `verify`), `simplify_rules` (not `simplify`)
4. No frame field contains a task list or job description
5. No serves field restates frame
6. Every simplify_rules entry is a prohibition or elimination, not a scope description
7. Every expertise.depth names a method or technique, not a domain label only
8. No collaborates_with entry names a role absent from the full role set (no phantom names)
9. No collaborates_with lists every role in the set (no universalist entries)
10. Every domain expert has at least one inertia-response question in verify_questions

---

PHASE 5 — REGISTRY SUMMARY

Write `.craft/roles/{area}/REGISTRY.md` using this template. Fill every slot:

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
  - {name}: derived from concern "{concern}" (Phase 1 DOMAIN-ANALYSIS);
    inertia objection pre-answered: "{inertia objection from Phase 1}"
  - (repeat for each domain expert)
**Coverage gaps:** {concerns from Phase 1 not fully addressed by any role, or "none detected"}
```

FAILURE MODE (C-15): heading-only stub — a section header (`## Registry Summary`) with no required content beneath it is not a complete registry entry and fails C-10 unconditionally. The heading is structural scaffolding; the five fields are the content. A registry that contains only headings provides no audit information to the caller.

GATE — Phase 5 complete when ALL of the following are TRUE:
1. REGISTRY.md exists at `.craft/roles/{area}/REGISTRY.md`
2. `area` field is present and non-empty
3. `total_roles` count matches the actual number of role files written in Phase 4
4. Stock roles section lists all four names: pm, architect, strategy, inertia-advocate
5. Domain experts section names each expert with its Phase 1 derivation source and inertia objection
6. Coverage gaps field is present with a non-empty value (even if "none detected")

---

FINAL LINE

The last line of `REGISTRY.md` must be:

```
Generated by: /org-roles {topic} — {date}
```

Replace `{topic}` and `{date}` with actual values. Do not emit literal placeholder text.
