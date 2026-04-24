---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-17
rubric_version: 14
round: 16
---

# signal-setup Variations — Round 16 (v14 rubric)

**Skill**: signal-setup
**Rubric**: v14 | **Denominator**: 35 (aspirational C-09–C-35) | **Date**: 2026-03-17
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/35 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

R15 scored V-01 and V-02 tied at 94.8% (27.5/29 v13). The round revealed a structural
tension: V-01 achieved C-27 (heading-level gate boundaries) but failed C-16 (adversary
framing); V-02 achieved C-16 but failed C-27 (bold-label structure only). Both failed C-24
(Copilot content detection — file-existence check only) and scored PARTIAL on C-29 (no
contiguous routing block at parent gates).

The v14 rubric formalizes five new criteria extracted from R15 excellence signals:

| Criterion | Source | Structural target for R16 |
|-----------|--------|---------------------------|
| C-31 | Uniform sub-gate identifier scheme | All sub-gates use the same convention throughout — letter-slot or word-suffix, never mixed |
| C-32 | Consequence anchors are complete assertable propositions | Every anchor resolves to S+P+O — no noun phrases, no dangling clauses |
| C-33 | Decline anchors name adversary as winning party | Inertia is the grammatical subject of the consequence; user's inaction is the mechanism |
| C-34 | Two-step causal chain in decline anchors | Immediate effect + downstream state, explicitly connected |
| C-35 | Routing blocks use `Route:` label + one-branch-per-line | Machine-parseable routing independent of prose narrative |

**Denominator: A=29 → A=35**

Single-axis choices for R16:
- **V-01**: C-35 axis — `Route:` label + one-branch-per-line (heading structure preserved from R15 V-01)
- **V-02**: C-33/C-34 axis — adversary-as-victor + two-step causal chain (heading structure preserved)
- **V-03**: C-24 axis — Copilot content detection (checks for `## Signal` in file, not just file existence)

Combined axes:
- **V-04**: C-35 + C-31 + C-24 — routing blocks + uniform identifier scheme + Copilot content detection
- **V-05**: Full synthesis — all R15 failures resolved + all new criteria satisfied

---

## V-01 — Route: label + one-branch-per-line (C-35 axis)

**Axis**: C-35 — machine-parseable routing blocks at every branching gate
**Hypothesis**: Adding `Route:` labels with one-entry-per-line to an otherwise R15 V-01
structure resolves the C-29 PARTIAL without disrupting heading-level gate boundaries.

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

Inertia wins the planning stage: every session starts without a Signal reminder, so the
question of why teams would do nothing never enters Claude's context before the next
feature commitment.

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

At the implementation stage, Copilot wins the default suggestion: code that assumes
adoption gets written without the inertia question in context, and the adoption question
never surfaces during the build.

---

## V-02 — Adversary-as-victor + two-step causal chain (C-33/C-34 axis)

**Axis**: C-33/C-34 — every decline anchor names inertia as the winning party and
expresses a two-step causal chain (immediate effect → downstream state)
**Hypothesis**: Heading-level gate structure (C-27) and adversary-as-victor framing
(C-16/C-33) can coexist — the adversary language lives in the preamble and decline
bodies, not in gate headings, so structural navigability is unaffected.

---

You are running `/signal-setup`. Configure Signal in this workspace.

**Inertia wins the default choice.** When Signal is not configured, every session starts
without a named opponent in Claude's context. Teams commit to feature directions without
being asked why users would change behavior — and because no reminder surfaces the
question, inertia collects the default. Setup writes the reminder once, permanently, so
inertia has a named opponent in every session that follows.

---

### GATE 1 — Detect CLAUDE.md

Read the workspace root for `CLAUDE.md`.

Route:
- (file missing) → GATE 1A
- (file found) → GATE 2

#### GATE 1A — CLAUDE.md Missing

No `CLAUDE.md` found in the workspace root.

> No CLAUDE.md found. Signal needs one to write the configuration.
> Create a new CLAUDE.md with the Signal section? [yes / no]

Route:
- (yes) → create minimal CLAUDE.md, proceed to GATE 3
- (no) → GATE 1A-Decline

**GATE 1A-Decline:**

> No changes made.

Inertia wins the planning stage: the spec gets committed without a Signal reminder in
context, and the question of why teams would do nothing never gets asked before the
feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Search for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already configured

> Signal section found — already configured. No write needed.
> Inertia already has a named opponent here. Your CLAUDE.md loads automatically every
> session — the inertia question is in Claude's context without you having to remember
> it. The configuration holds that position for you permanently.

Proceed to GATE 6.

---

### GATE 3 — Preview

Render the Signal section that will be appended. Display before any write:

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

Append the section to `CLAUDE.md`. Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a named competitor in
context, and the question of why teams would do nothing never gets asked before the
feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> Inertia has a named opponent in Claude's context every session.

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This extends Signal awareness into GitHub Copilot interactions. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot write path

Check whether `.github/copilot-instructions.md` exists. Scan for `## Signal` heading.

*(No sub-gate needed — file creation is included in the confirmed action when file is
missing; no separate confirmation is required.)*

Route:
- (Signal section already present) → Copilot already-configured affirmation, exit
- (Signal section absent or file missing) → write, print result, exit

**Copilot already-configured affirmation:**
> Copilot instructions already contain a Signal section. At the implementation stage,
> Copilot has the inertia question in context when it suggests code — inertia already has
> a named opponent there too.

**Copilot write result:**
> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present before
> the build direction is locked in.

#### GATE 6B — Copilot declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the build suggestion: Copilot writes code that
assumes adoption without the inertia question in context, and adoption assumptions get
locked into the implementation before anyone asks whether they are warranted.

---

## V-03 — Copilot already-configured content detection (C-24 axis)

**Axis**: C-24 — GATE 6A scans `.github/copilot-instructions.md` for an existing Signal
section (not just file existence) and affirms the tool-local consequence when found
**Hypothesis**: Splitting the Copilot path into GATE 6A (file detection) and GATE 6A-1
(content detection) with a complete already-configured affirmation resolves C-24 without
requiring C-28 to mandate sub-gate promotion for secondary optional paths.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

Teams commit feature directions without asking why users would change behavior. Signal
names the question and puts it in Claude's context. Setup happens once, but the reminder
lives in every session that follows — without anyone having to remember to ask.

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
- (yes) → create minimal CLAUDE.md, proceed to GATE 3
- (no) → print decline message, exit

**GATE 1A Decline:**
Inertia wins the planning stage: the spec gets committed without a Signal reminder in
context, and the question of why teams would do nothing never gets asked before the
feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Search for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already configured

> Signal section found — already configured. No write needed.
> Your CLAUDE.md loads automatically every session — the inertia question is in Claude's
> context without you having to remember it. The configuration holds that position
> persistently.

Proceed to GATE 6.

---

### GATE 3 — Preview

Display the Signal section that will be appended before any write:

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

Append the section to `CLAUDE.md`. Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

At the planning stage, inertia wins the default choice: the spec gets committed without a
named competitor in Claude's context, and the question of why teams would do nothing never
gets asked before the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> The inertia question is now in Claude's context every session.

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This adds Signal awareness to GitHub Copilot interactions. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot write path

Step 1: Check whether `.github/copilot-instructions.md` exists.

- If the file does not exist: note that creation will be part of the write action;
  proceed to step 2. *(No sub-gate — creation is included in the confirmed action.)*

Step 2: If the file exists, scan for `## Signal` heading.

- If `## Signal` found: print Copilot already-configured affirmation. Exit.
- If `## Signal` absent: append Signal section. Print write result. Exit.

**Copilot already-configured affirmation:**
> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — the
> adoption question surfaces during the build, not only at the planning stage. No change
> needed.

**Copilot write result:**
> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present before
> the build direction is locked in.

#### GATE 6B — Copilot declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the Copilot suggestion: code that assumes
adoption gets written without the inertia question in Copilot's context, and adoption
assumptions become locked into the build before anyone asks whether they hold.

---

## V-04 — Route: blocks + uniform identifiers + Copilot content detection (C-35 + C-31 + C-24)

**Axes**: C-35 (Route: labels), C-31 (uniform letter-slot scheme throughout), C-24
(Copilot content detection)
**Hypothesis**: Combining three structural fixes from single-axis variations with heading-
level gate boundaries and adversary-as-victor preamble (from R15 V-01/V-02 synthesis)
produces a spec that clears all three failures without introducing new regressions.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder
to ask why teams would change behavior. Feature specs get committed without a named
opponent — and inertia collects the default because no one thought to name it. Setup
writes the reminder once; your CLAUDE.md loads it automatically every session, so the
question is present without you having to remember it.

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
- (yes) → create minimal CLAUDE.md, proceed to GATE 3
- (no) → GATE 1B

#### GATE 1B — Creation Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a Signal reminder in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Search for `## Signal` heading.

Route:
- (Signal section found) → GATE 2A
- (Signal section absent) → GATE 3

#### GATE 2A — Already Configured

> Signal section found — already configured. No write needed.
> Inertia already has a named opponent here. Your CLAUDE.md loads automatically every
> session — the inertia question is in Claude's context without you having to remember
> it.

Proceed to GATE 6.

---

### GATE 3 — Preview

Display the Signal section that will be appended before any write:

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

Append the section to `CLAUDE.md`. Proceed to GATE 5.

#### GATE 4B — Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a named competitor in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> Inertia has a named opponent in Claude's context every session.

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This extends Signal awareness to GitHub Copilot during implementation. [yes / no / skip]

Route:
- (yes) → GATE 6A
- (no or skip) → GATE 6B

#### GATE 6A — Copilot Write Path

Check whether `.github/copilot-instructions.md` exists and, if it does, scan for
`## Signal` heading.

*(No sub-gate for file-existence detection — file creation is part of the confirmed write
action; no separate confirmation point is required.)*

Route:
- (file exists and Signal section found) → Copilot already-configured affirmation, exit
- (file missing or Signal section absent) → append or create, print result, exit

**Copilot already-configured affirmation:**
> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already present in Copilot's context —
> adoption assumptions surface during the build, not only at the planning stage.

**Copilot write result:**
> Signal section written to `.github/copilot-instructions.md`.
> While Copilot is suggesting implementation code, the inertia question is present before
> the build direction is locked in.

#### GATE 6B — Copilot Declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the build suggestion: Copilot writes code that
assumes adoption without the inertia question in context, and adoption assumptions get
locked into the implementation before anyone asks whether they are warranted.

---

## V-05 — Full synthesis (C-16 + C-27 + C-24 + C-29/C-35 + C-31 + C-32 + C-33 + C-34)

**Axes**: All unresolved failures from R15 plus all new criteria from v14
**Hypothesis**: A spec that opens with an adversary-as-victor preamble (C-16), uses
heading-level gates (C-27), applies uniform letter-slot sub-gate identifiers (C-31),
includes `Route:` label blocks at every branching gate (C-35), detects Copilot content
not just file existence (C-24), and writes every consequence anchor as a two-step causal
chain with inertia as the winning party (C-32/C-33/C-34) achieves a clean pass on all
35 criteria.

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder
to ask why teams would change behavior. Feature specs get committed without a named
opponent in context — and inertia collects the default because the question is never
asked. Setup writes the reminder once; your CLAUDE.md loads it automatically every
session, so inertia has a named opponent without you having to remember to name it.

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

At the implementation stage, inertia wins the build suggestion: Copilot writes code that
assumes adoption without the inertia question in context, and adoption assumptions get
locked into the implementation before anyone asks whether they are warranted.

---

## Axis Coverage Summary

| Variation | Primary Axis | Key New Criteria Targeted | Key R15 Failures Addressed |
|-----------|-------------|--------------------------|---------------------------|
| V-01 | C-35 (Route: labels) | C-35 | C-29 PARTIAL |
| V-02 | C-33/C-34 (adversary + causal chain) | C-33, C-34, C-32 | C-16 FAIL (with heading structure) |
| V-03 | C-24 (Copilot content detection) | C-24 | C-24 FAIL |
| V-04 | C-35 + C-31 + C-24 | C-35, C-31, C-24 | C-29 PARTIAL + C-24 FAIL |
| V-05 | Full synthesis | C-31, C-32, C-33, C-34, C-35 | C-16 FAIL + C-24 FAIL + C-27 note + C-29 PARTIAL |

## Synthesis Notes

**V-05 is the target golden candidate.** Key structural decisions:

1. **C-16 + C-27 coexistence**: Adversary framing lives in the preamble body text and
   decline gate bodies — not in heading labels. Heading labels remain navigational
   (`### GATE 1 — Detect CLAUDE.md`). No tension.

2. **C-31 uniformity**: V-05 uses letter-slot encoding everywhere. GATE 1A/1B, GATE 2A,
   GATE 4A/4B, GATE 6A/6B, GATE 6A-Found, GATE 6A-Write. The `-Found/-Write` word
   suffixes on GATE 6A sub-sub-gates are a secondary level; the top-level sub-gate scheme
   (letter-slot) is consistent. *(Scorer note: C-31 applies to the sub-gate identifier
   scheme — if `-Found/-Write` are treated as second-tier identifiers distinct from the
   A/B letter-slot tier, this is architecturally clean. If they are treated as the same
   tier as GATE 1A, a mixed convention exists. V-04 uses GATE 6A-Found/6A-Write to
   distinguish these as content-detection branches inside the already-promoted GATE 6A;
   this may require scorer adjudication.)*

3. **C-35 in V-05**: Every branching gate (GATE 1, 2, 4, 6) carries a `Route:` block.
   Terminal gates (1B, 2A, 4A, 4B, 5, 6A-Found, 6A-Write, 6B) have no Route block —
   they pass vacuously.

4. **C-32/C-33/C-34 chain design**: Every decline anchor in V-05 follows the form:
   - Subject: inertia (wins, collects)
   - Immediate effect: [what happens at the moment of decline — spec committed,
     code suggested]
   - Downstream state: [what question never gets asked / what assumption never gets
     surfaced]
   The chain is explicit via "and" or "; the result is" connectors.

5. **C-24 mechanism in V-05**: GATE 6A is a two-step detection sequence. Step 1 checks
   file existence. Step 2 scans file content for `## Signal`. Both the "already present"
   and "absent or missing" branches have complete consequence affirmations in Copilot-
   native vocabulary (implementation-stage, build-direction, Copilot-suggestion context).
