Now I have everything I need. Let me write the scorecard.

---

## Round 4 Scorecard — draft-pitch

### Per-Criterion Scoring

#### V-01 — Single Axis: Output Format (Explicit Failure Mode Column)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Phase 5 has explicit Exec / Dev / Maker sections |
| C-02 | Each version has all four elements | PASS | Hook, What It Does, Why It Matters, CTA in all three |
| C-03 | Exec version outcome-first, ROI framing | PASS | Phase 4 gate enforces outcome-first; Hook = locked EXEC OPENING SENTENCE; Why = ROI + named competitor |
| C-04 | Anti-positioning section present | PASS | Phase 6 "What Signal Is NOT," minimum four bullets |
| C-05 | Dev version shows the tool | PASS | "At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`." |
| C-06 | Maker version is jargon-free | PASS | "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology." |
| C-07 | Prior signals consulted | PASS | Phase 1 signal intake; documents overrides; waived if no signals found |
| C-08 | Proof points specific and traceable | PASS | Phase 7 requires `[source: {artifact-path}]` or `[UNVERIFIED]` flag on every factual claim |
| C-09 | Inertia named as primary competitor | PASS | DEFAULTS: Primary competitor = "teams doing nothing -- the review that never happened"; Phase 5 exec: "The alternative is not a competing product. It is [Competitor]." |
| C-10 | Exec self-check embedded at generation time | PASS | Phase 4 binary gate (YES/NO), rewrite loop before Phase 5 begins |
| C-11 | Positioning locked in writing before prose | PASS | Phases 2+3 produce locked named outputs; Phase 5 cannot revise their content |
| C-12 | Default fallback values for missing signals | PASS | DEFAULTS table at top of skill; "These apply unconditionally to all runs." |
| C-13 | DEFAULTS loaded unconditionally before intake | PASS | DEFAULTS table appears before Phase 1; explicit unconditional statement |
| C-14 | Gate output named and cited downstream | PASS | Phase 2 *Produces* BELIEF MAP → Phase 5 cites by exact name; Phase 3 *Produces* POSITIONING LOCK → Phase 5 cites by exact name; Phase 4 *Produces* EXEC OPENING SENTENCE → Phase 5 cites by exact name |
| C-15 | Belief mapping precedes argument construction | PASS | Phase 2 BELIEF MAP filled and locked before Phase 5; "Core Belief" column per audience |
| C-16 | Multi-node named dependency chain | PASS | Three-node chain: BELIEF MAP → Phase 5 by exact name; POSITIONING LOCK → Phase 5 by exact name; EXEC OPENING SENTENCE → Phase 5 by exact name; chain readable from structure |
| C-17 | Belief mapping includes per-audience failure modes | PASS | Failure Mode column definition: "A restatement of Core Belief in negative form does not pass (e.g., 'Exec won't believe the ROI argument' is a belief restatement, not a Failure Mode)." Negative example structurally enforces distinction. |
| C-18 | Per-audience inertia in DEFAULTS + structural CTA template | FAIL | DEFAULTS has single shared "Inertia cost" field; CTAs use BELIEF MAP Inertia Counter but no "Instead of [audience inertia], [action]" template; no per-audience DEFAULTS rows |

**Counts**: Essential 4/4, Recommended 3/3, Aspirational 10/11

```
composite = (4/4 × 60) + (3/3 × 30) + (10/11 × 10)
          = 60 + 30 + 9.09
          = 99.1
```

**Golden: YES** | Score: **99.1**

---

#### V-02 — Single Axis: Inertia Framing (Per-Audience DEFAULTS + "Instead Of" Template)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Phase 5 Exec / Dev / Maker |
| C-02 | Each version has all four elements | PASS | Hook, What, Why, CTA in all three |
| C-03 | Exec version outcome-first, ROI framing | PASS | Phase 4 gate; Hook = locked EXEC OPENING SENTENCE; Why = ROI framing |
| C-04 | Anti-positioning section present | PASS | Phase 6 "What Signal Is NOT," minimum four bullets |
| C-05 | Dev version shows the tool | PASS | Concrete interaction example with `/scout:requirements` |
| C-06 | Maker version is jargon-free | PASS | Explicit zero-acronym instruction |
| C-07 | Prior signals consulted | PASS | Phase 1 signal intake |
| C-08 | Proof points specific and traceable | PASS | Phase 7 proof audit with citation requirements |
| C-09 | Inertia named as primary competitor | PASS | Primary competitor in DEFAULTS; Exec Why It Matters names competitor explicitly |
| C-10 | Exec self-check embedded at generation time | PASS | Phase 4 binary gate with rewrite loop |
| C-11 | Positioning locked in writing before prose | PASS | Phases 2+3 lock outputs before Phase 5 |
| C-12 | Default fallback values for missing signals | PASS | DEFAULTS at top, unconditional |
| C-13 | DEFAULTS loaded unconditionally before intake | PASS | DEFAULTS before Phase 1 |
| C-14 | Gate output named and cited downstream | PASS | 3-node chain: BELIEF MAP + POSITIONING LOCK + EXEC OPENING SENTENCE all produced and consumed by exact name |
| C-15 | Belief mapping precedes argument construction | PASS | Phase 2 fills "Must believe before anything else" per audience before Phase 5 |
| C-16 | Multi-node named dependency chain | PASS | 3-node chain with Produces/Consumes metadata; chain readable from skill structure |
| C-17 | Belief mapping includes per-audience failure modes | FAIL | "Argument fails if" column header only; no definitional instruction distinguishing outcome failure from belief restatement; no negative example; strict reading of C-17 pass condition ("explicit failure mode... restatement of belief does not pass") requires enforcement mechanism, not just a column label |
| C-18 | Per-audience inertia in DEFAULTS + structural CTA template | PASS | DEFAULTS has Exec inertia / Dev inertia / Maker inertia rows; CTAs use "Instead of [active X inertia from SIGNAL DEFAULTS], [one concrete action]" template for all three audiences |

**Counts**: Essential 4/4, Recommended 3/3, Aspirational 10/11

```
composite = (4/4 × 60) + (3/3 × 30) + (10/11 × 10)
          = 60 + 30 + 9.09
          = 99.1
```

**Golden: YES** | Score: **99.1**

---

#### V-03 — Single Axis: Lifecycle Emphasis (3-Node Chain on C-18 Base)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Step 5 Exec / Dev / Maker |
| C-02 | Each version has all four elements | PASS | Hook, What, Why, CTA in all three |
| C-03 | Exec version outcome-first, ROI framing | PASS | Step 4 gate; Hook = locked EXEC OPENING SENTENCE |
| C-04 | Anti-positioning section present | PASS | Step 6 "What Signal Is NOT," minimum three bullets; C-04 requires at least one category, three qualifies |
| C-05 | Dev version shows the tool | PASS | Concrete interaction example |
| C-06 | Maker version is jargon-free | PASS | Explicit zero-acronym, zero CLI instruction |
| C-07 | Prior signals consulted | PASS | Step 1 signal intake |
| C-08 | Proof points specific and traceable | PASS | Step 7 proof points with citation requirements |
| C-09 | Inertia named as primary competitor | PASS | Primary competitor in DEFAULTS; Exec Why It Matters: "The alternative is [Competitor]. Signal eliminates that cost before the build starts." |
| C-10 | Exec self-check embedded at generation time | PASS | Step 4 binary gate with rewrite loop |
| C-11 | Positioning locked in writing before prose | PASS | Steps 2+3 lock outputs before Step 5 |
| C-12 | Default fallback values for missing signals | PASS | DEFAULTS at top, unconditional |
| C-13 | DEFAULTS loaded unconditionally before intake | PASS | DEFAULTS before Step 1 |
| C-14 | Gate output named and cited downstream | PASS | Step 2 *Produces* AUDIENCE BELIEF MAP; Step 3 *Produces* POSITIONING LOCK; Step 4 *Produces* EXEC OPENING SENTENCE; Step 5 *Consumes* all three by exact name |
| C-15 | Belief mapping precedes argument construction | PASS | "Do not draft pitch content until all six lines are written." Explicit gate. |
| C-16 | Multi-node named dependency chain | PASS | 3-node chain: AUDIENCE BELIEF MAP + POSITIONING LOCK + EXEC OPENING SENTENCE; all produced and consumed by exact name; chain readable from structure |
| C-17 | Belief mapping includes per-audience failure modes | FAIL | Prose belief mapping (what must they believe + inertia argument per audience); no failure mode / "pitch fails to achieve" language anywhere; belief mapping captures belief and inertia excuse only |
| C-18 | Per-audience inertia in DEFAULTS + structural CTA template | PASS | DEFAULTS has Exec/Dev/Maker inertia rows; CTAs use "Instead of [inertia argument from AUDIENCE BELIEF MAP], [one concrete action]" structural template |

**Counts**: Essential 4/4, Recommended 3/3, Aspirational 10/11

```
composite = (4/4 × 60) + (3/3 × 30) + (10/11 × 10)
          = 60 + 30 + 9.09
          = 99.1
```

**Golden: YES** | Score: **99.1**

---

#### V-04 — Combined: Output Format + Lifecycle Emphasis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Phase 5 Exec / Dev / Maker |
| C-02 | Each version has all four elements | PASS | Hook, What, Why, CTA in all three |
| C-03 | Exec version outcome-first, ROI framing | PASS | Phase 4 gate; Hook = locked EXEC OPENING SENTENCE; Why = ROI framing with named competitor |
| C-04 | Anti-positioning section present | PASS | Phase 6 "What Signal Is NOT," minimum four bullets |
| C-05 | Dev version shows the tool | PASS | Concrete interaction example |
| C-06 | Maker version is jargon-free | PASS | Explicit zero-acronym instruction |
| C-07 | Prior signals consulted | PASS | Phase 1 signal intake |
| C-08 | Proof points specific and traceable | PASS | Phase 7 proof audit |
| C-09 | Inertia named as primary competitor | PASS | Primary competitor in DEFAULTS; Exec: "The alternative is not a competing product. It is [Competitor]." |
| C-10 | Exec self-check embedded at generation time | PASS | Phase 4 binary gate with rewrite loop |
| C-11 | Positioning locked in writing before prose | PASS | Phases 2+3 locked before Phase 5 |
| C-12 | Default fallback values for missing signals | PASS | DEFAULTS at top, unconditional |
| C-13 | DEFAULTS loaded unconditionally before intake | PASS | DEFAULTS before Phase 1 |
| C-14 | Gate output named and cited downstream | PASS | 3-node chain with Produces/Consumes; Phase 5 consumes all three by exact name |
| C-15 | Belief mapping precedes argument construction | PASS | BELIEF MAP locked before Phase 5; "Draft each version from the Core Belief in BELIEF MAP." |
| C-16 | Multi-node named dependency chain | PASS | 3-node chain: BELIEF MAP + POSITIONING LOCK + EXEC OPENING SENTENCE, all produced and consumed by exact name |
| C-17 | Belief mapping includes per-audience failure modes | PASS | Failure Mode column with explicit instruction: "A restatement of Core Belief in negative form does not pass (e.g., 'Exec won't believe the ROI argument' restates the belief -- it is not a Failure Mode)." Three per-audience Failure Mode examples given inline. |
| C-18 | Per-audience inertia in DEFAULTS + structural CTA template | FAIL | DEFAULTS has single "Inertia cost" field (not per-audience); CTAs are "One specific decision..." / "One command or file path..." — no "Instead of [inertia], [action]" structural template |

**Counts**: Essential 4/4, Recommended 3/3, Aspirational 10/11

```
composite = (4/4 × 60) + (3/3 × 30) + (10/11 × 10)
          = 60 + 30 + 9.09
          = 99.1
```

**Golden: YES** | Score: **99.1**

---

#### V-05 — Combined: All Three Axes (C-16 + C-17 + C-18 Synthesis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Phase 5 Exec / Dev / Maker |
| C-02 | Each version has all four elements | PASS | Hook, What, Why, CTA in all three |
| C-03 | Exec version outcome-first, ROI framing | PASS | Phase 4 gate; Hook = locked EXEC OPENING SENTENCE; What = POSITIONING LOCK Outcome; Why = ROI framing with named competitor |
| C-04 | Anti-positioning section present | PASS | Phase 6 "What Signal Is NOT," minimum four bullets |
| C-05 | Dev version shows the tool | PASS | Concrete interaction example: `/scout:requirements topic={topic}` |
| C-06 | Maker version is jargon-free | PASS | "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology." |
| C-07 | Prior signals consulted | PASS | Phase 1 signal intake with documented overrides |
| C-08 | Proof points specific and traceable | PASS | Phase 7 proof audit |
| C-09 | Inertia named as primary competitor | PASS | DEFAULTS Primary competitor = "teams doing nothing"; Phase 5 exec names competitor explicitly |
| C-10 | Exec self-check embedded at generation time | PASS | Phase 4 binary gate with rewrite loop at generation time |
| C-11 | Positioning locked in writing before prose | PASS | Phases 2+3 lock BELIEF MAP and POSITIONING LOCK before Phase 5 begins |
| C-12 | Default fallback values for missing signals | PASS | DEFAULTS at top, unconditional statement |
| C-13 | DEFAULTS loaded unconditionally before intake | PASS | DEFAULTS table appears before Phase 1; "These apply unconditionally to all runs." |
| C-14 | Gate output named and cited downstream | PASS | Phase 2 *Produces* BELIEF MAP → Phase 5 by exact name; Phase 3 *Produces* POSITIONING LOCK → Phase 5 by exact name; Phase 4 *Produces* EXEC OPENING SENTENCE → Phase 5 by exact name |
| C-15 | Belief mapping precedes argument construction | PASS | BELIEF MAP locked before Phase 5; "Draft each version from the Core Belief in BELIEF MAP." Phase 5 explicitly driven from belief anchors. |
| C-16 | Multi-node named dependency chain | PASS | 3-node chain: BELIEF MAP + POSITIONING LOCK + EXEC OPENING SENTENCE; all assigned named identifiers at creation and consumed by Phase 5 by exact name; chain readable from skill structure alone |
| C-17 | Belief mapping includes per-audience failure modes | PASS | 4-column BELIEF MAP with Failure Mode column definition: "Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., 'Exec won't authorize the demo slot')." Negative example inline: "'Exec won't believe the ROI argument' -- this restates the belief and is not a Failure Mode." Per-audience enforcement. |
| C-18 | Per-audience inertia in DEFAULTS + structural CTA template | PASS | DEFAULTS has Exec inertia / Dev inertia / Maker inertia rows; BELIEF MAP Inertia Excuse column binds to these DEFAULTS rows ("Use active Exec/Dev/Maker inertia or scout override"); Phase 5 CTAs use "Instead of [active audience inertia from SIGNAL DEFAULTS], [one concrete action]" structural template for all three audiences |

**Counts**: Essential 4/4, Recommended 3/3, Aspirational 11/11

```
composite = (4/4 × 60) + (3/3 × 30) + (11/11 × 10)
          = 60 + 30 + 10
          = 100
```

**Golden: YES** | **Platinum** | Score: **100**

---

### Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Score | Band |
|------|-----------|-----------|-------------|--------------|-------|------|
| 1 | V-05 All three axes | 4/4 | 3/3 | 11/11 | **100** | Platinum |
| 2 | V-01 Output format | 4/4 | 3/3 | 10/11 | **99.1** | Golden |
| 2 | V-02 Inertia framing | 4/4 | 3/3 | 10/11 | **99.1** | Golden |
| 2 | V-03 Lifecycle emphasis | 4/4 | 3/3 | 10/11 | **99.1** | Golden |
| 2 | V-04 Output format + Lifecycle | 4/4 | 3/3 | 10/11 | **99.1** | Golden |

### The single discriminator: C-18

V-01 and V-04 fail C-18 (per-audience DEFAULTS + "Instead of" template) because they retain a single shared "Inertia cost" DEFAULTS field and their CTA instructions address inertia narratively rather than via the structural template. V-02 and V-03 fail C-17 (explicit outcome-failure per audience) — V-02 by relying on a bare column header without a definitional instruction that prevents belief restatement; V-03 by using prose belief mapping with no failure mode field at all. Only V-05 satisfies all three new R4 criteria simultaneously.

### Discrimination within the 99.1 cluster

| Variation | Failing criterion | Root cause |
|-----------|-----------------|------------|
| V-01 | C-18 | Inertia cost is a single shared DEFAULTS field; CTA uses Inertia Counter column but no "Instead of [named DEFAULTS field]" template |
| V-02 | C-17 | "Argument fails if" column lacks definitional instruction; structural enforcement of outcome-failure vs. belief-restatement distinction is absent |
| V-03 | C-17 | No failure mode concept in prose belief mapping; captures beliefs and inertia excuses only |
| V-04 | C-18 | Single shared "Inertia cost" DEFAULTS field; CTAs are freeform ("One specific decision...") with no structural inertia template |

### Excellence Signals from V-05

**ES-01 — Pre-committed Inertia Counter column in BELIEF MAP**
V-05 adds an "Inertia Counter" column to BELIEF MAP. The counter action for each audience is determined and locked during belief-mapping (Phase 2), not invented during drafting (Phase 5). Phase 5's CTA instruction is assembly from a locked counter, not composition from a blank slate. This moves the key CTA decision point earlier in the pipeline — to belief-mapping time — making the CTA structurally pre-committed rather than freestyle.

**ES-02 — DEFAULTS-row binding in BELIEF MAP column definition**
V-05's Inertia Excuse column definition explicitly says "Use active Exec/Dev/Maker inertia or scout override" — binding each BELIEF MAP cell to a named DEFAULTS field. This creates a three-tier verifiable lineage: DEFAULTS → BELIEF MAP inertia cells (bound by name) → CTA template (references DEFAULTS by name). At each junction the lineage is inspectable from skill structure alone. Prior variations that passed C-18 (V-03 R3, V-03 R4) had CTAs reference AUDIENCE BELIEF MAP inertia argument but without the explicit DEFAULTS binding in the table definition itself.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-committed Inertia Counter column in BELIEF MAP locks CTA action at belief-mapping time before drafting begins", "DEFAULTS-row binding in BELIEF MAP column definition creates three-tier verifiable lineage: DEFAULTS field → table cell (bound by name) → CTA structural template (references DEFAULTS by name)"]}
```
