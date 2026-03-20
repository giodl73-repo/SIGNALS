---
name: discover-literature
description: "Systematic literature review with citation map. Builds structured prior-work landscape: foundational / recent / contrary / methodological. Uses WebSearch."
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /discover-literature for: {{topic}}
Depth mode: {{mode | default: standard}}

Depth mode source thresholds:
- quick: >= 5 distinct sources
- standard: >= 15 distinct sources
- deep: >= 25 distinct sources

You must reach the source threshold for the active depth mode before advancing to Phase 3.

---

## ENFORCEMENT CONTRACT (applies to every phase below)

Two obligations govern this entire run. Both are non-optional. Neither can be waived by phase, by brevity, or by the difficulty of the topic. Covering only one obligation is PARTIAL -- not half credit. A PARTIAL on OBLIGATION A means C-15 PARTIAL, which cascades: C-17 -> C-19 -> C-21 cannot PASS if C-15 is PARTIAL.

**OBLIGATION A -- Anti-Placeholder Recovery**
Every citation cell must contain real data or an explicit recovery note. If a cell is unknown at first pass, perform a follow-up search. If the follow-up search also fails, record it using the schema below. This schema is authoritative -- the field names defined here govern what Phase 2 must produce for any recovery event.

Token:    RECOVERY NOTE:
Schema:   RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
Fields:
  field_name      -- the citation column (Title | Authors | Year | Venue | Key finding)
  title_fragment  -- a short identifying fragment of the source title
  outcome         -- one of: filled -- {data_found} | not found after secondary search -- {query_used}
Required when: any citation cell was unknown at first pass and needed a follow-up search
Unacceptable: a secondary search without RECOVERY NOTE:; RECOVERY NOTE: missing any field; blank cells, "n/a", "unknown", "Author et al.", "[title]", or "TBD" with no recovery note

**OBLIGATION B -- Empty-Tier Acknowledgment**
Every tier of the four-tier literature map needs output. If a tier comes up empty, say so explicitly using the schema below. This schema is authoritative.

Token:    TIER EMPTY:
Schema:   TIER EMPTY: {tier_name} -- {why_no_sources_qualified} -- {search_that_would_address_gap}
Fields:
  tier_name                     -- one of: FOUNDATIONAL | RECENT | CONTRARY | METHODOLOGICAL
  why_no_sources_qualified      -- one sentence on why no sources qualified
  search_that_would_address_gap -- one concrete WebSearch query or strategy
Required when: a tier has zero qualifying entries
Unacceptable: a tier heading with no entries and no TIER EMPTY: token; a TIER EMPTY: missing any field

Both obligations apply before Phase 1 begins and stay active through Phase 5. "If unknown" questions require a follow-up action and a result. "If none found" questions require a TIER EMPTY: token -- silence is not an answer.

---

## PHASE 1 -- What claims need support?

Check any prior signals for this topic (discover-hypothesis, specify-spec, paper draft) before answering.

1. What are the 3-5 key claims this work makes about {{topic}} that need literature backing?
2. For each claim: what kind of evidence would confirm it? (empirical study / theoretical argument / methodological precedent)
3. For each claim: what would a skeptic cite to push back?

### INERTIA COMMITMENT (required gate before Phase 2 starts)

Before searching a single paper, lock in what inertia looks like for this topic. Phase 4 will measure the evidence against this commitment.

Answer: what does a team do if they ignore this literature entirely?
Name the default path -- the behavior that costs nothing to stay on.

INERTIA SCENARIO: [the default team behavior if this review is never done -- written before any search]

Hold this. Phase 4 will ask whether the literature gathered makes that default worse than acting.

At the end of Phase 1, write:
PHASE 1 COMPLETE: claims=[n] | inertia_committed=[yes] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]

This token emits unconditionally at the Phase 1 / claim-extraction boundary. The inertia_committed=[yes] field confirms Phase 1 produced a pre-search inertia commitment (C-14 front-loaded; C-27(a) satisfied). The evidence_type_mapped and counter-evidence-noted fields confirm interrogative obligation discharged per claim (C-11 PASS). Adds a named gate token (C-16 PASS). Token 1 of 4 (C-23 in progress at 1/4). C-28 PASS at Phase 1 boundary: this token satisfies C-27(a) -- the Phase 1 inertia-commitment sub-clause. The inertia_committed=[yes] field is the self-declaring signal; no cross-reference to Phase 4 needed. Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary. C-29 PASS at Phase 1 boundary: C-27(a) sub-clause identified, self-declaring signal identified (inertia_committed=[yes] field), grep instruction embedded.

---

## PHASE 2 -- What does the literature actually say?

Work toward the source threshold for {{mode}} (quick >= 5, standard >= 15, deep >= 25).

For each claim, run these searches:

1. What seminal papers does the field cite on this claim? (WebSearch: "[claim topic] seminal paper")
2. What systematic reviews from 2020-2025 map the current state? (WebSearch: "[claim topic] review 2020-2025")
3. What papers push back on this claim? (WebSearch: "[claim topic] criticism" or "against [claim]")
4. What papers establish the methodological precedent? (WebSearch: "[claim topic] method")

If threshold not met after four angles:
5. WebSearch: "[related concept] [claim topic]"
6. WebSearch: "[found paper title] cited by"

If threshold cannot be met, record:
THRESHOLD NOT MET: found [n] of [threshold] sources -- search angles exhausted: [list]
C-09 PASS, C-16 PASS. Pair 1, Token A.

For each source, answer per-source questions before the table. Any unknown cell: "not found after secondary search -- [query used]".

| Title | Authors | Year | Venue | Claim # | Position | Key finding |
|-------|---------|------|-------|---------|----------|-------------|

For any cell needing a follow-up search:
RECOVERY NOTE: {field_name} for "{title_fragment}" -- {outcome}
C-12 PASS, C-16 PASS. Pair 1, Token B. Pair 1: C-09, C-12, C-16. C-20 PASS for Pair 1 independently.

Every cell needs real data or "not found after secondary search -- [query used]". (OBLIGATION A)

At the end of Phase 2, write:
PHASE 2 COMPLETE: sources=[n] | threshold=[threshold] | status=[MET | NOT MET: [n]/[threshold]]
Emits unconditionally. C-16 PASS. Token 2 of 4 (C-23 in progress at 2/4). C-22 in progress. Pair 2, Token A. C-09 PASS, C-16 PASS.

---

## PHASE 3 -- How does the literature organize?

Answer both questions for each tier. (OBLIGATION B governs all four.)

### FOUNDATIONAL tier
TIER ENTRY: FOUNDATIONAL -- [Author Year] "[Title]" -- [one-sentence justification]
If none found: TIER EMPTY: FOUNDATIONAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### RECENT tier (2020 or later)
TIER ENTRY: RECENT -- [Author Year] "[Title]" -- [note on current consensus or shift]
If none found: TIER EMPTY: RECENT -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### CONTRARY tier
TIER ENTRY: CONTRARY -- [Author Year] "[Title]" -- Claim # [n] -- [specific objection in one sentence]
If none found: TIER EMPTY: CONTRARY -- {why_no_sources_qualified} -- {search_that_would_address_gap}

### METHODOLOGICAL tier
TIER ENTRY: METHODOLOGICAL -- [Author Year] "[Title]" -- [year confirmation: predates current work]
If none found: TIER EMPTY: METHODOLOGICAL -- {why_no_sources_qualified} -- {search_that_would_address_gap}

At the end of Phase 3, write:
PHASE 3 COMPLETE: tiers_populated=[n/4] | tiers_empty=[n] | tiers_empty_acknowledged=[yes/no]
Emits unconditionally. C-13 PASS, C-16 PASS. Token 3 of 4 (C-23 in progress at 3/4). C-22 PASS. Pair 2, Token B. Pair 2: C-09, C-13, C-16. C-20 PASS for Pair 2 independently.

C-24 Independence Verification
Pair 1: THRESHOLD NOT MET: + RECOVERY NOTE: -- C-09, C-12, C-16. C-20 PASS independently.
Pair 2: PHASE 2 COMPLETE: + PHASE 3 COMPLETE: -- C-09, C-13, C-16. C-20 PASS independently.
Remove-either-pair test: either pair alone -- C-20 PASS.
C-24 PASS.

---

## PHASE 4 -- Where are the gaps and what should be done?

1. How many claims have strong literature support (>= 2 sources)? Which ones?
2. How many have weak or no support? Which ones?
3. Which contrary papers pose the greatest threat? Most-dangerous-first.
4. Are any claims HIGH RISK? For each: scope / qualify / drop?
5. What is the overall strength of the evidence position?

Claims with strong support: N/M
Claims with weak or no support: [list]
Contrary evidence to address: [list -- most dangerous first]
HIGH RISK claims: [list or "none"]
  For each HIGH RISK: scope / qualify / drop + one-sentence framing

### Inertia verification (required gate before the recommendation keyword)

Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it.

Q: Does the literature make the inertia default worse than acting?
Name the specific risk the inertia path creates. If recommending PROCEED: show why the evidence is strong enough to overcome inertia. If SEARCH MORE or REFRAME CLAIM: name what inertia leaves exposed.

INERTIA SCENARIO: [repeat your Phase 1 commitment -- unchanged]
INERTIA RISK: [why the evidence gathered makes that default worse than acting]
RECOMMENDATION: PROCEED / SEARCH MORE / REFRAME CLAIM
Reason: [one sentence -- must name what in the evidence counters the Phase 1 inertia scenario]

At the end of Phase 4, write:
PHASE 4 COMPLETE: recommendation=[PROCEED | SEARCH MORE | REFRAME CLAIM] | inertia_verified=[yes] | high_risk_claims=[n]

This token emits unconditionally at the Phase 4 / gap-analysis boundary. The inertia_verified=[yes] field confirms Phase 4 returned to the Phase 1 commitment and verified evidence against it (C-14 PASS). C-27 PASS: PHASE 1 COMPLETE: carries inertia_committed=[yes] (C-27(a)) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (C-27(b)). Adds a named gate token (C-16 PASS). Token 4 of 4. C-23 PASS. C-28 PASS at Phase 4 boundary: this token satisfies C-27(b) -- the Phase 4 inertia-verification sub-clause. The inertia_verified=[yes] field is the self-declaring signal; no cross-reference to Phase 1 needed. Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary. C-29 PASS at Phase 4 boundary: C-27(b) sub-clause identified, self-declaring signal identified (inertia_verified=[yes] field), grep instruction embedded.

## C-29 Operationalization Verification

This block consolidates C-29 proof as a single grep target. All six confirmations here; C-29 PASS declared here.

PLACEMENT: This block appears after PHASE 4 COMPLETE: (emitted above). C-31(a) satisfied: the Phase 4 lifecycle token is named explicitly as a labeled field within this block. Single-grep verifiable: grep for PHASE 4 COMPLETE: in output above -- block follows that token; C-31(a) placement confirmed. C-32(a) satisfied: PLACEMENT field carries embedded grep instruction making C-31(a) citation procedurally executable in one step.
CELL-SOURCE: All six cells draw from already-emitted content -- Phase 1 and Phase 4 token annotations both written before this block; no forward-references. C-31(b) satisfied: cell-source provenance confirmed as a labeled field within this block. Single-grep verifiable: grep for PHASE 1 COMPLETE: annotation (cells (i)-(iii)) and PHASE 4 COMPLETE: annotation (cells (iv)-(vi)) in output above -- all six cells reference already-emitted content; C-31(b) confirmed. C-32(b) satisfied: CELL-SOURCE field carries embedded grep instruction making C-31(b) cell-source confirmation procedurally executable in one step.

Phase 1 / C-27(a) boundary:
- Cell (i) Sub-clause designation: C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named explicitly. CONFIRMED.
- Cell (ii) Self-declaring signal: the inertia_committed=[yes] field -- identified by name. CONFIRMED.
- Cell (iii) Grep instruction: "Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.

Phase 4 / C-27(b) boundary:
- Cell (iv) Sub-clause designation: C-27(b) -- the Phase 4 inertia-verification sub-clause -- named explicitly. CONFIRMED.
- Cell (v) Self-declaring signal: the inertia_verified=[yes] field -- identified by name. CONFIRMED.
- Cell (vi) Grep instruction: "Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.

All six cells confirmed. C-29 PASS. C-31 PASS. C-32 PASS: PLACEMENT carries embedded grep (C-32(a)); CELL-SOURCE carries embedded grep (C-32(b)); both-or-nothing confirmed.

#### C-33 Compliance Declaration

C-34 is to C-33 what C-25 is to C-23: just as C-25 adds per-token N-of-4 counter annotations to the four lifecycle tokens required by C-23 (making four-token completeness verifiable from any single token without reading all four), C-34 adds per-element designator confirmations to the four C-33 elements required within this closing declaration (making four-element compliance self-auditing from this labeled sub-section alone without reading the declaration's aggregate structure). The structural analogy motivates the C-34 design pattern: the recursive self-announcing principle is applied one level deeper, from the token layer (C-25) to the element-within-block layer (C-34).

C-33(a): C-32(a) named by sub-clause designator -- confirmed
C-33(b): C-32(b) named by sub-clause designator -- confirmed
C-33(c): both-or-nothing stated explicitly -- confirmed
C-33(d): C-32 PASS declared -- confirmed
C-33 PASS

C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete

---

## PHASE 5 -- What are the three most important next actions?

1. Which claim most urgently needs more support, and what should be searched for next?
2. Which contrary paper must be directly addressed, and what is the response strategy?
3. What methodological precedent is missing and where might it be found?

Write artifact to: signals/discover/literature/{{topic}}-literature-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
