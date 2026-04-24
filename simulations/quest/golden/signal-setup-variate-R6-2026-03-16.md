# signal-setup Variations — Round 6 (v6-2026-03-16 rubric)
**Skill**: signal-setup
**Rubric**: v6-2026-03-16 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-20 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=12**
**Date**: 2026-03-16
**Round**: 6

---

## Context: what informed this round

Round 6 targets the v6 rubric. The v6 rubric adds two criteria observed in the R5 V-05 pattern
and formalizes them:

| Criterion | What it requires | Gap in V-05 R4 baseline |
|-----------|-----------------|------------------------|
| C-19 | Future-moment anchor (C-18 pattern) threads through **every** decline exit — not only GATE 4, but also GATE 1 (missing-file decline) | GATE 1 decline says "Inertia has no named opponent here. Run /signal-setup when ready." — no future-moment anchor |
| C-20 | GATE 2 already-configured path names the **mechanism** behind permanence: that CLAUDE.md loads automatically every session, meaning the inertia question is present without the user having to remember | GATE 2 says "your CLAUDE.md carries the reminder" — affirms consequence (C-15) but does not name how auto-load creates the permanence |

**v6 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=12 (C-09..C-20)

**Formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

**Golden threshold**: all 5 essentials PASS AND composite >= 80

**Score landmarks**:
- All essential + all recommended + all aspirational: 100
- All essential + all recommended + 0 aspirational: 90
- All essential + 0 recommended + 0 aspirational: 60

**V-05 R4 performance against v6 rubric** (the carry-forward baseline):
- C-01..C-12: All PASS (gate structure, edge-case gates, all behaviors)
- C-13: PASS (motivational preamble: "Configure once. Fight inertia every time.")
- C-14: PASS (GATE 4 decline names consequence)
- C-15: PASS (GATE 2 affirms positive consequence)
- C-16: PASS (inertia named as adversary in opening)
- C-17: PASS ("a Signal section... gives Claude a persistent reminder... before every feature, every session. Configure once." — "setup endures" argument present)
- C-18: PASS at GATE 4 ("before the next build" anchor) but FAIL at GATE 1 (no anchor)
- C-19: **FAIL** — GATE 1 decline carries no future-moment anchor; GATE 4 does
- C-20: **FAIL** — GATE 2 names the consequence but not the auto-load mechanism

**Predicted V-05 R4 composite against v6**:
```
(5/5 * 60) + (3/3 * 30) + (10/12 * 10) = 60 + 30 + 8.3 = 98.3
```

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Thread future-moment anchor to GATE 1 decline (C-19 fix) | GATE 1's decline currently says "Inertia has no named opponent in this workspace. Run /signal-setup when you are ready to add it." Adding "before you write the first line" — the same kind of future-moment anchor GATE 4 uses ("before the next build") — satisfies C-19. Single-axis change: GATE 1 decline only. Risk: The specific future moment for GATE 1 (no CLAUDE.md) may differ from GATE 4 (CLAUDE.md exists, user declines append). The "first line" anchor is accurate — the workspace has no CLAUDE.md at all, so every subsequent session starts without Signal context. |
| B | Name persistence mechanism in GATE 2 (C-20 fix) | GATE 2 currently affirms consequence ("your CLAUDE.md carries the reminder") but does not explain the mechanism. C-20 requires naming how it works: "Every session that opens this workspace loads CLAUDE.md and inherits the inertia question — automatically, without you having to remember." Single-axis change: GATE 2 only. Risk: The mechanism sentence may feel technical in a context that has been motivationally warm — "loads CLAUDE.md automatically" could read like a tool implementation detail rather than a human benefit. Framing matters. |
| C | Thread to GATE 6 Copilot decline (C-19 coverage extension) | GATE 6's decline for Copilot instructions currently says "Copilot will not carry the Signal context or the inertia rule." C-19 requires future-moment anchoring at *every* equivalent exit. If GATE 6 is treated as an equivalent decline exit (user exits without full configuration), it too should carry a specific future-moment anchor ("before the next Copilot session asks about building X"). Single-axis: GATE 6 decline only. Risk: GATE 6 is a secondary optional step — Signal IS configured by the time GATE 6 runs. The "equivalent exit" language in C-19 may not apply to optional secondary targets. This variation tests that interpretation. |
| D | A + B: Thread anchor + name mechanism | Fixes both new criteria simultaneously without touching any other axis. All other gates unchanged from V-05 R4 baseline. Risk: low — the two changes are in different gates and do not interact. |
| E | A + B + C: Full coverage of all decline exits | Extends D to include GATE 6 Copilot decline with its own future-moment anchor. If C-19 applies to GATE 6, this is the 100-point variation. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+C)

Base behaviors in all variations: C-01 through C-18 are preserved from V-05 R4.
Rubric in scope: v6 (C-01..C-20, A denominator = 12)
Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/12 * 10)`

---

## V-01 — Axis A: Thread future-moment anchor to GATE 1 decline

**Variation axis**: C-19 (single gate, GATE 1 decline)
**Hypothesis**: The only gap for C-19 in V-05 R4 is that GATE 1's decline path lacks the
future-moment anchor that GATE 4 carries. Adding a specific "before you write the first line"
anchor to GATE 1 decline satisfies C-19 without altering any other gate. The GATE 4 text is
preserved unchanged; the GATE 1 text is the single modification.

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
> Inertia already has a named opponent in this workspace — your CLAUDE.md carries the reminder
> to ask "why would teams do nothing?" before every build. No changes needed.
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
> .github/copilot-instructions.md not updated. Copilot will not carry the Signal context
> or the inertia rule. Run /signal-setup again to update it.

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

**V-01 change from V-05 R4 baseline:**
- GATE 1 decline: Added "there is no reminder to ask 'why would teams do nothing?' before you write the first line" — future-moment anchor now present

**V-01 expected gains vs V-05 R4:**
- C-19: PASS (both GATE 1 and GATE 4 decline paths now carry a future-moment anchor: "before you write the first line" and "before the next build" respectively)
- C-20: unchanged — FAIL (GATE 2 still names consequence but not mechanism)

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (11/12 * 10) = 60 + 30 + 9.2 = **99.2**

---

## V-02 — Axis B: Name persistence mechanism in GATE 2

**Variation axis**: C-20 (single gate, GATE 2)
**Hypothesis**: GATE 2's existing response affirms that inertia "already has a named opponent"
(C-15) but does not explain HOW. C-20 requires naming the mechanism: CLAUDE.md is loaded
automatically at the start of every Claude Code session, so the inertia question is present
without the user having to remember. Single-axis: GATE 2 only, all other gates unchanged.

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
> Signal not configured. Inertia has no named opponent in this workspace.
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
> .github/copilot-instructions.md not updated. Copilot will not carry the Signal context
> or the inertia rule. Run /signal-setup again to update it.

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

**V-02 change from V-05 R4 baseline:**
- GATE 2 response: Replaced "your CLAUDE.md carries the reminder to ask... before every build" with
  "every session that opens this workspace loads CLAUDE.md automatically, so the inertia question
  is present from the first message, without you having to remember to invoke it"

**V-02 expected gains vs V-05 R4:**
- C-20: PASS (GATE 2 now names the auto-load mechanism explicitly)
- C-19: unchanged — FAIL (GATE 1 decline still lacks future-moment anchor)

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (11/12 * 10) = 60 + 30 + 9.2 = **99.2**

---

## V-03 — Axis C: Thread future-moment anchor to GATE 6 Copilot decline

**Variation axis**: C-19 coverage extension (GATE 6 decline only)
**Hypothesis**: C-19 requires the future-moment anchor at every equivalent exit. V-05 R4 already
has it at GATE 4. V-01 adds it to GATE 1. This variation tests whether GATE 6 (Copilot
instructions decline) also qualifies as an "equivalent exit" under C-19. If yes, adding a
Copilot-specific future-moment anchor ("before the next Copilot session reaches for a build
suggestion") satisfies C-19's broadest interpretation. Single-axis: GATE 6 decline only.

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
> Signal not configured. Inertia has no named opponent in this workspace.
> Run /signal-setup when you are ready to add it.
Stop here.

If Y: proceed to GATE 4 (CONFIRM) with create-new mode.

---

## GATE 2 — ALREADY CONFIGURED (edge case)

A Signal section already exists in CLAUDE.md.

Respond:
> Signal is already configured.
> Inertia already has a named opponent in this workspace — your CLAUDE.md carries the reminder
> to ask "why would teams do nothing?" before every build. No changes needed.
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
> Copilot will not carry the inertia rule — before the next Copilot session reaches for a build
> suggestion, there is no prompt in its context to ask "why would teams do nothing first?"
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

**V-03 change from V-05 R4 baseline:**
- GATE 6 decline: Added future-moment anchor "before the next Copilot session reaches for a build
  suggestion, there is no prompt in its context to ask 'why would teams do nothing first?'"

**V-03 expected gains vs V-05 R4:**
- C-19 (extended reading): PASS if GATE 6 counts as an equivalent exit gate; PARTIAL if C-19 only
  applies to primary "no Signal at all" exit gates (GATE 1 and GATE 4)
- C-20: unchanged — FAIL (GATE 2 still lacks mechanism)
- C-19 (primary): FAIL (GATE 1 decline still lacks anchor; GATE 6 fix alone does not satisfy C-19)

**Predicted composite (narrow C-19 reading)**: (5/5 * 60) + (3/3 * 30) + (10/12 * 10) = **98.3**
**Predicted composite (broad C-19 reading)**: (5/5 * 60) + (3/3 * 30) + (11/12 * 10) = **99.2**

This variation is the C-19 boundary case — its score depends on whether the rubric means "all
Signal-absent decline exits" or "all decline exits."

---

## V-04 — Axes A + B: Thread anchor + name mechanism

**Variation axis**: C-19 + C-20
**Hypothesis**: Fixing both new criteria in isolation confirms they do not interact — GATE 1 change
and GATE 2 change are independent gates. Together they address the two v6 gaps without structural
change to any other path. This combination should predict 100 under the narrow reading of C-19.

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
> .github/copilot-instructions.md not updated. Copilot will not carry the Signal context
> or the inertia rule. Run /signal-setup again to update it.

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

**V-04 changes from V-05 R4 baseline:**
- GATE 1 decline: "there is no reminder to ask 'why would teams do nothing?' before you write the first line" (Axis A)
- GATE 2 response: "every session that opens this workspace loads CLAUDE.md automatically, so the inertia question is present from the first message, without you having to remember to invoke it" (Axis B)

**V-04 expected gains vs V-05 R4:**
- C-19: PASS (GATE 1 and GATE 4 both carry future-moment anchors)
- C-20: PASS (GATE 2 names the auto-load mechanism)
- All C-01..C-18: unchanged — PASS

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (12/12 * 10) = 60 + 30 + 10 = **100.0**

---

## V-05 — Axes A + B + C: Full coverage — all decline exits carry equivalent arguments

**Variation axis**: C-19 (GATE 1) + C-20 (GATE 2) + C-19 extended (GATE 6)
**Hypothesis**: If the broadest reading of C-19 applies — "every point where the user exits
without full configuration" includes GATE 6 — then V-04 still leaves a gap at the Copilot
decline. V-05 applies the future-moment framing to all three decline paths: GATE 1, GATE 4,
and GATE 6. This is the maximum-coverage variation. It also ensures that the phrasing contrast
between the three future moments is semantically distinct:
  - GATE 1: "before you write the first line" (workspace has no CLAUDE.md at all)
  - GATE 4: "before the next build" (workspace has CLAUDE.md, user declined to add Signal)
  - GATE 6: "before the next Copilot session reaches for a build suggestion" (Copilot target)

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
> Copilot will not carry the inertia rule — before the next Copilot session reaches for a build
> suggestion, there is no prompt in its context to ask "why would teams do nothing first?"
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

**V-05 changes from V-05 R4 baseline:**
- GATE 1 decline: "there is no reminder to ask 'why would teams do nothing?' before you write the first line" (Axis A)
- GATE 2 response: "every session that opens this workspace loads CLAUDE.md automatically, so the inertia question is present from the first message, without you having to remember to invoke it" (Axis B)
- GATE 6 decline: "before the next Copilot session reaches for a build suggestion, there is no prompt in its context to ask 'why would teams do nothing first?'" (Axis C)

**Three distinct future moments — one per decline exit:**
- GATE 1: "before you write the first line" — workspace with no context file at all
- GATE 4: "before the next build" — workspace with CLAUDE.md, Signal absent
- GATE 6: "before the next Copilot session reaches for a build suggestion" — Copilot missing rule

**V-05 expected gains vs V-05 R4:**
- C-19 (narrow): PASS (GATE 1 and GATE 4 covered)
- C-19 (broad): PASS (GATE 1, GATE 4, and GATE 6 all covered)
- C-20: PASS (GATE 2 names auto-load mechanism)
- All C-01..C-18: unchanged — PASS

**Predicted composite (narrow C-19)**: identical to V-04 = **100.0**
**Predicted composite (broad C-19)**: also **100.0** — GATE 6 fix is already achieved by V-04 +
narrow reading; it adds no new criterion under the current rubric. V-05 is a robustness variant —
it holds in both readings.

---

## Summary

| Variation | Axes | C-19 | C-20 | Gate changed | Predicted composite |
|-----------|------|------|------|--------------|---------------------|
| V-01 | A: GATE 1 anchor | PASS | FAIL | GATE 1 decline | ~99.2 |
| V-02 | B: GATE 2 mechanism | FAIL | PASS | GATE 2 response | ~99.2 |
| V-03 | C: GATE 6 anchor | PARTIAL* | FAIL | GATE 6 decline | ~98.3–99.2 |
| V-04 | A+B: anchor + mechanism | PASS | PASS | GATE 1 + GATE 2 | **100.0** |
| V-05 | A+B+C: all exits | PASS | PASS | GATE 1 + GATE 2 + GATE 6 | **100.0** |

*V-03 C-19: PASS under broad reading (GATE 6 as equivalent exit), PARTIAL under narrow reading
(GATE 1 still lacks anchor)

**Design recommendation**: V-04 is the minimum-change path to 100. V-05 is the semantically
complete variant — three future moments, one per exit, no argument weaker than any other.
If C-19's "equivalent exit" definition is ever expanded to include secondary optional targets,
V-05 is already correct; V-04 is not.
