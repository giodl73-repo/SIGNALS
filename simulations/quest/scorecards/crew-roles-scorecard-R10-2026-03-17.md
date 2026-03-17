# crew-roles Scorecard — Round 10 (Rubric v6)

## Scoring Formula

| Tier | Criteria | Max Pts |
|------|----------|---------|
| Essential | C-01–C-05, PASS=10pts each | 50 |
| Recommended | C-06–C-08, PASS=13.33pts, PARTIAL=6.67 | 40 |
| Aspirational | C-09–C-25, `pass_count / 17 × 10` | 10 |
| **Total** | | **100** |

PARTIAL = 0.5 weight in aspirational sum.

---

## Availability Note

Only V-01 (full text) and V-02 (STEP 1 only, truncated) were provided. V-03 through V-05 are absent from the input. V-01 and V-02 are scored below; V-03–V-05 cannot be scored.

---

## V-01 — Lifecycle Emphasis

**Axis:** Naming every phase explicitly and requiring a named exit artifact at each boundary forces structural discipline.

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | All 5 fields | **PASS** | Phase 5 spec enumerates all 5 fields (name, orientation.frame/verify/lens, expertise.domain/relevance, collaborates_with, scope) |
| C-02 | Inertia-advocate present | **PASS** | Phase 5 "Inertia-advocate requirements" block mandates frame, verify questions referencing Q1/Q2, Bucket A relevance |
| C-03 | Correct output path | **PASS** | Phase 5: "Write each role from the ROLE PLAN TABLE to `.craft/roles/{area}/`" |
| C-04 | Domain specificity | **PASS** | Phase 1 extracts domain vocabulary; Phase 5 requires expertise.relevance to reference ≥1 Phase 1 term; Phase 6 CHECK 4 gates |
| C-05 | Minimum 3 roles | **PASS** | Phase 4 constraint: "≥3 roles including inertia-advocate" enforced before Phase 5 opens |

Essential score: **5/5 → 50 pts**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-06 | Lens actionability | **PASS** | Phase 5: `verify` = must end with `?`; `lens` = "must be an imperative (not a question)" |
| C-07 | Collaborates_with resolves | **PASS** | Phase 5: "names from ROLE PLAN TABLE only"; Phase 6 CHECK 2 orphan-reference check blocks gate |
| C-08 | Perspective diversity | **PASS** | Phase 4 constraint: "≥3 distinct perspective categories (inertia counts as one; product, technical, domain-specialist are others)" |

Recommended score: **3/3 → 40 pts**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-09 | Scope gradient | **PASS** | Phase 4: "≥2 distinct scope values (team, cross-team, org)" |
| C-10 | Inertia domain-grounded | **PASS** | Phase 2 Q1 must reference a Bucket A term naming the specific existing system |
| C-11 | Vocabulary-forced-field | **PASS** | Phase 1 produces vocabulary; Phase 5 requires expertise.relevance to reference it; Phase 6 CHECK 4 enforces |
| C-12 | Inertia pre-characterization | **PASS** | Phase 2 answers exactly Q1 (current system), Q2 (migration cost), Q3 (user habit); Phase 5 verify requires ≥2 of these dimensions |
| C-13 | Registry summary table | **PASS** | Phase 6 CHECK 1 produces "Role \| Frame Excerpt (first 8 words) \| Scope \| Collaborates With" — column uses "Frame Excerpt" not "Orientation" but carries the same structural function |
| C-14 | Scope-gradient-enforcement | **PASS** | Phase 4: "If the plan has only one scope value: identify which roles to revise, update their scope, and re-verify the constraint. Writing is structurally blocked." |
| C-15 | Verification-gate-phase | **PASS** | Phase 6 is a single named VERIFICATION GATE with CHECK 1–5 bundled; "gate does not PASS until every check shows PASS; do not deliver output until gate verdict is PASS" |
| C-16 | Vocabulary-linked inertia Q&A | **PASS** | Phase 2 structurally requires Q1 from Bucket A, Q2 from Bucket B, Q3 from Bucket C; cross-bucket assignment fails Phase 2 exit |
| C-17 | Pre-write scope audit | **PASS** | Phase 4 is named "PRE-WRITE SCOPE AUDIT"; Phase 5 cannot begin until ≥2 distinct scope values appear in the ROLE PLAN TABLE |
| C-18 | Vocabulary check in gate | **PASS** | Phase 6 CHECK 4 "VOCABULARY COVERAGE CHECK" is a mandatory gate item; gate verdict cannot be PASS without CHECK 4 passing |
| C-19 | Inertia frame Q-slot template | **PASS** | Phase 3 template: `` `[Q1: current system] resists replacement because [Q2: migration cost], and users rely on [Q3: user habit].` `` — explicit named placeholders |
| C-20 | Q-domain-aligned distribution | **PASS** | Audit table enforces bucket alignment per Q; cross-bucket selection fails Phase 2 exit; same-term reuse across rows is caught by full-restart re-evaluation |
| C-21 | Bucketed vocabulary extraction | **PASS** | Phase 1 produces three named buckets (A = Current-System, B = Migration-Cost, C = User-Habit); each term assigned to exactly one bucket |
| C-22 | Domain-alignment audit table | **PASS** | Phase 2: structured audit table "Q \| Term Used \| Expected Bucket \| Match YES/NO" is a named phase artifact; any NO triggers replacement; gates Phase 2 |
| C-23 | Frame Fill as dedicated phase | **PASS** | Phase 3 "PHASE 3 — FRAME FILL" is a standalone named phase producing FRAME FILL RECORD before Phase 4 opens |
| C-24 | Audit-table full re-evaluation | **PASS** | Phase 2 explicit: "restart evaluation from Q1 — re-evaluate all three rows simultaneously… the gate condition is 'all three rows YES in a single full-pass evaluation,' not 'each row individually YES'" |
| C-25 | Frame-slot source citation | **PASS** | Phase 3 requires Q1, Q2, Q3 verbatim citations plus slot-binding verification (Q1 YES/NO, Q2 YES/NO); Phase 3 does not close until both binding checks YES |

Aspirational: **17/17 → 17/17 × 10 = 10 pts**

### V-01 Composite

| Tier | Points |
|------|--------|
| Essential | 50 |
| Recommended | 40 |
| Aspirational | 10 |
| **Total** | **100** |

---

## V-02 — Inertia Framing (Incomplete)

**Axis:** Building the inertia-advocate first and deriving all other roles in relation to what it challenges.

Only STEP 1 (EXTRACT BUCKETED VOCABULARY) is present in the provided text. STEP 2 onward is absent.

### Scoreable criteria from STEP 1

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-21 | Bucketed vocabulary extraction | **PASS** | STEP 1 describes three named buckets (A/B/C), min 2 terms each, no cross-bucket placement |
| All others | — | **UNSCORED** | Text absent |

### V-02 Composite

| Tier | Points |
|------|--------|
| Essential | 0 (not shown) |
| Recommended | 0 (not shown) |
| Aspirational | 1/17 × 10 ≈ **0.6** |
| **Total** | **~1** |

*Score reflects only STEP 1. If remaining steps exist in the full file, V-02 score would be substantially higher. Not comparable with V-01 in this state.*

---

## V-03 – V-05

Not provided. Cannot be scored.

---

## Rankings (Scoreable Variations)

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-01 — Lifecycle Emphasis | **100** | Yes |
| 2 | V-02 — Inertia Framing (partial) | ~1 | No (unscored) |

---

## Excellence Signals — V-01

**ES-1: Delivery gate re-verifies slot-binding independently of the Frame Fill phase**

Phase 6 CHECK 5 re-verifies the inertia frame's slot bindings against Phase 2 answers after all roles are written. This is a second, structurally independent check from Phase 3's production-time binding verification. The gap it closes: a slot that was bound correctly in Phase 3 could be transcribed incorrectly into the role file during Phase 5 authoring. Phase 3's binding check cannot detect a post-Phase-3 transcription error; the gate-level re-check can. Two-checkpoint binding verification is stronger than single-checkpoint.

**ES-2: Q3 slot has a citation but no binding verification — three-slot frame with two-binding audit**

The frame template fills Q1, Q2, and Q3 slots. Phase 3 requires source citations for all three slots (Q1 ← Phase 2 Q1, Q2 ← Phase 2 Q2, Q3 ← Phase 2 Q3). However, Phase 3's binding verification checks only Q1 and Q2 ("Q1 slot drawn from Q1 answer: YES/NO; Q2 slot drawn from Q2 answer: YES/NO"). Phase 6 CHECK 5 similarly verifies only Q1 and Q2 traces. Q3 slot binding is never structurally verified. The completed frame string can have Q3 populated from Q1 or Q2's answer — producing a citation pointing to the correct source while the slot content is drawn from the wrong one — and the error is undetectable by the current gate structure. This is the same structural gap that C-25 closed for Q1/Q2, now recurring for Q3.

---

## New Pattern Summary

| Candidate | Closes | What It Requires |
|-----------|--------|-----------------|
| C-26 | ES-1 | Delivery gate re-verification of frame slot bindings: Phase 6 must include a slot-binding check against Phase 2 answers that runs *after* role files are written, independent of Phase 3's production-time check |
| C-27 | ES-2 | Q3 slot binding verification: Phase 3 binding check and Phase 6 slot-binding check must explicitly verify Q3 slot drawn from Q3 answer, not only Q1 and Q2 |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["delivery gate re-verifies slot-binding after role authoring: Phase 6 includes a slot-binding check independent of Phase 3 production-time check, catching transcription errors between Frame Fill completion and role writing", "Q3 slot binding unverified: three-slot frame template verifies only Q1 and Q2 bindings at Phase 3 and Phase 6; Q3 slot can be populated from the wrong Phase 2 answer without structural detection"]}
```
