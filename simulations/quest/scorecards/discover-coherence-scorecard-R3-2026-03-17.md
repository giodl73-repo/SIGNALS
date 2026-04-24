Scorecard written to `simulations/quest/scorecards/discover-coherence-scorecard-R3-2026-03-17.md`.

---

## Results

**All 5 variations golden** (100–130/130, all essential pass).

| Rank | Variation | Score | Gap from 130 |
|------|-----------|-------|--------------|
| 1 | V-05 Full stack | **130** | 0 |
| 2 | V-03 Conversational | **115** | -15 (C-09, C-13, C-14) |
| 2 | V-04 Two-phase + token | **115** | -15 (C-09, C-13, C-14) |
| 4 | V-01 Silent-scan | **105** | -25 (adds C-10, C-16) |
| 5 | V-02 Token-enforced | **100** | -30 (adds C-06, C-15) |

**One prediction miss**: V-02 came in at 100, not ~110. The prediction assumed C-06 would pass; it fails because the CLOSING tally is structurally after entries. Without C-15 (two-phase), C-06 cannot be satisfied. This is the cleanest experimental confirmation of C-15's design rationale the series has produced.

**Register parity confirmed**: V-03 (conversational WHY-explanations) ties V-04 (explicit phase labels) at 115. For C-15 and C-16, the mechanism matters — register doesn't.

**No new patterns**: R3 was a confirmation round. C-15 and C-16 are now criteria; the dual-table apparatus remains the only path to 130.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": []}
```
STEP 4 entries |
| C-07 | Recommended | 10 | PASS | STEP 5 VERDICT with M=0 / M>=1 branches |
| C-08 | Recommended | 10 | PASS | Skill name + date in both claim slots |
| C-09 | Aspirational | 5 | FAIL | No taxonomy labels |
| C-10 | Aspirational | 5 | FAIL | "specific skill to run" but no /skill-name token requirement |
| C-11 | Aspirational | 5 | PASS | "GATE FAILED: {N} signal(s) found, need 2+." |
| C-12 | Aspirational | 5 | PASS | "not 'investigate further'" explicitly in resolution instruction |
| C-13 | Aspirational | 5 | FAIL | No inertia-first table |
| C-14 | Aspirational | 5 | FAIL | Prose entries, no named-column Markdown table |
| C-15 | Aspirational | 5 | PASS | STEP 2 PRE-SCAN: "do not output any contradiction in this step" + separate STEP 3 header |
| C-16 | Aspirational | 5 | FAIL | No severity-split token format rule |

**Score**: 60 + 30 + 15 = **105 / 130** -- GOLDEN

---

### V-02: Token-enforced (C-16 axis)

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED + glob present |
| C-02 | Essential | 12 | PASS | `{skill-A} ({date}): "{what it said, in its own words}"` |
| C-03 | Essential | 12 | PASS | "Severity: blocking | advisory" in template |
| C-04 | Essential | 12 | PASS | "Do not write 'investigate further' -- name the specific change needed" |
| C-05 | Essential | 12 | PASS | CROSS-SKILL RULE section present |
| C-06 | Recommended | 10 | FAIL | Tally in CLOSING (after entries); no tally before first entry |
| C-07 | Recommended | 10 | PASS | CLOSING has verdict tied to blocking count |
| C-08 | Recommended | 10 | PASS | Skill name + date in contradiction template |
| C-09 | Aspirational | 5 | FAIL | No taxonomy labels |
| C-10 | Aspirational | 5 | PASS | BLOCKING: "Resolve with: /{skill-name} [--focus {parameter}]" |
| C-11 | Aspirational | 5 | PASS | "GATE FAILED: {N} signal(s) found, need 2+." |
| C-12 | Aspirational | 5 | PASS | Two wrong-example lines + "Do not write 'investigate further'" |
| C-13 | Aspirational | 5 | FAIL | No inertia-first table |
| C-14 | Aspirational | 5 | FAIL | Prose entries, no named-column table |
| C-15 | Aspirational | 5 | FAIL | Single-pass: COHERENCE CHECK writes entries while scanning |
| C-16 | Aspirational | 5 | PASS | BLOCKING token format with correct/wrong examples; ADVISORY prose rule separate |

**Score**: 60 + 20 + 20 = **100 / 130** -- GOLDEN

**Key finding**: C-06 fails because without two-phase structure (C-15), the tally is placed
in CLOSING -- structurally after entries. Confirms C-15 design rationale: single-pass
cannot guarantee tally-before-first-entry.

---

### V-03: Conversational (phrasing register axis)

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED + glob present |
| C-02 | Essential | 12 | PASS | `"{exact quote or close paraphrase of what this signal said}"` |
| C-03 | Essential | 12 | PASS | "exactly `blocking` or `advisory` -- no other labels" |
| C-04 | Essential | 12 | PASS | "'Investigate further' is not a resolution -- it doesn't tell anyone what to do" |
| C-05 | Essential | 12 | PASS | Cross-skill requirement stated |
| C-06 | Recommended | 10 | PASS | "OPEN WITH THE TALLY" section precedes "ONE ENTRY PER CONTRADICTION" |
| C-07 | Recommended | 10 | PASS | VERDICT section with M=0 / M>=1 branches |
| C-08 | Recommended | 10 | PASS | Skill + date in both claim slots |
| C-09 | Aspirational | 5 | FAIL | No taxonomy labels |
| C-10 | Aspirational | 5 | PASS | "name the exact skill invocation: 'Resolve with: /discover-inertia --focus switching-cost'" |
| C-11 | Aspirational | 5 | PASS | "GATE FAILED: {N} signal(s) found, need 2+." |
| C-12 | Aspirational | 5 | PASS | "'Investigate further' is not a resolution" named as prohibited |
| C-13 | Aspirational | 5 | FAIL | No inertia-first table |
| C-14 | Aspirational | 5 | FAIL | Prose entries, no named-column table |
| C-15 | Aspirational | 5 | PASS | "Count N, M, K. Don't output yet." + separate "OPEN WITH THE TALLY" section |
| C-16 | Aspirational | 5 | PASS | "The /skill-name token is required -- prose like 'run the inertia skill' doesn't count" |

**Score**: 60 + 30 + 25 = **115 / 130** -- GOLDEN

---

### V-04: Two-phase + token (minimal combination)

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED + glob present |
| C-02 | Essential | 12 | PASS | `"{the specific claim in its own words}"` |
| C-03 | Essential | 12 | PASS | "Exactly `blocking` or `advisory` -- no other values" |
| C-04 | Essential | 12 | PASS | "Do not write 'investigate further'" in both BLOCKING and ADVISORY rules |
| C-05 | Essential | 12 | PASS | Cross-skill rule present |
| C-06 | Recommended | 10 | PASS | PHASE 3 FINDINGS HEADER before PHASE 4 entries |
| C-07 | Recommended | 10 | PASS | PHASE 5 VERDICT with M=0 / M>=1 |
| C-08 | Recommended | 10 | PASS | Skill + date in both claim slots |
| C-09 | Aspirational | 5 | FAIL | No taxonomy labels |
| C-10 | Aspirational | 5 | PASS | BLOCKING: "Resolve with: /{skill-name} [--focus {parameter}]" required |
| C-11 | Aspirational | 5 | PASS | "GATE FAILED: {N} signal(s) found, need 2+." |
| C-12 | Aspirational | 5 | PASS | "Do not write 'investigate further'" in both resolution sections |
| C-13 | Aspirational | 5 | FAIL | No inertia-first table |
| C-14 | Aspirational | 5 | FAIL | Contradiction entries in labeled sections, not Markdown table |
| C-15 | Aspirational | 5 | PASS | PHASE 2 PRE-SCAN: "Do not output any contradiction in this phase" |
| C-16 | Aspirational | 5 | PASS | BLOCKING token format with example + "A blocking entry without the /skill-name token fails" |

**Score**: 60 + 30 + 25 = **115 / 130** -- GOLDEN

---

### V-05: Full stack 130

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED + glob present |
| C-02 | Essential | 12 | PASS | "the specific conflicting statement in its own words, not just the topic" |
| C-03 | Essential | 12 | PASS | Severity column: "exactly `blocking` or `advisory`" |
| C-04 | Essential | 12 | PASS | "Do not write 'investigate further'" in both branches with inline anti-pattern naming |
| C-05 | Essential | 12 | PASS | Cross-skill rule in column rules |
| C-06 | Recommended | 10 | PASS | PHASE 4 FINDINGS HEADER before PHASE 5 tables |
| C-07 | Recommended | 10 | PASS | PHASE 6 VERDICT with M=0 / M>=1 branches |
| C-08 | Recommended | 10 | PASS | "Skill A (date)" and "Skill B (date)" named table columns |
| C-09 | Aspirational | 5 | PASS | Type column: rating-conflict / prediction-conflict / evidence-conflict |
| C-10 | Aspirational | 5 | PASS | BLOCKING requires "/skill-name" token |
| C-11 | Aspirational | 5 | PASS | "GATE FAILED: {N} signal(s) found, need 2+." |
| C-12 | Aspirational | 5 | PASS | "Wrong: 'Investigate the inertia discrepancy' (vague -- fails C-12, C-16)" inline negation |
| C-13 | Aspirational | 5 | PASS | "Inertia Contradictions" table first -- "render it even if empty" |
| C-14 | Aspirational | 5 | PASS | Two Markdown tables with Severity, Resolution, Type columns |
| C-15 | Aspirational | 5 | PASS | PHASE 3 "do not output any contradiction in this phase" + PHASE 4 header |
| C-16 | Aspirational | 5 | PASS | BLOCKING token format with correct/wrong examples; ADVISORY prose rule separate |

**Score**: 60 + 30 + 40 = **130 / 130** -- GOLDEN (perfect)

---

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | FAIL | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-10 | FAIL | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-14 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-15 | PASS | FAIL | PASS | PASS | PASS |
| C-16 | FAIL | PASS | PASS | PASS | PASS |

---

## Predicted vs Actual

| Variation | Predicted | Actual | Delta | Note |
|-----------|-----------|--------|-------|------|
| V-01 | ~105 | 105 | 0 | Exact |
| V-02 | ~110 | 100 | -10 | C-06 fails -- CLOSING tally is after entries; C-15 absence is the cause |
| V-03 | ~105-115 | 115 | at ceiling | Register achieves parity with V-04 structural combination |
| V-04 | ~115-120 | 115 | at floor | C-09, C-13, C-14 fail without table apparatus |
| V-05 | ~130 | 130 | 0 | Exact -- perfect score |

---

## Excellence Signals

### E-01: Dual-table format closes C-09 + C-13 + C-14 simultaneously

The 15-pt gap between V-03/V-04 (115) and V-05 (130) comes entirely from adding a
Markdown table with named columns. A single structural choice -- table format -- satisfies:
- C-09: Type column forces taxonomy labeling (labels are column-enforced, not prose-embedded)
- C-13: Two-table structure with Inertia rendered first enforces priority ordering
- C-14: Named Severity and Resolution columns structurally enforce completeness

This is the same pattern confirmed in R1 and R2. R3 confirms it again: the prose ceiling
is 115/130; table format is required to reach 130/130.

### E-02: V-03 parity with V-04 (register = structure for C-15 and C-16)

Conversational register (V-03, explaining WHY) achieves the same score as the minimal
structural combination (V-04, explicit phase labels + token rules) at 115/130. Both pass
C-15 and C-16. The WHY-explanation mechanism is sufficient to separate the scan and output
phases, and the token explanation ("prose like 'run the inertia skill' doesn't count") is
sufficient to enforce token format. For C-15 and C-16, mechanism matters more than register.

### E-03: V-02 C-06 failure confirms C-15 design rationale

Without two-phase structure (C-15), a tally placed in a CLOSING section will appear
after entries, failing C-06. V-02 is the clean proof: C-16 satisfied (token format), but
C-15 absent (single-pass scan), so C-06 fails. The dependency is structural: C-06
reliability requires C-15.

---

## Round Summary

All 5 variations golden (R3 = 5/5 golden, same as R2).

New criteria C-15 and C-16 confirmed satisfiable by multiple mechanisms: structural phase
labels (V-01, V-04), conversational WHY-explanation (V-03), or worked-example negation
(V-02 for C-16 only). All mechanisms that provide the logical separation/token enforcement
close the criteria equivalently.

Remaining gap from 130: C-09, C-13, C-14 require table format. No variation below V-05
closes these. The dual-table apparatus with Inertia-first ordering is the unique
differentiator.

No new patterns to promote: R3 confirms C-15 and C-16 as codified criteria. No additional
excellence signals emerge that would require a new criterion.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": []}
```
