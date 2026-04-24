Reading the R4 scorecard carefully before writing.

**New patterns extracted from R4 evidence:**

1. **C-23 — Three-step halt sequence** (V-03 C-20 strong form): `"HALT. Delete the violating line. Rewrite in PASS form."` — V-01/V-04 pass C-20 on the borderline ("halt and rewrite before advancing"); V-03's three explicit imperatives eliminate evaluator discretion about intermediate steps. Strengthens C-20.

2. **C-24 — Gate-to-section traceability** (V-02 C-21 evidence): "GATE F cites specific section IDs" — the Phase 6 gate names Coverage / Structural records / Risk / Next Steps by stable IDs, not just a count assertion. Extends C-17 into the Phase 6 gate.

3. **C-25 — Slot 2 paraphrase examples** (V-03 C-22 evidence): "Slot 2 revert shifts from forbidden-form labeling to near-miss paraphrase examples; all examples are quoted altered-token forms" — C-22 targets Slot 1; this extends the requirement to Slot 2.

**Denominator: 14 → 17. C-09 N/A cascade: C-09 + C-15 + C-20 + C-23 → denominator 13.**

**R4 ceiling re-scored against v5:** V-04 passes C-24 (inherits V-02 Phase 6 GATE F with section IDs), fails C-23 (borderline two-step halt) and C-25 (Slot 2 not extended) → 14/17 aspirational → 8.2 → **Total: 98.2**.

---

# Rubric — mock-accept v5

## What changed from v4

Three new aspirational criteria (C-23 to C-25) extracted from R4 excellence signals:

| ID | Pattern | Source |
|----|---------|--------|
| C-23 | **Three-step halt sequence** — the Standing Rule halt instruction names three sequential atomic steps using imperatives (HALT · DELETE · REWRITE or equivalent); two-step phrasing ("halt and rewrite") satisfies C-20 but not C-23; the three-step form eliminates evaluator discretion about intermediate steps; advisory phrasing or combined gerunds do not satisfy | V-03 C-20: `"HALT. Delete the violating line. Rewrite in PASS form."` — "unambiguous three-step action sequence; no evaluator ambiguity" vs. V-01 borderline: "not three-step explicit" |
| C-24 | **Gate-to-section traceability in Phase 6 gate** — the Phase 6 completeness gate (GATE F or equivalent) explicitly names the review artifact sections it covers (Coverage, Structural records, Risk, Next Steps) by their stable IDs; an anonymous count assertion or generic "all sections" phrasing does not satisfy; creates verifiable traceability from gate assertion to artifact structure | V-02 C-21: "GATE F cites specific section IDs"; extends C-17 (named gate registry) into cross-section referencing within the Phase 6 gate |
| C-25 | **Slot 2 paraphrase violation examples in revert instruction** — Slot 2 revert-on-violation includes at least two quoted near-miss paraphrase examples (altered-token forms); relying on forbidden-form class labels or generic violation categories without concrete quoted examples does not satisfy; extends C-22 to cover both MOCK-ACCEPTED slots | V-03 C-22: "Slot 2 revert shifts from forbidden-form labeling to near-miss paraphrase examples; all examples are quoted altered-token forms" |

Scoring formula updated: aspirational denominator changes from 14 to 17. Aspirational pool = `(passes / 17) × 10`.

C-09 N/A cascade updated: if C-09 is absent → C-15 is N/A → C-20 is N/A → C-23 is N/A; denominator becomes 13 (17 − 4). C-24 and C-25 remain in denominator regardless of C-09 status.

Three new failure modes added (MA-21 to MA-23), one per new criterion.

The R4 ceiling: V-04 at 100.0 against v4 (14/14 aspirational). Against v5: V-04 passes C-24 (inherits V-02 Phase 6 GATE F with section IDs), fails C-23 (borderline two-step halt, not three-step explicit) and C-25 (Slot 2 paraphrase not extended from baseline) → 14/17 aspirational → (14/17) × 10 = 8.2 → **total: 98.2**. R5 variations must address C-23 and C-25 to push toward 100.

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

### Aspirational — pool of 10 pts · `(passes / 17) × 10`

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
| C-18 | Adjacent framed CONSTRAINT co-location | Each constrained field is immediately followed by a standalone framed `CONSTRAINT:` line; the constraint appears as a visually distinct block adjacent to its target field; inline embedding within template description text or preamble does not satisfy; applies to all phases containing constrained fields |
| C-19 | Universal blank-slot enforcement | Blank `___` targets appear in auto-flag rule output templates and in the CANARY ASSERTION, not only in MOCK-ACCEPTED slots; every evaluator fill-in site is structurally visible by inspection; bracket notation `[placeholder]` does not satisfy (looks filled even when unmodified) |
| C-20 | Halt-on-violation instruction | The forbidden-form enumeration (C-15) includes an explicit halt or stop instruction naming the action to take when a violation is detected; diagnostic enumeration alone (self-diagnosing without stop action) does not satisfy |
| C-21 | Per-section CONSTRAINT in review Write block | Each named section within the review artifact Write block carries its own co-located CONSTRAINT block; a single top-level Write instruction without per-section constraints does not satisfy; extends C-12 to the review artifact structure |
| C-22 | Slot 1 paraphrase violation examples in revert instruction | Slot 1 revert-on-violation includes at least two quoted concrete paraphrase examples (altered token forms); naming "paraphrase" as a violation class without examples does not satisfy |
| C-23 | Three-step halt sequence | The Standing Rule halt instruction names three sequential atomic steps using imperatives (HALT · DELETE · REWRITE or equivalent); two-step phrasing ("halt and rewrite") satisfies C-20 but not C-23; the three-step form eliminates evaluator discretion about intermediate steps; advisory phrasing or combined gerunds do not satisfy |
| C-24 | Gate-to-section traceability in Phase 6 gate | The Phase 6 completeness gate (GATE F or equivalent) explicitly names the review artifact sections it covers (e.g., Coverage, Structural records, Risk, Next Steps) by their stable IDs; an anonymous count assertion or generic "all sections" phrasing does not satisfy; creates verifiable traceability from gate assertion to artifact structure |
| C-25 | Slot 2 paraphrase violation examples in revert instruction | Slot 2 revert-on-violation includes at least two quoted near-miss paraphrase examples (altered-token forms); relying on forbidden-form class labels or generic violation categories without concrete quoted examples does not satisfy; extends C-22 to cover both MOCK-ACCEPTED slots |

**C-09 N/A cascade:** if C-09 is absent → C-15 N/A → C-20 N/A → C-23 N/A; active denominator becomes 13 (17 − 4). C-24 and C-25 are independent of C-09 status.

---

## Failure Modes

| ID | Criterion | Failure Pattern |
|----|-----------|----------------|
| MA-01 | C-01 | Auto-flag rules use "I found…" or evaluator-subject phrasing |
| MA-02 | C-02 | Forbidden triad incomplete; two-of-three accepted without completeness guard |
| MA-03 | C-03 | CANARY ASSERTION absent or CANARY SUPPRESSED branch undefined |
| MA-04 | C-04 | Review sections orphaned outside the single Write block |
| MA-05 | C-05 | Slot 1 / Slot 2 merged; paraphrase not named as violation class |
| MA-06 | C-06 | Role output uses yes/no verdicts without artifact citation template |
| MA-07 | C-07 | Accumulator lists unnamed; empty-list acknowledgment omitted |
| MA-08 | C-08 | REAL-REQUIRED template missing one or more of the 5 required fields |
| MA-09 | C-09 | No standing rule; evaluator-subject form present in phase output |
| MA-10 | C-10 | Tier sourcing omitted or implicit; source not named |
| MA-11 | C-11 | Phase transition proceeds without written count assertion |
| MA-12 | C-12 | CONSTRAINT appears only in preamble; not co-located at point of use |
| MA-13 | C-13 | Phase exit assertion absent or lacks N+M count; interleave not blocked |
| MA-14 | C-14 | Fill-in sites use `[bracket]` notation; absence requires prose parsing |
| MA-15 | C-15 | Standing rule states positive form only; forbidden alternatives not enumerated |
| MA-16 | C-16 | Gate language advisory-only; "Do not proceed until written" absent |
| MA-17 | C-17 | Gates unnamed or ordinal-only; IDs not referenceable across phases |
| MA-18 | C-18 | CONSTRAINT embedded inline within template prose; no adjacent framed block |
| MA-19 | C-19 | Auto-flag templates or CANARY use `[bracket]` notation; fill-in sites not structurally visible |
| MA-20 | C-20 | Forbidden-form enumeration enumerates violations without naming a stop action |
| MA-21 | C-23 | Halt instruction uses two-step or combined phrasing; three-step atomic sequence absent |
| MA-22 | C-24 | Phase 6 gate uses anonymous count assertion; review artifact section IDs not cited by name |
| MA-23 | C-25 | Slot 2 revert names violation class only; no quoted near-miss paraphrase examples |
