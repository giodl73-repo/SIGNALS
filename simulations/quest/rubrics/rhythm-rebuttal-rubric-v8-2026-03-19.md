Looking at the scorecard, I can extract three beyond-rubric signals:

1. **Check 2c** (Axis G — V-01/V-04/V-05): extends C-25 — evidence form label named → evidence actually instantiated in exchange body
2. **Check 4 Part C** (Axis H — V-02/V-04/V-05): extends C-27 — SHIFTED classified → REINSTATE / CONFIRM CHANGE binding decision
3. **Check 6b** (Axis I — V-03/V-05): extends C-26 — R-ID referenced in cover letter → R-ID resolves to a CHANGE outcome (not P1 no-change)

Here is the complete updated rubric:

---

# Rubric: rhythm-rebuttal (v8)

## Change Log

### v8 (2026-03-19) — R7 excellence patterns

**Formula update**: aspirational denominator changes from `/19` to `/22` (19 criteria → 22 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-28 | Axis G `evidence instantiation gate` | Phase 7 Check 2c follows Check 2b: after Check 2b verifies a valid evidence form category label is present, Check 2c verifies the label is instantiated — "prior literature" resolves to a specific cited paper or author, "statistical result" to a specific statistic or test, "methodological argument" to a specific methodological principle; naming the category without a concrete referent fails Check 2c even when Check 2b passes |
| C-29 | Axis H `SHIFTED decision gate — REINSTATE / CONFIRM CHANGE` | Phase 7 Check 4 Part C follows Check 4 Part B: after Part B verifies classification, Part C requires a binding manuscript decision per SHIFTED entry — PRESSURE-DRIVEN entries must state REINSTATE or NO REINSTATE with a one-sentence rationale; EVIDENCE-DRIVEN entries must state CONFIRM CHANGE; the decision is recorded before write and cannot be deferred to the cover letter |
| C-30 | Axis I `cover letter claim–outcome consistency gate` | Phase 7 Check 6b follows Check 6: after Check 6 verifies each Paragraph 1 change claim has at least one R-ID reference, Check 6b verifies each referenced R-ID resolves to a CHANGE MANUSCRIPT OUTCOME (not P1 no-change); a cover letter claim asserting "we changed X in response to R-N" while R-N's MANUSCRIPT OUTCOME is P1 is a structural contradiction detectable only at this gate |

The three additions are structurally distinct from everything preceding them:

- **C-28** closes the gap between C-25's label-naming gate and actual evidence presence — C-25 detects missing category names; C-28 detects category names with no substance behind them. The same exchange can pass C-25 and fail C-28.
- **C-29** closes the gap between C-27's classification and the manuscript consequence of that classification — C-27 requires the PRESSURE-DRIVEN / EVIDENCE-DRIVEN determination; C-29 requires the author to commit to what happens to the manuscript as a result. Classification without decision is observation; C-29 converts it into a committed outcome.
- **C-30** closes the gap between C-26's traceability gate and cover-letter/manuscript consistency — C-26 detects claims with no R-ID; C-30 detects claims whose R-ID traces to a P1 no-change outcome, making the claim a structural lie. No prior criterion can detect this divergence class.

---

### v7 (2026-03-19) — R6 excellence patterns

**Formula update**: aspirational denominator changes from `/16` to `/19` (16 criteria → 19 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-25 | Pattern 1 `evidence form verification gate` | Phase 7 Check 2b converts RULE-1's declarative valid/invalid evidence taxonomy into a mechanical write-time gate: each P1 no-change MANUSCRIPT OUTCOME must name at least one valid evidence form category (prior literature, methodological argument, statistical result) before write; a well-phrased rationale using only restatement or precedent fails Check 2b regardless of phrasing quality or length |
| C-26 | Pattern 2 `cover letter Paragraph 1 R-ID traceability gate` | Phase 6a requires parenthetical R-ID references in each Paragraph 1 change claim; Phase 7 Check 6 lists each claim with its R-ID reference and fails any claim traceable to zero R-IDs, making cover letter vagueness a structural gate failure rather than an editorial observation that survives to submission |
| C-27 | Pattern 3 `SHIFTED pre-commitment classification protocol` | Phase 6a classifies each SHIFTED entry as PRESSURE-DRIVEN or EVIDENCE-DRIVEN; each class triggers a distinct re-examination action; Phase 7 Check 4 Part B verifies all SHIFTED entries are classified and re-examined before write, converting unstructured SHIFTED logging into a binary with defined consequences per type |

---

### v6 (2026-03-19) — R5 excellence patterns

**Formula update**: aspirational denominator changes from `/13` to `/16` (13 criteria → 16 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-23 | Pattern 1 `P1 concern-level pre-commitment block` | Phase 2 requires a HELD/SHIFTED pre-commitment block per P1 concern: each concern names its valid evidence form and commits to a position before any exchange is written; Phase 6a produces a HELD/SHIFTED table classifying each concern's outcome |
| C-24 | Pattern 2 `Phase 7 count-based structural gate` | Phase 7 contains at least five explicit numbered checks (REVIEWER SAID count, outcome resolution, cover letter structure, forecast/SHIFTED coverage, integer frontmatter) that must all pass before the artifact is written; failure of any check blocks write |
| C-22 | (promoted from pending) `forecast flag carry-forward as live exchange annotation` | Phase 4 forecast rows targeting specific R-IDs are carried into Phase 5 exchange headers as FLAGGED annotations; Phase 6b validates FLAGGED exchanges first then checks unflagged exchanges, creating two structurally distinct accuracy checks |

---

### v5 (2026-03-19) — R4 excellence patterns

**Formula update**: aspirational denominator changes from `/11` to `/13` (11 criteria → 13 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-20 | Pattern 1 `rule violation consequences declared per RULE-N` | Each numbered RULE in the constraints block includes an explicit violation consequence structurally distinct from the rule statement itself |
| C-21 | Pattern 2 `Phase 3.5 upstream type audit` | Phase 3.5 requires one explicit distinguishing justification sentence per scope, framing, or methodological assignment before the forecast is written — catches the three most confusion-prone types at the earliest gate before misclassification propagates to the forecast table, exchange, or cover letter |
| C-22 | Pattern 3 `forecast flag carry-forward as live exchange annotation` | Phase 4 forecast rows targeting specific R-IDs are carried into Phase 5 exchange headers as FLAGGED annotations, making the predicted failure visible at the moment of writing; Phase 6b validates FLAGGED exchanges first then checks unflagged exchanges |

---

### v4 (2026-03-19) — R3 excellence patterns

**Formula update**: aspirational denominator changes from `/8` to `/11` (8 criteria → 11 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-17 | Pattern 1 `format-as-rule architectural convergence` | Exchange template declared as a numbered RULE in the pre-workflow constraints block — one surface satisfies both C-14 (rules front-loaded) and C-16 (format enforced) rather than requiring two separate declarations |
| C-18 | Pattern 2 `forecast table specificity as falsifiability` | Forecast step uses a structured table (R-ID / predicted failure mode / trigger sentence) that enables row-by-row ACCURATE / MISSED / OVERSTATED validation in the amendment pass, turning C-15 from retrospective observation into a calibration loop |
| C-19 | Pattern 3 `type-response coupling by construction` | Per-type AUTHOR RESPONDS starter templates mean a wrong type assignment at Phase 3 produces a visibly wrong response at Phase 5, moving C-06 enforcement from the decomposition table to the exchange output itself |

---

### v3 (2026-03-19) — R2 excellence patterns

**Formula update**: aspirational denominator changes from `/5` to `/8` (5 criteria → 8 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-14 | Pattern 1 `rules-first architecture` | All binding constraints front-loaded into a named RULE-N block before workflow phases begin; no binding constraint embedded only inside a phase description |
| C-15 | Pattern 2 `weakness forecast as pre-commitment` | A forecast step predicts which concerns are likely hardest before any exchange is written; forecast completed before Phase 5 begins |
| C-16 | Pattern 3 `dialogue exchange format enforcement` | Three-part labeled format (REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME) enforced for every exchange, not just recommended |

---

## Scoring Formula

| Tier | Points | Formula |
|------|--------|---------|
| Essential (C-01–C-05) | 60 | 12 pts each |
| Recommended (C-06–C-08) | 30 | 10 pts each; PARTIAL = 5 |
| Aspirational (C-09–C-30) | 10 | (passed / **22**) × 10 |

Golden threshold: >= 90 AND all essential pass.

---

## Essential Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Concerns decomposed individually | structure | Each reviewer concern decomposed into its own numbered entry before any response is written. No two concerns merged into a single entry. |
| C-02 | Every concern receives a full response | completeness | Each decomposed concern entry has a complete REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME exchange. No concern left with a placeholder or empty response. |
| C-03 | P1 no-change requires overcoming inertia | depth | RULE-1 (or equivalent) is present in the pre-workflow constraints block and names "no change to manuscript" as the inertia default requiring author work to overcome. The rule uses explicit inertia framing, not just a requirement to justify. |
| C-04 | Professional register maintained | format | RULE-4 (or equivalent) constrains all responses to professional non-defensive register. Per-type AUTHOR RESPONDS openers acknowledge before responding. No combative or dismissive language in any exchange. |
| C-05 | Correct output path; integer frontmatter | format | Artifact written to `signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md` with integer-only frontmatter values. RULE-6 (or equivalent) states both constraints explicitly. |

---

## Recommended Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Concern types correctly classified | depth | Six-type taxonomy (factual / methodological / scope / framing / statistical / presentation) with explicit misclassification warnings. Each concern assigned a type before responses are written. PARTIAL if taxonomy present but warnings absent. |
| C-07 | Cover letter present and structurally correct | format | Cover letter has Paragraph 1 (3–4 specific changes with parenthetical R-ID references) and Paragraph 2 (disagreement framing or explicit statement of none). Both paragraphs updated in Phase 6a reconciliation. PARTIAL if one paragraph missing or reconciliation step absent. |
| C-08 | Amendment pass identifies real weaknesses | depth | Phase 6c (or equivalent) names exactly three exchanges to strengthen using the three diagnostic labels (too defensive / concedes too much / too brief). FLAGGED exchanges prioritized. PARTIAL if fewer than three labeled or labels absent. |

---

## Aspirational Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | No-change responses brief and non-defensive | format | RULE-2 (or equivalent) limits P1 no-change responses to 1 paragraph maximum with an explicit violation clause. The rule is named and binding, not advisory. |
| C-10 | Scope concerns handled distinctively | depth | Scope type has a distinct handling instruction that differs from factual and methodological handling. At minimum, scope concerns acknowledge the boundary question before responding. |
| C-11 | P1 no-change framed as inertia to overcome | depth | RULE-1 uses the phrases "the path requiring no additional author work" and "OVERCOMES that inertia" (or functionally equivalent burden language) in the rule text itself, not only in commentary. |
| C-12 | Cover letter drafted before individual responses | structure | Phase ordering requires the cover letter draft to appear before the individual exchange drafting phase. A cover-first commitment is structurally enforced by phase numbering, not just recommended. |
| C-13 | Severity tier headers in response section | format | The response section organizes concerns under severity tier headers (e.g., Major / Minor or equivalent) rather than a flat list. Tier assignment precedes response drafting. |
| C-14 | Critical constraints in pre-workflow RULE-N block | structure | All binding constraints (format, register, length, output path) appear in a named RULE-1, RULE-2, … block before the workflow phases begin. No binding constraint is embedded only inside a phase description. |
| C-15 | Weakness forecast precedes response drafting | depth | A forecast step predicts which concerns are likely hardest to address before any exchange is written. The forecast must be completed before Phase 5 (exchange drafting) begins. |
| C-16 | Dialogue exchange format (REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME) | format | Every exchange uses the three-part labeled format exactly. All three labels must appear in every exchange. |
| C-17 | Exchange format declared as numbered RULE in constraints block | structure | The three-part exchange format is declared as a numbered RULE-N in the pre-workflow constraints block. This single declaration satisfies both C-14 (rules front-loaded) and C-16 (format enforced as binding rule). |
| C-18 | Weakness forecast uses structured table with trigger column | depth | The forecast step uses a structured table with columns for R-ID, predicted failure mode, and trigger sentence (the specific reviewer sentence most likely to provoke the failure). The table enables row-by-row ACCURATE / MISSED / OVERSTATED validation in the amendment pass. |
| C-19 | Per-type AUTHOR RESPONDS templates | depth | Each of the six concern types has a distinct AUTHOR RESPONDS opener template beginning with the correct acknowledgment-before-response stance. Templates listed before the workflow phases or in Phase 3 alongside the type taxonomy. |
| C-20 | Rule violation consequences declared per RULE-N | structure | Each numbered RULE in the constraints block includes an explicit violation consequence (e.g., "editorial office will return it," "counts as a concession," "fails the gate"). The consequence is structurally distinct from the rule statement itself. |
| C-21 | Phase 3.5 upstream type audit | depth | A Phase 3.5 (or equivalent intermediary gate) requires one explicit distinguishing justification sentence per scope, framing, or methodological assignment before the forecast is written. Catches the three most confusion-prone types at the earliest gate before misclassification propagates. |
| C-22 | Forecast flags carried forward as live Phase 5 exchange annotations | depth | Phase 4 forecast rows targeting specific R-IDs are carried into Phase 5 exchange headers as FLAGGED annotations. Phase 6b validates FLAGGED exchanges first then checks unflagged exchanges, creating two structurally distinct accuracy checks. |
| C-23 | P1 concern-level pre-commitment block with HELD/SHIFTED audit | depth | Phase 2 (or equivalent pre-response phase) requires a HELD/SHIFTED pre-commitment block per P1 concern: each concern names its valid evidence form and commits to a position before any exchange is written. Phase 6a produces a HELD/SHIFTED table classifying each concern's outcome. |
| C-24 | Phase 7 count-based structural gate before artifact write | structure | Phase 7 contains at least five explicit numbered checks (REVIEWER SAID count, outcome resolution, cover letter structure, forecast/SHIFTED coverage, integer frontmatter) that must all pass before the artifact is written. Failure of any check blocks write. |
| C-25 | P1 no-change evidence form verification gate (Phase 7 Check 2b) | depth | Check 2b appears as an explicit numbered step in Phase 7 and requires each P1 no-change MANUSCRIPT OUTCOME to name at least one valid evidence form category by label (prior literature, methodological argument, statistical result). A rationale using only restatement or precedent fails regardless of phrasing quality. Distinct from C-03 (declares inertia rule) and C-23 (pre-commits positions) — C-25 is the only criterion that enforces RULE-1's taxonomy reaches the artifact surface. |
| C-26 | Cover letter Paragraph 1 R-ID traceability gate (Phase 7 Check 6) | format | Check 6 appears as an explicit numbered step in Phase 7, lists each Paragraph 1 change claim individually with its R-ID reference(s), and blocks any claim traceable to zero R-IDs. Distinct from C-07 (cover letter structure) and C-12 (cover-first commitment) — C-26 is the only criterion that converts cover letter vagueness from an editorial observation into a named, blocking failure category. |
| C-27 | SHIFTED classification protocol with type-specific re-examination (Phase 7 Check 4 Part B) | depth | PRESSURE-DRIVEN / EVIDENCE-DRIVEN binary with type-specific re-examination actions appears in Phase 6a. Check 4 Part B in Phase 7 verifies all SHIFTED entries are classified and re-examined before write. Distinct from C-23 (HELD/SHIFTED logging) — C-27 converts the SHIFTED event from a logged observation into an examined outcome with defined consequences per type. |
| C-28 | P1 no-change evidence instantiation gate (Phase 7 Check 2c) | depth | Check 2c appears as an explicit numbered step in Phase 7, following Check 2b. After Check 2b verifies a valid evidence form category label is present, Check 2c verifies the label is instantiated in the exchange body: "prior literature" resolves to a specific cited paper or author; "statistical result" resolves to a specific statistic or test; "methodological argument" resolves to a specific methodological principle. Naming the category label without a concrete referent fails Check 2c even when Check 2b passes. Distinct from C-25 (which tests label presence only) — C-28 is the only criterion that can detect evidence-label-without-substance at write time. |
| C-29 | SHIFTED decision gate — REINSTATE / CONFIRM CHANGE commitment (Phase 7 Check 4 Part C) | depth | Check 4 Part C appears as an explicit numbered step in Phase 7, following Check 4 Part B. After Part B verifies PRESSURE-DRIVEN / EVIDENCE-DRIVEN classification, Part C requires a binding manuscript decision per SHIFTED entry: PRESSURE-DRIVEN entries must state REINSTATE or NO REINSTATE with a one-sentence rationale; EVIDENCE-DRIVEN entries must state CONFIRM CHANGE. The decision is recorded before write and cannot be deferred to the cover letter. Distinct from C-27 (which tests classification only) — C-29 converts the classification from an observation about why the author shifted into a committed manuscript outcome. |
| C-30 | Cover letter claim–outcome consistency gate (Phase 7 Check 6b) | format | Check 6b appears as an explicit numbered step in Phase 7, following Check 6. After Check 6 verifies each Paragraph 1 change claim has at least one R-ID reference, Check 6b verifies each referenced R-ID resolves to a CHANGE MANUSCRIPT OUTCOME (not P1 no-change): a cover letter claim asserting "we changed X in response to R-N" while R-N's MANUSCRIPT OUTCOME is P1 is a structural contradiction. Distinct from C-26 (which tests R-ID presence only) — C-30 is the only criterion that can detect cover-letter/manuscript-outcome divergence before write. |
