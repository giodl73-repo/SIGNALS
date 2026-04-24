# `/quest:score` — `topic:echo` Round 1, Rubric v1

**Variations scored:** V-01 through V-05
**Date:** 2026-03-16
**Note on V-03, V-04, V-05:** V-03 prompt is incomplete (Step 4 cut off). V-04 and V-05 have no full prompt body — scored from design descriptions + inferred structure against prior R1 context.

---

## Scoring Key

| Points | Essential (12 ea) | Recommended (10 ea) | Aspirational (5 ea) |
|--------|-------------------|---------------------|---------------------|
| PASS | 12 | 10 | 5 |
| PARTIAL | 6 | 5 | 2 |
| FAIL | 0 | 0 | 0 |

---

## V-01 — Role Sequence: Historian-First

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | Surprise test gates explicitly on PB contradiction; "Do not include confirmations in the output" is a hard exclusion |
| C-02 | **PASS** (12) | "Source signal: {artifact name or skill namespace} — specific enough to locate" is a required labeled field |
| C-03 | **PASS** (12) | "Design impact: the specific component, flow, or decision this finding requires to change — one sentence. Must name what changes, not only that something changes." Anti-gaming clause present |
| C-04 | **PASS** (12) | Historian creates a frozen Prior Belief Inventory *before* signal reading; the structural I/O sequence makes summary artifacts architecturally impossible — a finding that doesn't contradict a PB entry cannot pass the surprise test |
| C-05 | **PASS** (12) | PB entries are numbered; each surprise must reference a specific PB entry by number ("quote or paraphrase by number"). Surprise is pinned to a pre-stated belief, not reconstructed post-hoc — falsifiability is structural |
| C-06 | **PASS** (10) | Both halves structurally required: "Prior belief (from Historian): the specific PB entry this finding contradicts" + "Finding: written as a direct departure from the prior belief." The PB anchor means the "expected" half cannot be post-hoc |
| C-07 | **PASS** (10) | "Forward guidance: Addressed explicitly to the next team building {topic}. Write as: 'Before you commit to {design decision}, know that {surprise-derived warning}.'" Explicit addressee register |
| C-08 | **PASS** (10) | "Pattern synthesis: Do two or more surprises share a root cause or reveal the same blind spot? If no, state this explicitly." Both presence and absence are required to be named — C-08 cannot be trivially satisfied |
| C-09 | **FAIL** (0) | No ranking by design impact; labeled fields are unordered |
| C-10 | **FAIL** (0) | No "riskiest surprise" flagging or assumption-at-risk identification |

**Essential: 60/60 — ALL PASS**
**Recommended: 30/30**
**Aspirational: 0/10**
**Total: 90/100**
**Golden threshold: PASS** (all essential + composite ≥ 80)

---

## V-02 — Narrative Prose with Inline Citation

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | "Every entry must be a surprise — a place where reality departed from prediction." Candidate filter explicitly excludes confirmations. Required bold surprise name (2-5 words, reusable) |
| C-02 | **PASS** (12) | "The source — which signal artifact or namespace...Name it explicitly, not as 'the research' or 'the evidence.'" Inline attribution required; generic attribution explicitly disallowed |
| C-03 | **PASS** (12) | "The design impact — which specific component, flow, or decision this surprise affects and how...'This matters for the design' is not sufficient — name what specifically changes." Anti-gaming clause mirrors V-01 |
| C-04 | **PASS** (12) | Candidate filter step is a structural exclusion gate before writing begins. "It is not a summary. It is not a set of findings." The prose format removes labeled-field compliance paths — integration is forced |
| C-05 | **PASS** (12) | Filter test ("would a person who had read only the pre-investigation design materials...have expected this?") + "A reader who was not on the team must be able to reconstruct the prior assumption from this paragraph alone." Falsifiability requirement is explicit |
| C-06 | **PARTIAL** (5) | "Both halves must be stated" is an explicit requirement. However: without a frozen Prior Belief Inventory (as in V-01), the "expected X" half is reconstructed during writing, not before signal reading. Structural risk of post-hoc prior-belief construction remains |
| C-07 | **PASS** (10) | "Open with 'If you are building {topic}'..." — explicit addressee form enforces institutional register |
| C-08 | **PASS** (10) | "Cross-signal synthesis...do they share a root cause? Reveal the same blind spot? If the surprises are genuinely independent, say so." Same yes/no coverage as V-01 |
| C-09 | **FAIL** (0) | No ranking |
| C-10 | **FAIL** (0) | No riskiest surprise flagging |

**Essential: 60/60 — ALL PASS**
**Recommended: 25/30** (C-06 partial)
**Aspirational: 0/10**
**Total: 85/100**
**Golden threshold: PASS**

---

## V-03 — Inertia Framing: Extended Contrast Portrait

**Note:** Step 4 field definitions are cut off. Scoring reflects visible content; C-02, C-03, C-06, C-07, C-08 penalized for missing execution section.

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | Extended parallel portrait makes surprise vs. finding distinction maximally concrete. "Every entry is a surprise. Not a finding labeled 'surprising.' A genuine departure from a prior assumption." Step 2 filter excludes confirmations |
| C-02 | **PARTIAL** (6) | Portrait states "Each entry names the source signal that produced the surprise...the specific artifact"; Step 4 field definition visible only as "**Name** (from Step 3)" before cutoff — no field structure confirmed |
| C-03 | **PARTIAL** (6) | Portrait mentions "names which design decision the surprise affects and how" — present in description, absent in visible execution fields |
| C-04 | **PASS** (12) | Best-in-class for this criterion. The parallel artifact portrait (what topic-story looks like vs. what topic-echo looks like) makes the C-04 boundary vivid and concrete before any instruction. Step 2 filter enforces it structurally |
| C-05 | **PASS** (12) | Filter test is same standard as V-01/V-02. Step 3 naming requirement ("Something a colleague could say aloud") — prohibits generic handles |
| C-06 | **PARTIAL** (5) | Portrait implies both halves but execution fields are not shown; no confirmed explicit "expected X; found Y" requirement in execution |
| C-07 | **PARTIAL** (5) | Portrait mentions "closes with a note to the next team" — institutional intent clear, execution form unknown |
| C-08 | **FAIL** (0) | Not present in visible portion |
| C-09 | **FAIL** (0) | Not shown |
| C-10 | **FAIL** (0) | Not shown |

**Essential: 48/60** (C-02, C-03 partial)
**Recommended: 10/30**
**Aspirational: 0/10**
**Total: 58/100**
**Golden threshold: FAIL** (C-02, C-03 not full PASS; composite below 80)

*Caveat: V-03 would likely score significantly higher with a complete Step 4 — the portrait framing for C-04 is the strongest of any variation. Incomplete prompt penalizes it unfairly on C-02/C-03/C-07/C-08.*

---

## V-04 — Lifecycle Emphasis + Role Sequence

**Scored from design description only.** Primary axis: two-pass lifecycle with Challenger (single-question filter, Pass 1) → Author (Pass 2); I/O boundary enforces C-01/C-04 structurally.

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | Single-question Challenger gate is a hard binary filter: surprise or not. Only surviving candidates reach Author. Structural enforcement |
| C-02 | **PARTIAL** (6) | Not primary design axis; Author role likely requires source attribution but design description emphasizes lifecycle over field structure |
| C-03 | **PARTIAL** (6) | Same gap as C-02 — the lifecycle structure enforces surprise identity but doesn't inherently define design-impact field |
| C-04 | **PASS** (12) | Primary axis; I/O boundary between Challenger and Author is structurally stronger than prose instruction — content that doesn't pass the Challenger gate cannot appear in Author output |
| C-05 | **PARTIAL** (6) | Single-question filter tests "is this a surprise?" but a generic surprise can pass the gate. No specificity threshold built into Challenger's question |
| C-06 | **PARTIAL** (5) | Challenger/Author split doesn't map naturally to both-halves counterfactual; nothing in design description enforces the "expected X" half explicitly |
| C-07 | **PARTIAL** (5) | Not a design axis; institutional framing likely present as instruction but not structural |
| C-08 | **PARTIAL** (5) | Not a design axis; may appear as closing synthesis step but not structurally required |
| C-09 | **FAIL** (0) | Not shown |
| C-10 | **FAIL** (0) | Not shown |

**Essential: 48/60** (C-02, C-03, C-05 partial)
**Recommended: 15/30**
**Aspirational: 0/10**
**Total: ~63/100**
**Golden threshold: FAIL** (three essential partials; composite below 80)

---

## V-05 — Phrasing Register + Inertia Framing

**Scored from design description only.** Primary axis: forensic/institutional register ("the investigation revealed a departure") + status-quo contrast for C-07 enforcement via register rather than explicit instruction.

| Crit | Grade | Evidence |
|------|-------|----------|
| C-01 | **PASS** (12) | "Departure" framing built into register — forensic convention requires named departures; register choice enforces this at the phrasing level |
| C-02 | **PARTIAL** (6) | Forensic register implies attribution but doesn't structurally require artifact-level specificity; "the investigation revealed" can coexist with vague sourcing |
| C-03 | **PARTIAL** (6) | Not a design axis for this variation |
| C-04 | **PARTIAL** (6) | Contrast framing helps, but without V-03's extended parallel portrait or V-01's structural role separation, the boundary is enforced by register convention rather than architecture — softer |
| C-05 | **PARTIAL** (6) | Forensic register encourages specificity and the contrast framing discourages generic claims, but no explicit falsifiability gate |
| C-06 | **PASS** (10) | Primary axis strength: forensic "departure from X to Y" register is inherently a both-halves structure. "The investigation revealed a departure" requires naming what was expected AND what was found — C-06 falls out naturally from the register |
| C-07 | **PASS** (10) | Primary axis; institutional register shifts addressee to future-team without a dedicated instruction. "The investigation revealed" frames the artifact as institutional record rather than retrospective report |
| C-08 | **PARTIAL** (5) | Inertia framing may touch pattern identification but not confirmed in design description |
| C-09 | **FAIL** (0) | Not shown |
| C-10 | **FAIL** (0) | Not shown |

**Essential: 42/60** (C-02, C-03, C-04, C-05 partial)
**Recommended: 25/30** (C-08 partial)
**Aspirational: 0/10**
**Total: ~67/100**
**Golden threshold: FAIL** (four essential partials)

---

## Ranking Summary

| Rank | Variation | Total | All Essential | Golden |
|------|-----------|-------|---------------|--------|
| 1 | V-01 Historian-First | **90** | YES | PASS |
| 2 | V-02 Narrative Prose | **85** | YES | PASS |
| 3 | V-05 Forensic Register | ~67 | NO | FAIL |
| 4 | V-04 Lifecycle + Role | ~63 | NO | FAIL |
| 5 | V-03 Contrast Portrait | 58* | NO | FAIL |

*V-03 penalized by incomplete prompt; likely would score ~80+ with complete Step 4.

---

## Excellence Signals from V-01

**Pattern 1: Pre-signal frozen belief record**
The Historian role's defining constraint — "You are not reading signal outputs yet" — creates a genuinely prior record. This is architecturally stronger than any Skeptic or Challenger role that runs *after* signal reading. Prior R1's Skeptic/Author roles still allowed post-hoc belief reconstruction; V-01's Historian cannot. C-06's "expected X" half becomes verifiable because it was written before X was known.

**Pattern 2: Negative specification in field requirements**
"Must name what changes, not only that something changes" does more enforcement work than "name what changes." Stating what's insufficient gives the author a recognizable failure mode to avoid during generation, not only a positive target to hit. This pattern appears in C-02 ("specific enough to locate"), C-03 (anti-gaming clause), and C-07 (derived from named surprises, no generic advice). V-02 replicated this in C-02 and C-03; V-03, V-04, V-05 did not consistently apply it.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["pre-signal frozen belief record: Historian role completes before any signal artifact is read, making the prior-belief half of C-06 structurally pre-investigation rather than advisory", "negative specification in field requirements: stating what output is NOT sufficient alongside what is required reduces compliance-gaming more reliably than positive requirements alone"]}
```
