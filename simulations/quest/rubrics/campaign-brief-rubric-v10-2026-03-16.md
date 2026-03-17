## Quest Rubric — v10

`29 criteria, 290 pts max` → `30 criteria, 300 pts max`

---

### What changed: v9 → v10

One new aspirational criterion extracted from R10 excellence signals. C-29's dual-mechanism independence was validated as a required structural property — neither preamble-only (V-01) nor declarative-only (V-02) achieves C-29 PASS. Both mechanisms are independently necessary. The criterion is not narrowed.

V-04 and V-05 both reached the 290-pt ceiling under v9. V-05 extends V-04 by generalizing dual-mechanism independence to the timestamp isolation rule (C-24 domain) in addition to the zero-signal synthesis rule (C-29 domain). Because v9 could not distinguish V-04 from V-05, C-30 is introduced so R11 can falsify whether timestamp-isolation dual-mechanism (C-30) produces measurably different outcomes from zero-signal dual-mechanism alone (C-29) under token pressure extreme enough to suppress mid-document `found` entries before their declarative guard is processed.

| New criterion | Source pattern | Relationship to existing |
|---|---|---|
| C-30 | Dual-mechanism independence generalized to timestamp isolation rule — positional (preamble) + declarative (COMPRESSED-collapse guard naming the failure mode) applied to C-24's domain | Generalization of C-29 to the C-24 chain |

**Structural chains updated:**

- Timestamp isolation chain: C-16 → C-24 → C-30 (timestamps mandated → dual-location restatement under COMPRESSED → dual-mechanism independence: positional + declarative, failure modes orthogonal)
- Zero-signal synthesis chain: C-18 → C-21 → C-22 → C-25 → C-27 → C-29 (unchanged from v9)
- Verdict action-posture chain: C-06 → C-23 → C-26 → C-28 (unchanged from v9)
- Compression survival generalization chain: C-24 → C-29 → C-30 (dual-location for timestamp isolation → dual-mechanism principle generalized to zero-signal rule → dual-mechanism principle generalized back to timestamp isolation with independent failure-mode framing)

**Relationship between C-24 and C-30:** C-24 requires dual-location restatement (entry format definition + execution note) to ensure the timestamp isolation rule survives COMPRESSED abbreviation regardless of which location is reached first. C-30 requires dual-mechanism independence (preamble position + declarative guard) to ensure the rule survives orthogonal failure modes: location elision under token pressure (countered by preamble placement) and positional processing without rule absorption (countered by declarative clause naming the COMPRESSED-collapse failure mode). C-24's dual-location provides structural redundancy within the same failure-mode class. C-30 requires that the two mechanisms guard against *different* failure modes so each compensates when the other's protection is unavailable.

**R9 investigation candidate resolved (carried forward):** C-29 dual-mechanism independence — VALIDATED. V-01 (preamble-only, C-29 PARTIAL −10) and V-02 (declarative-only, C-29 PARTIAL −10) each fail C-29. Neither mechanism alone is sufficient. The criterion is not narrowed.

**R10 investigation candidate:** Whether C-30's timestamp-isolation dual-mechanism produces measurably different outcomes from C-29 alone when token pressure is high enough to suppress mid-document `found` entries. R11 should construct a variation that achieves C-29 PASS (zero-signal dual-mechanism present) while leaving C-30 at PARTIAL (timestamp isolation via C-24 dual-location only, no preamble placement + declarative guard). If that variation scores below 300 under v10, C-30 is independently necessary. If it scores 300, the criterion should be re-examined for whether the failure modes it guards against are already covered by C-24's structural redundancy.

---

### Criteria Reference

#### C-01 through C-20 — carry forward from v6 unchanged

*(30 total criteria; C-01–C-20 definitions unchanged from v6.)*

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

#### C-25 — TOKEN-PRESSURE GUARD on zero-signal synthesis rule *(R9 Pattern — V-01/V-04/V-05)*

The zero-signal synthesis mandate (C-22) is a conditional rule: it activates only when `found` is empty. Conditional rules are vulnerable to token pressure because the model may process the condition but not enforce the clause when operating near context limits — the rule is nominally present but fires conditionally rather than unconditionally. A TOKEN-PRESSURE GUARD hardens C-22 by promoting the zero-signal synthesis mandate from a conditional clause to a named rule with an unconditional-firing declaration.

**PARTIAL** — C-22 PASS (explicit zero-signal clause present) but no TOKEN-PRESSURE GUARD promoting it to named-rule status; the clause remains conditional and is vulnerable to dormancy under high token pressure.

**PASS** — a named rule (e.g., `ZERO-SIGNAL SYNTHESIS RULE`) with an unconditional-firing declaration appears in the skill — "this rule fires regardless of token budget; empty `found` is not grounds for omitting synthesis" — promoting the mandate from conditional clause to named invariant that the model must enforce unconditionally.

Relationship to C-22: C-22 requires the clause to exist. C-25 requires the clause to be hardened as a named rule that fires unconditionally. C-25 is a structural escalation of C-22, not a restatement.

---

#### C-26 — VERDICT COMPRESSION GUARD on mandatory last-block sub-labels *(R9 Pattern — V-02/V-04/V-05)*

The VERDICT block appears at the end of STATUS output. Under token pressure, the model abbreviates end-of-document content — and the `action:` sub-label (C-06, C-23) may be dropped or collapsed into freeform verdict prose, destroying the posture signal. The VERDICT COMPRESSION GUARD names this failure mode and declares `action:` as a mandatory structural sub-label that must survive last-block compression.

**PARTIAL** — `action:` sub-label present in the nominal path (C-06 PASS) but no VERDICT COMPRESSION GUARD elevating it to a named invariant; the label may be lost when the VERDICT block is abbreviated under token pressure.

**PASS** — a VERDICT COMPRESSION GUARD explicitly declares that `action:` is a mandatory sub-label — not a format extension — and must survive COMPRESSED × last-block conditions; the guard is present in the skill as a named instruction, not implied by format examples.

Relationship to C-06: C-06 tests that `action:` exists in the nominal path. C-26 tests that the instruction architecture declares it a mandatory invariant under compression. They are independent checks on the same sub-label.

---

#### C-27 — TOKEN-PRESSURE GUARD names conditional-dormancy failure mode *(R9 Pattern — V-02/V-03/V-04/V-05)*

C-25 requires a TOKEN-PRESSURE GUARD with an unconditional-firing declaration. C-27 hardens C-25 by requiring the guard to explicitly name the failure mode it prevents: conditional dormancy — the model encounters the rule, evaluates the condition as inactive (empty `found` not yet observed), and suppresses the clause rather than holding it active for later evaluation. Naming the failure mode makes the guard self-documenting: a model that understands *why* the rule fires unconditionally is less likely to suppress it than a model that sees only the declaration without the failure mode.

**PARTIAL** — TOKEN-PRESSURE GUARD present (C-25 PASS) but unconditional-firing declaration does not name conditional-dormancy as the failure mode prevented; the guard fires but does not explain what it is guarding against; failure mode left implicit.

**PASS** — TOKEN-PRESSURE GUARD contains an explicit failure-mode declaration: "this rule fires unconditionally because conditional rules suppress under token pressure — the failure mode prevented is conditional dormancy, where the model processes the condition but does not enforce the clause when operating near context limits"; the failure mode is named, not implied.

Relationship to C-25: C-25 requires the guard to exist and declare unconditional firing. C-27 requires the guard to name the failure mode prevented. C-27 is a content requirement on C-25's structure.

---

#### C-28 — VERDICT COMPRESSION GUARD declares `action:` as mandatory invariant *(R9 Pattern — V-01/V-04/V-05)*

C-26 requires a VERDICT COMPRESSION GUARD. C-28 hardens C-26 by requiring the guard to explicitly declare `action:` as a mandatory invariant — not merely a preferred format or suggested sub-label — so the model treats its omission as a structural violation rather than an acceptable abbreviation. The distinction matters under last-block token pressure: a model that sees `action:` as a format preference may omit it; a model that sees it as a mandatory invariant will preserve it.

**PARTIAL** — VERDICT COMPRESSION GUARD present (C-26 PASS) but does not explicitly declare `action:` as a mandatory invariant; the guard protects the label under compression but leaves its status ambiguous between format convention and structural requirement.

**PASS** — VERDICT COMPRESSION GUARD contains an explicit invariant declaration: "`action:` is a mandatory sub-label, not a format extension; its omission is a structural violation regardless of token budget or COMPRESSED status"; the label's mandatory status is declared, not inferred from format examples.

Relationship to C-26: C-26 requires the guard to exist. C-28 requires the guard to declare `action:` as a mandatory invariant. C-28 is a content requirement on C-26's structure.

---

#### C-29 — Dual-mechanism independence for zero-signal synthesis rule *(R9 Pattern — V-04/V-05)*

Compression-critical execution rules — rules that must survive both token-pressure suppression and positional non-absorption — require two independent mechanisms, each compensating for the other's failure mode. A single mechanism (preamble position only, or declarative guard only) leaves a single point of failure. C-29 applies this principle to the zero-signal synthesis rule.

**Positional mechanism:** the zero-signal synthesis rule (or its TOKEN-PRESSURE GUARD) appears in the preamble of the skill, before the main body. Preamble placement ensures the rule is encountered before token pressure builds — even if late-document content is suppressed, the rule has already been processed.

**Declarative mechanism:** a named TOKEN-PRESSURE GUARD clause explicitly names conditional-dormancy as the failure mode prevented (C-27 PASS). The declarative mechanism ensures the rule survives cases where the preamble is processed without full rule absorption — the model encounters the clause mid-document and the failure-mode framing makes suppression more costly than compliance.

The failure modes are orthogonal: positional placement fails when the preamble is processed but the rule is not absorbed (model reads without retaining). Declarative guard fails when the guard clause itself is elided under extreme token pressure before processing. Because the failure modes are orthogonal, each mechanism compensates for the other's independent failure.

**PARTIAL** — one mechanism present (positional only OR declarative only); single-mechanism guard leaves the zero-signal synthesis rule with a single point of failure under compression.

**PASS** — both mechanisms present on the zero-signal synthesis rule: preamble placement (positional) AND a declarative TOKEN-PRESSURE GUARD naming conditional-dormancy (declarative); each mechanism independently guards against a distinct failure mode; the rule survives cases where either mechanism alone would fail.

Structural chain: C-24 (dual-location for timestamps) → C-29 (dual-mechanism principle generalized to zero-signal synthesis rule).

**R10 validation:** C-29 independence requirement confirmed. V-01 (preamble-only) and V-02 (declarative-only) each score C-29 PARTIAL. Neither mechanism alone is sufficient. The criterion is not narrowed.

---

#### C-30 — Dual-mechanism independence for timestamp isolation rule *(R10 Pattern — V-05)*

C-29 establishes dual-mechanism independence as a required structural property for compression-critical execution rules, validated on the zero-signal synthesis domain. C-30 extends this principle to the timestamp isolation rule (C-24 domain). The timestamp isolation rule is independently compression-critical: under extreme token pressure, mid-document `found` entries may be suppressed before their isolation guard is processed, and the COMPRESSED branch may abbreviate both locations required by C-24, collapsing timestamps into the blocking summary before either location is enforced.

C-24's dual-location restatement (entry format definition + execution note) provides structural redundancy within the same failure-mode class — both locations can be elided by the same token-pressure event that suppresses mid-document content. C-30 requires that the two mechanisms guarding timestamp isolation guard against *different* failure modes, so suppressing one mechanism's protection leaves the other active.

**Positional mechanism:** the timestamp isolation rule (or its COMPRESSED-collapse guard) appears in the preamble of the skill. Preamble placement ensures the rule is encountered before token pressure builds and before any COMPRESSED branch abbreviation begins — independent of whether mid-document locations are reached.

**Declarative mechanism:** an explicit guard clause names the COMPRESSED-collapse failure mode for timestamps: "if the COMPRESSED branch abbreviates `found`, timestamps must survive as structurally isolated fields; collapsing `found` into the blocking summary destroys the signal-level date record and is a structural violation." The declarative clause ensures the rule survives cases where the preamble is processed without rule absorption — the failure-mode framing makes suppression more costly than compliance when the clause is encountered.

The failure modes are orthogonal: positional placement fails when the preamble is processed but the timestamp isolation rule is not absorbed (model reads without retaining). Declarative guard fails when the guard clause itself is elided under extreme compression before processing. Each mechanism compensates for the other's independent failure.

**PARTIAL** — C-29 PASS (zero-signal synthesis dual-mechanism achieved) but timestamp isolation guarded by C-24 dual-location only; both C-24 locations are mid-document and subject to the same token-pressure suppression event; preamble placement + declarative failure-mode clause absent for the timestamp isolation rule; dual-mechanism independence not achieved for this compression-critical rule.

**PASS** — timestamp isolation rule present at preamble location AND a declarative guard clause names the COMPRESSED-collapse failure mode for timestamps; independence achieved because: (1) preamble position ensures the rule is encountered before token pressure builds, independent of mid-document reach; (2) declarative clause ensures the rule survives cases where preamble content is processed without absorption; the failure modes they guard against are orthogonal, so each mechanism compensates when the other's protection is unavailable.

Relationship to C-24: C-24 requires dual-location restatement (entry format + execution note) to ensure structural redundancy. C-30 requires dual-mechanism independence (positional + declarative) to ensure failure-mode orthogonality. C-24 guards against location elision within the same failure-mode class. C-30 guards against both location elision (preamble) and absorption failure (declarative). They are independent checks on the same field's compression survival — C-24 PASS is a necessary but not sufficient condition for C-30 PASS.

Structural chain: C-16 → C-24 → C-30 (timestamps mandated → dual-location under COMPRESSED → dual-mechanism independence with orthogonal failure modes).

Structural chain (compression generalization): C-24 → C-29 → C-30 (dual-location for timestamps → dual-mechanism for zero-signal synthesis → dual-mechanism for timestamp isolation; the principle propagates from its source domain back to close the chain).

**R11 investigation candidate:** Whether C-30's preamble-position mechanism is independently sufficient for timestamp isolation under token pressure when the declarative COMPRESSED-collapse guard is absent, or whether the declarative guard alone (mid-document, no preamble) is independently sufficient. R11 should construct: (a) a variation with C-29 PASS + C-24 PASS + preamble placement of timestamp rule but no declarative COMPRESSED-collapse guard (positional-only), and (b) a variation with C-29 PASS + C-24 PASS + declarative guard but no preamble placement (declarative-only). If either alone achieves C-30 PASS, the independence requirement should be narrowed. If neither alone achieves it, C-30's orthogonality requirement is validated.

---

### Composite Rankings (R10 — carried forward as baseline)

| Rank | Variation | Score (v9) | Score (v10) | Key differentiator |
|---|---|---|---|---|
| 1 | V-05 | 290/290 | 300/300 | Dual-mechanism on both zero-signal synthesis (C-29) and timestamp isolation (C-30) |
| 2 | V-04 | 290/290 | 290/300 | Dual-mechanism on zero-signal synthesis only; C-30 PARTIAL |
| 3 (tie) | V-02 | 280/290 | 280/300 | Declarative guard present (C-27 PASS); C-29 and C-30 both PARTIAL |
| 3 (tie) | V-03 | 280/290 | 280/300 | C-29 applied to wrong domain; C-29 and C-30 both PARTIAL |
| 5 | V-01 | 270/290 | 270/300 | Preamble-only; C-27, C-29, C-30 all PARTIAL |
