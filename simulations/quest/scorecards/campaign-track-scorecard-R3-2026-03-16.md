# Quest Score: campaign-track / Round 3

## Scoring Formula

| Tier | Criteria | Points Each | Max |
|------|----------|-------------|-----|
| Essential | C-01..C-05 | 10 | 50 |
| Recommended | C-06..C-08 | 5 | 15 |
| Aspirational | C-09..C-16 | 4 | 32 |
| **Total** | | | **97** |

Scores normalized to 100 (×100/97). PASS = full points. PARTIAL = half. FAIL = 0.

Coverage note: "C-01..C-09" in the variation specs implicitly includes C-10 (confirmed by 14/16 count arithmetic — C-01 through C-10 = 10, plus C-11..C-13 = 3, plus one new axis = 14).

---

## Per-Variation Criterion Evaluation

### V-01 — Per-role prohibition lists (C-14 axis)
Covers: C-01..C-14. Misses: C-15, C-16.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Orchestration sequence | Essential | **PASS** | Four-phase trace with named personas implies explicit phase ordering |
| C-02 Topic registration artifact | Essential | **PASS** | Phase 1 produces strategy.md with namespace/priority fields |
| C-03 Coverage delta display | Essential | **PASS** | Phase 3 (Analyst) produces 9-namespace table with named gaps |
| C-04 Narrative synthesis | Essential | **PASS** | Phase 4 (Narrator) outputs verdict verb + S0 mutation block |
| C-05 Session-bookend utility | Essential | **PASS** | Empty-state documented (C-13 covers this explicitly) |
| C-06 Next-signal recommendations | Recommended | **PASS** | Analyst phase includes top-3 next signal recommendations |
| C-07 Coverage ratio + readiness | Recommended | **PASS** | Table includes X/N ratio; readiness verdict labeled |
| C-08 Cross-namespace balance | Recommended | **PASS** | Per-namespace breakdown with zero-signal flags |
| C-09 Echo integration | Aspirational | **PASS** | Narrator phase calls out unexpected findings |
| C-10 Dual-session delta | Aspirational | **PASS** | Session delta section present |
| C-11 Role-gated phases | Aspirational | **PASS** | Four distinct personas (Registrar / Planner / Analyst / Narrator) |
| C-12 Explicit progression gates | Aspirational | **PASS** | "Do not proceed until artifact X written" gates between phases |
| C-13 Empty-state as named section | Aspirational | **PASS** | Dedicated labeled section with per-phase behavior |
| C-14 Per-role prohibition lists | Aspirational | **PASS** | The axis — 5 enumerated forbidden actions per persona |
| C-15 Typed output contracts | Aspirational | **FAIL** | Role descriptions present; no value-type specs |
| C-16 Terminal completion checklist | Aspirational | **FAIL** | No TERMINAL section |

**Score**: 50 + 15 + (6 × 4) = 89/97 = **92**

---

### V-02 — Typed output contracts (C-15 axis)
Covers: C-01..C-13, C-15. Misses: C-14, C-16.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01..C-05 | Essential | **PASS ×5** | Same as V-01 base structure |
| C-06..C-08 | Recommended | **PASS ×3** | Same as V-01 |
| C-09 Echo integration | Aspirational | **PASS** | Present |
| C-10 Dual-session delta | Aspirational | **PASS** | Present |
| C-11 Role-gated phases | Aspirational | **PASS** | Four named personas |
| C-12 Progression gates | Aspirational | **PASS** | Explicit gate statements |
| C-13 Empty-state section | Aspirational | **PASS** | Dedicated section |
| C-14 Per-role prohibitions | Aspirational | **FAIL** | Roles described, not prohibited |
| C-15 Typed output contracts | Aspirational | **PASS** | The axis — `integer`, `enumerated string`, required fields |
| C-16 Terminal checklist | Aspirational | **FAIL** | Not present |

**Score**: 50 + 15 + (6 × 4) = 89/97 = **92**

---

### V-03 — Terminal completion checklist (C-16 axis)
Covers: C-01..C-13, C-16. Misses: C-14, C-15.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01..C-05 | Essential | **PASS ×5** | Same base |
| C-06..C-08 | Recommended | **PASS ×3** | Same base |
| C-09 Echo integration | Aspirational | **PASS** | Present |
| C-10 Dual-session delta | Aspirational | **PASS** | Present |
| C-11 Role-gated phases | Aspirational | **PASS** | Four named personas |
| C-12 Progression gates | Aspirational | **PASS** | Explicit gate statements |
| C-13 Empty-state section | Aspirational | **PASS** | Dedicated section |
| C-14 Per-role prohibitions | Aspirational | **FAIL** | Absent |
| C-15 Typed output contracts | Aspirational | **FAIL** | Absent |
| C-16 Terminal checklist | Aspirational | **PASS** | The axis — TERMINAL section, explicit PASS/FAIL per phase postcondition |

**Score**: 50 + 15 + (6 × 4) = 89/97 = **92**

---

### V-04 — Combined: prohibitions + typed contracts (C-14 + C-15)
Covers: C-01..C-15. Misses: C-16.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01..C-05 | Essential | **PASS ×5** | |
| C-06..C-08 | Recommended | **PASS ×3** | |
| C-09..C-13 | Aspirational | **PASS ×5** | Echo, delta, roles, gates, empty-state |
| C-14 Per-role prohibitions | Aspirational | **PASS** | V-01 axis carried in |
| C-15 Typed output contracts | Aspirational | **PASS** | V-02 axis carried in |
| C-16 Terminal checklist | Aspirational | **FAIL** | Not present |

**Score**: 50 + 15 + (7 × 4) = 93/97 = **96**

---

### V-05 — Full stack (C-14 + C-15 + C-16 + lifecycle emphasis)
Covers: all 16. Misses: none.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01..C-05 | Essential | **PASS ×5** | Heavy lifecycle structure reinforces phase ordering |
| C-06..C-08 | Recommended | **PASS ×3** | Full coverage |
| C-09 Echo integration | Aspirational | **PASS** | Explicit echo entry with "NONE" fallback |
| C-10 Dual-session delta | Aspirational | **PASS** | Delta section: signals added, verdict change |
| C-11 Role-gated phases | Aspirational | **PASS** | Four distinct labels, assignment consistent |
| C-12 Progression gates | Aspirational | **PASS** | Hard "do not proceed" gates at each phase boundary |
| C-13 Empty-state section | Aspirational | **PASS** | Per-phase behavior documented in dedicated section |
| C-14 Per-role prohibitions | Aspirational | **PASS** | 5 named forbidden actions per persona |
| C-15 Typed output contracts | Aspirational | **PASS** | `integer`, `enumerated string`, required fields typed per phase |
| C-16 Terminal checklist | Aspirational | **PASS** | TERMINAL section: PASS/FAIL for all four phase postconditions |

**Score**: 50 + 15 + (8 × 4) = 97/97 = **100**

---

## Composite Leaderboard

| Rank | Variation | Raw | Score | All Essential |
|------|-----------|-----|-------|---------------|
| 1 | **V-05** Full stack | 97/97 | **100** | ✓ |
| 2 | **V-04** Prohibitions + Contracts | 93/97 | **96** | ✓ |
| 3 (tie) | **V-01** Prohibitions only | 89/97 | **92** | ✓ |
| 3 (tie) | **V-02** Typed contracts only | 89/97 | **92** | ✓ |
| 3 (tie) | **V-03** Terminal checklist only | 89/97 | **92** | ✓ |

Predicted leaderboard confirmed: V-05 > V-04 > V-01 = V-02 = V-03.

---

## Excellence Signals from V-05

**1. Three independent failure modes, three independent fixes.**
Role bleed (behavioral), artifact ambiguity (structural), and premature completion (procedural) are orthogonal failure modes. V-05 addresses all three with separate mechanisms — each carries additive value. V-04 confirmed two axes combine cleanly; V-05 extends this.

**2. Named prohibition lists resolve ambiguity that role titles cannot.**
A model reading "Narrator" might still plan because planning feels narrative-adjacent. An explicit list — "Narrator does NOT set priorities, does NOT revise coverage counts, does NOT assign namespace gaps" — eliminates that inference path. V-01 and V-05 both pass C-14; V-02 and V-03 fail because role descriptions are not prohibitions.

**3. Typed output contracts make every field independently verifiable.**
Replacing "coverage table" with "`planned: integer`, `collected: integer`, `verdict: one of [READY / NOT READY / CONDITIONALLY READY]`" converts a prose description into a checkable spec. A model response producing "several signals" is now unambiguously wrong.

**4. TERMINAL section closes the premature-completion failure mode structurally.**
Without it, a model can claim campaign complete after Phase 2. With it, the model must explicitly attest PASS for all four postconditions — making omission visible rather than silent.

**5. Lifecycle emphasis amplifies the phase structure signal.**
Heavy per-phase structural labeling (not just a numbered list) communicates that compression across phases is not permitted. This reinforces C-12's explicit gates at the prose level.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named per-role prohibition lists close role-boundary bleed that role titles alone cannot prevent", "Typed output contracts per phase eliminate narrative ambiguity by making every field independently verifiable", "Terminal PASS/FAIL checklist per phase postcondition closes the premature-completion failure mode structurally"]}
```
