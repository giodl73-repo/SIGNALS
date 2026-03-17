I now have all five variations. Let me score systematically.

---

# Scorecard: `topic:status` — Round 6

**Rubric:** v6 (max 180) | **Variations:** V-01 through V-05

---

## Criterion-by-Criterion Evaluation

### Essential (C-01--C-04, 60 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Signal discovery | PASS | PASS | PASS | PASS | PASS |
| C-02 Coverage percentage | PASS | PASS | PASS | PASS | PASS |
| C-03 Gap identification | PASS | PASS | PASS | PASS | PASS |
| C-04 Display-only behavior | PASS | PASS | PASS | PASS | PASS |

All variants: `Glob: simulations/**/{topic}-*` with `DISK` variable, zero case handled; `percent = total_verified / total_planned * 100` with consistency check; COMMIT RISKS section with named gaps; DISPLAY CONTRACT + DISPLAY GATE pre-display check. All four essential: **PASS across all variants**.

---

### Recommended (C-05--C-07, 30 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05 Readiness verdict | PASS | PASS | PASS | PASS | PASS |
| C-06 Namespace breakdown | PASS | PASS | PASS | PASS | PASS |
| C-07 Strategy cross-reference | PASS | PASS | PASS | PASS | PASS |

COMMIT DECISION with consequence sentence; 9-row namespace table pre-seeded; `strategy.md` named in commit baseline field with FOUND/NOT FOUND branch. All three recommended: **PASS across all variants**.

---

### Aspirational (C-08--C-12, 25 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 Recency awareness | PASS | PASS | PASS | PASS | PASS |
| C-09 Actionable next step | PASS | PASS | PASS | PASS | PASS |
| C-10 Structural namespace completeness | PASS | PASS | PASS | PASS | PASS |
| C-11 Phase-gated execution | PASS | PASS | PASS | PASS | PASS |
| C-12 Gap-first output ordering | PASS | PASS | PASS | PASS | PASS |

STALE EVIDENCE with age; HIGHEST PRIORITY RISK with skill invocation; 9 rows in template (Zero row: `0 | 0 | --`); named phases + DISPLAY GATE pre-check; COMMIT RISK REGISTER precedes EXPOSURE SUMMARY. All five aspirational: **PASS across all variants**.

---

### Structural Tier 2 (C-13--C-16, 20 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-13 Triple-redundancy ordering guard | PASS | PASS | PASS | PASS | PASS |
| C-14 Template-first structural absorption | PASS | PASS | PASS | PASS | PASS |
| C-15 Per-signal assertion chain | PASS | PASS | PASS | PASS | PASS |
| C-16 Consequence-framed readiness verdict | PASS | PASS | PASS | PASS | PASS |

Three structurally distinct layers present at mechanism locations; output template precedes execution section; each P in PLANNED receives exactly one VERIFIED/UNVERIFIED assertion; "Committing now means shipping without: {list}" present. All four Tier 2: **PASS across all variants**.

---

### Structural Tier 3 (C-17--C-19, 15 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-17 Labeled redundancy layers | PASS | PASS | PASS | PASS | PASS |
| C-18 Assertion table pre-seeded in template | PASS | PASS | PASS | PASS | PASS |
| C-19 Consequence vocabulary saturation | PASS | PASS | PASS | PASS | PASS |

`[LAYER 1 -- STRUCTURAL]`, `[LAYER 2 -- SEMANTIC]`, `[LAYER 3 -- EXECUTION]` labels present at mechanism locations in template; COMMIT RISK REGISTER table with VERIFIED/UNVERIFIED columns is in the output template (before execution section); all section headers use consequence vocabulary (COMMIT RISK REGISTER, COMMIT RISKS, EXPOSURE SUMMARY, COMMIT DECISION, HIGHEST PRIORITY RISK). All three Tier 3: **PASS across all variants**.

---

### Structural Tier 4 (C-20--C-22, 15 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-20 Assertion table as primary gap display artifact | PASS | PASS | PASS | PASS | PASS |
| C-21 Execution phase names in consequence vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-22 Missing baseline as epistemic consequence | PASS | PASS | PASS | PASS | PASS |

COMMIT RISK REGISTER labeled `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]`; phases named SIGNAL ACQUISITION / COMMITMENT ASSERTION / EXPOSURE COMPUTATION / DISPLAY GATE; "No planned baseline -- commit exposure is unquantifiable." All three Tier 4: **PASS across all variants**.

---

### Structural Tier 5 (C-23--C-25, 15 pts) — differentiating tier

#### C-23: Phase name as compressed criterion statement

Pass condition: phase name contains both an evaluation-granularity term (`PER-SIGNAL`) and a decision-stake term (`COMMITMENT`). C-21 pass required but not sufficient.

| Var | Phase 2 header | Verdict | Evidence |
|-----|---------------|---------|----------|
| V-01 | `COMMITMENT ASSERTION (per signal -- no batch evaluation)` | **FAIL** | Granularity qualifier `per signal` is in parenthetical note, not in the phase name itself. Phase name encodes decision stake only. |
| V-02 | `PER-SIGNAL COMMITMENT ASSERTION (no batch evaluation)` | **PASS** | `PER-SIGNAL` prefix encodes evaluation granularity; `COMMITMENT ASSERTION` encodes decision stake. Both dimensions in the name itself. |
| V-03 | `COMMITMENT ASSERTION (per signal -- no batch evaluation)` | **FAIL** | Identical to V-01 on this axis. |
| V-04 | `COMMITMENT ASSERTION (per signal -- no batch evaluation)` | **FAIL** | Identical to V-01 on this axis. |
| V-05 | `PER-SIGNAL COMMITMENT ASSERTION (no batch evaluation)` | **PASS** | Identical to V-02 on this axis. |

#### C-24: Cross-layer vocabulary coherence

Pass condition: [LAYER 3] enforcement label reads `DISPLAY GATE render order:` (not `Phase 4 render order:`); no enforcement label reverts to generic phase-number vocabulary.

| Var | [LAYER 3] label text | Additional note | Verdict | Evidence |
|-----|---------------------|-----------------|---------|----------|
| V-01 | `DISPLAY GATE render order: COMMIT RISK REGISTER -> ...` | None | **PASS** | Consequence-phase vocabulary in enforcement label. No "Phase N" anywhere in enforcement infrastructure. |
| V-02 | `DISPLAY GATE render order: COMMIT RISK REGISTER -> ...` | None | **PASS** | Same as V-01. |
| V-03 | `DISPLAY GATE render order: ...` + `Note: 'DISPLAY GATE' is the Phase 4 consequence name (not 'Phase 4'). Enforcement labels adopt consequence-phase vocabulary.` | Vocabulary coherence invariant block added before [LAYER 1] | **PASS** | C-24 satisfied plus explicitly stated as architectural rule. |
| V-04 | `DISPLAY GATE render order: COMMIT RISK REGISTER -> ...` | None | **PASS** | Same as V-01. |
| V-05 | `DISPLAY GATE render order: ...` + `Note: 'DISPLAY GATE' is the Phase 4 consequence name ...` | Vocabulary coherence invariant block present | **PASS** | Same as V-03. |

#### C-25: Template field inline consequence annotation

Pass condition: at least one template field contains epistemic consequence inline in the format string. Consequence structurally inseparable from the field.

| Var | Field(s) with inline annotation | Verdict | Evidence |
|-----|--------------------------------|---------|----------|
| V-01 | `strategy.md` field: `[FOUND: commit exposure is quantifiable \| NOT FOUND: commit exposure is unquantifiable]` | **PASS** | Inline in field format string; consequence structurally inseparable. |
| V-02 | Same as V-01 | **PASS** | No change to template fields on this axis. |
| V-03 | Same as V-01 | **PASS** | No change to template fields on this axis. |
| V-04 | `strategy.md` field (as V-01) + COMMIT RISKS entry: `[absent: ships without this signal if committed now]` + STALE EVIDENCE entry: `({N} days old -- if stale: commit may rest on evidence that no longer reflects current state)` | **PASS** | Extends to three fields. Consequence inline in each format string. |
| V-05 | Same three fields as V-04 | **PASS** | Same as V-04. |

All variants pass C-25 (minimum threshold is one field; the baseline strategy.md annotation was already present in V-01 as R5 inheritance).

---

## Composite Scores

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-02 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-03 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-04 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-05 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-09 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-17 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-18 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-19 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-20 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-21 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-22 | 5 | 5 | 5 | 5 | 5 | 5 |
| **C-23** | **5** | **0** | **5** | **0** | **0** | **5** |
| C-24 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-25 | 5 | 5 | 5 | 5 | 5 | 5 |
| **TOTAL** | **180** | **175** | **180** | **175** | **175** | **180** |

---

## Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 (tie) | **V-02** | **180/180** | C-23: PER-SIGNAL phase name — minimum path to closure |
| 1 (tie) | **V-05** | **180/180** | C-23 + C-24 explicit + C-25 extended — full structural depth |
| 3 (tie) | V-01 | 175/180 | R5 V-05 baseline — fails only C-23 |
| 3 (tie) | V-03 | 175/180 | C-24 explicitly stated but C-23 not targeted |
| 3 (tie) | V-04 | 175/180 | C-25 extended to 3 fields but C-23 not targeted |

**All essential criteria pass in all variations.** Passing threshold satisfied (all variants >= 80).

---

## Excellence Signals from V-02 / V-05

**E-1 (from V-02 and V-05) — Phase name as self-certifying specification:** `PER-SIGNAL COMMITMENT ASSERTION` is not merely a label — it is a compressed specification. A reviewer reading only the phase names can reconstruct both key constraints: evaluation granularity (per-signal, not batch) and decision frame (commitment, not status). This collapses the C-15 structural requirement into the execution architecture metadata layer, reducing the documentation surface needed to audit the skill.

**E-2 (from V-03 and V-05) — Explicit invariant declaration:** Adding a "Vocabulary coherence invariant" block that names the architectural rule makes the rule auditable without inferring it from content. C-24 is satisfied by the implementation in V-01; V-03/V-05 upgrade C-24 from implicit compliance to an explicitly declared design property. The invariant block also serves as documentation for future maintainers: the rule is stated, not merely instantiated.

**E-3 (from V-04 and V-05) — Consequence annotation pervasion across gap entries:** V-04/V-05 extend the C-25 field-level inline consequence principle to gap entries and stale entries. The commit risk entry reads `[absent: ships without this signal if committed now]` — every gap item is self-documenting about its ship impact without requiring readers to consult a surrounding note. This is architecturally stronger than C-25 (which requires at least one field) because the consequence framing is pervasive rather than localized.

**R7 candidate patterns (not yet captured by rubric):**

- **C-26 candidate:** *Consequence annotation pervasion* — every template field that carries decision-relevant data (gap entries, stale entries, not just the baseline field) contains its ship consequence inline. Extends C-25 from threshold (one field) to saturation (all decision-relevant fields). Parallels the C-16 -> C-19 escalation pattern.
- **C-27 candidate:** *Explicit invariant declaration* — architectural rules satisfied by the skill (vocabulary coherence, template-first placement, gap-first ordering) are explicitly stated as named invariants within the skill itself, making compliance auditable by inspection of the invariant statements rather than by full content analysis. The skill becomes self-certifying at the constraint level.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Consequence annotation pervasion -- every decision-relevant template field contains ship consequence inline (extends C-25 from one-field threshold to all-field saturation)", "Explicit invariant declaration -- architectural rules stated as named invariants making compliance auditable by inspection not inference (C-24 upgraded from implicit compliance to declared property)"]}
```
