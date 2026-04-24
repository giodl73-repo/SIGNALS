Now I have the full picture. R10 V-04's GATE 1 used bold inline routing (`**If ...**`) — a known C-27 issue fixed in R10 V-03. R12 introduced C-31 (letter-slot scheme preference) and C-32 (complete assertable anchor sentences) as the new denominator additions. The R13 axes should target these specifically.

---

```markdown
---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-17
rubric_version: 12
round: 13
---

# signal-setup Variations — Round 13 (v12 rubric)

**Skill**: signal-setup
**Rubric**: v12 | **Denominator**: A=26 | **Date**: 2026-03-17
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/26 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

Round 10 V-05 (Axes A+B+C: single detection parent + Copilot dual sub-gates + heading-only
routing) scored 100/100 on the v9 rubric (C-01..C-27). Rounds 11 and 12 extended the rubric
with C-28..C-30 (inline detection scope, routing prose contiguity, inline annotation) and
C-31..C-32 (scheme uniformity, anchor sentence completeness).

Two patterns extracted from R12 shape R13:

| Pattern | Source | R12 consequence |
|---------|--------|-----------------|
| Letter-slot preferred over word-suffix | V-01/V-02 equivalence note — both scored 98.75 confirming C-31 was scheme-agnostic under v11; v12 formalizes the preference | R12 V-01 used pure letter-slot; V-02 used uniform word-suffix. Both passed C-31. v12 adds preference — word-suffix specs may now score lower even when uniform. |
| Activity-verb anchoring in consequence sentences | V-03's C-22 analysis revealed that "phase label + nominalized noun" anchors fail C-32 even when phase vocabulary is correct | R12 V-03's GATE 5B anchor used the phase label "implementation stage" followed by a dangling clause, not a complete assertable proposition. v12 C-32 formalizes the completeness requirement. |

**R12 best candidate against v12 (estimated)**:
- C-01..C-30: All PASS
- C-31: PASS (V-01 used letter-slot uniformly; V-02 used word-suffix uniformly — both satisfy C-31)
- C-32: **PROBABLE FAIL** — R12 best candidates used anchors of the form "at the planning
  stage, before the spec is committed, there is no inertia question" which names a phase and
  states an absence but does not deliver a complete subject–predicate–outcome proposition that
  can be extracted and asserted standalone. "There is no inertia question" lacks an outcome
  consequence: it states absence of a check, not the downstream consequence of that absence.
  C-32 requires that the anchor be an extractable claim — not merely that it contain
  phase-appropriate words.

**New axes for R13**:

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Pure letter-slot throughout | R12 V-02 demonstrated word-suffix uniformity is equivalent under v11. v12's preference means V-02-style specs now face scoring pressure. Axis A enforces letter-slot identifiers exclusively (GATE 1A, 1B, 5A, 5B — no -Decline, -Confirm, -Missing, -Found suffixes anywhere). This is not a structural change from R12 V-01; the hypothesis is that explicitly annotating the choice as intentional and stripping any remnant word-suffix from the R11/R12 base delivers C-31 PASS under the new preference. |
| B | Complete, assertable consequence anchor sentences | R12 anchors passed C-18/C-21/C-22/C-23 because they contained the right vocabulary. But vocabulary presence does not satisfy C-32 if the sentence lacks a complete predicate that delivers a stated outcome. Axis B rewrites every decline and abort anchor as a sentence with an explicit subject, a full predicate, and a named outcome — not an absence label. Test: each anchor must be readable as a standalone claim that answers "what happens at that phase if Signal is absent?" |
| C | Contiguous routing block per parent gate with explicit gate IDs | C-29 requires all branches listed with (condition, destination gate ID) in a single contiguous location. R12 best candidates used plain prose routing ("Three cases: see GATE 1A if..., see GATE 1B if..., otherwise proceed to...") which satisfies C-27's no-bold requirement but may scatter routing information across phrases. Axis C introduces an explicit "Route:" block at the start of each parent gate body, listing every branch as a (condition → GATE NX) pair on a separate line. No routing information appears outside this block. |

Single-axis: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+C)

Base behaviors preserved across all R13 variations:
- All C-01..C-30 behaviors from R10 V-05 / R12 best candidate
- Single detection parent: GATE 1 with GATE 1A (missing) and GATE 1B (already configured)
- Copilot extension: GATE 5 with inline already-configured detection (annotation per C-30),
  GATE 5A (Copilot confirmed) and GATE 5B (Copilot declined) as first-class sub-gates (C-26)
- Primary detection paths promoted to heading-delimited sub-gates (C-12, C-27)
- Secondary detection (Copilot already-configured) inline with annotation (C-28, C-30)
- No bold inline routing in any parent gate body (C-27)
- Planning-stage vocabulary for primary decline gates (C-22, C-23)
- Implementation-stage vocabulary for GATE 5B (C-21, C-22, C-23)
- GATE 1B names auto-load persistence mechanism (C-20) and stage complementarity
- GATE 5A names Copilot-local consequence when already configured (C-24)
- Distinct implementation-context Copilot section template (planning/implementation symmetry)
- "Inertia now has a named opponent" in final report (C-08)

---

## V-01 — Axis A: Pure Letter-Slot Identifiers

**Variation axis**: C-31 — scheme uniformity with letter-slot preference
**Hypothesis**: R12 V-01 achieved letter-slot uniformity but the choice was incidental — not
explicitly architectural. v12 adds a preference criterion that favors letter-slot over
word-suffix even when both satisfy uniformity. V-01 makes the letter-slot choice
deliberately architectural: sub-gate identifiers encode parent + position (1A = parent 1,
position A) with no word-suffix variants anywhere in the spec. Consequence anchors carry
adequate phase vocabulary (satisfying C-18/C-22/C-23 from R10 base) but are not restructured
for C-32 completeness — isolating whether the scheme choice alone affects the composite score.

Gate structure: GATE 1 (GATE 1A, GATE 1B) | GATE 2 | GATE 3 | GATE 4 | GATE 5 (GATE 5A, GATE 5B) | GATE 6

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

## GATE 1 -- Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Three cases follow. If CLAUDE.md is not found, see GATE 1A. If CLAUDE.md is found and
already contains a Signal section, see GATE 1B. If CLAUDE.md is found and has no Signal
section, continue to GATE 2.

### GATE 1A -- Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal not configured. At the planning stage, before a spec is committed, there is no
> inertia question in Claude's context. Inertia has no named opponent here.
> Run /signal-setup when you are ready.
Stop.

If Y: proceed to GATE 3 in create-new mode.

### GATE 1B -- Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically -- the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> CLAUDE.md covers the planning stage. If you also use GitHub Copilot, run /signal-setup
> to extend coverage to the implementation stage. Otherwise, run /signal to see all
> available commands.

Stop.

---

## GATE 2 -- Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal -- Feature Decision Intelligence

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

## GATE 3 -- Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal not configured. At the planning stage, before the spec is committed, there is no
> standing inertia question in Claude's context. Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready.
Stop.

If Y: proceed to GATE 4.

---

## GATE 4 -- Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md."

Proceed to GATE 5.

---

## GATE 5 -- GitHub Copilot Extension

Check whether `.github/copilot-instructions.md` exists. If it does not exist, skip to GATE 6.

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`).

(Inline detection -- no sub-gate needed: existing-Copilot-configuration is a skip/affirm
path, not a new confirmation checkpoint requiring user input. Per C-28, secondary optional-
extension detection may be handled inline provided full consequence affirmation is given.)

If Signal already present in copilot-instructions.md:
> Copilot instructions already include Signal. Copilot Chat loads workspace instructions
> automatically at session start -- the inertia rule is already present when Copilot begins
> suggesting code. CLAUDE.md protects the planning stage; Copilot instructions protect the
> implementation stage. Both stages are covered.
Proceed to GATE 6.

If no Signal section in copilot-instructions.md, offer the extension. Two branches follow:
if user confirms, see GATE 5A; if user declines, see GATE 5B.

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

### GATE 5A -- Copilot Confirmed

Append to .github/copilot-instructions.md:

---
## Signal -- Feature Decision Intelligence (Implementation Context)

Before accepting a Copilot suggestion that adds a new feature or endpoint, ask:
"Does this code assume adoption without evidence?"

Use Signal skills to verify the assumption:
  /trace-request, /trace-permissions, /trace-state  -- implementation trace
  /flow-lifecycle, /flow-resilience, /flow-throttle  -- process and failure path
  /review-code, /review-design                       -- multi-discipline validation
  /prove-hypothesis, /prove-prototype                -- assumption testing

Docs: .github/prompts/
---

Confirm: ".github/copilot-instructions.md updated."

Proceed to GATE 6.

### GATE 5B -- Copilot Declined

> Copilot instructions not updated. At the implementation stage, before Copilot suggestions
> become code, there will be no inertia check in its context.
> Run /signal-setup again to extend coverage.

Proceed to GATE 6.

---

## GATE 6 -- Done

Print a status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     -- see all available commands
  /decide     -- run your first campaign
```

---

**V-01 changes from R12 base:**
- All sub-gate identifiers explicitly letter-slot: GATE 1A (parent=1, position A),
  GATE 1B (parent=1, position B), GATE 5A (parent=5, position A), GATE 5B (parent=5, position B)
- No word-suffix variants anywhere; identifier scheme is uniform throughout (C-31)
- Consequence anchors: planning-stage vocabulary, adequate but not fully engineered for C-32
  completeness — "before a spec is committed, there is no inertia question in Claude's context"
  is syntactically a sentence but the predicate names absence without stating downstream outcome
- Routing: plain prose listing (no bold, satisfying C-27; no explicit contiguous gate-ID pairs)

**Expected scores:**
- C-01..C-30: All PASS (preserved from R12 base)
- C-31: PASS — pure letter-slot uniformity, architecturally declared
- C-32: **PROBABLE FAIL** — "there is no inertia question in Claude's context" names absence
  but does not deliver a complete subject–predicate–outcome proposition. The downstream
  consequence of that absence (what the team will be doing when the absence is felt) is not
  stated. C-32 requires the anchor to be "readable as a standalone assertion" — this anchor
  requires the reader to infer the consequence rather than extracting it directly.

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (25/26 * 10) = 60 + 30 + 9.62 = **99.62**
(C-32 FAIL = -1/26; partial credit not applicable per C-32 wording)

---

## V-02 — Axis B: Complete Consequence Anchor Sentences

**Variation axis**: C-32 — syntactically complete, assertable consequence propositions
**Hypothesis**: R12's decline anchors were phase-indexed (C-22/C-23 PASS) but did not form
complete subject–predicate–outcome propositions. An anchor of the form "at the planning stage,
before the spec is committed, there is no inertia question" satisfies phase-labeling but the
predicate ("there is no inertia question") is an absence statement — it tells the user what
is missing, not what HAPPENS because it is missing. C-32 requires the anchor to be "a
syntactically complete sentence: a subject, a predicate, and a stated outcome or effect"
that can be read as a standalone assertion. V-02 rewrites every decline and abort anchor as
an explicitly complete proposition: "At the [phase], when you are [activity-verb], no [X] is
present in your context to [outcome-verb] before you [phase-terminal-action]." Single axis:
identifier scheme uses letter-slot (same as V-01 base) but the key change is anchor sentence
architecture.

Gate structure: identical to V-01 (GATE 1 / GATE 1A / GATE 1B / GATE 2 / GATE 3 / GATE 4 / GATE 5 / GATE 5A / GATE 5B / GATE 6)

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

## GATE 1 -- Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Three cases follow. If CLAUDE.md is not found, see GATE 1A. If a Signal section is already
present, see GATE 1B. If CLAUDE.md exists without a Signal section, continue to GATE 2.

### GATE 1A -- Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal is not installed in this workspace. At the planning stage, when you are committing
> to a feature specification, no inertia question is present in your Claude Code context to
> ask "why would teams do nothing?" before you make that commitment.
> Run /signal-setup when you are ready.
Stop.

If Y: proceed to GATE 3 in create-new mode.

### GATE 1B -- Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically -- the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the automatic load keeps the question present, not your memory.
>
> CLAUDE.md covers the planning stage. If you also use GitHub Copilot, run /signal-setup
> to extend coverage to the implementation stage. Otherwise, run /signal.

Stop.

---

## GATE 2 -- Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal -- Feature Decision Intelligence

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

## GATE 3 -- Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal is not installed in CLAUDE.md. At the planning stage, when you are reviewing a
> feature brief and deciding whether to proceed, no inertia question is present in your
> Claude Code context to ask "why would teams do nothing?" before you commit to building
> this feature.
> Run /signal-setup when you are ready.
Stop.

If Y: proceed to GATE 4.

---

## GATE 4 -- Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md."

Proceed to GATE 5.

---

## GATE 5 -- GitHub Copilot Extension

Check whether `.github/copilot-instructions.md` exists. If it does not exist, skip to GATE 6.

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`).

(Inline detection -- no sub-gate needed: existing-Copilot-configuration is a skip/affirm
path within a confirmed write step, not a new confirmation checkpoint requiring user input.
Secondary optional-extension detection may be handled inline per C-28, provided full
consequence affirmation is given below.)

If Signal already present in copilot-instructions.md:
> Copilot instructions already include Signal. Copilot Chat loads .github/copilot-instructions.md
> automatically at session start -- the inertia rule is present when Copilot begins suggesting
> code, without you attaching a prompt file. CLAUDE.md protects the planning stage; Copilot
> instructions protect the implementation stage. Both stages are covered.
Proceed to GATE 6.

If no Signal section in copilot-instructions.md, offer the extension. Two branches follow:
if user confirms, see GATE 5A; if user declines, see GATE 5B.

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

### GATE 5A -- Copilot Confirmed

Append to .github/copilot-instructions.md:

---
## Signal -- Feature Decision Intelligence (Implementation Context)

Before accepting a Copilot suggestion that adds a new feature or endpoint, ask:
"Does this code assume adoption without evidence?"

Use Signal skills to verify the assumption:
  /trace-request, /trace-permissions, /trace-state  -- implementation trace
  /flow-lifecycle, /flow-resilience, /flow-throttle  -- process and failure path
  /review-code, /review-design                       -- multi-discipline validation
  /prove-hypothesis, /prove-prototype                -- assumption testing

Docs: .github/prompts/
---

Confirm: ".github/copilot-instructions.md updated."

Proceed to GATE 6.

### GATE 5B -- Copilot Declined

> Copilot instructions are not updated. At the implementation stage, when Copilot is
> suggesting function bodies and code patterns for your feature, no Signal guidance is
> present in its context to ask "does this code assume adoption without evidence?" before
> Copilot's suggestion becomes part of your implementation.
> Run /signal-setup again to extend coverage.

Proceed to GATE 6.

---

## GATE 6 -- Done

Print a status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     -- see all available commands
  /decide     -- run your first campaign
```

---

**V-02 changes from V-01:**
- GATE 1A decline anchor: rewritten from absence-label to complete subject–predicate–outcome
  proposition: "no inertia question is present in your Claude Code context to ask 'why would
  teams do nothing?' before you make that commitment." Subject: "no inertia question."
  Predicate: "is present in your Claude Code context." Outcome: "to ask '...' before you
  make that commitment." All three components present and extractable as a standalone claim.
- GATE 3 decline anchor: equivalent complete proposition — same structure, different
  activity verb ("reviewing a feature brief and deciding whether to proceed" vs. "committing
  to a feature specification"). C-19: both Signal-absent exits carry equivalent argument depth.
- GATE 5B decline anchor: complete proposition with implementation-phase vocabulary —
  "when Copilot is suggesting function bodies and code patterns" (activity-native verb phrase
  per C-22); "no Signal guidance is present in its context to ask '...' before Copilot's
  suggestion becomes part of your implementation" (stated outcome). C-22: planning vocabulary
  ("reviewing a feature brief") and implementation vocabulary ("Copilot suggesting function
  bodies") are non-overlapping.
- Identifier scheme: same letter-slot as V-01 (no C-31 change)
- Routing: same prose format as V-01 (no C-29 change)

**Expected scores:**
- C-01..C-31: All PASS (C-31 preserved from V-01 letter-slot scheme)
- C-32: PASS — every decline anchor is a syntactically complete sentence with explicit
  subject, full predicate, and named downstream outcome. Each can be extracted and read
  as a standalone assertion without inference.

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (26/26 * 10) = 60 + 30 + 10 = **100.0**
(No predicted failures)

---

## V-03 — Axis C: Contiguous Routing Blocks with Explicit Gate IDs

**Variation axis**: C-29 — routing prose enumerates all branches with destination gate IDs
in a single contiguous location per parent gate
**Hypothesis**: R12 base candidates used scattered prose routing — "Three cases: see GATE 1A
if missing, GATE 1B if already configured, otherwise continue" which satisfies C-27's
no-bold requirement but may fail C-29 because the conditions and destinations are embedded
in a continuous sentence rather than listed as (condition, destination) pairs. C-29 requires
"a single contiguous location within the parent gate's prose" listing "every branch as a
(condition, destination gate ID) pair." V-03 introduces an explicit "Route:" block at the
start of each branching gate body that lists every branch on a dedicated line with its
condition and destination gate ID. No routing information appears outside this block.
Single axis: consequence anchors use adequate-but-not-engineered phrasing (same as V-01,
not V-02-level completeness), isolating whether the routing block format drives score.

Gate structure: GATE 1 (GATE 1A, GATE 1B) | GATE 2 | GATE 3 | GATE 4 | GATE 5 (GATE 5A, GATE 5B) | GATE 6

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

## GATE 1 -- Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Route:
- CLAUDE.md not found                              → GATE 1A
- CLAUDE.md found, Signal section already present  → GATE 1B
- CLAUDE.md found, no Signal section               → GATE 2

### GATE 1A -- Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

Route:
- User declines (N)   → exit (see consequence below)
- User confirms (Y)   → GATE 3 (create-new mode)

If exit:
> Signal not configured. At the planning stage, before a spec is committed, there is no
> inertia question in Claude's context. Inertia has no named opponent here.
> Run /signal-setup when you are ready.
Stop.

### GATE 1B -- Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically -- the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> CLAUDE.md covers the planning stage. If you also use GitHub Copilot, run /signal-setup
> to extend to the implementation stage. Otherwise, run /signal.

Stop.

---

## GATE 2 -- Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal -- Feature Decision Intelligence

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

Route:
- Preview displayed   → GATE 3

---

## GATE 3 -- Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

Route:
- User declines (N)   → exit (see consequence below)
- User confirms (Y)   → GATE 4

If exit:
> Signal not configured. At the planning stage, before the spec is committed, there is no
> standing inertia question in Claude's context. Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready.
Stop.

---

## GATE 4 -- Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md."

Route:
- Write complete   → GATE 5

---

## GATE 5 -- GitHub Copilot Extension

Check whether `.github/copilot-instructions.md` exists.

(Inline detection of existing Copilot configuration -- no sub-gate needed: detecting
presence of a copilot-instructions.md file and its existing Signal content is a skip/affirm
path, not a new confirmation checkpoint requiring user input. Secondary optional-extension
detection may be handled inline per C-28. Annotation required per C-30.)

If copilot-instructions.md is not found:
> No .github/copilot-instructions.md found. Skipping Copilot extension.
Proceed to GATE 6.

If copilot-instructions.md exists and already contains a Signal section:
> Copilot instructions already include Signal. Copilot Chat loads workspace instructions
> automatically at session start -- the inertia rule is already present when Copilot begins
> suggesting code. CLAUDE.md protects the planning stage; Copilot instructions protect the
> implementation stage. Both stages are covered.
Proceed to GATE 6.

If copilot-instructions.md exists with no Signal section:

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

Route:
- User confirms (Y)   → GATE 5A
- User declines (N)   → GATE 5B

### GATE 5A -- Copilot Confirmed

Append to .github/copilot-instructions.md:

---
## Signal -- Feature Decision Intelligence (Implementation Context)

Before accepting a Copilot suggestion that adds a new feature or endpoint, ask:
"Does this code assume adoption without evidence?"

Use Signal skills to verify the assumption:
  /trace-request, /trace-permissions, /trace-state  -- implementation trace
  /flow-lifecycle, /flow-resilience, /flow-throttle  -- process and failure path
  /review-code, /review-design                       -- multi-discipline validation
  /prove-hypothesis, /prove-prototype                -- assumption testing

Docs: .github/prompts/
---

Confirm: ".github/copilot-instructions.md updated."

Route:
- Write complete   → GATE 6

### GATE 5B -- Copilot Declined

> Copilot instructions not updated. At the implementation stage, before Copilot suggestions
> become code, there will be no inertia check in its context.
> Run /signal-setup again to extend coverage.

Route:
- User declined   → GATE 6

---

## GATE 6 -- Done

Print a status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     -- see all available commands
  /decide     -- run your first campaign
```

---

**V-03 changes from V-01:**
- Every branching parent gate (GATE 1, GATE 3, GATE 4, GATE 5) has an explicit "Route:" block
  listing every branch as a (condition → destination) pair on a dedicated line
- GATE 1A internal branching also uses "Route:" block (confirm → GATE 3, decline → exit)
- No routing information appears outside the "Route:" block in any parent gate body
- GATE 2 and GATE 4 have trivial single-branch Route blocks confirming the downstream gate
- Consequence anchors: same adequate-but-not-engineered phrasing as V-01 (C-32 not targeted)
- Identifier scheme: same letter-slot as V-01

**C-29 evidence**: Every parent gate has exactly one "Route:" block. Each branch is listed
as a (condition → GATE NX) pair. A reader who reads only the Route blocks can enumerate
every branch and every destination without reading any gate body prose.

**Expected scores:**
- C-01..C-31: All PASS
- C-29: PASS — contiguous (condition → destination gate ID) blocks present at every
  branching gate; no routing information scattered outside the Route block
- C-32: **PROBABLE FAIL** — anchors use same structure as V-01 (absence label, not
  complete subject–predicate–outcome proposition)

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (25/26 * 10) = 60 + 30 + 9.62 = **99.62**
(C-32 FAIL = -1/26)

---

## V-04 — Combined A+B: Letter-Slot Purity + Complete Anchor Sentences

**Variation axes**: C-31 (letter-slot scheme) + C-32 (complete assertable propositions)
**Hypothesis**: V-01 demonstrates letter-slot purity is sufficient for C-31 PASS. V-02
demonstrates complete anchor sentences are sufficient for C-32 PASS. The question is whether
both together produce a composite that equals or exceeds V-02 alone — and whether any
interaction between the two axes creates scoring effects not visible in single-axis runs.
The combined variation preserves the V-01 plain-prose routing format (Axis C not applied),
so C-29 is the remaining risk. If C-29 PASS requires the explicit Route: block and plain
prose routing fails it, V-04 should score the same as V-02 (both miss C-29). If C-29 PASS
is achievable with plain prose routing (as long as routing is complete and contiguous in
natural language), V-04 matches V-02 on all criteria.

Gate structure: identical to V-01 and V-02 (GATE 1 / GATE 1A / GATE 1B / GATE 2 / GATE 3 / GATE 4 / GATE 5 / GATE 5A / GATE 5B / GATE 6)

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

## GATE 1 -- Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Three cases follow. If CLAUDE.md is not found, see GATE 1A. If CLAUDE.md is found and
already contains a Signal section, see GATE 1B. If CLAUDE.md is found and has no Signal
section, continue to GATE 2.

### GATE 1A -- Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

If N:
> Signal is not installed in this workspace. At the planning stage, when you are committing
> to a feature specification, no inertia question is present in your Claude Code context to
> ask "why would teams do nothing?" before you make that commitment.
> Run /signal-setup when you are ready.
Stop.

If Y: proceed to GATE 3 in create-new mode.

### GATE 1B -- Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically -- the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the automatic load keeps the question present, not your memory.
>
> CLAUDE.md covers the planning stage. If you also use GitHub Copilot, run /signal-setup
> to extend coverage to the implementation stage. Otherwise, run /signal.

Stop.

---

## GATE 2 -- Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal -- Feature Decision Intelligence

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

## GATE 3 -- Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N:
> Signal is not installed in CLAUDE.md. At the planning stage, when you are reviewing a
> feature brief and deciding whether to proceed, no inertia question is present in your
> Claude Code context to ask "why would teams do nothing?" before you commit to building
> this feature.
> Run /signal-setup when you are ready.
Stop.

If Y: proceed to GATE 4.

---

## GATE 4 -- Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md."

Proceed to GATE 5.

---

## GATE 5 -- GitHub Copilot Extension

Check whether `.github/copilot-instructions.md` exists. If it does not exist, skip to GATE 6.

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`).

(Inline detection -- no sub-gate needed: existing-Copilot-configuration is a skip/affirm
path within the confirmed extension flow, not a new confirmation checkpoint. Secondary
optional-extension detection may be handled inline per C-28, provided full consequence
affirmation is given below.)

If Signal already present in copilot-instructions.md:
> Copilot instructions already include Signal. Copilot Chat loads .github/copilot-instructions.md
> automatically at session start -- the inertia rule is present when Copilot begins suggesting
> code, without you attaching a prompt file. CLAUDE.md protects the planning stage; Copilot
> instructions protect the implementation stage. Both stages are covered.
Proceed to GATE 6.

If no Signal section in copilot-instructions.md, offer the extension. Two branches follow:
if user confirms, see GATE 5A; if user declines, see GATE 5B.

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

### GATE 5A -- Copilot Confirmed

Append to .github/copilot-instructions.md:

---
## Signal -- Feature Decision Intelligence (Implementation Context)

Before accepting a Copilot suggestion that adds a new feature or endpoint, ask:
"Does this code assume adoption without evidence?"

Use Signal skills to verify the assumption:
  /trace-request, /trace-permissions, /trace-state  -- implementation trace
  /flow-lifecycle, /flow-resilience, /flow-throttle  -- process and failure path
  /review-code, /review-design                       -- multi-discipline validation
  /prove-hypothesis, /prove-prototype                -- assumption testing

Docs: .github/prompts/
---

Confirm: ".github/copilot-instructions.md updated."

Proceed to GATE 6.

### GATE 5B -- Copilot Declined

> Copilot instructions are not updated. At the implementation stage, when Copilot is
> generating function bodies and code patterns for your feature, no Signal guidance is
> present in its context to ask "does this code assume adoption without evidence?" before
> Copilot's suggestion becomes your implementation.
> Run /signal-setup again to extend coverage.

Proceed to GATE 6.

---

## GATE 6 -- Done

Print a status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     -- see all available commands
  /decide     -- run your first campaign
```

---

**V-04 changes from V-02:**
- All changes from V-02 preserved (complete anchor sentences)
- All changes from V-01 preserved (pure letter-slot: GATE 1A, 1B, 5A, 5B throughout)
- No structural change from either V-01 or V-02 — this is a union of their two single-axis changes
- The only incremental risk vs. V-02: none on C-31 (both use letter-slot); none on C-32
  (both use complete sentences). The question is whether the two axes are truly independent
  or whether their combination reveals a new interaction effect. Plain prose routing preserved
  (Axis C not applied); C-29 remains the untested criterion at this point.

**Expected scores:**
- C-01..C-32: All PASS
- C-29: **RISK** — plain prose routing ("Three cases follow. If ... see GATE 1A...") may
  not satisfy C-29's "single contiguous location" requirement if a scorer reads "three cases
  follow" as introducing a contiguous list versus reading the conditions scattered across
  a prose sentence as not constituting a formal (condition, gate ID) pairing.

**Predicted composite (optimistic)**: (5/5 * 60) + (3/3 * 30) + (26/26 * 10) = **100.0**
**Predicted composite (C-29 risk)**: (5/5 * 60) + (3/3 * 30) + (25/26 * 10) = **99.62**

---

## V-05 — Combined A+B+C: Letter-Slot + Complete Sentences + Contiguous Routing

**Variation axes**: C-31 (letter-slot) + C-32 (complete sentences) + C-29 (contiguous routing)
**Hypothesis**: V-02 demonstrates C-31+C-32 achieves a predicted 100.0. V-03 demonstrates
C-29 + C-31 achieves 99.62 (C-32 still fails). V-05 combines all three: pure letter-slot
sub-gate identifiers, complete subject–predicate–outcome consequence anchors at every decline
path, and explicit "Route:" blocks at every branching parent gate. The expected result is
100/100 with no C-29 risk because Route: blocks definitively satisfy "single contiguous
location with (condition, destination gate ID) pairs." V-05 is the full-integration candidate.

Gate structure: GATE 1 (GATE 1A, GATE 1B) | GATE 2 | GATE 3 | GATE 4 | GATE 5 (GATE 5A, GATE 5B) | GATE 6

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

## GATE 1 -- Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Route:
- CLAUDE.md not found                              → GATE 1A
- CLAUDE.md found, Signal section already present  → GATE 1B
- CLAUDE.md found, no Signal section               → GATE 2

### GATE 1A -- Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

Route:
- User declines (N)   → exit (see consequence below)
- User confirms (Y)   → GATE 3 (create-new mode)

If exit:
> Signal is not installed in this workspace. At the planning stage, when you are committing
> to a feature specification, no inertia question is present in your Claude Code context to
> ask "why would teams do nothing?" before you make that commitment.
> Run /signal-setup when you are ready.
Stop.

### GATE 1B -- Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically -- the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the automatic load keeps the question present, not your memory.
>
> CLAUDE.md covers the planning stage. If you also use GitHub Copilot, run /signal-setup
> to extend coverage to the implementation stage. Otherwise, run /signal.

Stop.

---

## GATE 2 -- Preview Signal Section

Show the user exactly what will be appended to CLAUDE.md:

---
## Signal -- Feature Decision Intelligence

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

Route:
- Preview displayed   → GATE 3

---

## GATE 3 -- Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

Route:
- User declines (N)   → exit (see consequence below)
- User confirms (Y)   → GATE 4

If exit:
> Signal is not installed in CLAUDE.md. At the planning stage, when you are reviewing a
> feature brief and deciding whether to proceed, no inertia question is present in your
> Claude Code context to ask "why would teams do nothing?" before you commit to building
> this feature.
> Run /signal-setup when you are ready.
Stop.

---

## GATE 4 -- Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending: add at the end of the file.
- Creating (GATE 1A mode): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md."

Route:
- Write complete   → GATE 5

---

## GATE 5 -- GitHub Copilot Extension

Check whether `.github/copilot-instructions.md` exists.

(Inline detection of existing Copilot configuration -- no sub-gate needed: detecting
presence and Signal-section content of copilot-instructions.md is a skip/affirm path,
not a new confirmation checkpoint requiring user input. Secondary optional-extension
detection may be handled inline per C-28; annotation required per C-30.)

Route (inline detection, resolved before user prompt):
- copilot-instructions.md not found          → skip to GATE 6 (no Copilot file present)
- copilot-instructions.md found, Signal present → affirm below, then GATE 6
- copilot-instructions.md found, no Signal   → offer update: user prompt below → GATE 5A or GATE 5B

If not found:
> No .github/copilot-instructions.md in this workspace. Skipping Copilot extension.
Proceed to GATE 6.

If Signal already present:
> Copilot instructions already include Signal. Copilot Chat loads .github/copilot-instructions.md
> automatically at session start -- the inertia rule is present when Copilot begins suggesting
> code, without you attaching a prompt file. CLAUDE.md protects the planning stage; Copilot
> instructions protect the implementation stage. Both stages are covered.
Proceed to GATE 6.

If no Signal section found: ask the user.

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

Route:
- User confirms (Y)   → GATE 5A
- User declines (N)   → GATE 5B

### GATE 5A -- Copilot Confirmed

Append to .github/copilot-instructions.md:

---
## Signal -- Feature Decision Intelligence (Implementation Context)

Before accepting a Copilot suggestion that adds a new feature or endpoint, ask:
"Does this code assume adoption without evidence?"

Use Signal skills to verify the assumption:
  /trace-request, /trace-permissions, /trace-state  -- implementation trace
  /flow-lifecycle, /flow-resilience, /flow-throttle  -- process and failure path
  /review-code, /review-design                       -- multi-discipline validation
  /prove-hypothesis, /prove-prototype                -- assumption testing

Docs: .github/prompts/
---

Confirm: ".github/copilot-instructions.md updated."

Route:
- Write complete   → GATE 6

### GATE 5B -- Copilot Declined

> Copilot instructions are not updated. At the implementation stage, when Copilot is
> generating function bodies and code patterns for your feature, no Signal guidance is
> present in its context to ask "does this code assume adoption without evidence?" before
> Copilot's suggestion becomes your implementation.
> Run /signal-setup again to extend coverage.

Route:
- User declined   → GATE 6

---

## GATE 6 -- Done

Print a status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     -- see all available commands
  /decide     -- run your first campaign
```

---

**V-05 changes from V-04:**
- All V-04 behaviors preserved (letter-slot identifiers + complete anchor sentences)
- Added "Route:" blocks to GATE 1, GATE 1A, GATE 2, GATE 3, GATE 4, GATE 5, GATE 5A, GATE 5B
- GATE 5 "Route (inline detection...)" block handles the three detection sub-cases (not found,
  Signal present, no Signal) as explicit (condition → destination) mappings before the user
  prompt, satisfying C-29 for the secondary detection path within the optional extension gate
- No routing information appears outside Route: blocks in any gate body
- C-29 evidence: a reader who reads only the Route: blocks in each gate can enumerate every
  branch and every destination without reading any prose body text

**Expected scores:**
- C-01..C-32: All PASS
- C-29: PASS — explicit (condition → GATE NX) pairs in contiguous Route: blocks at every
  branching gate, including GATE 5's inline detection sub-cases
- C-31: PASS — pure letter-slot throughout: GATE 1A (parent=1, A), GATE 1B (parent=1, B),
  GATE 5A (parent=5, A), GATE 5B (parent=5, B)
- C-32: PASS — every decline anchor has explicit subject ("Signal is not installed in..."),
  full predicate ("no inertia question is present in your Claude Code context"), and stated
  outcome ("to ask '...' before you [make that commitment / commit to building / Copilot's
  suggestion becomes your implementation]")

**Predicted composite**: (5/5 * 60) + (3/3 * 30) + (26/26 * 10) = 60 + 30 + 10 = **100.0**
```

---

**Summary of axis selection and predicted scores:**

| Variation | Axis | Key change | C-29 | C-31 | C-32 | Predicted |
|-----------|------|-----------|------|------|------|-----------|
| V-01 | A only | Letter-slot purity | RISK | PASS | FAIL | 99.62 |
| V-02 | B only | Complete anchor sentences | RISK | PASS | PASS | 100.0 |
| V-03 | C only | Contiguous Route: blocks | PASS | PASS | FAIL | 99.62 |
| V-04 | A+B | Letter-slot + complete sentences | RISK | PASS | PASS | 99.62–100.0 |
| V-05 | A+B+C | Full integration | PASS | PASS | PASS | 100.0 |

**Key diagnostic questions this round answers:**
1. Does C-32 FAIL alone explain the R12 score gap? → Compare V-01 (C-32 only) vs V-02 (C-32 fixed)
2. Does C-29 plain-prose routing fail C-29, or is it acceptable? → Compare V-02 vs V-05
3. Is V-02 already sufficient for 100/100, making V-05 redundant? → Compare V-02 vs V-05 scores
4. Does letter-slot purity alone (C-31) add any score increment over V-03 baseline? → Compare V-01 vs V-03
