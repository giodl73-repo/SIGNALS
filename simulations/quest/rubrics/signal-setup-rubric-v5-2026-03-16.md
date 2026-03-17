Scanning the scorecard for patterns not yet captured by any existing criterion.

**New pattern in V-03 / C-13 PASS** — The preamble explains *why configuration persists*: "setup happens once... needs to live in Claude's context for every session that follows." V-04 C-13 is PARTIAL precisely because this temporal-persistence reasoning is absent. C-13 only requires a motivational preamble exists — it doesn't require the "setup endures across sessions" argument. Distinct axis.

**New pattern in V-04 / C-14 PASS** — The decline feedback doesn't just name the absent thing; it anchors the consequence to a specific future moment: "there is no reminder in your context to ask 'why would teams do nothing?' **before the next build**." Prior partial forms only say what was given up, not *when* the absence will be felt. Distinct from C-14.

Adding as C-17 and C-18. Aspirational denominator: 8 → 10.

---

```markdown
---
skill: quest-rubric
skill_target: signal-setup
date: 2026-03-16
version: 5
---

# Scoring Rubric: signal-setup

## Skill Description
Configure Signal in a workspace after installation. Checks for existing CLAUDE.md and
.github/copilot-instructions.md, shows a preview, asks confirmation, then appends a
Signal section advertising available skills and the inertia rule. Safe to re-run —
detects existing Signal sections and skips.

---

## Essential Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **File detection before write** | correctness | Skill reads/checks for CLAUDE.md (and optionally copilot-instructions.md) before attempting any write. Does not blindly overwrite. |
| C-02 | **Preview shown before writing** | behavior | A preview of the Signal section content is displayed to the user prior to any file modification. |
| C-03 | **Confirmation required** | behavior | Skill explicitly asks user to confirm before writing. Does not write without a yes/proceed signal. |
| C-04 | **Signal section appended with skill advertising** | correctness | After confirmation, a Signal section is appended to CLAUDE.md that lists or references the available Signal skills (not an empty placeholder). |
| C-05 | **Idempotent re-run** | correctness | When run a second time on a workspace that already has a Signal section, the skill detects it and skips the write rather than duplicating content. |

---

## Recommended Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Inertia rule included** | coverage | The appended Signal section explicitly includes or references the inertia rule (the principle that governs when a topic is ready). |
| C-07 | **Copilot instructions offered** | coverage | Skill offers (prompts or describes) an option to update .github/copilot-instructions.md in addition to CLAUDE.md. |
| C-08 | **User feedback on outcome** | format | After completing (or skipping), skill outputs a clear status message: what was written, what was skipped, and where. |

---

## Aspirational Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Preview matches written output** | correctness | The previewed content is byte-for-byte (or semantically) identical to what is actually appended. No content drift between preview and write. |
| C-10 | **Handles missing CLAUDE.md gracefully** | behavior | If no CLAUDE.md exists, skill either creates one with the Signal section or clearly explains what it would create, without erroring out silently. |
| C-11 | **Named gate checkpoints as explicit phase boundaries** | structure | Each lifecycle phase (detect, preview, confirm, write, report) is named as a numbered gate or equivalent labeled checkpoint. No phase can be implicitly skipped — the structure of the spec itself enforces sequencing. |
| C-12 | **Edge-case paths promoted to first-class gates** | structure | The "already configured" and "missing CLAUDE.md" cases are handled as dedicated named gates (not inline conditionals inside the happy path). Each edge-case gate has its own complete, explicit treatment. |
| C-13 | **Skill opens with motivational preamble** | structure | The skill itself (not just the appended content) opens with a brief philosophical or motivational framing — explaining *why* setup matters — before procedural instructions begin. The inertia concept or equivalent is introduced as the reason to configure, not merely as output content. |
| C-14 | **Decline path names its consequence** | behavior | When the user declines to proceed, the skill's feedback explicitly names what remains unaddressed (e.g., "Signal not configured. Inertia remains unaddressed.") rather than only acknowledging the action ("No changes made."). The user understands what they gave up, not just what didn't happen. |
| C-15 | **Already-configured path affirms positive consequence** | behavior | When the skill detects an existing Signal section and skips the write, its response explicitly names what that configuration achieves — not just "Already configured. No changes needed." but something that affirms the work the existing setup is doing (e.g., "Inertia already has a named opponent here."). The user understands what their setup does for them, not merely that no action is required. |
| C-16 | **Inertia named as adversary, not concept** | structure | In the preamble or skill opening, inertia is framed as a named opponent or silent competitor — not merely described as a rule or principle. The user understands they are choosing a side in a conflict when they configure Signal, not just learning about a system behavior. |
| C-17 | **Preamble explains temporal persistence of configuration** | structure | The motivational preamble explains not just *why* inertia matters but *why the configuration must persist*: setup happens once, but the reminder must live in Claude's context for every session that follows. The "setup endures" argument is present — not merely the adversary framing. The user understands the stakes of the write, not merely the stakes of the problem. |
| C-18 | **Decline path anchors consequence to a future moment** | behavior | The decline feedback names not only what remains absent but connects it to a specific future moment where the absence will be felt (e.g., "there is no reminder in your context to ask 'why would teams do nothing?' before the next build"). The user understands *when* they will feel the consequence, not merely that a consequence exists. |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

**Golden threshold**: All 5 essential criteria pass **AND** composite score ≥ 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | ≥ 80, all essential | Publish-ready |
| Passing | ≥ 60, all essential | Usable with known gaps |
| Failing | Any essential fails | Not usable |
```

---

**What changed in v5:**

| New criterion | Source signal | What it captures |
|---|---|---|
| C-17 | V-03 C-13 PASS / V-04 C-13 PARTIAL | Preamble explains *why setup persists* — not just adversary framing but temporal durability argument |
| C-18 | V-04 C-14 PASS evidence | Decline consequence anchored to a future moment ("before the next build"), not just named abstractly |

C-17 and C-18 are logically downstream of C-13 and C-14 respectively — they require the parent behavior at full strength before the refinement applies. A skill that passes C-17 necessarily passes C-13; one that passes C-18 necessarily passes C-14.
