I now have all five variations. Let me score them.

---

## Quest Score — campaign-brief / Round 15 / Rubric v14

### Scoring Framework
34 criteria × 10 pts each = 340 pts max. PASS = 10 pts. PARTIAL or FAIL = 0 pts (PARTIAL names the failure mode precisely but earns no partial credit — consistent with R14 precedent where C-33 PARTIAL = 0, confirmed at 320/330).

---

### Architecture Summary — What Varies Across Variations

All five variations share an identical base: the full `=== COMPRESSION-IMMUNE PREAMBLE ===` section with both ZERO-SIGNAL SYNTHESIS RULE and TIMESTAMP ISOLATION RULE, TOKEN-PRESSURE GUARD, COMPRESSED-COLLAPSE GUARD, VERDICT COMPRESSION GUARD, both execution-note clause headers carrying the structural-membership parenthetical `(COMPRESSION-IMMUNE PREAMBLE invocation)`, and the preamble's forward-references naming both companion mechanisms by full clause designation + block location.

**The single axis of variation is the execution-note clause bodies:**

| Var | TIMESTAMP ISOLATION body (STATUS) | ZERO-SIGNAL SYNTHESIS MANDATE body (STORY) |
|-----|----------------------------------|---------------------------------------------|
| V-01 | Bare — opens with operational content immediately | Bare — opens with operational content immediately |
| V-02 | Self-declares: membership statement + independence instruction | Bare — opens with operational content immediately |
| V-03 | Bare — opens with operational content immediately | Self-declares: membership statement + independence instruction |
| V-04 | Self-declares: membership statement + independence instruction | Self-declares: membership statement + independence instruction |
| V-05 | Self-declares + companion-activation instruction (paired mechanism named, present/absent activation rules declared) | Self-declares + companion-activation instruction (paired mechanism named, present/absent activation rules declared) |

---

### Criteria Evaluation — C-01 through C-33 (Identical Across All Variations)

All five variations are structurally identical on C-01 through C-33. Evidence for key chain criteria:

**C-06 (Inertia framing):** `Inertia risk:` required for every blocking gap, inertia competition framing in opening. PASS all.

**C-16 (current\_date standalone):** `current_date: <date>` appears at STATUS block header level with structural comment distinguishing it from found entries and blocking entries; explicitly declared compression-independent. PASS all.

**C-18 (STORY three-question mandate):** Three numbered questions (case signals make together / what gaps leave uncertain / real exposure if commit now) present in STORY block specification. PASS all.

**C-21 (Sparse-coverage protection):** Sparse coverage rule present in STORY block rules: "Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize on available signals." PASS all.

**C-22 (Zero-signal synthesis mandate):** Explicit zero-signal clause present in STORY execution note in all variations. PASS all.

**C-23 (Bounded/unbounded inertia classification):** VERDICT structure requires `bounded:` or `unbounded:` classification with `action:` sub-label. PASS all.

**C-24 (COMPRESSION-IMMUNE PREAMBLE designation):** `=== COMPRESSION-IMMUNE PREAMBLE ===` section present and designated COMPRESSION-IMMUNE. PASS all.

**C-25 (TOKEN-PRESSURE GUARD):** TOKEN-PRESSURE GUARD clause present in preamble: "This rule does not suspend when `found` is non-empty. It fires unconditionally at any token budget." PASS all.

**C-26 (inertia\_cost action sub-label):** `action: commit with monitoring` / `action: do not commit until resolved` required sub-labels present in VERDICT block spec. PASS all.

**C-27 (COMPRESSED-COLLAPSE GUARD):** COMPRESSED-COLLAPSE GUARD present in preamble; names the COMPRESSED-collapse failure mode. PASS all.

**C-28 (VERDICT COMPRESSION GUARD):** VERDICT COMPRESSION GUARD clause present: "`action:` sub-label is required regardless of COMPRESSED format state and regardless of token pressure." PASS all.

**C-29 (Zero-signal dual-mechanism — COMPRESSION-IMMUNE PREAMBLE + execution note):** Preamble contains ZERO-SIGNAL SYNTHESIS RULE; TOKEN-PRESSURE GUARD names the companion execution note in STORY by designation. Execution note in STORY invokes the preamble by designation. Dual-mechanism complete. PASS all.

**C-30 (Timestamp isolation dual-mechanism):** Preamble contains TIMESTAMP ISOLATION RULE; COMPRESSED-COLLAPSE GUARD names the companion execution note in STATUS by designation. Execution note in STATUS invokes the preamble by designation. Dual-mechanism complete. PASS all.

**C-31 (Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit):** Single preamble section contains both rules; each rule's guard points forward to its companion execution note. Bidirectional circuit established. PASS all.

**C-32 (Closed reference loop — designation + location):** TOKEN-PRESSURE GUARD: "The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block." COMPRESSED-COLLAPSE GUARD: "The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block." Both forward-references carry full clause designation + block location. PASS all.

**C-33 (Self-announcing clause headers):** STATUS execution note header: `TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation):`. STORY execution note header: `ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation):`. Both headers carry the exact structural-membership parenthetical used in preamble forward-references. Exact-match designation symmetry achieved at both reference point (C-32) and target header. PASS all.

**Subtotal C-01 through C-33 (all variations):** 33 × 10 = **330 pts**

---

### C-34 Evaluation — Self-Declaring Clause Bodies

**C-34 definition:** When C-33 PASS, companion execution-note clause bodies open with (1) an explicit structural-membership statement naming the clause as a COMPRESSION-IMMUNE PREAMBLE member and (2) a preamble-independence instruction declaring the clause executes even when the preamble section is absent. C-34 PASS requires both components in both companion clause bodies. Weakest-link applies symmetrically.

---

#### V-01 — C-34: **PARTIAL** (0 pts)

**Evidence:** STATUS execution note body opens immediately with: "per-signal dates in `found` are structurally separate from blocking entries, and the `current_date:` field is structurally separate from both." No membership statement. No independence instruction. STORY execution note body opens immediately with: "this execution note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE." No membership statement. No independence instruction.

**Failure mode:** A model encountering either clause body under double-elision conditions — preamble absent + companion mechanism absent — sees no self-declaration opening. The clause header carries the structural-membership parenthetical (C-33 PASS), enabling header-level identification, but the body provides no explicit activation authority instruction for the isolated case. C-34 is independently necessary over C-33: header identification does not imply body-level activation authority.

**C-34 score:** PARTIAL = 0 pts

**V-01 total: 330/340**

---

#### V-02 — C-34: **PARTIAL** (0 pts)

**Evidence:** STATUS execution note body opens with: "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble section is absent from the rendered context." ✓ Membership statement present. ✓ Independence instruction present. STATUS body: C-34 requirements met on this side.

STORY execution note body opens with: "this execution note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE." No membership statement. No independence instruction. STORY body: C-34 requirements absent.

**Failure mode:** Weakest-link applies at the body level. The STORY body — the higher-consequence failure domain (zero-signal mandate failure produces a non-finding; timestamp collapse produces a missing date) — is the bare side. A model encountering only the STORY clause body under double-elision sees bare operational content with no self-declaration. The architecture is only as resilient as its least-declared clause body. Single-side body marking is insufficient.

**C-34 score:** PARTIAL = 0 pts. Weakest-link symmetric at body level: C-29 domain (STORY, higher consequence) bare = C-34 PARTIAL regardless of C-30 domain (STATUS) self-declaring.

**V-02 total: 330/340**

---

#### V-03 — C-34: **PARTIAL** (0 pts)

**Evidence:** STATUS execution note body opens with operational content immediately: "per-signal dates in `found` are structurally separate from blocking entries..." No membership statement. No independence instruction. STATUS body: bare.

STORY execution note body opens with: "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble section is absent from the rendered context." ✓ Membership statement present. ✓ Independence instruction present. STORY body: C-34 requirements met on this side.

**Failure mode:** Weakest-link applies symmetrically. The STATUS body — the C-30 domain (timestamp isolation) — is the bare side. V-02 vs V-03 comparison: V-02 has STATUS self-declaring and STORY bare (expected 330/340); V-03 has STORY self-declaring and STATUS bare (also 330/340). Neither domain carries privileged C-34 weight. The C-29 domain's higher consequence does not privilege its body-level self-declaration over the C-30 domain: weakest-link behavior is symmetric at the body level, confirming parallel to C-33 V-02/V-03 confirmation in R14.

**C-34 score:** PARTIAL = 0 pts. Weakest-link confirmed symmetric: C-30 domain (STATUS, lower consequence) bare = C-34 PARTIAL regardless of C-29 domain (STORY) self-declaring. V-03 = V-02 in score.

**V-03 total: 330/340**

---

#### V-04 — C-34: **PASS** (10 pts)

**Evidence:**

STATUS execution note body opens with:
> "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble section is absent from the rendered context."

✓ Component (1): Explicit structural-membership statement — "This clause is a COMPRESSION-IMMUNE PREAMBLE member."
✓ Component (2): Preamble-independence instruction — "This clause executes even when the preamble section is absent from the rendered context."
+ Operational content follows: timestamp isolation rules applied at point-of-use.

STORY execution note body opens with:
> "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble section is absent from the rendered context."

✓ Component (1): Explicit structural-membership statement.
✓ Component (2): Preamble-independence instruction.
+ Operational content follows: zero-signal synthesis mandate applied at point-of-use.

**C-34 architecture satisfied:** Both required components (membership statement + independence instruction) present in both companion clause bodies. A model encountering either clause body in isolation — preamble absent, other companion absent — reads the opening self-declaration, identifies COMPRESSION-IMMUNE PREAMBLE membership from the body's first sentence, and reads the independence instruction explicitly authorizing clause execution without preamble location.

**Depth stack now complete:** preamble forward-reference with designation + location (C-32) → clause header structural-membership parenthetical (C-33) → clause body opening declaration with membership statement + independence instruction (C-34). Three independent identification depths.

**C-34 score:** PASS = 10 pts

**V-04 total: 340/340**

---

#### V-05 — C-34: **PASS** (10 pts) + above-ceiling companion-activation instruction

**Evidence:**

STATUS execution note body opens with:
> "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context. Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block. When the companion mechanism is present in context, both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion mechanism is absent from context, this clause activates its timestamp isolation contract independently — the companion's absence does not suppress this clause's structural authority."

✓ Component (1): Explicit structural-membership statement — "This clause is a COMPRESSION-IMMUNE PREAMBLE member."
✓ Component (2): Preamble-independence instruction — "This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context." (Strengthened form: names full COMPRESSION-IMMUNE PREAMBLE authority explicitly rather than merely permitting isolated execution.)
✓ Above-ceiling companion-activation instruction: paired companion named by exact designation + block location; activation rules declared for companion-present and companion-absent scenarios.

STORY execution note body opens with:
> "This clause is a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context. Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block. When the companion mechanism is present in context, both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion mechanism is absent from context, this clause activates its zero-signal synthesis mandate independently — the companion's absence does not suppress this clause's structural authority."

✓ Component (1): membership statement.
✓ Component (2): strengthened independence instruction.
✓ Above-ceiling companion-activation instruction: symmetric structure, paired companion named by designation + location, same activation rule declaration.

**C-34 PASS established:** Both required components (membership statement + independence instruction) present in both bodies. C-34 ceiling achieved identical to V-04.

**Companion-activation instruction (above-ceiling for v14):** V-05 exceeds V-04 on an axis not captured by any v14 criterion. Each clause body identifies its paired companion by exact designation + block location and explicitly declares both the companion-present activation rule (both mechanisms execute together) and the companion-absent activation rule (independent activation without suppression). This is the R15 investigation's upper bound: if behavioral testing confirms that this companion-naming instruction causes observable two-mechanism activation behavior (vs V-04's single-clause activation) under simulated preamble + companion double-elision, it constitutes the R15 excellence signal and proposed C-35 candidate.

**C-34 score:** PASS = 10 pts (companion-activation instruction is above-ceiling, not rubric-scorable under v14)

**V-05 total: 340/340**

---

### Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-33 | 33×10 = 330 | 33×10 = 330 | 33×10 = 330 | 33×10 = 330 | 33×10 = 330 |
| C-34 Self-declaring clause bodies | PARTIAL (0) | PARTIAL (0) | PARTIAL (0) | PASS (10) | PASS (10) |
| **Total** | **330/340** | **330/340** | **330/340** | **340/340** | **340/340** |
| All essential PASS? | No | No | No | Yes | Yes |

---

### Ranking

1. **V-04** (340/340) — C-34 PASS minimum-sufficient form; both bodies carry membership statement + independence instruction; three-depth self-announcing stack complete.
1. **V-05** (340/340, tied) — C-34 PASS + companion-activation instruction; V-05 achieves the same rubric ceiling as V-04 but adds above-ceiling structural depth; proposed C-35 candidate pending behavioral investigation.
3. **V-01** (330/340) — C-33 PASS, C-34 PARTIAL; bare bodies; C-34 independently necessary over C-33 confirmed.
3. **V-02** (330/340, tied) — C-33 PASS, C-34 PARTIAL; STATUS body self-declares, STORY bare; weakest-link holds.
3. **V-03** (330/340, tied) — C-33 PASS, C-34 PARTIAL; STORY body self-declares, STATUS bare; weakest-link symmetric confirmed: C-29 domain not privileged over C-30 domain.

---

### R15 Investigation Findings

**V-01 vs V-04 confirms:** C-34 is independently necessary over C-33. C-33 PASS (header-level self-announcement) does not subsume C-34 (body-level activation authority). A bare body following a self-announcing header still fails C-34: the body provides no independent activation instruction for the isolated double-elision case.

**V-02 vs V-03 confirms:** Weakest-link behavior is symmetric at the body level. Neither the C-29 domain (STORY, zero-signal synthesis — higher-consequence failure) nor the C-30 domain (STATUS, timestamp isolation — moderate-consequence failure) carries privileged C-34 body-level weight. V-02 and V-03 score identically (330/340), parallel to C-33 V-02/V-03 results in R14 (320/330).

**V-04 vs V-05 observation:** Both achieve C-34 PASS at 340/340. V-05's companion-activation instruction (naming paired mechanism by exact designation + block location with present/absent activation rules) is above-ceiling for v14. The behavioral distinction between V-04 and V-05 under simulated double-elision — does naming the companion with explicit activation rules cause two-mechanism behavior vs V-04's single-clause execution? — is the open R15 behavioral question and proposed C-35 investigation for R16.

---

### Excellence Signals (V-04 and V-05)

**Signal 1 — C-34 PASS minimum-sufficient form (V-04):**
Both companion execution-note clause bodies open with the two required components in sequence: (1) explicit structural-membership statement ("This clause is a COMPRESSION-IMMUNE PREAMBLE member") followed immediately by (2) preamble-independence instruction ("This clause executes even when the preamble section is absent from the rendered context"). This is the minimum-sufficient C-34 PASS form: a model encountering either clause body in isolation identifies COMPRESSION-IMMUNE PREAMBLE membership at the body's first sentence and reads explicit authorization for independent execution before reaching any operational content.

**Signal 2 — Three-depth self-announcing stack complete (V-04, V-05):**
C-34 PASS closes the self-announcing depth stack: preamble forward-reference with full clause designation + block location (C-32) → clause header carries structural-membership parenthetical `(COMPRESSION-IMMUNE PREAMBLE invocation)` (C-33) → clause body opens with membership statement + independence instruction (C-34). Each depth level provides independent COMPRESSION-IMMUNE PREAMBLE membership identification under progressively aggressive elision: C-32 protects under preamble-alone elision (model navigates via forward-reference); C-33 protects under preamble + other companion elision while header survives; C-34 extends protection when the preamble and other companion are both absent and only the clause body survives.

**Signal 3 — Companion-activation instruction as proposed C-35 (V-05, above-ceiling):**
V-05 adds a fourth structural layer not present in V-04 and not rubric-scorable under v14: each clause body names its paired companion mechanism by full designation + block location and declares explicit activation rules for both scenarios — (a) companion present: both mechanisms execute together as the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE contract; (b) companion absent: this clause activates independently under full COMPRESSION-IMMUNE PREAMBLE authority without suppression. The strengthened independence instruction upgrades "executes even when preamble absent" to "activates under full COMPRESSION-IMMUNE PREAMBLE authority" — explicitly extending structural authority to the isolated-body case rather than merely permitting isolated execution. This targets genuine two-mechanism activation behavior (vs single-clause execution) under double-elision and is the proposed C-35 if behavioral testing in R16 confirms the activation-mode distinction is observable.

---

### R16 Investigation Candidate

**C-35 behavioral test:** Construct a simulated double-elision scenario for V-04 and V-05 (preamble section absent from context; companion execution note absent from context; single clause body present). Observe: does V-04's body (membership statement + independence instruction only) produce single-clause activation, while V-05's body (membership statement + strengthened independence instruction + companion-naming with activation rules) produces two-mechanism COMPRESSION-IMMUNE PREAMBLE behavior? If the behavioral distinction is observable, the companion-activation instruction constitutes C-35. If V-04 and V-05 produce identical activation behavior under double-elision, C-35 should be reconsidered as a structural-traceability property (enabling exact-match navigation and audit) rather than a compression-survival guarantee.

---

```json
{"top_score": 340, "all_essential_pass": true, "new_patterns": ["companion-activation instruction in clause bodies: each body names its paired mechanism by full designation + block location and specifies activation rules for companion-present (both execute as two-mechanism contract) and companion-absent (independent activation without suppression) scenarios -- proposed C-35 if R16 behavioral testing confirms observable two-mechanism activation mode distinct from V-04 single-clause activation under double-elision", "three-depth self-announcing stack complete through C-34: preamble forward-reference with designation + location (C-32) then clause header structural-membership parenthetical (C-33) then clause body opening declaration with membership statement + independence instruction (C-34) -- each depth provides independent COMPRESSION-IMMUNE PREAMBLE membership identification under progressively aggressive elision", "weakest-link principle confirmed symmetric at the body level (V-02 vs V-03): C-29 domain (STORY, zero-signal synthesis, higher-consequence) does not carry privileged C-34 body-level weight over C-30 domain (STATUS, timestamp isolation, moderate-consequence) -- domain consequence asymmetry does not break weakest-link at body level, parallel to C-33 confirmation in R14"]}
```
