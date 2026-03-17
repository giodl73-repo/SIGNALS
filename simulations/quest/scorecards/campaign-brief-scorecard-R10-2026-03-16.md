## Quest Score — campaign-brief / Round 10

**Rubric v9 | 29 criteria | 290 pts max**

---

### V-01: Preamble-only, no TOKEN-PRESSURE GUARD

| Criterion | Result | Evidence |
|---|---|---|
| C-01–C-24 (foundation block) | PASS ×24 | All foundational criteria met; variations do not degrade the base structure |
| C-25 | PASS | TOKEN-PRESSURE GUARD named rule present for zero-signal synthesis; preamble placement ensures positional availability of the rule |
| C-26 | PASS | VERDICT COMPRESSION GUARD present; `action:` sub-labels protected against verdict compression |
| C-27 | PARTIAL | TOKEN-PRESSURE GUARD exists (C-25 PASS) but does not explicitly name conditional-dormancy as the failure mode prevented; unconditional-firing declaration absent — preamble placement is a positional guard, not a declarative failure-mode guard |
| C-28 | PASS | VERDICT COMPRESSION GUARD declares `action:` as mandatory invariant, not merely format extension |
| C-29 | PARTIAL | Positional mechanism present (preamble placement of zero-signal rule) but declarative mechanism absent; if preamble section is processed without rule absorption, no guard clause compensates — dual-mechanism independence not achieved |

**Score: 270/290** *(C-27 PARTIAL −10, C-29 PARTIAL −10)*

---

### V-02: Declarative-only (mid-doc guard, no preamble)

| Criterion | Result | Evidence |
|---|---|---|
| C-01–C-24 (foundation block) | PASS ×24 | All foundational criteria met |
| C-25 | PASS | TOKEN-PRESSURE GUARD named rule present |
| C-26 | PASS | VERDICT COMPRESSION GUARD present |
| C-27 | PASS | Guard explicitly names conditional-dormancy as the failure mode prevented by unconditional firing; failure mode declared, not implied |
| C-28 | PASS | `action:` declared as mandatory invariant |
| C-29 | PARTIAL | Declarative mechanism present (named guard clause with failure-mode framing) but positional mechanism absent — guard clause placed mid-document where token pressure can suppress it before processing; if the guard clause itself is elided under compression, no positional fallback compensates |

**Score: 280/290** *(C-29 PARTIAL −10)*

---

### V-03: C-29 generalized to VERDICT action: rule

| Criterion | Result | Evidence |
|---|---|---|
| C-01–C-24 (foundation block) | PASS ×24 | All foundational criteria met |
| C-25 | PASS | TOKEN-PRESSURE GUARD named rule present for zero-signal synthesis |
| C-26 | PASS | VERDICT COMPRESSION GUARD present |
| C-27 | PASS | TOKEN-PRESSURE GUARD names conditional-dormancy failure mode |
| C-28 | PASS | `action:` declared as mandatory invariant |
| C-29 | PARTIAL | Dual-mechanism applied to the VERDICT `action:` rule (C-26 domain) rather than the zero-signal synthesis rule (C-25 domain); C-29's structural chain runs through C-24 (timestamp isolation) and C-25 (zero-signal) — applying the principle to a different compression-critical rule does not satisfy the independence requirement on that chain; credit is not earnable by substituting a different rule domain |

**Score: 280/290** *(C-29 PARTIAL −10)*

---

### V-04: R9 V-05 form (preamble + guard, VERDICT guard)

| Criterion | Result | Evidence |
|---|---|---|
| C-01–C-24 (foundation block) | PASS ×24 | All foundational criteria met |
| C-25 | PASS | TOKEN-PRESSURE GUARD named rule present |
| C-26 | PASS | VERDICT COMPRESSION GUARD present |
| C-27 | PASS | Guard names conditional-dormancy failure mode via unconditional-firing declaration; the failure the rule prevents is explicitly identified, not left implicit |
| C-28 | PASS | `action:` declared mandatory invariant with explicit hardening against last-block COMPRESSED scenarios |
| C-29 | PASS | Both mechanisms present on the zero-signal synthesis rule: preamble placement (positional — rule encountered before token pressure builds) + declarative TOKEN-PRESSURE GUARD naming conditional-dormancy (declarative — rule survives cases where preamble is processed without rule absorption); each mechanism compensates for the other's independent failure mode |

**Score: 290/290**

---

### V-05: Dual-mechanism on BOTH compression-critical rules

| Criterion | Result | Evidence |
|---|---|---|
| C-01–C-24 (foundation block) | PASS ×24 | All foundational criteria met |
| C-25 | PASS | TOKEN-PRESSURE GUARD named rule present |
| C-26 | PASS | VERDICT COMPRESSION GUARD present |
| C-27 | PASS | Guard names conditional-dormancy failure mode |
| C-28 | PASS | `action:` declared as mandatory invariant |
| C-29 | PASS | Dual-mechanism generalized to BOTH compression-critical rules (zero-signal synthesis + timestamp isolation); each rule independently guarded by preamble position AND declarative failure-mode clause; strongest possible form of C-29 compliance — suppressing either mechanism on either rule still leaves the other active |

**Score: 290/290**

---

### Composite Rankings

| Rank | Variation | Score | Key differentiator |
|---|---|---|---|
| 1 (tie) | V-04 | 290/290 | Preamble + declarative guard on zero-signal rule; VERDICT guard present |
| 1 (tie) | V-05 | 290/290 | Extends V-04 — dual-mechanism applied to timestamp isolation rule as well |
| 3 (tie) | V-02 | 280/290 | Declarative guard present (C-27 PASS) but missing positional mechanism for C-29 |
| 3 (tie) | V-03 | 280/290 | All named criteria present but C-29 applied to wrong rule domain |
| 5 | V-01 | 270/290 | Positional only — C-27 and C-29 both PARTIAL |

---

### R10 Investigation Results

**C-29 dual-mechanism independence: VALIDATED**

- V-01 (preamble-only): C-29 PARTIAL — positional mechanism alone is insufficient
- V-02 (declarative-only): C-29 PARTIAL — declarative mechanism alone is insufficient
- Neither mechanism alone achieves C-29 PASS. The independence requirement stands. The criterion should not be narrowed.

**C-29 rule-domain specificity (V-03): PARTIAL confirms domain-binding**

- Applying dual-mechanism to the VERDICT `action:` rule (C-26 domain) does not satisfy C-29
- C-29 is not rule-agnostic — it requires the dual-mechanism on the C-24/C-25 chain specifically
- V-03 score of 280 (not 290) falsifies the rule-agnostic hypothesis

---

### Excellence Signals (V-04 and V-05)

**From V-04:**
1. **Preamble-as-positional-anchor** — zero-signal rule in preamble guarantees encounter before token pressure accumulates; structural placement rather than instruction-following
2. **Failure-mode naming as guard activation** — declaring conditional-dormancy by name gives the model a failure mode to avoid rather than an abstract instruction to follow; the named failure mode is the mechanism, not a description of it
3. **Independent-failure compensation made explicit** — each mechanism covers a distinct failure scenario; naming both in context of the same rule makes the compensation relationship visible rather than structural-only

**From V-05 (future criterion candidate):**
4. **Dual-mechanism generalization principle** — applying positional + declarative dual-mechanism to all compression-critical rules within a shared preamble block creates a compression-immune structural contract; suppressing any one rule requires suppressing the entire preamble; this generalizes C-29 from a per-rule requirement to a skill-architecture pattern

---

```json
{"top_score": 290, "all_essential_pass": true, "new_patterns": ["Dual-mechanism generalization across all compression-critical rules in a shared preamble block creates a compression-immune structural contract — suppressing any single rule requires suppressing the entire preamble, not just a mid-document section", "Failure-mode naming as guard activation: declarative guards that name the specific failure mode they prevent (conditional-dormancy) are more robust than guards that declare unconditional firing without naming the failure class — the named failure mode becomes the enforcement target"]}
```
