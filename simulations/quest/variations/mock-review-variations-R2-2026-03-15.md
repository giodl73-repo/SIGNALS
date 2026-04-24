**mock-review Variate R2** written to `simulations/quest/golden/mock-review-variate-R2-2026-03-15.md`.

---

## Axis-Assignment Summary

| V | Axis | Gap targeted | Hypothesis |
|---|------|-------------|------------|
| V-01 | phrasing-register | C-11: R1 V-04 had DO NOT for EVIDENCE-HEAVY only; TIER-CRITICAL and COMPLIANCE had no forbidden-output phrasing | All three rules carry an explicit DO NOT statement naming the exact forbidden output pattern; C-11 passes cleanly |
| V-02 | lifecycle-emphasis | C-12: R1 V-03 had a normative statement ("zero fields may remain"), not a required output | Write-back phase ends with a mandatory count-and-confirm line (`Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.`); C-12 is machine-checkable |
| V-03 | role-sequence | C-13: R1 V-04 had separate STEP headings but no per-role sub-questions or individual STOP gates | PM, Architect, Strategy are three separately completable sections with 3 sub-questions each, own heading, and Verdict line; C-13 fully verifiable |
| V-04 | phrasing-register + role-sequence | C-11 + C-13: both failure modes blocked simultaneously | V-01 DO NOT gates on all three auto-rules plus V-03 verifiable role steps; no inline template, no collapsed evaluation |
| V-05 | output-format + lifecycle-emphasis + role-sequence | C-09, C-12, C-13 ceiling: pre-printed skeleton | Pre-printed section headers (PM/Architect/Strategy), coverage gap synthesis paragraph, and zero-remaining count line — model fills fields rather than generating structure |

**Design note from scout-feasibility R3 applied:** pre-printed template surfaces (V-05) produce stronger structural guarantees than instruction-based approaches because the model cannot drop or reformat what it did not generate. V-05 is the predicted ceiling variation for C-09, C-12, C-13 simultaneously.
