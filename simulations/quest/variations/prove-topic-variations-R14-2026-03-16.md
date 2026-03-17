Written to `simulations/quest/golden/prove-topic-variate-R14-2026-03-16-v02.md`.

---

## prove-topic Variations — Round 14 (Rubric v14)

**Structural baseline**: R13 V-05 (count-gated exits + CLAIM CHAIN TABLE + displacement verdict on full R12 V-05 stack)

**Three new single axes probed**:

| Axis | What R13 V-05 lacks | Candidate |
|------|---------------------|-----------|
| `counter_hypothesis_resolution` | Incumbent rebuttal committed at Stage 1; resolved at Stage 5 with verdict cap | C-14 |
| `scout_signal_mapping` | Each CLAIM-N traces to a named scout section; UNGROUNDED claims excluded from verdict | C-15 |
| `evidence_type_tagging` | Sources tagged MARKET/TECHNICAL/USER/ACADEMIC; 2+ types required at synthesis | C-16 |

---

### V-01 — counter_hypothesis_resolution (single)

Adds `COUNTER-HYPOTHESIS` at Stage 1 (one sentence: incumbent's best rebuttal, written *before* the CLAIM INDEX so it sharpens claims). Adds `COUNTER-HYPOTHESIS RESOLUTION` at Stage 5 (REFUTED / PARTIALLY REFUTED / OPEN RISK with artifact citation + verdict cap rule: OPEN RISK caps verdict at "partially supported").

**Why it matters**: R13 V-05 builds the prosecution case but never stages the defense. Without a committed counter-hypothesis, the campaign is confirmation-biased — evidence is filtered for support rather than tested against the strongest opposing argument.

---

### V-02 — scout_signal_mapping (single)

Adds `SCOUT SIGNAL MAP` at Stage 1 (one row per claim: scout section + exact signal text). `CLAIM CHAIN TABLE` at Stage 5 gains a "Scout Anchor" column. Claims with no scout anchor are marked `UNGROUNDED` and excluded from the verdict calculation.

**Why it matters**: R13 V-05 requires `scout_source` in the frontmatter and a body reference, but allows claims untethered to any specific scout finding. A claim without a scout anchor is speculation, not grounded hypothesis.

---

### V-03 — evidence_type_tagging (single)

Sources at Stages 2 and 3 are tagged with evidence type (MARKET / TECHNICAL / USER / ACADEMIC). Stage 5 runs an `EVIDENCE BREADTH CHECK`: if fewer than 2 distinct types appear across both stages, it emits `EVIDENCE BREADTH WARNING` and caps all claim confidence at Medium.

**Why it matters**: R13 V-05's COUNT GATEs prevent thin coverage but not single-category coverage. Three market analyst reports are count-sufficient but type-narrow.

---

### V-04 — counter_hypothesis_resolution + scout_signal_mapping (combined)

V-01 + V-02. Closes the adversarial loop (counter-hypothesis) and the grounding loop (scout anchors) simultaneously. Non-conflicting; addresses orthogonal quality dimensions.

---

### V-05 — Full Integration (all three + complete R13 V-05 baseline)

All three new axes layered on R13 V-05. Tests whether counter-hypothesis resolution + scout signal mapping + evidence type tagging are simultaneously additive without disturbing any of the ten v14 passing mechanisms.

**R14 thesis**: If V-04 and V-05 score 100 on v14, the three new axes are confirmed additive. V-05 becomes the proposed baseline for a six-candidate rubric upgrade (C-11 through C-16), setting up the next `quest-rubric` call to formalize which candidates earn promotion.
