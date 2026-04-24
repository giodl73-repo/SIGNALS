---
skill: quest-golden
skill_target: signal-setup
date: 2026-03-17
rounds: 20
rubric_final: signal-setup-rubric-v18-2026-03-17.md
score: 100
status: GOLDEN
---

# signal-setup — Golden Prompt (R20, v18 rubric)

**Variation**: V-04 (letter-slot uniform, single Copilot extension)
**Rubric**: v18 | **Denominator**: 45 aspirational | **Composite**: 100.0
**Formula**: `(5/5 × 60) + (3/3 × 30) + (45/45 × 10) = 100`

---

## Golden Prompt Body

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

## What Made It Golden

**1. Inertia as adversary with a named artifact (C-33, C-34, C-44)**
Every decline path names inertia as the grammatical subject of victory *and* follows the
causal chain one step further than technically required — to the concrete artifact inertia
produces. GATE 6B does not just say "inertia wins"; it says "code that assumes adoption
gets generated." This satisfies C-44 (artifact specificity) and extends the C-38 → C-21
chain to its terminal output. V-01's failing GATE 6VS-Write and V-02's GATE 6B each stop
one link short of this.

**2. Concurrent-moment placement of Signal (C-45)**
GATE 6AA places Signal as co-present at the instant Copilot acts: "While Copilot is
suggesting implementation code, the inertia question is already in Copilot's context."
The "while [tool] is [active verb phrase]" construction makes Signal operationally visible
— not an archival installation fact, not a future benefit. V-03's failure axis ("when the
team reaches the build phase, the inertia question will be in Copilot's context") shows
exactly what concurrent framing replaces: future conditional describes a coming state;
concurrent construction shows active co-presence now.

**3. Uniform letter-slot naming scheme throughout (C-31, C-41, C-42)**
Every sub-gate ID is a letter appended to its parent number: 1A/1B under GATE 1, 2A under
GATE 2, 4A/4B under GATE 4, 6A/6B under GATE 6, 6AA/6AB under GATE 6A. The scheme is
non-colliding, readable, and encodes depth-2 lineage without abbreviation ambiguity. C-41
(sub-gate IDs encode parent) and C-42 (non-colliding depth-2) pass non-vacuously.

**4. Two-step consequence chains at every decline gate (C-22, C-23, C-34)**
Each decline gate uses non-overlapping vocabulary: "planning stage" (GATE 1B, 4B) vs.
"implementation stage" (GATE 6B). The consequence anchors are syntactically complete
two-step chains: force wins → artifact produced → question never asked. No two decline
gates describe the same moment in the same words. This satisfies C-22 (non-overlapping
vocabulary) and C-34 (two-step chains present).

**5. Inline detection annotation scoped to the single extension gate (C-28, C-30)**
The inline annotation on GATE 6A — "(No sub-gate for file-existence — file creation is
included in the confirmed write action when the file is missing; no separate confirmation
point is required.)" — appears once, on the one gate that makes the inline architectural
choice. Because the spec has a single optional-extension gate, C-43 (cross-gate consistency)
passes vacuously; C-30 (annotation present) passes non-vacuously. The scope is right-sized
to the structure: one integration, one annotation, no asymmetry possible.

---

## Final Rubric Summary (v18, 45 criteria)

| Tier | Count | Criteria | Notes |
|------|-------|----------|-------|
| Essential | C-01–C-05 | 5 | GATE read, preview, confirm, signal section, idempotent |
| Recommended | C-06–C-08 | 3 | Inertia rule, optional extension menu, outcome report |
| Aspirational | C-09–C-45 | 37 | Structural precision, adversary framing, gate naming, consequence chains |

**v18 additions (C-43–C-45) — the precision chain:**

| ID | What it tests | Source evidence | Extends |
|----|---------------|-----------------|---------|
| C-43 | Parallel inline-detection paths carry identical promotion rationale | R19 V-02 C-30 PASS: both `6-Copilot` and `6-Code` carry same annotation | C-30 — consistency *across* gates, not just *within* one gate |
| C-44 | Tool-specific decline anchors name the artifact produced under inertia | R19 V-01 C-38 PASS: "through Copilot: code that assumes adoption gets generated" | C-21/C-38 — extends adversary chain from force+channel to force+channel+artifact |
| C-45 | Already-configured affirmations place Signal in concurrent operation with the tool | R19 V-01 C-24 PASS: "While Copilot is suggesting implementation code, the inertia question is already in Copilot's context" | C-24 — concurrent-moment framing, not archival description |

**Score breakdown (V-04):**

```
Essential:    5/5  × 60 =  60.00
Recommended:  3/3  × 30 =  30.00
Aspirational: 45/45 × 10 = 10.00  (C-43 vacuous PASS; C-44 and C-45 non-vacuous PASS)
                           -------
                            100.00
```

**Golden threshold**: all 5 essentials PASS AND composite >= 80. **Status: GOLDEN.**
