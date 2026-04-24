# Quest Score — org-scan R15 (v15 Rubric)

## Scoring Framework

| Band | Weight | Criteria | Max |
|---|---|---|---|
| Essential | 60% | C-01–C-05 | 60 |
| Recommended | 30% | C-06–C-08 | 30 |
| Aspirational | cap 10 | C-09–C-57 (49 criteria, 2 pts each, cap 10) | 10 |
| **Total** | | | **100** |

---

## Per-Variation Scoring

### V-01 — Row-Count Enforcement Statement

**Axis**: Output format — named N=N verification step in SYNTHESIZER before TABLE G is produced.

**Essential (C-01–C-05)**

| Criterion | Verdict | Note |
|---|---|---|
| C-01 Areas named and traceable | PASS | SCANNER instructions enumerate 7 source types; TABLE B schema requires per-row evidence |
| C-02 Multi-source scan (3+ of 7) | PASS | 7 source types enumerated in order; min 3 required in gate checklist item 3 |
| C-03 Headcount as range with rationale | PASS | SYNTHESIZER step 4 requires range + 2 TABLE B citations |
| C-04 Cross-cutting concerns with boundary note | PASS | SYNTHESIZER step 6 names boundary note per concern |
| C-05 Raw analysis only — no org chart | PASS | Stated in preamble and in SYNTHESIZER "Final constraint (stated twice)" |

Essential score: **60/60**

**Recommended (C-06–C-08)**

| Criterion | Verdict | Note |
|---|---|---|
| C-06 Team boundary candidates with seam rationale | PASS | SYNTHESIZER step 5: 2–4 candidates with seam rationale |
| C-07 Org shape named and justified | PASS | SYNTHESIZER step 7: named shape + 2–3 sentence justification from TABLE D |
| C-08 Evidence gaps flagged explicitly | PASS | TABLE C schema with 4 gap types including prediction-not-resolved |

Recommended score: **30/30**

**Aspirational (C-09–C-57)**

Key cluster checks (invariants from all prior rounds confirmed; only differentiators noted):

| Criterion | Verdict | Note |
|---|---|---|
| C-09 5+ file paths | PASS | Path floor enforced as gate condition (checklist item 4) |
| C-11 Anti-fabrication language | PASS | SCANNER instructions: "cite only paths that exist" |
| C-13 C-05 stated twice | PASS | Preamble + SYNTHESIZER "Final constraint (stated twice — preamble and here)" |
| C-15 Structural group labels | PASS | GROUP A / GROUP B / GROUP C boundaries present |
| C-16 File path floor as gate condition | PASS | Gate checklist item 4 blocks forward progress if unmet |
| C-17 Gate confirmation token | PASS | Named `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]` |
| C-18 Gate failure output | PASS | Explicit fail tokens: "Path floor not met" / "Source floor not met" |
| C-20 Bidirectional gate token protocol block | PASS | GATE TOKEN PROTOCOL preamble block defines both tokens before Phase 1 |
| C-22 Formal phase contract | PASS | "Both blocks name the same contract from both sides. Both must hold." |
| C-24 Self-documenting pass token | PASS | Token reports source count, path count, dominant pattern code |
| C-26 Dictionary invalidity statement | PASS | "Free text in the Inertia Match column is structurally invalid…" |
| C-27 Full-schema status annotation | PASS | Status: REQUIRED on every column in every table |
| C-28 Bilateral contract declaration sentence | PASS | Present at PREDICTOR/SCANNER and SCANNER/GATEKEEPER boundaries |
| C-55 TABLE G row-count mismatch structurally detectable | PASS | Completeness rule: "TABLE G row count must equal TABLE A row count — a row-count mismatch is a structurally detectable omission" |
| C-56 PREDICTOR blacklist names file reads / scan evidence | PASS | "Prohibited outputs: file reads / scan evidence / TABLE B / TABLE C…" |
| C-57 Primary constraint cascaded to all 4 roles + preamble | PASS | All four role scope declarations prohibit "org chart / reporting lines"; preamble constraint = 5 enforcement points |

All 49 aspirational criteria: **PASS** (49/49 = 98 aspirational points; capped at 10)

V-01 **unique pattern** (beyond rubric): Named `TABLE A count: N — TABLE G must contain exactly N rows.` assertion recorded before TABLE G is produced; agent verifies count at SYNTHESIZER exit. This is execution-time enforcement — the count is output, making closure verifiable without prose inspection. Not yet captured in any criterion.

**V-01 Total: 100/100**

---

### V-02 — Input Dependency Block in Scope Declarations

**Axis**: Scope declaration completeness — five-property role contract (authority + inputs + permitted + prohibited + constraint).

**Essential (C-01–C-05)**: PASS all — identical to V-01. **60/60**

**Recommended (C-06–C-08)**: PASS all. **30/30**

**Aspirational: All C-09–C-57 confirmed PASS** (structural invariants unchanged; input dependency blocks are additive).

V-02 **unique pattern** (beyond rubric): Named `Input Dependencies` block inside each ROLE SCOPE DECLARATION explicitly lists what tables and declarations must exist before the role may begin. Execution ordering becomes derivable from declarations alone — no instruction-sequence traversal required. C-54's in-block entry condition verifies; the new Input Dependencies block declares. Together they express the dependency relationship bidirectionally at role scope level.

**V-02 Total: 100/100**

---

### V-03 — Hypothesis Floor Gate

**Axis**: Lifecycle emphasis — named HYPOTHESIS FLOOR GATE at PREDICTOR/SCANNER boundary; dual-gate architecture.

**Essential (C-01–C-05)**: PASS all. **60/60**

**Recommended (C-06–C-08)**: PASS all. **30/30**

**Aspirational: All C-09–C-57 confirmed PASS**

Additional gate token protocol check: V-03 defines BOTH hypothesis floor gate tokens AND evidence gate tokens in the GATE TOKEN PROTOCOL preamble block. C-20 (gate token protocol block defines pass and fail tokens before Phase 1) — PASS; the block now defines two complete gate protocols, which is strictly stronger.

V-03 **unique pattern** (beyond rubric): Named `HYPOTHESIS FLOOR GATE` at PREDICTOR/SCANNER boundary evaluates TABLE A for 3+ predictions and 2+ distinct inertia pattern codes before scanning begins. Prediction underfitting (single-code TABLE A) is structurally detectable at the boundary via a named fail token, not only detectable after synthesis when TABLE G has fewer rows than expected. Creates a symmetric pair of named floor gates: hypothesis floor (prediction quality) ↔ evidence floor (path/source quality).

**V-03 Total: 100/100**

---

### V-04 — Combined: Row-Count Enforcement + Input Dependency Declarations

**Axes**: V-01 + V-02

**Essential (C-01–C-05)**: PASS all. **60/60**

**Recommended (C-06–C-08)**: PASS all. **30/30**

**Aspirational: All C-09–C-57 confirmed PASS**

V-04 carries both V-01 and V-02 patterns simultaneously:
- Input Dependencies in all four role scope declarations → execution order derivable from declarations
- Row-Count Verification step in SYNTHESIZER → completeness verifiable at execution exit

These close a bidirectional completeness loop: scope declarations assert pre-conditions per role (declarations before execution); the N=N enforcement step verifies the post-condition at synthesis exit (assertion after execution). Together they make the TABLE G completeness obligation both declared (V-02: SYNTHESIZER declares dependency on TABLE A) and enforced (V-01: SYNTHESIZER records N and verifies row count).

**V-04 Total: 100/100**

---

### V-05 — Combined: Input Dependency Declarations + Hypothesis Floor Gate

**Axes**: V-02 + V-03

**Essential (C-01–C-05)**: PASS all. **60/60**

**Recommended (C-06–C-08)**: PASS all. **30/30**

**Aspirational: All C-09–C-57 confirmed PASS**

V-05 carries V-02 and V-03 simultaneously:
- Input Dependencies in all four scope declarations
- Hypothesis Floor Gate at PREDICTOR/SCANNER boundary
- SCANNER's `Input Dependencies` block declares: `TABLE A (from PREDICTOR) — must pass hypothesis floor gate / hypothesis floor pass token`

This is architecturally notable: SCANNER's dependency declaration explicitly references the hypothesis floor gate as a named quality condition, not just the table. The floor gate result is threaded into the dependency contract, making the prediction quality obligation structurally visible at SCANNER's entry scope without inspecting the full boundary section.

V-05 does not carry the V-01 Row-Count Verification step — SYNTHESIZER instructions in V-05 begin with TABLE D (no N=N recording step).

**V-05 Total: 100/100**

---

## Variation Rankings

| Rank | Variation | Score | New Patterns | Distinguishing Feature |
|---|---|---|---|---|
| 1 | **V-04** | 100 | V-01 + V-02 | Closes pre/post-condition completeness loop: declarations assert pre-conditions, N=N step enforces post-condition — bidirectional verifiability across the full skill |
| 2 | **V-05** | 100 | V-02 + V-03 | Gives prediction phase a full structural contract: declared clean entry (scope), enforced quality exit (floor gate); SCANNER's dependency on TABLE A qualified by floor gate result |
| 3 | **V-03** | 100 | V-03 | Dual-gate architecture — hypothesis floor gate symmetrizes prediction governance with evidence governance |
| 4 | **V-01** | 100 | V-01 | Execution-time N=N enforcement in SYNTHESIZER — count is output, making TABLE G completeness machine-verifiable |
| 5 | **V-02** | 100 | V-02 | Five-property role contract — execution order derivable from scope declarations alone |

All five variations achieve maximum score. V-04 ranks first by combining the strongest completeness closure pattern (N=N execution enforcement) with the strongest structural transparency pattern (input dependency declarations), forming a closed pre/post-condition contract that spans the full skill.

---

## Excellence Signals (New Patterns for R16 Rubric)

Three new patterns from R15 variations, each a candidate criterion:

**From V-01 (present in V-01, V-04):**
> Named execution-time row-count recording in SYNTHESIZER: before producing TABLE G, the agent explicitly writes `TABLE A count: N — TABLE G must contain exactly N rows.`, performs TABLE G production, then verifies row count at exit. The count assertion is a named output in the execution trace, making hypothesis-closure completeness self-verifiable by row-count comparison without prose inspection. Extends C-55's schema-level row-count mismatch rule from a declared structural obligation to an in-execution enforcement action.

**From V-02 (present in V-02, V-04, V-05):**
> Named `Input Dependencies` block inside each ROLE SCOPE DECLARATION, listing tables and declarations required before the role may begin. Creates a five-property role contract (authority + inputs + permitted + prohibited + constraint check) where execution ordering is derivable from role declarations alone. Extends C-54's in-block constraint check (which verifies prerequisites exist) to a structured declaration of what those prerequisites are — declaration and verification become a matched pair at each role scope.

**From V-03 (present in V-03, V-05):**
> Named `HYPOTHESIS FLOOR GATE` at the PREDICTOR/SCANNER boundary evaluating TABLE A for 3+ predictions and 2+ distinct inertia pattern codes, with explicit named pass and fail tokens defined in the GATE TOKEN PROTOCOL preamble block. Creates a symmetric dual-gate architecture: prediction quality (hypothesis floor) ↔ evidence quality (path floor). Prediction underfitting is structurally detectable at the boundary via fail token without requiring post-synthesis inspection of TABLE G row count.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Execution-time N=N row-count recording in SYNTHESIZER: agent writes TABLE A count assertion before producing TABLE G, verifies row count at exit — makes hypothesis-closure completeness verifiable by count comparison without prose inspection, extending C-55 schema-level rule to in-execution enforcement", "Named Input Dependencies block in every ROLE SCOPE DECLARATION declaring tables and declarations required before the role begins — five-property role contract (authority + inputs + permitted + prohibited + constraint) makes execution ordering derivable from declarations alone without reading instruction sequence", "Named HYPOTHESIS FLOOR GATE at PREDICTOR/SCANNER boundary enforcing 3+ predictions and 2+ distinct pattern codes via explicit pass/fail tokens in preamble GATE TOKEN PROTOCOL — creates symmetric dual-gate architecture where prediction quality is enforced at boundary symmetrically with evidence quality, making underfitting structurally detectable before scanning begins"]}
```
