```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explain-why-not-just-what: explaining the reason behind a constraint produces better generalization than stating the rule alone", "connective-bridges-pre-merge: requiring bridge phrases between sections before merge forces prose flow as a first-class authoring step", "anti-trivial-amendment-guard: stating that restatements do not count closes the gap between satisfying instruction and satisfying intent", "gap-first-causal-scaffold: drafting the central gap before background produces tighter semantic flow at merge time"]}
```

---

**Scorecard written** to `simulations/quest/scorecards/specify-abstract-scorecard-R1-2026-03-19.md`

### Round 1 Result — specify-abstract

| Rank | Variation | Score | Essential |
|------|-----------|-------|-----------|
| 1 | V-05 Explanatory + Connectives | **100** | ALL PASS |
| 2 | V-04 Gap-First + Inertia | **98** | ALL PASS |
| 3 | V-03 Per-Section Checks | **97** | ALL PASS |
| 3 | V-02 Compressed | **97** | ALL PASS |
| 5 | V-01 Imperative | **91** | C-05 PARTIAL |

**The single differentiator**: C-10 (coherent prose) separates V-05 from the field. V-02 through V-04 all cover the essentials well. Only V-05 has an explicit mechanism — connective bridge phrases between sections before merge — that makes prose flow a first-class output property rather than a hope.

**Four new patterns extracted** from the top two variations, all applicable to other skills in the specify and rhythm namespaces where labeled blocks must merge into prose.
| PASS 12 | PASS 12 |
| C-02 | Word count in range | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-03 | Artifact path + frontmatter | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-04 | Gap framed as gap | 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-05 | Signal acquisition | 12 | PARTIAL 6 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| C-06 | Result quantified | 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-07 | 3 distinct amendments | 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-08 | Journal variant | 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| C-09 | Claim tense | 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-10 | Coherent prose | 5 | PARTIAL 2 | PARTIAL 2 | PARTIAL 2 | PARTIAL 3 | PASS 5 |
| **Total** | | **100** | **91** | **97** | **97** | **98** | **100** |

---

## Per-Criterion Notes

### C-01 — Six Sections Present
All 5 variations enumerate all 6 sections explicitly. No variation is at risk of structural omission. The design concern raised in the hypothesis for V-02 (minimal scaffold = risk) does not materialize — the 6 parts are still enumerated by name with descriptions.

### C-02 — Word Count
All 5 variations have explicit count/status/compression instructions. V-05 adds "identify the section responsible for overage" before compressing — a minor procedural improvement over "find the longest block."

### C-03 — Artifact Path + Frontmatter
All 5 variations include the exact path and required frontmatter fields. V-05 labels the frontmatter block "required" — no scoring difference but clearer intent.

### C-04 — Gap Framed as Gap
All PASS. Strength gradient:
- V-01/V-02: State the rule
- V-03: Inline check forces rewrite if violated
- V-04: Inertia framing throughout — Gap = what the field has not solved; not incidental to skill design but the structural principle
- V-05: Explains WHY the distinction matters ("goal framing implies the paper might have failed") — produces better generalization

### C-05 — Signal Acquisition
V-01: C-05 is PARTIAL because the top of the file is truncated and STEP 1 is not visible. The acquisition step cannot be confirmed from available text. All other variations have an explicit Phase 1 / acquisition step. V-04 is strongest: requires writing "Gap (raw)" before any section, proving engagement with signals.

### C-06 — Result Quantified
All PASS. V-05 adds motivational framing ("abstracts that say only 'we found improvements' are uninformative and signal a weak paper") which increases expected compliance.

### C-07 — 3 Distinct Amendments
All PASS. Strength gradient:
- V-01/V-02/V-03: 3 labeled targets with specific guidance
- V-04: Adds a before/after example for Gap amendment
- V-05: Anti-trivial guard ("a restatement is not an amendment") + before/after examples for all 3 slots

### C-08 — Journal Variant
All PASS. All 5 variations have 5 journal profiles. V-05 has the most detailed profile descriptions. Vacuous pass if no --for flag.

### C-09 — Claim Tense
All PASS. V-03 has the only enforcement mechanism (inline check with rewrite loop). V-05 explains WHY (timeless truths vs historical events).

### C-10 — Coherent Prose
C-10 is the primary differentiator in this round.
- V-01/V-02/V-03: PARTIAL (2 pts) — "merge into flowing paragraph" stated; no mechanism
- V-04: PARTIAL (3 pts) — Gap-first drafting means Background is written knowing the gap, producing tighter Background→Gap semantic flow at merge; slight structural advantage
- V-05: PASS (5 pts) — Connective bridge phrases required between every section before merge; Phase 3 uses them as glue; prose flow is a first-class authoring step, not an afterthought

---

## Excellence Signals

### E-01 — Explain WHY, not just WHAT
Source: V-05

Explaining the *reason* behind each constraint ("the goal framing implies the paper might have failed; the gap framing states a fact") produces better generalization than stating the rule alone. An AI that understands the motivation can self-correct edge cases not covered by examples. Applied to C-04 (gap framing), C-06 (quantification), C-09 (tense), C-10 (prose flow).

**How to apply**: For any criterion where an AI might satisfy the instruction without satisfying the intent, add a one-sentence explanation of the *reason for the rule*.

### E-02 — Connective Bridges as Pre-Merge Planning
Source: V-05

Requiring a 3-8 word connective phrase after each section, before merge, forces the AI to plan narrative flow as an authoring concern rather than a post-hoc fix. The connectives become glue at merge time. This directly addresses the structural failure mode where six correctly-written sentences are merged without logical connectives.

**How to apply**: For any skill that merges labeled blocks into prose, add a "connective to next section" planning step before merge.

### E-03 — Anti-Trivial-Amendment Guards
Source: V-05

"Each amendment must produce a visible change in the text. A restatement of the prior sentence is not an amendment." Guards against low-effort compliance. Paired with before/after examples, this closes the gap between satisfying the instruction and satisfying the intent of Phase 5.

**How to apply**: Add to any skill with an amendment, revision, or improvement phase: explicit statement that restatements do not count.

### E-04 — Gap-First Drafting as Causal Scaffold
Source: V-04

Writing the Gap section before the Background inverts the standard failure mode (Background written in isolation, disconnected from the gap it should create conditions for). Background written knowing the gap naturally leads into it at merge time, improving semantic flow without requiring explicit connective instructions.

**How to apply**: In abstract-generation or argument-structure skills, consider drafting the central tension/gap first, then writing the setup that makes it feel inevitable.

---

## Round 1 Summary

**Winner**: V-05 with 100/100. All essential criteria pass. C-10 (coherent prose) is the only criterion not passed by the other variations, and V-05 is the only variation with an explicit mechanism (connective bridges) to enforce it.

**Key finding**: The single highest-leverage addition from V-01 baseline to V-05 winner is the connective bridge mechanism in Phase 2. Everything else (signal acquisition, gap framing, tense convention) was already being handled adequately. C-10 was the uncovered gap, and V-05 closed it with a small structural addition (one "Connective to next" line per section).

**Recommendation for Round 2**: Test whether the connective bridge mechanism (E-02) can be back-ported into a simpler prompt structure (V-02 baseline) without the full explanatory register of V-05, to determine whether the benefit comes from the connective mechanism alone or from the combination.
