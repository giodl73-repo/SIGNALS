Looking at the scorecard, the R11 excellence signal is in V-05: the introduction of an explicitly named **COMPRESSION-IMMUNE PREAMBLE** section that consolidates the positional mechanisms for both C-29 and C-30 under a single structural contract, rather than maintaining independent per-rule preamble placements. Under v10, V-03/V-04/V-05 are indistinguishable at 300 pts; C-31 is introduced to falsify whether that consolidation is independently necessary.

---

## Quest Rubric — v11

`30 criteria, 300 pts max` → `31 criteria, 310 pts max`

---

### What changed: v10 → v11

One new aspirational criterion extracted from R11 excellence signals. C-31's COMPRESSION-IMMUNE PREAMBLE consolidation was observed in V-05 as a structural advance over V-03/V-04's distributed per-rule dual-mechanism approach. Under v10, V-03, V-04, and V-05 all reached the 300-pt ceiling — the rubric could not distinguish them.

**R11 investigation candidate resolved:** C-30 dual-mechanism independence — VALIDATED. V-01 (preamble position only for timestamp isolation, COMPRESSED-COLLAPSE GUARD absent → C-30 PARTIAL −10) and V-02 (COMPRESSED-COLLAPSE GUARD only, no preamble position → C-30 PARTIAL −10) each fail C-30 while passing C-29. Both mechanisms are independently necessary. V-03, V-04, and V-05 each achieve C-30 PASS (300 pts under v10).

**R11 excellence signal:** V-05 introduced a preamble section explicitly designated COMPRESSION-IMMUNE — collecting the zero-signal synthesis rule (C-29 domain) and the timestamp isolation rule (C-30 domain) under a single named structural contract, with execution notes referencing the section by its designation. V-03 achieves C-30 PASS by placing the preamble rule and adding a COMPRESSED-COLLAPSE GUARD in the execution note, without designating the preamble as structurally immune. V-04 achieves the same with a three-location registry in the execution note, naming the preamble as a location but not designating it as COMPRESSION-IMMUNE. V-05 unifies the positional mechanism for both rules under one contract, removing the per-rule positional bet. Because v10 cannot distinguish V-03/V-04/V-05, C-31 is introduced so R12 can falsify whether the explicit COMPRESSION-IMMUNE PREAMBLE designation produces measurably stronger protection than distributed per-rule dual-mechanism placement.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-31 | COMPRESSION-IMMUNE PREAMBLE consolidation — when C-29 and C-30 both PASS, the shared positional mechanism is explicitly designated as a compression-immune structural unit rather than maintained as independent per-rule preamble placements | Consolidation of C-29 and C-30 positional mechanisms under a named structural contract |

**Structural chains updated:**

- Timestamp isolation chain: C-16 → C-24 → C-30 (timestamps mandated → dual-location restatement under COMPRESSED → dual-mechanism independence: positional + declarative, failure modes orthogonal) — unchanged from v10
- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29 — unchanged from v10
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 — unchanged from v10
- Compression survival generalization chain: C-24 → C-29 → C-30 — unchanged from v10
- **Compression-immune consolidation chain (new):** C-29 → C-30 → C-31 (zero-signal dual-mechanism → timestamp isolation dual-mechanism → multi-rule COMPRESSION-IMMUNE PREAMBLE consolidation)

**Relationship between C-29/C-30 and C-31:** C-31 does not replace C-29 and C-30. C-29 and C-30 each require dual-mechanism independence for their respective rules individually. C-31 requires that when both rules coexist, the shared positional mechanism is unified under an explicit COMPRESSION-IMMUNE designation. A skill can satisfy C-29 PASS and C-30 PASS at PARTIAL on C-31 (per-rule dual-mechanism present, no unified designation). C-31 PASS requires an explicit structural designation beyond per-rule positional placement.

**R12 investigation candidate:** Whether C-31's COMPRESSION-IMMUNE PREAMBLE designation produces measurably different outcomes from distributed per-rule dual-mechanism protection (C-29 PASS + C-30 PASS without preamble consolidation, V-04 style) when three or more compression-critical rules must coexist or when token pressure is sufficient to suppress even preamble-placed rules before their declarative guards are processed. R12 should construct a variation that achieves C-29 and C-30 PASS via distributed mechanisms (V-04 style) while leaving C-31 at PARTIAL, then a variation with C-31 PASS (V-05 style, explicit designation). If the C-31-PASS variation scores 310 while the C-31-PARTIAL variation scores 300, C-31 is independently necessary. If both score the same, the criterion should be re-examined for whether the explicit designation adds structural protection beyond what per-rule dual-mechanism achieves.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(31 total criteria; C-01–C-20 definitions unchanged from v6.)*

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

#### C-25 — TOKEN-PRESSURE GUARD on zero-signal synthesis rule *(R7 Pattern)*

The zero-signal synthesis mandate (C-22) must be promoted to a named guard with an explicit unconditional-firing declaration. The model failure mode is treating the zero-signal clause as conditionally active only when `found` is empty — if `found` becomes non-empty at any point during generation, the model may suppress the clause. The TOKEN-PRESSURE GUARD must declare the rule active regardless of `found` content or token budget.

**PARTIAL** — zero-signal synthesis rule present (C-22 PASS) but no unconditional-firing declaration; model may treat the rule as conditionally dormant when `found` is non-empty.

**PASS** — TOKEN-PRESSURE GUARD promotes the zero-signal synthesis rule with an explicit unconditional-firing declaration: the rule does not suspend when `found` is non-empty and fires at any token budget. The declaration is a named structural instruction, not implied by rule examples.

---

#### C-26 — VERDICT COMPRESSION GUARD on mandatory last-block sub-labels *(R8 Pattern)*

The bounded/unbounded classification (C-23) requires an `action:` sub-label in the VERDICT block. The model failure mode under COMPRESSED format is to omit the sub-label on grounds that COMPRESSED permits abbreviation — and the sub-label is in the last block, where token pressure is highest. A VERDICT COMPRESSION GUARD must appear as a named instruction in the VERDICT execution note, declaring that the `action:` sub-label is required regardless of COMPRESSED format state and regardless of token pressure.

**PARTIAL** — bounded/unbounded classification present (C-23 PASS) but VERDICT COMPRESSION GUARD absent as a named instruction; model may omit `action:` sub-label under COMPRESSED or token-pressure conditions.

**PASS** — VERDICT COMPRESSION GUARD is a named instruction in the VERDICT execution note, explicitly declaring the `action:` sub-label required regardless of COMPRESSED format state and token pressure. The guard is not implied by format examples but stated as an independent rule.

---

#### C-27 — TOKEN-PRESSURE GUARD names conditional-dormancy failure mode *(R8 Pattern)*

The TOKEN-PRESSURE GUARD (C-25) must name the specific failure mode it guards against: conditional-context suppression — the model treats the zero-signal rule as dormant because `found` is large (non-empty context suppresses the conditional). Naming the failure mode makes the guard prescriptive rather than declarative: the model is told not just "this rule fires unconditionally" but "the failure this prevents is treating the rule as dormant when the condition appears inactive."

**PARTIAL** — TOKEN-PRESSURE GUARD present (C-25 PASS) with unconditional-firing declaration, but failure mode unnamed; guard is purely declarative without naming the suppression mechanism it counters.

**PASS** — TOKEN-PRESSURE GUARD explicitly names conditional-context suppression as the failure mode: a failure mode in which the model treats the rule as dormant because `found` is large. The failure-mode framing makes the guard mechanistically grounded rather than rule-assertion only.

---

#### C-28 — VERDICT COMPRESSION GUARD names last-block elision failure mode *(R9 Pattern)*

The VERDICT COMPRESSION GUARD (C-26) must name the specific failure mode it guards against: last-block elision — the model omits mandatory sub-labels from VERDICT because VERDICT is the final output block, where accumulated token pressure causes optional-appearing fields to be dropped at the output boundary. Without naming the failure mode, the guard is a compliance assertion; with it, the model understands why the sub-label is uniquely at risk in VERDICT and applies the guard as mechanistic protection rather than rule compliance alone.

**PARTIAL** — VERDICT COMPRESSION GUARD present (C-26 PASS) but last-block elision failure mode unnamed; guard is a compliance instruction without mechanistic grounding in the specific risk VERDICT faces.

**PASS** — VERDICT COMPRESSION GUARD explicitly names last-block elision: the `action:` sub-label is at risk because VERDICT is the final block and token budget accumulated through prior blocks may cause the model to treat mandatory fields as optional at the output boundary. The failure-mode framing pairs with C-26's compliance instruction and mirrors the C-27 pattern applied to the verdict chain.

---

#### C-29 — Dual-mechanism independence for zero-signal synthesis rule *(R9 Pattern — V-01/V-02 validated)*

The zero-signal synthesis rule (C-22) requires two independent mechanisms to survive under token pressure: (1) positional — preamble placement before STORY instructions, so the rule is processed before COMPRESSED abbreviation may elide it; (2) declarative — a named TOKEN-PRESSURE GUARD (C-25/C-27) that explicitly names the conditional-dormancy failure mode and declares unconditional firing. Neither mechanism alone is sufficient: preamble-only (V-01) fails because positional placement does not prevent conditional-dormancy suppression; declarative-only (V-02) fails because without preamble placement, the rule may be elided under COMPRESSED before the declarative guard is processed.

**PARTIAL** — one mechanism present (preamble placement OR declarative guard with failure-mode naming) but not both; the rule's survival under token pressure depends on a single protection mechanism, leaving one orthogonal failure mode unaddressed.

**PASS** — both mechanisms present and independent: preamble placement (positional) AND named declarative guard explicitly naming the conditional-dormancy failure mode (C-27 level). The two mechanisms guard against orthogonal failure modes: location elision under token pressure (countered by preamble placement) and conditional-dormancy suppression when `found` is non-empty (countered by declarative guard naming the failure mode). Each mechanism compensates when the other's protection is unavailable.

---

#### C-30 — Dual-mechanism independence generalized to timestamp isolation rule *(R10 Pattern — V-01/V-02 validated)*

C-29's dual-mechanism independence principle applied to the timestamp isolation rule (C-24 domain). The timestamp isolation rule must be protected by two independent mechanisms: (1) positional — preamble placement before STATUS instructions, so the rule is processed before COMPRESSED abbreviation may elide it; (2) declarative — a COMPRESSED-COLLAPSE GUARD in the STATUS or STORY execution note naming the failure mode: COMPRESSED-collapse, in which the model abbreviates `found` timestamps into the blocking-gap summary, destroying the per-signal date record.

**PARTIAL** — timestamp isolation rule protected by one mechanism only: preamble placement alone (positional present, COMPRESSED-COLLAPSE GUARD absent) OR COMPRESSED-COLLAPSE GUARD alone (declarative present, no preamble placement); survival under token pressure has a single point of failure.

**PASS** — both mechanisms present: preamble placement (positional) AND COMPRESSED-COLLAPSE GUARD in the execution note naming COMPRESSED-collapse as the failure mode (declarative). The two mechanisms guard against orthogonal failure modes: location elision under token pressure (countered by preamble placement) and abbreviation of `found` timestamps into the blocking-gap summary under COMPRESSED (countered by declarative guard naming the collapse failure mode). This mirrors C-29's structure applied to C-24's domain.

**Relationship between C-24 and C-30:** C-24 requires dual-location restatement (entry format definition + execution note) to ensure the timestamp isolation rule survives COMPRESSED abbreviation regardless of which location is reached first. C-30 requires dual-mechanism independence (preamble position + declarative guard) to ensure the rule survives orthogonal failure modes: location elision under token pressure (countered by preamble placement) and positional processing without rule absorption (countered by declarative clause naming the COMPRESSED-collapse failure mode). C-24's dual-location provides structural redundancy within the same failure-mode class. C-30 requires that the two mechanisms guard against *different* failure modes so each compensates when the other's protection is unavailable.

**Relationship between C-29 and C-30:** C-29 and C-30 apply the same dual-mechanism independence principle to different rule domains (zero-signal synthesis vs. timestamp isolation). They share the same structural pattern and validate that dual-mechanism independence is a generalizable principle rather than domain-specific.

---

#### C-31 — COMPRESSION-IMMUNE PREAMBLE consolidation for multi-rule dual-mechanism protection *(R11 Pattern — V-05)*

When two or more rules each independently require dual-mechanism protection (C-29 PASS and C-30 PASS both present), the shared positional mechanism (preamble placement) must be consolidated under an explicitly named COMPRESSION-IMMUNE PREAMBLE designation, rather than maintained as independent per-rule positional placements. Without the explicit designation, each rule's preamble placement is a separate positional bet — the model may honor one rule's preamble position while treating another's as optional under token pressure, because no structural contract prevents selective elision. With the designation, the model treats the entire preamble section as a structural unit that is immune to COMPRESSED abbreviation, providing unified protection for all enclosed rules under a single contract.

**PARTIAL** — two or more compression-critical rules each have dual-mechanism protection (C-29 PASS, C-30 PASS) with preamble placement as the positional mechanism, but the preamble section is not explicitly designated as COMPRESSION-IMMUNE by name; each rule's positional protection is independent (per-rule preamble placement with or without cross-references in execution notes), and the model must honor each separately rather than treating the preamble as a unified compression-immune unit.

**PASS** — the preamble section is explicitly designated as COMPRESSION-IMMUNE by structural name (e.g., "COMPRESSION-IMMUNE PREAMBLE" as section header or equivalent designation), collecting all compression-critical rules (zero-signal synthesis rule and timestamp isolation rule) under a single named structural contract; execution notes reference the preamble by its designated name rather than by positional description alone, and the designation creates a single unified survival guarantee for all enclosed rules rather than per-rule positional protection.

Relationship to C-29 and C-30: C-31 does not replace C-29 and C-30. C-29 and C-30 each require dual-mechanism independence for their respective rules individually and remain independently evaluated. C-31 requires that when both rules coexist, their shared positional mechanism is unified under an explicit compression-immune designation. A skill can satisfy C-29 PASS and C-30 PASS at C-31 PARTIAL (per-rule dual-mechanism present, no unified designation — V-03/V-04 style). C-31 PASS requires an explicit structural designation beyond per-rule placement — the contract is in the section name itself, not in any individual rule's preamble instruction.
