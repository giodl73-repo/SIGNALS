Written to `simulations/quest/scorecards/prove-synthesize-scorecard-R5-2026-03-14.md`.

---

## prove-synthesize — Round 5 Scorecard

### Scores

| Variation | Total | Status |
|-----------|-------|--------|
| V-05 | **125.0** | GOLDEN (max) |
| V-04 | **122.5** | GOLDEN |
| V-01 | **115.0** | GOLDEN |
| V-02 | **115.0** | GOLDEN |
| V-03 | **115.0** | GOLDEN |

All five Golden. All essential pass.

---

### Aspirational Criteria Matrix

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 through C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 (role prohibitions) | FAIL | FAIL | PASS | PASS | PASS |
| C-17 (record-specific diagnosis) | FAIL | PASS | FAIL | PASS | PASS |
| C-18 (register-word-first) | PASS | PASS | PASS | PASS | PASS |
| C-19 (frontmatter at open) | PASS | FAIL | FAIL | FAIL | PASS |
| C-20 (phase-sequenced filling) | PASS | FAIL | FAIL | PASS | PASS |
| C-21 (schema-traceable diagnosis) | FAIL | PASS | FAIL | PASS | PASS |
| C-22 (dual-layer register-word) | FAIL | FAIL | PASS | PASS | PASS |

---

### Three Calibration Questions — Answered

**Q1 (C-20 vs "fill now"):** "Fill now" instructions are insufficient. Per-field NOT: prohibitions make premature and deferred filling named violations with bounded windows at both ends. C-20 requires the per-field NOT: gate.

**Q2 (C-21 vs "derivable from"):** "Derivable from inventory" satisfies C-17 (evaluable). Schema field citation by name:value satisfies C-21 (falsifiable in one lookup without re-reading). These are distinct criteria.

**Q3 (C-22 — pre-flight vs DETERMINATION SEAL):** Both V-03 (PRE-FLIGHT) and V-04 (DETERMINATION SEAL explicit NOT: gate naming positional failure) pass C-22. Both satisfy dual-layer enforcement. PRE-FLIGHT is the sharpened form (C-25 candidate) — gate encountered before failure can occur; DETERMINATION SEAL gate is encountered alongside the commitment format.

---

### Excellence Signals (V-05)

1. **Triple enforcement layering** — per-field frontmatter prohibitions + phase-exit attestations + structural gate items. No constraint stated once.
2. **Frontmatter as 9-field compliance ledger** — tracks quality vectors (record_specific_antipattern, role_foreclusion_explicit, preflight_confirmed) enabling full audit from frontmatter alone.
3. **INVENTORY SCHEMA as shared vocabulary** — 5 named fields propagate from SURVEYOR to RECORD DIAGNOSIS to confidence calibration to frontmatter boolean tracking.
4. **PRE-FLIGHT expanded to structural audit** — not just register-word gate; verifies RECORD DIAGNOSIS schema citation before JUDGE begins.

---

### V6 Candidates

| Candidate | Mechanism |
|-----------|-----------|
| C-23 | Phase-boundary transition gates — fill window bounded at both ends with named violations |
| C-24 | Schema-quoted diagnosis — RECORD DIAGNOSIS falsifiable in one lookup by field:value citation |
| C-25 | Pre-JUDGE pre-flight block — register-word gate encountered before commitment sentence is written |

All three confirmed by independent variations; V-04 confirms C-23+C-24 compose without C-19; V-05 confirms all three compose with full R4 inheritance.

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["triple enforcement layering: per-field NOT: prohibitions in frontmatter + phase-boundary attestations at phase exits + gate items in structural gates -- no structural constraint stated once", "frontmatter as multi-dimensional compliance ledger tracking 9 fields including quality vectors (record_specific_antipattern, role_foreclusion_explicit, preflight_confirmed) enabling reader audit without full artifact read", "INVENTORY SCHEMA creates addressable named vocabulary propagating from SURVEYOR to RECORD DIAGNOSIS to confidence calibration to frontmatter boolean tracking", "PRE-FLIGHT block expanded beyond register-word gate to full structural audit: verifies C-21 compliance (schema citation present) as pre-condition before JUDGE begins"]}
```
 C-19 | **PASS** | FRONTMATTER DECLARATIONS block opens the artifact with machine-readable fields: signal_count, adversary_pre_determination, answer, confidence, register_word_used, not_first_gates. Booleans require commitment before prose begins. |
| C-20 | **PASS** | Per-field NOT: prohibitions for premature AND deferred fill: "NOT: signal_count filled before any SURVEYOR content is written. NOT: signal_count filled after ADVERSARY content begins." Same dual-gate for adversary_pre_determination, answer, register_word_used, not_first_gates. This is the new R5 mechanism -- each field's filling window is bounded at both ends. R4 V-03 base had frontmatter at open but no per-field phase gates (batch-fillable at start); V-01 per-field NOT: prohibitions make sequential filling a named violation, not just a missed instruction. C-20 fires. |
| C-21 | **FAIL** | No INVENTORY SCHEMA. No RECORD DIAGNOSIS citing schema field values. Adversarial challenge paragraphs lack any cross-referenceable inventory structure. Failure mode in paragraph 3 cannot be traced to SURVEYOR-inventoried properties because no schema fields exist to trace. |
| C-22 | **FAIL** | DETERMINATION SEAL gate: "NOT: DETERMINATION: is absent from the opening sentence -- the register word must commit before reasoning follows." This forecloses absence but does not name the register-word-placement failure mode by name. The failure mode ("Our final DETERMINATION is:", "Based on the foregoing, DETERMINATION:") is not named as a violation. A writer who produces "Based on the evidence, DETERMINATION: YES" has DETERMINATION: in the opening sentence but not as the first word. The absence-gate does not foreclose positional placement. |

**Aspirational subtotal: 10 x 2.5 = 25.0**

**V-01 Composite: 60 + 30 + 25 = 115.0 -- GOLDEN**

---

### V-02: SURVEYOR INVENTORY SCHEMA with Schema-Cited RECORD DIAGNOSIS

**Axis:** SURVEYOR phase produces a named INVENTORY SCHEMA (signal_count, method_set, convergence_pattern, dominant_signal, coverage_gaps); RECORD DIAGNOSIS must cite schema field names and exact values. Single-axis C-21 sharpened. Base: R4 V-02 (phase titles PHASE 1-5, structured diagnosis, no role labels, no frontmatter at open).

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: format enforced; "Open with DETERMINATION: and the answer word." |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with rationale paragraph. |
| C-03 | **PASS** | PHASE 4: EVIDENCE HIERARCHY with ranked argument prose paragraphs; signals must trace to Phase 1 inventory. |
| C-04 | **PASS** | PHASE 2: ADVERSARIAL CHALLENGE structurally before PHASE 3: DETERMINATION. |
| C-05 | **PASS** | DETERMINATION issued after adversarial challenge and RECORD DIAGNOSIS -- judgment, not list. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | PHASE 5: PRINCIPLES with declarative "X implies Y" format required. |
| C-07 | **PASS** | PHASE 5: OPEN QUESTIONS with specific question, undetermined-reason, and next step. |
| C-08 | **PASS** | CONFIDENCE rationale paragraph required by DETERMINATION GATE. |

**Recommended subtotal: 30/30**

#### Aspirational (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | "This is a ranked argument, not a ranked list." Comparative paragraphs with "why this signal over rank 2" required. |
| C-10 | **PASS** | "State this mandate in your opening paragraph." Standalone mandate explicit. |
| C-11 | **PASS** | Multiple NOT: failure-mode gates throughout. ADVERSARIAL CHALLENGE GATE names "generic anti-pattern" as failure mode; EVIDENCE GATE names "table with why column" as failure mode. |
| C-12 | **PASS** | "Write argumentative sections in prose paragraphs, not tables or bullet lists." EVIDENCE GATE forecloses tables. |
| C-13 | **PASS** | All gate items open with NOT: before Positive condition. |
| C-14 | **PASS** | DETERMINATION: as sentence-level commitment. |
| C-15 | **PASS** | "NOT: this phase runs after the determination -- counter-evidence selected post-verdict is selection bias." Pre-commitment enforced. |
| C-16 | **FAIL** | Phase labels are PHASE 1, PHASE 2, PHASE 3 -- descriptive phase titles, not procedural identity labels. "PHASE 3: DETERMINATION" does not assign a JUDGE identity; no prohibition statements. No "An ADVERSARY cannot advocate" equivalent. Titles name steps, not roles, and provide nothing to foreclose. |
| C-17 | **PASS** | RECORD DIAGNOSIS template explicitly present with schema field citation requirement: "Given this record's [INVENTORY SCHEMA field: exact value] and [INVENTORY SCHEMA field: exact value]... the most likely failure mode is [specific failure mode]." NOT: gate forecloses generic diagnosis. NOT: gate forecloses paraphrase without field citation. Diagnosis is falsifiable by cross-reference to INVENTORY SCHEMA. Record-specific anti-pattern declaration present and structurally enforced. |
| C-18 | **PASS** | DETERMINATION GATE: "NOT: DETERMINATION: is absent from the opening sentence." DETERMINATION: [YES/NO/MAYBE] opens judgment paragraph. |
| C-19 | **FAIL** | No frontmatter block at document open. Frontmatter fields listed at artifact write-out instructions at end. Machine-readable declarations are retroactive, not pre-commitment. |
| C-20 | **FAIL** | No frontmatter at open, so no phase-sequenced boolean filling. Frontmatter appears at artifact end. Fields cannot be phase-sequenced when they are filled retroactively at output time. |
| C-21 | **PASS** | INVENTORY SCHEMA with 5 named fields produced by SURVEYOR. RECORD DIAGNOSIS must cite "field names and exact values" with NOT: gates foreclosing paraphrase: "NOT: the record diagnosis names a generic anti-pattern... that does not cite the INVENTORY SCHEMA by field name." Positive condition: "a reader can falsify the diagnosis by (a) locating the named INVENTORY SCHEMA fields in Phase 1, (b) confirming the cited values match exactly." Schema citation makes the diagnosis reader-falsifiable in a single lookup. C-21 fires. |
| C-22 | **FAIL** | DETERMINATION GATE: "NOT: DETERMINATION: is absent from the opening sentence -- register word must commit before reasoning follows." Same absence-gate pattern as V-01. Does not explicitly name the positional failure mode ("Our final DETERMINATION is:", "Based on the foregoing, DETERMINATION:"). A writer who places DETERMINATION mid-sentence satisfies the absence test but violates register-word-first. The instruction-level gate targets the wrong failure mode. |

**Aspirational subtotal: 10 x 2.5 = 25.0**

**V-02 Composite: 60 + 30 + 25 = 115.0 -- GOLDEN**

---

### V-03: PRE-JUDGE PRE-FLIGHT Block

**Axis:** A PRE-JUDGE PRE-FLIGHT gate block is inserted between ADVERSARY COMPLETE and the JUDGE section; the register-word NOT: condition appears in this block before the commitment sentence is written. Single-axis C-22 sharpened. Base: R4 V-01 (role labels + explicit prohibition statements, standard adversarial challenge without INVENTORY SCHEMA, no frontmatter at open).

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: [YES/NO/MAYBE] format; PRE-FLIGHT further reinforces register-word-first before judgment begins. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with rationale paragraph. |
| C-03 | **PASS** | ADVOCATE section with named PRIMARY/SECONDARY/TERTIARY evidence; comparative paragraphs required. |
| C-04 | **PASS** | ADVERSARY phase before PRE-JUDGE PRE-FLIGHT before JUDGE. Double structural barrier to post-determination counter-evidence. |
| C-05 | **PASS** | JUDGE role prohibition ("A JUDGE does not hedge") enforces commitment. Judgment against ADVERSARY challenge required. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | SCHOLAR: PRINCIPLES AND OPEN RECORD with declarative Holdings. |
| C-07 | **PASS** | Open Record with specific question, undetermined-reason, next action. |
| C-08 | **PASS** | CONFIDENCE rationale paragraph required by DETERMINATION SEAL. |

**Recommended subtotal: 30/30**

#### Aspirational (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | "This is a ranked argument, not a ranked list." EVIDENCE GATE forecloses "table with why column." |
| C-10 | **PASS** | "State this mandate in your opening paragraph." |
| C-11 | **PASS** | PRE-FLIGHT CHECKLIST items and ADVERSARY GATE explicitly name failure modes: "NOT: adversarial challenge is absent or generic ('evidence is limited')." |
| C-12 | **PASS** | "Write argumentative sections in prose paragraphs, not tables or bullet lists." |
| C-13 | **PASS** | All gate items open with NOT: before positive condition. |
| C-14 | **PASS** | DETERMINATION: as sentence-level declaration. PRE-FLIGHT further enforces. |
| C-15 | **PASS** | "NOT: this section is placed after the DETERMINATION." ADVERSARY COMPLETE marker before PRE-FLIGHT before JUDGE. |
| C-16 | **PASS** | Explicit role prohibitions present: "A SURVEYOR inventories. A SURVEYOR does not evaluate, compare, rank, or reach conclusions about signal quality." "An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, surface supporting evidence, or assist the JUDGE." "A JUDGE rules. A JUDGE does not hedge, equivocate, or defer to signal ambiguity. Hedging in the JUDGE phase is a procedural breach." Identity labels AND foreclusion statements present for all three phases. |
| C-17 | **FAIL** | Paragraph 3 of ADVERSARY instructs "Name one failure mode this synthesis must avoid -- not a generic warning, but one that fits this investigation's signal set." Instruction-level nudge toward record-specificity, not structural enforcement. No RECORD DIAGNOSIS template, no INVENTORY SCHEMA to derive from. A writer following the instruction produces a record-specific failure mode, but one that cannot be verified by cross-reference -- there is no schema to check the derivation against. C-17 requires structural derivation; V-03 provides only an instruction to derive. |
| C-18 | **PASS** | PRE-FLIGHT REGISTER-WORD GATE + DETERMINATION: [YES/NO/MAYBE] format both enforce register-word-first. |
| C-19 | **FAIL** | No frontmatter block at document open. Frontmatter fields listed at artifact write-out at end. Pre-commitment boolean declarations are absent from the document's structural opening. |
| C-20 | **FAIL** | No frontmatter at open. Phase-sequenced boolean filling cannot occur without a frontmatter block that is filled progressively. Fields are specified at end, not phase-gated during writing. |
| C-21 | **FAIL** | No INVENTORY SCHEMA. ADVERSARY paragraphs challenge the record but have no schema fields to cite. Failure mode diagnosis in paragraph 3 cannot be cross-referenced to a structured inventory -- the SURVEYOR phase produces a record count only, not a named schema with addressable fields. |
| C-22 | **PASS** | PRE-JUDGE PRE-FLIGHT REGISTER-WORD GATE: "NOT: the commitment sentence begins with any word other than the register word. 'Our final DETERMINATION is:' violates this gate before you write it. 'Based on the foregoing, DETERMINATION:' violates this gate before you write it." Explicitly names the positional failure mode with examples. Positioned BEFORE the JUDGE section -- the prohibition is encountered before the failure mode can occur. Dual-layer: output format (DETERMINATION: [YES/NO/MAYBE]) + instruction-level NOT: gate naming placement failure by name. C-22 fires. |

**Aspirational subtotal: 10 x 2.5 = 25.0**

**V-03 Composite: 60 + 30 + 25 = 115.0 -- GOLDEN**

---

### V-04: Phase-Gate Attestations + INVENTORY SCHEMA Citation (Combo)

**Axes:** Inline phase-transition NOT: gates at each phase boundary (C-20 sharpened, without frontmatter at open) + SURVEYOR INVENTORY SCHEMA with schema-cited RECORD DIAGNOSIS (C-21 sharpened). C-22 at DETERMINATION SEAL level (explicit NOT: gate naming positional failure mode). Base: R4 V-04 (C-16 + C-17 + C-18, no C-19).

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: [YES/NO/MAYBE] format enforced. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with rationale paragraph. |
| C-03 | **PASS** | ADVOCATE section with PRIMARY/SECONDARY/TERTIARY prose paragraphs arguing comparative weight. |
| C-04 | **PASS** | ADVERSARY phase before JUDGE; structural NOT: gate enforces pre-placement. |
| C-05 | **PASS** | JUDGE issues determination against both ADVERSARY challenge and RECORD DIAGNOSIS. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | SCHOLAR: PRINCIPLES AND OPEN RECORD with declarative Holdings. |
| C-07 | **PASS** | Open Record with specific question, next investigative action. |
| C-08 | **PASS** | CONFIDENCE rationale required by DETERMINATION SEAL. |

**Recommended subtotal: 30/30**

#### Aspirational (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | "This is a ranked argument, not a ranked list." Comparative paragraphs required. |
| C-10 | **PASS** | Standalone mandate in opening paragraph. |
| C-11 | **PASS** | Failure modes named by name throughout: "table with why column," "generic anti-pattern," "paraphrase without field names." |
| C-12 | **PASS** | Argumentative sections required as prose; EVIDENCE GATE forecloses tables. |
| C-13 | **PASS** | All gate items NOT:-first throughout. |
| C-14 | **PASS** | DETERMINATION: as sentence-level declaration. |
| C-15 | **PASS** | "NOT: this section is placed after the DETERMINATION." ADVERSARY structurally before JUDGE. |
| C-16 | **PASS** | Explicit role prohibitions: "A SURVEYOR inventories. A SURVEYOR does not evaluate, compare, rank, or reach conclusions... Evaluation by a SURVEYOR is a procedural breach regardless of its accuracy." "An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis... Advocacy in the ADVERSARY phase is a procedural breach." "A JUDGE rules. A JUDGE does not hedge, equivocate, or defer. Hedging in the JUDGE phase is a procedural breach." Three-phase foreclusion. |
| C-17 | **PASS** | RECORD DIAGNOSIS template: "Given this record's [INVENTORY SCHEMA field: exact value] and [INVENTORY SCHEMA field: exact value]..." Two NOT: gates foreclose generic diagnosis AND paraphrase without citation. Schema-valued derivation required. Falsifiable by locating cited schema fields and confirming exact values match. |
| C-18 | **PASS** | DETERMINATION SEAL: "NOT: the register word appears after introductory language ('Our final DETERMINATION is:', 'Based on the foregoing, DETERMINATION:')." Register-word-first enforced. |
| C-19 | **FAIL** | No frontmatter block at document open. Frontmatter fields specified at bottom ("Write artifact: ... Frontmatter: skill, topic, date, answer, confidence, signal_count, adversary_pre_determination..."). Machine-readable pre-commitment declarations absent from document open. |
| C-20 | **PASS** | Inline phase-transition NOT: conditions enforce sequential filling even without frontmatter at open: "SURVEYOR COMPLETE. NOT: ADVERSARY begins before INVENTORY SCHEMA is produced and signal_count is set in frontmatter." "ADVERSARY COMPLETE. NOT: JUDGE begins before adversary_pre_determination is set true in frontmatter." "DETERMINATION SEALED. NOT: ADVOCATE begins before determination_sealed is set true in frontmatter." Sequential determinability enforced at each phase boundary: a field cannot be truthfully set before its phase completes. Mechanism differs from V-01 (frontmatter-at-open with per-field NOT: conditions) but achieves the same structural sequencing property. C-20 fires. |
| C-21 | **PASS** | INVENTORY SCHEMA (signal_count, method_set, convergence_pattern, dominant_signal, coverage_gaps) produced by SURVEYOR. RECORD DIAGNOSIS must cite schema field names with exact values. NOT: gates at two levels: "NOT: the record diagnosis names a generic anti-pattern... that does not cite INVENTORY SCHEMA field names with their exact values." AND "NOT: the record diagnosis paraphrases the INVENTORY SCHEMA without citing field names and exact values -- paraphrase cannot be falsified in a single lookup." Positive condition: reader can falsify by locating cited fields and confirming values match exactly. C-21 fires. |
| C-22 | **PASS** | DETERMINATION SEAL: "NOT: the register word appears after introductory language ('Our final DETERMINATION is:', 'Based on the foregoing, DETERMINATION:') -- a register word not first in its sentence allows hedging to precede the commitment point. Positive condition: DETERMINATION: is the first word of the commitment sentence." Explicitly names the positional failure mode with examples. Dual-layer: output format (DETERMINATION: [YES/NO/MAYBE]) + instruction-level NOT: gate naming placement failure by name. C-22 fires at standard (DETERMINATION SEAL) level; PRE-FLIGHT mechanism absent (C-25 candidate not present). |

**Aspirational subtotal: 13 x 2.5 = 32.5**

**V-04 Composite: 60 + 30 + 32.5 = 122.5 -- GOLDEN**

---

### V-05: Full Combo -- All Three Sharpened Mechanisms + R4 V-05 Inheritance

**Axes:** Per-field phase-gate NOT: conditions (C-20 sharpened) + SURVEYOR INVENTORY SCHEMA with schema-cited RECORD DIAGNOSIS (C-21 sharpened) + PRE-JUDGE PRE-FLIGHT block with register-word gate before commitment sentence (C-22 sharpened). Full R4 V-05 inheritance: role prohibitions (C-16), structured RECORD DIAGNOSIS (C-17), register-word-first format (C-18), frontmatter at open (C-19).

#### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | DETERMINATION: [YES/NO/MAYBE] format with PRE-FLIGHT enforcement before judgment begins. |
| C-02 | **PASS** | CONFIDENCE: [N]/100 with rationale paragraph; RECORD DIAGNOSIS informs confidence ceiling. |
| C-03 | **PASS** | ADVOCATE section with PRIMARY/SECONDARY/TERTIARY prose paragraphs arguing comparative weight. |
| C-04 | **PASS** | ADVERSARY phase before PRE-FLIGHT before JUDGE -- double structural barrier. |
| C-05 | **PASS** | JUDGE role prohibition enforces commitment. Determination addresses both ADVERSARY challenge and RECORD DIAGNOSIS. |

**Essential subtotal: 60/60**

#### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | SCHOLAR: Holdings with declarative principles that generalize beyond this hypothesis. |
| C-07 | **PASS** | Open Record with specific question, undetermined-reason, next investigative action. |
| C-08 | **PASS** | CONFIDENCE rationale required; DETERMINATION SEAL verifies rationale present. |

**Recommended subtotal: 30/30**

#### Aspirational (2.5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | "This is a ranked argument, not a ranked list." EVIDENCE GATE names table-as-argument failure mode. Comparative paragraphs with "why primary over secondary" required. |
| C-10 | **PASS** | Standalone mandate explicit in opening paragraph. Artifact write-out instruction reinforces: "a reader with no access to the investigation signals must understand the determination, the evidence basis, the pre-determination challenge, and what to do next from this document alone." |
| C-11 | **PASS** | Failure modes named throughout: "table with why column," "generic anti-pattern," "paraphrase without citation," "commitment sentence not register-word-first." Anti-patterns foreclosed by name at multiple structural points. |
| C-12 | **PASS** | "Write argumentative sections in prose paragraphs, not tables or bullet lists." EVIDENCE GATE forecloses tables. |
| C-13 | **PASS** | All gate items NOT:-first throughout all phases. Verified across SURVEYOR GATE, ADVERSARY GATE, DETERMINATION SEAL, EVIDENCE GATE, and SCHOLAR phase. |
| C-14 | **PASS** | DETERMINATION: as sentence-level declaration. PRE-FLIGHT positions this enforcement before the JUDGE section begins. |
| C-15 | **PASS** | "NOT: this section is placed after the DETERMINATION." ADVERSARY COMPLETE + PRE-FLIGHT before JUDGE. |
| C-16 | **PASS** | Full role prohibition statements for all three phases: SURVEYOR ("does not evaluate, compare, rank, or reach conclusions... Evaluation by a SURVEYOR is a procedural breach regardless of its accuracy"), ADVERSARY ("does not advocate for the hypothesis, surface supporting evidence, or assist the JUDGE's determination. Advocacy in the ADVERSARY phase is a procedural breach"), JUDGE ("does not hedge, equivocate, or defer to signal ambiguity. Hedging or equivocation in the JUDGE phase is a procedural breach"). |
| C-17 | **PASS** | RECORD DIAGNOSIS template requiring INVENTORY SCHEMA field citation: "Given this record's [INVENTORY SCHEMA field: exact value] and [INVENTORY SCHEMA field: exact value]..." Two NOT: gates foreclose generic diagnosis and paraphrase. Falsifiability condition explicit: "(a) locating the cited INVENTORY SCHEMA fields in the SURVEYOR section, (b) confirming the cited values match exactly, and (c) judging whether the causal link is plausible." record_specific_antipattern boolean tracks compliance. |
| C-18 | **PASS** | PRE-FLIGHT REGISTER-WORD GATE + DETERMINATION SEAL both enforce register-word-first. Dual-site enforcement. |
| C-19 | **PASS** | FRONTMATTER DECLARATIONS block at document open with 9 fields: signal_count, adversary_pre_determination, answer, confidence, register_word_used, not_first_gates, record_specific_antipattern, role_foreclusion_explicit, preflight_confirmed. Multi-dimensional compliance record. Artifact write-out instructions: "The frontmatter is a compliance record, not formatting metadata." |
| C-20 | **PASS** | Per-field NOT: prohibitions in frontmatter block: "NOT: signal_count filled before any SURVEYOR content is written. NOT: signal_count filled after ADVERSARY content begins." Same dual-gate for adversary_pre_determination, answer, register_word_used. Plus phase-boundary attestations: "SURVEYOR COMPLETE. Set signal_count: [N] in frontmatter now. NOT: ADVERSARY begins with signal_count unset in frontmatter." Dual enforcement layers: per-field prohibitions bound the fill window at both ends; phase-exit attestations confirm the boundary was respected before advancing. Maximum sequential determinability. |
| C-21 | **PASS** | INVENTORY SCHEMA (all 5 fields) + RECORD DIAGNOSIS with schema-field citation requirement. Two NOT: gates in ADVERSARY GATE: "NOT: RECORD DIAGNOSIS fails to cite INVENTORY SCHEMA field names with exact values." "NOT: RECORD DIAGNOSIS names a failure mode without explaining why the cited schema values produce it." record_specific_antipattern boolean in frontmatter tracks compliance. SURVEYOR GATE verifies schema produced. Chain: schema produced -> cited in diagnosis -> causal link explained -> tracked in frontmatter boolean. |
| C-22 | **PASS** | PRE-JUDGE PRE-FLIGHT REGISTER-WORD GATE: "NOT: the commitment sentence begins with any word other than the register word. 'Our final DETERMINATION is:' violates this gate before you write it. 'Based on the foregoing, DETERMINATION:' violates this gate before you write it. 'The record supports a DETERMINATION of:' violates this gate before you write it." Positioned BEFORE the JUDGE section -- the prohibition is encountered before the failure mode can occur. DETERMINATION SEAL additionally contains explicit NOT: gate. preflight_confirmed boolean tracks completion. Three-layer enforcement: PRE-FLIGHT gate (pre-phase) + DETERMINATION SEAL NOT: gate (post-phase check) + output format (DETERMINATION: [YES/NO/MAYBE]). |

**Aspirational subtotal: 14 x 2.5 = 35.0**

**V-05 Composite: 60 + 30 + 35 = 125.0 -- GOLDEN (maximum)**

---

### Round 5 Summary

| Variation | Essential | Recommended | Aspirational | Total | Status |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 60 | 30 | 25.0 (10/14) | **115.0** | GOLDEN |
| V-02 | 60 | 30 | 25.0 (10/14) | **115.0** | GOLDEN |
| V-03 | 60 | 30 | 25.0 (10/14) | **115.0** | GOLDEN |
| V-04 | 60 | 30 | 32.5 (13/14) | **122.5** | GOLDEN |
| V-05 | 60 | 30 | 35.0 (14/14) | **125.0** | GOLDEN (max) |

**Rank:** V-05 > V-04 > V-01 = V-02 = V-03

---

### Aspirational Criteria Matrix

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | FAIL | FAIL | PASS | PASS | PASS |
| C-17 | FAIL | PASS | FAIL | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | FAIL | FAIL | FAIL | PASS |
| C-20 | PASS | FAIL | FAIL | PASS | PASS |
| C-21 | FAIL | PASS | FAIL | PASS | PASS |
| C-22 | FAIL | FAIL | PASS | PASS | PASS |

---

### Three R5 Calibration Questions -- Answered

**Q1: Does C-20 require per-field NOT: prohibitions, or do "fill now" instructions already represent the strongest form?**

V-01 per-field NOT: prohibitions PASS C-20 where R4 V-03 "fill now" instructions FAIL. The distinction: "fill now" instructs the writer when to fill but does not name premature or deferred filling as a violation. A compliant writer follows the instruction; a non-compliant writer ignores it with no named consequence. The per-field NOT: gate makes premature filling a named procedural breach ("NOT: signal_count filled before any SURVEYOR content is written") and deferred filling a named retroactive declaration ("NOT: signal_count filled after ADVERSARY content begins"). The gate changes the failure mode from instruction-ignorable to structurally-foreclosed. **C-20 requires per-field NOT: prohibitions -- "fill now" alone is insufficient.**

**Q2: Does C-21 require schema field citation by name-and-value, or does "derivable from the inventory" already represent the strongest form?**

V-02 schema citation PASSES C-21 while "derivable from inventory" (C-17 mechanism) is evaluable but not falsifiable. "Derivable from" requires a reader to re-read the inventory and judge whether the derivation is plausible -- evaluation, not verification. "Cited by field name and exact value" allows a reader to locate the cited field, compare the exact value in one lookup, and confirm or falsify without re-reading inventory prose. The RECORD DIAGNOSIS is falsified if any cited value differs from the INVENTORY SCHEMA. **C-21 requires schema field citation -- "derivable from inventory" satisfies C-17, not C-21.**

**Q3: Does C-22 require the register-word gate to precede the JUDGE phase, or does the DETERMINATION SEAL gate already represent the strongest form?**

Both V-03 (PRE-FLIGHT) and V-04 (DETERMINATION SEAL explicit NOT: gate) pass C-22 -- both provide instruction-level NOT: gates naming the positional failure mode. The PRE-FLIGHT mechanism is the sharpened form (C-25 candidate): the gate is encountered BEFORE the commitment sentence can be written, not alongside the format template. V-04 DETERMINATION SEAL gate appears inside the structural block that also contains **DETERMINATION: [YES/NO/MAYBE]** -- a writer encounters the prohibition and the format simultaneously. PRE-FLIGHT positions the gate one full structural section earlier. **C-22 is satisfied by the DETERMINATION SEAL explicit NOT: gate naming the positional failure mode. C-25 (pre-flight positioning) is a sharpened form that foreclosures the failure mode before the commitment point is reached.**

---

### Excellence Signals from V-05 (Top Score: 125/125)

**Signal 1: Frontmatter as multi-dimensional compliance ledger (9 fields)**
V-05 frontmatter tracks not just primary structural constraints (adversary_pre_determination, register_word_used) but quality vectors: record_specific_antipattern (tracks RECORD DIAGNOSIS quality), role_foreclusion_explicit (tracks whether all role sections stated prohibitions), preflight_confirmed (tracks PRE-FLIGHT completion). The artifact write-out states: "The frontmatter is a compliance record, not formatting metadata. Verify before finalizing: All per-field NOT: prohibitions are present... INVENTORY SCHEMA was produced... RECORD DIAGNOSIS cited at least two fields... PRE-FLIGHT block appears between ADVERSARY COMPLETE and JUDGE section." A reader can audit multi-dimensional compliance from frontmatter alone.

**Signal 2: Triple enforcement layering at every critical transition**
V-05 enforces each structural constraint at three levels: (1) per-field NOT: prohibitions in the frontmatter block bounding the fill window, (2) inline phase-boundary attestations at phase exits ("SURVEYOR COMPLETE. Set signal_count now. NOT: ADVERSARY begins with signal_count unset"), (3) gate items in each phase's structural gate section. No constraint is stated once. Defense-in-depth: if a writer misses the frontmatter gate, the phase-exit attestation catches it; if they miss the attestation, the gate item forecloses it.

**Signal 3: INVENTORY SCHEMA as shared vocabulary propagating across all phases**
V-05 INVENTORY SCHEMA (signal_count, method_set, convergence_pattern, dominant_signal, coverage_gaps) creates addressable named fields that propagate through the entire artifact: RECORD DIAGNOSIS cites schema fields by name and value, confidence calibration references convergence_pattern as a ceiling factor, JUDGE must address whether the diagnosed failure mode applies, record_specific_antipattern boolean tracks schema-citation compliance. The schema is not a summary device -- it is a structured vocabulary that makes all downstream reasoning cross-referenceable without re-reading inventory prose.

**Signal 4: PRE-FLIGHT block expanded to full structural audit, not just register-word gate**
V-05 PRE-FLIGHT CHECKLIST goes beyond V-03's register-word check: "[ ] RECORD DIAGNOSIS appears in ADVERSARY phase and cites INVENTORY SCHEMA fields." V-05's PRE-FLIGHT verifies C-21 compliance as a pre-condition for proceeding to JUDGE. By requiring the writer to run the checklist before the commitment sentence, V-05 forecloses all three C-20/C-21/C-22 failure modes at the same structural moment: field-filling completeness, schema citation, and register-word placement are all checked before JUDGE begins.

---

### V6 Candidates (from R5 Mechanisms)

| Candidate | Name | Extends | Mechanism | Evidence Source |
|-----------|------|---------|-----------|-----------------|
| C-23 | Phase-boundary transition gates | C-20 | Explicit NOT: conditions at each phase exit prevent advancing with unset fields; phase-advance without attestation is a procedural breach. Fill window bounded at both ends (premature NOT: + deferred NOT:). | V-01 per-field prohibitions; V-05 dual enforcement layers |
| C-24 | Schema-quoted diagnosis | C-21 | RECORD DIAGNOSIS cites INVENTORY SCHEMA field names and exact values; paraphrase without citation fails; a reader verifies in one check without re-reading inventory prose. Diagnosis falsified if cited values do not match schema. | V-02 schema citation; V-04/V-05 combined |
| C-25 | Pre-JUDGE pre-flight block | C-22 | Register-word gate positioned structurally before the commitment sentence can be written; gate-first means the prohibition is encountered before the failure mode can occur, not alongside or after. V-05 expands to full structural audit (RECORD DIAGNOSIS check + register-word gate) run before JUDGE begins. | V-03 PRE-FLIGHT; V-05 expanded checklist |

**Discrimination confirmed:** V-01 isolated C-23 signal; V-02 isolated C-24 signal; V-03 isolated C-25 signal. V-04 confirmed C-23+C-24 compose without C-19. V-05 confirmed all three compose with full R4 V-05 inheritance. All three candidates are verified by at least two independent variations.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["triple enforcement layering: per-field NOT: prohibitions in frontmatter + phase-boundary attestations at phase exits + gate items in structural gates -- no structural constraint stated once", "frontmatter as multi-dimensional compliance ledger tracking 9 fields including quality vectors (record_specific_antipattern, role_foreclusion_explicit, preflight_confirmed) enabling reader audit without full artifact read", "INVENTORY SCHEMA creates addressable named vocabulary propagating from SURVEYOR to RECORD DIAGNOSIS to confidence calibration to frontmatter boolean tracking", "PRE-FLIGHT block expanded beyond register-word gate to full structural audit: verifies C-21 compliance (schema citation present) as pre-condition before JUDGE begins"]}
```
