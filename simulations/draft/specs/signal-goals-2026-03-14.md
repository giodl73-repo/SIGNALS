# Goals Specification

**Topic**: signal
**Namespace**: /goals:
**Skills**: 3
**Default mode**: Full
**Audience**: PMs, leads, anyone who sets OKRs, SLAs, or presents commitments to leadership.

---

## Purpose

/goals: helps teams design business commitments they can defend.

The problem: OKRs and SLAs are usually set by negotiation and gut feel. A PM proposes
"NPS > +30" because it sounds ambitious. Leadership pushes back with "+50." Neither has
evidence. The OKR lands somewhere in the middle -- still ungrounded.

Signal changes this. After running simulations, you have predicted NPS, NSAT, and
adoption numbers with variance ranges and confidence levels. /goals: reads those
predictions and helps you set targets that are:
- **Informed**: grounded in simulation evidence, not negotiation
- **Defensible**: you can show the evidence behind every target
- **Testable**: each target maps to an OCV survey question or telemetry metric
- **Honest**: the confidence range is shown, not hidden

The output of /goals: is a commitment brief that you take to your VP. Not "we think NPS
will be +30." Instead: "Three simulation signals predict primary audience NPS between
+38 and +52. We're committing to +35 as our 6-month target. Here's our measurement plan."

---

## Skills

### /goals:okr

**What**: Design OKR targets grounded in simulation predictions.
**Stock roles**: PM, Strategy, Architect (for technical OKRs)
**Input**: Topic name. Reads metrics signals for the topic.
**Output**: `simulations/{topic}/goals-okr-{date}.md`

**Lifecycle**:
- Setup: Read the metrics dashboard for the topic. Identify which metrics have simulation
  predictions (NPS, NSAT, adoption, SLA). For each metric: what is the predicted range?
  What is the confidence level (LOW/MEDIUM/HIGH)?

- Execute: For each metric with predictions, propose three OKR variants:
  - **Conservative**: lower bound of predicted range. Achievable even if simulations
    over-predicted. Example: NPS predicted +38 to +52 -> conservative target: +30
  - **Target**: mid-range. What a successful launch looks like. Example: +40
  - **Stretch**: upper bound. Requires everything going right. Example: +50

  For each variant, show: the prediction it's based on, what would need to be true for
  it to be achieved, and what would cause it to miss.

- Findings: Recommended OKR set (one per metric). Each OKR in standard format:
  - Objective (qualitative, 1 sentence)
  - Key Result (quantitative, measurable, time-bounded)
  - Evidence (which simulation signal grounds the target)
  - Measurement plan (OCV survey, telemetry, or other)
  - Risk (what would cause this KR to miss)

- Amend: PM adjusts targets up/down, adds business context the simulation didn't see
  (e.g., "leadership wants stretch goals this half"), or adds non-simulation KRs.

**Example output**:
```
## OKR Draft: Signal All-Hands Launch

### Objective: Ship Signal as the go-to pre-build investigation tool for Dynamics developers

**KR-01**: Primary audience NPS >= +35 within 90 days of all-hands
- Evidence: review:customers predicted +45, prove:interview predicted +52
- Conservative: +25 | Target: +35 | Stretch: +45
- Measurement: OCV Floodgate survey, week 8 post-launch
- Risk: Stub skill bodies at launch (critical finding from user testing). If skills
  ship without golden prompts, NPS may fall below +10.

**KR-02**: Primary audience NSAT >= 75% within 90 days
- Evidence: review:customers predicted 87%, listen:feedback predicted 82%
- Conservative: 65% | Target: 75% | Stretch: 85%
- Measurement: OCV survey "Overall satisfied with Signal?" (1-10, 7-10 = satisfied)
- Risk: No ADO integration means findings don't connect to work items (F-03 from interview).

**KR-03**: 50% of all-hands target audience installs Signal within 6 months
- Evidence: listen:adoption predicted 62% at month 6
- Conservative: 40% | Target: 50% | Stretch: 65%
- Measurement: Telemetry (Tool Usage Telemetry Framework, DAU)
- Risk: No install script (FL-06). Manual installation of 52 SKILL.md files is blocking.

**KR-04**: Zero P0 support tickets in first 30 days
- Evidence: listen:support predicted 0 P0 tickets (Signal is local, no server to fail)
- Measurement: Internal support queue review
- Risk: claude -p failures outside Signal's control (relay or auth issues)
```

### /goals:sla

**What**: Define SLA targets grounded in resilience simulation predictions.
**Stock roles**: Architect, SRE
**Input**: Topic name. Reads metrics:sla signals for the topic.
**Output**: `simulations/{topic}/goals-sla-{date}.md`

**What SLA means for a CLI tool** (important distinction from SaaS):
- Signal is a local tool. There is no server to be down.
- "SLA" for Signal = skill execution success rate + artifact correctness rate
- 99.9% SLA = 99.9% of skill invocations produce a valid, correctly-formatted artifact
- Violations: skill crashes, produces empty artifact, produces malformed frontmatter

**Lifecycle**:
- Setup: Read metrics:sla signal. Identify all failure modes and their recovery paths.
- Execute: Architect maps failure modes to SLA impact. SRE defines the measurement
  approach (how do we know when a skill fails?). Together they propose:
  - SLA definition: what constitutes a successful skill invocation
  - SLA target: the % of invocations that must succeed
  - Error budget: how many failures are acceptable per period
  - Incident definition: what triggers an SLA violation alert

- Findings: SLA brief with definition, target, error budget, measurement plan, and
  escalation path when violated.

**Example output**:
```
## SLA Definition: Signal

**Service**: Signal skill execution (any /signal:* invocation)
**SLA**: 99% of invocations produce a valid artifact within 60 seconds
**Error budget**: 1% of invocations = ~50 failures per 5,000-user all-hands in month 1

**Success definition**: Invocation produces a Markdown artifact with:
- Valid frontmatter (skill, topic, item, date fields present)
- Non-empty findings section
- Artifact written to correct simulations/ subdirectory

**Failure categories**:
| Category | Example | Recovery |
|----------|---------|---------|
| Skill crash | claude -p exits non-zero | Re-run (user action) |
| Empty artifact | Skill writes 0-byte file | Re-run (user action) |
| Malformed frontmatter | Missing required field | Re-run or manual fix |
| Wrong directory | Artifact in wrong namespace dir | Move file (user action) |

**Measurement**: Git commit history (artifact was created = success) +
  optional telemetry instrumentation (future)

**Escalation**: If >5% failure rate in first week: halt all-hands follow-up
  and diagnose skill body quality issue.
```

### /goals:commit

**What**: Generate the leadership brief -- what we're committing to and why.
**Stock roles**: PM, Strategy
**Input**: Topic name. Reads OKRs from goals:okr and SLA from goals:sla.
**Output**: `simulations/{topic}/goals-commit-{date}.md`

**What it produces**: A 1-page brief suitable for a VP review or an OKR planning meeting.
Format:
- What we're shipping (1 sentence)
- Why we're confident (3 simulation findings that ground the targets)
- What we're committing to (KRs with targets and measurement plans)
- What would cause us to miss (top 2 risks with mitigations)
- What we need (asks from leadership)

This is the artifact that closes the Signal loop for a PM: investigation → validation →
metrics prediction → commitment → ship → measure → compare.

**Example output**:
```
# Signal All-Hands Launch: Commitment Brief
Prepared for: VP Engineering review
Date: 2026-03-14

## What we're shipping
Signal -- a skills-in-repo pre-build investigation tool for Dynamics developers.
Copy one SKILL.md file. Run it. Get a competitive analysis, feasibility assessment,
or system trace in minutes, not days.

## Why we're confident
1. Primary audience (developers, architects, SREs) gave simulated would-adopt of 4.5/5
   across 12 customer personas and 3 in-depth developer interviews.
2. Copilot Studio developers immediately connected /flow:conversation to their daily work.
   No explanation needed.
3. Compliance story is strong: git-native, no server, no data persistence. Signal
   adopted for free once Claude Code is approved.

## What we're committing to
| Metric | Target | Measurement | Confidence |
|--------|--------|------------|-----------|
| Primary NPS | >= +35 at 90 days | OCV Floodgate, week 8 | MEDIUM |
| Primary NSAT | >= 75% at 90 days | OCV survey, week 8 | HIGH |
| Adoption | 50% at 6 months | Telemetry (DAU) | MEDIUM |
| SLA | 99% skill success | Git artifact audit | HIGH |

## What would cause us to miss
1. **Stub skill bodies shipped** (critical): If skills ship without golden prompts,
   NPS drops below +10. Mitigation: quest loop must complete for all 52 skills before launch.
2. **No install script** (major): Manual installation of 52 files is blocking for PMs.
   Mitigation: signal-install.sh before all-hands.

## What we need
- 30 minutes at all-hands for live demo (Dev Lead champion needed)
- Claude Code approval in IT tooling catalog before launch
- OCV survey slot in week 8 post-launch
```

---

## Artifact Layout

```
simulations/{topic}/
  goals-okr-{date}.md
  goals-sla-{date}.md
  goals-commit-{date}.md
```

### /goals:pr

**What**: Generate a Product Review (PR) packet for executive review using Signal signals.
Fills the AX&E PR Template structure from simulation predictions.
**Input**: Topic name. Reads all simulation signals + metrics + OKRs for the topic.
**Output**: `simulations/{topic}/goals-pr-{date}.md`

**PR Template sections Signal fills**:

| Section | Source signals |
|---------|---------------|
| 1. Executive Summary | goals:commit (one-line outcome, status) |
| 2. Business Context | scout:competitors (market), scout:requirements (customer problem) |
| 3. Goals & Success Metrics | goals:okr (targets vs actuals) + metrics:dashboard |
| 4. Progress Since Last Review | topic:status (signals gathered vs planned) |
| 5. Adoption & Customer Signals | listen:adoption (predictions) + review:customers (NPS/NSAT) |
| 6. Risks & Asks | findings register (P1/P2 findings from all signals) + decisions needed |

Sections Signal CANNOT fill (require human input):
- Actual shipped features (Signal predicts, doesn't track what shipped)
- Budget/headcount (outside simulation scope)
- Demo snapshot (human must record)

### /goals:msr

**What**: Generate a Monthly Service Review (MSR) metrics packet.
Fills the MSR BIC Project Standard format from Signal metrics signals.
**Input**: Topic name. Month being reviewed.
**Output**: `simulations/{topic}/goals-msr-{date}.md`

Signal feeds MSR with:
- NSAT % trend (predicted pre-ship or actual if post-ship data is provided)
- SLA compliance (99% skill execution target from goals:sla)
- Adoption rate (month-over-month from listen:adoption)
- Top support ticket categories (predicted from listen:support)
- P1 findings status (open/closed from findings register)

### /goals:xr

**What**: Generate an Experience Review (XR) packet focused on customer experience.
XR format: customer signals, friction analysis, NPS/NSAT, top verbatims.
**Input**: Topic name.
**Output**: `simulations/{topic}/goals-xr-{date}.md`

Signal feeds XR with:
- review:customers output (12 persona evaluations with scores + verbatims)
- prove:interview output (direct developer voice -- most credible for XR)
- listen:feedback output (simulated post-ship reactions)
- review:users output (5 persona advocates -- usability friction)

XR is where Signal's persona simulation work is most directly usable.
Every first-person persona reaction is a potential XR verbatim.

---

## Cross-Namespace Integration

- **metrics:* -> goals:okr**: metrics predictions are the evidence base for every KR
- **goals:okr -> goals:commit**: OKRs roll up into the leadership brief
- **goals:sla -> goals:commit**: SLA definition included in the brief
- **program:plan -> goals:okr**: the program plan's gates can become OKR milestones
- **prove:hypothesis -> goals:okr**: investigation findings ground the "why we're confident" section
- **goals:commit -> program:plan**: leadership approval of the brief = gate to build
