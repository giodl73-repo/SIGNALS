## /quest:score — mock-review Round 2

### Scoring Each Variation Against Rubric v2

---

#### V-01 — Forbidden-Output Enumeration (All Three Rules)

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Both lists required; "every namespace in exactly one list" before Phase 2 |
| C-02 Automatic rule correctness | P | Hard gate: "Do not begin Phase 2 until both lists complete." Rules stated non-overridable |
| C-03 MOCK-ACCEPTED reason codes | P | "At least one exact code... No paraphrase. No invented codes." |
| C-04 Status write-back | P | Phase 4 named mandatory, defined as "defining action" |
| C-05 Next-steps priority order | P | "Ordered by: critical namespaces first, evidence-heavy last." explicitly stated |
| C-06 Rule trigger named | P | Auto-flagged: trigger label per namespace; evaluation-driven: names the failing verdict |
| C-07 PM/Arch/Strategy shown | Pt | All three roles present with per-role questions; same phase block, no separate completable steps |
| C-08 Tier flag respected | P | Tier stated at top; RULE B gated on tier >= 2; Strategy verdict tied to tier |
| C-09 Coverage gap synthesis | F | Next-steps flat list only; no cross-namespace risk statement |
| C-10 MOCK-ACCEPTED namespace-specific rationale | F | Reason code required but no explanatory sentence per namespace |
| C-11 Forbidden-output enumeration | P | All three rules carry explicit DO NOT: EVIDENCE-HEAVY, TIER-CRITICAL, COMPLIANCE |
| C-12 Zero-remaining confirmation gate | F | Normative statement only ("Zero Status fields may remain") — not a required output |
| C-13 Verifiable role-step separation | F | PM/Architect/Strategy inline in Phase 2; no individual STOP gates or separate steps |

**Essential**: 5/5 = 1.0 | **Recommended**: 2.5/3 = 0.833 | **Aspirational**: 1/5 = 0.2
**Composite**: (1.0 × 60) + (0.833 × 30) + (0.2 × 10) = 60 + 25 + 2 = **87**
**All essential pass**: YES

---

#### V-02 — Zero-Remaining Confirmation Gate

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | STOP gate before Phase 3; both lists must be complete |
| C-02 Automatic rule correctness | P | Phase 2 auto-flagging before Phase 3 role eval; "mandatory and not role-overridable" |
| C-03 MOCK-ACCEPTED reason codes | P | "At least one code from this exact set... No paraphrase." |
| C-04 Status write-back | P | Phase 5 "defining action, cannot be skipped" |
| C-05 Next-steps priority order | P | Priorities 1–3 with ordering rule stated: "Critical first, evidence-heavy last." |
| C-06 Rule trigger named | P | Trigger label in Phase 2 output; failing evaluation verdict in Phase 3 |
| C-07 PM/Arch/Strategy shown | Pt | PM/Architect/Strategy in Phase 3 with brief questions; combined section, not separately completable |
| C-08 Tier flag respected | P | Tier at top; TIER-CRITICAL on tier >= 2; Strategy tests tier adequacy |
| C-09 Coverage gap synthesis | F | No cross-namespace risk or urgency grouping |
| C-10 MOCK-ACCEPTED namespace-specific rationale | F | Codes required but no explanatory sentence |
| C-11 Forbidden-output enumeration | F | Auto-rules stated as positive triggers only; no DO NOT phrasing |
| C-12 Zero-remaining confirmation gate | P | "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed." — explicitly required output; MUST NOT be written if any field missed |
| C-13 Verifiable role-step separation | F | PM/Architect/Strategy in single Phase 3 block |

**Essential**: 5/5 = 1.0 | **Recommended**: 2.5/3 = 0.833 | **Aspirational**: 1/5 = 0.2
**Composite**: (1.0 × 60) + (0.833 × 30) + (0.2 × 10) = 60 + 25 + 2 = **87**
**All essential pass**: YES

---

#### V-03 — Verifiable Role-Step Separation

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | "Every namespace in exactly one list. Do not begin Phase 2 until lists complete." |
| C-02 Automatic rule correctness | P | Phase 1 auto-flagging "not overridable" before Phase 2 role eval |
| C-03 MOCK-ACCEPTED reason codes | P | "At least one exact reason code required... No paraphrase." |
| C-04 Status write-back | P | Phase 5 "defining action, cannot be skipped" |
| C-05 Next-steps priority order | P | Priorities 1–3; ordering rule stated explicitly |
| C-06 Rule trigger named | P | Phase 1 trigger label; Phase 3 names failing evaluation |
| C-07 PM/Arch/Strategy shown | P | Three separately headed sections (#### PM, #### Architect, #### Strategy) each with 3 sub-questions, own verdict; PM asks to name specific sections |
| C-08 Tier flag respected | P | Tier at top; TIER-CRITICAL on tier >= 2; Strategy tests specific tier decision |
| C-09 Coverage gap synthesis | F | No cross-namespace synthesis paragraph |
| C-10 MOCK-ACCEPTED namespace-specific rationale | F | No explanatory sentence required |
| C-11 Forbidden-output enumeration | F | Positive-condition auto-rules only; no DO NOT statements |
| C-12 Zero-remaining confirmation gate | F | "Zero Status fields may remain..." is a closing normative statement, not a required output |
| C-13 Verifiable role-step separation | P | PM/Architect/Strategy each have own heading, 3 sub-questions, verdict, and sequential recording requirement before next role begins |

**Essential**: 5/5 = 1.0 | **Recommended**: 3/3 = 1.0 | **Aspirational**: 1/5 = 0.2
**Composite**: (1.0 × 60) + (1.0 × 30) + (0.2 × 10) = 60 + 30 + 2 = **92**
**All essential pass**: YES

---

#### V-04 — Forbidden-Output + Verifiable Role-Step (Combined)

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | "DO NOT proceed until every namespace is placed in exactly one list." |
| C-02 Automatic rule correctness | P | STEP 2 before STEP 3-5; "None is optional or role-overridable"; DO NOT gates on all three rules |
| C-03 MOCK-ACCEPTED reason codes | P | "NEVER use any other reason code. NEVER paraphrase these codes." |
| C-04 Status write-back | P | STEP 8 "MUST update every Status line... not optional" |
| C-05 Next-steps priority order | P | "Critical first, evidence-heavy last." stated with Priority 1–3 ordering |
| C-06 Rule trigger named | P | STEP 2 trigger label; STEP 6 "Name the specific evaluation that failed and the sub-question answer that drove it" |
| C-07 PM/Arch/Strategy shown | P | STEP 3, 4, 5 separately headed; 3 sub-questions each; PM asks to "Name at least one section that is present"; Architect: "Name the element"; Strategy: "What specific Tier {tier} decision depends on this namespace" |
| C-08 Tier flag respected | P | Tier at top; RULE 2 gated on tier >= 2; Strategy STEP 5 references tier explicitly |
| C-09 Coverage gap synthesis | F | No cross-namespace risk paragraph |
| C-10 MOCK-ACCEPTED namespace-specific rationale | F | No explanatory sentence required per namespace |
| C-11 Forbidden-output enumeration | P | All three rules: RULE 1 "regardless of mock quality, mock content depth, or PM/Architect/Strategy evaluation outcome"; RULE 2 "cannot be waived by evaluation quality"; RULE 3 "Compliance signals require real evidence" |
| C-12 Zero-remaining confirmation gate | F | STEP 8 has MUST confirm lines but no count-and-confirm required output |
| C-13 Verifiable role-step separation | P | STEP 3, 4, 5 as separately headed, separately gated evaluations with 3 sub-questions each and "DO NOT proceed to Step N+1 until verdicts written for every namespace" |

**Essential**: 5/5 = 1.0 | **Recommended**: 3/3 = 1.0 | **Aspirational**: 2/5 = 0.4
**Composite**: (1.0 × 60) + (1.0 × 30) + (0.4 × 10) = 60 + 30 + 4 = **94**
**All essential pass**: YES

---

#### V-05 — Pre-Printed Skeleton (Combined)

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Pre-printed tables for auto-flagged and remaining; "Fill this skeleton completely." |
| C-02 Automatic rule correctness | P | PHASE 1 fires before PHASE 2–4; phase structure enforces separation; rules listed as categorical |
| C-03 MOCK-ACCEPTED reason codes | P | PHASE 5: "Valid MOCK-ACCEPTED reason codes (exact, no paraphrase):" listed |
| C-04 Status write-back | P | PHASE 8 "mandatory" with full verification requirement |
| C-05 Next-steps priority order | P | PHASE 7 has ordering rule stated: "Critical REAL-REQUIRED namespaces first (trace-*, then scout-feasibility, then listen-*), non-critical second, evidence-heavy last." |
| C-06 Rule trigger named | P | PHASE 1 auto-flagged table has Trigger column; PHASE 5 Decisions table has Reason Code column |
| C-07 PM/Arch/Strategy shown | P | PHASE 2, 3, 4 as separate phases with pre-printed "### PM: [Namespace]", "### Architect: [Namespace]", "### Strategy: [Namespace]" per namespace with fill-in prompts for sections, gates, contradictions, tier decisions |
| C-08 Tier flag respected | P | Tier line pre-printed; TIER-CRITICAL has "(Tier 2+ only)"; PHASE 4 Strategy asks "Tier [N] decision at stake" |
| C-09 Coverage gap synthesis | P | PHASE 7 pre-prints "**Coverage gap synthesis:**" block with fill instruction: cross-namespace risk, interdependencies, gate-blocker vs informational vs evidence-only urgency grouping |
| C-10 MOCK-ACCEPTED namespace-specific rationale | F | PHASE 5 Decisions table has Reason Code column; no explanatory sentence slot pre-printed |
| C-11 Forbidden-output enumeration | F | PHASE 1 auto-rules positive-condition only; no DO NOT phrasing |
| C-12 Zero-remaining confirmation gate | P | PHASE 8 pre-prints "**Required verification output — do not omit this line:**" with "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed." embedded in skeleton |
| C-13 Verifiable role-step separation | P | PHASE 2, 3, 4 as separately headed phases; each has pre-printed "### [Role]: [Namespace]" section with "**[Role] Verdict: [...]**" pre-printed at bottom — model fills, cannot omit |

**Essential**: 5/5 = 1.0 | **Recommended**: 3/3 = 1.0 | **Aspirational**: 3/5 = 0.6
**Composite**: (1.0 × 60) + (1.0 × 30) + (0.6 × 10) = 60 + 30 + 6 = **96**
**All essential pass**: YES

---

### Round 2 Rankings

| V | Score | All Essential | Notes |
|---|-------|--------------|-------|
| V-05 | 96 | YES | C-09 + C-12 + C-13 via pre-printed skeleton |
| V-04 | 94 | YES | C-11 + C-13 via forbidden-output + step separation |
| V-03 | 92 | YES | C-13 via separate role sections |
| V-01 | 87 | YES | C-11 via all-three DO NOT; C-07 partial |
| V-02 | 87 | YES | C-12 via count-and-confirm output; C-07 partial |

---

### Excellence Signals from V-05

**1. Pre-printed fill blocks guarantee section presence at zero model-generation risk**
V-05 achieves C-09, C-12, and C-13 through pre-printing rather than instruction. "Coverage gap synthesis:" is a pre-printed paragraph header the model fills. "Count: 0 Status fields remain…" is a pre-printed skeleton line marked "do not omit." Role section headers are pre-printed per namespace. The model cannot omit what it did not generate — this is structurally different from telling a model to include something.

**2. Skeleton embedding outperforms normative statements for verification gates**
V-02 and V-03 both failed C-12 with normative statements ("Zero Status fields may remain as MOCK"). V-05 passes C-12 by embedding the exact required output string in the skeleton with "Required verification output — do not omit this line:" — the count line becomes a fill-in-the-blank operation rather than a generation task. The distinction: normative states what must be true; skeleton states what must be written.

---

```json
{"top_score": 96, "all_essential_pass": true, "new_patterns": ["Pre-printed fill blocks guarantee section presence at zero model-generation risk — the model cannot omit what it did not generate, making skeleton-embedded elements structurally stronger than instruction-based inclusion requirements", "Skeleton embedding outperforms normative statements for verification gates — embedding the exact required output string in the pre-printed skeleton converts generation tasks into fill operations, preventing omission more reliably than normative 'must include' instructions"]}
```
