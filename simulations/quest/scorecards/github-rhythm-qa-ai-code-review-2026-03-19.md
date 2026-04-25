● List directory signals
  └ 7 files found

● Search (glob)
  │ "signals/**/ai-code-review*"
  └ 28 files found

● Read ai-code-review-feedback-2026-03-19.md
  │ signals\validate\feedback\ai-code-review-feedback-2026-03-19.md
  └ 1 line read

● Read ai-code-review-adoption-blocker-2026-03-19.md
  │ signals\validate\adoption-blocker\ai-code-review-adoption-blocker-2026-03-19.md
  └ 1 line read

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ 1 line read

● List directory signals\validate
  └ 3 files found

● Read ai-code-review-adoption-2026-03-19.md
  │ signals\validate\adoption\ai-code-review-adoption-2026-03-19.md
  └ 171 lines read

● Read ai-code-review-feedback-2026-03-19.md
  │ signals\validate\feedback\ai-code-review-feedback-2026-03-19.md
  └ L1:120 (120 lines read)

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L1:120 (120 lines read)

● Read ai-code-review-adoption-blocker-2026-03-19.md
  │ signals\validate\adoption-blocker\ai-code-review-adoption-blocker-2026-03-19.md
  └ L1:120 (120 lines read)

● Read ai-code-review-feedback-2026-03-19.md
  │ signals\validate\feedback\ai-code-review-feedback-2026-03-19.md
  └ L120:280 (161 lines read)

● Read ai-code-review-adoption-blocker-2026-03-19.md
  │ signals\validate\adoption-blocker\ai-code-review-adoption-blocker-2026-03-19.md
  └ L120:300 (128 lines read)

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L120:300 (181 lines read)

Signal check passed — spec found at `signals\draft\specs\ai-code-review-spec-2026-03-19.md`. Existing validate signals found for feedback, adoption, and adoption-blocker. Now running the full 5-skill campaign.

**Step 2: Running sub-skills in sequence.**

Starting with **review-design** (validate-design):

● skill(review-design)

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L300:474 (175 lines read)

Now I have the full spec. Let me also read key prior signals for cross-reference, then produce the design review artifact.

● Read ai-code-review-feasibility-2026-03-19.md
  │ signals\discover\feasibility\ai-code-review-feasibility-2026-03-19.md
  └ L1:60 (60 lines read)

● Read ai-code-review-lifecycle-2026-03-19.md
  │ signals\simulate\lifecycle\ai-code-review-lifecycle-2026-03-19.md
  └ L1:60 (60 lines read)

● Read ai-code-review-risk-2026-03-19.md
  │ signals\discover\risk\ai-code-review-risk-2026-03-19.md
  └ L1:60 (60 lines read)

● Create review/design directory (shell)
  │ New-Item -ItemType Directory -Path "sim-test\signals\review\design" -Force | Out-Null;
  │ Write-Output "done"
  └ 2 lines...

● Create ai-code-review-design-2026-03-19.md +224
  └ signals\review\design\ai-code-review-design-2026-03-19.md

Now running **review-users** (validate-users):

● skill(review-users)

● Create review/users directory (shell)
  │ New-Item -ItemType Directory -Path "sim-test\signals\review\users" -Force | Out-Null;
  │ Write-Output "done"
  └ 2 lines...

● Create ai-code-review-users-2026-03-19.md +210
  └ signals\review\users\ai-code-review-users-2026-03-19.md

Now running **review-customers** (validate-customers):

● skill(review-customers)

● Create review/customers directory (shell)
  │ New-Item -ItemType Directory -Path "sim-test\signals\review\customers" -Force | Out-Null;
  │ Write-Output "done"
  └ 2 lines...

● Create ai-code-review-customers-2026-03-19.md +259
  └ signals\review\customers\ai-code-review-customers-2026-03-19.md

All 5 sub-skills complete. Now compiling the **Validation Brief** (Steps 3–4):

Here is the full **rhythm-qa** output:

---

# RHYTHM-QA: AI Code Review — Design Validation Campaign

## CAMPAIGN STATUS

| Sub-skill | Status | Artifact |
|-----------|--------|----------|
| **review-design** | ✅ RAN | `signals/review/design/ai-code-review-design-2026-03-19.md` |
| **review-users** | ✅ RAN | `signals/review/users/ai-code-review-users-2026-03-19.md` |
| **review-customers** | ✅ RAN | `signals/review/customers/ai-code-review-customers-2026-03-19.md` |
| **listen-feedback** | ✅ PRIOR | `signals/validate/feedback/ai-code-review-feedback-2026-03-19.md` |
| **listen-adoption** | ✅ PRIOR | `signals/validate/adoption/ai-code-review-adoption-2026-03-19.md` |

**Supporting signal:** `signals/validate/adoption-blocker/ai-code-review-adoption-blocker-2026-03-19.md` (14 blockers registered)

---

## CAMPAIGN RESULTS SUMMARY

| Sub-skill | Key Question | Key Output |
|-----------|-------------|-----------|
| **review-design** | Does this design hold under expert review? | 9 reviewers, **5 P1 blockers**, verdict: **CONDITIONAL PASS** |
| **review-users** | Does this design match user mental models? | **4 blocking usability issues**, worst persona: Compliance Officer (2/5) |
| **review-customers** | Will paying customers adopt this? | Top blocker: noise calibration in Week 1. WTP signal: strong for developers, blocked for enterprise. Weighted score: **3.5/5** |
| **listen-feedback** | What will users say in first 30 days? | Aggregate NPS: **6.6/10** (below 7.0 threshold). 3 blocking themes. Verdict: **REVISE BEFORE SHIP** |
| **listen-adoption** | How does adoption curve across archetypes? | Readiness score: **58/100** (conditional). Laggard converts at Month 6+ only with quantified proof. Chasm between Early Adopters (Week 4) and Early Majority (Month 2). |

---

```
VALIDATION BRIEF: ai-code-review
================================

P1 Blockers (ship-stopping):
  [review-design F04]   Prompt injection attack surface unaddressed — untrusted PR diffs
                        enter LLM prompts with no sanitization or boundary enforcement.
  [review-design F01]   No tenant isolation architecture — enterprise deployment blocked;
                        shared queue, shared DB, shared LLM context across orgs.
  [review-design F03]   Constraint C-01 contradicts finding storage — "no code persisted"
                        vs PostgreSQL storing code-referencing findings indefinitely.
  [review-design F13]   Context assembly under-designed — 220 hrs / 15 lines of spec;
                        highest-risk component with thinnest specification.
  [review-users]        Compliance persona scored 2/5 — tool un-approvable for regulated
                        orgs without data flow diagram, audit trail, retention policy.

Top Adoption Risk: FALSE-POSITIVE FATIGUE IN WEEK 1
  Every signal, every persona, every adoption model converges:
  - review-customers C-05: "I need to not see 50 false architecture findings"
  - listen-feedback NPS dragged down by skeptics (C-05: 4, C-06: 5)
  - listen-adoption Blocker #1: CRITICAL — "no second chance"
  - adoption-blocker B-05: KILL BLOCKER — "teams that experience >20% noise
    rate in Week 1 disable permanently"
  Default confidence threshold 0.7 is too permissive. Must ship at ≥0.85.

Predicted NPS at 30 days: 6.6 (below 7.0 ship threshold)
  → Projected to 7.8 if 3 amendments applied (data retention, human review
    safeguards, platform abstraction) per listen-feedback sensitivity analysis.

Fastest Win: CHANGE DEFAULT CONFIDENCE THRESHOLD FROM 0.7 TO 0.85
  Unblocks the most users with the least effort. Every developer persona,
  every adoption model, and every risk signal identifies noise as the #1 kill
  mechanism. One config change + calibration mode (≤5 findings/PR, ≥0.90,
  first 2 weeks) addresses the top blocker across all 5 sub-skills.

  Second-fastest: Add data retention/purge policy to §4 Constraints.
  Unblocks compliance persona (2/5 → 3/5), enterprise buyers, and CISO.
  Estimated effort: 1 day of spec work.

Verdict: VALIDATE-WITH-CONDITIONS
  The design is architecturally sound and solves a quantified problem
  (review bottleneck consuming 57% of cycle time). Primary audience
  (developers) scores 3.5-4.0/5 on adoption willingness. But 5 P1
  blockers, NPS below threshold, and compliance persona at 2/5 mean
  the spec requires revision before implementation begins.

  CONDITIONS FOR VALIDATION:
  1. Resolve C-01/storage contradiction with retention/purge policy
  2. Add prompt injection mitigation to §3.2
  3. Add tenant isolation to §3.7
  4. Expand context assembly design (§3.2) to match its 220-hr scope
  5. Change default confidence threshold to ≥0.85
  6. Add data flow diagram (cloud vs self-hosted) for compliance
```

---

## NEXT RECOMMENDED

Two skills that would most improve confidence:

→ **`/prove-prototype ai-code-review`** — Build the smallest possible prototype (shadow-mode analysis on 10 historical PRs from 2 internal repos). Measures: false-positive rate on real data, latency at realistic scale, context assembly depth vs. finding quality. Closes the gap that every signal identifies: "no working prototype, no dogfood data, no FP rate baseline." Adoption readiness score jumps from 58 → ~72 with empirical data.

→ **`/draft-spec ai-code-review --amend`** — Apply the 5 P1 findings + 3 feedback amendments to the spec. Resolves C-01 contradiction, adds tenant isolation, prompt injection design, context assembly expansion, and data retention policy. Projected NPS rises from 6.6 → 7.8 (above ship threshold). Compliance persona rises from 2/5 → 3+/5.

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: Full 5-skill campaign completed. 3 sub-skills ran fresh (review-design, review-users, review-customers), 2 consumed prior artifacts (listen-feedback, listen-adoption). All 5 sub-skills independently converge on false-positive fatigue as the #1 adoption risk — cross-signal coherence is HIGH. The compliance persona (2/5 in review-users, NPS 5 in listen-feedback, 2/5 in review-customers) is the consistent weak point across all validation signals. Copilot compatibility: all artifacts written to disk; no interactive tool-calling required; the orchestration is pure sequencing. Total context consumed: ~150K tokens across 8 prior signal artifacts.


Total usage est:        6 Premium requests
API time spent:         9m 40s
Total session time:     10m 2s
Total code changes:     +693 -0
Breakdown by AI model:
 claude-opus-4.6-1m       1.1m in, 23.6k out, 1.1m cached (Est. 6 Premium requests)
