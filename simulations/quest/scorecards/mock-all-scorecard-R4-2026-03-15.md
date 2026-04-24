## mock-all Variate — Round 4 Scoring (Rubric v4)

**Rubric:** v4 (C-01–C-17; aspirational denominator = 9)
**Scoring formula:** Essential (60) + Recommended (30) + Aspirational (9 criteria × 1.11 = 10)

---

### Essential Criteria Assessment (C-01–C-05)

All five variations share the same essential structure — all pass across the board.

| Criterion | All Variations |
|-----------|---------------|
| C-01 — Nine MOCK ARTIFACT header blocks | PASS — Phase 2 (or STEP 2) section format defines the MOCK ARTIFACT block for each namespace |
| C-02 — Category classification for every namespace | PASS — Classification table assigns all 9 namespaces in Phase 1 |
| C-03 — REAL-REQUIRED on EVIDENCE-HEAVY namespaces | PASS — REAL-REQUIRED rule names prove and listen explicitly; rationale present |
| C-04 — Coverage summary table with correct columns | PASS — Phase 3 (or STEP 3) defines Namespace / Category / Flag / Recommended Next Step |
| C-05 — Final handoff pattern | PASS — Phase 4 (or STEP 4) "#### HANDOFF" block with `Next: /mock:review {topic}...` |

---

### Recommended Criteria Assessment (C-06–C-08)

All five variations pass all recommended criteria.

| Criterion | All Variations |
|-----------|---------------|
| C-06 — Tier 2/3 critical namespaces flagged | PASS — TIER-CRITICAL flag rule covers trace-*, scout-feasibility, listen-* at tier >= 2 |
| C-07 — Plausible synthetic artifact body | PASS — Phase 2 vocabulary rules and pre-populated MUST use terms provide sufficient generation scaffolding; V-03/V-05 additionally prime bodies via inertia framing |
| C-08 — Compliance-tagged topics pre-flagged | PASS — Compliance-Tagged column + COMPLIANCE flag in summary rules; scout-compliance and trace-permissions gated on --compliance / TOPICS.md |

---

### Aspirational Criteria Assessment (C-09–C-17)

#### V-01 — Vocabulary-Column Anchoring (Output Format)

| C# | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Tier 2/3 Critical column in Phase 1 table scopes TIER-CRITICAL outputs correctly |
| C-10 | PASS | "Recommended Next Step: exact skill call. DO NOT write 'gather more signals.' Example: `/trace:component {topic}`" |
| C-11 | PASS | "Output the classification table — including vocabulary rule columns — before writing any artifact body" — explicit pre-generate ordering |
| C-12 | PASS | `#### HANDOFF` dedicated section at Phase 4 with explicit anti-placeholder instruction |
| C-13 | PASS | "REAL-REQUIRED rule: …A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY namespaces" — rationale in preamble scoping all placements |
| C-14 | PASS | Three explicit stop-gates: Phase 1→2, Phase 2→3, Phase 3→4 each use "Do not begin PHASE N+1 until…" form |
| C-15 | PASS | DO NOT use terms per namespace in table: prove row "DO NOT use specification language, schema definitions, contract structures"; flow row "DO NOT use interview language, user quotes, adoption percentages, study framing" — prohibition clauses present per category |
| C-16 | PASS | Phase 1→2 gate enumerates all five fields: "Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value (YES or NO), and Compliance-Tagged value (YES or NO)" |
| C-17 | PASS | MUST use / DO NOT use appear as columns in the classification table, co-located with category assignment |

**Aspirational: 9/9 | Score: 100.0**

---

#### V-02 — Enumerated Stop-Gates on Vocabulary-Column Table (Lifecycle Emphasis)

| C# | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Tier 2/3 Critical column present |
| C-10 | PASS | "Recommended Next Step: exact skill call — `/skill:subskill {topic}`. DO NOT write 'run the real skill.'" |
| C-11 | PASS | "Before writing any artifact body, assign every namespace to a category" — explicit pre-generate ordering at STEP 1 |
| C-12 | PASS | `#### HANDOFF` section at STEP 4; "Write this section only. No artifact bodies, no table rows, no other content." |
| C-13 | PASS | "A synthetic artifact cannot substitute for real signal in EVIDENCE-HEAVY namespaces" in REAL-REQUIRED rule block |
| C-14 | PASS | Explicit gate sentences at all three STEP boundaries: "Do not begin STEP 2/3/4 until…" form |
| C-15 | PASS | DO NOT use columns in table; Phase 2 adds redundant "DO NOT use specification language in any EVIDENCE-HEAVY artifact body" at generation step |
| C-16 | PASS | STEP 1→2 gate enumerates: "assigned category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value (YES or NO), and Compliance-Tagged value (YES or NO)" — five named fields |
| C-17 | PASS | MUST use / DO NOT use as table columns in STEP 1 classification table |

**Aspirational: 9/9 | Score: 100.0**

---

#### V-03 — Inertia Framing (Single-Axis)

| C# | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Tier 2/3 Critical column present |
| C-10 | PASS | "exact skill call that turns this mock into real signal for {topic}"; example `/listen:adoption {topic}` |
| C-11 | PASS | "Assign every namespace to exactly one category before writing any artifact body" at Phase 1 |
| C-12 | PASS | `#### HANDOFF` dedicated Phase 4 section |
| C-13 | PASS | "Rationale: A synthetic artifact cannot substitute for real signal" present in REAL-REQUIRED block |
| C-14 | PASS | Stop-gate sentences at all three phase boundaries: "Do not begin PHASE 2/3/4 until…" |
| C-15 | PASS | Prose vocabulary block has explicit DO NOT prohibitions per category: HIGH-STRUCTURE "DO NOT use interview language, user quotes, adoption percentages"; EVIDENCE-HEAVY "DO NOT use specification language, contract structures, or schema definitions"; MIXED "DO NOT use pure specification language alone OR pure study framing alone" |
| C-16 | PASS | Phase 1→2 gate enumerates the three columns that exist in the V-03 table: "Category, Tier 2/3 Critical value (YES or NO), and Compliance-Tagged value (YES or NO)." Gate is field-specific (not a generic "until complete" signal); enumerates exactly the output fields the table requires |
| C-17 | **FAIL** | MUST use / DO NOT use rules are in a prose block ("Vocabulary rules by category") positioned *below* the classification table, not as table columns. Vocabulary rules are not co-located with category assignment in the table structure |

**Aspirational: 8/9 | Score: 60 + 30 + (8/9 × 10) = 98.9**

---

#### V-04 — Vocabulary Columns + Enumerated Gates (Combined)

| C# | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Tier 2/3 Critical column present |
| C-10 | PASS | "DO NOT write 'gather more signals' or 'run the real skill.' Write the exact identifier." |
| C-11 | PASS | "The classification table — with vocabulary rule columns — must be fully completed before any artifact body is written" |
| C-12 | PASS | `#### HANDOFF` dedicated section; "DO NOT write any other content in this section" |
| C-13 | PASS | "REAL-REQUIRED rule (embedded at classification step, applied throughout): prove and listen are EVIDENCE-HEAVY. A synthetic artifact cannot substitute for real signal." |
| C-14 | PASS | Stop-gate sentences at all three phase boundaries in PHASE label register |
| C-15 | PASS | DO NOT use column pre-populated per namespace; Phase 2 adds "MUST use satisfied, DO NOT use not violated" as generation compliance check |
| C-16 | PASS | Phase 1→2 gate enumerates: "Category, MUST use terms, DO NOT use terms, Tier 2/3 Critical value (YES or NO), and Compliance-Tagged value (YES or NO)" — five named fields |
| C-17 | PASS | MUST use / DO NOT use as columns in Phase 1 classification table |

**Aspirational: 9/9 | Score: 100.0**

---

#### V-05 — All Three Axes (Ceiling Test)

| C# | Result | Evidence |
|----|--------|---------|
| C-09 | PASS | Tier 2/3 Critical column present |
| C-10 | PASS | "Name the specific skill that turns this mock into real signal. DO NOT write 'gather more signals.' Example: `/listen:adoption {topic}` not 'run a listen skill.'" — most explicit next-step specification across all variations |
| C-11 | PASS | "The classification table — including vocabulary rule columns — must be complete before any artifact body is written" |
| C-12 | PASS | `#### HANDOFF` dedicated section; "DO NOT write the literal placeholder string `{this-file}`. DO NOT write any other content in this section." |
| C-13 | PASS | REAL-REQUIRED rationale in Phase 1; extended in Phase 2: "DO NOT use specification language in any EVIDENCE-HEAVY artifact body — this violates the DO NOT use rule for that category" |
| C-14 | PASS | Stop-gate sentences at all three phase boundaries |
| C-15 | PASS | Vocabulary columns in table + full vocabulary compliance block in Phase 2 with per-category DO NOT use reminders — highest density prohibition coverage |
| C-16 | PASS | Five-field enumerated gate identical to V-04 |
| C-17 | PASS | MUST use / DO NOT use as table columns; most verbose cell content including quoted example phrases |

**Aspirational: 9/9 | Score: 100.0**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Score | Rank |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 output-format | 60/60 | 30/30 | 9/9 → 10.0 | **100.0** | T-1 |
| V-02 lifecycle-emphasis | 60/60 | 30/30 | 9/9 → 10.0 | **100.0** | T-1 |
| V-03 inertia-framing | 60/60 | 30/30 | 8/9 → 8.9 | **98.9** | 5 |
| V-04 output+lifecycle | 60/60 | 30/30 | 9/9 → 10.0 | **100.0** | T-1 |
| V-05 all three axes | 60/60 | 30/30 | 9/9 → 10.0 | **100.0** | T-1 |

**Discriminator confirmed:** C-17 is the sole discriminator. V-03 is the only variation that fails it — vocabulary rules in a prose block below the table rather than as table columns. All four other variations close C-16 and C-17 via instruction-based enforcement, confirming V-05's STEP vs PHASE finding: label style does not affect compliance.

**R4 finding confirmed:** STEP labeling (V-02) achieves identical compliance to PHASE labeling (V-01/V-04/V-05) — gate sentence presence matters; label register does not.

---

### Excellence Signals from Top-Scoring Variations

Patterns in V-01/V-02/V-04/V-05 that V-03 lacks — and that lift output quality beyond rubric floor:

1. **Vocabulary cell pre-population with quoted example phrases** — all four ceiling variations fill the MUST use cells with concrete example phrases (e.g., `"N of M tests showed..."`, `"Prototype against {topic} produced..."`). The model can directly pattern-match against these phrases rather than interpreting an abstract category label. V-17 requires column co-location; it does not require that cells contain pre-filled examples vs empty fill targets. The quoted phrase anchors are visible in V-01/V-02/V-04/V-05 but not captured by any current criterion.

2. **Bidirectional vocabulary reinforcement** — V-02's Phase 2 adds "DO NOT use specification language in any EVIDENCE-HEAVY artifact body" as a generation-step reminder that echoes the table column. V-05 adds a full `Vocabulary compliance:` block in Phase 2 re-stating DO NOT rules by category. Table-level co-location (C-17) establishes the rule; generation-level repetition closes the recall gap between classification and body writing. No current criterion requires this dual-layer enforcement — C-15 only requires DO NOT prohibition clauses exist (once, anywhere), not that they appear at both classification and generation points.

---

### New Patterns for v5 Rubric

**C-18 candidate — Vocabulary cell example anchoring:** MUST use and DO NOT use cells contain at least one quoted example phrase per category (e.g., `"N of M tests showed..."` for EVIDENCE-HEAVY, `"state transitions, trigger conditions, data flow contracts"` for HIGH-STRUCTURE) rather than abstract category labels alone. Pre-filled examples eliminate interpretation ambiguity at generation time; column headers naming the rule ("MUST use: study language") require the model to self-select appropriate vocabulary without a reference form.

**C-19 candidate — Generation-phase vocabulary echo:** Phase 2 (or STEP 2) generation instructions repeat DO NOT use prohibitions per category as a standalone compliance block, distinct from the Phase 1 table. The echo ensures vocabulary rules are active at the moment of artifact body generation, not only at classification — closing the recall gap between a pre-classified table and an extended generation phase.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Vocabulary cell example anchoring — MUST/DO NOT cells contain pre-filled quoted example phrases (not abstract category labels), giving the model direct pattern-match references at generation time", "Generation-phase vocabulary echo — Phase 2 generation instructions repeat DO NOT use prohibitions per category as a standalone compliance block, active at body-writing time distinct from the Phase 1 classification table"]}
```
