## Round 3 Scorecard — `topic-status`

---

### Scoring Approach

Each criterion evaluated against the rubric pass condition. Evidence drawn from the variation text directly.

**Point weights:** C-01–C-04: 15 each (60) | C-05–C-07: 10 each (30) | C-08–C-12: 5 each (25) | C-13–C-16: 5 each (20) | **Max: 135**

---

### V-01: C-13 Isolation — Labeled Ordering Layers

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | `Glob: simulations/**/{topic}-*`; `DISK_SIGNALS = [every returned path]`; zero case: "No signals found on disk. Continue." |
| C-02 | Coverage percentage | PASS | `percent = total_found / total_planned * 100`; consistency check: "GAP LIST non-empty and percent = 100% -> assertion error. Recheck Phase 2." |
| C-03 | Gap identification | PASS | `OPEN GAPS` section in template; named as `{namespace}/{skill} {item-name} ({priority})`; zero-gap case explicit: "No gaps -- all planned signals present." |
| C-04 | Display-only | PASS | "No file is written. No file is modified. Permitted tools: Read, Glob." Phase 4 pre-display gate present. |
| C-05 | Readiness verdict | PASS | `READINESS: {READY | ALMOST READY | NOT READY}` + `Ship risk:` sentence connected to gap list. |
| C-06 | Namespace breakdown | PASS | All 9 rows pre-seeded in table. "Zero row: 0 \| 0 \| --" instruction. |
| C-07 | Strategy cross-reference | PASS | `Signal plan: simulations/{topic}/strategy.md [FOUND | NOT FOUND]` in template; Phase 1.2 names path; missing case: "Signal plan not found -- no planned baseline." |
| C-08 | Recency awareness | PASS | `STALE EVIDENCE (>30 days old)` in template; Phase 3: parse YYYY-MM-DD suffix, age > 30 days = STALE. |
| C-09 | Actionable next step | PASS | `NEXT STEP: Run /{namespace}:{skill} to produce {item-name}. (Highest-priority essential gap. Omit if READY.)` |
| C-10 | Structural completeness | PASS | 9-row table physically pre-seeded in template; "All 9 rows required. Zero row: 0 \| 0 \| --" |
| C-11 | Phase-gated disk-check | PASS | Named phases DISCOVER → ASSERT → COMPUTE → DISPLAY. Phase 4 gate: "has any file been written or modified? YES -> stop." |
| C-12 | Gap-first ordering | PASS | OPEN GAPS before COVERAGE in template. "(This number summarizes the gap list above -- not the other way around.)" |
| C-13 | Triple-redundancy guard | PASS | Three explicitly labeled, structurally distinct layers: **[LAYER 1 -- STRUCTURAL]** (template position, "cannot be changed by execution instruction"), **[LAYER 2 -- SEMANTIC]** (ordering principle, "100% with gaps contradiction failure mode"), **[LAYER 3 -- EXECUTION]** (Phase 4 render order OPEN GAPS → ... → COVERAGE). Phase 4 reinforces all three by label. |
| C-14 | Template-first absorption | PASS | Output template appears before the three-layer block and before execution phases. Template includes 9-row table and OPEN GAPS before COVERAGE. C-10 implied. |
| C-15 | Per-signal assertion chain | PASS | Phase 2: "For each entry P in PLANNED, evaluate exactly one assertion… TRUE -> P.assertion = PRESENT; FALSE -> P.assertion = NOT_PRESENT. Evaluate every P individually. Do not skip any entry." Explicit residual: `GAP LIST = {P : assertion = NOT_PRESENT} [gaps = planned minus PRESENT set]`. |
| C-16 | Consequence-framed verdict | PASS | Template: `Ship risk: … "Committing now means shipping without: {list essential gap item-names}"`. Phase 3 computes the sentence with specific item names. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Aspirational:** 5/5 | **Aspirational-2:** 4/4

**Score: 135 / 135**

---

### V-02: C-15 + C-14 — Assertion Table Pre-Seeded in Template

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | `Glob: simulations/**/{topic}-*`; `DISK = set of every returned path`; zero case: "No signals found on disk. Continue." |
| C-02 | Coverage percentage | PASS | `percent = total_found / total_planned * 100`; consistency: "GAP LIST non-empty and percent = 100% -> assertion table error. Recheck Phase 2." |
| C-03 | Gap identification | PASS | `OPEN GAPS (= NOT_PRESENT rows from assertion table above)` in template; named; zero case: "All assertions return PRESENT. No gaps." |
| C-04 | Display-only | PASS | "No file is written. No file is modified. Permitted tools: Read, Glob. Write and Edit are forbidden." Phase 4 gate present. |
| C-05 | Readiness verdict | PASS | `READINESS: {READY | ALMOST READY | NOT READY}` + `Ship risk:` sentence. |
| C-06 | Namespace breakdown | PASS | 9-row table pre-seeded; "All 9 rows required. Zero row: 0 \| 0 \| --" |
| C-07 | Strategy cross-reference | PASS | Path named in template header and Phase 1.2; missing case handled. |
| C-08 | Recency awareness | PASS | `STALE EVIDENCE (>30 days old)` in template; Phase 3 computes age. |
| C-09 | Actionable next step | PASS | `NEXT STEP: Run /{namespace}:{skill} to produce {item-name}. (Highest-priority NOT_PRESENT essential entry. Omit if READY.)` |
| C-10 | Structural completeness | PASS | 9-row table pre-seeded; "All 9 rows required." |
| C-11 | Phase-gated disk-check | PASS | Named phases LOAD → ASSERT → AGGREGATE → DISPLAY. Phase 4 gate present. |
| C-12 | Gap-first ordering | PASS | OPEN GAPS before COVERAGE in template. Phase 4: "OPEN GAPS before COVERAGE." SECTION ORDER note: "The percentage summarizes the table -- not the other way around." |
| C-13 | Triple-redundancy guard | PASS | Three structurally distinct layers are identifiable: **Structural** (template positions ASSERTION TABLE → OPEN GAPS before COVERAGE), **Semantic** (SECTION ORDER block: "The risk list is not derived from the percentage. Do not reorder. The percentage summarizes the table -- not the other way around."), **Execution** (Phase 4 render order: "ASSERTION TABLE -> OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> ..."). No LAYER labels, but all three mechanism types are present and identifiable at distinct physical locations with distinct functions. |
| C-14 | Template-first absorption | PASS (strong) | Template header explicitly: "placed before execution instructions so the model absorbs the output shape before reading how to produce it." Template includes pre-seeded ASSERTION TABLE format, 9-row table, OPEN GAPS before COVERAGE. Physical placement confirmed before PHASE 1-4. |
| C-15 | Per-signal assertion chain | PASS (strong) | Template pre-seeds ASSERTION TABLE format: "one row per planned signal; mark each individually; Every planned signal receives exactly one mark. No row may be omitted." Phase 2: per-entry `ASSERT: DISK contains a path matching…`, `TRUE -> P.assertion = PRESENT; FALSE -> P.assertion = NOT_PRESENT`. Explicit residual: `GAP LIST = {P : assertion = NOT_PRESENT} [gaps = planned minus PRESENT set]`. C-14+C-15 fused: format enforced at absorption level. |
| C-16 | Consequence-framed verdict | PASS | `Ship risk: … "Committing now means shipping without: {list essential NOT_PRESENT item-names}"`. Names specific items. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Aspirational:** 5/5 | **Aspirational-2:** 4/4

**Score: 135 / 135**

---

### V-03: C-16 — Consequence Saturation (Deep Frame)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | `Glob: simulations/**/{topic}-*`; `EVIDENCE = [every returned path]`; zero: "No evidence gathered yet. Continue." Named variable. |
| C-02 | Coverage percentage | PASS | `percent = total_gathered / total_planned * 100`; consistency: "COMMIT RISK LIST non-empty and percent = 100% -> recheck Phase 2." |
| C-03 | Gap identification | PASS | `COMMIT RISKS (planned evidence not yet gathered)` section in template; named as `{namespace}/{skill} {signal-name} ({priority})`; zero case: "All planned evidence gathered. No commit risks." Section title differs from "OPEN GAPS" but structurally satisfies: a gap section exists, gaps are named, zero case explicit. |
| C-04 | Display-only | PASS | "Terminal output only. No file written. No file modified. Permitted: Read, Glob. Forbidden: Write, Edit." Phase 4 gate present. |
| C-05 | Readiness verdict | PASS | `COMMIT DECISION: {COMMIT / PROCEED WITH CAUTION / DO NOT COMMIT}` + `Consequence:` sentence. Connected to COMMIT RISK LIST. |
| C-06 | Namespace breakdown | PASS | 9-row table pre-seeded (Gathered/Planned/% columns); "All 9 rows required. Zero row: 0 \| 0 \| --" |
| C-07 | Strategy cross-reference | PASS | `Evidence plan: simulations/{topic}/strategy.md [FOUND | NOT FOUND]`; Phase 1.2 names path; missing case: "No evidence plan found -- commit risk cannot be assessed." |
| C-08 | Recency awareness | PASS | `STALE EVIDENCE (>30 days old -- may not reflect current state)` in template; Phase 3 computes age. |
| C-09 | Actionable next step | PASS | `HIGHEST PRIORITY RISK: Run /{namespace}:{skill} to gather {signal-name}. (Omit if COMMIT.)` |
| C-10 | Structural completeness | PASS | 9-row table pre-seeded; "All 9 rows required." |
| C-11 | Phase-gated disk-check | PASS | Named phases SURVEY → IDENTIFY RISKS → COMPUTE → DISPLAY. Phase 4 gate present. |
| C-12 | Gap-first ordering | PASS | COMMIT RISKS before EVIDENCE GATHERED in template. SECTION ORDER block: "COMMIT RISKS appears before EVIDENCE GATHERED. Compute risks first, then derive coverage from them." Phase 4 render order: "COMMIT RISKS -> UNPLANNED -> STALE -> EVIDENCE GATHERED -> ..." |
| C-13 | Triple-redundancy guard | PASS | Three structurally distinct layers present under consequence vocabulary: **Structural** (template: COMMIT RISKS before EVIDENCE GATHERED), **Semantic** (SECTION ORDER block: "The risk list is not derived from the percentage. Compute risks first, then derive coverage from them."), **Execution** (Phase 4 render order). All three mechanism types identifiable at distinct physical locations. |
| C-14 | Template-first absorption | PASS | Output template physically placed before EXECUTION PHASES. Template includes 9-row pre-seeded table; COMMIT RISKS (gap section) before EVIDENCE GATHERED (coverage). C-10 implied. Template header lacks explicit "placed before execution" language but physical positioning satisfies the pass condition. |
| C-15 | Per-signal assertion chain | **FAIL** | Phase 2 loop: "For each P in PLAN: is there a path in EVIDENCE matching…? YES -> GATHERED; NO -> MISSING (commit risk)." Per-signal evaluation is present. **However, the explicit mathematical residual derivation is absent.** No statement of form "COMMIT RISK LIST = planned minus GATHERED SET" or "{P : assertion = NOT_PRESENT}." "COMMIT RISK LIST is now fixed" is not equivalent. The pass condition requires "the gap list is explicitly derived as the NOT_PRESENT set" — this formula is missing. |
| C-16 | Consequence-framed verdict | PASS (strong) | Primary axis. "Committing now means shipping without: {list essential missing signals}" for both PROCEED WITH CAUTION and DO NOT COMMIT cases. Consequence vocabulary saturates entire output (COMMIT RISKS, COMMIT DECISION, HIGHEST PRIORITY RISK). |

**Essential:** 4/4 | **Recommended:** 3/3 | **Aspirational:** 5/5 | **Aspirational-2:** 3/4 (C-15 fails)

**Score: 130 / 135**

---

### V-04: C-13 + C-14 — Template-First Structural Ordering

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | `Glob: simulations/**/{topic}-*`; `DISK_SIGNALS = [every returned path, verbatim]`; zero case handled. |
| C-02 | Coverage percentage | PASS | `percent = total_found / total_planned * 100`; consistency check present. |
| C-03 | Gap identification | PASS | `OPEN GAPS` section in template; named items; zero case explicit. |
| C-04 | Display-only | PASS | "Terminal output only. No file written." Phase 4 gate present. |
| C-05 | Readiness verdict | PASS | `READINESS: {READY | ALMOST READY | NOT READY}` + `Ship risk:` sentence. |
| C-06 | Namespace breakdown | PASS | 9-row pre-seeded table; "All 9 rows required. Zero row: 0 \| 0 \| --" |
| C-07 | Strategy cross-reference | PASS | Path in template + Phase 1.2; missing case handled. |
| C-08 | Recency awareness | PASS | `STALE EVIDENCE (>30 days old)` in template; Phase 3 age computation. |
| C-09 | Actionable next step | PASS | `NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.` |
| C-10 | Structural completeness | PASS | 9-row table pre-seeded; "All 9 rows required." |
| C-11 | Phase-gated disk-check | PASS | Named phases DISCOVER → ASSERT → COMPUTE → DISPLAY. Phase 4 gate present. |
| C-12 | Gap-first ordering | PASS | OPEN GAPS before COVERAGE in template. Phase 4: "Coverage summarizes the gap list [LAYER 2]." |
| C-13 | Triple-redundancy guard | PASS | Three explicitly labeled layers: **[LAYER 1 -- STRUCTURAL]** (template position, "enforced by physical placement — it cannot be changed by an execution instruction without rewriting the template itself"), **[LAYER 2 -- SEMANTIC]** ("gap list must be enumerated first because coverage is its complement… creates the '100% with gaps' contradiction failure mode"), **[LAYER 3 -- EXECUTION]** (Phase 4 render order OPEN GAPS → COVERAGE; "Any deviation from this sequence is a structural error"). Phase 4 reinforces with label references. |
| C-14 | Template-first absorption | PASS (strong) | Template header: "placed before execution instructions so the model absorbs the output shape (section order, 9-row table, gap-first ordering) before reading how to produce it." Template includes 9-row table and OPEN GAPS before COVERAGE. Physical placement confirmed. |
| C-15 | Per-signal assertion chain | PASS | Phase 2: per-entry `ASSERT: DISK_SIGNALS contains a path matching…; TRUE -> P.assertion = PRESENT; FALSE -> P.assertion = NOT_PRESENT`. Explicit residual: `GAP LIST = {P : assertion = NOT_PRESENT} [gaps = planned minus PRESENT set]`. "GAP LIST is now fixed. Do not revise in Phase 3 or 4." |
| C-16 | Consequence-framed verdict | PASS | `Ship risk: … "Committing now means shipping without: {list essential gap item-names}"`. Names specific items. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Aspirational:** 5/5 | **Aspirational-2:** 4/4

**Score: 135 / 135**

---

### V-05: Full Synthesis — Targeting 135/135

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | PASS | `Glob: simulations/**/{topic}-*`; `DISK = set of every returned path. Fixed.`; zero case: "No signals found on disk." |
| C-02 | Coverage percentage | PASS | `percent = total_found / total_planned * 100`; template note: "If OPEN GAPS is non-empty, percent < 100%. If these contradict, recheck the assertion table." |
| C-03 | Gap identification | PASS | `OPEN GAPS (= rows where NOT_PRESENT is marked in the assertion table above)`; named items; zero case: "All assertions return PRESENT. No gaps." |
| C-04 | Display-only | PASS | "No file is written. No file is modified. Permitted tools: Read, Glob." Phase 4 gate: "has any file been written or modified? YES -> stop." |
| C-05 | Readiness verdict | PASS | `READINESS: {READY | ALMOST READY | NOT READY}` + `Ship risk:` sentence connected to gap list. |
| C-06 | Namespace breakdown | PASS | 9-row table pre-seeded; "All 9 rows required. Zero row: 0 \| 0 \| --" |
| C-07 | Strategy cross-reference | PASS | Path in template + Phase 1.2; missing case: "Signal plan not found -- assertion baseline is empty. Do not silently compute against zero." |
| C-08 | Recency awareness | PASS | `STALE EVIDENCE (>30 days old)` in template; Phase 3: "Age = today minus date. > 30 days = STALE, record age in days." |
| C-09 | Actionable next step | PASS | `NEXT STEP: Run /{namespace}:{skill} to produce {item-name}. (Highest-priority essential NOT_PRESENT entry. Omit if READY.)` |
| C-10 | Structural completeness | PASS | 9-row table pre-seeded in template with all 9 namespaces. "All 9 rows required. Zero row: 0 \| 0 \| --" |
| C-11 | Phase-gated disk-check | PASS | Named phases DISCOVER → ASSERT → COMPUTE → DISPLAY. Phase 4 gate present with "SKILL FAILED: disk write detected" consequence. |
| C-12 | Gap-first ordering | PASS | ASSERTION TABLE → OPEN GAPS → COVERAGE order in template. Template note: "(Derived from PRESENT marks… If OPEN GAPS is non-empty, percent < 100%.)". Phase 4 [LAYER 2] reference. |
| C-13 | Triple-redundancy guard | PASS | Three explicitly labeled, maximally distinct layers: **[LAYER 1 -- STRUCTURAL]** ("ASSERTION TABLE and OPEN GAPS sections positioned before COVERAGE… enforced by physical placement: execution instructions cannot reorder template sections without rewriting the template itself"), **[LAYER 2 -- SEMANTIC]** ("Gaps must be enumerated first because coverage is their mathematical complement. 'The coverage number summarizes the gap list — not the other way around.'"), **[LAYER 3 -- EXECUTION]** (Phase 4 render order ASSERTION TABLE → OPEN GAPS → ... → COVERAGE). Phase 4 references all three by label. Strongest expression of this criterion. |
| C-14 | Template-first absorption | PASS (strongest) | Template header: "placed BEFORE execution instructions so the model absorbs the output shape (section order, assertion format, 9 namespace rows) before reading how to produce it." Template includes pre-seeded ASSERTION TABLE format, 9-row table, OPEN GAPS before COVERAGE. Explicit absorption intent stated. |
| C-15 | Per-signal assertion chain | PASS (strongest) | Template pre-seeds ASSERTION TABLE: "fill one row per planned signal; mark PRESENT or NOT_PRESENT; Every planned signal receives exactly one mark. No row may be omitted." Phase 2: per-entry `ASSERT: DISK contains a path matching…; TRUE -> P.assertion = PRESENT; FALSE -> P.assertion = NOT_PRESENT. Do not skip any entry.` Explicit residual: `GAP LIST = {P : assertion = NOT_PRESENT} [gaps = planned minus PRESENT set]`. C-14+C-15 fused: model must evaluate each signal individually to fill the assertion table. Structural enforcement at absorption level. |
| C-16 | Consequence-framed verdict | PASS | `Ship risk: … "Committing now means shipping without: {list essential NOT_PRESENT item-names}"`. Names specific items. Template and Phase 3 both carry the sentence. |

**Essential:** 4/4 | **Recommended:** 3/3 | **Aspirational:** 5/5 | **Aspirational-2:** 4/4

**Score: 135 / 135**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Asp (C-08–C-12) | Asp-2 (C-13–C-16) | Score | All Essential? |
|------|-----------|-----------|-------------|------------------|-------------------|-------|----------------|
| 1 | V-01 C-13 Labeled Layers | 4/4 | 3/3 | 5/5 | 4/4 | **135** | YES |
| 1 | V-02 Assertion Table in Template | 4/4 | 3/3 | 5/5 | 4/4 | **135** | YES |
| 1 | V-04 Template-First + Labeled Layers | 4/4 | 3/3 | 5/5 | 4/4 | **135** | YES |
| 1 | V-05 Full Synthesis | 4/4 | 3/3 | 5/5 | 4/4 | **135** | YES |
| 5 | V-03 Consequence Saturation | 4/4 | 3/3 | 5/5 | 3/4 | **130** | YES |

**Predicted vs. actual divergence:**

| Prediction | Outcome | Analysis |
|------------|---------|----------|
| V-01 = 130 (C-14 expected partial) | **V-01 = 135** | C-14 passes for V-01 — template IS physically before execution phases; pass condition is positional, not about explicit "placed before" language in the header |
| V-02 C-13 = NO | **V-02 C-13 = PASS** | Three mechanism types are present and identifiable without explicit LAYER labels: template position (structural), SECTION ORDER block (semantic), Phase 4 render order (execution). Identifiability ≠ labeling. |
| V-03 C-14 = NO | **V-03 C-14 = PASS** | Template physically precedes execution phases; includes 9-row table and gap section before coverage. C-14 pass condition is positional — satisfied. |
| V-03 C-15 = NO | **V-03 C-15 = FAIL (confirmed)** | Loop uses GATHERED/MISSING vocabulary but omits explicit residual derivation formula. "COMMIT RISK LIST is now fixed" ≠ "gaps = planned minus PRESENT set." |
| V-04 = 132 | **V-04 = 135** | All criteria pass; no criterion was missed. |
| V-05 = 135 | **V-05 = 135 (confirmed)** | All four Tier-2 criteria at maximum structural strength. |

---

## Excellence Signals

### E-1: C-15 residual derivation formula is load-bearing — not the loop

V-03's Phase 2 loop IS per-signal evaluation (every P evaluated individually, GATHERED/MISSING verdict). But C-15 requires the gap list to be "explicitly derived as the NOT_PRESENT set." The formula `GAP LIST = {P : assertion = NOT_PRESENT} [gaps = planned minus PRESENT set]` in V-01/V-02/V-04/V-05 is not cosmetic — it is the explicit mathematical residual statement the criterion requires. Vocabulary substitution (COMMIT RISK LIST, MISSING) without the residual formula fails C-15 regardless of how correct the per-signal loop is.

### E-2: C-13 identifiability does not require explicit LAYER labels

V-02 passes C-13 without [LAYER N] labels. The three mechanism types — template position (structural), semantic note block, execution render sequence in Phase 4 — exist in structurally distinct physical locations serving structurally distinct functions. The labels in V-01/V-04/V-05 strengthen scorecard confidence and remove ambiguity, but they are not the mechanism itself. C-13 fails only when a mechanism type is genuinely absent, not when it is merely unlabeled.

### E-3: C-14+C-15 fusion via pre-seeded assertion table (V-02, V-05) is the tightest per-signal enforcement

Pre-seeding the ASSERTION TABLE format in the output template forces per-signal evaluation at model absorption time — the model must evaluate each signal to fill each row in the table, rather than following an instruction to do so. This is a stronger structural guarantee than instruction-only enforcement. V-02 and V-05 achieve C-15 compliance that cannot be bypassed by a model that follows the template shape but ignores execution-phase phrasing.

---

## Prediction Divergence Summary

The predictions underestimated C-13's resilience (three variations predicted NO or partial; all pass) and underestimated C-14 coverage (V-03 predicted NO; passes). The only confirmed prediction is C-15 failure in V-03. The R3 floor is now fully stable: all 16 criteria pass for four of five variations. The sole discriminating criterion is C-15, and the discriminating mechanism is the explicit residual derivation formula.

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["C-15 residual derivation formula is load-bearing: per-signal evaluation without an explicit 'gaps = planned minus present' formula fails the criterion even when the loop itself is correctly per-signal; vocabulary substitution (GATHERED/MISSING) that omits this formula is a structural gap not a cosmetic one", "C-13 identifiability does not require explicit LAYER labels: three structurally distinct mechanism types (template position, semantic note block, execution render sequence) satisfy the identifiability requirement when they appear in distinct physical locations serving distinct functions; labeling strengthens confidence but is not the mechanism"]}
```
