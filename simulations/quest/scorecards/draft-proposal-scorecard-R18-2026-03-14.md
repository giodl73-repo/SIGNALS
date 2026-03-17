# Draft-Proposal Round 18 Scoring

## Variation Scores

| Rank | Variation | Score | Pass/38 | Fails |
|------|-----------|-------|---------|-------|
| 1 | **V-03** | **99.74** | 37/38 | C-45 only |
| 2 | **V-02** | **99.21** | 35/38 | C-44, C-43, C-45 |
| 2 | **V-04** | **99.21** | 35/38 | C-24, C-44, C-43 |
| 4 | **V-01** | **98.95** | 34/38 | C-42→C-43→C-44 cascade + C-45 |
| 5 | **V-05** | **95.53** | 21/38 | C-23 root + 14-deep cascade + C-42/C-44/C-45 |

## Per-Variation Detail

### V-01 — Lifecycle Emphasis (98.95)
- **C-42 FAIL**: T-40 CONDITION names deficiency category without quoting a deficient T-38 form
- **C-43 FAIL**: Cascade from C-42 — no exemplar → no prescription guidance possible
- **C-44 FAIL**: Cascade from C-42 — no exemplar → no explanation-of-abstractness possible
- **C-45 FAIL**: T-42 CONDITION abstract-only; independent fail
- All E/R-tier: PASS

### V-02 — Output Format (99.21)
- **C-42 PASS**: Exemplar-quoting directive → deficient T-38 form successfully quoted
- **C-44 FAIL** (independent): Exemplar present, but no explanation directive → "why abstract" phrase absent
- **C-43 FAIL**: No prescription directive → no correct-format T-38 example shown
- **C-45 FAIL**: T-42 abstract in spec; mirrors abstract form
- All E/R-tier: PASS

### V-03 — Phrasing Register (99.74)
- **C-42 PASS**: Maximally explicit T-40 spec; exemplar quoted
- **C-43 PASS**: Prescription directive present; passing T-38 form shown
- **C-44 PASS**: Explanation-of-abstractness label present alongside exemplar
- **C-45 FAIL** (independent): T-42 uses abstract category language only; does not quote deficient T-40 form
- All E/R-tier: PASS

### V-04 — Lifecycle + Output Format (99.21)
- **C-24 FAIL**: Stale row count (43 rows instead of 45); PRE-DOCUMENT phase check fires
- **C-44 FAIL** (independent): Exemplar present, explanation absent — same as V-02 pattern
- **C-43 FAIL**: No prescription directive — same as V-02 pattern
- **C-45 PASS**: T-42 receives exemplar-guided direction; deficient T-40 form successfully quoted
- All E/R-tier: PASS

### V-05 — Cascade Root (95.53)
- **C-23 FAIL** (root): P×I computed inline in Phase 2 RISK instead of `[R-NN pending]`
- **C-26 FAIL**: Cascade — transition notation broken
- **C-31..C-43 FAIL**: 13-criterion cascade — Phase 9b back-fill chain requires `[R-NN pending]` placeholders as source; entire domain enumeration collapses
- **C-42, C-44, C-45 FAIL**: Independent — T-40/T-42 abstract in spec
- Total fails: 17 · All E/R-tier: PASS

## Excellence Signals — V-03

**Signal 1: Specification phrasing register is load-bearing.** Where the spec uses explicit labeled structure (T-40: "Part 1: exemplar + explanation / Part 2: prescription"), the LLM output precisely mirrors that structure. Where the spec uses category-only language (T-42), the LLM mirrors the abstraction level. The model does not upgrade abstract specs — it reproduces them.

**Signal 2: Triple-layer T-40 is the minimum for cascades immunity.** C-42 PASS (exemplar) + C-44 PASS (explanation) + C-43 PASS (prescription) are achieved together only when all three directives appear explicitly in the spec. V-03 confirms the prerequisite chain is sufficient, not just necessary.

**Signal 3: Single isolatable fail as calibration proof.** V-03's design (one deliberately abstract T-42, everything else explicit) proves the rubric is correctly calibrated: 37 criteria are genuinely independent and satisfiable without interdependence, and C-45 is a clean single-point failure with no cascade surface.

```json
{"top_score": 99.74, "all_essential_pass": true, "new_patterns": ["Specification phrasing register fidelity: LLM output abstraction level mirrors spec abstraction level — explicit labeled directives produce explicit outputs; category-only language produces category-only outputs, with no inference upgrade", "Triple-layer T-40 exemplar structure (quote + explain abstractness + prescribe correct form) is the minimum spec content for cascade immunity across C-42/C-43/C-44 simultaneously"]}
```
