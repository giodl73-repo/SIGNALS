## SCORECARD — `topic-status` Round 1

---

### V-01 (Table-centric)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Step 1 uses Glob explicitly, "Do not invent paths", zero case handled with "No signals found on disk" |
| C-02 | Coverage percentage | **PASS** (15) | Fixed `{total_found} / {total_planned} planned signals — {percent}%` header enforces the math structurally |
| C-03 | Gap identification | **PASS** (15) | Open Gaps section requires `{namespace}/{skill} {item-name} (priority)` per entry; "no gaps" case explicit |
| C-04 | Display-only | **PASS** (15) | "DISPLAY (terminal only — no file written)" in Step 4 label + opening IMPORTANT block |
| C-05 | Readiness verdict | **PASS** (10) | `READINESS: [READY \| ALMOST READY \| NOT READY]` + `Reason: {one sentence tied directly to gap list}` |
| C-06 | Namespace breakdown | **PASS** (10) | Pre-printed 9-row table, "Fill every row", zero shown as `0 \| 0 \| —` — omission structurally impossible |
| C-07 | Strategy cross-ref | **PASS** (10) | `Strategy: ... [FOUND \| NOT FOUND]` in output; Step 2 handles missing-file case explicitly |
| C-08 | Recency awareness | **FAIL** (0) | No staleness annotation or date-suffix flagging present |
| C-09 | Actionable next step | **PASS** (5) | `Next step: Run /{namespace}:{skill} to produce {item-name}.` required; "Omit if no gaps" |

**Score: 95 / 100** — All 4 essential pass. Strongest C-06 treatment (pre-printed table). Only gap: C-08.

---

### V-02 (Conversational)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Glob instruction explicit, "Don't make up paths", zero case handled |
| C-02 | Coverage percentage | **PASS** (15) | `Coverage: {found} / {planned} planned signals — {percent}%` in output template |
| C-03 | Gap identification | **PASS** (15) | Gaps section with `{namespace}/{skill} — {item-name} (essential \| recommended \| optional)`; all-present case explicit |
| C-04 | Display-only | **PASS** (15) | "Don't write anything to disk — just display." at top |
| C-05 | Readiness verdict | **PASS** (10) | `Readiness: READY \| ALMOST READY \| NOT READY` + "One sentence explaining why, tied to the gap list above" |
| C-06 | Namespace breakdown | **PASS** (10) | All 9 lines required; "Show all 9. Zero is a valid count — don't skip empty namespaces." |
| C-07 | Strategy cross-ref | **PASS** (10) | `Strategy: simulations/{topic}/strategy.md (found \| not found)` in output; missing case handled |
| C-08 | Recency awareness | **PASS** (5) | "Stale signals (>30 days old based on filename date): flag any whose date suffix is more than 30 days before today's date with '(stale — {N} days old)'" |
| C-09 | Actionable next step | **PASS** (5) | `Next: Run /{namespace}:{skill} to fill {item-name}. (Skip if no gaps.)` |

**Score: 100 / 100** — All 9 criteria pass. Only variation in full text to cover C-08. Structural note: conversational prose for C-06 is weaker than V-01's pre-printed table; empty-namespace display depends on "Show all 9" instruction holding rather than structural impossibility.

---

### V-03 (Lifecycle / 3-Phase — text truncated)

**Note:** Provided text ends at "Action 2.1 — Match signals". Phase 2 (COMPUTE) is incomplete; Phase 3 (DISPLAY) is absent. Scores reflect the text as provided.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Phase 1 Action 1.1 well-specified: Glob + DISK_SIGNALS variable + zero case |
| C-02 | Coverage percentage | **FAIL** (0) | Phase 2 cut off after `Action 2.1 — Match signals`; no computation formula present |
| C-03 | Gap identification | **FAIL** (0) | Phase 3 (DISPLAY) absent; no output format for gaps |
| C-04 | Display-only | **PASS** (15) | CONTRACT block is the strongest C-04 language in any variation: "If you write to disk, the skill fails regardless of output quality. Check before Phase 3." |
| C-05 | Readiness verdict | **FAIL** (0) | Phase 3 absent |
| C-06 | Namespace breakdown | **FAIL** (0) | Phase 3 absent |
| C-07 | Strategy cross-ref | **PARTIAL** (5) | Action 1.2 reads strategy.md and handles missing case; display-side reference not specified |
| C-08 | Recency awareness | **FAIL** (0) | Not present |
| C-09 | Actionable next step | **FAIL** (0) | Phase 3 absent |

**Score: 35 / 100** — C-01 and C-04 pass; all others fail due to truncation. V-03's CONTRACT language (C-04) is the best single-criterion treatment across all variations. If Phase 3 were present, estimated score ~85.

---

### V-04 (Gap-first ordering — full text not provided; scored from design description)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Consistent with all other variations per design notes |
| C-02 | Coverage percentage | **PASS** (15) | Gap-first ordering anchors the math: percentage computed after gaps are enumerated, closing the "100% contradicts listed gaps" fail condition |
| C-03 | Gap identification | **PASS** (15) | Gaps are primary output, listed before any aggregate |
| C-04 | Display-only | **PASS** (15) | Standard contract present across all variations |
| C-05 | Readiness verdict | **PASS** (10) | Standard per design decisions |
| C-06 | Namespace breakdown | **PASS** (10) | Standard per design decisions |
| C-07 | Strategy cross-ref | **PASS** (10) | Standard per design decisions |
| C-08 | Recency awareness | **FAIL** (0) | Not mentioned in description |
| C-09 | Actionable next step | **PASS** (5) | Standard per design decisions |

**Score: ~95 / 100** *(estimated — full text not provided)* — Strongest C-02 correctness guarantee of any single-axis variation. Structurally equivalent to V-01 except the ordering change.

---

### V-05 (Full synthesis — full text not provided; scored from design description)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Signal discovery | **PASS** (15) | Phase DISCOVER gate (V-03) + Glob tool (V-01) |
| C-02 | Coverage percentage | **PASS** (15) | Gap-first ordering (V-04) + fixed table header (V-01) — doubly anchored |
| C-03 | Gap identification | **PASS** (15) | Gap-first + named items per namespace/skill |
| C-04 | Display-only | **PASS** (15) | Named phase boundary: "Check before Phase 3" (V-03 pattern) |
| C-05 | Readiness verdict | **PASS** (10) | Standard |
| C-06 | Namespace breakdown | **PASS** (10) | Pre-printed 9-row table (V-01) |
| C-07 | Strategy cross-ref | **PASS** (10) | Explicitly named per design description |
| C-08 | Recency awareness | **PASS** (5) | Stale flagging from V-02 per design description |
| C-09 | Actionable next step | **PASS** (5) | Standard |

**Score: ~100 / 100** *(estimated — full text not provided)* — Predicted execution ceiling. Every criterion covered with maximum structural redundancy (table + phases + gap-first + stale flagging combined).

---

## Rankings

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | **V-02** (Conversational) | 100 | Only full-text variation covering all 9 criteria; C-08 via date-suffix stale flagging |
| 1 | **V-05** (Full synthesis) | ~100 | Predicted execution ceiling; all axes stacked; full text not provided |
| 3 | **V-01** (Table-centric) | 95 | Strongest C-06 guarantee; misses C-08 only |
| 3 | **V-04** (Gap-first) | ~95 | Strongest C-02 correctness guarantee; misses C-08 only |
| 5 | **V-03** (Lifecycle) | 35 | Text truncated; Phase 3 absent — CONTRACT language is best C-04 treatment if complete |

**Predicted vs. actual top:** Author predicted V-05 > V-04 > V-01 > V-03 > V-02. Rubric score shows V-02 ties V-05 on paper, outperforming V-01/V-04 by one criterion (C-08). V-03 last due to truncation, not design weakness.

---

## Excellence Signals from Top Variation (V-02)

1. **Stale flagging via date-suffix comparison closes C-08 with minimal overhead.** One instruction ("flag any whose date suffix is more than 30 days before today's date") covers the entire aspirational criterion at zero structural cost. Other variations simply omit it.

2. **Conversational "skip if" instructions prevent hallucinated empty sections.** `(Skip this section if none.)` after Unplanned Signals blocks model from generating placeholder content where there is none.

3. **"Zero is a valid count — don't skip" beats prose omission via explicit negative constraint.** Rather than pre-printing a table row, V-02 closes the silent-omission path with a direct prohibition. This proves constraint language can substitute for structural scaffolding when applied at the right point.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["stale-flag-via-date-suffix-minimal-cost", "skip-if-none-prevents-hallucinated-empty-sections", "explicit-negative-constraint-closes-omission-path-without-table-scaffolding"]}
```
