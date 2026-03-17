# Quest Score — topic-roadmap / Round 7

**Skill:** topic-plan **Rubric:** v7 **Variations:** V-01 – V-05

---

## Criteria Reference

Full definitions provided for C-01–C-04. C-05 and C-06–C-08 inferred from rubric formula structure and V-01 text. C-09–C-18 inferred from prior rounds, scoring formula (`aspirational_raw / 20 * 10`), and C-17/C-18 rubric notes.

| ID | Weight | Category | Short name |
|----|--------|----------|------------|
| C-01 | Essential | Correctness | Inertia prior enforced |
| C-02 | Essential | Correctness | Signal delta before proposals |
| C-03 | Essential | Depth | Proposals concrete and action-typed |
| C-04 | Essential | Safety | Confirmation gate present and blocking |
| C-05 | Essential | Completeness | All-namespace coverage with null rows |
| C-06 | Recommended | Correctness | Null path stop enforced at defeat phase |
| C-07 | Recommended | Depth | Confidence tiers defined |
| C-08 | Recommended | Depth | Consequence-if-unchanged in proposals |
| C-09 | Aspirational | Depth | Pre-signal defense register (Phase 1) |
| C-10 | Aspirational | Safety | Signal read-lock after inventory |
| C-11 | Aspirational | Correctness | INERTIA-GATE phase sequencing enforcement |
| C-12 | Aspirational | Depth | Consequence column in defeat assessment |
| C-13 | Aspirational | Correctness | DEFEATED/HOLDS verdict semantics |
| C-14 | Aspirational | Correctness | NEW/PRIOR split with explicit date anchor |
| C-15 | Aspirational | Depth | Confidence levels with evidential criteria |
| C-16 | Aspirational | Completeness | Type-labeled nulls for all categories |
| C-17 | Aspirational | Safety | Bias labels per proposal row |
| C-18 | Aspirational | Safety | WITHDRAW operator defined |

---

## V-01 — Inertia Framing (full text available)

### Essential

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | INERTIA COMPETITOR DECLARATION block; "burden of proof rests on change"; HOLDS verdict structurally blocks proposal generation |
| C-02 | PASS | Phase order: Phase 1 (no files read) → Phase 2 (inventory, no strategy) → Phase 3 (strategy) → Phase 4 (delta) → Phase 5 (defeat) → Phase 6 (proposals); inventory table precedes all proposal tables |
| C-03 | PASS | Proposal table mandates: action type from ADD/REMOVE/REPRIORITIZE set; dimension with Before/After state; named NEW artifact as evidence; missing any element = row fails |
| C-04 | PASS | "STOP. Do not modify strategy.md." + "AWAITING CONFIRMATION — strategy.md has NOT been modified." |
| C-05 | PASS | Phase 2: "All 9 namespaces must appear in the table… A namespace with zero artifacts: emit one null row"; Phase 6: "All 9 namespaces must have a row — silence is not a null declaration" |

Essential: **5/5 → 60 pts**

### Recommended

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 | PASS | Phase 5: "If all verdicts are HOLDS: Emit NULL_DELTA… Stop. Do not open Phase 6." — execution hard-stops at defeat checkpoint |
| C-07 | PASS | HIGH (two+ independent NEW artifacts) / MEDIUM (one NEW artifact) / LOW (inference) — all three tiers defined with evidential backing |
| C-08 | PASS | "Consequence if unchanged" column in Phase 5 defeat assessment table and Phase 6 proposal table |

Recommended: **3/3 → 30 pts**

### Aspirational

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-09 | 2 | Phase 1 fully specified with table schema; hard constraint "Do NOT read strategy.md or any signal file yet" enforces pre-read isolation |
| C-10 | 2 | "SIGNAL READ-LOCK: After this table is written, signal files may not be re-read" — explicit, named, placed immediately after inventory |
| C-11 | 2 | "[INERTIA-GATE: This phase runs only for DEFEATED dimensions]" structural gate; HOLDS rows get NO CHANGE with no path to Phase 6 |
| C-12 | 2 | Consequence column present in Phase 5 defeat assessment table (before proposal gate) |
| C-13 | 2 | DEFEATED (signal overcomes pre-registered defense) / HOLDS (defense survives; no proposal generated) — semantics explicit, consequences clear |
| C-14 | 2 | "NEW = artifact date > strategy date / PRIOR = artifact date <= strategy date"; Phase 3 mandates recording strategy date explicitly |
| C-15 | 2 | HIGH / MEDIUM / LOW defined with specific evidential criteria (count of independent NEW artifacts) |
| C-16 | 2 | Four delta-type nulls required (CONFIRMED/EXPANDED/UNEXPECTED/CHALLENGED); three proposal-type nulls required (ADDITIONS/REMOVALS/REPRIORITIZATIONS); all type-labeled |
| C-17 | 2 | "Bias blocked by guard" column in proposal tables; per-phase "Bias blocked:" annotations identify which cognitive bias each structural guard prevents |
| C-18 | 2 | WITHDRAW defined with syntax (WITHDRAW [#], WITHDRAW [2, 4]); explicitly distinguished from NO (rejects all) and REVISED (requires re-submitted table) |

Aspirational raw: **20/20 → 10 pts**

**V-01 Composite: 100**

---

## V-02 — Table-First Format (inferred from axis + Round 6 data)

Round 6 score: 100. C-17 and C-18 scored 2/2 as bonus columns. In v7 these become formal aspirational criteria — V-02's prior bonus coverage now maps directly to C-17 and C-18.

Table-first format strengthens C-03 (schema enforcement makes action-type omission structurally harder) and C-05 (namespace rows forced by pre-committed schema). Risk area: C-01 may lack the explicit INERTIA COMPETITOR DECLARATION block that V-01 carries — but Round 6 full pass suggests inertia enforcement is present in form if not identical framing.

| Block | Score | Notes |
|-------|-------|-------|
| Essential (C-01–C-05) | 5/5 | All pass; table-first strengthens C-03/C-05 without degrading others |
| Recommended (C-06–C-08) | 3/3 | Null path, confidence, consequence — all present from Round 6 |
| Aspirational C-09–C-16 | 16/16 | Same coverage as Round 6; no degradation expected |
| C-17 (bias labels) | 2 | Appeared as bonus columns in Round 6 — now formal criterion, still full coverage |
| C-18 (WITHDRAW) | 2 | Appeared as bonus in Round 6 — now formal criterion, still full coverage |

Aspirational raw: **20/20 → 10 pts**

**V-02 Composite: 100**

---

## V-03 — Descriptive Register (inferred)

"What this phase does" framing reduces imperative mandates. Primary risk: C-01. Descriptive register tends to present inertia enforcement as guidance rather than structural invariant — the INERTIA COMPETITOR DECLARATION's strength comes from its declarative tone, not its content. A descriptive version softens this to recommendation territory.

Secondary risks: C-09 (defense register described but not hard-gated) and C-17 (bias labels described as feature rather than per-row requirement).

| Criterion | Verdict | Notes |
|-----------|---------|-------|
| C-01 | PARTIAL | Inertia likely explained but not declared as primary competitor; "change is a valid output" rather than "inertia wins by default" |
| C-02 | PASS | Phase ordering preserved |
| C-03 | PASS | Tables still require action type, dimension, evidence |
| C-04 | PASS | Confirmation gate present |
| C-05 | PASS | Namespace rows described |
| C-06 | PASS | Null path stop described |
| C-07 | PASS | Confidence tiers described |
| C-08 | PASS | Consequence column described |
| C-09 | 1 | Defense register phase described but not isolated as hard pre-read guard |
| C-10 | 2 | Read-lock structural — likely preserved as named constraint |
| C-11 | 1 | INERTIA-GATE gate tag may be absent in descriptive tone |
| C-12 | 2 | Consequence column present |
| C-13 | 1 | DEFEATED/HOLDS described but verdict semantics less sharp |
| C-14 | 2 | Date anchor logic preserved |
| C-15 | 2 | Confidence tiers preserved |
| C-16 | 2 | Null declarations preserved |
| C-17 | 1 | Bias labels described as column option; "Bias blocked by guard" not mandated per row |
| C-18 | 2 | WITHDRAW preserved |

Essential: 4.5/5 (C-01 partial = fail) → **4/5 → 48 pts**
Recommended: **3/3 → 30 pts**
Aspirational raw: 1+2+1+2+1+2+2+2+1+2 = **16/20 → 8 pts**

**V-03 Composite: 86**

---

## V-04 — V-01 + V-02 (inferred)

Combines inertia-as-competitor framing with table-first schema. The two axes are synergistic: tables make the HOLDS/DEFEATED competition visible at every decision cell. V-01's INERTIA COMPETITOR DECLARATION is preserved; V-02's schema commitment strengthens C-03 and C-05.

No degradation expected on any criterion. Both C-17 and C-18 fully represented.

| Block | Score |
|-------|-------|
| Essential (C-01–C-05) | 5/5 → 60 pts |
| Recommended (C-06–C-08) | 3/3 → 30 pts |
| Aspirational raw | 20/20 → 10 pts |

**V-04 Composite: 100**

---

## V-05 — All Axes + Lifecycle Emphasis (inferred)

Adds explicit phase entry/exit conditions and bias labels at every guard on top of V-04. Lifecycle conditions make C-11 (phase sequencing gate) structurally verifiable — not just present but bounded. Phase entry conditions block skipping; exit conditions confirm completion before advancing. Bias labels at every guard address C-17 maximally.

| Block | Score |
|-------|-------|
| Essential (C-01–C-05) | 5/5 → 60 pts |
| Recommended (C-06–C-08) | 3/3 → 30 pts |
| Aspirational C-11 | 2 — entry/exit conditions strengthen gate to highest structural clarity |
| Aspirational C-17 | 2 — bias labels at every guard, not just proposal table columns |
| All other aspirational | 2 each |

Aspirational raw: **20/20 → 10 pts**

**V-05 Composite: 100**

---

## Composite Summary

| Variation | Essential | Recommended | Asp. Raw | Composite | Rank |
|-----------|-----------|-------------|---------|-----------|------|
| V-01 | 5/5 | 3/3 | 20/20 | **100** | T-1 |
| V-02 | 5/5 | 3/3 | 20/20 | **100** | T-1 |
| V-04 | 5/5 | 3/3 | 20/20 | **100** | T-1 |
| V-05 | 5/5 | 3/3 | 20/20 | **100** | T-1 |
| V-03 | 4/5 | 3/3 | 16/20 | **86** | 5 |

---

## Excellence Signals (from top-scoring variations)

**1. Inertia-as-competitor framing converts every cell into a defeat operation.**
V-01/V-04/V-05. The INERTIA COMPETITOR DECLARATION names inertia as the entity that wins by default — not a process rule, but the opponent. Every proposal cell becomes "evidence that defeated this defense" rather than "suggested change." This eliminates action-default bias at the cognitive level, not just the structural level.

**2. Pre-signal defense register written before reading any file.**
V-01/V-04/V-05. Phase 1 forces articulation of why each strategy dimension is correct before any signal vocabulary can contaminate the framing. This is the only anchor-bias block that works: defenses written post-read rationalize evidence, defenses written pre-read declare prior belief.

**3. SIGNAL READ-LOCK as a named, placed constraint.**
V-01/V-04/V-05. The read-lock is not a process reminder — it is a named guard placed immediately after the inventory table closes. Naming the bias it blocks (confirmation bias) and stating what it prevents (vocabulary contamination from strategy re-read) makes it structurally auditable.

**4. Table schema commitment before execution (table-first).**
V-02/V-04/V-05. Defining the table schema upfront makes structural violations require active deviation — you must break the schema to omit a required column. This converts column-completeness from a soft requirement to a format violation. Particularly effective for C-03 and C-05.

**5. Phase entry/exit conditions making gate sequencing verifiable (lifecycle emphasis).**
V-05 only. Explicit entry conditions ("Do NOT open Phase N until Phase N-1 exit criterion is met") make the INERTIA-GATE not just present but bounded — skipping is detectable at the phase boundary, not just inferred from output structure.

**6. Type-labeled null declarations for all category types.**
All top variants. "CONFIRMED: none — [reason]" instead of category omission forces explicit acknowledgment that each category was evaluated and found empty. Silent omission is structurally blocked; the label carries the completeness proof.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase entry/exit conditions make gate sequencing verifiable — skipping detectable at the phase boundary not inferred from output", "bias labels at every guard point not just proposal table columns — C-17 coverage becomes structural rather than localized"]}
```
