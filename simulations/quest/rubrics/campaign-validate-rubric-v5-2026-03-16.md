Reading the scorecard carefully before writing.

Key observations from R4:

1. **V-01 C-17 PARTIAL** — Rogers cascade present but via sequencing logic, not deliberate schema architecture. Full criterion-cascade-by-schema requires the schema *itself* to be designed with criterion clusters in mind.

2. **V-02 Table 4** — Cross-signal synthesis encoded as a dedicated table with a per-row anti-concatenation constraint ("each row must name a relationship not visible in either sub-skill alone"). C-06 requires synthesis to exist; this encodes the rule at row granularity, not document level.

3. **V-02 full architecture** — Five separate tables, each with a single analytical purpose (sub-skill summary / ranked findings / P1 blockers+remediation / synthesis / Rogers segments). Collapsing two concerns into one table breaks the per-concern completeness gate. Generalizes C-19's row-skeleton pattern to the table level.

4. **V-01 C-10 PARTIAL vs V-02 C-10 PASS** — V-01 buries remediation in verdict-framing prose; V-02 encodes it as a required column in the dedicated blockers table. Applies C-18's column-as-inertia-enforcement to the remediation dimension: every P1 blocker gets a path, not just the ones the author chose to narrate.

Three new criteria: **C-20** (synthesis-table-with-per-row-anti-concatenation), **C-21** (one-table-per-analytical-concern), **C-22** (remediation-column-not-verdict-prose).

Scoring update: aspirational 11→14 criteria, 55→70 pts, max 145→160. Golden threshold unchanged at 80.

---

# campaign-validate Rubric — v5

> Updated after R4 scoring (V-01: 122, V-02: partial visible). Three new aspirational criteria
> added from R4 excellence patterns: synthesis-table-with-per-row-anti-concatenation (C-20),
> one-table-per-analytical-concern (C-21), remediation-column-not-verdict-prose (C-22).

---

## Quick Reference

**5 essential** (all must pass for golden):
- **C-01** — All 5 sub-skills represented. Common failure: listen-adoption silently skipped; review-customers substituted for review-code fails unconditionally.
- **C-02** — Findings ranked by *adoption impact*, not severity.
- **C-03** — Explicit go/no-go verdict. "It depends" without a condition fails.
- **C-04** — Top 3 blockers attributed to source sub-skill (trivially passes on go verdicts).
- **C-05** — Artifact written to `simulations/{topic}/validate-{date}.md`.

**3 recommended** (needed to reach composite >= 80):
- **C-06** — Cross-signal synthesis. Concatenation fails.
- **C-07** — Per-sub-skill labeled sections.
- **C-08** — Severity tiers (P1/P2/P3), not flat list.

**14 aspirational** (5 pts each):
- **C-09** — Adoption impact quantified: `(segment, ~N%)` format.
- **C-10** — Remediation paths per blocker.
- **C-11** *(v2)* — Table skeleton per sub-skill as completeness gate.
- **C-12** *(v2)* — Adoption Impact as dedicated column, separate from Severity.
- **C-13** *(v2)* — `Artifact written: ...` confirmation string.
- **C-14** *(v3)* — Categorical separation declared for listen-feedback vs listen-adoption.
- **C-15** *(v3)* — All five Rogers segments named with % anchors.
- **C-16** *(v3)* — Status-quo workaround cited per blocker.
- **C-17** *(v4)* — Schema designed so one decision satisfies a criterion cluster.
- **C-18** *(v4)* — Switching-cost comparison encoded as required columns, not prose.
- **C-19** *(v4)* — Required rows pre-declared so absent content is a visible blank, not missing prose.
- **C-20** *(v5)* — Synthesis encoded as a dedicated table with a per-row anti-concatenation rule.
- **C-21** *(v5)* — One table per analytical concern; no two concerns share a table.
- **C-22** *(v5)* — Remediation paths encoded as a required column in the blockers table, not verdict-section prose.

**Max: 160. Golden: all essential pass + composite >= 80.**

---

## What changed in v5

| ID | Pattern | What it encodes |
|----|---------|-----------------|
| C-20 | `synthesis-table-with-per-row-anti-concatenation` | Cross-signal synthesis is encoded as a dedicated table where each row must satisfy a named anti-concatenation constraint — for example, "names a relationship not visible in either sub-skill alone." The constraint operates at row granularity, not at document level. C-06 (recommended) requires synthesis to exist; C-20 requires it to be structurally enforced per row. A prose synthesis paragraph with a single cross-skill observation satisfies C-06 but fails C-20. The table form makes each relationship discrete and independently testable. |
| C-21 | `one-table-per-analytical-concern` | Each analytical concern — sub-skill coverage, ranked findings, P1 blockers+remediation, cross-signal synthesis, Rogers segments — has its own dedicated table with a single focus. Tables are not combined. A single mega-table covering multiple concerns, or ranked findings with a synthesis row appended, loses the per-concern completeness gate. Generalizes C-19's row-skeleton pattern to the table level: each concern gets its own structural container, and an absent table is a visually detectable gap rather than absent prose. |
| C-22 | `remediation-column-not-verdict-prose` | Remediation paths for P1 blockers appear as a required column in a dedicated blockers table — not as prose embedded in the verdict section. The column applies C-18's inertia-enforcement pattern to the remediation dimension: every P1 blocker receives a remediation path by construction, not only those the author chose to narrate. A variation that puts remediation in the CONDITIONAL GO framing only (V-01 pattern) passes C-10 partially but fails C-22. |

**Scoring model** updated: aspirational expands from 55 pts (11 criteria) to 70 pts (14 criteria), max composite moves from 145 to 160. Golden threshold unchanged at 80.

---

## Essential Criteria (weight: 12 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | All 5 sub-skills represented | completeness | Output contains explicit findings or a confirmed-empty section for all five sub-skills: review-design, review-users, listen-feedback, listen-adoption, review-code. Silent omission of any sub-skill — especially listen-adoption — fails unconditionally. Substituting review-customers for review-code also fails unconditionally. |
| C-02 | Findings ranked by adoption impact | ranking | The ranked findings list orders items by estimated adoption impact, not by severity or effort. A finding that blocks the early majority outranks a P1 usability issue that affects only innovators. Severity may be noted but must not govern rank order. |
| C-03 | Explicit go/no-go verdict | verdict | Output contains an unambiguous go or no-go verdict for the feature. A conditional verdict ("go if X is fixed") passes only if the condition is specific and actionable. "It depends" without a named condition fails. A variation that ends at the ranked-findings table without a verdict section fails unconditionally. |
| C-04 | Top blockers attributed to source sub-skill | attribution | The top 3 blockers (or all blockers if fewer than 3) are each attributed to the sub-skill that surfaced them. If verdict is go, this criterion passes trivially. |
| C-05 | Artifact written to disk | behavior | Output is written to `simulations/{topic}/validate-{date}.md` following the signal artifact naming convention. File must exist after skill run. |

---

## Recommended Criteria (weight: 10 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Cross-signal synthesis | depth | Brief identifies at least one pattern or tension appearing across 2+ sub-skills (e.g., a usability finding from review-users confirmed by a support-ticket prediction from listen-feedback). Not just a concatenation of sub-skill outputs. |
| C-07 | Per-sub-skill labeled sections | format | Each sub-skill's findings appear under a clearly labeled heading. Reader can navigate directly to review-design findings, listen-adoption findings, etc. without reading the whole document. |
| C-08 | Severity tiers | format | Findings are categorized using explicit P1/P2/P3 severity tiers with definitions. A flat, untiered list fails. |

---

## Aspirational Criteria (weight: 5 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Adoption impact quantified | depth | Each significant finding is tagged with an affected segment and rough % of total addressable user base: `(segment, ~N%)` format. Qualitative "many users" without quantification fails. |
| C-10 | Remediation paths per blocker | depth | Each top blocker includes a concrete remediation path — not just diagnosis. A variation that names blockers without any remediation guidance fails. |
| C-11 *(v2)* | Table skeleton per sub-skill | format | A pre-declared table skeleton exists for each sub-skill, with named rows for expected output types. A blank mandatory row is visually detectable; absent prose is not. |
| C-12 *(v2)* | Adoption Impact as dedicated column | format | A separate "Adoption Impact" column exists in the findings table, independent of and not derived from the Severity column. Merged columns or prose descriptions of impact fail. |
| C-13 *(v2)* | Artifact confirmation string | behavior | Output includes the exact string `Artifact written: simulations/{topic}/validate-{date}.md` as a confirmation. Missing or paraphrased confirmation fails. |
| C-14 *(v3)* | listen-feedback vs listen-adoption separation | format | listen-feedback and listen-adoption findings appear in categorically separate sections with an explicit prohibition against merging. Unlabeled co-mingling fails. |
| C-15 *(v3)* | All five Rogers segments named with % anchors | depth | All five Rogers adoption segments — Innovators, Early Adopters, Early Majority, Late Majority, Laggards — are named with associated % anchors in the listen-adoption analysis. Omitting any segment fails. |
| C-16 *(v3)* | Status-quo workaround cited per blocker | depth | Each top blocker identifies the status-quo workaround the affected segment uses today. A "Status-Quo Workaround" column in the findings table satisfies this. Omitting the workaround context fails. |
| C-17 *(v4)* | Schema designed as criterion cluster | structure | The table schema is deliberately architected so that one structural decision satisfies a cluster of criteria simultaneously. The design intent must be schema-level — not incidental sequencing logic. Example: pre-declaring Rogers rows causes C-09, C-14, and C-15 to pass by construction. Sequencing that produces cascade effects accidentally (V-01 pattern) earns partial credit at scorer discretion. |
| C-18 *(v4)* | Switching-cost comparison as required columns | structure | "Status-Quo Workaround" and "Switching Cost" are encoded as required table columns, not prose instructions. Both columns apply to every row — not just P1 blockers the author chose to narrate. |
| C-19 *(v4)* | Required rows pre-declared in skeleton | structure | Required entries (Rogers segments, sub-skills, severity tiers) are pre-declared as named rows in the table skeleton. A missing entry appears as a visually detectable blank mandatory row rather than absent prose. Generalizes C-11's skeleton pattern: the skeleton applies to rows as well as tables. |
| C-20 *(v5)* | Synthesis encoded as table with per-row anti-concatenation rule | structure | Cross-signal synthesis appears as a dedicated table (not prose) where each row must satisfy a named anti-concatenation constraint — e.g., "names a relationship not visible in either sub-skill alone." The constraint operates at row granularity: each row is independently testable. A prose synthesis paragraph satisfies C-06 but fails C-20. Minimum one compliant row required. |
| C-21 *(v5)* | One table per analytical concern | structure | Each analytical concern has its own dedicated table: sub-skill coverage summary, ranked findings, P1 blockers+remediation, cross-signal synthesis, and Rogers segment analysis each occupy separate tables. No two concerns share a table. A mega-table or a ranked-findings table with synthesis rows appended fails. An absent table for a required concern is a visually detectable gap. |
| C-22 *(v5)* | Remediation paths as required column, not verdict prose | structure | Remediation paths for P1 blockers appear as a required column in the dedicated blockers table — not embedded in the verdict section or conditional-go framing. Applies C-18's column-as-inertia-enforcement to the remediation dimension: every blocker row receives a path by construction. A variation with remediation only in verdict narrative (V-01 pattern) earns partial C-10 credit but fails C-22 unconditionally. |

---

## Scoring Reference

| Band | Points | Interpretation |
|------|--------|----------------|
| Essential | 5 × 12 = 60 | Must all pass for golden eligibility |
| Recommended | 3 × 10 = 30 | Needed for composite ≥ 80 |
| Aspirational | 14 × 5 = 70 | Differentiate strong from exceptional outputs |
| **Max** | **160** | |
| **Golden threshold** | **≥ 80 composite + all essential pass** | |

## Pass/Fail Reference

| Variation | Essential | Rec | Asp | Composite | Golden? |
|-----------|-----------|-----|-----|-----------|---------|
| V-01 (R4) | 48 / 60 | 30 / 30 | 44 / 55* | 122 / 145* | NO — C-01 fails |
| V-02 (R4) | 24 / 60 | 30 / 30 | partial | — | NO — C-01, C-03, C-05 fail |
| V-05 (R3 top) | — | — | — | 125 / 130* | YES (v3 scale) |

\* Scored on v3 or v4 scale; v5 max is 160.
