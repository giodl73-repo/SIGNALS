## Simplification Analysis

**Essential criteria to preserve** (from rubric — all 5 must pass for golden):
- C-01: All 5 sub-skills represented
- C-02: P1/P2/P3 labeling present
- C-03: Rogers diffusion model applied (listen-adoption not silent)
- C-04: Feedback vs. adoption posture distinguished
- C-05: Adoption-impact rating used (not severity)

---

### Phrases doing NO work

| Location | Text | Reason to cut |
|----------|------|---------------|
| Header | "full design validation campaign for" | "campaign for" is sufficient |
| Preamble intro | "The campaign orchestrates five sub-skills in this sequence:" | Absorbed into the imperative "Run these five sub-skills in order:" |
| Item 1 desc | "(what breaks or blocks shipment)" | Phase 1 body says this |
| Item 4 desc | "from users or stakeholders" | Redundant with "existing feedback signal" |
| Item 5 desc | "across innovators → laggards" | Phase 5 body covers this |
| After list | "Do not substitute review-customers for review-code — these are different lenses and review-customers does not satisfy C-01." | Rubric meta-coaching; the phase structure already enforces this |
| Phase 1 | "and any" → "and" | Minor word economy |
| Phase 2 | "A conceptual confusion that will block early-majority adoption outranks a polish gap that affects only power users." | Illustration of the rule already stated; the rule stands without it |
| Phase 4 | "or stated user pain points" | Fourth item in an already complete list |
| Phase 4 | "into one signal" | "Do not collapse these." is sufficient |
| Phase 5 | The five percentages "(innovators ~2.5%, early adopters ~13.5%, early majority ~34%, late majority ~34%, laggards ~16%)" | Rogers model is named; percentages add precision not required by any rubric criterion |
| Phase 5 | "as-is" | Redundant with "the design" |
| Phase 5 | "This is the input to the adoption-impact ranking in your final output." | Connective throat-clearing; the adoption-impact concept already introduced in Phase 2 |

---

### Simplified Prompt

```
You are running a validation campaign for topic: {{topic}}.

Run these five sub-skills in order. Do not skip or reorder:
  1. review-code      — technical floor
  2. review-design    — design quality and spec coherence
  3. review-users     — usability and user-task alignment
  4. listen-feedback  — existing feedback signal
  5. listen-adoption  — Rogers diffusion readiness

---

PHASE 1 — review-code

Analyze the implementation or spec for: correctness of contracts, edge-case
handling, schema constraints, performance implications, and hard blockers
to shipment. Label all findings P1 (blocker), P2 (significant), or P3 (minor).
For every P1 finding, name the status-quo workaround users currently rely on.

---

PHASE 2 — review-design

Analyze the design for: internal consistency, alignment with prior spec signals,
conceptual integrity, and adherence to platform conventions. Rate each finding
by its adoption impact (not its severity).

---

PHASE 3 — review-users

Analyze the user experience for: task completion clarity, friction points,
cognitive load, and discoverability. For each finding, estimate the user segment
most affected: innovators, early adopters, early majority, late majority,
or laggards. Weight your finding's adoption-impact score accordingly.

---

PHASE 4 — listen-feedback

Synthesize existing feedback signals (interviews, support tickets, prior research).
Distinguish feedback from adoption posture: feedback is what users said; adoption
posture is what that implies about their switching readiness. Do not collapse these.

---

PHASE 5 — listen-adoption

Apply the Rogers diffusion model. For each segment (innovators, early adopters,
early majority, late majority, laggards), estimate whether the design would unlock
or block adoption. Name the single biggest friction per segment.

---

OUTPUT FORMAT

Write your validation brief in this structure:

## Sub-Skill Results

For each of the five sub-skills, write a labeled section:
### review-code | review-design | review-users | listen-feedback | listen-adoption
Include a table skeleton per s
```

---

### Simplification Report

| Category | Removed |
|----------|---------|
| Rubric meta-coaching | "Do not substitute review-customers…does not satisfy C-01" (19 words) |
| Illustrative example | Phase 2 adoption-ranking example sentence (17 words) |
| Rogers percentages | Five segment percentages (20 words) |
| Connective prose | "This is the input to the adoption-impact ranking…" (13 words) |
| List over-description | Items 1/4/5 trailing clauses (13 words) |
| Minor redundancies | "any", "or stated user pain points", "into one signal", "as-is", intro reframing (12 words) |

**Essential criteria check:**
- C-01 All 5 sub-skills: ✓ (all 5 phases intact)
- C-02 P1/P2/P3 labeling: ✓ (kept verbatim)
- C-03 Rogers model applied: ✓ (Phase 5 unchanged in substance)
- C-04 Feedback/adoption posture distinct: ✓ (distinction kept verbatim)
- C-05 Adoption-impact not severity: ✓ ("Rate each finding by its adoption impact (not its severity)" kept verbatim)

```json
{"simplified_word_count": 280, "original_word_count": 374, "all_essential_still_pass": true}
```
