## Quest Score — topic-achievements R1

**Scoring basis**: Prompt design analysis against rubric criteria (no trace artifact — evaluated by structural fidelity to rubric pass conditions).

---

## V-01 — Role Sequence: Scanner → Classifier → Synthesizer

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | One state per achievement | PASS | "Assign exactly one state" explicitly stated in Role 2; no-dual-state constraint enforced |
| C-02 | Falsified named as honesty signal | PASS | "Falsified must appear as its own block. It must not be embedded in the category loop above." — structural isolation enforced |
| C-03 | EARNED/IN-PROGRESS cite real artifacts | PASS | Role 1 creates closed inventory; "No EARNED or IN-PROGRESS entry may cite an artifact not in the Role 1 inventory" — ground truth locked before classification |
| C-04 | IN-PROGRESS shows numeric ratios | PASS | "show a numeric ratio (e.g., '3 of 5 namespaces')" explicitly required for IN-PROGRESS state |
| C-05 | Next action is specific | PASS | "Name one specific skill to invoke, the artifact type it produces, and the achievement it advances. State the current-to-target transition. Generic instructions not acceptable." |
| C-06 | All 7 categories present | PASS | "All 7 categories must appear. If a category has no applicable achievements, write: 'No achievements yet — [unlock condition].'" |
| C-07 | EARNED entries carry dates | PASS | "cite the artifact(s) from Role 1 and the ISO date earned" |
| C-08 | LOCKED entries state unlock conditions | PASS | "state the unlock condition (what artifact type, what count, what action)" |
| C-09 | Maturity synthesis precedes per-category detail | **FAIL** | Synthesis is in Role 3, which executes **after** Role 2 (per-category classification). Rubric requires synthesis to precede or open the per-category detail. The role sequence inverts the required order. |
| C-10 | Falsified framed as positive signal | PASS | LOCKED text: "This achievement is waiting for you… Retracting a belief is the reward, not the penalty." — explicitly positive in all states |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 1/2 → 5  
**Composite: 95** | All essential pass: YES | Band: Gold

---

## V-02 — Output Format: Table-Primary Grid

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | One state per achievement | PASS | Table column enforces "exactly one of EARNED, IN-PROGRESS, LOCKED. One value per row." — mechanically checkable at a glance |
| C-02 | Falsified named as honesty signal | PASS | "Falsified is not a category — it is the intellectual honesty signal and the most important achievement in the plugin. Render it as a standalone block." |
| C-03 | EARNED/IN-PROGRESS cite real artifacts | PASS | "no EARNED or IN-PROGRESS Evidence cell may name an artifact not found in Step 1" + fallback: "If unsure, write the namespace only" (prevents forced hallucination) |
| C-04 | IN-PROGRESS shows numeric ratios | PASS | Evidence column requires "numeric ratio (e.g., '4/9 namespaces')"; "Vague qualifiers ('almost there') are not acceptable" |
| C-05 | Next action is specific | PASS | Explicit format: "Invoke /[skill-name] to produce a [artifact-type] artifact. This advances [category] from [current state] to [target state]…" |
| C-06 | All 7 categories present | PASS | "All 7 must appear. If a category has no achievements at all, include a row with — in Achievement and LOCKED in State." |
| C-07 | EARNED entries carry dates | PASS | "Date: ISO date for EARNED entries. Blank for IN-PROGRESS and LOCKED." |
| C-08 | LOCKED entries state unlock conditions | PASS | Evidence column for LOCKED: "the unlock condition — artifact type, count, or action required" |
| C-09 | Maturity synthesis precedes per-category detail | PASS | Step 4: "This paragraph must appear before or immediately after the table — not buried at the end." Prohibits afterthought placement; "before" satisfies the criterion |
| C-10 | Falsified framed as positive signal | PASS | "If EARNED: frame as a mark of rigorous inquiry — following the evidence is what earned this. If LOCKED: frame as an open invitation — the achievement is waiting…" |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 2/2 → 10  
**Composite: 100** | All essential pass: YES | Band: Gold

---

## V-03 — Lifecycle Emphasis: Phase-Gated with Hard Boundaries

**Status**: Partial prompt only — Phase 1 (SCAN) structure visible; Phases 2-N not provided in this document.

Scoring from what is present + hypothesis:

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | One state per achievement | EST-PASS | Phase-gated classification phases enforce mandatory gate outputs — state discipline expected |
| C-02 | Falsified structural isolation | EST-PASS | Hypothesis explicitly targets: "prevent the model from compressing or skipping the Falsified structural check when in list-completion mode" — a dedicated phase would enforce this |
| C-03 | Artifact-grounded classification | EST-PASS | Phase 1 SCAN creates closed inventory with mandatory gate output before Phase 2 proceeds — anti-hallucination by construction |
| C-04 | IN-PROGRESS numeric ratios | UNKNOWN | Phase 2 content not visible |
| C-05 | Specific next action | UNKNOWN | Final phase content not visible |
| C-06 | All 7 categories | UNKNOWN | Phase 2 structure not visible |
| C-07 | EARNED dates | UNKNOWN | Phase 2 structure not visible |
| C-08 | LOCKED unlock conditions | UNKNOWN | Phase 2 structure not visible |
| C-09 | Synthesis precedes detail | EST-PASS | Hypothesis: "force the maturity paragraph to exist as a discrete artifact rather than an afterthought" — suggests synthesis phase placed before classification phases |
| C-10 | Falsified positive framing | UNKNOWN | Falsified phase content not visible |

**Composite: INCOMPLETE — cannot score** | Projected band: Gold (if remaining phases match hypothesis intent)

---

## V-04, V-05

Not present in this document. Cannot score.

---

## Ranking (complete variations only)

| Rank | Variation | Composite | All Essential | Band |
|------|-----------|-----------|---------------|------|
| 1 | V-02 (Table-Primary Grid) | 100 | YES | Gold |
| 2 | V-01 (Role Sequence) | 95 | YES | Gold |
| — | V-03 (Phase-Gated) | Incomplete | — | — |
| — | V-04, V-05 | Not provided | — | — |

---

## Excellence Signals

**From V-02 (top scorer):**

1. **Table-column state enforcement** — putting State in a dedicated column makes C-01 mechanically verifiable at a glance. The model cannot bury dual states in prose. Structure does the validation work.

2. **Synthesis placement boundary rule** — V-02 doesn't just require synthesis; it specifies position: "before or immediately after the table — not buried at the end." A placement rule is stronger than a presence rule. It directly prevents the most common degradation (synthesis as closing paragraph afterthought).

3. **Hallucination escape hatch** — "If unsure, write the namespace only" gives the model a safe fallback that doesn't force fabrication. Most prompts either demand full artifact citation (risking hallucination) or say nothing. V-02 threads the needle.

**From V-01 (strong on anti-hallucination):**

4. **Closed-inventory pipeline** — Role 1 creates a numbered artifact list that Role 2 is contractually constrained to. This is the strongest C-03 design: the model cannot classify what it hasn't inventoried. V-02's Step 1 has this too, but V-01's explicit "cite by name or namespace — no invented references" constraint is more emphatic.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table-column-state-enforcement", "synthesis-placement-boundary-rule", "hallucination-escape-hatch"]}
```
