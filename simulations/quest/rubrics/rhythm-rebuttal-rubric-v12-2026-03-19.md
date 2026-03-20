v12 written to `simulations/quest/rubrics/rhythm-rebuttal-rubric-v12-2026-03-19.md`.

---

**What changed:**

Formula: `/31` → `/34`. Three new aspirational criteria:

| ID | Pattern | Extends | Failure class caught |
|----|---------|---------|---------------------|
| C-40 | Phase 2 annotation coverage extends to Check 2c as well as Check 4 Part C | C-33 (Phase 2 for SHIFTED only) | Phase 2 carries only Check 4 Part C annotation — evidence form commitment made in HELD/SHIFTED block is unconstrained at authoring time |
| C-41 | Phase 7 Check 2c back-reference enumerates Phase 2 as a third upstream source | C-37 (back-ref names all known sources) | Back-reference names Phase 5 and Phase 6a but omits Phase 2 — source set not updated after C-40 promoted Phase 2 to a Check 2c annotation site |
| C-42 | Phase 7 "If FAIL" repair blocks satisfying C-38 contain only the delegation line | C-38 (delegation phrase exists) | Delegation line present but supplementary inline (a)/(b) content follows — two repair surfaces exist and can diverge even though C-38 passes |

**Structural chain**: C-40 extends Phase 2's annotation graph to Check 2c. C-41 extends C-37's source enumeration to reflect the new site (C-40 makes Phase 2 a Check 2c source; C-37 did not require this because Phase 2 wasn't a Check 2c site when C-37 was written). C-42 extends C-38 from "delegation phrase present" to "delegation is the complete repair statement." Each catches a failure class the others cannot.

**Key evidence**: The "(Phase 2 promoted to named source by C-39)" note in V-05's C-37 Check 2c row is the primary signal — V-05 names three sources for Check 2c (Phase 2, Phase 5, Phase 6a) because Phase 2 carries an individually labeled Check 2c forward-annotation. V-04 passes C-37 with two sources and passes C-38 but misses Phase 2 as a Check 2c annotation site (fails C-39 at Phase 2, so C-40 is also absent). V-05 is the only variation that achieves the minimal Phase 7 repair form (C-42 target) by combining C-38 delegation with C-39 self-contained upstream blocks.
d-annotation from Check 2c warned ..., and Phase 6a entity-type referent column ..." — Phase 2 is a named source because V-05 carries an individually labeled Check 2c annotation in Phase 2's HELD/SHIFTED block, establishing that the HELD/SHIFTED block is the earliest Check 2c decision point. V-04 fails C-40 because its Phase 2 uses a shared bullet-list format that omits a Check 2c-specific annotation; V-04 passes C-33 (Phase 2 has Check 4 Part C annotation) but Phase 2 carries no Check 2c constraint visibility.
- C-41 sourced from the "(Phase 2 promoted to named source by C-39)" note in the C-37 Check 2c evaluation: V-05 names 3 sources for Check 2c; V-01 and V-04 (both C-37 PASS) name only Phase 5 and Phase 6a. V-01 and V-04 pass C-37 because Phase 2 was not a Check 2c annotation site for them (they fail C-39, so Phase 2 has no individually labeled Check 2c block). A variation that satisfies C-40 (Phase 2 carries Check 2c annotation) but whose Phase 7 back-reference still names only two sources fails C-41 while passing C-37 — the source set was established before C-40 was in scope.
- C-42 sourced from the C-38 table contrast between V-01 and V-05: V-01 fails C-38 for Check 6b because paths are "restated inline without delegation phrase." The failure class C-42 captures is the mirror: a block with the delegation phrase followed by inline (a)/(b) paths. Both conditions produce two repair surfaces; C-38 catches the "no delegation" case; C-42 catches the "delegation plus inline" case. V-05's repair blocks pass C-38 with delegation-only content, establishing the minimal form as the excellence target.

---

### v11 (2026-03-19) — R10 excellence patterns

**Formula update**: aspirational denominator changes from `/28` to `/31` (28 criteria → 31 criteria).

**Three new aspirational criteria**:

| ID | Pattern | Extends | Failure class caught |
|----|---------|---------|---------------------|
| C-37 | Phase 7 back-references enumerate ALL upstream sources per gate | C-34 (back-ref exists) | Back-reference names only one of two upstream sources — the second upstream warning is unaccounted |
| C-38 | Phase 7 delegates repair to upstream annotation by label | C-35+C-32 (repair exists upstream + in Phase 7) | Phase 7 copies (a)/(b) paths rather than delegating by label — two surfaces that can diverge on edit |
| C-39 | Forward-annotation blocks are self-contained resolution modules | C-35 (upstream has (a)/(b)) | Block contains (a)/(b) but is not independently resolvable — author must reach Phase 7 to interpret failure condition or locate paths |

**Structural chain**: C-37 extends C-34 (back-reference exists → back-reference is complete). C-38 extends C-35+C-32 (repair upstream + repair in Phase 7 → Phase 7 delegates rather than duplicates). C-39 extends C-35 (upstream has (a)/(b) → upstream block is independently resolvable without Phase 7). Each catches a failure class the others cannot.

**Evidence base**:
- C-37 sourced from V-05 Check 6b back-reference: "Phase 6a forward-annotation warned... and Phase 5 Forward-annotation from Check 6b warned... — an entry failing Check 6b missed that constraint at its earliest visible points." V-01 and V-04 name only Phase 6a as the upstream source for Check 6b and pass C-34 but fail C-37; V-05 names both Phase 6a and Phase 5, quantifying the full breadth of missed warnings.
- C-38 sourced from V-05 Signal 2: Phase 7 repair blocks read "Apply the Forward-annotation repair paths: (a)... (b)..." — the upstream annotation is the authoritative repair source, referenced by label. V-02 passes C-35 (upstream has (a)/(b)) but fails C-38 because its Phase 7 repair blocks restate the paths rather than delegating to the upstream annotation by name.
- C-39 sourced from V-05 Signal 3: each "Forward-annotation from Check X:" block in Phase 5 and Phase 6a contains gate label + unconditional failure condition + (a)/(b) repair paths as a complete unit. V-03 fails C-39 because its Phase 5 forward-annotation blocks state the failure condition only, requiring the author to reach Phase 7 to discover the repair options.

---

### v10 (2026-03-19) — R9 excellence patterns

**Formula update**: aspirational denominator changes from `/25` to `/28` (25 criteria → 28 criteria).

**Three new aspirational criteria**:

| ID | Pattern | What it captures |
|----|---------|-----------------|
| C-34 | Phase 7 gate failures back-reference upstream forward-annotations | Phase 7 repair text names the upstream phase that warned about this constraint class, closing the accountability loop — a skill can pass C-33 (annotations exist) but fail C-34 (Phase 7 never references them back) |
| C-35 | Upstream forward-annotations embed (a)/(b) repair paths | The upstream annotation blockquote carries not just the failure condition but the (a)/(b) repair options from Phase 7 — a skill can pass C-32 (repair in Phase 7) and C-33 (condition upstream) but fail C-35 (repair options not propagated upstream) |
| C-36 | Single-artifact multi-gate annotation coverage | When a Phase 5 MANUSCRIPT OUTCOME is checked by both Check 2c and Check 6b, the template carries forward-annotations from both gates — a skill can pass C-33 (Phase 5 is annotated) but fail C-36 if the second gate's warning is absent from the same template slot |

---

### v9 (2026-03-19) — R8 excellence patterns

**Formula update**: aspirational denominator changes from `/22` to `/25` (22 criteria → 25 criteria).

**Three new aspirational criteria**:

| ID | Pattern | What it captures |
|----|---------|-----------------|
| C-31 | Phase 6a entity-type column propagation | Pushes the C-28 entity-type constraint backward into the Phase 6a reconciliation table schema — the referent must be named during authoring, not insertable at gate time |
| C-32 | Branched repair protocols in Phase 7 gate checks | Extends C-24's "gate exists and blocks" into "gate prescribes structured recovery" — each failing gate gives two or more labeled repair paths, converting a stop sign into a decision fork |
| C-33 | Gate failure conditions forward-annotated upstream | Extends C-32's gate-level repair into authoring-time visibility — Phase 2, Phase 5, and Phase 6a each carry forward-annotated failure conditions from their downstream Phase 7 gates, so the author encounters the constraint at the decision point, not after the draft is complete |

---

### v8 (2026-03-19) — R7 excellence patterns

**Formula update**: aspirational denominator changes from `/19` to `/22` (19 criteria → 22 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-28 | Axis G `evidence instantiation gate` | Phase 7 Check 2c follows Check 2b: after Check 2b verifies a valid evidence form category label is present, Check 2c verifies the label is instantiated — "prior literature" resolves to a specific cited paper or author, "statistical result" to a specific statistic or test, "methodological argument" to a specific methodological principle; naming the category without a concrete referent fails Check 2c even when Check 2b passes |
| C-29 | Axis H `SHIFTED decision gate — REINSTATE / CONFIRM CHANGE` | Phase 7 Check 4 Part C follows Check 4 Part B: after Part B verifies classification, Part C requires a binding manuscript decision per SHIFTED entry — PRESSURE-DRIVEN entries must state REINSTATE or NO REINSTATE with a one-sentence rationale; EVIDENCE-DRIVEN entries must state CONFIRM CHANGE; the decision is recorded before write and cannot be deferred to the cover letter |
| C-30 | Axis I `cover letter claim-outcome consistency gate` | Phase 7 Check 6b follows Check 6: after Check 6 verifies each Paragraph 1 change claim has at least one R-ID reference, Check 6b verifies each referenced R-ID resolves to a CHANGE MANUSCRIPT OUTCOME (not P1 no-change); a cover letter claim asserting "we changed X in response to R-N" while R-N's MANUSCRIPT OUTCOME is P1 is a structural contradiction detectable only at this gate |

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
| Aspirational (C-09–C-42) | 10 | (passed / **34**) × 10 |

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
| C-07 | Cover letter present and structurally correct | format | Cover letter has Paragraph 1 (3-4 specific changes with parenthetical R-ID references) and Paragraph 2 (disagreement framing or explicit statement of none). Both paragraphs updated in Phase 6a reconciliation. PARTIAL if one paragraph missing or reconciliation step absent. |
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
| C-14 | Critical constraints in pre-workflow RULE-N block | structure | All binding constraints (format, register, length, output path) appear in a named RULE-1, RULE-2, block before the workflow phases begin. No binding constraint is embedded only inside a phase description. |
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
| C-28 | P1 no-change evidence instantiation gate (Phase 7 Check 2c) | depth | Check 2c appears as an explicit numbered step in Phase 7, following Check 2b. After Check 2b verifies a valid evidence form category label is present, Check 2c verifies the label is instantiated: "prior literature" resolves to a specific cited paper or author; "statistical result" resolves to a specific statistic or test; "methodological argument" resolves to a specific methodological principle. Naming the category label without a concrete referent fails Check 2c even when Check 2b passes. Distinct from C-25 (which tests label presence only) — C-28 is the only criterion that can detect evidence-label-without-substance at write time. |
| C-29 | SHIFTED decision gate — REINSTATE / CONFIRM CHANGE commitment (Phase 7 Check 4 Part C) | depth | Check 4 Part C appears as an explicit numbered step in Phase 7, following Check 4 Part B. After Part B verifies PRESSURE-DRIVEN / EVIDENCE-DRIVEN classification, Part C requires a binding manuscript decision per SHIFTED entry: PRESSURE-DRIVEN entries must state REINSTATE or NO REINSTATE with a one-sentence rationale; EVIDENCE-DRIVEN entries must state CONFIRM CHANGE. The decision is recorded before write and cannot be deferred to the cover letter. Distinct from C-27 (which tests classification only) — C-29 converts the classification into a committed manuscript outcome. |
| C-30 | Cover letter claim-outcome consistency gate (Phase 7 Check 6b) | format | Check 6b appears as an explicit numbered step in Phase 7, following Check 6. After Check 6 verifies each Paragraph 1 change claim has at least one R-ID reference, Check 6b verifies each referenced R-ID resolves to a CHANGE MANUSCRIPT OUTCOME (not P1 no-change): a cover letter claim asserting "we changed X in response to R-N" while R-N's MANUSCRIPT OUTCOME is P1 is a structural contradiction. Distinct from C-26 (which tests R-ID presence only) — C-30 is the only criterion that can detect cover-letter/manuscript-outcome divergence before write. |
| C-31 | Phase 6a audit table carries entity-type referent column | depth | The Phase 6a reconciliation table schema includes an "entity-type referent" column (not just evidence category + instance), requiring the executor to name the concrete entity-type referent per P1 no-change entry during mid-workflow reconciliation. An executor cannot complete Phase 6a without naming the referent, closing the last-second-insertion loophole that exists when C-28 lives only in Phase 7. Distinct from C-28 (which enforces entity-type at the Phase 7 gate) — C-31 is the only criterion that propagates the entity-type constraint into the authoring-time audit surface. |
| C-32 | Phase 7 gate checks include branched repair protocols | structure | Each Phase 7 gate check that can fail includes a branched repair protocol specifying two or more structurally distinct corrective paths labeled (a) / (b): the repair choice is determined by the failure type rather than left to author discretion. The protocol is embedded within the gate check text itself, not in a separate appendix. Distinct from C-24 (which requires gate checks to exist and block write) — C-32 is the only criterion that requires each blocking gate to provide structured recovery rather than only detection. |
| C-33 | Gate failure conditions forward-annotated into upstream phase text | structure | Gate constraints enforced in Phase 7 are also forward-annotated as explicit failure conditions in the upstream phases where the author makes the relevant decision: Phase 2 for SHIFTED anti-deferral constraints; Phase 5 MANUSCRIPT OUTCOME template for entity-type requirements; Phase 6a for cover-letter/outcome consistency. An author working through the upstream phase sees the failure condition at the moment of decision. Distinct from C-32 (which embeds repair protocols at the Phase 7 gate) — C-33 is the only criterion that requires constraint visibility at the upstream authoring decision point where the failure can still be avoided. |
| C-34 | Phase 7 gate failures back-reference the upstream forward-annotation | structure | Each Phase 7 gate check whose failure class was forward-annotated into an upstream phase includes an explicit back-reference in the repair protocol text, naming the upstream phase and the specific annotation that warned about this constraint: e.g., "Phase 2 forward-annotation warned that this decision must be recorded in Phase 6a — an entry failing this check missed that constraint at its earliest visible point." The back-reference appears within the repair protocol at the point of failure, not only in the check preamble. Distinct from C-33 (which requires upstream annotations to exist) — C-34 closes the accountability loop by requiring Phase 7 to confirm the upstream warning was present when the failure occurs, converting detection into a learning signal about where the author's attention failed. |
| C-35 | Upstream forward-annotations embed (a)/(b) repair paths, not only failure conditions | structure | Forward-annotations in upstream phases (Phase 2, Phase 5, Phase 6a) include the branched (a)/(b) resolution options from Phase 7 within the annotation blockquote itself. The annotation is self-contained: the author sees both the failure condition and the structurally distinct repair paths at the authoring-time decision point. A forward-annotation that states "this will fail Check N" without naming the repair options is a warning, not a resolution surface. Distinct from C-33 (which requires failure condition visibility upstream) and C-32 (which requires (a)/(b) repair in Phase 7) — C-35 propagates the repair structure into the upstream authoring surface, enabling resolution at the decision point without reaching Phase 7. |
| C-36 | Single-artifact multi-gate forward-annotation coverage | depth | When a single upstream artifact (e.g., Phase 5 MANUSCRIPT OUTCOME) is checked by multiple downstream Phase 7 gates (e.g., both Check 2c and Check 6b apply to the same MANUSCRIPT OUTCOME entry), the upstream template carries forward-annotations from ALL applicable downstream gate checks, not only the most prominent one. A template annotating Check 2c but omitting Check 6b leaves the second failure class invisible during authoring even when the author reads the annotation. Distinct from C-33 (which requires forward-annotations to exist per phase but does not require complete gate coverage per artifact) — C-36 is the only criterion that prevents partial annotation gaps where an upstream artifact's second or third applicable Phase 7 gate check is never surfaced at authoring time. |
| C-37 | Phase 7 back-references enumerate ALL upstream sources per gate | structure | When a Phase 7 gate check's failure class was forward-annotated from multiple upstream phases, the back-reference names every upstream phase and annotation that warned about this constraint — not only the most proximate or prominent one. The canonical form: "Phase X forward-annotation warned that [constraint], and Phase Y Forward-annotation from Check N warned of this constraint at [authoring point] — an entry failing this check missed that constraint at its earliest visible points." A back-reference naming only one of two upstream sources leaves the second warning unaccounted. Distinct from C-34 (which requires a back-reference to exist) — C-37 is the only criterion that requires the back-reference to be complete, mapping every upstream warning site rather than only the nearest one. |
| C-38 | Phase 7 delegates repair to upstream annotation by label | structure | The Phase 7 "If FAIL" repair block references the upstream forward-annotation as the authoritative repair source by its label ("Apply the Forward-annotation repair paths: (a)/(b)") rather than restating the (a)/(b) paths inline. Phase 7 names the upstream block as the canonical repair surface; the upstream block is not duplicated but cross-referenced. A repair block that copies the paths from the upstream annotation creates two surfaces that can diverge on edit; a repair block that delegates by label creates a single authoritative surface. Distinct from C-35 (which requires (a)/(b) to exist upstream) and C-32 (which requires (a)/(b) to exist in Phase 7) — C-38 is the only criterion that requires the two surfaces to be unified into a named cross-reference rather than maintained as independent copies. |
| C-39 | Forward-annotation blocks are self-contained resolution modules | structure | Each "Forward-annotation from Check X:" block in an upstream phase contains all three components as a complete, independently-resolvable unit: (1) the gate label ("Forward-annotation from Check X:"), (2) an unconditional failure condition statement (the specific condition that triggers gate failure, not a conditional "if you did Y"), and (3) the (a)/(b) repair paths. The block is structured so the author can read it, identify whether the failure condition applies, and select a repair path without consulting Phase 7. A block whose failure condition is conditional on Phase 7 context, or whose repair paths are absent, requires the author to leave the authoring phase to resolve the constraint. Distinct from C-35 (which requires (a)/(b) to be present upstream) — C-39 is the only criterion that requires the three components to form a coherent, independently-actionable unit rather than a collection of upstream fragments. |
| C-40 | Phase 2 annotation coverage extends to Check 2c as well as Check 4 Part C | structure | Phase 2's HELD/SHIFTED pre-commitment block is the first point at which the author commits a P1 no-change position and names an evidence form, making it the earliest Check 2c decision point in addition to the earliest Check 4 Part C decision point. Phase 2 carries a C-39-compliant "Forward-annotation from Check 2c:" block alongside the "Forward-annotation from Check 4 Part C:" block required by C-33. A Phase 2 block carrying only the Check 4 Part C annotation passes C-33 but fails C-40 if the evidence form label commitment is also made in Phase 2. Distinct from C-33 (which requires Phase 2 annotation for SHIFTED constraints only) — C-40 requires Phase 2 annotation coverage to match all Phase 7 gate checks for which Phase 2 is the earliest decision point, not only the SHIFTED gate. |
| C-41 | Phase 7 Check 2c back-reference enumerates Phase 2 as a third upstream source | structure | When C-40 is satisfied (Phase 2 carries a Check 2c forward-annotation), the Phase 7 Check 2c back-reference names Phase 2 as an upstream source alongside Phase 5 and Phase 6a, yielding a three-source enumeration: "Phase 2 Forward-annotation from Check 2c warned..., Phase 5 Forward-annotation from Check 2c warned..., and Phase 6a entity-type referent column..." A back-reference naming only Phase 5 and Phase 6a passed C-37 before C-40 was established; after C-40 adds Phase 2 to the annotation graph, the back-reference source set must be updated. A skill can pass C-37 (all previously-known sources named) while failing C-41 if Phase 2 was added as a Check 2c annotation site by C-40 but the back-reference was not updated to reflect the expanded source set. Distinct from C-37 (which requires all known sources to be named) — C-41 requires the known-source set itself to be complete after C-40 extends the annotation graph. |
| C-42 | Phase 7 "If FAIL" repair blocks satisfying C-38 contain only the delegation line | structure | When a Phase 7 gate check delegates repair to an upstream annotation by label (satisfying C-38) and the upstream annotation is C-39-compliant (self-contained), the Phase 7 "If FAIL" repair block's entire content is the delegation line — no supplementary inline (a)/(b) paths or repair commentary follow it. A block beginning with "Apply the Forward-annotation repair paths:" and then listing inline paths creates two repair surfaces: the upstream annotation and the inline content; these surfaces can diverge on edit even though C-38 passes (delegation phrase is present). A block that passes C-38 (delegation phrase exists) fails C-42 if the delegation line is a preamble to inline content rather than the complete repair statement. Distinct from C-38 (which tests that the delegation phrase is present) — C-42 tests that the delegation is the entire repair statement, converting Phase 7 from a repair manual into a pure detection-and-delegation gate. |
