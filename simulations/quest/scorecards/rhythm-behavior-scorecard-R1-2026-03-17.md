## rhythm-behavior — Round 1 Scoring

### Criterion Evaluation Matrix

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| **C-01** Sequence declaration | essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** Single unified report | essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** Blast radius ranking explicit | essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** Spec-gap + contract violation | essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** Per-finding sub-skill attribution | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-06** Actionable next step — top finding | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** Section completeness / null result | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** Blast radius justification per finding | aspirational | FAIL | FAIL | FAIL | FAIL | FAIL |
| **C-09** Cross-sub-skill synthesis | aspirational | FAIL | FAIL | FAIL | FAIL | FAIL |

---

### Per-Criterion Evidence Notes

**C-01 — all PASS.** Every variation declares all five sub-skills in order before the first simulation section. V-01/V-03/V-04 use the `S1 flow-lifecycle -> ... -> FINDINGS` arrow notation; V-02/V-05 use "in this exact order: flow-lifecycle, then flow-conversation...". Both forms name all five and precede S1.

**C-02 — all PASS.** V-01/V-03/V-04: "Produce one unified simulation findings report. Do not split into separate outputs. Do not defer or stub any section." V-02/V-05: "Write everything as one document from start to finish. Do not break it into separate responses. Do not promise to continue." All five sections and FINDINGS are structurally present in every variation.

**C-03 — all PASS.** The rubric requires an explicit ranking mechanism, not implied prose order. Table variations (V-01/V-03/V-04/V-05): FINDINGS section sorts the table with label "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" — explicit column label per row + explicit sort with stated direction. V-02 (no table): "grouped first by blast radius (WIDE issues first, NARROW issues last)" — explicit grouping instruction; per-section "assign a blast radius" instruction ensures each finding carries a WIDE/MEDIUM/NARROW label in prose. PASS confirmed by rubric's "HIGH/MEDIUM/LOW labels" equivalence.

**C-04 — all PASS, with quality gradient.** V-01/V-03/V-04: REQUIRE block at bottom of FINDINGS mandates "At least one finding classified spec-gap / At least one finding classified contract-violation." V-02: "Confirm that your list contains at least one spec-gap and at least one contract-violation. If it does not, revisit the sections above." Recovery path present. V-05 (strongest): "If either category is missing, go back and find at least one before closing the report." — mandatory recovery, strongest enforcement.

**C-05 — all PASS.** Table variations: Sub-Skill column is structural; REQUIRE block reinforces "All findings carry a Sub-Skill attribution." V-02: "For each finding, say which sub-skill surfaced it" — per-finding prose attribution. Finding-level, not section-level. PASS.

**C-06 — all PASS.** All variations include: identify top finding (highest blast radius) + provide one concrete, specific next step + must name the exact spec section, boundary, or component + explicitly disallows "investigate further" generics.

**C-07 — all PASS.** All variations include explicit null-result instruction per section. Phase-level variations (V-03/V-04/V-05) add phase-granularity null results ("INIT: no findings.") which is strictly richer.

**C-08 — all FAIL.** Table variations have an `Impact` column and `Blast Radius` column, but no instruction requires a sentence explaining *why* a finding carries its assigned radius tier naming affected scope. DEFINITIONS explain the levels globally but per-finding justification is not mandated. The rubric requires "every finding includes a one-sentence rationale for its blast radius tier that names the affected scope" — this is missing in all five.

**C-09 — all FAIL.** No variation instructs the model to look for patterns that only become visible across multiple sub-skills. All findings are expected to originate in a single sub-skill. Cross-sub-skill synthesis is entirely absent from the FINDINGS section in all variations.

---

### Composite Scores

| Variation | Essential (4→60) | Recommended (3→30) | Aspirational (2→10) | Composite | Golden? |
|-----------|------------------|--------------------|---------------------|-----------|---------|
| V-01 | 4/4 → 60 | 3/3 → 30 | 0/2 → 0 | **90** | YES |
| V-02 | 4/4 → 60 | 3/3 → 30 | 0/2 → 0 | **90** | YES |
| V-03 | 4/4 → 60 | 3/3 → 30 | 0/2 → 0 | **90** | YES |
| V-04 | 4/4 → 60 | 3/3 → 30 | 0/2 → 0 | **90** | YES |
| V-05 | 4/4 → 60 | 3/3 → 30 | 0/2 → 0 | **90** | YES |

All five variations are golden. The rubric floor is high enough that the structural invariants (table, REQUIRE block, sort label, null-result instructions) clear all nine criteria. Differentiation at this level requires Round 2 aspirational pressure.

---

### Robustness Ranking (within tie at 90)

1. **V-05** — Strongest C-04 recovery ("go back and find"), table + sort label + lifecycle phases, unified-output language hardened against "promise to continue" failure
2. **V-04** — Table + lifecycle phases, clean imperative structure, EXIT gates per section, same C-04 REQUIRE block
3. **V-03** — Same as V-04 but phase descriptions use open questions ("What state does... What happens if...") — richer guidance, slightly more verbose
4. **V-01** — Table baseline, clean single-axis, EXIT gates, REQUIRE block — the canonical structural reference
5. **V-02** — All criteria pass but weakest C-03 mechanism (prose grouping vs labeled sort), weakest C-05 mechanism (prose instruction vs structural column), no EXIT gates, recovery path for C-04 weaker than V-05

---

### Open Question Resolutions

| Question | Resolution |
|----------|-----------|
| Does Blast Radius column satisfy C-03 without separate ranked list? | **YES** — column + sort label + "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" label is explicit ranking signal |
| Does Type column satisfy C-04 distinguishability? | **YES** — structural column enforces per-finding classification |
| Does conversational register risk losing sequence declaration (C-01)? | **NO** — declaration appears as explicit preamble; natural-language form is sufficient |
| Does per-phase S1 prompting violate C-02 continuity? | **NO** — phases are sub-bullets within the single S1 section in all variants |
| Does null-result instruction satisfy C-07? | **YES** — confirmed; phase-level granularity in V-03/V-04/V-05 is a bonus |

---

### Excellence Signals from V-05 (Top Robustness)

1. **Per-category recovery instruction** — "If either category is missing, go back and find at least one before closing the report" is the single highest-value C-04 enforcement pattern. It converts a static REQUIRE check into an active correction loop.
2. **Pre-opened table with append-throughout instruction** — Opening the findings table before S1 and instructing the model to append rows as findings are discovered embeds attribution (Sub-Skill column), classification (Finding Type column), and blast radius (column) at discovery time, not retrospectively. This is the structural reason C-03/C-04/C-05 are satisfied without extra enforcement.
3. **Sort label in consolidated section** — "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW" makes the ranking mechanism self-documenting. The label is the ranking evidence, satisfying C-03 definitively even if a reader skips the table header.

---

### Round 2 Design Targets

C-08 and C-09 are both failing across all variations — they were never targeted. Round 2 should introduce them as explicit variation axes:

- **C-08 axis**: Add a `Blast Radius Rationale` column to the table (or mandate a one-sentence "Why WIDE: ..." annotation per finding) — this is the minimal change to unlock 5 aspirational points
- **C-09 axis**: Add a SYNTHESIS step to FINDINGS instructing the model to identify any finding whose root cause spans two or more sub-skills and name the contributing sub-skills

Recommend carrying **V-05 as the Round 2 base** (highest robustness, strongest C-04 recovery) and adding C-08/C-09 as single-axis tests against it.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Per-category recovery instruction in FINDINGS ('if either category is missing, go back and find at least one') converts C-04 from a static check to an active correction loop", "Pre-opening the findings table before S1 with append-throughout instruction satisfies C-03/C-04/C-05 structurally at discovery time rather than retrospectively in consolidation", "Explicit sort label on consolidated table ('Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW') makes the ranking mechanism self-documenting and satisfies C-03 definitively"]}
```
