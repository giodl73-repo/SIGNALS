Now I have everything needed to score all five variations. Let me compile the full scorecard.

---

# flow-throttle Scorecard — Round 14

**Rubric:** v14 (C-01 through C-37) | **Date:** 2026-03-16
**Max composite:** 235 | **Golden threshold:** all 5 essential PASS + composite >= 80
**Baseline:** R13 V-04 → 230/235 under v14 (C-37 FAIL: no annotation inventory in FORMAT CONTRACT)

---

## Scoring Framework

All five variations inherit R13 V-04's architecture intact:

- Three-role pipeline: Format Analyst (Role 1) → Domain Expert (Role 2) → Consequence Analyst (Role 3)
- FORMAT CONTRACT with Section A (prose-restriction) and Section B (structured-output register, closed, with 3-field inertia annotation)
- SOURCE REGISTER (Step 1A) before tier analysis, UNDOCUMENTED enforcement
- TABLE A through TABLE F with full cross-artifact header structure
- TYPE SCAN GATE between TABLE E and TABLE F with 3-field purpose annotation, 5-observable + 1-observable audit test, escape-route demolisher
- Role 3 ACTIVATION CONDITIONS referencing gate-present (5 observables) and gate-absent (1 observable) count declarations
- Global criterion-coverage step

All C-01 through C-36 carry from R13 V-04. The scoring axis for R14 is C-37 only.

---

## Per-Variation Criterion Review

### V-01 — Lifecycle Emphasis (Section C as prose list)

**C-37 evidence:** Section C in FORMAT CONTRACT enumerates Annot-01 through Annot-07 as bullet points, each with anchor identifier (e.g., `TABLE A, \`Limit (number + unit)\` column definition`) and failure-mode label (e.g., `vague-label substitution`). Closes with: "This inventory is closed. An annotation not listed here does not exist as a contract requirement. An annotation listed here that is absent from its anchor site in the body is a FORMAT CONTRACT violation." Sealed before `FORMAT CONTRACT COMPLETE`.

| Band | Criteria | Verdict | Evidence note |
|------|----------|---------|---------------|
| Essential | C-01 | PASS | TABLE A Binding? + [prose: item 1 — binding-tier causal reason] |
| Essential | C-02 | PASS | TABLE B with mechanism values (queue-fill, connection-hold, etc.), 2+ hops |
| Essential | C-03 | PASS | TABLE A >=2 rows with Component + Scope + numeric Limit |
| Essential | C-04 | PASS | TABLE C one row per TABLE A Tier-ID, no omission |
| Essential | C-05 | PASS | TABLE D with burst path + gap reason |
| Recommended | C-06 | PASS | TABLE C Retry-After fields; TABLE B retry-amplification mechanism |
| Recommended | C-07 | PASS | TABLE B cascade hops + TABLE E Cascade type rows |
| Recommended | C-08 | PASS | TABLE A numeric Limit column backed by Source register |
| Aspirational | C-09 | PASS | TABLE F Tradeoff column present |
| Aspirational | C-10 | PASS | TABLE A Failure mode controlled vocabulary; 5 failure mode types distinguished |
| Aspirational | C-11 | PASS | Source register with UNDOCUMENTED enforcement for uncited tiers |
| Aspirational | C-12 | PASS | Global criterion-coverage step covers C-01 to C-05 |
| Aspirational | C-13 | PASS | Step 1A SOURCE REGISTER appears before TABLE A |
| Aspirational | C-14 | PASS | [prose: item 2 — binding constraint exclusivity] present |
| Aspirational | C-15 | PASS | Three named phases; one-directional handoff statements |
| Aspirational | C-16 | PASS | PROHIBITED at each phase boundary |
| Aspirational | C-17 | PASS | "For each tier in TABLE A (C-17)" enumeration anchor |
| Aspirational | C-18 | PASS | All 7 violation-type annotations at anchor sites (Annot-01 through Annot-07) |
| Aspirational | C-19 | PASS | [prose: item 3 — global criterion-coverage verdict notes] |
| Aspirational | C-20 | PASS | Section A with closed prose-permitted declaration |
| Aspirational | C-21 | PASS | Source headers co-located at all derived tables |
| Aspirational | C-22 | PASS | TABLE E Type column (Burst/Cascade/RetryAfter) with per-type minimum |
| Aspirational | C-23 | PASS | [prose: item 1], [prose: item 2], [prose: item 3] inline authorization tags |
| Aspirational | C-24 | PASS | TYPE SCAN GATE with per-category verdicts and PROCEED/BLOCKED |
| Aspirational | C-25 | PASS | Section B structured-output register |
| Aspirational | C-26 | PASS | TYPE SCAN GATE 3-field purpose annotation (failure mode, gap above C-22, audit test) |
| Aspirational | C-27 | PASS | "No other element types are added to this register without revising this contract" |
| Aspirational | C-28 | PASS | Audit test with gate-present and gate-absent verification instructions |
| Aspirational | C-29 | PASS | Section B inertia annotation names implicit-complement inference + content-inspection chain |
| Aspirational | C-30 | PASS | "FLAT-LOAD: within nominal band" concrete unregistered example in inertia annotation |
| Aspirational | C-31 | PASS | Gate-present: 5 named observables with positions; gate-absent: 1 observable |
| Aspirational | C-32 | PASS | "Escape route for C-26" demolisher present in TYPE SCAN GATE |
| Aspirational | C-33 | PASS | "3 fields: Failure mode prevented \| Gap above C-25 \| Concrete example (C-29, C-30)" field-count header |
| Aspirational | C-34 | PASS | "Gate-present audit method — 5 observables:" and "Gate-absent signature — 1 observable:" count declared |
| Aspirational | C-35 | PASS | FORMAT CONTRACT with FORMAT CONTRACT COMPLETE statement at role-handoff |
| Aspirational | C-36 | PASS | Role 3 ACTIVATION CONDITIONS reference 5/1 observable counts |
| Aspirational | C-37 | **PASS** | Section C prose-list inventory (7 bullets, anchor ID + failure-mode label per entry), sealed before FORMAT CONTRACT COMPLETE |

**V-01 Composite: 235/235**

---

### V-02 — Output Format (Section C as table with Annot-ID column)

**C-37 evidence:** Section C is a four-column table: Annot-ID / Anchor site / Failure-mode label / Prohibited form (example). Header declares expected row count: 7. "A row absent from this table does not exist as a contract requirement. A row present in this table whose annotation is absent from its anchor site in the body is a FORMAT CONTRACT violation detectable by anchor-ID lookup without content scan." Closed with "This table is closed." Sealed before `FORMAT CONTRACT COMPLETE`.

The table form adds count-scan verifiability: expected 7 rows; a missing row is a count discrepancy without reading annotation text. This is enforcement above V-01's prose list, but C-37's pass condition does not distinguish forms — it requires anchor identifier and failure-mode label per entry, which the table provides.

All C-01 through C-36: carry from V-01 (identical structure). C-37: PASS.

**V-02 Composite: 235/235**

---

### V-03 — Phrasing Register (Section C with SHALL/PROHIBITED enforcement)

**C-37 evidence:** Section C uses SHALL/MUST/PROHIBITED register. Each entry carries "SHALL appear at: [anchor]" and "Failure-mode label: [label]" with "Required form" specification. Section header states: "The annotations below SHALL appear at the named anchor sites in the prompt body." Closes with PROHIBITED clause: "PROHIBITED: omitting any of the following annotations from its declared anchor site — *prevents annotation dropout; a missing annotation at its anchor site converts a detectable precision-site failure mode into a silent gap not recoverable at the handoff boundary*". Closed: "This inventory is closed." Sealed before `FORMAT CONTRACT COMPLETE`.

The PROHIBITED dropout clause converts each missing annotation from a content gap into a named prohibition violation. C-37's pass condition is met: each annotation is listed by anchor identifier and failure-mode label, sealed in FORMAT CONTRACT COMPLETE.

Role 2 instruction explicitly references: "Section C SHALL requirements apply to every column definition annotated in the inventory." This reinforces C-18 compliance.

All C-01 through C-36: carry from baseline. C-37: PASS.

**V-03 Composite: 235/235**

---

### V-04 — Role Sequence + Lifecycle (Role 2 activation references annotation inventory count)

**C-37 evidence:** Section C is a table (V-02 form). Additionally, Role 2 opens with ROLE 2 ACTIVATION CONDITIONS: "Role 2 activates only after FORMAT CONTRACT COMPLETE is stated AND the following annotation-inventory confirmation is completed at this boundary. Confirm all 7 Annot-IDs are present at their anchor sites before Phase 1 opens: (1) Annot-01 at TABLE A `Limit`... (7) Annot-07 at TABLE F `Setting or API parameter`... Any Annot-ID absent from its anchor site = Role 2 activation blocked."

Annotation dropout is now a role-activation failure: Role 2 cannot open Phase 1 if any annotation is missing. This is enforcement above V-02's contract-lock-only approach. C-37's pass condition is satisfied by the Section C table in FORMAT CONTRACT sealed before FORMAT CONTRACT COMPLETE.

The Role 2 activation conditions enforce C-37 at the domain-execution entry boundary rather than only at the handoff boundary.

All C-01 through C-36: carry from baseline. C-37: PASS.

**V-04 Composite: 235/235**

---

### V-05 — All Three + ANNOTATION SCAN GATE

**C-37 evidence:** Section C table + SHALL/PROHIBITED (V-02 + V-03 combined). "PROHIBITED: omitting any annotation from its declared anchor site — *prevents annotation dropout; a missing annotation converts a detectable precision-site failure mode into a silent gap; dropout is a FORMAT CONTRACT violation detectable at this inventory without body scan*". Role 2 activation pre-confirms all 7 Annot-IDs (V-04). Additionally: ANNOTATION SCAN GATE between Phase 1B (TABLE A) and Phase 2.

**ANNOTATION SCAN GATE structure:**
- Purpose annotation (3-field C-26 format):
  - Failure mode prevented: annotation dropout creating silent precision gaps in claims output
  - Gap above C-37: C-37 seals the inventory in FORMAT CONTRACT but does not require a construction-time enforcement gate; this gate ensures annotation dropout cannot be produced by any valid execution path
  - Audit test: 7 observables (Annot-01 through Annot-07 verdict lines before PROCEED/BLOCKED) + 1 gate-absent observable
- Per-annotation scan: Annot-01 through Annot-07 `[present? Y / N]`
- PROCEED if all Y; BLOCKED if any N
- Phase 2 PROHIBITED now reads: "PROHIBITED: opening Phase 2 before Phase 1B is complete AND the ANNOTATION SCAN GATE returns PROCEED. — *prevents annotation-dropout propagation into claims analysis*"

C-37 is satisfied by Section C in FORMAT CONTRACT. The ANNOTATION SCAN GATE is enforcement beyond what C-37 requires — it makes annotation dropout a construction-time blocking condition parallel to how the TYPE SCAN GATE makes category elision a construction-time blocking condition.

All C-01 through C-36: carry from baseline. C-37: PASS.

**V-05 Composite: 235/235**

---

## Summary Scorecard

| Variation | Essential (60) | Recommended (30) | Aspirational (145) | Composite | All Essential PASS? |
|-----------|---------------|------------------|--------------------|-----------|---------------------|
| V-01 | 60 | 30 | 145 | **235/235** | YES |
| V-02 | 60 | 30 | 145 | **235/235** | YES |
| V-03 | 60 | 30 | 145 | **235/235** | YES |
| V-04 | 60 | 30 | 145 | **235/235** | YES |
| V-05 | 60 | 30 | 145 | **235/235** | YES |

**All five variations reach the golden threshold (all essential PASS + composite >= 80).**

---

## Single-Axis Isolation Verdicts

| Comparison | Question | Answer |
|------------|----------|--------|
| V-01 vs V-02 | Does table form vs prose list affect C-37? | NO — both satisfy "anchor identifier + failure-mode label sealed in FORMAT CONTRACT COMPLETE" |
| V-01 vs V-03 | Does SHALL/PROHIBITED phrasing affect C-37? | NO — C-37 requires inventory existence by lookup, not normative enforcement register |
| V-02 vs V-04 | Does activation-condition wiring affect C-37 beyond contract sealing? | NO — C-37 is satisfied by the contract-lock alone; the activation-condition check is enforcement above what the criterion measures |

C-37 is format-agnostic at this threshold: prose list, table, and SHALL/PROHIBITED all satisfy the pass condition equally. The enforcement-strength ladder (V-01 < V-02 < V-03 < V-04 < V-05) is real but not rubric-distinguishable at v14.

---

## Ranking (by enforcement strength, rubric score tied)

1. **V-05** — Table + SHALL/PROHIBITED + Role 2 pre-confirmation + ANNOTATION SCAN GATE. Maximum enforcement: dropout is a construction-time blocking condition before Phase 2 opens.
2. **V-04** — Table + Role 2 activation conditions. Dropout = role-activation failure before Phase 1 opens.
3. **V-03** — SHALL/PROHIBITED register. Dropout = named prohibition violation.
4. **V-02** — Table with row count. Dropout detectable by count discrepancy.
5. **V-01** — Prose list. Dropout detectable by anchor-ID identifier check.

---

## Excellence Signals (from V-05)

**1. ANNOTATION SCAN GATE as a structurally complete gate type**
V-05's ANNOTATION SCAN GATE is architecturally complete: it has a purpose annotation (3-field C-26 format), per-annotation verdict lines, a PROCEED/BLOCKED decision, and Phase 2 PROHIBITED references the gate by name. This is not an ad-hoc check — it instantiates the full gate-pattern established by the TYPE SCAN GATE, generalized to a different coverage axis (annotation presence vs. type presence). Two gates in the prompt covering two independent failure modes, both with the same structural guarantee.

**2. Gap-above-C-37 framing**
The ANNOTATION SCAN GATE purpose annotation explicitly names "Gap above C-37" — the same framing pattern as the TYPE SCAN GATE's "Gap above C-22." This establishes a consistent meta-pattern: each gate explains why the contract mechanism above it (C-22 for type inventory, C-37 for annotation inventory) is insufficient without a construction-time enforcement gate. The pattern is now generalized: for any inventory sealed in FORMAT CONTRACT, a corresponding scan gate names the gap between contract-lock and construction-time blocking.

**3. Double-boundary annotation detection**
V-05 installs two annotation-dropout detection boundaries: Role 2 activation pre-confirmation (before any domain execution) and the ANNOTATION SCAN GATE (before Phase 2 opens). Neither boundary alone is sufficient to block all dropout scenarios — a malicious executor that passes Role 2 activation but drops an annotation mid-Phase-1 would be caught by the gate; a gate-absent execution that adds annotations only after claims are assembled would be caught at Role 2 activation. The two-boundary design eliminates both paths.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": ["ANNOTATION SCAN GATE: a structurally complete gate between Phase 1B and Phase 2 that blocks claims analysis if any C-18 annotation is absent from its anchor site, mirroring the TYPE SCAN GATE pattern and seeding a potential C-38 criterion for construction-time annotation-dropout blocking", "Gap-above-C-37 framing: the gate purpose annotation names the gap above C-37 (contract-lock without construction-time blocking) using the same three-field structure as C-26's gap-above-C-22 framing, establishing a generalized meta-pattern for gate-purpose annotations across any FORMAT CONTRACT inventory layer"]}
```
