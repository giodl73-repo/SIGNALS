## Quest Score — signal-setup Round 5 (v5 rubric)

### Evaluation Framework

**Formula**: `(E/5 * 60) + (R/3 * 30) + (A/10 * 10)`
**Golden threshold**: all 5 essentials PASS AND composite ≥ 80

---

## V-01 — Axis A: Explicit temporal persistence argument in preamble

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | File detection before write | **PASS** | GATE 0 reads CLAUDE.md and searches for existing Signal section before any write |
| C-02 | Preview shown before writing | **PASS** | GATE 3 shows exact content before GATE 4 confirmation |
| C-03 | Confirmation required | **PASS** | GATE 4: "Add this Signal section to your CLAUDE.md? [y/N]" |
| C-04 | Signal section appended with skill advertising | **PASS** | Section lists `/decide`, `/signal`, `/competitors` with descriptions |
| C-05 | Idempotent re-run | **PASS** | GATE 2 detects existing Signal section and stops |
| C-06 | Inertia rule included | **PASS** | "The one rule: the primary competitor is always inertia. Before any feature, ask 'why would teams do nothing instead?'" |
| C-07 | Copilot instructions offered | **PASS** | GATE 6 checks and offers to update .github/copilot-instructions.md |
| C-08 | User feedback on outcome | **PASS** | GATE 5 confirms written; GATE 7 prints usage summary |
| C-09 | Preview matches written output | **PASS** | GATE 5: "Append the Signal section (exactly as shown in GATE 3)" |
| C-10 | Handles missing CLAUDE.md gracefully | **PASS** | GATE 1 creates new file with preview + confirmation |
| C-11 | Named gate checkpoints as explicit phase boundaries | **PASS** | GATE 0–7 all labeled; no phase implicitly skipped |
| C-12 | Edge-case paths promoted to first-class gates | **PASS** | GATE 1 (MISSING FILE) and GATE 2 (ALREADY CONFIGURED) are dedicated named gates |
| C-13 | Skill opens with motivational preamble | **PASS** | 4-sentence philosophical framing precedes all gates |
| C-14 | Decline path names its consequence | **PASS** | "Inertia remains unnamed… no reminder to ask 'why would teams do nothing?' before the next build. That question will not be in Claude's context by default." |
| C-15 | Already-configured path affirms positive consequence | **PASS** | "your CLAUDE.md carries the reminder to ask 'why would teams do nothing?' before every build" |
| C-16 | Inertia named as adversary, not concept | **PASS** | "Every Signal workspace has one silent competitor: inertia" |
| C-17 | Preamble explains temporal persistence of configuration | **PASS** | Explicit causal chain: "every Claude Code session that opens this workspace loads CLAUDE.md automatically — which means the inertia question is present every time, without you having to remember to ask it. The write happens once. The reminder is permanent." |
| C-18 | Decline path anchors consequence to a future moment | **PASS** | "before the next build" — specific future moment |

**E=5/5, R=3/3, A=10/10**
**Score: (60) + (30) + (10) = 100**

---

## V-02 — Axis B: Vivid future moment in decline path

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | All essential + recommended | **PASS** | Structure identical to V-01; same gates |
| C-09–C-16 | Aspirational C-09 through C-16 | **PASS** | Same gate structure as R4 V-05 which passed all |
| C-17 | Preamble explains temporal persistence | **PARTIAL** | "gives Claude a persistent reminder… before every feature, every session. Configure once. Fight inertia every time." — asserts persistence but omits the mechanism (loads automatically). The *why* of permanence is absent; the *that* is present only as claim. |
| C-18 | Decline path anchors to a future moment | **PASS** | "before you write the first line of your spec" — anchors to the *decision* moment, earlier and more precise than R4 V-05's "before the next build" |

**E=5/5, R=3/3, A=9/10** (C-17 PARTIAL = 0)
**Score: (60) + (30) + (9) = 99**

---

## V-03 — Axis C: Condensed preamble retaining C-17

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | All essential + recommended | **PASS** | Same gate structure |
| C-09–C-16 | Aspirational C-09 through C-16 | **PASS** | Gate structure preserved; C-16 PASS: "Inertia is the feature team's silent default" |
| C-17 | Preamble explains temporal persistence | **PARTIAL** | "every session that opens this workspace inherits it. You configure once. Claude asks it every time." — the *inheritance* chain is present but the mechanism is implied, not stated. "Inherits" stops short of naming why: CLAUDE.md is loaded automatically. C-17 requires the argument, not only the assertion. V-03 is a step closer than R4 V-05 but does not fully close the gap that V-01 closes by naming "loads CLAUDE.md automatically." |
| C-18 | Decline path anchors to a future moment | **PASS** | "before the next build" — specific future moment (unchanged from R4 V-05 baseline) |

**E=5/5, R=3/3, A=9/10** (C-17 PARTIAL = 0)
**Score: (60) + (30) + (9) = 99**

*Note on the border call*: V-03 is a genuine improvement on R4 V-05 — "inherits it" is closer to the mechanism than "Fight inertia every time." But the pass condition specifically requires explaining *why* configuration persists, which points to the automatic file-load. "Inherits" implies it; V-01 states it. Borderline PARTIAL is the correct ruling.

---

## V-04 — Axes A + B: Explicit persistence + vivid future moment

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | All essential + recommended | **PASS** | Same gate structure |
| C-09–C-16 | Aspirational C-09 through C-16 | **PASS** | All gates preserved from R4 V-05 baseline |
| C-17 | Preamble explains temporal persistence | **PASS** | V-01's preamble, unchanged: "loads CLAUDE.md automatically — which means the inertia question is present every time, without you having to remember to ask it. The write happens once. The reminder is permanent." Full causal chain present. |
| C-18 | Decline path anchors to a future moment | **PASS** | V-02's decline: "before you write the first line of your spec" — decision-moment anchor, more specific than build-phase anchor |

**E=5/5, R=3/3, A=10/10**
**Score: (60) + (30) + (10) = 100**

---

## V-05 — Axes A + B + E: Full threading through all exit gates

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | All essential + recommended | **PASS** | Same gate structure; GATE 1 and GATE 2 extended but still functionally correct |
| C-09 | Preview matches written output | **PASS** | "exactly as shown in GATE 3" |
| C-10 | Handles missing CLAUDE.md gracefully | **PASS** | GATE 1 creates file with preview, confirmation, and now adds temporal framing to the creation message — still graceful |
| C-11 | Named gate checkpoints | **PASS** | GATE 0–7 labeled |
| C-12 | Edge-case paths first-class gates | **PASS** | GATE 1 and GATE 2 both have their own full treatment |
| C-13 | Motivational preamble | **PASS** | Same preamble as V-01 |
| C-14 | Decline path names its consequence | **PASS** | GATE 4: "before you write the first line — there will be no reminder in your context to ask 'why would teams do nothing instead?'" |
| C-15 | Already-configured affirms positive consequence | **PASS** | GATE 2 now stronger: "Every session that opens this workspace loads CLAUDE.md and inherits the inertia question — automatically, without you having to remember. You configured this once; it has been working in every session since." |
| C-16 | Inertia named as adversary | **PASS** | "one silent competitor: inertia" |
| C-17 | Preamble explains temporal persistence | **PASS** | Explicit mechanism in preamble; GATE 2 also carries it, reinforcing the argument at the affirmation exit |
| C-18 | Decline anchors to a future moment | **PASS** | Both GATE 4 and GATE 1 decline carry "before you write the first line" — the same future moment appears at every decline exit |

**E=5/5, R=3/3, A=10/10**
**Score: (60) + (30) + (10) = 100**

---

## Score Summary

| Variation | Axis | E | R | A | Score | Golden |
|-----------|------|---|---|---|-------|--------|
| R4 V-05 (baseline) | A+B+C+D+E (v4) | 5/5 | 3/3 | 9/10 | 99 | Yes |
| **V-01** | A: explicit persistence | 5/5 | 3/3 | **10/10** | **100** | **Yes** |
| V-02 | B: vivid future moment | 5/5 | 3/3 | 9/10 | 99 | Yes |
| V-03 | C: condensed preamble | 5/5 | 3/3 | 9/10 | 99 | Yes |
| **V-04** | A+B: explicit + vivid | 5/5 | 3/3 | **10/10** | **100** | **Yes** |
| **V-05** | A+B+E: full threading | 5/5 | 3/3 | **10/10** | **100** | **Yes** |

---

## Champion Recommendation

**V-04** is the recommended champion.

V-01 reaches 100 with the minimum preamble change, but uses "before the next build" in the decline — a phase-level anchor. V-04 replaces that with "before you write the first line of your spec" — the decision moment, not the consequence moment. This is more honest about where the user's agency lies and does not add length anywhere in the gate structure. V-04 is the minimum-change path to 100 and the highest-quality expression of both C-17 and C-18.

V-05 is the architecturally coherent choice — every exit gate speaks the same voice. But the GATE 2 response now runs 4 sentences on the skip path, which introduces a verbose-on-skip risk. For a setup skill, the skip path (already configured) should be brief and reassuring; V-05's extension is defensible but not free. V-04 avoids that cost.

---

## Excellence Signals from Top-Scoring Variations

**E-01: Mechanism over slogan for temporal persistence.** V-01/V-04/V-05 all pass C-17 by stating the causal chain explicitly: "loads CLAUDE.md automatically — which means the inertia question is present every time, without you having to remember to ask it." The key phrase is "automatically" — it names the mechanism, not just the result. Slogans assert. Arguments explain. The rubric requires explanation.

**E-02: Decision-moment anchoring in decline paths.** V-04/V-05 anchor the decline consequence to "before you write the first line of your spec" rather than "before the next build." The spec-writing moment is where the user *makes the choice*; the build is where they *feel the consequence*. Anchoring to the choice moment is more precise about when the absence is felt — and more actionable, because the user is still at the decision point when they decline.

**E-03: Retroactive service affirmation in the already-configured path.** V-05 GATE 2 adds "You configured this once; it has been working in every session since." This goes beyond C-15's forward-oriented consequence naming — it affirms *accumulated past benefit*, creating recognition that the configuration has already been silently protecting every prior session. This is a distinct temporal register not captured by any existing criterion.

**E-04: Cross-gate temporal consistency.** V-05 threads the specific future moment ("before you write the first line") through both the GATE 1 decline and the GATE 4 decline. When every exit point speaks the same voice about *when* the absence will be felt, the skill achieves uniform emotional weight regardless of path taken. C-18 only measures the primary decline gate; coherence across all decline exits is a separate quality axis.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Retroactive service affirmation: the already-configured path names not just what configuration achieves going forward but affirms that it has been working silently on the user's behalf since setup — recognizing accumulated past benefit, distinct from C-15's forward-oriented consequence naming.", "Cross-gate temporal consistency: anchoring decline feedback to a specific future moment should be threaded through all decline exits (GATE 1 missing-file and GATE 4 primary) with the same voice, creating uniform emotional weight regardless of path — C-18 measures the primary gate only, not whether the moment is consistent across all exits."]}
```
