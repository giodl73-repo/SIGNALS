Written to `simulations/quest/rubrics/corps-build-rubric-v4-2026-03-16.md`.

---

**What changed in v4:**

Two new aspirational criteria extracted from R3 scorecard, both from V-05 signals:

| ID | Pattern | Source |
|----|---------|--------|
| C-17 | CROSS-REF IA lens-phrase verification at build-complete | V-05 Signal 3 -- fourth CROSS-REF check; closes C-16 derivation loop as post-write structural invariant |
| C-18 | Contract verbatim transcription | V-05 Signals 1+2 -- table and prose written once in contract phase, transcribed unchanged to org-chart.md |

**Structural relationship between C-16, C-17, and C-18:**

- **C-16** (v3): extract resistance profile *before* IA write -- derivation step
- **C-17** (v4): verify lens phrase verbatim *after* all files written -- confirmation step
- C-16 + C-17 form a construction-then-verification pair. A variation can pass C-16 by having a profile phase and fail C-17 by not closing the loop at build-complete.

- **C-13** (v2): headcount table written before role files -- ordering
- **C-18** (v4): headcount table and prose transcribed unchanged into org-chart.md -- fidelity
- C-13 + C-18 form a contract-then-transcription pair. C-13 can be satisfied by early writes that are later revised; C-18 requires those values reach the final document unchanged.

**Score formula:** `aspirational_pass / 10 * 10` (was `/8`). Aspirational pool remains 10 points.
13 by writing the table early and then silently revising it before output.
- No other new patterns emerged from R3 that are not covered by existing criteria or excluded on mechanism-vs-output grounds.

**Score formula:** `aspirational_pass / 10 * 10` (was `/8`). Pool unchanged at 10 points.

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

### C-03 -- Inertia Advocate role present in every team*
**Weight**: essential
**Category**: correctness
*: The Inertia Advocate role exists in every team node declared in org.yaml. No team
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
**Source**: R2 excellence signal -- V-03 on C-09 (highest qualitative signal across R1
and R2)
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
file's lens field opens with the exact lens phrase derived in the resistance profile
(C-16). This check runs after all files are written -- not at write time. It closes the
C-16 derivation loop as a structural invariant: derivation is not merely claimed at
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

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
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

## Version History

| Version | Changes |
|---------|---------|
| v1 | Initial 10-criterion rubric (5 essential, 3 recommended, 2 aspirational) |
| v2 | Added C-11 through C-14 from R1 excellence signals; formula /2 -> /6 |
| v3 | Added C-15 and C-16 from R2 excellence signals (both on C-09 quality bar); formula /6 -> /8 |
| v4 | Added C-17 and C-18 from R3 excellence signals (both from V-05 perfect-score architecture); formula /8 -> /10 |
