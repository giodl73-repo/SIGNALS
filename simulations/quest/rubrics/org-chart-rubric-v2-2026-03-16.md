Scanning the scorecard for excellence signals not yet captured in v1 criteria:

**V-02 (Table-Schema-First)**: Inline example rows in every schema block — not just field labels but a complete worked example row per table.

**V-04 (Count-and-Advance)**: Named verification checkpoints (MECHANISM-ROW-COUNT, CADENCE-ROW-COUNT, CHARTER-QUORUM-CHECK, HEADCOUNT-SUM, REGISTER-AREA-CHECK) that halt and verify a count before advancing. Four other variations lacked this.

**V-05 (Full Integration)**: Opens with explicit DEFAULT-POSITION declaration ("THE TEAM CAN OPERATE FLAT") before the mechanism table — burden-of-proof framing, not just inertia assessment.

**V-03 failure diagnosis**: C-01 went PARTIAL solely because of weak modal language ("should use" vs. "must use"). Every 100-scoring variation used "must"/"required"/"not acceptable" for all compliance rules. This is a distinct excellence signal: modal strength as a structural property.

Four new aspirational criteria → C-11 through C-14:

---

## Rubric: org-chart — v2

**10 essential/recommended criteria + 6 aspirational. Golden = all 5 essential pass + composite >= 80.**

### Essential (60 pts, 12 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Inertia Assessment complete — all 4 sub-sections, mechanism table >= 2 rows with closed-set Types, FLAT-CASE-PRESSURE rating from closed set, VERDICT with concrete re-assessment trigger, appears before any org diagram | behavior |
| C-02 | Roles block grounded in .craft/roles/ — ROLES-LOADED or ROLES-NOTE present; no role name introduced later that wasn't declared here | correctness |
| C-03 | ASCII org diagram with >= 2 hierarchy levels; committees as distinct nodes; all role names from roles block | format |
| C-04 | Operating rhythm table with >= 3 distinct rows: ROB + shiproom/gate + governance; no merged rows | coverage |
| C-05 | Committee charters with all 5 fields; Quorum in `N of M member roles` fraction form; Escalates names a destination; Membership >= 2 annotated roles | correctness |

### Recommended (30 pts, 10 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Headcount by area with split Decides/Escalates columns; >= 2 areas + Total row; Key Roles annotated with `(domain type)` | depth |
| C-07 | All 4 phase gate lines present in correct sequence; no section precedes its gate | format |
| C-08 | ROLE-TYPE-CLASSIFICATION block immediately after roles; all roles typed from closed set; three-tier order respected | correctness |

### Aspirational (30 pts, 5 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | ORG-ELEMENT REGISTER (cat-1 through cat-4) + Anti-Pattern Watch with `(cat-N)` typed citations; no uncited element | depth |
| C-10 | Org Evolution Roadmap >= 2 rows from distinct trigger categories (no two headcount thresholds) | depth |
| C-11 | Inline example rows — mechanism table, operating rhythm, committee charter, and headcount table each include a complete example row in the exact expected format, not just field labels | format |
| C-12 | Named verification checkpoints — >= 4 named checkpoints (e.g., MECHANISM-ROW-COUNT, CADENCE-ROW-COUNT, CHARTER-QUORUM-CHECK, HEADCOUNT-SUM) appear as explicit halt-and-verify gates; each states the check and the minimum required value | behavior |
| C-13 | Default-position declaration — the Inertia block opens with an explicit statement that the team can operate flat and structure must be justified; burden-of-proof framing precedes the mechanism table | behavior |
| C-14 | Strong modal language throughout — all compliance constraints use "must" / "required" / "not acceptable"; no compliance rule weakened to "should" or "recommended"; advisory framing is reserved for guidance, never for rules | correctness |

**Total: 120 pts. Golden = all 5 essential pass + composite >= 80.**

**Key failure modes seeded**: org-before-inertia, invented roles, merged decides/escalates, short quorum form, missing charter, flat diagram, generic rebuttal, cat-N mismatch, pressure line absent, mechanism table undercount, schema-only blocks (no example rows), missing checkpoints, no default-position framing, weak modal language ("should") on compliance rules.

**v2 additions rationale**:
- **C-11** (inline example rows): Signal from V-02 and V-05 — schemas with worked examples prevented format drift that field-label-only schemas did not.
- **C-12** (named checkpoints): Signal from V-04 — the count-and-advance pattern halted at each structural requirement; no other variation provided equivalent verification gates.
- **C-13** (default-position declaration): Signal from V-05 — opening with "THE TEAM CAN OPERATE FLAT" establishes burden-of-proof before any mechanism table row, making the inertia logic explicit rather than implicit.
- **C-14** (strong modal language): Derived from V-03's C-01 PARTIAL — "should use" instead of "must use" was the sole cause of failure; the four 100-scoring variations all used unambiguous modal language for every compliance rule.
