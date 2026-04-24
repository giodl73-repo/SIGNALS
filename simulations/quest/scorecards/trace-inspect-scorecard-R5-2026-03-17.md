# Quest Score — `trace-inspect` Round 5

**Rubric**: v3 (C-01 – C-14) | **Variations**: V-01 – V-05

---

## Scoring Table

**Weights**: Essential C-01–C-05 = 12 pts each (60 total) | Recommended C-06–C-08 = 10 pts each (30 total) | Aspirational C-09–C-10 = 2 pts each, C-11–C-14 = 1.5 pts each (10 total)

**Pass = full | Partial = half | Fail = 0**

| ID | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|----|------|------|------|------|------|
| C-01 | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-02 | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-03 | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-04 | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-05 | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| **Essential** | **60** | **60** | **60** | **60** | **60** | **60** |
| C-06 | 10 | PASS 10 | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 | PASS 10 |
| C-07 | 10 | PASS 10 | PASS 10 | PASS 10 | PARTIAL 5 | PASS 10 |
| C-08 | 10 | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 | PARTIAL 5 |
| **Recommended** | **30** | **25** | **20** | **20** | **15** | **25** |
| C-09 | 2 | PASS 2 | PARTIAL 1 | PARTIAL 1 | PARTIAL 1 | PASS 2 |
| C-10 | 2 | PASS 2 | PASS 2 | PARTIAL 1 | PARTIAL 1 | PASS 2 |
| C-11 | 1.5 | PARTIAL 0.75 | PARTIAL 0.75 | PASS 1.5 | PASS 1.5 | PASS 1.5 |
| C-12 | 1.5 | PARTIAL 0.75 | PARTIAL 0.75 | PASS 1.5 | PARTIAL 0.75 | PASS 1.5 |
| C-13 | 1.5 | FAIL 0 | PASS 1.5 | FAIL 0 | FAIL 0 | PARTIAL 0.75 |
| C-14 | 1.5 | PARTIAL 0.75 | PARTIAL 0.75 | PASS 1.5 | PARTIAL 0.75 | PASS 1.5 |
| **Aspirational** | **10** | **6.25** | **6.75** | **7.0** | **5.0** | **9.25** |
| **TOTAL** | **100** | **91** | **87** | **87** | **80** | **94** |

---

## Per-Criterion Evidence Notes

### Essential (all variations PASS)

**C-01 Phase completeness** — All five variations declare the four-phase structure. V-04's compression applies to Phase 1/2 setup verbosity, not phase presence; all phases exist.

**C-02 Artifact produced** — All variations inherit the explicit artifact-path mandate. V-01's "No trace artifact available" line is an invocation-scenario instruction ("use spec as reference"), not a waiver of the write requirement.

**C-03 Schema compliance** — Coverage Matrix with full {P1/P2/P3} and {SA/SG/EG/QO} declarations appears in V-01's visible text and is structurally carried by all variations; none relax the label-lock invariant.

**C-04 Gates checked** — Gate Registry (G-1/G-2/G-3) with explicit PASS/FAIL mandate is a base feature of the T3 prompt. No variation removes it.

**C-05 Verdict present** — Verdict classification rules (USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION) are base T3 structure, not modified by any variation's axis.

---

### Recommended

**C-06 SA-TO-SG promotion** (V-01/V-05 PASS; others PARTIAL)

- V-01: Execution-first ordering places the promotion decision *after* all EG-producing roles relay. Each promotion reason must cite execution-phase observations by role name. This grounds the decision in observed evidence rather than spec inference — PASS.
- V-05: Inherits V-01's execution-first ordering — PASS.
- V-02/V-03/V-04: No axis directly targets promotion quality; execution order is unspecified, so reasons may remain spec-inferred — PARTIAL.

**C-07 Per-role relays** (V-01/V-02/V-03/V-05 PASS; V-04 PARTIAL)

- V-04's explicit compression target is Phase 1/2, which includes role relay structure. "Less parsing overhead" trades relay field detail for gate focus — PARTIAL.
- All others maintain the explicit relay template (Received from, Received values, Schema 2 compliance, SA/SG gaps, Produced, EG gaps) — PASS.

**C-08 Findings table depth** (all PARTIAL)

- No variation explicitly mandates >=3 distinct findings across >=2 Source types with non-duplicate Actions. V-05's inertia framing raises general rigor motivation but does not impose a floor count. All variations rely on the executor's judgment for findings depth — PARTIAL across the board.

---

### Aspirational

**C-09 Compliance ledger** (V-01/V-05 PASS; others PARTIAL)

- V-01's visible Coverage Matrix includes VC-1 through VC-5 columns with explicit "Verdict-check" binding per schema. This mandates the compliance ledger structure — PASS.
- V-05 inherits this — PASS.
- V-02/V-03/V-04: Compliance ledger not explicitly targeted — PARTIAL.

**C-10 Sub-step transitions** (V-01/V-02/V-05 PASS; V-03/V-04 PARTIAL)

- V-01: Schema 5 sub-step table with explicit Prerequisite/Produces/Unblocks columns enforces transition sentences — PASS.
- V-02: Structured checkbox blocks require explicit "prerequisite confirmed / prior-step output named" verification before each sub-step begins, which subsumes C-10's transition sentence requirement — PASS.
- V-05: Inherits V-01's Schema 5 table — PASS.
- V-03/V-04: Named gate blocks don't specifically target sub-step transitions — PARTIAL.

**C-11 Phase-entry gate-clearance summary** (V-03/V-04/V-05 PASS; V-01/V-02 PARTIAL)

- V-03: Axis explicitly names "GATE CLEARANCE SUMMARY" as a required structural block before Phase 4 — PASS.
- V-04: Lifecycle emphasis is the primary axis; the compressed preamble frees attention for gate work, and the hypothesis specifically claims "high-ceremony gate work" — PASS.
- V-05: Explicitly names GATE CLEARANCE SUMMARY as a required output — PASS.
- V-01/V-02: Consolidated phase-entry summary not targeted; individual gate results satisfy C-04 but the consolidated block may be absent — PARTIAL.

**C-12 Gate-failure remediation loop** (V-03/V-05 PASS; others PARTIAL)

- V-03: Named REMEDIATION LOG block as required structural output — PASS.
- V-05: Mandatory C-12 EXEMPTION notice when all gates pass on first eval; remediation loop as named block when any gate fails — PASS. This is the only variation that makes the *absence* of a failure explicitly visible rather than relying on silence.
- V-01/V-02/V-04: Remediation not specifically targeted as a named output block — PARTIAL.

**C-13 Sub-step prerequisite checkboxes** (V-02 PASS; V-05 PARTIAL; others FAIL)

- V-02: Entire axis targets this criterion — named-artifact checkbox blocks at the opening of each sub-step. "Bare YES without a named referent fails" is precisely the rule V-02 enforces by format — PASS.
- V-05: Multi-axis approach includes structural blocks but does not specifically introduce a checkbox format for sub-step prerequisites. Inertia framing may motivate named referents but doesn't structurally enforce them — PARTIAL.
- V-01/V-03/V-04: No checkpoint format targeting this criterion — FAIL.

**C-14 Remediation-to-summary coherence** (V-03/V-05 PASS; others PARTIAL)

- V-14 only evaluable when both C-11 and C-12 are present.
- V-03: Both C-11 and C-12 pass; named structural blocks for each make the coherence requirement enforceable — PASS.
- V-05: Both C-11 and C-12 pass; named blocks + EXEMPTION notice make the gate state traceable from remediation to summary — PASS.
- V-01/V-02: C-11 or C-12 at PARTIAL; coherence between them is not formally enforced — PARTIAL.
- V-04: C-12 at PARTIAL; coherence not guaranteed — PARTIAL.

---

## Ranking

| Rank | ID | Score | Golden? | Winning axis |
|------|----|-------|---------|--------------|
| 1 | **V-05** | **94** | YES | Multi-axis: inertia framing + execution-first + named GATE CLEARANCE SUMMARY + mandatory C-12 EXEMPTION notice |
| 2 | **V-01** | **91** | YES | Execution-first ordering grounds SA-TO-SG promotion decisions in execution evidence |
| 3 | **V-03** | **87** | YES | Named structural blocks enforce C-11/C-12/C-14 as required outputs |
| 4 | **V-02** | **87** | YES | Checkbox format closes C-13 gap (named-artifact verification) |
| 5 | **V-04** | **80** | BORDERLINE | Conversational compression improves gate attention but sacrifices C-07 relay detail |

---

## Excellence Signals from V-05

Three design decisions drove V-05 to 94 and separated it from the field:

**1. Mandatory exemption notice (C-12 gap closure)**
Making C-12 *visible when exempt* — "C-12 EXEMPTION APPLIES: all gates passed on first evaluation" — is more rigorous than relying on silence. Without this, a reviewer cannot distinguish "no failure, nothing to document" from "forgot to check." This pattern is already in the rubric text of C-12 but V-05 is the first variation to enforce it at the prompt level as a required output.

**2. Named structural blocks as required outputs, not narrative inference**
V-05 treats GATE CLEARANCE SUMMARY and REMEDIATION LOG as named sections the trace must emit, not conclusions the reader infers from the gate-check paragraphs. This moves C-11/C-12/C-14 from "emergent from competent writing" to "structurally mandated." The distinction matters: C-04 can PASS (individual gate results present) while C-11 FAILs (no consolidated summary). Named blocks close that gap.

**3. Execution-first ordering as evidence grounding for C-06**
V-01 introduced execution-first ordering; V-05 inherits it. The promotion decision becomes verifiable: did the execution pass actually surface the gap or resolve it? A promotion reason that says "execution likely resolves this" fails when the execution pass is run first because the evidence is observable. This makes C-06 harder to satisfy lazily — and therefore more valuable when it passes.

---

## New Rubric Patterns

No new patterns extracted. Round 5 confirms the rubric v3 is well-calibrated:

- The only remaining systematic gap is **C-08** (findings depth), which no variation closed. C-08 requires >=3 distinct findings across >=2 Source types with non-duplicate Actions. No prompt formulation tested in this round mandates a floor count. This is a known open criterion, not a newly discovered one.
- The C-11 × C-12 × C-14 cluster is now structurally addressable via named blocks (V-03/V-05 demonstrate this). No new interaction criterion emerges beyond C-14.
- V-05's EXEMPTION notice pattern is already in the rubric text of C-12; it needed prompt-level enforcement, not a new criterion.

---

```json
{"top_score": 94, "all_essential_pass": true, "new_patterns": []}
```
