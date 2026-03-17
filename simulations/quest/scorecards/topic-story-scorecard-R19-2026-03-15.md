---

# Quest Score — `topic-story` R19 (Rubric v18)

## Results

| Rank | Variation | Score | Key |
|------|-----------|-------|-----|
| **1** | **V-04** | **195.0 / 100%** | C-46 PASS + C-47 PASS on step-integration base — ceiling |
| **1** | **V-05** | **195.0 / 100%** | C-46 PASS + C-47 PASS on axiom grammar base — ceiling + candidate C-48 |
| 3 | V-01 | 192.5 / 97.5% | C-46 PASS (action-fused labels), C-47 FAIL (no template) |
| 3 | V-02 | 192.5 / 97.5% | C-47 PASS (fill-in template), C-46 FAIL (no named labels) |
| 5 | V-03 | 190.0 / 95% | C-46 FAIL (discriminator confirmed), C-47 FAIL |

**All essential pass: YES.** First 100% composite in `topic-story` round history.

---

## C-46 Discriminator Resolved

V-03 scores **190.0** (not 192.5). Confirmed: `Sub-step (before finalizing this beat):` fails C-46 because `Sub-step` names a type, not an act. The positional qualifier is present but the action is not encoded in the label name — the model must read prose after the colon for the action. C-46 requires action-name encoding fused into the label token. Generic label + positional proximity is insufficient.

## Key Findings

**ES-01 — C-46**: The label name must carry the action. `Pattern necessity test (apply before finalizing this beat):` passes. `Sub-step (before finalizing this beat):` fails. Proximity is not the same as encoding.

**ES-02 — C-47**: Structural template eliminates inference overhead. `Conditions: {finding or threshold...}` → model infers form. `Flip conditional: If [{...}] resolves as [{...}], the verdict holds. If [{...}] resolves as [{...}], the verdict changes to [{Adjacent verb}].` → model fills, does not infer.

**ES-03 — Candidate C-48 (V-05)**: Resolution path taxonomy per Beat 4 item (`SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH`) transforms Beat 4 from bare list to structured triage. V-04 hits same ceiling without it — confirming C-48 is a genuine v19 addition, not absorbed by existing criteria. v19 ceiling = 197.5.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-46 discriminator confirmed: generic Sub-step labels with positional qualifiers fail C-46 — the label NAME must encode the action (Pattern necessity test / Proportionality audit), not just the position; proximity is insufficient for the criterion's self-enforcing property", "Candidate C-48 — Beat 4 Named Resolution Path: tagging each UNRESOLVED item with SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH transforms Beat 4 from a bare list into a structured triage, distinguishing whether each open question is closable by more signal work, a targeted experiment, or requires a human decision that no amount of signal gathering can substitute"]}
```
er before verdict line. |
| V-04 | PASS | Same structure as V-01/V-02/V-03. |
| V-05 | PASS | Same structure; axiom grammar base does not alter output stream order. |

### C-41: Pattern necessity test

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | `Pattern necessity test (apply before finalizing this beat):` — named sub-step with explicit removal test condition. |
| V-02 | PASS | Inherited from V-03 R18 base: cross-signal scan + necessity test prose in Beat 3. |
| V-03 | PASS | `Sub-step (before finalizing this beat): confirm the dominant claim names a relationship or tension, not a collection of findings.` — substantively correct even with generic label. |
| V-04 | PASS | `Pattern necessity test (apply before finalizing this beat):` — identical to V-01. |
| V-05 | PASS | `Pattern necessity test (apply before finalizing this beat):` — identical to V-01/V-04. |

### C-42: Genre contract as structural BLUF enforcer

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | Inherited from V-03 R18 base: "Write an editorial synthesis" establishes genre frame. No ROLE/PART delimiters. EVALUATOR/AUTHOR labels are workflow phases, not output architectural labels. |
| V-02 | PASS | Same genre frame inherited. |
| V-03 | PASS | Same genre frame; `Sub-step` labels are internal to AUTHOR beats, not output delimiters. |
| V-04 | PASS | Same genre frame inherited. |
| V-05 | PASS | Axiom grammar base (V-04 R18) also carries genre frame. AXIOM framing is EVALUATOR-phase, not AUTHOR output labels. |

### C-43: Decision-flip conditional per uncertainty item

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | Beat 4 auto-transfer check; Beat 4.5 Conditions field prompts conditional — abstract form but C-43 requires both branches named, not a fill-in template (that is C-47). |
| V-02 | PASS | Flip conditional template explicitly maps both branches: "the verdict holds" / "the verdict changes to [{Adjacent verb}]." Both branches present. |
| V-03 | PASS | Beat 4.5 `Conditions:` abstract form, same as V-01. C-43 pass condition (both branches named) satisfied via E-8.5 derivation flow. |
| V-04 | PASS | Flip conditional template present (same as V-02). |
| V-05 | PASS | Flip conditional template present (same as V-02/V-04). |

### C-44: Dual depth coverage without architectural conflict

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | C-41 (necessity test named sub-step) + C-43 (conditional in Conditions field) both present. No ROLE/PART architectural conflict. |
| V-02 | PASS | C-41 (inherited prose) + C-43 (flip template) both present. No architectural conflict. |
| V-03 | PASS | Both present via prose/sub-step combination. No conflict. |
| V-04 | PASS | Both present: named sub-step + flip template. No conflict. |
| V-05 | PASS | Both present: named sub-step + flip template. No conflict. |

### C-45: Proportionality check as structural closing act of recommendation beat

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | `Proportionality audit (required final act before closing this beat):` — label name encodes "required final act," making it the structural closing act. |
| V-02 | PASS | Inherited from V-03 R18 base. |
| V-03 | PASS | `Sub-step (required before closing this beat): confirm claim weight is consistent with HIGH-weight evidence and trajectory.` — position marker "required before closing" is in the label; audit is final instruction. |
| V-04 | PASS | `Proportionality audit (required final act before closing this beat):` — identical to V-01. |
| V-05 | PASS | `Proportionality audit (required final act before closing this beat):` — identical to V-01/V-04. |

---

## New v18 Criteria — Decisive Evaluation

### C-46: Named sub-step labels as beat-internal positioning anchors

**Pass condition**: Label name encodes both the action AND the positional requirement as a single typographic unit. Failure modes: (a) prose without named label; (b) named label but positional marker absent from label body.

**Key discriminator for R19**: Does `Sub-step (before finalizing this beat):` pass — where position IS in the label but action is generic — or does C-46 require the action name fused into the label?

**Ruling**: C-46 requires "named sub-step labels" where "named" means the label carries a meaningful action identifier (the sub-step is named BY what it does, not by its type). `Sub-step` is a category type, not a name. `Pattern necessity test`, `Proportionality audit`, `Cross-signal scan` are names — they encode the action. The criterion states "The label encodes both action and position" and failure case includes labels that say only `Sub-step:` without positional qualifier. V-03's labels have the positional qualifier but retain the generic `Sub-step` type noun, satisfying half the criterion (position encoded) while failing the other half (action not encoded). V-03 is therefore a FAIL: `Sub-step (before finalizing):` is not a named sub-step label in the C-46 sense; it is a labeled type-category with a positional annotation.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | PASS | Beat 3: `Cross-signal scan (complete before drafting this beat):` [action=scan, position=before drafting] + `Pattern necessity test (apply before finalizing this beat):` [action=necessity test, position=before finalizing] + `Proportionality audit (required final act before closing this beat):` [action=proportionality audit, position=final act before closing]. Beat 4: `Auto-transfer check (apply before finalizing this beat):` [action=transfer check, position=before finalizing]. Beat 5: `Verdict alignment check (required before writing this beat):` [action=alignment check, position=before writing]. All labels encode action + position in a single typographic unit. |
| V-02 | FAIL | AUTHOR phase has no named sub-step labels. Beat 3 is plain prose: "**Beat 3**: Pattern synthesis. Dominant claim, boundary, trajectory." No label-level positioning mechanism present. |
| V-03 | FAIL | Uses `Sub-step (before finalizing this beat):` pattern throughout. Position IS encoded in the label. However, `Sub-step` is a generic category noun, not an action name. C-46 requires the label to name the action itself (what the sub-step does). `Sub-step (before finalizing):` fails because the label name does not encode the action — the action appears only in the prose after the colon. This confirms: label proximity of positional language is insufficient; the positional requirement must be fused into the action-naming label token. |
| V-04 | PASS | Identical named sub-step labels to V-01: `Cross-signal scan (complete before drafting this beat):`, `Pattern necessity test (apply before finalizing this beat):`, `Proportionality audit (required final act before closing this beat):`. Beat 4: `Completeness gate (apply before finalizing this beat):`. Beat 5: `Verdict alignment check (required before writing this beat):`. Full action + position encoding. |
| V-05 | PASS | Identical to V-04 for Beat 3 and Beat 5. Beat 4 `Completeness gate (apply before finalizing this beat):` with additional Resolution path requirement. Action + position fused in all labels. |

### C-47: Flip-conditional sentence template

**Pass condition**: Prompt furnishes a literal fill-in template with both resolution branches: `"If [{open question}] resolves as [{favorable}], the verdict holds. If [{open question}] resolves as [{unfavorable}], the verdict changes to [{Adjacent verb}]."` Abstract descriptions of the requirement fail.

| Variation | Score | Evidence |
|-----------|-------|----------|
| V-01 | FAIL | Beat 4.5 retains abstract Conditions field: `Conditions: {finding or threshold whose change would let Adjacent verb win}`. No fill-in template. Model must infer the template shape — abstract description of requirement, not structural form. |
| V-02 | PASS | Beat 4.5 contains literal fill-in template: `Flip conditional: If [{open question from Beat 4}] resolves as [{favorable outcome}], the verdict holds. If [{open question from Beat 4}] resolves as [{unfavorable outcome}], the verdict changes to [{Adjacent verb}].` Both branches present. Template provides the exact structural form; model fills placeholders without inferring shape. |
| V-03 | FAIL | Same abstract Conditions field as V-01. `Conditions: {finding or threshold whose change would let Adjacent verb win}`. No template. |
| V-04 | PASS | Same fill-in template as V-02: `Flip conditional: If [{open question from Beat 4}] resolves as [{favorable outcome}], the verdict holds. If [{open question from Beat 4}] resolves as [{unfavorable outcome}], the verdict changes to [{Adjacent verb}].` Both branches present and fully templated. |
| V-05 | PASS | Same fill-in template as V-02/V-04. Additionally, Beat 4 Resolution path tags give `{open question from Beat 4}` structured inputs for the flip conditional — SIGNAL_PATH/EXPERIMENT_PATH/DECIDE_PATH label each UNRESOLVED item, making the open-question placeholder tractable. |

---

## Candidate C-48 Assessment (V-05 only)

V-05 adds `Resolution path: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH` per Beat 4 UNRESOLVED item with a required `Completeness gate` that verifies count AND resolution path fill. This is a FORMAT constraint on Beat 4 items not covered by any existing criterion.

- C-06 (uncertainty specific): passes when the uncertainty names a decision-linked question. Does not require path classification.
- C-43 (decision-flip conditional): passes when both resolution branches are named per item. Does not require path classification.
- No existing criterion governs whether each UNRESOLVED item is tagged with its resolution mechanism.

**Candidate C-48 verdict**: Present and functional in V-05. Does not affect v18 score (not yet a criterion). Proposed for v19 as: "Beat 4 Named Resolution Path — each UNRESOLVED item carries a `Resolution path:` field classifying whether it is closable via additional signal work (SIGNAL_PATH), a targeted experiment (EXPERIMENT_PATH), or a human/team decision (DECIDE_PATH)."

---

## Per-Variation Score Summary

### C-08–C-39 Estimate (32 criteria)

All five variations inherit the V-03 R18 / V-04 R18 base. Per design context, R18 top variations score 190.0 against v18 (38 aspirational passing × 2.5 + base 95 = 190.0), implying 32/32 pass for C-08–C-39 when the EVALUATOR/AUTHOR protocol is fully instantiated. R19 variations add named sub-step labels (V-01/V-04/V-05) and flip-conditional template (V-02/V-04/V-05) on top of this base; neither change regresses C-08–C-39.

**C-08–C-39 estimate: 32/32 for all five variations.**

### Composite Scores

| Variation | C-08–C-39 | C-40–C-45 | C-46 | C-47 | Total /40 | Composite | Point score |
|-----------|-----------|-----------|------|------|-----------|-----------|-------------|
| V-01 | 32/32 | 6/6 | PASS | FAIL | 39/40 | **97.5%** | **192.5** |
| V-02 | 32/32 | 6/6 | FAIL | PASS | 39/40 | **97.5%** | **192.5** |
| V-03 | 32/32 | 6/6 | FAIL | FAIL | 38/40 | **95.0%** | **190.0** |
| V-04 | 32/32 | 6/6 | PASS | PASS | 40/40 | **100%** | **195.0** |
| V-05 | 32/32 | 6/6 | PASS | PASS | 40/40 | **100%** | **195.0** |

Point score formula: base 95 + (aspirational passes × 2.5).

---

## Rankings

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 | **V-04** | 195.0 / 100% | C-46 + C-47 on step-integration base — ceiling path confirmed |
| 1 | **V-05** | 195.0 / 100% | C-46 + C-47 on axiom grammar base — ceiling confirmed independently; candidate C-48 present |
| 3 | V-01 | 192.5 / 97.5% | C-46 PASS (action-fused labels); C-47 FAIL (no template) |
| 3 | V-02 | 192.5 / 97.5% | C-47 PASS (fill-in template); C-46 FAIL (no named labels) |
| 5 | V-03 | 190.0 / 95% | C-46 FAIL (discriminator confirmed: generic `Sub-step` label fails); C-47 FAIL |

**All essential pass: YES.** Ceiling reached by V-04 and V-05 (40/40 aspirational). First 100% composite in `topic-story` round history.

---

## C-46 Discriminator Resolution

V-03 scores 190.0 (not 192.5), resolving the discriminator definitively:

**C-46 requires the positional requirement fused into the action-naming label token.** Generic `Sub-step (before finalizing):` fails because `Sub-step` names a type, not an act. The model reads the position but must read separate prose for the action. `Pattern necessity test (apply before finalizing this beat):` passes because the label name encodes the act (necessity test) and the position is fused into the same typographic unit — the model reads both simultaneously.

Implication: label proximity is insufficient. The action and position must be collapsed into the label NAME itself. This confirms the criterion's intent that "the label encodes both action and position."

---

## V-04 vs V-05 Architecture Check

Both V-04 (step-integration base, V-03 R18) and V-05 (axiom grammar base, V-04 R18) reach ceiling when C-46 and C-47 are added. The two architectures are ceiling-equivalent for v18 criteria:

- **Step-integration** (V-04): Writing `Vector status: REVISED` in step b IS the firing of E-8.5 (FIRING RULE). Sequential causal chain.
- **Axiom grammar** (V-05): Declaring `Vector status: REVISED` IS E-8.5 constitutively (AXIOM). Constitutive identity, not causation.

Both reach 40/40 aspirational under v18. The C-46/C-47 mechanism is orthogonal to the C-38/C-39 architecture — named sub-step labels and flip-conditional templates operate in the AUTHOR phase; VECTOR-STATUS semantics operate in the mid-draft re-sealing protocol.

---

## Excellence Signals from V-04 and V-05

**ES-01 — C-46 architecture: action-name encoding is required, proximity is insufficient**
The R19 discriminator test (V-03 at 190.0 vs V-01/V-04 at 192.5/195.0) confirms: a beat-internal sub-step achieves C-46 PASS only when the label NAME encodes the action. `Pattern necessity test (apply before finalizing this beat):` — the model reads "what to do" (necessity test) and "when to do it" (before finalizing) in one token sequence. `Sub-step (before finalizing this beat):` — the model reads "when" but must search prose for "what." C-46 fires on the LABEL NAME carrying both, not on positional language appearing anywhere near a label.

**ES-02 — C-47 architecture: structural form eliminates inference overhead**
Replacing `Conditions: {finding or threshold...}` with:
```
Flip conditional:
  If [{open question from Beat 4}] resolves as [{favorable outcome}], the verdict holds.
  If [{open question from Beat 4}] resolves as [{unfavorable outcome}], the verdict
    changes to [{Adjacent verb}].
```
Gives the model the structural form directly. Without the template, the model must infer: what is a "conditional," how many branches, what placeholders to use, how to express "the verdict holds" vs "changes." With the template, all inference is eliminated — only filling is required.

**ES-03 — Candidate C-48: Resolution path taxonomy per Beat 4 item (V-05 only)**
V-05 adds `Resolution path: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH` per UNRESOLVED item. Three categories:
- **SIGNAL_PATH**: closable by gathering more signal artifacts in existing namespaces
- **EXPERIMENT_PATH**: closable by running a targeted prototype, test, or proof-of-concept
- **DECIDE_PATH**: closable only by a human or team decision; no signal or experiment can close it

This transforms Beat 4 from a bare UNRESOLVED list into a structured triage. The taxonomy makes explicit whether the recommendation can be unblocked by the team itself (SIGNAL_PATH), by planned experimentation (EXPERIMENT_PATH), or requires a stakeholder decision to resolve (DECIDE_PATH). The `Completeness gate` requires every item to have a Resolution path filled before the beat closes.

---

## v19 Target

**Candidate C-48**: Beat 4 Named Resolution Path — each UNRESOLVED item must carry a `Resolution path:` field. Proposed pass condition: each Beat 4 item includes `Resolution path: SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH` with the applicable value filled, and the beat includes a completeness gate verifying that every UNRESOLVED item from E-5 has a Resolution path filled before the beat closes.

V-05 demonstrates the full mechanism. V-04 (without candidate C-48) scores the same ceiling (195.0) — confirming candidate C-48 is not covered by any existing criterion and would be a genuine v19 addition.

**v19 ceiling**: 197.5 (if C-48 added: 41 aspirational × 2.5 = 102.5 + base 95 = 197.5).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-46 discriminator confirmed: generic Sub-step labels with positional qualifiers fail C-46 — the label NAME must encode the action (Pattern necessity test / Proportionality audit), not just the position; proximity is insufficient for the criterion's self-enforcing property", "Candidate C-48 — Beat 4 Named Resolution Path: tagging each UNRESOLVED item with SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH transforms Beat 4 from a bare list into a structured triage, distinguishing whether each open question is closable by more signal work, a targeted experiment, or requires a human decision that no amount of signal gathering can substitute"]}
```
