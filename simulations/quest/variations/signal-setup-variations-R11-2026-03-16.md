---

# quest:variate — signal-setup — Round 11

**Skill:** `signal-setup`
**Rubric version:** v10 (C-01 through C-30, denominator A=22)
**Variation count:** 5

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Inertia framing (single) | Naming inertia as a recurring adversary throughout — not just in the preamble — gives every gate a consistent opponent to reference, producing higher C-16/C-17/C-18/C-19/C-21/C-22 scores |
| V-02 | Phrasing register — formal/technical imperative (single) | Stripped-down imperative prose reduces hedging that blurs gate boundaries, producing cleaner C-27/C-29 compliance |
| V-03 | Lifecycle emphasis — verbose gate treatment (single) | Allocating maximum prose per gate forces non-overlapping consequence vocabulary (C-22), explicit phase labels (C-23), and consistent argument threading (C-19) |
| V-04 | Inertia framing + conversational register (combined) | Adversary framing in conversational register is more resonant for C-13/C-16/C-17 but requires explicit structural compensation to avoid C-27/C-29 penalties |
| V-05 | Table-driven gate index + lifecycle emphasis (combined) | A gate index table before prose makes full phase structure machine-readable before any prose is read (C-11/C-25/C-29); verbose gate bodies deliver C-22/C-23 |

---

## V-01: Inertia as Named Adversary

**Axis:** Inertia framing (single-axis)
**Hypothesis:** Naming inertia as an active opponent throughout — not merely describing it as a concept in the preamble — provides a consistent referent for phase-indexed consequence language at every exit gate without requiring the reader to recall the preamble framing.

---

```markdown
# Signal Setup

## Why This Matters

Inertia is already present in your workspace. It has no name and asks no questions.
Every session that begins without a reminder to challenge assumptions is a session
where inertia wins by default. Signal setup does one thing: it gives Claude a standing
instruction to ask "why would a team do nothing?" before the next feature commitment
is made. Once that instruction is written into CLAUDE.md, it persists — automatically
loaded every session without you having to remember. Setup happens once. The reminder
lives forever. You are choosing a side.

---

## GATE 1: File Detection

Read `CLAUDE.md` in the workspace root.

**Routing:**
- CLAUDE.md does not exist → GATE 1B
- CLAUDE.md exists, contains a Signal section → GATE 1A
- CLAUDE.md exists, no Signal section found → GATE 2

### GATE 1A: Signal Already Configured

Signal is already configured in this workspace. CLAUDE.md contains an existing
Signal section.

> Signal is already configured here. CLAUDE.md loads automatically at the start of
> every Claude Code session — which means the inertia question is already present in
> your context without you having to think about it. Inertia has a named opponent in
> this workspace, and that opponent shows up before your first message, every session.
> No changes needed.

End here.

### GATE 1B: CLAUDE.md Missing

CLAUDE.md does not exist in this workspace.

> No CLAUDE.md found. Signal setup writes a Signal section into CLAUDE.md. Without
> CLAUDE.md, there is no file to carry the inertia reminder into your sessions.
>
> Options:
> - **Create CLAUDE.md with Signal section** — creates the file and writes the Signal
>   section as its initial content
> - **Abort** — leaves the workspace unconfigured

Wait for user choice.

**Routing:**
- User chooses Create → GATE 2 (write step will create the file)
- User chooses Abort → GATE 1B-Abort

#### GATE 1B-Abort

> Setup aborted. CLAUDE.md was not created. There is no persistent reminder in your
> context to ask "why would teams do nothing?" before the next feature is committed.
> Inertia is present at the planning stage — the moment before a spec is drafted and
> direction is locked — and it will remain uncontested there until Signal has a file
> to live in.

End here.

---

## GATE 2: Preview

Show the user a preview of the Signal section that will be appended.

The Signal section must include:
- A `# Signal` heading
- A one-sentence description of Signal as a developer tool for feature decision-making
- The nine namespace skills: scout, draft, review, flow, trace, prove, listen, program, topic
- The inertia rule: "When enough signals exist, the topic tells you you're ready"
- A reference to `/topic:` as the narrative coordinator

Format the preview inside a fenced code block.

> Here is what Signal Setup will append to CLAUDE.md:
>
> [fenced code block — exact Signal section content]
>
> This is the complete change. Nothing else in CLAUDE.md will be modified.

---

## GATE 3: Confirmation

Ask the user to confirm before writing.

> Append this Signal section to CLAUDE.md?

Wait for response.

**Routing:**
- User confirms → GATE 4
- User declines → GATE 3A

### GATE 3A: User Declines

> Signal section not written. CLAUDE.md remains unchanged. Inertia is still
> uncontested at the planning stage — before a spec is committed and feature direction
> is locked. That is when inertia operates most effectively: not by arguing, but by
> ensuring no one asks the question. Signal would have asked it automatically at the
> start of every session. It will not be there the next time you open this workspace.

End here.

---

## GATE 4: Write

Append the Signal section (exactly as previewed in GATE 2) to CLAUDE.md.

If CLAUDE.md did not exist (path from GATE 1B create branch): create the file and
write the Signal section as its sole content.

The written content must be byte-identical to the previewed content. No additions,
no reformatting, no drift.

---

## GATE 5: Report

> Signal section appended to CLAUDE.md. Every Claude Code session in this workspace
> will now load the inertia question automatically — before your first message, every
> time. Inertia has a standing opponent here.

---

## GATE 6: Copilot Extension Offer

Ask whether the user wants to update `.github/copilot-instructions.md` as well.

Check whether `.github/copilot-instructions.md` exists and already contains a Signal
section.

If an existing Signal section is found: respond inline —
"Copilot instructions already include Signal. The inertia question is present during
Copilot suggestions at the implementation phase — when you are writing function bodies
and endpoint signatures, not only when planning." (No sub-gate needed — this is a
detection skip path in an optional-extension gate, not a confirmation checkpoint.)
End GATE 6.

Otherwise:

> CLAUDE.md now covers the planning phase — spec authoring, feature decisions. Would
> you also like to add a Signal section to .github/copilot-instructions.md? That
> extends inertia coverage to the implementation phase, where Copilot is suggesting
> function bodies and endpoint signatures before interfaces lock.

Wait for response.

**Routing:**
- User confirms → GATE 6A
- User declines → GATE 6-Decline

### GATE 6A: Write Copilot Instructions

Append an equivalent Signal section to `.github/copilot-instructions.md`. Create the
file and `.github/` directory if they do not exist.

> Signal section added to .github/copilot-instructions.md. Copilot will now carry the
> inertia question into implementation sessions — asking "why would teams do nothing?"
> at the moment a function body is being written, before the interface commits.

### GATE 6-Decline

> Copilot instructions not updated. The implementation phase — when you are writing
> functions and Copilot is making suggestions — will proceed without a standing inertia
> check. CLAUDE.md covers the planning stage. This gap is specifically at the
> implementation phase, before endpoint signatures are committed in code.
```

---

## V-02: Formal/Technical Imperative Register

**Axis:** Phrasing register (single-axis)
**Hypothesis:** Stripped-down imperative commands reduce hedging prose that blurs gate boundaries and routing logic, producing cleaner structural compliance on C-27 and C-29. Motivational content is present but minimal — enough to satisfy C-13/C-16/C-17 without consuming space that belongs to structural clarity.

---

```markdown
# Signal Setup

## Purpose

Signal setup writes a persistent inertia reminder into your workspace. CLAUDE.md is
loaded by Claude Code at session start. A Signal section in CLAUDE.md means the inertia
question — "why would teams do nothing?" — is present at every session without manual
intervention. This configuration is a one-time act; the effect is permanent. Inertia is
the condition where teams do nothing by default; this configuration makes opposition to
that condition automatic. You are registering opposition to a named adversary as a
standing workspace policy.

---

## GATE 1: CLAUDE.md Detection

**Action:** Read `CLAUDE.md` from workspace root. Search for an existing Signal section.

**Routing:**
- `CLAUDE.md` absent → GATE 1B
- `CLAUDE.md` present, Signal section found → GATE 1A
- `CLAUDE.md` present, Signal section absent → GATE 2

### GATE 1A: Existing Signal Section Detected

**Action:** Output the following response, then terminate.

> Signal is already configured. CLAUDE.md is loaded automatically by Claude Code at
> session start — the inertia check is present in your context every session without
> manual action. The mechanism is already working. No write required.

### GATE 1B: CLAUDE.md Absent

**Action:** Output the following prompt. Await user input.

> `CLAUDE.md` was not found in the workspace root. Signal setup requires a CLAUDE.md
> to carry the inertia reminder into sessions. Without it, there is no file that
> Claude Code loads at session start, and no persistent inertia check.
>
> Select an option:
> - Create `CLAUDE.md` with Signal section as sole content
> - Abort setup

**Routing:**
- User selects create → GATE 2 (file creation mode)
- User selects abort → GATE 1B-Abort

#### GATE 1B-Abort

**Action:** Output the following response, then terminate.

> Setup aborted. `CLAUDE.md` was not created. No inertia check is present in your
> context. At the planning stage — before a spec is drafted and feature direction is
> committed — inertia operates without opposition. That is the phase where a standing
> question would have the most structural impact.

---

## GATE 2: Preview Generation

**Action:** Generate the exact Signal section text that will be written. Display it
in a fenced code block.

**Signal section content requirements:**
- Heading: `# Signal`
- One-sentence description of Signal's purpose
- Namespace list: scout, draft, review, flow, trace, prove, listen, program, topic
- Inertia rule: "When enough signals exist, the topic tells you you're ready"
- Reference to `/topic:` as narrative coordinator

Output:

> The following Signal section will be appended to `CLAUDE.md`. Review it before
> confirming.
>
> [fenced code block — exact content]

---

## GATE 3: Write Confirmation

**Action:** Output the following prompt. Await user input.

> Append this Signal section to `CLAUDE.md`?

**Routing:**
- User confirms → GATE 4
- User declines → GATE 3A

### GATE 3A: Write Declined

**Action:** Output the following response, then terminate.

> Write declined. `CLAUDE.md` is unchanged. The inertia check will not be present
> at session start. At the planning stage — when a spec is being drafted — there is
> no standing instruction to ask "why would teams do nothing?" before direction is
> committed. That question remains unasked until Signal is configured.

---

## GATE 4: Write Execution

**Action:**
- If appending: append the previewed Signal section to `CLAUDE.md`.
- If creating (path from GATE 1B): create `CLAUDE.md`, write the Signal section as
  its sole content.
- Written content must be byte-identical to the previewed content from GATE 2.

---

## GATE 5: Write Confirmation Report

**Action:** Output the following response.

> Signal section written to `CLAUDE.md`. Claude Code loads this file automatically
> at the start of every session in this workspace. The inertia check is now a
> standing workspace policy at the planning phase.

---

## GATE 6: Copilot Instructions Extension

**Action:** Prompt the user for optional Copilot configuration. First check whether
`.github/copilot-instructions.md` exists and contains an existing Signal section.

If an existing Signal section is found: output inline —
"Copilot instructions already contain a Signal section. The inertia check is present
during Copilot implementation suggestions — at the implementation phase, when function
signatures are being committed in code." (No sub-gate needed — this is a detection
skip path in an optional-extension gate, not a confirmation checkpoint.) Terminate
GATE 6.

Otherwise, output:

> `CLAUDE.md` now carries the inertia check at the planning phase. Optionally, a
> Signal section can also be added to `.github/copilot-instructions.md`, making the
> inertia check visible to Copilot at the implementation phase — when functions and
> endpoints are being written and interfaces begin to lock.
>
> Add Signal section to `.github/copilot-instructions.md`?

**Routing:**
- User confirms → GATE 6A
- User declines → GATE 6-Decline

### GATE 6A: Copilot Write Execution

**Action:** Append Signal section to `.github/copilot-instructions.md`. Create the
file and `.github/` directory if absent. Output:

> Signal section written to `.github/copilot-instructions.md`. Copilot will surface
> the inertia check during implementation — at the phase when a function body or
> endpoint signature is first written and the interface begins to lock.

### GATE 6-Decline

**Action:** Output the following response, then terminate.

> Copilot instructions not updated. The implementation phase — when Copilot is
> generating function bodies and endpoint signatures — will proceed without an inertia
> check. `CLAUDE.md` covers the planning phase. The gap is at implementation.
```

---

## V-03: Lifecycle Emphasis — Verbose Gate Treatment

**Axis:** Lifecycle emphasis (single-axis)
**Hypothesis:** Allocating substantial prose to each gate body — restating phase context, inputs, outputs, and phase-specific consequence — forces non-overlapping consequence vocabulary (C-22), makes phase labels explicit as direct text rather than implied through artifact names (C-23), and ensures no key argument is weaker at any equivalent exit gate (C-19).

---

```markdown
# Signal Setup

## Opening: The Problem This Solves

Before any feature is committed, before any spec is drafted, before any build is
kicked off — there is a moment when a team could choose not to act. Not because the
idea is bad, but because nothing forces the question. Inertia does not argue. It does
not need to. It wins by default in every session that begins without a standing
instruction to challenge it.

Signal setup exists to make that challenge automatic. It writes a Signal section into
CLAUDE.md — the file that Claude Code loads at the start of every session in this
workspace. Once the Signal section is present, the inertia question is present. You
do not have to remember to ask it. You do not have to be in the right frame of mind.
It is there before you open the first file.

You are not configuring a tool. You are registering opposition to a named condition —
inertia — and making that opposition a standing feature of your workspace. The
configuration happens once. The effect is permanent.

---

## GATE 1: File Detection Phase

**Phase context:** This is the entry gate. Before any preview is generated and before
any write is considered, the current state of the workspace must be established. Two
conditions must be known: whether CLAUDE.md exists, and if it does, whether it already
contains a Signal section. The answers determine every subsequent action.

**Action:** Read `CLAUDE.md` from the workspace root. Search for an existing Signal
section (a heading that identifies Signal configuration — `# Signal`, `## Signal`, or
equivalent marker).

**Routing:**
- `CLAUDE.md` is absent from the workspace root → GATE 1B
- `CLAUDE.md` is present and contains a Signal section → GATE 1A
- `CLAUDE.md` is present and does not contain a Signal section → GATE 2

### GATE 1A: Signal Section Already Present

**Phase context:** This gate handles the primary already-configured detection path for
the Signal configuration flow. The workspace is fully configured; no write is required.
The goal of this gate is not merely to acknowledge the absence of action — it is to
affirm what the existing configuration does for the user, name the mechanism by which
it achieves persistence across sessions, and close without unnecessary prompting.

**Action:** Output the following, then end the skill.

> Signal is already configured in this workspace.
>
> CLAUDE.md is loaded automatically by Claude Code at the start of every session —
> before your first message, every time you open this workspace. That is the mechanism:
> not a prompt you must remember, but a file that loads unconditionally. The Signal
> section in that file means the inertia question is already a standing feature of your
> workspace context. Inertia has a permanent opponent here, and that opponent is already
> showing up automatically. No changes needed.

### GATE 1B: CLAUDE.md Absent

**Phase context:** This gate handles the primary missing-file detection path in the
Signal configuration flow. CLAUDE.md is the vehicle for Signal's persistent reminder;
without it, setup cannot produce a durable configuration. This gate must fully explain
the dependency, present both resolution options, and await the user's decision. It is
not a fallthrough to an error — it is a decision gate with two explicit branches.

**Action:** Output the following prompt. Await user input.

> `CLAUDE.md` was not found in this workspace. Signal writes its inertia reminder into
> CLAUDE.md, which Claude Code loads automatically at session start. Without CLAUDE.md,
> the reminder has no persistent home — it cannot travel from session to session without
> a file that Claude Code is guaranteed to read.
>
> Signal can create `CLAUDE.md` now, with the Signal section as its initial content.
> You can add other workspace instructions to it later — it is just a markdown file.
>
> Options:
> - **Create `CLAUDE.md`** and continue with Signal setup
> - **Abort** — leave the workspace unconfigured for now

**Routing:**
- User selects Create → GATE 2 (write step will create the file rather than append)
- User selects Abort → GATE 1B-Abort

#### GATE 1B-Abort

**Phase context:** The user has chosen not to create CLAUDE.md. This is a Signal-absent
exit from the primary configuration flow at the planning-phase tool (Claude Code). The
consequence must name the planning stage explicitly and anchor the absence to a specific
future moment when the gap will be felt.

**Action:** Output the following, then end the skill.

> Setup aborted. `CLAUDE.md` was not created, and no Signal section will be written.
>
> At the planning stage — the next time you open this workspace to draft a spec or make
> a feature decision — there will be no standing instruction in your context to challenge
> inertia. That is the phase where inertia operates most effectively: not by arguing
> against good ideas, but by ensuring no one asks whether a team would act without the
> feature at all. The question will not be automatically present the next time direction
> is being committed here.

---

## GATE 2: Preview Phase

**Phase context:** The file state is confirmed: CLAUDE.md exists (or will be created)
and does not yet contain a Signal section. Before any write occurs, the user must see
exactly what will be written. This gate exists to close the gap between intent and
execution — the preview is the contract. GATE 4 will write exactly this content and
nothing more.

**Action:** Generate the Signal section content. Display it inside a fenced code block.

> Here is the exact Signal section that will be appended to `CLAUDE.md`. Nothing else
> will be modified. Review it before confirming.
>
> [fenced code block — Signal section content]

**Signal section must include:**
- A `# Signal` heading
- A brief description of Signal as a developer tool for feature decision-making
- The list of Signal namespaces: scout, draft, review, flow, trace, prove, listen,
  program, topic
- The inertia rule, stated explicitly: "When enough signals exist, the topic tells you
  you're ready"
- A reference to `/topic:` as the skill that coordinates the narrative across namespaces

---

## GATE 3: Confirmation Phase

**Phase context:** The user has seen the preview. This gate seeks a direct, unambiguous
confirmation before any file is modified. No write has occurred yet. The confirmation
is not ceremonial — it is the gate that separates reviewing from acting. Two branches
are possible; each has explicit handling below.

**Action:** Output the following prompt. Await user input.

> Append this Signal section to `CLAUDE.md`?

**Routing:**
- User confirms (yes, proceed, append, or equivalent) → GATE 4
- User declines (no, skip, abort, or equivalent) → GATE 3A

### GATE 3A: Write Declined

**Phase context:** The user has reviewed the full preview and chosen not to write.
This is a Signal-absent exit from the primary happy path at the planning-phase tool
(Claude Code). The consequence must name the planning stage as an explicit phase label
and anchor the absence to a specific future moment when it will be felt — distinct from
the GATE 1B-Abort framing, which addressed a user who never saw the preview.

**Action:** Output the following, then end the skill.

> Signal section not appended. `CLAUDE.md` is unchanged.
>
> At the planning stage — before a spec is drafted and feature direction is committed
> here — there is no standing instruction in your context to challenge inertia. That is
> the phase where inertia operates most effectively: not by arguing, but by ensuring
> no one asks whether teams would act without the feature. The next time you open this
> workspace to plan a feature, that question will not be automatically present.

---

## GATE 4: Write Phase

**Phase context:** Confirmation received. This gate executes the write. The content
written must be identical to the content previewed in GATE 2 — no additions, no
omissions, no reformatting. The preview was the contract; this gate honors it.

**Action:**
- If CLAUDE.md exists: append the Signal section to the end of the file.
- If CLAUDE.md was absent (path from GATE 1B create branch): create CLAUDE.md and
  write the Signal section as its sole content.
- Verify that the written content matches the previewed content exactly.

---

## GATE 5: Outcome Report Phase

**Phase context:** The write is complete. This gate closes the primary configuration
flow by reporting the outcome clearly: what was written, where it lives, what it
achieves going forward, and why the mechanism works.

**Action:** Output the following.

> Signal section appended to `CLAUDE.md`. Claude Code loads this file automatically
> at the start of every session in this workspace — before your first message, every
> time. The inertia question is now a standing feature of your workspace context at
> the planning stage. It will be there before you open the first file, without any
> manual step on your part.

---

## GATE 6: Copilot Extension Phase

**Phase context:** The primary Signal configuration is complete. This gate handles an
optional extension: adding a Signal section to `.github/copilot-instructions.md`,
which GitHub Copilot reads during implementation. CLAUDE.md governs the planning phase;
copilot-instructions.md governs the implementation phase. They are distinct phases
with distinct tool contexts, so their configurations carry distinct consequence anchors.

**Action:** Check whether `.github/copilot-instructions.md` exists and already contains
a Signal section.

If a Signal section is already present: output inline —
"Copilot instructions already contain a Signal section. The inertia check is present
during Copilot suggestions at the implementation phase — when you are writing function
bodies and endpoint signatures and the interface is beginning to lock. No update
needed." (No sub-gate needed — this is a detection skip path in an optional-extension
gate; no confirmation is required for an existing configuration.)

Otherwise, output the following prompt and await input.

> `CLAUDE.md` now carries the inertia check at the planning phase. Optionally, you
> can extend Signal coverage to the implementation phase by adding a Signal section
> to `.github/copilot-instructions.md`. Copilot reads this file when generating
> suggestions, which means the inertia check would be present when you are writing
> function signatures and endpoint bodies — before those interfaces lock.
>
> Add Signal section to `.github/copilot-instructions.md`?

**Routing:**
- User confirms → GATE 6A
- User declines → GATE 6-Decline

### GATE 6A: Copilot Write Phase

**Phase context:** The user has confirmed the optional Copilot extension. Write the
Signal section to `.github/copilot-instructions.md`. Report the outcome and name the
implementation-phase consequence using vocabulary native to the implementation phase —
non-overlapping with the planning-phase language in GATE 5.

**Action:** Append the Signal section to `.github/copilot-instructions.md`. Create the
file and `.github/` directory if they do not exist. Output:

> Signal section written to `.github/copilot-instructions.md`. Copilot will now carry
> the inertia check into implementation suggestions — before function bodies are written
> and endpoint interfaces are committed in code. The planning phase is covered by
> CLAUDE.md; the implementation phase is now covered here.

### GATE 6-Decline

**Phase context:** The user has declined the Copilot extension. The consequence must be
anchored to the implementation phase specifically, using phase-native vocabulary that
does not overlap with the planning-phase framing at GATE 3A. These gates protect
distinct tools at distinct development phases; their consequence arguments must be
visibly distinct.

**Action:** Output the following, then end the skill.

> Copilot instructions not updated. At the implementation phase — when Copilot is
> generating function bodies and endpoint signatures — there will be no standing inertia
> check present. `CLAUDE.md` covers the planning stage; the gap is specifically at the
> moment of writing code, before interfaces are committed. That is a different phase
> from spec authoring: direction is being encoded into function signatures, not into
> documents, and the inertia question takes a different form there.
```

---

## V-04: Conversational Register + Adversary Framing (Combined)

**Axes:** Phrasing register (conversational) + Inertia framing (named adversary)
**Hypothesis:** Conversational language with adversary framing produces higher reader resonance for C-13/C-16/C-17 — the preamble reads as a side you are choosing, not a tool you are configuring. Structural requirements (C-27/C-29) must be explicitly compensated through rigorous heading discipline and explicit routing blocks, since conversational prose naturally softens gate boundaries.

---

```markdown
# Signal Setup

## Before We Begin: What You're Actually Doing Here

Here is the honest version of what Signal setup does.

Every workspace you work in has a silent competitor. It is not a bad idea, a skeptical
colleague, or a budget constraint. It is inertia: the condition where teams, given a
perfectly reasonable new capability, simply do nothing. They do not argue against it.
They do not reject it. They just do not act — and their not-acting is enough for the
feature to fail quietly.

Signal's job is to make sure you ask "why would a team do nothing?" before you commit
to building the thing. That question, asked early enough, either surfaces a real adoption
problem you can solve or confirms the feature is genuinely worth building. Either outcome
beats building without asking.

But asking requires remembering. And remembering is what breaks down first under
pressure. So Signal setup does something simple: it writes a reminder into CLAUDE.md,
the file that Claude Code reads at the start of every session. You set it up once, and
the question is there every time — not because you remembered, but because the
configuration remembered for you.

You are not installing a plugin. You are appointing a standing opponent to inertia
in your workspace, and making sure that opponent shows up automatically.

---

## GATE 1: What Is the Current State of This Workspace?

Before doing anything, I need to know what we are working with.

I will read `CLAUDE.md` in the workspace root and check whether it already has a
Signal section.

**Routing:**
- No `CLAUDE.md` found → GATE 1B
- `CLAUDE.md` found, Signal section already present → GATE 1A
- `CLAUDE.md` found, no Signal section yet → GATE 2

### GATE 1A: You Are Already Configured

Good news — Signal is already set up here.

> Your CLAUDE.md already has a Signal section. That means every Claude Code session
> in this workspace starts with the inertia question already in context — loaded
> automatically, before you type anything. You do not have to prompt for it. You do
> not have to remember to think about adoption. It is already there because CLAUDE.md
> loads automatically at session start, every time. Inertia already has a named
> opponent in this workspace. Nothing to do here.

### GATE 1B: No CLAUDE.md Found

There is no CLAUDE.md here yet.

CLAUDE.md is what Claude Code reads at the start of each session. Without it, there
is nowhere for the inertia reminder to live — it cannot persist from session to session
without a file to ride in.

> I can create a `CLAUDE.md` for you with the Signal section as its initial content.
> You can add other workspace instructions to it later — it is just a markdown file.
> Or, if you would rather not, we can stop here.
>
> What would you like to do?
> - **Create `CLAUDE.md`** and continue setup
> - **Abort**

**Routing:**
- User wants to create → GATE 2 (I will create the file rather than append to it)
- User wants to abort → GATE 1B-Abort

#### GATE 1B-Abort

> No changes made.
>
> Here is what that means: there is no file in this workspace that loads at session
> start with an inertia check in it. The next time you sit down to draft a spec here —
> at the planning stage, before direction gets committed — there will be no standing
> question to ask "why would a team do nothing?" Inertia will be present, operating
> quietly. Signal will not.

---

## GATE 2: Here Is Exactly What I Will Write

Before touching anything, let me show you exactly what will go into `CLAUDE.md`.

> Here is the Signal section I am about to append:
>
> [fenced code block — exact Signal section content]

This is the complete section. Nothing else in your CLAUDE.md will be touched.

The Signal section contains a brief description of what Signal does, a list of the
nine namespaces (scout, draft, review, flow, trace, prove, listen, program, topic),
the inertia rule ("When enough signals exist, the topic tells you you're ready"),
and a note that `/topic:` is where the narrative comes together across all namespaces.

---

## GATE 3: Your Call

Does this look right? Should I go ahead and write it?

> Append this to `CLAUDE.md`?

**Routing:**
- User says yes → GATE 4
- User says no → GATE 3A

### GATE 3A: Not Writing It

> Understood. Nothing written. Your `CLAUDE.md` is untouched.
>
> Just so you know what you are leaving on the table: at the planning stage — the
> moment before a spec gets drafted and a direction gets chosen — there will be no
> automatic prompt to ask whether teams would actually adopt this. That question tends
> to get skipped under schedule pressure. It is exactly the kind of question inertia
> benefits from most when it goes unasked. If you want Signal to ask it for you, run
> this setup again when you are ready.

---

## GATE 4: Writing Now

Appending the Signal section to `CLAUDE.md` exactly as shown in the preview.

(If we are creating a new file: creating `CLAUDE.md` with the Signal section as its
initial content.)

---

## GATE 5: Done

> Written. The Signal section is now in `CLAUDE.md`. Claude Code loads that file
> automatically at the start of every session here, so the inertia question is already
> present before you open a single file. You have given inertia a standing opponent in
> this workspace. It will be there every time.

---

## GATE 6: One More Thing — GitHub Copilot

What you just set up covers the planning phase: when you are working in Claude Code,
drafting specs, making feature decisions. There is also an implementation phase, and if
you use GitHub Copilot, there is a way to extend Signal coverage there too.

First, let me check whether `.github/copilot-instructions.md` already has a Signal
section.

If it already does: output inline — "Your Copilot instructions are already configured
with Signal. When Copilot is generating suggestions during implementation — as you are
writing function bodies and endpoint signatures — the inertia check is already visible
there. The implementation phase is covered." (No sub-gate needed — already-configured
is a detection skip path here, not a confirmation checkpoint.) Done.

Otherwise:

> Want to also add a Signal section to `.github/copilot-instructions.md`?
>
> CLAUDE.md covers the planning stage — spec authoring, feature decisions. This would
> extend inertia coverage to the implementation phase, the moment you are actually
> writing code and function signatures are beginning to lock in.

**Routing:**
- User says yes → GATE 6A
- User says no → GATE 6-Decline

### GATE 6A: Adding Copilot Coverage

Appending a Signal section to `.github/copilot-instructions.md`. Creating the file
and `.github/` directory if needed.

> Done. Copilot instructions updated. Signal now covers both phases: planning
> (CLAUDE.md) and implementation (copilot-instructions.md). When Copilot suggests
> function signatures or endpoint patterns, the inertia check is part of its context —
> before the interface commits.

### GATE 6-Decline

> No problem. Copilot instructions left unchanged.
>
> Just note: the implementation phase — when you are writing functions and Copilot is
> making suggestions — will not have an inertia check. That is a different moment from
> spec authoring: the interface is being committed in code, not in a document. CLAUDE.md
> covers the planning stage. This gap is at the point of writing.
```

---

## V-05: Table-Driven Gate Index + Lifecycle Emphasis (Combined)

**Axes:** Output format (gate index table before prose) + Lifecycle emphasis (verbose gate bodies)
**Hypothesis:** A gate index table at the top makes the full phase structure machine-readable before any prose is parsed — C-11, C-25, C-29 compliance visible in one scan. Verbose gate bodies deliver C-22/C-23. Combined, this achieves the highest structural transparency but at the greatest total length.

---

```markdown
# Signal Setup

## Why Configure Signal

Inertia is the condition where teams do nothing — not because they disagree, but because
nothing compels them to act. Features built without first asking "why would a team do
nothing?" risk adoption failure that could have been anticipated and solved. Signal setup
writes a standing challenge to inertia into `CLAUDE.md` — the file Claude Code loads
automatically at the start of every workspace session. Once written, the inertia question
is present at the planning stage every time, without requiring manual effort. Setup is a
one-time act; the configuration is permanent. You are choosing to make inertia's opponent
a standing feature of your workspace.

---

## Gate Index

| Gate | Phase | Entry Condition | Routes To |
|------|-------|-----------------|-----------|
| GATE 1 | File Detection | Entry point | GATE 1A (Signal present), GATE 1B (CLAUDE.md absent), GATE 2 (CLAUDE.md exists, unconfigured) |
| GATE 1A | Already Configured | CLAUDE.md exists + Signal section found | End |
| GATE 1B | Missing CLAUDE.md | CLAUDE.md absent | GATE 1B-Abort (user aborts), GATE 2 (user creates) |
| GATE 1B-Abort | Abort — no file | User declines CLAUDE.md creation | End |
| GATE 2 | Preview | CLAUDE.md confirmed present or creatable | GATE 3 |
| GATE 3 | Confirmation | Preview shown | GATE 3A (decline), GATE 4 (confirm) |
| GATE 3A | Write Declined | User declines at confirmation | End |
| GATE 4 | Write | Confirmation received | GATE 5 |
| GATE 5 | Outcome Report | Write complete | GATE 6 |
| GATE 6 | Copilot Extension Offer | Primary setup complete | GATE 6A (confirm), GATE 6-Decline (decline) |
| GATE 6A | Copilot Write | User confirms Copilot update | End |
| GATE 6-Decline | Copilot Declined | User declines Copilot update | End |

---

## GATE 1: File Detection

**Purpose of this phase:** Establish the state of the workspace before any output is
generated. The two critical facts are: whether `CLAUDE.md` exists, and whether it
already contains a Signal section. Everything downstream depends on these two facts.
No output is produced at this gate other than routing to the appropriate next gate.

**Action:** Read `CLAUDE.md` from the workspace root. Search for a Signal section
(any heading that identifies Signal configuration — `# Signal`, `## Signal`, or
equivalent).

**Routing:**
- `CLAUDE.md` absent → GATE 1B
- `CLAUDE.md` present, Signal section found → GATE 1A
- `CLAUDE.md` present, Signal section absent → GATE 2

### GATE 1A: Signal Section Already Present

**Purpose of this gate:** Handle the already-configured path for the primary Signal
configuration flow. The workspace is fully configured; no write is required. This gate
must affirm what the configuration achieves, name the mechanism that makes it persist,
and close without prompting for further action.

**Action:** Output the following response, then end the skill.

> Signal is already configured in this workspace.
>
> `CLAUDE.md` is loaded automatically by Claude Code at the start of every session —
> before your first message, every time you open this workspace. That is the mechanism:
> not a prompt you must remember, not a command you must run, but a file that loads
> unconditionally. The Signal section in that file means the inertia question is already
> a standing feature of your workspace context. Inertia has a permanent opponent here.
> No changes needed.

### GATE 1B: CLAUDE.md Absent

**Purpose of this gate:** Handle the missing-file path for the primary Signal
configuration flow. `CLAUDE.md` is the vehicle for Signal's persistent reminder;
without it, setup cannot produce a durable configuration. This gate must explain the
dependency, present both options explicitly, and await a response. It is a decision
gate with two branches, each with explicit handling below.

**Action:** Output the following prompt. Await user input.

> `CLAUDE.md` was not found in this workspace root.
>
> Signal writes its inertia reminder into `CLAUDE.md`, which Claude Code loads
> automatically at session start. Without this file, there is no persistent home for
> the reminder — it cannot travel from session to session without a file that Claude
> Code is guaranteed to read.
>
> Signal can create `CLAUDE.md` now, with the Signal section as its initial content.
> You can add other workspace instructions to it later.
>
> Options:
> - **Create `CLAUDE.md`** — proceed with setup, file will be created
> - **Abort** — stop here, workspace remains unconfigured

**Routing:**
- User selects Create → GATE 2 (file creation mode)
- User selects Abort → GATE 1B-Abort

#### GATE 1B-Abort

**Purpose of this gate:** Handle the abort path after the user declines to create
`CLAUDE.md`. This is a Signal-absent exit from the primary flow at the planning-phase
tool (Claude Code). The consequence must be anchored to the planning stage as an
explicit phase label and name a specific future moment.

**Action:** Output the following, then end the skill.

> Setup aborted. `CLAUDE.md` was not created.
>
> At the planning stage — when you next open this workspace to draft a spec or make a
> feature decision — there will be no automatic instruction in your context to ask
> "why would a team do nothing?" before direction is committed. That question, unasked
> at the planning stage, is where inertia operates most effectively. The workspace
> remains unguarded at that phase until Signal is configured.

---

## GATE 2: Preview

**Purpose of this phase:** Generate and display the exact Signal section content that
will be written. This gate serves the contract function: the user sees precisely what
will appear in `CLAUDE.md`, and GATE 4 will write exactly this content — no additions,
no reformatting, no drift between what was shown and what was written.

**Action:** Generate the Signal section. Display it in a fenced code block within the
following response:

> Here is the Signal section that will be appended to `CLAUDE.md`. Review it before
> confirming.
>
> [fenced code block — exact Signal section]
>
> This is the complete change. No other content in `CLAUDE.md` will be modified.

**Signal section must include:**
- `# Signal` heading
- One-sentence description: Signal is a developer tool for feature decision-making
- Namespace list: scout, draft, review, flow, trace, prove, listen, program, topic
- Inertia rule: "When enough signals exist, the topic tells you you're ready"
- `/topic:` reference as the narrative coordinator across namespaces

---

## GATE 3: Confirmation

**Purpose of this phase:** Obtain explicit user confirmation before any file is
modified. The preview phase established what will be written. This phase establishes
that the user has consented to it. The two phases are deliberately separate — no write
occurs as a side effect of the preview.

**Action:** Output the following. Await user input.

> Append this Signal section to `CLAUDE.md`?

**Routing:**
- User confirms → GATE 4
- User declines → GATE 3A

### GATE 3A: Write Declined

**Purpose of this gate:** Handle the decline path after the user has reviewed the
preview. This is a Signal-absent exit from the primary happy path at the planning-phase
tool (Claude Code). The consequence must be anchored to the planning stage with a
specific future moment — using phase-native vocabulary distinct from GATE 1B-Abort,
which addressed a user who had not yet seen the preview.

**Action:** Output the following, then end the skill.

> Signal section not written. `CLAUDE.md` is unchanged.
>
> At the planning stage — the next time you draft a spec or make a feature direction
> decision in this workspace — there will be no standing inertia check in your context.
> That check would have been automatically present at the start of every session.
> Without it, the question "why would a team do nothing?" will not be asked unless you
> remember to ask it yourself. Run Signal setup again when you are ready to configure it.

---

## GATE 4: Write

**Purpose of this phase:** Execute the write. The content written must be byte-identical
to the content previewed in GATE 2. No additions, no omissions, no reformatting. The
preview was the contract; this gate honors it exactly.

**Action:**
- **If appending** (CLAUDE.md existed): append the previewed Signal section to the
  end of `CLAUDE.md`.
- **If creating** (path from GATE 1B create branch): create `CLAUDE.md`, write the
  Signal section as its sole content.

---

## GATE 5: Outcome Report

**Purpose of this phase:** Confirm the write outcome and report what the configuration
now achieves, naming the mechanism that produces persistence and the phase it covers.

**Action:** Output the following.

> Signal section written to `CLAUDE.md`. Claude Code loads this file automatically at
> the start of every session in this workspace — before your first message, every time.
> The inertia question is now a standing feature of your planning-stage context. You
> have given inertia a permanent opponent here.

---

## GATE 6: Copilot Extension Offer

**Purpose of this phase:** Offer to extend Signal coverage to the implementation phase
via `.github/copilot-instructions.md`. This is an optional extension distinct from the
primary Signal configuration. `CLAUDE.md` and `copilot-instructions.md` serve different
tools at different development phases: `CLAUDE.md` covers the planning phase (Claude
Code sessions, spec authoring, feature decisions); `copilot-instructions.md` covers the
implementation phase (Copilot suggestions, function body generation, endpoint signature
commitment).

**Action:** Check whether `.github/copilot-instructions.md` exists and already contains
a Signal section.

If an existing Signal section is found: output inline —
"Copilot instructions already contain a Signal section. The inertia check is present
during Copilot suggestions at the implementation phase — when you are writing function
bodies and endpoint signatures and the interface is beginning to lock. No update
needed." (No sub-gate needed — this is a detection skip path in an optional-extension
gate, not a confirmation checkpoint requiring its own gate structure.)

Otherwise, output:

> `CLAUDE.md` now covers the planning phase. Signal can also be extended to the
> implementation phase via `.github/copilot-instructions.md`, which Copilot reads when
> generating suggestions. With this addition, the inertia check would be present when
> you are writing function bodies and endpoint signatures — before those interfaces are
> committed in code.
>
> Add Signal section to `.github/copilot-instructions.md`?

**Routing:**
- User confirms → GATE 6A
- User declines → GATE 6-Decline

### GATE 6A: Copilot Write

**Purpose of this gate:** Execute the optional write to `.github/copilot-instructions.md`.
Report the implementation-phase consequence using vocabulary native to the implementation
phase — non-overlapping with the planning-phase language used in GATE 5.

**Action:** Append Signal section to `.github/copilot-instructions.md`. Create the file
and `.github/` directory if absent. Output:

> Signal section written to `.github/copilot-instructions.md`. Copilot will now surface
> the inertia check during implementation suggestions — at the phase when function
> signatures are being written and endpoint patterns are being committed in code.
> Planning is covered by `CLAUDE.md`; implementation is covered here.

### GATE 6-Decline

**Purpose of this gate:** Handle the decline path for the optional Copilot extension.
The consequence must be anchored to the implementation phase with phase-native vocabulary
that is non-overlapping with the planning-phase language at GATE 3A. These are distinct
phases; their consequence anchors must be visibly distinct.

**Action:** Output the following, then end the skill.

> Copilot instructions not updated. At the implementation phase — when you are writing
> function bodies and endpoint signatures and Copilot is making suggestions — there will
> be no inertia check present. `CLAUDE.md` covers the planning stage; the gap is at the
> moment of writing code. These are distinct phases: planning sets direction,
> implementation commits interfaces. The inertia question takes a different form at each.
```

---

## Rubric Coverage Notes

Each variation targets the full C-01–C-30 surface. Key structural commitments shared across all five:

| Criterion | Mechanism used in all variations |
|-----------|----------------------------------|
| C-11 | Each lifecycle phase is a `##` or `###` heading — named and numbered |
| C-12 | GATE 1A (already configured) and GATE 1B (missing file) are `###` sub-gates of GATE 1 |
| C-25 | Sub-gate IDs encode parent lineage: `GATE 1A`, `GATE 1B`, `GATE 1B-Abort`, `GATE 3A`, `GATE 6A`, `GATE 6-Decline` |
| C-26 | GATE 6A (Copilot confirmation) is a first-class named `###` sub-gate |
| C-27 | All gate boundaries are `##`/`###`/`####` headings; no bold-label pseudo-gates |
| C-28 | Primary detection (GATE 1A, GATE 1B) promoted to sub-gates; secondary Copilot detection handled inline |
| C-29 | Each gate has a contiguous routing block listing (condition → destination ID) pairs |
| C-30 | All inline detection paths in optional-extension gates carry explicit `(No sub-gate needed — ...)` annotation |

**Variation-specific differentiators:**

- **V-01** distinguishes itself on C-16/C-18/C-19 through the adversary identity persisting at every exit
- **V-02** distinguishes itself on C-27/C-29 through stripped-down routing prose with no structural ambiguity
- **V-03** distinguishes itself on C-22/C-23 through verbose per-gate phase-context blocks that force non-overlapping vocabulary
- **V-04** trades some structural density for resonance; compensates by making routing blocks explicit despite conversational tone
- **V-05** is the only variation where the full gate map is readable before any gate body is parsed, making C-11/C-25 compliance verifiable from the index table alone
