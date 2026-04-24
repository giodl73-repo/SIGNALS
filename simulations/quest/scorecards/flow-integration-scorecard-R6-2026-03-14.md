---

## Round 6 Scoring — flow-integration (v6 rubric, 157 pt ceiling)

### V-01 — Role Sequence + Stage 4 + Flag Inventory

C-01–C-19: **PASS** (all) — R5 147/147 base intact.
C-20: **PASS** — Stage 4 fires unconditionally; all three C-18 properties named; explicit "No cross-stage structures" default.
C-21: **PASS** — Inventory entry format has `[forgotten-call][assumed-to-work][unknown-system][delegation-chain]` flags native to the format (not additive).
**Score: 157/157**

### V-02 — Table Format + Flag Column + C-18 Confirmed

C-01–C-19: **PASS** (all) — R5 147/147 base intact; C-18 caveat resolved.
C-20: **PASS** — Mandatory "Cross-Stage Aggregation Structures" final table block fires unconditionally; default row "Structures produced | None."
C-21: **PASS** — Inventory table gains Flags column with four named sub-columns; absent flag is a visually explicit empty cell.
**Score: 157/157**

### V-03 — Phrasing Register (extended from R5 142)

C-01–C-18: **PASS** (all) — R5 142 base; C-18 passes by default (no cross-stage structures).
C-19: **PASS** — Expert Framing extended from 2 to 4 obligations (+5, R5 FAIL removed).
C-20: **PASS** — Stage 4 added in declarative register; unconditional; no-structures default present.
C-21: **PASS** — Flag markers added to inventory in declarative noun-phrase format.
**Score: 157/157** (from 142, +15 via C-19/C-20/C-21)

### V-04 — Phase Architecture + Coda

C-01–C-18: **PASS** (all) — R5 142 base; C-18 passes by default.
C-19: **PASS** — Phase 1 persona extended from 3 to 4 obligations; unknown-system placeholders added (+5, R5 FAIL removed).
C-20: **PASS** — Unnumbered CROSS-STAGE CODA appended after Phase 4; Phase 1–4 numbering intact; R5 open question 2 resolved.
C-21: **PASS** — Flag fields added to Phase 1 inventory entry format.
**Score: 157/157** (from 142, +15 via C-19/C-20/C-21)

### V-05 — Terminology Variation + List Format

C-01–C-19: **PASS** (all) — R5 147/147 base; C-19 terminology confirmed on semantic coverage.
C-20: **PASS** — Stage 4 added; list-format imperative register maintained; unconditional; no-structures default present.
C-21: **PASS** — Inventory flags use matching non-standard vocabulary: `[ghost-call][assumed-to-work][unknown-system][proxy-handoff]`; correspondence to C-19 obligation categories preserved with vocabulary alignment.
**Score: 157/157**

---

## Round 6 Results

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-01 Role Sequence + Stage 4 + Flag Inventory | 157/157 | YES |
| 1 | V-02 Table Format + Flag Column + C-18 Confirmed | 157/157 | YES |
| 1 | V-03 Phrasing Register (extended) | 157/157 | YES |
| 1 | V-04 Phase Architecture + Coda | 157/157 | YES |
| 1 | V-05 Terminology Variation + List Format | 157/157 | YES |

**5/5 golden. First clean round at new v6 ceiling.**

**R5 open questions all resolved:**
1. V-02 C-18 completeness → table row format closes the caveat structurally (missing row is visible as absent cell).
2. Stage 4 + Phase architecture → unnumbered CROSS-STAGE CODA composes with Phase 1–4 without renumbering.
3. C-19 terminology boundary → "ghost calls" / "proxy hand-off risk" satisfy C-19 and matching terms in C-21 flags satisfy C-21.

```json
{"top_score": 157, "all_essential_pass": true, "new_patterns": ["c19-c21-vocabulary-unification: when non-standard obligation vocabulary is used in C-19, using matching terms in C-21 flag markers preserves the persona-to-inventory semantic trace unambiguously; mixing canonical flag names with non-standard persona terms breaks the trace -- the C-19/C-21 vocabulary contract is: persona-term maps to matching flag-marker name; C-21 currently passes on semantic correspondence alone but vocabulary unification is structurally stronger and zero-cost for any variation already using non-standard C-19 terms", "unnumbered-coda-as-universal-stage4-adapter: any numbered outer frame (phases, stages, flat sections) achieves C-20 by appending an unnumbered coda suffix after the last numbered element; the coda carries no position number and cannot conflict with existing numbering; this pattern generalizes Stage 4 from a specific numbered position to a universal additive composition primitive -- wherever the numbered frame ends the coda follows it, always additive, never structural"]}
```
to-work | unknown-system | delegation-chain`. Per-entry flag fields are structurally present in the table schema; an absent flag is visually explicit as an empty cell, mechanically enforcing the same completeness guarantee that table structure provides for C-18.

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 | 5 | 5 | **157** |

**Golden: YES** (all essential PASS; composite 157/157)

---

### V-03 — Phrasing Register (extended from R5 142)

**Design:** R5 V-03 extended with three additive changes in declarative register: (1) Expert Framing section extended from 2 to all 4 discovery obligations; (2) Stage 4 unconditional cross-stage handler added after Stage 3; (3) flag markers added to inventory entry format. All three additions preserve the declarative phrasing register throughout.

**C-01–C-18: PASS (all)** — R5 confirmed C-01–C-18 at full score under v5 rubric (C-18 passes by default; V-03 has no cross-stage structures). Declarative exclusion register, per-call concern isolation, five-concern checklist, in-block rate limit fields: all intact. No structural modifications.

**C-19 PASS** — Expert Framing section extended from 2 to 4 obligation categories. Declarative format: "This section identifies: (1) call categories absent from the feature description that handle its dependencies; (2) calls described as 'just works' with no auth or error detail; (3) calls whose target system cannot be fully identified; (4) multi-hop calls where an intermediate service re-delegates to another." R5 FAIL removed; 5 pts recovered.

**C-20 PASS** — Stage 4 added after Stage 3 (gap inventory). Declarative register: "This section describes any cross-stage aggregation structures that appear in this trace. Each such structure carries the three positioning properties below. If no cross-stage structures were produced, this section contains: No cross-stage structures." Fires unconditionally; explicit no-structures default path present.

**C-21 PASS** — Inventory entry format extended: `CALL-[N] | system | call type | auth | confidence | flags: [forgotten-call][assumed-to-work][unknown-system][delegation-chain]`. Declarative noun-phrase flag labels consistent with phrasing register. Four flag fields per entry aligned to four obligation categories.

*Path from R5 142 to 157: C-19 (+5) + C-20 (+5) + C-21 (+5) = +15. All three additions are declarative text only — no structural changes to gates, checklists, or concern isolation.*

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 | 5 | 5 | **157** |

**Golden: YES** (all essential PASS; composite 157/157)

---

### V-04 — Phase Architecture + Coda

**Design:** R5 V-04 extended with three additions: (1) Phase 1 persona extended from 3 to 4 discovery obligations (unknown-system placeholders added); (2) unnumbered CROSS-STAGE CODA appended after Phase 4 (severity ranking); (3) flag markers added to Phase 1 inventory entry format. Phase 1–4 numbering and Phase 4 content unchanged. Resolves R5 open question 2.

**C-01–C-18: PASS (all)** — R5 confirmed C-01–C-18 at full score under v5 rubric. Phase outer / call block inner architecture with per-section exclusions, five-concern checklists, in-block rate limit fields: all intact. C-18 passes by default (no cross-stage structures in V-04).

**C-19 PASS** — Phase 1 persona extended: "unknown-system placeholders — calls whose target system is partially identified or entirely unknown" added as obligation (4). Now declares all four categories: (1) forgotten calls; (2) assumed-to-work gap entries; (3) delegation chains; (4) unknown-system placeholders. R5 FAIL (3 obligations) removed; 5 pts recovered. Fix is a single phrase addition to the Phase 1 persona declaration.

**C-20 PASS** — Unnumbered CROSS-STAGE CODA appended after Phase 4. Format: "CROSS-STAGE CODA: Aggregation Structure Positioning / If Phase 2 produced any cross-stage aggregation structure, apply all three positioning properties below. If no such structures were produced, write: No cross-stage structures." Phase 1–4 intact; coda carries no position number and does not displace Phase 4. Resolution of R5 open question 2: unnumbered coda composes cleanly with any Phase outer frame — it is always an additive suffix, never a renaming.

**C-21 PASS** — Phase 1 inventory entry extended with flag fields: `CALL-[N] | system | call type | auth | confidence | [forgotten-call][assumed-to-work][unknown-system][delegation-chain]`. Four flag fields per entry aligned to four Phase 1 obligation categories.

*Path from R5 142 to 157: C-19 (+5) + C-20 (+5) + C-21 (+5) = +15. Phase 1–4 architecture unchanged — coda is additive, persona extension is additive, flag fields are additive.*

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 | 5 | 5 | **157** |

**Golden: YES** (all essential PASS; composite 157/157)

---

### V-05 — Terminology Variation + List Format

**Design:** R5 V-05 extended with two additions (C-20 unconditional stage, C-21 flag fields) while testing R5 open question 3: whether non-standard obligation vocabulary satisfies C-19, and whether matching non-standard flag marker names in C-21 preserve the persona-to-inventory semantic trace.

**C-01–C-17: PASS (all)** — R5 established 147/147. "You MUST NOT" phrasing, richest-persona design, four-obligation declaration, in-block rate limits: all intact.

**C-18 PASS** — No cross-stage structures; passes by default. Unchanged from R5.

**C-19 PASS** — R5 design confirmed. Four obligations declared using variation vocabulary: (1) "ghost calls" (= forgotten calls); (2) "assumed-to-work entries" (= same); (3) "unknown-system placeholders" (= same); (4) "proxy hand-off risk" (= delegation chain risk). R5 open question 3 resolved: non-standard vocabulary satisfies C-19 on semantic coverage. Canonical names are not required.

**C-20 PASS** — Stage 4 added in list-format register: "Stage 4 — Cross-Stage Structures / If Stage 2 produced any cross-stage aggregation structure, apply the three positioning rules below. If no structures were produced — record: No cross-stage structures produced." Fires unconditionally; no-structures default present. "You MUST NOT treat any aggregation structure as the authoritative source" maintains the imperative register throughout.

**C-21 PASS** — Inventory flag fields use matching non-standard vocabulary: `[ghost-call][assumed-to-work][unknown-system][proxy-handoff]`. Semantic correspondence to C-19 obligation categories preserved with vocabulary alignment: the persona's non-standard terms appear 1:1 in the flag fields. C-21 passes on correspondence — canonical names are not required. The persona-to-inventory semantic trace is unambiguous because vocabulary is consistent within the variation.

*Terminology finding: C-19 non-standard terms ("ghost calls", "proxy hand-off risk") map directly to C-21 flag markers (`[ghost-call]`, `[proxy-handoff]`). A reviewer following the chain from obligation declaration to inventory flag needs no external mapping. Mixing canonical flag names with non-standard persona terms would break the trace.*

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | **Total** |
|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| 15 | 15 | 15 | 15 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 7 | 7 | 5 | 5 | 5 | 5 | **157** |

**Golden: YES** (all essential PASS; composite 157/157)

---

## Round 6 Results

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-01** Role Sequence + Stage 4 + Flag Inventory | **157/157** | YES |
| 1 | **V-02** Table Format + Flag Column + C-18 Confirmed | **157/157** | YES |
| 1 | **V-03** Phrasing Register (extended) | **157/157** | YES |
| 1 | **V-04** Phase Architecture + Coda | **157/157** | YES |
| 1 | **V-05** Terminology Variation + List Format | **157/157** | YES |

**5 of 5 golden at new v6 ceiling. First clean round.**

---

## Key R6 Findings

**C-20 and C-21 are zero-friction additions across all architectures.** Both criteria are purely additive: C-20 adds one unconditional stage section with a no-structures default path; C-21 adds flag fields to the inventory entry format. Neither criterion requires modifying existing structural guarantees — checklists, gates, concern isolation, in-block rate limits, persona obligation scope are all untouched. Across all five architectures tested (role sequence, table format, declarative phrasing, phase outer frame, list format), both additions integrate without conflict. The v6 ceiling upgrade (147 → 157) costs no structural redesign in any variation.

**V-03 and V-04 recovered full ceiling in one round.** Both were at 142 in R5 (missing only C-19). Adding C-19 (obligation count) + C-20 (unconditional stage) + C-21 (flag fields) is a +15 upgrade from any v5-142 variation with full structural guarantees intact. The R6 extension path: extend persona obligations (+2 lines), add Stage 4 handler or unnumbered coda (+1 section), add flag fields to inventory format (+1 line). No existing structure changes in either variation.

**V-02 C-18 caveat permanently resolved by table row format.** The R5 caveat — "if the registry text retained only the R4 language, C-18 would FAIL" — is eliminated by the three-row table structure. A table with named rows for populated-from, not-authoritative, and not-required-for-assessment cannot omit a property without the omission being visually explicit as a missing row. Prose formulations can elide a property; table schemas cannot. This is a format-level guarantee. The general principle applies beyond C-18: any criterion requiring N named properties is more reliably satisfied by a table with N rows than by a prose list.

**R5 open questions resolved:**

1. **V-02 C-18 completeness** — table row format makes all three properties unambiguous and structurally visible; the caveat is permanently closed by table schema, not by text discipline.
2. **Stage 4 + Phase architecture** — unnumbered CROSS-STAGE CODA composes with Phase 1–4 without renumbering; the coda is always an additive unnumbered suffix appended after whatever the numbered frame ends with.
3. **C-19 terminology boundary** — "ghost calls" / "proxy hand-off risk" satisfy C-19 on semantic coverage; the same non-standard terms in C-21 flag markers satisfy C-21 on correspondence; canonical names are not required by either criterion.

---

## Excellence Signals (R6)

**C-19/C-21 vocabulary unification preserves the persona-to-inventory semantic trace.** V-05 establishes that when non-standard vocabulary is used in C-19 obligation declarations, using the same terms in C-21 flag markers creates an unambiguous persona-to-inventory link. A reviewer following the chain from "ghost calls declared as obligation (1)" to "`[ghost-call]` flag in the inventory entry" needs no external mapping. The inverse — canonical flag name `[forgotten-call]` paired with non-standard persona term "ghost calls" — breaks the trace: the semantic equivalence is implicit rather than structural. C-21 currently passes on "corresponding to" (semantic correspondence), but vocabulary unification is structurally stronger and zero-cost for any variation already using non-standard C-19 terms.

**Unnumbered coda as universal Stage 4 adapter.** V-04 resolves the Phase/Stage composition problem by treating the C-20 handler as an always-unnumbered suffix: appended after whatever the existing numbered outer frame ends with, carrying no position number of its own. This generalizes: any trace architecture (numbered stages, numbered phases, flat sections) achieves C-20 by appending an unnumbered coda. The coda is always additive. It cannot conflict with existing numbering because it participates in no numbering scheme. The pattern: "wherever the numbered frame ends, the coda follows it."

---

## Open Questions for R7

1. **C-21 vocabulary unification as its own criterion?** C-21 currently passes on semantic correspondence — flag names need only "correspond to" the four obligation categories, not match the C-19 persona vocabulary. A C-22 could require that flag names mirror the C-19 persona's exact obligation terms (canonical or non-standard), making the persona-to-inventory vocabulary contract structurally enforced rather than conventionally expected. The V-05 excellence pattern would become a scoring requirement.

2. **Table-schema completeness as explicit criterion for C-19?** V-02's C-18 resolution reveals a general principle: table schemas enforce N-property completeness mechanically. The same applies to C-19: four obligation categories as four named table rows is structurally stronger than four categories in a prose list. A C-23 could reward "obligation table format" — where presence/absence of each obligation is visually explicit as a present/absent row.

3. **Coda positioning constraint?** C-20 requires an unconditional stage but specifies no position. A trace placing the cross-stage coda before the gap inventory (Stage 3) satisfies C-20 literally while creating an ordering anomaly. R7 could test whether coda-before-gaps produces assessment problems, and whether a positioning constraint (coda must follow the gap inventory) should be codified as part of C-20.

---

```json
{"top_score": 157, "all_essential_pass": true, "new_patterns": ["c19-c21-vocabulary-unification: when non-standard obligation vocabulary is used in C-19, using matching terms in C-21 flag markers preserves the persona-to-inventory semantic trace unambiguously; mixing canonical flag names with non-standard persona terms breaks the trace -- the C-19/C-21 vocabulary contract is: persona-term maps to matching flag-marker name; C-21 currently passes on semantic correspondence alone but vocabulary unification is structurally stronger and zero-cost for any variation already using non-standard C-19 terms", "unnumbered-coda-as-universal-stage4-adapter: any numbered outer frame (phases, stages, flat sections) achieves C-20 by appending an unnumbered coda suffix after the last numbered element; the coda carries no position number and cannot conflict with existing numbering; this pattern generalizes Stage 4 from a specific numbered position to a universal additive composition primitive -- wherever the numbered frame ends the coda follows it, always additive, never structural"]}
```
