Reading the R10 scorecard to identify the candidate v11 criteria before writing the updated rubric.

The scorecard explicitly names the R10 excellence signals: **"Three VM Row ID touch-points that lack consequence-form (CF) in R9 V-05"**, and states these target **candidate v11 criteria (C-33/C-34/C-35)**. The three sites where CF was probed across variations V-01 through V-05 correspond to the three enforcement timing points established by C-32 (CONSTRAINT MANIFEST load, COMPLIANCE CONTRACT, VERIFICATION MANIFEST). Each site gains its own CF-anchoring criterion.

New max: 210 + 5 + 5 + 5 = **225 pts**.

---

```markdown
# listen-support Quest Rubric — v11

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
| v8 | Added C-26 (Self-referential criterion enforcement), C-27 (Spine-as-sole-suspenders declaration) from R7 excellence signals. Max: 185 pts |
| v9 | Added C-28 (Compliance Contract spine-criterion anchoring), C-29 (Triple self-referential mechanism stack) from R8 excellence signals. Max: 195 pts |
| v10 | Added C-30 (Spine-row self-enforcement imperative), C-31 (Dual-load CONTRACT implementation), C-32 (Three-timing enforcement coverage) from R9 excellence signals. Max: 210 pts |
| v11 | Added C-33 (VM Row ID CF at constraint load), C-34 (VM Row ID CF in compliance contract), C-35 (VM Row ID CF in verification spine) from R10 excellence signals. Max: 225 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×27) | 5 | 2 | 0 |

**Max composite:** 225 pts  
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

### C-05 — Ticket body actionable and feedback-grounded
Each ticket body contains a specific, actionable description traceable to a source feedback item. Body text is not a paraphrase of the title. No placeholder language (e.g., "TBD", "see above", "N/A") appears in a scored body field.

**PASS:** All ticket bodies are actionable, traceable to a feedback item, and free of placeholder language.  
**PARTIAL:** Most bodies meet the criterion; one or more contain placeholder language or are non-actionable paraphrases of the title.  
**FAIL:** Bodies systematically absent, placeholder-filled, or not traceable to feedback items.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — [text unchanged from v10]

### C-07 — [text unchanged from v10]

### C-08 — [text unchanged from v10]

---

## Aspirational Criteria (5 pts each, max 135)

### C-09 — [text unchanged from v10]

### C-10 — [text unchanged from v10]

---

### C-11 — Phase as card field
[text unchanged from v10]

### C-12 — Fallback-grounded severity
[text unchanged from v10]

### C-13 — Mid-output verification block
[text unchanged from v10]

### C-14 — Phase+Title coexistence
[text unchanged from v10]

### C-15 — Temporal adoption window severity
[text unchanged from v10]

### C-16 — Prior-tool coverage in verification
[text unchanged from v10]

### C-17 — Phase-as-severity-key declaration
[text unchanged from v10]

### C-18 — Gate minimum correct at ≥7
[text unchanged from v10]

### C-19 — TABLE CHECK halt instruction
[text unchanged from v10]

### C-20 — Gap analysis coverage verification block
[text unchanged from v10]

### C-21 — Evidence-to-gap traceability with orphan-gap check
[text unchanged from v10]

### C-22 — Prohibited sentinel language on consequence fields
[text unchanged from v10]

### C-23 — Belt-and-suspenders criterion satisfaction
[text unchanged from v10]

### C-24 — Materialized-view traceability instruction
[text unchanged from v10]

### C-25 — Criterion-ID-named final verification spine
[text unchanged from v10]

### C-26 — Self-referential criterion enforcement
[text unchanged from v10]

### C-27 — Spine-as-sole-suspenders declaration
[text unchanged from v10]

### C-28 — Compliance Contract spine-criterion anchoring
[text unchanged from v10]

### C-29 — Triple self-referential mechanism stack
[text unchanged from v10]

### C-30 — Spine-row self-enforcement imperative
[text unchanged from v10]

### C-31 — Dual-load CONTRACT implementation
[text unchanged from v10]

### C-32 — Three-timing enforcement coverage
[text unchanged from v10]

---

### C-33 — VM Row ID consequence-form at constraint load
Each VM row cited in the CONSTRAINT MANIFEST carries a consequence-form (CF) clause — a stated enforcement action that fires if the VM value is violated. The CF clause must be bound to the VM Row ID (e.g., `VM-003-CF: halt and redeclare`), not stated as a free-floating or generic consequence note.

**PASS:** Every VM Row ID in the CONSTRAINT MANIFEST has a bound CF clause.  
**PARTIAL:** CF clause present but unbound to specific Row IDs, or absent on some rows while present on others.  
**FAIL:** No CF clauses on VM rows in the CONSTRAINT MANIFEST; or CONSTRAINT MANIFEST contains no VM Row IDs.

---

### C-34 — VM Row ID consequence-form in compliance contract
Each VM Row ID cited in the COMPLIANCE CONTRACT carries a consequence-form (CF) clause. The CF clause must name the VM Row ID and state the enforcement consequence for contract breach at that row.

**PASS:** Every VM Row ID referenced in the COMPLIANCE CONTRACT has a bound CF clause.  
**PARTIAL:** CF clause present but not bound to VM Row IDs, or missing on some contract entries while present on others.  
**FAIL:** No CF clauses on VM Row IDs in the COMPLIANCE CONTRACT; or the CONTRACT contains no VM Row ID references.

---

### C-35 — VM Row ID consequence-form in verification spine
Each VM Row ID checked in the VERIFICATION MANIFEST (or verification spine) carries a consequence-form (CF) clause specifying the action to take on a spine-row violation. The CF clause must be anchored to the VM Row ID within the spine row — not deferred to a separate consequences block.

**PASS:** Every VM Row ID in the VERIFICATION MANIFEST has an in-row CF clause.  
**PARTIAL:** CF clause deferred rather than in-row, or absent on some spine rows while present on others.  
**FAIL:** No CF clauses on VM Row IDs in the VERIFICATION MANIFEST; or VERIFICATION MANIFEST contains no VM Row ID references.
```

---

**What changed:**

| Item | Change |
|------|--------|
| Version history | v11 row added — names C-33/C-34/C-35, cites R10 probe |
| Scoring scale | Aspirational count 24→27, max 210→225 |
| C-33 | New: VM Row ID CF clause bound at constraint-load site |
| C-34 | New: VM Row ID CF clause bound in compliance-contract site |
| C-35 | New: VM Row ID CF clause bound in verification-spine site |

The three new criteria are the granular per-site complement to C-32 (three-timing coverage). C-32 asks whether enforcement spans all three moments; C-33/C-34/C-35 ask whether the CF clause is correctly bound at each individual moment.
