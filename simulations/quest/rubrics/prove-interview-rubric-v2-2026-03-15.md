Done. Here's the complete v2 rubric:

---

**prove-interview Rubric — v2**
`(E/5 x 60) + (R/3 x 30) + (A/4 x 10)` | PARTIAL = 0.5

**5 essential (C-01..C-05)** — unchanged, but C-05 clarified:
- C-05 now requires the exact vocabulary `SURPRISING (expected: X, got: Y)` / `CONFIRMING (validates: Z)`. R1 showed all five variations used the wrong label format — this is the fix.

**3 recommended (C-06..C-08)** — unchanged, but C-08 note updated:
- Prose-embedded taxonomy is now explicitly accepted (no table required).

**4 aspirational (C-09..C-12)** — C-11 and C-12 added:

| ID | Criterion | Source |
|----|-----------|--------|
| C-09 | Cross-interview synthesis | v1 |
| C-10 | Simulation fidelity annotated | v1 (note updated: reflective-invitation form accepted) |
| C-11 | **Voice divergence acknowledged** | V-03 signal: "don't let them all sound like the same AI wrote them" |
| C-12 | **Follow-up origin visible** | V-03 signal: "let their answer take you somewhere you didn't plan to go" |

The two new criteria test for *meta-awareness* rather than output structure: C-11 proves the author was managing voice intentionally, C-12 proves the follow-up was triggered by the actual answer rather than prepared in advance.
lary gap -- the label must be SURPRISING or CONFIRMING with an explicit prior-expectation link (format: `SURPRISING (expected: X, got: Y)` or `CONFIRMING (validates: Z)`).

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Persona identity declared** | correctness | essential | Each subject's identity is declared before the interview begins -- role, title, or function is explicit. Anonymous or role-free subjects fail. |
| C-02 | **Prior knowledge scoped** | correctness | essential | Each subject's prior knowledge and blind spots are stated before answers are given -- what they know, what they don't know, what they care about. A subject with no prior knowledge section fails. |
| C-03 | **Answers in persona voice** | behavior | essential | Answers are written in the declared persona's distinct voice -- vocabulary, concerns, and framing match the role. Answers that could belong to any persona (generic AI output) fail. |
| C-04 | **Evidence explicitly extracted** | coverage | essential | At least one concrete evidence item (insight, concern, requirement, contradiction, or signal) is explicitly extracted per subject -- not left implicit in the dialogue. Evidence listed only inside the transcript without a dedicated extraction phase or section fails. |
| C-05 | **Surprising or confirming moment labeled** | depth | essential | Each subject includes at least one moment labeled SURPRISING or CONFIRMING, tied to an explicit prior expectation. Required format: `SURPRISING (expected: X, got: Y)` or `CONFIRMING (validates: Z)`. Unlabeled interesting moments and labels without prior-expectation links do not count. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Questions probe declared concerns** | depth | recommended | Questions are anchored to the subject's declared role and prior knowledge -- they probe role-specific concerns, not generic topics. At least one follow-up question appears in response to a prior answer within the same interview. |
| C-07 | **Multiple distinct personas** | coverage | recommended | At least two subjects are present with meaningfully different roles, knowledge levels, or priorities -- not minor variations of the same profile. A single subject or near-identical subjects fail. |
| C-08 | **Evidence signal-typed** | behavior | recommended | Each extracted evidence item carries a signal type label (e.g., adoption risk, feasibility concern, requirement gap, scope signal, constraint) making its downstream use in the topic narrative explicit. Labels may appear in prose form or table columns -- either is accepted. Unlabeled evidence items fail. |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-interview synthesis** | depth | aspirational | After all interviews, a synthesis section aggregates findings across subjects -- naming patterns, contradictions, or convergences and connecting individual evidence items into a composite signal. (N/A when N=1 subject.) |
| C-10 | **Simulation fidelity annotated** | behavior | aspirational | The output includes a brief meta-note distinguishing grounded claims (based on documented persona knowledge or domain context) from constructed plausibility, naming at least one specific basis. Framing as a reflective invitation ("one last thing") or as a structural section both count -- the test is presence and specificity, not form. |
| C-11 | **Voice divergence acknowledged** | behavior | aspirational | The output includes a meta-observation naming at least one concrete contrast in how two subjects were made to sound different -- citing a specific vocabulary choice, framing preference, or concern priority that distinguishes them. Generic statements ("they had different roles") without citing a specific voice difference fail. |
| C-12 | **Follow-up origin visible** | depth | aspirational | Each follow-up question references a specific moment from the preceding answer -- quoting or explicitly pointing to what the subject just said that prompted the new question. Follow-ups that could appear in any order (not anchored to prior content) fail. |

---

## Scoring Reference

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass + composite >= 80 | Golden -- meets threshold |
| All C-01..C-05 pass + composite < 80 | Passing essential, weak on recommended/aspirational |
| Any C-01..C-05 fail | Below threshold regardless of composite |

---

## Notes

- A "persona" here is a simulated human stakeholder or customer -- not a UI persona or product feature walkthrough. C-03 requires answers to reflect the simulated human's perspective, concerns, and blind spots.
- C-05 requires both the label (SURPRISING / CONFIRMING) and an explicit prior-expectation link. R1 showed a universal vocabulary gap: all five variations marked notable moments without meeting either requirement. The minimum passing form is `SURPRISING (expected: X, got: Y)` or `CONFIRMING (validates: Z)`.
- C-08 (signal-typed evidence) is the bridge to the topic namespace: typed evidence can be consumed by `/topic:` skills directly. Prose embedding is accepted -- the test is whether the signal type is named, not whether it appears in a table.
- C-09 is N/A for single-subject runs; exclude from the aspirational denominator to avoid penalizing intentionally focused interviews. With C-09 N/A, use `(A/3 x 10)`.
- C-10: V-03 demonstrated that a reflective "one last thing" invitation reliably produces fidelity annotation where structural phase requirements are skipped. Either framing counts as long as it names a specific grounding basis.
- C-11 was derived from the V-03 excellence signal: "Don't let them all sound like the same AI wrote them." The meta-observation naming a concrete voice difference is itself the excellence signal -- it proves the author was managing voice intentionally, not by accident.
- C-12 was derived from the V-03 excellence signal: "Let their answer take you somewhere you didn't plan to go." The trigger must be visible in the question text. A follow-up that doesn't show what prompted it could have been written before the interview started.
