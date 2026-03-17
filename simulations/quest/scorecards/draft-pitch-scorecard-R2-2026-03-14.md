## Round 2 Scorecard — draft-pitch

**Rankings:**

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-03 DEFAULTS TABLE (single axis) | **100** | YES |
| 1 | V-04 Binary gate + DEFAULTS TABLE | **100** | YES |
| 1 | V-05 All axes + audience-sequenced | **100** | YES |
| 4 | V-01 Binary gate (single axis) | **99** | YES |
| 4 | V-02 Fill-in-the-blank (single axis) | **99** | YES |

All five variations Golden. The floor is 99, up from R1's 85.

---

**The discriminator: C-12 only.** C-10 and C-11 pass in all five variations using different structural forms. The 1-point gap is entirely from C-12: unconditional DEFAULTS TABLE (score 100) vs. conditional fallback inside Signal Intake (score 99, PARTIAL C-12). No other criterion separates the field.

**Criterion heatmap:** C-01 through C-11 pass universally. Only C-12 varies.

**V-03 surprise:** Predicted ~98, scored 100. The prediction assumed narrative C-10 and Q&A C-11 would not pass. Under the actual rubric pass conditions they do — both forms satisfy "write, test, rewrite *before* continuing." The criteria are form-agnostic: they test when the check happens, not which structural form implements it.

---

**Excellence signals from the top group:**

- **Unconditional DEFAULTS TABLE is the minimum structural change for full score** — V-03 adds only one element and reaches 100, proving the table is sufficient without binary gates or templates elsewhere
- **Binary Y/N gate creates an unbypassable forward reference** — naming the output "EXEC OPENING SENTENCE" and citing that name in Step 4's hook instruction makes skipping the gate a broken reference, not just a skipped instruction
- **Audience belief mapping (V-05 Step 2) is a new structural pattern** — "what must each audience believe first?" anchors each version in reader psychology before argument construction; no R1 analog

**Recommended golden:** V-05 (strongest form on every axis). V-04 as the minimum-complexity alternative (same score, 6 steps vs. 7). V-03 as the minimum-change upgrade path from an existing R1 skill.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Unconditional DEFAULTS TABLE alone achieves full score: a single-axis variation (V-03) that only adds the defaults table reaches 100, proving unconditional top-level loading is the minimum structural change for C-12 — narrative C-10 and Q&A C-11 both satisfy their rubric pass conditions without requiring binary gates or templates", "Binary Y/N gate creates unbypassable forward reference: naming the output EXEC OPENING SENTENCE and referencing that name in Step 4's hook instruction makes the gate step mechanically dependent — skipping the gate breaks the downstream reference, stronger than narrative write-test-rewrite which can be summarized in prose", "Audience belief mapping before drafting: answering 'what must each audience believe first?' before any pitch prose begins anchors each version in reader psychology rather than structural compliance, producing more persuasive output at the same quality ceiling — new pattern with no R1 analog"]}
```
answers are locked inputs for Step 4." Written outputs before any pitch content. |
| C-12 | Default fallback values provided | PARTIAL | Explicit defaults provided in Step 1 conditional branch ("If no prior signals: set Primary Competitor = ..."). Covers Primary Competitor, Outcome, Ruling Out — but conditional. Not loaded before intake. Intake-step misread can bypass. |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 4.5/5

```
composite = (4/4 * 60) + (3/3 * 30) + (4.5/5 * 10)
          = 60 + 30 + 9
          = 99
```

**Score: 99 / 100 -- GOLDEN**

---

## V-02 — Fill-in-the-Blank Templates (Single Axis: C-11)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Step 4 writes Exec, Dev, Maker with labeled sections. |
| C-02 | Each version has all four elements | PASS | Hook, What It Does, Why It Matters, Call to Action explicitly stated for all three versions. |
| C-03 | Exec version is outcome-first | PASS | Step 3: write exec opening, read it back, "if it opens with a feature or tool description, rewrite it using the cost/consequence from Template A. Continue only once the opening names a business consequence." Embedded before Step 4. |
| C-04 | Anti-positioning section present | PASS | Step 5: "## What Signal Is NOT" from Templates D and E plus additional bullet. Format enforced. |
| C-05 | Dev version shows the tool | PASS | "Show a command, artifact name, or specific workflow step. Format example: /scout:requirements topic={topic} produces {topic}-requirements-{date}.md. Reader answers 'what would I type?'" |
| C-06 | Maker version is jargon-free | PASS | "No acronyms. No tool names. No CLI references." Explicit. |
| C-07 | Prior signals consulted | PASS | Step 1 checks two signal paths, lists files found or "No prior signals." |
| C-08 | Proof points traceable | PASS | Step 6: [source: artifact-path], [source: prior signal], or [UNVERIFIED -- hedge before delivery]. "Remove or hedge all UNVERIFIED claims before saving." |
| C-09 | Inertia named as primary competitor | PASS | Template C: "The real competition is not Cursor, Copilot, or any named tool. It is ___." Default for Template C: "the meeting that never happened, the spec review that came after the build, the go/no-go that no one called." |
| C-10 | Exec self-check embedded at generation time | PASS | Step 3: write sentence, read it back, rewrite "using the cost/consequence from Template A" if wrong. "Continue only once the opening names a business consequence." Not a post-draft checklist — embedded before Step 4. |
| C-11 | Positioning locked in writing before prose | PASS | Templates A-E are fill-in-the-blank sentence starters. "Do not draft any pitch content until all five templates are filled. Partial answers are not acceptable." Strongest form: partial sentence forces completion — cannot be ambient. |
| C-12 | Default fallback values provided | PARTIAL | Defaults provided for Templates A and C only, conditional ("If no prior signals were found in Step 1, use these defaults to begin your completions"). Templates B, D, E have no explicit defaults. Incomplete field coverage; conditional loading. |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 4.5/5

```
composite = (4/4 * 60) + (3/3 * 30) + (4.5/5 * 10)
          = 60 + 30 + 9
          = 99
```

**Score: 99 / 100 -- GOLDEN**

---

## V-03 — Unconditional DEFAULTS TABLE (Single Axis: C-12)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Step 4 writes Exec, Dev, Maker. |
| C-02 | Each version has all four elements | PASS | Hook, What It Does, Why It Matters, Call to Action for all three versions. |
| C-03 | Exec version is outcome-first | PASS | Step 3: write exec opening sentence, "use the active Inertia cost value as your source," read it back, rewrite if feature/tool-first. "Continue only after the opening passes." |
| C-04 | Anti-positioning section present | PASS | Step 5: "## What Signal Is NOT" from active Ruling Out values. Minimum three bullets. Format enforced. |
| C-05 | Dev version shows the tool | PASS | "Show the interaction. Minimum one concrete example: a command, an artifact name, or a workflow step. Reader answers 'what would I type?'" |
| C-06 | Maker version is jargon-free | PASS | "Zero unexplained acronyms. Zero namespace references." Explicit prohibition. |
| C-07 | Prior signals consulted | PASS | Step 1 checks three signal paths, extracts overrides, produces active values table with Source column. |
| C-08 | Proof points traceable | PASS | Step 6: [source: artifact-path], [source: prior signal], or [UNVERIFIED]; "replace with hedged language or the active Proof fallback value before saving." Proof fallback in DEFAULTS TABLE: "technique experiments across 730+ scenarios." |
| C-09 | Inertia named as primary competitor | PASS | Step 2 Q1: "The real competition is not a named tool. It is [active Primary competitor value]." DEFAULTS TABLE row: "teams doing nothing -- the review that never happened." Active value table in Step 1 writes the final value explicitly. |
| C-10 | Exec self-check embedded at generation time | PASS | Step 3: write opening sentence using active Inertia cost, read it back, "if it opens with a feature or tool description, rewrite it. Continue only after the opening passes." Write-test-rewrite before Step 4. |
| C-11 | Positioning locked in writing before prose | PASS | Step 2: "Answer in writing before any pitch content is drafted." Three complete sentences written. "These are locked inputs." |
| C-12 | Default fallback values provided | PASS | SIGNAL DEFAULTS table at top of skill. Seven fields. Unconditional: "These defaults apply to all runs. Override with scout signal values when available. Use as-is when no scout signals exist." Loaded before intake step — cannot be bypassed by intake-step misread. |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 5/5

```
composite = (4/4 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

> **Surprise finding**: V-03 was predicted at ~98 but scores 100. The prediction assumed narrative C-10 (vs. binary gate) and Q&A C-11 (vs. templates) would not fully pass. Under the actual rubric pass conditions, both narrative write-test-rewrite (C-10) and written Q&A answers before prose (C-11) satisfy the criteria. Single-axis unconditional defaults alone is sufficient for a full score.

---

## V-04 — Binary Gate + DEFAULTS TABLE (V-01+V-03 Combined)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Step 4 writes Exec, Dev, Maker. |
| C-02 | Each version has all four elements | PASS | Hook, What It Does, Why It Matters, Call to Action for all three. |
| C-03 | Exec version is outcome-first | PASS | Step 3 EXEC OPENING GATE: binary YES/NO, named output "EXEC OPENING SENTENCE," rewrite instruction uses "active Inertia cost from SIGNAL DEFAULTS as your anchor." |
| C-04 | Anti-positioning section present | PASS | Step 5: "## What Signal Is NOT" from Q3 Ruling Out values. Minimum three bullets. |
| C-05 | Dev version shows the tool | PASS | "Show at least one command, artifact name, or workflow step. Format example: /scout:requirements topic={topic} produces {topic}-requirements-{date}.md. Reader answers 'what would I type?'" |
| C-06 | Maker version is jargon-free | PASS | "No acronyms, no namespace terms, no CLI references." Explicit. |
| C-07 | Prior signals consulted | PASS | Step 1 loads two signal paths, notes which SIGNAL DEFAULTS rows are overridden. |
| C-08 | Proof points traceable | PASS | Step 6: [source: {path}], [source: prior signal], or [UNVERIFIED]; "replace with active Proof fallback value before saving." |
| C-09 | Inertia named as primary competitor | PASS | Q1: "The real competition is not a named tool. It is ___." DEFAULTS TABLE: "teams doing nothing -- the meeting that never happened." Exec Why It Matters: "The alternative is [Q1 answer]. Signal eliminates that cost before the build starts." |
| C-10 | Exec self-check embedded at generation time | PASS | Step 3 binary gate: named output + explicit YES/NO + mandatory rewrite using "active Inertia cost from SIGNAL DEFAULTS" + "EXEC OPENING SENTENCE is now locked." Cannot proceed to Step 4 until YES. |
| C-11 | Positioning locked in writing before prose | PASS | Step 2: three questions answered in writing before any pitch content is drafted. "These are locked -- the draft step cannot override them." |
| C-12 | Default fallback values provided | PASS | SIGNAL DEFAULTS table at top. Six fields. "Always-on. Override with scout values when found. Use as-is when no scout signals exist." Unconditional. |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 5/5

```
composite = (4/4 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

## V-05 — All Three Axes + Audience-Sequenced Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Step 5 writes Exec, Dev, Maker with labeled sections. |
| C-02 | Each version has all four elements | PASS | Hook, What It Does, Why It Matters, Call to Action for each version with explicit requirements. |
| C-03 | Exec version is outcome-first | PASS | Step 4 EXEC OPENING GATE: binary YES/NO, named output, mandatory rewrite using "active Inertia cost from SIGNAL DEFAULTS." Hook is "EXEC OPENING SENTENCE (locked, exact)." |
| C-04 | Anti-positioning section present | PASS | Step 6: "## What Signal Is NOT" from Template 3 completions. Minimum three bullets. Format with topic-specific clarification sentence. |
| C-05 | Dev version shows the tool | PASS | "Show at least one concrete interaction. Example: /scout:requirements topic={topic} produces {topic}-requirements-{date}.md. Describe what comes back and why it matters. Reader answers 'what would I actually type?'" |
| C-06 | Maker version is jargon-free | PASS | "Zero acronyms. Zero namespace references. Zero CLI terminology. If they don't recognize the vocabulary, they stop reading." Strongest maker jargon prohibition in the round. |
| C-07 | Prior signals consulted | PASS | Step 1 checks three signal paths. Notes DEFAULTS row overrides explicitly. |
| C-08 | Proof points traceable | PASS | Step 7: annotate every factual claim. [source: artifact-path], [source: prior signal], or [UNVERIFIED]; "replace with hedged language or active Proof fallback value before saving." |
| C-09 | Inertia named as primary competitor | PASS | Template 4: "The real competition for Signal is not a named product. It is ___. That competitor wins by default when ___." Exec Why It Matters: "The alternative is not a competing tool -- it is [Template 4 answer]." DEFAULTS TABLE default: "teams doing nothing -- the review that never happened." |
| C-10 | Exec self-check embedded at generation time | PASS | Step 4 binary gate: named output "EXEC OPENING SENTENCE" + YES/NO + mandatory rewrite + "EXEC OPENING SENTENCE is locked." Step 5 cannot begin until YES. |
| C-11 | Positioning locked in writing before prose | PASS | Step 3 Templates 1-4: fill-in-the-blank templates. "These are locked inputs." Before any pitch prose begins. Templates structurally require completion -- partial sentences cannot be left partial. Strongest form of C-11. |
| C-12 | Default fallback values provided | PASS | SIGNAL DEFAULTS table at top with 9 fields -- most comprehensive of all variations. Includes audience-specific fields: Dev friction, Maker outcome, Exec outcome. Unconditional. |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 5/5

```
composite = (4/4 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-03 DEFAULTS TABLE only | 4/4 | 3/3 | 5/5 | **100** | YES |
| 1 | V-04 Gate + DEFAULTS TABLE | 4/4 | 3/3 | 5/5 | **100** | YES |
| 1 | V-05 All axes + audience | 4/4 | 3/3 | 5/5 | **100** | YES |
| 4 | V-01 Binary gate only | 4/4 | 3/3 | 4.5/5 | **99** | YES |
| 4 | V-02 Templates only | 4/4 | 3/3 | 4.5/5 | **99** | YES |

**C-12 is the sole discriminator.** All variations pass C-01 through C-11 fully. The 1-point gap between 99 and 100 is entirely attributable to whether defaults are unconditional (DEFAULTS TABLE, score 100) or conditional inside Signal Intake (score 99, PARTIAL C-12).

---

## Criterion Coverage Heatmap (R2)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (3 versions) | PASS | PASS | PASS | PASS | PASS |
| C-02 (4 elements) | PASS | PASS | PASS | PASS | PASS |
| C-03 (outcome-first exec) | PASS | PASS | PASS | PASS | PASS |
| C-04 (anti-positioning) | PASS | PASS | PASS | PASS | PASS |
| C-05 (dev shows tool) | PASS | PASS | PASS | PASS | PASS |
| C-06 (maker jargon-free) | PASS | PASS | PASS | PASS | PASS |
| C-07 (prior signals) | PASS | PASS | PASS | PASS | PASS |
| C-08 (traceable proof) | PASS | PASS | PASS | PASS | PASS |
| C-09 (inertia as competitor) | PASS | PASS | PASS | PASS | PASS |
| C-10 (self-check at generation) | PASS | PASS | PASS | PASS | PASS |
| C-11 (positioning locked) | PASS | PASS | PASS | PASS | PASS |
| C-12 (default fallbacks) | PARTIAL | PARTIAL | PASS | PASS | PASS |

The floor has risen dramatically from R1. C-01 through C-11 pass universally across all five variations. Discrimination reduces to a single point on C-12.

---

## Excellence Signals — Round 2

### E-1: Unconditional DEFAULTS TABLE is the minimum structural change for full score

V-03 adds only ONE new structural element — the DEFAULTS TABLE at the top — and scores 100. The narrative write-test-rewrite (C-10) and Q&A written answers before prose (C-11) both satisfy their rubric pass conditions without requiring binary gates or templates. This means: the DEFAULTS TABLE is the minimum, least-complex addition that achieves full aspirational coverage. **Pattern: unconditional loading before intake removes the last conditional failure mode without requiring additional structural complexity elsewhere.**

### E-2: Binary Y/N gate enforces C-10 more mechanically than narrative, but both pass

V-01/V-04/V-05 use a binary gate that produces a named isolated output ("EXEC OPENING SENTENCE") and requires an explicit YES/NO answer before proceeding. V-02/V-03 use narrative write-test-rewrite ("read it back... if it opens with a feature, rewrite it"). Both forms pass C-10. The binary gate form is stronger because the model produces a named artifact that downstream steps reference by name — creating a dependency the model cannot skip. **Pattern: named outputs create forward references that make steps mechanically dependent; a model that skips the gate produces a broken reference in Step 4's "use EXEC OPENING SENTENCE exactly."**

### E-3: Audience belief mapping adds persuasive depth at no structural cost

V-05 Step 2 asks: "What is the first thing this person needs to believe before they can be moved by any other argument?" This question is answered for exec, dev, and maker before any pitch prose begins. These answers anchor each version in reader psychology rather than structural compliance — "Lead to that belief, then through it." The quality ceiling is higher, but the rubric score is the same 100. **Pattern: belief-anchored drafting produces pitch content that feels crafted rather than templated; the audience-first question functions as an intent declaration before writing begins.**

### E-4: Audience-specific default fields close a cold-start gap for dev and maker versions

V-05's DEFAULTS TABLE includes "Dev friction" and "Maker outcome" fields that V-03/V-04 do not. These fields supply cold-start-safe framing for all three pitch versions, not just the exec. V-03/V-04 have exec-focused defaults; V-05 provides defaults per audience. **Pattern: scoping defaults to each output audience ensures C-12 applies equally across all three versions, not just the exec section where C-09 is scored.**

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate at equal score to V-03 and V-04 because:
- All 12 criteria pass fully
- Strongest C-11 form (fill-in-the-blank templates)
- Most comprehensive DEFAULTS TABLE (9 fields including audience-specific)
- Strongest C-06 floor (most explicit maker jargon prohibition)
- Audience belief mapping (Step 2) produces highest-quality output framing
- Proof fallback in DEFAULTS TABLE linked to traceable path (simulations/techniques/)

**V-04** is the complexity-minimizing alternative: binary gate + DEFAULTS TABLE achieves 100 with fewer total steps (6) than V-05 (7) and no audience mapping overhead. Best for teams that want full score with lower prompt token cost.

**V-03** is the minimum viable change for full score: single unconditional DEFAULTS TABLE addition to any R1-quality skill. Best as an upgrade path from existing V-05 R1 variant.

---

## Round 2 Findings

### F-01: All five variations achieve Golden — R2 floor is 99, up from R1's 85

The v2 rubric's additional aspirational criteria (C-10/C-11/C-12) do not break any variation. All five pass all 4 essential criteria, all 3 recommended criteria, and at minimum 4.5/5 aspirational criteria. The floor has risen 14 points vs. R1.

### F-02: C-12 is the sole discriminator in R2

C-10 and C-11 are satisfied by all five variations using different structural forms (binary gate, narrative, templates). Only C-12 separates the field: unconditional loading (DEFAULTS TABLE) vs. conditional loading (inline fallback).

### F-03: Conditional defaults satisfy C-09 but not C-12

V-01 and V-02 have explicit defaults that ensure C-09 passes. But C-12's "unconditionally" standard requires that defaults be loaded before intake, not triggered by intake result. Conditional defaults satisfy output correctness but not structural enforcement.

### F-04: V-03's 100 contradicts the predicted ~98

The prediction assumed narrative C-10 and Q&A C-11 would not fully pass. Under actual rubric pass conditions they do. This finding suggests the C-10 and C-11 rubric criteria are form-agnostic: they test whether the check is embedded before prose, not which structural form (binary/narrative) implements it.

### F-05: Audience mapping (V-05 Step 2) is a structural pattern not represented in R1

R1's V-05 used strategy passes (S-1 to S-4) to lock competitive framing. R2's V-05 adds a prior step that answers "what must each audience believe first?" This is a distinct structural move: it establishes reader-belief targets before any argument is constructed. No R1 variation included this pattern.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Unconditional DEFAULTS TABLE alone achieves full score: a single-axis variation (V-03) that only adds the defaults table reaches 100, proving unconditional top-level loading is the minimum structural change for C-12 — narrative C-10 and Q&A C-11 both satisfy their rubric pass conditions without requiring binary gates or templates", "Binary Y/N gate creates unbypassable forward reference: naming the output EXEC OPENING SENTENCE and referencing that name in Step 4's hook instruction makes the gate step mechanically dependent — skipping the gate breaks the downstream reference, stronger than narrative write-test-rewrite which can be summarized in prose", "Audience belief mapping before drafting: answering 'what must each audience believe first?' before any pitch prose begins anchors each version in reader psychology rather than structural compliance, producing more persuasive output at the same quality ceiling — new pattern with no R1 analog"]}
```
