## program-plan Scorecard — Round 4

**Rubric**: v4 (145 pts) | **Golden threshold**: 116

---

### Final Ranking

| Rank | ID | Score | Golden | C-18 | C-19 | Notes |
|------|----|-------|--------|------|------|-------|
| 1 | **V-01** | **145/145** | YES | P | **P** | Header embeds cascade requirement — entries demonstrate 3-hop → chains |
| 1 | **V-05** | **145/145** | YES | P | **P** | All entries have 3-hop → chains across all actors |
| 3 | V-02 | 140/145 | YES | P | F | Post-table cascade check: strong instruction but entries shown are single-consequence |
| 3 | V-03 | 140/145 | YES | P | F | Cascade requirement is conditional; demonstrated entries are single-consequence |
| 3 | V-04 | 140/145 | YES | P | F | Opener priming insufficient; entries single-consequence despite rich cascade narrative |

All five variations pass all essential criteria and are GOLDEN (>= 116).

---

### Hypotheses Resolved

**R4-H01**: RESOLVED — Header-embedded cascade (V-01) reliably drives multi-hop entries. The header-loading pattern from C-18 generalizes to cascade depth. V-01 = 145/145.

**R4-H02**: RESOLVED — Post-table cascade gate (V-02) does NOT outperform header instruction. V-02 entries remain single-consequence. V-01 (145) > V-02 (140).

**R4-H03**: RESOLVED — Cascade contrast opener alone (V-04) is INSUFFICIENT. Even with "the cascade begins here" in the PM entry, no table entry uses → notation. Explicit table-level instruction required.

**R4-H04**: RESOLVED — V-05 max-redundancy (145) > V-03 minimal form (140). The decisive factor is whether entries ARE cascades, not whether instructions REQUIRE cascades. Pre-filled → chains in the template are what passes C-19.

---

### Key New Pattern

**C-19 passes when cascades are demonstrated in the template's own actor table, not when instructions require them.** V-01 and V-05 pre-fill entries with → chains and pass. V-02/V-03/V-04 use instructions or priming but their entries are single-consequence and fail. The implication: to reliably elicit → cascades, the variation must contain example entries that are themselves cascades — the column header is the most instruction-efficient way to achieve this.

**V-01 is the new efficient frontier** — one axis change from R3 V-03 (header embeds cascade notation requirement) reaches the 145/145 ceiling. V-03 no longer holds this position.

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["header-embedded cascade requirement is sufficient for C-19: upgrading column header to include arrow notation and 2+ ordered consequences requirement drives cascade entries reliably -- the header-loading pattern from C-18 generalizes to cascade depth", "C-19 passes when cascade entries are demonstrated in the variation's own actor table, not when instructions require cascades: post-table checks and conditional requirements fail when the entries shown are single-consequence", "cascade opener priming alone is insufficient for C-19: explicit arc-layer cascade narrative in the opener does not elicit arrow-chain entries in the actor table without a table-level notation requirement", "V-01 is the new efficient frontier: header cascade requirement achieves 145/145 with minimal change from R3 V-03, replacing V-03 as the recommended canonical form"]}
```
earlier -- and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)." Primary label is "cannot run earlier" -- displacement-impossibility framing. Not parenthetical. |
| C-19 | Multi-hop downstream consequence cascade | **PASS** | Actor table entries IN the variation body demonstrate -> cascades. PM: "Moved later: design targets an unvalidated problem -> review evaluates a design anchored in wrong assumptions -> prove tests a hypothesis with no market grounding." 3-hop chain crossing breadth->design->depth layers. All six actor entries have full -> chains. *Resolves R4-H01: header-loading pattern generalizes to cascade depth requirements.* |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P] C-18 [P]
              C-19 [P]
              Pass count: 11 / 11  -> 11 * 5  = 55 pts (of 55)

Composite score: 145 / 145

Golden: all essential pass AND composite >= 116  ->  [X] YES
```

---

### V-02 -- Post-Table Cascade Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 identical to V-01 |
| C-02 | Echo stage contract | **PASS** | Step 6 identical |
| C-03 | All referenced skills valid | **PASS** | Inline catalog present; "no other skill names exist" |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 bans abstract completions |
| C-05 | Skills ordered by dependency | **PASS** | Evidence arc enforces layer order |
| C-06 | Stages group meaningfully | **PASS** | Step 5 identical |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 requires specific artifact type names |
| C-08 | Stage names descriptive | **PASS** | Step 5 identical |
| C-09 | Strategic pacing | **PASS** | Arc layer structure with layer-feeds-layer rationale |
| C-10 | Gates quantified | **PASS** | `>=N` required in Step 4 |
| C-11 | Skill catalog grounded inline | **PASS** | Inline catalog present |
| C-12 | Actor-role framing | **PASS** | Handoff format with named actors |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` inside Step 4 |
| C-14 | Naive-competitor framing | **PASS** | Same opener as V-01: "Naive program plans sort skills by namespace... This variation defeats that by two mechanisms..." Failure mode + structural choices both named. |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this actor cannot run earlier -- what breaks if displaced." PM: "Moved later: design targets an unvalidated problem." Each entry has position rationale + consequence-of-displacement. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Step 4 format string with actor + `>=N` + artifact |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "what happens if any gate is removed" |
| C-18 | Column header frames displacement impossibility | **PASS** | Column header: "Why this actor cannot run earlier -- what breaks if displaced." Contains "cannot run earlier" -- displacement-impossibility framing as primary label. |
| C-19 | Multi-hop downstream consequence cascade | **FAIL** | Actor table entries shown in the variation body are all single-consequence: PM "Moved later: design targets an unvalidated problem." No entry uses -> notation to chain 2+ ordered hops. The post-table arc cascade check provides format + conditional instruction ("If no entry has this depth, expand one entry before continuing") but is a future instruction, not a demonstrated cascade. Entries as demonstrated do not pass. *Resolves R4-H02: post-table check does not outperform header instruction; V-02 (140) < V-01 (145).* |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P] C-18 [P]
              C-19 [F]
              Pass count: 10 / 11  -> 10 * 5  = 50 pts (of 55)

Composite score: 140 / 145

Golden: all essential pass AND composite >= 116  ->  [X] YES
```

---

### V-03 -- C-18 Strong + C-19 Minimal Form

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 present |
| C-02 | Echo stage contract | **PASS** | Step 6 explicit |
| C-03 | All referenced skills valid | **PASS** | Inline catalog present |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 bans abstract completions |
| C-05 | Skills ordered by dependency | **PASS** | Arc layer mapping enforces order |
| C-06 | Stages group meaningfully | **PASS** | Step 5 same |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 requires artifact naming |
| C-08 | Stage names descriptive | **PASS** | Step 5 examples |
| C-09 | Strategic pacing | **PASS** | Breadth->Design->Depth->Synthesis arc with layer-output logic |
| C-10 | Gates quantified | **PASS** | `>=N` required |
| C-11 | Skill catalog grounded inline | **PASS** | Inline catalog present |
| C-12 | Actor-role framing | **PASS** | Handoff format |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` in Step 4 |
| C-14 | Naive-competitor framing | **PASS** | Same opener: "This variation defeats that by two mechanisms: actor-layer assignment... and a required handoff+threshold gate format..." Both elements present. |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this actor cannot run earlier -- and what breaks if displaced." PM: "Moved later: design targets an unvalidated problem." Each entry has rationale + consequence. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Step 4 unified format string |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "what happens if any gate is removed" |
| C-18 | Column header frames displacement impossibility | **PASS** | Column header: "Why this actor cannot run earlier -- and what breaks if displaced." Contains "cannot run earlier" as primary framing -- not parenthetical. |
| C-19 | Multi-hop downstream consequence cascade | **FAIL** | Actor table entries shown in the variation body are all single-consequence: PM "Moved later: design targets an unvalidated problem." Architect/PM "Moved earlier: design is unconstrained speculation with no landscape anchor." The post-table cascade requirement ("Expand one entry now if no chain is present") is a conditional instruction that acknowledges the entries don't currently have cascades. Entries demonstrated in the variation are single-hop and do not pass. |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P] C-18 [P]
              C-19 [F]
              Pass count: 10 / 11  -> 10 * 5  = 50 pts (of 55)

Composite score: 140 / 145

Golden: all essential pass AND composite >= 116  ->  [X] YES
```

---

### V-04 -- Cascade Contrast Opener

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 present |
| C-02 | Echo stage contract | **PASS** | Step 6 explicit |
| C-03 | All referenced skills valid | **PASS** | Inline catalog present |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 bans abstract completions |
| C-05 | Skills ordered by dependency | **PASS** | Arc layer mapping |
| C-06 | Stages group meaningfully | **PASS** | Step 5 |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 requires artifact type names |
| C-08 | Stage names descriptive | **PASS** | Step 5 examples |
| C-09 | Strategic pacing | **PASS** | Arc structure with layer-output rationale |
| C-10 | Gates quantified | **PASS** | `>=N` required |
| C-11 | Skill catalog grounded inline | **PASS** | Inline catalog present |
| C-12 | Actor-role framing | **PASS** | Handoff format with actors |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` in Step 4 |
| C-14 | Naive-competitor framing | **PASS** | "This variation defeats arc-layer cascade failure by two structural choices enforced before any skill is placed: actor-layer assignment that anchors every namespace to its validated prerequisite layer... and a gate format that exposes handoffs between arc layers... A flat skill list cannot prevent a cascade because it has no arc boundaries to protect." Failure mode (arc-layer cascade failure, flat skill list) + structural choices both named. |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this actor cannot run earlier -- what breaks if displaced." PM: "Moved later: design is anchored in the author's assumptions with no validated market context; the cascade begins here." Each entry has rationale + displacement consequence. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Step 4: "all three elements must appear together" with format string |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "what the gates are protecting against -- specifically, what happens if any gate is removed" |
| C-18 | Column header frames displacement impossibility | **PASS** | Column header: "Why this actor cannot run earlier -- what breaks if displaced." Contains "cannot run earlier" -- primary displacement-impossibility framing. |
| C-19 | Multi-hop downstream consequence cascade | **FAIL** | Actor table entries are single-consequence despite rich cascade priming in the opener. PM: "Moved later: design is anchored in the author's assumptions with no validated market context; the cascade begins here." -- single consequence, no -> chain. "The cascade begins here" acknowledges the opener's framing but does not trace subsequent hops with -> notation. No entry uses -> notation to chain 2+ ordered consequences across layers. *Resolves R4-H03: cascade opener priming alone is insufficient -- explicit table-level notation instruction is required.* |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P] C-18 [P]
              C-19 [F]
              Pass count: 10 / 11  -> 10 * 5  = 50 pts (of 55)

Composite score: 140 / 145

Golden: all essential pass AND composite >= 116  ->  [X] YES
```

---

### V-05 -- Full Synthesis Maximum

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | **PASS** | Step 7 present |
| C-02 | Echo stage contract | **PASS** | Step 6: "No other stage may be named `echo`." |
| C-03 | All referenced skills valid | **PASS** | Inline catalog present |
| C-04 | Gates present and non-trivial | **PASS** | Step 4 bans abstract completions |
| C-05 | Skills ordered by dependency | **PASS** | Arc layer enforces Breadth->Design->Depth->Synthesis |
| C-06 | Stages group meaningfully | **PASS** | Step 5 same |
| C-07 | Gate conditions reference artifacts | **PASS** | Step 4 requires specific artifact types |
| C-08 | Stage names descriptive | **PASS** | Step 5 examples |
| C-09 | Strategic pacing | **PASS** | Full arc structure with per-layer output-input chain and cascade archetype |
| C-10 | Gates quantified | **PASS** | `>=N` required |
| C-11 | Skill catalog grounded inline | **PASS** | Inline catalog present |
| C-12 | Actor-role framing | **PASS** | Handoff format with actors |
| C-13 | Quantified gate syntax instructed | **PASS** | `>=N` embedded in Step 4 |
| C-14 | Naive-competitor framing | **PASS** | "The failure mode this variation defeats is arc-layer cascade failure... This variation defeats arc-layer cascade failure by two structural choices enforced before any skill is placed: (1) an actor-layer assignment table with per-actor causal reasoning that traces the cascade of consequences if the actor is displaced..., and (2) a required handoff+threshold gate template... A flat skill list cannot prevent a cascade because it has no arc boundaries to protect." Failure mode (arc-layer cascade failure) + both structural choices explicitly named. Strongest form. |
| C-15 | Why-this-position column | **PASS** | Column header: "Why this actor cannot run earlier -- cascade of failures if displaced (use ->, 2+ hops, cross arc-layer boundaries)." PM entry: "Moved later: design is anchored in assumptions -> review evaluates a design targeting the wrong problem -> prove tests a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously." Full cascade chain per actor. |
| C-16 | Unified handoff+threshold gate template | **PASS** | Step 4: "all three elements must appear together" with format string including actor + `>=N` + artifact |
| C-17 | What-happens-if-removed clause | **PASS** | Step 8: "specifically, what is the multi-hop consequence cascade if the first gate (scout handoff) is removed." Most specific form -- names the first gate and requires cascade consequence reasoning. |
| C-18 | Column header frames displacement impossibility | **PASS** | Column header: "Why this actor cannot run earlier -- cascade of failures if displaced (use ->, 2+ hops, cross arc-layer boundaries)." Contains "cannot run earlier" + cascade requirement in the header itself. Maximum displacement-impossibility + cascade framing in one instruction. |
| C-19 | Multi-hop downstream consequence cascade | **PASS** | Actor table entries IN the variation body demonstrate full -> cascades. PM: "Moved later: design is anchored in assumptions -> review evaluates a design targeting the wrong problem -> prove tests a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously." 3-hop chain. Architect/PM, Team/Researcher, Domain/System Dev, listen, topic entries ALL have 3-hop -> chains. Maximum cascade depth across all entries. *Resolves R4-H04: V-05 maximum-redundancy (145) > V-03 minimal form (140) -- pre-filled cascade entries are the decisive factor.* |

```
Essential:    C-01 [P] C-02 [P] C-03 [P] C-04 [P] C-05 [P]
              Pass count: 5 / 5   -> 5 * 12 = 60 pts (of 60)

Recommended:  C-06 [P] C-07 [P] C-08 [P]
              Pass count: 3 / 3   -> 3 * 10 = 30 pts (of 30)

Aspirational: C-09 [P] C-10 [P] C-11 [P] C-12 [P] C-13 [P]
              C-14 [P] C-15 [P] C-16 [P] C-17 [P] C-18 [P]
              C-19 [P]
              Pass count: 11 / 11  -> 11 * 5  = 55 pts (of 55)

Composite score: 145 / 145

Golden: all essential pass AND composite >= 116  ->  [X] YES
```

---

### Final Ranking

| Rank | ID | Score | Golden | C-18 | C-19 | Notes |
|------|----|-------|--------|------|------|-------|
| 1 | V-01 | **145/145** | YES | P | P | Header embeds cascade requirement -- entries demonstrate 3-hop -> chains. New efficient frontier. |
| 1 | V-05 | **145/145** | YES | P | P | Maximum redundancy -- all entries demonstrate 3-hop -> chains across all actors |
| 3 | V-02 | **140/145** | YES | P | F | Post-table check is a strong instruction but entries shown are single-consequence |
| 3 | V-03 | **140/145** | YES | P | F | Cascade requirement is conditional; entries demonstrated are single-consequence |
| 3 | V-04 | **140/145** | YES | P | F | Opener priming insufficient; entries single-consequence despite rich cascade narrative |

---

### Hypotheses Resolved

**R4-H01 (Header-embedded cascade vs. entry depth)**: RESOLVED -- Header-embedded cascade requirement (V-01) reliably drives multi-hop entries in the actor table. The header "cannot run earlier -- and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)" fires at every row; all six V-01 actor entries have 3-hop -> chains. The header-loading pattern from C-18 generalizes fully to cascade depth requirements. V-01 = 145/145.

**R4-H02 (Post-table gate vs. header instruction)**: RESOLVED -- Post-table cascade gate (V-02) does NOT outperform header instruction (V-01). V-02's post-table check provides format + conditional instruction but the entries demonstrated in the variation remain single-consequence. The header mechanism is more reliable because it keeps the cascade requirement visible at every row during table construction. V-01 (145) > V-02 (140).

**R4-H03 (Cascade opener priming alone)**: RESOLVED -- Cascade contrast opener alone (V-04) is INSUFFICIENT for C-19. V-04's opener is the richest cascade narrative of all five variations; the PM entry even notes "the cascade begins here" -- but no entry uses -> notation to chain 2+ ordered hops. Explicit table-level cascade notation instruction is required; opener-level framing cannot substitute for direct instruction. V-04 = 140/145.

**R4-H04 (V-05 max-redundancy vs. V-03 minimal)**: RESOLVED -- V-05 maximum-redundancy (145/145) outperforms V-03 minimal form (140/145). The decisive factor is whether actor table entries shown in the variation demonstrate -> cascades, not whether instructions require them. V-05 pre-fills all entries with 3-hop chains; V-03's post-table cascade requirement sentence doesn't produce demonstrated cascades in its own entries. C-19 passes when cascades ARE present in the template, not when they are required by a conditional.

---

### Excellence Signals (New Patterns)

1. **Header-embedded cascade requirement is both sufficient and the new efficient frontier** -- V-01 achieves 145/145 with a single axis change from R3 V-03: upgrading the column header to include "(use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)". The header-loading mechanism that made C-18 reliable generalizes to cascade depth. V-01 is the minimum-instruction path to 145/145 and replaces V-03 as the recommended canonical form.

2. **C-19 passes when cascade entries ARE demonstrated in the template's actor table, not when instructions REQUIRE cascades** -- V-01 and V-05 pre-fill entries with full -> chains; they pass C-19. V-02/V-03 provide strong cascade requirement instructions (post-table check, conditional expansion) but the entries shown are single-consequence; they fail C-19. The criterion evaluates what the variation demonstrates, not what it instructs. For prompt design: the actor table template must contain example entries that are themselves cascades.

3. **Opener cascade priming requires explicit table-level instruction to fire in table entries** -- V-04 contains the most elaborate cascade narrative of any R4 variation; the PM entry even acknowledges "the cascade begins here" -- but without explicit "use -> notation" instruction at the table level, the cascade framing stays in the opener and does not produce -> chain entries. The opener teaches the pattern; a direct table-level instruction elicits the notation.

4. **V-01 is the new minimum-form ceiling path** -- R3 V-03 was the efficient frontier at 135/135. In R4, V-01 (header cascade requirement, one axis change from R3 V-03) reaches 145/145 while V-03 (post-table cascade requirement) scores 140/145. The minimum-form path to the v4 ceiling is: retain V-03's C-14/C-15 compact framing + upgrade column header to embed -> cascade notation requirement directly.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["header-embedded cascade requirement is sufficient for C-19: upgrading column header to include arrow notation and 2+ ordered consequences requirement drives cascade entries reliably -- the header-loading pattern from C-18 generalizes to cascade depth", "C-19 passes when cascade entries are demonstrated in the variation's own actor table, not when instructions require cascades: post-table checks and conditional requirements fail when the entries shown are single-consequence", "cascade opener priming alone is insufficient for C-19: explicit arc-layer cascade narrative in the opener does not elicit arrow-chain entries in the actor table without a table-level notation requirement", "V-01 is the new efficient frontier: header cascade requirement achieves 145/145 with minimal change from R3 V-03, replacing V-03 as the recommended canonical form"]}
```
