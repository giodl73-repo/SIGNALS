Looking at the three R3 patterns and their predecessor relationships:

- `schema-column-exclusion-as-structural-enforcement` → refines **C-15** (named roles/phases → schema-enforced exclusion)
- `in-progress-ledger-before-gate-enables-targeted-redirect` → refines **C-16** (multi-state ledger → ledger state surfaced *before* gate fires)
- `halt-instruction-semantics-vs-advisory-semantics` → refines **C-14** (blocking WARNING text → halt semantics, not advisory semantics)

These become C-17, C-18, C-19. Denominator updates to `/11`. Three new failure modes FM-14–FM-16.

---

## prove-intelligence rubric v4

**Three new aspirational criteria** extracted from Round 3 excellence signals:

| ID | Pattern Source | What it enforces |
|----|---------------|-----------------|
| C-17 | R3 (`schema-column-exclusion-as-structural-enforcement`) | The extraction table schema must physically exclude interpretation columns — a schema that omits Relevance/Strength/Verdict fields makes C-15 impossible to violate without a visible schema error |
| C-18 | R3 (`in-progress-ledger-before-gate-enables-targeted-redirect`) | The falsification ledger's IN-PROGRESS state must be surfaced before the insider gate fires — coverage gaps must be visible as a specific redirect agenda before synthesis begins |
| C-19 | R3 (`halt-instruction-semantics-vs-advisory-semantics`) | The insider gate WARNING must use halt semantics ("STOP. Do not proceed.") not advisory semantics ("before proceeding, re-search") — only the halt form requires explicit resolution before the artifact continues |

**Other changes:**
- Scoring formula denominator updated: `aspirational_pass / 11 * 10` (was `/ 8`)
- Three new failure modes added (FM-14, FM-15, FM-16) — one per new criterion

---

### The C-14 / C-15 / C-16 → C-17 / C-18 / C-19 relationship

Each new criterion closes the gap left open by its predecessor:

| Predecessor | Gap it leaves | Refinement | How it closes it |
|-------------|--------------|------------|-----------------|
| C-15: separation via named roles or phases | Named sections exist but interpretation columns can still appear inside the extraction phase block | C-17: schema-enforced column exclusion | A declared extraction schema with no interpretation columns makes the violation structurally visible — a rogue Relevance column in the extraction table breaks the schema contract |
| C-16: ledger exists in multiple phase-tied states | Multi-state ledger is required but state timing is unspecified — IN-PROGRESS state may appear after synthesis begins | C-18: IN-PROGRESS ledger surfaced before gate fires | Requires the IN-PROGRESS state to be visible at search completion, before the gate check — coverage gaps generate a specific redirect agenda, not a vague "search more" instruction |
| C-14: gate implemented as blocking WARNING text | WARNING text is present but may use advisory phrasing that permits continuation | C-19: gate uses halt semantics, not advisory semantics | "STOP. Do not proceed." requires explicit resolution. "Before proceeding, re-search" is advisory — the model can satisfy it and continue without pause |

---

### Full aspirational table (v4)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Output identifies at least one internal contradiction | aspirational | depth | Named conflict (source A vs. source B disagree on X) resolved or flagged unresolved. "Mixed sources" without identifying specific conflict is a fail. |
| C-10 | Output recommends follow-up queries for evidence gaps | aspirational | behavior | At least two named queries, each with: what to query, where to look, which FC it addresses. Generic "more research" language is a fail. |
| C-11 | Insider advantage treated as a hard exit condition | aspirational | behavior | Gate enforced — zero-insider runs must surface an explicit warning. Count field alone without gatekeeping does not pass. |
| C-12 | Extraction and interpretation are structurally separated | aspirational | correctness | Extraction logged before any interpretation, relevance, or strength labeling. Single-pass format does not pass. |
| C-13 | Falsification ledger is a first-class named artifact | aspirational | coverage | Named table mapping every FC to sources and status. Per-source FC fields alone do not pass. |
| C-14 | Insider gate enforced by blocking WARNING text, not by a count field | aspirational | behavior | Verbatim `WARNING: INSIDER GATE NOT MET` block + explicit "do not proceed" instruction. Count-only field or verdict note does not pass. Distinction from C-11: C-11 requires a gate exist; C-14 requires it be implemented as blocking text. |
| C-15 | Structural separation implemented with named roles or phases, not in-block ordering | aspirational | correctness | Named roles (Archivist/Analyst) or named phases (Phase 2/Phase 3) visible as distinct sections. In-block ordering (excerpt field then relevance field in the same source block) does not pass. Distinction from C-12: C-12 requires separation be visible; C-15 requires it be via named roles or phases. |
| C-16 | Falsification ledger exists in multiple lifecycle states tied to phase exits | aspirational | coverage | At minimum: initial state (all FCs open, at search completion) and final state (at synthesis). Three-state lifecycle (draft / in-progress / final) is gold standard. Single end-state ledger does not pass. Distinction from C-13: C-13 requires a named ledger exist; C-16 requires multiple phase-tied states. |
| C-17 | Extraction table schema physically excludes interpretation columns | aspirational | correctness | The declared extraction schema omits interpretation columns (Relevance, Strength, Verdict, Analysis) — a rogue interpretation column in the extraction block constitutes a visible schema violation. A schema that includes interpretation columns even in a separate section does not pass. Distinction from C-15: C-15 requires named roles or phases; C-17 requires the extraction schema itself to enforce the boundary by column exclusion. |
| C-18 | IN-PROGRESS falsification ledger surfaced before insider gate fires | aspirational | coverage | The IN-PROGRESS ledger state (showing which FCs remain open or weakly-evidenced) is produced at search completion, before the gate check executes. Uncovered FCs generate a named redirect agenda visible in the gate section. A multi-state ledger that produces the IN-PROGRESS state after synthesis begins does not pass. Distinction from C-16: C-16 requires multiple phase-tied states; C-18 requires the IN-PROGRESS state to appear at the gate decision point so coverage gaps drive targeted redirect rather than vague re-search. |
| C-19 | Insider gate uses halt semantics, not advisory semantics | aspirational | behavior | The gate instruction uses unconditional halt phrasing: "STOP. Do not proceed to [next section/phase/step]." Advisory phrasing ("before proceeding, re-search for insider sources") does not pass — it permits continuation after a nominal re-search attempt without requiring explicit resolution. Distinction from C-14: C-14 requires blocking WARNING text to exist; C-19 requires the phrasing to be halt-form, making continuation without explicit resolution a protocol violation. |

---

### Scoring formula (v4)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

### Full failure mode table (v4)

| ID | Criterion | Failure Pattern |
|----|-----------|-----------------|
| FM-01 | C-01 | Source cited without full path — filename only, or "see above" reference |
| FM-02 | C-02 | Paraphrase or summary substituted for verbatim excerpt |
| FM-03 | C-03 | Relevance judgment present but not linked to a named hypothesis or FC |
| FM-04 | C-04 | Source block omits strength label, or strength label is applied to the aggregate rather than per-source |
| FM-05 | C-05 | Output ends at analysis; no closing verdict maps evidence to hypothesis |
| FM-06 | C-06 | All sources are the same type (e.g., all code, all docs) — no cross-type corroboration |
| FM-07 | C-07 | Evidence sections exist but FC mapping is absent or informal — no explicit FC identifier per source |
| FM-08 | C-08 | Insider flag field present but populated by inspection after the fact — no structured count or gate |
| FM-09 | C-09 | Output notes "mixed sources" or "conflicting signals" without naming the specific sources and the specific claim in conflict |
| FM-10 | C-10 | Follow-up queries present but generic ("search for more examples") — not tied to named FCs or specific search targets |
| FM-11 | C-14 | Run includes an insider count check (C-11 passes) but uses a count-only field or verdict note rather than blocking WARNING text — the gate records the miss but does not prevent the model from continuing as if the skill's value was delivered |
| FM-12 | C-15 | Skill uses in-block ordering (excerpt field precedes relevance field within the same source block) and claims separation — passes C-12 on visual inspection but fails when the model compresses or merges fields, because a merged block leaves no structural gap in the artifact |
| FM-13 | C-16 | A complete and accurate falsification ledger exists at synthesis (C-13 passes) but was written in a single pass at the end — uncovered FCs are only visible after the verdict is already written, removing the opportunity to redirect search before synthesis |
| FM-14 | C-17 | Extraction phase uses named roles or phases (C-15 passes) but the extraction table schema includes interpretation columns (Relevance, Strength) alongside excerpt columns — the schema permits co-location and the boundary is maintained only by discipline, not by structure |
| FM-15 | C-18 | Multi-state ledger exists (C-16 passes) but the IN-PROGRESS state is produced after synthesis begins — the gate fires against a count-only check rather than against the coverage snapshot, so uncovered FCs are not visible as a redirect agenda at the decision point |
| FM-16 | C-19 | WARNING block exists (C-14 passes) but uses advisory phrasing: "before proceeding to synthesis, attempt to locate insider sources" — model satisfies the advisory by a nominal re-search attempt and continues without explicit resolution, defeating the gate's purpose |
