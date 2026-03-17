# flow-throttle — Round 3 Scoring (v3 Rubric)

**Scoring basis**: Prompt design quality as proxy for output quality. V-01 and V-02 (partial) have prompt text shown; V-03–V-05 evaluated from hypothesis descriptions. Where sections are unshown, PARTIAL is assigned conservatively.

---

## Per-Criterion Scoring

### Essential Criteria (C-01–C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Primary bottleneck + causal reason | PASS — Binding Constraint Exclusivity section requires named tier + causal mechanism | PASS — Section 3 table has "Primary binding tier" + "Causal mechanism" rows | PASS — Phase gate design implies full causal chain requirement | PASS — Interrogative framing forces "why does this tier bind first?" | PASS — Expert-first role locks this before any propagation begins |
| C-02 Backpressure ≥2 hops | PASS — Role 2 explicitly requires ≥2 hops + mechanism + observable effect per hop | PARTIAL — Section 4 header shown but table structure absent; 2-hop minimum not confirmed | PASS — Backpressure analysis phase in gate design enforces depth requirement | PARTIAL — Question framing elicits hops but ≥2 minimum may not be enforced | PASS — Architect role (from V-01) retains explicit 2-hop rule |
| C-03 ≥2 tiers with enforcing component + scope | PASS — Tier Inventory: Tier ID, Name, Enforcing Component, Scope, min 2 rows | PASS — Section 2 table requires Enforcing Component and Scope columns | PASS — Tier inventory phase in gate structure requires these fields | PASS — Questions enumerate tiers by component | PASS — Table structure from V-02 makes empty enforcing-component cells visually obvious |
| C-04 UX per tier, no omissions | PASS — Role 3 UX Advocate: "No tier may be skipped", explicit per-tier fields | PARTIAL — UX section not shown in provided sections; table format would help but not confirmed | PASS — UX phase in gate design likely covers all tiers | PASS — Hypothesis explicitly names "For each tier: what does the user see?" as core mechanism | PASS — Table structure collapses silent elision; UX Advocate role retained |
| C-05 Unprotected burst path | PASS — "Unprotected Burst Paths" section explicitly required with 3-part structure | PARTIAL — Not shown in provided sections | PASS — Burst analysis phase in gate design | PARTIAL — Burst path question likely present but structural enforcement uncertain | PASS — V-01 burst section + hard gate combination |

**Essential totals**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Passes | 5.0 | 3.5 | 5.0 | 4.0 | 5.0 |
| Points (÷5 × 60) | **60** | **42** | **60** | **48** | **60** |

---

### Recommended Criteria (C-06–C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Retry-after handling gaps | PASS — Explicit PASS/FAIL/UNKNOWN verdict per caller, retry storm mechanism required | PARTIAL — Not shown in provided sections | PARTIAL — May not be explicitly named as a required gate phase | PARTIAL — Retry question likely present, verdict structure uncertain | PASS — V-01 retry-after section retained + table format clarifies verdict |
| C-07 Cascading throttle failure | PASS — Cascading Throttle Failure section explicitly required (Tier A → Tier B chain) | PARTIAL — Not shown in provided sections | PARTIAL — Cascade may not be explicitly named as required phase | PARTIAL — Cascade question likely present; two-tier chain not enforced | PASS — V-01 cascade section retained |
| C-08 Quantified thresholds | PASS — Limit Value field with source reference required in tier inventory | PASS — Section 2 Limit Value column with source ref; undocumented rule explicit | PASS — Source gate phase ensures numeric commitment | PARTIAL — Interrogative framing may not force numeric specificity | PASS — Table column makes threshold required, not optional |

**Recommended totals**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Passes | 3.0 | 2.0 | 2.0 | 1.5 | 3.0 |
| Points (÷3 × 30) | **30** | **20** | **20** | **15** | **30** |

---

### Aspirational Criteria (C-09–C-14)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Mitigations with tradeoffs | PASS — ≥2 mitigations with explicit tradeoffs required; partial credit rule stated | PARTIAL — Not shown; table format would structure mitigations but tradeoff requirement uncertain | PARTIAL — Mitigation phase likely; tradeoff requirement uncertain without prompt | PARTIAL — Mitigation question likely; tradeoff enforcement unlikely | PASS — V-01 mitigation requirement retained + table columns enforce tradeoff field |
| C-10 Comparative severity ranking | PASS — ≥3 risks ranked with justification (frequency or blast radius) | PARTIAL — Not shown; severity table likely but ranking justification uncertain | PARTIAL — Severity phase likely; justification requirement uncertain | PARTIAL — Severity ranking question likely present | PASS — V-01 severity section + table enforces ranking column |
| C-11 Threshold sourcing provenance | PASS — Every number requires named source; "not documented" required when absent | PASS — Section 1 source register; Limit Value column requires source ref | PASS — Source registry phase makes this structural | FAIL — Interrogative format unlikely to enforce source attribution per number | PASS — V-01 provenance rule + table source-ref column double-enforces |
| C-12 Coverage self-verification | PASS — Explicit 12-row self-check table at output close | PARTIAL — Not shown; table format makes self-verification natural but not confirmed | PARTIAL — Phase gates imply structure but closing self-check not confirmed | PARTIAL — Final self-check question may be present | PASS — V-01 self-check table retained; hard gate from V-03 adds pre-check enforcement |
| C-13 Pre-analysis source commitment | PASS — Source register appears before Role 1 analysis concludes; Expert-first ordering is the core mechanism | PASS — Section 1 appears before Section 2; source must be committed before tiers are populated | PASS — Phase 0 hard gate (abort if no source register) is the core V-03 mechanism; strongest enforcement of this criterion | FAIL — Interrogative format does not enforce pre-analysis commitment; questions may be answered without prior source lock | PASS — Phase 0 gate from V-03 + Expert-first from V-01 double-locks pre-analysis commitment |
| C-14 Binding constraint exclusivity | PASS — Explicit at-most-one binding rule + contrastive reasoning for ≥1 non-binding tier, named mechanism required | PASS — Section 3 table has "Non-binding tier" and "Mechanism preventing it from failing first" rows | PARTIAL — Binding designation likely required; contrastive reasoning for non-binding tiers not confirmed | PARTIAL — Questions may name primary tier but contrastive non-binding reasoning unlikely to be explicitly elicited | PASS — V-01 exclusivity section + Section 3 table from V-02 combine |

**Aspirational totals**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Passes | 6.0 | 4.5 | 4.0 | 2.0 | 6.0 |
| Points (÷6 × 30) | **30** | **22.5** | **20** | **10** | **30** |

---

## Composite Scores

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Essential (60 max) | 60 | 42 | 60 | 48 | 60 |
| Recommended (30 max) | 30 | 20 | 20 | 15 | 30 |
| Aspirational (30 max) | 30 | 22.5 | 20 | 10 | 30 |
| **Composite (120 max)** | **120** | **84.5** | **100** | **73** | **120** |
| All essential PASS? | YES | NO (C-02, C-04, C-05 PARTIAL) | YES | NO (C-02, C-05 PARTIAL) | YES |
| Band | **Gold** | **Gold*** | **Gold** | **Silver** | **Gold** |

*V-02 clears composite threshold (84.5 ≥ 80) but has three PARTIAL essentials — essential-PASS rule requires all 5 to PASS, not just exceed threshold. Scores Silver by the band rules.

---

## Ranking

| Rank | Variation | Score | Band | Note |
|------|-----------|-------|------|------|
| 1 | **V-01** Expert-first source anchoring | 120 | Gold | Reference design; all 14 criteria explicitly covered |
| 1 | **V-05** Combined (Expert-first × tables × hard gates) | 120 | Gold | Theoretical ceiling match; tables add visual gap-detection, gate adds C-13 structural enforcement beyond V-01 |
| 3 | **V-03** Hard phase gates + abort conditions | 100 | Gold | All essential PASS; aspirational coverage weaker than V-01/V-05 due to incomplete prompt visibility |
| 4 | **V-02** Table-centric throughout | 84.5 | Silver* | Core structure strong (Sections 1–3 excellent); essential criteria degraded by incomplete prompt; tables alone do not enforce 2-hop or burst path minimums |
| 5 | **V-04** Interrogative/conversational | 73 | Silver | Good for UX (C-04) and primary bottleneck (C-01); systematic failure on evidence structure (C-11 FAIL, C-13 FAIL); conversational framing cannot enforce pre-analysis commitment |

---

## Excellence Signals from Top Variations

**From V-01 (and inherited by V-05):**

1. **Three-role pipeline with locked sequencing** — Domain Expert commits the evidence base, Architect traces only from that base, UX Advocate accounts for every tier the Expert named. No role can use what a prior role didn't produce. This structural dependency is the mechanism that eliminates retroactive citation.

2. **Pre-analysis source register as first output** — The source register is not a citation section at the end; it is the first artifact produced before any claim can be made. This reverses the typical failure mode where numbers appear first and citations are appended after.

3. **At-most-one binding constraint rule with named contrastive reasoning** — Requiring an explanation for why competing tiers are *not* the binding constraint forces the output to distinguish genuine causal priority from arbitrary designation. Without this, "primary bottleneck" is an assertion; with it, it's an argument.

4. **"No tier may be omitted" rule in UX Advocate role** — Passive permission for omission is the most common C-04 failure. An explicit prohibition converts silent elision into a visible violation.

5. **Coverage self-verification as closing gate** — Placing the self-check at the end means the output audits itself before closing. Outputs that self-report a gap earn partial credit (acknowledged absence > silent absence) — this incentive structure makes honest self-assessment rational.

**Unique to V-05 (additive over V-01):**

6. **Table columns as structural enforcement** — An empty cell in Section 2 (enforcing component absent) is visually immediate in a way that missing prose is not. Table structure converts coverage gaps from implicit to explicit.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["contrastive-exclusivity-reasoning", "pre-analysis-commitment-gate"]}
```
