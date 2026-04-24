## discover-compare R14 Scorecard

**Rubric**: v12 (/26) | **All projections confirmed**

| Rank | Variation | Composite | Key penalty |
|------|-----------|-----------|-------------|
| 1 | V-01 | **100.00** | None -- v12 ceiling |
| 2 | V-02 | **99.81** | C-32 PARTIAL: deviation-only routing block without scope header |
| 2 | V-03 | **99.81** | C-33 PARTIAL: BODY ORDER present but no named token |
| 4 | V-04 | **99.62** | C-32 + C-33 both PARTIAL (R13 V-01 rescored; additive) |
| 5 | V-05 | **99.58** | C-28 + C-29 PARTIAL; D = /24 (C-30 + C-32 both not scored) |

---

### Key findings

**C-32 PARTIAL penalty = 0.19**: One header line (`ROUTING: deviation from BODY ORDER only.`) is the fix.

**C-33 PARTIAL penalty = 0.19**: One named token (`BODY-ORDER-LAYER: active`) is the fix.

**C-32 and C-33 strictly additive**: V-04 = 99.62 exactly (2 × 0.19 = 0.38). No interaction effect.

**`BODY-ORDER-LAYER: none` satisfies C-33 PASS**: V-05 confirms declared-absence is a full PASS. Rubric body text gives this exact form as an example. Declared-absence path = full structural declaration, not PARTIAL.

**Denominator ladder confirmed**: /26 → /25 (one not scored) → /24 (both C-30 and C-32 not scored when no BODY ORDER).

---

### Three discriminating questions -- all resolved

1. **Does `Routing: if REG = engineering or general...` satisfy C-32 scope declaration?** NO. Branch condition states the triggering case but does not frame the block as handling only non-default cases. Label alone carries no scope content. C-32 PARTIAL.

2. **Does the `BODY ORDER:` prose directive satisfy C-33 named-token requirement?** NO. Prose instruction is not a token declaration. Implied-by-layout = PARTIAL.

3. **Does `BODY-ORDER-LAYER: none` satisfy C-33 PASS?** YES. Rubric body text gives this exact form as an explicit PASS example. Declared absence = declared status = PASS.

---

### New patterns

**`deviation-only-routing-scope-declaration`** (C-32): Opening a deviation-only routing block with an explicit scope declaration converts design intent from reconstructable-from-absence to declared-as-contract. The scope header is the incremental element beyond the v11 ceiling.

**`body-order-layer-token`** (C-33): A named `BODY-ORDER-LAYER:` token (active or none) makes C-30/C-32 applicability structurally determinable without routing inspection. `none` is explicitly valid per rubric; declared-absence achieves full PASS.

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["deviation-only-routing-scope-declaration", "body-order-layer-token"]}
```
 `Token: BODY-ORDER-LAYER: active` positioned immediately after BODY ORDER directive and before routing block -- named token declares layer status |

```
Essential:    4/4   * 60 = 60.00
Recommended:  3/3   * 30 = 30.00
Aspirational: 26/26 * 10 = 10.00
Composite: 100.00
```

---

#### V-02 -- C-32 PARTIAL probe: BODY-ORDER-LAYER token only, no routing scope header

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R13 V-01 baseline; no change |
| C-28 | **PASS** (1) | BODY ORDER and routing block isolated |
| C-29 | **PASS** (1) | Standalone unconditional BODY ORDER present |
| C-30 | **PASS** (1) | Deviation-only routing block; exec branch absent |
| C-31 | **PASS** (1) | Positional vocabulary in routing branch |
| C-32 | **PARTIAL** (0.5) | Routing block opens with `Routing: if REG = engineering or general...` -- branch condition only; no scope declaration at header; intent reconstructable from branch absence, not declared. `Routing:` label alone carries no scope content |
| C-33 | **PASS** (1) | `Token: BODY-ORDER-LAYER: active` present before routing block -- named token satisfies criterion |

**Discriminating question resolved**: `Routing: if REG = engineering or general...` does NOT satisfy C-32 scope declaration. Branch condition states the triggering case but does not frame the block as handling only non-default cases. Label alone is not content.

```
Essential:    4/4    * 60 = 60.00
Recommended:  3/3    * 30 = 30.00
Aspirational: 25.5/26 * 10 = 9.81
Composite: 99.81
```

---

#### V-03 -- C-33 PARTIAL probe: routing scope header only, no BODY-ORDER-LAYER token

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R13 V-01 baseline; no change |
| C-28 | **PASS** (1) | BODY ORDER and routing block isolated |
| C-29 | **PASS** (1) | Standalone unconditional BODY ORDER present |
| C-30 | **PASS** (1) | Deviation-only routing block; exec branch absent |
| C-31 | **PASS** (1) | Positional vocabulary in routing branch |
| C-32 | **PASS** (1) | Routing block opens with `ROUTING: deviation from BODY ORDER only.` -- explicit scope declaration at header; PASS |
| C-33 | **PARTIAL** (0.5) | No `BODY-ORDER-LAYER:` token. `BODY ORDER: ...` directive is a prose instruction, not a token declaration. Layer status implied by directive presence; evaluator must locate BODY ORDER to determine C-30 applicability. Implied-by-layout = PARTIAL |

**Discriminating question resolved**: Prose directive `BODY ORDER: ...` does NOT satisfy C-33 named-token requirement. Rubric requires a named token in `Token: KEY: value` form. A prose instruction is not a token declaration.

```
Essential:    4/4    * 60 = 60.00
Recommended:  3/3    * 30 = 30.00
Aspirational: 25.5/26 * 10 = 9.81
Composite: 99.81
```

---

#### V-04 -- R13 V-01 rescored against v12: both C-32 and C-33 PARTIAL

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R13 V-01 baseline; no change |
| C-28 | **PASS** (1) | BODY ORDER and routing block isolated |
| C-29 | **PASS** (1) | Standalone unconditional BODY ORDER present |
| C-30 | **PASS** (1) | Deviation-only routing block; exec branch absent |
| C-31 | **PASS** (1) | Positional vocabulary in routing branch |
| C-32 | **PARTIAL** (0.5) | R13 V-01 routing block opens with `Routing: if REG = engineering or general...` -- branch condition only; same as V-02; no scope declaration at header |
| C-33 | **PARTIAL** (0.5) | R13 V-01 has no `BODY-ORDER-LAYER:` token; BODY ORDER directive present but layer status not declared as named token; same as V-03 |

**Additivity confirmed**: 25/26 = 9.615... -> composite 99.62 exactly. V-02 and V-03 each cost 0.19; both firing simultaneously = 0.38. No interaction effect. C-32 and C-33 are strictly additive.

```
Essential:    4/4  * 60 = 60.00
Recommended:  3/3  * 30 = 30.00
Aspirational: 25/26 * 10 = 9.62
Composite: 99.62
```

---

#### V-05 -- BODY-ORDER-LAYER: none probe: R13 V-04 + declared-absence token

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R13 V-01 baseline C-01..C-22; C-23 PASS, C-24 PASS, C-25 PARTIAL carry from R13 V-04 |
| C-28 | **PARTIAL** (0.5) | No standalone BODY ORDER; body ordering implied only through routing block content; same as R13 V-04 |
| C-29 | **PARTIAL** (0.5) | No standalone BODY ORDER; exec ordering expressed only inside routing conditionals; no unconditional directive; same as R13 V-04 |
| C-30 | **N/A** | No standalone BODY ORDER present; criterion not scored; D loses 1 |
| C-31 | **PASS** (1) | Two-branch routing: "produce RECOMMENDATION first, then DECISION MATRIX" / "produce DECISION MATRIX first, then RECOMMENDATION" -- positional vocabulary only; BODY ORDER not named |
| C-32 | **N/A** | No standalone BODY ORDER; criterion not scored per C-32 condition; D loses 1 |
| C-33 | **PASS** (1) | `Token: BODY-ORDER-LAYER: none -- routing is sole ordering mechanism` declared before routing block. Rubric body gives this exact form as an explicit PASS example. Declared absence = declared status = PASS |

**Discriminating question resolved**: `BODY-ORDER-LAYER: none` satisfies C-33 PASS. The rubric body text gives `BODY-ORDER-LAYER: none -- routing is sole ordering mechanism` as an explicit example of the named token. Declared-absence path is a full structural declaration.

**Denominator**: /24 (C-30 not scored -1, C-32 not scored -1; C-33 scored)

Pass-weight: 20 (C-08..C-27) + 0.5 (C-28) + 0.5 (C-29) + 1.0 (C-31) + 1.0 (C-33) = 23/24

```
Essential:    4/4  * 60 = 60.00
Recommended:  3/3  * 30 = 30.00
Aspirational: 23/24 * 10 = 9.58
Composite: 99.58
```

---

### Penalty calibration table (v12)

| Failure mode | Criteria affected | Composite penalty vs V-01 |
|---|---|---|
| Deviation-only routing block without scope header | C-32 PARTIAL | -0.19 |
| BODY ORDER present but no BODY-ORDER-LAYER token | C-33 PARTIAL | -0.19 |
| Both scope header and token missing (R13 V-01 verbatim) | C-32 + C-33 PARTIAL | -0.38 |
| No BODY ORDER; two-branch routing; BODY-ORDER-LAYER: none token | C-28 + C-29 PARTIAL; D = /24 | -0.42 |

---

### V-01 excellence signals

1. **Scope header converts absence into contract**: `ROUTING: deviation from BODY ORDER only.` at the routing block header makes the design decision explicit. The absent exec branch is no longer an apparent omission -- the header declares it is intentionally absent. BODY ORDER owns exec ordering; routing owns only the deviation. One line at the routing block entry converts C-32 from PARTIAL to PASS.

2. **Named token makes applicability condition structurally determinable**: `Token: BODY-ORDER-LAYER: active` positioned immediately after the BODY ORDER directive declares the layer's status as a structural property. An evaluator reading the output can determine C-30/C-32 applicability from the token alone, without inspecting the routing block for exec-branch presence or absence. One token declaration converts C-33 from PARTIAL to PASS.

3. **Two independent, additive fixes on clean orthogonal axes**: Each v12 addition (token + scope header) targets exactly one new criterion (C-33 + C-32 respectively) without disturbing any prior criterion. V-02 and V-03 each demonstrate isolated single-criterion impact at identical cost. The fixes are strictly non-interacting -- confirmed by V-04 additivity at 99.62 exactly.

4. **Declared-absence path (V-05) is a full PASS**: The `BODY-ORDER-LAYER: none` form closes the token architecture for the no-BODY-ORDER case. When the body-ordering layer is explicitly absent, the token declares this as a structural property rather than requiring inference. The rubric explicitly enumerates this form as a PASS example. No-BODY-ORDER outputs can achieve C-33 PASS through declared absence.

---

### New patterns

**`deviation-only-routing-scope-declaration`** (C-32)
When the routing block is deviation-only (BODY ORDER present, no exec branch), opening the block with an explicit scope declaration (`ROUTING: deviation from BODY ORDER only.`, `ROUTING SCOPE: non-exec registers`) converts the design intent from reconstructable-from-absence to declared-as-contract. C-32 PASS requires this explicit declaration at the routing block header; C-30 PASS does not. The scope header is the incremental element that distinguishes the v12 ceiling from the v11/R13 ceiling. C-32 is a head-level criterion; the branch body is evaluated by C-30/C-31.

**`body-order-layer-token`** (C-33)
A named `BODY-ORDER-LAYER:` token before the routing block (value: `active` or `none`) makes the C-30/C-32 applicability condition structurally determinable from output inspection alone. Token value `none` (declared absence) satisfies C-33 PASS when no BODY ORDER is present -- the rubric body text explicitly lists this form as a PASS example. The token is the declaration; the value communicates the complete structural picture. Prose directives and layout inference are both PARTIAL; only named-token form achieves PASS.

---

### Cumulative discrimination map (R14)

| Composite band | Variation | Structural signature |
|---|---|---|
| 100.00 | V-01 | BODY ORDER + deviation-only + positional + scope header + BODY-ORDER-LAYER: active token |
| 99.81 | V-02 | BODY ORDER + deviation-only + positional + token; no scope header (C-32 PARTIAL) |
| 99.81 | V-03 | BODY ORDER + deviation-only + positional + scope header; no token (C-33 PARTIAL) |
| 99.62 | V-04 | BODY ORDER + deviation-only + positional; no header + no token (C-32 + C-33 both PARTIAL) |
| 99.58 | V-05 | No BODY ORDER + two-branch + positional + BODY-ORDER-LAYER: none token; D = /24 |

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["deviation-only-routing-scope-declaration", "body-order-layer-token"]}
```
