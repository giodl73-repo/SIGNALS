## validate-inertia R12 Scorecard

### Results summary

| Variation | C-38 | C-39 | Total | vs. predicted |
|-----------|------|------|-------|---------------|
| V-56 Block positive-only | PARTIAL (5) | FAIL (0) | **375/390** | 375 ✓ |
| V-57 Block positive + prohibition | PASS (10) | PASS (10) | **390/390** | 390 ✓ |
| V-58 Three-axis explicit block | PASS (10) | PASS (10) | **390/390** | 390 ✓ |
| V-59 Minimal footprint | PASS (10) | PASS (10) | **390/390** | 390 ✓ |
| V-60 Full ceiling | PASS (10) | PASS (10) | **390/390** | 390 ✓ |

All five predictions confirmed. All essential criteria pass across all variations.

### Structural questions answered

**Q1:** YES — Positive-only earns C-38 PARTIAL (5), not FAIL. The PARTIAL tier functions exactly as specified.

**Q2:** YES — Adding "not from Phase 5(3) and not from CCV" inside the block earns C-38 PASS + C-39 PASS. The prohibition phrase is the sole structural delta between V-56 (PARTIAL+FAIL) and V-57 (PASS+PASS).

**Q3:** YES — Three-axis labeling produces identical scoring to V-57. Enforcement advantage only: the explicit per-axis gate makes partial omission structurally visible without affecting the score.

**Q4:** YES — Single sentence at end of block is sufficient. Position within the block does not affect pass condition for C-38 or C-39.

**Q5:** YES — Explicit per-axis gate ("A block containing Axes 1 and 2 but omitting Axis 3 fails this gate") is the tightest enforcement shape: converts partial-axis omission from detectable to impossible.

### Excellence signals

1. **Prohibition form is the sole separator**: naming forbidden sources in the block is all that's needed to go from PARTIAL+FAIL to PASS+PASS
2. **Minimal footprint sufficient**: single appended sentence is the lowest-overhead path to ceiling
3. **Per-axis explicit gate** (V-60) extends the C-37 co-residence enforcement pattern to three criteria

```json
{"top_score": 390, "all_essential_pass": true, "new_patterns": ["prohibition form at architecture-read boundary is the sole separator between C-38 PARTIAL and C-38+C-39 PASS: naming forbidden sources (Phase 5(3), CCV) in the block is required; positive-only earns PARTIAL", "minimal footprint sufficient: single sentence at end of named block with positive+prohibition satisfies C-38+C-39 PASS; position within block does not affect pass condition", "per-axis explicit gate (V-60 pattern) extends co-residence enforcement to three criteria by naming all required axes and declaring two-of-three a gate failure"]}
```
o-resident in named architecture block**
Pass condition: derivation direction from C-36 declared within the AUDIT ARCHITECTURE DECLARED block, naming L3 Evidence as required source AND Phase 5(3)/CCV as prohibited sources. Positive-source-only earns PARTIAL.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-56 | **PARTIAL (5)** | Block gains paragraph: "AMEND(d) must derive its lever anchor from the L3 Evidence column of the Citation Chain Completeness Audit. The audit's L3 Evidence cell is the derivation authority -- the source AMEND(d) copies from, not verifies against. This constraint is declared here so it is visible at the same structural read-point as the artifact declarations and audit format above." Required source named (L3 Evidence); derivation direction co-resident. Phase 5(3) and CCV NOT named as prohibited sources anywhere in the block. Positive-source-only earns PARTIAL per pass condition. |
| V-57 | **PASS (10)** | Block gains third paragraph: "AMEND(d) must derive its lever anchor exclusively from the L3 Evidence column of the Citation Chain Completeness Audit -- not from Phase 5(3) and not from CCV. The L3 Evidence cell is the one permitted derivation source. Phase 5(3) and CCV are prohibited derivation sources for the lever anchor in AMEND(d). This derivation direction is declared at the architecture-read boundary so that the full constraint -- required source AND forbidden sources -- is known before any production phase begins." Required source named; both prohibited sources named explicitly. Co-resident in block. Full C-38 pass conditions met. |
| V-58 | **PASS (10)** | Axis 3: "AMEND(d) must derive its lever anchor from the L3 Evidence column of the Citation Chain Completeness Audit. Phase 5(3) is a prohibited derivation source for the lever anchor in AMEND(d). CCV is a prohibited derivation source for the lever anchor in AMEND(d). The L3 Evidence cell is the one permitted source." Derivation direction co-resident as named required axis; positive instruction and both prohibited sources explicitly named. C-38 PASS. |
| V-59 | **PASS (10)** | Single sentence appended to block before gate instruction: "Derivation constraint: AMEND(d) must derive its lever anchor from the L3 Evidence column of the Citation Chain Completeness Audit -- not from Phase 5(3) and not from CCV." Names required source (L3 Evidence) and both prohibited sources. Co-resident in block (before gate instruction). Placement at end of block does not reduce to PARTIAL; pass condition requires co-residence and prohibition form, not position within block. Gate instruction confirms: "the derivation direction constraint (AMEND(d) derives from L3 Evidence; Phase 5(3) and CCV are prohibited derivation sources) have been declared before Phase 1 begins." C-38 PASS. |
| V-60 | **PASS (10)** | Same Axis 3 structure as V-58. "Phase 5(3) is a prohibited derivation source. CCV is a prohibited derivation source. The L3 Evidence cell is the one permitted source." Gate: "A block containing Axes 1 and 2 but omitting Axis 3 fails this gate." Derivation direction co-resident with explicit prohibition form. C-38 PASS. |

---

**C-39 — Derivation prohibition declared at the architecture-read boundary**
Pass condition: AUDIT ARCHITECTURE DECLARED block includes explicit prohibition language naming Phase 5(3) and CCV as forbidden derivation sources within the block. Positive instruction without named forbidden sources fails. C-38 can pass with positive-only; C-39 requires prohibition form in the block.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-56 | **FAIL (0)** | The added paragraph names L3 Evidence as required source but contains no prohibition language. Phase 5(3) and CCV are not named as prohibited derivation sources within the AUDIT ARCHITECTURE DECLARED block. The prohibition exists only in AMEND(d), not at the architecture-read boundary. C-39 requires prohibition form in the block; positive-only fails. |
| V-57 | **PASS (10)** | Third paragraph: "not from Phase 5(3) and not from CCV... Phase 5(3) and CCV are prohibited derivation sources for the lever anchor in AMEND(d). This derivation direction is declared at the architecture-read boundary so that the full constraint -- required source AND forbidden sources -- is known before any production phase begins." Explicit prohibition language present in named block; both forbidden sources named. Gate confirms all three constraints declared. C-39 PASS. |
| V-58 | **PASS (10)** | Axis 3: "Phase 5(3) is a prohibited derivation source for the lever anchor in AMEND(d). CCV is a prohibited derivation source for the lever anchor in AMEND(d)." Explicit prohibition language at architecture-read boundary. Gate requires Axis 3 (with "prohibited sources named") to be present. C-39 PASS. |
| V-59 | **PASS (10)** | Single sentence: "AMEND(d) must derive its lever anchor from the L3 Evidence column of the audit -- not from Phase 5(3) and not from CCV." "Not from Phase 5(3)" and "not from CCV" are explicit prohibition forms within the named block. Gate confirms prohibited sources declared before Phase 1. Minimal footprint at end of block is sufficient for C-39 PASS. |
| V-60 | **PASS (10)** | Same Axis 3 as V-58. Explicit prohibition for both Phase 5(3) and CCV. Gate: "A block containing Axes 1 and 2 but omitting Axis 3 fails this gate" — Axis 3 carries the prohibition. C-39 PASS. |

---

### Composite Scores

| Variation | C-01–C-37 | C-38 | C-39 | **Total** | vs. predicted |
|-----------|-----------|------|------|-----------|---------------|
| V-56 | 370 | 5 | 0 | **375/390** | 375 ✓ |
| V-57 | 370 | 10 | 10 | **390/390** | 390 ✓ |
| V-58 | 370 | 10 | 10 | **390/390** | 390 ✓ |
| V-59 | 370 | 10 | 10 | **390/390** | 390 ✓ |
| V-60 | 370 | 10 | 10 | **390/390** | 390 ✓ |

All predictions confirmed. All essential criteria pass in all variations.

---

### Rankings

1. **V-57** — 390/390 (dedicated paragraph, positive + prohibition)
1. **V-58** — 390/390 (three-axis explicit block)
1. **V-59** — 390/390 (minimal-footprint single sentence)
1. **V-60** — 390/390 (three-axis + per-axis explicit gate)
5. **V-56** — 375/390 (positive-only: C-38 PARTIAL, C-39 FAIL)

---

### Structural Questions — Answered

**Q1 (C-38 partial test, V-56):** YES -- Positive-only in block earns C-38 PARTIAL (5 pts), not FAIL. The criterion explicitly states "positive-source-only (no prohibited sources named) earns PARTIAL." The presence of derivation direction co-resident in the block is sufficient for a non-zero score on C-38; the prohibition form is required to reach PASS. V-56 confirms the PARTIAL scoring tier functions exactly as specified.

**Q2 (C-38 + C-39 full, V-57):** YES -- Positive instruction + explicit prohibition language in block earns C-38 PASS (10) + C-39 PASS (10). The dedicated paragraph naming "not from Phase 5(3) and not from CCV" within the AUDIT ARCHITECTURE DECLARED block satisfies both criteria simultaneously. The prohibition form at the architecture-read boundary (C-39) is the single structural delta between V-56 (PARTIAL+FAIL) and V-57 (PASS+PASS). No other change was required.

**Q3 (structural axis, V-58):** YES -- Three-axis explicit labeling produces identical C-38+C-39 scoring as V-57 (390/390). Axis labeling does not add scoring beyond the prohibition form. The structural advantage is enforcement: an explicit gate condition naming all three axes by name ("A block containing only two of three axes fails this gate") makes partial-axis omission visible at the gate level without per-criterion analysis. Same ceiling, stronger structural omission detection.

**Q4 (phrasing axis, V-59):** YES -- Minimal footprint at end of block is sufficient. A single sentence with positive + prohibition at the end of the named block earns C-38 PASS + C-39 PASS identically to V-57's dedicated paragraph or V-58's labeled axis. Position within the block does not affect pass condition. The requirements are co-residence and prohibition form; both are satisfied regardless of whether the constraint appears as a dedicated paragraph, a labeled axis, or a single sentence appended at the end.

**Q5 (combination, V-60):** YES -- Explicit per-axis gate check does not add scoring above the ceiling (all four tie at 390). The enforcement advantage is the explicit impossibility statement: "A block containing Axes 1 and 2 but omitting Axis 3 fails this gate" converts partial-axis omission from a detectable failure into a structurally impossible compliance path. A model must write all three axes or visibly fail the gate. This is the tightest enforcement shape for C-38/C-39 and the recommended production variant.

---

### Excellence Signals from Top Variations

**Signal 1 -- Prohibition form is the sole C-38/C-39 separator.** V-56 demonstrates that co-resident positive instruction (naming required source only) earns C-38 PARTIAL but not C-39. V-57 demonstrates that adding "not from Phase 5(3) and not from CCV" within the same block upgrades C-38 to PASS and earns C-39 PASS. The exact delta is the prohibition phrase co-resident in the named block. No other structural change is required. The prohibition form at the block level is not redundant with AMEND(d)'s prohibition -- it makes the forbidden sources visible at the architecture-read boundary, before any production phase can introduce a reconstruction opportunity.

**Signal 2 -- Minimal footprint suffices; position within block does not matter.** V-59 demonstrates that a single compact sentence at the end of the AUDIT ARCHITECTURE DECLARED block achieves C-38 PASS + C-39 PASS. The pass conditions require co-residence in the named block and prohibition form naming both forbidden sources. They say nothing about paragraph structure, position, or labeling. The lowest-overhead production path to ceiling on C-38/C-39 is a single appended sentence before the gate instruction, with no structural penalty for minimal footprint.

**Signal 3 -- Per-axis explicit gate (V-60 pattern) extends co-residence enforcement to three criteria.** The C-37 pattern (named gated block makes simultaneous omission of C-33/C-34 the only failure shape) generalizes to three co-resident criteria when the gate explicitly names all three axes. V-60's "A block containing Axes 1 and 2 but omitting Axis 3 fails this gate" creates a structural impossibility for two-of-three compliance on C-33/C-34/C-38. This is the most complete enforcement shape: co-residence protects against individual-axis dropping; the named gate condition makes the protected set explicit and checkable.

---

```json
{"top_score": 390, "all_essential_pass": true, "new_patterns": ["prohibition form at architecture-read boundary is the sole separator between C-38 PARTIAL and C-38+C-39 PASS: naming forbidden sources (Phase 5(3), CCV) in the block is required; positive-only earns PARTIAL", "minimal footprint sufficient: single sentence at end of named block with positive+prohibition satisfies C-38+C-39 PASS; position within block does not affect pass condition", "per-axis explicit gate (V-60 pattern) extends co-residence enforcement to three criteria by naming all required axes and declaring two-of-three a gate failure"]}
```
