I now have all 5 variations fully read. Let me score each against all 24 criteria.

---

# mock-ns Round 6 — Quest Score

## Rubric Summary (v6)

| Weight | Criteria | Pts each | Max |
|--------|----------|----------|-----|
| Essential | C-01–C-05 | 10 | 50 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-24 | 2 | 32 |
| **Total** | | | **112** |

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01–C-05)

All 5 variates share identical A-1 through A-5 structure and the same S-1–S-3 steps. Essential criteria depend only on this shared structure.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01: 6-field header | PASS | PASS | PASS | PASS | PASS | A-1: Skill, Topic, Category, Date, Status, Flag — all present |
| C-02: CATEGORY correct | PASS | PASS | PASS | PASS | PASS | S-2 category table complete with 3 categories |
| C-03: FLAG correct | PASS | PASS | PASS | PASS | PASS | S-3 5-row FLAG table + compliance override |
| C-04: Fidelity warning matches CATEGORY | PASS | PASS | PASS | PASS | PASS | A-2: all 3 CATEGORY-matched warning templates |
| C-05: Body is skill-specific | PASS | PASS | PASS | PASS | PASS | A-3: requires correct section headings, tables, gate/verdict, enforcement for named skill-id |

**Essential subtotal: 50/50 all variates.**

---

### Recommended Criteria (C-06–C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06: S-1 emit lines (TOPICS.md + generating) | PASS | PASS | PASS | PASS | PASS | TOPICS.md line in S-0 (first); generating emit in S-1 (second) — correct ordering |
| C-07: Artifact path uses namespace, not skill-id | PASS | PASS | PASS | PASS | PASS | A-4: `simulations/mock/{topic}-{namespace}-mock-{date}.md` |
| C-08: Next-step line as final line | PASS | PASS | PASS | PASS | PASS | A-5: `Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md` |

**Recommended subtotal: 30/30 all variates.**

---

### Aspirational Criteria (C-09–C-24)

I evaluate criteria shared by all variates first, then the two discriminating criteria (C-23, C-24).

#### Shared Aspirational (C-09–C-22) — same result for all 5 variates

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09: topic default = topic-plan (not topic-status) | PASS | S-1 table: `topic-plan \| NEVER topic-status (excluded: meta-structural)` |
| C-10: Compliance override when tags present | PASS | S-3 compliance override block present; **default pass** when no tags |
| C-11: FLAG rule names critical namespaces, covers all 5 cases | PASS | S-3: 5-row table; condition cells name `trace-*`, `scout-feasibility`, `listen-*` explicitly; HS preamble enumerates all critical skill-ids |
| C-12: S-0 resolves tier before S-1 begins | PASS | S-0 is a separate labeled step; TOPICS.md status line emitted before S-1 begins |
| C-13: Error halt on unrecognized skill-id | PASS | S-2: "emit an error that names the unrecognized skill-id and points to the registry. Stop." V-05 uses equivalent phrasing |
| C-14: Assembly in discrete named steps A-1–A-5 | PASS | STEP A-1 ASSEMBLE HEADER, A-2 FIDELITY WARNING, A-3 GENERATE ARTIFACT BODY, A-4 WRITE ARTIFACT, A-5 NEXT-STEP LINE — all 5 present and labeled |
| C-15: CONSTRAINT names 3+ prohibited op types | PASS | V-01/V-04: 4 ops. V-02/V-03: 5 ops. V-05: 5 ops (synonym forms). All meet 3-op minimum |
| C-16: Wildcard patterns in FLAG table condition column cell | PASS | Rows 3–4: "skill-id matches `trace-*`, `scout-feasibility`, or `listen-*`" directly in condition cell |
| C-17: S-0 gate sentence names S-1 | PASS | All variates: "Do not begin S-1 until this line is emitted" (V-01–V-04) / "S-1 must not begin until the line above appears" (V-05) — name S-1 by label |
| C-18: Tier-carry handoff names S-2 and S-3 | PASS | All: "Carry the resolved tier into S-2 and S-3" (V-01–V-04) / "Forward the resolved tier to S-2 and S-3" (V-05) |
| C-19: Both preamble gate AND terminal gate present | PASS | All: preamble gate precedes resolution table; terminal gate follows table. C-19 requires gate before bullets — satisfied even when CONSTRAINT precedes preamble gate. C-23 is the stricter form |
| C-20: Tier-carry in table column AND standalone terminal sentence | PASS | Table tier row: "Carry into S-2 and S-3" (V-01–V-04) / "Propagates to S-2 and S-3" (V-05). Standalone: both consumer labels named in all variates |
| C-21: CONSTRAINT names 4+ op types including body generation | PASS | V-01/V-04: 4 ops including "No body generation". V-02/V-03/V-05: 5 ops including body generation equivalent |
| C-22: FLAG table has dedicated row for HS-critical-tier=1 | PASS | 5-row table: Row 4 = `...tier = 1` (critical, flag: none); Row 5 = `...all other skills, any tier`. Structurally separated |

**C-09–C-22 subtotal: 28/28 all variates.**

---

#### C-23: Preamble gate is the absolute opening sentence of S-0

| Variate | First content of S-0 | Result | Evidence |
|---------|---------------------|--------|---------|
| V-01 | "Before any other step begins, emit the TOPICS.md status line below." | **PASS** | Preamble gate IS the first sentence — zero pre-gate surface. CONSTRAINT follows after. |
| V-02 | `CONSTRAINT: No category lookup. No skill selection...` | **FAIL** | CONSTRAINT block precedes preamble gate. Reader encounters CONSTRAINT text before any gate sentence. |
| V-03 | "Read TOPICS.md to resolve the topic's tier and compliance tags." | **FAIL** | Introductory prose is first; preamble gate is second sentence. One intro sentence = minimal C-23 violation. |
| V-04 | `CONSTRAINT: No category lookup. No skill selection...` | **FAIL** | Same pattern as V-02. CONSTRAINT is pre-gate surface. |
| V-05 | "This step emits first. Write the TOPICS.md status line before any other work begins." | **PASS** | Alternative phrasing — declarative form — but IS the opening sentence before CONSTRAINT and all else. Zero pre-gate surface. |

---

#### C-24: CONSTRAINT names 5+ op types including artifact write phase

| Variate | CONSTRAINT ops | Write phase covered? | Result | Evidence |
|---------|---------------|---------------------|--------|----------|
| V-01 | "No category lookup. No skill selection. No mock generation. No body generation." (4 ops) | NO | **FAIL** | Artifact path construction and file write not prohibited. C-21 passes (4 ops) but C-24 requires 5th phase. |
| V-02 | "...No artifact path construction or file write." (5 ops) | YES | **PASS** | Explicitly prohibits A-4 WRITE phase activity. |
| V-03 | "...No artifact path construction or file write." (5 ops) | YES | **PASS** | Same 5-op CONSTRAINT as V-02. |
| V-04 | "No category lookup. No skill selection. No mock generation. No body generation." (4 ops) | NO | **FAIL** | Same 4-op CONSTRAINT as V-01. Artifact write phase unclosed. |
| V-05 | "No lookup of skill categories. No skill-id resolution. No mock content generation. No artifact body construction. No artifact path assembly or file output." (5 ops, synonym forms) | YES | **PASS** | "No artifact path assembly or file output" closes the output phase using synonym language. |

---

## Composite Scores

| Variate | Essential (50) | Recommended (30) | C-09–C-22 (28) | C-23 (2) | C-24 (2) | Total | Rank |
|---------|---------------|-----------------|----------------|----------|----------|-------|------|
| **V-05** | 50 | 30 | 28 | **PASS +2** | **PASS +2** | **112/112** | 1 |
| V-01 | 50 | 30 | 28 | PASS +2 | FAIL +0 | **110/112** | 2 (tie) |
| V-02 | 50 | 30 | 28 | FAIL +0 | PASS +2 | **110/112** | 2 (tie) |
| V-03 | 50 | 30 | 28 | FAIL +0 | PASS +2 | **110/112** | 2 (tie) |
| V-04 | 50 | 30 | 28 | FAIL +0 | FAIL +0 | **108/112** | 5 |

**All predicted scores confirmed exactly.**

---

## Failure Trap Validation

| Trap | Evidence | Confirmed? |
|------|----------|------------|
| "C-21 count satisfies C-24" | V-01: 4-op CONSTRAINT passes C-21 but leaves artifact write phase open; C-24 FAILS | YES — V-01 |
| "C-19 awarded as C-23 (CONSTRAINT form)" | V-02: dual-gate form intact (C-19 PASS) but CONSTRAINT is pre-gate surface (C-23 FAIL) | YES — V-02 |
| "C-19 awarded as C-23 (intro prose form)" | V-03: preamble gate before table (C-19 PASS) but intro sentence precedes gate (C-23 FAIL) | YES — V-03 |

All three R6 failure traps confirmed by distinct variates.

---

## Excellence Signals from V-05 (112/112)

**Signal 1 — Declarative preamble gate form satisfies C-23:**
"This step emits first. Write the TOPICS.md status line before any other work begins." — declarative/affirmative framing ("This step emits first") rather than imperative prohibition ("Before any other step begins, emit..."). Both satisfy C-23 because both position the emit requirement as the absolute first content of S-0. C-23 is content-based (zero pre-gate surface) not phrasing-based (canonical imperative form). Form-independence of C-23 confirmed.

**Signal 2 — 5-op synonym CONSTRAINT closes all production phases:**
"No lookup of skill categories. No skill-id resolution. No mock content generation. No artifact body construction. No artifact path assembly or file output." — five distinct production phases prohibited using synonym vocabulary without repeating canonical C-15 phrasings. Confirms C-24 is phase-coverage-based: discovery → decision → generation → content → output phases must be covered, but any unambiguous operation-type name closes the phase. The "artifact path assembly or file output" synonym is equivalent to "artifact path construction or file write."

**Signal 3 — Synonym tier-carry language preserves C-18 and C-20:**
"Forward the resolved tier to S-2 and S-3" (standalone) + "Propagates to S-2 and S-3" (table cell) — both synonym forms name both downstream consumers explicitly. Confirms the contract is consumer-naming, not verb-specific.

---

## Round 6 Summary

- **Predicted scores matched actual scores exactly** for all 5 variates
- V-04 (R5 baseline) scores 108/112 under v6 — correctly documents the baseline
- Three boundary variates each score 110/112, each losing exactly one criterion as predicted
- V-05 (convergent) scores 112/112 — all 24 criteria satisfied via form-variant language
- No unexpected scoring behaviors observed; rubric v6 discriminates exactly where intended

---

```json
{"top_score": 112, "all_essential_pass": true, "new_patterns": ["Declarative preamble gate form ('This step emits first') satisfies C-23 confirming the criterion is content-based not phrasing-based -- zero pre-gate surface area can be achieved with any sentence that makes the emit the first content of S-0, including affirmative declarative forms", "5-op synonym CONSTRAINT closes C-24 without canonical op-type names confirming C-24 is phase-coverage-based -- the five production phases (discovery/decision/generation/content/output) can be closed by any unambiguous operation-type description regardless of exact vocabulary"]}
```
