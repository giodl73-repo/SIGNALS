Written to `simulations/quest/rubrics/prove-intelligence-rubric-2026-03-14.md`.

**Rubric summary:**

- **5 essential** (C-01–C-05): file path per source, verbatim excerpt, hypothesis-connected relevance statement, per-source strength label, closing summary verdict
- **3 recommended** (C-06–C-08): multi-type source coverage, falsification-criterion mapping, insider-advantage flag
- **2 aspirational** (C-09–C-10): contradiction detection, follow-up query recommendations

The rubric is calibrated to the core contract of `prove-intelligence`: every source must be locatable, quotable, and linked to the hypothesis. The distinction from `prove-websearch` is enforced through C-08 (insider advantage flag) — if none of the internal sources surface knowledge that isn't on the public web, the skill hasn't delivered its unique value.
 a fail. |
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

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
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
