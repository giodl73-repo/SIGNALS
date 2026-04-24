```markdown
# org-chart Rubric — v6

## Essential Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | ROLE-TYPE-CLASSIFICATION with all four domain types | correctness | Output contains a ROLE-TYPE-CLASSIFICATION block listing every role from ROLES-LOADED, each annotated with exactly one domain type from the closed vocabulary: (strategic), (operational), (advisory), (governance). No role is missing. No unlisted domain type is introduced. |
| C-02 | ASCII diagram with hierarchy and committees as distinct nodes | correctness | Output contains an ASCII box/tree diagram showing at minimum two levels of hierarchy. Committees appear as distinct labeled nodes — not embedded inside an area box. No flat list of names without parent-child connectors. Role names in diagram must match those in ROLES-LOADED or ROLES-NOTE. |
| C-03 | Headcount table with Decides and Escalates columns | correctness | Output contains a headcount table with columns `Area`, `Headcount`, `Key Roles`, `Decides`, and `Escalates` — five columns, not four. `Decides` and `Escalates` are separate columns (no merged `Decision Scope`). Table includes at minimum two area rows plus a `**Total**` row with the sum. Key Roles cells annotated as `[role name] ([domain type])`. |
| C-04 | Operating rhythm table with minimum three distinct rows | coverage | Output contains an operating rhythm table with columns `Cadence`, `Frequency`, `DRI / Owner`, `Purpose`. Table contains at minimum three rows covering at minimum: (a) ROB, (b) a shiproom or gate meeting, and (c) a governance meeting. Two meetings must not be merged into one row. |
| C-05 | Committee charters with all five required fields | correctness | For every governance meeting in the rhythm table, a charter is written with all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`. Quorum field uses the fraction format `Quorum: [N] of [M] member roles required for binding decisions`. Membership lists at minimum two roles annotated as `[role name] ([domain type])`. Escalates names a destination — not `everything not listed under Decides`. |

---

## Recommended Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia assessment with verdict and pressure rating | depth | Output contains an Inertia Assessment with all four sub-sections in order: (1) Case for Staying Flat with a mechanism table (>=2 rows, Type values from closed vocabulary), (2) How We Coordinate Today, (3) Rebuttal naming a specific observable failure mode, (4) VERDICT opening with `FLAT-CASE-PRESSURE: [rating] — [justification]` where rating is from the closed set (Strong / Moderate / Weak / Negligible / Insufficient). Verdict declares exactly one of `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Re-assessment trigger names a concrete threshold (not "revisit as the team grows"). |
| C-07 | ORG-ELEMENT REGISTER with all four categories | coverage | Output contains an `ORG-ELEMENT REGISTER` block after the charters phase gate with all four categories populated: `cat-1 (Areas)` with headcount per area, `cat-2 (Committees/Cadences)`, `cat-3 (Headcount)` with total, `cat-4 (DRI Roles)`. No category may be empty or missing. |
| C-08 | Section order with all phase gates present | behavior | Output contains all four phase gate lines in correct sequence: (1) `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`, (2) `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`, (3) `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`, (4) `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`. No section appears before its gate. |

---

## Aspirational Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Anti-Pattern Watch with typed cat-N citations | depth | Output contains an Anti-Pattern Watch section after the Org Evolution Roadmap with columns `Anti-Pattern`, `Why It Applies Here`, `Mitigation`. Contains at minimum two rows. Every `Why It Applies Here` cell opens with `[element name] (cat-N) —` using a valid cat-N code from the ORG-ELEMENT REGISTER. No cell names an org element without the typed citation syntax. |
| C-10 | Org Evolution Roadmap with two distinct trigger categories | depth | Output contains an Org Evolution Roadmap trigger table with columns `Trigger`, `Structural Change`, `Type`. Contains at minimum two rows where Row 1 is a headcount threshold trigger and Row 2 comes from a different category (workload signal, structural symptom, or milestone event). Two headcount thresholds do not satisfy this criterion. |
| C-11 | Inertia Rebuttal is role-grounded with concrete re-assessment trigger | depth | The Rebuttal sub-section of the Inertia Assessment names at least one specific role from ROLES-LOADED as the coordination failure point. The failure described is an observable breakdown (e.g., "the [role] has no escalation path for cross-area dependency disputes") — not a growth projection ("as we scale, coordination will become harder"). The re-assessment trigger in the VERDICT names a concrete measurable threshold: a specific hire count, a named milestone event, or a structural symptom (e.g., "two or more missed ship dates attributable to cross-area misalignment") rather than a generic signal. |
| C-12 | Role-name coherence across all document sections | correctness | Every named role reference throughout the document — ASCII diagram, rhythm table DRI/Owner column, committee charter Membership and Decides fields, and Inertia Assessment sub-sections — matches a role listed in ROLES-LOADED or ROLES-NOTE. No new role names are introduced in any section after the roles block. This extends C-02 (diagram-only) to the full document. |
| C-13 | ROLE-NAME LOCK block emitted after classification | behavior | Output contains a visible `ROLE-NAME LOCK` block immediately after the ROLE-TYPE-CLASSIFICATION that explicitly enumerates every role from ROLES-LOADED as the complete set of permitted references for the remainder of the document. The block appears before the first phase gate. Its presence converts role-coherence from a prose-governed expectation into a mechanical per-section check: downstream sections (diagram, rhythm table DRI/Owner, charter Membership/Decides, Inertia sub-sections) can be verified against a single named list without rereading the roles block. |
| C-14 | Inertia Rebuttal uses mandatory four-field case form | depth | The Rebuttal sub-section of the Inertia Assessment is structured as a four-field form with explicit field labels in this order: `ROLE UNDER PRESSURE`, `OBSERVABLE BREAKDOWN`, `WHY EXISTING MECHANISMS FAIL`, `RE-ASSESSMENT TRIGGER`. Each field is present and populated. The `ROLE UNDER PRESSURE` field names exactly one role from ROLES-LOADED. The `OBSERVABLE BREAKDOWN` field describes a current coordination failure — not a future growth risk ("as we scale..." does not satisfy this field). This form structure makes role selection a syntactic precondition before the breakdown prose can begin, eliminating the compliance gap that exists when role-grounding is requested only via prose instruction. |
| C-15 | Anti-Pattern Watch uses schema-enforced CAT-N citation prefix | behavior | The Anti-Pattern Watch section is introduced with a `CAT-N-CITATION-SCHEMA` block (or equivalent column header template) that explicitly enumerates the valid cat-N codes drawn from the ORG-ELEMENT REGISTER and states the mandatory `[element name] (cat-N) —` prefix format for `Why It Applies Here` cells. The schema block appears immediately before the Anti-Pattern Watch table. Its presence converts the typed-citation requirement from a prose expectation into a mechanical per-cell check — each cell can be verified against the schema without rereading the register. This is the structural-mechanism parallel to C-09, using the same principle as C-13 (ROLE-NAME LOCK for role coherence) and C-14 (four-field form for Rebuttal role-grounding): a named contract that makes compliance syntactically checkable rather than prose-discipline-dependent. |
| C-16 | Org Evolution Roadmap uses TRIGGER-TYPE VOCABULARY block to enforce category diversity | behavior | The Org Evolution Roadmap section is introduced with a `TRIGGER-TYPE VOCABULARY` block that explicitly enumerates the closed set of permitted Type values (headcount threshold / workload signal / structural symptom / milestone event) and states that no two consecutive rows may share the same Type value. The block appears immediately before the trigger table. Its presence converts the category-diversity requirement of C-10 from a prose expectation into a mechanical per-row check — each row's Type value can be verified against the vocabulary and the consecutive-type constraint can be verified without rereading the section. This is the structural-mechanism parallel to C-10, applying the same principle as C-13 (ROLE-NAME LOCK), C-15 (CAT-N-CITATION-SCHEMA): a named contract block makes compliance syntactically checkable. |
| C-17 | Anti-Pattern Watch section has a dedicated phase gate separating it from Org Evolution Roadmap | behavior | Output contains a fifth phase gate line: `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===` appearing after the Org Evolution Roadmap and before the Anti-Pattern Watch table. The gate's presence makes Anti-Pattern Watch a structurally required section: its absence is a visible omission at the phase-gate level rather than a silent skip of an optional addendum. This is the architectural precondition for C-09 and C-15 — a prompt that defines only four phase gates cannot reliably produce both Org Evolution Roadmap and Anti-Pattern Watch as separate required sections. |
| C-18 | Every structural requirement with a known evasion mode has a corresponding VERIFY block | behavior | For every `PRODUCE:` command that has a documented failure mode, a `VERIFY:` block appears immediately after the command naming the exact disqualifying output variant. The VERIFY block uses present-tense disqualification syntax ("`[specific output]` does not satisfy this step") rather than affirmative restatement of the pass condition. At minimum, VERIFY blocks must be present for: the headcount table (disqualifying a merged `Decision Scope` column), the Org Evolution Roadmap (disqualifying two headcount threshold rows), and the Inertia Rebuttal (disqualifying future-tense breakdowns beginning with "as we scale..."). This mechanism is distinct from vocabulary-lock blocks (which enforce what must appear): VERIFY blocks enforce what must *not* appear, closing known compliance gaps that named vocabularies alone cannot close. |
| C-19 | Inertia Mechanism table uses MECHANISM-TYPE VOCABULARY block to enforce type coherence | behavior | The Inertia Assessment sub-section 2a (Case for Staying Flat) is introduced with a `MECHANISM-TYPE VOCABULARY` block that explicitly enumerates the closed set of permitted Type values for the mechanism table (e.g., span-of-control / direct-comms / shared-context / single-DRI / low-coordination-cost) and states that no row may introduce a Type value outside this vocabulary. The block appears immediately before the mechanism table. Its presence converts the mechanism-type constraint from a prose-inlined expectation into a mechanical per-row check — each row's Type value can be verified against the vocabulary without rereading the section narrative. This is the third inner-table application of the vocabulary-lock principle (after C-13 for roles and C-16 for trigger types), extending named-enumeration enforcement into the Inertia sub-section and making the mechanism table type column structurally checkable in the same way as role references and trigger categories. |

---

## Design Logic

| Criterion pair | What the mechanism does |
|----------------|------------------------|
| C-12 + C-13 | Role coherence enforced by ROLE-NAME LOCK (named enumeration, not prose rule) |
| C-11 + C-14 | Rebuttal role-grounding enforced by four-field form (syntax forces field order) |
| C-09 + C-15 | Cat-N citation enforced by CAT-N-CITATION-SCHEMA block (named contract before table) |
| C-10 + C-16 | Trigger category diversity enforced by TRIGGER-TYPE VOCABULARY block (closed set before table) |
| C-09 + C-15 + C-17 | Anti-Pattern Watch presence enforced by dedicated phase gate (section cannot be silently omitted) |
| C-06 + C-19 | Mechanism table Type coherence enforced by MECHANISM-TYPE VOCABULARY block (third inner-table vocabulary-lock application) |
| C-03 + C-10 + C-14 + C-18 | Known evasion modes closed by VERIFY blocks (merged columns, duplicate trigger types, future-tense breakdowns) |

---

## Scoring Weights Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 (5 criteria) | 60 pts total (12 per criterion) |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts total (10 per criterion) |
| Aspirational | C-09 through C-19 (11 criteria) | 10 pts total (0.91 per criterion) |

PARTIAL = 0.45 pts. Formula unchanged — a full aspirational sweep still earns 10 pts.
```
