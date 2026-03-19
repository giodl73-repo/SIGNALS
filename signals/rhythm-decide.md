iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


You are running /rhythm-decide for: {{topic}}

Run the full pre-commitment decision campaign. This orchestrates 6 skills in sequence.
Each produces an artifact. At the end, synthesize into a decision brief.

---

## CAMPAIGN SEQUENCE

Execute in order. Pass each output to the next step as context.

### Step 1: Inertia and Competition
Run discover-inertia and discover-competitors for {{topic}}.
Key question: why would teams do nothing? What named alternatives exist?

### Step 2: Feasibility and Risk  
Run discover-feasibility and discover-risk for {{topic}}.
Key question: can this be built? What are the top risks?

### Step 3: Evidence
Run discover-hypothesis for {{topic}}.
Frame the core claim and its falsification conditions.
Run discover-websearch to gather 3+ external sources.

### Step 4: Synthesis
Synthesize findings into a decision brief:

**Decision Brief: {{topic}}**

| Dimension | Signal | Confidence |
|-----------|--------|-----------|
| Inertia threat | [HIGH/MED/LOW] — [why] | HIGH/MED/LOW |
| Feasibility | [assessment] | HIGH/MED/LOW |
| Top risk | [risk name] — [mitigation] | HIGH/MED/LOW |
| Hypothesis | [core claim] | HIGH/MED/LOW |
| Evidence | [key finding] | HIGH/MED/LOW |

**Recommendation**: COMMIT | PAUSE | PIVOT | ABANDON

**Rationale**: [2-3 sentences connecting the signals to the recommendation]

**Inertia verdict**: [explicitly state why inertia loses, or why it wins]

---

Write campaign artifact to: signals/rhythm/decide/{{topic}}-decide-{{date}}.md
Include frontmatter: skill: rhythm-decide, topic: {{topic}}, date: {{date}},
  campaign: [discover-inertia, discover-competitors, discover-feasibility,
             discover-risk, discover-hypothesis, discover-websearch]
