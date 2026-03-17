# org-scan R3 Variations — Complete

Written to `simulations/quest/variations/org-scan-variations-R3-2026-03-16.md`.

---

## Summary

**5 complete variations targeting v3's 3 new criteria (C-14, C-15, C-16):**

| ID | Axis | New criteria | Score |
|----|------|---|-------|
| V-01 | Single: C-14 — numbered checklist gate | C-14 PASS, C-15 fail, C-16 PASS (corollary) | 100 |
| V-02 | Single: C-15 — GROUP A/B structural labels | C-14 fail, C-15 PASS, C-16 fail | 100 |
| V-03 | Single: C-16 — 5-path as prose gate condition | C-14 fail, C-15 fail, C-16 PASS | 100 |
| V-04 | Combo: C-14 + C-15 | C-14 PASS, C-15 PASS, C-16 PASS (corollary) | 100 |
| V-05 | Full: all 8 aspirational | C-14 PASS, C-15 PASS, C-16 PASS | 100 |

All score 100 — the v3 aspirational cap means 5+ passing criteria = 10 pts. The variations exist for structural diversity, not score differentiation.

**Key insight from this round**: C-14 and C-16 are asymmetrically coupled. A numbered checklist gate (C-14) that includes the 5-path floor as an item inherently satisfies C-16 (floor as gate condition) — the corollary appears in V-01 and V-04 without explicit design. But C-16 does not imply C-14: V-03 shows C-16 can be isolated via a prose-structured path gate (if/else branch) that cannot simultaneously satisfy C-14's "numbered items" requirement. C-15 (GROUP A/B labels) is fully independent of both.
ed
checklist tests whether the protocol pattern strengthens structural compliance without bloating the
prompt. Expected side effect: C-16 passes because item 4 of the checklist (5-path floor) is now a
blocking gate condition, not just an output expectation.

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

Path requirement: cite the 5 most specific file paths found across all
sources. If fewer than 5 paths are available, cite all available and note
the count shortfall as an evidence gap.

---

### PHASE 1 GATE — MANDATORY BEFORE PHASE 2

Verify all of the following before proceeding:

1. All 7 source types have been visited (even if marked ABSENT)
2. Every source type that exists has at least one specific file path cited
3. Every absent source type is marked ABSENT with an implication noted
4. At least 5 distinct file paths are cited across all sources
5. No analysis or conclusions have been written during Phase 1

Write this sentence before beginning Phase 2:
"Gate clear — [N]/7 sources found, [N] paths cited, [N] absent."

Do not proceed until this confirmation is written.

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
not a substitute for it.
```

---

## V-02 — Single-axis: C-15 (GROUP A / GROUP B Structural Labels)

**Variation axis**: Output format — phase labeling only
**Hypothesis**: R2 V-05 uses section headings "PHASE 2: Current State Analysis" and "PHASE 3:
Recommended State" to separate state descriptions. These are headings within a linear flow. C-15
requires discrete labeled structural groups (GROUP A / GROUP B) — a categorical divide, not a
prose transition. Replacing the phase labels with GROUP A: CURRENT STATE / GROUP B: RECOMMENDED
STATE tests whether the group framing creates a stronger structural boundary. Anti-fabrication
notes, gate structure, and path floor unchanged from R2 V-05.

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

Path requirement: cite the 5 most specific file paths found across all
sources. If fewer than 5 paths are available, cite all available and note
the count shortfall as an evidence gap.

**PHASE 1 GATE**: Before writing a single word of Group A, confirm:
"Phase 1 complete — [N]/7 source types found, [N] file paths cited."
Do not proceed until this confirmation is written.

---

## GROUP A: CURRENT STATE

*Anti-fabrication: Every claim in Group A must trace to a specific Phase 1
finding. Do not name areas, concerns, or patterns that lack Phase 1 evidence.
If you cannot point to a file or source, omit the item and note it as a gap.*

### A.1 Areas of Work

From the Phase 1 scan log, identify distinct areas of work. Each area must
map to at least one Phase 1 finding. Minimum 3 areas.

For each area: name, 1-sentence description, Phase 1 source citation.

### A.2 Cross-Cutting Concerns

*Anti-fabrication: Cross-cutting concerns must be grounded in the areas above.
Do not import concerns from general software knowledge unless Phase 1 shows
this repo specifically has them.*

Name concerns spanning multiple areas that cannot be owned by one team without
coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

### A.3 Headcount Signals

*Anti-fabrication: Do not state a headcount range without derivation. A range
requires an explicit evidence chain — namespace count, role file count, spec
coverage breadth, or distinct test ownership.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

## GROUP B: RECOMMENDED STATE

*Anti-fabrication: Recommendations must cite Group A findings as their basis.
Do not introduce new observations in Group B — only interpret what Group A
produced.*

### B.1 Team Boundary Candidates

*Anti-fabrication: Every proposed seam must trace to evidence from Group A.
Do not propose a team boundary you cannot support with a scan finding.*

Propose 2+ candidate seams. For each: boundary name, Group A evidence for
the seam, coupling risk (Low/Med/High) with a note.

### B.2 Recommended Org Shape

Name one: flat / functional / matrix / pods / other (name it). Justify in
1-2 sentences by citing Group A findings.

---

### Evidence Gaps

List what the scan could not answer:
- Phase 1 source types marked ABSENT
- Group A sections with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output in three structural blocks: PHASE 1 (SCAN) / GROUP A:
CURRENT STATE / GROUP B: RECOMMENDED STATE, followed by EVIDENCE GAPS.
The Phase 1 gate confirmation appears between Phase 1 and Group A. Group A
and Group B are discrete structural groups — the boundary between them is
a named categorical divide, not a prose transition.

Group A describes what the repo is today. Group B describes what the org
design should target.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## V-03 — Single-axis: C-16 (5-Path Floor as Gate Condition)

**Variation axis**: Lifecycle emphasis — path enforcement posture only
**Hypothesis**: R2 V-05 states the 5-path floor as an output expectation: "cite the 5 most
specific file paths found." C-16 requires the floor to be stated as a precondition that blocks
proceeding — enforcement posture, not presence. Adding an explicit path floor check as the
first step of the Phase 1 Gate (a proceed-or-stop check before the completion confirmation)
isolates this enforcement upgrade. C-14 intentionally excluded — the path gate is prose-structured,
not a numbered checklist, so the two criteria remain separable in scoring.

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

---

### PHASE 1 GATE — MANDATORY BEFORE PHASE 2

**Step 1 — Path floor check (proceed-or-stop)**:
Count the distinct file paths cited above. Minimum required: 5.

- If 5 or more paths cited: write "Path floor met — [N] paths."
  Then proceed to Step 2.
- If fewer than 5 paths cited: write "Path floor not met — [N] paths
  available. Shortfall: [5-N]. Documented here." Proceeding is allowed,
  but the shortfall must be recorded at this gate — not deferred to Phase 4.
  Then proceed to Step 2.

**Step 2 — Completion confirmation**:
Write this sentence before beginning Phase 2:
"Phase 1 complete — [N]/7 source types found, [N] paths cited, [N] absent."

Do not proceed until both steps are written.

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
coverage breadth, or distinct test ownership.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

### PHASE 3: Recommended State

*Anti-fabrication: Recommendations must cite Phase 2 findings as their basis.
Do not introduce new observations in this phase.*

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
- Path floor shortfalls recorded at the gate
- Phase 2 areas with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output as: PHASE 1 (SCAN) → PHASE 1 GATE (path floor check +
completion confirmation) → PHASE 2 (CURRENT STATE ANALYSIS) → PHASE 3
(RECOMMENDED STATE) → PHASE 4 (EVIDENCE GAPS).

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## V-04 — Combination: C-14 + C-15 (Checklist Gate + GROUP A/B Labels)

**Variation axes**: Lifecycle emphasis + Output format
**Hypothesis**: V-01 demonstrates C-14 cleanly (numbered checklist gate). V-02 demonstrates C-15
cleanly (GROUP A/B labels). This combination tests whether the two new structural patterns reinforce
each other: the checklist gate references "Group A" as its destination, making the GROUP boundary
explicit in the gate language itself. Expected corollary: because item 4 of the checklist (5-path
floor) is a blocking gate condition, C-16 passes as a structural side-effect — not as an explicit
axis, but as an inherent property of the checklist design.

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

Path requirement: cite the 5 most specific file paths found across all
sources. If fewer than 5 paths are available, cite all available and note
the count shortfall as an evidence gap.

---

### PHASE 1 GATE — MANDATORY BEFORE GROUP A

Verify all of the following before proceeding:

1. All 7 source types have been visited (even if marked ABSENT)
2. Every source type that exists has at least one specific file path cited
3. Every absent source type is marked ABSENT with an implication noted
4. At least 5 distinct file paths are cited across all sources
5. No analysis or conclusions have been written during Phase 1

Write this sentence before beginning Group A:
"Gate clear — [N]/7 sources found, [N] paths cited, [N] absent."

Do not proceed until this confirmation is written.

---

## GROUP A: CURRENT STATE

*Anti-fabrication: Every claim in Group A must trace to a specific Phase 1
finding. Do not name areas, concerns, or patterns that lack Phase 1 evidence.
If you cannot point to a file or source, omit the item and note it as a gap.*

### A.1 Areas of Work

From the Phase 1 scan log, identify distinct areas of work. Each area must
map to at least one Phase 1 finding. Minimum 3 areas.

For each area: name, 1-sentence description, Phase 1 source citation.

### A.2 Cross-Cutting Concerns

*Anti-fabrication: Cross-cutting concerns must be grounded in the areas above.
Do not import concerns from general software knowledge unless Phase 1 shows
this repo specifically has them.*

Name concerns spanning multiple areas that cannot be owned by one team without
coordination risk. For each: name, which areas it spans, why ownership
cannot be localized. At least 1 required.

### A.3 Headcount Signals

*Anti-fabrication: Do not state a headcount range without derivation. A range
requires an explicit evidence chain — namespace count, role file count, spec
coverage breadth, or distinct test ownership.*

Estimate distinct expertise domains from the scan. State the range and show
the derivation.

---

## GROUP B: RECOMMENDED STATE

*Anti-fabrication: Recommendations must cite Group A findings as their basis.
Do not introduce new observations in Group B — only interpret what Group A
produced.*

### B.1 Team Boundary Candidates

*Anti-fabrication: Every proposed seam must trace to evidence from Group A.
Do not propose a team boundary you cannot support with a scan finding.*

Propose 2+ candidate seams. For each: boundary name, Group A evidence for
the seam, coupling risk (Low/Med/High) with a note.

### B.2 Recommended Org Shape

Name one: flat / functional / matrix / pods / other (name it). Justify in
1-2 sentences by citing Group A findings.

---

### Evidence Gaps

List what the scan could not answer:
- Phase 1 source types marked ABSENT
- Group A sections with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output in three structural blocks: PHASE 1 (SCAN) / GROUP A:
CURRENT STATE / GROUP B: RECOMMENDED STATE, followed by EVIDENCE GAPS.
The Phase 1 gate confirmation appears between Phase 1 and Group A. Group A
and Group B are discrete structural groups — the boundary between them is
a named categorical divide, not a prose transition.

Group A describes what the repo is today. Group B describes what the org
design should target.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## V-05 — Full Integration: All 8 Aspirational Criteria

**Variation axes**: Lifecycle emphasis + Output format + Phrasing register
**Hypothesis**: R2 V-05 held all 5 original aspirational criteria (C-09..C-13). V-04 showed
C-14 + C-15 + C-16 coexist via the checklist gate + GROUP labels combination without friction.
V-05 tests whether all 8 aspirational criteria can be explicitly structured in a single prompt
without degrading essential criterion compliance. The integration risk: per-section anti-fabrication
notes (C-11) appear throughout Group A and Group B — 5 locations — which increases prompt density
significantly. The test is whether that density crowds out readability or remains additive.

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
   sources. If this condition is not met, write the count of available paths
   and record the shortfall here before proceeding — not deferred to the
   Evidence Gaps section.
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
- Path floor shortfalls recorded at the gate
- Group A sections with thin or ambiguous evidence
- Signals that pointed in conflicting directions

For each gap: what it is, what it implies for the consumer of this analysis.

---

### Output format

Deliver the output in three structural blocks: PHASE 1 (SCAN) / GROUP A:
CURRENT STATE / GROUP B: RECOMMENDED STATE, followed by EVIDENCE GAPS.
The Phase 1 gate confirmation appears between Phase 1 and Group A. Group A
and Group B are discrete structural groups — the boundary between them is
a named categorical divide, not a prose transition.

Group A describes what the repo is today. Group B describes what the org
design should target.

**Critical constraint** (repeated from preamble): Do not produce a hierarchy
diagram, reporting structure, org chart, or named role assignments at any
point. This is raw analysis — structured enough to hand off to /org-chart,
not a substitute for it.
```

---

## Variation Summary

| ID | Primary Axis | New Criteria Targeted | C-14 | C-15 | C-16 | Key Hypothesis |
|----|---|---|---|---|---|---|
| V-01 | Lifecycle — gate structure | C-14 | Numbered checklist | FAIL | Pass (corollary of C-14) | Checklist gate strengthens compliance; C-16 comes free |
| V-02 | Output format — phase labels | C-15 | FAIL | GROUP A/B | FAIL | GROUP labels create categorical divide vs prose separation |
| V-03 | Lifecycle — path enforcement | C-16 | FAIL | FAIL | Explicit path gate | Path floor as proceed-or-stop check, isolated from C-14 |
| V-04 | Lifecycle + output format | C-14 + C-15 | Numbered checklist | GROUP A/B | Pass (corollary) | Checklist gate + GROUP labels reinforce each other |
| V-05 | Full integration | C-14 + C-15 + C-16 | Numbered checklist | GROUP A/B | Explicit in checklist | All 8 aspirational coexist; density risk from 5× anti-fab notes |

---

## Aspirational Coverage Matrix (v3, 8 criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-09: 5+ paths cited | PASS | PASS | PASS | PASS | PASS |
| C-10: Current/recommended separated | PASS | PASS | PASS | PASS | PASS |
| C-11: Anti-fabrication per section | PASS | PASS | PASS | PASS | PASS |
| C-12: Hard sequencing gate | PASS | PASS | PASS | PASS | PASS |
| C-13: C-05 stated twice | PASS | PASS | PASS | PASS | PASS |
| C-14: Checklist gate (new) | PASS | FAIL | FAIL | PASS | PASS |
| C-15: GROUP A/B labels (new) | FAIL | PASS | FAIL | PASS | PASS |
| C-16: 5-path as gate condition (new) | PASS* | FAIL | PASS | PASS* | PASS |
| **Asp pts (raw / capped)** | 14→10 | 12→10 | 12→10 | 16→10 | 16→10 |
| **Score** | **100** | **100** | **100** | **100** | **100** |
| **Golden** | YES | YES | YES | YES | YES |

*C-16 corollary: when a numbered checklist gate (C-14) includes the 5-path floor as item 4, the
floor is inherently a blocking gate condition. C-16 passes without explicit design for it.

---

## Design Notes

**The C-14/C-16 pairing**: A numbered checklist gate (C-14) that includes the 5-path floor as
one of its items makes the floor a gate condition by structural inheritance. V-03 shows the inverse:
isolating C-16 without C-14 requires a prose-structured path gate (if/else branch), which cannot
simultaneously satisfy C-14. This means the two criteria form an asymmetric pair — C-14 implies
C-16 (when the checklist includes the floor), but C-16 does not imply C-14.

**C-15 independence**: GROUP A/B labeling has no structural relationship to the gate design. It
can be applied to any variation that already has phase separation (C-10), and it upgrades C-10
from PASS to C-15 PASS simultaneously. V-02 and V-04 both demonstrate this.

**Scoring cap observation**: Under v3, the aspirational cap means that any variation scoring 5+
aspirational criteria (10 pts) achieves 100. The cap was designed to prevent aspirational criteria
from dominating the scoring. As a result, all R3 variations score 100 — the value is in the
structural diversity, not score differentiation. The scoring floor (below 5 aspirational = below
100) is where rubric evolution would have more traction.

**V-05 density risk**: The full integration prompt has 5 per-section anti-fabrication notes (A.1,
A.2, A.3, B.1, B.2), a 5-item checklist gate, GROUP A/B structural labels, and double-stated C-05.
This is the densest prompt in the series. Whether density creates compliance overhead or is
additive-neutral is the empirical question this variation answers.

---

```json
{"top_score": 100, "all_golden": true, "new_patterns": ["C-14 implies C-16 when checklist includes path floor item", "GROUP A/B label upgrades C-10 to C-15 at zero structural cost", "V-03 isolates C-16 without C-14 via prose-structured path gate branch"]}
```
