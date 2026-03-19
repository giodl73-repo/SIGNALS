Now I have everything I need. Let me score all 5 variations against the rubric.

---

## roles-create R1 — Scoring

**Point values:**
- Essential (C-01–C-05): 12 pts each / 60 max
- Recommended (C-06–C-07): 15 pts each / 30 max
- Aspirational (C-08–C-09): 5 pts each / 10 max
- PARTIAL = 50% of criterion value

---

### V-01: Mode-routing-first

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Step 5: "Write the complete role to: .craft/roles/{area}/{subrole}.md" — explicit. |
| C-02 | All required frontmatter fields present | PASS | 12 | Step 3 enumerates all substantive fields by name with descriptions: orientation frame/serves, lens verify/simplify, expertise depth/relevance, archetype, scope, collaborates_with, artifacts, workflow. `name` and `version: "1.0"` are implied defaults at low omission risk. |
| C-03 | Mode detection routes correctly | PASS | 12 | Step 1 names all three modes with explicit rules. "Do NOT prompt for more information" guards the two silent modes. Crisp — this is the axis being tested. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | "Every field must draw from the input domain — not from adjacent or generic templates." Per-field descriptions reinforce domain-specificity without examples. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Step 2 fires before generation: "Note: no inertia-advocate exists for area {area}. Run /roles-create {area}:inertia-advocate to add it." Correct sequencing and message format. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | "At least 4 boolean checks… Phrasing: 'Is X configured before Y?'… Avoid: 'Check configuration', 'Review security', 'Ensure compliance'." Good/bad pattern examples present. |
| C-07 | Body includes domain specializations table | PASS | 15 | Step 4: "At least one structured table mapping domain-specific entities to their purpose." Explicit requirement. |
| C-08 | Archetype calibrated to area tier | PARTIAL | 3 | "Match the area's established pattern (craft for technical areas, process-specific for governance/discovery areas)." Two-option split, no instruction to check existing roles in the area — weaker than V-02/V-05. |
| C-09 | Orientation register matches audience | PARTIAL | 3 | "frame: Self-directed. How this role sees the domain… serves: Receiver-directed. Who benefits." Direction present; no format contracts or guard against serves-as-self-description failure. |
| **Total** | | | **96** | All 5 essential: PASS |

---

### V-02: Template-Anchored

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | "File path: .craft/roles/{area}/{subrole}.md" shown in the template header. |
| C-02 | All required frontmatter fields present | PASS | 12 | Complete YAML template shows every field explicitly including `name`, `version: "1.0"`, and all structural keys. No field can be omitted without deviating from the shown shape. |
| C-03 | Mode detection routes correctly | PASS | 12 | Three-mode table at top of prompt. Interactive case specifies three questions (area, subrole, orientation). Silent modes labelled "No questions." |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Per-field format contracts name failure modes: "If healthcare: name specific regulations (HIPAA, HITECH), specific audit types… No generic 'software engineering depth'." |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | "If absent: output 'Suggestion: run /roles-create {area}:inertia-advocate' before the role file." Fires before role generation. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Inline good/bad example per verify slot in the template itself: "Good: 'Is the posting profile mapped to GL accounts before transaction posting?' Bad: 'Check posting configuration.'" Strongest structural guard for C-06. |
| C-07 | Body includes domain specializations table | PASS | 15 | Template shows the table shape with domain-named column header instruction: "name this section for the domain, not 'Entities'." |
| C-08 | Archetype calibrated to area tier | PASS | 5 | Comment in template: "craft = technical/developer areas (backend, astro, flash). process = discovery/governance/ops areas. Use the archetype that matches other roles in this area, if any exist." Instructs checking existing roles — stronger than V-01/V-03/V-04. |
| C-09 | Orientation register matches audience | PASS | 5 | Template frame contract: "Self-directed. 'Sees every interaction through the lens of...' — first-person perspective." Serves: "Receiver-directed. Name the beneficiary explicitly: 'PMs and analysts who need...'." Implicit guard against self-description failure via beneficiary framing. |
| **Total** | | | **100** | All 5 essential: PASS |

---

### V-03: Inertia-Gated

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Phase 5: "Write to: .craft/roles/{area}/{subrole}.md (Write the inertia-advocate file first if it was absent in Phase 2.)" |
| C-02 | All required frontmatter fields present | PASS | 12 | Phase 3 enumerates all required fields by name with descriptions. Complete field list including orientation, lens, expertise, archetype, scope, collaborates_with, artifacts, workflow. Similar depth to V-01. |
| C-03 | Mode detection routes correctly | PASS | 12 | Phase 1 names all three modes; "No questions" for NAME-ONLY and DESCRIPTION; interactive asks area/subrole/orientation in sequence. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | "All fields must be domain-specific" in Phase 3; per-field descriptions reinforce domain draw. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Phase 2 is the axis being tested — explicit ABSENT/PRESENT branches. ABSENT generates the inertia-advocate as a companion role first (not just suggests) AND outputs explanatory message. Strongest C-05 behavior of any single-axis variation. |
| C-06 | Lens.verify questions sharp and actionable | PARTIAL | 8 | Phase 3: "4+ boolean checks naming specific artifacts, configs, or states." Criterion is present but no good/bad examples. V-01/V-02/V-05 all provide example phrasings. Higher vague-verify risk. |
| C-07 | Body includes domain specializations table | PASS | 15 | Phase 4: "at minimum one table mapping domain-specific entities (commands, regulations, modules, components) to their purpose and failure mode." |
| C-08 | Archetype calibrated to area tier | PARTIAL | 3 | Phase 3: "match the area's established archetype tier" — no category examples, no check-existing-roles instruction. Weakest archetype guidance of all variations. |
| C-09 | Orientation register matches audience | PARTIAL | 3 | Phase 3: "orientation.frame — how this role perceives the domain (self-directed), orientation.serves — who benefits and why (receiver-directed, name the beneficiary)." Present but no format contracts or examples. |
| **Total** | | | **89** | All 5 essential: PASS |

---

### V-04: Conversational-Register

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | "The file goes in .craft/roles/{area}/{subrole}.md" — stated explicitly. |
| C-02 | All required frontmatter fields present | PASS | 12 | "The frontmatter has: name, version (always '1.0'), archetype, orientation (frame and serves fields), lens (verify and simplify sublists), expertise (depth and relevance), scope, collaborates_with, artifacts, and workflow." — complete enumeration including `name` and `version: "1.0"`. |
| C-03 | Mode detection routes correctly | PASS | 12 | Three modes described in second-person paragraphs. "no clarifying questions needed" stated for name-only and description modes. Interactive asks three things "in sequence." |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | "Don't write 'deep software engineering knowledge' — name what specifically is in scope for this role in this domain." Direct anti-generic guard. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | "Before you write anything, check whether .craft/roles/{area}/inertia-advocate.md exists. If it doesn't, mention it — something like 'I notice there's no inertia-advocate in the {area} area yet…'" — check sequenced correctly, suggested wording provided. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | "'Is the audit log timestamped with timezone before export?' is good. 'Check audit logging' is not useful. Aim for at least four of these." Concrete good/bad example inline. |
| C-07 | Body includes domain specializations table | PASS | 15 | "Include at least one table that maps domain-specific entities (commands, regulations, modules, components, processes) to what they do and where they can fail." |
| C-08 | Archetype calibrated to area tier | PARTIAL | 3 | "pick the one that fits the area's established pattern — craft for technical areas, process-specific for governance/ops areas" — two-option guidance, no check-existing-roles instruction. |
| C-09 | Orientation register matches audience | PASS | 5 | "orientation.frame should read as if the role is speaking about itself — how it sees the domain, what it's always watching for. orientation.serves should name the people who benefit from having this perspective in the room." Clear first-person/third-person register split stated naturally. This is the axis being tested — pass. |
| **Total** | | | **98** | All 5 essential: PASS |

---

### V-05: Full Integration

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | File written to correct path | PASS | 12 | Phase 5: "Write files: .craft/roles/{area}/inertia-advocate.md (if generated in Phase 2) and .craft/roles/{area}/{subrole}.md." Correct path for both outputs. |
| C-02 | All required frontmatter fields present | PASS | 12 | Phase 3 template shows every field explicitly: name, version, archetype, orientation frame/serves, lens verify/simplify, expertise depth/relevance, scope, collaborates_with, artifacts, workflow — all with format contracts. |
| C-03 | Mode detection routes correctly | PASS | 12 | Phase 1 is a standalone gate. "Output of Phase 1: area string, subrole string, orientation seed." Interactive mode adds "Wait for answers before proceeding" — the only variation with explicit hold instruction. |
| C-04 | Frontmatter content is domain-specific | PASS | 12 | Per-field examples by domain: "Healthcare: HIPAA, HITECH, HL7, FHIR, covered entity obligations, BAAs. Finance: GAAP, GL account structure, period close, reconciliation workflows." Positive examples, not just anti-generic guard. |
| C-05 | Inertia-advocate surfaced when absent | PASS | 12 | Phase 2 ABSENT branch generates the companion role with content spec (orientation.frame, lens.verify with specific existing-system requirement, expertise.depth for switching costs). Not just a suggestion — delivers the file. |
| C-06 | Lens.verify questions sharp and actionable | PASS | 15 | Phase 3 inline good/bad: "Good: 'Is the HIPAA audit log exported in FHIR-compliant format before submission?' Bad: 'Check audit log configuration.'" Domain-specific example anchors the criterion. |
| C-07 | Body includes domain specializations table | PASS | 15 | Phase 4: "Column names should reflect the domain, not generic 'Entity / Purpose'." Table naming instruction is the strongest — prevents nominal-compliance (a table present but column-agnostic). |
| C-08 | Archetype calibrated to area tier | PASS | 5 | Phase 3 comment: "craft = technical/builder areas (backend, astro, flows, flash, craft). process = governance/ops/compliance areas (discovery, admin, compliance). Use the archetype present in other roles in this area, if any exist." Broadest category list + check-existing instruction. |
| C-09 | Orientation register matches audience | PASS | 5 | Phase 3: "Register: first-person observational" for frame and "Register: third-person recipient. Not a self-description." for serves. The "Not a self-description" guard directly targets the primary C-09 failure mode. Strongest register enforcement of any variation. |
| **Total** | | | **100** | All 5 essential: PASS |

---

## Rankings

| Rank | Variation | Score /100 | Band | Distinctive Strength |
|------|-----------|-----------|------|----------------------|
| 1 | **V-05: Full integration** | **100** | Golden | Best C-09 guard (register labels + "Not a self-description"), strongest C-05 (generates companion), domain-concrete C-04 examples per field |
| 2 | **V-02: Template-anchored** | **100** | Golden | Best C-02/C-06 (template shows shape, inline good/bad per slot), strong C-08 (check-existing-roles instruction) |
| 3 | **V-04: Conversational register** | **98** | Golden | Best C-09 for its register axis (natural split stated conversationally), strong anti-generic C-04 |
| 4 | **V-01: Mode-routing-first** | **96** | Golden | Crisp C-03 with "Do NOT prompt" guard, well-structured steps; C-08/C-09 weakest |
| 5 | **V-03: Inertia-gated** | **89** | Golden | Strongest C-05 (generates companion role first), but C-06 PARTIAL (no examples), C-08/C-09 minimal |

All five variations pass all 5 essential criteria. All five are Golden (>= 80 composite, all essential pass).

---

## Key Scoring Decisions

**V-05 vs V-02 tie at 100 — V-05 ranked first** because Phase 3's explicit `Register:` labels and "Not a self-description" guard give C-09 mechanical enforcement that V-02's format contract implies but does not state. V-05's Phase 2 also generates (not just suggests) the inertia-advocate. V-02 is the stronger choice if minimizing prompt verbosity is the constraint.

**V-03 C-06: PARTIAL** — Phase 3 says "4+ boolean checks naming specific artifacts" but no good/bad examples. V-01/V-02/V-04/V-05 all show example phrasings. V-03 is the only variation where vague-verify items remain a material risk. This is the primary score gap between V-03 (89) and V-01 (96).

**V-04 C-08: PARTIAL** — Conversational mode describes two archetype options but omits the "check existing roles" instruction present in V-02 and V-05. The axis being tested (register) passes cleanly; the unaddressed axis (archetype calibration) remains the weak spot.

**V-01 vs V-03 — both 96 before C-06 adjustment** — V-01 gains on C-06 (has examples); V-03 gains on C-05 intensity (generates companion vs suggests). After C-06 PARTIAL, V-03 drops to 89, making V-01 clearly fourth.

---

## Excellence Signals from V-05

1. **Register labels per orientation field prevent the same-register failure** — "Register: first-person observational" and "Register: third-person recipient. Not a self-description." gives the model explicit register anchors. The "Not a self-description" guard directly targets the primary C-09 failure. V-02 implies the register split through beneficiary framing but does not name it, leaving the model to infer. Naming the register makes C-09 mechanically checkable.

2. **Companion role generation turns C-05 from a hint into a delivery** — When ABSENT, Phase 2 generates the inertia-advocate with a content spec (specific orientation.frame for migration cost perspective, at least one verify question naming the existing system being displaced). This ensures the area gets inertia coverage on first invocation, regardless of whether the user follows up. Suggestion-only variants rely on user action; generation variants do not.

3. **Domain-concrete field examples beat anti-generic instructions** — V-01/V-03/V-04 say "be domain-specific, not generic." V-05 shows what domain-specific means per field: "Healthcare: HIPAA, HITECH, HL7, FHIR… Finance: GAAP, GL account structure, period close." Positive examples constrain the space more reliably than negative instructions, especially for uncommon domains where the model may not know what counts as "generic."

4. **Inline good/bad examples inside the field template are the most reliable C-06 guard** — V-02 and V-05 both embed a good/bad example directly in the verify slot of the template. V-03's absence of examples is the only thing that causes its C-06 PARTIAL and its 11-point drop from V-01. The implication: for criteria where the pass/fail distinction is subtle (vague vs. specific), a counter-example inside the template is more reliable than a prose description of the failure mode.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["register labels per orientation field prevent same-register failure: naming 'first-person observational' for frame and 'third-person recipient — Not a self-description' for serves gives the model explicit register anchors and guards the primary C-09 failure mode more reliably than implied beneficiary framing", "companion role generation turns C-05 from a hint into a delivery: when the inertia-advocate ABSENT branch generates the companion with a content spec (orientation.frame for migration cost, verify question naming the displaced system), coverage is guaranteed without user follow-through — suggestion-only variants rely on user action", "domain-concrete field examples beat anti-generic instructions: showing 'Healthcare: HIPAA, HITECH, HL7, FHIR' per field constrains C-04 compliance more reliably than 'no generic depth' — positive examples narrow the space; negative guards leave it open", "inline good/bad examples inside the field template are the most reliable C-06 guard: V-03's absence of verify examples is the only factor that causes its PARTIAL and 11-point drop — counter-examples embedded in the template slot are more durable than prose descriptions of the failure mode"]}
```
