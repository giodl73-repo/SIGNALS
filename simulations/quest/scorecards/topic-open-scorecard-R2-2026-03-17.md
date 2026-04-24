# topic-open — Round 2 Score Sheet

**Result: No variation achieves golden** — all 5 fail C-01 (missing start date in TOPICS.md row template).

## Scores

| Rank | Var | Composite | Essential | Rec | Asp | Axis | Golden |
|------|-----|-----------|-----------|-----|-----|------|--------|
| 1 | V-04 | **88** | 4/5 | 3/3 | 7/7 | vocab-first + self-check | NO |
| 1 | V-05 | **88** | 4/5 | 3/3 | 7/7 | compact all-criteria | NO |
| 3 | V-02 | 86.6 | 4/5 | 3/3 | 6/7 | self-check only | NO |
| 4 | V-01 | 85.1 | 4/5 | 3/3 | 5/7 | vocab placement only | NO |
| 5 | V-03 | 78 | 4/5 | 2/3 | 7/7 | conversational imperative | NO |

## Structural Finding

**C-01 is the sole blocker for all 5 variations.** Every R2 variation uses:
```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |
```
The v2 rubric requires slug + description + **start date**. The actual TOPICS.md format is `| Topic | What | Started |`. The golden had `YYYY-MM-DD`; R2 dropped it.

One-line fix: add `{YYYY-MM-DD}` to the row template. If applied to V-04 or V-05, composite = **100**.

## Key C-11 to C-15 Results

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 vocab block before instructions | PASS | FAIL | PASS | PASS | PASS |
| C-12 post-gen self-check | FAIL | PASS | PASS | PASS | PASS |
| C-13 AMEND names priority drift | FAIL | PASS | PASS | PASS | PASS |
| C-14 consequence framing | PASS | PASS | PASS | PASS | PASS |
| C-15 rationale before table | PASS | PASS | PASS | PASS | PASS |

V-02 fails C-11 (vocab buried in field schema, not leading standalone block). V-01 fails C-12/C-13 (prevention only, no detection layer). V-03 fails C-06 (no explicit ≥2 namespace count constraint, losing one recommended point).

## New Patterns

1. **TOPICS.md date regression** — single-focus rounds drop currently-passing essential criteria; need a preservation gate.
2. **Two-layer C-04 defense** — vocab lock (prevention) + named AMEND step (detection) consistently achieves 7/7 aspirational; V-05 proves compact design equals full-scaffolded V-04.
3. **Rationale-for-the-sequencing** — V-05's "Rationale written before the table *ensures owner roles emerge from decision context*" outperforms "write rationale first" because the model has a causal reason, not just an order.

```json
{"top_score": 88, "all_essential_pass": false, "new_patterns": ["TOPICS.md row template must include YYYY-MM-DD date placeholder — all R2 variations regressed on C-01 by dropping the date while focusing on C-11-C-15", "Two-layer C-04 defense (standalone vocab lock before instructions + post-generation AMEND targeting priority drift by name) achieves 7/7 aspirational; V-05 proves compact design matches full-scaffolded V-04 at lower cognitive load", "Single-focus variation rounds need a preservation gate: templates for currently-passing criteria must be explicitly carried from the golden to prevent regression"]}
```
; Phase 2 exit gate checks COV-03 |
| C-09 | Explicit commit gate | PASS | Phase 3 is a structurally isolated COMMIT GATE block; "not a section of Phase 2" stated explicitly |
| C-10 | Item names follow convention | PASS | F-04: `{topic}-{signal}-{date}.md`; Phase 2 exit gate: "[ ] All item names follow {topic}-{signal}-{date}.md" |
| C-11 | Vocab constraint before instructions | PASS | "## VOCABULARY LOCK" is the first content section with preface "Read this block before reading anything else in this skill" — precedes INERTIA REGISTER and all phase directives |
| C-12 | Post-generation self-check present | **FAIL** | No Phase 5 or post-write audit phase. Phase 2 exit gate checkboxes are pre-write (aspirational only, model hasn't produced output yet). |
| C-13 | AMEND step targets C-04 by name | **FAIL** | No AMEND step. The Phase 2 exit gate asks "[ ] Every priority value is one of: essential / recommended / optional" but is a pre-write gate, not a named post-generation correction loop. |
| C-14 | C-04 framed with downstream consequence | PASS | VOCABULARY LOCK: "Wrong vocabulary = silent breakage. This is the most common mistake in this skill." + multi-sentence explanation: "passes visual inspection but is unparseable... The commit gate silently stops working." |
| C-15 | Prose rationale sequenced before table | PASS | Phase 2: "**Write NARRATIVE RATIONALE first. The signal table comes after.**" Rationale section appears before SIGNAL TABLE section in template. |

**Essential**: 4/5 → 48
**Recommended**: 3/3 → 30
**Aspirational**: 5/7 → 7.1

**V-01 composite: 85.1 — C-01 fails; golden not achieved**

---

## V-02 — Post-generation self-check phase

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | TOPICS.md entry exists | **FAIL** | Phase 4 row template: `\| {TOPIC} \| active \| simulations/{TOPIC}/strategy.md \| [description] \|` — no date field |
| C-02 | Strategy file at correct path | PASS | Phase 4 Write 2: exact path named |
| C-03 | All five signal fields present | PASS | FIELD SCHEMA F-01 through F-05; Phase 2 signal table 5 columns; Phase 5 checks "every signal row contain all five fields" |
| C-04 | Priority vocabulary valid | PASS | F-01: "Exactly: essential / recommended / optional — **not** high/medium/low. Wrong vocabulary = strategy malformed; Design Lead cannot parse readiness. This is the most common mistake." Phase 5 AMEND trigger: "PRIORITY DRIFT CHECK: Did any row use high, medium, low...?" Two-layer: schema constraint + post-write check. |
| C-05 | At least one essential signal | PASS | COV-01: "≥ 1"; Phase 5 explicitly checks "at least one row marked `essential`" |
| C-06 | Spans multiple namespaces | PASS | COV-02: "≥ 2 distinct namespaces" |
| C-07 | Prose rationale present | PASS | Phase 2 Narrative Rationale section; "Write ≥ 2 sentences here before building the signal table" |
| C-08 | Owner roles differentiated | PASS | F-05: "≥ 2 distinct roles across all rows"; Narrative Rationale: "The roles you name here become owner roles in your signal table" |
| C-09 | Explicit commit gate | PASS | Phase 3 dedicated COMMIT GATE, structurally isolated |
| C-10 | Item names follow convention | PASS | F-04: `{topic}-{signal}-{date}.md` in FIELD SCHEMA |
| C-11 | Vocab constraint before instructions | **FAIL** | INERTIA REGISTER is the first section. Vocabulary appears in F-01 of FIELD SCHEMA (second major section). No standalone vocab block preceding all instructions. |
| C-12 | Post-generation self-check present | PASS | Phase 5 SELF-CHECK: checkbox list (C-01 through C-05 labeled by name) after both files written. "Check your actual output, not your intentions." |
| C-13 | AMEND step targets C-04 by name | PASS | Phase 5 AMEND Step triggered by C-04 failure: "Identify every row where priority is not essential / recommended / optional"; 4-step correction sequence named specifically for priority drift |
| C-14 | C-04 framed with downstream consequence | PASS | F-01: "Wrong vocabulary = strategy malformed; Design Lead cannot parse readiness. This is the most common mistake." Consequence named, failure mode identified. |
| C-15 | Prose rationale sequenced before table | PASS | Phase 2: Narrative Rationale section explicitly precedes Signal Table. "The roles you name here become owner roles in your signal table." |

**Essential**: 4/5 → 48
**Recommended**: 3/3 → 30
**Aspirational**: 6/7 → 8.6

**V-02 composite: 86.6 — C-01 fails; golden not achieved**

---

## V-03 — Phrasing register (conversational imperative)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | TOPICS.md entry exists | **FAIL** | Step 5 File 1: `\| {TOPIC} \| active \| simulations/{TOPIC}/strategy.md \| [one-line description] \|` — no date |
| C-02 | Strategy file at correct path | PASS | Step 5 File 2: `simulations/{TOPIC}/strategy.md` named |
| C-03 | All five signal fields present | PASS | Step 3 table has Priority / Namespace / Skill / Item Name / Owner Role columns |
| C-04 | Priority vocabulary valid | PASS | "BEFORE YOU START: VOCABULARY" block: "Do not use high, medium, or low for signal priority. Ever." Step 6 Q4: "Did any drift to high, medium, low, or anything else? (no = STOP AND FIX)" |
| C-05 | At least one essential signal | PASS | Step 3: "Include at least 1 signal marked `essential` — without it, you have no commit gate" |
| C-06 | Spans multiple namespaces | **FAIL** | Step 3 lists valid namespace vocabulary but imposes no minimum count ("at least 2 distinct namespaces" constraint absent). COV-02 equivalent missing. |
| C-07 | Prose rationale present | PASS | Step 2 "WRITE YOUR RATIONALE (BEFORE THE SIGNAL TABLE)" requires ≥ 2 sentences |
| C-08 | Owner roles differentiated | PASS | Step 3: "at least 2 distinct roles across all rows"; Step 2: "If your rationale does not mention at least two distinct roles, revise it before building the table" |
| C-09 | Explicit commit gate | PASS | Step 4 "NAME YOUR COMMIT GATE" with named gate template |
| C-10 | Item names follow convention | PASS | Step 3: "Item name: {topic}-{signal}-{date}.md — no exceptions" |
| C-11 | Vocab constraint before instructions | PASS | "BEFORE YOU START: VOCABULARY" is the first titled section, before any step instructions. Conversational block, standalone. |
| C-12 | Post-generation self-check present | PASS | Step 6 "CHECK YOUR WORK" with 5 questions including Q4 on priority drift; "Read what you actually wrote, not what you intended to write" |
| C-13 | AMEND step targets C-04 by name | PASS | Step 6 Q4: "Did any drift to high, medium, low, or anything else? (yes = all correct / no = STOP AND FIX BEFORE CONTINUING)" — named drift question, not generic |
| C-14 | C-04 framed with downstream consequence | PASS | "every tool downstream... will look for exactly these strings... If you write high instead of essential, the gate silently fails — it does not error, it just never trips. The Design Lead never knows the topic is missing signals. **This is the most common mistake in this skill.**" Strongest prose consequence framing in this set. |
| C-15 | Prose rationale sequenced before table | PASS | Step 2 title: "WRITE YOUR RATIONALE (BEFORE THE SIGNAL TABLE)"; sequencing enforced by step numbering and explicit title |

**Essential**: 4/5 → 48
**Recommended**: 2/3 → 20
**Aspirational**: 7/7 → 10

**V-03 composite: 78 — C-01 fails; C-06 fails; golden not achieved**

Note: V-03 achieves full 7/7 aspirational — the only variation besides V-04/V-05 to do so — but the C-06 miss in recommended (consequence of omitting an explicit namespace count constraint) drops its composite below the others. The conversational register is V-03's unique contribution: consequence framing in V-03 is notably more vivid than in V-01, V-04, or V-05.

---

## V-04 — Combination: vocabulary-first + post-generation self-check

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | TOPICS.md entry exists | **FAIL** | Phase 4 Write 1: `\| {TOPIC} \| active \| simulations/{TOPIC}/strategy.md \| [description] \|` — no date field |
| C-02 | Strategy file at correct path | PASS | Phase 4 Write 2: exact path; Phase 5 C-02 check: "Is the strategy file at simulations/{topic}/strategy.md specifically" |
| C-03 | All five signal fields present | PASS | F-01 through F-05 defined; Phase 5 C-03: "Does every signal row contain all five fields: priority, namespace, skill, item name, owner role?" |
| C-04 | Priority vocabulary valid | PASS | VOCABULARY LOCK (first section): forbidden values listed; consequence stated; "Re-read VOCABULARY LOCK before writing any priority value" in table; Phase 5 C-04 AMEND TRIGGER; two-layer defense |
| C-05 | At least one essential signal | PASS | COV-01: "≥ 1 essential signal"; Phase 2 exit gate; Phase 5 C-05: "Does the signal table contain at least one row marked `essential`?" |
| C-06 | Spans multiple namespaces | PASS | COV-02: "≥ 2 distinct namespaces"; Phase 2 exit gate checks it |
| C-07 | Prose rationale present | PASS | Phase 2: "Write NARRATIVE RATIONALE before the signal table"; ≥ 2 sentences; narrative section precedes table |
| C-08 | Owner roles differentiated | PASS | F-05: "≥ 2 distinct roles (IR-05 override)"; COV-03 enforced; Phase 2 exit gate; narrative leads to roles |
| C-09 | Explicit commit gate | PASS | Phase 3 is a structurally isolated COMMIT GATE; "Overriding IR-03" declared |
| C-10 | Item names follow convention | PASS | F-04: `{topic}-{signal}-{date}.md`; Phase 2 exit gate checks F-04 |
| C-11 | Vocab constraint before instructions | PASS | VOCABULARY LOCK is the first section: "> This block is read before any schema, register, or phase." Standalone, before INERTIA REGISTER and all phases. |
| C-12 | Post-generation self-check present | PASS | Phase 5 POST-GENERATION SELF-CHECK: checkbox list labeled C-01 through C-05 by name; "Audit what you actually produced." |
| C-13 | AMEND step targets C-04 by name | PASS | Phase 5: "PRIORITY DRIFT — AMEND TRIGGER: Did any row use high, medium, low, or any other value? If yes, do not mark C-04 as passing. Go to AMEND." 6-step AMEND sequence. C-04 named explicitly. |
| C-14 | C-04 framed with downstream consequence | PASS | VOCABULARY LOCK: "Wrong vocabulary = silent breakage. This is the most common mistake in this skill." + "Tools that gate on priority look for exact string matches. `high` does not match `essential`. The gate silently fails. The Design Lead never detects the gap." |
| C-15 | Prose rationale sequenced before table | PASS | Phase 2: "**Write NARRATIVE RATIONALE before the signal table.**"; narrative section precedes signal table in template |

**Essential**: 4/5 → 48
**Recommended**: 3/3 → 30
**Aspirational**: 7/7 → 10

**V-04 composite: 88 — C-01 fails; golden not achieved**

V-04 is the first variation to achieve 7/7 aspirational. The combination of V-01's vocab placement + V-02's post-generation self-check produces a two-layer C-04 defense that no single-axis variation achieves. Blocked only by the C-01 date regression common to all R2 variations.

---

## V-05 — Combination compact

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | TOPICS.md entry exists | **FAIL** | Phase 4 template: `\| {TOPIC} \| active \| simulations/{TOPIC}/strategy.md \| [one-line description] \|` — no date |
| C-02 | Strategy file at correct path | PASS | Phase 4 explicitly names path; Phase 5 checks "Strategy file is at simulations/{topic}/strategy.md — not a flat path?" |
| C-03 | All five signal fields present | PASS | Phase 2 signal table has 5 columns; Phase 5: "Every signal row has all five fields: priority, namespace, skill, item name, owner role?" |
| C-04 | Priority vocabulary valid | PASS | VOCABULARY CONSTRAINT standalone block (first section); signal table: "Re-read VOCABULARY CONSTRAINT before filling the Priority column"; Phase 5 AMEND — three-point defense |
| C-05 | At least one essential signal | PASS | Phase 2 gate: "≥ 1 row marked `essential`"; Phase 5: "At least one signal row is marked `essential`?" |
| C-06 | Spans multiple namespaces | PASS | Phase 2 gate: "≥ 2 distinct namespaces (scout, draft, review, flow, trace, prove, listen, program, topic)" — explicit minimum with namespace list |
| C-07 | Prose rationale present | PASS | Phase 2: "Rationale (write this before the signal table)" section; ≥ 2 sentences required |
| C-08 | Owner roles differentiated | PASS | Phase 2 signal table: "≥ 2 distinct owner roles"; Rationale section: "Name the roles involved — these become owner roles in your signal table" |
| C-09 | Explicit commit gate | PASS | Phase 3 COMMIT GATE; "Structurally isolated. Not a section of Phase 2." |
| C-10 | Item names follow convention | PASS | Signal table Item Name column labeled `{topic}-{signal}-{date}.md`; Phase 2 gate checks item names |
| C-11 | Vocab constraint before instructions | PASS | "## VOCABULARY CONSTRAINT — Standalone block. Read before any instruction." is the first content section, before DEFAULTS TABLE and all phases |
| C-12 | Post-generation self-check present | PASS | Phase 5 SELF-CHECK AND AMEND: 5-item per-essential-criterion checklist after both files written |
| C-13 | AMEND step targets C-04 by name | PASS | Phase 5 AMEND — Priority Drift Check: "Did any row use high, medium, low, or any other value? If yes: list every row where drift occurred. Replace each value. Re-scan before marking C-04 as passing." Named and targeted. |
| C-14 | C-04 framed with downstream consequence | PASS | VOCABULARY CONSTRAINT: "Wrong vocabulary = silent downstream breakage. This is the most common mistake. Tools gate on exact string matches. Writing `high` instead of `essential` causes the commit gate to silently fail — it does not error, it just stops working. The Design Lead sees a passing strategy file that is actually broken." |
| C-15 | Prose rationale sequenced before table | PASS | Phase 2: "**Write narrative rationale FIRST. Then build the signal table.** Rationale written before the table ensures owner roles emerge from decision context." Sequencing instruction + rationale for the sequencing. |

**Essential**: 4/5 → 48
**Recommended**: 3/3 → 30
**Aspirational**: 7/7 → 10

**V-05 composite: 88 — C-01 fails; golden not achieved**

V-05 matches V-04's composite with notably less structural overhead. The "DEFAULTS THIS SKILL OVERRIDES" table replaces the full INERTIA REGISTER + COVERAGE SCHEMA blocks while conveying the same override contract. V-05's C-15 evidence is the strongest in this set: "Rationale written before the table ensures owner roles emerge from decision context" — the skill names the *reason* for the sequencing, not just the order.

---

## Ranking

| Rank | Var | Composite | Essential | Recommended | Aspirational | Golden |
|------|-----|-----------|-----------|-------------|--------------|--------|
| 1 | V-04 | **88** | 4/5 | 3/3 | 7/7 | NO |
| 1 | V-05 | **88** | 4/5 | 3/3 | 7/7 | NO |
| 3 | V-02 | 86.6 | 4/5 | 3/3 | 6/7 | NO |
| 4 | V-01 | 85.1 | 4/5 | 3/3 | 5/7 | NO |
| 5 | V-03 | 78 | 4/5 | 2/3 | 7/7 | NO |

Golden threshold (all 5 essential + composite >= 80): **no variation achieves golden**.

---

## Round 2 Structural Finding

**All R2 variations fail C-01.** The TOPICS.md row template in all five variations:

```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |
```

...omits the start date. The v2 rubric C-01 pass condition requires "topic slug, short description, **and start date**". The actual TOPICS.md uses a three-column format: `| Topic | What | Started |` with `YYYY-MM-DD`. The golden (R20 QU5) included this; the R2 variations dropped it during redesign.

**The fix is a one-line template change.** Add `{YYYY-MM-DD}` to the row template. If this single change were applied uniformly, V-04 and V-05 would both score:

- Essential: 5/5 → 60
- Recommended: 3/3 → 30
- Aspirational: 7/7 → 10
- **Composite: 100 — golden achieved**

This is the sole remaining gap between Round 2 and a full golden.

---

## Excellence Signals

Patterns from the top-scoring variations and cross-variation comparison:

1. **Two-layer C-04 defense is sufficient; single-layer is not** — V-01 (vocab lock only) and V-02 (self-check only) each pass C-04 but miss the other layer. V-04 and V-05 combine both: standalone vocab lock before instructions (prevention) + post-generation AMEND targeting priority drift by name (detection). Neither layer alone is as reliable as both together.

2. **Compact design achieves equal aspirational coverage** — V-05 achieves 7/7 aspirational with fewer sections than V-04. The "DEFAULTS THIS SKILL OVERRIDES" table replaces INERTIA REGISTER + COVERAGE SCHEMA + FIELD SCHEMA with a two-column design-intent summary. The result is the same rubric coverage at lower cognitive load. Compactness is not a quality trade-off here.

3. **Named AMEND step outperforms pre-write gate for C-04 correction** — V-01's pre-write gate ("[ ] Every priority value is one of...") asks the model to check before it has written anything. V-02/V-04/V-05's post-write AMEND asks "Did any row use high/medium/low?" after output exists — a concrete re-read of actual content, not an aspirational intention.

4. **Rationale sequencing benefits from a stated reason** — V-05's Phase 2 says "Rationale written before the table *ensures owner roles emerge from decision context*" — explaining *why* the order matters. V-01 and V-04 just instruct the order. V-05's version is more likely to be followed under generation pressure because the model has a causal reason, not just a formatting rule.

5. **C-01 date regression is a single-focus round failure mode** — all R2 variations targeted C-11 through C-15 and all dropped the date from the TOPICS.md template. When a variation round focuses narrowly on new criteria, the templates for currently-passing criteria must be explicitly preserved. A "preservation gate" (e.g., "carry the TOPICS.md row template exactly from the golden") would have prevented this universal regression.

---

```json
{"top_score": 88, "all_essential_pass": false, "new_patterns": ["TOPICS.md row template must include YYYY-MM-DD date placeholder — all R2 variations regressed on C-01 by dropping the date while focusing on C-11-C-15", "Two-layer C-04 defense (standalone vocab lock before instructions + post-generation AMEND targeting priority drift by name) achieves 7/7 aspirational; V-05 proves compact design matches full-scaffolded V-04 at lower cognitive load", "Single-focus variation rounds need a preservation gate: templates for currently-passing criteria must be explicitly carried from the golden to prevent regression"]}
```
