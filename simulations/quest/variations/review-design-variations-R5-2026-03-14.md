Written to `simulations/quest/variations/review-design-variations-R5-2026-03-14.md`.

---

## Round 5 Variations — review-design

| Var | Axis | New Bet | Hypothesis |
|-----|------|---------|------------|
| **V-01** | role-sequence | Domain experts lead BLOCK 1.5 + BLOCK 2 | Domain-first sequencing primes stock reviewer attention — tests if ordering changes consensus density without affecting v5 score |
| **V-02** | lifecycle-emphasis | F-11 on SPLIT synthesis (C-09 → halt) | C-09 currently has no enforcement F-ID. F-11 converts post-hoc detection into an inline halt. Potential C-18 candidate if synthesis quality improves measurably |
| **V-03** | output-format | BLOCK 5 as 4-column amend table | Same structural-column argument as C-10: a blank `Re-run Scope` cell is visible; a missing line inside a code block is not. Potential C-18 candidate |
| **V-04** | combined (lifecycle + output-format) | F-11 + F-12 + BLOCK 5 table | F-12 is the amend-count equivalent of F-09: locks P1 count at BLOCK 2.5, verifies BLOCK 5 covers every P1. Tests whether F-11+F-12 are additive or overlapping |
| **V-05** | combined (role-seq + lifecycle + output-format) | Full R5 stack: domain-first + F-10 + F-11 + F-12 + table | Maximum proactive + structural + identity + synthesis + completeness form — basis for v6 rubric extraction |

**Design bets:**
- V-01 vs V-02–V-05: Is role sequence rubric-neutral or does domain-first ordering lift C-04/C-05 qualitatively?
- V-02/V-03 isolation: F-11 (synthesis quality) and F-12+table (amend completeness) are independent enforcement layers — each targets a distinct gap from C-09/C-06
- V-04 vs V-02+V-03: Confirms F-11 and F-12 are additive, not redundant
- V-05 confirms the full stack produces 100 on v5 and is the form from which C-18/C-19 candidates (F-11, F-12) are nominated
ndidate.

**V-04 vs V-02+V-03** (count parity gate): F-12 closes the amend-count gap the same way F-09 closed the roster-count gap. Does combining F-11+F-12 produce additive lift, or do they overlap?

**V-05 vs V-04** (domain-first + full stack): Does domain-first ordering combine with enforcement breadth to produce qualitatively stronger output, or are the effects independent?

---

## V-01 | Role Sequence — Domain Experts Lead BLOCK 1.5 and BLOCK 2
**Axis**: role-sequence
**Hypothesis**: Domain expert reviewers are sequenced first in BLOCK 1.5 (Domain rows appear before Stock rows) and run first in BLOCK 2. Domain experts' thematic focus (security, data, accessibility specialization) is applied to the design before stock disciplines generalize from it. The bet: domain-first ordering increases consensus density by giving stock reviewers an existing context frame to amplify rather than discover independently. C-16 (Source column) and C-17 (F-10 orphan detection) are included at baseline. Expected: score = 100. Role sequence is not a rubric criterion — the test is whether a scoring uplift appears on C-04 (consensus block) or C-05 (unique catches) at qualitative review time.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — BLOCK 5 Re-run scoped to "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in the BLOCK 1 domain expert table
```

Halt and restructure immediately if any of F-01 through F-10 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Scan the full design for content signals before filling the domain expert table. For each signal, add one row. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude the "No signals detected" row if present). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. **Domain experts are listed first, then stock disciplines.** Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert signal table — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Add one Domain row per domain expert from BLOCK 1, placed above the Stock rows. Use the exact Expert added value as the Reviewer name.

Gate — run both checks before BLOCK 2:
1. Count Domain rows in this table. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only)*

Run every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers run first. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

Gate: Every reviewer in BLOCK 1.5 must have a finding table in this block. A missing reviewer fires F-01. Do not begin BLOCK 2.5 until all finding tables are present.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.
F-04 fires on omission regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run must name specific section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

One entry per P1 finding. An amend scoped to "full review" fires F-05 — halt and re-scope.
If zero P1 findings: `No P1 findings — no amend actions required.`

---

## V-02 | Lifecycle Emphasis — F-11 Split Synthesis Halt (C-09 Enforcement)
**Axis**: lifecycle-emphasis
**Hypothesis**: A new halt condition F-11 fires when any SPLIT row in BLOCK 3 has an empty or absent synthesis note. C-09 currently requires synthesis for split opinions but carries no enforcement F-ID — the criterion is verified post-hoc at scoring time, not blocked during generation. F-11 converts C-09's presence-check into an inline halt: the output cannot proceed past BLOCK 3 with an incomplete split row. C-16 (Source column) and C-17 (F-10) are included at baseline. Expected: score = 100 on v5 rubric. The bet is qualitative: F-11 produces tighter synthesis notes (more specific trade-off framing, not boilerplate) than the prose reminder alone. If confirmed, F-11 is a C-18 candidate for v6.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — BLOCK 5 Re-run scoped to "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in the BLOCK 1 domain expert table
F-11  Split without synthesis     — BLOCK 3 contains a SPLIT row whose Synthesis field is empty or absent
```

Halt and restructure immediately if any of F-01 through F-11 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Scan the full design for content signals before filling the domain expert table. Add 1 to 5 rows. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude "No signals detected" row). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |
| [Expert added value from BLOCK 1] | Domain expert | Domain |

Add one Domain row per domain expert from BLOCK 1. Use the exact Expert added value as the Reviewer name.

Gate — run both checks before BLOCK 2:
1. Count Domain rows. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only)*

Run every reviewer listed in BLOCK 1.5, in listed order. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

Gate: Every reviewer in BLOCK 1.5 must have a finding table. A missing reviewer fires F-01.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04; F-11: SPLIT rows require synthesis)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent. explaining the underlying design tension] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.

Split synthesis requirement: every SPLIT row must have a Synthesis note that names the underlying design tension — not just a restatement of the opposing positions. An empty or absent synthesis field fires F-11. Halt and complete the synthesis before continuing.

F-04 fires on omission of this block. F-11 fires on any SPLIT row with an empty Synthesis field.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run must name specific section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

One entry per P1 finding. An amend scoped to "full review" fires F-05 — halt and re-scope.
If zero P1 findings: `No P1 findings — no amend actions required.`

---

## V-03 | Output Format — BLOCK 5 as Structured Amend Table
**Axis**: output-format
**Hypothesis**: The amend pathway (BLOCK 5) is presented as a 4-column table with dedicated columns `P1 Finding | Section | Action | Re-run Scope` instead of a fenced code-block key-value format. The structural argument mirrors C-10: a blank `Re-run Scope` cell in a table is immediately visible; a missing Re-run line inside a code block is hideable. F-05 fires on a `Re-run Scope` cell containing "full review" — same trigger, new structural form. C-16 (Source column) and C-17 (F-10) are included at baseline. Expected: score = 100 on v5 rubric. The bet is structural: table-form BLOCK 5 makes amend completeness and scope enforcement more detectable than code-block form.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in the BLOCK 1 domain expert table
```

Halt and restructure immediately if any of F-01 through F-10 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Scan the full design for content signals before filling the domain expert table. Add 1 to 5 rows. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude "No signals detected" row). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |
| [Expert added value from BLOCK 1] | Domain expert | Domain |

Add one Domain row per domain expert from BLOCK 1. Use the exact Expert added value as the Reviewer name.

Gate:
1. Count Domain rows. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only)*

Run every reviewer listed in BLOCK 1.5, in listed order. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

Gate: Every reviewer in BLOCK 1.5 must have a finding table. A missing reviewer fires F-01.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.
F-04 fires on omission regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope "full review" fires F-05; table form required)*

One row per P1 finding. Re-run Scope must name the specific section or component — never "full review."

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column contracts:
- `P1 Finding`: paste or summarize the P1 finding text.
- `Section`: the specific section or component where the change is made.
- `Action`: one sentence — what change resolves the finding.
- `Re-run Scope`: reviewer(s) name(s) + section scope only. "Full review" fires F-05 — halt and re-scope.

If zero P1 findings: row `| — | — | — | No P1 findings — no amend actions required. |`

---

## V-04 | Combined (Lifecycle + Output-Format) — F-11 Split Synthesis + F-12 Amend Count Parity + BLOCK 5 Table
**Axis**: combined (lifecycle-emphasis + output-format)
**Hypothesis**: Combines three enforcement extensions: (1) F-11 converts C-09 split synthesis into a halt condition (from V-02), (2) BLOCK 5 table form for structural column enforcement of amend entries (from V-03), and (3) F-12 — a new count parity gate that fires when BLOCK 5 entry count is less than P1 count from BLOCK 2.5. F-12 is the amend-completeness equivalent of F-09 (roster count parity): P1 count locks at BLOCK 2.5, BLOCK 5 must account for every P1. C-16 (Source column) and C-17 (F-10) are included at baseline. Expected: score = 100 on v5 rubric. The bet: F-11+F-12 are additive, not overlapping — F-11 enforces synthesis quality within BLOCK 3; F-12 enforces coverage completeness across BLOCK 2.5 and BLOCK 5.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in the BLOCK 1 domain expert table
F-11  Split without synthesis     — BLOCK 3 contains a SPLIT row whose Synthesis field is empty or absent
F-12  Amend count mismatch        — BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
```

Halt and restructure immediately if any of F-01 through F-12 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Scan the full design for content signals before filling the domain expert table. Add 1 to 5 rows. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude "No signals detected" row). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |
| [Expert added value from BLOCK 1] | Domain expert | Domain |

Add one Domain row per domain expert from BLOCK 1. Use the exact Expert added value as the Reviewer name.

Gate:
1. Count Domain rows. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only)*

Run every reviewer listed in BLOCK 1.5, in listed order. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

Gate: Every reviewer in BLOCK 1.5 must have a finding table. A missing reviewer fires F-01.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

Record `P1 count = [n from P1 row]`. This count is used in the BLOCK 5 gate (F-12).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04; F-11: SPLIT rows require synthesis)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent. naming the underlying design tension] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.

Split synthesis requirement: every SPLIT row Synthesis field must name the underlying design tension — not merely restate the opposing positions. An empty or absent synthesis field fires F-11. Halt and write the synthesis before continuing.

F-04 fires on omission. F-11 fires on any SPLIT row with an empty Synthesis field.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope "full review" fires F-05; F-12: entry count must equal P1 count from BLOCK 2.5; table form required)*

One row per P1 finding. Re-run Scope must name the specific section or component only.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column contracts:
- `Re-run Scope`: reviewer(s) + section scope only. "Full review" fires F-05 — halt and re-scope.

Gate before closing: count amend rows in this table (exclude the "no P1 findings" row if present). Must equal `P1 count` from BLOCK 2.5. F-12 fires if BLOCK 5 entry count < P1 count — halt and add the missing entries.

If zero P1 findings: row `| — | — | — | No P1 findings — no amend actions required. |`

---

## V-05 | Combined Maximum — Domain-First + F-10 + F-11 + F-12 + BLOCK 5 Table
**Axis**: combined (role-sequence + lifecycle-emphasis + output-format)
**Hypothesis**: Full R5 enforcement stack. Domain experts lead BLOCK 1.5 and BLOCK 2 (role-sequence axis from V-01). Source column in BLOCK 1.5 (C-16). F-10 orphan detection (C-17). F-11 split synthesis halt (from V-02). F-12 amend count parity gate (from V-04). BLOCK 5 as 4-column table (from V-03). Each enforcement layer addresses a distinct error class: F-10 catches identity substitution; F-11 catches synthesis omission; F-12 catches amend undercount. Domain-first ordering maximizes early-stage context framing. This is the maximum structural + proactive + identity + synthesis + completeness form for R5 and the intended basis for rubric v6 criterion extraction. Expected: score = 100 on v5 rubric.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in the BLOCK 1 domain expert table
F-11  Split without synthesis     — BLOCK 3 contains a SPLIT row whose Synthesis field is empty or absent
F-12  Amend count mismatch        — BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
```

Halt and restructure immediately if any of F-01 through F-12 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Scan the full design for content signals before filling the domain expert table. Add 1 to 5 rows. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude "No signals detected" row). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. **Domain experts are listed first, then stock disciplines.** Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Add one Domain row per domain expert from BLOCK 1, placed above the Stock rows. Use the exact Expert added value as the Reviewer name.

Gate — run both checks before BLOCK 2:
1. Count Domain rows. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only; domain experts run first)*

Run every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers run first. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

Gate: Every reviewer in BLOCK 1.5 must have a finding table. A missing reviewer fires F-01.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

Record `P1 count = [n from P1 row]`. This count is used in the BLOCK 5 gate (F-12).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04; F-11: SPLIT rows require synthesis)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent. naming the underlying design tension] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.

Split synthesis requirement: every SPLIT row Synthesis field must name the underlying design tension — not merely restate the opposing positions. An empty or absent synthesis field fires F-11. Halt and write the synthesis before continuing.

F-04 fires on omission. F-11 fires on any SPLIT row with an empty Synthesis field.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope "full review" fires F-05; F-12: entry count must equal P1 count from BLOCK 2.5; table form required)*

One row per P1 finding. Re-run Scope must name the specific section or component only. Domain-first ordering in BLOCK 2 means domain expert reviewers are re-run candidates when their thematic area overlaps with the P1 section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column contracts:
- `Re-run Scope`: reviewer(s) + section scope only. "Full review" fires F-05 — halt and re-scope.

Gate before closing: count amend rows in this table (exclude the "no P1 findings" row if present). Must equal `P1 count` from BLOCK 2.5. F-12 fires if BLOCK 5 entry count < P1 count — halt and add the missing entries.

If zero P1 findings: row `| — | — | — | No P1 findings — no amend actions required. |`
