## Scoring: flow-conversation Variations — Round 1

### Point Weights

| Tier | Per Criterion |
|------|--------------|
| Essential (C-01–C-04) | 15 pts each |
| Recommended (C-05–C-07) | 10 pts each |
| Aspirational (C-08–C-09) | 5 pts each |

PASS = full | PARTIAL = half | FAIL = 0

---

### V-01 — Role Sequence

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Role-primed CS context drives a complete turn-by-turn trace |
| C-02 Defect report (all 4 types) | PASS | CS vocabulary in role block causes defect labels to arrive in domain-specific form |
| C-03 Intent–response pairing | PASS | Prose-led trace pairs both sides per turn |
| C-04 Fallback handling | PASS | Step 3 exception path explicitly covers fallback |
| C-05 Session state tracked | PARTIAL | Role sets expectation but prose steps leave this abstract |
| C-06 Multi-path coverage | PARTIAL | Only one exception path specified; divergence shallow |
| C-07 Topic graph completeness | PARTIAL | No node inventory required; Step 1 topic inventory may stay as a list |
| C-08 CS vocabulary | PASS | Role priming delivers trigger phrases, redirect nodes, system topics organically |
| C-09 Actionable remediation | PARTIAL | No specificity enforcement; generic advice not prohibited |

**Score:** 15+15+15+15+5+5+5+5+2.5 = **82.5**

---

### V-02 — Output Format (table-heavy)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Dialog trace table with required columns prevents omission |
| C-02 Defect report (all 4 types) | PASS | Defect table with one row per type + required Verdict cell forces all 4 |
| C-03 Intent–response pairing | PASS | Separate User Utterance / Agent Response columns structurally enforce pairing |
| C-04 Fallback handling | PASS | Exception path section present |
| C-05 Session state tracked | PASS | Dedicated table section forces a state column |
| C-06 Multi-path coverage | PARTIAL | Two trace tables present but divergence between paths may be minimal |
| C-07 Topic graph completeness | PASS | Node inventory table with required rows covers the graph |
| C-08 CS vocabulary | PARTIAL | Generic column headers ("User Input", "Bot Response") — no CS-specific label enforcement |
| C-09 Actionable remediation | PARTIAL | Remediation column present but "Fix" label permits generic entries |

**Score:** 15+15+15+15+10+5+10+2.5+2.5 = **90**

---

### V-03 — Lifecycle Emphasis

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | HAPPY PATH phase exit condition requires complete trace |
| C-02 Defect report (all 4 types) | PASS | DEFECT SCAN phase has four named sub-checks; exit condition blocks "no issues" collapse |
| C-03 Intent–response pairing | PASS | Phase structure drives both sides per turn |
| C-04 Fallback handling | PASS | EXCEPTION PATH is a named phase with its own entry condition |
| C-05 Session state tracked | PASS | State tracking required as phase entry context |
| C-06 Multi-path coverage | PASS | HAPPY PATH + EXCEPTION PATH are separate gates; coverage summary phase checks both |
| C-07 Topic graph completeness | PASS | TOPIC INVENTORY phase exit condition requires node list |
| C-08 CS vocabulary | PARTIAL | Phase names are generic; no CS-specific vocabulary requirement in any gate |
| C-09 Actionable remediation | PARTIAL | REMEDIATION phase present but specificity not enforced by exit condition |

**Score:** 15+15+15+15+10+10+10+2.5+2.5 = **95**

---

### V-04 — Role Sequence + Phrasing Register

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | MUST clause tied to trace completeness |
| C-02 Defect report (all 4 types) | PASS | MUST clause per defect type |
| C-03 Intent–response pairing | PASS | Directive: "you MUST name the node" drives both sides |
| C-04 Fallback handling | PASS | Explicit MUST for exception path |
| C-05 Session state tracked | PASS | Directed by imperative |
| C-06 Multi-path coverage | PASS | Both paths required by directive |
| C-07 Topic graph completeness | PASS | Node inventory required by directive |
| C-08 CS vocabulary | PASS | Role block primes CS vocabulary; imperative directives reinforce domain labels |
| C-09 Actionable remediation | PASS | Explicit prohibition: "do not write 'add better error handling'" — names the failure mode and bans it |

**Score:** 15+15+15+15+10+10+10+5+5 = **100**

---

### V-05 — Lifecycle + Output Format + Phrasing Register (ceiling)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | PASS | Phase gate + required trace table with named columns |
| C-02 Defect report (all 4 types) | PASS | "ALL FOUR defect type rows MUST appear" + table schema with Severity column |
| C-03 Intent–response pairing | PASS | Table columns enforce pairing; "Do NOT leave Agent Response blank" closes gap |
| C-04 Fallback handling | PASS | EXCEPTION PATH is a named phase gate with exit condition |
| C-05 Session state tracked | PASS | Required column in trace table |
| C-06 Multi-path coverage | PASS | Two separate phase gates, each with a required table |
| C-07 Topic graph completeness | PASS | TOPIC INVENTORY gate with node inventory table |
| C-08 CS vocabulary | PASS | "Copilot Studio Object to Edit" column in remediation table forces CS-specific labels in every row |
| C-09 Actionable remediation | PASS | Same column forces specificity: a cell cannot say "improve error handling" if the column demands a CS UI path |

**Score:** 15+15+15+15+10+10+10+5+5 = **100**

---

### Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 (tie) | V-05 — Ceiling (all three axes) | 100 | Yes |
| 1 (tie) | V-04 — Role + Register | 100 | Yes |
| 3 | V-03 — Lifecycle | 95 | Yes |
| 4 | V-02 — Table Format | 90 | Yes |
| 5 | V-01 — Role Sequence | 82.5 | Yes |

**Top variation: V-05** — scored first by structural robustness. V-04 achieves the same rubric score but relies on imperative language to enforce C-08/C-09; V-05 encodes both into a table column that cannot be completed without CS-specific input.

---

### Excellence Signals from V-05

**Signal 1: Column name as constraint.** The "Copilot Studio Object to Edit" column in the remediation table forces C-08 and C-09 simultaneously without adding any extra instruction. A column header is a tighter contract than a prose directive — it cannot be skipped without producing a visibly incomplete table.

**Signal 2: Phase gates eliminate phase omission; table schemas eliminate row omission.** The two mechanisms operate at different granularities. Phase gates prevent missing sections. Table schemas prevent missing rows within a section. Used together they close both failure modes.

**Signal 3: Name the failure mode, not just the requirement.** V-04/V-05's "do not write 'add better error handling'" outperforms "provide actionable remediation" because it describes what non-compliance looks like. Naming the bad output is more constraining than naming the good output.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Column name as dual constraint: a table column requiring a CS-specific object name enforces both vocabulary (C-08) and specificity (C-09) without additional prose", "Phase gates × table schemas operate at different granularities — gates prevent missing sections, schemas prevent missing rows — combined they close both omission failure modes", "Name the failure mode explicitly: prohibiting 'add better error handling' is a tighter constraint than requiring 'actionable remediation' because it describes what non-compliance looks like"]}
```
