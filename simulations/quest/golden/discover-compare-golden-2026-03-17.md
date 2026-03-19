Golden prompt written to `simulations/quest/golden/discover-compare-golden-2026-03-17.md`.

**Summary:**

- **Source:** V-02 (minimal BRANCH-RULE, all paths use `{AMEND-HALT}` token recall)
- **Score:** 100.00 / 33 criteria (R20, pre-v18 ceiling criteria)
- **Simplification:** 22% reduction applied to analysis-phase directives (instructional prose stripped to operative-only form)

**What made it golden (vs V-01 baseline):**

1. **C-39 uniform recall** — all three AMEND paths use `{AMEND-HALT}`, never the literal string; V-01 failed because Override used the literal phrase
2. **C-39 timing** — `AMEND-HALT` declared before `AMEND:` opens; V-03 confirmed that inside-phase declaration fails the timing condition even with correct token-name recall
3. **C-40 minimal BRANCH-RULE confirmed** — naming both elements without equivalence sets satisfies C-40; equivalence sets are a v18/C-41 ceiling, not a C-40 gate
4. **Dual-polarity FAULT co-located at each inertia site** — single-line positive+negative encoding, not deferred to header
5. **BODY-ORDER-LAYER + deviation-only routing** — unconditional body order declared before routing block; routing scoped to deviation only, making exec ordering structure-independent

**Next ceiling:** C-41 (equivalence sets enumerated in BRANCH-RULE) and C-42 (per-path literal-substitution prohibition co-located at each AMEND halt) — both introduced in v18, not yet scored.
--

REG-framed.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

REG-framed.

Token: `COMP-A: {positioning}`

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
INERT-A:   [ ]
INERT-B:   [ ]
RISK-A:    [ ]
RISK-B:    [ ]
COMP-A:    [ ]
COMP-B:    [ ]
```

**HALT -- do not proceed if any token is absent.** Produce missing token, return here, verify all pass.

---

BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]

ROUTING: deviation from BODY ORDER only.
DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND-HALT: "any of the above tokens is absent"

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend matrix if {AMEND-HALT}.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if {AMEND-HALT}.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if {AMEND-HALT}.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

## What Made It Golden

**1. Consistent token-name recall across all AMEND paths (C-39 PASS)**
All three AMEND paths (`Add-C`, `Weight`, `Override`) use `{AMEND-HALT}` — never the literal string. V-01 failed C-39 because the Override path substituted the literal phrase "any of the above tokens is absent" while Add-C and Weight used the token name. The "one or more" clause in C-39 fires on a single non-recall path. Golden form: every path encodes the halt condition as a token reference, making encoding discipline uniform and detectable.

**2. AMEND-HALT declared before the AMEND phase opens (C-39 timing)**
`AMEND-HALT: "any of the above tokens is absent"` appears on the line immediately before `AMEND:` — outside the phase. V-03 confirmed that placing the declaration on the line immediately *after* `AMEND:` fails C-39's before-phase timing condition even when token-name recall is correct at all three paths. The two C-39 conditions (timing and encoding) are independently required.

**3. Minimal BRANCH-RULE satisfies C-40 without equivalence sets (confirmed by R20)**
`BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]` names both required elements without enumerating equivalence sets. R20 V-02 confirmed that equivalence set enumeration (`{DEVIATION: | OVERRIDE:}`, `{precedes | before | follows | after}`) is a visibility enhancement, not a C-40 gate condition. Minimal naming is sufficient. C-41 (v18) is the higher tier requiring enumeration.

**4. Dual-polarity FAULT at each inertia site — single-line encoding (C-11, C-18)**
Each inertia phase carries a one-line FAULT that encodes both the positive mandate (compare against ANCHOR[0] only) and the negative prohibition (inter-option comparison is an error) simultaneously. The prohibition is co-located with TOKEN RECALL at point of use, not deferred to a header or preamble. This makes inertia comparison violations structurally detectable.

**5. BODY-ORDER-LAYER token with deviation-only routing block (C-29, C-30, C-33)**
`BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` is declared unconditionally before any routing block. The ROUTING block handles only the engineering/general deviation — it does not restate the default order. `BODY-ORDER-LAYER: active` is declared as a standalone token. The routing block is scoped via `ROUTING: deviation from BODY ORDER only.` This separation means exec-register ordering is satisfied by body section position alone, independent of whether the routing block fires.

---

## Final Rubric Criteria Summary (v18 — /35 base denominator)

### Essential (60% weight — 4 criteria)

| ID | Criterion |
|----|-----------|
| C-01 | All four dimensions covered for both options |
| C-02 | Inertia applied independently to each option (dual-polarity FAULT co-located) |
| C-03 | Decision matrix present |
| C-04 | Concrete recommendation stated |

### Recommended (30% weight — 3 criteria)

| ID | Criterion |
|----|-----------|
| C-05 | Build/no-build gate surfaced when both inertia = HIGH |
| C-06 | Risks meaningfully differentiated between options |
| C-07 | AMEND section is actionable with concrete slots |

### Aspirational (10% weight — 28 criteria at /35 base)

| ID | Criterion |
|----|-----------|
| C-08 | Option 0 (status quo) named column in matrix |
| C-09 | Audience register calibrated in primary flow |
| C-10 | Token ledger cross-checked at matrix assembly |
| C-11 | Inertia independence stated as explicit exclusion rule |
| C-12 | Status quo baseline committed before analysis begins |
| C-13 | Anchor sentence reproduced verbatim at each inertia phase |
| C-14 | Exclusion prohibition named as failure class at point of use |
| C-15 | Register declared before status quo anchor |
| C-16 | Token ledger enforced as blocking gate |
| C-17 | Output compressed to operative directives only |
| C-18 | Exclusion FAULT encoded as single dual-polarity directive |
| C-19 | AMEND phase self-contained via inline TOKEN RECALL and FAULT |
| C-20 | TOKEN RECALL at each AMEND path scoped to that path's requirements |
| C-21 | Dual-polarity FAULT discipline propagates into every AMEND path |
| C-22 | Phase structure enforced by token positioning and dividers, not headers |
| C-23 | Exec-register output leads with recommendation before matrix |
| C-24 | AMEND path token enumeration present |
| C-25 | Register-gated routing block present |
| C-26 | Body section order exec-safe |
| C-27 | Routing block within LEDGER GATE scope |
| C-28 | Body-order and routing-scope isolated |
| C-29 | BODY ORDER unconditional |
| C-30 | Routing handles only deviation |
| C-31 | Routing vocabulary positionally descriptive |
| C-32 | Routing scope declared deviation-only |
| C-33 | BODY-ORDER-LAYER token present as standalone declaration |
| C-34 | AMEND enumeration in separable fenced-code block |
| C-35 | HALT uses positional reference language |
| C-36 | Engineering branch carries deviation marker |
| C-37 | HALT phrase uniform across all AMEND paths (resolved-value uniformity) |
| C-38 | Branch pairs deviation marker + positional vocabulary (line-level) |
| C-39 | HALT phrase declared as canonical token before AMEND phase, recalled by name at all paths |
| C-40 | Pairing contract (BRANCH-RULE) declared before routing block, names both required elements |
| C-41 | BRANCH-RULE enumerates equivalence sets for both required elements *(v18 new — gate: C-40 PASS required)* |
| C-42 | Each AMEND path halt carries co-located literal-substitution prohibition *(v18 new — gate: C-39 PASS required)* |

**Denominator:** /35 base. C-35+C-37+C-39+C-42 excluded when C-34 PARTIAL (-> /31). C-36+C-38+C-40+C-41 excluded when C-32 N/S (-> /31). Both exclusion pairs active simultaneously (-> /27).

**R20 score:** 33/33 = 100.00 (pre-v18; C-41 and C-42 not yet scored — next-round ceiling criteria).
