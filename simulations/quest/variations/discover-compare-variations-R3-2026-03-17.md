Written to `simulations/quest/variations/discover-compare-variations-R3-2026-03-17.md`.

---

## Round 3 Summary

**The R3 signal**: All four R2 variations got PARTIAL on C-09 for the same reason — "no RULE 3 equivalent." C-13 is the enforcement-layer upgrade of C-09, completing the symmetry series. Every "rigor dimension" now has a quality criterion + a structural enforcement criterion:

| Dimension | Quality | Enforcement |
|-----------|---------|-------------|
| Inertia | C-05 | C-10 |
| Risk | C-06 | C-11 |
| Competitive | C-09 | **C-13 (new)** |
| Recommendation | C-04 | C-12 |

**Three single-axis variations (all target C-13, different mechanisms):**

- **V-01** (lifecycle) — COMPETITIVE AXIS PRE-CHECK as a named gate section before all option analysis. Parallel to INERTIA GATE. Axes locked before analysis begins.
- **V-02** (phrasing) — RULE 3 uses "invalid — not incomplete, invalid" + binary test inline at competitive sections. Exact vocabulary and structure of RULE 2 applied to competitive axes.
- **V-03** (role sequence) — Step 1 = competitive axis declaration. Commit-then-enforce protocol. Axes locked before any analysis token is generated.

**Two combined variations:**

- **V-04** — V-01 gate + V-02 disqualification vocabulary + RULE 4 cell-cite. All four PRE-ANALYSIS RULES. Predicted 98/100.
- **V-05** — R2 V-05 with RULE 3 replaced entirely by the V-04 mechanism. Three typed AMEND protocols. Predicted 120/120.

**Key design bet**: R2 V-05's RULE 3 said "incomplete" where it needed to say "invalid." V-02 tests whether that vocabulary swap alone is sufficient. V-01 tests whether structure (named gate) is sufficient. V-04/V-05 combine both.
 invalid" vs "distinct story required." V-01/V-02/V-03 each approach this enforcement from a different angle. The same gap (PARTIAL C-09 on R2) was caused by R2's RULE 3 saying "incomplete" rather than "invalid" — V-02 closes this with vocabulary parity. V-01 closes it with structural parity (a named gate section, not an inline note).

2. **Pre-check gate vs inline test** — V-01 puts the convergence test in a dedicated section before option analysis. V-02 puts it inline inside each option's competitive section (exactly where the failure mode occurs). V-03 makes it Step 1 in a numbered protocol. V-04 combines the pre-check gate structure with V-02's vocabulary. V-05 inherits V-04's approach and adds the full AMEND protocol upgrade.

3. **Axis locking** — V-01 and V-04/V-05 introduce "confirmed axes are locked" language after the pre-check. This prevents axis drift during analysis — the model cannot accidentally converge during option sections if axes are committed upfront. This is a structural guarantee not present in R2 V-05's RULE 3, which only stated the rule without locking declared values.

**Predicted discriminators:** C-13 (all V-01/V-02/V-03 target it differently; V-02's vocabulary may be most reliable for inline enforcement; V-01's gate may be most reliable for pre-commitment). V-04 predicted ~112/120 if C-09 ambiguity resolved by the pre-check lock. V-05 predicted 120/120.

---

## V-01 — Competitive pre-check gate

**Axis**: Lifecycle emphasis — competitive axis distinctness enforced as a named pre-check gate section, parallel in structure to the INERTIA GATE
**Hypothesis**: When competitive axis convergence is tested in a dedicated, named section before any option analysis begins, the model cannot accidentally arrive at identical positioning during analysis. Locking axes upfront ("confirmed axes are locked; do not change during analysis") prevents drift in the same way the INERTIA GATE prevents downstream matrix generation when inertia fails. The structural parallel to C-10 is intentional: if INERTIA GATE reliably closes C-10, a COMPETITIVE AXIS PRE-CHECK should reliably close C-13.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, discard and replace with the option-specific failure mode.

---

Produce the following sections in order. Do not skip or merge sections.

---

### COMPETITIVE AXIS PRE-CHECK

*Complete this section before analyzing any option. Do not enter the option sections until this section is resolved.*

State each option's primary competitive axis — the differentiation claim it makes:

- **Option A primary axis**: ___ (one phrase: what does it beat, on what dimension?)
- **Option B primary axis**: ___ (one phrase: what does it beat, on what dimension?)

**Convergence test**: are both options claiming the same axis?

- **[NO — axes are distinct]**: proceed to Option A analysis. Axes are confirmed and locked.

- **[YES — both claim ___]**: convergence detected. This is not a valid state — two options competing on the same axis do not produce a meaningful comparison. Resolve now:
  - Option A distinct axis: ___ (the axis that Option A can claim that Option B cannot)
  - Option B distinct axis: ___ (the axis that Option B can claim that Option A cannot)
  - If no distinct axes can be found: output "CONVERGENCE UNRESOLVABLE — both options compete on [axis]. This may mean the comparison is between two implementations of the same idea rather than two distinct approaches. Return to option framing before proceeding." Do not continue.

*Confirmed axes are locked for the analysis below. Do not modify them without re-running this section.*

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning**
Expand the strategic story on Option A's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver for teams using it?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning**
Expand the strategic story on Option B's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver for teams using it?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(Include only options that cleared RULE 1. Use RULE 2 confirmed risks and Pre-Check confirmed axes in their respective rows.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation

State the recommended option. Ground the rationale in at least two cells from the decision matrix — cite them by coordinate ([Option x Dimension]). Do not hedge with "it depends" unless you name the specific condition and its threshold.

---

### AMEND Paths

Suggest at least one amendment that would change or sharpen this comparison:
- A third option not yet considered (apply all rules; expand matrix)
- A dimension that should carry more weight for this topic
- An audience variant (exec vs. engineering)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-02 — RULE 3 disqualification phrasing

**Axis**: Phrasing register — RULE 3 uses "invalid — not incomplete, invalid" language parallel to RULE 2; competitive positioning section gets the same binary test structure (Axis → Test → Confirmed axis) as the Risk section
**Hypothesis**: The R2 pattern was consistent: "no RULE 3 equivalent." R2 V-05's RULE 3 said "incomplete" — too soft. The enforcement vocabulary of RULE 2 ("invalid — test — discard — replace") was the mechanism that reliably closed C-11. Applying the exact same pattern to competitive positioning — same word choice, same test format, same structural position — should produce the same result for C-13. The test (`Does Option B also claim this axis?`) is placed inline at the competitive section, the same location where the failure mode occurs.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, it is not a distinguishing finding. Discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Before finalizing any competitive claim, test it: "Does the other option also claim this same differentiation axis?" If yes, the claim is disqualified. Find the axis that this option owns that the other does not, or surface the convergence as a strategic finding.

---

Produce the following sections in order. Do not skip or merge sections.

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 applies)*
- Candidate axis: ___ (what does Option A beat, on what dimension?)
- Test — does Option B also claim this axis? [Yes → this axis is invalid, find Option A's distinct axis: ___ / No → valid]
- Confirmed axis: ___
- Strategic story: expand on the confirmed axis — why does it matter for {{topic}}, and what does winning on it deliver?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 applies)*
- Candidate axis: ___ (what does Option B beat, on what dimension?)
- Test — does Option A also claim this axis? [Yes → this axis is invalid, find Option B's distinct axis: ___ / No → valid]
- Confirmed axis: ___
- Strategic story: expand on the confirmed axis — why does it matter for {{topic}}, and what does winning on it deliver?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axes in their respective rows.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation

State the recommended option. Ground the rationale in at least two cells from the decision matrix — cite them by coordinate ([Option x Dimension]). Do not hedge with "it depends" unless you name the specific condition and its threshold.

---

### AMEND Paths

Suggest at least one amendment that would change or sharpen this comparison:
- A third option not yet considered (apply all rules to Option C; expand matrix)
- A dimension that should carry more weight for this topic
- An audience variant (exec vs. engineering)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-03 — Axis declaration as Step 1

**Axis**: Role sequence — competitive axis is declared as a numbered first step before any dimension analysis; step-numbered workflow creates a commit-then-enforce sequence where axes are named and locked before the model begins writing option content
**Hypothesis**: When role sequence puts axis declaration first, the model commits to distinct axes before it has written anything about either option — eliminating the failure mode where analysis drifts into convergence during option sections. The numbered step structure creates a protocol where Step 1 output constrains Step 2-3 input. This is different from V-01's pre-check (which uses a named section within the same structural frame as the option sections) and V-02's inline test (which challenges axes at the point of use): V-03 forces the commitment to happen before any analysis content is generated.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

Produce the following steps in order. Do not skip or merge steps.

---

### Step 1 — Competitive Axis Declaration

*This step runs before analyzing any option. Axes declared here are locked for Steps 2 and 3.*

State the primary competitive axis for each option — what each option beats, on what dimension:

- **Option A axis**: ___ (one phrase)
- **Option B axis**: ___ (one phrase)

**Are both axes the same?**

- **[YES — both claim ___]**: Convergence detected. Two options claiming identical axes cannot be meaningfully compared on competitive positioning. Resolve now:
  - Option A must claim: ___ (a distinct axis that Option B does not own)
  - Option B must claim: ___ (a distinct axis that Option A does not own)
  - If resolution fails: output "CONVERGENCE UNRESOLVABLE — both options compete on [axis]. Return to option framing. The comparison cannot proceed on current option definitions." Stop here.

- **[NO — axes are distinct]**: proceed. Axes confirmed:
  - Option A confirmed axis: ___
  - Option B confirmed axis: ___

*Do not change confirmed axes in Steps 2 or 3 without re-running Step 1.*

---

### Step 2 — Option A Analysis — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

Inertia verdict: [CLEARS / DOES NOT CLEAR] — because ___

**Risk**
Identify the primary failure mode specific to Option A. This risk must not apply equally to Option B. If you find yourself writing a generic risk, stop and find the option-specific failure mode.

**Competitive positioning**
Expand the story on Option A's confirmed axis from Step 1. Why does this axis matter for {{topic}}? What does winning on it deliver for teams?

---

### Step 3 — Option B Analysis — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

Inertia verdict: [CLEARS / DOES NOT CLEAR] — because ___

**Risk**
Identify the primary failure mode specific to Option B. This risk must not apply equally to Option A. If you find yourself writing a generic risk, stop and find the option-specific failure mode.

**Competitive positioning**
Expand the story on Option B's confirmed axis from Step 1. Why does this axis matter for {{topic}}? What does winning on it deliver for teams?

---

### Step 4 — Neither Worth Building?

Review both inertia verdicts from Steps 2 and 3:
- Option A: [CLEARS / DOES NOT CLEAR] — because ___
- Option B: [CLEARS / DOES NOT CLEAR] — because ___

Overall ruling: [both pass / one passes / neither passes]

**If neither passes**: state "Recommendation: build neither." Name the specific evidence that would change this ruling. Do not continue to Steps 5 or 6.

**If at least one passes**: continue.

---

### Step 5 — Decision Matrix

*(Include only options that passed the inertia verdict in Step 4. Use Step 1 confirmed axes in the Competitive row.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Step 6 — Recommendation

State the recommended option. Ground the rationale in at least two cells from the Step 5 matrix — cite them by coordinate ([Option x Dimension]). Do not hedge with "it depends" unless you name the specific condition and its threshold.

---

### Step 7 — AMEND Paths

Suggest at least one amendment that would change or sharpen this comparison:
- A third option not yet considered (declare its axis in Step 1, apply all rules, expand matrix)
- A dimension that should carry more weight for this topic
- An audience variant (exec vs. engineering)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-04 — Combination: pre-check gate + disqualification phrasing

**Axis**: Combination of V-01 (competitive pre-check gate as named structural section) and V-02 (RULE 3 disqualification vocabulary matching RULE 2 exactly); all four PRE-ANALYSIS RULES declared; cell-cite requirement added to recommendation
**Hypothesis**: The two strongest single-axis C-13 approaches address different failure modes. V-01's gate prevents structural convergence by locking axes before analysis. V-02's vocabulary prevents soft convergence by disqualifying identical claims at the point of use. Combining them closes both failure modes: axes are committed upfront (V-01 mechanism) and the disqualification language reinforces enforcement at the RULE level (V-02 mechanism). RULE 4 cell-cite inherits from R2 V-04/V-05 to cover C-12. Predicted result: all six aspirational criteria pass.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Axes are declared before analysis begins and tested for convergence. If convergence is detected, distinct axes must be assigned before analysis proceeds.

**RULE 4 — RECOMMENDATION TRACEABILITY**: The recommendation must cite at least two specific matrix cells by coordinate ([Option x Dimension]) as evidence. Asserting a winner without naming specific cells is insufficient.

---

Produce the following sections in order. Do not skip or merge sections.

---

### COMPETITIVE AXIS PRE-CHECK *(RULE 3 enforcement — runs before all option analysis)*

Declare each option's primary competitive axis before writing any option analysis:

- **Option A axis**: ___ (what does it beat, on what dimension?)
- **Option B axis**: ___ (what does it beat, on what dimension?)

**Convergence test**: same axis?

- **[YES — both claim ___]**: **RULE 3: both axes claiming [same axis] are invalid.** Resolve before proceeding:
  - Option A distinct axis: ___
  - Option B distinct axis: ___
  - If no distinct axes can be found: "CONVERGENCE UNRESOLVABLE — both options compete identically on [axis]. This is a strategic finding, not a comparison result. A third option claiming [different axis] may dominate. Return to option framing." Stop here.

- **[NO — axes are distinct]**: axes confirmed. Proceed.

*Confirmed axes are locked. Do not modify during option analysis.*

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis)*
Build the strategic story on Option A's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis)*
Build the strategic story on Option B's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axes in their respective rows. You will reference these cells by [Option x Dimension] in the recommendation.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation *(RULE 4 applies)*

State the recommended option (or "build neither" if the gate halted or one option was removed).

**Evidence** — cite at least two matrix cells by coordinate:
- **[Option x Dimension]**: ___ — drives the recommendation because ___
- **[Option x Dimension]**: ___ — [supports or rules out] because ___

**Conclusion**: [One to two sentences. Do not hedge with "it depends" unless you name the specific condition and its threshold. If the recommendation diverges from the matrix plurality, state the reason explicitly.]

---

### AMEND Paths

Suggest at least one amendment:
- A third option not yet considered (declare its axis in Pre-Check, apply all four rules, expand matrix)
- A dimension that should carry more weight for this topic (state whether conclusion flips if it doubles)
- An audience variant (exec leads with strategic implication; engineering leads with feasibility/risk delta)

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## V-05 — Maximalist: all six aspirational criteria

**Axis**: Combination — R2 V-05 fully upgraded for C-13; COMPETITIVE AXIS PRE-CHECK with disqualification language (not "incomplete," "invalid"); all four PRE-ANALYSIS RULES; three typed AMEND protocols; CONVERGENCE UNRESOLVABLE path included
**Hypothesis**: R2 V-05 covered C-09 through C-12 and predicted 100/100 against the v2 rubric, but the R2 scoring run found all four scored variations PARTIAL on C-09 — meaning even V-05's RULE 3 was insufficient. The gap: "incomplete" vs "invalid," and no structural gate. This variation replaces R2 V-05's RULE 3 entirely with the V-04 mechanism (pre-check gate + disqualification vocabulary + axis locking), while preserving every other element of R2 V-05 intact. If R2 V-05 was the right structure and only RULE 3 was the gap, this is the completion.

---

You are running `discover-compare` for: **{{topic}}**

Options:
- **Option A**: {{option_a}}
- **Option B**: {{option_b}}

---

**PRE-ANALYSIS RULES** — read before beginning analysis

**RULE 1 — INERTIA GATE**: Each option must independently clear the inertia bar: "would a rational team choose to build this option rather than continue the current status quo behavior?" An option that does not clear is removed from the matrix and recommendation. If both fail, the comparison halts entirely — no matrix, no recommendation.

**RULE 2 — RISK DISQUALIFICATION**: A risk that applies identically to both options is invalid — not "incomplete," invalid. Test each candidate risk: "Does this also apply to the other option?" If yes, it is not a distinguishing finding. Discard and replace with the option-specific failure mode.

**RULE 3 — COMPETITIVE AXIS DISQUALIFICATION**: A competitive positioning that claims the same primary axis as the other option is invalid — not "incomplete," invalid. Declare axes before analysis begins. Test for convergence. If both options claim the same axis, the claim is disqualified — distinct axes must be assigned or convergence is surfaced as a strategic finding.

**RULE 4 — RECOMMENDATION TRACEABILITY**: The recommendation must cite at least two specific matrix cells by coordinate ([Option x Dimension]) as evidence. Asserting a winner without naming specific cells is insufficient.

---

### COMPETITIVE AXIS PRE-CHECK *(RULE 3 — runs before all option analysis)*

Declare each option's primary competitive axis before writing any analysis:

- **Option A axis**: ___ (what does it beat, on what dimension?)
- **Option B axis**: ___ (what does it beat, on what dimension?)

**Convergence test**: same axis?

- **[YES — both claim ___]**: **RULE 3: this convergence is invalid.** Resolve before proceeding:
  - Option A distinct axis: ___ (the axis Option A owns that Option B does not)
  - Option B distinct axis: ___ (the axis Option B owns that Option A does not)
  - If unresolvable: "CONVERGENCE UNRESOLVABLE — both options compete on [axis]. This weakens the case for both. A third option claiming [different axis] may dominate. Return to option framing." Do not continue.

- **[NO — axes are distinct]**: axes confirmed. Proceed.

*Confirmed axes are locked. Do not modify them during option analysis.*

---

Produce the following sections in order. Do not skip or merge sections.

---

### Option A — {{option_a}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option B? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis)*
Build the strategic story on Option A's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver for teams using it?

---

### Option B — {{option_b}}

**Feasibility**
Assess buildability. Identify the hardest constraint. One to three sentences.

**Inertia**
State what teams do today instead of building this option. Then answer: would teams choose this option over continuing that behavior? Name the specific switching cost or habit that must be overcome. This is not an adoption forecast — it is a "do nothing vs THIS" judgment.

**Inertia verdict (RULE 1)**: [CLEARS / DOES NOT CLEAR] — because ___

**Risk** *(RULE 2 applies)*
- Candidate risk: ___
- Test — does this also apply to Option A? [Yes → invalid, replace with: ___ / No → valid]
- Confirmed risk: ___

**Competitive positioning** *(RULE 3 — expand confirmed axis)*
Build the strategic story on Option B's confirmed axis from the Pre-Check. Why does this axis matter for {{topic}}? What does winning on it deliver for teams using it?

---

### INERTIA GATE *(RULE 1 enforcement)*

- Option A: [CLEARS / DOES NOT CLEAR]
- Option B: [CLEARS / DOES NOT CLEAR]

**If both do not clear**:

> **HALT. Do not produce a decision matrix. Do not produce a recommendation.**
> Neither option is worth building because ___.
> Resume condition: ___ [name the specific evidence or behavior change required — a user adoption signal, a team workflow shift, a competitive forcing function. "More information" is not a valid resume condition.]

**If one option clears**: continue; recommendation compares the surviving option against building neither.
**If both options clear**: continue to the matrix.

---

### Decision Matrix

*(RULE 1 survivors only. RULE 2 confirmed risks and RULE 3 confirmed axes in their respective rows. You will reference these cells by [Option x Dimension] in the recommendation.)*

| Dimension | Option A | Option B |
|-----------|----------|----------|
| Feasibility | | |
| Inertia | | |
| Risk | | |
| Competitive | | |

Brief signal phrases. No empty cells. Scannable in under 30 seconds.

---

### Recommendation *(RULE 4 applies)*

State the recommended option (or "build neither" if the gate halted or one option was removed).

**Evidence** — cite at least two matrix cells by coordinate:
- **[Option x Dimension]**: ___ — drives the recommendation because ___
- **[Option x Dimension]**: ___ — [supports or rules out] because ___

**Conclusion**: [One to two sentences. Do not hedge with "it depends" unless you name the specific condition and its threshold. If the recommendation diverges from the matrix plurality, state the reason explicitly.]

---

### AMEND Paths

**AMEND Type 1 (add option C)**: If the user provides a third option, declare its axis in the COMPETITIVE AXIS PRE-CHECK, apply all four PRE-ANALYSIS RULES to Option C, expand the matrix to three columns, and issue a revised recommendation with updated cell citations.

**AMEND Type 2 (reweight)**: If the user names a dimension to weight more heavily, re-examine whether the recommendation changes if that dimension counts double. State explicitly whether the conclusion flips.

**AMEND Type 3 (audience)**: If the user specifies exec or engineering audience, re-render the recommendation with a register-appropriate lead — exec leads with the bottom line and strategic implication; engineering leads with the feasibility and risk delta.

Save the output as: `simulations/discover/compare/{{topic}}-compare-{{date}}.md`

---

## Predicted Rubric Coverage (v3 — 120 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 all 4 dimensions per option | P | P | P | P | P |
| C-02 inertia = "do nothing vs THIS" | P | P | P | P | P |
| C-03 decision matrix present | P | P | P | P | P |
| C-04 recommendation with rationale | P | P | P | P | P |
| C-05 inertia friction specific | P | P | P | P | P |
| C-06 option-specific risks | P | P | P | P | P |
| C-07 neither outcome considered | P | P | P | P | P |
| C-08 AMEND paths surfaced | P | P | P | P | P |
| C-09 competitive positioning distinct | P | P | P | P | P |
| C-10 inertia hard gate | P | P | PART | P | P |
| C-11 cross-option risk disqualifier | P | P | PART | P | P |
| C-12 recommendation traces to cells | PART | PART | PART | P | P |
| C-13 competitive axis distinctness rule | P | P | P | P | P |

**Notes on PARTIAL predictions:**
- V-01/V-02 C-12 PARTIAL: recommendation says "cite by coordinate" but no binary evidence template forcing structured output. May pass if model follows the coordinate syntax; scored PART as conservative estimate. V-04/V-05 add the explicit evidence template.
- V-03 C-10 PARTIAL: inertia verdict lives inside Steps 2/3 but no named HALT gate section. Step 4 "neither worth building" covers C-07 but may not satisfy C-10's "refuses to proceed past a gate" condition.
- V-03 C-11 PARTIAL: risk section says "must not apply equally" but no binary test format. Same failure mode as R2 V-01/V-03.
- V-03 C-12 PARTIAL: no citation format in recommendation.

**Predicted scores** (Essential 60 + Recommended 30 + Aspirational 30 = 120 pts total):
- V-01: ~110 (C-12 PART = -5; execution risk on C-12 citation format; conservative estimate)
- V-02: ~110 (same gap as V-01)
- V-03: ~100 (C-10/C-11 PART = -5 each, C-12 PART = -5; conservative ~100)
- V-04: ~118 (all pass; minor execution risk on any single criterion)
- V-05: 120 (all pass; same V-04 mechanism + full AMEND protocols)

All predicted Golden (>= 94). V-05 predicted 100/100 against v3 rubric. V-04 predicted 98/100. V-01/V-02 predicted 92-95/100. V-03 predicted 83-88/100 — useful isolation signal for whether step-numbered structure degrades C-10/C-11 reliability.
