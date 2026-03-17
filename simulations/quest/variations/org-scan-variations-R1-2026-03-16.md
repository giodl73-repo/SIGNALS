Now I have everything I need. Generating the 5 variations.

---

# org-scan — Prompt Variations R1 (V-01 through V-05)

---

## V-01 — Axis: Role Sequence (breadth-first scan loop before synthesis)

**Hypothesis**: Completing a full breadth-first pass over all 7 source types before drawing any conclusions prevents premature anchoring on the first interesting source and produces more complete multi-source coverage (C-02) and better-grounded areas (C-01).

```markdown
You are running /org-scan.

Walk the repo and produce a raw structural analysis — areas of work, headcount
signals, cross-cutting concerns, team boundary candidates, and a recommended org
shape. This is NOT an org chart. Do not produce reporting lines, role boxes, or
hierarchy. The output feeds /org-chart, which will build the structure from your
analysis.

---

### Phase 1: Scan all 7 sources (breadth-first — complete all before drawing conclusions)

Read each source type in order. Record what you find. Do not synthesize yet.

1. **CLAUDE.md** — What domains, skill namespaces, or areas of work are described?
   Note any explicit role or team references.

2. **package.json / workspace manifests** — What packages exist? What are their
   names and purposes? Multiple packages signal team or ownership seams.

3. **design/ directories** — What design artifacts exist? What areas do they cover?
   Sparse design dirs signal ownership gaps.

4. **Namespaces** — What top-level namespaces, modules, or skill groups exist?
   Each namespace that is functionally independent is a candidate team boundary.

5. **Test coverage areas** — What is tested? What is not tested? Test gaps often
   reveal ownership ambiguity or under-resourced areas.

6. **SPECS.md / spec files** — What features or subsystems have written specs?
   Specs signal where deliberate design investment has occurred.

7. **.craft/roles/** — What roles exist? What expertise do they represent?
   Role files are direct headcount signals.

Record findings per source. Cite at least one file path or path pattern per source
as evidence. If a source type is absent from the repo, note it explicitly — this
is an evidence gap.

---

### Phase 2: Synthesize areas of work

From the scan log above, identify distinct areas of work. Each area must be
traceable to at least one source artifact from Phase 1. Do not invent areas that
have no evidence basis.

For each area:
- Name it
- Cite the scan source(s) that evidence it
- Note any overlap with other areas (overlap is a cross-cutting signal)

Minimum 3 areas required.

---

### Phase 3: Surface cross-cutting concerns

Identify concerns that span multiple areas and cannot be owned by a single team
without coordination risk. For each cross-cutting concern:
- Name it
- State which areas it touches
- Explain why it cannot be cleanly assigned to one team

---

### Phase 4: Estimate headcount signals

Based on the scan, how many distinct expertise domains exist? Derive this from:
- Number of namespaces or packages
- Number of role files found
- Number of spec or design areas with no overlap

State a range (e.g., "3-4 domains") with at least one observation from the scan
as supporting rationale.

---

### Phase 5: Propose team boundary candidates

Where are the natural seams in this repo? For each candidate boundary:
- Name the boundary (e.g., "between namespace X and namespace Y")
- State the evidence for the seam (shared dependencies? separate design dirs?
  independent test suites?)
- Note any coupling that makes the seam risky

---

### Phase 6: Recommend an org shape

Based on the scan, name a recommended org shape:
- flat (few layers, direct ownership)
- functional (deep expertise silos, shared platform)
- matrix (dual reporting, cross-functional pods)
- pods (small autonomous teams per product area)
- other (name it)

Justify your recommendation in 1-2 sentences using specific scan findings.

---

### Phase 7: Flag evidence gaps

List areas where the scan could not reach a confident conclusion:
- Missing source types (e.g., no test files found)
- Ambiguous signals (e.g., overlapping namespaces with unclear ownership)
- Absent artifacts that would normally be present (e.g., no SPECS.md despite
  complex behavior)

These gaps tell the consumer what to investigate before running /org-chart.

---

### Output format

Deliver the analysis as labeled sections matching the phases above. Use prose and
bullet lists. Do not produce a hierarchy diagram, reporting structure, or named
roles. This is raw analysis — structured enough to hand off, not a finished org.
```

---

## V-02 — Axis: Output Format (table-driven, evidence-linked rows)

**Hypothesis**: Forcing tabular output for every structural claim makes evidence linkage mandatory per row, directly driving C-09 (5+ file paths cited) and reducing the risk of invented areas (C-01) because a row with no evidence column cannot be completed.

```markdown
You are running /org-scan.

Walk the repo and produce a raw structural analysis. Output is tables and
supporting notes — not an org chart. No reporting lines. No role hierarchy.
The output feeds /org-chart.

---

### Step 1: Run the scan

Read from these 7 source types. For each source found, record it in the scan log
table below. If a source type is absent, mark it ABSENT.

| Source Type       | Found? | Key Finding                         | File Path Evidence         |
|-------------------|--------|-------------------------------------|----------------------------|
| CLAUDE.md         |        |                                     |                            |
| package.json      |        |                                     |                            |
| design/ dirs      |        |                                     |                            |
| Namespaces        |        |                                     |                            |
| Test coverage     |        |                                     |                            |
| SPECS.md files    |        |                                     |                            |
| .craft/roles/     |        |                                     |                            |

Fill every row before proceeding.

---

### Step 2: Areas of work

For each distinct area of work found, complete a row. Evidence column must contain
a file path or path pattern from the scan — leave no evidence column blank.

| Area Name | Description (1 sentence) | Evidence Source Type | Evidence Path       |
|-----------|--------------------------|----------------------|---------------------|
|           |                          |                      |                     |
|           |                          |                      |                     |
|           |                          |                      |                     |

Minimum 3 rows. If you cannot fill the evidence column, do not add the row.

---

### Step 3: Cross-cutting concerns

| Concern Name | Areas It Spans | Why It Cannot Be Owned By One Team |
|--------------|---------------|--------------------------------------|
|              |               |                                      |

At least 1 row required.

---

### Step 4: Headcount signals

| Signal Observation                          | Source                    | Implied Domain Count |
|---------------------------------------------|---------------------------|----------------------|
|                                             |                           |                      |
|                                             |                           |                      |

Summary: **Estimated distinct expertise domains: [N-M]**
Rationale (1-2 sentences tying estimate to table rows above):

---

### Step 5: Team boundary candidates

| Boundary Name         | Seam Evidence (path or pattern) | Coupling Risk (Low/Med/High) | Risk Note          |
|-----------------------|---------------------------------|------------------------------|--------------------|
|                       |                                 |                              |                    |
|                       |                                 |                              |                    |

At least 2 rows required.

---

### Step 6: Recommended org shape

Shape: _______________

Justification (cite at least one row from the tables above):

---

### Step 7: Evidence gaps

| Gap Description                    | Source Type Affected | Impact on /org-chart |
|------------------------------------|----------------------|----------------------|
|                                    |                      |                      |

---

### Constraints

- Do not produce a hierarchy diagram, org chart, or reporting structure.
- Do not add areas without evidence paths.
- Tables must be complete — no empty evidence cells in Steps 2-3.
```

---

## V-03 — Axis: Phrasing Register (descriptive/exploratory, think-aloud)

**Hypothesis**: A descriptive, think-aloud register encourages exploratory reasoning over checklist execution, surfacing richer cross-cutting concerns (C-04) and more nuanced evidence gaps (C-08) because the model reasons through ambiguity rather than pattern-matching to a template.

```markdown
You are running /org-scan.

Your job is to walk this repo as if you are an experienced engineering lead
arriving on day one and trying to understand how the work is organized — not to
produce an org chart, but to produce the analysis that would let someone else
build one. Think aloud. Document what you find. Call out what surprises you.

---

Start by exploring the repo. Look at these sources, in whatever order makes sense
given what you find:

- CLAUDE.md files (they often describe the intended purpose of each area)
- package.json or workspace manifests (structural seams show up here)
- design/ directories (deliberate design investment signals ownership)
- namespace or module structure (what are the top-level buckets?)
- test files or test coverage directories (what gets tested, and by whom?)
- SPECS.md or specification files (where has someone written down intent?)
- .craft/roles/ files (explicit role definitions are strong headcount signals)

As you explore, keep a running log of what each source tells you. Cite file paths
as you go — you want this analysis to be auditable, not impressionistic.

---

Once you have explored the sources, work through these questions and write up
your findings for each:

**What areas of work exist here?**
Name the distinct areas you see. For each, explain what evidence in the repo led
you to name it that way. If you found it in a namespace, say which one. If you
found it in a spec file, say which file. Don't name areas you can't point to.

**Where are the seams?**
What parts of the repo feel like they could be maintained by separate teams without
constant coordination? What makes you think that? What parts feel tightly coupled
in ways that would make separation painful? Say why.

**What crosses the seams?**
What concerns, dependencies, or processes would need to span any team boundary you
identified? These cross-cutting concerns are the hardest thing to design for, and
they're the thing most likely to get missed in an org design. Name at least one.
Explain why it can't be cleanly owned.

**How many distinct expertise domains does this repo represent?**
Don't just count namespaces — think about what skills someone would need to work
effectively in each area. Then estimate: how many people with genuinely different
backgrounds does this work require? Give a range and explain your reasoning.

**What shape of org fits this?**
Given everything you've found, what kind of org structure would work here — flat,
functional, pods, matrix, or something else? Why does that shape fit what you
found rather than a different shape?

**What couldn't you tell?**
Be honest about where the evidence was thin. Were any source types absent? Did any
namespaces have no matching specs? Were there test coverage gaps? These gaps are
not failures — they're the most useful output of the scan, because they tell
whoever runs /org-chart where to dig deeper.

---

Format your output as labeled sections (one per question above), using prose.
Use bullet lists where multiple items need enumeration. Cite file paths inline
where they support a claim.

Do not produce an org chart, reporting hierarchy, or named role assignments.
This is raw analysis — the input to /org-chart, not a substitute for it.
```

---

## V-04 — Axes: Lifecycle Emphasis + Output Format (explicit phase gates, labeled boundaries)

**Hypothesis**: Explicit phase gates with per-phase output requirements prevent C-05 failures (org chart appearing) by constraining what is allowed in each phase, and drive C-10 (current/recommended separation) by requiring separate labeled sections for "what we found" vs "what we'd recommend."

```markdown
You are running /org-scan.

This skill has four phases. Complete each phase fully before moving to the next.
Phase gates exist to keep scan findings separate from recommendations — this is
critical because org-scan produces input to /org-chart, not the chart itself.

---

## PHASE 1 — SCAN
*Goal: collect raw evidence. No analysis yet.*

Read the following source types. For each, note what you found and cite at least
one file path or path pattern. If a source type is absent, mark it ABSENT and
note what that absence implies.

Sources to scan (all 7 required):
1. CLAUDE.md files
2. package.json / workspace manifests
3. design/ directories
4. Namespaces or top-level module structure
5. Test coverage files or directories
6. SPECS.md or specification files
7. .craft/roles/ files

**Phase 1 output**: A scan log — one bullet per source type, each with a finding
and a path citation. Nothing else. Do not interpret yet.

---

## PHASE 2 — ANALYZE
*Goal: identify structure from scan evidence. Current state only.*

From the Phase 1 log:

**Areas of work (current state)**
Name each distinct area you can identify from the scan. Each area name must map
back to at least one Phase 1 finding. Do not invent areas without evidence.
Minimum 3 required.

**Cross-cutting concerns (current state)**
Name concerns that span multiple areas. For each, state which areas it touches
and why it cannot be owned by one team without coordination overhead.

**Headcount signals (current state)**
Estimate the number of distinct expertise domains the repo requires. Derive the
estimate from scan evidence (role file count, namespace count, spec coverage
breadth). State your evidence chain explicitly.

**Phase 2 output**: Three subsections (areas / cross-cutting / headcount).
No recommendations yet. Describe what IS, not what SHOULD BE.

---

## PHASE 3 — SURFACE
*Goal: propose team candidates and org shape. Recommended state only.*

Do not repeat Phase 2 findings here. This phase is forward-looking.

**Team boundary candidates (recommended)**
Where could this repo be divided across teams with manageable seam cost? Propose
at least 2 candidate boundaries. For each, state the evidence for the seam and
note any coupling that raises the cost of separation.

**Recommended org shape**
Name one of: flat, functional, matrix, pods, or other (name it). Justify the
recommendation in 1-2 sentences by citing specific Phase 2 findings.

**Phase 3 output**: Two subsections (boundaries / shape). Do not produce a
reporting hierarchy, org chart boxes, or named role assignments. Shape label
plus rationale only.

---

## PHASE 4 — GAPS
*Goal: flag what the scan could not answer.*

List evidence gaps: source types that were ABSENT, areas with thin evidence,
signals that pointed in conflicting directions. For each gap, note what it means
for the consumer of this analysis before they run /org-chart.

**Phase 4 output**: A gap list. One bullet per gap, each with an implication note.

---

## Delivery

Produce the full output as four labeled sections: SCAN / ANALYZE / SURFACE / GAPS.
The ANALYZE section describes current state. The SURFACE section describes
recommended state. These sections must be visibly separate so the reader can
distinguish what the repo is today from what the org design would target.

Constraints:
- No org chart, no reporting lines, no hierarchy diagrams at any point
- ANALYZE section must not contain recommendations
- SURFACE section must cite Phase 2 findings, not introduce new observations
- Every area named in ANALYZE must trace to a Phase 1 path citation
```

---

## V-05 — Axes: Inertia Framing + Role Sequence (challenge the default assumption first)

**Hypothesis**: Starting by stating the naive/default org assumption ("what would a newcomer assume this org looks like?"), then running the scan to validate or invalidate each assumption, produces better C-10 separation (current vs recommended) by making the gap visible, and stronger C-08 evidence gaps by revealing where assumptions lack scan backing.

```markdown
You are running /org-scan.

Before you read a single file, consider the default assumption: every repo has
an implied org structure that a newcomer would guess from the top-level directory
or README alone. That default assumption is your baseline. Your job is to scan
the repo and report what the evidence actually says — confirming, correcting, or
complicating the baseline.

This is raw analysis for /org-chart. No org chart. No reporting lines. No
hierarchy. Just what the repo tells you about how the work is and should be
organized.

---

### Step 1: State the default assumption

Before reading any files, write 2-3 sentences stating what a newcomer would
assume this repo's org structure looks like based on its name, top-level
directory layout, or any immediately visible signals (README title, workspace
name, top-level folders). This is the inertia baseline — the org shape the repo
will drift toward if no one intervenes.

Label this section: **DEFAULT ASSUMPTION (pre-scan)**

---

### Step 2: Scan the evidence sources

Now read the repo. Check all 7 source types:
- CLAUDE.md files — described purposes, role references, namespace maps
- package.json / workspace manifests — package names, workspace structure
- design/ directories — design artifacts, coverage, ownership signals
- Namespaces or top-level module structure — functional groupings
- Test coverage files or directories — what is tested, gaps in coverage
- SPECS.md or specification files — where deliberate design intent was written
- .craft/roles/ — explicit role definitions and expertise declarations

For each source type found, cite at least one file path. If a source type is
absent, mark it ABSENT.

Label this section: **SCAN LOG (evidence per source)**

---

### Step 3: Compare evidence to default assumption

For each element of your default assumption, state whether the scan evidence
confirms, complicates, or contradicts it. Be specific — cite scan findings.

| Assumption Element | Evidence Status | Supporting or Contradicting Finding |
|--------------------|----------------|-------------------------------------|
|                    |                |                                     |

Label this section: **ASSUMPTION CHECK**

---

### Step 4: Areas of work (current state, evidence-grounded)

From the scan, name the actual areas of work. Each must be traceable to scan
evidence — not to your default assumption. If an area from your default assumption
lacks scan evidence, do not include it here; flag it as a gap instead.

For each area: name, 1-sentence description, scan source citation.

Label this section: **AREAS OF WORK (current state)**

---

### Step 5: Cross-cutting concerns

Name concerns that span multiple areas and cannot be owned by a single team
without coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

Label this section: **CROSS-CUTTING CONCERNS**

---

### Step 6: Headcount signals

Estimate distinct expertise domains from the scan evidence. State a range and
show your derivation (e.g., "4 namespaces + 3 role files with distinct expertise
profiles = 3-5 domains"). Do not state a number without derivation.

Label this section: **HEADCOUNT SIGNALS**

---

### Step 7: Team boundary candidates and recommended org shape (recommended state)

Propose 2+ candidate team seams, each with evidence. Then name the recommended
org shape and justify it in 1-2 sentences from your findings.

This section is explicitly forward-looking. Separate it from the current-state
sections above so the reader can see the gap between what exists and what is
recommended.

Label this section: **RECOMMENDED STATE (boundaries + shape)**

---

### Step 8: Evidence gaps and assumption failures

List:
1. Source types that were ABSENT from the scan
2. Default assumptions that had no scan evidence to confirm or contradict them
3. Areas where the evidence was thin or conflicting

These gaps tell the consumer what to resolve before running /org-chart.

Label this section: **GAPS AND OPEN QUESTIONS**

---

### Constraints

- DEFAULT ASSUMPTION must be written before reading any files
- AREAS OF WORK must cite scan evidence, not assumption
- RECOMMENDED STATE must be visibly separate from current-state sections
- No org chart, no reporting hierarchy, no role boxes at any point
- Inertia baseline is a comparison tool, not a recommendation — the scan decides
```

---

## Variation Summary

| ID   | Axis(es)                              | Key Hypothesis                                                                 | Rubric Criteria Most Affected     |
|------|---------------------------------------|--------------------------------------------------------------------------------|-----------------------------------|
| V-01 | Role sequence (breadth-first scan)    | Full scan loop before synthesis prevents source anchoring                      | C-01, C-02, C-08                  |
| V-02 | Output format (table-driven)          | Evidence column per row makes source linkage mandatory, not optional           | C-01, C-09, C-10                  |
| V-03 | Phrasing register (think-aloud prose) | Exploratory register surfaces richer cross-cutting and gap reasoning           | C-04, C-08                        |
| V-04 | Lifecycle emphasis + output format    | Explicit phase gates prevent C-05 failures and enforce current/recommended sep | C-05, C-10, C-01                  |
| V-05 | Inertia framing + role sequence       | Pre-scan baseline makes current vs recommended gap explicit and measurable     | C-08, C-10, C-01                  |
