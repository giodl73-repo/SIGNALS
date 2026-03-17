Reading the scorecard carefully to extract the new patterns before writing the rubric.

Two signals surface that go beyond C-01 through C-15:

**From V-02**: The axis states "consequence clause, evasion surface, and floor declaration — embedded verbatim in template cells. Model fills placeholders only." C-14 and C-15 test for the *presence* of the text. They don't test the *mechanism*: pre-printing in the skeleton versus rule-stating. V-02 achieves a qualitatively different structural guarantee — the model cannot omit pre-printed text, whereas rule-stated requirements depend on the model generating them correctly. This is a new compliance axis.

**From V-03**: The axis states "Floor language is unconditional in body but introduced by a conditional section label." C-15 tests the floor declaration sentence itself. It doesn't test whether a conditional section label governs the section that contains the declaration. A floor body that reads "is always acceptable and is the safe floor" can still be framed conditionally if it lives under a heading like "When evidence is uncertain:" — the section label re-imposes the conditional frame C-15 prohibits at the sentence level.

These become **C-16** and **C-17**. Formula updates to `/9`.

---

# Quest Score Rubric — corps-achievements
**Version**: v4 (2026-03-17)

## What Changed in v4

**2 new aspirational criteria** extracted from Round 3 excellence signals:

- **C-16 (Structural compliance embedding)** — from V-02's pre-printed template skeleton. C-12 through C-15 test whether consequence clause, evasion path, and floor declaration are *present*. C-16 tests whether they are *structurally embedded* in a template skeleton as pre-printed text the model fills around, rather than rule-stated text the model must generate. Rule-stated requirements are generative; template-embedded requirements are structural. A prompt passes C-16 only if compliance-critical text is pre-printed in the skeleton — not if it is required by instruction alone.

- **C-17 (Section-label unconditional consistency)** — from V-03's "unconditional body, conditional section label" pattern. C-15 tests the floor declaration sentence. C-17 tests that no conditional section label or trigger phrase governs the section, block, or callout containing the floor declaration. A floor that reads "always acceptable and is the safe floor" under a heading labeled "When evidence is uncertain:" fails C-17 even if the sentence itself passes C-15. The conditional frame from the label contaminates the declaration regardless of the body's phrasing.

**Scoring formula updated**: `aspirational_pass / 9 * 10` (was `/7`). Max composite remains 100.

---

## Tiers

| Tier | Criteria | Points | Formula |
|------|----------|--------|---------|
| Essential | C-01 – C-05 | 60 | `pass/5 × 60` |
| Recommended | C-06 – C-08 | 30 | `pass/3 × 30` |
| Aspirational | C-09 – C-17 | 10 | `pass/9 × 10` |
| **Total** | | **100** | |

## Scoring Formula

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/9 × 10)
```

| Score | Grade |
|-------|-------|
| 100 | Platinum |
| 90–99 | Gold |
| 75–89 | Silver |
| < 75 | Bronze |

---

## Criteria

### Essential (C-01 – C-05)

**C-01 — One state per achievement**
Each achievement entry carries exactly one state value: EARNED, IN-PROGRESS, or LOCKED. Multi-state rows, ambiguous state, or missing state fail. Applies to both table and prose output formats.

**C-02 — Falsified named as honesty signal**
The Falsified achievement is present as a named entry. Its description frames falsification as evidence of investigative rigor ("followed evidence over assumptions" or equivalent), not as failure or absence.

**C-03 — Artifact-grounded classification**
State assignments cite source artifacts from Step 1 by namespace or skill. EARNED entries cite a specific artifact; IN-PROGRESS entries cite the partially-completed artifact or its count. Classification that cannot be traced to an artifact fails.

**C-04 — In-progress shows numeric progress**
IN-PROGRESS achievements express progress in `n of m` form (e.g., "3 of 5 namespaces covered"). Qualitative-only descriptions ("partially done", "underway") fail.

**C-05 — Next recommended action is specific**
Step 4 (or equivalent) names the next skill, the artifact it produces, and the achievement(s) it advances. Generic instructions ("continue the investigation") fail.

---

### Recommended (C-06 – C-08)

**C-06 — All 7 categories represented**
Every achievement category appears in the output. Categories with no earned or in-progress achievements are listed as LOCKED or explicitly noted as empty. Omitting a category fails.

**C-07 — Earned achievements carry dates**
EARNED entries include the date on which the achievement was earned. Date format may vary; absence of a date on an EARNED entry fails.

**C-08 — Locked achievements state unlock conditions**
LOCKED entries specify the concrete unlock condition: the artifact type, artifact count, or action required. "Not yet unlocked" without specifics fails.

---

### Aspirational (C-09 – C-17)

**C-09 — Maturity synthesis before classification**
A narrative synthesis of artifact maturity appears before (or as a required step preceding) the achievement table. Jumping directly from scan to table without synthesis fails.

**C-10 — Falsified framed as positive signal**
The Falsified entry uses invitational or constructive language ("reveals", "demonstrates", "signals rigor") rather than neutral inventory language. Neutral framing ("Falsified: not yet earned") fails.

**C-11 — State-column isolation**
The achievement table contains a dedicated, isolated State column whose sole content is one of the three state values. State embedded in prose cells or mixed with evidence text fails.

**C-12 — Consequence clause present for Falsified**
The Falsified framing rule includes an explicit consequence clause stating that incorrect framing (as absence, failure, or lack of evidence) fails the requirement. Rules without a consequence clause fail.

**C-13 — Escape hatch / evidence fallback instruction**
The prompt includes an explicit fallback instruction specifying what evidence is acceptable when direct Falsified evidence is uncertain or partially present. No fallback instruction fails.

**C-14 — Consequence clause names specific canonical evasion path**
The consequence clause required by C-12 names at least one specific canonical evasion surface within itself — the exact form of violation the rule is designed to foreclose (e.g., "including as a closing reflection"). A consequence clause that states only the general prohibition ("framing as absence fails") without naming a specific surface fails C-14.

**C-15 — Fallback declared as unconditional minimum**
The escape hatch required by C-13 is declared as an unconditional positive minimum: "always acceptable" or equivalent, standing alone without a conditional trigger governing it. A fallback introduced by "when evidence is uncertain" or any conditional clause fails, even if the fallback sentence itself uses unconditional language.

**C-16 — Structural compliance embedding**
Compliance-critical text — consequence clause, canonical evasion surface, and floor declaration — is pre-printed in the template skeleton as text the model fills placeholders around, not rule-stated text the model must generate. A prompt that requires these elements by instruction alone (however clearly) fails C-16. Only structural embedding — pre-printed cells, pre-printed sentences in a scaffold — passes.

**C-17 — Section-label unconditional consistency**
The section, block, callout, or subsection containing the floor declaration carries no conditional label or trigger phrase. A floor declaration that reads "always acceptable and is the safe floor" fails C-17 if it appears under a heading or label that introduces a condition (e.g., "When evidence is uncertain:", "If Falsified is ambiguous:"), regardless of whether the declaration sentence itself passes C-15. The conditional frame from the label contaminates the declaration.
