---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-17
rubric_version: 17
round: 19
---

# signal-setup Variations — Round 19 (v17 rubric)

**Skill**: signal-setup
**Rubric**: v17 | **Denominator**: 42 (aspirational C-09–C-42) | **Date**: 2026-03-17
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/42 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

R18 produced two golden candidates — V-04 (letter-slot uniform) and V-05 (word-suffix
uniform) — both expected to pass all v16 criteria (C-36/C-37/C-38/C-39/C-40/C-31).
The v17 rubric adds two new criteria extracted from R18 excellence patterns:

| Criterion | Source from R18 | What it tests |
|-----------|-----------------|---------------|
| C-41 | V-04: `GATE 6AA/6AB` as depth-2 children of `GATE 6A`; V-05: `GATE 6CP-Found/6CP-Write` as depth-2 children of `GATE 6-Copilot` | Recursive lineage encoding — depth-2 identifiers extend the parent chain by one encoding unit |
| C-42 | V-05: `6CP` for `6-Copilot` is unambiguous (no sibling of `GATE 6-Copilot` under `GATE 6` compresses to the same prefix) | Abbreviation uniqueness — word-suffix depth-2 prefixes must be non-colliding among siblings |

**R18 V-04 analysis under v17**: Letter-slot throughout. GATE 6A → GATE 6AA/6AB.
`6AA` encodes parent `6A` (by concatenation: `6A` + `A` → `6AA`). C-41 PASS.
C-42 is vacuous — letter-slot specs have no abbreviation step. **Net: V-04 passes all 42.**

**R18 V-05 analysis under v17**: Word-suffix throughout. GATE 6-Copilot → GATE 6CP-Found/
6CP-Write. `6CP` encodes parent `6-Copilot` (6 = parent gate number, CP = Copilot abbreviation).
C-41 PASS. GATE 6's first-level sub-gates are `6-Copilot` and `6-Decline`; only `6-Copilot`
has depth-2 children, so no abbreviation collision exists. C-42 PASS.
**Net: V-05 passes all 42.**

**R19 focus**: Since both golden candidates already pass C-41/C-42, R19 establishes the
failure modes through controlled negative variations and stress-tests the criteria with a
richer tree (two optional integrations) that exercises C-42 both in failure and passing forms.

**Single-axis choices for R19** (3 variations):
- **V-01**: C-41 failure axis — letter-slot spec where depth-2 identifiers drop the parent
  branch letter (naming children of `GATE 6A` as `GATE 6-Found` / `GATE 6-Write`);
  isolates C-41 as the failure vector (C-31 also fails as a byproduct of mixed convention)
- **V-02**: C-42 failure axis — word-suffix spec with two optional integrations
  (Copilot + VS Code) whose first-level branch names both abbreviate to `6C-`, creating
  an unresolvable depth-2 collision; C-41 structurally present but C-42 FAIL
- **V-03**: C-42 pass axis — same two-integration structure as V-02 but with explicitly
  non-colliding abbreviations (`6Cop-` for Copilot, `6VS-` for VS Code); confirms
  C-42 satisfaction when abbreviation discipline is applied

**Combined axes** (2 variations):
- **V-04**: R18 V-04 confirmed under v17 — letter-slot golden candidate; all 42 criteria
  expected PASS; no text changes from R18 V-04, with explicit depth-2 chain annotation
- **V-05**: R18 V-05 confirmed under v17 — word-suffix golden candidate; all 42 criteria
  expected PASS; no text changes from R18 V-05, with explicit C-42 disambiguation annotation

---

## V-01 — Depth-2 identifiers drop parent branch slot (C-41 failure axis)

**Axis**: C-41 — letter-slot spec where depth-2 sub-gates do not carry the parent's branch
letter in their identifier; children of `GATE 6A` are named `GATE 6-Found` and
`GATE 6-Write` rather than `GATE 6AA` and `GATE 6AB`
**Hypothesis**: Dropping the `A` slot from the parent `GATE 6A` in the depth-2 identifiers
causes C-41 to fail — a reader who sees `GATE 6-Found` cannot determine from the identifier
alone whether it belongs to `GATE 6A` or is a direct sub-gate of `GATE 6`. C-31 also fails
(the spec mixes letter-slot convention at depth-1 with word-suffix convention at depth-2).
All other gate bodies are identical to R18 V-04 to isolate depth-2 naming as the sole axis.
**Expected**: C-41 FAIL, C-31 FAIL, all R18 V-04 passes preserved on all other criteria

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
- (Signal section found) → GATE 6-Found
- (Signal section absent or file missing) → GATE 6-Write

#### GATE 6-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6-Write — Copilot Write

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

## V-02 — Word-suffix with colliding abbreviations in two-integration tree (C-42 failure axis)

**Axis**: C-42 — word-suffix spec where GATE 6 has two first-level integration paths
(Copilot and VS Code) whose branch names both shorten to `6C-`, creating an unresolvable
depth-2 namespace; C-41 is structurally present (encoding unit exists) but fails the
interpretability requirement C-42 enforces
**Hypothesis**: A word-suffix spec that naively abbreviates `6-Copilot` → `6C` and
`6-Code` → `6C` satisfies C-41's structural form (a depth-2 prefix is present) while
violating C-42's uniqueness requirement — two branches share the prefix, making it
impossible for a reader to determine which first-level gate a depth-2 identifier belongs
to from the identifier alone. All preamble and decline anchors are preserved from R18 V-05.
**Expected**: C-41 structural form PRESENT but C-42 FAIL, C-31 PASS (uniform word-suffix),
all preamble/decline criteria preserved from R18 V-05

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
- (VS Code) → GATE 6-Code
- (skip) → GATE 6-Decline

#### GATE 6-Copilot — Copilot Write Path

Check whether `.github/copilot-instructions.md` exists.

*(No sub-gate for file-existence — creation is included in the confirmed write; no
separate confirmation point is required.)*

If file exists, scan for `## Signal` heading.

Route:
- (Signal section found) → GATE 6C-Found
- (Signal section absent or file missing) → GATE 6C-Write

#### GATE 6C-Found — Copilot Already Configured

> Copilot instructions already contain a Signal section. While Copilot is suggesting
> implementation code, the inertia question is already in Copilot's context — adoption
> assumptions surface during the build, not only at the planning stage. No change needed.

Exit.

#### GATE 6C-Write — Copilot Write

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

#### GATE 6-Code — VS Code Write Path

Check whether `.vscode/settings.json` exists.

*(No sub-gate for file-existence — creation is included in the confirmed write; no
separate confirmation point is required.)*

If file exists, scan for `signal.inertia` key.

Route:
- (key found) → GATE 6C-Found
- (key absent or file missing) → GATE 6C-Write

*(Note: GATE 6C-Found and GATE 6C-Write are reused identifiers — `6C` abbreviates both
`6-Copilot` and `6-Code`, making the namespace unresolvable. A reader cannot determine
from `GATE 6C-Found` alone whether this is a Copilot path or a VS Code path. This is
the C-42 failure this variation is designed to demonstrate.)*

#### GATE 6-Decline — Extensions Declined

> No additional tools configured.

At the implementation stage, inertia wins the build suggestion: Signal awareness is absent
from the tools that generate code and workspace context, so adoption assumptions get
written into the implementation before anyone asks whether they are warranted.

---

## V-03 — Word-suffix two-integration tree with non-colliding abbreviations (C-42 pass axis)

**Axis**: C-42 — same two-integration structure as V-02, but abbreviations chosen to be
unambiguous: `6-Copilot` → `6Cop`, `6-Code` → `6VS`; depth-2 children are `GATE 6Cop-Found`,
`GATE 6Cop-Write`, `GATE 6VS-Found`, `GATE 6VS-Write`; no two first-level branches of
GATE 6 share the same prefix under this scheme
**Hypothesis**: Applying discipline in abbreviation selection — choosing distinct prefixes
that do not share leading characters — satisfies C-42's uniqueness requirement while
preserving C-41's structural extension requirement. The two-integration structure of V-02
is retained; only the abbreviation tokens change. If V-03 passes C-42 and V-02 fails it,
the criterion confirms it is abbreviation uniqueness, not tree structure, that determines
the pass/fail boundary.
**Expected**: C-41 PASS, C-42 PASS, C-31 PASS (uniform word-suffix), all preamble/decline
criteria from R18 V-05 preserved

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

Check whether `.vscode/settings.json` exists.

*(No sub-gate for file-existence — creation is included in the confirmed write; no
separate confirmation point is required.)*

If file exists, scan for `signal.inertia` key.

Route:
- (key found) → GATE 6VS-Found
- (key absent or file missing) → GATE 6VS-Write

#### GATE 6VS-Found — VS Code Already Configured

> VS Code workspace settings already contain a Signal entry. During development, the
> inertia question is present in the workspace annotation layer — adoption assumptions
> surface in the editor context, not only at planning. No change needed.

Exit.

#### GATE 6VS-Write — VS Code Write

Add (or create) the Signal workspace annotation:

```json
{
  "signal.inertia": "Inertia wins the default choice. Ask: what would cause adoption, and what would prevent it?"
}
```

> Signal annotation written to `.vscode/settings.json`.
> During development, the inertia question is present in VS Code workspace context before
> implementation assumptions get locked in.

Exit.

#### GATE 6-Decline — Extensions Declined

> No additional tools configured.

At the implementation stage, inertia wins the build suggestion: Signal awareness is absent
from the tools that generate and annotate code, so adoption assumptions get written into
the implementation before anyone asks whether they are warranted.

---

## V-04 — R18 V-04 confirmed under v17 (letter-slot golden candidate)

**Axes**: C-41 + C-42 confirmation on R18 V-04 (letter-slot uniform, all v16 criteria passing)
**Hypothesis**: R18 V-04 already satisfies C-41 and C-42. `GATE 6AA` extends `GATE 6A` by
one letter (concatenation: `6A` + `A` → `6AA`); `GATE 6AB` extends `GATE 6A` by one letter
(`6A` + `B` → `6AB`). C-41 PASS. Letter-slot specs pass C-42 vacuously — no abbreviation
step, no collision risk. C-42 vacuous PASS. The spec text is unchanged from R18 V-04; only
the header annotation is added to document the v17 compliance argument explicitly.
**Expected**: ALL 42 criteria PASS — primary golden candidate under v17

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

## V-05 — R18 V-05 confirmed under v17 (word-suffix golden candidate)

**Axes**: C-41 + C-42 confirmation on R18 V-05 (word-suffix uniform, all v16 criteria passing)
**Hypothesis**: R18 V-05 already satisfies C-41 and C-42. `GATE 6CP-Found` extends
`GATE 6-Copilot` by encoding the parent's word-suffix as the abbreviation `CP` (Copilot →
CP) and adding the child's branch label `-Found`. C-41 PASS. For C-42: GATE 6's first-level
sub-gates are `GATE 6-Copilot` and `GATE 6-Decline`; only `GATE 6-Copilot` has depth-2
children. No other first-level branch of GATE 6 abbreviates to `CP`, so no collision exists.
C-42 PASS. The spec text is unchanged from R18 V-05; only the header annotation is added.
**Expected**: ALL 42 criteria PASS — alternate golden candidate under v17

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

| Variation | Primary Axis | C-41 | C-42 | C-31 | C-36 | C-37 | C-38 | C-39 | C-40 | Structural Base |
|-----------|-------------|------|------|------|------|------|------|------|------|-----------------|
| V-01 | C-41 failure (depth-2 drops parent branch) | FAIL | vacuous | FAIL | PASS | PASS | PASS | PASS | PASS | R18 V-04 |
| V-02 | C-42 failure (colliding abbreviations) | structural PASS | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | R18 V-05 + 2 integrations |
| V-03 | C-42 pass (disambiguation) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | V-02 with distinct abbreviations |
| V-04 | C-41 + C-42 confirmed (letter-slot) | PASS | vacuous | PASS | PASS | PASS | PASS | PASS | PASS | R18 V-04 verbatim |
| V-05 | C-41 + C-42 confirmed (word-suffix) | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | R18 V-05 verbatim |

## Synthesis Notes

**V-04 and V-05 are the primary golden candidates** under v17 (identical to R18 V-04/V-05).
V-03 is an additional passing variant that confirms C-42 holds when a richer tree is
disciplined. Key decisions:

1. **C-41 failure mechanism (V-01)**: The failure mode is naming depth-2 children as
   `GATE 6-Found` / `GATE 6-Write` rather than `GATE 6AA` / `GATE 6AB`. The word-suffix
   suffix `Found`/`Write` carries semantic meaning but drops the parent branch letter `A`
   entirely. A reader who sees `GATE 6-Found` cannot determine whether this is a child of
   `GATE 6A` or a direct child of `GATE 6` — the grandparent relationship is unrecoverable
   from the identifier alone. C-41 requires the encoding to be *independently navigable*;
   V-01 demonstrates what happens when that requirement is not met. C-31 fails as a
   byproduct (letter-slot spec now contains word-suffix depth-2 identifiers).

2. **C-42 failure mechanism (V-02)**: The failure is structural, not a typo. When two
   first-level branches under the same parent gate are added to the spec (`6-Copilot` and
   `6-Code`), both naturally abbreviate to `6C`. No amount of care in constructing the
   depth-2 identifier can resolve the collision once the first-level names share a leading
   prefix. V-02 encodes this as an annotation inside GATE 6-Code, showing the reader what
   the failure looks like in context. C-41 is structurally satisfied (encoding unit present)
   but C-42 makes it uninterpretable.

3. **C-42 pass mechanism (V-03)**: The fix is abbreviation discipline: choosing distinct
   tokens (`6Cop` vs `6VS`) rather than defaulting to the initial consonant. The tree
   structure is identical to V-02; the only change is the abbreviation tokens. This
   confirms V-02's failure was not structural but lexical — a solvable naming problem, not
   a structural incompatibility between word-suffix and multi-branch trees.

4. **C-42 vacuity in letter-slot (V-04)**: Letter-slot depth-2 identifiers use concatenation
   (`6A` + `A` = `6AA`), not abbreviation. There is no step where a word-suffix is compressed
   to a shorter token, so there is no opportunity for collision. C-42 passes vacuously in
   V-04 — the criterion's integrity constraint does not apply when the depth-2 encoding
   mechanism is not abbreviation-based.

5. **C-42 non-vacuous pass in V-05**: V-05 uses word-suffix throughout, so C-42 applies
   non-vacuously. The key observation: GATE 6's first-level sub-gates are `6-Copilot` and
   `6-Decline`. Only `6-Copilot` has depth-2 children. Since there is only one branch
   requiring depth-2 expansion, no abbreviation collision is possible — the C-42 uniqueness
   requirement is satisfied by the absence of competing siblings, not by deliberate
   disambiguation. V-03 demonstrates what happens when a second branch is added: discipline
   is required. V-05 passes C-42 by tree sparsity; V-03 passes by abbreviation discipline.
   Both are valid; V-05 is the simpler spec.

6. **V-03 as a forward look**: V-03 previews what a multi-integration spec would look like
   when designed with C-42 compliance in mind. If Signal extends to VS Code in a future
   version, V-03's abbreviation scheme (`6Cop-`, `6VS-`) provides the template for adding
   integration paths without creating depth-2 identifier collisions.
