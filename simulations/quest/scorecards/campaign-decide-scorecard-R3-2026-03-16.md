# Quest Score — campaign-decide / Round 3 (v3 Rubric)

## Scoring Framework

**Formula:**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```
Each aspirational criterion is worth **1.43 pts** (10/7). Six passing = 8.57. Seven = 10.0.

---

## V-01 — Phase 0 structural lock (C-13 axis)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | `Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]` — explicit labeled field in Phase 5. |
| C-02 | **PASS** | `Confidence: [High/Medium/Low]` — labeled field in Phase 5. |
| C-03 | **PASS** | Phase 0 = prove-hypothesis, Phase 1 = competitors, Phase 2 = feasibility, Phase 3 = market, Phase 4 = websearch, Phase 5 = synthesize. All six domains present. |
| C-04 | **PASS** | `Ordering rule: all Inertia fields must precede any Rival field.` Inertia fields explicitly enumerated before rivals in Phase 1. |
| C-05 | **PASS** | Because block with four `because Phase N, [field]` citations. Recommendation is anchored to named phases. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Named labeled fields per phase, titled phase headers, summary + recommendation block in Phase 5. |
| C-07 | **PASS** | `Counter-evidence:` required field in Phase 5. |
| C-08 | **PASS** | `Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves the Phase 0 claim]` — explicit disposition field. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | `Confidence rationale: [name the specific findings or gaps that drove this rating — not just the label]` — required narrative field. |
| C-10 | **PASS** | `Next step: [COMMIT → concrete action, not "do more research" | no-build → exit condition or revisit trigger]` — conditioned by recommendation type. |
| C-11 | **PASS** | Named labeled rows per phase (Phase 0: 6 fields; Phase 1: inertia + rival rows; Phase 2: 4 feasibility dimensions + risk). Per-phase schema is structurally present. |
| C-12 | **PASS** | Because block prescribes `because Phase N, [field]` format explicitly. Rubric example syntax matched. |
| C-13 | **PASS** | Phase 0 header says `[PRIOR COMMITMENT — COMPLETE BEFORE SCOUTING]`. Template position enforces commitment before Phase 1 executes. PASS by construction. |
| C-14 | **PASS** | Four Because slots reference `Phase 0`, `Phase 1`, `Phase 2`, `Phase 3 or Phase 4` — minimum 3 distinct phase prefixes guaranteed even in the compressed case. Template makes single-phase collapse structurally awkward. |
| C-15 | **FAIL** | No FID system. Named fields (e.g., `Status-quo inertia:`) are human-readable labels, not enumerable per-finding keys. `because Phase 1, inertia field` passes C-12 but fails C-15. |

**Aspirational: 6/7 → 8.57 pts**

**V-01 Composite: 60 + 30 + 8.57 = 98.57 → 98.6 | Gold**

---

## V-02 — Five-phase labeled Because slots (C-14 axis)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase 6 table: `Recommendation` row required. |
| C-02 | **PASS** | Phase 6 table: `Confidence` row required. |
| C-03 | **PASS** | Phases 1–5 = competitors, feasibility, market, hypothesis, websearch + Phase 6 = synthesize. All six domains. |
| C-04 | **PASS** | Phase 1 table: `Inertia rows must precede named rival rows.` Structural table ordering enforces this. |
| C-05 | **PASS** | Five labeled Because slots each require a phase citation. Recommendation fully traceable. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Tables per phase + section headers + Phase 6 summary table. |
| C-07 | **PASS** | `Counter-evidence` row in Phase 6 table. |
| C-08 | **PASS** | `Hypothesis outcome [Confirmed/Refuted/Inconclusive]` row in Phase 6 table. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | `Confidence rationale` row: `[name specific evidence gaps or strengths — not just the label]`. |
| C-10 | **PASS** | `Next step` row: conditioned on COMMIT vs. no-build. |
| C-11 | **PASS** | Table-per-phase structure. Each phase has its own row schema verifiable at the phase level. |
| C-12 | **PASS** | Five Because slots prescribe `[claim] because Phase N, [force/dimension/field]` syntax throughout. Rubric example matched exactly. |
| C-13 | **FAIL** | Hypothesis is Phase 4. Phases 1, 2, 3 (competitors, feasibility, market) execute before the hypothesis is committed. Fails rubric requirement: "committed before any evidence phase executes." |
| C-14 | **PASS** | Five labeled slots — `PHASE 1 (competitors)`, `PHASE 2 (feasibility)`, `PHASE 3 (market)`, `PHASE 4 (hypothesis)`, `PHASE 5 (web evidence)`. Citations span exactly 5 distinct phases. PASS by template construction. |
| C-15 | **FAIL** | No FID system. Phase+section citations satisfy C-12 but do not provide per-finding enumerable keys. |

**Aspirational: 5/7 → 7.14 pts**

**V-02 Composite: 60 + 30 + 7.14 = 97.14 → 97.1 | Gold**

---

## V-03 — Pre-assigned FIDs (C-15 axis)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | F6-02 `Recommendation` field required. |
| C-02 | **PASS** | F6-03 `Confidence` field required. |
| C-03 | **PASS** | Phases 1–5 = competitors, feasibility, market, hypothesis, websearch; Phase 6 = synthesize. All six. |
| C-04 | **PASS** | `F1-01 through F1-03 (inertia) must be populated before F1-04+ (rivals).` FID ordering rule enforces sequence. |
| C-05 | **PASS** | Because block requires FID citations (`because [FID]`). Every claim is pinnable by ID. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Section headers per phase. F-prefixed row structure provides clear hierarchy. |
| C-07 | **PASS** | F6-05 `Counter-evidence: [one risk or caveat — cite the FID it qualifies]` — required and FID-anchored. |
| C-08 | **PASS** | F6-01 `Hypothesis outcome: [Confirmed/Refuted/Inconclusive]` — explicit disposition field. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | F6-04 `Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]` — narrative required and FID-grounded. |
| C-10 | **PASS** | F6-06 `Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]` — conditioned. |
| C-11 | **PASS** | FID-labeled required fields per phase constitute a per-phase schema. Every finding is addressable at the field level. |
| C-12 | **PASS** | `because [FID]` format (e.g., `because F1-01`) is mechanically auditable at a glance. Rubric criterion is defined as "mechanically auditable" and uses "e.g." for example syntax. FID satisfies the definition. *Strict-scorer risk noted: rubric example is Phase+section; FID differs syntactically. Low-to-moderate risk.* |
| C-13 | **FAIL** | Hypothesis is Phase 4. Phases 1–3 (competitors, feasibility, market) execute before the hypothesis is committed. Fails by position. |
| C-14 | **PASS** | Template instructs: `minimum 3 distinct phase prefixes must appear`. Because block has 3 free-form slots. Instruction is explicit; structural enforcement is soft. Scored PASS given the specific prohibition and "minimum 3" language — failure requires active instruction override. |
| C-15 | **PASS** | All fields pre-assigned FIDs (F1-01 through F6-06) throughout the template. Model fills values, cannot skip ID assignment. PASS by construction. |

**Aspirational: 6/7 → 8.57 pts**

**V-03 Composite: 60 + 30 + 8.57 = 98.57 → 98.6 | Gold**
*(Strict C-12 scorer scenario: C-12 FAIL → 5/7 → 97.1)*

---

## V-04 — C-13 + C-14 combined (Phase 0 lock + labeled slots)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase 5 table: `Recommendation` row. |
| C-02 | **PASS** | Phase 5 table: `Confidence` row. |
| C-03 | **PASS** | Phase 0 = hypothesis, Phase 1–3 = competitors/feasibility/market, Phase 4 = websearch, Phase 5 = synthesize. Six domains. |
| C-04 | **PASS** | Phase 1 table: `Inertia rows must precede named rival rows.` Three explicit inertia rows before rival rows. |
| C-05 | **PASS** | Five labeled Because slots with Phase+field citations. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Tables per phase + section headers + Phase 5 summary table. |
| C-07 | **PASS** | `Counter-evidence` row in Phase 5 table. |
| C-08 | **PASS** | `Hypothesis outcome [Confirmed/Refuted/Inconclusive — resolves Phase 0 claim]` row links to Phase 0. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | `Confidence rationale: [name specific evidence gaps or strengths — not just the label]` row. |
| C-10 | **PASS** | `Next step` row conditioned on COMMIT vs. no-build. |
| C-11 | **PASS** | Table-per-phase structure. Each phase has its own named row schema. |
| C-12 | **PASS** | Five Because slots prescribe `because Phase N, [field/row]` syntax. Clean Phase+section format. Zero strict-scorer risk — matches rubric example exactly. |
| C-13 | **PASS** | Phase 0 header: `[PRIOR COMMITMENT — COMPLETE BEFORE SCOUTING]`. Template position precedes all evidence phases. PASS by construction — structural, not instructional. |
| C-14 | **PASS** | Five labeled slots: `PHASE 0 (hypothesis prior)`, `PHASE 1 (competitors)`, `PHASE 2 (feasibility)`, `PHASE 3 (market)`, `PHASE 4 (web evidence)`. All five distinct phases required. PASS by template construction. |
| C-15 | **FAIL** | No FID system. Phase+section citations are clean (C-12 PASS) but individual findings have no unique enumerable key. A cross-section reference like "the status-quo inertia finding from Phase 1" is not pinnable by ID. |

**Aspirational: 6/7 → 8.57 pts**

**V-04 Composite: 60 + 30 + 8.57 = 98.57 → 98.6 | Gold**

---

## V-05 — C-13 + C-14 + C-15 (Phase 0 lock + FID-phase slots — 100-target)

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | F5-02 `Recommendation` field. Required, labeled, position-enforced. |
| C-02 | **PASS** | F5-03 `Confidence` field. Required. |
| C-03 | **PASS** | Phase 0 = prove-hypothesis (F0-01 to F0-05), Phase 1 = competitors, Phase 2 = feasibility, Phase 3 = market, Phase 4 = websearch, Phase 5 = synthesize. All six domains with mandatory fields. |
| C-04 | **PASS** | `Ordering rule: F1-01 through F1-03 (inertia) must be populated before F1-04+ (rivals).` FID ordering enforces inertia-first by number sequence. |
| C-05 | **PASS** | Five FID-labeled Because slots. Every recommendation claim is pinnable to a specific FID. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Section headers per phase + FID-prefixed row hierarchy = consistent document structure. |
| C-07 | **PASS** | F5-05 `Counter-evidence: [one risk or caveat — cite the FID it qualifies]` — required and evidence-anchored. |
| C-08 | **PASS** | F5-01 `Hypothesis outcome: [Confirmed/Refuted/Inconclusive — resolves F0-01]` explicitly links to the Phase 0 claim by FID. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | F5-04 `Confidence rationale: [cite the specific FIDs that drove this rating — not just the label]`. Narrative is FID-grounded — traceability built in. |
| C-10 | **PASS** | F5-06 `Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]` — conditioned. |
| C-11 | **PASS** | Pre-assigned FID rows per phase constitute the strongest per-phase schema possible. Every phase is verifiable at the individual-finding level. |
| C-12 | **PASS** | Because slots prescribe `because F[phase]-[seq]` (e.g., `because F1-01`). Mechanically auditable at a glance. Rubric defines pass as "mechanically auditable" and uses "e.g." — FID satisfies the definition more precisely than Phase+section, not less. *Strict-scorer risk: low-to-moderate (FID differs from rubric's example syntax). Full PASS on liberal reading, which is the appropriate reading given "e.g." and the definition.* |
| C-13 | **PASS** | Phase 0 structurally precedes all evidence phases. `HYPOTHESIS FIRST — Phase 0 must be complete before Phase 1 begins.` F0-01 to F0-05 fields pre-assigned before any evidence FID appears. PASS by template position. |
| C-14 | **PASS** | Five labeled slots require `F0-xx`, `F1-xx`, `F2-xx`, `F3-xx`, `F4-xx` prefixes respectively. All five phase prefixes required by name. PASS by template construction — not instruction. |
| C-15 | **PASS** | All findings pre-assigned FIDs (F0-01 through F5-06) throughout. No in-flight assignment. FIDs are stable identifiers — reordering findings within a phase does not break cross-section references. PASS by construction. |

**Aspirational: 7/7 → 10.0 pts**
*(Strict C-12 scenario: 6/7 → 8.57 → composite 98.6)*

**V-05 Composite: 60 + 30 + 10.0 = 100.0 | Gold**

---

## Ranked Results

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Band |
|------|-----------|-----------|-------------|--------------|-----------|------|
| 1 | **V-05** (Phase 0 + FID-phase slots) | 5/5 | 3/3 | 7/7 | **100.0** | Gold |
| 2 | **V-01** (Phase 0 lock) | 5/5 | 3/3 | 6/7 | **98.6** | Gold |
| 2 | **V-03** (Pre-assigned FIDs) | 5/5 | 3/3 | 6/7 | **98.6** | Gold |
| 2 | **V-04** (Phase 0 + labeled slots) | 5/5 | 3/3 | 6/7 | **98.6** | Gold |
| 5 | **V-02** (Five-phase slots) | 5/5 | 3/3 | 5/7 | **97.1** | Gold |

**Ties at 98.6:** V-01 fails C-15; V-03 fails C-13 (+ has soft C-12 risk); V-04 fails C-15. V-04 is the cleaner 98.6 — no C-12 risk, no instructional C-14 dependency.

**All five variations are Gold** (all essential pass, composite ≥ 80).

---

## Excellence Signals from V-05

**What made V-05 uniquely achieve 100:**

1. **Phase-0-first structural position**: The hypothesis gate works because Phase 0 *is numbered before* Phase 1 — the model has no template structure to fill in Phases 1+ before completing Phase 0. Positional enforcement beats instructional enforcement.

2. **Pre-assigned FIDs eliminate assignment variance**: IDs are baked into the template before the model executes. The model cannot produce a finding without an ID — there's nothing to fill in. In-flight ID assignment allows skipping; pre-assignment removes the option.

3. **Because block does double duty**: Each Because slot requires both a phase label (`PRIOR (Phase 0)`, `COMPETITORS (Phase 1)`) and a specific FID (`because F0-[seq]`). One template structure simultaneously satisfies C-14 (phase breadth) and C-15 (per-finding precision). This is the key structural insight of R3: two aspirational criteria collapsed into one mechanism.

4. **Preamble violations made concrete**: The three-rules preamble explicitly states what failing looks like — `"As shown above" is not` permissible. Not just the rule, but the counter-example. This pattern pre-empts the most common drift.

5. **Schema closure**: Every criterion from C-01 through C-15 has a named structural counterpart in the template. There is no criterion that relies on the model's self-organization — every pass condition is backed by a required field.

---

## New Patterns Identified

**Pattern: Double-duty synthesis block** — Design the Because block to simultaneously satisfy two distinct aspirational criteria (C-14 cross-phase span via labeled slots + C-15 per-finding precision via FID citations). When two criteria can be collapsed into one mechanism, the template becomes more constrained without becoming longer.

**Pattern: Pre-assignment over in-flight assignment** — Assign finding identifiers in the template skeleton before the model executes, not during. Eliminates the variance window where a model under context pressure omits IDs for some findings but not others. Applies to any enumerable schema (FIDs, finding numbers, evidence keys).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Double-duty synthesis block: design the Because block to satisfy two aspirational criteria simultaneously — labeled phase slots for C-14 span breadth plus FID citations for C-15 per-finding precision — collapsing two criteria into one mechanism", "Pre-assignment over in-flight assignment: bake finding identifiers into the template skeleton before the model executes; eliminates the variance window where in-flight ID assignment is skipped under context pressure"]}
```
