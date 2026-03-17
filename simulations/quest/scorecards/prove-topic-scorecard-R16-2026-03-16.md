## prove-topic — Quest Score Round 16 (rubric v14)

**Date**: 2026-03-16 | **Rubric**: v14 | **Anchor**: R15 V-05

---

### Scoring Reference

**Formula**:
```
composite = (essential_pass / 5 × 60)
          + (recommended_pass / 3 × 30)
          + (aspirational_pass / 2 × 10)
```

**Criteria map**:

| # | Criterion | Weight |
|---|-----------|--------|
| C-01 | All five stages orchestrated in correct sequence | Essential |
| C-02 | Scout artifact loaded and named before hypothesis | Essential |
| C-03 | Progressive artifact writes — one per stage | Essential |
| C-04 | Synthesis fields (verdict + displacement) structurally gated before synthesis_complete | Essential |
| C-05 | Counter-hypothesis resolved with typed verdict before synthesis verdict | Essential |
| C-06 | Structured evidence tables at all evidence stages | Recommended |
| C-07 | Displacement/inertia framing with per-stage displacement checks | Recommended |
| C-08 | Lifecycle gates: entry conditions + named exit signals at all boundaries | Recommended |
| C-09 | Numerical confidence scoring (1-10 scale with calculation) | Aspirational |
| C-10 | Aggregate displacement verdict at Stage 4 | Aspirational |

---

### V-01 — Session Invariants

**Axis**: Four fields declared read-only in SESSION INVARIANTS block (SI-01 through SI-04). Stages reference by field name only, never re-infer.

| Criterion | Result | Evidence Note |
|-----------|--------|---------------|
| C-01 | PASS | Header declares correct sequence; all five stage headers present in order |
| C-02 | PASS | SI-03 scout_artifact locked in SESSION INVARIANTS before Stage 1; Stage 1 entry condition explicitly references "SI-03 — do not re-infer" |
| C-03 | PASS | Each stage has a distinct WRITE + confirm + EXIT SIGNAL; five separate artifacts |
| C-04 | PARTIAL | Stage 5 has `displacement_case` with "Explicit answer required" but no structural gate (no DUAL-LOCK checklist) before synthesis_complete fires |
| C-05 | PARTIAL | Stage 5 entry condition lists "counter_hypothesis available" but no two-block structure with typed resolution_verdict; Stage 4 has s4_counter_evidence but no Stage 5 BLOCK 1 gate |
| C-06 | PASS | Evidence tables present in Stages 2, 3, 4 with multiple rated columns |
| C-07 | PASS | SI-04 status_quo_comparator; per-stage s2_displacement_read + s3_displacement_read fields; displacement_case in Stage 5 |
| C-08 | PASS | PRE-CHECK with invariants_locked exit; all stages have ENTRY CONDITIONS + EXIT SIGNAL |
| C-09 | FAIL | confidence_prior / confidence_final are Low/Med/High only; no 1-10 numerical scale |
| C-10 | PARTIAL | Per-stage displacement reads but no s4_aggregate_displacement_verdict in Stage 4 |

**Scores**: essential 3/5 | recommended 3/3 | aspirational 0/2
**Composite**: (3/5 × 60) + (3/3 × 30) + (0/2 × 10) = 36 + 30 + 0 = **66**
**All essential pass**: No (C-04 PARTIAL, C-05 PARTIAL)

---

### V-02 — Atomic Dual-Lock

**Axis**: Stage 5 requires `hypothesis_verdict [LOCKED]` AND `displacement_conclusion [LOCKED]` before synthesis_complete fires via DUAL-LOCK GATE checklist.

| Criterion | Result | Evidence Note |
|-----------|--------|---------------|
| C-01 | PASS | Correct five-stage sequence stated in header and enforced via stage headers |
| C-02 | PASS | CAMPAIGN OPEN declares scout_artifact; Stage 1 copies "from CAMPAIGN OPEN, not re-inferred"; scout not found halts campaign |
| C-03 | PASS | Five WRITE + confirm instructions, one per stage, each confirmed before EXIT |
| C-04 | PASS | DUAL-LOCK GATE: checklist requires `hypothesis_verdict [LOCKED]` AND `displacement_conclusion [LOCKED]`; "If either absent or not marked [LOCKED]: set it before proceeding" — structural enforcement |
| C-05 | PARTIAL | Stage 5 entry condition lists "counter_hypothesis from Stage 1 available" but no BLOCK 1 two-step; DUAL-LOCK only checks verdict and displacement_conclusion, not resolution_verdict |
| C-06 | PASS | Evidence tables in Stages 2, 3, 4 (ITEM\|SOURCE\|SUMMARY\|SUPPORT\|STRENGTH) |
| C-07 | PARTIAL | status_quo_comparator in CAMPAIGN OPEN; displacement_conclusion [LOCKED] in Stage 5; but no per-stage displacement_read fields through evidence stages |
| C-08 | PASS | ENTRY CONDITIONS + EXIT signals at all stage boundaries |
| C-09 | FAIL | Low/Med/High only |
| C-10 | FAIL | No s4_aggregate_displacement_verdict; Stage 4 closes with s4_primary_finding |

**Scores**: essential 4/5 | recommended 2/3 | aspirational 0/2
**Composite**: (4/5 × 60) + (2/3 × 30) + (0/2 × 10) = 48 + 20 + 0 = **68**
**All essential pass**: No (C-05 PARTIAL → FAIL)

---

### V-03 — Counter-Hypothesis Resolution Block

**Axis**: Stage 5 split into BLOCK 1 (resolve counter_hypothesis → typed resolution_verdict) + BLOCK 2 (synthesis verdict, gated on BLOCK 1 exit).

| Criterion | Result | Evidence Note |
|-----------|--------|---------------|
| C-01 | PASS | Correct five-stage sequence; all stage headers present in order |
| C-02 | PASS | CAMPAIGN OPEN declares scout_artifact; Stage 1: "copied from CAMPAIGN OPEN, not re-inferred" |
| C-03 | PASS | Five WRITE instructions, one per stage, each confirmed before EXIT |
| C-04 | PARTIAL | Stage 5 BLOCK 2 has `hypothesis_verdict` + `displacement_case`; no DUAL-LOCK structural gate — displacement_case can technically be left blank without enforcement |
| C-05 | PASS | BLOCK 1 fully resolves counter_hypothesis with `resolution_verdict` (REFUTED/PARTIALLY REFUTED/OPEN RISK); BLOCK 1 GATE: "resolution_verdict must be set before BLOCK 2 begins"; BLOCK 2 entry condition checks BLOCK 1 EXIT signal |
| C-06 | PASS | Tables in Stages 2, 3, 4 |
| C-07 | PARTIAL | status_quo_comparator in CAMPAIGN OPEN; displacement_case in BLOCK 2; but no per-stage displacement reads through evidence collection |
| C-08 | PASS | Entry conditions + exit signals at all stages; Stage 5 has block-level gates (BLOCK 1 EXIT: counter_hypothesis_resolved) |
| C-09 | FAIL | Low/Med/High only |
| C-10 | FAIL | No aggregate displacement verdict in Stage 4 |

**Scores**: essential 4/5 | recommended 2/3 | aspirational 0/2
**Composite**: (4/5 × 60) + (2/3 × 30) + (0/2 × 10) = 48 + 20 + 0 = **68**
**All essential pass**: No (C-04 PARTIAL → FAIL)

---

### V-04 — Session Invariants + Atomic Dual-Lock

**Axes**: SESSION INVARIANTS (V-01) + ATOMIC DUAL-LOCK (V-02), without the full R15 V-05 structural stack.

| Criterion | Result | Evidence Note |
|-----------|--------|---------------|
| C-01 | PASS | Correct sequence in header; all five stage headers present |
| C-02 | PASS | SI-03 scout_artifact locked in SESSION INVARIANTS; Stage 1 entry condition: "SI-03 — do not re-infer"; CAMPAIGN BLOCKED if not found |
| C-03 | PASS | Five WRITE + confirm instructions, one per stage |
| C-04 | PASS | Stage 5 ATOMIC DUAL-LOCK: both `hypothesis_verdict [LOCKED]` and `displacement_conclusion [LOCKED]` required; "If either absent or not marked [LOCKED]: set it before proceeding" |
| C-05 | PARTIAL | Stage 5 entry condition lists "counter_hypothesis available" but no two-block structure; DUAL-LOCK only checks verdict and displacement_conclusion |
| C-06 | PASS | Tables present in Stages 2, 3, 4 (basic format) |
| C-07 | PASS | SI-04 status_quo_comparator; s2_displacement_read + s3_displacement_read per evidence stage; displacement_conclusion [LOCKED] in Stage 5 |
| C-08 | PASS | PRE-CHECK with invariants_locked exit; all stages have entry conditions + EXIT signals |
| C-09 | FAIL | Low/Med/High only |
| C-10 | PARTIAL | Per-stage displacement reads but no s4_aggregate_displacement_verdict |

**Scores**: essential 4/5 | recommended 3/3 | aspirational 0/2
**Composite**: (4/5 × 60) + (3/3 × 30) + (0/2 × 10) = 48 + 30 + 0 = **78**
**All essential pass**: No (C-05 PARTIAL → FAIL)

---

### V-05 — All Three + R15 V-05 Full Stack

**Axes**: SESSION INVARIANTS + ATOMIC DUAL-LOCK + two-block Stage 5 + numbered dependency-chain roles + table evidence with SI-05 displacement template + entry conditions + exit signals.

| Criterion | Result | Evidence Note |
|-----------|--------|---------------|
| C-01 | PASS | Header states correct sequence; five stage headers present; PRE-STAGE EXIT gates Stage 1; exit signals chain all stages |
| C-02 | PASS | SESSION INVARIANTS partially open — SI-03 set by ROLE 1 and LOCKED after ROLE 1 CONFIRMED; Stage 1: "SI-03 locked — read from SESSION INVARIANTS, do not re-infer"; strongest possible enforcement |
| C-03 | PASS | WRITE + confirm at each stage; Stage 5 BLOCK 2 writes after DUAL-LOCK CLEARED; five distinct artifacts |
| C-04 | PASS | Stage 5 BLOCK 2 DUAL-LOCK GATE: checklist checks `hypothesis_verdict [LOCKED]` AND `displacement_conclusion [LOCKED]`; "DUAL-LOCK CLEARED" printed before WRITE and EXIT |
| C-05 | PASS | Stage 5 BLOCK 1: counter_hypothesis retrieved verbatim from Stage 1; evaluated against full evidence; typed resolution_verdict (REFUTED/PARTIALLY REFUTED/OPEN RISK); BLOCK 1 GATE: "resolution_verdict must be set before BLOCK 2 begins"; BLOCK 2 entry conditions verify BLOCK 1 EXIT and resolution_verdict not blank |
| C-06 | PASS | Rich tables with displacement check columns (SI-05 applied) in Stages 2, 3, 4; Stage 1 uses table for hypothesis fields |
| C-07 | PASS | ROLE 2 names comparator with comparator_strength + comparator_vulnerability; SI-05 displacement_template registered verbatim by ROLE 3 and applied to every evidence row in Stages 2, 3, 4; s4_aggregate_displacement_verdict; displacement_conclusion [LOCKED] in Stage 5 |
| C-08 | PASS | PRE-STAGE EXIT: campaign_open (all 3 roles confirmed); each stage has entry conditions + named EXIT signal; Stage 5 has block-level gates |
| C-09 | FAIL | confidence_final is Low/Med/High — no 1-10 numerical scale with penalty calculation |
| C-10 | PASS | Stage 4 has explicit `s4_aggregate_displacement_verdict` field with SI-05 applied to full pattern set; STAGE 4 EXIT carries the verdict value forward |

**Scores**: essential 5/5 | recommended 3/3 | aspirational 1/2
**Composite**: (5/5 × 60) + (3/3 × 30) + (1/2 × 10) = 60 + 30 + 5 = **95**
**All essential pass**: **Yes — GOLDEN**

---

### Rankings

| Rank | Var | Composite | All Essential | Notes |
|------|-----|-----------|---------------|-------|
| 1 | **V-05** | **95** | **Yes — GOLD** | Only variation satisfying full C-01 through C-05 stack |
| 2 | V-04 | 78 | No | Best non-gold; SESSION INVARIANTS + DUAL-LOCK close two gaps; C-05 still open |
| 3 | V-02 | 68 | No | DUAL-LOCK is strongest single-axis C-04 enforcement; C-05 and C-07 open |
| 3 | V-03 | 68 | No | Two-block Stage 5 is strongest single-axis C-05 enforcement; C-04 and C-07 open |
| 5 | V-01 | 66 | No | SESSION INVARIANTS robust for C-02 but misses C-04 and C-05 entirely |

---

### Excellence Signals (from V-05)

**Pattern 1 — Named-field immutability via SESSION INVARIANTS**
Fields SI-01 through SI-05 are declared once at campaign open and explicitly locked. Roles set SI-03 through SI-05; stages reference by SI-NN name only. This eliminates mid-campaign field drift without requiring the model to remember previous output. The "do not re-infer" instruction becomes a named rule against a named field, not an advisory reminder.

**Pattern 2 — ATOMIC DUAL-LOCK with [LOCKED] suffix notation**
Requiring both `hypothesis_verdict [LOCKED]` and `displacement_conclusion [LOCKED]` before a DUAL-LOCK GATE checklist clears creates a visible enforcement mechanism. The [LOCKED] suffix is a syntactic marker the model applies to the field value itself — easy to check, hard to accidentally bypass. The checklist repeats both field names explicitly with an escalation instruction: "If either absent or not marked [LOCKED]: set it before proceeding."

**Pattern 3 — Two-block Stage 5 with typed resolution_verdict as a blocking gate**
Splitting Stage 5 into BLOCK 1 (counter-hypothesis resolution → typed verdict) and BLOCK 2 (synthesis verdict, gated on BLOCK 1 EXIT) forces the counter-hypothesis to be explicitly resolved before the final verdict is permitted. The resolution_verdict types (REFUTED / PARTIALLY REFUTED / OPEN RISK) carry semantic meaning forward: OPEN RISK must be named in key_risk in BLOCK 2, creating a continuity chain between the resolution outcome and the risk disclosure.

**Pattern 4 — Displacement template registered once, applied everywhere**
ROLE 3 registers SI-05 as a verbatim displacement question template. Every evidence row in Stages 2, 3, and 4 applies SI-05 with a [Displacement Check] column. Stage 4 produces an aggregate verdict. Stage 5 BLOCK 2 issues displacement_conclusion [LOCKED]. This creates an unbroken displacement signal chain across six output points rather than a single synthesis-level assertion.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["SESSION INVARIANTS block with SI-NN field names declares campaign fields read-only after CAMPAIGN OPEN — stages reference by field name only, never re-infer", "ATOMIC DUAL-LOCK with [LOCKED] suffix notation gates synthesis_complete on both hypothesis_verdict and displacement_conclusion being explicitly marked before a checklist gate clears", "Two-block Stage 5: BLOCK 1 resolves counter-hypothesis with typed resolution_verdict as a structural gate before BLOCK 2 synthesis verdict can begin"]}
```
