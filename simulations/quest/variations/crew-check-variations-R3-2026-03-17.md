`crew-check-variate-R3-2026-03-17.md` written.

---

## crew-check — Variate R3 summary

**Design intent**: R2 floor held (C-11 lens-anchor, C-12 severity contract, C-13 challenger-first present in all five variations). New axes target the three v3 additions.

| Variation | Axis | v3 criteria targeted | Key structural bet |
|-----------|------|---------------------|--------------------|
| V-01 | Readiness-gate framing | C-14 | Every transition is a readiness assertion, not a rule. "You are not ready until X" is the idiom everywhere — lens anchor, named surface, severity value, recommendation location all expressed as gates, not instructions. |
| V-02 | Hard-halt execution gate | C-16 | Named halt registry defined upfront; four gate levels: G1 (registry), G4 lens, G4 severity, G4 location, G5 empty matrix. Every failure produces the exact message from the registry. |
| V-03 | Phrasing register — interrogative | softer C-14+C-16 | Skill structured as diagnostic questions (Q1–Q5). Models answering "what does this role actually care about?" may engage more genuinely with orientation content than models executing "quote one line." Softer gates, no formal halt messages. |
| V-04 | Readiness-gate + Hard-halt | C-14 + C-16 | Gate stack with two reinforcing properties: readiness framing changes the internal state question; hard halts make every failure visible and named. Severity sort included as a natural consequence (C-15 bonus). |
| V-05 | Readiness-gate + Hard-halt + Severity-sorted | C-14 + C-16 + C-15 | Full R3 integration. Sort gets its own halt condition (HALT [G5]) — a matrix that cannot be sorted has inconsistent severity values, surfacing calibration failure at render time. A run that reaches AMEND has passed all three. |

**Axis not explored in R3** (covered in R1/R2): inertia framing (R2 V-01/V-04), severity-sorted as primary axis (R2 V-03), coaching voice register (R2 V-02), phase-gated lifecycle (R1 V-03/R2 V-05), SHALL-language formal register (R1 V-04).
