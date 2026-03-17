## Round 3: mock-ns Scoring (Rubric v3)

### Scoring Criteria Summary

**Essential (60 pts):** C-01 header complete, C-02 category correct, C-03 golden structure, C-04 flag present and correct, C-05 path convention
**Recommended (30 pts):** C-06 default skill, C-07 fidelity warning, C-08 next-step line
**Aspirational (10 pts, /7):** C-09 tier-conditional flag, C-10 TOPICS.md emit, C-11 FLAG as named step, C-12 topic-status exclusion, C-13 FIDELITY CONTEXT lead, C-14 dual-site immutability, C-15 structural exclusion column

---

### V-01 — FLAG Site-Boundary Gate

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | All seven header fields present; Flag included |
| C-02 | essential | PASS | Category table maps to EVIDENCE-HEAVY / MIXED / HIGH-STRUCTURE correctly |
| C-03 | essential | PASS | A-3 requires skill-specific headings and all structural elements; reader-recognition check present |
| C-04 | essential | PASS | Flag field in header; S-4 logic covers all four category branches including compliance override |
| C-05 | essential | PASS | `{namespace}` in filename explicitly; skill-id excluded from path |
| C-06 | recommended | PASS | Default table present; topic → topic-plan (not topic-status) |
| C-07 | recommended | PASS | All three category warnings present; HIGH-STRUCTURE carries "REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen)" |
| C-08 | recommended | PASS | A-4 closing line: `Next: /mock:review {topic} {artifact path}` |
| C-09 | aspirational | PASS | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` for critical namespace branch in S-4 |
| C-10 | aspirational | PASS | Dedicated emit: `> TOPICS.md: {found -- topic {topic} registered, tier: {N}, compliance: ...}` |
| C-11 | aspirational | PASS | S-4 is a discrete named step; "The header assembly step (A-1) will copy FLAG from this step — it will not compute it" |
| C-12 | aspirational | PASS | Three-column table includes "Do NOT use topic-status. Hard exclusion: meta-structural..." in Exclusion column |
| C-13 | aspirational | PASS | A-2 opens with "This is the first section of the artifact body... before the reader encounters any skill-specific content. Delimited by `---` on both sides." |
| C-14 | aspirational | PASS | Compute site close (S-4): "Step S-4 is now complete. FLAG is final. Do not modify FLAG after this emit. Do not re-evaluate or re-derive FLAG in any subsequent step." Header site open (A-1): "FLAG was computed and finalized in S-4. Do not re-derive it here. The first rule of this step is: copy FLAG from S-4 verbatim." Both sites carry at-site prohibition. |
| C-15 | aspirational | PASS | Named "Exclusion" column in three-column table; topic row carries hard-constraint exclusion |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 7/7 × 10 = **10**
**Composite: 100**

---

### V-02 — FLAG RESOLUTION BLOCK

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | All seven fields; Flag references RESOLUTION BLOCK |
| C-02 | essential | PASS | Category classification table correct |
| C-03 | essential | PASS | Section 3 requires skill-specific headings, all structural elements; reader-recognition check |
| C-04 | essential | PASS | Flag in header; four-branch resolution including compliance override in RESOLUTION BLOCK |
| C-05 | essential | PASS | `{namespace}` in filename; "NOT `{skill-id}`" stated explicitly |
| C-06 | recommended | PASS | Default table; topic → topic-plan with exclusion note |
| C-07 | recommended | PASS | FIDELITY CONTEXT with all three variants; HIGH-STRUCTURE carries "REAL-REQUIRED at Tier 2+ for critical namespaces" |
| C-08 | recommended | PASS | Closing line present |
| C-09 | aspirational | PASS | Critical-namespace tier branch in RESOLUTION BLOCK |
| C-10 | aspirational | PASS | Dedicated `> TOPICS.md: {...}` emit |
| C-11 | aspirational | PASS | FLAG RESOLUTION BLOCK is a discrete structural step sequenced before header assembly section |
| C-12 | aspirational | PASS | Three-column Exclusion table; "Do NOT use topic-status -- excluded as meta-structural..." |
| C-13 | aspirational | PASS | Section 2 FIDELITY CONTEXT "appears immediately after the MOCK ARTIFACT header block and before any skill-specific content. Delimited by `---` on both sides." |
| C-14 | aspirational | PASS | Compute site: block preamble "FLAG is final and MUST NOT be recomputed anywhere in this run" + block close "STATUS: LOCKED -- do not modify FLAG after this line." Header site: "Do not compute a new flag value here. Do not re-derive it. Copy the locked value verbatim from the FLAG RESOLUTION BLOCK." Dual-site prohibition present. |
| C-15 | aspirational | PASS | Named "Exclusion" column; topic row carries exclusion constraint |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 7/7 × 10 = **10**
**Composite: 100**

---

### V-03 — MUST NOT Prohibition Register

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | All seven fields; MUST NOT language on Flag field itself |
| C-02 | essential | PASS | Category table present and correct |
| C-03 | essential | PASS | Step 8 requires skill-specific headings; "MUST NOT write generic prose where the skill produces structured output" |
| C-04 | essential | PASS | Flag in header from Step 4; four-branch table in Step 4 |
| C-05 | essential | PASS | Path correct; "MUST NOT use `{skill-id}` in filename" |
| C-06 | recommended | PASS | Default table; topic → topic-plan; MUST NOT use topic-status |
| C-07 | recommended | PASS | All three variants; HIGH-STRUCTURE "REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen)" |
| C-08 | recommended | PASS | Step 9 next-step line present |
| C-09 | aspirational | PASS | Critical-namespace row in Step 4 table |
| C-10 | aspirational | PASS | `> TOPICS.md: {result}` in Step 1 |
| C-11 | aspirational | PASS | Step 4 dedicated "Compute FLAG" step; Step 6 header references "FLAG from Step 4" |
| C-12 | aspirational | PASS | Three-column Exclusion table; "MUST NOT use topic-status. Hard exclusion..." |
| C-13 | aspirational | PASS | Step 7: "This is the first section of the artifact body, before any mock body content. Delimited by `---` on both sides." |
| C-14 | aspirational | PASS | Compute site close (Step 4): "FLAG is final. MUST NOT modify FLAG after this emit. MUST NOT re-derive FLAG in any subsequent step, including header assembly." Header site open (Step 6): "FLAG was computed in Step 4 and is final. MUST NOT re-derive FLAG here. Copy it verbatim from Step 4." Both sites use MUST NOT. |
| C-15 | aspirational | PASS | Named "Exclusion" column; MUST NOT language in topic row |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 7/7 × 10 = **10**
**Composite: 100**

---

### V-04 — Structural Gate + MUST NOT

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | All seven fields; A-1 GATE explicitly guards header block |
| C-02 | essential | PASS | Category table correct |
| C-03 | essential | PASS | A-3 requires skill-specific structure; reader-recognition check |
| C-04 | essential | PASS | Flag from S-4; four-branch logic; compliance override present |
| C-05 | essential | PASS | `{namespace}` in path; "MUST NOT use `{skill-id}`" |
| C-06 | recommended | PASS | Default table; topic → topic-plan; MUST NOT language in Exclusion column |
| C-07 | recommended | PASS | A-2 FIDELITY CONTEXT complete with all three variants; HIGH-STRUCTURE "REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen)" — fullest template of any variation |
| C-08 | recommended | PASS | A-4 closing line present |
| C-09 | aspirational | PASS | Critical namespace branch in S-4 |
| C-10 | aspirational | PASS | Dedicated `> TOPICS.md: {...}` emit in S-1 |
| C-11 | aspirational | PASS | S-4 "Resolve FLAG in this step"; A-1 header references S-4 emit |
| C-12 | aspirational | PASS | Three-column table; "MUST NOT use topic-status -- hard exclusion: meta-structural" |
| C-13 | aspirational | PASS | A-2: "first section of the artifact body... Delimited by `---` on both sides" |
| C-14 | aspirational | PASS | **S-4 GATE**: "-- S-4 GATE -- FLAG IS FINAL. MUST NOT modify FLAG after this emit. MUST NOT re-evaluate or re-derive FLAG in any step that follows. --" **A-1 GATE**: "-- A-1 GATE -- MUST NOT re-derive FLAG here. FLAG was finalized in S-4. Copy it verbatim from the S-4 emit. --" Named gate markers at both sites using MUST NOT — maximum enforcement. |
| C-15 | aspirational | PASS | Named "Exclusion" column; MUST NOT in topic row |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 7/7 × 10 = **10**
**Composite: 100**

---

### V-05 — FLAG RESOLUTION BLOCK + FIDELITY CONTEXT + Inertia Framing

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | All seven fields; Flag references RESOLUTION BLOCK |
| C-02 | essential | PASS | Category table correct |
| C-03 | essential | PASS | Section 3 requires skill-specific structure; reader-recognition check |
| C-04 | essential | PASS | Four-branch resolution in RESOLUTION BLOCK including compliance override |
| C-05 | essential | PASS | `{namespace}` in path; "NOT `{skill-id}`" |
| C-06 | recommended | PASS | Default table; topic → topic-plan with inertia-cost exclusion note |
| C-07 | recommended | PASS | FIDELITY CONTEXT with all three variants; HIGH-STRUCTURE "REAL-REQUIRED at Tier 2+ for critical namespaces"; each warning includes "What you can trust / What you cannot trust / Inertia risk" structure — richest warning block of any variation |
| C-08 | recommended | PASS | Closing next-step line present |
| C-09 | aspirational | PASS | Critical-namespace tier branch in RESOLUTION BLOCK |
| C-10 | aspirational | PASS | Dedicated `> TOPICS.md: {...}` emit |
| C-11 | aspirational | PASS | RESOLUTION BLOCK is a discrete structural step before header assembly |
| C-12 | aspirational | PASS | Three-column Exclusion table; topic row carries inertia-cost exclusion: "zero new signal, zero readiness advance" |
| C-13 | aspirational | PASS | Section 2: "first body section of the artifact, delimited by `---` on both sides. Do not position this section after the mock body." |
| C-14 | aspirational | PASS | Compute site: preamble "FLAG is final and MUST NOT be recomputed anywhere in this run" + block close "STATUS: LOCKED -- do not modify FLAG after this line." Header site: "Do not compute a new flag value here. Do not re-derive it. Copy the locked value verbatim." Dual-site prohibition. |
| C-15 | aspirational | PASS | Named "Exclusion" column; inertia-cost language in topic row |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 7/7 × 10 = **10**
**Composite: 100**

---

### Scorecard

| V | Essential | Recommended | Aspirational | Composite | Band |
|---|-----------|-------------|--------------|-----------|------|
| V-01 | 5/5 (60) | 3/3 (30) | 7/7 (10) | **100** | Gold |
| V-02 | 5/5 (60) | 3/3 (30) | 7/7 (10) | **100** | Gold |
| V-03 | 5/5 (60) | 3/3 (30) | 7/7 (10) | **100** | Gold |
| V-04 | 5/5 (60) | 3/3 (30) | 7/7 (10) | **100** | Gold |
| V-05 | 5/5 (60) | 3/3 (30) | 7/7 (10) | **100** | Gold |

**Round 3 verdict: all five variations achieve 100. The stability hypothesis is confirmed.** C-14 and C-15 are now stable across three independent enforcement mechanisms (structural site-boundary gates, procedural RESOLUTION BLOCK, MUST NOT modal register) and all their combinations.

---

### Excellence Signals

Round 3 is a stability round — no variation scores above 100, but two patterns emerge as qualitatively superior candidates for R4 forward bake-in:

**S-1 — Named gate markers at step boundaries (V-04)**
The `-- S-4 GATE --` / `-- A-1 GATE --` annotation pattern creates a visually prominent structural fence that cannot be merged with surrounding prose. Unlike inline finality declarations (V-01, V-03) or code-fence closers (V-02, V-05), named gate markers make the enforcement boundary an unmissable structural element. This is the most collapse-resistant C-14 mechanism in the round — a model shortcutting steps would have to explicitly skip a labeled gate, not merely omit a trailing sentence.

**S-2 — Inertia-cost framing in exclusion row (V-05)**
V-05's topic-status exclusion reads: "zero new signal, zero readiness advance" — naming the cost of the substitution rather than merely prohibiting it. This converts the exclusion from a syntactic rule into a consequence rule. The same cost-grounding pattern extends into every FIDELITY CONTEXT warning via the "Inertia risk:" block. This makes the warnings feel like system-level reasoning rather than appended caution labels.

**R4 candidate:** V-04's named gate structure (-- S-4 GATE -- / -- A-1 GATE --) merged with V-05's inertia-cost framing in both the exclusion row and FIDELITY CONTEXT warnings. The risk is prompt length — an editorial pass that preserves gates and inertia framing while trimming procedural redundancy is the natural R4 task.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named gate markers at step boundaries (-- S-4 GATE -- / -- A-1 GATE --) create collapse-resistant C-14 enforcement as a structural fence rather than prose or code-block terminus", "Inertia-cost framing in exclusion row converts topic-status prohibition from syntactic rule to consequence rule -- zero new signal, zero readiness advance"]}
```
