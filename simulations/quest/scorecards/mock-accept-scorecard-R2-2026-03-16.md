## mock-accept Round 2 — Scorecard

---

### Rubric Criteria Reference

| ID | Weight | Category | Pts |
|----|--------|----------|-----|
| C-01 | essential | DO-NOT gates + FORBIDDEN OUTPUTS TRIAD | 12 |
| C-02 | essential | Triad labels all present | 12 |
| C-03 | essential | Status write-back + CANARY ASSERTION | 12 |
| C-04 | essential | Review artifact with required structure | 12 |
| C-05 | essential | MOCK-ACCEPTED two-slot positive argument | 12 |
| C-06 | recommended | Entity-naming grammar | 10 |
| C-07 | recommended | Step sequencing + guard compliance | 10 |
| C-08 | recommended | Evaluation-driven REAL-REQUIRED template | 10 |
| C-09 | aspirational | Risk statement with urgency grouping | 2 |
| C-10 | aspirational | Tier sourcing explicit | 2 |
| C-11 | aspirational | Named guard-bypass error codes | 2 |
| C-12 | aspirational | Slot 2 before Slot 1 ordering | 2 |
| C-13 | aspirational | SKIP cells structural enforcement | 2 |

Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)`

Scoring convention: PARTIAL = 0.5 pass. N/A (C-13 for prose-only) = 0 toward numerator, denominator stays 5.

---

## V-01 — Phrasing Register: Slot 2 Before Slot 1

**Axis:** phrasing-register | **Target:** C-12

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | FORBIDDEN OUTPUTS TRIAD all 3 labels present; "Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate." AUTO-RULE CONTAMINATION GUARD with named error. |
| C-02 | **PASS** | [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] all labeled in triad section. |
| C-03 | **PASS** | Step 8 explicit with Edit tool instruction, CANARY ASSERTION verbatim, CANARY-FALSE-POSITIVE named, CANARY SUPPRESSED branch defined. |
| C-04 | **PASS** | Step 7 writes to `simulations/mock/{topic}-accept-{date}.md`; Coverage Review table with 4 columns; priority-ordered next-steps (P1/P2/P3); cross-namespace risk statement with urgency labels. |
| C-05 | **PASS** | "WRITE CONTRAST SLOT FIRST" imperative; Contrast (SLOT 2) label precedes Structural position (SLOT 1) in template; reason codes enumerated exactly (no paraphrase); SLOT-ORDER-INVERSION named as error. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Entity-naming grammar required; "Yes/no answers do not satisfy entity-naming sub-question requirements." Sub-questions ask to Name specific components. |
| C-07 | **PASS** | Two-list partition output explicit; Arch-blocked list recorded; Strategy-blocked list recorded; ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS named; proceeding lists explicit. |
| C-08 | **PASS** | Full evaluation-driven REAL-REQUIRED template: trigger, Failing evaluation, Failing verdict, SQ answer (artifact as subject), Artifact state. VERDICT-ECHO named. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Step 7 risk statement: specific Tier N decision at risk + urgency label (BLOCKING \| HIGH \| MEDIUM) + "Include urgency grouping commentary for each priority group." |
| C-10 | **PASS** | Step 1 output: `"Tier: {N} (source: TOPICS.md \| --tier \| default)"`. |
| C-11 | **PASS** | All three codes named in guard sections: ARCH-GUARD-BYPASS (Step 3 CROSS-STEP GUARD), STRATEGY-TO-PM-GUARD-BYPASS (Step 4 CROSS-STEP GUARD), GUARD-BYPASS CONTAMINATION (Step 4 entry condition). All three in the blocked-list recording sections. |
| C-12 | **PASS** | Template reordered: Contrast (SLOT 2) label before Structural position (SLOT 1); "WRITE CONTRAST SLOT FIRST"; SLOT-ORDER-INVERSION named; "DO NOT write Slot 1 (Structural position) before Slot 2 (Contrast)." |
| C-13 | **N/A** | Prose-only format (separate Steps 3-5). No evaluation table. → 0 toward numerator. |

**Aspirational: 4/5 → 8 pts**

### V-01 Score: **60 + 30 + 8 = 98**

---

## V-02 — Output Format: SKIP Table

**Axis:** output-format | **Target:** C-13

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | FORBIDDEN OUTPUTS TRIAD all 3 labels; AUTO-RULE CONTAMINATION GUARD states: "The evaluation table structurally enforces this: auto-flagged rows MUST show SKIP in all three role columns." |
| C-02 | **PASS** | All 3 labels present with completeness check. |
| C-03 | **PASS** | Step 6 with Edit tool, CANARY ASSERTION, CANARY-FALSE-POSITIVE named. |
| C-04 | **PASS** | Step 5 writes review artifact; Coverage Review table; priority-ordered next-steps; risk statement with urgency + grouping commentary. |
| C-05 | **PASS** | Reason codes exact; Slot 1 and Slot 2 both present and structurally separate (Slot 1 before Slot 2 in template — no ordering mandate, but both slots present). |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Entity-naming grammar for all sub-questions (SQ-A1/A2/A3, SQ-S1/S2/S3, SQ-P1/P2/P3). |
| C-07 | **PASS** | Two-list partition; Arch-blocked list (must be stated even if empty); Strategy-blocked list; ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS named. |
| C-08 | **PASS** | Full evaluation-driven REAL-REQUIRED template; VERDICT-ECHO named; "artifact as subject" form required. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Risk statement with specific decision, urgency label, grouping commentary. |
| C-10 | **PASS** | Tier sourcing in Step 1. |
| C-11 | **PARTIAL** | ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS named in 3a and 3b guard sections. **GUARD-BYPASS CONTAMINATION not named** — 3b entry condition says "(non-auto, non-Arch-blocked namespaces only)" but does not name the error code for violation. 2 of 3 codes named. |
| C-12 | **FAIL** | MOCK-ACCEPTED template has Slot 1 (Structural position) before Slot 2 (Contrast). No "WRITE CONTRAST SLOT FIRST" imperative. SLOT-ORDER-INVERSION not named. Classic SLOT-ORDER-INVERSION risk unremediated. |
| C-13 | **PASS** | Evaluation table with SKIP in all three columns for auto-flagged rows; "Partial SKIP (any single column SKIP while others blank or filled) = AUTO-RULE CONTAMINATION" explicitly stated; column rules reference AUTO-RULE CONTAMINATION; end-of-step verification required. |

**Aspirational: 3.5/5 → 7 pts**

### V-02 Score: **60 + 30 + 7 = 97**

---

## V-03 — Lifecycle Emphasis: Bypass Error Code Fields

**Axis:** lifecycle-emphasis | **Target:** C-11

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | FORBIDDEN OUTPUTS TRIAD all 3 labels; AUTO-RULE CONTAMINATION GUARD present. |
| C-02 | **PASS** | All 3 labels present. |
| C-03 | **PASS** | Step 8 with Edit tool, CANARY ASSERTION. |
| C-04 | **PASS** | Step 7 writes review artifact with table, ordering rule, risk statement. |
| C-05 | **PASS** | Reason codes exact; Slot 1 and Slot 2 both present (Slot 1 before Slot 2 — no ordering mandate, but both slots separate). Extra: CROSS-TEMPLATE RELATIONSHIP BLOCK table maps REAL-REQUIRED to MOCK-ACCEPTED field correspondence, reinforcing slot identity. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Entity-naming grammar; CROSS-TEMPLATE RELATIONSHIP BLOCK also clarifies artifact-as-subject grammar rule with "Row 5 grammar" annotation. |
| C-07 | **PASS** | Two-list partition; Arch-blocked and Strategy-blocked with `bypass-error-code:` fields; "not triggered" state required for empty lists. |
| C-08 | **PASS** | Full REAL-REQUIRED template; VERDICT-ECHO named; CROSS-TEMPLATE RELATIONSHIP BLOCK provides field-by-field comparison. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Risk statement with specific decision, urgency, grouping. |
| C-10 | **PASS** | Tier sourcing in Step 1. |
| C-11 | **PASS** | All three codes present as parseable output fields: `bypass-error-code: ARCH-GUARD-BYPASS` in blocked-list record format; `bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS` in Strategy-blocked record; GUARD-BYPASS CONTAMINATION fires explicitly at both Step 4 and Step 5 entry conditions. "not triggered" statement required when list empty. |
| C-12 | **FAIL** | Slot 1 (Structural position) before Slot 2 (Contrast) in MOCK-ACCEPTED template. No ordering imperative. |
| C-13 | **N/A** | Prose-only format (separate Steps 3-5). → 0 toward numerator. |

**Aspirational: 3/5 → 6 pts**

### V-03 Score: **60 + 30 + 6 = 96**

---

## V-04 — Combined: SKIP Table + Slot 2 First

**Axes:** phrasing-register + output-format | **Target:** C-12 + C-13

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | FORBIDDEN OUTPUTS TRIAD all 3 labels; AUTO-RULE CONTAMINATION GUARD with structural enforcement ("MUST show SKIP in ALL THREE role columns"). |
| C-02 | **PASS** | All 3 labels present. |
| C-03 | **PASS** | Step 6 with Edit tool, CANARY ASSERTION. |
| C-04 | **PASS** | Step 5 writes review artifact with table, ordering rule, risk statement. |
| C-05 | **PASS** | Reason codes exact; "WRITE CONTRAST SLOT FIRST — Named error: SLOT-ORDER-INVERSION if Slot 1 precedes Slot 2"; Contrast (SLOT 2) label before Structural position (SLOT 1); both slots structurally separate. |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Entity-naming grammar for all sub-questions. |
| C-07 | **PASS** | Two-list partition; Arch-blocked and Strategy-blocked lists (empty case must be stated); ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS named in guard sections. |
| C-08 | **PASS** | Full evaluation-driven REAL-REQUIRED template; VERDICT-ECHO named. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Risk statement with specific decision, urgency, grouping commentary. |
| C-10 | **PASS** | Tier sourcing in Step 1. |
| C-11 | **PARTIAL** | ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS named in 3a and 3b guard sections. **GUARD-BYPASS CONTAMINATION not named** — 3b and 3c entry conditions state the qualification constraint but do not name the violation error code. 2 of 3 codes named. Same gap as V-02. |
| C-12 | **PASS** | "*** WRITE CONTRAST SLOT FIRST — Named error: SLOT-ORDER-INVERSION if Slot 1 precedes Slot 2 ***"; Contrast (SLOT 2) label first in template; "WRITE AFTER SLOT 2" label on Slot 1. |
| C-13 | **PASS** | Table format with SKIP in all three columns for auto-flagged rows; "Any non-SKIP value in any role column for an auto-flagged row = AUTO-RULE CONTAMINATION"; end-of-step verification. AUTO-RULE CONTAMINATION referenced in column rules. |

**Aspirational: 4.5/5 → 9 pts**

### V-04 Score: **60 + 30 + 9 = 99**

---

## V-05 — Full R2 Integration: SKIP Table + Slot 2 First + Bypass Fields + Phase Scaffold

**Axes:** output-format + phrasing-register + lifecycle-emphasis | **Target:** C-11 + C-12 + C-13

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | FORBIDDEN OUTPUTS TRIAD all 3 labels; "Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate." AUTO-RULE CONTAMINATION GUARD with table structural enforcement. STOP gates between every phase. |
| C-02 | **PASS** | All 3 labels present with completeness check. |
| C-03 | **PASS** | Phase 6 with Edit tool, CANARY ASSERTION; **"This is the defining action of /mock:accept. It cannot be skipped."** — strongest non-skippability language of all R2 variations. CANARY-FALSE-POSITIVE named. CANARY SUPPRESSED branch defined. Confirmation block with decision-source cross-reference. |
| C-04 | **PASS** | Phase 5 writes review artifact; Coverage Review table; priority-ordered next-steps (P1/P2/P3); risk statement with urgency label + grouping commentary. STOP gate before Phase 6. |
| C-05 | **PASS** | "*** SLOT ORDER RULE: WRITE SLOT 2 (CONTRAST) BEFORE SLOT 1 (STRUCTURAL POSITION) ***"; Contrast (SLOT 2) first in template; SLOT-ORDER-INVERSION named; "Merged with Slot 1 into single block = RATIONALE-INCOMPLETE." |

**Essential: 5/5 → 60 pts**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Entity-naming grammar required; "Yes/no answers do not satisfy." All three sub-question sets (A/S/P) require named artifacts, components, or decisions. |
| C-07 | **PASS** | Two-list partition; Arch gate output with `bypass-error-code:` field; Strategy gate output with `bypass-error-code:` field; proceeding lists explicit; GUARD-BYPASS CONTAMINATION fires condition stated at both gates; STOP gate between phases. |
| C-08 | **PASS** | Full evaluation-driven REAL-REQUIRED template; VERDICT-ECHO = role as subject; Artifact state matches next-steps. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Risk statement with specific Tier N decision at risk; urgency label (BLOCKING \| HIGH \| MEDIUM); urgency grouping commentary for multi-namespace outputs. |
| C-10 | **PASS** | Phase 1 output: `"Tier: {N} (source: TOPICS.md \| --tier flag \| default)"`. |
| C-11 | **PASS** | All three codes as parseable output fields: `bypass-error-code: ARCH-GUARD-BYPASS`; `bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS`; GUARD-BYPASS CONTAMINATION fires stated explicitly at both gate sections. "not triggered" state required for empty blocked lists: `"Arch-blocked: none — bypass-error-code: ARCH-GUARD-BYPASS not triggered"`. Full strong pass — codes appear as output properties, not just instruction prose. |
| C-12 | **PASS** | "*** SLOT ORDER RULE: WRITE SLOT 2 (CONTRAST) BEFORE SLOT 1 (STRUCTURAL POSITION) ***"; SLOT-ORDER-INVERSION named; Contrast (SLOT 2) before Structural position (SLOT 1) in Phase 4 template. |
| C-13 | **PASS** | Phase 3 table with SKIP in all three columns; "Any non-SKIP value in any role column for an auto-flagged row = AUTO-RULE CONTAMINATION"; column rule headers reference AUTO-RULE CONTAMINATION; end-of-phase STOP gate with SKIP verification. |

**Aspirational: 5/5 → 10 pts**

### V-05 Score: **60 + 30 + 10 = 100**

---

## Rankings

| Rank | V | Essential (60) | Recommended (30) | Aspirational (10) | Total | All Essential |
|------|---|--------------|-----------------|-----------------|-------|---------------|
| 1 | **V-05** | 60 | 30 | 10 | **100** | Yes |
| 2 | **V-04** | 60 | 30 | 9 | **99** | Yes |
| 3 | **V-01** | 60 | 30 | 8 | **98** | Yes |
| 4 | **V-02** | 60 | 30 | 7 | **97** | Yes |
| 5 | **V-03** | 60 | 30 | 6 | **96** | Yes |

All five variations pass all essential criteria. All are Golden-eligible (≥80 composite). The spread is entirely in the aspirational tier.

---

## Differential Analysis

**V-05 vs V-04 (+1 pt):** Sole differentiator is C-11. V-04 names ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS but omits GUARD-BYPASS CONTAMINATION from the recording sections. V-05 names all three codes at both gate sections, uses `bypass-error-code:` as a parseable output field, and requires the "not triggered" state for empty lists.

**V-04 vs V-01 (+1 pt):** V-04 passes C-13 (table with SKIP cells); V-01 is prose-only → C-13 = N/A (0 toward numerator). Both pass C-12 and C-11. The SKIP table is the advantage.

**V-01 vs V-02 (+1 pt):** V-01 passes C-12 (Slot 2 before Slot 1) and C-11 fully; V-02 fails C-12 and gets PARTIAL on C-11 (missing GUARD-BYPASS CONTAMINATION). V-02's C-13 pass (+1) cannot recover these two gaps.

**V-02 vs V-03 (+1 pt):** V-02 passes C-13 (table format); V-03 is prose-only (C-13 N/A). V-03 passes C-11 more strongly (bypass fields) but V-02's table advantage edges it out. V-03's strongest contribution — the `bypass-error-code:` output field format — only reaches its full value in V-05 where GUARD-BYPASS CONTAMINATION is also named.

---

## Excellence Signals from V-05

**Signal 1 — "not triggered" state as required output:**
The empty blocked-list case emits `"bypass-error-code: ARCH-GUARD-BYPASS not triggered"` rather than silently omitting the section. This makes C-11 checkable in both triggered and untriggered states — a zero-cost extension that closes an omission path the "has namespaces" case alone cannot close.

**Signal 2 — bypass-error-code field elevates guard code from instruction to output property:**
The baseline and V-01 name ARCH-GUARD-BYPASS in prose; V-05 makes it a mandatory field in the blocked-list record format. This means the error code must appear in the model's output, not just in the prompt — the check shifts from instruction-compliance to output-inspection. The same structural move that V-02 applies to SKIP cells (making contamination visible by inspection) is now applied to guard error codes.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["bypass-error-code as a mandatory output field in blocked-list records makes guard errors inspectable without reading prose; empty-list 'not triggered' state closes the zero-blocked omission path", "all three R2 aspirational criteria target non-overlapping output regions (table SKIP cells, MOCK-ACCEPTED slot template, blocked-list record fields) and stack additively with no mutual interference at full combined length"]}
```
