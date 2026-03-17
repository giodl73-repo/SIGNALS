Written to `simulations/quest/rubrics/prove-topic-rubric-v2-2026-03-15.md`.

---

**Three new aspirational criteria extracted from Round 1:**

| ID | Source | Pattern captured |
|----|--------|-----------------|
| C-11 | V-01 (score 96) | GATE S hard-blocks hypothesis formation until scout artifact confirmed. C-07 (explicit handoff) passes when the anchor is named; C-11 passes only when advancement is structurally blocked. |
| C-12 | V-04 (only full C-09 PASS) | Status-quo comparator established at session open, referenced at each evidence stage, traced to synthesis. All other C-09 partials flagged thin evidence at Stage 4 without an upstream baseline — making the caveat untethered. |
| C-13 | V-01 vs V-03/V-04/V-05 | Per-artifact path enforcement on every write instruction. The three C-05 partials defined the prefix once at opening and relied on drift-free recall. C-05 checks consistency; C-13 checks whether the mechanism to enforce it was present. |

**Weight rebalance:** essential 12→10, recommended 8→10, aspirational 8→4 (now 5 criteria). Max stays 100, threshold stays 80. Recommended gains weight — C-06/C-07/C-08 proved more discriminating than originally scored. Aspirational per-criterion drops to make room for the expansion.
tional | format |

---

## Scoring Weights

| Tier | Criteria | Points each | Total |
|------|----------|-------------|-------|
| Essential | C-01 – C-05 | 10 | 50 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-13 | 4 | 20 |
| **Total** | | | **100** |

**Golden threshold**: all 5 essential PASS + composite >= 80 (max 100).

---

## Essential Criteria (10 pts each)

### C-01 — All five sub-skills execute

PASS: The response contains a distinct section, stage, or chapter for each of the five
sub-skills — hypothesis formation, web search, interview, prototype, and synthesis. A
structural omission (e.g., prototype stage absent) is a FAIL regardless of prose quality.

### C-02 — Hypothesis grounded in scout signals

PASS: The hypothesis is formed after loading a named scout artifact. An anchor field (slug,
path reference, or explicit "from scout" statement) must appear before the hypothesis is
stated. A hypothesis formed without any scout context is a FAIL.

### C-03 — Artifact written per stage

PASS: Each stage explicitly confirms that an artifact was written (or instructs the model to
write one) before advancing. Stages that complete with no artifact instruction are a FAIL.

### C-04 — Final synthesis is terminal and complete

PASS: The synthesis stage is the last stage and contains a defined set of required sections
(minimum: findings, confidence level, handoff). Synthesis placed mid-sequence or missing
required fields is a FAIL.

### C-05 — Topic prefix consistent across all artifacts

PASS: Every artifact path referenced in the response starts with `{topic}-`. A prefix
defined once at session opening but not repeated in per-artifact write instructions is a
PARTIAL (5 pts). Per-artifact path naming in each write instruction is full PASS.

---

## Recommended Criteria (10 pts each)

### C-06 — Stage order enforced

PASS: The five sub-skills are presented in a fixed sequence with a forward-only constraint.
No mechanism to skip back, re-run stages in arbitrary order, or proceed without completing
the prior stage is a FAIL.

### C-07 — Scout signal handoff is explicit

PASS: A named scout anchor (slug, path, or `scout-record` field) is required in the
hypothesis frontmatter or stage-entry block. The scout artifact must be named, not just
generally referenced. A vague "use your scout research" instruction without naming the
artifact is a PARTIAL (4 pts).

### C-08 — Synthesis signals readiness for topic-story

PASS: The synthesis stage includes a handoff indicator pointing to `topic-story` or
equivalent downstream artifact. A synthesis that ends without a named next step is a
PARTIAL (4 pts).

---

## Aspirational Criteria (4 pts each)

### C-09 — Thin-evidence acknowledgment propagates

PASS: If any evidence stage (web search, interview, prototype) yields thin or conflicting
evidence, that signal is carried forward explicitly to the synthesis. A flag at Stage 4
that is not referenced in Stage 5 is a PARTIAL (2 pts). Full PASS requires the synthesis
to name the thin-evidence finding and qualify confidence accordingly.

### C-10 — Progress narrated per stage

PASS: Each stage produces an explicit natural-language confirmation of what was found or
done before advancing — not just a structural gate. Verdict tokens alone (e.g., `[X]`,
`--`) without accompanying prose acknowledgment are a PARTIAL (2 pts).

### C-11 — Hypothesis entry is hard-gated on scout confirmation

*Excellence signal from V-01.*

PASS: The scout-load step structurally prevents any hypothesis work until the scout
artifact is confirmed present. Examples: an explicit GATE block before Stage 1, a
forward-condition checkbox required before the hypothesis section opens, or an explicit
"do not proceed until scout-record is on file" instruction. A named anchor (satisfying
C-07) without a blocking gate is insufficient for C-11. The V-01 GATE S pattern is the
exemplar.

Failure mode addressed: variations that name a scout anchor but allow hypothesis formation
to proceed from general knowledge rather than the loaded artifact.

### C-12 — Thin-evidence comparator anchored at session open

*Excellence signal from V-04.*

PASS: A status-quo baseline or incumbent comparator is named at the session's opening —
before any evidence gathering — and explicitly referenced at each evidence stage. This
grounds any thin-evidence acknowledgment in a concrete alternative rather than an
isolated caveat. A comparator introduced only at Stage 4 or only in the synthesis is a
PARTIAL (2 pts). The V-04 pattern — "status-quo comparator at campaign opening →
referenced at each evidence stage → Warning+effect at Stage 4 traced to synthesis" — is
the exemplar.

Failure mode addressed: C-09 partials where thin-evidence flags appear late and are not
connected to a pre-established baseline, making the confidence qualification untethered.

### C-13 — Per-artifact path enforcement on each write instruction

*Excellence signal from V-01.*

PASS: Every write instruction in the response names the full artifact path (e.g.,
`{topic}-hypothesis-{date}.md`), not just the topic prefix or a filename stem. A prefix
defined once at session opening without per-instruction path naming is a PARTIAL (2 pts).
This prevents prefix drift across sub-stages and multi-turn sessions. V-01's "`{topic}-`
in every path" enforcement pattern is the exemplar.

Failure mode addressed: C-05 partials where a correctly-defined opening prefix drifts by
Stage 3–4 because individual write instructions do not restate it.

---

## Design Rationale

### Essential tier

Focuses on the three things that make this skill an orchestrator rather than a single-step
skill: all stages ran (C-01), context was loaded from scout (C-02), and artifacts were
written progressively (C-03). C-04/C-05 ensure the terminal output is usable and
discoverable.

### Recommended tier

Adds traceability (C-06, C-07) and downstream handoff (C-08). All three were full PASS in
the highest-scoring Round 1 variations; partial failures here are the primary separator
between 85- and 95-range scores.

### Aspirational tier

Targets the failure modes unique to orchestration:

- **C-09, C-12**: Confidence inflation from thin evidence. C-09 checks propagation;
  C-12 checks whether the comparator that makes thin evidence meaningful was established
  upfront. These are complementary — C-12 is the upstream condition that makes C-09
  actionable.

- **C-10, C-11**: Opaque progress and silent gateway failures. C-10 asks for narrative
  confirmation; C-11 asks for a hard blocking gate before hypothesis formation.
  Together they prevent the failure mode where a variation looks complete but the
  scout-load step was nominal.

- **C-13**: Prefix drift in multi-stage sessions. C-05 checks consistency; C-13 checks
  the enforcement mechanism. A variation can satisfy C-05 by coincidence (no drift
  happened) without satisfying C-13 (no enforcement was present to prevent it).

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-15 | Initial rubric, 10 criteria (5 essential, 3 recommended, 2 aspirational), max 100 |
| v2 | 2026-03-15 | Add C-11, C-12, C-13 from Round 1 excellence signals; rebalance weights: essential 10 pts, recommended 10 pts, aspirational 4 pts; max unchanged at 100 |

### Weight change note (v1 → v2)

v1: essential 12 pts, recommended 8 pts, aspirational 8 pts (2 criteria).
v2: essential 10 pts, recommended 10 pts, aspirational 4 pts (5 criteria).

Recommended tier gains 2 pts per criterion — traceability and handoff proved more
discriminating in Round 1 than initially weighted. Aspirational per-criterion weight drops
from 8 to 4 as the tier expands from 2 to 5 criteria; total aspirational ceiling rises from
16 to 20. Max score is unchanged at 100. Golden threshold is unchanged at >= 80.
