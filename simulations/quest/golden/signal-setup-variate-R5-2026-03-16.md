# signal-setup Variations — Round 5 (v5-2026-03-16 rubric)
**Skill**: signal-setup
**Rubric**: v5-2026-03-16 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-18 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=10**
**Date**: 2026-03-16
**Round**: 5

---

## Context: what informed this round

Round 5 targets the v5 rubric dated 2026-03-16. R4 champion V-05 (Axes A+B+C+D+E) achieved PASS
on C-11 through C-16 for a predicted perfect score against the v4 rubric. The v5 rubric adds two
new aspirational criteria extracted from R4 excellence signals:

| Change | R4 (v4) | R5 (v5) | Design consequence |
|--------|---------|---------|-------------------|
| C-17 (temporal persistence explanation) | Not in rubric | **New Aspirational** — the preamble must explain not just *why* inertia matters but *why the configuration must persist*: setup happens once, but the reminder must live in Claude's context for every session that follows | R4 V-05 preamble says "Configure once. Fight inertia every time." — temporal persistence as slogan. C-17 PASS requires the *argument*: write to CLAUDE.md → every future session loads CLAUDE.md → the question is present without you remembering. |
| C-18 (decline anchors to future moment) | Not in rubric | **New Aspirational** — the decline feedback must connect the absence to a specific future moment where it will be felt, not merely name what was declined | R4 V-05 GATE 4 decline says "before the next build" — this likely PASSES C-18. The R5 variation space is in *how specific* and *how vivid* that future moment is. |
| N_aspirational denominator | 8 (C-09..C-16) | **10 (C-09..C-18)** | Formula: aspirational contribution changes from /8 to /10. |

**v5 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=10 (C-09..C-18)

**Formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

**Golden threshold**: all 5 essentials PASS AND composite >= 80

**Score landmarks:**
- All essential + all recommended + all aspirational: 100
- All essential + all recommended + no aspirational: 90
- All essential + no recommended + no aspirational: 60

**R4 V-05 diagnosis against v5 rubric:**

| Criterion | v4 verdict | v5 verdict | Note |
|-----------|-----------|-----------|------|
| C-17 | Not in rubric | **PARTIAL** | "Configure once. Fight inertia every time." contains the setup-endures *implication* but not the *argument*. The mechanism (write once → loads every session → question is present automatically) is gestured at but not explained. The slogan is not a causal chain. |
| C-18 | Not in rubric | **PASS** | GATE 4 decline: "before the next build" — specific future moment present. |
| C-01..C-16 | PASS | PASS | All preserved. |

**Predicted R4 V-05 score against v5**: (5/5 * 60) + (3/3 * 30) + (9/10 * 10) = **99**

R5 primary target: **C-17** — convert from PARTIAL to PASS by making the temporal persistence
argument explicit, not sloganed.
R5 secondary: **C-18** — confirm and test whether a more vivid future moment improves the
criterion or introduces presumptuousness risk.

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Explicit temporal persistence argument in preamble | C-17 requires the preamble to explain *why* configuration must persist — not assert that it does. R4 V-05's "Configure once. Fight inertia every time." is an injunction. The explicit form names the mechanism: write to CLAUDE.md → every future session that opens this workspace loads CLAUDE.md automatically → the inertia question is present without you remembering to ask it. Axis A tests whether 2-3 sentences stating this causal chain shifts C-17 from PARTIAL to PASS without making the preamble feel like a system tutorial. Risk: over-explaining the file-load mechanism may undermine C-13's requirement that the opening feel philosophical/motivational rather than procedural. |
| B | More vivid future moment in decline path | C-18 requires the decline path to name *when* the absence will be felt. R4 V-05 uses "before the next build" — specific but referring to a build phase. Axis B tests a more precise moment earlier in the workflow: "before you write the first line of your next spec" — the moment where inertia is chosen, not the moment where the build runs. Hypothesis: the spec-writing moment is where the decision is made; the build is where the consequence is felt. Naming the decision moment rather than the consequence moment may be more accurate and more vivid. Risk: "before you write the first line of your spec" presumes the user writes specs. Over-specificity can feel presumptuous. "Before the next build" may be the right level already. |
| C | Condensed preamble retaining C-17 | R4 V-05 preamble is 4-5 sentences. Axis C compresses to 2 sentences while retaining inertia-as-adversary (C-16) and the setup-endures argument (C-17). Tests whether temporal persistence survives compression or requires the fuller treatment to register as argument rather than slogan. Hypothesis: 2 sentences can carry the mechanism if the write→inherit→automatic chain is named economically. Risk: at 2 sentences, one or both of C-16 and C-17 may read as PARTIAL — present but not fully argued. |
| D | A + B: Explicit persistence + vivid future moment | Combine Axis A (explicit C-17 argument) with Axis B (specific future moment) in the R4 V-05 gate structure. Tests whether the two new criteria interact positively — whether a preamble that explains persistence makes the decline's future-moment reference feel more earned, because the user has been told exactly what they are giving up and when. |
| E | Full threading: A + B + persistence language in all exit gates | V-05 base with Axis A preamble, Axis B decline, and the temporal-persistence + future-moment language also threaded into GATE 1 (missing-file decline) and GATE 2 (already-configured affirmation). Every exit point speaks the same voice about what configuration does and when its absence is felt. Tests whether coherence across gates strengthens C-15 and C-17 further, or merely adds length without scoring gain. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+E)

Base behaviors in all variations (from R4 V-05): C-01 through C-16 are preserved.
Rubric in scope: `simulations/quest/rubrics/signal-setup-rubric-v5-2026-03-16.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)`
N_essential=5, N_recommended=3, N_aspirational=10
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 — Axis A: Explicit temporal persistence argument in preamble

**Variation axis**: Phrasing register — temporal persistence mechanism stated explicitly
**Hypothesis**: Replacing "Configure once. Fight inertia every time." with a 3-sentence
causal argument — write to CLAUDE.md → every session loads CLAUDE.md automatically →
the inertia question is present without you remembering — shifts C-17 from PARTIAL to PASS.
The user understands the stakes of the write (C-17 pass condition), not merely the stakes
of the problem.

---

```
You are running /signal-setup.

Every Signal workspace has one silent competitor: inertia — the choice to do nothing, to trust
the guess, to build without asking. Signal cannot challenge what your workspace context does not
name. This skill writes Signal into CLAUDE.md once. After that, every Claude Code session that
opens this workspace loads CLAUDE.md automatically — which means the inertia question is present
every time, without you having to remember to ask it. The write happens once. The reminder is
permanent.

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

**V-01 expected gains vs R4 V-05:**
- C-17: PASS — preamble now states the causal chain: "every Claude Code session that opens this
  workspace loads CLAUDE.md automatically — which means the inertia question is present every
  time, without you having to remember to ask it. The write happens once. The reminder is
  permanent." The setup-endures argument is explicit, not sloganed.
- C-18: PASS (unchanged from R4 V-05 — "before the next build" remains)
- All other criteria: unchanged

**Predicted composite score**: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = **100**

---

## V-02 — Axis B: Vivid future moment in decline path

**Variation axis**: Decline consequence — specificity of the future moment
**Hypothesis**: "Before the next build" names a phase. The decision to build without evidence
is made earlier — when the spec is being written or the ticket is being accepted. Anchoring
the decline consequence to the spec-writing moment ("before you write the first line of your
next spec") names the decision point, not the consequence point. Tests whether a more precise
future moment improves C-18 or introduces presumptuousness risk.

---

```
You are running /signal-setup.

Every Signal workspace has one silent competitor: inertia — the choice to do nothing, to trust
the guess, to build without asking. Signal cannot challenge what your workspace context does not
name. This is the one step that names it: a Signal section in your CLAUDE.md gives Claude a
persistent reminder to ask "why would teams do nothing instead?" before every feature, every
session. Configure once. Fight inertia every time.

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
> Inertia remains unnamed in this workspace. The next time a teammate asks "why are we building
> this instead of shipping what we have?" — before you write the first line of your spec — there
> will be no reminder in your context to ask that question first.
> Run /signal-setup when you are ready to change that.
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

**V-02 expected gains vs R4 V-05:**
- C-18: PASS — more precise future moment: "before you write the first line of your spec" —
  anchors the absence to the decision point (spec authorship) rather than the consequence
  point (the build). The user understands when the question will be missing, not merely that
  it will be.
- C-17: PARTIAL — preamble is unchanged from R4 V-05; "Configure once. Fight inertia every
  time." is still present as slogan rather than argument.
- All other criteria: unchanged.

**Predicted composite score**: (5/5 * 60) + (3/3 * 30) + (9/10 * 10) = **99**

**Risk note**: "before you write the first line of your spec" presumes a spec-writing workflow.
Teams that work from tickets or verbal briefs may find this less resonant. "Before the next
build" is more universal but less vivid. This trade-off is the design question this variation
puts on the table.

---

## V-03 — Axis C: Condensed preamble retaining C-17

**Variation axis**: Preamble compression — 2-sentence form carrying both C-16 and C-17
**Hypothesis**: V-01's preamble is 4 sentences. C-17 can be satisfied in 2 sentences if
the temporal persistence mechanism is stated economically: inertia is named as adversary
(C-16) AND the write→inherit→automatic chain is present (C-17). Tests whether compression
loses the argument or merely the explanation.

---

```
You are running /signal-setup.

Inertia is the feature team's silent default: do nothing, trust the guess, ship without asking.
This skill writes the counter-question into CLAUDE.md once — and from that point on, every
session that opens this workspace inherits it. You configure once. Claude asks it every time.

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

**V-03 expected gains vs R4 V-05:**
- C-17: PASS or PARTIAL (the argument: "every session that opens this workspace inherits it.
  You configure once. Claude asks it every time." — the mechanism is present but compressed.
  The chain write→inherit is stated; the *automatic* nature of the load is implied by "inherits
  it" rather than named explicitly as in V-01. A strict scorer may read this as PARTIAL.)
- C-16: PASS — "Inertia is the feature team's silent default" in the opening sentence names
  inertia as adversary.
- C-13: PASS — preamble is 2 sentences but motivational and present before any gate.
- C-18: PASS (unchanged) — "before the next build."
- All other criteria: unchanged.

**Predicted composite score (C-17 PASS)**: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = **100**
**Predicted composite score (C-17 PARTIAL)**: (5/5 * 60) + (3/3 * 30) + (9/10 * 10) = **99**

**Key question for scoring**: Does "every session that opens this workspace inherits it" satisfy
the pass condition "The 'setup endures' argument is present"? V-01 adds "loads CLAUDE.md
automatically" and "The write happens once. The reminder is permanent." — names the mechanism,
the once-ness, and the permanence explicitly. V-03 names only the once-ness and the inheritance.
The permanence and the automatic nature are implied but not stated.

---

## V-04 — Axes A + B: Explicit persistence + vivid future moment

**Variation axis**: Preamble mechanism explanation + specific future moment in decline
**Hypothesis**: V-01 (explicit persistence argument) and V-02 (vivid future moment in decline)
are independent design decisions that combine cleanly. V-01's preamble gives the full argument
for why the write matters (C-17 PASS); V-02's decline gives the full consequence at the most
vivid decision moment (C-18 maximum specificity). Neither change interacts with the other's
gate, so the combination should preserve all criteria from both single-axis runs.

---

```
You are running /signal-setup.

Every Signal workspace has one silent competitor: inertia — the choice to do nothing, to trust
the guess, to build without asking. Signal cannot challenge what your workspace context does not
name. This skill writes Signal into CLAUDE.md once. After that, every Claude Code session that
opens this workspace loads CLAUDE.md automatically — which means the inertia question is present
every time, without you having to remember to ask it. The write happens once. The reminder is
permanent.

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
> Inertia remains unnamed in this workspace. The next time a teammate asks "why are we building
> this instead of shipping what we have?" — before you write the first line of your spec — there
> will be no reminder in your context to ask that question first.
> Run /signal-setup when you are ready to change that.
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

**V-04 expected gains vs R4 V-05:**
- C-17: PASS — V-01's mechanism argument: "every Claude Code session that opens this workspace
  loads CLAUDE.md automatically — which means the inertia question is present every time,
  without you having to remember to ask it. The write happens once. The reminder is permanent."
- C-18: PASS — V-02's decision-point anchor: "before you write the first line of your spec."
- All other criteria: unchanged (PASS from R4 V-05).

**Predicted composite score**: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = **100**

---

## V-05 — Axes A + B + E: Explicit persistence + vivid moment + threading through all exit gates

**Variation axis**: All axes — explicit temporal persistence + vivid future moment + the
setup-endures language threaded into GATE 1 (missing-file decline) and GATE 2 (already-
configured affirmation) responses
**Hypothesis**: In V-01 through V-04, C-17 and C-18 are only present in the preamble and the
GATE 4 decline. GATE 1 (no-CLAUDE.md case) and GATE 2 (already-configured case) use language
from R4 V-05 that does not carry the temporal-persistence framing. Threading the same voice
through all exit points creates a coherent skill — one where the user hears the same argument
about what the configuration does and when its absence is felt regardless of which path they
take. Tests whether coherence across gates strengthens C-15 (GATE 2 affirmation) and C-17
further, at the cost of additional prompt length.

---

```
You are running /signal-setup.

Every Signal workspace has one silent competitor: inertia — the choice to do nothing, to trust
the guess, to build without asking. Signal cannot challenge what your workspace context does not
name. This skill writes Signal into CLAUDE.md once. After that, every Claude Code session that
opens this workspace loads CLAUDE.md automatically — the inertia question is present every time,
without you having to remember to ask it. The write happens once. The reminder is permanent.

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
> No CLAUDE.md found. Signal will create CLAUDE.md containing only the Signal section.
> Every future session that opens this workspace will load it automatically — the inertia
> question will be present from the next session forward. No existing content will be affected.

Show the preview (same content as GATE 3 preview below).
Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. The next time you open this workspace to start a feature — before
> you write the first line of a spec — the inertia question will not be in your context.
> It will not get asked unless you remember to ask it yourself.
> Run /signal-setup when you are ready to change that.
Stop here.

If Y: proceed to GATE 4 (WRITE) with create-new mode.

---

## GATE 2 — ALREADY CONFIGURED (edge case)

A Signal section already exists in CLAUDE.md.

Respond:
> Signal is already configured.
> Every session that opens this workspace loads CLAUDE.md and inherits the inertia question —
> automatically, without you having to remember. You configured this once; it has been working
> in every session since. Inertia already has a named opponent here. No changes needed.
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
> Inertia remains unnamed in this workspace. The next time you open a spec or start a feature —
> before you write the first line — there will be no reminder in your context to ask "why would
> teams do nothing instead?" That question will not be in Claude's context by default.
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

**V-05 expected gains vs R4 V-05:**
- C-17: PASS — explicit mechanism in preamble: "loads CLAUDE.md automatically... The write
  happens once. The reminder is permanent." GATE 2 also carries it: "Every session that opens
  this workspace loads CLAUDE.md and inherits the inertia question — automatically, without
  you having to remember. You configured this once; it has been working in every session since."
- C-18: PASS — GATE 4 decline: "before you write the first line." GATE 1 decline: "before
  you write the first line of a spec." Two gates, same specific future moment, same voice.
- C-15: PASS (strengthened over R4 V-05) — GATE 2 now explicitly names what the configuration
  has been doing: "it has been working in every session since."
- All other criteria: unchanged (PASS from R4 V-05).

**Predicted composite score**: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = **100**

**Risk**: V-05 is the longest variation in this round. GATE 1 and GATE 2 both carry more
language than in R4 V-05. GATE 2's exit response (already-configured) now runs 4 sentences
where R4 had 3 — the risk of feeling verbose on the skip path is real. The additional GATE 1
decline introduces a specific future moment even on the no-CLAUDE.md path, which is coherent
with the skill's voice but is a behavioral surface absent from V-01 through V-04. If a
reviewer finds this surface introduces an inconsistency (GATE 1 decline is more vivid than
GATE 1 confirmation), it could interact with C-10 (missing CLAUDE.md handled gracefully).

---

## Summary of predicted scores

| Variation | Axis | C-17 | C-18 | Aspirational | Score |
|-----------|------|------|------|--------------|-------|
| R4 V-05 (baseline) | A+B+C+D+E (v4 axes) | PARTIAL | PASS | 9/10 | 99 |
| V-01 | A: explicit persistence | PASS | PASS | 10/10 | **100** |
| V-02 | B: vivid future moment | PARTIAL | PASS | 9/10 | 99 |
| V-03 | C: condensed preamble | PASS or PARTIAL | PASS | 9-10/10 | 99-100 |
| V-04 | A+B: explicit + vivid | PASS | PASS | 10/10 | **100** |
| V-05 | A+B+E: full threading | PASS | PASS | 10/10 | **100** |

**Champion candidates**: V-01, V-04, V-05 all reach predicted 100.

**Design recommendation**: V-04 is the minimum change to achieve 100 — V-01's preamble plus
V-02's decline, no structural changes beyond R4 V-05. V-01 is simpler still (only preamble
changes; C-18 relies on R4 V-05's "before the next build" rather than V-02's more specific
moment). V-05 adds coherence across all exit gates at the cost of length.

The choice between V-01 and V-04 turns on whether the rubric treats V-02's "before you write
the first line of your spec" as a stronger C-18 PASS than V-01's "before the next build."
Both phrases name a specific future moment; V-02's is earlier in the workflow and names the
decision point. The rubric does not specify minimum specificity for C-18 PASS — it requires
only "a specific future moment where the absence will be felt." Both satisfy the criterion.
V-04 is preferred as champion if specificity is valued; V-01 if minimalism is preferred.
