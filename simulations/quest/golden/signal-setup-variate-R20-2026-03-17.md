---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-17
rubric_version: 18
round: 20
---

# signal-setup Variations — Round 20 (v18 rubric)

**Skill**: signal-setup
**Rubric**: v18 | **Denominator**: 45 (aspirational C-09–C-45) | **Date**: 2026-03-17
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/45 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

R19 produced two golden candidates — V-04 (letter-slot uniform) and V-05 (word-suffix
uniform) — both confirming R18 V-04 and R18 V-05 pass all v17 criteria (C-41/C-42
explicitly; C-36 through C-40 preserved verbatim from R18).

The v18 rubric adds three new criteria extracted from R19 non-trivial evidence:

| Criterion | Source from R19 | What it tests |
|-----------|-----------------|---------------|
| C-43 | V-02 C-30 PASS — both `6-Copilot` and `6-Code` carry identical rationale text | Cross-gate annotation consistency: parallel inline-detection paths in optional-extension gates must carry functionally identical promotion rationale |
| C-44 | V-01 C-38 PASS — "through Copilot: code that assumes adoption gets generated…" | Artifact specificity: tool-specific decline anchors must name the concrete output the tool produces under inertia, not merely name inertia as the winner |
| C-45 | V-01 C-24 PASS — "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context" | Concurrent-moment placement: secondary already-configured affirmations must place Signal as co-present during active tool operation, not as an archival installation fact |

**R19 V-04 analysis under v18** (letter-slot, single Copilot integration):
- C-43: Only one optional-extension gate (GATE 6A). No parallel inline-detection paths exist.
  C-43 passes vacuously — the consistency requirement applies only when two or more parallel
  gates make the same architectural choice.
- C-44: GATE 6B decline — "inertia wins the build suggestion through Copilot: code that
  assumes adoption gets generated without the inertia question in context." The artifact
  (code that assumes adoption) is named. **C-44 PASS**.
- C-45: GATE 6AA already-configured — "While Copilot is suggesting implementation code,
  the inertia question is already in Copilot's context." Concurrent-moment construction
  with Copilot as the active subject. **C-45 PASS**.
- **Net: V-04 passes all 45.**

**R19 V-05 analysis under v18** (word-suffix, single Copilot integration):
- C-43: Only one optional-extension gate (GATE 6-Copilot). C-43 passes vacuously.
- C-44: GATE 6-Decline — "inertia wins the build suggestion through Copilot: code that
  assumes adoption gets generated without the inertia question in context." **C-44 PASS**.
- C-45: GATE 6CP-Found — "While Copilot is suggesting implementation code, the inertia
  question is already in Copilot's context." **C-45 PASS**.
- **Net: V-05 passes all 45.**

**R20 focus**: Since both golden candidates already satisfy C-43 (vacuously), C-44, and
C-45, R20 establishes the failure modes for each new criterion through controlled negative
variations, then confirms the golden status of R19 V-04 and V-05 under v18.

**Single-axis choices for R20** (3 variations):
- **V-01**: C-43 failure axis — two-integration spec (Copilot + VS Code, non-colliding
  abbreviations from R19 V-03) where GATE 6-Copilot carries the inline-detection annotation
  but GATE 6-VSCode does not; the second parallel gate is structurally identical to the first
  yet lacks the rationale text, making C-43's consistency requirement unmet. GATE 6VS-Found
  is updated to use concurrent framing (correcting R19 V-03's archival VS Code path) to
  isolate C-43 as the sole failure axis.
- **V-02**: C-44 failure axis — single-Copilot spec (letter-slot from R19 V-04) where
  GATE 6B names inertia as the winning party ("inertia wins the build suggestion through
  Copilot") but omits the artifact — no "code that assumes adoption gets generated" or
  equivalent. C-38 PASS (inertia, not Copilot, wins); C-44 FAIL (artifact absent).
- **V-03**: C-45 failure axis — single-Copilot spec (word-suffix from R19 V-05) where
  GATE 6CP-Found describes Signal's presence as a future state the team will encounter
  ("when the team reaches the build phase, the inertia question will be in Copilot's
  context") rather than as a co-present operational fact. C-24 PASS (tool-local consequence);
  C-45 FAIL (concurrent-moment construction absent).

**Combined axes** (2 variations):
- **V-04**: R19 V-04 confirmed under v18 — letter-slot golden candidate; all 45 criteria
  expected PASS; no text changes from R19 V-04.
- **V-05**: R19 V-05 confirmed under v18 — word-suffix golden candidate; all 45 criteria
  expected PASS; no text changes from R19 V-05.

---

## V-01 — Asymmetric inline annotation in parallel extension gates (C-43 failure axis)

**Axis**: C-43 — two-integration spec (Copilot + VS Code, word-suffix with non-colliding
abbreviations `6Cop`/`6VS`) where GATE 6-Copilot carries the inline-detection annotation
but GATE 6-VSCode does not; the two paths are structurally identical (both check file
existence inline, both bundle creation into the confirmed write), yet only one carries the
rationale text justifying the inline treatment.
**Hypothesis**: The second parallel gate's omission creates an indeterminate reading —
a scorer cannot tell whether the absence of annotation on GATE 6-VSCode is a deliberate
architectural statement or an oversight. C-43 closes this gap by requiring the rationale
to appear in every gate that makes the same choice. C-30 passes on the annotated gate;
C-43 fails because the annotation is not consistent across the parallel pair. All preamble,
primary-path, and GATE 6-Copilot bodies are identical to R19 V-03. GATE 6-VSCode loses
its annotation. GATE 6VS-Found is updated to concurrent framing to isolate C-43 as the
sole failure vector.
**Expected**: C-43 FAIL; C-30 conditional PASS (annotated gate passes; absent annotation
on GATE 6-VSCode is the C-43 failure, not a C-30 failure since C-30 only fires when an
inline path exists without annotation — GATE 6-VSCode simply has no annotation at all,
which is the C-43 gap); C-41 PASS; C-42 PASS; C-44 vacuous (no per-tool decline gates);
C-45 PASS on both GATE 6Cop-Found and GATE 6VS-Found; all R19 V-03 preamble criteria
preserved.

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

### GATE 6 — Optional tool extensions

> Would you also like to extend Signal awareness to other development tools?
>
> - **Copilot** — adds Signal to `.github/copilot-instructions.md` (implementation code suggestions)
> - **VS Code** — adds Signal to `.vscode/settings.json` as a workspace annotation
> - **Skip** — no additional tools

Route:
- (Copilot) → GATE 6-Copilot
- (VS Code) → GATE 6-VSCode
- (skip) → GATE 6-Decline

#### GATE 6-Copilot — Copilot Write Path

Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate for file-existence — creation is included in the confirmed write; no
separate confirmation point is required.)*

If file exists, scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 6Cop-Found
- (Signal section absent or file missing) → GATE 6Cop-Write

#### GATE 6Cop-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6Cop-Write — Copilot Write

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

#### GATE 6-VSCode — VS Code Write Path

Check whether `.vscode/settings.json` exists. If file exists, scan for `signal.inertia` key.

Route:
- (key found) → GATE 6VS-Found
- (key absent or file missing) → GATE 6VS-Write

#### GATE 6VS-Found — VS Code Already Configured

> VS Code workspace settings already contain a Signal entry. While VS Code is open and
> the workspace annotation layer is active, the inertia question is present in the
> development context — adoption assumptions surface in the editor, not only at planning.
> No change needed.

Exit.

#### GATE 6VS-Write — VS Code Write

Add (or create) the Signal workspace annotation:

```json
{
  "signal.inertia": "Inertia wins the default choice. Ask: what would cause adoption, and what would prevent it?"
}
```

> Signal annotation written to `.vscode/settings.json`.
> While VS Code is open, the inertia question is present in workspace context before
> implementation assumptions get locked in.

Exit.

#### GATE 6-Decline — Extensions Declined

> No additional tools configured.

At the implementation stage, inertia wins the build suggestion: Signal awareness is absent
from the tools that generate and annotate code, so adoption assumptions get written into
the implementation before anyone asks whether they are warranted.

---

## V-02 — Copilot decline names inertia as winner but omits the artifact (C-44 failure axis)

**Axis**: C-44 — single-Copilot letter-slot spec (base: R19 V-04) where GATE 6B names
inertia as the winning party at the implementation stage but stops before naming what
Copilot produces under inertia's control; the artifact ("code that assumes adoption gets
generated") is absent from the consequence anchor.
**Hypothesis**: "Inertia wins the build suggestion through Copilot — Signal is absent from
the implementation context" satisfies C-38 (inertia, not Copilot, named as winner) and
C-33 (inertia as grammatical subject of victory) but fails C-44: the anchor does not reach
downstream to the concrete artifact the tool emits. The force is named; the channel is
named; but the output of the channel is not named. The C-38 → C-21 → C-44 causal chain
stops one link short. All other gates are identical to R19 V-04.
**Expected**: C-44 FAIL; C-38 PASS; C-33 PASS; C-34 conditional PASS (two-step chain
present: inertia wins → assumptions get locked in); C-41 PASS; C-42 vacuous; all R19 V-04
criteria preserved on all other gates.

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

At the implementation stage, inertia wins the build suggestion through Copilot — Signal is
absent from the implementation context, and adoption assumptions get locked into the build
before anyone asks whether they are warranted.

---

## V-03 — Already-configured affirmation uses archival framing instead of concurrent (C-45 failure axis)

**Axis**: C-45 — single-Copilot word-suffix spec (base: R19 V-05) where GATE 6CP-Found
describes Signal's presence as a future state the team will encounter ("when the team
reaches the build phase, the inertia question will be in Copilot's context") rather than
as a co-present operational fact active while the tool runs. The affirmation uses future
conditional rather than concurrent-moment construction.
**Hypothesis**: "When the team reaches the build phase, the inertia question will be in
Copilot's context" satisfies C-24 (tool-local consequence in Copilot's vocabulary) but
fails C-45: future conditional ("will be") describes a coming state rather than an ongoing
operational reality. C-45 requires the "while [tool] is [active verb phrase]" construction
or equivalent that shows Signal as co-present at the moment the tool acts, not as a
benefit that will materialize later. A reader learns that Signal will eventually be useful;
they do not learn that Signal is active right now when Copilot acts. All other gates are
identical to R19 V-05.
**Expected**: C-45 FAIL; C-24 PASS; C-15 PASS (positive consequence affirmed); C-20 PASS
(persistence mechanism named in GATE 2-Found); C-41 PASS; C-42 PASS (single extension,
vacuous); all R19 V-05 criteria preserved on all other gates.

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

> Copilot instructions already contain a Signal section — inertia has a named opponent at
> the implementation stage. When the team reaches the build phase, the inertia question
> will be in Copilot's context before implementation assumptions get locked in. No change
> needed.

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

## V-04 — R19 V-04 confirmed under v18 (letter-slot golden candidate)

**Axes**: C-43 + C-44 + C-45 confirmation on R19 V-04 (letter-slot uniform, all v17
criteria passing).
**Hypothesis**: R19 V-04 already satisfies all three new criteria. C-43 passes vacuously
— the spec has only one optional-extension gate (GATE 6A), so no parallel inline-detection
paths exist and the consistency requirement has nothing to enforce. C-44 PASS — GATE 6B
names inertia as the winning party AND names the artifact: "code that assumes adoption
gets generated." C-45 PASS — GATE 6AA places Signal in concurrent operation: "While
Copilot is suggesting implementation code, the inertia question is already in Copilot's
context." The spec text is unchanged from R19 V-04; only the header annotation is updated
to document the v18 compliance argument.
**Expected**: ALL 45 criteria PASS — primary golden candidate under v18.

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

## V-05 — R19 V-05 confirmed under v18 (word-suffix golden candidate)

**Axes**: C-43 + C-44 + C-45 confirmation on R19 V-05 (word-suffix uniform, all v17
criteria passing).
**Hypothesis**: R19 V-05 already satisfies all three new criteria. C-43 passes vacuously
— only one optional-extension gate (GATE 6-Copilot), so no parallel inline-detection
paths to compare. C-44 PASS — GATE 6-Decline names the artifact: "code that assumes
adoption gets generated without the inertia question in context." C-45 PASS — GATE
6CP-Found uses concurrent-moment construction: "While Copilot is suggesting implementation
code, the inertia question is already in Copilot's context." The spec text is unchanged
from R19 V-05; only the header annotation is updated to document v18 compliance.
**Expected**: ALL 45 criteria PASS — alternate golden candidate under v18.

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

| Variation | Primary Axis | C-43 | C-44 | C-45 | C-41 | C-42 | C-31 | C-38 | C-40 | Structural Base |
|-----------|-------------|------|------|------|------|------|------|------|------|-----------------|
| V-01 | C-43 failure (asymmetric annotation) | FAIL | vacuous | PASS | PASS | PASS | PASS | vacuous | PASS | R19 V-03 + concurrent VS Code path |
| V-02 | C-44 failure (artifact omitted) | vacuous | FAIL | PASS | PASS | vacuous | PASS | PASS | PASS | R19 V-04 verbatim except GATE 6B |
| V-03 | C-45 failure (archival framing) | vacuous | PASS | FAIL | PASS | PASS | PASS | PASS | PASS | R19 V-05 verbatim except GATE 6CP-Found |
| V-04 | C-43/44/45 confirmed (letter-slot) | vacuous | PASS | PASS | PASS | vacuous | PASS | PASS | PASS | R19 V-04 verbatim |
| V-05 | C-43/44/45 confirmed (word-suffix) | vacuous | PASS | PASS | PASS | PASS | PASS | PASS | PASS | R19 V-05 verbatim |

## Synthesis Notes

**V-04 and V-05 are the primary golden candidates** under v18 (identical to R19 V-04/V-05,
which are identical to R18 V-04/V-05 for the spec body). The golden text has been stable
since R18. Key decisions:

1. **C-43 failure mechanism (V-01)**: The failure mode is annotation asymmetry on
   structurally identical gates. GATE 6-Copilot carries "(No sub-gate for file-existence
   — creation is included in the confirmed write; no separate confirmation point is
   required.)" but GATE 6-VSCode does not. A scorer reading GATE 6-VSCode sees inline
   detection without rationale and cannot determine whether this was a deliberate
   architectural choice (same as GATE 6-Copilot) or an oversight. C-43 closes this gap:
   when two gates make the same architectural choice, both must carry the justification.
   V-01 also updates GATE 6VS-Found to use concurrent framing to isolate C-43 as the
   sole failure vector — R19 V-03's "During development" phrasing would add a C-45 failure
   that obscures the isolation.

2. **C-44 failure mechanism (V-02)**: The failure is one link short in the causal chain.
   "Inertia wins the build suggestion through Copilot — Signal is absent from the
   implementation context, and adoption assumptions get locked into the build" satisfies
   C-38 (inertia as winner, not Copilot) and C-33 (adversary named as grammatical subject
   of victory) but fails C-44 because the anchor does not name what Copilot produces.
   The force is present (inertia), the channel is present (through Copilot), the
   consequence is present (assumptions locked in) — but the artifact is absent. C-44
   requires the anchor to additionally reach the concrete output: "code that assumes
   adoption gets generated." The chain C-38 → C-21 → C-44 is force → path context →
   artifact; V-02 satisfies the first two links and drops the third.

3. **C-45 failure mechanism (V-03)**: The failure is temporal register. "When the team
   reaches the build phase, the inertia question will be in Copilot's context" uses
   future conditional — it describes a benefit that will materialize, not a co-presence
   that is active now. C-24 is satisfied: the framing is tool-local (Copilot's context,
   implementation stage). C-45 is not satisfied: the "while [tool] is [active verb phrase]"
   construction — which makes Signal visibly present at the moment Copilot acts — is
   absent. A reader understands they will benefit eventually; they do not understand that
   Signal is co-present right now, today, in every Copilot interaction.

4. **C-43 vacuity in single-extension specs (V-02, V-03, V-04, V-05)**: When a spec has
   only one optional-extension gate, no parallel inline-detection paths can exist by
   definition. C-43's consistency requirement has nothing to enforce and passes vacuously.
   C-43 becomes non-vacuous only when a second integration path is added (as in V-01's
   Copilot + VS Code structure). This means the v18 golden candidates (V-04, V-05) pass
   C-43 vacuously — their single-extension structure is not a weakness but a fact about
   their scope. A future multi-integration golden would need to satisfy C-43 non-vacuously.

5. **R19 V-03 as a partially compliant base**: R19 V-03 (two integrations, non-colliding
   word-suffix abbreviations) satisfies C-43 (both GATE 6-Copilot and GATE 6-VSCode carry
   identical annotation) but its GATE 6VS-Found uses "During development" rather than the
   "while [VS Code] is [active]" construction, which borderline-fails C-45. V-01 corrects
   this by updating GATE 6VS-Found to "While VS Code is open and the workspace annotation
   layer is active" — making V-01 a cleaner isolation of C-43 than a straight copy of R19
   V-03 would be. If V-03 from R19 had been scored on v18, it would likely fail C-45 on
   the VS Code path while passing C-43.

6. **The three criteria as a precision chain**: C-43 (consistency) → C-44 (artifact) →
   C-45 (concurrent presence) each add one level of concrete specificity over the
   existing criteria they extend. C-43 closes the gap between "annotating one gate" and
   "annotating all structurally equivalent gates." C-44 closes the gap between "naming
   the force that wins" and "naming what the force produces." C-45 closes the gap between
   "stating that Signal is installed" and "showing Signal as active at the moment the tool
   acts." Together they describe a progression from abstract correctness to vivid
   operational presence.
