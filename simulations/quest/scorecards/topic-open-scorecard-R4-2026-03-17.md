```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase 1 defensive tool citation — V-02 cites topic-status in the collision-check setup step, extending C-19 pervasion beyond structural constraint blocks to all phases including setup", "Vocabulary block meta-comparative framing — V-03 applies C-20 to the reading-order meta-instruction itself: 'If you read this block first / If you skip this block', making the constraint justify its own priority using the same pattern it describes", "Decision-point tables as labeled phase-transition elements — V-04 formalizes contrast into tables headed 'Phase X Decision: [Name]' that precede each phase instruction, making the decision a first-class structural element before the instruction is given", "Five-column consequence chain as unified decision matrix — V-05's Default / Rule / Why / What Breaks / Tool table encodes C-19 and C-20 simultaneously for every constraint in a single compact block, a design pattern for constraint surface compactness"]}
```

---

**Round 4 result**: All 5 variations score 100/100, all golden. Second consecutive perfect round.

The rubric v4 gaps (C-18/C-19/C-20) were fully closed universally — no variation missed any of the three new criteria. The differentiating dimension this round is **depth and compactness strategy**, not pass/fail:

- V-02 goes deepest on C-19 (5 tool citations, including Phase 1)
- V-03 goes deepest on C-20 (4 ordering instructions all contrasted)
- V-04 formalizes C-20 structurally (named decision tables)
- V-05 achieves maximum compactness (5-column consequence chain covers all criteria in one block)

Four excellence signals identified for v5, all centered on the question: *how do you extend consequence-visible constraint framing to every element of a skill, including setup steps and reading-order meta-instructions, while keeping the skill compact?*
most common mistake… The commit gate silently fails — no error, no warning, the gate simply never fires. The Design Lead never learns..." |
| C-15 | PASS | Phase 2: "Write NARRATIVE RATIONALE first. Then build the signal table." |
| C-16 | PASS | ROW TEMPLATE section shows all three canonical fields including `{YYYY-MM-DD}` |
| C-17 | PASS | Phase 2: "because the decisions you describe in the rationale determine which roles are responsible for which signals" — explicit causal reason |
| C-18 | PASS | ROW TEMPLATE: "> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: …date field is dropped at high frequency." FIELD SCHEMA: "> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: reconstructed schemas consistently collapse five fields into three or four." Both templates carry titled prohibition + named failure mode. |
| C-19 | PASS | Vocabulary: "topic-status performs exact string matching on the priority field" ✓. Path rule: "because topic-status and topic-scanner glob for this specific path" ✓. Field schema: "topic-status parses all five fields for coverage computation; topic-scanner reads the Item Name field" ✓. All structural constraints carry tool citations. |
| C-20 | PASS | Phase 2: "If you write the rationale first, owner roles emerge from purpose… If you write the signal table first, owner roles become post-hoc labels…" — explicit side-by-side contrast |

Aspirational: **12/12**

**V-01 Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-02 — Tool-Citation Pervasive

### Essential (C-01–C-05)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 4 Write-1: return to ROW TEMPLATE, copy it, append to `simulations/TOPICS.md` |
| C-02 | PASS | Phase 4 Write-2: `simulations/{topic}/strategy.md` — explicit |
| C-03 | PASS | FIELD SCHEMA: "Five fields required per signal row" — F-01 through F-05 all listed |
| C-04 | PASS | VOCABULARY LOCK: exactly `essential` / `recommended` / `optional` |
| C-05 | PASS | Phase 2 Exit Gate: "COV-01: ≥ 1 `essential` row" |

Essential: **5/5**

### Recommended (C-06–C-08)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-06 | PASS | COV-02: "≥ 2 distinct namespaces" |
| C-07 | PASS | Phase 2 Step A: "≥ 2 sentences. State: (1) why this topic requires investigation, (2) what design decisions the signals inform." |
| C-08 | PASS | COV-03: "≥ 2 distinct owner roles" |

Recommended: **3/3**

### Aspirational (C-09–C-20)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Phase 3: `## COMMIT GATE` template, isolated section |
| C-10 | PASS | FIELD SCHEMA F-04: `{topic}-{signal}-{date}.md` |
| C-11 | PASS | VOCABULARY LOCK is first section: "Read before anything else in this skill" |
| C-12 | PASS | Phase 5 has full C-01–C-05 checklist with tool context on each item |
| C-13 | PASS | "AMEND — PRIORITY DRIFT: If C-04 fails: list each row with drift." Named trigger and named fix. |
| C-14 | PASS | VOCABULARY LOCK: "Wrong vocabulary = silent breakage. This is the most common mistake… topic-status simply excludes that signal from the commit-gate check. The gate silently fails. The Design Lead sees a valid-looking strategy file and believes the investigation is on track." |
| C-15 | PASS | Phase 2: "Write NARRATIVE RATIONALE before building the signal table." |
| C-16 | PASS | ROW TEMPLATE section shows all three canonical fields |
| C-17 | PASS | Phase 2: "Write the rationale before the table — because the rationale surfaces the decisions that determine owner roles… Step A (rationale) determines who should care; Step B (table) formalizes it." |
| C-18 | PASS | ROW TEMPLATE: "Copy this template — do not reconstruct it. When rebuilt from memory, the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder." Explicit prohibition + named failure mode. Fixes R3 V-02 borderline. |
| C-19 | PASS | Deepest C-19 coverage of all variations. Vocabulary: topic-status exact string comparison ✓. FIELD SCHEMA: "because topic-status parses all five fields for coverage computation, and topic-scanner reads the Item Name field" ✓. Phase 3 commit gate: "topic-status reads the `## COMMIT GATE` section as a named, parseable block… A gate embedded inside the signal table fails topic-status's section parser" ✓. Phase 4 path: "topic-status and topic-scanner both glob for `simulations/{topic}/strategy.md` specifically" ✓. Phase 1: "because topic-status loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path" ✓. Five distinct tool citations including Phase 1 setup — unique to V-02. |
| C-20 | PASS | Phase 2: "If the rationale comes first, each owner role in the table maps to a decision stakeholder… If the signal table comes first, owner roles become retroactive column-fillers with no derivable reason to exist." Explicit side-by-side contrast on primary sequencing instruction. |

Aspirational: **12/12**

**V-02 Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-03 — Comparative Failure Framing Throughout

### Essential (C-01–C-05)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | Step 5 File 1: template shown, append to `simulations/TOPICS.md` |
| C-02 | PASS | Step 5 File 2: "Write to `simulations/{topic}/strategy.md`" |
| C-03 | PASS | Step 3 table: 5 columns — Priority / Namespace / Skill / Item Name / Owner Role |
| C-04 | PASS | "BEFORE YOU START: VOCABULARY" section: exactly three values |
| C-05 | PASS | Step 3: "≥ 1 row marked `essential` — without this, you have no commit gate" |

Essential: **5/5**

### Recommended (C-06–C-08)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-06 | PASS | Step 3: "use at least 2 distinct namespaces" |
| C-07 | PASS | Step 2: "≥ 2 sentences explaining: Why does this topic need investigation? What design decision will these signals inform?" |
| C-08 | PASS | Step 3: "≥ 2 distinct owner roles" |

Recommended: **3/3**

### Aspirational (C-09–C-20)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Step 4: "Write a `## COMMIT GATE` section in strategy.md listing every `essential` signal by its exact item name." |
| C-10 | PASS | Step 3 Item Name: `{topic}-{signal}-{date}.md` |
| C-11 | PASS | "BEFORE YOU START: VOCABULARY" is the first section: "Read this before anything else." |
| C-12 | PASS | Step 6 has Q1–Q5 checklist |
| C-13 | PASS | "AMEND — PRIORITY DRIFT: If Q4 fails…" Q4 asks "Did any priority drift to `high`, `medium`, `low`, or anything else?" Named question about priority drift, not a generic review pass. |
| C-14 | PASS | VOCABULARY section: "topic-status performs exact string matching — `high` does not match `essential`. The commit gate silently excludes that signal. The Design Lead sees a valid-looking strategy file that is actually broken." |
| C-15 | PASS | Step 2: "Write this **before** the table — not after." with full comparative framing |
| C-16 | PASS | ROW TEMPLATE section shows all three canonical fields; template also repeated in Step 5 |
| C-17 | PASS | Step 2 contrast: "If you write the rationale first: the decisions you describe surface the question 'who should own this signal?' Owner roles in the table emerge from the stakeholders you just named." Causal reason fully developed via contrast. |
| C-18 | PASS | ROW TEMPLATE: "Copy this template… Do not reconstruct from memory — reconstructed templates reliably drop the date field." Step 5: "Copy it — do not reconstruct." Explicit prohibition + named failure mode. |
| C-19 | PASS | Vocabulary: "topic-status performs exact string matching" ✓. Step 3 Priority inline: "topic-status gates on exact string match" ✓. Step 5 File 2 path: "because topic-status and topic-scanner glob for this specific path. A wrong path causes both tools to silently return zero results." ✓. (Field schema five-field requirement and commit gate isolation do not carry tool citations — but pass condition is "path and/or field schema"; path rule citation is sufficient.) |
| C-20 | PASS | Deepest C-20 of all variations — four ordering instructions each contrasted side by side: (1) VOCABULARY: "If you read this block first: … If you skip this block and read the schema first: …" ✓; (2) ROW TEMPLATE: "If you copy this template: … If you reconstruct the template from memory: …" ✓; (3) Step 2 rationale→table: "If you write the rationale first: … If you write the table first: …" ✓; (4) Step 6 self-check timing: "If you run this check after writing: … If you run this check before writing: …" ✓. |

Aspirational: **12/12**

**V-03 Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-04 — Lifecycle Phases + Contrast Tables

### Essential (C-01–C-05)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 4 Write-1: "Return to the **TOPICS.md ROW TEMPLATE** above. Copy it — do not reconstruct. Fill in the three placeholders. Append to `simulations/TOPICS.md`." |
| C-02 | PASS | Phase 4 Write-2: `simulations/{topic}/strategy.md` — explicit |
| C-03 | PASS | FIELD SCHEMA: F-01 through F-05, all five labeled and defined |
| C-04 | PASS | VOCABULARY LOCK: exactly three values |
| C-05 | PASS | Phase 2 Exit Gate: "COV-01: ≥ 1 `essential` row (no essential = no commit gate = no defined finish line)" |

Essential: **5/5**

### Recommended (C-06–C-08)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-06 | PASS | Phase 2 Exit Gate: "COV-02: ≥ 2 distinct namespaces" |
| C-07 | PASS | Phase 2 Step 2A: "≥ 2 sentences. State: (1) why this topic requires investigation, (2) what design decisions the signals inform." |
| C-08 | PASS | Phase 2 Exit Gate: "COV-03: ≥ 2 distinct owner roles" |

Recommended: **3/3**

### Aspirational (C-09–C-20)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Phase 3: `## COMMIT GATE` template, structurally isolated |
| C-10 | PASS | FIELD SCHEMA F-04: `{topic}-{signal}-{date}.md` |
| C-11 | PASS | VOCABULARY LOCK is first section, standalone block directive |
| C-12 | PASS | Phase 5 full checklist with AMEND triggers |
| C-13 | PASS | "AMEND — PRIORITY DRIFT: If C-04 fails: list each row with drift." Named, targeted. |
| C-14 | PASS | VOCABULARY LOCK: "Wrong vocabulary = silent breakage… topic-status performs exact string comparison… the commit gate silently fails — it does not error, it simply never trips." |
| C-15 | PASS | Phase 2 contrast table shows compliant path (rationale first); Step 2A precedes Step 2B |
| C-16 | PASS | ROW TEMPLATE section with all three canonical fields |
| C-17 | PASS | Phase 2 contrast table Compliant path: "Owner roles emerge from the decisions described in the rationale — each role is the accountable stakeholder for a question being answered. Coverage review can verify roles against the rationale." Causal reason fully developed. |
| C-18 | PASS | ROW TEMPLATE: "> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: the `{YYYY-MM-DD}` date field is the most commonly dropped field…" Phase 4 contrast table: "Non-compliant: Reconstruct the row format from memory. The `{YYYY-MM-DD}` date field is dropped at high frequency." Explicit prohibition + named failure mode + contrast table. |
| C-19 | PASS | VOCABULARY LOCK: "topic-status performs exact string comparison on the priority field" ✓. FIELD SCHEMA: "topic-status parses all five fields for coverage computation; topic-scanner reads the Item Name field for signal artifact discovery" ✓. Phase 3: "topic-status reads `## COMMIT GATE` as a named parseable section… A gate embedded inside the signal table… fails topic-status's section parser; coverage computation returns no gate status." ✓. Phase 4 Write-2: "because topic-status and topic-scanner glob for this specific path" ✓. Tool citations on vocabulary, field schema, commit gate, and path. |
| C-20 | PASS | Three formalized contrast tables at phase decision points: Phase 2 (rationale ordering), Phase 4 (template copy vs. reconstruction), Phase 5 (check timing). Each table has named header ("Phase X Decision: [Name]"), labeled Compliant/Non-compliant rows, and explicit consequence columns. Deepest structural formalization of C-20. |

Aspirational: **12/12**

**V-04 Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

## V-05 — Compact + Extended DEFAULTS TABLE

### Essential (C-01–C-05)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 4: "Copy it. Fill in slug, description, and today's date. Three fields — do not omit the date. Append to `simulations/TOPICS.md`." |
| C-02 | PASS | Phase 4: "Write to `simulations/{topic}/strategy.md`" |
| C-03 | PASS | Phase 2 signal table has five columns; all five enumerated in requirements |
| C-04 | PASS | VOCABULARY CONSTRAINT: "exactly `essential` / `recommended` / `optional`" |
| C-05 | PASS | Phase 2: "≥ 1 row `essential`" |

Essential: **5/5**

### Recommended (C-06–C-08)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-06 | PASS | Phase 2: "≥ 2 distinct namespaces" |
| C-07 | PASS | Phase 2: "Rationale: ≥ 2 sentences. State why the topic requires investigation and what decisions the signals inform." |
| C-08 | PASS | Phase 2: "≥ 2 distinct owner roles" |

Recommended: **3/3**

### Aspirational (C-09–C-20)

| ID | Pass? | Evidence |
|----|-------|---------|
| C-09 | PASS | Phase 3: `## COMMIT GATE` template, structurally isolated |
| C-10 | PASS | Phase 2 Item Name: `{topic}-{signal}-{date}.md` |
| C-11 | PASS | VOCABULARY CONSTRAINT: "Standalone block. Read before any instruction." First section. |
| C-12 | PASS | Phase 5 has C-01–C-05 checklist |
| C-13 | PASS | "AMEND — Priority Drift: If C-04 fails: identify each row with drift." Named trigger. |
| C-14 | PASS | VOCABULARY CONSTRAINT: "Wrong vocabulary = silent downstream breakage… topic-status performs exact string comparison… Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken." |
| C-15 | PASS | Phase 2: "Rationale first. Signal table second." + causal reason with contrast framing |
| C-16 | PASS | ROW TEMPLATE shows all three canonical fields |
| C-17 | PASS | Phase 2: "…because the rationale determines which decisions need answering, and those decisions determine which roles are accountable. If the rationale comes first, owner roles emerge as stakeholders responsible for each open decision. If the table comes first, owner roles become column-fillers…" Causal reason + contrast. |
| C-18 | PASS | ROW TEMPLATE: "Copy this template when writing the TOPICS.md entry. Do not reconstruct from memory — reconstructed templates reliably drop the date field." DEFAULTS TABLE row 2 also names the failure mode. Explicit prohibition + named failure mode. |
| C-19 | PASS | DEFAULTS TABLE "Tool That Detects It" column covers every structural constraint: Priority → "topic-status (commit-gate check, exact string match)"; TOPICS.md row → "topic-status (date filter)"; Inline commit gate → "topic-status (commit-gate section parser)"; Flat strategy path → "topic-status, topic-scanner (glob pattern match)". All constraints covered in a single dedicated column. Most compact C-19 delivery. |
| C-20 | PASS | DEFAULTS TABLE "What Breaks If You Skip" column provides non-compliant path consequence for every rule. Row 3 (rationale ordering) contrasts both paths explicitly: "If table first: roles are labels with no derivable purpose. If rationale first: roles are stakeholders accountable to named decisions." Phase 2 repeats the full contrast. C-20 delivered for all rules via the table structure — not just the rationale instruction. |

Aspirational: **12/12**

**V-05 Composite: 60 + 30 + 10 = 100/100** ✓ Golden

---

## Round 4 Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| **Essential** | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| **Recommended** | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| **Aspirational** | 12/12 | 12/12 | 12/12 | 12/12 | 12/12 |
| **Score** | **100** | **100** | **100** | **100** | **100** |
| **Golden** | YES | YES | YES | YES | YES |

All 5 variations score 100/100. All achieve golden. Second consecutive round of perfect scores (R3 was 100/100 on v3 rubric).

---

## R4 Gap Analysis Result

All three R4 gaps were closed across all variations:
- **C-18** (anti-reconstruction directive): Universally present with explicit prohibition + named failure mode
- **C-19** (downstream tool citation): Universally present; V-02 deepest (5 citations including Phase 1), V-05 most compact (DEFAULTS TABLE "Tool" column)
- **C-20** (comparative failure framing): Universally present; V-03 deepest (all 4 ordering instructions contrasted), V-04 most formalized (named decision tables at phase transitions), V-05 most compact (DEFAULTS TABLE "What Breaks" column)

No unresolved gaps remain at rubric v4.

---

## Excellence Signals for v5

**E-01 — Phase 1 defensive tool citation (V-02)**
V-02 cites topic-status in the collision-check step: "because topic-status loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path." No other variation annotates the setup phase with a tool dependency. Extends C-19 pervasion from structural constraint blocks to all phases including setup.

**E-02 — Vocabulary block uses comparative framing on itself (V-03)**
V-03 applies C-20 to the meta-instruction "read this block first": "If you read this block first: the constraint is locked before you encounter any signal row… If you skip this block and read the schema first: you may already have formed row vocabulary before the constraint arrives." Only variation that uses comparative framing to argue for the reading order of the skill itself — the vocabulary block justifies its own priority using the same pattern it describes.

**E-03 — Decision-point tables as labeled phase-transition elements (V-04)**
V-04 formalizes contrast into tables headed "Phase X Decision: [Decision Name]" that appear before each phase's instruction. The label names the decision; the table contrasts both paths before the instruction is given. The decision becomes a first-class structural element rather than embedded in prose.

**E-04 — Five-column consequence chain as unified decision matrix (V-05)**
V-05's DEFAULTS TABLE with Default / Rule / Why / What Breaks / Tool encodes C-19 and C-20 simultaneously for every constraint in a single block. At full maturity, a skill's entire constraint surface can be expressed as a structured consequence chain — a design pattern for constraint compactness.
