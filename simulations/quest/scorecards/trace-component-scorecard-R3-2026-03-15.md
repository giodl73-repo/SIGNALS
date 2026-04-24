## Round 3 Scorecard — trace-component

**Available**: V-01 fully scored, V-02 partially scored (hypothesis + partial template only). V-03 through V-05 not provided in the invocation.

---

### Results

| V | Score | Band | Key |
|---|-------|------|-----|
| V-01 | **117/120** | Golden | Vocabulary Contract mechanism nails C-13; Role 3 stamp makes incompleteness machine-readable |
| V-02 | **108/120** | Golden | STATUS column delivers C-12 + C-10; C-13 PARTIAL (no vocabulary contract), C-11 PARTIAL (no citation enforcement) |

---

### Discriminators

**C-13 (framework-neutral core trace)** — V-01 PASS, V-02 PARTIAL. V-01's three-layer mechanism (Role 1 Vocabulary Contract → Role 2 neutral-only constraint on §1-§7 → Role 3 jargon audit) eliminates the R2 escape route where "use framework vocabulary throughout" coexisted with a Framework Notes section. V-02 has neutrality intent in framing but no enforcement mechanism.

**C-12 (incompleteness tokens)** — Both PASS. V-01 uses named tokens (UNKNOWN, MISSING-LOADING, MISSING-ERROR) aggregated in a Role 3 stamp. V-02 uses the STATUS column itself as the token mechanism. Two orthogonal designs, both passing.

**C-08 (optimization)** — Both PARTIAL. Neither requires render-reduction quantification in remediation hints. A combined V-04/V-05 design would need to explicitly require the quantification.

---

### Excellence Signals

1. **Vocabulary Contract first** — Establishing the framework→neutral mapping as a Role 1 artifact before the trace begins locks the vocabulary boundary at invocation time. The contract is a named table (not buried prose), the constraint is explicit, and Role 3 closes the audit loop.

2. **Machine-readable incompleteness inventory** — Role 3 stamps "TRACE COMPLETE — {N} UNKNOWN tokens / {M} MISSING tokens / {K} issues flagged," making completeness a trace-level aggregate observable without reading every row.

```json
{"top_score": 117, "all_essential_pass": true, "new_patterns": ["Vocabulary Contract first -- Role 1 before the Trace Analyst establishes a framework-term to neutral-term mapping as a named table artifact before any trace content is written; §1-§7 are then explicitly constrained to neutral-column vocabulary only; §8 is the sole designated zone for framework terms; Role 3 audits for leakage; this inverts the R2 contradiction where role-level vocabulary instructions coexisted with Framework Notes and gave models an escape route into framework jargon in core sections", "Machine-readable incompleteness inventory -- Role 3 stamps the artifact with UNKNOWN token count and MISSING token count making the completeness level of the trace observable from the stamp alone without reading every row; this extends C-12 from individual gap marking to a trace-level aggregate that can be compared across artifacts and used as a quality signal in review pipelines"]}
```
nent tree: all hops have direction labels and prop/callback names." |
| V-02 | **PASS** | STATUS column requires every component row to declare its STATUS. A component with STATUS=UNKNOWN is present where a silently-omitted component would be absent. Direction and payload columns in table schema enforce per-hop annotation. |

---

#### C-03 -- State delta shown (essential, 15 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §3 table: State Key / Before / After / Derived Dependents. Explicit token marking: "Mark unresolvable values: UNKNOWN. Mark loading states not yet confirmed: MISSING-LOADING. Mark error states not yet confirmed: MISSING-ERROR." Derived state included in Derived Dependents column. Role 3 auditor verifies: "§3 state delta: all rows present, UNKNOWN/MISSING tokens used where needed." |
| V-02 | **PASS** | STATUS column on state delta table. STATUS=UNKNOWN for unresolvable values, STATUS=MISSING for absent branches. Before/After columns in schema. No state change can be implied -- every change needs a row and a STATUS. |

---

#### C-04 -- Re-render list complete (essential, 15 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §4 table: Component / Re-renders? / Reason / Notes. "SKIPPED components explicitly listed." Both re-rendered and not-re-rendered components required. Role 3 auditor verifies: "§4 re-render list: SKIPPED components explicitly listed." |
| V-02 | **PASS** | STATUS column on re-render table. Every component row is required with STATUS declaring its state. STATUS=SKIPPED or equivalent for non-re-rendering components prevents silent omission. Structured schema makes a missing component row structurally apparent. |

---

#### C-05 -- Side effects and async calls identified (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §5: timing (sync / deferred), owner component/middleware, loading branch, error branch all required. "Mark unconfirmed loading branches: MISSING-LOADING. Mark unconfirmed error branches: MISSING-ERROR." Both branches must be named or marked. Role 3 auditor verifies: "§5 async: both loading and error branches named or marked MISSING." |
| V-02 | **PASS** | STATUS column on side effects table. STATUS=MISSING-LOADING and STATUS=MISSING-ERROR as valid STATUS values for absent branches (inferred from C-12 targeting hypothesis). Every async effect row must declare its loading and error branch STATUS. Silent omission structurally impossible. |

---

#### C-06 -- Issue flags present (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §6: "Evaluate all four categories. Do not skip a category -- state 'none found' with supporting evidence from prior sections if applicable." Each of (a) unnecessary re-renders, (b) missing loading states, (c) error state gaps, (d) accessibility failures must be evaluated. "No issues found" requires citing specific §4 entries. Role 3 auditor verifies: "§6 issues: all four categories evaluated with evidence." Advisory escape strings blocked by audit mechanism. |
| V-02 | **PASS** | STATUS column on issue table. Every issue category row requires a STATUS. A category row with STATUS=NONE still requires evidence in the table row. Per-row STATUS prevents section-level "no issues" without per-category engagement. |

---

#### C-07 -- Final UI state described (recommended, 10 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §7: "Describe the observable final UI state: which elements are visible/hidden, what text or data is displayed, what interactive state." Explicit citation format: "Because [§3 key] changed from X to Y, [component] now shows [state]." Every UI change must cite a §3 key. Role 3 auditor verifies: "§7 final state: each UI change cites a §3 key." |
| V-02 | **PASS** | STATUS column on final UI state table. Every observable UI element requires a row and a STATUS. STATUS=CONFIRMED for verified states, STATUS=UNKNOWN for unconfirmed. §3 key citation in schema column enforces derivation link. |

---

#### C-08 -- Optimization opportunities called out (aspirational, 5 pts)

Pass condition (v3 tightening): optimization candidate named with component and expected render reduction; OR explicit "no optimization" with C-04 citations. Silent absence fails.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PARTIAL** | §6(a) "Unnecessary re-renders: cite §4 rows" + "each issue found includes... one-line remediation hint" + "no issues found requires citing §4 entries." The "no optimization" case is covered (§4 citations required with no-issues finding). The "optimization found" case is weakly covered: "one-line remediation hint" allows component + optimization type but does not require the render-reduction quantification that C-08 demands ("expected render reduction"). No dedicated optimization section. Score: 2 pts. |
| V-02 | **PARTIAL** | Same weakness: issue section remediation hint does not explicitly require render-reduction quantification. No dedicated optimization section in partial template. Score: 2 pts. |

---

#### C-09 -- Framework-portable annotations (aspirational, 5 pts)

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §8 Framework Notes is a mandatory section (not optional), placed after §7 Final UI State. Role 2 instruction: "Translate the trace into framework-specific vocabulary for teams working in {framework}. This is the only section where framework-specific terms from the Vocabulary Contract appear. Map each neutral term used in §1-§7 back to its framework equivalent." Dedicated annotation layer that makes the core trace framework-neutral and the framework-specific mechanics explicit. Score: 5 pts. |
| V-02 | **PARTIAL** | Partial template shows "Frontend domain expert" role with no dedicated Framework Notes section visible. The framing "auditable by any frontend engineer regardless of framework familiarity" signals neutrality intent, but without a mandatory Framework Notes section or vocabulary contract, framework-specific mechanics are not isolated in a dedicated layer. Template truncated before final sections -- Framework Notes section may exist but cannot be confirmed. Score: 2 pts. |

---

#### C-10 -- Gap-visible format for essential sections (aspirational, 5 pts)

Pass condition: structured format (table or numbered enumeration) for C-01 (event chain) and C-04 (re-render list) such that missing entries are visually apparent.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §1 Event Chain: "Format: numbered list, one row per entry." A missing handler = a missing numbered row, visible without cross-referencing source. §4 Re-render List: table format (Component / Re-renders? / Reason / Notes), one row per component. A missing component = a missing table row. Both targeted sections use enumeration formats. Score: 5 pts. |
| V-02 | **PASS** | STATUS column on every structured section ensures every section is a table. Every row for every section must have a STATUS. A handler row that is absent from the event chain table is structurally visible -- the table ends before accounting for all handlers. STATUS column adds a per-row audit marker that makes incompleteness self-evident. Score: 5 pts. |

---

#### C-11 -- Cross-section evidence chaining (aspirational, 5 pts)

Pass condition: at least two downstream sections cite upstream findings by name; C-07 (final UI state) traces back to at least one C-03 row.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §6 cites upstream by reference: "(b) Missing loading states: cite MISSING-LOADING tokens from §3 or §5" and "(a) Unnecessary re-renders: cite §4 rows." §7 citation format: "Because [§3 key] changed from X to Y, [component] now shows [state]" -- the §3 state key is the citation anchor. Role 3 auditor completes a derivation chain check: "event handler (Event Chain) -> state key change (State Delta) -> component re-render (Re-render List) -> observable UI element (Final UI State)." Score: 5 pts. |
| V-02 | **PARTIAL** | STATUS column establishes per-row tracking but does not inherently enforce citation chaining across sections. A row's STATUS is local to its section -- there is no mechanism in the partial template requiring downstream sections to name upstream row identifiers. The template may include citation requirements in the issue and final-state prose sections (template truncated), but this cannot be confirmed. Score: 2 pts. |

---

#### C-12 -- Explicit incompleteness tokens (aspirational, 5 pts)

Pass condition: gaps are marked with explicit tokens (UNKNOWN, MISSING-LOADING, MISSING-ERROR, or equivalent) rather than silently omitted; artifact contains at least one such token OR affirmative "no unknowns" statement.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | §1: "UNKNOWN: {reason}" for undetermined handlers. §2: "UNKNOWN permitted for components whose participation is unconfirmed." §3 table: UNKNOWN, MISSING-LOADING, MISSING-ERROR cells. §5: MISSING-LOADING and MISSING-ERROR for absent async branches. Role 3 stamps: "TRACE COMPLETE -- {N} UNKNOWN tokens / {M} MISSING tokens / {K} issues flagged" -- making the incompleteness inventory observable from the artifact stamp alone. Score: 5 pts. |
| V-02 | **PASS** | Mandatory STATUS column targets C-12 directly (stated in hypothesis). STATUS column values include UNKNOWN and MISSING-LOADING/MISSING-ERROR equivalents. Every row must declare its STATUS; a row cannot be silently incomplete -- it must declare STATUS=UNKNOWN or equivalent. The schema itself is the incompleteness-marking mechanism. Score: 5 pts. |

---

#### C-13 -- Framework-neutral core trace enforcement (aspirational, 5 pts)

Pass condition: C-01 through C-07 sections contain no framework-specific vocabulary in narrative body; framework terms confined to dedicated annotation layer.

| V | Verdict | Evidence |
|---|---------|---------|
| V-01 | **PASS** | Role 1 (Vocabulary Auditor) produces a Vocabulary Contract table mapping every framework-specific term to a neutral equivalent; FRAMEWORK-ONLY terms flagged for §8 only. Role 2 constraint: "Core trace sections (§1 through §7) must use ONLY the neutral equivalents from the Vocabulary Contract. Framework-specific terms are confined to §8 Framework Notes. Violation: framework jargon appearing in §1-§7 prose." Role 3 auditor checklist item: "§8 framework notes: no framework jargon leaked into §1-§7." Three-layer enforcement: contract established first, section constraint explicit, audit closes the loop. Directly addresses the R2 pattern where "use framework vocabulary throughout" coexisted with Framework Notes and gave models an escape route. Score: 5 pts. |
| V-02 | **PARTIAL** | Hypothesis framing: "auditable by any frontend engineer regardless of framework familiarity" signals neutrality intent. However, partial template shows role instruction starting with "Your domain expertise is auto-selected from the framework context" -- without a vocabulary contract and without an explicit neutral-vocabulary constraint on core sections, the model can use useState, v-model, etc. in core section prose and point to framework-familiarity framing as compliance. No enforcement mechanism equivalent to V-01's Vocabulary Contract + constraint + audit. Score: 2 pts. |

---

### Score Summary (complete)

| Criterion | V-01 | V-02 |
|-----------|------|------|
| C-01 Event chain complete (15) | PASS 15 | PASS 15 |
| C-02 Component tree traversal (15) | PASS 15 | PASS 15 |
| C-03 State delta shown (15) | PASS 15 | PASS 15 |
| C-04 Re-render list complete (15) | PASS 15 | PASS 15 |
| C-05 Side effects and async (10) | PASS 10 | PASS 10 |
| C-06 Issue flags (10) | PASS 10 | PASS 10 |
| C-07 Final UI state (10) | PASS 10 | PASS 10 |
| C-08 Optimization opportunities (5) | PARTIAL 2 | PARTIAL 2 |
| C-09 Framework-portable annotations (5) | PASS 5 | PARTIAL 2 |
| C-10 Gap-visible format (5) | PASS 5 | PASS 5 |
| C-11 Cross-section evidence chaining (5) | PASS 5 | PARTIAL 2 |
| C-12 Explicit incompleteness tokens (5) | PASS 5 | PASS 5 |
| C-13 Framework-neutral core trace (5) | PASS 5 | PARTIAL 2 |
| **Total** | **117** | **108** |
| All essential pass | YES | YES |
| Band | **Golden** | **Golden** |

---

### Ranking (available variations)

| Rank | V | Score | Key wins | Key gaps |
|------|---|-------|----------|----------|
| 1 | V-01 | 117 | C-13 PASS (vocabulary contract mechanism), C-09 PASS (mandatory Framework Notes), C-11 PASS (Role 3 derivation chain) | C-08 PARTIAL only (no render-reduction quantification requirement) |
| 2 | V-02 | 108 | C-12 PASS (STATUS column), C-10 PASS (tables everywhere) | C-09 PARTIAL (no dedicated Framework Notes confirmed), C-11 PARTIAL (no cross-section citation enforcement), C-13 PARTIAL (no vocabulary contract) |

V-03 through V-05: not scored (not provided in invocation). Based on standard round design pattern, V-04 (combined role seq + STATUS column) and V-05 (combined all axes) would be expected to reach 115-120 range.

---

### Key Findings

**C-13 is the discriminator:** V-01's three-role sequence (Vocabulary Auditor before Trace Analyst) directly fixes the R2 blocker: the Vocabulary Contract is established before the trace, §1-§7 are explicitly constrained to neutral vocabulary, and Role 3 audits for leakage. V-02's STATUS column is a structural incompleteness mechanism (C-12) but has no equivalent vocabulary enforcement, leaving C-13 at PARTIAL.

**C-12 satisfied by both available variations:** V-01 achieves C-12 through explicit named tokens (UNKNOWN, MISSING-LOADING, MISSING-ERROR) and a Role 3 stamp that aggregates the count. V-02 achieves C-12 through the STATUS column itself -- UNKNOWN and MISSING-* are STATUS values, not post-hoc tokens. Two orthogonal mechanisms for the same criterion.

**C-08 weakness in both:** Neither V-01 nor V-02 require render-reduction quantification in optimization findings. The "one-line remediation hint" format in §6 allows a component name + optimization type without the expected render reduction. A V-04/V-05 design that combines the vocabulary contract with explicit optimization quantification in the issue section could close this gap.

---

### Excellence Signals from V-01

**Signal 1 -- Vocabulary Contract first.**
Establishing the framework-to-neutral vocabulary mapping as a Role 1 artifact (a named table, pre-trace) inverts the R2 failure pattern. In R2, role instructions said "use framework vocabulary throughout" while also requiring a Framework Notes section -- the contradiction let models use useState in core sections. V-01 eliminates the contradiction: Role 1 produces the contract, Role 2 is constrained to neutral-column-only for §1-§7, and §8 is explicitly the only zone for framework terms. The contract is a first-class artifact, not an instruction buried in prose.

**Signal 2 -- Machine-readable incompleteness inventory.**
Role 3 stamps the artifact: "TRACE COMPLETE -- {N} UNKNOWN tokens / {M} MISSING tokens / {K} issues flagged." This extends C-12 from individual token marking to a trace-level summary. A reviewer can assess completeness from the stamp alone without reading every row. The stamp also creates a measurable property of the trace (N unknowns, M missing branches) that can be compared across trace artifacts and used as a quality signal in automated tooling.

**Signal 3 -- Three-role derivation mirrors trace structure.**
Role 1 (vocabulary contract) establishes the framework-neutral mapping for the annotation layer. Role 2 (trace analyst) follows the event-to-UI derivation chain using neutral vocabulary. Role 3 (completeness auditor) verifies the derivation chain end-to-end. The role sequence is isomorphic to the trace's own structure: setup -> derivation -> audit. This alignment means each role's output is a natural input to the next role, with no role forced to re-narrate from scratch.

---

```json
{"top_score": 117, "all_essential_pass": true, "new_patterns": ["Vocabulary Contract first -- Role 1 before the Trace Analyst establishes a framework-term to neutral-term mapping as a named table artifact before any trace content is written; §1-§7 are then explicitly constrained to neutral-column vocabulary only; §8 is the sole designated zone for framework terms; Role 3 audits for leakage; this inverts the R2 contradiction where role-level vocabulary instructions coexisted with Framework Notes and gave models an escape route into framework jargon in core sections", "Machine-readable incompleteness inventory -- Role 3 stamps the artifact with UNKNOWN token count and MISSING token count making the completeness level of the trace observable from the stamp alone without reading every row; this extends C-12 from individual gap marking to a trace-level aggregate that can be compared across artifacts and used as a quality signal in review pipelines"]}
```
