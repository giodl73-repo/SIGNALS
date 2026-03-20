Written to `simulations/quest/golden/discover-literature-golden-2026-03-19.md`.

**What's in it:**

- **Frontmatter** — exactly as specified (skill, skill_target, date, rounds, rubric_final, score: 235, status: GOLDEN)
- **Prompt body** — the simplified V-05 form (27% reduction, 1,530 words, all 30 aspirational criteria verified passing)
- **What made it golden** — 5 structural patterns that distinguish it from V-01 baseline:
  1. Inertia commitment housed in Phase 1 (not pre-phase) — the C-27(a) binding point is the token, not where prose lives
  2. C-38 cascade declaration in the enforcement contract — eliminates the 15-pt prediction gap V-04 surfaced
  3. Self-declaring lifecycle tokens with embedded grep instructions — single-grep verifiable per criterion, no cross-referencing
  4. Named C-29 Operationalization Verification block — independently required beyond distributed annotations (V-02 proved 40-pt cascade without it)
  5. C-36 analogy embedded in the structure that uses it — design rationale at point of demonstration
- **Final rubric summary** — all 38 criteria tabulated across essential / recommended / aspirational tiers, v20 ceiling 240
ma is authoritative.

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
Include frontmatter: skill: discover-literature, topic: {{topic}}, date: {{date}}, mode: {{mode}}, claims_checked: [n], sources_found: [n], high_risk_claims: [n]
```

---

## What Made It Golden

**1. Inertia commitment housed inside Phase 1 -- not pre-phase.**
The INERTIA SCENARIO lives in Phase 1, and PHASE 1 COMPLETE carries `inertia_committed=[yes]`. This satisfies C-27(a) at the lifecycle-token layer. V-03 proved that moving inertia to a pre-phase frame -- semantically equivalent -- breaks C-27(a) because the binding integration point is the PHASE 1 COMPLETE token, not wherever inertia prose appears. The golden prompt makes this architecture explicit and immovable.

**2. C-38 cascade declaration in the enforcement contract.**
The preamble names the cascade consequence of covering only one obligation: "C-17 -> C-19 -> C-21 cannot PASS if C-15 is PARTIAL." V-04 revealed a 15-point prediction gap when the cascade was not self-evident from the contract -- designers expected to lose 5 pts (C-15 alone) and lost 20. The golden prompt collapses that gap to zero by embedding consequence at the point of obligation definition.

**3. Self-declaring lifecycle tokens with embedded grep instructions.**
Each phase token carries its own compliance audit: criterion designators, self-declaring field names, and a single-grep instruction. No cross-referencing required. C-28 and C-29 are satisfied individually at each boundary before the consolidation block appears. Any criterion is verifiable by grepping one token.

**4. Named C-29 Operationalization Verification block as the single consolidation target.**
The block follows PHASE 4 COMPLETE and contains all six confirmations in one place. V-02 proved this named block is independently required beyond the distributed in-token annotations: omitting it fails C-30 and cascades through C-37 (8 x 5 = 40 pts). The golden prompt includes the block without treating it as optional elaboration.

**5. C-36 analogy embeds design rationale in the structure that uses it.**
"C-34 is to C-33 what C-25 is to C-23" appears inside the C-33 Compliance Declaration labeled sub-section -- exactly where a scorer reads about C-34. The recursive self-announcing principle (applied at the token layer by C-25, at the element-within-block layer by C-34) is stated where it is demonstrated, not in a separate note.

---

## Final Rubric Criteria Summary

**Rubric**: v20 | **Ceiling**: 240 pts (60 essential + 30 recommended + 150 aspirational)

### Essential (60 pts -- run fails without these)

| # | Criterion | Weight |
|---|-----------|--------|
| C-01 | Claims extracted before search -- 3+ distinct falsifiable claims with contrary-evidence notes | 10 |
| C-02 | Citation table present -- all 7 columns, non-placeholder rows | 10 |
| C-03 | Four-tier literature map built -- all four tier headings with >= 1 entry each | 10 |
| C-04 | Gap analysis recommendation issued -- support counts + PROCEED / SEARCH MORE / REFRAME CLAIM | 10 |
| C-05 | Artifact written with required frontmatter -- 6 fields, correct path | 10 |

### Recommended (30 pts -- output is better with these)

| # | Criterion | Weight |
|---|-----------|--------|
| C-06 | Contrary evidence mapped to claims -- CONTRARY entries reference claim numbers; Phase 5 names rebuttal direction | 10 |
| C-07 | WebSearch evidence visible -- 5+ sources with real authors, years 1990-2025, venue names | 10 |
| C-08 | High-risk claims flagged -- HIGH RISK block per flagged claim or explicit "none" | 10 |

### Aspirational (150 pts -- 30 criteria x 5 pts each)

| # | Criterion |
|---|-----------|
| C-09 | Depth mode source threshold met or THRESHOLD NOT MET token recorded |
| C-10 | Claim extraction interrogative completed (prior signals checked) |
| C-11 | Evidence type + counter-evidence fields in PHASE 1 COMPLETE |
| C-12 | RECOVERY NOTE typed schema with all three fields |
| C-13 | TIER EMPTY typed schema + tiers_empty_acknowledged in PHASE 3 COMPLETE |
| C-14 | Inertia named pre-search (Phase 1) and measured post-search (Phase 4) |
| C-15 | Both obligations named non-optional in enforcement contract preamble |
| C-16 | Named gate token at every phase boundary |
| C-17 | OBLIGATION A schema typed; failure class recoverable (depends C-15) |
| C-18 | OBLIGATION B schema typed; failure class auditable |
| C-19 | Recovery tokens auditable without YAML parsing (depends C-17) |
| C-20 | Token pairs each independently cover >= 2 distinct criteria |
| C-21 | Empty-tier tokens auditable without YAML parsing (depends C-19) |
| C-22 | Two unconditional lifecycle tokens (Phase 2 + Phase 3) |
| C-23 | Four lifecycle tokens covering all phase boundaries |
| C-24 | Independence verification: remove-either-pair test embedded |
| C-25 | N-of-4 counter embedded in every lifecycle token |
| C-26 | Remove-either-pair test named in verification block |
| C-27 | inertia_committed=[yes] in Phase 1 + inertia_verified=[yes] in Phase 4 |
| C-28 | Self-declaring signals at Phase 1 and Phase 4 boundaries |
| C-29 | Grep instructions embedded at both C-27 sub-clause boundaries |
| C-30 | Named C-29 Operationalization Verification block present |
| C-31 | PLACEMENT + CELL-SOURCE labeled fields in C-29 block |
| C-32 | Both labeled fields carry embedded grep instructions |
| C-33 | Four-element compliance declaration (a)-(d) present |
| C-34 | Per-element designator confirmations in C-33 declaration |
| C-35 | C-34 PASS declared within C-33 sub-section |
| C-36 | C-34/C-33 analogy to C-25/C-23 stated in C-33 sub-section |
| C-37 | Chain declaration C-14 + C-23 -> ... -> C-36 complete |
| C-38 | Enforcement contract declares single-obligation = PARTIAL and names cascade C-17 -> C-19 -> C-21 |
