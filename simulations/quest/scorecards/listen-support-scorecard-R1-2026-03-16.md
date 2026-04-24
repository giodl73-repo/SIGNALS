## listen-support Round 1 Scorecard (v1 Rubric)

**Evaluation mode:** Prompt-design scoring — no trace output available (placeholder). Each criterion assessed against the structural guarantees present in the prompt design.

**Scoring convention:** PARTIAL treated as FAIL in composite calculation (conservative).

---

### V-01 — Imperative/Technical Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Field completeness | **PASS** | SECTION 1 names all 6 fields explicitly; "No exceptions" |
| C-02 | Vocabulary validity | **PASS** | Exact token lists per field; explicit prohibition of "P2/P3", "medium-high" variants |
| C-03 | First-person voice | **PARTIAL** | Prohibition list covers "the SRE / they / their" but misses "I, as the SRE" appositive pattern; no activation block to force inhabitation |
| C-04 | Gap analysis three-axis | **PASS** | SECTION 6 requires all three sections with ≥1 entry each |
| C-05 | Min ticket count | **PASS** | "Generate at least 7 tickets" |
| C-06 | Phase distribution | **PARTIAL** | Constraints stated in SECTION 4 bullet list but no verification gate; model may not self-check |
| C-07 | Phase-severity alignment | **PARTIAL** | Phase severity rules stated as constraints; no post-generation check forces compliance |
| C-08 | Role diversity | **PASS** | SECTION 5 coverage check with explicit PASS/FAIL and add-if-fail instruction |
| C-09 | Inertia competitor grounding | **FAIL** | No prior tool anchor anywhere in prompt |
| C-10 | Pre-commitment table | **FAIL** | No table before bodies |

**Essential pass: 4/5** (C-03 fails) | **Recommended: 1/3** (C-08) | **Aspirational: 0/2**

```
Composite = (4/5 × 60) + (1/3 × 30) + 0 = 48 + 10 = 58
Golden: NO — C-03 essential failure
```

---

### V-02 — Performance/Conversational Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Field completeness | **PASS** | Ticket format in STEP 3 lists all 6 fields |
| C-02 | Vocabulary validity | **PASS** | Pipe-separated valid token lists for all fields |
| C-03 | First-person voice | **PASS** | Activation block ("I AM / MY SITUATION / MY FRUSTRATION") forces inhabitation; STEP 3 body instruction: "no 'I, as the SRE'... just I" explicitly closes the appositive gap V-01 missed |
| C-04 | Gap analysis three-axis | **PASS** | STEP 6 requires all three sections with ≥1 entry each |
| C-05 | Min ticket count | **PASS** | "Write at least 7 tickets" |
| C-06 | Phase distribution | **PARTIAL** | Phase constraints stated in STEP 4 but no distribution verification gate; STEP 5 checks roles only |
| C-07 | Phase-severity alignment | **PARTIAL** | Adoption-curve severity guidance present in STEP 4; no severity alignment check gate |
| C-08 | Role diversity | **PASS** | STEP 5 checks distinct roles ≥3; add-if-fail instruction present |
| C-09 | Inertia competitor grounding | **FAIL** | STEP 1 asks about prior tool but doesn't lock a named tool as anchor; body reference not structurally required |
| C-10 | Pre-commitment table | **FAIL** | No table before bodies |

**Essential pass: 5/5** | **Recommended: 1/3** (C-08 only; C-06 and C-07 PARTIAL→FAIL) | **Aspirational: 0/2**

```
Composite = (5/5 × 60) + (1/3 × 30) + 0 = 60 + 10 = 70
Golden: NO — composite 70 < 80 threshold
```

---

### V-03 — Inertia Framing (Front-Loaded Competitor)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Field completeness | **PASS** | STEP 3 format includes all 6 fields plus Phase |
| C-02 | Vocabulary validity | **PASS** | Pipe-separated valid values for all fields |
| C-03 | First-person voice | **PASS** | "Write in first person — 'I'. No role titles in third person. Every action taken by 'I'" |
| C-04 | Gap analysis three-axis | **PASS** | STEP 5 requires all three sections with ≥1 entry each |
| C-05 | Min ticket count | **PASS** | "Predict at least 7 support tickets" |
| C-06 | Phase distribution | **PASS** | STEP 2 establishes transition curve with all 3 phases; STEP 3 constraints require ≥2 Phase 1, ≥1 Phase 3; STEP 4 check fires before gap analysis |
| C-07 | Phase-severity alignment | **PASS** | Severity inference explicitly tied to PRIOR TOOL availability: "Phase 1 → P2/P3 (fallback to [PRIOR TOOL] available)"; "Phase 3 → P0/P1 (no fallback)"; per-ticket severity check in STEP 3 |
| C-08 | Role diversity | **PASS** | STEP 4 role coverage check with PASS/FAIL; add-if-fail |
| C-09 | Inertia competitor grounding | **PASS** | STEP 1 declares PRIOR TOOL (must be real named tool); STEP 3 requires at least one body to name it by exact name; STEP 4 explicitly verifies "[PRIOR TOOL] named in body: [T-NN list]" |
| C-10 | Pre-commitment table | **FAIL** | No pre-commitment table; metadata decided at body-writing time |

**Essential pass: 5/5** | **Recommended: 3/3** | **Aspirational: 1/2** (C-09 PASS, C-10 FAIL)

```
Composite = (5/5 × 60) + (3/3 × 30) + (1/2 × 10) = 60 + 30 + 5 = 95
Golden: YES ✓
```

---

### V-04 — Performance + Inertia (V-02 + V-03 Combined)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Field completeness | **PASS** | STEP 3 ticket format includes all 6 fields |
| C-02 | Vocabulary validity | **PASS** | Pipe-separated valid values with explicit Phase field |
| C-03 | First-person voice | **PASS** | Activation block present; body instruction: "no 'I, as the SRE', no 'I (the PM)', just I" closes appositive pattern |
| C-04 | Gap analysis three-axis | **PASS** | STEP 5 requires all three sections |
| C-05 | Min ticket count | **PASS** | "Write at least 7 tickets" |
| C-06 | Phase distribution | **PASS** | STEP 1 transition timeline establishes all 3 phases; STEP 3 constraints: ≥2 Phase 1 (P2/P3), ≥1 Phase 3 (P0/P1); STEP 4 checks Phase 1 and Phase 3 counts with PASS/FAIL |
| C-07 | Phase-severity alignment | **PASS** | STEP 1 severity inference: "I'm frustrated but I can switch back to [PRIOR TOOL]" (Phase 1 P2/P3); "I'm blocked and [PRIOR TOOL] is no longer an option" (Phase 3 P0/P1); constraints in STEP 3 enforce both directions; activation MY ADOPTION WINDOW ties persona to phase before body is written |
| C-08 | Role diversity | **PASS** | STEP 4 coverage check: "Distinct personas: [N], required: >= 3 → PASS / FAIL" |
| C-09 | Inertia competitor grounding | **PASS** | PRIOR TOOL declared in STEP 1; MY FRUSTRATION in activation specifically frames what "[PRIOR TOOL] did that this doesn't"; STEP 4 verifies "[PRIOR TOOL] named in body" |
| C-10 | Pre-commitment table | **FAIL** | No pre-commitment table; metadata assigned per-ticket during body generation |

**Essential pass: 5/5** | **Recommended: 3/3** | **Aspirational: 1/2** (C-09 PASS, C-10 FAIL)

```
Composite = (5/5 × 60) + (3/3 × 30) + (1/2 × 10) = 60 + 30 + 5 = 95
Golden: YES ✓
```

---

### V-05 — Full Synthesis (Performance + Inertia + Pre-Commitment Table)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Field completeness | **PASS** | STEP 3 table requires all 6 fields + Phase per row; TABLE CHECK verifies before any body is written |
| C-02 | Vocabulary validity | **PASS** | Explicit allowed-values block in STEP 3; TABLE CHECK enforces at gate |
| C-03 | First-person voice | **PASS** | STEP 4 activation block with 4 fields (including MY TRANSITION STATE); STEP 5 instruction: "no role title anywhere in the body. Just I"; STEP 6 post-body check: "All bodies written in first person" |
| C-04 | Gap analysis three-axis | **PASS** | STEP 7 requires all three sections with ≥1 named artifact each |
| C-05 | Min ticket count | **PASS** | STEP 3 table requires ≥7 rows; TABLE CHECK: "Total rows: [N] (required: >= 7) → PASS / FAIL" |
| C-06 | Phase distribution | **PASS** | TABLE CHECK: "Phase 1 rows: [N] (required: >= 2) → PASS / FAIL"; "Phase 3 rows: [N] (required: >= 1) → PASS / FAIL" — enforced before prose begins |
| C-07 | Phase-severity alignment | **PASS** | TABLE CHECK: "Phase 1 severities: [list] — all must be P2 or P3 → PASS / FAIL"; "Phase 3 severities: [list] — all must be P0 or P1 → PASS / FAIL" — strongest possible structural guarantee |
| C-08 | Role diversity | **PASS** | TABLE CHECK: "Distinct Persona values: [N] (required: >= 3) → PASS / FAIL" enforced pre-body |
| C-09 | Inertia competitor grounding | **PASS** | PRIOR TOOL declared in STEP 1; MY FRUSTRATION in STEP 4 activation frames tool-specific friction; STEP 5 body instruction requires naming by exact name; STEP 6 verifies "[PRIOR TOOL] named in at least one body" |
| C-10 | Pre-commitment table | **PASS** | STEP 3 is the pre-commitment table; TABLE CHECK gate prevents forward progress on any FAIL; STEP 6 verifies "All body field values match Step 3 table" |

**Essential pass: 5/5** | **Recommended: 3/3** | **Aspirational: 2/2**

```
Composite = (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 60 + 30 + 10 = 100
Golden: YES ✓
```

---

## Rankings

| Rank | Variation | Composite | Golden | Gap to prior |
|------|-----------|-----------|--------|--------------|
| 1 | **V-05** | **100** | YES | +5 over V-03/V-04 |
| 2 | **V-03** | **95** | YES | — |
| 2 | **V-04** | **95** | YES | — |
| 4 | V-02 | 70 | NO | −25 vs V-03 |
| 5 | V-01 | 58 | NO | −12 vs V-02 |

---

## Excellence Signals from V-05

**Signal 1 — Taxonomy-prose split (C-10 → C-06/C-07 cascade)**
The pre-commitment table separates two fundamentally different cognitive tasks: taxonomy decisions (what tickets exist, what their metadata is) and prose execution (writing the bodies). Every structural constraint — count, category diversity, phase distribution, severity alignment — is enforced at the table gate before a single body is written. This means distribution errors are caught and corrected at low cost, before they're embedded in prose.

**Signal 2 — TABLE CHECK as blocking gate**
V-01 and V-02 state constraints as bullet lists ("At least 2 Phase 1 tickets"). V-05 structures them as a TABLE CHECK block with per-row PASS/FAIL and explicit "do not proceed with a FAIL" instruction. A stated constraint invites drift; a blocking gate structurally prevents it. C-06 and C-07 improved from PARTIAL in V-01/V-02 to PASS in V-05 solely because of this mechanism — not because new information was added, but because enforcement was restructured.

**Signal 3 — MY TRANSITION STATE in the activation block**
V-04's activation block has three fields (I AM / MY SITUATION / MY FRUSTRATION). V-05 adds a fourth: MY TRANSITION STATE — "am I still running [PRIOR TOOL] in parallel, or am I fully committed?" This field connects the PRIOR TOOL anchor from STEP 1 to the individual persona before the body is written, ensuring the inertia context is active in the model's working register when generating prose. The transition state field also directly supports C-07 severity reasoning: a persona still running PRIOR TOOL in parallel is naturally P2/P3.

**Signal 4 — Two-checkpoint verification**
V-05 applies verification at two points: STEP 3 TABLE CHECK (before prose) and STEP 6 POST-BODY CHECK (after prose). The pre-body check catches distribution and vocabulary errors. The post-body check catches first-person drift and table divergence that escaped the pre-commitment gate. No other variation has a post-body verification step. This two-checkpoint pattern is the mechanism that makes C-10 a true guarantee rather than a best-effort constraint.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["taxonomy-prose split: pre-commitment table enforces all structural constraints before prose execution, preventing distribution and severity errors from being embedded in bodies", "TABLE CHECK blocking gate: each constraint expressed as PASS/FAIL with explicit do-not-proceed-on-fail instruction, converting stated aspirations into structural guarantees", "MY TRANSITION STATE activation field: fourth activation block field connects the PRIOR TOOL anchor to individual persona voice before body is written, directly supporting both C-09 grounding and C-07 severity reasoning", "two-checkpoint verification: TABLE CHECK pre-body + POST-BODY CHECK after prose catches first-person drift and table divergence that the pre-commitment gate cannot prevent"]}
```
