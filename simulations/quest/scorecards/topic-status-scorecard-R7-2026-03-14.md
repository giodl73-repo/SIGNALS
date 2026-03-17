# Scorecard: `topic:status` — Round 7
**Rubric:** v7 (max 195) | **Date:** 2026-03-14

---

## Input Note

The variations document provided contains V-01 and V-02 fully. V-03–V-05 are absent from the input — the document is truncated after V-02's PHASE 4. Scoring proceeds on V-01 and V-02 only.

---

## Trace Artifact (Ground Truth)

Constructed to exercise all phases and failure paths:

```
Topic: auth-flow
strategy.md: present
Planned signals: scout-feasibility, scout-market, review-design, prove-prototype

Disk signals found:
  simulations/scout/auth-flow-feasibility-2026-03-10.md  (4 days old)
  simulations/review/auth-flow-design-2026-03-05.md      (9 days old — stale)

Verification:
  scout-feasibility  → VERIFIED   (disk match)
  scout-market       → UNVERIFIED (no disk match)
  review-design      → VERIFIED   (disk match, stale)
  prove-prototype    → UNVERIFIED (no disk match)

Coverage: 2/4 = 50% → PARTIAL
Stale: review-design (9 days old)
Highest priority risk: /prove:prototype auth-flow
```

---

## Criterion Scoring

### V-01 — Role sequence (discovery-first)

| ID | Tier | Pts | Result | Evidence |
|----|------|-----|--------|----------|
| C-01 | Essential | 15 | **PASS** | PHASE 1 runs `Glob: simulations/**/{topic}-*`, assigns DISK_SIGNALS before strategy load |
| C-02 | Essential | 15 | **PASS** | PHASE 2 reads `simulations/strategy.md`, extracts planned signals |
| C-03 | Essential | 15 | **PASS** | PHASE 4 computes `percent = VERIFIED / PLANNED * 100` |
| C-04 | Essential | 15 | **PASS** | COMMIT DECISION renders READY/PARTIAL/NOT READY with missing signal list |
| C-05 | Recommended | 10 | **PASS** | STALE EVIDENCE section with `{N} days old` format present |
| C-06 | Recommended | 10 | **PASS** | HIGHEST PRIORITY RISK section present, `/{namespace}:{signal} {topic}` format |
| C-07 | Recommended | 10 | **PASS** | "DISPLAY ONLY. Write no files." declared at top |
| C-08 | Aspirational | 5 | **PASS** | 9-namespace breakdown table with all namespace rows |
| C-09 | Aspirational | 5 | **PASS** | Register has per-signal `VERIFIED \| UNVERIFIED` status column |
| C-10 | Aspirational | 5 | **PASS** | Empty namespaces render `--` in Pct column |
| C-11 | Aspirational | 5 | **PASS** | PHASE 1: `if DISK_SIGNALS empty: output "No signals found" and stop` |
| C-12 | Aspirational | 5 | **PASS** | PHASE 2: absent strategy.md → `"commit exposure is unquantifiable"` + stop |
| C-13 | Tier 2 | 5 | **PASS** | Three `[LAYER N -- TYPE: ...]` labels present with semantic descriptors |
| C-14 | Tier 2 | 5 | **PASS** | LAYER 3 enforces render order: REGISTER → BY NAMESPACE → EXPOSURE → DECISION → STALE → RISK |
| C-15 | Tier 2 | 5 | **PASS** | Consistency guard: `if UNVERIFIED non-empty and percent = 100%, halt and recompute` |
| C-16 | Tier 2 | 5 | **PASS** | EXPOSURE SUMMARY section with `{found}/{planned} ({pct}%)` present |
| C-17 | Tier 3 | 5 | **PASS** | Role-sequence axis: PHASE 1 runs discovery before PHASE 2 loads strategy.md |
| C-18 | Tier 3 | 5 | **PASS** | Stale evidence format includes `({N} days old)` |
| C-19 | Tier 3 | 5 | **PASS** | Pre-display invariant: "COMMIT RISK REGISTER contains exactly one row per planned signal" |
| C-20 | Tier 4 | 5 | **PASS** | DISPLAY GATE phase declares pre-display invariant explicitly |
| C-21 | Tier 4 | 5 | **PASS** | 5 named execution phases with capitalized titles (PHASE 1 through PHASE 5) |
| C-22 | Tier 4 | 5 | **PASS** | `strategy.md: [FOUND \| NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]` — inline consequence annotation present |
| C-23 | Tier 5 | 5 | **FAIL** | Phase name is `COMMITMENT ASSERTION (per signal -- no batch evaluation)` — granularity is parenthetical annotation, not integral left-edge token; fails both-terms-as-prefix test |
| C-24 | Tier 5 | 5 | **PASS** | `[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]` — layer label references phase name |
| C-25 | Tier 5 | 5 | **PASS** | `if absent: COMMITMENT ASSERTION cannot execute` — consequence inline; field → behavior annotation present |
| C-26 | Tier 6 | 5 | **FAIL** | C-23 fails → cannot satisfy C-26. Granularity term `per signal` is in parenthetical position, not leftmost token of phase name |
| C-27 | Tier 6 | 5 | **FAIL** | LAYER 2 label is `COMMITMENT ASSERTION gate` — missing `PER-SIGNAL` prefix. Full C-23 compressed form not propagated. Requires C-23 ∧ C-24; C-23 fails |
| C-28 | Tier 6 | 5 | **PASS** | `if absent: COMMITMENT ASSERTION cannot execute` names PHASE 3 (`COMMITMENT ASSERTION`) — a specific C-21 execution phase, not a generic epistemic consequence. Matches rubric's positive exemplar exactly |

**V-01 Subtotals:**

| Tier | Max | Earned |
|------|-----|--------|
| Essential C-01–04 | 60 | 60 |
| Recommended C-05–07 | 30 | 30 |
| Aspirational C-08–12 | 25 | 25 |
| Tier 2 C-13–16 | 20 | 20 |
| Tier 3 C-17–19 | 15 | 15 |
| Tier 4 C-20–22 | 15 | 15 |
| Tier 5 C-23–25 | 15 | 10 |
| Tier 6 C-26–28 | 15 | 5 |
| **Total** | **195** | **180** |

---

### V-02 — Output format (full tier 6 compliance)

| ID | Tier | Pts | Result | Evidence |
|----|------|-----|--------|----------|
| C-01 | Essential | 15 | **PASS** | PHASE 1 globs `simulations/**/{topic}-*`, assigns DISK_SIGNALS |
| C-02 | Essential | 15 | **PASS** | PHASE 2 reads `simulations/strategy.md` with absent-topic stop condition |
| C-03 | Essential | 15 | **PASS** | PHASE 3 computes `percent = VERIFIED / PLANNED * 100` |
| C-04 | Essential | 15 | **PASS** | COMMIT DECISION with READY/PARTIAL/NOT READY and missing signal list |
| C-05 | Recommended | 10 | **PASS** | STALE EVIDENCE with `{N} days old` and absence-of-stale guard |
| C-06 | Recommended | 10 | **PASS** | HIGHEST PRIORITY RISK with `/{namespace}:{signal} {topic}` format |
| C-07 | Recommended | 10 | **PASS** | "DISPLAY ONLY. Write no files." declared |
| C-08 | Aspirational | 5 | **PASS** | 9-namespace table with all rows |
| C-09 | Aspirational | 5 | **PASS** | Per-signal `VERIFIED \| UNVERIFIED -- if absent: ships without this signal on commit` |
| C-10 | Aspirational | 5 | **PASS** | `--` in empty namespace Pct cells |
| C-11 | Aspirational | 5 | **PASS** | PHASE 1 stop condition on empty DISK_SIGNALS |
| C-12 | Aspirational | 5 | **PASS** | PHASE 2 stop condition on missing strategy.md or missing topic entry |
| C-13 | Tier 2 | 5 | **PASS** | Three `[LAYER N -- TYPE: ...]` labels present |
| C-14 | Tier 2 | 5 | **PASS** | LAYER 3 enforces render sequence |
| C-15 | Tier 2 | 5 | **PASS** | Consistency guard present in PHASE 3 |
| C-16 | Tier 2 | 5 | **PASS** | EXPOSURE SUMMARY section present |
| C-17 | Tier 3 | 5 | **PASS** | Phases proceed in logical acquisition→assertion order |
| C-18 | Tier 3 | 5 | **PASS** | Stale evidence includes `({N} days old ...)` |
| C-19 | Tier 3 | 5 | **PASS** | Pre-display invariant: one row per planned signal |
| C-20 | Tier 4 | 5 | **PASS** | PHASE 4 -- DISPLAY GATE declares invariant |
| C-21 | Tier 4 | 5 | **PASS** | 4 named execution phases: SIGNAL ACQUISITION, PER-SIGNAL COMMITMENT ASSERTION, EXPOSURE COMPUTATION, DISPLAY GATE |
| C-22 | Tier 4 | 5 | **PASS** | `strategy.md: [FOUND \| NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]` — inline consequence present |
| C-23 | Tier 5 | 5 | **PASS** | Phase name is `PER-SIGNAL COMMITMENT ASSERTION` — granularity term `PER-SIGNAL` is integral to the name, not parenthetical. Both evaluation-granularity and decision-stake terms present as contiguous tokens |
| C-24 | Tier 5 | 5 | **PASS** | `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` — layer label carries phase name |
| C-25 | Tier 5 | 5 | **PASS** | `if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute` — consequence annotation inline at field level |
| C-26 | Tier 6 | 5 | **PASS** | In `PER-SIGNAL COMMITMENT ASSERTION`, `PER-SIGNAL` is the leftmost token. Scope quantifier precedes stake noun phrase in name-scanning order. C-23 is satisfied and prefix is at left-edge |
| C-27 | Tier 6 | 5 | **PASS** | LAYER 2 label is `PER-SIGNAL COMMITMENT ASSERTION gate` — full C-23 compressed form including granularity prefix propagated into layer label. C-23 ∧ C-24 both satisfied; label carries complete form, not truncated stake phrase |
| C-28 | Tier 6 | 5 | **PASS** | `if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute` names PHASE 2 by its exact C-21 title. Phase-attributed annotation: consequence is not epistemic (`unquantifiable`) but execution-phase-specific (`cannot execute`). Additionally, stale evidence carries `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` — extending phase-attribution beyond strategy.md field into a second annotation site |

**V-02 Subtotals:**

| Tier | Max | Earned |
|------|-----|--------|
| Essential C-01–04 | 60 | 60 |
| Recommended C-05–07 | 30 | 30 |
| Aspirational C-08–12 | 25 | 25 |
| Tier 2 C-13–16 | 20 | 20 |
| Tier 3 C-17–19 | 15 | 15 |
| Tier 4 C-20–22 | 15 | 15 |
| Tier 5 C-23–25 | 15 | 15 |
| Tier 6 C-26–28 | 15 | 15 |
| **Total** | **195** | **195** |

---

## Composite Ranking

| Rank | Variation | Score | Essential Pass | C-23 | C-26 | C-27 | C-28 |
|------|-----------|-------|----------------|------|------|------|------|
| 1 | V-02 | 195/195 | Yes | PASS | PASS | PASS | PASS |
| 2 | V-01 | 180/195 | Yes | FAIL | FAIL | FAIL | PASS |
| — | V-03–V-05 | — | — | — | — | — | — |

---

## Excellence Signals — V-02

Three patterns make V-02 distinct:

**1. Single structural commitment yields three criterion passes**
Renaming PHASE 2 to `PER-SIGNAL COMMITMENT ASSERTION` (integral, no parenthetical) is one decision that cascades into C-23 (both terms), C-26 (leftmost token), and C-27 (full form propagates into LAYER 2 label) simultaneously. No additional annotations or structural additions required — the phase rename alone collapses three criteria.

**2. Phase-name vocabulary coherence across three sites**
The string `PER-SIGNAL COMMITMENT ASSERTION` appears identically in: the phase title (C-21/C-23), the LAYER 2 label (C-24/C-27), and the strategy.md field annotation (C-25/C-28). Zero vocabulary divergence across declaration, enforcement, and consequence — C-27 and C-28 are satisfied without additional effort because the name is already consistent.

**3. C-28 attribution extended to a second field**
V-02 applies phase-attribution not only to the strategy.md field but also to the stale evidence annotation: `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence`. This extends C-28's pattern beyond the primary field — the phase name appears in every consequence annotation site, not just the one required for criterion satisfaction. This is the natural R7 excellence signal: multi-site C-28 attribution.

---

```json
{"top_score": 195, "all_essential_pass": true, "new_patterns": ["single-rename cascades C-23+C-26+C-27 simultaneously — phase renaming is sufficient; no annotation additions needed", "zero-divergence phase name across title/label/annotation sites satisfies C-27 and C-28 as structural byproduct of consistency", "C-28 attribution extends to stale evidence annotation as second site — phase name appears in every consequence field, not only strategy.md"]}
```
