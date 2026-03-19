You are running /discover-synthesize for: {{topic}}

Synthesize findings across all signal artifacts into a cross-signal insight.
Requires at least 2 prior signal artifacts to be meaningful.
The synthesis is the deliverable -- it supersedes individual signals.

---

## PHASE 1: SIGNAL INVENTORY

Glob signals/**/{topic}-* and read all artifacts found.

For each artifact, extract the single most important finding:

| Signal | Artifact Path | Key Finding | Verdict / Score |
|--------|--------------|-------------|-----------------|
| [e.g., discover-competitors] | [path] | [one sentence] | [e.g., HIGH threat] |
| [e.g., discover-feasibility] | [path] | [one sentence] | [e.g., FEASIBLE WITH CAVEATS] |
| [e.g., discover-risk]        | [path] | [one sentence] | [e.g., HIGH inertia risk] |
| [e.g., discover-hypothesis]  | [path] | [one sentence] | [e.g., OPEN / confidence 65] |

Signal count: [N]

If fewer than 2 signals found: stop and report "Insufficient signals for synthesis. Run at least 2 discover skills first."

---

## PHASE 2: AGREEMENT AND CONFLICT MAP

**Signals that agree** (3+ signals pointing the same direction):
- [Pattern]: [Which signals support it, one sentence each]
- [Pattern]: [Which signals support it, one sentence each]

**Signals that conflict** (2+ signals pointing opposite directions):
- [Conflict]: [Signal A says X. Signal B says Y. One sentence on why they diverge.]
- [Conflict]: [Signal A says X. Signal B says Y. Resolution: [which to weight more and why]]

**Signals that are isolated** (findings that appear in only one signal, not corroborated):
- [Finding]: [From which signal. Why it may or may not matter.]

---

## PHASE 3: CROSS-SIGNAL INSIGHTS

Extract 3-5 insights that are only visible when looking across signals together.
These are things no single signal could have surfaced alone.

**Insight 1**: [State the cross-signal observation. Which signals does it draw from?]
Implication: [What does this mean for the feature decision?]

**Insight 2**: [State the cross-signal observation. Which signals does it draw from?]
Implication: [What does this mean for the feature decision?]

**Insight 3**: [State the cross-signal observation. Which signals does it draw from?]
Implication: [What does this mean for the feature decision?]

[Add Insight 4-5 if --depth deep or if signal count >= 5]

---

## PHASE 4: DECISION IMPLICATION

**Answer**: PROCEED | PAUSE | PIVOT
**Confidence**: [0-100]

**Rationale**: [2-3 sentences. What do the signals say together? What is the dominant pattern?]

**The case for proceeding**: [One sentence drawn from supporting signals]
**The case for pausing**: [One sentence drawn from risk or conflict signals]
**The case for pivoting**: [One sentence -- what would a scoped alternative look like?]

**Recommendation**: [Final recommendation in one sentence. Be direct.]

**Signal gaps**: What discover skills have NOT been run that would most change this synthesis?
- [Missing signal]: [What question it would answer]
- [Missing signal]: [What question it would answer]

---

## PHASE 5: AMEND

3 improvements to this synthesis:

1. **Weight by recency**: If signals span multiple dates, weight newer signals more heavily -- the team may have learned something that makes older signals obsolete.

2. **Run the missing signal**: If one gap signal would resolve a conflict from Phase 2, run it before committing to the PROCEED/PAUSE/PIVOT recommendation.

3. **Reframe for audience**: The synthesis as written is neutral. Add --for exec to front-load cost/risk framing, or --for engineer to front-load implementation feasibility.

---

Write artifact to: signals/discover/synthesize/{{topic}}-synthesize-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-[this-skill]-{date}.md). No namespace subdirectory.
Include frontmatter: skill: discover-synthesize, topic: {{topic}}, date: {{date}}, signal_count: [n]
