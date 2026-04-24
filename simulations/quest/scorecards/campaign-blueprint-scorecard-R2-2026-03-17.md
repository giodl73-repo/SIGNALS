# campaign-blueprint Rubric v2 — Scoring Report (Round 2)

## V-01 — Single Axis: Inertia Framing

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 — All three artifacts present at correct paths | Essential | **PARTIAL** (6) | Three phases produce three artifacts; no file paths specified in the prompt |
| C-02 — Spec has all five sections | Essential | **FULL** (12) | Phase 1 explicitly lists PURPOSE / REQUIREMENTS (MoSCoW) / DESIGN / CONSTRAINTS / OPEN QUESTIONS in order |
| C-03 — Proposal: 3+ options, do-nothing, RECOMMENDATION | Essential | **FULL** (12) | Option 0 from Phase 0 name, Option 1, Option 2, RECOMMENDATION — all present |
| C-04 — Pitch: exec / developer / maker | Essential | **FULL** (12) | Phase 3 names all three versions explicitly |
| C-05 — Sequence integrity | Essential | **FULL** (12) | Completion Check block verifies spec→proposal→pitch chain; no contradictions mechanically possible |
| C-06 — Inertia baseline in all three artifacts | Recommended | **FULL** (10) | Phase 1 Spec: "Include one sentence connecting to the inertia baseline." Phase 2 Proposal: "Reference the inertia baseline." Phase 3 Pitch exec: "cost of inertia"; maker: "before/after" |
| C-07 — Scout signal scan | Recommended | **FAIL** (0) | No mention of scout signals anywhere in V-01 |
| C-08 — Spec self-review: 2+ specific open questions | Recommended | **FULL** (10) | "At least two specific questions (not boilerplate)" required — paired with discipline split |
| C-09 — Artifact contract matrix declared | Aspirational | **FAIL** (0) | No READ/WRITE/PRESERVE/CARRIES FORWARD matrix; Phase 0 is inertia-only |
| C-10 — Pitch anti-positioning: 2+ "what this is NOT" | Aspirational | **FULL** (5) | "Each version must include at least one 'what this is NOT' statement" — 3 versions × 1 = ≥3 total |
| C-11 — Do-nothing: quantified cost-of-inertia template | Aspirational | **FULL** (5) | Phase 0 requires filling in time/effort/risk dimensions before writing; Phase 2 Option 0 carries the template forward |
| C-12 — Execution gate markers | Aspirational | **FULL** (5) | `[SPEC WRITTEN]`, `[PROPOSAL WRITTEN — Option X recommended]`, `[PITCH WRITTEN]` — all required; Completion Check verifies |
| C-13 — Open questions split by discipline | Aspirational | **FULL** (5) | Phase 1: "Product/User domain: … Technical/Architecture domain: …" — explicit split with labeled prompt |
| C-14 — Per-audience delta statement | Aspirational | **FULL** (5) | Phase 3: each version begins "What changes for [audience]: [one sentence naming the delta — not just vocabulary, but a named delta from the base recommendation]" |

**V-01 Total: 99 / 120 (82.5%)**

---

## V-02 — Single Axis: Execution Gate Markers

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 — All three artifacts present at correct paths | Essential | **PARTIAL** (6) | Three phases, three artifacts; no file paths specified |
| C-02 — Spec has all five sections | Essential | **FULL** (12) | All five sections in Phase 1 |
| C-03 — Proposal: 3+ options, do-nothing, RECOMMENDATION | Essential | **FULL** (12) | Option 0 / Option 1 / Option 2 / RECOMMENDATION present |
| C-04 — Pitch: exec / developer / maker | Essential | **FULL** (12) | Three versions explicitly named |
| C-05 — Sequence integrity | Essential | **FULL** (12) | Dependency checks *restate* prior artifact decisions before each phase; strongest mechanical enforcement of C-05 in any variant |
| C-06 — Inertia baseline in all three artifacts | Recommended | **PARTIAL** (5) | Proposal SITUATION: "Reference what users do without this feature" ✓; Pitch exec: "cost of not acting" ✓; Spec Phase 1 has no inertia reference requirement — only two of three artifacts covered |
| C-07 — Scout signal scan | Recommended | **FAIL** (0) | Not mentioned |
| C-08 — Spec self-review: 2+ specific open questions | Recommended | **FULL** (10) | "At least two specific, non-boilerplate questions that will affect design or implementation choices" |
| C-09 — Artifact contract matrix | Aspirational | **FAIL** (0) | Dependency checks are forward-looking gates, not READ/WRITE/PRESERVE contract declarations |
| C-10 — Pitch anti-positioning | Aspirational | **FULL** (5) | Each of 3 versions requires at least one "what this is NOT" |
| C-11 — Quantified cost-of-inertia in do-nothing | Aspirational | **FULL** (5) | "Include cost-of-inertia with at least one concrete dimension (time, effort, or risk)" |
| C-12 — Execution gate markers | Aspirational | **FULL** (5) | Dependency check blocks before + completion tags after every phase; richest implementation: `[PROPOSAL WRITTEN — Option X recommended — spec decisions honored: … — open questions blocking: …]` |
| C-13 — Open questions split by discipline | Aspirational | **FAIL** (0) | Phase 1 requires two non-boilerplate questions but no discipline split |
| C-14 — Per-audience delta statement | Aspirational | **FULL** (5) | Each pitch version has "What changes for [audience]: [name the delta]" |

**V-02 Total: 89 / 120 (74.2%)**

---

## Ranking

| Rank | Variant | Score | All Essential Full? | Golden? (≥80/120) |
|------|---------|-------|---------------------|-------------------|
| 1 | **V-01** | **99/120** | No (C-01 PARTIAL) | Yes (82.5%) |
| 2 | V-02 | 89/120 | No (C-01 PARTIAL) | Yes (74.2%) → No, 89/120 = 74.2% — below 80 |

V-01 clears the golden threshold (≥80/120). V-02 does not. Neither clears all essentials at FULL due to C-01's missing path specification.

**V-01 vs V-02 delta: +10 pts** — driven by C-06 (V-01 FULL vs PARTIAL: +5) and C-13 (V-01 FULL vs FAIL: +5).

---

## Excellence Signals from V-01

**Signal 1 — Pre-artifact forcing function**
Phase 0 is a *dedicated block that must be completed before writing any artifact begins*. This is structurally different from instructions embedded within an artifact phase — it creates an anchor that all three outputs are required to reference. C-06 becomes nearly impossible to miss because the inertia baseline exists as a named, visible block before Phase 1 opens.

**Signal 2 — Named competitor pattern**
Do-nothing is named explicitly ("give it a name, e.g., 'Option 0: Status Quo'"). The name then propagates — it appears in the proposal options list by reference to Phase 0. This makes the do-nothing option a first-class tracked entity, not a throwaway catch-all.

**Signal 3 — Blank-filling quantification template**
Rather than instructing "quantify the cost," Phase 0 presents a fill-in-the-blank structure with forced dimension selection (time / effort / risk). This prevents qualitative-drift by requiring the writer to choose *which* dimension before completing the section.

---

```json
{"top_score": 99, "all_essential_pass": false, "new_patterns": ["Pre-artifact forcing function: a dedicated Phase 0 block completed before any artifact is written anchors inertia baseline across all three outputs, making C-06 structurally enforced rather than instructionally hoped for", "Named competitor pattern: do-nothing option assigned an explicit name in Phase 0 so it propagates as a tracked entity through proposal options and pitch framing, not as a catch-all final option"]}
```
