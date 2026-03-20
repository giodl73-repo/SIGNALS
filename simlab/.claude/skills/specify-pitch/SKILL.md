---
name: specify-pitch
description: Author a pitch deck narrative in exec, developer, and maker versions. Pulls from scout-positioning if available. Each ve
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /specify-pitch for: {{topic}}

Author a pitch narrative in three versions. Pull from any scout-positioning, discover-competitors, or specify-spec artifacts for this topic if available.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{{topic}}-*
Read any positioning, competitive, feasibility, or spec artifacts found.
Note the inertia case: why would teams do nothing? This MUST appear in the exec version.

---

## PHASE 2 -- THREE PITCH VERSIONS

### Version A: EXEC (decision-maker, ROI and risk framing, 1 page max)

**The problem**: What the status quo costs. Name the specific inertia mechanism -- why teams currently do nothing.
**The solution**: What this feature does in one sentence.
**Why now**: The specific trigger that makes this the right time to build.
**The return**: Quantified benefit where possible (time saved, risk reduced, adoption gained).
**The ask**: Decision required, resources needed, timeline.
**Risk of inaction**: What happens if the team does nothing in the next 90 days.

### Version B: DEVELOPER (technical audience, build conviction)

**What we're building**: Architecture in plain terms. Key technical decisions already made.
**Why this approach**: What alternatives were considered and why rejected.
**What's hard**: The honest technical challenge and how it's addressed.
**Dependencies**: What this relies on, what it unblocks for others.
**Definition of done**: Specific, verifiable completion criteria -- not "feature complete."

### Version C: MAKER (builder narrative, creative framing)

**The user moment**: The specific experience this creates that doesn't exist today.
**What we're proving**: The hypothesis this feature tests in the world.
**The creative constraint**: The hardest design decision -- what must be true for this to work.
**How we'll know**: What success looks like for a real user in the first 30 days.

---

## PHASE 3 -- AMEND

Three targeted adjustments:
1. [Sharpen the inertia case in the exec version -- be more specific about cost of inaction]
2. [Strengthen the technical definition of done in the developer version]
3. [Make the user moment more concrete in the maker version]

Write artifact to: signals/specify/pitch/{{topic}}-pitch-{{date}}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
Include frontmatter: skill: specify-pitch, topic: {{topic}}, date: {{date}}