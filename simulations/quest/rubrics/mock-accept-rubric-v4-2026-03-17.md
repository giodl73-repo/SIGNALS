Reading the R3 scorecard carefully before writing.

The new signals not yet captured in v3:

| Evidence | Pattern |
|----------|---------|
| V-03 C-01: "Rule A/B/C artifact-as-subject with blank `___` targets" | Blank slots in auto-flag rule templates, not just MOCK-ACCEPTED slots |
| V-03 C-03: "CANARY ASSERTION (blank slot + CONSTRAINT)" | CANARY itself carries a fill-in blank + constraint |
| V-02 C-15: "4 forbidden forms with halt instruction" | Forbidden-form enumeration includes explicit halt action, not just diagnosis |
| V-03 C-04: "4 sections with CONSTRAINT per section" | Per-section CONSTRAINT blocks inside the review Write block |
| V-03 C-05: "Revert-on-violation with paraphrase examples" | Revert instruction includes quoted violation examples, not just the class label |

C-19 folds V-03 C-01 + V-03 C-03 into one criterion (universal blank-slot enforcement). C-20 extends C-15 with the halt trigger. C-21 extends C-12 into the review artifact. C-22 strengthens the paraphrase revert.

Denominator: 10 → 14. C-09 N/A cascade: 14 - C-09 - C-15 - C-20 = denominator 11.

---

# Rubric — mock-accept v4

## What changed from v3

Four new aspirational criteria (C-19 to C-22) extracted from R3 excellence signals:

| ID | Pattern | Source |
|----|---------|--------|
| C-19 | **Universal blank-slot enforcement** — blank `___` targets appear in auto-flag rule output templates and in the CANARY ASSERTION, not only in MOCK-ACCEPTED slots; every evaluator fill-in site is structurally visible by inspection; bracket notation `[placeholder]` does not satisfy (looks filled even when unmodified) | V-03 C-01: "Rule A/B/C artifact-as-subject with blank `___` targets"; V-03 C-03: "CANARY ASSERTION (blank slot + CONSTRAINT)" |
| C-20 | **Halt-on-violation instruction** — the forbidden-form enumeration (C-15) includes an explicit halt or stop instruction naming the action to take when a violation is detected; diagnostic enumeration alone (self-diagnosing without stop action) does not satisfy | V-02 C-15: "4 forbidden forms with halt instruction" |
| C-21 | **Per-section CONSTRAINT in review Write block** — each named section within the review artifact Write block carries its own co-located CONSTRAINT block; a single top-level Write instruction without per-section constraints does not satisfy; extends C-12 to the review artifact structure | V-03 C-04: "4 sections with CONSTRAINT per section" |
| C-22 | **Paraphrase violation examples in revert instruction** — Revert-on-violation in the MOCK-ACCEPTED positive argument includes at least two quoted concrete paraphrase examples (altered token forms); naming "paraphrase" as a violation class without examples does not satisfy | V-03 C-05: "CONSTRAINT blocks + Revert-on-violation with paraphrase examples" |

Scoring formula updated: aspirational denominator changes from 10 to 14. Aspirational pool = `(passes / 14) × 10`.

C-09 N/A cascade updated: if C-09 is absent → C-15 is N/A → C-20 is N/A; denominator becomes 11 (14 − 3).

Four new failure modes added (MA-17 to MA-20), one per new criterion.

The R3 ceiling: V-01 at 98.0 (C-14, C-18 failing), V-02 at 97.0 (C-14, C-17, C-18 failing). Both pass C-19–C-20 but V-02 fails C-17. V-03 passes all Essential and Recommended; Aspirational data was unavailable for full scoring.

---

## Criteria

### Essential — 12 pts each · max 60

| ID | Criterion | Description |
|----|-----------|-------------|
| C-01 | Auto-flag rules | Rules A/B/C produce explicit, unconditional statements per namespace using artifact-as-subject form; no "I found…" language in auto-flag output |
| C-02 | Forbidden triad | All three forbidden triggers (namespace-level, artifact-level, evaluation-level) acknowledged by name; completeness check enforced ("a two-of-three set does not satisfy this gate") |
| C-03 | Status writeback + Canary | Phase N Edit tool call for status writeback; CANARY ASSERTION present verbatim; CANARY-FALSE-POSITIVE named; CANARY SUPPRESSED branch defined |
| C-04 | Review artifact structure | Review Write instruction includes: Coverage table (4 cols), Structural records, Risk section with urgency labels, Next Steps — all under a single Write block; no orphaned sections outside the Write |
| C-05 | MOCK-ACCEPTED positive argument | Labeled fields with exact-token constraint + revert-on-violation for each slot; Slot 1 and Slot 2 structurally separate; paraphrase explicitly named as a violation |

A single Essential FAIL caps the composite at 55. Two Essential FAILs cap at 43.

---

### Recommended — 10 pts each · max 30

| ID | Criterion | Description |
|----|-----------|-------------|
| C-06 | Entity-naming in roles | Each role output uses a "Required artifact citation" template naming specific elements (field name, token, slot) verbatim; yes/no verdicts alone do not satisfy |
| C-07 | Step sequencing and guard compliance | Named accumulator lists (Arch-blocked, Strategy-blocked) populated during evaluation phase; partition explicit before phase exit; empty list must be stated ("Arch-blocked: none") |
| C-08 | Eval-driven REAL-REQUIRED template | 5-field template per role evaluation: trigger condition · SQ answer (artifact as subject) · Artifact state · verdict · required action; VERDICT-ECHO named |

---

### Aspirational — pool of 10 pts · `(passes / 14) × 10`

| ID | Criterion | Description |
|----|-----------|-------------|
| C-09 | Artifact-as-subject grammar | Standing rule embedded at top of spec; auto-flag rules and role evaluations use "The mock artifact's [ns] section [records/shows/lacks]…" form throughout all phases |
| C-10 | Tier sourcing | Opening step output includes `"Tier: N (source: TOPICS.md \| --tier \| default)"`; instruction tier governing current phase is explicit, not implicit |
| C-11 | Inline completeness gate | Named completeness checkpoint with count assertion: `"N + M = [total]. Expected: 9."` or equivalent halt condition before phase transitions; anonymous narrative checks do not satisfy |
| C-12 | Reason-code enforcement at point of use | Exact-token constraint co-located with column rule or checkbox at the point of use — not in preamble or instructions section only |
| C-13 | Phase exit assertions | Explicit named PHASE N EXIT ASSERTION before each phase transition; each includes N+M count; "Do not proceed until" language; blocks interleave of auto-flag and evaluation phases |
| C-14 | Blank-line failure signal | Incomplete slots are structurally visible as fill-in blanks (`"Your codes: ___"` / `"Your statement: ___"`) without requiring prose parsing; absence readable by inspection |
| C-15 | Forbidden-form enumeration | The artifact-as-subject standing rule enumerates specific forbidden alternatives (e.g., `"FAIL: 'I found…' / 'This namespace has…'"`) alongside the positive form; rule is self-diagnosing without requiring the evaluator to infer violations |
| C-16 | Written-gate blocking language | Phase exit assertions include `"Do not proceed to Phase N+1 until written"` or equivalent; the assertion must be committed as output text before progression; advisory-only language does not satisfy |
| C-17 | Named gate registry | Completeness gates carry stable sequential IDs (GATE A, GATE B, GATE C…) forming a named registry; IDs are referenceable from other phases and from the review artifact; anonymous or ordinal-only gates do not satisfy |
| C-18 | Constraint-field co-location | Constraint block is physically adjacent to the field it governs; no intervening prose, headers, or instructions between the constraint statement and its fill-in target; preamble-only constraints do not satisfy |
| C-19 | Universal blank-slot enforcement | Blank `___` targets appear in auto-flag rule output templates and in the CANARY ASSERTION, not only in MOCK-ACCEPTED slots; every evaluator fill-in site is structurally visible by inspection; bracket notation `[placeholder]` does not satisfy |
| C-20 | Halt-on-violation instruction | The forbidden-form enumeration (C-15) includes an explicit halt or stop instruction naming the action to take when a violation is detected; diagnostic enumeration alone does not satisfy; the instruction must name the required action, not merely identify the violation |
| C-21 | Per-section CONSTRAINT in review Write block | Each named section within the review artifact Write block carries its own co-located CONSTRAINT block; a single top-level Write instruction without per-section constraints does not satisfy |
| C-22 | Paraphrase violation examples in revert instruction | Revert-on-violation in the MOCK-ACCEPTED positive argument includes at least two quoted concrete paraphrase examples (altered token forms); naming "paraphrase" as a violation class without quoted examples does not satisfy |

**C-09 N/A rule**: If the variation contains no artifact-as-subject standing rule (rule is absent, not failed), score aspirational as `passes / 11 × 10` and mark C-09, C-15, and C-20 as N/A (C-20 depends on C-15; C-15 depends on C-09). If C-09 is present but C-15 is independently absent, mark only C-15 and C-20 as N/A; denominator becomes 12.

---

## Failure Modes

| ID | Criterion | Failure Pattern |
|----|-----------|-----------------|
| MA-01 | C-01 | Auto-flag rules use evaluator-as-subject: `"I found…"`, `"This section has…"`, `"There is no…"` |
| MA-02 | C-02 | One or more triad labels absent; two-of-three treated as complete |
| MA-03 | C-03 | Status writeback missing Edit call; or CANARY ASSERTION absent; or CANARY-FALSE-POSITIVE not named |
| MA-04 | C-04 | Next Steps placed outside Write block; Coverage table missing a column; Risk section absent; urgency labels absent |
| MA-05 | C-05 | Slot 1 and Slot 2 not structurally separated; or revert-on-violation absent; or paraphrase not named as violation |
| MA-06 | C-06 | Role outputs give yes/no verdicts without naming field, token, or slot from the artifact |
| MA-07 | C-07 | Accumulator lists unnamed or absent; partition not stated before phase exit; empty list not declared |
| MA-08 | C-08 | 5-field template incomplete; SQ field absent; VERDICT-ECHO not named |
| MA-09 | C-09 | Auto-flag or role evaluation uses evaluator-as-subject despite standing rule being present |
| MA-10 | C-10 | Phase 0 output omits tier sourcing; tier is inferred or implicit |
| MA-11 | C-11 | Phase transitions occur without a named count assertion; narrative "all namespaces checked" does not satisfy |
| MA-12 | C-12 | Constraint appears only in preamble or a separate instructions section, not at the point of use |
| MA-13 | C-13 | Phase transition occurs without a named EXIT ASSERTION; "Do not proceed" language absent |
| MA-14 | C-14 | Incomplete slots use bracket notation `[placeholder]` rather than `___`; absence not readable by inspection |
| MA-15 | C-15 | Forbidden-form standing rule states the positive form only; specific forbidden alternatives not enumerated |
| MA-16 | C-16 | Phase exit assertion is advisory ("should be written") rather than blocking ("Do not proceed until written") |
| MA-17 | C-17 | Gates use ordinal names ("PHASE 1 EXIT ASSERTION") rather than stable sequential IDs (GATE A, GATE B…); IDs not referenceable across phases |
| MA-18 | C-18 | Constraint block separated from its governed field by intervening prose, headers, or instructions |
| MA-19 | C-19 | Blank `___` slots appear only in MOCK-ACCEPTED; auto-flag rule templates and/or CANARY ASSERTION use bracket notation or prose-only output targets |
| MA-20 | C-20 | Forbidden-form enumeration identifies violations but does not name a halt or stop action; evaluator must infer the response |
| MA-21 | C-21 | Review Write block has a single top-level CONSTRAINT; individual sections (Coverage, Risk, Next Steps, etc.) carry no per-section constraint |
| MA-22 | C-22 | Revert-on-violation names "paraphrase" as a class but provides no quoted examples of altered token forms |
