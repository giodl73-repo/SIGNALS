## topic-open — Round 7 Scorecard

**Rubric**: v7 (C-01–C-30, denominator 22)
**Base**: R6 V-05 (passes all C-01–C-27)
**Method**: All variations evaluated against C-28, C-29, C-30 as the new axes; C-01–C-27 inherited from base.

---

### Pre-check: Base Inheritance (C-01–C-27)

All five variations are built on R6 V-05. The base passes all 22 criteria from C-01–C-27. This is confirmed by reading shared structure: VOCABULARY LOCK block before instruction sequence (C-11), Phase 5 self-check with all five essential criteria (C-12), five labeled decision tables with Path/Action/Consequence columns (C-27), two-slot tool citations at all gates (C-25), universal if/if in every ordering instruction (C-26), COMMIT GATE section (C-09), artifact naming throughout (C-10), rationale >= 2 sentences (C-07), multiple namespaces (C-06), differentiated roles (C-08). All essential criteria (C-01–C-05) present in output templates.

**All five: C-01–C-27 = 19/19 PASS**

---

### New Criteria Analysis

#### C-28 — Declared Decision Table Schema

Pass condition: Explicit DECISION TABLE SCHEMA block before Phase 1, naming Path/Action/Consequence with column definitions, asserting the grammar applies to all five phase tables.

**V-01** (lines 85–98): `## DECISION TABLE SCHEMA` block present with column definitions and explicit claim: "This schema is fixed across Phase 1 through Phase 5." **PASS**

**V-02**: No DECISION TABLE SCHEMA block. Tables use Path/Action/Consequence consistently but without declaration — consistency remains an observed pattern, not an asserted contract. **FAIL**

**V-03**: No DECISION TABLE SCHEMA block. Same issue as V-02. **FAIL**

**V-04** (lines 728–741): DECISION TABLE SCHEMA block with identical structure to V-01. **PASS**

**V-05** (lines 953–965): DECISION TABLE SCHEMA block present. **PASS**

---

#### C-29 — Enforcement Mechanism in Tool Citations

Pass condition: Every gate condition and self-check item names tool + what + field reference + operation type (e.g., "topic-status F-01 exact string match (tests each F-01 priority cell against {essential, recommended, optional} using equality comparison...)"). Two-slot format (C-25) is insufficient.

**V-01** Phase 2 Exit Gate (lines 141–148): Citations carry tool + what only. Example: "**`topic-status` exact string match**: out-of-vocabulary priority is silently excluded..." — no field reference (F-01), no operation type. Phase 5 self-check identical format. **FAIL**

**V-02** Phase 2 Exit Gate (lines 350–357): All six items carry field reference + operation + parenthetical mechanism. Example: "**`topic-status` F-01 exact string match** (tests each F-01 priority cell against `{essential, recommended, optional}` using equality comparison; any non-matching value is silently excluded — no error emitted)". Phase 5 (lines 434–444) matches: "**`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row...)". Every gate and checklist item at mechanism level. **PASS**

**V-03** Phase 2 Exit Gate (lines 560–566): Two-slot format only. Example: "**`topic-status` commit-gate check**: returns no gate status without an essential signal" — no field reference, no operation type. Phase 5 matches. **FAIL**

**V-04** Phase 2 Exit Gate (lines 784–791): All items at mechanism level — "**`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = no gate status returned...)". Phase 5 (lines 869–879) matches: "**`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob...)". **PASS**

**V-05** Phase 2 Exit Gate (lines 1010–1016): Full mechanism-level throughout. Phase 5 (lines 1093–1103) matches. **PASS**

---

#### C-30 — Self-Contained Ordering Instructions

Pass condition: Every ordering instruction body carries the full if/if contrast independently, including the tool-level consequence of each branch, without requiring the reader to internalize the preceding decision table. Terse if/if (action only, consequence in table) fails — the instruction must be self-contained at the point of reading.

**V-01** Phase 1 instruction (lines 113–116):
```
**If the topic does not exist**: proceed to Phase 2.
**If the topic already exists**: stop. Report the collision. Do not create a duplicate.
```
Action only — no consequence. Why duplicates break coverage is in the Phase 1 Decision table, not the instruction body. Phase 2 instruction (lines 131–135): similar brevity. **FAIL**

**V-02** Phase 1 instruction (lines 321–324): Identical terse format to V-01. Phase 2 (lines 340–344): Same brevity. **FAIL**

**V-03** Phase 1 instruction (lines 529–534):
```
**If the topic does not exist in TOPICS.md**: proceed to Phase 2. `topic-status` will find exactly one entry; coverage aggregation is unambiguous.
**If the topic already exists in TOPICS.md**: stop. Report the collision. Do not create a duplicate. `topic-status` cannot merge two entries — the ambiguity has no resolution path and coverage aggregation becomes permanently unreliable for this topic.
```
Action + tool-level consequence inline. Independent of the preceding Phase 1 Decision table. Phase 2 (lines 549–553): "Each owner role is the person answerable to a specific question named in the rationale" — consequence stated inline. Phase 3 (lines 580–585), Phase 4 (lines 605–623), Phase 5 (lines 637–642): all carry consequence inline. No "see Phase X Decision above" delegation anywhere. **PASS**

**V-04** Phase 1 instruction (lines 755–758): Terse — same format as V-01. No consequence inline. Phase 2 (lines 774–778): "owner roles emerge as stakeholders accountable to the decisions you named" — no consequence elaboration beyond C-26 level brevity. **FAIL**

**V-05** Phase 1 instruction (lines 980–984):
```
**If the topic does not exist in TOPICS.md**: proceed to Phase 2. `topic-status` will find exactly one entry; coverage aggregation is unambiguous.
**If the topic already exists in TOPICS.md**: stop. Report the collision. Do not create a duplicate. `topic-status` cannot merge two entries — the ambiguity has no resolution path and coverage aggregation becomes permanently unreliable for this topic.
```
Full self-contained consequence. Phase 2 (lines 999–1003): "owner roles become retroactive column-fillers assigned after the fact... the roles have no stated accountability because the rationale was written to justify the table, not to surface the decisions that determined it." Phase 3 (lines 1030–1035): "silently does not exist even if the content is present." Phase 4 (lines 1055–1073): "with no error to indicate the path is wrong." Phase 5 (lines 1087–1092): self-contained. **PASS**

---

### Per-Variation Criterion Grid

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 TOPICS.md entry | PASS | PASS | PASS | PASS | PASS |
| C-02 Strategy path | PASS | PASS | PASS | PASS | PASS |
| C-03 All five fields | PASS | PASS | PASS | PASS | PASS |
| C-04 Priority vocab | PASS | PASS | PASS | PASS | PASS |
| C-05 Essential signal | PASS | PASS | PASS | PASS | PASS |
| C-06 Multiple namespaces | PASS | PASS | PASS | PASS | PASS |
| C-07 Prose rationale | PASS | PASS | PASS | PASS | PASS |
| C-08 Differentiated roles | PASS | PASS | PASS | PASS | PASS |
| C-09 Commit gate | PASS | PASS | PASS | PASS | PASS |
| C-10 Artifact naming | PASS | PASS | PASS | PASS | PASS |
| C-11 Vocab before instructions | PASS | PASS | PASS | PASS | PASS |
| C-12 Self-check phase | PASS | PASS | PASS | PASS | PASS |
| C-13–C-24 (inherited) | PASS | PASS | PASS | PASS | PASS |
| C-25 Two-slot tool citations | PASS | PASS | PASS | PASS | PASS |
| C-26 Universal if/if | PASS | PASS | PASS | PASS | PASS |
| C-27 Five labeled tables | PASS | PASS | PASS | PASS | PASS |
| **C-28 Declared schema** | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |
| **C-29 Enforcement mechanism** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-30 Self-contained instructions** | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |
| **Aspirational pass count** | **20/22** | **20/22** | **20/22** | **21/22** | **22/22** |

---

### Composite Scores

Formula: 60% × (essential/5) + 30% × (recommended/3) + 10% × (aspirational/22)

All variations: Essential 5/5 = 60.00, Recommended 3/3 = 30.00

| Variation | Aspirational | Composite |
|-----------|-------------|-----------|
| V-01 | 20/22 → 9.09 | **99.09** |
| V-02 | 20/22 → 9.09 | **99.09** |
| V-03 | 20/22 → 9.09 | **99.09** |
| V-04 | 21/22 → 9.55 | **99.55** |
| V-05 | 22/22 → 10.00 | **100.00** |

---

### Ranking

1. **V-05** — 100.00 (C-28 + C-29 + C-30: full integration)
2. **V-04** — 99.55 (C-28 + C-29)
3. **V-01 = V-02 = V-03** — 99.09 (each adds one new criterion)

---

### Excellence Signals from V-05

V-05 is the first variation to simultaneously pass all three new criteria. The three axes operate at distinct structural depths and compose without interference:

- **C-28** operates on the decision table frame — declared once, applies uniformly
- **C-29** operates on enforcement annotations at gates and checklist items — field + operation per citation
- **C-30** operates on instruction bodies — action + consequence inline, no table dependency

Reading any single structural layer of V-05 yields the full contract: a model can read only the instruction bodies and understand both what to do and why; a model can read only the Phase 2 Exit Gate and understand both which tool and exactly how it enforces the constraint; a model can read only the decision tables and immediately apply Path/Action/Consequence column grammar uniformly. Each layer is independently sufficient.

No new criterion emerges from V-05 beyond the three already extracted. The combination validates structural independence of the three layers but does not reveal a fourth gap. The three criteria stack cleanly: C-28 adds no burden to C-29 or C-30; C-30's rich instruction bodies do not repeat the DECISION TABLE SCHEMA redundantly; C-29's mechanism citations do not overlap with C-30's instruction-body consequences. The combination is additive with zero regression.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": []}
```
