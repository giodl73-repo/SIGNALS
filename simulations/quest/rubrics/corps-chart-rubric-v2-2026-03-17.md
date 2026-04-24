Written to `simulations/quest/rubrics/corps-chart-rubric-v2-2026-03-17.md`.

---

**Two new aspirational criteria extracted from Round 1 excellence signals:**

**C-11 — Inertia Rebuttal is role-grounded with concrete re-assessment trigger**
Source: V-02 earns full C-06 PASS; V-01/V-03 get PARTIAL. The distinguishing factor isn't the four sub-sections (all three have them) — it's whether the Rebuttal argues from actual team composition vs. generic growth projection. The excellence signal: a named role from ROLES-LOADED appears as the failure point, and the re-assessment trigger is a measurable threshold (hire count, event, structural symptom), not "revisit as the team grows."

**C-12 — Role-name coherence across all document sections**
Source: V-03 adds forward-reference discipline ("you will use them explicitly in Steps 3a and 3c"). C-02 already enforces diagram consistency, but V-03 reveals that rhythm table DRI/Owner cells and Inertia sub-sections are independent failure surfaces. The excellence signal: no role name appears anywhere after the roles block that wasn't in ROLES-LOADED.

**Aspirational weight change:** 4 criteria now share the 10-pt aspirational tier (2.5 pts each). The formula is unchanged — `aspirational_pass / N_aspirational * 10`.
Output contains an ASCII box/tree diagram showing at minimum two levels of hierarchy. Committees appear as distinct labeled nodes — not embedded inside an area box. No flat list of names without parent-child connectors. Role names in diagram must match those in ROLES-LOADED or ROLES-NOTE. |
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

---

## Scoring Weights Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 (5 criteria) | 60 pts total (12 per criterion) |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts total (10 per criterion) |
| Aspirational | C-09 through C-12 (4 criteria) | 10 pts total (2.5 per criterion) |

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
