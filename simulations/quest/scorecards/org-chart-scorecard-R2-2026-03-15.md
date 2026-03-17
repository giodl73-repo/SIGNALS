## org-chart R2 Score Report

### Evaluation: V-01 — Steelman Enforcement

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Inertia before org boxes | PASS | "INERTIA ASSESSMENT — THREE PARTS REQUIRED" section precedes "ASCII ORG DIAGRAM"; explicit gate: "Do not write an org diagram until the VERDICT is written." |
| C-02 | Org hierarchy readable | PASS | "At least two levels, at least two distinct nodes at the top level or second level" required. |
| C-03 | Roles input honored | PASS | ROLES-LOADED or ROLES-NOTE block with explicit fallback to inferred list; "Do not proceed past this block until it is written." |
| C-04 | Headcount by area | PASS | Table template with minimum two area rows and individual counts. |
| C-05 | Operating rhythm table | PASS | "Three or more distinct entries." "Do not combine two meetings into one row to reach the three-entry minimum." |
| C-06 | Committee charters complete | PASS | Four fields (Purpose, Membership, Decides, Escalates) per charter; "section is enforced — it is not optional." |
| C-07 | All four output sections | PASS | Section order enumerates inertia, ASCII diagram, headcount, operating rhythm, charters — all present. |
| C-08 | Decision rights indicated | PASS | "Decision Scope" column with "must describe specific decision types — not 'owns the area.'" |
| C-09 | Org evolution path | FAIL | No evolution roadmap section. |
| C-10 | Anti-patterns flagged | FAIL | No anti-pattern section. |
| C-11 | Inertia steelmans status quo | PASS | "Part 1 — Case for Staying Flat" requires minimum two numbered mechanisms; "DO NOT proceed until at least two are written"; content guard names what counts (channel, informal lead, cadence). |
| C-12 | Decides/Escalates split | FAIL | Headcount table uses single "Decision Scope" column, not two-column Decides/Escalates. |
| C-13 | VERDICT re-assessment trigger | PASS | "Part 3 — VERDICT and Re-assessment Trigger" explicitly required; trigger must name a threshold. |

**Essential:** 5/5 = 60  
**Recommended:** 3/3 = 30  
**Aspirational:** C-11, C-13 = 2/5 = 4  
**Composite: 94 — Golden**

---

### Evaluation: V-02 — Decides/Escalates Architecture

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Inertia before org boxes | PASS | "Inertia Assessment" section required before org diagram; "Do not write an org diagram until the VERDICT is written." |
| C-02 | Org hierarchy readable | PASS | "Minimum: two levels, two distinct nodes at top or second level." |
| C-03 | Roles input honored | PASS | ROLES-LOADED or ROLES-NOTE block; "Do not proceed until the block is written." |
| C-04 | Headcount by area | PASS | "At minimum two area rows with individual counts." |
| C-05 | Operating rhythm table | PASS | "Three or more distinct entries." "Do not combine two meetings into one row." |
| C-06 | Committee charters complete | PASS | All four fields required; "This section is enforced — do not label it optional." |
| C-07 | All four output sections | PASS | All sections in enumerated order. |
| C-08 | Decision rights indicated | PASS | Decides and Escalates columns constitute decision rights per area. |
| C-09 | Org evolution path | FAIL | No evolution roadmap section. |
| C-10 | Anti-patterns flagged | FAIL | No anti-pattern section. |
| C-11 | Inertia steelmans status quo | FAIL | Inertia section asks for "description of current coordination mechanisms" and "flat-team viability threshold" — no labeled steelman sub-section arguing *for* staying flat with minimum two reasons. Passes C-01, not C-11. |
| C-12 | Decides/Escalates split | PASS | Five-column table (Area / Headcount / Key Roles / Decides / Escalates) explicitly required; "'owns the area' does not pass either column"; "A single sentence describing scope does not pass C-12." |
| C-13 | VERDICT re-assessment trigger | PASS | "Re-assessment trigger: the specific condition that would flip this verdict (headcount threshold, coordination-failure signal, or milestone — not a vague 'as the team grows')." |

**Essential:** 5/5 = 60  
**Recommended:** 3/3 = 30  
**Aspirational:** C-12, C-13 = 2/5 = 4  
**Composite: 94 — Golden**

---

### Evaluation: V-03 — Aspirational Section Forcing

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Inertia before org boxes | PASS | "INERTIA ASSESSMENT" before ASCII diagram; VERDICT required before org structure. |
| C-02 | Org hierarchy readable | PASS | "Minimum: two levels, two distinct nodes." |
| C-03 | Roles input honored | PASS | ROLES-LOADED or ROLES-NOTE required. |
| C-04 | Headcount by area | PASS | Minimum two area rows. |
| C-05 | Operating rhythm table | PASS | Three or more entries covering ROB, shiproom, governance. "Do not combine meetings into one row." |
| C-06 | Committee charters complete | PASS | Charter "(enforced, not optional)" with Purpose, Membership, Decides/Escalates. |
| C-07 | All four output sections | PASS | All four canonical sections present in order. |
| C-08 | Decision rights indicated | PASS | "Decision Scope must describe specific decision types, not 'owns the area.'" |
| C-09 | Org evolution path | PASS | "ORG EVOLUTION ROADMAP — REQUIRED": table with minimum two rows, each requiring a "concrete headcount threshold or named workload signal" and named structural change; "'The org will evolve' is not a valid entry." |
| C-10 | Anti-patterns flagged | PASS | "ANTI-PATTERN WATCH — REQUIRED": named anti-pattern table with one-sentence domain-specific rationale; generic warnings explicitly disqualified. |
| C-11 | Inertia steelmans status quo | FAIL | Inertia section asks for "how the team coordinates today" and "flat-team viability threshold" — no labeled "Case for Staying Flat" sub-section with minimum two reasons arguing FOR the current state. |
| C-12 | Decides/Escalates split | FAIL | Headcount table uses single "Decision Scope" column: `| Area | Headcount | Key Roles | Decision Scope |`. |
| C-13 | VERDICT re-assessment trigger | PASS | "Re-assessment trigger: the concrete condition that would flip this verdict" explicitly required. |

**Essential:** 5/5 = 60  
**Recommended:** 3/3 = 30  
**Aspirational:** C-09, C-10, C-13 = 3/5 = 6  
**Composite: 96 — Golden**

---

### Evaluation: V-04 — Steelman + D/E + Trigger (Three Aspirational Combined)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Inertia before org boxes | PASS | "DO write the Inertia Assessment before any org boxes." "DO NOT write an org diagram as the first section." |
| C-02 | Org hierarchy readable | PASS | "DO show at minimum two levels." "DO NOT produce a flat list of names without hierarchy." |
| C-03 | Roles input honored | PASS | "DO check `.craft/roles/`" first; ROLES-LOADED or ROLES-NOTE block required. |
| C-04 | Headcount by area | PASS | "DO include at minimum two area rows with individual counts." |
| C-05 | Operating rhythm table | PASS | "DO include at minimum three distinct rows." "DO NOT combine two meetings into one row." |
| C-06 | Committee charters complete | PASS | All four fields (Purpose, Membership, Decides, Escalates) required per charter. "DO NOT label this section optional." |
| C-07 | All four output sections | PASS | "DO NOT reorder sections. DO NOT omit any of the six sections." |
| C-08 | Decision rights indicated | PASS | Decides and Escalates columns populate decision rights per area. |
| C-09 | Org evolution path | FAIL | No evolution roadmap section in V-04. |
| C-10 | Anti-patterns flagged | FAIL | No anti-pattern section in V-04. |
| C-11 | Inertia steelmans status quo | PASS | "Sub-section 1 — Case for Staying Flat": "DO include at minimum two numbered reasons"; "DO NOT write generic statements like 'the team communicates well.'"; each reason must name a mechanism. |
| C-12 | Decides/Escalates split | PASS | "DO use five columns — Area, Headcount, Key Roles, Decides, Escalates." "DO NOT use a single 'Decision Scope' column." "DO NOT write 'owns the area' or generic ownership phrases in either column." |
| C-13 | VERDICT re-assessment trigger | PASS | "DO write a re-assessment trigger immediately after the verdict." "DO NOT write 'revisit as the team grows' — the trigger must name a threshold." |

**Essential:** 5/5 = 60  
**Recommended:** 3/3 = 30  
**Aspirational:** C-11, C-12, C-13 = 3/5 = 6  
**Composite: 96 — Golden**

---

### Evaluation: V-05 — Full Aspirational Contract

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Inertia before org boxes | PASS | Phase 2 (Inertia) must complete before Phase 3 (org structure); "Do not begin a phase until the previous phase deliverable is written." |
| C-02 | Org hierarchy readable | PASS | Phase 3 requires "at minimum two levels, at minimum two distinct top-level or second-level nodes." |
| C-03 | Roles input honored | PASS | Phase 1 (ROLES) delivers ROLES-LOADED or ROLES-NOTE table; "Phase 1 complete when: table is written with at least one row." |
| C-04 | Headcount by area | PASS | Phase 3 headcount table with "at minimum two area rows with individual counts." |
| C-05 | Operating rhythm table | PASS | Phase 4 requires "three or more distinct rhythm rows"; ROB, shiproom, governance listed as three separate rows in template. |
| C-06 | Committee charters complete | PASS | Phase 4 charters with all four fields; "This section is enforced — not optional." Phase 4 complete when "at least two charters with all four fields are written." |
| C-07 | All four output sections | PASS | Artifact output section order covers all four canonical sections plus two aspirational phases. |
| C-08 | Decision rights indicated | PASS | Phase 3 Decides/Escalates columns cover decision rights. |
| C-09 | Org evolution path | PASS | Phase 5 "ORG EVOLUTION ROADMAP" is mandatory ("This phase is mandatory. It is not an addendum."); table requires "at minimum two rows, each with a concrete trigger and a named structural change"; "'The org will evolve' or 'revisit as needed' does not pass." |
| C-10 | Anti-patterns flagged | PASS | Phase 6 "ANTI-PATTERN WATCH" is mandatory ("This phase is mandatory. It is not a generic risk section."); "Two or more anti-patterns with domain-specific rationale earns full C-10 credit." |
| C-11 | Inertia steelmans status quo | PASS | Phase 2 "Case for Staying Flat" sub-section: "List the specific working mechanisms... Present the strongest case for NOT formalizing structure." Minimum two items with content guard; "Switching Cost" sub-section adds further structural weight to the steelman. |
| C-12 | Decides/Escalates split | PASS | Phase 3 five-column headcount table; "A single 'Decision Scope' column does not satisfy this requirement even if it contains decision language"; each column requires named decision types. |
| C-13 | VERDICT re-assessment trigger | PASS | Phase 2 VERDICT sub-section requires trigger; "Vague language such as 'revisit as the team grows' does not satisfy this requirement." |

**Essential:** 5/5 = 60  
**Recommended:** 3/3 = 30  
**Aspirational:** C-09, C-10, C-11, C-12, C-13 = 5/5 = 10  
**Composite: 100 — Golden**

---

## Summary Scorecard

| V | Axis | Essential | Recommended | Aspirational | Total | Band |
|---|------|-----------|-------------|--------------|-------|------|
| V-05 | full-aspirational-contract | 5/5 (60) | 3/3 (30) | 5/5 (10) | **100** | Golden |
| V-03 | section-forcing C-09+C-10 | 5/5 (60) | 3/3 (30) | 3/5 (6) | 96 | Golden |
| V-04 | C-11+C-12+C-13 combined | 5/5 (60) | 3/3 (30) | 3/5 (6) | 96 | Golden |
| V-01 | steelman-enforcement | 5/5 (60) | 3/3 (30) | 2/5 (4) | 94 | Golden |
| V-02 | decides-escalates-arch | 5/5 (60) | 3/3 (30) | 2/5 (4) | 94 | Golden |

**Note on predictions:** V-01 and V-02 each predicted 92 (1/5 aspirational) but score 94 (2/5) because C-13 is incidentally enforced in both — the re-assessment trigger was introduced alongside the steelman (V-01) and D/E split (V-02). V-03 and V-04 both match predicted 96. V-05 matches predicted 100.

---

## Excellence Signals from V-05

**Signal 1 — Phase-gated contract with explicit completion checks.**  
Each phase ends with "Phase N complete when: [named deliverable is present]." This acts as a quality gate the model must satisfy before advancing, rather than relying on a single prompt-level instruction to cover all outputs. The pattern prevents partial deliverables being buried inside a larger run.

**Signal 2 — Aspirational criteria elevated to mandatory phases, not suggestions.**  
C-09 and C-10 scored 0/5 across all of R1 and only appeared when given their own named phases (V-03 and V-05). The pattern: labeling a section "REQUIRED" or "mandatory — not an addendum" at the phase level is the lever, not the rubric criterion name. V-03 proved the pattern holds even outside the full-contract context.

**Signal 3 — Failure conditions stated inline at point of instruction.**  
Every aspirational phase in V-05 names the disqualifying output directly: "'The org will evolve' or 'revisit as needed' does not pass." This is distinct from C-11/C-12/C-13 in V-04 which state the DO NOT rules at the prompt level but not embedded in the template itself. Inline disqualification prevents the model from satisfying the structural slot with the exact content the rubric excludes.

**Signal 4 — Steelman given sub-layer architecture, not just a label.**  
V-01 added a labeled block with a minimum bullet count. V-05 gave the steelman five Phase 2 sub-sections (Case for Staying Flat / Switching Cost / Flat-Team Viability Threshold / Rebuttal / VERDICT), making the steelman structurally heavier. This architectural depth is what distinguishes C-11 passing in a full-contract versus token compliance in a weaker prompt.

**Signal 5 — All 13 criteria pass simultaneously with no zero-sum tradeoff.**  
R1 showed that adding aspirational content could displace essential coverage (V-05/R1 still scored 92, not 100, despite targeting aspirational slots). V-05/R2 demonstrates that a phase-sequenced contract reaches 100 without any degradation: every essential and recommended criterion also passes, confirming the phase architecture eliminates the coverage/depth tradeoff.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-gated contract with per-phase completion checks reliably surfaces all aspirational criteria without degrading essential coverage", "Naming failure conditions inline at the point of instruction (not just in rubric) prevents the specific vague content each criterion excludes", "Elevating aspirational criteria to mandatory named phases is sufficient — no dynamic context required; static template enforcement reaches 5/5"]}
```
