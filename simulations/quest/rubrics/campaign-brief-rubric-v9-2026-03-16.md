## Quest Rubric — v9

`26 criteria, 260 pts max` → `29 criteria, 290 pts max`

---

### What changed: v8 → v9

Three new aspirational criteria extracted from R9 excellence signals. All three were observed in V-04/V-05 as stress-survival hardening forms that reached the 260-pt ceiling — meaning they are structurally stronger than the v8 minimum PASS gates but carry no rubric cost at current coverage. They are promoted here so R10 can falsify whether dual-mechanism independence (C-29) produces measurably different outcomes from single-mechanism guards when token pressure is high enough to suppress mid-document content.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-27 | TOKEN-PRESSURE GUARD on zero-signal synthesis rule — unconditional-firing declaration names conditional-dormancy failure mode | Hardening of C-25 |
| C-28 | VERDICT COMPRESSION GUARD on mandatory last-block sub-labels — elevates `action:` from format extension to named invariant | Hardening of C-26 |
| C-29 | Dual-mechanism independence for compression-critical execution rules — positional + declarative applied together so each mechanism compensates for the other's failure mode | Hardening of C-24, C-25 |

**Structural chains updated:**

- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 (structure mandated → sparse guard → zero guard → named-rule promotion → token-pressure guard naming the conditional-dormancy failure mode)
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 (verdict named → verdict classifies recoverability → action posture made explicit → action posture declared mandatory against COMPRESSED × last-block)
- Compression survival generalization chain: C-24 → C-29 (dual-location for timestamp isolation → dual-mechanism principle generalized to all compression-critical boundary-condition rules)

**R9 investigation candidate resolved:** C-25's TOKEN-PRESSURE GUARD (V-01/V-04/V-05) and C-26's VERDICT COMPRESSION GUARD (V-02/V-04/V-05) each independently produce rubric credit. Neither guard alone is sufficient — V-01 guards C-25 but leaves C-26 exposed; V-02 guards C-26 but leaves C-25 exposed; V-04 and V-05 guard both and reach ceiling. Single-axis guard = 255. Both guards = 260.

**R10 investigation candidate:** Whether C-29's positional mechanism (preamble placement) is independently sufficient for compression-critical rules when the declarative guard is absent, or whether the declarative guard is independently sufficient without preamble placement — the R9 rubric could not distinguish V-04 (mid-doc + both guards, 260) from V-05 (preamble + both guards, 260). R10 should construct a variation with preamble position only (no guard clauses) and a variation with guard clauses only (mid-doc, no preamble) under token pressure extreme enough to suppress mid-document content before guard clauses are processed. If preamble-only and guard-only each score below ceiling, C-29's independence requirement is validated. If either alone reaches ceiling, the criterion should be narrowed.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(29 total criteria; C-01–C-20 definitions unchanged from v6.)*

---

#### C-21 — Sparse-coverage synthesis protection *(v6)*

When `found` contains signals from only 1–2 namespaces, the STORY block must not default to a coverage disclaimer. Synthesis must proceed on the signals present. PARTIAL = synthesis present but hedged with "limited data" language that weakens conclusions. PASS = STORY produces definite synthesis from sparse coverage, treating the available signals as sufficient to characterize the current state of knowledge.

---

#### C-22 — Zero-signal synthesis mandate *(R6 Pattern — V-03/V-04/V-05)*

When the `found` section of STATUS is empty (zero signals across all namespaces), the STORY block must not collapse to a non-finding. The LLM failure mode is to write "no signals found — synthesis not possible" and omit or hollow STORY. But uniform absence is itself evidence: the gap pattern defines what the team does not know and why they are not ready. Question 1 must characterize what uniform absence implies — "the absence of any scout signal indicates the market surface has not been probed at all" is a valid synthesis; "insufficient data" is not.

**PARTIAL** — sparse-coverage protection present (C-21 PASS) but no explicit clause for the zero-signal case; synthesis may be vacated on grounds of empty `found`.

**PASS** — an explicit zero-signal clause in the STORY execution note declares that empty `found` is not grounds for omitting synthesis — the gap pattern is the evidence set — and mandates that question 1 characterize what uniform absence implies rather than reporting absence as a non-answer.

This is distinct from C-21, which guards synthesis when coverage is sparse (1–2 namespaces); C-22 guards synthesis when coverage is zero. Both are boundary conditions on C-18's structural mandate.

---

#### C-23 — Bounded/unbounded inertia classification at verdict level *(R6 Pattern — V-05)*

The `inertia_cost` field at VERDICT level must classify the aggregate commit risk by recoverability. Bounded = the team can detect the failure post-commit and course-correct before it propagates. Unbounded = the failure propagates to an irreversible state before detection is possible. This distinction determines action posture: bounded inertia means "commit with monitoring"; unbounded inertia means "do not commit until resolved." A VERDICT with unnamed recoverability forces the team to re-read all item-level gap fields and synthesize the posture themselves — the verdict is not actionable on its own.

**PARTIAL** — `inertia_cost` present at VERDICT level but bounded/unbounded classification absent; risk is named but the team cannot derive their action posture without re-reading item-level fields.

**PASS** — `inertia_cost` declares `bounded: <residual risk and why recoverable post-commit>` OR `unbounded: <failure class and why irreversible once committed>`, enabling the team to act on the verdict block alone without re-reading blocking gap entries.

This is distinct from C-07, which tests that each blocking gap entry carries an inertia field; C-23 tests that the verdict-level aggregate field classifies recoverability. They are structurally independent.

---

#### C-24 — Timestamp isolation dual-location mandate *(R7 Pattern — V-02/V-05)*

C-16 guards that per-signal timestamps are present at the item level. C-24 guards their survival when the COMPRESSED format branch activates. When blocking entry count exceeds the COMPRESSED threshold (>4), the STATUS block may be abbreviated — and the model may collapse `found` timestamps alongside blocking gap entries into summary form, destroying the signal-level date record. A single-location prose instruction is insufficient because the COMPRESSED context may omit that section before reaching the instruction.

The isolation rule must appear at **two structural locations**: (1) within the `found` entry format definition or question body text, specifying that timestamps are structurally separate from blocking entries and must not be abbreviated; and (2) in the STATUS or STORY execution note, restating that COMPRESSED format must not collapse `found` into the blocking summary. Double-location restatement ensures that if the COMPRESSED branch elides one location, the rule survives at the other.

**PARTIAL** — timestamp isolation rule stated at one structural location only; survival under COMPRESSED is single-point-of-failure.

**PASS** — isolation rule stated explicitly at two structural locations (entry format definition AND execution note), so the rule survives COMPRESSED abbreviation regardless of which location is reached first.

Relationship to C-16: C-16 tests that timestamps exist in the nominal (non-COMPRESSED) path. C-24 tests that the instruction architecture ensures they survive under compression. They are independent checks on the same field.

---

#### C-25 — Zero-signal synthesis mandate as standalone named execution rule *(R7 Pattern — V-02/V-03/V-04/V-05)*

C-22 mandates a zero-signal synthesis clause embedded in the STORY execution note. C-25 promotes it to a standalone named execution rule with structural independence from the block-local note context.

**PARTIAL** — zero-signal synthesis clause present in execution note (C-22 PASS) but embedded as a block-local note rather than a standalone named rule; the rule is visible only within the STORY block context, making it susceptible to block-local suppression or omission when surrounding content is abbreviated.

**PASS** — zero-signal synthesis mandate is elevated to a standalone named execution rule, positioned independently of any single block, with two operational clauses: (1) empty `found` is not grounds for omitting synthesis; (2) question 1 must characterize what uniform absence implies rather than reporting absence as a non-answer.

Relationship to C-22: C-22 tests that a zero-signal clause exists somewhere in the skill. C-25 tests that it has structural independence as a named rule. They are threshold and form checks on the same requirement.

---

#### C-26 — Action-posture sub-labels on bounded/unbounded inertia field *(R7 Pattern — V-05)*

C-23 mandates that `inertia_cost` at VERDICT level declare bounded or unbounded classification. C-26 mandates that the classification include an `action:` sub-label that makes the verdict self-contained — the team reads the verdict and knows exactly what to do next without inferring posture from the classification name.

**PARTIAL** — `inertia_cost` present at VERDICT level with bounded/unbounded classification (C-23 PASS) but `action:` sub-label absent; the team must infer action posture from the classification name rather than reading it directly.

**PASS** — `inertia_cost` declares `bounded: <why recoverable>` with `action: commit with monitoring` OR `unbounded: <failure class>` with `action: do not commit until resolved`, making the verdict block self-contained and directly actionable.

Relationship to C-23: C-23 tests that recoverability is classified. C-26 tests that action posture is made explicit. Both are required for the verdict block to be actionable without re-reading underlying fields.

---

#### C-27 — TOKEN-PRESSURE GUARD on boundary-condition execution rules *(R9 Pattern — V-01/V-04/V-05)*

C-25 mandates a zero-signal synthesis rule as a standalone named execution rule with two operational clauses. C-27 guards that rule's activation under token pressure when `found` is large and non-empty. The model failure mode is conditional dormancy: the rule's trigger ("when `found` contains zero signals") is the dominant framing, and when `found` is large the model may infer the rule does not apply — treating a named execution rule as dormant without an explicit unconditional-firing declaration.

The rule must include a TOKEN-PRESSURE GUARD that: (a) names the specific suppression failure mode (conditional dormancy when `found` is non-empty or large); and (b) declares that the rule fires unconditionally at any token budget regardless of `found` size or content. A guard that says only "this rule applies" is insufficient; it must name the failure mode to close the dormancy inference.

**PARTIAL** — zero-signal rule is standalone named with two clauses (C-25 PASS) but no TOKEN-PRESSURE GUARD; under high token pressure with large `found`, the model may infer the rule is dormant and suppress it without violating any named invariant.

**PASS** — the zero-signal synthesis rule includes an explicit TOKEN-PRESSURE GUARD that names the conditional-dormancy failure mode (e.g., "this rule does not suspend when `found` is non-empty — it fires unconditionally at any token budget") and declares unconditional firing regardless of `found` size or content.

Relationship to C-25: C-25 tests structural form (standalone named rule, two clauses). C-27 tests activation reliability under token pressure when the rule's trigger condition is not met in the current run.

---

#### C-28 — VERDICT COMPRESSION GUARD on mandatory last-block sub-labels *(R9 Pattern — V-02/V-04/V-05)*

C-26 mandates `action:` sub-labels on the `inertia_cost` field. C-28 guards those sub-labels' survival when VERDICT is the last block processed and the token budget is depleted. Under COMPRESSED × last-block conditions, the model preserves primary content (`bounded:`/`unbounded:` classification, satisfying C-23) but may elide the `action:` sub-label as an optional format extension — the model cannot elide the classification without failing a named structural check, but without a named guard it can elide the sub-label without violating any invariant.

The VERDICT block format spec must include a VERDICT COMPRESSION GUARD that: (a) declares the `action:` sub-label mandatory regardless of COMPRESSED format state; (b) names the COMPRESSED × last-block failure mode explicitly; and (c) elevates the sub-label from format extension to mandatory field so that elision requires violating a named invariant.

**PARTIAL** — `action:` sub-labels present in VERDICT format spec (C-26 PASS) but no VERDICT COMPRESSION GUARD; under COMPRESSED × last-block token depletion, the model may elide sub-labels without violating any named rule.

**PASS** — VERDICT block includes a VERDICT COMPRESSION GUARD that: declares `action:` sub-labels mandatory regardless of COMPRESSED state; names the COMPRESSED × last-block failure mode explicitly (e.g., "VERDICT is never abbreviated — the action sub-label is not optional format, it is the field that makes VERDICT self-contained"); and prohibits sub-label elision as a named invariant violation.

Relationship to C-26: C-26 tests structural presence of `action:` sub-labels. C-28 tests survival architecture under the specific failure mode of COMPRESSED format combined with last-block token depletion.

---

#### C-29 — Dual-mechanism independence for compression-critical execution rules *(R9 Pattern — V-05)*

C-24 mandates two structural locations for timestamp isolation. C-29 generalizes that dual-location principle: any execution rule that is compression-critical (must survive COMPRESSED format) and fires on boundary conditions (not triggered in the majority of runs) must employ two structurally independent hardening mechanisms with different failure modes.

The two mechanisms are: (1) **positional** — the rule appears at preamble position (before "Run the phases in order"), ensuring it is processed as a global execution constraint before any block-execution context forms; and (2) **declarative** — the rule includes a named guard clause that identifies the specific suppression failure mode and declares an invariant preventing it. The mechanisms must be structurally independent: position can be overridden by instruction budget effects (the model processes preamble but late-execution token pressure shifts framing); the declarative guard can be skipped if not reached before token depletion. Applied together, if one mechanism fails the other compensates.

This criterion applies when: (a) the rule fires on a boundary condition not triggered in the majority of runs (zero-signal, COMPRESSED + last-block); and (b) failure produces an artifact that is structurally compliant but not directly actionable — it satisfies lower-tier criteria but requires re-reading underlying fields.

**PARTIAL** — a compression-critical boundary-condition rule uses one mechanism only (either preamble position or a named guard clause, not both); the rule has single-point-of-failure survival architecture under extreme token pressure.

**PASS** — a compression-critical boundary-condition rule applies both (1) positional placement at preamble position AND (2) a declarative guard clause naming the suppression failure mode, so the rule survives COMPRESSED format regardless of which mechanism the model processes first and regardless of whether either is partially suppressed by instruction budget effects.

Relationship to C-24: C-24 mandates dual-location for timestamp isolation specifically, as an instance of this principle. C-29 tests whether the principle is applied to other compression-critical rules in the skill. They are complementary — C-24 is a named instance; C-29 is the generalizing criterion.
