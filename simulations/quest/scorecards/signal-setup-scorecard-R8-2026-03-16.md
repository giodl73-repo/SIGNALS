# Quest Scorecard — signal-setup — Round 8

**Rubric**: v8 | **Denominator**: 16 (aspirational C-09–C-24) | **Date**: 2026-03-16

> **Note**: V-02 is truncated mid-preamble; V-03–V-05 are not present in the provided variate document. Scoring covers V-01 fully and V-02 partially.

---

## V-01 — Lifecycle Emphasis (Explicit Named Gates)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | File detection before write | **PASS** | GATE 1 reads workspace root for CLAUDE.md; GATE 6 reads copilot-instructions.md before any write |
| C-02 | Preview shown before writing | **PASS** | GATE 3 is a dedicated preview gate — displays full Signal section content before GATE 4 asks to confirm |
| C-03 | Confirmation required | **PASS** | GATE 4 explicitly asks "Append this Signal section to CLAUDE.md?" with Yes/No branch |
| C-04 | Signal section appended with skill advertising | **PASS** | Preview includes all 9 namespace shortcuts: `/scout · /draft · /review · /flow · /trace · /prove · /listen · /program · /topic` |
| C-05 | Idempotent re-run | **PASS** | GATE 2 searches for `## Signal` or `<!-- signal-setup -->` and SKIPs write with explicit reason |

**Essential gate**: ✅ All 5 pass

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Inertia rule included | **PASS** | `### Inertia Rule` block in preview with full inertia question text |
| C-07 | Copilot instructions offered | **PASS** | GATE 5–6 handle copilot-instructions.md as a distinct extension path |
| C-08 | User feedback on outcome | **PASS** | GATE 7 produces a two-column status table covering all four possible file states |

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Preview matches written output | **PASS** | GATE 3 displays the literal content; GATE 4 confirms "Append" with no drift language |
| C-10 | Handles missing CLAUDE.md gracefully | **PASS** | GATE 1 "Not found" path offers creation with explanation; GATE 3 skips to handle missing-then-created case |
| C-11 | Named gate checkpoints as explicit phase boundaries | **PASS** | Six numbered gates declared upfront with stated outcome triads; "No gate is implicit" asserted in preamble |
| C-12 | Edge-case paths promoted to first-class gates | **PASS** | Already-configured = GATE 2 (own complete treatment); missing CLAUDE.md = GATE 1 branch (own complete treatment) |
| C-13 | Skill opens with motivational preamble | **PASS** | "Why This Configuration Must Exist" section names inertia as adversary and explains why setup happens before any procedural gate |
| C-14 | Decline path names its consequence | **PASS** | GATE 1 decline: names absence of "persistent instruction in your workspace asking 'why would teams do nothing instead?'" GATE 4 decline: names "no standing instruction... to ask the inertia question" |
| C-15 | Already-configured path affirms positive consequence | **PASS** | GATE 2 SKIP: "the question 'why would teams do nothing?' is already in scope at the planning stage, every time, without manual invocation" |
| C-16 | Inertia named as adversary, not concept | **PASS** | Opening: "There is a force that wins every feature decision when no one intervenes: inertia. It is not passive." Closing: "Inertia now has a named opponent." |
| C-17 | Preamble explains temporal persistence of configuration | **PASS** | "CLAUDE.md loads at the start of every session... the configuration must persist because the question must persist" — mechanism and stakes both stated |
| C-18 | Decline path anchors consequence to a future moment | **PASS** | GATE 1: "At the planning stage — when a feature topic is open and you are deciding whether to build." GATE 4: "before the next feature topic is named and you want a structured challenge." Both name a specific future moment. |
| C-19 | Key arguments threaded through all equivalent exit gates | **PASS** | Both GATE 1 (file missing, user declines) and GATE 4 (file present, user declines) carry planning-stage future-moment framing; no Signal-absent exit delivers weaker language |
| C-20 | Already-configured gate names the persistence mechanism | **PASS** | GATE 2: "the mechanism that keeps the inertia question present is the load itself, not you remembering to ask" — names the autoload mechanism explicitly |
| C-21 | Secondary optional gates carry path-specific consequence anchors | **PASS** | GATE 6 decline: "during the implementation phase — before Copilot generates the first function body or endpoint" — vocabulary fully distinct from GATE 4's planning-stage framing |
| C-22 | Consequence anchors are phase-indexed, not tool-indexed | **PASS** | GATE 4 vocabulary: "planning stage / feature topic named / structured challenge." GATE 6 vocabulary: "implementation phase / function body / endpoint." Sets are non-overlapping and phase-native — not tool-name substitution. |
| C-23 | Explicit phase label at each decline anchor | **PASS** | GATE 1: "At the planning stage." GATE 4: "At the planning stage." GATE 6: "During the implementation phase." Phase category is named directly at every decline; inference from artifact vocabulary is not required. |
| C-24 | Secondary already-configured paths affirm tool-local consequence | **PASS** | GATE 6 already-configured SKIP: "while Copilot is generating code... When Copilot receives a prompt to implement a feature, the standing instruction... is present in its working scope." Fully Copilot-vocabulary-framed; not a reuse of GATE 2's CLAUDE.md/planning-stage language. |

### V-01 Score

| Section | Score |
|---------|-------|
| Essential (C-01–C-05) | 5/5 ✅ |
| Recommended (C-06–C-08) | 3/3 ✅ |
| Aspirational (C-09–C-24) | 16/16 |
| **Composite** | **100 / 100** |

---

## V-02 — Phrasing Register (Conversational / Descriptive)

**Status**: Truncated at line 7 of preamble. Cannot score C-01 through C-24 except C-13 (partially visible).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-13 | Skill opens with motivational preamble | **PARTIAL** | Preamble begins conversationally but is cut off before framing inertia as adversary — the core requirement. "You've installed Signal skills — a toolkit for gathering evidence before you commit to a feature. But having skills available isn't the same as having them [cut off]" Cannot confirm adversary framing, persistence argument, or why-configure rationale. |
| All other criteria | **N/A** | Document truncated — no gate structure, no write logic, no decline paths visible |

**V-02 Score**: Cannot compute. Excluded from ranking.

---

## V-03 through V-05

Not present in the provided variate document. Cannot score.

---

## Ranking

| Rank | Variation | Composite | All Essential |
|------|-----------|-----------|---------------|
| 1 | **V-01** (Lifecycle Emphasis) | **100 / 100** | ✅ |
| — | V-02 | N/A (truncated) | — |
| — | V-03–V-05 | N/A (not provided) | — |

---

## Excellence Signals — V-01

Three structural choices drove the perfect score:

**1. Outcome triad declared as meta-contract.** The preamble states "PROCEED / SKIP / EXIT" before any gate appears. This forces the reader to expect an EXIT at every gate — consequence language is not a surprise, it is a promised structural feature. Every decline path delivering named consequence feels earned rather than added.

**2. Adversary framing carried to the closing line.** The final report line ("Inertia now has a named opponent in the contexts listed above") echoes the opening adversary framing. This creates a rhetorical bracket: the skill opens by naming the enemy and closes by confirming the enemy has been named. The configured state has narrative completeness.

**3. Phase vocabulary selected before gate language was written.** GATE 4's planning-stage vocabulary ("feature topic is named," "structured challenge") and GATE 6's implementation-phase vocabulary ("function body," "endpoint") are semantically non-overlapping because they were drawn from different phases of the development timeline — not because a tool name was substituted. This is the structural move that earns C-22 and C-23 simultaneously.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
