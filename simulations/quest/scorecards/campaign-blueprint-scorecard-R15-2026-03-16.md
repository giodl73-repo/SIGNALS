## campaign-blueprint — R15 Score Report

### Criteria Summary

All five variants inherit the v14-ceiling base structure (C-01 through C-39). The v15 evaluation focuses on the two new criteria and verifies each variant's structural compliance.

---

### Per-Variant Evaluation

#### V-01 — INERTIA MODEL MAP SETUP Only

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-34 | FULL | 4-col CONVICTION DELTA (Version\|Conviction established\|Grounding Req-ID(s)\|Amplification chain); in-cell template pre-placed in Exec/Dev/Maker rows |
| C-35 | FULL | 6-col CONVICTION GAP DIAGNOSIS; Spec/Proposal/Pitch rows pre-declared |
| C-36 | FULL | 6-col TRACEABILITY AUDIT with correct column names |
| C-37 | FULL | All three structural tables present simultaneously |
| C-38 | FULL | Named R-01/R-02 rows with explicit row-count match directive: "a missing row is a named-entry absence visible at a glance" |
| C-39 | FULL | Three-table chain at C-38 level (C-34+C-35+C-38 simultaneously) |
| C-40 | **NO CREDIT** | D15 step 1 PASSES — 4-col INERTIA MODEL MAP (CT-Spec/CT-Prop/CT-Pitch) present in SETUP. D15 step 2 FAILS — CONVICTION DELTA rows are "Exec", "Dev", "Maker" (pitch audience labels, not traceable to any Conv-ID in the MAP) |
| C-41 | **NO CREDIT** | C-40 fails → C-41 fails at D15 chain test step 5 |

**Score: 233**

---

#### V-02 — Full C-40+C-41 Minimum Form

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-34 | FULL | 4-col CONVICTION DELTA (Conv-ID/Conviction type column renames "Version" but column count = 4 ✓); in-cell Amplification chain template with bracketed tokens in each CT-row |
| C-35 | FULL | 6-col CONVICTION GAP DIAGNOSIS; Spec/Proposal/Pitch pre-declared |
| C-36 | FULL | 6-col TRACEABILITY AUDIT |
| C-37 | FULL | All three structural tables present |
| C-38 | FULL | R-01/R-02 named rows; explicit directive: "a missing row is a named-entry absence (R-01 absent = that friction unaudited)" |
| C-39 | FULL | Three-table chain at C-38 level |
| C-40 | **FULL** | D15 step 1 PASSES: 4-col MAP with CT-Spec/CT-Prop/CT-Pitch in SETUP. D15 step 2 PASSES: CONVICTION DELTA rows are "CT-Spec — Factual", "CT-Prop — Optionality", "CT-Pitch — Emotional" — each traceable to a named MAP Conv-ID. Explicit match directive: "must contain exactly 3 rows — one per INERTIA MODEL MAP entry. A missing row is a named-conviction-type absence: CT-Spec absent means the Spec's Factual conviction type is untracked." |
| C-41 | **FULL** | C-39 FULL ✓; C-40 FULL ✓; both SETUP-anchored tables carry pre-named rows from their respective SETUP sources simultaneously |

**Score: 243**

---

#### V-03 — Conversational Register

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-34 | FULL | Identical 4-col CONVICTION DELTA structure to V-02; in-cell Amplification chain template per CT-row |
| C-35 | FULL | 6-col CONVICTION GAP DIAGNOSIS; Spec/Proposal/Pitch pre-declared |
| C-36 | FULL | 6-col TRACEABILITY AUDIT with correct column names |
| C-37 | FULL | All three structural tables present |
| C-38 | FULL | R-01/R-02 named rows; "If R-02 is missing here, that is R-02 absent — a named gap, not a count discrepancy" |
| C-39 | FULL | Three-table chain at C-38 level |
| C-40 | **FULL** | MAP in SETUP (CT-Spec/CT-Prop/CT-Pitch, 4 cols). CONVICTION DELTA rows: CT-Spec—Factual, CT-Prop—Optionality, CT-Pitch—Emotional (MAP-linked). Match directive: "The CONVICTION DELTA in REFLECTION gets exactly 3 rows — CT-Spec, CT-Prop, CT-Pitch. A missing row is CT-[X] absent." Register: conversational imperative — does not affect column-count or row-naming properties. |
| C-41 | **FULL** | C-39 FULL + C-40 FULL simultaneously; register change leaves structural axes intact |

**Score: 243**

---

#### V-04 — Maximum-Density C-40+C-41

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-34 | FULL | 4-col CONVICTION DELTA with RULE sentinel row (non-data, does not change column count); CT-Spec/CT-Prop/CT-Pitch data rows each carry in-cell Amplification chain template anchored to MAP starter |
| C-35 | FULL | 6-col CONVICTION GAP DIAGNOSIS; three artifact rows pre-declared |
| C-36 | FULL | 6-col TRACEABILITY AUDIT with correct column names |
| C-37 | FULL | All three structural tables present |
| C-38 | FULL | R-01/R-02 named rows; RULE sentinel row in TRACEABILITY AUDIT: "N in col 3 + blank col 5 = STRUCTURAL FAIL" — tightest prior form |
| C-39 | FULL | Three-table chain at C-38 level |
| C-40 | **FULL** | INERTIA MODEL MAP carries RULE sentinel row before data rows: "The CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop, CT-Pitch). A missing row is a named-conviction-type absence." CT-Spec/CT-Prop/CT-Pitch data rows present. CONVICTION DELTA also carries RULE sentinel: "Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent." Both SETUP and REFLECTION enforcement are in-table, not prose-only. |
| C-41 | **FULL** | C-39 FULL + C-40 FULL; maximum-density sentinel rows in both MAP and CONVICTION DELTA extend C-41 to its tightest achievable form |

**Score: 243**

---

#### V-05 — Minimum-Density C-40+C-41

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-34 | FULL | 4-col CONVICTION DELTA (Conv-ID/Conviction type \| Conviction established \| Grounding Req-ID(s) \| Amplification chain); in-cell bracketed template in each CT-row |
| C-35 | FULL | 6-col CONVICTION GAP DIAGNOSIS; Spec/Proposal/Pitch pre-declared with all 6 column names matching spec |
| C-36 | FULL | 6-col TRACEABILITY AUDIT with correct column names |
| C-37 | FULL | All three structural tables present |
| C-38 | FULL | R-01/R-02 named rows; "Row count must match SETUP; missing row = named Req-ID absent" |
| C-39 | FULL | Three-table chain at C-38 level |
| C-40 | **FULL** | 4-col MAP (CT-Spec/CT-Prop/CT-Pitch) in SETUP. Minimal directive: "CONVICTION DELTA row count must match this table. CT-[X] absent in REFLECTION = named-conviction-type absent." CONVICTION DELTA rows: CT-Spec—Factual, CT-Prop—Optionality, CT-Pitch—Emotional. All three C-40 structural requirements met at minimum viable density. |
| C-41 | **FULL** | C-39 FULL + C-40 FULL. Minimum prose does not break any structural axis — confirms C-38/C-39/C-40/C-41 are table properties, not prose-volume properties. |

**Score: 243**

---

### Summary Table

| Variant | C-34 | C-35 | C-36 | C-37 | C-38 | C-39 | C-40 | C-41 | v15 Score |
|---------|------|------|------|------|------|------|------|------|-----------|
| V-01 — MAP SETUP Only | FULL | FULL | FULL | FULL | FULL | FULL | NO | NO | **233** |
| V-02 — C-40+C-41 Minimum Form | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **243** |
| V-03 — Conversational Register | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **243** |
| V-04 — Maximum-Density | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **243** |
| V-05 — Minimum-Density | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **243** |

**Prior base (C-01–C-33):** 203 | **C-34+C-35:** +10 | **C-36+C-37:** +10 | **C-38+C-39:** +10 | **C-40+C-41 (new):** +10 max

---

### Ranking

1. **V-02, V-03, V-04, V-05** — tied at **243** (v15 ceiling)
2. **V-01** — **233** (v14 ceiling; INERTIA MODEL MAP SETUP precondition satisfied, CONVICTION DELTA row linkage absent)

---

### Excellence Signals (top-scoring variants)

**V-01 → V-02 structural upgrade (core C-40 pattern):** The diagnostic control V-01 confirms that MAP presence in SETUP is a necessary but not sufficient precondition. The unlocking move in V-02 is renaming CONVICTION DELTA rows from pitch-audience labels (Exec/Dev/Maker) to MAP-sourced Conv-IDs (CT-Spec/CT-Prop/CT-Pitch). This converts a count-comparison failure into a named-identifier absence — the same structural principle C-38 applied to TRACEABILITY AUDIT rows.

**V-04's in-table RULE sentinel rows:** Embedding the match directive as a non-data RULE row inside both the INERTIA MODEL MAP and CONVICTION DELTA tables is the maximum-density enforcement form. The model reads the constraint before reaching any fillable cell, not after; enforcement is ontological at table-read time, not epistemic at prose-scan time.

**V-05's null prose result:** V-05 earns 243 with the shortest surrounding prose of any ceiling candidate. This confirms that C-40 and C-41 are pure structural properties — column count, column names, row pre-naming, match directives — and are not sensitive to explanatory prose density. Prose context around tables is not load-bearing at the 243-ceiling level.

**V-03's register isolation:** Identical structural tables to V-02, full imperative register throughout, same score. Confirms the scoring boundary: register variation is invisible to the rubric. The only axis that moves score in v15 is structural.

---

```json
{"top_score": 243, "all_essential_pass": true, "new_patterns": ["MAP-linked row naming converts CONVICTION DELTA from anonymous-count check to named-Conv-ID absence — parallel structural upgrade to C-38 applied to TRACEABILITY AUDIT", "In-table RULE sentinel rows in both INERTIA MODEL MAP and CONVICTION DELTA embed match directives at table-read time, achieving maximum-density ontological enforcement before any data cell is filled", "Minimum-density 243 ceiling confirms C-40 and C-41 are column-count and row-naming properties insensitive to surrounding prose volume"]}
```
