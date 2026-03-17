# Quest Score — corps-chart (Round 1)

*Rubric: v1 | Variations: R1 V-01 through V-05 | Scoring basis: prompt-quality predictive analysis*

---

## Scoring Methodology

These variations are skill body prompts, not live outputs. Scoring is predictive: for each criterion, I assess whether the prompt framing reliably elicits compliant model output. PARTIAL = requirement present but framing raises meaningful compliance risk; PASS = explicit, well-gated requirement; FAIL = missing or actively undermined.

---

## V-01 — Phrasing Register (Conversational)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Roles block + classification | **PASS** | Steps 1–2 clearly require both blocks; format examples given; consistency constraint ("every loaded role must be classified") explicit |
| C-02 | ASCII diagram with distinct committee nodes | **PASS** | "Committees should appear as distinct labeled nodes" — soft "should" but instruction unambiguous |
| C-03 | Separate Decides / Escalates columns | **PARTIAL** | "Decides and Escalates are separate columns — do not merge them" is present, but conversational register reduces the salience of this constraint; no strong DO NOT anchor |
| C-04 | Rhythm table ≥3 distinct rows | **PASS** | "Do not combine two meetings into one row, and do not produce a rhythm table with only ROB" — explicit even in soft register |
| C-05 | Quorum in fraction form (N of M) | **PARTIAL** | "Do not use the short form" is stated, but the surrounding conversational tone lowers emphasis on this precise format detail; known high-failure criterion |
| C-06 | Inertia Assessment — all 4 sub-sections + FLAT-CASE-PRESSURE + VERDICT | **PARTIAL** | All 4 sub-sections present and format of FLAT-CASE-PRESSURE line specified; but gate is "You should not write the verdict declaration until this line is present" — soft; no argumentative framing to drive Rebuttal specificity; risk of generic VERDICT |
| C-07 | ORG-ELEMENT REGISTER — all 4 categories | **PASS** | Step 8 lists all four categories explicitly with format per entry |
| C-08 | All 4 phase gate lines in sequence | **PASS** | "emit this exact line" with verbatim gate strings at all four checkpoints |
| C-09 | Anti-Pattern Watch with typed cat-N citations | **PASS** | Step 10 states syntax requirement: "[element name] (cat-N) — [one sentence]"; closed vocabulary reference |
| C-10 | Org Evolution Roadmap — 2 trigger categories | **PASS** | "Row 1 should be a headcount threshold trigger. Row 2 must come from a different category" — explicit |

**Essential**: C-01✓ C-02✓ C-03~ C-04✓ C-05~ → 12+12+6+12+6 = **48/60**
**Recommended**: C-06~ C-07✓ C-08✓ → 5+10+10 = **25/30**
**Aspirational**: C-09✓ C-10✓ → **10/10**

**V-01 Composite: 83**

---

## V-02 — Inertia Framing (Flat team wins by default)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Roles block + classification | **PASS** | Steps 1–2 retain all format and consistency constraints; "Every loaded role must be classified. No role may appear in classification that was absent from the loaded block." |
| C-02 | ASCII diagram with distinct committee nodes | **PASS** | "Committees as distinct labeled nodes, not embedded in area boxes." |
| C-03 | Separate Decides / Escalates columns | **PASS** | "DO NOT use a merged `Decision Scope` column. Decides and Escalates are separate." — strong imperative form |
| C-04 | Rhythm table ≥3 distinct rows | **PASS** | "Do not merge two meetings into one row. Reference a loaded role in DRI / Owner." — both constraints explicit |
| C-05 | Quorum in fraction form (N of M) | **PASS** | "The fraction format (N of M) is required. Short form `N roles required` is not accepted." — both positive assertion and rejection of failure mode |
| C-06 | Inertia Assessment — all 4 sub-sections + FLAT-CASE-PRESSURE + VERDICT | **PASS** | "The flat team has already won" framing forces argumentative Rebuttal work; "DO NOT emit the verdict declaration before this line is present" — hard gate; "It must be: A specific observable... Tied to the actual team composition... Not a growth projection" — three explicit specificity constraints on Rebuttal; concrete re-assessment threshold required |
| C-07 | ORG-ELEMENT REGISTER — all 4 categories | **PASS** | "No category may be empty or missing." |
| C-08 | All 4 phase gate lines in sequence | **PASS** | All 4 exact gate strings specified; DO NOT section ordering reinforced at multiple points |
| C-09 | Anti-Pattern Watch with typed cat-N citations | **PASS** | "Every `Why It Applies Here` cell opens with: [element name] (cat-N) — [one sentence]"; "No element cited without typed syntax." |
| C-10 | Org Evolution Roadmap — 2 trigger categories | **PASS** | "Row 1: headcount threshold trigger. Row 2: different category — workload signal, structural symptom, or milestone event. Two headcount thresholds do not satisfy this requirement." |

**Essential**: all PASS → **60/60**
**Recommended**: all PASS → **30/30**
**Aspirational**: all PASS → **10/10**

**V-02 Composite: 100**

---

## V-03 — Role Sequence (Roles cross-referenced into Inertia)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Roles block + classification | **PASS** | "After classification, note the loaded role names — you will use them explicitly in Steps 3a and 3c below." — adds forward-reference discipline to Step 2 |
| C-02 | ASCII diagram with distinct committee nodes | **PASS** | "No new role names introduced" — additional consistency constraint strengthens C-01/C-02 coherence |
| C-03 | Separate Decides / Escalates columns | **PASS** | "DO NOT merge Decides and Escalates into a single column." |
| C-04 | Rhythm table ≥3 distinct rows | **PASS** | Explicit three-type row requirement, no-merge rule |
| C-05 | Quorum in fraction form (N of M) | **PASS** | "DO NOT use the short form `N roles required`." + fraction format explicitly stated |
| C-06 | Inertia Assessment — all 4 sub-sections + FLAT-CASE-PRESSURE + VERDICT | **PARTIAL** | "ROLE-GROUNDED FAILURE REQUIRED" and "ROLE CROSS-REFERENCE REQUIRED" improve Rebuttal specificity; all 4 sub-sections present with exact FLAT-CASE-PRESSURE format and DO NOT gate; however, no "flat team wins by default" argumentative framing — risk that VERDICT reads as mechanical execution rather than argued ruling; slightly lower confidence than V-02 on VERDICT quality |
| C-07 | ORG-ELEMENT REGISTER — all 4 categories | **PASS** | "All four categories must be populated. Do not proceed to Org Evolution Roadmap until complete." |
| C-08 | All 4 phase gate lines in sequence | **PASS** | All 4 exact gate strings present |
| C-09 | Anti-Pattern Watch with typed cat-N citations | **PASS** | Syntax requirement explicit |
| C-10 | Org Evolution Roadmap — 2 trigger categories | **PASS** | Row 1/Row 2 type constraint explicit |

**Essential**: all PASS → **60/60**
**Recommended**: C-06~ C-07✓ C-08✓ → 5+10+10 = **25/30**
**Aspirational**: all PASS → **10/10**

**V-03 Composite: 95**

---

## V-04 — Combined: Conversational Register + Inertia-Led

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Roles block + classification | **PASS** | Both blocks required; "Every loaded role should appear in classification. No classification entry should reference a role that wasn't loaded." |
| C-02 | ASCII diagram with distinct committee nodes | **PASS** | "Committees get their own nodes — don't fold them into an area box." |
| C-03 | Separate Decides / Escalates columns | **PARTIAL** | "Keep Decides and Escalates as separate columns — don't merge them into a single 'Decision Scope' column." — present but soft "don't merge" vs DO NOT; conversational register reduces critical-constraint salience |
| C-04 | Rhythm table ≥3 distinct rows | **PASS** | "Two meetings shouldn't share a row, and the table shouldn't have only ROB." |
| C-05 | Quorum in fraction form (N of M) | **PASS** | "The full fraction format (N of M) is required. The short form `N roles required` isn't sufficient." — explicit assertion despite soft register |
| C-06 | Inertia Assessment — all 4 sub-sections + FLAT-CASE-PRESSURE + VERDICT | **PASS** | Inertia-first framing retained from V-02: "The flat team wins until proven otherwise"; "Be specific: what breaks and who gets stuck"; "If there's no real failure to name, say so" — argumentative pressure maintained; FLAT-CASE-PRESSURE format specified; soft gate "should come before" reduces DO NOT confidence slightly but framing context compensates |
| C-07 | ORG-ELEMENT REGISTER — all 4 categories | **PASS** | "All four categories need to be populated." |
| C-08 | All 4 phase gate lines in sequence | **PASS** | Exact gate strings specified with "emit:" at all four checkpoints |
| C-09 | Anti-Pattern Watch with typed cat-N citations | **PASS** | Syntax requirement stated |
| C-10 | Org Evolution Roadmap — 2 trigger categories | **PASS** | "Two headcount rows don't count." — explicit |

**Essential**: C-01✓ C-02✓ C-03~ C-04✓ C-05✓ → 12+12+6+12+12 = **54/60**
**Recommended**: all PASS → **30/30**
**Aspirational**: all PASS → **10/10**

**V-04 Composite: 94**

---

## V-05 — Combined: Format Contract + Inertia-Led + Role Cross-Reference

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Roles block + classification | **PASS** | "After classification, hold the loaded role names in mind — they are required in Steps 3a and 3c." — forward-reference discipline from V-03 |
| C-02 | ASCII diagram with distinct committee nodes | **PASS** | "Committees as distinct labeled nodes. Role names must match ROLES-LOADED or ROLES-NOTE — no new names." |
| C-03 | Separate Decides / Escalates columns | **PASS** | FORMAT CONTRACT TABLE B: "NOTE: Decides and Escalates are TWO separate columns. Never merge as 'Decision Scope'." — stated before any output begins AND repeated at Step 5 |
| C-04 | Rhythm table ≥3 distinct rows | **PASS** | FORMAT CONTRACT TABLE C: "Min rows: 3 distinct rows (ROB + shiproom/gate + governance meeting)" + "NOTE: Never combine two meetings into one row" — pre-anchored |
| C-05 | Quorum in fraction form (N of M) | **PASS** | FORMAT CONTRACT TABLE D: "Quorum format: Quorum: [N] of [M] member roles required for binding decisions" + "NOTE: Fraction format (N of M) required. Short form 'N roles required' is NOT accepted." — pre-anchored before any output; strongest protection of all variations |
| C-06 | Inertia Assessment — all 4 sub-sections + FLAT-CASE-PRESSURE + VERDICT | **PASS** | Inertia-first framing from V-02 + role-grounding from V-03: "ROLE-GROUNDED FAILURE: Name the coordination failure using specific role names from ROLES-LOADED" + "Structure must earn its place. The flat team wins by default." — dual reinforcement; hard DO NOT gate on VERDICT |
| C-07 | ORG-ELEMENT REGISTER — all 4 categories | **PASS** | "DO NOT proceed to Org Evolution Roadmap until all four categories are populated." — hard gate; all four categories listed |
| C-08 | All 4 phase gate lines in sequence | **PASS** | All 4 exact gate strings present; FORMAT CONTRACT creates upfront cognitive anchor that reinforces section ordering |
| C-09 | Anti-Pattern Watch with typed cat-N citations | **PASS** | FORMAT CONTRACT TABLE F: "(cat-N) must be a valid code from the ORG-ELEMENT REGISTER" — pre-anchored before output begins |
| C-10 | Org Evolution Roadmap — 2 trigger categories | **PASS** | FORMAT CONTRACT TABLE E: "Row 1 = headcount threshold, Row 2 = different category" — pre-anchored |

**Essential**: all PASS → **60/60**
**Recommended**: all PASS → **30/30**
**Aspirational**: all PASS → **10/10**

**V-05 Composite: 100**

---

## Composite Scores

| Variation | Essential (/60) | Recommended (/30) | Aspirational (/10) | **Total** |
|-----------|-----------------|--------------------|--------------------|-----------|
| V-01 | 48 | 25 | 10 | **83** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 25 | 10 | **95** |
| V-04 | 54 | 30 | 10 | **94** |
| V-05 | 60 | 30 | 10 | **100** |

**Ranking**: V-02 = V-05 (100) > V-03 (95) > V-04 (94) > V-01 (83)

V-05 is the recommended top variation: it matches V-02 on all criteria while providing format-failure insurance through the upfront contract. V-02 is an equally strong alternative when instruction density is a concern.

---

## Excellence Signals from V-05

**Signal 1 — Pre-output FORMAT CONTRACT**
Declaring all table schemas (with NOTEs on known failure modes) before any output begins eliminates format-failure risk at the point of maximum model attention. The model reads the contract before it has written anything, so the schema is active in working context when each table is produced. This directly targets the two highest-frequency essential failures: merged Decides/Escalates (C-03) and short-form Quorum (C-05).

**Signal 2 — Inertia-first argumentative framing**
"Structure must earn its place. The flat team wins by default" forces the Rebuttal to do real argumentative work rather than executing a template. When the flat team is presumptively winning, the model must name a specific failure to overcome that presumption — producing more specific observables and more defensible FLAT-CASE-PRESSURE justifications.

**Signal 3 — Role-grounded failure specificity**
Requiring specific loaded role names in the inertia Rebuttal prevents generic "as the team grows" failure modes. The model is constrained to identify which roles are involved in the coordination failure, which naturally produces a more credible VERDICT.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-output format contract declares all table schemas before first output token, targeting the two highest-frequency essential failures (merged Decides/Escalates and short-form Quorum) at the point of maximum model attention", "inertia-first argumentative framing positions flat coordination as the default winner, forcing the Rebuttal to overcome that presumption with a specific observable failure rather than executing a template"]}
```
