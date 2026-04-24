Now I have full context. The R19 scorecard reveals how far the rubric has evolved (v15, C-01–C-44), but Round 2 uses v4 (C-01–C-16). I'll score accordingly. Note: V-01 is the only variation with a full prompt text — V-02 through V-05 are scored on description + R4 V-05 heritage.

---

## mock-ns Round 2 — Scoring (Rubric v4, C-01 through C-16)

**Scoring formula**: `(essential_pass / 5 × 60) + (recommended_pass / 3 × 30) + (aspirational_pass / 8 × 10)`. PARTIAL = 0.5.
**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

### V-01 — Compliance Override Reinstatement

Full prompt provided — criterion-by-criterion verification.

| # | Weight | Criterion | Result | Evidence |
|---|--------|-----------|--------|----------|
| C-01 | essential | MOCK ARTIFACT header complete | **PASS** | S-4 has all 6 fields: `[MOCK ARTIFACT -- NOT VERIFIED]`, Skill, Topic, Category, Date, Status, Flag — in exact order before body content |
| C-02 | essential | Category assignment correct | **PASS** | S-2 exhaustive three-category table; all 30+ skills mapped; "emit error and stop" for unknowns |
| C-03 | essential | Mock body follows golden structure | **PASS** | S-4 body instructions: skill-specific section headings, all required tables/lists, gate/verdict in position, enforcement mechanisms, recognizability test stated |
| C-04 | essential | Flag matches category | **PARTIAL** | Priority rows 2–6 correctly map category → flag. Priority 1 fires for scout-compliance or trace-permissions with compliance tags and produces "REAL-REQUIRED (compliance-sensitive)" — but scout-compliance is HIGH-STRUCTURE; C-04 requires `none` for HIGH-STRUCTURE. This violates C-04's category-to-flag mapping for the compliance-sensitive case |
| C-05 | essential | Artifact path convention | **PASS** | `simulations/mock/{topic}-{namespace}-mock-{date}.md`; skill-id correctly absent from filename |
| C-06 | recommended | Representative skill selection | **PASS** | S-1 lookup table; topic→topic-plan; topic-status exclusion explicit with reason |
| C-07 | recommended | Fidelity warning present | **PASS** | Three category-specific warnings (HIGH-STRUCTURE NOTE / EVIDENCE-HEAVY WARNING / MIXED CAUTION) all present in S-4 |
| C-08 | recommended | Final line is next-step | **PASS** | S-5: Next line + exception clause (omit when called from within mock-review session) |
| C-09 | aspirational | Tier-conditional flag for critical skills | **PASS** | Priority row 2: HIGH-STRUCTURE + Tier 2+ + critical skill → "none (structural coverage reliable; REAL-REQUIRED at Tier 2+)". Critical skills list matches R4 V-05 baseline. Scout-compliance is NOT in the critical list so compliance override doesn't collide with C-09 |
| C-10 | aspirational | TOPICS.md consultation visible | **PASS** | S-0: dedicated TOPICS.md read with explicit emit line before any other output |
| C-11 | aspirational | TOPICS.md emit is first output | **PASS** | CONSTRAINT: "Do not perform skill selection, category lookup, flag computation, or body generation until after the TOPICS.md status line below has been emitted" |
| C-12 | aspirational | Three-field format | **PASS** | Verbatim template: `> TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}` |
| C-13 | aspirational | Fields named by semantic purpose | **PASS** | "All three fields must be present -- existence (found/not found), tier classification, and compliance tags" |
| C-14 | aspirational | Ordering constraint names specific operations | **PASS** | CONSTRAINT names 4 specific operations: skill selection, category lookup, flag computation, body generation |
| C-15 | aspirational | Per-field resolution guidance | **PASS** | Three bullets with downstream actions: existence → tier/tags default if not found; tier → "Carry resolved tier into S-3 for flag computation"; compliance tags → "Carry resolved compliance tags into S-3 for compliance override check" |
| C-16 | aspirational | All three primary ops exhaustively named | **PASS** | CONSTRAINT names skill selection + category lookup + flag computation (+ body generation as 4th guarded op — all three primary ops present) |

**Essential**: 4.5 / 5 (C-04 PARTIAL)  
**Recommended**: 3 / 3  
**Aspirational**: 8 / 8  
**Composite**: (4.5/5 × 60) + (3/3 × 30) + (8/8 × 10) = 54 + 30 + 10 = **94**

---

### V-02 — Body Generation Specificity by Structural Category

No full prompt. Scored on variation description: R4 V-05 base (verified at 100 on v4) + per-category minimal structure hints added to S-4. No compliance override, no depth routing.

| # | Result | Evidence |
|---|--------|----------|
| C-01 | **PASS** | Inherited from R4 V-05 base; per-category hints in S-4 don't affect header fields |
| C-02 | **PASS** | Category table-centric lookup unchanged from R4 V-05 |
| C-03 | **PASS** | Per-category hints explicitly name required element types (headings, tables, gate/verdict, enforcement mechanisms) by category — HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED each get tailored structural guidance. This strengthens C-03 especially for MIXED and EVIDENCE-HEAVY edge cases |
| C-04 | **PASS** | No compliance override; flag computation table from R4 V-05 unchanged. Category-to-flag mapping preserved |
| C-05–C-16 | **PASS** | All inherited from R4 V-05. No changes to INPUTS, S-0 CONSTRAINT, S-1/S-2/S-3 tables, S-5 next-step, field naming, resolution bullets |

**Essential**: 5 / 5  
**Recommended**: 3 / 3  
**Aspirational**: 8 / 8  
**Composite**: 60 + 30 + 10 = **100**

---

### V-03 — Depth Parameter Integration

No full prompt. Scored on variation description: R4 V-05 base + `--depth` (quick/standard/deep) wired as first-class input, body generation length routed through a depth table.

| # | Result | Evidence |
|---|--------|----------|
| C-01 | **PASS** | Depth doesn't affect header fields |
| C-02 | **PASS** | Category lookup unchanged |
| C-03 | **PARTIAL** | Depth routing at `quick` may scope out structural elements (tables, enforcement mechanisms, gate/verdict line). Description says "separates body scope from structural fidelity" — but without per-category structure hints to anchor what structural elements must survive at any depth, `quick` could produce a body that fails C-03's recognizability test. No full prompt to verify that quick depth preserves the complete structural skeleton |
| C-04 | **PASS** | No compliance override; flag computation unchanged |
| C-05–C-16 | **PASS** | S-0 CONSTRAINT unchanged (4 ops); field table, resolution bullets, three-field format, exhaustive op enumeration — all inherited from R4 V-05. Adding `--depth` to INPUTS doesn't alter any of these |

**Essential**: 4.5 / 5 (C-03 PARTIAL)  
**Recommended**: 3 / 3  
**Aspirational**: 8 / 8  
**Composite**: (4.5/5 × 60) + (3/3 × 30) + (8/8 × 10) = 54 + 30 + 10 = **94**

---

### V-04 — Compliance Override + Body Generation Specificity (Two-Axis)

No full prompt. V-01 + V-02 combined. Inherits both their behaviors.

| # | Result | Evidence |
|---|--------|----------|
| C-01–C-03 | **PASS** | V-02's per-category hints reinforce C-03 at all skill types; no depth routing risk |
| C-04 | **PARTIAL** | Inherits V-01's compliance override: scout-compliance/trace-permissions + compliance tags → "REAL-REQUIRED (compliance-sensitive)" for a HIGH-STRUCTURE skill. Same C-04 violation as V-01 |
| C-05–C-16 | **PASS** | V-01 passes C-05–C-16; V-02 doesn't disturb any of them |

**Essential**: 4.5 / 5 (C-04 PARTIAL)  
**Recommended**: 3 / 3  
**Aspirational**: 8 / 8  
**Composite**: 54 + 30 + 10 = **94**

---

### V-05 — Convergent (R4 Heritage + Compliance Override + Body Specificity + Depth Routing)

No full prompt. All four signal families combined.

| # | Result | Evidence |
|---|--------|----------|
| C-01–C-02 | **PASS** | R4 V-05 base |
| C-03 | **PASS** | V-02's per-category hints name required structural elements by category, mitigating V-03's depth routing risk. At any depth, the named element types constrain what "quick scope" means — structural recognizability is preserved even if content density is reduced |
| C-04 | **PARTIAL** | Inherits V-01's compliance override; same C-04 category-flag tension. The compliance override is present in V-05 per its axis description ("R4 heritage + V-01") |
| C-05–C-16 | **PASS** | All inherited; 4-op CONSTRAINT, per-field resolution bullets, three-field format with semantic names, exhaustive three-op enumeration — all present. Compliance-tag carry in C-15 adds the override path explicitly |

**Essential**: 4.5 / 5 (C-04 PARTIAL)  
**Recommended**: 3 / 3  
**Aspirational**: 8 / 8  
**Composite**: 54 + 30 + 10 = **94**

---

### Ranking Summary

| Rank | Variation | Composite | all_essential_pass | Essential failure |
|------|-----------|-----------|-------------------|-------------------|
| 1 | **V-02** | **100** | true | — |
| 2 | V-04 | 94 | false | C-04 PARTIAL (compliance override → HIGH-STRUCTURE flag mismatch; C-03 strongest, no depth risk) |
| 3 | V-01 | 94 | false | C-04 PARTIAL (same; baseline C-03, no depth risk) |
| 4 | V-05 | 94 | false | C-04 PARTIAL (compliance override + depth complexity; C-03 mitigated by per-category hints) |
| 5 | V-03 | 94 | false | C-03 PARTIAL (depth routing risks thinning structural body without per-category guard) |

Within the 94 group, secondary rank: V-04 > V-01 ≈ V-05 > V-03. V-04 has V-02's C-03 reinforcement without V-03's depth risk; V-05 shares that advantage but adds overall complexity.

---

### Excellence Signals

**From V-02 (the winner)** — per-category structure hints in S-4 body generation:  
Adding a short per-category list of required element types to S-4 (naming section headings, table types, gate/verdict, enforcement mechanisms for each of HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED) closes the C-03 gap for edge-case skills without introducing any criterion conflict. It is an additive change — no existing criteria are touched — and it reduces the probability of a structurally thin body for MIXED and EVIDENCE-HEAVY skills where the "golden pattern" instruction alone may be under-constrained. This is the cleanest Round 2 signal: localized to S-4, no side effects.

**Key Round 2 finding (from V-01)** — compliance override creates a C-04 gap requiring rubric expansion:  
The compliance override fires correctly as a business rule (compliance-sensitive skills need REAL-REQUIRED regardless of structural category), but C-04's category-to-flag mapping has no exception clause for compliance overrides. A HIGH-STRUCTURE skill that receives "REAL-REQUIRED (compliance-sensitive)" violates C-04 as written. This is not a bug in V-01's prompt — it is a rubric gap. Round 2 surfaces the need for either (a) a C-04 amendment allowing compliance exception values, or (b) a C-17 criterion that specifically validates compliance-aware flag overrides as a new coverage class.

**Depth routing observation (from V-03)**:  
Depth parameter integration is viable as a single-axis isolation test but needs per-category body hints to safely pass C-03. V-03 alone (depth routing without category hints) carries C-03 risk; V-05's combination of depth routing + category hints resolves it. The pattern is: **depth routing must be paired with structural anchoring (per-category hints) to be C-03-safe**.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-category-structure-hints-in-S4-close-C03-gap-for-MIXED-and-EVIDENCE-HEAVY-skills-without-criterion-conflict", "compliance-override-as-priority-1-flag-row-exposes-C04-rubric-gap-requiring-compliance-exception-clause-or-new-C17-criterion"]}
```
