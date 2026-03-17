## Quest Score — org-build R13 (v9 rubric)

> **Note:** Only V-01 is present in the variate artifact. V-02 through V-05 are named in the header but contain no text. Scoring proceeds on V-01 only.

---

## V-01 — Roles-First → Assessment → Artifacts

### Essential Criteria (5)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Phase 3 Step 1 requires box/line ASCII diagram, min 2 org levels, every T1-AREAS area represented |
| C-02 | **PASS** | Phase 4 Step 2 names all five fields; Constraints: MUST include all five, FORBIDDEN: omitting any |
| C-03 | **PASS** | Phase 1 Step 6 requires inertia-advocate; both Phase 1 and Phase 4 Constraints carry FORBIDDEN: omitting |
| C-04 | **PASS** | Phase 1 Step 5 binds count floor to T1-DEPTH-FLAG: standard→20–30, deep→50+ |
| C-05 | **PASS** | Phase 3 Step 2: Area \| Headcount \| Key Roles \| Decides \| Escalates — all five columns explicit |

**Essential: 5 / 5**

---

### Recommended Criteria (3)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | Phase 4 Step 4 + Constraints: MUST group under `.craft/roles/{area}/`, FORBIDDEN: flat placement |
| C-07 | **PASS** | Phase 3 Step 3: ROB + shiproom + governance required; charter block with Quorum as N-of-M fraction |
| C-08 | **PASS** | Phase 3 Step 4 emits `FLAT-CASE-PRESSURE:` with T2-PRESSURE and single closed-set verdict |

**Recommended: 3 / 3**

---

### Aspirational Criteria (22)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **PASS** | Phase 3 Step 6: Row 1 = headcount threshold, Row 2 = different category — typed trigger differentiation enforced |
| C-10 | **PASS** | Phase 3 Step 5: every "Why It Applies Here" cell opens with `[element name] (cat-N) —` |
| C-11 | **PASS** | Phase 2 Step 4 captures verbatim template into T2-IA-SCOPE-TEMPLATE; Phase 4 Step 3 pipes it to IA `scope` — rating-keyed derivation chain intact |
| C-12 | **PASS** | Phase 2 Step 5 explicitly maps CAN-OPERATE-FLAT→cat-2/cat-3, STRUCTURE-WARRANTED→cat-1/cat-4; categories structurally tied to verdict |
| C-13 | **PASS** | Phase 3 Section 4: "Only one verdict. Both is an error. Neither is an error." — explicit error framing, not permissive |
| C-14 | **PASS** | Phase 1 emits T1-DEPTH-FLAG/T1-ROLE-COUNT/T1-AREAS; Phase 2 Input Contract names them by name; chain continues through Phase 4 |
| C-15 | **PASS** | Phase 2 Constraints: FORBIDDEN both, FORBIDDEN omitting both; Phase 3 Constraints repeats same bidirectional guards |
| C-16 | **PASS** | Phase 3 Constraints: FORBIDDEN: placing format guidance in Mitigation cells; MUST: specific remediation action |
| C-17 | **PASS** | Phase 2 Constraints: FORBIDDEN: paraphrasing, adapting, or deviating. Phase 4 Step 3: "verbatim text from T2-IA-SCOPE-TEMPLATE" |
| C-18 | **PASS** | Phase 2 Constraints: CAN-OPERATE-FLAT FORBIDDEN cat-1/cat-4; STRUCTURE-WARRANTED FORBIDDEN cat-2/cat-3 — exclusion sets explicitly named |
| C-19 | **PASS** | Every phase has a dedicated Constraints section; all constraint statements use MUST or FORBIDDEN; task steps use plain imperative (task register, not constraint register) — no advisory leakage |
| C-20 | **PASS** | All four phases declare typed record blocks; Phases 2–4 each carry named Input Contract sections consuming prior variables by name |
| C-21 | **PASS** | Every consuming Input Contract uses MUST: consume [T1-X / T2-X] — named typed variables bound imperatively in all downstream phases |
| C-22 | **PASS** | Phase 3 Section 7: Artifact Skeleton with `{{T2-PRESSURE}}`, `{{T2-VERDICT}}`, `{{T2-IA-SCOPE-TEMPLATE}}`, `{{T2-ANTI-PATTERN-CATS}}` — all slots keyed directly to Phase 2 gate variables |
| C-23 | **PASS** | Phase 1 Constraints: FORBIDDEN: beginning Phase 2 before emitting Phase 1 record block; same pattern at Phase 2→3 and Phase 3→4 — per-boundary, not top-level blanket |
| C-24 | **PASS** | `=== RECORD: PHASE-N ===` block with materialized variable assignments after every phase; Phases 1–3 each carry one |
| C-25 | **PASS** | Phase 1→2: outbound FORBIDDEN in Phase 1 Constraints + inbound FORBIDDEN in Phase 2 Input Contract; same at Phase 2→3 and Phase 3→4 — all three boundaries doubly guarded |
| C-26 | **PASS** | Each record block carries PHASE-ORDERING-GUARD (ordering anchor), named typed variables (gate schema), and is itself the materialized artifact — single construct satisfies all three properties |
| C-27 | **PASS** | Phase 1 Step 5 is a conditional inside the phase instruction: T1-DEPTH-FLAG = standard → 20–30; T1-DEPTH-FLAG = deep → 50+ — flag binding and per-value floors are structurally inside the phase, not in preamble |
| C-28 | **PASS** | PHASE-ORDERING-GUARD is the first named field inside every `=== RECORD: PHASE-N ===` block — not in preamble or surrounding prose |
| C-29 | **PASS** | Full scan: no "do not X", "never X", "avoid X" forms found in any constraint context. All prohibitions use `FORBIDDEN:` including the overwrite guard in Phase 4: "FORBIDDEN: overwriting any `.craft/roles/` file that already exists at the target path." |
| C-30 | **PASS** | Every phase has labeled sections: **Task Steps** (numbered prose) and **Constraints** (bulleted MUST/FORBIDDEN); Phase 2–4 also have **Input Contract** as a third distinct section — structural segmentation is explicit and auditable |

**Aspirational: 22 / 22**

---

## Score Summary

| Tier | Pass | Max | Weight | Points |
|------|------|-----|--------|--------|
| Essential | 5 | 5 | 60 | 60.0 |
| Recommended | 3 | 3 | 30 | 30.0 |
| Aspirational | 22 | 22 | 10 | 10.0 |
| **Composite** | | | | **100.0** |

---

## Variation Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | **V-01** | **100** | All 30 criteria pass |
| — | V-02 | n/a | Not provided |
| — | V-03 | n/a | Not provided |
| — | V-04 | n/a | Not provided |
| — | V-05 | n/a | Not provided |

---

## Excellence Signals from V-01

1. **Task / Constraint structural separation in every phase** — each phase uses labeled sections (Task Steps, Constraints, Input Contract) so constraint statements are auditable as a distinct class independent of task prose. This simultaneously satisfies C-19, C-30, and makes constraint completeness checkable by inspection.

2. **Type-annotated domain hints inside record block fields** — every `=== RECORD ===` field carries its valid value set inline (e.g., `[standard | deep]`, `[NONE | LOW | MODERATE | HIGH | CRITICAL]`, `[YES | NO]`). This makes the block schema self-documenting without needing a separate type legend. No rubric criterion tests this; it is a latent pattern.

3. **Input Contract as a named section distinct from the Constraints section** — consuming phases separate *what variables are required from upstream* (Input Contract) from *what must be true about the current phase's output* (Constraints). This structural split makes the gate-consumption audit independent of the gate-production audit.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Type-annotated domain hints inside record block fields (e.g., [NONE | LOW | MODERATE | HIGH | CRITICAL]) make the block schema self-documenting without a separate type legend — no criterion tests this inline value-set annotation pattern", "Input Contract as a structurally separate named section from Constraints — separates upstream-variable-consumption audit from current-phase-output audit, enabling independent inspection of each concern"]}
```
