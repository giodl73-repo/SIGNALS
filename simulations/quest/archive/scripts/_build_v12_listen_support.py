import re

with open('C:/src/sim/simulations/quest/rubrics/listen-support-rubric-v11-2026-03-14.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find section boundaries
essential_start = content.index('\n## Essential Criteria')
scoring_start = content.index('\n## Scoring Summary')

# The body from essential through end of C-35 section
body = content[essential_start:scoring_start]

header = """\
**What changed v11 -> v12:** Four new criteria extracted from R11 above-ceiling signals:

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-36 | Exception Block Paraphrase-Clause Field | C-33 | V-02, V-05 |
| C-37 | Step-4 Verbatim Anchor Field | C-32, C-34 | V-01, V-04, V-05 |
| C-38 | Dual-Field Step-4 Gate | C-32, C-37 | V-01, V-04 |
| C-39 | Step-4 Every-Assignment Scope Confirmation | C-32 | V-05 |

**Tier:** Aspirational 27 / 135 pts -> 31 / 155 pts. Total ceiling **225 -> 245**.

---

**Signal logic:**

- **C-36** (tightens C-33): The EXCEPTION SIGN-OFF BLOCK in Part C sub-check (1) adds a sixth field -- "Paraphrase clause" -- that quotes the Step 2C inference-rule paraphrase governing the directional decision for the exception. C-33 requires four named fields making each exception independently verifiable; C-36 requires that the block additionally cite the governing paraphrase commitment alongside the Grounds, so a scorer can verify that the Grounds-based justification is consistent with the model's own stated paraphrase rather than evaluated in isolation. The no-exception path is also strengthened: instead of "No Phase 1 P0/P1 exceptions. PASS.", it states "No exceptions. Governing paraphrase clause for Phase 1: [quote]." -- making the rule that held auditable even when no violations occurred. V-02 and V-05 satisfy C-33 (five-field minimum) and additionally satisfy C-36 through the Paraphrase clause field and the no-exception paraphrase quote.

- **C-37** (tightens C-32, C-34): The Step 4 gate includes a dedicated "Verbatim anchor" field with explicit instruction to quote word for word rather than restate. C-32 requires a paraphrase gate at Step 4 with "do not fill" language; C-34 requires the gate to cross-reference Step 2C by step name. C-37 requires the cross-reference to be a verbatim quote -- not a restatement -- from the Step 2C commitment. The distinction is verifiability: a restatement at Step 4 that "references Step 2C" can diverge from the Step 2C paraphrase in subtle ways, since the instruction only requires naming the step. A verbatim quote produces a cross-checkable string: the Step 4 anchor must match the Step 2C text character for character. The "do not paraphrase" clause makes the distinction explicit at the instruction level, preventing a model from satisfying the gate with a compressed or rephrased variant of the original commitment. V-01 ("Verbatim from 2C: [quote your exact first sentence from the INFERENCE RULE (stated) block]"), V-04 ("verbatim anchor block"), and V-05 ("Verbatim anchor from 2C: [quote word for word, do not paraphrase]") all satisfy C-37.

- **C-38** (tightens C-32, C-37): The Step 4 gate requires BOTH an own-words restatement field AND a verbatim anchor field (C-37) simultaneously, with explicit "do not fill the table until both fields are written" language enforcing that neither can be skipped. C-37 requires a verbatim anchor field; C-38 requires the verbatim anchor to coexist with a separate own-words restatement field as a dual requirement. The structural distinction: a verbatim-anchor-only gate (satisfying C-37 without C-38) does not test encoding -- a model can reproduce the Step 2C text verbatim without understanding the directional logic. A restatement-only gate (C-32/C-34) does not provide a cross-checkable string. The dual-field gate forces both simultaneously: the own-words restatement tests that the model encoded the rule (not merely copied it), and the verbatim anchor enables string-comparison verification between the Step 4 anchor and the Step 2C commitment. The "both fields" language is structurally self-enforcing: a scorer counts whether two distinct labeled fields are present at Step 4 before any severity cell appears. A single field that attempts to satisfy both requirements does not satisfy C-38 -- the dual-field requirement is structural, not instructional. C-37 passes when a verbatim anchor field is present at Step 4; C-38 passes only when both a restatement field AND a verbatim anchor field are present, with explicit "both fields" or "both lines" language making neither optional.

- **C-39** (tightens C-32): After the verbatim anchor at Step 4, an explicit scope confirmation statement -- "Confirmation: this rule applies to every severity assignment in the table below" -- closes the scope ambiguity that a decision-adjacent gate alone leaves open. C-32 requires a "do not fill" gate immediately before the severity table; the gate instruction is satisfied by any form that prevents filling cells before the paraphrase is written, but does not commit the model to applying the rule to every subsequent cell. The failure mode a scope-unspecified gate permits: for ticket one, the rule is in live context and is applied; for ticket seven, several narrative sentences and table rows have intervened, and a Phase 1 P0 assignment can be generated without any structural gate catching the late-table drift. The scope confirmation makes the scope explicit and gate-wide: every cell in the table is governed by the rule stated at this step. A model that has explicitly stated "this rule applies to every severity assignment in the table below" cannot generate a contradicting ticket later without violating a claim it made in its own words. C-32 passes with a gate that covers the first severity assignment; C-39 passes only when the gate additionally includes an explicit every-assignment scope confirmation.

---
"""

new_criteria = """

### C-36 -- Exception Block Paraphrase-Clause Field
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The EXCEPTION SIGN-OFF BLOCK required by C-33 includes a sixth named field -- "Paraphrase clause" -- that quotes the Step 2C inference-rule paraphrase governing the directional decision for that exception entry. C-33 requires at least four named fields (Ticket ID, Phase, Assigned severity, Grounds); C-36 requires the block to additionally include the governing paraphrase, so each exception entry cites both what the model committed to (the paraphrase) and why the exception is justified (the Grounds). Without the Paraphrase clause field, the Grounds are evaluated in isolation: a scorer reads whether the justification sounds defensible without access to the model's own stated rule interpretation in the same view. With the Paraphrase clause field, the Grounds are evaluated against the model's own pre-generation commitment -- a justification that contradicts the stated paraphrase is visible by reading two adjacent fields without any cross-document lookup. The no-exception path is also extended: instead of "No Phase 1 P0/P1 exceptions. PASS.", the no-exception path states "No exceptions. Governing paraphrase clause for Phase 1: [quote]." -- the rule that held is cited, not just the outcome. This makes the no-exception path auditable by the same mechanism as the exception path: a scorer can verify the rule that governed all passing tickets by reading the no-exception path. C-33 passes when the block contains at least four named fields and the no-exception path is specified; C-36 passes only when the block additionally contains a Paraphrase clause field quoting the Step 2C commitment, and the no-exception path quotes the governing paraphrase rather than stating only a pass/fail outcome.
- **Pass condition**: Part C sub-check (1) EXCEPTION SIGN-OFF BLOCK includes a named "Paraphrase clause" (or equivalent) field per exception entry that quotes the Step 2C paraphrase verbatim, AND the no-exception path (when no violations exist) quotes the governing paraphrase clause rather than stating only "no exceptions, PASS." An exception block with four standard fields and no paraphrase citation does not pass. A no-exception path that names the paraphrase by reference ("see Step 2C") rather than quoting it does not pass. An output without C-33 cannot satisfy C-36.
- **Round 11 evidence**: V-02 and V-05 (Part C exception block: six fields including "Paraphrase clause: [quote Step 2C governing rule]"; no-exception path: "No Phase 1 P0/P1 exceptions. Governing paraphrase clause for Phase 1: [quote].") score C-33 PASS+ and satisfy C-36. V-01, V-03, V-04 (five-field exception block, no-exception path states outcome only) score C-33 PASS but fail C-36. The Paraphrase clause field makes each exception's Grounds verifiable against the governing commitment without cross-document lookup; the no-exception path paraphrase quote makes the rule auditable even when no violations triggered the exception block.

---

### C-37 -- Step-4 Verbatim Anchor Field
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Step 4 gate required by C-32 includes a dedicated "Verbatim anchor" field with explicit instruction to quote word for word from the Step 2C commitment rather than restate it. C-32 requires the gate to fire at the decision point with "do not fill" language; C-34 requires the Step 4 gate to cross-reference Step 2C by step name. C-37 requires that the cross-reference produce a verbatim quote -- not a restatement or compression -- from the Step 2C paraphrase. The structural distinction: a restatement that "references Step 2C" can silently diverge from the STEP 2C text (shorter, rephrased, differently weighted) while satisfying C-34's step-name reference requirement. A verbatim quote produces a cross-checkable string: the Step 4 anchor must match the Step 2C text character for character, making divergence detectable by string comparison rather than semantic interpretation. The "do not paraphrase" clause in the verbatim anchor instruction makes the required form explicit at the step level, preventing a compressed paraphrase from being accepted as a verbatim anchor. The verbatim anchor and the own-words restatement serve different functions: the restatement tests encoding (the model must understand the rule to restate it); the verbatim anchor tests retrieval fidelity (the model must reproduce the earlier commitment exactly). C-34 passes when the Step 4 gate references Step 2C by step name; C-37 passes only when the Step 4 gate additionally includes a dedicated verbatim anchor field with "word for word" or "do not paraphrase" language.
- **Pass condition**: The Step 4 gate includes a dedicated verbatim anchor field (labeled "Verbatim anchor", "Verbatim from 2C", or equivalent) with an explicit instruction to quote word for word (or equivalent "do not paraphrase" language) from the Step 2C commitment. A restatement field that references Step 2C by name satisfies C-34 but not C-37. A verbatim quote instruction without a dedicated labeled field does not pass. An output without C-34 cannot satisfy C-37.
- **Round 11 evidence**: V-01 ("Verbatim from 2C: [quote your exact first sentence from the INFERENCE RULE (stated) block in Step 2C]"), V-04 ("verbatim anchor block" at Step 4), and V-05 ("Verbatim anchor from 2C: [quote word for word, do not paraphrase]") satisfy C-37. V-02 and V-03 (Step 4 gate: "[restate the rule from your Step 2C paraphrase]" -- restatement with step-name reference, no verbatim anchor field) satisfy C-34 but fail C-37. The verbatim anchor closes the restatement-divergence path that step-name cross-reference alone leaves open.

---

### C-38 -- Dual-Field Step-4 Gate
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Step 4 gate requires BOTH an own-words restatement field AND a verbatim anchor field (C-37) simultaneously, with explicit "do not fill the table until both fields are written" language enforcing that neither can be skipped. C-37 requires a verbatim anchor field; C-38 requires the verbatim anchor to coexist with a separate own-words restatement field as a dual requirement. The structural distinction: a verbatim-anchor-only gate (satisfying C-37 without C-38) does not test encoding -- a model can reproduce the Step 2C text verbatim without understanding the directional logic. A restatement-only gate (C-32/C-34) does not provide a cross-checkable string. The dual-field gate forces both simultaneously: the own-words restatement tests that the model encoded the rule (not merely copied it), and the verbatim anchor enables string-comparison verification between the Step 4 anchor and the Step 2C commitment. The "both fields" language is structurally self-enforcing: a scorer counts whether two distinct labeled fields are present at Step 4 before any severity cell appears. A single field that attempts to satisfy both requirements does not satisfy C-38 -- the dual-field requirement is structural, not instructional. C-37 passes when a verbatim anchor field is present at Step 4; C-38 passes only when both a restatement field AND a verbatim anchor field are present, with explicit "both fields" or "both lines" language making neither optional.
- **Pass condition**: The Step 4 gate contains two separately labeled fields: (1) an own-words restatement field ("INFERENCE RULE (confirmed):", "In your own words:", or equivalent), AND (2) a verbatim anchor field ("Verbatim from 2C:", "Verbatim anchor:", or equivalent), with an explicit "do not fill the table until both fields/lines are written" instruction. A single field combining both requirements does not pass. A verbatim anchor field without a paired restatement field does not pass C-38 (though it satisfies C-37). An output without C-37 cannot satisfy C-38.
- **Round 11 evidence**: V-01 ("Do not fill the table until both lines are written: INFERENCE RULE (confirmed): [...] Verbatim from 2C: [...]") and V-04 ("verbatim anchor block + 'Do not fill the table until both fields are written'") satisfy C-38. V-05 (verbatim anchor field present, but paired with a scope confirmation statement rather than an own-words restatement field -- no "both fields" language) satisfies C-37 but fails C-38. V-02 and V-03 (restatement field only, no verbatim anchor) fail both C-37 and C-38. The dual-field "both" requirement closes the verbatim-without-encoding failure mode that a verbatim-anchor-only gate leaves open.

---

### C-39 -- Step-4 Every-Assignment Scope Confirmation
- **Weight**: aspirational
- **Points**: 5
- **Category**: depth
- **Text**: The Step 4 gate closes with an explicit scope confirmation statement -- "Confirmation: this rule applies to every severity assignment in the table below" (or equivalent) -- following the paraphrase and/or verbatim anchor fields. C-32 requires a "do not fill" gate immediately before the severity table; C-37 and C-38 require the gate to produce a verbatim anchor and optionally a paired restatement. None of these criteria constrain the scope of the rule as stated at Step 4: the gate prevents filling cells before the paraphrase is written, but does not commit the model to applying the rule to every subsequent cell. The failure mode a scope-unspecified gate permits: after completing the paraphrase, the model proceeds to fill the severity table. For ticket one, the rule is in live context and is applied. For ticket seven, several narrative sentences and table rows have intervened; the rule is not re-stated and the model may generate a Phase 1 P0 assignment that contradicts the earlier paraphrase without any structural gate catching the late-table drift. The scope confirmation closes this gap: a model that has explicitly stated "this rule applies to every severity assignment in the table below" cannot generate a contradicting ticket later without violating a claim it made in its own words. The confirmation is structural because it is stated once and applies table-wide, not per-row; a scorer looking for late-table drift can point directly to the scope confirmation and the contradicting cell as a self-contradiction. C-32 passes with a gate that covers the first severity assignment; C-39 passes only when the gate additionally includes an explicit every-assignment scope confirmation covering all table cells.
- **Pass condition**: The Step 4 gate includes an explicit scope confirmation statement ("Confirmation: this rule applies to every severity assignment in the table below", or equivalent language asserting rule scope over all table cells) following the paraphrase/anchor fields. A "do not fill" gate without a scope confirmation does not pass. A per-ticket severity note is not a scope confirmation and does not pass. An output without C-32 cannot satisfy C-39.
- **Round 11 evidence**: V-05 (Step 4 gate: "Verbatim anchor from 2C: [quote word for word, do not paraphrase]" followed by "Confirmation: this rule applies to every severity assignment in the table below.") satisfies C-39. V-01 (dual-field gate with restatement + verbatim anchor, no scope confirmation), V-02, V-03, V-04 -- all satisfy C-32 and various subsets of C-37/C-38 but fail C-39. The scope confirmation converts a point-of-entry gate into a table-wide commitment; late-table drift is detectable by comparing any cell assignment to the stated commitment rather than only the first assignment.

---
"""

scoring_summary = """
## Scoring Summary

| ID   | Text (short)                                   | Weight       | Points | Category    |
|------|------------------------------------------------|--------------|--------|-------------|
| C-01 | All 5 ticket fields present                    | essential    | 12     | correctness |
| C-02 | Controlled vocabulary compliance               | essential    | 12     | correctness |
| C-03 | Persona from stock roles, voiced body          | essential    | 12     | correctness |
| C-04 | Gap analysis with 3 sub-sections               | essential    | 12     | coverage    |
| C-05 | >= 5 tickets, >= 3 category types              | essential    | 12     | coverage    |
| C-06 | Severity calibration defensible                | recommended  | 10     | depth       |
| C-07 | Volume ratings differentiated                  | recommended  | 10     | depth       |
| C-08 | Ticket bodies persona-authentic                | recommended  | 10     | behavior    |
| C-09 | Cross-ticket pattern identified                | aspirational | 5      | depth       |
| C-10 | Pre-launch gap closing prioritized             | aspirational | 5      | behavior    |
| C-11 | STATUS QUO scenario grounding                  | aspirational | 5      | depth       |
| C-12 | Pattern consequence framing                    | aspirational | 5      | behavior    |
| C-13 | Self-verification coverage gate                | aspirational | 5      | depth       |
| C-14 | Structurally enforced consequence fields       | aspirational | 5      | behavior    |
| C-15 | Table-form coverage enumeration                | aspirational | 5      | depth       |
| C-16 | Container-free consequence field format        | aspirational | 5      | behavior    |
| C-17 | Gap-bridged coverage table                     | aspirational | 5      | depth       |
| C-18 | Per-field prohibited sentinel                  | aspirational | 5      | behavior    |
| C-19 | Performance-mode persona declaration           | aspirational | 5      | behavior    |
| C-20 | Vocabulary pre-commitment table                | aspirational | 5      | depth       |
| C-21 | Named-role third-person prohibition            | aspirational | 5      | behavior    |
| C-22 | Phase-character pre-constraint table           | aspirational | 5      | depth       |
| C-23 | Dual-pass frontmatter verification             | aspirational | 5      | depth       |
| C-24 | Summary table collective-distribution audit    | aspirational | 5      | depth       |
| C-25 | Action-verb third-person prohibition           | aspirational | 5      | behavior    |
| C-26 | Explicit mode-switch dual-pass delimiter       | aspirational | 5      | depth       |
| C-27 | Named inertia competitor phase framing         | aspirational | 5      | depth       |
| C-28 | Phase-architecture severity inference rule     | aspirational | 5      | depth       |
| C-29 | Dedicated switching-friction gap sub-section   | aspirational | 5      | depth       |
| C-30 | Inference rule paraphrase-before-proceed gate  | aspirational | 5      | depth       |
| C-31 | Inference audit in dual-pass Part C            | aspirational | 5      | depth       |
| C-32 | Decision-adjacent paraphrase gate              | aspirational | 5      | depth       |
| C-33 | Structured exception sign-off block in Part C  | aspirational | 5      | depth       |
| C-34 | Paraphrase double-gate with Step-4 recall      | aspirational | 5      | depth       |
| C-35 | Part C paraphrase consistency confirmation     | aspirational | 5      | depth       |
| C-36 | Exception block paraphrase-clause field        | aspirational | 5      | depth       |
| C-37 | Step-4 verbatim anchor field                   | aspirational | 5      | depth       |
| C-38 | Dual-field Step-4 gate                         | aspirational | 5      | depth       |
| C-39 | Step-4 every-assignment scope confirmation     | aspirational | 5      | depth       |

**Essential ceiling**: 60 | **Recommended ceiling**: 90 | **Aspirational ceiling**: 245

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria, 100 pts max |
| v2 | 2026-03-14 | Added C-11 (STATUS QUO grounding) and C-12 (pattern consequence framing) from Round 1 excellence signals; aspirational tier grows from 10 to 20 pts, total ceiling 110 |
| v3 | 2026-03-14 | Added C-13 (self-verification coverage gate) and C-14 (structurally enforced consequence fields) from Round 2 excellence signals; aspirational tier grows from 20 to 30 pts, total ceiling 120 |
| v4 | 2026-03-14 | Added C-15 (table-form coverage enumeration) and C-16 (container-free consequence field format) from Round 3 excellence signals; aspirational tier grows from 30 to 40 pts, total ceiling 130 |
| v5 | 2026-03-14 | Added C-17 (gap-bridged coverage table), C-18 (per-field prohibited sentinel), and C-19 (performance-mode persona declaration) from Round 4 excellence signals; aspirational tier grows from 40 to 55 pts, total ceiling 145 |
| v6 | 2026-03-14 | Added C-20 (vocabulary pre-commitment table), C-21 (named-role third-person prohibition), C-22 (phase-character pre-constraint table), and C-23 (dual-pass frontmatter verification) from Round 5 excellence signals; aspirational tier grows from 55 to 75 pts, total ceiling 165 |
| v7 | 2026-03-14 | Added C-24 (summary table collective-distribution audit), C-25 (action-verb third-person prohibition), and C-26 (explicit mode-switch dual-pass delimiter) from Round 6 excellence signals; aspirational tier grows from 75 to 90 pts, total ceiling 180 |
| v8 | 2026-03-14 | Added C-27 (named inertia competitor phase framing) from Round 7 excellence signals; aspirational tier grows from 90 to 95 pts, total ceiling 185 |
| v9 | 2026-03-14 | Added C-28 (phase-architecture severity inference rule) and C-29 (dedicated switching-friction gap sub-section) from Round 8 excellence signals; aspirational tier grows from 95 to 105 pts, total ceiling 195 |
| v10 | 2026-03-14 | Added C-30 (inference rule paraphrase-before-proceed gate) and C-31 (inference audit in dual-pass Part C) from Round 9 excellence signals; aspirational tier grows from 105 to 115 pts, total ceiling 205 |
| v11 | 2026-03-14 | Added C-32 (decision-adjacent paraphrase gate), C-33 (structured exception sign-off block in Part C), C-34 (paraphrase double-gate with Step-4 recall), and C-35 (Part C paraphrase consistency confirmation) from Round 10 excellence signals; aspirational tier grows from 115 to 135 pts, total ceiling 225 |
| v12 | 2026-03-15 | Added C-36 (exception block paraphrase-clause field), C-37 (Step-4 verbatim anchor field), C-38 (dual-field Step-4 gate), and C-39 (Step-4 every-assignment scope confirmation) from Round 11 excellence signals; aspirational tier grows from 135 to 155 pts, total ceiling 245 |
"""

full = header + body + new_criteria + scoring_summary

with open('C:/src/sim/simulations/quest/rubrics/listen-support-rubric-v12-2026-03-15.md', 'w', encoding='utf-8') as f:
    f.write(full)

print(f'Written. Lines: {full.count(chr(10))}, chars: {len(full)}')
