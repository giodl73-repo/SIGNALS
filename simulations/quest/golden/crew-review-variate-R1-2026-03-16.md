---
skill: quest-variate
skill_target: crew-review
date: 2026-03-16
round: 1
rubric: crew-review-rubric-v1-2026-03-16.md
---

# crew-review — Variate R1

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis combinations (V-04, V-05).

Registry context assumed: `.roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

---

## V-01

**Axis**: Inertia framing
**Hypothesis**: Leading with an explicit null-hypothesis mandate — before any domain review
runs — forces every downstream finding to answer the inertia case, producing a more
discriminating matrix than a neutral role-selection opening.

---

You are running `/crew-review`.

Your job: route the artifact through the org registry and produce a multi-role review matrix.

---

### Step 1 — Load the registry

Read every file in `.roles/`. Build a list of all available roles.
Do not fabricate roles not found in that directory. If `.roles/` is absent or empty,
halt and output: `ERROR: .roles/ not found. Cannot proceed.`

---

### Step 2 — Open with the Inertia Advocate

Before any domain review, the Inertia Advocate speaks first. This is not optional.

Their single mandate: **argue the strongest possible case for doing nothing.**

State the null hypothesis explicitly in their matrix row:

> "The team currently does [X] instead of this artifact. That alternative costs [Y].
> This artifact is worth adopting only if [condition]."

Fill in all three blanks from the artifact content. If the artifact does not provide
enough information to fill them, that is itself the Inertia Advocate's HIGH finding:
the artifact has not named what it replaces.

The Inertia Advocate always uses this severity logic:
- HIGH if the "do nothing" case is credible and unaddressed in the artifact
- MEDIUM if the inertia case is named but the switching cost is not quantified
- LOW if the artifact directly neutralizes the status quo argument

---

### Step 3 — Select domain reviewers

Depth rules:
- **Standard** (default): select 2–3 additional roles from the registry whose domain
  intersects the artifact type. Document each selection in one sentence.
- **`--depth deep`**: run every role in the registry after the Inertia Advocate.

Relevance rule: match each role's `orientation.frame` and `expertise.relevance` fields
against the artifact's type and subject matter. Do not select roles whose domain has
no surface in the artifact.

---

### Step 4 — Run domain reviewers

For each selected domain role:
- Apply only that role's `lens.verify` perspective
- Find something specific in the artifact — name the section, field, or component
- Do not duplicate a finding already raised by a previous reviewer
- Assign severity: HIGH (blocks commitment), MEDIUM (must resolve before ship),
  LOW (advisory, does not block)
- Write a recommendation that names what to do and where in the artifact

---

### Step 5 — Review matrix

Output the full review as a 4-column table:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Row order: Inertia Advocate first, then domain roles in selection order.

- **Role**: name from `.roles/` file
- **Findings**: specific observation tied to a named artifact surface
- **Severity**: HIGH / MEDIUM / LOW only — no other labels
- **Recommendation**: concrete action naming a specific surface or next step

---

### Step 6 — Cross-role synthesis

After the matrix, 2–3 sentences:
- Name at least one convergence: two roles that independently raised the same concern
- Name any conflict: two roles that disagree on priority or approach
- If neither convergence nor conflict exists, write: "No cross-role signals detected."

---

### Step 7 — AMEND

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Run full registry: `/crew-review [artifact] --depth deep`
> - Restrict to one domain: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-02

**Axis**: Output format
**Hypothesis**: Defining the output schema before review execution — column types, severity
vocabulary, and row constraints — eliminates format drift and makes C-02/C-03 failures
structurally impossible rather than relying on post-hoc correction.

---

You are running `/crew-review`.

Produce a structured crew review for the provided artifact. Output format is defined
before execution begins and must be followed exactly.

---

### Output schema (read before executing)

The final output is a single markdown table with this column contract:

| Column | Type | Constraints |
|--------|------|-------------|
| Role | string | Must match a filename stem in `.roles/`. Zero fabricated names. |
| Findings | string | Must name a specific artifact surface (section title, field name, diagram element, named concept). Generic observations without a named surface are invalid. |
| Severity | enum | Exactly one of: `HIGH`, `MEDIUM`, `LOW`. No other values. HIGH = blocks commitment. MEDIUM = must resolve before ship. LOW = advisory. |
| Recommendation | string | One concrete action. Must name (1) what to do and (2) where in the artifact. Generic directives ("review this section") are invalid. |

After the table: a cross-role synthesis block and an AMEND block.
These are not optional. Missing either block fails the output contract.

---

### Execution

**Phase 1 — Load**

Open `.roles/`. Read every file. Available role pool = all files found.
If directory is missing: output `ERROR: .roles/ not found.` and stop.

**Phase 2 — Scope**

- Default (standard): select 2–4 roles whose domain intersects the artifact type
- `--depth deep`: select all roles in the registry

For standard: document which roles you selected and why (one sentence each).
Relevance is determined by matching role `expertise.relevance` to artifact type.

**Phase 3 — Review**

For each selected role, produce a review. Validate each row against the output schema
before writing it:
- Role name is in `.roles/` ✓
- Finding names a specific surface ✓
- Severity is HIGH, MEDIUM, or LOW ✓
- Recommendation names what to do and where ✓

If any cell fails validation, revise it before writing the row.

**Phase 4 — Output**

Write the table. Then:

**Cross-role synthesis** (required, 2–3 sentences):
Name at least one convergence (two roles raise the same concern area) or one conflict
(two roles disagree). If genuinely absent: "No cross-role signal detected."

**AMEND** (required):

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Scope to domain: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-03

**Axis**: Phrasing register
**Hypothesis**: A conversational, directive voice ("go do X", "name the thing") reduces
prompt-following friction compared to formal procedural language, and produces crisper
finding text because the register naturally discourages hedging.

---

You are running `/crew-review`. Here is what you do:

---

**Load the org**

Go to `.roles/`. Read every file. That directory is your complete reviewer pool —
don't invent anyone who isn't there. If the directory is missing, stop and say so.

---

**Pick reviewers**

Standard run (default): pick 2 to 4 roles. Pick the ones whose job actually touches
this artifact. Write one sentence per pick explaining why them and not someone else.

`--depth deep`: everyone runs.

---

**One extra move before any domain review**

Put the Inertia Advocate in first. Their whole job is to argue for doing nothing.

Make them answer this: what does the team do today instead of this artifact? Is that
actually worse? What is the real switching cost — not the obvious one, the hidden one?

If the artifact doesn't name what it replaces, that is their HIGH finding. Name it.

---

**Run the reviews**

Go role by role. For each one:

1. What does someone in this role actually care about? (one sentence — lock the lens)
2. What does this artifact do or fail to do for them? Point to something specific —
   a section title, a named field, a diagram, a stated assumption. Don't be vague.
3. Call it HIGH, MEDIUM, or LOW. Nothing else.
   - HIGH: can't proceed without fixing this
   - MEDIUM: fix before shipping
   - LOW: good to fix, not blocking
4. Tell them exactly what to do about it and where.

---

**Write the matrix**

Once all reviews are done, write the table:

| Role | Findings | Severity | Recommendation |

Specific cells, not vague ones. Every finding names something in the artifact.
Every recommendation says what and where.

---

**Cross-role read**

After the table: did any two reviewers agree on the same thing? That's your highest-confidence
signal — name it. Did any two disagree? Name that too. If neither, say so.

---

**AMEND**

Tell them what they can do next:

> **AMEND**
> - Add a reviewer: `/crew-review [artifact] --amend add:[role-name]`
> - Run everyone: `/crew-review [artifact] --depth deep`
> - Focus on one domain: `/crew-review [artifact] --amend scope:[domain]`

---

---

## V-04

**Axis**: Role sequence + Inertia framing (combination)
**Hypothesis**: Baking the Inertia Advocate into a hard position-1 mandate in the
sequencing logic (not just a "run first" suggestion) — and deriving role ordering
from registry archetypes — produces a matrix where every subsequent domain row is
implicitly responding to the inertia frame, making C-04 (perspective differentiation)
easier to satisfy.

---

You are running `/crew-review`.

Reviews execute in a fixed sequence derived from role archetypes. Sequence is not
configurable by the user — it is structurally determined by the registry.

---

### Step 1 — Load registry

Read every file in `.roles/`. Extract each role's `archetype` field.
Build an ordered execution queue:

1. `archetype: challenger` roles — run first (includes `inertia-advocate`)
2. `archetype: product` roles — run second
3. `archetype: technical` roles — run third
4. `archetype: quality` roles — run fourth (if present)
5. All other archetypes — run last

Within each archetype group, order alphabetically by role name.

If a role has no `archetype` field, place it at the end of the queue.

If `.roles/` is missing: output `ERROR: .roles/ not found.` and stop.

---

### Step 2 — Apply depth gate

- **Standard** (default): from each archetype group, select only roles whose domain
  intersects the artifact. Exception: all `challenger` roles always run regardless of
  depth setting. Aim for 2–4 total (challengers included).
- **`--depth deep`**: run all roles in archetype order.

For standard: document your selection (one line per role, one sentence of rationale).

---

### Step 3 — Challenger bracket (always runs first)

Execute all `challenger` archetype roles before any other review. For each:

- State the null hypothesis explicitly: "The team currently does [X] instead of this.
  The cost of that alternative is [Y]. This artifact is worth acting on only if [Z]."
- Assign severity based on how credible the inertia case is:
  - HIGH: inertia case is strong and the artifact does not address it
  - MEDIUM: inertia case is named but switching cost is not quantified
  - LOW: artifact directly neutralizes the status quo

The challenger bracket closes before any product or technical review opens. Domain reviewers
implicitly inherit the inertia frame when writing their own findings.

---

### Step 4 — Domain reviews

Execute remaining roles in archetype sequence order. For each role:
- Apply only that role's `lens.verify` perspective (read from the role file)
- Name a specific artifact surface in each finding
- Do not repeat a finding already raised by a previous role
- Severity: HIGH / MEDIUM / LOW only
- Recommendation: what to do + where in the artifact

---

### Step 5 — Matrix output

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Rows appear in execution order (challengers first, then by archetype group).
Archetype group label as a row separator is optional but encouraged.

---

### Step 6 — Cross-role synthesis

2–3 sentences after the matrix:
- Name at least one convergence: two roles independently raised the same concern
- Name any conflict: roles from different archetype groups that disagree
- If none: "No cross-role signal detected."

---

### Step 7 — AMEND

> **AMEND**
> - Add a reviewer (runs in archetype sequence): `/crew-review [artifact] --amend add:[role-name]`
> - Full registry: `/crew-review [artifact] --depth deep`
> - Skip challenger bracket: `/crew-review [artifact] --amend skip:challengers` *(changes output contract)*

---

---

## V-05

**Axis**: Output format + Lifecycle emphasis (combination)
**Hypothesis**: Structuring the skill as named phases with explicit entry/exit conditions —
Load, Select, Review, Render — makes the depth-gate logic (C-06) and format contract
(C-02) self-enforcing: each phase cannot begin until the previous one satisfies its exit
condition, eliminating the most common failure modes from a single undifferentiated instruction block.

---

You are running `/crew-review`.

This skill executes in four phases. Each phase has an entry condition and an exit
condition. Do not begin a phase until its entry condition is met.

---

## PHASE 1 — LOAD

**Entry**: invoked with an artifact
**Exit**: role pool is built and verified

**L1** Open `.roles/`. Read every file in the directory.
**L2** For each file, extract: role name, archetype, `orientation.frame`, `expertise.relevance`.
**L3** If `.roles/` is missing or empty: output `ERROR: role registry unavailable.` and halt.
**L4** Role pool = all roles found. Zero roles may be invented. Pool is now locked.

---

## PHASE 2 — SELECT

**Entry**: role pool locked
**Exit**: reviewer queue finalized with rationale

**S1** Check for `--depth deep` flag:
  - Present: queue = all roles in pool. Set `depth=deep`. Skip to S4.
  - Absent: set `depth=standard`. Proceed to S2.

**S2** (Standard only) From the role pool, select roles whose domain intersects
the artifact's type and subject matter. Target: 2–4 roles total.

Relevance test: does the role's `expertise.relevance` name the artifact's namespace,
type, or subject area? If yes, include. If ambiguous, include with a note.

Exception: any role with `archetype: challenger` is always included in standard depth.

**S3** (Standard only) For each selected role, write one sentence:
`[role-name] selected: [reason tied to artifact content].`

**S4** Reviewer queue is final. Note at top of output:
`Depth: standard | deep` and `Roles: [list]`

---

## PHASE 3 — REVIEW

**Entry**: reviewer queue finalized
**Exit**: all queued roles have produced a validated review row

Execute roles in this sequence: challenger archetype first, then all others.

For each role, produce a review row. Before writing the row, validate it:

| Cell | Validation rule |
|------|----------------|
| Role | Name matches `.roles/` file — not invented |
| Findings | Names a specific artifact surface (section, field, diagram, assumption) — not generic |
| Severity | Exactly HIGH, MEDIUM, or LOW — no other values |
| Recommendation | Names what to do AND where in the artifact — not a generic directive |

If a cell fails validation: revise it before proceeding to the next role.

For challenger roles: finding must include null hypothesis — what the team does today
as an alternative to this artifact, and why that alternative might be sufficient.

---

## PHASE 4 — RENDER

**Entry**: all review rows validated
**Exit**: complete output delivered to user

**R1** Write the header block:

```
Crew Review: [artifact name or type]
Depth: standard | deep
Roles run: [list]
```

**R2** Write the review matrix:

```
| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
[one row per reviewed role, in execution order]
```

**R3** Write the cross-role synthesis block (required):

2–3 sentences. Must name:
- At least one convergence (two roles flag the same concern) **OR**
- At least one conflict (two roles disagree on priority or approach)

If genuinely absent: write "No cross-role signal detected — findings are non-overlapping."

**R4** Write the AMEND block (required):

> **AMEND**
> - Add reviewer (appends to queue): `/crew-review [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-review [artifact] --depth deep`
> - Restrict to domain: `/crew-review [artifact] --amend scope:[domain]`
> - Re-run single role: `/crew-review [artifact] --amend rerun:[role-name]`

Output complete.

---
