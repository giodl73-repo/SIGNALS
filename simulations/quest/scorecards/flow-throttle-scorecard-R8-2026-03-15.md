I have the full text of all 5 variations. Let me now score each against the complete rubric.

---

# flow-throttle — Round 8 Scorecard (v8 Rubric)

**Scoring basis:** Prompt structure analysis. No trace artifact provided; scoring evaluates whether each prompt design reliably elicits outputs satisfying each criterion.

**Point values:** Essential C-01–C-05 = 12 pts each (60 total) | Recommended C-06–C-08 = 10 pts each (30 total) | Aspirational C-09–C-24 = 5 pts each (80 total) | **Max: 170**

---

## V-01 — C-23 Inline Prose-Exception Citations Only

**Design axis:** Adds INLINE PROSE AUTHORIZATION REQUIREMENT (`[prose: item N — context label]` tags) to the R7 V-01 golden. No structural changes to derived tables (C-21), no TABLE E (C-22), no TYPE SCAN GATE (C-24).

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | TABLE A "Binding at band" column + Step 1B causal mechanism required; `Load-shape verdict` must name the mechanism. |
| C-02 | **PASS** | TABLE B minimum 2 hops enforced; mechanism column restricted to queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. |
| C-03 | **PASS** | TABLE A requires Component + Scope per row; STEP 1A GATE blocks progression until all rows populated. |
| C-04 | **PASS** | TABLE C (Step 2B) requires one row per TABLE A Tier-ID; no tier may be omitted. |
| C-05 | **PASS** | TABLE D (Step 2C) requires at least one burst path row; explicit scope-violation prohibition prevents late tier invention. |

**Essential subtotal: 60/60**

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Step 2F Retry-After Gap Assessment explicitly required for 1x binding tier with named failure mode distinction. |
| C-07 | **PASS** | Step 2E CASCADE SCENARIO requires minimum 3 tiers, each causal link explicit. |
| C-08 | **PASS** | `Limit (number + unit)` column in TABLE A; vague label compliance failure condition stated. |

**Recommended subtotal: 30/30**

### Aspirational (80 pts max)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | TABLE F Step 2H includes `Expected outcome` column; mitigation entry with outcome satisfies tradeoff intent. 2+ rows required by table structure. |
| C-10 | **PASS** | Violation type + compliance failure condition for vague label in `Limit` column; error-code column requires "Specific HTTP status code or platform signal." |
| C-11 | **PASS** | Numbers must come from signal data read in full (PHASE ENTRY CONDITION Step 1A); no vague labels permitted. |
| C-12 | **PASS** | CLOSING AUDIT section: "Confirm C-01 through C-08 compliance. For each criterion, state PASS or FAIL." |
| C-13 | **PASS** | TABLE A functions as source register — numeric limits committed before any tier classification or analysis phase opens; STEP 1A GATE enforces completion of evidence base before Step 1B. |
| C-14 | **PASS** | `Binding at band` column with "N/A if never" for non-binding tiers; Load-shape verdict at Step 1B requires numeric rate differential and mechanism, providing contrastive evidence. |
| C-15 | **PASS** | Volume Analyst (Step 1A) → Load-shape Analyst (Step 1B) roles with locked phase entry/exit conditions; executor cannot open Step 2 until Step 1B GATE clears. |
| C-16 | **PASS** | STEP 1A GATE prohibition: "SHALL NOT open Step 1B until this gate is cleared." STEP 1B GATE prohibition: "SHALL NOT begin STEP 2 until this phase exit condition is met." Explicit prohibition form present. |
| C-17 | **PASS** | TABLE C anchor: "One row per TABLE A Tier-ID. No tier SHALL be omitted." Names the prior artifact as controlling input. |
| C-18 | **PASS** | "REGISTRY GAP PROHIBITION — **Failure 5 prevention (C-17)**" and "**Failure 2 + Failure 6 prevention (C-16, C-20, C-23)**" — prohibitions annotated with failure mode references at each phase boundary. |
| C-19 | **PASS** | CLOSING AUDIT names C-01 through C-08 by ID and requires per-criterion PASS/FAIL verdict — dedicated criterion-coverage step. |
| C-20 | **PASS** | PROSE-RESTRICTION DECLARATION present: "This list is complete and closed" with 4 numbered contexts. All other content "SHALL be expressed in tables." |
| C-21 | **FAIL** | No cross-artifact header lines on TABLE B through TABLE F. TABLE B has column definitions only; no "*[TABLE B — Source: TABLE A...]*" header with upstream identifier and coverage obligation. |
| C-22 | **FAIL** | No TABLE E. No `Type` column. Risk taxonomy (Burst / Cascade / RetryAfter) absent; type-category gaps not detectable by scan. |
| C-23 | **PASS** | INLINE PROSE AUTHORIZATION REQUIREMENT block present: `[prose: item N — context label]` required at each prose passage; 4 required opening forms specified; missing tag = "unauthorized regardless of content." |
| C-24 | **FAIL** | No TYPE SCAN GATE between risk inventory and mitigation phase. Mitigation table (TABLE F Step 2H) opens without any gate step. |

**Aspirational subtotal: 55 + 10 = 65/80**
*(C-09–C-19 = 55 | C-20 = 5, C-21 = 0, C-22 = 0, C-23 = 5, C-24 = 0)*

### V-01 Composite: **155/170** | All essential PASS | ≥ 80 threshold: **MET** ✓

---

## V-02 — C-22 + C-24: Typed Risk Inventory and TYPE SCAN GATE Only

**Design axis:** Adds TABLE E (typed risk inventory with Burst/Cascade/RetryAfter Type column + per-type minimum constraint) and TYPE SCAN GATE between TABLE E and renamed Step 2I (mitigation registry). No prose-restriction declaration (C-20), no cross-artifact headers (C-21), no inline citations (C-23).

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Same TABLE A + Step 1B structure; binding tier + causal mechanism required. |
| C-02 | **PASS** | TABLE B minimum 2 hops, specific mechanism values required. |
| C-03 | **PASS** | TABLE A with Component + Scope. |
| C-04 | **PASS** | TABLE C one row per TABLE A Tier-ID. |
| C-05 | **PASS** | TABLE D at least one burst path row. |

**Essential subtotal: 60/60**

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Step 2F present. |
| C-07 | **PASS** | Step 2E cascade minimum 3 tiers. |
| C-08 | **PASS** | Numeric limits required. |

**Recommended subtotal: 30/30**

### Aspirational (80 pts max)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | TABLE F (Step 2I) has explicit `Tradeoff` column: "MR-ID \| Risk-ID (TABLE E) \| Component \| Setting or API parameter \| Change \| Expected outcome \| Tradeoff." |
| C-10 | **PASS** | Vague-label violation type + compliance failure condition present. |
| C-11 | **PASS** | Numbers from signal; no vague labels permitted. |
| C-12 | **PASS** | CLOSING AUDIT present. |
| C-13 | **PASS** | TABLE A register commits evidence base before analysis phases open. |
| C-14 | **PASS** | `Binding at band` + N/A for non-binding tiers; Load-shape verdict requires mechanism. |
| C-15 | **PASS** | Volume Analyst → Load-shape Analyst locked sequencing with phase entry/exit conditions. |
| C-16 | **PASS** | STEP 1A/1B GATE prohibition statements present. |
| C-17 | **PASS** | TABLE C anchor names TABLE A as controlling input. |
| C-18 | **PASS** | REGISTRY GAP PROHIBITION annotated "Failure 5 prevention (C-17)"; Step 1B prohibition annotated "Failure 2 + Failure 6 prevention (C-16)." |
| C-19 | **PASS** | CLOSING AUDIT names C-01 through C-08 by ID. |
| C-20 | **FAIL** | No PROSE-RESTRICTION DECLARATION. Narrative sections (escape-route frame at Step 1B, UNIFORM/BURST at Step 2G) produce prose without declared permission structure. |
| C-21 | **FAIL** | No upstream source identifier headers on TABLE B, TABLE C, TABLE D, TABLE F. Tables present without "Source: TABLE A" header or coverage obligation statement. |
| C-22 | **PASS** | TABLE E (Step 2H) with `Type (Burst / Cascade / RetryAfter)` column; per-type minimum-row constraint stated: "at least one Burst row, at least one Cascade row, at least one RetryAfter row." Typed taxonomy makes category absence detectable by scan. |
| C-23 | **FAIL** | No INLINE PROSE AUTHORIZATION REQUIREMENT. Prose passages (escape-route frame, load-shape narrative) carry no `[prose: item N]` tags; unauthorized prose not detectable by tag-scan. |
| C-24 | **PASS** | TYPE SCAN GATE present between TABLE E and Step 2I: enumerates Burst/Cascade/RetryAfter presence with [PRESENT/ABSENT] verdict per category; explicit PROCEED/BLOCK decision; "SHALL NOT open Step 2I until this gate reports PROCEED." |

**Aspirational subtotal: 55 + 10 = 65/80**
*(C-09–C-19 = 55 | C-20 = 0, C-21 = 0, C-22 = 5, C-23 = 0, C-24 = 5)*

### V-02 Composite: **155/170** | All essential PASS | ≥ 80 threshold: **MET** ✓

---

## V-03 — C-21 + C-22 + C-24: Cross-Artifact Headers + Gate

**Design axis:** Combines cross-artifact referential integrity headers (C-21) on all derived tables with typed risk inventory (C-22) and TYPE SCAN GATE (C-24). No prose-restriction declaration (C-20), no inline citations (C-23).

### Essential (60 pts) — All PASS (identical structure, same result as V-01/V-02) — **60/60**

### Recommended (30 pts) — All PASS — **30/30**

### Aspirational (80 pts max)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | TABLE F (Step 2I) has `Tradeoff` column. |
| C-10–C-19 | **PASS** ×10 | Same prohibition + gate + annotation structure as V-01/V-02; C-18 annotations present at all phase boundaries. |
| C-20 | **FAIL** | No PROSE-RESTRICTION DECLARATION. Step 1B escape-route text, Step 2G narrative are unrestricted prose. |
| C-21 | **PASS** | Every derived artifact carries upstream source header co-located at the table: TABLE A ("*[Primary artifact. All downstream tables derive from TABLE A...]*"), TABLE B ("*[TABLE B — Source: TABLE A. ...No hop may reference a Tier-ID absent from TABLE A.]*"), TABLE C ("*[TABLE C — Source: TABLE A. One row per T-NN...Row count MUST equal TABLE A.]*"), TABLE D, RANKING, CASCADE, TABLE E ("*[Source: TABLE A + TABLE B + TABLE D...]*"), TABLE F ("*[TABLE F — Source: TABLE E. One row per TABLE E Risk-ID...]*"). All headers co-located, not prose-adjacent. |
| C-22 | **PASS** | TABLE E with `Type` column + per-type minimum constraint; gate entry condition blocks progression if type absent. |
| C-23 | **FAIL** | No inline prose authorization tags. Prose passages in Step 1B and Step 2G carry no `[prose: item N]` citation. |
| C-24 | **PASS** | TYPE SCAN GATE with Burst/Cascade/RetryAfter enumeration; PROCEED/BLOCK gate verdict required; "SHALL NOT open Step 2I until this gate reports PROCEED." |

**Aspirational subtotal: 55 + 15 = 70/80**
*(C-09–C-19 = 55 | C-20 = 0, C-21 = 5, C-22 = 5, C-23 = 0, C-24 = 5)*

### V-03 Composite: **160/170** | All essential PASS | ≥ 80 threshold: **MET** ✓

---

## V-04 — C-20 + C-21 + C-22 + C-23 (No Gate)

**Design axis:** Full format discipline — prose-restriction declaration (C-20), cross-artifact headers (C-21), typed risk inventory (C-22), inline prose citations (C-23). TYPE SCAN GATE (C-24) deliberately absent; TABLE E present with Type column but no structural gate before TABLE F.

### Essential (60 pts) — All PASS — **60/60**

### Recommended (30 pts) — All PASS — **30/30**

### Aspirational (80 pts max)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | TABLE F (Step 2I) has explicit `Tradeoff` column. |
| C-10–C-19 | **PASS** ×10 | Full prohibition/gate/annotation structure carried forward. |
| C-20 | **PASS** | PROSE-RESTRICTION DECLARATION present: "complete and closed" with 4 numbered contexts; "prose outside these contexts is a format violation." |
| C-21 | **PASS** | All 7 derived artifacts carry co-located source identifier + coverage obligation headers: TABLE B ("Source: TABLE A. Minimum 2 hops. No hop references a Tier-ID absent from TABLE A."), TABLE C (row-count equality constraint), TABLE D, RANKING, CASCADE, TABLE E (multi-source), TABLE F (Source: TABLE E, row-count constraint). |
| C-22 | **PASS** | TABLE E with `Type (Burst / Cascade / RetryAfter)` column; per-type minimum-row constraint; "No type category absent." |
| C-23 | **PASS** | INLINE PROSE AUTHORIZATION REQUIREMENT present; `[prose: item N — context label]` tags required; 4 required opening forms with explicit format ("Item 1: `[prose: item 1 — load-shape mechanism]` \| Item 2: ..."); missing tag = "unauthorized"; non-existent item number = "format violation detectable by tag-scan." |
| C-24 | **FAIL** | No TYPE SCAN GATE. Prompt explicitly notes: "*(Note: No TYPE SCAN GATE is present in this variation. Type completeness is verifiable by reading TABLE E but there is no structural step that makes a missing category a block.)*" Step 2I (mitigation) opens after Step 2H without gate checkpoint. |

**Aspirational subtotal: 55 + 20 = 75/80**
*(C-09–C-19 = 55 | C-20 = 5, C-21 = 5, C-22 = 5, C-23 = 5, C-24 = 0)*

### V-04 Composite: **165/170** | All essential PASS | ≥ 80 threshold: **MET** ✓

---

## V-05 — Maximum: All C-20 Through C-24

**Design axis:** Full combination — all five criteria: prose-restriction declaration (C-20), cross-artifact headers (C-21), typed risk inventory (C-22), inline prose citations (C-23), TYPE SCAN GATE (C-24). Also adds a structured-output exemption clause to C-20/C-23 to prevent gate verdicts from requiring prose tags.

### Essential (60 pts) — All PASS — **60/60**

### Recommended (30 pts) — All PASS — **30/30**

### Aspirational (80 pts max)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | TABLE F (Step 2I) has `Tradeoff` column. |
| C-10–C-19 | **PASS** ×10 | All prohibitions, gates, annotations, sequencing, enumeration anchors carried forward. |
| C-20 | **PASS** | PROSE-RESTRICTION DECLARATION with 4 numbered contexts + structural-output exemption: "Gate decision lines (PROCEED / BLOCKED) and cross-artifact header lines are structured output, not prose, and do not require inline prose citation tags." Makes the boundary between prose and structured output explicit — no ambiguity when gate verdicts and header lines coexist with prose restriction. |
| C-21 | **PASS** | All derived artifacts carry co-located headers with upstream source and coverage obligation; TABLE A header adds "No downstream section may reference a Tier-ID absent from TABLE A." |
| C-22 | **PASS** | TABLE E with Type column + per-type minimum coverage + gate enforcement. |
| C-23 | **PASS** | INLINE PROSE AUTHORIZATION REQUIREMENT with 4 required opening forms; gate decisions and header lines explicitly exempt: "Gate decision lines and cross-artifact header lines are exempt from inline citation tagging." |
| C-24 | **PASS** | TYPE SCAN GATE (C-24) present with explicit `Purpose` annotation: "**Purpose — prevents category elision:** C-22 ensures the Type column is present...This gate ensures type completeness is an explicit named structural check, not an implicit property verifiable only by reading TABLE E in full." Gate enumerates Burst/Cascade/RetryAfter with PRESENT/ABSENT verdict per category; BLOCKED decision names the recovery action. |

**Aspirational subtotal: 55 + 25 = 80/80**
*(C-09–C-19 = 55 | C-20 = 5, C-21 = 5, C-22 = 5, C-23 = 5, C-24 = 5)*

### V-05 Composite: **170/170** | All essential PASS | ≥ 80 threshold: **MET** ✓

---

## Composite Ranking

| Rank | Variation | C-20 | C-21 | C-22 | C-23 | C-24 | Composite | Golden? |
|------|-----------|------|------|------|------|------|-----------|---------|
| 1 | **V-05** | PASS | PASS | PASS | PASS | PASS | **170/170** | ✓ |
| 2 | **V-04** | PASS | PASS | PASS | PASS | FAIL | **165/170** | ✓ |
| 3 | **V-03** | FAIL | PASS | PASS | FAIL | PASS | **160/170** | ✓ |
| 4 | **V-01** | PASS | FAIL | FAIL | PASS | FAIL | **155/170** | ✓ |
| 4 | **V-02** | FAIL | FAIL | PASS | FAIL | PASS | **155/170** | ✓ |

**V-03 vs V-04 symmetry confirmed:** Both paths (table-structure: C-21+C-22+C-24 vs format-discipline: C-20+C-21+C-22+C-23) reach 160/165 respectively, with V-04 showing 5pt advantage from combining prose discipline with structural integrity. Neither path dominates without the gate.

**V-01 vs V-02 structural independence confirmed:** C-23 (inline citations) and C-24 (gate) are independently achievable; neither requires the other's scaffolding to hold.

---

## Excellence Signals from V-05

**Pattern 1 — Structured-output exemption class in prose-restriction declaration**

V-05's C-20 declaration adds an explicit enumeration of non-prose structured output types that are exempt from C-23 inline tagging: "Gate decision lines (PROCEED / BLOCKED) and cross-artifact header lines are structured output, not prose, and do not require inline prose citation tags." This is architecturally above C-20. C-20 declares where prose is *permitted*; this new element declares what *isn't prose at all*, resolving the category boundary. Without it, an executor applying C-23 to a prompt combining C-20/C-23/C-24 might tag gate verdicts with `[prose: ...]` tags (false compliance) or omit them and produce an ambiguous violation. The explicit exemption makes gate output and header lines self-classifying: a reader can determine by inspection whether an output element requires a C-23 tag without interpreting content.

**Pattern 2 — Gate inertia annotation (gate-level C-18 equivalent)**

V-05's TYPE SCAN GATE carries a "Purpose" statement that names the specific failure mode the gate prevents and explains the precise gap above C-22: "C-22 ensures the Type column is present and all categories appear in the finished output. This gate ensures type completeness is an explicit named structural check, not an implicit property verifiable only by reading TABLE E in full. A missing category is a structural block here, not a detectable gap in hindsight." This is the C-18 inertia-framing pattern applied to a gate step rather than a prohibition or enumeration anchor. C-24 requires the gate to exist with PROCEED/BLOCK; this pattern makes the gate self-explaining — an auditor reading only the gate section can reconstruct why it exists and what output would look like if it were absent. V-04 has the gate absent entirely; V-02/V-03 have the gate but without the Purpose annotation. Only V-05 combines all four: gate present, gate labels failure mode, gate is exempt from prose tagging, gate references C-22 as the criterion it operationalizes.

---

```json
{"top_score": 170, "all_essential_pass": true, "new_patterns": ["Structured-output exemption class in prose-restriction declaration — C-20 enumerates not only prose-permitted contexts but also names non-prose structured output types (gate verdicts, artifact headers) that are exempt from C-23 inline tagging, making the prose/structured-output boundary self-classifying without content inspection", "Gate inertia annotation — TYPE SCAN GATE carries a Purpose statement naming the specific failure mode it prevents and explaining the precise structural gap above C-22, making the gate self-explaining and auditable without cross-referencing the rubric"]}
```
