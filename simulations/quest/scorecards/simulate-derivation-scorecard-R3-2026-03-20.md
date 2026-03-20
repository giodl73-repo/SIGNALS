## simulate-derivation R3 Scorecard

**Top score: 127/130 (V-05) -- Exemplary**
**All essential pass: YES**

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | V-05 (all three + C-07 fix) | 127/130 | Exemplary |
| 2 | V-04 (C-14 + C-16) | 120/130 | Exemplary |
| 3 | V-01 (C-14 only) | 115/130 | Exemplary |
| 4 | V-02 (C-15 only) | 113/130 | Exemplary |
| 4 | V-03 (C-16 only) | 113/130 | Exemplary |

**All four R3 target criteria solved.** C-14, C-15, C-16, and C-07 all reach full score in the variations that target them. The ceiling moved from 110/130 (R2 base in v3 terms) to 127/130.

**Single residual gap:** C-08 (7/10) across all variations -- EXACT/PHYSICAL justifications not mirrored in Phase 2 block template. R4 target; fix expected to push ceiling to 130/130.

**Three new excellence signals:**
1. **Source-removal recovery path** -- "If NO: replace (b)" is a mandatory self-correction at generation time; paraphrase cannot be recorded as SOUND
2. **Pre-phase gateway table** -- unconditional ACTIVE/ABSENT gate before Phase 2 prevents silent axis degradation
3. **Severity-priority ordering in Amend** -- P1-first rule makes fault triage structural, closing the C-07 residual gap from all R2 variations

```json
{"top_score": 127, "all_essential_pass": true, "new_patterns": ["source-removal recovery path closes paraphrase escape: If NO replace-b instruction forces self-correction at generation time; LLM cannot record SOUND verdict after producing a paraphrase -- recovery is mandatory not optional", "pre-phase axis-commitment gateway table prevents silent degradation: unconditional Do NOT proceed gate before Phase 2 forces explicit ACTIVE assertion on all three structural axes; commitment device that cannot be passively satisfied", "severity-priority ordering in Amend makes fault triage structural: P1-first rule converts Amend from free-pick-3 citation list to severity-ordered structure; resolves C-07 residual gap from all R2 variations without changing the citation format"]}
```
 | 12/12 | Phase 3 with P1/P2/P3 and NEW tagging |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and all required fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section with SOUND/CONDITIONALLY SOUND/BROKEN table |
| C-07 Amend maps to faults | PARTIAL | 8/10 | [F-ID] [P1/P2/P3] format present; no P1/P2 priority ordering rule -- same gap as R2 |
| C-08 Step types classified | PARTIAL | 7/10 | APPROX sub-block rich; EXACT/PHYSICAL justifications still under-specified -- not targeted by V-01 |
| C-09 Catches fault not in paper | PASS | 5/5 | Source acknowledgment gate for WEAK/BROKEN + Phase 3 NEW tagging |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b with S-NNa/S-NNb notation and "(interpolated)" label |
| C-11 APPROX verified independently (prose) | PASS | 5/5 | "Do not paraphrase the source sentence; ground the statement in domain knowledge" + source-removal recovery instruction -- strongest C-11 signal |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] format in all three Amend slots |
| C-13 Verification blocks contain prose | PASS | 5/5 | Reasoning rule "YES -- [sentence] / NO -- [sentence]" applies to all checks |
| C-14 APPROX reasoning independent of source | PASS | 5/5 | Source-removal test explicit; "If NO: replace (b) with domain-principle-grounded statement" recovery path closes the paraphrase escape route |
| C-15 All axes stack without phase-dropping | FAIL | 0/5 | No axis-commitment checkpoint table; silent degradation risk -- C-15 rewards full integration only |
| C-16 Prose density uniform across block types | FAIL | 0/5 | No per-block density uniformity rule; APPROX sub-block richly specified, primary checks not constrained to match |

**V-01 Total: 115 / 130 -- Exemplary**

---

### V-02 -- Axis-Stacking Self-Check

**Axis**: Three-row completion checkpoint table after Phase 1b -- axes A/B/C must all show ACTIVE before Phase 2

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table unchanged |
| C-02 Verification block per step | PASS | 12/12 | Full Phase 2 block template; checkpoint commits to covering all S-IDs |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block present in block template |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3 and NEW tagging |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and required fields specified |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | [F-ID] [P1/P2/P3] format; no P1/P2 priority ordering rule |
| C-08 Step types classified | PARTIAL | 7/10 | Not targeted; EXACT/PHYSICAL under-specified |
| C-09 Catches fault not in paper | PASS | 5/5 | Source acknowledgment gate + Phase 3 NEW tagging (Axis C in checkpoint) |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b present (Axis A in checkpoint) |
| C-11 APPROX verified independently (prose) | PARTIAL | 3/5 | (b) says "state the validity condition in the tracer's own words -- e.g., valid when kT << E_gap"; no domain-principle grounding instruction; "own words" alone permits paraphrase |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend format |
| C-13 Verification blocks contain prose | PASS | 5/5 | Reasoning rule "YES -- [sentence]" applies to all checks; Axis B in checkpoint commits to this |
| C-14 APPROX reasoning independent of source | FAIL | 0/5 | No source-removal test; (b) is "own words" only -- does not distinguish paraphrase from independent domain reasoning |
| C-15 All axes stack without phase-dropping | PASS | 5/5 | Checkpoint table forces explicit ACTIVE/ABSENT assertion on all three axes before Phase 2; "Do NOT proceed to Phase 2 until all three show ACTIVE" is an unconditional gate -- commitment device prevents silent degradation |
| C-16 Prose density uniform across block types | FAIL | 0/5 | No per-block density uniformity rule; APPROX sub-block and primary checks may diverge in density within one block |

**V-02 Total: 113 / 130 -- Exemplary**

---

### V-03 -- Uniform Prose Density Rule

**Axis**: Density uniformity rule added to Phase 2 preamble -- APPROX prose richness requires matching prose in primary checks of the same block

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table unchanged |
| C-02 Verification block per step | PASS | 12/12 | Full Phase 2 block template |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block present |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3 and NEW tagging |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and required fields |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | [F-ID] [P1/P2/P3] format; no P1/P2 priority rule |
| C-08 Step types classified | PARTIAL | 7/10 | Not targeted; same partial as R2 |
| C-09 Catches fault not in paper | PASS | 5/5 | Source acknowledgment gate + Phase 3 NEW tagging |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b present |
| C-11 APPROX verified independently (prose) | PARTIAL | 3/5 | Same weak (b) phrasing as V-02 -- "own words" without domain-principle grounding; density uniformity rule does not fix the independence gate |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend |
| C-13 Verification blocks contain prose | PASS | 5/5 | Reasoning rule present; density uniformity rule reinforces it for APPROX-containing blocks |
| C-14 APPROX reasoning independent of source | FAIL | 0/5 | No source-removal test; same gap as V-02 |
| C-15 All axes stack without phase-dropping | FAIL | 0/5 | No axis-commitment checkpoint; silent degradation risk persists |
| C-16 Prose density uniform across block types | PASS | 5/5 | "Density uniformity rule -- per step block: Within any single step block, prose density must be uniform across the APPROX sub-block and the three primary checks... Mixed density within a single step block -- rich APPROX prose alongside bare primary checks, or vice versa -- fails this rule." Explicit, per-block, bidirectional |

**V-03 Total: 113 / 130 -- Exemplary**

---

### V-04 -- Combined: Independence Gate + Uniform Density

**Axes**: V-01 (source-removal test for C-14) + V-03 (density uniformity rule for C-16)

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table unchanged |
| C-02 Verification block per step | PASS | 12/12 | Full Phase 2 block template |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block with source-removal test + (c)/(d) |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3 and NEW tagging |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and required fields |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PARTIAL | 8/10 | [F-ID] [P1/P2/P3] format; no P1/P2 priority rule -- residual gap not addressed |
| C-08 Step types classified | PARTIAL | 7/10 | Not targeted; EXACT/PHYSICAL still under-specified |
| C-09 Catches fault not in paper | PASS | 5/5 | Source acknowledgment gate + Phase 3 NEW tagging |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b with S-NNa/S-NNb and "(interpolated)" label |
| C-11 APPROX verified independently (prose) | PASS | 5/5 | "Do not paraphrase the source sentence; ground the statement in domain knowledge" + source-removal recovery; density uniformity rule lifts primary check prose to match APPROX richness |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend |
| C-13 Verification blocks contain prose | PASS | 5/5 | Reasoning rule present; density uniformity rule enforces parity between APPROX and primary checks |
| C-14 APPROX reasoning independent of source | PASS | 5/5 | Source-removal test explicit; "If NO: replace (b) with domain-principle-grounded statement" recovery path |
| C-15 All axes stack without phase-dropping | FAIL | 0/5 | No axis-commitment checkpoint; all three axes present but no explicit gate preventing silent degradation -- C-15 is strict binary |
| C-16 Prose density uniform across block types | PASS | 5/5 | Density uniformity rule in Phase 2 preamble; per-block constraint with bidirectional enforcement |

**V-04 Total: 120 / 130 -- Exemplary**

---

### V-05 -- Full Ceiling: All Three R3 Axes + C-07 Priority Fix

**Axes**: V-01 (independence gate) + V-02 (axis-stacking check) + V-03 (density uniformity) + C-07 P1/P2 priority rule in Phase 4

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 Derivation map complete | PASS | 12/12 | Phase 1 table unchanged |
| C-02 Verification block per step | PASS | 12/12 | Full Phase 2 block template; checkpoint commits to covering all S-IDs including interpolated |
| C-03 Every APPROX flagged | PASS | 12/12 | APPROX sub-block with source-removal test, domain-principle grounding, and (c)/(d) |
| C-04 Fault register present | PASS | 12/12 | Phase 3 with P1/P2/P3 and NEW tagging |
| C-05 Artifact frontmatter | PASS | 12/12 | Write path and required fields |
| C-06 Global soundness verdict | PASS | 10/10 | Phase 4 summary section |
| C-07 Amend maps to faults | PASS | 10/10 | [F-ID] [P1/P2/P3] format + explicit priority rule: "if P1 faults exist, your first fix must address a P1 fault. If no P1 faults exist but P2 faults exist, at least one fix must address a P2 fault." Residual R2 gap fully closed |
| C-08 Step types classified | PARTIAL | 7/10 | Not targeted in R3; EXACT/PHYSICAL justification still under-specified -- single remaining structural gap across all variations |
| C-09 Catches fault not in paper | PASS | 5/5 | Source acknowledgment gate for WEAK/BROKEN + Phase 3 NEW tagging |
| C-10 Expands compressed steps | PASS | 5/5 | Phase 1b with S-NNa/S-NNb and "(interpolated)" label (Axis A in checkpoint) |
| C-11 APPROX verified independently (prose) | PASS | 5/5 | "Do not paraphrase the source sentence; ground the statement in domain knowledge" + source-removal recovery + density uniformity rule lifts all primary checks to match |
| C-12 Severity labels inline in Amend | PASS | 5/5 | [F-ID] [P1/P2/P3] in Amend; now combined with priority ordering -- severity visible at triage point |
| C-13 Verification blocks contain prose | PASS | 5/5 | Reasoning rule present (Axis B in checkpoint); density uniformity rule enforces parity |
| C-14 APPROX reasoning independent of source | PASS | 5/5 | Source-removal test + recovery instruction: LLM must replace paraphrase before recording verdict; cannot passively satisfy (b) |
| C-15 All axes stack without phase-dropping | PASS | 5/5 | Checkpoint table gates Phase 2 entry; "Do NOT proceed to Phase 2 until all three show ACTIVE" is unconditional; all three axes committed before any verification block is written |
| C-16 Prose density uniform across block types | PASS | 5/5 | Density uniformity rule in Phase 2 preamble; bidirectional per-block constraint closes the token-budget leak |

**V-05 Total: 127 / 130 -- Exemplary**

---

## Ranking

| Rank | Variation | Score | All Essential Pass? | Band | Notes |
|------|-----------|-------|---------------------|------|-------|
| 1 | **V-05** | **127/130** | YES | Exemplary | Ceiling test held; all four R3 gaps closed; C-08 (3 pts) is the only residual gap |
| 2 | **V-04** | **120/130** | YES | Exemplary | C-14 + C-16 recovered; C-15 absent costs 5 pts, C-07 residual costs 2 pts |
| 3 | **V-01** | **115/130** | YES | Exemplary | C-14 recovered; C-15 and C-16 absent |
| 4 | **V-02** | **113/130** | YES | Exemplary | C-15 recovered; C-14 and C-16 absent; C-11 drops to PARTIAL |
| 4 | **V-03** | **113/130** | YES | Exemplary | C-16 recovered; C-14 and C-15 absent; C-11 drops to PARTIAL |

---

## Per-criterion R2 vs R3 progression

| Criterion | R2 best | R3 best variation | R3 score | Status |
|-----------|---------|-------------------|---------|--------|
| C-07 Amend priority | PARTIAL 8/10 (all) | V-05 | 10/10 | SOLVED |
| C-14 APPROX independence | 0/5 (not targeted) | V-01, V-04, V-05 | 5/5 | SOLVED |
| C-15 Axis stacking | 0/5 (not targeted) | V-02, V-05 | 5/5 | SOLVED |
| C-16 Prose uniformity | 0/5 (not targeted) | V-03, V-04, V-05 | 5/5 | SOLVED |
| C-08 Step type depth | PARTIAL 7/10 (all) | none | 7/10 | OPEN -- R4 target |

All four R3 target criteria solved. C-08 is the only criterion below full score across all variations.

---

## Residual Gap: C-08 (3 pts across all variations)

EXACT and PHYSICAL step type justifications under-specified. Phase 1 requires EXACT steps to cite the algebraic identity and PHYSICAL steps to state the assumption, but the Phase 2 block template does not mirror this at verification time. R4 fix: add C-08 justification language to both the Phase 1 type definitions and the Phase 2 block template for EXACT and PHYSICAL steps.

Expected R4 ceiling with that fix: 130/130.

---

## Excellence Signals from V-05

1. **source-removal recovery path closes the paraphrase escape** -- The "If NO: replace (b) with a domain-principle-grounded statement before recording your verdict" instruction is the critical addition over V-04's baseline. Without recovery, an LLM can produce a paraphrase and still record SOUND. With recovery, the paraphrase must be replaced at generation time. C-14 cannot be failed by inertia.

2. **pre-phase gateway table as commitment device** -- The Phase 1b completion check forces the LLM to assert ACTIVE/ABSENT on each axis before writing any verification block. The unconditional gate ("Do NOT proceed to Phase 2 until all three show ACTIVE") prevents silent degradation -- the LLM cannot drop interpolated sub-step verification blocks or revert the prose rule mid-artifact without having first stated these axes are ACTIVE.

3. **severity-priority ordering transforms Amend from free-pick to structured triage** -- "If P1 faults exist, your first fix must address a P1 fault" converts the Amend section from a best-effort citation list to a severity-ordered structure. The P1-first rule resolves the R2 residual gap that persisted across all variations. C-07 now passes without ambiguity.

---

```json
{"top_score": 127, "all_essential_pass": true, "new_patterns": ["source-removal recovery path closes paraphrase escape: If NO replace-b instruction forces self-correction at generation time; LLM cannot record SOUND verdict after producing a paraphrase -- recovery is mandatory not optional", "pre-phase axis-commitment gateway table prevents silent degradation: unconditional Do NOT proceed gate before Phase 2 forces explicit ACTIVE assertion on all three structural axes; commitment device that cannot be passively satisfied", "severity-priority ordering in Amend makes fault triage structural: P1-first rule converts Amend from free-pick-3 citation list to severity-ordered structure; resolves C-07 residual gap from all R2 variations without changing the citation format"]}
```
