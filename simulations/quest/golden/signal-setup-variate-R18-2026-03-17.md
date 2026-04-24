---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-17
rubric_version: 16
round: 18
---

# signal-setup Variations — Round 18 (v16 rubric)

**Skill**: signal-setup
**Rubric**: v16 | **Denominator**: 40 (aspirational C-09–C-40) | **Date**: 2026-03-17
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/40 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

R17 scored V-02 and V-05 as the strongest candidates under v15 (denominator 38). Under v16
(denominator 40), two new criteria expose residual gaps:

| Criterion | V-01 R17 | V-02 R17 | V-05 R17 |
|-----------|----------|----------|----------|
| C-39 (refutation-then-assertion) | FAIL — opens with assertion, no prior negation | PASS — "not just enabling a tool. You are choosing a side." | FAIL — opens with assertion, no prior negation |
| C-40 (agency-choice echo at GATE 2A) | FAIL — GATE 2A uses neutral language, no choice-echo | PASS — "You chose a side" echoes preamble | PASS — "You chose a side" echoes preamble |

**Persistent gap across all R17 variations: C-31** — identifier scheme mixes letter-slot
(GATE 1A, GATE 1B, GATE 2A, GATE 4A, GATE 4B, GATE 6A, GATE 6B) with word-suffix
(GATE 6A-Found, GATE 6A-Write). C-31 requires uniform convention throughout.

**R18 target state**: A spec that simultaneously passes C-36, C-37, C-38, C-39, C-40,
and C-31. This requires threading R17 V-05's dominance-verb preamble (C-36) through the
refutation-then-assertion construction (C-39), while choosing and applying a single
identifier convention uniformly (C-31).

**Single-axis choices for R18** (3 variations):
- **V-01**: C-39 axis — refutation clause added to R17 V-05 preamble; mixed identifiers
  preserved to isolate C-39 as the sole variable
- **V-02**: C-31 axis — uniform letter-slot identifiers throughout R17 V-05; preamble
  unchanged (no refutation clause), to isolate the structural fix
- **V-03**: C-36 + C-39 coexistence test — start from R17 V-02 (which has C-37/C-38/C-39/
  C-40 but not C-36/C-31) and add dominance-verb; tests whether C-36 and C-39 can coexist
  in a preamble that was built for C-37/C-39

**Combined axes** (2 variations):
- **V-04**: C-39 + C-31 combined on R17 V-05 base — golden candidate; letter-slot
  uniformity plus refutation; all six target criteria in one spec
- **V-05**: C-39 + C-31 alternative on R17 V-05 base — same preamble as V-04, but uses
  word-suffix convention throughout instead of letter-slot; tests whether C-31 is satisfied
  by either encoding scheme, making V-04 and V-05 a C-31-mechanism pair

---

## V-01 — Refutation clause in preamble, mixed identifiers preserved (C-39 axis)

**Axis**: C-39 — refutation-then-assertion construction inserted into R17 V-05 preamble
**Hypothesis**: Inserting "You are not just enabling a plugin. You are choosing a side."
between the inertia-collection sentence and the "Teams that configure Signal" sentence
installs the C-39 form without disturbing any R17 V-05 pass. The negation and assertion
are contiguous (sentence pair), satisfying the "same logical unit" requirement. Mixed
identifiers are deliberately preserved so C-39 is the sole measured variable.
**Expected**: C-36 PASS, C-37 PASS, C-38 PASS, C-39 PASS, C-40 PASS, C-31 FAIL

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder
to surface the adoption question — feature specs get committed without a challenge, and
inertia collects the default because no session named it as a competitor. You are not just
enabling a plugin. **You are choosing a side.** Teams that configure Signal write inertia a
named opponent into every session, permanently. Setup happens once; your CLAUDE.md loads it
automatically, so the choice holds without you having to repeat it.

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

## V-02 — Uniform letter-slot identifiers throughout, no refutation clause (C-31 axis)

**Axis**: C-31 — identifier scheme made fully uniform (letter-slot throughout) on R17 V-05
**Hypothesis**: Renaming GATE 6A-Found → GATE 6AA and GATE 6A-Write → GATE 6AB eliminates
the only mixed-convention pair in the spec, satisfying C-31's uniformity requirement. The
preamble is unchanged from R17 V-05 (no refutation clause), keeping C-39 as the sole
remaining gap. GATE 2A's "You chose a side" echo preserves C-40. This is the structural
control variation: it confirms C-31 can be fixed without touching preamble framing.
**Expected**: C-36 PASS, C-37 PASS, C-38 PASS, C-39 FAIL, C-40 PASS, C-31 PASS

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
- (Signal section found) → GATE 6AA
- (Signal section absent or file missing) → GATE 6AB

#### GATE 6AA — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6AB — Copilot Write

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

## V-03 — Dominance-verb and refutation-then-assertion coexistence (C-36 + C-39 axis)

**Axis**: C-36 + C-39 — tests whether the dominance-verb construction and the
refutation-then-assertion construction can coexist in a single preamble, starting from
R17 V-02's base (which has C-37/C-38/C-39/C-40 but not C-36/C-31)
**Hypothesis**: R17 V-02 opens "Inertia is the adversary" (C-16, not C-36) and then applies
the refutation form ("not just enabling a tool. You are choosing a side."). Replacing
"Inertia is the adversary" with "Inertia wins the default choice" adds C-36 without
disturbing the contiguous refutation pair that satisfies C-39. If both criteria pass, this
confirms C-36 and C-39 are structurally compatible regardless of preamble base. C-31
remains broken (R17 V-02 inherited mixed identifiers).
**Expected**: C-36 PASS, C-37 PASS, C-38 PASS, C-39 PASS, C-40 PASS, C-31 FAIL

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice** — the silent competitor that benefits whenever teams
commit to a direction without asking why users would change their behavior. Every session
without Signal configured is a session where Claude has no reminder to challenge that
assumption. You are not just enabling a tool. **You are choosing a side.** Teams that
configure Signal appoint inertia a named opponent in Claude's context; teams that skip
leave the field to inertia by default. The reminder lives in CLAUDE.md and loads
automatically every session, so the choice holds without anyone having to repeat it.

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
> automatically every session, so the inertia question is in Claude's context without you
> having to remember it. The choice you made in setup holds permanently.

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

## V-04 — C-39 + C-31 combined on R17 V-05 base, letter-slot convention (golden candidate)

**Axes**: C-39 (refutation clause) + C-31 (uniform letter-slot identifiers) on R17 V-05
**Hypothesis**: Combining both R18 targets on the R17 V-05 base (which already passes
C-36/C-37/C-38/C-40) produces a spec that passes all six target criteria simultaneously.
Preamble: V-01's refutation form ("not just enabling a plugin. You are choosing a side.")
inserted into V-05's dominance-verb preamble. Identifiers: V-02's fix (GATE 6A-Found →
GATE 6AA, GATE 6A-Write → GATE 6AB). C-39 phrasing and C-31 fix are the only two
changes from R17 V-05; all other gate bodies are preserved verbatim.
**Expected**: C-36 PASS, C-37 PASS, C-38 PASS, C-39 PASS, C-40 PASS, C-31 PASS

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder
to surface the adoption question — feature specs get committed without a challenge, and
inertia collects the default because no session named it as a competitor. You are not just
enabling a plugin. **You are choosing a side.** Teams that configure Signal write inertia a
named opponent into every session, permanently. Setup happens once; your CLAUDE.md loads it
automatically, so the choice holds without you having to repeat it.

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
- (Signal section found) → GATE 6AA
- (Signal section absent or file missing) → GATE 6AB

#### GATE 6AA — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6AB — Copilot Write

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

## V-05 — C-39 + C-31 with word-suffix convention throughout (alternative C-31 approach)

**Axes**: C-39 (refutation clause) + C-31 (uniform word-suffix identifiers) on R17 V-05
**Hypothesis**: C-31 does not privilege letter-slot over word-suffix — either convention
satisfies the criterion when applied uniformly. This variation applies the same preamble
fix as V-04 but uses a consistent word-suffix scheme for all sub-gates. If V-04 and V-05
both pass C-31, the criterion is encoding-agnostic and any internally-uniform scheme
qualifies. Identifier mapping: GATE 1A → GATE 1-Miss, GATE 1B → GATE 1-Decline,
GATE 2A → GATE 2-Found, GATE 4A → GATE 4-Confirm, GATE 4B → GATE 4-Decline,
GATE 6A → GATE 6-Copilot, GATE 6B → GATE 6-Decline, GATE 6A-Found → GATE 6CP-Found,
GATE 6A-Write → GATE 6CP-Write (6CP = sub-gate of 6-Copilot, encoding parent lineage
as "6" + "CP").
**Expected**: C-36 PASS, C-37 PASS, C-38 PASS, C-39 PASS, C-40 PASS, C-31 PASS

---

You are running `/signal-setup`. Configure Signal in this workspace after installation.

**Inertia wins the default choice.** When Signal is not configured, Claude has no reminder
to surface the adoption question — feature specs get committed without a challenge, and
inertia collects the default because no session named it as a competitor. You are not just
enabling a plugin. **You are choosing a side.** Teams that configure Signal write inertia a
named opponent into every session, permanently. Setup happens once; your CLAUDE.md loads it
automatically, so the choice holds without you having to repeat it.

---

### GATE 1 — Detect CLAUDE.md

Read the workspace root for `CLAUDE.md`.

Route:
- (file missing) → GATE 1-Miss
- (file found) → GATE 2

#### GATE 1-Miss — CLAUDE.md Missing

> No CLAUDE.md found. Signal needs one to write the configuration.
> Create a new CLAUDE.md with the Signal section? [yes / no]

Route:
- (yes) → create minimal CLAUDE.md, proceed to GATE 3 with creation noted in GATE 5 report
- (no) → GATE 1-Decline

#### GATE 1-Decline — Creation Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a Signal reminder in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 2 — Detect existing Signal section

Read `CLAUDE.md`. Scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 2-Found
- (Signal section absent) → GATE 3

#### GATE 2-Found — Already Configured

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
- (yes) → GATE 4-Confirm
- (no) → GATE 4-Decline

#### GATE 4-Confirm — Confirmed

Append the section to `CLAUDE.md`. Do not overwrite existing content. Proceed to GATE 5.

#### GATE 4-Decline — Declined

> No changes made.

Inertia wins the planning stage: the spec gets committed without a named competitor in
Claude's context, and the question of why teams would do nothing never gets asked before
the feature direction is locked.

---

### GATE 5 — Report outcome

> Signal section appended to CLAUDE.md — exactly as shown in GATE 3.
> Inertia has a named opponent in Claude's context every session.

*(If GATE 1-Miss created CLAUDE.md: note that a new CLAUDE.md was created and the Signal
section was appended to it.)*

Proceed to GATE 6.

---

### GATE 6 — Optional Copilot extension

> Would you also like to add a Signal section to `.github/copilot-instructions.md`?
> This extends Signal awareness to GitHub Copilot during implementation. [yes / no / skip]

Route:
- (yes) → GATE 6-Copilot
- (no or skip) → GATE 6-Decline

#### GATE 6-Copilot — Copilot Write Path

Step 1 — file detection: Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate for file-existence — file creation is included in the confirmed write action
when the file is missing; no separate confirmation point is required.)*

Step 2 — content detection: If the file exists, scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 6CP-Found
- (Signal section absent or file missing) → GATE 6CP-Write

#### GATE 6CP-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6CP-Write — Copilot Write

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

#### GATE 6-Decline — Copilot Declined

> Copilot instructions not updated.

At the implementation stage, inertia wins the build suggestion through Copilot: code that
assumes adoption gets generated without the inertia question in context, and adoption
assumptions get locked into the implementation before anyone asks whether they are
warranted.

---

## Axis Coverage Summary

| Variation | Primary Axis | C-36 | C-37 | C-38 | C-39 | C-40 | C-31 | Structural Base |
|-----------|-------------|------|------|------|------|------|------|-----------------|
| V-01 | C-39 (refutation clause) | PASS | PASS | PASS | PASS | PASS | FAIL | R17 V-05 |
| V-02 | C-31 (letter-slot uniformity) | PASS | PASS | PASS | FAIL | PASS | PASS | R17 V-05 |
| V-03 | C-36 + C-39 coexistence | PASS | PASS | PASS | PASS | PASS | FAIL | R17 V-02 |
| V-04 | C-39 + C-31 letter-slot | PASS | PASS | PASS | PASS | PASS | PASS | R17 V-05 |
| V-05 | C-39 + C-31 word-suffix | PASS | PASS | PASS | PASS | PASS | PASS | R17 V-05 |

## Synthesis Notes

**V-04 is the primary golden candidate.** V-05 is a structural control that tests whether
C-31 is encoding-agnostic. Key decisions:

1. **C-39 mechanism** (V-01, V-03, V-04, V-05): The sentence pair "You are not just
   enabling a plugin. You are choosing a side." satisfies C-39 because (a) it negates the
   weaker tool-framing ("not just enabling a plugin"), (b) immediately asserts the stronger
   adversarial-choice framing ("choosing a side"), and (c) the two sentences are contiguous
   within the same paragraph — satisfying "same logical unit." The insertion point matters:
   the pair is placed after the inertia-collection sentence (preserving C-36's subject-verb
   construction as the paragraph opener) and before the "Teams" sentence (preserving C-37).

2. **C-31 mechanism — letter-slot (V-02, V-04)**: Renaming GATE 6A-Found → GATE 6AA and
   GATE 6A-Write → GATE 6AB converts the only word-suffix sub-gates to the letter-slot
   convention used by all other sub-gates (GATE 1A/1B, GATE 2A, GATE 4A/4B, GATE 6A/6B).
   C-25 is satisfied: GATE 6AA encodes parent=6A and branch=A; GATE 6AB encodes parent=6A
   and branch=B.

3. **C-31 mechanism — word-suffix (V-05)**: Renaming ALL sub-gates to word-suffix
   eliminates the mixed-convention source from the other direction. GATE 6CP-Found and
   GATE 6CP-Write use the "6CP" prefix, encoding parent=6-Copilot (the "6" identifies the
   primary gate; "CP" identifies the Copilot sub-path) and branch=Found/Write. C-25 is
   satisfied because the identifier encodes parent lineage ("6CP" links to "6-Copilot")
   and branch position ("Found" vs "Write").

4. **C-36 + C-39 independence (V-03)**: V-03 demonstrates the two criteria are compatible:
   opening with "Inertia wins the default choice" (C-36) does not prevent the refutation
   pair from working later in the same paragraph. The C-36 dominance verb is the paragraph
   opener; the C-39 refutation pair follows. Both criteria are satisfied simultaneously.

5. **V-03 vs V-01 as controls**: V-01 adds C-39 to R17 V-05 (which has C-36/C-37/C-38/
   C-40). V-03 adds C-36 to R17 V-02 (which has C-37/C-38/C-39/C-40). Both should produce
   the same criteria pass/fail pattern (pass C-36 through C-40, fail C-31). If they both
   score identically, this confirms that neither base introduced hidden passes or failures
   on the other criteria.

6. **V-04 over V-05 as primary**: V-04 makes the minimal change set from R17 V-05 (two
   sentence insertions in the preamble, two gate renames). V-05 renames seven gates,
   introducing more surface area for scoring edge cases on C-25/C-29/C-35. V-04 is the
   lower-risk golden candidate; V-05 validates the encoding-agnostic interpretation of C-31.
