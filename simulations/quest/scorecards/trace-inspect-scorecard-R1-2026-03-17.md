## Quest Score — trace-inspect R1

---

## Per-Variation Scoring

---

### V-01 — Role Sequence (QO → IA → SA)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | **PASS** | All 4 phases present and structurally closed. Phase 1 has full per-role schema binding blocks for all three named roles (Schema 1 and Schema 2 binding fields explicit for QO/IA/SA). |
| C-02 | Essential | **PASS** | Phase 2 directly states "Produce the hand-compiled artifact `{topic}-skill-trace-{date}.md` with every section the artifact contract requires." |
| C-03 | Essential | **PASS** | Coverage Matrix declares all five schemas before Stage 1. Label lock invariant stated. "A phase using a label not declared here is in violation." |
| C-04 | Essential | **PASS** | Step 3c has all three gates with explicit PASS/FAIL prompts. Schema 5 transition condition states "G-1=PASS, G-2=PASS, G-3=PASS" before 3d may begin. |
| C-05 | Essential | **PASS** | Phase 5 Verdict includes all three classifications with decision rules (NEEDS-SPEC-REVISION if P1 SA remains SA; NEEDS-REDESIGN if EG>3; USEFUL otherwise). |
| C-06 | Recommended | **PASS** | SA-TO-SG PROMOTION template is complete: per-gap evaluation entry, PROMOTES/REMAINS decision, one-sentence reason, and post-promotion inventory. |
| C-07 | Recommended | **PASS** | All three role relays have labeled fields including the explicit "Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO" field. |
| C-08 | Recommended | **PARTIAL** | Step 3b Schema 5 transition only requires ">=2 entries" — no explicit 3-row minimum stated in the instruction. QO-first ordering improves Source type diversity but does not enforce the count floor. |
| C-09 | Aspirational | **PASS** | Full VC compliance ledger (VC-1 through VC-5) per usage site. "'Observed behavior: as expected' is structurally invalid; name specific values, labels, or invariant results." Observed fields prompt specifics (e.g. "[list severity values; counts; flags]"). |
| C-10 | Aspirational | **PASS** | All four sub-steps carry explicit Schema 5 prerequisite statements and transition sentences: "Schema 5 transition: Step 3a complete. Step 3b is valid to begin." through Phase 4. |

**Essential**: 5/5 → 60 pts
**Recommended**: 2.5/3 → 25 pts
**Aspirational**: 2/2 → 10 pts
**Score: 95 | all_essential_pass: YES**

---

### V-02 — Lifecycle Emphasis (Compressed Setup + STOP Banners)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | **PARTIAL** | All phases present. Phase 1 compressed to 6-line checklist + one-line abbreviated gap attribution: `[role: {{name}}] SA/SG affecting: [list] | EG expected: [list]`. Schema 1 and Schema 2 binding fields are in the Coverage Matrix header, not confirmed in Phase 1 itself. The abbreviated one-liner does not produce schema binding blocks. |
| C-02 | Essential | **PASS** | Phase 2 commands artifact write with "Every section the artifact contract requires must appear." |
| C-03 | Essential | **PASS** | Coverage Matrix present with full schema declarations. "Only {P1,P2,P3} valid anywhere." |
| C-04 | Essential | **PASS** | Strongest C-04 of all five variations. STOP banners at every gate. "Minimum output: Explicit PASS or FAIL for G-1, G-2, and G-3. A gate recorded without an explicit result (e.g., 'probably passes') is structurally invalid. A FAIL blocks Step 3d and Phase 4." |
| C-05 | Essential | **PASS** | Verdict section present with all three classifications. |
| C-06 | Recommended | **PASS** | SA-TO-SG PROMOTION template complete. |
| C-07 | Recommended | **PASS** | "Schema 2 compliance field is mandatory in every relay" stated explicitly in Phase 2 Execute. |
| C-08 | Recommended | **PASS** | Step 3b states: "Minimum output: Findings table with >=3 entries and >=2 distinct Source types. A table with fewer than 3 entries, or with all entries from a single Source type, fails G-1." Strongest explicit count enforcement in this round. |
| C-09 | Aspirational | **PASS** | Compliance ledger present. "'Observed behavior: as expected' is structurally invalid -- name the specific values, labels, roles, or invariant results observed." |
| C-10 | Aspirational | **PASS** | STOP banner format carries transition sentences at each sub-step: ">>>Step 3a COMPLETE. Step 3b is valid to begin.<<<" through ">>>Step 3d COMPLETE. Channel taxonomy active. Phase 4 is valid to begin.<<<" |

**Essential**: 4.5/5 → 54 pts (C-01 PARTIAL)
**Recommended**: 3/3 → 30 pts
**Aspirational**: 2/2 → 10 pts
**Score: 94 | all_essential_pass: NO (C-01 PARTIAL, fails golden threshold)**

---

### V-03 — Phrasing Register (Imperative Commands)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | **PASS** | All phases present. Phase 1 "Bind Your Inputs" has full per-role 4-field attribution blocks: Schema 1 binding, Schema 2 binding, SA/SG gaps, EG expected. |
| C-02 | Essential | **PASS** | "Write the artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md`. Every section the artifact contract requires must appear in that file." Direct imperative command. |
| C-03 | Essential | **PASS** | "Remember these rules" section: "Use ONLY {P1, P2, P3} for severity. Never write 'high', 'medium', 'low', or 'critical'." and "Use ONLY {SA, SG, EG, QO} for source labels. Never write 'spec gap', 'runtime error', or 'design issue'." Strongest schema compliance instruction of all variations. |
| C-04 | Essential | **PASS** | "For each gate, write an explicit result: PASS or FAIL. Nothing else is valid here." Self-correction loops: "If FAIL: go back to 3b... Return here and re-check." |
| C-05 | Essential | **PASS** | "Now write your trace result. Choose exactly one:" with all three options listed. Rationale field required. |
| C-06 | Recommended | **PASS** | "For every SA gap in your relay, decide: can a spec-competent invoker supply this at runtime?" Promotion template complete. |
| C-07 | Recommended | **PASS** | "Fill every field. Do not summarize with 'role ran normally.'" All relay fields explicit in template. Schema 2 compliance field named. |
| C-08 | Recommended | **PASS** | "Write at least 3 rows. Make sure at least 2 distinct Source types appear in the Source column." Explicit minimum in imperative form. G-2 gate covers duplicate Actions within same-Source pairs. |
| C-09 | Aspirational | **PASS** | Strongest ledger instruction of all variations. "Do not write 'as expected' -- name the actual value, label, count, or result you observed." Observed column prompts are specific: "paste your exact 3a legend entries", "list: P1=n, P2=n, P3=n; flag any others". |
| C-10 | Aspirational | **PASS** | Each sub-step begins with "Prerequisite: [X]. Check: YES." and ends with "Done with 3a. Move to 3b now." — explicit prerequisite and transition at every boundary. |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 2/2 → 10 pts
**Score: 98 | all_essential_pass: YES**

---

### V-04 — Role Sequence + Prose Relay Format (EG-first + Paragraphs)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | **PASS** | All phases present. Phase 1 has full per-role schema binding in EG-first order with Schema 1 and Schema 2 binding fields. |
| C-02 | Essential | **PASS** | "Write the hand-compiled artifact `{topic}-skill-trace-{date}.md`. All artifact contract sections required." |
| C-03 | Essential | **PASS** | Coverage Matrix present. Schema declarations clear. |
| C-04 | Essential | **PASS** | Step 3c has all three gates with PASS/FAIL prompts and self-correction loops. |
| C-05 | Essential | **PASS** | Verdict section with all three classifications. |
| C-06 | Recommended | **PASS** | SA-TO-SG PROMOTION template complete. |
| C-07 | Recommended | **PARTIAL** | Prose relay format risks burying the Schema 2 compliance field. Instruction requires it as an explicit sentence: "Schema 2 compliance: Source labels used by this role were [list] -- all from {SA,SG,EG,QO}: YES/NO." Strong structural guard but field discipline typically degrades in prose. A relay that naturally omits this sentence in flowing text is a realistic failure mode. |
| C-08 | Recommended | **PARTIAL** | Step 3b Schema 5 transition requires only ">=2 entries with >=2 Source types" — no explicit 3-row floor. EG-first ordering improves Source diversity but the count minimum is not enforced. |
| C-09 | Aspirational | **PASS** | "'Observed behavior' must name specific values. 'As expected' is invalid." Compliance ledger template present. |
| C-10 | Aspirational | **PASS** | Schema 5 prerequisite stated before each sub-step; "Schema 5 transition: Step 3a complete. Step 3b valid." after each. |

**Essential**: 5/5 → 60 pts
**Recommended**: 2/3 → 20 pts (C-07 PARTIAL, C-08 PARTIAL)
**Aspirational**: 2/2 → 10 pts
**Score: 90 | all_essential_pass: YES**

---

### V-05 — Full Integration (Lifecycle + Imperative + Inertia)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | **PASS** | All phases present. Phase 1 one-liner format includes Schema 1 and Schema 2 bindings: `[role: NAME] | Schema 1: [labels] | Schema 2: [labels] | SA/SG binding: [list or none] | EG expected: [list or none]`. Compact but all required fields present. |
| C-02 | Essential | **PASS** | "Write the artifact now at `simulations/trace/skill/{topic}-skill-trace-{date}.md`. Every section the artifact contract requires must appear. No partial artifacts." |
| C-03 | Essential | **PASS** | Hard rules section with commitment language: "Every severity label is P1, P2, or P3. 'High', 'medium', 'low', 'critical' are not valid. Ever." — the "Ever" emphasis is the strongest prohibition framing in this round. |
| C-04 | Essential | **PASS** | GATE format at each sub-step. "Write PASS or FAIL. No other answer is valid. A FAIL blocks 3d and Phase 4. This is not negotiable." Self-correction: "If FAIL: go to 3b... Come back and re-check G-1." |
| C-05 | Essential | **PASS** | "The result must match your gap inventory" + all three classifications listed with conditions. Rationale sentence required. |
| C-06 | Recommended | **PASS** | Promotion Decision section with full per-gap template and "Commit now: you will not use the SA label for any promoted gap from this point forward." |
| C-07 | Recommended | **PASS** | Standard field-format relay (not prose). "Do not write 'role ran normally.' Fill every field explicitly." Schema 2 compliance field named. |
| C-08 | Recommended | **PASS** | GATE 3b: "Minimum required: at least 3 rows. At least 2 distinct Source types." Self-correction loop: "If you reach this minimum, Step 3c may begin. If not, add findings until you do." Strongest C-08 enforcement of all variations. |
| C-09 | Aspirational | **PASS** | Compliance ledger with "The 'Observed' column names specific values. 'As expected' is not valid." Template row prompts specific (e.g., "[your exact 3a legend]", "[labels + counts in table]"). |
| C-10 | Aspirational | **PASS** | GATE banner format at each sub-step with "Prerequisite: ... CHECK: YES" and ">>>3a DONE. Legend written. Step 3b may begin.<<<" — the visual GATE stop makes schema 5 transitions structurally impossible to skip silently. |

**Essential**: 5/5 → 60 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 2/2 → 10 pts
**Score: 96 | all_essential_pass: YES**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | **Total** | all_essential_pass | Golden |
|-----------|-----------|-------------|--------------|-----------|-------------------|--------|
| V-01 | 60 | 25 | 10 | **95** | YES | YES |
| V-02 | 54 | 30 | 10 | **94** | NO (C-01 PARTIAL) | NO |
| **V-03** | **60** | **30** | **10** | **98** | **YES** | **YES** |
| V-04 | 60 | 20 | 10 | **90** | YES | YES |
| V-05 | 60 | 30 | 10 | **96** | YES | YES |

**Rank**: V-03 > V-05 > V-01 > V-02 (not golden) > V-04

---

## Excellence Signals — V-03 (Top Variation)

**1. Imperative commands close the instruction-action gap.**
Every instruction is phrased as "Write X now" rather than "A valid X produces Y." The model is less likely to describe what output should contain and more likely to produce it. Example: "Write the artifact file at [path]. Every section... must appear." versus "An Execute phase that produces role relays without a written artifact fails."

**2. ONLY/Never label-prohibition lists prevent schema drift more effectively than declarative Coverage Matrix alone.**
The "Remember these rules" section names the exact wrong labels: "Never write 'high', 'medium', 'low', or 'critical'." This pre-empts the most common failure pattern (C-03) by naming the competitor labels explicitly rather than only listing valid ones.

**3. Prerequisite-check + done-transition pattern enforces Schema 5 ordering without structural overhead.**
Each sub-step begins "Prerequisite: X. Check: YES." and ends "Done with X. Move to Y now." This is less verbose than STOP-banner format but provides the same schema 5 compliance guarantee through the systematic alternation of prerequisite and completion markers.

---

## Why V-05 Trails V-03 (Score: 96 vs 98)

V-05's compact Phase 1 one-liner format covers the required schema binding fields but lacks the explicit multi-line block structure that makes C-01 most resilient. V-03's four-field per-role blocks (Schema 1 binding / Schema 2 binding / SA/SG gaps / EG expected) are less susceptible to field omission under model compression. V-03 also has more specific observed-value prompts in the compliance ledger ("paste your exact 3a legend entries" vs "[your exact 3a legend]"). V-05's inertia framing adds motivational context at the cost of ~200 words before the protocol — beneficial for commitment framing but marginally reduces effective instruction density.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["Imperative commands ('Write X now') close the instruction-action gap — models produce required output rather than describing what it should contain", "ONLY/Never label-prohibition lists naming forbidden labels by name block schema violations more effectively than declarative-only Coverage Matrix", "Prerequisite-check plus done-transition on every sub-step enforces Schema 5 ordering without STOP-banner overhead"]}
```
