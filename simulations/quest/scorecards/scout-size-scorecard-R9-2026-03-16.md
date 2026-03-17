# Scout-Size R9 Scorecard — v9 Rubric

## Scope Note

V-03, V-04, and V-05 were not present in the provided source text. This scorecard covers V-01 and V-02 only. V-02 was truncated after Phase 1 §1.2; uncertain criteria are marked.

---

## Scoring Method

| Tier | Criteria | Points | Per criterion |
|------|----------|--------|---------------|
| Essential | C-01–C-05 | 60 | 12 each |
| Recommended | C-06–C-08 | 30 | 10 each |
| Aspirational | C-09–C-27 | 10 | ≈0.53; PARTIAL = 0.26 |

---

## V-01 — Sequential Prose with Inline WRONG/CORRECT Guards

### Essential — 60/60

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | Section 1: named points + total count required; WRONG (general description) / CORRECT (named, counted) inline. |
| C-02 | PASS | "Exactly ONE of: LOW / MEDIUM / HIGH / XL — this vocabulary, nothing else." WRONG examples include "MODERATE" and "3/5." |
| C-03 | PASS | Section 9: workaround named + directional cost judgment required; WRONG (workaround only) / CORRECT (named + direction). |
| C-04 | PASS | Section 6: pairs confidence level with specific established fact. WRONG (bare "Confidence: HIGH") / CORRECT shown. |
| C-05 | PASS | "BANNED from output: task breakdowns, sprint assignments, owner names, milestone dates. Presence of any banned item invalidates the output." |

### Recommended — 30/30

| ID | Score | Evidence |
|----|-------|----------|
| C-06 | PASS | Section 4: specialist disciplines + allocation; WRONG (headcount only) / CORRECT (disciplines named). |
| C-07 | PASS | Section 5: sprint range required; WRONG (calendar date, point estimate) / CORRECT (range). |
| C-08 | PASS | "immediately name the one or two factors that most drive the rating." Generic justification explicitly fails. |

### Aspirational — 11.5/19 = 6.1/10

| ID | Score | Evidence |
|----|-------|----------|
| C-09 | PASS | Section 3 asks for one tier-UP and one tier-DOWN condition by name. |
| C-10 | PASS | Section 8 "Confidence Calibration" present. |
| C-11 | PASS | Section 7 names "the specific thing that is NOT yet known." WRONG/CORRECT examples both present. |
| C-12 | PASS | "It is a single named scenario — not a list of factors." WRONG ("several factors could push") / CORRECT shown. |
| C-13 | PASS | "names the destination tier explicitly: 'Tier rises to XL.'" WRONG/CORRECT shown. |
| C-14 | PASS | "falsifiable — a reader can confirm or rule it out through concrete investigation." Abstract hedges ("if requirements change") explicitly fail. |
| C-15 | PASS | Section 7: "gap must address a DIFFERENT dimension than the confidence basis." Inline self-check: "Could a reader derive this gap from the confidence basis above by negating something I confirmed?" WRONG/CORRECT both present. |
| C-16 | PASS | "destination tier DIFFERS from the currently assigned tier." WRONG ("Tier rises to HIGH" when current is HIGH) shown explicitly. |
| C-17 | PASS | WRONG/CORRECT inline examples present for C-11, C-15, and C-16 — all three documented-failure-mode constraints. |
| C-18 | FAIL | All constraints in prose. C-13/C-16 tier-value requirements are bullets in Section 3, not column headers or structural field labels. |
| C-19 | PASS | Every WRONG/CORRECT block appears within or immediately before the section it governs. No post-output checklist with deferred examples. |
| C-20 | FAIL | Single-phase design; no role separation. |
| C-21 | PASS | Every C-17-scoped block supplies both a named WRONG instance (with stated failure reason) and a named CORRECT instance. |
| C-22 | PARTIAL | Gap non-overlap constraint ("address a DIFFERENT dimension") appears in Section 7 body prose — co-located with the field but in the body, not the section header/label. |
| C-23 | FAIL | No role charters; no field ownership assignments. |
| C-24 | FAIL | No Phase 2; no non-access clause. |
| C-25 | FAIL | Inline self-check present in Section 7 ("Could a reader derive this gap by negating...?") but this is in a single-phase field body, not a Phase 2 charter. Criterion requires Phase 2 charter context. |
| C-26 | FAIL | No roles; no role-tagged column headers. |
| C-27 | FAIL | No compilation table; no cross-phase field colocation. |

**V-01 Composite: 60 + 30 + 6.1 = 96.1**

---

## V-02 — Two-Phase Role Separation with C-25 Self-Test

*V-02 truncated after Phase 1 §1.2. Criteria scored from visible text + stated design axis/hypothesis. Uncertainty noted per criterion.*

### Essential — 60/60

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | Phase 1 §1.1: "List each integration point by name. End with a total count." Visible. |
| C-02 | PASS | Phase 1 §1.2 (visible): "Assign exactly ONE of: LOW / MEDIUM / HIGH / XL — this vocabulary, nothing else." |
| C-03 | PASS | "Inertia Check" explicitly listed in Phase 1 Sizing Analyst charter. |
| C-04 | PASS | "Confidence Basis" explicitly listed in Phase 1 charter. |
| C-05 | PASS | "BANNED from any output field: task breakdowns, sprint assignments, owner names, milestone dates." |

### Recommended — 30/30

| ID | Score | Evidence |
|----|-------|----------|
| C-06 | PASS | "Team-Size Signal" in Phase 1 charter field list; specialist-type requirement follows V-01 axis. |
| C-07 | PASS | "Timeline Signal" in Phase 1 charter; sprint-range instruction inferred from design continuity. |
| C-08 | PASS | "Primary Complexity Driver" named as explicit Phase 1 field. |

### Aspirational — 12/19 = 6.3/10

| ID | Score | Evidence |
|----|-------|----------|
| C-09 | PASS | "Tier Sensitivity (UP and DOWN conditions)" in Phase 1 charter field list. |
| C-10 | PASS | "Confidence Calibration" excluded from Phase 1 → assigned to Phase 2 by charter. |
| C-11 | PASS | "Confidence Gap" excluded from Phase 1 → owned by Phase 2 charter. |
| C-12 | PASS | Single-named-condition requirement inferred as carried over; consistent with design axis. |
| C-13 | PASS | Tier destination requirement inferred as carried over. |
| C-14 | PASS | Falsifiability requirement inferred as carried over. |
| C-15 | PASS | Role separation enforces non-overlap structurally: "Phase 2 explicitly may NOT reproduce or negate Phase 1 confirmed content — it must address dimensions Phase 1 did not cover." Charter violation, not rule violation. |
| C-16 | PASS | Same-destination prohibition inferred; no contradicting signal in visible text. |
| C-17 | FAIL | No WRONG/CORRECT inline failure examples visible in Phase 1. Design emphasis is charter architecture; generation-time inline examples appear absent. |
| C-18 | FAIL | No structural column-header encoding visible in Phase 1 output fields. |
| C-19 | FAIL | C-17 fails, so C-19 is vacuously unmet at the C-17-governed fields. Even if examples appear later in Phase 2 (not visible), they would follow Phase 1 field production. |
| C-20 | PASS | Explicit Sizing Analyst / Risk Assessor separation with distinct charter scopes and non-overlap rule. |
| C-21 | FAIL | No concrete named WRONG + CORRECT pair visible. Design description does not indicate their presence. |
| C-22 | PARTIAL | "Phase 2 may NOT reproduce or negate Phase 1 confirmed content" appears in the framing prose before Phase 1 output, not in the dependent (gap) field's column header. Constraint is articulated but not co-located with the production site. |
| C-23 | PASS | Phase 1 charter enumerates 8 fields with explicit ownership; explicitly names 2 fields it does NOT produce and assigns them to Phase 2. All fields appear in exactly one charter. |
| C-24 | PARTIAL | Non-access clause names the structural property ("not reproduce or negate Phase 1 confirmed content") but does not (from visible text) name the specific confirmed-content category (e.g., "do not cite the API contract status if the Sizing Analyst confirmed it"). Phase 2 charter text not visible to confirm. |
| C-25 | PASS | Design axis title: "with C-25 Self-Test Falsifiability Query." Hypothesis: "named self-test query in Phase 2." This is the defining feature of V-02 — the self-test is the stated axis variable. |
| C-26 | FAIL | No role-tagged column headers in output structure visible. |
| C-27 | FAIL | No output compilation table visible; cross-phase constraint co-encoding not evidenced. |

**V-02 Composite: 60 + 30 + 6.3 = 96.3**

---

## Rankings (scored variations only)

| Rank | Variation | Composite | All Essential | Aspirational PASS | Key trade |
|------|-----------|-----------|---------------|-------------------|-----------|
| 1 | V-02 | **96.3** | Yes | 11 PASS, 2 PARTIAL, 6 FAIL | Gains C-20/C-23/C-25; loses C-17/C-21 |
| 2 | V-01 | **96.1** | Yes | 11 PASS, 1 PARTIAL, 7 FAIL | Strong inline examples; no role architecture |

V-03–V-05: not scored (text not available).

---

## Excellence Signals

**From V-01 (strongest single-phase design):**

1. **Single-phase falsifiability self-check in field body** — Section 7 embeds "Could a reader derive this gap from the confidence basis above by negating something I confirmed?" directly before the Confidence Gap output slot. This achieves C-25's generation-time intent (the model must evaluate its draft before committing) without Phase 2 overhead. The criterion requires a Phase 2 charter to PASS C-25, but the pattern itself is a transferable technique for single-phase designs.

2. **Both WRONG and CORRECT instances are concrete and named** — V-01's inline examples use specific domain content ("API contract is established" / "API contract is not confirmed"), not structural descriptions of the failure pattern. This is why C-21 passes cleanly: the model recognizes drift against a named instance, not an abstract shape.

**From V-02 (strongest role-architecture design):**

3. **Charter exclusion lists complement inclusion lists** — "The Sizing Analyst does NOT produce: Confidence Gap or Confidence Calibration. Those belong to Phase 2." The explicit exclusion is as constraint-active as the inclusion list for preventing opportunistic cross-phase fill. Naming what a role must not produce is a distinct mechanism from naming what it must produce.

4. **Self-test query as Phase 2 charter instruction** — The self-test activates at generation time within a role's mandate rather than as a post-output gate. The role must evaluate its own draft before the field is fixed. Structurally, this is a charter constraint, not a reminder.

**Critical gap this round**: V-02 gains C-20/C-23/C-24/C-25 through role architecture but loses C-17/C-21 by omitting inline WRONG/CORRECT examples. The two strategies are competing where they should be cumulative. A V-05 combined design that provides both role-separation charters *and* WRONG/CORRECT inline examples within each role's output-field definitions would accumulate both pass sets.

---

```json
{"top_score": 96, "all_essential_pass": true, "new_patterns": ["Single-phase falsifiability self-check in field body achieves C-25 generation-time intent without Phase 2 overhead — embed the query directly in the governed output field's definition, not in a post-output gate", "Charter exclusion lists (explicitly naming fields a role does NOT produce and assigning them to the other phase) prevent opportunistic cross-phase fill as effectively as inclusion lists — both directions of charter scoping are needed for C-23 to be structurally tight"]}
```
