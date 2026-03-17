# quest:score — signal-setup — Round 11

**Rubric:** v10 (C-01 through C-30, denominator A=22)
**Scoring:** PASS=1, PARTIAL=0.5, FAIL=0 · Score = raw/30 × 100

---

## V-01 Full Scorecard: Inertia as Named Adversary

*Full spec text provided — scored from text.*

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | GATE 1 reads CLAUDE.md before any write; explicitly checks existence |
| C-02 | **PASS** | GATE 2 shows preview in fenced code block before file modification |
| C-03 | **PASS** | GATE 3 asks "Append this Signal section to CLAUDE.md?" and waits |
| C-04 | **PASS** | GATE 2 specifies nine namespace skills plus inertia rule in written content |
| C-05 | **PASS** | GATE 1A detects existing Signal section and terminates without writing |

**Essential: 5/5 — ALL PASS ✓**

---

### Recommended Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | GATE 2 content spec: "The inertia rule: 'When enough signals exist, the topic tells you you're ready'" |
| C-07 | **PASS** | GATE 6 offers `.github/copilot-instructions.md` extension with rationale |
| C-08 | **PASS** | GATE 5 reports write completion; GATE 1A, GATE 3A, GATE 6-Decline each report outcome with explicit status |

**Recommended: 3/3 — ALL PASS ✓**

---

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **PASS** | GATE 4: "The written content must be byte-identical to the previewed content. No additions, no reformatting, no drift." |
| C-10 | **PASS** | GATE 1B handles missing CLAUDE.md with create-or-abort option; no silent failure |
| C-11 | **PASS** | 10 named gates (GATE 1 through GATE 6-Decline); every phase is a delimited checkpoint |
| C-12 | **PASS** | GATE 1A (already configured) and GATE 1B (missing file) are both promoted as `###`-headed sub-gates |
| C-13 | **PASS** | "## Why This Matters" opens before GATE 1; inertia framed as why setup matters before any procedural step |
| C-14 | **PASS** | GATE 3A: "Inertia is still uncontested at the planning stage… Signal would have asked it automatically… It will not be there the next time you open this workspace." Names what was given up. |
| C-15 | **PASS** | GATE 1A: "Inertia has a named opponent in this workspace, and that opponent shows up before your first message, every session." Names active benefit, not just "no changes needed." |
| C-16 | **PASS** | Preamble: "inertia wins by default… You are choosing a side." GATE 1A: "Inertia has a named opponent." GATE 3A: "Inertia is still uncontested." Adversary framing is not preamble-only. |
| C-17 | **PASS** | Preamble: "Setup happens once. The reminder lives forever." + "automatically loaded every session without you having to remember." Both stakes and mechanism present. |
| C-18 | **PASS** | GATE 3A: "not be there the next time you open this workspace." GATE 1B-Abort: "at the planning stage — the moment before a spec is drafted and direction is locked." Future moment named. |
| C-19 | **PASS** | Both Signal-absent exits (GATE 1B-Abort and GATE 3A) carry planning-stage future-moment framing. Neither delivers weaker consequence than the other. |
| C-20 | **PASS** | GATE 1A: "CLAUDE.md loads automatically at the start of every Claude Code session — which means the inertia question is already present in your context without you having to remember." Mechanism named explicitly. |
| C-21 | **PARTIAL** | GATE 6-Decline is truncated at "The implementation phase — when you are writing." Implementation-phase vocabulary is present but consequence sentence is incomplete; cannot confirm full path-specific anchor. |
| C-22 | **PARTIAL** | GATE 3A: planning-stage vocabulary ("spec is committed," "feature direction is locked"). GATE 6-Decline: "implementation phase" visible. Vocabulary sets are non-overlapping but GATE 6-Decline is truncated; full pass not confirmable. |
| C-23 | **PASS** | GATE 1B-Abort: "at the planning stage" (explicit label). GATE 3A: "at the planning stage" (explicit label). GATE 6-Decline: "The implementation phase" (explicit label, visible before truncation). |
| C-24 | **PASS** | Copilot already-configured inline: "inertia question is present during Copilot suggestions at the implementation phase — when you are writing function bodies and endpoint signatures, not only when planning." Tool-local vocabulary, not generic reuse. |
| C-25 | **PARTIAL** | GATE 1A, GATE 1B, GATE 3A, GATE 6A follow parent-number + letter convention. GATE 1B-Abort and GATE 6-Decline use word suffixes instead of letter slots. Mixed convention; not uniformly machine-parseable by identifier alone. |
| C-26 | **PASS** | GATE 6A (write Copilot) and GATE 6-Decline are `###`-headed sub-gates. Optional-extension confirmation is not a trailing paragraph in GATE 6 body. |
| C-27 | **PASS** | All gate and sub-gate boundaries are `##` or `###` headings. Bold appears only in GATE 1B option labels ("**Create CLAUDE.md with Signal section**", "**Abort**") inside a bullet list — option presentation, not gate boundary. |
| C-28 | **PASS** | Primary detection (GATE 1A, GATE 1B) promoted to sub-gates. Secondary detection (Copilot existing) left inline with explicit annotation. Scope boundary recognized and applied. |
| C-29 | **PASS** | GATE 1: three branches, all with gate IDs. GATE 1B: two branches with IDs. GATE 3: two branches with IDs. GATE 6: two branches with IDs. All routing blocks are contiguous (condition, destination) pairs. |
| C-30 | **PASS** | Copilot inline detection: "(No sub-gate needed — this is a detection skip path in an optional-extension gate, not a confirmation checkpoint.)" Annotation is present; intent is explicit. |

**Aspirational: 19 PASS + 3 PARTIAL + 0 FAIL = 20.5/22**

---

### V-01 Composite

| Tier | Points | Max | % |
|------|--------|-----|---|
| Essential | 5.0 | 5 | 100% |
| Recommended | 3.0 | 3 | 100% |
| Aspirational | 20.5 | 22 | 93.2% |
| **Total** | **28.5** | **30** | **95** |

---

## V-02 through V-05: Projected Scores

*No full spec text provided for these variations. Scores are projections from axis hypotheses.*

### V-02: Formal/Technical Imperative

**Axis:** Stripped-down imperative prose for cleaner gate boundaries.

Projected strengths: C-27, C-29 (clean structure reduces pseudo-gate formatting risk). Projected weaknesses: C-13, C-16, C-17 likely thinner; imperative register tends toward instruction lists that elide motivational preamble. C-21, C-22, C-23 uncertain — imperative brevity may compress consequence language below the phase-indexed threshold. C-18, C-19 probably pass at surface level but may lose the visceral future-moment specificity.

**Projected score: ~79** | All essential: likely PASS

---

### V-03: Lifecycle Emphasis — Verbose Gate Treatment

**Axis:** Maximum prose per gate; forces non-overlapping consequence vocabulary.

Known from rubric intro: passes C-12 under C-28 scope rules (inline secondary detection is valid when annotated). Verbose treatment makes C-21, C-22, C-23 high-probability passes. C-18, C-19 likely strong. Risk: verbose bodies without a formal routing discipline may produce prose-embedded routing (C-29 partial) or heading-less condition splits (C-27 partial). C-30 depends on whether inline paths are annotated.

**Projected score: ~86** | All essential: likely PASS

---

### V-04: Inertia Framing + Conversational Register

**Axis:** Adversary framing in conversational prose.

Strong on C-13, C-16, C-17 — conversational register can carry adversary framing fluently. The hypothesis itself flags structural risk: "requires explicit structural compensation to avoid C-27/C-29 penalties." Conversational continuity resists heading-based gate boundaries; routing tends to be embedded in flowing prose without explicit gate IDs. C-25 sub-gate naming in conversational style likely inconsistent. C-29 is the critical risk — conversational routing omits gate IDs or names destinations implicitly ("as described above").

**Projected score: ~75** | All essential: likely PASS

---

### V-05: Table-Driven Gate Index + Lifecycle Emphasis

**Axis:** Pre-prose gate index table + verbose gate bodies.

Table index directly delivers C-11 (machine-readable phase structure), C-25 (identifier encoding visible in table), C-29 (table rows as contiguous routing). Verbose bodies deliver C-22, C-23. This combination addresses the two hardest structural criteria from opposite ends — the index for navigability, the bodies for consequence depth. Risk: combined approach may produce a long spec where some gates satisfy table index but trail off in consequence language; C-21, C-24 depend on execution discipline in the extension gates. Likely the strongest overall structural design.

**Projected score: ~90** | All essential: likely PASS

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | **V-01** | **95** | Full text scored; near-complete pass; 3 partials from truncation/naming |
| 2 | V-05 | ~90 | Table index resolves C-11/C-25/C-29 structurally; verbose bodies cover consequence depth |
| 3 | V-03 | ~86 | Verbose treatment strong; routing discipline uncertain without text |
| 4 | V-02 | ~79 | Clean structure but motivational thinness hurts consequence criteria |
| 5 | V-04 | ~75 | Adversary framing strong; conversational register structurally fragile at C-27/C-29 |

---

## Excellence Signals from V-01

**1. Adversary recurrence, not adversary introduction.**
Inertia is not introduced in the preamble and then dropped. The language "Inertia has a named opponent," "Inertia is still uncontested," "Inertia is present… and will remain uncontested" follows the user through every gate that matters. The adversary framing is a *shared vocabulary* across the spec, not a rhetorical warm-up.

**2. Routing block discipline: one location, all branches, explicit IDs.**
Every gate with branching has a **Routing:** block listing every branch as `(condition → GATE ID)`. No condition is mentioned only in prose. No destination is named without its gate identifier. The routing block is the only place routing logic lives — not split between opening prose and a trailing note.

**3. C-28 annotation as documented architecture, not compliance footnote.**
"(No sub-gate needed — this is a detection skip path in an optional-extension gate, not a confirmation checkpoint.)" is placed immediately after the inline treatment. This phrasing does three things: names the decision, names the reason, and identifies the rubric category the decision operates in. A reviewer reading only the annotation knows exactly why this path is inline and under which conditions it would need promotion.

**4. Symmetric opposition vocabulary across decline/success pairs.**
GATE 3A: "Inertia is still uncontested." GATE 5: "Inertia has a standing opponent here." The decline and success outcomes are not independent messages — they are antonyms in the same metaphor. This makes the stakes of the confirmation gate legible without re-reading the preamble.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["leaf-gate explicit terminator — 'End here.' at each dead-end gate disambiguates leaf gates from those with implicit continuation; scoring cannot currently penalize a spec that omits it, leaving ambiguous leaf gates undetectable", "symmetric opposition vocabulary pairs — decline gates use 'uncontested' where success gates use 'named opponent', anchoring both messages to the same adversary metaphor; a spec with asymmetric pairs (decline names inertia, success does not) cannot be penalized under current criteria despite losing the rhetorical coherence that makes the stakes legible at a glance"]}
```
