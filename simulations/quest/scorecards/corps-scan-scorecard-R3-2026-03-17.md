## Quest Score — corps-scan R3 (Rubric v3)

### Scoring Method

16 criteria × 10 pts. PASS = 10, PARTIAL = 5, FAIL = 0. Max = 160 pts.
Golden: all 5 essentials PASS AND composite ≥ 80 pts.

---

## V-01 — Output Format: NOT COMPLETE UNTIL Headers + Gate-Row Tables

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | Valid org.yaml code fence | PASS | Phase 3 template shows complete org.yaml with `groups:`, `teams:`, `exec-office:` |
| C-02 | Team areas derived from repo signals | PASS | `# source: Signal [ID]` on every team area; repair instruction routes to Phase 1 if missing |
| C-03 | Group structure organizes teams | PASS | Template nests teams under named groups; explicit constraint "flat team list with no grouping fails" |
| C-04 | Standard roles per team | PASS | "at least 2 named roles... 'TBD' and placeholder tokens are not named roles." Inertia Advocate excluded |
| C-05 | Does not write .craft/roles/ | PASS | Disclaimer at top; no role file content anywhere in prompt |
| C-06 | Pivot mode with rationale | PASS | Phase 2 requires `Primary signal: Signal [ID]` + one sentence reasoning |
| C-07 | Exec office placeholder | PASS | `exec-office:` with `name:` in template |
| C-08 | Amend options listed | PASS | Phase 4: AMEND-A/B/C with named commands `/corps-scan --pivot`, `--exec-office`, `--groups` |
| C-09 | Pre-YAML scan inventory | PASS | Signal Inventory Table in Phase 1 before any YAML |
| C-10 | Draft boundary before first structural content | PASS | "State this before any structural content: 'This is a draft org.yaml…'" — explicit directive |
| C-11 | Inventory as typed table | PASS | 4-column table: Signal ID, Path or Identifier, Type, Pivot Mode Fit |
| C-12 | Pivot rationale cites specific named signal | PASS | Phase 2 reasoning "must name the Signal ID" |
| C-13 | Hard ordering gate between inventory and YAML | PASS | "Any YAML content appearing before the GATE row is an ordering error" + NOT COMPLETE UNTIL header |
| C-14 | Gate row as terminal row of inventory table | PASS | `\| **GATE** \| **INVENTORY COMPLETE** \| **[n] signals** \| **YAML authoring authorized** \|` as final row; constraint requires it structurally |
| C-15 | Phase incompleteness predicate per phase | PASS | All 4 phases open with "Phase N is NOT COMPLETE until [artifact]" — covers inventory, YAML, and amend phases |
| C-16 | Traceability failure triggers repair instruction | PASS | "If a team area has no matching Signal ID, return to Phase 1 and add the missing signal before continuing" |

**V-01 Score: 160 / 160** — All essentials PASS. **GOLDEN**

---

## V-02 — Lifecycle Emphasis: Explicit Phase Completion Tests

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | Valid org.yaml code fence | PASS | Phase 3 template complete with all required keys |
| C-02 | Team areas derived from repo signals | PASS | `# anchor: Signal [ID]` per team area; traceability rule + repair instruction |
| C-03 | Group structure organizes teams | PASS | Nested groups template; "at least one `groups:` container above teams" |
| C-04 | Standard roles per team | PASS | "at least 2 named roles. No 'TBD'." Inertia Advocate excluded |
| C-05 | Does not write .craft/roles/ | PASS | Disclaimer required output at top; no role file content |
| C-06 | Pivot mode with rationale | PASS | `Basis: Signal [ID]` + reasoning naming Signal ID |
| C-07 | Exec office placeholder | PASS | `exec-office:` with name in template |
| C-08 | Amend options listed | PASS | Phase 4 AMEND-A/B/C with commands |
| C-09 | Pre-YAML scan inventory | PASS | Signal Inventory Table before YAML in Phase 1 |
| C-10 | Draft boundary before first structural content | PASS | "Output this line before any structural content: 'Draft org.yaml for human review only…'" |
| C-11 | Inventory as typed table | PASS | 4-column typed table with GATE terminal row |
| C-12 | Pivot rationale cites specific named signal | PASS | Phase 2 Completion Test verifies "Named Signal ID present in basis statement: YES / NO" |
| C-13 | Hard ordering gate | PASS | "Phase 2 does not open until 'Gate row present as final table row: YES' appears" |
| C-14 | Gate row as terminal row of inventory table | PASS | Terminal GATE row in typed table; Phase 1 Completion Test requires "Gate row present: YES" as mandatory output before Phase 2 |
| C-15 | Phase incompleteness predicate per phase | PASS | Post-phase Completion Test per phase: "Phase N does not open until [condition]: YES" — equivalent predicate for inventory, pivot, YAML, and amend phases |
| C-16 | Traceability failure triggers repair instruction | PASS | Phase 3 Completion Test: "If 'Traceability failures' is greater than 0: return to Phase 1 and add the missing signals before proceeding to Phase 4" |

**V-02 Score: 160 / 160** — All essentials PASS. **GOLDEN**

---

## V-03 — Phrasing Register: INVARIANT / VIOLATION / REPAIR Notation

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | Valid org.yaml code fence | PASS | Phase 3 template complete with all required keys |
| C-02 | Team areas derived from repo signals | PASS | `# signal: Signal [ID]` annotation + Phase 3 REPAIR routes to Phase 1 |
| C-03 | Group structure organizes teams | PASS | Groups template; INVARIANT VIOLATION CHECK includes "groups: present" |
| C-04 | Standard roles per team | PASS | "at least 2 named roles. 'TBD' and placeholder tokens are not named roles." |
| C-05 | Does not write .craft/roles/ | PASS | Disclaimer required output; no .craft/roles/ content |
| C-06 | Pivot mode with rationale | PASS | Phase 2 `Basis: Signal [ID]` + reasoning; VIOLATION names the failure condition |
| C-07 | Exec office placeholder | PASS | `exec-office:` with name in YAML template |
| C-08 | Amend options listed | PASS | Phase 4 AMEND-A/B/C with named commands; Phase 4 REPAIR names the correct form |
| C-09 | Pre-YAML scan inventory | PASS | Typed Signal Inventory Table in Phase 1 pre-YAML |
| C-10 | Draft boundary before first structural content | PASS | "State before any structural content: 'This output is a draft org.yaml…'" |
| C-11 | Inventory as typed table | PASS | 4-column typed table with GATE terminal row |
| C-12 | Pivot rationale cites specific named signal | PASS | Phase 2 VIOLATION block: "Pivot mode references 'repo shape' without naming a Signal ID" — confirms named Signal ID is required |
| C-13 | Hard ordering gate | PASS | Phase 1 INVARIANT requires GATE row; VIOLATION: "Phase 2 begins before the GATE row is present" |
| C-14 | Gate row as terminal row of inventory table | PASS | INVARIANT: "Signal Inventory Table exists with >= 3 signal rows AND a terminal GATE row as the table's final row" |
| C-15 | Phase incompleteness predicate per phase | PASS | INVARIANT block per phase states the condition that must be satisfied before exit — all four phases covered |
| C-16 | Traceability failure triggers repair instruction | PASS | Phase 3 REPAIR: "Return to Phase 1 and add the missing signal as a new table row before the GATE row. Assign it a Signal ID. Then add the `# signal:` annotation…" |

**V-03 Score: 160 / 160** — All essentials PASS. **GOLDEN**

---

## V-04 — Output Format + Lifecycle: Dual Gate Architecture

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | Valid org.yaml code fence | PASS | Phase 3 template complete with all required keys |
| C-02 | Team areas derived from repo signals | PASS | `# trace: Signal [ID]` per team area; two repair paths (inline + Completion Test) |
| C-03 | Group structure organizes teams | PASS | Nested groups template; "at least one `groups:` container above teams" |
| C-04 | Standard roles per team | PASS | "Every team area: at least 2 named roles. No 'TBD'." Inertia Advocate excluded |
| C-05 | Does not write .craft/roles/ | PASS | Disclaimer at top; no .craft/roles/ content |
| C-06 | Pivot mode with rationale | PASS | `Primary signal: Signal [ID]` + reasoning naming Signal ID |
| C-07 | Exec office placeholder | PASS | `exec-office:` with name in template |
| C-08 | Amend options listed | PASS | Phase 4 AMEND-A/B/C with named commands |
| C-09 | Pre-YAML scan inventory | PASS | Signal Inventory Table in Phase 1 pre-YAML |
| C-10 | Draft boundary before first structural content | PASS | "State this before any structural content: 'This output is a draft org.yaml for review only…'" |
| C-11 | Inventory as typed table | PASS | 4-column typed table with GATE terminal row |
| C-12 | Pivot rationale cites specific named signal | PASS | Phase 2 Completion Test: "Named Signal ID in basis: YES / NO" enforces the named citation |
| C-13 | Hard ordering gate | PASS | "The GATE row must be the final row. Any Phase 2 content before the GATE row is a gate violation." + Completion Test gate |
| C-14 | Gate row as terminal row of inventory table | PASS | `\| **GATE** \| **INVENTORY COMPLETE** \| **[n] signals** \| **Phase 2 authorized** \|` as terminal row; Completion Test requires "YES" for this field |
| C-15 | Phase incompleteness predicate per phase | PASS | **Dual enforcement**: all 4 phases have a pre-phase "NOT COMPLETE UNTIL" header AND a post-phase Completion Test — strongest C-15 implementation |
| C-16 | Traceability failure triggers repair instruction | PASS | Two explicit repair instructions: inline constraint ("return to Phase 1 and add the missing signal") + Phase 3 Completion Test ("if > 0: return to Phase 1") |

**V-04 Score: 160 / 160** — All essentials PASS. **GOLDEN**

---

## V-05 — Role Sequence + Phrasing Register: Invariant-Gated Specialist Roles

| # | Criterion | Result | Evidence |
|---|-----------|--------|----------|
| C-01 | Valid org.yaml code fence | PASS | Role 3 (DRAFTER) template complete with all required keys |
| C-02 | Team areas derived from repo signals | PASS | `# anchor: Signal [ID]` per team area; DRAFTER REPAIR routes to Role 1 |
| C-03 | Group structure organizes teams | PASS | Nested groups in DRAFTER template; "at least one `groups:` container above teams" |
| C-04 | Standard roles per team | PASS | "at least 2 named roles. No 'TBD'." Inertia Advocate excluded |
| C-05 | Does not write .craft/roles/ | PASS | Skill-wide constraint at very top: "Any role output containing role file content is a skill violation." Strongest C-05 framing of all 5 variations |
| C-06 | Pivot mode with rationale | PASS | Role 2 PIVOT ANALYST output requires `Decision signal: Signal [ID]` + reasoning |
| C-07 | Exec office placeholder | PASS | `exec-office:` with name in Role 3 template |
| C-08 | Amend options listed | PASS | Role 3 Action 2: all three AMEND options with commands |
| C-09 | Pre-YAML scan inventory | PASS | Role 1 SCANNER produces typed table before Role 3 (YAML phase) |
| C-10 | Draft boundary before first structural content | PASS | "State before Role 1 begins: 'Draft org.yaml for review only…'" + skill-wide constraint precedes all roles |
| C-11 | Inventory as typed table | PASS | 4-column typed table with GATE terminal row in Role 1 |
| C-12 | Pivot rationale cites specific named signal | PASS | Role 2 exit declaration: "mode `[mode]` selected on Signal [ID]"; "Decision signal" field required in output |
| C-13 | Hard ordering gate | PASS | Role 1 EXIT INVARIANT requires GATE row; VIOLATION: "Role 2 activates before the GATE row is present"; Role 1 Exit Declaration required before Role 2 |
| C-14 | Gate row as terminal row of inventory table | PASS | EXIT INVARIANT: "Signal Inventory Table exists with >= 3 signal rows AND a terminal GATE row as the table's final row" |
| C-15 | Phase incompleteness predicate per phase | PASS | "ROLE N IS NOT COMPLETE until the EXIT INVARIANT is satisfied" per role — all three roles (inventory, pivot, YAML) have explicit incompleteness predicates; ENTRY CONDITIONs additionally enforce inter-phase ordering |
| C-16 | Traceability failure triggers repair instruction | PASS | Role 3 REPAIR: "Return to Role 1 table. Add the missing signal as a new signal row inserted before the GATE row. Assign the next Signal ID." Rules also: "apply the REPAIR instruction before continuing" |

**V-05 Score: 160 / 160** — All essentials PASS. **GOLDEN**

---

## Composite Scores

| Variation | Essential (50) | Recommended (30) | Aspirational (80) | Total (160) | Golden? |
|-----------|----------------|------------------|-------------------|-------------|---------|
| V-01 | 50 | 30 | 80 | **160** | YES |
| V-02 | 50 | 30 | 80 | **160** | YES |
| V-03 | 50 | 30 | 80 | **160** | YES |
| V-04 | 50 | 30 | 80 | **160** | YES |
| V-05 | 50 | 30 | 80 | **160** | YES |

All five variations achieve the v3 maximum. The R3 design held — every variation was constructed to carry forward full v2 coverage while satisfying all three new criteria.

---

## Ranking by Mechanism Strength

All variations tie numerically. Ranked by enforcement robustness:

1. **V-04** — Dual gate architecture: pre-phase "NOT COMPLETE UNTIL" header + post-phase Completion Test per phase. A model that ignores one cannot ignore both. C-15 doubly enforced; C-16 appears twice (inline + Completion Test).
2. **V-05** — Role-exit invariant structure: ENTRY CONDITION / EXIT INVARIANT / REPAIR per specialist role. C-05 expressed as a skill-level violation, not a phase instruction — strongest boundary framing. VIOLATION/REPAIR structurally impossible to omit.
3. **V-03** — INVARIANT/VIOLATION/REPAIR notation: Phase 3 INVARIANT VIOLATION CHECK is the most exhaustive pre-continuation verification of all variations.
4. **V-02** — Post-phase completion tests convert predicates into mandatory output blocks. The model must write the completion state — it cannot skip it silently.
5. **V-01** — Cleanest: two conventions (NOT COMPLETE UNTIL header + GATE row) cover all three new criteria with minimum added structure. Lowest cognitive load.

---

## Excellence Signals

**From V-04 (top by mechanism strength):**

**Dual-gate C-15 enforcement.** Placing the incompleteness predicate BOTH before the phase body (header) AND after it (Completion Test output) creates two independent enforcement points. A model that reads the header as preamble and continues cannot skip writing the Completion Test, which explicitly requires YES/NO answers before the next phase opens. Single-mechanism C-15 (headers only, or completion tests only) has one bypass path; dual-gate has none.

**Completion Test as mandatory output for traceability.** The Phase 3 Completion Test requires writing "Traceability failures: [n]" as an output field. If the value is non-zero, the repair instruction fires. This converts C-16 from an inline constraint (which could be read and ignored) into a required arithmetic output — the model must count and report the failures, making silent bypass structurally harder.

**From V-05:**

**Skill-wide constraint before all roles.** Stating the draft-only boundary as a skill-level invariant ("Any role output containing role file content is a skill violation") before any phase or role begins creates a higher-authority constraint than per-phase disclaimers. The violation framing makes C-05 a system error, not an instruction to follow.

**Per-role exit declaration as activation token.** Role N's Exit Declaration is the literal activation condition for Role N+1. This converts the phase handoff from a sequential instruction into a structural handshake — Role 2 "IS NOT ACTIVE" without Role 1's exit declaration in the output. The handshake pattern makes phase ordering auditable from the output transcript alone.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["dual-gate: pre-phase NOT COMPLETE UNTIL header combined with post-phase Completion Test output creates double-enforcement of C-15 that survives single-mechanism failure", "completion-test-as-mandatory-output: phase incompleteness predicate written as a required output block with YES/NO fields makes the predicate executable and the traceability count auditable", "skill-wide-violation-framing: stating draft-only boundary as a skill-level violation constraint before all phases creates higher-authority than per-phase disclaimers", "role-exit-declaration-as-activation-token: EXIT INVARIANT satisfied condition written as a named declaration activates the next role, making phase handoffs auditable from transcript alone"]}
```
