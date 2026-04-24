## scout-inertia — V-01 / V-02 Scoring (R6 Rubric)

---

### V-01 — Role Sequence

#### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Workaround named specifically | **PASS** | Step 2 explicitly rejects "a manual process," enforces exact mechanism + unit format string |
| C-02 | Switching cost quantified | **PASS** | Step 3 requires ≥2 categories, unit enforcement, explicit format: "[role] spends [N] [unit]" |
| C-03 | Inertia threat score declared | **PASS** | Step 6 declares score with format, default HIGH, deviation requires quantified justification |
| C-04 | Defeat conditions identified | **PASS** | DC-[N] format requires team type + falsifiable condition + connected FM number |
| C-05 | Workaround failure modes identified | **PASS** | FM-[N] format with observable signal field; "manual is slow" explicitly fails |

#### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| R-01 | Trigger scoped to team type | **PASS** | DC format requires "Name a specific team type (not 'users')" |
| R-02 | Role-level precision | **PASS** | Role Registry in Step 1 prohibits department/group labels at declaration time |
| R-03 | At least one cost cited to role | **PASS** | Step 3 explicitly requires ≥1 cost tied to a registry role |

#### Advanced Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| A-08 | FM numbers precede defeat conditions | **PASS** | Step 4 (FM-[N] assignment) comes before Step 5 (DC-[N] writing); structural ordering enforced |
| A-10 | C-05 structurally first (fail-first) | **FAIL** | C-05 is Step 4 of 6; Steps 1–3 (roles, workaround map, costs) precede it — inertia armor not named before costs quantified |
| A-11 | Question-per-criterion mapping | **PARTIAL** | Six steps implicitly cover each criterion but are not labeled as per-criterion prompts; an unanswered step is a missing section, not a visible blank |
| A-12 | BRIDGE dual-closure | **FAIL** | No bridge markers; no named Q3/Q4 artifact closing FM→actor and FM→trigger chains |

**V-01 Score: ~77 / 115**
All essential: PASS | All recommended: PASS | A-08: PASS | A-10/A-12: FAIL

---

### V-02 — Output Format (Tables + Numbered Inventory)

#### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Workaround named specifically | **PASS** | Table 1 rejects blank cells; "exact mechanism, not 'manual process'" enforced in column schema |
| C-02 | Switching cost quantified | **PASS** | Table 3 requires Unit and Role columns; ≥2 rows; blank Unit cell = visibly failed criterion |
| C-03 | Inertia threat score declared | **PASS** | THREAT SCORE DECLARATION section with explicit format; default HIGH, downgrade requires quantified cite |
| C-04 | Defeat conditions identified | **PASS** | Table 4 has Team type + falsifiable condition + Connected FM# columns; blank cell structurally visible |
| C-05 | Workaround failure modes identified | **PASS** | Table 2 with FM# + Trigger condition + Consequence + Role columns; "manual is slow" explicitly excluded |

#### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| R-01 | Trigger scoped to team type | **PASS** | Table 4 has dedicated "Team type" column — cannot be omitted without a blank cell |
| R-02 | Role-level precision | **PASS** | Table 1 "Performer role" annotated "[role label, not department]"; Table 4 role tracking required |
| R-03 | At least one cost cited to role | **PASS** | Table 3 "Role" column; prompt states "at least one row must name a specific role" |

#### Advanced Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| A-08 | FM numbers precede defeat conditions | **PASS** | Table 2 (FM inventory with FM-01, FM-02) precedes Table 4 (defeat conditions); FM# is assigned before DC# is written — structurally guaranteed by table ordering |
| A-10 | C-05 structurally first (fail-first) | **PARTIAL** | Table 2 (failure modes = C-05) is section 2 of 5, after Table 1 (workaround profile). Failure modes precede costs and defeat conditions, but not the entire output — Table 1 comes first |
| A-11 | Question-per-criterion mapping | **PARTIAL** | Completeness check at the end maps each criterion to a binary checkbox; this is post-hoc verification, not per-criterion prompts embedded in the template. Unanswered criterion = unchecked box, which is more visible than V-01's missing step but still a trailing check, not a structural upfront prompt |
| A-12 | BRIDGE dual-closure | **FAIL** | No bridge markers, no named Q3/Q4 artifact; dual-closure absent |

**V-02 Score: ~82 / 115**
All essential: PASS | All recommended: PASS | A-08: PASS | A-10: PARTIAL | A-12: FAIL

---

### Ranking

| Rank | Variation | Score | Essential | Rec. | A-08 | A-10 | A-11 | A-12 |
|------|-----------|-------|-----------|------|------|------|------|------|
| 1 | V-02 | ~82 | PASS | PASS | PASS | PARTIAL | PARTIAL | FAIL |
| 2 | V-01 | ~77 | PASS | PASS | PASS | FAIL | PARTIAL | FAIL |

---

### Excellence Signals — V-02

1. **Tabular column schema makes criterion gaps structurally visible as blank cells** — where V-01 prose steps allow a partial sentence to satisfy a criterion, a blank table cell is immediately visible to author and reviewer without a full read.

2. **FM# pre-assignment in a dedicated table before defeat conditions are written** — Table 2 appearing before Table 4 structurally enforces A-08 (fail-first number → defeat condition connection) without relying on author discipline; the numbered inventory exists before DC-[N] can reference it.

3. **Trailing completeness checklist converts each essential criterion to a binary observable** — the five checkboxes at the end mirror the five essential criteria; an unchecked box names the specific gap rather than requiring full-output review to detect it.

---

### R6 Gap Note

Neither variation implements A-12 (BRIDGE dual-closure). The R6 target combination — A-08 (FM pre-numbering) + A-12 (named bridge artifacts closing FM→actor and FM→trigger) — is half-present in V-02 (A-08 satisfied structurally) but A-12 remains unimplemented across both. A V-03 that adds explicit BRIDGE section markers after Table 2 would close this gap.

---

```json
{"top_score": 82, "all_essential_pass": true, "new_patterns": ["Tabular column schema makes missing criterion data structurally visible as blank cells rather than detectable only on full prose read", "FM# pre-assignment in a numbered inventory table before defeat condition table enforces A-08 structurally without author discipline", "Trailing completeness checklist maps each essential criterion to a named binary checkbox, converting content gaps into visible unchecked items"]}
```
