```markdown
# listen-support Quest Rubric — v7

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 8 essential/recommended criteria |
| v2 | Added C-11 (Phase as card field), C-12 (Fallback-grounded severity), C-13 (Mid-output verification block) from R1 excellence signals. Max: 115 pts |
| v3 | Added C-14 (Phase+Title coexistence), C-15 (Temporal adoption window severity), C-16 (Prior-tool coverage in verification) from R2 excellence signals. Max: 130 pts |
| v4 | Added C-17 (Phase-as-severity-key declaration), C-18 (Gate minimum correct at ≥7) from R3 excellence signals. Max: 140 pts |
| v5 | Added C-19 (TABLE CHECK halt instruction), C-20 (Gap analysis coverage verification block) from R4 excellence signals. Max: 150 pts |
| v6 | Added C-21 (Evidence-to-gap traceability with orphan-gap check), C-22 (Prohibited sentinel language on consequence fields) from R5 excellence signals. Max: 160 pts |
| v7 | Added C-23 (Belt-and-suspenders criterion satisfaction), C-24 (Materialized-view traceability instruction), C-25 (Criterion-ID-named final verification spine) from R6 excellence signals. Max: 175 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×17) | 5 | 2 | 0 |

**Max composite:** 175 pts  
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

### C-06 — [carry from v6]

### C-07 — [carry from v6]

### C-08 — [carry from v6]

---

## Aspirational Criteria (5 pts each, max 85)

### C-09 — [carry from v6]

### C-10 — [carry from v6]

### C-11 — Phase as card field
[carry from v6]

### C-12 — Fallback-grounded severity
[carry from v6]

### C-13 — Mid-output verification block
[carry from v6]

### C-14 — Phase+Title coexistence
[carry from v6]

### C-15 — Temporal adoption window severity
[carry from v6]

### C-16 — Prior-tool coverage in verification
[carry from v6]

### C-17 — Phase-as-severity-key declaration
[carry from v6]

### C-18 — Gate minimum correct at ≥7
[carry from v6]

### C-19 — TABLE CHECK halt instruction
[carry from v6]

### C-20 — Gap analysis coverage verification block
[carry from v6]

### C-21 — Evidence-to-gap traceability with orphan-gap check
[carry from v6]

### C-22 — Prohibited sentinel language on consequence fields
[carry from v6]

---

### C-23 — Belt-and-suspenders criterion satisfaction
For any criterion that requires both a generation-time enforcement point and a post-generation audit, the prompt embeds two independent mechanisms: an inline column or annotation (blocks at generation) and a dedicated verification step (audits after generation). Either mechanism alone is sufficient for PARTIAL; both are required for PASS. If the model drops one under compression, the other survives.

**PASS:** At least one criterion in the prompt is satisfied by both an inline column/annotation at the generation step and a dedicated verification block at a subsequent step. The two mechanisms reference the same criterion and would each independently enforce or detect a violation.  
**PARTIAL:** Dual-layer enforcement applied to one criterion but the two layers are not independent (e.g., the verification step merely re-states the generation instruction without auditing output), or only one mechanism is present for a criterion that requires both.  
**FAIL:** No criterion uses dual independent enforcement layers; all verification is single-path.

---

### C-24 — Materialized-view traceability instruction
When the prompt requires a traceability or cross-reference table that echoes values from an earlier generated table, it instructs the model to populate the downstream table by copying values from the upstream table ("Populate [field] from the [earlier table] — same values") rather than re-deriving them independently. This converts a second-pass generation task into a transcription task, eliminating the risk of divergence between the two tables.

**PASS:** At least one instruction in the prompt explicitly directs the model to populate a downstream table field by copying from a named upstream table, using language equivalent to "same values" or "from the [step N] table." The upstream and downstream tables reference the same data (e.g., Gap IDs, ticket IDs).  
**PARTIAL:** A traceability table is required but the instruction asks the model to generate or derive the values rather than copy them, or the copy instruction is present but references fields that are not structurally linked in the output template.  
**FAIL:** No copy-from-upstream instruction present; traceability table (if present) is generated independently.

---

### C-25 — Criterion-ID-named final verification spine
A FINAL VERIFICATION block appears at or near the end of the prompt. It names each scored criterion by its ID (e.g., C-01, C-02, …, C-NN) and provides at least one explicit YES/NO sub-question per criterion. The block functions as a self-auditing spine: a scorer can determine criterion satisfaction by reading this block alone without scanning the full output. A halt or escalation instruction is present for any NO answer.

**PASS:** FINAL VERIFICATION block present; names every criterion by ID; each criterion has ≥1 YES/NO sub-question; a halt or escalation instruction fires on any NO.  
**PARTIAL:** FINAL VERIFICATION block present but covers only a subset of criteria by ID, or sub-questions are present without a halt instruction, or criteria are referenced by description rather than ID.  
**FAIL:** No FINAL VERIFICATION block, or the block does not reference criteria by ID.
```

Three changes from v6:

- **Version history** — v7 row added.
- **Scoring scale** — Aspirational tier updated from ×14 to ×17; max composite updated from 160 to 175.
- **New criteria** — C-23, C-24, C-25 added as aspirational (5 pts each), each with PASS/PARTIAL/FAIL ladder drawn directly from the R6 excellence signal descriptions.

The `[carry from v6]` stubs mark the sections whose wording was not included in the provided input; slot in the existing text verbatim.
