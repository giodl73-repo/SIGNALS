## Quest Score — scout-inertia Round 13 (Rubric v13)

**Formula**: `aspirational_pass / 36 * 10`
**Variations**: V-01 through V-05
**New criteria under test**: C-41, C-42, C-43, C-44

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (all must pass — gating)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Workaround mapped | PASS — Section 2 `[C-01 COMMAND]` requires exact tool/role/number+unit | PASS — Section 2 same structure | PASS — Section 2 same structure | PASS — Stage 3 same structure | PASS — Stage 3 same structure |
| **C-02** Switching costs quantified | PASS — Section 3 requires >=2 categories, number+unit, role named | PASS | PASS | PASS — Stage 4 adds "revisit Stage 0 and revise PROVISIONAL" feedback | PASS — Stage 4 same feedback loop |
| **C-03** Threat score declared | PASS — Section 4, HIGH default, deviation requires evidence | PASS | PASS | PASS — Stage 0 first, PROVISIONAL mechanism for pre-evidence non-HIGH scores | PASS — Stage 0 first, PROVISIONAL mechanism |
| **C-04** Defeat conditions | PASS — Section 5 requires >=2 falsifiable, FM-[N] citation, threshold | PASS | PASS | PASS | PASS |
| **C-05** Failure modes inventoried | PASS — Section 1 requires mechanism-level, not category, >=2 rows | PASS | PASS | PASS | PASS |

**All essential: PASS (5/5) across all variations.**

---

### Aspirational Criteria — Bracket Structure (C-34 through C-40)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-34** Primary key bracket label at Stage 1 | PASS — `[STATUS QUO PRIMARY KEY RULE]` in Section 1 | PASS — `[INERTIA THREAT PRIMARY KEY RULE]` | PASS — `[DEFAULT OPTION PRIMARY KEY RULE]` | PASS — `[INCUMBENT PRIMARY KEY RULE]` in Stage 1 | PASS — `[STATUS QUO COMPETITOR PRIMARY KEY RULE]` |
| **C-35** Citation integrity bracket label at defeat conditions | PASS — `[STATUS QUO CITATION INTEGRITY RULE]` in Section 5 | PASS — `[INERTIA THREAT CITATION INTEGRITY RULE]` | PASS — `[DEFAULT OPTION CITATION INTEGRITY RULE]` | PASS — `[INCUMBENT CITATION INTEGRITY RULE]` in Stage 5 | PASS — `[STATUS QUO COMPETITOR CITATION INTEGRITY RULE]` |
| **C-36** Three+ distinct bracket obligations | PASS — PRIMARY KEY RULE + CITATION INTEGRITY RULE + BRIDGE COMPLETION COMMAND + C-0N commands | PASS | PASS | PASS | PASS |
| **C-37** Bracket command in gate block body | PASS — `[STATUS QUO BRIDGE COMPLETION COMMAND]` inside gate block | PASS — `[INERTIA THREAT BRIDGE COMPLETION COMMAND]` | PASS — `[DEFAULT OPTION BRIDGE COMPLETION COMMAND]` | PASS — `[INCUMBENT BRIDGE COMPLETION COMMAND]` in Stage 2 gate block | PASS — `[STATUS QUO COMPETITOR BRIDGE COMPLETION COMMAND]` |
| **C-38** FAIL-FIRST heading has domain subtitle | PASS — `THE STATUS QUO` is domain-axis vocabulary | PASS — `THE INERTIA THREAT` | PASS — `THE DEFAULT OPTION` | PASS — `THE INCUMBENT WORKAROUND` (domain term) | PASS — `THE STATUS QUO COMPETITOR` |
| **C-39** Gate heading binary question form | PASS — `HAVE BOTH STATUS QUO BRIDGES BEEN POPULATED?` answerable Y/N | PASS | PASS | PASS | PASS |
| **C-40** Systematic C-NN: prefix coverage on checklist | PASS — all 5 checklist rows carry `C-NN:` prefix | PASS | PASS | PASS | PASS |

---

### Aspirational Criteria — R13 New (C-41 through C-44)

#### C-41 — Per-Artifact Bracket Commands at Bridge Sections

| Variation | Q3 command | Q4 command | Placement | Verdict |
|-----------|-----------|-----------|-----------|---------|
| V-01 | `[STATUS QUO Q3 COMMAND]` at `## Q3 -- FM->ACTOR BRIDGE` | `[STATUS QUO Q4 COMMAND]` at `## Q4 -- FM->TRIGGER BRIDGE` | Co-located with bridge table; independent of gate block | **PASS** |
| V-02 | `[INERTIA THREAT Q3 COMMAND]` at Q3 section | `[INERTIA THREAT Q4 COMMAND]` at Q4 section | Same | **PASS** |
| V-03 | `[DEFAULT OPTION Q3 COMMAND]` at Q3 section | `[DEFAULT OPTION Q4 COMMAND]` at Q4 section | Same | **PASS** |
| V-04 | `[INCUMBENT Q3 COMMAND]` at `### Q3 -- FM->ACTOR BRIDGE` within Stage 2 | `[INCUMBENT Q4 COMMAND]` at `### Q4 -- FM->TRIGGER BRIDGE` within Stage 2 | Co-located within bridge stage subsections | **PASS** |
| V-05 | `[STATUS QUO COMPETITOR Q3 COMMAND]` at Q3 subsection | `[STATUS QUO COMPETITOR Q4 COMMAND]` at Q4 subsection | Co-located within Stage 2 | **PASS** |

All variations place both per-artifact commands at the correct authoring point, distinct from the gate-level command. All PASS.

---

#### C-42 — Vocabulary Threading (Domain-Axis Word Shared Across Three C-36 Elements)

Test: *Given only the shared vocabulary element across the three bracket labels, can a reader identify this scaffold as a scout-inertia analysis?*

| Variation | Threading term | Domain-axis identification test | Three elements sharing the term | Verdict |
|-----------|---------------|--------------------------------|--------------------------------|---------|
| V-01 | `STATUS QUO` | PASS — "STATUS QUO" names the competitor axis in the inertia domain; distinct from scaffold vocabulary | PRIMARY KEY RULE + CITATION INTEGRITY RULE + BRIDGE COMPLETION COMMAND | **PASS** |
| V-02 | `INERTIA THREAT` | PASS — "INERTIA THREAT" is the skill's canonical term; drawn from skill description, not scaffold management vocabulary | Same three | **PASS** |
| V-03 | `DEFAULT OPTION` | PASS — "DEFAULT OPTION" names the structural role of the workaround (path of least resistance); domain-derivable | Same three | **PASS** |
| V-04 | `INCUMBENT` | PASS — "INCUMBENT" connotes tenure, organizational lock-in; inertia domain term | Same three | **PASS** |
| V-05 | `STATUS QUO COMPETITOR` | PASS (strongest) — compound term explicitly names both the axis (STATUS QUO) and structural role (COMPETITOR); most unambiguous domain identification | Same three | **PASS** |

Assessment: All five pass C-42. Strength ranking: V-05 (compound, dual-axis) > V-02 (canonical skill term) > V-01 (precision) > V-03 (structural role) > V-04 (single anthropomorphic word).

---

#### C-43 — Explicit Count Quantifier in Gate Heading Interrogative

Test: *Given the heading interrogative alone, can an author state the expected artifact count as a number?*

| Variation | Interrogative component | Count determinable from heading? | Form | Verdict |
|-----------|------------------------|----------------------------------|------|---------|
| V-01 | `HAVE BOTH STATUS QUO BRIDGES BEEN POPULATED?` | Yes — "BOTH" = exactly 2 | Bare "BOTH" | **PASS** |
| V-02 | `HAVE BOTH INERTIA THREAT BRIDGES BEEN POPULATED?` | Yes — "BOTH" = exactly 2 | Bare "BOTH" | **PASS** |
| V-03 | `HAVE BOTH Q3 AND Q4 DEFAULT OPTION BRIDGES BEEN POPULATED?` | Yes — "BOTH Q3 AND Q4" = exactly 2, artifact IDs named | Explicit enumeration (strongest per rubric note) | **PASS** |
| V-04 | `HAVE BOTH INCUMBENT BRIDGES BEEN POPULATED?` | Yes — "BOTH" = exactly 2 | Bare "BOTH" | **PASS** |
| V-05 | `HAVE BOTH STATUS QUO COMPETITOR BRIDGES BEEN POPULATED?` | Yes — "BOTH" = exactly 2 | Bare "BOTH" | **PASS** |

V-03 is the strongest C-43 implementation: "BOTH Q3 AND Q4" names exact count AND artifact identities; both determinable from heading alone without reading gate body. V-01/V-02/V-04/V-05 pass at the count level but require reading artifact list to confirm identities.

---

#### C-44 — Action-Imperative Gate Structural Marker

Test: *Does the marker before `--` tell the author what to DO rather than what the gate IS?*

| Variation | Marker component | Commands behavior? | Fails if it only names type? | Verdict |
|-----------|-----------------|-------------------|------------------------------|---------|
| V-01 | `PASS BEFORE ADVANCING` | Yes — enforcement directive | Distinct from "BRIDGE COMPLETION GATE" | **PASS** |
| V-02 | `STOP BEFORE PROCEEDING` | Yes — alternative enforcement; commands stop | Distinct from "COMPLETION CHECK" | **PASS** |
| V-03 | `DO NOT ADVANCE UNTIL` | Yes — conditional prohibition; rubric explicitly lists this form as passing | Distinct from "ARTIFACT REVIEW STEP" | **PASS** |
| V-04 | `PASS BEFORE ADVANCING` | Yes — same enforcement directive as V-01 | Structurally identical to V-01 for C-44 | **PASS** |
| V-05 | `PASS BEFORE ADVANCING` | Yes — same enforcement directive | Structurally identical to V-01 for C-44 | **PASS** |

Assessment: All pass. Three distinct imperative forms tested: enforcement directive (V-01/V-04/V-05), alternative enforcement (V-02), conditional prohibition (V-03). All three command the author's behavior rather than labeling the gate's structural type.

---

## Composite Scores

All 36 aspirational criteria pass for all 5 variations (criteria C-34 through C-44 verified above; prior criteria C-06 through C-33 carry forward from golden scaffold design across prior rounds).

| Variation | Aspirational Pass | Score | Essential Pass |
|-----------|-----------------|-------|----------------|
| V-01 | 36/36 | **10.0** | All 5 |
| V-02 | 36/36 | **10.0** | All 5 |
| V-03 | 36/36 | **10.0** | All 5 |
| V-04 | 36/36 | **10.0** | All 5 |
| V-05 | 36/36 | **10.0** | All 5 |

---

## Ranking (Qualitative Strength at Tied Scores)

All five variations score 10.0. Tie-breaking by implementation strength of the new R13 criteria:

**1. V-03** — C-43 strongest form ("BOTH Q3 AND Q4" names artifact IDs, not just count). C-44 conditional prohibition form is distinctive. Rubric explicitly endorses V-03's C-43 as the ceiling example.

**2. V-05** — C-42 strongest threading term (compound "STATUS QUO COMPETITOR" is dual-axis, most unambiguous identification). Numbered stage lifecycle. C-04 checklist specifies "measurable threshold from Q4" (traceability explicit). Extra `Evidence type` column in defeat condition table.

**3. V-04** — Unique provisional threat score mechanism (Stage 0 declares verdict before evidence; PROVISIONAL marker for non-HIGH; Stage 4 verification loop). C-04 checklist specifies "from Q4". Numbered stage lifecycle.

**4. V-01** — STATUS QUO threading: semantically precise, visually distinct from scaffold vocabulary. Clean baseline for C-41 through C-44 implementation.

**5. V-02** — INERTIA THREAT threading draws from skill's own canonical term. STOP BEFORE PROCEEDING tests C-44 vocabulary range. No structural innovations beyond new criteria.

---

## Excellence Signals (R13 Patterns)

**Signal 1 — Explicit artifact enumeration in gate heading (V-03)**
"BOTH Q3 AND Q4" names specific artifact IDs in the interrogative. Authors reading the gate heading know both the count (2) and the identity of what they're confirming. Eliminates the need to cross-reference the gate body to determine which artifacts are expected. The rubric endorses this as the strongest C-43 form; it's also the most author-friendly form at the point of decision.

**Signal 2 — "from Q4" traceability in C-04 checklist criterion (V-04, V-05)**
Both V-04 and V-05 write the C-04 checklist row as "each has measurable threshold **from Q4**" rather than "each has a measurable threshold." The difference closes a structural gap: defeat condition thresholds should not be invented independently in Section 5 — they must be re-used from Q4's FM->TRIGGER BRIDGE. The checklist layer enforces the chain FM-[N] → Q4 threshold → DC threshold. V-01/V-02/V-03 leave this traceable only at the bracket command level, not at the checklist layer.

**Signal 3 — Stage 0 provisional threat posture with feedback loop (V-04, V-05)**
Declaring C-03 (threat score) in Stage 0 before failure modes (Stage 1) creates an evidence-to-verdict feedback loop: author states verdict first, then collects evidence that confirms or challenges it. The PROVISIONAL marker for non-HIGH scores enforces that deviations cannot be finalized until Stage 4 quantified evidence exists. This is a different cognitive model than declaring threat score after evidence: verdict-first makes the author's assumptions explicit from the start.

**Signal 4 — Compound domain term for C-42 threading (V-05)**
"STATUS QUO COMPETITOR" combines two dimensions of domain identification: axis (STATUS QUO = the option to do nothing) and structural role (COMPETITOR = it is competing against the feature). The compound passes C-42's identification test with maximum redundancy — removing either word still leaves a domain-axis term. This is more robust than single-word or single-dimension threading terms.

---

## New Patterns (Candidates for C-45+)

**Candidate C-45 — C-04 checklist threshold sourcing**
The C-04 checklist criterion should explicitly name Q4 as the required threshold source: "each has measurable threshold from Q4" not merely "each has measurable threshold." This closes the traceability chain at the checklist enforcement layer, preventing independently-authored thresholds in defeat conditions.

**Candidate C-46 — Artifact-ID enumeration in gate heading**
When bridge artifacts carry distinct identifiers (Q3, Q4), the gate heading interrogative should enumerate them explicitly ("BOTH Q3 AND Q4") rather than using type-only reference ("BOTH ... BRIDGES"). Count AND identity in heading = no ambiguity at the point of decision, no body cross-reference required.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["C-04 checklist criterion specifies 'from Q4' as threshold source, closing FM→Q4→DC traceability at the checklist layer — V-04 and V-05 write 'each has measurable threshold from Q4' vs V-01/V-02/V-03 write 'each has a measurable threshold'", "Stage 0 provisional threat posture mechanism: non-HIGH scores declared before evidence with PROVISIONAL marker, feedback loop requires Stage 4 quantified evidence to finalize — separates declaration from evidence and makes assumptions explicit", "Artifact-ID enumeration in gate heading interrogative: 'BOTH Q3 AND Q4' names count and identities, eliminating gate body cross-reference at the point of decision — generalizable to any bridge scaffold where artifacts carry distinct IDs"]}
```
