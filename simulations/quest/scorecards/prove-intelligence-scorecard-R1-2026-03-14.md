## Scorecard: prove-intelligence — Round 1

### Composite Scores

| Rank | Variation | Composite | All Essential? |
|------|-----------|-----------|---------------|
| 1 (tie) | V-01 | **100** | YES |
| 1 (tie) | V-03 | **100** | YES |
| 1 (tie) | V-05 | **100** | YES |
| 4 | V-04 | **90** | YES |
| 5 | V-02 | **80** | YES |

All five pass the golden threshold (all essential + composite >= 80). V-02 lands exactly at 80.

---

### What separated the 100s from the rest

**V-04 lost C-06** — the detective register is otherwise excellent (C-09 and C-10 are concrete and FC-linked), but "cast a wide net" doesn't enumerate source type categories. A model could return all design docs and comply fully.

**V-02 lost C-07, C-09, C-10** — the single-pass minimal structure trades coverage for brevity. FC engagement is gap-only (not per-source), contradiction check has no named-sources format requirement, and follow-up queries lack the where/FC structure.

---

### Excellence Signals (new patterns this round)

1. **Insider advantage as a hard exit condition** — V-05 is the only variation requiring "At least one source carries Insider: YES" as a phase gate, not just a field. This is the strongest FM-07 prevention seen so far.

2. **Role separation for extraction fidelity** — V-03's Archivist/Analyst split is a new structural pattern: verbatim extraction in Role 1 before any interpretation, making FM-02 (fabricated excerpts) architecturally impossible rather than just warned against.

3. **FC ledger as a first-class named artifact** — V-01 and V-05 both elevate falsification mapping to its own table with per-criterion status. V-03 goes further with per-source FC field + aggregate coverage map. This is what drives C-07 to PASS in three variations vs. FAIL in V-02.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["insider-advantage-exit-condition", "role-separation-for-extraction-fidelity", "fc-ledger-as-first-class-artifact"]}
```
 |
| V-05 | **PASS** | Phase 3: "extract the verbatim passage most relevant to the hypothesis. Do not summarize from memory." Phase 4 `**Excerpt**: "[from table]"` anchors it back. |

#### C-03 — Each source includes a relevance statement connected to the hypothesis

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | `**Relevance**: ...` field specifies "How this excerpt supports, contradicts, or is tangential to the hypothesis — stated in terms of the hypothesis claim, not the file topic." Explicitly fails generic statements. |
| V-02 | **PASS** | "One sentence on how the excerpt bears on the hypothesis" — hypothesis-connected, though less specific than V-01 about requiring hypothesis-claim terms. Sufficient. |
| V-03 | **PASS** | Analyst role: `**Relevance**: How this excerpt bears on the hypothesis — state the connection in terms of the hypothesis claim or a specific falsification criterion.` FC-aware. |
| V-04 | **PASS** | `What it means for the hypothesis: [connect it to the hypothesis claim directly — "this supports / undermines / complicates the claim because..."]` — hypothesis-claim framing required. |
| V-05 | **PASS** | Phase 4: `**Relevance**: [how the excerpt bears on the hypothesis — connect to hypothesis claim or FC-NN explicitly]` — dual-anchor to hypothesis or FC. |

#### C-04 — Each source includes an explicit evidence strength label

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | `**Strength**: strong | moderate | weak` as its own dedicated field in the Source N block. Hard-failure warning in Step 3: "Omitting any field on any row is a hard failure." |
| V-02 | **PASS** | "A strength label: **strong**, **moderate**, or **weak**" listed as a required per-source item. |
| V-03 | **PASS** | Analyst adds `**Strength**: strong | moderate | weak` per source entry. Role separation ensures this is an interpretation layer applied to every source. |
| V-04 | **PASS** | `Weight: strong | moderate | weak` in the case file entry format. Consistent with rubric vocabulary (different label name but equivalent values). |
| V-05 | **PASS** | Phase 4 Source N block: `**Strength**: strong | moderate | weak`. Appears in assessment phase after evidence extraction, ensuring per-source application. |

#### C-05 — Output ends with a summary verdict

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 6 specifies a dedicated `## Verdict` section with `**Collective finding**`, `**Confidence**`, and `**Basis**` fields. Basis requires citing at least one source by path. |
| V-02 | **PASS** | "After the sources, write a short verdict. State whether the internal evidence collectively confirms, contradicts, or leaves inconclusive the hypothesis. Name at least one specific file." 150-word cap tightens focus without hiding the verdict. |
| V-03 | **PASS** | Analyst step 3: "Verdict: Confirms / contradicts / inconclusive. Confidence: high / medium / low. One paragraph, at least one source cited by path." Placed after contradiction report and coverage map — structural position enforces closing position. |
| V-04 | **PASS** | `## Verdict` section with explicit format: "The internal record [confirms / contradicts / leaves inconclusive] the hypothesis. Confidence: [high / medium / low] — because [one sentence grounded in a specific lead, cited by path]." Detective register maintained. |
| V-05 | **PASS** | Phase 5 step 3: `## Verdict` with `**Finding**`, `**Confidence**`, `**Basis**` fields. Exit condition for Phase 5 explicitly requires "Verdict section present." Hard gate. |

---

### Recommended Criteria (10 pts each, 30 pts total)

#### C-06 — Sources span at least two distinct internal source types

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 1 explicitly directs Glob across multiple namespace directories (`scout/`, `draft/`, `prove/`, `trace/`) and Grep across `**/*.md` and `**/*.yaml`. Multi-type search is required before proceeding. |
| V-02 | **PASS** | Search instruction enumerates: "design docs, specs, CLAUDE.md files, scenario files, prior signal artifacts, YAML configs." All six types named; breadth is framed as part of the search contract. |
| V-03 | **PASS** | Archivist must run "at least four distinct Glob or Grep queries" logged with result counts. Four independent queries against a mixed repo will reliably surface multi-type sources. Query log makes diversity traceable. |
| V-04 | **FAIL** | Search instructions are generic: "Cast a wide net first — search by key terms, by related concepts, by file path patterns." No enumeration of source type categories; no requirement to cover multiple types. A model could return all leads from design docs and fully comply with V-04's instructions. |
| V-05 | **PASS** | Phase 1 requires identifying "internal source types most likely to hold evidence: spec/design docs, scenario files, prior signal artifacts, YAML configs, CLAUDE.md files." Phase 2 requires "at least one Glob query per source type identified." Phase 3 evidence table has a `Source Type` column. Strongest C-06 design across all variations. |

#### C-07 — At least one finding maps to a falsification criterion

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 4 requires a dedicated `### Falsification Mapping` table: `Criterion | Source(s) | Status` with satisfies/violates/inconclusive values. Step 1 extracts FCs from the signal artifact first. If no FCs exist, Step 4 instructs deriving 2-3 from the hypothesis statement. |
| V-02 | **FAIL** | FCs are mentioned only as "gaps": "Note any gap — a falsification criterion in the hypothesis that no source addresses." No per-source FC reference required. The rubric requires a source entry to explicitly cite an FC by name or number — V-02's gap-only framing does not drive this. |
| V-03 | **PASS** | Analyst adds `**FC mapping**: FC-NN satisfies / violates / inconclusive | n/a` per source. Coverage map explicitly maps each FC to sources and flags uncovered criteria. FC engagement is both per-source and aggregate. |
| V-04 | **PASS** | "The case against the null" section: `FC-01: [criterion] — answered by Lead N / unanswered`. FC-by-FC ledger required after the leads. |
| V-05 | **PASS** | Phase 4 Source N block: `**FC**: FC-NN [satisfies / violates / inconclusive] | n/a` per source. Phase 5 step 1 produces a full Falsification Ledger table. Dual coverage: per-source and aggregate. |

#### C-08 — At least one finding is identified as insider advantage

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | `**Insider**: YES — [reason this knowledge is not on the public web]` or `no` required field in every Source N block. |
| V-02 | **PASS** | "Mark any source as **[Insider]** if it contains knowledge that could not be found via a web search — this is what makes `/prove:intelligence` distinct from `/prove:websearch`." Explicitly motivates the flag by naming the skill's differentiator. |
| V-03 | **PASS** | Analyst adds `**Insider**: YES — [why this is not on the public web] | no` per source. Role separation ensures the insider flag is applied thoughtfully, not reflexively. |
| V-04 | **PASS** | `Exclusive intel: [is this something the web doesn't know? If yes, flag it: "Insider — this is only knowable from the internal repo because..."]` — explicit flag with reasoning required. |
| V-05 | **PASS** | Phase 4 Source N block: `**Insider**: YES — [why a web search could not find this] | no`. Phase 4 has extended guidance on what qualifies. Exit condition: "At least one source carries Insider: YES." Only variation making insider a hard gate, not just a field. |

---

### Aspirational Criteria (5 pts each, 10 pts total)

#### C-09 — Output identifies at least one internal contradiction

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 5 (`### Contradictions`) requires naming: "Source A (path) and Source B (path) disagree on X: [what each says] / Status: resolved / unresolved." Explicit negative statement required if no contradictions. |
| V-02 | **FAIL** | "Note any place where two sources conflict with each other." Instruction present but format unspecified — no requirement to name sources by path or state resolved/unresolved status. Does not meet rubric's naming requirement. |
| V-03 | **PASS** | "Contradiction report: Name any two sources that disagree. If none, state so explicitly." Naming required; explicit negative also required. |
| V-04 | **PASS** | "Did any two leads tell you conflicting things? Name them: 'Lead 2 says X; Lead 5 says Y — they can't both be right.' If you can resolve it, resolve it. If you can't, flag it open." Named conflict plus resolution/open-flag required. |
| V-05 | **PASS** | Phase 5 step 2: "Identify any two sources that disagree. State: 'Source A (path) and Source B (path) conflict on X: [what each says]. Status: resolved / unresolved.'" If none, explicit negative. Structural parity with V-01. |

#### C-10 — Output recommends follow-up queries for evidence gaps

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 7: `1. **Query**: [what to search for] | **Where**: [directory or file pattern] | **Addresses**: [FC-NN]` — full three-part structure, FC-linked. Minimum two queries required. |
| V-02 | **FAIL** | "For each gap, name one search that would close it." Single search per gap; no "where to look" or "which FC" required. Does not meet rubric's three-part structure (what / where / FC). |
| V-03 | **PASS** | "Follow-up queries: Two or more specific internal queries for uncovered falsification criteria — each with: what to query, where to look, which FC it addresses." Three-part structure explicitly required. FC linkage mandatory. |
| V-04 | **PASS** | "## Open Threads: Search for [what], in [where], to address [FC-NN]." Three-part structure present in template format. Two or more required. |
| V-05 | **PASS** | Phase 5 step 4: `1. Query: [what] | Where: [path pattern] | Addresses: FC-NN` with at least two required, each tied to an uncovered FC. |

---

## Composite Scores

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Essential | Recommended | Aspirational | Composite | All Essential? |
|-----------|------|------|------|------|------|------|------|------|------|------|-----------|-------------|--------------|-----------|---------------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 60 | 30 | 10 | **100** | YES |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | FAIL | 60 | 20 | 0 | **80** | YES |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 60 | 30 | 10 | **100** | YES |
| V-04 | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | PASS | PASS | 60 | 20 | 10 | **90** | YES |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 60 | 30 | 10 | **100** | YES |

**Golden threshold** (all essential + composite >= 80): all five variations pass. V-02 is exactly at 80.

---

## Ranking

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 (tie) | V-01 | 100 | Structured table + explicit hard-failure warnings. Reference format. |
| 1 (tie) | V-03 | 100 | Role separation gives strongest excerpt fidelity guarantee (FM-02 prevention). |
| 1 (tie) | V-05 | 100 | Phase gates + insider exit condition. Strongest C-06 and C-08 design. |
| 4 | V-04 | 90 | Detective register covers C-09/C-10 well. Loses only C-06 (no type-enumeration). |
| 5 | V-02 | 80 | All essentials pass. Weakest recommended/aspirational coverage. Minimal structure trades explicitness for brevity. |

---

## Excellence Signals

Patterns from the top-scoring variations (V-01, V-03, V-05) that drove scores to 100:

### 1. Hard-failure warnings embedded adjacent to field definitions
V-01 states "Omitting any field on any row is a hard failure" inside Step 3, not in a preamble. V-05 does equivalent work through phase exit conditions. Embedding the failure condition at the point of use — not in a separate rubric section — reduces the chance the model skips a field under load.

### 2. Insider advantage as a hard gate, not a soft field
V-05 is the only variation with an explicit phase exit condition: "At least one source carries Insider: YES." All other variations require the Insider field per source but provide no enforcement if every source evaluates to `no`. V-05's exit condition means the skill cannot complete without at least one insider flag — directly preventing FM-07.

### 3. Falsification ledger as a first-class artifact
V-01 (Step 4 Falsification Mapping table) and V-05 (Phase 5 FC Ledger table) both elevate FC mapping to a named artifact with its own table and per-criterion status column. V-03 goes further with dual coverage: per-source FC field in the Analyst section plus an aggregate Coverage Map. This is why C-07 scores PASS in three variations but FAIL in V-02 where FCs appear only in gap-checking context.

### 4. Role separation for extraction fidelity
V-03's Archivist/Analyst split enforces verbatim extraction before interpretive framing. This directly prevents FM-02 (excerpts written from training knowledge rather than actual file content) — the most dangerous failure mode because plausible-looking fabricated excerpts are invisible in the output. The query log also makes search coverage auditable: you can verify that at least four searches were run.

### 5. Phase entry/exit conditions as structural contracts
V-05's explicit exit conditions per phase prevent skipping. "Exit condition: Evidence table complete, misses noted" requires the model to confirm completion before moving to assessment. This prevents the shortcut of jumping from search results to verdict without reading files.

---

## Failure Mode Analysis

| FM | Criterion | Affected Variations | Notes |
|----|-----------|---------------------|-------|
| FM-01 (path as paraphrase) | C-01 | None | All variations pass C-01; all explicitly require exact file path. |
| FM-02 (excerpt from memory) | C-02 | V-02, V-04 risk | V-02 and V-04 have anti-paraphrase language but no architectural enforcement. V-03's role separation is the strongest structural guard. |
| FM-03 (generic relevance) | C-03 | Low risk in all | V-01 explicitly says "stated in terms of the hypothesis claim, not the file topic." V-03 and V-05 add "or FC-NN" clause for precision. |
| FM-04 (strength in verdict only) | C-04 | V-02 elevated risk | V-02 has the weakest format enforcement; a model producing global strength labels in the verdict section rather than per-source labels could slip through. |
| FM-05 (verdict buried) | C-05 | None | All variations specify a dedicated `## Verdict` section with explicit format. |
| FM-06 (FC at hypothesis level) | C-07 | V-02 | V-02 fails C-07 — FC engagement is gap-only, not per-criterion per source. |
| FM-07 (no insider flag applied) | C-08 | V-01, V-02, V-03, V-04 | All require the field; only V-05 enforces at least one YES via exit condition. |
