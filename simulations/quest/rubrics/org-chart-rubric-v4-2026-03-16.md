Reading the scorecard evidence carefully for novel PASS signals not yet captured in the rubric criteria.

**New pattern 1 — V-01 C-15 evidence:** "ends artifact after ABSENT block" — C-15 requires labeling eliminated sections ABSENT and naming prohibited alternatives. V-01 adds a further constraint: the instruction terminates the artifact after the ABSENT block. Without explicit termination, a model can label a section ABSENT and then continue producing content anyway, satisfying the letter of C-15 while defeating its purpose.

**New pattern 2 — V-03 C-17 evidence:** "post-interleave verification" — C-17 requires interleaved production order. V-03 adds an explicit post-production count check: pair count must equal governance row count. Without this, a model can interleave correctly for the first N pairs and silently drop the last charter, passing C-17's order check while producing an incomplete artifact.

Both are genuinely structural — they close bypass paths that the current criteria leave open. Two new aspirational criteria: C-18 and C-19.

---

## Rubric: org-chart — v4

**10 essential/recommended criteria + 11 aspirational. Golden = all 5 essential pass + composite >= 80.**

### Essential (60 pts, 12 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Inertia Assessment complete — all 4 sub-sections, mechanism table >= 2 rows with closed-set Types, FLAT-CASE-PRESSURE rating from closed set, VERDICT with concrete re-assessment trigger, appears before any org diagram | behavior |
| C-02 | Roles block grounded in .roles/ — ROLES-LOADED or ROLES-NOTE present; no role name introduced later that wasn't declared here | correctness |
| C-03 | ASCII org diagram with >= 2 hierarchy levels; committees as distinct nodes; all role names from roles block | format |
| C-04 | Operating rhythm table with >= 3 distinct rows: ROB + shiproom/gate + governance; no merged rows | coverage |
| C-05 | Committee charters with all 5 fields; Quorum in `N of M member roles` fraction form; Escalates names a destination; Membership >= 2 annotated roles | correctness |

### Recommended (30 pts, 10 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Headcount by area with split Decides/Escalates columns; >= 2 areas + Total row; Key Roles annotated with `(domain type)` | depth |
| C-07 | All 4 phase gate lines present in correct sequence; no section precedes its gate | format |
| C-08 | ROLE-TYPE-CLASSIFICATION block immediately after roles; all roles typed from closed set; three-tier order respected | correctness |

### Aspirational (55 pts, 5 each)

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | ORG-ELEMENT REGISTER (cat-1 through cat-4) + Anti-Pattern Watch with `(cat-N)` typed citations; no uncited element | depth |
| C-10 | Org Evolution Roadmap >= 2 rows from distinct trigger categories (no two headcount thresholds) | depth |
| C-11 | Inline example rows — mechanism table, operating rhythm, committee charter, and headcount table each include a complete example row in the exact expected format, not just field labels | format |
| C-12 | Named verification checkpoints — >= 4 named checkpoints appear as explicit halt-and-verify gates; each states the check and the minimum required value | behavior |
| C-13 | Default-position declaration — the Inertia block opens with an explicit statement that the team can operate flat and structure must be justified; burden-of-proof framing precedes the mechanism table | behavior |
| C-14 | Strong modal language throughout — all compliance constraints use "must" / "required" / "not acceptable" or a systematic DO/DO NOT register; no compliance rule weakened to "should" or "recommended" | correctness |
| C-15 | ABSENT-label SKIP — when the flat-verdict branch eliminates a section, the section is explicitly labeled ABSENT (not silently omitted) and the instruction explicitly prohibits "simplified" or "compact" alternatives; closes the compressed-hierarchy false-positive path | behavior |
| C-16 | Two-site constraint enforcement — each critical constraint is anchored at two independent sites: once as a structural slot-order rule, and once as a conditional "if you write X, then Y must precede it" prohibition; one site permits silent bypass, two sites close it | behavior |
| C-17 | Rhythm-charter interleaving — operating rhythm rows and committee charters are produced in pairs (rhythm row 1 → its charter, rhythm row 2 → its charter); the instruction explicitly prohibits batching all rhythm rows first and all charters second | format |
| **C-18** | **Artifact termination on flat-verdict** — when the flat-verdict branch is taken, the instruction contains an explicit STOP or artifact-end directive immediately after the ABSENT block; no content may follow the termination marker; closes the ABSENT-label-then-continue bypass where a model labels a section ABSENT and proceeds to produce it anyway | behavior |
| **C-19** | **Post-interleave pair-count verification** — after all rhythm-charter pairs are produced, the instruction requires an explicit count check: the number of pairs produced must equal the number of governance rows in the operating rhythm table; closes the silent-drop bypass where a model interleaves correctly for N−1 pairs but omits the final charter | behavior |

**Total: 145 pts. Golden = all 5 essential pass + composite >= 80.**

---

### v4 additions rationale

**C-18** (Artifact termination on flat-verdict): Signal from V-01 C-15 evidence. V-01 added "ends artifact after ABSENT block" to its flat-verdict handling — no other variation included an explicit termination directive. C-15 closes the compressed-hierarchy false-positive (ABSENT label present, prohibited alternatives named). C-18 closes the next bypass: a model that satisfies C-15's labeling requirement but then continues to produce content is behaviorally equivalent to one that never labeled the section at all. The STOP directive converts a labeling constraint into a structural halt. C-15 and C-18 are complementary — C-15 governs what the label must say, C-18 governs what must not follow it.

**C-19** (Post-interleave pair-count verification): Signal from V-03 C-17 evidence. V-03 introduced "post-interleave verification" alongside its interleaving rule — a count check confirming pairs produced equals governance rows. C-17 checks production-order coupling (no batching). C-19 checks production completeness: a model can interleave correctly for every pair it produces while silently dropping the last charter, satisfying C-17's ordering constraint while leaving the artifact structurally incomplete. The post-production count check closes this gap. C-17 and C-19 are complementary — C-17 governs order, C-19 governs count.

---

### v3 additions rationale (preserved)

**C-15** closes the false-positive where "simplified hierarchy" satisfies C-03 while violating the flat-verdict branch. V-05 was the only variation that labeled eliminated sections ABSENT and named the prohibited alternative explicitly. C-13 (positive declaration) and C-15 (elimination labeling) are complementary — different locations in the instruction, different logical roles.

**C-16** closes the single-anchor bypass. V-05 enforced trigger placement at two independent sites: slot order *and* a conditional rule. Every other variation used one site only — satisfying slot order while violating the conditional, or vice versa, was possible. The pattern generalizes to any constraint that appears in C-01 or C-05.

**C-17** closes the batching gap. V-04's "Do not batch all rows first and all charters second" was the only variation to state this. Without the coupling constraint, a variation can pass C-04 (three distinct rhythm rows) and C-05 (five-field charters) while producing them as two disconnected blocks, allowing drift between what the rhythm table names and what the charter specifies.

---

### v2 additions rationale (preserved)

**C-11** (inline example rows): Signal from V-02 and V-05 — schemas with worked examples prevented format drift that field-label-only schemas did not.

**C-12** (named checkpoints): Signal from V-04 — the count-and-advance pattern halted at each structural requirement; no other variation provided equivalent verification gates.

**C-13** (default-position declaration): Signal from V-05 — opening with "THE TEAM CAN OPERATE FLAT" establishes burden-of-proof before any mechanism table row, making the inertia logic explicit rather than implicit.

**C-14** (strong modal language): Derived from V-03's C-01 PARTIAL — "should use" instead of "must use" was the sole cause of failure; the four 100-scoring R1 variations all used unambiguous modal language for every compliance rule. V-05 demonstrated that a systematic DO/DO NOT register achieves this uniformly without restructuring prompt architecture.
