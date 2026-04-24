# discover — Evidence Before Commitment

## The short version

The discover namespace answers the two questions every feature decision must answer before
you write a spec: "Why would teams do nothing?" and "Is our core assumption actually true?"
Nine skills span market intelligence, risk analysis, and hypothesis investigation. Inertia
is always the primary competitor. Research before commitment.

---

## When to use this namespace

Discover is the first namespace in almost every investigation. Use it before you have a spec,
before you have picked a direction, before you have committed to anything. Discover is where
you find out whether the feature is worth building and what the real constraints are.

- You have a feature idea and want to know whether teams would adopt it or stick with their
  current workaround.
- You are about to write a spec and want to ground it in requirements, constraints, and
  evidence rather than assumptions.
- A core assumption is driving the feature design. You want to test it before encoding it
  in a spec.
- A stakeholder asks "did we actually validate that this is feasible?"
- You want to know what could go wrong before you start building.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `discover-competitors` | Competitive landscape with inertia-first framing. "None / status quo" is always assessed first, always HIGH threat. 5-8 named competitors with threat scoring. --focus market for sizing, --focus positioning for framework. | First. Always. Before anything else for any feature. |
| `discover-feasibility` | Traffic-light feasibility rating per component, overall score 0-100. --focus compliance, --focus stakeholders, --focus requirements, --focus naming, --focus size for additional dimensions. | Before drafting any spec. Catches blockers early. |
| `discover-risk` | Risk register across technical, market, compliance, dependency, and timeline dimensions. Each risk: severity (HIGH/MEDIUM/LOW), likelihood, mitigation. Inertia risk always listed first. | When you want to surface what could go wrong before committing. |
| `discover-inertia` | Deep analysis of the do-nothing competitor. Maps current workaround in detail, switching cost, inertia threat score (always HIGH by default), specific conditions under which inertia loses. | When the inertia case is your biggest risk. The most important analysis in Signal. |
| `discover-hypothesis` | State what you believe and what would change your mind. Claim, falsification condition, confidence level (0-100), planned experiments. The commitment step before investigation. | Before running any evidence skill. Commits you before you see results. |
| `discover-websearch` | Search the public web for evidence. Direct quotes with URLs only -- no paraphrase without attribution, no training-data claims. --confidence strict enforces citation discipline. | When public evidence is relevant. After discover-hypothesis. |
| `discover-analysis` | Analyze existing data, telemetry, schemas, or scenarios for patterns. Distinguishes correlation from causation explicitly. | When you have existing data or artifacts that bear on the hypothesis. |
| `discover-synthesize` | Merge all investigation signals into an answer-first synthesis: answer (yes/no/maybe), confidence, key evidence, counter-evidence, principles extracted, open questions. The synthesis supersedes individual investigation signals. | After gathering evidence. The deliverable. |
| `discover-orchestrate` | Orchestrate the full evidence campaign: hypothesis, websearch, analysis, synthesize in sequence. --focus intelligence, --focus topic, --focus prototype, --focus publish, --focus interview for specialized steps. | When you want the full campaign without managing each step. |

---

## Example workflow

You have an idea for "payment-reminders" -- automated reminders for overdue invoices.

**Step 1: Scout the inertia case.**

```
/discover-competitors payment-reminders
```

Output opens with "The Primary Competitor: why teams do nothing." You learn that the current
workaround is a Slack channel with a manual weekly spreadsheet review. Teams have been doing
it for two years and it works well enough. Threat: HIGH. You now have the inertia case.

**Step 2: Check feasibility.**

```
/discover-feasibility payment-reminders
```

Scans your repo for stack signals. Finds the platform throttles email to 3/minute/org.
Flags this as YELLOW: doable but requires backpressure design. The spec will need to
address this before it is written.

**Step 3: State the hypothesis.**

```
/discover-hypothesis payment-reminders
```

Forces a commitment: "Automated reminders reduce average days-to-pay by 25% or more."
Falsification condition: "any study showing no effect for the target cohort falsifies this."
Confidence: 55%. Planned experiments: websearch, internal data analysis.

**Step 4: Run the evidence.**

```
/discover-websearch payment-reminders --confidence strict
```

Finds 3 public studies. Two confirm the direction (18-32% reduction). One finds no effect
for enterprise customers with invoices above $10K. Counter-evidence noted.

**Step 5: Synthesize.**

```
/discover-synthesize payment-reminders
```

Answer: SUPPORTED with constraints. Confidence: 72% (up from 55%). Key finding: timing of
the first reminder is the critical variable. Principle extracted: reminders sent within 3
days of due date work; reminders sent after day 5 show no effect. Open question: is the
enterprise finding a volume effect or an account-size effect?

**Step 6: Check your topic status.**

```
/govern-status payment-reminders
```

Discover namespace: 4 of 9 skills covered. Readiness for spec: sufficient to proceed.

---

## What it produces

Discover artifacts write to `simulations/scout/` and `simulations/prove/`:

```
simulations/scout/
  competitors/    payment-reminders-competitors-2026-03-16.md
  feasibility/    payment-reminders-feasibility-2026-03-16.md
  risk/           payment-reminders-risk-2026-03-16.md
  inertia/        payment-reminders-inertia-2026-03-16.md

simulations/prove/
  investigations/ payment-reminders-hypothesis-2026-03-16.md
  investigations/ payment-reminders-websearch-2026-03-16.md
  investigations/ payment-reminders-analysis-2026-03-16.md
  investigations/ payment-reminders-synthesis-2026-03-16.md
  research/       payment-reminders-research-2026-03-16.md
```

Every artifact opens with standard frontmatter:

```yaml
---
skill: discover-competitors
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Run discover-competitors before everything else.** The inertia case is the most important
signal Signal produces. If you cannot explain why inertia loses, you are not ready to build.
discover-competitors answers that question in 10 minutes.

**discover-inertia is the deep dive.** discover-competitors surfaces the inertia case.
discover-inertia investigates it: exact workaround steps, switching cost breakdown, the
specific conditions under which inertia loses. Run it when the inertia threat is HIGH and
you want to understand it, not just identify it.

**State the falsification condition before you see any results.** discover-hypothesis
requires you to declare what evidence would change your mind. Without this commitment, you
will interpret all evidence as confirming your hypothesis. The falsification condition is
the intellectual honesty checkpoint.

**discover-synthesize supersedes the individual signals.** Once discover-synthesize runs,
the answer to "what did the investigation find?" is the synthesis, not a summary of each
experiment. INCONCLUSIVE is a valid outcome -- it means the hypothesis is not testable with
available evidence, which is itself a useful finding.

**discover-feasibility and the --focus flags are a modular assessment toolkit.** You do not
have to run eight separate skills to cover requirements, compliance, stakeholders, and naming.
`/discover-feasibility my-feature --focus compliance` runs the compliance dimension inline.
The full eight-skill sweep is available, but a single feasibility run with the right focus
often covers what you need.

---

## What's next

- **[specify](specify.md)** -- write the spec. Use discover findings as context.
- **[validate](validate.md)** -- review the spec against real user and customer personas.
- **[simulate](simulate.md)** -- simulate how the system actually behaves at runtime.
- **[govern](govern.md)** -- track investigation coverage and synthesize signals into decisions.
