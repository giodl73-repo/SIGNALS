# signal-setup Variations — Round 7 (v7-2026-03-16 rubric)
**Skill**: signal-setup
**Rubric**: v7-2026-03-16 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-21 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=13**
**Date**: 2026-03-16
**Round**: 7

---

## Context: what informed this round

Round 7 targets the v7 rubric. The v7 rubric adds one criterion observed in the R6 V-05 pattern
and formalizes it:

| Criterion | What it requires | Gap in V-05 R6 baseline |
|-----------|-----------------|------------------------|
| C-21 | Every gate where the user can decline an optional post-Signal extension step names a future-moment consequence **local to that path's tool** — not a generic reuse of primary decline framing. GATE 6 Copilot decline must name a Copilot-specific moment; GATE 4 decline names a Claude-session-specific moment. No two exits share identical consequence language when the tools they protect are distinct. | V-05 R6 GATE 6 decline says "before the next Copilot session reaches for a build suggestion, there is no prompt in its context to ask 'why would teams do nothing first?'" — this IS Copilot-specific and IS distinct from GATE 4. But both use "build" as the anchor event and both frame the absence as "no prompt/reminder in context." The distinction is by-tool but not by-phase. C-21 may demand phase-local anchors, not just tool-local anchors. |

**v7 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=13 (C-09..C-21)

**Formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 13 * 10)
```

**Golden threshold**: all 5 essentials PASS AND composite >= 80

**V-05 R6 performance against v7 rubric** (carry-forward baseline):
- C-01..C-18: All PASS
- C-19: PASS (GATE 1: "before you write the first line"; GATE 4: "before the next build")
- C-20: PASS (GATE 2 names auto-load mechanism: "loads CLAUDE.md automatically, so the inertia
  question is present from the first message, without you having to remember to invoke it")
- C-21: **PROBABLE PASS** — GATE 6 decline is Copilot-specific and distinct from GATE 4. But the
  distinction rests on tool-name only ("Copilot" vs "Claude"), not on phase. Both anchors reference
  a "build" event. C-21's strictest reading requires no shared anchor vocabulary between protected
  tools. Risk: partial credit under strict scoring.

**V-05 R6 predicted composite against v7**:
```
Best case (C-21 PASS): (5/5 * 60) + (3/3 * 30) + (13/13 * 10) = 60 + 30 + 10 = 100.0
Risk case (C-21 PARTIAL): (5/5 * 60) + (3/3 * 30) + (12/13 * 10) = 60 + 30 + 9.2 = 99.2
```

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Concretize GATE 6 decline by phase | Replace "build suggestion" with a Copilot-specific output artifact that is implementation-phase, not planning-phase (inline completion, function body). This separates GATE 4 (spec/commit decision) from GATE 6 (implementation/code output) by phase, not just by tool name. Eliminates any shared "build" vocabulary between the two exits. |
| B | Add Copilot already-configured affirm with mechanism | If .github/copilot-instructions.md already has a Signal section, the current skill either skips silently or is unspecified. Adding an explicit already-configured path for GATE 6 — naming the mechanism (copilot-instructions.md is loaded by Copilot Chat automatically) — gives GATE 6 parity with GATE 2's C-20 treatment. Not required by C-21, but symmetry may prevent future criterion gap. |
| C | Phase-label all three decline exits explicitly | Add inline labels (SPEC PHASE, IMPLEMENTATION PHASE) to consequence anchors at GATE 4 and GATE 6 so the phase distinction is explicit in the text, not inferred. Makes C-21's path-specificity unmistakable to a scorer. |
| D | A + B | Concrete phase-specific GATE 6 anchor + Copilot already-configured affirm. Isolates whether the concreteness of the future moment drives the score, separate from structural symmetry. |
| E | A + B + C | Maximum coverage: concrete Copilot implementation moment + already-configured affirm + explicit phase labels. Strongest possible C-21 formulation; also most verbose. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+C)

Base behaviors in all variations: C-01 through C-20 preserved from V-05 R6.
Rubric in scope: v7 (C-01..C-21, A denominator = 13)
Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/13 * 10)`

---

## V-01 — Axis A: Concretize GATE 6 by implementation phase

**Variation axis**: C-21 (single gate, GATE 6 decline only)
**Hypothesis**: V-05 R6's GATE 6 decline uses "build suggestion" as the future-moment anchor —
the same semantic field as GATE 4's "next build." C-21 requires consequence language that is
local to the tool's distinct role. Copilot's role is implementation (function bodies, inline
completions, code suggestions); Claude Code's role at GATE 4 is commit decision (planning,
spec, "should we build this"). Replacing "build suggestion" with "implementation suggestion" or
"first function body" makes the phase separation unmistakable and eliminates vocabulary overlap.
Single-axis: GATE 6 decline text only.

---

```
You are running /signal-setup.

Teams skip Signal not because they reject it — because there is always a reason to configure
later. Later never comes. Meanwhile, inertia wins every build where it is not named. This is
the one step that names it: a Signal section in your CLAUDE.md gives Claude a persistent
reminder to ask "why would teams do nothing instead?" before every feature, every session.
Configure once. Fight inertia every time.

---

## GATE 0 — Detect existing configuration

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

**If CLAUDE.md does not exist:** proceed to GATE 1 (MISSING FILE).
**If Signal section found:** proceed to GATE 2 (ALREADY CONFIGURED).
**If CLAUDE.md exists, no Signal section:** proceed to GATE 3 (PREVIEW).

---

## GATE 1 — MISSING FILE (edge case)

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the preview (same content as GATE 3 preview below).
Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. Inertia has no named opponent in this workspace —
> there is no reminder to ask "why would teams do nothing?" before you write the first line.
> Run /signal-setup when you are ready to add it.
Stop here.

If Y: proceed to GATE 4 (CONFIRM) with create-new mode.

---

## GATE 2 — ALREADY CONFIGURED (edge case)

A Signal section already exists in CLAUDE.md.

Respond:
> Signal is already configured.
> Inertia already has a named opponent here — every session that opens this workspace
> loads CLAUDE.md automatically, so the inertia question is present from the first message,
> without you having to remember to invoke it.
> Run `/signal` to see all 77 available commands.
Stop here.

---

## GATE 3 — Preview

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all available commands
  /competitors <topic>   inertia-first competitive analysis

The one rule: the primary competitor is always inertia. Before any feature,
ask "why would teams do nothing instead?" If you cannot answer that,
you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 4.

---

## GATE 4 — Confirm

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured.
> Inertia remains unnamed in this workspace — no reminder to ask "why would teams do nothing?"
> before the next build. That question will not be in Claude's context by default.
> Run /signal-setup when you are ready to address that.
Stop here.

If Y: proceed to GATE 5.

---

## GATE 5 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 3) to CLAUDE.md.
- If appending: add the section at the end of the file.
- If creating (GATE 1 mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 6.

---

## GATE 6 — GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If it does not exist: skip to GATE 7.

If it exists, ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> .github/copilot-instructions.md not updated.
> Copilot will not carry the inertia rule — before Copilot writes the first function body
> for a new feature, there is no instruction in its context to ask "why would teams do
> nothing instead of implementing this?" Run /signal-setup again to update it.

If Y: append to .github/copilot-instructions.md:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 7.

---

## GATE 7 — Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-01 change from V-05 R6 baseline:**
- GATE 6 decline: Replaced "before the next Copilot session reaches for a build suggestion" with
  "before Copilot writes the first function body for a new feature, there is no instruction in
  its context to ask 'why would teams do nothing instead of implementing this?'"
- Key distinction: GATE 4 anchor = "before the next build" (commit decision, planning phase)
  GATE 6 anchor = "before Copilot writes the first function body" (implementation phase, code output)
- Vocabulary separation: removed "build" from GATE 6; named a Copilot-specific output artifact

**V-01 expected gains vs V-05 R6:**
- C-21: PASS (GATE 6 now names a phase-specific Copilot implementation moment, distinct from
  GATE 4's planning/commit moment; no shared anchor vocabulary between the two tools)
- All C-01..C-20: unchanged — PASS

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (13/13 * 10) = 60 + 30 + 10 = **100.0**

---

## V-02 — Axis B: Add Copilot already-configured affirm with mechanism

**Variation axis**: GATE 6 symmetry extension (adding an already-configured sub-path to GATE 6)
**Hypothesis**: GATE 2 names the mechanism behind CLAUDE.md's permanence (auto-load per session).
GATE 6 has no equivalent path for when copilot-instructions.md already has Signal. If the file
exists and already contains Signal, the current spec either silently skips or is undefined. Adding
an explicit Copilot already-configured path — naming how copilot-instructions.md is loaded
(Copilot Chat loads workspace instructions at session start) — creates structural parity and
prevents an undefined edge case from affecting a future round's score. Single-axis: GATE 6
structure only (adding already-configured sub-path; decline text unchanged from V-05 R6).

---

```
You are running /signal-setup.

Teams skip Signal not because they reject it — because there is always a reason to configure
later. Later never comes. Meanwhile, inertia wins every build where it is not named. This is
the one step that names it: a Signal section in your CLAUDE.md gives Claude a persistent
reminder to ask "why would teams do nothing instead?" before every feature, every session.
Configure once. Fight inertia every time.

---

## GATE 0 — Detect existing configuration

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

**If CLAUDE.md does not exist:** proceed to GATE 1 (MISSING FILE).
**If Signal section found:** proceed to GATE 2 (ALREADY CONFIGURED).
**If CLAUDE.md exists, no Signal section:** proceed to GATE 3 (PREVIEW).

---

## GATE 1 — MISSING FILE (edge case)

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the preview (same content as GATE 3 preview below).
Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. Inertia has no named opponent in this workspace —
> there is no reminder to ask "why would teams do nothing?" before you write the first line.
> Run /signal-setup when you are ready to add it.
Stop here.

If Y: proceed to GATE 4 (CONFIRM) with create-new mode.

---

## GATE 2 — ALREADY CONFIGURED (edge case)

A Signal section already exists in CLAUDE.md.

Respond:
> Signal is already configured.
> Inertia already has a named opponent here — every session that opens this workspace
> loads CLAUDE.md automatically, so the inertia question is present from the first message,
> without you having to remember to invoke it.
> Run `/signal` to see all 77 available commands.
Stop here.

---

## GATE 3 — Preview

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all available commands
  /competitors <topic>   inertia-first competitive analysis

The one rule: the primary competitor is always inertia. Before any feature,
ask "why would teams do nothing instead?" If you cannot answer that,
you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 4.

---

## GATE 4 — Confirm

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured.
> Inertia remains unnamed in this workspace — no reminder to ask "why would teams do nothing?"
> before the next build. That question will not be in Claude's context by default.
> Run /signal-setup when you are ready to address that.
Stop here.

If Y: proceed to GATE 5.

---

## GATE 5 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 3) to CLAUDE.md.
- If appending: add the section at the end of the file.
- If creating (GATE 1 mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 6.

---

## GATE 6 — GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If it does not exist: skip to GATE 7.

If it exists: check whether it already contains a Signal section (marker: `## Signal`).

**If Signal already present in copilot-instructions.md:**
> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
Skip to GATE 7.

**If Signal not present in copilot-instructions.md:**
Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> .github/copilot-instructions.md not updated.
> Copilot will not carry the inertia rule — before the next Copilot session reaches for a
> build suggestion, there is no prompt in its context to ask "why would teams do nothing first?"
> Run /signal-setup again to update it.

If Y: append to .github/copilot-instructions.md:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 7.

---

## GATE 7 — Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-02 change from V-05 R6 baseline:**
- GATE 6 structure: Added already-configured sub-path for copilot-instructions.md
  "Copilot Chat loads workspace instructions at session start — the inertia rule is already
  present when Copilot begins suggesting code, without you attaching a prompt file."
- GATE 6 decline: unchanged from V-05 R6
- No other gates changed

**V-02 expected gains vs V-05 R6:**
- C-21: unchanged — PROBABLE PASS (GATE 6 decline still uses "build suggestion")
- New behavior: GATE 6 already-configured path now names the Copilot auto-load mechanism
  (C-20 parity for Copilot path; not a current criterion but closes a structural gap)
- All C-01..C-20: unchanged — PASS

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (13/13 * 10) = **100.0** (if C-21 passes)
/ (5/5 * 60) + (3/3 * 30) + (12/13 * 10) = **99.2** (if C-21 partial under strict reading)

---

## V-03 — Axis C: Phase-label all decline exits explicitly

**Variation axis**: C-21 (labeling, all decline gates — GATE 1, GATE 4, GATE 6)
**Hypothesis**: C-21 requires that consequence language be "local to that path's tool or context."
The safest way to guarantee this is to make the phase of each future moment explicit in the text:
label GATE 4's anchor as a planning/commit-phase event and GATE 6's anchor as an implementation-
phase event. Scorers applying C-21 cannot find shared language when the phase labels differ.
Single-axis: only the consequence anchor phrasing at GATE 1, GATE 4, and GATE 6 is changed; all
other gate content unchanged from V-05 R6.

---

```
You are running /signal-setup.

Teams skip Signal not because they reject it — because there is always a reason to configure
later. Later never comes. Meanwhile, inertia wins every build where it is not named. This is
the one step that names it: a Signal section in your CLAUDE.md gives Claude a persistent
reminder to ask "why would teams do nothing instead?" before every feature, every session.
Configure once. Fight inertia every time.

---

## GATE 0 — Detect existing configuration

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

**If CLAUDE.md does not exist:** proceed to GATE 1 (MISSING FILE).
**If Signal section found:** proceed to GATE 2 (ALREADY CONFIGURED).
**If CLAUDE.md exists, no Signal section:** proceed to GATE 3 (PREVIEW).

---

## GATE 1 — MISSING FILE (edge case)

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the preview (same content as GATE 3 preview below).
Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. Inertia has no named opponent in this workspace —
> there is no reminder to ask "why would teams do nothing?" before you design the first
> component. Every session that opens here starts without the question.
> Run /signal-setup when you are ready to add it.
Stop here.

If Y: proceed to GATE 4 (CONFIRM) with create-new mode.

---

## GATE 2 — ALREADY CONFIGURED (edge case)

A Signal section already exists in CLAUDE.md.

Respond:
> Signal is already configured.
> Inertia already has a named opponent here — every session that opens this workspace
> loads CLAUDE.md automatically, so the inertia question is present from the first message,
> without you having to remember to invoke it.
> Run `/signal` to see all 77 available commands.
Stop here.

---

## GATE 3 — Preview

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all available commands
  /competitors <topic>   inertia-first competitive analysis

The one rule: the primary competitor is always inertia. Before any feature,
ask "why would teams do nothing instead?" If you cannot answer that,
you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 4.

---

## GATE 4 — Confirm

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured.
> Inertia remains unnamed in this workspace — no reminder to ask "why would teams do nothing?"
> before the spec is committed. That question will not be in Claude's context at the planning
> stage. Run /signal-setup when you are ready to address that.
Stop here.

If Y: proceed to GATE 5.

---

## GATE 5 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 3) to CLAUDE.md.
- If appending: add the section at the end of the file.
- If creating (GATE 1 mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 6.

---

## GATE 6 — GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If it does not exist: skip to GATE 7.

If it exists, ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> .github/copilot-instructions.md not updated.
> Copilot will not carry the inertia rule — before Copilot starts implementing the first
> endpoint, there is no instruction in its context to ask "why would teams do nothing
> instead of shipping this?" Run /signal-setup again to update it.

If Y: append to .github/copilot-instructions.md:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 7.

---

## GATE 7 — Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-03 changes from V-05 R6 baseline:**
- GATE 1 decline: "before you design the first component" (design/planning phase, pre-spec)
  vs V-05 R6: "before you write the first line" (ambiguous phase)
- GATE 4 decline: "before the spec is committed" (planning/commit phase)
  vs V-05 R6: "before the next build" (ambiguous — could be planning or implementation)
- GATE 6 decline: "before Copilot starts implementing the first endpoint" (implementation phase)
  vs V-05 R6: "before the next Copilot session reaches for a build suggestion" (ambiguous phase)

**Phase separation achieved:**
- GATE 1: design phase ("design the first component")
- GATE 4: planning/spec phase ("spec is committed")
- GATE 6: implementation phase ("implementing the first endpoint")

**V-03 expected gains vs V-05 R6:**
- C-21: PASS — GATE 6 anchor is now implementation-phase, unambiguously distinct from GATE 4's
  planning/spec anchor. No shared vocabulary. Three distinct phases, one per exit.
- C-18: PASS — all three still anchor to a specific future moment (design, spec, endpoint)
- C-19: PASS — C-18 pattern present at both GATE 1 and GATE 4
- All C-01..C-20: unchanged — PASS

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (13/13 * 10) = 60 + 30 + 10 = **100.0**

---

## V-04 — Axes A + B: Concrete Copilot phase anchor + already-configured affirm

**Variation axis**: C-21 (GATE 6 concrete anchor) + GATE 6 structural symmetry (Axis A + B)
**Hypothesis**: V-01 makes GATE 6's consequence language implementation-phase-specific. V-02 adds
an already-configured sub-path for copilot-instructions.md. Together they produce a GATE 6 that
has full C-20/C-21 parity with GATE 2: a mechanism-naming affirm for the already-configured case,
and a phase-local consequence anchor for the decline case. These changes are independent (different
sub-paths of GATE 6) and do not interact.

---

```
You are running /signal-setup.

Teams skip Signal not because they reject it — because there is always a reason to configure
later. Later never comes. Meanwhile, inertia wins every build where it is not named. This is
the one step that names it: a Signal section in your CLAUDE.md gives Claude a persistent
reminder to ask "why would teams do nothing instead?" before every feature, every session.
Configure once. Fight inertia every time.

---

## GATE 0 — Detect existing configuration

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

**If CLAUDE.md does not exist:** proceed to GATE 1 (MISSING FILE).
**If Signal section found:** proceed to GATE 2 (ALREADY CONFIGURED).
**If CLAUDE.md exists, no Signal section:** proceed to GATE 3 (PREVIEW).

---

## GATE 1 — MISSING FILE (edge case)

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the preview (same content as GATE 3 preview below).
Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. Inertia has no named opponent in this workspace —
> there is no reminder to ask "why would teams do nothing?" before you write the first line.
> Run /signal-setup when you are ready to add it.
Stop here.

If Y: proceed to GATE 4 (CONFIRM) with create-new mode.

---

## GATE 2 — ALREADY CONFIGURED (edge case)

A Signal section already exists in CLAUDE.md.

Respond:
> Signal is already configured.
> Inertia already has a named opponent here — every session that opens this workspace
> loads CLAUDE.md automatically, so the inertia question is present from the first message,
> without you having to remember to invoke it.
> Run `/signal` to see all 77 available commands.
Stop here.

---

## GATE 3 — Preview

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all available commands
  /competitors <topic>   inertia-first competitive analysis

The one rule: the primary competitor is always inertia. Before any feature,
ask "why would teams do nothing instead?" If you cannot answer that,
you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 4.

---

## GATE 4 — Confirm

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured.
> Inertia remains unnamed in this workspace — no reminder to ask "why would teams do nothing?"
> before the next build. That question will not be in Claude's context by default.
> Run /signal-setup when you are ready to address that.
Stop here.

If Y: proceed to GATE 5.

---

## GATE 5 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 3) to CLAUDE.md.
- If appending: add the section at the end of the file.
- If creating (GATE 1 mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 6.

---

## GATE 6 — GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If it does not exist: skip to GATE 7.

If it exists: check whether it already contains a Signal section (marker: `## Signal`).

**If Signal already present in copilot-instructions.md:**
> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
Skip to GATE 7.

**If Signal not present in copilot-instructions.md:**
Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> .github/copilot-instructions.md not updated.
> Copilot will not carry the inertia rule — before Copilot writes the first function body
> for a new feature, there is no instruction in its context to ask "why would teams do
> nothing instead of implementing this?" Run /signal-setup again to update it.

If Y: append to .github/copilot-instructions.md:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 7.

---

## GATE 7 — Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-04 changes from V-05 R6 baseline:**
- GATE 6 decline: "before Copilot writes the first function body for a new feature, there is no
  instruction in its context to ask 'why would teams do nothing instead of implementing this?'"
  (Axis A — implementation-phase anchor, distinct from GATE 4's planning-phase anchor)
- GATE 6 structure: Added already-configured sub-path for copilot-instructions.md, naming the
  Copilot Chat auto-load mechanism (Axis B — symmetry with GATE 2)
- All other gates: unchanged from V-05 R6

**Three future moments (phase-distinct):**
- GATE 1: "before you write the first line" — workspace context missing entirely
- GATE 4: "before the next build" — planning/commit decision phase
- GATE 6: "before Copilot writes the first function body" — implementation output phase

**V-04 expected gains vs V-05 R6:**
- C-21: PASS — GATE 6 decline names implementation-phase moment distinct from GATE 4's
  planning-phase moment; no shared vocabulary; tool-specific output artifact named ("function body")
- Copilot already-configured path: closes a structural gap (not a current criterion)
- All C-01..C-20: unchanged — PASS

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (13/13 * 10) = 60 + 30 + 10 = **100.0**

---

## V-05 — Axes A + B + C: Full — concrete phase anchor + already-configured affirm + explicit phase labels

**Variation axis**: C-21 (GATE 6 concrete anchor) + GATE 6 already-configured affirm + phase
labels across all decline gates (Axes A + B + C)
**Hypothesis**: V-04 (A+B) fixes C-21 robustly and adds structural symmetry. V-03 (C) makes
phase distinctions explicit in the text — design, spec, implementation — so no scorer can infer
shared language. V-05 combines all three. It is the maximum-coverage variant. It also introduces
the strongest possible answer to a future criterion: GATE 6 now has a mechanism-naming affirm
(Axis B) parallel to GATE 2's C-20 treatment, and all three decline paths are phase-labeled so
that no two exits can be read as protecting the same development moment.

---

```
You are running /signal-setup.

Teams skip Signal not because they reject it — because there is always a reason to configure
later. Later never comes. Meanwhile, inertia wins every build where it is not named. This is
the one step that names it: a Signal section in your CLAUDE.md gives Claude a persistent
reminder to ask "why would teams do nothing instead?" before every feature, every session.
Configure once. Fight inertia every time.

---

## GATE 0 — Detect existing configuration

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

**If CLAUDE.md does not exist:** proceed to GATE 1 (MISSING FILE).
**If Signal section found:** proceed to GATE 2 (ALREADY CONFIGURED).
**If CLAUDE.md exists, no Signal section:** proceed to GATE 3 (PREVIEW).

---

## GATE 1 — MISSING FILE (edge case)

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the preview (same content as GATE 3 preview below).
Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. Inertia has no named opponent in this workspace —
> there is no reminder to ask "why would teams do nothing?" before you design the first
> component. Every session that opens here starts without the question.
> Run /signal-setup when you are ready to add it.
Stop here.

If Y: proceed to GATE 4 (CONFIRM) with create-new mode.

---

## GATE 2 — ALREADY CONFIGURED (edge case)

A Signal section already exists in CLAUDE.md.

Respond:
> Signal is already configured.
> Inertia already has a named opponent here — every session that opens this workspace
> loads CLAUDE.md automatically, so the inertia question is present from the first message,
> without you having to remember to invoke it.
> Run `/signal` to see all 77 available commands.
Stop here.

---

## GATE 3 — Preview

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all available commands
  /competitors <topic>   inertia-first competitive analysis

The one rule: the primary competitor is always inertia. Before any feature,
ask "why would teams do nothing instead?" If you cannot answer that,
you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 4.

---

## GATE 4 — Confirm

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured.
> Inertia remains unnamed in this workspace — no reminder to ask "why would teams do nothing?"
> before the spec is committed. That question will not be in Claude's context at the planning
> stage. Run /signal-setup when you are ready to address that.
Stop here.

If Y: proceed to GATE 5.

---

## GATE 5 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 3) to CLAUDE.md.
- If appending: add the section at the end of the file.
- If creating (GATE 1 mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 6.

---

## GATE 6 — GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If it does not exist: skip to GATE 7.

If it exists: check whether it already contains a Signal section (marker: `## Signal`).

**If Signal already present in copilot-instructions.md:**
> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
Skip to GATE 7.

**If Signal not present in copilot-instructions.md:**
Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> .github/copilot-instructions.md not updated.
> Copilot will not carry the inertia rule — before Copilot starts implementing the first
> endpoint, there is no instruction in its context to ask "why would teams do nothing
> instead of shipping this?" Run /signal-setup again to update it.

If Y: append to .github/copilot-instructions.md:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 7.

---

## GATE 7 — Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-05 changes from V-05 R6 baseline:**
- GATE 1 decline: "before you design the first component" (design phase label)
  vs V-05 R6: "before you write the first line"
- GATE 4 decline: "before the spec is committed... at the planning stage" (planning phase label)
  vs V-05 R6: "before the next build"
- GATE 6 decline: "before Copilot starts implementing the first endpoint" (implementation phase)
  vs V-05 R6: "before the next Copilot session reaches for a build suggestion"
- GATE 6 structure: Added already-configured sub-path with Copilot auto-load mechanism (Axis B)

**Three distinct phases, one per exit:**
- GATE 1: design phase — "before you design the first component"
- GATE 4: planning/spec phase — "before the spec is committed"
- GATE 6: implementation phase — "before Copilot starts implementing the first endpoint"

**V-05 expected gains vs V-05 R6:**
- C-21: PASS — three exits, three phases, three tools; no shared anchor vocabulary anywhere
- C-19 (GATE 1 and GATE 4): PASS — phase anchors are even more specific than V-05 R6
- C-18: PASS — all three anchors name concrete future moments
- C-20 (GATE 2): PASS — unchanged
- Copilot already-configured: structural gap closed (not a current criterion)
- All C-01..C-20: unchanged — PASS

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (13/13 * 10) = 60 + 30 + 10 = **100.0**

**Why V-05 is preferred over V-04**: V-04 fixes C-21 (implementation-phase anchor at GATE 6).
V-05 additionally makes all three phases explicit by label. If a future criterion requires
"each decline exit's phase is explicitly named," V-05 is already correct; V-04 is not. V-05 is
also more robust against a scorer who reads "build suggestion" (V-05 R6 GATE 6) as ambiguously
planning-phase rather than implementation-phase.

---

## Summary

| Variation | Axes | C-21 | Key change | Predicted composite |
|-----------|------|------|------------|---------------------|
| V-01 | A: GATE 6 implementation anchor | PASS | "before Copilot writes the first function body" replaces "before the next Copilot session reaches for a build suggestion" | **100.0** |
| V-02 | B: GATE 6 already-configured affirm | PROBABLE | Copilot already-configured path added with auto-load mechanism; decline text unchanged | **100.0** / 99.2 |
| V-03 | C: Phase labels all declines | PASS | GATE 1: design, GATE 4: spec, GATE 6: implementation — explicit phase labels, no shared vocabulary | **100.0** |
| V-04 | A+B: Concrete anchor + affirm | PASS | Implementation-phase GATE 6 anchor + Copilot already-configured sub-path | **100.0** |
| V-05 | A+B+C: All axes | PASS | Phase-labeled declines (design/spec/implementation) + GATE 6 affirm + concrete GATE 6 anchor | **100.0** |

**Design recommendation**: V-01 is the minimum-change path to a robust C-21 PASS — one sentence
change, clear phase distinction. V-03 is the structural clarity variant — all phases labeled,
hardest to misread. V-05 is the maximum-coverage variant — closes all gaps across all gates
simultaneously. If scoring is being done by a rubric reader rather than automated, V-05's
explicit phase labels leave least room for ambiguity.

**Carry-forward for R8**: V-05 (A+B+C) unless scoring shows V-01's single-change is sufficient.
If V-05 scores 100 and V-01 also scores 100, prefer V-01 for minimalism (follow CLAUDE.md:
avoid over-engineering; the right amount of complexity is the minimum needed for the task).
