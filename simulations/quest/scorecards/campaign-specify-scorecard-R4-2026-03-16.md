Now I have everything needed. Let me score.

---

# Quest Score — campaign-specify / Round 4

## Scoring Framework

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/12 × 10)
```

PARTIAL = criterion structurally present but form is weaker than required; counts as 0 in pass tally.

---

## Variation Scorecards

### V-01 — Stability Trajectory (C-17 target)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-01 | PASS | Three artifacts produced: spec, proposal, pitch — all phases write to disk |
| C-02 | PASS | All six sections named explicitly; "Do not skip or merge" instruction |
| C-03 | PASS | Three options minimum; Option 1 must be named Do Nothing; description/pros/cons/risk/effort + recommendation |
| C-04 | PASS | Exec, Dev, Maker versions + Anti-Positioning as separate section |
| C-05 | PASS | Step 0a inertia costs flow through User Problem (spec), Do Nothing defeat (proposal), and pitch openings — consistent by threading |
| C-06 | PASS | "At least one named gap. 'No gaps found' fails this section." |
| C-07 | PASS | Anti-Positioning: "3-5 'This is not...' statements. Separate from the three audience versions above." |
| C-08 | PASS | "Defeating [other option]" requires "specific trade-off or risk from the options analysis above — traceable to a specific field in the options, not a preference statement." |
| C-09 | PASS | Step 0d globs `scout/**/*.md`; Phases 1–3 each have distinct targeted pulls |
| C-10 | PASS | Each pitch version has a distinct structural hook rooted in Step 0a inertia cost; exec=risk, dev=friction, maker=blocked step |
| C-11 | PASS | Completion Check: "If any artifact is missing: write it now before stopping." Active recovery instruction, not passive warning |
| C-12 | PASS | Phase 0 (Steps 0a–0d including Step 0c voice contracts) must complete before Phase 1 begins |
| C-13 | PASS | Phase 1 pulls `scout/` broadly; Phase 2 targets `scout-feasibility/`; Phase 3 targets `scout-positioning/` |
| C-14 | PASS | Step 0a: "Name a consequence, not a category" / "Name the friction, not the feeling" / "Name the step" — audience-specific concrete cost language |
| C-15 | PASS | Defeating Do Nothing block cites specific Step 0a inertia cost + Step 0b stability + "We choose to build because [why the cost is not acceptable]" |
| C-16 | PASS | `**Defeating Do Nothing**` appears on its own line as a standalone bold header — dedicated block, structurally separate from `**Defeating [other option]**` paragraph |
| C-17 | PASS | Step 0b: named stability assessment with required form ("Do Nothing is not stable: [rationale]" or "Do Nothing is stable..."); Phase 2 defeat block requires "cite the Step 0b stability assessment verbatim"; Completion Check confirms citation. Two-location requirement satisfied by construction |
| C-18 | PASS | "Do not advance to Step 0b until all three inertia costs are complete" + "Do not advance to Step 0c until the stability assessment is complete" — two explicit intra-Phase 0 advancement gates |
| C-19 | FAIL | End-of-skill Completion Check covers all three artifacts at once — not inline gates collocated at production points. Satisfies C-11, not C-19 |
| C-20 | FAIL | No voice differentiation check before saving pitch file |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 10/12

```
composite = (5/5 × 60) + (3/3 × 30) + (10/12 × 10) = 60 + 30 + 8.33 = 98.3
```

---

### V-02 — Per-Artifact Inline Write Gates (C-19 target)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-01 | PASS | Three phases, three artifacts, three write gates each confirming file exists |
| C-02 | PASS | All six sections listed; "Do not skip or merge" instruction |
| C-03 | PASS | Three options minimum, Do Nothing as Option 1, full fields + recommendation |
| C-04 | PASS | Exec/Dev/Maker versions + Anti-Positioning section |
| C-05 | PASS | Step 0a inertia costs thread through spec (User Problem), proposal (Do Nothing defeat), pitch (opening hooks) |
| C-06 | PASS | "'No gaps found' fails." |
| C-07 | PASS | Anti-Positioning: "3-5 'This is not...' statements. Separate from the three audience versions." |
| C-08 | PASS | "Defeating [other option]" requires trade-off traceable to risk/effort in options analysis |
| C-09 | PASS | Step 0d scout glob; per-phase targeted pulls |
| C-10 | PASS | Each pitch version led by audience-specific inertia cost hook from Step 0a |
| C-11 | PASS | Each write gate: "write it again now" — active recovery, not passive warning. Completion Index adds confirmation |
| C-12 | PASS | Voice contracts in Step 0b; Phase 0 precedes Phase 1 |
| C-13 | PASS | Phase 1 broad, Phase 2 feasibility, Phase 3 positioning — per-phase namespace targeting |
| C-14 | PASS | Step 0a requires specific consequences per audience: "Name it" / "the actual manual operation" / "the exact missing capability" |
| C-15 | PASS | "Do Nothing must be named and defeated by a specific cost. Implicit defeat fails." — named + specific |
| C-16 | FAIL | `**Defeating Do Nothing**: Do Nothing perpetuates [...]` — bold+colon inline label, content on same line as label. This is inline defeat language, not a dedicated structural block. Criterion requires block to be "independently traceable by label" via a dedicated header — not a labeled paragraph opening |
| C-17 | FAIL | Step 0c produces a one-word tag ("stable" \| "worsening") + mechanism. Phase 2 asks for "one sentence on stability from Step 0c" — not a verbatim cite of a named assessment. Two-location requirement is technically present but the Phase 0 output is not a citeable statement; it's a tag. Compare V-01's Form A/Form B which produces the exact citation text |
| C-18 | PASS | "Do not advance to Step 0b until all three costs are named" — at least one explicit intra-Phase 0 gate |
| C-19 | PASS | Three `>> PHASE N WRITE GATE <<` blocks, each collocated with the artifact production instruction, each with "Do not begin Phase N+1 until [file] exists on disk" — gate fires at point of production, not end-of-skill |
| C-20 | FAIL | Phase 3 write gate checks existence but no voice differentiation extraction or conditional rewrite trigger before saving |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 9/12

```
composite = (5/5 × 60) + (3/3 × 30) + (9/12 × 10) = 60 + 30 + 7.5 = 97.5
```

---

### V-03 — Voice Differentiation Save Gate (C-20 target)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-01 | PASS | Three phases, three artifacts |
| C-02 | PASS | All six sections; "No gaps found" fails |
| C-03 | PASS | Three options, Do Nothing as Option 1, full fields + recommendation |
| C-04 | PASS | Exec/Dev/Maker + Anti-Positioning separate section |
| C-05 | PASS | Step 0a costs thread through all three artifacts |
| C-06 | PASS | "'No gaps found' fails." |
| C-07 | PASS | Anti-Positioning: explicit and separate |
| C-08 | PASS | "Defeating [other option]" requires specific options-analysis-traceable trade-off |
| C-09 | PASS | Step 0d glob; Phase 1 broad, Phase 2 feasibility, Phase 3 positioning |
| C-10 | PASS | Distinct hook structures per audience; voice contracts in Step 0b anchor each |
| C-11 | PASS | Completion Check: "write now" active recovery per artifact |
| C-12 | PASS | Voice contracts in Step 0b, Phase 0 precedes Phase 1 |
| C-13 | PASS | Per-phase namespace targeting |
| C-14 | PASS | Step 0a: "Concrete and specific. Name it." for each audience |
| C-15 | PASS | "Defeating Do Nothing" block cites specific Step 0a cost + stability + rationale |
| C-16 | FAIL | `**Defeating Do Nothing**: Do Nothing perpetuates [...]` — same bold+colon inline format as V-02. Label is not a dedicated structural block with its own header line |
| C-17 | FAIL | Step 0c has "stable \| worsening -- name mechanism if worsening." Phase 2 asks for "one sentence on stability from Step 0c." Same weakness as V-02 — one-word tag without the named-form output needed for a verbatim citation. The Phase 2 reference does not cite a named assessment statement |
| C-18 | PASS | "Do not advance to Step 0b until all three inertia costs are named" — explicit intra-Phase 0 gate |
| C-19 | FAIL | Phases 1 and 2 have "Save to:" with path only — no `>> WRITE GATE <<` blocking instruction collocated at production. Phase 3 has a conditional save after voice gate, but C-19 requires all three artifacts to have inline gates |
| C-20 | PASS | `>> VOICE DIFFERENTIATION CHECK (required before saving) <<` fires before save; extracts opening sentences side-by-side; conditional trigger: "If YES: Rewrite the duplicated version(s) until all three openings are detectably distinct... Do not save the pitch until all three openings are distinct." Both check and rewrite condition present; save follows gate pass |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 9/12

```
composite = (5/5 × 60) + (3/3 × 30) + (9/12 × 10) = 60 + 30 + 7.5 = 97.5
```

---

### V-04 — Combined: Stability + Inline Gates + Named Block (C-16, C-17, C-18, C-19 targets)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-01 | PASS | Three phases, three inline write gates, three artifacts |
| C-02 | PASS | Six sections; "no skipping, no merging" |
| C-03 | PASS | Three options, Do Nothing as Option 1, full fields + recommendation |
| C-04 | PASS | Exec/Dev/Maker + Anti-Positioning separate section |
| C-05 | PASS | Step 0a inertia costs flow through all three artifacts; Step 0e pre-compiles for Phase 2 reference |
| C-06 | PASS | Self-review with named gap; "No gaps found fails." |
| C-07 | PASS | Anti-Positioning: explicit and separate |
| C-08 | PASS | "Defeating [Other Option]" block requires trade-off traceable to specific options-analysis field |
| C-09 | PASS | Step 0d glob with per-artifact routing; Phase-targeted re-queries |
| C-10 | PASS | Voice contracts in Step 0c; distinct structural openings per pitch version |
| C-11 | PASS | Each write gate: "Check: does the file exist? If not: write it now" — active recovery |
| C-12 | PASS | Five-step Phase 0 (including Step 0c voice contracts) precedes Phase 1 |
| C-13 | PASS | Phase 1 broad, Phase 2 feasibility, Phase 3 positioning |
| C-14 | PASS | Step 0a requires "Specific revenue exposure... Name the consequence" / "specific workaround or capability gap. Name the friction, not the feeling." / "Specific blocked workflow step. Name the step." |
| C-15 | PASS | Defeating Do Nothing block: specific Step 0a cost + Step 0b stability verbatim cite + "We choose to act because" |
| C-16 | PASS | `#### Defeating Do Nothing` as its own header, structurally separate from `#### Defeating [Other Option Name]`; explicit disqualification: "A combined recommendation paragraph that defeats all options in prose does not satisfy C-16." |
| C-17 | PASS | Step 0b: Form A/Form B named output with "a stability assessment without a mechanism or timeline fails C-17." Step 0e copies it verbatim. Phase 2: "Paste the Step 0b stability assessment verbatim: paste the assessment from Step 0b here." Completion Index item 7 confirms citation occurred |
| C-18 | PASS | Three intra-Phase 0 gates: "Do not advance to Step 0b" / "Do not advance to Step 0c" / "Do not advance to Step 0d" — all explicit blocking language |
| C-19 | PASS | `>> SPEC WRITE GATE <<`, `>> PROPOSAL WRITE GATE <<`, `>> PITCH WRITE GATE <<` — each collocated with the production instruction, each with "Do not begin Phase N+1 until file exists." Three gates, each at production point |
| C-20 | FAIL | Pitch openings are anchored to Step 0a costs and voice contracts, which structurally differentiates them, but no explicit voice differentiation extraction check + conditional rewrite trigger fires before the pitch is saved |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 11/12

```
composite = (5/5 × 60) + (3/3 × 30) + (11/12 × 10) = 60 + 30 + 9.17 = 99.2
```

---

### V-05 — Full Synthesis: All Five New Criteria (C-16 + C-17 + C-18 + C-19 + C-20)

| ID | Pass? | Evidence |
|----|-------|----------|
| C-01 | PASS | Three phases, three inline write gates, Completion Index confirms all three exist |
| C-02 | PASS | Six sections named; "Do not skip or merge any section." |
| C-03 | PASS | Three options minimum; Option 1 MUST be named Do Nothing; all fields + recommendation |
| C-04 | PASS | Exec/Dev/Maker versions + Anti-Positioning as separate named section |
| C-05 | PASS | Step 0a costs flow into spec (User Problem), proposal (Step 0e pre-compile → Defeating Do Nothing), pitch (voice contract anchors) — consistent by threading; Step 0e eliminates reconstructed-vs-established drift |
| C-06 | PASS | "Which section needs more work and why? 'No gaps found' fails this section." |
| C-07 | PASS | Anti-Positioning: "3-5 'This is not...' statements. This section is structurally separate from the three audience versions above." |
| C-08 | PASS | "Defeating [Other Option]" block requires "specific trade-off traceable to a risk, effort, or cons field in the options analysis — not a preference statement." |
| C-09 | PASS | Step 0d with per-artifact signal routing; Phase 1 pulls scout/ broadly, Phase 2 targets scout-feasibility/, Phase 3 targets scout-positioning/ |
| C-10 | PASS | Voice contracts (Step 0c) anchor pitch openings; voice differentiation gate verifies distinct frames before save; each version has "Do not open with..." counter-instruction |
| C-11 | PASS | Each write gate: "If the file does not exist: write it now before continuing." Active recovery instruction; Completion Index confirms artifacts exist |
| C-12 | PASS | Five-step Phase 0 (Steps 0a–0e including Step 0c voice contracts) precedes Phase 1; voice contracts defined at Step 0c, before spec draft |
| C-13 | PASS | Step 0d → Phase 1 broad → Phase 2 scout-feasibility → Phase 3 scout-positioning; per-phase namespace targeting, not a single orchestration-start glob |
| C-14 | PASS | Step 0a: "Quantify if possible ('$X quarterly' or 'N%')"; dev: "Estimate the recurring cost if possible ('3-5 hours per sprint')"; maker: "What does the maker do today instead, and why is that worse?" — most specific inertia cost instructions across all variations |
| C-15 | PASS | Defeating Do Nothing: names Do Nothing, cites specific Step 0a cost, pastes stability, "We choose to act because [one sentence: why this cost is not acceptable given the trajectory]" — required form fully specified |
| C-16 | PASS | `#### Defeating Do Nothing` header structurally separate from `#### Defeating [Other Option Name]`; explicit disqualification: "A recommendation paragraph that combines Do Nothing defeat with other comparisons in prose does not satisfy C-16 or C-17." |
| C-17 | PASS | Step 0b: Form A ("Do Nothing is not stable: [specific mechanism and timeline]") or Form B ("Do Nothing is stable: [rationale]") — named forms produce complete citeable sentences. Step 0e compiles stability verbatim. Phase 2 requires "Paste the Step 0e stability line here verbatim." Note on structure: "The Step 0e stability line must appear verbatim inside that block." Completion Index item confirms citation. Strongest two-location enforcement of any variation |
| C-18 | PASS | "Do not advance to Step 0b until all three inertia costs are complete" + "Do not advance to Step 0c until the stability assessment is complete" + "Do not advance to Step 0d until all three voice contracts are written" — three explicit advancement gates between Phase 0 internal steps |
| C-19 | PASS | `>> SPEC WRITE GATE <<` after Phase 1, `>> PROPOSAL WRITE GATE <<` after Phase 2, `>> PITCH WRITE GATE <<` after Phase 3 (after voice gate). Each collocated with production instruction; each has "Do not begin Phase N+1 until [file] is on disk." Structurally distinct from the Completion Index table |
| C-20 | PASS | `>> VOICE DIFFERENTIATION GATE (required before saving pitch) <<` fires before `>> PITCH WRITE GATE <<`; extracts opening sentences per audience; specifies expected patterns ("Exec opens with: a business cost... Dev opens with: a tool friction... Maker opens with: a workflow step"); conditional trigger: "IF any two openings are the same or use the same frame: Rewrite the duplicated version(s)... Re-run this check after rewriting. Do not save the pitch until all three opening frames are distinct." Both check and rewrite condition present; save is collocated after the gate passes |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 12/12

```
composite = (5/5 × 60) + (3/3 × 30) + (12/12 × 10) = 60 + 30 + 10 = 100.0
```

---

## Leaderboard

| Rank | Variation | Essential | Rec | Asp | Composite | New criteria earned |
|------|-----------|-----------|-----|-----|-----------|---------------------|
| 1 | V-05 | 5/5 | 3/3 | 12/12 | **100.0** | C-16, C-17, C-18, C-19, C-20 |
| 2 | V-04 | 5/5 | 3/3 | 11/12 | **99.2** | C-16, C-17, C-18, C-19 |
| 3 | V-01 | 5/5 | 3/3 | 10/12 | **98.3** | C-16, C-17, C-18 |
| 4= | V-02 | 5/5 | 3/3 | 9/12 | **97.5** | C-18, C-19 |
| 4= | V-03 | 5/5 | 3/3 | 9/12 | **97.5** | C-18, C-20 |

**C-16 gap**: V-02 and V-03 use bold+colon inline labels (`**Defeating Do Nothing**: content...`) — the label opens the paragraph but is not a standalone structural header. C-16 requires the block to be independently traceable, which requires the label to be its own line or header. V-01's standalone bold line and V-04/V-05's `####` headers satisfy this; inline-labeled paragraphs do not.

**C-17 gap**: V-02 and V-03 Step 0c produces a one-word tag ("stable \| worsening") with a short mechanism. Phase 2 asks for "one sentence on stability from Step 0c" — a reference instruction, not a verbatim-cite instruction. The Phase 0 output is not a named assessment statement; it has no citeable form. Compare V-01/V-04/V-05 which produce a complete sentence via Form A/Form B that can be pasted verbatim.

---

## Excellence Signals from V-05

**Five independent enforcement mechanisms at five different structural locations:**

1. **Form A / Form B named output structure for Phase 0 assessments** — V-05 Step 0b requires the model to choose between two labeled forms and complete a full sentence (e.g., "Do Nothing is not stable: competitor ships equivalent feature in Q2..."). This is stronger than "is it stable? + mechanism" because the form produces the exact citation text. Any Phase 0 output that will be cited by name in a later phase should be structured as a named form — not a free-form answer, not a tag.

2. **Step 0e pre-compilation block** — Before Phase 2 begins, Step 0e copies all Phase 0 outputs (inertia costs, stability assessment) into a single block labeled "Do Nothing Baseline." The Phase 2 defeat block then cites from Step 0e, not from Phase 0 directly. This eliminates backward-reference drift under context pressure: the cite target is collocated with the Phase 2 write instruction, not buried earlier.

3. **Voice gate with specified expected-pattern targets** — The voice differentiation gate in V-05 does not just check for distinctness ("are they different?"). It tells the model what each opening should look like: "Exec opens with: a business cost, risk, or revenue consequence / Dev opens with: a tool friction, workaround, or capability gap / Maker opens with: a workflow step that is blocked, absent, or manual." This makes the conditional rewrite actionable — the model has a target state to rewrite toward, not just a negative constraint.

4. **Completion Index as a self-scoring instrument** — V-05's Completion Index table requires the model to explicitly confirm key execution facts (stability cited: yes/no, voice gate result: distinct/rewritten-to-distinct, named block header: yes/no). This is not a summary — it's an honest disclosure mechanism. A model that cannot fill the table honestly will self-expose the gap before the skill terminates. This pattern generalizes: any skill with multiple criteria can add a Completion Index table with explicit yes/no rows for the hardest criteria.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Form A/Form B named output structure: Phase 0 stability assessment uses a labeled form that produces a complete citeable sentence — any Phase 0 output that will be cited verbatim in a later phase should be structured as a named form, not a free-form answer or one-word tag", "Step 0e pre-compilation block: copying all Phase 0 outputs into a single block immediately before Phase 2 begins eliminates backward-reference drift — the cite target is collocated with the Phase 2 write instruction rather than requiring the model to scan back to Phase 0", "Voice gate with specified expected-pattern targets per audience: the pre-save check names what each opening should look like (exec=business cost, dev=tool friction, maker=blocked workflow step) making the conditional rewrite actionable rather than open-ended", "Completion Index as self-scoring instrument: a table requiring the model to explicitly confirm yes/no for key criterion execution facts — model that cannot fill it honestly self-exposes the gap before the skill terminates"]}
```
