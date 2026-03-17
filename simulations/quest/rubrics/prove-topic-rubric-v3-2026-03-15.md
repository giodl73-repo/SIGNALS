Written to `simulations/quest/rubrics/prove-topic-rubric-v3-2026-03-15.md`.

---

**Two new criteria extracted from Round 2:**

| ID | Source | Pattern |
|----|--------|---------|
| C-14 | V-04/V-05 | Counter-evidence is a mandatory synthesis section with a required fallback instruction — not conditional on having found any. V-01–V-03 allow elision when evidence is uniform; V-04/V-05 make it unconditional. |
| C-15 | V-04/V-05 | Gate clearance state (`gate_s_cleared: true`) propagated into hypothesis frontmatter. Gate defined (C-11) != gate clearance traceable in artifact. Without this, gate compliance can't be audited from the artifact alone. |

**Weight outcome:** Per-criterion aspirational weight unchanged at 4 pts. Max rises from 100 to 108. Golden threshold stays at **80** — which equals essential + recommended exactly (50 + 30). The aspirational tier is now structurally bonus above the bar, not required to cross it. The v2 → v3 shift makes that design intent explicit rather than coincidental.
, stage, or chapter for each of the five
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

### C-14 — Counter-evidence unconditionally required in synthesis

*Excellence signal from V-04/V-05.*

PASS: The synthesis section requires counter-evidence as a named, mandatory field — not as
a conditional section or optional addition. The instruction must make counter-evidence
unconditionally required, with an explicit fallback for the case where none was gathered
during the campaign (e.g., "If no counter-evidence was found, state why."). A synthesis
that says "include counter-evidence if any was found" is a PARTIAL (2 pts).

Failure mode addressed: Synthesis sections that silently elide counter-evidence when all
evidence was uniformly positive, inflating confidence in the output. The V-04 pattern —
synthesis lists Counter-Evidence as a mandatory section alongside Findings and Confidence,
with a required fallback instruction — is the exemplar.

### C-15 — Gate clearance state propagated into hypothesis artifact

*Excellence signal from V-04/V-05.*

PASS: After GATE S clears, the hypothesis artifact or its frontmatter includes an explicit
field recording gate clearance (e.g., `gate_s_cleared: true`). This provides a traceable
record that the gate was checked — visible in the artifact itself, not only in the session
preamble. A GATE block with no artifact-level record of clearance satisfies C-11 but not
C-15. FAIL if C-11 is FAIL (no gate defined at all). PARTIAL (2 pts) if the gate clears
but clearance is recorded only in the session log, not in the hypothesis frontmatter.

Failure mode addressed: Gate instructions that leave no trace in the artifact chain, making
it impossible to audit gate compliance from the artifact alone without replaying the full
session.

---

## Design Rationale

### Essential tier

Focuses on the three things that make this skill an orchestrator rather than a single-step
skill: all stages ran (C-01), context was loaded from scout (C-02), and artifacts were
written progressively (C-03). C-04/C-05 ensure the terminal output is usable and
discoverable.

### Recommended tier

Adds traceability (C-06, C-07) and downstream handoff (C-08). All three were full PASS in
the highest-scoring Round 1 and Round 2 variations; partial failures here are the primary
separator between 85- and 95-range scores. The recommended tier and essential tier together
sum to exactly 80 — the golden threshold — making these six criteria the complete baseline
for a qualifying skill output.

### Aspirational tier

Targets the failure modes unique to orchestration. The seven criteria form three pairs plus
one standalone:

- **C-09, C-12**: Confidence inflation from thin evidence. C-09 checks propagation;
  C-12 checks whether the comparator that makes thin evidence meaningful was established
  upfront. Complementary — C-12 is the upstream condition that makes C-09 actionable.

- **C-10, C-11**: Opaque progress and silent gateway failures. C-10 asks for narrative
  confirmation; C-11 asks for a hard blocking gate before hypothesis formation. Together
  they prevent the failure mode where a variation looks complete but the scout-load step
  was nominal.

- **C-13, C-15**: Prefix drift and gate-trace gaps. C-13 checks per-instruction path
  enforcement; C-15 checks that gate clearance is recorded in the artifact. Both address
  the same failure pattern: a correct instruction at session open that leaves no trace in
  the artifact chain.

- **C-14** (standalone): Counter-evidence elision. Makes the synthesis unconditionally
  require counter-evidence rather than conditionally include it, closing a confidence
  inflation path that is invisible to C-04.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-15 | Initial rubric, 10 criteria (5 essential, 3 recommended, 2 aspirational), max 100 |
| v2 | 2026-03-15 | Add C-11, C-12, C-13 from Round 1 excellence signals; rebalance weights: essential 10 pts, recommended 10 pts, aspirational 4 pts; max unchanged at 100 |
| v3 | 2026-03-15 | Add C-14, C-15 from Round 2 excellence signals; max rises to 108; golden threshold unchanged at 80 (essential + recommended = 80 exactly; aspirational is bonus above the bar) |

### Weight change note (v2 → v3)

v2: max 100, aspirational 5 criteria x 4 pts = 20 pts.
v3: max 108, aspirational 7 criteria x 4 pts = 28 pts.

Essential and recommended weights are unchanged. Max rises by 8 to accommodate the two new
aspirational criteria at full 4-pt weight. The golden threshold holds at 80, which equals
essential + recommended exactly — the same structural relationship as v2. Aspirational
criteria remain bonus above the baseline; the ceiling rises but the bar does not.
