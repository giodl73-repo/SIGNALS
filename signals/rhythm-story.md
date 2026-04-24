You are running /rhythm-story for: {{topic}}

Synthesize all signals gathered for this topic into a coherent narrative. This is NOT a
summary of each signal. It is an editorial synthesis -- the story of what the investigation
found, written in the author's voice, organized by insight rather than by skill.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{{topic}}-*
Read every artifact. For each one, extract: (1) the key finding, (2) what changed about
your understanding after reading it, (3) any surprises.

---

## PHASE 2 -- THREE-SECTION NARRATIVE

Write in continuous prose. No bullet lists. Minimum 300 words per section.

### Section 1: The Investigation Story

Tell the story of what was learned, in the order the understanding evolved. Start with
what the team believed at the start. Name the signal that changed that belief most. End
with where the investigation stands now.

The inertia finding belongs here: what does the investigation say about why teams would
do nothing instead?

### Section 2: The Decision Case

What do the signals say together -- not individually? What pattern emerged across
namespaces? If the signals agree, say so and say why that agreement is meaningful.
If they conflict, name the conflict and take a position.

State the commit/pause/pivot case as clearly as possible. What would have to be false
for the opposite conclusion to be right?

### Section 3: The Open Questions

What does this investigation not yet know? Name 2-4 specific questions that remain
genuinely open -- not observations about missing coverage, but real uncertainties about
the feature's value, feasibility, or adoption. Each question should be falsifiable:
what evidence would close it?

---

## PHASE 3 -- AMEND

Three editorial improvements:
1. [What's missing from Section 1 that would make the story more honest]
2. [What the decision case in Section 2 is asserting without sufficient evidence]
3. [Which open question in Section 3 is most urgent to answer before commitment]

Write artifact to: signals/rhythm/story/{{topic}}-story-{{date}}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
Include frontmatter: skill: rhythm-story, topic: {{topic}}, date: {{date}}