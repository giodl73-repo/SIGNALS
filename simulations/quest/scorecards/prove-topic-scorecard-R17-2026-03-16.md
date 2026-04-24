## prove-topic — Quest Score Round 17 (Rubric v14)

**Skill**: prove-topic | **Round**: R17 | **Date**: 2026-03-16 | **Rubric**: v14

---

### Scoring Reference

| Criterion | Weight | Points |
|-----------|--------|--------|
| C-01 through C-05 | essential | 12 pts each → 60 total |
| C-06 through C-08 | recommended | 10 pts each → 30 total |
| C-09 through C-10 | aspirational | 5 pts each → 10 total |

Formula: `(E/5 * 60) + (R/3 * 30) + (A/2 * 10)`

---

### V-01 — Per-Stage Inertia Displacement

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | SETUP → S1 → S2 → S3 → S4 → S5, all present with declared stage headers and exit signals |
| C-02 | Scout artifact named before hypothesis | **PASS** | SETUP globs `simulations/scout/{topic}-scout-*.md`; "SCOUT READY cannot fire without a found file"; scout_source set before Stage 1 opens |
| C-03 | Progressive writes — one per stage | **PASS** | Six write instructions: S1 hypothesis, S2 websearch, S3 intelligence, S4 analysis, S5 Write A draft + Write B brief |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | `Close: Evidence brief for {topic} is ready for /topic-story.` — explicit downstream named |
| C-05 | Full artifact paths on every write | **PASS** | All six write instructions name full `simulations/prove/{sub}/{topic}-{signal}-{date}.md` paths |
| C-06 | Forward-only with scout gate | **PASS** | Each stage gated: "STAGE N cannot begin until [prior signal] fires"; SCOUT READY blocks on absent file |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 frontmatter: `scout_source:` + `status_quo_comparator:` both named |
| C-08 | Thin flags at point of discovery | **PASS** | S2: "Flag thin or absent evidence at the point of discovery — not deferred: THIN: [area] -- [gap]"; S3: same inline |
| C-09 | Thin propagates to synthesis with claim qualification | **PASS** | Write A: "name source stage, weakened claim, and adjusted confidence (e.g., 'Confidence reduced — Stage 2 found no peer data for claim X')"; explicit per-claim tracing |
| C-10 | Hypothesis structurally blocked until scout confirmed | **PASS** | SCOUT READY cannot fire without found file (halts); STAGE 1 cannot begin until SCOUT READY fires — chain blocks hypothesis entry |

**Scores**: E 5/5, R 3/3, A 2/2 → **(5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 100/100** | Golden: **YES**

---

### V-02 — Resume Audit

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | RESUME AUDIT is a pre-S1 structural step, not a core stage; S1–S5 present in order with exit signals |
| C-02 | Scout artifact named before hypothesis | **PASS** | SETUP globs scout; "SCOUT READY cannot fire without a found file"; scout_source named |
| C-03 | Progressive writes — one per stage | **PASS** | Six write instructions across five stages; RESUME-SKIP stages bypass without merging writes |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | `Close: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full artifact paths on every write | **PASS** | All six write instructions carry full paths; resume audit also lists all five paths explicitly — path determinism structural requirement |
| C-06 | Forward-only with scout gate | **PASS** | SCOUT READY → AUDIT COMPLETE → STAGE 1 chain; each gated; scout absence halts before any stage |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 frontmatter: `scout_source:` — also carried from existing artifact if RESUME-SKIP |
| C-08 | Thin flags at point of discovery | **PASS** | S2: "not deferred: THIN: [area] -- [gap]"; S3: "Flag thin findings" inline |
| C-09 | Thin propagates to synthesis with claim qualification | **PASS** | Write A iterates "For each hypothesis claim" → thin entries name source stage and adjusted confidence; per-claim iteration makes the weakened claim structurally identified |
| C-10 | Hypothesis structurally blocked until scout confirmed | **PASS** | SCOUT READY fires only with found file; STAGE 1 requires AUDIT COMPLETE (requires SCOUT READY); two-gate chain blocks hypothesis |

**Scores**: E 5/5, R 3/3, A 2/2 → **(5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 100/100** | Golden: **YES**

**Additional signal**: Resume audit makes C-05 a mechanical necessity — artifact paths must be deterministic for globbing to work, turning path discipline from formatting preference into resumability precondition.

---

### V-03 — Confidence Chain with Count Gates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | S1–S5 in order; confidence register initialized in SETUP, populated per stage |
| C-02 | Scout artifact named before hypothesis | **PASS** | SETUP globs scout; "SCOUT READY cannot fire without a found file"; scout_source set |
| C-03 | Progressive writes — one per stage | **PASS** | Six write instructions; count gates close before write fires at each stage |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | `Close: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full artifact paths on every write | **PASS** | All six write instructions carry full paths |
| C-06 | Forward-only with scout gate | **PASS** | SCOUT READY gate + per-stage "cannot begin until [prior signal] fires" |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 frontmatter: `scout_source:` + `confidence_prior:` |
| C-08 | Thin flags at point of discovery | **PASS** | S2: THIN flags + "THIN COVERAGE" count-gate note at discovery; S3: same pattern for internal signals |
| C-09 | Thin propagates to synthesis with claim qualification | **PASS** | Write A: "name source stage, weakened claim, and adjusted confidence delta (e.g., 'Stage 2 source_count = 1: -1 confidence on claim X')" — most explicit form; chain equation in Write B shows per-stage contribution |
| C-10 | Hypothesis structurally blocked until scout confirmed | **PASS** | SCOUT READY cannot fire without found file; STAGE 1 gated on SCOUT READY |

**Scores**: E 5/5, R 3/3, A 2/2 → **(5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 100/100** | Golden: **YES**

**Additional signal**: Count gates (`source_count >= 3`, `signal_count >= 2`) appear in exit signal payloads — evidence sufficiency becomes a visible, stage-boundary-level constraint rather than a post-hoc synthesis observation.

---

### V-04 — Per-Stage Inertia + Resume Audit

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | RESUME AUDIT pre-S1; S1–S5 in order with exit signals |
| C-02 | Scout artifact named before hypothesis | **PASS** | SETUP globs scout; SCOUT READY cannot fire without found file; inertia_anchor also named from scout |
| C-03 | Progressive writes — one per stage | **PASS** | Six write instructions; resume-skip stages skip execution, not writes when running |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | `Close: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full artifact paths on every write | **PASS** | All six write instructions carry full paths; resume audit lists all five paths |
| C-06 | Forward-only with scout gate | **PASS** | Three-gate chain: SCOUT READY → AUDIT COMPLETE → STAGE 1 |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 frontmatter: `scout_source:` + `status_quo_comparator:` |
| C-08 | Thin flags at point of discovery | **PASS** | S2/S3: THIN inline flags; inertia_delta also captures displacement shift inline |
| C-09 | Thin propagates to synthesis with claim qualification | **PASS** | Write A per-claim iteration; "name source stage and adjusted confidence" per claim; Write B references displacement_verdict from S4 |
| C-10 | Hypothesis structurally blocked until scout confirmed | **PASS** | SCOUT READY halt on absent file; STAGE 1 blocked until AUDIT COMPLETE (requires SCOUT READY) |

**Scores**: E 5/5, R 3/3, A 2/2 → **(5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 100/100** | Golden: **YES**

**Combination note**: inertia_anchor survives the resume boundary — AUDIT COMPLETE carries it forward for resumed stages. V-01 and V-02 coexist cleanly; no structural conflict detected.

---

### V-05 — Full Stack (All Three + R2 Champion)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All five sub-skills in sequence | **PASS** | RESUME AUDIT pre-S1; S1–S5 in order; confidence chain, inertia, and resume all layered without disrupting stage sequence |
| C-02 | Scout artifact named before hypothesis | **PASS** | SETUP: glob, "SCOUT READY cannot fire without a found file", scout_source + inertia_anchor + confidence chain register all initialized |
| C-03 | Progressive writes — one per stage | **PASS** | Six write instructions; count gates and resume-skip both handled per-stage before write fires |
| C-04 | Synthesis signals readiness for topic-story | **PASS** | `Close: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full artifact paths on every write | **PASS** | All six write instructions carry full `simulations/prove/{sub}/...` paths; resume audit lists all five deterministic paths |
| C-06 | Forward-only with scout gate | **PASS** | SCOUT READY → AUDIT COMPLETE → S1; each subsequent stage gated on prior signal |
| C-07 | Scout anchor in hypothesis artifact | **PASS** | Stage 1 frontmatter: `scout_source:`, `status_quo_comparator:`, `confidence_prior:` — three-field anchor, richest of any variation |
| C-08 | Thin flags at point of discovery | **PASS** | S2: THIN flags + "THIN WEB COVERAGE" count-gate note; S3: THIN flags + "THIN INTERNAL" note; both inline at discovery |
| C-09 | Thin propagates to synthesis with claim qualification | **PASS** | Write A: "name source stage, weakened claim, and confidence delta (e.g., 'Stage 2 THIN WEB COVERAGE: s2_delta = -1 on claim X')"; Write B states confidence_final chain equation + displacement_verdict — most complete propagation of any variation |
| C-10 | Hypothesis structurally blocked until scout confirmed | **PASS** | SCOUT READY cannot fire without found file (halt); STAGE 1 blocked until AUDIT COMPLETE; three-gate chain is the strongest blocking structure |

**Scores**: E 5/5, R 3/3, A 2/2 → **(5/5 × 60) + (3/3 × 30) + (2/2 × 10) = 100/100** | Golden: **YES**

---

### Variation Rankings

| Rank | Var | Score | Golden | Distinguishing feature |
|------|-----|-------|--------|----------------------|
| 1 | V-05 | 100/100 | YES | All three axes + full R2 stack; richest Stage 1 frontmatter (three fields); chain equation + displacement_verdict in Write B; most complete C-09 exemplar |
| 2 | V-04 | 100/100 | YES | Inertia + resume coexist cleanly; inertia_anchor survives resume boundary |
| 3 | V-03 | 100/100 | YES | Most explicit count-gate machinery; confidence chain equation is visible at synthesis |
| 4 | V-01 | 100/100 | YES | Per-stage displacement tracking, cleanest single-axis implementation |
| 5 | V-02 | 100/100 | YES | Resume audit enforces C-05 as structural necessity; clean two-gate chain |

All five hit the ceiling. Round 17 replicates R2's outcome: zero discriminating failures at v14. Pattern ceiling confirmed.

---

### Excellence Signals from V-05

**1. Inertia delta as first-class evidence chain** — `s2_inertia_delta` and `s3_inertia_delta` flow as named fields through exit signal payloads into Stage 4's `displacement_verdict`. The displacement conclusion is not a post-hoc synthesis judgment but the mechanical product of per-stage evidence assessments. This makes inertia displacement traceable at every stage boundary.

**2. Count-gated exit signals enforce minimum evidence sufficiency** — `source_count >= 3` and `signal_count >= 2` appear in exit signal payloads. The gate either clears on count or records an explicit "THIN COVERAGE" note that propagates to synthesis. Evidence sufficiency is enforced at the stage boundary, not discovered during synthesis.

**3. Resume audit as C-05 structural enforcer** — The pre-S1 glob requires deterministic artifact paths at every stage; resumability cannot work without them. This turns artifact path discipline from a formatting preference into a mechanical precondition.

---

### New Pattern Candidates for Rubric v15

These two patterns appeared consistently across three or more variations and produced structural differentiation:

1. **Per-stage inertia delta chaining** (V-01, V-04, V-05): displacement tracking as an evidence-stage output that aggregates structurally into Stage 4, making displacement_verdict a derived value rather than an assertion.

2. **Count-gated exit signals with numeric confidence chain** (V-03, V-05): minimum source thresholds enforced before exit signal fires; confidence chain equation visible in synthesis; evidence sufficiency becomes observable at every stage boundary.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-stage inertia delta chaining: s2_inertia_delta and s3_inertia_delta flow through exit signal payloads into Stage 4 displacement_verdict, making displacement a derived chain value not a synthesis assertion", "count-gated exit signals with numeric confidence chain: source_count >= 3 and signal_count >= 2 gate each stage exit signal, confidence_prior + s2_delta + s3_delta + s4_delta = confidence_final chain equation visible at synthesis"]}
```
