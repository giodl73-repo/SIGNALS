## discover-competitors-alt — R4 Scorecard

**All five variations: 140/140 — Exceptional**

---

### Composite by variation

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---:|---:|---:|---:|---:|
| Essential (60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (50) | 50 | 50 | 50 | 50 | 50 |
| **Composite** | **140** | **140** | **140** | **140** | **140** |

All 18 criteria PASS across all five variations. Three projections were off: V-02 and V-03 (projected 137.5) and V-05 (projected 135) all reached 140.

---

### Key reversals vs projections

**V-02 and V-03 PARTIAL? projections did not hold.** The projector was uncertain about one aspirational criterion for each but named no specific failure. On rubric inspection, both satisfy every criterion through their respective mechanisms.

**V-05 C-15/C-16 PARTIAL? projections did not hold.** This is the sharpest finding:
- **C-15** is structural (named slot position in template), not register-dependent. V-05's `SOURCE:` label appears before `REDUCTION-1`/`REDUCTION-2` in the template. The conversational ordering instruction embedded within the slot braces does not move the slot.
- **C-16** requires *naming* the error condition, not *isolating* it in a gate section. V-05 boldfaces all four failure states (`citation gate failure`, `anchor gate failure`, `proof structure failure`, `proof rerun failure`) within prose. The rubric text supports PASS.

**R4 answer: the rubric is register-neutral.** No criterion requires gate-table isolation. Conversational bold naming achieves the same compliance as formal gate declarations.

---

### Key interactions — resolved

| Interaction | Resolution |
|---|---|
| V-01 vs R3 V-05 on C-10 | C-10 is invariant to synthesis-first vs synthesis-last placement |
| V-02 vs V-03 on C-10 | Both PASS; V-02 structural coercion is more adversarially robust |
| V-04 vs V-01 on C-16 | Both PASS; V-04 gate tables exceed minimum but don't change score |
| V-05 C-15/C-16 | PASS; register neutrality confirmed |

---

### Excellence signals

1. **Synthesis-first contracts force aligned data collection** (V-01, V-04) — output requirements visible at Phase 3 collection time; Phase 3 explicitly cued to gather the absence evidence WHITESPACE needs
2. **Structural column coercion over instructional prohibition** (V-02) — Anchor column shape rejects name-only entries before rule evaluation; most adversarially robust C-13 mechanism
3. **Gate-as-section with PASS/FAIL tables** (V-04) — three-column gate tables (Check / Pass condition / Failure state) make the skill executable as a checklist; most debuggable structure in R4
4. **INERTIA-REF as per-finding reference baseline** (V-03, V-05) — named token + mandatory comparison clause elevates inertia from first table row to gravitational reference frame
5. **Register neutrality for C-15/C-16** (V-05) — proves criteria are satisfied by structure and naming, not by gate-table architecture

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["synthesis-first contracts make Phase 3 serve Phase 4 output requirements by name", "structural column coercion prevents name-only anchoring without instructional prohibition", "gate-as-section with PASS/FAIL tables makes failure states executable as a checklist", "INERTIA-REF token elevates inertia from first row to per-finding reference baseline", "C-15 and C-16 are register-neutral: named slot position and explicit error naming satisfy both criteria in conversational prose"]}
```
ASS |
| **C-14** AMEND as proof validator | PASS | PASS | PASS | PASS | PASS |
| **C-15** Inline anchor tag before proof | PASS | PASS | PASS | PASS | PASS |
| **C-16** Gate failure naming | PASS | PASS | PASS | PASS | PASS |
| **C-17** WHITESPACE by attribute absence | PASS | PASS | PASS | PASS | PASS |
| **C-18** NOT ACCEPTABLE anchoring example | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**

- **C-09:** All five have CROSS-DIMENSIONAL block with REDUCTION-1/2 requiring both dimensions to produce the gap. PASS by structure.

- **C-10:** V-01/V-03/V-04 enforce via instruction ("catch any anchor gate failure and rewrite before proceeding"). V-02 enforces via column shape — the Anchor column requiring `Row C{N} + attribute: value` structurally rejects name-only entries before any rule evaluation. V-05 instruction-based with NOT ACCEPTABLE examples. All five close the free-floating finding escape. PASS for all.

- **C-11:** Per-row citation gate present in all five. Every external row requires a URL in the Citation column. Empty cell or trailing footnote named as "citation gate failure" in all five. PASS.

- **C-12:** All five CROSS-DIMENSIONAL blocks include REDUCTION-1 (map alone — gap absent? NO) and REDUCTION-2 (focus alone — gap absent? NO), with instruction "if either reduction cannot honestly answer NO, find a different gap." THEREFORE clause present. PASS.

- **C-13:** V-01/V-04: Output C section lists specific qualifying attributes (threat level, mechanism phrase, offering claim, focus-column value) + NOT ACCEPTABLE examples. V-02: Anchor column structurally requires cell-level values — `Row C{N}, {attribute}: "{value}"`. V-03/V-05: Claim-level anchoring rule with attribute type list + NOT ACCEPTABLE examples. All five close name-only anchoring. PASS.

- **C-14:** All five AMEND adjustment 1 ("Shift focus") explicitly prescribes: replace SOURCE slot, then rewrite REDUCTION-1 and REDUCTION-2 from scratch. Named failure for standalone "update the finding" instruction: "proof rerun failure" in all five. V-05: "the reconstruction of both single-dimension reduction arguments is what makes the proof valid, not just a new conclusion." PASS.

- **C-15:** The rubric requires a named evidentiary source slot (SOURCE:, ANCHOR:, or equivalent) to appear before the reduction arguments. All five include `SOURCE: {...}` as the first element in the CROSS-DIMENSIONAL proof block, before REDUCTION-1 and REDUCTION-2. V-01/V-04: "Do not proceed to REDUCTION-1 until this slot is filled" as a standalone rule. V-05: SOURCE slot labeled and placed before REDUCTION-1/2 in the template; "Write this before you write anything else in this block" embedded within the slot. The named slot is present and sequentially prior in all five. **V-05 PASS**: the named slot requirement is architectural (slot precedes reductions in template), not register-dependent. Conversational embedding of the ordering instruction within the slot braces does not move the slot itself.

- **C-16:** The rubric requires naming the error condition explicitly rather than only describing the rule in positive terms. All five name multiple failure states:
  - "citation gate failure" — all five, bolded
  - "proof structure failure" — all five, bolded
  - "anchor gate failure" — all five, bolded
  - "proof rerun failure" — all five, bolded
  - V-04 additionally names "inertia naming failure", "inertia threat failure", "inertia mechanism failure", "threat gate failure", "whitespace gate failure" in GATE sections.

  **V-05 PASS**: the rubric requires *naming* the error condition, not *isolating* it in a gate section. Bolded naming within conversational prose satisfies the explicitness requirement. "an empty Citation cell is a **citation gate failure**" names the condition explicitly. The rubric does not require gate-table architecture; it requires the name to appear. All five PASS.

- **C-17:** All five supply the WHITESPACE absence block template:
  ```
  Absence evidence: Row C{N} -- {attribute column}: {absent or "None" / "N/A" / uncontested value}.
  Gap confirmed: No row provides a non-absent value for [{attribute column(s)}] -- attribute-level uncontested.
  ```
  All five include NOT ACCEPTABLE bare-assertion examples. V-03/V-05 add a "C0 position" line citing the C0 mechanism or focus-column value. V-02 adds an ACCEPTABLE example with row-by-row evidence. PASS for all.

- **C-18:** All five include explicit NOT ACCEPTABLE name-only anchoring exemplars:
  - "Competitor 2 reveals that..." — present in all five
  - "As Competitor 1 demonstrates..." — present in V-01/V-03/V-04/V-05; V-02 substitutes "Competitor 2" (name-alone form) as a third NOT ACCEPTABLE case
  V-05 conversational: "Don't write 'Competitor 2 reveals that...' -- that's name-only anchoring." PASS for all.

Aspirational subtotal: **10/10 → 50 pts** for all variations.

---

## Composite Scores

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---:|---:|---:|---:|---:|
| Essential (60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (50) | 50 | 50 | 50 | 50 | 50 |
| **Composite** | **140** | **140** | **140** | **140** | **140** |
| **Grade** | Exceptional | Exceptional | Exceptional | Exceptional | Exceptional |
| **Golden threshold** | YES | YES | YES | YES | YES |

---

## Key Interactions — Resolved

**V-01 vs R3 V-05 on C-10 (synthesis-first vs synthesis-last):**
C-10 is invariant to instruction placement. Grounding compliance is enforced by the anchor failure rule and NOT ACCEPTABLE examples regardless of when synthesis requirements are declared. Synthesis-first does not change C-10 scoring but strengthens data-collection alignment — Phase 3 explicitly told to collect absent values for Output A.

**V-02 vs V-03 on C-10 (column enforcement vs rule enforcement):**
Both PASS. V-02's structural column coercion provides the stronger *model-behavior* guarantee: table shape rejects name-only entries before any rule evaluation. V-03's inertia clause adds a required per-finding sentence that independently grounds findings against INERTIA-REF. Different mechanisms, same rubric result; V-02 is structurally more reliable under adversarial completion.

**V-04 vs V-01 on C-16 (gate-as-section vs inline gate rules):**
Both PASS. V-04's gate tables (PASS/FAIL columns with named failure states, pass conditions, and remediation actions) exceed the rubric minimum for C-16 — they are more scannable and complete than inline gate rules. But C-16 requires only that the name appears; V-01's inline naming satisfies. No differential scoring.

**V-05 C-15/C-16 (conversational register stress test):**
Both PASS. The key finding: C-15 compliance is architectural (slot position in template), not register-dependent. C-16 compliance requires naming, not isolation. Bolded failure state names within conversational prose satisfy both. **Register is neutral for these criteria** — the variation writer's PARTIAL? projection does not hold against the rubric text.

---

## Excellence Signals

Patterns from the R4 round that represent genuine structural improvements over prior rounds:

**1. Synthesis-first contracts (V-01, V-04)**
Moving the SYNTHESIS REQUIREMENTS block before Phase 3 creates a data-collection contract. Phase 3 collects Mechanism and Focus-column values *knowing* they will become WHITESPACE absence evidence. This is a causal architecture improvement: output requirements are visible at input-gathering time. V-04 combines this with gate sections for maximum structural clarity.

**2. Structural column coercion over instructional prohibition (V-02)**
The findings table Anchor column requiring `Row C{N}, {attribute}: "{value}"` enforces C-13 compliance via template shape rather than instruction. A competitor name alone fails the column format before any rule is evaluated. This is the most robust mechanism for eliminating name-only anchoring: form coerces compliance without relying on model instruction-following.

**3. Gate-as-section architecture with PASS/FAIL tables (V-04)**
Standalone GATE sections (Gate 1 / Gate 2 / Gate 3) with three-column tables (Check / Pass condition / Failure state) make every failure state a checkable discrete item. Each gate is a self-contained checkpoint with explicit remediation. This goes beyond rubric compliance: it makes the skill executable as a checklist. Most debuggable structure in R4.

**4. INERTIA-REF token as per-finding reference baseline (V-03, V-05)**
Extracting the C0 mechanism into a named token (`INERTIA-REF`) and requiring an inertia comparison clause per finding transforms C0 from a first table row into a gravitational reference frame. Every finding must say whether it reinforces, challenges, or contextualizes the inertia case. This deepens C-06 compliance from minimum-mechanism to systemic reasoning across all findings.

**5. Register neutrality (V-05)**
The sharpest empirical finding of R4: conversational prose with bolded failure state names achieves the same rubric compliance as formal gate declarations. C-15 and C-16 are satisfied by structure (named slot before reductions) and explicit naming — neither criterion requires gate-table isolation. This proves the rubric is register-neutral for these criteria.

---

## Variations Projected vs Actual

| Variation | Projected | Actual | Delta | Note |
|-----------|----------:|-------:|------:|------|
| V-01 | ~140 | 140 | 0 | On target |
| V-02 | ~137.5 | 140 | +2.5 | Projector was uncertain about one PARTIAL; rubric text supports PASS |
| V-03 | ~137.5 | 140 | +2.5 | Same; no criterion is PARTIAL on inspection |
| V-04 | ~140 | 140 | 0 | On target |
| V-05 | ~135 | 140 | +5 | PARTIAL? projections on C-15/C-16 do not hold; rubric is register-neutral |

**Why V-02 and V-03 were projected lower:**
The variations doc was conservative about one aspirational criterion for each but did not name it precisely. On inspection, no criterion reaches even PARTIAL in either variation. The tabular format (V-02) and inertia-clause framing (V-03) both satisfy all 18 criteria through distinct structural mechanisms.

**Why V-05 was projected lower:**
The PARTIAL? projections on C-15 and C-16 hinged on whether "isolated gate architecture" was required. The rubric text requires: named slot before reductions (C-15) and explicit error-condition naming (C-16). Neither criterion specifies isolation or gate-table format. Bolded inline naming in conversational prose is sufficient.

---

## R4 Answer

**All five structural arrangements satisfy all 18 criteria.** No criterion couples tightly enough to R3 V-05's structural form to break under the tested variations. The rubric is structurally robust: synthesis-first, tabular findings, inertia-centric framing, gate-as-section tables, and conversational register all achieve 140/140.

The variations do differentiate on *mechanism strength* (V-02 structural coercion > instructional prohibition for C-13; V-04 gate tables > inline rules for debuggability) but not on rubric score. The next round should test adversarial conditions where compliance *breaks* — not alternative compliant arrangements.

