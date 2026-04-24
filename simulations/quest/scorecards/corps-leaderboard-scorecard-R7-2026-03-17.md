## Quest Score — corps-leaderboard R7

### Scoring Method

R6 confirmed all five variations pass C-01 through C-21 (100/100 against v6). R7 evaluation focuses on C-22 and C-23 for all five, with essential criteria spot-checked.

---

## C-22 — Dual-Statement Prevents-Rule Redundancy

Does `prevents:` appear at two structurally independent locations: (1) a pre-write check construct placed *before* the template, and (2) inside the template's Breaks field definition?

| Variation | Pre-write Check Location | Template Restatement | Verdict |
|-----------|--------------------------|----------------------|---------|
| V-01 | Phase 7 — standalone pre-write check table (two rows: score >= 1 / score = 0) placed before the action template | Template's `Breaks` field: "if condition score = 0: `prevents:` condition name — re-entry rationale" | **PASS** |
| V-02 | Requirement 7 — `Pre-write check — Breaks field` block with WHEN/THEN clauses, named and placed before the template | Template's `Breaks` field: "WHEN score = 0: `prevents:` condition name — re-entry rationale" + separate MUST statement "The `prevents:` prefix MUST appear…" | **PASS** |
| V-03 | Phase 7 — `Pre-write check — Breaks field determination` block placed before the action template | Template's `Breaks` field: "score = 0: `prevents:` condition name — re-entry rationale" | **PASS** |
| V-04 | Role 3 / Task C — `Pre-write decision check — Breaks field` table placed before the action template | Template's `Breaks` field: "if condition score = 0: `prevents:` condition name — re-entry rationale" + "The `prevents:` prefix is required when the targeted condition scores 0. Writing the condition name without the `prevents:` prefix when score = 0 is a Compiler error." | **PASS** |
| V-05 | Role 2 / Section E — named `Pre-write check table` (a two-row decision table: Score >= 1 / Score = 0 → `prevents:`) placed before the action template | Template's `Breaks` field: "resolved condition → `prevents:` condition name — re-entry rationale" + "The `prevents:` prefix is required when the targeted condition scores 0. An action that names a resolved condition without `prevents:` is a Compiler error." | **PASS** |

**All five pass C-22.** The R7 design target was achieved: every variation places the pre-write check as a first-class construct independent of the template.

---

## C-23 — Two-Level Nearest-Miss Cascade

When no 1-away gaps exist, does the output require both Level 1 (closest to 1-away, with name + numeric gap) and Level 2 (closest to 2-away, with name + numeric gap)?

| Variation | Level 1 Required | Level 2 Required | Failure Named | Verdict |
|-----------|-----------------|-----------------|---------------|---------|
| V-01 | Yes — "Level 1 — closest to 1-away: [specific topic] \| needs [n] more [unit]" as mandatory table row | Yes — "Level 2 — closest to 2-away: [specific topic] \| needs [n] more [unit]" as mandatory table row | "Both Level 1 and Level 2 rows are required when the 1-away list is empty…'No 1-away gaps found' alone does not satisfy this section." | **PASS** |
| V-02 | Yes — "Level 1 — Closest to 1-away threshold: [specific topic] needs [n] more [unit]" — MUST | Yes — "Level 2 — Closest to 2-away threshold: [specific topic] needs [n] more [unit]" — MUST | "The Level 1 and Level 2 statements are not optional…An absence statement without both levels fails this requirement." | **PASS** |
| V-03 | Yes — "Level 1 — Closest to 1-away threshold: [specific topic] needs [n] more [unit]" | Yes — "Level 2 — Closest to 2-away threshold: [specific topic] needs [n] more [unit]" | Gate condition: "PHASE 6 cannot close if either level is absent, vague ('a topic'), or lacks a specific numeric step count." | **PASS** |
| V-04 | Yes — "Level 1 — Closest to 1-away: [specific topic] needs [n] more [unit]" — BOTH required | Yes — "Level 2 — Closest to 2-away: [specific topic] needs [n] more [unit]" | "Both levels must carry a specific name (not 'a topic') and a specific numeric step count." Gate: "Level 1 and Level 2: [written / not needed]" | **PASS** |
| V-05 | Yes — "Level 1 — Closest to 1-away threshold: [specific topic] needs [n] more [unit]" | Yes — "Level 2 — Closest to 2-away threshold: [specific topic] needs [n] more [unit]" | "If only one level is written, the Skeptic wins — the team has no two-sprint plan." | **PASS** |

**All five pass C-23.** The R7 design achieved full ceiling opening closure — the R6 split (V-02/V-04 pass C-23 but fail C-22; V-05 passes C-22 but fails C-23) is resolved.

---

## Essential Criteria — Spot Check (C-01 to C-05)

Confirmed forward-carried from R6. All five variations pass all essential criteria:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 — Scan + registry | PASS | PASS | PASS | PASS | PASS |
| C-02 — 5 achievements, exact names | PASS | PASS | PASS | PASS | PASS |
| C-03 — 3 milestones, exact names | PASS | PASS | PASS | PASS | PASS |
| C-04 — Leaderboard ranked | PASS | PASS | PASS | PASS | PASS |
| C-05 — 3+ actions, namespace + achievement | PASS | PASS | PASS | PASS | PASS |

---

## Composite Scores

All five variations carry C-01 through C-21 (confirmed from R6) and now pass C-22 and C-23. All 15 aspirational criteria are satisfied.

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total |
|-----------|---------------|-----------------|-------------------|-------|
| V-01 | 60/60 | 30/30 | 10/10 (15/15) | **100.00** |
| V-02 | 60/60 | 30/30 | 10/10 (15/15) | **100.00** |
| V-03 | 60/60 | 30/30 | 10/10 (15/15) | **100.00** |
| V-04 | 60/60 | 30/30 | 10/10 (15/15) | **100.00** |
| V-05 | 60/60 | 30/30 | 10/10 (15/15) | **100.00** |

**Five-way tie at 100.00.** The v7 ceiling is now closed.

---

## Excellence Signals

All five variations score 100/100. To identify new patterns for v8, the analysis looks for mechanisms present in one or two variations that go beyond what C-22 and C-23 test.

### Signal 1 — Gate-Level Prevents: Count Self-Audit (V-02 only)

V-02's ACTIONS GATE line emits: `"ACTIONS GATE: [n] actions written. Prevents: prefix used for [n] zero-score conditions."` This forces the model to count and report how many times it applied the `prevents:` rule across all actions written. No other variation requires a self-audit count at gate time — the others state the rule and require its use, but do not require the model to report how many times it triggered. The count verification is a structural enforcement mechanism distinct from C-20/C-22: it tests application frequency, not just presence of the rule. A gate line that tracks `prevents:` count would surface cases where the rule was never applied even when zero-score conditions exist.

### Signal 2 — Synthesis Novelty Constraint (V-05 only)

V-05's Role 3 instruction: `"The insight must be something the Skeptic (Role 1) would acknowledge as new information — not a restatement of the inertia assessment."` This adds a constraint on the Team Insight sentence that no other variation has: it must contain information not visible from the health/inertia section. The existing synthesis criterion (C-13 or equivalent) tests for structure (cross-topic conclusion + concrete number + specific name). V-05 adds a *novelty* constraint — the insight must advance beyond what the Skeptic already established. This is independently testable: does the synthesis sentence repeat an observation already present in the inertia or health section, or does it add a new cross-dimension conclusion?

---

## Ranking

All five co-ceiling at 100.00 against v7. No ranking differential. The v7 rubric is fully saturated.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Gate-level prevents: prefix count self-audit — the ACTIONS GATE line reports how many actions applied the prevents: prefix for zero-score conditions, testing application frequency rather than rule presence alone", "Synthesis novelty constraint — the team insight sentence must contain information the health/inertia assessment does not already state, tested by whether the insight advances beyond what the opening skeptic role established"]}
```
