# govern — Coverage Tracking, Narrative, and Org Governance

## The short version

The govern namespace manages two things: the investigation narrative (are we ready to commit?)
and the org governance layer (has the right organization reviewed this?). Fourteen skills
span topic tracking, decision orchestration, virtual org setup, review of business,
committee simulation, and PR review. Govern is where signals become decisions and decisions
get organizational sign-off.

---

## When to use this namespace

Use govern at the start of an investigation to register it, during the investigation to
track coverage and orchestrate evidence campaigns, and at the end to synthesize signals
into a decision. Use the org governance skills when decisions require multi-team or
exec-level review.

**Topic management:**
- You are starting a new feature investigation and want to register it with a strategy.
- You want to know which namespaces have coverage and which are missing.
- The investigation has gathered enough signals and you want to synthesize them into a story.

**Decision orchestration:**
- You want to run the full pre-commitment evidence campaign in one command.
- You want to validate a design across review, feedback, and adoption in one pass.
- You want a topic narrative dashboard showing what signals exist and what is missing.

**Org governance:**
- You want to set up a virtual org for your product area.
- A feature needs ROB review before the next planning cycle.
- You want every relevant role in your org to review a PR before it merges.
- Your monthly product review is tomorrow and you want to rehearse it today.

---

## Skills

### Topic and narrative skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `govern-status` | Show current signal coverage, gaps, and readiness. DISPLAY ONLY -- no file written. --view roadmap, --view reflect, --view retro, --view achievements for supplementary perspectives. | Anytime during an investigation. "Am I done?" |
| `govern-story` | Synthesize all signals into a narrative: what we investigated, what each signal revealed (key finding only), what the signals say together, what remains uncertain, the recommendation (proceed/pause/pivot/abandon). NOT a summary -- an editorial synthesis. | When the investigation is complete enough for a decision. |

### Decision orchestration skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `govern-decide` | Full pre-commitment decision campaign. Orchestrates: discover-competitors, discover-feasibility, discover-risk, discover-hypothesis, discover-websearch, discover-synthesize. --scope evidence or --scope blueprint for partial runs. | When you want the complete evidence brief for a feature decision in one command. |
| `govern-behavior` | Full technical simulation campaign. Orchestrates: simulate-lifecycle, simulate-conversation, simulate-state, simulate-contract, simulate-permissions in sequence. | Before implementation, to find spec gaps and contract violations. |
| `govern-qa` | Full design validation campaign. Orchestrates: validate-design, validate-users, validate-customers, validate-feedback, validate-adoption in sequence. | To validate a design before committing to spec, or before shipping. |
| `govern-brief` | Full topic narrative campaign. Orchestrates: topic-new (register), topic-roadmap (plan signals), govern-status (coverage), govern-story (narrative). | At the start and end of a signal-gathering session. |

### Org setup and governance skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `govern-scan` | Walk a repo and produce a draft org.yaml. Pivot modes: directory, concept, service, domain. Does NOT write .craft/roles/ -- outputs draft for human review first. | First-time setup. When onboarding a new codebase. |
| `govern-build` | Read confirmed org.yaml and generate org-chart.md and all .craft/roles/ files. Inertia Advocate always included in every team. | After confirming org.yaml. Regenerate when org structure changes. |
| `govern-roles` | Generate a typed role registry for a domain. Each role: orientation, lens, expertise, scope, collaborates_with. Inertia Advocate always included. Outputs .craft/roles/{area}/ directory. | Before graduating from lightweight crew review to full org governance. |
| `govern-chart` | Generate org structure for a product or domain: areas, divisions, committees, operating rhythms. Reads .craft/roles/ to build from real roles. ASCII org box + headcount table. | When you need a visual org representation. After govern-build. |
| `govern-product-review` | Run Review of Business (ROB) stages: leadership, teams, pm, tpm, arch-board, exec-office. --stage all for full ROB in sequence. --scope for one division. | Before planning cycles, feature commits, or major releases. |
| `govern-pull-request` | Run a PR through the full org. Selects reviewers by files changed. Per-role findings P1/P2/P3, consensus analysis, go/no-go recommendation. | Before merging high-impact PRs. |
| `govern-committee` | Simulate a committee meeting before the real one: ROB, shiproom, arch-board. Each participant reviews from their role. Outputs mock meeting minutes. | Before real committee meetings. Rehearsal artifact. |
| `govern-check` | Run any artifact through the full org (or stock roles if no .craft/roles/ exists). Per-role findings with severity. Review matrix: role, findings, severity, recommendation. | Anytime you have an artifact worth reviewing. Zero config required. |

---

## Example workflow: investigation tracking

You are investigating "payment-reminders" from the start.

**Step 1: Check status anytime.**

```
/govern-status payment-reminders
```

```
topic: payment-reminders
strategy: 12 signals planned
found:    5 signals

  ESSENTIAL (must have)
    [x] discover-competitors    payment-reminders-competitors-2026-03-16.md
    [x] discover-feasibility    payment-reminders-feasibility-2026-03-16.md
    [x] specify-spec            payment-reminders-spec-2026-03-16.md
    [ ] validate-design         not found
    [ ] simulate-lifecycle      not found

  RECOMMENDED
    [x] discover-hypothesis     payment-reminders-hypothesis-2026-03-16.md
    [x] discover-synthesize     payment-reminders-synthesis-2026-03-16.md
    [ ] validate-adoption       not found

  COVERAGE: 42% -- not ready for design commit
```

**Step 2: Run the full decision campaign when ready.**

```
/govern-decide payment-reminders
```

Orchestrates the complete pre-commitment evidence brief in one pass: competitors, feasibility,
risk, hypothesis, websearch evidence, synthesis. Produces a single decision brief with
recommendation and stated confidence.

**Step 3: Synthesize into a narrative.**

```
/govern-story payment-reminders
```

"We set out to determine whether automated payment reminders could reduce days-to-pay by
25%. Discovery found the primary threat is the existing spreadsheet workflow. Feasibility
found a throttle constraint requiring batching design. The synthesis found timing is the
critical variable. Validation found two adoption blockers: no org policy controls, no audit
log. Together the signals say: build it, but address the audit log and policy controls before
ship. Recommendation: PROCEED with two pre-ship spec updates."

---

## Example workflow: org governance

Your team needs ROB review on a major feature before the next planning cycle.

**Step 1: Set up the virtual org (first time only).**

```
/govern-scan my-product-area
```

Walks the repo. Produces a draft org.yaml for your review -- no role files written yet.
You review, adjust team names, add a Security Architect role, confirm.

```
/govern-build my-product-area
```

Generates org-chart.md and all `.craft/roles/` files. Inertia Advocate included in every
team. The virtual org is ready.

**Step 2: Rehearse the committee meeting before the real one.**

```
/govern-committee payment-reminders --type shiproom
```

Simulates the shiproom. Each participant reviews from their role. Mock minutes produced:
decisions, action items, dissenting opinions. The Inertia Advocate argues the spreadsheet
workflow is sufficient. You need an answer before the real meeting.

**Step 3: Run the ROB.**

```
/govern-product-review payment-reminders --stage all
```

Six stages in sequence: leadership, teams, pm, tpm, arch-board, exec-office. Each stage
produces its artifact. The tpm stage produces a risk register and go/no-go recommendation.

**Step 4: Review an artifact with no setup.**

If you do not have .craft/roles/ configured:

```
/govern-check payment-reminders-spec-2026-03-16.md
```

Stock roles activate: Architect, PM, Engineer, UX Designer, Security Architect, Compliance,
Inertia Advocate. Seven roles review the spec. No configuration required.

---

## What it produces

Govern artifacts write to multiple directories:

```
simulations/{topic}/
  {topic}-story-{date}.md               govern-story
  strategy.md                            investigation plan (via govern-brief)

simulations/campaign/
  {topic}-decide-{date}.md              govern-decide
  {topic}-validate-{date}.md            govern-qa
  {topic}-simulate-{date}.md            govern-behavior
  {topic}-brief-{date}.md               govern-brief

simulations/corps/
  {topic}-scan-{date}.md                govern-scan
  {topic}-rob-{stage}-{date}.md         govern-product-review
  {topic}-pr-review-{date}.md           govern-pull-request
  {topic}-committee-{date}.md           govern-committee

simulations/crew/
  {topic}-check-{date}.md               govern-check

design/corp/
  org-chart.md                           govern-chart, govern-build
.craft/roles/
  {area}/{role}.md                       govern-build, govern-roles
```

---

## Common patterns

**govern-story is not a summary.** govern-story is an editorial synthesis. Do not use it
to summarize each signal -- that produces a list, not a narrative. Use it to interpret what
the signals say together. The synthesis is the decision artifact; the individual signals
are the evidence.

**govern-decide runs the full evidence campaign before govern-story.** The campaign skills
(govern-decide, govern-qa, govern-behavior, govern-brief) are orchestrators -- they run
multiple underlying skills in sequence and produce consolidated output. Use them when you
want full coverage in one pass. Use the individual skills when you want targeted coverage.

**govern-check is the zero-setup org review.** If you do not have .craft/roles/ configured,
govern-check uses stock roles that activate by default. Seven expert perspectives review
any artifact, immediately, with no prior setup. It is the fastest path from "I have a spec"
to "I have expert critique."

**The Inertia Advocate is always present.** Every org review in govern includes an Inertia
Advocate role. Their job is to argue that the current workaround is sufficient. If the feature
cannot survive the Inertia Advocate's objections, it is not ready for the real committee.

**govern-committee before the real meeting, then compare.** The Simulation Rehearsal pattern
requires running govern-committee before a real committee meeting and recording the comparison.
The gap between what the simulation predicted and what actually happened is a calibration
signal for your role definitions.

---

## What's next

- **[discover](discover.md)** -- gather the evidence that govern-decide orchestrates.
- **[validate](validate.md)** -- govern-qa orchestrates validate skills. Run them directly
  for targeted review.
- **[simulate](simulate.md)** -- govern-behavior orchestrates simulate skills. Run them
  directly for targeted simulation.
- **[evals](evals.md)** -- the eval framework perspective: govern-story is where causal
  validity arguments must be made explicit.
