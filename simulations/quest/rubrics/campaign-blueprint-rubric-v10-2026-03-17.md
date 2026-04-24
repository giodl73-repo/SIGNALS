```markdown
## campaign-blueprint Rubric — v10

---

### v10 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 188):**

**C-29 — REFLECTION TRACEABILITY AUDIT sub-field** (5 pts, FULL or NO CREDIT): C-27
places the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP; C-28 directs active cell-fill
during REQUIREMENTS writing; C-29 tests whether CAMPAIGN REFLECTION closes the loop with
a named TRACEABILITY AUDIT sub-field that returns to the table post-execution. A passing
instance: (1) names the sub-field TRACEABILITY AUDIT explicitly; (2) instructs per-row
verification — for each table row, name the REQUIREMENTS Must-have (by Req-ID) that
addresses the friction and confirm it appears as a distinct bulleted item in the written
spec; (3) instructs explicit gap naming if any row has no corresponding Must-have; (4)
prescribes a scout namespace recommendation for each gap. The three-phase loop is:
SETUP pre-populates the table (C-27) → REQUIREMENTS fills it via active directive (C-28)
→ REFLECTION audits it (C-29). Without C-29, the loop has no closing gate and gaps can
go undetected. V-02 and V-04 (R9) earn FULL; V-01, V-03, and V-05 (R9) earn NO CREDIT.

**C-30 — CLOSE "Conviction type met" column** (5 pts, FULL or NO CREDIT): C-21 requires
conviction type labels during writing; C-22 requires per-site conviction type restatement
in READ/PRESERVE reminders; C-30 tests whether CAMPAIGN CLOSE extends conviction typing
into a terminal self-assessment column. A passing instance: (1) adds a "Conviction type
met" column to the CAMPAIGN CLOSE artifact tracking table; (2) includes a scoring
instruction that defines what earns Y, partial, or N — specifically, whether the
artifact's dominant register matches its declared conviction type (Factual for spec,
Optionality for proposal, Emotional for pitch); (3) pre-populates each row with the
Y / partial / N scoring options. A CLOSE table with path and scout-consumed columns only
earns C-30 NO CREDIT regardless of how well the artifacts themselves perform. The
"Conviction type met" column converts conviction typing from a write-time instruction
into a close-time verification gate. V-03 and V-04 (R9) earn FULL; V-01, V-02, and
V-05 (R9) earn NO CREDIT.

**One new diagnostic rule:**

**D10 (Register compression and structural criteria)**: The C-18/C-19 double-prohibition
("not before pitch production begins, not during pitch production") is structurally
load-bearing and register-sensitive. Both prohibition arms must survive intact. Compressing
to a single-arm gate — "only after the pitch file is on disk," "after pitch file exists on
disk only," or any form that omits the "not during" arm — fails C-18 and cascades to fail
C-19. Conversational or compressed register is permissible only when both arms survive
verbatim or in equivalent two-arm form. The identifying test: count the prohibition clauses.
One clause ("only after…") = single-prohibition = C-18 FAIL. Two clauses ("not before…
not during…") = double-prohibition = C-18 FULL. V-01 and V-05 (R9) demonstrate the
failure; V-02, V-03, and V-04 (R9) demonstrate safe preservation. (R9 finding from the
V-01 register-compression axis.)

**Retroactive R9 scoring under v10:**

| Variant | v9 | C-29 | C-30 | v10 |
|---------|-----|------|------|-----|
| V-01 — Register: Conversational Imperative | 168 | 0 | 0 | **168** |
| V-02 — REFLECTION: Traceability Audit Sub-field | 178 | +5 | 0 | **183** |
| V-03 — CLOSE: Conviction Quality Column | 178 | 0 | +5 | **183** |
| V-04 — Combination: Audit + Conviction Quality | 178 | +5 | +5 | **188** |
| V-05 — Minimum-Density Path to 178 | 168† | 0 | 0 | **168†** |

†V-05 confirmed losses under full scoring: C-18, C-19 (skeleton compression removed the
"not during" arm from the REFLECTION gate). 168 is a confirmed minimum; additional criteria
may be lost under complete criterion-by-criterion scoring.

V-04 alone reaches 188: double-prohibition preserved + TRACEABILITY AUDIT in REFLECTION +
"Conviction type met" in CLOSE. V-02 and V-03 each reach 183 via complementary paths —
V-02 closes the traceability loop; V-03 closes the conviction loop — but neither adds both.
V-01 and V-05 tie at 168: register compression stripped the double-prohibition in both
cases regardless of their other differences.

**Scale:** 178 (v9 ceiling) + 5 + 5 = **188 ceiling**

---

### v9 Changes

**One new aspirational criterion (+5 pts, new ceiling 178):**

**C-28 — Active fill directive in REQUIREMENTS back-reference** (5 pts, FULL or NO
CREDIT): C-27 tests whether REQUIREMENTS references back to the campaign-level scout
traceability table; C-28 tests whether that back-reference takes the *active directive*
form — an explicit per-item instruction to complete the scout table as each Must-have is
written (e.g., "As you write each Must-have, complete its Req-ID and Must-have entry in
the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have must correspond to
a row in that table."). A static correspondence assertion ("Each Must-have must have a
corresponding row in...") satisfies C-27 but not C-28. The directive form enforces
real-time traceability as a writing behavior rather than a structural assertion — a
causal-ordering improvement over post-hoc correspondence checking. V-01 and V-02 (R8)
earn FULL; V-03 earns NO CREDIT.

**One diagnostic rule clarification:**

**D9 (C-27 back-reference forms)**: The C-27 back-reference criterion admits two
structurally distinct forms: (a) *minimal pointer* — names the SETUP table by its rubric
label, uses a positional reference ("above"), and asserts Must-have → row correspondence
without further instruction; (b) *active directive* — an explicit per-item fill
instruction that prompts the model to complete table cells while writing each Must-have.
Minimal pointer satisfies C-27 FULL. Active directive satisfies both C-27 FULL and C-28
FULL. The distinguishing test: does the instruction assert correspondence (pointer) or
command in-progress cell completion (directive)? (V-03 R8 finding; directive form
confirmed V-01 and V-02 R8.)

**Retroactive R8 scoring under v9:**

| Variant | v8 | C-28 | v9 |
|---------|-----|------|----|
| V-01 — C-27 + D8 Bracket: Named R8 Design Space | 173 | +5 | **178** |
| V-02 — C-27 + Compact C-26: SETUP Placement with Anchor | 168 | +5 | **173** |
| V-03 — C-27 Back-Reference Minimality: Pointer vs Directive | 173 | 0 | **173** |

V-01 alone reaches 178: bracket D8 + SETUP placement + bulleted C-26 + directive
back-reference. V-02 reaches 173 via a different path: full prose D8 + SETUP placement +
directive back-reference, but anchor-sentence C-26 costs 5 points. V-03 reaches 173 via
the complementary path: full prose D8 + SETUP placement + bulleted C-26, but minimal
pointer costs C-28. The two R8 173-point paths trade C-26 against C-28 — V-01 holds both
and is the unique 178 realization.

**Scale:** 173 (v8 ceiling) + 5 = **178 ceiling**

---

## Essential

| ID | Criterion | Weight |
|----|-----------|--------|
| C-01 | All three artifacts produced | 12 |
| C-02 | Canonical paths | 12 |
| C-03 | Topic identity consistency | 12 |
| C-04 | Execution order | 12 |
| C-05 | Minimum structure per sub-artifact | 12 |

**Essential total: 60**

---

## Recommended

| ID | Criterion | Weight |
|----|-----------|--------|
| C-06 | Proposal respects spec | 10 |
| C-07 | Pitch crystallizes recommended option | 10 |
| C-08 | Campaign framing — campaign opens with setup summary, closes with package summary | 10 |

**Recommended total: 30**

---

## Aspirational

| ID | Criterion | Weight |
|----|-----------|--------|
| C-09 | Narrative arc — each artifact amplifies conviction without repeating content | 5 |
| C-10 – C-22 | *(unchanged from v7)* | — |
| C-23 | Inertia-grounded conviction — CONVICTION TYPE labels explicitly reference INERTIA MODEL field at both campaign matrix and per-site execution reminder (D8) | 5 |
| C-24 | Scout signal integration — must-have requirements carry originating friction citations from scout files | 5 |
| C-25 | Scout traceability table — four-column labeled table present (Req-ID / Must-have / Originating Friction / Scout File); FULL or NO CREDIT | 5 |
| C-26 | Named INERTIA MODEL entity — three-field entity (Name / Behavior / Cost) declared with enumerated bulleted field-to-conviction-type mapping, one bullet per conviction type; FULL or NO CREDIT | 5 |
| C-27 | Scout traceability table in CAMPAIGN SETUP (friction-first placement) — table appears in CAMPAIGN SETUP pre-populated from scout inventory before Artifact 1 instruction; REQUIREMENTS references back to campaign-level table; FULL or NO CREDIT | 5 |
| C-28 | Active fill directive in REQUIREMENTS back-reference — REQUIREMENTS back-reference takes the active directive form: explicit per-item instruction to complete scout table cells as each Must-have is written, not a static correspondence assertion; FULL or NO CREDIT | 5 |
| **C-29** | **REFLECTION TRACEABILITY AUDIT sub-field — CAMPAIGN REFLECTION contains a named TRACEABILITY AUDIT sub-field that performs per-row Must-have coverage verification against the SCOUT TRACEABILITY TABLE, names any gaps, and prescribes a scout namespace for each gap; closes the SETUP→REQUIREMENTS→REFLECTION traceability loop; FULL or NO CREDIT** | **5** |
| **C-30** | **CLOSE "Conviction type met" column — CAMPAIGN CLOSE artifact table contains a "Conviction type met" column with a Y / partial / N scoring instruction that self-assesses whether each artifact's dominant register matches its declared conviction type; FULL or NO CREDIT** | **5** |

---

## Diagnostic Rules

| ID | Rule |
|----|------|
| D1–D7 | *(unchanged from v7)* |
| D8 | C-23 FULL requires inertia-grounded CONVICTION TYPE labels at BOTH the campaign-level matrix AND per-site execution reminders. Matrix-only grounding is insufficient. Accepted per-site forms: (a) full prose naming the INERTIA MODEL field ("document the INERTIA MODEL Cost field as factual record; do not argue"), (b) bracket notation explicitly naming the field (`[INERTIA MODEL Cost → factual record]`). Abstract per-site labels without INERTIA MODEL field reference earn C-23 PARTIAL regardless of matrix form. (V-01 R6 finding; bracket form validated V-03 R7.) |
| D9 | C-27 back-reference admits two forms: (a) *minimal pointer* — names the SETUP table by rubric label, positional reference ("above"), Must-have → row correspondence assertion; (b) *active directive* — per-item fill instruction commanding cell completion during Must-have writing. Minimal pointer earns C-27 FULL only. Active directive earns both C-27 FULL and C-28 FULL. The test: does the instruction assert structure (pointer) or command in-progress behavior (directive)? (V-03 R8 finding; directive form confirmed V-01 and V-02 R8.) |
| **D10** | **C-18/C-19 double-prohibition is register-sensitive and structurally load-bearing. The REFLECTION gate requires two explicit prohibition arms: "not before pitch production begins" AND "not during pitch production." Compressing to a single-arm form ("only after the pitch file is on disk," "after pitch file exists on disk only") drops the "not during" arm and fails C-18, cascading to C-19. Count the prohibition clauses: one clause = C-18 FAIL; two clauses = C-18 FULL. Conversational register is permissible only when both arms survive. (V-01 and V-05 R9 finding; preservation confirmed V-02, V-03, V-04 R9.)** |

---

## Scoring Summary

| Band | Points |
|------|--------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational (C-09, C-10–C-22, C-23–C-30) | 98 |
| **Ceiling** | **188** |
```
