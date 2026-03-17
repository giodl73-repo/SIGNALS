| Variate | Essential | Recommended | Aspirational passing | Aspirational pts | Composite | % max | Golden? |
|---------|-----------|-------------|----------------------|------------------|-----------|-------|---------|
| V-01 | 60 | 30 | 43/49 | 215.0 | **305.0** | 91.0% | YES |
| V-02 | 60 | 30 | 43/49 | 215.0 | **305.0** | 91.0% | YES |
| V-03 | 60 | 30 | 42/49 | 210.0 | **300.0** | 89.6% | YES |
| V-04 | 60 | 30 | 42/49 | 210.0 | **300.0** | 89.6% | YES |
| V-05 | 60 | 30 | 49/49 | 245.0 | **335.0** | 100% | YES |

_43/49 × 245 = 10535/49 = 215.0. 42/49 × 245 = 10290/49 = 210.0._

---

## Rankings

| Rank | Variate | Score | Delta from top |
|------|---------|-------|----------------|
| 1 | **V-05** (BOUNDED BLOCK PROTOCOL -- full chain C-50 through C-56) | 335/335 | -- |
| 2 | **V-01** (SCAN PROTOCOL -- C-50 only) | 305/335 | -30 |
| 2 | **V-02** (BOUNDED BLOCK PROTOCOL first -- C-51 only) | 305/335 | -30 |
| 4 | **V-03** (UNIVERSAL VERIFICATION PROTOCOL -- new axis) | 300/335 | -35 |
| 4 | **V-04** (MANDATE ECHO SATURATION PROTOCOL -- new axis) | 300/335 | -35 |

V-01 and V-02 tie at 305: each satisfies one half of the C-50/C-51 conjunction but not both, leaving C-52 through C-56 unreachable. V-03 and V-04 are new single-axis variants -- both fail C-50 and C-51, missing all 7 chain criteria for -35 vs V-05. The gap between V-01/V-02 and V-03/V-04 is 5 pts: V-01 gains C-50, V-02 gains C-51, both fail the other.

---

## Excellence Signals from V-05

V-05 achieves 335/335 -- perfect score under v19 rubric. The new signal this round is what V-05 adds beyond C-55 and C-56: the dual-site active verification extension.

### Signal -- Dual-Site Active Verification (potential C-57)

V-05 Component 1 header carries three layers at the application site:

```
# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above      <- C-56: static mandate echo
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)             <- C-56: NOT list echo
# Verify before finalizing this Component 1: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns  <- new: active verification echo
```

The third line is distinct from C-56. C-56 echoes the static mandate and exclusion list as context -- the model reads the boundary. The third line converts the application site into an active verification checkpoint -- the model is instructed to run per-item checks before completing Component 1. This is C-55's mechanism (per-item NOT/IS confirmation protocol) applied at the application site rather than only at the declaration site.

**Design principle**: C-55 places active verification at the declaration site; C-56 echoes the static boundary at the application site; the C-57 pattern echoes the active verification itself at the application site. A model that skips the protocol section (C-55 site) encounters the active checklist at the Component 1 header (C-57 site). Dual-site coverage makes active verification document-skip-resistant.

**Distinction from C-56**: C-56 is passive (boundary as reference: "NOT these formats"); C-57 is active (instruction: "Verify before finalizing: NOT these formats"). Both close different attention gaps: C-56 closes the boundary-recall gap; C-57 closes the verification-trigger gap.

### R19 new axes -- V-03 and V-04 pattern signals

**V-03 (Universal Verification)**: The SELF-VERIFY blocks at every construction step apply C-55's mechanism broadly. Each step ends with NOT/IS checks specific to that step's output, preventing error propagation. Potential C-58: "Universal per-step active verification -- every construction step ends with a SELF-VERIFY block listing forbidden outputs and required output for that step."

**V-04 (Mandate Echo Saturation)**: Per-field mandate echoes in the production YAML schema make every template field locally self-contained. Extends co-location discipline (C-26/C-37/C-39) from BAD PLAN body to the production template. Potential C-59: "Per-field mandate echo saturation -- every template field that carries a criterion-testable value echoes its governing mandate inline at the field position."

Both V-03 and V-04 score 42/49. Their new patterns are architecturally sound. Evaluation as C-57/C-58/C-59 candidates for R20.

---

## New Patterns

**Pattern from V-05 -- Dual-site active verification echo**: The active NOT/IS verification checklist (C-55, at declaration site) is also echoed at the Component 1 header (application site) as a "Verify before finalizing:" instruction, extending C-56's co-location discipline from static mandate to active verification protocol. Both passive boundary and active verification instruction are present at the instantiation point, independently of whether the protocol section was read.

**Pattern from V-03 -- Universal per-step verification**: The C-55 active NOT/IS checklist pattern applied universally at every construction step, not just the Component 1 format mandate. Each SELF-VERIFY block is step-specific and prevents error propagation forward.

**Pattern from V-04 -- Mandate echo saturation in production template**: The C-56 co-location echo applied to every YAML template field, converting the production schema into a locally self-contained authoring guide where each field carries its governing rule.

---

```json
{"top_score": 335, "all_essential_pass": true, "new_patterns": ["dual-site active verification echo -- the active NOT/IS verification checklist (C-55, at the protocol declaration site) is also echoed at the Component 1 header (application site) as a Verify-before-finalizing instruction, extending C-56's co-location discipline from static mandate/NOT-list to the active verification protocol itself, making per-item format checks fire at both the declaration site and the instantiation site independently so document-skip behavior does not bypass the verification trigger"]}
```
