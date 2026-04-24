Now I have enough to score all 5 variations. Let me run the evaluation.

---

# mock-accept Variations R1 — Scoring

**Rubric version:** v1 | **Date:** 2026-03-16 | **Tier assumed:** 1 (no trace artifact; evaluating design intent)

**Scoring formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
**Golden threshold:** all 5 essential pass + composite >= 80

---

## V-01 — Inertia framing throughout

> Note: File starts at RULE 2 (line 33 truncation artifact — STEP 1 and RULE 1 beginning not directly visible). Scored against description + visible content.

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | Auto-flag rules fire correctly | **PASS** | RULES 2 and 3 visible with inertia notes; RULE 1 inferred from description + inertia-note pattern; AUTO-RULE CONTAMINATION GUARD named and present |
| C-02 | FORBIDDEN OUTPUTS TRIAD honored | **PASS** | All 3 labels in INERTIA GATE with "inertia cannot be overcome by..." language; two-of-three explicitly rejected |
| C-03 | Status write-back + CANARY | **PASS** | STEP 8 marked "mandatory, non-skippable"; CANARY ASSERTION template verbatim; CANARY-FALSE-POSITIVE named; CANARY SUPPRESSED fallback present |
| C-04 | Review artifact structure | **PASS** | STEP 7 present; 5-column table (adds Inertia outcome beyond the 4-column minimum); ordering rule stated; priority 1/2/3 labeled; risk statement with urgency |
| C-05 | MOCK-ACCEPTED slots + reason codes | **PASS** | SLOT 2 (Contrast) placed *before* SLOT 1 — strongest CONTRAST-INCOMPLETE prevention; both slots structurally separate; exact reason codes; SLOT-VIOLATION, CONTRAST-INCOMPLETE, RATIONALE-INCOMPLETE all named |
| C-06 | Entity-naming grammar in roles | **PASS** | All 3 role eval steps use entity-naming sub-question tables with "Contradiction found — name the specific element" and "Inconsistency found — name the specific element" prompts |
| C-07 | Guard compliance explicit | **PASS** | Two-list partition at STEP 2; Arch-blocked and Proceeding-to-Strategy lists recorded; Strategy-blocked and Proceeding-to-PM lists recorded; DO NOT proceed gates at each step |
| C-08 | REAL-REQUIRED evaluation template complete | **PASS** | All 5 fields (trigger, Failing evaluation, Failing verdict, SQ answer, Artifact state) present in STEP 6; VERDICT-ECHO named |
| C-09 | Risk statement with decision + urgency | **PASS** | "Highest-risk inertia gap: {namespace} — {specific Tier {tier} decision at risk} — urgency: {BLOCKING | HIGH | MEDIUM}"; urgency grouping commentary explicitly required |
| C-10 | Tier sourcing explicit | **PARTIAL** | STEP 1 not visible due to file truncation; consistent tier references in STEPS 3-5; cannot verify "Tier: N (source: ...)" statement format |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 1.5/2 → 7.5 pts

**Composite: 97.5** | All essential: YES | **Golden threshold: MET**

---

## V-02 — Role sequence: PM → Strategy → Architect

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | Auto-flag rules fire correctly | **PASS** | All 3 rules present; AUTO-RULE CONTAMINATION guard named; auto-flagged namespaces explicitly excluded from PM/Strategy/Arch via FORBIDDEN OUTPUTS TRIAD gate |
| C-02 | FORBIDDEN OUTPUTS TRIAD honored | **PASS** | All 3 labels in PHASE GATE block with "Completeness check: all 3 labels present. Two-of-three does not satisfy this gate" |
| C-03 | Status write-back + CANARY | **PASS** | STEP 8 "mandatory, non-skippable"; CANARY ASSERTION verbatim; CANARY-FALSE-POSITIVE named; CANARY SUPPRESSED fallback |
| C-04 | Review artifact structure | **PASS** | Correct path; 4-column table; ordering rule stated; priority 1/2/3; risk statement with urgency grouping |
| C-05 | MOCK-ACCEPTED slots + reason codes | **PASS** | SLOT 1 (Structural position) then SLOT 2 (Contrast); both dedicated and separate; exact reason codes; SLOT-VIOLATION warning; CONTRAST-INCOMPLETE warning; RATIONALE-INCOMPLETE warning |
| C-06 | Entity-naming grammar in roles | **PASS** | "Yes/no answers do not satisfy entity-naming sub-question requirements" stated explicitly at STEP 5 (Arch); entity-naming grammar invoked in all role steps |
| C-07 | Guard compliance explicit | **PASS** | Two-list partition at STEP 2; PM-blocked list recorded after STEP 3 with named error PM-TO-STRATEGY-GUARD-BYPASS; Strategy-blocked recorded after STEP 4 with STRATEGY-TO-ARCH-GUARD-BYPASS; GUARD-BYPASS CONTAMINATION named for entry violations; Arch is last role so no downstream contamination path exists |
| C-08 | REAL-REQUIRED evaluation template complete | **PASS** | All 5 fields present; VERDICT-ECHO named |
| C-09 | Risk statement with decision + urgency | **PASS** | Specific Tier {tier} decision at risk; urgency label enumerated; urgency grouping commentary when more than one namespace |
| C-10 | Tier sourcing explicit | **PASS** | STEP 1: "Output: 'Tier: {N} (source: TOPICS.md | --tier | default)'" stated explicitly |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 2/2 → 10 pts

**Composite: 100** | All essential: YES | **Golden threshold: MET**

---

## V-03 — Output format: table-first throughout

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | Auto-flag rules fire correctly | **PASS** | All 3 rules fire at STEP 2; auto-flagged rows get Arch = SKIP, Strategy = SKIP, PM = SKIP; "AUTO-RULE CONTAMINATION — any row with a non-empty Auto-flag cell must have Arch = Strategy = PM = SKIP" is a *structural* enforcement (empty cell = visible violation) |
| C-02 | FORBIDDEN OUTPUTS TRIAD honored | **PASS** | All 3 labels in PHASE GATE table-completeness check; "Two-of-three fails this gate" explicit |
| C-03 | Status write-back + CANARY | **PASS** | STEP 8 "mandatory, non-skippable"; CANARY ASSERTION verbatim; CANARY-FALSE-POSITIVE named; CANARY SUPPRESSED fallback |
| C-04 | Review artifact structure | **PASS** | STEP 7 writes from final decision table; 4-column Coverage Review table; ordering rule stated; priority 1/2/3; risk statement with urgency grouping |
| C-05 | MOCK-ACCEPTED slots + reason codes | **PASS** | SLOT 1 from Strategy SQ-1 cell; SLOT 2 dedicated and separate; exact reason codes; "Confirmatory sentence without named contrasting namespace = CONTRAST-INCOMPLETE. Merged slots = RATIONALE-INCOMPLETE" |
| C-06 | Entity-naming grammar in roles | **PASS** | Nested sub-question tables per step (STEP 3, 4, 5) make entity-naming violations immediately visible as empty or generic cells; "Yes/no answers do not satisfy" stated at STEP 3 |
| C-07 | Guard compliance explicit | **PASS** | Table state encodes guards structurally: SKIP cells prevent downstream contamination; ARCH-GUARD-BYPASS named; STRATEGY-TO-PM-GUARD-BYPASS named; entry conditions tied to table column values (Auto-flag = — AND Arch = CONSISTENT AND Strategy = ADEQUATE) |
| C-08 | REAL-REQUIRED evaluation template complete | **PASS** | All 5 fields present; "(sources from table row)" annotation adds traceability; VERDICT-ECHO named |
| C-09 | Risk statement with decision + urgency | **PASS** | "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk} — urgency:" with urgency grouping commentary |
| C-10 | Tier sourcing explicit | **PASS** | STEP 1: "State: 'Tier: {N} (source: TOPICS.md | --tier | default)'" and table initialized with Category column sourced from artifact |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 2/2 → 10 pts

**Composite: 100** | All essential: YES | **Golden threshold: MET**

---

## V-04 — Phrasing register + compressed lifecycle

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | Auto-flag rules fire correctly | **PASS** | All 3 rules present in prose form; AUTO-RULE CONTAMINATION named ("AUTO-RULE CONTAMINATION error and any resulting verdict is void") |
| C-02 | FORBIDDEN OUTPUTS TRIAD honored | **PASS** | All 3 labels present in acknowledgment form: "[EVIDENCE-HEAVY]: no auto-flagged namespace in this category will receive MOCK-ACCEPTED" x3; all 3 listed |
| C-03 | Status write-back + CANARY | **PASS** | Step 8 "this step is not skippable"; CANARY ASSERTION verbatim; CANARY-FALSE-POSITIVE named; CANARY SUPPRESSED fallback |
| C-04 | Review artifact structure | **PASS** | Step 7 writes file with three sections; 4-column table; ordering rule; priority 1/2/3; risk statement with urgency grouping |
| C-05 | MOCK-ACCEPTED slots + reason codes | **PASS** | SLOT 1 (structural position) and SLOT 2 (contrast) both present and separate; exact reason codes; SLOT-VIOLATION named; CONTRAST-INCOMPLETE named; RATIONALE-INCOMPLETE named |
| C-06 | Entity-naming grammar in roles | **PASS** | All 3 role steps use entity-naming framing with explicit anti-generic warning ("generic statements like 'the structure looks fine' or 'the mock is plausible' do not satisfy these questions"); example of valid vs invalid VERDICT-ECHO phrasing provided |
| C-07 | Guard compliance explicit | **PARTIAL** | Two-list partition written; "set aside — it does not proceed" language present for each role; BUT imperative DO NOT gates and inter-role guard error names (ARCH-GUARD-BYPASS, STRATEGY-TO-PM-GUARD-BYPASS) are removed; soft "set aside" framing without named errors reduces enforcement signal for step-transition guards |
| C-08 | REAL-REQUIRED evaluation template complete | **PASS** | All 5 fields present; VERDICT-ECHO with concrete example ("Section 4.2 lacks a tier-boundary gate" valid vs "Architect found no gate" is a VERDICT-ECHO error) — clearest VERDICT-ECHO guidance of all 5 variations |
| C-09 | Risk statement with decision + urgency | **PASS** | "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk} — urgency:" with urgency grouping commentary |
| C-10 | Tier sourcing explicit | **PASS** | Step 1: "Write out: 'Tier: {N} (source: TOPICS.md | --tier | default)'" |

**Essential:** 5/5 → 60 pts | **Recommended:** 2.5/3 → 25 pts | **Aspirational:** 2/2 → 10 pts

**Composite: 95** | All essential: YES | **Golden threshold: MET**

---

## V-05 — Strategy-first + inertia framing throughout

| ID | Criterion | Verdict | Evidence note |
|----|-----------|---------|---------------|
| C-01 | Auto-flag rules fire correctly | **PASS** | All 3 rules with inertia notes; "inertia is unconditional here: no role evaluation, no mock quality, and no user override lifts these flags"; AUTO-RULE CONTAMINATION guard named |
| C-02 | FORBIDDEN OUTPUTS TRIAD honored | **PASS** | INERTIA GATE with all 3 labels; "Two-of-three does not satisfy this gate"; labels framed as unconditional constraints |
| C-03 | Status write-back + CANARY | **PASS** | STEP 8 "mandatory, non-skippable"; CANARY ASSERTION verbatim; CANARY-FALSE-POSITIVE named; CANARY SUPPRESSED fallback |
| C-04 | Review artifact structure | **PASS** | Correct path; 4-column table; ordering rule stated; priority 1/2/3; risk statement with "Highest-risk inertia gap" framing and urgency grouping |
| C-05 | MOCK-ACCEPTED slots + reason codes | **PASS** | SLOT 1 framed as "Strategy SQ-1 anchor, established before plausibility and structure were checked" — strongest SLOT-VIOLATION prevention of all 5 variations; SLOT 2 dedicated and separate; exact reason codes; all 3 violation names present |
| C-06 | Entity-naming grammar in roles | **PASS** | Entity-naming sub-question tables with "Inertia direction" column per sub-question; "Contradiction found — name the specific element" and "Inconsistency found — name the specific element" |
| C-07 | Guard compliance explicit | **PASS** | Two-list partition at STEP 2; STRATEGY-TO-ARCH-GUARD-BYPASS named (new error name for V-05's order); ARCH-TO-PM-GUARD-BYPASS named (new error name); entry conditions stated at each step; "Named error for violating entry: GUARD-BYPASS CONTAMINATION" at each step |
| C-08 | REAL-REQUIRED evaluation template complete | **PASS** | All 5 fields; VERDICT-ECHO named; "propagates to next-steps" traceability explicit |
| C-09 | Risk statement with decision + urgency | **PASS** | "Highest-risk inertia gap: {namespace} — {specific Tier {tier} decision at risk} — urgency:" with urgency grouping commentary per priority group |
| C-10 | Tier sourcing explicit | **PASS** | STEP 1: "Tier: {N} (source: TOPICS.md | --tier | default)" as direct output |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 2/2 → 10 pts

**Composite: 100** | All essential: YES | **Golden threshold: MET**

---

## Rankings

| Rank | Variation | Score | All essential | Golden |
|------|-----------|-------|---------------|--------|
| 1 | V-02 | 100 | YES | YES |
| 1 | V-03 | 100 | YES | YES |
| 1 | V-05 | 100 | YES | YES |
| 4 | V-01 | 97.5 | YES | YES |
| 5 | V-04 | 95 | YES | YES |

**Tiebreaker analysis (100-point group):**

- **V-03** produces the structurally strongest guard enforcement: table SKIP cells make AUTO-RULE CONTAMINATION and GUARD-BYPASS CONTAMINATION immediately visible as a formatting violation, not just a textual instruction. Step 6 "confirms rather than authors" eliminates reconstruction-error drift.
- **V-05** produces the strongest C-05 design: SLOT 1 framed as "established before plausibility was checked" directly prevents the most common SLOT-VIOLATION (generic adequacy statements appear when the decision anchor wasn't named early). Layered inertia argument is hardest for LLM to satisfy with a vague response.
- **V-02** produces the cleanest disqualification chain: PM first filters the most mechanical failures before strategy or architecture judgment is expended.

**Top variation for excellence signals: V-03** (table enforcement is the most transferable structural pattern — removes a class of contamination errors rather than naming them).

---

## EXCELLENCE SIGNALS

Patterns from V-03 (primary) and V-05 (secondary) that made them strongest:

**E-01 — Table-as-ledger guard enforcement (V-03)**
Decision table initialized at STEP 1 with Final decision = REAL-REQUIRED for all rows. SKIP cells added for auto-flagged rows at STEP 2 are *structural* guards — a non-SKIP cell on an auto-flagged row is a visible table formatting violation, not a textual instruction that can be reasoned around. Guard compliance shifts from "do not do X" to "the table state is incorrect if X happens."

**E-02 — Strategy-first SLOT 1 anchoring (V-05)**
Running Strategy evaluation first establishes the tier decision anchor (SLOT 1) before architectural plausibility or structural completeness is checked. The SLOT 1 block is explicitly framed as "established before plausibility and structure were checked" — this prevents the most common SLOT-VIOLATION where an LLM fills SLOT 1 with generic adequacy language after the evaluation is complete.

**E-03 — Layered inertia-escape argument (V-01 + V-05)**
Framing each role evaluation as "adding one layer to the escape argument" (V-05) rather than "performing a check" changes the direction of the evaluation. An LLM must produce three named positive contributions to the escape argument; partial completion is explicitly named as "inertia holds." This reduces zero-argument acceptances more effectively than listing what is forbidden.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table-as-ledger guard enforcement: SKIP cells make contamination a structural table violation not a textual instruction", "strategy-first SLOT 1 anchoring: tier decision named before plausibility checked, framed as established-before to prevent generic completions", "layered inertia-escape framing: each role adds one named layer to the escape argument; incomplete argument explicitly holds inertia"]}
```
