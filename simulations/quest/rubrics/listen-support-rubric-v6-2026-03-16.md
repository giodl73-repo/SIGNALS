```markdown
# listen-support Quest Rubric — v6

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 8 essential/recommended criteria |
| v2 | Added C-11 (Phase as card field), C-12 (Fallback-grounded severity), C-13 (Mid-output verification block) from R1 excellence signals. Max: 115 pts |
| v3 | Added C-14 (Phase+Title coexistence), C-15 (Temporal adoption window severity), C-16 (Prior-tool coverage in verification) from R2 excellence signals. Max: 130 pts |
| v4 | Added C-17 (Phase-as-severity-key declaration), C-18 (Gate minimum correct at ≥7) from R3 excellence signals. Max: 140 pts |
| v5 | Added C-19 (TABLE CHECK halt instruction), C-20 (Gap analysis coverage verification block) from R4 excellence signals. Max: 150 pts |
| v6 | Added C-21 (Evidence-to-gap traceability with orphan-gap check), C-22 (Prohibited sentinel language on consequence fields) from R5 excellence signals. Max: 160 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×14) | 5 | 2 | 0 |

**Max composite:** 160 pts  
**Golden gate:** all_essential_pass = TRUE AND composite ≥ 80

PARTIAL on any Essential criterion = all_essential_pass FALSE (Golden blocked regardless of composite).

---

## Essential Criteria (12 pts each, max 60)

### C-01 — Title field on card
Each ticket card includes `Title: [descriptive subject line]` as a named field. A ticket ID (`Ticket T-NN`) does not satisfy this criterion — Title must be a human-readable subject line that summarizes the feedback. A heading of the form `## T-NN — {Title}` does not satisfy this criterion; the title must appear as a discrete named field in the card body.

**PASS:** Every card has a `Title:` field with a descriptive value.  
**PARTIAL:** Title absent on some cards, or ticket ID used in place of subject line, or title embedded in heading only.  
**FAIL:** No title field on any card.

---

### C-02 — Controlled vocabulary declared and enforced
Phase, Category, Volume, and Severity use controlled vocabularies declared in the planning table. The model enforces values — no free-form variants accepted in scored fields.

**PASS:** Vocabulary table present; all card values match declared options.  
**PARTIAL:** Vocabulary declared but not consistently enforced.  
**FAIL:** Free-form values used; no vocabulary declaration.

---

### C-03 — First-person voice throughout
All ticket bodies written in first person. No role titles in body text. The voice constraint is stated explicitly in the prompt (e.g., "Write as me — first person throughout. No role titles in body text.").

**PASS:** All bodies pass first-person check; constraint is stated in prompt.  
**PARTIAL:** Constraint stated but some bodies break first-person or include role titles.  
**FAIL:** Constraint absent or systematically violated.

---

### C-04 — Gap analysis with three named sections
A gap analysis step (distinct from ticket generation) produces three sections: Doc Gaps, Design Gaps, Operational Gaps. Each section must reference ≥1 named artifact.

**PASS:** All three sections present, each with ≥1 named artifact.  
**PARTIAL:** Sections present but one or more is empty or unnamed.  
**FAIL:** Gap analysis absent or fewer than three sections.

---

### C-05 — Minimum ticket count enforced with structural gate
A TABLE CHECK block appears after the planning table and before ticket generation. The block verifies that declared phase or layer minimums sum to ≥7. An explicit halt instruction names the next step and blocks progression until the check passes (e.g., "Do not proceed to STEP 4 until this check shows YES"). The minimum must be declared structurally, not as an advisory instruction.

**PASS:** TABLE CHECK block present with halt instruction naming the blocked step; minimums sum to ≥7; gate is structural not advisory.  
**PARTIAL:** TABLE CHECK or halt instruction present but minimum is < 7, or enforcement is advisory language without a named gate.  
**FAIL:** No TABLE CHECK, no halt instruction, or no minimum declared.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — Phase target declared before ticket generation
A phase target table or PHASE-ROLE MAP is declared before ticket generation begins. The table names each phase and specifies a minimum ticket count or role priority for that phase. Targets are declared as a lookup structure, not embedded in prose.

**PASS:** Phase target table or map present before the ticket generation step; each phase has a named minimum or priority.  
**PARTIAL:** Phase targets declared in prose or only implicitly; no lookup structure.  
**FAIL:** No phase concept; no pre-generation targeting.

---

### C-07 — Role-phase matrix
A role-phase matrix presents ≥4 distinct role rows, each mapped to one or more phases, with priority or sequencing indicated. The matrix must have both a role dimension and a phase dimension — a phase map with no role rows, or a role list with no phase association, does not satisfy this criterion.

**PASS:** Matrix has ≥4 role rows and a phase dimension; priority or sequence indicated per cell.  
**PARTIAL:** Phase-row map with role priority but fewer than 4 role rows; or role-phase association implied but not structured as a matrix.  
**FAIL:** No role-phase matrix; phase concept absent; or role list with no phase mapping.

---

### C-08 — Migration framing present
A STATUS QUO section names the specific prior tool, the friction point that motivates migration, and the first action the user takes with the new feature. Each ticket card includes a STATUS QUO connection field linking the ticket to a named prior-tool element.

**PASS:** STATUS QUO section present with tool name, friction point, and first new-feature action; every card has a STATUS QUO connection field.  
**PARTIAL:** STATUS QUO section present but card connection field absent or unnamed; or prior tool named without friction point.  
**FAIL:** No migration framing; no prior-tool reference.

---

## Aspirational Criteria (5 pts each, max 70)

### C-09 — Cross-ticket pattern table
A CROSS-TICKET PATTERN step produces a structured table with named fields shared across tickets (e.g., Root Cause, Consequence, Recurrence Risk). At least three Consequence-class fields are present.

**PASS:** CROSS-TICKET PATTERN table present with ≥3 consequence-class named fields populated.  
**PARTIAL:** Pattern table present but fewer than 3 consequence fields, or fields unnamed.  
**FAIL:** No cross-ticket pattern step.

---

### C-10 — Resolution paths for high-severity tickets
High-severity tickets (P0/P1) include a named resolution path — a concrete next action, owner role, or escalation route. A gap-level priority ordering does not satisfy this criterion; resolution paths must be per-ticket.

**PASS:** Every P0/P1 ticket has a named resolution path field.  
**PARTIAL:** Resolution paths present at gap level only; or present on some but not all high-severity tickets.  
**FAIL:** No resolution paths; severity-only labeling with no action path.

---

### C-11 — Phase as card field with day range
Each card includes a `Phase:` field with both the phase label and its day range (e.g., `Phase 2 (day 8–30)`). Phase label alone, without the day range, does not satisfy this criterion.

**PASS:** Every card has a `Phase:` field with label and day range.  
**PARTIAL:** Phase label present on cards but day range absent; or day range present in planning table but not propagated to card field.  
**FAIL:** No Phase field on cards.

---

### C-12 — Fallback-grounded severity
Severity assignment includes an explicit fallback rule for tickets whose phase is ambiguous or unlabeled (e.g., "if phase is unclear, assign P2"). A norm-based rule (workaround availability) without an ambiguous-phase fallback does not satisfy this criterion.

**PASS:** Severity rule present; explicit fallback clause for ambiguous-phase tickets names the default value.  
**PARTIAL:** Severity rule present but fallback is a general tie-breaker, not an ambiguous-phase-specific clause.  
**FAIL:** No severity rule; or severity rule with no fallback of any kind.

---

### C-13 — Mid-output verification block
A named verification step appears after ticket generation and before the gap analysis. The block checks at minimum: phase distribution against declared targets, severity distribution against P0/P1 limits, and role diversity. Each check produces a PASS/FAIL gate.

**PASS:** Verification block present post-generation; checks phase distribution, severity compliance, and role diversity; each check has a PASS/FAIL output.  
**PARTIAL:** Verification block present but checks fewer than three dimensions, or outputs are advisory rather than PASS/FAIL.  
**FAIL:** No mid-output verification block.

---

### C-14 — Phase and Title coexistence verified
Both Phase and Title appear as discrete named fields in every card, and the verification block (C-13) includes an explicit coexistence check confirming both fields are present. Coexistence on the card template alone, without a verification gate, does not satisfy this criterion.

**PASS:** Phase and Title both present as card fields; verification block includes a named coexistence check with PASS/FAIL.  
**PARTIAL:** Both fields present on cards but no verification gate; or verification gate present but not scoped to coexistence.  
**FAIL:** Phase or Title absent from cards; no coexistence check.

---

### C-15 — Temporal adoption window severity model
Severity assignment uses a day-window lookup table tied to phase definitions. Each phase row specifies a severity range (e.g., P0–P1 permitted in days 1–7; P2–P3 required in days 31+). An explicit override prohibition states that severity may not be assigned outside the window range for that phase.

**PASS:** Day-window severity lookup table present; override prohibition stated; assignment rules are phase-derived not workaround-derived.  
**PARTIAL:** Phase day windows declared but no severity ranges per window; or severity ranges present but no override prohibition.  
**FAIL:** No day-window concept; severity assigned by workaround availability independent of phase.

---

### C-16 — Prior-tool coverage as 4th verification check
The mid-output verification block (C-13) includes a fourth check confirming that every named STATUS QUO element from the migration framing appears in at least one ticket's STATUS QUO connection field. The check names a minimum citation count and outputs PASS/FAIL.

**PASS:** Verification block has ≥4 checks; fourth check explicitly scoped to prior-tool coverage; minimum citation count named; PASS/FAIL output.  
**PARTIAL:** Prior-tool coverage assessed outside the verification block (e.g., in a separate coverage trace table) but not as a named gate inside the block.  
**FAIL:** No prior-tool coverage check of any kind; verification block absent.

---

### C-17 — Phase-as-severity-key declaration
The prompt explicitly declares: "Phase is the lookup key for severity assignment" (or equivalent). An additional constraint states that no override path exists — severity may not be reassigned after phase is determined. A workaround-based severity rule does not satisfy this criterion regardless of quality.

**PASS:** Explicit declaration that phase is the severity lookup key; no-override constraint stated.  
**PARTIAL:** Phase-severity relationship implied by structure but not explicitly declared as a lookup key; no-override clause absent.  
**FAIL:** Severity derived from workaround availability; phase not mentioned as a severity input.

---

### C-18 — Gate minimum correct at ≥7
The structural gate (C-05) declares a minimum ticket count of ≥7. A gate with a minimum below 7 does not satisfy this criterion even if all other gate mechanics are correct.

**PASS:** TABLE CHECK gate present; declared minimum is ≥7.  
**PARTIAL:** Gate present with a declared minimum below 7.  
**FAIL:** No gate; or gate present with no minimum declared.

---

### C-19 — TABLE CHECK halt instruction with named target step
The TABLE CHECK block includes an explicit halt instruction that names the specific next step being blocked (e.g., "Do not proceed to STEP 4 until this check shows YES"). A generic "verify before proceeding" instruction without naming the blocked step does not satisfy this criterion.

**PASS:** TABLE CHECK block present; halt instruction names the specific blocked step by number or label; instruction is imperative not advisory.  
**PARTIAL:** Halt instruction present but does not name the specific target step; or instruction is advisory ("should verify") not imperative.  
**FAIL:** No TABLE CHECK block; no halt instruction.

---

### C-20 — Gap analysis coverage verification block
A verification block (distinct from mid-output verification, C-13) appears after the gap analysis step. It checks each of the three gap sections (Doc, Design, Operational) individually and produces a PASS/FAIL per section based on whether ≥1 named artifact is present. All three checks must be named and gated.

**PASS:** Post-gap verification block present; three named checks (one per gap section); each check produces PASS/FAIL; gated on ≥1 named artifact per section.  
**PARTIAL:** Coverage trace table checks ticket-to-gap linkage but does not verify per-section artifact presence with PASS/FAIL gates; or only some sections are checked.  
**FAIL:** No post-gap verification block; gap section completeness not checked.

---

### C-21 — Evidence-to-gap traceability with orphan-gap check
A 3-column COVERAGE TRACE TABLE (Ticket ID / STATUS QUO element traced / Gap ID traced to) links every ticket to both a named prior-tool element and a specific Gap ID. An explicit orphan-gap check follows the table and requires naming any gap item from the gap analysis that has no supporting ticket — the check must produce a named list or a "none" confirmation, not a blanket assertion. Distinct from C-20 (which checks gap section completeness) and C-16 (which checks prior-tool citation count): this criterion closes the ticket-evidence-to-gap-claim loop.

**PASS:** 3-column COVERAGE TRACE TABLE present linking every ticket to a STATUS QUO element and a Gap ID; orphan-gap check present with explicit named output (gap IDs with no ticket, or "none").  
**PARTIAL:** Coverage trace table present but missing the Gap ID column; or orphan-gap check absent; or check is a blanket assertion without naming gaps.  
**FAIL:** No coverage trace table; no gap traceability mechanism.

---

### C-22 — Prohibited sentinel language on consequence fields
CROSS-TICKET PATTERN consequence fields carry explicit `Prohibited:` lists naming disallowed value patterns (e.g., `Prohibited: "users", "this will cause confusion", "this will slow adoption"`). Prohibited lists must name specific disallowed strings or patterns, not generic quality instructions. The prohibition forces named stock roles, specific events with ticket references, and quantified friction statements. Complementary to C-02 (controlled vocabulary on fixed-vocabulary fields) but applied to free-text consequence fields.

**PASS:** Every consequence-class field in the CROSS-TICKET PATTERN step carries a `Prohibited:` list naming ≥2 specific disallowed patterns; pattern list includes at least one role-vagueness term (e.g., "users") and one impact-vagueness term (e.g., "this will cause confusion").  
**PARTIAL:** `Prohibited:` list present on some but not all consequence fields; or list names only generic quality guidance without specific disallowed strings.  
**FAIL:** No `Prohibited:` lists on consequence fields; anti-vagueness enforced only through examples or instructions, not prohibition lists.
```
