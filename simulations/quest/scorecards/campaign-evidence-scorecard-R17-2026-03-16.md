## Quest Scorecard — campaign-evidence (Round 17)

---

### Evaluation Basis

All five R17 variates carry the full R16 baseline — C-01 through C-38 pass in every variation per the explicit baseline declaration. Scoring differentiation concentrates on C-39 through C-42.

---

### Variation-by-Variation Scoring

---

#### V-01 — Axis A: Multi-column rule-named interrogative headers (C-41 only; SEQUENCING = single rule)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Multi-stage campaign (5 stages) | PASS | Web → Intel → Hypothesis → Analysis → Synthesis declared in order |
| C-02 | Evidence before hypothesis | PASS | S1+S2 complete; S3 entry condition gates on S2 exit pass |
| C-03 | Hypotheses with falsification conditions | PASS | S3 execution requires claim + falsification condition per hypothesis |
| C-04 | Output self-contained | PASS | Evidence Brief + Gate Record + Consolidated Audit Table |
| C-05 | Source attribution per claim | PASS | `[web]`, `[intel]`, `[hypothesis]`, `[analysis]`, `[synthesis]` tags required at each stage |
| C-06 | Synthesis distinguishes consensus vs conflict | PASS | S5 explicitly requires sections 2 (consensus) and 3 (conflict) |
| C-07 | Calibrated confidence levels | PASS | Anti-uniformity guard at S4 and S5; distribution must show 2+ levels |
| C-08–C-38 | R16 baseline criteria | PASS | Carried forward per variate declaration |
| C-39 | Interrogative at column-header level | PASS | `\| Will ATTRIBUTION hold? [Stage 1 of 5] \|` — interrogative IS the column header |
| C-40 | SEQUENCING scope covers evidence-stage ordering | PASS | SEQUENCING RULE declares "(2) evidence-stage relative ordering — the ordering among evidence stages is a named, governed decision invokable by identifier" |
| **C-41** | Rule-named interrogative column headers | **PASS** | `"Will ATTRIBUTION hold?"`, `"Will SEQUENCING hold?"`, `"Will FALSIFICATION hold?"` — each column header names the specific rule under interrogation. Tables are self-describing when detached from context. |
| **C-42** | SEQUENCING decomposed into peer rules | **FAIL** | Single SEQUENCING RULE in coverage map; hypothesis placement and evidence ordering share one row, one invocation trail, checksum 40. Gap at evidence-ordering boundary invisible behind shared identifier. |

**V-01 Score**: 60 + 30 + (34/35 × 10) = **99.7**

---

#### V-02 — Axis B: SEQUENCING decomposed into peer rules (C-42 only; generic headers)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-07 | Essential + Recommended | PASS | Baseline intact |
| C-08–C-38 | R16 baseline | PASS | Carried forward |
| C-39 | Interrogative at column-header level | PASS | `\| Rule \| Will this rule hold? [Stage N of 5] \|` — generic interrogative IS the column header on a row-per-rule table |
| C-40 | SEQUENCING scope covers evidence-stage ordering | PASS | SEQUENCING-ORDER RULE explicitly governs evidence-stage relative ordering as its sole governed dimension |
| **C-41** | Rule-named interrogative column headers | **FAIL** | Column header is `"Will this rule hold? [Stage N of 5]"` — generic, not rule-named. Rule identity appears only in the Row column. A reader detaching the table cannot determine which rule is under interrogation from the header alone. |
| **C-42** | SEQUENCING decomposed into peer rules | **PASS** | SEQUENCING-HYPO (S1+, S2+, S3+, S4−, S5−) and SEQUENCING-ORDER (S1+, S2+, S3−, S4−, S5−) occupy independent coverage-map rows with independent invocation trails. Checksum shift 40→47 is computed automatically: SEQUENCING-ORDER contributes 2 positive × 2 phases + 3 negative × 1 = 7 new artifacts. No static integers required updating. C-29 extensibility demonstrated in live action. |

**V-02 Score**: 60 + 30 + (34/35 × 10) = **99.7**

---

#### V-03 — Axis A (boundary test): Conversational rule-named interrogative headers

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-07 | Essential + Recommended | PASS | Baseline intact |
| C-08–C-38 | R16 baseline | PASS | Carried forward |
| C-39 | Interrogative at column-header level | PASS | Expanded interrogative ("Will every ATTRIBUTION claim be labeled with its source stage?") IS the column header; no cell-level prompt required |
| C-40 | SEQUENCING scope covers evidence-stage ordering | PASS | SEQUENCING RULE declares "(2) declared ordering among evidence stages" |
| **C-41** | Rule-named interrogative column headers | **PASS** | Conversational phrasing names ATTRIBUTION explicitly: "Will every ATTRIBUTION claim be labeled with its source stage? [Stage 1 of 5]". C-41 requires rule identity in the header — it does not require "Will X hold?" terse form. Header identifies ATTRIBUTION as the rule under interrogation when detached from context. PASS (boundary confirmed: rule identity is sufficient; terse form is not required). |
| **C-42** | SEQUENCING decomposed into peer rules | **FAIL** | Single SEQUENCING RULE; same gap as V-01 |

**V-03 Score**: 60 + 30 + (34/35 × 10) = **99.7**

**Boundary signal**: V-03 confirms C-41 is about rule identity in the header, not about terse "Will X hold?" phrasing. A first-time reader encountering "Will CALIBRATION ratings show 2+ distinct levels? [Stage 4 of 5]" can identify CALIBRATION as the rule under check — that's the bar, and conversational phrasing clears it.

---

#### V-04 — Combined: Role reversal + C-41 + C-42

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-07 | Essential + Recommended | PASS | 5 stages; Intel (S1) then Web (S2) then Hypothesis (S3); falsifiable hypotheses; self-contained output; attribution; consensus/conflict; calibrated confidence |
| C-08–C-38 | R16 baseline | PASS | Carried forward; note role reversal is a SEQUENCING-ORDER governed decision, not a structural violation |
| C-39 | Interrogative at column-header level | PASS | `"Will ATTRIBUTION hold? [Stage 1 of 5]"` as column header |
| C-40 | SEQUENCING scope covers evidence-stage ordering | PASS | SEQUENCING-ORDER RULE declares Intel-first ordering as a named governed decision; any deviation from this declared order is an auditable violation |
| **C-41** | Rule-named interrogative column headers | **PASS** | `"Will ATTRIBUTION hold?"`, `"Will SEQUENCING-HYPO hold?"`, `"Will SEQUENCING-ORDER hold?"` as column headers. Each checkpoint table is self-describing when detached. Rule decomposition does not complicate C-41 — SEQUENCING-HYPO and SEQUENCING-ORDER each get their own column with their own rule-named header. |
| **C-42** | SEQUENCING decomposed into peer rules | **PASS+** | SEQUENCING-HYPO and SEQUENCING-ORDER with independent rows and invocation trails. Critically: SEQUENCING-ORDER governs a live, non-default ordering decision. FORM-PRE-S1 SEQUENCING-ORDER cell: "Intel-first ordered as governed decision. [Yes]." FORM-PRE-S2 cell: "S2 Web follows declared Intel-first ordering. [Yes]." The rule does actual governance work at both S1 and S2 boundaries — not a ceremonial default confirmation. This is the strongest demonstration of C-42 value: a rule that names only hypothesis placement could silently miss the ordering reversal; decomposition makes the Intel-first decision auditable at its own boundary. |

**V-04 Score**: 60 + 30 + (35/35 × 10) = **100.0**

---

#### V-05 — Combined: Inertia framing + C-41 + C-42

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-07 | Essential + Recommended | PASS | 5 stages; evidence-first; falsifiable hypotheses; self-contained; attribution; consensus/conflict; calibrated |
| C-08–C-38 | R16 baseline | PASS | Carried forward |
| C-39 | Interrogative at column-header level | PASS | `"Will ATTRIBUTION hold? [Stage N of 5]"` as column header |
| C-40 | SEQUENCING scope covers evidence-stage ordering | PASS | SEQUENCING-ORDER RULE explicitly governs evidence-stage relative ordering |
| **C-41** | Rule-named interrogative column headers | **PASS** | `"Will ATTRIBUTION hold?"`, `"Will SEQUENCING-HYPO hold?"`, `"Will SEQUENCING-ORDER hold?"`, `"Will FALSIFICATION hold?"`, `"Will CALIBRATION hold?"`, `"Will PROVENANCE hold?"` — all six rules get rule-named column headers. Cell annotations further embed antipattern names: `"[Yes / No] -- no hypothesis-first mode"` beneath SEQUENCING-HYPO header converts the binary into an antipattern-absence check. |
| **C-42** | SEQUENCING decomposed into peer rules | **PASS+** | SEQUENCING-HYPO and SEQUENCING-ORDER with independent rows, trails, and checksum 47. The Inertia Baseline table explicitly maps each antipattern to its governing rule: `hypothesis-first mode → SEQUENCING-HYPO` / `unordered collection → SEQUENCING-ORDER`. The decomposition is now doubly visible: (1) in the coverage map as two independent rows, and (2) in the Inertia Baseline as two distinct failure modes requiring two distinct rules. The checksum shift commentary ("prior single-SEQUENCING campaigns had checksum 40; shift to 47 reflects SEQUENCING-ORDER adding 7 artifacts automatically") embeds the extensibility proof as narrative context rather than just arithmetic. |

**V-05 Score**: 60 + 30 + (35/35 × 10) = **100.0**

---

### Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | C-41 | C-42 | Total | Rank |
|-----------|:--------------:|:----------------:|:-----------------:|:----:|:----:|:-----:|:----:|
| V-04 | 60 | 30 | 10.00 | PASS | PASS+ | **100.0** | 1 (tie) |
| V-05 | 60 | 30 | 10.00 | PASS | PASS+ | **100.0** | 1 (tie) |
| V-01 | 60 | 30 | 9.71 | PASS | FAIL | **99.7** | 3 (tie) |
| V-02 | 60 | 30 | 9.71 | FAIL | PASS | **99.7** | 3 (tie) |
| V-03 | 60 | 30 | 9.71 | PASS | FAIL | **99.7** | 3 (tie) |

---

### Excellence Signals

**Top variation: V-04 and V-05 (tied at 100.0)**

The R17 round achieves its primary objective in V-04 and V-05: C-41 (rule-named interrogative column headers) and C-42 (SEQUENCING decomposed into independently-trackable peer rules) are simultaneously satisfied within the named-table physical-separation baseline from R16.

**Signal 1 — Antipattern Baseline as Governance Complement (V-05 PASS+)**
V-05's Inertia Baseline table maps each named failure mode to the rule that prevents it (`hypothesis-first mode → SEQUENCING-HYPO RULE`, `unordered collection → SEQUENCING-ORDER RULE`). This converts C-42 compliance from a positive assertion ("evidence ordering is governed") into a two-sided declaration with named failure modes. The invocation cells then reference antipattern names: `"[Yes/No] -- no hypothesis-first mode detected"`, making each binary check an antipattern-absence check. The governance framework becomes readable by a first-time executor who does not already know what the rules prevent.

**Signal 2 — Live Ordering Decision as SEQUENCING-ORDER Stress Test (V-04 PASS+)**
V-04 deploys Intel-first stage ordering as a real SEQUENCING-ORDER-governed decision. FORM-PRE-S1 declares the ordering at S1's boundary; FORM-PRE-S2 confirms compliance at S2's boundary. This demonstrates that SEQUENCING-ORDER governs actual choices, not just ceremonial default confirmations. A campaign using Web-first (the default) trivially satisfies SEQUENCING-ORDER at every invocation; V-04's reversal forces the rule to do governance work, making the decomposition's value concrete.

**Signal 3 — C-41 Boundary Clarification (V-03 boundary confirmed)**
V-03 confirms that C-41 requires rule identity in the column header — not "Will X hold?" terse form. "Will every ATTRIBUTION claim be labeled with its source stage?" passes because ATTRIBUTION is identifiable from the header alone when detached from context. This boundary is clean and stable.

**Signal 4 — Checksum Shift as Extensibility Proof (V-02 and V-04/V-05)**
The 40→47 shift narrative — "SEQUENCING-ORDER added 2 positive cells and 3 negative cells, 7 new artifacts, absorbed automatically without static integer updates" — is now a documented, repeatable proof of C-29 extensibility. Any future peer rule added to the registry will produce a computable checksum shift for the same reason.

---

### Rubric Notes

**C-39 vs C-41 distinction confirmed**: C-39 requires any interrogative at column-header level (V-02's generic "Will this rule hold?" passes C-39 but fails C-41). C-41 requires the rule name in the header (V-02 fails; V-01/V-03/V-04/V-05 pass). The distinction is: C-39 makes blank cells doubly visible as open column-level questions; C-41 makes the table independently inspectable by naming which rule is questioned.

**C-42 vs C-40 scope**: C-40 requires that the SEQUENCING RULE explicitly names evidence-stage ordering as a governed dimension. C-42 requires that the two governed dimensions (hypothesis placement and evidence ordering) are tracked as independent rules with independent audit trails. V-01 and V-03 satisfy C-40 (both dimensions named in a single rule) but fail C-42 (a single invocation at the hypothesis boundary counts for both dimensions, concealing the possibility of an evidence-ordering gap).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertia Baseline table as preamble fixture — maps each named failure mode to its governing rule, converting C-42 compliance from a positive assertion into a two-sided declaration with named excluded antipatterns", "Live non-default evidence-stage ordering as SEQUENCING-ORDER stress test — Intel-first declaration at S1 PRE boundary forces the rule to govern a real choice rather than confirm the default convention, demonstrating C-42 value concretely", "Antipattern-name annotations in invocation cell labels convert binary yes/no checks into antipattern-absence assertions — 'no hypothesis-first mode detected' makes the executor report failure-mode absence rather than generic rule satisfaction"]}
```
