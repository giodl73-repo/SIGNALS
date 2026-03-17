## /quest:score — mock-review Round 1

---

### Scoring Methodology

**Formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
**PARTIAL** = 0.5 credit. **PASS** = 1.0. **FAIL** = 0.

Tier notation: P = PASS, Pt = PARTIAL, F = FAIL.

---

### V-01 — Role Sequence: Auto-Rules Gate Before Role Evaluation

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | **PASS** | "Every namespace must appear in exactly one list" — Phase 1 auto-flag list + Phase 2 remaining list account for all namespaces; no namespace can be skipped |
| C-02 Automatic rule correctness | **PASS** | Phase 1 fires all three rules before any role evaluation begins; "Rules are not role-overridable" is explicit; STOP gate after Phase 1 output enforces ordering |
| C-03 MOCK-ACCEPTED reason codes | **PASS** | Phase 2: "at least one reason code from: STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT. Valid reason codes are exactly as written above. No paraphrase." |
| C-04 Status write-back | **PASS** | Phase 4 "Write Status Back to Source Artifact (mandatory)"; "This is the defining action of /mock:review. It is required"; zero-remaining confirmation required |
| C-05 Next-steps priority order | **PASS** | Phase 3 explicitly defines Priority 1 (critical: trace → scout-feasibility → listen) / Priority 2 (non-critical) / Priority 3 (evidence-heavy) |
| C-06 Rule trigger named | **PASS** | Phase 1: "trigger = {EVIDENCE-HEAVY \| TIER-CRITICAL \| COMPLIANCE}"; Phase 2: "REAL-REQUIRED with the evaluation verdict that drove the decision" |
| C-07 PM/Arch/Strategy shown | **PASS** | Phase 2 per-namespace template: PM sub-questions (sections present? gates? tables?), Architect ("Does mock content contradict known architectural facts?"), Strategy ("Is coverage adequate for Tier {tier} decisions?") — all three required with verdicts |
| C-08 Tier flag respected | **PASS** | "State the tier at the top of your output: Tier used: {N} (source: ...)"; Rule B gates on tier >= 2 |
| C-09 Coverage gap synthesis | **FAIL** | Next-steps is a flat priority-ordered list with no cross-namespace risk statement or urgency grouping commentary |
| C-10 MOCK-ACCEPTED namespace-specific rationale | **FAIL** | Reason codes required but no instruction to produce a namespace-specific explanatory sentence; a bare code satisfies the format |

**Essential**: 5/5 = 1.0 | **Recommended**: 3/3 = 1.0 | **Aspirational**: 0/2 = 0
**Composite**: (1.0 × 60) + (1.0 × 30) + (0 × 10) = **90**
**All essential pass**: YES

---

### V-02 — Output Format: Prose Evaluation Then Summary Table

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | **PASS** | Per-namespace prose entry + summary table together cover all namespaces; auto-flagged entries get a decision, remaining entries get full evaluation |
| C-02 Automatic rule correctness | **PARTIAL** | "Apply before any review. These fire independently and cannot be overridden." + per-namespace "[If auto-flagged: skip evaluation sections]" — correct intent but inline conditional logic rather than a hard completed-phase gate; a model could still evaluate an EVIDENCE-HEAVY namespace before skipping |
| C-03 MOCK-ACCEPTED reason codes | **PASS** | Decision line template shows exact codes; "[For MOCK-ACCEPTED: use STRUCTURAL-COVERAGE-SUFFICIENT when structural completeness drove the verdict… use both when both apply. Use exact codes only.]" |
| C-04 Status write-back | **PARTIAL** | "Write Status Back" section with explicit Edit instructions, but it is a closing prose section — no named-phase label, no stop gate, no "mandatory" keyword; easiest action to omit |
| C-05 Next-steps priority order | **PASS** | "Number the real skill runs in priority order: 1. Critical... 2. Non-critical... 3. Evidence-heavy" — ordering rule is explicit |
| C-06 Rule trigger named | **PASS** | Auto-flagged: "Trigger: {EVIDENCE-HEAVY \| TIER-CRITICAL \| COMPLIANCE}"; evaluation-driven: "name the evaluation failure" |
| C-07 PM/Arch/Strategy shown | **PASS** | Prose format explicitly requires **PM assessment**, **Architect assessment**, **Strategy assessment** as labeled headings with one-to-three sentence requirements and "Name specific sections or mechanisms" — strongest C-07 forcing function among V-01–V-04 |
| C-08 Tier flag respected | **PASS** | "State at the top: 'Tier: {N} (source: ...)'" + Rule 2 checks Tier 2+ |
| C-09 Coverage gap synthesis | **FAIL** | Next-steps is numbered with priority labels but no cross-namespace synthesis or risk statement |
| C-10 MOCK-ACCEPTED namespace-specific rationale | **PASS** | PM / Architect / Strategy assessment paragraphs appear per-namespace before the decision and name specific elements; prose format produces namespace-specific reasoning as the evaluation output |

**Essential**: (1 + 0.5 + 1 + 0.5 + 1)/5 = 4.0/5 = 0.80 | **Recommended**: 3/3 = 1.0 | **Aspirational**: 1/2 = 0.5
**Composite**: (0.80 × 60) + (1.0 × 30) + (0.5 × 10) = 48 + 30 + 5 = **83**
**All essential pass**: NO (C-02 PARTIAL, C-04 PARTIAL)

---

### V-03 — Lifecycle Emphasis: Named Phases with Stop Gates

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | **PASS** | Phase 1 inventory + Phase 2 two-list partition + Phase 3 evaluation together require every namespace to be placed; "STOP. Every namespace must appear in exactly one list before entering Phase 3" |
| C-02 Automatic rule correctness | **PASS** | Phase 2 is a dedicated AUTO-FLAGGING phase with three named rules and a STOP gate; "Record the trigger rule for each auto-REAL-REQUIRED namespace" |
| C-03 MOCK-ACCEPTED reason codes | **PASS** | Phase 3: "MOCK-ACCEPTED requires at least one code from this exact set: STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT. No paraphrase. No invented codes." |
| C-04 Status write-back | **PASS** | PHASE 5 "WRITE STATUS BACK (mandatory)": "This is the defining action of /mock:review. It cannot be skipped." + "Zero Status fields may remain as MOCK (awaiting review) after Phase 5 completes." Strongest enforcement of write-back among all variations |
| C-05 Next-steps priority order | **PASS** | Phase 4 Section 3: Priority 1 (critical: trace → scout-feasibility → listen) / Priority 2 (non-critical) / Priority 3 (evidence-heavy) |
| C-06 Rule trigger named | **PASS** | Phase 2: trigger recorded per auto-flagged namespace; Phase 3: "name which evaluation verdict drove the decision" |
| C-07 PM/Arch/Strategy shown | **PARTIAL** | Phase 3 output template is "- PM: [verdict] / - Architect: [verdict] / - Strategy: [verdict]" — three roles required but format is verdict-only with no sub-questions; could produce single-word verdicts ("adequate") without substantive evaluation |
| C-08 Tier flag respected | **PASS** | "State the tier: 'Tier: {N} (source: ...)'"; Phase 2 RULE TIER-CRITICAL gates on Tier >= 2 |
| C-09 Coverage gap synthesis | **FAIL** | Next-steps is a flat priority-ordered list with no risk synthesis |
| C-10 MOCK-ACCEPTED namespace-specific rationale | **FAIL** | Phase 3 decision format shows code only; no instruction to explain why the code applies to this specific namespace |

**Essential**: 5/5 = 1.0 | **Recommended**: (1 + 0.5 + 1)/3 = 2.5/3 = 0.833 | **Aspirational**: 0/2 = 0
**Composite**: (1.0 × 60) + (0.833 × 30) + (0 × 10) = 60 + 25 + 0 = **85**
**All essential pass**: YES

---

### V-04 (Combined) — Role Sequence + Phrasing Register: Strict Imperative

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | **PASS** | STEP 2 two-list partition + STEP 6 decide covers all namespaces; "DO NOT proceed until every namespace is placed in exactly one list" |
| C-02 Automatic rule correctness | **PASS** | Strongest enforcement: "DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality" + "DO NOT mark any Tier 2+ critical namespace MOCK-ACCEPTED" + "DO NOT apply PM/Architect/Strategy evaluation to any auto-flagged namespace" — all three forbidden outputs named explicitly |
| C-03 MOCK-ACCEPTED reason codes | **PASS** | STEP 6: "MUST include at least one reason code from this exact list: STRUCTURAL-COVERAGE-SUFFICIENT / DOMAIN-KNOWLEDGE-CONSISTENT. NEVER use any other reason code. NEVER paraphrase these codes." |
| C-04 Status write-back | **PASS** | STEP 8: "MUST update every Status line"; "MUST confirm"; "NEVER leave any Status field as MOCK (awaiting review) after this step. This is the defining action of /mock:review. It is not optional." |
| C-05 Next-steps priority order | **PASS** | STEP 7 "Next Steps (numbered, strict priority)" with Priority 1/2/3 explicit ordering |
| C-06 Rule trigger named | **PASS** | STEP 2: "trigger = {rule label}" for auto-flagged; STEP 6: "Name the specific evaluation that failed and why" |
| C-07 PM/Arch/Strategy shown | **PASS** | Separate dedicated STEPS 3, 4, 5 — each with "MUST assess... for each remaining namespace" plus specific diagnostic questions and required verdict per namespace; three-step architecture makes completion verifiable; verdicts precede STEP 6 decision |
| C-08 Tier flag respected | **PASS** | "WRITE at the top: 'Tier: {N} (source: ...)'"; RULE 2 in STEP 2 gates on tier >= 2 |
| C-09 Coverage gap synthesis | **FAIL** | STEP 7 next-steps uses priority ordering but no cross-namespace synthesis, grouping labels, or risk commentary |
| C-10 MOCK-ACCEPTED namespace-specific rationale | **FAIL** | STEP 6 codes annotated with "(when structural completeness drove the verdict)" but no instruction requiring a namespace-specific explanatory sentence attached to the code |

**Essential**: 5/5 = 1.0 | **Recommended**: 3/3 = 1.0 | **Aspirational**: 0/2 = 0
**Composite**: (1.0 × 60) + (1.0 × 30) + (0 × 10) = **90**
**All essential pass**: YES

---

### V-05 (Combined) — Output Format + Inertia Framing: Skip-Cost Column

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | **PASS** | Per-namespace entries + consolidated decision grid require coverage of all namespaces; "Write Status Back" edits every namespace |
| C-02 Automatic rule correctness | **PARTIAL** | "Apply before any role evaluation. Not subject to override by evaluation roles." + per-namespace "[If auto-flagged: skip PM/Architect/Strategy sections]" — inline conditional rather than hard gate; same structural weakness as V-02; no equivalent of V-01/V-03 STOP gate |
| C-03 MOCK-ACCEPTED reason codes | **PARTIAL** | Codes shown in decision template "{MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT \| DOMAIN-KNOWLEDGE-CONSISTENT]}" but no explicit "exact codes only / no paraphrase" instruction; the template implies the values but does not prohibit paraphrase |
| C-04 Status write-back | **PASS** | "**Write Status Back**" section: "This step is mandatory. The decision recorded in the review grid must exist in the source artifact. A Status field left as MOCK (awaiting review) is not coverage — it is unknown." |
| C-05 Next-steps priority order | **PASS** | "Ordered by skip cost (highest inertia risk first)" with Priority 1/2/3; inertia framing reinforces the ordering rationale |
| C-06 Rule trigger named | **PASS** | Per-namespace "Auto-flag: {REAL-REQUIRED (trigger) \| none}"; decision template: "REAL-REQUIRED [reason]" |
| C-07 PM/Arch/Strategy shown | **PASS** | Per-namespace PM/Architect/Strategy sections with one-to-two sentence requirement; Strategy framing ("What is the cost of not running the real skill?") pushes beyond structural adequacy toward evidential reasoning |
| C-08 Tier flag respected | **PASS** | "Tier used: {N} \| Source: ..." at top; TIER-CRITICAL rule checks Tier 2+ |
| C-09 Coverage gap synthesis | **PASS** | Next-steps Priority 1 header: "These are Tier 2 gates. Inertia here risks undetectable build constraints or adoption blockers at commit time." Priority 2: "Skip cost is moderate. Run after critical namespaces are VERIFIED." Priority 3: "Mock content is structurally correct but evidentially zero. No real run means no data." + skip-cost column in grid provides per-namespace risk annotation |
| C-10 MOCK-ACCEPTED namespace-specific rationale | **PASS** | Skip cost field for MOCK-ACCEPTED: "No evidence lost — structural coverage sufficient at Tier {tier}. [Name the specific structural property that supports acceptance.]" — requires namespace-specific structural reasoning by name |

**Essential**: (1 + 0.5 + 0.5 + 1 + 1)/5 = 4.0/5 = 0.80 | **Recommended**: 3/3 = 1.0 | **Aspirational**: 2/2 = 1.0
**Composite**: (0.80 × 60) + (1.0 × 30) + (1.0 × 10) = 48 + 30 + 10 = **88**
**All essential pass**: NO (C-02 PARTIAL, C-03 PARTIAL)

---

### Score Summary

| V | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Score | All Ess |
|---|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|------:|:-------:|
| V-01 | P | P | P | P | P | P | P | P | F | F | **90** | YES |
| V-02 | P | Pt | P | Pt | P | P | P | P | F | P | **83** | NO |
| V-03 | P | P | P | P | P | P | Pt | P | F | F | **85** | YES |
| V-04 | P | P | P | P | P | P | P | P | F | F | **90** | YES |
| V-05 | P | Pt | Pt | P | P | P | P | P | P | P | **88** | NO |

**Ranking**: V-01 = V-04 (90) > V-05 (88) > V-03 (85) > V-02 (83)

---

### Variation Comparison: V-01 vs V-04 (tied leaders)

Both score 90 with all essential pass. V-04 is the stronger variation on the criteria that matter most in failure analysis:

- **C-02**: V-04's DO NOT framing ("DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality") names the exact forbidden output. V-01's positive framing ("If Category == EVIDENCE-HEAVY → REAL-REQUIRED") states the rule but does not block the failure case directly. V-04 is more failure-resistant.
- **C-07**: V-04's three dedicated sweep steps (STEP 3 PM, STEP 4 Architect, STEP 5 Strategy) make role completion structurally verifiable. V-01's per-namespace grouping requires all three to be present but in a single phase where a compressed format is easier to produce.

**Winner by tie-break**: V-04

---

### Excellence Signals from V-04

1. **DO NOT gate naming the exact forbidden output** — "DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality" blocks the specific failure mode directly. Positive framing tells the model what to do in the normal case; negative framing blocks the error case. They are not equivalent. The DO NOT form is more effective when the failure mode is a specific identifiable output pattern.

2. **Separate role-sweep steps before decide** — PM sweep (STEP 3) → Architect sweep (STEP 4) → Strategy sweep (STEP 5) → Decide (STEP 6) makes three-role coverage verifiable without depending on per-namespace grouping discipline. Each role gets a full dedicated step with its own diagnostic questions and a required verdict-per-namespace output.

---

### Patterns Observed from V-05 (not top, but valuable for Round 2)

V-05 achieves both C-09 and C-10 — the aspirational criteria no other variation touches. Its mechanism:

- **Skip-cost column as C-09 forcing function** — asking "what evidence is lost if this namespace stays at MOCK?" produces the cross-namespace risk synthesis required by C-09 as a natural table output rather than a separate synthesis step. The column makes the inertia competitor visible in the artifact.
- **Strategy framing as cost-of-inaction** — "What Tier {tier} decision would be made incorrectly if this mock were treated as evidence?" inverts the evaluation from "is this mock adequate?" to "what is at risk if we accept it?" This shift produces namespace-specific reasoning for C-10 as a natural consequence of answering the question.

**Round 2 target**: Combine V-04's DO NOT gating (fix C-02, enforce C-03) with V-05's skip-cost column and inertia-framing Strategy prompt. Expected: all five essential + C-09 + C-10 = composite 100.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["DO NOT gate naming exact forbidden output blocks failure modes more effectively than positive-form rule statements — pair with positive rule for complete coverage", "Separate role-sweep steps (PM sweep → Architect sweep → Strategy sweep → Decide) make three-role compliance structurally verifiable without per-namespace grouping discipline", "Skip-cost column with inertia framing produces C-09 coverage gap synthesis as natural table output — preserving this in a variation with hard auto-flag gate is the Round 2 target"]}
```
