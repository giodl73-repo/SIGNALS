# Quest Score — campaign-brief / Round 3

**Rubric:** v3 (15 criteria, 150 pts max)
**Variations:** V-01 through V-05
**Date:** 2026-03-16

---

## Criteria Reference

| ID | Tier | Description |
|----|------|-------------|
| C-01 | Essential | Sub-skills invoked in order (structural gates) |
| C-02 | Essential | Existing signals enumerated by namespace |
| C-03 | Essential | Missing signals explicitly named |
| C-04 | Essential | Narrative arc synthesizes signals together |
| C-05 | Essential | Topic registered with name, date, intent |
| C-06 | Recommended | Explicit readiness verdict (named block) |
| C-07 | Recommended | Gap prioritization with inertia framing (item-level) |
| C-08 | Recommended | Visual hierarchy with structural blocks |
| C-09 | Aspirational | DELTA block (session-over-session tracking) |
| C-10 | Aspirational | Confidence dimension table (derived, auditable) |
| C-11 | Aspirational | Per-gap dual commit-risk fields (Assumption + Consequence) |
| C-12 | Aspirational | Prose confined to STORY block (structural enforcement) |
| C-13 | Aspirational | Coverage percentage |
| C-14 | Aspirational | Confidence block isolation (standalone CONFIDENCE between STATUS and STORY) |
| C-15 | Aspirational | STATUS density ceiling (stated mechanism, not convention) |

*Scoring: PASS=10 pts, PARTIAL=5 pts, FAIL=0 pts*

---

## V-01 — Confidence block isolation

**Hypothesis tested:** Standalone CONFIDENCE block between STATUS and STORY resolves the STORY/confidence-table structural conflict from R2. C-15 deliberately absent to isolate the axis.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Seven named phases with deterministic block order stated explicitly |
| C-02 | PASS | STATUS `found:` section lists `<ns>/<artifact> <date>` per line — enumerable by namespace |
| C-03 | PASS | BLOCKING and OPTIONAL sections required; empty BLOCKING must be stated explicitly |
| C-04 | PARTIAL | STORY execution instructs cross-signal reasoning ("interpret what the signals mean together — not what each individual signal contains") but no structural constraints (no prohibitions, no question sequence) — synthesis likely but not guaranteed |
| C-05 | PASS | TOPIC block performs registration (Glob + confirm/create); all three fields present |
| C-06 | PASS | VERDICT block with named `status: READY \| NOT READY \| CONDITIONAL` |
| C-07 | PASS | `Inertia risk:` field required per blocking gap — rubric-named PASS example |
| C-08 | PASS | Seven named discrete blocks; prose/structured data visually separated |
| C-09 | PASS | Full DELTA block: prior_brief, prior_date, prior_verdict, signals_added, gaps_closed, verdict_shift |
| C-10 | PASS | Standalone CONFIDENCE block with 3-dimension table; `Do not assert the level from intuition; derive it from the average` |
| C-11 | PARTIAL | Single `Inertia risk:` field per gap — no dual Assumption+Consequence format; commit-risk is named but one-dimensional |
| C-12 | PASS | `Prose is confined to the STORY block. All other blocks are structured data.` — prompt-level structural enforcement |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone [CONFIDENCE] block explicitly between STATUS and STORY; execution: "Do not embed this block inside STORY" |
| C-15 | FAIL | No density ceiling — deliberately omitted to isolate C-14 axis |

**Tier totals:** Essential 45/50 · Recommended 30/30 · Aspirational 55/70
**V-01 Total: 130/150**

---

## V-02 — STATUS density ceiling

**Hypothesis tested:** Explicit two-tier density contract (≤4 FULL format, >4 COMPRESSED + BLOCKING-DETAIL) satisfies C-15 via stated structural mechanism. DELTA and C-14 absent to isolate axis.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Phases listed in structural order with deterministic block sequence |
| C-02 | PASS | STATUS `found:` section lists `<ns>/<artifact>` per line |
| C-03 | PASS | BLOCKING and OPTIONAL sections; `State explicitly when the section is empty` |
| C-04 | PARTIAL | STORY has prose instructions but no prohibitions or question structure — synthesis likely but not guaranteed |
| C-05 | PASS | TOPIC block with registration execution |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | FULL FORMAT: `Assumption: ... Consequence: ...` per gap; item-level consequence grounding is explicit |
| C-08 | PASS | Named blocks throughout with clear structural separation |
| C-09 | FAIL | No DELTA block — deliberately omitted |
| C-10 | PASS | Confidence dimension table present and derived; embedded in STORY as `confidence_dimensions:` section |
| C-11 | PASS | FULL FORMAT provides both `Assumption:` and `Consequence:` fields; COMPRESSED entries carry full fields in BLOCKING-DETAIL |
| C-12 | PARTIAL | STORY contains both narrative prose and the confidence_dimensions table — not pure prose; the table inside STORY violates the spirit of prose confinement |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | FAIL | Confidence table embedded inside STORY, not a standalone block — the structural conflict V-01 was designed to resolve remains present |
| C-15 | PASS | Explicit two-tier density contract stated as a structural rule: `If blocking gaps <= 4: use FULL format. If blocking gaps > 4: use COMPRESSED format + [BLOCKING-DETAIL]` — mechanism is stated, not discovered |

**Tier totals:** Essential 45/50 · Recommended 30/30 · Aspirational 45/70
**V-02 Total: 120/150**

---

## V-03 — STORY purity enforcement

**Hypothesis tested:** Explicit negative constraints on STORY (no bullets, no artifact filenames, no confidence restatement, three-question sequential structure) lift C-04 from PARTIAL to PASS without other axis changes. Standalone CONFIDENCE is a side effect.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Six named phases in deterministic order |
| C-02 | PASS | STATUS `found:` section enumerates `<ns>/<artifact>` per line |
| C-03 | PASS | BLOCKING required with `Inertia risk:` per gap; empty case explicitly stated |
| C-04 | PASS | PERMITTED/NOT PERMITTED constraint list prohibits bullets, artifact filenames, tables, confidence level restatement, per-gap enumeration; three-question structure mandates: (1) what case do signals make together, (2) what do gaps leave uncertain, (3) what is team's real exposure — structural, not advisory |
| C-05 | PASS | TOPIC block with registration execution |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Inertia risk:` required per blocking gap |
| C-08 | PASS | Named blocks: TOPIC, STRATEGY, STATUS, CONFIDENCE, STORY, VERDICT |
| C-09 | FAIL | No DELTA block — deliberately omitted |
| C-10 | PASS | Standalone CONFIDENCE block with 3-dimension derived table; "This block is the confidence record — STORY will not restate the level" |
| C-11 | PARTIAL | Single `Inertia risk:` field per blocking gap — no dual Assumption+Consequence |
| C-12 | PASS | "All blocks except STORY contain structured data only. STORY contains prose only — no tables, no bullet lists." — explicit structural enforcement at both directions |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | CONFIDENCE is standalone between STATUS and STORY (structural side effect of STORY purity constraint — table cannot live in STORY if STORY is prose-only) |
| C-15 | FAIL | No density ceiling — deliberately omitted |

**Tier totals:** Essential 50/50 · Recommended 30/30 · Aspirational 45/70
**V-03 Total: 125/150**

*Note: V-03 is the only variation achieving all Essential criteria at PASS. The PERMITTED/NOT PERMITTED + three-question structure is the confirmed mechanism for C-04 PASS.*

---

## V-04 — C-14 + C-15 combined (no DELTA)

**Hypothesis tested:** C-14 and C-15 are additive — combining both on a clean base without DELTA should score V-01 + 10 (C-15 adds) and V-05 - 10 (C-09 absent).

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Named phases in deterministic order |
| C-02 | PASS | STATUS enumerates signals by namespace |
| C-03 | PASS | BLOCKING with required Inertia risk; empty case stated |
| C-04 | PARTIAL | STORY rules prohibit bullets, artifact filenames, confidence restatement, per-gap enumeration; requires inertia-as-pattern framing — better than V-01/V-02 but lacks V-03's three-question sequential structure; synthesis likely, not guaranteed |
| C-05 | PASS | TOPIC block with registration |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Inertia risk:` required per blocking gap in FULL FORMAT |
| C-08 | PASS | Named blocks with clear structural separation |
| C-09 | FAIL | No DELTA — deliberately omitted to isolate C-14+C-15 additivity |
| C-10 | PASS | Standalone CONFIDENCE block with derived 3-dimension table; "CONFIDENCE is a standalone block — do not embed inside STORY" |
| C-11 | PARTIAL | FULL FORMAT uses single `Inertia risk:` field — no dual Assumption+Consequence |
| C-12 | PASS | "Prose is confined to the STORY block. All other blocks are structured data." |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE block; explicit execution instruction against embedding in STORY |
| C-15 | PASS | Density contract stated structurally: `Count blocking missing signals before formatting. Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL] if blocking gaps > 4` |

**Tier totals:** Essential 45/50 · Recommended 30/30 · Aspirational 55/70
**V-04 Total: 130/150**

*Additivity confirmed: V-04 (130) = V-01 (130) with C-15 replacing C-09 — the two mechanisms swap the same 10 points. No interaction effect detected.*

---

## V-05 — Full 15-criterion sweep

**Hypothesis tested:** R2 V-05 extended with C-14 (standalone CONFIDENCE) + C-15 (density ceiling). Ceiling test: 7+ blocks without cognitive overload, all 15 criteria targeted simultaneously.

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Full named phase sequence; structural block ordering is deterministic |
| C-02 | PASS | STATUS `found:` enumerates `<ns>/<artifact> <date>` per line |
| C-03 | PASS | BLOCKING with `Inertia risk:` per gap; empty case explicitly required |
| C-04 | PARTIAL | STORY constraints prohibit bullets, artifact names, confidence restatement, per-gap enumeration; "Do address inertia risk as a pattern" — enforces one synthesis dimension but lacks three-question sequential structure; PARTIAL not PASS |
| C-05 | PASS | TOPIC block performs registration |
| C-06 | PASS | VERDICT block with named `status:` |
| C-07 | PASS | `Inertia risk:` required per blocking gap |
| C-08 | PASS | Eight named blocks (plus optional BLOCKING-DETAIL) — clear structural separation throughout |
| C-09 | PASS | Full DELTA block with prior_brief, prior_date, prior_verdict, signals_added, gaps_closed, verdict_shift |
| C-10 | PASS | Standalone CONFIDENCE block; "Derive average arithmetically — do not estimate. CONFIDENCE is a standalone block; do not embed inside STORY" |
| C-11 | PARTIAL | Single `Inertia risk:` field per blocking gap in FULL FORMAT — V-02's dual Assumption+Consequence not carried forward; C-11 gap persists |
| C-12 | PASS | "Prose is confined to the STORY block. All other blocks are structured data." |
| C-13 | PASS | `coverage: X/(X+Y) = Z%` in STATUS |
| C-14 | PASS | Standalone CONFIDENCE block between STATUS and STORY; `do not embed inside STORY` explicit in execution |
| C-15 | PASS | Full density contract: `Count blocking missing signals before formatting. Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL] if blocking gaps > 4` |

**Tier totals:** Essential 45/50 · Recommended 30/30 · Aspirational 65/70
**V-05 Total: 140/150**

*Prompt complexity failure: not observed. 7-block base + optional BLOCKING-DETAIL remains coherent. Progressive decomposition model validated at maximum scale.*

---

## Score Summary

| Var | Essential /50 | Recommended /30 | Aspirational /70 | Total /150 | Rank |
|-----|--------------|-----------------|-----------------|-----------|------|
| V-05 | 45 | 30 | 65 | **140** | 1 |
| V-01 | 45 | 30 | 55 | 130 | 2 |
| V-04 | 45 | 30 | 55 | 130 | 2 |
| V-03 | **50** | 30 | 45 | 125 | 4 |
| V-02 | 45 | 30 | 45 | 120 | 5 |

---

## Excellence Signals from V-05

**What made V-05 the top scorer:**

1. **DELTA + CONFIDENCE isolation + density ceiling are independently additive.** The three structural mechanisms that interact conceptually (DELTA tracks gap counts across runs; gap counts trigger the density ceiling; confidence block isolation separates calibration from the narrative) coexist without structural conflict. They operate on different phases and different blocks — no cross-mechanism interference observed.

2. **Eight-block maximum pipeline validates progressive decomposition at ceiling.** TOPIC → DELTA → STRATEGY → STATUS → [BLOCKING-DETAIL] → CONFIDENCE → STORY → VERDICT is coherent at full scale. One concept per block is the design principle that makes this work — the prompt grows in block count, not in per-block complexity.

**Remaining gap to 150 (R4 targets):**

- **C-04 (+5):** V-03's PERMITTED/NOT PERMITTED + three-question sequential structure is the confirmed mechanism. Port it into V-05's STORY block. No other axis change required.
- **C-11 (+5):** V-02's dual `Assumption: / Consequence:` format is the confirmed mechanism for PASS. The FULL FORMAT in V-05 currently uses single `Inertia risk:`. Merge V-02's dual-field format into V-05's FULL FORMAT (leaving COMPRESSED at ≤12-word single line).

---

## R4 Design Guidance

V-05 is the base for R4. Two surgical changes close the remaining 10-point gap:

1. Replace STORY execution instruction with V-03's full PERMITTED/NOT PERMITTED + three-question structure
2. Upgrade FULL FORMAT blocking entries from single `Inertia risk:` to dual `Assumption: / Consequence:` (leave COMPRESSED unchanged — the 12-word ceiling already handles scale)

Expected R4 V-01 score: 150/150. No new axes needed — this is a refinement round, not an expansion round.

---

```json
{"top_score": 140, "all_essential_pass": false, "new_patterns": ["DELTA + standalone CONFIDENCE block + STATUS density ceiling are independently additive — three mechanisms that interact conceptually operate on distinct phases and blocks with no structural conflict", "eight-block maximum pipeline (TOPIC, DELTA, STRATEGY, STATUS, BLOCKING-DETAIL, CONFIDENCE, STORY, VERDICT) validates progressive decomposition at ceiling without prompt complexity failure"]}
```
