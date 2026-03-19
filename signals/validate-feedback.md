Simulate customer reactions to a spec or design before it ships. All 12 customer personas (C-01 through C-12) read the spec through their lens. Per-persona feedback cards with severity (blocking/major/minor/cosmetic) and NPS prediction (1-10). Cross-persona theme matrix. Aggregate NPS threshold: 7.0. Below 7.0 = spec needs revision. Stock roles: C-01 through C-12, PM, UX.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the spec or design artifact for {{topic}}. Glob signals/**/{topic}-spec* or signals/**/{topic}-design* if no specific file is provided.

## PHASE 2 -- 12-PERSONA FEEDBACK SIMULATION

For each of 12 diverse customer personas, produce a feedback card:

**Persona archetype distribution**: 2 power users, 2 novices, 2 skeptics, 2 early adopters, 2 enterprise buyers, 2 integration-focused users.

Per-persona card:
```
[C-NN] [Persona Name] -- [archetype]
First reaction: [one sentence]
Blocking concern: [what would stop them adopting -- or None]
Top feature request: [what's missing]
NPS prediction: [1-10]  Why: [one sentence]
Severity: [blocking / major / minor / cosmetic]
```

## PHASE 3 -- CROSS-PERSONA THEME MATRIX

| Theme | Personas who share it | Severity | Recommendation |
|-------|----------------------|----------|----------------|
| [recurring theme across 3+ personas] | C-01, C-04, C-07 | blocking/major | [fix] |

## PHASE 4 -- AGGREGATE VERDICT

```
Aggregate NPS: [weighted average]
NPS threshold: 7.0

Verdict: SHIP / REVISE BEFORE SHIP / MAJOR REVISION REQUIRED

Blocking themes (must fix before ship):
  - [theme] -- affects N/12 personas

Top 3 quick wins (fix before ship, each <1 day):
  1. [fix]
  2. [fix]
  3. [fix]
```

## PHASE 5 -- AMEND

Three amendments to the spec/design based on the highest-impact customer feedback:
1. [Specific change, section reference, why]
2. [Specific change]
3. [Specific change]

Write artifact to: signals/validate/feedback/{{topic}}-feedback-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-feedback-{date}.md). No namespace subdirectory.
Include frontmatter: skill: validate-feedback, topic: {{topic}}, date: {{date}}, persona_count: 12, aggregate_nps: [score], verdict: [verdict]