Scoring against rubric v5 (C-01 through C-17; max 135). V-01's full prompt is present. V-02 through V-05 are scored from the variation map, state analysis, and structural descriptions since only V-01's prompt was provided.

---

## Scoring — V-01

**Axis:** Role sequence — prohibition as formal role-boundary declaration (two-part gate: completion + prohibition).

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 | PASS | Step 1C requires T-NN + threshold value + causal mechanism; "Exactly one binding tier" enforced by schema |
| C-02 | PASS | Step 2A table: minimum 2 hops, mechanism column restricted to 6 named values; generic labels prohibited |
| C-03 | PASS | Step 1B Tier Registry: minimum two distinct enforcing components enforced |
| C-04 | PASS | Step 2B header: "For each tier in the ROLE 1 Tier Registry — expand every T-NN row, omit none" — every T-NN required |
| C-05 | PASS | Step 2C: dedicated gap table with `Structural gap reason` column requiring structural explanation |
| C-06 | PASS | Step 2E: dedicated Retry-After Gap Assessment section; failure-mode vocabulary required |
| C-07 | PASS | Step 2D: cascade format requires T-NN chain with "minimum two downstream hops with explicit causal links" |
| C-08 | PASS | Step 1B: Threshold column forbids vague labels; "number with unit" or `not documented [reason]` required |
| C-09 | PASS | Step 2G: Mitigation Prescriptions; R4-confirmed pattern carries forward (Change + Tradeoff fields) |
| C-10 | PASS | Step 2F: every T-NN ranked by severity, justification referencing blast radius or impact frequency; top tier requires recovery time |
| C-11 | PASS | Step 1B: Source-ID column must match Step 1A register; "A threshold without a Source-ID is an unattributed claim" |
| C-12 | PARTIAL | Count-match checks at Steps 2B and 2F cover UX and severity coverage only; no global self-check section names all criterion categories (C-01 through C-05) before closing |
| C-13 | PASS | Step 1A Source Register required before first tier; minimum two named sources; inference prohibited |
| C-14 | PASS | Step 1C: single T-NN designation enforced; contrastive reasoning required for at least one non-binding tier |
| C-15 | PASS | Explicit ROLE 1 / ROLE 2 structure; "ROLE 1 COMPLETE" gate; PHASE BOUNDARY RULES; one-directional data dependency enforced |
| C-16 | PASS | Gate reads: "No new tier name, source reference, or limit value may be introduced after this declaration. A component appearing in ROLE 2 without a T-NN from Step 1B is a scope violation." Specific forbidden data classes named; scannable for compliance |
| C-17 | PASS | Step 2B: "For each tier in the ROLE 1 Tier Registry — expand every T-NN row, omit none:" names the specific prior artifact, not a vague class |

**V-01 composite:** 60 + 30 + (5+5+5+3+5+5+5+5+5) = **133/135**

---

## Scoring — V-02

**Axis:** Output format — named table artifacts with sequential identifiers (TABLE-A, TABLE-B, TABLE-C); consequence sections anchor by canonical table name.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 through C-08 | PASS | R4-confirmed under registry schema; table naming doesn't weaken enforcement |
| C-09 | PASS | R4-confirmed mitigation table with Change + Tradeoff fields |
| C-10 | PASS | R4-confirmed severity ranking with T-NN justification |
| C-11 | PASS | R4-confirmed Source-ID attribution requirement |
| C-12 | PARTIAL | Table-naming format doesn't inherently add a global criterion-level self-check; count-match checks remain section-level only |
| C-13 | PASS | R4-confirmed source register requirement |
| C-14 | PASS | R4-confirmed exclusivity designation + contrastive reasoning |
| C-15 | PASS | R4-confirmed role-locked sequencing carries forward even with TABLE labels overlaid |
| C-16 | PARTIAL | V-02's design targets C-17 (canonical anchoring), not C-16. Table-to-table references take the form "For each row in TABLE-B" (positive) rather than "no new tier name or limit value may appear after TABLE-A" (prohibition). Positive references satisfy C-15 handoff but not C-16 prohibition requirement |
| C-17 | PASS | Named table identifiers (TABLE-A, TABLE-B) make consequence section headers anchor by canonical name: "For each row in TABLE-B" / "Expanding TABLE-B row by row" — specific prior artifact named |

**V-02 composite:** 60 + 30 + (5+5+5+3+5+5+5+3+5) = **131/135**

---

## Scoring — V-03

**Axis:** Phase-lock prohibition as primary structural organizing principle — stated before role and table definitions.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 through C-08 | PASS | R4-confirmed |
| C-09 | PASS | R4-confirmed |
| C-10 | PASS | R4-confirmed |
| C-11 | PASS | R4-confirmed |
| C-12 | PARTIAL | Prohibition-first framing primes model against violation but does not add a global criterion-level self-check section |
| C-13 | PASS | R4-confirmed |
| C-14 | PASS | R4-confirmed |
| C-15 | PASS | R4-confirmed |
| C-16 | PASS | Prohibition architecture declared first — before role definitions — makes prohibition the governing structural frame. Specific forbidden data classes named as primary constraints. Stronger form than V-01's gate-embedded declaration. |
| C-17 | PARTIAL | V-03 targets C-16 as its axis. Without an explicit "For each tier in [named artifact]" instruction in consequence section headers, the model may produce consequence coverage without an explicit named enumeration anchor. Coverage may be correct (C-04 satisfied) but C-17's auditing posture requirement is not structurally enforced |

**V-03 composite:** 60 + 30 + (5+5+5+3+5+5+5+5+3) = **131/135**

---

## Scoring — V-04

**Axis:** Combined — role sequence + lifecycle emphasis + basic enumeration anchor. Both C-16 and C-17 targeted.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 through C-08 | PASS | R4-confirmed + role sequence reinforces |
| C-09 | PASS | R4-confirmed |
| C-10 | PASS | R4-confirmed |
| C-11 | PASS | R4-confirmed |
| C-12 | PARTIAL | Lifecycle emphasis and combined structure strengthen output shape but don't add a dedicated criterion-level self-check step; count-match checks remain the coverage verification mechanism |
| C-13 | PASS | R4-confirmed |
| C-14 | PASS | R4-confirmed |
| C-15 | PASS | R4-confirmed |
| C-16 | PASS | Role sequence carries V-01's prohibition-in-gate form; lifecycle emphasis reinforces phase-lock framing |
| C-17 | PASS | Basic enumeration anchor explicitly added: consequence section headers include named cross-reference to prior tier inventory artifact |

**V-04 composite:** 60 + 30 + (5+5+5+3+5+5+5+5+5) = **133/135**

---

## Scoring — V-05

**Axis:** Maximum density — V-04 + inertia framing naming the three failure modes C-16/C-17 existence corrects + dedicated global self-verification step.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 through C-08 | PASS | R4-confirmed + structural density reinforces |
| C-09 | PASS | R4-confirmed |
| C-10 | PASS | R4-confirmed |
| C-11 | PASS | R4-confirmed |
| C-12 | PASS | "Maximum density" adds a dedicated global self-verification step (Step 2H or equivalent) that names all criteria by category and maps each to its output section — not just count-match checks. The inertia preamble's naming of specific failure modes also primes the model to complete the self-check comprehensively |
| C-13 | PASS | R4-confirmed |
| C-14 | PASS | R4-confirmed |
| C-15 | PASS | R4-confirmed |
| C-16 | PASS | Carries V-04's role-sequence prohibition; inertia framing additionally names the three C-16/C-17 failure modes, priming the model to understand why the prohibition exists — not just to follow a gate rule |
| C-17 | PASS | Carries V-04's explicit enumeration anchor; inertia preamble's "UX conclusions that cannot be traced to any registered tier" names the C-17 failure pattern, priming consequence section anchoring |

**V-05 composite:** 60 + 30 + (5+5+5+5+5+5+5+5+5) = **135/135**

---

## Composite Ranking

| Rank | Variation | Composite | All Essential | Gap |
|------|-----------|-----------|---------------|-----|
| 1 | V-05 | 135/135 | YES | none |
| 2 | V-01 | 133/135 | YES | C-12 PARTIAL |
| 2 | V-04 | 133/135 | YES | C-12 PARTIAL |
| 4 | V-02 | 131/135 | YES | C-12 PARTIAL, C-16 PARTIAL |
| 4 | V-03 | 131/135 | YES | C-12 PARTIAL, C-17 PARTIAL |

---

## Excellence Signals — V-05

**Pattern 1 — Prohibition-first declaration as primary structural frame.** Stating the data-lock prohibition architecture before any role or table definitions makes the prohibition the governing lens, not a gate decoration. V-01 embeds the prohibition inside the role-closing gate (it is the second half of a two-part gate form). V-03 and V-05 declare the prohibition first. The practical difference: a model that skims the prompt for "what are the roles?" will encounter the prohibition before the role definitions — the prohibition primes the structural design rather than closing it. This is a positioning effect above and beyond C-16's requirement that prohibitions exist.

**Pattern 2 — Dedicated global criterion-level self-verification step.** V-01 through V-04 use per-section count-match checks (row count must match registry count) that verify coverage for individual sections but do not produce a closing section that maps output to criterion categories. C-12 requires a self-check naming each criterion (bottleneck identified, propagation traced, tiers enumerated, UX described, burst path found). V-05's "maximum density" step adds a dedicated closing step (beyond count checks) that enumerates all criteria by name and maps each to its output section. This is the difference between coverage verification and criterion verification: coverage checks confirm row counts, criterion verification confirms that the analysis addressed each analytical question.

**Pattern 3 — Violation-class priming in the inertia preamble.** V-05's inertia framing names the specific violation patterns that C-16 and C-17 were introduced to prevent: retroactive source citation (citing sources after bottlenecks are named), mid-analysis tier introduction (naming a tier in ROLE 2 without a ROLE 1 T-NN), and UX conclusions untraceable to registered tiers (consequence section that references components absent from the evidence base). Naming violation classes before the structural rules appear activates model avoidance of those patterns as recognized failure modes — not just mechanical compliance with a prohibition rule. A model told "don't do X" follows a rule; a model shown "X is the failure mode we discovered in prior analyses" avoids X because it recognizes the failure mode.

---

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["prohibition-first declaration: state the data-lock prohibition architecture as the primary structural frame before any role or table definitions, so the prohibition governs the prompt design rather than decorating role gate closings — a positioning effect that primes the model before roles are defined", "dedicated global criterion-level self-verification step: a named closing step that enumerates all analytical criteria by name and maps each to its output section, replacing per-section count-match checks that verify coverage for individual tables but not criterion completeness across the full analysis", "violation-class priming in inertia preamble: name the specific violation patterns C-16 and C-17 were introduced to prevent (retroactive source citation, mid-analysis tier introduction, UX conclusions untraceable to registered tiers) before the structural rules appear, activating model avoidance of recognized failure modes rather than mechanical rule-following"]}
```
