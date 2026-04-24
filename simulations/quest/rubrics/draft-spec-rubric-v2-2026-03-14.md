Here is the complete updated rubric:

---

```
skill: quest:score
rubric_for: draft-spec
version: v2
date: 2026-03-14
source_rounds: R1
```

# Rubric — `draft-spec` — v2

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 5 | 25 |
| **Total** | **13** | **115** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 25)
```

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | Guided section structure preserved | essential | structure | All five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and appear in the prescribed order; reordering any section is a fail; appending extra sections after the prescribed set is allowed |
| C-02 | Scout artifact status table present | essential | structure | A status table with a row for each expected scout artifact appears in the SETUP block before any EXECUTE content; each row records LOADED or NOT FOUND; absence of the table is a fail even if the artifacts were used |
| C-03 | P0 requirement coverage | essential | coverage | Every P0 requirement from a loaded scout-requirements artifact maps to a named spec entry; coverage count is stated explicitly (e.g., "8/8 P0 requirements covered"); criterion is waived — not silently skipped — when no scout-requirements artifact exists, and the waiver is stated |
| C-04 | Self-review findings present | essential | behavior | A findings section explicitly addresses at least one of: contradictions, gaps, ambiguities, or hotspots; stating "none found" as a written claim is a pass; absence of the section, or producing an empty section without a written claim, is a fail |
| C-05 | Artifact frontmatter complete | essential | correctness | Output artifact follows `{topic}-spec-{date}.md` naming convention; frontmatter includes all required fields: skill, topic, item, date, skill_version, input |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | Secondary role validation | recommended | behavior | At least one secondary role (PM, Strategy, Compliance, or Design) is explicitly invoked to validate a named section and records PASS or a finding; listing role names without invoking them does not satisfy |
| C-07 | Contradiction detection and resolution | recommended | depth | Any conflicting requirements between loaded scout artifacts are identified by name (e.g., "R-06 vs R-10") and resolved or flagged with a proposed amendment; detection without resolution or flagging does not satisfy |
| C-08 | Actionable amendment list | recommended | depth | Phase 4 (Amend) produces a numbered list of at least 2 specific, actionable items that address gaps or ambiguities surfaced in the findings phase; vague items ("improve section 2") do not satisfy |

---

## Aspirational Criteria (25 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | No-scout-context fallback documented | aspirational | coverage | Spec explicitly documents behavior when no prior scout context is available (e.g., "ask 3–5 sentence description" or equivalent fallback prompt); fallback must appear as a named conditional in the spec, not implied by absence |
| C-10 | Cross-namespace coherence | aspirational | depth | At least one spec decision (constraint, design choice, or naming convention) is explicitly traced to a signal from a namespace other than scout-requirements (e.g., feasibility score, compliance posture, positioning differentiator), with the source artifact named |
| C-11 | Pre-printed cross-namespace column | aspirational | structure | The Purpose or Design section includes a pre-printed column or named row (e.g., "Cross-namespace signal") that requires the model to name a non-requirements artifact or leave the cell visibly blank; an instruction in prose to "name the artifact" does not satisfy — the column must be structurally present in the template so omission is immediately visible |
| C-12 | Role annotations inline with section content | aspirational | behavior | At least one secondary role annotation is embedded inline within its target section in the same content block, not deferred to a later phase or appended at document end; deferred-phase placement does not satisfy even if the annotation is complete |
| C-13 | Per-row P0 status column in requirements table | aspirational | coverage | The requirements section includes a table with a per-row Status or Spec Entry column that maps each P0 requirement ID to its corresponding spec entry by name; a coverage count or summary statement without per-row row-level traceability does not satisfy |

---

## Scoring

- Essential criteria C-01..C-05: 12 pts each, 60 pts total
- Recommended criteria C-06..C-08: 10 pts each, 30 pts total
- Aspirational criteria C-09..C-13: 5 pts each, 25 pts total
- **Grand total: 115 pts**
- All criteria are binary pass/fail at the stated weight

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric — 5 essential, 3 recommended, 2 aspirational (100 pts) |
| v2 | 2026-03-14 | Added C-11, C-12, C-13 from R1 excellence signals; aspirational pool grows to 25 pts; total 115 pts |

---

**Three decisions made in v2:**

1. **C-11 targets the enforcement mechanism, not the behavior.** C-10 already rewards cross-namespace tracing. C-11 rewards doing it via a pre-printed structural column — the distinction is whether omission is *visible* without reading. That's a different quality than C-10 and warrants a separate criterion.

2. **C-12 distinguishes inline from deferred.** C-06 rewards invoking a role at all. C-12 rewards co-location — the annotation appears in the same block as the content it validates. This is observable structurally and produces better annotations (context is fresh when the model writes it).

3. **Grand total grows to 115.** The aspirational pool expands from 10 to 25 pts rather than compressing 5 criteria into 10 pts (2 pts each would make them effectively invisible). The golden threshold of >= 80 is unchanged — a spec that passes all essential + all recommended already clears it comfortably, so the expanded pool raises the ceiling for excellence without moving the floor.
