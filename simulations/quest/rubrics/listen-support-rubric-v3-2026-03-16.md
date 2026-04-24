Looking at the R2 scorecard, I can extract three new excellence patterns not yet captured in v2:

1. **C-14 — Phase + Title coexistence**: R2 revealed a structural displacement regression — variants adding Phase evicted Title; variants preserving Title lost Phase. V-03 has Title (C-01 PASS), V-01 has Phase (C-11 PASS), but none achieved both simultaneously on the card template. This is the synthesis target.

2. **C-15 — Temporal adoption window severity model**: V-03's transition curve (Day 0-30 → P2/P3, Day 61-90 → P0/P1) anchors severity in objective calendar position rather than fallback inference. Distinct from C-12: no fallback language required — the model reads the day-window and assigns the tier mechanically.

3. **C-16 — Prior-tool coverage as 4th verification dimension**: V-03's STEP 5B adds an explicit count of ticket bodies naming the prior tool by exact name, with PASS/FAIL. C-13 requires 3 checks (phase distribution, severity compliance, role diversity). C-16 is the 4th check that completes full traceability coverage.

---

```markdown
# listen-support Quest Rubric — v3

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 8 essential/recommended criteria |
| v2 | Added C-11 (Phase as card field), C-12 (Fallback-grounded severity), C-13 (Mid-output verification block) from R1 excellence signals. Max: 115 pts |
| v3 | Added C-14 (Phase+Title coexistence), C-15 (Temporal adoption window severity), C-16 (Prior-tool coverage in verification) from R2 excellence signals. Max: 130 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×8) | 5 | 2 | 0 |

**Max composite:** 130 pts  
**Golden gate:** all_essential_pass = TRUE AND composite ≥ 80

PARTIAL on any Essential criterion = all_essential_pass FALSE (Golden blocked regardless of composite).

---

## Essential Criteria (12 pts each, max 60)

### C-01 — Title field on card
Each ticket card includes `Title: [descriptive subject line]` as a named field. A ticket ID (`Ticket T-NN`) does not satisfy this criterion — Title must be a human-readable subject line that summarizes the feedback.

**PASS:** Every card has a `Title:` field with a descriptive value.  
**PARTIAL:** Title absent on some cards, or ticket ID used in place of subject line.  
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
**PARTIAL:** Minimum stated as a goal but not structurally enforced.  
**FAIL:** Fewer than 7 tickets and/or no enforcement mechanism.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — Phase distribution compliance
Phase distribution across tickets satisfies a minimum spread: Phase 1 ≥ 2, Phase 2 ≥ 1, Phase 3 ≥ 1. A TABLE CHECK or verification step enforces the distribution, not just requests it.

**PASS:** Distribution enforced structurally; output satisfies spread requirement.  
**PARTIAL:** Distribution stated as goal; verification present but not enforced with PASS/FAIL.  
**FAIL:** No distribution requirement or enforcement.

---

### C-07 — Phase-severity alignment
Phase maps to severity tier: Phase 1 (early adoption) → P2/P3; Phase 3 (deep adoption) → P0/P1. The alignment rule is stated explicitly and verified — TABLE CHECK or verification step confirms compliance.

**PASS:** Rule stated; TABLE CHECK or verification step confirms all cards comply.  
**PARTIAL:** Rule implied but not stated; or stated but not verified.  
**FAIL:** No phase-severity alignment rule.

---

### C-08 — Role/persona diversity
≥3 distinct Persona values appear across tickets. A TABLE CHECK or verification step enforces the diversity count.

**PASS:** Structural gate enforces ≥3 distinct Persona; output satisfies.  
**PARTIAL:** Diversity stated as goal; no enforcement.  
**FAIL:** Fewer than 3 distinct Persona or no diversity requirement.

---

## Aspirational Criteria (5 pts each, max 40)

### C-09 — Prior tool named in at least one body
At least one ticket body names the prior tool by its exact name from the planning step. This creates a concrete anchor for the "before" state of the adoption journey.

**PASS:** Prompt requires at least one exact prior tool citation in a body; output complies.  
**PARTIAL:** Prior tool appears in planning table or metadata only; not in any body text.  
**FAIL:** Prior tool never named in bodies.

---

### C-10 — Pre-commitment table before bodies
The planning table (Phase, Category, Persona, Volume, Severity for all tickets) is committed before any ticket body is written. Bodies must match the pre-committed table — no on-the-fly metadata assignment.

**PASS:** Explicit step locks all metadata in table; bodies written in a separate subsequent step; prompt states bodies must match table.  
**PARTIAL:** Table present but bodies not explicitly constrained to match; or table and bodies written in same step.  
**FAIL:** No pre-commitment table; metadata assigned inline with bodies.

---

### C-11 — Phase as first-class ticket card field
Phase appears as a named field on the ticket card template (`Phase: [Phase 1|2|3]`), not only in the planning table. Verification reads phase from card field values — not inferred from body text.

**PASS:** Card template has explicit `Phase:` field; verification reads from field.  
**PARTIAL:** Phase enforced via planning table and verification, but card template omits the field.  
**FAIL:** Phase tracked only in planning table; not present on card.

---

### C-12 — Fallback-grounded severity rationale
Severity is derived from fallback availability at adoption position. The inference rule is explicit: "I can still fall back to [PRIOR TOOL]" → P2/P3; "I can no longer use [PRIOR TOOL]" → P0/P1. The rule is stated in the prompt and applied per-ticket — severity is derived, not asserted.

**PASS:** Inference rule stated in prompt; per-ticket fallback language ("I can still…" / "I can no longer…") drives severity value; verification confirms consistency.  
**PARTIAL:** Phase-severity alignment enforced structurally (TABLE CHECK) but no per-card fallback language; severity derived from phase rule rather than explicit fallback statement.  
**FAIL:** No fallback-severity connection; severity assigned without rationale.

---

### C-13 — Mid-output verification block (3-dimension)
A verification block fires in the output between ticket bodies and gap analysis. It tabulates three dimensions with explicit PASS/FAIL verdicts:
1. Phase distribution counts per tier
2. Phase-severity compliance scan
3. Role/persona diversity count

The block appears in the output — it is observable, not silent.

**PASS:** All three dimensions present with PASS/FAIL verdicts; block fires between bodies and gap analysis.  
**PARTIAL:** Verification block present but missing one or more dimensions, or PASS/FAIL verdicts absent.  
**FAIL:** No mid-output verification block.

---

### C-14 — Phase and Title coexist on card template
The ticket card template includes both `Title:` and `Phase:` as distinct named fields — neither displaces the other. Addresses the R2 structural regression where adding Phase evicted Title and preserving Title evicted Phase.

**PASS:** Card template includes both `Title: [descriptive subject line]` and `Phase: [Phase 1|2|3]` as separate named fields.  
**PARTIAL:** One field present on template; the other captured only in planning table or omitted.  
**FAIL:** Neither field present on card template, or only one field with no planning-table coverage for the other.

---

### C-15 — Temporal adoption window as severity anchor
Severity tiers are anchored to explicit time windows in the adoption timeline (e.g., Day 0-30 → P2/P3, Day 31-60 → P1/P2, Day 61-90 → P0/P1). This makes severity objectively verifiable from calendar position alone — independent of fallback language (C-12). The time windows are declared in the planning step and referenced in verification.

**PASS:** Time-window table declared in planning step; severity tiers map to day/week ranges; TABLE CHECK or verification reads against declared windows.  
**PARTIAL:** Temporal framing present in prompt description but no explicit window table; severity-to-time mapping is implied rather than declared.  
**FAIL:** No temporal adoption model; severity anchored only to phase label or fallback language.

---

### C-16 — Prior-tool coverage in verification block
The mid-output verification block (see C-13) includes a fourth check: explicit count of ticket bodies naming the prior tool by exact name, with a PASS/FAIL verdict. Extends C-13 to cover prior tool traceability as a structural compliance dimension.

**PASS:** Verification block includes prior tool citation count with PASS/FAIL; fires alongside C-13 phase/severity/diversity checks.  
**PARTIAL:** Prior tool checked at end of output or in planning step, but not as a PASS/FAIL item inside the mid-output verification block.  
**FAIL:** No prior tool coverage check.

---

## Composite Scoring Table

| Bucket | Criteria | Max |
|--------|----------|-----|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational | C-09 through C-16 | 40 |
| **Total** | | **130** |

---

## Golden Gate

```
GOLDEN = all_essential_pass AND composite >= 80
```

`all_essential_pass` = TRUE only if every Essential criterion scores PASS (12 pts). Any PARTIAL or FAIL on C-01 through C-05 blocks Golden regardless of composite.

---

## Criterion Dependency Map

```
C-01 + C-11 → C-14   (Title + Phase must coexist; displacement = regression)
C-07 + C-12 → C-15   (Phase-severity alignment upgrades to temporal model)
C-13 + C-09 → C-16   (Verification block gains prior-tool as 4th dimension)
C-10 → C-11          (Pre-commitment table is prerequisite for Phase-as-field)
```

Variants that pass C-14 solve the R2 Title/Phase displacement regression.  
Variants that pass C-15 provide objective severity verification without requiring fallback prose.  
Variants that pass C-13 + C-16 achieve full 4-dimension structural verification coverage.
```

---

**What changed in v3 vs v2:**

- **C-14** (Phase + Title coexistence): Aspirational. Codifies the R2 regression pattern — 4 of 5 variants dropped Title when adding Phase. No R2 variant passed this yet; it is the synthesis target for R3.
- **C-15** (Temporal adoption window severity): Aspirational. V-03's transition curve pattern elevated to a standalone criterion. Distinct from C-12 (fallback language) — anchors severity in observable calendar position, no inference required.
- **C-16** (Prior-tool coverage in verification block): Aspirational. V-03's STEP 5B 4th check. Extends C-13 (3-dimension) to full 4-dimension coverage. Variants pass C-13 without C-16 until they add the prior-tool count to the block.
- **Aspirational bucket**: 5 → 8 criteria, 25 → 40 pts. **Max composite: 115 → 130.**
- **Golden threshold unchanged:** all_essential_pass + composite ≥ 80.
