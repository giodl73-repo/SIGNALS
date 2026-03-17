## org-review — Round 3 Scoring

### Rubric Applied: v3 (C-01–C-15, 100 pts, golden threshold 80)

---

## V-01 — Gate Sequencing: Verdict Propagation Chain

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role Coverage | PASS (9) | Three named archetype slots: CHALLENGER / DOMAIN / LIFECYCLE, sourced from `.craft/roles/signal/` |
| C-02 Artifact Scope | PARTIAL (5) | No explicit enumeration of artifact surface (spec, feasibility, prior decisions) before review begins |
| C-03 Per-Reviewer Findings | PASS (9) | Each gate has distinct Findings block with explicit Severity |
| C-04 Severity Anchored | PARTIAL (6) | Gate 1 anchor is null-hypothesis-specific ("HIGH = artifact does not address null hypothesis"). Universal commit-gate semantics (HIGH=blocks / MEDIUM=conditions / LOW=advisory) absent from preamble and Gates 2–3 |
| C-05 Lifecycle Coverage | PASS (9) | Gate 1 = null hypothesis, Gate 2 = domain, Gate 3 = commitment readiness — full three-stage coverage |
| C-06 Action Items | PARTIAL (5) | Per-gate Recommendation fields exist; no consolidated action list distinguishing BLOCKED / CONDITIONAL / advisory items with explicit traceability |
| C-07 Null Hypothesis Framing | PASS (9) | "Gate 1 runs first, in isolation. This gate determines whether the null hypothesis is named and addressed." Pre-domain. |
| C-08 Summary Exists | PARTIAL (6) | Disposition section emits verdict + primary driver (one sentence). Explicitly prohibits narrative synthesis: "Do not editorially reason from findings." Fails "integrating narrative" requirement. |
| C-09 Conflict Detection | PARTIAL (2) | No explicit conflict-detection field; domain aggregate = worst-case only |
| C-10 Reviewer Independence | PASS (4) | Phase-separated gates; Gate 1 runs in isolation |
| C-11 Disposition Code | PASS (4) | "Overall Disposition: READY / CONDITIONAL / BLOCKED" labeled |
| C-12 NH Anchor per Role | PARTIAL (2) | Domain NH engagement conditional ("if Gate 1 = CONDITIONAL or FAIL: my findings must address…"). Not a universal per-role stance. |
| C-13 Gate Verdict Propagation | PASS (4) | Full propagation rules: Gate 1 PASS / CONDITIONAL / FAIL each change Gate 2's task definition. "A gate's verdict is not a finding — it is a typed signal that changes the task of downstream gates." |
| C-14 Disposition Algebra | PASS (4) | Explicit algebra: "BLOCKED if any gate = FAIL / CONDITIONAL if no FAIL and ≥1 CONDITIONAL / READY if all PASS" |
| C-15 Adversarial Bracket | FAIL (0) | Challenger runs once (Gate 1 only). No Bracket Closing. |

**V-01 Total: 78 / 100** — below golden threshold (80)

---

## V-02 — Pre-printed Template Surface

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role Coverage | PASS (9) | Pre-printed Role Manifest table with labeled CHALLENGER / DOMAIN / LIFECYCLE slots; cannot be omitted |
| C-02 Artifact Scope | PARTIAL (5) | No explicit artifact surface enumeration in preamble |
| C-03 Per-Reviewer Findings | PASS (9) | Pre-printed per-section Findings and Severity fields; structural omission impossible |
| C-04 Severity Anchored | PASS (9) | DOMAIN section: "Anchor: HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory" — universal commit-gate semantics, pre-printed and present |
| C-05 Lifecycle Coverage | PASS (9) | CHALLENGER (null hypothesis) → DOMAIN (technical) → LIFECYCLE (commitment) — all three stages |
| C-06 Action Items | PASS (8) | DISPOSITION: pre-printed Conditions (CONDITIONAL) + Blocker (BLOCKED) fields traceable to gate verdicts; per-section Recommendation fields |
| C-07 Null Hypothesis Framing | PASS (9) | CHALLENGER section runs first with pre-printed "Null hypothesis" field |
| C-08 Summary Exists | PASS (9) | CROSS-ROLE SIGNALS (conflicts, convergence, uncovered areas) + DISPOSITION (primary driver, conditions) — full synthesis, pre-printed |
| C-09 Conflict Detection | PASS (4) | CROSS-ROLE SIGNALS section pre-printed: "Conflicts: [Two reviewers whose recommendations are incompatible — name roles and tension. If none: write 'None detected.']" Cannot be omitted |
| C-10 Reviewer Independence | PASS (4) | Phase-separated gates; CHALLENGER runs before DOMAIN |
| C-11 Disposition Code | PASS (4) | "Overall Disposition: [READY / CONDITIONAL / BLOCKED]" labeled field |
| C-12 NH Anchor per Role | PASS (4) | Per-section null hypothesis engagement: LIFECYCLE has "Null hypothesis status: [yes / partial / no]"; DOMAIN must address Gate 1 gap |
| C-13 Gate Verdict Propagation | PASS (4) | "Received Gate 1 Verdict: [copy from CHALLENGER]" + "Received Gate 2 Verdict: [copy from DOMAIN]" in pre-printed LIFECYCLE section |
| C-14 Disposition Algebra | PASS (4) | DISPOSITION: "Apply the algebra below to the gate vector above. Do not reason editorially." with stated BLOCKED / CONDITIONAL / READY rules |
| C-15 Adversarial Bracket | FAIL (0) | CHALLENGER appears in one section only. No BRACKET CLOSING. |

**V-02 Total: 89 / 100** — above golden threshold

---

## V-03 — Formula-First Disposition Algebra

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role Coverage | PASS (9) | Three explicit archetype slots: CHALLENGER, DOMAIN, LIFECYCLE |
| C-02 Artifact Scope | PARTIAL (5) | No artifact surface enumeration |
| C-03 Per-Reviewer Findings | PASS (9) | Per-gate Findings + Severity |
| C-04 Severity Anchored | PASS (9) | Inline per gate: "Severity: HIGH / MEDIUM / LOW (HIGH = blocks commitment; MEDIUM = conditions; LOW = advisory)" — universal and repeated |
| C-05 Lifecycle Coverage | PASS (9) | CHALLENGER → DOMAIN → LIFECYCLE sequence covers all three stages |
| C-06 Action Items | PASS (8) | Step 3 "Conditions (if CONDITIONAL): In priority order… state exactly what must be resolved." Per-gate Recommendations. |
| C-07 Null Hypothesis Framing | PASS (9) | CHALLENGER runs first; formula preamble elevates null gate: "g_null = FAIL always yields BLOCKED" |
| C-08 Summary Exists | PASS (8) | Step 3 Formula Evaluation: gate verdict table + "Primary driver" + "Conditions" — structured synthesis |
| C-09 Conflict Detection | PARTIAL (2) | "Null Hypothesis Stance: These stances must differ substantively across roles" — requires divergence but no named conflict-detection mechanism |
| C-10 Reviewer Independence | PASS (4) | Phase-separated: CHALLENGER → DOMAIN → LIFECYCLE |
| C-11 Disposition Code | PASS (4) | "Overall Disposition: READY / CONDITIONAL / BLOCKED" in Step 3 |
| C-12 NH Anchor per Role | PASS (4) | Per-gate "Null Hypothesis Stance" with differentiated frame requirements (CHALLENGER: workaround worse? / DOMAIN: makes workaround obsolete? / LIFECYCLE: decision case strong enough?) |
| C-13 Gate Verdict Propagation | PARTIAL (2) | Sequential CHALLENGER → DOMAIN → LIFECYCLE with consistent severity calibration ("do not copy another gate's level"), but no typed verdict that changes downstream gate's task. Formula collects verdicts at Step 3; gates don't receive prior verdicts during execution. |
| C-14 Disposition Algebra | PASS (4) | **Strongest C-14 implementation**: formula stated in preamble before any reviewer runs. Step 3 explicitly says "Evaluate the preamble formula." Model cannot rewrite the formula it did not generate — strongest pre-run commitment. |
| C-15 Adversarial Bracket | FAIL (0) | Challenger runs at Gate 1 only. No closing bracket. |

**V-03 Total: 86 / 100** — above golden threshold

---

## V-04 — Adversarial Bracket + Gate Verdict Propagation

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role Coverage | PASS (9) | "Assign one role per slot: CHALLENGER, DOMAIN, LIFECYCLE" from `.craft/roles/signal/` |
| C-02 Artifact Scope | PARTIAL (5) | No artifact surface enumeration |
| C-03 Per-Reviewer Findings | PASS (9) | Each gate section has Findings + Severity |
| C-04 Severity Anchored | PARTIAL (6) | Bracket Opening: "Anchor: HIGH = artifact does not address null hypothesis; LOW = null hypothesis convincingly defeated" — null-hypothesis-scoped, not universal. Domain and Lifecycle: "Calibrate independently" — no commit-gate anchor. |
| C-05 Lifecycle Coverage | PASS (9) | Bracket Opening + Domain Gate + Lifecycle Gate + Bracket Closing = full lifecycle plus synthesis |
| C-06 Action Items | PASS (8) | Per-gate Recommendation; Disposition: Conditions + Blocker; Bracket Closing: Remaining Gaps. Cross-role conflicts named as actionable signal. |
| C-07 Null Hypothesis Framing | PASS (9) | "The challenger runs first. This is a declaration pass… Null Hypothesis: What the team does today instead of building this." |
| C-08 Summary Exists | PASS (9) | Bracket Closing: Domain Evidence Assessment table + Remaining Gaps + Challenger Final Verdict. Disposition: primary driver + conditions. Rich synthesis referencing null hypothesis verdict. |
| C-09 Conflict Detection | PASS (4) | Disposition: "Cross-role conflicts: Did any domain reviewer produce a null hypothesis address that contradicted the Bracket Closing verdict? Name the tension — this is the most important signal in the review if present." Bracket Closing table has "Challenge Answered? yes / partial / no" per reviewer. |
| C-10 Reviewer Independence | PASS (4) | Bracket architecture: domain and lifecycle reviewers write inside the bracket (after Opening, before Closing) without seeing Closing. |
| C-11 Disposition Code | PASS (4) | "Overall Disposition: READY / CONDITIONAL / BLOCKED" labeled |
| C-12 NH Anchor per Role | PASS (4) | Domain: "Null Hypothesis Address: From this role's technical frame — does the artifact defeat the null hypothesis? Must differ from challenger's framing." Lifecycle: "Null Hypothesis Status: yes / partial / no." Per-role and frame-differentiated. |
| C-13 Gate Verdict Propagation | PASS (4) | Full typed propagation: "Gate 0 carries forward. All subsequent gates open with: Received Gate 0 Verdict: [value] \| Challenge: '[challenge text]'" — both verdict AND specific challenge text propagate. Domain may not issue PASS without answering challenge. |
| C-14 Disposition Algebra | PASS (4) | Disposition algebra stated explicitly: "BLOCKED if GClose = FAIL… OR if any other gate = FAIL. CONDITIONAL if no gate = FAIL and ≥1 CONDITIONAL. READY if all = PASS." Auditable rule. |
| C-15 Adversarial Bracket | PASS (4) | Full bracket: Bracket Opening (first, before domain) + Bracket Closing (last, after all domain/lifecycle). "GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict from the challenger is not overturned by domain or lifecycle PASses." |

**V-04 Total: 92 / 100** — above golden threshold

---

## V-05 — Pre-printed Template + Formula + Adversarial Bracket

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role Coverage | PASS (9) | Pre-printed Role Manifest: "CHALLENGER (bracket open + close) \| inertia-advocate", "DOMAIN \| technical/architecture", "LIFECYCLE \| PM/program" — cannot be dropped |
| C-02 Artifact Scope | PARTIAL (5) | No artifact surface enumeration |
| C-03 Per-Reviewer Findings | PASS (9) | All section headers and Findings fields pre-printed; structural omission impossible |
| C-04 Severity Anchored | PARTIAL (6) | BRACKET OPENING: "Anchor: HIGH = artifact does not address null hypothesis; LOW = null hypothesis convincingly defeated" — null-hypothesis-scoped. DOMAIN and LIFECYCLE sections carry `[HIGH / MEDIUM / LOW]` without universal commit-gate anchor. Preamble lacks the standard mapping. |
| C-05 Lifecycle Coverage | PASS (9) | BRACKET OPENING (null hypothesis) → DOMAIN (technical) → LIFECYCLE (commitment) → BRACKET CLOSING (synthesis) |
| C-06 Action Items | PASS (9) | DISPOSITION: pre-printed "Conditions (complete only if CONDITIONAL)" + "Blocker (complete only if BLOCKED)" with explicit fill format. Per-gate Recommendation fields. Pre-printing guarantees presence. |
| C-07 Null Hypothesis Framing | PASS (9) | BRACKET OPENING is first pre-printed section: "Null hypothesis: [What the team does today instead of building this — one sentence.]" |
| C-08 Summary Exists | PASS (9) | BRACKET CLOSING: Domain Evidence Assessment table + Remaining gaps + GClose verdict. DISPOSITION: gate vector fill + formula evaluation + primary driver. Pre-printed synthesis cannot be omitted. |
| C-09 Conflict Detection | PASS (4) | BRACKET CLOSING: "Domain evidence assessment" table with "Challenge Answered? yes / partial / no" per reviewer. Structural conflict detection: a partial/no in that table is an explicit conflict signal. |
| C-10 Reviewer Independence | PASS (4) | Bracket architecture pre-printed: BRACKET OPENING → DOMAIN → LIFECYCLE → BRACKET CLOSING. "Do not alter, reorder, or omit any pre-printed heading." Order is structurally enforced. |
| C-11 Disposition Code | PASS (4) | "Overall Disposition: [READY / CONDITIONAL / BLOCKED — result of evaluating the formula above]" pre-printed labeled field |
| C-12 NH Anchor per Role | PASS (4) | Pre-printed per-section null hypothesis address fields: DOMAIN "Null hypothesis address: [from this role's technical frame… must differ from challenger's framing]", LIFECYCLE "Null hypothesis status: [yes / partial / no]" — mechanically required |
| C-13 Gate Verdict Propagation | PASS (4) | Pre-printed carry-forward lines in every section: DOMAIN opens "Received GOpen: [copy from BRACKET OPENING]", LIFECYCLE opens "Received GOpen: [...]" and "Received G_domain: [...]", BRACKET CLOSING "Full record received." GClose overrides all prior verdicts. |
| C-14 Disposition Algebra | PASS (4) | **Strongest C-14**: formula pre-printed in preamble ("do not alter this block") AND re-printed as fill fields in DISPOSITION ("Apply pre-stated formula — do not alter the formula; do not reason editorially — evaluate the gate vector against the formula"). Dual enforcement at pre-review and post-review positions. |
| C-15 Adversarial Bracket | PASS (4) | Pre-printed BRACKET OPENING and BRACKET CLOSING as fixed section headers. "Do not alter, reorder, or omit any pre-printed heading." Bracket architecture is structurally enforced — model cannot collapse the two positions. GClose = FAIL is first line of formula. |

**V-05 Total: 93 / 100** — above golden threshold

---

## Round 3 Summary

| Variation | Axes | Score | Essential gaps | Golden |
|-----------|------|-------|----------------|--------|
| V-05 | Template + Formula + Bracket | **93** | C-02 PARTIAL, C-04 PARTIAL | ✓ |
| V-04 | Bracket + Propagation | **92** | C-02 PARTIAL, C-04 PARTIAL | ✓ |
| V-02 | Pre-printed Template | **89** | C-02 PARTIAL, C-15 FAIL | ✓ |
| V-03 | Formula-First | **86** | C-02 PARTIAL, C-13 PARTIAL, C-15 FAIL | ✓ |
| V-01 | Verdict Propagation | **78** | C-02 PARTIAL, C-04 PARTIAL, C-08 PARTIAL, C-15 FAIL | ✗ |

**Ranking**: V-05 > V-04 > V-02 > V-03 > V-01

**C-02 is the universal weak point** across all R3 variations: no variation explicitly enumerates the artifact surface (spec, design, feasibility, competitive context, prior decisions) in the preamble. This is the main remaining essential gap.

**C-04 in V-04/V-05**: Both bracket variations anchor severity for the null hypothesis dimension in Bracket Opening ("LOW = null hypothesis convincingly defeated") but do not carry the universal commit-gate semantics (HIGH=blocks / MEDIUM=conditions / LOW=advisory) to DOMAIN and LIFECYCLE sections or the preamble. V-02 and V-03 handle this better.

---

## Excellence Signals from V-05

**Signal 1 — Dual-position formula enforcement**: V-05 pre-prints the disposition formula twice: in the preamble ("do not alter this block") and as fill fields in DISPOSITION ("do not alter the formula; evaluate the gate vector"). The preamble position prevents editorial drift before the review runs; the DISPOSITION position prevents formula rewrite or substitution at close. V-03 (preamble only) and V-04 (close only, stated in text) each prevent one failure class; V-05 closes both.

**Signal 2 — Bracket position enforcement via template**: In V-04, the bracket is instructional — the model is told the challenger runs first and last. In V-05, BRACKET OPENING and BRACKET CLOSING are pre-printed section headers with "do not alter, reorder, or omit." The model cannot collapse the bracket because it did not generate the headers. This converts C-15 from compliance-by-instruction to compliance-by-structure.

---

```json
{"top_score": 93, "all_essential_pass": false, "new_patterns": ["Dual-position formula enforcement: stating the disposition formula in the preamble AND re-printing it as fill fields in the DISPOSITION section closes two distinct failure classes — pre-review editorial drift and post-review formula substitution — neither preamble-only nor close-only formula statement achieves both", "Bracket enforcement via pre-printed section headers: when BRACKET OPENING and BRACKET CLOSING are fixed structural elements with an explicit no-reorder instruction, the adversarial bracket cannot be collapsed by the model because it did not generate the positions, converting C-15 from instructional compliance to structural compliance"]}
```
