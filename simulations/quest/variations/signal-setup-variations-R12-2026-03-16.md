Now I have the full picture. R10 V-05 reached 100/100 on v9, R11 introduced C-31 (uniform identifier scheme) and C-32 (syntactically complete consequence anchors). The failure patterns: R11 mixed `GATE 1B-Abort` (word-suffix) with `GATE 1A`, `GATE 6A` (letter-slot), and `GATE 6-Decline` (word-suffix); and `GATE 6-Decline` had a fragment anchor `"The implementation phase — when you are writing."` that fails C-32.

---

```markdown
---
skill: quest-variate
skill_target: signal-setup
date: 2026-03-17
rubric_version: 11
round: 12
---

# signal-setup Variations — Round 12 (v11 rubric)

**Skill**: signal-setup
**Rubric**: v11 | **Denominator**: A=24 (aspirational C-09–C-32) | **Date**: 2026-03-17
**Formula**: `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/24 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## Context: What Informed This Round

R11 introduced two new failure patterns from observing V-01:

| Pattern | Criterion | Failure in R11 V-01 |
|---------|-----------|---------------------|
| Mixed identifier scheme | C-31 | `GATE 1A`, `GATE 1B`, `GATE 3A`, `GATE 6A` use letter-slot; `GATE 1B-Abort`, `GATE 6-Decline` use word-suffix hyphen. |
| Fragment consequence anchor | C-32 | `GATE 6-Decline` resolves to "The implementation phase — when you are writing." — a noun phrase with an appositive, not a complete sentence. C-21 and C-22 scored PARTIAL because the anchor contained correct phase vocabulary but no extractable claim. |

The v11 rubric formalizes these:
- **C-31**: All sub-gate identifiers in a spec use the same positional-encoding convention throughout.
- **C-32**: Every consequence anchor must be a syntactically complete sentence: subject, predicate, and stated outcome.

**R11 V-05 carry-forward baseline against v11 rubric (estimated)**:
- C-01..C-30: All assumed PASS (inherited from R10 V-05 + R11 structural fixes)
- C-31: **FAIL** — mixed scheme present
- C-32: **FAIL** — GATE 6-Decline is a fragment

**Estimated R11 V-05 composite against v11**:
```
(5/5 * 60) + (3/3 * 30) + (22/24 * 10) = 60 + 30 + 9.17 = 99.17
```

---

## Variation Axis Selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | C-31 letter-slot uniform | Convert all sub-gate identifiers to pure letter-slot (1A/1B, 5A/5B). No word-suffix hyphen variants anywhere. Single-axis: fix C-31 only; consequences inherited from R11. |
| B | C-31 word-suffix uniform | Convert all sub-gate identifiers to pure word-suffix (1-Missing/1-Present, 5-Confirm/5-Decline). Alternative scheme test. Single-axis: fix C-31 only; consequences inherited from R11. |
| C | C-32 complete-sentence anchors (subject-first) | Rewrite all consequence anchors as syntactically complete sentences with subject-first construction ("Signal is not configured in this workspace; at the planning stage..."). Single-axis: fixes C-32 only; identifier scheme from R11 (mixed). |
| A+C | Letter-slot + complete sentences (phase-first) | Both fixes: letter-slot identifiers plus phase-first complete-sentence anchors ("At the planning stage, when a specification is being drafted..."). Minimum-change dual fix. |
| A+C+Adversary | Letter-slot + adversary-named complete sentences + routing tables | Maximum combination: uniform letter-slot, consequence anchors name inertia as the winning actor ("Inertia wins the next planning session; when a specification is committed in this workspace, there is no question..."), routing tables in GATE 1 for C-29 maximality. |

Single-axis: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+C phase-first), V-05 (A+C adversary-named + routing tables)

Base behaviors preserved in all R12 variations (from R10 V-05):
- Distinct implementation-context Copilot template (implementation-phase vocabulary)
- Stage complementarity mapping in GATE 5A already-configured affirm
- Phase vocabulary separation: planning stage at GATE 3 decline, implementation stage at GATE 5B
- PROCEED/SKIP/EXIT meta-contract in preamble
- "Inertia now has a named opponent" in GATE 6 report
- C-01..C-30: all inherited

---

## V-01 — Axis A: C-31 Letter-Slot Uniform

**Variation axis**: C-31 (identifier uniformity — all letter-slot)
**Hypothesis**: R11 introduced word-suffix sub-gates (`GATE 1B-Abort`, `GATE 6-Decline`) alongside
letter-slot sub-gates (`GATE 1A`, `GATE 1B`, `GATE 3A`, `GATE 6A`). C-31 fails because the scheme
is mixed. The minimum fix is to rename all word-suffix variants to letter-slot: the abort path of
GATE 1B becomes GATE 1C; the decline path of GATE 6 becomes GATE 6B. No gate content changes.
Single-axis: consequence text is preserved from R11 including the fragment anchor at GATE 6B —
C-32 will still fail, isolating C-31 as the only variable.

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

Three outcomes are possible at each gate: PROCEED (continue to the next gate), SKIP (condition
already met, advance without writing), or EXIT (configuration incomplete, user declined). No gate
is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Route to GATE 1A if CLAUDE.md does not exist.
Route to GATE 1B if CLAUDE.md exists and already contains a Signal section.
Route to GATE 2 if CLAUDE.md exists and has no Signal section.

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

Route to GATE 3 (create-new mode) if the user confirms.
Route to GATE 1C if the user declines.

### GATE 1B — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

EXIT. Do not proceed to GATE 2.

### GATE 1C — Creation Declined

> Signal not configured. At the planning stage — before the next feature topic is named
> and the team decides whether to build — there will be no standing question in your context
> to ask "why would teams do nothing instead?" Inertia has no named opponent here.
> Run /signal-setup when you are ready to address that.

EXIT.

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

PROCEED to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

Route to GATE 3A if the user confirms.
Route to GATE 3B if the user declines.

### GATE 3A — Confirmed

PROCEED to GATE 4.

### GATE 3B — Declined

> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing instruction in Claude's context to
> ask "why would teams do nothing instead?" Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready to address that.

EXIT.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending mode: add at the end of the file.
- Create-new mode (GATE 1A path): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md"

PROCEED to GATE 5.

---

## GATE 5 — GitHub Copilot Extension (optional)

Check if `.github/copilot-instructions.md` exists. If it does not exist, SKIP to GATE 6.

*(Inline detection — intentionally not promoted to a sub-gate per C-28: this is a
detection-then-skip path; if copilot-instructions.md is absent the extension is
unavailable, requiring no user confirmation and no dedicated gate treatment.)*

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`). See GATE 5A (already configured) and GATE 5B/5C (confirmation)
below for all three outcomes.

### GATE 5A — Copilot Already Configured

A Signal section is already present in copilot-instructions.md.

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> CLAUDE.md protects the planning stage; Copilot instructions protect the implementation
> stage. Both stages are covered.

SKIP to GATE 6.

### GATE 5B — Confirm Copilot Append

No Signal section present. Ask: "Also update .github/copilot-instructions.md for GitHub
Copilot? [y/N]"

Route to GATE 5C (declined) if the user declines.

If confirmed: append to .github/copilot-instructions.md:

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

Confirm: ".github/copilot-instructions.md updated"

PROCEED to GATE 6.

### GATE 5C — Copilot Append Declined

> Copilot instructions not updated. During the implementation phase — when you are writing.
> Run /signal-setup again to extend coverage.

PROCEED to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-01 changes from R11 V-01 baseline:**
- `GATE 1B-Abort` → renamed to `GATE 1C` (letter-slot)
- `GATE 6-Decline` → renamed to `GATE 5C` (letter-slot; Copilot gate renumbered to GATE 5)
- `GATE 6A` → renamed to `GATE 5A`, `GATE 3A` preserved
- All sub-gates now: GATE 1A, GATE 1B, GATE 1C, GATE 3A, GATE 3B, GATE 5A, GATE 5B, GATE 5C
- **No content changes** — GATE 5C consequence deliberately preserves the R11 fragment
  "During the implementation phase — when you are writing." to isolate C-31 as single axis

**Expected scores against v11 rubric:**
- C-31: **PASS** — all sub-gates use letter-slot throughout; no word-suffix hyphen present
- C-32: **FAIL** — GATE 5C consequence "During the implementation phase — when you are writing."
  is still a fragment (intentionally unchanged for single-axis isolation)
- C-01..C-30: unchanged — PASS

**Predicted composite**:
```
(5/5 * 60) + (3/3 * 30) + (23/24 * 10) = 60 + 30 + 9.58 = 99.58
```

---

## V-02 — Axis B: C-31 Word-Suffix Uniform

**Variation axis**: C-31 (identifier uniformity — all word-suffix)
**Hypothesis**: V-01 demonstrates that letter-slot achieves C-31 uniformity. V-02 tests the
alternative: pure word-suffix identifiers (`GATE 1-Missing`, `GATE 1-Present`, `GATE 1-Abort`,
`GATE 3-Confirm`, `GATE 3-Decline`, `GATE 5-Present`, `GATE 5-Confirm`, `GATE 5-Decline`).
Word-suffix identifiers are more semantically self-documenting but longer. C-31 does not specify
which scheme must be used, only that the chosen scheme be internally consistent. This variation
tests whether word-suffix satisfies C-31 equally. Single-axis: same fragment consequence anchor
as V-01 GATE 5-Decline to continue isolating C-31 from C-32.

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

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled), or
EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Route to GATE 1-Missing if CLAUDE.md does not exist.
Route to GATE 1-Present if CLAUDE.md exists and already contains a Signal section.
Route to GATE 2 if CLAUDE.md exists and has no Signal section.

### GATE 1-Missing — CLAUDE.md Not Found

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

Route to GATE 3 (create-new mode) if the user confirms.
Route to GATE 1-Abort if the user declines.

### GATE 1-Present — Signal Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

EXIT. Do not proceed to GATE 2.

### GATE 1-Abort — Creation Declined

> Signal not configured. At the planning stage — before the next feature topic is named
> and the team decides whether to build — there will be no standing question in your context
> to ask "why would teams do nothing instead?" Inertia has no named opponent here.
> Run /signal-setup when you are ready to address that.

EXIT.

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

PROCEED to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

Route to GATE 3-Confirm if the user confirms.
Route to GATE 3-Decline if the user declines.

### GATE 3-Confirm — Write Authorized

PROCEED to GATE 4.

### GATE 3-Decline — Write Declined

> Signal not configured. At the planning stage — before the next feature topic is named
> and the spec is committed — there will be no standing instruction in Claude's context to
> ask "why would teams do nothing instead?" Inertia remains unnamed in this workspace.
> Run /signal-setup when you are ready to address that.

EXIT.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending mode: add at the end of the file.
- Create-new mode (GATE 1-Missing path): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md"

PROCEED to GATE 5.

---

## GATE 5 — GitHub Copilot Extension (optional)

Check if `.github/copilot-instructions.md` exists. If it does not exist, SKIP to GATE 6.

*(Inline detection — intentionally not promoted to a sub-gate per C-28: absence of
copilot-instructions.md is a skip-path requiring no user confirmation, so no named
gate is needed for a file-absent case that produces no decision point.)*

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`). See GATE 5-Present (already configured) and GATE 5-Confirm /
GATE 5-Decline (confirmation) below for all three outcomes.

### GATE 5-Present — Copilot Already Configured

A Signal section is already present in copilot-instructions.md.

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> CLAUDE.md protects the planning stage; Copilot instructions protect the implementation
> stage. Both stages are covered.

SKIP to GATE 6.

### GATE 5-Confirm — Copilot Append Confirmation

No Signal section present. Ask: "Also update .github/copilot-instructions.md for GitHub
Copilot? [y/N]"

Route to GATE 5-Decline if the user declines.

If confirmed: append to .github/copilot-instructions.md:

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

Confirm: ".github/copilot-instructions.md updated"

PROCEED to GATE 6.

### GATE 5-Decline — Copilot Append Declined

> Copilot instructions not updated. During the implementation phase — when you are writing.
> Run /signal-setup again to extend coverage.

PROCEED to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-02 changes from V-01:**
- All letter-slot sub-gate identifiers replaced with word-suffix throughout:
  - `GATE 1A` → `GATE 1-Missing`, `GATE 1B` → `GATE 1-Present`, `GATE 1C` → `GATE 1-Abort`
  - `GATE 3A` → `GATE 3-Confirm`, `GATE 3B` → `GATE 3-Decline`
  - `GATE 5A` → `GATE 5-Present`, `GATE 5B` → `GATE 5-Confirm`, `GATE 5C` → `GATE 5-Decline`
- Same fragment consequence at GATE 5-Decline as V-01 (C-32 still fails, single-axis isolation)
- Routing prose updated to reference word-suffix IDs throughout

**Expected scores against v11 rubric:**
- C-31: **PASS** — pure word-suffix throughout; letter-slot entirely absent
- C-32: **FAIL** — fragment preserved intentionally (single-axis)
- C-01..C-30: unchanged — PASS

**Predicted composite**:
```
(5/5 * 60) + (3/3 * 30) + (23/24 * 10) = 99.58
```

---

## V-03 — Axis C: C-32 Complete-Sentence Anchors (Subject-First)

**Variation axis**: C-32 (syntactically complete consequence anchors)
**Hypothesis**: All three consequence anchors in the R11 baseline that touch C-18/C-21/C-22 are
rewritten as syntactically complete sentences using subject-first construction: "Signal is not
configured in this workspace; at the planning stage, when a feature specification is drafted and
committed, there is no question in this context to ask whether the feature displaces a real default
behavior, and the decision proceeds on an assumption that was never named." This form ensures a
subject (`Signal is not configured`), a predicate (`there is no question`), and a stated outcome
(`the decision proceeds on an assumption that was never named`) are all present — making the
anchor an extractable claim. Single-axis: identifier scheme from R11 preserved (mixed) to isolate
C-32 from C-31.

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

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled), or
EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Route to GATE 1A if CLAUDE.md does not exist.
Route to GATE 1B if CLAUDE.md exists and already contains a Signal section.
Route to GATE 2 if CLAUDE.md exists and has no Signal section.

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

Route to GATE 3 (create-new mode) if the user confirms.
Route to GATE 1B-Abort if the user declines.

### GATE 1B — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

EXIT.

### GATE 1B-Abort — Creation Declined

Signal is not configured in this workspace; at the planning stage, when a feature topic is
being named and the team is deciding whether to build, there is no standing question in this
context to ask whether the feature displaces a real default behavior, and the decision proceeds
on an assumption that was never named. Run /signal-setup when you are ready to address that.

EXIT.

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

PROCEED to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

Route to GATE 3A if the user confirms.
Route to GATE 3B if the user declines.

### GATE 3A — Confirmed

PROCEED to GATE 4.

### GATE 3B — Declined

Signal is not configured in this workspace; at the planning stage, when a feature
specification is drafted and committed, there is no standing instruction in Claude's context
to ask whether the feature displaces a real default behavior, and the build is authorized
on an assumption that was never tested. Run /signal-setup when you are ready to address that.

EXIT.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending mode: add at the end of the file.
- Create-new mode (GATE 1A path): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md"

PROCEED to GATE 5.

---

## GATE 5 — GitHub Copilot Extension (optional)

Check if `.github/copilot-instructions.md` exists. If it does not exist, SKIP to GATE 6.

*(Inline detection — intentionally not promoted to a sub-gate per C-28: absence of
copilot-instructions.md is a skip-path with no decision point; no annotation needed
for a path that produces no gate body.)*

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`). See GATE 6A (already configured) and GATE 6-Decline (declined) below.

### GATE 6A — Copilot Already Configured

A Signal section is already present in copilot-instructions.md.

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> CLAUDE.md protects the planning stage; Copilot instructions protect the implementation
> stage. Both stages are covered.

SKIP to GATE 6.

Ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

Route to GATE 6-Decline if the user declines.

If confirmed: append to .github/copilot-instructions.md:

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

Confirm: ".github/copilot-instructions.md updated"

PROCEED to GATE 6.

### GATE 6-Decline — Copilot Append Declined

The Copilot instructions file is not updated; during the implementation phase, when Copilot
suggests the first function body for a new feature, there is no instruction in its context to
ask whether the behavior being coded matches what teams actually do today, and the implementation
proceeds on a premise that was never validated. Run /signal-setup to add the Copilot instructions
when you are ready.

PROCEED to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-03 changes from R11 V-01 baseline:**
- `GATE 1B-Abort` consequence: rewritten as complete sentence with subject-first construction.
  Before: (inferred fragment from R11 pattern)
  After: "Signal is not configured in this workspace; at the planning stage, when a feature topic
  is being named and the team is deciding whether to build, there is no standing question in this
  context to ask whether the feature displaces a real default behavior, and the decision proceeds
  on an assumption that was never named."
- `GATE 3B` consequence: same subject-first complete sentence for the spec-commit future moment.
- `GATE 6-Decline` consequence: complete sentence with implementation-phase anchor.
  Before (R11 fragment): "The implementation phase — when you are writing."
  After: "The Copilot instructions file is not updated; during the implementation phase, when
  Copilot suggests the first function body for a new feature, there is no instruction in its
  context to ask whether the behavior being coded matches what teams actually do today, and the
  implementation proceeds on a premise that was never validated."
- Identifier scheme: **intentionally preserved as R11 mixed** (1A letter-slot, 1B-Abort
  word-suffix, 6A letter-slot, 6-Decline word-suffix) to isolate C-32 as single axis

**Expected scores against v11 rubric:**
- C-31: **FAIL** — mixed scheme intentionally preserved (single-axis isolation)
- C-32: **PASS** — all three decline anchors are syntactically complete sentences with subject,
  predicate, and stated outcome; each is an extractable claim
- C-18: **PASS** — each anchor names a specific future moment
- C-21: **PASS** — GATE 6-Decline anchor is implementation-phase specific; GATE 3B is planning-specific
- C-22: **PASS** — GATE 3B uses "spec drafted and committed" vocabulary; GATE 6-Decline uses
  "function body" and "implementation" vocabulary — no overlap
- C-01..C-30: unchanged — PASS

**Predicted composite**:
```
(5/5 * 60) + (3/3 * 30) + (23/24 * 10) = 99.58
```

---

## V-04 — Axes A+C: Letter-Slot Uniform + Phase-First Complete Sentences

**Variation axis**: C-31 (letter-slot) + C-32 (phase-first complete sentences)
**Hypothesis**: V-01 fixes C-31 alone; V-03 fixes C-32 alone. V-04 combines both fixes using
phase-first sentence construction: consequence anchors open with an explicit phase label
("At the planning stage, when..."), placing the temporal context at the start rather than mid-
sentence. Phase-first construction satisfies C-23 (explicit phase label) more conspicuously than
subject-first: the phase category is the first words the reader encounters, making the distinction
unmistakable. Combined with pure letter-slot identifiers throughout, V-04 is the minimum-change
dual fix.

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

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled), or
EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

Route to GATE 1A if CLAUDE.md does not exist.
Route to GATE 1B if CLAUDE.md exists and already contains a Signal section.
Route to GATE 2 if CLAUDE.md exists and has no Signal section.

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

Route to GATE 3 (create-new mode) if the user confirms.
Route to GATE 1C if the user declines.

### GATE 1B — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

EXIT.

### GATE 1C — Creation Declined

At the planning stage, when a feature topic is being named and the team is deciding whether to
build, there is no standing question in this context to ask whether the feature displaces a real
default behavior, and the decision proceeds with inertia unnamed. Signal is not configured in this
workspace. Run /signal-setup when you are ready to address that.

EXIT.

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

PROCEED to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

Route to GATE 3A if the user confirms.
Route to GATE 3B if the user declines.

### GATE 3A — Confirmed

PROCEED to GATE 4.

### GATE 3B — Declined

At the planning stage, when a feature specification is being drafted and committed to the
repository, there is no standing instruction in Claude's context to ask whether the feature
displaces a real default behavior, and the build is authorized on an assumption that was never
tested. Signal is not configured in this workspace. Run /signal-setup when you are ready to
address that.

EXIT.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending mode: add at the end of the file.
- Create-new mode (GATE 1A path): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md"

PROCEED to GATE 5.

---

## GATE 5 — GitHub Copilot Extension (optional)

Check if `.github/copilot-instructions.md` exists. If it does not exist, SKIP to GATE 6.

*(Inline detection — intentionally not promoted to a sub-gate per C-28: this is a
detection-then-skip path; copilot-instructions.md absence requires no user decision, so
no sub-gate body is needed for the file-absent case.)*

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`). See GATE 5A (already configured) and GATE 5B/5C (confirmation)
below for all three outcomes.

### GATE 5A — Copilot Already Configured

A Signal section is already present in copilot-instructions.md.

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> CLAUDE.md protects the planning stage; Copilot instructions protect the implementation
> stage. Both stages are covered.

SKIP to GATE 6.

### GATE 5B — Confirm Copilot Append

No Signal section present. Ask: "Also update .github/copilot-instructions.md for GitHub
Copilot? [y/N]"

Route to GATE 5C if the user declines.

If confirmed: append to .github/copilot-instructions.md:

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

Confirm: ".github/copilot-instructions.md updated"

PROCEED to GATE 6.

### GATE 5C — Copilot Append Declined

During the implementation phase, when Copilot suggests the first function body for a new
feature, there is no instruction in its context to ask whether the behavior being coded
matches what teams actually do today, and the implementation proceeds on a premise that was
never validated. The Copilot instructions file is not updated. Run /signal-setup to add the
Copilot instructions when you are ready.

PROCEED to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-04 changes from R11 V-01 baseline:**
- Identifier scheme: pure letter-slot throughout (C-31 fixed)
  - Word-suffix variants removed: `GATE 1B-Abort` → `GATE 1C`, `GATE 6-Decline` → `GATE 5C`
- All consequence anchors: rewritten as phase-first complete sentences (C-32 fixed)
  - GATE 1C: "At the planning stage, when a feature topic is being named and the team is
    deciding whether to build, there is no standing question in this context..."
  - GATE 3B: "At the planning stage, when a feature specification is being drafted and
    committed to the repository, there is no standing instruction in Claude's context..."
  - GATE 5C: "During the implementation phase, when Copilot suggests the first function body
    for a new feature, there is no instruction in its context..."
- Phase-first construction: phase label is the first clause in each anchor sentence
- GATE 1C and GATE 3B share the planning-stage future moment (C-19: both Signal-absent exits)
- GATE 5C uses distinct implementation-phase vocabulary (C-22: no overlap with planning exits)

**Expected scores against v11 rubric:**
- C-31: **PASS** — pure letter-slot: GATE 1A, 1B, 1C, 3A, 3B, 5A, 5B, 5C; zero word-suffix
- C-32: **PASS** — all three decline anchors are syntactically complete; phase-first construction
  makes subject/predicate/outcome maximally readable; each is an extractable claim
- C-18: **PASS** — each anchor names a specific future moment
- C-21: **PASS** — GATE 5C is implementation-phase specific, distinct from GATE 3B planning-specific
- C-22: **PASS** — planning ("spec drafted and committed") vs implementation ("function body")
  — non-overlapping vocabulary sets
- C-23: **PASS** — phase label is the opening clause: "At the planning stage" / "During the
  implementation phase" — explicit, not inferred from artifact vocabulary
- C-19: **PASS** — GATE 1C and GATE 3B both reference the same planning-stage future moment

**Predicted composite**:
```
(5/5 * 60) + (3/3 * 30) + (24/24 * 10) = 60 + 30 + 10.0 = 100.0
```

---

## V-05 — Axes A+C+Adversary: Letter-Slot + Adversary-Named Sentences + Routing Tables

**Variation axis**: C-31 (letter-slot) + C-32 (adversary-named complete sentences) + C-29
(routing tables in GATE 1 for maximal routing explicitness)
**Hypothesis**: V-04 fixes both new criteria. V-05 maximizes the strength of the C-32 fix by
using adversary-named construction: consequence anchors name inertia as the actor that wins when
Signal is absent. "Inertia wins the next planning session; when a feature specification is drafted
and committed in this workspace, there is no question in this context to challenge whether teams
would adopt the planned behavior, and the build proceeds as if adoption were guaranteed." This
phrasing makes C-16 (inertia as named adversary) and C-32 (extractable claim) mutually reinforcing
— the adversary is the subject, winning is the predicate, the future moment is the outcome — and
also adds a routing table in GATE 1 so that all three detection branches and their destination gate
IDs are visible in a single contiguous block (strengthening C-29).

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
Inertia is not a concept; it is an adversary. This configuration decides whether it enters
every session named or unnamed.

Three outcomes are possible at each gate: PROCEED (continue), SKIP (already handled), or
EXIT (configuration incomplete). No gate is implicit.

---

## GATE 1 — Detect CLAUDE.md

Read CLAUDE.md in the current directory (or .claude/CLAUDE.md).
Search for an existing Signal section (marker: `## Signal` or `Signal is installed`).

| Condition | Route to |
|-----------|----------|
| CLAUDE.md does not exist | GATE 1A |
| CLAUDE.md exists, Signal section present | GATE 1B |
| CLAUDE.md exists, no Signal section | GATE 2 |

### GATE 1A — Missing CLAUDE.md

CLAUDE.md does not exist in this workspace.

Inform the user:
> No CLAUDE.md found. Signal will create one containing only the Signal section.
> No existing content will be affected.

Show the Signal section preview (same content as GATE 2 preview below).

Ask: "Create CLAUDE.md with this Signal section? [y/N]"

| User response | Route to |
|---------------|----------|
| Confirms (y) | GATE 3 (create-new mode) |
| Declines (N) | GATE 1C |

### GATE 1B — Already Configured

A Signal section already exists in CLAUDE.md.

> Signal is already configured. Inertia already has a named opponent here.
> Every session that opens this workspace loads CLAUDE.md automatically — the inertia
> question is present from the first message, without you having to remember to invoke it.
> That is the mechanism: the load itself keeps the question present, not you remembering to ask.
>
> If you also use GitHub Copilot, run /signal-setup to extend coverage to the implementation
> stage. Otherwise, run `/signal` to see all 77 available commands.

EXIT.

### GATE 1C — Creation Declined

Inertia wins the next planning session in this workspace; at the planning stage, when a
feature topic is being named and the team decides whether to build, there is no question in
this context to challenge whether the feature displaces a real default behavior, and the
decision proceeds as if the answer were obvious. Signal is not configured. Run /signal-setup
when you are ready to name the adversary.

EXIT.

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

PROCEED to GATE 3.

---

## GATE 3 — Confirm CLAUDE.md Write

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

Route to GATE 3A if the user confirms.
Route to GATE 3B if the user declines.

### GATE 3A — Confirmed

PROCEED to GATE 4.

### GATE 3B — Declined

Inertia wins the next planning session in this workspace; at the planning stage, when a
feature specification is drafted and committed to the repository, there is no standing
instruction in Claude's context to challenge whether the feature displaces a real default
behavior, and the build is authorized on an assumption that was never tested. Signal is not
configured. Run /signal-setup when you are ready to name the adversary.

EXIT.

---

## GATE 4 — Write to CLAUDE.md

Append the Signal section (exactly as shown in GATE 2) to CLAUDE.md.
- Appending mode: add at the end of the file.
- Create-new mode (GATE 1A path): write CLAUDE.md with only the Signal section.

Confirm: "Signal section added to CLAUDE.md"

PROCEED to GATE 5.

---

## GATE 5 — GitHub Copilot Extension (optional)

Check if `.github/copilot-instructions.md` exists. If it does not exist, SKIP to GATE 6.

*(Inline detection — intentionally not promoted to a sub-gate per C-28: copilot-instructions.md
absence is a detection-then-skip path with no user decision point; a sub-gate body would have
no content since there is nothing to offer when the file does not exist.)*

If copilot-instructions.md exists: check whether it already contains a Signal section
(marker: `## Signal`). See GATE 5A (already configured) and GATE 5B/5C (confirmation)
below for all three outcomes.

### GATE 5A — Copilot Already Configured

A Signal section is already present in copilot-instructions.md.

> Copilot instructions already include Signal.
> Copilot Chat loads workspace instructions at session start — the inertia rule is already
> present when Copilot begins suggesting code, without you attaching a prompt file.
>
> CLAUDE.md protects the planning stage; Copilot instructions protect the implementation
> stage. Both stages are covered. Inertia is named at both phases.

SKIP to GATE 6.

### GATE 5B — Confirm Copilot Append

No Signal section present. Ask: "Also update .github/copilot-instructions.md for GitHub
Copilot? [y/N]"

Route to GATE 5C if the user declines.

If confirmed: append to .github/copilot-instructions.md:

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

Confirm: ".github/copilot-instructions.md updated"

PROCEED to GATE 6.

### GATE 5C — Copilot Append Declined

Inertia wins the implementation phase in this workspace; during the implementation phase,
when Copilot suggests the first function body for a new feature, there is no instruction in
its context to challenge whether the behavior being coded matches what teams actually do today,
and the implementation proceeds on a premise that was never validated. The Copilot instructions
file is not updated. Run /signal-setup to name the adversary at the implementation stage.

PROCEED to GATE 6.

---

## GATE 6 — Done

Print a two-column status table:

| File | Status |
|------|--------|
| CLAUDE.md | Signal section written |
| .github/copilot-instructions.md | [Written / Already present / Skipped / Not found] |

Print: "Inertia now has a named opponent in the contexts listed above."

Print:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```

---

**V-05 changes from V-04 baseline:**
- Preamble: added "Inertia is not a concept; it is an adversary. This configuration decides
  whether it enters every session named or unnamed." (strengthens C-16)
- GATE 1 routing: converted from prose to a routing table with condition/destination columns
  (strengthens C-29: all branches enumerable from a single contiguous location)
- GATE 1A routing: added routing table within GATE 1A for confirm/decline branching
- Consequence construction: changed from phase-first to adversary-named construction
  - GATE 1C: "Inertia wins the next planning session in this workspace; at the planning stage..."
  - GATE 3B: "Inertia wins the next planning session in this workspace; at the planning stage,
    when a feature specification is drafted and committed..."
  - GATE 5C: "Inertia wins the implementation phase in this workspace; during the implementation
    phase, when Copilot suggests the first function body..."
- GATE 5A already-configured affirm: added "Inertia is named at both phases." to close the
  adversary-framing loop for the success path
- All other content: identical to V-04

**Three future moments, fully distinct:**

| Gate | Exit type | Phase label | Future moment | Inertia framing |
|------|-----------|-------------|---------------|-----------------|
| GATE 1C | Signal-absent exit | planning stage | feature topic being named | "wins the next planning session" |
| GATE 3B | Signal-absent exit | planning stage | spec drafted and committed | "wins the next planning session" |
| GATE 5C | Optional decline | implementation phase | first function body suggested | "wins the implementation phase" |

GATE 1C and GATE 3B share the same planning-stage future moment (C-19: consistent across
Signal-absent exits). GATE 5C uses non-overlapping implementation vocabulary (C-22). All
three are phase-labeled explicitly (C-23). All three are syntactically complete (C-32).

**Expected scores against v11 rubric:**
- C-31: **PASS** — pure letter-slot: GATE 1A, 1B, 1C, 3A, 3B, 5A, 5B, 5C; no word-suffix
- C-32: **PASS** — adversary-named construction is maximally complete: subject (inertia), predicate
  (wins), phase label (planning/implementation), future moment (spec committed/function body), outcome
  (build proceeds on untested assumption). Every anchor is an extractable claim.
- C-29: **PASS (strengthened)** — GATE 1 and GATE 1A both use routing tables; all branches and
  destination gate IDs enumerable without reading sub-gate prose
- C-16: **PASS (strengthened)** — adversary framing present in preamble, all decline anchors,
  and GATE 5A already-configured affirm
- C-18, C-19, C-21, C-22, C-23: **PASS** — same reasoning as V-04, now with adversary framing
- C-01..C-30: all unchanged — PASS

**Predicted composite**:
```
(5/5 * 60) + (3/3 * 30) + (24/24 * 10) = 60 + 30 + 10.0 = 100.0
```

---

## Summary

| Variation | Axes | C-31 | C-32 | Key change | Predicted composite |
|-----------|------|------|------|------------|---------------------|
| V-01 | A: letter-slot only | **PASS** | FAIL | Convert word-suffix sub-gates to letter-slot; preserve R11 fragment anchor | 99.58 |
| V-02 | B: word-suffix only | **PASS** | FAIL | Convert all sub-gates to word-suffix; preserve R11 fragment anchor | 99.58 |
| V-03 | C: complete sentences only | FAIL | **PASS** | Rewrite all decline anchors as complete sentences; preserve R11 mixed scheme | 99.58 |
| V-04 | A+C: letter-slot + phase-first sentences | **PASS** | **PASS** | Both fixes; phase-first construction ("At the planning stage, when...") | **100.0** |
| V-05 | A+C+adversary+routing tables | **PASS** | **PASS** | Both fixes; adversary-named construction + routing tables in GATE 1 | **100.0** |

**Design recommendation**: V-04 is the minimum-change dual fix — two criteria resolved,
no additional structural additions. V-05 is the maximum-coverage variant — additionally
strengthens C-16, C-29, and closes the adversary-framing loop in GATE 5A. If V-04 and V-05
both score 100 under v11, prefer V-04 for minimalism. V-05 is preferred if any prior round
criterion was scored as PARTIAL on C-16 or C-29.

V-01 and V-02 test whether the scheme choice (letter-slot vs word-suffix) independently
resolves C-31 — both should score identically. V-03 tests whether sentence completeness alone
(without scheme fix) independently resolves C-32 — should score identically to V-01/V-02 but
on the opposite criterion.

**Carry-forward for R13**: V-05 (A+C+adversary+routing) unless scoring reveals V-04's
phase-first construction matches V-05's score — in which case V-04 is preferred per minimum
complexity principle from CLAUDE.md.
```
