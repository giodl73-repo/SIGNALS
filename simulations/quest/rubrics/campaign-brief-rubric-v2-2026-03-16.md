Reading the scorecard evidence carefully for patterns not yet captured in C-01–C-10.

**Three excellence signals across V-01–V-04:**

1. **V-04 / C-07 PASS** — strongest gap prioritization came from *inertia framing* ("what happens if we commit without this signal?"), not just labeling. Grounding in commit-risk is a distinct technique from mere blocking/optional labeling.

2. **V-05 structure** — prose confined to one designated section (STORY); all other blocks are structured data. Prevents narrative drift into status sections. No existing criterion captures this discipline.

3. **V-02 / C-01 PASS** — "skipping produces obvious incompleteness" — the format is designed so silence *breaks* the pattern rather than passing silently. This is a structural enforcement property orthogonal to visual hierarchy (C-08).

---

```markdown
# Quest Rubric — campaign-brief — v2
**Date:** 2026-03-16  
**Previous:** v1 (10 criteria)  
**Changes:** Added C-11, C-12, C-13 from Round 1 excellence signals

---

## Rubric Purpose

Evaluate skill variations for the `campaign-brief` orchestration skill.
A `campaign-brief` output is a dashboard that tells the team what signals
exist, what is missing, and whether the topic is ready to commit. The core
diagnostic pair is C-02/C-03. The differentiator is C-04. If orchestration
over plain `topic-status` has no additional value, the skill fails.

---

## Scoring Scale

| Score | Meaning |
|-------|---------|
| PASS | Criterion fully met — structural or explicit evidence |
| PARTIAL | Criterion partially met — likely to emerge but not guaranteed |
| FAIL | Criterion absent or structurally impossible |

| Tier | Points (PASS) |
|------|---------------|
| Essential | 10 |
| Recommended | 10 |
| Aspirational | 10 |

---

## Tier 1 — Essential (C-01–C-05)
*Minimum for a useful output. Fail any of these and the output is not a dashboard.*

**C-01 — Sub-skills invoked in order**  
All four sub-skills (topic-status, scout, signal-check, topic-register or equivalent)
are invoked in a defined sequence. Execution order must be deterministic — implied
sequence is PARTIAL; structural enforcement (gates, named phases, block ordering) is PASS.

**C-02 — Existing signals enumerated by namespace**  
Signals found are listed per namespace, not summarized as "signals exist."
The output must be enumerable — a reader must be able to count signals by namespace
without re-running the skill.

**C-03 — Missing signals explicitly named**  
Gaps are named, not silenced. If a namespace has no signals, that absence must
appear as a named entry, not an omission. Silence on gaps is FAIL.

**C-04 — Narrative arc synthesizes signals together**  
The synthesis section interprets what the signals mean *together* — not a flat list
with a label. A list labeled "narrative" without cross-signal reasoning is PARTIAL.
The synthesis must answer: what story do these signals tell as a set?

**C-05 — Topic registered with name, date, intent**  
The topic is registered (or confirmed registered) with all three fields present.
Checking registration is PARTIAL. Performing registration as a required output is PASS.

---

## Tier 2 — Recommended (C-06–C-08)
*Separates good from adequate. Miss these and the output is technically complete but not actionable.*

**C-06 — Explicit readiness verdict**  
The output includes a terminal, named readiness verdict: ready / not ready / conditional.
A verdict that emerges in prose is PARTIAL. A named verdict block is PASS.

**C-07 — Gap list prioritized — blocking vs. optional**  
Gaps are split into blocking (commit-risk) and optional. Unlabeled gap lists are FAIL.
Labels without rationale are PARTIAL. See also C-11 for the commit-risk grounding upgrade.

**C-08 — Scannable dashboard with visual hierarchy**  
The output uses headers, tables, or named blocks to create visual separation between
sections. Dense prose is PARTIAL. A declared template or skeleton that enforces
the hierarchy is PASS.

---

## Tier 3 — Aspirational (C-09–C-13)
*Raise the bar once C-01–C-08 are stable. These distinguish excellent from good.*

**C-09 — Session delta**  
The output explicitly records what changed this session: signals added, gaps closed,
verdict shift. A delta slot in the output template is the structural form. Absent
delta mechanism is FAIL.

**C-10 — Narrative confidence level with rationale**  
The synthesis section includes an explicit confidence level (e.g., high / medium / low)
with a one-line rationale. Hedging language that implies uncertainty is PARTIAL.
A named confidence field is PASS.

**C-11 — Commit-risk framing for blocking gaps**  
*From V-04 Round 1 — strongest C-07 evidence.*  
Blocking gaps are grounded in decision exposure, not just labeled. Each blocking gap
answers: "what happens if we commit without this signal?" The inertia anchor
("we ship with this unknown") is the structural form. Categorical labels without
decision stakes reasoning are PARTIAL. This upgrades C-07 — a skill can PASS C-07
and FAIL C-11 if labels exist but commit-risk rationale is absent.

**C-12 — Prose confinement — narrative prose restricted to one named section**  
*From V-05 Round 1 — structural discipline pattern.*  
The output format confines narrative prose to exactly one designated section
(STORY, NARRATIVE, or equivalent). All other sections — STATUS, GAPS, VERDICT,
TOPIC — are structured data (tables, lists, named fields). Prose that drifts into
status or verdict sections is PARTIAL. Explicit template discipline that makes
prose-outside-STORY structurally impossible is PASS.

**C-13 — Structural incompleteness detection**  
*From V-02 Round 1 — phase gate pattern.*  
The output format is designed so that a skipped or empty section is visually
obvious — silence breaks the pattern rather than passing silently. Named slots
that must be filled, required-output checkpoints, or gate structures where
omission creates visible incompleteness qualify. A format where the model can
silently omit a section without detection is FAIL.

---

## Scoring Summary

| Tier | Criteria | Max |
|------|----------|-----|
| Essential | C-01–C-05 | 50 |
| Recommended | C-06–C-08 | 30 |
| Aspirational | C-09–C-13 | 50 |
| **Total** | | **130** |

*Note: Total increased from 100 to 130 with the addition of C-11–C-13.
Normalize to 100 for cross-round comparison: `score / 130 × 100`.*

---

## Design Notes

**Core diagnostic pair:** C-02/C-03 — what you have and what you're missing.  
**Synthesis differentiator:** C-04 — cross-signal reasoning, not a labeled list.  
**Commitment differentiator:** C-11 — gaps grounded in decision stakes, not labels.  
**Structural discipline:** C-12 (prose confinement) + C-13 (incompleteness detection)
work together — a well-structured output both confines narrative drift and makes
gaps visible without active inspection.

**Relationship between C-07 and C-11:**  
C-07 asks whether gaps are split into blocking/optional.  
C-11 asks whether blocking gaps are *grounded* in commit-risk reasoning.  
A skill can PASS C-07 and FAIL C-11. The reverse is not possible — C-11 PASS
implies C-07 PASS.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-16 | Initial — 10 criteria, 3 tiers |
| v2 | 2026-03-16 | Added C-11 (commit-risk framing), C-12 (prose confinement), C-13 (incompleteness detection) from Round 1 excellence signals |
```

---

**Three additions and why:**

- **C-11** captures the V-04 inertia pattern — the strongest C-07 performance came specifically from decision-stakes reasoning, not labeling. Worth separating so future rounds can distinguish "has labels" from "labels mean something."

- **C-12** captures V-05's structural discipline — confining prose to one section is a real design choice that prevents drift and is invisible in v1's criteria.

- **C-13** captures V-02's gate pattern — "skipping produces obvious incompleteness" is a property you can engineer into a skill, and it's orthogonal to visual hierarchy (C-08).

Note the max score shifts to 130. I included a normalization formula so Round 1 scores (scored against 100) remain comparable.
