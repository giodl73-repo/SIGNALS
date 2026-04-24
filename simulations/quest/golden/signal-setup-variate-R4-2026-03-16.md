# signal-setup Variations — Round 4 (v4-2026-03-16 rubric)
**Skill**: signal-setup
**Rubric**: v4-2026-03-16 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-16 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=8**
**Date**: 2026-03-16
**Round**: 4

---

## Context: what informed this round

Round 4 targets the v4 rubric dated 2026-03-16. The existing golden (`signals/signal-setup.md`)
was written directly without a quest loop and scores well on C-01 through C-10. The v4 rubric
adds two new aspirational criteria extracted from R3 signals:

| Change | R3 (v3) | R4 (v4) | Design consequence |
|--------|---------|---------|-------------------|
| C-15 (already-configured affirmation) | Not in rubric | **New Aspirational** — already-configured path must name what the existing setup achieves, not just confirm no action is needed | The current golden says "Nothing to do." C-15 PASS requires something like "Inertia already has a named opponent here." Structural placement is the same; the behavioral consequence shifts from acknowledgement to affirmation. |
| C-16 (inertia as adversary, not concept) | Not in rubric | **New Aspirational** — inertia must be named as a silent competitor or adversary in the preamble/opening, not merely referenced as a rule inside the appended content | The current golden's Signal section says "the primary competitor is always inertia" as a rule. C-16 requires this framing in the skill's own opening — the user understands they are choosing a side when they configure, not just learning a system principle. |
| N_aspirational denominator | 6 (C-09..C-14) | **8 (C-09..C-16)** | Formula: aspirational contribution changes from /6 to /8. |

**v4 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=8 (C-09..C-16)

**Formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essentials PASS AND composite >= 80

**Score landmarks:**
- All essential + all recommended + all aspirational: 100
- All essential + all recommended + no aspirational: 90
- All essential + no recommended + no aspirational: 60

**Existing golden weaknesses** (against v4 rubric):
- C-11: Steps numbered but not labeled as gates with explicit entry/exit conditions — PARTIAL
- C-12: Already-configured and no-CLAUDE.md cases handled as inline conditionals — PARTIAL
- C-13: No motivational preamble; opens directly with procedural framing — FAIL
- C-14: Decline path says "Run /signal-setup any time" — does not name consequence — PARTIAL
- C-15: Already-configured path says "Nothing to do" — no affirmation — FAIL (NEW)
- C-16: Inertia named as rule inside appended content, not as adversary in skill opening — FAIL (NEW)

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Inertia as adversary in preamble | C-16 requires inertia named as opponent/silent competitor in the skill's opening, not merely in the appended Signal section content. The existing golden mentions inertia inside the preview block as "the primary competitor" — a rule to learn. Axis A moves this framing to the skill's own opening: the user understands they are choosing a side in a conflict before they see any procedural step. Risk: a strong preamble that opens with adversary framing may feel dramatic relative to a procedural setup skill; the user may read it as a philosophical interlude and skip to the steps. |
| B | Already-configured path affirms positive consequence | C-15 requires the skip-write response to name what the existing configuration achieves, not merely confirm no action. The current golden says "Nothing to do." Axis B changes this to a response that names the active benefit — e.g., "Inertia already has a named opponent in this workspace." The user learns what their setup does for them. Risk: the affirmation language must be specific enough to satisfy C-15 (naming consequence) without being falsely reassuring if the Signal section is stale or incomplete. |
| C | Decline path names consequence | C-14 requires the decline response to explicitly name what remains unaddressed when the user says no — not just "No changes made" or "Run /signal-setup anytime." Axis C changes the decline response to name the gap: e.g., "Signal not configured. Inertia remains unnamed in this workspace — no reminder to ask 'why would teams do nothing?' before the next build." Risk: naming a consequence the user chose not to address can feel prescriptive or judgmental; the phrasing must be informative rather than scolding. |
| D | Motivational preamble before procedure | C-13 requires a brief philosophical or motivational framing — explaining why setup matters — before any procedural steps begin. The inertia concept must appear as a reason to configure, not only as output content. Axis D adds a preamble block that explains what Signal setup creates and why it persists between sessions. Risk: a preamble that is too long slows down experienced users who run /signal-setup programmatically; the preamble should be short (2-4 sentences) and not obstruct the procedural flow. |
| E | Named gate checkpoints with edge-case gates | C-11 requires phases labeled as explicit numbered gates with entry/exit conditions. C-12 requires the already-configured and missing-CLAUDE.md cases to be treated as dedicated named gates, not inline conditionals. Axis E restructures the prompt from numbered steps into labeled GATE blocks, each with explicit entry and exit conditions, including full dedicated gate definitions for each edge-case path. Risk: more structural scaffolding may not change execution behavior in practice — gates that are labeled but not enforced by position collapse to annotated steps. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (D)
Combinations: V-04 (A+B+C), V-05 (A+B+C+D+E)

Base behaviors in all variations (from existing golden): C-01 through C-10 are preserved.
Rubric in scope: `simulations/quest/rubrics/signal-setup-rubric-v4-2026-03-16.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)`
N_essential=5, N_recommended=3, N_aspirational=8
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 — Axis A: Inertia as adversary in preamble

**Variation axis**: Inertia framing
**Hypothesis**: Moving inertia from the appended Signal section content into the skill's opening
statement — and naming it as a silent adversary rather than a rule — changes the user's
understanding of what they are doing. They are not running a setup step; they are choosing to
give Signal a home in their context so it can fight inertia on their behalf.

---

```
You are running /signal-setup.

Every Signal workspace has one silent competitor. Not a rival tool. Not a competing methodology.
Inertia — the choice to do nothing, trust the existing guess, skip the research, and ship without
asking. Signal cannot challenge what it cannot see. This skill gives Signal visibility in your
workspace context so it can be invoked before every build.

---

## Step 1: Check current state

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Check if a Signal section already exists (look for `## Signal` or `Signal is installed`).

If Signal section already found:
> Signal is already configured in your CLAUDE.md. Nothing to do.
> Run `/signal` to see all available skills.
Stop here.

---

## Step 2: Preview

Show the user exactly what will be added:

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

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N: stop. Print "Run /signal-setup any time to configure Signal."

---

## Step 3: Write to CLAUDE.md

If confirmed:
1. If CLAUDE.md exists: append the Signal section at the end
2. If CLAUDE.md does not exist: create it with just the Signal section
3. Confirm: "Signal section added to CLAUDE.md ✓"

---

## Step 4: GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If yes, ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If confirmed, append:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

---

## Step 5: Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-01 expected gains vs existing golden:**
- C-16: PASS (inertia named as silent adversary in skill opening, not only in appended content)
- C-13: PARTIAL (adversary framing introduced but no full motivational preamble explaining *why* setup matters over time)
- All other criteria: unchanged

---

## V-02 — Axis B: Already-configured path affirms positive consequence

**Variation axis**: Already-configured affirmation
**Hypothesis**: When the skill detects an existing Signal section and responds with an affirmation
of what that configuration achieves — rather than "Nothing to do" — the user understands the
active benefit of their prior setup. The response names the working state, not the absence of
required action.

---

```
You are running /signal-setup for the current workspace.

Signal skills are installed in `.claude/skills/`. This skill adds Signal to your
workspace context so Claude knows the skills are available.

---

## Step 1: Check current state

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Check if a Signal section already exists (look for `## Signal` or `Signal is installed`).

If Signal section already found:
> Signal is already configured in your CLAUDE.md.
> Inertia already has a named opponent here — your workspace context includes the reminder
> to ask "why would teams do nothing?" before any build.
> Run `/signal` to see all available skills.
Stop here.

---

## Step 2: Preview

Show the user exactly what will be added:

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

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N: stop. Print "Run /signal-setup any time to configure Signal."

---

## Step 3: Write to CLAUDE.md

If confirmed:
1. If CLAUDE.md exists: append the Signal section at the end
2. If CLAUDE.md does not exist: create it with just the Signal section
3. Confirm: "Signal section added to CLAUDE.md ✓"

---

## Step 4: GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If yes, ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If confirmed, append:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

---

## Step 5: Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-02 expected gains vs existing golden:**
- C-15: PASS (already-configured response names what the existing setup achieves: "Inertia already has a named opponent here")
- C-16: No change — inertia still named only inside the appended content and the affirmation, not in the skill's own preamble as an adversary
- All other criteria: unchanged

---

## V-03 — Axis D: Motivational preamble before procedure

**Variation axis**: Phrasing register — motivational/philosophical opening
**Hypothesis**: A 3-sentence preamble explaining *why* setup matters — what Signal context creates
and why it needs to persist between sessions — satisfies C-13's requirement for a philosophical
framing before procedure. Users who understand the reason for setup complete it with more intention
and are less likely to skip or defer.

---

```
You are running /signal-setup.

Teams skip Signal not because they disagree with it — because configuring a context file feels
like overhead on a sprint that is already behind. But setup happens once. The question
"why would teams do nothing instead?" needs to live in Claude's context for every session
that follows. This step creates that persistence.

---

## Step 1: Check current state

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Check if a Signal section already exists (look for `## Signal` or `Signal is installed`).

If Signal section already found:
> Signal is already configured in your CLAUDE.md. Nothing to do.
> Run `/signal` to see all available skills.
Stop here.

---

## Step 2: Preview

Show the user exactly what will be added:

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

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N: stop. Print "Run /signal-setup any time to configure Signal."

---

## Step 3: Write to CLAUDE.md

If confirmed:
1. If CLAUDE.md exists: append the Signal section at the end
2. If CLAUDE.md does not exist: create it with just the Signal section
3. Confirm: "Signal section added to CLAUDE.md ✓"

---

## Step 4: GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If yes, ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If confirmed, append:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

---

## Step 5: Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-03 expected gains vs existing golden:**
- C-13: PASS (preamble explains why setup matters — "setup happens once, the question needs to live in context for every session that follows" — before any procedural step)
- C-16: PARTIAL (inertia introduced as the question setup creates persistence for — implied opponent role — but not explicitly named as adversary or silent competitor)
- All other criteria: unchanged

---

## V-04 — Axes A + B + C: Adversary framing + affirmation + decline consequence

**Variation axis**: Inertia framing + already-configured affirmation + decline consequence
**Hypothesis**: The three behavioral consequence criteria (C-14, C-15, C-16) are mutually
reinforcing. Naming inertia as an adversary in the opening establishes the frame; affirming
what existing configuration achieves makes the already-configured response consistent with that
frame; naming the consequence of decline closes the loop. Together they create coherent behavioral
accountability at every exit point.

---

```
You are running /signal-setup.

Every Signal workspace has one silent competitor: inertia. Not a rival tool — the choice to
do nothing, to trust the guess, to build without asking. Signal cannot challenge what your
workspace context does not name. This skill names it.

---

## Step 1: Check current state

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Check if a Signal section already exists (look for `## Signal` or `Signal is installed`).

If Signal section already found:
> Signal is already configured in your CLAUDE.md.
> Inertia already has a named opponent here. Your context file carries the reminder to ask
> "why would teams do nothing?" before every build.
> Run `/signal` to see all available skills.
Stop here.

---

## Step 2: Preview

Show the user exactly what will be added:

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

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured. Inertia remains unnamed in this workspace — there is no reminder in
> your context to ask "why would teams do nothing?" before the next build.
> Run /signal-setup when you are ready to change that.
Stop here.

---

## Step 3: Write to CLAUDE.md

If confirmed:
1. If CLAUDE.md exists: append the Signal section at the end
2. If CLAUDE.md does not exist: create it with just the Signal section
3. Confirm: "Signal section added to CLAUDE.md ✓"

---

## Step 4: GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If yes, ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> GitHub Copilot not configured. Copilot will not have Signal context or the inertia rule.
> Run /signal-setup again to update .github/copilot-instructions.md.

If confirmed, append:
---
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
---

Confirm: ".github/copilot-instructions.md updated ✓"

---

## Step 5: Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
```

---

**V-04 expected gains vs existing golden:**
- C-14: PASS (decline path names consequence: "Inertia remains unnamed in this workspace — no reminder to ask why teams would do nothing before the next build")
- C-15: PASS (already-configured path affirms: "Inertia already has a named opponent here")
- C-16: PASS (inertia named as silent competitor in the skill's own opening sentence)
- C-13: PARTIAL (adversary framing present but not a full motivational preamble explaining *why* setup matters over time)
- C-11/C-12: No structural change — phases numbered but not gated

---

## V-05 — Axes A + B + C + D + E: Full coverage

**Variation axis**: All axes combined — adversary framing + affirmation + decline consequence +
motivational preamble + named gate checkpoints with edge-case gates
**Hypothesis**: Maximizing all aspirational criteria simultaneously — while preserving every
essential and recommended behavior — produces the highest composite score against the v4 rubric.
The gate structure enforces phase sequencing; the adversary framing and consequential responses
at every exit point create a coherent skill that teaches as it configures.

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

If Y: proceed to GATE 4 (WRITE) with create-new mode.

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

**V-05 expected gains vs existing golden:**
- C-11: PASS (each phase is a named GATE with explicit entry and exit conditions; no phase can be implicitly skipped)
- C-12: PASS (GATE 1 and GATE 2 are dedicated named gates for edge cases, not inline conditionals inside the happy path)
- C-13: PASS (4-sentence preamble explains why setup matters — "configure once, fight inertia every time" — before any gate)
- C-14: PASS (GATE 4 decline names consequence: "Inertia remains unnamed... That question will not be in Claude's context by default")
- C-15: PASS (GATE 2 affirms: "Inertia already has a named opponent in this workspace — your CLAUDE.md carries the reminder")
- C-16: PASS (opening names inertia as adversary: "inertia wins every build where it is not named")

**Remaining risk**: The gate structure adds ~40% more prompt length. Longer prompts increase the
probability of partial execution or phase-skipping in practice, even when the structure enforces
sequencing. C-09 (preview matches written output) depends on no content drift between GATE 3 and
GATE 5 — the instruction to write "exactly as shown" is the only enforcement mechanism.

---

## Summary

| Variation | Axis | C-13 | C-14 | C-15 | C-16 | C-11 | C-12 | Predicted composite |
|-----------|------|------|------|------|------|------|------|---------------------|
| V-01 | A: Inertia as adversary | PARTIAL | unchanged | unchanged | PASS | unchanged | unchanged | ~89 |
| V-02 | B: Already-configured affirmation | unchanged | unchanged | PASS | unchanged | unchanged | unchanged | ~90 |
| V-03 | D: Motivational preamble | PASS | unchanged | unchanged | PARTIAL | unchanged | unchanged | ~90 |
| V-04 | A+B+C: Adversary+affirmation+decline | PARTIAL | PASS | PASS | PASS | unchanged | unchanged | ~94 |
| V-05 | A+B+C+D+E: Full coverage | PASS | PASS | PASS | PASS | PASS | PASS | ~100 |

*Predicted composite assumes existing golden passes C-01..C-10 fully.*
