Reading the Round 7 scorecard carefully to extract the new patterns before writing.

From the evidence, three distinct patterns emerge that aren't captured by C-09–C-21:

1. **Phase-indexed vocabulary** — V-02's PARTIAL on C-21 wasn't tool-distinctness failure, it was phase-distinctness failure. "build"/"build suggestion" differ by tool name only. C-21 as written requires path-specific anchors, but doesn't explicitly require phase-vocabulary separation. The new pattern: consequence anchors must index into development phases, not merely swap tool names.

2. **Explicit phase labels** — V-03 and V-05 distinguished themselves by naming the phase category directly ("at the planning stage," "while implementing") rather than leaving phase implied by artifact vocabulary. This is structurally stronger than vocabulary choice alone.

3. **Secondary gate already-configured affirm** — The ranking notes call out "GATE 6 already-configured affirm" as a feature of V-04 and V-05. C-15 covers the primary already-configured path (GATE 2), but the Copilot already-configured path (GATE 6) is a distinct secondary gate with its own tool-local consequence to affirm. No existing criterion reaches it.

These become C-22, C-23, C-24. Denominator moves from 13 → 16.

---

```markdown
---
skill: quest-rubric
skill_target: signal-setup
date: 2026-03-16
version: 8
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
| C-19 | **Key arguments threaded through all equivalent exit gates** | structure | The future-moment anchor (C-18) and any other critical consequence arguments appear at *every* point where the user exits without configuring Signal — not only at the primary decline gate. If both GATE 1 (missing file, user declines creation) and GATE 4 (existing file, user declines append) are Signal-absent exits, both carry the same specific future-moment framing. No Signal-absent decline path delivers a weaker consequence argument than any other. |
| C-20 | **Already-configured gate names the persistence mechanism** | behavior | The already-configured path (GATE 2 or equivalent) goes beyond affirming positive consequence (C-15) to explicitly name *how* the configuration achieves permanence — that CLAUDE.md loads automatically every session, meaning the inertia question is present without the user having to remember. The user understands the mechanism behind the permanence, not merely that the configuration is doing something good. |
| C-21 | **Secondary optional gates carry path-specific consequence anchors** | behavior | Every gate where the user can decline an optional post-Signal extension step (e.g., GATE 6 for Copilot instructions) names a specific future-moment consequence that is local to that path's tool or context — not a generic reuse of the primary decline framing. A GATE 6 decline names a Copilot-specific moment; a GATE 4 decline names a build-specific moment. No optional exit is consequence-free, and no two exits share identical consequence language when the tools they protect are distinct. |
| C-22 | **Consequence anchors are phase-indexed, not tool-indexed** | behavior | When two decline gates protect tools that operate at different development phases (e.g., planning vs. implementation), their consequence anchors draw vocabulary from those phases — they do not merely substitute a tool name into shared framing. "Before the next build" vs. "before the next Copilot build suggestion" fails this criterion: "build" is the shared anchor and tool-name substitution is the only difference. "Before the spec is committed" vs. "before Copilot implements the first endpoint" passes: the vocabulary sets are non-overlapping and each is phase-native. |
| C-23 | **Explicit phase label at each decline anchor** | structure | Decline-path consequence anchors name the development phase as an explicit category ("at the planning stage," "while implementing") rather than implying phase only through artifact vocabulary (e.g., "spec," "function body"). The user reads the phase label directly; inference from word choice is not required. |
| C-24 | **Secondary already-configured paths affirm tool-local consequence** | behavior | When an optional extension gate (e.g., GATE 6 for Copilot instructions) detects an existing configuration, its response affirms what that specific tool's configuration achieves — framed in that tool's vocabulary and workflow context, not a generic reuse of the primary already-configured affirmation (C-15, C-20). The user learns what the Copilot configuration does for them inside Copilot interactions, not merely that a file already exists. |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)
```

**Golden threshold**: All 5 essential criteria pass **AND** composite score ≥ 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | ≥ 80 + all essential | Production-ready. Ships. |
| Silver | ≥ 70 | Strong. One targeted revision reaches gold. |
```

---

Three criteria added, denominator updated 13 → 16:

- **C-22** closes the gap that made V-02 PARTIAL: tool-name substitution alone does not satisfy path-specificity; the vocabulary must be phase-native to each gate.
- **C-23** promotes V-03/V-05's explicit phase labeling from "nice vocabulary choice" to a testable structural requirement.
- **C-24** extends the already-configured affirmation pattern (C-15, C-20) to secondary gates — the Copilot path has its own tool-local benefit to name, and the existing criteria only reach GATE 2.
