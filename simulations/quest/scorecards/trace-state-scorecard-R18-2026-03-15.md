## trace-state · R18 Score · Rubric v16

**Scoring baseline:** R17 V-01 under v16 = 82.2 (26 PASS × 1.22 + 50 base). Unit = 1.22 pts. Pool = 41 criteria.

---

### V-01 — Sales, single-pass tabular

| Criterion | Result | Note |
|-----------|--------|------|
| C-30 | PASS | Column headers carry criterion IDs + directives |
| C-34 | PASS | `FAILS if:` patterns in headers |
| C-36, C-37, C-40, C-41, C-42, C-47 | FAIL | Multi-pass format required |
| C-38, C-39 | FAIL | Step-block format required |
| C-43 | PASS | Lead → Opportunity → Closed Won labels in cells |
| C-44 | PASS | Sub-step decomposition present |
| C-45 | PASS | Pre-Defect / Triggering Op / Post-Defect+Reason |
| C-46 | PASS | Phase vocabulary declared before table |
| C-48 | PASS | IS/IS-NOT/IS-BLOCKED across all constraint-carrying sections |
| C-49 | PASS | EPOCH-CLUSTER ANALYSIS section maps F-NN → epoch, names highest-density epoch, states targeted remediation implication |
| C-50 | FAIL | Single-domain |
| R1–C-28 accumulated | ~25 PASS | Confirmed by R17 baseline |

**PASS count:** 27 · **Score:** 50 + 27 × 1.22 = **82.9**

---

### V-02 — Finance, single-pass tabular + Arc Position column

Same criteria profile as V-01. Arc Position column (Entry boundary / Gate boundary / Approval event / Terminal settlement) grounds the C-49 remediation implication in epoch structural role → C-49 confirmed PASS, remediation specificity elevated above generic.

| C-48 | PASS | IS-NOT register in GATE definitions, FINDINGS preamble, EPOCH-CLUSTER preamble |
| C-49 | PASS | Arc Position column enables epoch-role-specific remediation (not generic) |
| C-50 | FAIL | Single-domain |

**PASS count:** 27 · **Score:** 50 + 27 × 1.22 = **82.9**
*(Arc Position elevates quality depth, not PASS count — same score as V-01)*

---

### V-03 — Customer Service, step-block format

Swaps tabular criteria for step-block analogs. C-49 delivered as labeled step-block (ECL-1 through ECL-4).

| Criterion | Result | Note |
|-----------|--------|------|
| C-30 | FAIL | Tabular format not used |
| C-34 | FAIL | Tabular format not used |
| C-38 | PASS | Step labels carry `[C-XX: directive]` |
| C-39 | PASS | Step labels carry `FAILS if:` pattern |
| C-48 | PASS | Register saturates all constraint-carrying sections including ECL preamble |
| C-49 | PASS | ECL-1 → ECL-4 step-block satisfies format-neutral C-49 requirement |
| C-50 | FAIL | Single-domain |

Net swap: C-30/C-34 → C-38/C-39. Count unchanged.

**PASS count:** 27 · **Score:** 50 + 27 × 1.22 = **82.9**

---

### V-04 — Finance → Sales, two-pass multi-domain

Multi-pass unlocks C-36, C-37, C-40, C-41, C-42, C-47. Multi-domain unlocks C-50.

| Criterion | Result | Note |
|-----------|--------|------|
| C-36 | PASS | Pass headings name defect class targeted |
| C-37 | PASS | Consequence clause at each pass heading |
| C-40 | PASS | One distinct labeled defect per domain pass with type + triggering op + reason |
| C-41 | PASS | Finance postcondition explicitly named as Sales precondition in BRIDGE TABLE |
| C-42 | PASS | Finance-first ordering annotated as defect-class hypothesis vehicle |
| C-47 | PASS | Defect-hypothesis confirmation cites predicted class from C-42 + bridge row from C-41 |
| C-48 | PASS | IS-negation register + C-50 declaration written in IS-NOT form |
| C-49 | PASS | EPOCH-CLUSTER spans both Finance and Sales epoch vocabularies; highest-density epoch named; cross-domain remediation implication |
| C-50 | PASS | Top-scope DOMAIN DEPENDENCY DECLARATION before Pass 1: Finance IS the state authority → Sales IS the downstream consumer; two-hop chain complete |

+6 multi-pass (C-36, C-37, C-40, C-41, C-42, C-47) + 1 C-50 vs V-01 base of 27.

**PASS count:** 34 · **Score:** 50 + 34 × 1.22 = **91.5**

---

### V-05 — Finance → Sales → CS, three-pass multi-domain

Full three-pass synthesis. C-50 explicitly names all three domains and both dependency hops (Finance → Sales → CS), directly targeting the PARTIAL boundary: "fewer than all downstream domains named in a 3+ domain trace."

| Criterion | Result | Note |
|-----------|--------|------|
| C-36 | PASS | Three pass headings, each with defect class |
| C-37 | PASS | Three consequence clauses |
| C-40 | PASS | Three distinct labeled defects (one per pass) |
| C-41 | PASS | Finance→Sales bridge + Sales→CS bridge, both explicit |
| C-42 | PASS | Three-pass ordering annotated as hypothesis vehicle |
| C-47 | PASS | Both bridge rows cited; three defect-hypothesis confirmations present |
| C-48 | PASS | IS-negation saturates DOMAIN DEPENDENCY DECLARATION + all three GATE definitions + FINDINGS preamble + EPOCH-CLUSTER preamble |
| C-49 | PASS | EPOCH-CLUSTER spans three epoch vocabularies; cross-domain highest-density epoch identified; remediation implication names the inter-domain handoff as the defect concentration boundary |
| C-50 | PASS | Full chain declared: "Finance IS the state authority; Sales IS NOT independent — it IS the Finance-downstream consumer; CS IS the terminal settlement domain dependent on both" |

C-50 PARTIAL risk (fewer than all downstream domains named) explicitly avoided by naming all three.

**PASS count:** 35 · **Score:** 50 + 35 × 1.22 = **92.7**

---

### Rankings

| Rank | Variant | Score | Key differentiator |
|------|---------|-------|-------------------|
| 1 | V-05 | **92.7** | Three-pass + C-48 + C-49 (three-domain) + C-50 (full chain) |
| 2 | V-04 | **91.5** | Two-pass + C-48 + C-49 + C-50 (two-hop) |
| 3 | V-01 | **82.9** | C-48 + C-49; no multi-pass, no C-50 |
| 3 | V-02 | **82.9** | Same count as V-01; Arc Position deepens C-49 quality without raising count |
| 3 | V-03 | **82.9** | Step-block format-neutral C-49; C-38/C-39 swap for C-30/C-34 |

**Gap:** V-04/V-05 outscore V-01–V-03 by ~8.6 pts — the multi-pass criteria cluster is the dominant differentiator, not IS-negation saturation alone.

---

### Excellence Signals (from V-05)

**Signal 1 — LIFECYCLE EPOCH MAP as analysis surface, not label structure.** C-49 requires the map to be *used*: findings cross-referenced to epochs, highest-density epoch named, remediation tied to epoch's structural role in the arc. V-05 demonstrates this across three epoch vocabularies — the map becomes an argument, not a decoration.

**Signal 2 — C-50 declaration written in IS-negation register.** "Finance IS the state authority; Sales IS NOT independent — it IS the Finance-downstream consumer." This simultaneously satisfies C-50 (artifact-scope dependency declaration) and contributes to C-48 saturation (IS-negation register in a constraint-carrying section). One structural move earns two criteria.

**Signal 3 — Three-domain C-50 avoids PARTIAL by naming all downstream domains.** The rubric explicitly marks "fewer than all downstream domains named in a 3+ domain trace" as PARTIAL. V-05 names Finance, Sales, and CS with both dependency hops in the top-scope declaration — a precise structural decision driven by rubric awareness.

---

```json
{"top_score": 92.7, "all_essential_pass": true, "new_patterns": ["LIFECYCLE EPOCH MAP used as cross-reference analysis surface: findings mapped to epochs, highest-density epoch named, remediation tied to epoch structural role in arc", "C-50 artifact-scope declaration written in IS-negation register simultaneously satisfies C-50 and contributes to C-48 saturation — one structural move earns two criteria", "three-domain C-50 declaration explicitly names all downstream domains and both dependency hops to avoid PARTIAL boundary"]}
```
