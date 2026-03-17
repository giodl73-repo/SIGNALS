**corps-achievements-rubric-v11** written to `simulations/quest/rubrics/corps-achievements-rubric-v11-2026-03-16.md`.

---

### What changed v10 → v11

**Four new criteria** from R11 excellence signals:

**C-31** (from V-01/V-04 C-29 excellence) — **Global retry protocol**. Rather than repeating the correction triad in each gate's fail path, the skill declares a single named preamble-level protocol block that all gates reference. V-02/V-03/V-05 satisfied C-29 with per-gate repetition; V-01/V-04 made the contract architecturally global. Satisfying C-29 at every gate still does not satisfy C-31.

**C-32** (from V-01/V-04 C-29 excellence) — **Delimited retry block output**. When a retry fires, the re-run output is wrapped in explicit labeled delimiters — `> RETRY [C-XX]: … > END RETRY` — so the retry boundary is visible and parseable. The correction triad (C-29) alone does not satisfy this criterion; the output container must be specified.

**C-33** (from V-02/V-04 C-30 excellence) — **Attribution gate as standalone position**. The C-30 backward-inference prohibition must be a structurally independent named gate executing before the leaderboard cluster gate. V-01's inline pre-check (physically before but not a standalone gate) and V-05's sub-step embedding both fail this criterion; V-02 and V-04's `ATTRIBUTION INTEGRITY GATE [C-28/C-30]` satisfies it.

**C-34** (from V-04 C-27 excellence) — **Complete super-gate enumeration in structural audit**. If the skill contains N cluster gates, all N must appear in the structural audit. V-04 verified 4; others verified 2–3. Partial enumeration — even fully accurate — does not satisfy this criterion.

**Scoring**: aspirational pool 22 → 26; each criterion `20/26 ≈ 0.769 pts`. Maximum still 100.
28/C-30]` — executing before the leaderboard cluster gate. V-01's inline pre-check and V-05's embedded sub-step do not satisfy this criterion; the gate must be structurally independent, not subordinate to another gate.

**C-34** (new, from V-04 C-27 excellence) — **Complete super-gate enumeration in structural audit**. V-04 verified all 4 multi-criterion cluster gates in its structural audit; V-01/V-03/V-05 verified only 2 and V-02 verified 3. When the skill contains N super-gates, all N must be named in the structural audit. A partial enumeration — even of correctly described super-gates — does not satisfy this criterion.

**Scoring**: aspirational pool grows 22 → 26; each criterion now worth `20/26 ≈ 0.769 pts`. Maximum still 100.

---

## Criteria

### ESSENTIAL (5) — all must pass

| ID | What it checks |
|----|----------------|
| C-01 | Artifact scan grounded in real workspace files — no hallucinated topics |
| C-02 | Every discovered topic appears in achievements output |
| C-03 | All three named milestones present by name (First Team Signal, Shared Coverage, Debate Starter) |
| C-04 | Contributor leaderboard section exists and is populated |
| C-05 | Next actions name both the action AND the achievement it unlocks |

---

### RECOMMENDED (3)

| ID | What it checks |
|----|----------------|
| C-06 | Earned vs. available achievements visually separated |
| C-07 | Achievements grouped into at least 2 named categories with explicit labels |
| C-08 | Sprint/date framing present in output |

---

### ASPIRATIONAL (26)

| ID | What it checks |
|----|----------------|
| C-09 | "1 away" quantified close-to-unlock callouts — dedicated section with exact count and exact thing needed |
| C-10 | Cross-topic or cross-contributor insight stated as a named conclusion — and that conclusion differs from any stagnation pattern or gap statement already made |
| C-11 | Skill includes at least one inline pre-write self-test gate — a verification question or confirmation statement the model must answer before generating a section (e.g., "Does this next action name the exact achievement it unlocks?") |
| C-12 | Next actions use anti-inertia framing: each action names not only what it unlocks but what stagnation pattern it breaks — format `[Action] → Unlocks [Achievement] → Breaks [Pattern]` |
| C-13 | The cross-topic insight (C-10) is formatted as a titled, named artifact — `**TEAM INSIGHT — [descriptive name]:**` — making it referenceable by name rather than embedded in prose |
| C-14 | Stagnation patterns referenced in anti-inertia actions (C-12) are drawn from a pre-existing named registry, not invented inline — enforced via label syntax such as `[PATTERN_LABEL from registry]`, preventing vocabulary drift across runs |
| C-15 | When a gate check fails, the error message names the specific instance that triggered the failure (topic name, contributor name, or action row) — not just "halt" but "GATE-B: [topic X] missing → halt" — creating a self-documenting failure trace |
| C-16 | The contributor leaderboard uses an explicit weighted scoring formula (e.g., Signals×1 + Topics×3 + Milestones×5) — not a rank-ordered count — making each contributor's score auditable from raw counts and the team's value judgment about signal types explicit and debatable |
| C-17 | Stagnation pattern labels (C-14) use semantic names that encode the pattern type without requiring a definition lookup (e.g., SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE) — opaque codes such as PATTERN_1 do not satisfy this criterion |
| C-18 | The 1-away callout (C-09) is rendered as a structured table with distinct columns for at minimum: topic/target, achievement to unlock, gap (what's missing), and exact action needed — preventing prose from omitting any field for individual entries |
| C-19 | When the skill includes a formula-driven ranked section (e.g., contributor leaderboard), the skill explicitly instructs the model to render a worked example calculation for the top-ranked contributor inline — e.g., `"Rank-1 calculation: Score = {n}×1 + {n}×3 + {n}×5 = {total}"` — so the reader can verify the ranking without reconstruction; asserting that the formula "makes scores auditable" without this instruction does not satisfy this criterion |
| C-20 | Inline gate checks reference criterion IDs (e.g., `[C-04/C-16]`) as part of the gate label — creating a direct, traceable link between the skill's verification logic and rubric criteria — making gate coverage auditable against the rubric without narrative reconstruction |
| C-21 | When the skill includes a formula verification gate (C-19), the gate explicitly instructs the model to reconcile the ranked table if the worked example calculation reveals a mismatch — e.g., "If the calculated total does not match the Score column entry, correct the table before proceeding" — turning the gate from a display check into an active correction loop; a gate that renders the calculation but does not instruct correction does not satisfy this criterion |
| C-22 | The cross-topic insight gate (C-10) applies a single-topic-derivability test — the skill explicitly instructs that the insight must NOT be derivable from any single topic view alone, not merely cross-topic or cross-contributor in scope — forcing genuine synthesis rather than parallel observation; a gate that only checks scope without testing derivability does not satisfy this criterion |
| C-23 | Multi-condition gate checks enumerate their conditions as numbered sub-steps — e.g., "(1) Every topic I list is traced to a real file. (2) Every topic appears in the achievement section. (3) …" — making each condition individually checkable and preventing a gate from being treated as passed when only some sub-conditions are satisfied; prose commitment statements inside a gate do not satisfy this criterion |
| C-24 | When the skill uses multi-phase execution, at least one later-phase gate explicitly asks whether findings from a prior phase alter the current phase's output — e.g., "Did Phase 2's milestone gaps surface topics not already in the Phase 1 scan?" — creating dynamic cross-phase continuity; a gate that only verifies the current phase's own output without referencing prior-phase findings does not satisfy this criterion |
| C-25 | When a single gate covers multiple interdependent criteria simultaneously, the gate label enumerates all criterion IDs it covers — e.g., `[C-05/C-12/C-14/C-20]` — making inter-criterion dependency explicit and preventing partial-cluster passes where some criteria in the group are verified but related ones are silently omitted; a gate label that names only one criterion ID for a multi-criterion check does not satisfy this criterion |
| C-26 | The skill includes at least one gate condition that verifies whether all other gate labels in the skill carry criterion ID references — a meta-verification step that makes structural compliance (C-20) self-enforcing rather than dependent on external rubric review; C-20 is satisfied by gates that carry criterion IDs, but C-26 is only satisfied when a gate condition audits that requirement across the skill's own gate labels |
| C-27 | When the skill includes a structural audit gate (C-26), that gate names each multi-criterion super-gate by its full label and specifies the exact criterion IDs expected in it — e.g., `"'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21"` — enabling detection of wrong-enumeration failures (a label that reads `[C-16/C-19]` when `[C-16/C-19/C-21]` is required) that a generic presence check cannot catch; a structural audit that only checks whether any criterion ID appears in a gate label does not satisfy this criterion |
| C-28 | When a gate includes a criterion-confirmation condition, the gate frames that confirmation as a first-person ownership statement from the model — e.g., "Before I write this section, I confirm [C-28]: …" — rather than a procedural sub-step or external instruction; framing that reads "Does X satisfy C-28?" or "Check C-28 before proceeding" does not satisfy this criterion because it positions the model as an auditor rather than a committed agent |
| C-29 | When a gate check fails, the skill instructs the model to emit a named correction triad — `"GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section."` — and then re-run the affected section; converting gate violation from a terminal halt event to a named, recoverable correction procedure; a skill that instructs the model to halt or flag without specifying the re-run step does not satisfy this criterion |
| C-30 | When the skill includes a contributor leaderboard, the skill includes a pre-write gate condition that explicitly prohibits inferring achievements backward from contributor identity — requiring that contributor scores derive from the Phase 1 achievement census, not from the model's prior knowledge of contributors' roles or prominence; a gate that verifies formula correctness (C-16) or phase ordering (C-24) without this backward-inference prohibition does not satisfy this criterion |
| C-31 | When the skill includes retry instructions (C-29), those instructions are declared as a single named global retry protocol block — e.g., a preamble section titled "RETRY PROTOCOL" that all gates reference — rather than repeated individually in each gate's fail-path prose; a skill that satisfies C-29 by embedding the re-run instruction only within per-gate fail paths does not satisfy this criterion even if every fail path carries the instruction |
| C-32 | When the skill triggers a retry (C-29/C-31), the skill explicitly instructs the model to wrap the re-run output in labeled open/close delimiters — e.g., `> RETRY [C-XX]: … > END RETRY` — making the retry boundary visible and parseable in the output stream; instructing the model to "re-run the section" without specifying output delimiters does not satisfy this criterion even when the correction triad (C-29) is present |
| C-33 | When the skill includes a backward-inference prohibition (C-30), that prohibition is implemented as a standalone named gate — e.g., `ATTRIBUTION INTEGRITY GATE [C-28/C-30]` — that executes before the contributor leaderboard cluster gate, not as a numbered sub-step embedded within the cluster gate or as an inline pre-check preceding it; a C-30 check that is structurally subordinate to another gate does not satisfy this criterion even when the check is explicitly labeled with C-30 |
| C-34 | When the skill includes a structural audit gate (C-27), that gate's enumeration covers every multi-criterion cluster gate present in the skill — if the skill contains N super-gates, all N are named and verified in the audit; a structural audit that enumerates only a subset of the skill's cluster gates does not satisfy this criterion even if every enumerated gate is correctly and fully described |

---

## Scoring Formula

```
score = (essential_pass/5 × 60) + (recommended_pass/3 × 20) + (aspirational_pass/26 × 20)
PARTIAL = 0.5 weight
```

**Essential**: 5 criteria × 12 pts = 60 pts maximum
**Recommended**: 3 criteria × 6.67 pts = 20 pts maximum
**Aspirational**: 26 criteria × 0.769 pts = 20 pts maximum

To reach 100: all essential pass + all recommended pass + all aspirational pass.
