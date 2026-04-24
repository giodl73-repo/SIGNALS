Reading the scorecard carefully before writing.

Three new patterns emerge from Round 10:

1. **Primary vs. secondary detection promotion scope** — V-03 passes C-12 despite handling Copilot already-configured inline, because C-12's promotion requirement applies to the primary Signal configuration flow. The scorecard makes this explicit ("C-12 territory, not a confirmation point — inline prose is valid for it") but no criterion encodes the scope distinction. Without C-28, a spec could incorrectly promote secondary detection to sub-gates and fail, or correctly leave it inline and have no rubric support.

2. **Routing prose enumerates branches with destination identifiers** — V-03's routing blocks are flat (condition → gate ID) lists in plain prose; V-02's GATE 0 uses bold to carry the same information. C-27 prohibits the bold but does not specify the positive form. Without C-29, a spec that uses implicit routing ("proceed to the next section") would avoid bold but still fail navigability — and the rubric could not reach it.

3. **Inline skip paths carry explicit promotion rationale** — V-03 annotates "(no sub-gate needed — this is a skip path)". This transforms an ambiguous inline treatment into a documented architectural decision. Without C-30, a reader (or scorer) cannot distinguish an intentional inline skip from a forgotten promotion. The annotation is the evidence that C-28's scope distinction was *applied*, not merely that it exists in the rubric.

Denominator: A=19 → A=22.

---

```markdown
---
skill: quest-rubric
skill_target: signal-setup
date: 2026-03-16
version: 10
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
| C-12 | **Edge-case paths promoted to first-class gates** | structure | The "already configured" and "missing CLAUDE.md" cases in the primary Signal configuration flow are handled as dedicated named gates (not inline conditionals inside the happy path). Each edge-case gate has its own complete, explicit treatment. |
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
| C-25 | **Sub-gate identifiers encode parent gate lineage** | structure | Named sub-gates carry an identifier that encodes both the parent gate number and the branch position — e.g., `GATE 1A` names the parent phase (1) and the branch slot (A). A reader can determine, without reading prose, which phase a sub-gate belongs to and how many branches that phase has. Sub-gates numbered or lettered independently of their parent (e.g., GATE 7, GATE 8 for what are structurally branches of GATE 1) fail this criterion. This applies to edge-case branches, optional-extension confirmation points, and any other sub-gate introduced by C-12 or C-26. |
| C-26 | **Optional-step confirmation points promoted to first-class named sub-gates** | structure | Every point where the user confirms or declines an optional extension step — distinct from the main Signal configuration — is promoted to a dedicated named sub-gate with its own complete treatment. Optional extension confirmation is not folded into the parent gate as a trailing paragraph, handled as an inline continuation block, or omitted from the gate index. A spec with seven named GATE headers that handles the Copilot append confirmation as a paragraph inside the final gate fails this criterion. C-12 covers edge-case detection paths; C-26 covers optional confirmation checkpoints on happy extension paths. Both require first-class promotion; neither subsumes the other. |
| C-27 | **Gate boundaries enforced by document-structure markers, not prose markers** | structure | Every gate and sub-gate boundary is delimited by a heading element (`##`, `###`, `####`, or equivalent block-level structural delimiter) rather than an inline typographic marker (`**bold**:`, `*italic*:`, or bullet sub-items containing conditional logic). A reader navigating the document by heading outline can enumerate every gate without reading prose. A spec that uses bold inline labels — e.g., `**If not found**:` or `**Already present**:` inside a step body — as pseudo-gate delimiters fails this criterion regardless of how complete the conditional treatment is. This is the mechanism behind C-12: the structural heading is what makes a gate "dedicated" and "named" in a navigable sense, not the presence of a label in prose. |
| C-28 | **Primary-path detection promotion scope distinguished from secondary-path** | structure | C-12's requirement that "already configured" and "missing file" detection paths be promoted to first-class named sub-gates applies to the primary Signal configuration flow (detection of existing CLAUDE.md Signal section; detection of missing CLAUDE.md). Detection of existing configuration in secondary optional-extension tools (e.g., Copilot instructions) may be handled inline within the parent optional-extension gate body — provided the inline treatment carries complete consequence affirmation (C-24). A spec that promotes every detection path to a sub-gate is not penalized; a spec that handles any primary detection path inline fails C-12 regardless of secondary handling. This criterion rewards explicit recognition of the scope boundary: primary detection always promotes; secondary detection may be inline when no confirmation is required. |
| C-29 | **Routing prose enumerates all branches with destination gate identifiers** | structure | When a gate body branches to multiple downstream gates, the routing block lists every branch as a (condition, destination gate ID) pair in a single contiguous location within the parent gate's prose. A reader who reads only the routing block can name every branch and every destination without reading any sub-gate body. Routing split across multiple paragraphs, routing that omits any branch, routing that names destinations without conditions, or routing that names conditions without gate identifiers — all fail this criterion. This is the positive architectural requirement that complements C-27's typographic prohibition: explicit gate identifiers in plain prose are what make routing navigable without formatting crutches. Implicit routing ("proceed to the next section," "see below") and typographic routing (`**bold**` labels) both fail for different reasons — implicit routing loses the destination identity; typographic routing violates C-27. |
| C-30 | **Inline detection paths carry explicit promotion rationale** | structure | When a detection path in an optional-extension gate is intentionally left inline (not promoted to a sub-gate per C-12), the spec annotates the decision with an explicit rationale — e.g., "(no sub-gate needed — this is a skip path, not a confirmation point)" or equivalent. The annotation distinguishes a deliberate architectural choice from an oversight. A spec whose inline optional-extension detection paths carry no annotation is scored FAIL (the intent is indeterminate; absence of annotation cannot be credited as a pass). Detection paths that are promoted to sub-gates do not require annotation; only intentional inline paths in optional-extension gates require rationale. A spec that has no optional-extension gates passes this criterion vacuously. |

---

## Scoring Formula

`(essential/5 × 60) + (recommended/3 × 30) + (aspirational/22 × 10)`

**Scoring**: PASS=1 | PARTIAL=0.5 | FAIL=0
```
