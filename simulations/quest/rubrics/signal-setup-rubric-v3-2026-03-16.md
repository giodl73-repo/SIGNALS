Reading the scorecard for excellence signals not yet captured in C-01 through C-12.

Two patterns stand out:

1. **V-05 / C-06**: "Leads the entire skill with a three-paragraph inertia framing before any instructions" — the skill *itself* opens with motivational philosophy before procedural steps. Distinct from C-06 (inertia rule in the *appended content*).

2. **V-05 / C-03**: "'Signal not configured. Inertia remains unaddressed.'" — the decline path names the *consequence* the user accepts, not just acknowledges the action ("No changes made.").

Neither is captured by existing criteria. Adding as C-13 and C-14. Aspirational denominator: 4 → 6.

```markdown
---
skill: quest-rubric
skill_target: signal-setup
date: 2026-03-16
version: 3
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

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: All 5 essential criteria pass **AND** composite score ≥ 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | ≥ 80, all essential | Publish-ready |
| Passing | ≥ 60, all essential | Usable with known gaps |
| Failing | Any essential fails | Not usable |
```

---

**What changed v2 → v3:**

- **C-13** (aspirational): Skill-level motivational preamble. Sourced from V-05's three-paragraph inertia framing that precedes all procedural instructions. Different from C-06, which scores whether inertia appears in the *appended content* — this scores whether the *skill document itself* leads with the *why*.
- **C-14** (aspirational): Consequence-named decline. Sourced from V-05's decline message "Signal not configured. Inertia remains unaddressed." The criterion captures a meaningful UX distinction: telling the user what they accepted, not just what was skipped.
- **Aspirational denominator**: 4 → 6. A perfect aspirational sweep is now worth the same 10 points, distributed across 6 criteria.
