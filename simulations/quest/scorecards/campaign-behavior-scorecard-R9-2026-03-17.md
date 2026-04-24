I have all five variation texts. Now I'll score each against v7 systematically.

---

# Quest Scorecard — campaign-behavior (Round 9)
**Skill:** campaign-behavior (org-review)
**Rubric:** v7 (C-01–C-26, denominator 18)
**Date:** 2026-03-17

---

## Scoring Key

| Tier | Formula | Max |
|------|---------|-----|
| Essential | C-01–C-05 × 10 | 50 |
| Recommended | C-06–C-08 × 10 | 30 |
| Aspirational | (passed/18) × 10 | 10 |
| **Total** | | **90** |

---

## V-01 — Chain Terminus Registry

**Axis:** Phase 0 T-NN numbered table; every propagation chain must resolve to a T-NN entry or be flagged "unresolved chain." DEFINITIONS chain format uses `[origin] -> ... -> [T-NN terminal]`. Q1 traces to T-NN terminal.

### Essential

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 — All 5 sub-skills | PASS | Ph1 trace-state, Ph2 trace-permissions, Ph3 trace-contract, Ph4 flow-lifecycle, Ph5 flow-trigger all present with tables and exit criteria |
| C-02 — Ranked by blast radius | PASS | "Ranked findings (calibrated blast radius order, wide first)" in CONSOLIDATE |
| C-03 — Spec gaps | PASS | "Spec gaps: [list each gap with missing-clause citation, or 'none detected']" labeled section |
| C-04 — Contract violations | PASS | "Contract violations: [list each with producer and consumer named, or 'none detected']" labeled section |
| C-05 — Lifecycle violations | PASS | flow-lifecycle table has "Exception path" + "Exception handled?" columns; EXIT CRITERIA requires all phases evaluated |

**Essential: 50/50**

### Recommended

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-06 — Blast radius label | PASS | Field 3: "Blast radius: [wide \| medium \| narrow] -- propagation chain: ..." in every atomic block |
| C-07 — Confirmation status | PASS | Field 6: "Classification: [CONFIRMED \| RUNTIME ANOMALY \| isolated]" in every block |
| C-08 — Sub-skill attribution | PASS | Field 2: "Source phase: [phase name]" in every block |

**Recommended: 30/30**

### Aspirational

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-09 | F-NN sequential IDs | PASS | "Finding [N]" in CONSOLIDATE, numbered blast-radius order |
| C-10 | Lifecycle phase tag | PASS | "Phase tag" column in both Ph4 and Ph5 tables; named tier values (INIT, ACTIVE, SUSPENDED, TERMINAL) |
| C-11 | Compound findings | PASS | Ph2 EXIT CRITERIA: "[N] compound anchor hits"; phrase "compound anchor hit" in Ph2 Phase 1 state surface + escalation path intersection |
| C-12 | Spec gap citation | PASS | "list each gap with missing-clause citation" structurally required in CONSOLIDATE section |
| C-13 | Producer/consumer | PASS | "list each with producer and consumer named" structurally required |
| C-14 | Privilege escalation paths | PASS | Ph2 has "Escalation path?" column; CONSOLIDATE "Privilege escalation paths" section |
| C-15 | Severity defined scale | PASS | DEFINITIONS: "Severity = damage depth at the epicenter (high / med / low)"; field 4 per block |
| C-16 | Executive summary top-3 | PASS | No dedicated heading, but ranked findings list (wide first) makes top-3 identifiable by position; blast radius (field 3) and confirmation (field 6) present on each |
| C-17 | Evidence per CONFIRMED | PASS | DEFINITIONS: "Name the matching Phase 1-3 finding when classifying CONFIRMED"; same instruction as R8 V-05 baseline which passed |
| C-18 | Q1–Q6 calibration | PASS | Six calibration questions (Q1–Q6) all present with named targets |
| C-19 | Atomic 7-field block | PASS | Exactly 7 numbered and labeled fields in CONSOLIDATE block |
| C-20 | Tiebreaker stated | PASS | DEFINITIONS + CONSOLIDATE both state protocol; "State whether any ties were encountered" |
| C-21 | SYSTEMIC phase list | PASS | DEFINITIONS: "Required format: 'SYSTEMIC: yes -- phases: [...]'" binary flag rejected; Q3 enforces |
| C-22 | State-anchor first | PASS | Ph1: "trace-state runs first"; explicit rationale linking first-position to blast radius pre-classification |
| C-23 | Permissions-anchor before flow | PASS | Ph2: "trace-permissions runs second, before all flow sub-skills" with explicit rationale |
| C-24 | Anchor tags on headers | PASS | Ph1: `[ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]`; Ph2: `[ANCHOR: privilege boundary classification anchors flow blast radius assessment]` |
| C-25 | Q6 sequence integrity gate | PASS | Q6: "Did the execution sequence deliver its pre-classification guarantee?" — post-execution self-check with anchor violation logging format |
| C-26 | Propagation chain in field 3 | PASS | DEFINITIONS chain format ✓; field 3 chain with T-NN terminal ✓; Q1 traces to T-NN terminal ✓; VERDICT: "State the propagation chain from origin to T-NN terminal blast surface" ✓ — all four elements present |

**Aspirational: 18/18 → 10/10**

**V-01 Total: 90/90** | All-essential pass: YES

---

## V-02 — Dedicated Executive Summary

**Axis:** `## EXECUTIVE SUMMARY` heading before ranked findings; 3 structured bullets with `[F-NN] [blast-radius tier] -- [origin] -> [terminal] -- [CONFIRMED/RUNTIME ANOMALY]`. No T-NN registry. No inline evidence citation.

### Essential / Recommended

All C-01–C-08 pass for identical structural reasons as V-01 (same phase tables, columns, exit criteria, CONSOLIDATE sections). **50/50 essential, 30/30 recommended.**

### Aspirational Differentials (from V-01 baseline)

| # | Criterion | Result | Evidence vs V-01 |
|---|-----------|--------|-----------------|
| C-16 | Executive summary top-3 | PASS | **Dedicated `## EXECUTIVE SUMMARY` heading** with exactly 3 bullets — unambiguous by section position, no list-order inference required; stronger than V-01's ranked-list pass |
| C-26 | Propagation chain | PASS | DEFINITIONS chain format "[origin] -> [component-B] -> [terminal]" ✓; field 3 chain ✓; Q1: "trace the full propagation chain ([origin] -> ... -> [terminal])" ✓; VERDICT: "State the propagation chain from origin to terminal blast surface" ✓ — no T-NN notation but all four elements present |

All other aspirationals: identical PASS as V-01.

**V-02 Total: 90/90** | All-essential pass: YES

---

## V-03 — Inline CONFIRMED Evidence Citation

**Axis:** Field 6 format changed to `"CONFIRMED -- evidence: [matching phase name]: [matching finding description]"` structurally enforced in DEFINITIONS, field template, and VERDICT. Q2 explicitly verifies inline citation presence. No T-NN registry. No EXECUTIVE SUMMARY section.

### Essential / Recommended

All C-01–C-08 pass.

**C-07 note:** Field 6 now contains richer format including evidence citation. C-07 pass condition is "named confirmation status in a labeled field." `CONFIRMED -- evidence: [...]` contains the named status CONFIRMED. → PASS

**50/50 essential, 30/30 recommended.**

### Aspirational Differentials

| # | Criterion | Result | Evidence vs V-01 |
|---|-----------|--------|-----------------|
| C-16 | Executive summary top-3 | PASS | No dedicated heading; top-3 identifiable by ranked list position + field 3 blast radius + field 6 CONFIRMED classification — same as V-01 pass |
| C-17 | Evidence per CONFIRMED | PASS | **Structurally enforced** — field 6 template embeds citation format; DEFINITIONS: "This citation is required. CONFIRMED without an inline evidence citation = incomplete block"; Q2 verifies. Stronger compliance surface than DEFINITIONS-instruction-only |
| C-19 | 7-field atomic block | PASS | Still exactly 7 numbered/labeled fields; field 6 content is richer but field count unchanged |

All other aspirationals: identical PASS.

**V-03 Total: 90/90** | All-essential pass: YES

---

## V-04 — Chain Terminus Registry + Dedicated Executive Summary

**Axis:** V-01 + V-02 combination. T-NN registry in Phase 0; EXECUTIVE SUMMARY before ranked findings with T-NN in bullet chains ("-- [origin] -> [T-NN terminal] -- [CONFIRMED/RUNTIME ANOMALY]"). No inline evidence citation.

### Essential / Recommended

All C-01–C-08 pass. **50/50 essential, 30/30 recommended.**

### Aspirational Differentials

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-16 | Executive summary top-3 | PASS | Dedicated `## EXECUTIVE SUMMARY` section with T-NN chain in each bullet — no inference required |
| C-17 | Evidence per CONFIRMED | PASS | DEFINITIONS-instructed, same as V-01 (not structurally enforced in field 6) |
| C-26 | Propagation chain | PASS | DEFINITIONS T-NN format ✓; field 3 T-NN chain ✓; Q1 T-NN trace ✓; VERDICT T-NN chain ✓ — all four |

**Interference check:** T-NN notation in EXECUTIVE SUMMARY bullets ("-- [origin] -> [T-NN terminal] --") is consistent with field 3 chain format and DEFINITIONS. No interference detected — T-NN appears coherently in both input vocabulary layer (Phase 0 registry) and output communication layer (EXECUTIVE SUMMARY). C-16 pass is strengthened, not disrupted.

**V-04 Total: 90/90** | All-essential pass: YES

---

## V-05 — Full Combination (All Three Axes + R8 V-05 Max Coverage)

**Axis:** T-NN registry + EXECUTIVE SUMMARY + inline field 6 evidence citation, all composing together. EXECUTIVE SUMMARY bullets include inline evidence: `[F-NN] [tier] -- [origin] -> [T-NN terminal] -- [CONFIRMED -- evidence: [phase]: [match] | RUNTIME ANOMALY]`. Q2 verifies inline citation in field 6. VERDICT: "State CONFIRMED (with evidence: [phase]: [matching finding]) or RUNTIME ANOMALY."

### Essential / Recommended

All C-01–C-08 pass. **50/50 essential, 30/30 recommended.**

### Aspirational Differentials

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-16 | Executive summary top-3 | PASS | Dedicated EXECUTIVE SUMMARY + T-NN chains + inline evidence citation per bullet — most information-dense version across all rounds |
| C-17 | Evidence per CONFIRMED | PASS | **Three independent enforcement surfaces**: DEFINITIONS require inline citation; field 6 template encodes it; EXECUTIVE SUMMARY bullets encode it; VERDICT encodes it; Q2 audits it |
| C-19 | 7-field block | PASS | 7 fields; field 6 content enriched but count unchanged |
| C-26 | Propagation chain | PASS | DEFINITIONS T-NN format ✓; field 3 T-NN chain ✓; Q1 T-NN trace ✓; VERDICT T-NN chain + evidence ✓ |

**Interference checks:**
- T-NN in field 3 vs C-26: **No interference** — T-NN is the terminus notation, C-26 requires named hops in chain. T-NN adds structure without removing hops.
- EXECUTIVE SUMMARY with T-NN vs C-16: **No interference** — T-NN in bullets makes the chain more auditable, not less. C-16 pass strengthened.
- Inline field 6 vs C-07/C-19: **No interference** — C-07 requires named confirmation status; "CONFIRMED -- evidence: ..." names CONFIRMED. C-19 requires 7 fields; count unchanged.

All 18 aspirationals pass.

**V-05 Total: 90/90** | All-essential pass: YES

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Total | Notes |
|-----------|-----------|-------------|--------------|-------|-------|
| V-01 | 50 | 30 | 10 | **90** | Chain Terminus Registry; all C-24/25/26 present |
| V-02 | 50 | 30 | 10 | **90** | Dedicated EXECUTIVE SUMMARY removes C-16 inference |
| V-03 | 50 | 30 | 10 | **90** | Inline field 6 citation enforces C-17 structurally |
| V-04 | 50 | 30 | 10 | **90** | V-01+V-02 compose cleanly; no T-NN/EXEC interference |
| V-05 | 50 | 30 | 10 | **90** | Full combination; three evidence surfaces for C-17 |

**All variations: 90/90. All essential criteria pass.**

---

## Excellence Signals from V-05 Differential

V-05 is the maximum redundancy configuration. Three structural patterns emerge that go beyond anything in v7:

**Signal 1 — Chain Terminus Registry converts terminus validation from prose audit to table lookup.**
Phase 0 now declares a numbered T-NN table. Every propagation chain in field 3, EXECUTIVE SUMMARY, and VERDICT must resolve to a T-NN entry. A reviewer validates blast-radius claims by checking the chain terminus against the table — no re-reading of DEFINITIONS prose required. Chains that miss the registry are flagged "unresolved chain — registry miss: [component name]" and excluded from ranking. This is a structural audit gate that DEFINITIONS alone cannot enforce.

**Signal 2 — Dedicated `## EXECUTIVE SUMMARY` before ranked findings makes top-3 identification position-independent.**
V-02/V-04/V-05 demonstrate that a dedicated heading with exactly 3 structured bullets (F-NN + blast-radius + abbreviated chain + confirmation) removes the inferential step in C-16. In V-01/V-03 (no EXECUTIVE SUMMARY), a reviewer must read to the top of the ranked list and verify that field 3 and field 6 are populated for the first three entries. The EXECUTIVE SUMMARY compresses that to three scannable lines. V-05 enhances this further by embedding inline evidence in each EXECUTIVE SUMMARY bullet.

**Signal 3 — Field 6 inline evidence citation creates three independent enforcement surfaces for C-17.**
In V-03/V-05, "CONFIRMED" without `evidence: [phase]: [finding]` fails the block format. DEFINITIONS declare this required; the field 6 template encodes it; EXECUTIVE SUMMARY bullets encode it; VERDICT encodes it; Q2 audits it. Any CONFIRMED finding that omits the citation fails at five checkpoints. The enforcement is no longer dependent on the DEFINITIONS instruction being followed voluntarily — it is embedded in the output structure itself.

These three patterns are independent of each other and independent of C-24/C-25/C-26. They are the candidates for C-27 (terminal registry lookup), C-28 (dedicated executive summary heading), and C-29 (inline evidence citation as field-level requirement).

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Chain Terminus Registry in Phase 0 converts terminus validation from DEFINITIONS prose to numbered T-NN table lookup — blast radius claims become mechanically auditable without re-reading definitional text", "Dedicated ## EXECUTIVE SUMMARY heading before ranked findings makes top-3 identification unambiguous by section position rather than list-order inference", "Inline CONFIRMED evidence citation in field 6 template (CONFIRMED -- evidence: [phase]: [finding]) enforces C-17 at the structural level across field, VERDICT, and EXECUTIVE SUMMARY bullets — three independent compliance surfaces"]}
```
