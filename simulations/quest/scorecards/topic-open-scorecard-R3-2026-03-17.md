## topic-open Round 3 — Scoring

### Criteria Evaluation

#### V-01 — Template Lock (C-16 focus)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | TOPICS.md ROW TEMPLATE block with `{topic-slug}`, `{one-line description}`, `{YYYY-MM-DD}`; Phase 4 Write 1 says "return here and copy it — do not reconstruct" |
| C-02 | **PASS** | "Write `simulations/{topic}/strategy.md`" explicit |
| C-03 | **PASS** | Field Schema F-01 through F-05; Phase 2 Exit Gate checks all five |
| C-04 | **PASS** | VOCABULARY LOCK block first; silent-gate failure consequence stated |
| C-05 | **PASS** | COV-01 stated; Phase 2 Exit Gate checks it |
| C-06 | **PASS** | COV-02: ≥ 2 distinct namespaces in Field Schema and Exit Gate |
| C-07 | **PASS** | Phase 2: ≥ 2 sentences rationale, both why + decision |
| C-08 | **PASS** | COV-03: ≥ 2 distinct owner roles stated |
| C-09 | **PASS** | Phase 3 with structurally isolated `## COMMIT GATE` block |
| C-10 | **PASS** | F-04 Item Name: `{topic}-{signal}-{date}.md` |
| C-11 | **PASS** | VOCABULARY LOCK preceded by "Read this block before reading anything else in this skill" |
| C-12 | **PASS** | Phase 5 Post-Generation Self-Check with C-01 through C-05 checkbox items |
| C-13 | **PASS** | "PRIORITY DRIFT AMEND: If any row has `high`, `medium`, `low`… re-scan all priority cells before marking C-04 passing" |
| C-14 | **PASS** | "commit gate silently fail — no error, no warning… The Design Lead never learns" — full consequence chain |
| C-15 | **PASS** | "Owner roles should emerge from decisions described in the rationale. Writing first means roles derive from purpose; writing after means column-fillers" |
| C-16 | **PASS** | Named `TOPICS.md ROW TEMPLATE` block, physically separated, all three fields; referenced again at Phase 4 Write 1 with explicit back-reference |
| C-17 | **PASS** | Phase 2 explains *why*: "Writing the rationale first means roles derive from purpose; writing it after means roles are column-fillers" — causal, not merely positional |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 9/9**
**Composite: 60 + 30 + 10 = 100**

---

#### V-02 — Causal Sequencing (C-17 focus)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Phase 4 inline template with all three fields; "use this exact template, because a reconstructed template drifts from the canonical three-field format" |
| C-02 | **PASS** | "write to `simulations/{topic}/strategy.md` (not a flat path, not inline in TOPICS.md) — because topic-status and topic-scanner glob for this specific path" |
| C-03 | **PASS** | Field Schema: five fields listed with downstream parse justification |
| C-04 | **PASS** | VOCABULARY LOCK; silent-gate consequence stated |
| C-05 | **PASS** | "≥ 1 row marked `essential` — without this there is no commit gate; the topic has no defined finish line" |
| C-06 | **PASS** | "≥ 2 distinct namespaces — prevents monoculture investigations" |
| C-07 | **PASS** | Step A: ≥ 2 sentences, both why + design decisions |
| C-08 | **PASS** | "≥ 2 distinct owner roles — ensures accountability is distributed" |
| C-09 | **PASS** | Phase 3 COMMIT GATE with causal rationale for timing |
| C-10 | **PASS** | Item Name: `{topic}-{signal}-{date}.md` in Field Schema |
| C-11 | **PASS** | VOCABULARY LOCK: "This block is first in the skill — before schema, before phases, before everything — because priority vocabulary errors corrupt all downstream automation silently" |
| C-12 | **PASS** | Phase 5 Post-Generation Self-Check C-01 through C-05 |
| C-13 | **PASS** | "AMEND — PRIORITY DRIFT: Triggered by any C-04 failure. List each failing row. Replace. Re-scan. Re-run C-04 check before marking passing" |
| C-14 | **PASS** | "`high` does not match `essential` in string comparison. The commit gate silently fails — no error, just no gate. The Design Lead never detects missing signals" |
| C-15 | **PASS** | Step A: "because owner roles should emerge from decisions… not retrospective column-filling"; Step B repeats the causal chain |
| C-16 | **PASS** | Inline template in Phase 4 with all three canonical fields including `{YYYY-MM-DD}`; "use this exact template" + "do not reconstruct" |
| C-17 | **PASS** | Pervasive causal density: vocab placement ("because priority errors corrupt silently"), rationale→table ("because the rationale answers 'who should care'"), Phase 3 timing ("because the commit gate is defined by essential signals"), Phase 5 timing ("because this check tests what you produced, not what you planned") |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 9/9**
**Composite: 60 + 30 + 10 = 100**

---

#### V-03 — Conversational Register + Full Coverage

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "The TOPICS.md Row" named section before steps; template with all three fields; "The date is not optional"; Step 5 copies it again; Step 6 Q1 verifies |
| C-02 | **PASS** | "File 2 — strategy.md: Write to `simulations/{topic}/strategy.md`" |
| C-03 | **PASS** | Step 3: five-column table header, all five fields named |
| C-04 | **PASS** | "BEFORE YOU START: VOCABULARY" block |
| C-05 | **PASS** | "At least 1 row marked `essential` — without this, you have no commit gate and no defined finish line" |
| C-06 | **PASS** | "Use **at least 2 distinct namespaces**" stated twice (Step 3 rule + minimums) |
| C-07 | **PASS** | Step 2: "write 2 or more sentences explaining…" |
| C-08 | **PASS** | "At least 2 distinct owner roles" in minimums |
| C-09 | **PASS** | Step 4: `## COMMIT GATE` listing all essential signals by exact item name |
| C-10 | **PASS** | "Item Name: `{topic}-{signal}-{date}.md`" in Step 3 |
| C-11 | **PASS** | "BEFORE YOU START: VOCABULARY" — standalone block, "Before you do anything else, read this" |
| C-12 | **PASS** | Step 6: five named questions with amend redirects |
| C-13 | **PASS** | Q4: "Did any priority drift to `high`, `medium`, `low`, or anything else? → If yes — stop. List every row where it happened. Replace. Do not mark this step as done until every priority cell reads exactly `essential`, `recommended`, or `optional`" |
| C-14 | **PASS** | Strongest C-14 across all variations: "the tool does not error — it silently ignores that signal. The commit gate never fires. The Design Lead never knows the topic is missing key evidence. The file looks perfectly valid. The investigation silently stalls. That is the scenario you are preventing" |
| C-15 | **PASS** | Step 2: "Write this **before** the table — not after. Here's why: the decisions you describe determine which roles are responsible" |
| C-16 | **PASS** | Named "The TOPICS.md Row" section positioned before all steps; template with all three fields; explicit: "The date is not optional"; Step 5 repeats template with "Do not reconstruct it — copy it" |
| C-17 | **PASS** | Step 2: "Here's why: the decisions you describe in the rationale determine which roles are responsible… If you write the table first, the owner roles become post-hoc labels… If you write the rationale first, the roles emerge from the question you're trying to answer — they have a reason to exist" |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 9/9**
**Composite: 60 + 30 + 10 = 100**

---

#### V-04 — Combination: C-16 + C-17 + Full Scaffolding

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Named `TOPICS.md ROW TEMPLATE` block; Phase 4 Write 1 says "Return to the TOPICS.md ROW TEMPLATE at the top of this skill. Copy it." Template has all three fields |
| C-02 | **PASS** | "Write `simulations/{topic}/strategy.md`" |
| C-03 | **PASS** | FIELD SCHEMA F-01 through F-05; "because topic-status parses all five for coverage computation" |
| C-04 | **PASS** | VOCABULARY LOCK first block with consequence |
| C-05 | **PASS** | COVERAGE SCHEMA: "COV-01: no essential = no commit gate = no defined finish line" |
| C-06 | **PASS** | COVERAGE SCHEMA: COV-02 stated |
| C-07 | **PASS** | Phase 2: "Write NARRATIVE RATIONALE First" ≥ 2 sentences |
| C-08 | **PASS** | COVERAGE SCHEMA: COV-03 stated; "roles should derive from Phase 2 rationale" |
| C-09 | **PASS** | Phase 3 structurally isolated COMMIT GATE; causal reason given for isolation timing |
| C-10 | **PASS** | F-04: `{topic}-{signal}-{date}.md` |
| C-11 | **PASS** | VOCABULARY LOCK: "This block precedes all schema, register, and phase directives — because priority vocabulary errors corrupt downstream gating silently, and the lock must be set before any instruction can override it" |
| C-12 | **PASS** | Phase 5 Post-Generation Self-Check C-01 through C-05 |
| C-13 | **PASS** | Phase 5 AMEND: "PRIORITY DRIFT — AMEND TRIGGER: Did any row use `high`, `medium`, `low`, or any other value?" — named trigger with four-step repair protocol |
| C-14 | **PASS** | "`high` does not match `essential`. The gate silently fails — it does not error, it simply never trips. The Design Lead never detects the gap" |
| C-15 | **PASS** | Phase 2: "so owner roles emerge from the decision context rather than from post-hoc column-filling… Writing it first means the owner roles in the table have a derivable reason to exist. Writing it after means they are assigned to fill a schema requirement" |
| C-16 | **PASS** | Named `TOPICS.md ROW TEMPLATE` as second first-class named block; "Reference this template at write time. Do not reconstruct it from memory — reconstructed templates drop fields"; referenced again in Phase 4 with back-pointer; AMEND TRIGGER for date in Phase 5 |
| C-17 | **PASS** | Three named causal points: vocab placement, rationale sequencing, Phase 5 timing; Phase 3 also causal ("Written after the signal table because the commit gate is enumerated from essential signals") |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 9/9**
**Composite: 60 + 30 + 10 = 100**

---

#### V-05 — Combination Compact

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Named `TOPICS.md ROW TEMPLATE` block with all three fields; Phase 4: "Return to the ROW TEMPLATE above. Copy it… Three fields — do not omit the date" |
| C-02 | **PASS** | "Write to `simulations/{topic}/strategy.md` — not flat path" |
| C-03 | **PASS** | Phase 2 signal table headers; requirements state "priority, namespace, skill, item name, owner role" |
| C-04 | **PASS** | VOCABULARY CONSTRAINT standalone block |
| C-05 | **PASS** | "≥ 1 row `essential`" in Phase 2 requirements |
| C-06 | **PASS** | "≥ 2 distinct namespaces" with explicit namespace list in Phase 2 |
| C-07 | **PASS** | Phase 2: rationale ≥ 2 sentences with both content requirements |
| C-08 | **PASS** | "≥ 2 distinct owner roles" in Phase 2 requirements |
| C-09 | **PASS** | Phase 3 structurally isolated COMMIT GATE |
| C-10 | **PASS** | "Item Name: `{topic}-{signal}-{date}.md`" |
| C-11 | **PASS** | VOCABULARY CONSTRAINT: "Standalone block. Read before any instruction" |
| C-12 | **PASS** | Phase 5 Self-Check and Amend with C-01 through C-05 |
| C-13 | **PASS** | "AMEND — Priority Drift: If C-04 fails: identify each row with drift. Replace. Re-scan before marking C-04 passing" |
| C-14 | **PASS** | "It does not error. It stops working. The Design Lead sees a passing strategy file that is actually broken" |
| C-15 | **PASS** | Phase 2: "so owner roles emerge from decision context rather than post-hoc count enforcement. If the table comes first, owner roles become column-fillers; if the rationale comes first, they become meaningful stakeholders whose accountability derives from the decisions being described" |
| C-16 | **PASS** | Named `TOPICS.md ROW TEMPLATE` as second first-class named block; "Do not reconstruct from memory — reconstructed templates drop fields"; DEFAULTS TABLE explicitly reinforces it; referenced again in Phase 4 |
| C-17 | **PASS** | Phase 2 causal sequencing instruction; DEFAULTS TABLE "Why" column carries causal reason ("Owner roles emerge from decision context, not post-hoc column-filling") as structural override rationale |

**Essential: 5/5 · Recommended: 3/3 · Aspirational: 9/9**
**Composite: 60 + 30 + 10 = 100**

---

### Summary Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Essential | PASS | PASS | PASS | PASS | PASS |
| C-03 Essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Essential | PASS | PASS | PASS | PASS | PASS |
| C-05 Essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-09 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-13 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 Aspirational | PASS | PASS | PASS | PASS | PASS |
| **Essential** | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| **Recommended** | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| **Aspirational** | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 |
| **Composite** | **100** | **100** | **100** | **100** | **100** |
| Golden | ✓ | ✓ | ✓ | ✓ | ✓ |

---

### Ranking

All five variations score 100 and pass the golden threshold. Qualitative differentiators for R4 planning:

**Rank 1 (tied): V-02, V-04, V-05**
All three introduce a named **AMEND — DATE FIELD** trigger (parallel to the PRIORITY DRIFT amend) that activates if C-01 fails on the date, directing the model back to the canonical template. This is the strongest single defense against C-01 regression at the repair layer. V-02 additionally achieves the highest causal density — every ordering instruction carries a "because" clause, not just the rationale→table transition.

**Rank 2 (tied): V-01, V-03**
Both pass all criteria but neither includes a named date-field AMEND trigger. V-01 has an inline C-01 amend note in Phase 5; V-03 has a Q1 redirect. These are functionally adequate but architecturally weaker than a named trigger. V-03 retains the best C-14 consequence vividness across all variations ("the file looks perfectly valid. The investigation silently stalls").

---

### Excellence Signals

**1. Named AMEND trigger for the date field (V-02, V-04, V-05)**
C-13 created a named repair loop for priority drift. The R3 top variations extend this pattern to C-01: "AMEND — DATE FIELD: If C-01 fails on date: return to the ROW TEMPLATE. Use the three-field canonical template. Fill in today's date. Verify three fields present before proceeding." This makes the C-01 self-correction loop as explicit and named as the C-04 loop. A skill with only a C-04 amend but no C-01 amend has asymmetric repair coverage. The parallel amend closes the most historically frequent regression path.

**2. Pervasive causal density across all ordering instructions (V-02 distinctive)**
C-17 tests whether the rationale→table instruction is causal. V-02 generalizes this: every ordering instruction in the skill carries a "because" clause — vocab block placement, rationale→table, Phase 3 after table, Phase 5 after writing, even path specificity (Phase 4 path has "because topic-status and topic-scanner glob for this specific path"). When the model understands the *intent* behind every ordering choice, it can recover from generation pressure by reasoning about purpose rather than just restoring surface order. The causal "because" pattern is not localized to C-17's single instruction but distributed throughout the skill as an architectural principle.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named AMEND trigger for date field — parallel to PRIORITY DRIFT AMEND; if C-01 fails on date the skill names a repair step directing the model back to the canonical template, closing the C-01 self-correction loop symmetrically with C-13's C-04 loop", "Pervasive causal density — every ordering instruction carries a because clause, not just the rationale-before-table transition; the model can recover from generation pressure by reasoning about intent at each step rather than restoring surface order"]}
```
