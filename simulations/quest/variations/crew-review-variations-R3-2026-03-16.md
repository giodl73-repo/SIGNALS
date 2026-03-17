Written to `simulations/quest/golden/crew-review-variate-R3-2026-03-16.md`.

---

# crew-review -- Variate R3

5 complete variations. Single-axis: V-01, V-02, V-03. Combination: V-04, V-05.

---

## V-01 -- Inertia framing

**Axis**: Inertia framing
**Hypothesis**: Declaring the challenger pass as a named, self-contained execution phase -- with a 4-slot null hypothesis form where each empty slot auto-escalates to a HIGH finding -- makes C-09 correct-by-construction (challenger leads because the domain phase cannot interrupt the challenger bracket) and C-16 correct-by-construction (template enforced by per-slot escalation, not by completeness instruction).

**Key structural moves:**
- `CHALLENGER PHASE` and `DOMAIN PHASE` as labeled section headers (C-15)
- 4-slot form: SLOT-A through SLOT-D with names (C-11)
- Per-slot escalation: `[not stated in artifact]` + logged HIGH finding per unfilled slot (C-16)
- Three-level ERROR halt: absent / empty / malformed fields (C-14)
- Standard 4-column matrix

**Aspirational targets**: C-14 PASS, C-15 PASS, C-16 PASS, C-11 PASS. Weak on C-12 (no lens column), C-13 (no typed schema).

---

## V-02 -- Output format

**Axis**: Output format
**Hypothesis**: A 5-column typed schema -- with Lens as a required column, explicit per-column type contracts, and a named per-row validation gate -- makes C-12 and C-13 correct-by-construction. A missing lens entry is a visible column gap. A non-conforming severity value cannot pass the gate.

**Key structural moves:**
- 5-column schema table with `Column | Type | Constraint` header (C-13)
- Lens column with typed constraint and anti-pattern ("no generic restatements") (C-12)
- Per-row validation gate: named checklist before any row is written (C-13)
- Challenger included via "include any role with `archetype: challenger`" exception clause -- single flat selection step (not a named phase -- C-15 FAIL by design)
- Three-level ERROR halt (C-14)

**Aspirational targets**: C-12 PASS, C-13 PASS, C-14 PASS. Weak on C-15 (exception clause, not phase), C-16 (challenger finding requirement is prose, not slot form).

**Differentiator from R2 V-01**: R2 V-01 had a schema but no explicit named validation pass. V-02 adds "Per-row validation gate" as a visible named step, targeting the C-13 PARTIAL -> PASS gap.

---

## V-03 -- Phrasing register

**Axis**: Phrasing register
**Hypothesis**: A conversational, directive voice can carry the full aspirational structure without schema tables or formal phase headers. Tests whether register is independent of structural quality, or whether formal declarations do structural work that instruction proximity cannot replicate.

**Key structural moves:**
- Short declarative sentences, "go do X," imperative throughout
- `Challenger Phase -- runs before anything else` + `Domain Phase starts now` as labeled sections (C-15 attempt in conversational voice)
- 4-slot form written as a markdown blockquote with blanks (C-11 attempt)
- Per-slot escalation: "Can't fill a blank? That's their HIGH finding." (C-16 attempt)
- Lens-lock as step 1 per domain reviewer ("Lock the lens. One sentence...") (C-12 attempt)
- Three-level stop conditions in conversational language (C-14 attempt)

**Aspirational targets**: All six attempted. Hypothesis is that the conversational register weakens C-13 (no schema table), but the rest may survive. If register-driven degradation shows up in scoring, the formal apparatus in V-01/V-02 is earning its weight.

---

## V-04 -- Inertia framing + Lifecycle emphasis

**Axis combination**: Inertia framing + Lifecycle emphasis
**Hypothesis**: Embedding the challenger bracket as a hard phase gate -- where DOMAIN cannot begin until CHALLENGER has exited, and where the CHALLENGER exit condition depends on slot completion -- produces the strongest possible guarantee for C-09/C-15 (challenger leads because it's a lifecycle gate) and C-11/C-16 (template enforced because the phase cannot exit with a silent slot). Combines V-01's inertia framing with V-05 R1's four-phase lifecycle.

**Key structural moves:**
- Four named phases: LOAD, CHALLENGER BRACKET, DOMAIN REVIEW, RENDER (C-15)
- CHALLENGER BRACKET exit condition: "every slot is either filled or escalated" (C-16 via lifecycle gate, strongest guarantee)
- `Domain review does not begin until PHASE 2 exits.` -- explicit gate statement
- Slot form in PHASE 2 with `C3` steps naming the escalation rule per slot (C-16)
- Lens declaration as `D2 step 1` in DOMAIN REVIEW phase (C-12)
- Three-level halt in LOAD (C-14)
- 4-column matrix (C-13 not targeted)

**Aspirational targets**: C-11 PASS, C-12 PASS, C-14 PASS, C-15 PASS, C-16 PASS. Weak on C-13 (no typed schema, no named per-row validation).

**R3 note**: The exit condition design is new -- prior variations used instruction proximity for slot completion. Making the CHALLENGER PHASE unclosable with silent slots is a stronger enforcement than any instruction inside the phase.

---

## V-05 -- Output format + Role sequence

**Axis combination**: Output format + Role sequence
**Hypothesis**: Combining archetype-derived execution order with a 5-column typed schema and embedding the challenger bracket as Group 1 (a named execution block in the sequence, not an exception clause) targets all six aspirational criteria in a single coherent design.

**Key structural moves:**
- Archetype group table: Group 1 = challenger, Groups 2-5 = domain archetypes (C-15 via group sequence structure)
- 5-column schema: Role, Lens, Findings, Severity, Recommendation with typed constraints (C-12, C-13)
- Per-row validation gate: "before writing any row, verify all five cells" (C-13)
- Three-level ERROR halt (C-14)
- Null hypothesis slot form in Group 1 bracket with per-slot escalation (C-11, C-16)
- `Group 1 closes here. Group 2 begins next.` -- explicit group boundary (C-15)
- Lens escalation for unfilled slots produces a separate logged HIGH finding row (C-16, strongest form)

**Aspirational targets**: All six (C-11, C-12, C-13, C-14, C-15, C-16). This is the broadest attempt. Risk: six aspirational targets in one prompt may produce diluted execution vs. a narrower design that fully enforces two or three.

**Differentiator from R1 V-04**: R1 V-04 used archetype groups but had a flat 4-column matrix, no lens column, and no slot form. V-05 layers all R2 excellence patterns onto that backbone.

---

## Design space summary

| Variation | Primary axes | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | New mechanism |
|-----------|-------------|------|------|------|------|------|------|---------------|
| V-01 | Inertia framing | target | -- | -- | target | target | target | Phase bracket as labeled header sections |
| V-02 | Output format | -- | target | target | target | -- | -- | Named per-row validation gate |
| V-03 | Phrasing register | attempt | attempt | -- | attempt | attempt | attempt | Register as structural stress-test |
| V-04 | Inertia + Lifecycle | target | target | -- | target | target | target | Phase exit condition dependent on slot completion |
| V-05 | Format + Sequence | target | target | target | target | target | target | Archetype groups as C-15 vehicle; Lens in schema |
