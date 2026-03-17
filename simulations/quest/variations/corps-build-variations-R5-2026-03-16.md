Written to `simulations/quest/golden/corps-build-variate-R5-2026-03-16.md` (1594 lines).

---

## Variate R5 -- corps-build

**R4 Gap Analysis (rubric v5 lens):**

| New Criterion | Best R4 Coverage | Gap Addressed in R5 |
|---------------|-----------------|---------------------|
| C-20 BUILD-VERIFY single-purpose | R4 V-01 (97 pts): named phase, binary verdict per team | R4's phase had a stated purpose but no structural prohibition. C-20 fails when non-verdict content (CROSS-REF checks, summaries, file-count rows) accumulates inside the phase block. Fix: **SINGLE-PURPOSE GATE declaration** at phase entry that names what the block contains (N VERBATIM/DRIFT verdicts, nothing else) and makes excess content a named build error. |
| C-19 TRANSCRIPTION-RECEIPT self-correcting | R4 V-02 (99 pts): VERBATIM/REVISED per artifact + "Any REVISED -> rewrite" | R4 could detect REVISED and note the rewrite instruction, then proceed to CHART-WRITTEN without re-auditing. Fix: **PHASE-EXIT GUARD** (named TRANSCRIPTION-CLEAR) that re-audits all three receipt verdicts and refuses to emit CHART-WRITTEN until all show VERBATIM. The phase cannot exit in a REVISED state -- structural enforcement, not behavioral instruction. |

**Variation Axes:**

| Var | Axis | Primary Target |
|-----|------|----------------|
| V-01 | Lifecycle: SINGLE-PURPOSE GATE at BUILD-VERIFY entry | C-20 |
| V-02 | Output format: TRANSCRIPTION-CLEAR exit guard | C-19 |
| V-03 | Phrasing register: declarative output-forward shapes for both | C-19, C-20 |
| V-04 | Lifecycle + Output format combined | C-19 + C-20 |
| V-05 | Full integration: all 12 aspirational criteria | C-09 through C-20 |

**Key structural advances over R4:**

- **V-01**: BUILD-VERIFY entry now declares `"This phase produces exactly one output per team: a VERBATIM or DRIFT verdict. This phase contains NO file writes, NO structural checks, NO directory comparisons..."` -- the constraint is a named prohibition, not an implied expectation.
- **V-02**: TRANSCRIPTION-CLEAR is a required named block. CHART-WRITTEN is gated behind it. The receipt loop is self-closing: REVISED -> rewrite -> re-audit -> VERBATIM required before exit.
- **V-03**: Both constraints expressed as output shapes ("The BUILD-VERIFY block contains exactly N lines"), making them format constraints the model must match rather than behavioral instructions it may abbreviate.
- **V-04**: C-19 and C-20 compose without interference -- they govern different phases (WRITE-CHART vs BUILD-VERIFY) and the single-purpose gate doesn't impair the transcription loop.
- **V-05**: Slots both v5 mechanisms into the full 12-criterion architecture with explicit per-criterion attribution in the FINAL SUMMARY.
