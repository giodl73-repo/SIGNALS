## Round 3 Scoring — /quest:mock-review (v3 Rubric)

---

### V-01 — Entity-Naming Sub-Question Grammar

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Phase 1 two-list output, "every namespace in exactly one list" |
| C-02 Automatic rule correctness | P | Rules A/B/C defined before Phase 2; "not role-overridable"; STOP gate present |
| C-03 MOCK-ACCEPTED reason codes | P | Exact codes named; "No paraphrase. No invented codes." |
| C-04 Status write-back | P | Phase 5 Edit in-place; "defining action of /mock:review" |
| C-05 Next-steps priority order | P | Priority 1/2/3 with "Critical first, evidence-heavy last" stated |
| C-06 Rule trigger named | P | Auto-flagged: `trigger = {rule label}`; eval-driven: "name the evaluation that failed and the verdict" |
| C-07 PM/Arch/Strategy shown | P | Three separate evaluation blocks; all sub-questions in "Name X" form referencing sections/gates/components/decisions |
| C-08 Tier flag respected | P | Tier stated at top; TIER-CRITICAL gates on tier >= 2 |
| C-09 Coverage gap synthesis | F | Priority-ordered list only; no cross-namespace risk statement |
| C-10 MOCK-ACCEPTED namespace rationale | P | "Include one sentence stating why the reason code applies to this specific namespace" |
| C-11 Forbidden-output enumeration | F | Rules state Action/trigger only; no "DO NOT mark EVIDENCE-HEAVY MOCK-ACCEPTED" phrasing |
| C-12 Zero-remaining confirmation gate | P | Confirmation required; "DO NOT write the count-zero confirmation" if any field missed |
| C-13 Verifiable role-step separation | P | PM/Architect/Strategy each in own labeled block with sub-questions, verdict, and completion gate |
| C-14 Sub-question answer citation | F | No [SUB-QUESTION ANSWER] slot in decision template; eval-driven REAL-REQUIRED just says "name the evaluation that failed" |
| C-15 Entity-naming sub-question grammar | P | All nine sub-questions in "Name X" / "What specific X" form; no yes/no openers |
| C-16 Canary confirmation | F | R2-style prohibition only; no CANARY-FALSE-POSITIVE named error |

**Essential:** 5/5 × 60 = **60** | **Recommended:** 3/3 × 30 = **30** | **Aspirational:** 4/8 × 10 = **5**
**V-01 Total: 95**

---

### V-02 — Canary Confirmation Framing

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Phase 2 two-list output with completeness gate |
| C-02 Automatic rule correctness | P | Three rules before Phase 3; STOP gate; "mandatory and not role-overridable" |
| C-03 MOCK-ACCEPTED reason codes | P | Exact codes; "Reason codes are exact. No paraphrase." |
| C-04 Status write-back | P | Phase 5 Edit in-place; "cannot be skipped" |
| C-05 Next-steps priority order | P | Priority 1/2/3; ordering rule stated |
| C-06 Rule trigger named | P | `trigger = {rule label}` for auto-flagged; `REAL-REQUIRED [failed evaluation verdict]` for eval-driven |
| C-07 PM/Arch/Strategy shown | Pt | Three roles with verdicts, but sub-questions are yes/no: "Are required sections present?" — PM doesn't reference named sections |
| C-08 Tier flag respected | P | Tier stated; TIER-CRITICAL correct |
| C-09 Coverage gap synthesis | F | No cross-namespace risk synthesis |
| C-10 MOCK-ACCEPTED namespace rationale | F | MOCK-ACCEPTED format shows codes only; no "one sentence stating why" |
| C-11 Forbidden-output enumeration | F | No DO NOT statements |
| C-12 Zero-remaining confirmation gate | P | Confirmation required; prohibition on failure |
| C-13 Verifiable role-step separation | F | PM/Architect/Strategy inline in single Phase 3 block; no separate headings or STOP gates between roles |
| C-14 Sub-question answer citation | F | No citation template |
| C-15 Entity-naming sub-question grammar | F | Yes/no openers throughout: "Are required sections present?", "Does content contradict...?" |
| C-16 Canary confirmation | P | CANARY OUTPUT named; "CANARY-FALSE-POSITIVE" named error; CANARY SUPPRESSED protocol on failure |

**Essential:** 5/5 × 60 = **60** | **Recommended:** 2.5/3 × 30 = **25** | **Aspirational:** 2/8 × 10 = **2.5**
**V-02 Total: 87.5**

---

### V-03 — Sub-Question Answer Citation Template

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | Two-list completeness gate |
| C-02 Automatic rule correctness | P | Three rules before Phase 2; "mandatory and not overridable by role" |
| C-03 MOCK-ACCEPTED reason codes | P | Exact codes; "no paraphrase" |
| C-04 Status write-back | P | Phase 5 Edit in-place; "defining action of /mock:review" |
| C-05 Next-steps priority order | P | Priority 1/2/3; "Critical first, evidence-heavy last" |
| C-06 Rule trigger named | P | Auto-flagged: `trigger = {rule label}`; REAL-REQUIRED template has "Failing evaluation" field |
| C-07 PM/Arch/Strategy shown | Pt | Three roles present, but sub-questions are yes/no: "Are required sections present? ... Would a PM accept...?" — no named artifacts in questions |
| C-08 Tier flag respected | P | Tier stated; TIER-CRITICAL correct |
| C-09 Coverage gap synthesis | F | No cross-namespace synthesis |
| C-10 MOCK-ACCEPTED namespace rationale | P | "Rationale: [One sentence explaining why the reason code applies to this specific namespace]" |
| C-11 Forbidden-output enumeration | F | No DO NOT statements for auto-rules |
| C-12 Zero-remaining confirmation gate | P | Confirmation required; "DO NOT write" prohibition on failure |
| C-13 Verifiable role-step separation | F | PM/Architect/Strategy inline in Phase 2 block; no separate STOP gates between roles |
| C-14 Sub-question answer citation | P | "Sub-question answer that drove this verdict: [Exact answer — name the specific section, element, or gap, not a restatement]"; "A REAL-REQUIRED decision that omits the sub-question answer field is incomplete" |
| C-15 Entity-naming sub-question grammar | F | Yes/no openers: "Are required sections present?", "Does mock content contradict...?", "Would a team making Tier {tier} decisions be adequately served?" |
| C-16 Canary confirmation | F | R2-style prohibition only; no canary framing or named error |

**Essential:** 5/5 × 60 = **60** | **Recommended:** 2.5/3 × 30 = **25** | **Aspirational:** 3/8 × 10 = **3.75**
**V-03 Total: 88.75**

---

### V-04 — Entity-Naming Grammar + Citation Template

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | STEP 2 two-list; "DO NOT proceed until every namespace is placed in exactly one list" |
| C-02 Automatic rule correctness | P | Three rules in STEP 2; "mandatory, none optional or role-overridable"; "DO NOT apply ... evaluation to any auto-flagged namespace" |
| C-03 MOCK-ACCEPTED reason codes | P | "exact codes only; both when both apply; no paraphrase" |
| C-04 Status write-back | P | STEP 8 "MUST update every Status line"; Edit tool; "not optional" |
| C-05 Next-steps priority order | P | STEP 7 Priority 1/2/3; ordering rule stated |
| C-06 Rule trigger named | P | Auto-flagged trigger in STEP 2; REAL-REQUIRED template has "Failing evaluation" + citation slot |
| C-07 PM/Arch/Strategy shown | P | STEP 3/4/5 each have entity-naming sub-questions referencing sections, gates, components, API shapes, tier decisions |
| C-08 Tier flag respected | P | Tier stated at top; TIER-CRITICAL gates on tier >= 2 |
| C-09 Coverage gap synthesis | F | Priority list only; no cross-namespace risk |
| C-10 MOCK-ACCEPTED namespace rationale | P | "Rationale: [One sentence: why this code applies to this specific namespace]" |
| C-11 Forbidden-output enumeration | F | No DO NOT statements on auto-rules; rules state only trigger condition and action |
| C-12 Zero-remaining confirmation gate | P | "MUST confirm: Count: 0..."; "DO NOT write the count-zero confirmation" if any missed |
| C-13 Verifiable role-step separation | P | STEP 3, STEP 4, STEP 5 are individually numbered with sub-questions, verdict line, and "DO NOT proceed to Step N+1 until..." gate |
| C-14 Sub-question answer citation | P | STEP 6 citation slot: "name the specific section, element, gap, or decision; not a restatement of the verdict" |
| C-15 Entity-naming sub-question grammar | P | All sub-questions "Name X" / "What specific X"; no yes/no openers |
| C-16 Canary confirmation | F | R2-style prohibition only; no CANARY-FALSE-POSITIVE named error |

**Essential:** 5/5 × 60 = **60** | **Recommended:** 3/3 × 30 = **30** | **Aspirational:** 5/8 × 10 = **6.25**
**V-04 Total: 96.25**

---

### V-05 — Ceiling Combination

| Criterion | Rating | Evidence |
|-----------|--------|---------|
| C-01 Decision completeness | P | STEP 2 two-list; completeness gate before STEP 3 |
| C-02 Automatic rule correctness | P | Three rules before any evaluation; "mandatory, none optional or role-overridable"; explicit evaluation block exclusion |
| C-03 MOCK-ACCEPTED reason codes | P | "exact codes only; both when both apply; no paraphrase; NEVER invent codes" |
| C-04 Status write-back | P | STEP 8 "MUST update every Status line"; Edit tool; "defining action, not optional" |
| C-05 Next-steps priority order | P | STEP 7 Priority 1/2/3; "Critical first, evidence-heavy last" stated |
| C-06 Rule trigger named | P | Auto-flagged trigger in STEP 2; REAL-REQUIRED citation template has Failing evaluation + sub-question answer slot |
| C-07 PM/Arch/Strategy shown | P | STEP 3/4/5 entity-naming sub-questions reference named sections, gates, components, API shapes, tier decisions; block-level constraint enforces artifact answers |
| C-08 Tier flag respected | P | Tier stated; TIER-CRITICAL gates correctly |
| C-09 Coverage gap synthesis | F | Priority-ordered list only; no cross-namespace risk statement in STEP 7 |
| C-10 MOCK-ACCEPTED namespace rationale | P | "Rationale: [One sentence: why this code applies to this specific namespace]" |
| C-11 Forbidden-output enumeration | P | RULE 1: "DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality... or evaluation outcome"; RULE 2: "DO NOT mark any Tier 2+ critical namespace MOCK-ACCEPTED"; RULE 3: "DO NOT mark any compliance-tagged namespace MOCK-ACCEPTED when compliance context is active" — all three covered |
| C-12 Zero-remaining confirmation gate | P | Canary line required on success |
| C-13 Verifiable role-step separation | P | STEP 3, STEP 4, STEP 5 separately numbered with sub-questions, verdict, and STOP gate |
| C-14 Sub-question answer citation | P | STEP 6 citation slot with "not a restatement of the verdict" constraint in slot label |
| C-15 Entity-naming sub-question grammar | P | All sub-questions "Name X"; block-level preamble: "Each sub-question requires a named artifact in the answer — not a yes/no judgment" |
| C-16 Canary confirmation | P | CANARY OUTPUT named; "CANARY-FALSE-POSITIVE" as protocol error; CANARY SUPPRESSED output on failure |

**Essential:** 5/5 × 60 = **60** | **Recommended:** 3/3 × 30 = **30** | **Aspirational:** 7/8 × 10 = **8.75**
**V-05 Total: 98.75**

---

## Composite Score Summary

| V | Essential | Recommended | Aspirational | **Total** | All-Ess |
|---|-----------|-------------|--------------|-----------|---------|
| V-01 | 60 (5/5) | 30 (3/3) | 5.00 (4/8) | **95.00** | Y |
| V-02 | 60 (5/5) | 25 (2.5/3) | 2.50 (2/8) | **87.50** | Y |
| V-03 | 60 (5/5) | 25 (2.5/3) | 3.75 (3/8) | **88.75** | Y |
| V-04 | 60 (5/5) | 30 (3/3) | 6.25 (5/8) | **96.25** | Y |
| **V-05** | **60 (5/5)** | **30 (3/3)** | **8.75 (7/8)** | **98.75** | **Y** |

**Rank:** V-05 > V-04 > V-01 > V-03 > V-02

---

## Excellence Signals from V-05

**1. Block-level artifact constraint as step preamble**
V-04 had entity-naming sub-questions but no structural enforcement. V-05 adds a block-level gate before each role step: "Each sub-question requires a named artifact in the answer — not a yes/no judgment." This operates at the role-step level, not the question level — the constraint cannot be satisfied by answering one question correctly and skipping the grammar on the others.

**2. Named-error semantics for the canary**
V-02 introduced the prohibition. V-05 elevates it: CANARY-FALSE-POSITIVE names the error condition, and CANARY SUPPRESSED names the required output when suppression occurs. The failure path now produces a specific artifact rather than just withholding the success artifact. This transforms a behavioral rule into a verifiable protocol — a reviewer can distinguish "canary absent because skipped" from "canary suppressed because fields were missing."

**3. Forbidden-output phrasing anchored to cause, not just outcome**
V-05's DO NOT statements include the reason: "regardless of mock quality, mock content depth, or PM/Architect/Strategy evaluation outcome" (EVIDENCE-HEAVY) and "The critical designation applies at the structural level and cannot be waived by evaluation quality" (TIER-CRITICAL). This closes the loophole where a model might reason "the mock is very thorough, so the rule probably doesn't apply here."

**Only remaining gap:** C-09 (coverage gap synthesis) has been untouched across all three rounds — it requires a cross-namespace risk statement in the Next Steps section, not just priority ordering. A single-axis R4 variation adding a pre-printed risk synthesis skeleton to STEP 7 would complete the rubric.

---

```json
{"top_score": 98.75, "all_essential_pass": true, "new_patterns": ["Block-level artifact constraint as role-step preamble ('Each sub-question requires a named artifact — not a yes/no judgment') enforces entity-naming structurally across the entire step, not just per-question grammar", "Named-error semantics for canary failure: CANARY-FALSE-POSITIVE names the error condition and CANARY SUPPRESSED names the required failure-path output, making the prohibition falsifiable by inspection rather than behavioral-only", "Forbidden-output phrasing anchored to cause ('regardless of evaluation outcome', 'cannot be waived by evaluation quality') closes the loophole where a model might reason around the rule when mock quality is high"]}
```
