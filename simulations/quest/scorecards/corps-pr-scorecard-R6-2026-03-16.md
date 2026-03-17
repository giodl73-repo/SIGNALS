Now I have enough to score all five variations. Let me compile the full evaluation.

---

# corps-pr Scorecard — Round 6 (v6 Rubric)

## Scoring Reference

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
Golden threshold: all 5 essential pass AND composite >= 80
```

---

## V-01 — Inertia Framing: C-19 Terminal Field Separation

**Structure**: Steps 1–5 + AMEND. No pipeline declaration.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 (E) | PASS | Routing table with exact org.yaml pattern per file; coverage gap block appended immediately |
| C-02 (E) | PASS | Domain-lens gate Step A/B enforces finding specificity; IA cost anchor requires named ledger row |
| C-03 (E) | PASS | Consensus template includes Divergence field with required Mechanism line |
| C-04 (E) | PASS | Exactly GO / NO-GO / GO WITH CONDITIONS; delegated/hedged decisions fail stated |
| C-05 (E) | PASS | Domain-lens gate: Step A binary test + Step B rewrite consequence with drop consequence |
| C-06 (R) | PASS | Coverage gap block with File / Reason fields appended immediately after table |
| C-07 (R) | PASS | Summary line "N findings — x P1, y P2, z P3" required per-role section |
| C-08 (R) | PASS | AMEND section uses named-field block (What was amended / Roles added / Roles removed / Files / Prior superseded) |
| C-09 (A) | PASS | Mechanism field required in Divergence block; names structural reason for divergence |
| C-10 (A) | PASS | Conditions block requires "sign-off: [role]" per condition |
| C-11 (A) | PASS | IA appears in Step 2 before Step 3 (structural, non-configurable); cost ledger makes it reference object |
| C-12 (A) | PASS | Mechanism field must name "specific code or architectural property" — ban on perspective labels reinforced |
| C-13 (A) | PASS | 5-item enumerated ban list with checkbox format; each phrase independently checkable |
| C-14 (A) | PASS | IA cost anchor block required per role citing named ledger row + Net direction |
| C-15 (A) | PASS | Domain-lens gate includes binary test + rewrite gate ("still NO after revision → drop") |
| C-16 (A) | PASS | AMEND section is named-field template, not prose instruction |
| C-17 (A) | PASS | Cost ledger with magnitude labels (LOW/MED/HIGH/CRITICAL) + cost terms; IA verdict in cost terms |
| C-18 (A) | **FAIL** | Numbered steps 1–5 lack named entry/exit conditions per step; no criteria-gates listed; no pipeline declaration |
| C-19 (A) | PASS | 4 rows × 2 columns + Net direction; separator (`---`) enforced structurally; Budget verdict + Budget strength as terminal declarations outside table; instruction "do not add a 5th cost row" explicit |
| C-20 (A) | **FAIL** | No pipeline entry condition naming IA phase completion; the prerequisite is stated inline ("this is a prerequisite, not a sequencing convention") but not as a named pipeline gate |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 10/12 → 8.33  
**Composite**: **98.33** | Golden: YES

---

## V-02 — Lifecycle Emphasis: C-20 Dual-Clause Entry Condition

**Structure**: Five-phase pipeline declaration (A–E) with named entry/exit conditions and criteria gates.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 (E) | PASS | Phase A routing table with exact org.yaml pattern; coverage gap inline |
| C-02 (E) | PASS | Domain-lens gate enforced as Phase C exit condition; Step A/B with drop consequence |
| C-03 (E) | PASS | Phase D consensus includes Divergence + Mechanism field |
| C-04 (E) | PASS | Phase E: exactly one GO/NO-GO/GO WITH CONDITIONS; delegated fails |
| C-05 (E) | PASS | Domain-lens gate binary test + rewrite consequence as Phase C exit condition |
| C-06 (R) | PASS | Coverage gap with named output fields immediately after Phase A table |
| C-07 (R) | PASS | Per-role "Summary: N findings — x P1, y P2, z P3" in Phase C template |
| C-08 (R) | PASS | AMEND block with all five named fields before Phase A |
| C-09 (A) | PASS | Phase D Mechanism field: "structural or architectural property of the code causing the difference" |
| C-10 (A) | PASS | Phase E conditions: "sign-off: [role who confirms before merge]" per condition |
| C-11 (A) | PASS | Phase B (IA) precedes Phase C (technical roles) in pipeline; Phase B output is reference object for Phase C anchors |
| C-12 (A) | PASS | Mechanism field required; ban-to-fix table reinforces prohibition |
| C-13 (A) | PASS | 5-row ban-to-fix substitution table with Banned → Required replacement form; each row independently checkable |
| C-14 (A) | PASS | Phase C template requires IA cost anchor naming specific Phase B ledger row; C14 gated in Phase C |
| C-15 (A) | PASS | Domain-lens gate Step A binary test + Step B rewrite gate declared as Phase C exit condition |
| C-16 (A) | PASS | AMEND block is a named-field template with enumerated slots |
| C-17 (A) | PASS | Phase B cost ledger with quantified magnitude + cost terms; IA verdict in cost terms (B5) |
| C-18 (A) | PASS | Named phases A–E; each has explicit entry/exit conditions; criteria listed per phase (e.g., Phase C gates C-02, C-05, C-07, C-14, C-15, C-18, C-20); domain-lens gate named as Phase C exit |
| C-19 (A) | PASS | Phase B exit condition B2 requires 4 named rows × 2 named columns × Net direction; B3/B4 require Budget verdict + Budget strength as terminal fields "below the cost table" |
| C-20 (A) | PASS | Phase C entry is two named sub-conditions: C1 (Phase B exit verification, B1–B5 checklist) and C2 (per-role IA read prerequisite requiring named row + Net direction + Budget strength citation); C1 is pre-flight, C2 is per-role; each independently auditable |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 12/12 → 10  
**Composite**: **100** | Golden: YES

---

## V-03 — Role Sequence: IA Read-Receipt as Per-Role Structural Prefix

**Structure**: Steps 1–5 with sub-steps 3A → 3B → 3C. No pipeline declaration. C-20 satisfied via per-role READ RECEIPT output artifact.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 (E) | PASS | Routing table in Step 1 with exact org.yaml scope pattern |
| C-02 (E) | PASS | Domain-lens gate Step A/B + domain-lens column in findings table |
| C-03 (E) | PASS | Step 4 consensus with Mechanism field per divergence |
| C-04 (E) | PASS | Step 5 decision: one value, no delegation, no hedging |
| C-05 (E) | PASS | Domain-lens gate Step A binary test + Step B rewrite gate in 3B |
| C-06 (R) | PASS | Coverage gap block with File / Reason fields |
| C-07 (R) | PASS | Per-role summary "N findings — x P1, y P2, z P3" in 3C template |
| C-08 (R) | PASS | AMEND SCOPE named-field block with all required fields |
| C-09 (A) | PASS | Consensus Mechanism field requires architectural code property |
| C-10 (A) | PASS | Recommendation conditions include "sign-off: [role]" |
| C-11 (A) | PASS | IA in Step 2 before Step 3; structured as reference object (null hypothesis + cost ledger + verdict) |
| C-12 (A) | PASS | Mechanism must name code property; ban-to-fix table enforces substitution |
| C-13 (A) | PASS | 5-row ban-to-fix substitution table with replacement forms in Step 4 |
| C-14 (A) | PASS | IA READ RECEIPT block (3A) + IA cost anchor (3C) both require named ledger row citation with Net direction; stronger than C-14 baseline |
| C-15 (A) | PASS | Domain-lens gate Step A binary test + Step B rewrite consequence; Domain-Lens column in findings table makes compliance visible per finding |
| C-16 (A) | PASS | AMEND MODE block with named-field template |
| C-17 (A) | PASS | Cost ledger with magnitude + cost terms; Budget verdict in cost terms |
| C-18 (A) | **FAIL** | Steps 1–5 without named entry/exit conditions; sub-steps 3A/3B/3C are within Step 3 not separate phase gates; "complete before proceeding to step 4" is prose, not named exit condition with criteria gates listed |
| C-19 (A) | PASS | Step 2 template: 4 rows × 2 columns + Net direction; separator (`---`) enforced; Budget verdict + Budget strength declared as terminal fields; "do not embed them as additional rows" explicit |
| C-20 (A) | **FAIL** | No pipeline entry condition naming IA phase completion; per-role READ RECEIPT block is strong evidence of C-14 compliance but does not satisfy C-20's requirement for a named pipeline entry condition declaring IA phase exit + read prerequisite |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 10/12 → 8.33  
**Composite**: **98.33** | Golden: YES

---

## V-04 — Combined: C-19 Terminal Field Schema + C-20 Dual-Clause Pipeline

**Structure**: Five-phase pipeline (A–E), C1 pre-flight checklist rendered as output artifact, C2 requires Net direction citation (the C-19 proof token). Chain: Phase B fills Net direction per row → Phase C C1 verifies those fields → Phase C C2 requires citing a Net direction value.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 (E) | PASS | Phase A routing table with exact scope pattern; coverage gap inline |
| C-02 (E) | PASS | Domain-lens gate as Phase C exit condition |
| C-03 (E) | PASS | Phase D divergence Mechanism field |
| C-04 (E) | PASS | Phase E one-decision requirement |
| C-05 (E) | PASS | Domain-lens gate Step A/B as Phase C exit |
| C-06 (R) | PASS | Coverage gap with `COVERAGE GAP: [file] — no org.yaml scope pattern covers this path` |
| C-07 (R) | PASS | Per-role summary in Phase C template |
| C-08 (R) | PASS | AMEND block with named fields before Phase A |
| C-09 (A) | PASS | Phase D Mechanism field; ban-to-fix table in Phase D |
| C-10 (A) | PASS | Phase E conditions with named sign-off role per condition |
| C-11 (A) | PASS | Phase B before Phase C; cost ledger structured as reference object |
| C-12 (A) | PASS | Mechanism field + ban-to-fix table |
| C-13 (A) | PASS | 5-row ban-to-fix substitution table in Phase D |
| C-14 (A) | PASS | Phase C IA cost anchor requires Phase B ledger row + Net direction + Budget strength citation |
| C-15 (A) | PASS | Domain-lens gate binary test + rewrite gate as Phase C exit condition |
| C-16 (A) | PASS | AMEND block named-field template |
| C-17 (A) | PASS | Phase B cost ledger with cost terms; IA verdict in cost terms (B5) |
| C-18 (A) | PASS | Named phases A–E with explicit entry/exit conditions and criteria gates; domain-lens gate declared as Phase C exit |
| C-19 (A) | PASS | Phase B exit B2 names "4 named rows × 2 named columns × Net direction per row"; B3/B4 explicitly require Budget verdict + Budget strength as terminal fields "below the cost table — not as additional table rows"; C1 pre-flight checklist enumerates B3/B4 compliance verbatim |
| C-20 (A) | PASS | Phase C entry: C1 is pre-flight checklist (output artifact, independently auditable); C2 per-role requires citing "a specific Phase B ledger row name, that row's Net direction from Phase B, and Budget strength from Phase B terminal field." Net direction value only exists in Phase B table — citation is mechanical proof of read |

**Excellence note**: C-19 compliance is the C-20 verification mechanism. The Net direction column (required by C-19) is the proof token for C-20 C2. The C1 pre-flight checklist is rendered as a visible output block — Phase B exit becomes auditable post-hoc without reconstructing the pipeline intent.

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 12/12 → 10  
**Composite**: **100** | Golden: YES

---

## V-05 — Combined: C-19 Terminal Field Schema + Per-Role Read Receipt + Ban-to-Fix

**Structure**: Steps 1–5 (Step 6 = AMEND). No pipeline declaration. C-20 via per-role READ RECEIPT (same approach as V-03). Adds Domain-Lens column in findings table. Consensus rendered as a named-column table.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 (E) | PASS | Routing table Step 1 with exact org.yaml scope pattern |
| C-02 (E) | PASS | Domain-lens gate Step A/B; Domain-Lens column in findings table makes gate compliance visible per finding |
| C-03 (E) | PASS | Step 4 consensus table with Divergence row and Mechanism/Notes column |
| C-04 (E) | PASS | Step 5 recommendation block: one decision, no delegation, no hedging |
| C-05 (E) | PASS | Domain-lens gate Step A binary test + Step B rewrite consequence; additionally materialized as output column |
| C-06 (R) | PASS | Coverage gap block with File / Reason fields |
| C-07 (R) | PASS | "Summary: N findings — x P1, y P2, z P3" in 3C template |
| C-08 (R) | PASS | Step 6 AMEND SCOPE named-field block with all required fields |
| C-09 (A) | PASS | Consensus table Mechanism/Notes column captures root cause for divergent findings |
| C-10 (A) | PASS | Step 5 "Sign-off roles" named field per condition |
| C-11 (A) | PASS | IA in Step 2 before Step 3; null hypothesis strength field added; structured as reference object |
| C-12 (A) | PASS | Mechanism/Notes column must name architectural code property; ban-to-fix table enforces substitution |
| C-13 (A) | PASS | 5-row ban-to-fix substitution table in Step 4 with replacement forms; "each row is independently checkable" explicit |
| C-14 (A) | PASS | IA READ RECEIPT 3A requires named row + Net direction citation; IA cost anchor 3C restates final position |
| C-15 (A) | PASS | Domain-lens gate Step A/B + Domain-Lens column materializes gate result per finding |
| C-16 (A) | PASS | AMEND SCOPE block (Step 6) uses named-field template |
| C-17 (A) | PASS | Cost ledger with magnitude labels and cost terms; Budget verdict in cost terms |
| C-18 (A) | **FAIL** | Steps 1–5 with sub-steps; no named phase-gate structure with entry/exit conditions and criteria gates |
| C-19 (A) | PASS | Step 2 template: 4 rows × 2 columns + Net direction; separator + terminal fields; null hypothesis strength added as named field; explicit "do not embed them as table rows" |
| C-20 (A) | **FAIL** | Per-role READ RECEIPT is a strong output artifact for C-14 but does not constitute a pipeline entry condition naming IA phase completion; same failure mode as V-03 |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: 10/12 → 8.33  
**Composite**: **98.33** | Golden: YES

---

## Summary Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (E) | P | P | P | P | P |
| C-02 (E) | P | P | P | P | P |
| C-03 (E) | P | P | P | P | P |
| C-04 (E) | P | P | P | P | P |
| C-05 (E) | P | P | P | P | P |
| C-06 (R) | P | P | P | P | P |
| C-07 (R) | P | P | P | P | P |
| C-08 (R) | P | P | P | P | P |
| C-09 (A) | P | P | P | P | P |
| C-10 (A) | P | P | P | P | P |
| C-11 (A) | P | P | P | P | P |
| C-12 (A) | P | P | P | P | P |
| C-13 (A) | P | P | P | P | P |
| C-14 (A) | P | P | P | P | P |
| C-15 (A) | P | P | P | P | P |
| C-16 (A) | P | P | P | P | P |
| C-17 (A) | P | P | P | P | P |
| C-18 (A) | **F** | P | **F** | P | **F** |
| C-19 (A) | P | P | P | P | P |
| C-20 (A) | **F** | P | **F** | P | **F** |
| **Score** | **98.33** | **100** | **98.33** | **100** | **98.33** |
| Golden | YES | YES | YES | YES | YES |

**Ranking**: V-02 = V-04 (100) > V-01 = V-03 = V-05 (98.33)

---

## Excellence Signals — Top Variations (V-02, V-04)

Both V-02 and V-04 achieve a perfect score. V-04 introduces three patterns that go beyond V-02 without adding new criterion passes under v6:

**Pattern 1 — Phase B exit as output checklist artifact**
V-04 renders the Phase C C1 pre-flight as a checkable output block (with literal `[ ]` boxes against B1–B5). This makes Phase B exit compliance visible and auditable post-hoc — a reader can verify the checklist was completed without reconstructing the pipeline intent. V-02 declares the same condition but does not render it as an output artifact.

**Pattern 2 — Net direction citation as C-20 proof token**
V-04 explicitly chains C-19 and C-20: Phase B must fill Net direction per row (C-19 requirement) → Phase C C2 requires citing a specific Net direction value → citing that value is mechanical proof the role read Phase B. The proof is unforgeable: a role cannot fabricate a Net direction value that wasn't in Phase B. V-02 requires similar anchoring but does not foreground the chaining logic.

**Pattern 3 — Consensus rendered as a named-column table (V-05 contribution)**
V-05 restructures the consensus section as a table with named columns (Signal, Finding Area, Roles, Mechanism/Notes). This makes agreement/divergence/critical findings row-auditable rather than requiring prose parsing. The ban-to-fix substitution applies to the Mechanism/Notes cell, making the prohibited phrase check per-cell rather than per-paragraph. This pattern does not yet have a rubric criterion — it is a structural format upgrade to C-03/C-09/C-12.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase B exit rendered as output checklist artifact (C1 pre-flight as visible checked list, not only a declared condition)", "Net direction citation as mechanical C-20 proof token — value only exists in Phase B, so citing it is unforgeable read evidence", "Consensus rendered as named-column table (Signal / Finding Area / Roles / Mechanism) making agreement and divergence row-auditable"]}
```
