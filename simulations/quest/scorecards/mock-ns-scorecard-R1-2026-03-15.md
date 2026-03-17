## Scoring: mock-ns — Round 1

---

### Rubric recap (weights)

| Band | Essential (5×) | Recommended (3×) | Aspirational (2×) |
|------|---------------|-----------------|------------------|
| Points | 60 | 30 | 10 |
| Formula | pass/5 × 60 | pass/3 × 30 | pass/2 × 10 |
| PARTIAL counts as 0.5 | | | |

**Golden threshold**: all 5 essential pass AND composite ≥ 80.

---

### V-01 — Lifecycle Explicit

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Header complete | PASS | Phase 2 specifies all 6 lines in order including Flag |
| C-02 Category correct | PASS | Full three-row category table with canonical skill lists |
| C-03 Golden structure | PASS | "exact golden structure of {skill-id}" with headings, tables, gates, role cards |
| C-04 Flag present | PASS | Step 1.4 computes flag before header block; header block references it by name |
| C-05 Path = namespace | PASS | Step 1.5 explicit: "The `{namespace}` segment is the namespace argument, not the skill-id" |
| C-06 Default skill | PASS | Full default table + explicit note: "topic-status is excluded as meta-structural" |
| C-07 Fidelity warning | PASS | All three category warnings written in full including REAL-REQUIRED at Tier 2+ qualifier |
| C-08 Next-step line | PASS | Phase 3 specifies the exact next-step line with path template |
| C-09 Tier-conditional flag | PASS | Step 1.4 includes critical namespace row with REAL-REQUIRED at Tier 2+ suffix |
| C-10 TOPICS.md visible | PASS | Step 1.1 is dedicated to TOPICS.md with explicit emit line format |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: 2/2 → 10
**Composite: 100** — Gold

---

### V-02 — Compressed / Output-Forward

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Header complete | PASS | Header block shown with all 6 fields in order |
| C-02 Category correct | PASS | Three-row category classification present |
| C-03 Golden structure | PASS | "Follow the golden structural pattern for {skill-id} exactly" with all bullet requirements |
| C-04 Flag present | PASS | Item 4 in Quick setup list with all three category values |
| C-05 Path = namespace | PASS | "simulations/mock/{topic}-{namespace}-mock-{date}.md — use namespace, not skill-id" |
| C-06 Default skill | PASS | Inline mapping "topic=topic-plan" correct (no exclusion note, but default is right) |
| C-07 Fidelity warning | PARTIAL | HIGH-STRUCTURE warning truncated — missing "REAL-REQUIRED at Tier 2+ for critical namespaces" qualifier; EVIDENCE-HEAVY and MIXED are complete |
| C-08 Next-step line | PASS | End of artifact section specifies the line |
| C-09 Tier-conditional flag | PASS | "add `; REAL-REQUIRED at Tier 2+` if the skill is trace-*, scout-feasibility, or listen-*" |
| C-10 TOPICS.md visible | FAIL | TOPICS.md is checked in step 1 but result is not surfaced in a dedicated emit line; the only output line is the general `> Generating mock for...` which embeds tier but omits TOPICS.md result |

**Essential**: 5/5 → 60  **Recommended**: 2.5/3 → 25  **Aspirational**: 1/2 → 5
**Composite: 90** — Gold (but weakest of the set)

---

### V-03 — Imperative Register

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Header complete | PASS | Step 6 specifies all 6 lines with "Include all six. Do not skip any." |
| C-02 Category correct | PASS | Step 3 table with all three categories and canonical skill lists |
| C-03 Golden structure | PASS | Step 8: "Use skill-specific section headings. Include every required table, gate, verdict, or role card." |
| C-04 Flag present | PASS | Step 4 dedicated: "Write the Flag line value. Write it now. Do not defer it." — strongest defense in the set |
| C-05 Path = namespace | PASS | Step 5 dedicated: "Use `{namespace}`, not `{skill-id}`." Path declared before any content |
| C-06 Default skill | PASS | Default table + "Do NOT use topic-status as the topic default. topic-status is excluded." |
| C-07 Fidelity warning | PASS | Step 7 specifies full warning blocks for all three categories |
| C-08 Next-step line | PASS | Step 9: "Last line of the artifact, always" |
| C-09 Tier-conditional flag | PASS | Step 4 includes critical namespace case with REAL-REQUIRED at Tier 2+ suffix |
| C-10 TOPICS.md visible | PASS | Step 1: "Emit one line: `> TOPICS.md: {result}`" — mandatory dedicated emit |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: 2/2 → 10
**Composite: 100** — Gold

---

### V-04 — Fidelity-Forward

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Header complete | PASS | Header block with all 6 fields in order including Flag table reference |
| C-02 Category correct | PASS | Full classification table, "Lock it before writing." |
| C-03 Golden structure | PASS | "'Recognizable' means: correct section count, correct element types, correct gate/verdict positions." |
| C-04 Flag present | PASS | Dedicated flag table covering all four cases including compliance override |
| C-05 Path = namespace | PASS | "The `{namespace}` segment is the namespace argument. The skill-id does not appear in the filename." |
| C-06 Default skill | PASS | Inline default list "topic→topic-plan" |
| C-07 Fidelity warning | PASS | Strongest in set — three full warning blocks with `---` delimiters, positioned as the organizing concept before the body |
| C-08 Next-step line | PASS | Closing section specifies the line |
| C-09 Tier-conditional flag | PASS | Flag table row: "HIGH-STRUCTURE (critical: trace-*, scout-feasibility, listen-*) | REAL-REQUIRED at Tier 2+" |
| C-10 TOPICS.md visible | PASS | "Emit `> TOPICS.md: {result}`" in setup section |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: 2/2 → 10
**Composite: 100** — Gold

---

### V-05 — Path-First

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Header complete | PASS | Header block specified with all 6 fields in order |
| C-02 Category correct | PASS | Full three-row classification table |
| C-03 Golden structure | PASS | "All required structural elements (tables, gates, verdicts, role cards, named outputs)" |
| C-04 Flag present | PASS | Step 4 flag table with all category/type combinations |
| C-05 Path = namespace | PASS | Strongest in set — path declared first before skill-id enters context; "The skill-id does NOT appear in the path." |
| C-06 Default skill | PASS | Default table shows topic=topic-plan |
| C-07 Fidelity warning | PASS | Abbreviated inline format but HIGH-STRUCTURE variant correctly includes "REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen)" |
| C-08 Next-step line | PASS | "(Use the path you declared at the top. Do not reconstruct it.)" — path integrity enforced |
| C-09 Tier-conditional flag | PASS | Flag table: "HIGH-STRUCTURE | critical | REAL-REQUIRED at Tier 2+" row present |
| C-10 TOPICS.md visible | PASS | "Emit: `> TOPICS.md: {result}`" in setup step 1 |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: 2/2 → 10
**Composite: 100** — Gold

---

### Summary table

| Variation | Essential | Recommended | Aspirational | Composite | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-01 Lifecycle Explicit | 5/5 | 3/3 | 2/2 | **100** | Gold |
| V-02 Compressed | 5/5 | 2.5/3 | 1/2 | **90** | Gold |
| V-03 Imperative | 5/5 | 3/3 | 2/2 | **100** | Gold |
| V-04 Fidelity-Forward | 5/5 | 3/3 | 2/2 | **100** | Gold |
| V-05 Path-First | 5/5 | 3/3 | 2/2 | **100** | Gold |

**Ranking**: V-01 = V-03 = V-04 = V-05 (100) > V-02 (90)

---

### Excellence signals from top-scoring variations

**Pattern 1 — Dedicated TOPICS.md emit line (V-01, V-03, V-04, V-05)**
Every top-scoring variation mandates a specific `> TOPICS.md: {result}` progress line. V-02's failure on C-10 came precisely from collapsing the TOPICS.md check into a silent sub-step of the Quick setup block with no dedicated output. An emit line is required to satisfy C-10; a check that doesn't surface its result fails the aspirational criterion.

**Pattern 2 — Flag value computed before the header block is written (V-03)**
V-03's "Write it now. Do not defer it." is the strongest formulation in the set. V-01 pre-computes in Step 1.4 then references it in Phase 2. Both prevent C-04 failures by ensuring the flag value is resolved while the category lookup is still active in context, not after heading and body content have been written.

**Pattern 3 — Path declared before skill-id enters context (V-05)**
V-05 leads with path declaration as the first instruction, before skill resolution. The instruction "The skill-id does NOT appear in the path" is stated at the moment the path is constructed — before `{skill-id}` becomes prominent in working memory. V-03 also dedicates a step (Step 5) to path declaration before body writing.

**Pattern 4 — "Do not reconstruct the path" anchor (V-05)**
V-05's closing instruction "(Use the path you declared at the top. Do not reconstruct it.)" prevents path drift in the next-step line and the artifact-written emit. Reconstruction at closure is when skill-id contamination re-enters — holding a single declared path reference eliminates this failure mode.

**New pattern identified by scoring (not in spread-design plan):**
V-02 exposed that full verbose warning text is load-bearing. The HIGH-STRUCTURE warning in V-02 dropped the "REAL-REQUIRED at Tier 2+ for critical namespaces" qualifier — a factually important phrase — when compressed to a single inline sentence. Abbreviated warnings are not structurally equivalent to full warning blocks; the qualifier must be present to pass C-07 reliably across all category branches.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Full verbose HIGH-STRUCTURE warning text is required — abbreviated inline warnings silently drop the REAL-REQUIRED at Tier 2+ qualifier, causing C-07 partial failures on the most common category branch", "Path anchor instruction prevents reconstruction drift — 'use the declared path verbatim, do not reconstruct' at artifact close eliminates skill-id re-entry into the filename at the next-step line"]}
```
