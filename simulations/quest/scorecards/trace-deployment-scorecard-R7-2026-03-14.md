---

# Scorecard: trace-deployment (R7)

**Rubric**: v6 | **22 criteria** | **160 pts** | **5/5 predictions matched**

---

## Research Questions — Answered

**Q1: Does C-20 hold with fresh domain vocabulary?**
Yes. V-01 uses catalog-sync/service-activation disqualifiers (vs R6's error-rates/schema-migration). Same 135/160. C-20 is phrasing-independent — any domain-vocabulary wrong-pattern naming without inertia source satisfies it.

**Q2: Are C-21 and C-22 independently isolable?**
Yes. V-02 (colloquial + inline prose) = C-21 PASS / C-22 FAIL at 135. V-03 (formal + bare) = C-22 PASS / C-21 FAIL at 135. Single-axis control confirmed.

**Q3: Does colloquial + bare reach 140?**
Yes. V-04 (colloquial + bare) = C-21+C-22 simultaneously = **140/160** — the first variation to exceed 130 under any rubric version. Template path now leads prose path: 140 vs 135.

**Bonus (V-05):** Role-block inertia narrative does not contaminate C-20. C-20 evaluates disqualifier content only; role persona framing is orthogonal. V-05 scores 135/160 identical to V-01.

---

## Cross-Variation Summary

| Criterion | V-01 | V-02 | V-03 | **V-04** | V-05 |
|-----------|------|------|------|----------|------|
| C-01–C-08 | all PASS | all PASS | all PASS | all PASS | all PASS |
| C-09–C-13 | all PASS | all PASS | all PASS | all PASS | all PASS |
| C-14 | FAIL | PASS | PASS | **PASS** | FAIL |
| C-15 | PASS | FAIL | FAIL | FAIL | PASS |
| C-16 | FAIL | PASS | PASS | **PASS** | FAIL |
| C-17 | PASS | FAIL | FAIL | FAIL | PASS |
| C-18 | FAIL | PASS | PASS | **PASS** | FAIL |
| C-19 | PASS | FAIL | FAIL | FAIL | PASS |
| C-20 | PASS | FAIL | FAIL | FAIL | **PASS** |
| C-21 | FAIL | PASS | FAIL | **PASS** | FAIL |
| C-22 | FAIL | FAIL | PASS | **PASS** | FAIL |
| **Score** | **135** | **135** | **135** | **140** | **135** |

---

## Excellence Signals

V-04 distinguishing axis: colloquial register AND bare labels simultaneously — the only combination that satisfies both C-21 and C-22, adding 10 pts to the template-path base of 130.

**New patterns:**

- `role-block-inertia-orthogonal-to-c20-disqualifier-source` — An inertia persona in the role block does not contaminate C-20. C-20 evaluates the disqualifier content, not the role framing. Role persona and disqualifier source are fully independent dimensions.

- `c21-c22-orthogonal-template-path-ceiling-140` — C-21 (register) and C-22 (field density) are independent template-path axes; joint satisfaction is additive. The absolute ceiling is 140/160 when all 10 template-path aspirational criteria pass simultaneously.

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["role-block-inertia-orthogonal-to-c20-disqualifier-source", "c21-c22-orthogonal-template-path-ceiling-140"]}
```
2 PASS (formal + bare), C-21 FAIL
        -> Bare labels pass C-22; register independently controls C-21
  V-04: C-21+C-22 simultaneous PASS (colloquial + bare) -> 140/160 ceiling confirmed
        -> C-21 and C-22 are orthogonal template-path axes; joint satisfaction adds 5 pts to either alone
  V-05: C-20 PASS with inertia in role block -> role-persona inertia orthogonal to disqualifier source
        -> C-20 evaluates disqualifier content; role framing is not load-bearing for C-20

Hard ceiling architecture:
  Template:  C-14 requires structural apparatus -> C-15 cannot pass -> C-19/C-20 blocked
             C-21+C-22 require template path -> prose path cannot reach 140
  Prose:     C-15 requires absence of apparatus -> C-14/C-16/C-18 cannot pass -> C-21/C-22 blocked
             C-20 requires no inertia in disqualifiers -> inertia-prose path ceiling = 130
  Absolute ceiling: 140/160 (template path, colloquial, bare labels)
```

---

### Cross-Variation Criterion Summary (R7)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| **C-14** | FAIL | **PASS** | **PASS** | **PASS** | FAIL |
| **C-15** | **PASS** | FAIL | FAIL | FAIL | **PASS** |
| **C-16** | FAIL | **PASS** | **PASS** | **PASS** | FAIL |
| **C-17** | **PASS** | FAIL | FAIL | FAIL | **PASS** |
| **C-18** | FAIL | **PASS** | **PASS** | **PASS** | FAIL |
| **C-19** | **PASS** | FAIL | FAIL | FAIL | **PASS** |
| **C-20** | **PASS** | FAIL | FAIL | FAIL | **PASS** |
| **C-21** | FAIL | **PASS** | FAIL | **PASS** | FAIL |
| **C-22** | FAIL | FAIL | **PASS** | **PASS** | FAIL |
| **Score** | **135** | **135** | **135** | **140** | **135** |

Prose path (C-15+C-17+C-19+C-20): V-01, V-05.
Template path (C-14+C-16+C-18): all three template variations.
  V-02 adds C-21 (colloquial); V-03 adds C-22 (bare); V-04 adds both.
V-01 vs V-05: same score — role-block inertia is not load-bearing for C-20; disqualifier content
  is the only dimension that matters.
V-02 vs V-03: same score — C-21/C-22 are independent axes, each isolable.
V-04 vs V-02/V-03: +5 pts — joint C-21+C-22 satisfaction confirms the 140/160 ceiling.

---

### V-01: C-20 Fresh Vocabulary Confirmation (Prose Path, No Inertia)

**Axis**: Prose path, no inertia framing, fresh catalog-sync/service-activation domain vocabulary
in disqualifiers — distinct from R6-V-01 error-rates/schema-migration vocabulary.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "List at least 3 checks; for each, name what is verified and what failure looks like — 'catalog sync confirmed' does not name which catalog artifact or state is being verified and does not pass." >=3, dual elements, fresh-vocabulary disqualifier. |
| C-02 | **PASS** | "Number at least 4 deployment steps with the action and its precondition." Count >=4, structure explicit. |
| C-03 | **PASS** | "List at least 2 post-deploy validation actions with the probe name, expected result, and failure indicator — 'service activation confirmed' does not name a probe or a pass threshold and does not pass." Three elements, fresh-vocabulary disqualifier. |
| C-04 | **PASS** | "Name the specific metric threshold or probe result that triggers rollback — 'catalog sync failed' does not name an observable signal and does not pass; list rollback steps; state the observable outcome confirming rollback succeeded — 'service deactivated' does not name an observable catalog state and does not pass." All four elements, two fresh-vocabulary disqualifiers. |
| C-05 | **PASS** | Each of four phases ends with gap directive: "identify what is missing or weak, state what should be added, and rate severity." Four gap directives, one per phase. |
| C-06 | **PASS** | "'pipeline drain before service restart' passes; 'drain then restart' does not name why drain must precede restart and does not pass." Explicit ordering dependency with reason required. |
| C-07 | **PASS** | "Your vocabulary: catalog sync, service activation, feature gate status, catalog manifest, tenant-state lock, health probe, activation threshold, rollback trigger, canary gate, pipeline drain, environment parity." 11 Commerce/Operations terms in role description. |
| C-08 | **PASS** | "state what should be added", "state the fix", "state what should replace it", "state the fix" per gap phase. |
| C-09 | **PASS** | "Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank — rank all four gaps by deployment blast radius; a severity assignment that does not compare this gap against the other three does not satisfy the ranking requirement." Cross-comparison mandate explicit. |
| C-10 | **PASS** | "name one CI gate or pre-deploy script that could enforce a check currently done manually" (pre-deploy) + "name one canary gate or activation probe that could replace a currently manual check" (post-deploy). Two hook locations via prose. |
| C-11 | **PASS** | Named vocabulary list in opening role description: "Your vocabulary: catalog sync, service activation, feature gate status..." 11 terms enumerated. Role/persona block placement; no formal ## ROLE header required (R4-V-03 precedent). |
| C-12 | **PASS** | "State the current deployment practice for {topic} and the specific failure mode it carries — this is your baseline; reference it where gap analysis connects directly." Explicit baseline instruction before phases. |
| C-13 | **PASS** | "Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank" — named columns specified in prose. C-13 achieved via C-15 mechanism. |
| C-14 | **FAIL** | No structural skeleton table before phases. No pre-printed blank rows. No do-not-pre-fill guard. C-14 requires upfront structural commitment with empty skeleton apparatus. |
| C-15 | **PASS** | No template apparatus. Three requirements: (a) output elements named (>=3 checks with failure, >=4 steps with precondition, >=2 validations with probe/expected/indicator, rollback trigger/steps/outcome, gap table with named columns); (b) cross-gap comparison mandated; (c) contextual disqualifiers per phase — fresh catalog-sync/service-activation vocabulary throughout. All three requirements met. |
| C-16 | **FAIL** | No Check-NN, Step-NN, Validation-NN, or Hook-NN template fields. C-16 requires template field scaffolding. |
| C-17 | **PASS** | C-15 PASS. Each phase instruction is exactly one paragraph. Single-paragraph-per-phase density confirmed; all three C-15 requirements present at this density without verbosity expansion. |
| C-18 | **FAIL** | C-14 FAIL -> C-18 cannot pass. |
| C-19 | **PASS** | C-15 PASS. Disqualifying examples expressed as contextual failure-mode statements in domain terms: "'catalog sync confirmed' does not name which catalog artifact or state" (catalog-sync vocabulary), "'drain then restart' does not name why drain must precede restart" (pipeline vocabulary), "'service activation confirmed' does not name a probe or a pass threshold" (activation vocabulary), "'catalog sync failed' does not name an observable signal" (rollback vocabulary). All four phases carry fresh-vocabulary disqualifiers. |
| C-20 | **PASS** | C-19 PASS. Zero inertia narrative — no incident, postmortem, or "we learned" framing anywhere in the prompt. Disqualifiers grounded entirely in catalog-sync/service-activation domain vocabulary. Confirms: C-20 is phrasing-independent; the R6-V-01 error-rates/schema-migration vocabulary and the R7-V-01 catalog-sync/service-activation vocabulary are equivalent generators. Any domain-vocabulary wrong-pattern naming without inertia source satisfies C-20. |
| C-21 | **FAIL** | Prose path — no template field scaffolding. C-21 requires C-14/C-16/C-18 to pass. |
| C-22 | **FAIL** | Prose path — no template field scaffolding. C-22 requires C-14/C-16/C-18 to pass. |

**Score: 135 / 160** | All essential PASS | **Golden: YES**

*Key finding: C-20 phrasing-independence confirmed. The criterion is structural — domain vocabulary
without inertia source — not lexical. Catalog-sync/service-activation disqualifiers satisfy C-20
with identical force to error-rates/schema-migration disqualifiers from R6-V-01. Vocabulary
selection within the domain is free.*

---

### V-02: Colloquial Register + Inline Prose (C-21 Isolation, Template Path)

**Axis**: Template-path architecture (field scaffolding + skeleton + vocabulary in role block +
gate-free) with colloquial section headers and field labels AND inline prose instructions within
fields. Isolates C-21 (colloquial register) without triggering C-22 (bare labels).

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "check-1: What are you verifying? \| Passes when: [state an observable condition, not 'environment is ready'] \| Fails when: [specific symptom, not 'something is wrong']" fields x3. >=3 count, dual pass/fail elements per field with inline guards. |
| C-02 | **PASS** | "step-1: Action: [what you do] \| Precondition: [what must be true first] \| Output: [observable result]" fields x4. Count >=4, structure explicit. |
| C-03 | **PASS** | "validation-1: Probe: [specific tool or check] \| Expected: [exact pass state] \| Failure indicator: [observable signal, not 'looks wrong']" fields x2. Three elements, inline guard per field. |
| C-04 | **PASS** | "trigger: [threshold or signal — 'deployment failed' does not name an observable metric] \| rollback-1/2 fields \| confirmation: [observable state — not 'done' or 'reverted']". All four elements with inline guards. |
| C-05 | **PASS** | "What is missing or weak in this phase? \| Fix: [specific change, not 'add tests'] \| Severity: [rank after comparing to other gaps]" gap block per phase x4. |
| C-06 | **PASS** | "note any hard ordering: step X must finish before step Y because [explicit reason]" inline instruction within step field. Ordering dependency with reason required. |
| C-07 | **PASS** | "Domain terms you'll use: catalog sync, order pipeline drain, inventory lock, tenant provisioning, feature flag gate, environment parity check, health probe, rollback threshold, canary assertion, circuit breaker, deployment manifest." 11 terms in role/vocabulary section. |
| C-08 | **PASS** | "Fix: [specific change, not 'add tests']" in each gap block. Label-only barred by inline guard. |
| C-09 | **PASS** | Front-loaded gap log skeleton with blank rows + "When you rank, compare each gap against the other three — do not justify severity in isolation." Cross-comparison mandate upfront. |
| C-10 | **PASS** | "Something that could be CI-gated here: [what gate / enforces what / currently manual because]" per phase x3. Three automation hook sections in colloquial register. |
| C-11 | **PASS** | Named vocabulary list in opening role section. Role/persona block placement confirmed; colloquial register of role section does not change placement requirement. |
| C-12 | **PASS** | "Current practice: [what your team does for {topic} deployments] \| Known failure mode: [what goes wrong under current practice]" named fields in role section + reference instruction. |
| C-13 | **PASS** | Front-loaded gap log skeleton with Rank/Phase/Gap/Severity/Why-this-rank columns. Skeleton table satisfies C-13 before tracing begins. |
| C-14 | **PASS** | Gap log skeleton placed before first phase. Guard: "leave blank, fill in only after tracing all four phases." Return instruction: "compare each gap against the other three — do not justify severity in isolation." All three C-14 requirements met in colloquial register. Colloquial wording does not change structural function. |
| C-15 | **FAIL** | Template apparatus present: structured field labels ("check-1:", "step-1:", "validation-1:", "trigger:", "confirmation:", "gap-1:", "fix:", "severity:"), gap sub-fields, hook sub-fields. Inline prose within fields constitutes instruction-carrying template scaffolding. Prose-alone path blocked regardless of field register. |
| C-16 | **PASS** | No GATE enforcement text ("GATE N: Do not proceed until..."). Hook fields per phase present in colloquial form. Field count floors met: 3 check fields, 4 step fields, 2 validation fields, trigger + rollback x2 + confirmation fields, gap block per phase. Gate-free confirmed. |
| C-17 | **FAIL** | C-15 FAIL -> C-17 cannot pass. |
| C-18 | **PASS** | C-14 PASS + C-16 PASS. Colloquial "leave blank, fill in only after tracing all four phases" is not GATE enforcement text — it is a skeleton commitment guard. Colloquial register does not disqualify C-16; no "GATE N: Do not proceed" blocks present. |
| C-19 | **FAIL** | C-15 FAIL -> C-19 cannot pass. |
| C-20 | **FAIL** | C-19 FAIL -> C-20 cannot pass. |
| C-21 | **PASS** | C-14 PASS + C-16 PASS + C-18 PASS. Section headers are colloquial: "Before you touch anything:", "Now roll it out:", "Did it work?", "If you need to back out:". Field labels are colloquial: "check-1:", "step-1:", "validation-1:", "trigger:", "confirmation:". Structural requirements satisfied with colloquial register throughout. Confirms C-21 passes independently of C-22 — inline field prose does not disqualify C-21. |
| C-22 | **FAIL** | Inline prose within fields present: "What are you verifying?", "state an observable condition, not 'environment is ready'", "what must be true first", "not 'done' or 'reverted'" within field definitions. C-22 requires bare identifiers only — no embedded instruction prose inside any field. |

**Score: 135 / 160** | All essential PASS | **Golden: YES**

*C-21 isolation confirmed: colloquial register satisfies C-21 regardless of field instruction density.
C-22 is the independent axis — it evaluates field content, not header vocabulary. A variation can
be maximally colloquial in all structural labels while carrying rich inline prose and still achieve
C-21. The register and density axes do not interact.*

---

### V-03: Formal Labels + Bare Field Labels (C-22 Isolation, Template Path)

**Axis**: Template-path architecture with formal section headers ("## PHASE N — PRE-DEPLOY") and
formal field labels ("Check-01:", "Step-01:") AND bare field labels — no inline prose instructions
within fields. Isolates C-22 (bare labels) without triggering C-21 (colloquial register).

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "Check-01: [artifact verified] \| Pass: [condition] \| Failure: [symptom]" fields x3. >=3 count, dual elements embedded in field structure as bare slot labels. |
| C-02 | **PASS** | "Step-01/02/03/04: [action] \| Precondition: [dependency] \| Output: [result]" fields x4. Count >=4. |
| C-03 | **PASS** | "Validation-01/02: [probe] \| Expected: [result] \| Failure: [symptom]" fields x2. Three elements each. |
| C-04 | **PASS** | "Trigger: [metric threshold or probe result — not 'if deployment fails'] \| Rollback-01/02 fields \| Verification: [observable state — not 'complete']". All four elements; guards are within field slot labels as bare disqualifier hints, not prose instructions. |
| C-05 | **PASS** | "Gap-01: Missing \| Fix \| Severity" block per phase x4. |
| C-06 | **PASS** | "Ordering-dep: [Step-X must precede Step-Y]: [explicit reason]" field. Step references and explicit reason required by bare slot structure. |
| C-07 | **PASS** | "Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning, feature flag gate, environment parity check, health probe, rollback threshold, canary assertion, circuit breaker, deployment manifest." 11 terms in ## ROLE block. |
| C-08 | **PASS** | "Fix: [specific change]" slot per gap block. Bare slot label implies concrete action. |
| C-09 | **PASS** | ## GAP PLAN table skeleton with Rank/Phase/Gap/Severity/Why-this-rank columns + "Rank by deployment blast radius. In 'Why this rank' compare this gap against the other three." |
| C-10 | **PASS** | "Hook-01: [CI gate or pre-deploy script] \| Enforces: [check] \| Currently: [manual or absent]" fields in Phase 1, Phase 2; "Hook-01: [canary assertion or health probe] \| Replaces: [manual check] \| Currently: [absent]" in Phase 3. Three hook fields, all bare. |
| C-11 | **PASS** | Named vocabulary list in ## ROLE block: 11 terms enumerated. Formal ## ROLE header does not affect criterion; role-block placement is load-bearing. |
| C-12 | **PASS** | "Current practice: [...] \| Known failure mode: [...]" bare fields in ## ROLE block + return reference instruction: "reference baseline in Why-this-rank comparisons." Named baseline fields before Phase 1. |
| C-13 | **PASS** | ## GAP PLAN skeleton table front-loaded with required columns. |
| C-14 | **PASS** | ## GAP PLAN before ## PHASE 1. Guard: "Leave all rows blank — fill only after tracing all four phases." Return instruction: "In 'Why this rank' compare this gap against the other three." All three C-14 requirements met. |
| C-15 | **FAIL** | Template apparatus present: ## ROLE, ## GAP PLAN, ## PHASE 1-4 headers; Check-NN, Step-NN, Validation-NN, Hook-NN, Rollback-NN, Gap-NN fields. Structural apparatus present regardless of instruction density within fields. |
| C-16 | **PASS** | No GATE enforcement text. Hook fields in Phases 1, 2, 3. Field count floors met. Gate-free at bare-label density. |
| C-17 | **FAIL** | C-15 FAIL -> C-17 cannot pass. |
| C-18 | **PASS** | C-14 PASS + C-16 PASS. "Leave all rows blank" is skeleton commitment guard, not GATE enforcement text. Bare-label template satisfies C-14 and C-16 simultaneously. |
| C-19 | **FAIL** | C-15 FAIL -> C-19 cannot pass. |
| C-20 | **FAIL** | C-19 FAIL -> C-20 cannot pass. |
| C-21 | **FAIL** | Section headers are formal: "## PHASE 1 — PRE-DEPLOY", "## PHASE 2 — DEPLOY SEQUENCE", "## PHASE 3 — POST-DEPLOY VALIDATION", "## PHASE 4 — ROLLBACK". Field labels are formal: "Check-01:", "Step-01:", "Validation-01:", "Trigger:", "Rollback-01:", "Verification:". C-21 requires colloquial register; formal labels do not satisfy the distinguishing condition. |
| C-22 | **PASS** | Field labels are bare identifiers only: "Check-01: [artifact verified] \| Pass: [condition] \| Failure: [symptom]" — slot names with placeholder brackets, no embedded instruction prose. No inline instructions ("What are you verifying?", "not 'environment ready'", etc.) appear inside any field. Skeleton, return instruction, vocabulary list in role block, baseline fields, and hook fields constitute the complete apparatus. Bare-label structure is confirmed. |

**Score: 135 / 160** | All essential PASS | **Golden: YES**

*C-22 isolation confirmed: bare field labels satisfy C-22 regardless of header formality. C-21 is
the independent axis — it evaluates section and field label register, not field content density.
A variation can carry formal ## PHASE headers and Check-NN labels while having zero inline prose
and still achieve C-22. The two axes control distinct dimensions of template architecture.*

---

### V-04: Colloquial Register + Bare Labels (C-21 + C-22 Simultaneously)

**Axis**: Template-path architecture with colloquial section headers AND bare field labels — the
only combination not previously tested. First variation predicted to reach 140/160.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "check-1: [what] \| passes-when: [condition] \| fails-when: [symptom]" fields x3. Colloquial labels, bare slots, >=3 count, dual elements. |
| C-02 | **PASS** | "step-1/2/3/4: [action] \| before: [precondition] \| output: [result]" fields x4. Colloquial bare structure. |
| C-03 | **PASS** | "validation-1/2: [probe] \| expected: [result] \| failure: [symptom]" fields x2. Three bare slot elements each. |
| C-04 | **PASS** | "trigger: [metric threshold or signal] \| rollback-1/2: [step] \| confirmed-when: [observable state]" fields. All four elements as bare slots. |
| C-05 | **PASS** | "pre-gap: missing \| fix \| severity" per phase x4. Bare three-slot gap blocks. |
| C-06 | **PASS** | "ordering-dep: [step-X must precede step-Y]: [reason]" bare field. |
| C-07 | **PASS** | "Vocabulary: catalog sync, order pipeline drain, inventory lock, tenant provisioning, feature flag gate, environment parity check, health probe, rollback threshold, canary assertion, circuit breaker, deployment manifest." 11 terms in role section. |
| C-08 | **PASS** | "fix: [specific change]" bare slot per gap block. Slot label implies concrete action. |
| C-09 | **PASS** | "gap-log — leave blank, rank after all phases — compare each gap to the others" skeleton with colloquial table columns (rank/phase/gap/severity/why-this-rank). Cross-comparison mandate in colloquial return instruction. |
| C-10 | **PASS** | "ci-hook: [gate] \| enforces: [check] \| currently: [manual or absent]" per applicable phase; "canary-hook: [canary or probe] \| replaces: [manual check] \| currently: [absent]" in validation phase. Three automation hook fields, all bare. |
| C-11 | **PASS** | Named vocabulary list in opening role section: 11 terms. Colloquial role framing ("You're an Operations engineer who ships Commerce features") does not affect role-block placement requirement. |
| C-12 | **PASS** | "current-practice: [...] \| known-failure: [...]" bare fields in role section before phases. Colloquial label names ("current-practice", "known-failure") satisfy the named-fields requirement. |
| C-13 | **PASS** | "gap-log" skeleton table front-loaded with five column labels. Colloquial column names (rank/phase/gap/severity/why-this-rank) satisfy the C-13 column requirement — column semantics match, not column label formality. |
| C-14 | **PASS** | "gap-log" skeleton before first phase. Guard: "leave blank, rank after all phases." Return: "compare each gap to the others." All three C-14 requirements satisfied in colloquial bare form. The guard "leave blank" is functionally equivalent to "Leave all rows blank — do not pre-fill" — brevity does not disqualify when the do-not-pre-fill intent is unambiguous. |
| C-15 | **FAIL** | Template apparatus present: colloquial bare labels ("check-1:", "step-1:", "validation-1:", "trigger:", "confirmed-when:", "gap-log" table) constitute structural template field scaffolding regardless of register or instruction density. |
| C-16 | **PASS** | No GATE enforcement text. Hook fields (ci-hook, auto-hook, canary-hook) per applicable phase. Field count floors met with colloquial bare labels: 3 check fields, 4 step fields, 2 validation fields, trigger + rollback x2 + confirmed-when, gap block per phase. Gate-free at minimum bare density. |
| C-17 | **FAIL** | C-15 FAIL -> C-17 cannot pass. |
| C-18 | **PASS** | C-14 PASS + C-16 PASS. "leave blank, rank after all phases" is skeleton commitment guard in colloquial form, not GATE enforcement text. Colloquial bare template satisfies both C-14 and C-16. |
| C-19 | **FAIL** | C-15 FAIL -> C-19 cannot pass. |
| C-20 | **FAIL** | C-19 FAIL -> C-20 cannot pass. |
| C-21 | **PASS** | C-14 PASS + C-16 PASS + C-18 PASS. Section headers are colloquial: "before you touch anything:", "roll it out:", "check it worked:", "back out:". Field labels are colloquial: "check-1:", "step-1:", "validation-1:", "trigger:", "confirmed-when:", "ci-hook:", "canary-hook:". C-21 passes simultaneously with C-22 — confirming the axes are orthogonal. |
| C-22 | **PASS** | Field labels are bare identifiers only: "check-1: [what] \| passes-when: [condition] \| fails-when: [symptom]" — colloquial slot names with placeholder brackets, zero embedded instruction prose. No "What are you verifying?", no "state an observable condition, not 'environment is ready'", no inline guards within fields. C-22 passes simultaneously with C-21 — confirming the axes are orthogonal. |

**Score: 140 / 160** | All essential PASS | **Golden: YES**

*First variation to exceed 130 under any rubric version. Template-path ceiling of 140/160 confirmed.
The joint C-21+C-22 pass adds 5 pts to either variation that satisfies only one axis (V-02 or V-03).
Colloquial register and bare field labels are fully orthogonal template-path properties — neither
disqualifies nor depends on the other. V-04 is the minimum-viable ceiling architecture for the
template path: further reduction would break a field count floor or remove a structural property.*

---

### V-05: Prose Path + Inertia in Role Block (C-20 Orthogonality Test)

**Axis**: Prose path (C-15 architecture), inertia narrative framing in the role persona block
(not as disqualifier source), domain-contextual disqualifiers drawn from deployment vocabulary
without incident reference. Tests whether role-block inertia contaminates C-20.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "List at least 3 checks; for each, name what is verified and what failure looks like — 'environment parity confirmed' does not name which system state is being verified and does not pass." >=3, dual elements, domain-contextual disqualifier. |
| C-02 | **PASS** | "Number at least 4 deployment steps with the action and its precondition." Count >=4, structure explicit. |
| C-03 | **PASS** | "List at least 2 post-deploy validation actions with the probe name, expected result, and failure indicator — 'health probe passing' does not name a specific threshold or expected response and does not pass." Three elements, domain-contextual disqualifier. |
| C-04 | **PASS** | "Name the specific metric threshold or probe result that triggers rollback — 'rollback if needed' does not name an observable signal and does not pass; list rollback steps; state the observable outcome confirming rollback succeeded — 'catalog restored' does not identify a specific catalog state observable and does not pass." All four elements, two disqualifiers. |
| C-05 | **PASS** | Gap directives in all four phases, one per phase. |
| C-06 | **PASS** | "'pipeline drain before service restart' passes; 'pipeline drain, then restart' does not name why drain must precede restart and does not pass." |
| C-07 | **PASS** | Named vocabulary list in role paragraph: 11 Commerce/Operations terms. |
| C-08 | **PASS** | "state what should be added", "state the fix", "state what should replace it", "state the fix" per gap phase. |
| C-09 | **PASS** | "Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank — rank all four gaps by deployment blast radius; a severity assignment that does not compare this gap against the other three does not satisfy the ranking requirement." |
| C-10 | **PASS** | "name one CI gate or pre-deploy script that could enforce a check currently done manually" + "name one canary assertion or activation probe that could replace a currently manual check." |
| C-11 | **PASS** | Named vocabulary list in role paragraph. Inertia persona framing does not change role-block placement requirement. |
| C-12 | **PASS** | "State the current deployment practice for {topic} and the specific failure mode it carries — this is your baseline; reference it where gap analysis connects directly." Explicit baseline instruction. Inertia narrative also seeds failure-mode context (parallel to R6-V-02 finding). |
| C-13 | **PASS** | "Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank" — named columns in prose. |
| C-14 | **FAIL** | No structural skeleton before phases. No pre-printed blank rows. No do-not-pre-fill guard. |
| C-15 | **PASS** | No template apparatus. Three requirements met: (a) output elements named (counts per phase, named columns); (b) cross-gap comparison mandated; (c) contextual disqualifiers per phase in domain deployment vocabulary — "'environment parity confirmed' does not name which system state", "'health probe passing' does not name a specific threshold", "'rollback if needed' does not name an observable signal", "'catalog restored' does not identify a specific catalog state observable." All disqualifiers derive from deployment domain knowledge. |
| C-16 | **FAIL** | No template field scaffolding. |
| C-17 | **PASS** | C-15 PASS. Single-paragraph-per-phase density confirmed. All three C-15 requirements present at compressed density. |
| C-18 | **FAIL** | C-14 FAIL -> C-18 cannot pass. |
| C-19 | **PASS** | C-15 PASS. Disqualifying examples are contextual failure-mode statements in domain vocabulary. Four phases each carry a domain-specific wrong-pattern disqualifier. Inertia framing in role block does not contaminate disqualifier source — the disqualifiers themselves contain zero incident, postmortem, or "we learned" language. |
| C-20 | **PASS** | C-19 PASS. **Key finding**: disqualifier content is domain-contextual without any incident reference despite the role block containing inertia narrative ("your team has been on call through incidents where the postmortem read..."). C-20 evaluates the disqualifying example content, not the role persona framing. The inertia backstory in the role block and the disqualifier source are independent dimensions. Role-level inertia does not contaminate C-20 when the actual disqualifiers are grounded in domain vocabulary alone. Confirms: disqualifier source is the only load-bearing dimension for C-20; role framing is orthogonal. |
| C-21 | **FAIL** | Prose path — no template field scaffolding. C-21 requires C-14/C-16/C-18 to pass. |
| C-22 | **FAIL** | Prose path — no template field scaffolding. C-22 requires C-14/C-16/C-18 to pass. |

**Score: 135 / 160** | All essential PASS | **Golden: YES**

*Role-block inertia orthogonality confirmed: the C-20 boundary is the disqualifier text content,
not the role persona framing. A prompt whose role block is grounded in incident experience ("your
team was on call through incidents where...") can still satisfy C-20 if the actual disqualifying
examples name specific wrong patterns in domain vocabulary without incident reference. The inertia
persona primes domain expertise as a frame; it does not force inertia framing into the disqualifiers.
V-05 score matches V-01 (135/160): zero effect of role-block inertia on any scored criterion.*

---

## Excellence Signals

**Top variation**: V-04 at 140/160 — first to exceed 130 under any rubric version.

The distinguishing property: V-04 is the only variation satisfying all 10 template-path aspirational
criteria simultaneously. The two new criteria that lift V-04 above V-02 and V-03:

1. **C-21 (colloquial register)**: Colloquial labels ("before you touch anything:", "check-1:")
   are not a stylistic preference — they are the distinguishing condition for C-21. Any fully-spec-
   compliant template with formal headers passes C-14/C-16/C-18 at 130; switching to colloquial
   adds 5 pts for free with zero structural cost.

2. **C-22 (bare field labels)**: Bare slot labels ("check-1: [what] | passes-when: [condition]")
   with no inline instruction prose are not impoverished — they are structurally sufficient for all
   field-count floors. Prose within fields is optional at the ceiling; removing it adds 5 pts with
   zero structural cost.

**New patterns from R7:**

`role-block-inertia-orthogonal-to-c20-disqualifier-source` — V-05 confirms: an inertia persona in
the role block does not contaminate C-20. C-20 evaluates the disqualifier content — whether it
names a wrong pattern in domain deployment vocabulary without incident reference. The role persona
framing and the disqualifier source are fully independent dimensions. An engineer persona that
references prior incidents in its framing can still produce domain-vocabulary disqualifiers that
satisfy C-20. Role framing is not the disqualifier source.

`c21-c22-orthogonal-template-path-ceiling-140` — C-21 (register) and C-22 (field density) are
independent template-path axes. V-02 confirms C-21 passes without C-22; V-03 confirms C-22 passes
without C-21; V-04 confirms joint satisfaction is additive (+5 each). The template-path absolute
ceiling is 140/160 when all 10 aspirational template-path criteria pass simultaneously: colloquial +
bare unlocks the ceiling that colloquial-alone or bare-alone cannot reach.

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["role-block-inertia-orthogonal-to-c20-disqualifier-source", "c21-c22-orthogonal-template-path-ceiling-140"]}
```
