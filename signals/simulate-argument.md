You are running /simulate-argument for: {{topic}}

Four specialists examine every argument. Commit before any specialist begins: (1) the argument's best case, (2) H0 (null hypothesis: the argument is structurally sound), (3) which inference steps are most load-bearing, (4) which generalizations the paper makes beyond its direct evidence. Logician identifies form -- immutable through Phase 5. Advocate gives the author's best reading -- form-independent generalization scan across all inference steps, including causal inference and argument-from-analogy, citing Phase 0 Gen-IDs. Reviewer challenges the Advocate's committed readings. Chair synthesizes verdicts. Phase 4 closes with an unconditional CP adjacency audit: Step 2 runs for every CP step regardless of Step 1, and CONFIRMED-ELSEWHERE verdict strings carry Gen-ID anchors. The adversary is inertia.

---

## PHASE 0 -- ARGUMENT SETUP

**Best-case argument** (one paragraph):
> "The paper argues that [X], on the grounds that [Y] and [Z]. If correct, this matters because [W]."

**Null hypothesis**:
> "H0: This argument is structurally sound and requires no revision before submission."

**Critical path**: Write TBD; revise after Phase 2 with specific C-IDs.
> "The conclusion depends most heavily on [inference type]. If that step fails, [consequence]."

**Pre-committed generalizations**: Write TBD; revise after Phase 1.

| Gen-ID | Generalization | Why expected |
|--------|----------------|--------------|
| Gen-01 | [claim text] | [why you expect this to lack direct evidence] |
| Gen-02 | | |

Min 2 generalizations. UNSUPPORTED-GEN Gap fields must cite a Gen-ID -- assertion-only Gap does not pass.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}. Also read prior signals: discover-hypothesis, discover-causal, specify-spec.

Revise Phase 0: update critical path with specific C-IDs, update Gen-registry with actual generalizations, mark CP-flagged inferences with YES.

---

## PHASE 2 -- CLAIM MAP

| C-ID | Claim | Type | Depends on | Status | CP? |
|------|-------|------|------------|--------|-----|
| C-01 | [exact claim text] | premise / inference / empirical / definition / conclusion | -- | to-verify | -- |
| C-02 | | inference | C-01 | to-verify | YES / -- |

Min 6 claims. At least one per major section. Mark CP inferences `YES`. Note Phase 0 Gen-ID in Claim column where applicable.

> Do not proceed to PHASE 3 until every claim has an ID, all dependencies are mapped, and CP? flags are assigned.

---

## PHASE 3 -- FOUR-SPECIALIST TRACE

Strict sequence. Each specialist commits under their role identity. Subsequent specialists are bound by prior commitments.

### 3A -- THE LOGICIAN

Names the logical form of every inference step. No evaluation.

```
FORM [C-ID] [CP? YES/--]: [claim text]
Role: Logician
Logical form: [modus ponens / modus tollens / hypothetical syllogism / disjunctive syllogism /
               abduction / inductive generalization / argument from analogy /
               argument from authority / causal inference / other: describe]
Formal structure: [If/Then/Therefore in 1-3 lines]
```

> **I, the Logician, commit the above form identifications for all inference steps. These identifications are immutable across Phase 3, Phase 4, and Phase 5 -- including INVALID-FORM fault classification.** The Advocate, Reviewer, and Chair are bound to these forms. No subsequent specialist and no subsequent phase may reclassify logical structure committed here. INVALID-FORM in Phase 4 is the only available fault class for structural violations -- no re-derivation of form is permitted. Phase 4 INVALID-FORM rows must carry a derivation reference to the specific FORM block committed here. Phase 5 may not propose form reclassification. Conflicts between later findings and my committed forms are INVALID-FORM candidates, not corrections.

### 3B-ADVOCATE -- THE ADVOCATE

States the minimum assumption that would make each inference valid given the Logician's committed form. Scans every inference step for generalization assumptions -- **form-independent**: applies to all steps regardless of form label, including causal inference steps (key assumption posits universal mechanism applicability) and argument-from-analogy steps (key assumption extends analogy scope beyond studied population). Cites Phase 0 Gen-ID when assumption extends beyond studied cases.

```
ADVOCATE [C-ID]: [claim text]
Role: Advocate
  Best reading: [The inference is valid if we assume: ...]
  Key assumption: [one sentence -- the precise unstated premise that closes the gap;
                   "Stated premises are sufficient given the Logician's form" if no gap]
  Generalization assumed: [YES -- this best reading assumes X holds beyond the specific
                            cases, population, or conditions studied /
                            NO -- key assumption is scoped to studied cases only]
  Gen-ID anchor: [Gen-NN from Phase 0 covering this assumption /
                  NEW: not pre-committed; flag for Gen-registry revision /
                  -- (only if Generalization assumed: NO)]
```

> **I, the Advocate, commit the above best readings for all inference steps.** I scanned every best reading for generalization assumptions by examining the *content* of the assumption -- not the Logician's form label. This scan covered all inference steps including those labeled causal inference, argument from analogy, and abduction. A step labeled "causal inference" whose best reading assumes the studied mechanism operates universally, and a step labeled "argument from analogy" whose best reading extends the analogy's scope beyond the studied population, each received the same generalization scan as a step labeled "inductive generalization." All Generalization assumed: YES entries cite a Phase 0 Gen-ID or are flagged NEW. All Generalization assumed: NO entries assert the assumption is scoped to the studied cases. I have not evaluated whether any assumption holds.

### 3B-CRITIC -- THE EMPIRICAL REVIEWER

Tests whether evidence supports the Advocate's committed key assumptions. Checks term consistency. Bound to Logician's forms and Advocate's committed readings. Where the Advocate cited a Gen-ID anchor, this assessment is the direct test of that pre-committed generalization.

```
CRITIC [C-ID]: [claim text]
Role: Empirical Reviewer
  (1) Does evidence support the Advocate's key assumption?
              [YES] / [CITED: ref] / [ASSUMED: taken for granted, not demonstrated] /
              [UNSUPPORTED: evidence needed]
  (2) Term consistency with definition claims?
              [YES] / [DRIFT: term, definition C-ID, how it shifted]
```

> **I, the Empirical Reviewer, commit the above evidence challenges.** I tested the Advocate's committed assumptions -- not re-evaluated Logician forms or generated new best readings. Where the Advocate cited a Gen-ID anchor, my assessment is the direct test of that generalization. The Chair now synthesizes.

### 3C -- THE COMMITTEE CHAIR

Synthesizes all committed analyses into verdicts. No new forms, readings, or checks. CP steps receive explicit severity attention.

```
VERDICT [C-ID]: SOUND / WEAK / BROKEN
Role: Committee Chair
Reason: [why SOUND holds; or the gap between Advocate's requirement and Reviewer's finding,
         with reference to the Logician's committed form]
If WEAK or BROKEN:
  Reviewer flag: YES/NO -- one sentence
  Depth tier: OBVIOUS / NOTABLE / SIGNIFICANT
  Domain comparison: [what standard or prior result does this gap violate?]
```

> **I, the Committee Chair, commit the above verdicts** from the four sealed analyses. No new analyses introduced.

---

## PHASE 4 -- FAULT REGISTER

Every WEAK or BROKEN verdict must appear here with exactly one fault class per row.

**Fault classes**:
- **DEF-DRIFT** -- term shifts meaning from its definition claim to its use
- **UNSUPPORTED-GEN** -- generalization exceeds evidence; Gap must cite Phase 0 Gen-ID (assertion-only Gap fails)
- **CIRCULAR-DEP** -- conclusion appears as implicit premise in its own support chain
- **INVALID-FORM** -- structure violates the Logician's committed form; derives from Phase 3A FORM block only; may not be independently re-derived in Phase 4. **Every INVALID-FORM row requires an immediate derivation line below it.**

| F-ID | C-ID | Verdict | Class | Gap | Fix required | Severity | CP? |
|------|------|---------|-------|-----|--------------|----------|-----|
| F-01 | | BROKEN | [class] | [DEPTH-TIER] [Advocate required X; Reviewer found only Y -- Gen-ID for UNSUPPORTED-GEN] | [exact repair] | P1/P2/P3 | YES/-- |

For every INVALID-FORM row:
> `Derives from: FORM [C-ID] committed in Phase 3A as [form]. The Reviewer's evidence challenge reveals a structural violation of this form.`

Severity: P1 = breaks central conclusion / P2 = weakens key section / P3 = precision issue

**UNSUPPORTED-GEN Gap example**:
> `[SIGNIFICANT] The Advocate required Gen-02: the learning algorithm generalizes to low-resource languages. The Reviewer found only results on five high-resource languages with >=10M training tokens. A specialist in low-resource NLP would require explicit low-resource benchmarks.`

---

**Phase 4 Closing** -- five steps, in order:

**Step 1 -- Fault class count**: Count rows per class code. Name the dominant fault class.

**Step 2 -- H0 test**: Count P1 faults. P1 >= 1: "H0 is rejected." P1 = 0: assess whether P2 faults collectively challenge the central argument.

**Step 3 -- Inertia verdict**: "H0 is [rejected / not rejected]. Inertia -- submitting without revision -- is [not defensible / defensible with minor fixes / defensible]."

**Step 4 -- CP priority audit**: For each CP-flagged step, run all three sub-steps. **Sub-step B runs unconditionally for every CP step regardless of sub-step A result.**

> Sub-step A -- Fault check: "Did a fault register at this CP step? [F-ID at P_-severity, Class: CODE / SOUND -- no fault registered]"

> Sub-step B -- CP-adjacency search **(unconditional)**: "CP dependency chain checked: [list every C-ID this step depends on and every C-ID that depends on it, from the Phase 2 Claim Map]. Faults in chain: [F-NN on C-MM: description; for UNSUPPORTED-GEN, name the Gen-ID anchor from the Advocate's Phase 3 reading / none -- all steps in dependency chain checked and found SOUND]."

> Sub-step C -- Three-way verdict:
> - **CONFIRMED**: sub-step A found a fault
> - **CONFIRMED-ELSEWHERE**: sub-step A SOUND; sub-step B found fault(s) on adjacent step(s)
> - **DISCONFIRMED**: sub-step A SOUND; sub-step B found no faults in the chain

> Write as: "CP audit [C-ID]: [sub-step A result]. [sub-step B dependency chain and result]. Verdict: [CONFIRMED / CONFIRMED-ELSEWHERE: UNSUPPORTED-GEN (Gen-NN) on adjacent C-MM / DISCONFIRMED -- dependency chain checked, no faults found]."

> Rules: (1) CONFIRMED-ELSEWHERE must embed the Gen-ID anchor in the verdict string -- fault ID alone does not pass. (2) DISCONFIRMED must list the dependency chain -- undocumented DISCONFIRMED does not pass.

> After all CP steps: "Structural risk distribution: [one sentence on where actual risk lies vs. Phase 0 prediction]."

**Step 5 -- Generalization accountability**: For each Gen-ID from Phase 0:
> "Gen-01: [F-ID -- UNSUPPORTED-GEN at P_-severity / No fault -- supported by evidence]."

> "Generalization accountability verdict: [one sentence -- were pre-committed generalizations the primary risk, or did other fault classes dominate?]"

---

## PHASE 5 -- AMEND

Three structural fixes ordered P1 -> P2 -> P3. Each cites F-ID, C-ID, Class.

1. [P1 -- F-ID, C-ID, Class: exact repair]
2. [P2 -- F-ID, C-ID, Class: exact repair]
3. [P3 -- F-ID, C-ID, Class: if DEF-DRIFT, name originating definition C-ID and propose stable replacement wording; otherwise name the exact precision gap]

Write artifact to: signals/simulate/argument/{{topic}}-argument-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-argument, topic: {{topic}}, date: {{date}}, claims_mapped: [n], broken_steps: [n], p1_count: [n]
