Now I have the complete R2 picture. The prompt's scorecard (which I'm updating from) uses a different set of criteria than the actual file — these are two distinct rubrics in the same system. The prompt's V-05 scorecard rows are blank, so I need to work from V-01–V-04 excellence signals.

Here is the complete updated rubric v3:

---

# Rubric — mock-accept v3

## What changed from v2

Four new aspirational criteria (C-15 to C-18) extracted directly from R2 excellence signals:

| ID | Pattern | Source |
|----|---------|--------|
| C-15 | **Forbidden-form enumeration** — the artifact-as-subject standing rule explicitly names forbidden alternatives alongside the positive form (e.g., `FAIL: "I found…" / "This namespace has…"`) making the rule self-diagnosing | V-04 C-09 strongest evidence: "Standing rule at top: 'PASS: The mock artifact's [namespace] section [shows/records/lacks]…' FAIL: 'I found…' / 'This namespace has…'" |
| C-16 | **Written-gate blocking language** — phase exit assertions include "Do not proceed to Phase N+1 until written," making progression contingent on committed text, not just mental verification | V-04 C-13 evidence: "PHASE 0/1/2/3 EXIT ASSERTIONs explicit; each includes N+M count; 'Do not proceed to Phase N+1 until written'" |
| C-17 | **Named gate registry** — completeness gates carry stable sequential identifiers (GATE A, GATE B, GATE C…) forming a referenceable named registry across phases and review artifacts | V-02 C-11 evidence: "GATE A / B / C / D named blocking checkpoints — strongest C-11 implementation" |
| C-18 | **Constraint-field co-location** — the constraint block is physically adjacent to the field it governs with no intervening prose, headers, or instructions between constraint statement and fill-in target | V-03 C-12 evidence: "Framed CONSTRAINT block co-located with Field 1 — strongest C-12 implementation" |

Scoring formula updated: aspirational denominator changes from 6 to 10. The 10pt aspirational pool is now `aspirational_pass / 10 * 10`. The C-09 N/A note is updated to use denominator 9 when triggered.

Four new failure modes added (MA-13 to MA-16), one per new criterion.

The R2 ceiling (V-04 at 86.7) reflects passing C-09, C-11, C-12, C-13 but missing C-10 (tier sourcing) and C-14 (blank-line failure signal). Under v3, that same V-04 output would retroactively earn partial credit on C-15 and C-16 (both patterns visible in V-04's evidence), raising its effective ceiling — but C-15 and C-16 are now the challenge bar for future variations.

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

### Aspirational — pool of 10 pts · `(passes / 10) × 10`

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

**C-09 N/A rule**: If the variation contains no artifact-as-subject standing rule (rule is absent, not failed), score aspirational as `passes / 9 × 10` and mark C-09 as N/A. The C-15 criterion depends on C-09 being present; if C-09 is N/A, C-15 must also be N/A (denominator 8).

---

## Failure Modes

| ID | Criterion | Failure Pattern |
|----|-----------|-----------------|
| MA-01 | C-01 | Auto-flag rules use evaluator-as-subject: `"I found…"`, `"This section has…"`, `"There is no…"` |
| MA-02 | C-02 | One or more triad labels absent; two-of-three treated as complete |
| MA-03 | C-03 | Status writeback missing Edit call; or CANARY ASSERTION absent; or CANARY-FALSE-POSITIVE not named |
| MA-04 | C-04 | Next Steps placed outside Write block; Coverage table missing a column; Risk section absent; urgency labels absent |
| MA-05 | C-05 | MOCK-ACCEPTED slots merged into single block; or revert-on-violation absent for a slot; or paraphrase not named as violation |
| MA-06 | C-06 | Role output records verdict only; no "Required artifact citation" template; yes/no verdicts treated as satisfying entity-naming requirement |
| MA-07 | C-07 | Guard compliance produces narrative summary only; no named accumulator lists; empty list silently omitted rather than stated |
| MA-08 | C-08 | Role + verdict captured but 5-field template absent; trigger condition and/or Artifact state fields missing; VERDICT-ECHO not named |
| MA-09 | C-09 | No standing artifact-as-subject rule; evaluations drift to evaluator-as-subject with no structural correction |
| MA-10 | C-10 | No tier sourcing statement; instruction tier governing the phase is implicit or derived from context only |
| MA-11 | C-11 | No named completeness checkpoint; count check is narrative (`"looks complete"` / `"all present"`) without asserting the count |
| MA-12 | C-12 | Reason-code constraint present in preamble or instructions section only; not co-located with the column rule or checkbox at point of use |
| MA-13 | C-13 | No named phase exit assertions; phase transitions proceed without explicit N+M counts; auto-flag and evaluation phases may interleave |
| MA-14 | C-14 | Incomplete slots described in prose only; no fill-in blank pattern; structural incompleteness not visible without reading |
| MA-15 | C-15 | Artifact-as-subject rule states positive form only; forbidden alternatives not enumerated; evaluator must infer what counts as a violation |
| MA-16 | C-16 | Phase exit assertions present but expressed as advisory only (`"verify before continuing"`); no "until written" gate; written-text requirement absent |
| MA-17 | C-17 | Completeness gates unnamed or numbered only (Step 1, Step 2…); no stable GATE IDs enabling cross-phase reference or audit |
| MA-18 | C-18 | Constraint statement separated from fill-in target by prose, headers, or intervening instructions; co-location violated; constraint and target require separate navigation to locate |

---

## Scoring Formula

```
composite = (essential_pass / 5 × 60)
          + (recommended_pass × 10)
          + (aspirational_pass / 10 × 10)
```

| Tier | Weight | Criteria | Max |
|------|--------|----------|-----|
| Essential | 12 pts each | C-01 to C-05 | 60 |
| Recommended | 10 pts each | C-06 to C-08 | 30 |
| Aspirational | pool of 10 | C-09 to C-18 | 10 |
| **Total** | | | **100** |

**PARTIAL**: Counts as 0.5 pass toward numerator.

**C-09 N/A**: Denominator = 9; C-15 also forced N/A → denominator = 8.

**Essential cap**: Any Essential FAIL caps the composite at `(essential_pass / 5 × 60) + remainder`; a 4/5 essential pass caps Essential at 48, making 78 the maximum composite regardless of Recommended and Aspirational performance.

---

## Ceiling Analysis

| Round | Champion | Score | Aspirational ceiling note |
|-------|----------|-------|---------------------------|
| R1 | — | 95 | C-09 fails all variations; composite capped at 95 because no variation instructs artifact-as-subject grammar |
| R2 | V-04 | 86.7 (v2 scoring) | C-10 and C-14 unachieved; best combination was C-09 + C-11 + C-12 + C-13 |
| v3 target | — | 100 | Requires C-09 + C-15 (positive + forbidden forms); C-13 + C-16 (assertions + written-gate); C-11 + C-17 (inline check + named IDs); C-12 + C-18 (point-of-use + co-location); C-10 + C-14 (tier sourcing + blank lines) |
