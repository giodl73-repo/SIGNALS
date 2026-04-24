# topic:echo — Round 5 Scorecard

**Rubric:** v5 | **Max composite:** 140 | **Date:** 2026-03-16

---

## Per-Variation Criterion Evaluation

### V-01 — Dedicated Enforcement Mechanism Section

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 Named surprises | PASS | Minimum 2 SURPRISE verdicts required; named handles with departure framing |
| C-02 Signal tracing | PASS | Source signal field + orphan-attribution test enforced |
| C-03 Design impact | PASS | Field required, must name specific component/flow/decision |
| C-04 Synthesis not summary | PASS | Anti-Pattern Catalog + Gatekeeper filter removes non-surprises |
| C-05 Surprise specificity | PASS | Orphan-attribution test enforces investigation specificity |
| C-06 Expectation counterfactual | PASS | "We believed" field required in every entry |
| C-07 Institutional framing | PASS | "Institutional memory for the next team" preamble + forward guidance step |
| C-08 Cross-signal pattern | PASS | Synthesis step requires explicit pattern statement or explicit absence declaration |
| C-09 Surprise hierarchy | **FAIL** | No impact triage or ranking step present |
| C-10 Riskiest surprise | **FAIL** | No riskiest surprise step |
| C-11 Pre-committed PBI | PASS | COMMIT-PBI marker, addressable PBI-NN identifiers, entries cite PBI-Ref |
| C-12 Named handles | PASS | Handle Ledger with 2-5 word title-case labels, COMMIT-HANDLE-LEDGER |
| C-13 Dual phase-locked | PASS | Independence check: PBI belief language vs Handle finding language enforced |
| C-14 Audit trail completeness | PASS | Three-pointer Verified field (Handle, PBI-Ref, Source) |
| C-15 Enforcement mechanism | PASS | Dedicated Provenance Enforcement Mechanism section present |
| C-16 Production-time attestation | PASS | Named checks in Verified field (Handle confirmed, PBI-Ref confirmed, Source confirmed) |
| C-17 Strength classification | PASS | Dedicated table: Tier = "Structural > temporal", distinguishing property (role-scope exclusion vs phase sequencing), reviewer implication ("Independence is enforced, not instructed") — all three elements at highest level |
| C-18 Evidentiary quotation | PASS | Verified requires quoted Handle label, full belief statement with predicate, specific source sentence naming a component |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 8/10 = 40
**Composite: 130 / 140**

---

### V-02 — Quotation Quality Template

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | SURPRISE verdicts + named handles required |
| C-02 | PASS | Source signal tracing enforced |
| C-03 | PASS | Design impact field required |
| C-04 | PASS | Pre-Write Prediction Sort routes non-surprises to topic-story/topic-report |
| C-05 | PASS | Route-assignment forces investigation-specificity |
| C-06 | PASS | "We believed" field required |
| C-07 | PASS | "Institutional memory for the next team" + forward guidance |
| C-08 | PASS | Synthesis step with explicit absence clause |
| C-09 | **FAIL** | No ranking step |
| C-10 | **FAIL** | No riskiest flag |
| C-11 | PASS | COMMIT-PBI, PBI-NN identifiers, entries cite PBI-Ref |
| C-12 | PASS | Handle Ledger, 2-5 words |
| C-13 | PASS | Independence check enforced |
| C-14 | PASS | Three-pointer Verified field |
| C-15 | PASS | Inline PBI preamble: "structural provenance isolation: the PBI was written in a role that accesses only original design materials, not signal artifacts" |
| C-16 | PASS | Named checks with quoted texts in Verified field |
| C-17 | **PASS (minimum bar)** | Inline: "Structural provenance (role-scope exclusion) is stronger than temporal provenance (phase sequencing) because role-scope exclusion prevents cross-phase reasoning" — tier ✓, distinguishing property ✓, reviewer implication **absent** (no "independence is enforced, not instructed" statement). Passes minimum bar per rubric (a)+(b); not highest level. Note: design predicted FAIL, but rubric pass bar is (a)+(b) only — inline declaration qualifies. |
| C-18 | PASS | Self-certifying quality template: predicate test, uniqueness test, length test (8+ words), specificity test, locatability test — all named, author must confirm before committing |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 8/10 = 40
**Composite: 130 / 140**

> **Scoring deviation from prediction:** Design predicted 125 (C-17 FAIL). Actual: 130 (C-17 PASS at minimum bar). The inline declaration in V-02's PBI preamble contains both required C-17 elements — tier label and distinguishing property. Reviewer implication absent, so this is minimum-bar pass, not highest level. Finding: C-17 navigability (dedicated section vs inline) is not a blocking pass/fail distinction under v5. Dedicated section provides highest-level pass; inline provides minimum-bar pass. This is itself an excellence signal (see below).

---

### V-03 — Post-Production Chain Integrity Audit

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | Named surprises required |
| C-02 | PASS | Source signal tracing enforced |
| C-03 | PASS | Design impact field required |
| C-04 | PASS | Anti-Pattern Catalog + Gatekeeper |
| C-05 | PASS | Specificity enforced |
| C-06 | PASS | "We believed" field |
| C-07 | PASS | Institutional framing + forward guidance |
| C-08 | PASS | Synthesis step |
| C-09 | **PASS** | Impact triage (Step 5) assigns HIGH/MEDIUM/LOW with explicit tier criteria; entries ordered HIGH→MEDIUM→LOW with tier header; per-entry Design impact field names specific consequence that maps to tier definition ("forces a design decision to change" = HIGH); Chain Audit Check B confirms tier consistency — hierarchy is defensible per-entry |
| C-10 | **PASS** | Riskiest surprise (Step 9): names assumption at risk + signal that revealed it + what would need to be true |
| C-11 | PASS | COMMIT-PBI with structural provenance confirmation |
| C-12 | PASS | Named handles, COMMIT-HANDLE-LEDGER |
| C-13 | PASS | Independence check + Chain Audit Check A (Handle language: finding, not belief) |
| C-14 | PASS | Three-pointer Verified field with quoted content |
| C-15 | PASS | Dedicated Provenance Enforcement Mechanism table in Step 2 |
| C-16 | PASS | Verified field names all three checks with 8+ word quotations |
| C-17 | PASS | Dedicated table: Tier = "Structural > temporal", property = "role-scope exclusion closes the cross-phase reasoning path", reviewer implication = "Independence is enforced, not instructed... confirmatory rather than probative" — highest level |
| C-18 | PASS | Verified quotes "Handle Ledger label text", "full belief statement from PBI-NN... 8+ words", "specific sentence from source artifact... naming a component or behavior, 8+ words" |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 10/10 = 50
**Composite: 140 / 140**

---

### V-04 — Combination: Dedicated C-17 Section + Quotation Quality Template

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | Named surprises required |
| C-02 | PASS | Source tracing enforced |
| C-03 | PASS | Design impact required |
| C-04 | PASS | Anti-Pattern Catalog + gate |
| C-05 | PASS | Specificity enforced |
| C-06 | PASS | "We believed" field |
| C-07 | PASS | Institutional framing + forward guidance |
| C-08 | PASS | Synthesis step |
| C-09 | **FAIL** | No ranking step |
| C-10 | **FAIL** | No riskiest flag |
| C-11 | PASS | COMMIT-PBI, identifiers |
| C-12 | PASS | Named handles |
| C-13 | PASS | Independence check |
| C-14 | PASS | Three-pointer Verified |
| C-15 | PASS | Dedicated Enforcement Mechanism Declaration section (Step 3) |
| C-16 | PASS | Named checks with quotations in Verified |
| C-17 | PASS | Dedicated section: Tier = "Structural > temporal", distinguishing property = "role-scope exclusion is the stronger mechanism because it closes the cross-phase reasoning path that phase gates leave open", reviewer implication = "Independence is enforced, not instructed... C-13... confirmatory rather than probative" — highest level |
| C-18 | PASS | Named quality tests (predicate, uniqueness, length; specificity, locatability, length) with self-certifying commitment requirement |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 8/10 = 40
**Composite: 130 / 140**

---

### V-05 — Full Combination: All Criteria + All R5 Structural Innovations

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | Named surprises, Institutional Archaeologist framing |
| C-02 | PASS | Source tracing enforced |
| C-03 | PASS | "What the next team would get wrong" field (stronger than generic design impact — names the concrete mis-design) |
| C-04 | PASS | Anti-Pattern Catalog + gate + Chain Audit eliminates non-surprises |
| C-05 | PASS | Specificity enforced throughout |
| C-06 | PASS | "We believed" field required |
| C-07 | PASS | Institutional Archaeologist role + explicit forward framing + forward guidance step |
| C-08 | PASS | Synthesis with Institutional Archaeologist perspective: "Look for a pattern in how the materials mislead future teams" — explicitly stronger than generic pattern analysis |
| C-09 | **PASS** | Impact triage + HIGH/MEDIUM/LOW tier headers + entries ordered by triage + Rules of Thumb encoding only HIGH/MEDIUM surprises (LOW excluded) — tier anchoring check confirms hierarchy; Chain Audit Check B validates tier consistency |
| C-10 | **PASS** | Riskiest assumption (Step 9): assumption at risk + signal + what would need to be true |
| C-11 | PASS | COMMIT-PBI with structural provenance confirmation |
| C-12 | PASS | Named handles, COMMIT-HANDLE-LEDGER; Institutional Archaeologist encodes correction, not discovery |
| C-13 | PASS | Independence check + Chain Audit Check A + Archaeologist handle framing explicitly encodes finding language ("correction the next team needs, not the discovery the original team made") |
| C-14 | PASS | Three-pointer Verified with quality tests |
| C-15 | PASS | Dedicated Provenance Enforcement Mechanism table, headed section |
| C-16 | PASS | Named checks with self-certifying quality tests in Verified |
| C-17 | PASS | Full table: Tier = "Structural > temporal", property (role-scope exclusion), reviewer implication ("A reviewer unfamiliar with the hierarchy can calibrate from this section alone without re-deriving the claim") — highest level + strongest reviewer implication phrasing of any variation |
| C-18 | PASS | Self-certifying quality tests (predicate, uniqueness, length; specificity, locatability, length) + Chain Audit Check C/D post-production validation of quotation fidelity |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 10/10 = 50
**Composite: 140 / 140**

---

## Score Summary and Rankings

| Rank | Variation | C-09 | C-10 | C-17 | C-18 | Asp | Composite | vs Prediction |
|------|-----------|------|------|------|------|-----|-----------|---------------|
| 1 (tie) | V-03 | PASS | PASS | PASS | PASS | 10/10 | **140** | = |
| 1 (tie) | V-05 | PASS | PASS | PASS | PASS | 10/10 | **140** | = |
| 3 (tie) | V-01 | FAIL | FAIL | PASS | PASS | 8/10 | **130** | = |
| 3 (tie) | V-02 | FAIL | FAIL | PASS | PASS | 8/10 | **130** | +5 (predicted 125) |
| 3 (tie) | V-04 | FAIL | FAIL | PASS | PASS | 8/10 | **130** | = |

All variations pass the golden threshold (all essential pass + composite ≥ 80).

---

## Excellence Signals

### ES-1: Post-production Chain Integrity Audit with visible tokens (V-03, V-05)

The chain integrity audit (CHAIN-COMPLETE / CHAIN-FLAG tokens per entry) adds a third enforcement layer that did not exist in R4 V-05:

- **Layer 1 (definition)**: Field vocabulary constraints prohibit bad language at production time (belief vs finding language in PBI/Handle; role-scope exclusion enforced during PBI writing)
- **Layer 2 (per-entry attestation)**: C-16/C-18 Verified fields attest checks were performed and quote what was found
- **Layer 3 (post-production audit)**: Chain Integrity Audit re-verifies all four chain elements [PBI-Ref → Handle → Source → Verified quotation] for internal consistency, producing visible CHAIN-COMPLETE tokens in the artifact

The distinguishing property: Layer 3 confirms that Layer 2 attestations are correct — it's not enough to say "I checked"; the audit confirms the check was accurate. This is the C-19 candidate: **chain integrity is auditable from output alone**, without re-running production steps.

### ES-2: Impact-anchored Rules of Thumb with traceability check (V-05 only)

Rules of Thumb encode the highest-impact findings in ≤20-word quotable form, with:
- Tier annotation matching the surprise entry tier (`[HIGH]` or `[MEDIUM]` only)
- RULES-ANCHORED traceability check confirming tier alignment after all rules are written

This creates a distilled output layer that: (1) is citable without reading full entries, (2) is anchored to the proven hierarchy, and (3) self-verifies its own accuracy via the traceability check. Potential C-20 candidate: **artifact includes an impact-anchored distillation layer verified against the hierarchy at production time**.

### ES-3: C-17 navigability finding — inline declaration passes minimum bar (from V-02 scoring deviation)

V-02 was designed to test "does dedicated-section placement matter for C-17?" The scoring result answers the question: **dedicated section is not required for C-17 minimum pass**. Inline declaration with tier + distinguishing property (no reviewer implication) achieves 130 identical to V-01 and V-04.

The navigability difference is:
- Inline declaration (V-02): PASS, minimum bar (tier + property)
- Dedicated section without reviewer implication: PASS, minimum bar
- Dedicated section with reviewer implication (V-01, V-04): PASS, highest level

The C-19 navigability candidate that V-02 was testing does not surface as a rubric criterion under v5 — navigability affects pass level but not pass/fail. This closes the navigability question from R5's design context. If v6 wants to reward navigability, it must formulate a dedicated criterion (e.g., "C-19: the enforcement mechanism declaration is in a headed section independently navigable without reading the artifact").

---

## New Criteria Candidates for v6

| Candidate | Basis | Pass condition |
|-----------|-------|----------------|
| C-19 | ES-1: Chain Integrity Audit | Artifact contains a post-production chain audit with visible per-entry CHAIN-COMPLETE tokens, distinct from the production-time attestation layer (C-16/C-18) |
| C-20 | ES-2: Rules of Thumb | Artifact includes impact-anchored distillation layer (Rules of Thumb) verified against the surprise hierarchy at production time via a named traceability check |
| C-21 | C-17 navigability (ES-3 residual) | The enforcement mechanism declaration is in a headed section independently navigable without full-artifact reading |

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["post-production chain integrity audit with visible CHAIN-COMPLETE tokens per entry — third enforcement layer (definition → per-entry attestation → post-production audit) confirming attestation correctness, not just attestation presence", "impact-anchored Rules of Thumb with RULES-ANCHORED traceability check — distilled output layer encoding highest-impact findings in quotable form, tier verified against surprise hierarchy at production time", "C-17 navigability is not a blocking pass-fail distinction under v5 — inline declaration with tier plus property reaches minimum-bar pass; dedicated section with reviewer implication reaches highest-level pass"]}
```
