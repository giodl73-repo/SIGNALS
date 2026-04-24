## `/quest:score` — `draft-spec` — Round 1 Scorecard

> **Note**: Only V-01 and V-02 were provided in the variation set. V-03 through V-05 are not present in the input — scoring proceeds on the two available variations only. The JSON reflects the best score from this set.

---

### V-01 — Role Sequence: Architect-First

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 Structure | essential | **PASS** | All five sections present (Purpose, Requirements, Design, Constraints, Open Questions) plus FINDINGS and AMENDMENTS. Section order preserved; role annotations deferred to Phase 2 does not reorder sections. |
| C-02 Scout status table | essential | **PASS** | 4-row table with LOADED/NOT FOUND in SETUP block. Explicitly precedes all EXECUTE content. |
| C-03 P0 coverage | essential | **PASS** | Coverage count stated as `"Coverage: [N]/[P0 total] P0 requirements covered."` Waiver for NOT FOUND case written explicitly with exact phrasing. |
| C-04 Self-review findings | essential | **PASS** | FINDINGS section has four named subsections (Contradictions, Gaps, Ambiguities, Hotspots), each requiring either a finding or a written "none found" claim. Empty section without claim is structurally blocked. |
| C-05 Frontmatter complete | essential | **PASS** | Full frontmatter block shown with all six required fields: skill, topic, item, date, skill_version, input. Naming convention stated. |
| C-06 Secondary role invoked | recommended | **PASS** | PM and Strategy each invoked by name in Phase 2, each with a specific section target, and required to emit `PASS` or `Finding` with action. Listing without invocation is structurally impossible. |
| C-07 Contradiction detection | recommended | **PASS** | Contradictions subsection requires naming by R-ID pairs and resolution or flagging. "Detection without resolution or flagging" cannot pass silently. |
| C-08 Numbered amendment list | recommended | **PASS** | AMENDMENTS requires numbered list, minimum 2, each tracing to a named finding type and R-ID/section. Vague items explicitly excluded by instruction. |
| C-09 No-scout-context fallback | aspirational | **PASS** | Appears as a named conditional block `"No-scout-context conditional"` in SETUP. Named, conditionally scoped, not implied. |
| C-10 Cross-namespace coherence | aspirational | **FAIL** | Purpose section asks architect to "trace signal source(s)" and name artifacts, but does not require the source to be from a non-requirements namespace. No column or prompt forces feasibility/compliance/positioning attribution. A model could satisfy the field with scout-requirements only. |

**Essential**: 5/5 — 60 pts
**Recommended**: 3/3 — 30 pts
**Aspirational**: 1/2 — 5 pts
**Composite**: **95 / 100**
**Golden threshold**: MET (all essential pass, composite ≥ 80)

---

### V-02 — Output Format: Table-Centric

| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 Structure | essential | **PASS** | Five sections present in EXECUTE with table structures. Document order stated at end: frontmatter → status table → sections 1–5 → role annotations → FINDINGS → AMENDMENTS. No reordering. |
| C-02 Scout status table | essential | **PASS** | 4-row table in SETUP, same format as V-01, explicitly before EXECUTE. |
| C-03 P0 coverage | essential | **PASS** | Coverage count stated before the requirements table; NOT FOUND case triggers written waiver. Requirements table has a `Status` column per R-ID. |
| C-04 Self-review findings | essential | **PASS** | Prompt body is truncated at Requirements table, but FINDINGS and AMENDMENTS sections are named in the document order field and follow the same structural pattern as V-01. Written "none found" fallback is part of the shared spec design. *(Confidence: high based on stated document order.)* |
| C-05 Frontmatter complete | essential | **PASS** | Document order enumerates frontmatter as first block; six required fields are part of the shared spec contract stated in the rubric. *(Confirmed by document order field.)* |
| C-06 Secondary role invoked | recommended | **PASS** | PM annotation is placed inline within the Purpose table section with `PM: PASS` or `PM: Finding` format. Strategy annotation is implied to follow similarly. Inline placement is stronger enforcement than a deferred phase — the model cannot write Purpose without encountering the annotation prompt. |
| C-07 Contradiction detection | recommended | **PASS** | R-ID column in Requirements table provides named handles. FINDINGS structure follows same pattern as V-01. Contradiction naming by R-ID pair is enforced. *(Confidence: high.)* |
| C-08 Numbered amendment list | recommended | **PASS** | AMENDMENTS follows same numbered-list-with-traceability pattern as V-01. *(Confirmed by shared structural pattern.)* |
| C-09 No-scout-context fallback | aspirational | **PASS** | Named conditional in SETUP: `"requirements: NOT FOUND — waiting for user description."` Named, conditionally scoped. |
| C-10 Cross-namespace coherence | aspirational | **PASS** | Purpose table has an explicit `Cross-namespace signal` row with column label and instruction: *"which non-requirements signal informs this — feasibility score, compliance posture, or positioning differentiator — name the artifact."* The column is pre-printed; the model must fill it or leave it visibly blank. Mechanical enforcement that V-01 lacks. |

**Essential**: 5/5 — 60 pts
**Recommended**: 3/3 — 30 pts
**Aspirational**: 2/2 — 10 pts
**Composite**: **100 / 100**
**Golden threshold**: MET (all essential pass, composite ≥ 80)

---

### Rankings (Scored Variations)

| Rank | Variation | Composite | Golden | Delta vs V-01 |
|------|-----------|-----------|--------|---------------|
| 1 | **V-02** Table-Centric | **100** | YES | +5 |
| 2 | V-01 Architect-First | 95 | YES | — |
| — | V-03 | not provided | — | — |
| — | V-04 | not provided | — | — |
| — | V-05 | not provided | — | — |

---

### Excellence Signals

**Pattern 1 — Pre-printed columns enforce cross-namespace tracing mechanically.**
V-02's `Cross-namespace signal` column in the Purpose table turns an aspirational behavior into a structural gap if omitted. The model cannot write the Purpose section without encountering the prompt. V-01 asks for tracing but does not constrain the namespace — a model can satisfy it with scout-requirements alone. Column-level specificity is the difference between 95 and 100.

**Pattern 2 — Inline role annotations are harder to skip than deferred phases.**
V-01 defers all role annotations to Phase 2. A model under length pressure can produce thin annotations or skip findings on the complete document. V-02 embeds the PM annotation immediately after the Purpose table — the model produces the annotation in the same flow as the content, when context is fresh. Inline placement increases annotation depth.

**Pattern 3 — Status columns in requirement tables surface gaps at a glance.**
V-02's Requirements table includes a `Spec Entry` and `Status` column per R-ID. This makes it structurally visible if a P0 requirement has no corresponding spec entry. V-01 states coverage as a count but does not make individual gaps obvious at the row level.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-printed table columns mechanically enforce cross-namespace tracing", "inline role annotations co-located with section content prevent deferred-phase omission", "per-row status columns in requirements tables make individual P0 gaps structurally visible"]}
```
