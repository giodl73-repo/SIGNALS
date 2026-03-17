Written to `simulations/quest/golden/program-plan-variate-R19-2026-03-16.md`.

---

# program-plan -- R19 Variate Prompt Bodies (V-01 through V-05)

**Rubric**: v19 (C-01 through C-56, 49 aspirational criteria, 335 pts)

## Variation summary

| Variate | Protocol Name | Axis | C-50 | C-51 | C-55 | C-56 | Anticipated |
|---------|---------------|------|------|------|------|------|-------------|
| **V-01** | SCAN PROTOCOL | Output format: C-41 as 4-column pipe table | PASS | FAIL | NO | NO | 43/49 · 305/335 |
| **V-02** | BOUNDED BLOCK PROTOCOL | Role sequence: protocol section document-first | FAIL | PASS | NO | NO | 43/49 · 305/335 |
| **V-03** | UNIVERSAL VERIFICATION PROTOCOL | Universal verification: C-55 NOT/IS active checklist at every construction step | FAIL | FAIL | NO | NO | 42/49 · 300/335 |
| **V-04** | MANDATE ECHO SATURATION PROTOCOL | Mandate echo saturation: C-56 governing-rule echo at every YAML template field | FAIL | FAIL | NO | NO | 42/49 · 300/335 |
| **V-05** | BOUNDED BLOCK PROTOCOL | Full chain C-50+C-51+C-52+C-53+C-54+C-55+C-56 + dual-site active verification | PASS | PASS | PASS | PASS | 49/49 · 335/335 |

## New axes for R19

**V-03 (Universal Verification)** applies the C-55 active NOT/IS checklist pattern universally: every construction step ends with a `SELF-VERIFY` block listing forbidden forms (NOT) and the required form (IS) for that specific step. Hypothesis: per-step verification prevents error propagation -- catching wrong stage names at Step 2 before skills are selected, catching bad gate forms at Step 5a before YAML is assembled.

**V-04 (Mandate Echo Saturation)** applies the C-56 co-location echo pattern to every YAML template field: `name:` echoes its governing rule inline, `skills:` echoes catalog constraint, `gate:` echoes format requirement, `intent:` echoes interrogative mandate. Hypothesis: if every template field carries its governing rule at the application site, no field requires cross-document recall.

## V-05 potential C-57 signal

V-05 adds **dual-site active verification**: the active NOT/IS checklist is present at BOTH the declaration site (BOUNDED BLOCK PROTOCOL section, C-55) AND the application site (Component 1 header, extending C-56). The Component 1 header carries:
```
# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above      ← C-56 mandate echo
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)             ← C-56 NOT list echo  
# Verify before finalizing: NOT prose enum / NOT indented list / NOT bulleted / IS pipe table  ← NEW: active checklist at application site
```

This converts the Component 1 header from a passive mandate reminder into an active verification checkpoint -- closing the attention gap for a model that skips the protocol section entirely.
