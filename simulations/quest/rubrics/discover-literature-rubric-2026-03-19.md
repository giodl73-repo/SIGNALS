Rubric written to `simulations/quest/rubrics/discover-literature-rubric-2026-03-19.md`.

**Structure:**
- **5 Essential (C-01..C-05)** — claim extraction, citation table, four-tier map, gap analysis + recommendation, artifact with frontmatter
- **3 Recommended (C-06..C-08)** — contrary evidence mapped to claims, real WebSearch evidence visible, high-risk claims explicitly flagged
- **2 Aspirational (C-09..C-10)** — depth mode source threshold met, methodological precedent chain traceable

The golden bar requires all 5 essential to pass plus composite >= 80. The hardest essential to fake is C-05 (artifact on disk with populated frontmatter) — it catches runs that produced good prose but never wrote the file.
nd what contrary evidence would undermine it.

### C-02 Citation Table Present
- **Category**: format
- **Weight**: essential
- **Text**: Phase 2 produces a citation table with all required columns for each source found.
- **Pass condition**: At least one Markdown table appears with columns Title, Authors, Year, Venue, Claim #, Position (supports/contradicts/qualifies), and Key finding. Rows contain non-placeholder values.

### C-03 Four-Tier Literature Map Built
- **Category**: correctness
- **Weight**: essential
- **Text**: Phase 3 organizes sources into FOUNDATIONAL, RECENT, CONTRARY, and METHODOLOGICAL tiers, each with at least one entry and a one-sentence justification.
- **Pass condition**: All four tier headings appear; each tier has >= 1 cited source with a justification sentence. RECENT tier entries are dated 2020 or later.

### C-04 Gap Analysis Recommendation Issued
- **Category**: correctness
- **Weight**: essential
- **Text**: Phase 4 states claims with strong vs. weak support, lists contrary evidence to address, and issues a PROCEED / SEARCH MORE / REFRAME CLAIM recommendation.
- **Pass condition**: Output contains a gap analysis block with counts of supported vs. unsupported claims, at least one item under contrary evidence (or explicit "none"), and a clearly stated recommendation keyword (PROCEED, SEARCH MORE, or REFRAME CLAIM).

### C-05 Artifact Written with Required Frontmatter
- **Category**: behavior
- **Weight**: essential
- **Text**: Skill writes a signal artifact to the correct path with all required frontmatter fields.
- **Pass condition**: A file exists at signals/discover/literature/{topic}-literature-{date}.md (or the --output path). Frontmatter contains skill, topic, date, claims_checked, sources_found, and high_risk_claims fields, all populated with non-null values.

---

## RECOMMENDED Criteria (30 points -- output is better with these)

### C-06 Contrary Evidence Mapped to Claims
- **Category**: depth
- **Weight**: recommended
- **Text**: Phase 3 CONTRARY tier maps each contrary paper back to the specific claim it challenges, and Phase 5 identifies the single most dangerous contrary paper with a suggested response framing.
- **Pass condition**: Each CONTRARY entry references a claim number or label. Phase 5 item 2 names the contrary paper and proposes a rebuttal direction (scope qualification, methodological distinction, or domain limitation).

### C-07 WebSearch Evidence Visible
- **Category**: behavior
- **Weight**: recommended
- **Text**: The artifact shows evidence of actual WebSearch execution -- real titles, authors, years, and venues rather than generic placeholders.
- **Pass condition**: At least 5 distinct sources appear with real author names, publication years between 1990-2025, and venue names (journal, conference, or preprint server). No row contains placeholder text such as "Author et al." or "[title]".

### C-08 High-Risk Claims Flagged
- **Category**: coverage
- **Weight**: recommended
- **Text**: Any claim with no supporting literature and strong contrary evidence is explicitly flagged HIGH RISK with a scoping or reframing suggestion.
- **Pass condition**: If high_risk_claims >= 1 in frontmatter, the body contains a HIGH RISK block per flagged claim with a concrete suggestion (scope, qualify, or drop). If high_risk_claims = 0, the gap analysis explicitly states why no claim is at risk.

---

## ASPIRATIONAL Criteria (10 points -- raise the bar once essential/recommended are stable)

### C-09 Depth Mode Source Threshold Met
- **Category**: coverage
- **Weight**: aspirational
- **Text**: Source count meets the threshold for the active depth mode (quick >= 5, standard >= 15, deep >= 25).
- **Pass condition**: sources_found in frontmatter >= threshold for the active depth mode. Pass if threshold is met or exceeded.

### C-10 Methodological Precedent Chain
- **Category**: depth
- **Weight**: aspirational
- **Text**: The METHODOLOGICAL tier forms a traceable precedent chain -- each entry identifies the paper that established the method and its publication year, showing the method predates the current work.
- **Pass condition**: Each METHODOLOGICAL entry names the originating paper and includes a year. The chain shows the method was established before the current work (all years < current paper year).
