Here is the complete updated rubric:

---

**New criterion extracted from Round 3:**

| ID | Criterion | Source pattern |
|----|-----------|----------------|
| C-15 | Anti-Pattern Watch uses schema-enforced CAT-N citation prefix | C-09 is PARTIAL in every variant — "no schema contract covers Anti-Pattern Watch columns; typed-citation syntax depends on prose discipline" |

**Design logic:**
C-15 is the structural-mechanism parallel for C-09, using the same principle applied in C-13 and C-14:

| Criterion pair | What the mechanism does |
|----------------|------------------------|
| C-12 + C-13 | Role coherence enforced by ROLE-NAME LOCK (named enumeration, not prose rule) |
| C-11 + C-14 | Rebuttal role-grounding enforced by four-field form (syntax forces field order) |
| C-09 + C-15 | Cat-N citation enforced by CAT-N-CITATION-SCHEMA block (named contract before table) |

The pattern is consistent: every prose-discipline requirement that generates PARTIALs gets a structural mechanism that makes compliance checkable without rereading upstream sections.

**Scoring weight update:** Aspirational tier expands from 6 → 7 criteria; per-criterion weight drops from 1.67 → 1.43 pts. PARTIAL = 0.71 pts. Formula unchanged — a full aspirational sweep still earns 10 pts.
contains an ASCII box/tree diagram showing at minimum two levels of hierarchy. Committees appear as distinct labeled nodes — not embedded inside an area box. No flat list of names without parent-child connectors. Role names in diagram must match those in ROLES-LOADED or ROLES-NOTE. |
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

---

## Scoring Weights Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 (5 criteria) | 60 pts total (12 per criterion) |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts total (10 per criterion) |
| Aspirational | C-09 through C-15 (7 criteria) | 10 pts total (1.43 per criterion) |

Aspirational scoring: PASS = 1.43 pts | PARTIAL = 0.71 pts | FAIL = 0

---

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — C-01 through C-10 |
| v2 | Round 1 excellence signals — added C-11 (role-grounded Rebuttal) and C-12 (role-name coherence); aspirational tier expanded to 4 criteria at 2.5 pts each |
| v3 | Round 2 excellence signals — added C-13 (ROLE-NAME LOCK block) and C-14 (mandatory Rebuttal case form); aspirational tier expanded to 6 criteria at 1.67 pts each |
| v4 | Round 3 excellence signals — added C-15 (CAT-N-CITATION-SCHEMA block for Anti-Pattern Watch); aspirational tier expanded to 7 criteria at 1.43 pts each |

---

## Quick Reference: Common Failure Modes

- **C-01 fail**: Roles block present but ROLE-TYPE-CLASSIFICATION missing or has unlisted roles.
- **C-03 fail**: Single `Decision Scope` column used instead of separate `Decides` + `Escalates`.
- **C-04 fail**: Rhythm table has only ROB, or two meetings merged into one row.
- **C-05 fail**: Quorum field uses short form `N roles required` instead of fraction `N of M`.
- **C-06 fail**: Inertia Assessment present but FLAT-CASE-PRESSURE line missing from VERDICT sub-section.
- **C-08 fail**: Sections written in correct order but phase gate lines absent from output.
- **C-11 fail**: Rebuttal describes future growth risk ("as we scale...") rather than a current observable failure tied to a named role.
- **C-12 fail**: Rhythm table DRI/Owner or charter Membership lists a role not found in ROLES-LOADED.
- **C-13 fail**: No ROLE-NAME LOCK block present, or block appears after the first phase gate rather than immediately after classification.
- **C-14 fail**: Rebuttal written as free prose without labeled fields, or ROLE UNDER PRESSURE field absent or names a role not in ROLES-LOADED.
- **C-15 fail**: No CAT-N-CITATION-SCHEMA block before the Anti-Pattern Watch table, or schema block present but does not enumerate valid cat-N codes from the ORG-ELEMENT REGISTER.
