# Signal — Quickstart

## The short version

Signal is a pre-commitment evidence tool. Before you build a feature, you gather signals across 9 namespaces. When you have enough signals, your topic tells you you're ready. The primary competitor is always inertia.

---

## The problem

You have a feature idea. You build it. You ship it. Three weeks later, adoption is flat. You dig in and discover that the status-quo workaround — the one your users cobbled together with a spreadsheet and a Slack channel — was actually good enough. The workaround is free, it requires no training, and the team already knows how to use it. You just lost three weeks to a buildable thing that nobody needed.

Signal forces you to answer one question before you write a line of code: **Why would teams do nothing instead?**

That question — the inertia case — is the first signal every investigation produces. If you cannot explain why inertia loses, you are not ready to build.

---

## The 9 namespaces

Each namespace is an evidence-gathering domain. Every skill in a namespace produces a dated artifact in `signals/`. The namespace prefix also routes by audience: `scout` and `draft` are PM-facing; `trace` and `flow` are developer-facing; `review` is team-facing.

| Namespace | What it answers | Example skill |
|-----------|----------------|---------------|
| `scout`   | Who else does this? Is it feasible? What does the market look like? | `/scout-competitors` |
| `draft`   | What exactly are we building? | `/draft-spec` |
| `review`  | Does this design work for real users and teams? | `/review-design` |
| `flow`    | How does this actually behave at runtime? | `/flow-lifecycle` |
| `trace`   | Does the implementation match the spec? | `/trace-contract` |
| `prove`   | Is our core assumption correct? | `/prove-hypothesis` |
| `listen`  | Will teams actually adopt this? What blocks them? | `/listen-adoption` |
| `program` | What are we committing to? What is the staged plan? | `/program-plan` |
| `topic`   | Are we ready to commit? What signals are missing? | `/topic-status` |

---

## The inertia rule

Every `/scout-competitors` run assesses "none / status quo" first. Always. This is not one competitor among many — it is the primary competitor, scored threat HIGH by default.

The inertia case answers: Why would a team do nothing? What does the status quo workaround cost them? Is that cost lower than the switching cost of adopting something new?

```
Inertia assessment (always first)
  What is the status quo workaround?
  How well does it work?
  What does it cost the team (time, risk, friction)?
  What would make a team choose it over your feature?
  Threat: HIGH (always)
```

If you cannot write a paragraph explaining why inertia loses, your feature does not have a clear value case yet. Signal surfaces this in 10 minutes, not 3 weeks.

---

## The minimal workflow

Five steps from idea to first read on readiness:

```
1. Open topic      /topic-new my-feature
2. Scout inertia   /scout-competitors my-feature
3. Scout feasibility  /scout-feasibility my-feature
4. Check status    /topic-status my-feature
5. Commit when ready
```

**Step 1: Open topic**

```
/topic-new payment-reminders
```

Registers the topic in `signals/TOPICS.md`, creates a `strategy.md` with planned signals for the investigation. The strategy is an editorial plan — which namespaces to cover, in what order, who owns each signal. Every skill runs standalone even without this step, but opening a topic gives you coverage tracking.

**Step 2: Scout the inertia case first**

```
/scout-competitors payment-reminders
```

Produces `signals/scout/competitors/payment-reminders-competitors-2026-03-16.md`. The artifact opens with "The Primary Competitor" — why teams do nothing — before listing named competitors. This is the signal that either validates your feature's existence or stops a bad idea early.

**Step 3: Check feasibility**

```
/scout-feasibility payment-reminders
```

Assesses technical, resource, and timeline constraints. Flags blockers before you draft a spec.

**Step 4: Check what's missing**

```
/topic-status payment-reminders
```

No file written. Terminal display only. Shows:
- Signals found (which namespaces have coverage)
- Signals missing (which are in the strategy but not yet run)
- Coverage percentage
- Readiness for your target outcome (design commit, ship, post-ship)

**Step 5: Commit when ready**

You are ready when all essential namespaces for your feature's risk tier have coverage and the inertia case has been answered. `/topic-status` tells you when you are there. You decide whether to commit.

---

## Signal files

Every skill writes one dated artifact. Two people running the same skill on the same topic produce two files — different signals, no collision.

```
signals/
  scout/
    competitors/    payment-reminders-competitors-2026-03-16.md
    feasibility/    payment-reminders-feasibility-2026-03-16.md
  draft/
    specs/          payment-reminders-spec-2026-03-16.md
  flow/
    lifecycle/      payment-reminders-lifecycle-2026-03-16.md
  trace/
    contract/       payment-reminders-contract-2026-03-16.md
  prove/
    investigations/ payment-reminders-hypothesis-2026-03-16.md
  listen/
    adoption/       payment-reminders-adoption-2026-03-16.md
  topic/
    status/         payment-reminders-status-2026-03-16.md
```

Artifact naming is a contract: `{topic}-{signal}-{date}.md`. The topic prefix ties all artifacts for an initiative across all directories — `glob payment-reminders-*` finds everything. The signal name describes the angle covered, not the skill that ran. The date is a timestamp, not a version.

## What a signal looks like

These are abbreviated but representative examples drawn from real Signal skill outputs.

```
# scout-competitors: Signal plugin — 2026-03-16

## The Primary Competitor

**Inertia / status quo** — threat: HIGH
Teams already have informal evidence-gathering: Slack conversations,
hallway PM interviews, one-pager docs. Switching cost: zero. Training
cost: zero. The workaround has been in place since the team formed.
Cost of continuing: 2-3 hours wasted per feature on misaligned specs.

F-01: Inertia is not passivity. It is an active, habitual, socially
reinforced choice. Signal wins by being faster than the threshold of
"is this worth the time?" — not by being more comprehensive.
```

```
# trace-contract: payment-gateway — v2.3 spec — 2026-03-16

Finding F-01
  element: idempotency-key — success path
  deviation: spec declares "idempotency guaranteed on retry" but no
    retry-key field exists in CreateOrderRequest schema
  severity: breaking
  mechanism-type: missing-field
  spec: §4.2 Idempotency Requirements
  hypothesis: CreateOrderRequest schema was never updated when §4.2
    was added; field exists in spec narrative but not in schema declaration

gate-status: FAIL
Verdict: Contract violated
Coverage: 6/7 fields verified, 1 deviation
```

```
# prove-hypothesis: AI pair programming reduces review time — 2026-03-16

Claim: AI pair programming reduces code review time by 30% or more
  for mixed-seniority engineering teams.

Falsification conditions:
  F-01: If median review time delta across 50+ PRs is < 15%, false.
  F-02: If effect disappears when senior:junior ratio exceeds 2:1, false.

Finding: 3 studies confirm 20-40% reduction (Wei et al. 2024,
  GitHub Copilot study n=974, internal Microsoft data n=312)
Finding: Effect concentrates in junior developers; senior devs show
  8% reduction only — F-02 is live risk

Verdict: PARTIALLY CONFIRMED — 30% holds for junior cohort,
  does NOT hold for mixed teams. Revise claim scope before spec.
```

Every artifact opens with standard frontmatter the skill writes automatically:

```yaml
---
skill: scout-competitors
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Parameters

Every skill accepts a common parameter set. You rarely need to specify them — the defaults are calibrated by namespace audience.

| Parameter | Values | Default | What it does |
|-----------|--------|---------|-------------|
| `--depth` | `quick / standard / deep` | `standard` | Thoroughness. Standard = 15+ findings. Deep = multi-angle, 30+ findings. |
| `--for` | `pm / engineer / exec` | auto-detected | Tailors output framing and vocabulary. |
| `--confidence` | `strict` | off | Only cite claims you can quote directly. |
| `--mode` | `risk` | off | Available on scout skills. Frames output as cost-of-not-acting for exec audiences. |
| `--json` | flag | off | Writes a structured sidecar `.json` alongside the Markdown artifact. |

```
/scout-competitors payment-reminders --depth deep --for exec --mode risk
/review-design payment-reminders --confidence strict
/flow-lifecycle payment-reminders --for engineer --depth quick
```

---

## The topic narrative

`/topic-status` is the readout of your current position. It globs `signals/**/{topic}-*`, cross-references against `strategy.md` planned signals, and computes coverage.

```
topic: payment-reminders
strategy: 12 signals planned
found:    5 signals
missing:  7 signals

  ESSENTIAL (must have)
    [x] scout-competitors    payment-reminders-competitors-2026-03-16.md
    [x] scout-feasibility    payment-reminders-feasibility-2026-03-16.md
    [ ] draft-spec           not found
    [ ] prove-hypothesis     not found

  RECOMMENDED
    [x] review-design        payment-reminders-design-2026-03-16.md
    [ ] flow-lifecycle       not found
    [ ] listen-adoption      not found

  COVERAGE: 42% -- not ready for design commit
```

For a written summary artifact rather than terminal display, use `/topic-report`. For tracking signal exposure across a portfolio of topics, see the `program` namespace.

---

## Corp and Crew

For teams using Signal on a shared repo with an org configuration, two additional namespaces accelerate review across your org structure.

**Crew** reviews artifacts through your compiled org roles:

```
/crew-review payment-reminders-spec-2026-03-16.md
```

Reads `.roles/` and selects reviewers relevant to the artifact type. Each role reviews from their perspective. Produces a review matrix: role, findings, severity, recommendation. No roles configured? Crew uses a set of stock roles automatically.

**Corp** surfaces org-wide signals:

```
/corp-pr 447
```

Every relevant role reviews PR 447. Findings organized by role and severity. Catches issues a single reviewer misses — a security architect finds the access control gap a PM reviewer never looked for.

```
/corp-rob --stage all
```

Runs a full Review of Business. Leadership, teams, PM, TPM, Arch Board, Exec Office — each stage produces its own artifact. Use `--stage pm` or `--stage leadership` to run a single stage. The ROB is Signal's mechanism for surfacing org-level readiness, not just feature readiness.

---

## Zero setup

The first run of any skill produces a useful result with no prior configuration.

- No config file required. `simulate.yaml` is created on first run if you want to customize, but it is never required.
- Stock roles ship with every skill and activate by default.
- No skill requires another to have run first. Run `/trace-contract` without running `/scout-competitors` first. The skills are self-contained.
- The first artifact you see is useful, not a setup wizard.

> **Works without a code repo.** Signal skills run on any topic — a product description, a Notion doc, a feature brief, even a conversation. The `signals/` directory is the only requirement. Power Platform builders, citizen developers, and pre-code PMs can run Signal from day one.

---

## Common starting points

You do not always start with `/topic-new`. Start where the pain is.

| Situation | Start here |
|-----------|-----------|
| Feature idea, don't know if it's worth building | `/scout-competitors` |
| Spec written, want a design review | `/review-design` |
| Implementation done, want to verify it matches spec | `/trace-contract` |
| Shipped, adoption is low, want to understand why | `/listen-adoption` |
| Assumption driving the feature, want to test it | `/prove-hypothesis` |
| Need a runtime behavior walkthrough | `/flow-lifecycle` |
| Ready to plan the full investigation | `/topic-new` then `/program-plan` |

---

## What's next

- **[Namespace guides](guides/)** — deep coverage of each namespace, all skills, parameter options, and artifact examples
  - [scout](guides/scout.md) — competition, feasibility, market, requirements, compliance, naming, positioning, stakeholders
  - [draft](guides/draft.md) — spec, brainstorm, pitch, proposal
  - [review](guides/review.md) — design, code, users, customers
  - [flow](guides/flow.md) — lifecycle, trigger, throttle, resilience, conversation, dataflow, integration
  - [trace](guides/trace.md) — contract, state, permissions, request, component, deployment, migration
  - [prove](guides/prove.md) — hypothesis, websearch, interview, analysis, synthesize, program, prototype, publish, intelligence
  - [listen](guides/listen.md) — adoption, feedback, support
  - [program](guides/program.md) — plan, orchestration, the echo stage
  - [topic](guides/topic.md) — status, report, story, plan, new, echo
- **[Philosophy](philosophy.md)** — why Signal exists, the evidence behind the techniques, the scale table
- **[Principles](../PRINCIPLES.md)** — design decisions: naming contract, append-only artifacts, concurrent by default
- **[Corp and Crew guide](guides/corps.md)** — org chart, role compilation, ROB cadence, PR review automation
- **[Install guide](../install/README.md)** — which binding to choose, install scripts, prerequisites
- **[Golden prompts](../signals/README.md)** — the 75 convergent skill prompt bodies
- **[Role registry](.roles/README.md)** — 206 expert roles, domain subsets, role creation
