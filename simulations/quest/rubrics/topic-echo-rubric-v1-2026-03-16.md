---
skill: quest-rubric
skill_target: topic-echo
date: 2026-03-16
version: 1
---

# topic-echo — Scoring Rubric v1

## Skill Definition

`topic:echo` synthesizes unexpected findings after all essential signals are gathered.
It asks exactly one question: **"What did we learn that we did not expect?"**

It is not a summary of findings. It is a synthesis of surprises. Each surprise must be
named, traced to its source signal, and assessed for impact on the design direction.
The artifact is institutional memory — written for the next team that walks this path,
not a retrospective for the team that just finished.

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. If any essential criterion fails, the output is not useful.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Named surprises present** | correctness | At least one surprise is named as a discrete item. A surprise is not a finding — it must be framed as something unexpected: the output must make clear what was anticipated and why the actual result departed from it. A list of findings without surprise framing fails this criterion entirely. NOT: "We found that X matters" (finding). PASS: "We expected X to be negligible; it turned out to dominate" (surprise). |
| C-02 | **Signal tracing per surprise** | correctness | Every named surprise is traced to a specific source signal or artifact by name. Generic attribution ("the evidence showed") is insufficient. Each surprise must name the artifact that produced it (e.g., a specific namespace output, interview result, prototype run). A surprise without a traceable source cannot be audited by the next team and fails. |
| C-03 | **Design impact assessed per surprise** | depth | Every named surprise carries an explicit assessment of its impact on design direction. Impact may be confirming (validates current direction), redirecting (changes a decision), or destabilizing (opens a previously closed question). An impact statement that does not identify which design decision is affected fails. "This changes things" without naming what changes is insufficient. |
| C-04 | **Synthesis not summary** | behavior | The artifact does not summarize all findings. It contains only surprises and their analysis. If expected findings appear, they are either absent or explicitly marked as context-only (not presented as output items). An artifact that enumerates findings and labels some "interesting" does not satisfy this criterion — the surprise/expected partition must be explicit and structural. NOT: a summary section followed by a "highlights" section. PASS: a document whose every entry is framed as a surprise with a departure-from-expectation statement. |
| C-05 | **Surprise specificity** | correctness | Each surprise is specific to this topic's signal set, not a generic observation that could appear in any investigation. "APIs are harder to design than expected" fails — it applies universally. "The scout:competitors signal revealed that all three competitors treat X as a solved problem, contrary to our assumption that the space was unsolved" passes — it is falsifiable against this investigation's artifacts. |

---

## Recommended Criteria (weight: 30 points total, 10 pts each)

Output is better with these. Golden typically requires at least 2 of 3.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Expectation counterfactual** | depth | Each surprise explicitly names what was expected versus what was found. The counterfactual structure ("We expected X; we found Y") is stated, not implied. A reader new to the topic can reconstruct the prior assumption from the surprise entry alone, without consulting the underlying signal artifacts. Surprises that omit the expected-state half are incomplete — they describe the finding but not the departure. |
| C-07 | **Institutional framing** | behavior | The artifact is explicitly addressed to a future team, not the current one. At least one element signals forward-facing intent: the surprises are framed as "things you would not predict from the artifacts alone," a closing note names what the next team should investigate first given these surprises, or the opening declares the institutional purpose. An artifact that reads as a personal retrospective without forward framing fails this criterion. |
| C-08 | **Cross-signal pattern identification** | coverage | If two or more surprises share an underlying cause or implication, that relationship is named. The pattern identification goes beyond listing — it states what the surprises have in common and what that pattern implies for the design. If all surprises are genuinely independent, the output explicitly states this. Omitting pattern analysis when multiple surprises exist is a fail; "these surprises are unrelated" with a brief rationale is a pass. |

---

## Aspirational Criteria (weight: 10 points total, 5 pts each)

Raise the bar once essential and recommended criteria are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Surprise hierarchy by design impact** | depth | The surprises are ranked by design impact, with an explicit rationale for the ranking. The ranking is argued ("this surprise outranks the others because it affects the X decision which is load-bearing for the architecture") not asserted. A ranked list without argument is insufficient — the hierarchy must be defensible to a reader who disagrees with it. |
| C-10 | **Riskiest surprise flagged** | behavior | The single surprise most likely to invalidate a core assumption is explicitly flagged with a warning. The flag names the assumption at risk, the signal that revealed it, and what would need to be true for the assumption to hold despite the surprise. An artifact that surfaces surprises without escalating the most dangerous one misses its highest-value contribution to the next team. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 80 |
| Passing | All essential pass, composite < 80 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 10 points total (2 criteria, 5 points each)
- Max composite: 100

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 1/2 pass -> 1/2 * 10 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall

### Golden path (baseline)

- Essential: 5/5 -> 60
- Recommended: 2/3 -> 20
- Aspirational: 0/2 -> 0
- **Composite = 80** -- golden (all essential + composite >= 80)

### Golden path (full)

- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 2/2 -> 10
- **Composite = 100** -- maximum

---

## Criterion Relationships

**C-01 / C-04 relationship**: C-01 requires at least one named surprise with departure framing.
C-04 requires that the artifact contains *only* surprises -- no unsegregated summary content.
Both must pass together: an artifact can have named surprises (C-01) while burying them in a
summary (C-04 fail), or can contain only surprise entries but without departure framing (C-01 fail).

**C-02 / C-05 relationship**: C-02 requires tracing to a named source artifact. C-05 requires
specificity to this investigation. Both are independently verifiable: an artifact can cite a
specific source (C-02 pass) but describe a generic observation not derived from that source's
content (C-05 fail). The highest-quality surprises satisfy both.

**C-06 / C-07 tension**: C-06 (expectation counterfactual) is oriented backward -- reconstructing
the prior state. C-07 (institutional framing) is oriented forward -- addressing the next team.
An artifact that does both anchors the surprise in history and projects it into the future.
An artifact that does only one is still useful but not fully realized.

**C-09 / C-10 relationship**: C-09 requires ranking all surprises. C-10 requires flagging the
most dangerous one. C-09 can be satisfied without C-10 (all surprises ranked but none escalated
as risk). C-10 requires identifying the riskiest surprise but does not require ranking the others.
The highest-quality artifacts satisfy both.
