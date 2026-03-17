---
skill: quest-score
skill_target: prove-topic
round: R2
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations_scored: [V-01, V-02, V-03, V-04, V-05]
top_score: 100
max_score: 100
all_essential_pass: true
rubric_ceiling_hit: true
new_patterns:
  - "Exit-signal chaining ('SCOUT READY cannot fire without found file' + 'STAGE N cannot begin until SCOUT READY fires') satisfies C-10 as a two-step structural block without GATE block headers"
  - "Two-write synthesis makes C-09 structural by construction -- Write A enumerates per-claim confidence adjustments by artifact definition, not by closing instruction"
  - "Role-sequence framing (SCOUT-LOADER -> ANALYST -> SYNTHESIZER) satisfies C-02 and C-07 by architecture -- the role that owns scout loading inherently precedes hypothesis formation"
---

# prove-topic -- Round R2 Score Sheet (Rubric v14)

## Rubric Structure

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01 to C-05 | 12 | 60 |
| Recommended | C-06 to C-08 | 10 | 30 |
| Aspirational | C-09 to C-10 | 5 | 10 |
| **Total** | | | **100** |

Golden threshold: all 5 essential PASS + composite >= 80.
Round 2 primary discovery: rubric v14 ceiling reached. Four of five variations score 100.
Only discriminating criterion: C-10 (structural block) -- minimalist prose is borderline.

---

## V-01 -- Minimalism

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All five sub-skills in sequence | 12 | PASS | Stages 1-5 named and ordered: hypothesis -> websearch -> intelligence -> analysis -> synthesize. |
| C-02 | Scout artifact loaded before hypothesis | 12 | PASS | "Before Stage 1: locate the scout artifact... Read the file before forming the hypothesis." |
| C-03 | Progressive artifact writes | 12 | PASS | 5 explicit Write instructions with distinct paths, one per stage. |
| C-04 | Synthesis signals readiness for topic-story | 12 | PASS | "Close with this exact statement: Evidence brief for {topic} is ready for /topic-story." |
| C-05 | Artifact paths on every write instruction | 12 | PASS | All 5 writes carry full paths. |
| C-06 | Forward-only stage order with gate | 10 | PASS | "Before Stage 1: if no file found, stop and emit... Do not proceed." Equivalent checkpoint; blocks on absent scout. |
| C-07 | Scout anchor in hypothesis artifact | 10 | PASS | "Include `scout_source: simulations/scout/{topic}-scout-{date}.md` in the frontmatter." In-artifact named field. |
| C-08 | Evidence gaps flagged at discovery | 10 | PASS | Stage 2: "note at point of discovery -- do not defer." Stage 3: "Note thin inline when found." |
| C-09 | Thin-evidence propagates to synthesis | 5 | PASS | Stage 5: "state your adjusted confidence explicitly, naming the source stage and the weakened claim." |
| C-10 | Hypothesis structurally blocked until scout | 2.5 | PARTIAL | "stop and emit... Do not proceed" is a functional abort. Stage 1 body adds advisory "Do not begin this stage without a confirmed scout artifact." Functional block present, but no formal signal, gate field, or role mechanism. Borderline PARTIAL per rubric. |

**V-01: 97.5/100 -- all essential PASS**

---

## V-02 -- Exit-Signal Framing

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All five sub-skills in sequence | 12 | PASS | SETUP + Stages 1-5 with exit signal dependencies enforcing forward-only order. |
| C-02 | Scout artifact loaded before hypothesis | 12 | PASS | SETUP: "SCOUT READY cannot fire without a found file." Halts on absent scout before Stage 1 opens. |
| C-03 | Progressive artifact writes | 12 | PASS | One Write per stage; exit signal fires only after write. |
| C-04 | Synthesis signals readiness for topic-story | 12 | PASS | "Emit: CAMPAIGN COMPLETE. Evidence brief for {topic} is ready for /topic-story." |
| C-05 | Artifact paths on every write instruction | 12 | PASS | Every Write line + exit signal emit both carry full path. |
| C-06 | Forward-only stage order with gate | 10 | PASS | SETUP gate: "STAGE 1 cannot begin until SCOUT READY fires." SCOUT READY requires found file. No bypass. |
| C-07 | Scout anchor in hypothesis artifact | 10 | PASS | Stage 1: "Include `scout_source` in the frontmatter pointing to the scout artifact path." In-artifact. |
| C-08 | Evidence gaps flagged at discovery | 10 | PASS | Stages 2-3: "Flag thin or absent evidence at the point of discovery -- not deferred: THIN: [area] -- [gap]." |
| C-09 | Thin-evidence propagates to synthesis | 5 | PASS | Stage 5: "For each THIN-flagged claim: name the source stage and adjusted confidence." |
| C-10 | Hypothesis structurally blocked until scout | 5 | PASS | "SCOUT READY cannot fire without a found file" + "STAGE 1 cannot begin until SCOUT READY fires." Two-step structural block. |

**V-02: 100/100 -- all essential PASS**

---

## V-03 -- Role Sequence

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All five sub-skills in sequence | 12 | PASS | SCOUT-LOADER -> Stages 1-4 [ANALYST] -> Stage 5 [SYNTHESIZER]. All five stages, ordered by role. |
| C-02 | Scout artifact loaded before hypothesis | 12 | PASS | SCOUT-LOADER runs first, Globs, halts if absent, emits scout_source. Stage 1 ENTRY checks receipt. |
| C-03 | Progressive artifact writes | 12 | PASS | 5 writes, one per stage, all with full paths. |
| C-04 | Synthesis signals readiness for topic-story | 12 | PASS | Stage 5 [SYNTHESIZER]: "Close: Evidence brief for {topic} is ready for /topic-story." |
| C-05 | Artifact paths on every write instruction | 12 | PASS | All 5 Write instructions carry full paths. |
| C-06 | Forward-only stage order with gate | 10 | PASS | Stage 1 ENTRY: "scout_source must be confirmed received from SCOUT-LOADER. If not confirmed: halt." Role boundary is equivalent checkpoint. |
| C-07 | Scout anchor in hypothesis artifact | 10 | PASS | Stage 1: "Frontmatter must include: scout_source: simulations/scout/{topic}-scout-{date}.md." In-artifact. |
| C-08 | Evidence gaps flagged at discovery | 10 | PASS | Stages 2-3: "Flag thin findings at point of discovery: THIN: [area] -- [gap]." |
| C-09 | Thin-evidence propagates to synthesis | 5 | PASS | Stage 5 [SYNTHESIZER]: "For each THIN-flagged claim: Name source stage / weakened claim / adjusted confidence." All three sub-requirements met. |
| C-10 | Hypothesis structurally blocked until scout | 5 | PASS | SCOUT-LOADER: "Halt. ANALYST does not receive control." Stage 1 ENTRY: "If not confirmed: halt." Two-layer block -- no fallback in either layer. |

**V-03: 100/100 -- all essential PASS**

---

## V-04 -- Two-Write Synthesis

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All five sub-skills in sequence | 12 | PASS | Stages 1-5 in order. Stage 5 contains two writes (synthesis stage), not a sixth stage. |
| C-02 | Scout artifact loaded before hypothesis | 12 | PASS | SETUP: "If absent: halt... Do not proceed." Scout read before Stage 1. |
| C-03 | Progressive artifact writes | 12 | PASS | Stages 1-4: one write each. Stage 5: two writes still within the synthesis stage. C-03 requires at least one per stage. |
| C-04 | Synthesis signals readiness for topic-story | 12 | PASS | Write B: "Close: Evidence brief for {topic} is ready for /topic-story." Isolated from confidence notes. |
| C-05 | Artifact paths on every write instruction | 12 | PASS | Write A and Write B both carry full paths. Stages 1-4 writes carry full paths. |
| C-06 | Forward-only stage order with gate | 10 | PASS | SETUP: "If absent: halt... Do not proceed." Equivalent checkpoint before Stage 1. |
| C-07 | Scout anchor in hypothesis artifact | 10 | PASS | Stage 1: "Frontmatter: scout_source: simulations/scout/{topic}-scout-{date}.md." In-artifact. |
| C-08 | Evidence gaps flagged at discovery | 10 | PASS | Stages 2-3: "Flag thin findings at point of discovery: THIN: [area] -- [gap]." |
| C-09 | Thin-evidence propagates to synthesis | 5 | PASS | Write A: "If thin: name source stage and adjusted confidence." Per-claim structure by artifact definition. |
| C-10 | Hypothesis structurally blocked until scout | 5 | PASS | SETUP: "If absent: halt... Do not proceed." No fallback. Matches rubric example 2: "abort here if scout-record is absent instruction with no fallback." |

**V-04: 100/100 -- all essential PASS**

---

## V-05 -- Minimalism + Exit-Signal + Two-Write

| ID | Criterion | Pts | Verdict | Evidence |
|----|-----------|-----|---------|----------|
| C-01 | All five sub-skills in sequence | 12 | PASS | SETUP + Stages 1-5 with exit signal chain enforcing order. |
| C-02 | Scout artifact loaded before hypothesis | 12 | PASS | SETUP: "SCOUT READY cannot fire without a found file." Stage 1 ENTRY: "SCOUT READY must have fired." |
| C-03 | Progressive artifact writes | 12 | PASS | Stages 1-4: one write each. Stage 5: Write A + Write B. All carry full paths. |
| C-04 | Synthesis signals readiness for topic-story | 12 | PASS | Write B: "Close: Evidence brief for {topic} is ready for /topic-story." Separated from Write A. |
| C-05 | Artifact paths on every write instruction | 12 | PASS | All 6 write instructions (Stages 1-4 + Write A + Write B) carry full paths. |
| C-06 | Forward-only stage order with gate | 10 | PASS | "STAGE 1 cannot begin until SCOUT READY fires." SCOUT READY requires found file. Structural gate. |
| C-07 | Scout anchor in hypothesis artifact | 10 | PASS | Stage 1: "Frontmatter: scout_source: simulations/scout/{topic}-scout-{date}.md." In-artifact. |
| C-08 | Evidence gaps flagged at discovery | 10 | PASS | Stages 2-3: "Flag thin findings at point of discovery: THIN: [area] -- [gap]." |
| C-09 | Thin-evidence propagates to synthesis | 5 | PASS | Write A: "If thin: name source stage and adjusted confidence." By construction. |
| C-10 | Hypothesis structurally blocked until scout | 5 | PASS | "SCOUT READY cannot fire without a found file" + "STAGE 1 cannot begin until SCOUT READY fires." Two-step structural block. |

**V-05: 100/100 -- all essential PASS**

---

## Final Rankings

| Rank | Variation | Score | C-10 |
|------|-----------|-------|------|
| 1 (tie) | V-02 Exit-signal | 100 | PASS -- two-signal chain |
| 1 (tie) | V-03 Role sequence | 100 | PASS -- two-layer role block |
| 1 (tie) | V-04 Two-write synthesis | 100 | PASS -- abort with no fallback |
| 1 (tie) | V-05 Combined | 100 | PASS -- two-signal chain |
| 5 | V-01 Minimalism | 97.5 | PARTIAL -- prose block, no signal/field |

## Excellence Signals

**Signal 1 — Exit-signal chaining is a portable structural block**
"SCOUT READY cannot fire without a found file" + "STAGE N cannot begin until SCOUT READY fires" satisfies C-10 without GATE block headers, gate_cleared fields, or role mechanisms. This two-signal pattern is compact and consistent with V-01's minimalist style — it could be added to V-01 in Round 3 to close the 2.5-point gap.

**Signal 2 — Two-write synthesis makes C-09 structural by construction**
Write A (claim-evidence map) requires per-claim enumeration with source stage and confidence adjustment. C-09 cannot be partially satisfied — Write A either has the per-claim structure or it is not the artifact defined. This is different from a Stage 5 reminder instruction, which can be partially followed. Round 3 should carry two-write synthesis as baseline.

**Signal 3 — Role sequence satisfies C-02/C-07 by architecture**
SCOUT-LOADER's job is scout loading. If the role runs, it loads; if the file is absent, it halts. The hypothesis stage's ENTRY then independently confirms receipt. Two independent enforcement points for the same property, zero duplicated instructions. Role-sequence framing is a cleaner mechanism for C-02/C-07 than redundant per-stage reminders.

## Round 3 Recommendation

Rubric v14 ceiling reached. Four of five variations score 100 in Round 2. Next actions:
1. Promote V-05 (Combined) as primary golden candidate — carries all three new patterns
2. Fix V-01's C-10 PARTIAL by adding two-signal chain to SETUP (one-line change)
3. Consider whether v14 needs new aspirational criteria before Round 3 to preserve discrimination signal
