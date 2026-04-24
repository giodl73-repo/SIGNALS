## Quest Score — corps-scan Variate R2

**Rubric**: v2 (13 criteria, 130 pts max)
**Golden threshold**: all 5 essentials pass AND composite >= 80 pts

---

## V-01 — Output Format: Typed Inventory Table

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Valid org.yaml code fence | Essential | **PASS** | Explicit yaml template with `groups:`, `teams:`, `exec-office:` shown; constraint "groups: section must contain at least one named group container" |
| C-02 Team areas from repo signals | Essential | **PASS** | "Every team area name must correspond to a row in the Signal Inventory Table. If you are naming a team area that has no matching row, you are inventing names — stop." |
| C-03 Group structure organizes teams | Essential | **PASS** | "The `groups:` section must contain at least one named group container above teams. A flat team list with no grouping fails." |
| C-04 Standard roles per team | Essential | **PASS** | "at least 2 named roles. 'TBD' and 'role_1' are not roles." + "Inertia Advocate must NOT appear as a listed role." |
| C-05 Does not write .roles/ | Essential | **PASS** | "Do NOT write `.roles/` files. Do NOT instruct the user to create role files. Do NOT include role file content." — leading constraint |
| C-06 Pivot mode with rationale | Recommended | **PASS** | Pivot Decision block with quoted rationale requirement: "MUST name a specific path or identifier from the table" + example |
| C-07 Exec office placeholder | Recommended | **PASS** | exec-office: in template with `# placeholder: confirm name before running corps-build`; "exec-office: must be present with a name value" |
| C-08 Amend options | Recommended | **PASS** | Step 4 requires all three AMEND-A/B/C with specific commands; "'Let me know if you want changes' does not count. All three options are required." |
| C-09 Pre-YAML inventory | Aspirational | **PASS** | Step 1 (inventory table) precedes Step 3 (YAML); table is a structural prerequisite |
| C-10 Draft boundary before content | Aspirational | **PASS** | "State this constraint now, before any structural content:" followed by quoted statement to output |
| C-11 Inventory as typed table | Aspirational | **PASS** | 3-column typed table specified: `Signal \| Path or Identifier \| Pivot Relevance`; "Every row must have a value in all three columns." |
| C-12 Rationale cites specific named signal | Aspirational | **PASS** | "rationale MUST name a specific path or identifier from the table" + concrete example: "Signal row '/services/payments/'" |
| C-13 Hard ordering gate | Aspirational | **PASS** | Sentinel `` --- [SIGNAL INVENTORY COMPLETE] --- `` as literal code block + "Do NOT begin Step 2 until this sentinel line is written." |

**V-01 Score: 130 / 130** — all essentials PASS. **GOLDEN.**

---

## V-02 — Lifecycle Emphasis: Two-Gate Protocol

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Valid org.yaml code fence | Essential | **PASS** | yaml template with groups:, teams:, exec-office: |
| C-02 Team areas from repo signals | Essential | **PASS** | "Every team area name must trace to a Signal ID in the GATE-1 table. No invented names." |
| C-03 Group structure organizes teams | Essential | **PASS** | "At least one group container above teams." in YAML constraints |
| C-04 Standard roles per team | Essential | **PASS** | "at least 2 named roles"; "Inertia Advocate must NOT appear" |
| C-05 Does not write .roles/ | Essential | **PASS** | "corps-scan does not write `.roles/` files. It does not describe what role files would contain." — stated unconditionally |
| C-06 Pivot mode with rationale | Recommended | **PASS** | GATE-2 Basis line: "must cite a Signal ID from the GATE-1 inventory. A mode selection without a named signal citation is not confirmed." |
| C-07 Exec office placeholder | Recommended | **PASS** | exec-office: in template with placeholder note |
| C-08 Amend options | Recommended | **PASS** | Three amend options with Signal ID references in AMEND-A alternatives |
| C-09 Pre-YAML inventory | Aspirational | **PASS** | GATE-1 inventory table must exist before "YAML authoring is now AUTHORIZED" |
| C-10 Draft boundary before content | Aspirational | **PARTIAL** | Scope constraint block present at top of prompt but no explicit "say this before structural content" instruction; model not directed to output the boundary statement as first visible line |
| C-11 Inventory as typed table | Aspirational | **PASS** | 4-column typed table: `Signal ID \| Path or Name \| Category \| Org Mode Implication` with column definitions |
| C-12 Rationale cites specific named signal | Aspirational | **PASS** | GATE-1 clearance requires named Signal ID; GATE-2 Basis "must cite a Signal ID" |
| C-13 Hard ordering gate | Aspirational | **PASS** | "YAML authoring does not begin before this statement. Any YAML appearing above this line is an ordering violation." |

**V-02 Score: 125 / 130** — all essentials PASS. **GOLDEN.** (C-10 PARTIAL = -5)

---

## V-03 — Phrasing Register: Precondition/Postcondition Specification

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Valid org.yaml code fence | Essential | **PASS** | yaml template with required keys; Phase 3 postcondition checklist verifies `groups:`, `teams:`, `exec-office:` all present |
| C-02 Team areas from repo signals | Essential | **PASS** | Postcondition: "all teams grounded in Phase 1 identifiers"; checklist: "Every team area name traces to a Phase 1 Identifier" |
| C-03 Group structure organizes teams | Essential | **PASS** | Phase 3 checklist: "At least one group container above teams" |
| C-04 Standard roles per team | Essential | **PASS** | Checklist: "Every team area has 2+ named roles (no TBD, no placeholder role names)"; "Inertia Advocate does NOT appear as a listed role" |
| C-05 Does not write .roles/ | Essential | **PASS** | SCOPE CONSTRAINT block + Phase 3 PRECONDITION + checklist item; triple-layered |
| C-06 Pivot mode with rationale | Recommended | **PASS** | Phase 2 postcondition: "Basis: Identifier '[exact value from Phase 1 table]'" — postcondition violation if missing |
| C-07 Exec office placeholder | Recommended | **PASS** | Template shows exec-office: + Phase 3 checklist includes it |
| C-08 Amend options | Recommended | **PASS** | Phase 4 postcondition: "3 named amend options with commands; no generic 'let me know' language" |
| C-09 Pre-YAML inventory | Aspirational | **PASS** | Phase 1 produces typed table; Phase 3 PRECONDITION: "Phase 2 complete" which requires Phase 1 complete |
| C-10 Draft boundary before content | Aspirational | **PASS** | "State the draft boundary now, before any operational content:" with quoted output statement |
| C-11 Inventory as typed table | Aspirational | **PASS** | Phase 1 POSTCONDITION: 4-column typed table `Signal \| Identifier \| Type \| Mode Fit`; "Phase 1 is not complete until the typed table exists" |
| C-12 Rationale cites specific named signal | Aspirational | **PASS** | Phase 2 postcondition: "Basis: Identifier '[exact value from Phase 1 table]'"; "A pivot mode statement without a named Identifier citation is a postcondition violation" |
| C-13 Hard ordering gate | Aspirational | **PASS** | Phase transition declarations + cascading PRECONDITION chain: Phase 3 PRECONDITION requires Phase 2 complete, Phase 2 PRECONDITION requires Phase 1 complete with typed table |

**V-03 Score: 130 / 130** — all essentials PASS. **GOLDEN.**

---

## V-04 — Table IS the Gate (Output Format + Lifecycle Emphasis)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Valid org.yaml code fence | Essential | **PASS** | yaml template with groups:, teams:, exec-office:; mandatory constraints listed |
| C-02 Team areas from repo signals | Essential | **PASS** | "Every team area name must map to a Signal ID in the inventory table. If a team area has no matching Signal ID, return to Part 1 and add the missing signal before continuing." |
| C-03 Group structure organizes teams | Essential | **PASS** | "At least one group container (division, tribe, pillar) above teams. No flat team list." |
| C-04 Standard roles per team | Essential | **PASS** | "Every team area must list at least 2 named roles. Role names must be specific job functions." + "Inertia Advocate must NOT appear as a listed role." |
| C-05 Does not write .roles/ | Essential | **PASS** | "Non-negotiable scope: This skill does not write `.roles/` files." |
| C-06 Pivot mode with rationale | Recommended | **PASS** | Part 2 requires mode + "Primary signal: [Signal ID] — '[Path or Name]' — [why one sentence]"; failure stated explicitly |
| C-07 Exec office placeholder | Recommended | **PASS** | exec-office: in template with placeholder note; "exec-office: must be present" |
| C-08 Amend options | Recommended | **PASS** | Part 4 requires all three options with Signal IDs for alternatives |
| C-09 Pre-YAML inventory | Aspirational | **PASS** | Part 1 inventory table precedes Part 3 YAML; GATE ROW enforces the boundary |
| C-10 Draft boundary before content | Aspirational | **PASS** | "Say this before any structural output:" with quoted statement |
| C-11 Inventory as typed table | Aspirational | **PASS** | 4-column typed table with Signal ID; GATE ROW is terminal row — structurally inseparable from typed table |
| C-12 Rationale cites specific named signal | Aspirational | **PASS** | "The `Primary signal` field must name a Signal ID from the inventory table. A pivot declaration that does not cite a Signal ID fails this part regardless of the rationale quality." |
| C-13 Hard ordering gate | Aspirational | **PASS** | GATE ROW `\| GATE \| INVENTORY COMPLETE \| [n] signals \| YAML authoring authorized \|` is part of the table itself; "Any YAML appearing before the GATE row is an ordering error." C-11 and C-13 are structurally inseparable. |

**V-04 Score: 130 / 130** — all essentials PASS. **GOLDEN.**

---

## V-05 — Role Sequence + Typed Table (Role Sequence + Output Format)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Valid org.yaml code fence | Essential | **PASS** | ROLE 3 yaml template with groups:, teams:, exec-office:; DRAFTER COMPLETE declaration verifies group/team count |
| C-02 Team areas from repo signals | Essential | **PASS** | "Every team area must have an `# anchor: Signal [ID]` comment tracing it to a Signal Inventory row. A team area without an anchor is not grounded." |
| C-03 Group structure organizes teams | Essential | **PASS** | "At least one group container above teams." |
| C-04 Standard roles per team | Essential | **PASS** | "Every team area must list at least 2 named roles. No TBD. No placeholder role names. Inertia Advocate must NOT appear as a listed role." |
| C-05 Does not write .roles/ | Essential | **PASS** | Skill-wide constraint applies to all three roles; "Any role output containing role file content is a skill violation." ROLE 3 re-states it. |
| C-06 Pivot mode with rationale | Recommended | **PASS** | ROLE 2 "Decision signal: [Signal ID] — '[Identifier]'" is mandatory; completion declaration must include Signal ID |
| C-07 Exec office placeholder | Recommended | **PASS** | exec-office: in ROLE 3 template with placeholder note |
| C-08 Amend options | Recommended | **PASS** | ROLE 3 Action 2 requires all three amend options; "All three amend options are required." |
| C-09 Pre-YAML inventory | Aspirational | **PASS** | ROLE 1 (SCANNER) produces typed table; ROLE 3 (DRAFTER) entry condition requires ROLE 2 completion, which requires ROLE 1 completion |
| C-10 Draft boundary before content | Aspirational | **PASS** | "State the draft boundary before the first role:" with quoted output statement |
| C-11 Inventory as typed table | Aspirational | **PASS** | ROLE 1 required output: 4-column typed table `Signal ID \| Identifier (exact path or name) \| Type \| Pivot Mode Fit`; min 3 rows |
| C-12 Rationale cites specific named signal | Aspirational | **PASS** | ROLE 2: "Decision signal field is mandatory. A pivot analysis without a named Signal ID citation is incomplete and the DRAFTER must request a re-analysis before proceeding." |
| C-13 Hard ordering gate | Aspirational | **PASS** | "The next role does not begin until the prior role's completion declaration is written." ROLE 3 entry condition: "ROLE 2 COMPLETION declaration exists and pivot mode is confirmed with a named Signal ID citation." |

**V-05 Score: 130 / 130** — all essentials PASS. **GOLDEN.**

---

## Score Summary

| Variation | Essential (50) | Recommended (30) | Aspirational (50) | Total | Golden? |
|-----------|---------------|-----------------|------------------|-------|---------|
| V-01 | 50 (5/5) | 30 (3/3) | 50 (5/5) | **130** | YES |
| V-02 | 50 (5/5) | 30 (3/3) | 45 (4.5/5) | **125** | YES |
| V-03 | 50 (5/5) | 30 (3/3) | 50 (5/5) | **130** | YES |
| V-04 | 50 (5/5) | 30 (3/3) | 50 (5/5) | **130** | YES |
| V-05 | 50 (5/5) | 30 (3/3) | 50 (5/5) | **130** | YES |

**All five variations are golden. V-02 is the only one below 130.**

---

## Ranking

1. **V-04 — 130/130** (top by mechanism elegance: C-11 and C-13 are structurally inseparable — cannot write the gate without the typed table)
2. **V-05 — 130/130** (role completion declarations are the hardest gate form; re-analysis request is unique)
3. **V-01 — 130/130** (simplest fully-compliant form; sentinel line is the clearest human-readable gate)
4. **V-03 — 130/130** (postcondition checklist provides self-verification; most verbose but most resilient to checklist skipping)
5. **V-02 — 125/130** (C-10 PARTIAL: no explicit instruction to output the draft boundary before structural content)

---

## Excellence Signals

Patterns from R2 top-scoring variations that were not present in R1:

**1. Signal ID column makes C-12 structurally trivial (all V-01 through V-05)**
Every variation in R2 introduces a `Signal ID` column (S-01, S-02...) in the typed table. This means the pivot rationale can cite a short token (`Signal S-03`) rather than requiring an exact path string. The citation requirement becomes low-friction once the IDs exist — the model cannot fail C-12 by "forgetting to name a signal" because the IDs are already labeled in the table it just wrote.

**2. Gate-row embedded as final table row (V-04)**
V-04's GATE ROW is not a separate sentinel — it is the terminal row of the typed table itself. This makes C-11 and C-13 inseparable by construction: the gate cannot exist without the typed table, and the typed table cannot be complete without the gate row. Any YAML before the GATE row is defined as an ordering error, not advisory advice.

**3. Role completion declarations as verifiable success criteria (V-05)**
V-05's completion declarations (`SCANNER COMPLETE: [n] signals catalogued. Strongest pivot signal: [Signal ID] — [Identifier].`) require the model to summarize specific results — count of signals, strongest Signal ID, identifier name — not just declare that a phase is done. This converts the gate from a formatting requirement into an evidence checkpoint. ROLE 3's entry condition specifies that it "must request a re-analysis" if ROLE 2's declaration is missing, introducing a correction loop absent from all other variations.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Signal ID column scheme (S-01, S-02) makes pivot rationale citation structurally trivial — low-friction C-12 compliance once IDs exist in the table", "Gate-row embedded as terminal table row makes C-11 and C-13 structurally inseparable — cannot satisfy C-13 without first satisfying C-11", "Role completion declarations as verifiable evidence checkpoints — require specific counts and Signal ID citations, not just phase-done declarations, and introduce a correction loop if missing"]}
```
