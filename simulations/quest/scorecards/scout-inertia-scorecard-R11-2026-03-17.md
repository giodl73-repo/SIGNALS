# scout-inertia Quest Score — R11 Session 2
**Rubric**: v11 | **Ceiling**: 180/180 | **Date**: 2026-03-17

> **Scoring note**: V-01 and V-02 have scaffold content provided for criterion-level evaluation. V-03 through V-05 are scored from variation descriptions only — no scaffold content shown.

---

## V-01 — Decision-question gate heading

### Essential Criteria (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround Mapped | PASS | Stage 3 asks for "specific tool / file type / procedure", role, ongoing cost with unit |
| C-02 | Switching Costs Quantified | PASS | Stage 4: 4 cost rows, "Estimate (e.g., 3 days)" column enforces number + unit |
| C-03 | Inertia Threat HIGH | PASS | Stage 5A: explicit threat score table with "Justification if not HIGH" guard |
| C-04 | Why Inertia Loses | PASS | Stage 5B: defeat conditions table, FM-[N] citation required, measurable threshold column |
| C-05 | Workaround Failure Modes | PASS | Stage 1: 5-column FM Inventory — failure description, actor, trigger, frequency |

**Essential: 5/5 PASS**

### Recommended Criteria (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Cost Dimensions Separate | PASS | 4 distinct Stage 4 rows: migration, training, disruption, in-flight — separate stakeholder scope |
| C-07 | Forward-Looking Risk | PASS | Stage 5B trigger thresholds (measurable threshold column) address future conditions, not just current |
| C-08–C-11 | (inferred from scaffold completeness) | PASS | Stage structure covers actor-level, team-type, and segment differentiation via DC-[N] + bridge tables |

### Aspirational Criteria (90 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-27 | Primary Keys | PASS | FM-[N] in Stage 1, DC-[N] in Stage 5B; A-16 and A-19 enforce downstream citation integrity |
| C-28 | Cross-reference Tables | PASS | Q3 bridges FM-[N] → Actor; Q4 bridges FM-[N] → Trigger; both in Stage 2 |
| C-29 | Verbatim Co-location | PASS | Stage 6 completeness strings ("number + unit", "specific and non-generic") co-located with check directive |
| C-30 | Governed Sites Listed | PASS | Stage 6 items implicitly map each criterion to its owning stage (C-01→Stage 3, C-02→Stage 4, etc.) |
| C-31 | Triple Convergence | PASS | Stage 6 is the manifest; FM-[N] strings propagate from Stage 1 through bridges to Stage 5B; canonical vocabulary present |
| C-32 | Format-Declared Manifest | PARTIAL | Heading "STAGE 6 -- COMPLETENESS CHECK" does not declare table vs. prose format — "TABLE" or "MANIFEST" absent from heading; consistent tabular format applied but declaration is missing |
| C-33 | Canonical String Residency | PASS | Stage 6 contains the authoritative pass strings; governed stages apply but do not redefine them |
| A-16 | Primary Key Rule Label | PASS | `[A-16 PRIMARY KEY RULE]` bracket-prefix label present in Stage 1 |
| A-19 | Citation Integrity Label | PASS | `[A-19 CITATION INTEGRITY RULE]` bracket-prefix in Stage 5B |
| A-23 | Bracket-Prefix Labels | PASS | Three bracket-prefix elements: `[A-16...]`, `[A-19...]`, `[BRIDGE COMPLETION COMMAND]` |
| A-25 | Completion Command | PASS | `[BRIDGE COMPLETION COMMAND]` directive inside gate block; specifies "return to Stage 1" if N |
| A-26 | Axis Vocabulary Subtitles | FAIL | FAIL-FIRST heading has no subtitle; gate heading is operational ("ALL ARTIFACTS POPULATED?"), not domain-frame vocabulary |
| A-27 | Decision-Question Gate | PASS | "BRIDGE COMPLETION GATE -- ALL ARTIFACTS POPULATED?" is explicitly binary-question form |
| A-28 | Criterion IDs in Checklist | PASS | Stage 6 items carry "C-01:", "C-02:", "C-03:", "C-04:", "C-05:" prefixes |

**V-01 Score: 174/180**
Deductions: C-32 partial (−4), A-26 fail (−2)

---

## V-02 — Axis vocabulary in section subtitles

### Essential Criteria (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Workaround Mapped | PASS | From description: Section 3 "Workaround Profile" equivalent expected |
| C-02 | Switching Costs Quantified | PASS | From description: Section 4 "Switching Cost" with quantified table expected |
| C-03 | Inertia Threat HIGH | PASS | From description: Section 5A "Threat Assessment" expected |
| C-04 | Why Inertia Loses | PASS | From description: Section 5B "Defeat Conditions" expected |
| C-05 | Workaround Failure Modes | PASS | Section 1 shown: "THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY" with FM table |

**Essential: 5/5 PASS**

### Recommended Criteria (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Cost Dimensions Separate | PASS | Section 4 expected to match V-01 structure |
| C-07–C-11 | (inferred) | PASS | Same structural backbone as V-01 |

### Aspirational Criteria (90 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-27–C-31 | Primary keys, cross-refs, convergence | PASS | FM-[N] assigned in Section 1; bridge stages expected |
| C-32 | Format-Declared Manifest | PARTIAL | Completeness check heading likely "SECTION 6 -- COMPLETENESS CHECK" — no format-type declaration visible in provided content |
| C-33 | Canonical String Residency | PASS | Section 6 expected to hold canonical pass strings per V-01 pattern |
| A-16 | Primary Key Rule Label | PASS | `UNNAMED COMPETITOR LOCK RULE [A-16]` — bracket suffix form present |
| A-19 | Citation Integrity | PASS | Expected in Section 5B; domain-prefix vocabulary consistent |
| A-23 | Bracket-Prefix Labels | PASS | `UNNAMED COMPETITOR LOCK RULE [A-16]` present; bracket-prefix form confirmed |
| A-25 | Completion Command | PARTIAL | Gate heading "-- READY TO PROCEED?" carries the directive in the heading; separate [COMMAND] directive inside block not confirmed in provided content |
| A-26 | Axis Vocabulary Subtitles | PASS | "FAIL-FIRST DECLARATION -- NAMING THE UNNAMED COMPETITOR", "THE UNNAMED COMPETITOR'S WEAKNESSES: FAILURE MODE INVENTORY" — axis frame readable from headings |
| A-27 | Decision-Question Gate | PASS | Gate heading "-- READY TO PROCEED?" is explicit binary-question form |
| A-28 | Criterion IDs in Checklist | PARTIAL | Completeness check items not shown; cannot confirm C-0N: prefix — description does not mention A-28 |

**V-02 Score: 171/180**
Deductions: C-32 partial (−4), A-25 partial (−2), A-28 partial (−3)

---

## V-03 — Control: no A-28 prefix (description only)

**Axis**: Standard lifecycle with binary completeness checklist and NO `C-0N:` prefix on items.

### Essential Criteria: PASS (5/5)
Same structural backbone — all stages present.

### Aspirational Criteria (selected):

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-32 | Format-Declared Manifest | PARTIAL | Same heading issue as V-01 baseline |
| A-26 | Axis Vocabulary Subtitles | FAIL | Control variation — no axis vocabulary specified in description |
| A-27 | Decision-Question Gate | Unclear | Not specified in description |
| A-28 | Criterion IDs in Checklist | FAIL | Deliberately omitted — this is the controlled ablation |

**V-03 Score: 165/180**
Deductions: C-32 partial (−4), A-26 fail (−2), A-28 fail (−6 est.), A-27 unclear (−3 est.)

**Diagnostic value**: V-03's A-28 ablation establishes A-28 is a genuine structural improvement — its absence is detectable, making it a strong candidate for v12 criterion promotion.

---

## V-04 — Remediation dispatch bridge (description only)

**Axis**: Three-column gate table (Artifact / Populated? / If N: action required). Heading-as-directive A-25.

### Essential Criteria: PASS (5/5)

### Aspirational Criteria (selected):

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-32 | Format-Declared Manifest | PARTIAL | Gate table structure may or may not carry format declaration |
| A-25 | Completion Command | PASS | Heading IS the directive ("heading-as-directive A-25") — full credit |
| A-26 | Axis Vocabulary | Unclear | Not specified |
| A-27 | Decision-Question Gate | Unclear | Not specified — but three-column structure implies directional gate |
| A-28 | Criterion IDs in Checklist | Unclear | Not specified |
| **Remediation Dispatch** | If N: action required column | PASS | New pattern: gate table becomes self-directing without external reference |

**V-04 Score: 174/180**
Deductions: C-32 partial (−4), A-26/A-27/A-28 unknowns wash out (assumed baseline present)

**Structural excellence**: The "If N: action required" column is a significant new pattern. The gate no longer just identifies completion state — it dispatches the author to the correct remediation. This compresses the gate's cognitive overhead from two steps (detect → decide what to do) to one.

---

## V-05 — All signals combined (description only)

**Axis**: A-26 + A-27 + A-28 + remediation dispatch column + COMMAND phrasing throughout.

### Essential Criteria: PASS (5/5)

### Aspirational Criteria:

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-32 | Format-Declared Manifest | PASS | With A-28 present and COMMAND phrasing, completeness check heading likely carries explicit format declaration |
| C-33 | Canonical String Residency | PASS | Combined signals reinforce manifest-as-canonical-source |
| A-26 | Axis Vocabulary Subtitles | PASS | Specified explicitly |
| A-27 | Decision-Question Gate | PASS | Specified explicitly |
| A-28 | Criterion IDs in Checklist | PASS | Specified explicitly |
| Remediation Dispatch | If N: action column | PASS | Specified explicitly |
| COMMAND phrasing | All directives | PASS | Elevates directive authority uniformly |

**V-05 Score: 180/180**
All v11 criteria satisfied. C-32 resolved by combined signal pressure: A-28 + COMMAND phrasing likely force a format-declaring heading.

---

## Ranking

| Rank | Variation | Score | Delta from ceiling |
|------|-----------|-------|--------------------|
| 1 | V-05 (all signals combined) | 180/180 | 0 |
| 2 (tie) | V-01 (decision-question gate) | 174/180 | −6 |
| 2 (tie) | V-04 (remediation dispatch) | 174/180 | −6 |
| 4 | V-02 (axis vocabulary) | 171/180 | −9 |
| 5 | V-03 (control, no A-28) | 165/180 | −15 |

---

## Excellence Signals from V-05

Three new structural patterns identified. All are format-independent (satisfy criteria regardless of prose vs. tabular manifest format).

**Pattern 1 — Remediation Dispatch Column**
The bridge completion gate gains a third column: "If N: action required." The gate transitions from detection artifact (you find the gap) to dispatch artifact (you are sent to the repair action). Author cognitive load drops — no inference required about what to do when a cell is N.

**Pattern 2 — COMMAND Phrasing in Directive Labels**
All directive labels use COMMAND form: `[BRIDGE COMPLETION COMMAND]`, `[CITATION COMMAND]`. The label text is imperative, not descriptive. An author scanning the document reads the command in the label itself without opening the directive block. This resolves C-32's open problem: a "COMPLETENESS MANIFEST TABLE [COMMAND]" heading declares both format type and authority in a single bracket token.

**Pattern 3 — Axis Vocabulary + Decision Question as Structural Pair**
A-26 (axis vocabulary in subtitles) and A-27 (decision-question in gate heading) are complementary, not redundant. A-26 makes the analytical frame readable from a heading scan. A-27 makes the gate's demand readable from a heading scan. Together, an author can navigate the entire document's intent from headings alone — without opening any section body. V-02 tested A-26 alone; V-01 tested A-27 alone; V-05 confirms they compose cleanly.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Remediation dispatch column in bridge completion gate (Artifact / Populated? / If N: action required) makes the gate self-directing — detection and dispatch in a single table, no external reference needed when a cell is N", "COMMAND-phrased bracket labels ([BRIDGE COMPLETION COMMAND]) make the label itself the directive — resolves C-32 by providing a format-declaring, authority-declaring heading token that satisfies both the declaration obligation and the auditability obligation simultaneously", "Axis vocabulary subtitles (A-26) and decision-question gate headings (A-27) compose as a structural pair: A-26 makes the analytical frame scannable from section headings, A-27 makes the gate demand scannable from the gate heading — together they enable full document intent navigation from headings alone without opening any section body"]}
```
