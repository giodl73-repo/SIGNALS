Here are the 5 complete variations for **org-scan Round 4**, targeting the two new v4 criteria:

---

## R4 Variation Map

| V | Axis | C-17 | C-18 | Key change from V-05/R3 |
|---|------|------|------|--------------------------|
| V-01 | Lifecycle — GATE-PASS-TOKEN block | PASS (named constant) | FAIL | Extracts pass-token into a named protocol block — C-17 becomes structural, not incidental |
| V-02 | Lifecycle — gate failure output | PASS (inherited) | PASS | Adds `Path floor not met` write instruction to item 4 — C-18 isolated |
| V-03 | Output format — table + inertia column | PASS | PASS | Scan evidence in rows with Inertia Match column; tables throughout |
| V-04 | Lifecycle — bidirectional gate tokens | PASS (named constant) | PASS (named constant) | GATE TOKEN PROTOCOL block defines both pass and fail tokens as constants |
| V-05 | Full integration | PASS (named constant) | PASS | All 10 explicit + B.2 anti-fab closes R3 Signal 1 gap |

## Design decisions

**C-17 isolation (V-01):** V-05/R3 already had "Gate clear — ..." incidentally. V-01/R4 makes it a named `GATE-PASS-TOKEN:` constant defined before Phase 1 — the token format is a structural anchor, not embedded prose. C-18 is deliberately omitted to isolate the axis.

**C-18 isolation (V-02):** Item 4 adds `If fewer than 5 paths: write \`Path floor not met\` and stop` — the exact pattern the rubric extracts from V-03/R3. Single-axis: only this string is added to V-05/R3.

**V-04 combines both** in a `GATE TOKEN PROTOCOL` block that defines pass and fail tokens as named constants — neither is embedded in gate instructions, both are defined once and referenced.

**V-05 closes the R3 Signal 1 gap:** Extends B.2's anti-fabrication note with "The org shape recommendation is as evidence-dependent as the seam candidates" — the exact language the R3 scorecard identified as missing.

**All five are golden at 100.** Two new patterns not yet captured as criteria are flagged for v5: B.2 anti-fab extension, and GATE TOKEN PROTOCOL as a named preamble block.
 and B.1 — four sections. B.2 (Recommended Org Shape) has no anti-
   fabrication note. The R3 scorecard identified this: "The org shape recommendation is as
   evidence-dependent as the seam candidates." V-05/R4 closes this gap by adding an anti-
   fabrication note to B.2 matching the depth of the B.1 note.

**Three questions drive R4:**

1. Does a named `GATE-PASS-TOKEN:` protocol block — placed in the preamble, before Phase 1,
   defining the token format as a named constant — make C-17 structurally present rather
   than incidentally satisfied? (V-01)

2. Does adding an explicit named failure-state string (`Path floor not met`) to item 4 of
   the checklist gate — as a write-this-exact-string instruction — make gate failures
   machine-parseable without prose inspection, satisfying C-18? (V-02)

3. Does a table-driven output format with an inertia column — scan evidence in rows, each
   row carrying an inertia-match verdict — create a structurally distinct approach that
   satisfies all 10 aspirational criteria while varying the presentation axis? (V-03)

V-04/R4 combines V-01 (GATE-PASS-TOKEN block) + V-02 (fail token) on V-05/R3 base, making
both gate directions defined as named constants in a GATE TOKEN PROTOCOL block.
V-05/R4 is full integration: V-05/R3 base + GATE TOKEN PROTOCOL block (C-17 structural) +
explicit fail token (C-18) + B.2 anti-fabrication note (R3 Signal 1 gap).

---

## Round 4 Variation Map

| V | Axis | Primary change vs V-05/R3 | Hypothesis |
|---|------|--------------------------|------------|
| V-01 | Lifecycle emphasis — gate token protocol | Extract pass-token format into named `GATE-PASS-TOKEN:` protocol block before Phase 1; remove token from embedded gate instruction | Incidental confirmation token (V-05/R3) vs. defined constant (V-01/R4). Named block makes format-absence structurally detectable. Expected: C-17 PASS (structural), C-18 FAIL (no fail token). Composite: 100. |
| V-02 | Lifecycle emphasis — gate failure output | Add explicit `Path floor not met` fail string to item 4 of the checklist gate; gate fails write the string and stop | Gate failure becomes machine-parseable without prose inspection. Expected: C-17 PASS (inherited), C-18 PASS (new). Composite: 100. |
| V-03 | Output format — table-driven + inertia column | Replace prose scan log with evidence table; add Inertia Match column per row; replace prose sections with tables throughout | Tables force per-cell evidence discipline; inertia column surfaces scan value explicitly. Expected: C-17 PASS, C-18 PASS, all 10 aspirational. Composite: 100. |
| V-04 | Lifecycle emphasis — bidirectional gate tokens | Named `GATE TOKEN PROTOCOL` block defines both pass token and fail token as constants before Phase 1 | Both gate directions are machine-parseable. C-17 structural (pass token constant), C-18 structural (fail token constant). Expected: all 10 aspirational. Composite: 100. |
| V-05 | Full integration — all 10 aspirational + B.2 anti-fab | V-05/R3 base + GATE TOKEN PROTOCOL block + explicit fail token in item 4 + anti-fabrication note in B.2 | Closes all three R4 structural gaps simultaneously. Expected: C-17 PASS (structural), C-18 PASS, B.2 anti-fab closes R3 Signal 1 gap. All 10 aspirational. Composite: 100. |

---

## V-01 — Single-axis: C-17 (GATE-PASS-TOKEN Protocol Block)

**Variation axis**: Lifecycle emphasis — gate confirmation token format
**Hypothesis**: V-05/R3 had "Gate clear — ..." embedded as a confirmation sentence inside
the gate instruction. The token matched C-17's named-token format, but only because the
instruction text happened to use that phrasing. Extracting the token format into a named
`GATE-PASS-TOKEN:` block before Phase 1 makes the format a structural constant: defined
once, referenced at the gate. Absence of the block creates a detectable structural gap.
C-18 is not added — fail token remains implicit ("record the shortfall before proceeding"),
isolating C-17 as the single change axis.

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

**GATE-PASS-TOKEN**: Every gate in this skill, when it passes, writes this
exact confirmation string:

  `Gate clear — [N]/7 sources found, [N] paths cited, [N] absent.
  Path floor: [met / not met — N available].`

Do not paraphrase this token. Write it exactly as formatted.

---

### PHASE 1: Scan (breadth-first — complete all 7 sources before Group A)

Read each source type. Record your finding and cite at least one specific
file path. Mark ABSENT if the source type does not exist in the repo.

1. CLAUDE.md files
2. package.json / workspace manifests
3. design/ directories
4. Namespaces or top-level module structure
5. Test coverage files or directories
6. SPECS.md or specification files
7. .craft/roles/ files

---

### PHASE 1 GATE — MANDATORY BEFORE GROUP A

Verify all of the following before proceeding. Each item must be explicitly
confirmed or addressed before Group A begins:

1. All 7 source types have been visited (even if marked ABSENT)
2. Every source type that exists has at least one specific file path cited
3. Every absent source type is marked ABSENT with an implication noted
4. **Path floor gate**: At least 5 distinct file paths are cited across all
   sources. If this condition is not met, write the count of available paths
   and record the shortfall here before proceeding — not deferred to the
   Evidence Gaps section.
5. No analysis or conclusions have been written during Phase 1

Write the GATE-PASS-TOKEN (defined above) before beginning Group A.
Do not write a single word of Group A until the GATE-PASS-TOKEN is written.

---

## GROUP A: CURRENT STATE

*Anti-fabrication: Every claim in Group A must trace to a specific Phase 1
finding. Do not name areas, concerns, or patterns that lack Phase 1 evidence.
If you cannot point to a file or source, omit the item and note it as a gap.*

### A.1 Areas of Work

*Anti-fabrication: Only name areas you can trace to a Phase 1 finding. Every
area must have a cited source. Do not infer areas from general repo patterns
without direct scan evidence.*

From the Phase 1 scan log, identify distinct areas of work. Each area must
map to at least one Phase 1 finding. Minimum 3 areas.

For each area: name, 1-sentence description, Phase 1 source citation.

### A.2 Cross-Cutting Concerns

*Anti-fabrication: Cross-cutting concerns must be grounded in the areas above.
Do not import concerns from general software knowledge unless Phase 1 shows
this repo specifically has them. If a common concern is absent from the scan,
flag it as absent — do not include it as a finding.*

Name concerns spanning multiple areas that cannot be owned by one team without
coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

### A.3 Headcount Signals

*Anti-fabrication: Do not state a headcount range without derivation. A range
requires an explicit evidence chain — namespace count, role file count, spec
coverage breadth, or distinct test ownership. Round numbers with no evidence
chain do not pass this step.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

## GROUP B: RECOMMENDED STATE

*Anti-fabrication: Recommendations must cite Group A findings as their basis.
Do not introduce new observations in Group B — only interpret what Group A
produced.*

### B.1 Team Boundary Candidates

*Anti-fabrication: Every proposed seam must trace to evidence from Group A.
Do not propose a team boundary you cannot support with a scan finding. If
evidence is ambiguous, say so and note the ambiguity.*

Propose 2+ candidate seams. For each: boundary name, Group A evidence for
the seam, coupling risk (Low/Med/High) with a note.

### B.2 Recommended Org Shape

*Anti-fabrication: Justification must cite a specific Group A finding. General
org design reasoning without scan reference does not meet this step.*

Name one: flat / functional / matrix / pods / other (name it). Justify in
1-2 sentences by citing Group A findings.

---

### Evidence Gaps

List what the scan could not answer:
- Phase 1 source types marked ABSENT
- Path floor shortfalls recorded at the gate
- Group A sections with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output in three structural blocks: PHASE 1 (SCAN) / GROUP A:
CURRENT STATE / GROUP B: RECOMMENDED STATE, followed by EVIDENCE GAPS.
The GATE-PASS-TOKEN appears between Phase 1 and Group A. Group A and Group B
are discrete structural groups — the boundary between them is a named
categorical divide, not a prose transition.

Group A describes what the repo is today. Group B describes what the org
design should target.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## V-02 — Single-axis: C-18 (Explicit Gate Failure-State String)

**Variation axis**: Lifecycle emphasis — gate failure output
**Hypothesis**: V-05/R3's item 4 had an enforcement posture ("Path floor gate:") and a
conditional branch, but the failure branch said "record the shortfall before proceeding" —
not a named string the agent writes. Adding an explicit `Path floor not met` fail string
to item 4 makes the failure branch machine-parseable: a reader can detect gate failure by
scanning for the token, without interpreting prose. C-17 is inherited from V-05/R3 base
(the confirmation sentence is in "Gate clear — ..." named-token format). The single change
axis is C-18: the fail string is new.

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

### PHASE 1: Scan (breadth-first — complete all 7 sources before Group A)

Read each source type. Record your finding and cite at least one specific
file path. Mark ABSENT if the source type does not exist in the repo.

1. CLAUDE.md files
2. package.json / workspace manifests
3. design/ directories
4. Namespaces or top-level module structure
5. Test coverage files or directories
6. SPECS.md or specification files
7. .craft/roles/ files

---

### PHASE 1 GATE — MANDATORY BEFORE GROUP A

Verify all of the following before proceeding. Each item must be explicitly
confirmed or addressed before Group A begins:

1. All 7 source types have been visited (even if marked ABSENT)
2. Every source type that exists has at least one specific file path cited
3. Every absent source type is marked ABSENT with an implication noted
4. **Path floor gate**: At least 5 distinct file paths are cited across all
   sources.
   - If fewer than 5 paths: write `Path floor not met` and stop. Do not
     write Group A or Group B.
   - If 5 or more paths: continue to item 5.
5. No analysis or conclusions have been written during Phase 1

Write this confirmation sentence before beginning Group A:
"Gate clear — [N]/7 sources found, [N] paths cited, [N] absent. Path
floor: [met / not met — N available]."

Do not write a single word of Group A until this sentence is written.

---

## GROUP A: CURRENT STATE

*Anti-fabrication: Every claim in Group A must trace to a specific Phase 1
finding. Do not name areas, concerns, or patterns that lack Phase 1 evidence.
If you cannot point to a file or source, omit the item and note it as a gap.*

### A.1 Areas of Work

*Anti-fabrication: Only name areas you can trace to a Phase 1 finding. Every
area must have a cited source. Do not infer areas from general repo patterns
without direct scan evidence.*

From the Phase 1 scan log, identify distinct areas of work. Each area must
map to at least one Phase 1 finding. Minimum 3 areas.

For each area: name, 1-sentence description, Phase 1 source citation.

### A.2 Cross-Cutting Concerns

*Anti-fabrication: Cross-cutting concerns must be grounded in the areas above.
Do not import concerns from general software knowledge unless Phase 1 shows
this repo specifically has them. If a common concern is absent from the scan,
flag it as absent — do not include it as a finding.*

Name concerns spanning multiple areas that cannot be owned by one team without
coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

### A.3 Headcount Signals

*Anti-fabrication: Do not state a headcount range without derivation. A range
requires an explicit evidence chain — namespace count, role file count, spec
coverage breadth, or distinct test ownership. Round numbers with no evidence
chain do not pass this step.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

## GROUP B: RECOMMENDED STATE

*Anti-fabrication: Recommendations must cite Group A findings as their basis.
Do not introduce new observations in Group B — only interpret what Group A
produced.*

### B.1 Team Boundary Candidates

*Anti-fabrication: Every proposed seam must trace to evidence from Group A.
Do not propose a team boundary you cannot support with a scan finding. If
evidence is ambiguous, say so and note the ambiguity.*

Propose 2+ candidate seams. For each: boundary name, Group A evidence for
the seam, coupling risk (Low/Med/High) with a note.

### B.2 Recommended Org Shape

*Anti-fabrication: Justification must cite a specific Group A finding. General
org design reasoning without scan reference does not meet this step.*

Name one: flat / functional / matrix / pods / other (name it). Justify in
1-2 sentences by citing Group A findings.

---

### Evidence Gaps

List what the scan could not answer:
- Phase 1 source types marked ABSENT
- Path floor shortfalls (`Path floor not met` if gate failed)
- Group A sections with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output in three structural blocks: PHASE 1 (SCAN) / GROUP A:
CURRENT STATE / GROUP B: RECOMMENDED STATE, followed by EVIDENCE GAPS.
The Phase 1 gate confirmation appears between Phase 1 and Group A. If item 4
fails, write `Path floor not met` and stop — do not write Group A or Group B.

Group A describes what the repo is today. Group B describes what the org
design should target.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## V-03 — Single-axis: Output Format (Table-Driven + Inertia Column)

**Variation axis**: Output format — table-driven scan evidence with inertia contrast
**Hypothesis**: V-05/R3 uses prose scan logs and prose sections. Replacing the Phase 1
scan log with a structured evidence table (one row per file path, with Inertia Match
column) forces per-artifact evaluation of what the scan actually adds versus what teams
assume without scanning. Table format also satisfies C-09 structurally: paths appear in
table rows, not embedded in prose. C-17 and C-18 are both present: the gate uses the
"Gate clear — ..." named-token confirmation and an explicit `Path floor not met` fail
string on item 4.

```markdown
You are running /org-scan.

Walk the repo and produce a raw structural analysis of its org structure.
Output: areas of work, headcount signals, cross-cutting concerns, team
boundary candidates, and a recommended org shape.

**Critical constraint** (stated here and repeated in the output format below):
This is NOT an org chart. Do not produce reporting lines, role boxes, or
hierarchy diagrams at any point. The output feeds /org-chart, which will
build the structure from your analysis.

The inertia assumption: without scanning, most teams assume org structure
maps to top-level directory structure. This scan checks where that assumption
holds, where it contradicts, and where evidence is absent.

---

### PHASE 1: Scan (breadth-first — complete all 7 sources before Group A)

For each file you examine, record one row in the Phase 1 evidence table.
Mark ABSENT rows for source types that yield no files.

| # | File Path | Source Type | Finding | Inertia Match? |
|---|-----------|-------------|---------|----------------|

Source types (visit all 7, mark ABSENT if not present):
1. CLAUDE.md files
2. package.json / workspace manifests
3. design/ directories
4. Namespaces or top-level module structure
5. Test coverage files or directories
6. SPECS.md or specification files
7. .craft/roles/ files

*Anti-fabrication: Only record paths you actually find. Do not add rows for
expected paths that do not exist in the repo.*

---

### PHASE 1 GATE — MANDATORY BEFORE GROUP A

Verify all of the following before proceeding:

1. All 7 source types appear in the Phase 1 table (as found rows or ABSENT)
2. Every found source type has at least one row with a specific file path
3. Every ABSENT source type has an implication noted in its Finding cell
4. **Path floor gate**: At least 5 distinct file-path rows appear in the
   table (ABSENT rows do not count).
   - If fewer than 5 path rows: write `Path floor not met` and stop. Do not
     write Group A or Group B.
   - If 5 or more path rows: continue to item 5.
5. No analysis or conclusions appear in Phase 1 table cells — findings only

Write this confirmation sentence before beginning Group A:
"Gate clear — [N]/7 sources found, [N] paths cited, [N] absent. Path
floor: [met / not met — N available]."

Do not write a single word of Group A until this sentence is written.

---

## GROUP A: CURRENT STATE

### A.1 Areas of Work

| Area | Evidence paths | Inertia match? | Notes |
|------|----------------|----------------|-------|

*Anti-fabrication: Only include areas with at least one path from the Phase 1
evidence table. Do not add areas from general knowledge without direct scan
support. If an area has no Phase 1 row, omit it and note it as a gap.*

### A.2 Cross-Cutting Concerns

| Concern | Spans areas | Ownership implication | Inertia match? |
|---------|-------------|----------------------|----------------|

*Anti-fabrication: Concerns must trace to Phase 1 evidence rows. Do not import
concerns from general software knowledge unless Phase 1 shows this repo
specifically has them. Absent common concerns go in Evidence Gaps.*

### A.3 Headcount Signals

| Expertise domain | Phase 1 signal path |
|-----------------|---------------------|

**Range**: [N–M] engineers. **Derivation**: [cite domain rows above]

*Anti-fabrication: Range derivation must come from the domain rows above.
Round numbers with no evidence chain do not pass this step.*

---

## GROUP B: RECOMMENDED STATE

*Anti-fabrication: Recommendations must cite Group A findings as their basis.
Do not introduce new observations in Group B — only interpret what Group A
produced.*

### B.1 Team Boundary Candidates

| Boundary | Group A evidence | Coupling risk | Note |
|----------|-----------------|---------------|------|

*Anti-fabrication: Every proposed seam must trace to evidence from Group A.
Do not propose a team boundary you cannot support with a scan finding. If
evidence is ambiguous, mark the row and note the ambiguity.*

### B.2 Recommended Org Shape

**Shape**: [flat / functional / matrix / pods / other]
**Justification**: [cite specific Group A finding]

*Anti-fabrication: Justification must cite a specific Group A finding. General
org design reasoning without scan reference does not meet this step.*

---

### Evidence Gaps

| Gap | Source | Impact on analysis |
|-----|--------|--------------------|

Include: ABSENT source types, path floor shortfalls (`Path floor not met`
if gate failed), thin or ambiguous Group A rows, conflicting signals.

---

### Output format

Deliver output as: PHASE 1 table → gate confirmation → GROUP A (tables) →
GROUP B (tables) → EVIDENCE GAPS table. Table format throughout — prose
summaries are not a substitute for table rows.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## V-04 — Combination: C-17 + C-18 (Bidirectional Gate Token Protocol)

**Variation axes**: Lifecycle emphasis — both gate directions defined as named constants
**Hypothesis**: V-01/R4 defines the pass token as a named constant (C-17 structural).
V-02/R4 adds the fail string (C-18). V-04 combines both in a single `GATE TOKEN PROTOCOL`
block that defines pass token and fail token as named constants before any gate. This
makes the gate protocol bidirectionally machine-parseable by design: pass and fail are
both detectable without reading gate instruction prose. Neither token is embedded in the
gate instructions — both are defined once in the protocol block and referenced from there.

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

**GATE TOKEN PROTOCOL**

Every gate in this skill has two defined outcomes. Write the token exactly —
do not paraphrase.

- Pass: `Gate clear — [N]/7 sources found, [N] paths cited, [N] absent.
  Path floor: [met / not met — N available].`
- Fail: `Path floor not met`

When a gate passes, write the pass token and continue.
When a gate fails, write the fail token and stop.

---

### PHASE 1: Scan (breadth-first — complete all 7 sources before Group A)

Read each source type. Record your finding and cite at least one specific
file path. Mark ABSENT if the source type does not exist in the repo.

1. CLAUDE.md files
2. package.json / workspace manifests
3. design/ directories
4. Namespaces or top-level module structure
5. Test coverage files or directories
6. SPECS.md or specification files
7. .craft/roles/ files

---

### PHASE 1 GATE — MANDATORY BEFORE GROUP A

Verify all of the following before proceeding. Each item must be explicitly
confirmed or addressed before Group A begins:

1. All 7 source types have been visited (even if marked ABSENT)
2. Every source type that exists has at least one specific file path cited
3. Every absent source type is marked ABSENT with an implication noted
4. **Path floor gate**: At least 5 distinct file paths are cited across all
   sources. If this condition is not met, write the fail token and stop.
   Do not write Group A or Group B.
5. No analysis or conclusions have been written during Phase 1

Write the appropriate gate token (defined in GATE TOKEN PROTOCOL above)
before beginning Group A. Do not write a single word of Group A until the
pass token is written.

---

## GROUP A: CURRENT STATE

*Anti-fabrication: Every claim in Group A must trace to a specific Phase 1
finding. Do not name areas, concerns, or patterns that lack Phase 1 evidence.
If you cannot point to a file or source, omit the item and note it as a gap.*

### A.1 Areas of Work

*Anti-fabrication: Only name areas you can trace to a Phase 1 finding. Every
area must have a cited source. Do not infer areas from general repo patterns
without direct scan evidence.*

From the Phase 1 scan log, identify distinct areas of work. Each area must
map to at least one Phase 1 finding. Minimum 3 areas.

For each area: name, 1-sentence description, Phase 1 source citation.

### A.2 Cross-Cutting Concerns

*Anti-fabrication: Cross-cutting concerns must be grounded in the areas above.
Do not import concerns from general software knowledge unless Phase 1 shows
this repo specifically has them. If a common concern is absent from the scan,
flag it as absent — do not include it as a finding.*

Name concerns spanning multiple areas that cannot be owned by one team without
coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

### A.3 Headcount Signals

*Anti-fabrication: Do not state a headcount range without derivation. A range
requires an explicit evidence chain — namespace count, role file count, spec
coverage breadth, or distinct test ownership. Round numbers with no evidence
chain do not pass this step.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

## GROUP B: RECOMMENDED STATE

*Anti-fabrication: Recommendations must cite Group A findings as their basis.
Do not introduce new observations in Group B — only interpret what Group A
produced.*

### B.1 Team Boundary Candidates

*Anti-fabrication: Every proposed seam must trace to evidence from Group A.
Do not propose a team boundary you cannot support with a scan finding. If
evidence is ambiguous, say so and note the ambiguity.*

Propose 2+ candidate seams. For each: boundary name, Group A evidence for
the seam, coupling risk (Low/Med/High) with a note.

### B.2 Recommended Org Shape

*Anti-fabrication: Justification must cite a specific Group A finding. General
org design reasoning without scan reference does not meet this step.*

Name one: flat / functional / matrix / pods / other (name it). Justify in
1-2 sentences by citing Group A findings.

---

### Evidence Gaps

List what the scan could not answer:
- Phase 1 source types marked ABSENT
- Path floor shortfalls (fail token written at gate)
- Group A sections with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output in three structural blocks: PHASE 1 (SCAN) / GROUP A:
CURRENT STATE / GROUP B: RECOMMENDED STATE, followed by EVIDENCE GAPS.
The gate token appears between Phase 1 and Group A. Group A and Group B
are discrete structural groups — the boundary between them is a named
categorical divide, not a prose transition.

Group A describes what the repo is today. Group B describes what the org
design should target.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## V-05 — Full Integration: All 10 Aspirational Criteria + B.2 Anti-Fab

**Variation axes**: Lifecycle emphasis + Output format + Phrasing register
**Hypothesis**: V-05/R3 had all 8 v3 criteria, C-17 incidentally (confirmation token
in named-token format), C-18 missing (no explicit fail string), and B.2 without an
anti-fabrication note (R3 Signal 1 gap). V-05/R4 closes all three gaps: GATE TOKEN
PROTOCOL block makes C-17 structural; explicit fail string in item 4 satisfies C-18;
B.2 anti-fabrication note extends to "The org shape recommendation is as evidence-
dependent as the seam candidates" — the phrasing from the R3 scorecard's Signal 1.
Expected: all 10 aspirational pass by deliberate design, not by corollary or inheritance.

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

**GATE TOKEN PROTOCOL**

Every gate in this skill has two defined outcomes. Write the token exactly:

- Pass: `Gate clear — [N]/7 sources found, [N] paths cited, [N] absent.
  Path floor: [met / not met — N available].`
- Fail: `Path floor not met`

When a gate passes, write the pass token. When a gate fails, write the fail
token and stop. Do not paraphrase either token.

---

### PHASE 1: Scan (breadth-first — complete all 7 sources before Group A)

Read each source type. Record your finding and cite at least one specific
file path. Mark ABSENT if the source type does not exist in the repo.

1. CLAUDE.md files
2. package.json / workspace manifests
3. design/ directories
4. Namespaces or top-level module structure
5. Test coverage files or directories
6. SPECS.md or specification files
7. .craft/roles/ files

---

### PHASE 1 GATE — MANDATORY BEFORE GROUP A

Verify all of the following before proceeding. Each item must be explicitly
confirmed or addressed before Group A begins:

1. All 7 source types have been visited (even if marked ABSENT)
2. Every source type that exists has at least one specific file path cited
3. Every absent source type is marked ABSENT with an implication noted
4. **Path floor gate**: At least 5 distinct file paths are cited across all
   sources. If this condition is not met, write `Path floor not met` and
   stop — do not write Group A or Group B.
5. No analysis or conclusions have been written during Phase 1

Write the gate pass token (defined in GATE TOKEN PROTOCOL above) before
beginning Group A. Do not write a single word of Group A until the pass
token is written.

---

## GROUP A: CURRENT STATE

*Anti-fabrication: Every claim in Group A must trace to a specific Phase 1
finding. Do not name areas, concerns, or patterns that lack Phase 1 evidence.
If you cannot point to a file or source, omit the item and note it as a gap.*

### A.1 Areas of Work

*Anti-fabrication: Only name areas you can trace to a Phase 1 finding. Every
area must have a cited source. Do not infer areas from general repo patterns
without direct scan evidence.*

From the Phase 1 scan log, identify distinct areas of work. Each area must
map to at least one Phase 1 finding. Minimum 3 areas.

For each area: name, 1-sentence description, Phase 1 source citation.

### A.2 Cross-Cutting Concerns

*Anti-fabrication: Cross-cutting concerns must be grounded in the areas above.
Do not import concerns from general software knowledge unless Phase 1 shows
this repo specifically has them. If a common concern is absent from the scan,
flag it as absent — do not include it as a finding.*

Name concerns spanning multiple areas that cannot be owned by one team without
coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

### A.3 Headcount Signals

*Anti-fabrication: Do not state a headcount range without derivation. A range
requires an explicit evidence chain — namespace count, role file count, spec
coverage breadth, or distinct test ownership. Round numbers with no evidence
chain do not pass this step.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

## GROUP B: RECOMMENDED STATE

*Anti-fabrication: Recommendations must cite Group A findings as their basis.
Do not introduce new observations in Group B — only interpret what Group A
produced.*

### B.1 Team Boundary Candidates

*Anti-fabrication: Every proposed seam must trace to evidence from Group A.
Do not propose a team boundary you cannot support with a scan finding. If
evidence is ambiguous, say so and note the ambiguity.*

Propose 2+ candidate seams. For each: boundary name, Group A evidence for
the seam, coupling risk (Low/Med/High) with a note.

### B.2 Recommended Org Shape

*Anti-fabrication: Justification must cite a specific Group A finding. The org
shape recommendation is as evidence-dependent as the seam candidates — general
org design reasoning without scan reference does not meet this step.*

Name one: flat / functional / matrix / pods / other (name it). Justify in
1-2 sentences by citing Group A findings.

---

### Evidence Gaps

List what the scan could not answer:
- Phase 1 source types marked ABSENT
- Path floor shortfalls (`Path floor not met` if gate failed)
- Group A sections with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output in three structural blocks: PHASE 1 (SCAN) / GROUP A:
CURRENT STATE / GROUP B: RECOMMENDED STATE, followed by EVIDENCE GAPS.
The gate token appears between Phase 1 and Group A. Group A and Group B
are discrete structural groups — the boundary between them is a named
categorical divide, not a prose transition.

Group A describes what the repo is today. Group B describes what the org
design should target.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## Variation Summary

| ID | Primary Axis | C-17 | C-18 | B.2 anti-fab | Composite |
|----|---|---|---|---|---|
| V-01 | Lifecycle — GATE-PASS-TOKEN block (C-17 structural) | PASS (named constant) | FAIL (no fail string) | No (V-05/R3 level) | 100 |
| V-02 | Lifecycle — gate failure output (C-18 explicit) | PASS (inherited) | PASS (explicit fail string) | No (V-05/R3 level) | 100 |
| V-03 | Output format — table-driven + inertia column | PASS (inherited) | PASS (explicit fail string) | No (V-05/R3 level) | 100 |
| V-04 | Lifecycle — bidirectional gate tokens (C-17 + C-18) | PASS (named constant) | PASS (named constant) | No (V-05/R3 level) | 100 |
| V-05 | Full integration — all 10 explicit + B.2 anti-fab | PASS (named constant) | PASS (explicit + named) | YES (closes R3 Signal 1) | 100 |

---

## Aspirational Coverage Matrix (v4, 10 criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-09: 5+ paths cited | PASS | PASS | PASS | PASS | PASS |
| C-10: Current/recommended separated | PASS | PASS | PASS | PASS | PASS |
| C-11: Anti-fabrication per section | PASS | PASS | PASS | PASS | PASS |
| C-12: Hard sequencing gate | PASS | PASS | PASS | PASS | PASS |
| C-13: C-05 stated twice | PASS | PASS | PASS | PASS | PASS |
| C-14: Checklist gate | PASS | PASS | PASS | PASS | PASS |
| C-15: GROUP A/B labels | PASS | PASS | PASS | PASS | PASS |
| C-16: 5-path as gate condition | PASS | PASS | PASS | PASS | PASS |
| C-17: Gate confirmation token | PASS | PASS | PASS | PASS | PASS |
| C-18: Gate failure output | FAIL | PASS | PASS | PASS | PASS |

All variations golden. V-01 deliberately isolates C-17 by omitting C-18 — single-axis
clarity requires that the non-axis criteria remain at V-05/R3 level (which did not have
C-18). V-02 adds C-18 without adding the GATE TOKEN PROTOCOL block — C-17 passes
through the inherited confirmation sentence format, not through a named constant.

---

## New Patterns Not Yet Captured as Criteria

| Pattern | Source | Distinction from Existing Criteria |
|---|---|---|
| B.2 anti-fabrication (org shape justification) | V-05/R4 | C-11 requires anti-fab "per evidence-dependent section." V-05/R4 extends this to B.2 with the explicit statement "The org shape recommendation is as evidence-dependent as the seam candidates." Gap: C-11 does not name GROUP B sections as required coverage sites. A v5 criterion could require anti-fab notes in both GROUP A and GROUP B content sections explicitly. |
| GATE TOKEN PROTOCOL as preamble block | V-01/R4, V-04/R4, V-05/R4 | C-17 requires named-token format for the confirmation; it does not require the token format to be defined as a named constant before Phase 1. V-01/R4 shows this pattern: the GATE-PASS-TOKEN block is a structural anchor whose absence is detectable. A v5 criterion could require the token format to be defined in a named preamble block, not just embedded in gate instructions. |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["B.2 anti-fabrication — org shape recommendations are as evidence-dependent as seam candidates; GROUP B sections require anti-fabrication notes as explicitly as GROUP A sections", "GATE TOKEN PROTOCOL as named preamble block — pass token defined as a structural constant before Phase 1, making format-absence structurally detectable independent of gate instruction text"]}
```
