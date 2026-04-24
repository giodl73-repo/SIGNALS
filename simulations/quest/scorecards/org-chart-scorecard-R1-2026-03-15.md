## org-chart Scoring — Round 1

**Run context:** `.roles/signal/` is populated with `pm.md`, `architect.md`, and `inertia-advocate.md`. All C-03 evaluations assume roles exist.

---

### V-01 — Inertia as Named Gate with VERDICT

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia assessment present | PASS | Explicit INERTIA GATE section with Current state / Flat-team viability / VERDICT sub-fields. Hard stop: "Do not write an org diagram or rhythm table until the VERDICT is written." Prevents generic filler. |
| C-02 | ASCII org box rendered | PASS | ASCII ORG BOX section with two-level requirement, committee-as-distinct-node requirement, and an example diagram. |
| C-03 | Roles input honored | PASS | ROLES INPUT section checks `.roles/`, emits ROLES-LOADED list, or writes ROLES-NOTE if absent. Both paths handled. |
| C-04 | Headcount by area | PASS | HEADCOUNT BY AREA with `| Area \| Headcount \| Key Roles |` table, two-row minimum, total row. |
| C-05 | Operating rhythm table | PASS | Explicit three-entry minimum (ROB, shiproom, governance). "Do not combine multiple meetings into a single row." Required columns specified. |
| C-06 | Committee charters complete | FAIL | No committee charters section anywhere. ARTIFACT OUTPUT lists only four sections; charters omitted entirely. |
| C-07 | All four output sections present | PASS | ARTIFACT OUTPUT enumerates all four sections in order. |
| C-08 | Decision rights indicated | FAIL | Headcount table is `Area \| Headcount \| Key Roles` — no decision rights column, no note requirement. |
| C-09 | Org evolution path | FAIL | Not mentioned. |
| C-10 | Anti-patterns flagged | FAIL | Not mentioned. |

**Score:** Essential 5/5 (60) + Recommended 1/3 (10) + Aspirational 0/2 (0) = **70**
**Band:** Acceptable

---

### V-02 — Section Scaffolds with Required Slots

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia assessment present | PASS | SECTION 1 template with Verdict field, Current coordination mode, Flat-team threshold, Justification. Section ordering enforced: "Fill in this section before writing anything else." |
| C-02 | ASCII org box rendered | PASS | SECTION 2 with diagram requirements: two levels, two top-level nodes, committees as separate layer. |
| C-03 | Roles input honored | PASS | ROLES INPUT PROTOCOL at end requires checking `.roles/`, listing in ROLES-LOADED field in Section 2, and roles must appear in at least one output section. |
| C-04 | Headcount by area | PASS | SECTION 3 table with two-area minimum, numeric count, Decision Scope column, total row. |
| C-05 | Operating rhythm table | PASS | SECTION 4 template pre-fills ROB, shiproom, governance rows. Three-entry minimum stated. |
| C-06 | Committee charters complete | PARTIAL | Charter section exists with correct template (Purpose / Membership / Decides) but is explicitly labeled "OPTIONAL." A model may skip it. Mechanism is right, enforcement is absent. |
| C-07 | All four output sections present | PASS | Four SECTION headings pre-filled; "Fill in every slot. Do not omit any template section." |
| C-08 | Decision rights indicated | PASS | Decision Scope column is built into SECTION 3 template; "Decision Scope column satisfies C-08" is stated explicitly. |
| C-09 | Org evolution path | FAIL | Not mentioned. |
| C-10 | Anti-patterns flagged | FAIL | Not mentioned. |

**Score:** Essential 5/5 (60) + Recommended 2.5/3 (25) + Aspirational 0/2 (0) = **85**
**Band:** Golden-adjacent (all essential pass, score ≥ 80 but C-06 partial)

---

### V-03 — Roles-First with Named ROLES-LOADED Step

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia assessment present | PASS | STEP 2 contains verdict + one-sentence roles-to-verdict connection. "Do not write an org diagram until the verdict is written." Strong because inertia draws on the loaded roles for coordination-failure analysis. |
| C-02 | ASCII org box rendered | PASS | STEP 3 with two-level minimum, two-node minimum, committees as distinct labeled nodes. |
| C-03 | Roles input honored | PASS | Strongest C-03 across all variations. STEP 1 is the first named action; produces ROLES-LOADED block before anything else is written. "Do not proceed to Step 2 until this block is written." Named roles anchor the entire subsequent design. |
| C-04 | Headcount by area | PASS | STEP 4 with two-area minimum, Key Roles column references ROLES-LOADED. |
| C-05 | Operating rhythm table | PASS | STEP 5 with ROB + shiproom + governance minimum. DRI/Owner references ROLES-LOADED where possible. |
| C-06 | Committee charters complete | PASS | STEP 6 is a named required step (not optional) with Purpose / Membership / Decides template. Conditional on committees in Step 5 (which are required), so it fires reliably. |
| C-07 | All four output sections present | PASS | STEP 7 ARTIFACT OUTPUT lists all four canonical sections in order. |
| C-08 | Decision rights indicated | PARTIAL | Headcount table is `Area \| Headcount \| Key Roles \| Notes` — Notes column exists but decision rights are not required content; no explicit instruction to fill it with decision scope. |
| C-09 | Org evolution path | FAIL | Not mentioned. |
| C-10 | Anti-patterns flagged | FAIL | Not mentioned. |

**Score:** Essential 5/5 (60) + Recommended 2.5/3 (25) + Aspirational 0/2 (0) = **85**
**Band:** Golden-adjacent (different strength profile from V-02: stronger C-03/C-06, weaker C-08)

---

### V-04 — Imperative DO/DO NOT Register + Inertia Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia assessment present | PASS | Strongest single-criterion protection across V-01–V-04. Seven explicit DO/DO NOT rules for inertia alone. "DO NOT write 'the team is growing' without specifying the headcount or coordination failure." No path to skip. |
| C-02 | ASCII org box rendered | PASS | "DO show at minimum two levels. DO NOT produce a flat list of names without hierarchy. DO NOT draw a single-node diagram." |
| C-03 | Roles input honored | PASS | "DO check .roles/ before writing anything. DO list every role found in ROLES-LOADED. DO NOT invent role names." |
| C-04 | Headcount by area | PASS | "DO include at minimum two distinct areas. DO NOT produce only a single total." Decision Scope column required. |
| C-05 | Operating rhythm table | PASS | "DO include at minimum three distinct rows. DO NOT combine two meetings into one row. DO NOT produce a rhythm table with only ROB." Three explicit prohibitions. |
| C-06 | Committee charters complete | PASS | "DO write a mini-charter for each committee. Each charter MUST include: Purpose, Membership, Decides." "DO NOT write a rhythm table row for a committee and then omit its charter." |
| C-07 | All four output sections present | PASS | SECTION ORDER lists six required sections. "DO NOT omit any of these six sections." |
| C-08 | Decision rights indicated | PASS | Decision Scope column required in headcount. "DO NOT write 'owns the area' — write what kinds of decisions are made at this level versus escalated upward." |
| C-09 | Org evolution path | FAIL | Not mentioned. |
| C-10 | Anti-patterns flagged | FAIL | Not mentioned. |

**Score:** Essential 5/5 (60) + Recommended 3/3 (30) + Aspirational 0/2 (0) = **90**
**Band:** Golden (all essential + ≥ 80)

---

### V-05 — Five-Phase Sequence with Per-Phase Output Contracts

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Inertia assessment present | PASS | Most substantive inertia formulation. Four required sub-sections: Status-quo defense (argues FOR doing nothing), Flat-team viability, Switching cost, VERDICT + re-assessment trigger. "Phase 2 complete when: VERDICT and re-assessment trigger are written." |
| C-02 | ASCII org box rendered | PASS | Phase 3 with two-level minimum, two-node minimum, committees as distinct labeled nodes. |
| C-03 | Roles input honored | PASS | Phase 1 is gated ("Phase 1 complete when: table is written"). Produces structured Roles table with Role/Archetype/Orientation columns. Absence path explicit. |
| C-04 | Headcount by area | PASS | Phase 3 headcount table with two-area minimum, Decides/Escalates split. "Phase 3 complete when: diagram and headcount table (with Decides/Escalates) are written." |
| C-05 | Operating rhythm table | PASS | Phase 4 with ROB + shiproom + governance. "Phase 4 complete when: three or more distinct rows are written." Completion gate enforces minimum. |
| C-06 | Committee charters complete | PASS | Phase 5 is a named phase (not optional) with explicit charter checklist. Charter elements: Purpose / Membership / Decides+Escalates. Checklist: `[ ] Purpose (one sentence) / [ ] Membership (roles, ≥2) / [ ] Decides/Escalates (≥1 each)`. "Phase 5 complete when: every governance row has a charter with all three elements checked." |
| C-07 | All four output sections present | PASS | ARTIFACT OUTPUT collects all five phase deliverables; four canonical sections are embedded within phases. |
| C-08 | Decision rights indicated | PASS | Decides/Escalates as two separate columns in Phase 3 headcount table — more explicit than a single Decision Scope column. "The Decides/Escalates split satisfies C-08." |
| C-09 | Org evolution path | PARTIAL | Phase 2 requires a "Trigger for re-assessment" — the headcount/milestone that would flip the verdict. This is a growth trigger, but it addresses when to adopt structure (not how structure evolves after adoption). Partial credit: concrete trigger required, but it precedes structure rather than describing structural evolution. |
| C-10 | Anti-patterns flagged | FAIL | Not mentioned. |

**Score:** Essential 5/5 (60) + Recommended 3/3 (30) + Aspirational 0.5/2 (2.5) = **92.5**
**Band:** Golden

---

### Rankings

| Rank | Variation | Score | Band | Key Differentiator |
|------|-----------|-------|------|--------------------|
| 1 | V-05 | 92.5 | Golden | Phase-completion gates + status-quo defense + Decides/Escalates split |
| 2 | V-04 | 90 | Golden | Imperative DO/DO NOT covering all recommended criteria |
| 3 | V-02 | 85 | Golden-adjacent | Section scaffolds lock C-07/C-08; charter is optional (C-06 partial) |
| 3 | V-03 | 85 | Golden-adjacent | Strongest C-03; C-06 pass; C-08 partial due to Notes column |
| 5 | V-01 | 70 | Acceptable | C-01 well-protected; charters and decision rights omitted entirely |

---

### Excellence Signals — V-05

The top-scoring variation produced four patterns not present (or weaker) in lower-ranked variations:

**1. Phase-completion contracts** — Each phase ends with an explicit `Phase N complete when: X` statement. This prevents partial execution: the model cannot begin Phase 3 (org design) before Phase 2 (inertia VERDICT) is written. The gate is verifiable by reading the output, not inferring intent.

**2. Status-quo defense sub-section** — Phase 2 includes an explicit "argue FOR doing nothing" step before proposing structure. This is the inertia-advocate lens operationalized: the skill must steel-man flat operation before the VERDICT is allowed to say STRUCTURE-WARRANTED. No other variation requires the model to argue the other side first.

**3. Switching cost as a required inertia sub-section** — Making formalization cost visible (reporting overhead, slower decisions, political weight of titles) prevents the skill from defaulting to structure when the cost difference is ambiguous.

**4. Decides/Escalates as two distinct columns** — Rather than a single "Decision Scope" column, V-05 forces `Decides` and `Escalates` as separate columns with separate minimum requirements (≥1 item each side). This prevents a vague "owns the area" statement from satisfying C-08.

---

```json
{"top_score": 92, "all_essential_pass": true, "new_patterns": ["phase-completion-contract: each phase ends with an explicit completion gate that prevents the next phase from executing, making partial execution detectable", "status-quo-defense: inertia section requires arguing FOR not formalizing before proposing structure — operationalizes the inertia-advocate lens", "decides-escalates-split: two distinct table columns with minimum requirements each side, stronger than a single Decision Scope column", "switching-cost-section: explicit formalization cost enumeration as a required inertia sub-section prevents defaulting to structure"]}
```
