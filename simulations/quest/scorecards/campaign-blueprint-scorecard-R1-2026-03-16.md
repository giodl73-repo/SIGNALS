## campaign-blueprint — Scoring Round 1

---

### Criterion Evaluation

#### V-01 — Role Sequence Axis

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | All three artifacts explicitly produced with write instructions |
| C-02 | PASS | All three canonical paths stated exactly |
| C-03 | PASS | 4-line campaign brief at top is an explicit shared contract; "do not deviate from it" |
| C-04 | PASS | "grounded in the spec just written" and "recommended option from the proposal" establish read-before-write dependencies |
| C-05 | PASS | Spec sections listed; proposal has three options min + pros/cons/risk/effort + recommendation; pitch has three versions with hook/what/why/CTA |
| C-06 | PASS | "Do not re-open design questions the spec resolved" is explicit |
| C-07 | PARTIAL | Exec leads with recommended option (pass); maker must be jargon-free (pass); dev version referencing technical design from spec is absent |
| C-08 | PASS | CAMPAIGN SETUP opens; CAMPAIGN CLOSE lists artifacts, signals, open questions |
| C-09 | PARTIAL | Role differentiation creates natural scope separation but no explicit anti-duplication instruction or conviction-building check |
| C-10 | PASS | Scout-requirements → spec, scout-feasibility → proposal, scout-positioning → pitch |

**Essential**: 5/5 = 60 | **Recommended**: 2.5/3 = 25 | **Aspirational**: 1.5/2 = 7.5
**Composite: 92.5** — Golden ✓

---

#### V-02 — Output Format Axis

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | All three artifacts produced |
| C-02 | PASS | All three paths specified |
| C-03 | PARTIAL | No shared brief or topic identity lock; format enforces field coverage but not topic consistency |
| C-04 | PASS | "Each artifact is written to disk before the next begins" — explicit |
| C-05 | PASS | Spec table has all five required sections; proposal table has all six required fields; pitch table has all three versions with all four fields |
| C-06 | PASS | "three reasons grounded in the spec" in recommendation |
| C-07 | PARTIAL | Pitch table has three versions; exec hook is "ROI / outcome first" (not explicitly tied to recommended option); dev version says "Tool / capability first" but does not say "reference technical design from spec" |
| C-08 | PARTIAL | CAMPAIGN SUMMARY table closes; no opening header naming topic and listing artifacts to be produced |
| C-09 | FAIL | Format focus only; no narrative arc or duplication prevention instruction |
| C-10 | PASS | Scout signals referenced per artifact with conditional pull |

**Essential**: 4.5/5 = 54 | **Recommended**: 2/3 = 20 | **Aspirational**: 0.5/2 = 5
**Composite: 79** — Failing (C-03 essential not fully passing) ✗

---

#### V-03 — Lifecycle Emphasis Axis

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | Three artifacts with explicit WRITE and GATE per artifact |
| C-02 | PASS | All three canonical paths present |
| C-03 | PASS | "Confirm topic identity — this identity must remain consistent across all three artifacts" in PHASE 0 |
| C-04 | PASS | "GATE: Do not begin Artifact 2 until this file is written." "GATE: Do not begin Artifact 3 until this file is written." — strongest mechanism in the round |
| C-05 | PASS | Spec: all five required sections. Proposal: three options min, description/pros/cons/risk/effort, recommendation. Pitch: three versions, hook/what/why/CTA, anti-positioning. |
| C-06 | PASS | "Read the spec just written. Identify key decisions that constrain the option space." "Flag any design question the proposal had to resolve that the spec left open." |
| C-07 | PASS | "Exec version leads with the outcome of the recommended option." "Dev version references the technical design from the spec." "Maker version uses no jargon from the spec." All three sub-conditions satisfied. |
| C-08 | PASS | PHASE 0 CAMPAIGN SETUP opens; PHASE 4 CAMPAIGN CLOSE closes with full list including signal namespaces |
| C-09 | PASS | "State what conviction each version establishes that the previous artifacts did not. Note any content you nearly duplicated from spec or proposal." — explicit conviction audit and anti-duplication check in pitch FINDINGS |
| C-10 | PASS | PHASE 0 proactively globs simulations/scout/ and lists found signals; each artifact section pulls its specific signal namespace |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 2/2 = 10
**Composite: 100** — Golden ✓

---

#### V-04 — Register + Inertia Framing

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | Three artifacts with write instructions |
| C-02 | PASS | All three canonical paths |
| C-03 | PARTIAL | "Three artifacts. One topic." stated but no explicit topic identity lock; inertia baseline threads through all three but is not named as a drift-prevention mechanism |
| C-04 | PASS | "Don't start the proposal until this is done and written to disk." "Read the spec you just wrote." "Read the proposal." — explicit ordering |
| C-05 | PARTIAL | Spec has all required sections; proposal has three options + recommendation. Pitch: exec/dev/maker structure present; dev version is missing explicit "why it matters" and CTA — conversational phrasing implies but doesn't name them |
| C-06 | PASS | "Ground the recommendation in the spec's design and constraints — don't re-invent anything the spec already decided." |
| C-07 | PASS | Exec leads with inertia cost → recommended option change. Dev: "Reference the technical design from the spec." Maker: "plain language only. No spec terminology. No proposal jargon." |
| C-08 | PARTIAL | "BEFORE YOU START" sets up inertia baseline but does not name the three artifacts to be produced; WRAP UP lists artifacts and open questions |
| C-09 | PARTIAL | "Different words, same conviction" is a strong narrative directive; inertia thread creates natural non-duplication but no explicit anti-duplication check |
| C-10 | PASS | Scout-requirements, scout-feasibility, scout-positioning all referenced per artifact |

**Essential**: 4/5 = 48 | **Recommended**: 2.5/3 = 25 | **Aspirational**: 1.5/2 = 7.5
**Composite: 80.5** — Failing (C-03 and C-05 essential not fully passing) ✗

---

#### V-05 — Full Integration

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | All three artifacts with GATE per artifact |
| C-02 | PASS | All three canonical paths with GATE |
| C-03 | PASS | "Topic identity — one sentence: what feature, for whom, solving what." Setup block printed and locked before Artifact 1 begins |
| C-04 | PASS | Three explicit GATE statements, each requiring file written before next begins |
| C-05 | PASS | Spec: PURPOSE/REQUIREMENTS/DESIGN/CONSTRAINTS/OPEN QUESTIONS, all required. Proposal: three options min + do-nothing + all six fields + recommendation with three reasons. Pitch: three named versions each with Hook/What/Why/CTA plus shared anti-positioning. |
| C-06 | PASS | "Every reason must reference a spec decision or constraint — no new design work here." "Do not re-open any design question the spec resolved." |
| C-07 | PASS | Exec: leads with outcome of recommended option. Dev: "reference the technical design from the spec." Maker: "plain language only. No spec or proposal terminology." |
| C-08 | PASS | SETUP block opens with topic identity + scout signal inventory; CAMPAIGN CLOSE table lists all three artifacts with paths, scout signal consumed, open questions |
| C-09 | PARTIAL | Inertia thread + role differentiation creates strong progressive conviction, but no explicit "state what conviction each version adds" check or "note any duplication" instruction (which V-03 has) |
| C-10 | PASS | SETUP globs scout signals; each artifact section pulls its specific signal; CAMPAIGN CLOSE table logs which signal was consumed |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 1.5/2 = 7.5
**Composite: 97.5** — Golden ✓

---

### Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Composite | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|-----------|--------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PARTIAL | PASS | **92.5** | Yes |
| V-02 | PASS | PASS | PARTIAL | PASS | PASS | PASS | PARTIAL | PARTIAL | FAIL | PASS | **79** | No |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** | Yes |
| V-04 | PASS | PASS | PARTIAL | PASS | PARTIAL | PASS | PASS | PARTIAL | PARTIAL | PASS | **80.5** | No |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | **97.5** | Yes |

**Rank**: V-03 (100) > V-05 (97.5) > V-01 (92.5) > V-04 (80.5) > V-02 (79)

---

### Excellence Signals from V-03

**What made V-03 the top score:**

1. **Four-phase lifecycle (SETUP/EXECUTE/FINDINGS/AMEND) per artifact** — forces structured reflection after each artifact before the gate opens. The model can't drift because the FINDINGS step surfaces what it decided and the AMEND step names what's still unresolved.

2. **GATE keyword as a hard sequencing barrier** — "Do not begin Artifact 2 until this file is written" is unambiguous. Ordering is enforced by prohibition, not by implication.

3. **Conviction audit in pitch FINDINGS** — "State what conviction each version establishes that the previous artifacts did not" is the only instruction in the round that directly targets C-09 as a measurable output, not a side effect.

4. **Anti-duplication reflection embedded in FINDINGS** — "Note any content you nearly duplicated from spec or proposal" creates an explicit self-monitoring loop. V-03 is the only variation that catches this at execution time rather than hoping the model infers it from role assignment.

5. **Proactive scout signal discovery before writing** — PHASE 0 globs for all scout signals at campaign open and lists them. V-02, V-04 use conditional per-artifact checks; V-03 discovers the full signal inventory before any artifact begins, so each artifact can use the complete picture.

**V-03's gap** (gap that V-05 partially addressed): The lifecycle emphasis produces great self-monitoring but lacks the inertia thread (V-04/V-05) that anchors "why it matters" across all three versions. V-03 achieves C-09 through reflection; V-05 achieves it through the persistent inertia anchor. The ideal combination would have both.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["four-phase lifecycle per artifact as structured reflection loop", "GATE keyword as hard write-before-proceed sequencing barrier", "conviction audit in FINDINGS — state what each artifact adds that prior artifacts did not", "anti-duplication reflection — note content nearly duplicated from prior artifacts", "proactive scout signal glob at campaign open before any artifact begins"]}
```
