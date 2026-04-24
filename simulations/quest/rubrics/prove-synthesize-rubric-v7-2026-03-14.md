All checks pass. Here is the complete v7 rubric as written:

---

**prove-synthesize-rubric-v7** — written to `simulations/quest/rubrics/prove-synthesize-rubric-v7-2026-03-14.md`

**Three new aspirational criteria:**

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-26 | Violation taxonomy registry at document open | C-23 | All violation types (PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION VIOLATION, FALSE ATTESTATION VIOLATION, PHASE-ADVANCE VIOLATION) are indexed in a named registry block **before FRONTMATTER** — taxonomy visible before any fill window is encountered. NOT: violation names appear only inline at each bound without a preceding registry. NOT: registry appears after FRONTMATTER. |
| C-27 | Arrow-chain three-site chain of custody | C-24, C-25 | Arrow-chain field:value notation is traceable at all three named sites: **creation** in RECORD DIAGNOSIS, **audit** in PRE-FLIGHT Phase B (SCHEMA-CITATION AUDIT), **application** in JUDGE confidence paragraph. Two-site presence does not satisfy. NOT: arrow-chain in RECORD DIAGNOSIS only. NOT: PRE-FLIGHT audits but JUDGE does not apply. NOT: JUDGE applies without PRE-FLIGHT having explicitly verified. |
| C-28 | PRE-FLIGHT anti-skip gate | C-25 | A named gate at **PRE-FLIGHT's entry** names PHASE-ADVANCE VIOLATION (or equivalent) before any phase step is listed — the bypass failure mode is encountered before the steps can be skipped. NOT: PRE-FLIGHT begins with phase steps without a preceding entry gate. NOT: bypass failure mode named only at end of PRE-FLIGHT or at JUDGE boundary (post-hoc). |

**Scoring delta:**

| | v6 | v7 |
|-|----|-----|
| Aspirational | 42.5 pts / 17 criteria | **50.0 pts / 20 criteria** |
| Max composite | 132.5 | **140.0** |
| Golden threshold | >= 90 | >= 90 (unchanged) |

**R6 calibration under v7:** V-05 scores 140.0 (all three new pass); V-01/V-02/V-03/V-04 all unchanged (0 new criteria pass — each lacks the preconditions for C-26/C-27/C-28).
for a front-indexed registry.
- **C-24/C-25/C-27**: C-24 requires arrow-chain in RECORD DIAGNOSIS. C-25 requires a named PRE-FLIGHT phase. C-27 requires the arrow-chain propagate across three sites -- creation (ADVERSARY), audit (PRE-FLIGHT), and application (JUDGE). Both C-24 and C-25 are necessary but not sufficient for C-27.
- **C-25/C-28**: C-25 requires a named PRE-FLIGHT structural phase between ADVERSARY and JUDGE. C-28 requires an anti-skip gate at PRE-FLIGHT entry that names the bypass failure mode before any phase step is encountered. PRE-FLIGHT existing is necessary but not sufficient for C-28.

**R6 Q-answer confirmations** (all three): (Q1) C-23 fires with inline embedding -- V-01 pattern satisfies C-23; standalone labels outside the prohibition text are not required; (Q2) C-24 fires with arrow-chain in RECORD DIAGNOSIS alone (V-02 PASS without PRE-FLIGHT) -- audit propagation is C-27 territory, not C-24; (Q3) three-phase PRE-FLIGHT fully satisfies C-25 (V-03 PASS); SCHEMA-CITATION AUDIT as named Phase B is the direct C-27 predecessor.

**C-11/C-12 tension**: Confirmed across R2, R3, R4, R5, R6. Both criteria remain; the tension is a feature.

**C-17/C-21 relationship**: C-17 requires the failure mode be *derived from* the record's structural properties. C-21 requires those properties be *traceable to* the SURVEYOR phase inventory -- verifiable by cross-reference, not merely plausible. Both can be satisfied independently; the highest-quality artifacts satisfy both.

**C-18/C-22 relationship**: C-18 fires when the register word opens the commitment sentence at the output level. C-22 requires an explicit NOT: gate at the instruction level. C-18 is necessary but not sufficient for C-22.

**C-19/C-20 relationship**: C-19 requires the frontmatter block exist and prohibits retroactive completion. C-20 requires each field be filled at its individually correct structural moment -- phase-sequenced, not batch-filled at start or end.

**C-20/C-23 relationship**: C-20 requires per-field NOT: gates bounding the fill window at both ends. C-23 requires each bound be expressed as a named violation category -- not merely "NOT: fill before X" but a label such as "premature completion violation" that a writer can cite. Named violations create addressable failure types; unnamed prohibitions do not. C-20 is necessary but not sufficient for C-23.

**C-21/C-24 relationship**: C-21 requires the adversarial challenge cite structural properties cross-referenceable to the SURVEYOR inventory. C-24 requires that citation be expressed as field:value notation within the RECORD DIAGNOSIS text, producing a one-lookup falsifiability guarantee. C-21 is satisfied by prose derivation that names the inventoried property; C-24 requires the explicit field:value syntax. C-21 is necessary but not sufficient for C-24.

**C-22/C-25 relationship**: C-22 requires dual-layer register-word enforcement -- output-level format plus instruction-level NOT: gate. C-25 requires the instruction-level gate be a named structural phase (PRE-FLIGHT or equivalent) positioned between ADVERSARY and JUDGE -- encountered before the commitment sentence is reached. A DETERMINATION SEAL gate (C-22) is encountered at the moment of commitment; a PRE-FLIGHT gate (C-25) is encountered before commitment begins. C-22 is necessary but not sufficient for C-25.

**C-23/C-26 relationship**: C-23 requires named violation categories inline at each fill-window bound -- the writer encounters the violation name when reading the constraint. C-26 requires all violation categories be indexed as a named registry block before FRONTMATTER begins -- the violation taxonomy is visible before the first constraint is encountered. Inline naming satisfies C-23; front-indexing requires the additional registry block. C-23 is necessary but not sufficient for C-26.

**C-24/C-25/C-27 relationship**: C-24 requires arrow-chain field:value notation in RECORD DIAGNOSIS. C-25 requires a named PRE-FLIGHT structural phase between ADVERSARY and JUDGE. C-27 requires the arrow-chain propagate across all three named sites -- RECORD DIAGNOSIS creates the chain, PRE-FLIGHT Phase B audits it, JUDGE confidence paragraph applies it. A rubric satisfying C-24 alone has one-site chain creation; satisfying C-25 alone has a PRE-FLIGHT phase without chain audit; only a rubric satisfying both and extending to JUDGE application satisfies C-27. C-24 and C-25 are each necessary but not sufficient for C-27.

**C-25/C-28 relationship**: C-25 requires a named PRE-FLIGHT structural phase exist as a sequenced block between ADVERSARY and JUDGE. C-28 requires an explicit anti-skip gate at PRE-FLIGHT entry that names the bypass failure mode (PHASE-ADVANCE VIOLATION or equivalent) before any PRE-FLIGHT phase step is listed -- the gate is encountered before the steps can be skipped, not after. PRE-FLIGHT that begins with its phase steps satisfies C-25; only PRE-FLIGHT that begins with a named entry gate satisfies C-28. Entry-gate position is structurally prior to all phase content; a gate embedded within or after phase steps is not an entry gate. C-25 is necessary but not sufficient for C-28.

**Round 6 calibration**: All 5 R6 variations were Golden (117.5-132.5 under v6). V-05 achieved maximum 132.5 / 132.5. New criteria predicted from V-05 excellence signals (3/3). R6 Q-answers confirmed: (Q1) C-23 inline embedding confirmed to fire on V-01 -- named violation type within the NOT: sentence is sufficient; standalone registry is C-26 territory; (Q2) C-24 fires without PRE-FLIGHT audit -- arrow-chain creation in RECORD DIAGNOSIS alone satisfies C-24; V-03 SCHEMA-CITATION AUDIT as PRE-FLIGHT Phase B is the direct C-27 predecessor; (Q3) three-phase PRE-FLIGHT satisfies C-25; PHASE-ADVANCE VIOLATION at PRE-FLIGHT entry satisfies C-28; SCHEMA-CITATION AUDIT as Phase B + JUDGE application is C-27 mechanism.

---
## Essential Criteria (weight: 60 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Answer-first** | format | The synthesis opens with a direct answer to the hypothesis before any evidence or reasoning. The answer is a complete declarative sentence, not a hedge or a restatement of the question. |
| C-02 | **Confidence score present and calibrated** | correctness | A numeric confidence score (0-100) is stated. It is calibrated: high confidence (>=75) only when evidence strongly converges; low confidence (<=40) when evidence is mixed or thin. |
| C-03 | **Key evidence cited** | coverage | Exactly or up to 3 signals are named as key evidence. Each named signal is traceable to an artifact produced during the investigation (not invented). Each signal is explained in terms of *why* it influenced the answer. |
| C-04 | **Counter-evidence present** | correctness | At least one piece of evidence arguing *against* the answer is explicitly named. If none exists, the output states "no counter-evidence found" with a brief rationale. Omitting this section entirely is a fail. |
| C-05 | **Synthesis supersedes signals** | behavior | The synthesis takes a position -- it does not merely restate or list the investigation signals. The answer and confidence together constitute a judgment call, not a summary. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Principles extracted** | depth | At least one principle is stated -- something learned beyond this specific hypothesis that generalizes to future investigations. Principles are declarative ("X implies Y") not restatements of the finding. |
| C-07 | **Open questions identified** | coverage | At least one question the investigation did not resolve is named. Questions are specific and actionable, not generic ("more research needed"). |
| C-08 | **Confidence is explained** | depth | The confidence score is accompanied by a brief rationale (1-3 sentences) explaining what drove it up or down. Score alone without rationale is a partial pass (counts as fail for this criterion). |

---

## Aspirational Criteria (weight: 50.0 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Evidence hierarchy is argued** | depth | The output explains *why* the top signals outweighed the others -- not just what they are. A comparative question is present for each rank: "why this signal over the one below it?" A ranked argument is present, not a ranked list. |
| C-10 | **Synthesis is self-contained** | behavior | A reader with no access to the underlying investigation signals can understand the answer, the reasoning, and what to do next from the synthesis alone. No unexplained references to prior artifacts. The standalone mandate is stated explicitly in the opening, not assumed to emerge from structure. |
| C-11 | **Anti-pattern gates named explicitly** | behavior | At least one gate or checklist item names the failure mode by name rather than only naming the success condition. Example: "This is a ranked argument, not a ranked list" is stronger than "Evidence hierarchy is argued." A gate that names what *not* to do forecloses compliant-but-wrong outputs that pass presence checks. |
| C-12 | **Argumentative sections are prose** | depth | Evidence ranking, synthesis judgment, and confidence rationale are written as prose paragraphs, not tables or bullet lists. Tables are permitted only for enumerative sections (e.g., open questions list, principles list). Prose is a structural enforcement mechanism: it requires argument construction and cannot be satisfied by filling cells. |
| C-13 | **NOT:-first gate ordering** | behavior | Gates that enforce anti-patterns list the failure mode *before* the success condition. NOT: "[failure mode]" precedes the positive pass condition in each gate item. A gate that names the failure mode after the pass condition allows the writer to satisfy the presence check before encountering the prohibition. NOT:-first ordering forecloses the failure mode before the pass condition is reached. |
| C-14 | **Formal verdict register** | behavior | The synthesis uses a dedicated lexical register for its judgment -- a term (RULING, VERDICT, DETERMINATION, FINDING, or equivalent) that signals commitment rather than summary. The register word appears as a sentence-level declaration (not as a section header or container label). Register-level commitment enforces anti-hedging independent of gate structure: a RULING cannot be followed by hedging language in a way that "Based on the evidence..." can. NOT: the register word appears only as a section header; `## VERDICT` labels a container and does not foreclose hedging at the commitment point. |
| C-15 | **Pre-committed counter-evidence** | behavior | The adversarial challenge (counter-evidence obligation) is issued structurally *before* the verdict section, not as a post-hoc reflection section after the determination. Pre-commitment forces the synthesis to issue its judgment against the best opposing case already on the table. NOT: counter-evidence section follows the verdict and is selected after the position is formed. C-04 requires counter-evidence present; C-15 requires it structurally precede the verdict. |
| C-16 | **Role-labeled cognitive phases** | behavior | Each phase is assigned a procedural identity label (SURVEYOR, ADVERSARY, JUDGE, SCHOLAR, or equivalent) AND explicit prohibition statements foreclose what that identity cannot produce: "A JUDGE cannot hedge. Violation is a procedural breach." / "An ADVERSARY cannot advocate." Labels name who the writer is in that phase; prohibition statements foreclose what that identity cannot produce. One without the other is insufficient -- identity without foreclusion creates a role name without a constraint; prohibition without identity creates a rule without a subject. NOT: phase labels are descriptive titles (OVERVIEW, VERDICT, PRINCIPLES) that do not foreclose output type. NOT: role labels are present without accompanying prohibition statements -- labels alone do not satisfy this criterion. |
| C-17 | **Record-specific anti-pattern declaration** | behavior | The adversarial challenge names the failure mode most likely given *this record's specific structure* -- not a generic anti-pattern that could appear in any synthesis. The declaration is derived from the record at hand: "given this record's thin signal set, the most likely failure mode is confidence inflation" passes; "do not list signals instead of synthesizing" does not. C-11 requires a failure mode be named; C-17 requires it be diagnosed from the record under review. NOT: the adversarial challenge names a generic anti-pattern that does not reference the record's signal composition or structural properties. |
| C-18 | **Register word opens the commitment sentence** | behavior | The formal verdict register word (RULING, VERDICT, DETERMINATION, FINDING, or equivalent from C-14) is the first word of the judgment sentence: `DETERMINATION: YES` or `VERDICT: the hypothesis is supported`. A register word that appears mid-sentence or after introductory language allows hedging to precede it. C-14 requires the register word appear in a sentence-level declaration; C-18 requires it open that sentence. NOT: the register word appears in a section header, parenthetical, or after introductory language ("Our final determination is..."). |
| C-19 | **Frontmatter commitment declarations** | behavior | The artifact opens with machine-readable boolean declarations recording whether each structural constraint was honored at output time: `adversary_pre_determination: true`, `register_word_used: true`, `record_specific_antipattern: true`, or equivalent fields. Frontmatter booleans require the writer to commit before the prose begins and cannot be retroactively satisfied. NOT: structural compliance is implicit, undeclared, or detectable only by reading the full artifact. |
| C-20 | **Phase-sequenced frontmatter completion** | behavior | Each frontmatter boolean is filled at the structural moment its corresponding phase becomes determinable -- not all at the artifact's start before phases are written, and not all at the end after the prose is complete. `adversary_pre_determination: true` can only be truthfully filled after the ADVERSARY phase content is written and before the JUDGE phase begins; filling it earlier is a false declaration, filling it later is retroactive completion. Sequential determinability enforces phase order: a writer who fills phase-sequenced booleans correctly must complete each structural phase before its boolean becomes truthfully fillable. C-19 requires the frontmatter block exist and prohibits retroactive completion; C-20 requires each field be individually sequenced to its phase. NOT: all frontmatter fields are filled at the artifact's start before any phases are written. NOT: all fields are filled at the artifact's end after full prose completion. |
| C-21 | **SURVEYOR-traceable anti-pattern diagnosis** | correctness | The failure mode diagnosis in the adversarial challenge cites structural properties that are traceable to values stated in the SURVEYOR phase inventory. A reader can falsify the diagnosis by checking whether the cited property -- record count N, method diversity, signal concentration, or equivalent -- appears in the SURVEYOR output. The diagnosis is reader-falsifiable, not merely reader-evaluable. C-17 requires the failure mode be derived from the record's structure; C-21 requires the derivation be verifiable by cross-reference to the SURVEYOR inventory. NOT: the failure mode diagnosis cites a structural property that does not correspond to a value stated in the SURVEYOR phase. NOT: the diagnosis is stated without reference to a specific inventoried structural property. |
| C-22 | **Dual-layer register-word enforcement** | behavior | The register-word-first constraint (C-18) is enforced at both output level and instruction level. Output level: the commitment sentence format (`DETERMINATION: [YES/NO/MAYBE]`) structurally produces the register word as the first word. Instruction level: an explicit NOT: gate forecloses the failure mode by name ("NOT: the register word appears in a section header, parenthetical, or after introductory language in the commitment sentence"). C-18 fires on output-level enforcement alone; C-22 requires the additional instruction-level gate as a second enforcement layer. Defense-in-depth: the gate forecloses prompt drift toward register-word-after-introductory-language before the commitment sentence is reached. NOT: the commitment sentence format produces correct behavior but no explicit prohibition gate names the register-word-placement failure mode. |
| C-23 | **Phase-boundary named-violation gates** | behavior | Each frontmatter fill-window bound is expressed as a named violation category, not merely a NOT: condition. "NOT: `signal_count` filled before SURVEYOR content is written" is a prohibition; "Filling `signal_count` before SURVEYOR content is written is a **premature completion violation**; filling it after ADVERSARY content begins is a **deferred completion violation**" names the violation types. Named violations are citable by type: the writer understands *what they did*, not only *what to avoid*. Both bounds -- premature (too early) and deferred (too late) -- must carry named violation labels for each field. C-20 requires the NOT: bounds exist; C-23 requires each bound express a named violation category. NOT: fill-window bounds are stated as NOT: conditions without naming the violation type. NOT: violation naming covers only one bound (premature named, deferred unnamed, or vice versa). |
| C-24 | **Schema-field:value-quoted RECORD DIAGNOSIS** | correctness | The RECORD DIAGNOSIS cites SURVEYOR inventory values using explicit field:value notation inline in the diagnosis text: `convergence_pattern: fragmented -> failure mode: false consensus from weak signals`. A reader falsifies the diagnosis in one lookup -- locate the named field in SURVEYOR output, verify the value matches. No re-reading required. C-21 requires cross-reference traceability by naming the inventoried property; C-24 requires the citation be expressed as field:value syntax within the RECORD DIAGNOSIS itself, binding the diagnosis claim to a specific inventory entry by name and value. NOT: the RECORD DIAGNOSIS describes structural properties in prose without field:value citation syntax. NOT: field names are cited without corresponding values, leaving the lookup ambiguous. |
| C-25 | **Pre-JUDGE pre-flight structural audit block** | behavior | A named PRE-FLIGHT block (or equivalent) is placed as a sequenced structural phase between ADVERSARY and JUDGE. The register-word gate and schema-citation verification are phase steps encountered before the commitment sentence is written -- not embedded within the commitment sentence format and not listed as post-judgment reflection items. C-22 requires the instruction-level NOT: gate exist; C-25 requires that gate be a named structural phase occurring before JUDGE begins. Defense-in-depth through phase sequencing: the PRE-FLIGHT block forecloses the register-word and schema-citation failure modes before the commitment sentence is reachable. A DETERMINATION SEAL gate satisfies C-22 (encountered at commitment); only a pre-JUDGE structural phase satisfies C-25 (encountered before commitment). NOT: the register-word prohibition is embedded in the commitment sentence format rather than as a preceding structural phase. NOT: pre-flight checks appear as post-judgment reflection items rather than as a structural block between ADVERSARY and JUDGE. |

| C-26 | **Violation taxonomy registry at document open** | behavior | All named violation categories are indexed in a dedicated registry block before the FRONTMATTER declarations section -- the complete violation taxonomy is visible before any fill window is encountered. A writer reading the artifact encounters every violation type (PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION VIOLATION, FALSE ATTESTATION VIOLATION, PHASE-ADVANCE VIOLATION, and equivalents) as an indexed set before reaching any constraint that references them. C-23 requires violation names appear inline at each fill-window bound; C-26 requires the complete set be front-indexed in a named registry. Named inline at point-of-use is C-23; named inline plus indexed registry before FRONTMATTER is C-26. NOT: violation names appear only within the fill-window instructions where they apply, without a preceding registry block. NOT: the registry block appears after FRONTMATTER or within a phase section rather than before FRONTMATTER begins. |
| C-27 | **Arrow-chain three-site chain of custody** | correctness | The arrow-chain field:value notation propagates across three named verification sites: creation in RECORD DIAGNOSIS (ADVERSARY phase), audit in a named PRE-FLIGHT structural phase (e.g., SCHEMA-CITATION AUDIT as Phase B), and application in the JUDGE confidence paragraph. A reader can trace each cited inventory field from its diagnostic origin through its PRE-FLIGHT verification to its application in the final commitment. C-24 requires arrow-chain in RECORD DIAGNOSIS; C-25 requires a PRE-FLIGHT phase; C-27 requires the arrow-chain be present and traceable at all three sites. Two-site presence (creation + audit without JUDGE application, or creation + application without PRE-FLIGHT audit) satisfies C-24 and C-25 but not C-27. NOT: arrow-chain appears in RECORD DIAGNOSIS only without PRE-FLIGHT audit verification. NOT: PRE-FLIGHT audits schema citations but the JUDGE confidence paragraph does not reference the audited chain. NOT: the JUDGE paragraph applies the chain without the PRE-FLIGHT audit step having explicitly verified it. |
| C-28 | **PRE-FLIGHT anti-skip gate** | behavior | An explicit named gate is placed at the entry to the PRE-FLIGHT block, naming the bypass failure mode as PHASE-ADVANCE VIOLATION (or equivalent) before any PRE-FLIGHT phase step is listed. The gate forecloses the looking-complete-but-incomplete failure mode: advancing to JUDGE without completing PRE-FLIGHT is named as a violation before the steps that would be skipped are encountered. C-25 requires the PRE-FLIGHT structural phase exist between ADVERSARY and JUDGE; C-28 requires that phase be gated against bypass with a named violation at its entry point, encountered before any phase content. A PRE-FLIGHT block that begins with its phase steps satisfies C-25 but not C-28. NOT: the PRE-FLIGHT block begins with phase steps without a preceding named anti-skip gate at the block entry point. NOT: the bypass failure mode is named only at the end of PRE-FLIGHT or at the JUDGE boundary -- post-hoc naming rather than entry-gate naming does not satisfy C-28. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 90 |
| Passing | All essential pass, composite < 90 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 50.0 points total (20 criteria, 2.5 points each)
- Max composite: 140.0

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 3/20 pass -> 3/20 * 50 = 7.5
- **Composite = 75.5** -- fails golden (essential incomplete), failing overall

### Round 1 calibration (under v2 rubric)

All 5 Round 1 variations were Golden (90-100). Differentiation was entirely in the aspirational tier:

| Score | Variations | Pattern |
|-------|-----------|---------|
| 100 | V-05 | Standalone mandate in opening sentence + explicit "ranked argument, not ranked list" distinction |
| 95 | V-02, V-03, V-04 | Argued hierarchy (C-09 pass) but standalone not explicitly mandated (C-10 fail) |
| 90 | V-01 | Table-based hierarchy (C-09 fail) + no standalone mandate (C-10 fail) |

### Round 2 calibration (under v2 rubric)

All 5 Round 2 variations were Golden (97.5-100). Differentiation narrowed to C-11/C-12 structural tension:

| Score | Variation | Pattern |
|-------|-----------|---------|
| 100 | V-01, V-02, V-04, V-05 | R1 fixes baked in; C-11 and C-12 both satisfied |
| 97.5 | V-03 | Continuous prose design maximized C-12; eliminating gates made C-11 structurally impossible |

C-13, C-14, C-15 derived from R2 winning mechanisms.

### Round 3 calibration (under v3 rubric)

All 5 Round 3 variations were Golden (102.5-107.5). New criteria perfectly predicted (5/5):

| Score | Variation | New criteria passed |
|-------|-----------|---------------------|
| 107.5 | V-05 | C-13, C-14, C-15 |
| 105.0 | V-04 | C-13, C-14 |
| 102.5 | V-01 | C-13 only |
| 102.5 | V-02 | C-14 only |
| 102.5 | V-03 | C-15 only |

C-16, C-17, C-18, C-19 derived from R3 V-05 winning mechanisms: role-labeled phases, record-specific anti-pattern diagnosis, register-word-first commitment, frontmatter boolean declarations.

### Round 4 calibration (under v4 rubric)

All 5 Round 4 variations were Golden (112.5-117.5). V-05 achieved maximum 117.5. New criteria predicted from V-05 excellence signals (3/3):

| Score (v4) | Score (v5) | Variation | v4 new criteria passed | v5 delta |
|------------|------------|-----------|------------------------|----------|
| 117.5 | 125.0 | V-05 | C-16, C-17, C-18, C-19 | +7.5 (C-20, C-21, C-22 all pass) |
| 115.0 | 122.5 | V-04 | C-16, C-17, C-18 | +7.5 (C-21, C-22 pass; C-20 pass) |
| 113.75 | 112.5 | V-03 | C-18, C-19 (partial C-16) | -1.25 (C-16 partial removed; C-20/C-21/C-22 fail) |
| 112.5 | 115.0 | V-01 | C-16, C-18 | +2.5 (C-22 pass; C-20/C-21 fail) |
| 112.5 | 115.0 | V-02 | C-17, C-18 | +2.5 (C-21 pass; C-20/C-22 fail) |

C-16 partial-credit removal: V-03's ad hoc 1.25 partial (labels only, no prohibition) is no longer credited under v5's clarified pass condition. C-20, C-21, C-22 derived from R4 V-05 excellence signals: phase-sequenced frontmatter completion, SURVEYOR-traceable failure mode diagnosis, dual-layer register-word enforcement.

### Round 5 calibration (under v5 rubric)

All 5 Round 5 variations were Golden (115.0-125.0). V-05 achieved maximum 125.0. New criteria predicted from V-05 excellence signals (3/3):

| Score (v5) | Variation | R5 aspirational passed | v6 candidates |
|------------|-----------|------------------------|---------------|
| 125.0 | V-05 | All 14 (C-09 through C-22) | C-23, C-24, C-25 all predicted |
| 122.5 | V-04 | 13/14 (C-19 fail) | C-23, C-24 predicted; C-25 partial (DETERMINATION SEAL satisfies C-22, not C-25) |
| 115.0 | V-03 | 10/14 (C-16/C-17/C-19/C-20 fail) | PRE-FLIGHT mechanism satisfies C-25 |
| 115.0 | V-01 | 10/14 (C-16/C-17/C-21/C-22 fail) | Per-field NOT: gates satisfy C-20; C-23 requires named violation categories |
| 115.0 | V-02 | 10/14 (C-16/C-19/C-20/C-22 fail) | Schema cross-reference satisfies C-21; field:value syntax satisfies C-24 |

R5 Q-answer confirmations: (Q1) "fill now" and unnamed NOT: conditions satisfy C-20 but not C-23 -- named violation categories required; (Q2) prose derivation satisfies C-21; field:value citation syntax satisfies C-24 -- one lookup, no re-reading; (Q3) PRE-FLIGHT (V-03, V-05) satisfies C-25; DETERMINATION SEAL (V-04) satisfies C-22 only -- gate-before-failure vs gate-at-failure distinction confirmed by independent variations.

C-23, C-24, C-25 derived from R5 V-05 excellence signals: (1) triple enforcement layering -- per-field named-violation gates + phase-exit attestations + structural gate items, no constraint stated once; (2) INVENTORY SCHEMA as shared field:value vocabulary propagating from SURVEYOR to RECORD DIAGNOSIS to frontmatter boolean tracking; (3) PRE-FLIGHT expanded to structural audit phase before JUDGE -- verifies C-21 compliance as pre-condition before commitment sentence is reachable.

### Round 6 calibration (under v6 rubric)

All 5 Round 6 variations were Golden (117.5-132.5). V-05 achieved maximum 132.5 / 132.5. New criteria predicted from V-05 excellence signals (3/3):

| Score (v6) | Score (v7) | Variation | R6 new criteria passed | v7 delta |
|------------|------------|-----------|------------------------|----------|
| 132.5 | 140.0 | V-05 | C-23, C-24, C-25 | +7.5 (C-26, C-27, C-28 all pass) |
| 122.5 | 122.5 | V-03 | C-22, C-25 (C-23/C-24 fail) | 0 (PRE-FLIGHT three-phase is C-27 predecessor; C-28 entry gate absent) |
| 122.5 | 122.5 | V-04 | C-20, C-22, C-23, C-24 (C-25 fail) | 0 (PHASE-ADVANCE VIOLATION present; PRE-FLIGHT absent; C-26/C-27/C-28 all fail) |
| 120.0 | 120.0 | V-01 | C-20, C-22, C-23 (C-24/C-25 fail) | 0 (inline violation naming; no registry block; C-26/C-27/C-28 all fail) |
| 117.5 | 117.5 | V-02 | C-21, C-24 (C-23/C-25 fail) | 0 (single-site arrow-chain; no PRE-FLIGHT; C-26/C-27/C-28 all fail) |

R6 Q-answer confirmations: (Q1) C-23 inline embedding confirmed to fire on V-01 -- named violation type within the NOT: sentence is sufficient; standalone registry before FRONTMATTER is C-26 territory; (Q2) C-24 fires without PRE-FLIGHT audit -- arrow-chain creation in RECORD DIAGNOSIS alone satisfies C-24; V-03 SCHEMA-CITATION AUDIT as PRE-FLIGHT Phase B is the direct C-27 predecessor; (Q3) three-phase PRE-FLIGHT satisfies C-25; PHASE-ADVANCE VIOLATION at PRE-FLIGHT entry satisfies C-28; SCHEMA-CITATION AUDIT as Phase B + JUDGE confidence application is C-27 mechanism -- each confirmed by independent variation.

C-26, C-27, C-28 derived from R6 V-05 excellence signals: (1) violation taxonomy registry block before FRONTMATTER -- all four violation types indexed before any fill window is encountered; taxonomy visible before first constraint rather than discoverable on demand at each constraint; (2) arrow-chain three-site chain of custody -- RECORD DIAGNOSIS creates chain, PRE-FLIGHT Phase B audits it, JUDGE confidence paragraph applies it -- three named verification sites with full traceability; (3) PRE-FLIGHT entry gate naming PHASE-ADVANCE VIOLATION before phase steps begin -- forecloses looking-complete-but-incomplete bypass before any step can be skipped, not as post-hoc annotation.
