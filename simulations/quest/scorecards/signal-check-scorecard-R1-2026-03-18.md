---

## Signal-Check R1 Scoring Results

**All 5 variations cleared gold.** Top score: **100** (V-04 and V-05 tied).

### Criterion Matrix Summary

| V | Essential (5) | Recommended (3) | Aspirational (2) | Composite | Gold |
|---|---------------|-----------------|------------------|-----------|------|
| V-01 | 5/5 | 3/3 | 1/2 | **95** | YES |
| V-02 | 5/5 | 3/3 | 1/2 | **95** | YES |
| V-03 | 5/5 | 3/3 | 1/2 | **95** | YES |
| V-04 | 5/5 | 3/3 | 2/2 | **100** | YES |
| V-05 | 5/5 | 3/3 | 2/2 | **100** | YES |

**Sole differentiator**: C-10 (missing signals by namespace + skill). V-01/V-02/V-03 fail C-10 — they prompt for skill names but don't require the `/namespace:skill` format contractually. V-04/V-05 pass via the `MISSING SIGNAL GUIDE` section.

### Key Findings

1. **Scores exceeded design estimates by 7–21 points.** Design notes expected V-01 at 74–88, V-02 at 70–82. Actual: 95 for all three singles. The estimates anticipated runtime prose drift; at design level each axis has explicit prohibitions ("silence does not pass", "do not assert order without dates") that satisfy the rubric criteria.

2. **All three axes independently satisfy C-01 through C-09.** The combination variations don't improve essential or recommended coverage — they only add C-10. The research axes (status tags, CAUSAL GAP-first, coaching scaffold) matter for runtime reliability but are equivalent at design level.

3. **C-10 is a format contract, not a depth criterion.** V-01 knows about skills ("which discover skill would close this gap?") but doesn't enforce the `/namespace:skill` format. One MISSING SIGNAL GUIDE section closes C-07 and C-10 simultaneously.

**Recommended for golden**: V-04. Full coverage at minimum overhead.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-10 is a format threshold not a depth threshold...", "Single-axis scores exceeded estimates by 7-21 points...", "CAUSAL GAP-first, status tags, and coaching scaffold are rubric-equivalent for C-01 through C-09..."]}
```
V-02 PASS**: "Cite artifact names and dates." + "If no discovery artifacts exist: state this explicitly -- do not assert an order." Explicit prohibition on orderless assertion. Weaker structural enforcement (no Basis: field) but clear negative instruction.
- **V-03 PASS**: "Name the artifacts and their dates. Do not assert an order without citing dates." Same prohibition form as V-02, embedded in the preflight item.
- **V-04/V-05 PASS**: STATUS/Basis/Finding structure with `Basis: [artifact names and dates compared]` and `Finding: [state the order the dates show; no assertion without dates]`. Strongest structural form.

### C-04 — CAUSAL GAP states mechanism or absence

- **V-01 PASS**: `Finding: [does any artifact name the causal chain? If yes, cite it. If no, state explicitly: "no mechanism evidence found -- the gap is open."]` Silence is structurally prohibited by the required Finding field.
- **V-02 PASS**: "Report one of two things -- and be explicit: (a) or (b). Silence on mechanism does not pass this section." Direct prohibition. CAUSAL GAP is the first dimension analyzed, preventing the trailing-analysis silence pattern.
- **V-03 PASS**: "State clearly either: (a) 'Mechanism evidence found...' (b) 'No mechanism evidence found. The causal gap is open.' Do not leave this item blank or hedge with 'mechanism may be implied.'" Explicit negative case named.
- **V-04/V-05 PASS**: `Finding: [one of two explicit statements: (a) or (b). Silence does not pass.]` STATUS field forces a discrete conclusion. CAUSAL GAP-first order preserves the anti-silence effect.

### C-09 — Cross-dimension patterns named

All PASS. Every variation includes a dedicated cross-dimension section. V-01: `=== STEP 3: CROSS-DIMENSION PATTERNS ===`. V-02: `=== CROSS-DIMENSION PATTERNS ===`. V-03: `=== PATTERNS ===`. V-04: `=== CROSS-DIMENSION PATTERNS ===` with two named examples. V-05: `=== CROSS-ITEM PATTERNS ===` with three worked examples. All provide explicit instruction to name shared roots or declare none found.

### C-10 — Missing signals identified by namespace + skill

- **V-01 FAIL**: CAUSAL GAP Action says "which discover skill would close this gap?" — skill name prompted but not namespace:skill format. STALENESS Action says "which skill would produce the refresh?" — vague. No dedicated MISSING SIGNAL GUIDE section. The format `/namespace:skill` is not required.
- **V-02 FAIL**: CAUSAL GAP cites example `/discover-causal` but inconsistently. NEXT ACTIONS says "name a concrete next step" without requiring namespace:skill form. No structured guide for all dimensions.
- **V-03 FAIL**: "What you can do: name the skill that would close it (e.g., /discover-causal)." Per-item guidance but no namespace:skill format requirement. No MISSING SIGNAL GUIDE.
- **V-04 PASS**: `=== MISSING SIGNAL GUIDE ===` requires "name the specific skill (by namespace and skill name) that would close the gap. One line per gap: [Dimension] gap: run /[namespace]:[skill] to [what it produces]." Format enforced structurally.
- **V-05 PASS**: Same MISSING SIGNAL GUIDE with explicit examples: `CAUSAL GAP open: run /discover:causal -- produces mechanism evidence`. Format and skill catalog awareness both present.

---

## Composite Scores

Formula: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/2 × 10)`

| V | Essential | Recommended | Aspirational | **Composite** | Gold? |
|---|-----------|-------------|--------------|---------------|-------|
| V-01 | 60 (5/5) | 30 (3/3) | 5 (1/2) | **95** | YES |
| V-02 | 60 (5/5) | 30 (3/3) | 5 (1/2) | **95** | YES |
| V-03 | 60 (5/5) | 30 (3/3) | 5 (1/2) | **95** | YES |
| **V-04** | **60 (5/5)** | **30 (3/3)** | **10 (2/2)** | **100** | **YES** |
| **V-05** | **60 (5/5)** | **30 (3/3)** | **10 (2/2)** | **100** | **YES** |

**Ranking**: V-04 = V-05 > V-01 = V-02 = V-03

**Recommended for golden**: **V-04** — full criterion coverage at minimum overhead. The MISSING SIGNAL GUIDE section is the only structural addition over V-01/V-02/V-03 that changes the score. Coaching scaffold (V-03) does not add rubric coverage beyond V-01/V-02; V-04's combination of status tags + CAUSAL GAP first + MISSING SIGNAL GUIDE closes all 10 criteria without the additional prose of V-05's preflight metaphor.

---

## Research Question Verdicts

**RQ1: Do status tags (V-01) close C-02/C-03 failures better than prose instruction alone?**
Inconclusive at design level. V-01 (status tags) and V-02/V-03 (prose) all score 5/5 essential including C-02 and C-03. The structural Basis: field in V-01 provides stronger grounding guarantees than prose instruction, but both forms satisfy the rubric criterion as designed. Runtime experiment needed to confirm whether prose-only instructions drift on C-02/C-03 under minimal artifact inventories.

**RQ2: Does CAUSAL GAP-first order (V-02) close the C-04 silence pattern?**
C-04 passes for all five variations. CAUSAL GAP-first (V-02/V-04/V-05) provides a stronger anti-silence guarantee structurally, but V-01/V-03 (CAUSAL GAP last) also satisfy C-04 through explicit "silence does not pass" prohibitions. The ordering axis is not the decisive criterion for design-level compliance.

**RQ3: Does coaching scaffold (V-03) produce C-05 compliance more reliably than a stated instruction?**
V-03 achieves C-05 PASS, as do V-01 and V-02 with simpler register instructions. The "What you can do:" structural slot in V-03 enforces advisory framing more redundantly than the preamble instructions in V-01/V-02, but C-05 passes for all three at the rubric level.

**Key finding:** All three axes independently satisfy C-01 through C-09, exceeding design estimates by 7-21 points. The sole differentiator is C-10 — which requires a dedicated MISSING SIGNAL GUIDE section with explicit namespace:skill format. No single-axis variation includes this section. V-04 and V-05 pass C-10 via the MISSING SIGNAL GUIDE.

---

## Excellence Signals

### EX-01: C-10 is a format threshold, not a depth threshold

C-10 fails for V-01/V-02/V-03 not because the prompts are weaker on depth but because the namespace:skill identification format is absent as a structural requirement. V-01's Action fields prompt for "which discover skill would close this gap?" — skill awareness is present, but the `/namespace:skill` format is not required. V-04's MISSING SIGNAL GUIDE introduces format enforcement: "run /[namespace]:[skill]" as a required string template. The distinction is not whether the model knows the skill catalog but whether the output format is contractually specified. C-10 is a formatting contract, not a depth criterion.

### EX-02: MISSING SIGNAL GUIDE closes C-07 and C-10 simultaneously

V-01 satisfies C-07 via per-dimension Action fields. V-02 satisfies C-07 via a dedicated NEXT ACTIONS section. V-04's MISSING SIGNAL GUIDE provides a third, stronger mechanism: a final collation pass that lists every FLAG or OPEN dimension with the specific skill to run. Because the guide is structured as one-line-per-gap, it is both a C-07 mechanism (next action required) and a C-10 mechanism (namespace + skill name required). Adding the section upgrades C-07 from instructed compliance to structurally redundant compliance -- the Action field and the guide both require an action, making omission a visible structural gap.

### EX-03: Single-axis scores exceeded design estimates by 7-21 points

Design notes estimated V-01 at 74-88, V-02 at 70-82, V-03 at 72-85. Actual scores: 95 for all three. The gap traces to: (a) C-09 passes for all variations -- its dedicated cross-dimension section is present in each but was estimated as uncertain; (b) C-08 passes for all variations -- the "draft last, position first" instruction satisfies the readiness-summary criterion at design level in all three. The design estimates anticipated runtime compliance failures; the design-level rubric reveals that all three single-axis variations are structurally complete through C-09, with only C-10 missing.

---

## R2 Direction

The rubric is saturated at v1 -- V-04 and V-05 both score 100, no criterion differentiates them at the design level.

**R2 candidates:**

1. **Runtime compliance experiment**: run V-01 and V-04 against a single-artifact topic and a zero-artifact topic. Measure whether prose form (V-01) drifts on C-02/C-03 while structural form (V-04) holds. Directly tests RQ1 against ground-truth inventory conditions.
2. **C-11 — Zero-artifact graceful handling**: introduce a criterion requiring the prompt to produce a named stop message when Glob returns no results, rather than proceeding with OPEN status on all dimensions. V-04 says "If no artifacts found: stop." but does not specify what the stop message must contain.
3. **C-12 — Frontmatter field completeness**: require all declared frontmatter fields to be populated with correct value types in the output artifact. V-04/V-05 both declare richer frontmatter (`missing_signals_by_skill`, `open_dimensions`) -- runtime compliance closes the ARCHITECTURE-to-output binding.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-10 is a format threshold, not a depth threshold: single-axis variations (V-01/V-02/V-03) score 95 by satisfying C-01 through C-09 but fail C-10 because the namespace:skill format is absent as a contractual requirement -- not because skill awareness is missing. The MISSING SIGNAL GUIDE section introduces format enforcement (/namespace:skill template) that closes C-07 and C-10 simultaneously. The sole differentiator between 95 and 100 is one dedicated collation section.", "All three single-axis variations independently satisfy all essential and recommended criteria plus C-09, exceeding design estimates by 7-21 points. The estimates anticipated runtime prose drift; at design level each axis contains explicit prohibitions (do not assert order without dates, silence does not pass, mechanism may not be implied) and structural slots that close each criterion. C-09 passes for all variations because every prompt includes a dedicated cross-dimension section -- the axis-level isolation design underestimated how universally this section was adopted.", "CAUSAL GAP-first order, status-tagged format, and coaching scaffold are equivalent rubric performers for C-01 through C-09. None of the three research axes produces a criterion failure at the design level. The three axes matter for runtime reliability -- structural enforcement (status tags) vs. prose compliance risk vs. register activation -- but the rubric v1 does not distinguish runtime reliability from design completeness. A runtime experiment scoring C-02 and C-03 compliance against minimal artifact inventories would resolve RQ1 and RQ2 empirically."]}
```
