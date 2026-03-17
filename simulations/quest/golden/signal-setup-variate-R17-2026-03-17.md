---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-17
rubric_version: 15
round: 17
---

# signal-setup Variations — Round 17 (v15 rubric)

**Skill**: signal-setup
**Rubric**: v15 | **Denominator**: 38 (aspirational C-09–C-38) | **Date**: 2026-03-17
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/38 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

R16 scored V-02 and V-05 as the strongest candidates under v14 (denominator 35). The
scorecard revealed three residual patterns that became v15's new criteria:

| Pattern | Source | R16 Status |
|---------|--------|------------|
| C-36: Preamble dominance-verb ("inertia wins," "collects the default") | V-02 PASS C-13 | V-01 FAIL — "governs" is regulatory, not victorious |
| C-37: Team configuration framed as explicitly choosing a side | V-02 PASS C-16 (implied) | All variations FAIL — none say "choose a side" literally in text |
| C-38: Tool-specific decline names inertia as force, not tool | V-02/V-05 PASS | V-01 FAIL — "Copilot wins the default suggestion" names tool as victor |

**Denominator: A=35 → A=38**

Key rubric distinctions for R17:
- **C-36 vs C-16**: C-16 requires inertia to be *named as adversary*; C-36 requires inertia
  to be the *grammatical subject of an active-victory clause*. "Inertia is the adversary"
  satisfies C-16; "Inertia wins the default choice" satisfies both.
- **C-37 vs C-16**: C-16 is satisfied when the reader *understands* they are choosing sides;
  C-37 requires the spec to *say so* — "teams choose a side" or equivalent agency phrase
  must be in the text.
- **C-38 vs C-33**: C-38 is a sub-case of C-33 at tool-specific gates. "Copilot wins" names
  the tool as winner (C-38 FAIL); "inertia wins through Copilot" names the force (C-38 PASS).

Single-axis choices for R17:
- **V-01**: C-36 axis — dominance-verb preamble on R16 V-05 structure; C-37 deliberately absent
- **V-02**: C-37 axis — team-agency preamble on R16 V-05 structure; C-36 deliberately absent
- **V-03**: C-38 axis — R16 V-01 base + fix only GATE 6B; preamble stays weak on C-36/C-37

Combined axes:
- **V-04**: C-36 + C-37 — both preamble fixes on R16 V-05 structure; GATE 6B retains
  "Copilot wins" to leave C-38 as the sole remaining gap
- **V-05**: Full synthesis — C-36 + C-37 in preamble + C-38 at GATE 6B + all R16 V-05
  structural passes maintained

---

## V-01 — Dominance-verb preamble, no team-agency construction (C-36 axis)

**Axis**: C-36 — preamble makes inertia the grammatical subject of an active-victory clause
**Hypothesis**: A preamble built around "Inertia wins X" and "inertia collects Y" satisfies
C-36 independently of C-37. The absence of "choose a side" language keeps C-37 cleanly
isolated and verifiable. C-38 is inherited from R16 V-05's GATE 6B framing.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** Every time a feature gets built without gathering
evidence, inertia collects the outcome — the change does not happen, the team continues
what it was already doing, and no session asked why. Signal names the force that holds
that line and writes a question into Claude's context to contest it. Setup happens once;
your CLAUDE.md loads it automatically every session, so the inertia question is present
without you having to remember it.

---

### GATE 1 — Detect CLAUDE.md

Read the workspace root for `CLAUDE.md`.

Route:
- (file missing) → GATE 1A
- (file found) → GATE 2

#### GATE 1A — CLAUDE.md Missing

> No CLAUDE.md found. Signal needs one to write the configuration.
> Create a new CLAUDE.md with the Signal section? [yes / no]

Route:
- (yes) → create minimal CLAUDE.md, proceed to GATE 3 with creation noted in GATE 5 report
- (no) → GATE 1B

#### GATE 1B — Creation Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a Signal reminder in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already Configured

> Signal section found — already configured. No write needed.
>
> Inertia already has a named opponent here. Your CLAUDE.md loads automatically every
> session — the inertia question is in Claude's context without you having to remember it.
> The configuration holds that position permanently.

Proceed to GATE 6.

---

### GATE 3 — Preview

Display the Signal section that will be appended. No write yet.

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Available namespaces**: /scout, /draft, /review, /flow, /trace, /prove, /listen,
/program, /topic

**Inertia rule**: Inertia wins the default choice. When the topic has no evidence of why
teams would change behavior, gather signals until the topic can answer: what would cause
adoption, and what would prevent it?
```

---

### GATE 4 — Confirm append

> Append the Signal section shown above to CLAUDE.md? [yes / no]

Route:
- (yes) → GATE 4A
- (no) → GATE 4B

#### GATE 4A — Confirmed

Append the section to `CLAUDE.md`. Do not overwrite existing content. Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a named competitor in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> Inertia has a named opponent in Claude's context every session.

*(If GATE 1A created CLAUDE.md: note that a new CLAUDE.md was created and the Signal
section was appended to it.)*

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This extends Signal awareness to GitHub Copilot during implementation. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot Write Path

Step 1 — file detection: Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate for file-existence — file creation is included in the confirmed write action
when the file is missing; no separate confirmation point is required.)*

Step 2 — content detection: If the file exists, scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 6A-Found
- (Signal section absent or file missing) → GATE 6A-Write

#### GATE 6A-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6A-Write — Copilot Write

Append (or create) the Copilot Signal section:

```markdown
## Signal

Signal is active in this workspace. When suggesting implementation code, apply the
inertia rule: if the feature assumes adoption without evidence, surface the question
before the suggestion is accepted.

**Inertia rule**: Inertia wins the default choice. Ask: what would cause adoption, and
what would prevent it?
```

> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present before
> the build direction is locked in.

Exit.

#### GATE 6B — Copilot Declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the build suggestion through Copilot: code that
assumes adoption gets generated without the inertia question in context, and adoption
assumptions get locked into the implementation before anyone asks whether they are
warranted.

---

## V-02 — Team-agency preamble, no dominance-verb construction (C-37 axis)

**Axis**: C-37 — preamble explicitly names team configuration as choosing a side
**Hypothesis**: "Choosing a side" language satisfies C-37 independently of C-36. A preamble
that names inertia as adversary and frames configuration as an act of choice — but without
making inertia the grammatical subject of an active-victory clause — passes C-37 while
leaving C-36 cleanly absent for measurement. C-38 is maintained from R16 V-05.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

Inertia is the adversary every feature faces — the silent competitor that benefits when
teams commit to a direction without asking why users would change their behavior. When you
configure Signal, you are not just enabling a tool. **You are choosing a side.** Teams
that configure Signal appoint inertia as a named opponent in Claude's context; teams that
skip setup leave the field to inertia by default. The reminder lives in CLAUDE.md and
loads automatically every session, so the choice holds without anyone having to repeat it.

---

### GATE 1 — Detect CLAUDE.md

Read the workspace root for `CLAUDE.md`.

Route:
- (file missing) → GATE 1A
- (file found) → GATE 2

#### GATE 1A — CLAUDE.md Missing

> No CLAUDE.md found. Signal needs one to write the configuration.
> Create a new CLAUDE.md with the Signal section? [yes / no]

Route:
- (yes) → create minimal CLAUDE.md, proceed to GATE 3 with creation noted in GATE 5 report
- (no) → GATE 1B

#### GATE 1B — Creation Declined

> No changes made.

At the planning stage, inertia wins the default choice: the spec gets committed without
a Signal reminder in Claude's context, and the question of why teams would do nothing
never gets asked before the feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already Configured

> Signal section found — already configured. No write needed.
>
> You chose a side — inertia already has a named opponent here. Your CLAUDE.md loads
> automatically every session, so the inertia question is in Claude's context without
> you having to remember it. The choice you made in setup holds permanently.

Proceed to GATE 6.

---

### GATE 3 — Preview

Display the Signal section that will be appended. No write yet.

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Available namespaces**: /scout, /draft, /review, /flow, /trace, /prove, /listen,
/program, /topic

**Inertia rule**: Inertia wins the default choice. When the topic has no evidence of why
teams would change behavior, gather signals until the topic can answer: what would cause
adoption, and what would prevent it?
```

---

### GATE 4 — Confirm append

> Append the Signal section shown above to CLAUDE.md? [yes / no]

Route:
- (yes) → GATE 4A
- (no) → GATE 4B

#### GATE 4A — Confirmed

Append the section to `CLAUDE.md`. Do not overwrite existing content. Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

At the planning stage, inertia wins the default choice: the spec gets committed without
a named competitor in Claude's context, and the question of why teams would do nothing
never gets asked before the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> Inertia has a named opponent in Claude's context every session.

*(If GATE 1A created CLAUDE.md: note that a new CLAUDE.md was created and the Signal
section was appended to it.)*

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This extends Signal awareness to GitHub Copilot during implementation. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot Write Path

Step 1 — file detection: Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate for file-existence — file creation is included in the confirmed write action
when the file is missing; no separate confirmation point is required.)*

Step 2 — content detection: If the file exists, scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 6A-Found
- (Signal section absent or file missing) → GATE 6A-Write

#### GATE 6A-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6A-Write — Copilot Write

Append (or create) the Copilot Signal section:

```markdown
## Signal

Signal is active in this workspace. When suggesting implementation code, apply the
inertia rule: if the feature assumes adoption without evidence, surface the question
before the suggestion is accepted.

**Inertia rule**: Inertia wins the default choice. Ask: what would cause adoption, and
what would prevent it?
```

> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present before
> the build direction is locked in.

Exit.

#### GATE 6B — Copilot Declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the build suggestion through Copilot: code that
assumes adoption gets generated without the inertia question in context, and adoption
assumptions get locked into the implementation before anyone asks whether they are
warranted.

---

## V-03 — Tool-specific force naming at GATE 6B only (C-38 axis)

**Axis**: C-38 — at tool-specific decline gates, the winning party is a behavioral force,
not a tool name
**Hypothesis**: Replacing "Copilot wins" with "inertia wins through Copilot" at GATE 6B
satisfies C-38 as a single-point change to an otherwise R16 V-01-quality spec. The
preamble intentionally stays weak on C-36/C-37 to isolate the gate fix as the sole axis.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

Signal helps teams gather evidence across 9 namespaces before committing to a feature. The
inertia rule governs when a topic is ready. Configuring Signal adds the rule and skill
advertising to Claude's context so it is present in every session without anyone having to
remember it.

---

### GATE 1 — Detect CLAUDE.md

Read the workspace root for `CLAUDE.md`.

Route:
- (file missing) → GATE 1A
- (file found) → GATE 2

#### GATE 1A — CLAUDE.md Missing

`CLAUDE.md` was not found in the workspace root.

Signal requires a CLAUDE.md to append to. Offer to create one:

> No CLAUDE.md found. Signal needs one to write the configuration.
> Create a new CLAUDE.md with the Signal section? [yes / no]

Route:
- (yes) → create minimal CLAUDE.md, proceed to GATE 3 with the creation noted
- (no) → print decline message, exit

**GATE 1A Decline:**
Inertia wins the planning stage: every session starts without a Signal reminder, so the
question of why teams would do nothing never enters Claude's context before the next
feature commitment.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Search for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already configured

`CLAUDE.md` already contains a `## Signal` section.

> Signal section found — already configured. No write needed.
> Your CLAUDE.md loads automatically every session, so the inertia question is present
> in Claude's context without you having to remember it. The configuration does that work
> persistently, once written.

Proceed to GATE 6 to offer optional Copilot extension.

---

### GATE 3 — Preview

Render the Signal section that will be appended. Display to user before any write:

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Available namespaces**: /scout, /draft, /review, /flow, /trace, /prove, /listen,
/program, /topic

**Inertia rule**: When the topic has no evidence of why teams would change behavior,
inertia wins the default. Gather signals until the topic can answer: what would cause
adoption, and what would prevent it?
```

---

### GATE 4 — Confirm append

> Append the Signal section shown above to CLAUDE.md? [yes / no]

Route:
- (yes) → GATE 4A
- (no) → GATE 4B

#### GATE 4A — Confirmed

Append the section to `CLAUDE.md`. Do not overwrite existing content.

Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a named competitor in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> The inertia rule is now in Claude's context every session.

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This adds Signal awareness to GitHub Copilot interactions. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot write path

Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate needed for file-existence detection — if file is missing, creation is
included in the confirmed action; no separate confirmation point is required.)*

If file exists, scan for `## Signal` heading.

Route:
- (Signal section already present) → print Copilot already-configured message, exit
- (Signal section absent or file missing) → append or create, print result, exit

**Copilot already-configured message:**
> Copilot instructions already contain a Signal section. During implementation, Copilot
> has the inertia question in context when it suggests code — no change needed.

**Copilot write result:**
> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present —
> before the build direction is locked in.

#### GATE 6B — Copilot declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the build suggestion through Copilot: code that
assumes adoption gets generated without the inertia question in context, and adoption
assumptions get locked into the implementation before anyone asks whether they are
warranted.

---

## V-04 — Dominance-verb + team-agency preamble; tool-name gate left intact (C-36 + C-37 axis)

**Axis**: C-36 + C-37 — both preamble constructions present simultaneously
**Hypothesis**: A preamble that combines "Inertia wins X" (dominance-verb, C-36) with
"teams choose a side" (explicit agency, C-37) satisfies both criteria on a solid structural
foundation. GATE 6B deliberately retains "Copilot wins" to confirm that C-38 is the sole
remaining gap — the preamble axes and the gate axis are independent failure modes.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** Every session without Signal configured is a session
where Claude has no reminder to challenge adoption assumptions — the feature gets committed,
and inertia collects the default because no one named it as a competitor. Teams that
configure Signal choose a side: they appoint inertia as a named opponent in every session
that follows. Setup writes the reminder once; your CLAUDE.md loads it automatically, so
the choice holds without you having to repeat it.

---

### GATE 1 — Detect CLAUDE.md

Read the workspace root for `CLAUDE.md`.

Route:
- (file missing) → GATE 1A
- (file found) → GATE 2

#### GATE 1A — CLAUDE.md Missing

> No CLAUDE.md found. Signal needs one to write the configuration.
> Create a new CLAUDE.md with the Signal section? [yes / no]

Route:
- (yes) → create minimal CLAUDE.md, proceed to GATE 3 with creation noted in GATE 5 report
- (no) → GATE 1B

#### GATE 1B — Creation Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a Signal reminder in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already Configured

> Signal section found — already configured. No write needed.
>
> You chose a side — inertia already has a named opponent here. Your CLAUDE.md loads
> automatically every session, so the inertia question is in Claude's context without you
> having to remember it. The configuration holds that position permanently.

Proceed to GATE 6.

---

### GATE 3 — Preview

Display the Signal section that will be appended. No write yet.

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Available namespaces**: /scout, /draft, /review, /flow, /trace, /prove, /listen,
/program, /topic

**Inertia rule**: Inertia wins the default choice. Gather signals until the topic can
answer: what would cause adoption, and what would prevent it?
```

---

### GATE 4 — Confirm append

> Append the Signal section shown above to CLAUDE.md? [yes / no]

Route:
- (yes) → GATE 4A
- (no) → GATE 4B

#### GATE 4A — Confirmed

Append the section to `CLAUDE.md`. Do not overwrite existing content. Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a named competitor in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> Inertia has a named opponent in Claude's context every session.

*(If GATE 1A created CLAUDE.md: note that a new CLAUDE.md was created and the Signal
section was appended to it.)*

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This extends Signal awareness to GitHub Copilot during implementation. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot Write Path

Step 1 — file detection: Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate for file-existence — file creation is included in the confirmed write action
when the file is missing; no separate confirmation point is required.)*

Step 2 — content detection: If the file exists, scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 6A-Found
- (Signal section absent or file missing) → GATE 6A-Write

#### GATE 6A-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6A-Write — Copilot Write

Append (or create) the Copilot Signal section:

```markdown
## Signal

Signal is active in this workspace. When suggesting implementation code, apply the
inertia rule: if the feature assumes adoption without evidence, surface the question
before the suggestion is accepted.

**Inertia rule**: Inertia wins the default choice. Ask: what would cause adoption, and
what would prevent it?
```

> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present before
> the build direction is locked in.

Exit.

#### GATE 6B — Copilot Declined

> Copilot instructions not updated.

At the implementation stage, Copilot wins the build suggestion: code that assumes adoption
gets written without the inertia question in context, and adoption assumptions get locked
into the implementation before anyone asks whether they are warranted.

*(Note: This gate deliberately uses "Copilot wins" to isolate C-38 as the remaining gap.
V-05 replaces this with the force-naming construction.)*

---

## V-05 — Full synthesis (C-36 + C-37 + C-38)

**Axes**: All three new v15 criteria on top of R16 V-05 structural foundation
**Hypothesis**: A spec that opens with "Inertia wins" (C-36) + "teams choose a side"
(C-37), maintains heading-level gates, Route: blocks, letter-slot identifiers, and content
detection from R16 V-05, and names inertia (not Copilot) as the winning force at GATE 6B
(C-38) achieves a clean pass on all 38 criteria.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder
to surface the adoption question — feature specs get committed without a challenge, and
inertia collects the default because no session named it as a competitor. Teams that
configure Signal choose a side: they write inertia a named opponent into every session,
permanently. Setup happens once; your CLAUDE.md loads it automatically, so the choice
holds without you having to repeat it.

---

### GATE 1 — Detect CLAUDE.md

Read the workspace root for `CLAUDE.md`.

Route:
- (file missing) → GATE 1A
- (file found) → GATE 2

#### GATE 1A — CLAUDE.md Missing

> No CLAUDE.md found. Signal needs one to write the configuration.
> Create a new CLAUDE.md with the Signal section? [yes / no]

Route:
- (yes) → create minimal CLAUDE.md, proceed to GATE 3 with creation noted in GATE 5 report
- (no) → GATE 1B

#### GATE 1B — Creation Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a Signal reminder in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already Configured

> Signal section found — already configured. No write needed.
>
> You chose a side — inertia already has a named opponent here. Your CLAUDE.md loads
> automatically every session, so the inertia question is in Claude's context without you
> having to remember it. The configuration holds that position permanently.

Proceed to GATE 6.

---

### GATE 3 — Preview

Display the Signal section that will be appended. No write yet.

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Available namespaces**: /scout, /draft, /review, /flow, /trace, /prove, /listen,
/program, /topic

**Inertia rule**: Inertia wins the default choice. When the topic has no evidence of why
teams would change behavior, gather signals until the topic can answer: what would cause
adoption, and what would prevent it?
```

---

### GATE 4 — Confirm append

> Append the Signal section shown above to CLAUDE.md? [yes / no]

Route:
- (yes) → GATE 4A
- (no) → GATE 4B

#### GATE 4A — Confirmed

Append the section to `CLAUDE.md`. Do not overwrite existing content. Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a named competitor in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> Inertia has a named opponent in Claude's context every session.

*(If GATE 1A created CLAUDE.md: note that a new CLAUDE.md was created and the Signal
section was appended to it.)*

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This extends Signal awareness to GitHub Copilot during implementation. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot Write Path

Step 1 — file detection: Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate for file-existence — file creation is included in the confirmed write action
when the file is missing; no separate confirmation point is required.)*

Step 2 — content detection: If the file exists, scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 6A-Found
- (Signal section absent or file missing) → GATE 6A-Write

#### GATE 6A-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6A-Write — Copilot Write

Append (or create) the Copilot Signal section:

```markdown
## Signal

Signal is active in this workspace. When suggesting implementation code, apply the
inertia rule: if the feature assumes adoption without evidence, surface the question
before the suggestion is accepted.

**Inertia rule**: Inertia wins the default choice. Ask: what would cause adoption, and
what would prevent it?
```

> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present before
> the build direction is locked in.

Exit.

#### GATE 6B — Copilot Declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the build suggestion through Copilot: code that
assumes adoption gets generated without the inertia question in context, and adoption
assumptions get locked into the implementation before anyone asks whether they are
warranted.

---

## Axis Coverage Summary

| Variation | Primary Axis | C-36 | C-37 | C-38 | Key Structural Base |
|-----------|-------------|------|------|------|---------------------|
| V-01 | C-36 (dominance-verb preamble) | PASS | FAIL | PASS | R16 V-05 |
| V-02 | C-37 (team-agency preamble) | FAIL | PASS | PASS | R16 V-05 |
| V-03 | C-38 (force naming at GATE 6B) | FAIL | FAIL | PASS | R16 V-01 |
| V-04 | C-36 + C-37 (both preamble axes) | PASS | PASS | FAIL | R16 V-05 |
| V-05 | Full synthesis (C-36 + C-37 + C-38) | PASS | PASS | PASS | R16 V-05 |

## Synthesis Notes

**V-05 is the target golden candidate.** Key structural decisions:

1. **C-36 mechanism**: "Inertia wins the default choice" and "inertia collects the
   default" appear in the opening sentence and preamble body. Inertia is the grammatical
   subject; "wins" and "collects" are active-victory verbs. "governs" (R16 V-01 preamble)
   was regulatory and fails C-36; "wins" passes.

2. **C-37 mechanism**: "Teams that configure Signal choose a side" is present as a
   complete, explicit sentence in the preamble. This is not implied — the phrase "choose a
   side" is in the text. The GATE 2A already-configured affirmation reinforces it: "You
   chose a side."

3. **C-38 mechanism**: GATE 6B reads "inertia wins the build suggestion through Copilot."
   Inertia is the winner; Copilot is named as the channel. This matches the rubric's
   positive example: "inertia wins the implementation stage — Copilot suggests code without
   the question in context."

4. **C-36 + C-37 independence**: V-01 shows C-36 can pass without C-37 (dominance verb,
   no "choose a side"). V-02 shows C-37 can pass without C-36 (explicit agency, no
   dominance verb as the *preamble's* subject-verb construction). V-04 confirms both can
   coexist. The criteria are structurally independent.

5. **C-38 independence from preamble**: V-03 shows C-38 can be fixed by changing one gate
   body, without touching the preamble. The preamble constructions and the gate force-
   naming are independent failure modes — fixing one does not fix the other.

6. **V-04 as diagnostic**: V-04 is the planned-fail variation for C-38. Its GATE 6B
   deliberately says "Copilot wins" with an annotation. This confirms that the C-38 failure
   in R16 V-01 was a gate-body failure, not a consequence of weak preamble framing.
