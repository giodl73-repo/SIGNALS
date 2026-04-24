## flow-throttle — Round 19 Scoring

### Confirmed Baseline

All five variations carry the full R18 inheritance: C-01 through C-48 pass in every variant (290 pts, 58 × 5). The only open question is whether each variant closes C-49, C-50, C-51, and C-52 simultaneously.

---

### C-49 — Audit Gate-Compliance Field as Typed-Row Table

Requires Field 5 elevated to `| Item | Criterion | Evidence required | Status |` (or equivalent) — not prose or flat verdict.

| Variant | Evidence | Result |
|---------|----------|--------|
| V-01 | Field 5 is an 8-row typed table with exactly those four columns. Each audit target is an independently-scannable row. | **PASS** |
| V-02 | Field 5 has `| Item | Criterion | Evidence required | Status |` — rows mirror the five-role chain sequence (GATE-A and GATE-B as distinct rows). | **PASS** |
| V-03 | Field 5 `| Item | Criterion | Evidence required | Status |` — rows named as lifecycle phase gate artifacts in execution order. | **PASS** |
| V-04 | Field 5 has `| Item | Criterion | SHALL cite | Status |` — renamed third column but still a typed-row table; shall-contract vocabulary does not reduce it to prose. | **PASS** |
| V-05 | Field 5 is a 9-row typed table — adds a C-44+C-47+C-48 inertia-bypass confirmation row beyond the 8 V-01 rows. Audit table with exactly those four columns. | **PASS** |

---

### C-50 — Count Verification Atomized into Sub-Steps with Multi-Field VERIFICATION STATUS RECORD

Requires G-1 through G-4 (or equivalent), each with its own SHALL instruction, plus a separate fill field per component in the concluding status record.

| Variant | Evidence | Result |
|---------|----------|--------|
| V-01 | G-1 through G-4 each with own SHALL instruction. VERIFICATION STATUS RECORD: `[ SIG-01 confirmed: Y / N ]` / `[ Annot-ID count confirmed (7 of 7): Y / N ]` / `[ Role 2 activation cleared: Y / N ]` — 3 fill fields. | **PASS** |
| V-02 | GATE-B carries G-1 through G-4 each with own SHALL instruction. VERIFICATION STATUS RECORD has the same 3 fill fields. Sub-role boundary makes atomization a role-contract property. | **PASS** |
| V-03 | P0-A through P0-D (lifecycle renaming of G-1 through G-4), each with own SHALL instruction. PHASE 0 STATUS RECORD: same 3 fill fields (SIG-01 confirmed / Annot-ID count confirmed / Phase 1 entry cleared). | **PASS** |
| V-04 | V-1 through V-4, each with SHALL instruction AND SHALL NOT PROCEED IF condition — double obligation per step. MANDATORY STATUS DECLARATION has 3 SHALL FILL fields. | **PASS** |
| V-05 | G-1 through G-4, each with SHALL instruction AND "Cannot skip because" structural consequence clause. VERIFICATION STATUS RECORD: same 3 fill fields. | **PASS** |

---

### C-51 — Bypass-Condition Column in Role Activation Chain Table at Header

Requires bypass conditions header-scannable alongside activation and handoff signals.

| Variant | Evidence | Result |
|---------|----------|--------|
| V-01 | Header table: `| Role \| Activation condition \| Handoff signal \| Responsibility \| SHALL NOT activate if |` — 5-column with bypass column. Instruction explicitly notes the column "makes each role's bypass condition header-scannable." | **PASS** |
| V-02 | Same 5-column header extended with GATE-A and GATE-B as distinct rows, each with their own bypass conditions. | **PASS** |
| V-03 | Lifecycle stage overview: `| Phase \| Entry condition \| Exit signal \| Responsibility \| GATE CONDITION — blocked if |` — equivalent bypass column adapted to lifecycle framing. Header states the column "makes each phase's bypass condition header-scannable alongside its entry condition and exit signal." | **PASS** |
| V-04 | SHALL-ACTIVATION CONTRACT: `| Role \| SHALL activate when \| SHALL emit \| SHALL be responsible for \| SHALL NOT ACTIVATE WHEN |` — bypass column in all-caps, linguistically co-equal with activation and handoff. | **PASS** |
| V-05 | Same 5-column header as V-01. Introductory sentence: "makes each role's bypass condition simultaneously scannable alongside its activation condition and handoff signal before any role body begins." | **PASS** |

---

### C-52 — Non-Conflation Statement Quotes "Does NOT confirm" Cell Value Verbatim with Falsifiability Instruction

Requires the exact cell text quoted (not a column name reference) plus a string-match falsifiability instruction.

| Variant | Evidence | Result |
|---------|----------|--------|
| V-01 | Quotes: **"That Section C annotation count = declared count of 7"** — labeled "authoritative statement." Falsifiability: "a reader can verify it by locating the SIG-01 row's 'Does NOT confirm' cell and confirming the quoted text matches exactly. No prose interpretation is required; string equality is the verification method." | **PASS** |
| V-02 | Same verbatim quote, explicitly labeled "a quoted-artifact citation: this text is the exact cell value." Verification: "locate the SIG-01 row's 'Does NOT confirm' cell and confirm the quoted text matches character-for-character." Epistemic status of the quote is explicitly named. | **PASS** |
| V-03 | Verbatim quote in Phase 0.1 entry statement: **"That Section C annotation count = declared count of 7"** with "no interpretation required; string equality is the verification method." Quote co-located at the micro-checkpoint where the signal is consumed. | **PASS** |
| V-04 | Column renamed to "SHALL NOT confirm" but same cell value quoted in a dedicated blockquote: > **"That Section C annotation count = declared count of 7"** — labeled "the SHALL-authoritative cell value." String-match verification instruction present. | **PASS** |
| V-05 | Same verbatim quote. Falsifiability: "a reader can confirm it by locating the SIG-01 row's 'Does NOT confirm' cell and verifying the quoted text above matches exactly character-by-character. No prose interpretation is required; string equality is the verification method." Most precise falsifiability instruction (character-by-character). | **PASS** |

---

### Composite Scores

| Variant | C-01–C-48 | C-49 | C-50 | C-51 | C-52 | **Total** |
|---------|-----------|------|------|------|------|-----------|
| V-01 | 290 | 5 | 5 | 5 | 5 | **310/310** |
| V-02 | 290 | 5 | 5 | 5 | 5 | **310/310** |
| V-03 | 290 | 5 | 5 | 5 | 5 | **310/310** |
| V-04 | 290 | 5 | 5 | 5 | 5 | **310/310** |
| V-05 | 290 | 5 | 5 | 5 | 5 | **310/310** |

All five variations achieve ceiling. No partial credits required — each criterion was cleanly satisfied in each variant.

---

### Ranking

All tie at 310/310. Structural quality differentiation (not score-bearing under v19):

1. **V-05** — densest form. Three axes combined. "Cannot skip because" clauses provide causal argument per atomized step. 9th audit row names inertia-bypass detection as an auditable artifact. "Character-by-character" is the sharpest falsifiability formulation.
2. **V-04** — strongest obligation language. SHALL NOT ACTIVATE WHEN (caps) and the blockquote labeled "SHALL-authoritative cell value" create the most contracted citation form.
3. **V-02** — cleanest role architecture. Sub-role boundary elevation makes atomization a role-contract property rather than a within-role step list.
4. **V-03** — lifecycle framing is the most natural for multi-phase reasoning; "GATE CONDITION — blocked if" is semantically cleaner for phase-based prompts than "SHALL NOT activate if."
5. **V-01** — baseline output-format axis. All four criteria expressed as typed tables but no compounding structural choices.

---

### Excellence Signals (V-05 + V-04)

**"Cannot skip because" structural consequence clause per atomized sub-step (V-05).** Prior rounds had SHALL instructions per step. V-05 adds a named consequence: "Cannot skip because: [specific structural failure if skipped]." This converts prohibition from injunction to causal argument — a reader understands not just that skipping is forbidden but why the sequence cannot be collapsed.

**9th audit row combining multi-criterion evidence for inertia-bypass detection (V-05).** C-44, C-47, and C-48 are verified together as a single auditable row: "bypass-attempt rejection register row present AND G-1 fill field filled — cite both artifacts." This elevates multi-criterion joint evidence from a narrative check to a named, independently-auditable row in the audit table.

**"SHALL-authoritative cell value" label in blockquote format (V-04).** The verbatim quote is presented as a contracted artifact (blockquoted, labeled) rather than inline evidence. This converts the citation from "here is what the column says" to "here is the artifact you are contracted to reproduce," which is a higher obligation form.

---

```json
{"top_score": 310, "all_essential_pass": true, "new_patterns": ["Cannot skip because clause names structural consequence per atomized sub-step, converting prohibition into causal argument", "9th combined-criterion audit row makes inertia-bypass detection a named independently-auditable artifact (C-44+C-47+C-48)", "SHALL-authoritative cell value label in blockquote format contracts the verbatim citation as an obligation artifact rather than reference evidence"]}
```
