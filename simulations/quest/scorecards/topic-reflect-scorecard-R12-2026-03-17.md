## Quest Score — topic-reflect (Round 12) — Rubric v11

**File:** `simulations/quest/golden/topic-echo-variate-R12-2026-03-17.md`
**Rubric:** v11 | 30 criteria | Max: 200 pts | Golden threshold: all essential pass + ≥100

---

### Scoring Basis

All five variations share an identical structural base: Stage 6 restored (C-02 fixed), Field Reference block (C-29), Surprise 0 with boundary marker (C-30), Build Risk triple-anchor definition (C-27), four-field ✓ checklist gate (C-28), and COMMIT-STAGE-3-CLEAN / FLAGGED (C-14). The variation axes are register, lifecycle framing, role sequence, conversational tone, and delta framing. The scoring task is therefore to identify whether any variation falls short on the base criteria and whether any novel patterns emerge.

---

## V-01 — Formal/Specification Register

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 Surprise orientation | PASS | Sub-Spec 4.A.1 requires B-# reference; EXIT criterion requires ≥1 contradiction; COMMIT-ENTRY gate enforces belief label |
| C-02 Symmetric Contract | PASS | Stage 1: Opening Model + Epistemic Profile + ≥3 B-## beliefs; Stage 6: verdict table with Revision Direction + COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED |
| C-03 Signal tracing | PASS | Sub-Spec 4.A.2 requires specific artifact name/namespace/date; explicit enforcement HALT on generic phrase |
| C-04 Design impact specificity | PASS | Sub-Spec 4.A.3 prohibits "the system/architecture/codebase"; enforcement HALT on abstract subject |
| C-05 Adversarial gate executed | PASS | Five-check table present; VALID/INVALID per row; GATE-CONFIRMED/GATE-REJECTED; Stage 3.5 with COMMIT-STAGE-3-CLEAN/FLAGGED |
| C-06 Epistemic dimension compliance | PASS | Standalone VOCABULARY RULE section; SHALL scan at every EXIT; 5 canonical names listed |
| C-07 Minimum 2 surprises | PASS | EXIT criterion: "≥2 GATE-CONFIRMED entries. If fewer than 2, extend the sweep." |
| C-08 Cluster map actionability | PASS | Stage 5: "SHALL name at least one specific skill (e.g., `flow-trigger`, `trace-permissions`) or role per row" |
| C-09 Token protocol integrity | PASS | Gate Sequence Overview table present; all COMMIT-STAGE-1 through -7 present; COMMIT-ENTRY in entry loop |
| C-10 Foreknowledge signal evaluated | PASS | Stage 6: CLEAR or FLAGGED per belief; HALT before Stage 7 if FOREKNOWLEDGE-FLAGGED unresolved |
| C-11 Stage 4 prose template format | PASS | "Markdown tables SHALL NOT be used for entry content"; numbered prose blocks with labeled sub-fields |
| C-12 Stage 4 entry completeness | PASS | Sub-Spec 4.A.2/4.A.3 require full sentences; COMMIT-ENTRY gate enforces completeness |
| C-13 Closed-list dimension vocabulary | PASS | Standalone section with explicit closed set + "Any dimension value not in the closed set is a vocabulary violation and SHALL be corrected" |
| C-14 Foreknowledge dual-token gate | PASS | Stage 3.5: COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED; "SHALL NOT proceed to Stage 4 without a COMMIT-STAGE-3-CLEAN token" |
| C-15 Pre-stage gate sequence map | PASS | GATE SEQUENCE OVERVIEW table with Stage/Token/Halt Condition/Flow before Stage 1 |
| C-16 Worked calibration example | PASS | Surprise 0: complete entry with `topic-scanner-state-2026-03-10.md` in Signal Source; `TopicScanner.checkReadiness()` in Design Impact |
| C-17 Named synonym exclusions | PASS | Prohibited table names: Reliability, Performance, Maintainability, Learnability, Viability |
| C-18 Synonym-to-canonical mapping | PASS | Five full mappings: Reliability→Correctness, Performance→Scalability, Maintainability→Correctness, Learnability→Usability, Viability→Feasibility |
| C-19 Per-stage ENTER/EXIT lifecycle contract | PASS | Every stage (1–7) has explicit ENTER contract ("MUST be present") and EXIT criterion |
| C-20 Calibration example as Stage 4 entry 0 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; full sub-field format; COMMIT-ENTRY emitted; positioned before ENTRY LOOP |
| C-21 Vocabulary self-repair at EXIT gate | PASS | "Requirement 3: At every Stage EXIT gate, the model SHALL scan all dimension values and replace any prohibited name with its canonical substitute" |
| C-22 Stage 4 Build Risk sub-field | PASS | Sub-Spec 4.A.4 present; modeled in Surprise 0; specific component named in example |
| C-23 Surprise 0 dual-field specificity anchoring | PASS | Design Impact: `TopicScanner.checkReadiness()` (forward-looking); Build Risk: `ProgramOrchestrator` (risk surface); conceptually distinct, non-redundant |
| C-24 COMMIT-ENTRY Build Risk specificity gate | PASS | ✓ checklist bullet: "Does it name a specific component or contract implicated by the Design Impact change, and is it conceptually distinct from Design Impact? If not — identify what downstream element could fail... and rewrite." |
| C-25 Four-field convergent mechanism coverage | PASS | All four fields: (a) Surprise 0 imitation floor ✓, (b) COMMIT-ENTRY checklist gate ✓, (c) Sub-Spec enforcement HALT instruction ✓ — three mechanisms per field |
| C-26 Build Risk paired conceptual formula | PASS | "Paired formula: Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail." |
| C-27 Build Risk triple-anchor sequence | PASS | Three labeled anchors in sequence: "Purpose:" + "Paired formula:" + "Abstract structural gloss:" — all present before Surprise 0 |
| C-28 COMMIT-ENTRY four-field visual checklist | PASS | ✓ Surprise / ✓ Signal Source / ✓ Design Impact / ✓ Build Risk — each on dedicated bullet with gate condition and corrective action |
| C-29 Stage 4 dedicated Field Reference block | PASS | "FIELD REFERENCE BLOCK" heading; Sub-Spec 4.A.1–4.A.4 consolidate all four definitions before entry loop; structurally separate from COMMIT-ENTRY gate |
| C-30 Calibration entry live/example boundary marker | PASS | "It is labeled Surprise 0 and is a Calibration Entry (not a live entry). Live entries begin at Surprise 1." |

**V-01 Score: 200/200** | Essential: 60/60 | Recommended: 30/30 | Aspirational: 110/110 | **GOLDEN**

---

## V-02 — Lifecycle / Gate Anatomy

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | Field Reference: "A Surprise that does not reference a specific B-# does not pass the COMMIT-ENTRY gate"; EXIT requires ≥1 contradiction |
| C-02 | PASS | Stage 1 symmetric with Stage 6; verdict table has Revision Direction + three verdict tokens |
| C-03 | PASS | Field Reference: "Generic phrases... do not pass the COMMIT-ENTRY gate" |
| C-04 | PASS | Field Reference: "Subjects such as 'the system,' 'the architecture' do not pass the COMMIT-ENTRY gate" |
| C-05 | PASS | Five-check table; GATE-CONFIRMED/GATE-REJECTED; COMMIT-STAGE-3-CLEAN/FLAGGED in Stage 3.5 |
| C-06 | PASS | Gate rule: "scan all dimension values... replace any prohibited synonym" at every stage close |
| C-07 | PASS | "At least two entries carry GATE-CONFIRMED status. If fewer, extend the sweep." |
| C-08 | PASS | Stage 5: named skill or role required; "Generic entries ('TBD') not permitted" |
| C-09 | PASS | GATE SEQUENCE OVERVIEW with "Gate Opens When" / "Gate Closes With" columns; all tokens present |
| C-10 | PASS | Stage 6: CLEAR or FLAGGED per belief; "This gate closes flagged and does not advance to Stage 7 without user confirmation." |
| C-11 | PASS | "Do not use markdown tables for entry content" |
| C-12 | PASS | Field Reference requires full sentences; COMMIT-ENTRY gate enforces |
| C-13 | PASS | Standalone vocabulary section; "A dimension value not in the canonical set is a gate violation" |
| C-14 | PASS | "The Stage 4 gate does not open without COMMIT-STAGE-3-CLEAN." |
| C-15 | PASS | GATE SEQUENCE OVERVIEW table with distinctive gate-anatomy columns before Stage 1 |
| C-16 | PASS | Surprise 0 with identical content; realistic artifact reference; full Design Impact sentence |
| C-17 | PASS | Five named prohibited synonyms in table |
| C-18 | PASS | Five canonical mappings |
| C-19 | PASS | Every stage: "Gate opens:" (ENTER) + "Gate closes:" (EXIT) — clean lifecycle contract at every stage |
| C-20 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; COMMIT-ENTRY present |
| C-21 | PASS | Gate rule: replacement scans active "at the close of every stage gate" |
| C-22 | PASS | Build Risk in Field Reference; modeled in Surprise 0 |
| C-23 | PASS | Same Surprise 0 content — Design Impact / Build Risk conceptually distinct |
| C-24 | PASS | ✓ Build Risk bullet with specificity check and corrective action |
| C-25 | PASS | Each field: Field Reference gate-blocking condition ✓ + COMMIT-ENTRY checklist ✓ + Surprise 0 imitation floor ✓ |
| C-26 | PASS | "Paired formula: Design Impact names what must change; Build Risk names what is implicated by that change..." |
| C-27 | PASS | Purpose + Paired formula + Abstract structural gloss — all three labeled anchors present |
| C-28 | PASS | ✓ checklist with four dedicated bullets; gate condition + corrective action per bullet |
| C-29 | PASS | "FIELD REFERENCE BLOCK — Stage 4 Gate-Open Ritual" — declared as gate-open ritual; all four definitions unified before entry loop |
| C-30 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; "Live entries begin at Surprise 1 and must match or exceed" |

**V-02 Score: 200/200** | Essential: 60/60 | Recommended: 30/30 | Aspirational: 110/110 | **GOLDEN**

---

## V-03 — Three Named Roles

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | Field Reference: "A Surprise without a B-# reference does not pass the COMMIT-ENTRY gate"; EXIT ≥1 contradiction |
| C-02 | PASS | Symmetric: Stage 1 (Historian) + Stage 6 (Synthesizer) verdict table with all three verdict tokens |
| C-03 | PASS | "Phrases such as 'multiple sources,' 'the signals,' or 'various artifacts' do not pass the COMMIT-ENTRY gate." |
| C-04 | PASS | "Subjects such as 'the system,' 'the architecture' do not pass the COMMIT-ENTRY gate." |
| C-05 | PASS | Five-check table; GATE-CONFIRMED/GATE-REJECTED; Stage 3.5 COMMIT-STAGE-3-CLEAN/FLAGGED |
| C-06 | PASS | Vocabulary rule applies to all three roles; scan at every stage exit |
| C-07 | PASS | EXIT: "At least two entries carry GATE-CONFIRMED status. If fewer, extend the sweep." |
| C-08 | PASS | "Next Team / Skill: at least one specific skill or role per row. Generic entries not permitted." |
| C-09 | PASS | Gate Sequence Overview table includes Role column; all tokens present |
| C-10 | PASS | Stage 6: CLEAR or FLAGGED; "do not advance to Stage 7 without user confirmation" |
| C-11 | PASS | Entry loop: "Each entry has labeled sub-fields... Markdown tables SHALL NOT be used" |
| C-12 | PASS | COMMIT-ENTRY gate enforces; field definitions require full sentences |
| C-13 | PASS | Standalone vocabulary section with closed set; "replaces any prohibited name" instruction |
| C-14 | PASS | "COMMIT-STAGE-3-CLEAN unlocks the Surprise Synthesizer." |
| C-15 | PASS | Gate Sequence Overview table with Role column adds role-stage mapping context |
| C-16 | PASS | Surprise 0 present with complete content |
| C-17 | PASS | Five named prohibited synonyms |
| C-18 | PASS | Five canonical mappings |
| C-19 | PASS | Every stage has explicit ENTER contract + EXIT criterion |
| C-20 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; "The Surprise 0 label distinguishes this entry from all live entries; the Synthesizer does not number live entries starting at 2." |
| C-21 | PASS | "Before emitting any commit token, the active role scans all dimension values and replaces any prohibited name" |
| C-22 | PASS | Build Risk in Synthesizer's Field Reference; modeled in Surprise 0 |
| C-23 | PASS | Same Surprise 0 — Design Impact / Build Risk distinct and non-redundant |
| C-24 | PASS | ✓ Build Risk specificity check with corrective action |
| C-25 | PASS | All four fields: Field Reference gate-block ✓ + COMMIT-ENTRY checklist ✓ + Surprise 0 imitation ✓ |
| C-26 | PASS | "Paired formula: Design Impact names what must change; Build Risk names what is implicated by that change..." |
| C-27 | PASS | Three labeled anchors in sequence: Purpose + Paired formula + Abstract structural gloss |
| C-28 | PASS | ✓ checklist with four dedicated bullets; gate condition + corrective action per bullet |
| C-29 | PASS | "SYNTHESIZER'S FIELD REFERENCE BLOCK" — explicitly owned by the Synthesizer role; all four definitions before entry loop |
| C-30 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; explicit note: "does not number live entries starting at 2" |

**V-03 Score: 200/200** | Essential: 60/60 | Recommended: 30/30 | Aspirational: 110/110 | **GOLDEN**

---

## V-04 — Conversational Register + Inline Examples

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | Field guide: "Name the specific belief it contradicts (use its label)"; "If you haven't named a B-# belief, the entry isn't done yet." |
| C-02 | PASS | Stage 1: Opening Model + Epistemic Profile + ≥3 beliefs; Stage 6: verdict table with all three verdict tokens |
| C-03 | PASS | "Don't write 'multiple sources' or 'various signals.' If you wrote a generic phrase here, the entry isn't done yet." |
| C-04 | PASS | "If you wrote 'the system' or 'the architecture,' the entry isn't done yet." |
| C-05 | PASS | Five-check table; GATE-CONFIRMED/GATE-REJECTED; COMMIT-STAGE-3-CLEAN/FLAGGED |
| C-06 | PASS | Vocabulary section with closed set; table of substitutions; enforcement scan before each stage close |
| C-07 | PASS | "Do you have at least two GATE-CONFIRMED entries? If not, extend the sweep." |
| C-08 | PASS | "name a specific skill (like `flow-trigger`) or a specific role (like 'API contract owner'). 'TBD' doesn't count." |
| C-09 | PASS | "Your stage map (read this first)" table covers all tokens and stop conditions before Stage 1 |
| C-10 | PASS | Stage 6: CLEAR or FLAGGED; "stop before Stage 7 until the user has confirmed what to do" |
| C-11 | PASS | "Use labeled prose — not a table." |
| C-12 | PASS | COMMIT-ENTRY checklist; field definitions require full sentences; inline examples reinforce completeness |
| C-13 | PASS | Standalone vocabulary section: "You have exactly five dimension names. Use only these:"; prohibition enforced via enforcement statement |
| C-14 | PASS | "You can't open Stage 4 without COMMIT-STAGE-3-CLEAN." |
| C-15 | PASS | "Your stage map (read this first)" — stage map table before Stage 1 |
| C-16 | PASS | Surprise 0 with complete content AND inline _Example:_ annotations at each field definition |
| C-17 | PASS | Five prohibited synonyms named in table |
| C-18 | PASS | Five canonical mappings ("If you wrote this... Replace it with...") |
| C-19 | PASS | Every stage: "Before you start Stage X" (ENTER condition) + "Before closing Stage X" (EXIT criterion) |
| C-20 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; "Do not number your live entries starting at 2 — Surprise 0 is the calibration entry only; it is separate from the live sequence." |
| C-21 | PASS | "Before you close each stage, scan any dimension values you wrote and swap out any prohibited name for its canonical substitute." |
| C-22 | PASS | Build Risk defined in field guide with inline _Example:_ showing `ProgramOrchestrator`; Surprise 0 models it |
| C-23 | PASS | Same Surprise 0 — Design Impact / Build Risk distinct and non-redundant |
| C-24 | PASS | ✓ Build Risk bullet: "ask yourself 'what could fail because of the Design Impact change?' and rewrite" |
| C-25 | PASS | All four fields: field guide inline _Example:_ anchors ✓ + COMMIT-ENTRY checklist ✓ + Surprise 0 ✓ |
| C-26 | PASS | "Design Impact is forward-looking (what to update); Build Risk is the risk surface (what could break or require rework). They are two different things." — names both fields in structural relation |
| **C-27** | **PARTIAL** | Purpose statement ✓; abstract structural gloss ✓ ("Design Impact is forward-looking..."); but no distinct *paired conceptual formula* anchor as a separate labeled statement naming both fields in the "X names what must change; Y names what is implicated" form — the gloss and formula collapse into a single statement, leaving only two of three independent anchors |
| C-28 | PASS | ✓ checklist with four dedicated bullets; gate condition + corrective action per bullet |
| C-29 | PASS | "Your field guide (read this before every entry)" — dedicated named section; all four field definitions before Surprise 0 and entry loop |
| C-30 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; "Do not number your live entries starting at 2" |

**V-04 Score: 197.5/200** | Essential: 60/60 | Recommended: 30/30 | Aspirational: 107.5/110 | **GOLDEN**
*(C-27 scored as 2.5/5 — partial credit for 2 of 3 required anchors)*

---

## V-05 — Role Sequence + Inertia Framing

| Criterion | Verdict | Evidence Note |
|-----------|---------|---------------|
| C-01 | PASS | Field Reference: "Reference the specific belief it contradicts by label"; "A Surprise without a B-# reference does not pass the COMMIT-ENTRY gate" |
| C-02 | PASS | Stage 1 symmetric with Stage 6; Auditor executes verdict table with Revision Direction + all three verdict tokens + Foreknowledge Status column |
| C-03 | PASS | "Phrases such as 'multiple sources,' 'the signals,' or 'various artifacts' do not pass the COMMIT-ENTRY gate." |
| C-04 | PASS | "Subjects such as 'the system,' 'the architecture' do not pass the COMMIT-ENTRY gate." |
| C-05 | PASS | Five-check table (Check 4 = Inertia Test); GATE-CONFIRMED/GATE-REJECTED; Stage 3.5 COMMIT-STAGE-3-CLEAN/FLAGGED |
| C-06 | PASS | Vocabulary rule applies to all four roles at every stage exit |
| C-07 | PASS | EXIT: "At least two GATE-CONFIRMED entries. If fewer, extend sweep." |
| C-08 | PASS | "Next Team / Skill: at least one specific skill or role per row. Generic entries not permitted." |
| C-09 | PASS | Gate Sequence Overview with Role column; all tokens; COMMIT-ENTRY in entry loop |
| C-10 | PASS | Stage 6 has Foreknowledge Status column; CLEAR or FLAGGED; Auditor mandate: "Do not advance to Stage 7 without user confirmation." |
| C-11 | PASS | "Do not use tables." Numbered prose blocks with delta framing + labeled sub-fields |
| C-12 | PASS | COMMIT-ENTRY gate enforces full sentences; field definitions require specificity |
| C-13 | PASS | Standalone vocabulary section with closed set and prohibited table |
| C-14 | PASS | "Stage 4 does not open without COMMIT-STAGE-3-CLEAN." |
| C-15 | PASS | Gate Sequence Overview table with Role column before Stage 1 |
| C-16 | PASS | Surprise 0 with delta framing ("Opening Model Predicted" / "Evidence Showed") + complete sub-fields |
| C-17 | PASS | Five named prohibited synonyms |
| C-18 | PASS | Five canonical mappings |
| C-19 | PASS | Every stage has explicit ENTER contract + EXIT criterion; Auditor role adds a second EXIT checkpoint at Stage 6 |
| C-20 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; "live entries are numbered starting at 1, not 2" |
| C-21 | PASS | "At every stage EXIT gate, the active role scans all dimension values... replaces any prohibited name" |
| C-22 | PASS | Build Risk in Synthesizer's Field Reference; Surprise 0 models it with delta framing visible |
| C-23 | PASS | Same Surprise 0 content — Design Impact / Build Risk distinct; delta framing makes the forward-looking / risk-surface poles explicit above the entry |
| C-24 | PASS | ✓ Build Risk specificity check with corrective action |
| C-25 | PASS | All four fields: Field Reference gate-block ✓ + COMMIT-ENTRY checklist ✓ + Surprise 0 (with delta framing) ✓ |
| C-26 | PASS | "Paired formula: Design Impact names what must change; Build Risk names what is implicated by that change..." |
| C-27 | PASS | Three labeled anchors: Purpose + Paired formula + Abstract structural gloss — all present |
| C-28 | PASS | ✓ checklist with four dedicated bullets; gate condition + corrective action per bullet |
| C-29 | PASS | "FIELD REFERENCE BLOCK — Synthesizer's toolset" — all four definitions before entry loop |
| C-30 | PASS | "Surprise 0 — Calibration Entry (not a live entry)"; "live entries are numbered starting at 1, not 2" |

**V-05 Score: 200/200** | Essential: 60/60 | Recommended: 30/30 | Aspirational: 110/110 | **GOLDEN**

---

## Rankings

| Rank | Variation | Score | All Essential | Golden |
|------|-----------|-------|---------------|--------|
| 1 | V-01 (Formal/Specification) | 200/200 | YES | YES |
| 1 | V-02 (Gate Anatomy) | 200/200 | YES | YES |
| 1 | V-03 (Three Named Roles) | 200/200 | YES | YES |
| 1 | V-05 (Role + Inertia Framing) | 200/200 | YES | YES |
| 5 | V-04 (Conversational + Inline Examples) | 197.5/200 | YES | YES |

**First round in which all 5 variations achieve golden threshold.** The base established by R11 V-01 is now sufficiently robust that register, lifecycle framing, and role sequence cannot meaningfully differentiate performance under v11.

---

## Excellence Signals

The four perfect-scoring variations each bring structural innovations not captured by any v11 criterion. Two patterns from V-05 are the strongest candidates:

**1. Per-entry delta framing block (V-05)** — V-05 introduces a structural sub-block before each Surprise statement requiring two labeled lines: "Opening Model Predicted: [what was assumed]" and "Evidence Showed: [what was found]." This appears in the Surprise sub-field definition in the Field Reference block, in the entry loop template, and is modeled in Surprise 0. No existing criterion tests for this — C-01 tests that at least one entry contradicts a belief, but not that every entry explicitly serializes the predicted/found delta before writing the Surprise synthesis. The benefit is that the contradiction structure is externalized as a visual artifact, making the B-# connection auditable without parsing the Surprise prose.

**2. Inertia Test as a named mandate with explicit skeptic articulation requirement (V-05)** — V-05 renames Check 4 as the "Inertia Test" and assigns the Challenger a mandate: "explicitly state: 'A status-quo skeptic [would / would not] accept this as a genuine surprise because [reason].'" This converts the check from a binary VALID/INVALID verdict to a reasoned judgment with a required articulation of the skeptic's perspective. No existing criterion tests for this — C-05 tests that the five-check table is present with VALID/INVALID verdicts, but not that Check 4 carries an explicit skeptic-articulation slot. The benefit is that borderline entries must survive a named adversarial framing before reaching Stage 4.

The inline _Example:_ annotations at each field definition (V-04) are also notable but are somewhat superseded by C-25's convergent coverage requirement. Neither delta framing nor the Inertia Test mandate is derivable from existing criteria.

---

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["Per-entry delta framing block (V-05): structural slot before each Surprise statement requiring 'Opening Model Predicted' and 'Evidence Showed' lines, externalizing the predicted/found delta as a visual artifact before the synthesis — not captured by C-01 which tests belief reference but not explicit delta serialization", "Inertia Test explicit skeptic-articulation mandate (V-05): Check 4 renamed with a required statement 'A status-quo skeptic [would/would not] accept this as a genuine surprise because [reason]' — converts VALID/INVALID verdict to a reasoned judgment with named adversarial framing, not captured by C-05 which tests table presence and verdict tokens but not skeptic-articulation slot"]}
```
