## quest-variate Scorecard — Round 7

### Scoring Basis

The document is evaluated as a single output artifact: the shared pre-generation section (per-axis pole table, doc-level VARIATION MAP with C-30 columns, combination roadmap, evaluation order, tension notes) plus five individual V-NN variation bodies. Set-level criteria (C-06, C-09, C-10, C-12, C-13, C-16, C-22, C-24, C-27, C-29, C-30) are shared across all variations and scored uniformly. Per-body differentiators are C-33, C-25 (key naming), and C-17/C-18/C-21/C-34 (combination-only).

---

### V-01 — Output Format: Declared Responsibility Key in All Phases

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Complete standalone body: VARIATION MAP, 3 phases, AXIS-FREEZE PROTOCOL, all sections fully written |
| C-02 | PASS | Labeled V-01, proper sequence |
| C-03 | PASS | `axis: output-format`; nested `hypothesis:` block with all sub-fields |
| C-04 | PASS | Single axis: output-format only |
| C-05 | PASS | Distinct from V-02 (no nested schema) and V-03 (no champion-baseline) |
| C-06 | PASS | Set-level: covers output-format, phrasing-register, inertia-framing (3 axes) |
| C-07 | PASS | Directional: "increases C-33 pass rates"; mechanism names the detectability pathway |
| C-08 | PASS | Pre-generation pole table declares all axes; baseline clearly inferable |
| C-09 | PASS | Combination roadmap with 3 rows, criterion IDs |
| C-10 | PASS | Pre-Combination Axis Tension Note surfaces output-format/phrasing-register tension |
| C-11 | PASS | `failure-condition-outcome:` and `failure-condition-implementation:` both present |
| C-12 | PASS | Evaluation order table with 5 rows, cost/independence/dependency columns |
| C-13 | PASS | Axis-Tension Pre-Ranking section with V-04/V-05 dominance predictions |
| C-14 | PASS | "criterion-targeted: C-33" explicit in header |
| C-15 | PASS | AXIS-FREEZE PROTOCOL fires per body before writing; names axes being checked |
| C-16 | PASS | Per-axis pole table covers all 6 axes before any body generated |
| C-17 | PASS | Single-axis: vacuous |
| C-18 | PASS | Single-axis: vacuous |
| C-19 | PASS | Header hypothesis has criterion-target, direction, mechanism ("because..."), failure conditions — all four structurally labeled in single entry |
| C-20 | PASS | Outcome failure (C-33 rate unchanged) vs implementation failure (label text restates title, independently violates C-23) — mechanistically distinct |
| C-21 | PASS | Single-axis: vacuous |
| C-22 | PASS | Roadmap rows: C-33+C-19+C-07 / C-33+C-08+C-16 / C-19+C-08+C-16 |
| C-23 | PASS | Phase 1 / Phase 2 / Phase 3 numbered, labeled, with named transition points |
| C-24 | PASS | Doc-level VARIATION MAP has per-variation per-criterion directional predictions with mechanism sentences |
| C-25 | PASS | `failure-condition-outcome:` (not `failure-condition:`) as first key; `failure-condition-implementation:` as second key |
| C-26 | PASS | AXIS-FREEZE PROTOCOL: Step 1 reads VARIATION MAP, Step 2 names and freezes all 6 axes, Step 3 writes |
| C-27 | PASS | `## VARIATION MAP — Immutable after Phase 2 begins` as top-level header with immutability instruction |
| C-28 | PASS | "A freeze list with fewer than six entries is incomplete — do not proceed" |
| C-29 | PASS | "The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table"; Step 2 entries labeled "read from VARIATION MAP for this body" |
| C-30 | PASS | Doc-level VARIATION MAP has `failure-condition-outcome prediction` and `failure-condition-implementation prediction` columns |
| C-31 | PASS | Step 2B: "VARIATION MAP assigned axis for this V-NN" vs "Phase 1 header declared axis for this V-NN" |
| C-32 | PASS | `Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]` as named binary token in Step 2B |
| C-33 | **PASS** | Phase 1: `Declared responsibility: lock axis assignments…`; Phase 2: `Declared responsibility: write each committed variation body…`; Phase 3: `Declared responsibility: confirm in-loop axis consistency…` — all 3 phases carry the labeled key |
| C-34 | PASS | Single-axis: vacuous |

**Essential:** 5/5 → 60  
**Recommended:** 3/3 → 30  
**Aspirational:** 26/26 → 10  
**Composite: 100** | **Band: Gold**

---

### V-02 — Phrasing Register: Four-Part Nested Hypothesis Schema

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Runnable, labeled, single-axis (phrasing-register), genuinely distinct |
| C-06–C-16 | PASS | All shared/set-level criteria met (same as V-01 basis) |
| C-17 | PASS | Single-axis: vacuous |
| C-18 | PASS | Single-axis: vacuous |
| C-19 | PASS | Header has nested `hypothesis:` with all four sub-fields; template ALSO enforces nested schema for generated variations |
| C-20 | PASS | `failure-condition:` + `failure-condition-implementation:` — outcome (C-19 no improvement) vs implementation (mechanism field restates direction, independently failing C-07) |
| C-21 | PASS | Single-axis: vacuous |
| C-22–C-24 | PASS | Shared roadmap/map |
| C-25 | **FAIL** | First failure condition keyed as `failure-condition:`, not `failure-condition-outcome:` — C-25 requires the canonical key name `failure-condition-outcome:` to be structurally detectable without prose parsing |
| C-26–C-32 | PASS | Shared template structure |
| C-33 | **FAIL** | Phase 1 and Phase 2 have no `Declared responsibility:` labeled key — the axis change does not touch phase headers; only Phase 3 carries the key. C-33 requires ALL phases |
| C-34 | PASS | Single-axis: vacuous |

**Essential:** 5/5 → 60  
**Recommended:** 3/3 → 30  
**Aspirational:** 24/26 → 9.23  
**Composite: 99.2** | **Band: Gold**

---

### V-03 — Inertia Framing: Champion-Baseline Field at Body Scope

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Runnable, labeled, single-axis (inertia-framing), genuinely distinct |
| C-06–C-16 | PASS | All shared/set-level criteria met |
| C-17 | PASS | Single-axis: vacuous |
| C-18 | PASS | Single-axis: vacuous |
| C-19 | PASS | Header has criterion-target, direction, mechanism ("because…"), failure conditions — all four parts |
| C-20 | PASS | Outcome failure (C-08/C-16 no improvement over pre-gen scope) vs implementation failure (champion-baseline lacks round qualifier, independently fails C-16) |
| C-21 | PASS | Single-axis: vacuous |
| C-22–C-24 | PASS | Shared |
| C-25 | **FAIL** | First failure condition keyed as `failure-condition:`, not `failure-condition-outcome:` — same defect as V-02 |
| C-26–C-32 | PASS | Shared template structure; AXIS-FREEZE PROTOCOL fires with count gate and verdict token |
| C-33 | **FAIL** | Phase 1 and Phase 2 lack `Declared responsibility:` key — axis change adds `champion-baseline:` at body scope only, does not touch phase-level structure |
| C-34 | PASS | Single-axis: vacuous |

**Essential:** 5/5 → 60  
**Recommended:** 3/3 → 30  
**Aspirational:** 24/26 → 9.23  
**Composite: 99.2** | **Band: Gold**

---

### V-04 — Combination: Output Format × Phrasing Register

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Runnable; labeled; C-04 exception explicitly invoked; distinct from V-05 (phrasing-register vs inertia-framing second axis) |
| C-06–C-16 | PASS | All shared/set-level criteria met |
| C-17 | PASS | "Do not revise axis assignments after Phase 2 begins" in template |
| C-18 | PASS | `failure-condition-outcome:` cites "V-01 R7 alone (C-33 single-axis baseline)" and "V-02 R7 alone (C-19 single-axis baseline)" |
| C-19 | PASS | Header has all four parts; template enforces nested `hypothesis:` schema |
| C-20 | PASS | Outcome failure (joint C-33+C-19 no compound benefit) vs implementation failure (mechanism sub-field collapses to outcome restatement, independently failing C-07) |
| C-21 | PASS | "C-04 exception explicitly invoked" verbatim at line 653 |
| C-22–C-24 | PASS | Shared |
| C-25 | PASS | `failure-condition-outcome:` and `failure-condition-implementation:` as distinct named keys |
| C-26–C-32 | PASS | Phase 2 AXIS-FREEZE PROTOCOL with all gates |
| C-33 | PASS | Phase 1: `Declared responsibility: lock axis assignments… hypothesis: block present with all four sub-fields non-blank…`; Phase 2: `Declared responsibility: write each committed variation body in full under the AXIS-FREEZE PROTOCOL…`; Phase 3: `Declared responsibility: post-generation axis consistency audit, hypothesis schema compliance audit…` |
| C-34 | PASS | "V-01 R7 alone" and "V-02 R7 alone" — round qualifiers present in both denominators |

**Essential:** 5/5 → 60  
**Recommended:** 3/3 → 30  
**Aspirational:** 26/26 → 10  
**Composite: 100** | **Band: Gold**

---

### V-05 — Combination: Output Format × Inertia Framing

| ID | Result | Evidence |
|----|--------|---------|
| C-01–C-05 | PASS | Runnable; labeled; C-04 exception explicitly invoked; distinct from V-04 |
| C-06–C-16 | PASS | All shared/set-level criteria met |
| C-17 | PASS | "Do not revise axis assignments after Phase 2 begins" in template |
| C-18 | PASS | `failure-condition-outcome:` cites "V-01 R7 alone (C-33 single-axis baseline)" and "V-03 R7 alone (C-08/C-16 single-axis baseline)" |
| C-19 | PASS | Header has all four parts |
| C-20 | PASS | Outcome failure (no compound C-33+C-08/C-16 benefit) vs implementation failure (champion-baseline citation without round qualifier, independently fails C-34) |
| C-21 | PASS | "C-04 exception explicitly invoked" verbatim at line 852 |
| C-22–C-24 | PASS | Shared |
| C-25 | PASS | `failure-condition-outcome:` and `failure-condition-implementation:` as distinct named keys |
| C-26–C-32 | PASS | Phase 2 AXIS-FREEZE PROTOCOL with all gates and verdict token |
| C-33 | PASS | Phase 1: `Declared responsibility: lock axis assignments…`; Phase 2: `Declared responsibility: write each committed variation body…` including "`champion-baseline:` field populated with round-qualified prior-champion citation…"; Phase 3: `Declared responsibility: post-generation axis consistency audit, champion-baseline citation audit…` |
| C-34 | PASS | "V-01 R7 alone" and "V-03 R7 alone" — round qualifiers present |

**Essential:** 5/5 → 60  
**Recommended:** 3/3 → 30  
**Aspirational:** 26/26 → 10  
**Composite: 100** | **Band: Gold**

---

### Rankings

| Rank | V | Axis | Composite | Fails |
|------|---|------|-----------|-------|
| 1 (tie) | V-01 | output-format | **100** | none |
| 1 (tie) | V-04 | output-format × phrasing-register | **100** | none |
| 1 (tie) | V-05 | output-format × inertia-framing | **100** | none |
| 4 (tie) | V-02 | phrasing-register | **99.2** | C-25, C-33 |
| 4 (tie) | V-03 | inertia-framing | **99.2** | C-25, C-33 |

---

### Excellence Signals

**Why V-01, V-04, V-05 score higher than V-02, V-03:**

1. **`Declared responsibility:` in ALL phases (C-33)** — V-01 adds the labeled key to Phase 1 and Phase 2 (Phase 3 already had it from baseline). V-04 and V-05 inherit this. V-02 and V-03 change other axes and never touch phase headers, so Phase 1 and Phase 2 remain unlabeled. The deduction is small (1 aspirational criterion) but the signal is clean: axis changes that don't include phase-structure modifications leave C-33 failing.

2. **`failure-condition-outcome:` as canonical first key (C-25)** — V-01, V-04, V-05 use `failure-condition-outcome:` consistently. V-02 and V-03 use `failure-condition:` for the first condition — structurally different from the canonical key name, which fails C-25 even though the content satisfies C-20. This is a key-naming discipline gap: `failure-condition:` and `failure-condition-outcome:` are not interchangeable once C-25 is active.

3. **Combination-axis-specific `Declared responsibility:` text (V-04, V-05)** — Both combination passes customize their Phase 2 `Declared responsibility:` text to name the specific structural addition from the second axis: V-04 names "`hypothesis:` block present with all four sub-fields non-blank"; V-05 names "`champion-baseline:` field populated with round-qualified prior-champion citation." The key text does not just describe the generic phase action — it names the specific mechanism that makes the phase's commitment verifiable. This exceeds what C-33 requires and points toward a v8 criterion.

---

### Write Scorecard

```
simulations/quest/scorecards/quest-variate-scorecard-R7-2026-03-15.md
```

| V | Essential | Recommended | Aspirational | Composite | Band | C-33 | C-25 | C-34 |
|---|-----------|-------------|--------------|-----------|------|------|------|------|
| V-01 | 5/5 | 3/3 | 26/26 | 100 | Gold | PASS | PASS | vac |
| V-02 | 5/5 | 3/3 | 24/26 | 99.2 | Gold | FAIL | FAIL | vac |
| V-03 | 5/5 | 3/3 | 24/26 | 99.2 | Gold | FAIL | FAIL | vac |
| V-04 | 5/5 | 3/3 | 26/26 | 100 | Gold | PASS | PASS | PASS |
| V-05 | 5/5 | 3/3 | 26/26 | 100 | Gold | PASS | PASS | PASS |

**Top score:** 100 (V-01, V-04, V-05)  
**All essential pass:** YES  
**Golden threshold met:** ALL FIVE variations (≥80, all essential pass)

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["failure-condition-outcome: as canonical first key for all variation hypotheses with dual failure conditions, not only combination passes — failure-condition: and failure-condition-outcome: are not interchangeable once C-25 is active; single-axis variations should use the canonical key pair", "Combination-aware Declared responsibility: key text names the specific structural mechanism enforced by that phase (protocol name, field name, or criterion ID), not just the generic phase action — makes the declaration verifiable against a named element rather than a prose description"]}
```
