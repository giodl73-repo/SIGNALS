Written to `simulations/quest/golden/trace-inspect-variate-R2-2026-03-17.md`.

---

## trace-inspect -- Variations v2 R2 (2026-03-17)

**Entry state summary**: R1 established C-01 through C-10 PASS. The v2 rubric adds three new aspirational criteria. All three are FAIL in R1's best output.

---

### Variation axis selection

| Axis | Label | Targets | Hypothesis |
|------|-------|---------|------------|
| A | Lifecycle emphasis | **C-11** | Add explicit Gate Clearance Summary blocks at two phase boundaries (before Step 3d, before Phase 4). Each block names all three gates and states the composite entry verdict. Distinct from C-04 (individual results) and C-10 (transition sentences). |
| B | Lifecycle emphasis | **C-12** | Add structured remediation loop template triggered on FAIL gates. Three required fields: defect identified, action taken (specific finding ID or text), re-check result. When all gates pass on first evaluation, emit an explicit exemption notice. |
| C | Output format | **C-13** | Add prerequisite verification checkboxes opening each Phase 3 sub-step BEFORE the sub-step body. Each checkpoint states the named prerequisite condition and a YES/NO resolution. Stronger than C-10: fires prospectively before the step, not retrospectively after the prior step. |

---

### Variation inventory

| Variation | Single axis | Combined axes | C-11 target | C-12 target | C-13 target |
|-----------|------------|---------------|-------------|-------------|-------------|
| V-01 | A (C-11) | -- | Gate Clearance Summary at Step 3c and Phase 4 boundary | -- | -- |
| V-02 | B (C-12) | -- | -- | Remediation loop sub-blocks per gate; exemption notice for all-first-pass | -- |
| V-03 | C (C-13) | -- | -- | -- | Prerequisite checkboxes opening Steps 3a, 3b, 3c, 3d |
| V-04 | -- | A + B | Gate Clearance Summary | Remediation loop + exemption notice | -- |
| V-05 | -- | A + B + C | Gate Clearance Summary | Remediation loop + exemption notice | Prerequisite checkboxes |

---

### Key design decisions

**C-11 placement**: Two locations -- one inside Step 3c (after all individual gate checks and any remediation loops), one at Phase 4 entry. The Step 3c summary covers "is Step 3d valid?" The Phase 4 summary covers "is Phase 4 valid?" Together they satisfy C-11's requirement for a consolidated summary "before Step 3d begins and before Phase 4 begins."

**C-12 exemption notice**: When all gates pass on first evaluation, the trace emits an explicit "C-12 exemption applies" notice. This is intentional: it prevents a reviewer from marking C-12 FAIL on a trace that correctly has no remediation loops (because no gates failed). The rubric specifies "exempt" for this case.

**C-13 vs C-10 separation**: C-10's transition sentences appear at the END of a step as carry-forward confirmation. C-13's prerequisite checkboxes appear at the TOP of the NEXT step as entry verification. V-03 and V-05 use a named-artifact form for the YES check (e.g., "name the specific row from Step 3a confirming the legend exists") to prevent mechanical YES answers.

**V-05 temporal bracket**: The three additions form a temporal structure that surrounds gate execution. C-13 fires before the step (entry verification), C-12 fires within the gate step (correction on FAIL), C-11 fires after all gates (composite exit verdict). Each addition closes a distinct visibility gap without overlapping the others' scope.
