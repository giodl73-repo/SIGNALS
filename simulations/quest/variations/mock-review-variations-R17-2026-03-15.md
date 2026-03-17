[C-18] [C-28]:
DO NOT proceed to Step 4 (PM Evaluation) until architect-verdict recorded for all non-blocked namespaces.

---

## STEP 4: PM EVALUATION [C-07]

BEGIN PHASE 4. Final structural completeness check.
APPLY to namespaces not blocked at Step 3.

For each namespace:

| Row # | Sub-question [C-15] | Answer |
|-------|---------------------|--------|
| 1 | Name the section or table covering each required structural element. | {answer} |
| 2 | Name any structural element absent from the mock that the spec requires. | {answer} |
| 3 | Name the gate or table confirming the Status field is correctly formed. | {answer} |

RECORD verdicts:

| Namespace | pm-verdict |
|-----------|:----------:|
| {ns} | COMPLETE / INCOMPLETE / PARTIAL |

END PHASE 4.

---

## DECISION OUTPUT [C-40]

PRODUCE one block per namespace.

**MOCK-ACCEPTED:**
```
namespace: {name}
decision: MOCK-ACCEPTED
reason = STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT
Structural position: [C-23] [C-30] Feeds tier decision: {Strategy Row 1 answer}
Contrast: [C-20] [C-25] {Contrastive sentence naming the factor absent here that is present
  in namespaces like trace or scout-feasibility — the specific factor whose absence places
  this namespace below the REAL-REQUIRED threshold. Required form: "This namespace has no
  [factor], so structural coverage is sufficient — unlike [example namespace] where [factor]
  would require real evidence."}
```

**REAL-REQUIRED:**
```
namespace: {name}
decision: REAL-REQUIRED
trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE | EVALUATION-DRIVEN}
Artifact state: [C-14] [C-21] {Present-tense artifact observation: "Section X shows Y".
  VERDICT ECHO ERROR: "Role found Y" is prohibited.
  STRUCTURAL RULE: present-tense artifact naming ("Section 3.2 lists no fallback path")
  vs past-tense assessment restatement ("Architect found no fallback path").}
```

---

## STEP 5: WRITE-BACK [C-04]

EDIT each source mock artifact in-place. SET Status field per decision:
- MOCK-ACCEPTED → `Status: MOCK-ACCEPTED`
- REAL-REQUIRED → `Status: REAL-REQUIRED`

**CANARY CONFIRMATION [C-12] [C-16]:**
REQUIRED OUTPUT: "Zero Status: MOCK (awaiting review) fields remain."
CANARY ERROR: DO NOT write this output if any Status field remains `MOCK (awaiting review)`.
VIOLATION NAME: CANARY-PREMATURE — writing the confirmation when the condition is not met.

---

## STEP 6: NEXT-STEPS [C-05] [C-09] [C-24]

ORDERING RULE (stated explicitly): Tier-critical first because they gate tier-advancement.
Evidence-heavy last because real evidence collection is an independent workstream.

PRIORITY:
1. Tier-critical REAL-REQUIRED (trace, scout-feasibility, listen)
2. Evaluation-driven REAL-REQUIRED (by artifact state severity)
3. Automatic REAL-REQUIRED (evidence-heavy, compliance)

FORMAT: `/{skill-id} {topic} — {artifact state}`

CROSS-NAMESPACE RISK: STATE combined failure mode if highest-priority cluster is unresolved.
NAME the cluster. NAME the tier-advancement consequence.
```

---

## Variation Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Axis** | Lifecycle emphasis | Output format | Phrasing register | Role seq + Inertia | All combined |
| **Role order** | Strategy→Arch→PM | Arch→Strategy→PM | Strategy→Arch→PM | Strategy→Arch→PM | Strategy→Arch→PM |
| **C-35** | PASS | FAIL | PASS | PASS | PASS |
| **C-36** | FAIL | PASS | FAIL | FAIL | FAIL |
| **C-42** | PARTIAL (TRIAD header unlabeled) | FAIL (only C-40 blocks) | PASS (universal) | PARTIAL (TRIAD header unlabeled) | PASS (universal) |
| **C-43** | FAIL (inline SQ-N:) | PASS (Row # col) | FAIL (inline SQ-N:) | PASS (Row # col) | PASS (Row # col) |
| **Distinguishing feature** | Explicit begin/end per phase | All SQs in tables; Arch-first | `[C-27]` on TRIAD header; imperative verbs | Inertia reminder at every step heading | All four axes; `[C-15]` in table column header |
