Good — the full v4 body is here. Now I can identify the R4 signals.

From the scorecard, two new patterns emerged that are not yet criteria:

1. **V-03 C-04**: "STEP 9 with Doc/Design/Operational sections + **GAP CLASSIFICATION COVERAGE block**" — a structural verification appended to the gap analysis step, analogous to C-13 (mid-output verification) but scoped to gap output.

2. **V-03 C-05**: TABLE CHECK includes "**Do not proceed to STEP 4 until this check shows YES**" — an explicit halt instruction with a named target step. Distinct from C-18 (threshold correctness): this captures the blocking enforcement semantics.

Those become C-19 and C-20. Here is the complete v5 rubric:

---

```markdown
# listen-support Quest Rubric — v5

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 8 essential/recommended criteria |
| v2 | Added C-11 (Phase as card field), C-12 (Fallback-grounded severity), C-13 (Mid-output verification block) from R1 excellence signals. Max: 115 pts |
| v3 | Added C-14 (Phase+Title coexistence), C-15 (Temporal adoption window severity), C-16 (Prior-tool coverage in verification) from R2 excellence signals. Max: 130 pts |
| v4 | Added C-17 (Phase-as-severity-key declaration), C-18 (Gate minimum correct at ≥7) from R3 excellence signals. Max: 140 pts |
| v5 | Added C-19 (TABLE CHECK halt instruction), C-20 (Gap analysis coverage verification block) from R4 excellence signals. Max: 150 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×12) | 5 | 2 | 0 |

**Max composite:** 150 pts  
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

### C-05 — Minimum ticket count enforced
The output contains ≥7 tickets. A TABLE CHECK or equivalent structural gate enforces the minimum — not just a soft instruction.

**PASS:** Structural gate enforces ≥7 rows; output meets the minimum.  
**PARTIAL:** Structural gate present but enforces a lower threshold (e.g., ≥6); output meets that lower threshold.  
**FAIL:** No structural gate; ticket count not enforced.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — Phase target declared before ticket generation
Before any ticket is written, Step 1 (or equivalent planning step) declares the Phase 1/Phase 2/Phase 3 distribution targets. The targets anchor the role-phase matrix and severity assignment that follow.

**PASS:** Phase targets declared in a planning step prior to ticket generation.  
**PARTIAL:** Phase targets mentioned but not declared as a prior planning step.  
**FAIL:** No phase target declaration.

---

### C-07 — Role-phase matrix
A role-phase cross-matrix is present with ≥4 role rows and per-phase constraints (e.g., Phase 1 → SRE + Power User focus). The matrix must appear as a named planning artifact, not as inline commentary.

**PASS:** Named matrix artifact with ≥4 role rows and phase constraints.  
**PARTIAL:** Matrix present but fewer than 4 roles, or no per-phase constraints.  
**FAIL:** No role-phase matrix.

---

### C-08 — Migration framing present
The prompt encodes prior-tool knowledge — e.g., a Status Quo Analysis step, references to what users did in the old system, or a constraint that body text must name the transition explicitly. Migration framing is not just a label; it shapes ticket content.

**PASS:** Dedicated migration framing step or constraint present; tickets reflect prior-system knowledge.  
**PARTIAL:** Migration framing mentioned but not operationalized in ticket content.  
**FAIL:** No migration framing.

---

## Aspirational Criteria (5 pts each, max 60)

### C-09 — Cross-ticket pattern table
A synthesis step (distinct from gap analysis) produces a table of cross-ticket patterns — recurring themes, role clusters, or phase concentrations across the ticket set.

**PASS:** Cross-ticket pattern table present as a named output step.  
**PARTIAL:** Pattern discussion present but not as a structured table.  
**FAIL:** No cross-ticket synthesis.

---

### C-10 — Resolution paths for high-severity tickets
A resolution path table or equivalent structure is present for high-volume or P0/P1 tickets, specifying owner type and next action per ticket or cluster.

**PASS:** Resolution path table present covering high-severity or high-volume tickets.  
**PARTIAL:** Resolution paths mentioned inline but not as a structured artifact.  
**FAIL:** No resolution paths.

---

### C-11 — Phase as card field
Each ticket card includes `Phase: Phase N (day X–Y)` as a named metadata field — not just as a category tag or in the heading. The day range is included.

**PASS:** Every card has a `Phase:` named field with day range.  
**PARTIAL:** Phase present on some cards, or day range omitted.  
**FAIL:** Phase absent as a card field.

---

### C-12 — Fallback-grounded severity
When a ticket's phase position is ambiguous, severity is assigned by explicit fallback rule (e.g., "if phase is unclear, assign P2 as default") rather than free inference. The fallback rule is stated in the planning section.

**PASS:** Explicit fallback severity rule stated; applied consistently.  
**PARTIAL:** Severity norm mentioned but no explicit fallback rule for ambiguous cases.  
**FAIL:** Severity assigned by unconstrained inference.

---

### C-13 — Mid-output verification block
A verification step (Step 9 or equivalent) appears after ticket generation and performs at least three structural checks: phase distribution, severity compliance, role diversity. The block outputs PASS/FAIL per check.

**PASS:** Verification block present with ≥3 named checks and PASS/FAIL output.  
**PARTIAL:** Verification step present but fewer than 3 checks, or checks are soft reminders not gates.  
**FAIL:** No verification block.

---

### C-14 — Phase+Title coexistence
Both `Title:` and `Phase:` appear as discrete named fields on the same card — neither embedded in the heading. The card template definition requires both fields explicitly, and the verification block (C-13) includes a coexistence check ("both fields present").

**PASS:** Both fields present as named fields on every card; verification checks coexistence.  
**PARTIAL:** Both fields present on some cards, or verification check absent.  
**FAIL:** One or both fields absent as named fields; or title embedded in heading.

---

### C-15 — Temporal adoption window severity model
Severity is assigned by a mechanical day-window lookup table (e.g., Day 0–30 → P2/P3, Day 31–60 → P1/P2, Day 61–90 → P0/P1) rather than by inference or norm with override. No override path exists. The verification block includes a mechanical compliance check against the table.

**PASS:** Day-window lookup table present; no override path; verification checks mechanical compliance.  
**PARTIAL:** Day-window table present but override path exists, or verification check absent.  
**FAIL:** Severity assigned by inference or norm language; no day-window table.

---

### C-16 — Prior-tool coverage as 4th verification check
Step 1 (or equivalent) declares the prior tool's exact name. The vocabulary table includes a `Prior-tool ref?` column requiring ≥2 Y values. The verification block (C-13) adds a 4th check: prior-tool citation count with PASS/FAIL gate, completing full traceability coverage.

**PASS:** Prior tool named in planning step; vocabulary column present; 4th verification check gates on citation count.  
**PARTIAL:** Prior tool named but vocabulary column absent, or verification check absent.  
**FAIL:** No prior-tool traceability mechanism.

---

### C-17 — Phase-as-severity-key declaration
The Phase field is explicitly declared as the *lookup key* for severity assignment within the card template definition or the Phase/Severity rule block — not merely as a metadata label. The rule block states "No override path exists" as an explicit constraint. This makes the Phase→Severity relationship structurally declared and machine-checkable from the template alone, not just implied by C-14 and C-15 in combination.

**PASS:** Card template or rule block explicitly names Phase as the severity lookup key; "No override path exists" stated as a constraint.  
**PARTIAL:** Phase-severity relationship described but not declared as a structural rule; override prohibition absent.  
**FAIL:** Phase and severity rules exist independently with no declared coupling.

---

### C-18 — Gate minimum correct at ≥7
The TABLE CHECK or structural gate (C-05) enforces exactly ≥7 tickets — not ≥6 or any lower threshold. This criterion is only reachable if C-05 is at least PARTIAL (gate present); C-18 awards the point for threshold correctness.

**PASS:** Structural gate enforces ≥7; C-05 is PASS.  
**PARTIAL:** Gate enforces ≥7 but C-05 is PARTIAL for another reason (e.g., gate wording ambiguous).  
**FAIL:** Gate enforces < 7, or no structural gate present.

---

### C-19 — TABLE CHECK halt instruction
The TABLE CHECK block includes an explicit halt instruction that names the target next step and requires a YES/NO resolution before permitting progression (e.g., "Do not proceed to STEP 4 until this check shows YES"). Distinct from C-18 (threshold correctness): C-19 captures the *blocking enforcement semantics* — the gate is a hard stop, not an advisory warning. The halt instruction must name a specific step number, not just say "do not continue."

**PASS:** TABLE CHECK block contains a named-step halt instruction with a YES/NO progression gate.  
**PARTIAL:** Halt language present but step number absent, or phrasing is advisory rather than blocking.  
**FAIL:** No halt instruction in the TABLE CHECK block; or no TABLE CHECK block present.

---

### C-20 — Gap analysis coverage verification block
A structural coverage verification block (e.g., GAP CLASSIFICATION COVERAGE) is appended to the gap analysis step, confirming that all three gap types (Doc, Design, Operational) each contain at least one named artifact. Mirrors C-13 (mid-output verification for tickets) applied to the gap analysis output. The block must output a PASS/FAIL result per gap type, not merely restate the gap table.

**PASS:** Coverage verification block present in the gap analysis step; PASS/FAIL output per gap type with named-artifact check.  
**PARTIAL:** Coverage summary present but no per-type PASS/FAIL output, or artifact naming not verified.  
**FAIL:** No coverage verification block in the gap analysis step.
```

---

**Two new patterns extracted from R4:**

- **C-19 (TABLE CHECK halt instruction)** — V-03's TABLE CHECK included "Do not proceed to STEP 4 until this check shows YES." The halt instruction with a named target step makes the gate a hard stop. C-18 rewards threshold correctness (≥7); C-19 rewards blocking enforcement semantics. Both can pass independently.

- **C-20 (Gap analysis coverage verification block)** — V-03's STEP 9 appended a GAP CLASSIFICATION COVERAGE block confirming per-type artifact presence. This is the gap-output analogue of C-13: a PASS/FAIL gate on the gap table itself, not just on the ticket set.

Max composite rises from 140 → **150 pts** (12 aspirational criteria × 5 pts each = 60 + 60 essential/recommended = 150).
