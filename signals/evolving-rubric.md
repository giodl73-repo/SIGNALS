# /evolving-rubric — Score Artifacts Against a Rubric That Learns

Score any artifact against a rubric that evolves from its own outputs. When a scorer encounters something exceptional that the rubric didn't anticipate, it gets logged as an innovation. After 2+ innovations in the same dimension, the rubric version increments.

## Usage

```
/evolving-rubric <artifact> --rubric <rubric-file>
```

## Protocol

### Phase 1 — Load Rubric

Read the rubric file. Note the current version (e.g., v1.0) and all scored dimensions. If no rubric file exists, ask the user to provide one or create a baseline rubric first.

### Phase 2 — Score Each Dimension

For every dimension in the rubric, score the artifact with specific evidence:

```markdown
### {Dimension Name} — {score}/{max}

**Evidence**: "{quoted text from artifact}"
**Rationale**: {why this score, referencing rubric criteria}
```

Do not score on impression. Every score must cite the artifact.

### Phase 3 — Innovation Detection

While scoring, flag any exceptional technique the rubric didn't anticipate — something that works well but has no home in the current rubric's criteria.

For each innovation:

| Field | Value |
|-------|-------|
| Source | {artifact name} |
| Date | {date} |
| Dimension | {nearest rubric dimension} |
| Description | {what the technique is} |
| Why it works | {why this is effective, with evidence} |

### Phase 4 — Rubric Evolution Check

Count innovations logged against each dimension (including prior scoring sessions if an innovation log exists).

- **0-1 innovations in a dimension**: Note for future tracking. No rubric change.
- **2+ innovations in the same dimension**: Propose a rubric amendment.

Amendment proposal format:

```markdown
## Proposed Amendment: {dimension}
Rubric version: v{current} → v{next}
Trigger: {N} innovations in {dimension}
Sources: {list artifacts that triggered innovations}

### Current criterion
{existing rubric text}

### Proposed criterion
{new rubric text incorporating the innovations}

### Note
New bar applies forward only. Prior scores are unchanged.
```

### Phase 5 — Output

Produce:
1. **Scorecard**: All dimensions with scores and evidence
2. **Innovation log entries**: Any new innovations detected (append to existing log if one exists)
3. **Amendment proposals**: If any dimension hit the 2-innovation threshold

## Input

- **artifact**: The artifact to score (file path or inline text)
- **rubric**: Path to the rubric file (must include version, dimensions, criteria)

## Output

Scorecard with per-dimension scores, optional innovation log entries, optional rubric amendment proposals.

Write artifact to: signals/validate/{topic}-scored-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: evolving-rubric, topic: {topic}, date: {date}, rubric_version: v{N.N}, total_score: {n}/{max}, innovations_logged: {n}, amendments_proposed: {n}
