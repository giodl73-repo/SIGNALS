Scorecard written. Here is the full scoring output:

---

## prove-topic — Quest Score — Round 1 (Rubric v14)

**Variate source**: `prove-topic-variate-R1-2026-03-16-v14.md`

| Variation | E (5) | R (3) | A (2) | Composite | Golden |
|-----------|-------|-------|-------|-----------|--------|
| V-01 — Lifecycle Emphasis | 5/5 | 3/3 | 1.5/2 | ~97.5 | YES |
| V-02 — Output Format | 5/5 | 3/3 | 2/2 | 100 | YES |
| V-03 — Phrasing Register | 5/5 | 3/3 | 1.5/2 | ~97.5 | YES |
| V-04 — Inertia Framing | 5/5 | 3/3 | 2/2 | 100 | YES |
| **V-05 — Combined** | 5/5 | 3/3 | 2/2 | **100** | YES |

**All 5 variations are golden.** Top score: 100. Top integration candidate: V-05.

**C-09 gap in V-01 and V-03**: Both score partial on C-09 because synthesis instructs "state adjusted confidence" but doesn't require naming the source stage or specific weakened claim. V-04 and V-05 close this organically by threading `weakens: [claim vs {status_quo}]` into the THIN flag format at Stages 2-3, so the synthesis table consumes it naturally.

**Top excellence signals from V-05**:
1. CAMPAIGN OPEN emit chain satisfies C-02, C-06, and C-10 through one structural mechanism
2. `Source Stage` column in synthesis table makes C-09 a structural requirement, not prose
3. `weakens: [specific claim]` in THIN flag format creates a self-threading chain from discovery to qualification

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["CAMPAIGN OPEN emit chain satisfies C-02, C-06, C-10 simultaneously through one structural mechanism", "Source Stage column in synthesis table converts C-09 from prose instruction to structural table requirement", "Displacement-framed THIN flag format (weakens: [claim vs status_quo]) at discovery creates self-threading chain to synthesis confidence table"]}
```
RMED is emitted" |
| C-07 | Scout anchor in hypothesis artifact         | PASS    | Stage 1 frontmatter: `scout_source: simulations/scout/{topic}-scout-{date}.md` |
| C-08 | Evidence gaps flagged at point of discovery | PASS    | Stages 2 and 3: "flag at point of discovery: THIN: [area] — [gap found]"; Stage 4 aggregates and maps flags to hypothesis claims |
| C-09 | Thin-evidence propagates to synthesis       | PARTIAL | Stage 5: "For any THIN-flagged claims, state adjusted confidence." Instructs confidence but does not require naming source stage or specific weakened claim. C-09 full PASS requires both. |
| C-10 | Hypothesis structurally blocked until scout | PASS    | STAGE 0 emits SCOUT CONFIRMED; GATE-1 CHECK blocks Stage 1 until that emit is present — structural chain |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: C-09 PARTIAL (~2.5 pts) + C-10 PASS (5 pts) = ~7.5/10
**Composite**: (5/5 * 60) + (3/3 * 30) + 7.5 = **97.5**
**Golden**: YES

**C-09 gap**: Synthesis says "state adjusted confidence" but does not prompt source-stage attribution or weakened-claim naming. One additional constraint closes it: "for each flag: name source stage, weakened hypothesis element, adjusted confidence."

---

## V-02 — Output Format (Path Declaration Table + Preconditions)

| ID   | Criterion                                   | Result  | Evidence |
|------|---------------------------------------------|---------|---------|
| C-01 | All five sub-skills in sequence             | PASS    | Stages 1-5 with precondition-based sequencing |
| C-02 | Scout artifact named before hypothesis      | PASS    | SETUP section globs + halts if absent; sets scout_source; Stage 1 precondition references it |
| C-03 | Progressive writes — one per stage          | PASS    | Each stage has a WRITE instruction |
| C-04 | Synthesis signals readiness for topic-story | PASS    | Stage 5: `Close with the explicit statement: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full paths on every write instruction       | PASS    | All five WRITE lines include full paths; path declaration table reinforces but does not replace per-instruction naming |
| C-06 | Forward-only gate before Stage 1            | PASS    | SETUP halts if scout absent; Stage 1 Precondition: "scout_source confirmed from setup above" — equivalent checkpoint |
| C-07 | Scout anchor in hypothesis artifact         | PASS    | Stage 1 frontmatter table: `scout_source | simulations/scout/{topic}-scout-{date}.md` |
| C-08 | Evidence gaps flagged at point of discovery | PASS    | Stages 2 and 3: "Flag evidence gaps immediately when found — do not defer to synthesis: THIN: [area] — [specific gap]"; Stage 4 aggregation table |
| C-09 | Thin-evidence propagates to synthesis       | PASS    | Stage 5 table: `| Claim | Source Stage | Gap | Confidence |` — explicit Source Stage column required. Full traceability from flag to synthesis. |
| C-10 | Hypothesis structurally blocked until scout | PASS    | SETUP: "If absent: halt and emit 'No scout artifact for {topic}. Run a scout skill first.'" — no fallback; Stage 1 precondition enforces it |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Composite**: 100
**Golden**: YES

---

## V-03 — Phrasing Register (Conversational)

| ID   | Criterion                                   | Result  | Evidence |
|------|---------------------------------------------|---------|---------|
| C-01 | All five sub-skills in sequence             | PASS    | Stages 1-5 in order under soft "you're running..." register |
| C-02 | Scout artifact named before hypothesis      | PASS    | "Before you start — find the scout artifact: simulations/scout/{topic}-scout-*.md"; halt if absent; Stage 1 reads it |
| C-03 | Progressive writes — one per stage          | PASS    | Each stage ends with "write it to: simulations/prove/.../..." |
| C-04 | Synthesis signals readiness for topic-story | PASS    | Stage 5: `Close the synthesis with this explicit statement: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full paths on every write instruction       | PASS    | All five write instructions include full paths inline |
| C-06 | Forward-only gate before Stage 1            | PASS    | "Before you start" section: "If no scout artifact exists, stop here" — before Stage 1, references scout presence |
| C-07 | Scout anchor in hypothesis artifact         | PASS    | Stage 1: "Include a `scout_source` field in the frontmatter pointing to the scout artifact path" — named field explicitly required |
| C-08 | Evidence gaps flagged at point of discovery | PASS    | Stages 2 and 3: "if something is thin or absent, flag it inline: THIN: [area] — [what's missing]"; Stage 4: "Collect all THIN flags. Map each to the specific hypothesis claim it weakens." |
| C-09 | Thin-evidence propagates to synthesis       | PARTIAL | Stage 5: "For each claim that had weak evidence (THIN flags), say how confident you are in that claim." Asks for per-claim confidence but does not require naming source stage. C-09 full PASS requires naming source stage + weakened claim. |
| C-10 | Hypothesis structurally blocked until scout | PASS    | "Before you start: If no scout artifact exists, stop here" — explicit stop with no fallback, before Stage 1 opens |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: C-09 PARTIAL (~2.5 pts) + C-10 PASS (5 pts) = ~7.5/10
**Composite**: ~97.5
**Golden**: YES

**Finding**: Conversational register passes 9 of 10 criteria without any structural degradation. C-09 is the only gap and it is a phrasing choice, not a register limitation — soft register can satisfy C-09 with one additional phrase.

---

## V-04 — Inertia Framing (CAMPAIGN OPEN + Displacement)

| ID   | Criterion                                   | Result  | Evidence |
|------|---------------------------------------------|---------|---------|
| C-01 | All five sub-skills in sequence             | PASS    | Stages 1-5 in order under displacement framing |
| C-02 | Scout artifact named before hypothesis      | PASS    | CAMPAIGN OPEN: locate scout artifact, halt if absent, read it; extract status_quo and inertia from scout findings |
| C-03 | Progressive writes — one per stage          | PASS    | Each stage has WRITE instruction |
| C-04 | Synthesis signals readiness for topic-story | PASS    | Stage 5: `Close with: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full paths on every write instruction       | PASS    | All five WRITE lines name full paths inline |
| C-06 | Forward-only gate before Stage 1            | PASS    | CAMPAIGN OPEN: "If absent: halt. Emit 'BLOCKED — no scout artifact for {topic}. Run scout first.'" — before Stage 1 with scout-presence check |
| C-07 | Scout anchor in hypothesis artifact         | PASS    | Stage 1 frontmatter: `scout_source: simulations/scout/{topic}-scout-{date}.md` |
| C-08 | Evidence gaps flagged at point of discovery | PASS    | Stages 2 and 3: `THIN: [area] — [gap] — weakens: [specific claim vs {status_quo}]` — flags name the displacement claim weakened at point of discovery. Strongest C-08 specification across all variations. |
| C-09 | Thin-evidence propagates to synthesis       | PASS    | Stage 5 table: `| Displacement Claim (vs {status_quo}) | Gap Source | Adjusted Confidence |` — Gap Source = originating stage, Displacement Claim = weakened element. Full C-09 requirements met. |
| C-10 | Hypothesis structurally blocked until scout | PASS    | CAMPAIGN OPEN: halt + emit BLOCKED; "No stage begins until CAMPAIGN OPEN is emitted with all three fields named" — structural block via emit requirement |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Composite**: 100
**Golden**: YES

**Excellence note**: The inertia framing makes C-08 and C-09 organic. Flags using "weakens: [specific claim vs {status_quo}]" at discovery point mean the synthesis table is populated by natural carry-forward, not a separate compliance instruction. The chain from gap discovery to synthesis qualification is self-threading.

---

## V-05 — Combined (Lifecycle + Format + Inertia)

| ID   | Criterion                                   | Result  | Evidence |
|------|---------------------------------------------|---------|---------|
| C-01 | All five sub-skills in sequence             | PASS    | Stages 1-5 with GATE CHECK per stage in order |
| C-02 | Scout artifact named before hypothesis      | PASS    | CAMPAIGN OPEN globs, halts if absent, reads scout; Stage 1 GATE CHECK requires CAMPAIGN OPEN emitted with all fields named |
| C-03 | Progressive writes — one per stage          | PASS    | Each stage has WRITE instruction; ARTIFACT PATHS table at campaign open declares all five, each stage echoes the matching path |
| C-04 | Synthesis signals readiness for topic-story | PASS    | Stage 5: `Close with: Evidence brief for {topic} is ready for /topic-story.` |
| C-05 | Full paths on every write instruction       | PASS    | All five WRITE lines name full paths; campaign-open table + per-stage echo = strongest C-05 enforcement across variations |
| C-06 | Forward-only gate before Stage 1            | PASS    | STAGE 1 GATE CHECK: `[ ] CAMPAIGN OPEN emitted. [ ] scout_source, status_quo, inertia all named. If not: BLOCKED at Stage 1. Halt.` — strongest gate across all variations |
| C-07 | Scout anchor in hypothesis artifact         | PASS    | Stage 1 frontmatter table: `scout_source | simulations/scout/{topic}-scout-{date}.md` |
| C-08 | Evidence gaps flagged at point of discovery | PASS    | Stages 2 and 3: `THIN: [area] — [gap] — weakens: [specific claim vs {status_quo}]`; Stage 4: aggregation table with "Displacement Claim Weakened" column |
| C-09 | Thin-evidence propagates to synthesis       | PASS    | Stage 5 table: `| Displacement Claim (vs {status_quo}) | Source Stage | Gap | Adjusted Confidence |` — explicit Source Stage column, named displacement claim, adjusted confidence. Full pass. |
| C-10 | Hypothesis structurally blocked until scout | PASS    | STAGE 1 GATE CHECK with checkboxes + "BLOCKED at Stage 1. Halt." combined with CAMPAIGN OPEN emit requirement. Deepest structural block across all variations. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 2/2
**Composite**: 100
**Golden**: YES

---

## C-09 Diagnostic — V-01 and V-03

Both variations instruct "state adjusted confidence per THIN-flagged claim" in synthesis but do not prompt source-stage attribution or specific-claim naming. The rubric requires both for C-09 full PASS.

The gap is one additional phrase in the synthesis instruction:
- V-01 fix: after "state adjusted confidence", add "for each flag: source stage (Stage 2 or 3), weakened hypothesis element, adjusted confidence"
- V-03 fix: after "say how confident you are", add "name which stage first flagged it and which part of the hypothesis it weakens"

V-04 and V-05 achieve this without an extra instruction by threading `weakens: [specific claim]` into the THIN flag format at Stages 2-3. The synthesis table then consumes the annotation naturally.

---

## Excellence Signals — V-05 (Top Integration Candidate)

**CAMPAIGN OPEN emit chain**: Emitting `(scout_source, status_quo, inertia)` as a named state object before Stage 1 satisfies C-02, C-06, and C-10 simultaneously through one mechanism rather than three separate instructions. Stage 1 GATE CHECK blocks on CAMPAIGN OPEN being emitted — this is structurally stronger than a prose "stop if absent" instruction.

**Source Stage column in synthesis table**: V-02, V-04, and V-05 place a `Source Stage` column in the synthesis confidence table. This converts C-09 from a prose requirement into a structural table requirement — the column must be populated or the table is visibly incomplete. Structural tables are harder to skip than prose instructions.

**Displacement-framed THIN flag format**: `THIN: [area] — [gap] — weakens: [specific claim vs {status_quo}]` in Stages 2-3 creates a direct chain to the synthesis table: the "weakens" annotation is exactly what populates the "Displacement Claim" column. No separate C-09 carry-forward instruction needed — the annotation format provides the data in the right shape.
