Scorecard written to `simulations/quest/scorecards/prove-websearch-scorecard-R3-2026-03-14.md`.

---

## prove-websearch R3 Results

**Top score: 116/116** (V-04 and V-05 tied)
**All essential pass: true** (all 5 variations)

| V | Score | Gap |
|---|-------|-----|
| V-01 | 112 | C-11 FAIL, C-18 FAIL |
| V-02 | 115 | C-17 PARTIAL only |
| V-03 | 114 | C-17 PARTIAL, C-18 PARTIAL |
| V-04 | **116** | none |
| V-05 | **116** | none |

**New patterns from top scorers:**

1. `rules-block-violation-consequence` — Rule 6 in the RULES block with "no exceptions" + "omitting is a Rule 3 violation" closes C-17 where gate-embedded language leaves a borderline reading. RULES-level placement + named consequence = no conditional escape.

2. `verdict-field-precedes-synthesis` — Standalone `Null-Attack Verdict: [YES / NO / INCONCLUSIVE]` as the first PHASE 4 field (before Convergence) forces a binary verdict artifact before synthesis sub-fields are written. Closes C-18 structurally vs embedding the verdict in a Conclusion paragraph template.

3. `pre-commit-gate-binding` (V-05 only) — GATE 0 PRE-COMMIT forces falsification event commitment before the query template is seen; GATE 1 binds Q2's target declaration to the PRE-COMMIT event (copy-forward, not independently generated). Strongest C-16 implementation.

**Key finding:** V-03 lands at 114, *below* V-02 (115). PRE-COMMIT improves C-16 but without the RULES-level C-17 fix and standalone verdict field, adding GATE 0 alone is net-negative vs V-02's simpler lifecycle change. The two closures that matter most are Rule 6 (C-17) and the verdict field (C-18) — V-04 delivers both with minimal overhead. V-05 adds PRE-COMMIT for potential live-run Q2 quality improvement.

```json
{"top_score": 116, "all_essential_pass": true, "new_patterns": ["rules-block-violation-consequence", "verdict-field-precedes-synthesis", "pre-commit-gate-binding"]}
```
e structurally skippable -- no phase checkpoint forces a stop before proceeding.

**C-17 PASS:** R-09 states "MUST be completed for every SEARCH record, unconditionally -- including when no refinement occurred" with "ran as planned" as an explicit fill-in. No conditional escape present. Normative delivery but unambiguous.

**C-18 FAIL:** SYNTHESIS has Convergence/Conflict/Conclusion only. No standalone null-attack verdict field. Frontmatter includes `null_attack_result` but that is metadata, not a synthesis-phase decision artifact.

**RFC ceiling confirmed:** Normative MUST-rules can reach 112 but cannot close C-11 (structurally requires gate blocks) and C-18 (structurally requires a standalone verdict field) without phase scaffolding.

---

### V-02 (115/116)

**C-17 PARTIAL (1 pt):** GATE 2 "every query has a refinement entry" + "ran as planned" fill-in is present and close. Does not explicitly say "no exceptions" or name omission as a violation. A strict scorer can read "refinement entry" as conditional on refinement having occurred. Missing the RULES-level unconditional mandate present in V-04/V-05.

**C-18 PASS:** Standalone `Null-Attack Verdict: [YES / NO / INCONCLUSIVE]` field in PHASE 4 before Convergence. Forces binary verdict as a dedicated artifact. Conclusion then "references the Null-Attack Verdict above -- do not re-adjudicate" -- clean separation.

**Gap from 116:** Only C-17. Closing requires either RULES-level Rule 6 (V-04) or equivalent unconditional mandate with explicit violation consequence.

---

### V-03 (114/116)

**C-16 PASS (strong):** GATE 0 PRE-COMMIT block names specific falsification event before query design. GATE 1 binds Q2 target declaration to the PRE-COMMIT event. Two-checkpoint enforcement is the strongest C-16 implementation across all variations.

**C-17 PARTIAL (1 pt):** Same GATE 2 wording as V-02 (R2 V-03 base). "Every query has a refinement entry" lacks "no exceptions" + violation consequence. Same borderline reading as V-02.

**C-18 PARTIAL (1 pt):** PHASE 3 has a `Null hypothesis verdict:` field (required by GATE 3). PHASE 4 Conclusion instruction references it as prose item "(2) whether the null hypothesis attack found the falsification event (YES/NO/INCONCLUSIVE per PHASE 3 verdict)." Verdict is required and propagated, but embedded in a paragraph template rather than rendered as a standalone PHASE 4 artifact. A model satisfies the letter by inserting a narrative sentence. Not structurally equivalent to a standalone pre-Convergence field.

**Gap from 116:** Both C-17 and C-18. V-03 demonstrates that PRE-COMMIT alone (without RULES-level C-17 fix and standalone verdict field) lands at 114, below both V-02 (115) and V-04/V-05 (116).

---

### V-04 (116/116)

**C-17 PASS:** Rule 6 in the RULES block: "MUST be completed for every SEARCH BLOCK -- no exceptions. When the original query ran unchanged, record: [...]. Omitting or skipping this field is a Rule 3 violation." Field label "(Rule 6 -- mandatory for every SEARCH BLOCK)" reinforces at point of use. RULES-level placement means the constraint is parsed before any phase template. Naming violation consequence removes all conditional reading.

**C-18 PASS:** Standalone `Null-Attack Verdict: [YES / NO / INCONCLUSIVE]` field in PHASE 4 before Convergence. Consistency check with PHASE 3 null hypothesis verdict required. Conclusion says "reference it; do not re-adjudicate here" -- verdict is a dedicated decision artifact at the synthesis level.

**Architecture:** Two targeted additions to R2 V-05 base (Rule 6 + verdict field). No PRE-COMMIT overhead. Achieves 116/116 with minimal structural change from R2.

---

### V-05 (116/116)

All criteria pass. Three R3 mechanisms combined:

**C-16 (strongest):** GATE 0 PRE-COMMIT block (before query design) + GATE 1 requiring Q2 target declaration to match PRE-COMMIT event. Adversarial commitment is front-loaded before support-framing of Q1 can prime pro-hypothesis perspective.

**C-17 PASS:** Same Rule 6 mechanism as V-04. RULES-level, no exceptions, violation consequence named.

**C-18 PASS:** Same standalone verdict field as V-04. Consistency check against PHASE 3 null hypothesis verdict.

**Additional:** Frontmatter includes `falsification_event` field (from PRE-COMMIT) -- propagates the pre-committed falsifier to the output artifact for auditability.

**Architecture overhead vs V-04:** PRE-COMMIT block adds ~8 lines before PHASE 1. GATE 0 adds a stop condition. Whether this produces measurably better Q2 quality in live runs is the empirical question for choosing between V-04 and V-05.

---

## Excellence Signals (R3 New Patterns)

**Pattern 1: `rules-block-violation-consequence`**
Moving the unconditional refinement mandate to the RULES block (Rule 6) with "no exceptions" + "omitting is a Rule 3 violation" eliminates the borderline reading in GATE-embedded language. RULES-level placement means the constraint is parsed before any phase template. Naming the consequence converts it from instruction to enforcement. Closes C-17 unambiguously.

**Pattern 2: `verdict-field-precedes-synthesis`**
Placing `Null-Attack Verdict: [YES / NO / INCONCLUSIVE]` as the first field in PHASE 4 (before Convergence/Conflict) forces binary rendering before convergence analysis begins. The Conclusion then references rather than re-adjudicates -- adversarial result is a standalone artifact at the decision point, not a clause in a paragraph template. Closes C-18 structurally.

**Pattern 3: `pre-commit-gate-binding`** (V-05 only)
GATE 0 PRE-COMMIT block forces falsification event commitment before query template is seen. GATE 1 requires Q2 target declaration to match the PRE-COMMIT event (copy-forward, not independently generated). Front-loads adversarial commitment at the earliest possible structural point. Strengthens C-16 beyond GATE 1-only target declaration.

---

## R3 Findings

**Both V-04 and V-05 achieve 116/116.** The ceiling was reached by two targeted additions to R2 V-05: Rule 6 (C-17) and standalone verdict field (C-18).

**V-03 underperforms V-02 (114 vs 115).** PRE-COMMIT improves C-16 but does not close C-17 or C-18. Adding GATE 0 without the RULES-level C-17 fix and standalone C-18 field is net-negative vs V-02's simpler lifecycle change.

**V-01 RFC ceiling = 112.** C-11 (structurally requires gate blocks) and C-18 (structurally requires standalone field) cannot be closed by normative MUST rules alone. If live runs show C-11 does not affect production behavior, normative architecture reaches 112 without gate overhead.

**Golden candidate selection:** V-04 achieves 116 with less structural overhead; V-05 achieves 116 with PRE-COMMIT for potentially stronger Q2 quality in live runs. Live run comparison of Q2 adversarial depth is the deciding test.

---

## Version History

| Round | Date | Top Score | Golden Candidate |
|-------|------|-----------|-----------------|
| R1 | 2026-03-14 | ~108-110 | V-05 (phase gates + target framing + tables) |
| R2 | 2026-03-14 | ~112-114 | V-03 (null attack + phase gates) |
| R3 | 2026-03-14 | 116/116 | V-04 or V-05 (pending live run) |
