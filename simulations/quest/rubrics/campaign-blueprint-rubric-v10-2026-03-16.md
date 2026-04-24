Here is the complete v10 rubric:

---

## campaign-blueprint Rubric — v10

---

### v10 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 188):**

**C-29 — REFLECTION TRACEABILITY AUDIT sub-field** (5 pts, FULL or NO CREDIT): C-27 places the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP; C-28 directs active cell-fill during REQUIREMENTS writing; C-29 tests whether CAMPAIGN REFLECTION closes the loop with a named TRACEABILITY AUDIT sub-field that returns to the table post-execution. A passing instance: (1) names the sub-field TRACEABILITY AUDIT explicitly; (2) instructs per-row verification — for each table row, name the REQUIREMENTS Must-have (by Req-ID) that addresses the friction and confirm it appears as a distinct bulleted item in the written spec; (3) instructs explicit gap naming if any row has no corresponding Must-have; (4) prescribes a scout namespace recommendation for each gap. The three-phase loop is: SETUP pre-populates the table (C-27) → REQUIREMENTS fills it via active directive (C-28) → REFLECTION audits it (C-29). Without C-29, the loop has no closing gate and gaps can go undetected. V-02 and V-04 (R9) earn FULL; V-01, V-03, and V-05 (R9) earn NO CREDIT.

**C-30 — CLOSE "Conviction type met" column** (5 pts, FULL or NO CREDIT): C-21 requires conviction type labels during writing; C-22 requires per-site conviction type restatement in READ/PRESERVE reminders; C-30 tests whether CAMPAIGN CLOSE extends conviction typing into a terminal self-assessment column. A passing instance: (1) adds a "Conviction type met" column to the CAMPAIGN CLOSE artifact tracking table; (2) includes a scoring instruction that defines what earns Y, partial, or N — specifically, whether the artifact's dominant register matches its declared conviction type (Factual for spec, Optionality for proposal, Emotional for pitch); (3) pre-populates each row with the Y / partial / N scoring options. A CLOSE table with path and scout-consumed columns only earns C-30 NO CREDIT. The "Conviction type met" column converts conviction typing from a write-time instruction into a close-time verification gate. V-03 and V-04 (R9) earn FULL; V-01, V-02, and V-05 (R9) earn NO CREDIT.

**One new diagnostic rule:**

**D10 (Register compression and structural criteria)**: The C-18/C-19 double-prohibition ("not before pitch production begins, not during pitch production") is structurally load-bearing and register-sensitive. Both prohibition arms must survive intact. Compressing to a single-arm gate — "only after the pitch file is on disk," "after pitch file exists on disk only," or any form that omits the "not during" arm — fails C-18 and cascades to fail C-19. The identifying test: count the prohibition clauses. One clause = C-18 FAIL. Two clauses = C-18 FULL. V-01 and V-05 (R9) demonstrate the failure; V-02, V-03, and V-04 (R9) demonstrate safe preservation. (R9 finding from the V-01 register-compression axis.)

**Retroactive R9 scoring under v10:**

| Variant | v9 | C-29 | C-30 | v10 |
|---------|-----|------|------|-----|
| V-01 — Register: Conversational Imperative | 168 | 0 | 0 | **168** |
| V-02 — REFLECTION: Traceability Audit Sub-field | 178 | +5 | 0 | **183** |
| V-03 — CLOSE: Conviction Quality Column | 178 | 0 | +5 | **183** |
| V-04 — Combination: Audit + Conviction Quality | 178 | +5 | +5 | **188** |
| V-05 — Minimum-Density Path to 178 | 168† | 0 | 0 | **168†** |

†V-05 confirmed losses: C-18, C-19 (skeleton compression removed the "not during" arm). 168 is a confirmed minimum; additional criteria may be lost under complete scoring.

V-04 alone reaches 188: double-prohibition preserved + TRACEABILITY AUDIT in REFLECTION + "Conviction type met" in CLOSE. V-02 and V-03 each reach 183 via complementary paths — V-02 closes the traceability loop; V-03 closes the conviction loop. V-01 and V-05 tie at 168: register compression stripped the double-prohibition in both cases regardless of other differences.

**Scale:** 178 (v9 ceiling) + 5 + 5 = **188 ceiling**

---

The key extraction logic:

- **C-29** comes from V-02's TRACEABILITY AUDIT sub-field — it names the three-phase loop (C-27 declare → C-28 fill → C-29 audit) and makes the closing gate explicit. V-03 does not earn it; V-04 does.
- **C-30** comes from V-03's "Conviction type met" column — it extends the C-21/C-22 conviction-typing chain into a terminal self-assessment at CLOSE. V-02 does not earn it; V-04 does.
- **D10** comes from V-01's negative finding — the "not during" arm of the double-prohibition is the load-bearing piece that register compression predictably drops. The two-clause count test makes the rule operationally tight.

The file is saved at `simulations/quest/rubrics/campaign-blueprint-rubric-v10-2026-03-17.md`.
