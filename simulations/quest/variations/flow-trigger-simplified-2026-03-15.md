**Simplification Report**

---

## What Was Removed and Why

| Section | Words Removed | Reason |
|---------|---------------|--------|
| STRUCTURAL INVARIANT LAYER | ~120 | Redundant: 5 invariants duplicate FM-16, FM-17, FM-22, FM-21, and the Entry Schema Contract slot mandate already in the PROTOCOL PREAMBLE |
| LIFECYCLE OVERVIEW table | ~80 | Redundant summary of the 7 individual phase descriptions that follow |
| OBLIGATION REGISTRY cell verbosity | ~200 | Refutation Conditions shortened to key facts; Failure Mode cells reduced to bold label only — full explanations already in DERIVATION TEST |
| INERTIA CONTRAST: 3 extra entries removed (EXCLUSION LOG, EOR TABLE, BREACH TOKEN PROTOCOL) | ~200 | V-05 added these entries for aspirational v18 criteria (C-48, C-49); all three mechanisms are already covered by the DERIVATION TEST rows; C-39 requires only DUAL-TIME ATTRIBUTION CHAIN, which is kept |
| Forward dependency elaborative tails (all 6 phases) | ~275 | Text after each bold violation mode label elaborates consequences already implied by the label name; C-46 requires only (a) downstream dependency + (b) violation mode — not elaborative sentences |
| Redundant opening sentence | ~15 | "No phase SHALL begin until all prior phases have issued their required outputs" duplicates "Each phase SHALL be declared complete before the next SHALL begin" |
| Phase 0 Job last sentence | ~12 | "No obligation's compliance SHALL require navigation outside its row" is design rationale, not an executable instruction |
| Minor trimming | ~3 | Constraint propagation statement shortened |

**Total removed: ~905 words**

---

## Criteria Verification

| Criterion | Check | Status |
|-----------|-------|--------|
| **C-46** — all 6 phases carry dependency + violation mode | Phase 0: **pre-enumeration state collapse** ✓; Phase 1: **denominator-free enumeration** ✓; Phase 2: **post-sync state ambiguity** ✓; Phase 3: **incomplete cascade basis** ✓; Phase 4: **evidence-free anomaly verdict** ✓; Phase 5: **unevaluated trigger map** ✓; Phase 6: closing dependency statement ✓ | **PASS** |
| **C-47** — Domain Expert rows before Auditor rows + header annotation | Registry header "(Row order: Domain Expert obligations first...)" present; EOR TABLE and CASCADE DEPTH BUDGET rows precede all Auditor rows | **PASS** |
| **C-44** — 3/3 extended NOTE brackets | CLOSURE CHECK NOTE has 3 assertions all with `[must be X -- rationale clause]` form | **PASS** |
| **C-43** — REMEDIATION SELF-SUFFICIENCY as 3rd extended assertion | Third NOTE assertion: `maintained [must be maintained -- removing either attribution layer breaks self-sufficiency; this is a structural failure, not a coverage reduction]` | **PASS** |
| **C-39** — DUAL-TIME ATTRIBUTION CHAIN in INERTIA CONTRAST | Entry present with weaker alternative, failure mode, and full explanation | **PASS** |
| **C-40** — CLOSURE CHECK in code fence | Code fence with `---- NOTE:` block present | **PASS** |
| All phase structural requirements | Entry condition, job, exit condition in every phase; FM Catalog complete; Entry Schema Contract intact | **PASS** |

---

## Simplified Prompt Body

Written to: `simulations/quest/golden/flow-trigger-golden-QU5-simplified-2026-03-16.md`

```json
{"simplified_word_count": 3490, "original_word_count": 4385, "all_essential_still_pass": true}
```
