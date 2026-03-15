# Metrics Specification

**Topic**: signal
**Namespace**: /topic: (extension -- topic:metrics)
**Default mode**: Lightweight
**Audience**: PMs, team leads, anyone presenting Signal results to leadership

---

## Purpose

Signal is a pre-ship measurement instrument. Every simulation skill that involves
personas produces predicted NPS and NSAT scores using Microsoft's exact question
wording. After you ship, OCV/Floodgate measures the same questions with real users.
You compare. The prediction-to-reality gap is the most valuable signal Signal produces.

---

## Microsoft Metrics Framework (from internal sources)

### NPS -- Net Promoter Score

**Question**: "How likely are you to recommend [Signal] to a friend or colleague?"
**Scale**: 0-10
**Buckets**: Detractors 0-6 | Passives 7-8 | Promoters 9-10
**Formula**: NPS = %Promoters - %Detractors (range: -100 to +100)
**Post-ship measurement**: OCV / Floodgate survey

### NSAT -- Net Satisfaction Score

**Question**: "Overall, how satisfied are you with [Signal]?"
**Scale**: 1-10
**Formula**: NSAT % = (responses 7-10) / total responses
**Threshold**: 7-10 = Satisfied, 1-6 = Not Satisfied
**Post-ship measurement**: OCV / Floodgate (or Engineering Thrive survey if internal tool)
**Note**: Microsoft developer tools prefer NSAT over NPS because internal users are
"captive" -- advocacy logic breaks down when users cannot easily switch tools.
NSAT measures friction and satisfaction, not loyalty.

### Telemetry Adoption

**Metrics**: DAU (daily active users), WAU (weekly active users), skill invocation
count, installation count, time-to-first-value (minutes from install to first artifact)
**Post-ship measurement**: Tool Usage Telemetry Framework (maturity stage 2+)
**Note**: Signal SKILL.md files need telemetry instrumentation to produce these metrics.
Not in v0.1 scope but on the roadmap.

---

## How Signal Produces Predicted Metrics

### review:customers
Each persona provides:
- NPS prediction: "How likely to recommend?" (0-10)
- Usability score: maps to NSAT (1-5 → 2-10)
- Verbatim reaction (the "why" behind the score)

Aggregated output:
```
Predicted NPS:  +32  (12 personas, 4 promoters, 3 detractors)
Predicted NSAT: 67%  (8 of 12 personas scored 7-10 equivalent satisfaction)
Primary audience NSAT: 87% (all 4 primary personas satisfied)
```

### listen:feedback
Each of the 12 personas provides:
- NPS prediction: "Would you recommend this?" (0-10)
- Satisfaction assessment: blocking/major/minor/cosmetic finding severity
- Verbatims

### prove:interview
Each interview subject provides:
- NPS prediction (explicit in interview)
- NSAT prediction based on observed friction and delight signals
- Verbatims (most valuable -- the "why" behind the score)

---

## /topic:metrics

**What**: Aggregate all simulated NPS and NSAT predictions across a topic's signals
into a single pre-ship metrics dashboard.

**Input**: Topic name
**Output**: `simulations/{topic}/metrics-{date}.md` with:

```
# Pre-Ship Metrics: {topic}
As of {date}. Based on {N} simulation signals.

## Predicted NPS
| Signal | Run | Primary NPS | All-persona NPS |
|--------|-----|------------|----------------|
| review:customers | 2026-03-14 | +45 | +12 |
| listen:feedback | 2026-03-14 | +38 | +8 |
| prove:interview | 2026-03-14 | +52 | +24 |

Aggregate predicted NPS: +33 (range: +8 to +52)
Confidence: MEDIUM (3 signals, primary audience consistent)

## Predicted NSAT
| Signal | Primary NSAT% | All NSAT% |
|--------|--------------|---------|
| review:customers | 87% | 58% |
| listen:feedback | 82% | 54% |

Aggregate predicted NSAT: 85% primary, 56% all-persona
Microsoft threshold: 7-10 = satisfied. Primary audience at 85% is healthy.

## NPS Verbatim Themes (top 3 from all signals)
1. "Skills-in-repo install is exactly how I want this to work" (C-02, C-09 -- delight)
2. "Stub skill bodies kill credibility with architects" (Amara interview -- P1 blocker)
3. "No ADO integration -- findings don't connect to work items" (Ravi interview -- major)

## Post-Ship Measurement Plan
When Signal ships at all-hands:
- Week 2: Run OCV NPS survey via Floodgate ("How likely to recommend Signal?")
- Week 4: Run NSAT survey ("Overall satisfied with Signal?")
- Month 3: Pull telemetry adoption data (DAU, skill invocations)
- Compare to predicted values above

Target: Predicted NPS +33 -> Actual NPS >= +25 (within 10 points)
Target: Predicted NSAT 85% -> Actual NSAT >= 75% (within 10 points)
```

**Lifecycle** (always Lightweight -- metrics aggregation is fast):
- Glob all signals for the topic: `simulations/**/{topic}-*.md`
- Extract NPS and NSAT predictions from frontmatter and findings sections
- Compute aggregates weighted by signal type (interview > customers > feedback)
- Write metrics dashboard
- Generate post-ship measurement plan with OCV/Floodgate survey templates

---

## Standardized Score Block

Every simulation skill that involves personas MUST include this block in its artifact:

```markdown
## Predicted Metrics

**NPS** (0-10 scale, "How likely to recommend?"):
| Persona | Score | Category |
|---------|-------|---------|
| C-02 James | 9 | Promoter |
| C-09 Lisa | 9 | Promoter |
| C-01 Maria | 2 | Detractor |
...
**Aggregate NPS**: +33 (4 promoters, 3 detractors, 5 passives)

**NSAT** (1-10 scale, "Overall satisfied?"):
| Persona | Score | Satisfied? |
|---------|-------|-----------|
| C-02 James | 9 | Yes |
| C-09 Lisa | 10 | Yes |
| C-01 Maria | 2 | No |
...
**Aggregate NSAT%**: 67% (8 of 12 personas scored 7-10)
**Primary audience NSAT%**: 87% (4 of 4 primary personas scored 7-10)

**Top verbatims** (most impactful, positive and negative):
- [POSITIVE] "..." (C-02)
- [NEGATIVE] "..." (C-01)
```

This block makes Signal artifacts directly compatible with Microsoft's OCV/Floodgate
post-ship measurement. Pre-ship predicted scores vs. post-ship actual scores = the
Signal feedback loop.

---

## --metrics flag

Any simulation skill that involves personas supports `--metrics` to produce a JSON
sidecar with just the scores:

```json
{
  "skill": "signal:review",
  "skill_variant": "customers",
  "topic": "frogs",
  "date": "2026-03-14",
  "nps": {
    "score": 33,
    "promoters": ["C-02", "C-09", "C-10"],
    "passives": ["C-03", "C-04", "C-08", "C-11"],
    "detractors": ["C-01", "C-06", "C-07", "C-12"]
  },
  "nsat": {
    "pct_satisfied": 0.67,
    "pct_primary_satisfied": 0.87,
    "scale": "1-10",
    "threshold": 7
  },
  "verbatims": {
    "top_positive": "Skills-in-repo install is exactly how I want this to work",
    "top_negative": "Stub skill bodies kill credibility with architects"
  }
}
```

This JSON is ingested by Power BI, ADO dashboards, or any Microsoft telemetry tooling.
Makes Signal's predictions a first-class input to Microsoft's measurement infrastructure.

---

## SHIPPING.md update

Add to v0.1 shipping criteria:
- [ ] Every persona-based skill artifact includes the Predicted Metrics block
- [ ] `--metrics` flag produces JSON sidecar on all persona-based skills
- [ ] `/topic:metrics` added to topic namespace (7th topic skill)
- [ ] Post-ship OCV/Floodgate survey templates written and linked from QUICKSTART.md
