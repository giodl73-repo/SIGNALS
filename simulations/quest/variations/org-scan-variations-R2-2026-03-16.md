# org-scan — Prompt Variations R2 (V-01 through V-05)

---

## V-01 — Role Sequence (breadth-first phases, C-09 hardened, C-10 explicit labels)

**Hypothesis**: R1's V-01 scored 95 with breadth-first scan phases, embedded anti-fabrication, and double-stated C-05. The two PARTIALs were C-09 (floor risk when sources absent) and C-10 (current/recommended not labeled). Adding an explicit 5-path floor requirement and CURRENT STATE / RECOMMENDED STATE section headers closes both gaps.

**Key changes from R1 V-01:**
- C-09: replaced "at least one path per source" with "cite the 5 most specific file paths found across all sources"
- C-10: Phases 2-4 now labeled `CURRENT STATE — *` and Phases 5-6 labeled `RECOMMENDED STATE — *`
- C-13: C-05 restated verbatim in output format section

---

## V-02 — Output Format (dual-table architecture: Group A Current State / Group B Recommended State)

**Hypothesis**: R1's V-02 scored 80 (truncated) and had no current/recommended separation. Completing all 7 steps and splitting tables into two explicitly labeled groups makes C-10 structural: the separation is in the schema, not just the instructions. Table A-1 requires all 7 paths before any analysis table is filled (C-12 gate). Anti-fabrication embedded per table header (C-11).

**Key changes from R1 V-02:**
- All steps present including boundaries, shape, gaps
- Group A (Current State Tables) + Group B (Recommended State Tables) as top-level structure
- A-1 must be complete before A-2 (hard gate)
- 5-path floor on A-1
- Anti-fabrication: "do not add row without evidence path" per table

---

## V-03 — Phrasing Register (anti-fabrication directives embedded per section, C-11 primary axis)

**Hypothesis**: R1 embedded anti-fabrication once in Phase 2. C-11 requires it per evidence-dependent section. Moving the constraint from a single preamble warning to a per-section note fires the check at the decision point — when the model is actively making a claim — rather than having it forgotten after setup. Also adds explicit Step 7 (Current state vs recommended state) for C-10.

**Structure**: 8 steps, each evidence-dependent section opens with an `*Anti-fabrication constraint:*` note.

---

## V-04 — Lifecycle Emphasis + Hard Phase Gate (C-12 as explicit STOP checkpoint)

**Hypothesis**: R1's V-01 had "complete all before drawing conclusions" as a behavioral instruction in a phase header. C-12 requires a hard sequencing gate. Replacing the soft instruction with a literal checklist the model must verify and confirm before proceeding — "Stage 1 Gate: verify [ ] [ ] [ ], write confirmation sentence" — turns scan-completion from advice into a structural gate.

**Structure**: Two top-level stages (SCAN / SYNTHESIS) separated by a mandatory gate checkpoint with a 5-item verification checklist and required confirmation sentence.

---

## V-05 — Full Integration (all 5 aspirational criteria explicitly structured)

**Hypothesis**: V-01 R1 had C-11/C-12/C-13 organically embedded and scored 95. C-09 and C-10 were partial. Making all five aspirational patterns structurally explicit — each positioned at the exact point of use — closes the remaining gap to 100. The test is whether explicit naming degrades readability or maintains it while driving full aspirational coverage.

**What each aspirational criterion gets:**
- **C-09**: "cite the 5 most specific file paths found" — explicit floor, not a floor-per-source
- **C-10**: Phase 2 labeled CURRENT STATE ANALYSIS, Phase 3 labeled RECOMMENDED STATE — separate labeled phases
- **C-11**: `*Anti-fabrication:*` note at the start of each evidence-dependent section (2a, 2b, 2c, 3a, 3b)
- **C-12**: Phase 1 Gate sentence between phases — must write confirmation before Phase 2
- **C-13**: C-05 stated word-for-word in preamble AND in output format section

---

## Variation Summary

| ID | Axis(es) | Primary Gap Targeted | C-09 | C-10 | C-11 | C-12 | C-13 |
|----|----------|---------------------|------|------|------|------|------|
| V-01 | Role sequence (evolved R1) | C-09 + C-10 | 5-path floor | CURRENT/RECOMMENDED labels | Preamble | Phase header | Preamble + output format |
| V-02 | Output format (dual-table) | C-10 structural | 5-path floor in A-1 | Group A / Group B split | Per-table note | A-1 fill gate | Preamble + constraints |
| V-03 | Phrasing register (per-section anti-fab) | C-11 per-section | All-source pass | Step 7 explicit | Per-section * note | Step 1 instruction | Preamble + output format |
| V-04 | Lifecycle + hard gate | C-12 checkpoint | 5-path checklist | CURRENT/RECOMMENDED sections | N/A | STOP checklist | Preamble + output format |
| V-05 | Full integration | All 5 aspirational | Explicit 5-path floor | Named phase labels | Per-section * note | Phase gate sentence | Verbatim double-statement |

Saved to `simulations/quest/variations/org-scan-variations-R2-2026-03-16.md`.
DED): Recommend an org shape

Name a recommended org shape:
- flat (few layers, direct ownership)
- functional (deep expertise silos, shared platform)
- matrix (dual reporting, cross-functional pods)
- pods (small autonomous teams per product area)
- other (name it)

Justify the recommendation in 1-2 sentences using specific findings from the
CURRENT STATE sections above.

Label this section: **RECOMMENDED STATE — Org Shape**

---

### Phase 7: Flag evidence gaps

List gaps where the scan could not reach confident conclusions:
- Absent source types (mark as ABSENT)
- Ambiguous or conflicting signals
- Artifacts missing that would normally be present

Label this section: **EVIDENCE GAPS**

---

### Output format

Deliver the full output as labeled sections matching the phases above. Use
prose and bullet lists. The CURRENT STATE sections describe what the repo is
today. The RECOMMENDED STATE sections describe what the org design should target.
Keep these visibly separate — the consumer needs to see what is vs what is
recommended.

Do not produce a hierarchy diagram, reporting structure, named roles, or
org chart at any point. This is raw analysis — not a finished org.
```

---

## V-02 — Axis: Output Format (dual-table architecture, current/recommended table groups)

**Hypothesis**: R1's V-02 scored 80 (at the floor) because steps 5+ were absent — it was truncated — and had no current/recommended separation. Completing the table structure with all 7 steps, separating scan tables from recommendation tables by explicit group label, and adding anti-fabrication constraints per table makes C-10 structural: the separation is in the schema, not just the instructions.

```markdown
You are running /org-scan.

Walk the repo and produce a raw structural analysis. Output is two groups of
tables — Current State and Recommended State — plus a gap list. This is NOT
an org chart. No reporting lines. No hierarchy. No role boxes. The output
feeds /org-chart.

---

## GROUP A: CURRENT STATE TABLES

### Table A-1: Scan Log

Fill every row before proceeding to Table A-2. Do not analyze yet.

| Source Type       | Found? | Key Finding                          | Specific File Path                |
|-------------------|--------|--------------------------------------|-----------------------------------|
| CLAUDE.md         |        |                                      |                                   |
| package.json      |        |                                      |                                   |
| design/ dirs      |        |                                      |                                   |
| Namespaces        |        |                                      |                                   |
| Test coverage     |        |                                      |                                   |
| SPECS.md files    |        |                                      |                                   |
| .craft/roles/     |        |                                      |                                   |

If a source type is absent, mark Found? = ABSENT and record what the absence
implies in the Key Finding column. The Specific File Path column must contain
an actual path, not a glob — mark ABSENT if no file found.

**Gate: Table A-1 must be complete before filling any other table.**

Across all A-1 rows, at least 5 distinct file paths must be cited. If the
repo has fewer than 5 reachable paths, cite all available and note the
shortfall in Table A-4.

---

### Table A-2: Areas of Work

One row per distinct area. Evidence Path must come from Table A-1. If you
cannot fill the Evidence Path column from the scan log, do not add the row.

| Area Name | Description (1 sentence) | Source Type | Evidence Path from A-1 |
|-----------|--------------------------|-------------|------------------------|
|           |                          |             |                        |
|           |                          |             |                        |
|           |                          |             |                        |

Minimum 3 rows. Do not invent areas — only include what the scan log supports.

---

### Table A-3: Cross-Cutting Concerns

| Concern Name | Areas It Spans | Why Single-Team Ownership Fails |
|--------------|----------------|---------------------------------|
|              |                |                                 |

At least 1 row. Spans column must reference area names from Table A-2.

---

### Table A-4: Headcount Signals

| Signal Observation               | Source Type     | Implied Domain Count |
|----------------------------------|-----------------|----------------------|
|                                  |                 |                      |
|                                  |                 |                      |

Summary: **Estimated distinct expertise domains: [N-M]**
Derivation (1-2 sentences tying the range to table rows above):

---

## GROUP B: RECOMMENDED STATE TABLES

*These tables describe what the org design should target, not what currently
exists. Cite Table A findings as the basis for each recommendation.*

### Table B-1: Team Boundary Candidates

| Boundary Name | Seam Evidence (from Table A) | Coupling Risk | Risk Note |
|---------------|------------------------------|---------------|-----------|
|               |                              | Low/Med/High  |           |
|               |                              | Low/Med/High  |           |

At least 2 rows. Evidence column must reference a finding from Table A-1 or
A-2 — do not introduce new observations in Group B.

---

### Table B-2: Recommended Org Shape

| Shape | Justification (cite Table A findings) |
|-------|---------------------------------------|
|       |                                       |

Shape options: flat / functional / matrix / pods / other (name it).
One row only. Justification must cite at least one Table A row by reference.

---

## EVIDENCE GAPS

| Gap Description                   | Source Type Affected | Implication for /org-chart |
|-----------------------------------|----------------------|---------------------------|
|                                   |                      |                           |

List source types marked ABSENT in Table A-1, ambiguous findings, and any
areas in Table A-2 where evidence was thin. At least 1 row required.

---

## Constraints

- Table A-1 must be filled before any other table.
- Table A-2 rows require an Evidence Path from Table A-1 — no path, no row.
- Group B rows must cite Group A findings — no new observations in Group B.
- No hierarchy diagram, org chart, reporting lines, or role boxes anywhere.
- This is raw analysis — not a finished org.
```

---

## V-03 — Axis: Phrasing Register (anti-fabrication language embedded per section)

**Hypothesis**: R1's V-01 embedded anti-fabrication language once in Phase 2 ("do not invent areas that have no evidence basis"). C-11 requires it per evidence-dependent section. Moving from a single preamble warning to a per-section constraint fires the anti-fabrication check at the decision point, not at setup — making fabrication harder even when the model has lost context of the opening instructions.

```markdown
You are running /org-scan.

Walk the repo and infer its org structure. Produce raw analysis only — areas
of work, cross-cutting concerns, headcount signals, team boundary candidates,
and a recommended org shape. This is NOT an org chart. Do not produce
reporting lines, named roles, or hierarchy at any point.

---

### Step 1: Scan the evidence sources

Explore the repo using these 7 source types. For each, record what you found
and cite at least one specific file path. If a source type is absent, say so.

- CLAUDE.md files
- package.json / workspace manifests
- design/ directories
- Namespaces or top-level module structure
- Test coverage files or directories
- SPECS.md or specification files
- .craft/roles/ files

Complete the scan of all 7 source types before continuing. Do not draw
conclusions while scanning.

---

### Step 2: Areas of work

*Anti-fabrication constraint: Only name areas you can point to in the scan
log above. Every area must have a cited source. If you found it in a
namespace, name the namespace. If you found it in a spec file, name the file.
Do not name an area you cannot trace to evidence.*

Name the distinct areas of work found in the scan. For each:
- Area name
- What evidence led you to name it this way
- Cite the specific source file or path

Minimum 3 areas.

---

### Step 3: Cross-cutting concerns

*Anti-fabrication constraint: Cross-cutting concerns must be grounded in the
areas you named above. Do not import concerns from general software knowledge
unless you can point to evidence that this repo specifically has them. If a
concern is common but absent from the scan, flag it as absent — do not include
it as a finding.*

Name concerns that span multiple of the areas above and cannot be owned by a
single team without coordination risk. For each:
- Concern name
- Which areas it spans (cite from Step 2)
- Why it cannot be cleanly assigned to one team

At least 1 required.

---

### Step 4: Headcount signals

*Anti-fabrication constraint: Do not state a headcount range without derivation.
Round numbers with no evidence ("probably 3-5 people") do not pass this step.
Derive the range from something you found — namespace count, role file count,
spec coverage breadth, or distinct test ownership areas.*

How many distinct expertise domains does this repo require? Show your work:
- What did the scan find that informs this estimate?
- What is the range?
- What would change the estimate up or down?

---

### Step 5: Team boundary candidates

*Anti-fabrication constraint: Every proposed seam must trace to evidence from
Steps 1-4. Do not propose a team boundary you cannot support with a scan
finding. If the evidence is ambiguous, say so and note the ambiguity.*

Where are the natural seams in this repo? For each candidate boundary:
- Name the boundary
- Cite the evidence for the seam (from the scan log)
- Note any coupling risk

At least 2 candidates required.

---

### Step 6: Recommended org shape

Name a recommended org shape — flat, functional, matrix, pods, or other
(name it) — and justify the recommendation in 1-2 sentences using findings
from this scan, not from general org design principles.

*Anti-fabrication constraint: The justification must cite a specific finding
from this repo. General reasoning about org shapes without reference to scan
findings does not meet this step.*

---

### Step 7: Current state vs recommended state

Write two short paragraphs:

**Current state**: What does the scan show the org structure actually is today?
Cite areas, headcount signals, and cross-cutting concerns from above.

**Recommended state**: What would the org look like if the team boundaries and
shape recommendations above were adopted? Describe the difference from today.

This section makes the gap between now and the recommendation explicit.

---

### Step 8: Evidence gaps

Be honest about what the scan could not answer. List:
- Source types that were absent
- Areas with thin or conflicting evidence
- Assumptions you made that should be verified

These gaps tell whoever runs /org-chart what to investigate first.

---

### Output format

Labeled sections, one per step. Prose and bullets. Cite file paths inline.

Do not produce a hierarchy diagram, reporting structure, or org chart at any
point. This is raw analysis — not a finished org.
```

---

## V-04 — Axes: Lifecycle Emphasis + Hard Phase Gate (explicit scan-completion checkpoint)

**Hypothesis**: R1's V-01 included "complete all before drawing conclusions" in Phase 1's header — a behavioral instruction. C-12 requires a hard sequencing gate. Upgrading the soft instruction to a literal STOP checkpoint — with a checklist the model must verify before proceeding — turns the scan-completion requirement from advice into a gate that the prompt structure itself enforces.

```markdown
You are running /org-scan.

This skill has two stages: SCAN and SYNTHESIS. These stages are separated by
a hard gate — you must confirm Stage 1 is complete before Stage 2 begins.
This constraint exists because synthesis done with an incomplete scan produces
analysis anchored on the first interesting source and misses weaker signals.

This is NOT an org chart. Do not produce reporting lines, role boxes, or
hierarchy diagrams at any point in Stage 1 or Stage 2.

---

## STAGE 1 — SCAN
*Collect evidence. No analysis. No conclusions.*

Read from all 7 source types below. For each, record your finding and cite at
least one specific file path. Mark ABSENT if the source type is not present
in the repo.

**Source 1: CLAUDE.md**
Finding:
Path:

**Source 2: package.json / workspace manifests**
Finding:
Path:

**Source 3: design/ directories**
Finding:
Path:

**Source 4: Namespaces or top-level module structure**
Finding:
Path:

**Source 5: Test coverage files or directories**
Finding:
Path:

**Source 6: SPECS.md or specification files**
Finding:
Path:

**Source 7: .craft/roles/ files**
Finding:
Path:

---

### STAGE 1 GATE — MANDATORY BEFORE CONTINUING

Before beginning Stage 2, verify all of the following:

- [ ] All 7 source types have been visited
- [ ] Every source type that exists has a specific file path cited
- [ ] Every absent source type is marked ABSENT with an implication noted
- [ ] At least 5 distinct file paths are cited across all sources (if the repo
      has fewer than 5 reachable paths, note the count and continue)

Write a one-sentence gate confirmation: "Stage 1 complete. Sources found: N/7.
Paths cited: N. Absent sources: [list]."

Do not begin Stage 2 until this confirmation is written.

---

## STAGE 2 — SYNTHESIS
*Analyze the Stage 1 scan log. No new evidence gathering here.*

### Section A (CURRENT STATE): Areas of Work

From the Stage 1 scan log, identify distinct areas of work. Each area must map
to at least one Stage 1 finding. Do not introduce areas that lack scan evidence.
Minimum 3 required.

For each area: name, description, source citation from Stage 1.

---

### Section B (CURRENT STATE): Cross-Cutting Concerns

Identify concerns that span multiple of the areas named in Section A and cannot
be owned by a single team without coordination risk.

For each: name, which areas it spans, why single-team ownership fails.

At least 1 required. If no cross-cutting concerns are found, state why —
do not leave this section blank.

---

### Section C (CURRENT STATE): Headcount Signals

From the Stage 1 scan log, estimate distinct expertise domains. Show the
derivation: what did the scan find (role files, namespace count, spec breadth)
and how does it translate to a domain range?

State a range (e.g., "3-4 domains") with at least one explicit scan observation
as the derivation.

---

### Section D (RECOMMENDED STATE): Team Boundary Candidates

Where could this repo be divided across teams with manageable seam cost?

For each candidate: boundary name, Stage 1 evidence for the seam, coupling
risk (Low/Med/High) with a note explaining the risk level.

At least 2 candidates. Evidence must come from Stage 1 — do not introduce
new observations in this section.

---

### Section E (RECOMMENDED STATE): Org Shape

Name one: flat / functional / matrix / pods / other (name it).
Justify in 1-2 sentences by citing specific findings from Stage 2 Sections A-C.

The RECOMMENDED STATE sections describe what the org should target. The
CURRENT STATE sections describe what exists. Keep these visibly distinct.

---

### Section F: Evidence Gaps

List what the scan could not answer:
- Absent source types from Stage 1
- Ambiguous or conflicting scan findings
- Areas in Section A with thin evidence backing

One bullet per gap. Each gap should note its implication for whoever runs
/org-chart next.

---

### Output format

Deliver Stage 1 (SCAN) and Stage 2 (SYNTHESIS) as two visibly separate
sections, with the Stage 1 Gate written between them. Within Stage 2, use
the Section A-F labels. Current State sections (A-C) must precede Recommended
State sections (D-E).

Do not produce a hierarchy diagram, reporting structure, or org chart. This
is raw analysis — not a finished org.
```

---

## V-05 — Axes: Full Integration (C-09 + C-10 + C-11 + C-12 + C-13, all explicitly structured)

**Hypothesis**: V-01 R1 had C-11/C-12/C-13 organically but C-09 and C-10 only partially. Making all five aspirational patterns structurally explicit — each named and positioned at the exact point of use rather than implied — closes the remaining gap. The test is whether explicit naming of aspirational constraints degrades readability or maintains it while driving score to 100.

```markdown
You are running /org-scan.

Walk the repo and produce a raw structural analysis of its org structure.
Output: areas of work, headcount signals, cross-cutting concerns, team
boundary candidates, and a recommended org shape.

**Critical constraint** (stated here and repeated in the output format below):
This is NOT an org chart. Do not produce reporting lines, role boxes, or
hierarchy diagrams at any point. The output feeds /org-chart, which will
build the structure from your analysis.

---

### PHASE 1: Scan (breadth-first — complete all 7 sources before Phase 2)

Read each source type. Record your finding and cite at least one specific
file path. Mark ABSENT if the source type does not exist in the repo.

1. CLAUDE.md files
2. package.json / workspace manifests
3. design/ directories
4. Namespaces or top-level module structure
5. Test coverage files or directories
6. SPECS.md or specification files
7. .craft/roles/ files

Path requirement: cite the 5 most specific file paths found across all sources.
If fewer than 5 paths are available (e.g., due to absent source types), cite
all available paths and note the count shortfall as an evidence gap.

**PHASE 1 GATE**: Before writing a single word of Phase 2, confirm:
"Phase 1 complete — N/7 source types found, N file paths cited." Do not
proceed until this confirmation is written.

---

### PHASE 2: Current State Analysis

*Anti-fabrication: Every claim in this phase must trace to a specific Phase 1
finding. Do not name areas, concerns, or patterns that lack Phase 1 evidence.
If you cannot point to a file or source, omit the item and note it as a gap.*

#### 2a. Areas of Work

From the Phase 1 scan log, identify distinct areas of work. Each area must
map to at least one Phase 1 finding. Minimum 3 areas.

For each area: name, 1-sentence description, Phase 1 source citation.

#### 2b. Cross-Cutting Concerns

*Anti-fabrication: Cross-cutting concerns must be grounded in the areas above.
Do not import concerns from general software knowledge unless Phase 1 shows
this repo specifically has them.*

Name concerns spanning multiple areas that cannot be owned by one team without
coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

#### 2c. Headcount Signals

*Anti-fabrication: Do not state a headcount range without derivation. A range
requires an explicit evidence chain — namespace count, role file count, spec
coverage breadth, or distinct test ownership. Round numbers with no evidence
chain do not pass this step.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

### PHASE 3: Recommended State

*Anti-fabrication: Recommendations must cite Phase 2 findings as their basis.
Do not introduce new observations in this phase — only interpret what Phase 2
produced.*

#### 3a. Team Boundary Candidates

Propose 2+ candidate seams. For each: boundary name, Phase 2 evidence for
the seam, coupling risk (Low/Med/High) with a note.

#### 3b. Recommended Org Shape

Name one: flat / functional / matrix / pods / other (name it). Justify in
1-2 sentences by citing Phase 2 findings.

---

### PHASE 4: Evidence Gaps

List what the scan could not answer:
- Phase 1 source types marked ABSENT
- Phase 2 areas with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output as four labeled phases: PHASE 1 (SCAN) / PHASE 2
(CURRENT STATE ANALYSIS) / PHASE 3 (RECOMMENDED STATE) / PHASE 4 (EVIDENCE
GAPS). The Phase 1 gate confirmation appears between Phase 1 and Phase 2.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it. The consumer of this output is /org-chart, not an
org designer reading a finished document.
```

---

## Variation Summary

| ID   | Axis(es)                                      | Key Hypothesis                                                                                 | Rubric Criteria Targeted              | Expected Gap vs R1 V-01 |
|------|-----------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------------|-------------------------|
| V-01 | Role sequence (evolved from R1 V-01)          | Preserving 95-point structure + C-09 hardened + explicit CURRENT/RECOMMENDED labels closes to 100 | C-01..C-13 (all)                      | C-09, C-10 closed       |
| V-02 | Output format (dual-table architecture)       | Structural current/recommended separation at schema level makes C-10 behavioral-proof           | C-01..C-09, C-10, C-11..C-13          | C-10 structural fix     |
| V-03 | Phrasing register (per-section anti-fab)      | Anti-fabrication at decision point beats a preamble warning for C-11 reliability               | C-01, C-04, C-08, C-10, C-11 emphasis | C-11 per-section        |
| V-04 | Lifecycle emphasis + hard phase gate          | STOP checkpoint checklist for Stage 1 completion is a structural C-12 guarantee                | C-12 emphasis + C-10                  | C-12 structural         |
| V-05 | Full integration (all 5 aspirational)         | Explicit per-phase anti-fabrication + hard gate + double-stated C-05 + 5-path floor = 100      | C-01..C-13 (all, explicitly named)    | All aspirational closed |
