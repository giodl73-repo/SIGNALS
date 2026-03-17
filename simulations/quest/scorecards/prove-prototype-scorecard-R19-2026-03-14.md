## Scoring — prove-prototype Round 19 (Rubric v18)

**Rubric ceiling:** 357 pts (Essential 60 + Recommended 30 + Aspirational 257 + Excellence 10)
**New criteria:** C-49 (5 pts) + C-50 (5 pts)
**R19 base assumption:** All variations built on R18 base satisfying C-01 through C-48 (337 pts non-excellence baseline)

---

### C-49 Detailed Analysis — Construction-Enforced Co-equality

C-49 requires identical column schema AND both rows carry **equivalent depth in every column**. The Key structural markers column is the critical test.

| Thread table column | V-01 Thread 1 : Thread 2 | V-02 Thread 1 : Thread 2 | V-03 Thread 1 : Thread 2 | V-04 Thread 1 : Thread 2 | V-05 Thread 1 : Thread 2 |
|--------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| **Scope** | ~2 clauses : 4 clauses | 3 clauses : 3 clauses | 3 clauses (instructional) : 3 clauses (instructional) | 3 clauses : 3 clauses | 4 clauses : 4 clauses |
| **Key structural markers** | **5 items : 5 items** ✓ | **6 items : 3 items** ✗ | **"write all five" : "write all three"** ✗ | **5 items : 5 items** ✓ | **5 items (enumerated) : 5 items (enumerated)** ✓ |
| **Terminal discharge obligation** | two contracts : two contracts | one chain : one confirmation | commanded : commanded | two contracts : two contracts | chain + 5-surface condition : two-row discharge table |

**Root cause of C-49 failure in V-02 and V-03:** Both lack the BUILD sub-role split. Without IMPLEMENTER/MEASURER, Thread 2 has only 3 structural markers (Phase 10 handoff, Phase 11 gate, CLOSE COMPLETE discharge). Thread 1 always has 5 markers across its five competitor surfaces. The 5:3 asymmetry cannot be resolved without adding BUILD intra-container markers. V-01, V-04, V-05 — which all add Phase 7 IMPLEMENTER handoff and Phase 8 MEASURER gate — bring Thread 2 to 5 markers, achieving depth parity.

---

### C-50 Detailed Analysis — Structural Marker Inventory

All five variations have the required elements: dedicated section before containers, four-column table, all four C-43/C-44/C-45 marker types, REQUIRED closure statement.

| Feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Section before containers | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4-column table (Marker type \| Required by \| Location \| Form) | ✓ | ✓ | ✓ | ✓ | ✓ |
| All 4 marker types present | ✓ | ✓ | ✓ | ✓ | ✓ |
| REQUIRED closure with hard modal | ✓ | ✓ | ✓ (commanded exactly) | ✓ | ✓ (adds "voids this C-50 inventory") |
| Location/Form cells are declarative | ✓ | ✓ | partial (instructional wrappers) | ✓ | ✓ |

V-03's inventory cells use parenthetical instruction wrappers ("Write the exact location:...") rather than direct column values. The REQUIRED closure is commanded in exact language, which is sufficient. C-50: PASS across all five, with V-03 weakest due to instructional form.

---

### Per-Variation Full Criterion Scores

> All R18 criteria (C-01 through C-48) treated as PASS in all variations — built on verified R18 base.

#### V-01 — Role Sequence

| Tier | Key criteria | Verdict | Evidence |
|------|-------------|---------|----------|
| Essential C-01–C-05 | Hypothesis, scope, measurement, actual/predicted, verdict | PASS all | All five CLOSE COMPLETE required elements present with hard-modal structure |
| Recommended C-06–C-08 | Minimality, raw evidence, limitations/next step | PASS all | Phase 12 + 13 explicitly gated |
| Aspirational C-09–C-48 | All R18 criteria | PASS (carried) | R18 base |
| **C-49** | Table-enforced co-equality | **PASS** | 5:5 Key markers parity (Phase 7 handoff, Phase 8 gate, Phase 10 handoff, Phase 11 gate, CLOSE COMPLETE discharge) |
| **C-50** | Structural Marker Inventory | **PASS** | 4-column pre-execution table with all 4 types; REQUIRED closure naming standalone-element requirement |

**Composite: 347/357**

---

#### V-02 — Output Format

| Tier | Key criteria | Verdict | Evidence |
|------|-------------|---------|----------|
| Essential C-01–C-05 | All | PASS all | CLOSE COMPLETE has required elements; Phase 10 verdict table structurally enforces evidence-grounding |
| Recommended C-06–C-08 | All | PASS all | Phase 12 limitations table, Phase 13 replication table |
| Aspirational C-09–C-48 | All R18 criteria | PASS (carried) | R18 base |
| **C-49** | Table-enforced co-equality | **PARTIAL** | Thread 2 Key markers = 3 items (Phase 10 handoff, Phase 11 gate, CLOSE COMPLETE discharge) vs Thread 1's 6 items — 6:3 depth disparity in the Key structural markers column; schema present and Scope column 3:3 equivalent, but Key markers depth fails equivalence requirement |
| **C-50** | Structural Marker Inventory | **PASS** | Pre-execution section, all 4 types, REQUIRED closure with prose-fails-C-48 language |

**Composite: 342/357** (C-49 partial credit ~3/5)

---

#### V-03 — Phrasing Register

| Tier | Key criteria | Verdict | Evidence |
|------|-------------|---------|----------|
| Essential C-01–C-05 | All | PASS all | Direct-address imperatives carry all required CLOSE COMPLETE elements; "GATE: Counter-evidence question explicitly closed" gate enforces C-16 |
| Recommended C-06–C-08 | All | PASS all | Phase 12 + 13 gated |
| Aspirational C-09–C-48 | All R18 criteria | PASS (carried) | R18 base |
| **C-49** | Table-enforced co-equality | **PARTIAL** | Thread 2 instructed to "write all three markers" while Thread 1 is instructed to "write all five surfaces" — 5:3 commanded depth asymmetry in Key structural markers column, compounded by instructional-cell form (commanded equivalence ≈ assertion-enforced, not construction-enforced) |
| **C-50** | Structural Marker Inventory | **PASS** | Section commanded before containers; table schema with all 4 marker types; exact REQUIRED closure commanded verbatim; instructional cell wrappers are a register choice, not a structural failure |

**Composite: 341/357** (C-49 partial credit ~2/5 — weaker than V-02 because of commanded asymmetry)

---

#### V-04 — Role Sequence + Phrasing Register

| Tier | Key criteria | Verdict | Evidence |
|------|-------------|---------|----------|
| Essential C-01–C-05 | All | PASS all | All CLOSE COMPLETE elements commanded with hard-modal operators; CLOSE COMPLETE includes two Thread 2 discharge confirmations |
| Recommended C-06–C-08 | All | PASS all | Phases 12 + 13 gated; AUDITOR explicitly owns Phase 12 limitations |
| Aspirational C-09–C-48 | All R18 criteria | PASS (carried) | R18 base |
| **C-49** | Table-enforced co-equality | **PASS** | Thread 2 row lists 5 structural markers (despite "Four markers" heading — counting: Phase 7 handoff, Phase 8 gate, Phase 10 handoff, Phase 11 gate, CLOSE COMPLETE discharge = 5); 5:5 depth parity; four sub-roles declared in Thread 2 scope matching Thread 1's multi-clause scope |
| **C-50** | Structural Marker Inventory | **PASS** | Pre-execution section; 4-column table; all 4 marker types; REQUIRED closure with standalone-element language |

**Note:** Thread 2 Key markers heading says "Four markers" but lists five — minor labeling inconsistency, actual depth parity is maintained.

**Composite: 347/357**

---

#### V-05 — Role Sequence + Output Format + Inertia Framing

| Tier | Key criteria | Verdict | Evidence |
|------|-------------|---------|----------|
| Essential C-01–C-05 | All | PASS all | CLOSE COMPLETE structured as a two-column element table — each required element on its own row with labeled key, making C-05 verdict and C-04 actual/predicted independently scannable |
| Recommended C-06–C-08 | All | PASS all | Phase 12 limitations table, Phase 13 replication table |
| Aspirational C-09–C-48 | All R18 criteria | PASS (carried) | R18 base; competitor lifecycle framing in tabular format with contamination risk + isolation purpose per boundary (advances C-46 expression) |
| **C-49** | Table-enforced co-equality | **PASS (strongest)** | Thread 1 explicitly declares "Five structural surfaces: (1)...(5)..." and Thread 2 explicitly declares "Five structural markers: (1)...(5)..." — numeric count labeling makes depth equivalence verifiable by count-match rather than by parsing prose length; most rigorous C-49 implementation across all R19 variations |
| **C-50** | Structural Marker Inventory | **PASS** | Pre-execution section; 4-column table; all 4 marker types with precise location/form; REQUIRED closure with "voids this C-50 inventory" consequence language — strongest closure phrasing |

**Additional structural advances:**
- CLOSE COMPLETE as two-column table: Thread 2 has two separate rows (`Thread 2 — IMPLEMENTER/MEASURER contract | DISCHARGED` and `Thread 2 — COMPARATOR/AUDITOR contract | DISCHARGED`), extending tabular construction enforcement through the terminal discharge line
- Competitor lifecycle framing in tabular form (5-column table with sub-transition rows) — most structured C-46 expression across R19

**Composite: 347/357 (tied on points; qualitatively strongest C-49 expression)**

---

### Composite Score Summary

| Rank | Variation | C-49 | C-50 | Total |
|------|-----------|------|------|-------|
| **1** | **V-05** (Role seq + Format + Inertia) | **PASS** — explicit 5:5 numeric count | **PASS** | **347/357** |
| **2** | **V-04** (Role seq + Register) | **PASS** — 5:5 depth parity | **PASS** | **347/357** |
| **3** | **V-01** (Role sequence) | **PASS** — 5:5 depth parity | **PASS** | **347/357** |
| 4 | V-02 (Output format) | PARTIAL — 6:3 Key markers | PASS | 342/357 |
| 5 | V-03 (Phrasing register) | PARTIAL — 5:3 commanded asymmetry | PASS | 341/357 |

**Note on three-way tie:** V-05 > V-04 ≈ V-01 by structural quality within PASS:
- V-05: Explicit count-verified 5:5, CLOSE COMPLETE table format, sub-role contracts on separate scannable rows
- V-04: Symmetric handoffs + conversational execution clarity; minor "Four markers" heading inconsistency
- V-01: Clean 5:5 structural parity without labeling artifacts

---

### Excellence Signals — V-05 (Top Variation)

**Signal 1 — Explicit numeric count labeling makes C-49 depth equivalence count-verifiable:**
V-05 declares "Five structural surfaces" for Thread 1 and "Five structural markers" for Thread 2 — using numeric labels that make column depth equivalence verifiable by checking whether the count matches (5 = 5) rather than by parsing prose clause length. This eliminates the subjectivity in evaluating "equivalent depth" that plagues unnumbered multi-clause entries, advancing C-49 from structural-schema enforcement to count-enforced co-equality.

**Signal 2 — Sub-role contract discharge as a two-row table inside CLOSE COMPLETE:**
V-05 structures Thread 2's terminal discharge as two separately labeled rows (`IMPLEMENTER/MEASURER contract | DISCHARGED` and `COMPARATOR/AUDITOR contract | DISCHARGED`) within the CLOSE COMPLETE table, rather than a compound statement. Each contract is independently scannable and auditable in isolation. This extends the tabular construction enforcement of C-49 through the document's terminal line — the same structural property (table = cannot collapse two rows into one) that C-49 uses in the preamble is preserved at the document exit.

**Signal 3 — BUILD sub-role split is structurally necessary for C-49 Key markers depth parity:**
V-02 and V-03 (no BUILD split) both fail C-49 depth equivalence despite having identical column schema. Without IMPLEMENTER/MEASURER, Thread 2 produces only 3 structural markers (Phase 10 handoff, Phase 11 gate, CLOSE COMPLETE discharge) vs Thread 1's 5 competitor surfaces. The BUILD split adds Phase 7 IMPLEMENTER handoff and Phase 8 MEASURER gate, bringing Thread 2 to 5 markers and achieving 5:5 parity. Construction-enforced co-equality requires depth equivalence in the Key markers column; achieving that equivalence requires symmetric intra-container structure across both containers that have role splits.

---

### R20 Seed

V-05 establishes the ceiling. The two remaining advances:

1. **Count-labeled parity + tabular CLOSE COMPLETE** are now both demonstrated. Combine with V-03's conversational register: direct-address imperatives commanding the model to write a table with "five items in each Key markers cell" enforces C-49 by both construction and instruction simultaneously.

2. **The "Four markers" heading inconsistency in V-04** (says Four but lists Five) is a labeling artifact that could surface as a genuine Thread 2 depth violation in a less well-formed document. R20 might test whether adding a count-verification instruction ("count the items you wrote; BOTH rows MUST list exactly five items") before the thread table produces stronger C-49 depth guarantee than the numeric labels alone.

---

```json
{"top_score": 347, "all_essential_pass": true, "new_patterns": ["BUILD sub-role split (IMPLEMENTER/MEASURER) is structurally necessary for Thread 2 Key structural markers to reach Thread 1 depth parity — without it Thread 2 has 3 markers vs Thread 1's 5, and C-49 depth equivalence fails regardless of schema identity", "Explicit numeric count labeling in both thread rows ('Five structural surfaces' / 'Five structural markers') makes column depth equivalence verifiable by count-match rather than prose-length parsing, advancing C-49 from schema-enforced to count-enforced co-equality", "Sub-role contract discharge expressed as two separately labeled rows inside CLOSE COMPLETE extends tabular construction enforcement through the terminal line — each contract is independently scannable rather than embedded in a compound statement"]}
```
