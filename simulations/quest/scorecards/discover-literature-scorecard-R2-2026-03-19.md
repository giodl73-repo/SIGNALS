Scorecard written to `simulations/quest/scorecards/discover-literature-scorecard-R2-2026-03-19.md`.

---

## discover-literature — Round 2 Scorecard Summary

### Scores

| Rank | Variation | Raw | Golden | C-12 | C-14 |
|------|-----------|-----|--------|------|------|
| 1 | **V-05** Full Synthesis | **115** | YES | PASS | PASS |
| 2 | **V-04** Embedded Recovery | 110 | YES | PASS | FAIL |
| 3 | **V-03** Inertia Gate | 110 | YES | FAIL | PASS |
| 4 | **V-01** Recovery Checklist | 110 | YES | PASS | FAIL |
| 5 | **V-02** Tier-Gate | 105 | YES | FAIL | FAIL |

All five variations pass the golden bar. Score differences are entirely in the four new aspirational criteria (C-11..C-14).

### What separated them

The v2 rubric created two gaps relative to R1's winner: C-12 (PARTIAL → needed PASS) and C-14 (FAIL → needed PASS). The variations closed them differently:

- **V-01** closed C-12 with a standalone recovery checklist sub-step
- **V-03** closed C-14 with a structural inertia gate before the recommendation keyword
- **V-04** closed C-12 more elegantly — embedding recovery inside the per-field questions so compliance can't be skipped
- **V-05** stacked all mechanisms; proved they compose without conflict; sole variant with 5/6 aspirational

### Excellence signals (new in R2)

1. **Dual-domain obligation preamble** — V-05's opening frame covers both "if unknown" (C-12) and "if none found" (C-13) before Phase 1. A global enforcement contract that precedes every phase is more reliable than per-phase rules.
2. **Template-label checkability** — `INERTIA SCENARIO:` / `INERTIA RISK:` as labeled output fields make the inertia gate grep-verifiable, not prose-inference-dependent. Any structural gate benefits from producing a named token.

### Remaining gap

C-09 (Depth Mode Source Threshold) failed across all five variations. No variation added a minimum source count gate. This is the open target for a V-06 candidate.

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["Dual-domain obligation preamble: opening frame names both 'if unknown' (C-12) and 'if none found' (C-13) as non-optional — global enforcement contract before any phase begins", "Template-label checkability: INERTIA SCENARIO: and INERTIA RISK: labels make structural gate compliance grep-verifiable rather than prose-inference-dependent"]}
```
AIL | No minimum source count check added; depends on execution volume |
| C-10 | Methodological precedent chain | PASS | Phase 3 Q4 requires year confirmation that paper predates current work |
| C-11 | Interrogative obligation satisfied | PASS | Inherits R1 full-interrogative register; no enhancement but no regression |
| C-12 | Anti-placeholder recovery executed | PASS | Named "2b. Recovery pass" with six per-field checkboxes; each checkbox specifies follow-up query and "not found after secondary search" fallback — auditable and non-skippable |
| C-13 | Empty-tier acknowledgment present | PASS | Blanket rule: "If a tier has no entries, write 'NONE FOUND — explain why and what additional search is needed.'" |
| C-14 | Inertia guard on PROCEED | FAIL | No inertia scenario added; gap from R1 baseline unaddressed |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/6 = 20
**Raw score: 110** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-02 — Per-Tier Acknowledgment Gate

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical to baseline |
| C-02 | Citation table present | PASS | Phase 2 has explicit 7-column template |
| C-03 | Four-tier literature map built | PASS | Four tiers with per-tier two-question gate; NONE FOUND becomes required answer |
| C-04 | Gap analysis recommendation issued | PASS | Phase 4 five questions + structured template |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies correct path and all 6 frontmatter fields |
| C-06 | Contrary evidence mapped to claims | PASS | CONTRARY tier Q1 requires Claim # and specific objection sentence; Phase 5 Q2 requires response strategy |
| C-07 | WebSearch evidence visible | PASS | Four per-claim search queries; inline "No placeholder entries. If a cell is unknown, note it and search again." |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 explicit HIGH RISK gate |
| C-09 | Depth mode source threshold met | FAIL | No minimum source count check |
| C-10 | Methodological precedent chain | PASS | METHODOLOGICAL tier Q1 requires year with explicit "confirming the year predates the current work's contribution date" |
| C-11 | Interrogative obligation satisfied | PASS | Inherits R1 interrogative register; tier two-gate questions add density but no regression |
| C-12 | Anti-placeholder recovery executed | FAIL | Inline "note it and search again" remains; no structural enforcement — recovery is a rule, not a required question, and can be satisfied with vague prose |
| C-13 | Empty-tier acknowledgment present | PASS | Per-tier "If none found — why not?" is a required question, not a fallback rule; structurally stronger than baseline |
| C-14 | Inertia guard on PROCEED | FAIL | No inertia scenario added |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 3/6 = 15
**Raw score: 105** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-03 — Inertia Guard as PROCEED Gate

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical to baseline |
| C-02 | Citation table present | PASS | Phase 2 has explicit 7-column template |
| C-03 | Four-tier literature map built | PASS | Phase 3 with blanket NONE FOUND rule |
| C-04 | Gap analysis recommendation issued | PASS | Phase 4 five questions + inertia gate template; PROCEED keyword structurally gated |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies correct path and all 6 frontmatter fields |
| C-06 | Contrary evidence mapped to claims | PASS | Phase 3 Q3 requires Claim # per CONTRARY entry; Phase 5 Q2 requires response strategy |
| C-07 | WebSearch evidence visible | PASS | Four per-claim search queries; inline "note it and search again" |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 explicit HIGH RISK gate |
| C-09 | Depth mode source threshold met | FAIL | No minimum source count check |
| C-10 | Methodological precedent chain | PASS | Phase 3 Q4 requires year confirmation |
| C-11 | Interrogative obligation satisfied | PASS | Inherits R1 interrogative register; inertia gate adds two new required questions |
| C-12 | Anti-placeholder recovery executed | FAIL | Inline "note it and search again" only; same structural weakness as R1 baseline |
| C-13 | Empty-tier acknowledgment present | PASS | Blanket NONE FOUND rule in Phase 3 |
| C-14 | Inertia guard on PROCEED | PASS | Explicit "Inertia scenario (required gate before the recommendation keyword)" block; two required questions before PROCEED; template labels INERTIA SCENARIO: / INERTIA RISK: / Reason: — grep-verifiable output |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/6 = 20
**Raw score: 110** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-04 — Interrogative Obligation + Embedded Recovery

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical to baseline |
| C-02 | Citation table present | PASS | Phase 2 per-source questions + 7-column table; questions feed directly into table columns |
| C-03 | Four-tier literature map built | PASS | Phase 3 with blanket NONE FOUND rule |
| C-04 | Gap analysis recommendation issued | PASS | Phase 4 five questions + structured template |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies correct path and all 6 frontmatter fields |
| C-06 | Contrary evidence mapped to claims | PASS | Phase 2 per-source Q asks "Which Claim # from Phase 1 does this source bear on?" — mapping embedded at search time, before the tier map |
| C-07 | WebSearch evidence visible | PASS | Per-field "if unknown after WebSearch..." queries enforce real data at point of entry |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 explicit HIGH RISK gate |
| C-09 | Depth mode source threshold met | FAIL | No minimum source count check |
| C-10 | Methodological precedent chain | PASS | Phase 2 per-source year question + Phase 3 Q4 year confirmation — captured at two levels |
| C-11 | Interrogative obligation satisfied | PASS | Enhanced: per-source seven-question block in Phase 2 creates densest interrogative structure of any single-axis variation; preamble explicitly forbids "blank" and "not answered" |
| C-12 | Anti-placeholder recovery executed | PASS | Per-field questions embed recovery: "If unknown after WebSearch [query], write: 'not found after secondary search — [query used]'"; interrogative obligation and recovery are the same mechanism — question cannot be answered with a blank |
| C-13 | Empty-tier acknowledgment present | PASS | Blanket rule: "If a tier has no entries, write 'NONE FOUND — explain why and what additional search is needed.'" |
| C-14 | Inertia guard on PROCEED | FAIL | No inertia scenario added; gap from R1 baseline unaddressed |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 4/6 = 20
**Raw score: 110** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### V-05 — Full Synthesis

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Claims extracted before search | PASS | Phase 1 identical to baseline |
| C-02 | Citation table present | PASS | Per-source seven-question block + 7-column table; V-04 mechanism |
| C-03 | Four-tier literature map built | PASS | Per-tier two-question gate; V-02 mechanism |
| C-04 | Gap analysis recommendation issued | PASS | Phase 4 five questions + inertia gate before recommendation keyword; V-03 mechanism |
| C-05 | Artifact written with required frontmatter | PASS | Phase 5 specifies correct path and all 6 frontmatter fields |
| C-06 | Contrary evidence mapped to claims | PASS | Claim # embedded in Phase 2 per-source Q (V-04) + CONTRARY tier Q1 two-gate (V-02) + Phase 5 Q2 response strategy |
| C-07 | WebSearch evidence visible | PASS | Per-field "if unknown after WebSearch..." queries (V-04 mechanism) |
| C-08 | High-risk claims flagged | PASS | Phase 4 Q4 explicit HIGH RISK gate |
| C-09 | Depth mode source threshold met | FAIL | No minimum source count check |
| C-10 | Methodological precedent chain | PASS | METHODOLOGICAL tier Q1 two-gate (V-02) + Phase 2 per-source year question (V-04) + year confirmation (Phase 3 Q4) |
| C-11 | Interrogative obligation satisfied | PASS | Enhanced: preamble explicitly names both "if unknown" and "if none found" domains as non-optional; per-source seven-question block; densest interrogative structure across all variations |
| C-12 | Anti-placeholder recovery executed | PASS | Per-field embedded recovery (V-04 mechanism); preamble states "Questions that include 'if unknown' require you to perform the follow-up action and report the result" |
| C-13 | Empty-tier acknowledgment present | PASS | Per-tier two-question gate (V-02 mechanism); preamble states "Questions that include 'if none found' require an explanation — they cannot be answered with silence" |
| C-14 | Inertia guard on PROCEED | PASS | Inertia gate with INERTIA SCENARIO: / INERTIA RISK: template labels (V-03 mechanism); only variation that closes all four new gaps |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 5/6 = 25
**Raw score: 115** | Composite: 100 (capped) | All essential pass: YES | Golden: YES

---

### Ranking

| Rank | Variation | Raw Score | Composite | Golden | C-12 | C-14 | Differentiator |
|------|-----------|-----------|-----------|--------|------|------|----------------|
| 1 | **V-05** | **115** | 100 | YES | PASS | PASS | Only variant closing all four new criteria; proves all mechanisms compose without conflict |
| 2 | **V-04** | 110 | 100 | YES | PASS | FAIL | Elegance: embedded-question mechanism unifies C-11 + C-12 into a single step |
| 3 | **V-03** | 110 | 100 | YES | FAIL | PASS | Highest single-axis gain: turns C-14 from FAIL to PASS; INERTIA SCENARIO: template label is grep-verifiable |
| 4 | **V-01** | 110 | 100 | YES | PASS | FAIL | C-12 PASS via auditable checklist; adds prompt length without V-04's elegance |
| 5 | **V-02** | 105 | 100 | YES | FAIL | FAIL | C-13 enhanced (question-gate vs blanket rule) but misses both C-12 and C-14 |

All variations pass the golden bar. Score differences appear only in aspirational criteria.

Sub-ranking within the 110 group: V-04 ranks above V-03 and V-01 because per-field embedded recovery produces C-12 PASS without an extra sub-step and incidentally strengthens C-11 at the same time. V-03 addresses the harder prior gap (FAIL → PASS on C-14 vs PARTIAL → PASS on C-12). V-01 is comparable to V-03 but the checklist mechanism adds structural overhead that V-04 avoids.

---

### Excellence Signals

**From V-05 — the top scorer:**

1. **Dual-domain obligation preamble** — V-05 opens with a frame that names both recovery domains simultaneously: "Questions that include 'if unknown' require you to perform the follow-up action and report the result. Questions that include 'if none found' require an explanation — they cannot be answered with silence." This covers C-12 and C-13 before any phase begins, rather than embedding each domain in its respective phase. The pattern: a global enforcement contract at the top of the skill primes compliance for the entire run. New pattern not present in any R1 variation.

2. **Template-label checkability for structural gates** — V-03 and V-05 both produce INERTIA SCENARIO: and INERTIA RISK: as labeled output fields. This makes the gate grep-verifiable: presence of the label confirms the gate fired, without parsing prose intent. The pattern generalizes: any structural gate produces a labeled output token, not a prose compliance claim. This is a design principle that can be applied to any future gate criterion.

---

### C-09 Gap Note

C-09 (Depth Mode Source Threshold) fails across all five variations — no variation adds a minimum source count gate. A V-06 candidate should add a Phase 2 check: "How many distinct sources appear in the table? If fewer than [threshold for active depth mode], continue searching before advancing to Phase 3." This is the one aspirational criterion no variation attempted.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["Dual-domain obligation preamble: opening frame names both 'if unknown' (C-12) and 'if none found' (C-13) as non-optional — global enforcement contract before any phase begins", "Template-label checkability: INERTIA SCENARIO: and INERTIA RISK: labels make structural gate compliance grep-verifiable rather than prose-inference-dependent"]}
```
