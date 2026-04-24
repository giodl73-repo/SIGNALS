## flow-throttle Scoring — Round 9 (v9 Rubric)

**Date:** 2026-03-16
**Rubric:** v9 | **Criteria:** C-01–C-26 | **Max composite:** 180
**Baseline:** R8 V-05 confirmed passes C-01–C-24 under v9

---

## Scoring Method

All five variations build on the R8 V-05 baseline. C-01–C-24 carry forward; the open question for each variation is whether it satisfies C-25 and C-26. I evaluate C-01–C-24 as a block, then score C-25 and C-26 individually per variation.

---

## C-01 through C-24 — Baseline Carry

All five variations inherit the full R8 V-05 structure: phase pipeline (C-15), prohibition statements (C-16), enumeration anchor (C-17), inertia annotations (C-18), dedicated coverage step (C-19), prose-restriction declaration (C-20), cross-artifact referential integrity (C-21), typed-row taxonomy (C-22), inline prose-exception citations (C-23), and TYPE SCAN GATE (C-24). No variation removes or weakens any inherited element. All five: **PASS** on C-01–C-24.

---

## Variation-by-Variation Scoring

### V-01 — Inertia Framing

**C-25:** Named "STRUCTURED OUTPUT EXEMPTION CLASS — prevents false-positive C-23 tagging (C-25):" appears immediately after the prose-permitted list. Enumerates four element types as bullet list (gate decision lines, cross-artifact header lines, phase boundary prohibition lines, per-criterion verdict lines). Includes escape-route framing: "the temptation is to treat gate decision lines as prose because they appear in narrative positions." Named exemption clause, all element types present, escape route demolished at the enforcement point. **PASS**

**C-26:** "Purpose — prevents category elision above C-22 (C-26):" label at the gate. Satisfies all three C-26 requirements: (1) references C-22 explicitly ("C-22 ensures the Type column is present and all three categories appear in the finished TABLE E"), (2) names the failure mode ("Without this gate, a missing category is detectable only after the mitigation table is complete"), (3) explains the gap above C-22 ("This gate ensures type completeness is an explicit named structural check, not an implicit property verifiable only by reading TABLE E in full"). Escape-route framing closes the "gate appears redundant" reasoning at the point of execution. **PASS**

| Band | Criteria | Score |
|------|----------|-------|
| Essential | C-01–C-05 | 60/60 |
| Recommended | C-06–C-08 | 30/30 |
| Aspirational C-09–C-24 | 16 × 5 | 80/80 |
| C-25 | PASS | 5/5 |
| C-26 | PASS | 5/5 |
| **Total** | | **180/180** |

---

### V-02 — Phrasing Register

**C-25:** Exemption class is embedded in explanatory prose within the FORMAT CONTRACT rather than as a named clause. The content is present: "gate decision lines, cross-artifact header lines, phase boundary prohibition lines, and per-criterion verdict lines are structured output — their type is determinable before their content is read." The explanation also provides the rationale ("if the boundary between prose and structured output is left to content inspection, an executor tagging output must interpret each element"). C-25 pass condition requires "the prose-restriction declaration names at least one structured-output type as explicitly exempt from C-23 tagging" — V-02 names all four. No discrete named-clause label, but the pass condition is met. **PASS** *(weakest C-25 implementation across the five variations — content satisfies the pass condition but lacks a structural label that would make the exemption class independently locatable)*

**C-26:** Gate uses equivalent label "Here is why this gate step is necessary even though C-22 already requires the Type column and per-type minimums" — this satisfies the rubric's "or equivalent label" provision. Satisfies all three C-26 requirements: (1) references C-22 by name, (2) describes the failure mode through the cascade narrative ("an executor who builds TABLE F and then discovers a missing Cascade row has produced a mitigation table with no Cascade mitigations"), (3) explains the gap ("C-22 ensures that the finished output has the correct type structure. This gate ensures that type completeness is verified during construction"). **PASS**

| Band | Criteria | Score |
|------|----------|-------|
| Essential | C-01–C-05 | 60/60 |
| Recommended | C-06–C-08 | 30/30 |
| Aspirational C-09–C-24 | 16 × 5 | 80/80 |
| C-25 | PASS | 5/5 |
| C-26 | PASS | 5/5 |
| **Total** | | **180/180** |

---

### V-03 — Lifecycle Emphasis

**C-25:** "**Section B — STRUCTURED OUTPUT REGISTER (C-25)**" appears at the same heading level as Section A (prose-permitted contexts). Implemented as a formal three-column table with Element type / Form / Exempt from C-23? columns. All four element types present as table rows. Closing declaration: "No other element types are added to this register without revising this contract" — closes the register. This is the strongest standalone C-25 form: structural symmetry with Section A signals equal importance; tabular form makes each element type independently verifiable by row scan. **PASS**

**C-26:** "**Annotation block (C-26):**" with three explicitly labeled fields (Field 1 — Failure mode prevented / Field 2 — Gap above C-22 / Field 3 — Audit test). Field 1: "Category elision — a type category is absent from TABLE E, but this is detectable only by reading the full table after the fact." Field 2: "C-22 ensures the Type column is present and all three categories appear in the *finished* output. This gate ensures type completeness is an explicit named structural check *before construction of TABLE F begins*." Field 3 provides the audit verification method. All three C-26 requirements met with independent labeled fields. **PASS**

| Band | Criteria | Score |
|------|----------|-------|
| Essential | C-01–C-05 | 60/60 |
| Recommended | C-06–C-08 | 30/30 |
| Aspirational C-09–C-24 | 16 × 5 | 80/80 |
| C-25 | PASS | 5/5 |
| C-26 | PASS | 5/5 |
| **Total** | | **180/180** |

---

### V-04 — Role Sequence + Inertia Framing

**C-25:** Format Analyst role produces the PROSE-RESTRICTION DECLARATION as a required role output. The declaration includes both prose-permitted contexts and the structured-output exemption class as a bulleted list. The Format Analyst instruction explicitly requires: "Structured-output exemption class (enumerate all types that are NOT prose and therefore exempt from C-23 inline citation requirements):" — four element types listed. "Escape route note for Format Analyst (C-25)" explains why the complement-set reasoning is insufficient. The role-assignment mechanism transforms the exemption class from an annotation into a precondition: the Domain Expert cannot activate until the Format Analyst produces it. **PASS**

**C-26:** "Purpose — prevents category elision above C-22 (C-26):" with the without-gate / with-gate narrative distinguishing construction-time vs. post-completion detection. References C-22 by name. Names failure mode through the cascade scenario ("an executor completes TABLE F (all TABLE E rows have mitigation entries), then a post-hoc scan detects the missing Cascade row in TABLE E — at that point TABLE F also has no Cascade mitigations"). Explains the gap: "C-22 requires the Type column and per-type minimum rows. This gate checks type completeness before TABLE F opens." "Escape route for C-26 — 'C-22 makes this gate redundant'" section demolishes the specific reasoning chain. All three C-26 requirements met. **PASS**

| Band | Criteria | Score |
|------|----------|-------|
| Essential | C-01–C-05 | 60/60 |
| Recommended | C-06–C-08 | 30/30 |
| Aspirational C-09–C-24 | 16 × 5 | 80/80 |
| C-25 | PASS | 5/5 |
| C-26 | PASS | 5/5 |
| **Total** | | **180/180** |

---

### V-05 — All Three Axes

**C-25:** Format Analyst produces "**Section B — STRUCTURED OUTPUT REGISTER (C-25)**" as a role output, parallel to Section A. Four-column table: Element type / Canonical form / Prose? / C-23 tag required? All four element types present with explicit No/No in the last two columns. Escape-route framing: "The temptation is to omit this register on the grounds that structured output is the complement of the prose-permitted list... This reasoning requires content inspection to classify boundary elements." The four-column table is the strongest implementation: "Prose? = No" and "C-23 tag required? = No" make the compliance test visible by column scan without any content interpretation. Role-locked production makes it a structural precondition. **PASS** *(strongest C-25 implementation)*

**C-26:** "**Purpose annotation (C-26) — three fields:**" with explicitly labeled sub-bullets:
- **Failure mode prevented:** "Category elision — a risk type is absent from TABLE E, making the entire risk category unmitigated, but the absence is detectable only by a full table scan after TABLE F is complete."
- **Gap above C-22:** "C-22 is a finished-output structural requirement; this gate is a construction-time blocking check. An executor who reasons 'C-22 already requires all three types — the gate adds no substance' is confusing a structural requirement with a construction-time enforcement mechanism."
- **Audit test:** Dual-path verification instructions (gate present vs. gate absent audit method).

Additional "Escape route for C-26" paragraph explicitly demolishes the C-22-redundancy reasoning chain: "C-22 tells the executor what the finished output must contain. The gate tells the executor *when* to verify it." Three-field structure ensures all three C-26 sub-requirements are independently auditable. **PASS** *(strongest C-26 implementation)*

| Band | Criteria | Score |
|------|----------|-------|
| Essential | C-01–C-05 | 60/60 |
| Recommended | C-06–C-08 | 30/30 |
| Aspirational C-09–C-24 | 16 × 5 | 80/80 |
| C-25 | PASS | 5/5 |
| C-26 | PASS | 5/5 |
| **Total** | | **180/180** |

---

## Rankings

| Rank | Variation | Score | C-25 quality | C-26 quality |
|------|-----------|-------|-------------|-------------|
| 1 | V-05 | 180/180 | 4-column table, role output, escape route | 3-field labeled block, dual escape route, audit test |
| 2 | V-03 | 180/180 | Named sub-section with table, closed register | 3-field labeled block |
| 3 | V-04 | 180/180 | Role output as precondition, named exemption class | Purpose label + without/with narrative + escape route |
| 4 | V-01 | 180/180 | Named clause + escape route | Purpose label + escape route |
| 5 | V-02 | 180/180 | Embedded prose (no named clause) | Equivalent label, explanatory form |

All five clear the golden threshold: all essential PASS, composite >= 80.

---

## Excellence Signals from V-05

**ES-1 — Structural symmetry as completeness signal.** Elevating the C-25 exemption class to a Section B at the same heading level as Section A (prose-permitted list) creates a symmetry that signals equal importance and invites equal completeness. An asymmetric nesting (Section A named, Section B embedded in prose) produces asymmetric attention during execution. Symmetry at the structural level communicates the two sections are a pair, not a list with an appendix.

**ES-2 — Per-field labeled annotation for multi-requirement criteria.** When a criterion has three independently auditable sub-requirements (C-26: reference C-22, name failure mode, explain gap above C-22), the V-05 pattern elevates to three explicitly labeled fields. Each field is independently incomplete-detectable: an executor cannot satisfy "Failure mode prevented" while omitting "Gap above C-22" without producing an obvious blank field. This is the C-18 inertia-framing pattern applied at sub-criterion granularity rather than criterion granularity.

**ES-3 — Classification column as compliance surface.** V-05's four-column STRUCTURED OUTPUT REGISTER table includes dedicated "Prose?" and "C-23 tag required?" columns with explicit No/No values. This makes the compliance test for each element type visible by column scan without content interpretation — an auditor can verify C-25 compliance by confirming the two rightmost columns contain No/No for each listed element type. Earlier variations name the element types but leave the compliance implication implicit.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Per-field labeled annotation for multi-requirement criteria: when a criterion has 3 sub-requirements, elevate to explicitly labeled fields (Field 1/2/3) so each is independently incomplete-detectable rather than satisfiable by a single sentence that addresses one sub-requirement implicitly", "Structural symmetry as completeness signal: elevating the exemption class to the same heading level as the prose-permitted list (Section A / Section B) signals equal importance and invites equal completeness, preventing asymmetric attention during execution"]}
```
