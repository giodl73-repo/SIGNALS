## crew-check — Quest Scorecard R4 (Rubric v4)

### Evaluation Summary

All five variations carry the R3 floor (C-11 through C-16 PASS) and the full essential + recommended baseline. R4 differentiates on C-17 and C-18 exclusively.

---

### Per-Variation Scoring

#### V-01 — Named Halt IDs as Four-Position Bindings

| Tier | ID | Score | Evidence |
|------|----|-------|----------|
| Essential | C-01 | PASS (12) | Role source traceability maintained from R3 baseline |
| Essential | C-02 | PASS (12) | Review matrix structure present |
| Essential | C-03 | PASS (12) | Perspective fidelity via lens-anchor step (C-11) |
| Essential | C-04 | PASS (12) | Depth mode compliance present |
| Essential | C-05 | PASS (12) | Severity present in matrix |
| Recommended | C-06 | PASS (10) | Finding specificity carried from R3 |
| Recommended | C-07 | PASS (10) | Recommendation actionability present |
| Recommended | C-08 | PASS (10) | Severity calibration consistent |
| Aspirational | C-09–C-16 | PASS (16) | Full R3 floor confirmed |
| Aspirational | C-17 | **PASS (2)** | Four-position bindings: registry definition, gate headers (`GATE 1 [G1]`), verbatim error messages, AMEND routing keys (`--amend rerun:G4-{role}`, `--amend reload:G1`). Sub-gate hierarchy (G4a, G4b, G4c, G4d) encodes position — strongest C-17 in R4 among single-criterion variations |
| Aspirational | C-18 | **FAIL (0)** | Has per-gate AMEND routing keys but no `--amend halts` sub-command enumerating all fired gates. Per-gate routing is not gate-audit enumeration |

**Composite: 108 / 110**
Golden: YES (all essential PASS; 108 >= 80)

---

#### V-02 — Structured Gate-Audit Output

| Tier | ID | Score | Evidence |
|------|----|-------|----------|
| Essential | C-01–C-05 | PASS (60) | R3 baseline maintained |
| Recommended | C-06–C-08 | PASS (30) | R3 baseline maintained |
| Aspirational | C-09–C-16 | PASS (16) | Full R3 floor confirmed |
| Aspirational | C-17 | **PARTIAL (1)** | Gate IDs present in audit table ("Gate ID" column); "Defining the format forces tracking throughout execution" implies IDs persist through runtime — but the four-position binding system (explicit registry, gate-header decoration, verbatim error ID, AMEND routing key) is not the design axis. IDs are instrumentally present, not architecturally primary |
| Aspirational | C-18 | **PASS (2)** | Defines exact `--amend halts` output format: table with Gate ID, gate name, message triggered, resolution step. Adds `--amend halts:{id}` for focused single-gate lookup. Format specification forces tracking throughout execution — most complete C-18 in R4 |

**Composite: 109 / 110**
Golden: YES

---

#### V-03 — Self-Routing Halt Messages

| Tier | ID | Score | Evidence |
|------|----|-------|----------|
| Essential | C-01–C-05 | PASS (60) | R3 baseline maintained |
| Recommended | C-06–C-08 | PASS (30) | R3 baseline maintained |
| Aspirational | C-09–C-16 | PASS (16) | Full R3 floor confirmed |
| Aspirational | C-17 | **PASS (2)** | Explicitly noted "Halt IDs are still stable (C-17 floor)." Named IDs like `[G4a-pm]` appear verbatim in halt messages: `HALT [G4a-pm]: Lens anchor absent.` Stable ID system present, though not defined via four-position binding |
| Aspirational | C-18 | **FAIL (0)** | No `--amend halts` enumeration sub-command. Recovery is embedded in halt messages themselves (`→ To continue: /crew-check [artifact] --amend rerun:pm`), which is a different mechanism — self-routing, not gate-audit |

**Composite: 108 / 110**
Golden: YES

---

#### V-04 — Named Halt IDs + Structured Gate-Audit

| Tier | ID | Score | Evidence |
|------|----|-------|----------|
| Essential | C-01–C-05 | PASS (60) | R3 baseline maintained |
| Recommended | C-06–C-08 | PASS (30) | R3 baseline maintained |
| Aspirational | C-09–C-16 | PASS (16) | Full R3 floor confirmed |
| Aspirational | C-17 | **PASS (2)** | Explicitly "four-position named IDs (C-17)." Audit resolution steps reference the same gate IDs seen in headers and error messages — three independent evidence trails per failure, satisfying the coupling requirement noted in rubric preamble |
| Aspirational | C-18 | **PASS (2)** | Explicitly "cross-referenced by the structured audit output (C-18)." Audit block enumerates fired gates using the same stable IDs — the coupling between C-17 and C-18 is the design axis. Strongest demonstration of the coupled use case |

**Composite: 110 / 110**
Golden: YES

---

#### V-05 — Full v4 Integration + Priority Summary + Audit-as-AMEND-Menu

| Tier | ID | Score | Evidence |
|------|----|-------|----------|
| Essential | C-01–C-05 | PASS (60) | R3 baseline maintained |
| Recommended | C-06–C-08 | PASS (30) | R3 baseline maintained |
| Aspirational | C-09–C-16 | PASS (16) | Full R3 floor confirmed; priority summary (R3 V-05 pattern) enhances C-09 cross-role synthesis |
| Aspirational | C-17 | **PASS (2)** | Self-routing halt messages (V-03 pattern) carry stable named IDs; `HALT [G4a-pm]` form present. IDs appear in halt messages with embedded recovery commands |
| Aspirational | C-18 | **PASS (2)** | Audit block present; each entry includes a ready-to-paste re-entry command (audit-as-AMEND-menu). Extends C-18 beyond introspection to execution: user holds an action list, not a diagnostic report |

**Composite: 110 / 110**
Golden: YES

---

### Ranking

| Rank | Variation | Score | Delta |
|------|-----------|-------|-------|
| 1 (tie) | V-05 | 110/110 | Full v4; self-routing halts + executable audit |
| 1 (tie) | V-04 | 110/110 | Full v4; strongest C-17+C-18 coupling |
| 3 | V-02 | 109/110 | C-18 PASS; C-17 PARTIAL (instrumentally present) |
| 4 (tie) | V-01 | 108/110 | C-17 PASS; C-18 FAIL (routing vs. enumeration) |
| 4 (tie) | V-03 | 108/110 | C-17 PASS; C-18 FAIL (self-routing replaces audit) |

**Tiebreaker V-05 over V-04:** V-05 demonstrates all four mechanisms simultaneously — four-position IDs, gate-audit enumeration, self-routing halt messages, and executable audit entries — making the skill's error recovery fully self-contained. V-04 couples C-17+C-18 cleanly but requires the user to run `--amend halts` separately; V-05 surfaces the action list automatically.

---

### Excellence Signals (V-05)

Two patterns from the top-scoring variation not yet captured as rubric criteria:

**Signal 1 — Self-routing halt message**
The halt output is a self-contained recovery unit. Pattern: `HALT [G4a-pm]: Lens anchor absent. → To continue: /crew-check [artifact] --amend rerun:pm`. The user does not need to consult documentation or run a separate audit command — the halt message itself is the recovery instruction. Appears in V-03 and V-05 (two variations).

**Signal 2 — Executable audit block**
The `--amend halts` output is not diagnostic-only. Each row includes a ready-to-paste re-entry command alongside the Gate ID, gate name, and message. The audit doubles as an AMEND menu. Appears in V-05 (one variation, but architecturally distinct from C-18's introspection-only form). V-05's explicit claim: "any halt leaves the user with a structured action list, not a diagnostic puzzle."

**Confirmed pattern (R3 → R4):** Priority summary tier between matrix and synthesis. Present in R3 V-05, present again in R4 V-05 — confirming it as a durable structural pattern, not a one-round signal.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["Self-routing halt message: halt output embeds recovery command inline making each halt self-contained without requiring separate audit lookup", "Executable audit block: audit entries include ready-to-paste re-entry commands converting gate-audit from diagnostic report into actionable AMEND menu"]}
```
