Reading the scorecard carefully to extract the three excellence patterns from R15 V-01, V-02, V-03 — each closes one named gap. Then I'll produce the complete v10 rubric.

**Patterns extracted:**

- **C-33** from V-01: PERSPECTIVE AUDIT gate before Phase 6 + CHECK 8 re-validation from written files → closes Gap-A, C-08 moves PARTIAL → PASS
- **C-34** from V-02: per-slot `Phase 1 source: {row-id} = "{verbatim phrase}"` in FRAME FILL + CHECK 5 split (5A frame match, 5B source verifiable) → closes Gap-B, C-25 + C-27 move PARTIAL → PASS
- **C-35** from V-03: ROLE-REPLACE sub-procedure (4 fields + CONFIRMED gate) at every CHECK 3B/4B mismatch → closes Gap-C, C-24 moves PARTIAL → PASS

Formula: `/27 * 10`, each full pass = 0.370 pts.

---

```markdown
# crew-roles rubric — v10

## Changes from v9

Three new aspirational criteria extracted from R15 variations V-01, V-02, V-03. Each closes
a named gap identified in the R15 baseline assessment (Gap-A, Gap-B, Gap-C).

**C-33 — Perspective diversity gate** (from V-01):
C-08 (recommended) requires ≥ 3 distinct perspective values across written roles. A Phase 5
planning column satisfies C-08 only if the written output happens to cover three distinct
perspectives — no structural mechanism prevents Phase 6 from opening with fewer than three
planned. The sufficient condition is a two-part structural gate: (1) a PERSPECTIVE AUDIT
fires before Phase 6 opens, confirming that the planned role set includes ≥ 3 distinct
perspective values; (2) CHECK 8 in Phase 7 re-validates ≥ 3 distinct perspective values from
the actual written files. Advancing to Phase 6 without PERSPECTIVE AUDIT PASS is a blocking
error. C-08 requires correct output; C-33 requires the gate ran before authoring and the
check re-validated from written artifacts. V-01 (R15): PERSPECTIVE AUDIT gate fires before
Phase 6; CHECK 8 validates from written files; Gap-A closes; C-08 moves from PARTIAL to
PASS.

**C-34 — Phase 1 verbatim source citation in Frame Fill** (from V-02):
C-25 requires frame-slot source citations and C-27 requires forensic source-phrase tracing.
Citing CONVERGENCE SUMMARY satisfies neither — CONVERGENCE SUMMARY is a derived artifact,
not a primary Phase 1 source; citations to it are unverifiable against original inputs. The
sufficient condition is direct verbatim tracing: each FRAME FILL slot includes a `Phase 1
source: {row-id} = "{verbatim phrase}"` line, and CHECK 5 splits into 5A (frame slot matches
FRAME FILL output) + 5B (source citation present, row ID exists in Phase 1, verbatim phrase
verifiable). CHECK 5B must emit `[{slot}: Phase 1 source missing or unverifiable — CITATION
FAIL]` on any violation. C-25 requires source citation in FRAME FILL output; C-27 requires
forensic source-phrase tracing; C-34 requires both are structurally enforced per slot via
CHECK 5B. V-02 (R15): per-slot `Phase 1 source:` lines + CHECK 5A/5B split closes Gap-B;
C-25 and C-27 move from PARTIAL to PASS.

**C-35 — ROLE-REPLACE sub-procedure gate** (from V-03):
C-24 requires full audit-table re-evaluation after any role is replaced. Ad hoc re-evaluation
satisfies C-24 only if it happens to be complete — no structural mechanism ensures every
replacement event is recorded and all four re-evaluation fields are present. The sufficient
condition is a named sub-procedure: ROLE-REPLACE fires at every CHECK 3B / 4B mismatch
(scope or vocab binding failure that triggers a role change), recording four fields —
`planned`, `written`, `resolution`, `re-evaluation` — and emitting `ROLE-REPLACE CONFIRMED:
YES` when all four fields are present and the re-evaluation row is complete, or `ROLE-REPLACE
CONFIRMED: NO` otherwise. CHECK 3B and CHECK 4B cannot reach PASS status while any
ROLE-REPLACE CONFIRMED is NO. C-24 requires re-evaluation after replacement; C-35 requires
the ROLE-REPLACE sub-procedure ran and emitted CONFIRMED for every replacement event. V-03
(R15): ROLE-REPLACE sub-procedure fires at each mismatch, records all four fields, emits
CONFIRMED artifact; Gap-C closes; C-24 moves from PARTIAL to PASS.

**Formula updated**: `aspirational_pass / 27 * 10` (was `/24`). Each full pass = 0.370 pts.

---

## Criteria (full table)

### Essential (5)
C-01 All 5 fields | C-02 Inertia-advocate present | C-03 Correct output path |
C-04 Domain specificity | C-05 Minimum 3 roles

### Recommended (3)
C-06 Lens actionability | C-07 Collaborates_with resolves | C-08 Perspective diversity

### Aspirational (27)

| ID | Criterion | Introduced |
|----|-----------|------------|
| C-09 | Scope gradient | v1 |
| C-10 | Inertia domain-grounded | v1 |
| C-11 | Vocabulary-forced-field | v2 / R1 |
| C-12 | Inertia pre-characterization | v2 / R1 |
| C-13 | Registry summary table | v3 / R2 |
| C-14 | Scope-gradient-enforcement | v3 / R2 |
| C-15 | Verification-gate-phase | v3 / R2 |
| C-16 | Vocabulary-linked inertia Q&A | v4 / R3 |
| C-17 | Pre-write scope audit | v4 / R3 |
| C-18 | Vocabulary check in verification gate | v4 / R3 |
| C-19 | Inertia frame Q-slot template | v5 / R4 |
| C-20 | Q-domain-aligned vocabulary distribution | v5 / R4 |
| C-21 | Bucketed vocabulary extraction | v5 / R4 |
| C-22 | Domain-alignment audit table at Phase 2 exit | v5 / R4 |
| C-23 | Frame Fill as phase-boundary artifact | v5 / R4 |
| C-24 | Audit-table full re-evaluation after replacement | v6 / R5 |
| C-25 | Frame-slot source citation in Frame Fill output | v6 / R5 |
| C-26 | Four-failure-mode annotation gate | v7 / R12 |
| C-27 | Source-phrase forensic citation | v7 / R12 |
| C-28 | Five-failure-mode annotation gate | v8 / R13 |
| C-29 | Scope plan-to-write binding | v8 / R13 |
| C-30 | Inertia-first write order gate | v9 / R14 V-01 |
| C-31 | Vocab plan-to-write binding | v9 / R14 V-02 |
| C-32 | Inline per-role LENS AUDIT gate | v9 / R14 V-03 |
| **C-33** | **Perspective diversity gate** | **v10 / R15 V-01** |
| **C-34** | **Phase 1 verbatim source citation in Frame Fill** | **v10 / R15 V-02** |
| **C-35** | **ROLE-REPLACE sub-procedure gate** | **v10 / R15 V-03** |

---

## Criterion Definitions

### Essential

**C-01 All 5 fields**
Every role entry contains all five required fields: `name`, `scope`, `expertise`,
`orientation`, `collaborates_with`. A role with any field missing fails this criterion
regardless of all other scores.

**C-02 Inertia-advocate present**
At least one role is designated the inertia advocate. The role must be explicitly named or
labeled as such; the inertia advocate function cannot be inferred from scope text alone.

**C-03 Correct output path**
All role files are written to the correct output path as specified in the skill invocation or
program context. Files written to ad hoc or temporary paths fail this criterion.

**C-04 Domain specificity**
Role definitions must reference the specific domain of the topic under investigation. Generic
role templates applied without domain grounding fail this criterion.

**C-05 Minimum 3 roles**
The skill must produce at least 3 distinct, named roles. A single role split across multiple
files does not satisfy this criterion.

---

### Recommended

**C-06 Lens actionability**
`orientation.verify` must be phrased as a `?`-terminated question. `orientation.simplify`
must begin with an imperative verb. Both constraints must hold for every role in the output.

**C-07 Collaborates_with resolves**
Every name appearing in a `collaborates_with` field must correspond to a role that exists
in the output set. Forward references to roles not yet planned are permitted only if the
referenced role is subsequently written; dangling references fail this criterion.

**C-08 Perspective diversity**
The written role set must contain ≥ 3 distinct perspective values across all roles. Perspective
is determined by the orientation framing and scope positioning of each role, not by role name
alone.

---

### Aspirational

**C-09 Scope gradient**
Roles must exhibit a deliberate scope gradient from narrow/tactical to broad/strategic across
the role set. A flat scope distribution where all roles occupy the same layer fails this
criterion.

**C-10 Inertia domain-grounded**
The inertia advocate's scope or expertise must name at least one specific system, cost, or
habit from the domain under investigation (Phase 2 or equivalent). Generic inertia framing
("resistance to change") without domain anchors fails this criterion.

**C-11 Vocabulary-forced-field**
At least one role's `expertise.relevance` field must contain a term drawn directly from the
domain vocabulary extracted in Phase 3 or equivalent. The vocabulary term must be traceable
to the extraction step, not inserted post hoc.

**C-12 Inertia pre-characterization**
The inertia advocate role must be characterized before Phase 6 authoring begins. A
characterization block in Phase 2 or equivalent that names the inertia source, affected
system, and expected resistance vector satisfies this criterion.

**C-13 Registry summary table**
A summary table mapping each role to its key fields (at minimum: name, scope layer,
primary expertise domain) must appear as a phase-boundary artifact before the verification
gate.

**C-14 Scope-gradient-enforcement**
A mechanism must explicitly assign scope layers to planned roles before authoring begins.
Post-write scope relabeling does not satisfy this criterion; the layer assignment must precede
Phase 6.

**C-15 Verification-gate-phase**
A named verification gate must execute after all roles are written and before the skill
closes. The gate must check at minimum: field completeness, collaborates_with resolution,
and scope diversity. An ad hoc summary without a named gate fails this criterion.

**C-16 Vocabulary-linked inertia Q&A**
The inertia advocate's characterization block must include at least one Q&A pair that links
a domain vocabulary term to the specific inertia mechanism it represents. The Q&A must
appear before Phase 6.

**C-17 Pre-write scope audit**
Before any role is authored, a scope audit must confirm that planned roles span at least
two distinct scope layers. The audit must be recorded as a named step; implicit scope checks
embedded in prose fail this criterion.

**C-18 Vocabulary check in verification gate**
The verification gate (C-15) must include an explicit vocabulary coverage check confirming
that at least one domain vocabulary term appears in the written output. The check must be
a named item in the gate, not a post-gate observation.

**C-19 Inertia frame Q-slot template**
The inertia advocate's pre-characterization must use a structured Q-slot template with
named slots (e.g., `inertia_source:`, `affected_system:`, `resistance_vector:`). Free-form
prose characterization without named slots fails this criterion.

**C-20 Q-domain-aligned vocabulary distribution**
Vocabulary terms extracted for role planning must be distributed across at least two
distinct domain dimensions (e.g., technical, organizational, process). A vocabulary list
drawn entirely from one dimension fails this criterion.

**C-21 Bucketed vocabulary extraction**
Vocabulary extraction must produce named buckets grouping terms by dimension or theme.
A flat, unbucketed vocabulary list fails this criterion even if the terms are correct.

**C-22 Domain-alignment audit table at Phase 2 exit**
A domain-alignment audit table must appear at the exit boundary of Phase 2 (or equivalent
domain characterization phase), listing each planned role against the domain dimensions it
covers. The table must precede Phase 3 vocabulary extraction.

**C-23 Frame Fill as phase-boundary artifact**
The FRAME FILL output must be emitted as an explicit phase-boundary artifact — a named,
bounded block — before Phase 6 opens. Frame fill content embedded inline in Phase 6
authoring steps does not satisfy this criterion.

**C-24 Audit-table full re-evaluation after replacement**
When any role is replaced (scope mismatch, vocab binding failure, or equivalent), the
audit table must be fully re-evaluated for the replacement role. A partial re-evaluation
covering only the changed row fails this criterion; all table rows must be re-checked
against the replacement to confirm no downstream contamination.

**C-25 Frame-slot source citation in Frame Fill output**
Each slot in the FRAME FILL output must include a source citation identifying where the
frame content originated. A citation to a derived artifact (e.g., CONVERGENCE SUMMARY)
without tracing to the primary input fails this criterion.

**C-26 Four-failure-mode annotation gate**
The annotation gate must check for at least four named failure modes before the verification
gate (C-15) closes. The four modes must be listed by name in the gate output; an unstructured
scan for "issues" does not satisfy this criterion.

**C-27 Source-phrase forensic citation**
Each annotation or frame-slot citation must include the verbatim phrase from the source that
supports the annotation, not a paraphrase or summary. A citation that identifies a source
document without quoting the relevant phrase fails this criterion.

**C-28 Five-failure-mode annotation gate**
The annotation gate must check for at least five named failure modes. This criterion extends
C-26; a gate that checks exactly four modes satisfies C-26 but not C-28.

**C-29 Scope plan-to-write binding**
The Phase 5 (or equivalent) role planning table must include a `Planned-Scope-Layer` column.
CHECK 3B (or equivalent) must compare planned scope layer vs. written `scope` field per role
and emit `[{role}: planned {layer}, written scope diverges — SCOPE BINDING MISMATCH]` on
any violation. A post-write scope audit that detects the same divergence satisfies C-17 but
not C-29; the binding check must operate row-by-row against the planning table.

**C-30 Inertia-first write order gate**
A named `INERTIA-ADVOCATE WRITTEN` gate must fire before any other role is planned or
authored in Phase 6. The gate passes only when: (1) the inertia advocate file is confirmed
written and (2) the domain framing in that file contains at least one named system, cost,
or habit from Phase 2. Writing any other role before this gate passes is a blocking error.
C-10 requires the output to be domain-grounded; C-30 requires the structural gate ran first.
A correct inertia advocate written in open order satisfies C-10 but not C-30.

**C-31 Vocab plan-to-write binding**
The Phase 5 (or equivalent) role planning table must include a `Planned-Vocab-Term` column.
CHECK 4B (or equivalent) must compare planned vocab term vs. written `expertise.relevance`
field per role and emit `[{role}: planned {term}, written expertise.relevance lacks it —
VOCAB BINDING MISMATCH]` on any violation. CHECK 4A confirms overall vocabulary coverage;
C-31 / CHECK 4B confirms per-role binding. A post-write vocabulary scan that detects the
same gap satisfies C-11 / CHECK 4A but not C-31 / CHECK 4B.

**C-32 Inline per-role LENS AUDIT gate**
A `LENS AUDIT` block must execute immediately after each role is authored, before advancing
to the next role. The audit checks: (1) `orientation.verify` is `?`-terminated; (2)
`orientation.simplify` begins with an imperative verb. On any violation the gate must emit
`[LENS AUDIT FAIL: {role} — {dimension}: {issue}]` and block advancement until the
violation is resolved. C-06 requires correct output; C-32 requires the per-role gate ran
during authoring. A role set that satisfies C-06 via post-write fix does not satisfy C-32.

**C-33 Perspective diversity gate**
A named PERSPECTIVE AUDIT must fire before Phase 6 opens, confirming that the planned role
set includes ≥ 3 distinct perspective values. Additionally, CHECK 8 (or equivalent) must
re-validate ≥ 3 distinct perspective values from the actual written files in Phase 7 (or the
verification gate phase). Advancing to Phase 6 without PERSPECTIVE AUDIT PASS is a blocking
error. C-08 requires correct output; C-33 requires the pre-authoring gate ran and the
post-write check re-validated from written artifacts. A role set that satisfies C-08 without
the gate satisfies C-08 but not C-33.

**C-34 Phase 1 verbatim source citation in Frame Fill**
Each slot in the FRAME FILL output must include a `Phase 1 source: {row-id} = "{verbatim
phrase}"` line citing the specific Phase 1 input row and the exact phrase that grounds the
slot content. CHECK 5 must split into 5A (frame slot matches FRAME FILL output) + 5B
(source citation present, row ID exists in Phase 1, verbatim phrase verifiable). CHECK 5B
must emit `[{slot}: Phase 1 source missing or unverifiable — CITATION FAIL]` on any
violation. C-25 requires source citation; C-27 requires forensic phrase tracing; C-34
requires both are structurally enforced per slot by CHECK 5B. A FRAME FILL that cites only
CONVERGENCE SUMMARY or other derived artifacts satisfies neither C-25 nor C-34.

**C-35 ROLE-REPLACE sub-procedure gate**
A named ROLE-REPLACE sub-procedure must fire at every CHECK 3B / 4B mismatch that triggers
a role change. The sub-procedure must record four fields: `planned`, `written`, `resolution`,
`re-evaluation`. The sub-procedure must emit `ROLE-REPLACE CONFIRMED: YES` when all four
fields are present and the re-evaluation row is complete, or `ROLE-REPLACE CONFIRMED: NO`
otherwise. CHECK 3B and CHECK 4B cannot reach PASS status while any ROLE-REPLACE CONFIRMED
signal is NO. C-24 requires re-evaluation after replacement; C-35 requires the ROLE-REPLACE
sub-procedure ran and emitted CONFIRMED for every replacement event. An ad hoc re-evaluation
that produces correct output satisfies C-24 but not C-35.

---

## Scoring Formula

```
aspirational_score = (aspirational_pass / 27) * 10
```

Each aspirational criterion at full PASS contributes **0.370 pts**.

| Aspirational PASS | Score |
|-------------------|-------|
| 27 / 27 | 10.00 |
| 24 / 27 | 8.89 |
| 21 / 27 | 7.78 |
| 18 / 27 | 6.67 |

Essential criteria are pass/fail prerequisites; recommended criteria affect the recommended
score band independently of the aspirational formula.
```
