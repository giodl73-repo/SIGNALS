# Quest: Variate — org-build R13 (v9 rubric)

Five complete, runnable variations. Single-axis: V-01 (role sequence), V-02 (output format), V-03 (inertia framing). Combined: V-04 (lifecycle emphasis + formal register), V-05 (role sequence + skeleton-dominant format).

---

## V-01 — Axis: Role Sequence (Roles-First → Assessment → Artifacts)

**Hypothesis:** Enumerating the full role set before running the inertia assessment produces grounded verdicts — the IA evaluates an actual populated org rather than a hypothetical structure.

---

### Skill: org-build

You are generating a complete organizational structure from scan results or a repository. Produce: (1) `org-chart.md` in craftworks format with ASCII hierarchy diagram, headcount-by-area table, inertia assessment, anti-pattern watch, and org evolution roadmap; (2) typed `.roles/{area}/{role}.md` files for every role with five required fields.

**Inputs**

- `REPO_PATH` — path to the repository or scan output to analyze
- `DEPTH_FLAG` — `standard` (20–30 roles) or `deep` (50+ roles); default `standard`
- `TOPIC` — topic name used in artifact naming

---

#### IA Scope Templates (verbatim — copy the matching entry exactly; paraphrase fails)

```
NONE:     "Monitor for first signs of coordination overhead. FORBIDDEN: recommending any
           structural change until a repeating decision bottleneck has been documented
           across three consecutive sprints."

LOW:      "Represent the status quo. Challenge every hierarchy proposal by naming its cost
           in coordination overhead and cognitive load. FORBIDDEN: endorsing any structural
           addition until lightweight ceremony has been tried and documented as insufficient."

MODERATE: "Represent the status quo under acknowledged pressure. Accept ceremony additions.
           FORBIDDEN: endorsing layer additions before a 60-day observable outcome period
           completes."

HIGH:     "Accept a single targeted layer addition in the highest-friction area only.
           FORBIDDEN: endorsing org-wide restructuring. Require a reversibility plan with
           a sunset date before any structural change proceeds."

CRITICAL: "Accept that structure is warranted. Advocate for the minimum viable intervention
           only. FORBIDDEN: endorsing any structural addition without an explicit removal
           criterion and a 12-month sunset review date."
```

---

#### Phase 1 — Role Enumeration

**Task Steps**

1. Read the repository or scan output at `REPO_PATH`.
2. Identify all functional areas requiring dedicated ownership.
3. Enumerate every role: title, area, seniority level, primary function.
4. Bind `T1-DEPTH-FLAG` from the provided `DEPTH_FLAG` input.
5. Apply the count floor:
   - T1-DEPTH-FLAG = `standard` → enumerate 20–30 roles
   - T1-DEPTH-FLAG = `deep` → enumerate 50+ roles
6. Include an `inertia-advocate` role in the enumeration.

**Constraints**

- MUST enumerate exactly the role count required by T1-DEPTH-FLAG: standard = 20–30, deep = 50+.
- MUST include an `inertia-advocate` role. FORBIDDEN: omitting inertia-advocate.
- FORBIDDEN: enumerating roles not grounded in the scan or repository content.
- FORBIDDEN: beginning Phase 2 before emitting the Phase 1 record block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-ROLE-COUNT: [integer]
T1-AREAS: [comma-separated list of functional areas]
T1-IA-PRESENT: [YES | NO]
===
```

---

#### Phase 2 — Inertia Assessment

**Input Contract**

- MUST consume T1-DEPTH-FLAG, T1-ROLE-COUNT, T1-AREAS from the Phase 1 record block.
- FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.

**Task Steps**

1. Evaluate the role list for coordination overhead signals: span-of-control violations, repeated escalation paths, siloed expertise clusters.
2. Assign a FLAT-CASE-PRESSURE rating from the closed set: `NONE | LOW | MODERATE | HIGH | CRITICAL`.
3. Derive a single verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
4. Copy the verbatim IA scope template matching the FLAT-CASE-PRESSURE rating into `T2-IA-SCOPE-TEMPLATE`.
5. Select anti-pattern categories from the verdict:
   - CAN-OPERATE-FLAT → categories cat-2, cat-3
   - STRUCTURE-WARRANTED → categories cat-1, cat-4

**Constraints**

- MUST assign exactly one verdict. FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. FORBIDDEN: omitting both verdicts.
- MUST copy the verbatim template text into T2-IA-SCOPE-TEMPLATE. FORBIDDEN: paraphrasing, adapting, or deviating from the template text in any way.
- CAN-OPERATE-FLAT verdict: MUST include cat-2 and cat-3. FORBIDDEN: including cat-1 or cat-4.
- STRUCTURE-WARRANTED verdict: MUST include cat-1 and cat-4. FORBIDDEN: including cat-2 or cat-3.
- FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-SCOPE-TEMPLATE: [verbatim text of the applicable template — full copy, no abbreviation]
T2-ANTI-PATTERN-CATS: [cat-N, cat-N]
===
```

---

#### Phase 3 — Produce org-chart.md

**Input Contract**

- MUST consume T2-PRESSURE, T2-VERDICT, T2-IA-SCOPE-TEMPLATE, T2-ANTI-PATTERN-CATS from the Phase 2 record block.
- FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.

**Task Steps**

Produce `org-chart.md` with these seven sections in order:

1. **ASCII Hierarchy Diagram** — box/line diagram with minimum 2 org levels, every area from T1-AREAS represented.

2. **Headcount by Area** — table with columns: `Area | Headcount | Key Roles | Decides | Escalates`.

3. **Operating Rhythm** — table with columns: `Cadence | Meeting | Owner | Attendees | Output`. Rows must include ROB, shiproom, and at least one governance meeting. Each governance meeting gets a charter block with fields: Name, Purpose, Frequency, Quorum (as N of M fraction), Output.

4. **Inertia Assessment** — emit in this form:
   ```
   FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
   {{T2-VERDICT}}
   Only one verdict. Both is an error. Neither is an error.
   ```
   Append the verbatim text from T2-IA-SCOPE-TEMPLATE on the following line.

5. **Anti-Pattern Watch** — table with columns: `Anti-Pattern | Category | Why It Applies Here | Mitigation`. Include only categories from T2-ANTI-PATTERN-CATS. Every "Why It Applies Here" cell opens with `[element name] (cat-N) —`.

6. **Org Evolution Roadmap** — table with columns: `Trigger | Category | Structural Response`. Row 1 trigger is a headcount threshold. Row 2 trigger is a different category.

7. **Artifact Skeleton** — pre-print template for this artifact:
   ```
   FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
   VERDICT: {{T2-VERDICT}}
   IA-SCOPE: {{T2-IA-SCOPE-TEMPLATE}}
   ANTI-PATTERN-CATS: {{T2-ANTI-PATTERN-CATS}}
   ```

**Constraints**

- MUST produce all seven sections.
- FORBIDDEN: including anti-pattern categories not listed in T2-ANTI-PATTERN-CATS.
- FORBIDDEN: placing format guidance in Mitigation cells. MUST place a specific remediation action in each Mitigation cell.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in Section 4. FORBIDDEN: omitting both verdicts in Section 4.
- FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-SECTIONS-PRODUCED: [comma-separated section names]
T3-ANTI-PATTERN-ROWS: [integer]
T3-RHYTHM-ROWS: [integer]
===
```

---

#### Phase 4 — Produce .roles/ Files

**Input Contract**

- MUST consume T1-AREAS, T1-ROLE-COUNT from the Phase 1 record block.
- MUST consume T2-VERDICT, T2-IA-SCOPE-TEMPLATE from the Phase 2 record block.
- FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.

**Task Steps**

1. Create `.roles/{area}/{role}.md` for every role enumerated in Phase 1.
2. Each file contains five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
3. The `inertia-advocate` file `scope` field is the verbatim text from T2-IA-SCOPE-TEMPLATE.
4. Group files under area subdirectories matching T1-AREAS.

**Constraints**

- MUST produce one file per role enumerated in Phase 1. FORBIDDEN: producing fewer files than T1-ROLE-COUNT.
- MUST include all five fields in every file. FORBIDDEN: omitting any field from any role file.
- MUST group files under `.roles/{area}/` subdirectories. FORBIDDEN: placing all role files flat with no area grouping.
- MUST produce the inertia-advocate file. FORBIDDEN: omitting the inertia-advocate role.
- FORBIDDEN: placing the IA scope template text anywhere other than the `scope` field of the inertia-advocate file.
- FORBIDDEN: overwriting any `.roles/` file that already exists at the target path.

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no further phases begin before this block is emitted.
T4-FILES-PRODUCED: [integer]
T4-AREAS-USED: [comma-separated list]
T4-IA-FILE-PATH: [path to inertia-advocate file]
===
```

**Output artifact names**
- `simulations/org-build/{TOPIC}-org-chart-{date}.md`
- `.roles/{area}/{role}.md` — one per enumerated role

---

## V-02 — Axis: Output Format (Table-Heavy Constraints)

**Hypothesis:** Rendering constraint declarations in a dedicated table column (`Register: MUST | FORBIDDEN`) makes them structurally auditable as a class independent of task prose — satisfying C-30 via a distinct table structure rather than a separate prose section.

---

### Skill: org-build

Generate a complete organizational structure from scan results or a repository. Outputs: `org-chart.md` (ASCII diagram, headcount table, operating rhythm, inertia assessment, anti-pattern watch, org evolution roadmap) and typed `.roles/{area}/{role}.md` files for every role.

**Inputs:** `REPO_PATH`, `DEPTH_FLAG` (`standard` | `deep`), `TOPIC`

---

#### IA Scope Templates (verbatim — copy the matching entry exactly; paraphrase fails)

| Rating | Verbatim Scope Text |
|--------|---------------------|
| NONE | "Monitor for first signs of coordination overhead. FORBIDDEN: recommending any structural change until a repeating decision bottleneck has been documented across three consecutive sprints." |
| LOW | "Represent the status quo. Challenge every hierarchy proposal by naming its cost in coordination overhead and cognitive load. FORBIDDEN: endorsing any structural addition until lightweight ceremony has been tried and documented as insufficient." |
| MODERATE | "Represent the status quo under acknowledged pressure. Accept ceremony additions. FORBIDDEN: endorsing layer additions before a 60-day observable outcome period completes." |
| HIGH | "Accept a single targeted layer addition in the highest-friction area only. FORBIDDEN: endorsing org-wide restructuring. Require a reversibility plan with a sunset date before any structural change proceeds." |
| CRITICAL | "Accept that structure is warranted. Advocate for the minimum viable intervention only. FORBIDDEN: endorsing any structural addition without an explicit removal criterion and a 12-month sunset review date." |

---

#### Phase 1 — Ingest and Enumerate Roles

**Task Steps**

1. Read `REPO_PATH`. Identify all functional areas requiring dedicated ownership.
2. Bind T1-DEPTH-FLAG from `DEPTH_FLAG`.
3. Enumerate every role with: title, area, seniority level, primary function.
4. Include `inertia-advocate` in the enumeration unconditionally.

**Constraint Table**

| ID | Constraint Statement | Register | Trigger |
|----|----------------------|----------|---------|
| P1-C1 | Enumerate 20–30 roles when T1-DEPTH-FLAG = standard | MUST | always when standard |
| P1-C2 | Enumerate 50+ roles when T1-DEPTH-FLAG = deep | MUST | always when deep |
| P1-C3 | Include inertia-advocate role | MUST | unconditional |
| P1-C4 | Roles grounded in scan/repo content | MUST | all roles |
| P1-C5 | Begin Phase 2 before emitting Phase 1 record block | FORBIDDEN | phase transition |

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-ROLE-COUNT: [integer]
T1-AREAS: [comma-separated list]
T1-IA-PRESENT: [YES | NO]
===
```

---

#### Phase 2 — Inertia Assessment

**Input Contract Table**

| Variable | Source | Register |
|----------|--------|----------|
| T1-DEPTH-FLAG | Phase 1 record block | MUST consume |
| T1-ROLE-COUNT | Phase 1 record block | MUST consume |
| T1-AREAS | Phase 1 record block | MUST consume |
| Phase 1 record block emitted | prerequisite | FORBIDDEN: executing before |

**Task Steps**

1. Evaluate the role list for coordination overhead: span-of-control, repeated escalation paths, siloed expertise clusters.
2. Assign FLAT-CASE-PRESSURE from closed set: `NONE | LOW | MODERATE | HIGH | CRITICAL`.
3. Derive a single verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
4. Copy verbatim IA scope template for the assigned rating into T2-IA-SCOPE-TEMPLATE.
5. Select anti-pattern categories per verdict path:
   - CAN-OPERATE-FLAT → cat-2, cat-3
   - STRUCTURE-WARRANTED → cat-1, cat-4

**Constraint Table**

| ID | Constraint Statement | Register | Trigger |
|----|----------------------|----------|---------|
| P2-C1 | Assign exactly one verdict | MUST | unconditional |
| P2-C2 | Write both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED | FORBIDDEN | verdict emission |
| P2-C3 | Omit both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED | FORBIDDEN | verdict emission |
| P2-C4 | Copy verbatim template text for assigned rating | MUST | IA scope |
| P2-C5 | Paraphrase, adapt, or deviate from template text | FORBIDDEN | IA scope |
| P2-C6 | Include cat-2, cat-3 when verdict = CAN-OPERATE-FLAT | MUST | anti-pattern selection |
| P2-C7 | Include cat-1 or cat-4 when verdict = CAN-OPERATE-FLAT | FORBIDDEN | anti-pattern selection |
| P2-C8 | Include cat-1, cat-4 when verdict = STRUCTURE-WARRANTED | MUST | anti-pattern selection |
| P2-C9 | Include cat-2 or cat-3 when verdict = STRUCTURE-WARRANTED | FORBIDDEN | anti-pattern selection |
| P2-C10 | Begin Phase 3 before emitting Phase 2 record block | FORBIDDEN | phase transition |

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-SCOPE-TEMPLATE: [verbatim text — full copy, no abbreviation]
T2-ANTI-PATTERN-CATS: [cat-N, cat-N]
===
```

---

#### Phase 3 — Produce org-chart.md

**Input Contract Table**

| Variable | Source | Register |
|----------|--------|----------|
| T2-PRESSURE | Phase 2 record block | MUST consume |
| T2-VERDICT | Phase 2 record block | MUST consume |
| T2-IA-SCOPE-TEMPLATE | Phase 2 record block | MUST consume |
| T2-ANTI-PATTERN-CATS | Phase 2 record block | MUST consume |
| Phase 2 record block emitted | prerequisite | FORBIDDEN: executing before |

**Task Steps**

Produce `org-chart.md` with these sections:

1. **ASCII Hierarchy Diagram** — min 2 org levels, all areas from T1-AREAS represented.
2. **Headcount by Area** — `Area | Headcount | Key Roles | Decides | Escalates`
3. **Operating Rhythm** — `Cadence | Meeting | Owner | Attendees | Output` — ROB, shiproom, governance (3+ rows). Each governance meeting: charter with Name, Purpose, Frequency, Quorum (N of M), Output.
4. **Inertia Assessment**:
   ```
   FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
   {{T2-VERDICT}}
   Only one verdict. Both is an error. Neither is an error.
   [verbatim IA scope text from T2-IA-SCOPE-TEMPLATE]
   ```
5. **Anti-Pattern Watch** — `Anti-Pattern | Category | Why It Applies Here | Mitigation`
6. **Org Evolution Roadmap** — `Trigger | Category | Structural Response` — Row 1: headcount threshold. Row 2: different trigger category.
7. **Artifact Skeleton**:
   ```
   FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
   VERDICT: {{T2-VERDICT}}
   IA-SCOPE: {{T2-IA-SCOPE-TEMPLATE}}
   ANTI-PATTERN-CATS: {{T2-ANTI-PATTERN-CATS}}
   ```

**Constraint Table**

| ID | Constraint Statement | Register | Trigger |
|----|----------------------|----------|---------|
| P3-C1 | Produce all seven sections | MUST | unconditional |
| P3-C2 | Include anti-pattern categories not in T2-ANTI-PATTERN-CATS | FORBIDDEN | anti-pattern table |
| P3-C3 | "Why It Applies Here" cell opens with `[element name] (cat-N) —` | MUST | every row |
| P3-C4 | Place format guidance in Mitigation cells | FORBIDDEN | anti-pattern table |
| P3-C5 | Each Mitigation cell contains a specific remediation action | MUST | every row |
| P3-C6 | Write both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in Section 4 | FORBIDDEN | inertia assessment |
| P3-C7 | Omit both verdicts from Section 4 | FORBIDDEN | inertia assessment |
| P3-C8 | Org Evolution Roadmap has min 2 rows, Row 1 headcount trigger | MUST | roadmap |
| P3-C9 | Row 2 trigger uses same category as Row 1 | FORBIDDEN | roadmap |
| P3-C10 | Begin Phase 4 before emitting Phase 3 record block | FORBIDDEN | phase transition |

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-SECTIONS-PRODUCED: [comma-separated section names]
T3-ANTI-PATTERN-ROWS: [integer]
T3-RHYTHM-ROWS: [integer]
===
```

---

#### Phase 4 — Produce .roles/ Files

**Input Contract Table**

| Variable | Source | Register |
|----------|--------|----------|
| T1-AREAS | Phase 1 record block | MUST consume |
| T1-ROLE-COUNT | Phase 1 record block | MUST consume |
| T2-VERDICT | Phase 2 record block | MUST consume |
| T2-IA-SCOPE-TEMPLATE | Phase 2 record block | MUST consume |
| Phase 3 record block emitted | prerequisite | FORBIDDEN: executing before |

**Task Steps**

1. Create `.roles/{area}/{role}.md` for every role from Phase 1.
2. Each file contains: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
3. `inertia-advocate` `scope` field = verbatim text from T2-IA-SCOPE-TEMPLATE.
4. Group files under area subdirectories matching T1-AREAS.

**Constraint Table**

| ID | Constraint Statement | Register | Trigger |
|----|----------------------|----------|---------|
| P4-C1 | Produce one file per role enumerated in Phase 1 | MUST | all roles |
| P4-C2 | Produce fewer files than T1-ROLE-COUNT | FORBIDDEN | file production |
| P4-C3 | Include all five fields in every role file | MUST | every file |
| P4-C4 | Omit any field from any role file | FORBIDDEN | every file |
| P4-C5 | Group files under `.roles/{area}/` subdirectories | MUST | file structure |
| P4-C6 | Place all role files flat with no area grouping | FORBIDDEN | file structure |
| P4-C7 | Produce the inertia-advocate file | MUST | unconditional |
| P4-C8 | Omit the inertia-advocate role | FORBIDDEN | unconditional |
| P4-C9 | IA scope field contains verbatim text from T2-IA-SCOPE-TEMPLATE | MUST | IA file only |
| P4-C10 | Paraphrase IA scope in the inertia-advocate file | FORBIDDEN | IA file only |
| P4-C11 | Overwrite any `.roles/` file already existing at target path | FORBIDDEN | all files |

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no further phases begin before this block is emitted.
T4-FILES-PRODUCED: [integer]
T4-AREAS-USED: [comma-separated list]
T4-IA-FILE-PATH: [path]
===
```

---

## V-03 — Axis: Inertia Framing (IA Assessment Leads — Assessment-First → Roles → Artifacts)

**Hypothesis:** Running the inertia assessment as the first act — before enumerating any roles — frames the entire role architecture as a response to a known structural verdict rather than an assessment of a completed structure. The IA advocate is present from the start, not appended after the fact.

---

### Skill: org-build

Generate a complete organizational structure from scan results or a repository. The inertia-advocate leads: the FLAT-CASE-PRESSURE verdict is the first output, and the entire org is built in response to it. Outputs: `org-chart.md` and typed `.roles/{area}/{role}.md` files.

**Inputs:** `REPO_PATH`, `DEPTH_FLAG` (`standard` | `deep`), `TOPIC`

---

#### IA Scope Templates (verbatim — copy the matching entry exactly; paraphrase fails)

```
NONE:     "Monitor for first signs of coordination overhead. FORBIDDEN: recommending any
           structural change until a repeating decision bottleneck has been documented
           across three consecutive sprints."

LOW:      "Represent the status quo. Challenge every hierarchy proposal by naming its cost
           in coordination overhead and cognitive load. FORBIDDEN: endorsing any structural
           addition until lightweight ceremony has been tried and documented as insufficient."

MODERATE: "Represent the status quo under acknowledged pressure. Accept ceremony additions.
           FORBIDDEN: endorsing layer additions before a 60-day observable outcome period
           completes."

HIGH:     "Accept a single targeted layer addition in the highest-friction area only.
           FORBIDDEN: endorsing org-wide restructuring. Require a reversibility plan with
           a sunset date before any structural change proceeds."

CRITICAL: "Accept that structure is warranted. Advocate for the minimum viable intervention
           only. FORBIDDEN: endorsing any structural addition without an explicit removal
           criterion and a 12-month sunset review date."
```

---

#### Phase 1 — Ingest and Assess

**Task Steps**

1. Read `REPO_PATH`. Extract: team size, functional areas, decision bottlenecks, escalation patterns, expertise clusters.
2. Bind T1-DEPTH-FLAG from `DEPTH_FLAG`.
3. Assign FLAT-CASE-PRESSURE from closed set: `NONE | LOW | MODERATE | HIGH | CRITICAL` based on what the scan reveals.
4. Derive a single verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
5. Copy verbatim IA scope template for the assigned rating into T1-IA-SCOPE-TEMPLATE.
6. Select anti-pattern categories from the verdict:
   - CAN-OPERATE-FLAT → cat-2, cat-3
   - STRUCTURE-WARRANTED → cat-1, cat-4

**Constraints**

- MUST assign exactly one FLAT-CASE-PRESSURE rating. FORBIDDEN: leaving the rating unassigned.
- MUST assign exactly one verdict. FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. FORBIDDEN: omitting both verdicts.
- MUST copy verbatim template text. FORBIDDEN: paraphrasing or adapting the template text in any way.
- CAN-OPERATE-FLAT: MUST select cat-2, cat-3. FORBIDDEN: selecting cat-1 or cat-4.
- STRUCTURE-WARRANTED: MUST select cat-1, cat-4. FORBIDDEN: selecting cat-2 or cat-3.
- FORBIDDEN: beginning Phase 2 before emitting the Phase 1 record block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T1-IA-SCOPE-TEMPLATE: [verbatim text — full copy, no abbreviation]
T1-ANTI-PATTERN-CATS: [cat-N, cat-N]
T1-FUNCTIONAL-AREAS: [comma-separated list]
===
```

---

#### Phase 2 — Role Enumeration (Shaped by Verdict)

**Input Contract**

- MUST consume T1-DEPTH-FLAG, T1-VERDICT, T1-FUNCTIONAL-AREAS from the Phase 1 record block.
- FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.

**Task Steps**

1. Enumerate every role the repo/scan calls for: title, area, seniority, primary function.
2. Shape the role architecture to reflect T1-VERDICT:
   - CAN-OPERATE-FLAT → enumerate roles in flat bands without a management layer above IC level.
   - STRUCTURE-WARRANTED → enumerate roles including at least one management or lead layer.
3. Apply the count floor keyed to T1-DEPTH-FLAG:
   - T1-DEPTH-FLAG = `standard` → enumerate 20–30 roles
   - T1-DEPTH-FLAG = `deep` → enumerate 50+ roles
4. Include `inertia-advocate` in the enumeration unconditionally.

**Constraints**

- MUST enumerate roles in the range required by T1-DEPTH-FLAG: standard = 20–30, deep = 50+.
- MUST include an `inertia-advocate` role. FORBIDDEN: omitting inertia-advocate.
- MUST shape the role architecture to reflect T1-VERDICT as specified above.
- FORBIDDEN: enumerating roles that are not grounded in the scan or repository content.
- FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT: [integer]
T2-AREAS: [comma-separated list]
T2-IA-PRESENT: [YES | NO]
T2-VERDICT-SHAPE-APPLIED: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===
```

---

#### Phase 3 — Produce org-chart.md

**Input Contract**

- MUST consume T1-PRESSURE, T1-VERDICT, T1-IA-SCOPE-TEMPLATE, T1-ANTI-PATTERN-CATS from the Phase 1 record block.
- MUST consume T2-ROLE-COUNT, T2-AREAS from the Phase 2 record block.
- FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.

**Task Steps**

Produce `org-chart.md` with these seven sections:

1. **ASCII Hierarchy Diagram** — box/line diagram, min 2 org levels, all areas from T2-AREAS.

2. **Headcount by Area** — table: `Area | Headcount | Key Roles | Decides | Escalates`.

3. **Operating Rhythm** — table: `Cadence | Meeting | Owner | Attendees | Output`. Rows: ROB, shiproom, plus at least one governance meeting (3+ rows total). Each governance meeting has a charter with: Name, Purpose, Frequency, Quorum (N of M), Output.

4. **Inertia Assessment**:
   ```
   FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
   {{T1-VERDICT}}
   Only one verdict. Both is an error. Neither is an error.
   [verbatim text from T1-IA-SCOPE-TEMPLATE]
   ```

5. **Anti-Pattern Watch** — table: `Anti-Pattern | Category | Why It Applies Here | Mitigation`.
   Every "Why It Applies Here" cell opens with `[element name] (cat-N) —`.
   Every Mitigation cell contains a specific remediation action.

6. **Org Evolution Roadmap** — table: `Trigger | Category | Structural Response`.
   Row 1: headcount threshold. Row 2: different trigger category.

7. **Artifact Skeleton**:
   ```
   FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
   VERDICT: {{T1-VERDICT}}
   IA-SCOPE: {{T1-IA-SCOPE-TEMPLATE}}
   ANTI-PATTERN-CATS: {{T1-ANTI-PATTERN-CATS}}
   ROLE-COUNT: {{T2-ROLE-COUNT}}
   ```

**Constraints**

- MUST produce all seven sections.
- FORBIDDEN: including anti-pattern categories not in T1-ANTI-PATTERN-CATS.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in Section 4. FORBIDDEN: omitting both.
- FORBIDDEN: placing format guidance in Mitigation cells. MUST place a specific remediation action in each Mitigation cell.
- FORBIDDEN: opening a "Why It Applies Here" cell without `[element name] (cat-N) —`.
- FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-SECTIONS-PRODUCED: [comma-separated section names]
T3-ANTI-PATTERN-ROWS: [integer]
T3-RHYTHM-ROWS: [integer]
===
```

---

#### Phase 4 — Produce .roles/ Files

**Input Contract**

- MUST consume T2-AREAS, T2-ROLE-COUNT from the Phase 2 record block.
- MUST consume T1-IA-SCOPE-TEMPLATE from the Phase 1 record block.
- FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.

**Task Steps**

1. Create `.roles/{area}/{role}.md` for every role enumerated in Phase 2.
2. Each file: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
3. `inertia-advocate` `scope` = verbatim text from T1-IA-SCOPE-TEMPLATE.
4. Group under area subdirectories matching T2-AREAS.

**Constraints**

- MUST produce one file per role. FORBIDDEN: producing fewer files than T2-ROLE-COUNT.
- MUST include all five fields in every file. FORBIDDEN: omitting any field from any file.
- MUST group files under area subdirectories. FORBIDDEN: placing all files flat with no area grouping.
- MUST produce the inertia-advocate file. FORBIDDEN: omitting inertia-advocate.
- MUST write verbatim template text into IA `scope`. FORBIDDEN: paraphrasing or adapting.
- FORBIDDEN: overwriting any `.roles/` file that already exists at the target path.

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no further phases begin before this block is emitted.
T4-FILES-PRODUCED: [integer]
T4-AREAS-USED: [comma-separated list]
T4-IA-FILE-PATH: [path]
===
```

---

## V-04 — Combined: Lifecycle Emphasis (Equal-Depth Phases) + Formal Register

**Hypothesis:** Enforcing structural symmetry across all phases — identical section headers (Purpose / Inputs / Task Steps / Constraints / Gate Variables / Record Block) — and a strictly formal register maximizes rubric coverage for the structural-segmentation criteria (C-30) and reduces constraint-omission risk because every phase follows the same auditable template.

---

### Skill: org-build

**Purpose:** Generate a complete organizational structure artifact set from a repository or scan output, producing an org-chart document and typed role files.

**Input Parameters**

| Parameter | Type | Values | Default |
|-----------|------|--------|---------|
| REPO_PATH | path | any valid path | — |
| DEPTH_FLAG | enum | `standard` \| `deep` | `standard` |
| TOPIC | string | topic identifier | — |

---

#### IA Scope Templates — Verbatim Reference

The following templates are the authoritative text for the `inertia-advocate` `scope` field. The applicable template is selected by matching the FLAT-CASE-PRESSURE rating. Copy the text verbatim. Paraphrase, condensation, or rewording of any kind constitutes a constraint violation.

| Rating | Verbatim Scope Text |
|--------|---------------------|
| NONE | "Monitor for first signs of coordination overhead. FORBIDDEN: recommending any structural change until a repeating decision bottleneck has been documented across three consecutive sprints." |
| LOW | "Represent the status quo. Challenge every hierarchy proposal by naming its cost in coordination overhead and cognitive load. FORBIDDEN: endorsing any structural addition until lightweight ceremony has been tried and documented as insufficient." |
| MODERATE | "Represent the status quo under acknowledged pressure. Accept ceremony additions. FORBIDDEN: endorsing layer additions before a 60-day observable outcome period completes." |
| HIGH | "Accept a single targeted layer addition in the highest-friction area only. FORBIDDEN: endorsing org-wide restructuring. Require a reversibility plan with a sunset date before any structural change proceeds." |
| CRITICAL | "Accept that structure is warranted. Advocate for the minimum viable intervention only. FORBIDDEN: endorsing any structural addition without an explicit removal criterion and a 12-month sunset review date." |

---

#### Phase 1 — Parameter Ingestion and Role Enumeration

**Purpose:** Read the repository or scan output, bind the depth parameter, and enumerate the complete role set that will serve as the foundation for all subsequent phases.

**Inputs**

| Variable | Source |
|----------|--------|
| REPO_PATH | invocation parameter |
| DEPTH_FLAG | invocation parameter |

**Task Steps**

1. Read the repository or scan output at REPO_PATH.
2. Identify all functional areas requiring dedicated ownership. Record them as the canonical area list.
3. Bind T1-DEPTH-FLAG from the DEPTH_FLAG parameter.
4. Enumerate every role: title, area, seniority level, primary function.
5. Include `inertia-advocate` in the enumeration unconditionally.
6. Count the enumerated roles and record as T1-ROLE-COUNT.

**Constraints**

- MUST enumerate roles within the range specified by T1-DEPTH-FLAG: `standard` → 20–30 roles; `deep` → 50+ roles.
- MUST include an `inertia-advocate` role in the enumeration.
- FORBIDDEN: enumerating roles not grounded in the content of REPO_PATH.
- FORBIDDEN: enumerating fewer roles than the T1-DEPTH-FLAG lower bound.
- FORBIDDEN: beginning Phase 2 before emitting the Phase 1 record block.

**Gate Variables**

| Variable | Type | Description |
|----------|------|-------------|
| T1-DEPTH-FLAG | enum | `standard` or `deep` |
| T1-ROLE-COUNT | integer | total roles enumerated |
| T1-AREAS | string-list | functional areas identified |
| T1-IA-PRESENT | boolean | YES if inertia-advocate is in enumeration |

**Record Block**

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-ROLE-COUNT: [integer]
T1-AREAS: [comma-separated list]
T1-IA-PRESENT: [YES | NO]
===
```

---

#### Phase 2 — Inertia Assessment

**Purpose:** Evaluate the enumerated role set for structural pressure, assign the FLAT-CASE-PRESSURE rating, derive the verdict, and select the applicable IA scope template and anti-pattern categories.

**Inputs**

| Variable | Source | Register |
|----------|--------|----------|
| T1-DEPTH-FLAG | Phase 1 record block | MUST consume |
| T1-ROLE-COUNT | Phase 1 record block | MUST consume |
| T1-AREAS | Phase 1 record block | MUST consume |
| T1-IA-PRESENT | Phase 1 record block | MUST consume |
| Phase 1 record block emitted | prerequisite | FORBIDDEN: executing before |

**Task Steps**

1. Evaluate the role list for coordination overhead signals: span-of-control violations, repeated escalation paths, siloed expertise clusters.
2. Assign a FLAT-CASE-PRESSURE rating from the closed set: `NONE | LOW | MODERATE | HIGH | CRITICAL`.
3. Derive a single verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
4. Locate the verbatim IA scope template for the assigned rating in the IA Scope Templates table above. Copy the text exactly into T2-IA-SCOPE-TEMPLATE.
5. Determine anti-pattern categories from the verdict path.

**Constraints**

- MUST assign exactly one FLAT-CASE-PRESSURE rating from the closed set.
- MUST assign exactly one verdict.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. FORBIDDEN: omitting both verdicts.
- MUST copy the verbatim template text from the IA Scope Templates table. FORBIDDEN: paraphrasing, condensing, or rewording the template text.
- CAN-OPERATE-FLAT verdict: MUST record cat-2 and cat-3 in T2-ANTI-PATTERN-CATS. FORBIDDEN: recording cat-1 or cat-4.
- STRUCTURE-WARRANTED verdict: MUST record cat-1 and cat-4 in T2-ANTI-PATTERN-CATS. FORBIDDEN: recording cat-2 or cat-3.
- FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

**Gate Variables**

| Variable | Type | Description |
|----------|------|-------------|
| T2-PRESSURE | enum | NONE \| LOW \| MODERATE \| HIGH \| CRITICAL |
| T2-VERDICT | enum | CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED |
| T2-IA-SCOPE-TEMPLATE | string | verbatim text of applicable template |
| T2-ANTI-PATTERN-CATS | string-list | categories required by verdict path |

**Record Block**

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-SCOPE-TEMPLATE: [verbatim text — full copy, no abbreviation]
T2-ANTI-PATTERN-CATS: [cat-N, cat-N]
===
```

---

#### Phase 3 — Produce org-chart.md

**Purpose:** Assemble the org-chart.md document from all gate variable values. Every section derives from a named typed variable emitted in a preceding record block.

**Inputs**

| Variable | Source | Register |
|----------|--------|----------|
| T1-AREAS | Phase 1 record block | MUST consume |
| T1-ROLE-COUNT | Phase 1 record block | MUST consume |
| T2-PRESSURE | Phase 2 record block | MUST consume |
| T2-VERDICT | Phase 2 record block | MUST consume |
| T2-IA-SCOPE-TEMPLATE | Phase 2 record block | MUST consume |
| T2-ANTI-PATTERN-CATS | Phase 2 record block | MUST consume |
| Phase 2 record block emitted | prerequisite | FORBIDDEN: executing before |

**Task Steps**

Produce `org-chart.md` with the following sections in order:

**Section 1 — ASCII Hierarchy Diagram**
Box/line diagram with minimum 2 org levels. All areas from T1-AREAS appear as labeled boxes.

**Section 2 — Headcount by Area**
Table: `Area | Headcount | Key Roles | Decides | Escalates`

**Section 3 — Operating Rhythm**
Table: `Cadence | Meeting | Owner | Attendees | Output`
Include: one ROB row, one shiproom row, at least one governance row (minimum 3 rows total).
For each governance meeting, append a charter block: Name, Purpose, Frequency, Quorum (N of M), Output.

**Section 4 — Inertia Assessment**
Emit the following verbatim structure:
```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
{{T2-VERDICT}}
Only one verdict. Both is an error. Neither is an error.
```
On the next line, emit the full verbatim text of T2-IA-SCOPE-TEMPLATE.

**Section 5 — Anti-Pattern Watch**
Table: `Anti-Pattern | Category | Why It Applies Here | Mitigation`
Populate using only categories from T2-ANTI-PATTERN-CATS.

**Section 6 — Org Evolution Roadmap**
Table: `Trigger | Category | Structural Response`
Minimum 2 rows: Row 1 uses a headcount threshold trigger. Row 2 uses a different trigger category.

**Section 7 — Artifact Skeleton**
```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
IA-SCOPE: {{T2-IA-SCOPE-TEMPLATE}}
ANTI-PATTERN-CATS: {{T2-ANTI-PATTERN-CATS}}
AREAS: {{T1-AREAS}}
ROLE-COUNT: {{T1-ROLE-COUNT}}
```

**Constraints**

- MUST produce all seven sections in order.
- FORBIDDEN: including anti-pattern categories absent from T2-ANTI-PATTERN-CATS.
- MUST open every "Why It Applies Here" cell with `[element name] (cat-N) —`.
- FORBIDDEN: placing format guidance in Mitigation cells. MUST place a specific remediation action in each Mitigation cell.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in Section 4. FORBIDDEN: omitting both verdicts in Section 4.
- MUST include the Quorum field as an N of M fraction in each governance charter.
- FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

**Gate Variables**

| Variable | Type | Description |
|----------|------|-------------|
| T3-SECTIONS-PRODUCED | string-list | names of sections produced |
| T3-ANTI-PATTERN-ROWS | integer | row count in anti-pattern table |
| T3-RHYTHM-ROWS | integer | row count in rhythm table |

**Record Block**

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-SECTIONS-PRODUCED: [comma-separated section names]
T3-ANTI-PATTERN-ROWS: [integer]
T3-RHYTHM-ROWS: [integer]
===
```

---

#### Phase 4 — Produce .roles/ Files

**Purpose:** Write one typed role file for every role enumerated in Phase 1, grouped by area subdirectory, with the IA scope template applied verbatim to the inertia-advocate file.

**Inputs**

| Variable | Source | Register |
|----------|--------|----------|
| T1-AREAS | Phase 1 record block | MUST consume |
| T1-ROLE-COUNT | Phase 1 record block | MUST consume |
| T2-IA-SCOPE-TEMPLATE | Phase 2 record block | MUST consume |
| Phase 3 record block emitted | prerequisite | FORBIDDEN: executing before |

**Task Steps**

1. For every role enumerated in Phase 1, produce a file at `.roles/{area}/{role}.md`.
2. Each file contains exactly five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
3. The `inertia-advocate` file's `scope` field receives the verbatim text of T2-IA-SCOPE-TEMPLATE.
4. Organize files under subdirectories keyed to T1-AREAS.

**Constraints**

- MUST produce exactly T1-ROLE-COUNT files. FORBIDDEN: producing fewer files than T1-ROLE-COUNT.
- MUST include all five fields in every file. FORBIDDEN: omitting any field from any role file.
- MUST organize files under area subdirectories matching T1-AREAS. FORBIDDEN: organizing all files flat under `.roles/` without area subdirectories.
- MUST produce the `inertia-advocate` file. FORBIDDEN: omitting the inertia-advocate role.
- MUST write the verbatim T2-IA-SCOPE-TEMPLATE text into the `scope` field of the inertia-advocate file. FORBIDDEN: paraphrasing, condensing, or rewording that text.
- FORBIDDEN: overwriting any `.roles/` file that already exists at the target path.

**Gate Variables**

| Variable | Type | Description |
|----------|------|-------------|
| T4-FILES-PRODUCED | integer | total role files written |
| T4-AREAS-USED | string-list | area subdirectories created |
| T4-IA-FILE-PATH | path | path to inertia-advocate file |

**Record Block**

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no further phases begin before this block is emitted.
T4-FILES-PRODUCED: [integer]
T4-AREAS-USED: [comma-separated list]
T4-IA-FILE-PATH: [path]
===
```

**Output artifact names**
- `simulations/org-build/{TOPIC}-org-chart-{date}.md`
- `.roles/{area}/{role}.md` — one per enumerated role

---

## V-05 — Combined: Role Sequence (Inventory-as-Table) + Skeleton-Dominant Format

**Hypothesis:** Producing the role set as a typed inventory table in Phase 1 — rather than a prose list — makes the role enumeration a machine-readable gate output rather than a narrative description. Combining this with a skeleton-dominant format (every artifact section rendered as a fill-in template first, then materialized) makes the connection between gate variables and artifact slots visually explicit.

---

### Skill: org-build

Generate a complete organizational structure from a repository or scan output. The role inventory is the primary Phase 1 artifact — a structured table that feeds all downstream phases. Every output section is produced first as a named skeleton with `{{VARIABLE}}` slots, then filled. Outputs: `org-chart.md` and typed `.roles/{area}/{role}.md` files.

**Inputs:** `REPO_PATH`, `DEPTH_FLAG` (`standard` | `deep`), `TOPIC`

---

#### IA Scope Templates (verbatim — copy the matching entry exactly; paraphrase fails)

```
NONE:     "Monitor for first signs of coordination overhead. FORBIDDEN: recommending any
           structural change until a repeating decision bottleneck has been documented
           across three consecutive sprints."

LOW:      "Represent the status quo. Challenge every hierarchy proposal by naming its cost
           in coordination overhead and cognitive load. FORBIDDEN: endorsing any structural
           addition until lightweight ceremony has been tried and documented as insufficient."

MODERATE: "Represent the status quo under acknowledged pressure. Accept ceremony additions.
           FORBIDDEN: endorsing layer additions before a 60-day observable outcome period
           completes."

HIGH:     "Accept a single targeted layer addition in the highest-friction area only.
           FORBIDDEN: endorsing org-wide restructuring. Require a reversibility plan with
           a sunset date before any structural change proceeds."

CRITICAL: "Accept that structure is warranted. Advocate for the minimum viable intervention
           only. FORBIDDEN: endorsing any structural addition without an explicit removal
           criterion and a 12-month sunset review date."
```

---

#### Phase 1 — Role Inventory (Structured Table)

**Task Steps**

1. Read `REPO_PATH`. Identify all functional areas requiring dedicated ownership.
2. Bind T1-DEPTH-FLAG from `DEPTH_FLAG`.
3. Produce a role inventory table with columns: `Title | Area | Level | Primary Function`.
4. Apply the count floor:
   - T1-DEPTH-FLAG = `standard` → 20–30 rows in the inventory table
   - T1-DEPTH-FLAG = `deep` → 50+ rows in the inventory table
5. Include `inertia-advocate` as a row in the inventory table unconditionally.
6. Emit the skeleton for the role inventory before filling it, then fill every slot:
   ```
   [ROLE-INVENTORY-SKELETON]
   | Title | Area | Level | Primary Function |
   | {{ROLE-TITLE}} | {{ROLE-AREA}} | {{ROLE-LEVEL}} | {{ROLE-FUNCTION}} |
   ... (one row per role)
   ```

**Constraints**

- MUST produce the inventory table with 20–30 rows when T1-DEPTH-FLAG = standard. MUST produce 50+ rows when T1-DEPTH-FLAG = deep.
- MUST include an `inertia-advocate` row. FORBIDDEN: omitting inertia-advocate from the inventory table.
- MUST emit the skeleton before the filled table. FORBIDDEN: emitting a filled table without a preceding skeleton.
- FORBIDDEN: enumerating roles not grounded in the scan or repository content.
- FORBIDDEN: beginning Phase 2 before emitting the Phase 1 record block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
T1-ROLE-COUNT: [integer — must equal rows in inventory table]
T1-AREAS: [comma-separated list of unique area values from inventory table]
T1-IA-PRESENT: [YES | NO]
===
```

---

#### Phase 2 — Inertia Assessment

**Input Contract**

- MUST consume T1-DEPTH-FLAG, T1-ROLE-COUNT, T1-AREAS from the Phase 1 record block.
- FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.

**Task Steps**

1. Evaluate the role inventory from Phase 1 for coordination overhead signals: span-of-control violations, repeated escalation paths, siloed expertise clusters.
2. Assign FLAT-CASE-PRESSURE from closed set: `NONE | LOW | MODERATE | HIGH | CRITICAL`.
3. Derive a single verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
4. Copy verbatim IA scope template for the assigned rating.
5. Select anti-pattern categories:
   - CAN-OPERATE-FLAT → cat-2, cat-3
   - STRUCTURE-WARRANTED → cat-1, cat-4
6. Emit the assessment skeleton before filling it:
   ```
   [ASSESSMENT-SKELETON]
   FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
   VERDICT: {{T2-VERDICT}}
   IA-SCOPE: {{T2-IA-SCOPE-TEMPLATE}}
   ANTI-PATTERN-CATS: {{T2-ANTI-PATTERN-CATS}}
   ```

**Constraints**

- MUST assign exactly one verdict. FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. FORBIDDEN: omitting both verdicts.
- MUST copy verbatim template text. FORBIDDEN: paraphrasing or adapting the template text.
- CAN-OPERATE-FLAT: MUST select cat-2, cat-3. FORBIDDEN: selecting cat-1 or cat-4.
- STRUCTURE-WARRANTED: MUST select cat-1, cat-4. FORBIDDEN: selecting cat-2 or cat-3.
- MUST emit the assessment skeleton before the filled assessment. FORBIDDEN: emitting filled values without a preceding skeleton.
- FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-SCOPE-TEMPLATE: [verbatim text — full copy, no abbreviation]
T2-ANTI-PATTERN-CATS: [cat-N, cat-N]
===
```

---

#### Phase 3 — Produce org-chart.md (Skeleton → Fill)

**Input Contract**

- MUST consume T1-AREAS, T1-ROLE-COUNT from the Phase 1 record block.
- MUST consume T2-PRESSURE, T2-VERDICT, T2-IA-SCOPE-TEMPLATE, T2-ANTI-PATTERN-CATS from the Phase 2 record block.
- FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.

**Task Steps**

For each section, emit the skeleton first, then fill it.

**Section 1 — ASCII Hierarchy Diagram**
Skeleton:
```
[HIERARCHY-SKELETON]
+--{{AREA-1}}--+   +--{{AREA-2}}--+
|              |   |              |
... (one box per area from T1-AREAS, at min 2 levels)
```
Fill: produce the completed ASCII diagram.

**Section 2 — Headcount by Area**
Skeleton:
```
[HEADCOUNT-SKELETON]
| Area | Headcount | Key Roles | Decides | Escalates |
| {{AREA}} | {{N}} | {{KEY-ROLES}} | {{DECIDES}} | {{ESCALATES}} |
```
Fill: one row per area from T1-AREAS.

**Section 3 — Operating Rhythm**
Skeleton:
```
[RHYTHM-SKELETON]
| Cadence | Meeting | Owner | Attendees | Output |
| {{CADENCE}} | {{MEETING}} | {{OWNER}} | {{ATTENDEES}} | {{OUTPUT}} |
```
Fill: ROB row, shiproom row, at least one governance row (3+ rows total). Each governance meeting appended with a charter: Name, Purpose, Frequency, Quorum (N of M), Output.

**Section 4 — Inertia Assessment**
Skeleton:
```
[INERTIA-SKELETON]
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
{{T2-VERDICT}}
Only one verdict. Both is an error. Neither is an error.
{{T2-IA-SCOPE-TEMPLATE}}
```
Fill: substitute all slots with values from Phase 2 record block.

**Section 5 — Anti-Pattern Watch**
Skeleton:
```
[ANTI-PATTERN-SKELETON]
| Anti-Pattern | Category | Why It Applies Here | Mitigation |
| {{PATTERN-NAME}} | {{T2-ANTI-PATTERN-CATS[N]}} | {{ELEMENT}} ({{CAT-N}}) — {{EXPLANATION}} | {{REMEDIATION-ACTION}} |
```
Fill: one row per anti-pattern, using only categories from T2-ANTI-PATTERN-CATS.

**Section 6 — Org Evolution Roadmap**
Skeleton:
```
[ROADMAP-SKELETON]
| Trigger | Category | Structural Response |
| {{HEADCOUNT-THRESHOLD}} | headcount | {{RESPONSE}} |
| {{NON-HEADCOUNT-TRIGGER}} | {{DIFFERENT-CATEGORY}} | {{RESPONSE}} |
```
Fill: Row 1 headcount threshold, Row 2 different trigger category.

**Constraints**

- MUST emit each section's skeleton before its filled version. FORBIDDEN: emitting filled sections without a preceding skeleton.
- MUST produce all six sections.
- FORBIDDEN: including anti-pattern categories absent from T2-ANTI-PATTERN-CATS.
- MUST open every "Why It Applies Here" cell with `[element name] (cat-N) —`. FORBIDDEN: opening that cell without that prefix.
- FORBIDDEN: placing format guidance in Mitigation cells. MUST place a specific remediation action in each Mitigation cell.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED in Section 4. FORBIDDEN: omitting both verdicts in Section 4.
- MUST fill all `{{VARIABLE}}` slots with values traceable to named gate variables. FORBIDDEN: leaving any `{{VARIABLE}}` slot unfilled in the output.
- FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-SECTIONS-PRODUCED: [comma-separated section names]
T3-ANTI-PATTERN-ROWS: [integer]
T3-RHYTHM-ROWS: [integer]
T3-SKELETONS-EMITTED: [integer — must equal T3-SECTIONS-PRODUCED count]
===
```

---

#### Phase 4 — Produce .roles/ Files (Skeleton → Fill)

**Input Contract**

- MUST consume T1-AREAS, T1-ROLE-COUNT from the Phase 1 record block.
- MUST consume T2-IA-SCOPE-TEMPLATE from the Phase 2 record block.
- FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.

**Task Steps**

1. Emit the role file skeleton once before producing any files:
   ```
   [ROLE-FILE-SKELETON]
   orientation: {{ORIENTATION}}
   lens: {{LENS}}
   expertise: {{EXPERTISE}}
   scope: {{SCOPE}}
   collaborates_with: {{COLLABORATES-WITH}}
   ```
2. For every role in the Phase 1 inventory table, produce `.roles/{area}/{role}.md` by filling the skeleton.
3. The `inertia-advocate` `scope` field = verbatim text from T2-IA-SCOPE-TEMPLATE (substitute into `{{SCOPE}}` slot).
4. Group files under area subdirectories matching T1-AREAS.

**Constraints**

- MUST emit the role file skeleton before producing any role files. FORBIDDEN: producing role files without a preceding skeleton emission.
- MUST produce exactly T1-ROLE-COUNT files. FORBIDDEN: producing fewer files than T1-ROLE-COUNT.
- MUST include all five fields in every file. FORBIDDEN: omitting any field from any role file.
- MUST group files under area subdirectories. FORBIDDEN: placing all files flat with no area subdirectory structure.
- MUST produce the inertia-advocate file. FORBIDDEN: omitting inertia-advocate.
- MUST fill the `inertia-advocate` `scope` slot with the verbatim T2-IA-SCOPE-TEMPLATE text. FORBIDDEN: paraphrasing or adapting that text.
- FORBIDDEN: overwriting any `.roles/` file that already exists at the target path.

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: no further phases begin before this block is emitted.
T4-FILES-PRODUCED: [integer]
T4-AREAS-USED: [comma-separated list]
T4-IA-FILE-PATH: [path]
T4-SKELETON-EMITTED: [YES | NO]
===
```

**Output artifact names**
- `simulations/org-build/{TOPIC}-org-chart-{date}.md`
- `.roles/{area}/{role}.md` — one per enumerated role

---

## Variation Summary

| # | Axis | Key Structural Bet | Primary C-30 Mechanism | IA Timing |
|---|------|--------------------|------------------------|-----------|
| V-01 | Role Sequence (Roles-First) | Full role set before verdict → grounded IA | Task/Constraints prose subsections | Phase 2 |
| V-02 | Output Format (Table-Heavy) | Constraint table with Register column → scannable audit | Constraint table rows structurally separate from task prose | Phase 2 |
| V-03 | Inertia Framing (IA-Primary) | Verdict first → roles shaped by structural decision | Task/Constraints prose subsections | Phase 1 |
| V-04 | Lifecycle + Formal Register | Symmetric phase template → uniform constraint coverage | Purpose/Inputs/Task Steps/Constraints/Gate Variables/Record Block per phase | Phase 2 |
| V-05 | Role Inventory + Skeleton-Dominant | Skeleton-before-fill → {{VARIABLE}} slots trace gate outputs | Skeleton emission as structural phase separator | Phase 2 |
