# Quest Score — campaign-track — Round 11

**Rubric**: v11 | **Scoring date**: 2026-03-16
**Variations present**: V-01 (full text), V-02 (partial — truncated after field type key)

---

## Point Structure

| Tier | Per Criterion | Count | Max |
|------|--------------|-------|-----|
| Essential | 10 | 5 | 50 |
| Recommended | 7 | 3 | 21 |
| Aspirational C-09–C-16 | 3 | 8 | 24 |
| C-36 (new) | 7.5 | 1 | 7.5 |
| C-37 (new) | 7.5 | 1 | 7.5 |
| C-17–C-21 | 3 | 5 | 15 *(text not available — unscoreable)* |
| **Scoreable max** | | | **110** |
| **Rubric max** | | | **137** |

---

## V-01 — Role Sequence

### Essential

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 Four-phase structure | **PASS (10)** | Registration / Planning / Analysis / Narration — four labeled, sequenced phases |
| C-02 Artifact-per-phase | **PASS (10)** | `{topic}-new`, `-roadmap`, `-status`, `-story` — four distinct artifacts, each unique, each with write path |
| C-03 Nine-namespace coverage table | **PASS (10)** | Section A — all nine rows, all five columns (Namespace / Planned / Collected / Missing / Zero-Signal) |
| C-04 Verdict from enumerated set | **PASS (10)** | `READY \| NOT READY \| CONDITIONALLY READY` — set declared; verdict constrained to it |
| C-05 Narrative verdict with evidence | **PASS (10)** | Phase 4 four-component structure: verdict, hypothesis mutation, echo findings, ≥3 next-signal recs |

**Essential subtotal: 50/50**

### Recommended

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-06 Artifact write paths | **PASS (7)** | All four phases end with explicit `Write to: simulations/{namespace}/{topic}-{artifact}-{date}.md` |
| C-07 Coverage ratio + readiness statement | **PASS (7)** | Section B — `coverage_ratio: {collected}/{planned}` and `readiness_preliminary:` token |
| C-08 Cross-namespace signal balance | **PASS (7)** | Nine-row table; `YES/NO` zero-signal flag per namespace; explicit zero-signal count visible |

**Recommended subtotal: 21/21**

### Aspirational

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-09 Echo integration | **PASS (3)** | Section C — "Echo Candidates" with explicit `echo_candidates: NONE` fallback |
| C-10 Dual-session delta | **FAIL (0)** | No delta section; session-to-session signal change not tracked |
| C-11 Role-gated phases | **PASS (3)** | ROLES table — four distinct labels: Signal Registrar / Planner / Auditor / Narrator; role consistency enforced |
| C-12 Explicit progression gates | **PASS (3)** | "Gate: Do not begin Phase X until `{artifact}` has been written." — present at all three transitions, naming artifact by file |
| C-13 Empty-state as named section | **PASS (3)** | `EMPTY-STATE BEHAVIOR (first invocation)` — dedicated labeled section with per-phase behavior for all four phases |
| C-14 Per-role prohibition lists | **PASS (3)** | ROLES table column "Prohibited Actions" — named forbidden behaviors per role, not just role title inference |
| C-15 Typed output contracts | **PARTIAL (1.5)** | Phase 3 states "Integer values only for count fields" and `YES/NO` for zero-signal flag; partial typing — not systematic typed contracts on all fields across all phases |
| C-16 Terminal completion checklist | **PASS (3)** | Terminal checklist — per-phase PASS conditions named; "re-run that phase only. Do not restart the full campaign." — targeted re-run language explicit |

**C-17–C-21**: text not available in rubric — unscoreable; excluded from denominator

**Aspirational subtotal: 19.5/24**

### New Criteria (v11)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-36 Causal framing at Phase 4 activation | **PASS (7.5)** | OBLIGATION header: "If Phase 4 completes without writing this artifact, `verdict_after` in `{topic}-status-{date}.md` becomes stale — the delta record reflects pre-session hypothesis state rather than the narrative conclusion reached here." — assertion → named consequence at activation site |
| C-37 Cascade scope justification | **FAIL (0)** | No cascade rule present; no scope exclusion with causal justification |

**New criteria subtotal: 7.5/15**

### V-01 Total

| Section | Score | Max |
|---------|-------|-----|
| Essential | 50 | 50 |
| Recommended | 21 | 21 |
| Aspirational | 19.5 | 24 |
| New (C-36, C-37) | 7.5 | 15 |
| **Total** | **98** | **110 scoreable** |

**98/110 = 89.1% of scoreable criteria**

---

## V-02 — Output Format

*Note: V-02 content is truncated — only axis declaration, hypothesis, and field type key are present. Criteria scored as: PASS where the shown text confirms it, FAIL where the axis suggests absence, PARTIAL where baseline structure is presumed but the feature is not this variation's axis.*

### Essential

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 | **PASS (10)** | "Execute four phases in sequence" — stated |
| C-02 | **PASS (10)** | "Each phase produces exactly one artifact" — explicit |
| C-03 | **PASS (10)** | Baseline — assumed present (not shown but structural requirement) |
| C-04 | **PASS (10)** | Assumed present — enumerated verdict is baseline |
| C-05 | **PASS (10)** | Assumed present |

**Essential subtotal: 50/50**

### Recommended

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-06 | **PASS (7)** | Assumed — format axis would preserve write paths |
| C-07 | **PASS (7)** | Assumed — coverage ratio is baseline |
| C-08 | **PASS (7)** | Assumed — nine-namespace table is baseline |

**Recommended subtotal: 21/21**

### Aspirational

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-09 Echo integration | **PASS (3)** | Assumed — echo section is baseline |
| C-10 Dual-session delta | **FAIL (0)** | Not this axis |
| C-11 Role-gated phases | **FAIL (0)** | Not this axis; no role names in shown text |
| C-12 Explicit progression gates | **PARTIAL (1.5)** | Likely basic sequence enforcement, not named artifact gates |
| C-13 Empty-state named section | **FAIL (0)** | Not this axis — absent from shown text |
| C-14 Per-role prohibition lists | **FAIL (0)** | Not this axis — no roles, no prohibitions |
| C-15 Typed output contracts | **PASS (3)** | **This IS the axis.** Field type key explicit: integer / token / string / list[string] — all fields typed |
| C-16 Terminal completion checklist | **PARTIAL (1.5)** | Likely minimal checklist; no targeted re-run language in shown text |

**Aspirational subtotal: 9/24**

### New Criteria (v11)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-36 | **FAIL (0)** | No OBLIGATION header in shown text |
| C-37 | **FAIL (0)** | No cascade rule |

**New criteria subtotal: 0/15**

### V-02 Total

| Section | Score | Max |
|---------|-------|-----|
| Essential | 50 | 50 |
| Recommended | 21 | 21 |
| Aspirational | 9 | 24 |
| New | 0 | 15 |
| **Total** | **80** | **110 scoreable** |

**80/110 = 72.7% of scoreable criteria** *(caution: estimated from partial text)*

---

## Rankings

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | **V-01 — Role Sequence** | **98/110** | YES | Full text; C-36 PASS; C-37 FAIL; C-15 PARTIAL |
| 2 | V-02 — Output Format | ~80/110 | YES (estimated) | Truncated; strong on C-15; weak on C-11, C-13, C-14 |

---

## Excellence Signals from V-01

V-01's margin comes from three clusters operating in combination:

1. **Role table + prohibition column** — the tabular format (role / prohibited actions side-by-side) makes C-11 and C-14 scannable at a glance; prevents the common failure mode of per-role behavior buried in prose
2. **Artifact-named gate language** — "Do not begin Phase X until `{topic}-artifact-{date}.md` has been written" — the gate names the specific artifact file, not just the phase label; tighter contract than generic ordering language
3. **OBLIGATION header with named stale consequence (C-36)** — already promoted to rubric; the pattern holds: naming the specific broken state (stale `verdict_after`) at the activation site rather than a generic obligation warning

No new patterns beyond those already captured in v11 rubric criteria.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": []}
```
