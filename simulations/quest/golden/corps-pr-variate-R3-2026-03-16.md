---
skill: quest-variate
skill_target: corps-pr
round: 3
date: 2026-03-16
rubric_version: 3
---

# Variate R3 — corps-pr

5 complete prompt body variations for the `corps-pr` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (IA anchor as mandatory named template slot in each technical section) | V-01, V-04 |
| Output format (table-centric with IA anchor as explicit header row per role table) | V-02, V-05 |
| Phrasing register (conversational "convince the skeptic" framing) | V-03, V-04 |
| Lifecycle emphasis (sub-phase gate: 2A=IA, 2B=technical roles, each with IA anchor entry condition) | V-04 |
| Consensus mechanism (ban list as named numbered artifact BL-01..BL-05, referenced by ID) | V-05 |

---

## V-01 — Role Sequence: Mandatory IA-Anchor Slot

**Axis**: Role sequence
**Hypothesis**: Making the IA anchor a mandatory named field in the technical role section
template — not an optional instruction — ensures C-14 structurally. The template slot
is either filled or visibly empty; the model cannot produce a complete technical section
without addressing the IA verdict by name. This differs from R2 V-01, which established
inertia-first ordering but did not require each technical section to contain a named IA
anchor field.

---

You are running `/corps-pr`. Route this PR through the org and produce a pre-merge review.

**SETUP**

Read `org.yaml`, the PR diff, and `.roles/` before any output begins.

---

**STEP 1 — REVIEWER ROUTING**

Map every changed file to an org.yaml role. Write the routing table before any review begins:

```
## Reviewer Selection

| File / File Group | Change Type | Role | org.yaml Scope Reason |
|-------------------|-------------|------|-----------------------|
| [path(s)]         | [add/modify/delete] | [role name] | [scope pattern that matched] |
```

Rules:
- Every changed file must appear in at least one row.
- Role selection must cite the org.yaml scope pattern — not be inferred from the filename.
- Coverage gap: if any file has no org.yaml owner, write it below the table:
  `COVERAGE GAP: [file] — no scope pattern matches this path.`
- The Inertia Advocate is always included regardless of diff content. Add them as:
  `| (all changed files) | default | Inertia Advocate | default — always included |`

---

**STEP 2 — INERTIA ADVOCATE (runs first — always)**

The Inertia Advocate section is the first review section in the output. Technical roles
read it before writing their own findings. The IA verdict becomes the reference object
every subsequent technical section must respond to.

Mandate: argue the strongest possible case that this PR should not merge — not because
the code is defective, but because the current codebase may already handle this
adequately.

```
## Review: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y]. The switching cost
is [Z]. This PR is justified only if [condition].
Null hypothesis strength: HIGH / MEDIUM / LOW
  HIGH   — the "do nothing" case is credible and unaddressed by the PR
  MEDIUM — the PR names the problem but does not justify the switching cost
  LOW    — the PR directly defeats the status quo argument

F-01 [P1/P2/P3] [specific argument that the status quo is sufficient or the change is
     unnecessary — names an existing mechanism or path, not a category]
     Owner: [role] | Resolution: [what would need to change for this finding to close]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [concrete action]
[additional findings if warranted; minimum 2]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

**STEP 3 — TECHNICAL ROLE REVIEWS**

Run each role from the routing table. Sequence: security and compliance roles first →
domain-specific roles second → PM/TPM roles last.

Each technical role section uses this template. The **IA anchor** field is mandatory —
fill it before writing any findings. A technical section with an unfilled IA anchor is
incomplete.

```
## Review: [role name]

Source files: [files from routing table that triggered this role]
Orientation: [one phrase from .roles/ — what this role is trained to catch]

IA anchor: The Inertia Advocate [agreed / disagreed / was silent] on [the area this
role addresses]. Specifically: [one sentence naming the IA's relevant finding or
verdict and whether this role confirms it, extends it, or disputes it — and the
architectural or code-level reason why].
  Example: "IA found the existing error-handling sufficient at the API boundary.
  Compiler-lead disputes this: the new codegen emission path in compiler/emit.ts:214
  bypasses the existing guard entirely — a regression surface the IA section did not
  reach because it does not own compilation outputs."

F-01 [P1/P2/P3] [finding specific to this role's domain — names a code surface,
     function, or contract — not a category]
     Owner: [role] | Resolution: [concrete action naming what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings; more if the diff warrants it]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Validity check per finding: would only this role raise this finding given their domain
lens? If any generic reviewer could write the same sentence, revise it until it carries
the role's domain signal.

---

**STEP 4 — CONSENSUS ANALYSIS**

Read across all sections. Identify agreement, divergence, and the critical finding.

For every divergence: name the structural or architectural mechanism that causes two
roles to rate the same change differently. Perspective labels are not mechanisms.

**Perspective-label ban list — self-audit checklist. Scan every divergence explanation
against all five phrases before submitting:**

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from their perspective" (when used as the sole cause of divergence) — BANNED

Each phrase is independently checkable. If any banned phrase appears in a divergence
explanation, replace it with the architectural mechanism — even if a mechanism is also
named alongside it.

```
## Consensus Analysis

Inertia baseline: IA rated null hypothesis [HIGH/MEDIUM/LOW].
  Technical roles [confirm / challenge / defeat] this verdict.
  [One sentence on what the technical reviews collectively did to the IA baseline.]

Agreement: [area] — [role-A] and [role-B] independently raised [concern]

Divergence: [role-A] rates [concern] P1; [role-B] rates it P3.
  Mechanism: [specific property of the code — what makes one role see P1 and the
  other see P3, stated as a code or architectural fact, not a role attribute]

Critical: [F-XX from role] — [one sentence on why this finding most threatens the merge]
```

If no divergence: omit the Divergence line.
If no agreement: write "No cross-role convergence detected — findings cover
non-overlapping surfaces."

---

**STEP 5 — RECOMMENDATION**

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms resolution before merge]
2. [additional condition if present] — sign-off: [role]
```

Exactly one decision. Delegated or hedged decisions ("the team should decide") fail.

---

**AMEND**

When run with `--amend`, output this block before the routing table:

```
AMEND SCOPE
What was amended: [description]
Roles added: [list or "none"]
Roles removed: [list or "none"]
Prior findings superseded: [F-ID list or "none — prior findings stand"]
```

Then run the full sequence for the amended scope.

---

## V-02 — Output Format: Table-Centric with IA Anchor Row

**Axis**: Output format
**Hypothesis**: In a table-centric format, the IA anchor can be implemented as a
dedicated labeled field above each per-role findings table — making it structurally
impossible to omit. A missing field is immediately visible in a tabular layout in a
way a missing prose sentence is not. C-14 becomes a format contract rather than a
behavioral instruction, and the ban list (C-13) is surfaced as a column constraint on
Divergence rows in the consensus table rather than embedded prose.

---

You are running `/corps-pr`. Route this pull request through the org for pre-merge
review. All output follows structured table format. Follow the format contract exactly.

**INPUT**

- PR diff (files changed and nature of each change)
- `org.yaml` (role scope patterns)
- `.roles/` (role orientations and domain lenses)

---

**TABLE 1 — ROUTING**

Produce before any review begins. Do not begin reviews until this table is complete.

| File / File Group | Change Type | Role Selected | org.yaml Scope Pattern |
|-------------------|-------------|---------------|------------------------|
| [paths]           | [add/modify/delete] | [role name] | [pattern that matched] |
| (all files)       | default     | Inertia Advocate | default — always included |

If any file has no org.yaml match, add a coverage gap table immediately below:

| File | Gap Reason |
|------|------------|
| [path] | No org.yaml scope pattern matches this file. |

---

**TABLES 2–N — FINDINGS (one table per role)**

Inertia Advocate runs first. Their findings table appears before all technical role
tables. Then run each technical role in this sequence: security and compliance first →
domain-specific → PM/TPM last.

**Inertia Advocate findings table:**

```
## Inertia Advocate — Findings

Null hypothesis: [what the codebase currently does in this area — one sentence]
Null hypothesis strength: HIGH / MEDIUM / LOW

| ID   | Finding                | Severity | Owner  | Resolution         |
|------|------------------------|----------|--------|--------------------|
| F-01 | [argument status quo is sufficient — names an existing mechanism, not a category] | P1/P2/P3 | [role] | [concrete action] |
| F-02 | [second argument]      | P1/P2/P3 | [role] | [concrete action]  |
| TOTAL | —                     | —        | [N] findings: [x] P1, [y] P2, [z] P3 | — |

IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

**Technical role findings table (one per role):**

```
## [role name] — Findings

Source files: [files from routing table that triggered this role]
Orientation: [one phrase from .roles/]

IA anchor: IA verdict was [BLOCK/CONDITION/PASS]. IA's most relevant finding for
this domain: [brief summary of the IA finding that bears on this role's scope].
This role [confirms / extends / disputes] that assessment because: [architectural
or code-level reason — names the code surface, not the perspectives].

| ID   | Finding                | Severity | Owner  | Resolution         |
|------|------------------------|----------|--------|--------------------|
| F-01 | [domain-specific finding — names exact function, module, interface, or changed line] | P1/P2/P3 | [role] | [concrete action] |
| F-02 | [second finding]       | P1/P2/P3 | [role] | [concrete action]  |
| TOTAL | —                     | —        | [N] findings: [x] P1, [y] P2, [z] P3 | — |
```

Column contract:
- **Finding**: must name a specific function, module, interface, or changed line — not
  a category. "Auth concern" fails. "Token expiry check missing on silent-refresh path
  in `auth/middleware.ts:88`" passes.
- **Severity**: exactly P1 (blocking), P2 (resolve before merge), P3 (advisory).
- **Owner**: the role responsible for resolution.
- **Resolution**: one concrete action naming what to do and where.
- **TOTAL row**: required. A section without a TOTAL row fails.
- **IA anchor field**: required for every technical role table. A section without a
  filled IA anchor field is incomplete regardless of findings quality.

---

**TABLE N+1 — CONSENSUS**

After all per-role findings tables:

| Signal     | Finding Area       | Roles                     | Mechanism / Notes                  |
|------------|--------------------|---------------------------|------------------------------------|
| Inertia    | IA null hypothesis | Inertia Advocate          | [HIGH/MEDIUM/LOW — one sentence on how technical reviews responded] |
| Agreement  | [area both flagged] | [role-A], [role-B]       | [one sentence on the shared concern] |
| Divergence | [area where rates differ] | [role-A (P1)], [role-B (P3)] | [structural property of the code causing the difference] |
| Critical   | [most important finding] | [role]               | [why this one most threatens the merge] |

**Divergence Mechanism — self-audit ban list:**
Scan every Mechanism cell in Divergence rows against all five phrases before submitting:
- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" (as sole cause of divergence) — BANNED

Each phrase is independently checkable. A Divergence Mechanism cell containing any
banned phrase fails even if a code mechanism is also named in the same cell.

---

**TABLE N+2 — RECOMMENDATION**

| Decision | Primary Finding | Conditions | Sign-off Role |
|----------|-----------------|------------|---------------|
| GO / NO-GO / GO WITH CONDITIONS | [F-XX from [role] — one sentence] | [condition text or "none"] | [role name or "none"] |

If GO WITH CONDITIONS: Conditions cell must name what resolves the condition.
Sign-off Role must name the role that confirms resolution before merge.
One decision value only. Hedged decisions ("the team should consider") fail.

---

**AMEND**

When run with `--amend`, output this block before TABLE 1:

```
AMEND SCOPE
What changed: [description]
Roles added: [list or "none"]
Roles removed: [list or "none"]
Prior findings superseded: [F-ID list or "none"]
```

Then run the full table sequence for the amended scope.

---

## V-03 — Phrasing Register: Convince the Skeptic

**Axis**: Phrasing register
**Hypothesis**: Framing the IA as "the skeptic in the room" and asking each technical
role to respond to the skeptic before stating their own findings produces IA anchoring
that feels like a natural dialogue rather than a template obligation. The model is more
likely to write substantive IA anchors because the framing matches how real technical
discussions work: you acknowledge the skeptic's strongest argument before making your
own case. The ban list is embedded as explicit dialogue rules — "when explaining why
two people disagree, say what in the code causes it, not what in their jobs does."

---

You are running `/corps-pr`. Your job is to find out what would happen if this PR went
into a room with the people who own the affected code — and one very skeptical person
who thinks it probably should not merge at all.

---

**Read the room before anyone speaks**

Open `org.yaml`. Know who owns what file path.
Open the PR diff. Know what changed and in which files.
Open `.roles/`. Know what each person in that room actually worries about —
what failure modes they have been burned by, what they look for first.

---

**Step 1 — Decide who is in the room**

Go through each changed file. For each file or logical group: who in org.yaml owns
this path? Write them down before anyone starts talking:

```
Who reviews this PR:
- Inertia Advocate (always in the room)
- [role name]: files [path, path] — because [org.yaml scope reason — one sentence]
- [role name]: file [path] — because [org.yaml scope reason]
```

If any file has no owner: "No one in org.yaml covers [path] — coverage gap."

Do not skip files. Do not leave anything unaccounted for.

---

**Step 2 — The skeptic goes first**

Before anyone else speaks, the Inertia Advocate states their case. They represent the
system as it currently works. Their job is to ask the hardest possible question: why
does this need to change at all?

They are not hostile — they are the person who has been burned before by a "fix" that
introduced more problems than it solved. They want to know exactly what the current
implementation fails to do that justifies this PR.

```
## Inertia Advocate

The current system: [what the codebase currently does in this area — one sentence]
The skeptic's question: [what condition would need to be true for this PR to be
justified against the status quo]

F-01 [P1/P2/P3] [specific reason the current approach may be sufficient — names an
     existing mechanism or path]
     Owner: [who owns this] | Fix: [what would resolve this concern]
F-02 [P1/P2/P3] [second reason]
     Owner: [role] | Fix: [action]
[more if warranted; at least 2]

[N] findings — [x] P1, [y] P2, [z] P3
Skeptic's verdict: BLOCK / CONDITION / PASS — [one sentence]
```

---

**Step 3 — Everyone else responds, then reviews**

The technical reviewers have just heard the skeptic. They do not get to ignore what
the Inertia Advocate said. Before raising their own concerns, each reviewer must
acknowledge the skeptic's position and explain where they agree, partially agree, or
disagree — and why.

"We see this differently" is not a reason. The reason must be in the code.

For each reviewer in the room:

```
## [role name]

These files put me here: [paths from routing]
What I look at: [one phrase from .roles/ — the failure mode I am trained to catch]

Responding to the skeptic: The Inertia Advocate [said / found] [brief restatement of
IA's verdict or the IA finding most relevant to this role's domain]. From where I sit,
they are [right / partially right / missing something important] — specifically because
[architectural or code-level reason: name the mechanism. "We see this differently" is
not a reason. "The IA section reviewed the service boundary but the new codegen path
bypasses that boundary entirely" is a reason.].

F-01 [P1/P2/P3] [finding from my domain — names a specific function, module, or
     code surface — not a category]
     Owner: [who] | Fix: [concrete action, named location]
F-02 [P1/P2/P3] [second finding]
     Owner: [who] | Fix: [action]
[more if warranted; at least 2]

[N] findings — [x] P1, [y] P2, [z] P3
```

Finding check: does this finding carry this reviewer's voice? Could only they have
raised it given their domain? A finding that any reviewer could write regardless of
role — rewrite it.

---

**Step 4 — What the room decided**

Once everyone has spoken, step back and read across the sections.

Did two people independently flag the same thing? That is the most reliable signal —
it survived two different lenses arriving at the same place without coordination.

Did two people rate the same change at different severities? Work out why — not "they
have different jobs" (that is obvious), but what specific property of the code makes
one of them see a P1 and the other a P3.

When explaining why two reviewers disagree, say what causes it in the code, not in
the people. These phrases are banned in any disagreement explanation — check your
output against all of them before finishing:

**Banned phrases (check each independently — any present in a disagreement
explanation fails):**
- "they have different perspectives" — names no code property
- "they prioritize differently" — names no mechanism
- "they see this through different lenses" — metaphor, not cause
- "their roles lead them to different conclusions" — circular, not structural
- "it comes down to their focus area" — role label, not code fact

Replace with: what specific code property, system boundary, or architectural
constraint causes the rating difference?

```
## What the room decided

Skeptic's position: IA rated the status quo as [HIGH/MEDIUM/LOW] risk to change.
  The technical reviews [confirmed / partially challenged / defeated] that position.
  [One sentence on which technical finding most directly engaged the IA verdict.]

Agreed on: [area two or more reviewers independently raised]

Disagreed on: [concern] — [role-A] rates P1; [role-B] rates P3.
  Why: [specific code property, system boundary, or architectural fact causing the
  difference — not a reviewer attribute]

Biggest risk: [F-XX from role] — [why this finding most threatens the merge]
```

If no disagreement: omit the Disagreed block.
If no agreement: write "No shared concern detected — findings cover non-overlapping
surfaces."

---

**Step 5 — The call**

One of three outcomes. Pick one:

```
## The call

Decision: GO / NO-GO / GO WITH CONDITIONS
Why: [F-XX from [role] — one sentence]

Before merge (if applicable):
1. [what must be fixed] — confirmed by: [role]
2. [second condition] — confirmed by: [role]
```

No hedging. No "the team should weigh." The PR merges, does not merge, or merges
after named conditions are met by named roles.

---

**To amend:**

Add a reviewer: `/corps-pr --amend add:[role]`
Say: what role was added, which files triggered the addition, which earlier findings
(if any) are superseded.

Change scope: `/corps-pr --amend scope:[domain]`
Say: which roles were removed, which earlier findings no longer apply.

---

## V-04 — Lifecycle Emphasis + Inertia Framing: Phase-Gated with IA Anchor Gate

**Axes**: Lifecycle emphasis (explicit phase gates with entry/exit conditions) +
Inertia framing (IA section as the entry gate that unlocks technical role reviews)
**Hypothesis**: Making the completed IA section the entry condition for Sub-phase 2B,
and making each technical role's IA anchor the entry condition for writing that role's
findings, positions C-14 as a structural gate rather than a style preference. The
model cannot begin writing technical findings until the IA anchor field is filled —
the sequence constraint and the anchor requirement reinforce each other. C-13 is
enforced as an explicit Phase 3 self-audit step before Phase 4 is permitted to begin.

---

You are running `/corps-pr`. Execute in four phases. Do not begin a phase until its
entry condition is satisfied. Do not begin writing findings for any technical role
until that role's IA anchor is completed.

---

## PHASE 1 — ROUTE

**Entry condition**: PR diff and `org.yaml` available.
**Exit condition**: routing table complete; every changed file assigned to a role or
explicitly flagged as unowned.

**R1** Read `org.yaml` — extract scope patterns and role definitions.
**R2** Read the PR diff — list every changed file.
**R3** Match each file to an org.yaml scope pattern. Assign the first matching role.
**R4** Write the routing table:

```
## Routing Table

| File / File Group | Change Type | Role | org.yaml Scope Pattern |
|-------------------|-------------|------|------------------------|
| [paths]           | [add/modify/delete] | [role] | [pattern] |
```

**R5** Add the Inertia Advocate as a default entry:
`| (all changed files) | — | Inertia Advocate | default — always included |`

**R6** Coverage gaps: any file with no org.yaml match → add below the routing table:

```
COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.
```

**Phase 1 complete.** Phase 2 entry condition met.

---

## PHASE 2 — REVIEW

**Entry condition**: routing table complete.
**Exit condition**: every role from the routing table has a findings section; every
technical role section has a filled IA anchor.

### Sub-phase 2A — Inertia Advocate

The Inertia Advocate section must be written and complete before any technical role
section begins. Sub-phase 2B may not begin until this section is done.

```
## Review: Inertia Advocate

Null hypothesis: The codebase currently [does X via mechanism Y]. The switching cost
is [Z]. This PR is justified only if [condition].
Null hypothesis strength: HIGH / MEDIUM / LOW
  HIGH   — the "do nothing" case is credible and the PR does not address it
  MEDIUM — the PR names the problem but does not justify the switching cost
  LOW    — the PR directly defeats the status quo argument

F-01 [P1/P2/P3] [argument the status quo is sufficient — names an existing mechanism]
     Owner: [role] | Resolution: [what resolves this finding]
F-02 [P1/P2/P3] [second argument]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
IA verdict: BLOCK / CONDITION / PASS — [one sentence]
```

**Sub-phase 2A complete.** The IA verdict above is the reference object for Sub-phase 2B.

### Sub-phase 2B — Technical Role Reviews

Entry condition: Sub-phase 2A complete (IA verdict written above).

Sequence: security and compliance roles first → domain-specific roles → PM/TPM last.

**Entry condition for each role section within 2B**: IA anchor filled before any
findings are written. Do not write F-01 until the IA anchor field is complete.

```
## Review: [role name]

Source files: [files from routing table that triggered this role]
Orientation: [one phrase from .roles/]

IA anchor: [Required — complete this field before writing findings.
  State: (a) what the IA's verdict was, (b) which IA finding is most relevant to
  this role's domain, (c) whether this role confirms, extends, or disputes that
  finding, and (d) the architectural or code-level reason for any divergence.
  Example: "IA verdict: CONDITION. IA found existing pagination logic sufficient
  at the service boundary. Compiler-lead disputes: the new emission path in
  codegen/emit.ts:214 bypasses that guard entirely — a regression surface the IA
  section did not reach because it does not own compilation outputs."]

F-01 [P1/P2/P3] [finding from this role's domain — names a code surface, function,
     or contract — not a category]
     Owner: [role] | Resolution: [concrete action naming what and where]
F-02 [P1/P2/P3] [second finding]
     Owner: [role] | Resolution: [concrete action]
[minimum 2 findings; more if the diff warrants it]

Summary: [N] findings — [x] P1, [y] P2, [z] P3
```

Validity check per finding: is this finding specific to this role's domain? If a
generic reviewer could write the same sentence regardless of their role, revise it.

**Phase 2 complete** when every routing-table role has a section and every technical
role section has a filled IA anchor.

---

## PHASE 3 — SYNTHESIZE

**Entry condition**: all role findings sections complete (Phase 2 exit reached).
**Exit condition**: consensus analysis written; Phase 3 self-audit checklist cleared.

Read across all findings sections. Produce three components:

**A — Inertia baseline status**
State what the technical role reviews collectively did to the IA baseline: confirmed,
partially challenged, or defeated it. Name which technical finding most directly
engaged the IA verdict.

**B — Cross-role signals**
Agreement: a concern raised independently by two or more roles.
Divergence: the same code change rated at different severities by two roles.
For every divergence: name the structural or architectural mechanism causing the
rating difference.

**C — Critical finding**
The single finding that most threatens the merge if unresolved.

```
## Consensus Analysis

Inertia baseline: IA rated null hypothesis [HIGH/MEDIUM/LOW].
  Technical reviews [confirm / partially challenge / defeat] this verdict.
  [One sentence on which technical finding most directly engaged the IA baseline.]

Agreement: [area] — independently raised by [role-A] and [role-B]

Divergence: [role-A] rates [concern] P1; [role-B] rates it P3.
  Mechanism: [structural or architectural property of the code causing this difference
  — names a code surface, system boundary, or contract — not a reviewer attribute]

Critical finding: [F-XX from role] — [one sentence on why this threatens the merge
most]
```

**Phase 3 self-audit — complete before Phase 4 begins:**
Scan every Divergence Mechanism line against this ban list. Each phrase is
independently checkable. Any banned phrase present fails C-13, even if a mechanism
is also named:

- `[ ]` "they have different perspectives" — BANNED
- `[ ]` "they prioritize differently" — BANNED
- `[ ]` "they see this through different lenses" — BANNED
- `[ ]` "their roles lead them to different conclusions" — BANNED
- `[ ]` "from [role]'s perspective" (as sole explanation of divergence) — BANNED

All five boxes must be checkable-clear before Phase 4 begins.

**Phase 3 complete** when consensus analysis is written and self-audit is clear.

---

## PHASE 4 — DECIDE

**Entry condition**: Phase 3 self-audit complete.
**Exit condition**: recommendation written.

```
## Recommendation

Decision: GO / NO-GO / GO WITH CONDITIONS
Primary reason: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
1. [what must be resolved] — sign-off: [role who confirms resolution before merge]
2. [additional condition] — sign-off: [role]
```

Exactly one decision value. Delegated decisions ("the team should weigh") fail.

---

**AMEND**

Before Phase 1, if `--amend` is set:

```
AMEND SCOPE
What was amended: [description]
Roles added: [list or "none"]
Roles removed: [list or "none"]
Prior findings superseded: [F-ID list or "none — prior findings stand"]
```

- `--amend add:[role]`: Sub-phase 2B reruns for the added role only. Phases 3 and 4
  rerun. Phase 3 self-audit reruns.
- `--amend scope:[domain]`: Phase 1 reruns with filtered scope. Phases 2–4 rerun.

---

## V-05 — Formal/Terse Register + Ban List as Named Artifact

**Axes**: Phrasing register (formal/technical, imperative, dense) + consensus
mechanism (ban list as a named numbered artifact BL-01 through BL-05, referenced by
ID throughout the output)
**Hypothesis**: Surfacing the perspective-label prohibition as a named, numbered
artifact that the skill references by ID — rather than embedding it as instructional
prose — makes C-13 a checkable external standard rather than an embedded reminder.
A model generating output can scan against BL-01 through BL-05 as a first-class
audit step. The formal register keeps the protocol dense and mechanical; the numbered
ban list is a contract component, not a style note. C-14 is implemented as a mandatory
IA ANCHOR field in the technical role section template — named in the contract, not
described in instructions.

---

You are running `/corps-pr`. Execute the following protocol. Deviations from format
requirements are failures.

---

## BAN LIST — Perspective-Label Prohibition

The following phrases are prohibited in all divergence explanations. Each is
independently auditable. Reference by ID throughout this run.

| ID    | Banned Phrase                                          | Failure Reason                                     |
|-------|--------------------------------------------------------|----------------------------------------------------|
| BL-01 | "they have different perspectives"                     | Names role identity, not code mechanism            |
| BL-02 | "they prioritize differently"                          | Attributes divergence to preference, not property  |
| BL-03 | "they see this through different lenses"               | Metaphorical; names no architectural constraint    |
| BL-04 | "their roles lead them to different conclusions"       | Circular; the role is the reviewer; names no fact  |
| BL-05 | "from [role]'s perspective" (as sole divergence cause) | Perspective label without structural grounding     |

Any divergence explanation containing a phrase matching BL-01 through BL-05 fails,
even if a mechanism is also named in the same sentence. Scan before submitting.

---

## SECTION 1 — ROUTING

Precondition: `org.yaml` and PR diff available.

For each changed file, match to an org.yaml scope pattern. Assign one role per file
or logical file group. Always include the Inertia Advocate as a default reviewer.

```
ROUTING

| File / File Group | Type        | Role             | Scope Pattern       |
|-------------------|-------------|------------------|---------------------|
| [paths]           | [add/mod/del] | [role]           | [pattern]           |
| (all files)       | default     | Inertia Advocate | default — always included |
```

Any file with no scope pattern match:
```
COVERAGE GAP: [file] — no org.yaml scope pattern.
```

---

## SECTION 2 — INERTIA ADVOCATE

Inertia Advocate output precedes all technical role sections. Ordering is structural —
not configurable.

The IA section establishes the null hypothesis: the case for not merging. Technical
roles read this section before producing their own output. The IA verdict is the
reference object the consensus section measures all technical findings against.

```
INERTIA ADVOCATE

Null hypothesis: [what the system currently does; why it may already be sufficient]
Null hypothesis strength: HIGH | MEDIUM | LOW

F-01 [P1|P2|P3] [argument against merging — names an existing mechanism specifically]
     Owner: [role] | Resolution: [concrete action]
F-02 [P1|P2|P3] [second argument]
     Owner: [role] | Resolution: [concrete action]
[>=2 findings required]

Summary: [N] findings — [x]P1 [y]P2 [z]P3
IA verdict: BLOCK | CONDITION | PASS — [one sentence]
```

---

## SECTION 3 — TECHNICAL ROLE REVIEWS

Sequence: compliance/security roles first → domain-specific roles → PM/TPM last.

For each role, the IA ANCHOR field is mandatory. Complete it before writing findings.
A technical section without a completed IA ANCHOR field is incomplete regardless of
findings quality.

```
[ROLE NAME]

Files: [source files from routing]
Scope: [one phrase from .roles/]

IA ANCHOR: IA verdict was [BLOCK|CONDITION|PASS]. IA's most relevant finding for
this domain: [one-phrase summary of the IA finding bearing on this role's scope].
This role [confirms|extends|disputes] because: [architectural mechanism — must not
match BL-01 through BL-05. Name the code surface, boundary, or contract that makes
this role's view differ from the IA's.].

F-01 [P1|P2|P3] [domain-specific finding — names exact code surface, not a category]
     Owner: [role] | Resolution: [concrete action]
F-02 [P1|P2|P3] [second finding]
     Owner: [role] | Resolution: [concrete action]
[>=2 findings required]

Summary: [N] findings — [x]P1 [y]P2 [z]P3
```

Finding validity: a finding that any reviewer could write regardless of domain fails.
Rewrite until only this role's domain lens produces it.

---

## SECTION 4 — CONSENSUS

After all role sections.

```
CONSENSUS

Inertia baseline: IA null hypothesis rated [HIGH|MEDIUM|LOW].
  Technical findings: [confirm | partially challenge | defeat] this verdict.
  Basis: [which technical finding most directly engaged the IA baseline, and how]

Agreement: [concern area] — [role-A], [role-B] raised independently

Divergence: [role-A] rates [concern] [P1]; [role-B] rates [P3].
  Mechanism: [structural code property causing the difference — must not match
  BL-01 through BL-05. A passing mechanism names a code property, system boundary,
  or architectural constraint — not a reviewer attribute.]

Critical: [F-XX from role] — [why this finding most threatens the merge]
```

BL audit: before submitting, scan the Mechanism line against BL-01 through BL-05.
Each ID is independently checkable. All five must be clear.

---

## SECTION 5 — RECOMMENDATION

```
RECOMMENDATION

Decision: GO | NO-GO | GO WITH CONDITIONS
Basis: [F-XX from [role] — one sentence]

Conditions (GO WITH CONDITIONS only):
C-01: [what must be resolved] — sign-off: [role]
C-02: [second condition if present] — sign-off: [role]
```

One decision value. Hedged or delegated decisions are protocol failures.

---

## AMEND PROTOCOL

When `--amend` is active, output this block before SECTION 1:

```
AMEND
Amended: [description]
Roles added: [list | none]
Roles removed: [list | none]
Findings superseded: [F-ID list | none]
```

`--amend add:[role]`: SECTION 3 reruns for added role only. SECTIONS 4–5 rerun.
`--amend scope:[domain]`: All sections rerun with filtered scope.
