Good — I have full context. Writing the 5 variations now.

---

# org-roles Skill Body — Variations V-01 through V-05

**Round 1 | Single-axis first, then combined**

---

## V-01 — Axis: Role Sequence (context-first, stock second, devil-advocate last)

**Hypothesis**: Analyzing domain context before reaching for stock roles keeps domain expert derivation specific. If the LLM reads the input and derives candidates first, it generates more targeted frames than if it starts from the PM/Architect/Strategy template and then adds domain names.

---

```markdown
You are generating a typed role registry for a domain. The registry will be written
to `.roles/{area}/` as individual Markdown files — one file per role.

---

## Step 1 — Read the input

Analyze the provided context: product description, codebase, spec, or combination.
Extract the following before writing any role:

- What problem does this product/feature solve?
- What are the riskiest technical decisions in the domain?
- What domain-specific concerns appear that a generic reviewer would miss
  (e.g., data pipeline correctness, auth boundary enforcement, signal fidelity)?
- Name 2-4 candidate domain expert roles. A domain expert role is specific enough
  that its verify questions could not apply verbatim to an unrelated domain.

Record your candidates as a brief list. Do not generate files yet.

---

## Step 2 — Derive domain expert roles

For each candidate from Step 1, generate a role file. Each file must contain:

```yaml
---
name: {role-id}
version: "1.0"
archetype: {domain-expert}

orientation:
  frame: |
    {Epistemic viewpoint — how this expert sees the world.
     Must reference the specific domain concern identified in Step 1.}
  serves: |
    {Beneficiary — who or what depends on this expert's signal.
     Must be a different statement from frame, not a paraphrase.}

lens:
  verify:
    - "{Testable question 1 — answerable by reading artifacts or running code}"
    - "{Testable question 2 — domain-specific; no other role would ask this}"
    - "{Testable question 3 — references a specific behavior or measurable outcome}"
  simplify:
    - "{Constraining rule 1 — excludes something or reduces scope}"
    - "{Constraining rule 2 — not a description; an opinion with consequences}"

expertise:
  depth: |
    {List of specific competency areas for this role.}
  relevance: |
    {Which Signal namespaces or skill areas this role appears in.}

scope: workspace
collaborates_with:
  - {area}:{role-id}   # other roles in this registry only
```

---

## Step 3 — Add stock roles

After domain experts are written, add three stock roles. These are always emitted
regardless of domain. Do not modify them based on the domain input; they are stable
across all registries.

**PM role** (`pm.md`):
```yaml
orientation:
  frame: "Sees every skill from the product perspective — what does this signal mean
    for the feature decision? Is the evidence strong enough to commit?"
  serves: "Teams that need to translate artifacts into go/no-go decisions."
lens:
  verify:
    - "Does the signal address the inertia case — why would teams do nothing?"
    - "Is there a clear commitment threshold or does the signal leave the decision open?"
    - "Which namespace is still missing before we can commit?"
  simplify:
    - "If the signal doesn't change what we build, it wasn't worth gathering"
    - "Coverage without depth is noise — 3 strong signals beat 9 weak ones"
expertise:
  depth: "Feature prioritization, signal sufficiency thresholds, go/no-go framing."
  relevance: "Appears in scout, draft, review, listen, program."
scope: workspace
collaborates_with:
  - {area}:architect
  - {area}:strategy
```

**Architect role** (`architect.md`):
```yaml
orientation:
  frame: "Sees every skill through the lens of technical feasibility and system design.
    Can this feature be built given the constraints?"
  serves: "Teams that need to validate technical soundness before committing to spec."
lens:
  verify:
    - "Is technical complexity correctly estimated — not just what, but how hard?"
    - "Are system boundaries correctly identified?"
    - "Are there dependency or integration risks the PM hasn't surfaced?"
  simplify:
    - "If you can't hand-compile the spec, you can't implement it"
    - "Complexity is honest — a spec that hides difficulty will fail"
expertise:
  depth: "Technical feasibility, spec boundary definition, complexity scoring, dependency mapping."
  relevance: "Appears in scout-feasibility, draft-spec, draft-proposal, scout-requirements."
scope: workspace
collaborates_with:
  - {area}:pm
  - {area}:strategy
```

**Strategy role** (`strategy.md`):
```yaml
orientation:
  frame: "Sees every skill from the perspective of market positioning and long-term
    competitive advantage. Is this feature a wedge or a table stake?"
  serves: "Leadership and teams deciding where to place sustained bets."
lens:
  verify:
    - "Does this feature advance a defensible position or just close a gap?"
    - "What does shipping this signal to competitors?"
    - "Is the audience large enough to justify the investment?"
  simplify:
    - "A feature that doesn't change positioning isn't strategy — it's maintenance"
    - "Market share is a lagging indicator; strategic leverage is leading"
expertise:
  depth: "Market positioning, competitive moat analysis, build/buy/partner framing."
  relevance: "Appears in scout-competitors, scout-positioning, scout-market."
scope: workspace
collaborates_with:
  - {area}:pm
  - {area}:architect
```

---

## Step 4 — Add the devil-advocate (inertia-advocate) role

This role is always the last file written. It challenges every proposal in the
registry by arguing the status quo is sufficient. It is not a quality critic — it
specifically argues that doing nothing is better.

**inertia-advocate.md**:
```yaml
---
name: inertia-advocate
version: "1.0"
archetype: challenger

orientation:
  frame: "Plays the status quo. For every proposed feature or change, argues the case
    for doing nothing. Not a blocker — a calibration device. Forces the team to
    genuinely answer: why is this better than doing nothing?"
  serves: "Teams that need their inertia case stress-tested before committing.
    Every analysis must answer the inertia-advocate before proceeding."

lens:
  verify:
    - "What is the team doing today instead — and is that actually worse?"
    - "What is the true switching cost, including hidden costs?"
    - "Has the team talked to users who chose NOT to adopt, or only early adopters?"
    - "Is this solution better than the existing workaround, or just different?"
  simplify:
    - "The inertia case is always HIGH threat — burden of proof is on the feature"
    - "A workaround that exists is evidence against the feature, not neutral"
    - "If you can't name what the team does today, you don't understand inertia"

expertise:
  depth: "Status quo defense, workaround analysis, switching cost quantification,
    adoption friction modeling, null hypothesis construction."
  relevance: "Mandatory in every registry. Every scout-competitors run starts here."

scope: workspace
collaborates_with:
  - {area}:pm
  - {area}:strategy
```

---

## Step 5 — Write the registry summary

Write a `REGISTRY.md` file in `.roles/{area}/` with:

- Area name and date
- Total role count
- Which roles are stock (PM, Architect, Strategy, inertia-advocate)
- Which roles are context-derived domain experts (names + one-line frame summary)
- Any coverage gaps detected (e.g., "No security role — consider adding if auth is in scope")

---

## Output

Write all files to `.roles/{area}/` where `{area}` is derived from the domain
context (lowercase, hyphen-separated, descriptive). Never use `default` as the area name.

File per role. No bundling. YAML frontmatter in each file.
```

---

## V-02 — Axis: Phrasing Register (conversational / imperative)

**Hypothesis**: Terse, imperative phrasing with explicit "do/don't" rules reduces hallucinated filler prose and keeps schema compliance higher. An LLM following commands produces fewer field omissions than one following descriptive guidance.

---

```markdown
Generate a role registry for the domain described below. Write one Markdown file per
role to `.roles/{area}/`. Every role gets exactly these six fields — no more,
no fewer.

---

## The schema. Follow it exactly.

```yaml
---
name: {slug}
version: "1.0"
archetype: {type}

orientation:
  frame: "How this role sees the world. One sentence. Epistemic viewpoint."
  serves: "Who depends on this role's signal. One sentence. NOT a restatement of frame."

lens:
  verify:
    - "Testable question. Must be answerable by reading an artifact or running code."
    - "Domain-specific. No other role in this registry would ask this."
    - "References a specific behavior, boundary, or measurable outcome."
  simplify:
    - "A rule that excludes or constrains something. Not a description."
    - "Opinionated. Has consequences if broken."

expertise:
  depth: "Specific competencies. Comma-separated noun phrases."
  relevance: "Which Signal namespaces this role shows up in."

scope: workspace
collaborates_with:
  - {area}:{role}   # only names that exist in this registry
```

---

## What to generate

**Read the domain input.** Ask yourself: what domain-specific risks exist here that a
PM, Architect, or Strategy role would not naturally surface? Each answer is a domain
expert candidate.

**Always generate these four roles** (no exceptions):
1. `pm.md` — product perspective, go/no-go decisions, signal sufficiency
2. `architect.md` — technical feasibility, spec boundaries, complexity
3. `strategy.md` — market positioning, competitive moat, build/buy/partner
4. `inertia-advocate.md` — status quo defender (see below)

**Generate 2-4 domain expert roles** derived from the input. A domain expert is valid
if and only if its verify questions are specific to this domain and would fail if
applied to an unrelated product.

---

## The inertia-advocate is mandatory and must come first in your thinking

Before you write any other role, write the inertia-advocate. It sets the standard
every other role must clear. The inertia-advocate's job is exactly one thing:

> Argue that doing nothing is better than the proposed feature.

Its verify questions must include at least one of the form:
"Why is the current approach insufficient?" or "What is the team doing today instead?"

This is not a generic skeptic role. It is a status-quo specialist. If your
inertia-advocate could appear in any project, it is wrong. Rewrite it.

---

## Do not do these things

- Do not use `default` as the area name in the output path
- Do not bundle multiple roles into one file
- Do not use `serves` as a restatement of `frame`
- Do not list collaborators who don't exist in this registry
- Do not write verify questions that are rhetorical or unanswerable
- Do not write simplify rules that describe rather than constrain

---

## Output

1. One `.md` file per role in `.roles/{area}/`
2. One `REGISTRY.md` in `.roles/{area}/` — lists area, date, role count,
   stock vs. derived breakdown, any gaps

Derive `{area}` from the domain input. It should be specific enough that someone
reading the directory name knows the domain (e.g., `signal-evidence`, `crm-sync`,
`auth-gateway`).
```

---

## V-03 — Axis: Inertia Framing (devil-advocate leads and anchors the registry)

**Hypothesis**: Opening with the inertia case before any constructive role forces every subsequent role's verify questions to implicitly answer it. The inertia-advocate becomes the benchmark; other roles must clear it. This produces more differentiated lenses than when inertia is just another slot at the end.

---

```markdown
You are generating a typed role registry. Before you write a single role, you must
name the enemy.

---

## Phase 0 — Name the enemy

The primary competitor for any feature is not another product. It is inertia.
Inertia is the argument that doing nothing — continuing with the current workflow,
the existing workaround, the status quo — is better than adopting the proposed feature.

Before you analyze the domain or write any role, answer:

1. What is the team doing today instead of this feature?
2. What is the switching cost to adopt it?
3. What does the team lose by changing?

Write these three answers in one short paragraph. This is your **inertia statement**.
Every role you generate will be evaluated against it: does this role's lens surface
evidence that can answer or refute the inertia statement?

---

## Phase 1 — Write the inertia-advocate role

The inertia-advocate is the first role file you write. It personifies the inertia
statement. Its verify questions are direct challenges to every proposal:

```yaml
---
name: inertia-advocate
version: "1.0"
archetype: challenger

orientation:
  frame: |
    Plays the status quo. For every proposed feature or change, argues the case
    for doing nothing. Not a blocker — a calibration device. Forces the team to
    answer: why is this better than doing nothing?
  serves: |
    Teams that need their inertia case stress-tested before committing.
    Every Signal analysis must answer the inertia-advocate before proceeding.

lens:
  verify:
    - "What is the team doing today instead — and is that actually worse?"
    - "What is the true switching cost, including hidden costs?"
    - "Has the team talked to users who chose NOT to adopt, or only enthusiasts?"
    - "Is this solution better than the existing workaround, or just different?"
    - "{Add one domain-specific question derived from your Phase 0 inertia statement}"
  simplify:
    - "The inertia case is always HIGH threat — burden of proof is on the feature"
    - "A workaround that exists is evidence against the feature, not neutral"
    - "If you can't name what the team does today, you don't understand inertia"

expertise:
  depth: |
    Status quo defense, workaround analysis, switching cost quantification,
    adoption friction modeling, null hypothesis construction.
  relevance: |
    Mandatory in every registry. Runs before every scout-competitors analysis.

scope: workspace
collaborates_with:
  - {area}:pm
  - {area}:strategy
```

---

## Phase 2 — Derive domain expert roles

With the inertia statement in mind, analyze the domain input. For each domain expert
you derive, ask: **does this role's lens produce evidence that can answer the inertia
statement?** If not, the role is decorative. A role that can't address inertia is not
a Signal role — it is a title.

Generate 2-4 domain expert roles. For each:

- `frame`: how this expert sees the world (epistemic viewpoint, not job title)
- `serves`: who depends on their signal (beneficiary, not restatement of frame)
- `verify`: at least two questions that are specific to this domain AND produce
  evidence relevant to the inertia statement
- `simplify`: at least two constraining rules (not descriptions)
- `expertise.depth`: specific competency areas
- `expertise.relevance`: which Signal namespaces use this role
- `collaborates_with`: only names present in this registry

Schema:
```yaml
---
name: {slug}
version: "1.0"
archetype: domain-expert

orientation:
  frame: "..."
  serves: "..."

lens:
  verify:
    - "..."
    - "..."
    - "..."
  simplify:
    - "..."
    - "..."

expertise:
  depth: "..."
  relevance: "..."

scope: workspace
collaborates_with:
  - {area}:{role}
```

---

## Phase 3 — Add stock roles

Always add PM, Architect, and Strategy. These are not derived from context — they are
fixed. Add any domain-specific verify question(s) to each that are motivated by the
inertia statement from Phase 0.

**PM** (`pm.md`):
- frame: product perspective, go/no-go decisions, signal sufficiency
- verify must include: "Does the signal address the inertia case — why would teams do nothing?"
- simplify must include: "The primary competitor is always inertia — name it first"

**Architect** (`architect.md`):
- frame: technical feasibility, system boundaries, complexity
- verify must include: "Are there integration risks that make the status quo safer?"
- simplify must include: "Complexity is honest — a spec that hides difficulty will fail"

**Strategy** (`strategy.md`):
- frame: market positioning, competitive moat, build/buy/partner
- verify must include: "Is the inertia case actually a market signal about weak demand?"
- simplify must include: "A feature that doesn't change positioning is maintenance"

---

## Phase 4 — Collaborates_with audit

Before writing files:
- List every role name you are about to emit
- Check every `collaborates_with` list against that list
- Remove any cross-reference to a role not in the list

---

## Phase 5 — Write all files

Write to `.roles/{area}/` where `{area}` is derived from domain context.
One file per role. Include a `REGISTRY.md` summary:

```markdown
# Role Registry — {area}

Date: {date}
Total roles: {n}
Stock roles: pm, architect, strategy, inertia-advocate
Derived roles: {names and one-line frame summary}
Inertia statement: {your Phase 0 paragraph}
Coverage gaps: {any domain concern not covered by any role}
```
```

---

## V-04 — Combined Axes: Output Format + Role Sequence (table-enumeration → file generation)

**Hypothesis**: A structured enumeration table before file generation forces explicit coverage accounting. The LLM commits to a role list and their key properties before writing, which catches schema drift and missing C-05 domain experts earlier than going straight to file generation.

---

```markdown
You are generating a typed role registry for the domain described in the input.
Output destination: `.roles/{area}/` — one Markdown file per role.

Work in two passes: enumerate first, then generate.

---

## Pass 1 — Enumerate the registry

Analyze the domain input and produce a coverage table before writing any files.

| Slot | Role ID | Archetype | Source | Frame (one phrase) | Key verify concern |
|------|---------|-----------|--------|--------------------|--------------------|
| S-01 | pm | stock | always | product go/no-go | signal sufficiency |
| S-02 | architect | stock | always | technical feasibility | spec boundaries |
| S-03 | strategy | stock | always | competitive positioning | moat vs. gap |
| S-04 | inertia-advocate | challenger | always | status quo defense | switching cost |
| D-01 | {name} | domain-expert | derived: {why} | {frame phrase} | {key concern} |
| D-02 | {name} | domain-expert | derived: {why} | {frame phrase} | {key concern} |
| ... | ... | ... | ... | ... | ... |

Rules for Pass 1:
- Stock slots S-01 through S-04 are always present. Do not omit them.
- Domain slots D-01 onward must be derived from the input. Write the "derived: {why}"
  column by naming the specific artifact, codebase concern, or spec section that
  motivated this role. If you cannot fill in "derived: why", the role is generic — drop it.
- Minimum 2 domain slots. Maximum 4.
- Review the table before proceeding. Ask: does every domain slot have a unique key
  verify concern that no stock role would surface?

---

## Pass 2 — Generate role files

For each row in the Pass 1 table, generate a role file using this schema:

```yaml
---
name: {role-id}        # from Pass 1 table, slug format
version: "1.0"
archetype: {archetype} # from Pass 1 table

orientation:
  frame: |
    {Expand the "Frame (one phrase)" from Pass 1 into 1-2 sentences.
     Epistemic viewpoint — how this expert sees the world.}
  serves: |
    {Name the beneficiary. NOT a restatement of frame.
     Answers: who depends on this role's signal?}

lens:
  verify:
    - "{Question 1: testable, references artifact or behavior}"
    - "{Question 2: specific to this domain — fails if applied elsewhere}"
    - "{Question 3: derived from key verify concern in Pass 1 table}"
  simplify:
    - "{Rule 1: constraining — excludes or reduces scope}"
    - "{Rule 2: opinionated — has consequences if broken}"

expertise:
  depth: "{Competency list for this role}"
  relevance: "{Signal namespaces where this role is useful}"

scope: workspace
collaborates_with:
  - {area}:{role-id}    # only IDs from Pass 1 table
```

Generation order: stock roles first (pm, architect, strategy), then domain experts
in D-01 order, then inertia-advocate last.

---

## Pass 2 — Schema validation checkpoint

After generating all files, verify:

- [ ] Every file has all 6 top-level fields
- [ ] Every file's `orientation.frame` is a viewpoint, not a job description
- [ ] Every file's `orientation.serves` is a beneficiary, not a paraphrase of frame
- [ ] Every `verify` question is answerable (not rhetorical)
- [ ] Every `simplify` rule constrains rather than describes
- [ ] Every `collaborates_with` entry is in the Pass 1 table

If any check fails, fix the file before proceeding.

---

## Output

All files in `.roles/{area}/`. Plus `REGISTRY.md` which is the Pass 1 table
extended with the file path for each role:

```markdown
# Role Registry — {area}

Generated: {date}

| Slot | Role ID | Archetype | Source | File |
|------|---------|-----------|--------|------|
| S-01 | pm | stock | always | pm.md |
| S-02 | architect | stock | always | architect.md |
| S-03 | strategy | stock | always | strategy.md |
| S-04 | inertia-advocate | challenger | always | inertia-advocate.md |
| D-01 | {name} | domain-expert | {why} | {name}.md |
...

## Coverage gaps
{Any domain concerns not represented in the role set}
```
```

---

## V-05 — Combined Axes: Lifecycle Emphasis + Formal Register

**Hypothesis**: Explicit phase headers with named entry/exit criteria behave like typed interfaces — they catch schema violations at phase boundaries rather than at the end. A formal register signals to the LLM that it is producing a structured artifact (not conversational text), which reduces prose inflation in the role files.

---

```markdown
## Skill: org-roles

**Purpose**: Generate a typed role registry for a domain.

**Input**: Product description, codebase excerpt, or feature specification.

**Output**: `.roles/{area}/` — one `.md` file per role, one `REGISTRY.md` summary.

**Invariants** (enforced at every phase boundary):
1. Stock roles PM, Architect, Strategy are always present in the output set.
2. The inertia-advocate role is always present in the output set.
3. Every role file contains all six required fields and their sub-fields.
4. The `collaborates_with` field references only roles present in the output set.
5. At least one domain expert role is derived specifically from the input context.

---

### Phase 1 — Domain Analysis

**Entry**: Input context received.
**Exit criteria**: Domain profile written; role candidate list with at least 2 domain-expert candidates identified; inertia statement drafted.

Tasks:
1. Extract the domain's primary problem and the most critical technical risk.
2. Identify 2-4 domain-specific expert perspectives that would not be surfaced by
   the three stock roles. For each candidate, record:
   - The domain concern motivating the role (specific, not generic)
   - The key verify question unique to this role
3. Draft the inertia statement: what is the team doing today, what would it cost
   to change, what would be lost by adopting the proposed feature?

Output of this phase: inline analysis (not a file). Do not write role files yet.

---

### Phase 2 — Inertia-Advocate Construction

**Entry**: Inertia statement from Phase 1.
**Exit criteria**: `inertia-advocate.md` is complete and satisfies Invariants 3 and 4.

Construct the inertia-advocate role file. This role's purpose is singular and
non-negotiable: argue that the status quo is sufficient. It is not a quality reviewer.
It is not a risk auditor. It challenges every proposal by defending doing nothing.

Required verify questions (in addition to any domain-specific additions):
- "What is the team doing today instead — and is that actually worse?"
- "What is the true switching cost, including hidden costs not in the spec?"
- "Has the team spoken with users who chose not to adopt, or only early adopters?"

Required simplify rules:
- "The inertia case is always HIGH threat — burden of proof is on the feature"
- "A workaround that exists is evidence against the feature, not neutral"

Schema:
```yaml
---
name: inertia-advocate
version: "1.0"
archetype: challenger

orientation:
  frame: |
    {Phase 1 inertia statement converted to epistemic viewpoint.}
  serves: |
    {Teams that need inertia stress-tested before committing.}

lens:
  verify:
    - "What is the team doing today instead — and is that actually worse?"
    - "What is the true switching cost, including hidden costs?"
    - "Has the team talked to non-adopters, not only early enthusiasts?"
    - "{Domain-specific inertia question from Phase 1}"
  simplify:
    - "The inertia case is always HIGH threat — burden of proof is on the feature"
    - "A workaround that exists is evidence against the feature, not neutral"
    - "If you cannot name what the team does today, you do not understand inertia"

expertise:
  depth: |
    Status quo defense, workaround analysis, switching cost quantification,
    adoption friction modeling, null hypothesis construction.
  relevance: |
    Mandatory in every registry. Runs first in scout-competitors analysis.

scope: workspace
collaborates_with:
  - {area}:pm
  - {area}:strategy
```

---

### Phase 3 — Domain Expert Role Construction

**Entry**: Domain candidate list from Phase 1.
**Exit criteria**: All derived domain expert role files complete and satisfy Invariants 3, 4, 5.

For each domain-expert candidate, construct a role file using this schema:

```yaml
---
name: {domain-slug}
version: "1.0"
archetype: domain-expert

orientation:
  frame: |
    {Epistemic viewpoint specific to this domain concern.
     Must be non-transferable — it would fail if applied to an unrelated domain.}
  serves: |
    {Beneficiary of this role's signal. Distinct from frame.}

lens:
  verify:
    - "{Testable question 1 — references artifacts or measurable outcomes}"
    - "{Testable question 2 — would only this role ask this, not PM or Architect}"
    - "{Testable question 3 — specific to domain concern identified in Phase 1}"
  simplify:
    - "{Constraining rule 1 — reduces scope or excludes a failure mode}"
    - "{Constraining rule 2 — opinionated, with consequences if broken}"

expertise:
  depth: |
    {Specific competencies. Noun phrases.}
  relevance: |
    {Signal namespaces where this role's frame is useful.}

scope: workspace
collaborates_with:
  - {area}:{role}   # only roles in this output set
```

Verification before proceeding:
- Does each role's `frame` contain a domain-specific term from Phase 1?
- Are any two roles' verify questions substantially overlapping? If so, merge or
  differentiate them.

---

### Phase 4 — Stock Role Construction

**Entry**: Domain expert roles complete.
**Exit criteria**: `pm.md`, `architect.md`, `strategy.md` written; all satisfy Invariant 3.

Construct the three stock roles. These are stable across all registries; domain input
should not alter their frames, but may inform one domain-specific verify question each.

**pm.md**:
```yaml
orientation:
  frame: "Sees every skill from the product perspective — does this signal justify
    the cost of building? Is the inertia case genuinely addressed?"
  serves: "Teams that need to translate artifacts into go/no-go decisions."
lens:
  verify:
    - "Does the signal address the inertia case — why would teams do nothing?"
    - "Is there a clear commitment threshold or does the signal leave the decision open?"
    - "Which namespace is still missing before we can commit?"
    - "{Optional: one domain-specific signal sufficiency question}"
  simplify:
    - "If the signal doesn't change what we build, it was not worth gathering"
    - "The primary competitor is always inertia — name it before anything else"
    - "Coverage without depth is noise — three strong signals beat nine weak ones"
expertise:
  depth: "Feature prioritization, signal sufficiency thresholds, go/no-go framing,
    inertia quantification, namespace coverage assessment."
  relevance: "scout, draft, review, listen, program"
scope: workspace
collaborates_with:
  - {area}:architect
  - {area}:strategy
  - {area}:inertia-advocate
```

**architect.md**:
```yaml
orientation:
  frame: "Sees every skill through the lens of technical feasibility and system design.
    Can this feature be built within the given constraints?"
  serves: "Teams that need to validate technical soundness before committing to spec."
lens:
  verify:
    - "Is technical complexity correctly estimated — not just what, but how hard?"
    - "Are system boundaries correctly identified in the spec?"
    - "Are there dependency or integration risks not visible to the PM?"
    - "{Optional: one domain-specific architectural concern}"
  simplify:
    - "If you cannot hand-compile the spec, you cannot implement it"
    - "Complexity is honest — a spec that hides difficulty will fail in build"
expertise:
  depth: "Technical feasibility, spec boundary definition, complexity scoring,
    dependency mapping, build-vs-buy analysis."
  relevance: "scout-feasibility, draft-spec, draft-proposal, scout-requirements"
scope: workspace
collaborates_with:
  - {area}:pm
  - {area}:strategy
```

**strategy.md**:
```yaml
orientation:
  frame: "Sees every skill from the perspective of market positioning and long-term
    competitive advantage. Is this feature a wedge or a table stake?"
  serves: "Leadership and teams deciding where to place sustained investment bets."
lens:
  verify:
    - "Does this feature advance a defensible position or merely close a parity gap?"
    - "What does shipping this signal to competitors?"
    - "Is the inertia case actually a market signal about weak demand?"
  simplify:
    - "A feature that does not change positioning is maintenance, not strategy"
    - "Market share is a lagging indicator — strategic leverage is the leading one"
expertise:
  depth: "Market positioning, competitive moat analysis, build/buy/partner framing,
    wedge vs. table-stake classification."
  relevance: "scout-competitors, scout-positioning, scout-market"
scope: workspace
collaborates_with:
  - {area}:pm
  - {area}:architect
  - {area}:inertia-advocate
```

---

### Phase 5 — Registry Summary and File Output

**Entry**: All role files constructed and verified against Invariants 1-5.
**Exit criteria**: All files written to `.roles/{area}/`; `REGISTRY.md` present.

Determine `{area}`: derive from domain input using lowercase, hyphen-separated terms
specific to this domain. Reject `default`, `general`, `roles`, or any area name that
could apply to an unrelated project.

Write all files. Then write `REGISTRY.md`:

```markdown
# Role Registry — {area}

Generated: {date}

## Stock Roles (always present)
| Role | File | Purpose |
|------|------|---------|
| PM | pm.md | Product go/no-go, signal sufficiency |
| Architect | architect.md | Technical feasibility, spec boundaries |
| Strategy | strategy.md | Market positioning, competitive moat |
| Inertia-Advocate | inertia-advocate.md | Status quo defense, switching cost |

## Domain Expert Roles (derived from context)
| Role | File | Domain Concern | Phase 1 Source |
|------|------|----------------|----------------|
| {name} | {file} | {concern} | {artifact or spec section} |

## Inertia Statement
{Phase 1 inertia statement verbatim}

## Coverage Gaps
{Any domain concern identified in Phase 1 that is not represented in any role}
{If none: "No gaps detected."}
```
```

---

## Variation Summary

| ID | Primary Axis | Secondary Axis | Hypothesis |
|----|-------------|----------------|------------|
| V-01 | Role sequence: context-first → stock → devil-advocate last | — | Domain-first derivation produces more specific expert frames |
| V-02 | Phrasing register: imperative / do-not list | — | Commands reduce schema drift and filler prose |
| V-03 | Inertia framing: devil-advocate anchors the entire registry | — | Inertia-first forces other roles to address it explicitly |
| V-04 | Output format: table enumeration → file generation | Role sequence: stock before domain experts | Pre-commit table catches coverage gaps before file write |
| V-05 | Lifecycle emphasis: explicit phase gates with entry/exit criteria | Formal register | Phase boundaries catch invariant violations early |
