**Round 4 Scorecard — review-users**

| Rank | Variation | Composite | Golden | Sole discriminator |
|------|-----------|-----------|--------|--------------------|
| 1 | **V-05** | **100** | YES | C-17 PASS (2-example per-section) + C-16 rule + C-18 workaround-first |
| 2 | **V-04** | **100** | YES | C-17 PASS (1-example per-section) + C-16 rule |
| 3 | **V-02** | **100** | YES | C-17 PASS (1-example per-section) + C-16 convention |
| 4 | **V-01** | **99** | YES | C-17 FAIL -- global contrast block only |
| 4 | **V-03** | **99** | YES | C-17 FAIL -- global contrast block only |

**C-17 is the sole rubric discriminator.** V-01 and V-03 fail only because their contrast block is global, not per-section -- the exact failure mode C-17 was designed to catch. All other criteria pass across all five variations.

**Within-100 structural strength:** V-05 > V-04 > V-02 on three independent axes:
- **C-16**: V-04/V-05 (numbered sequence rule) > V-02 (field position)
- **C-17**: V-05 (two domain examples) > V-02/V-04 (one domain example)
- **C-18**: V-03/V-05 (workaround first + gap-statement) > V-01/V-02/V-04 (slot after quote)

**Three new patterns:**
1. **Numbered step sequence** -- makes workaround-before-brief a sequence rule, not a layout convention; closes the last model-reordering risk for C-16
2. **Domain-matched per-section blockquotes** -- role-appropriate prototype at each persona boundary prevents tag drift better than a global reminder 3000 tokens back
3. **Workaround-first amend with gap-statement** -- reframes proposals from artifact annotations ("step 3 is unclear") into workaround-replacement arguments ("Sam currently does Y and the artifact cannot replace Y because X")

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Numbered step sequence makes workaround-before-scenario-brief a sequence rule rather than a layout convention; a model cannot place Step 2 before Step 1 without violating the numbered sequence, closing the last model-reordering risk for C-16", "Domain-matched per-section blockquote reminders with role-appropriate friction examples prevent tag drift in long multi-persona outputs better than domain-agnostic global blocks; the model has a live domain prototype at the exact persona boundary where it begins narrating, not a generic example from 3000 tokens prior", "Workaround-first amend template with explicit gap-statement field restructures proposals from artifact annotations into workaround-replacement arguments; when workaround is the first field written, the problem is framed as Sam currently does Y and the artifact cannot replace Y because X rather than the artifact said X and that was a problem, producing targeted rather than generic remediation"]}
```
C-06 -- All variations PASS

Every prompt states "Write each walkthrough in first person AS the named character." The Step 3 / Walkthrough instruction reinforces this at the persona level.

#### C-07 -- All variations PASS

All five templates include separate tables for "Universal friction (3+ personas)" and "Role-specific friction (1-2 personas only)" with distinct column structures.

#### C-08 -- All variations PASS

All five templates include a "Persona conflicts" subsection with explicit instructions to identify Beats/Loses cross-comparison and name both characters, the artifact feature, and who gains vs. who loses.

#### C-09 -- All variations PASS (different structural strength)

V-01 and V-03 provide a single global contrast block in the PERSONA WALKTHROUGHS preamble. V-02 and V-04 provide a role-appropriate blockquote per persona with one correct/wrong pair. V-05 provides per-section blockquotes with two correct examples per persona. All five satisfy the C-09 pass condition (contrast block present). C-17 captures the per-section distinction.

#### C-14 -- All variations PASS

- V-01, V-04, V-05: "Step 1 -- Current workaround (before anything else):" -- table-anchored, numbered, positionally first in persona section.
- V-02, V-03: "**What [Name] does today instead:**" -- appears before the scenario heading. Both satisfy "before the walkthrough narrative begins."

#### C-16 -- All variations PASS (different structural strength)

- V-01, V-04, V-05: Numbered step sequence (Step 1 = workaround, Step 2 = scenario brief). Ordering is a sequence rule: a model cannot place Step 2 before Step 1 without violating the numbered sequence.
- V-02, V-03: "**What [Name] does today instead:**" appears before the "**Scenario:**" heading. Field position enforces the ordering. Less structurally rigid than numbered steps but satisfies the pass condition.

#### C-17 -- FAIL in V-01 and V-03

C-17 pass condition: contrast block inside each individual persona section, not only in a global preamble.

- V-01: Single global contrast block in the PERSONA WALKTHROUGHS preamble. No per-section blockquote. The contrast block is 3000+ tokens before the 4th and 5th persona sections. FAIL.
- V-03: Same structure as V-01 -- global contrast block only. FAIL.
- V-02, V-04: Role-appropriate blockquote inside each persona section with one correct/wrong pair drawn from that role's friction domain. PASS.
- V-05: Per-section blockquotes with two correct examples per persona (domain-matched). PASS -- strongest guarantee.

#### C-18 -- All variations PASS (different structural strength)

C-18 pass condition: amend template includes an explicit named-workaround slot before stating the proposed change.

- V-01, V-02, V-04: Template order -- verbatim quote -> "Current workaround being displaced" -> proposed change. Slot appears after the quote but before the proposed change. Pass condition satisfied.
- V-03, V-05: Template order -- workaround -> gap-statement -> verbatim quote -> proposed change. Workaround is the first field, with an explicit "What the workaround provides that the artifact does not:" gap-statement before the quote. Workaround becomes the primary frame, not secondary context.

---

### Composite Scores

```
V-01: (5/5 * 60) + (3/3 * 30) + (9/10 * 10)  = 60 + 30 + 9  = 99
V-02: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = 60 + 30 + 10 = 100
V-03: (5/5 * 60) + (3/3 * 30) + (9/10 * 10)  = 60 + 30 + 9  = 99
V-04: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = 60 + 30 + 10 = 100
V-05: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = 60 + 30 + 10 = 100
```

---

### Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden | C-16 mechanism | C-17 mechanism | C-18 mechanism |
|------|-----------|-----------|-------------|--------------|-----------|--------|----------------|----------------|----------------|
| 1 | **V-05** | 5/5 | 3/3 | 10/10 | **100** | YES | Numbered steps (rule) | Per-section, 2 domain examples | Workaround first + gap-statement |
| 2 | **V-04** | 5/5 | 3/3 | 10/10 | **100** | YES | Numbered steps (rule) | Per-section, 1 domain example | Slot after quote |
| 3 | **V-02** | 5/5 | 3/3 | 10/10 | **100** | YES | Field position (convention) | Per-section, 1 domain example | Slot after quote |
| 4 | **V-01** | 5/5 | 3/3 | 9/10 | **99** | YES | Numbered steps (rule) | Global only (FAIL) | Slot after quote |
| 4 | **V-03** | 5/5 | 3/3 | 9/10 | **99** | YES | Field position (convention) | Global only (FAIL) | Workaround first + gap-statement |

The sole discriminator between 100 and 99 is C-17: per-section contrast blocks (V-02, V-04, V-05) score 100; global-only (V-01, V-03) score 99.

---

### Within-100 Structural Strength Ranking

| Strength | Variation | Why |
|----------|-----------|-----|
| Strongest | V-05 | Numbered steps (C-16 as rule) + per-section with 2 domain examples (C-17 strongest) + workaround-first amend with gap-statement (C-18 strongest frame) |
| Strong | V-04 | Numbered steps (C-16 as rule) + per-section with 1 domain example (C-17 strong) + slot after quote (C-18 weaker frame) |
| Adequate | V-02 | Field position for C-16 (convention, not rule) + per-section with 1 domain example (C-17 strong) + slot after quote (C-18 weaker frame) |

V-05 is the only variation that structurally enforces all three R4 mechanisms simultaneously at their maximum strength.

---

### Excellence Signals -- Round 4

#### E-1: Numbered step sequence makes C-16 a rule, not a convention

V-01, V-04, and V-05 use explicit numbered steps (Step 1 -- workaround, Step 2 -- scenario brief, Step 3 -- walkthrough). A model operating on a numbered sequence cannot place Step 2 before Step 1 without violating the sequence -- the ordering is structural, not positional. V-02 and V-03 rely on field position alone. The numbered step mechanism closes the last model-reordering risk for C-16. V-01 demonstrates that numbered steps alone (without per-section blocks) still fail C-17; this confirms the two mechanisms are independent -- each is necessary for its criterion, neither is sufficient on its own.

#### E-2: Domain-matched examples per section prevent friction-tag drift better than domain-agnostic reminders

V-02, V-04, and V-05 provide role-appropriate contrast block examples at each persona boundary: Sam gets a build-process confusion example, Dev gets an API error-handling friction example, Casey gets a GDPR fear example, Jordan gets an approval-chain confusion example, Alex gets a recovery-step friction example. A global contrast block placed once at prompt level is 3000+ tokens away from the 4th and 5th persona sections. A role-specific prototype placed at the exact start of each walkthrough is harder to skip and easier to pattern-match: the model has a live domain example for the persona it is about to narrate. V-05 extends this with two correct examples per section -- a second example adds a different tag type, reducing the risk of the model pattern-matching only confusion and skipping fear or jargon.

#### E-3: Workaround-first amend template restructures proposals from artifact annotations to workaround-replacement arguments

V-03 and V-05 invert the field order to: (1) current workaround -> (2) what the workaround provides that the artifact does not (explicit gap-statement) -> (3) verbatim quote -> (4) proposed change. When the workaround is the first field, the problem is framed as "Sam currently does Y, and the artifact cannot replace Y because X" rather than "the artifact said X and that was a problem." The gap-statement field forces the model to name the specific capability gap before citing the artifact text that exposes it. V-03 demonstrates this mechanism is independent of numbered steps: V-03 FAILS C-17 but has the strongest amend template. V-05 combines both.

---

### R4 Findings

#### F-01: C-17 is the sole discriminator at rubric level

All variations pass all essential and recommended criteria. C-17 alone separates the 100 cluster (V-02, V-04, V-05) from the 99 cluster (V-01, V-03). Per-section contrast blocks vs. global-only blocks is the single actionable design lever at the rubric level in R4.

#### F-02: Within-100, three mechanism strengths create a quality gradient invisible to the rubric

All three 100-scoring variations have identical rubric scores but different structural guarantees:
- C-16: numbered steps (V-04, V-05) > field position (V-02)
- C-17: two domain examples (V-05) > one domain example (V-02, V-04)
- C-18: workaround-first + gap-statement (V-05) > slot after quote (V-02, V-04)

The rubric score cannot distinguish V-05 from V-02 or V-04, but V-05's compound structural enforcement is expected to produce higher compliance rates in live model runs.

#### F-03: C-16 and C-17 are independent mechanisms -- neither is sufficient without the other

V-01 demonstrates the failure mode: numbered steps enforce C-16 but do nothing for C-17. V-03 demonstrates the symmetric failure: workaround-first amend and field-position C-16, but no per-section blocks, so C-17 fails. A variation must independently satisfy both mechanisms to score 100. V-04 is the minimum combination (numbered steps + per-section blocks). V-05 adds the strongest C-18 on top.

#### F-04: All five R4 variations are Golden -- R3 floor holds

The floor established in R3 holds through R4: all essential and recommended criteria pass across all five variations. Discrimination lives entirely at C-17 (rubric level) and within-100 structural strength (quality level).

---

### Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- 100/100 composite
- Strongest structural guarantees on all three R4 criteria
- All R3 mechanisms carried forward at equal or higher strength
- No format switching required at any step -- all five mechanism groups mutually reinforce

**V-04** is the structural runner-up. Numbered steps + per-section blocks, but amend template places workaround after quote. In contexts where amend loop quality is less critical (all scores >= 3), V-04 is structurally equivalent to V-05.

**V-02** is the minimal-change path from R3: adds per-section contrast blocks without introducing numbered steps. Lower structural risk than V-01/V-03 but weaker than V-04/V-05.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Numbered step sequence makes workaround-before-scenario-brief a sequence rule rather than a layout convention; a model cannot place Step 2 before Step 1 without violating the numbered sequence, closing the last model-reordering risk for C-16", "Domain-matched per-section blockquote reminders with role-appropriate friction examples prevent tag drift in long multi-persona outputs better than domain-agnostic global blocks; the model has a live domain prototype at the exact persona boundary where it begins narrating, not a generic example from 3000 tokens prior", "Workaround-first amend template with explicit gap-statement field restructures proposals from artifact annotations into workaround-replacement arguments; when workaround is the first field written, the problem is framed as Sam currently does Y and the artifact cannot replace Y because X rather than the artifact said X and that was a problem, producing targeted rather than generic remediation"]}
```