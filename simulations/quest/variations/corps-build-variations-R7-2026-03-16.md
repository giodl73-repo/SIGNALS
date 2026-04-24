Written to `simulations/quest/golden/corps-build-variate-R7-2026-03-16.md`.

---

## Variate R7 -- corps-build

**5 variations targeting C-22 and C-23 under rubric v7.**

---

### R6 Gap Analysis (rubric v7 lens)

| Criterion | Gap |
|-----------|-----|
| **C-22** Named binary path structure | V-01/V-02/V-04 R6 define PATH-A/PATH-B as instruction-level section headers. No variation explicitly instructs the model to emit `PATH-A` or `PATH-B` as an output token at the moment the path fires. A model executing PATH-B correctly may never print "PATH-B" in WRITE-CHART output -- only in FINAL SUMMARY. C-22 pass condition requires the label at execution point. |
| **C-23** Declarative block-shape correctness rules | V-03 R6 passes C-23 (has "a BUILD-VERIFY block with non-verdict content is structurally invalid"; "a TRANSCRIPTION-CLEAR that names fewer than three artifacts is structurally incomplete") but got C-08 PARTIAL -- AMEND section had no block-shape correctness rule. V-01/V-02/V-04 use procedural framing throughout; no "a correct X is..." rules adjacent to block definitions. |

---

### Variation Axes

| Axis | Variation |
|------|-----------|
| C-22 single: PATH-A/PATH-B label emitted as explicit output token at execution point | V-01 |
| C-23 single: declarative block-shape correctness rules adjacent to all named blocks | V-02 |
| C-23 narrow fix: AMEND correctness rule added to R6 V-03 declarative architecture | V-03 |
| C-22 + C-23 combined on R6 V-02 step architecture | V-04 |
| Full integration: PROFILE-before-CONTRACT + PATH label emission + correctness rules | V-05 |

---

### Key Design Decisions

**V-01 (C-22 axis):** One addition to R6 V-01: after TRANSCRIPTION-RECEIPT, the prompt explicitly instructs `emit CHART-PATH: PATH-A` or `emit CHART-PATH: PATH-B` before executing the path. FINAL SUMMARY traces `[CHART-PATH: PATH-A -- ... | CHART-PATH: PATH-B -- ...]`. The label becomes an observable output token, not just a structural heading.

**V-02 (C-23 axis):** Each named block (PROFILE, IA-WRITTEN, TRANSCRIPTION-RECEIPT, TRANSCRIPTION-CLEAR, BUILD-VERIFY, AMEND, CROSS-REF) gets an adjacent declarative correctness rule in "a correct X contains..." form with a named invalidity condition ("a BUILD-VERIFY block with any content other than per-team VERBATIM/DRIFT entries is structurally invalid").

**V-03 (C-23 narrow fix):** R6 V-03 (stage-based declarative framing, 95 pts) with one addition: a declarative AMEND correctness rule specifying the three option shapes with org.yaml value placeholders. Shape A / Shape B framing satisfies C-22 (named path equivalents).

**V-04 (C-22 + C-23):** R6 V-02's step architecture (strongest PATH-A/PATH-B output shape design) + `CHART-PATH:` emission instruction + declarative correctness rules for all seven named blocks.

**V-05 (full integration):** R6 V-04's phase ordering (PROFILE before CONTRACT -- deepest C-16 coverage) + `CHART-PATH:` emission + declarative correctness rules for all blocks including AMEND. Phase sequence preserves C-13 (WRITE-CHART before WRITE-ROLES).
