## Round 5 Scorecard — topic-open (v5 rubric)

**Scoring**: essential 5×12pt = 60 | recommended 3×10pt = 30 | aspirational 16×0.625pt = 10

---

### V-01 — Phase-Pervasive Tool Citation

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4 Write 1 instructs append to `simulations/TOPICS.md` |
| C-02 | PASS | Phase 4 Write 2 instructs write to `simulations/{topic}/strategy.md` |
| C-03 | PASS | FIELD SCHEMA defines F-01–F-05; Phase 2 says "Apply F-01 through F-05 to every row" |
| C-04 | PASS | VOCABULARY LOCK specifies exactly `essential` / `recommended` / `optional` |
| C-05 | PASS | Phase 2 Exit Gate COV-01 requires >= 1 `essential` row |
| C-06 | PASS | Phase 2 Exit Gate COV-02 requires >= 2 distinct namespaces |
| C-07 | PASS | Phase 2 requires rationale >= 2 sentences |
| C-08 | PASS | Phase 2 Exit Gate COV-03 requires >= 2 distinct owner roles |
| C-09 | PASS | Phase 3 defines isolated `## COMMIT GATE` section with named essential signals |
| C-10 | PASS | F-04 and Phase 2 Exit Gate both specify `{topic}-{signal}-{date}.md` |
| C-11 | PASS | VOCABULARY LOCK is a standalone block preceding all instruction phases |
| C-12 | PASS | Phase 5 Post-Generation Self-Check: checkbox list with C-01–C-05 items |
| C-13 | PASS | "AMEND — PRIORITY DRIFT: list each row with drift. Re-scan all priority cells before marking C-04 passing" |
| C-14 | PASS | "Wrong vocabulary = silent breakage. This is the most common mistake." + `topic-status` exact string consequence named |
| C-15 | PASS | Phase 2 Decision table and Phase 2 body both enforce rationale-first order |
| C-16 | PASS | ROW TEMPLATE `| {topic-slug} | {one-line description…} | {YYYY-MM-DD} |` provided inline |
| C-17 | PASS | Phase 2 Decision table: "Owner roles emerge from decision context; each role is accountable to a named question" |
| C-18 | PASS | "> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: `{YYYY-MM-DD}` date field is the most commonly dropped" |
| C-19 | PASS | CONSTRAINT SURFACE: all 5 rows name `topic-status` or `topic-scanner` with specific failure modes |
| C-20 | PASS | Phase 2 Decision table contrasts compliant/non-compliant paths explicitly |
| C-21 | PASS (deep) | 7 sites: Phase 1 setup cites `topic-status`; Phase 2 Exit Gate items each cite tool; Phase 3 cites `topic-status`; Phase 4 cites both tools; Phase 5 checklist annotates every item with tool name |
| C-22 | PASS (min) | VOCABULARY LOCK: "If you read this block first… / If you skip this block…" — comparative framing on priority instruction |
| C-23 | PASS (min) | Phase 2 Decision: Content Order table precedes Phase 2 instruction body |
| C-24 | PASS | CONSTRAINT SURFACE: Rule \| Rationale \| What Breaks \| Tool — 4-column unified block covering all 5 constraints |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 16/16
**Score**: 60 + 30 + 10 = **100/100**

---

### V-02 — Recursive Meta-Comparative Framing

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4 Write 1 |
| C-02 | PASS | Phase 4 Write 2 |
| C-03 | PASS | F-01–F-05 defined; Phase 2 applies all |
| C-04 | PASS | VOCABULARY LOCK |
| C-05 | PASS | Phase 2 Exit Gate COV-01 |
| C-06 | PASS | COV-02 |
| C-07 | PASS | >= 2 sentence rationale required |
| C-08 | PASS | COV-03 |
| C-09 | PASS | Phase 3 isolated commit gate |
| C-10 | PASS | F-04 item naming |
| C-11 | PASS | VOCABULARY LOCK standalone before phases |
| C-12 | PASS | Phase 5 self-check |
| C-13 | PASS | AMEND — PRIORITY DRIFT |
| C-14 | PASS | "Wrong vocabulary = silent downstream breakage. Most common mistake." |
| C-15 | PASS | Phase 2 Decision table + body comparative framing on order |
| C-16 | PASS | ROW TEMPLATE present |
| C-17 | PASS | Phase 2 body: "If you write the rationale first: the decisions you describe surface the question 'who should own this signal?'" |
| C-18 | PASS | "> **COPY — DO NOT RECONSTRUCT.**" |
| C-19 | PASS | CONSTRAINT SURFACE table with Tool column |
| C-20 | PASS | Phase 2 Decision table + Phase 2 body both have if/if contrast |
| C-21 | PASS (min) | Phase 1: "because `topic-status` loads this file on every status check; a duplicate entry creates ambiguous coverage aggregation" |
| C-22 | PASS (deep) | Four ordering instructions each use comparative framing: VOCABULARY LOCK ("If you read… / If you skip and read the schema first"), ROW TEMPLATE ("If you copy… / If you reconstruct from memory"), Phase 2 body ("If you write the rationale first… / If you write the signal table first"), Phase 5 timing ("If you run this check after writing… / If you run this check before writing") |
| C-23 | PASS (min) | Phase 2 Decision: Narrative Order table |
| C-24 | PASS | CONSTRAINT SURFACE: Rule \| Rationale \| What Breaks \| Tool |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 16/16
**Score**: 60 + 30 + 10 = **100/100**

---

### V-03 — Labeled Decision Tables at All Phase Transitions

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4 Write 1 |
| C-02 | PASS | Phase 4 Write 2 |
| C-03 | PASS | F-01–F-05 |
| C-04 | PASS | VOCABULARY LOCK |
| C-05 | PASS | COV-01 |
| C-06 | PASS | COV-02 |
| C-07 | PASS | >= 2 sentence rationale |
| C-08 | PASS | COV-03 |
| C-09 | PASS | Isolated commit gate |
| C-10 | PASS | F-04 naming |
| C-11 | PASS | VOCABULARY LOCK standalone |
| C-12 | PASS | Phase 5 self-check |
| C-13 | PASS | AMEND — PRIORITY DRIFT |
| C-14 | PASS | "Wrong vocabulary = silent breakage." |
| C-15 | PASS | Phase 2 Decision: Content Order enforces rationale-first |
| C-16 | PASS | ROW TEMPLATE present |
| C-17 | PASS | Phase 2 Decision table: "Owner roles emerge from the decisions described in the rationale — each role is the stakeholder accountable" |
| C-18 | PASS | "> **COPY — DO NOT RECONSTRUCT.**" |
| C-19 | PASS | CONSTRAINT SURFACE + FIELD SCHEMA name tools; Phase 1 Decision table names `topic-status` in consequence column |
| C-20 | PASS | Phase 2 Decision table; Phase 3 Decision table; Phase 4 Decision table; Phase 5 Decision table — all contrast both paths |
| C-21 | PASS (min) | Phase 1 setup cites `topic-status`; Phase 1 Decision table consequence column names `topic-status` |
| C-22 | PASS (min) | VOCABULARY LOCK: "If you read this block first… / If you skip this block…" |
| C-23 | PASS (deep) | All five phases have named decision tables: Phase 1 Decision: Collision Check; Phase 2 Decision: Content Order; Phase 3 Decision: Gate Structure; Phase 4 Decision: Output Write; Phase 5 Decision: Check Timing |
| C-24 | PASS | CONSTRAINT SURFACE: 4-column unified block covering all 5 constraints |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 16/16
**Score**: 60 + 30 + 10 = **100/100**

---

### V-04 — Pervasive Tool Citation + Recursive Comparative Framing

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4 Write 1 |
| C-02 | PASS | Phase 4 Write 2 |
| C-03 | PASS | F-01–F-05; Phase 2 cites tools for each check |
| C-04 | PASS | VOCABULARY LOCK |
| C-05 | PASS | COV-01 |
| C-06 | PASS | COV-02 |
| C-07 | PASS | >= 2 sentence rationale |
| C-08 | PASS | COV-03 |
| C-09 | PASS | Phase 3 isolated commit gate |
| C-10 | PASS | F-04 + Phase 2 Exit Gate item naming |
| C-11 | PASS | VOCABULARY LOCK standalone |
| C-12 | PASS | Phase 5 self-check with tool annotations |
| C-13 | PASS | AMEND — PRIORITY DRIFT |
| C-14 | PASS | "Wrong vocabulary = silent breakage. Most common mistake." |
| C-15 | PASS | Phase 2 Decision + body enforce rationale-first |
| C-16 | PASS | ROW TEMPLATE present |
| C-17 | PASS | Phase 2 body: "owner roles in the table emerge as stakeholders accountable to the decisions you named. `topic-status` and coverage review can verify each role" |
| C-18 | PASS | "> **COPY — DO NOT RECONSTRUCT.**" |
| C-19 | PASS | CONSTRAINT SURFACE names tools; FIELD SCHEMA names tools; Phase 2 Exit Gate items each cite tools |
| C-20 | PASS | Phase 2 Decision; Phase 2 body; Phase 3 body; Phase 4 body; Phase 5 body — all have if/if comparative framing |
| C-21 | PASS (deep) | Every phase names its tool: Phase 1 ("topic-status loads…"); Phase 2 body ("topic-status parses all five… topic-scanner uses Item Name"); Phase 3 ("`topic-status` reads it / section parser cannot find"); Phase 4 (tool in both copy/reconstruct branches and correct/flat path branches); Phase 5 checklist every item names tool |
| C-22 | PASS (deep) | VOCABULARY LOCK names `topic-status` in BOTH comparative branches ("topic-status will find the correct vocabulary" / "topic-status will silently exclude those signals"); ROW TEMPLATE names tool in both branches ("topic-status date filter will exclude"); Phase 3 names tool in both branches; Phase 4 names tool in both path descriptions |
| C-23 | PASS (min) | Phase 2 Decision: Content Order table |
| C-24 | PASS | CONSTRAINT SURFACE: Rule \| Rationale \| What Breaks \| Tool — 4-column unified block |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 16/16
**Score**: 60 + 30 + 10 = **100/100**

---

### V-05 — Decision Tables + Unified Constraint Matrix

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 4 Write 1 |
| C-02 | PASS | Phase 4 Write 2 |
| C-03 | PASS | F-01–F-05 |
| C-04 | PASS | VOCABULARY LOCK |
| C-05 | PASS | Phase 2 Exit Gate COV-01 |
| C-06 | PASS | COV-02 |
| C-07 | PASS | >= 2 sentence rationale |
| C-08 | PASS | COV-03 |
| C-09 | PASS | Phase 3 isolated commit gate; Phase 3 Decision table |
| C-10 | PASS | F-04 naming |
| C-11 | PASS | VOCABULARY LOCK standalone |
| C-12 | PASS | Phase 5 self-check |
| C-13 | PASS | AMEND — PRIORITY DRIFT |
| C-14 | PASS | "Wrong vocabulary = silent downstream breakage." |
| C-15 | PASS | Phase 2 Decision: Content Order + body |
| C-16 | PASS | ROW TEMPLATE present |
| C-17 | PASS | Phase 2 Decision: "Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered" |
| C-18 | PASS | "> **COPY — DO NOT RECONSTRUCT.**" |
| C-19 | PASS | DEFAULTS TABLE Tool column; FIELD SCHEMA names tools; Phase 1 Decision consequence column names `topic-status` |
| C-20 | PASS | All 5 phase Decision tables contrast both paths; DEFAULTS TABLE has "What Breaks If You Skip" column |
| C-21 | PASS (min) | Phase 1 setup: "because `topic-status` loads this file on every status check; a duplicate entry creates ambiguous coverage aggregation." Phase 1 Decision table consequence names `topic-status` |
| C-22 | PASS (min) | VOCABULARY LOCK: "If you read this block first… / If you skip this block…" — comparative framing on vocab block's reading-order instruction |
| C-23 | PASS (deep) | All 5 phase Decision tables present: Phase 1 Decision: Collision Check; Phase 2 Decision: Content Order; Phase 3 Decision: Gate Structure; Phase 4 Decision: Output Write; Phase 5 Decision: Check Timing |
| C-24 | PASS (deep) | DEFAULTS THIS SKILL OVERRIDES: Default \| Rule \| Why \| What Breaks If You Skip \| Tool — true 5-column table, all 5 constraints in one block |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 16/16
**Score**: 60 + 30 + 10 = **100/100**

---

### Ranking

| Rank | Variation | Score | Distinguishing Strength |
|------|-----------|-------|------------------------|
| 1 (tie) | V-01 | 100 | Deepest C-21: tool citation at 7 sites including Phase 5 checklist annotations |
| 1 (tie) | V-02 | 100 | Deepest C-22: comparative framing on all 4 ordering instructions |
| 1 (tie) | V-03 | 100 | Deepest C-23: all 5 phases have labeled decision tables |
| 1 (tie) | V-04 | 100 | C-21+C-22 fused: tool named in BOTH branches of every comparative frame |
| 1 (tie) | V-05 | 100 | C-23+C-24 integrated: 5-column DEFAULTS TABLE + all-phase decision tables |

All five variations score 100/100. The denominator update from 12→16 did not break the ceiling — every variation was designed to cover all four new criteria at minimum, and each deep-axis variation exceeded the minimum on its target criteria.

---

### Excellence Signals

**V-04's fusion pattern — tool-integrated comparative framing**: C-21 and C-22 are applied simultaneously at the instruction level. In V-04's VOCABULARY LOCK, `topic-status` appears in BOTH the compliant branch ("topic-status will find the correct vocabulary in every cell") AND the non-compliant branch ("topic-status will silently exclude those signals"). This is distinct from V-01 (tool citations in separate annotations) and V-02 (comparative framing without tool names in the branches). The fusion means every contrast is tool-witnessed on both sides — the tool is not just the victim of the wrong path but the observer of both outcomes. No current criterion captures this: C-21 requires tool citation in phases; C-22 requires comparative framing on the vocab block; neither requires the tool to appear inside both comparative branches simultaneously.

**V-05's default-naming column — constraint-as-override framing**: The DEFAULTS TABLE's first column explicitly names what behavior the rule is correcting ("Any priority vocabulary," "Free-form TOPICS.md row," "Table before rationale," "Inline commit gate," "Any strategy file location"). This makes each constraint visible as a correction to a natural AI default rather than a stand-alone prohibition. C-24 requires the unified table to have rule + rationale + consequence + tool columns — it does NOT require a column naming the unconstrained behavior being overridden. The "Default" column surfaces the model's prior assumption, making the contrast between natural behavior and required behavior explicit at the constraint level, not just at the phase level.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Tool-integrated comparative framing: tool citations embedded inside both branches of every comparative frame (not just in consequence annotations), so the named tool witnesses both the compliant outcome and the non-compliant failure simultaneously", "Default-naming column in constraint tables: an explicit 'Default' column (or equivalent) that names the unconstrained AI behavior each rule overrides, making every constraint visible as a correction to a prior assumption rather than a stand-alone prohibition"]}
```
