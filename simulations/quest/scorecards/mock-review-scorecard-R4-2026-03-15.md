## Round 4 Scorecard — /quest:mock-review

**Rubric:** v4 | **Criteria:** C-01 through C-19 | **Aspirational denominator:** 11
**Formula:** `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/11 × 10)`

---

### Criterion Evaluation Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Decision completeness | P | P | P | P | P |
| **C-02** Auto rule correctness | P | P | P | P | P |
| **C-03** MOCK-ACCEPTED reason codes | P | P | P | P | P |
| **C-04** Status write-back | P | P | P | P | P |
| **C-05** Next-steps priority order | P | P | P | P | P |
| **C-06** Rule trigger named | Pt | Pt | **P** | Pt | **P** |
| **C-07** PM/Arch/Strategy shown | P | P | P | P | P |
| **C-08** Tier flag respected | P | P | P | P | P |
| **C-09** Coverage gap synthesis | F | F | F | F | **P** |
| **C-10** MOCK-ACCEPTED namespace rationale | Pt | Pt | Pt | Pt | Pt |
| **C-11** Forbidden-output enumeration | P | P | P | P | P |
| **C-12** Zero-remaining confirmation gate | P | P | P | P | P |
| **C-13** Verifiable role-step separation | P | P | P | P | P |
| **C-14** Sub-question answer citation | Pt | Pt | Pt | Pt | Pt |
| **C-15** Entity-naming sub-question grammar | P | P | P | P | P |
| **C-16** Canary confirmation (prohibited under failure) | P | P | P | P | P |
| **C-17** Auto-flagged contamination guard | **P** | F | F | **P** | **P** |
| **C-18** Inter-step gate with next-step reference | Pt | **P** | Pt | **P** | **P** |
| **C-19** Structured trigger notation | F | F | **P** | F | **P** |

P = PASS (1.0) · Pt = PARTIAL (0.5) · F = FAIL (0.0)

---

### Evidence Notes

**V-01 — Named Contamination Error**

- **C-17 PASS**: STEP 2 appends: *"Applying role evaluation to a namespace already decided by an automatic rule is a named error: **auto-rule contamination**. This error is detectable by inspection."* Error has a label; a reviewer can ask "is auto-rule contamination present?" and audit by inspection. Rule prohibition upgraded to diagnosable error state.
- **C-18 PARTIAL**: STEP 3→4 gate: "DO NOT proceed to Step 4 until PM verdicts written" ✓. STEP 4→5: "DO NOT proceed to Step 5 until Architect verdicts written" ✓. STEP 1 gate: "DO NOT proceed until all fields extracted" — missing "to STEP 2" ✗. STEP 2 gate: "DO NOT proceed until every namespace placed in exactly one list" — missing "to STEP 3" ✗. Conservative C-18 reading requires all gates.
- **C-19 FAIL**: Auto-flag listing uses `trigger = {label}` (lowercase, equals). STEP 6 auto-flagged template uses `Trigger: [label]` (uppercase T, colon). Two notations co-exist; field not mechanically parseable with single rule.
- **C-06 PARTIAL**: `trigger = ` in listing context; evaluation-driven REAL-REQUIRED template has no trigger field at all (only "Failing evaluation: [PM | Architect | Strategy]").

**V-02 — All-Gate Forward Naming**

- **C-18 PASS**: All seven inter-step gates now forward-name: STEP 1 "DO NOT proceed to STEP 2", STEP 2 "DO NOT proceed to STEP 3", STEP 3 "DO NOT proceed to STEP 4", STEP 4 "DO NOT proceed to STEP 5", STEP 5 "DO NOT proceed to STEP 6", STEP 6 "DO NOT proceed to STEP 7", STEP 7 "DO NOT proceed to STEP 8." Conservative reading fully covered.
- **C-17 FAIL**: No named contamination error. Guard is present ("DO NOT apply evaluation to auto-flagged namespace") but error has no label — same gap as R3 V-05.
- **C-19 FAIL**: Notation unchanged from R3 V-05: dual format persists.
- **C-06 PARTIAL**: Same as V-01 — no trigger field in evaluation-driven template.

**V-03 — Unified Trigger Field Notation**

- **C-19 PASS**: STEP 6 opens with structural field note: *"The `trigger` field is a named artifact field in a fixed position — second line of every REAL-REQUIRED block, third line of every MOCK-ACCEPTED block (where it is `trigger = n/a`). Value drawn from this enumeration: Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE; Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE; MOCK-ACCEPTED: n/a. Uses lowercase `trigger` and equals-sign notation in all positions."* Single canonical format; fixed position declared; complete enumeration.
- **C-06 PASS**: Evaluation-driven template now carries `trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}`. All decision types have a trigger field. Evaluation-driven REAL-REQUIRED decisions now name which evaluation role drove the verdict via a parseable field.
- **C-18 PARTIAL**: STEP 3→4 and STEP 4→5 gates forward-name. STEP 1, STEP 2, and STEP 5 gates do not include forward reference. Narrower coverage than V-02.
- **C-17 FAIL**: No named contamination error.

**V-04 — Combined: Named Contamination Error + All-Gate Forward Naming**

- **C-17 PASS**: Same named error block as V-01 in STEP 2.
- **C-18 PASS**: All seven gate positions forward-name as in V-02.
- **C-19 FAIL**: STEP 6 auto-flagged template retains uppercase `Trigger:` colon notation. No unified trigger field note. Evaluation-driven template has no trigger field. No `trigger = n/a` for MOCK-ACCEPTED. Three-format gap remains.
- **C-06 PARTIAL**: Same as V-01/V-02 — evaluation-driven template missing trigger field.

**V-05 — Ceiling: C-17 + C-18 + C-19 + C-09**

- **C-17 PASS**: Named contamination error block from V-01. ✓
- **C-18 PASS**: All seven gates forward-name from V-02. ✓
- **C-19 PASS**: Structural field note and unified `trigger = ` notation from V-03. ✓
- **C-09 PASS**: STEP 7 pre-printed skeleton contains four mandatory sections with `(none)` suppression: Priority 1 (critical REAL-REQUIRED, blocker), Priority 2 (non-critical REAL-REQUIRED), Priority 3 (evidence-heavy REAL-REQUIRED), and a required *Cross-namespace risk statement* slot: `"Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk} — urgency: {BLOCKING | HIGH | MEDIUM}"`. Urgency grouping is present via Priority 1/2/3 triage AND explicit urgency classification on the single highest-risk gap. Not a flat priority list — the cross-namespace identification and urgency assignment satisfy the criterion.
- **C-06 PASS**: Unified trigger field from V-03 reaches evaluation-driven decisions. ✓
- **C-10 PARTIAL**: Rationale sentence is required ("why this code applies to this specific namespace") but the template does not ask for a comparative statement — it does not require explaining why this namespace's structural pattern makes real evidence unnecessary vs. what would require real evidence. The rationale is confirmatory, not contrastive.
- **C-14 PARTIAL**: Sub-question answer citation template is `"[The exact SQ answer — name the specific section, element, gap, or decision; not a restatement of the verdict]"`. The distinction from a verdict restatement is stated as a negative prohibition but there is no named failure mode or positive structural signal (e.g., a field format that forces present-tense artifact naming vs. past-tense assessment). A reviewer reading the output cannot mechanically distinguish a genuine SQ answer from a verdict restatement without judgment.

---

### Score Computation

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | **Total** |
|-----------|----------------|------------------|-------------------|-----------|
| V-01 | 5/5 = **60** | 2.5/3 = **25** | 7.5/11 = **6.8** | **91.8** |
| V-02 | 5/5 = **60** | 2.5/3 = **25** | 7.0/11 = **6.4** | **91.4** |
| V-03 | 5/5 = **60** | 3/3 = **30** | 7.5/11 = **6.8** | **96.8** |
| V-04 | 5/5 = **60** | 2.5/3 = **25** | 8.0/11 = **7.3** | **92.3** |
| **V-05** | 5/5 = **60** | 3/3 = **30** | 10.0/11 = **9.1** | **99.1** |

**Rank:** V-05 > V-03 > V-04 > V-01 > V-02

---

### Ranking Explanation

**V-05** wins on every contested criterion. The decisive gaps:

- V-03 vs V-05: V-03 achieves C-06 and C-19 (unified trigger) but fails C-17 and C-18, losing 2.7 aspirational points and 5 recommended (C-06 PARTIAL in V-04 costs 5 pts). Wait — V-03 actually gets C-06 PASS but loses on C-17 (no named error) and C-18 (partial gate coverage). Net effect: V-03 gets 30 recommended but only 6.8 aspirational vs. V-05's 9.1.
- V-04 vs V-05: V-04 gets C-17 and C-18 but loses C-19 and C-06 (PARTIAL), costing 5 recommended points and 0.7 aspirational. V-05 captures all four target criteria plus preserves all R3 V-05 strengths.

**Discriminating result from V-05:** The cross-namespace risk statement passes C-09 structurally — the mandatory slot with urgency classification and the explicit "name the specific Tier N decision at risk" format compels cross-namespace synthesis rather than a per-namespace restatement. The skeleton's `(none)` suppression rule for empty sections is a key structural guarantee not present in any earlier variation.

---

### Excellence Signals from V-05

**Signal 1 — Pre-printed skeleton with `(none)` suppression**

V-05's STEP 7 pre-prints the full Priority 1/2/3/Cross-namespace skeleton before asking the model to fill it. Sections with no entries require `(none)` — they cannot be silently omitted. This is categorically different from an ordering rule: an ordering rule tells the model what order to write; a pre-printed skeleton makes the omission of a section structurally visible. The pattern: *mandatory output sections pre-declared with explicit empty-slot markers prevent structural omission under long evaluation phases*. This generalizes beyond next-steps — any high-stakes output section (e.g., canary confirmation block, cross-tier risk statement) could use the pre-printed skeleton technique.

**Signal 2 — Urgency triage as a required output contract, not as a derived observation**

The cross-namespace risk statement requires: `urgency: {BLOCKING | HIGH | MEDIUM}`. The urgency label is not a recommendation — it is a required output field drawn from a closed enumeration. This upgrades the risk statement from a prose observation to a structured decision input. The pattern: *assigning a required urgency label from a closed enum to the highest-risk gap converts a synthesis observation into an actionable decision signal*. Opens a path for C-09 to require urgency triaging across ALL REAL-REQUIRED namespaces (not just the single highest-risk), which would distinguish a genuine cross-namespace synthesis from a restatement of Priority 1.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Pre-printed mandatory output skeleton with (none) suppression: pre-declaring all Next Steps sections as named slots prevents structural omission under long evaluation phases — a model must write (none) rather than silently skip a section, making omission visible without reviewer expertise", "Urgency triage as required closed-enum output field: assigning BLOCKING/HIGH/MEDIUM to the cross-namespace risk statement converts it from a prose observation into an actionable decision input — opens C-09 to a stricter criterion requiring urgency triaging across all REAL-REQUIRED namespaces rather than naming only the single highest-risk gap"]}
```
