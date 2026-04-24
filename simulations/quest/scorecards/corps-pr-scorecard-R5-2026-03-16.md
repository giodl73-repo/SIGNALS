## Quest Score — corps-pr R5

### Rubric Reference

**Essential (5 criteria, 60 pts):** C-01 routing, C-02 role orientation, C-03 consensus synthesis, C-04 single decision, C-05 domain-lens validity check
**Recommended (3 criteria, 30 pts):** C-06 coverage gap, C-07 per-role severity summary, C-08 AMEND block
**Aspirational (10 criteria, 10 pts):** C-09 root cause, C-10 sign-off roles, C-11 IA sequenced first, C-12 architectural mechanism, C-13 ban list ≥3, C-14 IA anchor per role, C-15 rewrite gate, C-16 AMEND schema, C-17 IA cost terms, C-18 phase gates

---

## V-01 — Inertia Framing: IA Cost Ledger

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Routing table with `org.yaml Scope Pattern` column; every file gets a row; coverage gap rule present |
| C-02 | **PASS** | Each role section has `Source files` and `Orientation: [one phrase from .roles/]` |
| C-03 | **PASS** | Consensus template includes `Critical: [F-XX from role] — [one sentence on why this finding most threatens the merge]` |
| C-04 | **PASS** | "Exactly one decision. Values: GO, NO-GO, GO WITH CONDITIONS only. Delegated decisions fail. Hedged decisions fail." |
| C-05 | **PASS** | Explicit domain-lens gate: Step A binary test + Step B rewrite consequence per finding; "gate tests domain fidelity, not specificity" |

Essential: **5/5**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | "`COVERAGE GAP: [file] — no org.yaml scope pattern covers this path.`" |
| C-07 | **PASS** | `Summary: [N] findings — [x] P1, [y] P2, [z] P3` at end of every role section template |
| C-08 | **PASS** | AMEND block with five named mandatory fields |

Recommended: **3/3**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Consensus template: `Mechanism: [the specific code or architectural property causing the rating difference — names a structural fact in the code, not a perspective difference]` |
| C-10 | **PASS** | `1. [what must be resolved] — sign-off: [role who confirms resolution before merge]` |
| C-11 | **PASS** | "The IA section appears before all technical role sections. This is structural and non-configurable." |
| C-12 | **PASS** | Mechanism line instructions: "names a structural fact in the code, not a perspective difference" |
| C-13 | **PASS** | 5 enumerated banned phrases in checklist form with checkboxes — independently checkable per phrase |
| C-14 | **PASS** | Each role section has `IA cost anchor` block with `Cost category disputed` and `confirms / disputes … because [code surface]` |
| C-15 | **PASS** | Step A (binary test) + Step B (rewrite consequence) with explicit drop path for persistent failures |
| C-16 | **PASS** | AMEND block uses named-field schema: "What was amended:", "Roles added:", "Roles removed:", etc. |
| C-17 | **PASS** | 4-row × 2-column cost ledger: each row (Maintenance / Incident exposure / Integration cost / Regression risk) has both Current-State Cost and Adoption Cost columns; `Budget verdict` and `Budget strength` required |
| C-18 | **FAIL** | No top-level pipeline declaration. Domain-lens gate is a per-finding inline instruction ("DOMAIN-LENS GATE (execute per finding)"), not a named phase exit condition. No unified declaration of phases with entry/exit conditions and criteria gated. |

Aspirational: **9/10**

### Score

```
essential:    5/5 × 60 = 60
recommended:  3/3 × 30 = 30
aspirational: 9/10 × 10 =  9
─────────────────────────────
composite:                99
```

**Golden: YES** (all essential pass, composite 99 ≥ 80)

---

## V-02 — Lifecycle Emphasis: Top-Level Pipeline Declaration

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase A routing table with `org.yaml Scope Pattern` column; Phase A exit condition names every-file-has-a-row |
| C-02 | **PASS** | Phase C role template: `Source files` + `Orientation: [one phrase from .roles/]` |
| C-03 | **PASS** | Phase D consensus: `Agreement`, `Divergence`, `Critical` required elements |
| C-04 | **PASS** | Phase E: "One decision only. Values: GO, NO-GO, GO WITH CONDITIONS. Delegated decisions fail. Hedged decisions fail." |
| C-05 | **PASS** | Phase C domain-lens gate: binary test + rewrite consequence; "The gate tests domain fidelity, not specificity" |

Essential: **5/5**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Coverage gap appended immediately after routing table |
| C-07 | **PASS** | Per-role summary line in Phase C template |
| C-08 | **PASS** | AMEND block with named fields before Phase A |

Recommended: **3/3**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Phase D `Mechanism:` line requires structural/architectural code property; ban-to-fix table enforces it |
| C-10 | **PASS** | GO WITH CONDITIONS conditions include `sign-off: [role who confirms before merge]` |
| C-11 | **PASS** | Phase B (IA) declared before Phase C (technical roles) in pipeline declaration; entry condition for Phase C is "Phase B exit met; roles read Phase B before writing" |
| C-12 | **PASS** | Mechanism line: "structural or architectural property of the code causing the difference — names a fact in the code, not a perspective difference" |
| C-13 | **PASS** | Phase D ban-to-fix table: 5 rows, each with banned phrase + required replacement form; "Each row is independently checkable" |
| C-14 | **PASS** | Phase C role template: `IA cost anchor` block cites Phase B budget strength and cost term; `This role [confirms / disputes] that cost estimate because: [names code surface]` |
| C-15 | **PASS** | Phase C exit condition in pipeline declaration: "every finding in every section has passed the domain-lens gate (Step A binary test + Step B rewrite consequence); no finding advances to Phase D without passing it" |
| C-16 | **PASS** | AMEND block: five named fields in structured block format, each mandatory |
| C-17 | **PASS** | Phase B cost terms: 4 required fields — Maintenance cost (current approach), Incident exposure (current failure risk), Adoption cost (this PR), Regression risk (new failure risk vs current). Phase B exit condition: "all 4 cost terms filled"; "A Phase B section that lists concerns without filling cost terms fails its exit condition" |
| C-18 | **PASS** | Top-level PIPELINE DECLARATION table with 5 named phases (A–E), entry condition, exit condition, and criteria gated per phase. Phase C exit condition explicitly includes domain-lens gate. "The pipeline declaration below is the execution contract. Read it before producing any output. Each phase may not begin until its stated entry condition is satisfied." |

Aspirational: **10/10**

### Score

```
essential:    5/5 × 60 = 60
recommended:  3/3 × 30 = 30
aspirational: 10/10 × 10 = 10
──────────────────────────────
composite:                100
```

**Golden: YES** (all essential pass, composite 100 ≥ 80)

---

## V-03 — Role Sequence: Two-Pass Finding Generation

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Step 2 routing table with `org.yaml Pattern` column; every file gets a row |
| C-02 | **PASS** | 4C output template: `Source files` + `Orientation: [one phrase from .roles/]` |
| C-03 | **PASS** | Step 5 consensus: `Agreement`, `Divergence` with Mechanism, `Critical` |
| C-04 | **PASS** | Step 6: "One decision. No delegation. No hedging." |
| C-05 | **PASS** | Step 4B audit test: "Would only [this role] raise this finding, given their domain?" + rewrite path + drop path |

Essential: **5/5**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Coverage gap rule in step 2 |
| C-07 | **PASS** | Per-role summary in 4C output template |
| C-08 | **PASS** | Step 7 AMEND block with all named fields mandatory |

Recommended: **3/3**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Consensus `Mechanism:` line requires structural/architectural property |
| C-10 | **PASS** | GO WITH CONDITIONS sign-off: `sign-off: [role]` |
| C-11 | **PASS** | "The IA section appears before all technical role sections" (step 3 before step 4) |
| C-12 | **PASS** | Mechanism requires naming structural code property |
| C-13 | **PASS** | Ban-to-fix table in step 5: 5 rows with banned phrases + required replacements |
| C-14 | **PASS** | Each role in 4A has IA cost anchor block; 4C output includes revised IA cost anchor |
| C-15 | **PASS** | 4B audit test (binary) + rewrite path + drop; "The audit log is the Phase C exit gate — it must be complete before synthesis" |
| C-16 | **PASS** | Step 7 AMEND: all named fields, "Every field is mandatory" |
| C-17 | **PASS** | Step 3 IA cost terms: `Current-state cost: [maintenance burden + incident exposure]` and `Adoption cost: [integration overhead + regression risk of this PR]` — two-line cost tradeoff; `Budget verdict` required. Framing is present though consolidated vs 4-row ledger. |
| C-18 | **FAIL** | No top-level pipeline declaration with named phases, entry conditions, exit conditions, and criteria gated. Step 4B labels its audit log as "the Phase C exit gate" but Routing, IA, Synthesis, and Decision phases have no equivalent named exit conditions. The gate structure is partial — one phase exit named, four phases without declared entry/exit. |

Aspirational: **9/10**

### Score

```
essential:    5/5 × 60 = 60
recommended:  3/3 × 30 = 30
aspirational: 9/10 × 10 =  9
─────────────────────────────
composite:                99
```

**Golden: YES** (all essential pass, composite 99 ≥ 80)

---

## V-04 — Combined: IA Cost Ledger + Pipeline Declaration

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase A routing table with `org.yaml Scope Pattern`; Phase A exit names completeness conditions |
| C-02 | **PASS** | Phase C template: `Source files` + `Orientation: [one phrase from .roles/]` |
| C-03 | **PASS** | Phase D consensus: `Agreement`, `Divergence + Mechanism`, `Critical` |
| C-04 | **PASS** | Phase E: "One decision. Delegated decisions fail. Hedged decisions fail." |
| C-05 | **PASS** | Phase C domain-lens gate (binary test + rewrite consequence) declared as Phase C exit condition in both the pipeline table and the Phase C body |

Essential: **5/5**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Coverage gap rule in Phase A |
| C-07 | **PASS** | Per-role summary in Phase C template |
| C-08 | **PASS** | AMEND named-field block before Phase A; all fields mandatory |

Recommended: **3/3**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Phase D Mechanism line requires architectural/structural code property |
| C-10 | **PASS** | GO WITH CONDITIONS conditions include `sign-off: [role who confirms before merge]` |
| C-11 | **PASS** | Phase B (IA) before Phase C (technical) by pipeline structure; "Technical roles read the Phase B cost ledger before writing" |
| C-12 | **PASS** | Mechanism line explicitly requires "names a structural fact in the code, not a perspective difference" |
| C-13 | **PASS** | Phase D ban-to-fix table: 5 rows; "Each row is independently checkable"; "A Mechanism line containing a banned phrase fails even if a code mechanism is also named" |
| C-14 | **PASS** | Phase C template: `IA cost anchor (required — cite a specific Phase B ledger row)` with `Phase B cost row cited: [Maintenance / Incident exposure / Integration cost / Regression risk]` — enumerated pick-list enforces IA reference |
| C-15 | **PASS** | Phase C exit: "every finding passed Step A of the domain-lens gate"; Phase C exit condition in pipeline table: "every finding passed the domain-lens gate (binary test + rewrite consequence)" |
| C-16 | **PASS** | AMEND block with five named fields in structured format |
| C-17 | **PASS** | Phase B 4-row × 2-column cost ledger (Maintenance / Incident exposure / Integration cost / Regression risk × Current-State Cost / Adoption Cost); "Phase B exit requires filled cost ledger cells — a Phase B section with missing cost cells does not satisfy its exit condition" |
| C-18 | **PASS** | Top-level PIPELINE DECLARATION table: 5 named phases (A–E), entry conditions, exit conditions, criteria gated per phase. Phase B exit explicitly requires cost ledger cells filled. Phase C exit explicitly requires domain-lens gate. Pipeline declared before any execution: "This skill runs as a five-phase pipeline. The pipeline declaration below is the execution contract." |

Aspirational: **10/10**

### Score

```
essential:    5/5 × 60 = 60
recommended:  3/3 × 30 = 30
aspirational: 10/10 × 10 = 10
──────────────────────────────
composite:                100
```

**Golden: YES** (all essential pass, composite 100 ≥ 80)

---

## V-05 — Combined: IA Cost Ledger + Two-Pass Audit + Ban-to-Fix

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Step 2 routing table with `org.yaml Scope Pattern Matched` column; coverage gap block with named fields |
| C-02 | **PASS** | 4C output template: `Source files` + `Orientation: [one phrase from .roles/]` |
| C-03 | **PASS** | Step 5 consensus table with `Agreement`, `Divergence`, `Critical` rows |
| C-04 | **PASS** | Step 6: "One decision value: GO, NO-GO, or GO WITH CONDITIONS. No others. No delegation. No hedging." |
| C-05 | **PASS** | 4B audit test: "Would only [this role] raise this finding, given their domain?" + rewrite + drop path |

Essential: **5/5**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Step 2 coverage gap block: `COVERAGE GAP / File: [path] / Reason: No org.yaml scope pattern matches this path.` |
| C-07 | **PASS** | 4C output template: `Summary: [N] findings — [x] P1, [y] P2, [z] P3` |
| C-08 | **PASS** | Step 7 AMEND block with all named fields mandatory; "Do not convert to prose." |

Recommended: **3/3**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Consensus table `Divergence` row requires `Mechanism / Notes` cell with structural code property |
| C-10 | **PASS** | Step 6: `Sign-off roles: [role(s) who confirm resolution before merge, or "n/a"]` |
| C-11 | **PASS** | Step 3 (IA) before step 4 (two-pass technical findings); "This block appears before all technical role sections and before the two-pass finding generation begins" |
| C-12 | **PASS** | Ban-to-fix table in step 5: replacement forms require naming code mechanism, not role perspective |
| C-13 | **PASS** | Divergence Mechanism ban-to-fix: 5 rows; "Each row is independently checkable"; "A Mechanism cell containing a banned phrase fails even if a code mechanism is also named in the same cell" |
| C-14 | **PASS** | 4A draft pass requires IA cost anchor block per role; 4C output pass includes revised IA cost anchor |
| C-15 | **PASS** | 4B: audit test binary + rewrite + drop; "The audit log is the Phase C exit gate — an incomplete log means Phase C is not finished" |
| C-16 | **PASS** | Step 7 AMEND block: five named fields; "Every field is mandatory; write 'none' if not applicable. Do not convert to prose." |
| C-17 | **PASS** | Step 3 cost ledger: 4-row × 2-column schema with Current-State Cost and Adoption Cost per category; "all rows required — Phase B exit condition" |
| C-18 | **FAIL** | No top-level pipeline declaration table. Step 4B names the audit log as "the Phase C exit gate" and the cost ledger is labeled "Phase B exit condition," but no unified declaration names all 5 phases with entry/exit conditions and criteria gated. The phase-gate structure is referenced inline at two points but is not declared as an auditable pre-execution contract. |

Aspirational: **9/10**

### Score

```
essential:    5/5 × 60 = 60
recommended:  3/3 × 30 = 30
aspirational: 9/10 × 10 =  9
─────────────────────────────
composite:                99
```

**Golden: YES** (all essential pass, composite 99 ≥ 80)

---

## Ranking Summary

| Rank | Variation | Composite | Essential | Recommended | Aspirational | C-18 |
|------|-----------|-----------|-----------|-------------|-------------|------|
| 1 | **V-04** — Combined: Cost Ledger + Pipeline Declaration | **100** | 5/5 | 3/3 | 10/10 | PASS |
| 1 | **V-02** — Lifecycle: Pipeline Declaration | **100** | 5/5 | 3/3 | 10/10 | PASS |
| 3 | V-01 — Inertia: IA Cost Ledger | 99 | 5/5 | 3/3 | 9/10 | FAIL |
| 3 | V-03 — Role Sequence: Two-Pass | 99 | 5/5 | 3/3 | 9/10 | FAIL |
| 3 | V-05 — Combined: Cost Ledger + Two-Pass + Ban-to-Fix | 99 | 5/5 | 3/3 | 9/10 | FAIL |

**The C-18 split is the decisive criterion this round.** V-02 and V-04 both pass by virtue of the top-level pipeline declaration. V-01, V-03, and V-05 have inline gate instructions at individual steps but no unified pre-execution declaration of all phases — the audit trail for phase transitions exists only where it's embedded, not as a declared contract.

**V-04 over V-02 on architectural tightness**: Both score 100, but V-04 is the stronger design. V-04 explicitly couples Phase B to Phase C via the `Phase B cost row cited: [Maintenance / Incident exposure / Integration cost / Regression risk]` enumerated pick-list in every technical role section. V-02's IA cost anchor uses a free-text field ("which Phase B cost row is most relevant"). V-04 creates a structural dependency chain from cost ledger cell → technical role IA anchor → Phase C exit verification.

---

## Excellence Signals (V-04)

**Signal 1 — Pipeline declaration table includes criteria-gated column**
The pipeline declaration table in V-04 maps each phase to the specific rubric criteria it gates (Phase A: C-01, C-06; Phase B: C-11, C-17; Phase C: C-02, C-05, C-07, C-14, C-15, C-18; Phase D: C-03, C-09, C-12, C-13; Phase E: C-04, C-10). A reviewer can locate any criterion by phase, then verify the corresponding exit condition was satisfied. The declaration is self-documenting against the rubric — compliance is auditable in two directions: against the output structure and against the criteria list.

**Signal 2 — Phase C IA anchor cites Phase B ledger row by enumerated pick-list**
V-04's Phase C template requires `Phase B cost row cited: [Maintenance / Incident exposure / Integration cost / Regression risk]` — a pick-from-enum rather than free-text. This creates an auditable chain: the IA fills a cell in Phase B, the technical role names that specific cell in Phase C, and a reviewer can verify the two are consistent without reading prose. It converts C-14's narrative anchor requirement into a structural dependency.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pipeline declaration table includes criteria-gated column making each phase self-documenting against the rubric — compliance auditable by phase and by criterion", "Phase C IA anchor cites Phase B cost ledger row by enumerated pick-list creating auditable cross-phase dependency chain from IA cost cell to technical role position"]}
```
