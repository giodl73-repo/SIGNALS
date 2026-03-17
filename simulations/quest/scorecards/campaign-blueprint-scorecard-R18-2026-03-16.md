Now I have all five variants. Let me score them.

---

## campaign-blueprint R18 — Scorecard

### Scoring Approach

The v18 rubric adds two aspirational criteria on top of the v17 ceiling (263):
- **C-46** (+5): CONVICTION GAP DIAGNOSIS carries a non-data RULE sentinel row, positioned before Spec/Proposal/Pitch data rows, embedding (1) identifier-to-MAP-entry binding and (2) missing row = named-artifact absence, not count discrepancy
- **C-47** (+5): All five structural sentinels present simultaneously (MAP + CONVICTION DELTA + SCOUT TRACEABILITY TABLE + TRACEABILITY AUDIT + CONVICTION GAP DIAGNOSIS)

All variants inherit their v17 foundation. The audit below focuses on the decisive axis.

---

### V-01 — Four-Sentinel Control

**Axis:** Lifecycle gap-axis isolation — four R17 sentinels present; CONVICTION GAP DIAGNOSIS retains R17 form

**CONVICTION GAP DIAGNOSIS (CAMPAIGN CLOSE):**
```
| Artifact | Sub-section ... | Register found | Register declared | Scout sub-skill | Evidence needed |
|----------|-----------------|----------------|-------------------|-----------------|-----------------|
| Spec     |                 |                |                   |                 |                 |
| Proposal |                 |                |                   |                 |                 |
| Pitch    |                 |                |                   |                 |                 |
```
No RULE sentinel row. Spec/Proposal/Pitch are the first rows. The table meets C-35 (6-column, pre-declared rows, register-split columns) but carries no in-table enforcement sentinel.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-35 CONVICTION GAP DIAGNOSIS (6-col, pre-declared rows) | FULL | 6-column table; Spec/Proposal/Pitch pre-declared; register-split columns present |
| C-42 MAP RULE sentinel | FULL | INERTIA MODEL MAP carries RULE row: "CONVICTION DELTA...exactly 3 rows...missing row is named-conviction-type absence" |
| C-43 CONVICTION DELTA RULE sentinel | FULL | CONVICTION DELTA carries RULE row: "Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent." |
| C-44 SCOUT TRACEABILITY TABLE RULE sentinel | FULL | SCOUT TRACEABILITY TABLE carries RULE row: "TRACEABILITY AUDIT (REFLECTION) must have one row per entry here. Missing row = R-[NN] absent" |
| C-45 TRACEABILITY AUDIT RULE sentinels | FULL | Two RULE rows in TRACEABILITY AUDIT — named-absence rule + N+blank STRUCTURAL FAIL rule |
| **C-46 CONVICTION GAP DIAGNOSIS RULE sentinel** | **NO CREDIT** | No RULE row inside CONVICTION GAP DIAGNOSIS. Table has only Spec/Proposal/Pitch data rows. C-35 FULL; C-46 not triggered. |
| **C-47 Five-Sentinel Chain** | **NO CREDIT** | Depends on C-46 FULL. C-46 fails. |

**V-01 Score: 263 / 273**

---

### V-02 — Minimum-Form Five-Sentinel Chain

**Axis:** Output format — minimum-text CONVICTION GAP DIAGNOSIS RULE sentinel

**CONVICTION GAP DIAGNOSIS (CAMPAIGN CLOSE):**
```
| RULE     | Each artifact row here must match a named INERTIA MODEL MAP entry.
             Missing row = [artifact-ID] absent, not a count discrepancy. | — | — | — | — |
| Spec     | ...
| Proposal | ...
| Pitch    | ...
```
RULE row precedes Spec/Proposal/Pitch data rows. Minimum-text form.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-35 | FULL | 6-column table, pre-declared artifact rows, register-split columns |
| C-42 | FULL | MAP RULE row present (identical to V-01) |
| C-43 | FULL | CONVICTION DELTA RULE row present |
| C-44 | FULL | SCOUT TRACEABILITY TABLE RULE row present |
| C-45 | FULL | Two TRACEABILITY AUDIT RULE rows present |
| **C-46** | **FULL** | RULE row inside CONVICTION GAP DIAGNOSIS, positioned before Spec/Proposal/Pitch rows. Text: (1) "must match a named INERTIA MODEL MAP entry" — identifier binding declared; (2) "Missing row = [artifact-ID] absent, not a count discrepancy" — named-artifact absence declared. Both structural requirements met at minimum text density. |
| **C-47** | **FULL** | All five sentinels simultaneously: MAP (C-42) + CONVICTION DELTA (C-43) + SCOUT TRACEABILITY TABLE (C-44) + TRACEABILITY AUDIT (C-45) + CONVICTION GAP DIAGNOSIS (C-46). C-47 strict superset of C-46 — satisfied. |

**V-02 Score: 273 / 273**

---

### V-03 — Conversational Register

**Axis:** Phrasing register — CONVICTION GAP DIAGNOSIS RULE sentinel in conversational second-person

**CONVICTION GAP DIAGNOSIS (CAMPAIGN CLOSE):**
```
| RULE     | Every row here must be one of the three artifacts from the INERTIA MODEL MAP
             (Spec, Proposal, Pitch). If Proposal is missing, say "Proposal absent" —
             don't just count rows. | — | — | — | — |
| Spec     | ...
| Proposal | ...
| Pitch    | ...
```
RULE row precedes data rows. Conversational phrasing throughout.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-35 | FULL | 6-column structure, pre-declared rows, register-split columns (conversational headers) |
| C-42 | FULL | MAP RULE row: "You need exactly 3 rows...CT-[X] absent — a named failure, not a count problem" |
| C-43 | FULL | CONVICTION DELTA RULE: "Each Conv-ID must match...Missing row = CT-[X] absent — a named failure" |
| C-44 | FULL | SCOUT TRACEABILITY TABLE RULE: conversational form — "If a row is missing there, that's R-[NN] absent — say it by name" |
| C-45 | FULL | Two TRACEABILITY AUDIT RULE rows in conversational register — both structural requirements met |
| **C-46** | **FULL** | RULE row inside table, before data rows. Conversational text: (1) "must be one of the three artifacts from the INERTIA MODEL MAP" — identifier binding; (2) "If Proposal is missing, say 'Proposal absent' — don't just count rows" — named-artifact absence. Register is invariant property; in-table placement + rule content are the only evaluated dimensions. |
| **C-47** | **FULL** | All five sentinels present. D17 register invariance extends symmetrically to gap-diagnosis axis. |

**V-03 Score: 273 / 273**

---

### V-04 — Maximum-Density Five-Sentinel Chain

**Axis:** Lifecycle emphasis — all five sentinels at maximum text density

**CONVICTION GAP DIAGNOSIS (CAMPAIGN CLOSE):**
```
| RULE     | The CONVICTION GAP DIAGNOSIS must contain exactly one row per artifact declared
             in the INERTIA MODEL MAP (Spec, Proposal, Pitch). A missing row is a named-
             artifact absence — "Proposal absent" means the Proposal artifact's conviction
             gap status is undiagnosed — not a count discrepancy discoverable only by
             comparing totals. Artifact identifiers in col 1 must match INERTIA MODEL MAP
             entries. Do not introduce anonymous rows. | — | — | — | — |
| Spec     | ...
| Proposal | ...
| Pitch    | ...
```
Maximum-density RULE row; exhaustive structural declaration; all surrounding prose at maximum directive density.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-35 | FULL | 6-column, pre-declared rows, register-split columns |
| C-42 | FULL | MAP RULE: maximum-density — "CT-Spec absent means the Spec's Factual conviction type is untracked — visible at a glance by named-entry absence, not discoverable only by count comparison" |
| C-43 | FULL | CONVICTION DELTA RULE: maximum-density — "A missing row is a named-conviction-type absence: CT-Spec absent means...not discoverable by count alone" |
| C-44 | FULL | SCOUT TRACEABILITY TABLE RULE: maximum-density — "A missing REFLECTION row is a named-identifier absence...not a count discrepancy discoverable only by comparing totals" |
| C-45 | FULL | Two maximum-density TRACEABILITY AUDIT RULE rows |
| **C-46** | **FULL** | RULE row inside table, positioned before Spec/Proposal/Pitch. Maximum text: identifier binding + named-artifact absence + row count equality + prohibition on anonymous rows. All C-46 structural requirements met. Additional text density non-load-bearing — structural placement is the evaluated property. |
| **C-47** | **FULL** | All five sentinels present simultaneously at maximum density. |

**V-04 Score: 273 / 273**

---

### V-05 — Prose-Compressed Five-Sentinel Chain

**Axis:** Lifecycle compression — five sentinels present; all surrounding prose stripped to minimum

**CONVICTION GAP DIAGNOSIS (CAMPAIGN CLOSE):**
```
| RULE     | Each row here must match a named INERTIA MODEL MAP entry (Spec, Proposal, Pitch).
             Missing row = [artifact-ID] absent, not a count discrepancy. | — | — | — | — |
| Spec     | ...
| Proposal | ...
| Pitch    | ...
```
Minimum surrounding prose — phase headers retained, instructional paragraphs removed. RULE sentinel inside table before data rows.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-35 | FULL | 6-column table, Spec/Proposal/Pitch pre-declared, register-split columns present (compressed headers retained) |
| C-42 | FULL | MAP RULE: compressed — "CONVICTION DELTA (REFLECTION) must have exactly 3 rows: CT-Spec, CT-Prop, CT-Pitch. Missing row = named-conviction-type absent." |
| C-43 | FULL | CONVICTION DELTA RULE: "Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent. No anonymous rows." |
| C-44 | FULL | SCOUT TRACEABILITY TABLE RULE: compressed form — identical semantics to V-02 |
| C-45 | FULL | Two TRACEABILITY AUDIT RULE rows (compressed but structurally intact) |
| **C-46** | **FULL** | RULE row inside CONVICTION GAP DIAGNOSIS, before data rows. Compressed text: (1) "must match a named INERTIA MODEL MAP entry (Spec, Proposal, Pitch)" — identifier binding; (2) "Missing row = [artifact-ID] absent, not a count discrepancy" — named-artifact absence. Structurally equivalent to V-02 at minimum prose density. Adjacent prose volume is non-load-bearing for C-46. |
| **C-47** | **FULL** | All five sentinels present. Surrounding prose compression does not affect sentinel chain completeness. |

**V-05 Score: 273 / 273**

---

### Summary Table

| Variant | C-42 | C-43 | C-44 | C-45 | C-35 | C-46 | C-47 | Score |
|---------|------|------|------|------|------|------|------|-------|
| V-01 — Four-Sentinel Control | FULL | FULL | FULL | FULL | FULL | NO | NO | **263** |
| V-02 — Minimum Five-Sentinel Form | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **273** |
| V-03 — Conversational Register | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **273** |
| V-04 — Maximum-Density Five-Sentinel | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **273** |
| V-05 — Prose-Compressed Five-Sentinel | FULL | FULL | FULL | FULL | FULL | FULL | FULL | **273** |

**Ranking:** V-02 = V-03 = V-04 = V-05 (273) > V-01 (263)

---

### Excellence Signals

**From V-02 through V-05 (ceiling earners):**

1. **Fifth sentinel closes the gap-diagnosis axis.** The CONVICTION GAP DIAGNOSIS becomes self-enforcing when a non-data RULE row, positioned before the artifact data rows, declares: (a) each artifact identifier must match a named INERTIA MODEL MAP entry, and (b) a missing row is a named-artifact absence — not a count discrepancy. This mirrors the upgrade chain applied to the MAP (C-42) and SCOUT TRACEABILITY TABLE (C-44) in earlier rounds.

2. **Named-artifact absence vs count discrepancy is the semantic core.** All four 273-earning variants pass C-46 not by using more words but by including the structural distinction: "Proposal absent" (named) vs "one row short" (count). Any RULE text carrying this contrast satisfies the criterion regardless of register or density.

3. **Register and density invariance now extends to all five structural tables.** V-03 (conversational), V-04 (maximum density), V-05 (prose-compressed) all earn 273 — confirming that the evaluated property for C-46/C-47 is in-table structural placement, not text register, directive verbosity, or surrounding prose volume.

4. **C-47 is a strict superset requiring no additional work beyond C-46.** Any variant that achieves C-46 FULL and already carries the four R17 sentinels (C-42/C-43/C-44/C-45) automatically earns C-47 — the five-sentinel chain is complete as soon as the fifth sentinel exists.

---

```json
{"top_score": 273, "all_essential_pass": true, "new_patterns": ["CONVICTION GAP DIAGNOSIS gains self-enforcement when RULE sentinel row precedes artifact data rows and declares named-artifact absence (not count discrepancy) as failure mode", "Named-artifact absence vs count discrepancy is the semantic minimum for C-46 — any form carrying this contrast passes regardless of register or density", "Register and density invariance confirmed for gap-diagnosis axis: C-46/C-47 evaluated on in-table structural placement only, not text register, verbosity, or surrounding prose volume", "C-47 is automatic when C-46 FULL and four R17 sentinels present — fifth sentinel completes the chain with no additional structural work"]}
```
