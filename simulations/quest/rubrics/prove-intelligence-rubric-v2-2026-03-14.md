Done. Here's what changed in v2:

**Three new aspirational criteria** extracted from Round 1 excellence signals:

| ID | Pattern Source | What it enforces |
|----|---------------|-----------------|
| C-11 | V-05 (insider-advantage-exit-condition) | Insider: YES must be a **phase gate**, not just a field — runs that produce zero insider sources must emit an explicit warning |
| C-12 | V-03 (role-separation-for-extraction-fidelity) | Extraction and interpretation must be **structurally separated** in the output — single-pass formats where the model excerpts and interprets simultaneously do not pass |
| C-13 | V-01/V-05 (fc-ledger-as-first-class-artifact) | A dedicated falsification **ledger table** must exist as its own artifact mapping every FC to status — per-source FC fields alone are insufficient |

**Other changes:**
- Scoring formula denominator updated: `aspirational_pass / 5 * 10` (was `/ 2`)
- Three new failure modes added (FM-08, FM-09, FM-10) — one per new criterion
- Summary line updated to reflect 5 aspirational criteria
 (C-11, C-12, C-13) extracted from Round 1 excellence signals. Scoring formula denominator for aspirational tier updated from 2 to 5. Three new failure modes added (FM-08, FM-09, FM-10).

---

## Essential (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Each source includes a full file path | essential | correctness | Each source entry includes the full repository-relative file path to the file (e.g., `simulations/scout/...`). A source cited by label or paraphrase ("the feasibility spec") without a resolvable path is a fail. |
| C-02 | Each source includes a verbatim or near-verbatim excerpt | essential | correctness | Each source entry contains a direct quote or close paraphrase of the relevant text from that file. A summary written from memory without reproducing any passage from the source does not pass. The excerpt must be long enough to verify the claim — a single word fragment is a fail. |
| C-03 | Each source includes a relevance statement connected to the hypothesis | essential | coverage | Each source entry contains an explicit sentence explaining how the excerpt supports, contradicts, or is tangential to the hypothesis under investigation. "This file is related" is a fail — the connection must be stated in terms of the hypothesis claim or its falsification criteria. |
| C-04 | Each source includes an explicit evidence strength label | essential | format | Each source entry carries a strength rating — strong / moderate / weak, or equivalent — as its own field, not embedded in prose. A verdict-level strength summary does not substitute for per-source labels. Omitting strength on any source is a hard fail. |
| C-05 | Output ends with a summary verdict | essential | coverage | The output closes with a dedicated verdict section that states the collective weight of internal evidence toward the hypothesis: confirms / contradicts / inconclusive. The verdict must reference at least one source by name. A verdict that is only implied by the source table does not pass. |

---

## Recommended (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Sources span at least two distinct internal source types | recommended | depth | The cited sources include entries from at least two of the following categories: spec/design doc, scenario/test file, prior signal artifact, configuration file (YAML/JSON), CLAUDE.md or session driver. All sources from a single category (e.g., all specs) do not pass. |
| C-07 | At least one finding maps to a falsification criterion | recommended | correctness | At least one source entry explicitly references a falsification criterion from the hypothesis document by name or number, and states whether the finding satisfies, violates, or is inconclusive on that criterion. A generic relevance statement that does not mention falsification criteria does not pass. |
| C-08 | At least one finding is identified as insider advantage | recommended | depth | At least one source entry is explicitly flagged as insider evidence — information that is only knowable from internal sources and is not reflected in public documentation or external web research. The flag must appear in the entry itself (e.g., "Insider: this design decision does not appear in public docs"). Implicit insider value without labeling does not pass. |

---

## Aspirational (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Output identifies at least one internal contradiction | aspirational | depth | The output explicitly surfaces a case where one internal source contradicts another, or where an internal source contradicts previously gathered external evidence. The contradiction must be named (source A vs. source B disagree on X) and briefly resolved or flagged as unresolved. Noting that sources are "mixed" without identifying specific conflict is a fail. |
| C-10 | Output recommends follow-up queries for evidence gaps | aspirational | behavior | The output includes a dedicated section listing at least two specific follow-up internal queries — each named query tied to an unanswered falsification criterion. Generic "more research needed" language without query specifics is a fail. Each follow-up must state: what to query, where to look, and which falsification criterion it would address. |
| C-11 | Insider advantage treated as a hard exit condition | aspirational | behavior | The output or skill prompt enforces "at least one Insider: YES source" as a phase gate — not merely a field to populate. A run that completes without any insider-flagged source must surface an explicit warning that the skill's unique value has not been delivered. Producing C-08 fields without a gatekeeping check does not pass. |
| C-12 | Extraction and interpretation are structurally separated | aspirational | correctness | The output demonstrates role or phase separation: verbatim extraction from source files is completed and logged before any interpretation, relevance judgment, or strength labeling is applied. A single-pass format where the model excerpts and interprets simultaneously does not pass. The separation must be visible in the output structure (e.g., an extraction log precedes the analysis table, or two named roles are distinguished). |
| C-13 | Falsification ledger is a first-class named artifact | aspirational | coverage | The output includes a dedicated falsification ledger — a named table or section that maps every falsification criterion to: the source(s) that address it, and a per-criterion status (satisfies / violates / inconclusive / uncovered). A per-source FC field alone does not pass; the aggregate ledger must exist as its own artifact so that coverage gaps are visible without reading individual source entries. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

| ID | Criterion | Failure Pattern |
|----|-----------|-----------------|
| FM-01 | C-01 | Source cited by paraphrase or label ("the feasibility spec") without a file path — happens when the model summarizes from memory rather than searching |
| FM-02 | C-02 | Source entry contains only the model's interpretation of a passage, no direct text — excerpts written from training knowledge rather than actual file content |
| FM-03 | C-03 | Relevance statement is generic ("this file is about the same topic") without connecting to the hypothesis claim or falsification criteria |
| FM-04 | C-04 | Strength labels present in the verdict section only, not per-source — model summarizes evidence quality globally but omits the per-entry label |
| FM-05 | C-05 | Verdict buried mid-document or phrased as a transition sentence rather than a dedicated closing section |
| FM-06 | C-07 | Model references the hypothesis document but does not cite specific falsification criteria — relevance stated at hypothesis level, not at criterion level |
| FM-07 | C-08 | All sources are design docs that are also publicly readable; no entry flagged as insider-only knowledge |
| FM-08 | C-11 | Insider flag fields are populated (C-08 passes) but no gate is enforced — run completes silently when all insider fields are "no", losing the skill's differentiation without any warning |
| FM-09 | C-12 | Model excerpts and interprets in the same pass — relevance and strength labels are written alongside the quote before extraction is complete, making fabricated excerpts indistinguishable from real ones in the output structure |
| FM-10 | C-13 | Per-source FC fields are present but no aggregate ledger exists — uncovered falsification criteria are invisible unless the reader scans every source entry individually |
