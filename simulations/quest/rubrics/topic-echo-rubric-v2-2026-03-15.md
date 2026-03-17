Done. Here is the complete updated rubric — `topic-echo-rubric-v2-2026-03-15.md`.

---

## What changed and why

**Three new aspirational criteria extracted from Round 1 excellence signals:**

### C-10 | Epistemic Delta Tracing
*Source: V-04 R1*

V-04's Archaeologist/Chronicler split was the highest-performing C-01 mechanism because it forced explicit prior-assumption surfacing *before* the gate ran. The excellence pattern: at least one surprise entry names what was believed before the signal arrived — not just the finding, but the delta from prior belief. "We assumed X; signal showed Y; therefore Z changes." C-02 traces *where* the signal came from. C-10 traces *what belief it overturned*.

### C-11 | Confirmation Accounting
*Source: V-03 R1*

V-03's "CONFIRMATION → Release it → topic-story" routing was the key mechanism that made the inversion *provable* rather than assumed. Without this, a reviewer can't tell whether the gate ran or was skipped. The excellence pattern: the output explicitly names at least one reviewed-and-rejected item, classifying it as a confirmation and stating its destination. Gate proof requires showing what was excluded.

### C-12 | Collective Next-Team Signal
*Source: V-04 R1*

V-04 was the only variation that asked "what do the surprises tell the next team *collectively*?" — and that question produced output distinct from C-06 (individual durable register) and C-08 (cross-signal mechanics). The excellence pattern: a dedicated synthesis block whose content is non-derivable from reading the individual surprises in sequence. The next team should be able to read only the collective block and have an accurate orientation.

---

**Formula update:** aspirational denominator changes from `/ 2` to `/ 5`. Max composite remains 100. Each full aspirational pass is now worth 2 pts (vs. 5 pts in v1). The tier stays a ceiling bonus, not a score driver.
s interesting" or omits consequences fails this criterion.

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

### C-10 | Epistemic Delta Tracing
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one surprise makes the belief-before-signal explicit. Not just "the signal showed X" but "we assumed Y before this signal; the signal showed X; this changes Z." The prior assumption is named, not implied.
- **Pass condition**: At least one surprise entry contains an explicit prior assumption ("we believed...", "the design assumed...", "prior to this signal, the expectation was...") and traces the delta from that assumption to the finding. Entries that state the finding alone -- even with strong source tracing (C-02) -- do not satisfy this criterion.
- **Source**: V-04 R1 excellence. The Archaeologist/Chronicler split forced prior-assumption surfacing before gate application. Made the epistemic shift structural rather than optional.

### C-11 | Confirmation Accounting
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The output demonstrates gate enforcement by naming at least one signal reviewed and classified as a *confirmation* -- not a surprise -- and stating where it belongs. Silence about confirmations does not prove the gate ran.
- **Pass condition**: The output explicitly names at least one artifact or finding that was reviewed, passed through the surprise gate, and classified as a confirmation. The intended destination for that confirmation is stated (e.g., "this belongs in topic-story, not here"). A reviewer cannot distinguish a rigorous gate from an absent gate if only passing items appear.
- **Source**: V-03 R1 excellence. The CONFIRMATION -> Release it path routing to topic-story made inversion visible. Variations that omit rejected items leave gate status unverifiable.

### C-12 | Collective Next-Team Signal
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The synthesis concludes with a statement of what the surprises mean *together* for the next team -- an emergent collective takeaway that cannot be derived from reading the individual surprises in sequence. This is distinct from C-06 (per-entry durable register) and C-08 (cross-signal mechanics).
- **Pass condition**: The output contains a dedicated synthesis block (titled or clearly demarcated) that frames the collective lesson. A reader who read only this block -- without the individual surprises -- must come away with a meaningfully accurate understanding of the topic's signal landscape. Restating individual surprises as a numbered list does not satisfy this criterion.
- **Source**: V-04 R1 excellence. "What do the surprises tell the next team collectively?" was the only variation where next-team framing appeared in the synthesis section. Identified as the PASS case for C-06 that per-entry register alone cannot achieve.

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

PARTIAL counts as 0.5 pass toward formula. FULL PASS required for `all_essential_pass` boolean.

**Golden threshold**: All 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential | Institutional memory -- ready to hand off |
| Silver | >= 65, all essential | Useful but needs depth on impact or framing |
| Bronze | >= 50, all essential | Structurally valid but thin -- more surprises needed |
| Fail | any essential miss | Not a valid echo -- rerun skill |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 9 criteria (4 essential / 3 recommended / 2 aspirational) |
| v2 | 2026-03-15 | +C-10 Epistemic Delta Tracing, +C-11 Confirmation Accounting, +C-12 Collective Next-Team Signal. Aspirational tier: 2 -> 5 criteria. Formula denominator updated from 2 to 5. |
