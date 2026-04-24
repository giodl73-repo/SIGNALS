Written to `simulations/quest/rubrics/corps-build-rubric-v8-2026-03-16.md`.

---

Three new criteria extracted from R8, all scoring 100/100 across all five variations:

**C-24 -- Phase lifecycle boundary markers** (correctness, v8)
Every named phase emits a PHASE-ENTERED / PHASE-EXITED token as a discrete output line. Orthogonal to C-20 (single-purpose phase) and C-22 (named paths) -- those say what a phase does; C-24 says when it starts and ends. V-01/V-04/V-05 carry this; V-02/V-03 rely on headings as implicit boundaries.

**C-25 -- Resistance landscape as named contract artifact** (depth, v8)
The per-team resistance profiles from C-16 are compiled into a named fourth contract artifact (ARTIFACT-D) that enters the TRANSCRIPTION-RECEIPT and TRANSCRIPTION-CLEAR loops as a peer to the headcount table and analytic prose. V-02/V-04/V-05 re-audit four artifacts; V-01/V-03 re-audit three. C-25 makes that count difference scoreable.

**C-26 -- Named write passes with per-pass receipts** (correctness, v8)
The role-file write phase is decomposed into named passes (PASS-EXEC / PASS-SHARED / PASS-TEAM) each with a scope declaration and per-pass receipt. FINAL SUMMARY references pass-level receipts, not an aggregate total. Orthogonal to C-12 (IA-first ordering) -- C-26 applies to the entire write phase structure. V-03/V-05 carry this; V-01/V-02/V-04 use a single undifferentiated pass.

**Formula:** `aspirational_pass / 15 * 10` → `aspirational_pass / 18 * 10`
are compiled into a named fourth contract artifact
that enters the TRANSCRIPTION-RECEIPT and TRANSCRIPTION-CLEAR audit loops alongside the
headcount table, analytic prose, and org-chart structure. The scorecard C-19 and C-21 notes
confirm "four artifacts" for V-02/V-04/V-05 vs "three artifacts" for V-01/V-03, making the
structural distinction visible. C-25 makes this artifact-count difference scoreable.

**C-26** -- V-03 and V-05 both pass the full v7 rubric and share one axis absent from V-01,
V-02, and V-04: named write passes. C-12 requires IA files to be written before standard and
specialized roles. C-26 goes further: the entire role-file writing phase is decomposed into
named passes (PASS-EXEC, PASS-SHARED, PASS-TEAM or equivalent), each with an explicit scope
declaration and a per-pass completion receipt. The scorecard C-08 note confirms "WRITE-ROLES
three-pass receipts listed in FINAL SUMMARY role-files row" for V-03, making the per-pass
decomposition structurally distinct from a single-aggregate write confirmation.

**Formula:** `/15 -> /18`. Max aspirational points unchanged at 10.

---

## Essential Criteria (60 points total -- all must pass)

### C-01 -- Role file completeness
**Weight**: essential
**Category**: correctness
**Text**: Every role declared in org.yaml has a corresponding .roles/{area}/{role}.md
file. No declared role is missing. No extra files are generated for roles not in org.yaml.
**Pass condition**: Count of role files under .roles/ equals count of roles declared
in org.yaml. One-to-one correspondence between declared roles and generated files.

---

### C-02 -- org-chart.md with ASCII diagram
**Weight**: essential
**Category**: format
**Text**: The output includes an org-chart.md file. The file contains an ASCII tree diagram
that reflects the declared org structure (Division > Team > Sub-group) from org.yaml.
**Pass condition**: org-chart.md exists. An ASCII tree (using characters such as --, |,
+, or similar) is present. The tree depth and branch count reflect the nesting levels in
org.yaml.

---

### C-03 -- Inertia Advocate role present in every team
**Weight**: essential
**Category**: correctness
**Text**: The Inertia Advocate role exists in every team node declared in org.yaml. No team
is exempt. The role file must be present, not merely referenced in org-chart.md.
**Pass condition**: For every team in org.yaml, a file named inertia-advocate.md (or
equivalent canonical name) exists under .roles/{area}/. Count of teams in org.yaml
equals count of Inertia Advocate role files.

---

### C-04 -- org.yaml structural fidelity
**Weight**: essential
**Category**: correctness
**Text**: The generated role file directory tree reflects every declared group nesting level
(Division > Team > Sub-group) and every role assignment from org.yaml. No structural
reshuffling or flattening that was not in the input.
**Pass condition**: Directory structure under .roles/ maps 1-to-1 to the area/group
nesting in org.yaml. No area appears in .roles/ that does not exist in org.yaml. No
area declared in org.yaml is absent from .roles/.

---

### C-05 -- Role file typed fields present
**Weight**: essential
**Category**: coverage
**Text**: Every .roles/{area}/{role}.md file contains all five required typed fields:
orientation, lens, expertise, scope, and collaboration pattern. Placeholder text ("TBD",
empty section, omitted heading) is a fail.
**Pass condition**: Each role file contains all five headings with non-empty body text. A
file missing any single field fails this criterion for the full output.

---

## Recommended Criteria (30 points total -- output is better with these)

### C-06 -- Headcount by group/area table in org-chart.md
**Weight**: recommended
**Category**: depth
**Text**: org-chart.md includes a headcount table with one row per area/group showing
individual headcount plus a Total row. Level distribution (IC vs management, or explicit
level labels from org.yaml) is shown either in the same table or in a companion section.
**Pass condition**: Table present with at least two area rows and a Total row. Level
distribution visible as either a column, a sub-table, or a labeled distribution block.
Counts sum correctly to Total.

---

### C-07 -- Standard vs specialized role distinction honored
**Weight**: recommended
**Category**: correctness
**Text**: Role files correctly reflect whether a role is standard (shared across all teams),
specialized (team-specific), shared group-level, or exec office. The distinction is visible
in the role file's scope field or a role-type annotation -- not inferred only from directory
placement.
**Pass condition**: At least one role file for a standard role and at least one for a
specialized role each contain explicit scope or role-type language that differentiates them.
Exec office roles (if declared in org.yaml) are placed under an exec-office area, not
embedded inside a team area.

---

### C-08 -- AMEND section with three actionable options
**Weight**: recommended
**Category**: behavior
**Text**: The output includes an AMEND section listing exactly three amendment options the
user can invoke: (1) regenerate a specific area, (2) adjust level vocabulary, (3) change
group structure. Each option is concrete and references the relevant org.yaml element.
**Pass condition**: AMEND section present. Three distinct options listed. Each option names
a specific mechanism (area name, level term, group node) rather than a generic description.

---

## Aspirational Criteria (10 points total -- raise the bar)

### C-09 -- Inertia Advocate role files are team-contextualized
**Weight**: aspirational
**Category**: depth
**Text**: Each Inertia Advocate role file is customized to the specific team context: the
lens and expertise fields reference that team's domain, not a generic "status quo" boilerplate
copied across all teams.
**Pass condition**: No two Inertia Advocate role files share identical lens or expertise
body text. Each references at least one domain-specific term drawn from the team's declared
responsibilities in org.yaml.

---

### C-10 -- Cross-reference integrity between org-chart.md and .roles/
**Weight**: aspirational
**Category**: correctness
**Text**: Every role path referenced or implied in org-chart.md resolves to an actual file
in .roles/. The headcount total in the chart matches the count of generated role files.
**Pass condition**: Headcount total in org-chart.md equals the number of .roles/ files
generated (excluding any index or README files). No role mentioned in the chart is absent
from .roles/. No file in .roles/ is unmentioned in org-chart.md.

---

### C-11 -- Pre-write structural validation gate
**Weight**: aspirational
**Category**: correctness
**Source**: R1 excellence signal -- V-03 on C-04
**Text**: A dedicated VALIDATE phase runs before any role files or org-chart.md are written.
It checks: no duplicate team names, no role-name collision within a team, no area declared
in org.yaml with no roles. The build halts and reports failures before touching the
filesystem if any check fails.
**Pass condition**: The output narrative or step log shows an explicit validation phase
preceding the first file write. At minimum two structural checks are named (e.g.,
duplicate-name check, role-collision check). If validation fails, no files are written and
the failure names the specific node or role at fault.

---

### C-12 -- Inertia Advocate files written before standard and specialized roles
**Weight**: aspirational
**Category**: correctness
**Source**: R1 excellence signal -- V-01/V-04 on C-03
**Text**: All Inertia Advocate role files are generated either as the first file per team
or in a dedicated IA phase that completes before any standard or specialized roles are
written. This ordering makes IA omission structurally impossible -- an unstarted IA file
means the team is not yet begun, not silently skipped.
**Pass condition**: The output step sequence places every IA write before the first
standard or specialized role write for its team. Alternatively, a dedicated IA phase is
named and all IA files are confirmed complete before the standard-role phase begins. A
BUILD-COMPLETE or phase-gate block explicitly confirms IA coverage ("X of X teams covered")
at the end of the IA phase.

---

### C-13 -- Headcount table constructed as build contract before role files
**Weight**: aspirational
**Category**: depth
**Source**: R1 excellence signal -- V-02 on C-06
**Text**: The headcount table in org-chart.md is the first artifact produced, before any
.roles/ files are written. The file-writing phase derives its work items from the
table -- each row becomes a write target. This makes the table a contract between the
declared org structure and the generated file set rather than a post-hoc summary.
**Pass condition**: The output step log or narrative shows the headcount table written
prior to the first role file. The role-file writing phase references the table (or its
row count) as the source of its work list. Final totals in the table match the number
of role files produced.

---

### C-14 -- Org analytic narrative prose alongside headcount tables
**Weight**: aspirational
**Category**: depth
**Source**: R1 excellence signal -- V-05 on C-06
**Text**: The headcount section of org-chart.md includes 2-3 sentences of analytic prose
that interpret the numbers -- identifying the largest area by headcount, naming any
concentration in level distribution, flagging teams with no declared levels, and providing
a one-sentence seniority profile. The narrative adds interpretive value that the table rows
alone do not convey.
**Pass condition**: org-chart.md contains at least two prose sentences adjacent to (not
inside) the headcount tables. At least one sentence names a specific area or level finding
(e.g., "Platform Engineering accounts for 40% of total headcount"). Sentences are not
generic templates -- they reference actual values from the generated org.

---

### C-15 -- Inertia Advocate role file reads as person-portrait, not role template
**Weight**: aspirational
**Category**: depth
**Source**: R2 excellence signal -- V-03 on C-09 (highest qualitative signal across R1 and R2)
**Text**: Each Inertia Advocate role file is written at the level of a portrait -- describing
the specific kind of person who would occupy this role on this team, not a filled-in
template. Lens and expertise read as characterizations of a particular individual's
worldview, concerns, and specialized knowledge. Generic phrases such as "ensures stability,"
"advocates for continuity," or "resists unnecessary change" are absent. The file could not
be transplanted to a different team without substantive rewrite.
**Pass condition**: No IA role file contains generic resistance language applicable to any
team. Every lens entry describes a specific viewpoint anchored to this team's domain. Every
expertise entry names a concrete artifact, system, or practice this person would defend --
not a generic category. Optionally: a strong/weak example pair or annotated contrast is
present in the output (weak: "ensures process stability" vs strong: "guards the three-stage
review gate that prevented two P0s last quarter").

---

### C-16 -- Resistance profile extracted per team before IA files are written
**Weight**: aspirational
**Category**: depth
**Source**: R2 excellence signal -- V-04 on C-09 (strongest construction mechanism for
C-09 quality observed across all variations)
**Text**: Before writing any Inertia Advocate file, the build extracts a named resistance
profile for each team that identifies: (1) the specific system, process, or practice this
team's IA would defend, (2) the particular change pressure that threatens it, and (3) a
candidate lens phrase derived from those two. IA role file content is then constructed from
the profile -- not written from scratch. This makes team-specific lens and expertise
unreachable through boilerplate substitution.
**Pass condition**: The output step log or narrative contains a named resistance-profile
step that precedes the first IA file write. Each profile names a specific defended artifact
(e.g., "the nightly data reconciliation job" not "data stability"). Each profile names a
specific change pressure (e.g., "migration to streaming pipeline" not "rapid change"). The
IA role file's lens field traces back to language from the profile. Generic profiles
applicable to any team (e.g., "defends status quo against change") fail this criterion.

---

### C-17 -- CROSS-REF IA lens-phrase verification at build-complete
**Weight**: aspirational
**Category**: correctness
**Source**: R3 excellence signal -- V-05 Signal 3 (CROSS-REF C4: IA lens-phrase verbatim
trace at build-complete; differentiating signal for the only perfect-score variation in R3)
**Text**: A build-complete verification step confirms that every Inertia Advocate role
file's lens field opens with the exact lens phrase derived in the resistance profile (C-16).
This check runs after all files are written -- not at write time. It closes the C-16
derivation loop as a structural invariant: derivation is not merely claimed at
profile-extraction time but confirmed against the finished artifact. Any IA lens that drifts
from its profile phrase during file-writing is caught and named.
**Pass condition**: The output step log or narrative contains a named build-complete or
CROSS-REF step that executes after the last role file write. The step explicitly checks
each IA lens against its corresponding resistance profile lens phrase. At minimum the check
is stated as "lens phrase in [team] IA file matches profile: [phrase]" or equivalent
verbatim trace. A mismatch causes the build to flag the specific IA file and profile entry
by name.

---

### C-18 -- Contract verbatim transcription to org-chart.md
**Weight**: aspirational
**Category**: depth
**Source**: R3 excellence signal -- V-05 Signals 1+2 (headcount table as count target
before any file is written; analytic prose as Phase 3 output transcribed verbatim to
org-chart.md)
**Text**: The headcount table and analytic prose produced in the pre-role contract phase
are transcribed unchanged into org-chart.md. No revision or reformatting occurs between
the contract artifact and the user-visible document. This prevents drift between the build
contract (which constrains role-file count and content) and the final deliverable. A
variation that rewrites the table or prose at org-chart.md write time does not pass, even
if the final values are correct.
**Pass condition**: The output step log or narrative explicitly states that the headcount
table and analytic prose sections are copied or transcribed verbatim from the contract
phase artifact into org-chart.md -- not regenerated. The final org-chart.md headcount
total is numerically identical to the contract-phase count target. At least one prose
sentence in org-chart.md is traceable word-for-word to a phrase produced before the first
role file was written.

---

### C-19 -- TRANSCRIPTION-RECEIPT with per-artifact verdict and auto-correction
**Weight**: aspirational
**Category**: depth
**Source**: R4 excellence signal -- V-02 Signal on C-18 (highest-scoring variation in R4;
differentiates detect-drift from detect-and-correct-drift; a variation can pass C-18 by
asserting transcription occurred and fail C-19 by not emitting a per-artifact receipt with
a rewrite triggered on REVISED)
**Text**: At org-chart.md write time, the build emits a TRANSCRIPTION-RECEIPT that assigns
an explicit per-artifact VERBATIM/REVISED verdict to each contract artifact being
transcribed (at minimum: headcount table and analytic prose). If any artifact receives a
REVISED verdict -- indicating that content changed from the contract phase value -- a
rewrite step is triggered automatically before the phase completes. This makes transcription
self-correcting rather than merely drift-reporting: the phase cannot exit in a REVISED state.
**Pass condition**: The output step log or narrative contains a named TRANSCRIPTION-RECEIPT
or equivalent block at org-chart.md write time. Each contract artifact receives a stated
verdict (VERBATIM or REVISED). A REVISED verdict causes an explicit rewrite action to be
named -- not merely flagged. The phase output confirms no artifact remains in a REVISED
state when the phase closes. A variation that reports drift without correcting it fails
this criterion.

---

### C-20 -- BUILD-VERIFY as single-purpose phase with binary per-team verdict
**Weight**: aspirational
**Category**: correctness
**Source**: R4 excellence signal -- V-01 Signal on C-17 (differentiates phase isolation
from an embedded CROSS-REF subcheck; a variation can pass C-17 by checking IA lens inside
CROSS-REF and fail C-20 by not having a dedicated single-responsibility phase with one
binary verdict per team)
**Text**: The build-complete IA lens verification (C-17) is implemented as a dedicated,
single-purpose phase -- not embedded in CROSS-REF or any file-writing step. This phase has
exactly one responsibility: confirm each IA lens field matches its resistance profile phrase.
Each team in the org receives exactly one binary verdict (VERBATIM or DRIFT) in this phase
output. No file writes, structural integrity checks, summary generation, or other operations
occur within this phase. The phase gate closes only after all teams have received a verdict.
**Pass condition**: The output step log or narrative names a discrete phase whose stated
purpose is IA lens verification and nothing else. The phase produces one VERBATIM/DRIFT
verdict per team and no other outputs. The phase runs after all role files are written and
before any final output block (e.g., AMEND, summary, or CROSS-REF). A variation that
performs this check as a numbered subitem of CROSS-REF fails this criterion even if the
check itself is correct.

---

### C-21 -- TRANSCRIPTION-CLEAR as named structural re-audit gate before phase exit
**Weight**: aspirational
**Category**: depth
**Source**: R5 excellence signal -- V-01 PARTIAL on C-19 (V-01 triggers a rewrite on
REVISED but asserts TRANSCRIPTION-PASS without re-auditing the remaining artifacts; V-02
differentiates by naming a PHASE-EXIT GUARD that re-audits all three receipt verdicts
after any rewrite and gates CHART-WRITTEN on a named TRANSCRIPTION-CLEAR confirmation block)
**Text**: After any REVISED-triggered rewrite in the TRANSCRIPTION-RECEIPT phase (C-19),
the build emits a named re-audit block -- TRANSCRIPTION-CLEAR, PHASE-EXIT GUARD, or
equivalent -- that explicitly re-checks every contract artifact in a single pass, including
those that were already VERBATIM before the rewrite. This makes the exit guard structural
rather than behavioral: a TRANSCRIPTION-PASS assertion that covers only the rewritten
artifact fails this criterion. CHART-WRITTEN may not be emitted until the named block
confirms all artifacts are VERBATIM in that re-audit pass.
**Pass condition**: The output step log or narrative contains a named re-audit block that
runs after any rewrite and explicitly states a final verdict for every contract artifact --
not only the one that was rewritten. The block gates CHART-WRITTEN: CHART-WRITTEN is
emitted only after the block confirms all artifacts VERBATIM. A variation that asserts
TRANSCRIPTION-PASS without a named re-audit of all artifacts in a single pass fails this
criterion even if the rewritten artifact is correct. A variation where no REVISED verdict
ever occurs is exempt: if all artifacts are VERBATIM on first receipt, no re-audit block
is required.

---

### C-22 -- Named binary path structure for conditional execution
**Weight**: aspirational
**Category**: correctness
**Source**: R6 excellence signal -- V-02 differentiating signal on C-21 (PATH-A/PATH-B
labeling makes the exempt path and the obligation path structurally distinguishable as named
siblings; C-21 requires the re-audit gate; C-22 requires that the two conditional execution
paths are themselves named, so path identity is visible without re-reading the condition
logic)
**Text**: When a phase has two distinct conditional execution paths -- such as the
all-VERBATIM path (no rewrite needed) and the at-least-one-REVISED path (rewrite triggered)
-- each path is given an explicit label (PATH-A / PATH-B, or equivalent named identifiers).
The label appears in both the branch condition definition and in the phase output when that
path fires. The exempt path and the obligation path are named as peer structures, not as a
main case and an unnamed exception or an implied else clause. This makes which path fired
legible from the output alone, without tracing back through conditional logic.
**Pass condition**: The output step log or narrative names at least one conditional phase
with two labeled paths. Each path label appears in the phase output at the point where that
path executes. The exempt path (e.g., PATH-A: all artifacts VERBATIM, no re-audit block
needed) and the obligation path (e.g., PATH-B: at least one REVISED, re-audit block
required) each carry distinct names that function as identifiers. A variation that uses
unnamed conditional prose ("if all VERBATIM, skip; otherwise re-audit") fails this
criterion even if the conditional logic is correct.

---

### C-23 -- Declarative block-shape correctness rules
**Weight**: aspirational
**Category**: depth
**Source**: R6 excellence signal -- V-03 differentiating signal across C-17, C-20, C-21
(each named structural block declared with an explicit correctness rule in output-forward
terms; structural invalidity named for violations; the PARTIAL on C-08 confirms the pattern
by its absence: V-03 names the AMEND section but does not declare the three concrete option
shapes, leaving that block without a correctness rule)
**Text**: Each named structural block (TRANSCRIPTION-RECEIPT, TRANSCRIPTION-CLEAR,
BUILD-VERIFY, AMEND, or equivalent) has an explicit declarative correctness rule that states
what a well-formed instance of that block contains and what makes an instance structurally
invalid. The rule is stated in output-forward terms ("a correct X names all three artifacts")
rather than procedural terms ("the phase should emit X"). Structural violations are named as
structural invalidity -- not as behavioral failure or omission. The rule appears adjacent to
or within the block definition, making the block self-describing rather than dependent on a
preamble.
**Pass condition**: At least two named structural blocks in the output have associated
declarative correctness rules. At least one rule names a structural invalidity condition
by form (e.g., "a TRANSCRIPTION-CLEAR that names fewer than three artifacts is structurally
incomplete"; "a BUILD-VERIFY block with non-verdict content is structurally invalid"). Rules
use declarative framing ("a correct X is...") not procedural framing ("X must contain...").
A variation that describes what a phase does without declaring what a correct block instance
looks like fails this criterion for those blocks.

---

### C-24 -- Phase lifecycle boundary markers
**Weight**: aspirational
**Category**: correctness
**Source**: R8 excellence signal -- V-01/V-04/V-05 PHASE-ENTERED/PHASE-EXITED axis
(differentiates from V-02/V-03 which use phase headings as implicit boundaries; C-20
requires BUILD-VERIFY to be a single-purpose phase; C-22 requires conditional paths to be
named; C-24 is orthogonal: every named phase emits an explicit entry and exit token as a
discrete output line, making phase sequencing verifiable from the token stream alone without
reading phase body content)
**Text**: Each named phase in the build emits an explicit entry marker (PHASE-ENTERED or
equivalent) at the start of its execution and an explicit exit marker (PHASE-EXITED or
equivalent) at the end. These boundary tokens appear as discrete output lines -- not
embedded in heading prose or narrative. This makes phase sequencing structurally legible: an
observer can determine the precise start and end of each phase from the output token stream
without reading phase body content. A phase that begins with a heading and ends with its
last content line does not satisfy this criterion, even if it satisfies C-20's
single-responsibility requirement.
**Pass condition**: At least two named phases in the output emit explicit boundary tokens.
Each token identifies the phase by name (e.g., "PHASE-ENTERED: WRITE-ROLES" /
"PHASE-EXITED: WRITE-ROLES"). Entry and exit tokens appear as distinct output lines that
bracket the phase body -- not as the heading of the first section or the label of the last
action. A variation that uses phase headings or numbered steps as implicit boundaries fails
this criterion even if all phases have single-purpose responsibility.

---

### C-25 -- Resistance landscape as named contract artifact
**Weight**: aspirational
**Category**: depth
**Source**: R8 excellence signal -- V-02/V-04/V-05 ARTIFACT-D axis (differentiates from
V-01/V-03 which extract per-team resistance profiles at C-16 but do not compile them into a
named contract artifact; V-02/V-04/V-05 TRANSCRIPTION-CLEAR re-audits four artifacts
including ARTIFACT-D as a peer to headcount table and analytic prose; V-01/V-03 cover three
artifacts only; C-25 makes the artifact-count difference scoreable)
**Text**: The per-team resistance profiles extracted in the pre-IA phase (C-16) are compiled
into a named contract artifact -- resistance landscape, ARTIFACT-D, or equivalent -- before
any role files are written. This artifact enters the contract phase alongside the headcount
table and analytic prose and participates in the full TRANSCRIPTION-RECEIPT and
TRANSCRIPTION-CLEAR audit loops as a peer artifact. The TRANSCRIPTION-CLEAR block names the
resistance landscape explicitly when it re-audits all artifacts at phase exit. This elevates
resistance derivation from a behavioral input (profiles inform IA writing) to a structural
contract (the compiled landscape is transcription-audited at build-complete).
**Pass condition**: The output step log or narrative names a resistance landscape artifact
(or ARTIFACT-D equivalent) that is produced in the contract phase before any role file is
written. The TRANSCRIPTION-RECEIPT block assigns an explicit VERBATIM/REVISED verdict to
this artifact alongside the other contract artifacts. The TRANSCRIPTION-CLEAR re-audit
block names this artifact as one of the entries it re-checks. A variation that extracts
per-team profiles (satisfying C-16) but does not compile them into a named contract artifact
that enters the transcription audit loops fails this criterion.

---

### C-26 -- Named write passes with per-pass receipts
**Weight**: aspirational
**Category**: correctness
**Source**: R8 excellence signal -- V-03/V-05 PASS-EXEC/SHARED/TEAM axis (differentiates
from V-01/V-02/V-04 which write all role files in a single phase with a single aggregate
confirmation; C-12 requires IA-first write ordering; C-26 is orthogonal: the entire
role-file writing phase is decomposed into named passes covering distinct role categories,
each with its own scope declaration and per-pass receipt, referenced individually in the
FINAL SUMMARY)
**Text**: The role-file writing phase is decomposed into named passes -- such as PASS-EXEC
(executive roles), PASS-SHARED (shared/standard roles), and PASS-TEAM (team-specific roles),
or equivalent category labels -- each of which has a declared scope and produces an explicit
per-pass completion receipt confirming the files written in that pass. Each pass runs to
completion before the next begins. The FINAL SUMMARY role-files row references per-pass
receipts rather than a single aggregate file count. This makes the write phase per-segment
accountable rather than monolithic: a skipped pass is structurally visible as a missing
receipt, not silently absent from an aggregate count.
**Pass condition**: The output step log or narrative names at least two distinct write
passes covering different role categories. Each pass has an explicit scope declaration
(naming which role category it covers) and a per-pass completion receipt or count
confirmation. The FINAL SUMMARY role-files row references pass-level receipts rather than
a total-only count. A variation that writes all roles in a single undifferentiated pass
fails this criterion even if IA-first ordering (C-12) is satisfied and the total file
count is correct.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 18 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

---

## Criterion Summary

| ID   | Text (short)                               | Weight       | Category    | Added |
|------|--------------------------------------------|--------------|-------------|-------|
| C-01 | Role file completeness                     | essential    | correctness | v1    |
| C-02 | org-chart.md with ASCII diagram            | essential    | format      | v1    |
| C-03 | Inertia Advocate in every team             | essential    | correctness | v1    |
| C-04 | org.yaml structural fidelity               | essential    | correctness | v1    |
| C-05 | Role file typed fields present             | essential    | coverage    | v1    |
| C-06 | Headcount by group table + levels          | recommended  | depth       | v1    |
| C-07 | Standard vs specialized distinction        | recommended  | correctness | v1    |
| C-08 | AMEND section with three options           | recommended  | behavior    | v1    |
| C-09 | Inertia Advocate team-contextualized       | aspirational | depth       | v1    |
| C-10 | Cross-reference integrity chart/roles      | aspirational | correctness | v1    |
| C-11 | Pre-write structural validation gate       | aspirational | correctness | v2    |
| C-12 | IA-first write ordering                    | aspirational | correctness | v2    |
| C-13 | Headcount table as build contract          | aspirational | depth       | v2    |
| C-14 | Org analytic narrative prose               | aspirational | depth       | v2    |
| C-15 | IA role file as person-portrait            | aspirational | depth       | v3    |
| C-16 | Resistance profile as pre-IA artifact      | aspirational | depth       | v3    |
| C-17 | CROSS-REF IA lens-phrase at build-complete | aspirational | correctness | v4    |
| C-18 | Contract verbatim transcription            | aspirational | depth       | v4    |
| C-19 | TRANSCRIPTION-RECEIPT with auto-correction | aspirational | depth       | v5    |
| C-20 | BUILD-VERIFY as single-purpose phase       | aspirational | correctness | v5    |
| C-21 | TRANSCRIPTION-CLEAR structural re-audit    | aspirational | depth       | v6    |
| C-22 | Named binary path structure                | aspirational | correctness | v7    |
| C-23 | Declarative block-shape correctness rules  | aspirational | depth       | v7    |
| C-24 | Phase lifecycle boundary markers           | aspirational | correctness | v8    |
| C-25 | Resistance landscape as contract artifact  | aspirational | depth       | v8    |
| C-26 | Named write passes with per-pass receipts  | aspirational | correctness | v8    |

## Version History

| Version | Changes |
|---------|---------|
| v1 | Initial 10-criterion rubric (5 essential, 3 recommended, 2 aspirational) |
| v2 | Added C-11 through C-14 from R1 excellence signals; formula /2 -> /6 |
| v3 | Added C-15 and C-16 from R2 excellence signals (both on C-09 quality bar); formula /6 -> /8 |
| v4 | Added C-17 and C-18 from R3 excellence signals (both from V-05 perfect-score architecture); formula /8 -> /10 |
| v5 | Added C-19 and C-20 from R4 excellence signals (V-02 self-correcting transcription; V-01 phase isolation); formula /10 -> /12 |
| v6 | Added C-21 from R5 V-01 PARTIAL on C-19 (structural vs behavioral exit guard; TRANSCRIPTION-CLEAR re-audit block gates CHART-WRITTEN); formula /12 -> /13. V-03 phrasing-register axis deferred: empty aspirational table, no evidence to extract. |
| v7 | Added C-22 and C-23 from R6 excellence signals (V-02 PATH-A/PATH-B named binary path structure; V-03 declarative block-shape correctness rules); formula /13 -> /15. |
| v8 | Added C-24, C-25, and C-26 from R8 excellence signals (V-01/V-04/V-05 phase lifecycle boundary markers; V-02/V-04/V-05 resistance landscape as named contract artifact; V-03/V-05 named write passes with per-pass receipts); formula /15 -> /18. |
