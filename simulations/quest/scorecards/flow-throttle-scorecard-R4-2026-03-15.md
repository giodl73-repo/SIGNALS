Now I have enough context to score. The v18 rubric file is a different track; the current task uses a fresh rubric (v4, C-01 through C-15). Only V-01 and V-02 are present in the task — V-03 through V-05 were cut off. I'll score based on structural analysis of the prompt templates against the new rubric criteria.

---

# flow-throttle Scorecard — Round 4 (Rubric v4, C-01–C-15)

**Date:** 2026-03-16
**Rubric max:** 125 | **Golden threshold:** all 5 essential PASS + composite ≥ 80
**Variations scored:** V-01 (complete), V-02 (prompt truncated after Phase B opening — scored on visible portions)
**Variations absent:** V-03, V-04, V-05 (not supplied; cannot score)

---

## V-01 — Role Sequence Axis

**Design:** Three-role pipeline (Domain Expert → Systems Architect → UX Advocate), each role explicitly prohibited from introducing data not produced by prior roles. Explicit Handoff Statements close each phase.

### Criterion Scores

| ID | Score | Evidence |
|----|-------|----------|
| **C-01** | **PASS** | Phase 2 requires "Designate exactly one tier... State the causal mechanism: why does this tier fail before all others." Both tier name and causal reason are structurally mandatory. |
| **C-02** | **PASS** | Phase 2 Backpressure Propagation: "trace how throttle pressure propagates for **at least two hops**. For each hop: Hop N / Mechanism / Observable effect." Minimum-hop count and format both explicit. |
| **C-03** | **PASS** | Phase 1 Tier Inventory requires Tier name + Enforcing component + Scope (per-connection/per-user/tenant/platform) for every tier. Multiple tiers structurally required by instruction. |
| **C-04** | **PASS** | Phase 3: "For **each tier in the Phase 1 inventory**: What the user sees / Time-to-impact." One-row-per-tier mapping enforced by reference to Phase 1 inventory. |
| **C-05** | **PASS** | Phase 2: "Identify **at least one** unprotected burst path... Name the specific mechanism (parallel branch fan-out, retry storm, cold-start surge, etc.)." Named mechanism required. |
| **C-06** | **PASS** | Phase 2 Retry-After Audit: per-caller verdict COMPLIANT / NON-COMPLIANT / UNKNOWN required. Non-compliant callers must state retry-storm risk. Both halves of C-06 pass condition satisfied. |
| **C-07** | **PASS** | Phase 2 Cascading Failure Scenario: "Tier A throttles → [mechanism] → Tier B receives [what] → Tier B throttles." Two-tier cascade with named causal link required. |
| **C-08** | **PASS** | Phase 2: "Restate the **numeric limit** for the binding constraint, citing its Phase 1 source register entry. Include at least one additional threshold for context." |
| **C-09** | **PASS** | Phase 3 Mitigations with Tradeoffs: per-gap format "Gap / Mitigation / Tradeoff" for every structural gap from Phase 2. Tradeoff column mandatory. |
| **C-10** | **PASS** | Phase 3 Severity Ranking: High/Medium/Low for all throttle risks including burst path and cascade, "justified by impact frequency or blast radius." Justification explicitly required. |
| **C-11** | **PASS** | Phase 1 Source Register provides named sources with documented/partially documented/not documented coverage. Phase 1 Tier Inventory: "Limit value — cite the source register entry by name. If no register entry exists, mark UNDOCUMENTED — do not infer or estimate." Both attribution and undocumented-path explicitly covered. |
| **C-12** | **PASS** | Phase 3 Coverage Self-Check table with columns Criterion / Addressed? / Where. All 14 substantive criteria listed by description. Any absent criterion is flagged as a gap rather than silently omitted. |
| **C-13** | **PASS** | Source Register is the **first output** of Phase 1, before any tier or number. Phase 1 Handoff Statement: "Phase 2 draws only from the Source Register and Tier Inventory above. No new data sources may be introduced after this line." Evidence base committed before analysis begins. |
| **C-14** | **PASS** | Phase 2: "Designate **exactly one** tier... Do not designate two tiers as co-equal binding constraints. Then provide contrastive reasoning for **at least one non-binding tier**: name the mechanism that prevents it from failing first." Both components of C-14 explicitly required. |
| **C-15** | **PASS** | Three named phases with explicit one-directional constraints: Phase 2 explicitly states "You may not introduce any new tier, limit value, or source reference." Phase 3 explicitly states "You may not introduce new tiers, new sources, or new failure modes." Handoff Statements close each phase. An undifferentiated output is architecturally impossible — the three-role structure enforces the phase boundary at instruction level. |

### V-01 Composite

| Band | Pass | Weight | Points |
|------|------|--------|--------|
| Essential (C-01–C-05) | 5 / 5 | 60 | **60** |
| Recommended (C-06–C-08) | 3 / 3 | 30 | **30** |
| Aspirational (C-09–C-15) | 7 / 7 | 35 | **35** |
| **Total** | | | **125 / 125** |

All essential pass: **YES** | Golden: **YES**

---

## V-02 — Output Format Axis

**Design:** Table-dominant format with explicit phase banners and handoff markers. Single-author structure (no role separation). Phases A/B enforce source-register-before-tier-inventory sequencing. The visible prompt ends at the opening of the Binding Constraint Declaration in Phase B — Phases C onward are not supplied.

**Scoring caveat:** Criteria that depend on unseen phases (Phase C onward) are scored PARTIAL where the hypothesis provides strong structural intent, or INFERRED-FAIL where the format provides no mechanism.

### Criterion Scores

| ID | Score | Evidence |
|----|-------|----------|
| **C-01** | **PARTIAL** | Binding Constraint Declaration is present ("designate exactly one tier as the binding constraint"), but the **causal mechanism** requirement (why does this tier fail before others?) is not visible in the truncated prompt. Table format is unlikely to force causal prose naturally. |
| **C-02** | **INFERRED-PASS** | Table-dominant format would produce a Backpressure table (not shown). Hypothesis explicitly mentions "every tier must appear in the tier table before it can be referenced in the propagation table" — structural pre-registration enforces C-02's hop coverage if the backpressure table is present. Scored PASS on table-enforcement inference; degrades to PARTIAL if Phase C is prose-only. |
| **C-03** | **PASS** | Phase B Tier Inventory table with Tier / Enforcing Component / Scope / Limit / Source Register Entry is explicitly visible. Multiple tiers with enforcing component required by table structure. |
| **C-04** | **INFERRED-PARTIAL** | UX section not visible. Table format would likely enforce one-row-per-tier UX if a UX table is present, but without explicit "for each tier in Phase B inventory" instruction (as V-01 has), rows could be omitted. |
| **C-05** | **INFERRED-PASS** | Burst path section likely present (consistent with hypothesis that all analysis sections appear as tables). Without visible instruction requiring a specific burst mechanism name, reduces to PARTIAL. Scored PARTIAL. |
| **C-06** | **INFERRED-PARTIAL** | Retry-After audit likely present as a table. Whether COMPLIANT/NON-COMPLIANT/UNKNOWN verdict and retry-storm consequence are required is unknown. |
| **C-07** | **INFERRED-PASS** | Cascading failure likely present. Table format would force Tier A / mechanism / Tier B if table schema requires it. PARTIAL without visible schema. |
| **C-08** | **PASS** | Phase B Tier Inventory includes a Limit column with Source Register Entry. Numeric limit for at least one tier is structurally required. Primary bottleneck numeric threshold covered. |
| **C-09** | **INFERRED-PARTIAL** | Mitigations section likely present. Table format may include a Mitigation column but the **tradeoff** component is aspirational and easy to omit without explicit column enforcement. |
| **C-10** | **INFERRED-PARTIAL** | Severity ranking not visible. Table format could enforce it, but justification requirement (impact frequency / blast radius) is easy to miss without explicit mandate. |
| **C-11** | **PASS** | Phase A Source Register names sources with coverage ratings. Phase B requires each tier to cite a Source Register entry. Source chain from Register → Tier → number is structurally enforced by the table's cross-reference column. |
| **C-12** | **INFERRED-PARTIAL** | Self-check section not visible. Table-dominant format does not inherently generate a coverage verification table unless explicitly required. |
| **C-13** | **PASS** | Phase A (Source Register) appears before Phase B (Tier Inventory). Handoff A→B: "Source Register closed. Phase B draws only from this table." Evidence base locked before tier enumeration. |
| **C-14** | **PARTIAL** | Binding Constraint Declaration visible but only "designate exactly one tier." **Contrastive reasoning for at least one non-binding tier** (C-14's second requirement) is not visible. Single-author format without explicit contrastive-prose instruction is likely to omit this. |
| **C-15** | **PARTIAL** | Phase A and Phase B are named with an explicit handoff banner — two named phases with handoff statement satisfy the structural minimum. However, V-02 is a **single-author** format: the instruction prohibiting introduction of new data in later phases ("You may not introduce any new tier") is NOT present. The evidence-phase-to-analysis-phase dependency is enforced by table pre-registration (tiers must appear in Phase B before being cited in Phase C) but this is weaker than V-01's explicit prohibition. "An output with all correct content in a single undifferentiated block fails" — V-02 avoids that, but the one-directional enforcement relies on table conventions rather than role-based structural incapability. |

### V-02 Composite (Estimated)

| ID | Points |
|----|--------|
| C-01 PARTIAL | 6 |
| C-02 PARTIAL | 6 |
| C-03 PASS | 12 |
| C-04 PARTIAL | 3 |
| C-05 PARTIAL | 3 |
| C-06 PARTIAL | 5 |
| C-07 PARTIAL | 5 |
| C-08 PASS | 10 |
| C-09 PARTIAL | 2.5 |
| C-10 PARTIAL | 2.5 |
| C-11 PASS | 5 |
| C-12 PARTIAL | 2.5 |
| C-13 PASS | 5 |
| C-14 PARTIAL | 2.5 |
| C-15 PARTIAL | 2.5 |

Applying rubric bands:
- Essential: C-01 PARTIAL (0.5) + C-02 PARTIAL (0.5) + C-03 PASS + C-04 PARTIAL (0.5) + C-05 PARTIAL (0.5) = 3/5 essential-equivalents → 3.0/5 × 60 = **36 pts** (C-01 and C-04 PARTIAL means essential gate NOT guaranteed)
- Recommended: C-06 PARTIAL (0.5) + C-07 PARTIAL (0.5) + C-08 PASS = 2.0/3 × 30 = **20 pts**
- Aspirational: C-09 PARTIAL + C-10 PARTIAL + C-11 PASS + C-12 PARTIAL + C-13 PASS + C-14 PARTIAL + C-15 PARTIAL = (0.5+0.5+1+0.5+1+0.5+0.5)/7 × 35 = 4.5/7 × 35 ≈ **22.5 pts**

**V-02 Composite: ~78.5 / 125** (below golden threshold of 80, and essential gate is at risk)
All essential pass: **NO** (C-01 PARTIAL — causal mechanism not confirmed)

---

## V-03 through V-05

**Not provided in this invocation.** These variations cannot be scored.

---

## Ranking (scored variations only)

| Rank | Variation | Composite | All Essential Pass | Golden |
|------|-----------|-----------|-------------------|--------|
| 1 | **V-01** | **125 / 125** | YES | YES |
| 2 | V-02 | ~78.5 / 125 | NO (C-01 at risk) | NO |

---

## Excellence Signals (from V-01)

**Signal 1 — Explicit data-introduction prohibition per role.**
V-01 Phase 2 says "You may not introduce any new tier, limit value, or source reference"; Phase 3 says "You may not introduce new tiers, new sources, or new failure modes." These prohibitions make retroactive citation architecturally incapable rather than merely discouraged. A single-author format with handoff markers (V-02) relies on the model's compliance with a convention; a role boundary enforced by explicit prohibition is a structural gate.

**Signal 2 — Three-role separation removes the rationalization path for late data injection.**
By assigning Domain Expert, Systems Architect, and UX Advocate as distinct named agents with distinct mandates, V-01 removes the rationalization path available in single-author prompts: a single author can always internally conclude "I'll add this source here since it's relevant." A named role that produced zero rows in Phase 1 cannot legitimately add sources in Phase 2 without violating the stated role identity.

**Signal 3 — Coverage Self-Check table enumerates all criteria by name in Phase 3.**
The explicit 14-row self-check table forces the model to confirm or flag each criterion individually. This satisfies C-12 more reliably than a general "verify coverage" instruction because each criterion is a binary attestation, not a holistic verdict.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["explicit per-role data-introduction prohibition makes retroactive citation architecturally impossible rather than merely discouraged", "three-role identity separation removes the single-author rationalization path for late evidence injection", "per-criterion self-check table in consequence phase converts coverage verification from holistic to binary attestation"]}
```
