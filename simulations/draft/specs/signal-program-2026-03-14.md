# Program Specification

**Topic**: sim
**Namespace**: /program:
**Skills**: 1
**Default mode**: Full
**Audience**: Tech leads, program managers, and architects who orchestrate multi-skill initiatives across the full simulate plugin surface

## Purpose

How do you run the whole pipeline? /program: is the Layer 2 orchestrator that sequences skills from all other namespaces into a staged plan with gates, tracks progress via topic prefix, and ensures no stage is skipped or run out of order. It answers "What needs to happen, in what order, with what evidence, before we can ship?"

## Skills

### /program:plan

**What**: Generate, validate, and track a staged execution plan that sequences Layer 1 skills from any namespace into an initiative pipeline with gates.
**Stock roles**: None (the lead is the operator; skills execute within their own role systems)
**Input**: An initiative description (what you're building and why), optionally a list of namespaces to include, and optionally a set of constraints (timeline, team size, risk tolerance).
**Output**: A `program.yaml` file defining stages, skills, gates, and dependencies — plus a tracking dashboard that shows progress across all stages.
**Lifecycle**:
- Setup: Lead describes the initiative. Skill analyzes the description to identify which namespaces are relevant — does this need scouting? Design? Review? Simulation? Investigation? Listening? Proposes a stage sequence based on the natural dependency order (scout before draft, draft before review, review before build, build before listen). Lead confirms or adjusts. A topic prefix is assigned — all artifacts produced by skills in this program will use this prefix, making the entire initiative discoverable via `{topic}-*.md` glob.
- Execute: Generate the `program.yaml` with concrete stages. For each stage: name, description, which skills to run, gate criteria (what must be true before advancing), and dependencies on prior stages. Skills within a stage can run in parallel if they have no mutual dependencies. The plan also identifies which stages are inside plugin scope (automated by simulate skills) and which are outside (implementation, deployment — noted but not orchestrated).
- Findings: Validate the plan against known anti-patterns. Check: are stages in the right dependency order? Are gate criteria measurable and achievable? Are any namespaces missing that the initiative description implies? Are there stages with no skills (just notes) that should have skills? Are there skills that produce artifacts consumed by later skills without an explicit dependency? Flag warnings and suggestions.
- Amend: Lead reviews the plan, adjusts stages, adds or removes skills, tightens or loosens gates, adds notes for out-of-scope stages. Re-validates. Iterate until the plan passes validation with no warnings.
**Lightweight**: `--quick` generates a 3-5 stage plan with default gates, skips validation, skips Amend. Good for prototyping a plan structure before committing.
**Artifact**: `program/plan/sim-{slug}-{date}.md` (human-readable summary) + `program/plan/sim-{slug}-{date}.yaml` (machine-readable plan)
**Example**:

User runs `/program:plan "Build an AI-assisted deployment validator for Dynamics 365 solutions — scans solutions for common deployment failures before shipping"`.

**Setup**: Skill analyzes the initiative. Detects need for: competitive research (what validators exist?), feasibility check (can we scan solution XML fast enough?), design (spec the validator), review (multi-perspective validation of the design), simulation (trace deployment scenarios), implementation (outside plugin scope), code review (after implementation), and post-ship listening. Proposes topic prefix: `depval`. Proposes 7 stages. Lead confirms, but adds: "Include a prove stage — we need to verify that our top-10 failure list matches real customer pain."

**Execute**: Generates `program.yaml`:

```yaml
topic: depval
initiative: "AI-assisted deployment validator for Dynamics 365 solutions"
created: 2026-03-14
stages:
  - name: scout
    description: "Understand the competitive landscape and validate feasibility"
    skills:
      - scout:competitors
      - scout:feasibility
      - scout:requirements
    gate: "PM reviews findings — at least 5 unmet needs identified, feasibility confirmed for top 3"
    artifacts:
      - depval-competitors-2026-03-14.md
      - depval-feasibility-2026-03-14.md
      - depval-requirements-2026-03-14.md

  - name: prove
    description: "Validate that our failure taxonomy matches real customer pain"
    skills:
      - prove:hypothesis
      - prove:intelligence
      - prove:analysis
      - prove:interview
      - prove:synthesize
    gate: "Hypothesis confirmed or revised — failure taxonomy validated against telemetry and customer feedback"
    depends_on: [scout]
    artifacts:
      - depval-failure-taxonomy-2026-03-15.md
      - depval-failure-telemetry-2026-03-15.md
      - depval-failure-analysis-2026-03-15.md
      - depval-failure-interviews-2026-03-15.md
      - depval-failure-synthesis-2026-03-16.md

  - name: draft
    description: "Write the design spec and proposal"
    skills:
      - draft:spec
      - draft:proposal
    gate: "Spec covers all validated failure types — no gaps against prove findings"
    depends_on: [prove]
    artifacts:
      - depval-spec-2026-03-16.md
      - depval-proposal-2026-03-16.md

  - name: review
    description: "Multi-perspective design validation"
    skills:
      - review:design
      - review:users
      - review:customers
    gate: "No P1 findings remain — all personas score >= 3/5 — primary customer personas score would-adopt >= 3"
    depends_on: [draft]
    artifacts:
      - depval-design-review-2026-03-17.md
      - depval-user-walkthrough-2026-03-17.md
      - depval-customer-eval-2026-03-17.md

  - name: build
    description: "Implementation — outside simulate plugin scope"
    skills: []
    note: "Team implements the validator. Use the spec from draft stage and findings from review stage as implementation guide. Track in ADO or GitHub issues."
    gate: "Implementation complete — all spec requirements covered — unit tests pass"
    depends_on: [review]

  - name: validate
    description: "Post-implementation validation — code review and deployment tracing"
    skills:
      - review:code
      - trace:deployment
    gate: "All review disciplines pass — deployment trace shows no unhandled failure paths"
    depends_on: [build]
    artifacts:
      - depval-code-review-2026-03-20.md
      - depval-deployment-trace-2026-03-20.md

  - name: listen
    description: "Simulate post-ship customer reactions"
    skills:
      - listen:feedback
      - listen:adoption
    gate: "No critical adoption blockers — feedback synthesis shows no P1 issues from primary personas"
    depends_on: [validate]
    artifacts:
      - depval-feedback-2026-03-21.md
      - depval-adoption-2026-03-21.md
```

**Findings**: Validation checks:
- Stage ordering: correct (scout -> prove -> draft -> review -> build -> validate -> listen)
- Gate measurability: all gates have measurable criteria (pass)
- Missing namespaces: no `/flow:` skills included — warning: "Initiative involves deployment workflows. Consider adding `flow:lifecycle` to trace the deployment process end-to-end. Deployment validators that don't understand the deployment flow may miss sequence-dependent failures."
- Artifact dependencies: `draft:spec` consumes `prove:synthesize` output — dependency is explicit via `depends_on` (pass). `review:design` consumes `draft:spec` output — dependency is explicit (pass). `review:code` consumes implementation — dependency on `build` stage is explicit (pass).
- Empty stages: `build` has no skills but has a note — acceptable (outside plugin scope).
- Skill internal sequencing: `prove:` stage lists hypothesis, experiments, and synthesize — the internal sequencing of prove is respected (hypothesis first, synthesize last). (pass)

One warning generated: "Consider adding `flow:lifecycle` to the review or validate stage."

**Amend**: Lead reviews. Adds `flow:lifecycle` to the validate stage: "Good catch — we should trace the deployment flow to make sure our validator catches sequence-dependent failures." Adjusts validate gate to include flow trace. Re-validates: all checks pass, no warnings. Plan finalized.

Final `program.yaml` written to `program/plan/sim-depval-2026-03-14.yaml`. Human-readable summary written to `program/plan/sim-depval-2026-03-14.md`.

**Tracking**: As skills execute, their artifacts are written with the `depval-` topic prefix. The program dashboard reads all `depval-*.md` files across all namespace artifact directories and shows:

```
depval — AI Deployment Validator
================================
Stage 1: scout .............. [3/3 artifacts] COMPLETE
Stage 2: prove .............. [4/5 artifacts] IN PROGRESS
  - hypothesis .............. done
  - intelligence ............ done
  - analysis ................ done
  - interview ............... done
  - synthesize .............. pending
Stage 3: draft .............. [0/2 artifacts] BLOCKED (depends on: prove)
Stage 4: review ............. [0/3 artifacts] BLOCKED (depends on: draft)
Stage 5: build .............. [outside scope] NOT STARTED
Stage 6: validate ........... [0/3 artifacts] BLOCKED (depends on: build)
Stage 7: listen ............. [0/2 artifacts] BLOCKED (depends on: validate)
```

## Roles

### Stock roles

/program:plan has no stock roles of its own. It is a meta-skill — it orchestrates skills that have their own role systems. The roles active at any point in a program execution are determined by which skill is running:

| Stage | Active Roles | Determined By |
|-------|-------------|---------------|
| scout | PM, Strategy, Market Analyst | /scout: namespace role system |
| prove | Researcher + experiment-specific (interview personas, academic reviewers for publish) | /prove: namespace role system |
| draft | Architect, Author | /draft: namespace role system |
| review | 6 disciplines, 5 personas, 12 customers, domain experts | /review: namespace role system |
| flow | Domain roles (Sales, CRM Admin, etc.) | /flow: namespace role system |
| trace | System roles (Platform Engineer, API Designer, etc.) | /trace: namespace role system |
| listen | Customer personas, Support roles | /listen: namespace role system |

### Custom roles (optional)

/program:plan does not benefit from custom roles directly. However, each skill it orchestrates may use custom roles. If your initiative requires custom experts, personas, or stakeholders, create them in `.roles/{name}/ROLE.md` before running the program — all skills in the program will have access to them.

## Artifacts

```
program/
└── plan/
    ├── sim-depval-2026-03-14.md              # Human-readable plan summary
    ├── sim-depval-2026-03-14.yaml            # Machine-readable program.yaml
    ├── sim-frogs-2026-03-15.md               # Another initiative plan
    ├── sim-frogs-2026-03-15.yaml             # Another initiative program.yaml
    └── sim-onboarding-revamp-2026-03-16.md   # Another initiative
```

The `program.yaml` file is the canonical plan. The `.md` file is a human-readable rendering of the same information, suitable for PR descriptions, stakeholder reviews, and team alignment meetings.

All skill artifacts produced during program execution live in their respective namespace directories (not under `program/`). The topic prefix ties them together:

```
# All artifacts for the depval initiative, across all namespaces:
scout/competitors/depval-competitors-2026-03-14.md
scout/feasibility/depval-feasibility-2026-03-14.md
prove/hypothesis/depval-failure-taxonomy-2026-03-15.md
prove/intelligence/depval-failure-telemetry-2026-03-15.md
prove/synthesize/depval-failure-synthesis-2026-03-16.md
draft/spec/depval-spec-2026-03-16.md
review/design/depval-design-review-2026-03-17.md
review/users/depval-user-walkthrough-2026-03-17.md
review/customers/depval-customer-eval-2026-03-17.md
review/code/depval-code-review-2026-03-20.md
listen/feedback/depval-feedback-2026-03-21.md
```

To find everything for an initiative: `**/{topic}-*.md` (e.g., `**/depval-*.md`).

## Technique Heritage

| Aspect | Technique | What It Contributes |
|--------|-----------|-------------------|
| Stage sequencing | Wave complexity gradient (cross-cutting pattern 1) | The W1 -> W2 -> W3 -> W4 progression (happy path -> composition -> adversarial) maps to stage ordering: scout (explore) -> draft (compose) -> review (validate) -> listen (observe). Each stage increases the commitment level and the cost of rework. |
| Gate criteria | Finding lifecycle (cross-cutting pattern 2) | Gates use the same P1/P2/P3 severity system as findings. A gate fails if P1 findings remain. This is directly from the discipline review finding format. |
| Topic tracking | Session drivers (cross-cutting pattern 6) | Topic prefix is the program-level equivalent of a CLAUDE.md session driver. Just as a session driver enforces vocabulary and tracks progress within a series, the topic prefix enforces naming and tracks progress across an initiative. |
| Plan validation | Hand-compile before automating (cross-cutting pattern 4) | The Findings phase hand-compiles the plan — traces each stage's dependencies, checks gate measurability, identifies missing skills. This is the same technique used in compiler scenario validation: trace the rules manually before running them. |
| Hypothesis-first | Hypothesis-first (cross-cutting pattern 3) | `/program:plan` treats the plan itself as a hypothesis: "We believe this stage sequence will produce a validated, shippable feature." The validation phase tests this hypothesis against known anti-patterns. |
| Multi-step lifecycle | 08 Hypothesis Investigation | The `/prove:` internal sequencing (hypothesis -> experiments -> synthesize -> publish) is the strongest example of multi-step lifecycle. `/program:plan` generalizes this to arbitrary namespace sequences. |

## Cross-Namespace Integration

**This is the integration point.** /program: exists specifically to connect all other namespaces. Every namespace is both an input and an output:

**As orchestrator of other namespaces**:

| Namespace | How /program: Uses It |
|-----------|-----------------------|
| /scout: | Early stages — competitive analysis, feasibility, requirements gathering before design work begins |
| /draft: | Middle stages — spec and proposal writing after scouting confirms the direction |
| /review: | Validation stages — design review after drafting, code review after implementation, user/customer review at multiple points |
| /flow: | Simulation stages — business process simulation to validate that the design handles real workflows |
| /trace: | Simulation stages — system-level tracing to validate architecture, request paths, deployment sequences |
| /prove: | Investigation stages — hypothesis validation when the team disagrees or lacks evidence for a design decision |
| /listen: | Late stages — post-ship (or pre-ship simulated) feedback collection and adoption monitoring |

**As consumer of namespace outputs**:
- Each skill produces artifacts with the topic prefix
- /program:plan reads these artifacts to update the tracking dashboard
- Gate evaluation reads skill artifacts to determine pass/fail
- Stage transitions are triggered when all artifacts for a stage exist and the gate passes

**As the single view of progress**:
- The program dashboard is the only place that shows cross-namespace progress
- Individual namespaces know their own artifacts but not the broader initiative context
- The topic prefix is the glue — it's assigned by /program:plan and consumed by all downstream skills

**Recursive programs**:
A program can include `/prove:` stages that themselves have internal sequencing (hypothesis -> experiments -> synthesize). /program:plan is aware of this internal structure and reflects it in the dashboard (showing individual experiment progress within the prove stage). This is Layer 2 orchestrating Layer 1 skills that have their own internal lifecycle.

**Programs without /program:**:
Users can run individual namespace skills without a program. /program: is optional — it adds orchestration, gating, and tracking but is not required. A developer who just needs a quick `/review:code` can run it directly. /program: is for initiatives that span multiple namespaces and need coordination.

**The dogfood program**:
The simulate plugin itself is being developed using /program:plan. The topic prefix is `sim`. The stages are: scout (validate skill catalog via Q01), prove (validate lifecycle via Q02), draft (write namespace specs — this document), review (persona + customer + design review of specs), build (implement the plugin), validate (code review + trace), listen (adoption monitoring). Every artifact in `simulate\simulations\` uses the `sim-` prefix. This specification is artifact `program/plan/sim-program-2026-03-14.md` — the program describing itself.
