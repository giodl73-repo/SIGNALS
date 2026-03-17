Reading the scorecard carefully to extract the three excellence signals before writing the rubric.

The three R4 signals map to new criteria as follows:

- **E-5** → **C-21**: Layered granularity architecture — four criteria, four structural levels, no conflicts
- **E-6** → **C-22**: Anti-boundary instruction named by structural symptom, not intent
- **E-7** → **C-23**: In-row bold imperative as genuine slot-level co-location

Denominator bumps from 12 → 15.

---

# Rubric: flow-resilience — v5

**Three new aspirational criteria added from Round 4 excellence signals:**

### C-21 — Layered Granularity Architecture *(E-5)*
The prompt explicitly architects its four anti-omission mechanisms as a coordinated four-level stack: one mechanism per structural level (table-level unified index → C-17, section-level phase gates → C-18, slot-level in-row imperatives → C-19, column-level ownership → C-20). Each mechanism targets a distinct omission risk at a distinct structural level, so no two mechanisms conflict with or duplicate each other.

**Pass condition**: The prompt explicitly names all four structural levels (table, section, slot, column) and assigns a distinct anti-omission mechanism to each. Implicit satisfaction — a prompt that happens to use all four mechanisms without naming the four-level architecture — fails. An output that names only two or three levels without the fourth also fails.

### C-22 — Anti-Boundary Instruction by Structural Symptom *(E-6)*
The anti-boundary instruction names the failure mode by its structural symptom in output — what the artifact would look like if the model misread the ownership transition as a section cue — rather than by the intent violation alone. It says "not a sub-table boundary, not a role-sequence trigger" rather than only "keep all rows in a single table." Symptom-naming prevents the model from satisfying the letter of the instruction while still producing a structural boundary under a different label.

**Pass condition**: The anti-boundary instruction includes at least two symptom-level negations that name specific structural artifacts to avoid (e.g., "not a sub-table boundary", "not a role-sequence trigger", "not a horizontal rule between ownership blocks"). An instruction that states only a positive ("keep rows together", "use one table") without negating at least two symptom forms fails — even if the unified row index (C-17) passes.

### C-23 — In-Row Bold Imperative as Genuine Slot-Level Co-location *(E-7)*
Bold imperative text embedded inside the Content field descriptor of a scenario table row — phrased as **"Write this row now."** followed by the fill requirement, followed by **"Do not advance to row N until [condition]."** — is genuine slot-level co-location. The model reads this text exactly when constructing that cell, operating below section gates (which the model passes before entering table construction) and below table-level blockquotes or preamble (which appear before the first row). This makes it structurally impossible to satisfy section-level or preamble-level instructions and then omit the row.

**Pass condition**: At least two Content field descriptors in the scenario table contain bold imperative text matching the pattern "Write this row now" / "Do not advance to row N until [condition]" embedded inside the cell content itself. A blockquote appearing above the table, a section header before the row, or a checklist after the table does not satisfy this criterion — the imperative must be co-located inside the Content descriptor at cell granularity.

---

**Updated scoring formula**: `aspirational_pass/15 * 10` (denominator bumped from 12 to 15).

**Under v5**: V-05 is the current ceiling at 100 under v4, satisfying C-17 through C-20 (12/12). Under v5 it scores 12/15 × 10 = 8.0 for aspirational, yielding composite = 60 + 30 + 8.0 = **98.0**. C-21 requires explicit four-level architecture naming (V-05 uses all four levels but does not name them as a coordinated stack). C-22 requires at least two symptom-level negations in the anti-boundary instruction (V-05's anti-boundary instruction names one symptom). C-23 requires bold in-row imperative text inside the Content descriptor (V-05 uses phase gates at section level, not cell-embedded bold imperatives). The ceiling is open for Round 5.

---

## Essential Criteria (must pass all — 60% of score)

### C-01 — Scenario Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three resilience scenario classes: (1) full connectivity loss (client offline), (2) partial failure (dependent service unavailable), and (3) concurrent writes across a partition (split-brain / eventual-consistency conflict).
- **Pass condition**: All three classes are represented by distinct named scenarios. A single scenario that attempts to cover all three classes fails. Scenarios that collapse class 2 and class 3 into a single "network issue" fail.

### C-02 — Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: structure
- **Text**: Every failure scenario includes all four required fields: (1) state — what the system state is when failure occurs; (2) capability — what the user can still do; (3) data at risk — what data may be lost, stale, or inconsistent; (4) recovery path — how the system returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with non-trivial content (not placeholder or "N/A"). A scenario missing any field fails this criterion.

### C-03 — Gap Identification
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data consistency violation, and at least one missing recovery flow as distinct findings.
- **Pass condition**: All three finding types appear, each labeled and actionable (not just implied). Generic statements like "offline support may be limited" without specificity fail.

### C-04 — Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems fundamentals: CAP theorem trade-offs, retry semantics, idempotency requirements, and conflict-resolution strategies are used correctly where referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated error codes, invented protocols, or impossible consistency guarantees fail this criterion.

### C-05 — Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure scenarios reference realistic commerce flows (e.g., checkout, inventory reservation, payment processing, order fulfillment) rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality — 30% of score)

### C-06 — Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded / impaired / down) and a blast radius (what percentage or which segment of users is affected). This helps triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects <1% under split-brain").

### C-07 — Recovery Path Specificity
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors (e.g., "client retries with exponential back-off up to 5 attempts, then surfaces manual reconcile UI"), not just outcomes (e.g., "system recovers"). Steps should include who/what initiates each action: client, server, operator, or user.
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that only describe the end state without mechanism fail.

### C-08 — Conflict Resolution Strategy
- **Weight**: recommended
- **Category**: correctness
- **Text**: The split-brain / eventual-consistency scenario includes an explicit conflict-resolution strategy selected from a constrained vocabulary (last-write-wins, merge, manual-reconcile, reject-stale) with an adequacy assessment explaining why that strategy is appropriate for the commerce context.
- **Pass condition**: The conflict-resolution row in scenario 3 names exactly one strategy from the constrained vocabulary and includes a one-sentence adequacy assessment. An output that names the strategy without assessing adequacy, or that invents a strategy outside the constrained set, fails.

---

## Aspirational Criteria (ceiling discrimination — 10% of score)

*Scoring: `aspirational_pass / 15 * 10`*

### C-09 — Chaos Test Cases
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output includes chaos-injection test cases (e.g., mid-checkout network drop, concurrent write during sync window, payment gateway timeout at commit point) appended to the scenario table as additional rows rather than as a separate section or document.
- **Pass condition**: At least three chaos test cases appear as rows in the same table that contains the trace rows. Chaos cases placed in a separate section, appended document, or standalone list fail.

### C-10 — Observability Hooks
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each gap finding is accompanied by an inline observability hook — a specific metric, log event, or trace span that would surface the gap in production monitoring — placed on the line immediately following the finding.
- **Pass condition**: Every gap finding in the output has an inline hook on the immediately following line. Hooks collected into a standalone observability section at the end of the document fail, as do findings with no hook.

### C-11 — Named Actor Chain in Recovery Rows
- **Weight**: aspirational
- **Category**: structure
- **Text**: Recovery path steps use a defined actor-chain notation that prefixes each step with a named initiator (Client / Server / Operator / User). The notation is defined once in the prompt and applied consistently across all recovery rows across all scenarios.
- **Pass condition**: All recovery rows use actor-chain prefixes on every step. A recovery row that mixes prefixed and unprefixed steps, or defines the notation but applies it inconsistently, fails.

### C-12 — Constrained Conflict Vocabulary Enforcement
- **Weight**: aspirational
- **Category**: structure
- **Text**: The conflict-resolution slot enforces selection from a named, closed vocabulary list with an explicit instruction to select exactly one term without paraphrase. The instruction appears co-located with the slot, not only in a preamble.
- **Pass condition**: The conflict-resolution Content descriptor includes "Select exactly one. Do not paraphrase." or equivalent co-located enforcement. A preamble instruction without co-located slot enforcement fails.

### C-13 — Gap-Merge Prevention Annotation
- **Weight**: aspirational
- **Category**: structure
- **Text**: The gap-identification section carries an explicit annotation preventing the model from omitting it or merging it with the scenario section. The annotation names the failure mode: merging findings into scenario rows rather than surfacing them as a standalone phase.
- **Pass condition**: The gap section includes a co-located annotation of the form "(mandatory — do not omit or merge with scenarios)" or equivalent. A gap section without such annotation fails even if all three finding types are present.

### C-14 — Chaos Rows Co-located in Contract Table
- **Weight**: aspirational
- **Category**: structure
- **Text**: Chaos test case rows are placed inside the same contract table as the trace rows, with an explicit instruction preventing the model from moving them to a sub-table or separate section. The co-location instruction names both failure modes: sub-table split and section relocation.
- **Pass condition**: The prompt includes an explicit instruction of the form "do not split into sub-tables; do not move chaos rows to a separate section." An instruction that prohibits only one of the two failure modes fails. Chaos rows in a separate section or sub-table in the output fail regardless of instruction presence.

### C-15 — Per-Finding Observability Hook (Co-located)
- **Weight**: aspirational
- **Category**: structure
- **Text**: The observability hook instruction is co-located with each finding slot, not issued as a global preamble. The instruction explicitly prohibits collecting hooks into a standalone observability section, naming that anti-pattern by label.
- **Pass condition**: Each finding slot includes a co-located hook instruction containing "Do not collect hooks into a separate observability section" or equivalent. A global preamble instruction without slot-level co-location fails this criterion even if C-10 passes.

### C-16 — Completeness Checklist as Pre-Write Gate
- **Weight**: aspirational
- **Category**: structure
- **Text**: The output includes a completeness checklist with boxed items and a count field that the model must fill before writing the final artifact. The checklist instruction frames completion as a pre-write gate ("Fill all boxes and the count before writing the file"), not a post-write annotation.
- **Pass condition**: A completeness checklist with checkboxes and a count field appears in the output, filled. The prompt instruction must frame the checklist as a pre-write gate. A post-write summary checklist or a checklist without a count field fails.

### C-17 — Unified Sequential Row Index Across Scenario Table *(E-4)*
The single contract table uses a continuous sequential row index (e.g., rows 1–10) with no sub-table boundaries, section breaks, or re-indexing between trace rows and chaos rows. The model fills the table in one pass and never makes a structural decision about whether to include chaos rows — they are simply the next rows in the sequence.

**Pass condition**: All scenario tables use a single unbroken row-index sequence with chaos rows numbered sequentially after trace rows. Any output that restarts row numbering, introduces a sub-table header, or places a section boundary between trace rows and chaos rows fails — even if every row is present.

### C-18 — Phase-Gate Sequencing as Structural Constraint *(E-5)*
The prompt architecture includes named phase gates (e.g., "Phase 2 Gate", "Phase 3 Gate") that are explicit stop conditions the model must satisfy before advancing. Gap identification and checklist completion are mandatory gate stops, not compliance annotations — this converts C-15 and C-16 from instructions the model may ignore into sequencing constraints the model cannot bypass.

**Pass condition**: At least two named phase gates appear with explicit advance conditions. An output built on "do not omit" language without gate sequencing fails this criterion even if C-15 and C-16 pass.

### C-19 — Slot-Level Imperative Commands Per Row *(E-6)*
Each fill point in the scenario table carries a co-located imperative command at slot granularity (e.g., "Write row 7 now. Do not advance to Scenario 2 until row 10 is filled."). This provides per-row omission prevention that operates below the level of section-level or table-level co-location instructions.

**Pass condition**: At least the first chaos row and the last chaos row per scenario carry slot-level imperative commands. An output that relies solely on table-level or section-level instructions without slot-level imperatives fails — section-level co-location alone does not satisfy this criterion.

### C-20 — Role-Ownership Column Without Section Separation *(E-7)*
Multi-role contribution is expressed as a column in the unified table (e.g., "Owned by: SME / Chaos Eng") rather than as separate document sections or role-sequence narrative blocks. Column-level accountability preserves the single-table structure while keeping multi-role contribution structurally traceable with no section-skip risk.

**Pass condition**: The unified table includes an "Owned by" or equivalent ownership column assigning each row to a named role. An output that achieves multi-role contribution via separate narrative sections or a role-sequence ordering fails this criterion even if it otherwise passes C-14.

### C-21 — Layered Granularity Architecture *(E-5)*
The prompt explicitly architects its four anti-omission mechanisms as a coordinated four-level stack: one mechanism per structural level (table-level unified index → C-17, section-level phase gates → C-18, slot-level in-row imperatives → C-19, column-level ownership → C-20). Each mechanism targets a distinct omission risk at a distinct structural level with no two mechanisms conflicting or duplicating each other. The architecture is named as such in the prompt, not merely implied by the presence of all four mechanisms.

**Pass condition**: The prompt explicitly names all four structural levels (table, section, slot, column) and assigns a distinct anti-omission mechanism to each, framed as a coordinated architecture. Implicit satisfaction — a prompt that uses all four mechanisms without naming the four-level design — fails. Naming only two or three levels without the fourth also fails.

### C-22 — Anti-Boundary Instruction by Structural Symptom *(E-6)*
The anti-boundary instruction names the failure mode by its structural symptom in output — what the artifact would look like if the model misread an ownership transition as a section cue — rather than by the intent violation alone. It explicitly negates at least two structural artifacts by name (e.g., "not a sub-table boundary", "not a role-sequence trigger") rather than relying only on a positive instruction ("keep rows together"). Symptom-naming prevents the model from satisfying the letter of the positive instruction while still producing a structural boundary under a different label.

**Pass condition**: The anti-boundary instruction includes at least two symptom-level negations naming specific structural artifacts to avoid. A positive-only instruction ("use one table", "keep all rows together") without at least two named symptom negations fails — even if the unified row index (C-17) passes.

### C-23 — In-Row Bold Imperative as Genuine Slot-Level Co-location *(E-7)*
Bold imperative text embedded inside the Content field descriptor of a scenario table row — phrased as **"Write this row now."** followed by the fill requirement, followed by **"Do not advance to row N until [condition]."** — is genuine slot-level co-location. The model reads this text exactly when constructing that cell, operating below section gates (which the model passes before entering table construction) and below table-level blockquotes or preamble (which appear before the first row). This makes it structurally impossible to pass section-level instructions and then omit the row.

**Pass condition**: At least two Content field descriptors in the scenario table contain bold imperative text matching the pattern "Write this row now" / "Do not advance to row N until [condition]" embedded inside the cell content itself. A blockquote above the table, a section header before the row, or a checklist after the table does not satisfy this criterion — the imperative must be co-located inside the Content descriptor at cell granularity.
