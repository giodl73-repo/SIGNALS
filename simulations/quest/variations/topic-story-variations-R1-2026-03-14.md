Written to `simulations/quest/variations/topic-story-variations-R1-2026-03-14.md`.

---

## Five Variations — Summary

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Phrasing register — imperative/direct | Hard imperatives leave no fallback to summarizing; the model must treat synthesis as the only valid path |
| **V-02** | Output format — typed template with constraints | Per-section field types and a one-row-per-signal table force selectivity before composition begins |
| **V-03** | Lifecycle emphasis — anti-summary priming | Opening with an extended description of the failure mode primes resistance to summarizing throughout, not just at the synthesis section |
| **V-04** | Role sequence + editorial voice | A named investigator stance + explicit read order (strategy before signals) produces stronger voice and keeps the original question in frame while reading evidence |
| **V-05** | Output format + lifecycle — two-pass structure | A mandatory scan pass (one extraction per signal, no writing) then a synthesis pass (write from extractions only) enforces selectivity structurally rather than by instruction |

**Key design tensions surfaced:**

- **V-01 vs V-03** test whether positive imperatives ("write this") or negative priming ("here is what you must not do") is the stronger anti-summary mechanism.
- **V-02 vs V-05** both use format to enforce selectivity, but differently: V-02 uses a table as a constraint within a single pass, V-05 uses a process gate (complete pass 1 before pass 2).
- **V-04** is the only variation that introduces a reader — "your team lead has ten minutes" — which tests whether audience awareness produces stronger editorial voice than structural instruction alone.

The C-09 aspirational criterion (causal logic in the pattern) is hardest to elicit. V-04 and V-05 both address it most directly: V-04 explicitly asks "why do the signals converge?" and V-05 separates "three signals agree" from "three signals agree because [reason]" as distinct required moves.
gnal findings. Draw the cross-signal conclusion — the insight that requires all the signals together to see. Name the pattern. Give it a label if you can. Explain why the signals converge, not just that they do.

If you find yourself writing "Signal A found X. Signal B found Y. Together this suggests Z" — stop. That is summarizing. Start over from the pattern itself.

### What Remains Uncertain

Name the open questions this investigation did not resolve. Be specific: what would a follow-on investigation need to ask? "More work is needed" is not an answer. Name the unknown.

### Recommendation

State one of: **proceed**, **pause**, **pivot**, or **abandon**.

Connect the verdict to the pattern you named above. Then specify the immediate action: who does what next, or what the decision gate is. A verdict without a next action is incomplete.

---

**Artifact**: `simulations/{topic}/{topic}-story-{date}.md`

Write the artifact. Do not describe what you are about to write. Write it.

---

## V-02 — Output Format: Typed Template with Constraints

**Axis**: Output format
**Hypothesis**: Providing explicit per-section constraints (word budget, typed field, format rule) forces selectivity before the model starts writing — it cannot inflate signal findings into mini-summaries when the format only allows one sentence per signal.

---

Synthesize all gathered signals for `{topic}` into a narrative artifact at `simulations/{topic}/{topic}-story-{date}.md`.

**Before writing:** Read `simulations/{topic}/strategy.md` to understand the investigation's original question. Then glob and read all `simulations/**/{topic}-*` artifacts. Identify: what question was each signal meant to answer, and what was the single most important finding from each.

**Output format** — use this template exactly:

```
# {Topic} Story
*{date} | {N} of {M} essential signals gathered*

## What We Set Out to Understand
[1-2 sentences. The original investigation question from strategy.md. Not findings — the question.]

## What the Signals Revealed
| Signal | Key Finding |
|--------|-------------|
| {signal-name} | [1 sentence — the single most important finding] |
| ...    | ...         |

## What the Signals Say Together
[3-5 sentences. Cross-signal synthesis only. Name the pattern explicitly in the first or second sentence: "The signals converge on [X]." Explain why — what shared assumption, constraint, or dynamic accounts for the convergence. Do not restate per-signal findings.]

**Pattern**: [one sentence that a reader can extract and quote]

## What Remains Uncertain
[2-4 sentences. Name at least one specific open question. Format: "We do not know [X] because [Y and Z signals gave conflicting results / no signal covered this angle]." Generic hedges ("more research may be needed") do not count.]

## Recommendation
**Verdict**: [proceed / pause / pivot / abandon]

[2-3 sentences. Connect the verdict to the named pattern above. Specify the immediate next action or decision gate. "Proceed" alone is not sufficient — say what to proceed to.]
```

**Constraints:**
- Signal table: one row per signal, one sentence maximum per finding. If you need more than one sentence, you are summarizing. Pick the single most important thing.
- Pattern section: must contain the words "The signals converge" or equivalent explicit naming — vague positivity ("signals are mostly aligned") fails.
- Recommendation: must reference the pattern by name or paraphrase. A verdict disconnected from the pattern is not grounded.

---

## V-03 — Lifecycle Emphasis: Anti-Summary Priming

**Axis**: Lifecycle emphasis
**Hypothesis**: Opening with an extended description of the failure mode (summarizing) before describing the task primes the model to treat synthesis as a constraint throughout — not just when reaching the "what signals say together" section.

---

Before you begin writing, understand what this skill is not.

**This is not a summary.** A summary of signals describes what each signal found. It reads like: "The scout-market signal found that the market is large. The scout-feasibility signal found that the integration is complex. The review-users signal found that users want the feature. Together these suggest we should proceed." That is a summary. It adds no analytical value. Any reader who had access to the signals could write it themselves.

**This is a story.** A story interprets. It asks: what do these signals mean together that none of them says alone? What is the shape of what we learned? What is the pattern that only emerges when you hold all the signals at once? The story tells the reader something they could not get by reading the signals individually.

The test: if every sentence in your "what the signals say together" section could have appeared in one of the source signals, you have written a summary. Start over.

---

Now write the story for `{topic}`.

**Read first:**
1. `simulations/{topic}/strategy.md` — what question were we trying to answer?
2. All `simulations/**/{topic}-*` artifacts — what did each signal reveal?

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md` with these sections:

**What We Set Out to Understand** — The investigation question, stated plainly. One or two sentences.

**What the Signals Revealed** — The key finding from each signal. One sentence per signal. Not a recap — the single most consequential thing that signal established. Brevity here is correctness.

**What the Signals Say Together** — The synthesis. Draw the cross-signal conclusion. Name the pattern. Explain why the signals converge, not just that they do. This section should contain at least one sentence that could not appear in any single signal artifact.

**What Remains Uncertain** — The open questions this investigation did not resolve. Specific, named unknowns. At least one question a follow-on investigation could actually address.

**Recommendation** — One of: proceed, pause, pivot, or abandon. Connected to the pattern. With a concrete next action.

---

A final check before you write: ask yourself whether the "what the signals say together" section would surprise a reader who had already read all the signals. If the answer is no — if the synthesis merely restates what any attentive reader already knew — revise until the answer is yes.

---

## V-04 — Role Sequence + Editorial Voice

**Axis**: Role sequence (strategy-first read order) + phrasing register (named investigator stance)
**Hypothesis**: Framing the author as a named investigator writing for a specific reader — before any structural instruction — produces stronger editorial voice and richer interpretation than abstract structural guidance alone. Read order is also made explicit: strategy before signals, so the question is held in mind while reading the evidence.

---

You are the lead investigator for `{topic}`. You have gathered signals from across the investigation. Now you are writing the story — a single document that tells your team lead what the investigation found and what to do about it.

Your team lead has ten minutes. They will not re-read the signals. What you write is what they know. Make it count.

**Read in this order:**

1. **Strategy first.** Read `simulations/{topic}/strategy.md`. Hold the original investigation question in mind. Everything you write will be an answer to that question or a revision of it.

2. **Signals second.** Glob and read all `simulations/**/{topic}-*` artifacts. For each, ask: what is the single finding that most changes or confirms my understanding of the investigation question? Note it.

3. **Write the story.** An editorial synthesis — not a transcript of what you read, but your interpretation of what it means.

---

**Structure of the artifact** (`simulations/{topic}/{topic}-story-{date}.md`):

**What We Set Out to Understand**
Restate the investigation question from strategy.md in your own words. One to two sentences. Anchor the reader before you tell them what you learned.

**What the Signals Revealed**
For each signal: one sentence. The key finding — not what the signal covered, but what it established. Write it as the investigator who read it, not as a cataloguer: "The feasibility signal settled the technical risk question — the API rate limits are not a blocker" not "The feasibility signal found that API rate limits are within acceptable range."

**What the Signals Say Together**
The interpretive core of the document. Step back from individual signals and ask: what shape does this evidence take? What pattern emerges? Name it. Then account for it — why do the signals converge here? What shared assumption or structural constraint explains the alignment (or tension)?

Write in the investigator's voice. "What's striking is..." / "The evidence forces a conclusion I didn't expect..." / "Three signals point in the same direction for the same underlying reason..." This section should feel like it was written by someone who has an opinion, not a system generating a report.

**What Remains Uncertain**
The honest accounting. What did the investigation not resolve? Name the specific unknowns — by signal gap, by conflicting result, by untested assumption. At least one concrete question that a follow-on investigation could answer.

**Recommendation**
The verdict: proceed, pause, pivot, or abandon. State it clearly. Connect it to the pattern you named. Then say what happens next — the immediate action, the decision gate, the thing someone should do Monday morning.

---

Tone: editorial, not neutral. You have read the signals. You have an interpretation. The story is that interpretation, offered with the confidence of someone who has done the work.

---

## V-05 — Output Format + Lifecycle: Two-Pass Structure

**Axis**: Output format (two-pass: scan pass then synthesis pass) + lifecycle emphasis (pass boundaries are explicit gates, not suggestions)
**Hypothesis**: Structuring the task as two discrete passes — a scan pass that extracts one finding per signal before any writing, and a synthesis pass that writes the story using only what was captured — forces selectivity structurally rather than relying on the model to self-regulate verbosity mid-composition.

---

Writing the story for `{topic}` happens in two passes. Complete Pass 1 fully before starting Pass 2. Do not merge them.

---

### Pass 1 — Scan Pass (no writing)

Read the following. Do not write the artifact yet.

**Read:** `simulations/{topic}/strategy.md`
Extract: the investigation question (one sentence).

**Read:** All `simulations/**/{topic}-*` artifacts.
For each artifact, extract exactly one thing: the single finding that most advances or complicates the investigation question. One sentence. If you cannot compress to one sentence, compress harder — you are selecting the most important thing, not summarizing.

When Pass 1 is complete, you have:
- The investigation question (1 sentence)
- One key finding per signal (1 sentence each)
- Nothing else

This is your raw material. The story is built from these extractions only.

---

### Pass 2 — Synthesis Pass (write the artifact)

Write `simulations/{topic}/{topic}-story-{date}.md` using only the material from Pass 1.

**Section 1 — What We Set Out to Understand**
The investigation question from Pass 1. Optionally expand to two sentences to give context, but do not add findings here.

**Section 2 — What the Signals Revealed**
Your per-signal extractions from Pass 1, formatted as a list. One entry per signal. Do not expand beyond what you extracted. The constraint is the point: if a finding was important enough to capture in Pass 1, one sentence is enough to convey it. If it wasn't captured, it doesn't belong here.

**Section 3 — What the Signals Say Together**
This section cannot be derived from Pass 1 alone — it must be synthesized from the pattern you see across all the Pass 1 findings. Ask: what do these one-sentence findings have in common that none of them says individually? Name the pattern. Explain the convergence — not "three signals agree" but "three signals agree because [underlying reason]."

This is the section that justifies the skill's existence. A reader who had read your Pass 1 extractions but not this section would not know what the investigation found. This section tells them.

**Section 4 — What Remains Uncertain**
Gaps in the Pass 1 extractions — signals that conflicted, questions the strategy planned for but no signal answered, or dimensions that no signal covered. Name them specifically. One concrete open question minimum.

**Section 5 — Recommendation**
Verdict: proceed / pause / pivot / abandon.
Grounded in Section 3's pattern — cite it by name or paraphrase.
Action-forcing: specify the next concrete step beyond the verdict.

---

**Pass discipline:** If you find yourself in Pass 2 pulling in details not captured in Pass 1, stop. Either the detail belongs in Pass 1 (go back and add it to the extraction) or it doesn't belong in the story at all. The two-pass structure is not procedural ceremony — it is the mechanism that keeps the story from collapsing into a summary.
