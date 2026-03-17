## corps-committee — Quest Score R2

### Scoring Matrix

#### V-01 — Lifecycle Emphasis (COMMITTEE-TYPE GATE)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type instantiated | **PASS** | COMMITTEE-TYPE GATE in Phase 0 skeleton commits Type, Required framing, Required output before Phase 1. PHASE-0-COMMIT includes "Type framing committed" and "Required output." Fill rules have ACCEPTABLE/FAILS validation examples per type. TYPE-SPECIFIC OUTPUT section in Phase 5. |
| C-02 | Participants speak from role | **PASS** | Phase 3: "2-4 sentences per participant from their charter orientation." Tier-differentiated requirements (Tier 1 cite inertia label, Tier 2 name specific condition, Tier 3 CITE+RESPONDS-TO). |
| C-03 | Decisions explicitly recorded | **PASS** | Phase 5 DECISIONS section with Verdict, Conditions for full approval, Re-entry path. Fill rule: "Verdict matching OUTCOME exactly." |
| C-04 | Action items with owners | **PASS** | Phase 5 ACTION ITEMS fill rule: "[Owner Role] — [specific action] — [deadline]; all three fields required." |
| C-05 | Dissent represented | **PASS** | DISSENTING OPINIONS section linked to STANCE MANIFEST CONDITION/BLOCK entries. Fill rule: "dissent per CONDITION/BLOCK stance — specific objection citing INERTIA-FINDING-* label, resolution path, named authority." |
| C-06 | Formal structure | **PASS** | All sections present: header, agenda, discussion (Phases 1-4), DECISIONS, ACTION ITEMS, DISSENTING OPINIONS, TYPE-SPECIFIC OUTPUT. |
| C-07 | Type-specific discussion depth | **PASS** | TYPE-SPECIFIC OUTPUT fill rules enforce per-type evidence: ROB needs named metric citation, Shiproom needs specific blocking issue, Arch-board needs two rejected alternatives with rationale. ACCEPTABLE/FAILS validation present. |
| C-08 | AMEND honored | **VACUOUS** | Not invoked. |
| C-09 | Pre-mortem outside-in risk | **PARTIAL** | INERTIA-FINDING-D requires a "non-obvious switching cost the proposal author did not account for." GATE enforces non-obviousness. Does not explicitly operationalize the outside-in test (would a competent internal reviewer have predicted this?). |
| C-10 | Charter fidelity traceable | **FAIL** | No CHARTER CONSTRAINTS table and no CHARTER FIDELITY TRACE table. PHASE-0-COMMIT references participants and type but not explicit constraint tracing. Systematic R1 gap unaddressed. |
| C-11 | Injection as default | **PARTIAL** | INERTIA CONTINUITY BRIDGE present. INSPECT → CONFIRM → INJECT flow, but framed as "identify whether a charter role exists" (find YES). Not a burden-flip. No INJECTION-PROOF block. |
| C-12 | Provisional annotation in Phase 0 | **FAIL** | No provisional annotation mechanism in participant list or Phase 0 structure. |

**Essential: 5/5** | **Recommended: 3/3** (C-08 vacuous) | **Aspirational: 0/4** (C-09 partial, C-10 fail, C-11 partial, C-12 fail)

**Composite: (5/5 × 60) + (3/3 × 30) + (0/4 × 10) = 60 + 30 + 0 = 90**
**Tier: GOLD** (all essential + 90 ≥ 80)

---

#### V-02 — Output Format (CHARTER CONSTRAINTS + CHARTER FIDELITY TRACE)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type instantiated | **FAIL** | No COMMITTEE-TYPE GATE. Phase 0 has `Committee Type: ___` field but no type-specific framing commitment. Phase 5 has CHARTER FIDELITY TRACE instead of TYPE-SPECIFIC OUTPUT. Fill rules specify no type-differentiated output. R1 gap unaddressed. |
| C-02 | Participants speak from role | **PASS** | Same Phase 3 tier structure. |
| C-03 | Decisions explicitly recorded | **PASS** | DECISIONS section present with Verdict, Conditions, Re-entry path. |
| C-04 | Action items with owners | **PASS** | Three-field ACTION ITEMS requirement. |
| C-05 | Dissent represented | **PASS** | DISSENTING OPINIONS linked to CONDITION/BLOCK stances. |
| C-06 | Formal structure | **PASS** | Complete structural sections. |
| C-07 | Type-specific discussion depth | **FAIL** | No type-specific framing in Phase 0 or Phase 3. Without the COMMITTEE-TYPE GATE, no mechanism enforces ROB metric discussion, shiproom risk register, or arch-board trade-off depth. C-07 falls with C-01. |
| C-08 | AMEND honored | **VACUOUS** | Not invoked. |
| C-09 | Pre-mortem outside-in risk | **PARTIAL** | Same inertia framework. INERTIA CONTINUITY BRIDGE has explicit two-axis validation ("FAILS (incorrect affirmation)"), slightly stronger than V-01 but no outside-in test. |
| C-10 | Charter fidelity traceable | **PASS** | CHARTER CONSTRAINTS table (Phase 0) with Quorum/Scope/Veto/Escalation rows. CHARTER FIDELITY TRACE table (Phase 5) with Honored YES/NO + Evidence columns. Fill rules: "FAILS: any row blank — C-10 fail." "REQUIRE: at least two rows cite charter-specific constraint language." |
| C-11 | Injection as default | **PARTIAL** | Bridge validate section added ("FAILS (incorrect affirmation): YES declared when no Tier 1/Tier 2 participant maps to inertia analysis"), but no INJECTION-PROOF block and no burden-flip. |
| C-12 | Provisional annotation in Phase 0 | **FAIL** | No provisional annotation. |

**Essential: 4/5** (C-01 fail) | **Recommended: 2/3** (C-07 fail, C-08 vacuous) | **Aspirational: 1/4** (C-10 pass)

**Composite: (4/5 × 60) + (2/3 × 30) + (1/4 × 10) = 48 + 20 + 2.5 = 70.5**
**Tier: BRONZE** (4/5 essential, 70.5 ≥ 60)

---

#### V-03 — Phrasing Register (Conversational Imperatives)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type instantiated | **PASS** | Pre-skeleton "BEFORE YOU START" block states direct imperatives per type: "For ROB — your job is to assess readiness...If there is no metric, you have not done a ROB." "For Arch-board — your job is to pick an architecture...If there are fewer than two rejected alternatives, the ADR is incomplete." COMMITTEE OUTPUT section in Phase 5. Fill rules reinforce per-type requirements with explicit fail conditions. |
| C-02 | Participants speak from role | **PASS** | Same Phase 3 tier structure with charter-orientation framing. |
| C-03 | Decisions explicitly recorded | **PASS** | DECISIONS section with Verdict and specific deliverables. |
| C-04 | Action items with owners | **PASS** | Three-field ACTION ITEMS. |
| C-05 | Dissent represented | **PASS** | DISSENTING OPINIONS with CONDITION/BLOCK linkage. |
| C-06 | Formal structure | **PASS** | All structural sections present. |
| C-07 | Type-specific discussion depth | **PASS** | "BEFORE YOU START" block enforces type-specific discussion requirements before skeleton filling begins. "For ROB...discussion must reference at least one specific feature or metric." Fill rules reinforce. Conversational imperative framing may be more reliable for enforcing depth than formal gate syntax. |
| C-08 | AMEND honored | **VACUOUS** | Not invoked. |
| C-09 | Pre-mortem outside-in risk | **PASS** | Phase 1 fill rule includes the explicit outside-in test: "ask yourself whether a sharp analyst reviewing the proposal would have flagged this already. If yes, that is not FINDING-D — find something they would miss." This directly operationalizes the pass+ gate criterion. Strongest C-09 of all variations. |
| C-10 | Charter fidelity traceable | **FAIL** | No CHARTER CONSTRAINTS table and no CHARTER FIDELITY TRACE. R1 gap unaddressed. |
| C-11 | Injection as default | **PARTIAL** | Standard bridge: "Look at your Tier 1 and Tier 2 participants. Does any of them cover switching-cost analysis by charter...If yes: YES...If no: NO and inject." No burden-flip; no INJECTION-PROOF block. |
| C-12 | Provisional annotation in Phase 0 | **FAIL** | No provisional annotation. |

**Essential: 5/5** | **Recommended: 3/3** (C-08 vacuous) | **Aspirational: 1/4** (C-09 pass)

**Composite: (5/5 × 60) + (3/3 × 30) + (1/4 × 10) = 60 + 30 + 2.5 = 92.5**
**Tier: GOLD** (all essential + 92.5 ≥ 80)

---

#### V-04 — Lifecycle Emphasis + Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type instantiated | **PASS** | COMMITTEE-TYPE GATE in Phase 0 with Type, Required framing, Required output. PHASE-0-COMMIT commits both fields. TYPE-SPECIFIC OUTPUT in Phase 5 with fill rule validation. |
| C-02 | Participants speak from role | **PASS** | Same tier-differentiated Phase 3 structure. |
| C-03 | Decisions explicitly recorded | **PASS** | DECISIONS section present. |
| C-04 | Action items with owners | **PASS** | Three-field requirement. |
| C-05 | Dissent represented | **PASS** | DISSENTING OPINIONS with CONDITION/BLOCK linkage. |
| C-06 | Formal structure | **PASS** | Complete structural sections including COMMITTEE-TYPE GATE and INJECTION-PROOF block. |
| C-07 | Type-specific discussion depth | **PASS** | TYPE-SPECIFIC OUTPUT fill rules explicitly fail C-07: "FAILS: section present but no evidence (no metric / no blocking issue / no alternatives) — C-07 partial." Per-type evidence requirements enforced in Phase 5. |
| C-08 | AMEND honored | **VACUOUS** | Not invoked. |
| C-09 | Pre-mortem outside-in risk | **PARTIAL** | INERTIA-FINDING-D requires non-obvious cost not accounted for by proposal author, but no explicit "sharp analyst" outside-in test. |
| C-10 | Charter fidelity traceable | **FAIL** | No CHARTER CONSTRAINTS table. No CHARTER FIDELITY TRACE. R1 gap unaddressed — V-04 targets C-01/C-11/C-12 but not C-10. |
| C-11 | Injection as default | **PASS** | Full burden-flip implemented. Preamble: "INJECTION IS THE DEFAULT." Three-rule bridge: RULE 1 ("default state is INJECTED"), RULE 2 ("to waive, cite (a) role name AND (b) orientation clause — claiming YES without both is incorrect affirmation"), RULE 3 (validation). INJECTION-PROOF block in skeleton. Two independent FAILS axes in validate. PROVISIONAL resolved annotation printed at bridge resolution. |
| C-12 | Provisional annotation in Phase 0 | **PASS** | Participant line in skeleton includes PROVISIONAL annotation template. Fill rule: "INSPECT each participant for inertia coverage. IF unresolved — ANNOTATE with [PROVISIONAL...]." Bridge fill rule: "RESOLVE: any PROVISIONAL annotation — print [PROVISIONAL resolved: ...]" whether injected or confirmed. |

**Essential: 5/5** | **Recommended: 3/3** (C-08 vacuous) | **Aspirational: 2/4** (C-11, C-12 pass)

**Composite: (5/5 × 60) + (3/3 × 30) + (2/4 × 10) = 60 + 30 + 5 = 95**
**Tier: GOLD** (all essential + 95 ≥ 80)

---

#### V-05 — Full Integration

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Committee type instantiated | **PASS** | COMMITTEE-TYPE GATE in Phase 0, TYPE-SPECIFIC OUTPUT in Phase 5. Fill rules cite criterion explicitly at fail points: "FAILS: section absent — C-01 fail." Strongest C-01 of all variations. |
| C-02 | Participants speak from role | **PASS** | Same tier-differentiated Phase 3 structure. |
| C-03 | Decisions explicitly recorded | **PASS** | DECISIONS section with Verdict, Conditions, Re-entry path. |
| C-04 | Action items with owners | **PASS** | Three-field requirement: "[Owner Role] — [specific action] — [deadline]; all three fields required." |
| C-05 | Dissent represented | **PASS** | DISSENTING OPINIONS with CONDITION/BLOCK linkage and INERTIA-FINDING-* citation requirement. |
| C-06 | Formal structure | **PASS** | Most complete structure of all variations: COMMITTEE-TYPE GATE, CHARTER CONSTRAINTS, all phases, TYPE-SPECIFIC OUTPUT, CHARTER FIDELITY TRACE, ACTION ITEMS, DISSENTING OPINIONS. |
| C-07 | Type-specific discussion depth | **PASS** | TYPE-SPECIFIC OUTPUT fill rules with per-type evidence requirements. Meta-rubric awareness: "FAILS: verdict present but no metric — C-07 partial." COMMITTEE-TYPE GATE frames Phase 3 discussion before it begins. |
| C-08 | AMEND honored | **VACUOUS** | Not invoked. |
| C-09 | Pre-mortem outside-in risk | **PARTIAL** | INERTIA-FINDING-D required non-obvious, and the gate structure ensures this, but no explicit "sharp analyst" outside-in operationalization (V-03 is stronger on C-09). |
| C-10 | Charter fidelity traceable | **PASS** | CHARTER CONSTRAINTS table (Phase 0) + CHARTER FIDELITY TRACE table (Phase 5). PHASE-0-COMMIT names all four values. Fill rules: "FAILS: row absent — C-10 fail." "REQUIRE: at least two rows cite charter-specific constraint language." Closed loop: declared upfront, traced in Phase 5. |
| C-11 | Injection as default | **PASS** | Same three-rule burden-flip as V-04. Preamble: "INJECTION IS THE DEFAULT." RULE 3 added: "YES is only valid when both (a) and (b) are populated with specific, non-generic content." Two independent FAILS axes validated. |
| C-12 | Provisional annotation in Phase 0 | **PASS** | PROVISIONAL annotation in Phase 0 participant template. Fill rule: "ENFORCE: annotation present whenever any participant's inertia coverage is uncertain at Phase 0." Bridge skeleton includes `[PROVISIONAL resolved: ___]` line. Both injection and non-injection paths print explicit resolution. |

**Essential: 5/5** | **Recommended: 3/3** (C-08 vacuous) | **Aspirational: 3/4** (C-10, C-11, C-12 pass; C-09 partial)

**Composite: (5/5 × 60) + (3/3 × 30) + (3/4 × 10) = 60 + 30 + 7.5 = 97.5**
**Tier: GOLD** (all essential + 97.5 ≥ 80)

---

### Rankings

| Rank | Variation | Score | Tier | Gaps |
|------|-----------|-------|------|------|
| 1 | V-05 Full Integration | 97.5 | GOLD | C-09 partial only |
| 2 | V-04 Lifecycle + Inertia | 95 | GOLD | C-09 partial, C-10 fail |
| 3 | V-03 Phrasing Register | 92.5 | GOLD | C-09 pass, C-10/C-11/C-12 open |
| 4 | V-01 Lifecycle Emphasis | 90 | GOLD | C-09/C-11 partial, C-10/C-12 fail |
| 5 | V-02 Output Format | 70.5 | BRONZE | C-01/C-07 essential fail; C-10 closed |

---

### Excellence Signals from V-05

**Signal 1 — Closed-loop charter tracing.** Declaring the CHARTER CONSTRAINTS table in Phase 0 and requiring the CHARTER FIDELITY TRACE table in Phase 5 creates a structural closed loop: every constraint declared must be traced. The table format makes omission explicit (blank cell = visible gap) rather than silent. This is more reliable than prose-level honoring.

**Signal 2 — Cognitive burden-flip with three-rule injection gate.** Moving from "inject if no owner found" to "injection is default; waive only by citing (a) role name AND (b) orientation clause" inverts the cognitive path. RULE 3 ("YES is only valid when both are populated with specific, non-generic content") closes the loophole where a generic orientation description could pass vacuous confirmation. The false-affirmation fail axis makes the error visible.

**Signal 3 — PROVISIONAL annotation as lifecycle completion signal.** Annotating unconfirmed participants in Phase 0 as PROVISIONAL creates a forward-reference obligation that must resolve in the bridge section. The resolution print (`[PROVISIONAL resolved: ...]`) closes the loop regardless of injection outcome — both YES and NO paths require an explicit resolution statement. This converts a silent structural assumption into a traceable lifecycle event.

**Signal 4 — Meta-rubric awareness in fill rules.** Fill rules that cite criterion IDs at FAILS points ("FAILS: section absent — C-01 fail") embed the rubric directly into the prompt. This surfaces which criterion each structural omission would violate, making the enforcement contract explicit to the model.

---

### Key Finding

V-02 is the only variation that drops below Gold, and its failure is categorical: removing the COMMITTEE-TYPE GATE to focus exclusively on charter tracing caused C-01 and C-07 to fail in tandem. The axes are not independent — without type commitment, the charter trace has nothing concrete to anchor to. V-05 integrates both axes, and the combination is additive rather than crowded.

The one remaining gap across all variations is C-09 (outside-in pre-mortem). V-03 comes closest by operationalizing the "sharp analyst" test in Phase 1 fill rules. A future R3 axis could transplant that specific phrasing into V-05's inertia phase fill rules to close the last aspirational gap.

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["closed-loop charter tracing: declare constraints in Phase 0 table, trace them in Phase 5 table — blank cell is an explicit fail not a silent omission", "cognitive burden-flip: injection is the default assumption, waived only by cited proof with named role and orientation clause — prevents silent false affirmations via incorrect YES", "PROVISIONAL annotation with lifecycle resolution: Phase 0 forward-reference annotates uncertain coverage, Phase 2 bridge resolves with explicit print regardless of injection outcome"]}
```
