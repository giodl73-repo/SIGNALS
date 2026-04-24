---

## crew-check — Quest Score R5

### All Variations: 114 / 114 (Golden)

All five variations cleared every criterion. All five essential PASS. All aspirational through C-20 PASS. Five-way tie at maximum score.

---

### Per-Variation Breakdown

| Var | Axis | C-19 | C-20 | Score | Golden |
|-----|------|------|------|-------|--------|
| V-01 | Sub-gate precision routing | **DEEP** | incidental | 114/114 | Yes |
| V-02 | Audit-as-numbered-action-queue | yes | **DEEP** | 114/114 | Yes |
| V-03 | Two-tier halt classification (BLOCKING/SCOPED) | incidental | incidental | 114/114 | Yes |
| V-04 | Cross-referenced halt + audit | yes | yes | 114/114 | Yes |
| V-05 | Recovery-first flow | yes | yes | 114/114 | Yes |

**Qualitative rank**: V-05 > V-01 = V-02 > V-04 > V-03 (by structural novelty and recovery completeness, not score)

---

### Key Evidence Notes

**V-01** — Sub-gate precision is C-19 deepened beyond R4. `HALT [G4c-{role}]` embeds `--amend rerun:G4c-{role}`, not `--amend rerun:{role}`. Re-entry semantics stated per sub-gate ("resumes from this step, skipping G4a–G4b"). Minimum-restart routing.

**V-02** — C-20 DEEP via numbered sequential action queue. Format explicitly: "execute 1 → 2 → ... → re-run." Terminal entry provides the re-run command. Cognitive artifact changes from reference table to executable procedure.

**V-03** — Genuinely new axis: BLOCKING (run-level, full stop) vs SCOPED (row-level, row excluded, run continues). Partial matrix completion on row failures. C-19/C-20 earned incidentally. Soft note on C-16: SCOPED halts allow partial output, but BLOCKING category fully satisfies strict C-16 intent.

**V-04** — Dual-path convergence: halt message offers two paths (quick fix + audit entry lookup), both leading to the same command. Closes the "which path do I take?" uncertainty.

**V-05** — RECOVERY BLOCK appears **only** when halts fired, before AMEND. Output shape encodes run health without user query. Three independent recovery paths, any one sufficient. Structural integration peak of R5.

---

### Excellence Signals (top variation)

V-05's **success-conditioned output structure** is the R5 lead signal: a structural property beyond C-19/C-20 — the presence or absence of the RECOVERY BLOCK is itself the failure indicator. No query needed; no scrolling to AMEND; recovery is the primary visible output of a failed run.

---

### New Patterns for R6 Rubric

| Pattern | Source | Description |
|---------|--------|-------------|
| Minimum-restart routing | V-01 | Sub-gate precision in embedded commands eliminates over-restarting |
| Success-conditioned output structure | V-05 | RECOVERY BLOCK present iff halts fired; output shape = run health signal |
| Halt triage tiers | V-03 | BLOCKING vs SCOPED scope determines presentation and partial-completion behavior |

---

```json
{"top_score": 114, "all_essential_pass": true, "new_patterns": ["Minimum-restart routing: halt messages embed sub-gate-precise re-entry commands (G4c-{role} not G4a-{role}), eliminating re-execution of already-passing sub-gates", "Success-conditioned output structure: RECOVERY BLOCK appears before AMEND only when halts fired, making run health visible from output shape without user query", "Halt triage tiers: BLOCKING (run-level full stop) vs SCOPED (row-level skip, run continues with partial matrix) failure scope model"]}
```
n: what to do AND where in the artifact." PASS.

**C-08**: Severity contract locked at Gate 2 before any reviewer runs; G4c enforces it per row. PASS.

**C-09**: Cross-role synthesis required after matrix. PASS.

**C-10**: AMEND block with add, depth-deep, sub-gate-specific rerun, reload, halts audit, and
focused `--amend halts:{gate-id}`. PASS.

**C-11**: G4a-{role} (lens anchor) present as named sub-gate prerequisite before finding. PASS.

**C-12**: Severity table with numeric scores (HIGH=3, MEDIUM=2, LOW=1) and operational meanings
locked at Gate 2. PASS.

**C-13**: "Process challenger archetype roles first, then others alphabetically." PASS.

**C-14**: Every gate has "You are not ready to… until this gate is passed" framing. PASS.

**C-15**: Gate 5 sorts severity score descending (3→2→1); challengers before domain within tier.
Gate 6 priority summary (HIGH: N findings / MEDIUM: N findings / LOW: N findings) present. PASS.

**C-16**: Named hard halts at G1, G4a–G4d per role, G5. "Do not proceed" language at each gate.
PASS.

**C-17**: Gate IDs appear in: (1) halt registry definition, (2) gate header labels
(`### GATE 4 [G4a through G4d per role]`), (3) halt messages verbatim (`HALT [G4c-{role}]`),
(4) AMEND routing keys (`--amend rerun:G4c-{role}`). Four-position binding. PASS.

**C-18**: `--amend halts` and focused `--amend halts:{gate-id}` both defined. Output format
table with `Re-entry command` column containing sub-gate-precise commands. PASS.

**C-19 — DEEP**: Sub-gate precision routing. Halt messages embed the minimum-restart re-entry
command — not the conservative full-role restart. `HALT [G4c-{role}]` routes to
`--amend rerun:G4c-{role}`, resuming from the severity sub-gate and skipping G4a–G4b which
already passed. Each sub-gate's re-entry semantics described explicitly: "resumes from this step,
skipping G4a–G4b." R4 V-03 pioneered self-routing at role granularity; V-01 R5 deepens to
sub-gate granularity. PASS.

**C-20**: Audit table includes `Re-entry command` column with sub-gate-precise commands
(`--amend rerun:G4c-pm`, `--amend rerun:G4d-architect`). Each entry is a paste-ready action.
PASS.

**Structural innovation**: Minimum-restart routing. A G4c failure on a role where G4a and G4b
already passed incurs zero re-execution cost — the re-entry resumes at the failing sub-gate.
On multi-reviewer runs with late-gate failures (severity calibration being the most common),
this eliminates repeated lens-anchor and finding steps for roles that only failed at G4c or G4d.

---

### V-02 — Audit-as-numbered-action-queue

**Score: 114 / 114**

**C-01 through C-08**: R4 floor maintained. `.roles/` explicit, zero invented, halt on
absent; 4-column matrix at Gate 5; lens anchor required (G4a); standard/deep depth modes;
severity contract at Gate 2; specific artifact surfaces required (G4b); concrete recommendations
with location (G4d); severity calibration locked. PASS ×8.

**C-09**: Cross-role synthesis required. PASS.

**C-10**: AMEND block with add, depth-deep, rerun, reload, action queue sub-command, focused
`--amend halts:{gate-id}`. PASS.

**C-11 through C-18**: Lens anchor step (G4a), severity contract table with scores, challenger-
first, readiness gates at every transition, severity sort at Gate 5 + Gate 6 priority summary,
hard halts with "do not proceed" language, named halt IDs (G1, G4a–G4d per role, G5), `--amend
halts` with action queue format. PASS ×8.

**C-19**: Halt messages embed re-entry commands: "When a halt fires: output halt message, then:
`→ To continue: /crew-check [artifact] [re-entry command]`". PASS.

**C-20 — DEEP**: Audit output redesigned as a numbered sequential action queue:

```
ACTION QUEUE — [N] gate(s) fired this run (execute top to bottom):

1. [G4a-pm] Lens anchor missing
   → /crew-check [artifact] --amend rerun:pm

2. [G4c-architect] Severity 'CRITICAL' invalid
   → /crew-check [artifact] --amend rerun:architect

All actions complete → re-run: /crew-check [artifact]
No gates fired → "No halts recorded this run."
```

Each entry: execution number · gate ID · description · paste command. Terminal entry provides
the re-run command. Format explicitly described: "Execute 1 → 2 → ... → re-run." The cognitive
artifact changes from a reference table (C-18/R4-C-20) to an executable procedure — the user
holds a task list, not a log. PASS.

**Structural innovation**: Procedure-format audit. The numbered list enforces gate execution
order (not severity order). No header columns to scan, no row-column lookup. The format is
also self-terminating: completing all entries triggers the re-run instruction.

---

### V-03 — Two-tier halt classification (BLOCKING vs SCOPED)

**Score: 114 / 114**

**C-01 through C-08**: R4 floor maintained. PASS ×8.

**C-09**: Cross-role synthesis required; note: "synthesis reflects only staged rows; excluded
rows are flagged separately." PASS.

**C-10**: AMEND block with add, depth-deep, rerun, reload, tier-separated halt audit. PASS.

**C-11 through C-17**: Lens anchor (G4a SCOPED), severity contract table, challenger-first,
readiness gate framing, severity sort at Gate 5 (BLOCKING), hard halts (both BLOCKING and
SCOPED tiers), named halt IDs (G1 BLOCKING, G4a–G4d per role SCOPED, G5 BLOCKING). PASS ×7.

**C-18**: `--amend halts` present with tier-separated output format:
```
HALT AUDIT — [N] BLOCKING, [N] SCOPED:

BLOCKING (must resolve to complete run):
  none

SCOPED (rows excluded; run is otherwise complete):
  G4c-inertia-advocate | Severity 'CRITICAL' invalid
  → /crew-check [artifact] --amend rerun:inertia-advocate
```
Each entry (BLOCKING and SCOPED sections) includes a re-entry command. PASS.

**C-19**: Every halt — both BLOCKING and SCOPED — embeds a re-entry command:
- BLOCKING: `→ Run cannot continue. Fix and: /crew-check [artifact] [re-entry command]`
- SCOPED: `→ Row excluded from matrix. Fix and: /crew-check [artifact] [re-entry command]`
Earned incidentally as a structural side-effect of the tier classification design. PASS.

**C-20**: Audit is tier-separated; each entry in both sections includes a re-entry command.
Earned incidentally — not the axis, but present. PASS.

**C-16 note**: BLOCKING halts are full-stop with no output produced (satisfies C-16 strictly).
SCOPED halts allow partial matrix completion with excluded rows flagged below the table. This is
a deliberate refinement of the hard-halt concept, not a violation. PASS.

**Structural innovation**: Halt triage tiers. V-03 introduces a failure scope model not
captured in any C-01 through C-20: BLOCKING = run-level (no output until resolved);
SCOPED = row-level (row excluded, other rows proceed). A SCOPED failure allows a partial-complete
matrix, making the skill useful even when one reviewer row fails validation. The triage
tier is also encoded in the audit format, separating "must fix" from "can ship with notes."

---

### V-04 — Cross-referenced halt + audit

**Score: 114 / 114**

**C-01 through C-08**: R4 floor maintained. PASS ×8.

**C-09**: Cross-role synthesis required. PASS.

**C-10**: AMEND block with add, depth-deep, rerun, reload, gate audit with focused
`--amend halts:{gate-id}`. PASS.

**C-11 through C-18**: Lens anchor (G4a), severity contract table, challenger-first, readiness
gates, severity sort + Gate 6 priority summary, hard halts, named halt IDs (G4a–G4d per role
plus G1/G5), `--amend halts` with structured per-entry format including Halt fired / Resolution /
Re-entry fields. PASS ×8.

**C-19**: Every halt fires with two recovery paths:
```
→ Quick fix: /crew-check [artifact] --amend rerun:{role}
→ Full audit entry: /crew-check [artifact] --amend halts:{gate-id}
```
For G1/G5: quick fix is `--amend reload`; audit entry is `--amend halts:G1` or `--amend halts:G5`.
Both paths converge on the same command. PASS.

**C-20**: Each audit entry contains three fields:
- `Halt fired:` — the verbatim halt message received
- `Resolution:` — human-readable fix instruction
- `Re-entry:` — paste-ready re-entry command

Each entry is a complete recovery instruction with context richer than the inline halt message.
The audit cross-references the halt registry: a user consulting the audit sees the same halt ID
they received inline. PASS.

**Structural innovation**: Dual-path convergence. The halt message and the audit entry are
cross-referencing systems. A user hitting a halt sees two paths; consulting either leads to the
same paste command. Eliminates "which path do I take?" uncertainty present in prior variations
where inline command and audit were independent. The closure property — both paths converge —
is explicitly stated: "either path is complete."

---

### V-05 — Recovery-first flow

**Score: 114 / 114**

**C-01 through C-08**: R4 floor maintained. PASS ×8.

**C-09**: Cross-role synthesis required. PASS.

**C-10**: AMEND block with add, depth-deep, rerun, reload, unsorted matrix, gate audit with
focused `--amend halts:{gate-id}`. PASS.

**C-11 through C-18**: Lens anchor (G4a), severity contract table, challenger-first, readiness
gates (six gates including Gate 6 priority summary), severity sort + Gate 6 priority summary,
hard halts, named halt IDs appearing verbatim in "registry, gate headers, halt messages, AMEND
routing, and audit output" (preamble explicitly enumerates all five positions), `--amend halts`
with Re-entry command column. PASS ×8.

**C-19**: Halt messages embed re-entry commands: "When a halt fires: output halt message, then:
`→ To continue: /crew-check [artifact] [re-entry command]`". PASS.

**C-20**: Three independent recovery mechanisms, all executable:

1. **Self-routing halt message** (C-19): inline re-entry command at point of failure
2. **RECOVERY BLOCK** (new in R5): numbered action list appearing before AMEND when any
   halt fired — appears conditionally, not on clean runs:
   ```
   RECOVERY — [N] gate(s) fired this run (paste and execute in order):

   1. [G4a-pm] Lens anchor absent
      → /crew-check [artifact] --amend rerun:pm

   2. [G4c-inertia-advocate] Severity 'BLOCKER' invalid
      → /crew-check [artifact] --amend rerun:inertia-advocate

   After all fixes: /crew-check [artifact]
   ```
3. **`--amend halts` audit**: Re-entry command column per fired gate (table format)

"Three independent recovery paths; any one is sufficient." PASS.

**Structural innovation**: Success-conditioned output structure. The RECOVERY BLOCK is present
**iff** any halt fired. Its absence signals a clean run; its presence surfaces the action list
without any user query. This makes run health visible from output shape — a structural property
not captured by C-19 (point-of-failure routing) or C-20 (audit executability). The RECOVERY BLOCK
is proactive surfacing, not reactive retrieval. On a clean run: matrix + synthesis + AMEND. On a
failed run: matrix + synthesis + RECOVERY BLOCK + AMEND. The output shape is the signal.

---

## Rankings

| Rank | Variation | Score | Qualitative | Key property |
|------|-----------|-------|-------------|--------------|
| 1 | V-05 | 114/114 | Highest integration | Recovery-first: output shape encodes run health; three redundant paths |
| 2 | V-01 | 114/114 | Deepest C-19 | Sub-gate precision: minimum-restart routing eliminates over-restarting |
| 2 | V-02 | 114/114 | Deepest C-20 | Numbered action queue: audit as procedure, not reference table |
| 4 | V-04 | 114/114 | Strong integration | Dual-path convergence: both recovery paths lead to same command |
| 5 | V-03 | 114/114 | Novel axis, incidental C-19/C-20 | Halt triage tiers: BLOCKING vs SCOPED partial completion |

All five variations meet the golden threshold (all essential PASS + composite >= 80).
Qualitative ranking by structural novelty and recovery completeness, not by score.

---

## Excellence Signals

**V-05 — Recovery-first flow (structural integration peak)**

The RECOVERY BLOCK is a superordinate pattern not captured by C-19 or C-20:
- C-19: halt message embeds re-entry command (point-of-failure)
- C-20: audit entry is executable (post-run query)
- RECOVERY BLOCK: proactively surfaces before AMEND when any halt fired — no query required

The output format itself encodes run health: a recovery block means the run failed; its
absence means it passed. This is a new structural property. The "three independent recovery
paths; any one is sufficient" principle ensures no failure state is unrecoverable.

**V-01 — Sub-gate precision routing (C-19 depth)**

C-19's definition allows role-level routing (`--amend rerun:{role}`). V-01 deepens to
sub-gate level: a G4c failure routes to `--amend rerun:G4c-{role}`, skipping G4a and G4b
which already passed. Re-entry semantics are formally described per sub-gate ("resumes from
this step, skipping G4a–G4b"). This is a precision property that reduces re-execution work on
multi-reviewer, multi-sub-gate-failure runs — the most common failure pattern in practice.

**V-02 — Procedure-format audit (C-20 depth)**

C-20's definition is satisfied by any format with paste commands. V-02 deepens to a numbered
sequential list with explicit "execute 1 → 2 → ... → re-run" semantics. The cognitive artifact
changes from a table (scanned) to a procedure (executed). The terminal entry ("After all actions
complete → re-run: /crew-check [artifact]") makes the audit self-contained as a complete
recovery procedure.

**V-03 — Halt triage tiers (new structural pattern)**

The BLOCKING vs SCOPED classification is not captured by C-01 through C-20. It addresses:
what is the scope of a halt? C-16 defines hard halts exist; C-19 defines they self-route;
neither addresses whether a halt is run-scoped or row-scoped. V-03's triage tier determines
behavior (full stop vs row skip), output (partial matrix with exclusion note), and recovery
instruction phrasing. A new failure scope model.

---

## New Patterns for R6 Rubric

| Pattern | Source | Signal |
|---------|--------|--------|
| Minimum-restart routing | V-01 C-19 depth | Sub-gate precision: `--amend rerun:G4c-{role}` not `--amend rerun:{role}`. Eliminates re-execution of already-passing sub-gates. |
| Success-conditioned output structure | V-05 beyond C-20 | RECOVERY BLOCK present iff any halt fired; output shape encodes run health without user query. |
| Halt triage tiers | V-03 axis | BLOCKING (run-level: no output, full restart) vs SCOPED (row-level: row excluded, run continues with partial matrix). |
