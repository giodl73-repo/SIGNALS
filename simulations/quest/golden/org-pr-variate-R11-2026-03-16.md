---
skill: quest-variate
skill_target: org-pr
round: 11
date: 2026-03-16
rubric_version: 10
---

# Variate R11 — org-pr

5 complete prompt body variations for the `org-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (terse self-describing column schema — C-33 probe on column names) | V-01 |
| Lifecycle emphasis (inline gate in opening line — C-30 probe) | V-02 |
| Role sequence (UX/product-first, impact-ordered) | V-03 |
| Phrasing register (conversational "what you missed") + Inertia framing (prominent) | V-04 |
| Lifecycle emphasis (named phases) + Consensus mechanism (architectural root cause required) | V-05 |

---

## V-01 — Output Format: Terse Self-Describing Column Schema

**Axis**: Output format
**Hypothesis**: C-33 confirmed that self-describing form names satisfy C-31 without
parenthetical elaboration when names encode the failure mode. This variation tests whether
the same principle extends one level up: if output-table column names are themselves
self-describing — "Surface" encodes "specific code surface not a category label",
"Fix" encodes "concrete action naming what and where" — then column constraint instructions
can be omitted and the schema itself carries the C-31 specificity contract. If the model
infers specificity from a self-describing column name, we get a tighter prompt with
equivalent constraint enforcement. Failure mode: opaque column names ("Notes", "Details")
force elaboration back in, which would confirm C-33's opaque-name path applies to schemas
as well as form catalogs.

---

You are running `/org-pr`. Route this PR through the org and produce a pre-merge review.

**LOAD**

- `org.yaml` — role scope patterns and committee definitions
- PR diff — all changed files and the nature of each change
- `.craft/roles/` — role orientation and lens for each reviewer

**TABLE 1 — ROUTING**

One row per changed file or logical file group. Complete before any reviews begin.

| Path | Change | Role | Scope-Match |
|------|--------|------|-------------|
| [file or group] | [add/modify/delete] | [role from org.yaml] | [pattern that matched] |

**Unowned** (add below the table if any file has no org.yaml match):

| Path | Gap |
|------|-----|
| [file] | Unowned — no org.yaml scope pattern covers this path. |

---

**TABLE 2 — FINDINGS (one table per role, in routing order)**

| ID | Surface | Sev | Owner | Fix |
|----|---------|-----|-------|-----|
| F-01 | [specific function, interface, or call site in the diff] | P1/P2/P3 | [role] | [what to do and where] |
| F-02 | [second surface] | P1/P2/P3 | [role] | [what to do and where] |
| — | TOTAL | — | [N] findings: [x]P1 [y]P2 [z]P3 | — |

Section header for each table:

```
## [role name]
Files: [paths from routing table]
Lens: [one phrase from .craft/roles/]
```

Minimum 2 data rows per role. TOTAL row required. Severity must vary across rows.

Named invalid forms — each name encodes the failure the form represents:

- **Generic**: a finding whose Surface names a category ("authentication layer",
  "error handling", "performance") rather than a specific code artifact. Correction:
  rewrite Surface to name the function, interface, or line range in the diff.
- **Unlensed**: a finding any reviewer could have written regardless of role — Surface
  is specific but carries no domain lens. Correction: rewrite to embed the role's
  orientation; the finding must be impossible from a different role's position.

---

**TABLE 3 — CONSENSUS**

| Signal | Area | Roles | Mechanism |
|--------|------|-------|-----------|
| Agreement | [concern raised independently by 2+ roles] | [role-A], [role-B] | [one sentence] |
| Divergence | [same change rated differently] | [role-A (P1)], [role-B (P3)] | [architectural property causing the gap — not a perspective label] |
| Critical | [most important finding across all roles] | [role] | [why this one threatens the merge] |

If no Agreement or Divergence exists, write one row:
`| None | — | all roles | Findings cover non-overlapping surfaces: [reason] |`

---

**TABLE 4 — RECOMMENDATION**

| Decision | Finding | Conditions | Sign-off |
|----------|---------|------------|----------|
| GO / NO-GO / GO WITH CONDITIONS | [F-XX from role — one sentence] | [what must resolve, or "none"] | [role, or "none"] |

Exactly one decision value. No delegation.

---

**AMEND**

- `--amend add:[role]`: insert a TABLE 2 section for the added role; rerun TABLE 3 and 4.
  Open with: "AMEND: adding [role]. Files: [list]. Prior findings unchanged."
- `--amend scope:[domain]`: rerun full sequence for filtered scope.
  Open with: "AMEND: restricting to [domain]. Roles removed: [list]. Prior findings superseded."

---

## V-02 — Lifecycle Emphasis: Inline Gate (C-30 Probe)

**Axis**: Lifecycle emphasis
**Hypothesis**: C-30 established that a phase/lifecycle gate satisfies C-09 when it contains
all three elements — lifecycle condition, halt instruction, alternative path reference —
regardless of structural placement or labeling. This variation tests the minimal expression:
a single inline gate sentence in the first instruction line, with no named section, no
phase headers, and no gate label. If the three elements are present in that sentence, C-09
is satisfied and C-30 fires. Secondary test: does the absence of explicit phase headers
cause routing-and-reviewing to collapse into a single pass (the failure mode gate structure
was designed to prevent)? If findings appear before the routing table is complete in output,
inline gate is insufficient and a structural separator is load-bearing.

---

You are running `/org-pr` — if this PR has already been merged, stop here and switch to
post-merge audit mode (re-scope each step as "would this have been caught?" then halt
after the recommendation).

**LOAD**

1. Read `org.yaml` — role scope patterns and committee definitions.
2. Read the PR diff — all changed files and nature of each change.
3. Read `.craft/roles/` — orientation and lens for each role you will select.

**STEP 1 — ROUTING TABLE**

Map every changed file to an org.yaml role before any review begins.

```
## Reviewer Selection

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [path(s)]         | [add/modify/delete] | [role name] | [pattern that matched] |
```

Rules:
- Every changed file must appear in a row, alone or in a named logical group.
- Role selection traces to an org.yaml scope pattern — not inferred.
- Unowned files: add below the table.
  `UNOWNED: [file] — no org.yaml scope pattern covers this path.`
- Multiple files mapping to the same role: group in one row.

**STEP 2 — ROLE REVIEWS**

For each role in the routing table. Run in this order: security and compliance roles →
domain-specific roles → PM and TPM roles.

```
## Review: [role name]

Files: [paths from routing table]
Orientation: [one phrase from .craft/roles/]

F-01 [P1/P2/P3] [finding — names a specific function, module, or interface in the diff]
     Owner: [role] | Resolution: [concrete action naming what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Validity check per finding: could only this role raise it from their domain lens?
If a different reviewer could write the same finding word-for-word, revise it.

**STEP 3 — CONSENSUS**

After all role sections are complete:

```
## Consensus Analysis

Agreement: [area raised independently by 2+ roles] — [role-A] and [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates it P3.
  Mechanism: [specific code property or architectural constraint causing this gap —
  not a label for the roles' different priorities]

Critical finding: [F-XX from role] — [one sentence on why this is most important]
```

If no convergence or divergence: "No cross-role signal — findings cover non-overlapping surfaces."

**STEP 4 — RECOMMENDATION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
- [what must be resolved] — sign-off: [role who confirms before merge]
```

One decision value. No hedging.

**AMEND**

- `--amend add:[role]`: "AMEND: adding [role]. Files: [list]. Prior findings unchanged.
  New findings below."
- `--amend scope:[domain]`: "AMEND: restricting to [domain]. Roles removed: [list].
  Prior findings for removed roles superseded."

---

## V-03 — Role Sequence: UX/Product-First, Impact-Ordered

**Axis**: Role sequence
**Hypothesis**: Standard org-pr sequences security and compliance first (risk-ordered), but
PRs in practice get blocked by PM veto and UX regression before security concerns surface.
Running user-facing and product roles first (UX, PM, product owner) produces findings that
set expectations about user-visible surface area before technical roles weight in — the
technical roles then write findings knowing what the product considers important rather than
in isolation. Divergence in the consensus section becomes more interpretable: a P1 from
UX and a P3 from security on the same line change signals a product-vs-infrastructure
tension, which is a different architectural diagnosis than two security roles diverging.
Counter-hypothesis: product roles often lack specificity without code surface context;
running them first may produce unlensed findings.

---

You are running `/org-pr`. Route this PR through the org for a pre-merge review.

**LOAD**

1. Read `org.yaml` — role scope patterns and committee definitions.
2. Read the PR diff — all changed files, type of each change, and affected interfaces.
3. Read `.craft/roles/` — orientation and lens for each selected role.

**STEP 1 — ROUTING TABLE**

Before any review begins, map every changed file to its org.yaml role.

```
## Reviewer Selection

| File / File Group | Change Type | Role | Scope Match in org.yaml |
|-------------------|-------------|------|------------------------|
| [path(s)]         | [add/modify/delete] | [role name] | [pattern that matched] |
```

Coverage Gap: any file with no org.yaml match.
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`

Complete this table before any role writes their section.

**STEP 2 — ROLE REVIEWS**

Sequence: user-facing and product roles first → domain/technical roles second →
security and compliance roles third.

Within each tier: roles that own more changed files run before roles that own fewer.

For each role:

```
## Review: [role name]

Source files: [files from routing table]
Orientation: [one phrase from .craft/roles/ — what this role is trained to catch]

F-01 [P1/P2/P3] [finding specific to this role's domain — names a code surface or user flow]
     Owner: [role] | Resolution: [concrete action naming what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [concrete action]
[additional findings if the diff warrants; minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Finding validity: does this finding require this role's specific orientation to produce?
A UX finding must address user-facing behavior, interaction, or discoverability — not
architecture. A security finding must address threat surface or trust boundary — not UI.
If a finding could appear identically in two different roles' sections, revise it.

**STEP 3 — CONSENSUS ANALYSIS**

Read across all role sections.

```
## Consensus Analysis

Agreement: [area raised independently by 2+ roles] — [role-A] and [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates it P3.
  Mechanism: [structural or architectural property of the code causing this difference —
  name the code property, not the role priority difference]

Critical finding: [F-XX from role] — [one sentence on why this is most important for merge]
```

Impact ordering note: findings from user-facing roles that conflict with technical role
ratings signal a product-risk tension — name it in the divergence mechanism. "UX rates
[change] P1 because the form interaction path changes for all users; security rates it P3
because the change is isolated to a rendering helper with no auth surface" is a valid
mechanism. "They have different priorities" is not.

If no convergence or divergence: "No cross-role signal — findings cover non-overlapping surfaces."

**STEP 4 — RECOMMENDATION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
- [what must be resolved] — sign-off: [role who confirms before merge]
```

One decision value. Delegated decisions fail.

**AMEND**

- `--amend add:[role]`: Add a reviewer. Output opens with:
  "AMEND: adding [role]. Files: [list]. Prior findings unchanged. New findings below."
- `--amend scope:[domain]`: Restrict scope. Output opens with:
  "AMEND: restricting to [domain]. Roles removed: [list]. Prior findings superseded."

---

## V-04 — Phrasing Register (Conversational) + Inertia Framing (Prominent)

**Axes**: Phrasing register (conversational "what the author missed") + Inertia framing
(Inertia Advocate runs first, section anchors consensus as a reference baseline)
**Hypothesis**: Framing the entire review as "what did the author not consider?" rather
than "what does each role find?" shifts the model into adversarial mode — it looks for
gaps rather than confirming existing surface coverage. Combined with an Inertia Advocate
running first and anchoring the consensus section (their null-hypothesis verdict is the
reference object that all technical roles respond to), the review becomes structurally
adversarial from the first line. The author's blind spots are the organizing principle, and
the status-quo argument is the baseline every technical reviewer must either defeat or
confirm. Expected gain: richer P2 and P3 findings (things the author probably saw but
deprioritized). Risk: conversational framing may reduce finding specificity — the
surface-naming requirement becomes harder to enforce without imperative column constraints.

---

You are running `/org-pr`. Your job: find what the PR author didn't think about, and make
sure none of it slips through to main.

---

**Start by reading three things**

- `org.yaml`: who owns which file paths, and what each role's scope covers.
- The PR diff: what changed, where, and what the changes actually do.
- `.craft/roles/`: for every reviewer you'll run — how they read code, what failure
  patterns they've been burned by before, what they look for first.

---

**Map the PR to the org**

Go through every changed file. Find the org.yaml role that owns it.
Write down who reviews before anyone starts reviewing:

```
Who reviews this PR:
- [role name]: files [path-a, path-b] — [why their scope covers these files, from org.yaml]
- [role name]: file [path-c] — [one sentence]
```

If any file has no owner: say so now.
"No role covers [path] — this is a coverage gap in org.yaml."

Don't skip any file. Don't leave anything unassigned without noting it.

---

**The Inertia Advocate goes first — always**

Before any technical reviewer writes a word, the Inertia Advocate asks: does this PR
need to exist? What does the codebase already do instead of this change, and is that
actually good enough?

Their job is to make the strongest case for not merging — not because the code is wrong,
but because the change might be unnecessary. Every technical reviewer reads this section
before writing their own findings.

```
## Inertia Advocate

The codebase currently [does X via mechanism Y]. The cost of the current approach is [Z].
This PR is worth merging only if [condition].

Null hypothesis strength: HIGH / MEDIUM / LOW
  HIGH   — the "do nothing" option is credible and the PR hasn't addressed it
  MEDIUM — the PR names the problem but hasn't justified the switching cost
  LOW    — the PR directly defeats the status quo case

F-01 [P1/P2/P3] [the strongest argument that the current code is sufficient, or the change is unjustified]
     Owner: [role] | What changes this: [what would need to be true for this to become P3]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | What changes this: [concrete action]
[more if the PR touches multiple areas the status quo handles adequately; minimum 2]

[N] findings — [x] P1, [y] P2, [z] P3
Verdict: BLOCK / CONDITION / PASS — [one sentence on why]
```

---

**Now let each reviewer do their job**

For each role in the routing list, simulate what that person would catch that the PR
author didn't think about.

The question isn't "what does this code do" — the PR author knows that. The question is:
"what did they not anticipate?" Each reviewer is looking for something the author either
didn't know about their domain or assumed away.

A security reviewer isn't verifying the happy path. They're asking: what happens when
a caller lies? What trust assumption in this diff is wrong?

A testing engineer isn't reading for functionality. They're asking: what behavior did
just become impossible to test, and what regression will this mask?

Read `.craft/roles/` for each reviewer. Their orientation tells you what failure patterns
they're wired to notice. Let that shape what they find — a finding that any reviewer
could have written regardless of their role isn't doing its job.

```
## [role name]

Files that triggered this review: [paths]
What I'm watching for: [one phrase from their orientation — their specific failure-pattern radar]

F-01 [P1/P2/P3] [what the author missed, specific to my domain and these changed lines]
     Owner: [who owns this] | Fix: [what they need to do, and where — specific]
F-02 [P1/P2/P3] [second gap — also domain-specific]
     Owner: [role] | Fix: [action]
[more if the diff has more gaps for this role; minimum 2]

[N] findings — [x] P1, [y] P2, [z] P3
```

Severity is about impact on the merge decision:
- P1: this must be resolved before merge — I won't approve with it open
- P2: needs to be fixed before merge — I'll approve after it's addressed
- P3: worth noting, won't block

---

**Read across the gaps**

Once all reviewers have written their sections, read across them and ask two questions.

First: did two reviewers independently find the same gap? That's your most reliable signal
— it survived two different lenses without coordination.

Second: did two reviewers look at the same code change and rate it differently? That's your
most interesting signal. Not because they have different jobs — of course they do. Figure
out what specific property of the code makes one person see a P1 and the other see a P3.
Name that property. "They prioritize differently" is not an answer.

Write this up under **Consensus Analysis** — 2–4 sentences:
- Name the convergence or the divergence
- If divergence: name the specific code mechanism causing the rating gap
- Name the Inertia Advocate verdict and whether the technical reviewers' gaps confirm or
  defeat the null hypothesis

---

**Make the call**

GO / NO-GO / GO WITH CONDITIONS. Pick one.

Name the specific finding from the specific reviewer that's driving the call. No hedging.

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Driving gap: [F-XX — role — one sentence]
Conditions (if needed): [what must be closed before merge] — sign-off: [role who confirms]
```

---

**To amend this run:**

- Add a reviewer: `/org-pr --amend add:[role]`
  Say who was added, what files triggered them, and whether any prior findings are superseded.
- Change scope: `/org-pr --amend scope:[domain]`
  Say which roles were removed and which of their findings no longer apply.

---

## V-05 — Lifecycle Emphasis (Named Phases) + Consensus Mechanism (Architectural Root Cause)

**Axes**: Lifecycle emphasis (ROUTE → REVIEW → SYNTHESIZE → DECIDE with hard entry
conditions) + Consensus mechanism (explicit prohibition on perspective-label divergence
explanations; architectural root cause required)
**Hypothesis**: V-04 in R2 confirmed that phase-gated structure prevents routing-and-reviewing
from collapsing into a single pass. This variation extends the phase-gate approach with a
stronger consensus constraint: divergence explanations must name an architectural mechanism
(ownership scope, abstraction boundary, downstream isolation, versioned interface) rather than
a code property in the general sense. The hypothesis is that naming the architecture — not
just the code — produces actionable divergence analysis: "the change crosses the codegen
emission boundary which falls inside role-A's ownership scope but is isolated downstream by
a versioned interface, so role-B's users never traverse it directly" tells the PR author
exactly what to fix (the boundary crossing), not just that two roles disagreed.
Named invalid forms for the consensus section:
- **PerspectiveLabel**: a divergence explanation that attributes the rating gap to role
  identity rather than architectural property. Correction: name the ownership scope,
  abstraction boundary, isolation layer, or interface contract causing the divergence.
- **CodeProperty**: a divergence explanation that names a code property (e.g., "the
  function is complex") without naming the architectural boundary it crosses or sits behind.
  Correction: identify which architectural layer makes the complexity a P1 from one role's
  position and a P3 from the other's.

---

You are running `/org-pr`. Execute in four phases. Do not begin a phase until its entry
condition is satisfied.

---

## PHASE 1 — ROUTE

**Entry condition**: PR diff and org.yaml are available.
**Exit condition**: routing table complete; every changed file assigned to a role or
explicitly flagged as unowned. No review begins until this exit condition is reached.

**R1** Read `org.yaml`. Extract scope patterns and role definitions.
**R2** Read the PR diff. List every changed file.
**R3** For each file: evaluate org.yaml scope patterns. Assign the first matching role.
**R4** Write the routing table:

```
## Routing Table

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [path(s)]         | [add/modify/delete] | [role] | [pattern that matched] |
```

**R5** Any file with no org.yaml match: add to the Coverage Gap section below the table.

```
## Coverage Gap

| File | Reason |
|------|--------|
| [path] | No org.yaml scope pattern covers this file. |
```

**R6** Phase 1 is complete. Phase 2 begins only after this step is done.

---

## PHASE 2 — REVIEW

**Entry condition**: routing table complete (Phase 1 exit reached).
**Exit condition**: every role from the routing table has a findings section.

Load `.craft/roles/` for each role in the routing table. Extract orientation and lens.

Role sequence: security and compliance → domain-specific → PM and TPM.
If org.yaml designates an Inertia Advocate as a default reviewer, they run before all others.

For each role, validate each finding against two criteria before writing it:
1. Does it name a specific code surface, function, module, or interface — not a category?
2. Does it embed this role's domain lens — could only this role have produced it?

```
## Review: [role name]

Triggered by: [files from routing table]
Orientation: [one phrase from .craft/roles/]

F-01 [P1/P2/P3] [finding tied to this role's domain — names the specific code surface]
     Owner: [role] | Resolution: [concrete action naming what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings; more if the diff warrants it]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase 2 complete when every role from the routing table has a findings section.

---

## PHASE 3 — SYNTHESIZE

**Entry condition**: all role findings sections complete (Phase 2 exit reached).
**Exit condition**: consensus analysis written with at least one signal.

Read across all findings sections. Identify:

1. **Agreement** — a concern raised independently by two or more roles
2. **Divergence** — the same code change rated at different severities by two roles
3. **Critical finding** — the one finding that most threatens the merge if unresolved

**Divergence explanation contract**

For any divergence: the explanation must name an architectural mechanism. Valid forms:

> "[role-A] rates [concern] P1 because [architectural property — e.g., the change modifies
> the emission path inside role-A's ownership scope, with no compensating abstraction at the
> phase boundary]. [role-B] rates it P3 because [architectural reason — e.g., the emission
> path is isolated downstream behind a versioned interface that role-B's callers never
> traverse directly, so their observable behavior is unchanged]."

Named invalid forms — each name encodes the failure mode:

- **PerspectiveLabel**: the explanation attributes the divergence to role identity rather
  than architectural property ("they have different priorities", "their roles lead to
  different conclusions", "they view this from different angles"). Correction: replace with
  an architectural mechanism — name the ownership scope, abstraction boundary, isolation
  layer, or interface contract that causes the rating gap.
- **CodeProperty**: the explanation names a surface code property without identifying the
  architectural boundary making it a P1 from one role's position ("it's a complex function",
  "the change is large", "there are many callers"). Correction: identify the architectural
  layer — which boundary does the complexity cross, and why does that boundary exist inside
  role-A's scope but downstream-isolated for role-B?

```
## Consensus Analysis

Agreement: [area] — raised independently by [role-A] and [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates it P3.
  Mechanism: [architectural property — ownership scope, abstraction boundary, isolation
  layer, or interface contract causing this rating gap — not a code property and not a
  perspective label]

Critical finding: [F-XX from role] — [one sentence on why this threatens the merge most]
```

If no convergence or divergence: "No cross-role signal — findings cover non-overlapping surfaces."

Phase 3 complete when the consensus analysis section is written.

---

## PHASE 4 — DECIDE

**Entry condition**: consensus analysis complete (Phase 3 exit reached).
**Exit condition**: go/no-go recommendation written with justification and (if conditions
apply) explicit sign-off roles.

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms resolution before merge]
2. [additional condition if present] — sign-off: [role]
```

Exactly one decision value. Delegated or ambiguous decisions fail.

---

**AMEND**

- `--amend add:[role]`: Phase 2 reruns for the added role only. Phases 3 and 4 rerun.
  Open with: "AMEND: adding [role]. Files: [list]. Prior findings unchanged."
- `--amend scope:[domain]`: Phase 1 reruns with filtered scope. Phases 2–4 rerun.
  Open with: "AMEND: restricting to [domain]. Roles removed: [list].
  Prior findings for removed roles superseded."
