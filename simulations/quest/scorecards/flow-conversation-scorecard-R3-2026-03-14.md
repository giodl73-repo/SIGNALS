# Quest Scorecard — flow-conversation — Round 3

**Rubric version:** v3 (13 criteria: C-01 through C-13)
**Scoring formula:** `(essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/6 * 10)`
**Golden threshold:** all 4 essential pass AND composite ≥ 80

---

## Per-Variation Scorecards

### V-01 — Role Sequence: Auditor Produces Separate Per-Turn Spec Annotations

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Phase 2 preserves turn-by-turn structure with all mandatory fields: user input, trigger phrase, confidence, node path, session variables, response |
| C-02 | All four defect classes | **PASS** | Phase 3 Defect Matrix covers dead ends, infinite loops, trigger phrase collisions, missing fallbacks — each row requires FOUND or CONFIRMED ABSENT |
| C-03 | Session state tracked | **PASS** | Per-turn session variable block tracks scope, current value, change status, and carry-forward across all transitions |
| C-04 | Copilot Studio framing | **PASS** | Vocabulary throughout: topics, trigger phrases, conditions, fallback topics, session variables, topic redirects, escalation nodes |
| C-05 | Defect reproduction steps | **PASS** | Phase 6 amendments require trigger phrase sequence + observable failure — minimal reproduction structure enforced |
| C-06 | Fallback chain coverage | **PASS** | Phase 4 dedicated fallback chain trace walks from unrecognized input to terminal state with quality verdict |
| C-07 | Intent collision disambiguation | **PASS** | Phase 3 collision row mandates disambiguation strategy with rationale (entity enrichment / condition ordering / trigger phrase refactor) |
| C-08 | Graph coverage metric | **PASS** | Phase 6 coverage report: topics visited/total, trigger phrases exercised/estimated total, percentage ratios |
| C-09 | Adversarial turn injection | **PASS** | Phase 5 injects one adversarial scenario with node path trace and GRACEFUL / BRITTLE / SILENT FAILURE outcome verdict |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 1 enumerates prohibited terms; Phase 7 Auditor scans for violations in the finished trace |
| C-11 | Turn-level conformance verdict | **PASS** | `SPEC_CONFORMANCE: CONFORMS / DEVIATES` required on every Developer turn in Phase 2; violations cross-reference CS-SPEC-NN |
| C-12 | Role-separated post-production audit | **PASS** | Phase 7 Auditor explicitly reads the completed Phase 2 trace as a finished artifact and produces an independent per-turn SPEC_CONFORMANCE annotation layer — separate from Developer self-report, enables discrepancy detection where Developer reported CONFORMS but topology evidence shows deviation |
| C-13 | Typed assertion fields with constrained enums | **FAIL** | Developer SPEC_CONFORMANCE uses "/" notation (CONFORMS/DEVIATES) — not a typed `\|` enum field. No per-turn `PROHIBITED_TERM_SCAN: CLEAN \| FOUND` field. Phase 7 scan is narrative, not a structured typed output |

**Essential:** 4/4 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 5/6 → 8.33 pts
**Composite: 98.33** | All essential: YES

---

### V-02 — Phrasing Register: Typed Fields with Constrained Verdict Enums

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Turn-by-turn Phase 2 structure preserved |
| C-02 | All four defect classes | **PASS** | Phase 3 DEFECT_VERDICT uses constrained `FOUND \| CONFIRMED_ABSENT` enum — no free-text hedging in verdict position |
| C-03 | Session state tracked | **PASS** | Session variable block per turn, scope and change tracked |
| C-04 | Copilot Studio framing | **PASS** | CS vocabulary enforced throughout |
| C-05 | Defect reproduction steps | **PASS** | Amendments carry reproduction sequences |
| C-06 | Fallback chain coverage | **PASS** | Phase 4 fallback chain with terminal state verdict |
| C-07 | Intent collision disambiguation | **PASS** | Collision row with disambiguation rationale |
| C-08 | Graph coverage metric | **PASS** | Phase 6 quantified coverage ratios |
| C-09 | Adversarial turn injection | **PASS** | Phase 5 adversarial scenario with outcome verdict |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 1 prohibited term list; Phase 7 scan |
| C-11 | Turn-level conformance verdict | **PASS** | Per-turn `SPEC_CONFORMANCE: CONFORMS \| DEVIATES` typed field in Developer trace |
| C-12 | Role-separated post-production audit | **FAIL** | Phase 7 remains a scanning role operating alongside production — no hard artifact boundary, no explicit declaration that Auditor reads a *finished* Developer document. Producer still partially self-certifies. |
| C-13 | Typed assertion fields with constrained enums | **PASS** | `PROHIBITED_TERM_SCAN: CLEAN \| FOUND` typed field per Developer turn; `DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT` in Phase 3; all verdict positions use constrained `\|` enum format — free-text hedging structurally prevented |

**Essential:** 4/4 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 5/6 → 8.33 pts
**Composite: 98.33** | All essential: YES

---

### V-03 — Lifecycle Emphasis: Hard Artifact Boundary

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Turn-by-turn trace preserved |
| C-02 | All four defect classes | **PASS** | All four defect classes in matrix |
| C-03 | Session state tracked | **PASS** | Session variable tracking per turn |
| C-04 | Copilot Studio framing | **PASS** | CS vocabulary throughout |
| C-05 | Defect reproduction steps | **PASS** | Reproduction sequences in amendments |
| C-06 | Fallback chain coverage | **PASS** | Dedicated fallback trace phase |
| C-07 | Intent collision disambiguation | **PASS** | Disambiguation strategy in collision row |
| C-08 | Graph coverage metric | **PASS** | Coverage ratios reported |
| C-09 | Adversarial turn injection | **PASS** | Phase 5 adversarial injection with verdict |
| C-10 | Prohibited vocabulary gate | **PASS** | Prohibited term list + Phase 7 scan |
| C-11 | Turn-level conformance verdict | **PASS** | Per-turn SPEC_CONFORMANCE by Developer |
| C-12 | Role-separated post-production audit | **PASS** | `=== DEVELOPER ARTIFACT ===` / `=== AUDITOR ARTIFACT ===` hard boundary is structural, not role-label. Auditor Artifact explicitly declares Developer Artifact as its input document — Auditor reads the completed output, not working in parallel with production |
| C-13 | Typed assertion fields with constrained enums | **FAIL** | No typed `\|` enum syntax specified for verdict positions. Verdict format unspecified — does not structurally prevent hedging. No per-turn `PROHIBITED_TERM_SCAN` field |

**Essential:** 4/4 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 5/6 → 8.33 pts
**Composite: 98.33** | All essential: YES

---

### V-04 — Role Sequence + Phrasing Register

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | Full turn-by-turn Phase 2 trace |
| C-02 | All four defect classes | **PASS** | Phase 3 with `DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT` constrained enum |
| C-03 | Session state tracked | **PASS** | Session variable block per turn |
| C-04 | Copilot Studio framing | **PASS** | CS vocabulary throughout |
| C-05 | Defect reproduction steps | **PASS** | Amendments with reproduction sequences |
| C-06 | Fallback chain coverage | **PASS** | Phase 4 fallback chain to terminal |
| C-07 | Intent collision disambiguation | **PASS** | Collision disambiguation with rationale |
| C-08 | Graph coverage metric | **PASS** | Quantified coverage ratios in Phase 6 |
| C-09 | Adversarial turn injection | **PASS** | Phase 5 adversarial with GRACEFUL/BRITTLE/SILENT FAILURE verdict |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 1 term list; Auditor post-production scan |
| C-11 | Turn-level conformance verdict | **PASS** | Per-turn `SPEC_CONFORMANCE: CONFORMS \| DEVIATES` by Developer (inline self-report) |
| C-12 | Role-separated post-production audit | **PASS** | V-01 mechanism: Phase 7 Auditor reads finished Phase 2 trace and produces independent per-turn SPEC_CONFORMANCE annotation layer. Two conformance layers: Developer self-report (C-11) + Auditor independent re-annotation (C-12). Auditor catches cases where Developer reported CONFORMS but topology evidence shows deviation |
| C-13 | Typed assertion fields with constrained enums | **PASS** | V-02 mechanism: per-turn `PROHIBITED_TERM_SCAN: CLEAN \| FOUND` typed field in Developer trace; `DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT` in Phase 3; all assertion positions use `\|` enum — free-text hedging structurally prevented at point of production |

**Essential:** 4/4 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 6/6 → 10 pts
**Composite: 100.00** | All essential: YES

---

### V-05 — Full Synthesis

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Dialog path traced as turns | **PASS** | R2 V-05 7-phase gate architecture; Phase 2 TRACE GATE enforces all turn fields before advancing |
| C-02 | All four defect classes | **PASS** | Phase 3 DEFECT GATE with `DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT` — gate prevents advancing until all four rows have verdict + evidence |
| C-03 | Session state tracked | **PASS** | Session variable tracking per turn; Phase 2 TRACE GATE confirms state carried across all transitions |
| C-04 | Copilot Studio framing | **PASS** | CS vocabulary enforced from Phase 1 SETUP GATE through Phase 7 Auditor Artifact |
| C-05 | Defect reproduction steps | **PASS** | Phase 6 amendments require trigger phrase sequence + observable failure; DEFECT GATE cross-references Phase 2 SPEC_CONFORMANCE violations |
| C-06 | Fallback chain coverage | **PASS** | Phase 4 with FALLBACK GATE — quality verdict (COMPLETE / LOOPS / TRUNCATED) required before advancing |
| C-07 | Intent collision disambiguation | **PASS** | Phase 3 collision row mandates disambiguation strategy with rationale |
| C-08 | Graph coverage metric | **PASS** | Phase 6 coverage report with topic ratio + trigger phrase ratio |
| C-09 | Adversarial turn injection | **PASS** | Phase 5 adversarial injection with node path trace and GRACEFUL/BRITTLE/SILENT FAILURE outcome |
| C-10 | Prohibited vocabulary gate | **PASS** | Phase 1 SETUP GATE enumerates prohibited terms; Phase 7 Auditor Artifact independently scans the completed Developer trace |
| C-11 | Turn-level conformance verdict | **PASS** | Developer inline `SPEC_CONFORMANCE: CONFORMS \| DEVIATES` per turn in Phase 2; TRACE GATE confirms presence before advancing |
| C-12 | Role-separated post-production audit | **PASS** | Phase 7 Auditor reads Phases 1–6 as a finished artifact. Per-turn re-annotation layer is explicitly separate from Developer self-report. Role separation enforced by the 7-phase gate: Auditor cannot begin until Phases 1–6 are gated complete. Creates symmetric discrepancy detection for both SPEC_CONFORMANCE (C-11 vs C-12) and PROHIBITED_TERM_SCAN (Developer field vs Auditor scan) |
| C-13 | Typed assertion fields with constrained enums | **PASS** | Per-turn `PROHIBITED_TERM_SCAN: CLEAN \| FOUND` in Phase 2 Developer trace; `DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT` in Phase 3; `SPEC_CONFORMANCE: CONFORMS \| DEVIATES` per turn; `PROHIBITED_TERM_SCAN: CLEAN \| FOUND` in Auditor Artifact. Point-of-production enforcement: Developer evaluates vocabulary compliance as each turn is written, not only retroactively. Auditor's independent scan then cross-validates Developer's CLEAN verdicts — detecting false-clean reports in both compliance axes |

**Essential:** 4/4 → 60 pts
**Recommended:** 3/3 → 30 pts
**Aspirational:** 6/6 → 10 pts
**Composite: 100.00** | All essential: YES

---

## Rankings

| Rank | Variation | Composite | All Essential | C-12 | C-13 |
|------|-----------|-----------|---------------|------|------|
| 1 (tie) | **V-04** | **100.00** | YES | PASS | PASS |
| 1 (tie) | **V-05** | **100.00** | YES | PASS | PASS |
| 3 (tie) | V-01 | 98.33 | YES | PASS | FAIL |
| 3 (tie) | V-02 | 98.33 | YES | FAIL | PASS |
| 3 (tie) | V-03 | 98.33 | YES | PASS | FAIL |

---

## Excellence Signals

**V-04 and V-05 achieve 100.00 by satisfying both C-12 and C-13 simultaneously.** The three lower variations each satisfy exactly one of the two new criteria — confirming that C-12 and C-13 are orthogonal dimensions. Neither substitutes for the other.

**What V-05 adds over V-04:** V-05 integrates C-12 and C-13 into the existing 7-phase gate structure rather than layering them onto a less-structured prompt. The TRACE GATE enforces that the Auditor cannot begin Phase 7 until all Developer turns are complete — the gate enforces the role-separation contract structurally, not just through instruction. This is coherence through architecture: the mechanism that prevents self-certification is the same mechanism that enforces completeness.

**Key architectural insight from V-05:** Combining C-12 and C-13 creates symmetric coverage across two compliance axes:

| | Developer (inline) | Auditor (post-production) |
|--|-------------------|--------------------------|
| **Spec conformance** | C-11: SPEC_CONFORMANCE per turn | C-12: Independent re-annotation |
| **Vocabulary compliance** | C-13: PROHIBITED_TERM_SCAN per turn | C-10: Retroactive scan |

The Auditor in V-05 can detect false-clean verdicts in *both* axes — a Developer-reported `SPEC_CONFORMANCE: CONFORMS` that the Auditor's re-annotation finds wrong, and a `PROHIBITED_TERM_SCAN: CLEAN` in a turn that the Auditor's scan finds contains "dialog" or "intent." This 2×2 coverage grid is fully implied by C-12 + C-13 together but neither criterion alone produces it.

No new criteria emerge: the rubric reaches its designed ceiling at 100.00 with C-13 added in v3. The 2×2 architecture is an implied property of combining existing criteria, not a new measurable dimension.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
