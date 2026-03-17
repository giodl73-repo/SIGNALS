## /quest:score — validate-inertia — Round 3 Complete

| V | Score | All Essential | Key |
|---|-------|---------------|-----|
| V-01 R3 upgraded baseline | **100** | YES | R3 floor: four-phase + explicit C-13/C-14/C-15 labels |
| V-02 Type-resolution contract | **100** | YES | Strongest C-14: Phase 2 contract binds Phase 4 |
| V-03 Lost TAM standalone | **100** | YES | Strongest C-15: Phase 5 isolation + anchoring terms |
| V-04 Inertia type gate | **100** | YES | Strongest C-13: "Do not proceed" + "Gate passed." |
| V-05 Compressed R3 | **99** | YES | C-13 PARTIAL: parenthetical weaker than phase header |

---

**Four-way tie at 100.** R3's question — can C-13/C-14/C-15 be made structurally reliable? — is answered yes for phase-based formats. The compressed format (V-05) loses 1 pt on C-13: numbered sections with parenthetical enforcement don't fully satisfy "dedicated pre-persona phase."

**Three new patterns extracted for R4:**

1. **Contract-write pattern** (V-02): Phase 2 writes `Required mitigation form:` before any persona work. Phase 4 fulfills it. The model can't drift to generic mitigation without contradicting its own prior output.

2. **Phase isolation for unconditional fields** (V-03): Any field that must appear regardless of evidence confidence gets its own dedicated phase + anchoring vocabulary. Proximity to surrounding if/then language in synthesis causes conditional drift; phase boundaries prevent it.

3. **Procedural gate + self-affirmation** (V-04): `"Do not proceed until you have classified inertia type."` → `"Gate passed. Proceeding."` The self-affirmation token appears in output as a confirmed prerequisite, not a passively-read header.

**R4 framing shift:** The rubric floor is now high enough that four variants hit 100. R4's design question is no longer "what criteria are missing" — it's "which structural techniques make existing criteria most reliable under adversarial output conditions (long outputs, compressed formats, kill-barrier revisions)."

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Contract-write pattern: Phase 2 writes 'Required mitigation form: [if Structural: specific product change required] [if Behavioral: specific launch sequence required]' as a binding contract before persona analysis; Phase 4 must fulfill it -- model reads its own prior output rather than re-deriving the type condition at synthesis time, preventing generic drift structurally rather than by instruction", "Phase isolation for required-unconditional output fields: extract any field that must appear regardless of evidence confidence into its own dedicated phase with its own header, anchoring vocabulary, and 'required regardless of evidence confidence' instruction -- proximity to surrounding if/then language in shared synthesis sections causes conditional drift that phase-boundary isolation prevents", "Procedural gate + self-affirmation: frame critical pre-analysis classifications as blocking prerequisites ('Do not proceed to [next phase] until you have [classified X]') and close with a trackable self-affirmation token ('Gate passed. Proceeding.') -- makes the classification appear in model output as a confirmed prerequisite rather than a passively-read section header"]}
```
nd satisfaction assessed | PASS | Phase 3 "Workaround Satisfaction (1-5). Flag 4+ as 'good enough' -- state the specific reason why that score means the workaround feels sufficient for this persona." Score + trigger + explanation required per persona. |
| C-05 | Per-persona inertia score present | PASS | "Inertia Score: Low / Medium / High / Critical. Same scale. Required every row." |
| C-06 | Habit lock-in addressed | PASS | "Habit at Risk: specific behavioral pattern, not a category. 'Runs make check before every commit' not 'relies on existing tooling.'" Exemplar-anchored specificity rule. |
| C-07 | Social proof requirement mapped | PASS | "Social Proof Needed: specific threshold -- names, numbers, evidence type. 'Peer validation' fails." Vague fails explicitly stated. |
| C-08 | Learning curve quantified | PASS | "Learning Curve: time or concept count; comparison anchor if possible ('similar to learning X, which took Y days')." Comparison anchor explicitly requested. |
| C-09 | Overall risk rating with mitigation | PASS | Phase 4: "Overall adoption inertia risk: Low / Medium / High / Critical" + "Mitigation: one specific action targeting the kill barrier. If structural: name product change. If behavioral: name launch sequence or social proof intervention. Do not restate. Do not propose generic onboarding." |
| C-10 | Inertia asymmetry identified | PASS | Phase 4: "Inertia asymmetry: Structural / Behavioral" + "Lost TAM implication: {one sentence -- name permanent lost TAM vs. delayed adoption. Write this regardless of evidence confidence.}" Unconditional framing present. |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | Phase 1 (hypothesis) -> Phase 2 (landscape classification) -> Phase 3 (personas). Sequential gating enforced by section structure. |
| C-12 | Status-quo treated as competitor | PASS | Phase 2 "why did users choose it? What job does it do well for them?" + Phase 3 "Why They Use the Incumbent: the adoption decision -- 'X won this persona because...'" Adoption-decision framing at both levels. |
| C-13 | Inertia landscape classified before persona analysis | PASS | Phase 2 "INERTIA LANDSCAPE CLASSIFICATION": "Before analyzing individual personas, classify the resistance this feature faces. This classification determines the type of solution required -- complete it before proceeding to personas." Classification/Rationale/Implication fields required. Dedicated pre-persona phase with clear gating instruction. |
| C-14 | Type-conditioned mitigation | PASS | Phase 4 Mitigation: "If the kill barrier is structural: name the product change required. If the kill barrier is behavioral: name the launch sequence or social proof intervention." Explicit if/then branching at synthesis time. |
| C-15 | Lost TAM implication stated unconditionally | PASS | Phase 4 "Lost TAM implication: {one sentence -- ... Write this regardless of evidence confidence.}" Required, unconditional, labeled. |

**Score:** 12+12+12+12+12 + 10+10+10 + 2+2+1+1+2+1+1 = **100**
**All essential pass:** YES

---

### V-02 — Type-Resolution Contract

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | Phase 3 "Identify 3-5 personas. For each, state why they chose the incumbent -- role-grounded." Column: "Why They Use the Incumbent: 'X won this persona because their role requires...'" |
| C-02 | Switching cost quantified | PASS | "Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). Vague fails." |
| C-03 | Kill barrier named | PASS | Phase 1 Kill Barrier Hypothesis + Phase 3 "Kill Barrier (confirmed or revised)" with revision-contract reconciliation note. |
| C-04 | Workaround satisfaction assessed | PASS | "Workaround Satisfaction: 1-5. Flag 4+ as 'good enough' -- state the specific reason." |
| C-05 | Per-persona inertia score present | PASS | "Inertia Score: Low / Medium / High / Critical. Same scale. Required every row." |
| C-06 | Habit lock-in addressed | PASS | "Habit at Risk: specific behavior that fires automatically. Not a category." |
| C-07 | Social proof requirement mapped | PASS | "Social Proof Needed: specific threshold -- number, name, or evidence type." |
| C-08 | Learning curve quantified | PASS | "Learning Curve: time or concept count; comparison anchor preferred." |
| C-09 | Overall risk rating with mitigation | PASS | Phase 4: "Mitigation: fulfill the contract you wrote in Phase 2. Use the 'Required mitigation form' you specified. Name the specific product change, launch sequence, or social proof strategy that directly removes the kill barrier. Name the owner." Contract-fulfillment framing: model cannot produce generic mitigation without violating its own Phase 2 output. |
| C-10 | Inertia asymmetry identified | PASS | Phase 4: "Inertia asymmetry: Structural/Behavioral" + "Lost TAM implication: ... Required. Write this regardless of evidence confidence." |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | Phase 1 -> Phase 2 -> Phase 3. "The type determines the solution category. Four phases. Phase 2 writes a contract; Phase 4 fulfills it." |
| C-12 | Status-quo treated as competitor | PASS | Phase 2 "Why users chose it: one sentence -- the adoption story, the job it does well." + Phase 3 "'X won this persona because their role requires...'" |
| C-13 | Inertia landscape classified before persona analysis | PASS | Phase 2 "INERTIA LANDSCAPE CLASSIFICATION": "Answer this question before any persona analysis. Your answer determines what form your Phase 4 mitigation must take." Classification/Rationale/Implication + "Required mitigation form (write this now; Phase 4 must fulfill it):" contract. Most complete C-13 implementation: classification gates not just analysis but mitigation form. |
| C-14 | Type-conditioned mitigation | PASS -- strongest of all variants | Phase 2 writes the contract: "Structural: Phase 4 mitigation must name a specific product change... Generic onboarding, tutorials, and framing do not qualify. / Behavioral: Phase 4 mitigation must name a specific launch sequence, social proof seeding strategy, or framing intervention..." Phase 4 must fulfill, not re-derive. Model reads its own Phase 2 output; cannot drift to generic form. Kill-barrier revision edge case handled: "if revised, state whether Phase 2 classification still holds or also requires update." |
| C-15 | Lost TAM implication stated unconditionally | PASS | Phase 4 "Lost TAM implication: ... Required. Write this regardless of evidence confidence." |

**Score:** 12+12+12+12+12 + 10+10+10 + 2+2+1+1+2+1+1 = **100**
**All essential pass:** YES

---

### V-03 — Lost TAM Standalone Section

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | Phase 3 "Why They Chose the Incumbent: adoption decision -- 'X won this persona because...'" + Phase 2 "Adoption story: 'Users adopted {incumbent} because ___.' (role-grounded, at least one persona)" |
| C-02 | Switching cost quantified | PASS | "Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). Vague fails." |
| C-03 | Kill barrier named | PASS | Phase 1 Kill Barrier Hypothesis + Phase 3 "Kill Barrier (confirmed or revised)." |
| C-04 | Workaround satisfaction assessed | PASS | "Workaround Satisfaction: 1-5. Flag 4+ as 'good enough' and state the specific reason." |
| C-05 | Per-persona inertia score present | PASS | "Inertia Score: Low / Medium / High / Critical. Same scale. Required every row." |
| C-06 | Habit lock-in addressed | PASS | "Habit at Risk: specific behavior that fires before they think about it. Not a category." |
| C-07 | Social proof requirement mapped | PASS | "Social Proof Needed: specific threshold -- number, name type, evidence form." |
| C-08 | Learning curve quantified | PASS | "Learning Curve: time estimate or concept count; comparison anchor if possible." |
| C-09 | Overall risk rating with mitigation | PASS | Phase 4: Overall risk + "Mitigation targeting the kill barrier: If structural: name the specific product change, specific enough to assign to owner. If behavioral: name the specific launch sequence or social proof seeding strategy, name the sequence and owner." |
| C-10 | Inertia asymmetry identified | PASS | Phase 4 "Inertia asymmetry: Structural/Behavioral" + Phase 5 "Lost TAM implication" dedicated section. Both halves of C-10 pass. |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | Phase 1 -> Phase 2 -> Phase 3 -> Phase 4 -> Phase 5. Sequential five-phase structure. |
| C-12 | Status-quo treated as competitor | PASS | Phase 2 "Adoption story: 'Users adopted {incumbent} because ___.' (role-grounded)" + Phase 3 "'X won this persona because...'" Adoption-decision framing at both levels. |
| C-13 | Inertia landscape classified before persona analysis | PASS | Phase 2 "INERTIA LANDSCAPE": "Classify the inertia this feature faces before analyzing any persona. This classification determines what category of mitigation is valid." Classification/Rationale/Implication fields. Dedicated pre-persona phase with explicit gating instruction. |
| C-14 | Type-conditioned mitigation | PASS | Phase 4 Mitigation: "If structural: name the specific product change -- not 'improve the feature' -- name the gap and the fix, specific enough to assign to an owner. If behavioral: name the specific launch sequence or social proof seeding strategy -- not 'improve onboarding' -- name the sequence and the owner." Strongest anti-generic instruction of any variant. |
| C-15 | Lost TAM implication stated unconditionally | PASS -- strongest of all variants | Phase 5 "LOST TAM IMPLICATION" is a dedicated standalone section: own header, required template, explicit "This section is required. Write it regardless of evidence confidence." instruction, and anchoring vocabulary: "Use 'permanent lost TAM' and 'delayed adoption' as anchoring terms." Phase isolation prevents conditional drift from surrounding synthesis language. |

**Score:** 12+12+12+12+12 + 10+10+10 + 2+2+1+1+2+1+1 = **100**
**All essential pass:** YES

---

### V-04 — Inertia Type Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | Phase 3 "Why They Use the Incumbent: 'X won this persona because...' Not 'it works' -- why it works for this specific person in this role." |
| C-02 | Switching cost quantified | PASS | "Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). 'High' fails." |
| C-03 | Kill barrier named | PASS | Phase 1 Kill Barrier Hypothesis + Phase 3 "Kill Barrier (confirmed or revised)." |
| C-04 | Workaround satisfaction assessed | PASS | "Workaround Satisfaction: 1-5. Flag 4+ as 'good enough' -- state the specific reason." |
| C-05 | Per-persona inertia score present | PASS | "Inertia Score: Low / Medium / High / Critical. Same scale. Required every row." |
| C-06 | Habit lock-in addressed | PASS | "Habit at Risk: specific behavioral pattern. Not a category label." |
| C-07 | Social proof requirement mapped | PASS | "Social Proof Needed: specific threshold -- numbers, names, evidence type." |
| C-08 | Learning curve quantified | PASS | "Learning Curve: time or concept count; comparison anchor if possible." |
| C-09 | Overall risk rating with mitigation | PASS | Phase 4: "Overall adoption inertia risk" + "Mitigation targeting the kill barrier: If structural: name the specific product change -- specific enough to assign to an owner and schedule. If behavioral: name the specific launch sequence or social proof seeding intervention -- name the sequence and the owner. Do not restate. Do not propose generic onboarding." Owner assignment required by both branches. |
| C-10 | Inertia asymmetry identified | PASS | Phase 4 "Inertia asymmetry: Structural / Behavioral" + "Lost TAM implication: ... Required. Unconditional." |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | "Run in four phases. Do not start a phase until the previous one is complete." Phase 1 (hypothesis) must complete before Phase 2 (gate) must complete before Phase 3 (personas). |
| C-12 | Status-quo treated as competitor | PASS | Phase 2 "Why users chose it: one sentence -- the adoption story, not current state." + Phase 3 "'X won this persona because...'" |
| C-13 | Inertia landscape classified before persona analysis | PASS -- strongest of all variants | Phase 2 "INERTIA TYPE GATE": "Do not proceed to persona analysis until you have classified inertia type." Rationale provided: "Getting the type wrong produces a useless mitigation." Classification/Rationale/Implication fields. Closes with: "Gate passed. Proceeding to persona analysis." Self-affirmation makes classification a blocking prerequisite the model tracks in its own output rather than a passively-read section header. |
| C-14 | Type-conditioned mitigation | PASS | Phase 4 Mitigation: "If structural: name the specific product change -- specific enough to assign to an owner and schedule. If behavioral: name the specific launch sequence or social proof seeding intervention -- name the sequence and the owner." |
| C-15 | Lost TAM implication stated unconditionally | PASS | Phase 4 "Lost TAM implication: ... Required. Unconditional." |

**Score:** 12+12+12+12+12 + 10+10+10 + 2+2+1+1+2+1+1 = **100**
**All essential pass:** YES

---

### V-05 — Compressed R3 Complete

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | Section 3 table column "Why Incumbent Won: role-grounded. Not 'it works.'" Required for each row. |
| C-02 | Switching cost quantified | PASS | "Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). 'High' fails." |
| C-03 | Kill barrier named | PASS | Section 1 "Kill Barrier Hypothesis" + Section 4 "Kill Barrier (confirmed or revised)." |
| C-04 | Workaround satisfaction assessed | PASS | Section 3 table "Workaround Satisfaction (1-5)" + column rule "Flag 4+ as 'good enough' -- state the specific reason." Score + trigger + explanation. |
| C-05 | Per-persona inertia score present | PASS | "Inertia Score: Low / Medium / High / Critical. Same scale. Required every row." |
| C-06 | Habit lock-in addressed | PASS | "Habit at Risk: specific behavior. Not a category." |
| C-07 | Social proof requirement mapped | PASS | "Social Proof Needed: specific threshold -- number, name, or evidence type." |
| C-08 | Learning curve quantified | PASS | "Learning Curve: time or concept count; comparison anchor preferred." |
| C-09 | Overall risk rating with mitigation | PASS | Section 6 "Overall risk" + "Mitigation (type-conditioned -- derived from Section 2 inertia type): If Structural: {name the specific product change, assignable to an owner} / If Behavioral: {name the specific launch sequence or social proof intervention} / If Mixed: {structural change + behavioral sequence}. Do not restate. Do not write 'improve onboarding.'" |
| C-10 | Inertia asymmetry identified | PASS | Section 5 "INERTIA ASYMMETRY": Structural/Behavioral split + "Lost TAM implication: {one sentence -- required, unconditional.}" |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | "Produce these sections in order. Do not reorder." Section 1 = Kill Barrier Hypothesis; Section 3 = Persona Table. Structural ordering locked. |
| C-12 | Status-quo treated as competitor | PASS | Section 2 "Why users chose it: 'They adopted {incumbent} because ___.' (adoption decision, not current state -- at least one persona; role-grounded)" + Section 3 "Why Incumbent Won: role-grounded. Not 'it works.'" |
| C-13 | Inertia landscape classified before persona analysis | PARTIAL | Section 2 "INERTIA LANDSCAPE (complete before any persona analysis)" is positioned before Section 3 and has Inertia type/Rationale/Implication fields. The parenthetical "(complete before any persona analysis)" is advisory enforcement, not structural gating. Phase-header framing (--- PHASE 2: INERTIA LANDSCAPE CLASSIFICATION ---) creates a structural boundary the compressed format lacks. The rubric requires a "dedicated pre-persona phase"; a numbered section may read as an inline classification even with the parenthetical. C-13 reliability is lower than V-01/V-02/V-03/V-04. PARTIAL: 1 of 2 pts. |
| C-14 | Type-conditioned mitigation | PASS | Section 6 explicit conditional fields: "If Structural: {name the specific product change...} / If Behavioral: {name the specific launch sequence...} / If Mixed: {structural change | behavioral sequence}." |
| C-15 | Lost TAM implication stated unconditionally | PASS | Section 5 "Lost TAM implication: {one sentence -- required, unconditional. Name which personas or persona type represent permanent lost TAM until product changes vs. delayed adoption reachable with launch strategy.}" |

**Score:** 12+12+12+12+12 + 10+10+10 + 2+2+1+1+1+1+1 = **99**
**All essential pass:** YES

---

## Rankings

| Rank | Variation | Score | All Essential Pass | Key Differentiator |
|------|-----------|-------|--------------------|--------------------|
| T-1 | V-01 R3 upgraded baseline | **100** | YES | Stable four-phase structure; all R3 criteria present with explicit labels -- the reliable floor |
| T-1 | V-02 Type-resolution contract | **100** | YES | Strongest C-14: Phase 2 writes binding "Required mitigation form:" contract; Phase 4 fulfills it |
| T-1 | V-03 Lost TAM standalone section | **100** | YES | Strongest C-15: dedicated Phase 5 with own header, anchoring terms, isolated from synthesis |
| T-1 | V-04 Inertia type gate | **100** | YES | Strongest C-13: "Do not proceed until..." + "Gate passed. Proceeding." self-affirmation |
| 5 | V-05 Compressed R3 complete | **99** | YES | C-13 PARTIAL: parenthetical enforcement weaker than phase-header structural gating |

---

## Excellence Signals

**1. Contract-write pattern: pre-committed "Required mitigation form:" (V-02)**
Phase 2 writes an explicit contract: "Phase 4 mitigation must name a specific product change [if Structural] / must name a specific launch sequence [if Behavioral]." Phase 4 reads the contract it wrote and fills it in. The model cannot produce generic mitigation without contradicting its own Phase 2 output. This is structurally narrower than if/then branching at synthesis time: the answer space is constrained before persona analysis begins, not after. The kill-barrier revision edge case is handled with a reconciliation note. Pattern candidate for R4: pre-committed output contracts for high-drift fields.

**2. Phase isolation for required-unconditional fields: standalone Phase 5 (V-03)**
Lost TAM implication extracted from the synthesis section into its own dedicated phase with its own header, "This section is required. Write it regardless of evidence confidence." instruction, and anchoring vocabulary ("permanent lost TAM", "delayed adoption"). When a required-unconditional field shares a busy synthesis block, surrounding if/then language causes conditional drift. Isolation by phase boundary removes the proximity effect. Pattern candidate for R4: any output field that must appear unconditionally should have its own phase, not share a section with conditional fields.

**3. Procedural gate + self-affirmation: "Do not proceed until..." + "Gate passed." (V-04)**
Phase 2 framed as a blocking prerequisite: "Do not proceed to persona analysis until you have classified inertia type." Closes with: "Gate passed. Proceeding to persona analysis." The self-affirmation token appears in model output as a confirmed prerequisite -- the model cannot generate the next phase without first generating the gate-pass. Stronger C-13 guarantee than a section header the model reads passively. Pattern candidate for R4: critical classification decisions that gate downstream specificity should be framed as blocking prerequisites with self-affirmation.

**4. R3 result: the rubric floor is now high enough that differentiation is about reliability, not correctness.**
R2's top score was 100 (one variant). R3's top score is 100 (four variants). The convergence is a rubric maturity signal: the design space for this skill has been largely captured. R4's question is not "what criteria are missing" but "which structural techniques make existing criteria most reliable under adversarial output conditions."

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Contract-write pattern: Phase 2 writes 'Required mitigation form: [if Structural: specific product change required] [if Behavioral: specific launch sequence required]' as a binding contract before persona analysis; Phase 4 must fulfill it -- model reads its own prior output rather than re-deriving the type condition at synthesis time, preventing generic drift structurally rather than by instruction", "Phase isolation for required-unconditional output fields: extract any field that must appear regardless of evidence confidence into its own dedicated phase with its own header, anchoring vocabulary, and 'required regardless of evidence confidence' instruction -- proximity to surrounding if/then language in shared synthesis sections causes conditional drift that phase-boundary isolation prevents", "Procedural gate + self-affirmation: frame critical pre-analysis classifications as blocking prerequisites ('Do not proceed to [next phase] until you have [classified X]') and close with a trackable self-affirmation token ('Gate passed. Proceeding.') -- makes the classification appear in model output as a confirmed prerequisite rather than a passively-read section header"]}
```
