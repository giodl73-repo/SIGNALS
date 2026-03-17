# org-review / Round 12 Scorecard (v11 rubric)

---

## Baseline Assessment

All five variations inherit the complete V-05 R11 template (210/225). The shared infrastructure passes all 5 essential, all 3 recommended, and C-09 through C-32 (24 aspirationals).

**Baseline per tier:**
- Essential (C-01–C-05): 5/5 × 12 pts = **60 pts**
- Recommended (C-06–C-08): 3/3 × 10 pts = **30 pts**
- Aspirationals C-09–C-32: 24/24 × 5 pts = **120 pts**
- **Base total: 210/225**

---

## New Criteria Differentials — C-33/C-34/C-35

### C-33 — Lens Applicability Rating Pre-committed
**Pass condition**: §1.5 LENS COVERAGE TABLE (the §17 pre-committed table) carries HIGH/MEDIUM/LOW ratings per artifact-domain × reviewer pair; preamble states ratings determine coverage expectations.

| Variation | §17 LENS COVERAGE APPLICABILITY? | §1.5 Table Rows have H/M/L? | C-33 |
|-----------|----------------------------------|-----------------------------|------|
| V-01 | NO — §17 is NULL HYPOTHESIS TABLE | N/A | FAIL |
| V-02 | YES (§17) | YES — `\| Artifact Domain \| Reviewer \| Lens Applicability (H/M/L) \|` | PASS |
| V-03 | YES (§17) | YES — identical to V-02 | PASS |
| V-04 | YES (§17) | YES — identical to V-02 | PASS |
| V-05 | YES (§17 extended) | YES — identical to V-02 | PASS |

**Evidence note**: V-01's §17 is the NULL HYPOTHESIS TABLE (renamed §18 in V-02+). It has no artifact-domain × reviewer applicability structure. C-33 requires the §1.5 applicability table, not the per-section §15 table, because V-02 is the canonical source and its §15 table has no applicability column — confirming "LENS COVERAGE TABLE" in C-33 refers to §17's §1.5 construct.

---

### C-34 — ADVISORY-GAP Domain Coverage Pre-committed
**Pass condition**: Domain gap-check pre-committed in preamble using HIGH-applicability tier; uncovered domains → ADVISORY-LENS-GAP in ACTION ITEM REGISTER.

| Variation | §17 Domain Gap-Check? | ADVISORY-LENS-GAP in Register? | C-34 |
|-----------|----------------------|-------------------------------|------|
| V-01 | NO (no §17 LENS COVERAGE APPLICABILITY) | NO | FAIL |
| V-02 | YES — "if no reviewer carries HIGH applicability → classify ADVISORY-LENS-GAP" | YES — §17 row in register | PASS |
| V-03 | YES — identical to V-02 | YES | PASS |
| V-04 | YES — identical to V-02 | YES | PASS |
| V-05 | YES — identical to V-02 | YES | PASS |

**Evidence note**: V-01 has C-31 active (§15), but C-34's operative vacuous condition is the absence of §17's HIGH-applicability tier framework — no tier = no gap check possible. C-34 FAIL for V-01 (not vacuous, but fails on missing mechanism).

---

### C-35 — Null Hypothesis Challenger Dimension Comparison Table
**Pass condition**: Challenger's null hypothesis evaluation uses structured dimension table with Current State / Proposed State / Delta / g_null Signal columns; g_null(initial) derivable from table values alone via mechanical formula; ≥3 dimensions; appears before domain sections.

| Variation | §17/§18 NULL HYPOTHESIS TABLE? | g_null Signal column present? | Formula mechanical? | C-35 |
|-----------|-------------------------------|------------------------------|---------------------|------|
| V-01 | YES (§17) | YES — WEAKENS NULL / NEUTRAL / STRENGTHENS NULL | YES — count formula → FAIL/CONDITIONAL/PASS | PASS |
| V-02 | YES (§18) | YES — same formula | YES | PASS |
| V-03 | NO (§18 absent; §9 Stage 1 = GOpen directly) | NO | NO | FAIL |
| V-04 | YES (§18) | YES — same formula | YES | PASS |
| V-05 | YES (§18 extended) | YES — same formula + §17 domain citation | YES | PASS |

**Evidence note**: V-03 confirms C-35 independence — it has §17 LENS COVERAGE but no §18, and §9 Stage 1 reads "g_null(initial) = GOpen verdict directly. [BRACKET OPENING; §18 inactive]". Clearly excluded.

---

## Per-Variation Composite Scores

### V-01 — §17 NULL HYPOTHESIS DIMENSION TABLE

| Criterion | Status | Pts |
|-----------|--------|-----|
| C-01 through C-32 (inherited base) | PASS | 210 |
| C-33 | FAIL — no §17 LENS COVERAGE APPLICABILITY PROTOCOL | 0 |
| C-34 | FAIL — no HIGH-applicability tier to gap-check against | 0 |
| C-35 | **PASS** — §17 dimension table; g_null derivable from WEAKENS NULL count formula | 5 |
| **Total** | | **215/225** |

---

### V-02 — §17 LENS COVERAGE APPLICABILITY + §18 NULL HYPOTHESIS TABLE (Integrated, Canonical)

| Criterion | Status | Pts |
|-----------|--------|-----|
| C-01 through C-32 (inherited base) | PASS | 210 |
| C-33 | **PASS** — §1.5 table: each row carries HIGH/MEDIUM/LOW per artifact-domain × reviewer; preamble defines coverage expectation by tier | 5 |
| C-34 | **PASS** — §17 domain gap-check: "if no reviewer carries HIGH → ADVISORY-LENS-GAP"; register row `§17 LENS COVERAGE APPLICABILITY \| ADVISORY-LENS-GAP` | 5 |
| C-35 | **PASS** — §18 dimension table with WEAKENS/NEUTRAL/STRENGTHENS NULL and mechanical majority formula; g_null(initial) = formula output (not GOpen) | 5 |
| **Total** | | **225/225** |

*Note*: The rubric summary states "~215/225" for V-02, but this appears to be an intermediate estimate during authoring. The variate file states expected 225/225 and the template fully activates all three criteria. Scored at 225 per the implemented design.

---

### V-03 — §17 LENS COVERAGE APPLICABILITY ONLY

| Criterion | Status | Pts |
|-----------|--------|-----|
| C-01 through C-32 (inherited base) | PASS | 210 |
| C-33 | **PASS** — §1.5 table identical to V-02; HIGH/MEDIUM/LOW ratings per domain × reviewer | 5 |
| C-34 | **PASS** — domain gap-check identical to V-02; ADVISORY-LENS-GAP register row | 5 |
| C-35 | FAIL — no §18; §9 Stage 1 explicitly reads "g_null(initial) = GOpen verdict directly [§18 inactive]"; null hypothesis remains prose-based | 0 |
| **Total** | | **220/225** |

---

### V-04 — V-01 + V-03 Additive (§17 LENS + §18 NULL TABLE)

| Criterion | Status | Pts |
|-----------|--------|-----|
| C-01 through C-32 (inherited base) | PASS | 210 |
| C-33 | **PASS** — §17 §1.5 table identical to V-02/V-03 | 5 |
| C-34 | **PASS** — domain gap-check identical to V-02/V-03 | 5 |
| C-35 | **PASS** — §18 table identical to V-01; g_null derivable from formula | 5 |
| **Total** | | **225/225** |

*No structural difference from V-02 for C-33/C-34/C-35 scoring purposes. "Additive" vs "integrated" design doesn't surface a rubric gap — both pass the same criteria.*

---

### V-05 — V-04 + §17↔§18 Cross-Reference Contract

| Criterion | Status | Pts |
|-----------|--------|-----|
| C-01 through C-32 (inherited base) | PASS | 210 |
| C-33 | **PASS** — §17 §1.5 table identical to V-02/V-04 | 5 |
| C-34 | **PASS** — domain gap-check identical to V-02/V-04 | 5 |
| C-35 | **PASS** — §18 table identical to V-04; §18->§17 citation adds domain traceability but does not break the table's g_null derivability | 5 |
| C-36 (candidate) | NOT SCORED — v11 rubric has no C-36 criterion | 0 |
| **Total** | | **225/225** |

*V-05 introduces a cross-reference chain that exceeds current rubric coverage. The §17->§18 chain requirement and §18->§17 citation requirement are present but inert under v11. They may become C-36 in v12.*

---

## Ranking Summary

| Rank | Variation | Score | Delta vs Base |
|------|-----------|-------|---------------|
| 1 (tied) | V-02 | 225/225 | +15 |
| 1 (tied) | V-04 | 225/225 | +15 |
| 1 (tied) | V-05 | 225/225 | +15 |
| 4 | V-03 | 220/225 | +10 |
| 5 | V-01 | 215/225 | +5 |

**All essential criteria pass**: YES for all five variations.

---

## Excellence Signals from Top-Scoring Variations (V-02/V-04/V-05)

**Signal 1 — Pre-committed §1.5 LENS COVERAGE TABLE separates role selection from reviewer execution.** §17 forces applicability commitments before any reviewer runs. An auditor can verify whether domain coverage was pre-decided or ad hoc without reading reviewer narrative. The artifact-domain × reviewer matrix is the structural evidence for C-33.

**Signal 2 — Domain-inward gap-check (C-34) is orthogonal to role-outward lens exhaustion (C-31).** V-02/V-03/V-04/V-05 show these two coverage layers can be independently activated. C-31 answers "did the reviewer use every lens?" C-34 answers "does every artifact domain have an expert?" A review can pass C-31 while failing C-34 (every reviewer exhausted their lenses, but no reviewer has HIGH applicability to some domain). The register's ADVISORY-LENS-GAP class makes this visible.

**Signal 3 — §18 WEAKENS NULL / NEUTRAL / STRENGTHENS NULL formula replaces g_null(initial) editorial judgment.** In V-01/V-02/V-04/V-05, the challenger cannot assign g_null(initial) = PASS if a majority of dimensions WEAKENS NULL. The formula is a constraint, not a description. V-03's §9 Stage 1 still reads "= GOpen verdict directly" — the challenger retains editorial control. C-35 eliminates that last editorial step in the bracket opening.

**Signal 4 (V-05 only, candidate C-36) — §17↔§18 cross-reference chain creates coverage-to-hypothesis traceability.** ADVISORY-LENS-GAP domains from §17 must appear as §18 dimensions. This prevents the null hypothesis from being evaluated only on well-covered domains while silently ignoring coverage gaps. §18 dimensions that lack a §17 citation are ADVISORY-DIMENSION-ORPHAN. A chain-verification field in BRACKET OPENING makes the traceability machine-verifiable. This pattern may warrant C-36 extraction in v12.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["ADVISORY-LENS-GAP domains (§17) must feed §18 null hypothesis dimension table — coverage gaps must be evaluated in null hypothesis, not only in lens coverage", "§18 dimensions carry §17 domain citations; uncited dimensions are ADVISORY-DIMENSION-ORPHAN — creates bidirectional traceability between applicability table and null hypothesis table", "Chain verification field in BRACKET OPENING confirms §17->§18 cross-reference is intact before reviewer sections execute"]}
```
