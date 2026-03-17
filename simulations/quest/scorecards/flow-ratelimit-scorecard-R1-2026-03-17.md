## flow-ratelimit R1 — Scorecard

### Scoring Key
- Essential: 12 pts (PARTIAL = 6)
- Recommended: 10 pts (PARTIAL = 5)
- Aspirational: 5 pts (PARTIAL = 2.5)

---

## V-01 — Table-Dominant Format

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | First-limit ordering | PARTIAL | TABLE 2 binding-order column requires causal reason, but schema-column enforcement produces label-level causation ("higher volume hits T-01 first") rather than mechanism-level reasoning. Table constraint prevents deep "why" chains. |
| C-02 | Backpressure chain | PASS | Named-set column + 2-hop minimum is the strongest structural guarantee of any variation for this criterion. |
| C-03 | UX per throttle tier | PASS | ≥2 tiers + specific error codes encoded in TABLE 4 column definitions. |
| C-04 | Unprotected burst path | PARTIAL | TABLE 5A column says "structural-absence language required," but encoding a conceptual distinction (structural vs. high-headroom) in a column header is weak enforcement. A model can write "no burst mechanism present" without genuinely testing for the structural gap. |
| C-05 | Retry-After gap check | PASS | TABLE 5B PASS/FAIL per caller + failure mode column is the most explicit structure for this criterion across all variations. |
| C-06 | Cascading throttle failure | PASS | TABLE 6 `Cascading effect` column requires second-tier causation, not coincidence. |
| C-07 | Numeric specificity | PASS | TABLE 1 `Limit` column rejects vague labels at schema level — strongest guarantee for this criterion. |
| C-08 | Volume-to-behavior mapping | PASS | TABLE 6 is the explicit mapping. |
| C-09 | Per-bottleneck mitigation | PASS | Free-form Mitigation Section requires named parameter per gap. |
| C-10 | Quantified spike | PARTIAL | Arithmetic is in the free-form Mitigation Section — the only non-table section. Models routinely produce shallower arithmetic in free-form blocks than in structured columns. |

**V-01 Total: 6 + 12 + 12 + 6 + 12 + 10 + 10 + 10 + 5 + 2.5 = 85.5**

---

## V-02 — Three Named Analyst Roles

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | First-limit ordering | PASS | Role A owns tier inventory with numeric limits and causal binding order. Handoff mechanism prevents Role B from starting until Role A produces this. |
| C-02 | Backpressure chain | PASS | Role B exclusively owns backpressure chain. Sequential gate prevents it from being crowded out by tier enumeration (a common failure mode). |
| C-03 | UX per throttle tier | PASS | Role B owns UX per tier with explicit ≥2-tier requirement. |
| C-04 | Unprotected burst path | PASS | Role C owns structural gap identification with explicit absence language requirement. Isolated role prevents this from being buried in a larger section. |
| C-05 | Retry-After gap check | PASS | Role C has explicit PASS/FAIL ownership. Handoff confirms Role B completed before Role C activates. |
| C-06 | Cascading throttle failure | PASS | Role B's cascade scenario is sequentially confirmed before Role C. The handoff note explicitly says a skipped cascade blocks Role C confirmation. |
| C-07 | Numeric specificity | PASS | Role A explicitly owns numeric limits. |
| C-08 | Volume-to-behavior mapping | PARTIAL | No explicit table schema enforced. Role C's arithmetic step covers volume-to-behavior implicitly, but a model can produce this as a prose paragraph. |
| C-09 | Per-bottleneck mitigation | PASS | Role C mitigation step requires named parameter. |
| C-10 | Quantified spike | PASS | Role C has a dedicated arithmetic step with explicit derivation-from-Role-A-limits requirement. Most focused arithmetic structure of any variation. |

**V-02 Total: 12 + 12 + 12 + 12 + 12 + 10 + 10 + 5 + 5 + 5 = 95**

---

## V-03 — Conversational Imperative

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | First-limit ordering | PASS | Step 2 ("Find the first bottleneck") requires causal explanation. Direct command is clear. |
| C-02 | Backpressure chain | PASS | Step 3 ("Follow the pressure") requires named mechanisms and ≥2 hops explicitly. |
| C-03 | UX per throttle tier | PASS | Step 4 requires specific error codes and ≥2 tiers. |
| C-04 | Unprotected burst path | PASS | Step 5 explicitly filters high-headroom paths — the negative filter ("not just high headroom") is the sharpest burst-path instruction of V-01–V-04. |
| C-05 | Retry-After gap check | PASS | Step 6 requires header-level evaluation and named failure mode. |
| C-06 | Cascading throttle failure | PASS | Step 8 explicitly requires causation vs. coincidence distinction. |
| C-07 | Numeric specificity | PARTIAL | Step 1 uses explicit negative examples ("not 'limited', not 'throttled'"), which is good. But no schema enforcement — conversational register risks drift to prose quantifiers like "a few hundred" or "moderate volume." |
| C-08 | Volume-to-behavior mapping | PARTIAL | Step 7 requests an explicit load table. But conversational register offers no column-level type constraints; a model can satisfy "load table" with an unstructured narrative table. |
| C-09 | Per-bottleneck mitigation | PARTIAL | Step 9 asks for named parameter. But without a table column schema or role handoff enforcing it, mitigation sections in conversational prompts frequently produce category descriptions ("add caching") rather than named parameters ("set `cache-ttl=300`"). |
| C-10 | Quantified spike | PASS | Step 10 requires arithmetic with derivation steps. Explicit enough to survive conversational register. |

**V-03 Total: 12 + 12 + 12 + 12 + 12 + 10 + 5 + 5 + 2.5 + 5 = 87.5**

---

## V-04 — Finding-First / Inverted Structure

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | First-limit ordering | PASS | VERDICT 1.1 forces the model to name the binding constraint as a claim before the evidence section. This commitment-before-evidence structure produces the clearest binding-order statements of any variation. |
| C-02 | Backpressure chain | PASS | Section 2.2 requires named mechanisms and ≥2 hops. |
| C-03 | UX per throttle tier | PASS | Section 2.3 requires specific error codes and ≥2 tiers, tied to VERDICT 1.3. |
| C-04 | Unprotected burst path | PARTIAL | Section 2.4 requires structural-absence language. However, the verdict-first structure creates a risk: the model commits to "burst path = unprotected" in VERDICT 1.4 before doing the structural analysis. If the burst path is only partially unprotected (e.g., leaky bucket exists but no max-queue guard), a pre-committed verdict can anchor the model to confirming rather than testing the structural gap. |
| C-05 | Retry-After gap check | PASS | Section 2.5 PASS/FAIL with failure mode. |
| C-06 | Cascading throttle failure | PASS | Section 2.6 cascade evidence must confirm or explicitly revise VERDICT 1.5 — this is a built-in consistency check. |
| C-07 | Numeric specificity | PASS | Section 2.1 tier inventory requires number + unit. |
| C-08 | Volume-to-behavior mapping | PASS | Section 3 is the dedicated volume-to-behavior table. |
| C-09 | Per-bottleneck mitigation | PASS | Section 4 Mitigation Table has a named-parameter column with explicit "rejects generic advice" instruction. |
| C-10 | Quantified spike | PASS | Section 5 is a dedicated arithmetic block with derivation requirement from 2.1 limits. |

**V-04 Total: 12 + 12 + 12 + 6 + 12 + 10 + 10 + 10 + 5 + 5 = 94**

---

## V-05 — Inertia-Framed + Multi-Role + Mixed Format

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | First-limit ordering | PASS | Role 1 with TABLE A + causal binding order. Inertia framing primes "what makes the first limit bind in the baseline?" which sharpens the causal reasoning. |
| C-02 | Backpressure chain | PASS | Role 2 Part A requires named mechanisms and ≥2 hops. Sequential gate enforces completeness. |
| C-03 | UX per throttle tier | PASS | Role 2 Part B requires specific error codes and ≥2 tiers. |
| C-04 | Unprotected burst path | PASS | Role 3 Gap 1 filters high-headroom paths AND the inertia question ("is this gap structural or incidental?") is the only variation with an explicit structural-vs-incidental sub-test. This is the sharpest C-04 enforcement across all variations. |
| C-05 | Retry-After gap check | PASS | Role 3 Gap 2 requires PASS/FAIL + failure mode. Inertia framing adds "does the baseline handle this by default?" which produces an explicit two-part test rather than a single gap flag. |
| C-06 | Cascading throttle failure | PASS | Role 2 Part C explicitly distinguishes cascade from coincident throttling. |
| C-07 | Numeric specificity | PASS | TABLE A schema rejects vague labels. |
| C-08 | Volume-to-behavior mapping | PASS | Synthesis Table rows cover 1x/2x/5x with inertia vs. protected comparison — unique dual-state mapping that satisfies C-08 more richly than any other variation. |
| C-09 | Per-bottleneck mitigation | PASS | Mitigation Table has named-parameter column + `Improvement over inertia` column — dual enforcement that rejects both category descriptions and improvements that don't move from baseline. |
| C-10 | Quantified spike | PARTIAL | Role 3 Gap 3 requires arithmetic with derivation from TABLE A limits. Present and explicit. But V-05 has the most competing demands in Role 3 (Gap 1 burst-path analysis, Gap 2 Retry-After, Gap 3 arithmetic, plus inertia framing on each) — the arithmetic step is most likely to be compressed under total token pressure of any variation that attempts it. |

**V-05 Total: 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 5 + 2.5 = 97.5**

---

## Ranking Summary

| Rank | Variation | Score | Essential PASS | Notable gap |
|------|-----------|-------|----------------|-------------|
| 1 | V-05 Inertia + Roles | **97.5** | YES (all 5) | C-10 PARTIAL (arithmetic competes with heaviest Role 3 load) |
| 2 | V-02 Three Roles | 95 | YES (all 5) | C-08 PARTIAL (no table schema → prose risk) |
| 3 | V-04 Finding-First | 94 | NO (C-04 PARTIAL) | C-04 PARTIAL (verdict commitment anchors burst-path conclusion before structural test) |
| 4 | V-03 Conversational | 87.5 | YES (all 5) | C-07, C-08, C-09 all PARTIAL (no schema enforcement) |
| 5 | V-01 Table-Dominant | 85.5 | NO (C-01, C-04 PARTIAL) | C-01 PARTIAL (schema column ≠ reasoning depth), C-04 PARTIAL (structural concept too thin for column header) |

---

## Excellence Signals from V-05

**1. Inertia baseline as a reference state converts findings to deltas.**
Naming a do-nothing baseline before any analysis begins means every finding is categorized as "expected in baseline" or "gap from baseline." This is sharper than requiring "structural-absence language" in a column because the model is forced to ask *relative to what* the path is unprotected. Without a baseline, "structurally absent" is a claim; with inertia, it is a delta.

**2. Structural-or-incidental sub-question is more powerful than structural-absence column headers.**
V-01 encodes structural-absence as a column definition. V-05 encodes it as a two-part test: "high-headroom or structurally absent?" + "structural or incidental?" The sub-question forces the model to articulate *why* the path is structurally absent — it cannot satisfy the criterion by just writing "no burst mechanism present."

**3. Synthesis comparison table (inertia vs. protected at multiple load bands) satisfies C-08 more richly than a purpose-built volume-to-behavior table.**
The delta column — `inertia behavior | protected behavior | delta` — gives C-08 a double-column structure that no other variation generates. A purpose-built volume-to-behavior table (V-01 TABLE 6, V-04 Section 3) shows *what happens*. The V-05 synthesis table shows *what changes*, which is the question a rate-limit analysis actually needs to answer.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["inertia-baseline-as-reference-state: name a do-nothing baseline before analysis begins to convert observations into named deltas from baseline, sharpening structural-gap identification beyond what column-header language alone can enforce", "structural-or-incidental-sub-question: replace structural-absence column headers with an explicit two-part test (high-headroom-vs-absent + structural-vs-incidental) to force mechanism-level reasoning rather than label-level claims", "synthesis-comparison-table-with-delta-column: a table contrasting inertia-state vs. protected-state at multiple load bands (1x/2x/5x) satisfies volume-to-behavior mapping while generating unique cross-criteria evidence unavailable from a purpose-built single-state table"]}
```
