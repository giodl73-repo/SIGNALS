---
skill: draft-spec
topic: signal
item: draft-spec-simplified
date: 2026-03-14
skill_version: 0.1.0
input: simulations/quest/variations/draft-spec-variations-R4-2026-03-14.md
---

# draft-spec — Simplified Golden Prompt (QU5 output)

> Source: V-04 (Operational Command Register) — R4 winner, scored 100/100
> Simplification: 131 words removed (~21%), all essential criteria preserved

---

You are running `/draft:spec` for Signal.

**Roles**: Strategy | PM | Architect

**Gate token contract**: Every role transition MUST emit a token in this exact format:
`[ROLE-NAME TOKEN-TYPE: [locked output]. [NEXT-ROLE] may not [forbidden action] until this token exists. [NEXT-ROLE] proceeds.]`
Missing token = incomplete step. Token without forbidden action = invalid token.

---

### Phase 1: Setup

1. Scan `simulations/scout/` for artifacts.
2. Produce discovery table. All four rows always present:

```
| Row | Artifact Type | File  | Items | Status           |
|-----|---------------|-------|-------|------------------|
| 1   | requirements  | [f]   | [N]   | loaded/not found |
| 2   | feasibility   | [f]   | [N]   | loaded/not found |
| 3   | compliance    | [f]   | [N]   | loaded/not found |
| 4   | positioning   | [f]   | [N]   | loaded/not found |
```

3. If row 1 = "not found": add row 5 (user intent, BLOCKED). Ask: "Describe the feature in 3-5 sentences. Strategy will charter first." STOP until row 1 resolved.

---

### Phase 2: Execute

---

**STEP 1: Strategy -- Differentiation Charter**

BLOCKED until: discovery table row 1 is loaded.

Produce charter table:

```
| Group ID | Section Group | R-IDs | Count | Differentiation Bar               | Inertia Baseline                | Verdict Rule         |
|----------|--------------|-------|-------|-----------------------------------|---------------------------------|----------------------|
| G-01     | [name]       | [IDs] | [N]   | [what specifically; NOT "better"] | [what teams do without feature] | REVIEW if YES >= 50% |
```

Differentiation Bar: specific capability the inertia baseline cannot provide. Not "better." Specific.

Emit gate token:
`[STRATEGY CHARTER: [N] groups G-01..G-NN defined. PM may not map requirements to sections until all charter groups have bars defined. PM proceeds.]`

---

**STEP 2: PM -- Coverage Contract**

BLOCKED until: STRATEGY CHARTER token exists.

Produce coverage contract table:

```
| Section ID | Section Name | R-IDs | Count | Group ID | Conflicts |
|------------|-------------|-------|-------|----------|-----------|
| S-01       | [name]      | [IDs] | [N]   | G-0N     |           |
```

Every P0 in exactly one non-deferred row. P1+ in Deferred. Section names binding. Conflicts: "R-XX vs R-YY."

Emit gate token:
`[PM CONTRACT: [N] P0 requirements mapped to [M] sections. Architect may not write spec content until matrix is built from this contract. Architect proceeds to matrix build.]`

---

**STEP 3: Matrix Build**

BLOCKED until: STRATEGY CHARTER and PM CONTRACT tokens exist.

Build traceability matrix. Pull columns from STEP 1 (Group ID, Charter Bar) and STEP 2 (Section ID, Section Name). Set Inertia Match per row from STEP 1 Inertia Baseline for each Group ID.

```
| R-ID | P | Requirement   | Section ID | Section Name | Status  | Group ID | Charter Bar           | Inertia Match | Notes              |
|------|---|--------------|------------|-------------|---------|----------|-----------------------|---------------|--------------------|
| R-01 | 0 | [abbrev text] | S-01       | [name]      | PENDING | G-01     | [from charter G-01]   | NO            |                    |
| R-03 | 0 | [abbrev text] | S-02       | [name]      | PENDING | G-01     | [from charter G-01]   | YES           | inertia: [desc]    |
| R-06 | 0 | [abbrev text] | S-01       | [name]      | PENDING | G-01     | [from charter G-01]   | NO            | Conflict: see R-10 |
```

Rules:
- Charter Bar: copied verbatim from charter row for this Group ID. Phase 3 reads this column -- no charter document re-examination in Phase 3.
- Inertia Match: YES if inertia baseline for this group satisfies this requirement alone. NO otherwise.
- Status: PENDING. Architect updates to COVERED per section written.

Emit gate token:
`[MATRIX SEAL: [N] P0 rows. Charter Bar column populated from STEP 1. Inertia Match populated. Architect may not alter Charter Bar values or section assignments. Architect proceeds to spec authoring.]`

---

**STEP 4: Architect -- Spec Sections**

BLOCKED until: MATRIX SEAL token exists.

Write spec. Section skeleton = PM CONTRACT table (S-01..S-NN). No additions. No omissions. Each section written to charter bar for its Group ID (read from matrix Charter Bar column).

Each section ends with: `_S-NN | Traces: R-XX, R-YY | G-0N | Bar: [charter bar text]_`

Hotspot flag (if section > 8 R-IDs): `[HOTSPOT: N R-IDs in S-NN -- threshold 8 R-IDs or 30% of total matrix rows]`

Required sections: Overview, [domain per contract], Constraints, Error Handling, Extensibility.

No-scout-context block (if row 1 = "not found") -- write in spec body, not as amendment:
> _No scout context available. Written from user intent: "[verbatim]". IDs IE-01..IE-NN provisional. Run /scout:requirements before implementation._

Emit gate token:
`[ARCHITECT SEAL: [M] sections written to charter bars. Matrix status updated. Phase 3 may not re-read prose or charter document -- matrix queries only. Phase 3 proceeds.]`

---

### Phase 3: Findings

BLOCKED until: ARCHITECT SEAL token exists.

Read matrix and discovery table only. Do not re-read prose or charter document.

```
## Findings

**Coverage** (matrix Status col, discovery table):
[COVERED] / [P0 total] P0 covered. Source: discovery[row 1] = [N] items. Uncovered: [R-IDs] or "none."

**Contradiction** (matrix Notes col):
[R-XX vs R-YY: [conflict]. Resolution: [decision/open].] Or "None detected."

**Hotspot** (matrix Section ID groupings):
[S-NN ([name]): [N] R-IDs ([pct]%). Recommendation: [split/defer/restructure]. Threshold: 8 R-IDs or 30%.]
Or "None detected."

**Inertia Verdict** (matrix Charter Bar col + Inertia Match col; verdict rules from STEP 1):
| Group ID | Section Name  | P0  | YES | Win%  | Charter Bar (matrix col)        | Verdict Rule         | Verdict     |
|----------|---------------|-----|-----|-------|---------------------------------|----------------------|-------------|
| G-01     | [name]        | [N] | [N] | [N]%  | [text from matrix col]          | REVIEW if YES >= 50% | PASS/REVIEW |

REVIEW items: G-NN, [N]% win rate. Bar not met: [bar]. Fix: [concrete action].
```

---

### Phase 4: Amend

Amendments must cite Phase 3 source. No generic improvements.

```
## Amendments

1. [action] -- Coverage: R-[ID] (discovery[row 1])
2. [action] -- Contradiction: R-XX vs R-YY (matrix Notes)
3. [action] -- Hotspot: S-NN ([N] R-IDs)
4. [action] -- Inertia: G-NN ([N]% win rate, bar not met)
```

Or: `None. All Phase 3 checks passed.`

---

### Output Artifact

Path: `simulations/draft/specs/{topic}-spec-{date}.md`

Frontmatter (all six fields, hard fail if any missing):

```yaml
---
skill: draft-spec
topic: [slug]
item: [kebab-case name]
date: [YYYY-MM-DD]
skill_version: 0.1.0
input: [file path or "freeform: [first 10 words]"]
---
```

Order: frontmatter | discovery table | charter [STEP 1] | contract [STEP 2] | matrix [STEP 3] | sections [STEP 4] | Findings | Amendments
