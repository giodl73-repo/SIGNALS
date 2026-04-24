# simulate-argument — Round 8 Scorecard (v8 Rubric, Pool = 21)

## Scoring Framework

| Layer | Criteria | Scoring |
|-------|----------|---------|
| Essential | C-01–C-05 | Pass/Fail (prerequisite) |
| Recommended | C-06–C-08 | Noted, not in formula |
| Aspirational pool | C-09–C-29 (21 criteria) | `pass / 21 × 10` |

Golden threshold: **9.6** (96%). All variations share canonical implementation for C-01–C-26; differences appear only on C-27, C-28, C-29.

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01–C-05) — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Claim map present, ≥6 rows with ID/type | PASS | PASS | PASS | PASS | PASS |
| C-02 | Dependency graph complete, no dangling refs | PASS | PASS | PASS | PASS | PASS |
| C-03 | Section coverage — each section represented | PASS | PASS | PASS | PASS | PASS |
| C-04 | Every inference step has STEP block with form + checks + verdict | PASS | PASS | PASS | PASS | PASS |
| C-05 | Fault register matches BROKEN/WEAK verdicts exactly | PASS | PASS | PASS | PASS | PASS |

All-essential-pass: **TRUE** across all five variations.

---

### Aspirational Pool (C-09–C-29)

#### C-09 — Term drift pinpointed to C-ID

All variations: **PASS** — canonical design; DEF-DRIFT rows cite definition claim C-ID.

#### C-10 — P1/P2 fault is non-obvious and reviewer-worthy

All variations: **PASS** — canonical design; fault selection targets structural gaps, not surface issues.

#### C-11 — Falsification target in Phase 0

All variations: **PASS** — Phase 0 best-case paragraph frames a falsifiable claim.

#### C-12 — Inline reviewer hook inside every WEAK/BROKEN verdict

All variations: **PASS** — "As committee chair, would I flag this..." present in every 3C verdict that is WEAK or BROKEN.

#### C-13 — Fault-pattern closure names structural fault class, not depth tier

All variations: **PASS** — fault class column uses DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM.

#### C-14 — Enumerated Class column in fault register

All variations: **PASS** — Class column is present and populated with exactly-one-per-row label.

#### C-15 — Reviewer depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) with domain comparison

All variations: **PASS** — every WEAK/BROKEN 3C verdict carries depth tier and domain comparison sentence.

#### C-16 — Null-hypothesis binary verdict

All variations: **PASS** — H0 stated in Phase 0; Phase 4 close carries mechanical reject/fail-to-reject.

#### C-17 — Dedicated form-identification sub-pass (3A) before validity checks

All variations: **PASS** — Phase 3A runs as isolated Logician pass; no evaluation intermixed.

#### C-18 — Critical-path pre-commitment; Phase 4 audits CP fault landing

All variations: **PASS** — Phase 0 names load-bearing C-IDs; Phase 4 CP? flags populated; audit present.

#### C-19 — Named specialist handoff with closure language enforcing temporal separation

All variations: **PASS** — each specialist closes with first-person identity commitment before the next begins.

#### C-20 — Advocate gap accounts: "needed X, found only Y" relative to Phase 0 generalizations

All variations: **PASS** — UNSUPPORTED-GEN Gap fields cite Gen-ID and state the evidential shortfall.

#### C-21 — Advocate Phase 3 gen-anchoring — best readings cite Phase 0 Gen-IDs

All variations: **PASS** — Advocate ADVOCATE blocks carry Gen-ID anchor field tied to Phase 0 registry.

#### C-22 — Logician global binding — closure names all downstream specialists and prohibits reclassification

All variations: **PASS** — Logician closure sentence names Advocate, Empirical Reviewer, and Committee Chair.

*Exception V-04*: Logician closure is **specialist-only** (no phase-extension language) → this affects C-25 and C-28 (scored below), not C-22 directly. C-22 still passes in V-04 because the global specialist prohibition is present.

#### C-23 — CP audit three-way verdict (CONFIRMED / DISCONFIRMED / CONFIRMED-ELSEWHERE)

All variations: **PASS** — CONFIRMED-ELSEWHERE category is instantiated in the CP audit template.

#### C-24 — Advocate form-independent gen-anchoring — trigger fires on content, not form label

All variations: **PASS** — Advocate instruction explicitly states the scan applies to every inference step regardless of Logician form label; two-field check (Generalization assumed + Gen-ID anchor) is present.

#### C-25 — Logician cross-phase immutability — reclassification prohibition extends to phases

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Logician closure contains both "no subsequent specialist" and "no subsequent *phase* may reclassify logical structure" |
| V-02 | **PASS** | Same as V-01; V-02's axis is Phase-4 row specificity, not Logician closure language |
| V-03 | **PASS** | Full Logician closure with phase-extension language present |
| V-04 | **FAIL** | Logician closure is specialist-only — no phase-extension clause; C-25 requires the phase-prohibition language and V-04's axis intentionally removes it (this FAIL propagates to C-28 as well) |
| V-05 | **PASS** | Canonical Logician closure with full phase-language |

#### C-26 — CP audit forced adjacency search — DISCONFIRMED requires documented Step 2

All variations: **PASS** — DISCONFIRMED verdicts in all five variations include documented adjacency search before the verdict is written.

---

### New Criteria — C-27, C-28, C-29

#### C-27 — Advocate named form-type trigger enumeration

**Rule**: Advocate block must explicitly name causal inference AND argument-from-analogy as trigger form types; closure must attest that steps bearing both enumerated labels received the same gen scan as steps labeled "inductive generalization." Generic assertion without both names in the attestation sentence fails.

| Variation | Result | Evidence |
|-----------|--------|----------|
| **V-01** | **FAIL** | Advocate closure places both form types in the "not only" contextual list but the explicit attestation sentence — "same scan as inductive generalization" — is replaced with generic form-independent language. Neither "causal inference" nor "argument-from-analogy" appears in the attestation sentence. Generic form-independent attestation is the boundary C-27 was designed to catch. |
| V-02 | **PASS** | Both form types named in Advocate instruction and explicitly repeated in the "same scan as inductive generalization" attestation sentence in the closure. |
| V-03 | **PASS** | Same as V-02; V-03's axis is CP adjacency, not Advocate closure. |
| V-04 | **PASS** | Advocate instruction names both types; closure attests both received same gen scan. C-27 passes independently of Logician closure. |
| **V-05** | **PASS** | Closure explicitly attests BOTH "causal inference" AND "argument-from-analogy" steps received the same generalization scan as steps labeled "inductive generalization" — matching the maximum-strength formulation. |

#### C-28 — Logician cross-phase derivation double-lock

**Rule**: BOTH elements required simultaneously — (1) Logician closure with phase-extension language AND (2) Phase-4 INVALID-FORM rows carry `Derives from: FORM [specific-C-ID]`. Neither element alone suffices.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Full Logician phase-language present (element 1). Phase-4 INVALID-FORM rows carry `Derives from: FORM [C-ID]` block references (element 2). Both elements present. |
| **V-02** | **FAIL** | Element 1 present (full Logician phase-language). Element 2 absent: Phase-4 INVALID-FORM derivation template reads "Derives from: Phase 3A committed form analysis" — generic phase reference without specific FORM [C-ID] block citation. One element without the other fails C-28 by definition. |
| V-03 | **PASS** | Both elements present; V-03's axis is CP adjacency only. |
| **V-04** | **FAIL** | V-04's Logician closure is specialist-only — no phase-extension language. Element 1 absent. Element 2 also absent (no Phase-4 derivation requirement). C-28 fails by double absence; also propagated from C-25 FAIL. |
| **V-05** | **PASS** | Canonical double-lock: Logician closure carries phase-extension language (element 1); Phase-4 INVALID-FORM rows carry `Derives from: FORM [C-ID]` (element 2). Both elements confirmed present simultaneously. |

#### C-29 — Unconditional CP adjacency with Gen-ID provenance

**Rule**: Step 2 runs unconditionally (even for CONFIRMED steps). CONFIRMED-ELSEWHERE verdicts must carry Gen-ID anchor from Phase 3 inline in the verdict string using format: `CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM`.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Step 2 unconditional; CONFIRMED-ELSEWHERE uses Gen-ID parenthetical format matching rubric example. |
| V-02 | **PASS** | Step 2 unconditional; CONFIRMED-ELSEWHERE carries Gen-ID. V-02's axis is Phase-4 derivation specificity only. |
| **V-03** | **FAIL** | Step 2 runs unconditionally (Step-2 conditionality check passes), but CONFIRMED-ELSEWHERE verdict writes only `CONFIRMED-ELSEWHERE — F-NN on adjacent C-MM` — no Gen-ID. The body text of Step 2 documents the Gen-ID, but the verdict string itself omits it. C-29 requires the Gen-ID to appear in the verdict string, not only in supporting documentation. |
| V-04 | **PASS** | Step 2 unconditional; CONFIRMED-ELSEWHERE uses full `CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM` format. |
| **V-05** | **PASS** | Step 2 runs unconditionally for every CP step. CONFIRMED-ELSEWHERE verdict uses rubric-matching format: `CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM` — Gen-ID is inline in the verdict string, not deferred to body text. |

---

## Aspirational Pool Summary (C-09–C-29)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | **FAIL** | PASS |
| C-26 | PASS | PASS | PASS | PASS | PASS |
| C-27 | **FAIL** | PASS | PASS | PASS | PASS |
| C-28 | PASS | **FAIL** | PASS | **FAIL** | PASS |
| C-29 | PASS | PASS | **FAIL** | PASS | PASS |
| **Pass count** | **20/21** | **20/21** | **20/21** | **19/21** | **21/21** |

> **Note on V-04**: V-04's C-25 FAIL (specialist-only Logician closure lacks phase-extension language) cascades: C-28 requires element 1 (phase-language) AND element 2 (FORM [C-ID] rows) simultaneously. With element 1 absent from the Logician closure, C-28 fails independently. V-04 thus accumulates C-25 FAIL + C-28 FAIL = 19/21, not 20/21 as predicted. This is a prediction error in the variation design document — V-04's axis description ("specialist-only") removes C-25 compliance, which was not flagged in the predicted C-25 column.

---

## Composite Scores

| Variation | Aspirational Pass | Formula | Score | Golden (≥9.6)? |
|-----------|-------------------|---------|-------|----------------|
| V-01 | 20/21 | 20/21 × 10 | **9.52** | No (95.2%) |
| V-02 | 20/21 | 20/21 × 10 | **9.52** | No (95.2%) |
| V-03 | 20/21 | 20/21 × 10 | **9.52** | No (95.2%) |
| V-04 | 19/21 | 19/21 × 10 | **9.05** | No (90.5%) |
| **V-05** | **21/21** | 21/21 × 10 | **10.0** | **YES (100%)** |

**Ranking**: V-05 > V-01 = V-02 = V-03 > V-04

---

## Excellence Signals

**V-05** is the sole golden variation (10.0/10.0, 21/21 aspirational). Three patterns distinguish it:

### Signal 1: `closure-attestation-enumerates-both-form-types-explicitly`
The Advocate closure does not merely list causal inference and argument-from-analogy in contextual surrounding text — it places both labels directly inside the "same scan as inductive generalization" attestation sentence. The sentence reads as an explicit equivalence claim: steps labeled X AND steps labeled Y received the same treatment as steps labeled Z. V-01 proved that placing both types in a nearby list without repeating them in the attestation sentence fails C-27.

### Signal 2: `phase4-invalid-form-row-names-specific-block-id-not-phase`
The Phase-4 INVALID-FORM derivation field cites the specific committed FORM block: `Derives from: FORM [C-07] — causal inference` rather than `Derives from: Phase 3A committed form analysis`. V-02 proved that generic phase attribution without a block-level ID fails C-28 even when the Logician closure is fully correct. The double-lock requires the row to be traceable to a specific immutable record, not just to a phase.

### Signal 3: `confirmed-elsewhere-gen-id-in-verdict-string-not-body`
The CONFIRMED-ELSEWHERE verdict carries the Gen-ID parenthetical inline in the verdict string itself — `CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM` — rather than documenting the Gen-ID only in the Step 2 body text. V-03 proved that body-text documentation of Gen-IDs does not satisfy C-29 when the verdict string is ambiguous. The anchor must be machine-readable at the verdict line.

---

## Prediction Discrepancy

The variation design document predicted V-04 at 20/21. The actual score is 19/21. Root cause: V-04's specialist-only Logician closure (the C-28 axis) also removes the phase-extension clause required for C-25. The design document did not flag C-25 as affected by V-04's axis, but C-25 explicitly requires the phase-prohibition language that V-04 removes. This is a real double-failure, not a scoring artifact — C-25 and C-28 are separable criteria and V-04 fails both independently.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": []}
```
