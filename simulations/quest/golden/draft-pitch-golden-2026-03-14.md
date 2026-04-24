Golden prompt document written to `simulations/quest/golden/draft-pitch-golden-2026-03-14.md`.

**What's in it:**

- **Frontmatter**: skill, target, date, rounds=12, rubric, score=100.0, status=GOLDEN
- **Prompt body**: Simplified (1065 words, 43.7% reduction) — all essential criteria verified PASS
- **Note**: Full scored body (with BINDING DECLARATION, PHASE 5 STRUCTURE, VERSION DIFFERENTIATION GATE) preserved in the variations file
- **What made it golden** — 5 patterns:
  1. SIGNAL DEFAULTS unconditional loading (no-signal resilience)
  2. Three-node named dependency chain (BELIEF MAP → POSITIONING LOCK → EXEC OPENING SENTENCE)
  3. Phase 2 BINDING DECLARATION with exhaustiveness closure *(full scored version)*
  4. Binary gate with embedded rewrite loop (exec opening cannot reach Phase 5 without passing)
  5. Audience belief mapping as pre-condition for argument construction
- **Full rubric summary**: All 45 criteria (4 essential + 3 recommended + 38 aspirational) with per-criterion pass status
requirement was wrong" |
| Maker inertia | "waiting to see how it lands before asking if we should have built it differently" |
| Exec outcome | "know what you know before you commit" |
| Dev friction | "late-stage requirement changes traced back to questions nobody asked before starting" |
| Maker outcome | "stop finding out you built the wrong thing after you built it" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code or run CI." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios (simulations/techniques/)" |

---

**=== PHASE 1: SIGNAL INTAKE ===**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-positioning-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS rows it overrides and the override value.

**Phase 1 output**: active values table -- which DEFAULTS fields are overridden and by what.

**-- PHASE 1 COMPLETE. Do not proceed until active values are written. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Consumes*: Phase 1 active values.
*Produces*: **AUDIENCE BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land. Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not serve as the primary belief anchor for a different audience.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting").
- **Inertia Excuse**: Use active inertia value from Phase 1 active values. Use scout override if available; otherwise use SIGNAL DEFAULTS value exactly.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step. Pre-commit this value -- Phase 5 CTA uses it by exact reference.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief -- substantively distinct from Dev and Maker beliefs] | [Name the pitch outcome failure] | [active Exec inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Dev | [Write belief -- substantively distinct from Exec and Maker beliefs] | [Name the pitch outcome failure] | [active Dev inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Maker | [Write belief -- substantively distinct from Exec and Dev beliefs] | [Name the pitch outcome failure] | [active Maker inertia from SIGNAL DEFAULTS] | [Name the counter action] |

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Consumes*: Phase 1 active values.
*Produces*: **POSITIONING LOCK** (named output). Phase 5 references this output by exact name.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
3. **Ruling out**: Three categories Signal is NOT. Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Produces*: **EXEC OPENING SENTENCE** (named output).

**Write: EXEC OPENING SENTENCE**
> [One sentence only.]

**Binary gate:** Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?
- **YES** -- locked. Proceed to Phase 5.
- **NO** -- rewrite. Anchor in active Exec inertia. Re-apply gate. Repeat until YES.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes*:
- **AUDIENCE BELIEF MAP**
- **POSITIONING LOCK**
- **EXEC OPENING SENTENCE**

Draft order: Maker first, then Dev, then Exec.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

**Maker Version** *(draft first)*
- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Inertia arc from AUDIENCE BELIEF MAP Maker row. Maker outcome from SIGNAL DEFAULTS. No jargon.
- **Call to Action**: CTA template, maker row.

**Dev Version** *(draft second)*
- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`.
- **Why It Matters**: Inertia arc from AUDIENCE BELIEF MAP Dev row. Before-state and after-state named. Dev friction from SIGNAL DEFAULTS.
- **Call to Action**: CTA template, dev row.

**Exec Version** *(draft last)*
- **Hook**: EXEC OPENING SENTENCE -- exact text, no edits.
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: Inertia arc from AUDIENCE BELIEF MAP Exec row. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK]." 2-3 sentences ROI framing.
- **Call to Action**: CTA template, exec row.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category. Minimum four bullets. Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

**-- PHASE 6 COMPLETE. --**

---

**Output format**: `## Exec Version` / `## Dev Version` / `## Maker Version` / `## What Signal Is NOT`

Phase outputs are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## What Made It Golden

Five patterns -- accumulated across 12 rounds -- separate R12 V-01 from an unconstrained pitch generator:

**1. SIGNAL DEFAULTS table loaded unconditionally before intake (C-12/C-13)**
A full defaults table appears at the top of the skill, before any signal intake or branching. Every run has a complete set of active values regardless of whether scout artifacts exist. No conditional loading, no "if signal not found, skip." The table guarantees C-09 (inertia-as-competitor) and C-03 (exec outcome-first) pass unconditionally on the first run against any new topic.

**2. Three-node named dependency chain (C-14/C-16)**
AUDIENCE BELIEF MAP, POSITIONING LOCK, and EXEC OPENING SENTENCE are each assigned a name at the point of creation and cited by that exact name in every downstream step. The data flow is readable from skill structure alone -- you can trace the provenance of every Phase 5 input without executing the prompt. A broken reference is structurally visible, not silently ignored.

**3. Phase 2 BINDING DECLARATION with exhaustiveness closure (C-25/C-26/C-27)**
*(Full scored version only -- R12 V-01 in variations file)*
Before any row of the AUDIENCE BELIEF MAP is filled, an explicit table declares which SIGNAL DEFAULTS fields bind to which BELIEF MAP columns. The declaration closes with: "No other DEFAULTS fields are directly bound to BELIEF MAP columns" (exhaustiveness) and "Phase 5 does not read SIGNAL DEFAULTS inertia fields directly" (downstream access prohibition). The data flow is auditable from skill structure alone without tracing execution.

**4. Binary gate with embedded rewrite loop (C-10)**
The exec opening sentence is written, tested against a single binary criterion (cost/risk/productivity consequence without naming a feature or product), and rewritten in a loop -- all before Phase 5 begins. The gate is not a post-draft checklist. EXEC OPENING SENTENCE cannot reach Phase 5 without passing. The loop is embedded in Phase 4 so a model that skips the gate produces a broken downstream reference, not a degraded output.

**5. Audience belief mapping as pre-condition for argument construction (C-15)**
The 12-cell AUDIENCE BELIEF MAP (Core Belief + Failure Mode + Inertia Excuse + Inertia Counter for each of Exec, Dev, Maker) is completed and locked before any version is drafted. Each pitch version draws its Hook, Why-It-Matters, and CTA from pre-committed BELIEF MAP values -- not from structural slot-filling. The constraint-ascending draft order (Maker first) ensures plain-language coherence is established before specialized framing is added.

---

## Final Rubric Criteria Summary

**Rubric**: `draft-pitch-rubric-v11-2026-03-14.md` | **Aspirational denominator**: 38 | **R12 V-01 score**: 100.0

### Essential (60% weight) — 4/4

| ID | Criterion | R12 V-01 |
|----|-----------|----------|
| C-01 | All three versions present | PASS |
| C-02 | Each version has all four elements | PASS |
| C-03 | Exec version outcome-first with ROI framing | PASS |
| C-04 | Anti-positioning section present | PASS |

### Recommended (30% weight) — 3/3

| ID | Criterion | R12 V-01 |
|----|-----------|----------|
| C-05 | Dev version shows the tool, not the business case | PASS |
| C-06 | Maker version is jargon-free | PASS |
| C-07 | Prior signals consulted | PASS |

### Aspirational (10% weight) — 38/38

| ID | Pattern | R12 V-01 |
|----|---------|----------|
| C-08 | Proof points are specific and traceable | PASS |
| C-09 | Competitive framing names inertia as primary competitor | PASS |
| C-10 | Exec self-check embedded at generation time | PASS |
| C-11 | Positioning answers locked in writing before prose | PASS |
| C-12 | Default fallback values provided for missing signals | PASS |
| C-13 | DEFAULTS TABLE loaded unconditionally before intake | PASS |
| C-14 | Gate output named and cited by downstream instruction | PASS |
| C-15 | Audience belief mapping precedes argument construction | PASS |
| C-16 | Multi-node named dependency chain across gate outputs | PASS |
| C-17 | Inertia Counter pre-committed in Phase 2 for Phase 5 CTA | PASS |
| C-18 | CTA uses exact Inertia Counter value, not paraphrase | PASS |
| C-19 | Column definitions include pass/fail distinction | PASS |
| C-20 | Phase completion markers present and explicit | PASS |
| C-21 | Exec Hook sourced from named gate output | PASS |
| C-22 | Exec What-It-Does sourced from named POSITIONING LOCK | PASS |
| C-23 | BINDING DECLARATION appears before table fill | PASS |
| C-24 | Binding table names source field and destination column | PASS |
| C-25 | Exhaustiveness closure on binding declaration | PASS |
| C-26 | Downstream access prohibition explicit | PASS |
| C-27 | Meta-purpose auditability statement present | PASS |
| C-28 | Draft order declared before version sections | PASS |
| C-29 | Maker version drafted first (constraint-ascending) | PASS |
| C-30 | INERTIA PROFILE pre-commit before any draft | PASS |
| C-31 | INERTIA PROFILE sourced from AUDIENCE BELIEF MAP | PASS |
| C-32 | VERSION DIFFERENTIATION GATE present | PASS |
| C-33 | Gate table covers all three versions | PASS |
| C-34 | Gate questions are binary YES/NO | PASS |
| C-35 | Gate enforces rewrite on failure | PASS |
| C-36 | Why-It-Matters sources inertia arc from locked phase output | PASS |
| C-37 | Exec Why-It-Matters names inertia-as-competitor explicitly | PASS |
| C-38 | PHASE 5 STRUCTURE block present and read-before-draft | PASS |
| C-39 | Draft-order integrity paragraph present | PASS |
| C-40 | Gate cites advisory text, not paraphrase | PASS |
| C-41 | Phase structure cites and declares at declaration site | PASS |
| C-42 | Integrity scope names canonical output set | PASS |
| C-43 | Gate questions cite exact canonical advisory text | PASS |
| C-44 | Heading-line compound colocation | PASS |
| C-45 | Targeted variation scoping -- zero prior-phase regression | PASS |

### Score

```
Score = (4/4)*60 + (3/3)*30 + (38/38)*10 = 100.0
```
