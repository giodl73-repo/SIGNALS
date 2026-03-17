## /quest:score — validate-inertia — Round 2

---

### Scoring: V-01 through V-05

| V | C01 | C02 | C03 | C04 | C05 | C06 | C07 | C08 | C09 | C10 | C11 | C12 | **Total** |
|---|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----------|
| V-01 | P | P | P | **~** | P | P | P | P | P | **~** | P | P | **93** |
| V-02 | P | P | P | **P** | P | P | P | P | P | **P** | P | P | **100** |
| V-03 | P | P | P | P | P | P | P | **F** | P | **~** | P | P | **89** |
| V-04 | P | P | P | P | P | P | P | P | P | **~** | P | P | **99** |
| V-05 | P | P | P | **~** | P | P | P | P | P | **P** | P | P | **94** |

P = PASS, ~ = PARTIAL, F = FAIL

**Rankings:** V-02 (100) > V-04 (99) > V-05 (94) > V-01 (93) > V-03 (89)

---

### Key findings

**V-02 is the first perfect score.** The asymmetry-triage-first design unlocks both C-04 and C-10 simultaneously:
- C-04 passes because Phase 3's Workaround Satisfaction column explicitly requires "Flag 4+ as 'good enough.' State the specific reason."
- C-10 passes because Phase 2 forces inertia landscape classification (Structural/Behavioral/Mixed) before any persona, and Phase 4 includes "permanent lost TAM until product changes" explicitly.

**C-04 is the persistent gap in table-format variants.** V-01 and V-05 both have satisfaction framing but no "good enough" explanation rule. The fix is a single column rule: "Flag 4+ as 'good enough' -- state the specific reason."

**C-10 requires the TAM framing, not just the vocabulary.** V-01, V-03, V-04 all use structural/behavioral language but without "permanent lost TAM" as an explicit required statement — all three get PARTIAL. V-02 and V-05 (which has "Lost TAM implication: {one sentence}" as a required output) both get PASS.

**V-03 drops C-08 entirely** (no learning curve question anywhere in the prompt). Its trade-off — the success signal in Phase 3 — makes C-09 the strongest of any variant, but losing a full recommended criterion costs 10 pts.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertia landscape classification as a dedicated pre-persona phase (Structural/Behavioral/Mixed) transforms C-10 from post-hoc synthesis to deliberate analytical choice -- the type of inertia structurally gates the type of mitigation, propagating specificity into C-09", "Type-conditioned mitigation ('if structural: name the product change; if behavioral: name the launch sequence') is a stronger C-09 guarantee than an anti-patterns list -- it constrains the answer space before the model writes rather than naming failures after", "Explicit 'Lost TAM implication' statement as a required non-conditional synthesis line locks in the permanent-vs-delayed framing C-10 requires -- conditional asymmetry sections reliably produce PARTIAL regardless of structural/behavioral vocabulary"]}
```
2 + 12 + 6 + 12 + 10 + 10 + 10 + 3 + 2 + 2 + 2 = **93**
**All essential pass:** NO (C-04 = PARTIAL)

---

### V-02 — Asymmetry triage first

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | Phase 3: "For each persona, state why they chose the incumbent -- role-grounded, not generic"; table column "Why They Use the Incumbent: the adoption decision -- 'X won this persona because...'" |
| C-02 | Switching cost quantified | PASS | "Switching Cost: concrete units only (hours, steps, files, dollars, rollback risk). Vague fails." -- unconditional enforcement |
| C-03 | Kill barrier named | PASS | Phase 1 kill barrier hypothesis with explicit label; Phase 3 "Kill Barrier (confirmed):" or "Kill Barrier (revised):" |
| C-04 | Workaround satisfaction assessed | PASS | Table column "Workaround Satisfaction (1-5). Flag 4+ as 'good enough.' State the specific reason." -- satisfaction level + "good enough" trigger + explanation all required per persona |
| C-05 | Per-persona inertia score present | PASS | "Inertia Score: Low / Medium / High / Critical. Consistent scale." Required every row |
| C-06 | Habit lock-in addressed | PASS | "Habit at Risk: specific behavioral pattern, not a category." Required table column |
| C-07 | Social proof requirement mapped | PASS | "Social Proof Needed: specific threshold -- names, numbers, evidence type." Required column |
| C-08 | Learning curve quantified | PASS | "Learning Curve: time or concept count; comparison anchor preferred." Required column |
| C-09 | Overall risk rating with mitigation | PASS | Phase 4: overall risk + type-conditioned mitigation: "If the kill barrier is structural: name the product change required. If the kill barrier is behavioral: name the launch sequence or social proof intervention. Do not restate. Do not propose generic onboarding." -- strongest C-09 constraint of any variant |
| C-10 | Inertia asymmetry identified | PASS | Phase 2 inertia landscape classification (Structural/Behavioral/Mixed) runs before any persona analysis; Phase 4 asymmetry section explicitly includes "permanent lost TAM until product changes" and "delayed adoption, reachable with launch strategy" -- full pass condition met |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | Phase 1 → Phase 2 (landscape classification) → Phase 3 (personas); kill barrier structurally first |
| C-12 | Status-quo treated as competitor | PASS | Phase 2: "Name the incumbent... In one sentence: why did users choose it?"; Phase 3 per-persona column captures adoption decision framing |

**Score:** 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 3 + 3 + 2 + 2 = **100**
**All essential pass:** YES

---

### V-03 — Mitigation workshop

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | Phase 2: "Why did this persona choose the incumbent? Role-grounded reason -- 'X won this persona because their role requires...' Not just what they use, but why they use it." Per persona |
| C-02 | Switching cost quantified | PASS | "What would switching cost them? At least one concrete unit: hours to migrate, number of files to change, dollars, rollback risk. Vague language ('significant effort') fails." |
| C-03 | Kill barrier named | PASS | Phase 1 hypothesis; Phase 3 "Kill Barrier: {confirmed or revised -- one sentence}" with explicit label |
| C-04 | Workaround satisfaction assessed | PASS | Phase 2: "Workaround satisfaction (1-5). Flag 4+ as 'good enough' and state why." Per persona with "good enough" trigger and explanation required |
| C-05 | Per-persona inertia score present | PASS | "Assign each persona an inertia score: Low / Medium / High / Critical." Per persona, consistent scale |
| C-06 | Habit lock-in addressed | PASS | Phase 2: "What behavioral pattern or ritual keeps them on the incumbent even when it frustrates them? Name the specific habit, not the category." Per persona |
| C-07 | Social proof requirement mapped | PASS | Phase 2: "What social proof would it take for them to try the feature? Specific threshold." Per persona |
| C-08 | Learning curve quantified | FAIL | No learning curve question anywhere in V-03. Phase 2's five per-persona questions cover: (1) why they chose incumbent, (2) workaround satisfaction, (3) switching cost, (4) behavioral habit, (5) social proof. Learning curve is entirely absent. |
| C-09 | Overall risk rating with mitigation | PASS -- strongest of all variants | Phase 3 Mitigation Workshop: overall risk + kill barrier mechanism ("why this kills adoption: the mechanism, not the symptom") + specific mitigation assignable to owner + success signal ("how you would know the mitigation worked"). Anti-patterns list explicitly names 4 failure modes. |
| C-10 | Inertia asymmetry identified | PARTIAL | "Inertia asymmetry (if the evidence supports it)" -- conditional; structural/behavioral distinction present but no "permanent lost TAM" language and section is gated on evidence |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | Phase 1 (kill barrier) before Phase 2 (competitor analysis + personas) |
| C-12 | Status-quo treated as competitor | PASS | Phase 2 title "COMPETITOR ANALYSIS"; per-persona "Why did this persona choose the incumbent? ... Not just what they use, but why they use it." |

**Score:** 12 + 12 + 12 + 12 + 12 + 10 + 10 + 0 + 3 + 2 + 2 + 2 = **89**
**All essential pass:** YES (C-08 is recommended, not essential)

---

### V-04 — Narrative register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | "Identify 3-5 personas... For each, write a portrait addressing: Who are they and what is their relationship to this problem?" -- role and resistance reason emerge structurally from the portrait format |
| C-02 | Switching cost quantified | PASS | Per portrait: "What would switching actually cost them? Use concrete terms: hours, number of files to touch, risk of something breaking, investment to migrate existing work." |
| C-03 | Kill barrier named | PASS | "THE VERDICT" section: "Kill Barrier: {one sentence -- the specific mechanism that would prevent adoption entirely. Must be feature-specific...}" -- explicitly labeled |
| C-04 | Workaround satisfaction assessed | PASS | Per portrait: "What is their current workaround and how satisfied are they? (Rate 1-5.)" -- satisfaction rating required per persona |
| C-05 | Per-persona inertia score present | PASS | "Close each portrait with one line: Inertia Score: Low / Medium / High / Critical" -- required final line of every portrait |
| C-06 | Habit lock-in addressed | PASS | Per portrait: "What is the habit or ritual that would pull them back -- the behavior that fires before they even think about it?" -- behavioral specificity required |
| C-07 | Social proof requirement mapped | PASS | Per portrait: "What would they need to see from colleagues or the community before trusting this feature?" -- threshold question |
| C-08 | Learning curve quantified | PASS | Per portrait: "How long would it take them to feel fluent? Compare to something they already know." -- time estimate + comparison anchor explicitly requested |
| C-09 | Overall risk rating with mitigation | PASS | "Overall adoption inertia risk: Low / Medium / High / Critical" + "Name a specific mitigation -- not 'improve onboarding' but the actual intervention... Name the action and the owner." Anti-generic framing present |
| C-10 | Inertia asymmetry identified | PARTIAL | "Inertia asymmetry (if the portrait work reveals it)" -- conditional; structural/behavioral framing present ("won't adopt without product changes" vs "reached with the right launch approach") but no "permanent lost TAM" language |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | "START WITH YOUR BET" section runs before "THE INCUMBENT'S STORY" and "PERSONA INERTIA PORTRAITS" -- structural ordering enforced |
| C-12 | Status-quo treated as competitor | PASS -- strongest narrative execution | "THE INCUMBENT'S STORY" section: "Why did users adopt it?... For at least one persona, tell the story of how they came to rely on it: 'Maya adopted the bash script because...'" -- sentence-starter template directly encodes the C-12 pass condition |

**Score:** 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 3 + 2 + 2 + 2 = **99**
**All essential pass:** YES

---

### V-05 — Compressed minimal scaffold

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Named personas, role-grounded resistance | PASS | Table column "Why Incumbent Won: role-grounded reason, not 'it works.'" Required 3-5 rows |
| C-02 | Switching cost quantified | PASS | "Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). 'High' fails." Required column |
| C-03 | Kill barrier named | PASS | Section 1 hypothesis with explicit label; Section 4 "Kill Barrier (confirmed or revised):" |
| C-04 | Workaround satisfaction assessed | PARTIAL | Table header includes "Workaround Satisfaction (1-5)" column but no column rules require explanation of why the score means "good enough"; compressed format produces a number but not the "why it feels good enough" reasoning the rubric requires |
| C-05 | Per-persona inertia score present | PASS | "Inertia Score: exactly Low / Medium / High / Critical. Same scale. Required for every row." |
| C-06 | Habit lock-in addressed | PASS | "Habit at Risk: specific behavior, not a category." Required column |
| C-07 | Social proof requirement mapped | PASS | "Social Proof Needed: specific threshold -- number, name, or evidence type." Required column |
| C-08 | Learning curve quantified | PASS | "Learning Curve: time or concept count; comparison anchor preferred." Required column |
| C-09 | Overall risk rating with mitigation | PASS | Section 6: overall risk + "Mitigation: specific action targeting the kill barrier. Not a restatement. Not 'improve onboarding.' Specific enough to assign to an owner and measure." |
| C-10 | Inertia asymmetry identified | PASS | Section 5 "INERTIA ASYMMETRY": "Structural (product must change to reach these personas)... Behavioral (launch strategy can reach these personas)... Lost TAM implication: {one sentence}" -- explicit "Lost TAM" framing satisfies "permanent lost TAM vs. delayed adoption" requirement |
| C-11 | Kill barrier hypothesized before persona analysis | PASS | "Produce these sections in order. Do not reorder." Section 1 = Kill Barrier Hypothesis; Section 3 = Persona Table -- structural ordering locked |
| C-12 | Status-quo treated as competitor | PASS | Section 2: "Why users chose it: 'They adopted it because ___.' (at least one persona -- the adoption decision, not just current state)" -- sentence-starter encodes adoption decision framing |

**Score:** 12 + 12 + 12 + 6 + 12 + 10 + 10 + 10 + 3 + 3 + 2 + 2 = **94**
**All essential pass:** NO (C-04 = PARTIAL)

---

## Rankings

| Rank | Variation | Score | All Essential Pass | Key Differentiator |
|------|-----------|-------|--------------------|--------------------|
| 1 | V-02 Asymmetry triage first | **100** | YES | Only variant with full C-04 + full C-10; type-conditioned mitigation is strongest C-09 |
| 2 | V-04 Narrative register | **99** | YES | Strongest C-12 execution; loses 1 pt only on C-10 (no TAM language, conditional) |
| 3 | V-05 Compressed scaffold | **94** | NO | C-10 PASS via "Lost TAM implication"; C-04 PARTIAL (no "good enough" reasoning in table) |
| 4 | V-01 Best-of-R1 baseline | **93** | NO | C-04 PARTIAL (no satisfaction column); C-10 PARTIAL (conditional, no TAM language) |
| 5 | V-03 Mitigation workshop | **89** | YES | Strongest C-09 (success signal + anti-patterns); C-08 fully absent; C-10 PARTIAL |

---

## Excellence Signals (from V-02)

**1. Pre-persona inertia landscape classification produces a reliable C-10 PASS.**
When Claude must classify the feature's inertia as Structural/Behavioral/Mixed before analyzing any persona, C-10 becomes a deliberate analytical choice rather than a post-hoc label. This also gates mitigation type: structural demands a product answer, behavioral demands a launch answer -- that constraint propagates forward into C-09 and eliminates vague mitigations structurally rather than by instruction.

**2. Type-conditioned mitigation is a stronger C-09 guarantee than anti-patterns alone.**
V-02's "if structural: name the product change; if behavioral: name the launch sequence or social proof intervention" constrains the answer space before the model writes the mitigation. V-03's anti-patterns list names what to avoid but leaves the solution space open. Type-conditioning is structurally narrower and more reliable.

**3. "Lost TAM implication" as a required (non-conditional) synthesis statement locks C-10.**
V-01, V-03, V-04 all use "if the evidence supports it" framing for asymmetry, producing reliable PARTIAL results. V-05's explicit required section with "Lost TAM implication: {one sentence}" forces the permanent-vs-delayed framing regardless of evidence confidence. For C-10, the framing trigger matters more than the evidence quality.

**4. C-04's "good enough" trigger requires both a rating AND a reason.**
V-02 and V-03 pass C-04 because they explicitly ask for a score AND "state the specific reason" / "state why." V-01 and V-05 fail because they have the rating (or just framing) but not the explanation requirement. In compressed table formats, the "Flag 4+ as 'good enough' -- state the specific reason" column rule pattern is the key fix.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertia landscape classification as a dedicated pre-persona phase (Structural/Behavioral/Mixed) transforms C-10 from post-hoc synthesis to deliberate analytical choice -- the type of inertia structurally gates the type of mitigation, propagating specificity into C-09", "Type-conditioned mitigation ('if structural: name the product change; if behavioral: name the launch sequence') is a stronger C-09 guarantee than an anti-patterns list -- it constrains the answer space before the model writes rather than naming failures after", "Explicit 'Lost TAM implication' statement as a required non-conditional synthesis line locks in the permanent-vs-delayed framing C-10 requires -- conditional asymmetry sections reliably produce PARTIAL regardless of structural/behavioral vocabulary"]}
```
