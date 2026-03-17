# Scorecard — mock-accept · Round 4 · Rubric v4

**Skill:** mock-accept
**Date:** 2026-03-17
**Rubric:** v4 (denominator 14; C-09 N/A cascade not triggered — C-09 present in all variations)
**Baseline:** R3 champion V-04 at 98.0 · passes C-09–C-13, C-15–C-17 · fails C-14, C-18 · C-19–C-22 unscored

---

## Stable Criteria — All Variations

The following criteria are identical across all five variations (inherited from the passing baseline unchanged). Brief shared evidence from V-01 specimen:

| ID | Criterion | All Variations | Evidence |
|----|-----------|---------------|----------|
| C-01 | Auto-flag rules | **PASS** | Rule A/B/C each produce unconditional artifact-as-subject statements with `___` namespace slot; no `"I found…"` language |
| C-02 | Forbidden triad | **PASS** | All three trigger levels named; completeness guard: "A two-of-three set does not satisfy this gate" present |
| C-03 | Status writeback + Canary | **PASS** | Phase 4 Edit tool call per namespace; CANARY ASSERTION present; CANARY-FALSE-POSITIVE named; CANARY SUPPRESSED branch defined |
| C-04 | Review artifact structure | **PASS** | Phase 6 single Write block with "All sections in ONE Write call. No orphaned sections." Baseline Phase 6 inherited (Coverage table / Structural records / Risk / Next Steps present from R3 passing spec) |
| C-05 | MOCK-ACCEPTED positive argument | **PASS** | Slot 1 and Slot 2 separate; Slot 1 has exact-token CONSTRAINT; paraphrase explicitly named as violation; revert instruction present in both slots |
| C-06 | Entity-naming in roles | **PASS** | Required artifact citation template names `[field: X, token: Y, slot: Z]` verbatim in Phases 2 and 3 |
| C-07 | Step sequencing + guard compliance | **PASS** | Arch-blocked and Strategy-blocked accumulators named; empty-list statement required ("Write 'Arch-blocked: none' if list is empty") |
| C-08 | Eval-driven REAL-REQUIRED template | **PASS** | All 5 fields present in Phases 2 and 3: trigger condition · SQ (with own CONSTRAINT) · artifact state · verdict · required action; VERDICT-ECHO named |
| C-09 | Artifact-as-subject grammar | **PASS** | STANDING RULE at top; PASS form defined; 4 FAIL forms enumerated; halt-and-rewrite enforcement active every phase |
| C-10 | Tier sourcing | **PASS** | Phase 0: `"Tier: ___"` with CONSTRAINT `"Write exactly 'Tier: N (source: TOPICS.md | --tier | default)'"` |
| C-11 | Inline completeness gate | **PASS** | GATE A–E each carry N+M=total count assertion with halt condition before phase transition |
| C-12 | Reason-code enforcement at point of use | **PASS** | CONSTRAINT `"Write exactly STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT"` co-located at each Reason field in Phases 2, 3, 4, 5 |
| C-13 | Phase exit assertions | **PASS** | All five gates include `"Do not proceed to Phase N until [GATE] is written"` with count; blocks interleave |
| C-15 | Forbidden-form enumeration | **PASS** | Standing Rule enumerates 4 specific forbidden forms: `"I found…" / "This namespace has…" / "There is no…" / "Coverage shows…"` |
| C-16 | Written-gate blocking language | **PASS** | Every gate includes `"Do not proceed to Phase N until [GATE] is written"` |
| C-17 | Named gate registry | **PASS** | GATE A, B, C, D, E — stable sequential IDs referenceable across phases |

---

## Differentiating Criteria — Per Variation

### V-01 — Output Format: Universal Blank-Slot + Constraint Co-location

| ID | Verdict | Evidence |
|----|---------|---------|
| C-14 | **PASS** | All fill-in targets converted to `___` throughout Phases 0–5: `"Topic: ___"`, `"Namespace: ___"`, `"SQ: ___"`, `"Status: ___"`, etc. No `[bracket]` placeholders remain |
| C-18 | **PASS** | Each constrained field followed immediately by a framed `CONSTRAINT:` line: `"SQ: ___\n  CONSTRAINT: Write 'Does the mock artifact's [namespace] section…'"` — no intervening prose |
| C-19 | **PASS** | Auto-flag Rule A/B/C templates use `___` for namespace slot: `"The mock artifact's ___ section is absent."` CANARY ASSERTION: `"Status fields written: ___."`  — structurally visible blanks throughout |
| C-20 | **PASS** | Standing Rule: `"If output contains a forbidden form, halt and rewrite before advancing"` — halt (stop) + rewrite (action) both named. Borderline: not three-step explicit, but criterion satisfied |
| C-21 | **FAIL** | Phase 6 not addressed in this axis; baseline Phase 6 lacks per-section CONSTRAINT blocks; each review section does not carry its own co-located CONSTRAINT |
| C-22 | **PASS** | Slot 1 revert: `"Paraphrase ('sufficient coverage', 'domain realistic') — delete and rewrite with the exact token"` — two quoted altered-token examples present |

**Aspirational:** 13/14 · (13/14) × 10 = **9.3**
**Total: 60 + 30 + 9.3 = 99.3**

---

### V-02 — Lifecycle: Per-Section CONSTRAINT in Phase 6

| ID | Verdict | Evidence |
|----|---------|---------|
| C-14 | **FAIL** | Phases 0–5 unchanged from V-04 baseline — `[bracket]` notation retained throughout; blank-slot structural visibility absent |
| C-18 | **FAIL** | CONSTRAINT blocks remain inline within template phrasing; no framed adjacent CONSTRAINT lines in Phases 2/3 |
| C-19 | **FAIL** | Auto-flag templates retain `[namespace]` bracket form; CANARY uses bracket notation; fill-in sites not structurally visible by inspection |
| C-20 | **PASS** | Inherits baseline Standing Rule `"halt and rewrite before advancing"` — borderline pass same as V-01 |
| C-21 | **PASS** | Phase 6 gains per-section CONSTRAINT block immediately after each section name (Coverage, Structural records, Risk, Next Steps); GATE F cites specific section IDs |
| C-22 | **PASS** | Phase 5 unchanged from baseline; Slot 1 revert retains two quoted paraphrase examples |

**Aspirational:** 11/14 · (11/14) × 10 = **7.9**
**Total: 60 + 30 + 7.9 = 97.9**

---

### V-03 — Phrasing Register: Halt Naming + Paraphrase Examples

| ID | Verdict | Evidence |
|----|---------|---------|
| C-14 | **FAIL** | Phases 0–5 unchanged from baseline — `[bracket]` notation retained; structural visibility absent |
| C-18 | **FAIL** | CONSTRAINT blocks remain inline; no framed adjacent CONSTRAINT lines |
| C-19 | **FAIL** | Auto-flag templates retain bracket form; CANARY bracket notation unchanged |
| C-20 | **PASS** | Standing Rule rewritten as: `"HALT. Delete the violating line. Rewrite in PASS form."` — unambiguous three-step action sequence; no evaluator ambiguity |
| C-21 | **FAIL** | Phase 6 unchanged from baseline; no per-section CONSTRAINT blocks in review artifact |
| C-22 | **PASS** | Slot 1 gains third example (`"coverage sufficient"`); Slot 2 revert shifts from forbidden-form labeling to near-miss paraphrase examples; all examples are quoted altered-token forms |

**Aspirational:** 10/14 · (10/14) × 10 = **7.1**
**Total: 60 + 30 + 7.1 = 97.1**

---

### V-04 — Combined: Output Format + Lifecycle (C-14/C-18/C-19 + C-21)

| ID | Verdict | Evidence |
|----|---------|---------|
| C-14 | **PASS** | V-01 blank-slot changes applied across Phases 0–5; all fill-in targets use `___` |
| C-18 | **PASS** | V-01 CONSTRAINT co-location applied in Phases 2/3/4; framed CONSTRAINT: lines immediately follow each constrained field |
| C-19 | **PASS** | V-01 universal blank-slot: auto-flag templates and CANARY use `___`; structurally visible throughout |
| C-20 | **PASS** | Baseline Standing Rule `"halt and rewrite before advancing"` — borderline pass; V-03 phrasing not included |
| C-21 | **PASS** | V-02 Phase 6 per-section CONSTRAINT blocks applied; non-overlapping surface with V-01 Phases 0–5 changes |
| C-22 | **PASS** | Baseline Phase 5 paraphrase examples inherited; two quoted altered-token forms in Slot 1 revert |

**Aspirational:** 14/14 · (14/14) × 10 = **10.0**
**Total: 60 + 30 + 10.0 = 100.0**

---

### V-05 — Full Stack: All Four New Criteria + C-14/C-18

| ID | Verdict | Evidence |
|----|---------|---------|
| C-14 | **PASS** | V-04 blank-slot structure throughout; all fill-in targets use `___` |
| C-18 | **PASS** | V-04 CONSTRAINT co-location; framed CONSTRAINT: lines in all constrained phases |
| C-19 | **PASS** | V-04 universal blank-slot; auto-flag templates and CANARY confirmed `___` |
| C-20 | **PASS** | V-03 explicit HALT sequence: `"HALT. Delete the violating line. Rewrite in PASS form."` — unambiguous, three-step; no borderline qualifier needed |
| C-21 | **PASS** | V-04 Phase 6 per-section CONSTRAINT blocks; GATE F present |
| C-22 | **PASS** | V-03 extended paraphrase: three Slot-1 examples + two near-miss Slot-2 examples; both slots carry concrete altered-token evidence |

**Aspirational:** 14/14 · (14/14) × 10 = **10.0**
**Total: 60 + 30 + 10.0 = 100.0**

---

## Score Summary

| Variation | Axis | Essential | Recommended | Aspirational | **Total** | C-20 quality |
|-----------|------|-----------|-------------|--------------|-----------|--------------|
| V-04 | output-format + lifecycle | 60 | 30 | 10.0 (14/14) | **100.0** | borderline |
| V-05 | full stack | 60 | 30 | 10.0 (14/14) | **100.0** | unambiguous |
| V-01 | output-format | 60 | 30 | 9.3 (13/14) | **99.3** | borderline |
| V-02 | lifecycle | 60 | 30 | 7.9 (11/14) | **97.9** | borderline |
| V-03 | phrasing-register | 60 | 30 | 7.1 (10/14) | **97.1** | unambiguous |

---

## Rankings

1. **V-05** — 100.0 · all 14 aspirational pass · C-20 and C-22 unambiguous (recommended for adoption)
2. **V-04** — 100.0 · all 14 aspirational pass · C-20 borderline (structurally complete; phrasing gap)
3. **V-01** — 99.3 · only C-21 failing · largest single-axis gain this round
4. **V-02** — 97.9 · C-21 pass + C-20/C-22 pass · C-14/C-18/C-19 remain structural gaps
5. **V-03** — 97.1 · C-20/C-22 unambiguous pass · four aspirational gaps remain

**V-04 and V-05 tie numerically at 100.0.** V-05 is the preferred champion because its C-20 halt sequence is free of qualifier risk and its extended Slot-2 near-miss paraphrase examples close the last ambiguous edge in C-22.

---

## Excellence Signals

The V-05 patterns that drove the ceiling:

1. **Non-overlapping surface strategy** — V-01 covers Phases 0–5 structure (blank-slot + CONSTRAINT co-location), V-02 covers Phase 6 structure (per-section CONSTRAINT), V-03 covers phrasing register (halt sequence + paraphrase examples). The three axes address different spec surfaces; combining them in V-05 achieves full aspirational coverage with no structural interference or regression risk.

2. **Universal blank-slot extends to output templates, not only evaluator fill-ins** — applying `___` to the auto-flag Rule A/B/C namespace slot and the CANARY count slot makes C-19 pass without any special-casing. The criterion is satisfied by the same mechanical substitution that fixes C-14.

3. **Explicit named action sequence in halt instruction** — `"HALT. Delete the violating line. Rewrite in PASS form."` removes the borderline qualifier on C-20. Three distinct steps (stop, delete, rewrite) leave no interpretive gap for an evaluator who might read `"halt and rewrite"` as advisory rather than imperative.

4. **Per-section CONSTRAINT co-location in Phase 6** — placing a CONSTRAINT block immediately after each section name in the review Write block (C-21) applies the same pattern proven in Phases 2/3 to the review artifact; consistency across all Write surfaces eliminates a class of compliance drift.

5. **Near-miss paraphrase examples in Slot-2 revert** — shifting Slot 2 from `"Forbidden form ('I found…')"` to quoted near-miss paraphrase examples tightens C-22 and symmetrizes the revert pattern across both slots. Evaluators can detect Slot-2 violations by comparison rather than by class-label lookup.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["universal blank-slot enforcement extends to auto-flag output templates and CANARY count slot, not only evaluator fill-in fields", "explicit HALT + delete + rewrite action sequence removes borderline qualifier on C-20", "near-miss paraphrase examples in Slot-2 revert symmetrize C-22 coverage across both slots"]}
```
