Written to `simulations/quest/rubrics/trace-component-rubric-v16-variate-R16-2026-03-15.md`.

---

# trace-component — Round 16 Variations

**Variation axes used:**
- Single-axis: Role sequence (V-01), Output format (V-02), Lifecycle emphasis (V-03)
- Combined: Role sequence + Output format (V-04), All three + Phrasing register (V-05)

---

## Variation Summary

| Var | Axis | C-49 Named Registers | C-50 Per-Register Close | C-51 Successor Naming | Expected |
|-----|------|---------------------|------------------------|----------------------|---------|
| V-01 | Role sequence | YES — NULL/DEPARTURE section headers | no — single CAUSAL PHASE CLOSE | no — terminal position only | ~172-173 |
| V-02 | Output format | no — single undivided block | no | YES — "TABLE-N header follows directly below" | ~172-173 |
| V-03 | Lifecycle emphasis | YES | YES — NULL REGISTER CLOSE + DEPARTURE REGISTER CLOSE | no | ~173-174 |
| V-04 | Role sequence + Output format | YES | no | YES | ~173-174 |
| V-05 | All three + Phrasing register | YES | YES | YES + Phase Contracts | ~174-176 |

---

## Key structural deltas

**C-49 isolation (V-01):** Adds `**NULL REGISTER**` and `**DEPARTURE REGISTER**` section headers as named document elements within CAUSAL PHASE. No `NULL REGISTER CLOSE` line — the transition is the heading itself. Tests whether labeled sections alone satisfy C-49 without gating the boundary.

**C-51 isolation (V-02):** Manifest close cue changes from `"verbatim, as this manifest's terminal line. Reproduce now."` to `"verbatim. This is the last content line of MANIFEST-N. TABLE-N header follows directly below. Reproduce now."` across all 5 manifests. No register subdivision in CAUSAL PHASE. Tests C-51 independently of causal-phase structure.

**C-49+C-50 (V-03):** Full register close chain: `NULL REGISTER CLOSE` gates the NULL→DEPARTURE boundary; `DEPARTURE REGISTER CLOSE` gates the DEPARTURE→SCHEMA boundary (serving as both register-level and phase-level close). Manifest closes remain terminal-position only. Tests whether the register-close chain satisfies C-50 given C-49 precondition.

**C-49+C-51 (V-04):** Named register headers (C-49, no per-register close) combined with TABLE-N successor naming in all manifest closes (C-51). Tests whether C-49+C-51 creates emergent pressure toward C-50.

**C-49+C-50+C-51 (V-05):** Full R16 expression. Phase Contracts from R15 V-05 carried through. Close-line text carries two simultaneous assertions: `"This is the last content line of MANIFEST-N. TABLE-N header follows directly below."` The unifying principle: every structural boundary — register-to-register, manifest-to-table — requires both an identity assertion (what this closes) and a successor assertion (what must follow next).
