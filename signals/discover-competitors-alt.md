You are running /discover-competitors-alt for: {{topic}}

Unified competitive analysis with optional focus dimension woven into the analysis. Assesses inertia (status quo) first. Then named competitors with a focus dimension active throughout, not appended at the end.

--focus options: market-sizing | positioning | moat | distribution | pricing
Default: no focus (equivalent to discover-competitors with richer synthesis).

---

## PHASE 1 -- INERTIA (primary competitor, always first)

Why would teams do nothing? What is the specific status-quo workaround?

Status quo assessment:
- Current workaround: [specific tool/process teams use today]
- Workaround cost: [time, risk, or friction -- quantified where possible]
- Switching trigger: [what would cause teams to abandon the workaround]
- Inertia threat: HIGH (always)

If --focus active, weave focus dimension into inertia assessment:
  market-sizing: how large is the "do nothing" segment?
  positioning: how is the status quo positioned in users' minds?
  moat: what lock-in makes the status quo sticky?
  pricing: what is the implicit cost of the status quo?

---

## PHASE 2 -- NAMED COMPETITORS (5-8 entries)

For each named competitor, assess with focus dimension active throughout:

| Competitor | Positioning | Technical Moat | Distribution | Threat | [Focus if active] |
|------------|-------------|----------------|--------------|--------|-------------------|

Use WebSearch to verify at least one claim per major competitor. Cite source inline.

---

## PHASE 3 -- SYNTHESIS

Three cross-competitor insights only visible across the full field:
1. [Pattern across competitors]
2. [Whitespace no competitor owns]
3. [Table stakes any entrant must have]

---

## PHASE 4 -- AMEND

Three adjustments:
1. [Shift focus dimension or add one if none was active]
2. [Sharpen the inertia threat -- make it more specific]
3. [Add or remove a competitor based on new information]

Write artifact to: signals/discover/competitors-alt/{{topic}}-competitors-alt-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-competitors-alt-{date}.md). No namespace subdirectory.
Include frontmatter: skill: discover-competitors-alt, topic: {{topic}}, date: {{date}}, focus: [dimension or none]
