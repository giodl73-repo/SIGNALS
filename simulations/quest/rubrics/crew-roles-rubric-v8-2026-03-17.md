Reading the two excellence signals, extracting C-28 and C-29, then producing the full v8 rubric.

**ES-1 → C-28**: The annotation declares a term; a fifth failure mode `[TERM NOT IN QUESTION TEXT]` verifies the declared term appears verbatim (or stem-matched) in the question body. Converts annotation from metadata into content constraint.

**ES-2 → C-29**: Post-write diversity check is set-level and cannot detect silent per-role scope drift during authoring. A row-by-row plan-to-write binding check emitting `[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]` is the sufficient condition. Analogous to C-26 for annotations.

Formula bumps to `/21`.

---

```markdown
# crew-roles rubric — v8

---

## Changes from v7

- Added **C-28 Five-failure-mode annotation gate** (aspirational): The three-handle
  annotation `[Q: Q{N} — vocab: {bucket-row-id} — {term}]` carries three independently
  verifiable dimensions audited across four failure modes (C-26): Q-number correct,
  row-ID correct, term matches Phase 2, row-ID matches Phase 2. A question body that
  never uses the declared term passes all four checks — the annotation is structurally
  valid while the term remains metadata rather than content. CHECK 6 (or equivalent) must
  add a **fifth failure mode** `[TERM NOT IN QUESTION TEXT: annotation declares {term},
  question body does not contain it]` that verifies the declared term appears verbatim or
  stem-matched in the question body before the annotation is accepted. C-11 and C-18
  require the term to appear in `expertise.relevance` and the verification gate,
  respectively; neither closes the annotation-body gap. V-05 (R13) demonstrates: CHECK 6
  emits the fifth flag independently; a question annotated with a term that does not
  appear in its body fails CHECK 6 regardless of the other four checks passing.

- Added **C-29 Scope plan-to-write binding** (aspirational): C-14 and C-17 together
  mandate a pre-write scope audit and a post-write diversity confirmation (`>= 2 distinct
  scope values`). Diversity confirmation is a set-level property: if the planned role set
  assigns `team` and `cross-team` to two roles, the post-write check passes even if one
  role silently adopts `org` during authoring — two distinct values still appear. The
  sufficient condition is a row-by-row binding check that compares each role's planned
  scope (Phase 5 or equivalent) to its written scope (Phase 6 or equivalent) and emits
  `[{role}: planned {scope-A}, written {scope-B} — SCOPE BINDING MISMATCH]` for any
  divergence. This check is structurally analogous to C-26 (row-ID binding independent of
  term matching): diversity detection is necessary but not sufficient; per-role binding is
  the sufficient condition. CHECK 3B (or equivalent) must emit the mismatch flag before
  the verification gate (C-15) closes. V-05 (R13) demonstrates: CHECK 3B compares the
  planned-scope table to the written-scope table row-by-row and blocks the gate on any
  mismatch, independent of whether the post-write diversity count still passes.

- **Formula updated**: `aspirational_pass / 21 * 10` (was `/19`). Twenty-one aspirational
  criteria; each full pass contributes 0.476 points. Partial credit rule unchanged.

---

## Criteria

### Essential — all 5 must PASS for full essential score

| ID   | Criterion                | Description |
|------|--------------------------|-------------|
| C-01 | All 5 fields             | Every role file contains all 5 required fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope` |
| C-02 | Inertia-advocate present | At least one role has `orientation.frame` explicitly challenging the status quo; verify questions reference why the current approach is insufficient |
| C-03 | Correct output path      | Roles written to `.craft/roles/{area}/` |
| C-04 | Domain specificity       | `expertise.relevance` is anchored to the specific domain of the input; no generic engineering language |
| C-05 | Minimum 3 roles          | Output contains at least 3 roles, including the inertia-advocate |

### Recommended — partial credit (0.5 per PARTIAL)

| ID   | Criterion                    | Description |
|------|------------------------------|-------------|
| C-06 | Lens actionability           | `orientation.verify` fields are questions (`?`); `orientation.simplify` fields are imperatives; examples reinforce the constraint |
| C-07 | Collaborates_with resolves   | Every `collaborates_with` value matches the name of another file in the registry; no placeholder text or unresolved references at delivery |
| C-08 | Perspective diversity        | Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist); no category monopoly |

### Aspirational — partial credit (0.5 per PARTIAL); denominator 21

| ID   | Criterion                              | Description |
|------|----------------------------------------|-------------|
| C-09 | Scope gradient                         | Roles span at least 2 distinct scope values (e.g., `team`, `cross-team`, `org`); no homogeneous scope set |
| C-10 | Inertia domain-grounded                | The inertia-advocate framing names the specific current system, migration cost, or user habit — not generic resistance language |
| C-11 | Vocabulary-forced-field                | Phase 1 produces a named vocabulary list extracted from input; every `expertise.relevance` field must reference at least one vocabulary term |
| C-12 | Inertia pre-characterization           | Before writing the inertia-advocate, the skill answers 3 explicit questions: (1) current system name, (2) migration costs, (3) user habits; verify questions must reference at least 2 of these 3 dimensions |
| C-13 | Registry summary table                 | A `Role \| Orientation \| Scope \| Collaborates With` table appears in output after all roles are written; forces orphan-reference and scope-homogeneity checks at execution time |
| C-14 | Scope-gradient-enforcement             | A structural step after writing checks scope diversity; if all roles share the same scope value, the skill identifies and revises 1-2 roles before delivery — structural gate, not soft instruction |
| C-15 | Verification-gate-phase                | All post-write structural checks (registry summary table, orphan-reference check, scope-gradient check) are bundled into a single named gate that explicitly blocks delivery until all pass; checks are not scattered across instructions |
| C-16 | Vocabulary-linked inertia Q&A          | Each Q1/Q2/Q3 answer in the inertia pre-characterization references at least one term from the Phase 1 vocabulary; C-11 and C-12 are structurally wired, not independently satisfied |
| C-17 | Pre-write scope audit                  | Before any roles are written, a SCOPE AUDIT surveys the planned role set and assigns scope values; writing is blocked until >= 2 distinct scope values appear in the plan — prevention, not correction; structural gate before authoring |
| C-18 | Vocabulary check in verification gate  | The verification gate includes an explicit vocabulary coverage check confirming every `expertise.relevance` references a Phase 1 vocabulary term; the gate does not PASS without this check, regardless of orphan and scope checks passing |
| C-19 | Inertia frame Q-slot template          | The inertia-advocate `orientation.frame` is a fill-in template with explicit Q1 and Q2 slots populated from Phase 2 answers; the frame text contains named placeholders (e.g., `[Q1 current system]`, `[Q2 migration cost]`) that must be filled, not a soft instruction to reference them |
| C-26 | Four-failure-mode annotation gate      | The three-handle annotation `[Q: Q{N} — vocab: {bucket-row-id} — {term}]` is verified across four independent failure modes: Q-NUMBER MISMATCH, ROW-ID MISMATCH, TERM MISMATCH (annotation vs Phase 2), and ROW-ID MISMATCH (annotation vs Phase 2 row used). ROW-ID MISMATCH is emitted independently of TERM MISMATCH; a term appearing in two row positions cannot mask a wrong row citation |
| C-27 | Source-phrase forensic citation        | After any term replacement triggered by a NO row in the Phase 2 audit table, the replacement record quotes the verbatim Phase 1 source phrase alongside the new row identifier: `Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"`. A bucket-name re-assertion is non-verifiable; the forensic format requires the quoted phrase to exist verbatim in Phase 1 output; CHECK 7 (or equivalent) validates the match before the replacement is accepted |
| C-28 | Five-failure-mode annotation gate      | The annotation verification gate adds a **fifth failure mode** `[TERM NOT IN QUESTION TEXT: annotation declares {term}, question body does not contain it]` beyond the four required by C-26. The declared term must appear verbatim or stem-matched in the question body before the annotation is accepted; structural validity of the annotation (correct Q-number, row-ID, and term match against Phase 2) is necessary but not sufficient. CHECK 6 (or equivalent) emits the fifth flag independently; a structurally valid annotation whose declared term is absent from the question body fails CHECK 6 |
| C-29 | Scope plan-to-write binding            | A row-by-row binding check compares each role's planned scope (from the pre-write scope audit, C-17) to its written scope and emits `[{role}: planned {scope-A}, written {scope-B} — SCOPE BINDING MISMATCH]` for any per-role divergence. This check runs before the verification gate (C-15) closes and blocks delivery on any mismatch. Post-write diversity confirmation (C-14) is a necessary but insufficient guard; per-role binding (C-29) is the sufficient condition. CHECK 3B (or equivalent) emits the binding mismatch flag independently of whether the post-write diversity count still satisfies `>= 2 distinct values` |
```
