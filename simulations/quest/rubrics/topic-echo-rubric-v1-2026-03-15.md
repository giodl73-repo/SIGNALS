---
skill: quest-rubric
skill_target: topic-echo
date: 2026-03-15
version: 1
---

# Scoring Rubric: topic-echo

Skill: Synthesize unexpected findings after all essential signals are gathered. Each surprise is named, traced to its source signal, and assessed for design impact. The output is institutional memory for the next team.

---

## Essential Criteria (60 pts total -- must all pass)

### C-01 | Surprise Orientation
- **Weight**: essential
- **Category**: correctness
- **Text**: The output synthesizes *unexpected* findings only. It does not summarize expected outcomes, restate known hypotheses, or recap what the team set out to learn.
- **Pass condition**: Every item in the output is framed as something that contradicted, extended, or overturned a prior assumption. No item reads as a routine confirmation of a planned discovery. Reviewer should find zero items that could have been written before the signals were gathered.

### C-02 | Source Signal Tracing
- **Weight**: essential
- **Category**: correctness
- **Text**: Each surprise is anchored to a specific source signal artifact (e.g., flow-throttle, trace-permissions, scout-competitors). The trace is explicit -- named inline, not implied.
- **Pass condition**: Every surprise names at least one signal artifact by skill slug or file reference. A surprise with no traceable source fails this criterion regardless of content quality.

### C-03 | Design Impact Assessment
- **Weight**: essential
- **Category**: depth
- **Text**: Each surprise includes an explicit statement of how it affects the design direction -- what changes, what gets reconsidered, or what new constraint it imposes.
- **Pass condition**: Every surprise has a distinct "impact on design direction" clause. A surprise that names the finding and its source but says only "this is interesting" or omits consequences fails this criterion.

### C-04 | Named and Countable Surprises
- **Weight**: essential
- **Category**: format
- **Text**: Each surprise is a discrete, titled item. The output contains at least 2 surprises. A single observation is not a synthesis.
- **Pass condition**: Output has >= 2 surprises, each with a distinct name or title that can be referenced. An undifferentiated paragraph fails even if it contains multiple ideas.

---

## Recommended Criteria (30 pts total -- output better with these)

### C-05 | Surprise Diversity
- **Weight**: recommended
- **Category**: coverage
- **Text**: The surprises span meaningfully different dimensions -- not three variations on the same theme. Diversity might be across namespace (e.g., one from flow, one from prove, one from scout), or across concern type (behavioral, structural, adoption, constraint).
- **Pass condition**: No two surprises are drawn from the same root cause or the same signal cluster. Reviewer should not be able to collapse any two surprises into one without loss.

### C-06 | Future-Team Framing
- **Weight**: recommended
- **Category**: behavior
- **Text**: The document reads as institutional memory written *for* the next team, not as a personal reflection. Language is durable: it does not assume the current team's context and frames surprises as transferable lessons.
- **Pass condition**: A reader with no prior context on this topic can understand each surprise, its source, and its design implication without asking a follow-up question.

### C-07 | Impact Specificity
- **Weight**: recommended
- **Category**: depth
- **Text**: Design impact statements are concrete and falsifiable. "Changes how throttle decisions are sequenced" passes. "Might affect design" or "worth noting" fails.
- **Pass condition**: Each impact clause names a specific artifact, decision, constraint, or behavior that changes as a result of the surprise. Vague consequences do not pass.

---

## Aspirational Criteria (10 pts total -- raise the bar)

### C-08 | Cross-Signal Synthesis
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one surprise synthesizes a pattern visible only across *multiple* signals -- something no single signal would have revealed alone. This is the highest form of the echo: emergent insight from signal convergence.
- **Pass condition**: At least one surprise explicitly cites 2+ source signals and articulates why the surprise requires both to be visible. Single-source surprises, however well-written, do not satisfy this criterion.

### C-09 | Counterfactual Awareness
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one surprise includes a counterfactual: what decision would have been made, or what design would have been built, had this surprise not been discovered.
- **Pass condition**: At least one surprise contains an explicit "without this signal, we would have..." or equivalent clause that names a specific wrong turn that was avoided or a better path that was revealed.

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential | Institutional memory -- ready to hand off |
| Silver | >= 65, all essential | Useful but needs depth on impact or framing |
| Bronze | >= 50, all essential | Structurally valid but thin -- more surprises needed |
| Fail | any essential miss | Not a valid echo -- rerun skill |
