Now I have everything. Let me score all five variations.

---

# Quest Scorecard — `topic-story` Round 6 (Rubric v6)

**Date**: 2026-03-15  
**Skill**: topic-story  
**Rubric**: v6 (C-01 through C-20; essential C-01–C-04)  
**Trace artifact**: none (placeholder)

---

## Evaluation Method

These are prompt templates — not completed outputs. Each criterion is evaluated as: **does the prompt structure mechanically enforce this criterion in any compliant output?** PASS = structurally guaranteed. PARTIAL = encouraged but with gap. FAIL = not addressed.

---

## V-01 — Role Sequence (Signal Analyst → Bridge Builder → Narrator)

**Axis**: Role sequence — three named roles in strict completion order.

### Essential Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "The story must open with the recommendation — not build toward it." BLUF before Beat 1 explicitly required. |
| C-02 | **PASS** | All five beats named with their exact labels (Beat 1–5). |
| C-03 | **PASS** | Pattern Block must "name a relationship, tension, or gap that no single signal reveals alone." Bridge Builder role completes this analytically before narration begins. |
| C-04 | **PASS** | Pattern forced to be a single, self-contained sentence naming relationship/tension/gap. Role-based gate prevents narrative prose before this is locked. |

**Essential: 4/4**

### Recommended Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-05 | **PASS** | Signal Analyst requires at least three distinct namespaces explicitly. |
| C-06 | **PASS** | Beat 4: "If [this question] resolves to [X], the recommendation moves from [current verb] to [alternate verb]." Direction-specific enforcement. |
| C-07 | **PARTIAL** | Bridge Builder requires one of proceed/pause/pivot/abandon; posture required in Beat 5. But no explicit calibration mapping (strong positive → proceed etc.) stated anywhere. A model could produce mixed posture with proceed verb without contradiction. |

**Recommended: 2/3**

### Aspirational Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Three-role sequence creates inherent arc (Analyst → synthesis → narrative). |
| C-09 | **PASS** | Delta Block required in Bridge Builder; Beat 2 requires explicit "we expected X but found Y" restatement. |
| C-10 | **PASS** | "The pattern: [sentence]" labeled block required in Part 1. |
| C-11 | **PASS** | Beat 5 bridge sentence directly connects pattern to verb. |
| C-12 | **PASS** | Beat 4 direction annotation is explicit and specific. |
| C-13 | **PASS** | Beat 5 item 3: "A team deciding X should do Y, not as a finding." Explicitly required. |
| C-14 | **PASS** | Pattern Block must "Stand without the surrounding narrative (C-14)" — literal criterion reference in the prompt. |
| C-15 | **PASS** | Delta Block produced in Part 1 (Bridge Builder) before Part 2 (Narrator). Structural gate. |
| C-16 | **PASS** | Beat 5 item 1 requires exact posture restatement formula. |
| C-17 | **PASS** | Beat 5 item 2 requires bridge sentence restated independently of Part 1 placement. |
| C-18 | **PASS** | Named Part 1 / Part 2 separator; "A role may not begin until the role before it has fully completed its block." |
| C-19 | **PASS** | Per-artifact: "Production here does NOT satisfy the Beat N requirement. Both placements must be independently satisfied. (C-19)" — stated for Pattern Block, Delta Block, and Bridge Sentence. |
| C-20 | **PASS** | Beat 5 items 1 and 2 each note: "inconsistency between placements is self-revealing. (C-20)." |

**Aspirational: 13/13**

### Score

```
composite = (4/4 × 60) + (2/3 × 30) + (13/13 × 10)
          = 60 + 20 + 10
          = 90
```

**All essential pass. Composite: 90. Status: GOLDEN.**

---

## V-02 — Output Format (Pre-composition as structured table)

**Axis**: Output format — single pre-composition table with Artifact / Content / Required Again In columns.

### Essential Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "The story must open with the recommendation before the first labeled beat." BLUF required before Beat 1. |
| C-02 | **PASS** | Five beats with required labels. |
| C-03 | **PASS** | Pattern row required: "one self-contained sentence naming a relationship, tension, or gap that no single signal shows alone." Beat 3 opens with it. |
| C-04 | **PASS** | Table structure enforces pattern as a discrete analytical output before narration. |

**Essential: 4/4**

### Recommended Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-05 | **PASS** | Signal inventory row: "Minimum 3 distinct namespaces." |
| C-06 | **PASS** | Beat 4: "If [this] resolves to [X], this moves from [current verb] to [alternate verb]." |
| C-07 | **PARTIAL** | Recommendation verb row present, posture row present, Beat 5 posture-to-verb link visible. But no calibration mapping stated (strong positive → proceed etc.). Gap identical to V-01. |

**Recommended: 2/3**

### Aspirational Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-08 | **PASS** | BLUF + five-beat structure creates narrative arc. |
| C-09 | **PASS** | Delta row required; Beat 2 requires "explicit 'we expected X but found Y' statement." |
| C-10 | **PASS** | Pattern labeled in table; Beat 3 opens with it as "discrete labeled statement." |
| C-11 | **PASS** | Bridge sentence row; Beat 5 includes it. |
| C-12 | **PASS** | Beat 4 direction-specific required. |
| C-13 | **PASS** | Beat 5 item 3: "A [role] deciding [question] should [action]." |
| C-14 | **PASS** | Pattern is "one self-contained sentence" in table; Beat 3 instruction: "Do not bury the pattern in flowing prose." |
| C-15 | **PASS** | Delta produced in table (Part 1) before narrative. |
| C-16 | **PASS** | Beat 5 item 1: posture restatement formula required. |
| C-17 | **PASS** | Beat 5 item 2: bridge sentence independent of table. |
| C-18 | **PASS** | Named Part 1 / Part 2 separator; table format makes pre-composition structurally visible and scannable. |
| C-19 | **PASS** | "Non-substitution rule" section: "Each artifact in the 'Required Again In' column must be restated independently at the named beat. The table is an analytic record, not a reusable reference. Pointing a reader to the table does not satisfy a beat-level placement requirement. (C-19)" — global statement covering all artifacts. "Required Again In" column makes this scannable at a glance. |
| C-20 | **PASS** | "Multi-stage consistency rule" section: "If the content differs between the table and the beat, the output is inconsistent. Inconsistency between the two placements is structurally visible and constitutes a failure. (C-20)" |

**Aspirational: 13/13**

### Score

```
composite = (4/4 × 60) + (2/3 × 30) + (13/13 × 10)
          = 60 + 20 + 10
          = 90
```

**All essential pass. Composite: 90. Status: GOLDEN.**

**V-02 differentiator vs V-01**: The "Required Again In" column makes non-substitution *scannable* — a reader can verify compliance for all artifacts in one table scan. V-01 states non-substitution per-artifact in prose; V-02 makes the structure itself carry the requirement.

---

## V-03 — Lifecycle Emphasis (Explicit gate, per-placement non-substitution)

**Axis**: Lifecycle emphasis — non-substitution stated at every individual artifact placement point.

### Essential Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "The story opens with the recommendation — not with context, not with hedging. A story that builds to the recommendation fails." |
| C-02 | **PASS** | Five beats with required labels. |
| C-03 | **PASS** | Pattern [C] required as cross-signal claim before narrative. Beat 3 opens with it. |
| C-04 | **PASS** | Pattern [C] must name relationship/tension/gap that no single signal alone reveals. |

**Essential: 4/4**

### Recommended Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-05 | **PASS** | "[A] Signal coverage: At least three distinct namespaces must be identifiable." |
| C-06 | **PASS** | Beat 4: direction-specific uncertainty with verb shift required. |
| C-07 | **PARTIAL** | No calibration mapping (strong positive → proceed etc.) stated. Same gap as V-01/V-02. |

**Recommended: 2/3**

### Aspirational Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Six-output analytic stage + narrative arc. |
| C-09 | **PASS** | Delta [D] identified in Part 1; Beat 2 requires explicit contrast independently. |
| C-10 | **PASS** | Pattern [C] labeled "The pattern: [sentence]" in Part 1. |
| C-11 | **PASS** | Bridge sentence [F] required; Beat 5 includes it. |
| C-12 | **PASS** | Beat 4 direction-specific. |
| C-13 | **PASS** | Beat 5 item 3: decision framing required. |
| C-14 | **PASS** | Pattern [C] "must be readable without surrounding context." |
| C-15 | **PASS** | Delta [D] in Part 1 before narrative. Structural gate: "⬇ GATE — Part 2 begins only after all six analytic outputs above are complete ⬇" |
| C-16 | **PASS** | Beat 5 item 1: posture restatement. |
| C-17 | **PASS** | Beat 5 item 2: bridge sentence independent of [F]. |
| C-18 | **PASS** | Explicit named gate line: "⬇ GATE — Part 2 begins only after all six analytic outputs above are complete ⬇" — the clearest structural gate of any variation. |
| C-19 | **PASS** | Per-artifact non-substitution at every placement point. E.g., Pattern [C]: "The placement here does not satisfy Beat 3. Beat 3 must restate it independently." Bridge [F]: "The placement here does not satisfy Beat 5. Beat 5 must include it independently." Posture [B]: "The placement here does not satisfy Beat 5. Beat 5 must state posture independently." Strongest per-artifact C-19 coverage of all variations. |
| C-20 | **PASS** | Per-artifact consistency statements. Pattern [C]: "If Beat 3 pattern differs from this, the output is inconsistent. (C-20)" Bridge [F]: "If Beat 5 bridge sentence differs from this, the output is inconsistent. (C-20)" |

**Aspirational: 13/13**

### Score

```
composite = (4/4 × 60) + (2/3 × 30) + (13/13 × 10)
          = 60 + 20 + 10
          = 90
```

**All essential pass. Composite: 90. Status: GOLDEN.**

**V-03 differentiator vs V-01/V-02**: Non-substitution is stated *per artifact at the point of first production* — not globally and not just in a rules section. Each artifact carries its own "this does not satisfy the later requirement" statement. V-03's gate line ("⬇ GATE ⬇") is also the most explicit structural separator.

---

## V-04 — Role Sequence + Phrasing Register (conversational directive)

**Axis**: Role sequence + phrasing register — same three-role sequence in directive conversational language with explicit sanity check.

### Essential Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "Lead with the recommendation — do not build toward it. A story that saves the recommendation for the end fails." |
| C-02 | **PASS** | Five beats with required labels. |
| C-03 | **PASS** | Beat 3 opens with pattern sentence; cross-signal requirement in Step 2. |
| C-04 | **PASS** | "What the signals show TOGETHER that no single signal shows alone." |

**Essential: 4/4**

### Recommended Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-05 | **PASS** | "You need at least three distinct namespaces." |
| C-06 | **PASS** | Beat 4: "If X turns out to be Y, this moves from [verb] to [alternate verb]." |
| C-07 | **PASS** | Step 3 Sanity Check explicitly states: "Does your verb match your posture? **Strong positive → proceed. Mixed → pause. Conflicting → pivot. Weak or negative → abandon.** If the verb and posture don't match, fix one of them." This is the first variation with an explicit calibration mapping. |

**Recommended: 3/3** ← KEY DIFFERENTIATOR

### Aspirational Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Three-stage structure with arc. |
| C-09 | **PASS** | Delta in Step 2 and Beat 2. |
| C-10 | **PASS** | "Write this sentence: `The pattern: [...]`" in Step 2 (pre-composition). |
| C-11 | **PASS** | Beat 5 bridge sentence required. |
| C-12 | **PASS** | Beat 4 direction-specific. |
| C-13 | **PASS** | Beat 5: "Name who is deciding and under what constraint. Write it as a decision, not a finding." |
| C-14 | **PASS** | "The sentence has to stand on its own. If it only makes sense after reading the story around it, rewrite it." |
| C-15 | **PASS** | Delta identified in Stage 1 before Stage 2. |
| C-16 | **PASS** | Beat 5: posture-verb formula required. |
| C-17 | **PASS** | Beat 5: bridge sentence required. |
| C-18 | **PASS** | Stage 1 / Stage 2 structural separation; conversational gate: "Don't start Stage 2 until Stage 1 is done." (Note: the prompt contains a copy-paste error — "Don't start Stage 2 until Stage 2 is done" — but intent and structural separation are clear.) |
| C-19 | **PARTIAL** | Non-substitution stated for Pattern, Delta, and Bridge: "Writing it here does not satisfy that requirement." But posture uses softer language: "You'll need to state this again in your recommendation" — does not explicitly say "prior placement does not satisfy Beat 5." Gap: posture non-substitution is incomplete. |
| C-20 | **PARTIAL** | Posture match enforced via Step 3 sanity check: "The two statements must match." Beat 5 posture-verb formula is required. But the explicit "inconsistency between two placements is structurally visible" framing of C-20 is absent. Multi-stage consistency is instructionally implied rather than structurally stated. |

**Aspirational: 11/13 (C-19 PARTIAL → FAIL, C-20 PARTIAL → FAIL)**

### Score

```
composite = (4/4 × 60) + (3/3 × 30) + (11/13 × 10)
          = 60 + 30 + 8.46
          ≈ 98
```

**All essential pass. Composite: 98. Status: GOLDEN.**

---

## V-05 — Output Format + Inertia Framing (table + status-quo competitor)

**Axis**: Output format + inertia framing — pre-composition table with status-quo default row forcing counterfactual defeat, plus active consistency checkpoint.

### Essential Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "The story opens with the recommendation. It does not build toward the recommendation. A story that saves the recommendation for a final section fails." |
| C-02 | **PASS** | Five beats with required labels. |
| C-03 | **PASS** | Row 4 pattern as cross-signal claim; Beat 3 opens with labeled statement. |
| C-04 | **PASS** | "one self-contained sentence — relationship, tension, or gap that no single signal shows alone." |

**Essential: 4/4**

### Recommended Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-05 | **PASS** | Row 1: "Min 3 distinct namespaces." |
| C-06 | **PASS** | Beat 4: direction-specific uncertainty required. |
| C-07 | **PASS** | "Verb-posture calibration (C-07): Row 7 must follow from row 2. Strong positive → proceed. Mixed → pause. Conflicting → pivot. Weak or negative → abandon. A verb that contradicts the posture fails." — Explicitly labeled with the criterion ID, full mapping, and failure condition. Strongest C-07 enforcement of any variation. |

**Recommended: 3/3**

### Aspirational Criteria

| ID | Rating | Evidence |
|----|--------|----------|
| C-08 | **PASS** | Table + five-beat arc enforced. |
| C-09 | **PASS** | Delta row 5; Beat 2 requires explicit stated contrast, independent of table. |
| C-10 | **PASS** | Pattern row 4; Beat 3 opens with "The pattern: [sentence]" as discrete labeled statement. |
| C-11 | **PASS** | Bridge row 8; Beat 5 item 2 requires it. |
| C-12 | **PASS** | Beat 4 direction-specific. |
| C-13 | **PASS** | Beat 5 contains *two* elements for C-13: (3) Inertia displacement — "Without this evidence, the team would [default]. The signals change this because [specific reason]" — and (4) Decision-grounded close — "A [role] deciding [question] under [constraint] should [action]." Strongest C-13 enforcement of any variation. |
| C-14 | **PASS** | Beat 3: "Do not embed the pattern in flowing prose." Discrete labeled statement required. |
| C-15 | **PASS** | Delta in table (Part 1) before narrative. |
| C-16 | **PASS** | Beat 5 item 1: posture statement required. |
| C-17 | **PASS** | Beat 5 item 2: bridge sentence required, must match rows 4 and 7. |
| C-18 | **PASS** | Named Part 1 / Part 2 separator. Table format makes pre-composition structurally verifiable. |
| C-19 | **PASS** | "Non-substitution (C-19): Each artifact in the table is required at its designated beat in Part 2. The table is an analytic record — not a reusable source. Citing the table does not satisfy a beat-level placement. Each beat placement must be independently stated." Beat 5 header reinforces: "Must contain all five elements below. Each is independent of the table. (C-19)" |
| C-20 | **PASS** | Two-layer enforcement: (a) "Multi-stage consistency (C-20): Rows 2, 4, 7, and 8 appear in both the table and in designated beats. If the content differs between the table and the beat, the output is inconsistent." (b) Beat 5 item 5: "Consistency checkpoint (C-20): After writing this beat, confirm that posture, pattern, and bridge sentence in this beat match rows 2, 4, and 8 respectively. If any differ, **return to the table and reconcile before submitting.**" — The only variation with an active remediation instruction, not merely visibility. |

**Aspirational: 13/13**

### Score

```
composite = (4/4 × 60) + (3/3 × 30) + (13/13 × 10)
          = 60 + 30 + 10
          = 100
```

**All essential pass. Composite: 100. Status: EXEMPLARY.**

---

## Scorecard Summary

| Variation | Axis | Essential | Recommended | Aspirational | Composite | Status |
|-----------|------|-----------|-------------|--------------|-----------|--------|
| V-01 | Role sequence | 4/4 | 2/3 | 13/13 | 90 | GOLDEN |
| V-02 | Output format (table) | 4/4 | 2/3 | 13/13 | 90 | GOLDEN |
| V-03 | Lifecycle (per-placement gate) | 4/4 | 2/3 | 13/13 | 90 | GOLDEN |
| V-04 | Role seq + phrasing register | 4/4 | 3/3 | 11/13 | 98 | GOLDEN |
| V-05 | Output format + inertia framing | 4/4 | 3/3 | 13/13 | **100** | EXEMPLARY |

**Top score: 100 (V-05). All variations essential-pass.**

---

## Ranking

1. **V-05** (100) — Explicit calibration mapping, active consistency checkpoint, inertia displacement element
2. **V-04** (98) — First variation to pass C-07 via sanity check; C-19/C-20 partial
3. **V-01** (90) — Strongest role-sequence enforcement; C-07 gap
4. **V-02** (90) — Strongest visual non-substitution (scannable "Required Again In" column); C-07 gap
5. **V-03** (90) — Strongest per-artifact non-substitution statements and clearest gate line; C-07 gap

---

## Excellence Signals from V-05

**Signal 1 — Verb-posture calibration as a named table rule with labeled criterion reference**

V-01 through V-03 omit the explicit posture-to-verb mapping entirely. V-04 introduces it as a sanity check step. V-05 promotes it to a formally labeled table rule with the criterion ID ("Verb-posture calibration (C-07)"), the full four-way mapping, and an explicit failure condition. This structural elevation — from sanity check to named rule — closes C-07 without ambiguity and makes the calibration impossible to miss or skip. The pattern: *when a proportionality rule must be enforced, state the full mapping table (posture → verb), label it with the criterion it addresses, and place it in the rules section rather than in a mid-sequence check.*

**Signal 2 — Active consistency remediation checkpoint as a numbered beat element**

C-20 requires critical claims to appear at multiple positions such that inconsistency is self-revealing. V-01 through V-03 satisfy this via structural visibility (claims appear in two places; mismatch is visible). V-04 handles it instructionally. V-05 goes further: Beat 5 item 5 is a numbered element that actively instructs: "confirm that posture, pattern, and bridge sentence in this beat match rows 2, 4, and 8 respectively. If any differ, return to the table and reconcile before submitting." This transforms consistency enforcement from passive detection (C-20's "self-revealing") to active remediation (model is explicitly told to check and fix before submission). No existing criterion requires this. The pattern: *the recommendation beat should include a numbered verification step that instructs the model to compare its claims against the pre-composition record and correct mismatches — not merely expose them.*

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Verb-posture calibration as a named table rule: explicitly mapping posture labels to recommendation verbs (strong positive → proceed, mixed → pause, conflicting → pivot, weak/negative → abandon) with criterion reference and failure condition in the rules section — not as a mid-sequence sanity check — closes C-07 without ambiguity and cannot be skipped", "Active consistency remediation checkpoint as a numbered beat element: Beat 5 includes an explicit numbered instruction to compare posture, pattern, and bridge sentence against the pre-composition record and reconcile before submitting — transforms C-20 structural visibility into active correction, closing the gap where inconsistency is visible but not resolved"]}
```
