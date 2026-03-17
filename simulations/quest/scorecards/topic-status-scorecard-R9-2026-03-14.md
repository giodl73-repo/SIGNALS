## Scorecard: `topic:status` — Round 9, Rubric v9 (max 225)

### Common Baseline (C-01 – C-31): All 5 variants PASS — 210/225

All R9 variants inherit the full R8 body unchanged. Every criterion from Essential through Tier 7 passes across the board.

---

### Tier 8 Differential (C-32, C-33, C-34)

#### C-32 — Named-exit labeling: **ALL PASS**

All five variants carry named exits at the branch declaration site:
- V-01/V-02/V-04: inline prose `Exit A -- file absent:` / `Exit B -- topic not registered:`
- V-03/V-05: GUARD contract fields `Exit A -- file absent ->` / `Exit B -- topic not registered ->`

V-05 repair confirmed: numbered `(1)` / `(2)` GUARD entries replaced with named exits.

#### C-33 — Preamble architectural invariant declaration: **ALL PASS**

All five preamble blocks precede the guard mechanism and name the structural property. V-02's generic form (`PHASE 2 implements the dual-axis exit as an architectural invariant`) names "dual-axis exit" by description — sufficient for C-33. V-05 transcription error repaired: erroneous `(C-31)` citation on dual-axis line is absent.

#### C-34 — Axis-enumerated invariant declaration: **V-01/V-03/V-04/V-05 PASS — V-02 FAIL**

| Variant | Preamble form | C-34 |
|---------|--------------|------|
| V-01 | Canonical: `file-absent and topic-absent are structurally distinct stop conditions with distinct messages` | PASS |
| V-02 | `PHASE 2 implements the dual-axis exit as an architectural invariant` — no axes named | **FAIL** |
| V-03 | Canonical (identical to V-01) | PASS |
| V-04 | Canonical + supplementary per-axis trigger sentences | PASS |
| V-05 | Canonical + C-31/C-29 preamble annotations (different structural contexts) | PASS |

---

### Final Scores

| Rank | ID | C-32 | C-33 | C-34 | Score |
|------|----|------|------|------|-------|
| T-1 | V-01 | PASS | PASS | PASS | **225/225** |
| T-1 | V-03 | PASS | PASS | PASS | **225/225** |
| T-1 | V-04 | PASS | PASS | PASS | **225/225** |
| T-1 | V-05 | PASS | PASS | PASS | **225/225** |
| 5 | V-02 | PASS | PASS | FAIL | **220/225** |

**C-34 isolation confirmed:** V-01 (225) vs V-02 (220) — clean 5-point gap. Property-name alone (`architectural invariant`) satisfies C-33 but not C-34. Axis-complete canonical form is independently necessary.

**C-32 form-agnosticism confirmed:** Inline prose (V-01) and GUARD contract fields (V-03/V-05) both satisfy C-32.

---

### Excellence Signals

1. **Canonical sentence sufficiency** — single-line axis-complete preamble is minimum-sufficient for C-34; elaboration is additive but not required
2. **C-32 form-agnosticism** — branch-level name at declaration site is the criterion gate regardless of prose vs. GUARD-field structure
3. **Supplementary per-axis trigger characterization (V-04)** — explicit trigger sentences after the canonical declaration are C-34-compatible; candidate Tier 9 criterion for per-axis trigger sentence characterization beyond what axis-name alone conveys
4. **Three-site invariant echo (V-05)** — preamble + GUARD entry names + OUTPUT block echo; invariant verifiable from any single site independently; candidate Tier 9 criterion for multi-site invariant declaration chain

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["Canonical sentence sufficiency confirmed: single-line axis-complete preamble is minimum-sufficient for C-34 without elaboration; supplementary per-axis trigger sentences are C-34-compatible but not necessary", "C-32 form-agnosticism confirmed: named exit labels satisfy C-32 in inline execution prose and in GUARD contract fields -- branch-level name at declaration site is the criterion gate regardless of surrounding structural form", "Supplementary per-axis trigger characterization in preamble (V-04): explicit trigger sentences after canonical declaration are C-34-compatible and represent a candidate Tier 9 criterion separating canonical-axis-name from explicit-trigger-sentence per axis", "Three-site invariant echo (V-05): dual-axis invariant declared at preamble (C-33/C-34), named in GUARD entries (C-32), and echoed in OUTPUT block -- invariant verifiable from any single site independently; candidate Tier 9 criterion for multi-site invariant declaration chain"]}
```
n dual-axis line is absent; additional sentences reference other criteria in different structural contexts | **PASS** |

**C-33: PASS — all five variants. +5 pts each.**

V-05 transcription repair confirmed: the R8 error (`dual-axis exit (C-31)`) has been removed.
Additional sentences in V-05 preamble reference C-31 and C-29 in different structural contexts
(register rows, stale evidence) — they do not misattribute the dual-axis criterion.

---

#### C-34 — Axis-enumerated invariant declaration

C-34 requires the C-33-compliant preamble to (1) name both axes, (2) characterize each trigger,
(3) assert structural distinctness, (4) assert distinct messages. Canonical sufficient form:
`"PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct stop conditions
with distinct messages"`.

| Variant | Preamble form | Axes named | Triggers | Distinctness | Messages | C-34 |
|---------|--------------|------------|----------|--------------|----------|------|
| V-01 | Canonical single-line | file-absent, topic-absent YES | By axis-name (sufficient per canonical) YES | "structurally distinct" YES | "with distinct messages" YES | **PASS** |
| V-02 | `PHASE 2 implements the dual-axis exit as an architectural invariant.` | Neither axis named NO | Not characterized NO | Not asserted NO | Not asserted NO | **FAIL** |
| V-03 | Canonical single-line (identical to V-01) | YES | YES | YES | YES | **PASS** |
| V-04 | Canonical single-line + supplementary per-axis trigger sentences | YES | Canonical form + explicit trigger sentences YES | YES | YES | **PASS** |
| V-05 | Canonical single-line + C-31/C-29 preamble annotations | YES | By axis-name YES | YES | YES | **PASS** |

**C-34: V-01 PASS, V-02 FAIL, V-03/V-04/V-05 PASS.**

V-02 deliberately withholds C-34: "dual-axis exit as an architectural invariant" names the
structural property but provides no axis enumeration. C-33 and C-34 are independently necessary:
property-name alone satisfies C-33; axis-complete canonical form is additionally required for C-34.

---

### Per-Variant Scorecard

#### V-01 — Canonical preamble, minimum delta from R8 V-04

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32 | 5/5 | PASS |
| Tier 8 | C-33 | 5/5 | PASS |
| Tier 8 | C-34 | 5/5 | PASS |
| **Total** | | **225/225** | **34/34** |

Hypothesis confirmed: replacing R8 V-04's multi-sentence criterion-citing preamble with the
single canonical declaration moves the variant from 220 to 225. The preamble line is the sole
delta; all other structure is unchanged. C-34 gap closed by minimum structural change.

---

#### V-02 — C-34 withheld (isolation test)

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32 | 5/5 | PASS |
| Tier 8 | C-33 | 5/5 | PASS |
| Tier 8 | **C-34** | **0/5** | **FAIL** |
| **Total** | | **220/225** | **33/34** |

Isolation confirmed: `PHASE 2 implements the dual-axis exit as an architectural invariant`
passes C-33 (structural property named) but fails C-34 (no axis names, no trigger
characterization, no distinctness assertion). The 5-point delta between V-01 (225) and V-02
(220) proves C-34 is independently necessary beyond C-33.

---

#### V-03 — Lifecycle emphasis, named GUARD exits + canonical preamble

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32 | 5/5 | PASS |
| Tier 8 | C-33 | 5/5 | PASS |
| Tier 8 | C-34 | 5/5 | PASS |
| **Total** | | **225/225** | **34/34** |

C-32 form-agnosticism confirmed: `Exit A -- file absent ->` inside a GUARD contract field
satisfies C-32 identically to the inline prose form in V-01. GUARD field provides a bonus:
each named exit is verifiable from the contract declaration alone without reading the execution
prose body beneath the phase block.

---

#### V-04 — Canonical preamble + named exits + trigger characterization + inertia framing

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32 | 5/5 | PASS |
| Tier 8 | C-33 | 5/5 | PASS |
| Tier 8 | C-34 | 5/5 | PASS |
| **Total** | | **225/225** | **34/34** |

Supplementary trigger characterization is C-34-compatible: adding per-axis trigger sentences
(`File-absent trigger: strategy.md not present on disk...` / `Topic-absent trigger: strategy.md
present but {topic} has no registered planned signals...`) after the canonical declaration does
not confound C-34. The canonical sentence is sufficient; supplementary sentences are additive.
Since V-01 and V-04 both score 225, trigger characterization is a candidate Tier 9 embryo.

---

#### V-05 — Lifecycle + canonical preamble + named GUARD exits + multi-site + R8 transcription repair

| Tier | Criteria | Points | Result |
|------|----------|--------|--------|
| Essential | C-01–C-04 | 60/60 | 4/4 PASS |
| Recommended | C-05–C-07 | 30/30 | 3/3 PASS |
| Aspirational | C-08–C-12 | 25/25 | 5/5 PASS |
| Tier 2 | C-13–C-16 | 20/20 | 4/4 PASS |
| Tier 3 | C-17–C-19 | 15/15 | 3/3 PASS |
| Tier 4 | C-20–C-22 | 15/15 | 3/3 PASS |
| Tier 5 | C-23–C-25 | 15/15 | 3/3 PASS |
| Tier 6 | C-26–C-28 | 15/15 | 3/3 PASS |
| Tier 7 | C-29–C-31 | 15/15 | 3/3 PASS |
| Tier 8 | C-32 | 5/5 | PASS |
| Tier 8 | C-33 | 5/5 | PASS |
| Tier 8 | C-34 | 5/5 | PASS |
| **Total** | | **225/225** | **34/34** |

R8 V-05 repair fully confirmed: (1) numbered `(1)` / `(2)` GUARD entries replaced with named
exits `Exit A -- file absent ->` / `Exit B -- topic not registered ->` — C-32 PASS; (2)
erroneous `(C-31)` citation on dual-axis preamble line removed — C-34 clean. V-05 is the
maximum-auditability variant: the dual-axis invariant is declared at three structural sites
simultaneously — preamble (C-33/C-34), GUARD entry names (C-32), and OUTPUT block echo
(`file-absent and topic-absent exits are structurally distinct with distinct messages`). No
current criterion scores the three-site pattern; it exceeds all existing Tier 8 requirements.

---

### Ranking

| Rank | ID | Score | Differentiator |
|------|----|-------|----------------|
| T-1 | V-01 | 225/225 | Minimum delta — canonical preamble replaces R8 V-04 multi-sentence form |
| T-1 | V-03 | 225/225 | Lifecycle GUARD — named exits in contract fields, canonical preamble |
| T-1 | V-04 | 225/225 | Canonical preamble + supplementary trigger characterization + inertia framing |
| T-1 | V-05 | 225/225 | Three-site invariant declaration; transcription repair; maximum auditability |
| 5 | V-02 | 220/225 | C-34 withheld — confirms property-name alone is insufficient for axis enumeration |

---

### C-34 Isolation Confirmed

V-01 scores 225 and V-02 scores 220 — clean 5-point gap. Preamble sentence `PHASE 2 implements
the dual-axis exit as an architectural invariant` satisfies C-33 (property named) but fails C-34
(no axis names, no trigger characterization, no distinctness assertion). Axis-complete canonical
form is independently necessary. C-33 ⊄ C-34 confirmed.

### C-32 Form-Agnosticism Confirmed

V-01 (inline prose named exits) and V-03/V-05 (GUARD contract field named exits) all score 225.
C-32 evaluates the presence of a branch-level declared name at the declaration site; surrounding
structural form (prose vs. contract field) is not part of the criterion gate.

---

### Excellence Signals (from top-scoring variants)

**Signal 1 — Canonical sentence sufficiency for C-34**
Single-line declaration `PHASE 2 dual-axis exit: file-absent and topic-absent are structurally
distinct stop conditions with distinct messages` satisfies all four C-34 requirements without
elaboration. V-01 achieves 225 with this as the sole delta from R8 V-04. Canonical form is the
minimum-sufficient implementation; elaboration is additive, not required.

**Signal 2 — C-32 form-agnosticism: named labels satisfy regardless of surrounding structure**
V-01 names exits in inline execution prose; V-03 and V-05 name exits in GUARD contract fields.
All three satisfy C-32. The branch-level declared name is the unit of compliance. Implication:
a future criterion could add a position-within-structure dimension (analogous to C-26 left-edge
rule) to distinguish GUARD-field declaration (higher auditability) from inline-prose declaration.

**Signal 3 — Supplementary per-axis trigger sentences as Tier 9 embryo (V-04)**
V-04 adds `File-absent trigger: strategy.md not present on disk -- output unquantifiable-exposure
message and stop immediately` / `Topic-absent trigger: strategy.md present but {topic} has no
registered planned signals -- output topic-specific stop message before PHASE 3` after the
canonical declaration. These are C-34-compatible (canonical form present; supplements additive).
In R9 they carry no scoring weight but are structurally present in the highest-structure prose
variant. Candidate Tier 9 criterion: explicit per-axis trigger sentence characterization beyond
what axis-name alone conveys.

**Signal 4 — Three-site invariant echo as auditability maximization pattern (V-05)**
V-05 declares the dual-axis invariant at three structurally independent sites: preamble block
(C-33/C-34), GUARD entry names (C-32), and PHASE 2 OUTPUT block echo (`file-absent and
topic-absent exits are structurally distinct with distinct messages`). A scorer can verify the
invariant from any single site without consulting the others. No current criterion requires
more than two sites (preamble + implementation). Candidate Tier 9 criterion: multi-site
invariant echo — invariant declared at preamble, named at execution branch, confirmed at output,
collapsing all three structural tiers into a single verifiable chain.

---

```json
{"top_score": 225, "all_essential_pass": true, "new_patterns": ["Canonical sentence sufficiency confirmed: single-line axis-complete preamble is minimum-sufficient for C-34 without elaboration; supplementary per-axis trigger sentences are C-34-compatible but not necessary", "C-32 form-agnosticism confirmed: named exit labels satisfy C-32 in inline execution prose and in GUARD contract fields -- branch-level name at declaration site is the criterion gate regardless of surrounding structural form", "Supplementary per-axis trigger characterization in preamble (V-04): explicit trigger sentences after canonical declaration are C-34-compatible and represent a candidate Tier 9 criterion separating canonical-axis-name from explicit-trigger-sentence per axis", "Three-site invariant echo (V-05): dual-axis invariant declared at preamble (C-33/C-34), named in GUARD entries (C-32), and echoed in OUTPUT block -- invariant verifiable from any single site independently; candidate Tier 9 criterion for multi-site invariant declaration chain"]}
```
