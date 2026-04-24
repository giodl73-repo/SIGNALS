---
skill: quest-rubric
skill_target: prove-topic
date: 2026-03-15
version: 1
---

# prove-topic — Scoring Rubric v1

**Skill**: `prove-topic`
**Description**: Orchestrates the full prove evidence campaign in one command: prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis → prove-synthesize. Reads prior scout signals to ground the hypothesis. Writes each artifact as it goes. Terminal output: synthesized evidence brief ready for topic-story.

---

## Essential Criteria (weight: 60 points total, 12 pts each)

Must all pass. Any essential fail = failing output.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **All five sub-skills execute** | behavior | Output shows evidence that all five stages ran: prove-hypothesis, prove-websearch, prove-intelligence, prove-analysis, prove-synthesize. Each stage produces visible output or a named artifact. Skipping any stage — even silently — is a fail. NOT: the output jumps directly to a synthesis without passing through intermediate stages. |
| C-02 | **Hypothesis grounded in scout signals** | correctness | Before the hypothesis is framed, the skill checks for existing scout artifacts for the topic. If scout artifacts exist, the hypothesis explicitly references at least one scout finding as its starting premise. If no scout artifacts exist, the skill notes this absence and proceeds from stated assumptions. NOT: hypothesis is written from scratch with no reference to scout signals even when scout artifacts are present in the topic directory. |
| C-03 | **Artifact written per stage** | behavior | Each sub-skill stage produces and writes a separate artifact to disk before the next stage begins. Artifact naming follows the convention `{topic}-{signal}-{date}.md`. NOT: all output is produced as a single terminal document with no intermediate artifacts written. NOT: intermediate artifacts are listed as "pending" and written only at the end. |
| C-04 | **Final synthesis is terminal and complete** | correctness | The last artifact produced is a prove-synthesize output — an answer-first brief with a confidence score, key evidence cited, and a judgment call (not a summary). The synthesis references findings from at least two of the preceding stages as named evidence. NOT: the campaign ends with a data-gathering artifact (analysis, websearch) as the final output. NOT: synthesis is present but reads as a restatement of intermediate artifacts without taking a position. |
| C-05 | **Topic prefix consistent across all artifacts** | format | All artifacts produced during the campaign share the same topic prefix. Naming follows `{topic}-{signal}-{date}.md` for each stage artifact. A reader can run `{topic}-*` to retrieve all artifacts from the campaign. NOT: artifact names are inconsistent, using different prefixes or no prefix across stages. |

---

## Recommended Criteria (weight: 30 points total, 10 pts each)

Output is better with these.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Stage order enforced** | behavior | Stages execute in the defined sequence: hypothesis first, synthesize last, with evidence-gathering stages (websearch, intelligence, analysis) in between. Each stage's output is available as input to later stages — specifically, the synthesis cites artifacts from the evidence-gathering stages by name. NOT: stages are run in arbitrary order with no dependency chain between outputs. |
| C-07 | **Scout signal handoff is explicit** | coverage | The hypothesis artifact names the specific scout artifact(s) it drew from (file path or artifact slug), and the websearch/intelligence stages note what the scout record contained vs. what they are adding. The chain from scout → hypothesis → evidence is traceable. NOT: the hypothesis mentions scout signals only in general terms ("based on prior research") without naming specific artifacts. |
| C-08 | **Synthesis signals readiness for topic-story** | format | The final synthesis artifact includes an explicit handoff statement or metadata indicating it is ready for consumption by `/topic:story` — e.g., a `ready_for_topic_story: true` frontmatter field, or a closing section headed "Handoff" naming the topic and the confidence verdict. NOT: synthesis concludes without any indication that the topic's evidence campaign is complete or what the downstream consumer should do with it. |

---

## Aspirational Criteria (weight: 10 points total, 5 pts each)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Thin-evidence acknowledgment propagates** | depth | If an evidence-gathering stage (websearch, intelligence, or analysis) produces thin or inconclusive results, later stages — including the synthesis — explicitly name this gap and adjust confidence accordingly. The synthesis does not project false confidence from a thin signal set. NOT: synthesis uses high confidence (>= 75) when one or more evidence stages returned no substantive findings without naming this as a structural limitation. |
| C-10 | **Progress narrated per stage** | behavior | Between each stage transition, the skill outputs a brief status line visible to the user (e.g., "prove-websearch complete — 3 signals found. Proceeding to prove-intelligence."). This lets the user follow campaign progress in real time without waiting for the terminal artifact. NOT: all output appears only after all stages complete, with no intermediate progress visible to the user. |

---

## Scoring

### Weights

| Tier | Points | Criteria | Per criterion |
|------|--------|----------|---------------|
| Essential | 60 | 5 | 12 pts |
| Recommended | 30 | 3 | 10 pts |
| Aspirational | 10 | 2 | 5 pts |
| **Max composite** | **100** | | |

### Formula

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
```

### Thresholds

| Result | Condition |
|--------|-----------|
| **Golden** | All C-01 through C-05 pass AND composite >= 80 |
| **Passing** | All essential pass, composite < 80 |
| **Failing** | Any essential criterion fails |

### Example score calculation

- Essential: 5/5 pass → 60
- Recommended: 2/3 pass → 20
- Aspirational: 1/2 pass → 5
- **Composite = 85** — Golden

- Essential: 4/5 pass → 48
- Recommended: 3/3 pass → 30
- Aspirational: 2/2 pass → 10
- **Composite = 88** — Failing (essential incomplete, C-0x fail overrides)

---

## Design Notes

**Why C-01 is essential**: An orchestrator that silently skips stages is worse than running a single prove-synthesize directly — it implies coverage it didn't provide. The first essential test is that the campaign actually ran.

**Why C-02 is essential**: The defining differentiation of prove-topic over manually running prove-hypothesis is that it bootstraps from existing context. If scout signals are ignored, the skill adds no value over a cold start.

**Why C-03 is essential**: "Writes each artifact as it goes" is in the skill description. A campaign with no intermediate artifacts cannot be resumed, inspected, or referenced by subsequent skills. Writing is not optional output formatting — it is the artifact lifecycle.

**C-06/C-07 tension**: C-06 (stage order enforced) is about dependency — does each stage consume the prior? C-07 (scout handoff explicit) is about traceability — can a reader follow the chain from scout signal to hypothesis to final verdict? Both can be satisfied independently.

**C-09 aspirational rationale**: Confidence inflation from thin evidence is the primary failure mode in orchestrated campaigns. When all five stages run but some produce nothing, a naive synthesis may still reach high confidence because the structure is complete. C-09 requires the thin-signal case be explicitly diagnosed — the same logic as prove-synthesize's record-specific anti-pattern diagnosis (C-17 in that rubric), applied at the campaign level.
