# Metrics Specification

**Topic**: signal
**Namespace**: /metrics:
**Skills**: 5
**Default mode**: Lightweight
**Audience**: PMs, team leads, data scientists -- anyone who needs to report
pre-ship predicted scores and compare them to post-ship actuals.

---

## Purpose

/metrics: aggregates simulation signals into Microsoft-compatible measurement scores.
Every persona-based skill (review:customers, listen:feedback, prove:interview) produces
raw NPS and NSAT observations. /metrics: synthesizes them into the headline numbers
you present to leadership -- and the baselines you compare to OCV/Floodgate post-ship.

Signal is a pre-ship measurement instrument. /metrics: makes that explicit.

---

## Microsoft Metrics Standards (from internal sources)

**NPS**: "How likely are you to recommend [feature] to a friend or colleague?" (0-10)
- Detractors 0-6 | Passives 7-8 | Promoters 9-10
- Score = %Promoters - %Detractors (range -100 to +100)
- Delivered post-ship via OCV / Floodgate

**NSAT**: "Overall, how satisfied are you with [feature]?" (1-10)
- NSAT % = responses 7-10 / total
- Developer tools prefer NSAT over NPS -- internal users are captive, advocacy
  logic breaks down. NSAT measures friction, not loyalty.
- Delivered post-ship via OCV / Floodgate or Engineering Thrive survey

**Telemetry adoption**: DAU, WAU, skill invocation count, time-to-first-value
- Measured via Tool Usage Telemetry Framework (maturity stage 2+)
- Signal v0.1: no telemetry instrumentation (roadmap item)

---

## Skills

### /metrics:nps

**What**: Aggregate NPS predictions from all simulation signals for a topic.
**Input**: Topic name. Reads all `simulations/**/[topic]-*.md` artifacts.
**Output**: `simulations/{topic}/metrics-nps-{date}.md`

For each simulation signal that contains NPS predictions:
- Extract per-persona scores and categories (promoter/passive/detractor)
- Identify which personas are in the primary audience (3x weight), secondary (2x), non-target (1x)
- Compute weighted NPS: %weighted_promoters - %weighted_detractors
- Flag divergence: signals that disagree by more than 20 NPS points

Output:
```
## NPS Summary: {topic}

| Signal | Run | Primary NPS | All-persona NPS | Confidence |
|--------|-----|------------|----------------|-----------|
| review:customers | 2026-03-14 | +45 | +12 | HIGH (12 personas) |
| listen:feedback  | 2026-03-14 | +38 | +8  | MEDIUM (4 personas) |
| prove:interview  | 2026-03-14 | +52 | +24 | LOW (3 interviews)  |

Aggregate predicted NPS: +33 (range: +8 to +52)
Primary audience NPS: +45 (developers, architects, SREs)
Confidence: MEDIUM -- 3 signals, primary audience consistent within 15 points

Post-ship target (for /goals:okr): NPS >= +25
OCV survey question: "How likely are you to recommend [feature] to a friend or colleague?"
```

### /metrics:nsat

**What**: Aggregate NSAT predictions from all simulation signals for a topic.
**Input**: Topic name.
**Output**: `simulations/{topic}/metrics-nsat-{date}.md`

Microsoft NSAT standard: 1-10 scale. Satisfied = 7-10. NSAT% = (7-10 count) / total.

For each simulation signal:
- Extract per-persona satisfaction scores (usability scores, would-adopt, explicit ratings)
- Convert to 1-10 NSAT scale if needed (e.g., usability 4/5 -> NSAT 8/10)
- Compute NSAT% overall and for primary audience separately

Output:
```
## NSAT Summary: {topic}

| Signal | Run | Primary NSAT% | All NSAT% |
|--------|-----|--------------|---------|
| review:customers | 2026-03-14 | 87% | 58% |
| listen:feedback  | 2026-03-14 | 82% | 54% |

Aggregate NSAT%: 85% primary, 56% all-persona
Microsoft threshold: 7-10 = satisfied. Primary audience at 85% is healthy.
All-persona at 56% reflects correct non-target positioning (makers, executives).

Post-ship target (for /goals:okr): Primary NSAT >= 75%
OCV survey question: "Overall, how satisfied are you with [feature]?"
```

### /metrics:adoption

**What**: Adoption curve prediction from listen:adoption signals.
**Input**: Topic name.
**Output**: `simulations/{topic}/metrics-adoption-{date}.md`

Reads listen:adoption artifacts. Extracts:
- Month 1, 3, 6 projections (absolute and % of target)
- Chasm risk: the gap between early adopters and early majority
- Champion personas: who spreads it and to how many
- Churn risk: who tries and abandons

Output:
```
## Adoption Prediction: {topic}

| Horizon | Predicted Users | % of Target | Phase |
|---------|----------------|-------------|-------|
| Month 1 | 400 | 8% | Innovators |
| Month 3 | 1,800 | 36% | Early Adopters |
| Month 6 | 3,100 | 62% | Early Majority |

Chasm risk: D365 specialists (understand methodology) vs. broader engineering
  (don't have the vocabulary). Bridge: starter templates + guided first-run.

Champions: C-02 James (8-10 developers), C-09 Lisa (5-6 SREs), C-04 David (12-15 PMs)
Churn risk: C-01 Maria (day 3, jargon + no wizard), C-07 Catherine (never tries, no ROI frame)

Post-ship target (for /goals:okr): 50% of target audience within 6 months
```

### /metrics:sla

**What**: Reliability predictions from flow:resilience and trace:state signals.
**Input**: Topic name.
**Output**: `simulations/{topic}/metrics-sla-{date}.md`

Reads flow:resilience, trace:deployment, trace:state artifacts. For each failure mode:
- Severity: blocking (feature unusable), degraded (feature impaired), cosmetic
- Recovery path: does one exist? How long?
- MTTR estimate: mean time to recovery

Computes implied reliability ceiling:
- If a blocking failure has no recovery path: SLA < 99.9% is the ceiling
- If all failure modes have sub-1-hour recovery: 99.9% SLA is achievable

Output:
```
## Reliability Prediction: {topic}

### Failure Mode Inventory
| Failure | Severity | Recovery Path | MTTR | SLA Impact |
|---------|----------|--------------|------|-----------|
| skill produces empty artifact | blocking | re-run | <5min | -0.1% |
| trace artifact missing | degraded | run trace-skill | <30min | -0.01% |

### Implied SLA Ceiling
All failure modes have recovery paths under 1 hour.
Implied SLA ceiling: 99.9% (8.7 hours downtime/year) is achievable.
Note: Signal is a local CLI tool -- "uptime" = skill execution success rate.
Recommended SLA definition: >=99% of skill invocations produce a valid artifact.

Post-ship target (for /goals:sla): 99% skill execution success rate
```

### /metrics:dashboard

**What**: Single pre-ship metrics view -- all four metrics for a topic in one document.
**Input**: Topic name. Optional: --format teams for ASCII card.
**Output**: `simulations/{topic}/metrics-dashboard-{date}.md`

Calls metrics:nps, metrics:nsat, metrics:adoption, metrics:sla and produces a single
summary dashboard. The dashboard format matches what leadership expects at a review.

```
## Pre-Ship Metrics Dashboard: {topic}
As of {date}. Signals analyzed: {N}.

NPS     +33   (primary: +45)   TARGET: +25   STATUS: ON TRACK
NSAT    85%   (primary: 87%)   TARGET: 75%   STATUS: ON TRACK
ADOPT   62%   (month 6)        TARGET: 50%   STATUS: ON TRACK
SLA     99%   (predicted)      TARGET: 99%   STATUS: ON TRACK

Post-ship measurement: OCV survey in week 2 (NPS) and week 4 (NSAT).
Telemetry adoption: Tool Usage Telemetry Framework, DAU/WAU from month 1.
```

---

## Artifact Layout

```
simulations/{topic}/
  metrics-nps-{date}.md
  metrics-nsat-{date}.md
  metrics-adoption-{date}.md
  metrics-sla-{date}.md
  metrics-dashboard-{date}.md
```

---

## Cross-Namespace Integration

- **review:customers -> metrics:nps, metrics:nsat**: primary source of persona scores
- **listen:feedback -> metrics:nsat**: secondary NPS/NSAT source
- **listen:adoption -> metrics:adoption**: primary source of adoption predictions
- **prove:interview -> metrics:nps**: strongest signal (real conversation, explicit scores)
- **flow:resilience + trace:state -> metrics:sla**: failure mode inventory
- **metrics:* -> goals:okr**: metrics predictions become the evidence base for OKR targets
