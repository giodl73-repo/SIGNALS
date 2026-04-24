## Round 10 Scoring — `topic:plan` (v9 rubric, C-01–C-35)

---

### V-01 — Universal Closed-Enum at Both Declaration Sites

**Axis**: Universal enum lock, C-34 isolated

| Tier | Criterion | Result | Evidence |
|------|-----------|--------|---------|
| Essential | C-01 Read strategy | PASS | Step 1a reads strategy.md, extracts 5 fields |
| Essential | C-02 Read signals | PASS | Step 2 globs and reads all artifacts |
| Essential | C-03 Delta not inventory | PASS | Step 3 "stop and name the anti-pattern" |
| Essential | C-04 Typed proposals | PASS | Type column mandatory in Step 6 |
| Essential | C-05 Confirm gate | PASS | Step 8 "Reply YES" |
| Recommended | C-06 Evidence per change | PASS | Evidence column in proposals |
| Recommended | C-07 Before/after diff | PASS | Step 7 diff table |
| Recommended | C-08 All three types | PASS | Verbatim null rows for each type |
| Aspirational | C-09 Namespace gaps | PASS | Step 4 lists all 9 by name |
| Aspirational | C-10 Conflicting signals | PASS | Step 5 conflict audit |
| Aspirational | C-11 Typed confirmation verb | PASS | "Reply YES" |
| Aspirational | C-12 Explicit no-change rows | PASS | Verbatim null rows reproduced |
| Aspirational | C-13 Inline evidence in diff | PASS | "[file.md — ≤10 word finding]" in Step 7 |
| Aspirational | C-14 Anti-inventory warning | PASS | Step 3 stop+name |
| Aspirational | C-15 All 9 namespaces named | PASS | Step 4 table with all 9 rows |
| Aspirational | C-16 Two-level traceability | PASS | Delta Finding + Evidence in Step 6 |
| Aspirational | C-17 Explicit no-conflicts | PASS | CF-00 verbatim null row |
| Aspirational | C-18 Structured delta format | PASS | "Strategy assumed [X] / Signal revealed [Y]" |
| Aspirational | C-19 Diff Proposal ID col | PASS | Proposal column in Step 7 (committed) |
| Aspirational | C-20 Delta Finding col | PASS | Delta Finding mandatory + null rows |
| Aspirational | C-21 Column-completeness declaration | PASS | "Do not omit any column" at every table |
| Aspirational | C-22 Active anti-pattern checkpoint | PASS | Step 3 stop+name |
| Aspirational | C-23 Pre-reproduced null templates | PASS | All null outcomes provided verbatim |
| Aspirational | C-24 Unstated assumption extraction | PASS | Step 1b with scan dimensions (a–e) |
| Aspirational | C-25 Inertia cost column | PASS | "If unchanged" column present |
| Aspirational | C-26 Schema-first priming | PASS | Full upfront schema before Step 1 |
| Aspirational | C-27 Cascade checkpoints | PASS | Steps 3+6+7 commitment statements |
| Aspirational | C-28 Named role + scan dimensions | **PARTIAL** | Scan (a–e) listed but no named Archaeologist role |
| Aspirational | C-29 Back-fill column | PASS | "Contradicted by a signal?" + back-fill instruction |
| Aspirational | C-30 Forward-reasoning columns | PASS | "Why this matters" + "Delta candidate?" |
| Aspirational | C-31 Decision-gate framing | **FAIL** | Commitment says "preference, not a decision" but column header itself only says "specific degradation — not a delta finding synonym"; disqualification rule not adjacent to template definition |
| Aspirational | C-32 Reversibility taxonomy | PASS | Three-value enum in upfront schema + Step 6 commitment with prose-prohibition |
| Aspirational | C-33 Full assumption table in upfront schema | **FAIL** | Five columns present but "Implicit evidence" absent — replaced by "What assumed without writing" (the assumption itself, not evidence) |
| Aspirational | C-34 Universal closed-enum at both sites | **PASS** | All 4 enumerated columns (Delta candidate?, Consistent with strategy?, Type, Reversibility) carry closed values + prose-prohibition in upfront schema; Step 6 commitment reproduces Type and Reversibility with selectors |
| Aspirational | C-35 Column independence | **FAIL** | No independence rule; upfront schema names assumption table but no disqualification condition for row-key aliasing |

**V-01 Aspiration passes**: 23.5/27 (C-31 fail, C-33 fail, C-35 fail, C-28 partial = 0.5)
**V-01 Score**: (5/5 × 60) + (3/3 × 30) + (23.5/27 × 135) = 60 + 30 + **117.5 = 207.5**

---

### V-02 — Implicit Evidence Column Independence Rule

**Axis**: Lifecycle emphasis, C-35 isolated

| Tier | Criterion | Result | Evidence |
|------|-----------|--------|---------|
| Essential | C-01–C-05 | PASS (all) | Step 1/2/3/6/8 all present |
| Recommended | C-06–C-08 | PASS (all) | Evidence col, diff, all three types |
| Aspirational | C-09–C-27 | PASS (all) | All mechanisms present |
| Aspirational | C-28 Named role + scan dimensions | **PARTIAL** | Neither named role nor explicit scan dimensions in V-02 Step 1; archaeology framing present in Implicit evidence column rule but no structured dimension list |
| Aspirational | C-29 Back-fill column | PASS | "Contradicted by a signal?" in upfront schema + back-fill instruction |
| Aspirational | C-30 Forward-reasoning columns | PASS | "Why this matters" + "Delta candidate?" in upfront schema |
| Aspirational | C-31 Decision-gate framing | PASS | "a row that cannot name a specific degradation is a preference, not a decision" in Step 6 commitment and column template |
| Aspirational | C-32 Reversibility taxonomy | PASS | Three-value enum in upfront schema + Step 6 column header |
| Aspirational | C-33 Full assumption table in upfront schema | PASS | Implicit evidence column with independence rule in upfront schema annotation |
| Aspirational | C-34 Universal closed-enum at both sites | **FAIL** | Only Reversibility carries closed enum in upfront schema; "Consistent with strategy?" named without [Yes/No/Partial] in schema; "Delta candidate?" named without [yes/no]; commitment checkpoint names these columns without their value lists |
| Aspirational | C-35 Column independence | PASS | Three fail examples + one pass example at both upfront schema annotation and Step 1 extraction; "row-key aliasing" anti-pattern named |

**V-02 Aspiration passes**: 25.5/27 (C-34 fail, C-28 partial = 0.5)
**V-02 Score**: (5/5 × 60) + (3/3 × 30) + (25.5/27 × 135) = 60 + 30 + **127.5 = 217.5**

---

### V-03 — Pre-Schema COLUMN CONTRACT with Decision-Question Independence Test

**Axis**: Phrasing register (unified CONTRACT), C-34 + C-35

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-05 | PASS (all) | All essential steps present |
| C-06–C-08 | PASS (all) | Recommended all covered |
| C-09–C-27 | PASS (all) | All prior mechanisms present |
| C-28 | PASS | Named Archaeologist role (Step 1b) + scan dimensions (a–e) |
| C-29 | PASS | Named Step 2b back-fill lifecycle + verdict-per-row rule |
| C-30 | PASS | "Why this matters" + "Delta candidate?" in upfront schema + Step 1b |
| C-31 | PASS | "a row that cannot name one is a preference, not a decision" in column header template |
| C-32 | PASS | Three-value enum in upfront schema + commitment reproduced at Step 6 with Rule 1 reference |
| C-33 | PASS | Implicit evidence column in upfront schema with Rule 2 decision-question test |
| C-34 | **PASS** | COLUMN CONTRACT Rule 1 declares closed-enum obligation universally before schema; upfront schema carries all four enumerated columns with closed values; Step 6 commitment reproduces Type and Reversibility with Rule 1 reference |
| C-35 | **PASS** | COLUMN CONTRACT Rule 2 with decision-question independence test ("Can I fill this without reading the source document?"); Implicit evidence column annotation carries the test + fail/pass distinction |

**V-03 Aspiration passes**: 27/27
**V-03 Score**: (5/5 × 60) + (3/3 × 30) + (27/27 × 135) = 60 + 30 + **135 = 225**

---

### V-04 — Universal Enum Lock + Implicit Evidence Independence Rule

**Axis**: Combination (V-01 + V-02 mechanisms, no COLUMN CONTRACT wrapper)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-05 | PASS (all) | All essential steps present |
| C-06–C-08 | PASS (all) | Recommended all covered |
| C-09–C-27 | PASS (all) | Role sequence, cascade checkpoints, all mechanisms |
| C-28 | PASS | Named Archaeologist role (Step 1b) + scan dimensions (a–e) |
| C-29 | PASS | Upfront schema + named Step 2b back-fill |
| C-30 | PASS | Forward-reasoning columns present + updated post-Step 3 |
| C-31 | PASS | Adjacent disqualification rule + committed in Step 6 |
| C-32 | PASS | Three-value enum in upfront schema + Step 6 commitment reproduced |
| C-33 | PASS | Implicit evidence column in upfront schema with independence rule + fail/pass examples |
| C-34 | **PASS** | All four enumerated columns (Delta candidate? [yes/no], Consistent with strategy? [Yes/No/Partial], Type [ADD/REMOVE/REPRIORITIZE], Reversibility [(1)/(2)/(3)]) carry closed enums in upfront schema; Step 6 commitment reproduces Type and Reversibility with prose-prohibition |
| C-35 | **PASS** | Upfront schema Implicit evidence annotation carries independence rule with fail/pass examples; Step 1b extraction names three fail patterns and one pass pattern explicitly |

**V-04 Aspiration passes**: 27/27
**V-04 Score**: 60 + 30 + 135 = **225**

---

### V-05 — Full Stack

**Axis**: All R9 V-05 mechanisms + COLUMN CONTRACT + universal enum lock + column independence contract + extraction anti-patterns

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01–C-05 | PASS (all) | All essential steps |
| C-06–C-08 | PASS (all) | Recommended all covered |
| C-09–C-27 | PASS (all) | Complete R9 V-05 ceiling architecture |
| C-28 | PASS | Archaeologist role + scan (a–f, extended) |
| C-29 | PASS | Named Step 2b + verdict-per-row |
| C-30 | PASS | Forward-reasoning columns + F-NN update |
| C-31 | PASS | Adjacent rule + committed; "a row that cannot commit has not reasoned about the deferral window" |
| C-32 | PASS | Three-value enum in upfront schema AND Step 6 commitment with disqualification framing |
| C-33 | PASS | Implicit evidence in upfront schema with fail/pass examples + Rule 2 |
| C-34 | **PASS** | COLUMN CONTRACT Rule 1 + all four enumerated columns in upfront schema + Step 6 commitment names all four with valid-value selectors and prose-prohibition ("same values as upfront schema") |
| C-35 | **PASS** | COLUMN CONTRACT Rule 2 + upfront schema fail/pass examples (A-01 FAILS, "first run scout" FAILS, "see rationale" FAILS; "teams run scout before draft" PASSES) + Step 1b archaeology obligation with traceability test |

**V-05 Aspiration passes**: 27/27
**V-05 Score**: 60 + 30 + 135 = **225**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Golden? |
|-----------|-----------|-------------|--------------|-------|---------|
| V-01 | 60 | 30 | 117.5 (23.5/27) | **207.5** | Yes (>130) |
| V-02 | 60 | 30 | 127.5 (25.5/27) | **217.5** | Yes |
| V-03 | 60 | 30 | 135 (27/27) | **225** | Yes (ceiling) |
| V-04 | 60 | 30 | 135 (27/27) | **225** | Yes (ceiling) |
| V-05 | 60 | 30 | 135 (27/27) | **225** | Yes (ceiling) |

---

## Ranking

1. **V-03, V-04, V-05** — 225/225 (tied at ceiling)
2. **V-02** — 217.5 (C-34 fail: "Consistent with strategy?" and "Delta candidate?" carry no closed-enum annotation in upfront schema or commitment)
3. **V-01** — 207.5 (C-31 fail: disqualification rule in commitment but not in column template; C-33 fail: "Implicit evidence" column absent from assumption table; C-35 fail: no independence rule)

**Key differentiator V-01 vs V-02**: V-01 wins C-34 (universal enum) but drops C-31, C-33, C-35. V-02 wins C-31, C-33, C-35 but drops C-34. The combination (V-04) passes both.

**Key differentiator V-03/V-04/V-05 vs V-01/V-02**: The top tier closes every gap by combining: (a) the COLUMN CONTRACT structural governance block or equivalent per-column coverage, (b) the named Archaeologist role + scan dimensions for C-28, (c) the disqualification rule adjacent to the column template for C-31.

**Within the tie (V-03 vs V-04 vs V-05)**:
- V-03 achieves parity through the COLUMN CONTRACT framing alone — a single pre-schema block replaces scattered per-column annotations, making it the most architecturally compact
- V-04 achieves parity through explicit per-column mechanism combination (V-01+V-02) — more verbose but each mechanism is independently verifiable
- V-05 subsumes all prior mechanisms — highest redundancy, highest resilience under context pressure, adds a sixth scan dimension and traceability obligation

For extraction purposes: **V-05 is the recommended new ceiling** because the COLUMN CONTRACT + extraction anti-patterns survive partial context attention better than equivalent per-column annotations; V-03 is the minimal sufficient form for both C-34 and C-35.

---

## Excellence Signals — Patterns from the Top Tier

**Signal 1 — COLUMN CONTRACT as a structural governance block before the output schema**
V-03 and V-05 introduce a named `### COLUMN CONTRACT` section placed *before* the output schema declaration. This block states two rules using binding language ("A cell that passes this test contains a structural alias — it is derived from the row identifier... and is treated as absent regardless of the text it contains"). The structural effect: both C-34 (enumerated columns) and C-35 (column independence) become pre-reading commitments that the model holds before encountering any schema definition or step instruction. V-04 achieves equivalent coverage through per-column annotations but the CONTRACT framing is more resilient — it front-loads the governance before the model's context is consumed by schema detail.

**Signal 2 — Decision-question independence test as a generative procedure**
V-03 and V-05 replace a list of named fail examples with a self-executable question: *"Can this cell be filled correctly without reading the source document?"* This is more portable than fail-example enumeration: a model that has internalized the question applies it to any column at any step without needing to match against a specific known failure mode. V-02 and V-04 use named examples (three fails, one pass), which are more concrete but less generalizable. Both approaches pass C-35; the decision-question form is the new architectural primitive.

**Signal 3 — Universal enum lock at both declaration sites closes the partial-compliance gap**
R9 applied the closed-enum lock to Reversibility only. R10 V-01/V-03/V-04/V-05 extend it to all four enumerated columns. The critical gap R9 left: "Consistent with strategy?" and "Delta candidate?" in the Signal Inventory and Assumption Table were declared by column name in the upfront schema but without their value lists — a model could write "Mostly yes" or "probably" and satisfy C-26 (column declared) while violating C-32's spirit. The universal extension makes prose-fill detectable at any column, not just Reversibility.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["Pre-schema COLUMN CONTRACT block with two named binding rules (Rule 1: closed-enum at every declaration site; Rule 2: column-independence test) placed before the output schema, converting C-34 and C-35 into pre-reading structural commitments rather than per-column annotations encountered under context pressure", "Decision-question independence test -- 'Can this cell be filled correctly without reading the source document?' -- as a generative self-applicable procedure that replaces specific fail-example enumeration, extending column independence enforcement to any column without requiring named failure modes", "Universal closed-enum extension from single column (Reversibility) to all four enumerated columns (Delta candidate?, Consistent with strategy?, Type, Reversibility) at both the upfront schema and each schema-commitment checkpoint, closing prose-fill in columns that were previously declared by name only"]}
```
