Scorecard written to `simulations/quest/scorecards/prove-interview-scorecard-R3-2026-03-14.md`.

---

## prove-interview Round 3 Scores

| Rank | Variation | Score | Golden | Essential |
|------|-----------|-------|--------|-----------|
| 1 | **V-05** Full v3 ceiling candidate | **121/125** | YES | ALL PASS |
| 2 | **V-02** Lifecycle — Named Tension Log | 114/125 | NO | C-05 partial |
| 3 | **V-03** Output format — Traceability Table | 114/125 | NO | C-05 partial |
| 4 | **V-04** Incumbent seeds log (coupling) | 113/125 | NO | C-05 partial |
| 5 | **V-01** Inertia framing — Baseline as Subject 0 | 112/125 | NO | C-05 partial |

---

**Why V-05 missed 125:** Two regressions from R2 V-05:
- **C-10 PARTIAL (3/5):** The coupling architecture dropped the Rationale column from Evidence Pull tables when adding the verbatim Quote column. Both are required; this is additive — restore Rationale alongside Quote.
- **C-11 PARTIAL (3/5):** Explicit CHAMPION/SKEPTIC disposition labels were dropped from the Human Subjects roster when refactoring around "Current practice with Incumbent." The Skeptic assessment in Arc Signal is strong synthesis-level coverage, but C-11's "explicit" requirement means roster-level labeling.

**Three new patterns:**

1. **C-15 is now the default.** All five R3 variations satisfied C-15 through their Contradiction sections' "cite both SUBJECT turns verbatim" language — including three designed to exclude C-15. C-14/C-15 isolation is no longer achievable without deliberately weakening the Contradiction structure. They come free with well-structured C-12 implementation.

2. **C-13 requires a within-interview Q1 anchor, not cross-interview tension tracking.** V-02 (Tension Log) and V-03 (Traceability Table) both FAIL C-13 for the same structural reason: they track claims between subjects, not within-interview current-practice vs. feature-reaction contrast. V-04's coupling mechanism partially satisfies C-13 (grounding infrastructure present, Q1 position absent). Only V-05 passes.

3. **C-10 regression in incumbent-framing architectures.** V-01, V-04, V-05 all dropped the Rationale column when adopting the coupling architecture. V-02 and V-03 kept Confidence + Rationale and scored C-10 PASS. The column swap gains C-14/C-15 depth but loses C-10 compliance — the canonical spec must carry both.

```json
{"top_score": 121, "all_essential_pass": true, "new_patterns": ["C-15 is now the default in all R3 variations — every Contradiction section uses both-sides verbatim quote requirements regardless of design intent, making C-15 isolation no longer achievable without explicitly weakening the Contradiction structure; C-14 and C-15 come free with any well-structured C-12 implementation", "C-13 requires a within-interview Q1 position anchor — cross-interview tension mechanisms (Tension Log prose in V-02, Tension Traceability Table in V-03, Incumbent coupling in V-04) all fail or partially satisfy C-13 because they create grounding infrastructure across interviews without enforcing the Q1 position requirement or within-interview contrast mechanism", "C-10 regression in incumbent-framing architectures — V-01 V-04 and V-05 drop the Rationale column from Evidence Pull tables when adopting the incumbent/baseline coupling architecture; V-02 and V-03 retain Confidence+Rationale and score PASS; the canonical spec must carry both verbatim Quote and Rationale columns regardless of architecture"]}
```

| C-12 | PASS | 5 | Critical Contradiction table: Subject A/B claims + Quote A/B (verbatim, labeled) + Evidential weight ("what it confirms, undermines, or leaves unresolved — not the most dramatic, the most consequential"). Strongest C-12 framing in the round. |
| C-13 | FAIL | 0 | Absent by design. No Q1 current-practice anchor. Opening questions grounded in prior knowledge and relationship with Baseline, not a neutral "what do you do today" question. |
| C-14 | PASS | 5 | Global synthesis rule: "Every synthesis claim — every pattern, Critical Contradiction claim, Baseline Delta item, arc synthesis claim, and assumption update — must cite a direct quote from a SUBJECT turn. No synthesis claim without a source quote." Covers all C-11/C-12 arc synthesis claims. |
| C-15 | PASS | 5 | Critical Contradiction table has explicit Quote A and Quote B fields, both requiring verbatim SUBJECT turns. "Both sides must be cited verbatim." Fully satisfies C-15. |

**Composite: 112/125**
Essential: 56/60 (C-05 partial) | Recommended: 30/30 | Aspirational: 26/35 (C-10 partial: 3, C-11 partial: 3, C-13 fail: 0)
All C-01..C-05 pass: **NO**
Golden: **NO**

---

## V-02: Lifecycle Emphasis — Named Tension Log Phase

*Axis: lifecycle. Targets: C-13. C-14, C-15 absent by design.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | Phase 1 ROSTER table with Subject/Role/Title required before any interview begins. |
| C-02 | PASS | 12 | Phase 2 prior knowledge statement required per subject before first INTERVIEWER turn. Template includes "They know… They do not know… Their primary concern… Their current assumption." |
| C-03 | PASS | 12 | "vocabulary, concerns, and framing must reflect the declared role; distinguishable from other subjects without reading the role label." Generic answers called out as grounding failures. |
| C-04 | PASS | 12 | Evidence Pull tables per subject in Phase 3 (Round 1) and Phase 4 (Round 2). Min 2 rows per subject per round. |
| C-05 | PARTIAL | 8 | No Q1 current-practice anchor. Phase 3 opens with "question — open-ended, grounded in this subject's declared prior knowledge and concerns." Behavioral forcing absent — declared knowledge can sound role-appropriate without being grounded in actual practice. Same structural gap as R2 V-01/V-03. |
| C-06 | PASS | 10 | Surprise section per interview in Phase 3 with verbatim SUBJECT turn quote. |
| C-07 | PASS | 10 | Min 3 INTERVIEWER turns per subject. Labeled FOLLOW-UP required. |
| C-08 | PASS | 10 | Min 2 subjects with "meaningfully different roles, knowledge levels, or concerns." Disposition column. |
| C-09 | PASS | 5 | Phase 5 synthesis with Pattern, Contradiction, Tension Log Resolution, Arc Signal, Prior Assumption Revisited. |
| C-10 | PASS | 5 | Evidence Pull columns: Signal / Quote / Confidence / Rationale. "[one-line rationale]" explicitly required on every row. Phase 3 and Phase 4 evidence tables both have Confidence + Rationale. |
| C-11 | PARTIAL | 3 | Disposition column ("positive / skeptical / neutral") in roster — labels present. But prompt does not require that at least one subject be "positive" AND at least one be "skeptical." Two neutral subjects would satisfy the roster structure. Arc Signal requires one SUBJECT quote for the arc claim but does not enforce an advocate/skeptic pair being present. |
| C-12 | PASS | 5 | Phase 5 Contradiction: "Name it, state why it outranks others (what it confirms, undermines, or leaves unresolved), and cite both SUBJECT turns verbatim." Ranking + evidential weight + both-sides quotes. |
| C-13 | FAIL | 0 | **Scoring finding — hypothesis refuted.** The Tension Log is a cross-interview mechanism tracking claims made by one subject and testing them against other subjects. C-13 requires a within-interview Q1 anchor: "At least one interview opens with a neutral current-practice question… The contrast between the Q1 answer and subsequent feature-reaction answers is used as behavioral grounding evidence." Phase 3 opens with a generic prior-knowledge-grounded question, not a neutral "what do you do today" question. T-number addressing in Phase 4 creates cross-interview grounding, not within-interview Q1 contrast. |
| C-14 | PASS | 5 | **Unintentional compliance.** Arc Signal: "Cite one SUBJECT turn that best evidences the dominant arc" — one quote per arc claim satisfies C-14's per-claim requirement. Contradiction: "cite both SUBJECT turns verbatim" — both-sides quotes satisfy C-14 for the contradiction claim. C-14 was designed absent but satisfied through the Contradiction structure. |
| C-15 | PASS | 5 | **Unintentional compliance.** Phase 5 Contradiction explicitly says "cite both SUBJECT turns verbatim." Critical contradiction is both-sides sourced regardless of design intent. |

**Composite: 114/125**
Essential: 56/60 (C-05 partial) | Recommended: 30/30 | Aspirational: 28/35 (C-11 partial: 3, C-13 fail: 0)
All C-01..C-05 pass: **NO**
Golden: **NO**

**Key finding:** C-13 hypothesis refuted — cross-interview Tension Log does not satisfy within-interview Q1 anchor requirement. C-14 and C-15 satisfied unintentionally through Contradiction section's "cite both SUBJECT turns verbatim" language.

---

## V-03: Output Format — Tension Traceability Table

*Axis: output format. Targets: C-13. C-14, C-15 absent by design.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | ROSTER table with Subject/Role/Title columns required before any interview. |
| C-02 | PASS | 12 | Prior knowledge statement required before first INTERVIEWER turn, not merged with Q&A. Includes prior experience, concern, disposition with grounded reason. |
| C-03 | PASS | 12 | "vocabulary, concerns, and framing must reflect the declared role; distinguishable from other subjects without the role label." |
| C-04 | PASS | 12 | Evidence Pull per subject with min 2 rows, verbatim Quote column. |
| C-05 | PARTIAL | 8 | Same gap as V-02. No Q1 current-practice anchor. Opening question "grounded in this subject's declared prior knowledge and concerns" — generic structure, not behavioral. |
| C-06 | PASS | 10 | Surprise section per subject with verbatim quote and assumption-vs-revelation statement. |
| C-07 | PASS | 10 | Min 3 INTERVIEWER turns. Labeled FOLLOW-UP required. |
| C-08 | PASS | 10 | Min 2 subjects from non-overlapping stakeholder types. |
| C-09 | PASS | 5 | Synthesis with Pattern, Contradiction, Tension Resolution, Arc Signal, Prior Assumption Revisited. |
| C-10 | PASS | 5 | Evidence Pull columns include Rationale: "Signal / Quote / Confidence / Rationale." "[rationale]" required on every row. |
| C-11 | PARTIAL | 3 | Disposition column present ("positive / skeptical / neutral") but advocate/skeptic pair not enforced. Arc Signal requires "one SUBJECT turn that best evidences the dominant arc" — one quote, not per subject. Same gap as V-02. |
| C-12 | PASS | 5 | Contradiction: "Name it, state why it outranks others — what it confirms, undermines, or leaves unresolved. Cite both SUBJECT turns verbatim." Ranking + evidential weight + both-sides quotes. |
| C-13 | FAIL | 0 | **C-13 format-neutral verdict: confirmed FAIL.** The four-column Tension Traceability Table tracks tensions across interviews but is a cross-interview mechanism. Interview opening is "question — open-ended, grounded in this subject's declared prior knowledge" — same structural gap as V-02 prose Tension Log. C-13 fails identically in both formats. Research question 2 answered: format-neutral verdict is double failure, not double pass. |
| C-14 | PASS | 5 | **Unintentional compliance.** Contradiction "Cite both SUBJECT turns verbatim" satisfies C-14 for contradiction claim. Pattern "Cite a supporting SUBJECT quote per subject" satisfies C-14 for convergence claim. Arc Signal "Cite one SUBJECT turn" satisfies C-14 for arc claim. |
| C-15 | PASS | 5 | **Unintentional compliance.** Contradiction: "Cite both SUBJECT turns verbatim." Same finding as V-02. |

**Composite: 114/125**
Essential: 56/60 (C-05 partial) | Recommended: 30/30 | Aspirational: 28/35 (C-11 partial: 3, C-13 fail: 0)
All C-01..C-05 pass: **NO**
Golden: **NO**

**Tie with V-02 at 114.** V-02 ranked above V-03: V-02's explicit phase gates enforce lifecycle sequencing more reliably than V-03's incremental table population without an advancement blocker. V-03 has stronger empty-cell visibility for traceability gaps.

---

## V-04: Incumbent Seeds Log — Coupling Hypothesis (C-13 + C-14)

*Axes: inertia framing + lifecycle. Targets: C-13 + C-14. C-15 absent by design.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | ROSTER with Subject 0 (Incumbent) explicitly labeled + Human Subjects table with Subject/Role/Title. |
| C-02 | PASS | 12 | Prior knowledge blocks required per subject. Human blocks include "What they rely on the Incumbent for that they could not easily replicate: [dependency]." Richer current-practice context than V-02/V-03. |
| C-03 | PASS | 12 | "word choice, concerns, workflow references, and domain artifacts must reflect this specific role; distinguishable from the Incumbent and from all other human subjects without the role label." |
| C-04 | PASS | 12 | IE-# Evidence Pull (Incumbent, min 2 rows) + HE-# (human subjects, min 2 rows). Verbatim Quote column required. |
| C-05 | PARTIAL | 8 | Prior knowledge blocks are the richest of the round (include dependency, switching concern, current practice), but no behavioral Q1 anchor. Human interviews open with "opening question grounded in this subject's role and prior knowledge — references at least one detail from the prior knowledge block." That detail could be current practice but is not required to be a neutral "what do you do today" question. Behavioral forcing absent. |
| C-06 | PASS | 10 | Surprise section per subject with verbatim SUBJECT turn + roster assumption cited + revelation stated. |
| C-07 | PASS | 10 | Min 3 INTERVIEWER turns. At least one turn must directly name a Tension Log entry by T-number. |
| C-08 | PASS | 10 | Min 2 human subjects from non-overlapping stakeholder types. |
| C-09 | PASS | 5 | Phase 3 synthesis with Pattern, Contradiction, Tension Resolution, Inertia Verdict Matrix, Arc Signal, Prior Assumption Revisited. |
| C-10 | PARTIAL | 3 | IE-# and HE-# evidence tables have Confidence column only: "Claim / Quote / Confidence" and "Signal / Quote / Confidence." No Rationale column. Regression from R2 V-04 which had Confidence + Rationale. |
| C-11 | PARTIAL | 3 | No Disposition column in Human Subjects table (Stakeholder type only). Incumbent = implicit advocate. Arc Signal: "Cite a verbatim SUBJECT turn per subject. A SUBJECT turn claiming convergence without role-grounded reasoning is a red flag — flag it explicitly." Per-subject quotes and convergence quality check present, but advocate/skeptic pair not enforced at roster level. |
| C-12 | PASS | 5 | "Name it, state its evidential weight (what it confirms, undermines, or leaves unresolved — not the most dramatic disagreement, the most consequential for the answer), and cite both SUBJECT turns verbatim." |
| C-13 | PARTIAL | 3 | **Coupling mechanism assessed.** The Incumbent Evidence Pull rows promoted to Tension Log create current-practice claims that human subjects verify: "T-[N] — the current approach claims [tension item]. Does that match what you actually encounter in your context?" This creates a current-practice verification loop. However: (a) the T-number question is the THIRD interviewer turn (after opening + follow-up), not Q1; (b) the within-interview Q1 vs feature-reaction contrast is absent; (c) no "Q1 must be a neutral current-practice question before any feature question" structural requirement. Coupling provides grounding infrastructure but not Q1 position enforcement. PARTIAL: substantial current-practice grounding through coupling, Q1 position enforcement missing. |
| C-14 | PASS | 5 | Global synthesis rule: "Every synthesis claim — every pattern, contradiction, Tension resolution entry, Inertia Verdict Matrix row, and assumption update — must cite a direct quote from a SUBJECT turn. No synthesis claim without a source." Contradiction section also requires both-sides quotes. Arc Signal requires per-subject quotes. |
| C-15 | PASS | 5 | **Unintentional compliance.** Phase 3 Contradiction: "cite both SUBJECT turns verbatim." Same pattern as V-01/V-02/V-03. C-15 was absent by design but the Contradiction structure satisfies it regardless — fourth variation with this finding. |

**Composite: 113/125**
Essential: 56/60 (C-05 partial) | Recommended: 30/30 | Aspirational: 27/35 (C-10 partial: 3, C-11 partial: 3, C-13 partial: 3)
All C-01..C-05 pass: **NO**
Golden: **NO**

**Key finding:** Coupling hypothesis partially confirmed — Incumbent Evidence Pull → Tension Log is the structural precursor to C-13. But coupling alone does not satisfy C-13 PASS: the mechanism produces current-practice verification without Q1 position + within-interview contrast. C-15 satisfied unintentionally.

---

## V-05: Full v3 Ceiling Candidate (C-13 + C-14 + C-15)

*Axes: all five. Targets: C-13 + C-14 + C-15. None absent by design.*

| ID | Result | Score | Evidence note |
|----|--------|-------|---------------|
| C-01 | PASS | 12 | ROSTER with Subject 0 (Incumbent) + Human Subjects table. Subject 0 has explicit "Current practice" field. |
| C-02 | PASS | 12 | Prior knowledge blocks required for all subjects. Human blocks include "Current practice: the specific workflow function." Incumbent block includes claims, switching-cost argument, rough edge acknowledged internally. |
| C-03 | PASS | 12 | Q1 answer "specific enough that another role with a different current practice could not give the same Q1 answer." INTERVIEWER:/SUBJECT: format makes persona voice auditable per turn. Q1 contrast note after each interview flags grounding failures structurally. |
| C-04 | PASS | 12 | Evidence Pull with verbatim Quote column per subject (IE-# Incumbent, min 2 rows; HE-# human subjects, min 2 rows). "Quote column must contain verbatim SUBJECT text — not paraphrase, not summary." |
| C-05 | PASS | 12 | Q1 current-practice anchor on BOTH Incumbent (Step 1: "What does a team that depends on incumbent_name actually do in their workflow… Walk me through the specific daily function. This is a neutral question about current practice — not about features, not about evaluation.") AND each human subject (Step 2: "Walk me through what you actually do with incumbent_name in a typical workflow cycle. I want to understand what you do today, before we talk about anything else."). Q1 contrast note required after each human interview: "A Q1 answer that ignores or contradicts the declared current practice is a grounding failure — flag it explicitly here." Behavioral forcing is bidirectional and structurally visible at the turn level. |
| C-06 | PASS | 10 | Surprise section per subject with verbatim SUBJECT turn quote + roster assumption cited + revelation stated. |
| C-07 | PASS | 10 | Min 3 INTERVIEWER turns per subject. Q1 is the opening question. At least one subsequent turn must directly name a Tension Log entry by T-number. Labeled FOLLOW-UP per interview. |
| C-08 | PASS | 10 | Min 2 human subjects from non-overlapping stakeholder types. "Current practice with Incumbent" must differ meaningfully between S-01 and S-02 — behavioral differentiation enforced beyond role labels. |
| C-09 | PASS | 5 | Synthesis with Pattern, Critical Contradiction, Tension Resolution, Inertia Verdict Matrix, Arc Signal, Prior Assumption Revisited. |
| C-10 | PARTIAL | 3 | **Regression from R2 V-05.** Evidence tables: "IE-# / Claim / Quote / Confidence" and "HE-# / Signal / Quote / Confidence." No Rationale column. R2 V-05 had Confidence + Rationale and scored PASS. R3 V-05 dropped Rationale when adding the coupling architecture. C-10 requires "explicit confidence marker with a one-line rationale." Confidence present, rationale absent — PARTIAL. |
| C-11 | PARTIAL | 3 | No explicit Disposition labels in Human Subjects roster (Stakeholder type only). Incumbent is structural advocate for status quo. Arc Signal includes "Skeptic assessment" field: "Did any subject's resistance appear role-grounded (rooted in their declared current practice) or positional? Cite one SUBJECT turn. A SUBJECT turn claiming skepticism that ignores the subject's declared current practice is a grounding failure — flag it." Strong synthesis-level skeptic identification, but advocate/skeptic pair not enforced at roster level. No "at least one CHAMPION and one SKEPTIC required" instruction. |
| C-12 | PASS | 5 | Critical Contradiction table: Subject A/B + positions + Quote A/Quote B (verbatim, not paraphrased) + Evidential weight ("Not the most dramatic — the one whose resolution most changes the answer to the interview question"). Strongest C-12 structure in the round. |
| C-13 | PASS | 5 | Two C-13 mechanisms present: (1) Incumbent Q1 anchor in Step 1 — neutral workflow question before any feature or evaluation question; (2) human subject Q1 anchor per-interview in Step 2 — "I want to understand what you do today, before we talk about anything else"; (3) Q1 contrast note after each human interview explicitly checks whether Q1 answer is consistent with declared current practice. Incumbent → Tension Log coupling reinforces grounding infrastructure. All three C-13 structural components present: Q1 position, neutrality, within-interview contrast mechanism. |
| C-14 | PASS | 5 | Global synthesis rule: "Every synthesis item — every pattern claim, Critical Contradiction claim, Tension resolution entry, Inertia Verdict Matrix row, Arc Signal claim, and assumption update — must cite a direct quote from a SUBJECT turn. No synthesis claim without a source. No inference without a turn." Strongest C-14 enforcement in the round. |
| C-15 | PASS | 5 | Critical Contradiction table has explicit Quote A and Quote B fields ("verbatim SUBJECT turn from Subject A — not paraphrased, not summarized"). Both sides fully sourced. |

**Composite: 121/125**
Essential: 60/60 | Recommended: 30/30 | Aspirational: 31/35 (C-10 partial: 3, C-11 partial: 3)
All C-01..C-05 pass: **YES**
Golden: **YES**

---

## Round 3 Rankings

| Rank | Variation | Score | Essential | Golden | Key differentiator |
|------|-----------|-------|-----------|--------|-------------------|
| 1 | V-05 (Full v3 ceiling candidate) | 121/125 | ALL PASS | YES | Dual Q1 anchor (Incumbent + per-subject) + Q1 contrast note closes C-13; global quote rule + both-sides Contradiction covers C-14 + C-15 |
| 2 | V-02 (Lifecycle — Named Tension Log) | 114/125 | C-05 PARTIAL | NO | C-14 + C-15 unintentional PASS; C-10 PASS (Rationale retained); C-13 FAIL (cross-interview not Q1 anchor) |
| 3 | V-03 (Output format — Traceability Table) | 114/125 | C-05 PARTIAL | NO | C-14 + C-15 unintentional PASS; C-10 PASS; C-13 FAIL (format-neutral double failure confirmed) |
| 4 | V-04 (Incumbent seeds log) | 113/125 | C-05 PARTIAL | NO | C-13 PARTIAL (coupling is the precursor structure, not full pass); C-10 PARTIAL (dropped Rationale); C-15 unintentional PASS |
| 5 | V-01 (Inertia framing — Baseline as Subject 0) | 112/125 | C-05 PARTIAL | NO | C-14 + C-15 PASS; strongest C-12 table structure; C-10 PARTIAL (no Rationale); C-13 absent |

V-05 ranked above all others as the only Golden variation. V-02 ranked above V-03 at the 114 tie: explicit phase gates (PHASE 3b, PHASE 4, PHASE 5 advancement rules) enforce lifecycle sequencing more reliably than V-03's incremental table population without a phase advancement blocker.

---

## Why V-05 hit 121 and not 125

Two criteria missed:

**C-10 (3/5):** The coupling architecture (Incumbent Evidence Pull → Tension Log) trades the Rationale column for the verbatim Quote column — a column swap that gains grounding depth (satisfying C-14/C-15) but loses the confidence rationale required by C-10. R2 V-05 had both Quote and Rationale. R3 V-05 dropped Rationale when adopting the coupling architecture. The fix is additive: restore Rationale column alongside Quote column.

**C-11 (3/5):** The Human Subjects roster has Stakeholder type but no Disposition labels. The Skeptic assessment in Arc Signal is strong synthesis-level enforcement, but C-11 requires "at least one explicit advocate (champion or supporter) and at least one explicit skeptic" — the "explicit" requirement means roster-level labeling, not just synthesis-level identification. R2 V-05 had explicit CHAMPION/SKEPTIC labels. R3 V-05 dropped them when refactoring the roster around "Current practice with Incumbent." Fix: add Disposition field to Human Subjects table and require at least one POSITIVE and one SKEPTICAL declaration.

---

## R3 Research Question Verdicts

**Q1: Can one axis change (inertia framing) carry two new criteria (C-14 + C-15)?**
Confirmed for V-01 specifically — but superseded by a round-level finding. All five R3 variations satisfy C-14 and C-15 through their Contradiction sections. The both-sides quote pattern is now universal. The inertia framing's contribution to C-14/C-15 is real but redundant. **True finding:** C-14/C-15 are not isolatable in any well-structured Contradiction section. They come standard with strong C-12 implementation.

**Q2: Is C-13 format-neutral between V-02 prose and V-03 table?**
Confirmed — but the format-neutral verdict is double failure. Both V-02 and V-03 fail C-13 identically. Cross-interview tension tracking does not satisfy C-13's within-interview Q1 anchor requirement regardless of prose vs. columnar format. The format-neutrality thesis was confirmed; the format that was neutral was FAIL.

**Q3: Does V-04 coupling mechanism remain valid at C-13 + C-14 level without C-15?**
Partially confirmed. V-04 achieves C-14 PASS and C-13 PARTIAL (not PASS). The coupling thesis — that Incumbent Evidence Pull seeding Tension Log generates C-13 content as a side effect — holds for creating grounding infrastructure but is insufficient alone for C-13 PASS: the Q1 position requirement is the gap. C-15 was satisfied unintentionally (fourth variation with this finding).

**Q4: Do C-13 and C-15 conflict or reinforce?**
Reinforce. V-05 achieves both C-13 PASS and C-15 PASS simultaneously without structural conflict. Mechanisms are independent: C-13 targets Q1 within-interview position; C-15 targets Contradiction synthesis. Source quotes generated by the Q1 anchor (fed into Tension Log) are not the same quotes required for C-15's both-sides Contradiction table. No overlap, no conflict.

---

## Excellence Signals (from V-05)

### Signal 1: Dual Q1 anchor closes C-13 at both the non-human and human interview levels

V-05 applies the Q1 current-practice anchor twice: once to the Incumbent ("What does a team that depends on it actually do in their workflow that would require a replacement path before moving away? This is a neutral question about current practice — not about features, not about evaluation.") and once to every human subject ("Walk me through what you actually do… I want to understand what you do today, before we talk about anything else."). The Q1 contrast note after each human interview makes behavioral grounding failures structurally visible.

**Implication:** V-04's single-mechanism coupling (Incumbent Q1 only, no per-subject Q1) scored C-13 PARTIAL. The dual-level structure is the reliable C-13 implementation. Single-mechanism approaches are insufficient.

### Signal 2: C-14/C-15 are now the default — isolation is no longer achievable

Every R3 variation required "cite both SUBJECT turns verbatim" in its Contradiction section, satisfying C-15 regardless of design intent. V-02, V-03, and V-04 all intended C-15 absent but satisfied it through the Contradiction structure. C-14/C-15 come free with any well-structured C-12 implementation. Future rubric versions should reflect this: C-14 and C-15 may be better modeled as quality tiers of C-12 than as separable aspirational criteria.

### Signal 3: C-10 regression in incumbent-framing architectures requires explicit preservation

V-01, V-04, and V-05 all use Incumbent/Baseline Evidence Pull tables and all dropped the Rationale column (Confidence only), scoring C-10 PARTIAL. V-02 and V-03 retain Confidence + Rationale and score C-10 PASS. The coupling architecture trades the Rationale column for the Quote column — a gain in C-14/C-15 compliance at the cost of C-10 compliance. The canonical spec must explicitly carry both columns regardless of architecture.

---

## Prediction Accuracy

| Variation | Predicted | Scored | Delta | Root cause |
|-----------|-----------|--------|-------|------------|
| V-01 | 120/125 | 112/125 | -8 | C-10 PARTIAL (-2), C-11 PARTIAL (-2), C-05 PARTIAL assumed PASS in prediction (-4) |
| V-02 | 115/125 | 114/125 | -1 | C-11 PARTIAL (-2) offset by C-14 + C-15 unintentional PASS (+10 vs predicted FAIL); C-05 assumed PASS in prediction (-4) |
| V-03 | 115/125 | 114/125 | -1 | Same as V-02 |
| V-04 | 120/125 | 113/125 | -7 | C-05 PARTIAL (-4), C-10 PARTIAL (-2), C-11 PARTIAL (-2), C-13 PARTIAL vs predicted PASS (-2); C-15 unintentional PASS (+5) partially offsets |
| V-05 | 125/125 | 121/125 | -4 | C-10 PARTIAL (-2, Rationale column dropped), C-11 PARTIAL (-2, explicit disposition labels dropped) |

Systematic overestimation of C-05 and C-11: predictions assumed both would pass based on prior architecture patterns. C-10 regression is a genuine design error — Rationale was present in R2's V-04 and V-05 and was inadvertently dropped in R3.

---

```json
{"top_score": 121, "all_essential_pass": true, "new_patterns": ["C-15 is now the default in all R3 variations — every Contradiction section uses both-sides verbatim quote requirements regardless of design intent, making C-15 isolation no longer achievable without explicitly weakening the Contradiction structure; C-14 and C-15 come free with any well-structured C-12 implementation", "C-13 requires a within-interview Q1 position anchor — cross-interview tension mechanisms (Tension Log prose in V-02, Tension Traceability Table in V-03, Incumbent coupling in V-04) all fail or partially satisfy C-13 because they create grounding infrastructure across interviews without enforcing the Q1 position requirement or within-interview contrast mechanism", "C-10 regression in incumbent-framing architectures — V-01 V-04 and V-05 drop the Rationale column from Evidence Pull tables when adopting the incumbent/baseline coupling architecture; V-02 and V-03 retain Confidence+Rationale and score PASS; the canonical spec must carry both verbatim Quote and Rationale columns regardless of architecture"]}
```
