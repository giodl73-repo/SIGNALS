Written to `simulations/quest/golden/program-plan-variate-R17-2026-03-16.md`.

---

**R17 summary — five complete prompt bodies targeting C-52 and C-53:**

| Variate | Protocol | Axis | C-50 | C-51 | C-52 | C-53 | Anticipated |
|---------|----------|------|------|------|------|------|-------------|
| **V-01** | SCAN PROTOCOL | Output format (4-column table carry-forward) | YES | NO | NO | NO | 310/320 |
| **V-02** | BOUNDED BLOCK PROTOCOL | Role sequence (protocol-first carry-forward) | NO | YES | NO | NO | 310/320 |
| **V-03** | MANDATE VERIFICATION PROTOCOL | Phrasing register (SHALL/MUST throughout) | NO | NO | NO | NO | 300/320 |
| **V-04** | ZONE LOCK PROTOCOL | Lifecycle emphasis (per-phase zone lock declarations at Step 2) | NO | NO | NO | NO | 300/320 |
| **V-05** | BOUNDED BLOCK PROTOCOL | Combined C-50+C-51+C-52+C-53 | YES | YES | YES | YES | 320/320 |

**C-52/C-53 mechanism in V-05:** The BOUNDED BLOCK PROTOCOL section (first in document, C-51) contains an explicit "FORMAT REQUIREMENT" subsection for Component 1 that:
1. States "Component 1 MUST be a 4-column pipe-delimited table" — directive language satisfying C-53
2. Enumerates all four column purposes (field type / criterion / tag string / C-42 back-ref) — schema pre-declaration satisfying C-52
3. Adds "Any other format is a protocol violation" — converts C-50 from structural observation to mandated requirement

The delta from R16 V-05: R16 said *"The BAD PLAN header is a 4-column pipe-delimited table. Columns: [table]"* (descriptive, C-52 pass only). R17 says *"Component 1 MUST be a 4-column pipe-delimited table. Format requirement... Any other format is a protocol violation."* (prescriptive, C-52 + C-53 pass).
