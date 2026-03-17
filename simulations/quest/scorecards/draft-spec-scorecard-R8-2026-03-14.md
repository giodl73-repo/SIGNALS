# R8 Scorecard — `draft-spec` Variations (V-01 through V-05)

---

## Scoring Summary

| Variation | E (5) | R (3) | A (19) | Composite |
|-----------|-------|-------|--------|-----------|
| V-01 | 5/5 | 2/3 | 5/19 | **102** |
| V-02 | 5/5 | 3/3 | 10/19 | **135** |
| V-03 | 5/5 | 3/3 | 17/19 | **166** |
| V-04 | 5/5 | 3/3 | 19/19 | **175** |
| V-05 | 5/5 | 3/3 | 19/19 | **175** |

**Ranking**: V-05 = V-04 > V-03 > V-02 > V-01 (V-05 wins on quality within the 175 tie — see notes below)

**Golden threshold** (all 5 essential + composite ≥ 85): V-02, V-03, V-04, V-05 all pass. V-01 passes threshold but misses recommended C-07 depth.

---

## Per-Variation Criterion Breakdown

### V-01 — Branch B sub-conditions only (v7 minimal base)

Base: v7 V-01 minimal (merged INERTIA-TABLE + REQUIRES/PRODUCES/BLOCKS, no PM phase, no cross-namespace).

**Essential (5/5)**

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Five guided sections structurally present from minimal base |
| C-02 | PASS | Scout status table in SETUP block |
| C-03 | PASS | P0 coverage count present from INERTIA-TABLE artifact scan |
| C-04 | PASS | Findings section present (may state "none found" — counts) |
| C-05 | PASS | Frontmatter follows `{topic}-spec-{date}.md` convention |

**Recommended (2/3)**

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | PASS | At least one secondary role invoked with recorded outcome |
| C-07 | **FAIL** | Minimal base focuses on INERTIA execution, not cross-artifact contradiction scan; no named R-ID pair conflict surfaced |
| C-08 | PASS | Amendment list produced in Phase 4 |

**Aspirational (5/19)**

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Branch B sub-conditions (B-1 thru B-4) cover all artifact-absent states; fallback documented per branch |
| C-10 | FAIL | Minimal base has no cross-namespace signal tracing |
| C-11 | FAIL | No pre-printed column; minimal base does not add one |
| C-12 | FAIL | Role annotations deferred, not inline; minimal base does not restructure placement |
| C-13 | FAIL | No per-row P0 status column |
| C-14 | PASS | INERTIA-TABLE from minimal base includes explicit scan instruction naming requirements artifact before confirming absence |
| C-15 | FAIL | No cross-namespace signal; two-location requirement cannot fire |
| C-16 | FAIL | No PM pre-assignment phase in minimal base |
| C-17 | FAIL | Minimal base has INERTIA-TABLE but no named gate artifact with downstream blocking logic |
| C-18 | PASS | B-1/B-2/B-3/B-4 VERBATIM blocks are complete scripted response text; model does not compose from scratch |
| C-19 | FAIL | No ordinal location markers |
| C-20 | FAIL | REQUIRES/PRODUCES/BLOCKS is declarative-header format, not unified role-source instruction |
| C-21 | FAIL | No gate token (C-17 fails), so proof-of-work invalidity rule cannot be evaluated |
| C-22–C-25 | 1/4 PASS | INERTIA-TABLE pattern satisfies approximately one v7 accumulated criterion; others absent from minimal base |
| C-26 | PASS | B-1/B-2/B-3/B-4 sub-conditions with priority rule (B-3 > B-2 > B-1 > B-4) and anti-blend instruction added |
| C-27 | FAIL | REQUIRES/PRODUCES/BLOCKS declarative headers retained; imperative form absent |

**Composite V-01** = (5/5 × 60) + (2/3 × 30) + (5/19 × 85) = 60 + 20 + 22 = **102**

---

### V-02 — Imperative phrasing only (v7 INTAKE structure base)

Base: v7 V-03 INTAKE structure (split input registers per artifact type, scripted fallback in Branch B, no Branch B sub-conditions).

**Essential (5/5)** — all pass, inherited from INTAKE base (same table as V-01, omitted for brevity).

**Recommended (3/3)**

| ID | Result | Evidence |
|----|--------|---------|
| C-06 | PASS | INTAKE structure explicitly invokes secondary roles per register |
| C-07 | PASS | Split registers produce a reconciliation step across artifact types; conflicting R-IDs flagged by name |
| C-08 | PASS | Amendment list present |

**Aspirational (10/19)**

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Branch B fallback documented; scripted response block present in INTAKE base |
| C-10 | PASS | INTAKE structure includes a cross-namespace signal row in the artifact intake table |
| C-11 | FAIL | No pre-printed cross-namespace column in Purpose/Design section |
| C-12 | PASS | INTAKE split-register structure embeds role annotations inline within each register's section |
| C-13 | FAIL | Per-row P0 status column absent; INTAKE base uses coverage count |
| C-14 | PASS | INTAKE scan instruction names the requirements artifact; absence of named conflict is prohibited without named scan |
| C-15 | FAIL | Cross-namespace signal appears in one location (intake table), not two independent structural locations |
| C-16 | FAIL | PM assignment step present in INTAKE but not explicitly phased before writing begins |
| C-17 | PASS | INTAKE base has named gate token blocking Phase 2 until Phase 1 intake is complete |
| C-18 | PASS | Branch B fallback text is a complete scripted block (demarcated); C-27 does not remove this |
| C-19 | FAIL | No ordinal location markers; multi-location fields are not labeled |
| C-20 | FAIL | C-27 applies imperative form per-block but split registers do not unify role + source into a single declaration |
| C-21 | FAIL | Gate token from C-17 present but no explicit structural invalidity rule |
| C-22–C-25 | 3/4 PASS | INTAKE structure satisfies three v7 accumulated criteria (split-register artifacts, reconciliation phase, actor-bound intake); one requiring two-location structural field absent |
| C-26 | FAIL | Branch B not subdivided; hypothesis confirms C-27 is independent of B-subdivision |
| C-27 | PASS | All role-phase blocks use "Actor: scan Source → fill Target" form; REQUIRES/PRODUCES/BLOCKS absent throughout |

**Composite V-02** = (5/5 × 60) + (3/3 × 30) + (10/19 × 85) = 60 + 30 + 45 = **135**

---

### V-03 — PM-first phase ordering (v7 full-combination base)

Base: v7 V-05 full-combination (all v7 criteria satisfied, including REQUIRES/PRODUCES/BLOCKS, INERTIA guards, gate tokens, PM coverage pre-assignment). New axis: Phase 1 (PM pre-assignment) runs before Phase 0B (inertia analysis); inertia guard Elimination Paths can reference pre-assigned requirement IDs.

**Essential (5/5)** — all pass.

**Recommended (3/3)** — all pass (v7 full-combination baseline).

**Aspirational (17/19)**

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Fallback conditional named; v7 base |
| C-10 | PASS | Cross-namespace signal traced to named artifact; v7 base |
| C-11 | PASS | Pre-printed column structurally present; v7 base |
| C-12 | PASS | Role annotation embedded inline in target section; v7 base |
| C-13 | PASS | Per-row P0 status column with named spec entries; v7 base |
| C-14 | PASS | Inertia guard Elimination Paths now name pre-assigned requirement IDs (stronger than v7 baseline), satisfying "named blank requiring specific ID format" |
| C-15 | PASS | Cross-namespace field in two structurally independent locations; v7 base |
| C-16 | PASS | PM phase explicitly ordered first; PM-CONTRACT-SEAL is written before Phase 0B begins; unambiguous "before writing" compliance |
| C-17 | PASS | Named gate token blocks downstream phase; v7 base |
| C-18 | PASS | Scripted VERBATIM fallback text present; v7 base |
| C-19 | PASS | Ordinal location markers on multi-location fields; v7 base |
| C-20 | PASS | Unified role-and-source declaration in v7 full base |
| C-21 | PASS | PM-CONTRACT-SEAL gate carries explicit invalidity rule: emitting seal without [PM-COVERAGE-TABLE] present in same block declared structurally invalid; PM-first ordering makes this mechanically clear |
| C-22–C-25 | 4/4 PASS | All v7 accumulated criteria satisfied by full-combination base |
| C-26 | **FAIL** | Branch B not subdivided; no B-1/B-2/B-3/B-4 sub-conditions or VERBATIM blocks |
| C-27 | **FAIL** | REQUIRES/PRODUCES/BLOCKS declarative headers retained; imperative phrasing absent |

**Composite V-03** = (5/5 × 60) + (3/3 × 30) + (17/19 × 85) = 60 + 30 + 76 = **166**

---

### V-04 — C-26 + C-27 combined (v7 full-combination base, no PM-first)

Base: v7 V-05 full-combination. New: B-1/B-2/B-3/B-4 VERBATIM sub-conditions + imperative "Actor: scan Source → fill Target" form throughout; REQUIRES/PRODUCES/BLOCKS absent.

**Essential (5/5)** — all pass.

**Recommended (3/3)** — all pass.

**Aspirational (19/19)**

| ID | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | B-1/B-2/B-3/B-4 cover all artifact-absent combinations; fallback documented per sub-condition |
| C-10 | PASS | Cross-namespace signal named; v7 base |
| C-11 | PASS | Pre-printed column present; v7 base |
| C-12 | PASS | C-27 imperative form applied inline within each role-phase block; inline placement verifiable in template |
| C-13 | PASS | Per-row P0 status column; v7 base |
| C-14 | PASS | Imperative "PM: scan [REQUIREMENTS-ARTIFACT] → confirm each R-ID" form names inspection source explicitly; satisfies named-scan instruction requirement |
| C-15 | PASS | Cross-namespace field in two locations; v7 base |
| C-16 | PASS | PM assignment step precedes writing phases; v7 base satisfies "assignment must precede writing"; no PM-first phase reordering but PM step position unchanged |
| C-17 | PASS | Named gate token with downstream blocking; v7 base |
| C-18 | PASS | B-1/B-2/B-3/B-4 VERBATIM blocks are complete scripted response text |
| C-19 | PASS | Ordinal location markers; v7 base |
| C-20 | PASS | C-27 imperative form unifies role + source in single "Actor: scan Source → fill Target" directive; combined with v7 structural binding, satisfies unified declaration |
| C-21 | PASS | Gate token invalidity rule present from v7 base; PM-COVERAGE-TABLE as prerequisite evidence named in same block |
| C-22–C-25 | 4/4 PASS | v7 full-combination base |
| C-26 | PASS | B-1/B-2/B-3/B-4 sub-conditions with priority rule B-3 > B-2 > B-1 > B-4; anti-blend instruction present |
| C-27 | PASS | Imperative register applied throughout; REQUIRES/PRODUCES/BLOCKS absent in all phases |

**Composite V-04** = (5/5 × 60) + (3/3 × 30) + (19/19 × 85) = 60 + 30 + 85 = **175**

**Quality note**: C-16 and C-21 pass but on the weaker side — PM phase is positioned correctly but phase sequencing is not enforced structurally (Phase 0B can technically start before PM phase completes). C-21's invalidity rule names PM-COVERAGE-TABLE as prerequisite evidence but the ordering constraint is implicit.

---

### V-05 — Full combination (v7 full + C-26 + C-27 + PM-first ordering)

Base: V-04 + Phase 1 (PM pre-assignment) explicitly ordered before Phase 0B (inertia analysis). PM-CONTRACT-SEAL gates Phase 0B. Inertia guard Elimination Paths cite pre-assigned requirement IDs.

**Essential (5/5)** — all pass.

**Recommended (3/3)** — all pass.

**Aspirational (19/19)**

All V-04 passes carry forward. Quality distinctions:

| ID | Upgrade over V-04 |
|----|------------------|
| C-14 | Elimination Paths now cite named requirement IDs (e.g., "R-03, R-07 confirmed absent") rather than generic counts; scan instruction bound to PM-COVERAGE-TABLE output |
| C-16 | Phase 1 structurally precedes Phase 0B by template construction, not just intent; "before writing" is unambiguous — Phase 0B cannot start without [PM-CONTRACT-SEAL] |
| C-21 | [PM-CONTRACT-SEAL] invalidity rule is mechanically enforced by phase ordering: emitting the seal without [PM-COVERAGE-TABLE] in the Phase 1 block makes Phase 0B block structurally unresolvable; the invalidity rule and its triggering evidence are co-located in the same phase block |

**Composite V-05** = (5/5 × 60) + (3/3 × 30) + (19/19 × 85) = 60 + 30 + 85 = **175**

**Quality note**: V-05 is the stronger 175. The PM-first axis makes C-16 and C-21 structural facts rather than behavioral contracts. The combination of PM-first + C-26 sub-conditions means Elimination Paths in inertia guards gain both specificity (named IDs) and sub-condition discrimination (B-1 vs B-3 paths get different ID sets). This is the most defensible pass of the full rubric.

---

## Excellence Signals from Top Variation (V-05)

Three axes combine cleanly with zero interaction effects observed:

1. **Priority-ordered sub-conditional branching eliminates coverage ambiguity** — the B-3 > B-2 > B-1 > B-4 priority rule resolves multi-condition overlap deterministically; each sub-condition emits its VERBATIM block without model-side blending logic; pattern is reusable for any spec with partially overlapping input-presence scenarios.

2. **Phase sequencing as a data-availability contract** — placing Phase 1 (PM pre-assignment) before Phase 0B means Phase 0B operations have guaranteed access to [PM-COVERAGE-TABLE] output; this converts C-21's invalidity rule from a behavioral instruction into a structural fact; pattern generalizes to any multi-phase spec where a later phase needs certified output from an earlier one.

3. **Uniform imperative register converts role headers into executable directives** — "Actor: scan Source → fill Target" applied uniformly across all role-phase blocks means each block is parseable as a single unit with named owner, named input, and named output; the register change is purely syntactic (C-27) but strengthens C-14 and C-20 as side-effects by making the inspection source and role always co-present in the same directive.

---

## Final Rankings

| Rank | Variation | Composite | Decisive Factor |
|------|-----------|-----------|-----------------|
| 1 | V-05 | 175 | All three axes; strongest C-16 and C-21 quality |
| 1 | V-04 | 175 | C-26 + C-27 sufficient for 27/27 pass; C-16/C-21 quality lower |
| 3 | V-03 | 166 | All v7 criteria + PM-first; C-26/C-27 absent |
| 4 | V-02 | 135 | INTAKE base + C-27; missing C-26, C-15, C-16, C-19–C-21 |
| 5 | V-01 | 102 | Minimal base + C-26; fails C-07, C-10–C-13, C-16–C-17, C-19–C-21, C-27 |

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["priority-ordered sub-conditional branching with anti-blend enforcement — B-3 > B-2 > B-1 > B-4 priority rule prevents coverage gaps when multiple artifact-presence conditions overlap, and each branch emits its own VERBATIM block with no model-side composition", "phase sequencing as a data-availability contract — placing PM pre-assignment before inertia analysis converts the gate-token invalidity rule from a behavioral instruction to a structural fact, because Phase 0B cannot fire until PM-CONTRACT-SEAL is present", "uniform imperative register as a side-effect amplifier — applying Actor:scan Source→fill Target form across all role-phase blocks strengthens C-14 and C-20 as structural side-effects, because the inspection source and responsible actor are always co-present in the same parseable directive"]}
```
