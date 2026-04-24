Written to `simulations/quest/rubrics/quest-rubric-variate-R9-2026-03-15.md`.

---

## v9 summary

**3 new criteria** from R8 excellence signals. Aspirational denominator: `/29` → `/32`.

| ID | Criterion | Source | Distinction |
|----|-----------|--------|-------------|
| **C-38** | Point-of-production anti-pattern prohibition with corrective instruction | V-02 C-36 evidence: PROHIBITION block at each phase -- "A `Declared responsibility:` label whose content echoes the phase title... is a required rewrite" | C-36 requires action-verb content and can be satisfied by post-hoc check. C-38 requires the failure mode to be named and declared a required rewrite physically adjacent to the label production site -- the generator encounters the prohibition while writing, not after. |
| **C-39** | Named structural key uniformity auditor role with per-key result emission and phase gate | V-03 C-37 evidence: "Structural Key Uniformity Auditor: post-generation set-level scan against all 4 required keys, emits per-key results, blocks Step 3 on FAIL" | C-37 requires uniform propagation as an outcome; C-15 enforces it per-body during authorship. C-39 requires a separately named role that fires post-generation over the complete set, emits per-key pass/fail (not aggregate), and hard-gates the findings phase. |
| **C-40** | Check-step inline expected-form declaration for structural keys | V-04 C-35 evidence: Step 2A -- "Key 1 (Consistency verdict: `[CONSISTENT \| AXIS DIVERGENCE]` in Step 2B)" -- bracket form embedded at the check site | C-35 requires bracket notation at the field definition site. C-40 requires it also at the check site. Makes the check self-documenting: a generator can confirm compliance by comparing against the embedded expected form without consulting the criterion or the declaration site. |
