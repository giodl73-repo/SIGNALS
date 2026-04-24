## mock-review R10 Scorecard

**Score Summary**

| Variant | Aspirational credit | Total |
|---------|---------------------|-------|
| V-05 | 23.0 / 23 | **100.00** |
| V-04 | 19.5 / 23 | **98.48** |
| V-01 | 17.0 / 23 | **97.39** |
| V-02 | 16.5 / 23 | **97.17** |
| V-03 | 10.0 / 23 | **94.35** |

All variants pass all 5 essential and 3 recommended criteria (90 pts base). Differentiation is entirely aspirational.

**Key scoring logic:**
- **V-01** (PHASE GATE + C-31): gains C-31 PASS; blocked by no step labels (C-28 FAIL), no C-30, no C-26. Partial on C-21/C-23/C-24/C-25.
- **V-02** (step anchors + C-30): gains C-30/C-28 PASS; blocked by distributed TRIAD (C-29 FAIL), no C-31, no C-26. C-17 PARTIAL (no phase gate).
- **V-03** (minimal + C-25): C-25 fix lands; eleven aspirational FAIL including C-14, C-17, C-18, C-21, C-24 entirely absent.
- **V-04** (combined + Strategy-first): all R10 additions present; ceiling gap = C-16 (canary prohibition) and C-26 (Architect-first) only.
- **V-05** (full ceiling): 31/31 PASS. C-30 and C-31 integrate cleanly; canary prohibition, SQ structural signal, artifact state propagation, and two-layer contamination error taxonomy all present.

**Excellence signals** written to `simulations/quest/scorecards/mock-review-scorecard-R10-2026-03-15.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Citation sub-field within template slot encodes SQ-1 tier decision as a required slot output rather than a conceptual instruction — author must name the specific tier decision being supported (C-30)", "Cardinality declaration at block header converts completeness verification from counting entries to a header-level assertion — reviewer confirms count by reading the header, then verifies each entry matches (C-31)"]}
```
orbidden outputs. |
| C-12 Zero-remaining confirmation gate | PASS | Explicit verification step in write-back phase. |
| C-13 Verifiable role-step separation | PASS | PM, Architect, Strategy have own headings, sub-questions, required verdicts. |
| C-14 Sub-question answer citation in verdict traceability | PASS | REAL-REQUIRED decisions name specific SQ answer driving verdict. |
| C-15 Entity-naming sub-question grammar | PASS | "Name X" / "What specific X" forms throughout. |
| C-16 Canary confirmation (prohibited under failure) | FAIL | Confirmation gate present (C-12 PASS) but no named prohibition when condition not met. Canary inversion not declared. |
| C-17 Auto-flagged contamination guard | PASS | PHASE GATE includes explicit "DO NOT apply evaluation to auto-flagged namespace" statement. |
| C-18 Inter-step gate with next-step reference | PASS | Gates name specific next evaluation step being blocked by descriptive role label. |
| C-19 Structured trigger notation | PASS | Rule trigger in named parseable template field at fixed position. |
| C-20 Contrastive MOCK-ACCEPTED rationale | PASS | Contrastive sentence distinguishes namespace state from threshold requiring real evidence. |
| C-21 SQ answer structural signal | PARTIAL | SQ citation form present; structural rule naming present-tense artifact naming as the distinguishing form not declared. "Verdict echo" error not named. |
| C-22 Decision inversion framing | PASS | Named DEFAULT DECISION POSITION block at skill level. |
| C-23 Strategy SQ-1 anchor in structural position | PARTIAL | SQ-1 named as conceptual source of structural position; slot grammar does not declare SQ-1 as a required input field. |
| C-24 Artifact state field propagation into next-steps | PARTIAL | Artifact state defined in REAL-REQUIRED decision block; next-steps format does not require propagated artifact state field. |
| C-25 Dedicated contrast sub-slot in MOCK-ACCEPTED template | PARTIAL | Contrastive framing instructions present; labeled `Contrast:` sub-slot structurally separate from `Structural position` slot not declared. Single-slot escape not closed. |
| C-26 Role-sequence gate as contamination control | FAIL | Strategy-first; no Architect-first gate naming `architect-verdict = CONTRADICTS-ARCHITECTURE` as PM suppressor. |
| C-27 Triad DO NOT coverage (complete forbidden-output set) | PASS | All three rules have individually labeled DO NOT statements. |
| C-28 Step-name anchor in forward reference | FAIL | No step labels; forward references name role descriptively but carry no step number + label pair. |
| C-29 Phase-gate co-location of forbidden-output block | PASS | TRIAD block co-located with PHASE GATE at phase boundary. |
| C-30 SQ-1 sourcing label in Structural position slot | FAIL | No `Feeds tier decision: [Strategy SQ-1 answer]` citation sub-field in template definition. |
| C-31 TRIAD header declares cardinality | PASS | TRIAD header carries "(3 rules, all required)". |

**Essential**: 5/5 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: PASS=15, PARTIAL=4 (×0.5=2.0), FAIL=4 → 17.0/23 × 10 = **7.39**
**Total: 97.39**

---

## V-02 — output-format (step-name anchors, distributed TRIAD, Strategy-first, + C-30)

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | PASS | All namespaces decided. |
| C-02 Automatic rule correctness | PASS | Hard gate / STOP instruction before role evaluation. |
| C-03 MOCK-ACCEPTED reason code present | PASS | Exact codes used. |
| C-04 Status fields written back | PASS | Mandatory write-back phase. |
| C-05 Next-steps priority order | PASS | Ordering rule stated explicitly. |
| C-06 Rule trigger named per REAL-REQUIRED | PASS | Rule trigger recorded per auto-flagged namespace. |
| C-07 PM/Architect/Strategy evaluation shown | PASS | All three roles evaluated. |
| C-08 Tier flag respected | PASS | Tier stated with source; TIER-CRITICAL applied. |
| C-09 Coverage gap synthesis | PASS | Risk statement and urgency grouping in next-steps. |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | PASS | Per-namespace explanatory sentence. |
| C-11 Forbidden-output enumeration for auto-rules | PASS | Forbidden outputs enumerated. |
| C-12 Zero-remaining confirmation gate | PASS | Verification step present. |
| C-13 Verifiable role-step separation | PASS | Separate headings, sub-questions, verdicts per role. |
| C-14 Sub-question answer citation in verdict traceability | PASS | REAL-REQUIRED decisions cite specific SQ answer. |
| C-15 Entity-naming sub-question grammar | PASS | "Name X" / "What specific X" grammar. |
| C-16 Canary confirmation (prohibited under failure) | FAIL | No named prohibition when condition not met. |
| C-17 Auto-flagged contamination guard | PARTIAL | No PHASE GATE; contamination concept present (rule described) but explicit "DO NOT apply evaluation to auto-flagged namespace" not co-located at a phase boundary — distributed rule descriptions rather than a named guard statement. |
| C-18 Inter-step gate with next-step reference | PASS | Step-name anchors enable forward references naming the blocked step by number and label. |
| C-19 Structured trigger notation | PASS | Trigger in named template field at fixed position. |
| C-20 Contrastive MOCK-ACCEPTED rationale | PASS | Contrastive sentence present. |
| C-21 SQ answer structural signal | PARTIAL | SQ citation present; positive structural form rule and "verdict echo" error not declared. |
| C-22 Decision inversion framing | PASS | DEFAULT DECISION POSITION block present. |
| C-23 Strategy SQ-1 anchor in structural position | PARTIAL | SQ-1 referenced conceptually; slot grammar does not encode it as required input field. |
| C-24 Artifact state field propagation into next-steps | PARTIAL | Artifact state in decision block; not required in next-steps entry format. |
| C-25 Dedicated contrast sub-slot in MOCK-ACCEPTED template | PARTIAL | Contrastive framing present; labeled `Contrast:` sub-slot not structurally declared. |
| C-26 Role-sequence gate as contamination control | FAIL | Strategy-first; no Architect-first guard. |
| C-27 Triad DO NOT coverage (complete forbidden-output set) | PASS | All three rules have labeled DO NOT statements. |
| C-28 Step-name anchor in forward reference | PASS | Step-name anchors present; forward references carry step number and label. |
| C-29 Phase-gate co-location of forbidden-output block | FAIL | Distributed TRIAD across role steps; no single co-located block at phase boundary. |
| C-30 SQ-1 sourcing label in Structural position slot | PASS | `Feeds tier decision: [Strategy SQ-1 answer]` citation sub-field in template definition. |
| C-31 TRIAD header declares cardinality | FAIL | TRIAD present but header does not declare count. |

**Essential**: 5/5 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: PASS=14, PARTIAL=5 (×0.5=2.5), FAIL=4 → 16.5/23 × 10 = **7.17**
**Total: 97.17**

---

## V-03 — inertia-framing (minimal, Strategy-first, inline TRIAD, no PHASE GATE, no step labels, + C-25 fix)

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | PASS | All namespaces decided. |
| C-02 Automatic rule correctness | PASS | Auto rules fire before evaluation via STOP instruction. |
| C-03 MOCK-ACCEPTED reason code present | PASS | Exact codes used. |
| C-04 Status fields written back | PASS | Write-back phase present. |
| C-05 Next-steps priority order | PASS | Ordering rule stated. |
| C-06 Rule trigger named per REAL-REQUIRED | PASS | Trigger recorded per auto-flagged decision. |
| C-07 PM/Architect/Strategy evaluation shown | PASS | All three roles evaluated. |
| C-08 Tier flag respected | PASS | Tier applied correctly. |
| C-09 Coverage gap synthesis | PARTIAL | Priority ordering present; cross-namespace risk synthesis and urgency grouping commentary absent in this minimal variant. |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | PASS | Per-namespace rationale present. |
| C-11 Forbidden-output enumeration for auto-rules | PASS | DO NOT statements in inline TRIAD. |
| C-12 Zero-remaining confirmation gate | PASS | Confirmation gate present. |
| C-13 Verifiable role-step separation | PASS | Separate role sections with headings and verdicts. |
| C-14 Sub-question answer citation in verdict traceability | FAIL | Minimal variant; REAL-REQUIRED decisions name the failing verdict but specific SQ answer citation not present. |
| C-15 Entity-naming sub-question grammar | PASS | "Name X" form used. |
| C-16 Canary confirmation (prohibited under failure) | FAIL | No canary prohibition. |
| C-17 Auto-flagged contamination guard | FAIL | No PHASE GATE; no explicit "DO NOT apply evaluation to auto-flagged namespace" statement. Auto-rule firing and evaluation separation handled procedurally only. |
| C-18 Inter-step gate with next-step reference | FAIL | No step labels; gates do not name the blocked next step. |
| C-19 Structured trigger notation | PARTIAL | Inline TRIAD present; trigger notation embedded in prose rather than a named parseable template field. |
| C-20 Contrastive MOCK-ACCEPTED rationale | PASS | Contrastive framing instruction applied. |
| C-21 SQ answer structural signal | FAIL | No SQ answer citation form; no structural rule; "verdict echo" error not named. |
| C-22 Decision inversion framing | PARTIAL | Inversion concept present in prose; no named DEFAULT DECISION POSITION block at skill level. |
| C-23 Strategy SQ-1 anchor in structural position | PARTIAL | SQ-1 referenced conceptually; no slot-level anchor. |
| C-24 Artifact state field propagation into next-steps | FAIL | Artifact state field absent; traceability chain not established. |
| C-25 Dedicated contrast sub-slot in MOCK-ACCEPTED template | PASS | `RATIONALE TEMPLATE (2 required slots — both must be populated)` with numbered (1)/(2) labels and RATIONALE INCOMPLETE error name. Two-slot structure enforces contrast. |
| C-26 Role-sequence gate as contamination control | FAIL | Strategy-first; no Architect-first guard. |
| C-27 Triad DO NOT coverage (complete forbidden-output set) | PASS | All three rules labeled in inline TRIAD. |
| C-28 Step-name anchor in forward reference | FAIL | No step labels. |
| C-29 Phase-gate co-location of forbidden-output block | FAIL | No PHASE GATE; TRIAD inline within role steps. |
| C-30 SQ-1 sourcing label in Structural position slot | FAIL | No `Feeds tier decision:` citation sub-field. |
| C-31 TRIAD header declares cardinality | FAIL | No cardinality declared in header. |

**Essential**: 5/5 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: PASS=8, PARTIAL=4 (×0.5=2.0), FAIL=11 → 10.0/23 × 10 = **4.35**
**Total: 94.35**

---

## V-04 — lifecycle-emphasis + output-format (PHASE GATE + step-name anchors + C-30 + C-31 + C-25, Strategy-first)

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | PASS | All namespaces decided. |
| C-02 Automatic rule correctness | PASS | PHASE GATE hard gate before evaluation. |
| C-03 MOCK-ACCEPTED reason code present | PASS | Exact codes used. |
| C-04 Status fields written back | PASS | Write-back phase. |
| C-05 Next-steps priority order | PASS | Ordering rule explicit. |
| C-06 Rule trigger named per REAL-REQUIRED | PASS | Trigger recorded per decision. |
| C-07 PM/Architect/Strategy evaluation shown | PASS | All three roles evaluated. |
| C-08 Tier flag respected | PASS | Tier stated with source; gate applied correctly. |
| C-09 Coverage gap synthesis | PASS | Risk statement and urgency grouping in next-steps. |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | PASS | Per-namespace rationale. |
| C-11 Forbidden-output enumeration for auto-rules | PASS | DO NOT statements in TRIAD. |
| C-12 Zero-remaining confirmation gate | PASS | Zero-remaining verification step. |
| C-13 Verifiable role-step separation | PASS | Separate headings, sub-questions, verdicts per role. |
| C-14 Sub-question answer citation in verdict traceability | PASS | REAL-REQUIRED decisions cite specific SQ answer. |
| C-15 Entity-naming sub-question grammar | PASS | "Name X" / "What specific X" forms. |
| C-16 Canary confirmation (prohibited under failure) | FAIL | Confirmation gate present; no canary prohibition declared. |
| C-17 Auto-flagged contamination guard | PASS | PHASE GATE includes explicit "DO NOT apply evaluation to auto-flagged namespace" guard. |
| C-18 Inter-step gate with next-step reference | PASS | Step-name anchors enable forward references naming step number and label. |
| C-19 Structured trigger notation | PASS | Named template field at fixed position. |
| C-20 Contrastive MOCK-ACCEPTED rationale | PASS | Contrastive sentence present. |
| C-21 SQ answer structural signal | PARTIAL | SQ citation and template present; structural rule naming positive form and "verdict echo" error not explicitly declared. |
| C-22 Decision inversion framing | PASS | Named DEFAULT DECISION POSITION block. |
| C-23 Strategy SQ-1 anchor in structural position | PARTIAL | `Feeds tier decision:` sub-field present (satisfies C-30); slot label does not independently declare SQ-1 as a named sourcing requirement — sub-field carries the mechanical anchor but the slot label does not state "required input: Strategy SQ-1 tier decision" separately. |
| C-24 Artifact state field propagation into next-steps | PARTIAL | Artifact state in decision block; next-steps entry format does not require propagated artifact state field. |
| C-25 Dedicated contrast sub-slot in MOCK-ACCEPTED template | PASS | `RATIONALE TEMPLATE (2 required slots)` with labeled (1) Structural position and (2) Contrast: sub-slots declared. |
| C-26 Role-sequence gate as contamination control | FAIL | Strategy-first; no Architect-first cross-step guard naming `architect-verdict = CONTRADICTS-ARCHITECTURE`. |
| C-27 Triad DO NOT coverage (complete forbidden-output set) | PASS | All three rules with individually labeled DO NOT statements. |
| C-28 Step-name anchor in forward reference | PASS | Step number + label in all forward references. |
| C-29 Phase-gate co-location of forbidden-output block | PASS | TRIAD block co-located with PHASE GATE at phase boundary. |
| C-30 SQ-1 sourcing label in Structural position slot | PASS | `Feeds tier decision: [Strategy SQ-1 answer]` citation sub-field in template definition. |
| C-31 TRIAD header declares cardinality | PASS | "(3 rules, all required)" in TRIAD header. |

**Essential**: 5/5 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: PASS=18, PARTIAL=3 (×0.5=1.5), FAIL=2 → 19.5/23 × 10 = **8.48**
**Total: 98.48**

---

## V-05 — full ceiling (Architect-first + all V-04 additions + SQ structural signal + canary prohibition + artifact state propagation + guard-distinctness)

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | PASS | All namespaces decided; no skip. |
| C-02 Automatic rule correctness | PASS | PHASE GATE hard gate; rules fire before any role evaluation. |
| C-03 MOCK-ACCEPTED reason code present | PASS | Exact codes per MOCK-ACCEPTED decision. |
| C-04 Status fields written back | PASS | Mandatory write-back phase with in-place edit requirement. |
| C-05 Next-steps priority order | PASS | Ordering rule explicit; critical first, evidence-heavy last. |
| C-06 Rule trigger named per REAL-REQUIRED | PASS | Auto-flag rule and evaluation verdict both named per decision. |
| C-07 PM/Architect/Strategy evaluation shown | PASS | All three roles with sub-questions and verdicts. |
| C-08 Tier flag respected | PASS | Tier stated with source; TIER-CRITICAL gate correct. |
| C-09 Coverage gap synthesis | PASS | Cross-namespace risk statement and urgency grouping. |
| C-10 Namespace-specific MOCK-ACCEPTED rationale | PASS | Per-namespace rationale sentence. |
| C-11 Forbidden-output enumeration for auto-rules | PASS | All three rules have named DO NOT statements. |
| C-12 Zero-remaining confirmation gate | PASS | Zero-remaining verification required in write-back phase. |
| C-13 Verifiable role-step separation | PASS | PM, Architect, Strategy each independently completable with own heading, sub-questions, required verdict. |
| C-14 Sub-question answer citation in verdict traceability | PASS | REAL-REQUIRED decisions name specific SQ answer via SQ answer driving verdict field. |
| C-15 Entity-naming sub-question grammar | PASS | "Name X" / "What specific X" forms throughout. |
| C-16 Canary confirmation (prohibited under failure) | PASS | Confirmation declared as canary; writing it when condition not met is a named canary violation error. |
| C-17 Auto-flagged contamination guard | PASS | PHASE GATE names "DO NOT apply evaluation to auto-flagged namespace"; guard-distinctness note explicitly separates AUTO-RULE CONTAMINATION from GUARD-BYPASS CONTAMINATION as two named error types. |
| C-18 Inter-step gate with next-step reference | PASS | Gates name specific blocked next step with descriptive label. |
| C-19 Structured trigger notation | PASS | Named parseable template field at fixed position. |
| C-20 Contrastive MOCK-ACCEPTED rationale | PASS | Contrastive sentence distinguishes namespace state from threshold for real evidence. |
| C-21 SQ answer structural signal | PASS | Template provides positive structural form (present-tense artifact naming); "verdict echo" error named; structural rule distinguishing genuine SQ answer from verdict restatement declared. |
| C-22 Decision inversion framing | PASS | Named DEFAULT DECISION POSITION block at skill level. |
| C-23 Strategy SQ-1 anchor in structural position | PASS | Structural position slot labels SQ-1 as sourcing requirement; `Feeds tier decision: [Strategy SQ-1 answer]` sub-field present; slot grammar declares SQ-1 as its input requirement. |
| C-24 Artifact state field propagation into next-steps | PASS | Artifact state propagates end-to-end: SQ answer → artifact state field → verdict → next-steps entry `/{skill-id} {topic} — {artifact state}`. |
| C-25 Dedicated contrast sub-slot in MOCK-ACCEPTED template | PASS | Two-slot RATIONALE TEMPLATE with labeled (1) Structural position and (2) Contrast: sub-slots; RATIONALE INCOMPLETE error declared. |
| C-26 Role-sequence gate as contamination control | PASS | Architect runs before PM; cross-step guard names `architect-verdict = CONTRADICTS-ARCHITECTURE` as trigger; PM Evaluation named as suppressed step. Guard distinguished from C-17 auto-rule contamination guard. |
| C-27 Triad DO NOT coverage (complete forbidden-output set) | PASS | All three rules carry individually labeled DO NOT statements. |
| C-28 Step-name anchor in forward reference | PASS | All gates carry step number + descriptive label (e.g., "DO NOT proceed to Step 3 (PM Evaluation) until..."). |
| C-29 Phase-gate co-location of forbidden-output block | PASS | TRIAD block co-located with PHASE GATE at phase boundary; independent of role ordering. |
| C-30 SQ-1 sourcing label in Structural position slot | PASS | `Feeds tier decision: [Strategy SQ-1 answer]` citation sub-field in template definition; SQ-1 answer mechanically captured as required slot output. |
| C-31 TRIAD header declares cardinality | PASS | Header: "FORBIDDEN OUTPUTS TRIAD (3 rules, all required)" — cardinality asserted at block level. |

**Essential**: 5/5 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: PASS=23, PARTIAL=0, FAIL=0 → 23/23 × 10 = **10.00**
**Total: 100.00**

---

## Score Summary

| Variant | Essential | Recommended | Aspirational | Total |
|---------|-----------|-------------|--------------|-------|
| V-05 | 60.00 | 30.00 | 10.00 | **100.00** |
| V-04 | 60.00 | 30.00 | 8.48 | **98.48** |
| V-01 | 60.00 | 30.00 | 7.39 | **97.39** |
| V-02 | 60.00 | 30.00 | 7.17 | **97.17** |
| V-03 | 60.00 | 30.00 | 4.35 | **94.35** |

---

## Ranking

1. **V-05 — 100.00** Full ceiling. All 31 criteria PASS. Architect-first guard with named verdict trigger, SQ structural signal with positive form rule, canary prohibition as named error, end-to-end artifact state traceability, two-layer contamination error taxonomy. R10 additions (C-30, C-31, C-25) fully integrated.
2. **V-04 — 98.48** All R10 structural additions present. PHASE GATE + step-name anchors. Blocked only by C-16 (canary prohibition) and C-26 (Architect-first guard). C-21/C-23/C-24 partial — SQ structural signal and artifact state propagation absent.
3. **V-01 — 97.39** PHASE GATE axis with C-31 cardinality declaration. Misses C-16, C-26, C-28, C-30. Partial on C-21/C-23/C-24/C-25 (SQ signal, SQ-1 anchor, artifact state, contrast sub-slot).
4. **V-02 — 97.17** Step-label axis with C-30 citation sub-field. Misses C-16, C-26, C-29, C-31. C-17 partial (no phase gate co-location for contamination guard); C-21/C-23/C-24/C-25 partial.
5. **V-03 — 94.35** Minimal inertia-framing. C-25 fix present. Eleven aspirational FAIL including C-14, C-16, C-17, C-18, C-21, C-24, C-26, C-28, C-29, C-30, C-31.

---

## Excellence Signals from V-05

**1. Two-layer contamination error taxonomy (C-17 + C-26)**
V-05 names two structurally distinct contamination errors — AUTO-RULE CONTAMINATION (role evaluation applied to an auto-flagged namespace) and GUARD-BYPASS CONTAMINATION (PM evaluation applied to a namespace with `architect-verdict = CONTRADICTS-ARCHITECTURE`). Each is a named error type, independently verifiable. Prior variants had phase separation but not named error taxonomy.

**2. Positive structural form for SQ answer citation (C-21)**
V-05 provides a named positive form — present-tense artifact naming ("Section 3.2 lists no fallback path") — as the structural signal of a genuine SQ answer, and names "verdict echo" as the prohibited alternative. This converts the template from advisory guidance ("not a restatement") into a falsifiable structural rule.

**3. Canary prohibition as a named error (C-16)**
The zero-remaining confirmation statement is declared a canary: writing it when the condition is not met is a named violation, not just an advisory failure. The confirmation's presence now asserts a system state that is falsifiable at the output level.

**4. End-to-end artifact state traceability (C-24)**
The chain `SQ answer → artifact state field → verdict → /{skill-id} {topic} — {artifact state}` in next-steps propagates the diagnostic source into every action item. Prior variants defined the artifact state field but broke the chain at the next-steps format.

**5. Citation sub-field within template slot — R10 new (C-30)**
`Feeds tier decision: [Strategy SQ-1 answer]` inside the Structural position slot captures the SQ-1 tier decision as a required slot output rather than a conceptual instruction. The author must name the specific tier decision being supported — mechanically distinguishing tier-gating namespaces (where the sub-field would force the author to name a gating decision) from structural-form namespaces.

**6. Cardinality declaration at block header — R10 new (C-31)**
`FORBIDDEN OUTPUTS TRIAD (3 rules, all required)` converts completeness verification from counting entries to a single header assertion. A reviewer confirms completeness by reading the header, then verifies each entry matches — separating the counting operation from content verification.

---

## R10 Ceiling Gap Analysis (V-04 → V-05 delta)

V-04 reaches 98.48 — 1.52 points below ceiling. The remaining gap is entirely aspirational:

| Gap | Criterion | R11 fix |
|-----|-----------|---------|
| Canary prohibition absent | C-16 | Declare confirmation as a named error when written under failure condition |
| No Architect-first guard | C-26 | Switch to Architect-first; add named cross-step guard with `architect-verdict = CONTRADICTS-ARCHITECTURE` trigger |
| SQ structural signal partial | C-21 | Add positive form rule (present-tense artifact naming) and name "verdict echo" as structural error |
| SQ-1 anchor partial | C-23 | Rewrite slot label: `Structural position (required input: Strategy SQ-1 tier decision):` |
| Artifact state not propagated | C-24 | Require `/{skill-id} {topic} — {artifact state}` format in next-steps template |
