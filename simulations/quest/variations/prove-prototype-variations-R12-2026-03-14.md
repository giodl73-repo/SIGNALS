Saved to `simulations/quest/rubrics/prove-prototype-rubric-v12-variate-R12-2026-03-15.md`.

---

## Round 12 Variations — prove-prototype (v12 rubric, 260 pts)

**Base**: R11 V-04 (238) — C-33 (numbered CALIBRATE entry) + C-34 (competitor-labeled baseline column) on R10 V-05.
**R12 target**: Add C-35 (document manifest) + C-36 (full-chain CLOSE COMPLETE). Seed = 252.

---

### Variation axes selected

| # | Single/Combined | Axis | New criteria targeted |
|---|----------------|------|-----------------------|
| V-01 | Single | Lifecycle emphasis | C-35 only — manifest before containers |
| V-02 | Single | Output format | C-36 only — enriched terminal completion line |
| V-03 | Single (gap probe) | Lifecycle emphasis + inertia framing | Neither — probes chain-coherent handoff lines between containers |
| V-04 | Combined (seed) | Both | C-35 + C-36 simultaneously |
| V-05 | Combined + gap | Both + gap | C-35 + C-36 + checkable manifest with conformance record at CLOSE |

---

### Key structural differences

**V-01** — Adds the `## Output Contract` manifest table before `CONTAINER: DESIGN`. Four rows: container name, phases, principal purpose, expected output. No change to CLOSE COMPLETE (stays R11 V-04 style — verdict + B-00 delta only).

**V-02** — No manifest. Replaces the CLOSE COMPLETE line with a six-field cross-container audit record: `[DESIGN] hypothesis = "..."`, `[CALIBRATE] competitor + B-00 + threshold`, `[BUILD] result + delta`, `[CLOSE] verdict + prototype conclusion + counter-evidence`. Tests C-36 independently of C-35.

**V-03** — No manifest, no C-36. Instead, each CONTAINER COMPLETE line carries a *forward-reference* to the next container's input requirement: DESIGN COMPLETE says "CALIBRATE receives: hypothesis and measurement metric"; CALIBRATE COMPLETE says "BUILD receives: B-00 and Phase 3 metric"; BUILD COMPLETE says "CLOSE receives: raw result and B-00 for comparison." Gap probe — tests whether chain-coherent handoff acknowledgment is a scorable v13 surface.

**V-04** — R12 seed. Both axes combined on R11 V-04 base. Manifest (C-35) + full-chain CLOSE COMPLETE (C-36). Expected 238 + 7 + 7 = **252**.

**V-05** — V-04 base, but the manifest adds an "Expected output (verifiable at COMPLETE line)" column making each manifest row checkable against the container's COMPLETE line. The CLOSE COMPLETE adds a `manifest conformance:` field cross-verifying all four containers against their promises. Gap probe for a potential v13 criterion: "terminal line cross-verifies document manifest."

---

### Predicted scores

| Variation | C-35 | C-36 | Score |
|-----------|------|------|-------|
| V-01 | PASS | FAIL | **245** |
| V-02 | FAIL | PASS | **245** |
| V-03 | FAIL | FAIL | **238** (gap only) |
| V-04 | PASS | PASS | **252** (seed) |
| V-05 | PASS | PASS | **252** + gap signal |
