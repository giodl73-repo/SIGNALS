## Quest Score — mock-all R2

**Rubric:** v2 (C-01–C-13) | **Variations:** V-01–V-05 | **Date:** 2026-03-15

---

## Scoring Methodology

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 5 * 10)
```

Partial credit = 0.5 per criterion where a mechanism is present but underspecified.

---

## V-01 — Output Format: Pre-Classification Table

**Axis:** output-format | **Targets:** C-11, C-02

| Criterion | Band | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 | Essential | PASS | Step 2 explicitly requires `[MOCK ARTIFACT]` header for all 9 namespaces |
| C-02 | Essential | PASS | Pre-classification table in Step 1 locks category; Step 2 requires body to match |
| C-03 | Essential | PASS | EVIDENCE-HEAVY rule → prove + listen get REAL-REQUIRED unconditionally |
| C-04 | Essential | PASS | Step 3 `## Coverage Summary` with all required columns |
| C-05 | Essential | PASS | Step 4 `## FINAL LINE` section with exact `Next:` line format |
| C-06 | Recommended | PASS | Coverage table column `Tier flag` + explicit TIER-2/3-CRITICAL marks for trace, scout, listen |
| C-07 | Recommended | PASS | Step 2 requires min 3 substantive skill-specific lines + failure condition defined |
| C-08 | Recommended | PASS | COMPLIANCE rule in Step 1 table detects `--compliance` + TOPICS.md tags; flows to summary |
| C-09 | Aspirational | PASS | TIER-CRITICAL rule is tier-conditional (`tier >= 2`); classification table updates by active tier |
| C-10 | Aspirational | PASS | Coverage table `Recommended next step` column requires namespace-specific skill command |
| C-11 | Aspirational | PASS | Step 1 is structurally prior to Step 2; "Do not begin writing namespace artifact bodies until this table is complete" is explicit gate |
| C-12 | Aspirational | PASS | `## FINAL LINE` is a dedicated labelled block; anti-placeholder language: "Do not leave these as placeholders" |
| C-13 | Aspirational | PASS | RATIONALE PREAMBLE block in Step 1 scoped to all REAL-REQUIRED placements; appears once before first body |

**Essential:** 5/5 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 5/5 → 10

**Score: 100** ✓ Golden (all essential pass, composite ≥ 80)

---

## V-02 — Lifecycle Emphasis: Named Phases + Stop Gates

**Axis:** lifecycle-emphasis | **Targets:** C-12, C-05

| Criterion | Band | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 | Essential | PASS | GENERATE phase implies all 9 namespace bodies |
| C-02 | Essential | PASS | CLASSIFY phase handles categories |
| C-03 | Essential | PASS | CLASSIFY phase would mark EVIDENCE-HEAVY namespaces |
| C-04 | Essential | PASS | SUMMARIZE phase = coverage table |
| C-05 | Essential | PASS | HANDOFF phase enforces `Next:` line |
| C-06 | Recommended | PARTIAL | Phases suggest tier flags in SUMMARIZE, but not explicitly required in hypothesis |
| C-07 | Recommended | PASS | GENERATE phase implies artifact bodies |
| C-08 | Recommended | PARTIAL | Compliance detection not mentioned; may or may not be in CLASSIFY |
| C-09 | Aspirational | PARTIAL | Tier scoping not the axis focus; conditional behavior unspecified |
| C-10 | Aspirational | PASS | SUMMARIZE phase would include next steps |
| C-11 | Aspirational | PARTIAL | CLASSIFY as Phase 1 implies ordering, but no explicit "classification table" with all rows before Phase 2 |
| C-12 | Aspirational | PASS | Dedicated HANDOFF phase with single output = exactly the `Next:` line |
| C-13 | Aspirational | FAIL | Rationale not mentioned; hypothesis says nothing about REAL-REQUIRED rationale |

**Essential:** 5/5 → 60 | **Recommended:** 2/3 → 20 | **Aspirational:** 3/5 → 6

**Score: 86** ✓ Golden (all essential pass, composite ≥ 80)

---

## V-03 — Phrasing Register: Rationale Preamble

**Axis:** phrasing-register | **Targets:** C-13, C-03

| Criterion | Band | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 | Essential | PASS | All 9 namespaces implied by base skill structure |
| C-02 | Essential | PASS | Category classification implied |
| C-03 | Essential | PASS | EVIDENCE-HEAVY namespaces get REAL-REQUIRED with rationale |
| C-04 | Essential | PASS | Coverage table implied |
| C-05 | Essential | PASS | Handoff pattern present (basic element) |
| C-06 | Recommended | PARTIAL | Tier flags not in V-03's scope; basic implementation may omit |
| C-07 | Recommended | PASS | Artifact bodies implied |
| C-08 | Recommended | PARTIAL | Rationale preamble doesn't guarantee compliance detection; C-08 requires detection + flagging in summary |
| C-09 | Aspirational | PARTIAL | Tier scoping not addressed |
| C-10 | Aspirational | PASS | Namespace-specific steps plausibly included |
| C-11 | Aspirational | FAIL | Not the axis; classification interleaving not prevented |
| C-12 | Aspirational | FAIL | Handoff isolation not addressed |
| C-13 | Aspirational | PASS | The single-axis target; preamble rule covers all REAL-REQUIRED placements |

**Essential:** 5/5 → 60 | **Recommended:** 2/3 → 20 | **Aspirational:** 2.5/5 → 5

**Score: 85** ✓ Golden (all essential pass, composite ≥ 80)

---

## V-04 — Combination: Pre-Classification + Named Phases

**Axis:** output-format + lifecycle-emphasis | **Targets:** C-11, C-12, C-07

| Criterion | Band | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 | Essential | PASS | Phase 2 = GENERATE → all 9 namespace bodies |
| C-02 | Essential | PASS | Phase 1 = pre-classification table from V-01 |
| C-03 | Essential | PASS | Classification table marks EVIDENCE-HEAVY |
| C-04 | Essential | PASS | Phase 3 = SUMMARIZE |
| C-05 | Essential | PASS | Phase 4 = HANDOFF |
| C-06 | Recommended | PASS | V-01's tier flags column carried into Phase 3 |
| C-07 | Recommended | PASS | Explicitly predicted to pass in axis plan |
| C-08 | Recommended | PASS | V-01's COMPLIANCE rule inherited |
| C-09 | Aspirational | PASS | V-01's tier-conditional table inherited |
| C-10 | Aspirational | PASS | Namespace-specific steps in Phase 3 summary |
| C-11 | Aspirational | PASS | V-01 pre-classification table as Phase 1 gate |
| C-12 | Aspirational | PASS | V-02's dedicated HANDOFF phase (Phase 4) |
| C-13 | Aspirational | PARTIAL | Axis plan predicts C-11/C-12/C-07 pass; C-13 not predicted → inheritance from V-01 uncertain |

**Essential:** 5/5 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 4.5/5 → 9

**Score: 99** ✓ Golden

---

## V-05 — Combination: Rationale + Evidence-First Ordering + Conversational Register

**Axis:** phrasing-register + role-sequence | **Targets:** C-13, C-03, C-06

| Criterion | Band | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 | Essential | PASS | All 9 namespaces; evidence-first reorders but doesn't drop any |
| C-02 | Essential | PASS | Classification implied |
| C-03 | Essential | PASS | Rationale preamble from V-03 + evidence-first ordering ensures consistent REAL-REQUIRED application |
| C-04 | Essential | PASS | Coverage table implied |
| C-05 | Essential | PASS | Handoff pattern present |
| C-06 | Recommended | PASS | Explicitly predicted target; evidence-first ordering surfaces TIER-CRITICAL namespaces early |
| C-07 | Recommended | PASS | Evidence-first namespaces (prove, listen) produced with full bodies |
| C-08 | Recommended | PASS | Rationale preamble + compliance flagging from V-03 |
| C-09 | Aspirational | PARTIAL | Tier scoping not in axis description |
| C-10 | Aspirational | PASS | Namespace-specific steps in coverage |
| C-11 | Aspirational | FAIL | Evidence-first reorders bodies but no pre-classification table before first body |
| C-12 | Aspirational | FAIL | Handoff isolation not addressed |
| C-13 | Aspirational | PASS | Core axis target; preamble rationale inherited from V-03 |

**Essential:** 5/5 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 2.5/5 → 5

**Score: 95** ✓ Golden

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | **Score** | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-01 | 60/60 | 30/30 | 10/10 | **100** | ✓ |
| V-04 | 60/60 | 30/30 | 9/10 | **99** | ✓ |
| V-05 | 60/60 | 30/30 | 5/10 | **95** | ✓ |
| V-02 | 60/60 | 20/30 | 6/10 | **86** | ✓ |
| V-03 | 60/60 | 20/30 | 5/10 | **85** | ✓ |

---

## Excellence Signals — V-01

**ES-01: Pre-commit-then-generate gate**
Publishing a complete 9-row classification table as a named structural step (Step 1), with an explicit gate ("Do not begin writing namespace artifact bodies until this table is complete"), prevents the interleaved classification failure mode at the instruction level. No post-hoc correction needed. This is qualitatively different from "CLASSIFY is Phase 1" (V-02): a phase label allows a classification that is per-namespace, just before each body; a complete table forces global commitment first.

**ES-02: Anti-placeholder language in FINAL LINE**
C-12 is satisfied not just by structural isolation (its own `##` section) but by an explicit "Replace {topic} and {date} with actual values. Do not leave these as placeholders." instruction. The structural isolation prevents absorption; the anti-placeholder language prevents literal string bleed. Two independent failure modes closed.

**ES-03: Preamble-scoped rationale as a reusable rule**
A single RATIONALE PREAMBLE block in Step 1, explicitly scoped to all downstream REAL-REQUIRED placements, satisfies C-13 without per-flag repetition. It also appears early enough (before any artifact body) to be read before the first REAL-REQUIRED application, making it semantically prior even if the reader skips ahead.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-commit-then-generate: publish complete 9-row classification table as a hard gate before any artifact body is written, preventing per-section category drift", "anti-placeholder gate in FINAL LINE: pair structural isolation of handoff section with explicit replace-instruction to close both absorption and literal string bleed failure modes independently", "preamble-scoped rationale: single RATIONALE PREAMBLE block before first artifact body satisfies C-13 for all downstream REAL-REQUIRED placements without per-flag repetition"]}
```
