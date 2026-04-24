Written to `simulations/quest/golden/corps-rob-variate-R11-2026-03-17.md`.

---

**R11 summary**

The audit of V-05 R10 found three unguarded positions -- all prose slots or derivation steps that produce conclusions without a typed citation or grounding obligation:

| Variation | Axis | What it closes |
|-----------|------|----------------|
| V-01 | Synthesis F-IDs in Handoff Packet | Cross-Stage Synthesis prose characterizes forwarded patterns without naming the F-IDs it synthesizes; typed field requiring ≥2 F-IDs from the Forwarded table |
| V-02 | Risk Shift Source F-ID in Handoff Packet | Downstream Risk Shift prose names net-new failure modes without grounding them in a finding; typed field requiring exactly one current-stage F-ID |
| V-03 | STAGE VERDICT AGGREGATE in ROB Summary | Overall Verdict is derived editorially from six stage verdicts; typed table with one row per stage, Governing F-ID per verdict, Propagation flag, and explicit worst-verdict-wins aggregation rule |
| V-04 | V-01 + V-02 | Both Handoff Packet prose positions -- backward citation (synthesis) and forward citation (risk shift) -- completed in the same packet structure |
| V-05 | V-01 + V-02 + V-03 | Full structural closure: Handoff Packet citation-complete, Overall Verdict derivable end-to-end from finding → risk register → stage verdict → aggregate → overall |

**Design note:** V-01 and V-02 are structurally complementary within the same artifact. Synthesis F-IDs cites backward (from the Forwarded table into the synthesis prose); Risk Shift Source F-ID cites forward (from this stage's findings into the risk assertion). Together they complete the citation architecture within the Handoff Packet itself -- the only artifact in the ROB that previously had a typed sender table but unconstrained prose commentary on it.

V-03 follows the same pattern as VERDICT CALIBRATION at the stage level but applies it at the summary level: converting an editorial synthesis step into a derivable result with a pre-stated aggregation rule.
