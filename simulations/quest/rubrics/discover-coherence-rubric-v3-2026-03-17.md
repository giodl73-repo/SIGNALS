Done. Here's what changed:

---

## v3 changes

**2 new aspirational criteria** promoted from R2 excellence signals:

| ID | Source | What it enforces |
|----|--------|-----------------|
| C-15 | R2 V-01/V-04/V-05 | Two-phase scan — PRE-SCAN (silent count) then FINDINGS HEADER (emit tally before first entry). The architectural mechanism that makes C-06 reliable in streaming output; single-pass generation cannot guarantee tally-before-first-entry. |
| C-16 | R2 V-03/V-05 | Severity-split resolution with token syntax — BLOCKING requires exact `/skill-name [--focus param]` token; ADVISORY requires concrete-action prose. Extends C-10 to enforce machine-parseable format and surface the blocking/advisory architectural distinction. |

**Scoring**: aspirational 6→8 criteria, 30→40 pts; total max 120→130; golden threshold 90→95 (~75% proportional bar maintained).

**Design rationale for each criterion:**
- C-15 is distinct from C-06: C-06 requires tally-at-top; C-15 requires the *mechanism* (two-pass) that makes that requirement structurally safe. A prompt that places the tally in its template but generates in one pass can still fail C-06 in streaming. Two-phase eliminates that failure mode entirely.
- C-16 is distinct from C-10: C-10 requires a skill reference for blocking contradictions; C-16 requires the *exact token format* (`/skill-name [--focus param]`), making the resolution directly runnable and syntactically distinguishable from advisory prose.
han two signals are present,
the output states this explicitly and declines to run the coherence check (insufficient
input — not a contradiction error).

**Pass condition**: At least two distinct discover signal files are identified by name/path
in the output, OR the output explicitly reports "fewer than 2 signals found, coherence
check cannot run."

---

### C-02 — Side-by-side contradiction listing

**Text**: Every contradiction surfaces both signals that conflict, quoting or directly
paraphrasing the specific claim from each signal in its own words (not just naming the
source files). The reader must be able to see exactly what Signal A said and exactly what
Signal B said without opening the source files.

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
switching-cost finding in discover-inertia"). The resolution must name a specific skill
to run, field to update, or claim to amend — not "investigate further."

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
such as "N contradictions: M blocking, K advisory" or a summary table with those counts.

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

## Aspirational Criteria (40 pts)

| ID | Criterion | Weight | Category | Origin |
|----|-----------|--------|----------|--------|
| C-09 | Contradiction taxonomy | aspirational | depth | v1 |
| C-10 | Suggested skill per blocking contradiction | aspirational | behavior | v1 |
| C-11 | Named phase gate with explicit failure message | aspirational | robustness | R1 excellence |
| C-12 | Failure-mode negation in resolution instruction | aspirational | depth | R1 excellence |
| C-13 | Priority-category-first table rendering | aspirational | format | R1 excellence |
| C-14 | Table-format output with named columns | aspirational | format | R1 excellence |
| C-15 | Two-phase scan structure | aspirational | robustness | R2 excellence |
| C-16 | Severity-split resolution with token syntax | aspirational | depth | R2 excellence |

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

### C-11 — Named phase gate with explicit failure message

*Promoted from R1 excellence signal (V-05).*

**Text**: The insufficient-signal gate emits a named, structured error state rather than
a prose stop condition. The output must include a recognizable gate label (e.g.,
"GATE FAILED") followed by the count found, the count required, and a directive for what
to run next — not just a sentence stating that the check cannot proceed.

Example: `GATE FAILED: 1 signal found, need 2+. Run discover skills before coherence check.`

**Why it matters**: A named error state cannot be silently dropped or misread as a
successful empty result. A prose "if fewer than 2, stop" can be omitted by any variation
that skips the guard; a GATE FAILED prefix is structurally unmistakable.

**Pass condition**: When fewer than two signals are present, the output emits a token
matching `GATE FAILED` (or an equivalent named gate label) followed by the count and a
next-step directive. A prose statement without a named gate token fails.

---

### C-12 — Failure-mode negation in resolution instruction

*Promoted from R1 excellence signal (V-05).*

**Text**: The resolution field or instruction explicitly names the failure mode it
prohibits, not only the behavior it requires. For the C-04 resolution requirement, the
instruction should read "specific skill to run, field to update, or claim to amend — not
'investigate further'" (or equivalent). Naming the exact anti-pattern in the instruction
reduces the rate of that failure more reliably than positive-only guidance.

**Why it matters**: Round 1 confirmed that positive-only resolution instructions
("provide a concrete next step") allow outputs to satisfy the letter of C-04 with
vague narrative. Naming the anti-pattern in the instruction reduces this failure mode
without changing the pass condition.

**Pass condition**: The resolution instruction or prompt text explicitly forbids "investigate
further" (or an equivalent vague resolution). A prompt that only states what to include,
without naming what to exclude, fails.

---

### C-13 — Priority-category-first table rendering

*Promoted from R1 excellence signal (V-05).*

**Text**: When contradiction output uses separate tables by category (e.g., inertia vs
other), the highest-decision-criticality category renders first — even if its table is
empty. This ensures the most consequential cross-skill comparison (typically inertia
contradictions, which directly block or enable product strategy) is always visible at
the top of the output and cannot be buried behind lower-priority categories.

**Why it matters**: Structural ordering enforces C-05 cross-skill coverage beyond the
minimum rule — a reader scanning the first table always hits the highest-stakes category.

**Pass condition**: The output renders a dedicated "Inertia Contradictions" section or
equivalent priority-first table before any general contradictions section, whether or
not it contains entries. A flat undifferentiated list that omits the priority category
header fails.

---

### C-14 — Table-format output with named columns

*Promoted from R1 excellence signal (V-02, V-05).*

**Text**: Contradiction entries are rendered in a Markdown table with at minimum these
named columns: `Severity`, `Contradiction`, `Resolution`. (Additional columns such as
`Type`, `Signal A`, `Signal B` are permitted.) Named columns structurally enforce
completeness: a blank Severity cell is immediately visible; a missing severity in prose
requires the reader to notice its absence.

**Why it matters**: R1 confirmed that table format eliminates the "labels contradictions
'unclear'" failure mode — the column header explicitly lists the two allowed values, and
any violation is conspicuous by structure rather than requiring active inspection.

**Pass condition**: Contradiction entries appear in a Markdown table with a `Severity`
column and a `Resolution` column (or equivalent named columns). A prose list without
column names fails.

---

### C-15 — Two-phase scan structure

*Promoted from R2 excellence signal (V-01, V-04, V-05).*

**Text**: The output generation uses a two-phase structure: a PRE-SCAN phase (silent —
count and classify all contradictions before emitting any output) followed by a FINDINGS
HEADER phase (emit the tally line, then emit entries). The tally emitted in the header
is computed over all contradictions found in the scan, not accumulated as entries are
written.

**Why it matters**: C-06 requires the tally to appear before the first entry, but a
single-pass prompt that places the tally "at the top" in its template can still emit
partial entries before the tally in streaming output. Two-phase structure — scan
everything first, then output — is architecturally incompatible with tally-before-first-entry
failure. R2 confirmed this is the minimal fix: V-01 adds only two-phase structure and
scores 100/130 on the v3 rubric.

**Pass condition**: The prompt or output explicitly separates a scan/count phase (no
output, all contradictions enumerated) from an output phase (tally header emitted first,
then entries). A prompt with a single generation step that interleaves scanning and
writing fails.

---

### C-16 — Severity-split resolution with token syntax

*Promoted from R2 excellence signal (V-03, V-05).*

**Text**: Resolution instructions are split by severity class with distinct formats:
- `blocking` contradictions: resolution must use the exact token syntax
  `Resolve with: /skill-name [--focus param]` — a machine-parseable directive
  that names the specific skill invocation needed to generate resolving evidence
- `advisory` contradictions: resolution must name a concrete action (field to update,
  claim to amend, reframing to apply) — prose is permitted, token syntax is not required

Both severity classes prohibit "investigate further" (inherited from C-12). The split
surfaces the architectural difference: blocking means run more evidence; advisory means
amend existing findings.

**Why it matters**: C-10 requires a skill reference for blocking contradictions but
permits any narrative that mentions a skill name. C-16 enforces the token format, making
blocking resolutions structurally distinct from advisory ones and directly runnable
by the team.

**Pass condition**: Every BLOCKING contradiction resolution uses the `/skill-name [--focus
param]` token format. Every ADVISORY contradiction resolution names a concrete action
without requiring the token. A blocking resolution that names a skill in prose without
the token format fails this criterion.

---

## Scoring

### Point allocation

| Tier | Criteria | Points each | Tier max |
|------|----------|-------------|----------|
| Essential | C-01 to C-05 | 12 | 60 |
| Recommended | C-06 to C-08 | 10 | 30 |
| Aspirational | C-09 to C-16 | 5 | 40 |
| **Total** | | | **130** |

### Golden threshold

- All 5 essential criteria must pass (any essential fail = not golden)
- Composite score >= 95 to be considered golden

### Scoring example

| Criteria set | Pass count | Points |
|---|---|---|
| Essential (5) | 5/5 | 60 |
| Recommended (3) | 3/3 | 30 |
| Aspirational (8) | 2/8 | 10 |
| **Total** | | **100** |

Golden: all essential pass = YES, composite 100 >= 95 = YES → **GOLDEN**.

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
| Tally appears after contradictions, not before | C-06 | Recommended |
| Insufficient-signal guard emits prose stop, not named gate token | C-11 | Aspirational |
| Resolution instruction says what to include but not what to exclude | C-12 | Aspirational |
| Flat contradiction list buries inertia entries after lower-priority ones | C-13 | Aspirational |
| Contradiction entries in prose — no named Severity or Resolution column | C-14 | Aspirational |
| Single-pass generation interleaves scan and output — tally computed mid-stream | C-15 | Aspirational |
| Blocking resolution names skill in prose without /skill-name token syntax | C-16 | Aspirational |

---

## Changelog

### v3 (2026-03-17)

**New criteria**: C-15, C-16 promoted from R2 excellence signals.

**C-15 — Two-phase scan structure**: PRE-SCAN (silent count and classify) then FINDINGS
HEADER (emit tally before first entry). Source: V-01/V-04/V-05 structural pattern that
closed C-06 universally in R2. Architecturally incompatible with single-pass tally-at-top
failure; two-pass structure is the minimal fix.

**C-16 — Severity-split resolution with token syntax**: BLOCKING resolutions use exact
`/skill-name [--focus param]` token format; ADVISORY resolutions use concrete-action
prose. Source: V-03/V-05 severity-split resolution rule block in R2. Extends C-10
(skill reference) by enforcing machine-parseable token syntax and surfacing the
blocking/advisory architectural distinction.

**Scoring**: aspirational tier expanded from 6 criteria (30 pts) to 8 criteria (40 pts);
total max raised from 120 to 130; golden threshold raised from ≥90 to ≥95.

**Round 2 summary**: All 5 variations golden. Top score 120/120 (V-05, perfect on v2
rubric). Three R1 gaps all closed (C-06, C-09, C-10). Key finding: table format closes
C-09, C-10, C-13, C-14 simultaneously — prose ceiling is 105/120. Two-phase scan is
the architectural fix for C-06. Severity-split resolution closes C-10 and C-12 together.
Two new patterns promoted to C-15 and C-16.

---

### v2 (2026-03-17)

**New criteria**: C-11, C-12, C-13, C-14 promoted from R1 excellence signals.

**Criterion updates**:
- C-02: added "in its own words" phrasing (from V-04 excellence signal — lower
  interpretation ambiguity than "exact quote or close paraphrase")
- C-04: added "not 'investigate further'" negation clause directly to criterion text
  (from V-05 excellence signal — failure-mode negation in the criterion itself, not
  only in the rubric instruction)

**Scoring**: aspirational tier expanded from 2 criteria (10 pts) to 6 criteria (30 pts);
total max raised from 100 to 120; golden threshold raised from ≥80 to ≥90.

**Round 1 summary**: Top score 80/100 (V-02, V-03, V-04, V-05). Three universal gaps:
C-06 (tally at top), C-09 (taxonomy), C-10 (skill per blocking). Four excellence
patterns surfaced and promoted to aspirational criteria (C-11–C-14).
