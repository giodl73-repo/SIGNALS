## scout-risk R3 — Scorecard

---

### Criteria Reference

| ID | Category | Weight |
|----|----------|--------|
| C-01–C-05 | Essential | 12 pts each (60 total) |
| C-06–C-08 | Recommended | 10 pts each (30 total) |
| C-09–C-16 | Aspirational | 2 PASS / 1 PARTIAL / 0 FAIL |

---

### V-01 — Lifecycle Emphasis (≥3 pairs on R2 V-03 base)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "always the first entry. Do not skip it. Do not move it." |
| C-02 | PASS | "at least one risk each from 3 or more" dimensions listed |
| C-03 | PASS | Phase 2 format specifies name / dimension / severity / likelihood / mitigation |
| C-04 | PASS | "HIGH, MEDIUM, or LOW — nothing else" |
| C-05 | PASS | Re-read gate: "if two or more are generic non-actions, replace them" |
| C-06 | PASS | Explicit Dimension field per entry |
| C-07 | PASS | "what specific condition or scenario triggers this risk — not just 'possible'" |
| C-08 | PASS | "Sort dimensional risks from highest to lowest severity" |
| C-09 | PASS (2) | Mandatory Phase 3 with ≥3 named pairs → at least one dependency present |
| C-10 | PARTIAL (1) | AMEND clause in Phase 4 handles correctly; no live directive in base prompt |
| C-11 | PARTIAL (1) | Re-read gate allows 1 generic to survive ("replace if two or more") — zero not enforced |
| C-12 | PARTIAL (1) | "specific condition or scenario" is semantic instruction, not structural template — most entries qualify but all entries not structurally guaranteed |
| C-13 | PASS (2) | Dedicated `## Risk Interdependencies` section with ≥3 pairs requirement satisfies ≥2 bar |
| C-14 | FAIL (0) | No IF-THEN syntactic template on likelihood field |
| C-15 | FAIL (0) | No Mitigation Type field or sub-field obligations |
| C-16 | PASS (2) | "at least 3 pairings are required. If fewer than 3... your risks are not specific enough — go back to Phase 2" — explicit backward pressure |

**Composite: 60 + 30 + 2 + 1 + 1 + 1 + 2 + 0 + 0 + 2 = 99** | GOLDEN

---

### V-02 — Output Format (IF-THEN as table schema template)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "always the first entry" |
| C-02 | PASS | "Cover at least 3 of: Technical, Market, Compliance, Dependency, Timeline" |
| C-03 | PASS | Table schema includes all anatomy fields |
| C-04 | PASS | "Severity: HIGH / MEDIUM / LOW — no other values" |
| C-05 | PASS | Forbidden mitigation words list + type vocabulary structurally reduce generics |
| C-06 | PASS | Dimension column in table schema |
| C-07 | PASS | IF-THEN column enforces condition-based likelihood across all entries |
| C-08 | PASS | "Sort rows by severity descending" |
| C-09 | FAIL (0) | "Note any risks that compound each other" — conditional phrasing, model may produce 0 |
| C-10 | PARTIAL (1) | AMEND in Step 4 handles correctly; no live directive |
| C-11 | PARTIAL (1) | Forbidden word list + type column reduce generics but no sub-field obligations — non-listed equivalent non-actions could survive |
| C-12 | PASS (2) | Column header `IF [condition], THEN risk activates` is the template cell text; "Do not write 'high', 'possible', '~30%'" explicit exclusion |
| C-13 | FAIL (0) | No dedicated section requirement; no ≥2 minimum |
| C-14 | PASS (2) | Column header embeds the IF-THEN syntactic form as a schema completion task |
| C-15 | FAIL (0) | Type column requires a label; type definitions describe sub-fields but sub-fields not declared as required outputs |
| C-16 | FAIL (0) | No ≥3 pairs requirement |

**Composite: 60 + 30 + 0 + 1 + 1 + 2 + 0 + 2 + 0 + 0 = 96** | GOLDEN

---

### V-03 — Phrasing Register (type contract sub-fields)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Mandatory first entry |
| C-02 | PASS | "3 or more of these dimensions" |
| C-03 | PASS | All anatomy fields required per entry |
| C-04 | PASS | "HIGH, MEDIUM, or LOW — nothing else" |
| C-05 | PASS | "Generic hedges... are incompatible with all six types — no type contract can be fulfilled by a generic phrase" |
| C-06 | PASS | Dimension field per risk |
| C-07 | PASS | "what specific condition or scenario triggers this risk — not just 'possible'" |
| C-08 | PASS | "Sort dimensional risks from highest to lowest severity" |
| C-09 | FAIL (0) | "If any two risks compound each other..." — conditional, not mandatory. Model may skip. |
| C-10 | PARTIAL (1) | AMEND in Step 5 handles correctly; no live directive |
| C-11 | PASS (2) | Sub-field obligations per type make generic hedges structurally incompatible — a Spike without named unknown and time-box is "incomplete"; gate requires named criterion; no type contract can accept "monitor closely" |
| C-12 | PARTIAL (1) | "what specific condition or scenario triggers this risk" is semantic; without IF-THEN template, some entries may still read as plain conditions rather than explicit trigger-qualified statements |
| C-13 | FAIL (0) | No dedicated interdependency section; no minimum count |
| C-14 | FAIL (0) | No IF-THEN syntactic template |
| C-15 | PASS (2) | Sub-field obligations explicitly required per type: "Spike without a named unknown and time-box is incomplete. Gate without a named criterion is incomplete." Every type has named required outputs. |
| C-16 | FAIL (0) | No ≥3 pairs requirement |

**Composite: 60 + 30 + 0 + 1 + 2 + 1 + 0 + 0 + 2 + 0 = 96** | GOLDEN

---

### V-04 — Lifecycle + Output Format (≥3 pairs + IF-THEN schema)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Mandatory first entry |
| C-02 | PASS | "Cover at least 3 of" |
| C-03 | PASS | Table schema + inertia format covers all fields |
| C-04 | PASS | "only HIGH, MEDIUM, or LOW — no numbers, percentages, or invented labels" |
| C-05 | PASS | Forbidden words list + type vocabulary + type definitions + self-check item |
| C-06 | PASS | Dimension column in table |
| C-07 | PASS | IF-THEN column enforces condition-based likelihood |
| C-08 | PASS | "Sort rows by severity descending" + self-check item |
| C-09 | PASS (2) | Mandatory `## Risk Interdependencies` section with ≥3 named pairs |
| C-10 | PARTIAL (1) | AMEND in Step 5 with correct inertia + section retention; no live directive |
| C-11 | PASS (2) | Forbidden words + type column in schema + type definitions + self-check: "No forbidden mitigation words in any entry" |
| C-12 | PASS (2) | IF-THEN column header template + self-check: "Every likelihood cell in the table starts with 'IF' — scan every row" |
| C-13 | PASS (2) | Mandatory `## Risk Interdependencies` section with ≥3 named pairs satisfies ≥2 bar |
| C-14 | PASS (2) | IF-THEN schema template in column header |
| C-15 | PARTIAL (1) | Mitigation Type column requires a label and definitions describe sub-fields, but sub-field outputs are not declared as required named fields. Model may fulfill the type spirit without naming the unknown, time-box, or criterion explicitly. |
| C-16 | PASS (2) | "at least 3 named compound-risk pairings" + "If you find fewer than 3... your risks are not specific enough — revise Phase 2" |

**Composite: 60 + 30 + 2 + 1 + 2 + 2 + 2 + 2 + 1 + 2 = 104** | GOLDEN

---

### V-05 — Full Integration (R2 V-05 base + all v3 upgrades)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | "STEP 1 — INERTIA RISK (mandatory, always first)" — prominent header |
| C-02 | PASS | Three-role decomposition covers Technical+Dependency (Realist), Market+Compliance (Skeptic), Timeline (Scheduler) by construction |
| C-03 | PASS | All anatomy fields required in STEP 1 format + table schema |
| C-04 | PASS | "Severity values are only HIGH, MEDIUM, or LOW — no numbers, percentages, or invented labels" in self-check |
| C-05 | PASS | Sub-field type contracts + forbidden text list + "if you draft one, replace it with a typed mitigation before continuing" |
| C-06 | PASS | Dimension column in table |
| C-07 | PASS | IF-THEN column header enforces condition-based likelihood |
| C-08 | PASS | "sorted by severity descending after inertia" |
| C-09 | PASS (2) | Mandatory STEP 3 with ≥3 named pairs |
| C-10 | PARTIAL (1) | STEP 5 AMEND handling is correct (keep inertia + interdependencies section); no live directive |
| C-11 | PASS (2) | Sub-field contracts make "monitor closely" structurally impossible per type + forbidden text list + "Fulfilling the sub-fields makes generic hedges structurally impossible" stated explicitly |
| C-12 | PASS (2) | IF-THEN column header template; self-check: "Every likelihood cell starts with 'IF' — scan every row; no bare probability labels" |
| C-13 | PASS (2) | Mandatory `## Risk Interdependencies` section with ≥3 named pairs |
| C-14 | PASS (2) | Column header template is the syntactic enforcer; "Bare probability labels ('high', '~30%', 'possible', 'likely when') cannot satisfy a column that begins with 'IF'" |
| C-15 | PASS (2) | Sub-field templates per type declared as required outputs: "A mitigation is only complete when its named sub-fields are filled in. A Spike without a named unknown and time-box is incomplete." Self-check: "Every mitigation fulfills its type contract (named sub-fields present)" |
| C-16 | PASS (2) | "Minimum 3 named pairs. If you find fewer than 3 after reviewing all rows, your risks are too generic — revise STEP 2." |

**Composite: 60 + 30 + 2 + 1 + 2 + 2 + 2 + 2 + 2 + 2 = 105** | GOLDEN

---

### Rankings

| Rank | Variation | Score | Golden | Key differentiator |
|------|-----------|-------|--------|--------------------|
| 1 | **V-05** | **105** | YES | All three v3 mechanisms + sub-field obligations as required named outputs |
| 2 | **V-04** | **104** | YES | All three v3 mechanisms; type definitions present but sub-fields not required → C-15 PARTIAL |
| 3 | **V-01** | **99** | YES | C-16 isolated cleanly; no IF-THEN or type taxonomy → C-14/C-15 absent |
| 4 | **V-02** | **96** | YES | C-14 via schema template; no interdependency section or sub-fields → C-13/C-15/C-16 absent |
| 4 | **V-03** | **96** | YES | C-15 via sub-field obligations; no IF-THEN or interdependency section → C-12/C-13/C-14/C-16 absent |

---

### Excellence Signals

**Signal 1 — Sub-field templates as required outputs vs. type definitions alone (V-05 vs V-04, C-15)**
V-04 provides type definitions and a Mitigation Type column but does not require sub-fields as named outputs. V-05 adds: "A mitigation is only complete when its named sub-fields are filled in. A Spike without a named unknown and time-box is incomplete." This single addition moves C-15 from PARTIAL to PASS. The pattern: structural obligation requires named required fields, not just vocabulary definitions.

**Signal 2 — C-10 ceiling is stable at PARTIAL across all base prompts**
All five variations hit PARTIAL on C-10. AMEND behavior requires a live directive to demonstrate; no base prompt can produce PASS. The 105/106 ceiling is confirmed as the theoretical max for base-prompt evaluation. R4 cannot improve this without introducing a paired AMEND test variation.

---

```json
{"top_score": 105, "all_essential_pass": true, "new_patterns": ["Sub-field templates as required named outputs (V-05) achieve C-15 PASS; type definitions alone (V-04) achieve only PARTIAL — the distinction is whether the prompt declares sub-fields as required outputs or merely describes their meaning"]}
```
