# /narrate-review — Multi-Persona Prose Review With Structural Assessment

Run a multi-persona review on any prose artifact. Reviewers are organized into clusters; the cluster that leads depends on the section type being reviewed. Each reviewer scores against section-appropriate principles. Includes structural assessment: pacing maps, emotional trajectory, missing/excess diagnosis. Proposes up to 5 concrete fixes.

Unlike /narrate-rubric (which scores dimensions) and /narrate-editorial (which finds issues by lens), this skill puts the artifact in front of a panel of named literary voices who each respond from their own aesthetic. The panel composition shifts based on what's being reviewed.

## Usage

```
/narrate-review <artifact> [--section-type narrative|analytical|argument|opening|close]
```

If section type is not specified, infer it from the artifact's content.

## The Reviewer Clusters

Seven clusters of 2-3 voices each. The lead cluster changes based on section type.

| Cluster | Focus | Voices | What They Watch For |
|---------|-------|--------|-------------------|
| A — Rigor | Precision, evidence, honest numbers | Pinker, Taleb, McPhee | Claims without evidence, false precision, hand-waving |
| B — Pace | Momentum, rhythm, reader retention | Didion, Gladwell, Sacks | Where the reader stops, where the page turns itself |
| C — Beauty | Language, image, compression | Dillard, Robinson, Goethe | The sentence that earns its place by sound alone |
| D — Lightness | Play, surprise, the unexpected turn | Calvino, Marquez, Borges | Where the prose takes itself too seriously |
| E — Honesty | Intellectual integrity, self-awareness | Orwell, Sontag, Baldwin | Where the author is performing rather than thinking |
| F — Myth | Narrative structure, archetypal resonance | Campbell, Calasso, Miller | Whether the story's bones are right |
| G — Life | Embodied knowledge, specificity, the real | Darwin, Carson, Lopez | Whether the prose smells like the world or like a library |

### Section Type Lead Clusters

| Section Type | Lead Cluster | Priority Stack |
|-------------|-------------|----------------|
| **Narrative** | F (Myth) + G (Life) | Myth > Life > Pace > Beauty |
| **Analytical** | A (Rigor) + E (Honesty) | Honesty > Rigor > Pace > Beauty |
| **Argument** | A (Rigor) + E (Honesty) | Rigor > Honesty > Pace > Lightness |
| **Opening** | B (Pace) + D (Lightness) | Pace > Lightness > Beauty > Myth |
| **Close** | C (Beauty) + F (Myth) | Beauty > Myth > Honesty > Pace |

The lead cluster's voices get the most weight. All clusters contribute, but secondary clusters do not override the lead.

---

## Protocol

### Phase 1 — Load and Classify

1. Read the full artifact
2. Determine the section type (or use the user's --section-type)
3. Identify the lead cluster and priority stack
4. Select 5-7 reviewers: all voices from the lead cluster + 2-3 voices from secondary clusters that are most relevant to this specific artifact

### Phase 2 — Per-Reviewer Assessment

For each selected reviewer, produce:

```markdown
### {Reviewer Name} (Cluster {X} — {Focus})

**Score: {N}/10**

{2-3 sentence assessment from this reviewer's perspective. What works, what doesn't, in this reviewer's own voice and priorities.}

*"{One-line quote in the reviewer's actual voice — the kind of thing this writer would say about this passage}"*

**Best passage:** "{quoted text}" — {why this reviewer values it}
**Weakest passage:** "{quoted text}" — {what this reviewer would change}
```

Every score must cite the artifact. No scoring on impression.

### Phase 3 — Structural Assessment

Before proposing fixes, assess the artifact's architecture:

**3A. Pacing map:** Break the artifact into beats (3-7 major beats). For each beat:
- What it does (introduces, escalates, lands, transitions)
- Approximate word count
- Whether it earns its length or overstays

Flag any beat taking more than 30% of the word count — it may be compressing others. Flag any beat under 5% — it may be underdeveloped.

**3B. Emotional trajectory:** Map the arc in one line (e.g., "curiosity -> complexity -> doubt -> resolution -> permanence"). Does it build? Plateau? Peak too early? Is there a false climax? Does the landing earn the buildup?

**3C. What's missing:** Name 1-2 things the artifact does NOT do that it should. Be specific: "the second example needs one sentence connecting it back to the opening claim" not "needs better transitions." These are structural gaps, not style violations.

**3D. What should be cut:** Name 0-2 passages that could be removed without loss. Not every artifact has fat — if it's lean, say so. But if a paragraph restates what the reader already knows, or explains what the prose already showed, flag it.

### Phase 4 — Cross-Cluster Synthesis

Identify patterns across reviewers:

- **Universal praise** (3+ reviewers): passages that work for everyone — these are the artifact's strengths, do not touch them
- **Universal friction** (3+ reviewers): passages that bother everyone — highest priority fixes
- **Cluster conflicts**: where one cluster loves what another hates — note both perspectives, the author decides
- **The consensus gap**: the single thing most reviewers agree is missing

### Phase 5 — Propose Up To 5 Fixes

Select the highest-impact fixes. Two types:

**Sentence replacements** (surgical):
- Quote the exact current text with location
- Provide the exact replacement
- Name which reviewer most wants this fix and why
- Apply **the replacement test**: does this fix make the passage better for the reader, or does it just make it more compliant with a rule? If compliance without improvement, do not propose it.

**Structural fixes** (larger):
- Describe what to change and where
- Which structural gap it fills (from 3C) or pacing problem it solves (from 3A)
- Provide draft text if adding, or instructions if restructuring
- Estimate word count impact

Format:

```markdown
**Fix {N} of 5:**
> **Type:** Sentence replacement | Structural addition | Structural cut | Restructure
>
> **Current:** "{exact quote}" (for replacements/cuts)
>
> **Proposed:** "{exact replacement or new text}" (for replacements/additions)
>
> **Instructions:** (for restructures — what to move where)
>
> *Fixes {structural gap or principle}. {Reviewer}: "{one-line rationale}"*
> *Word count impact: +N / -N / net 0*
```

Mix: at least 2 sentence-level fixes AND at least 1 structural fix. If no structural problems exist, say so explicitly and provide all sentence-level fixes.

### Phase 6 — Summary Table

```markdown
| Reviewer | Cluster | Score | Note |
|----------|---------|-------|------|
| {name} | {cluster} | N | {5-word summary} |
| ... | ... | ... | ... |
| **OVERALL** | | **N.N** | |
```

The overall score is the mean of all reviewer scores, weighted by the lead cluster's priority stack. Reviewers in the top-priority cluster get 2x weight.

---

## Key Rules

- **No invented reviewers.** Every voice is a real writer or critic. Each must be consistent with that person's actual aesthetic and critical priorities. If you cannot write in a reviewer's voice accurately, research their work first.
- **Honest scores.** 10 = masterful execution. 8 = works with minor issues. 6 = structural problems. Below 6 = failing. Do not inflate.
- **The replacement test.** Before proposing any fix, ask: does this make the passage better for the reader, or just more rule-compliant? If compliance without improvement, drop it.
- **Structural assessment is mandatory.** The pacing map (3A), emotional trajectory (3B), missing elements (3C), and excess elements (3D) are always included. They are the foundation the fixes are built on.
- **Section type matters.** An analytical section is judged by Rigor and Honesty. A narrative section is judged by Myth and Life. Do not apply the wrong cluster's priorities to the wrong section type.
- **Word counts are exact.** Count specific repeated words when flagging issues. Vague claims ("too repetitive") are not actionable.
- **Cluster conflicts are findings, not problems.** When Rigor loves what Lightness hates, that tension is informative. Report both views — the author decides.

## Input

- **artifact**: Path to the prose artifact to review
- **section-type**: (optional) narrative, analytical, argument, opening, or close. Inferred if omitted.

## Output

Multi-persona review with per-reviewer scores, structural assessment (pacing map, emotional trajectory, gaps, excess), cross-cluster synthesis, and up to 5 concrete fixes.

Write artifact to: signals/narrate/{topic}-review-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: narrate-review, topic: {topic}, date: {date}, section_type: {type}, lead_cluster: {cluster}, reviewers: {n}, overall_score: {n.n}, p1_fixes: {n}, structural_verdict: {reorder|restructure|leave-as-is}
