## flow-conversation — Round 2 Scoring (Rubric v2, C-01–C-12)

**Note:** Trace artifact is `placeholder`. Scoring evaluates prompt enforcement strength — whether each variation's structure forces compliant model output — not against a live artifact.

---

### Scoring Basis

All five R2 variations are built on the R1 V-04/V-05 foundation. C-01 through C-09 score is treated as the **shared base** (100 pts) because each variation carries the structural elements that passed those criteria in R1. The Round 2 differentiation is entirely on C-10/C-11/C-12 (+5 pts each, max 115).

Point scale: Essential C-01–C-04 = 15 pts each; Recommended C-05–C-07 = 10 pts each; Aspirational C-08–C-12 = 5 pts each.

---

### Per-Variation Scores

#### V-01 — Named Prohibitions

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Artifact structure | PASS | Six numbered sections, output artifact path defined |
| C-02 Defect report | PASS | Section 4 lists all four types; named prohibition blocks generic summary |
| C-03 Intent–response pairing | PASS | Section 2 requires "user intent label + utterance" AND "agent's exact response" |
| C-04 Fallback handling | PASS | Section 3 exception path + Section 4 missing-fallback type coverage |
| C-05 Session state | PASS | "session variable delta (name and value)" required per turn |
| C-06 Multi-path | PASS | Sections 2 + 3 = happy + exception paths |
| C-07 Node coverage | PASS | Section 6 coverage summary with per-node status |
| C-08 (aspirational) | PASS | R1 baseline: V-04/V-05 passed |
| C-09 (aspirational) | PASS | R1 baseline: V-04/V-05 passed |
| **C-10 Named prohibitions** | **PASS** | Inline "Do NOT write: [example]" at every instruction site — dead-end pattern named at point of use |
| **C-11 CS column headers** | **FAIL** | Prose instructions only; no table schema forcing CS vocabulary |
| **C-12 Phase exit conditions** | **FAIL** | No phase gates; no MAY NOT constraints |

**Score: 105 / 115** (all essential PASS)

---

#### V-02 — CS Column Headers

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Six table-structured sections |
| C-02 | PASS | Section 4 table requires all four defect types; "Found / Not found only" rule blocks vague verdicts |
| C-03 | PASS | Separate columns: "Trigger Phrase / User Utterance" AND "Agent Response (Message Node Text)" |
| C-04 | PASS | Section 3 exception trace + Section 4 missing-fallback row in defect table |
| C-05 | PASS | "Session Variable Delta" column present in trace tables |
| C-06 | PASS | Section 2 (happy) + Section 3 (exception) = two structural paths |
| C-07 | PASS | Section 6 coverage summary table |
| C-08 | PASS | R1 baseline |
| C-09 | PASS | R1 baseline |
| **C-10 Named prohibitions** | **FAIL** | No inline prohibitions; no named degenerate-output examples at instruction sites |
| **C-11 CS column headers** | **PASS** | "Topic Node (Copilot Studio)", "Copilot Studio Object to Edit", "Redirect Target / System Topic" — every table cell becomes a CS artifact by schema |
| **C-12 Phase exit conditions** | **FAIL** | No phase structure; no MAY NOT gates |

**Score: 105 / 115** (all essential PASS)

---

#### V-03 — Phase Exit Conditions

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Phase structure with named entry/exit conditions |
| C-02 | PASS | Phase 4 (implied from structure) covers defect scan; exit conditions prevent empty verdicts |
| C-03 | PASS | Phase 2 requires "user intent + utterance" AND "exact agent response" per turn |
| C-04 | PASS | Phase 1 inventory has "Fallback Defined?" column; exit condition blocks empty cells |
| C-05 | PASS | Phase 2 includes "session variable delta" |
| C-06 | PASS | Phase 2 (happy) + Phase 3 (exception, implied) = two paths |
| C-07 | PASS | Phase structure enforces completeness |
| C-08 | PASS | R1 baseline |
| C-09 | PASS | R1 baseline |
| **C-10 Named prohibitions** | **FAIL** | No inline "Do NOT write" examples — MAY NOT gates name failure *forms*, not output *instances* |
| **C-11 CS column headers** | **FAIL** | Phase 1 table uses "Node" not "Topic Node (Copilot Studio)"; no CS-vocabulary column schema in trace tables |
| **C-12 Phase exit conditions** | **PASS** | "MAY NOT proceed if any row has an empty cell"; "MAY NOT end trace on active topic node" — hard negative constraints blocking the two primary collapse patterns |

**Score: 105 / 115** (all essential PASS)

---

#### V-04 — C-10 + C-11 Combined

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-09 | PASS | All inherited from component designs |
| **C-10 Named prohibitions** | **PASS** | Inherits V-01's inline named prohibitions |
| **C-11 CS column headers** | **PASS** | Inherits V-02's CS column schema |
| **C-12 Phase exit conditions** | **FAIL** | Neither V-01 nor V-02 has phase exit conditions |

**Score: 110 / 115** (all essential PASS)

---

#### V-05 — All Three Combined (Ceiling)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-09 | PASS | All inherited |
| **C-10 Named prohibitions** | **PASS** | Inline at every instruction site |
| **C-11 CS column headers** | **PASS** | CS-vocabulary column schema throughout all tables |
| **C-12 Phase exit conditions** | **PASS** | Hard MAY NOT gates at each phase transition |

**Score: 115 / 115** (all essential PASS)

---

### Ranking

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-05 | 115 / 115 | Yes |
| 2 | V-04 | 110 / 115 | Yes |
| 3 (tie) | V-01 | 105 / 115 | Yes |
| 3 (tie) | V-02 | 105 / 115 | Yes |
| 3 (tie) | V-03 | 105 / 115 | Yes |

All five R2 variations clear the 80-point golden threshold. V-05 is the only one to achieve all three new aspirational criteria simultaneously.

---

### Excellence Signals — V-05

**1. Layered enforcement: three independent collapse-prevention mechanisms**
V-05's three axes operate at different levels of the prompt — inline prohibition (prose), column schema (table), phase gate (structure) — so a degenerate response that evades one mechanism is caught by another. No single axis is sufficient; the ceiling requires all three.

**2. Named failure-mode proximity**
The named prohibition ("Do NOT write: 'Agent responds appropriately'") appears at the moment the model is forming that response, not in a preamble it has already processed. Spatial proximity of the banned form to the instruction it governs is what makes C-10 different from a general "be specific" instruction.

**3. CS column schema as vocabulary constraint, not just formatting**
"Copilot Studio Object to Edit" as a column header makes every cell in that column require a CS artifact path. Role priming asks the model to use CS vocabulary; column schema makes it structurally impossible to fill the cell without one. This is enforcement without reliance on the model's domain knowledge activation.

**4. MAY NOT gates naming the blocked failure, not the desired state**
"MAY NOT end the trace on an active topic node" forces the model to check for the specific named failure before proceeding. A positive gate ("must show terminal state") allows the model to declare completion and move on. A negative gate ("cannot proceed if [named failure present]") creates a detectable condition the model must actively falsify.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["Layered enforcement across prose/table/structure: three mechanisms catch what any single axis misses", "Named prohibition at instruction site (not preamble): spatial proximity to the instruction it governs is the operative technique", "Column header as vocabulary constraint: CS-specific schema prevents non-CS cell content by construction", "MAY NOT gate names the blocked failure form, not the desired outcome: creates a detectable negative the model must actively falsify"]}
```
