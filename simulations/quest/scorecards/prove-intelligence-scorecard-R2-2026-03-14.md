Scorecard written to `simulations/quest/scorecards/prove-intelligence-scorecard-R2-2026-03-14.md`.

---

## Results: prove-intelligence R2

| Rank | Variation | Composite | All Essential? |
|------|-----------|-----------|---------------|
| 1 (tie) | V-01 | **100** | YES |
| 1 (tie) | V-04 | **100** | YES |
| 1 (tie) | V-05 | **100** | YES |
| 4 | V-02 | **98** | YES |
| 5 | V-03 | **96** | YES |

The floor rose from 80 (R1) to 96 (R2) — all five variations now pass every essential and recommended criterion. The only differentiation is in the three new aspirational criteria.

**What failed where:**
- **V-02** (C-12 axis): Lost C-11 — has Insider fields but no `## Insider Gate` block and no WARNING text. FM-08 is live.
- **V-03** (C-13 axis): Lost C-11 and C-12 — insider is "document in verdict" (post-hoc note, not a gate); source blocks combine extraction and interpretation in the same pass (FM-09).

**Key finding:** V-01 achieves C-12 incidentally — its Step 3/Step 4 separation (extraction table before interpretation blocks) passes the structural separation criterion even though C-11 was its design axis. The two-step extraction-before-analysis pattern generalizes beyond explicit role/phase naming.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["blocking-warning-text-as-gate-mechanism", "named-role-phase-separation-for-c12-durability", "ledger-lifecycle-tied-to-phase-exit-conditions"]}
```
----|
| V-01 | **PASS** | Step 4: `- **Path**: [exact file path]` in every Source N block; Step 3 candidate table also requires path column. |
| V-02 | **PASS** | Phase 1 Raw Evidence table `Path` column (verbatim extraction log); Phase 2 Source N: `- **Path**: [from Archivist table row N]` anchors to the logged path. |
| V-03 | **PASS** | Source block: `- **Path**: [exact file path]`. Step 2 instructions: "extract the verbatim passage most relevant to the hypothesis. Do not summarize from memory." |
| V-04 | **PASS** | Archivist Raw Evidence Table `Path` column; Analyst Source N: `- **Path**: [from Archivist table row N]`. Path is recorded at extraction and referenced at interpretation — two-layer anchor. |
| V-05 | **PASS** | Phase 2 Raw Evidence table `Path` column; Phase 3 Source N: `- **Path**: [from table]`. Phase separation means path must be recorded during extraction before interpretation begins. |

#### C-02 — Each source includes a verbatim or near-verbatim excerpt

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 3: "extract the most relevant passage verbatim. Do not summarize from memory." Step 4: `- **Excerpt**: "[verbatim text — minimum one full sentence]"`. Minimum length requirement prevents word-fragment excerpts. |
| V-02 | **PASS** | Phase 1: "Open each promising file. Extract the most relevant passage verbatim. Do not paraphrase from memory." Raw Evidence table column label is "Excerpt (verbatim)". Phase 2: `- **Excerpt**: "[from table — reference the log, do not re-read the file]"`. |
| V-03 | **PASS** | `- **Excerpt**: "[verbatim passage — minimum one full sentence]"` in every Source N block. Step 2 instructs: "extract the verbatim passage most relevant to the hypothesis. Do not summarize from memory." |
| V-04 | **PASS** | Archivist mandate: "record the verbatim passage most relevant to the hypothesis." Raw Evidence Table column is "Excerpt (verbatim)". Analyst: `- **Excerpt**: "[from Archivist table row N — do not re-excerpt from the file; reference the table]"` prevents double-read fabrication. |
| V-05 | **PASS** | Phase 2 mandate: "extract verbatim passage most relevant to hypothesis. Do not paraphrase from memory." Raw Evidence column "Excerpt (verbatim)". Phase 3: `- **Excerpt**: "[from table — reference the log, do not re-read the file]"`. |

#### C-03 — Each source includes a relevance statement connected to the hypothesis

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 4: `- **Relevance**: [how this excerpt supports, contradicts, or is tangential to the hypothesis — stated in terms of the hypothesis claim or FC-NN, not just the file topic]`. Explicit negation of generic relevance. |
| V-02 | **PASS** | Source N: `- **Relevance**: [how the excerpt bears on the hypothesis — connect to hypothesis claim or FC-NN explicitly, not just file topic]`. Dual-anchor to hypothesis or named FC. |
| V-03 | **PASS** | Source block: `- **Relevance**: [how this excerpt bears on the hypothesis — stated in terms of the hypothesis claim or FC-NN]`. FC-aware. |
| V-04 | **PASS** | Analyst Source N: `- **Relevance**: [how the excerpt bears on the hypothesis — connect to hypothesis claim or FC-NN explicitly]`. Archivist mandated not to write relevance — role separation enforces FC-aware framing in the interpretation layer only. |
| V-05 | **PASS** | Phase 3 Source N: `- **Relevance**: [connect to hypothesis claim or FC-NN — not just file topic]`. Interpretation phase only, after extraction is complete. |

#### C-04 — Each source includes an explicit evidence strength label

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 4: `- **Strength**: strong | moderate | weak` as dedicated field. "Every field is required — omitting any field on any source is a hard failure." Hard-fail warning at point of use. |
| V-02 | **PASS** | Source N: `- **Strength**: strong | moderate | weak`. Applied in Phase 2 only — extraction phase contains no strength labels, enforcing per-source rather than per-verdict labeling. |
| V-03 | **PASS** | `- **Strength**: strong | moderate | weak` per Source N block. Step 2 requires a complete block per source; omission would leave an incomplete block. |
| V-04 | **PASS** | Analyst Source N: `- **Strength**: strong | moderate | weak`. Archivist does not apply strength labels — Analyst is the only role that can, ensuring per-source application rather than per-verdict. |
| V-05 | **PASS** | Phase 3 Source N: `- **Strength**: strong | moderate | weak`. Phase gate structure means assessment blocks are only produced in Phase 3 — strength labels cannot bleed into the extraction log. |

#### C-05 — Output ends with a summary verdict

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 8: `## Verdict` with `**Collective finding**`, `**Confidence**`, `**Basis**` fields. Basis requires citing at least one source by path. |
| V-02 | **PASS** | Phase 2 `## Verdict` with `**Collective finding**`, `**Confidence**`, `**Basis**`. "At least one source cited by path from the Extraction Log." Dedicated closing section after Contradiction Check. |
| V-03 | **PASS** | Step 7: `## Verdict` with collective finding, confidence, basis citing at least one source by path. Follows insider check and contradiction check — structural position enforces closing position. |
| V-04 | **PASS** | Synthesis `## Verdict` with collective finding, confidence, basis. Cannot be written until Insider Gate is resolved. |
| V-05 | **PASS** | Phase 5 step 3: `## Verdict` with `**Collective finding**`, `**Confidence**`, `**Basis**`. Phase 5 exit condition explicitly requires "Verdict section present." |

---

### Recommended Criteria (30 pts total)

#### C-06 — Sources span at least two distinct internal source types

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 1 identifies source types; Step 2 requires "at least one Glob or Grep query per source type identified in Step 1." Multi-type search enforced before extraction. |
| V-02 | **PASS** | Phase 1: "Search at least two distinct source type categories (e.g., specs AND scenario files — not all from one category)." Explicit category requirement with example of what fails. |
| V-03 | **PASS** | Step 4 coverage check: "Count sources by type. If all sources are from a single category, note this as a gap and run one additional search targeting a different type before proceeding." Hard correction required on failure. |
| V-04 | **PASS** | Archivist: "Target at least two distinct source type categories: spec/design doc, scenario file, prior signal artifact, YAML config, CLAUDE.md/session driver." Explicit enumeration + minimum. |
| V-05 | **PASS** | Phase 1 identifies source type list; Phase 2 requires "at least one Glob query per source type identified." Raw Evidence table has `Source Type` column making diversity auditable. |

#### C-07 — At least one finding maps to a falsification criterion

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 4: `- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a` per source. Step 6 `## Falsification Ledger` maps every FC to sources and status — per-source and aggregate. |
| V-02 | **PASS** | Source N: `- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a`. Phase 2 `## Falsification Ledger` — every FC must appear. FC mapping is both per-source and aggregate. |
| V-03 | **PASS** | `- **FC addressed**: FC-NN [satisfies / violates / inconclusive]` per source block. Ledger updated inline after each source — FC mapping is live throughout, not deferred to synthesis. |
| V-04 | **PASS** | Analyst Source N: `- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a`. Synthesis `## Falsification Ledger` with every FC listed. |
| V-05 | **PASS** | Phase 3 Source N: `- **FC**: FC-NN [satisfies / violates / inconclusive] | n/a`. Inline ledger updates in Phase 3. Phase 5 `## Falsification Ledger — Final`. Three-layer FC coverage. |

#### C-08 — At least one finding is identified as insider advantage

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 4: `- **Insider**: YES — [reason this knowledge is not findable on the public web] | no`. Required field per source block. |
| V-02 | **PASS** | Source N: `- **Insider**: YES — [why this is not findable on the public web] | no`. Insider flag appears in Phase 2 after extraction — applied thoughtfully, not reflexively. |
| V-03 | **PASS** | `- **Insider**: YES — [why this is not on the public web] | no` per Source N block. Step 6 counts Insider: YES sources — surface check confirms field was applied. |
| V-04 | **PASS** | Analyst Source N: `- **Insider**: YES — [why this is not findable via web search] | no`. Insider flagging is an Analyst responsibility — ensures it is applied after evidence is collected, not during search. |
| V-05 | **PASS** | Phase 3 Source N: `- **Insider**: YES — [why a web search cannot find this: implementation choice, internal convention, unreleased scenario outcome, in-progress work] | no`. Four-item guidance list for what qualifies. |

---

### Aspirational Criteria (10 pts total)

#### C-09 — Output identifies at least one internal contradiction

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 7: "Source A ([path]) and Source B ([path]) disagree on [X]: [what each says]. Status: resolved / unresolved." Explicit negative required if none. |
| V-02 | **PASS** | `## Contradictions`: "Source A (row N, [path]) and Source B (row M, [path]) disagree on [X]..." Row-number reference anchors to Extraction Log. |
| V-03 | **PASS** | Step 5: "Name any two sources that disagree." Named conflict required; explicit negative also required. |
| V-04 | **PASS** | Synthesis `## Contradictions`: "Source A (row N, [path]) and Source B (row M, [path]) disagree on [X]: [what each says]. Status: resolved / unresolved." |
| V-05 | **PASS** | Phase 5 step 2: "Source A (row N, [path]) and Source B (row M, [path]) conflict on [X]..." If none: explicit negative required. |

#### C-10 — Output recommends follow-up queries for evidence gaps

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 9: `1. **Query**: [what] | **Where**: [directory or file pattern] | **Addresses**: FC-NN`. Three-part structure, FC-linked, minimum two. |
| V-02 | **PASS** | `## Follow-Up Queries`: `1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN`. Min two, each tied to uncovered FC. |
| V-03 | **PASS** | Step 8: `1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN`. "For each `uncovered` row in the final ledger, write a follow-up query." Ledger-driven FC linkage. |
| V-04 | **PASS** | `## Follow-Up Queries`: three-part format, min two, each tied to uncovered FC. |
| V-05 | **PASS** | Phase 5 step 4: `1. **Query**: [what] | **Where**: [path pattern] | **Addresses**: FC-NN`. At least two, each tied to uncovered or weakly-evidenced FC. |

#### C-11 — Insider advantage treated as a hard exit condition

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 5 `## Insider Gate` block with YES/no count. If Insider: YES is zero: full `WARNING: INSIDER GATE NOT MET` text block. "Do not proceed to Step 6 until the gate is acknowledged." Hard blocking instruction. |
| V-02 | **FAIL** | Insider field present per source in Phase 2, but no `## Insider Gate` section exists. No WARNING block. No blocking instruction. A run where every source is `Insider: no` completes silently. FM-08 active. |
| V-03 | **FAIL** | Step 6 says "If zero, document this explicitly in the Verdict and note that the skill's insider-advantage value was not delivered." Documentation in the verdict is post-hoc, not a gate. No WARNING block. No blocking instruction. FM-08 active. |
| V-04 | **PASS** | `## Insider Gate` after all Source N blocks with YES/no count. If Insider: YES is zero: `WARNING: INSIDER GATE NOT MET` block with reclassification instructions. "Do not write the Synthesis sections until the gate is acknowledged." Hard gate before synthesis. |
| V-05 | **PASS** | Phase 4 `## Insider Gate` with YES/no count. If zero: `WARNING: INSIDER GATE NOT MET` block with four-item reclassification list. "Proceed only after the gate is acknowledged — either resolved or explicitly documented." Phase gate before Phase 5. |

#### C-12 — Extraction and interpretation are structurally separated

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 3 (`## Candidate Files` table): "Do not interpret yet. Record paths and excerpts only." Step 4 (`### Source N` blocks): interpretation only. Two named sections with distinct mandates. Extraction table precedes analysis blocks in the artifact. |
| V-02 | **PASS** | Phase 1 (`## Extraction Log`): verbatim only, no interpretation, no strength, no insider. Phase 2 (`## Analysis`): interpretation only, cannot introduce new sources. Named phases are the structural contract. Strongest C-12 design in the round. |
| V-03 | **FAIL** | Source blocks during Step 2 combine `**Excerpt**` (extraction) with `**Relevance**`, `**Strength**`, `**Insider**` (interpretation) in the same block, written simultaneously as search progresses. No phase separation. Single-pass format. FM-09 active. |
| V-04 | **PASS** | Archivist role (`## Archivist Output`, Raw Evidence Table): "If you find yourself writing about what something means, stop — that is Role 2's job." Analyst: operates on Archivist table only, cannot add sources. Two named roles with distinct mandates visible in output structure. |
| V-05 | **PASS** | Phase 2 (Extraction): "Collect verbatim evidence only. No interpretation, no relevance statements, no strength labels, no insider flags." Phase 3 (Analysis): "Interpret the Raw Evidence table only — do not introduce new sources." Named phases enforce order in output structure. |

#### C-13 — Falsification ledger is a first-class named artifact

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 6 `## Falsification Ledger`: named table with FC, Criterion, Source(s), Status. Every FC must appear. `uncovered` is a valid terminal status. Aggregate map exists independently of per-source FC fields. |
| V-02 | **PASS** | Phase 2 `## Falsification Ledger`: named table, every FC listed. "Every FC must appear. Uncovered FCs are listed with status `uncovered`." Coverage gaps visible without reading individual entries. |
| V-03 | **PASS** | Three ledger versions: draft at Step 1 (all `open`), inline update after each Source N, final at Step 3. "This redundancy is intentional: it makes evidence coverage visible at every stage of the run." Best C-13 lifecycle in the round. |
| V-04 | **PASS** | Synthesis `## Falsification Ledger`: named table, every FC with sources and status. `uncovered` is valid terminal status. |
| V-05 | **PASS** | Three ledger versions tied to phases: Draft (Phase 1), In Progress (Phase 3, updated after each source), Final (Phase 5). Phase ties make the lifecycle structurally enforced. |

---

## Composite Scores

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Essential | Recommended | Aspirational | Composite | All Essential? |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|-------------|--------------|-----------|---------------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 60 | 30 | 10 | **100** | YES |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | 60 | 30 | 8  | **98**  | YES |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | PASS | 60 | 30 | 6  | **96**  | YES |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 60 | 30 | 10 | **100** | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 60 | 30 | 10 | **100** | YES |

**Golden threshold** (all essential + composite >= 80): all five pass. Floor rose from 80 (R1) to 96 (R2).

---

## Ranking

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 (tie) | V-01 | 100 | C-11 gate + Steps 3/4 separation passes C-12 incidentally. Reference step-by-step format. |
| 1 (tie) | V-04 | 100 | Archivist/Analyst named roles (C-12) + Insider Gate warning (C-11) + FC Ledger (C-13). Clean two-role architecture. |
| 1 (tie) | V-05 | 100 | Full five-phase lifecycle. Strongest C-06, C-13 (phase-tied ledger), C-11 (four-item reclassification list). |
| 4     | V-02 | 98  | Best C-12 in round (named phases, Phase 2 cannot add sources). Loses only C-11 — no insider gate block. |
| 5     | V-03 | 96  | Best C-13 lifecycle (three inline snapshots, ledger-first framing). Loses C-11 and C-12. Confirms ledger-first and extraction-first are independent concerns. |

---

## Excellence Signals

### 1. Blocking WARNING text is the mechanism, not a count field
V-01, V-04, V-05 all include the `WARNING: INSIDER GATE NOT MET` block verbatim in the prompt followed by "Do not proceed until acknowledged." V-03's formulation ("document in the Verdict") records the failure after the fact rather than preventing it. The warning text is the gate; the count field is only how you check whether to show it.

### 2. Named role/phase separation makes C-12 durable under model compression
V-02 (Phase 1 / Phase 2), V-04 (Archivist / Analyst), V-05 (Phase 2 / Phase 3) all use named structural units visible in the output artifact. When a model compresses or skips steps, named sections leave a visible gap in the artifact. V-03's in-block separation (Excerpt first, then Relevance) is invisible under compression — a merged block still looks like a complete source block.

### 3. Ledger lifecycle tied to phase exit conditions is stronger than tied to steps
V-05's ledger tied to phases (Draft in Phase 1, In Progress in Phase 3, Final in Phase 5) is more durable than V-03's ledger tied to steps because phase exit conditions enforce output order. A model cannot reach Phase 5 synthesis without Phase 3 analysis artifacts. In V-03, the final ledger can in principle be written without the in-progress snapshots.

### 4. V-01 achieves C-12 structurally despite being a C-11 single-axis variation
V-01 was designed for C-11, but its Step 3 (extraction table, "Do not interpret yet") / Step 4 (interpretation blocks) design passes C-12 incidentally. This confirms that the two-step pattern — log extraction separately from analysis — is robust enough to enforce separation even without explicit phase framing. The pattern generalizes beyond role-named variations.

---

## Failure Mode Analysis (R2 additions)

| FM | Criterion | Affected Variations | Notes |
|----|-----------|---------------------|-------|
| FM-08 (gate not enforced) | C-11 | V-02, V-03 | V-02 has no gate section; V-03 has a post-hoc verdict note. Both allow silent completion with zero insider sources. |
| FM-09 (simultaneous extract+interpret) | C-12 | V-03 | Source blocks combine Excerpt and Relevance/Strength/Insider in one pass. Fabricated excerpts indistinguishable structurally. |
| FM-10 (no aggregate ledger) | C-13 | None | All five produce a named Falsification Ledger table. C-13 was the best-covered new criterion in R2. |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["blocking-warning-text-as-gate-mechanism", "named-role-phase-separation-for-c12-durability", "ledger-lifecycle-tied-to-phase-exit-conditions"]}
```
