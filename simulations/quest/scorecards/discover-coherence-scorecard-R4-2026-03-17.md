Scorecard written to `simulations/quest/scorecards/discover-coherence-scorecard-R4-2026-03-17.md`.

---

## Results

**All 5 variations golden** (125–130/130). All predictions exact.

| Rank | Variation | Score | Gap |
|------|-----------|-------|-----|
| 1 | V-01 Minimized phases | **130** | 0 |
| 1 | V-03 Conversational full-stack | **130** | 0 |
| 1 | V-04 Minimized + inertia-motivated | **130** | 0 |
| 1 | V-05 Production candidate | **130** | 0 |
| 5 | V-02 Blocking-priority table | **125** | -5 (C-13 only) |

**R4 findings:**

1. **Phase collapse floor confirmed** — V-01 (6 phases) and V-05 (5 steps) both score 130. The EXTRACT CLAIMS phase in R3-V-05 was scaffolding overhead. Minimum structure: INVENTORY → SILENT SCAN → TALLY HEADER → TABLES → VERDICT.

2. **C-13 diagnostic result** — V-02 fails C-13 as predicted. "Blocking Contradictions" first does not satisfy the inertia-specific pass condition: advisory inertia contradictions render in the second table. The inertia label is structurally required, not just any priority-first ordering.

3. **Register parity extended to 130** — V-03 (conversational WHY-register + table) = 130. Three registers all reach 130 when the dual-table apparatus is present.

4. **Production candidate confirmed** — **V-05** (5 steps, 130/130) is the recommended skill body. **V-03** is the alternative for human-readable contexts.

No new patterns to promote. The series is complete.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": []}
```
aim in internal record + Claim A/B columns "in its own words, not just the topic" |
| C-03 | Essential | 12 | PASS | Severity column "exactly blocking or advisory" |
| C-04 | Essential | 12 | PASS | ADVISORY: "Do not write investigate further." + BLOCKING wrong examples with "fails C-12, C-16" |
| C-05 | Essential | 12 | PASS | "Cross-skill rule: Both skills in each row must be different discover skills." |
| C-06 | Recommended | 10 | PASS | PHASE 3: FINDINGS HEADER before PHASE 4: REPORT tables |
| C-07 | Recommended | 10 | PASS | PHASE 5 VERDICT: M=0 / M>=1 branches |
| C-08 | Recommended | 10 | PASS | Skill A (date) / Skill B (date) named columns |
| C-09 | Aspirational | 5 | PASS | Type column: rating-conflict / prediction-conflict / evidence-conflict |
| C-10 | Aspirational | 5 | PASS | BLOCKING: required token format Resolve with: /skill-name [--focus parameter] |
| C-11 | Aspirational | 5 | PASS | GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check. |
| C-12 | Aspirational | 5 | PASS | Wrong: Investigate the inertia discrepancy (vague -- fails C-12, C-16) inline negation |
| C-13 | Aspirational | 5 | PASS | Inertia Contradictions ... always first + render it even if empty |
| C-14 | Aspirational | 5 | PASS | Two Markdown tables with # / Type / Severity / Skill A / Claim A / Skill B / Claim B / Resolution |
| C-15 | Aspirational | 5 | PASS | PHASE 2: SILENT SCAN (do not output any contradiction in this phase) -> separate PHASE 3 header |
| C-16 | Aspirational | 5 | PASS | BLOCKING: token format with correct/wrong examples; ADVISORY: concrete action in prose, Do not write investigate further. |

**Score**: 60 + 30 + 40 = **130 / 130** -- GOLDEN

Phase collapse is harmless: the EXTRACT CLAIMS step in R3-V-05 was structural overhead, not a functional requirement.

---

### V-02: Blocking-priority table (Output format axis)

7-phase structure; replaces Inertia/Other table split with Blocking/Advisory table split.

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED + glob present |
| C-02 | Essential | 12 | PASS | Claim A / Claim B: the specific conflicting statement in its own words |
| C-03 | Essential | 12 | PASS | Each entry belongs to exactly one severity-labeled table; severity unambiguously assigned by table membership |
| C-04 | Essential | 12 | PASS | Wrong: Investigate the discrepancy (vague -- fails C-12, C-16) + Do not write investigate further |
| C-05 | Essential | 12 | PASS | Cross-skill rule: Both skills in each row must be different discover skills. |
| C-06 | Recommended | 10 | PASS | PHASE 4: FINDINGS HEADER before PHASE 5: REPORT tables |
| C-07 | Recommended | 10 | PASS | PHASE 6 VERDICT: M=0 / M>=1 branches |
| C-08 | Recommended | 10 | PASS | Skill A (date) and Skill B (date) named columns |
| C-09 | Aspirational | 5 | PASS | Type column: three taxonomy labels enforced |
| C-10 | Aspirational | 5 | PASS | required token format Resolve with: /skill-name [--focus parameter] in BLOCKING section |
| C-11 | Aspirational | 5 | PASS | GATE FAILED: {N} signal(s) found, need 2+. |
| C-12 | Aspirational | 5 | PASS | Wrong: Investigate the discrepancy (vague -- fails C-12, C-16) |
| C-13 | Aspirational | 5 | FAIL | Pass condition requires dedicated Inertia Contradictions section. Blocking Contradictions is severity-based, not topic-based -- advisory inertia contradictions render in the second table. No inertia-specific priority section present. |
| C-14 | Aspirational | 5 | PASS | Two Markdown tables; Resolution column present; severity encoded by table name (equivalent named structure) |
| C-15 | Aspirational | 5 | PASS | PHASE 2 EXTRACT CLAIMS + PHASE 3 COUNT+CLASSIFY (both silent) -> PHASE 4 FINDINGS HEADER |
| C-16 | Aspirational | 5 | PASS | BLOCKING token with correct/wrong examples; ADVISORY prose rule with investigate further prohibition |

**Score**: 60 + 30 + 35 = **125 / 130** -- GOLDEN

C-13 confirmed fail: Blocking Contradictions is severity-based, not topic-based. Advisory inertia contradictions render in the second table. The inertia-specific label is required -- not just priority-first ordering. Cleanest experimental confirmation of this requirement in the series.

---

### V-03: Conversational full-stack (WHY-register + dual-table apparatus)

Conversational WHY-first register from R3-V-03 plus the dual-table apparatus from R3-V-05.

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check. |
| C-02 | Essential | 12 | PASS | quote or closely paraphrase the specific conflicting statement. The reader must see exactly what each signal said without opening the source files. |
| C-03 | Essential | 12 | PASS | Severity: blocking / advisory -- no other values. unclear, high-priority, or any other label fails C-03. |
| C-04 | Essential | 12 | PASS | Wrong: Investigate the switching-cost discrepancy (no action -- fails C-12, C-16) |
| C-05 | Essential | 12 | PASS | Cross-skill: Both skills in each row must be different discover skills. |
| C-06 | Recommended | 10 | PASS | OPEN WITH THE TALLY section before TWO TABLES: INERTIA FIRST |
| C-07 | Recommended | 10 | PASS | VERDICT section with M=0 / M>=1 branches |
| C-08 | Recommended | 10 | PASS | Skill A (date) and Skill B (date) named columns |
| C-09 | Aspirational | 5 | PASS | Type: rating-conflict / prediction-conflict / evidence-conflict -- no other values. Using a different label, or leaving this blank, fails C-09. |
| C-10 | Aspirational | 5 | PASS | BLOCKING: Use the exact token format: Resolve with: /skill-name [--focus parameter] |
| C-11 | Aspirational | 5 | PASS | GATE FAILED: {N} signal(s) found, need 2+. |
| C-12 | Aspirational | 5 | PASS | Wrong: Investigate the switching-cost discrepancy (no action -- fails C-12, C-16) |
| C-13 | Aspirational | 5 | PASS | Inertia Contradictions (inertia / switching-cost / workaround-quality / adoption) first; Render the Inertia table first, even if it is empty. Rendering an empty table is correct; omitting it is not. |
| C-14 | Aspirational | 5 | PASS | Two Markdown tables with # / Type / Severity / Skill A / Claim A / Skill B / Claim B / Resolution |
| C-15 | Aspirational | 5 | PASS | COUNT EVERYTHING BEFORE YOU OUTPUT: Before writing any table, read all files and finish your count. Don't output anything yet. -> separate OPEN WITH THE TALLY section |
| C-16 | Aspirational | 5 | PASS | BLOCKING: The leading slash is required. Correct/Wrong examples. ADVISORY: Name a concrete change in prose. No token required, but investigate further fails. |

**Score**: 60 + 30 + 40 = **130 / 130** -- GOLDEN

Register parity extended to 130: conversational WHY-explanations close all 16 criteria when paired with the dual-table apparatus. V-03 is the most human-readable 130-scoring candidate in the series.

---

### V-04: Minimized + inertia-motivated (6 phases + inertia motivation)

6-phase collapse from V-01 plus 2-sentence inertia motivation in PHASE 2 and PHASE 4.

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED + glob |
| C-02 | Essential | 12 | PASS | the specific conflicting statement in its own words + Claim A/B columns |
| C-03 | Essential | 12 | PASS | Severity: blocking / advisory in PHASE 2 + column exactly blocking or advisory |
| C-04 | Essential | 12 | PASS | Wrong: Investigate the discrepancy (vague -- fails C-12, C-16) in BLOCKING; Do not write investigate further. in ADVISORY |
| C-05 | Essential | 12 | PASS | Cross-skill: Both skills in each row must be different discover skills. |
| C-06 | Recommended | 10 | PASS | PHASE 3: FINDINGS HEADER before PHASE 4: REPORT |
| C-07 | Recommended | 10 | PASS | PHASE 5 VERDICT: M=0 / M>=1 |
| C-08 | Recommended | 10 | PASS | Skill A (date) / Skill B (date) named columns |
| C-09 | Aspirational | 5 | PASS | Type column with three taxonomy labels |
| C-10 | Aspirational | 5 | PASS | BLOCKING: Resolve with: /skill-name [--focus parameter] required |
| C-11 | Aspirational | 5 | PASS | GATE FAILED: {N} signal(s) found, need 2+. |
| C-12 | Aspirational | 5 | PASS | Wrong: Investigate the discrepancy (vague -- fails C-12, C-16) |
| C-13 | Aspirational | 5 | PASS | Inertia Contradictions (inertia / switching-cost / workaround-quality / adoption) first; affect product strategy viability directly, making them the highest-priority category. Render the Inertia table even if empty. |
| C-14 | Aspirational | 5 | PASS | Two Markdown tables with named columns |
| C-15 | Aspirational | 5 | PASS | PHASE 2: SILENT SCAN (do not emit any output in this phase) -> PHASE 3: FINDINGS HEADER |
| C-16 | Aspirational | 5 | PASS | BLOCKING token with correct/wrong examples; ADVISORY: Do not write investigate further. |

**Score**: 60 + 30 + 40 = **130 / 130** -- GOLDEN

Inertia motivation adds context without changing scoring. V-04 and V-01 both score 130, confirming the motivation sentences are additive human-readable enhancement, not functional overhead.

---

### V-05: Production candidate (5 steps, merged verdict + artifact)

5-step structure: INVENTORY -> SILENT SCAN -> TALLY HEADER -> TABLES -> VERDICT + ARTIFACT.

| Criterion | Tier | Pts | Result | Evidence |
|-----------|------|-----|--------|---------|
| C-01 | Essential | 12 | PASS | GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check. |
| C-02 | Essential | 12 | PASS | the specific conflicting statement in its own words -- reader must see what each signal said without opening the source files |
| C-03 | Essential | 12 | PASS | Severity: blocking / advisory -- no other values |
| C-04 | Essential | 12 | PASS | Wrong: Investigate the discrepancy (no action -- fails C-12); ADVISORY: Not acceptable: investigate further |
| C-05 | Essential | 12 | PASS | Cross-skill: Skill A and Skill B must be different discover skills. |
| C-06 | Recommended | 10 | PASS | STEP 3: TALLY HEADER (output before any table) before STEP 4: TABLES |
| C-07 | Recommended | 10 | PASS | STEP 5: VERDICT with M=0 / M>=1 |
| C-08 | Recommended | 10 | PASS | Skill A (date) and Skill B (date) named columns |
| C-09 | Aspirational | 5 | PASS | Type: rating-conflict / prediction-conflict / evidence-conflict -- no other values |
| C-10 | Aspirational | 5 | PASS | required token (machine-parseable, directly runnable): Resolve with: /skill-name [--focus parameter] |
| C-11 | Aspirational | 5 | PASS | GATE FAILED: {N} signal(s) found, need 2+. in STEP 1 |
| C-12 | Aspirational | 5 | PASS | Wrong: Investigate the discrepancy (no action -- fails C-12) inline negation |
| C-13 | Aspirational | 5 | PASS | Inertia Contradictions table first; Inertia table renders first, even if empty. |
| C-14 | Aspirational | 5 | PASS | Two Markdown tables with # / Type / Severity / Skill A / Claim A / Skill B / Claim B / Resolution |
| C-15 | Aspirational | 5 | PASS | STEP 2: SILENT SCAN (read everything -- emit nothing) + Do not emit any output. -> STEP 3: TALLY HEADER (output before any table) |
| C-16 | Aspirational | 5 | PASS | BLOCKING: token with no slash token -- fails C-16 wrong example; ADVISORY: concrete prose action (no token required) |

**Score**: 60 + 30 + 40 = **130 / 130** -- GOLDEN

V-05 is the confirmed production candidate: 5 steps, 130/130, leanest prompt in the series that addresses all 16 criteria in a single read-through.

---

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | FAIL | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |

---

## Predicted vs Actual

| Variation | Predicted | Actual | Delta | Note |
|-----------|-----------|--------|-------|------|
| V-01 | 130 | 130 | 0 | Exact |
| V-02 | 125 | 125 | 0 | Exact -- C-13 fails as hypothesized |
| V-03 | 130 | 130 | 0 | Exact |
| V-04 | 130 | 130 | 0 | Exact |
| V-05 | 130 | 130 | 0 | Exact -- production candidate confirmed |

---

## Excellence Signals

### E-01: Phase collapse floor established

V-01 (6 phases) and V-05 (5 steps) both score 130. The structural minimum is: INVENTORY -> SILENT SCAN -> TALLY HEADER -> TABLES -> VERDICT. Additional phases (EXTRACT CLAIMS, separate ARTIFACT) are human-readable scaffolding, not functional scoring requirements.

### E-02: C-13 requires inertia-topic label, not just priority-first ordering

V-02 is the cleanest experimental test of C-13 in the series. Severity-based priority (blocking first) fails; topic-based priority (inertia first) passes. The inertia-specific label is structurally required because it guarantees inertia entries are visible regardless of severity -- advisory inertia contradictions must appear in the first table, which severity-split ordering does not guarantee.

### E-03: Conversational register + table = 130 confirmed

V-03 extends the R3 register-parity finding to 130. Conversational WHY-explanations satisfy all 16 criteria at the same level as structured phase labels when paired with the dual-table apparatus. Three distinct registers (structural phases, minimized headers, conversational WHY-first) all reach 130.

---

## Round Summary

All 5 variations golden. 4 score 130; 1 scores 125 (diagnostic).

R4 answers both framing questions:
1. Can V-05 be shorter than R3-V-05? Yes. V-05 at 5 steps = 130. V-01 at 6 phases = 130. Production candidate confirmed.
2. Is C-13 specifically about inertia? Yes. V-02 confirms: the inertia-specific label is structurally required -- equivalent priority-first table does not extend to severity-split tables.

Recommended production candidate: V-05 (5 steps, 130/130, leanest single-read prompt).
Alternative for human-readable contexts: V-03 (conversational WHY-register, also 130/130).

No new patterns to promote. R4 is a convergence round. The series is complete.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": []}
```
