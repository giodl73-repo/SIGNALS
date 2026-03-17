Scorecard written to `simulations/quest/scorecards/listen-support-scorecard-R1-2026-03-14.md`.

**Round 1 result: V-05 = 100, V-04 = 97, V-02 = 87, V-03 = 86, V-01 = 84.**

The gap between V-04 (97) and V-05 (100) is narrow — V-05 earns the extra 3 points entirely on C-07 and C-08 through STATUS QUO grounding. The critical round 2 question is whether STATUS QUO is actually load-bearing for those criteria or whether V-04's per-card rationale achieves the same differentiation without the overhead.

V-02's structural miss on C-09 (no CROSS-TICKET PATTERN section) is the most actionable finding: adding that one section to V-02 would bring it to ~92 and make it competitive with V-04 as a lower-overhead alternative.
riterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 | PASS | 12/12 | All 5 fields pre-printed as named labels in every card. "Fill every field in every card. Do not omit any field or leave a field blank." Hard to skip. |
| C-02 | PASS | 12/12 | Vocabulary embedded in every field label as constrained value set. |
| C-03 | PARTIAL | 9/12 | Stock roles listed. Body is a named section (not a table cell). Detailed instruction in T-01; T-02+ abbreviates to "Role-specific vocabulary required." Persona label appears above body in card -- proximity helps but no explicit callback. |
| C-04 | PASS | 12/12 | Three sub-sections labeled (Doc Gaps, Design Gaps, Operational Gaps). Priority Close Order pre-printed. |
| C-05 | PASS | 12/12 | "Predict at least 5 tickets. Cover at least 3 distinct category values." CATEGORY COVERAGE CHECK section enforces count. |
| C-06 | PARTIAL | 5/10 | Severity is a pre-printed field with vocabulary constraint only. No rationale required. Full model discretion -- severity washing risk is high. |
| C-07 | PARTIAL | 5/10 | Volume is a pre-printed field. VOLUME CHECK catches uniform volume post-hoc ("revise at least two cards before proceeding") but provides no rationale forcing mechanism. Prevention is absent; correction is weak. |
| C-08 | PARTIAL | 7/10 | Named body section prevents table-cell truncation. T-01 body instruction is detailed. T-02+ instruction is abbreviated. No STATUS QUO grounding. |
| C-09 | PASS | 5/5 | CROSS-TICKET PATTERN section pre-printed with explicit instruction and worked example. |
| C-10 | PASS | 5/5 | Priority Close Order pre-printed with "Rank all gaps by severity and volume." |

**V-01 total: 84/100**
Essential: 54/60 (C-03 PARTIAL). Recommended: 17/30 (C-06, C-07 both weak). Aspirational: 10/10.

---

### V-02: Role Sequence (Support -> PM -> SRE)

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 | PARTIAL | 10/12 | Fields split: Support table has title/category/persona; PM table has volume/severity; body section has bodies. "Mirror all ticket IDs" mitigates but three-pass assembly introduces cross-section omission risk. |
| C-02 | PASS | 12/12 | Vocabulary in every table cell placeholder. |
| C-03 | PARTIAL | 9/12 | Persona locked in Support pass; bodies written after all ratings are locked -- good sequencing. "A body that fits any persona equally well fails this step." But persona and body are in separate sections; no co-location enforcement. |
| C-04 | PASS | 12/12 | Three sub-sections labeled. |
| C-05 | PASS | 12/12 | "Minimum 5. At least 3 distinct category values required." |
| C-06 | PASS | 10/10 | PM severity rationale column required with explicit P0/P1 vs P2/P3 definition. SRE escalation pass structurally confirms operational-class severity. Strongest C-06 mechanism in Round 1. |
| C-07 | PASS | 9/10 | PM volume rationale column required -- "cite affected user population size and ask frequency." "Do not assign all tickets the same volume level." Volume coverage check. Minor gap: rationale could still be written without differentiation. |
| C-08 | PARTIAL | 8/10 | Bodies after personas locked. Explicit fail-condition: "a body that fits any persona equally well fails." But no STATUS QUO grounding. Body section instruction is general, not per-persona-type. |
| C-09 | FAIL | 0/5 | No CROSS-TICKET PATTERN section. Not pre-printed. Model would need to insert it on discretion -- unreliable. |
| C-10 | PASS | 5/5 | Priority Close Order with severity/volume from PM ratings. |

**V-02 total: 87/100**
Essential: 55/60 (C-01, C-03 PARTIAL). Recommended: 27/30. Aspirational: 5/10 (C-09 FAIL -- structural miss).

---

### V-03: Lifecycle Emphasis (Three Phase Windows)

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 | PARTIAL | 10/12 | Phase tables cover title/category/persona/volume/severity. Bodies in separate per-ticket section. All 5 fields present but distributed across template sections -- body omission risk persists from table format. |
| C-02 | PASS | 12/12 | Vocabulary in every table column. |
| C-03 | PARTIAL | 8/12 | Persona in phase tables; body in separate body section. Phase context (Phase 1 = first adopters, Phase 3 = power users) provides implicit voice grounding. But persona and body are not co-located; callback relies on model tracking across sections. |
| C-04 | PASS | 12/12 | Three sub-sections with phase references included. |
| C-05 | PASS | 12/12 | Phase architecture structurally forces category spread -- Phase 1 = how-to/bug, Phase 2 = config/integration, Phase 3 = feature-request. Coverage check enforces >= 3. |
| C-06 | PARTIAL | 6/10 | Severity in table but no rationale column. Phase framing provides implicit pressure (Phase 1 first-adopter friction suggests P1/P2 range) but no explicit constraint -- phase labels are insufficient to prevent severity washing. |
| C-07 | PASS | 9/10 | Phase dominant-volume declarations (one per phase) structurally force differentiation. Phase rationale sentences required. "Distinct volume levels: Must be >= 2." Best C-07 mechanism among table-format variations. |
| C-08 | PARTIAL | 7/10 | Body section per ticket with "role-specific vocabulary and framing required." Phase context helps. But no co-location and no STATUS QUO grounding. |
| C-09 | PASS | 5/5 | CROSS-TICKET PATTERN section pre-printed with instruction to "span two or more phases." Phase labels make cross-phase patterns visible structurally. |
| C-10 | PASS | 5/5 | Priority Close Order with "Phase 1 gaps typically rank first -- explain if not." |

**V-03 total: 86/100**
Essential: 54/60 (C-01, C-03 PARTIAL). Recommended: 22/30 (C-06 weak). Aspirational: 10/10.

---

### V-04: Per-Ticket Cards + Role-Labeled Sections

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 | PASS | 12/12 | All 5 fields across three labeled sections (Support: Triage, PM: Rating, Ticket Body) in every card. "All card fields are required. Do not skip, merge, or reorder any section or field." |
| C-02 | PASS | 12/12 | Vocabulary in every field. |
| C-03 | PASS | 11/12 | Persona in Support: Triage section, body labeled "in the persona's voice named in the Support triage section above." Detailed per-type instruction in T-01 (SRE: ops/infra, PM: roadmap/metrics, C-XX: domain pain). Co-location is strong. Minor gap: T-02+ body instruction abbreviates to "Role-specific language required." |
| C-04 | PASS | 12/12 | Three sub-sections with ticket ID reference instructions. |
| C-05 | PASS | 12/12 | >=5 tickets, >=3 categories, COVERAGE CHECKS section. |
| C-06 | PASS | 10/10 | Severity rationale required in every card with explicit definition: "broken or inaccessible (P0/P1), or is a workaround available and impact is lower (P2/P3)?" Strongest per-ticket C-06 mechanism. |
| C-07 | PASS | 9/10 | Volume rationale required in every card: "how large is the affected user population? How frequently does this situation arise?" Coverage check flags absent levels. Minor gap: no phase gradient to structurally force spread. |
| C-08 | PASS | 9/10 | Body co-located with persona in same card. "Do not write a body that fits any persona equally well." Per-type instruction in T-01. |
| C-09 | PASS | 5/5 | CROSS-TICKET PATTERN section pre-printed with Name/Tickets/Root cause structure. |
| C-10 | PASS | 5/5 | Priority Close Order: "Rank all gaps by severity and volume from the PM rating fields in the ticket cards above. Show reasoning." |

**V-04 total: 97/100**
Essential: 59/60 (C-03 trivial abbreviation gap). Recommended: 28/30. Aspirational: 10/10.

---

### V-05: Full Synthesis (STATUS QUO + Phases + Role-Labeled Cards)

| Criterion | Verdict | Score | Evidence |
|-----------|---------|-------|---------|
| C-01 | PASS | 12/12 | Role-labeled cards within phases. All 5 fields pre-printed. Phase structure adds ticket-ID scoping but does not split fields across sections. |
| C-02 | PASS | 12/12 | Vocabulary in every field. |
| C-03 | PASS | 12/12 | Persona in Support: Triage, body co-located. STATUS QUO provides realistic workaround scenario context that grounds what the persona tried and why. Body instruction: "Reference what they tried, what failed, what they need." Phase label anchors temporal persona role. |
| C-04 | PASS | 12/12 | Three sub-sections with STATUS QUO and phase tie-ins. |
| C-05 | PASS | 12/12 | Phase architecture forces category spread. Coverage checks. |
| C-06 | PASS | 10/10 | Severity rationale in every card with definition. Phase 1 framing ("first adopters hit setup walls") anchors higher severity expectation, reducing severity-washing risk at the phase level. |
| C-07 | PASS | 10/10 | Three independent mechanisms: STATUS QUO volume anchor ("High workaround friction = high Phase 1 volume"), phase gradient (Phase 1 > Phase 2 > Phase 3), per-card rationale referencing STATUS QUO. Uniform volume requires overriding all three. |
| C-08 | PASS | 10/10 | STATUS QUO grounds the scenario across all personas. Body instruction adds "what they tried, what failed, what they need" -- scenario-specific framing that resists generic bodies. Co-located with persona. |
| C-09 | PASS | 5/5 | CROSS-TICKET PATTERN section with STATUS QUO root-cause trace requirement. "Not closing this means:" consequence statement forces forward-looking impact framing. Phase labels make cross-phase pattern connection explicit. Strongest C-09 mechanism. |
| C-10 | PASS | 5/5 | Priority Close Order with "STATUS QUO root:" required per ranked gap. Ties gap to ticket data by ID, phase, severity, and volume. |

**V-05 total: 100/100**
Essential: 60/60. Recommended: 30/30. Aspirational: 10/10.

---

### Round 1 Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Full Synthesis | 100 | Yes |
| 2 | V-04 Cards + Role Fields | 97 | Yes |
| 3 | V-02 Role Sequence | 87 | No (C-01 partial, C-03 partial, C-09 fail) |
| 4 | V-03 Lifecycle Phases | 86 | No (C-01 partial, C-03 partial) |
| 5 | V-01 Per-Ticket Cards | 84 | No (C-03 partial) |

---

### Excellence Signals from V-05

1. **STATUS QUO pre-generation grounding** -- completing the STATUS QUO section before generating any tickets anchors volume predictions, body realism, and gap priority all at once. A single well-filled STATUS QUO section produces downstream correctness across C-07, C-08, and C-09 without requiring the model to exercise judgment independently for each.

2. **Consequence statement at the pattern level** -- the "Not closing this means:" line forces the model to state what day-90 looks like if the pattern is unaddressed. This is more specific than a gap ranking and harder to write generically -- it produces the most actionable C-09 output in the round.

3. **Phase-labeled ticket IDs make cross-section pattern recognition structural** -- because T-01 (P1), T-03 (P2) labels appear in both the ticket cards and the CROSS-TICKET PATTERN field, the model has a concrete citation format that doesn't require it to construct a cross-reference from scratch.

4. **Three-layer C-07 pressure eliminates discretion entirely** -- STATUS QUO friction level, phase dominant-volume rationale, and per-card volume rationale each independently force differentiation. All three would need to fail simultaneously to produce uniform volume output.

---

### Key Round 2 Experiments

| Question | Experiment |
|----------|-----------|
| Is STATUS QUO load-bearing for C-07, or does the per-card rationale in V-04 achieve the same differentiation? | Run V-04 and V-05 on the same topic; compare volume spread across cards |
| Does STATUS QUO measurably improve body authenticity (C-08) vs. V-04's co-location alone? | Blind-judge body authenticity for V-04 vs V-05 outputs |
| Is V-02's C-09 miss recoverable by appending a cross-ticket section? | Test V-02 + CROSS-TICKET PATTERN section as V-06 |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["STATUS QUO pre-generation section anchors all downstream volume, body, and gap priority decisions -- one section, three criteria", "Co-located consequence statement (Not closing this means:) forces gap impact framing at the pattern level rather than the gap list level", "Phase-labeled ticket IDs in both cards and pattern section create a structural citation format that makes cross-ticket pattern recognition non-discretionary"]}
```
