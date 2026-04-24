Written to `simulations/quest/golden/quest-rubric-variate-v10-R10-2026-03-16.md`.

---

## quest-rubric Variate — v10, Round 10

**Target criterion:** C-29 — AUDITOR-PRE pre-declaration of PARTIAL-CONDITION boundary

**What drives each variation:**

| Variation | Axis | C-29 mechanism | Key structural feature |
|-----------|------|---------------|----------------------|
| **V-01** | Role sequence | Batch AUDITOR-PRE PHASE before Phase 2; register locked; Author reads fixed input | Pre-Declaration Register table + verbatim Partial condition field |
| **V-02** | Lifecycle emphasis | Per-criterion forward gate: AUDITOR-PRE block required before each pass condition; phase-exit audit | Inline AUDITOR-PRE blocks + STOP CONDITION at per-criterion boundary |
| **V-03** | Phrasing register | Conversational "Partial credit (0.5) applies when..." field; no formal block naming or phase boundary | Six-field criterion with partial-credit sentence ordered before pass condition |
| **V-04** | Role sequence + lifecycle | Batch register (V-01) + per-criterion inline gate (V-02) simultaneously; REGISTER REVISION note required if batch entry needs correction | Both structural positions enforced; reproduction check at Phase 4 Emit |
| **V-05** | Lifecycle + output format | Per-criterion gate (V-02) + PARTIAL-CREDIT MANIFEST table in emitted document (C-NN / Partial boundary / Pass condition) | Manifest makes boundary-vs-pass-condition coherence visually scannable |

**M-07 probe design:** The ablation map isolates three independent variables — formal block naming (V-01/V-02 vs V-03), temporal position (V-01 batch vs V-02 per-criterion), and manifest format (V-02 vs V-05). If V-03 fails C-29, formal block naming is load-bearing. If V-02 boundaries are more specific than V-01, per-criterion timing is load-bearing. V-04's REGISTER REVISION mechanism is the signal for M-07 resolution.

**R10→R11 candidate:** If revisions between batch register and inline blocks are frequent and specific, the C-30 candidate is: *AUDITOR-PRE block must contain a calibration anchor (an example of 0.5 evidence) rather than a boundary statement alone.*
