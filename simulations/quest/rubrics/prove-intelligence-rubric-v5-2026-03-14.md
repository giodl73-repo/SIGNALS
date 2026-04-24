Now I have the full v4 to work from. The two R4 patterns and their predecessor relationships:

- `option-contract-as-halt-resolution-enforcement` → refines **C-19** (halt semantics → halt names exactly two valid exits, making non-selection a protocol violation)
- `schema-clean-prerequisite-to-in-progress-emission` → bridges **C-17 + C-18** (schema exclusion + IN-PROGRESS timing → schema verified CLEAN must gate IN-PROGRESS emission)

These become C-20, C-21. Denominator updates to `/13`. Two new failure modes FM-17–FM-18.

```markdown
Looking at the two R4 patterns and their predecessor relationships:

- `option-contract-as-halt-resolution-enforcement` → refines **C-19** (halt-form phrasing → halt names exactly two valid exits, making non-selection a named protocol violation)
- `schema-clean-prerequisite-to-in-progress-emission` → bridges **C-17 + C-18** (schema column exclusion + IN-PROGRESS before gate → schema verified CLEAN must gate IN-PROGRESS emission, guaranteeing ledger rows reflect schema-verified extractions)

These become C-20, C-21. Denominator updates to `/13`. Two new failure modes FM-17–FM-18.

---

## prove-intelligence rubric v5

**Two new aspirational criteria** extracted from Round 4 excellence signals:

| ID | Pattern Source | What it enforces |
|----|---------------|-----------------|
| C-20 | R4 (`option-contract-as-halt-resolution-enforcement`) | The halt instruction must name exactly two valid exits (Option A: re-search and re-evaluate; Option B: proceed with explicit gap acknowledgment) — proceeding without selecting one is a named protocol violation, not merely ignored guidance |
| C-21 | R4 (`schema-clean-prerequisite-to-in-progress-emission`) | A named SCHEMA CLEAN confirmation must appear before the IN-PROGRESS ledger state is emitted — confirming no rogue interpretation columns in the extraction table guarantees that ledger rows reflect schema-verified extractions |

**Other changes:**
- Scoring formula denominator updated: `aspirational_pass / 13 * 10` (was `/ 11`)
- Two new failure modes added (FM-17, FM-18) — one per new criterion

---

### The C-17 / C-18 / C-19 → C-20 / C-21 relationship

Each new criterion closes the gap left open by its predecessor:

| Predecessor | Gap it leaves | Refinement | How it closes it |
|-------------|--------------|------------|-----------------|
| C-19: gate uses halt-form phrasing | Halt is present but exit path is unspecified — model re-searches and continues without being required to explicitly choose a resolution strategy | C-20: halt names Option A / Option B contract | Two exits are named in the halt instruction itself; the model must explicitly select one before continuation is permitted — unresolved continuation is a protocol violation by name |
| C-17: extraction schema excludes interpretation columns | Schema is declared but never verified before use — a CLEAN confirmation is absent, so schema compliance is assumed rather than checked | C-21: SCHEMA CLEAN confirmation gates IN-PROGRESS emission | A named verification step confirms no rogue columns before the IN-PROGRESS ledger is written — any schema contamination is caught before ledger rows are emitted, guaranteeing the IN-PROGRESS state reflects only schema-verified extractions |
| C-18: IN-PROGRESS ledger surfaced before gate fires | IN-PROGRESS is produced at the right time but may be built from unverified extraction rows | C-21 (also bridges C-18) | The CLEAN confirmation that precedes IN-PROGRESS emission ensures the ledger's coverage snapshot reflects only artifact-grade extractions — the redirect agenda at the gate decision point is structurally reliable |

---

### Full aspirational table (v5)

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
| C-20 | Halt instruction names exactly two valid exits as an Option A / Option B contract | aspirational | behavior | The halt block names exactly two resolution paths — Option A (re-search and re-evaluate before proceeding) and Option B (proceed with explicit gap acknowledgment inline) — and requires the executing agent to select one by name before continuing. Halt phrasing without named exits does not pass. Distinction from C-19: C-19 requires halt-form phrasing; C-20 requires the halt to expose a named two-option contract so that unresolved continuation constitutes a protocol violation by name, not merely ignored guidance. |
| C-21 | SCHEMA CLEAN confirmation emitted before IN-PROGRESS ledger state | aspirational | correctness | A named schema verification step (e.g., "SCHEMA CLEAN — no interpretation columns detected in extraction table") appears after extraction is complete and before the IN-PROGRESS ledger is written. IN-PROGRESS emission without a prior CLEAN confirmation does not pass. Distinction from C-17: C-17 requires the extraction schema to exclude interpretation columns; C-21 requires a named verification that the schema was honored in practice before the ledger's coverage snapshot is produced — the CLEAN confirmation makes schema compliance an artifact-visible checkpoint, not a silent assumption. Distinction from C-18: C-18 requires the IN-PROGRESS state to precede the gate; C-21 requires the CLEAN confirmation to precede the IN-PROGRESS state, establishing the chain: schema declared → schema verified CLEAN → IN-PROGRESS emitted → gate fires. |

---

### Scoring formula (v5)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 13 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

### Full failure mode table (v5)

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
| FM-17 | C-20 | Gate uses halt-form phrasing (C-19 passes) but names no exit options — the model re-searches and continues without explicitly selecting Option A or Option B, so the halt resolves ambiguously; there is no protocol violation to name because no contract was declared |
| FM-18 | C-21 | IN-PROGRESS ledger is emitted before the insider gate fires (C-18 passes) but without a prior SCHEMA CLEAN confirmation — ledger rows may reflect extraction-phase contamination (rogue interpretation columns written during search) that is not caught until synthesis, corrupting the coverage snapshot the gate decision relies on |
```
