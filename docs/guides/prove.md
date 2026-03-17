# prove — Hypothesis Investigation

## The short version

The prove namespace tests whether the assumption underneath your feature is actually true.
Nine skills cover hypothesis formation, web search, internal intelligence, prototype, analysis,
interview simulation, synthesis, and publication. A hypothesis that cannot be falsified is
an assertion. prove makes it a hypothesis.

---

## When to use this namespace

Use prove when you have an assumption that is load-bearing enough to be worth testing. The
prove namespace is where Signal forces intellectual honesty: you state what you believe and
what would change your mind before you see the results.

- You are building a feature on the assumption that teams will adopt a new workflow. Is that true?
- A spec asserts "users want real-time notifications." Do they? Or do they want daily digests?
- You have a hypothesis about what is causing adoption failure. You want to test it before
  making a design change.
- You need to synthesize evidence from multiple sources into a defensible answer.
- A past investigation produced important findings and you want to write them up for institutional memory.

prove is also pre-commitment valuable: running prove-hypothesis before draft-spec earns the
Evidence-Based Draft chain achievement. A spec that starts from an investigated hypothesis
is stronger than one that starts from an untested belief.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `prove-hypothesis` | States the claim, falsification condition, confidence level, and planned experiments. Entry point to any prove investigation. | First. The commitment step: state what you believe before you investigate. |
| `prove-websearch` | Searches the public web for evidence, extracts direct quotes with URLs. --confidence strict: only cites claims you can quote. | When public evidence is relevant. After prove-hypothesis. |
| `prove-intelligence` | Searches internal sources (repo files, design docs, scenarios, prior signals) for evidence. | For product-specific hypotheses where internal context is the best evidence. |
| `prove-prototype` | Builds the smallest thing that tests the hypothesis and measures it. Define: what to build, what to measure, what confirms vs. refutes. | When the hypothesis requires empirical measurement rather than analysis. |
| `prove-analysis` | Analyzes data, telemetry, schemas, or scenarios for patterns. Distinguishes correlation from causation explicitly. | When you have existing data or artifacts that bear on the hypothesis. |
| `prove-interview` | Simulates stakeholder or customer interviews using persona-driven methodology. Each persona speaks in their own voice. | When user perspective is the key evidence. Produces simulated but grounded interview data. |
| `prove-synthesize` | Merges all investigation signals into an answer-first synthesis: answer, confidence, key evidence, counter-evidence, principles, open questions. | After gathering evidence. The deliverable that supersedes the individual investigation signals. |
| `prove-publish` | Writes the investigation as a paper for institutional memory. Simplified panel review. | When findings are significant enough to be referenced by future teams. |
| `prove-topic` | Orchestrates the full prove campaign in one command: hypothesis, websearch, intelligence, analysis, synthesize in sequence. | When you want the full campaign without managing each step. |

---

## Example workflow

You are building "payment-reminders" and the feature rests on an assumption: "teams that
receive reminders pay invoices 30% faster than teams that do not." You want to test this
before building.

**Step 1: State the hypothesis.**

```
/prove-hypothesis payment-reminders
```

Produces: Claim: "automated payment reminders reduce average days-to-pay by >= 25%."
Falsification condition: "any study or internal data showing no statistically significant
difference between reminded and non-reminded cohorts falsifies this." Confidence: 55%.
Planned experiments: websearch for academic/industry data, internal analysis of past
manual reminder data.

**Step 2: Search for external evidence.**

```
/prove-websearch payment-reminders --confidence strict
```

Finds 3 studies. Two confirm the direction (automated reminders reduce days-to-pay 18-32%).
One finds no effect for enterprise customers (invoices > $10K). The enterprise finding
is counter-evidence. You note it.

**Step 3: Analyze internal data.**

```
/prove-intelligence payment-reminders
```

Finds prior manual reminder records in the repo's support history. Pattern: manual reminders
sent in the first 5 days after due date show 28% faster payment. After day 5, no effect.
Finding: timing matters. The spec does not specify when reminders send.

**Step 4: Synthesize.**

```
/prove-synthesize payment-reminders
```

Answer: SUPPORTED with constraints. Confidence: 78% (up from 55%). Key evidence: 2 public
studies + internal manual data. Counter-evidence: no effect for large-invoice enterprise
accounts. Principle extracted: "timing of first reminder is the critical variable, not
the reminder itself." Open question: is the enterprise finding a volume effect or an
account-size effect?

---

## What it produces

All prove artifacts write to `simulations/prove/`:

```
simulations/prove/
  investigations/  payment-reminders-hypothesis-2026-03-16.md
  investigations/  payment-reminders-websearch-2026-03-16.md
  investigations/  payment-reminders-intelligence-2026-03-16.md
  investigations/  payment-reminders-analysis-2026-03-16.md
  investigations/  payment-reminders-synthesis-2026-03-16.md
  publications/    payment-reminders-paper-2026-03-16.md
```

Example frontmatter:

```yaml
---
skill: prove-hypothesis
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**State the falsification condition before you see any results.** prove-hypothesis requires
you to declare what evidence would change your mind. This is the commitment step. Without it,
you will interpret all evidence as confirming your hypothesis regardless of what it actually
says.

**INCONCLUSIVE is a valid and valuable outcome.** If prove-synthesize produces INCONCLUSIVE,
you have learned that the hypothesis is not testable with the evidence available. This is
not failure -- it is a reason to either run more experiments or to design the feature so it
does not rest on an untestable assumption. The Falsified achievement is earned on INCONCLUSIVE
as well as REJECTED.

**prove-synthesize supersedes the individual signals.** The synthesis is the deliverable.
Once prove-synthesize has been run, the answer to "what did the investigation find?" is
the synthesis, not a summary of each experiment. Do not summarize the experiments -- read
the synthesis.

---

## What's next

- **[draft](draft.md)** -- run draft-spec after prove-synthesize for the Evidence-Based Draft chain.
- **[scout](scout.md)** -- if prove changes the inertia analysis, re-run scout-competitors.
- **[topic](topic.md)** -- record what the investigation found in topic-echo (unexpected findings).
- **[listen](listen.md)** -- if the hypothesis was about adoption, prove-synthesize feeds into listen-adoption analysis.
