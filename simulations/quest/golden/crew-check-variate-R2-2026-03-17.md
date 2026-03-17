---
skill: quest-variate
skill_target: crew-check
date: 2026-03-17
round: 2
rubric: crew-check-rubric-v2-2026-03-17.md
---

# crew-check — Variate R2

5 complete prompt body variations for the `crew-check` skill.
Single-axis first (V-01 through V-03), then two-axis combinations (V-04, V-05).

Registry context assumed: `.craft/roles/signal/` contains `inertia-advocate.md`,
`pm.md`, `architect.md` (and whatever else the workspace adds).

Rubric v2 reminder:
- Essential (must-pass): C-01 role source, C-02 matrix structure, C-03 perspective fidelity,
  C-04 depth compliance, C-05 severity presence
- Recommended: C-06 finding specificity, C-07 recommendation actionability, C-08 severity calibration
- Aspirational (v2 additions): C-09 cross-role synthesis, C-10 AMEND responsiveness,
  C-11 lens-anchoring step, C-12 severity calibration contract, C-13 challenger-first sequencing

Design intent for R2: All five variations structurally enforce C-11, C-12, and C-13.
R1-V-02 failed C-11 because it had no lens-quote step. R2 has no variation that omits it.

---

## V-01

**Axis**: Inertia framing (inertia-hypothesis block as pre-review gate)
**Hypothesis**: Requiring a standalone inertia block as the *first output* — before role
selection even begins — forces the entire review to take place against a concrete switching-cost
frame. Every domain reviewer who reads "the team currently does X and it costs Y" will calibrate
severity against that baseline rather than an abstract scale. C-13 (challenger-first) becomes a
structural property, not a reminder; C-12 (severity calibration) is seeded at the top rather than
defined mid-execution.

---

You are running `/crew-check`.

Your task: pass the provided artifact through the registered org roles and produce a multi-role
review matrix. Before any role runs, the inertia case is established. Everything else builds on it.

---

### Step 1 — Load the registry

Read every file in `.craft/roles/`. Build the role pool from only what you find there.
Do not add roles not present in that directory.

If `.craft/roles/` is absent or empty: output `ERROR: .craft/roles/ not found. Halting.`

For each role record: name, archetype, `orientation.frame`, `expertise.relevance`.

---

### Step 2 — Inertia block (required before any review)

Before selecting reviewers, produce this block. It is the first thing written in the output.

```
## Inertia Case

Status quo: [What does the team currently do instead of this artifact?
             Name the existing tool, process, document, or practice being displaced.]

Switching cost: [What does it cost to adopt this artifact?
                 State in concrete terms: time, process change, ramp-up, or risk.]

Tipping condition: [Under what specific condition is acting on this artifact
                    worth the switching cost? Name the threshold.]
```

Rules:
- All three fields must be filled from artifact content.
- If the artifact does not name what it replaces: fill Status quo as
  `"Not stated in artifact — this is a HIGH-severity gap."` The inertia case being
  unknown is itself the most important finding in the review.
- This block sets the severity baseline. A finding is HIGH only if it is worse than
  or equally urgent as the inertia gap identified here.

---

### Step 3 — Determine depth and select reviewers

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one sentence per selection explaining why this role over others for this artifact.

**`--depth deep`**: Select all roles. No selection rationale needed.

Challenger archetype roles are always included regardless of relevance score.

---

### Step 4 — Severity contract

Before running any reviewer, lock this scale. Use it for every row without deviation.

| Label | Operational meaning |
|-------|---------------------|
| HIGH | Blocks commitment or ship decision — must resolve before committing resources |
| MEDIUM | Must resolve before shipping — does not block commitment |
| LOW | Advisory — fix if time permits without affecting commitment or ship |

No other severity values are valid. Calibrate against the inertia block established in Step 2.

---

### Step 5 — Run each reviewer

For each selected role, in this order (challenger roles first, then others):

**a. Anchor the lens**
Quote or paraphrase one line from this role's `orientation.frame` or `lens.verify`.
This sentence defines what the role cares about for *this* review.
Do not skip this step. A review without a lens anchor is invalid.

**b. Find**
What does the artifact do or fail to do under this lens?
Name the specific artifact surface: section heading, field name, stated assumption,
diagram label. A finding without a named surface fails the specificity check.

**c. Assign severity**
Apply the contract from Step 4. Ask: is this worse than or as urgent as the inertia gap?

**d. Recommend**
One concrete action: (1) what to do and (2) where in the artifact.
Not "improve this area." A recommendation without a location fails the actionability check.

Challenger roles: the Finding must include a reference to the inertia block.
State whether this finding *amplifies*, *contradicts*, or is *independent of* the status-quo case.

---

### Step 6 — Review matrix

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Rows appear in execution order: challenger rows first, then domain roles.

---

### Step 7 — Cross-role synthesis

2–3 sentences after the matrix:
- Name at least one convergence: two roles independently flagged the same concern area.
- Name any conflict: roles that assign different severity to the same artifact surface.
- If neither: "No cross-role signal detected."

---

### Step 8 — AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]` *(inserted in archetype sequence)*
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run inertia block only: `/crew-check [artifact] --amend rerun:inertia`
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`

---

---

## V-02

**Axis**: Phrasing register (conversational coaching voice)
**Hypothesis**: A second-person coaching register — "Before you write the finding, pause
and quote the role's orientation frame" — produces better C-11 (lens-anchoring) compliance
than SHALL-language mandates, because the coaching voice frames lens-anchoring as a thinking
discipline rather than a syntax check. Models that treat SHALL as a formatting directive will
paste a token quote; models responding to coaching language are more likely to actually engage
with the orientation content and let it shape the finding.

---

You are running `/crew-check`.

You're about to run an artifact through the registered org roles and produce a review matrix.
Think of this as facilitating a real review: each role brings a distinct perspective, and
your job is to let each perspective speak for itself — not collapse everything into a single
generic voice.

---

### Getting started — load the roles

Open `.craft/roles/` and read every file there.
Those files are your reviewer pool. Don't invent roles that aren't in the directory.

If the directory is missing or empty, stop and say: `ERROR: .craft/roles/ not found.`

For each file, note: the role's name, archetype, what they care about (their
`orientation.frame`), and what domain they cover (`expertise.relevance`).

---

### Who reviews this artifact?

**Standard run** (default): Pick 2–4 roles whose domain touches the artifact's subject.
For each one, write a single sentence: *why this reviewer for this artifact specifically?*
Always include any role with `archetype: challenger` — their job is to ask whether this
artifact is worth doing at all.

**`--depth deep`**: Include every role from the directory. No need to explain each selection.

---

### Before you start each review — establish the severity baseline

Here's the scale you'll use. Read it once. Use it consistently for every row.

- **HIGH** — This blocks a commitment or ship decision. It cannot be deferred.
- **MEDIUM** — This must be resolved before shipping, but doesn't block making the commitment.
- **LOW** — Worth fixing if there's time. Won't hold up commitment or ship.

Stick to exactly these three labels throughout. If something feels "HIGH-ish" — it's HIGH.
The scale is intentionally small. Calibration matters more than granularity.

---

### Running each review

Work through your selected roles in this order: challenger archetype roles first, then the
rest of the selected reviewers.

For each role, walk through four steps — in order, without skipping:

**Step 1: Find their voice**
Before you write anything else, read this role's `orientation.frame` or `lens.verify`.
Pick one line — quote it or paraphrase it tightly — that captures what this role
actually cares about. Write it down. This is the lens for everything that follows.
If you haven't done this step, you're not ready to write the finding.

**Step 2: Look at the artifact through that lens**
What does this reviewer see? Find something specific — not a vague impression, but
a named surface: a section heading, a field, a stated assumption, a design decision.
If you can't name where in the artifact the concern lives, the finding isn't ready yet.

**Step 3: Calibrate severity**
Use the scale above. Challenger roles in particular: is the status quo actually worse
than what this artifact proposes? Be honest. If the artifact doesn't name what it
replaces, that's a HIGH — you can't argue for a switch without naming what you're
switching from.

**Step 4: Give a concrete recommendation**
Tell the author what to do and where to do it. Not "address this concern" —
something like "add a switching-cost comparison to the Motivation section."
If your recommendation doesn't name a location, it isn't concrete enough yet.

---

### Review matrix

Once you've worked through all reviewers, write the matrix:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

Rows appear in execution order: challengers first, domain roles after.

---

### What did the reviewers agree on?

After the matrix, 2–3 sentences:
- Where did two or more reviewers land on the same concern independently?
- Did any reviewers disagree on how serious something is?
- If neither: "No cross-role signal detected."

---

### Want to go further?

> **AMEND**
> - Add a reviewer: `/crew-check [artifact] --amend add:[role-name]` *(slot into sequence)*
> - Run every role: `/crew-check [artifact] --depth deep`
> - Re-run one reviewer: `/crew-check [artifact] --amend rerun:[role-name]`
> - Narrow to a domain: `/crew-check [artifact] --amend scope:[domain]`

---

---

## V-03

**Axis**: Output format (severity-sorted matrix with numeric score column)
**Hypothesis**: Adding a numeric severity column (HIGH=3, MEDIUM=2, LOW=1) and
sorting the output matrix by score descending produces better C-12 (severity calibration
contract) compliance, because the sorting step forces the model to resolve calibration
ambiguity *before* rendering: a matrix that cannot be sorted has inconsistent values.
Numeric totals also give the human reader an instant prioritization signal that the
pure-label matrix does not provide.

---

You are running `/crew-check`.

Your task: run the provided artifact through the registered org roles and produce a
review matrix sorted by severity — highest risks first. The output uses a numeric
severity score to enable consistent calibration and automatic ordering.

---

### Step 1 — Load the registry

Read every file in `.craft/roles/`. Build the role pool from only what you find there.
Do not add roles not present in that directory.

If `.craft/roles/` is absent or empty: output `ERROR: .craft/roles/ not found. Halting.`

For each role record: name, archetype, `orientation.frame`, `expertise.relevance`.

---

### Step 2 — Select reviewers

**Standard (default)**: Select 2–4 roles whose domain intersects the artifact type.
Write one sentence per selection explaining why this role for this artifact.
Challenger archetype roles are always included.

**`--depth deep`**: Select all roles. No rationale needed.

---

### Step 3 — Severity scoring contract

Before running any reviewer, lock this scale:

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision |
| MEDIUM | 2 | Must resolve before shipping; does not block commitment |
| LOW | 1 | Advisory; fix if time permits |

Use exactly these labels and scores. Assign the *label* in the review; the *score* is
used for sorting only. No scores other than 3, 2, 1 are valid.

---

### Step 4 — Run each reviewer

**Challenger archetype roles run first.** For all others, order alphabetically.

For each role:

**a. Anchor the lens**
Quote or paraphrase one line from this role's `orientation.frame` or `lens.verify`.
This sentence defines the reviewing perspective. Do not proceed to the finding without it.

**b. Find**
Locate a specific artifact surface this lens would flag: a section heading, a named
field, a diagram element, or a stated assumption. No unnamed surfaces.

For challenger roles: name the null hypothesis — what the team currently does instead
of this artifact, and whether that alternative is demonstrably worse.

**c. Score severity**
Apply the contract from Step 3. Assign both the label and score internally;
only the label appears in the matrix.

**d. Recommend**
One concrete action: what to do and where in the artifact.

---

### Step 5 — Review matrix (sorted by severity score descending)

After all reviews are complete, order rows by severity score: 3 first, then 2, then 1.
Within the same score, challenger roles appear before domain roles.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

*Rows sorted: HIGH (score 3) first, then MEDIUM (score 2), then LOW (score 1).*

---

### Step 6 — Priority summary

After the matrix, one line per severity tier:

```
HIGH (score 3): [N] finding(s) — [one-phrase summary of the blocking concern, or "none"]
MEDIUM (score 2): [N] finding(s) — [one-phrase summary, or "none"]
LOW (score 1): [N] finding(s) — [one-phrase summary, or "none"]
```

---

### Step 7 — Cross-role synthesis

2–3 sentences:
- Name at least one convergence (two roles flagged the same concern area).
- Name any conflict (two roles scored the same surface differently).
- If neither: "No cross-role signal detected."

---

### Step 8 — AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Show unsorted matrix: `/crew-check [artifact] --amend unsorted`

---

---

## V-04

**Axes**: Inertia framing + Output format (combination)
**Hypothesis**: Combining a mandatory inertia hypothesis block with a severity-sorted
matrix creates a dual structural guarantee for v2's new criteria: C-13 (challenger-first)
is met by the pre-review inertia block which cannot be skipped; C-12 (severity calibration
contract) is reinforced by the sort, which forces resolution of calibration ambiguity before
rendering. The two mechanisms reinforce each other — the inertia block establishes what HIGH
*means concretely* (worse than the status quo), and the sort then operationalizes that meaning
by pushing those findings to the top of the output.

---

You are running `/crew-check`.

Your task: run the provided artifact through the registered org roles and produce a severity-sorted
review matrix. Before any role runs, the inertia case is documented. Severity is calibrated
against that baseline throughout.

---

### Stage 1 — Load the registry

Read every file in `.craft/roles/`. Role pool = all files discovered. No invented roles.

If `.craft/roles/` missing: `ERROR: .craft/roles/ not found.` Halt.

For each role: name, archetype, `orientation.frame`, `expertise.relevance`.

---

### Stage 2 — Inertia block (first output, required)

Write this block before selecting reviewers or running any role. It is the header of the output.

```
## Inertia Case

Status quo: [What does the team currently do instead of this artifact?]

Switching cost: [What effort does adoption require? Time, process change, ramp-up, risk.]

Tipping condition: [What specific threshold makes acting on this artifact worth the cost?]
```

Fill all three fields from artifact content.

If the artifact does not name what it replaces:
- Status quo: `"Not stated. This is a HIGH-severity gap — an artifact cannot justify adoption
  costs it has not acknowledged."`
- This gap is automatically the highest-severity finding in the run.

This block defines the HIGH bar: a finding is HIGH only if it is at least as urgent as an
unaddressed inertia gap.

---

### Stage 3 — Severity contract

Lock this before running any reviewer. Apply without deviation.

| Label | Score | Operational meaning |
|-------|-------|---------------------|
| HIGH | 3 | Blocks commitment or ship decision. At least as urgent as the inertia gap. |
| MEDIUM | 2 | Must resolve before shipping. Does not block commitment. |
| LOW | 1 | Advisory. Fix if time permits. |

---

### Stage 4 — Select reviewers

**Standard**: Select 2–4 roles whose `expertise.relevance` intersects the artifact type.
One rationale sentence per selection. Challenger archetype roles always included.

**`--depth deep`**: Select all roles. No rationale required.

---

### Stage 5 — Run each reviewer

Challenger archetype roles run first. Other selected roles follow in alphabetical order.

For each role:

**1. Anchor the lens**
Quote or paraphrase one line from this role's `orientation.frame` or `lens.verify`.
This defines the review perspective. Do not write the finding before writing the lens.

**2. Find**
What does this lens see in the artifact? Name the specific surface: section, field,
assumption, diagram element. No unnamed surfaces pass.

For challenger roles: reference the inertia block.
State whether this finding amplifies, contradicts, or is independent of the status-quo case.

**3. Score severity**
Apply Stage 3 contract. Challenger HIGH means: the inertia gap is real and unaddressed.

**4. Recommend**
Concrete action: what to do and where. Not a directive — a location is required.

---

### Stage 6 — Review matrix (severity-sorted)

Order rows by score descending (HIGH first, then MEDIUM, then LOW).
Within each tier: challenger rows before domain rows.

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|

---

### Stage 7 — Priority summary

```
HIGH: [N] finding(s) — [brief label of blocking concern, or "none"]
MEDIUM: [N] finding(s) — [brief label, or "none"]
LOW: [N] finding(s) — [brief label, or "none"]
```

---

### Stage 8 — Cross-role synthesis

2–3 sentences: convergence, conflict, or "No cross-role signal detected."

---

### Stage 9 — AMEND

> **AMEND**
> - Add reviewer: `/crew-check [artifact] --amend add:[role-name]`
> - Full registry: `/crew-check [artifact] --depth deep`
> - Re-run inertia block: `/crew-check [artifact] --amend rerun:inertia`
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Show unsorted: `/crew-check [artifact] --amend unsorted`

---

---

## V-05

**Axes**: Role sequence + Lifecycle emphasis + Lens-anchoring mandate (full integration)
**Hypothesis**: Full integration targeting all three v2 aspirational criteria simultaneously
with dedicated enforcement mechanisms: C-11 (lens-anchoring) via a mandatory lens-quote gate
embedded in each reviewer step — the step structurally cannot produce output before the quote
exists; C-12 (severity calibration contract) via a severity decision table defined once as a
phase-entry artifact and referenced by name at every assignment; C-13 (challenger-first) via
a Phase 1 that runs challenger roles exclusively before any other reviewer is selected. The
three mechanisms form a coherent execution contract: Phase 1 seeds the inertia frame and
challenger severity bar; Phase 2 selects and sequences domain reviewers against it; Phase 3
enforces lens-anchoring and calibrated severity row by row; Phase 4 renders the full output.

---

You are running `/crew-check`.

This skill runs in four phases with hard exit conditions. Challenger roles run in Phase 1
before domain role selection begins. Lens-anchoring is a required gate before each finding.
The severity contract is defined once and referenced throughout.

---

## PHASE 1 — LOAD + CHALLENGER REVIEWS

**Entry condition**: artifact provided
**Exit condition**: registry locked AND all challenger rows validated and staged

**P1.1 — Load registry**

Open `.craft/roles/`. Read every file.
For each file extract: name, archetype, `orientation.frame`, `expertise.relevance`.
Role pool = all discovered files. Zero roles may be invented.
If `.craft/roles/` missing or empty: output `ERROR: registry unavailable.` Halt.

**P1.2 — Lock severity contract**

Define once here. Reference by name at every severity assignment throughout the run.

```
SEVERITY CONTRACT
  HIGH   — blocks commitment or ship decision; cannot be deferred
  MEDIUM — must resolve before shipping; does not block commitment
  LOW    — advisory; fix if time permits
```

Only these three labels are valid. Assign one label per row, no others.

**P1.3 — Identify challengers**

Find all roles with `archetype: challenger`. They run now, before any other role selection.

If no challenger role exists in the registry: note this as a gap but continue.
Write: `No challenger archetype found in registry. Inertia case is unreviewed.`

**P1.4 — Run each challenger role**

For each challenger:

> **Lens gate (required)**
> Quote one line from `orientation.frame` or `lens.verify` verbatim or in tight paraphrase.
> Label it: `Lens: "[quote]"`
> You may not proceed to the finding before this label is written.

> **Inertia finding (required for challengers)**
> State the null hypothesis in this form:
> "The team currently [X] instead of this artifact.
>  That alternative costs [Y] in [effort/time/risk].
>  This artifact is worth acting on only if [Z]."
>
> Fill X, Y, Z from artifact content.
> If the artifact does not name what it replaces: X = "unspecified — artifact does not
> acknowledge what it displaces." Severity = HIGH. Reason: no artifact can justify
> adoption costs it has not acknowledged.

> **Severity (per contract)**
> Apply SEVERITY CONTRACT from P1.2.
> - HIGH: inertia case is credible, real, and unaddressed in the artifact
> - MEDIUM: inertia is named but switching cost is not quantified
> - LOW: artifact directly neutralizes the status-quo argument with evidence

> **Recommendation**
> One concrete action naming what to do and where in the artifact.

Validate the row:
- Lens gate written before finding? Y/N
- Finding names the null hypothesis with filled X/Y/Z? Y/N
- Severity is exactly HIGH, MEDIUM, or LOW? Y/N
- Recommendation names what AND where? Y/N

If any N: revise before staging. Stage only when all Y.

**Exit condition met**: registry locked, SEVERITY CONTRACT defined, all challenger rows staged.

---

## PHASE 2 — SELECT DOMAIN REVIEWERS

**Entry condition**: Phase 1 complete
**Exit condition**: domain reviewer queue declared with rationale

**P2.1 — Check depth flag**

- `--depth deep`: queue = all non-challenger roles from pool. Depth = deep. Skip to P2.3.
- Absent: depth = standard. Continue.

**P2.2 — Standard selection**

Select 2–3 non-challenger roles whose `expertise.relevance` or `orientation.frame`
intersects the artifact's content, namespace, or subject domain.

For each selected role write: `[name]: selected because [one sentence tying their
documented relevance to this artifact's specific content].`

**P2.3 — Declare queue**

Output at document top (before the matrix):
```
Crew Check: [artifact name or type]
Depth: [standard | deep]
Roles: [challenger roles] → [domain roles, in selection order]
```

**Exit condition met**: queue finalized, rationale written.

---

## PHASE 3 — DOMAIN REVIEWS

**Entry condition**: Phase 2 complete
**Exit condition**: all domain queue members have validated rows staged

For each domain role in queue order:

> **Lens gate (required)**
> Quote or paraphrase one line from `orientation.frame` or `lens.verify`.
> Label it: `Lens: "[quote]"`
> This gate must be written before the finding. The lens defines the reviewing voice
> for this row. Without it, the finding risks collapsing into generic review language.

> **Finding**
> What does this lens see in the artifact?
> Name the artifact surface explicitly: section heading, field name, stated assumption,
> diagram element. A finding that cannot name a surface is not specific enough.
>
> Do not repeat a concern already staged by a challenger row.

> **Severity (per SEVERITY CONTRACT)**
> Apply the contract defined in P1.2. Ask: how does this compare to the inertia gap
> established in Phase 1? Calibrate accordingly.

> **Recommendation**
> One concrete action: (1) what to do and (2) where in the artifact. Not a directive.

Validate each row before staging:
- Lens gate written? Y/N
- Finding names a specific artifact surface? Y/N
- Severity is exactly HIGH, MEDIUM, or LOW? Y/N
- Recommendation is concrete with location? Y/N
- Finding is not a duplicate of a challenger row? Y/N

Revise any N before staging.

**Exit condition met**: all domain roles have validated rows staged.

---

## PHASE 4 — RENDER

**Entry condition**: all rows staged (Phase 1 challenger rows + Phase 3 domain rows)
**Exit condition**: complete output delivered

**R1. Header block** (written at document top, before all rows):
```
Crew Check: [artifact name or type]
Depth: [standard | deep]
Roles: [list in execution order — challengers first]
```

**R2. Review matrix** — flush from staging buffer, challenger rows first:

| Role | Findings | Severity | Recommendation |
|------|----------|----------|----------------|
*[one row per reviewer in execution order; lens gates appear above each row as sub-headers]*

**R3. Cross-role synthesis** (required):
2–3 sentences. Name at least one:
- **Convergence**: two or more roles independently flagged the same concern area
- **Conflict**: two roles assigned different severity to the same artifact surface

If neither: "No cross-role signal detected — findings are non-overlapping."

**R4. AMEND block** (required):

> **AMEND**
> - Add reviewer (inserted in archetype sequence): `/crew-check [artifact] --amend add:[role-name]`
> - Full registry run: `/crew-check [artifact] --depth deep`
> - Skip challenger phase: `/crew-check [artifact] --amend skip:challengers` *(removes inertia gate)*
> - Re-run single role: `/crew-check [artifact] --amend rerun:[role-name]`
> - Re-run challenger only: `/crew-check [artifact] --amend rerun:challengers`
> - Restrict to domain: `/crew-check [artifact] --amend scope:[domain]`

Output complete. Phase 4 exit condition met.

---
