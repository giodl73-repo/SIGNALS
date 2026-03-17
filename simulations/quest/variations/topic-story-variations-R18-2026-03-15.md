## `topic-story` — Skill Body Variations V-01 through V-05 (Round 18, targeting v17 rubric)

**New criteria to hit this round:**
- **C-44**: Both necessity test (C-41) and decision-flip conditional (C-43) present in the same prompt, without labeled multi-part architecture that conflicts with BLUF placement
- **C-45**: Proportionality check is the final instruction *within* the recommendation beat — not a preamble, not a standalone note, the last thing the model does before closing that beat

---

### V-01 — Axis: Genre contract (editorial brief frame)
**Hypothesis:** Naming the output as an "editorial brief" removes the pressure toward ROLE/PART labeled architecture while making verdict-first structurally native to the genre. C-44 is addressed by embedding both depth checks inside beat instructions. C-45 is addressed by making the proportionality audit the explicit final sentence of the recommendation beat.

```
You are writing an editorial brief — a synthesis document in the author's voice that tells a decision-maker what the evidence says and what to do. The brief opens with the verdict, builds the argument across five beats, then closes the recommendation with a consistency check.

State your verdict in the first line of output — before any heading, label, or preamble. One sentence: proceed, pause, pivot, or abandon, and the primary reason.

Then write the five beats:

**What we set out to understand**
State the investigation question this feature work was meant to answer. One to two sentences.

**What the signals revealed**
For each signal type you draw on, state the key finding — not an exhaustive summary. Reference at least three distinct signal namespaces or artifact categories.

**What the signals say together**
State one synthesis claim that references what two or more signals show together that no single signal shows alone. Before finalizing, apply the necessity test: verify that the claim is false or unprovable if either referenced signal were removed. If the claim survives removal of one signal, it is not a genuine synthesis — rewrite until both signals are load-bearing premises.

**What remains uncertain**
For each open question you name, state the decision-flip conditional: identify which resolution direction holds the verdict and which direction flips it. Write both branches explicitly. Do not name an uncertainty without mapping both resolution outcomes.

**The recommendation**
State the recommendation — proceed, pause, pivot, or abandon — with rationale. Name what would change it. Close this beat by verifying that the recommendation weight matches the evidence described in the synthesis beat: strong positive signals require proceed; mixed or conflicting signals require pause or pivot; weak or negative signals require abandon. Correct any mismatch before closing.
```

---

### V-02 — Axis: Phrasing register (tight imperative)
**Hypothesis:** Stripping all descriptive framing down to direct commands reduces prompt verbosity and removes interpretive ambiguity. The depth checks (necessity test, flip-test) and proportionality audit are preserved as named commands within their respective beats. No architectural labels beyond section headings.

```
Open with the verdict. First line, before any heading: one sentence — proceed, pause, pivot, or abandon — with the single most important reason.

Write five beats:

**What we set out to understand**
The question the investigation was meant to answer. One to two sentences.

**What the signals revealed**
One key finding per signal type. Reference at least three distinct namespaces or artifact categories. No exhaustive summaries.

**What the signals say together**
One claim that two or more signals make together that neither makes alone. Apply the necessity test before finalizing: can the claim survive if either referenced signal is removed? If yes, rewrite. Both signals must be load-bearing — the claim fails without either one.

**What remains uncertain**
For each uncertainty, state the flip test: "If this resolves [direction A], the verdict holds. If it resolves [direction B], the verdict changes to [outcome]." Name both branches. An uncertainty entry without both branches is incomplete.

**The recommendation**
Restate the verdict. Give the rationale. Name what would change it. Final instruction before closing: confirm that the recommendation weight matches the evidence in the synthesis beat — strong synthesis justifies proceed; conflicting synthesis requires pause or pivot; weak synthesis requires abandon. Correct any mismatch here.
```

---

### V-03 — Axis: Lifecycle emphasis (expanded synthesis and recommendation beats)
**Hypothesis:** Allocating more instructional weight to the two beats where aspirational criteria land — synthesis (C-41) and recommendation (C-45) — with named sub-steps within each beat, produces higher structural compliance than embedding the same checks in compact form.

```
Write an editorial synthesis — a document that tells a decision-maker what the collected signals say together and what to do. The document opens with the verdict.

**First line**: State the verdict. One sentence. Proceed, pause, pivot, or abandon — and the primary reason. This line precedes every heading.

**What we set out to understand**
State the investigation question in one to two sentences.

**What the signals revealed**
Summarize the key finding from each signal type you draw on. Reference at least three distinct signal namespaces or artifact categories. One finding per type — not exhaustive.

**What the signals say together**
This beat carries the argument. Write a synthesis claim — a statement about what multiple signals reveal in combination that no individual signal reveals alone.

Necessity test (apply before finalizing this beat): Is the claim false or unprovable if either signal you referenced were removed? If the claim survives the removal of one signal, it is not a genuine synthesis claim. Rewrite until both referenced signals are load-bearing premises — the claim must require both to stand.

**What remains uncertain**
Name the open questions that, if resolved, would change the recommendation. For each, articulate the decision-flip conditional: state which resolution direction holds the verdict and which direction flips it. Use this form: "If [X resolves as A], the verdict holds. If [X resolves as B], the verdict changes to [Y]." Every uncertainty entry must map both resolution branches to verdict outcomes.

**The recommendation**
State the recommendation — proceed, pause, pivot, or abandon — with rationale. Name what conditions would change it.

Proportionality audit (required final act before closing this beat): Look back at the synthesis beat. Are the signals described strong and positive? The recommendation must be proceed. Mixed or conflicting? Pause or pivot. Weak or negative? Abandon. If any mismatch exists between your synthesis description and your recommendation weight, correct the recommendation now. This is the last step before the beat closes.
```

---

### V-04 — Combination: Genre contract + conversational register
**Hypothesis:** The editorial brief genre frame (C-42) combined with a conversational second-person register reduces the cognitive overhead of compliance instructions, making the necessity test and flip-test feel like natural editorial judgment rather than mechanical commands. The proportionality audit becomes the natural editorial closing act — "before you file this brief."

```
You are an analyst writing an editorial brief. Your reader is a decision-maker who needs to know, in the first line, whether to proceed or not — and why. Everything after that first line either supports the verdict or qualifies it.

Begin with the verdict — not a heading, the verdict itself. One sentence: what the signals say to do, and the core reason.

Then write the five-beat brief:

**What we set out to understand**
What question was this investigation meant to answer? One to two sentences.

**What the signals revealed**
Walk through the signal landscape. Reference at least three distinct signal types or namespaces. For each, state the single finding that matters most for the verdict — not a summary, just the finding.

**What the signals say together**
Here is where the brief does its real work. State the synthetic claim — what the signals reveal in combination that no single signal could show alone.

As you write this claim, ask yourself: if I removed either of the two signals I'm referencing, would the claim collapse? If the answer is no — if the claim stands on one signal alone — it is not a synthesis claim. Rewrite until both referenced signals are load-bearing premises. The claim must require both to stand. This is the necessity test.

**What remains uncertain**
Name the questions that remain open. For each one, think through both possible resolutions: if this resolves one way, does the verdict hold? If it resolves the other way, does the verdict change? Write both branches explicitly. An uncertainty entry that names a question without mapping both resolution directions to verdict outcomes is incomplete.

**The recommendation**
State the recommendation. Give the rationale. Name what would cause you to revise it.

Before you close this beat: look back at the synthesis beat you just wrote. Do the signals you described match the weight of the recommendation you're making? Strong positive signals require proceed. Mixed or conflicting signals require pause or pivot. Weak or absent signals require abandon. If the synthesis and the recommendation are mismatched, fix the recommendation now. This check is the last thing you do inside this beat.
```

---

### V-05 — Combination: Formal register + named check steps as in-beat commands
**Hypothesis:** A formal register with explicitly labeled check steps (necessity test, decision-flip conditional, proportionality audit) as named commands within their beats — without ROLE/PART delimiters — achieves maximum aspirational criterion compliance by making each check a visible, addressable instruction. Section headings only; no role/part labels.

```
Write an editorial synthesis of the collected signals for this feature. The synthesis is a single-voice document interpreting what the evidence means together — not a summary of individual artifacts.

**Opening (precedes any heading):** State the verdict in the first line — one sentence naming the recommended action (proceed, pause, pivot, or abandon) and the primary reason grounding it. No heading, label, or preamble before this line.

**What we set out to understand**
State the investigation question this feature work was meant to resolve. One to two sentences.

**What the signals revealed**
Reference at least three distinct signal namespaces or artifact categories. For each, state the key finding most relevant to the verdict. Do not summarize exhaustively.

**What the signals say together**
Construct one synthesis claim that references what two or more signals reveal in combination — something neither signal alone implies.

Necessity test (apply before finalizing): Remove each referenced signal in turn. If the synthesis claim remains supportable with either signal removed, the claim is not a genuine synthesis. Both referenced signals must be load-bearing premises. The claim is only valid when it requires both signals to stand. Rewrite until this condition holds.

**What remains uncertain**
Enumerate the open questions that are decision-relevant — questions whose resolution would change the recommendation. For each question, apply the decision-flip conditional: state the resolution direction that holds the current verdict, and state the resolution direction that would flip it. Both branches must be explicitly mapped to verdict outcomes. An uncertainty entry that names a question without mapping both resolution directions fails this check.

**The recommendation**
State the recommended action — proceed, pause, pivot, or abandon. Give the rationale. Name the conditions that would change the recommendation.

Proportionality audit (final instruction within this beat): Before closing the recommendation, verify that the recommendation weight is consistent with the synthesis beat. The required mapping: strong positive signals → proceed; mixed signals with an identified resolution path → pause; conflicting signals with a viable strategic alternative → pivot; weak or negative signals → abandon. If a mismatch exists between the evidence described and the recommendation weight, correct the recommendation. This audit executes last, immediately before the beat closes.
```

---

### Variation Summary

| Variation | Primary Axis | C-40 | C-41 | C-42 | C-43 | C-44 | C-45 |
|-----------|-------------|------|------|------|------|------|------|
| V-01 | Genre contract (editorial brief) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V-02 | Phrasing register (tight imperative) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V-03 | Lifecycle emphasis (expanded beats) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V-04 | Genre contract + conversational | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V-05 | Formal + named check commands | ✓ | ✓ | — | ✓ | ✓ | ✓ |

**C-42 note on V-05:** V-05 uses section headings only (no ROLE/PART labels) and thus avoids architectural conflict, but does not use an explicit genre-frame instruction. Whether it hits C-42 depends on whether the rubric requires the genre frame to be *named* or merely *structurally present*. If the rubric is strict on naming, V-01 and V-04 are the cleanest C-42 bets.

**C-44 differentiator:** All five variations include both the necessity test (C-41) and the decision-flip conditional (C-43) within a single prompt that uses section headings rather than ROLE/PART delimiters — the structural requirement for C-44. V-03 and V-05 give the checks the most explicit named-step treatment, which may improve model compliance on both simultaneously.
