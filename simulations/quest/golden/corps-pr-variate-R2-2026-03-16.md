---
skill: quest-variate
skill_target: corps-pr
round: 2
date: 2026-03-16
rubric_version: 2
---

# Variate R2 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Inertia framing (Inertia Advocate sequenced first, section as reference baseline) | V-01, V-05 |
| Output format (table-centric findings, per-role summary rows) | V-02, V-04 |
| Phrasing register (descriptive/role-oriented vs imperative/procedural) | V-03 |
| Lifecycle emphasis (explicit phase gates: ROUTE → REVIEW → SYNTHESIZE → DECIDE) | V-04 |
| Consensus mechanism (anti-perspective-label prohibition + architectural mechanism naming) | V-05 |

---

## V-01 — Inertia Framing: Advocate-First Baseline

**Axis**: Inertia framing
**Hypothesis**: Placing the Inertia Advocate's full review section before any technical role
review — and making their section an explicit reference baseline — forces the consensus
section to record where technical roles agree or argue against the status-quo verdict rather
than producing pile-on agreement. The Inertia Advocate's findings become a fixed anchor
that structural divergence is measured against.

---

You are running `/corps-pr`. Route this PR through the org and produce a pre-merge review.

**SETUP**

1. Read `org.yaml` — load role scope patterns and committee definitions.
2. Read the PR diff — identify all changed files and the nature of each change.
3. Read `.craft/roles/` — load orientation and lens for each role you will select.

**STEP 1 — ROUTING TABLE**

Before any review begins, map every changed file to an org.yaml role.

```
## Reviewer Selection

| File / File Group | Change Type | org.yaml Role | Selection Reason |
|-------------------|-------------|---------------|------------------|
| [path(s)]         | [add/modify/delete] | [role name] | [one sentence from role scope in org.yaml] |
```

Rules:
- Every changed file must appear in a row, alone or in a named logical group.
- Role selection must be traceable to an org.yaml scope pattern — not inferred.
- If no org.yaml role covers a file, add a Coverage Gap entry below the table:
  `COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`
- If multiple files map to the same role, group them in a single row.

**STEP 2 — INERTIA ADVOCATE (runs first, always)**

Before any technical role produces findings, the Inertia Advocate reviews first.
This section appears before all other review sections. This is structural, not configurable.

Their purpose: establish a status-quo baseline that every subsequent technical reviewer
reads before writing their own findings. Their verdict is the reference object — technical
reviewers argue alongside or against it.

Their mandate: produce the strongest possible case that this PR should not merge.
Not because the code is defective — because the change may be unnecessary.

Required elements in this section:
1. State the null hypothesis explicitly: what the codebase currently does instead of this
   change, and why that alternative might be sufficient.
2. Rate null hypothesis strength: HIGH (credible and unaddressed by the PR), MEDIUM (named
   but switching cost not justified), LOW (PR directly defeats the status quo argument).
3. Produce at least 2 findings with P1/P2/P3 severity arguing the status quo is sufficient
   or the change is unjustified.
4. Close with a verdict: BLOCK / CONDITION / PASS.

```
## Review: Inertia Advocate

Null hypothesis: The codebase currently [does X via existing mechanism Y]. That alternative
has cost [Z]. This PR is worth merging only if [condition].
Null hypothesis strength: HIGH / MEDIUM / LOW

F-01 [P1/P2/P3] [specific argument that the status quo is sufficient or the change is unjustified]
     Owner: [role] | Resolution: [what would move this finding to P3]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [concrete action]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
Verdict: BLOCK / CONDITION / PASS
```

**STEP 3 — TECHNICAL ROLE REVIEWS**

After the Inertia Advocate section, run each role from the routing table in this order:
security and compliance roles → domain-specific roles → PM and TPM roles.

For each technical role:

```
## Review: [role name]

Source files: [files from routing table that triggered this selection]
Orientation: [one phrase from .craft/roles/ describing their lens]

F-01 [P1/P2/P3] [finding specific to this role's domain — names a code surface, function, or contract]
     Owner: [role] | Resolution: [concrete action naming what and where]
F-02 [P1/P2/P3] [second domain-specific finding]
     Owner: [role] | Resolution: [concrete action]
[additional findings if the diff warrants them; minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Validity check per finding: could only this role have raised it, given their domain lens?
If any generic reviewer could write the same finding, revise it.

**STEP 4 — CONSENSUS ANALYSIS**

After all role sections (Inertia Advocate + technical roles):

```
## Consensus Analysis

Inertia baseline: Inertia Advocate rated null hypothesis [HIGH/MEDIUM/LOW].
  Technical reviewers [confirm / challenge / do not address] this verdict.

Agreement: [area where two or more roles raised the same concern independently]
  — Roles: [role-A], [role-B]

Divergence: [role-A] rates [concern] as P1; [role-B] rates it as P3.
  Mechanism: [structural or architectural property of the code causing this rating difference]

Critical finding: [F-XX from role-Y] — [one sentence on why this finding most threatens the merge]
```

If no agreement or divergence exists: "No cross-role convergence or divergence detected —
findings cover non-overlapping surfaces."

**STEP 5 — RECOMMENDATION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [cite specific finding ID from a specific role — one sentence]

Conditions (GO WITH CONDITIONS only):
- [what must be resolved] — sign-off: [role who confirms resolution before merge]
```

Decision must be one of the three options. Ambiguous or delegated decisions ("the team
should decide") fail.

**AMEND**

- Add a reviewer: `/corps-pr --amend add:[role-name]`
  Output must open with: "AMEND: adding [role]. Source files: [list]. Prior findings
  unchanged. New findings below."
- Change scope: `/corps-pr --amend scope:[domain]`
  Output must open with: "AMEND: restricting to [domain]. Roles removed: [list].
  Prior findings for removed roles are superseded."

---

## V-02 — Output Format: Table-Centric

**Axis**: Output format
**Hypothesis**: Defining all output as structured tables before execution begins makes C-01
(file-to-role mapping) and C-07 (per-role severity summary) structurally impossible to fail
— the table schema forces the mapping and count into fixed columns. It also makes C-06
(coverage gap) and C-04 (go/no-go) fail-safe: a missing table row is visible in a way that
a missing prose sentence is not.

---

You are running `/corps-pr`. Route this pull request through the org for pre-merge review.

**INPUT**

- PR diff (files changed and the nature of each change)
- `org.yaml` (role scope patterns and committee definitions)
- `.craft/roles/` (role orientations and domain lenses)

**OUTPUT CONTRACT**

All reviewer selections and all findings appear in structured tables. No prose finding lists.
Format is defined here and must be followed exactly through the full run.

---

**TABLE 1 — ROUTING**

Produce this table before any review begins. Do not start reviews until the routing table
is complete.

| File / File Group | Change Type | Role Selected | Scope Match in org.yaml |
|-------------------|-------------|---------------|-------------------------|
| [path(s)]         | [add/modify/delete] | [role name] | [scope pattern that matched] |

Every changed file must appear in a row, alone or grouped logically.
A missing file is a hard fail — not acceptable as a silent omission.

Coverage Gap (add below the routing table if any files have no matching org.yaml role):

| File | Gap Reason |
|------|------------|
| [path] | No org.yaml scope pattern covers this file. |

---

**TABLE 2 — FINDINGS (one table per selected role)**

For each role in the routing table, produce a separate findings table.
Tables appear in routing order.

Column contract:

| Column | Type | Constraint |
|--------|------|------------|
| ID | string | F-01, F-02, ... — restart at F-01 for each role |
| Finding | string | Must name a specific function, module, interface, or code surface — not a category. "Authentication concern" fails. "Token refresh in auth/middleware.ts does not validate expiry on silent refresh path" passes. |
| Severity | enum | Exactly P1, P2, or P3. No other values. P1 = blocking, P2 = major (resolve before merge), P3 = minor (advisory) |
| Owner | string | The role responsible for resolution |
| Resolution | string | One concrete action naming what to do and where — not a generic directive |

Per-role table format:

```
## [role name] — Findings

Source files: [files from routing table that triggered this role]

| ID   | Finding       | Severity | Owner  | Resolution       |
|------|---------------|----------|--------|------------------|
| F-01 | [specific finding from this role's domain] | P1/P2/P3 | [role] | [concrete action] |
| F-02 | [second finding] | P1/P2/P3 | [role] | [concrete action] |
| TOTAL | — | — | [N] findings: [x] P1, [y] P2, [z] P3 | — |
```

Minimum 2 data rows per role (not counting the TOTAL row).
The TOTAL row is required — it is not optional. A section with no TOTAL row fails C-07.
Severity must vary: not all rows may carry the same severity label.

---

**TABLE 3 — CONSENSUS**

After all per-role finding tables:

| Signal | Finding Area | Roles | Mechanism / Notes |
|--------|-------------|-------|-------------------|
| Agreement | [area two or more roles flagged independently] | [role-A], [role-B] | [one sentence] |
| Divergence | [area where roles rate the same change differently] | [role-A (P1)], [role-B (P3)] | [structural/architectural reason — name the mechanism, not the perspectives. "They have different priorities" fails.] |
| Critical | [single most important finding across all roles] | [role] | [why this one matters most] |

A Consensus table with zero data rows fails. If Agreement and Divergence are both absent,
write one row:
`| No cross-role signal | — | all roles | Findings cover non-overlapping surfaces: [reason] |`

---

**TABLE 4 — RECOMMENDATION**

| Decision | Primary Reason | Conditions | Sign-off Role |
|----------|---------------|------------|---------------|
| GO / NO-GO / GO WITH CONDITIONS | [F-XX from [role] — one sentence] | [condition text or "none"] | [role name or "none"] |

Exactly one decision value. "The team should consider" or equivalent hedges fail.
If GO WITH CONDITIONS: Conditions column must name what resolves the condition,
Sign-off Role column must name which role confirms resolution before merge.

---

**EXECUTION SEQUENCE**

1. Read org.yaml and .craft/roles/
2. Produce TABLE 1. Routing complete before reviews begin.
3. For each role in TABLE 1: produce TABLE 2 (one findings table per role).
4. Produce TABLE 3 (consensus).
5. Produce TABLE 4 (recommendation).

---

**AMEND**

When run with `--amend`, output this block before TABLE 1:

```
AMEND SCOPE
What changed: [what was added or removed from the default run]
Roles added: [list or "none"]
Roles removed: [list or "none"]
Prior findings superseded: [F-ID list, or "none — prior findings stand"]
```

Then run the full table sequence for the amended scope.

---

## V-03 — Phrasing Register: Descriptive / Role-Oriented

**Axis**: Phrasing register
**Hypothesis**: Describing what each role actually cares about — their professional anxieties,
the failure patterns they're trained to catch — instead of issuing procedural PRODUCE /
FORMAT instructions activates the persona more naturally. The model writes from inside the
role rather than executing a checklist, producing findings that could only come from that
role's lens rather than generic observations in a labeled box.

---

You are running `/corps-pr`. Your job: send this pull request through the people in the org
who actually need to see it, and find out what each of them would raise before it merges.

---

**Read what you need**

Open `org.yaml`. Know which roles own which file paths and what their scope covers.

Open the PR diff. Know what changed, in which files, and what the changes do.

Open `.craft/roles/`. For each role you'll run: read their orientation — what they're paid
to catch, what failure modes they've been burned by, what they look at first in a review.

---

**Figure out who reviews**

Go through the changed files. For each file or logical group of files, ask: which role in
org.yaml owns this path?

Write down who reviews and why, before any review runs:

```
Who reviews this PR:
- [role name]: files [path-a, path-b] — [one sentence on why their scope covers these files]
- [role name]: file [path-c] — [one sentence]
```

If any file has no owner in org.yaml, say so explicitly:
"No role covers [path] — coverage gap in org.yaml."

Don't skip files. Don't silently leave anything unassigned.

---

**Let each reviewer do their job**

For each role in the list, simulate that person reviewing this PR the way they actually
review PRs in their domain.

A security engineer reviewing a PR isn't looking for style or formatting — they're asking:
what new attack surface does this open? What trust boundaries does it cross? Are inputs
validated at the right layer or is validation deferred to a caller that might not do it?

A compiler lead isn't reading for variable naming — they're asking: does this touch the
codegen path? Does the type inference still hold across all call sites? Are the IR
assumptions valid under the new change?

Let the role's orientation from `.craft/roles/` shape what they find. If a finding reads
exactly the same regardless of which role wrote it, it isn't carrying its reviewer's lens.
Revise it until it does.

Each reviewer writes their section:

```
## [role name]

These files triggered this review: [paths]
What I'm looking at: [one sentence from their orientation — what they trained to catch]

F-01 [P1/P2/P3] [what I found — specific to my domain and these changed lines or functions]
     Owner: [who owns this] | Fix: [what they need to do, and where]
F-02 [P1/P2/P3] [second finding, also domain-specific]
     Owner: [role] | Fix: [action]
[more if the diff warrants it; minimum 2]

[N] findings — [x] P1, [y] P2, [z] P3
```

Severity logic:
- P1: I won't sign off on this merge until this is resolved
- P2: this needs to be fixed before merge — I'll approve after
- P3: worth noting, not blocking

---

**Read across the reviews**

Once all reviewers have written their sections, read across them.

Did two reviewers independently flag the same thing? That's your most reliable signal — it
survived two different lenses arriving at the same place without coordinating.

Did two reviewers rate the same code change at different severities? That's your most
interesting signal. Work out why — not because they have different jobs (that's obvious),
but what specific property of the code makes one of them see a P1 and the other see a P3.

Write 2–4 sentences under **Consensus Analysis**:
- Name the convergence or the divergence
- If divergence: name the structural or architectural reason for the rating gap

---

**Make the call**

End with a recommendation. Pick one: GO / NO-GO / GO WITH CONDITIONS.

Name the specific finding driving the call. No hedging — the merge either proceeds,
is blocked, or proceeds once named conditions are met.

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Driving finding: [F-XX — role — one sentence]
Conditions (if applicable): [what must be resolved] — sign-off: [role who confirms]
```

---

**To amend this run:**

- Add a reviewer: `/corps-pr --amend add:[role]`
  Say what role was added, which files triggered the addition, and which prior findings
  (if any) are superseded or unchanged.

- Change scope: `/corps-pr --amend scope:[domain]`
  Say which roles were added or removed, and which prior findings no longer apply.

---

## V-04 — Role Sequence + Lifecycle Emphasis: Explicit Phase Gates

**Axes**: Role sequence (security-first within reviews) + Lifecycle emphasis (explicit
ROUTE → REVIEW → SYNTHESIZE → DECIDE phase gates with entry/exit conditions)
**Hypothesis**: Splitting the skill into four named phases with hard entry conditions
prevents the most common composite failure: routing and reviewing happening in the same
pass, which causes role selection to drift mid-output and leaves some changed files
unrouted. A hard phase boundary forces the complete routing table to exist before any
review begins — making C-01 a structural property of the output rather than something
the model remembers to do.

---

You are running `/corps-pr`. Execute in four explicit phases. Do not begin a phase until
its entry condition is satisfied.

---

## PHASE 1 — ROUTE

**Entry condition**: PR diff and org.yaml are available.
**Exit condition**: complete routing table written; every changed file assigned to a role
or explicitly flagged as unowned.

**R1** Read `org.yaml`. Extract scope patterns and role definitions.
**R2** Read the PR diff. List every changed file.
**R3** For each file, evaluate org.yaml scope patterns. Assign the first matching role.
**R4** Write the routing table:

```
## Routing Table

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [path(s)]         | [add/modify/delete] | [role] | [pattern that matched] |
```

**R5** Any file with no org.yaml match: add to Coverage Gap section below the table.

```
## Coverage Gap

| File | Reason |
|------|--------|
| [path] | No org.yaml scope pattern matches this file. |
```

**R6** Phase 1 is complete. Phase 2 may not begin until this step is done.

---

## PHASE 2 — REVIEW

**Entry condition**: routing table complete (Phase 1 exit reached).
**Exit condition**: every role from the routing table has a findings section.

Read `.craft/roles/` for each role in the routing table. Load orientation and lens.

Role sequence within this phase: security and compliance roles first → domain-specific
roles second → PM and TPM roles last. If the Inertia Advocate appears in the routing
table or in org.yaml as a default reviewer, they run before all others.

For each role, produce a findings section. Validate each finding before writing it:
- Does it name a specific code surface, function, module, or interface — not a category?
- Does it reflect this role's domain lens — not something any reviewer could have written?
- Does it carry a P1/P2/P3 severity label?

```
## Review: [role name]

Triggered by: [files from routing table]
Orientation: [one phrase from .craft/roles/]

F-01 [P1/P2/P3] [finding tied to this role's domain — names the code surface]
     Owner: [role] | Resolution: [concrete action naming what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings; more if the diff warrants it]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Phase 2 complete when every role from the routing table has a section.

---

## PHASE 3 — SYNTHESIZE

**Entry condition**: all role findings sections complete (Phase 2 exit reached).
**Exit condition**: consensus analysis written with at least one signal row.

Read across all findings sections. Identify:

1. **Agreement** — a concern raised independently by two or more roles
2. **Divergence** — the same code change rated at different severities by two roles
3. **Critical finding** — the one finding that most threatens the merge if unresolved

For any divergence found: explain the structural or architectural reason for the rating
gap. Name the property of the code that causes one role to see P1 and another to see P3.
Do not use perspective-label explanations ("they prioritize differently").

```
## Consensus Analysis

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [concern] P1; [role-B] rates it P3.
  Mechanism: [specific code property, system boundary, or architectural constraint
  that causes this difference — not a perspective label]

Critical finding: [F-XX] from [role] — [one sentence on why this is the most important]
```

If no convergence or divergence: "No cross-role signal detected — findings cover
non-overlapping surfaces."

Phase 3 complete when the consensus analysis section is written.

---

## PHASE 4 — DECIDE

**Entry condition**: consensus analysis complete (Phase 3 exit reached).
**Exit condition**: go/no-go recommendation written with justification.

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [cite F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms resolution before merge]
2. [additional condition if present] — sign-off: [role]
```

Exactly one decision value. Delegated or ambiguous decisions fail.

---

**AMEND**

- `--amend add:[role]`: Phase 2 reruns for the added role only. Phases 3 and 4 rerun.
  Disclose at output start: what role was added, which files triggered the addition.

- `--amend scope:[domain]`: Phase 1 reruns with filtered scope. Phases 2–4 rerun for
  new scope.
  Disclose at output start: which roles were removed, which prior findings are superseded.

---

## V-05 — Inertia Framing + Consensus Mechanism (Combination)

**Axes**: Inertia framing (Inertia Advocate first, section as reference baseline) +
consensus mechanism (explicit anti-perspective-label prohibition in divergence explanations)
**Hypothesis**: Combining Inertia-first sequencing (C-11) with a structural prohibition on
perspective-label divergence explanations (C-12) and a root cause synthesis requirement
(C-09) targets all three aspirational criteria in one variation. The Inertia Advocate's
section is the anchor; the consensus section is required to explain why technical roles
diverge from or confirm that anchor in terms of code mechanism, not role identity.

---

You are running `/corps-pr`. Route this PR through the org and produce a pre-merge review
that explicitly tests whether the change is justified against the status quo.

**SETUP**

1. Read `org.yaml` — role scope patterns and committee definitions.
2. Read the PR diff — all changed files and the nature of each change.
3. Read `.craft/roles/` — orientation and lens for each role you will use.

**STEP 1 — ROUTING TABLE**

Map every changed file to an org.yaml role before any review begins.

```
## Reviewer Selection

| File / File Group | Change Type | Role | org.yaml Scope Match |
|-------------------|-------------|------|---------------------|
| [path(s)]         | [type]      | [role] | [scope pattern] |
```

Coverage Gap: any file with no org.yaml match — list explicitly below the table.
`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`
Do not silently omit.

---

**STEP 2 — INERTIA ADVOCATE (always runs first)**

The Inertia Advocate's review section appears before all other role sections.
This is structural — not a default that can be overridden.

Their role: establish the status-quo baseline. Every subsequent technical reviewer reads
this section before writing their own findings. The Inertia Advocate's verdict is the
reference object that the consensus section compares all technical findings against.

Their question: is the PR justified, or does the current codebase already handle this
adequately? Argue the strongest possible case for not merging.

```
## Review: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y]. The cost of that
alternative is [Z]. This PR is worth merging only if [condition].

Null hypothesis strength: HIGH / MEDIUM / LOW
  HIGH   — the "do nothing" case is credible and the PR does not address it
  MEDIUM — the PR names the problem but does not justify the switching cost
  LOW    — the PR directly defeats the status quo argument

F-01 [P1/P2/P3] [specific argument that the status quo is sufficient or the change is unjustified]
     Owner: [role] | Resolution: [what would need to change for this finding to become P3]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [concrete action]
[additional findings if the PR touches multiple unjustified areas; minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
Verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

**STEP 3 — TECHNICAL ROLE REVIEWS**

Run each role from the routing table. Sequence: security and compliance roles before
domain-specific roles before PM and TPM roles.

```
## Review: [role name]

Source files: [files from routing table]
Orientation: [one phrase from .craft/roles/ describing this role's lens]

F-01 [P1/P2/P3] [finding from this role's domain — names a code surface, function, or contract]
     Owner: [role] | Resolution: [concrete action]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Validity check: if a finding could have been written by any reviewer regardless of their
role, revise it until it carries the domain lens. A compiler-lead finding must address
compilation, IR, codegen, or type-system concerns. A security finding must address threat
surface, trust boundaries, or input validation. A finding that a PM and an architect would
write identically is not domain-loaded.

---

**STEP 4 — CONSENSUS ANALYSIS**

Read across all review sections (Inertia Advocate + all technical roles).
The consensus section does three things explicitly.

**A — Inertia status**
State whether the Inertia Advocate's null hypothesis was confirmed, partially challenged,
or defeated by the technical role findings.

**B — Agreement**
Name at least one finding area where two or more roles converged independently.

**C — Divergence with mechanism**

If two roles rated the same code change at different severity levels, explain WHY.
The explanation must name the structural or architectural property of the code that causes
the divergence.

**Prohibited divergence explanations** — these are perspective labels, not mechanisms.
The following phrases fail C-12 and must not appear:
- "they have different perspectives"
- "they prioritize differently"
- "their roles lead them to different conclusions"
- "they view this from different angles"
- any equivalent phrase that attributes the divergence to role identity rather than code property

**Valid divergence explanation format**:
> "[role-A] rates [concern] P1 because [specific code property — e.g., the change modifies
> the codegen emission path, which falls within their ownership scope and has no compensating
> abstraction downstream]. [role-B] rates it P3 because [specific reason — e.g., from their
> frame the codegen path is isolated behind a versioned interface that callers do not
> traverse directly, so user-visible behavior is unchanged]."

**D — Critical finding**
Surface the single finding that, if unresolved, most threatens the merge.

```
## Consensus Analysis

Inertia status: The Inertia Advocate rated null hypothesis [HIGH/MEDIUM/LOW].
  Technical findings [confirm / partially challenge / defeat] this baseline.
  [One sentence explaining how technical roles responded to the status-quo argument.]

Agreement: [finding area] — raised independently by [role-A] and [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates it P3.
  Mechanism: [structural or architectural property of the code causing this rating
  difference — names the code, not the perspectives]

Critical finding: [F-XX from role-Y] — [one sentence on why this is the critical one]
```

If no agreement or divergence: write "No cross-role signal detected" and explain why
the findings cover non-overlapping surfaces.

---

**STEP 5 — RECOMMENDATION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [cite F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [specific condition — what must be resolved] — sign-off: [role who confirms before merge]
2. [additional condition if present] — sign-off: [role]
```

---

**AMEND**

- Add a reviewer: `/corps-pr --amend add:[role-name]`
  Output must open with:
  "AMEND: adding [role]. Source files triggering this addition: [list].
   Prior findings unchanged. Findings superseded by this addition: [F-IDs or 'none']."

- Change scope: `/corps-pr --amend scope:[domain]`
  Output must open with:
  "AMEND: restricting to [domain]. Roles removed: [list].
   Prior findings for removed roles are superseded. Remaining findings stand."
