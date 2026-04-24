## Scorecard: mock-all Variate R7

**Rubric:** v7 (C-01–C-20; aspirational denominator = 12)
**Date:** 2026-03-15

---

## Scoring Key

| Tier | Criteria | Weight | Per-criterion |
|------|----------|--------|--------------|
| Essential | C-01–C-05 | 60% | 12 pts each |
| Recommended | C-06–C-08 | 30% | 10 pts each |
| Aspirational | C-09–C-20 | 10% | 0.833 pts each |

---

## V-01 — Role-Sequence Baseline

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** All 9 namespaces with MOCK ARTIFACT headers | PASS | Role structure requires all nine |
| **C-02** Category classification correct | PASS | ROLE 1 CLASSIFIER with explicit Category column |
| **C-03** REAL-REQUIRED on EVIDENCE-HEAVY namespaces | PASS | Column in classification table |
| **C-04** Coverage summary table present | PASS | ROLE 3 SUMMARIZER |
| **C-05** Final handoff pattern | PASS | ROLE 4 HANDOFF WRITER |
| **C-06** Tier 2/3 critical flagged in summary | PASS | Tier 2/3 Critical column in table |
| **C-07** Plausible synthetic artifact body per namespace | PASS | ROLE 2 artifact body placeholder |
| **C-08** Compliance-tagged topics pre-flagged | PASS | Compliance-Tagged column in table |
| **C-09** Tier flag scopes output | PASS | Inherited from R6 base |
| **C-10** Next steps actionable and namespace-specific | PASS | "exact skill invocation — `/namespace:skill {topic}`; not generic advice" |
| **C-11** Classification table before first artifact body | PASS | ROLE 1 completes before ROLE 2 activates |
| **C-12** Handoff isolated in labelled section | PASS | ROLE 4 structurally isolated |
| **C-13** REAL-REQUIRED with rationale | PASS | ROLE 2 gate requires rationale-accompanied statement |
| **C-14** Explicit stop-gate at each phase boundary | PASS | Three stop-gates, one per ROLE transition |
| **C-15** Artifact body register-matches Category (with DO NOT) | PASS | DO NOT-use column in classification table |
| **C-16** Stop-gates enumerate specific fields | PASS | Gate enumerates all 7 classification fields by name |
| **C-17** Vocabulary rules as table columns | PASS | MUST use / DO NOT use columns co-located with Category |
| **C-18** Named role-identity per phase | PASS | CLASSIFIER / GENERATOR / SUMMARIZER / HANDOFF WRITER |
| **C-19** Placeholder contains inline depth anchor | **FAIL** | Placeholder is `{artifact body — vocabulary-compliant…}` — no sentence count in token text |
| **C-20** Inertia answer drives next-step derivation | **FAIL** | No inertia question or derivation bridge exists |

**Aspirational pass:** 10/12
**Score:** 60 + 30 + (10/12 × 10) = **98.3**

---

## V-02 — Minimal Inline Depth Anchor

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-18 | PASS (all) | Same structure as V-01 |
| **C-19** Placeholder contains inline depth anchor | **PASS** | Placeholder is `{3-5 sentence artifact body — register matches Category…}` — depth cue is the token name itself |
| **C-20** Inertia answer drives next-step derivation | **FAIL** | No inertia mechanism; next steps are generic "exact skill invocation" |

**Aspirational pass:** 11/12
**Score:** 60 + 30 + (11/12 × 10) = **99.2**

---

## V-03 — Explicit Inertia Derivation Bridge

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-18 | PASS (all) | Same structure as V-01 |
| **C-19** Placeholder contains inline depth anchor | **FAIL** | Body placeholder is `{artifact body — vocabulary-compliant… grounded in the inertia statement above}` — no sentence count in token text |
| **C-20** Inertia answer drives next-step derivation | **PASS** | ROLE 3 instruction: "the skill call that closes the specific gap named in this namespace's inertia statement from ROLE 2 — Derive from the inertia answer. A recommendation valid for any topic or namespace without reference to the inertia answer is not valid here." Gate explicitly rejects inertia-disconnected recommendations. |

**Aspirational pass:** 11/12
**Score:** 60 + 30 + (11/12 × 10) = **99.2**

---

## V-04 — Role-Sequence + Output-Format Combination

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-18 | PASS (all) | Inherits role identity + expanded field-enumeration gates from V-01; ROLE 2 gate adds register-mismatch as gate failure mode |
| **C-19** Placeholder contains inline depth anchor | **PASS** | Placeholder is `{3-5 sentence artifact body — register matches Category…}` identical to V-02 form |
| **C-20** Inertia answer drives next-step derivation | **FAIL** | No inertia mechanism; next steps are "exact skill invocation — not generic advice" |

**Note on C-16:** V-04's expanded gate language ("Do not activate ROLE 3 until you have verified: (1)…(4)…") is a marginal improvement over V-01 but does not change the PASS verdict — C-16 was already passing.

**Aspirational pass:** 11/12
**Score:** 60 + 30 + (11/12 × 10) = **99.2**

---

## V-05 — Full Combination (All Three Axes)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-18 | PASS (all) | Role identity + expanded gates + inertia preamble |
| **C-19** Placeholder contains inline depth anchor | **PASS** | Placeholder is `{3-5 sentence artifact body — register matches Category…; body must be grounded in the inertia statement above — a body that could exist without the inertia answer must be revised}` — depth cue is the first element of the token |
| **C-20** Inertia answer drives next-step derivation | **PASS** | ROLE 3: "Derive from the inertia answer. A recommendation valid for any topic or namespace without reference to the inertia answer is not valid here." ROLE 3 gate: "inertia-disconnected next step fails this gate." |

**Aspirational pass:** 12/12
**Score:** 60 + 30 + (12/12 × 10) = **100**

---

## Variation Ranking

| Rank | Variation | Score | C-19 | C-20 |
|------|-----------|-------|------|------|
| 1 | **V-05** | **100** | PASS | PASS |
| 2 (tied) | V-02 | 99.2 | PASS | FAIL |
| 2 (tied) | V-03 | 99.2 | FAIL | PASS |
| 2 (tied) | V-04 | 99.2 | PASS | FAIL |
| 5 | V-01 | 98.3 | FAIL | FAIL |

---

## Excellence Signals — V-05

**1. Dual-anchor placeholder token.**
The body placeholder carries two quality requirements inline: `{3-5 sentence artifact body — … body must be grounded in the inertia statement above — a body that could exist without the inertia answer must be revised}`. Both depth and grounding are visible at fill time, not buried in prose. Neither constraint needs to be remembered from a separate section.

**2. Inertia field as structural forcing function.**
The `Without this signal, {topic}'s feature story would be missing:` field precedes the body placeholder in the template. This forces gap analysis before content generation — the model cannot write the artifact body without having named the gap first. The sequence is architectural, not advisory.

**3. Gate rejection language names the specific anti-pattern.**
ROLE 3 gate does not say "next steps must be specific." It says: "A recommendation valid for any topic or namespace without reference to the inertia answer is not valid here." The negative form targets the exact failure mode — namespace-agnostic filler recommendations — rather than restating the positive instruction.

**4. Closed inertia loop across roles.**
V-05 creates an explicit three-link chain: ROLE 2 inertia statement → ROLE 2 artifact body (grounded in gap) → ROLE 3 next step (closes named gap). The same inertia answer is the input to two separate outputs in two separate roles, enforced by both the template structure and the gate language. No equivalent loop exists in V-01 through V-04.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["dual-anchor placeholder: depth cue + grounding constraint as inline token text, both requirements visible at fill time", "inertia field as structural forcing function: required field preceding body placeholder forces gap analysis before content generation", "negative gate language targeting specific anti-pattern: rejects recommendations valid for any namespace, not just restates positive instruction"]}
```
