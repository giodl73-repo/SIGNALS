---
skill: quest-score
skill_target: scout-competitors
topic: plugin
date: 2026-03-14
round: 1
rubric: scout-competitors-rubric-2026-03-14.md
rubric_version: 1
---

# Scorecard: scout-competitors Round 1

Scoring each variation against the v1 rubric by simulating the output each
variation would produce for the test invocation.

---

## Per-Variation Scoring

### V-01: Baseline

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01: Inertia row | PASS | Setup says "Always include none/status quo" |
| C-02: Whitespace | PASS | Findings explicitly highlight gaps |
| C-03: Table stakes | PASS | Findings section flags table stakes |
| C-04: Threat level | PASS | All 4 roles assess per competitor |
| C-05: Auto-detect | PASS | Setup auto-detects without prompting |
| C-06: Inertia framing | PARTIAL | Inertia is a row but not narratively developed |
| C-07: External verify | FAIL | No WebSearch cited in prompt body |
| C-08: Risk reframing | FAIL | No --mode risk or exec framing |
| C-09: GTM difficulty | PARTIAL | GTM role runs but no explicit difficulty scale |
| C-10: Amend specificity | PARTIAL | "List 3 things" without requiring impact spec |

Essential: 5/5 PASS. Recommended: 0/3. Composite: 60 + 0 + 0 = **60**

---

### V-02: Inertia-first

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01: Inertia row | PASS | Inertia is step 1, explicitly first |
| C-02: Whitespace | PASS | Step 3 explicitly asks for whitespace |
| C-03: Table stakes | PASS | Listed last in findings |
| C-04: Threat level | PASS | "None = always HIGH" explicitly stated |
| C-05: Auto-detect | PASS | "Auto-detect without prompting" stated |
| C-06: Inertia framing | PASS | Step 1 asks "WHY do teams do nothing?" -- narrative required |
| C-07: External verify | FAIL | No WebSearch cited |
| C-08: Risk reframing | FAIL | No --mode risk or exec framing |
| C-09: GTM difficulty | FAIL | GTM role not included in this variation |
| C-10: Amend specificity | PASS | "3 specific adjustments with impact" -- requires impact |

Essential: 5/5 PASS. Recommended: 1/3 (C-06). Composite: 60 + 10 + 0 = **70**

**Excellence signal**: C-06 passes here but not in V-01. The "WHY do teams do nothing?" instruction
forces the narrative development of inertia that C-06 requires.

---

### V-03: Role-reduced (PM + Strategy only)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01: Inertia row | PASS | "Inertia as a competitor row" in findings |
| C-02: Whitespace | PASS | Strategy role explicitly covers whitespace |
| C-03: Table stakes | PASS | Listed in findings |
| C-04: Threat level | PASS | "Threat level per competitor" in findings |
| C-05: Auto-detect | PASS | "Auto-detect without prompting" stated |
| C-06: Inertia framing | FAIL | No "why do teams do nothing?" instruction |
| C-07: External verify | FAIL | No WebSearch cited |
| C-08: Risk reframing | FAIL | No --mode risk |
| C-09: GTM difficulty | FAIL | GTM role removed |
| C-10: Amend specificity | PASS | "3 adjustments with impact" stated |

Essential: 5/5 PASS. Recommended: 0/3. Composite: 60 + 0 + 5 = **65**

Note: Removing Architect and GTM loses technical moat and distribution analysis.
This weakens the brief for technical audiences. Not a useful variation direction.

---

### V-04: Traffic-light format

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01: Inertia row | PASS | "including none/status quo" in execute |
| C-02: Whitespace | PASS | "Whitespace (where all competitors are LOW)" |
| C-03: Table stakes | PASS | "Table stakes (features all HIGH competitors have)" |
| C-04: Threat level | PASS | Overall threat: HIGH/MEDIUM/LOW per row |
| C-05: Auto-detect | PASS | "Auto-detect" stated |
| C-06: Inertia framing | FAIL | No inertia narrative beyond the row |
| C-07: External verify | FAIL | No WebSearch cited |
| C-08: Risk reframing | PASS | "--mode risk reframing for exec audiences" explicitly in findings |
| C-09: GTM difficulty | PASS | Distribution dimension: HIGH/MEDIUM/LOW |
| C-10: Amend specificity | PASS | "3 specific adjustments with impact" |

Essential: 5/5 PASS. Recommended: 1/3 (C-08). Composite: 60 + 10 + 10 = **80**

**Excellence signal**: C-08 passes here via traffic-light. The "--mode risk reframing" instruction
in the findings section is what triggers this. Also C-09 passes via the distribution dimension.

---

### V-05: Narrative-first

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01: Inertia row | PASS | "None/status quo" in setup |
| C-02: Whitespace | PASS | "The Whitespace" is section 2 of findings |
| C-03: Table stakes | PASS | "The Table Stakes" is section 3 |
| C-04: Threat level | PASS | "Threat summary" per competitor |
| C-05: Auto-detect | PASS | "Auto-detect domain" stated |
| C-06: Inertia framing | PASS | "The Primary Competitor (why inertia is the real threat)" -- section 1 |
| C-07: External verify | FAIL | No WebSearch cited |
| C-08: Risk reframing | PASS | "--mode risk: cost of building the wrong thing" explicit |
| C-09: GTM difficulty | PARTIAL | GTM role runs but no explicit difficulty scale in this variation |
| C-10: Amend specificity | PASS | "3 specific adjustments with impact" |

Essential: 5/5 PASS. Recommended: 2/3 (C-06, C-08). Composite: 60 + 20 + 5 = **85**

**Excellence signals**:
- C-06: "The Primary Competitor" as section 1 forces the inertia narrative
- C-08: "--mode risk" framing explicit in findings structure

---

## Leaderboard

| Rank | Variation | Composite | Essential | Rec passed |
|------|-----------|-----------|-----------|------------|
| 1 | V-05 Narrative-first | 85 | 5/5 | 2/3 |
| 2 | V-04 Traffic-light | 80 | 5/5 | 1/3 |
| 3 | V-02 Inertia-first | 70 | 5/5 | 1/3 |
| 4 | V-03 Role-reduced | 65 | 5/5 | 0/3 |
| 5 | V-01 Baseline | 60 | 5/5 | 0/3 |

---

## Excellence Signals

| Signal | Criterion | Variation | Pattern |
|--------|-----------|-----------|---------|
| ES-01 | C-06 (inertia narrative) | V-02, V-05 | Name inertia as "The Primary Competitor" and ask WHY teams do nothing -- this forces narrative, not just a row |
| ES-02 | C-08 (risk reframing) | V-04, V-05 | Explicitly include "--mode risk" as a named findings section -- it must be instructed, not implied |
| ES-03 | C-09 (GTM difficulty) | V-04 | Traffic-light distribution dimension produces C-09 naturally -- a named distribution assessment scale is needed |

---

## Failure Patterns

**C-07 (WebSearch verification)**: FAILS in all 5 variations. This is a skill design issue --
the WebSearch tool is declared but no variation explicitly instructs the skill to use it
for verification. Add to all variations: "Use WebSearch to verify at least one key
competitive claim. Cite the source."

---

## Round 1 Verdict

V-05 (narrative-first) leads at 85. Not yet at golden threshold (all essential + composite >= 80
AND recommended >= 2/3). V-05 hits 2/3 recommended. Missing: C-07 (WebSearch verification).

**Proposed rubric update (QU3)**:
- Pattern from ES-01: "The Primary Competitor" naming forces inertia narrative -- add to rubric
- Pattern from ES-02: "--mode risk" section naming forces exec reframing -- add to rubric
- C-07 failure is universal -- clarify: this is a generation-time issue, not a rubric issue.
  The skill body must explicitly instruct WebSearch use.

**Next round**: Generate V-06 combining V-05 structure + explicit WebSearch instruction +
inertia as "The Primary Competitor" (combining ES-01 and ES-07 into one variation).
