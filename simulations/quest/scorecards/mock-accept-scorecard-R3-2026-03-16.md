## mock-accept Scorecard — Round 3

**Skill:** mock-accept | **Rubric:** v3 | **Date:** 2026-03-16
**Baseline:** R2 champion (SKIP table + Slot-2-first + bypass-error-code)

---

### Scoring Model

| Band | Criteria | Points each | Max |
|------|----------|------------|-----|
| Essential | C-01–C-05 | 12 (PARTIAL = 6) | 60 |
| Recommended | C-06–C-08 | 10 (PARTIAL = 5) | 30 |
| Aspirational | C-09–C-16 | 1.25 (PARTIAL = 0.625) | 10 |
| **Total** | | | **100** |

C-09–C-10: carried from earlier rounds (not explicitly defined in v3 rubric; assumed PASS across all variations since all carry R2 baseline).

---

### V-01 — Lifecycle Emphasis: CANARY SUPPRESSED Two-Branch Gate

**Axis:** lifecycle-emphasis | **Target:** C-14

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 — FORBIDDEN OUTPUTS TRIAD + CONTAMINATION GUARD | Essential | PASS | All 3 triad labels + completeness check present; AUTO-RULE CONTAMINATION GUARD with named error code (lines 101–115) |
| C-02 — Triad labels labeled | Essential | PASS | [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] all present |
| C-03 — Status written in-place + CANARY | Essential | PASS | Edit tool invocation + BRANCH A CANARY ASSERTION defined (lines 291–312) |
| C-04 — Review artifact structure | Essential | PASS | 4-col table, P1/P2/P3, urgency labels in Step 7 |
| C-05 — MOCK-ACCEPTED two-slot positive argument | Essential | PASS | Slot 2 first instruction explicit; Slot 1 labeled second; separate slots |
| C-06 — Entity-naming grammar | Recommended | PASS | "Yes/no answers do not satisfy entity-naming sub-question requirements" |
| C-07 — Two-list partition + bypass-error-codes | Recommended | PASS | ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS both named at guard sites; both lists recorded |
| C-08 — REAL-REQUIRED template + VERDICT-ECHO | Recommended | PASS | All 5 fields present; VERDICT-ECHO appears as prose constraint |
| C-09–C-10 | Aspirational | PASS | Carried from baseline |
| C-11 — bypass-error-code fields | Aspirational | PASS | `bypass-error-code: ARCH-GUARD-BYPASS` and `bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS` explicit |
| C-12 — Slot-2-first | Aspirational | PASS | "WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before Slot 2" |
| C-13 — SKIP table | Aspirational | PASS | SKIP in all evaluation columns for auto-flagged rows |
| C-14 — CANARY SUPPRESSED branch | Aspirational | **PASS** | BRANCH A/B gate structure; "CANARY SUPPRESSED is not an error"; "Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE" — all present |
| C-15 — Empty blocked-lists explicit | Aspirational | **PARTIAL** | Arch-blocked has "required even if list is empty" + empty notation, BUT Step 4 Strategy-blocked record has no empty notation (`[{list}]` only) |
| C-16 — VERDICT-ECHO as parseable code | Aspirational | **FAIL** | VERDICT-ECHO appears as prose note only — no `Error-code:` field |

**Aspirational score:** (5 + 1) × 1.25 + 0.625 + 0 = 7.5 + 0.625 = **8.125**
**V-01 Composite: 60 + 30 + 8.125 = 98**

---

### V-02 — Output Format: Empty Blocked-Lists Explicit

**Axis:** output-format | **Target:** C-15

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01–C-05 | Essential | **PASS × 5** | All triad elements, Edit tool, review artifact, two-slot argument present |
| C-06–C-07 | Recommended | **PASS × 2** | Entity-naming grammar; both guard lists + both bypass-error-codes present |
| C-08 — REAL-REQUIRED template + VERDICT-ECHO | Recommended | PASS | VERDICT-ECHO in prose |
| C-09–C-13 | Aspirational | PASS | Baseline |
| C-14 — CANARY SUPPRESSED branch | Aspirational | **PARTIAL** | CANARY SUPPRESSED named as inline fallback; "If condition not met: output 'CANARY SUPPRESSED...'" — present, but no BRANCH A/B structure, no "is not an error" clarification |
| C-15 — Empty blocked-lists explicit | Aspirational | **PASS** | Both Step 3 and Step 4 guard records have "REQUIRED OUTPUT even when list is empty" + "If empty: ..." notation for Arch-blocked and Strategy-blocked |
| C-16 — VERDICT-ECHO parseable code | Aspirational | **FAIL** | Prose only |

**Aspirational:** (5 + 0.625 + 1.25 + 0) + baseline 6.25 → 5×1.25 + 0.625 + 1.25 + 0 = 8.125
**V-02 Composite: 60 + 30 + 8.125 = 98**

---

### V-03 — Phrasing Register: VERDICT-ECHO as Parseable Error Code

**Axis:** phrasing-register | **Target:** C-16

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01–C-05 | Essential | **PASS × 5** | All present |
| C-06–C-07 | Recommended | **PASS × 2** | Entity-naming; two-list partition + bypass-error-codes |
| C-08 — REAL-REQUIRED template + VERDICT-ECHO | Recommended | PASS | VERDICT-ECHO now present as Error-code field (elevated from prose) — criterion satisfied |
| C-09–C-13 | Aspirational | PASS | Baseline |
| C-14 — CANARY SUPPRESSED branch | Aspirational | **PARTIAL** | Inline CANARY SUPPRESSED fallback; no BRANCH A/B gate; no "is not an error" statement |
| C-15 — Empty blocked-lists explicit | Aspirational | **FAIL** | Step 3 guard: `Arch-blocked (CONTRADICTS-ARCHITECTURE): [{list}]` — no empty notation. Step 4 guard: same. No "required even if empty" constraint |
| C-16 — VERDICT-ECHO parseable code | Aspirational | **PASS** | `Error-code: [VERDICT-ECHO if role is grammatical subject \| NONE if artifact is subject]` — structured artifact field with enumerated values |

**Aspirational:** 5×1.25 + 0.625 + 0 + 1.25 = 8.125
**V-03 Composite: 60 + 30 + 8.125 = 98**

---

### V-04 — Combination: CANARY SUPPRESSED Branch + Empty Blocked-Lists (C-14 + C-15)

**Axis:** lifecycle-emphasis + output-format | **Target:** C-14, C-15

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01–C-05 | Essential | **PASS × 5** | All present |
| C-06–C-08 | Recommended | **PASS × 3** | Entity-naming; partition + bypass-codes; REAL-REQUIRED template with VERDICT-ECHO prose |
| C-09–C-13 | Aspirational | PASS | Baseline |
| C-14 — CANARY SUPPRESSED branch | Aspirational | **PASS** | BRANCH A/B gate; "CANARY SUPPRESSED is not an error — it is the correct disclosure output"; "Do NOT conflate" statement |
| C-15 — Empty blocked-lists explicit | Aspirational | **PASS** | Both Step 3 (lines 969–978) and Step 4 (lines 1004–1013) have "REQUIRED OUTPUT even when list is empty" + explicit empty-list notation for both lists |
| C-16 — VERDICT-ECHO parseable code | Aspirational | **FAIL** | Prose: `[Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]` — not a structured field |

**Aspirational:** 5×1.25 + 1.25 + 1.25 + 0 = 8.75
**V-04 Composite: 60 + 30 + 8.75 = 98.75 → 99**

---

### V-05 — Full R3 Integration (C-14 + C-15 + C-16)

**Axis:** lifecycle-emphasis + output-format + phrasing-register | **Target:** C-14, C-15, C-16

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 — FORBIDDEN OUTPUTS TRIAD + CONTAMINATION GUARD | Essential | PASS | All 3 triad labels + completeness check; AUTO-RULE CONTAMINATION GUARD |
| C-02 — Triad labels labeled | Essential | PASS | All 3 present |
| C-03 — Status written in-place + CANARY | Essential | PASS | Edit tool; BRANCH A CANARY ASSERTION |
| C-04 — Review artifact structure | Essential | PASS | Step 7 complete: 4-col table, P1/P2/P3, urgency |
| C-05 — MOCK-ACCEPTED two-slot | Essential | PASS | Slot 2 first, Slot 1 second, structurally separate |
| C-06 — Entity-naming grammar | Recommended | PASS | "Yes/no answers do not satisfy..." |
| C-07 — Two-list partition + bypass-codes | Recommended | PASS | Both bypass-error-codes named; both lists with unconditional output |
| C-08 — REAL-REQUIRED template + VERDICT-ECHO | Recommended | PASS | Error-code field present — VERDICT-ECHO explicitly surfaced as parseable value |
| C-09–C-10 | Aspirational | PASS | Baseline |
| C-11 — bypass-error-code fields | Aspirational | PASS | Both guard sites |
| C-12 — Slot-2-first | Aspirational | PASS | "WRITE CONTRAST SLOT FIRST" |
| C-13 — SKIP table | Aspirational | PASS | Auto-flagged rows receive SKIP |
| C-14 — CANARY SUPPRESSED branch | Aspirational | **PASS** | BRANCH A / BRANCH B gate; "CANARY SUPPRESSED is not an error — it is the correct disclosure output when edits are incomplete"; "Do NOT conflate" |
| C-15 — Empty blocked-lists explicit | Aspirational | **PASS** | Step 3 (lines 1248–1257) and Step 4 (lines 1283–1292): "REQUIRED OUTPUT even when list is empty" + "If empty: 'Arch-blocked: [] (none...)'" and "If empty: 'Strategy-blocked: [] (none...)'" |
| C-16 — VERDICT-ECHO parseable code | Aspirational | **PASS** | `Error-code: [VERDICT-ECHO if role is grammatical subject \| NONE if artifact is subject]` + worked examples distinguishing correct vs incorrect subject; Row 5 of correspondence table labeled "(+ Error-code)" |

**Aspirational:** 8 × 1.25 = 10
**V-05 Composite: 60 + 30 + 10 = 100**

---

### Ranking

| Rank | Variation | Composite | New Aspirational |
|------|-----------|-----------|-----------------|
| 1 | V-05 | **100** | C-14 PASS, C-15 PASS, C-16 PASS |
| 2 | V-04 | **99** | C-14 PASS, C-15 PASS, C-16 FAIL |
| 3 | V-01 | **98** | C-14 PASS, C-15 PARTIAL, C-16 FAIL |
| 3 | V-02 | **98** | C-14 PARTIAL, C-15 PASS, C-16 FAIL |
| 3 | V-03 | **98** | C-14 PARTIAL, C-15 FAIL, C-16 PASS |

Single-axis variations all tie at 98 — each gains one criterion fully but has a PARTIAL and FAIL on the other two. The combination structure is load-bearing: V-04 adds 1 pt over V-01/V-02, and V-05 adds 1.25 pts over V-04 purely through the Error-code schema change.

---

### Excellence Signals from V-05

**Signal 1 — BRANCH A/B gate as semantic contract, not just branching logic.** The two-branch structure forces a model to select one named path and emit its associated output. By naming CANARY SUPPRESSED as "the correct disclosure output when edits are incomplete" and CANARY-FALSE-POSITIVE as "wrong assertion," the gate is not a conditional — it is a correctness taxonomy. Models that conflate suppression with error are prevented structurally.

**Signal 2 — Unconditional schema forces record presence independent of content.** "REQUIRED OUTPUT even when list is empty" + explicit `If empty: "..."` notation changes the guard record from a conditional output to a mandatory field. The record's *presence* becomes the signal, not just its contents. This closes a silent-omission failure mode that would otherwise be invisible in execution.

**Signal 3 — Promoting VERDICT-ECHO from prose constraint to structured field schema.** Row 5 of the REAL-REQUIRED template in V-05 has a `Claim:` / `Error-code:` / `Note:` sub-structure with two worked examples. The prose form says "do not do X"; the schema form says "output a checkable field whose value is either VERDICT-ECHO or NONE." The output becomes scannable without reading the rationale.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Two-branch CANARY gate (BRANCH A/B) assigns CANARY SUPPRESSED as a named affirmative path with explicit 'is not an error' declaration, preventing conflation with CANARY-FALSE-POSITIVE", "Unconditional guard record schema — 'REQUIRED OUTPUT even when list is empty' with explicit empty-list notation at both Arch-blocked and Strategy-blocked sites eliminates silent omission failure mode", "Error-code field in REAL-REQUIRED template promotes VERDICT-ECHO from prose instruction to parseable structured field with Claim/Error-code/Note substructure and worked examples"]}
```
