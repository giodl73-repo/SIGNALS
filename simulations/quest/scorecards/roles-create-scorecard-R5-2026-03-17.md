# roles-create R5 — Scorecard (Rubric v4)

## Scoring Summary

| Variation | Score | Band | C-15 | C-16 | C-17 |
|-----------|-------|------|------|------|------|
| V-05 Full Three-Criteria | **100** | Golden | PASS | PASS | PASS |
| V-04 In-Phase + Pre-Declared | **99** | Golden | PASS | PASS | FAIL |
| V-01 Pre-Declared + Terminal | **98** | Golden | FAIL | PASS | FAIL |
| V-02 In-Phase + No Pre-Declaration | **98** | Golden | PASS | FAIL | FAIL |
| V-03 CONTRACT-Only + Terminal | **98** | Golden | FAIL | FAIL | PASS |

All five variations pass C-01 through C-14 (essential + recommended + base aspirational). The only axis of variation is C-15/C-16/C-17.

---

## Rubric Separation: CONFIRMED

- V-01/V-02/V-03 tie at 98, each failing a different pair of the new trio — no entanglement
- V-04 outscore V-01/V-02/V-03 by exactly 1 — C-15 and C-16 are independently additive
- V-05 is the sole 100 — C-17 adds exactly 1 point to the C-15+C-16 base

**Key distinctions confirmed:**
- C-16 (declaration) does not imply C-15 (distribution) — V-01 declares at entry but batches all checks at Phase 5
- C-15 does not imply C-16 — V-02 has per-phase gates that emerge organically with no pre-declared commitment
- C-17 is independent of both — V-03 extracts all rules into named CONTRACT blocks without pre-declaring an audit list or distributing gates

---

## Excellence Signals

1. **CONTRACT: AUDIT-CHECKLIST as traceability layer** — pre-declaring the full audit as a named table with gate-phase assignments creates bidirectional traceability. Cross-reference notation (`Gate 3b [C]`) binds each gate to its declared obligation at both ends.

2. **Thin-phase referencing** — when all rules live in CONTRACT blocks, phases become single-line references ("Apply CONTRACT: FIELD-REGISTER") instead of repeating rules. Shorter skill, same enforcement, single source of truth.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["contract-audit-checklist: pre-declaring the full audit as a named CONTRACT table with gate-phase assignments creates bidirectional traceability from declaration to execution and back", "thin-phase-referencing: when all rules live in CONTRACT blocks phases become single-line references eliminating rule repetition without losing enforcement"]}
```
e Phase 0 (pre-detection) + Phase 1 (mode routing). Phase 0 handles malformed inputs before Phase 1's three-way branch. NAME-ONLY, DESCRIPTION, INTERACTIVE each route to distinct generation paths. No variation silently cross-routes.

**C-04** — Phase 3 in all variations enforces domain-specific content through field-register rules (first-person observational frame, specific beneficiary in serves, boolean verify checks). Audit items [C][D][E] enforce this explicitly before write.

**C-05** — Phase 2 in all variations checks for `.roles/{area}/inertia-advocate.md`. When absent, a complete companion file is generated with full frontmatter and body table -- not a suggestion. All 5 satisfy this and exceed C-05's minimum by also satisfying C-11.

### Recommended

**C-06** -- Phase 3 in all variations specifies "4+ boolean checks, each naming a specific artifact, state, or config, answerable yes/no." GOOD/BAD examples given in every variation (V-03/V-05 lift these into CONTRACT: FIELD-REGISTER). Audit item [E] enforces the minimum before write.

**C-07** -- Phase 4 in all variations requires a `## {Subrole} Domain` heading plus a domain specializations table with minimum 3 rows. FAIL/PASS column header examples provided in all variations.

### Aspirational

**C-08** -- All variations instruct "check existing roles in `{area}` first; use their archetype value -- `craft` for technical/builder areas, `process` for governance/ops areas; do not apply without checking." V-03/V-05 surface this in CONTRACT: FIELD-REGISTER.

**C-09** -- All variations specify FIRST-PERSON OBSERVATIONAL for `orientation.frame` and THIRD-PERSON RECIPIENT naming a specific beneficiary for `orientation.serves`. Audit items [C]/[D] enforce register compliance in all variations.

**C-10** -- All variations include explicit FAIL/PASS column header examples. Generic headers (Entity, Item, Area, Purpose, Description, Notes) = FAIL explicitly stated in all 5. Audit item [F] enforces this before write.

**C-11** -- All variations generate a complete inertia-advocate companion file when absent. Template includes all 12 fields and a body table. Audit item [H] verifies no literal `{area}` remains.

**C-12** -- All variations include three categorical prohibitions for interactive mode: (1) no content after one or two answers, (2) no draft/stub mid-conversation, (3) proceed only when all three answers confirmed. Labeled "categorical prohibitions, not preferences" in all 5.

**C-13** -- All variations include a structured YES/NO self-audit in Phase 5 between generation and write. Phase 6 is only reachable after the audit confirms all items YES (or N/A for H).

**C-14** -- All variations include a Phase 0 Input Guard that classifies all four malformed input types before mode detection: BARE AREA (ask which subrole), EXTRA COLONS (use first two tokens and notify), VAGUE PHRASE (ask for clarification), EMPTY (route to INTERACTIVE).

**C-15: In-phase gates**
- V-01: FAIL -- The SKILL ENTRY block declares the audit, but Phases 0-4 produce content with no embedded gates. All 8 checks are batched in Phase 5. Distribution is declared but not executed.
- V-02: PASS -- Every content-producing phase ends with an explicit `Gate N:` checkpoint. Gate 0 after Phase 0, Gate 1 after Phase 1, Gates 2a/2b after Phase 2, Gates 3a-3e after Phase 3, Gates 4a-4c after Phase 4. Phase 5 is a rollup confirmation, not the sole execution site.
- V-03: FAIL -- CONTRACT blocks define all invariants, but no in-phase gates exist. The full audit checklist is written for the first time at Phase 5.
- V-04: PASS -- Same per-phase gate structure as V-02. Gate labels bracket each phase's output with their declared obligation IDs (e.g., `Gate 3a [B]`). Phase 5 confirms all previously-passed gates.
- V-05: PASS -- Same per-phase gate structure, with gates citing CONTRACT references (e.g., `Gate 3b [C]: orientation.frame passes CONTRACT: FIELD-REGISTER`). Phase 5 confirms all gates resolved against CONTRACT: AUDIT-CHECKLIST.

**C-16: Pre-declared audit obligations**
- V-01: PASS -- SKILL ENTRY block at the top of the skill (before Phase 0) declares all 8 audit items A-H as a committed list. Phase 5 executes against this pre-declared list.
- V-02: FAIL -- No SKILL ENTRY block. Gates emerge from each phase organically. The checklist is discovered during execution, not committed upfront. A reader cannot determine from skill entry what the full audit scope is.
- V-03: FAIL -- No pre-declaration. CONTRACT blocks define invariants, but the Phase 5 checklist is written for the first time at Phase 5. No upfront commitment to which items will be checked.
- V-04: PASS -- SKILL ENTRY block pre-declares all 8 items with their gate phase assignments (e.g., "[B] Frontmatter contains all 12 required fields -- verified at Phase 3 Gate 3a"). Maps every obligation to its execution site before Phase 0 begins.
- V-05: PASS -- CONTRACT: AUDIT-CHECKLIST is a named contract that pre-declares all 8 items with gate phase assignments in table form before Phase 1. Phase 5 references this contract by name.

**C-17: Named CONTRACT sections**
- V-01: FAIL -- All constraints (field register rules, column header rules, interactive hold rules, input routing rules) expressed as inline prose within phase steps. No named CONTRACT blocks.
- V-02: FAIL -- Same as V-01. Per-phase gates reference local rules embedded inline. No named CONTRACT blocks.
- V-03: PASS -- Five named CONTRACT blocks defined before the PHASES section: CONTRACT: INPUT-ROUTING-RULES (table), CONTRACT: INTERACTIVE-HOLD (categorical prohibitions), CONTRACT: FIELD-REGISTER (field register table), CONTRACT: COLUMN-HEADER (header verdict table), CONTRACT: INERTIA-ADVOCATE-TEMPLATE. Phases reference by name ("Apply CONTRACT: FIELD-REGISTER").
- V-04: FAIL -- All constraints remain as inline prose within phase steps. SKILL ENTRY pre-declares what will be checked but the rules themselves are still embedded in phases. Pre-declaration != extraction.
- V-05: PASS -- Same five CONTRACT blocks as V-03, plus CONTRACT: AUDIT-CHECKLIST. All phases reference contracts by name. No rule is restated inside a phase; every phase is a thin referencing layer.

---

## Scoring Worksheets

**V-01: Pre-Declared + Terminal**
```
Essential:    5 / 5  =>  5 * 60 / 5  = 60
Recommended:  2 / 2  =>  2 * 30 / 2  = 30
Aspirational: 8 / 10 =>  8 * 10 / 10 = 8   (fails C-15, C-17)
Composite: 98   Golden: YES
```

**V-02: In-Phase + No Pre-Declaration**
```
Essential:    5 / 5  =>  5 * 60 / 5  = 60
Recommended:  2 / 2  =>  2 * 30 / 2  = 30
Aspirational: 8 / 10 =>  8 * 10 / 10 = 8   (fails C-16, C-17)
Composite: 98   Golden: YES
```

**V-03: CONTRACT-Only + Terminal**
```
Essential:    5 / 5  =>  5 * 60 / 5  = 60
Recommended:  2 / 2  =>  2 * 30 / 2  = 30
Aspirational: 8 / 10 =>  8 * 10 / 10 = 8   (fails C-15, C-16)
Composite: 98   Golden: YES
```

**V-04: In-Phase + Pre-Declared (no CONTRACTs)**
```
Essential:    5 / 5  =>  5 * 60 / 5  = 60
Recommended:  2 / 2  =>  2 * 30 / 2  = 30
Aspirational: 9 / 10 =>  9 * 10 / 10 = 9   (fails C-17)
Composite: 99   Golden: YES
```

**V-05: Full Three-Criteria**
```
Essential:    5 / 5  =>  5 * 60 / 5  = 60
Recommended:  2 / 2  =>  2 * 30 / 2  = 30
Aspirational: 10 / 10 => 10 * 10 / 10 = 10  (all pass)
Composite: 100   Golden: YES
```

---

## Final Rankings

| Rank | Variation | Score | Band | Differentiator |
|------|-----------|-------|------|----------------|
| 1 | V-05 Full Three-Criteria | 100 | Golden | All three new criteria satisfied; CONTRACT: AUDIT-CHECKLIST is the only pre-declared contract that maps each item to its gate phase |
| 2 | V-04 In-Phase + Pre-Declared | 99 | Golden | C-15 + C-16 together; pre-declaration names gate locations, making the distribution accountable -- only deficit is no CONTRACT extraction |
| T-3 | V-01 Pre-Declared + Terminal | 98 | Golden | C-16 only; commits to what will be checked, batches all checks at Phase 5 |
| T-3 | V-02 In-Phase + No Pre-Declaration | 98 | Golden | C-15 only; gates emerge organically from phases but no upfront commitment to full scope |
| T-3 | V-03 CONTRACT-Only + Terminal | 98 | Golden | C-17 only; all five contracts defined, phases referencing by name, audit still batched at Phase 5 |

---

## Rubric Separation Check

**Result: CONFIRMED -- no entanglement among C-15, C-16, C-17.**

- V-01/V-02/V-03 each score 98, each failing a different pair from {C-15, C-16, C-17}. Three-way tie confirms no criterion subsumes another.
- V-04 scores 99 -- outscore V-01/V-02/V-03 by exactly 1 point, confirming C-15 and C-16 are independently additive.
- V-05 is the sole 100 -- C-17 adds exactly 1 point when added to V-04's C-15+C-16 base.

**Independence test:** If C-17 were redundant with C-16, V-03 and V-01 would have scored identically on C-17 (both would have gotten it "for free"). They did not -- V-01 fails C-17 because all its rules are inline prose; V-03 passes C-17 because rules are extracted into named blocks. The distinction is measurable.

**Entanglement test:** If C-15 implied C-16, V-02 would have gotten C-16 as a byproduct of distributed gates. It did not -- V-02's gates emerge without any pre-declaration at skill entry. Distribution != declaration.

---

## Excellence Signals

**Signal from V-05: CONTRACT: AUDIT-CHECKLIST as traceability layer**
The pre-declared audit table maps each criterion ID (A-H) to its gate phase (Phase 3 Gate 3a, Phase 4 Gate 4b, etc.). This creates bidirectional traceability: from the pre-declaration to the execution point, and from each gate back to its declared obligation. Cross-reference notation (`Gate 3b [C]`) makes the mapping explicit at both ends. A model cannot silently add an undeclared gate or miss a declared one.

**Signal from V-05: Phases as thin referencing layers**
When all rules live in CONTRACT blocks, each phase needs only "Apply CONTRACT: FIELD-REGISTER" instead of repeating the full field-register rules. The skill text is shorter without losing enforcement. Rules have a single source of truth: updating CONTRACT: COLUMN-HEADER in one place updates every phase that references it.

**Signal from V-04: Pre-declaration with gate-phase mapping**
V-04's SKILL ENTRY names not just what will be checked, but where each item will be gated: "[B] All 12 frontmatter fields -- verified at Phase 3 Gate 3a." More informative than V-01's declaration (which only names items) and creates accountability for the in-phase distribution -- a variation could declare items upfront but distribute them to the wrong phases, and V-04's gate-phase mapping closes this gap.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["contract-audit-checklist: pre-declaring the full audit as a named CONTRACT table with gate-phase assignments creates bidirectional traceability from declaration to execution and back", "thin-phase-referencing: when all rules live in CONTRACT blocks phases become single-line references eliminating rule repetition without losing enforcement"]}
```