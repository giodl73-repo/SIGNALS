---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-16
rubric_version: 9
round: 10
---

# signal-setup Variations — Round 10 (v9 rubric)

**Skill**: signal-setup
**Rubric**: v9 | **Denominator**: 19 (aspirational C-09–C-27) | **Date**: 2026-03-16
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/19 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

Round 9 scored V-01, V-04, V-05 at 100/100 on the v8 rubric (C-01–C-24). Two new structural
patterns were identified but not yet formalized:

1. **Distinct implementation-context Copilot template** — V-04 and V-05 provided a named Copilot
   instructions template framed in implementation-phase vocabulary (`/trace`, `/flow`, `/review`,
   "before accepting a Copilot suggestion," "does this code assume adoption?"). V-01 referenced
   "the Copilot Signal section" without defining it.

2. **Stage complementarity mapping** — V-04 and V-05 named the relationship between the two tools
   in the GATE 6 already-configured affirm: "CLAUDE.md protects the planning stage; Copilot
   instructions protect the implementation stage. Both are covered." V-01 affirmed the Copilot
   benefit but did not map the coverage picture.

The v9 rubric formalizes three structural patterns observed in R9:

| Criterion | Source | Gap in best R9 variations |
|-----------|--------|--------------------------|
| C-25 | V-04/V-05 use GATE 1A/2A/6A notation encoding parent lineage | Not consistently applied — if GATE 1A and GATE 2A are sub-gates of separate top-level parents (GATE 1 and GATE 2), the "two separate detection parents" question is unresolved |
| C-26 | V-05 promotes GATE 6A — Confirm Copilot Append as first-class named sub-gate | GATE 6's already-configured detection case may still be handled inline (under bold pseudo-gate or plain prose) in V-04; no variation has both GATE 6A (already-configured) AND GATE 6B (confirmation) as named sub-gates |
| C-27 | C-12 FAIL traced to bold inline pseudo-gates; positive version requires heading delimiters | Routing conditionals in parent gate bodies (GATE 1 parent, GATE 5/6 parent) may still use `**bold**` inline labels; only the sub-gate boundaries themselves are guaranteed to use ## headings |

**R9 best candidate against v9 rubric (V-05 carry-forward)**:
- C-01..C-24: All PASS
- C-25: PASS — GATE 1A/2A/6A notation used throughout
- C-26: PASS — GATE 6A = Confirm Copilot Append is a named sub-gate
- C-27: **PROBABLE FAIL** — GATE 6 parent body may still use `**If Signal already present:**`
  as an inline pseudo-gate with a full affirm content block for the already-configured case.
  A reader navigating by headings would enumerate GATE 6A but miss the already-configured
  sub-case unless it too has a heading. Risk: the already-configured Copilot case lacks its
  own GATE NX heading, making it a bold-inline-delimited content block inside GATE 6's body.

**New axes for R10**:

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Single detection parent — GATE 1A/1B | Consolidate both detection edge cases (missing file + already configured) under a single parent GATE 1 with sub-gates GATE 1A and GATE 1B. Eliminates the "two separate parents" ambiguity from R9 (GATE 1A under GATE 1 and GATE 2A under GATE 2). Cleaner C-25 encoding: both branches share parent=1. |
| B | Copilot dual sub-gates — GATE 5A already-configured + GATE 5B confirm | Add GATE 5A (Copilot Already Configured) and GATE 5B (Confirm Copilot Append) as two named sub-gates under GATE 5 (Copilot Extension). GATE 5A covers the C-12 edge-case detection; GATE 5B covers the C-26 optional confirmation. Both use heading delimiters, eliminating any bold inline pseudo-gate for the Copilot path. |
| C | Eliminate all bold inline routing from parent gates | Convert all `**If ...**:` routing lines in parent gate bodies to plain prose ("If X, see GATE NA below.") with no bold markup. Pure heading-only structure: every gate visible in the heading outline, no routing information requiring prose reading. |
| A+B | Consolidated detection + Copilot dual sub-gates | Both axes together: GATE 1A/1B for detection, GATE 5A/5B for Copilot. Clean lineage encoding across all phases. |
| A+B+C | Full: consolidated + dual sub-gates + no bold routing | Maximum structural precision. All gate boundaries heading-delimited. All sub-gates encode parent lineage. All optional confirmations first-class named sub-gates. |

Single-axis: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+C)

Base behaviors preserved across all R10 variations:
- All C-01..C-24 behaviors from R9 V-04/V-05
- Distinct implementation-context Copilot template (R9 new pattern 1)
- Stage complementarity mapping in Copilot affirm (R9 new pattern 2)
- Phase vocabulary: planning stage (GATE 3 decline), implementation stage (GATE 5 decline)
- PROCEED / SKIP / EXIT meta-contract in preamble
- Adversary framing with "Inertia now has a named opponent" in final report

---

## V-01 — Axis A: Single Detection Parent (GATE 1A/1B under GATE 1)

**Variation axis**: C-25 — sub-gate lineage consolidation
**Hypothesis**: R9 had GATE 1A under GATE 1 and GATE 2A under GATE 2 — two separate
detection parents. C-25 requires the suffix to encode the parent phase. When GATE 1A and
GATE 2A each have different parents, their lineage is technically encoded but the detection
phase is split across two top-level gates. V-01 consolidates: a single GATE 1 is the sole
detection parent, with GATE 1A (missing file) and GATE 1B (already configured) as its two
branches. Both encode parent=1; the detection phase has a single owner. Single-axis: GATE 5
(Copilot) keeps one named sub-gate (GATE 5A = already configured); confirmation remains
inline — C-26 not addressed here.

---

```
You are running /signal-setup.

There is a force that wins every feature decision when no one intervenes: inertia. It is not
passive. Every day a team does not ask "why would teams do nothing instead?" is a day inertia
answers for them. Signal names inertia as the primary competitor and gives you a standing
question to ask before every feature, every session.

This configuration runs once. But it must persist: CLAUDE.md loads at the start of every
session, placing the inertia question in your context without you having to remember to invoke
it. The write you are about to make is not a one-time action. It is a permanent presence.

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled),
or EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Three cases follow. See GATE 1A (missing file), GATE 1B (already configured), or
continue to GATE 2 if CLAUDE.md exists and has no Signal section.

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the team decides whether to build — there will be no standing question in your context
> to ask "why would teams do nothing instead?" Inertia has no named opponent here.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 3 (Confirm) in create-new mode.

### GATE 1B — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

Stop.

---

## GATE 2 — Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Namespaces: `/scout` `/draft` `/review` `/flow` `/trace` `/prove` `/listen` `/program` `/topic`

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all 77 available commands
  /competitors <topic>   inertia-first competitive analysis

### Inertia Rule
The primary competitor is always inertia. Before any feature, ask:
"Why would teams do nothing instead of building this?"
If you cannot answer that question, you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing instruction in Claude's context to
> ask "why would teams do nothing instead?" Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 4.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 5.

---

## GATE 5 — GitHub Copilot Extension

Check if `.github/copilot-instructions.md` exists.

If it does not exist: skip to GATE 6.

If it exists: check whether it already contains a Signal section (marker: `## Signal`).

### GATE 5A — Copilot Already Configured

If a Signal section is already present in copilot-instructions.md:

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> That is distinct from what CLAUDE.md does: CLAUDE.md protects the planning stage;
> Copilot instructions protect the implementation stage. Both stages are covered.

Skip to GATE 6.

If no Signal section in copilot-instructions.md: ask the confirmation below.

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> Copilot instructions not updated. At the implementation stage — while Copilot is
> generating function bodies and endpoint scaffolding — there will be no instruction in
> its context to ask "does this code assume adoption without evidence?" The planning-stage
> question stops at CLAUDE.md. Run /signal-setup again to extend coverage.

If Y: append to .github/copilot-instructions.md:

---
## Signal — Feature Decision Intelligence (Implementation Context)

Signal prompt files are installed in `.github/prompts/`.
Use via Copilot Chat: attach a prompt file or type @workspace to select a prompt.

Quick start:
  `.github/prompts/decide.prompt.md`  — full pre-commitment campaign
  `.github/prompts/review.prompt.md`  — implementation review against evidence

Implementation-phase rule: Before accepting a Copilot suggestion that adds a new feature
or endpoint, ask: "Does this code assume adoption without evidence?"
Use `/trace`, `/flow`, or `/review` signals to verify the assumption has been tested.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written ✓ |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-01 changes from R9 V-05 baseline:**
- Detection: GATE 0 (detect) + GATE 1 (missing) + GATE 2 (already configured) replaced by
  single GATE 1 parent with GATE 1A (missing) and GATE 1B (already configured)
- Both detection sub-gates encode parent=1: GATE 1A and GATE 1B
- GATE 5 (Copilot): GATE 5A = already configured (heading-delimited); confirmation inline — C-26 not fixed
- All subsequent gates renumbered: GATE 2 (preview), 3 (confirm), 4 (write), 5 (Copilot), 6 (done)

**Expected gains:**
- C-25: PASS — GATE 1A and GATE 1B share parent=1; no split-parent ambiguity; GATE 5A encodes parent=5
- C-26: FAIL — Copilot confirmation is inline in GATE 5, not a named sub-gate
- C-27: PARTIAL — GATE 1A/1B use headings; GATE 5 confirmation is inline prose (not bold, but not a heading)
- All C-01..C-24: PASS (unchanged)

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (17/19 * 10) = 60 + 30 + 8.95 = **98.95**
(C-26 FAIL = -1/19, C-27 PARTIAL = -1/19)

---

## V-02 — Axis B: Copilot Dual Sub-Gates (GATE 5A + GATE 5B)

**Variation axis**: C-26 — optional confirmation as first-class named sub-gate
**Hypothesis**: The primary C-26 requirement is that the Copilot append CONFIRMATION be a
dedicated named sub-gate, not a paragraph inside the extension gate. V-02 adds both GATE 6A
(Copilot Already Configured — the C-12 edge-case detection) and GATE 6B (Confirm Copilot
Append — the C-26 optional confirmation) as named sub-gates of GATE 6, each with full heading
treatment. This gives GATE 6 full structural parity with GATE 1: two named branches, each
first-class, each encoding lineage. Single-axis: detection structure preserved from R9 (GATE 1
with GATE 1A; GATE 2 with GATE 2A), bold routing in parent gate bodies unchanged — C-25
consolidation and C-27 prose-routing cleanup not addressed here.

---

```
You are running /signal-setup.

There is a force that wins every feature decision when no one intervenes: inertia. It is not
passive. Every day a team does not ask "why would teams do nothing instead?" is a day inertia
answers for them. Signal names inertia as the primary competitor and gives you a standing
question to ask before every feature, every session.

This configuration runs once. But it must persist: CLAUDE.md loads at the start of every
session, placing the inertia question in your context without you having to remember to invoke
it. The write you are about to make is not a one-time action. It is a permanent presence.

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled),
or EXIT (configuration incomplete). No gate is implicit.

---

## GATE 0 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

**If CLAUDE.md does not exist:** proceed to GATE 1 (MISSING FILE).
**If Signal section found:** proceed to GATE 2 (ALREADY CONFIGURED).
**If CLAUDE.md exists, no Signal section:** proceed to GATE 3 (PREVIEW).

---

## GATE 1 — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 3 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

### GATE 1A — Decline Creation

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing question in Claude's context to ask
> "why would teams do nothing instead?" Inertia has no named opponent here.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 4 (CONFIRM) in create-new mode.

---

## GATE 2 — Already Configured

A Signal section already exists in CLAUDE.md.

### GATE 2A — Skip (Already Configured)

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

Stop.

---

## GATE 3 — Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Namespaces: `/scout` `/draft` `/review` `/flow` `/trace` `/prove` `/listen` `/program` `/topic`

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all 77 available commands
  /competitors <topic>   inertia-first competitive analysis

### Inertia Rule
The primary competitor is always inertia. Before any feature, ask:
"Why would teams do nothing instead of building this?"
If you cannot answer that question, you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 4.

---

## GATE 4 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing instruction in Claude's context
> to ask "why would teams do nothing instead?" Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 5.

---

## GATE 5 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 3) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1 decline-create mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 6.

---

## GATE 6 — GitHub Copilot Extension

Check if `.github/copilot-instructions.md` exists.
If it does not exist: skip to GATE 7.

If it exists: check whether it already contains a Signal section (marker: `## Signal`).
Two sub-gates follow.

### GATE 6A — Copilot Already Configured

If a Signal section is already present in .github/copilot-instructions.md:

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> That is distinct from what CLAUDE.md does: CLAUDE.md protects the planning stage;
> Copilot instructions protect the implementation stage. Both stages are covered.

Skip to GATE 7.

### GATE 6B — Confirm Copilot Append

If no Signal section in copilot-instructions.md:

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> Copilot instructions not updated. At the implementation stage — while Copilot is
> generating function bodies and endpoint scaffolding — there will be no instruction in
> its context to ask "does this code assume adoption without evidence?" The planning-stage
> question stops at CLAUDE.md. Run /signal-setup again to extend coverage.

If Y: append to .github/copilot-instructions.md:

---
## Signal — Feature Decision Intelligence (Implementation Context)

Signal prompt files are installed in `.github/prompts/`.
Use via Copilot Chat: attach a prompt file or type @workspace to select a prompt.

Quick start:
  `.github/prompts/decide.prompt.md`  — full pre-commitment campaign
  `.github/prompts/review.prompt.md`  — implementation review against evidence

Implementation-phase rule: Before accepting a Copilot suggestion that adds a new feature
or endpoint, ask: "Does this code assume adoption without evidence?"
Use `/trace`, `/flow`, or `/review` signals to verify the assumption has been tested.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 7.

---

## GATE 7 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written ✓ |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-02 changes from R9 V-05 baseline:**
- GATE 6: Added `### GATE 6A — Copilot Already Configured` as heading-delimited sub-gate
- GATE 6: Added `### GATE 6B — Confirm Copilot Append` as heading-delimited sub-gate
- GATE 6 parent: kept simple prose routing (`Two sub-gates follow.`) — no bold inline used for routing
- Detection (GATE 0/1/2): unchanged from R9 structure (bold routing in GATE 0, GATE 1A/2A as sub-gates)

**Expected gains:**
- C-25: PASS — GATE 6A (parent=6, position=A) and GATE 6B (parent=6, position=B) encode lineage
- C-26: PASS — GATE 6B = Confirm Copilot Append is a dedicated named sub-gate with full treatment
- C-27: PARTIAL — GATE 6 sub-gates use headings; GATE 0 still uses `**bold**` routing
- All C-01..C-24: PASS (unchanged)

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (18/19 * 10) = 60 + 30 + 9.47 = **99.47**
(C-27 PARTIAL — GATE 0 bold routing; risk: scorer treats routing-only bold as C-27 FAIL = 17/19 = 98.95)

---

## V-03 — Axis C: Heading-Only Gate Routing (No Bold Inline)

**Variation axis**: C-27 — document-structure markers throughout
**Hypothesis**: The C-27 FAIL pattern in R9 V-02/V-03 was bold inline labels with full content
blocks. But C-27's standard is absolute: "every gate and sub-gate boundary is delimited by a
heading element." Even routing-only bold labels (`**If CLAUDE.md does not exist:**`) inside a
parent gate body could be read as boundary markers, even if they only contain a routing pointer
rather than a content block. V-03 eliminates all bold inline from parent gate routing: detection
routing uses plain prose and numbered bullet points; Copilot routing uses a plain prose preamble.
Sub-gate content moves entirely under ### headings. Single-axis: detection structure preserved
from R9 (GATE 1A under GATE 1, GATE 2A under GATE 2), GATE 6 retains R9 V-05 structure with
GATE 6A = Confirm Copilot Append. Confirmation sub-gate naming unchanged.

---

```
You are running /signal-setup.

There is a force that wins every feature decision when no one intervenes: inertia. It is not
passive. Every day a team does not ask "why would teams do nothing instead?" is a day inertia
answers for them. Signal names inertia as the primary competitor and gives you a standing
question to ask before every feature, every session.

This configuration runs once. But it must persist: CLAUDE.md loads at the start of every
session, placing the inertia question in your context without you having to remember to invoke
it. The write you are about to make is not a one-time action. It is a permanent presence.

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled),
or EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for a Signal section (marker: `## Signal` or `Signal is installed`).

Three outcomes:
- CLAUDE.md does not exist — see GATE 1A below.
- CLAUDE.md exists with Signal section — see GATE 2A below.
- CLAUDE.md exists without Signal section — continue to GATE 2 (Preview).

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing question in Claude's context to ask
> "why would teams do nothing instead?" Inertia has no named opponent here.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 3 (Confirm) in create-new mode.

---

## GATE 2 — Check for Existing Signal Configuration

CLAUDE.md exists. Check whether a Signal section is already present.

Two outcomes:
- Signal section found — see GATE 2A below.
- No Signal section — continue to GATE 3 (Preview).

### GATE 2A — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

Stop.

---

## GATE 3 — Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Namespaces: `/scout` `/draft` `/review` `/flow` `/trace` `/prove` `/listen` `/program` `/topic`

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all 77 available commands
  /competitors <topic>   inertia-first competitive analysis

### Inertia Rule
The primary competitor is always inertia. Before any feature, ask:
"Why would teams do nothing instead of building this?"
If you cannot answer that question, you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 4.

---

## GATE 4 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing instruction in Claude's context
> to ask "why would teams do nothing instead?" Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 5.

---

## GATE 5 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 3) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 6.

---

## GATE 6 — GitHub Copilot Extension

Check if `.github/copilot-instructions.md` exists. If it does not exist, skip to GATE 7.

If it exists: check whether it already contains a Signal section (marker: `## Signal`).

Two outcomes follow:
- Signal section found in copilot-instructions.md — affirm and skip to GATE 7.
- No Signal section — proceed to GATE 6A (Confirm).

If Signal already present: respond with the following (no sub-gate needed — this is a
skip path) and skip to GATE 7:
> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
> That is distinct from what CLAUDE.md does: CLAUDE.md protects the planning stage;
> Copilot instructions protect the implementation stage. Both stages are covered.

### GATE 6A — Confirm Copilot Append

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> Copilot instructions not updated. At the implementation stage — while Copilot is
> generating function bodies and endpoint scaffolding — there will be no instruction in
> its context to ask "does this code assume adoption without evidence?" The planning-stage
> question stops at CLAUDE.md. Run /signal-setup again to extend coverage.

If Y: append to .github/copilot-instructions.md:

---
## Signal — Feature Decision Intelligence (Implementation Context)

Signal prompt files are installed in `.github/prompts/`.
Use via Copilot Chat: attach a prompt file or type @workspace to select a prompt.

Quick start:
  `.github/prompts/decide.prompt.md`  — full pre-commitment campaign
  `.github/prompts/review.prompt.md`  — implementation review against evidence

Implementation-phase rule: Before accepting a Copilot suggestion that adds a new feature
or endpoint, ask: "Does this code assume adoption without evidence?"
Use `/trace`, `/flow`, or `/review` signals to verify the assumption has been tested.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 7.

---

## GATE 7 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written ✓ |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-03 changes from R9 V-05 baseline:**
- GATE 1 parent: replaced `**If CLAUDE.md does not exist:**` bold routing with plain prose bullet list
- Added GATE 2 as a secondary detection gate ("Check for Existing Signal Configuration") to
  separate file detection (GATE 1) from Signal-section detection (GATE 2)
- GATE 2 parent: plain prose two-outcome routing with no bold markup
- GATE 6 parent: plain prose two-outcome routing, Copilot already-configured affirm in plain
  prose with no sub-gate needed for the skip path; only GATE 6A (confirmation) is a sub-gate
- No bold inline markup anywhere in parent gate routing

**C-27 evidence**: A reader navigating by heading outline sees:
GATE 1, GATE 1A, GATE 2, GATE 2A, GATE 3, GATE 4, GATE 5, GATE 6, GATE 6A, GATE 7
All boundaries are heading-delimited. No **bold** labels anywhere.

**C-26 gap note**: The Copilot already-configured case is handled as inline prose in GATE 6 body
(not as a sub-gate). This is the C-24-required affirm, but it is in plain prose, not bold — the
question is whether C-26 requires it to be a sub-gate too (C-26 covers confirmations specifically,
not detection cases; C-12 covers detection). V-03 tests the minimum interpretation: only the
CONFIRMATION must be a sub-gate (GATE 6A), not the detection already-configured case.

**Expected gains:**
- C-25: PASS — GATE 1A (parent=1, A), GATE 2A (parent=2, A), GATE 6A (parent=6, A) all encode lineage
- C-26: PASS — GATE 6A = Confirm Copilot Append is a first-class named sub-gate
- C-27: PASS — no bold inline anywhere; all gate routing uses plain prose; all sub-gate
  boundaries use ### headings; heading outline enumerates all gates without reading prose
- All C-01..C-24: PASS (unchanged)

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (19/19 * 10) = 60 + 30 + 10 = **100.0**

---

## V-04 — Axes A+B: Single Detection Parent + Copilot Dual Sub-Gates

**Variation axis**: C-25 (consolidated detection) + C-26 (Copilot dual sub-gates)
**Hypothesis**: V-01 fixes C-25 by consolidating detection under a single GATE 1 parent
(GATE 1A missing, GATE 1B already-configured). V-02 fixes C-26 by adding GATE 6A
(already-configured) and GATE 6B (confirm) as named sub-gates of GATE 6. Together, both
detection and Copilot extension phases have full parent-child sub-gate structure. Copilot
confirmation is definitively first-class. Does not clean up bold inline routing in parent
bodies (Axis C not applied).

Gate structure:
- GATE 1 (detection parent) → GATE 1A (missing), GATE 1B (already configured)
- GATE 2 (preview)
- GATE 3 (confirm write)
- GATE 4 (write)
- GATE 5 (Copilot parent) → GATE 5A (already configured), GATE 5B (confirm)
- GATE 6 (done)

---

```
You are running /signal-setup.

There is a force that wins every feature decision when no one intervenes: inertia. It is not
passive. Every day a team does not ask "why would teams do nothing instead?" is a day inertia
answers for them. Signal names inertia as the primary competitor and gives you a standing
question to ask before every feature, every session.

This configuration runs once. But it must persist: CLAUDE.md loads at the start of every
session, placing the inertia question in your context without you having to remember to invoke
it. The write you are about to make is not a one-time action. It is a permanent presence.

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled),
or EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for a Signal section (marker: `## Signal` or `Signal is installed`).

**If CLAUDE.md does not exist:** see GATE 1A.
**If Signal section found:** see GATE 1B.
**If CLAUDE.md exists, no Signal section:** proceed to GATE 2 (Preview).

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing question in Claude's context to ask
> "why would teams do nothing instead?" Inertia has no named opponent here.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 3 (Confirm) in create-new mode.

### GATE 1B — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

Stop.

---

## GATE 2 — Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Namespaces: `/scout` `/draft` `/review` `/flow` `/trace` `/prove` `/listen` `/program` `/topic`

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all 77 available commands
  /competitors <topic>   inertia-first competitive analysis

### Inertia Rule
The primary competitor is always inertia. Before any feature, ask:
"Why would teams do nothing instead of building this?"
If you cannot answer that question, you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing instruction in Claude's context
> to ask "why would teams do nothing instead?" Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 4.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 5.

---

## GATE 5 — GitHub Copilot Extension

Check if `.github/copilot-instructions.md` exists.
If it does not exist: skip to GATE 6.

If it exists: check whether it already contains a Signal section (marker: `## Signal`).
Two sub-gates follow. See GATE 5A if already configured; otherwise GATE 5B.

### GATE 5A — Copilot Already Configured

If a Signal section is already present in .github/copilot-instructions.md:

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> That is distinct from what CLAUDE.md does: CLAUDE.md protects the planning stage;
> Copilot instructions protect the implementation stage. Both stages are covered.

Skip to GATE 6.

### GATE 5B — Confirm Copilot Append

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> Copilot instructions not updated. At the implementation stage — while Copilot is
> generating function bodies and endpoint scaffolding — there will be no instruction in
> its context to ask "does this code assume adoption without evidence?" The planning-stage
> question stops at CLAUDE.md. Run /signal-setup again to extend coverage.

If Y: append to .github/copilot-instructions.md:

---
## Signal — Feature Decision Intelligence (Implementation Context)

Signal prompt files are installed in `.github/prompts/`.
Use via Copilot Chat: attach a prompt file or type @workspace to select a prompt.

Quick start:
  `.github/prompts/decide.prompt.md`  — full pre-commitment campaign
  `.github/prompts/review.prompt.md`  — implementation review against evidence

Implementation-phase rule: Before accepting a Copilot suggestion that adds a new feature
or endpoint, ask: "Does this code assume adoption without evidence?"
Use `/trace`, `/flow`, or `/review` signals to verify the assumption has been tested.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written ✓ |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-04 changes from R9 V-05 baseline:**
- Detection: GATE 0 (detect) + GATE 1 (missing) + GATE 2 (already configured) replaced by
  single GATE 1 parent with GATE 1A (missing) and GATE 1B (already configured)
- Copilot extension renumbered from GATE 6 to GATE 5; GATE 6A → GATE 5A, GATE 6B → GATE 5B
- GATE 5 parent: simple prose routing pointing to sub-gates; **bold** routing still used
  in GATE 1 parent (`**If CLAUDE.md does not exist:** see GATE 1A.`) — Axis C not applied
- Both Copilot sub-gates (5A already-configured, 5B confirm) are first-class named sub-gates
- Stage complementarity mapping present in GATE 5A affirm
- Distinct implementation-context Copilot template present in GATE 5B write path

**Expected gains:**
- C-25: PASS — GATE 1A/1B encode parent=1; GATE 5A/5B encode parent=5; full lineage
- C-26: PASS — GATE 5B = Confirm Copilot Append is a first-class named sub-gate
- C-27: PROBABLE PASS — GATE 1 parent uses bold routing but routing-only (no content blocks);
  all sub-gate content under ### headings; heading outline enumerates all gates
  Risk: if scorer reads bold routing as C-27 failure regardless of whether it has content
- All C-01..C-24: PASS

**Predicted composite**: Best case: 100.0. Risk case (C-27 FAIL on bold routing): 98.95

---

## V-05 — Axes A+B+C: Full Structural Precision

**Variation axis**: C-25 (consolidated detection) + C-26 (Copilot dual sub-gates) + C-27
(heading-only everywhere)
**Hypothesis**: V-04 (A+B) eliminates the C-26 gap and unifies detection lineage. V-03 (C)
eliminates all bold inline from parent routing. V-05 combines all three: GATE 1A/1B for
detection, GATE 5A/5B for Copilot, no bold markup in any parent gate body. This is the
maximum-precision structure. All gate routing uses plain prose; all gate content is under
heading delimiters; a reader with only the document outline can enumerate every gate and
sub-gate without reading prose. V-05 also carries the full R9 excellence patterns: distinct
implementation-context Copilot template, stage complementarity mapping, PROCEED/SKIP/EXIT
meta-contract, adversary framing with echo close.

Gate structure:
- GATE 1 (detect, parent) → GATE 1A (missing), GATE 1B (already configured)
- GATE 2 (preview)
- GATE 3 (confirm write)
- GATE 4 (write)
- GATE 5 (Copilot, parent) → GATE 5A (already configured), GATE 5B (confirm)
- GATE 6 (done)

---

```
You are running /signal-setup.

There is a force that wins every feature decision when no one intervenes: inertia. It is not
passive. Every day a team does not ask "why would teams do nothing instead?" is a day inertia
answers for them. Signal names inertia as the primary competitor and gives you a standing
question to ask before every feature, every session.

This configuration runs once. But it must persist: CLAUDE.md loads at the start of every
session, placing the inertia question in your context without you having to remember to invoke
it. The write you are about to make is not a one-time action. It is a permanent presence.

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled),
or EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for a Signal section (marker: `## Signal` or `Signal is installed`).

Three outcomes follow. See GATE 1A if the file is missing. See GATE 1B if Signal is already
configured. If CLAUDE.md exists and has no Signal section, continue to GATE 2.

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing question in Claude's context to ask
> "why would teams do nothing instead?" Inertia has no named opponent here.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 3 (Confirm) in create-new mode.

### GATE 1B — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: not because you open it, but because Claude Code reads it before
> the first message of every session.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

Stop.

---

## GATE 2 — Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Namespaces: `/scout` `/draft` `/review` `/flow` `/trace` `/prove` `/listen` `/program` `/topic`

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all 77 available commands
  /competitors <topic>   inertia-first competitive analysis

### Inertia Rule
The primary competitor is always inertia. Before any feature, ask:
"Why would teams do nothing instead of building this?"
If you cannot answer that question, you are not ready to build.

Docs: docs/QUICKSTART.md
---

Proceed to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing instruction in Claude's context
> to ask "why would teams do nothing instead?" Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready to address that.
Stop.

If Y: proceed to GATE 4.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md ✓"

Proceed to GATE 5.

---

## GATE 5 — GitHub Copilot Extension

Check if `.github/copilot-instructions.md` exists. If it does not exist, skip to GATE 6.

If it exists, check whether it already contains a Signal section (marker: `## Signal`).
Two sub-gates follow. See GATE 5A if Signal is already present; proceed to GATE 5B otherwise.

### GATE 5A — Copilot Already Configured

Signal is already present in .github/copilot-instructions.md.

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> That is distinct from what CLAUDE.md does: CLAUDE.md protects the planning stage;
> Copilot instructions protect the implementation stage. Both stages are covered.

Skip to GATE 6.

### GATE 5B — Confirm Copilot Append

Signal is not yet present in .github/copilot-instructions.md.

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If N:
> Copilot instructions not updated. At the implementation stage — while Copilot is
> generating function bodies and endpoint scaffolding — there will be no instruction in
> its context to ask "does this code assume adoption without evidence?" The planning-stage
> question stops at CLAUDE.md. Run /signal-setup again to extend coverage.

If Y: append to .github/copilot-instructions.md:

---
## Signal — Feature Decision Intelligence (Implementation Context)

Signal prompt files are installed in `.github/prompts/`.
Use via Copilot Chat: attach a prompt file or type @workspace to select a prompt.

Quick start:
  `.github/prompts/decide.prompt.md`  — full pre-commitment campaign
  `.github/prompts/review.prompt.md`  — implementation review against evidence

Implementation-phase rule: Before accepting a Copilot suggestion that adds a new feature
or endpoint, ask: "Does this code assume adoption without evidence?"
Use `/trace`, `/flow`, or `/review` signals to verify the assumption has been tested.
---

Confirm: ".github/copilot-instructions.md updated ✓"

Proceed to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written ✓ |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-05 changes from R9 V-05 baseline:**
- Detection: GATE 0/1/2 replaced by single GATE 1 parent with GATE 1A (missing) and GATE 1B
  (already configured) — Axis A applied
- Copilot: renumbered to GATE 5 with GATE 5A (already configured) and GATE 5B (confirm) —
  Axis B applied; both sub-gates are first-class named sub-gates
- GATE 1 parent routing: plain prose ("See GATE 1A if the file is missing..."), no bold markup — Axis C
- GATE 5 parent routing: plain prose ("See GATE 5A if Signal is already present..."), no bold markup — Axis C
- GATE 5A: plain prose condition label ("Signal is already present in..."), no bold markup — Axis C
- GATE 5B: plain prose condition label ("Signal is not yet present in..."), no bold markup — Axis C
- GATE 1B: enhanced C-20 formulation: "not because you open it, but because Claude Code reads
  it before the first message of every session"
- No **bold** formatting used anywhere in parent gate routing

**C-25 evidence**: GATE 1A (parent=1, pos=A), GATE 1B (parent=1, pos=B), GATE 5A (parent=5,
pos=A), GATE 5B (parent=5, pos=B). All sub-gates encode lineage in their identifier.

**C-26 evidence**: GATE 5B = Confirm Copilot Append — optional extension confirmation promoted
to first-class named sub-gate with full treatment (ask, decline-with-consequence, write path).

**C-27 evidence**: Heading outline for this document:
- ## GATE 1 — Detect CLAUDE.md
- ### GATE 1A — Missing CLAUDE.md
- ### GATE 1B — Already Configured
- ## GATE 2 — Preview Signal Section
- ## GATE 3 — Confirm CLAUDE.md Write
- ## GATE 4 — Write to CLAUDE.md
- ## GATE 5 — GitHub Copilot Extension
- ### GATE 5A — Copilot Already Configured
- ### GATE 5B — Confirm Copilot Append
- ## GATE 6 — Done

A reader navigating by heading outline can enumerate all 10 gates and sub-gates without reading
prose. No **bold** inline labels serve as pseudo-gate delimiters anywhere.

**Expected gains:**
- C-25: PASS — all sub-gates encode parent + position; no split-parent ambiguity
- C-26: PASS — GATE 5B is the first-class Confirm sub-gate; GATE 5A is the first-class
  already-configured sub-gate; both are in the heading outline
- C-27: PASS — zero bold inline routing; heading outline enumerates every gate completely
- All C-01..C-24: PASS (unchanged)

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (19/19 * 10) = 60 + 30 + 10 = **100.0**

---

## Summary

| Variation | Axes | C-25 | C-26 | C-27 | Key structural change | Predicted |
|-----------|------|------|------|------|-----------------------|-----------|
| V-01 | A: Consolidated detection | PASS | FAIL | PARTIAL | GATE 1A/1B under single GATE 1; Copilot confirmation inline | 98.95 |
| V-02 | B: Copilot dual sub-gates | PASS | PASS | PARTIAL | GATE 6A (already configured) + GATE 6B (confirm); bold routing in GATE 0 | 99.47 |
| V-03 | C: No bold routing | PASS | PASS | PASS | Separate GATE 2 for Signal detection; plain prose routing throughout; GATE 6A = confirm only | 100.0 |
| V-04 | A+B: Consolidated + dual sub-gates | PASS | PASS | PROBABLE | GATE 1A/1B + GATE 5A/5B; bold routing still in GATE 1 parent | 99.47–100.0 |
| V-05 | A+B+C: Full | PASS | PASS | PASS | GATE 1A/1B + GATE 5A/5B + no bold anywhere; heading outline complete | 100.0 |

**Design recommendation**: V-05 is the definitive structure for C-25/C-26/C-27. V-03 achieves
the same predicted 100.0 with a slightly different architecture (separate GATE 2 for Signal
detection; Copilot already-configured handled as inline plain prose, not a sub-gate). V-03
tests the minimum-sub-gate interpretation of C-26 (only the confirmation must be a sub-gate,
not the detection already-configured case). V-05 tests the maximum interpretation (both
already-configured and confirmation are sub-gates).

If C-27 scorer treats bold routing-only lines as a structural failure, V-04 drops to 99.47
and V-05 becomes the sole 100.0. If C-26 scorer requires both sub-gates to be named (not just
the confirmation), V-03 drops and V-05 becomes the sole 100.0.

**Carry-forward for R11**: V-05 (A+B+C). If V-03 also scores 100.0, prefer V-03 for minimalism
(fewer sub-gate labels; plain prose Copilot detection). If V-05 scores 100.0 and V-03 does not,
V-05 becomes the golden candidate.
