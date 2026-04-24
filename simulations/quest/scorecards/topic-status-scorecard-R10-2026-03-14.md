## Scorecard: `topic:status` — Round 10, Rubric v10 (max 235)

### Common Baseline (C-01 – C-34): All 5 variants PASS — 225/235

All R10 variants inherit the full C-01–C-31 body from R9 (210 pts) plus Tier 8 (C-32/C-33/C-34 all PASS = 15 pts). Note: R10 V-02 uses a canonical C-34-passing preamble — unlike R9 V-02 which held C-34 at FAIL. The R10 isolation test is C-35 withheld, not C-34.

---

### Tier 9 Differential (C-35, C-36)

#### C-35 — Per-axis trigger sentence characterization

C-35 requires the C-34-compliant preamble to contain at least one dedicated trigger sentence per axis, explicitly characterizing the condition that fires each exit. Axis names alone (`file-absent`, `topic-absent`) satisfy C-34 but not C-35.

| Variant | Preamble per-axis form | C-35 |
|---------|------------------------|------|
| V-01 | Canonical line + `File-absent trigger: strategy.md not present on disk -- output unquantifiable-exposure message and stop immediately.` + `Topic-absent trigger: strategy.md present but {topic} has no registered planned signals -- output topic-specific stop message before PHASE 3 (EXPOSURE COMPUTATION).` | **PASS** |
| V-02 | Canonical single-line only: `file-absent and topic-absent are structurally distinct stop conditions with distinct messages` — no per-axis trigger sentences | **FAIL** |
| V-03 | Per-axis trigger sentences present (same pattern as V-01) | **PASS** |
| V-04 | Per-axis trigger sentences present (lifecycle GUARD variant) | **PASS** |
| V-05 | Per-axis trigger sentences present (execution-body variant) | **PASS** |

V-02 deliberately withholds C-35 to isolate whether per-axis trigger characterization is independently necessary beyond C-34 canonical form.

#### C-36 — Multi-site invariant declaration chain

C-36 requires three independently verifiable declaration sites: (1) preamble (C-34 compliance), (2) GUARD entry names (C-32 compliance), (3) at least one additional structural site. Each site must be independently verifiable without cross-referencing the others.

| Variant | Site 1 (preamble) | Site 2 (GUARD) | Site 3 (additional) | C-36 |
|---------|-------------------|----------------|---------------------|------|
| V-01 | Canonical preamble declaration | `Exit A -- file absent:` / `Exit B -- topic not registered:` | COMMIT DECISION block: `Dual-axis gate invariant: file-absent and topic-absent exits are structurally distinct stop conditions with distinct messages` | **PASS** |
| V-02 | Canonical preamble declaration | Same named exits | COMMIT DECISION block echo (same as V-01, per design context) | **PASS** |
| V-03 | Canonical preamble declaration | Named exits present | Third site withheld — no OUTPUT block echo, no COMMIT DECISION echo | **FAIL** |
| V-04 | Canonical preamble declaration | Named exits present | Lifecycle PHASE 2 OUTPUT field echo | **PASS** |
| V-05 | Canonical preamble declaration | Named exits present | Explicit PHASE 2 OUTPUT DECLARATION in execution body | **PASS** |

V-03 withholds the third site to isolate whether the multi-site chain is independently necessary beyond preamble + GUARD.

---

### Per-Variant Scorecards

#### V-01 — Minimum delta from R9 V-04 (C-35 PASS + C-36 PASS via COMMIT DECISION echo)

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35 | 5/5 | **PASS** |
| Tier 9 | C-36 | 5/5 | **PASS** |
| **Total** | | **235/235** | **36/36** |

Hypothesis confirmed: R9 V-04 scored 230 (C-35 PASS, C-36 FAIL). Adding one line to COMMIT DECISION — `Dual-axis gate invariant: file-absent and topic-absent exits are structurally distinct stop conditions with distinct messages` — satisfies C-36's third-site requirement. That single line is the entire delta from 230 to 235. The COMMIT DECISION block is a commit-framing section, explicitly named as a valid third site under C-36.

---

#### V-02 — C-35 withheld, C-36 present (isolation test for C-35)

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | **C-35** | **0/5** | **FAIL** |
| Tier 9 | C-36 | 5/5 | **PASS** |
| **Total** | | **230/235** | **35/36** |

Isolation test: same COMMIT DECISION third-site echo as V-01 (C-36 PASS), but preamble ends after the canonical C-34 line with no per-axis trigger sentences (C-35 FAIL). Expected 5-point delta from V-01 (235) confirms that per-axis trigger sentences are independently necessary beyond what axis names in the canonical declaration convey.

---

#### V-03 — C-35 present, C-36 withheld (isolation test for C-36)

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35 | 5/5 | **PASS** |
| Tier 9 | **C-36** | **0/5** | **FAIL** |
| **Total** | | **230/235** | **35/36** |

Isolation test: per-axis trigger sentences present (C-35 PASS), but no OUTPUT block echo or commit-framing echo — only preamble and GUARD sites (two sites, not three). C-36 FAIL. Expected 5-point delta from V-01 (235) confirms that the three-site chain is independently necessary beyond rich per-axis preamble characterization.

---

#### V-04 — C-35 PASS + C-36 PASS via lifecycle OUTPUT field

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35 | 5/5 | **PASS** |
| Tier 9 | C-36 | 5/5 | **PASS** |
| **Total** | | **235/235** | **36/36** |

Third site is the lifecycle PHASE 2 OUTPUT field — an OUTPUT block, which is explicitly named as a valid third site category under C-36. C-35 and C-36 jointly satisfied via a different structural placement than V-01.

---

#### V-05 — C-35 PASS + C-36 PASS via execution-body OUTPUT DECLARATION

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32–C-34 | 15/15 | 3/3 PASS |
| Tier 9 | C-35 | 5/5 | **PASS** |
| Tier 9 | C-36 | 5/5 | **PASS** |
| **Total** | | **235/235** | **36/36** |

Third site is an explicit PHASE 2 OUTPUT DECLARATION in the execution body — a third structurally distinct placement from V-01 (COMMIT DECISION) and V-04 (lifecycle OUTPUT field). C-36 satisfied via execution-body structural site.

---

### Ranking

| Rank | ID | Score | Differentiator |
|------|----|-------|----------------|
| T-1 | V-01 | **235/235** | Minimum delta — single COMMIT DECISION echo line added to R9 V-04 |
| T-1 | V-04 | **235/235** | C-36 satisfied via lifecycle PHASE 2 OUTPUT field |
| T-1 | V-05 | **235/235** | C-36 satisfied via execution-body OUTPUT DECLARATION |
| T-4 | V-02 | **230/235** | C-35 withheld — axis names alone insufficient for trigger characterization |
| T-4 | V-03 | **230/235** | C-36 withheld — two sites insufficient for multi-site chain |

---

### C-35 Isolation Confirmed

V-01 (235) vs V-02 (230): clean 5-point gap. Both variants carry the COMMIT DECISION third-site echo (C-36 PASS). The sole difference is the presence of per-axis trigger sentences in the preamble. Axis name alone (`file-absent`) satisfies C-34 but not C-35. Naming the axis and characterizing the condition that fires it are structurally distinct declarations. C-34 ⊄ C-35 confirmed.

### C-36 Isolation Confirmed

V-01 (235) vs V-03 (230): clean 5-point gap. Both variants carry per-axis trigger sentences (C-35 PASS). The sole difference is the presence of the third structural site. Preamble + GUARD entries (two sites) satisfies C-32 and C-34 but not C-36. Three-site chain is independently necessary. C-32 ∧ C-34 ⊄ C-36 confirmed.

### C-36 Site-Agnosticism Confirmed

V-01 (COMMIT DECISION block), V-04 (lifecycle OUTPUT field), V-05 (execution-body OUTPUT DECLARATION): three independent third-site placements, all C-36 PASS at 235. C-36 is confirmed site-agnostic within the named categories. Candidate excellence signal for R10.

---

### Excellence Signals

**Signal 1 — C-35 and C-36 jointly satisfiable: R9 gap closes at R10**

The R9 differentiating observation was that V-04 satisfied C-35 but not C-36, and V-05 satisfied C-36 but not C-35 — no single variant achieved both. R10 closes this gap: V-01, V-04, and V-05 each satisfy both criteria simultaneously. There is no design tension between per-axis trigger depth (C-35) and multi-site chain breadth (C-36). They compose freely.

**Signal 2 — C-36 site-agnosticism across three independent placements**

Three variants achieve C-36 via three structurally different third sites: COMMIT DECISION block (V-01), lifecycle PHASE 2 OUTPUT field (V-04), execution-body OUTPUT DECLARATION (V-05). The criterion is confirmed agnostic to which valid third site is used, consistent with the rubric's "OUTPUT block, commit-framing section, or equivalent" enumeration. A future criterion could add a site-specificity or site-ordering dimension — the current agnosticism is the minimum-sufficient version.

**Signal 3 — Minimum delta achieves maximum score**

V-01 adds one line to the COMMIT DECISION block from R9 V-04's 230-scoring structure: `Dual-axis gate invariant: file-absent and topic-absent exits are structurally distinct stop conditions with distinct messages`. This single line is the complete delta from 230 to 235. No structural reconstruction, no new phases, no template additions. The commit-framing section (COMMIT DECISION) is the lowest-friction third site because it already frames shipping consequences — the invariant echo reads as a natural output decision property rather than a retrofit.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": ["C-35 and C-36 jointly satisfiable in a single variant — no design tension between per-axis trigger depth and multi-site chain breadth; R9 gap closes at R10", "C-36 site-agnosticism confirmed across three independent placements: COMMIT DECISION block, lifecycle OUTPUT field, and execution-body OUTPUT DECLARATION — criterion is agnostic to which valid third site is used within the named categories", "Minimum delta from 230 to 235: single invariant echo line added to a commit-framing section (COMMIT DECISION block) is sufficient to satisfy C-36; no structural reconstruction required"]}
```
