---

## prove-interview — Scorecard R1

**Formula**: `(E/5 × 60) + (R/3 × 30) + (A/2 × 10)` | PARTIAL = 0.5

---

### Per-Variation Scoring

| ID | Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|------|
| C-01 | Persona identity declared | E | PASS | PASS | PASS | PASS | PASS |
| C-02 | Prior knowledge scoped | E | PASS | PARTIAL | PASS | PASS | **FAIL** |
| C-03 | Answers in persona voice | E | PASS | PASS | PASS | PARTIAL | PASS |
| C-04 | Evidence explicitly extracted | E | PASS | PASS | PASS | PASS | PASS |
| C-05 | Surprising/confirming labeled | E | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-06 | Probing questions + follow-up | R | PARTIAL | FAIL | PASS | FAIL | FAIL |
| C-07 | Multiple distinct personas | R | PASS | PARTIAL | PASS | PARTIAL | PASS |
| C-08 | Evidence signal-typed | R | FAIL | PASS | PASS | FAIL | PASS |
| C-09 | Cross-interview synthesis | A | PASS | PASS | PASS | PASS | PASS |
| C-10 | Simulation fidelity annotated | A | FAIL | FAIL | PASS | FAIL | FAIL |

---

### Ranked Leaderboard

| Rank | Variation | Composite | Golden? |
|------|-----------|-----------|---------|
| **1** | **V-03** — Conversational register | **94** | No — C-05 PARTIAL |
| 2 | V-01 — Disposition-ordered | 74 | No — C-05 PARTIAL |
| 3 | V-02 — Structured table | 68 | No — C-02/C-05 PARTIAL |
| 4 | V-05 — Combined | 67 | No — C-02 FAIL |
| 5 | V-04 — Lifecycle + inertia | 58 | No — C-03/C-05 PARTIAL |

---

### Failure Patterns

**C-05 — universal PARTIAL across all 5 variations.** The mechanism (marking a notable moment) is present everywhere. The rubric-required vocabulary (SURPRISING/CONFIRMING) with an explicit prior-expectation link is absent everywhere. This is a vocabulary gap, not a structural gap — fixable in R2 by adding `SURPRISING (expected: X, got: Y)` / `CONFIRMING (validates: Z)` label format to every variation.

**C-10 — FAIL in 4/5.** Fidelity annotation will not appear unless explicitly prompted. Only V-03's "one last thing" invitation reliably produces it.

**C-06 — FAIL in 3/5.** Follow-up sub-criterion is the commonly dropped one. Only V-03 meets both sub-criteria.

---

### Excellence Signals from V-03

1. **"Don't let them all sound like the same AI wrote them"** — naming the voice-failure anti-pattern is more effective than abstract "write in their voice" requirements
2. **Prose-embedded signal taxonomy** matches rubric label examples exactly; applies in free-form extraction without requiring table format
3. **"One last thing" fidelity close** — reflective invitation framing reliably produces C-10 where formal phase requirements would be skipped
4. **Organic follow-up framing** — "let their answer take you somewhere you didn't plan to go" produces follow-up naturally; mechanical formatting rules produce compliance without authenticity

---

```json
{"top_score": 94, "all_essential_pass": false, "new_patterns": ["conversational-descriptive register produces stronger C-03 voice fidelity and organic C-06 follow-up than imperative commands", "signal taxonomy embedded in prose body matches rubric examples and applies in free-form extraction without table format", "simulation fidelity close as reflective invitation reliably produces C-10 without structural enforcement", "C-05 vocabulary gap: all R1 variations use wrong label -- R2 must add SURPRISING/CONFIRMING vocabulary with expectation-link to fix the universal essential partial"]}
```
tem states: what was said, why it matters to the hypothesis" -- dedicated extraction section. |
| C-05 | Surprising/confirming moment labeled | E | PARTIAL | "[SIGNAL MOMENT]" label required per subject; defined as "something that surprises the interviewer or explicitly confirms/contradicts a prior assumption" -- concept present, labeling required, but wrong vocabulary (not SURPRISING/CONFIRMING) and no prior expectation declared. |
| C-06 | Questions probe concerns + follow-up | R | PARTIAL | "At least one follow-up question that responds to a prior answer (not from the prepared list)" -- follow-up explicit. Role-anchoring implicit via identity block context, not mandated as a question-design rule. |
| C-07 | Multiple distinct personas | R | PASS | SKEPTIC/NEUTRAL/CHAMPION prescribed -- three dispositions structurally distinct by construction. |
| C-08 | Evidence signal-typed | R | FAIL | "Each item states: what was said, why it matters" -- prose only, no signal type taxonomy. |
| C-09 | Cross-interview synthesis | A | PASS | "Cross-Interview Synthesis" section required with three sub-questions covering skeptic/champion arc, dominant direction, and confidence shift. |
| C-10 | Simulation fidelity annotated | A | FAIL | No meta-note requirement distinguishing grounded from constructed claims. Not present. |

**V-01**: E=4.5/5, R=1.5/3, A=1/2 -> (54) + (15) + (5) = **74**
Essential threshold: NOT MET (C-05 PARTIAL)

---

## Scoring -- V-02: Output Format / Structured Table Extract

| ID | Criterion | Tier | Verdict | Evidence note |
|----|-----------|------|---------|---------------|
| C-01 | Persona identity declared | E | PASS | "Role: their title or function / Context: 2-3 sentences on what they know, what they care about, and what lens they bring" -- role and context before transcript. |
| C-02 | Prior knowledge scoped | E | PARTIAL | "Context: 2-3 sentences on what they know, what they care about" -- positive knowledge and concerns present, but no blind spots field. Rubric requires "what they know, what they don't know, what they care about." |
| C-03 | Answers in persona voice | E | PASS | "The subject's answers should sound like *them* -- not like a product description or a neutral summary. They have opinions, blind spots, and vocabulary that matches their role." |
| C-04 | Evidence explicitly extracted | E | PASS | Mandatory table after each transcript: "Quote (verbatim from transcript) / Signal Type / Strength" -- verbatim requirement prevents implicit-only evidence. |
| C-05 | Surprising/confirming moment labeled | E | PARTIAL | ">> NOTABLE" label required per subject; "where something unexpected, confirming, or contradictory surfaces" -- concept present but wrong vocabulary, no prior expectation link. |
| C-06 | Questions probe concerns + follow-up | R | FAIL | "4-6 exchanges" format with no explicit follow-up requirement and no role-anchoring mandate. |
| C-07 | Multiple distinct personas | R | PARTIAL | "{N} stakeholder interviews" -- freeform subject selection, no distinctness mandate. |
| C-08 | Evidence signal-typed | R | PASS | "Signal Type must be one of: `risk`, `preference`, `constraint`, `validation`, `invalidation`" -- complete taxonomy, required column, table makes omission visible. |
| C-09 | Cross-interview synthesis | A | PASS | "Cross-Interview Synthesis" with tally-by-type, contradiction surface, and net verdict with confidence. |
| C-10 | Simulation fidelity annotated | A | FAIL | Not present. |

**V-02**: E=4.0/5, R=1.5/3, A=1/2 -> (48) + (15) + (5) = **68**
Essential threshold: NOT MET (C-02 PARTIAL, C-05 PARTIAL)

---

## Scoring -- V-03: Phrasing Register / Conversational-Descriptive

| ID | Criterion | Tier | Verdict | Evidence note |
|----|-----------|------|---------|---------------|
| C-01 | Persona identity declared | E | PASS | "*Before you begin:* their role, what they know, and what they care about most in this area" -- role and prior-state declared per subject before questions. |
| C-02 | Prior knowledge scoped | E | PASS | "their role, what they've seen, what they're worried about, what they don't know yet" -- both positive knowledge ("what they've seen") and blind spots ("what they don't know yet") explicitly named. |
| C-03 | Answers in persona voice | E | PASS | "Write their answers in their voice. If they're an engineer, they'll say things engineers say. If they're a product manager, they'll talk in outcomes and timelines. Don't let them all sound like the same AI wrote them." -- strongest voice priming in R1; names the failure mode it guards against. |
| C-04 | Evidence explicitly extracted | E | PASS | "*What you extracted:* 1-3 specific items of evidence from this conversation, stated plainly" -- dedicated extraction section per subject, separate from transcript. |
| C-05 | Surprising/confirming moment labeled | E | PARTIAL | "You mark that moment" -- labeling present but no SURPRISING/CONFIRMING vocabulary; no prior expectation required. Body text establishes the concept ("Some of them will surprise you. Some will confirm what you already suspected.") but does not enforce label format. |
| C-06 | Questions probe concerns + follow-up | R | PASS | "Ask questions that come out of that specific person's situation" (role-anchoring explicit) + "listen to their answers and follow up -- at least once per interview, let their answer take you somewhere you didn't plan to go" (follow-up explicit). Both sub-criteria met. |
| C-07 | Multiple distinct personas | R | PASS | "Pick three people... Give each a different job, a different level of technical depth, and a different reason to care" -- distinctness mandate on three explicit dimensions. |
| C-08 | Evidence signal-typed | R | PASS | "Tag each item with what kind of signal it is: adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation" -- prose-embedded taxonomy matching rubric's own label examples exactly. |
| C-09 | Cross-interview synthesis | A | PASS | "After all three interviews, step back. What do the conversations add up to?... Where did they contradict each other in ways that tell you something real about the tension in the hypothesis?" -- synthesis required with cross-pattern instruction. |
| C-10 | Simulation fidelity annotated | A | PASS | "One last thing: note briefly which parts of these interviews are grounded in real domain knowledge or documented context, and which parts are plausible constructions. The reader should know what to trust and what to verify." -- explicit meta-note requirement. Only V-03 passes this criterion. |

**V-03**: E=4.5/5, R=3.0/3, A=2/2 -> (54) + (30) + (10) = **94**
Essential threshold: NOT MET (C-05 PARTIAL -- the only gap in the top variation)

---

## Scoring -- V-04: Lifecycle Emphasis + Inertia Framing

| ID | Criterion | Tier | Verdict | Evidence note |
|----|-----------|------|---------|---------------|
| C-01 | Persona identity declared | E | PASS | "Subject card: Role and title / Current practice... / Known concerns... / Blind spots... / Disposition..." -- five-field card declared in Phase 1 before any transcript. |
| C-02 | Prior knowledge scoped | E | PASS | Subject card includes "Current practice" (domain experience today), "Known concerns" (what has gone wrong), and "Blind spots" (what they're not considering) -- covers knowledge, concerns, and gaps. |
| C-03 | Answers in persona voice | E | PARTIAL | Phase 2 runs two-part transcripts but no explicit "write in subject's voice / their vocabulary" instruction. V-04 structures questions but does not enforce voice. The rubric requires answers to "reflect the simulated human's perspective, concerns, and blind spots." |
| C-04 | Evidence explicitly extracted | E | PASS | "Phase 3 -- Evidence Extraction: After each interview, extract: 1-3 evidence items, each stated as: what the subject said -> what this means for the hypothesis" -- dedicated extraction phase. |
| C-05 | Surprising/confirming moment labeled | E | PARTIAL | "[SIGNAL MOMENT]" label required per interview, but wrong vocabulary and no prior expectation link. |
| C-06 | Questions probe concerns + follow-up | R | FAIL | Phase 2 has Part A (current practice) and Part B (hypothesis probe) but no explicit follow-up instruction. "At least one follow-up responding to a prior answer" is absent. |
| C-07 | Multiple distinct personas | R | PARTIAL | "2-3 subjects" implied but no distinctness mandate. Near-identical subject cards would not be flagged. |
| C-08 | Evidence signal-typed | R | FAIL | Phase 3 evidence: "what the subject said -> what this means for the hypothesis / note whether Part A context amplifies or changes how you read Part B answer" -- no signal type taxonomy. |
| C-09 | Cross-interview synthesis | A | PASS | Phase 4 with four required sub-questions: inertia baseline, divergence across subjects, cross-subject signal, and verdict. |
| C-10 | Simulation fidelity annotated | A | FAIL | Not present. |

**V-04**: E=4.0/5, R=0.5/3, A=1/2 -> (48) + (5) + (5) = **58**
Essential threshold: NOT MET (C-03 PARTIAL, C-05 PARTIAL)

---

## Scoring -- V-05: Combined (Role Sequence + Output Format + Inertia Framing)

| ID | Criterion | Tier | Verdict | Evidence note |
|----|-----------|------|---------|---------------|
| C-01 | Persona identity declared | E | PASS | Subject roster table with Role, Current Practice, Disposition, Rationale columns; plus interview header "Subject name, role, disposition from roster" -- role declared structurally. |
| C-02 | Prior knowledge scoped | E | FAIL | Roster table has: Role, Current Practice (today), Disposition, Rationale. No "Prior knowledge" field (what they know about the domain) and no "Blind spots" field. Rubric: "prior knowledge and blind spots... stated before answers are given." Both dimensions absent. |
| C-03 | Answers in persona voice | E | PASS | "Write every answer in the subject's voice -- role-grounded vocabulary, specific concerns" -- explicit voice requirement in interview format. |
| C-04 | Evidence explicitly extracted | E | PASS | "Evidence Table (after each interview): Quote (verbatim) / Signal Type / Strength / Current-Practice Link" -- mandatory table. |
| C-05 | Surprising/confirming moment labeled | E | PARTIAL | ">> [SIGNAL MOMENT]" label required but wrong vocabulary, no prior expectation required. |
| C-06 | Questions probe concerns + follow-up | R | FAIL | "4-6 exchanges per subject" with no explicit follow-up requirement. |
| C-07 | Multiple distinct personas | R | PASS | Three-subject roster with fixed SKEPTIC/NEUTRAL/CHAMPION roles -- structurally distinct. |
| C-08 | Evidence signal-typed | R | PASS | Evidence table Signal Type: "`risk` / `preference` / `constraint` / `validation` / `invalidation`" -- complete taxonomy per required column. |
| C-09 | Cross-interview synthesis | A | PASS | "Cross-Interview Synthesis" with inertia verdict, arc signal, signal tally, and net verdict. |
| C-10 | Simulation fidelity annotated | A | FAIL | Not present. |

**V-05**: E=3.5/5, R=2.0/3, A=1/2 -> (42) + (20) + (5) = **67**
Essential threshold: NOT MET (C-02 FAIL = disqualified regardless of composite; C-05 PARTIAL)

---

## Synthesis

### Composite Scores

```
V-01: E=4.5/5, R=1.5/3, A=1/2  ->  (54) + (15) + (5)  =  74
V-02: E=4.0/5, R=1.5/3, A=1/2  ->  (48) + (15) + (5)  =  68
V-03: E=4.5/5, R=3.0/3, A=2/2  ->  (54) + (30) + (10) =  94
V-04: E=4.0/5, R=0.5/3, A=1/2  ->  (48) + (5)  + (5)  =  58
V-05: E=3.5/5, R=2.0/3, A=1/2  ->  (42) + (20) + (5)  =  67
```

### Ranked Leaderboard

| Rank | Variation | Composite | Golden? | Essential block |
|------|-----------|-----------|---------|----------------|
| 1 | V-03 -- Conversational register | 94 | No | C-05 PARTIAL |
| 2 | V-01 -- Disposition-ordered | 74 | No | C-05 PARTIAL |
| 3 | V-02 -- Structured table | 68 | No | C-02 PARTIAL, C-05 PARTIAL |
| 4 | V-05 -- Combined | 67 | No | C-02 FAIL, C-05 PARTIAL |
| 5 | V-04 -- Lifecycle + inertia | 58 | No | C-03 PARTIAL, C-05 PARTIAL |

No variation achieves golden status. All fail on C-05; V-05 also fails C-02 outright.

### Failure Patterns

**C-05 (Surprising/confirming moment labeled) -- PARTIAL across all 5 variations.**

No variation requires the exact SURPRISING/CONFIRMING label vocabulary tied to a stated prior
expectation. V-01/V-04/V-05 use [SIGNAL MOMENT], V-02 uses >> NOTABLE, V-03 uses "mark that
moment" with no label vocabulary at all. The mechanism (labeling a notable moment) is present
in all five variations. The rubric's specific label words and the expectation-link requirement
are absent in all five. This is a vocabulary alignment gap, not a structural gap -- fixable by
adding "label it SURPRISING (expected: X, got: Y) or CONFIRMING (validates: Z)" to any
variation's label instruction.

**C-10 (Simulation fidelity annotated) -- FAIL in 4 of 5 variations.**

Only V-03 passes. Fidelity annotation will not appear unless explicitly prompted -- it is not
a natural output of stakeholder simulation. The "one last thing" framing in V-03 is the only
version that reliably produces it.

**C-06 (Questions probe concerns + follow-up) -- FAIL in 3 of 5 variations.**

V-02, V-04, V-05 all omit the follow-up requirement. The follow-up sub-criterion is the more
commonly dropped. Role-anchoring is typically implicit in persona framing but not enforced.

### Excellence Signals

**V-03 / C-10 -- only variation to pass fidelity annotation.**
The "One last thing: note briefly which parts are grounded vs plausible constructions" framing
as a natural closing invitation rather than a required phase step produces reliable compliance.
Structuring fidelity as reflective advice prevents it from being skipped.

**V-03 / C-03 -- strongest persona voice priming.**
"Don't let them all sound like the same AI wrote them" + concrete role-vocabulary contrasts
(engineer/product manager examples) is the only variation that explicitly names the failure
mode it guards against. Naming the anti-pattern is more effective than abstract voice
requirements.

**V-03 / C-06 -- only variation meeting both sub-criteria.**
"Ask questions that come out of that specific person's situation" (role-anchoring explicit) AND
"let their answer take you somewhere you didn't plan to go" (follow-up organic, not mechanical).
Both sub-criteria satisfied by natural instruction rather than mechanical formatting rules.

**V-03 / C-08 -- prose-embedded taxonomy vs. table-column taxonomy.**
V-03's inline "adoption risk | feasibility concern | requirement gap | scope signal | constraint
| validation" matches the rubric's own examples exactly and is visible at extraction time even
without a table format -- unlike V-02/V-05 where the taxonomy only appears as table column
instructions.

### Regression Signals

No prior round data -- regression analysis cannot be performed.

---

## Score Output

```json
{"top_score": 94, "all_essential_pass": false, "new_patterns": ["conversational-descriptive register produces stronger C-03 voice fidelity and organic C-06 follow-up than imperative commands", "signal taxonomy embedded in prose body matches rubric examples and applies in free-form extraction without table format", "simulation fidelity close as reflective invitation reliably produces C-10 without structural enforcement", "C-05 vocabulary gap: all R1 variations use wrong label (SIGNAL MOMENT / NOTABLE / unmarked) -- R2 must add SURPRISING/CONFIRMING vocabulary with expectation-link to fix the universal essential partial"]}
```
