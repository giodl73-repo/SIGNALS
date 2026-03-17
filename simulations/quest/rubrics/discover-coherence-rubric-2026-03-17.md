Rubric written to `simulations/quest/rubrics/discover-coherence-rubric-2026-03-17.md`.

**5 essential criteria** covering the skill's core value proposition:

| ID | What it enforces |
|----|-----------------|
| C-01 | Signal inventory — knows what it read |
| C-02 | Side-by-side claims — not just "these two disagree" |
| C-03 | Every entry labeled blocking / advisory |
| C-04 | Concrete resolution per contradiction (not "investigate further") |
| C-05 | Actually compares across different skills, not within one |

The key design decision: C-02 and C-04 are the failure modes most likely to produce a technically-compliant but useless output — a report that names disagreements without quoting the claims, or prescribes no actionable next step. Both are essential.
ntory | essential | coverage |
| C-02 | Side-by-side contradiction listing | essential | correctness |
| C-03 | Severity classification on every entry | essential | correctness |
| C-04 | Resolution path per contradiction | essential | depth |
| C-05 | Cross-skill comparison | essential | correctness |

### C-01 — Signal inventory

**Text**: The output begins by listing which discover artifacts were found for the topic,
including each skill name and file path or date. If fewer than two signals are present,
the output states this explicitly and declines to run the coherence check (insufficient
input — not a contradiction error).

**Pass condition**: At least two distinct discover signal files are identified by name/path
in the output, OR the output explicitly reports "fewer than 2 signals found, coherence
check cannot run."

---

### C-02 — Side-by-side contradiction listing

**Text**: Every contradiction surfaces both signals that conflict, quoting or directly
paraphrasing the specific claim from each signal (not just naming the source files). The
reader must be able to see exactly what Signal A said and exactly what Signal B said
without opening the source files.

**Pass condition**: Each contradiction entry shows a "Signal A says: …" / "Signal B says:
…" or equivalent parallel structure with the conflicting claims visible in the output. A
summary like "discover-competitors and discover-inertia disagree" with no quoted claims
fails.

---

### C-03 — Severity classification on every entry

**Text**: Every contradiction is labeled exactly `blocking` or `advisory` — no other
values. Blocking means the contradiction must be resolved before specifying (the two
signals cannot both be true and the decision depends on which is correct). Advisory means
the contradiction is worth noting but does not block specifying.

**Pass condition**: Every contradiction entry carries either `blocking` or `advisory` as
its severity label. Any entry without a severity label fails this criterion. No
contradictions found is a valid outcome (pass).

---

### C-04 — Resolution path per contradiction

**Text**: Each contradiction entry ends with a concrete resolution: a specific action,
reframing, or next skill to run that would eliminate the contradiction. "Investigate
further" alone fails — the resolution must be actionable (e.g., "Run discover-inertia
--focus switching-cost to reconcile the switching-cost discrepancy" or "Update
discover-competitors threat rating for inertia from MEDIUM to HIGH to match the
switching-cost finding in discover-inertia").

**Pass condition**: Each contradiction entry contains a resolution that names a specific
action (a skill to run, a claim to amend, a field to update). Generic advice without a
concrete next step fails.

---

### C-05 — Cross-skill comparison

**Text**: The coherence check compares signals across at least two different discover
skills (e.g., competitors vs inertia, hypothesis vs websearch, feasibility vs risk).
A report that only looks within one artifact, or that only compares version dates, does
not constitute a coherence check.

**Pass condition**: The output explicitly identifies at least one pair of different discover
skills being compared, even if no contradictions are found. "Compared: discover-competitors,
discover-inertia, discover-hypothesis — no contradictions found" passes. A report that
never names two different skills being cross-referenced fails.

---

## Recommended Criteria (30 pts)

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-06 | Summary tally at top | recommended | format |
| C-07 | Ready-to-specify verdict | recommended | behavior |
| C-08 | Evidence citations in contradiction entries | recommended | depth |

### C-06 — Summary tally at top

**Text**: The report opens with a one-line summary tally before the per-contradiction
detail: total contradictions found, how many are blocking, how many are advisory. Enables
quick triage without reading the full report.

**Pass condition**: A tally line appears before the first contradiction entry in a form
such as "N contradictions: M blocking, M advisory" or a summary table with those counts.

---

### C-07 — Ready-to-specify verdict

**Text**: The report closes with an explicit readiness statement: either "Ready to specify"
or "Not ready to specify — resolve blocking contradictions first." The verdict is tied to
the blocking count (0 blocking → ready; any blocking → not ready).

**Pass condition**: The final section or closing line contains a readiness verdict that
matches the blocking count in the tally. A report with 1 blocking contradiction that
concludes "ready to specify" fails.

---

### C-08 — Evidence citations in contradiction entries

**Text**: Each contradiction entry cites the source artifact (skill name + date or file
path) for both conflicting claims, so the reader can trace the finding back to its origin
without searching.

**Pass condition**: At least one of the two claim sides in each contradiction entry
includes a source reference (skill ID or file path). A report where claims float free
of any attribution fails this criterion.

---

## Aspirational Criteria (10 pts)

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-09 | Contradiction taxonomy | aspirational | depth |
| C-10 | Suggested skill per blocking contradiction | aspirational | behavior |

### C-09 — Contradiction taxonomy

**Text**: Each contradiction is typed by the nature of the disagreement:
- `rating-conflict` — two signals assign different ratings (HIGH / MEDIUM / LOW) to the same factor
- `prediction-conflict` — one signal predicts an outcome the other contradicts
- `evidence-conflict` — two evidence findings point in opposite directions

Taxonomy helps the team understand whether they are looking at a measurement disagreement
or a logical one, and prioritize accordingly.

**Pass condition**: Each contradiction entry carries one of the three taxonomy labels (or
an equivalent named type). Entries without a type label do not count toward this criterion.

---

### C-10 — Suggested skill per blocking contradiction

**Text**: For each blocking contradiction, the resolution path names a specific Signal
skill to run next (e.g., `discover-inertia`, `discover-analysis`, `discover-websearch`)
that would generate the evidence needed to resolve the conflict. Advisory contradictions
may include a skill suggestion but are not required to.

**Pass condition**: Every `blocking` contradiction entry ends with a "Resolve with:
/skill-name [params]" line or equivalent. A blocking entry whose resolution is purely
narrative without a skill reference fails this criterion.

---

## Scoring Example

| Criteria set | Pass count | Weight | Points |
|---|---|---|---|
| Essential (5) | 5/5 | 60 | 60 |
| Recommended (3) | 2/3 | 30 | 20 |
| Aspirational (2) | 1/2 | 10 | 5 |
| **Total** | | | **85** |

Golden: all essential pass = YES, composite 85 >= 80 = YES → **GOLDEN**.

---

## Failure Modes

| Failure | Criterion failed | Severity |
|---------|-----------------|----------|
| Lists contradictions but no quoted claims | C-02 | Essential |
| Labels contradictions "unclear" instead of blocking/advisory | C-03 | Essential |
| Closes with "investigate further" on every contradiction | C-04 | Essential |
| Only compares the same skill's two runs | C-05 | Essential |
| Reports "all signals agree" without naming what was compared | C-01 + C-05 | Essential x2 |
| 1 blocking contradiction but says "ready to specify" | C-07 | Recommended |
