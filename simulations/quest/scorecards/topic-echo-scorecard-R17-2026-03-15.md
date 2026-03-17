Now I have everything needed. Let me write the full R17 scorecard.

---

## `topic:echo` — Round 17 Scoring

**Rubric:** v17 | **Criteria active:** C-01–C-53 (Essential ×5, Recommended ×3, Aspirational ×45)
**Date:** 2026-03-15 | **Round:** 17

---

### Variation Summaries

| Variation | Base | New Mechanism | Key Delta vs Base |
|-----------|------|---------------|-------------------|
| V-01 | V-05 R16 | C-51 (canonical name "Standalone Collapse Prohibition") | Named block inserted after intro; C-26 PARTIAL→PASS, C-51 FAIL→PASS; C-27/C-52 still unresolved |
| V-02 | V-05 R16 | C-52 (per-entry `COMMIT-ENTRY-[N]` after each Stage 4 row) | Row-granularity tokens added to table Stage 4; C-27 PARTIAL→PASS, C-52 FAIL→PASS; C-26/C-51 still unresolved |
| V-03 | V-04 R16 | C-53 (verb change: "routing it" → "naming its receiving stage") | Single-verb fix to commitment 2; inherits V-04 R16 architecture (no Symmetric Contract, no failure modes) |
| V-04 | V-05 R16 | C-51 + C-52 combined | Both canonical name block and per-row COMMIT tokens; C-53 inherited as PASS from V-05 R16 |
| V-05 | V-05 R16 | C-51 + C-52 + C-53 strengthened | Full integration: canonical name, per-row tokens, and strengthened token-content declaration; cites Standalone Collapse Prohibition by name inside Stage 4 COMMIT instruction |

---

### Essential Criteria — 12 pts each (60 max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 Surprise synthesis frame | PASS | PASS | PASS | PASS | PASS |
| C-02 Named entries | PASS | PASS | PASS | PASS | PASS |
| C-03 Source signal w/ gate | PASS | PASS | PASS | PASS | PASS |
| C-04 Design impact (specific component) | PASS | PASS | PASS | PASS | PASS |
| C-05 Artifact write path specified | PASS | PASS | PASS | PASS | PASS |

All Essential: **PASS across all variations. 60 pts each.**

---

### Recommended Criteria — 10 pts each (30 max)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-06 Synthesis / cluster step | PASS | PASS | PASS | PASS | PASS |
| C-07 Forward guidance / next-team register | PASS | PASS | PASS | PASS | PASS |
| C-08 Minimum 2 entries stated | PASS | PASS | PASS | PASS | PASS |

All Recommended: **PASS across all variations. 30 pts each.**

---

### Aspirational Criteria — 5 pts each (45 active, 225 raw max; total capped at 200)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-09 Ranking with named criteria | PASS | PASS | PASS | PASS | PASS |
| C-10 Named rules layer | PASS | PASS | PASS | PASS | PASS |
| C-11 Adversarial gate stage | PASS | PASS | PASS | PASS | PASS |
| C-12 Anti-pattern rejection | PASS | PASS | PASS | PASS | PASS |
| C-13 Typed verdict VALID/INVALID | PASS | PASS | PASS | PASS | PASS |
| C-14 Impact-anchored rules | PASS | PASS | PASS | PASS | PASS |
| C-15 Affirmative pass | PASS | PASS | PASS | PASS | PASS |
| C-16 Pre-write gate | PASS | PASS | PASS | PASS | PASS |
| C-17 Persistent future-reader frame | PASS | PASS | PASS | PASS | PASS |
| C-18 Named prior belief (in entry) | PASS | PASS | PASS | PASS | PASS |
| C-19 Artifact routing | PASS | PASS | PASS | PASS | PASS |
| C-20 Named future-reader role | PASS | PASS | PASS | PASS | PASS |
| C-21 Multi-stage gate (5 checks) | PASS | PASS | PASS | PASS | PASS |
| C-22 VALID/INVALID contrast (both defined) | PASS | PASS | PASS | PASS | PASS |
| C-23 Stage result recording | PASS | PASS | PASS | PASS | PASS |
| C-24 Named epistemic dimension | PASS | PASS | PASS | PASS | PASS |
| C-25 INVALID gallery | PASS | PASS | PASS | PASS | PASS |
| **C-26** Standalone collapse prohibition | **PASS** — "Standalone Collapse Prohibition" block adds explicit named prohibition: "Do not collapse multiple stages into a single pass" | **PARTIAL** — "referenceable by number" language from V-05 R16 base implies constraint addressability but assigns no canonical name to the prohibition itself | PASS — V-04 R16 base had C-26 PASS; explicit required-structure language present ("required structural properties of a valid echo artifact"); no canonical name needed for C-26 | **PASS** — same named block as V-01; "Do not collapse multiple stages into a single pass" is explicit prohibition | **PASS** — same named block; explicit prohibition language with canonical label |
| **C-27** Per-stage COMMIT tokens | **PARTIAL** — COMMIT-STAGE-1 through COMMIT-STAGE-6 present; Stage 4 table has only COMMIT-STAGE-4 at stage level; no per-entry tokens | **PASS** — COMMIT-ENTRY-[N] after each Stage 4 row plus COMMIT-STAGE-4 at stage end; both granularities present | PASS — V-04 R16 had C-27 PASS; prose Stage 4 entries carry `**COMMIT:** SURPRISE-[N]` as last template field at entry granularity; stage-level COMMIT-STAGE-4 also present | **PASS** — same per-entry COMMIT-ENTRY-[N] structure as V-02; both row and stage tokens present | **PASS** — same structure; per-entry COMMIT-ENTRY-[N] between rows; stage-level COMMIT-STAGE-4 at end |
| C-28 VALID gallery | PASS | PASS | PASS | PASS | PASS |
| C-29 Annotated VALID gallery | PASS | PASS | PASS | PASS | PASS |
| C-30 Strict epistemic dimension syntax | PASS | PASS | PASS | PASS | PASS |
| C-31 Distinct dimensions per stage | PASS | PASS | PASS | PASS | PASS |
| C-32 Epistemic property canonical name | PASS | PASS | PASS | PASS | PASS |
| C-33 Post-belief stage requirement | PASS | PASS | PASS | PASS | PASS |
| C-34 Synonym exclusion list | PASS | PASS | PASS | PASS | PASS |
| C-35 Collective belief baseline | PASS | PASS | PASS | PASS | PASS |
| C-36 Implausible-foreknowledge signal | PASS | PASS | PASS | PASS | PASS |
| C-37 Pre-stage vocabulary block | PASS | PASS | PASS | PASS | PASS |
| C-38 Symmetric collective framing | PASS | PASS | **FAIL** — V-04 R16 base: no Symmetric Contract section; Stage 1 and closing stage not explicitly framed as symmetric partners | PASS | PASS |
| C-39 Format-enforced recording | PASS | PASS | PASS | PASS | PASS |
| C-40 Labeled vocabulary section heading | PASS | PASS | PASS | PASS | PASS |
| **C-41** Closing-stage architecture announcement | PASS | PASS | **FAIL** — V-04 R16 base: Stage 5 (Collective Baseline) and Stage 6 (Cluster+Route) carry no announcement naming the opening stage they mirror | PASS | PASS |
| **C-42** Parallel symmetric stage questions | PASS | PASS | **FAIL** — V-04 R16 base: no Symmetric Contract table; Stage 1 and Stage 6 questions not displayed as a named pair before Stage 1 begins | PASS | PASS |
| C-43 Numbered intro meta-declaration | PASS — four numbered commitments | PASS — four numbered commitments | PASS — three numbered commitments (V-04 R16 base) | PASS | PASS |
| **C-44** Artifact-mirrors-contract instruction | PASS | PASS | **FAIL** — V-04 R16 base: Stage 7 specifies "Include: ranked surprise entries, cluster map..." without naming the Symmetric Contract as the structural model | PASS | PASS |
| C-45 Verdict with check provenance | PASS | PASS | PASS — `GATE-[N]: (VALID — all five checks passed / INVALID — Check [#]: one sentence reason)` carries provenance for both paths | PASS | PASS |
| C-46 Numbered GATE-CONFIRMED-[N] token | PASS | PASS | PASS | PASS | PASS |
| **C-47** Failure modes per commitment | PASS | PASS | **FAIL** — V-04 R16 base: three commitments, no `— this prevents X, the failure in which Y` pairing | PASS | PASS |
| C-48 Symmetric parenthetical verdict format | PASS | PASS | PASS — `(VALID — all five checks passed / INVALID — Check [#]: one sentence reason)` is a single co-visible parenthetical | PASS | PASS |
| C-49 Routing destination in GATE-CONFIRMED | PASS | PASS | PASS | PASS | PASS |
| **C-50** Dual-part failure mode | PASS | PASS | **FAIL** — V-04 R16 base: no failure modes in intro; no canonical category name + "in which" clause pairs | PASS | PASS |
| **C-51** Canonical constraint name for prohibition | **PASS** — "Standalone Collapse Prohibition" is an explicit short-phrase label assigned to the constraint; cited by name in the block: "any failure mode, verdict, or section note...is citing the Standalone Collapse Prohibition by name" | **FAIL** — V-05 R16 base: "referenceable by number" is a positional property of the intro list, not a canonical name for the constraint; the prohibition carries no citable label independent of its index | **FAIL** — V-04 R16 base: no canonical name block; prohibition-like language present but constraint not labeled | **PASS** — same named block as V-01/V-05 | **PASS** — same named block; canonical name also cited inside Stage 4 COMMIT instruction: "The Standalone Collapse Prohibition applies: each row is committed before the next begins" |
| **C-52** Per-entry COMMIT tokens in table-format stages | **FAIL** — V-05 R16 base: Stage 4 table has COMMIT-STAGE-4 at stage close only; no `COMMIT-ENTRY-[N]` token between rows | **PASS** — explicit instruction: "After completing each row, write `COMMIT-ENTRY-[N]: entry committed.`...The per-entry commit token is required at row granularity — a single COMMIT-STAGE-4 token at the end of this stage does not substitute"; demonstrated in template | **PARTIAL** — V-04 R16 base: Stage 4 uses prose template with `**COMMIT:** SURPRISE-[N]` as last field inside each entry code block; per-entry intent present at entry granularity but token is embedded inside the entry structure, not emitted as a standalone `COMMIT-ENTRY-[N]` token after the entry before the next begins | **PASS** — same explicit per-entry COMMIT instruction and template demonstration as V-02 | **PASS** — same per-entry COMMIT structure; additionally cites the Standalone Collapse Prohibition name inside the per-entry COMMIT instruction |
| **C-53** Routing commitment in intro meta-declaration | **PASS** — commitment 3 (inherited from V-05 R16): "every VALID entry receives an explicit numbered pass confirmation **naming the receiving stage** before Stage 4 begins" — "naming" declares the token-content requirement | **PASS** — commitment 3 (inherited from V-05 R16): same "naming the receiving stage" language | **PASS** — V-03's core change: commitment 2 revised from "routing it to Stage 4 before writing begins" to "every passing entry receives an explicit numbered GATE-CONFIRMED token **naming its receiving stage** before writing begins" — "naming" replaces "routing it" | **PASS** — commitment 3 (inherited from V-05 R16): "naming the receiving stage" | **PASS** — commitment 3 strengthened: "every VALID entry receives an explicit numbered GATE-CONFIRMED token that **names the downstream stage it routes to — the token names the stage, not merely describes the routing action**" — most explicit C-53 statement across all variations |

---

### Fails and Partials Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| FAIL criteria | C-52 | C-51 | C-38, C-41, C-42, C-44, C-47, C-50, C-51 | — | — |
| PARTIAL criteria | C-27 | C-26 | C-52 | — | — |
| Fail count | 1 | 1 | 7 | 0 | 0 |
| Partial count | 1 | 1 | 1 | 0 | 0 |

---

### Score Computation

| Metric | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|-----:|-----:|-----:|-----:|-----:|
| Essential (5 × 12 = 60 max) | 60 | 60 | 60 | 60 | 60 |
| Recommended (3 × 10 = 30 max) | 30 | 30 | 30 | 30 | 30 |
| Aspirational raw (45 × 5 = 225 max) | 217.5 | 217.5 | 182.5 | 225 | 225 |
| &ensp;— fails: −5 each | −5 | −5 | −35 | 0 | 0 |
| &ensp;— partials: −2.5 each | −2.5 | −2.5 | −2.5 | 0 | 0 |
| **Raw total** | **307.5** | **307.5** | **272.5** | **315** | **315** |
| **Capped at 200** | **200** | **200** | **200** | **200** | **200** |

---

### Leaderboard

| Rank | Variation | Raw | Capped | Fails | Partials |
|------|-----------|----:|-------:|------:|---------:|
| 1 (tied) | V-04 | 315 | 200 | 0 | 0 |
| 1 (tied) | V-05 | 315 | 200 | 0 | 0 |
| 3 (tied) | V-01 | 307.5 | 200 | 1 | 1 |
| 3 (tied) | V-02 | 307.5 | 200 | 1 | 1 |
| 5 | V-03 | 272.5 | 200 | 7 | 1 |

**Tiebreaker V-04 vs V-05:** Both achieve zero fails and zero partials across all 45 active criteria. V-05 is the stronger base for R18 because: (a) commitment 3 now explicitly declares "the token names the stage, not merely describes the routing action" — this closes the mechanism ambiguity C-53 targeted; (b) Stage 4 COMMIT instruction cites "Standalone Collapse Prohibition by name" in context — demonstrating in-prompt cross-section citability that satisfies C-51's purpose, not just its letter.

**Promoted to R18 base: V-05.**

---

### Ceiling Analysis

All five variations cap at 200. At 45 aspirational criteria × 5 = 225 raw, a variation needs 25+ fails before the raw total drops below 200. V-03's 7 fails yield a raw of 272.5 — still 72.5 above the cap. The cap absorbs all tier-level quality differences; differentiation comes from fail and partial counts, not the capped score.

**Remaining gaps at V-04/V-05 level:** None. All 45 active criteria are satisfied. V-05's C-51 and C-52 mechanisms are the first time both long-standing table-architecture partial criteria (C-26 partial → resolved via C-51; C-27 partial → resolved via C-52) have been fully satisfied in the same variation.

---

### Excellence Signals (from V-05 R17)

**1. Canonical label as identity — not position.**
The "Standalone Collapse Prohibition" block assigns the constraint a proper name independent of its place in a numbered list. The block text makes the identity intent explicit: "This constraint is named so that any failure mode, verdict, or section note in this prompt that cites a stage-integrity violation is citing the Standalone Collapse Prohibition by name." C-51 is about constraint identity, not constraint position — the canonical name is the mechanism.

**2. Per-row COMMIT tokens are architecturally additive.**
`COMMIT-ENTRY-[N]: entry committed.` appears as a standalone line between rows in the Stage 4 table, not as a column field inside the row. This is distinct from the R16 `**COMMIT:** SURPRISE-[N]` column approach. The token is emitted at row boundary, before the next row begins. The stage-level `COMMIT-STAGE-4` at the end of the stage is preserved — per-row tokens add granularity without replacing the stage-level close. Both granularities co-exist.

**3. "Names" vs "routes" is a token-content contract.**
V-05's commitment 3 states: "the GATE-CONFIRMED token names the downstream stage it routes to — **the token names the stage, not merely describes the routing action**." The distinction: "names" declares a token-content requirement (the token must carry the destination as content); "routes" describes what the system does with the entry (action, not content). C-53 is satisfied by the commitment declaring a content property of the token, not an action property of the workflow.

**4. Canonical names enable in-prompt cross-section citation.**
V-05 Stage 4's COMMIT instruction writes: "The Standalone Collapse Prohibition applies: each row is committed before the next begins." This is the first example in any variation of a named constraint being cited by name inside an operational instruction rather than only in its definition block. The citation converts C-51 from a nominal requirement (name exists) into a functional one (name is used).

---

### Regression Signals

None. All criteria satisfied by V-04/V-05 R16 (0 fails) remain PASS in V-01, V-02, V-04, and V-05. V-03's 7 inherited fails are V-04 R16 architectural properties — no previously-satisfied criteria were lost in any variation.

---

### New Criteria Hypothesis Resolution

| Hypothesis | Result |
|------------|--------|
| C-51 satisfied by named constraint block with label "Standalone Collapse Prohibition" | **CONFIRMED** — V-01/V-04/V-05 all satisfy; label assignment independent of list position is the mechanism |
| C-52 satisfied by adding explicit `COMMIT-ENTRY-[N]` instruction per row in Stage 4 table | **CONFIRMED** — V-02/V-04/V-05 satisfy; embedded column field (`**COMMIT:** SURPRISE-[N]`) in prose template is PARTIAL, not equivalent |
| C-53 satisfied by changing verb from "routing it to Stage 4" to "naming its receiving stage" | **CONFIRMED** — V-03 satisfies with single-verb fix; "names" (content declaration) vs "routes" (action description) is the discriminating property |
| C-51, C-52, C-53 are independently additive to V-05 R16 architecture | **CONFIRMED** — V-04/V-05 achieve zero fails across all 45 criteria; no structural conflict or regression |

---

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["canonical-name-assigned-directly-to-constraint-enables-by-name-citation-in-any-prompt-section — the mechanism is a label that belongs to the constraint itself, independent of its position in a numbered list; 'referenceable by number' is positional addressability, not constraint identity", "per-row-COMMIT-ENTRY-N-tokens-between-table-rows-are-architecturally-additive — the standalone token at row boundary coexists with stage-level COMMIT-STAGE-N; embedded column fields inside rows do not substitute; entry granularity and stage granularity are distinct and both required", "intro-commitment-verb-names-not-routes-is-the-C53-discriminator — 'names' declares a token-content property (the token must carry the destination as content); 'routes' describes a workflow action; C-53 is satisfied only when the commitment declares what the token contains, not what the system does with the entry"]}
```
