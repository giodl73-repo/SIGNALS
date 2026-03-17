```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["checkbox-gate before phase transition forces coverage self-verification and eliminates silent criterion omissions", "operational-consequence framing ties invalid vocabulary to downstream failure rather than style preference", "dedicated section per aspirational criterion prevents C-09 and C-10 from being treated as inline reminders"]}
```
ASS | Pre-printed table with 5 column headers + "Every row must fill every column. Do not leave any cell blank." |
| C-04 Valid priority vocab | PASS | Column header shows (essential / recommended / optional) + explicit exclusion list "Do not write: high, medium, low, required, nice-to-have or any other value." Two enforcement points. |
| C-05 At least one essential | PASS | "At least one row must be marked essential. A strategy with no essential signals has no defined commit gate and is invalid." |
| C-06 Multi-namespace | FAIL | "Aim for signals from at least 2 distinct namespaces." Soft -- "aim for" is not a hard requirement. Model can produce 1 namespace without violating the instruction. |
| C-07 Narrative rationale | PASS | "Write 2-4 sentences: why does this topic need investigation? What decision does it inform?" Explicit questions. |
| C-08 Owner roles | PASS | "Use at least 2 distinct owner roles across the rows." Hard requirement. |
| C-09 Commit gate | PASS | Pre-printed "### Commit Gate" section heading with example. Structural anchor. |
| C-10 Naming convention | PASS | Template row shows {topic}-{item}-{date}.md inline. |

Composite: 5/5 * 60 + 2/3 * 30 + 2/2 * 10 = 60 + 20 + 10 = **90**
All essential pass: YES

---

## V-02: Phrasing Register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md exists | PASS | "Open simulations/TOPICS.md. Create it if missing. Add one row... Save." |
| C-02 Correct path | PASS | "Open simulations/{topic}/strategy.md. Create it fresh." |
| C-03 All 5 fields | PASS | "Every signal gets five fields: Namespace | Skill | Item name | Owner role | Priority" -- all five named, table header shown. |
| C-04 Valid priority vocab | PASS | Explicit three-value list with semantic labels + negative examples: "No other values. Not 'high'. Not 'required'. Not 'nice-to-have'." |
| C-05 At least one essential | PASS | "No essential signals = no commit gate = invalid strategy." Hard invalidation consequence. |
| C-06 Multi-namespace | PASS | "Cover at least 2 namespaces." Hard requirement -- "cover" not "aim for." |
| C-07 Narrative rationale | PASS | "Write a short rationale section -- 2 to 4 sentences." Explicit requirement. |
| C-08 Owner roles | PASS | "Use at least 2 distinct owner roles (PM, developer, architect, designer, researcher, etc.)." |
| C-09 Commit gate | PASS | "5. WRITE COMMIT GATE -- Add a sentence after the table stating what the minimum signal set is." Numbered step with example. |
| C-10 Naming convention | PASS | "Item name format: {topic}-{slug}-{date}.md" stated once in table rules. |

Composite: 5/5 * 60 + 3/3 * 30 + 2/2 * 10 = 60 + 30 + 10 = **100**
All essential pass: YES

---

## V-03: Lifecycle Emphasis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md exists | PASS | "Read simulations/TOPICS.md (create if absent). Add one row... Write the file." Phased and explicit. |
| C-02 Correct path | PASS | "Write simulations/{topic}/strategy.md" stated in PHASE 3. |
| C-03 All 5 fields | PASS | Pre-printed table + column rules for each field + gate: "GATE: Do not begin PHASE 3 until the signal table is complete with all five columns filled." |
| C-04 Valid priority vocab | PASS | "WARNING: Do not use high/medium/low or any substitute. Only these three values are valid." WARNING label draws attention before rule. |
| C-05 At least one essential | PASS | "At least one signal marked essential (if none, the strategy has no commit gate)." Coverage requirement. |
| C-06 Multi-namespace | PASS | "At least 2 distinct namespaces represented" in coverage requirements. Hard. |
| C-07 Narrative rationale | PASS | Pre-printed "## Rationale" section with 2-4 sentence requirement in PHASE 3 template. |
| C-08 Owner roles | PASS | "At least 2 distinct owner roles" in coverage requirements. |
| C-09 Commit gate | PASS | "## Commit Gate" pre-printed as a section in PHASE 3 file template. |
| C-10 Naming convention | PASS | "{topic}-{slug}-{date}.md" in column rules and repeated in PHASE 3 table. |

Composite: 5/5 * 60 + 3/3 * 30 + 2/2 * 10 = 60 + 30 + 10 = **100**
All essential pass: YES

---

## V-04: Output Format + Priority Enforcement

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md exists | PASS | "Path: simulations/TOPICS.md. Action: Read, append row, write." Named artifact format. |
| C-02 Correct path | PASS | "ARTIFACT 2: simulations/{topic}/strategy.md" -- named artifact anchor. |
| C-03 All 5 fields | PASS | Pre-printed table with 5 columns + "Every row fills every column. No blank cells." Hard prohibition. |
| C-04 Valid priority vocab | PASS | Two enforcement points: (1) dedicated vocab section before the table with definitions, (2) "INVALID values (do not use): high, medium, low, required, critical, nice-to-have, P1, P2, P3." Longest exclusion list. |
| C-05 At least one essential | PASS | "(No essential = invalid. A topic with no essential signals has no commit gate and cannot be used to govern design decisions.)" Operational consequence framing. |
| C-06 Multi-namespace | PASS | "At least 2 distinct namespaces appear in the Namespace column." Hard column-level requirement. |
| C-07 Narrative rationale | PASS | "[2-4 sentences explaining why this feature cannot be committed to without investigation.]" |
| C-08 Owner roles | PASS | "At least 2 distinct owner roles appear in the Owner role column." |
| C-09 Commit gate | PASS | "### Commit Gate" with forced sentence template: "Design commit is permitted when: [list the minimum signal set]." Completion format, not free text. |
| C-10 Naming convention | PASS | "Item name follows: {topic}-{slug}-{date}.md" in requirements list + visible in pre-printed table row. |

Composite: 5/5 * 60 + 3/3 * 30 + 2/2 * 10 = 60 + 30 + 10 = **100**
All essential pass: YES

---

## V-05: Full Structure (All Axes)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 TOPICS.md exists | PASS | "Read simulations/TOPICS.md. Create if absent with this header:" -- explicit header template included. |
| C-02 Correct path | PASS | "Write simulations/{topic}/strategy.md" in PHASE 3 instructions. |
| C-03 All 5 fields | PASS | Pre-printed table + column definitions + checklist: "[ ] Every cell in every row is filled." Checklist enforces before phase transition. |
| C-04 Valid priority vocab | PASS | Three enforcement points: (1) column header in COLUMN DEFINITIONS, (2) valid value definitions with semantic labels, (3) "INVALID substitutes: high / medium / low / required / critical / P1 / P2 / P3 / nice-to-have. Using any invalid value makes the strategy unusable as a commit gate." |
| C-05 At least one essential | PASS | Checklist: "[ ] At least one row marked essential -- if zero, the strategy has no commit gate (invalid)." Checkbox format forces verification. |
| C-06 Multi-namespace | PASS | Checklist: "[ ] At least 2 distinct namespaces in the Namespace column." Gate item. |
| C-07 Narrative rationale | PASS | Pre-printed "## Rationale" section with 2-4 sentence specification and three guiding questions. |
| C-08 Owner roles | PASS | Checklist: "[ ] At least 2 distinct roles in the Owner role column." |
| C-09 Commit gate | PASS | Pre-printed "## Commit Gate" section with completion sentence, example, AND "Do not leave this section implicit. State the gate as a condition, not a hope." |
| C-10 Naming convention | PASS | Dedicated "## Naming Reference" section with format, example, and parameterized instance. Only variation with C-10 as its own section. |

Composite: 5/5 * 60 + 3/3 * 30 + 2/2 * 10 = 60 + 30 + 10 = **100**
All essential pass: YES

---

## Rankings

| Rank | Variation | Composite | All Essential | Differentiator |
|------|-----------|-----------|---------------|----------------|
| 1 | V-05 | 100 | YES | Checklist-gate at phase boundary; three C-04 enforcement points; dedicated Naming Reference section; "condition, not a hope" meta-instruction |
| 2 | V-04 | 100 | YES | Two C-04 enforcement points; longest INVALID list; forced sentence completion for commit gate |
| 3 | V-03 | 100 | YES | Phase gate enforces structural sequencing; WARNING label on C-04 |
| 4 | V-02 | 100 | YES | Hard "Cover" fixes V-01 C-06 gap; terse exclusion list effective |
| 5 | V-01 | 90 | YES | C-06 FAIL -- "Aim for" is soft; all other criteria well-enforced |

---

## Excellence Signals (from V-05)

1. **Checkbox-gate before phase transition**: [ ] checklist items make coverage requirements into explicit self-verification steps. The model cannot advance without checking each box, eliminating silent omissions on C-05, C-06, C-08.

2. **Three-point vocabulary enforcement with operational consequence**: C-04 addressed at three separate structural points, and the INVALID list is followed by "Using any invalid value makes the strategy unusable as a commit gate" -- connecting formatting rule to operational failure.

3. **Dedicated Naming Reference section**: C-10 gets its own named section (## Naming Reference) with a format line and a filled example. Elevates naming from an inline reminder to a first-class structural commitment.

4. **Meta-instruction against implicit gates**: "Do not leave this section implicit. State the gate as a condition, not a hope." Targets the failure mode where a model writes a vague commitment-gate sentence rather than an operational pass/fail condition.
