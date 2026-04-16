# /editorial-triple-pass — Three Editorial Lenses on Any Prose

Run three independent editorial lenses on a prose artifact. Each lens produces a terse findings list with line numbers, quoted text, and severity ratings.

## Usage

```
/editorial-triple-pass <artifact>
```

## Protocol

Read the artifact in full before running any lens.

---

### Lens 1 — Judgment Auditor

Scan for the author's hidden perspective: words that reveal assumptions, framings that position the subject relative to an unstated default, evaluative language disguised as description.

Look for:
- **Unmarked defaults**: Language that treats one perspective as normal and others as deviations
- **Smuggled evaluation**: Adjectives that sound descriptive but encode judgment ("primitive", "sophisticated", "surprisingly")
- **Invisible comparisons**: Phrases that position the subject against an unstated reference point ("advanced for its time", "unlike most")
- **Authority claims**: Passages where the author's voice overrides the subject's own terms

Output format:

```markdown
## Judgment Auditor

| # | Line | Quote | Finding | Severity |
|---|------|-------|---------|----------|
| J1 | L42 | "remarkably advanced system" | Smuggled evaluation — implies surprise at competence | P1 |
```

---

### Lens 2 — Voice Keeper

Establish the opening paragraph's register (vocabulary level, sentence rhythm, formality, emotional temperature) as the baseline. Scan the full text for shifts away from that register.

Look for:
- **Textbook drift**: Passages that shift into explanatory, academic mode
- **Lecture mode**: Passages where the author addresses the reader directly to teach
- **Commentary intrusion**: Passages where the author steps out of the narrative to comment on it
- **Register breaks**: Sudden shifts in vocabulary, formality, or sentence structure

Output format:

```markdown
## Voice Keeper

**Baseline register** (from opening): {describe the opening's voice — vocabulary, rhythm, formality}

| # | Line | Quote | Finding | Severity |
|---|------|-------|---------|----------|
| V1 | L67 | "It should be noted that this practice..." | Lecture mode — breaks from narrative into direct instruction | P2 |
```

---

### Lens 3 — Compression Editor

Mark passages where the text is doing unnecessary work: re-explaining what a scene already showed, telling the reader how to feel, clearing its throat before making a point.

Look for:
- **Re-explanation**: A scene or example showed something, then the text explains it again in abstract terms
- **Earned-emotion violations**: The text tells the reader what to feel instead of letting the content earn the response
- **Throat-clearing**: Opening qualifiers, hedges, or preambles that delay the point ("It is worth considering that...")
- **Repetition**: The same idea restated in slightly different words within a short span
- **Unnecessary transitions**: Connective tissue that adds words without adding meaning ("Moving on to the next topic...")

Output format:

```markdown
## Compression Editor

| # | Line | Quote | Finding | Severity |
|---|------|-------|---------|----------|
| C1 | L23-L28 | "The harvest ceremony...This demonstrates the importance of..." | Re-explanation — the ceremony already showed its importance | P2 |
```

---

## Severity Scale

- **P1** (must fix): Actively undermines the artifact's integrity or voice
- **P2** (should fix): Weakens the artifact but doesn't break it
- **P3** (author decides): Stylistic — reasonable people might disagree

## Input

- **artifact**: Path to the prose artifact to review

## Output

Three editorial reports (Judgment Auditor, Voice Keeper, Compression Editor), each with a findings table.

Write artifact to: signals/validate/{topic}-editorial-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: editorial-triple-pass, topic: {topic}, date: {date}, p1_count: {n}, p2_count: {n}, p3_count: {n}, total_findings: {n}
