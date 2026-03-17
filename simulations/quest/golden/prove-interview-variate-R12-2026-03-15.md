# prove-interview — Skill Body Variations — R12

**Skill:** prove-interview
**Round:** 12
**Rubric version:** v12
**Date:** 2026-03-15

---

## R12 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|-----------|----------------|------|------------|
| V-01 | Single | 0B Internal Decomposition (C-33) | When Phase 0B is split into 0B-I (constitutive thresholds) and 0B-II (margin declarations) with independent exit gates whose conditions cannot overlap, C-31 compliance becomes architecturally enforced at gate-read time: a margin cell that restates a threshold definition fails the 0B-II exit gate without requiring cross-column comparison |
| V-02 | Single | Prohibition-First Gate Clauses (C-34) | When every sub-phase exit gate opens with a PROHIBITED clause naming out-of-scope content by category before stating affirmative completion conditions, a scope violation is detectable by reading the gate text alone — no adjacent sub-phase inspection required |
| V-03 | Single | Bidirectional Audit Table (C-35) | Rendering the VERDICT MARGIN AUDIT as a mandatory two-row table (one row for the upper boundary, one for the lower) makes the structural incompleteness of a one-direction audit visually immediate — a table with one populated row is a visible format failure, not a prose omission |
| V-04 | Combined | 0B Decomposition + Prohibition Gates (C-33 + C-34) | C-33 and C-34 reinforce at the 0B level: when 0B-I and 0B-II each carry independent prohibition-first gates, the 0B-II gate clause "if your content restates a threshold definition, it has exceeded 0B-I scope" makes C-31 enforcement gate-mechanical at the sub-section level as well as the sub-phase level |
| V-05 | Combined | Full apparatus — all four new criteria + all prior late-aspirational criteria | All twelve late-aspirational criteria (C-26 through C-36) become architectural consequences: C-33 (0B-I/0B-II independent gates), C-34 (every gate prohibition-first), C-35 (bidirectional audit table in Phase 4), and C-36 (PROFILE RELEVANCE vocabulary defined in Phase 0A header and propagated through Phase 3 and Phase 4 accounting) are satisfied by structural completion rather than authorial memory |

Single-axis variations: V-01 (0B-I/0B-II independent gates), V-02 (prohibition-first gate clauses), V-03 (bidirectional audit table)
Combination variations: V-04 (C-33 + C-34 at sub-section level), V-05 (all twelve late-aspirational criteria)

New R12 territory probed:
- **0B-I / 0B-II independent gates** (V-01, V-04, V-05): each sub-section has an exit gate whose conditions are logically disjoint — satisfying 0B-I (threshold definitions present, no margin content) cannot satisfy 0B-II (margin declarations present, no threshold restatements)
- **Prohibition-first gate clauses** (V-02, V-04, V-05): gate text opens with "PROHIBITED: if your content contains [category], it has exceeded scope" before stating what must be present — scope violation is gate-readable without adjacent-phase inspection
- **Bidirectional margin audit table** (V-03, V-05): two-row synthesis table forces upper-boundary and lower-boundary statements as separate structural cells; a single-direction audit leaves one row empty, which is a visible completion failure
- **PROFILE RELEVANCE vocabulary anchored in Phase 0A** (V-05): tag vocabulary (STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL) is declared as part of the Phase 0A exit gate, making the Phase 3 evidence item format and Phase 4 accounting a forward-reference to a defined vocabulary rather than a free-text field

---

## V-01 — 0B Internal Decomposition (C-33 focus)

**Variation axis:** 0B Internal Decomposition
**Hypothesis:** R11 V-05 split Phase 0B into sub-sections 0B-I and 0B-II structurally, but the Phase 0B exit gate covered both sub-sections together. When 0B-I and 0B-II each carry their own independent exit gates — 0B-I's gate verifies constitutive threshold definitions and explicitly rejects any margin content; 0B-II's gate verifies margin declarations and explicitly rejects any content that restates an adjacent level's constitutive definition — C-31's "margin must not restate adjacent definition" requirement becomes mechanically enforced by the 0B-II gate. An evaluator reads the 0B-II exit gate, checks each margin cell against the prohibition, and records pass or fail without opening the 0B-I section.

---

You are running prove-interview for the topic: {topic}

Execute in named phases. Phase 0 is decomposed into three independently-gated sub-phases with non-overlapping scope. Phase 0B is further decomposed into two independently-gated sub-sections (0B-I and 0B-II) with non-overlapping scope. Do not advance past any gate until it passes.

---

**PHASE 0A — SEQUENCE + SIGNAL COMMITMENT**

Scope: tier sequence rationale and signal categories only. Verdict threshold definitions and margin declarations are out of scope for this sub-phase.

Entry gate: none.
Exit gate (0A only): tier sequence declared with one adjacency block per consecutive pair — each block names what the preceding tier establishes and what the following tier's departure is measured against, with a contrast-lost statement; signal categories enumerated with per-category rationale; no verdict threshold or margin content present.

Tier sequence: [list tiers in order]

For each consecutive pair:

ADJACENCY [Tier A → Tier B]
Tier A establishes: [what posture, evidence type, or baseline Tier A's interview produces]
Tier B departure measured against: [what becomes interpretable in Tier B's evidence because Tier A ran first]
Contrast lost if reversed: [one sentence]

Signal categories sought: [enumerate which of RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION and why each is needed for {topic}]

---

**PHASE 0B — VERDICT DECISION FUNCTION WITH MARGINS**

Phase 0B is split into two independently-gated sub-sections. Complete 0B-I before 0B-II. Each sub-section has its own exit gate whose conditions do not overlap: satisfying the 0B-I gate does not satisfy the 0B-II gate and vice versa.

Entry gate (0B): Phase 0A exit gate passed.

---

**PHASE 0B-I — CONSTITUTIVE THRESHOLD DEFINITIONS**

Scope: constitutive evidence-configuration definitions for each verdict level only. Margin-boundary declarations belong to 0B-II and are out of scope here.

Exit gate (0B-I only): every verdict level row carries a constitutive evidence-configuration definition naming types, tier sources, and re-weighting outcomes; no row restates the level name; no margin-boundary content (deciding factor at adjacent-level boundaries) is present in this sub-section. Completing 0B-II does not pass this gate.

| Verdict level | Constitutive threshold — evidence configuration that produces this classification |
|---------------|-----------------------------------------------------------------------------------|
| STRONG VALIDATION | |
| VALIDATION | |
| MIXED | |
| INVALIDATION | |
| STRONG INVALIDATION | |

Replace blank cells with {topic}-specific constitutive definitions. A definition that restates the level name fails the exit gate. A cell that names the deciding boundary factor belongs in 0B-II and fails this gate.

---

**PHASE 0B-II — MARGIN-BOUNDARY DECLARATIONS**

Scope: deciding evidence factor at each adjacent-level boundary only. Constitutive threshold definitions belong to 0B-I — do not restate them here. Reference the 0B-I table by level name only.

Entry gate (0B-II): Phase 0B-I exit gate passed.
Exit gate (0B-II only): every boundary row carries a margin declaration naming the evidence property decisive at that boundary; no margin cell restates either adjacent level's constitutive definition from 0B-I; no constitutive threshold rewrites present. Completing 0B-I does not pass this gate.

| Boundary | Margin — deciding evidence factor that tips the verdict from lower level to upper level |
|----------|----------------------------------------------------------------------------------------|
| STRONG INVALIDATION → INVALIDATION | [name the property STRONG INVALIDATION lacks that, if present, tips the verdict upward — must not restate either level's 0B-I definition] |
| INVALIDATION → MIXED | [deciding factor] |
| MIXED → VALIDATION | [deciding factor] |
| VALIDATION → STRONG VALIDATION | [deciding factor] |

Each margin cell must name the boundary-resolving factor, not the central case of either adjacent level. A margin that says "VALIDATION: majority evidence is positive" fails — it restates the 0B-I definition. A margin that says "convergence across at least two non-adjacent tiers" names a boundary factor.

---

**PHASE 0C — TIER PREDICTIONS**

Scope: per-tier prediction blocks only. Verdict thresholds and margin declarations belong to 0B. Sequence rationale belongs to 0A.

Entry gate: Phase 0B-II exit gate passed.
Exit gate (0C only): one prediction block per planned subject tier; each block names expected posture, evidence anchor, confirming signal, and surprising signal; predictions specific enough to be auditable in Phase 4; no verdict or margin content present; no sequence adjacency rewrites (reference 0A, do not restate it).

For each planned subject tier:

TIER PREDICTION — [tier label]
Expected posture: [specific stance — name what they will anchor in]
Expected evidence anchor: [the specific practice, concern, or experience their answers will orbit]
Confirming signal: [what evidence would confirm this prediction — name type and content]
Surprising signal: [what departure would be diagnostic — specific enough to determine after the interview]

---

**PHASE 1 — SUBJECT DESIGN**

Entry gate: Phases 0A, 0B-I, 0B-II, and 0C exit gates all passed.
Exit gate: all subject card fields non-blank and specific; blind spots names a structural limitation, not a tautology; INCUMBENT's inertia baseline names a specific practice; subject tier labels match the Phase 0A sequence.

For each subject, in Phase 0A sequence order:

Subject tier: [matching Phase 0A sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience — specific domain and depth]
Blind spots: [structural limitation — not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia baseline: [specific current practice and switching cost]

---

**PHASE 2 — TRANSCRIPT**

Entry gate: all Phase 1 subject cards complete.
Exit gate: all transcripts complete before any extraction begins; each transcript closes with a MOMENT line citing a Phase 0C tier prediction by content; INCUMBENT transcript names the inertia baseline directly in at least one question; answers are not interchangeable across subjects.

For each subject, in Phase 0A sequence order:

[5–8 exchanges in the subject's distinct voice. Questions probe the declared primary concern and prior knowledge. Answers are grounded in declared prior knowledge — not interchangeable across subjects.]

MOMENT: [SURPRISING or CONFIRMING] — [cite the Phase 0C prediction by content; where applicable name the Phase 0A adjacency baseline that gives this departure its diagnostic value]

---

**PHASE 3 — EVIDENCE EXTRACTION**

Entry gate: all transcripts complete.
Exit gate: 3–5 items per subject; type, strength, and rationale present for each; rationale non-blank and non-self-referential; not merged with transcript or synthesis.

For each subject:

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential — name what makes this item robust or fragile as evidence]

---

**PHASE 4 — SYNTHESIS**

Entry gate: all extraction complete.
Exit gate: all synthesis sections present with content-level evidence references.

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items]

**Inertia/adoption partition**

INERTIA SIGNALS: [with subject names and evidence item references]
ADOPTION SIGNALS: [with subject names and evidence item references]

**Epistemic re-weighting**

For each subject's declared blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**Sequence contrast audit** (closes Phase 0A)

Return to Phase 0A adjacency blocks. For each:
- Adjacency: [Tier A → Tier B]
- Predicted contrast: [restate from Phase 0A]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT — name specific evidence items]

**Prediction delta** (closes Phase 0C)

Return to Phase 0C. For each tier prediction:
- Tier: [label]
- Prediction: [restate]
- Classification: [CONFIRMED / CONTRADICTED / ABSENT / PARTIAL]
- Evidence: [specific items]

**VERDICT MARGIN AUDIT** (closes Phase 0B-I and 0B-II)

Return to Phase 0B-I for constitutive thresholds. Return to Phase 0B-II for margin declarations.

Classification: [level name]
Threshold crossed: [restate the Phase 0B-I constitutive definition and show which evidence items meet it]
Upper boundary: [name the Phase 0B-II margin factor at the boundary between this classification and the level above; state whether the actual evidence satisfies that margin factor and why — determines whether the verdict reaches the higher level]
Lower boundary: [name the Phase 0B-II margin factor at the boundary between this classification and the level below; state whether the actual evidence satisfies that margin factor and why — confirms the verdict exceeds the lower level]

Both the upper and lower boundary statements must be present. A verdict audit that states only one direction leaves the other boundary unaudited.

**Net verdict**

[One or two sentences. Classification must match the VERDICT MARGIN AUDIT above.]

---

## V-02 — Prohibition-First Gate Clauses (C-34 focus)

**Variation axis:** Prohibition-first gate clauses
**Hypothesis:** R11 V-05 included named scope prohibitions in the Scope header of each sub-phase but expressed the exit gate conditions with affirmative-first framing: "all cells populated with specific content; no verdict threshold content present." When the gate text is inverted — opening with a PROHIBITED clause that names what categories belong to other sub-phases before stating what must be present — scope violation is detectable from the gate text alone without reading the section content. An evaluator checks for prohibited categories first; if found, the gate fails immediately. The Scope header becomes redundant as a guard and survives only as a reader aid.

---

You are running prove-interview for the topic: {topic}

Execute in named phases. Phase 0 is decomposed into three independently-gated sub-phases with non-overlapping scope. Each gate opens with a PROHIBITED clause — scope violations are detectable at gate-read time without inspecting adjacent sub-phases. Do not advance past any gate until it passes.

---

**PHASE 0A — INERTIA PROFILE**

Entry gate: none.
Exit gate (0A):
PROHIBITED: if your Phase 0A content contains verdict level names with threshold definitions, margin-boundary declarations, tier sequence ordering, or per-tier prediction blocks, it has exceeded Phase 0A scope — move that content to Phase 0B or 0C and return to this gate.
REQUIRED: at least one practice row complete with at least two named stickiness factors, a switching cost estimate with one-sentence justification naming the specific cost driver, and a displacement target tier; all cells populated with specific content.

Before designing any subject, profile the status quo {topic} would displace:

| Practice name | Stickiness factors | Switching cost | Displacement target tier |
|---------------|--------------------|----------------|--------------------------|
| | [at least two named factors — e.g., workflow dependency, sunk investment, social proof, learned behavior, vendor lock-in] | [High / Medium / Low — one-sentence justification naming the specific cost driver] | [which subject tier most directly embodies this practice] |

Add rows for each distinct practice displaced. Stickiness factors declared here propagate forward to Phase 2 incumbent question design and Phase 4 INERTIA PROFILE ACCOUNTING.

---

**PHASE 0B — VERDICT DECISION FUNCTION WITH MARGINS**

Entry gate: Phase 0A exit gate passed.
Exit gate (0B):
PROHIBITED: if your Phase 0B content contains inertia stickiness factor rows (Phase 0A scope), sequence adjacency blocks (Phase 0C scope), or per-tier prediction blocks (Phase 0C scope), it has exceeded Phase 0B scope — move that content to its owning phase and return to this gate.
REQUIRED: (1) every verdict level row carries a constitutive evidence-configuration definition naming types, tier sources, and re-weighting outcomes; no row restates the level name; (2) every adjacent-level boundary row carries a margin declaration naming the deciding evidence property at that boundary; no margin cell restates either adjacent level's constitutive definition.

**Constitutive Threshold Definitions**

| Verdict level | Constitutive threshold |
|---------------|------------------------|
| STRONG VALIDATION | [evidence configuration — name types, tier sources, re-weighting outcomes] |
| VALIDATION | [evidence configuration] |
| MIXED | [evidence configuration] |
| INVALIDATION | [evidence configuration] |
| STRONG INVALIDATION | [evidence configuration] |

Definitions that restate the level name fail the REQUIRED clause of this gate.

**Margin-Boundary Declarations**

| Boundary | Margin — deciding evidence factor that tips the verdict from lower level to upper level |
|----------|----------------------------------------------------------------------------------------|
| STRONG INVALIDATION → INVALIDATION | [deciding factor — must not restate either level's constitutive definition] |
| INVALIDATION → MIXED | [deciding factor] |
| MIXED → VALIDATION | [deciding factor] |
| VALIDATION → STRONG VALIDATION | [deciding factor] |

Margin cells that restate a constitutive definition fail the REQUIRED clause. A margin that says "VALIDATION means majority positive evidence" is a constitutive restatement; a margin that says "the presence of a VALIDATION signal from the INCUMBENT tier after re-weighting" is a boundary factor.

---

**PHASE 0C — SEQUENCE BLUEPRINT + TIER PREDICTIONS**

Entry gate: Phase 0B exit gate passed.
Exit gate (0C):
PROHIBITED: if your Phase 0C content contains stickiness factor rows (Phase 0A scope) or verdict threshold / margin-boundary declarations (Phase 0B scope), it has exceeded Phase 0C scope — move that content to its owning phase and return to this gate.
REQUIRED: (1) tier sequence declared; one adjacency block per consecutive pair — each block names what the preceding tier establishes and what the following tier's departure is measured against; contrast-lost statement present per adjacency; (2) one prediction block per planned subject tier — each names expected posture, evidence anchor, confirming signal, and surprising signal specific enough to be auditable in Phase 4; predictions using "may" without committed direction fail this gate.

Tier sequence: [list in order]

For each consecutive pair:

ADJACENCY [Tier A → Tier B]
Tier A establishes: [what posture, evidence type, or baseline Tier A's interview produces]
Tier B departure measured against: [what becomes interpretable in Tier B's evidence because Tier A ran first]
Contrast lost if reversed: [one sentence]

For each planned subject tier:

TIER PREDICTION — [tier label]
Expected posture: [specific stance — trace INCUMBENT anchors to a named Phase 0A practice row]
Expected evidence anchor: [the specific practice, concern, or experience their answers will orbit]
Confirming signal: [what evidence would confirm this prediction — name type and content]
Surprising signal: [what departure would be diagnostic — specific enough to determine after the interview]

---

**PHASE 1 — SUBJECT DESIGN**

Entry gate: Phases 0A, 0B, and 0C exit gates all passed.
Exit gate:
PROHIBITED: if your Phase 1 content contains verdict level definitions, margin declarations, sequence adjacency reasoning, or tier predictions, it has exceeded Phase 1 scope.
REQUIRED: all subject card fields non-blank and specific; blind spots names a structural limitation, not a tautology; INCUMBENT's inertia anchor traces to a named Phase 0A practice row; subject tier labels match the Phase 0C sequence.

For each subject, in Phase 0C sequence order:

Subject tier: [matching Phase 0C sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience — specific domain and depth]
Blind spots: [structural limitation — not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia anchor: [Phase 0A practice name and stickiness factor this subject's answers will orbit]

---

**PHASE 2 — TRANSCRIPT**

Entry gate: all Phase 1 subject cards complete.
Exit gate:
PROHIBITED: if your Phase 2 content contains evidence extraction items, synthesis sections, or verdict classifications, it has exceeded Phase 2 scope.
REQUIRED: all transcripts complete before any extraction begins; each transcript closes with a MOMENT line citing a Phase 0C tier prediction by content; INCUMBENT transcript names the inertia anchor directly in at least one question; answers are not interchangeable across subjects.

For each subject, in Phase 0C sequence order:

[5–8 exchanges in the subject's distinct voice. Answers grounded in declared prior knowledge and primary concern. Register, vocabulary, and framing distinctly theirs.]

MOMENT: [SURPRISING or CONFIRMING] — [cite which Phase 0C tier prediction this moment confirms or departs from, identified by content; where applicable, name the Phase 0C adjacency baseline that gives this departure its diagnostic value]

---

**PHASE 3 — EVIDENCE EXTRACTION**

Entry gate: all transcripts complete.
Exit gate:
PROHIBITED: if your Phase 3 content contains cross-subject synthesis findings, inertia/adoption partition labels, or verdict classifications, it has exceeded Phase 3 scope.
REQUIRED: 3–5 items per subject; type, strength, rationale, and profile relevance tag present for each; rationale non-blank and non-self-referential; not merged with transcript or synthesis.

For each subject:

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential] | PROFILE RELEVANCE: [STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL]

PROFILE RELEVANCE tags which Phase 0A inertia profile dimension the evidence speaks to. EXTERNAL marks items outside the profile scope.

---

**PHASE 4 — SYNTHESIS**

Entry gate: all extraction complete.
Exit gate: all synthesis sections present with content-level evidence references; none marked "see above" or left blank.

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items]

**Inertia/adoption partition**

INERTIA SIGNALS: [with subject names and evidence item references]
ADOPTION SIGNALS: [with subject names and evidence item references]

**INERTIA PROFILE ACCOUNTING** (closes Phase 0A)

Return to Phase 0A. For each declared stickiness factor:
- Confirmed: which subject? Which evidence item? Content-level reference.
- Absent: name the factor and record the absence as a finding — not an omission.

**Epistemic re-weighting**

For each subject's declared blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**PREDICTION DELTA** (closes Phase 0C tier predictions)

Return to Phase 0C. For each tier prediction:
- Tier: [label]
- Prediction: [restate from Phase 0C]
- Classification: [CONFIRMED / CONTRADICTED / ABSENT / PARTIAL]
- Evidence: [specific items — ABSENT must name what was predicted and did not appear]

**SEQUENCE CONTRAST AUDIT** (closes Phase 0C sequence blueprint)

Return to Phase 0C adjacency blocks. For each:
- Adjacency: [Tier A → Tier B]
- Predicted contrast: [restate]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT — name specific evidence items]

**VERDICT MARGIN AUDIT** (closes Phase 0B)

Return to Phase 0B constitutive thresholds and margin declarations.

Classification: [level name]
Threshold crossed: [restate the Phase 0B constitutive definition and show which evidence items meet it]
Upper boundary: [return to Phase 0B margin declarations. Name the margin factor at the boundary between this classification and the level above. State whether the actual evidence satisfies it and why — determines whether the evidence reaches the next higher level.]
Lower boundary: [name the margin factor at the boundary between this classification and the level below. State whether the actual evidence satisfies it and why — confirms the evidence exceeds the next lower level.]
Both boundary placements must be stated.

**Net verdict**

[One or two sentences. Classification must match the VERDICT MARGIN AUDIT above.]

---

## V-03 — Bidirectional Audit Table (C-35 focus)

**Variation axis:** Bidirectional margin audit as a structural two-row table
**Hypothesis:** R11 V-05's VERDICT MARGIN AUDIT required "both boundary placements must be stated" as a prose condition. When the margin audit is rendered as a mandatory two-row table — one row for the upper boundary, one row for the lower boundary, each with Factor / Evidence Status / Implication columns — structural incompleteness is visually immediate: a table with one empty row is not a prose omission but a visible format failure. The practitioner cannot produce a complete table without placing the verdict on both sides. C-35 becomes a format completion requirement.

---

You are running prove-interview for the topic: {topic}

Before designing any subject, complete the OPENING COMMITMENT. All sections must pass their gates before proceeding to subject design.

---

**OPENING COMMITMENT — Section A: Verdict Threshold Table**

Declare the verdict decision function before evidence collection begins.

| Verdict level | Constitutive threshold — evidence configuration that produces this classification | Margin — deciding factor at boundary with adjacent higher level |
|---------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------|
| STRONG VALIDATION | | [what tips the verdict from VALIDATION to STRONG VALIDATION — the factor VALIDATION lacks] |
| VALIDATION | | [what tips from MIXED to VALIDATION] |
| MIXED | | [what tips from INVALIDATION to MIXED] |
| INVALIDATION | | [what tips from STRONG INVALIDATION to INVALIDATION] |
| STRONG INVALIDATION | — (no higher adjacent level) | — |

Instructions:
- Constitutive threshold: name evidence types, tier sources, re-weighting outcomes. Do not restate the level name.
- Margin: name the deciding boundary factor. Do not restate the adjacent level's constitutive definition.
- All non-dash cells must be populated before proceeding.

Gate: every constitutive threshold cell carries a configuration definition (not a level-name restatement); every margin cell names a boundary factor (not a constitutive restatement). Both columns populated before proceeding to Section B.

---

**OPENING COMMITMENT — Section B: Sequence and Signal Declaration**

Tier sequence: [list tiers in order]

For each consecutive pair, one adjacency block:

ADJACENCY [Tier A → Tier B]
Tier A establishes: [specific evidence or posture baseline]
Tier B measured against: [what becomes interpretable because Tier A ran first]
Contrast lost if reversed: [one sentence]

Signal categories sought for {topic}: [enumerate RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION as applicable with per-category rationale]

Gate: adjacency blocks complete for every consecutive pair; at least two signal categories named.

---

For each subject, in declared sequence order:

**SUBJECT CARD**

Subject tier: [matching declared sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience — specific domain and depth]
Blind spots: [structural limitation — not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia baseline: [specific current practice and switching cost — named practice, not "current workflow"]

---

**TRANSCRIPT**

[5–8 exchanges in this subject's distinct voice. Questions probe declared primary concern and prior knowledge. INCUMBENT questions name the inertia baseline directly. Answers not interchangeable across subjects.]

MOMENT: [SURPRISING or CONFIRMING] — [state the prior expectation and whether confirmed or departed from; name the relevant adjacency baseline that gives this departure its interpretive frame]

---

**EVIDENCE EXTRACTION**

[Complete all transcripts before any extraction. Do not merge with transcript or synthesis.]

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential]

---

After all subjects and extraction:

**SYNTHESIS**

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items]

**Inertia/adoption partition**

INERTIA SIGNALS: [subject names + evidence item references]
ADOPTION SIGNALS: [subject names + evidence item references]

**Epistemic re-weighting**

For each subject's declared blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**Sequence contrast audit**

Return to Section B adjacency blocks. For each:
- Adjacency: [Tier A → Tier B]
- Predicted contrast: [restate]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT — specific evidence items]

**VERDICT MARGIN AUDIT**

Return to Section A. Name the threshold row the actual evidence satisfies, then complete the two-row boundary table below. Both rows must be populated — a single-row audit leaves one boundary unaudited.

Classification: [level name]
Threshold crossed: [restate the Section A constitutive definition; show which specific evidence items meet it]

| Boundary direction | Adjacent level | Margin factor (from Section A) | Evidence status | Implication |
|--------------------|---------------|-------------------------------|-----------------|-------------|
| Upper boundary (between this classification and the level above) | [level above] | [restate margin factor from Section A] | [does actual evidence satisfy this margin factor? MEETS / FALLS SHORT — explain why] | [if MEETS: verdict is at risk of upward reclassification unless named; if FALLS SHORT: rules out the level above] |
| Lower boundary (between this classification and the level below) | [level below] | [restate margin factor from Section A] | [does actual evidence satisfy this margin factor? EXCEEDS / JUST REACHES — explain why] | [if EXCEEDS: rules out the level below; if JUST REACHES: verdict is at risk of downward reclassification unless named] |

A verdict audit table with one row left blank fails this section. If this is the highest possible classification (STRONG VALIDATION), state "no upper boundary applies" in the upper row and complete only the lower row; document the exception explicitly.

**Net verdict**

[One or two sentences. Classification must match the VERDICT MARGIN AUDIT classification above. Any reclassification challenge must refute a named boundary statement from the table.]

---

## V-04 — Combined: 0B Decomposition + Prohibition Gates (C-33 + C-34)

**Variation axis:** 0B Internal Decomposition (C-33) + Prohibition-First Gate Clauses (C-34)
**Hypothesis:** C-33 and C-34 reinforce each other most tightly at the Phase 0B level. C-33 requires 0B-I and 0B-II to have independent exit gates whose conditions do not overlap. C-34 requires each gate to name prohibited content by category. When combined, the 0B-II exit gate opens with: "PROHIBITED: if your 0B-II content restates an adjacent level's constitutive definition from 0B-I, it has exceeded 0B-I scope — revise the margin cell to name a boundary factor." This clause makes C-31 enforcement mechanical at the sub-section level: the evaluator reads the 0B-II gate text, checks each margin cell for constitutive-definition restatements, and records a fail without comparing the two columns. C-33 provides the structural separation; C-34 makes the prohibition gate-readable. Neither criterion alone achieves both enforcement properties.

---

You are running prove-interview for the topic: {topic}

Execute in named phases. Phase 0 is decomposed into three independently-gated sub-phases with non-overlapping scope. Phase 0B is further decomposed into two independently-gated sub-sections (0B-I and 0B-II) with non-overlapping scope. Every gate opens with a PROHIBITED clause identifying out-of-scope content by category before stating completion requirements. Do not advance past any gate until it passes.

---

**PHASE 0A — SEQUENCE BLUEPRINT + SIGNAL COMMITMENT**

Entry gate: none.
Exit gate (0A):
PROHIBITED: if your Phase 0A content contains verdict threshold definitions, margin-boundary declarations, or per-tier prediction blocks, it has exceeded Phase 0A scope — move that content to Phase 0B or 0C before proceeding.
REQUIRED: tier sequence declared with one adjacency block per consecutive pair; each adjacency block names what the preceding tier establishes, what the following tier's departure is measured against, and what contrast would be lost if the order were reversed; signal categories enumerated with per-category rationale; at least two categories named.

Tier sequence: [list in order]

For each consecutive pair:

ADJACENCY [Tier A → Tier B]
Tier A establishes: [what posture, evidence type, or baseline Tier A produces]
Tier B departure measured against: [what becomes interpretable in Tier B because Tier A ran first]
Contrast lost if reversed: [one sentence]

Signal categories sought: [enumerate RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION as applicable with rationale for {topic}]

---

**PHASE 0B — VERDICT DECISION FUNCTION WITH MARGINS**

Phase 0B is decomposed into two independently-gated sub-sections. Each sub-section has its own prohibition-first exit gate. Satisfying 0B-I does not satisfy 0B-II and vice versa.

Entry gate (0B): Phase 0A exit gate passed.

---

**PHASE 0B-I — CONSTITUTIVE THRESHOLD DEFINITIONS**

Exit gate (0B-I):
PROHIBITED: if your Phase 0B-I content contains margin-boundary declarations (deciding factors at adjacent-level boundaries), tier sequence adjacency blocks, or tier prediction blocks, it has exceeded 0B-I scope — margin content belongs in 0B-II; sequence and prediction content belongs in 0A and 0C.
REQUIRED: every verdict level row carries a constitutive evidence-configuration definition naming types, tier sources, and re-weighting outcomes; no row restates the level name; all rows populated.

| Verdict level | Constitutive threshold — evidence configuration that produces this classification |
|---------------|-----------------------------------------------------------------------------------|
| STRONG VALIDATION | |
| VALIDATION | |
| MIXED | |
| INVALIDATION | |
| STRONG INVALIDATION | |

Replace blank cells with {topic}-specific constitutive definitions before attempting the 0B-I gate.

---

**PHASE 0B-II — MARGIN-BOUNDARY DECLARATIONS**

Entry gate (0B-II): Phase 0B-I exit gate passed.
Exit gate (0B-II):
PROHIBITED: if your Phase 0B-II content restates any adjacent level's constitutive definition from 0B-I, it has exceeded 0B-I scope — revise the margin cell to name the deciding boundary factor rather than the central case of either adjacent level. If your content contains tier sequence or prediction material, it belongs to 0A or 0C.
REQUIRED: every boundary row carries a margin declaration identifying the evidence property decisive at that boundary; every margin cell is logically distinct from both adjacent levels' 0B-I constitutive definitions; all boundary rows populated.

| Boundary | Margin — deciding evidence factor that tips the verdict from lower level to upper level |
|----------|----------------------------------------------------------------------------------------|
| STRONG INVALIDATION → INVALIDATION | [boundary-resolving factor — the property STRONG INVALIDATION lacks; must not restate either 0B-I definition] |
| INVALIDATION → MIXED | |
| MIXED → VALIDATION | |
| VALIDATION → STRONG VALIDATION | |

Gate test: for each margin cell, ask "does this cell describe what makes one level the central case?" If yes, it restates a constitutive definition and fails the PROHIBITED clause. A passing cell names what tips the verdict from one side to the other when the evidence is ambiguous between adjacent levels.

---

**PHASE 0C — TIER PREDICTIONS**

Entry gate: Phase 0B-II exit gate passed.
Exit gate (0C):
PROHIBITED: if your Phase 0C content contains verdict threshold definitions or margin-boundary declarations (Phase 0B scope), or sequence adjacency blocks without prediction content (Phase 0A scope), it has exceeded Phase 0C scope.
REQUIRED: one prediction block per planned subject tier; each block names expected posture, evidence anchor, confirming signal, and surprising signal; all prediction fields specific enough to be auditable in Phase 4; predictions using "may" without committed direction fail this gate.

For each planned subject tier:

TIER PREDICTION — [tier label]
Expected posture: [specific stance — what they will anchor in, not merely that they will resist or support]
Expected evidence anchor: [the specific practice, concern, or experience their answers will orbit]
Confirming signal: [what evidence would confirm this prediction — name type and content]
Surprising signal: [what departure would be diagnostic — specific enough to determine after the interview]

---

**PHASE 1 — SUBJECT DESIGN**

Entry gate: Phases 0A, 0B-I, 0B-II, and 0C exit gates all passed.
Exit gate:
PROHIBITED: if your Phase 1 content contains verdict definitions, margin declarations, sequence rationale, or prediction blocks, it has exceeded Phase 1 scope.
REQUIRED: all subject card fields non-blank and specific; blind spots names a structural limitation, not a tautology; INCUMBENT's inertia baseline names a specific practice; subject tier labels match the Phase 0A sequence.

For each subject, in Phase 0A sequence order:

Subject tier: [matching Phase 0A sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience — specific domain and depth]
Blind spots: [structural limitation — not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia baseline: [specific current practice and switching cost]

---

**PHASE 2 — TRANSCRIPT**

Entry gate: all Phase 1 subject cards complete.
Exit gate:
PROHIBITED: if your Phase 2 content contains evidence extraction items or synthesis sections, it has exceeded Phase 2 scope.
REQUIRED: all transcripts complete before any extraction; each closes with a MOMENT line citing a Phase 0C prediction by content; INCUMBENT transcript names inertia baseline directly in at least one question; answers not interchangeable across subjects.

For each subject, in Phase 0A sequence order:

[5–8 exchanges in the subject's distinct voice. Questions probe primary concern and prior knowledge.]

MOMENT: [SURPRISING or CONFIRMING] — [cite the Phase 0C tier prediction this moment confirms or departs from; where applicable name the Phase 0A adjacency baseline that gives the departure its diagnostic value]

---

**PHASE 3 — EVIDENCE EXTRACTION**

Entry gate: all transcripts complete.
Exit gate:
PROHIBITED: if your Phase 3 content contains cross-subject synthesis statements, inertia/adoption partition sections, or verdict classifications, it has exceeded Phase 3 scope.
REQUIRED: 3–5 items per subject; type, strength, rationale present; rationale non-blank and non-self-referential; not merged with transcript or synthesis.

For each subject:

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential]

---

**PHASE 4 — SYNTHESIS**

Entry gate: all extraction complete.
Exit gate: all synthesis sections present with content-level references; none blank or marked "see above."

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items]

**Inertia/adoption partition**

INERTIA SIGNALS: [subject names + evidence item references]
ADOPTION SIGNALS: [subject names + evidence item references]

**Epistemic re-weighting**

For each subject's blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**Sequence contrast audit** (closes Phase 0A)

Return to Phase 0A adjacency blocks. For each:
- Adjacency: [Tier A → Tier B]
- Predicted contrast: [restate]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT — specific items]

**Prediction delta** (closes Phase 0C)

Return to Phase 0C. For each tier prediction:
- Tier: [label]
- Prediction: [restate]
- Classification: [CONFIRMED / CONTRADICTED / ABSENT / PARTIAL]
- Evidence: [specific items]

**VERDICT MARGIN AUDIT** (closes Phase 0B-I and 0B-II)

Return to Phase 0B-I for constitutive thresholds and Phase 0B-II for margin declarations.

Classification: [level name]
Threshold crossed: [restate the Phase 0B-I constitutive definition; show which evidence items meet it]
Upper boundary: [Phase 0B-II margin factor at the boundary with the level above; state whether evidence satisfies it and why]
Lower boundary: [Phase 0B-II margin factor at the boundary with the level below; state whether evidence satisfies it and why]
Both boundary placements required.

**Net verdict**

[One or two sentences. Classification must match the VERDICT MARGIN AUDIT above.]

---

## V-05 — Full Apparatus: All Four New Criteria + All Prior Late-Aspirational Criteria

**Variation axis:** C-33 (0B-I/0B-II independent gates) + C-34 (prohibition-first gates throughout) + C-35 (bidirectional audit table) + C-36 (PROFILE RELEVANCE vocabulary defined in Phase 0A, propagated through Phase 3 and Phase 4 accounting) + C-26 through C-32 (full prior apparatus)
**Hypothesis:** All twelve late-aspirational criteria (C-26 through C-36) are structurally related. C-33 and C-34 are both Phase 0B concerns: C-33 provides the structural separation between 0B-I and 0B-II; C-34 makes each gate's prohibition clause the primary scope enforcement mechanism. C-35 is a Phase 4 concern: the VERDICT MARGIN AUDIT table requires both rows to be populated, making the bidirectionality a format completion rather than a prose condition. C-36 is a Phase 0A-to-Phase-3 propagation concern: when the PROFILE RELEVANCE tag vocabulary is declared in the Phase 0A exit gate as part of the stickiness factor enumeration, Phase 3 evidence items that use the vocabulary are forward-referencing a defined set, and Phase 4 INERTIA PROFILE ACCOUNTING rows can close by tag rather than by content recall. All twelve criteria become consequences of completing the phase gates in declared order.

---

You are running prove-interview for the topic: {topic}

Execute in named phases. Each phase has an entry gate and an exit gate. Phase 0 is decomposed into three independently-gated sub-phases with mutually exclusive scope. Phase 0B is further decomposed into two independently-gated sub-sections (0B-I and 0B-II) with mutually exclusive scope. Every gate opens with a PROHIBITED clause before stating completion requirements. Satisfying one sub-phase's or sub-section's exit gate cannot satisfy another's. Do not advance past any gate until it passes.

---

**PHASE 0A — INERTIA PROFILE**

Entry gate: none.
Exit gate (0A):
PROHIBITED: if your Phase 0A content contains verdict level names with threshold definitions, margin-boundary declarations, tier sequence adjacency blocks, or per-tier prediction blocks, it has exceeded Phase 0A scope — move that content to Phase 0B or 0C before returning to this gate. Phase 0A scope is stickiness factor enumeration only.
REQUIRED: at least one practice row complete with at least two named stickiness factors from the PROFILE RELEVANCE vocabulary below, a switching cost estimate with one-sentence justification naming the specific cost driver, and a displacement target tier; all cells populated with specific content.
PROFILE RELEVANCE vocabulary declared here and used in Phase 3 evidence items: STICKINESS (speaks to a declared stickiness factor in this table) / LIMITATION (speaks to a switching cost or structural constraint) / DISPLACEMENT (speaks to which tier embodies the displaced practice) / EXTERNAL (no direct connection to this profile). Each Phase 3 evidence item will carry one of these four tags.

Before designing any subject, profile the status quo {topic} would displace:

| Practice name | Stickiness factors (name each factor; these become PROFILE RELEVANCE referents in Phase 3) | Switching cost | Displacement target tier |
|---------------|---------------------------------------------------------------------------------------------|----------------|--------------------------|
| | [at least two named factors: e.g., workflow dependency, sunk investment, social proof, learned behavior, vendor lock-in] | [High / Medium / Low — one-sentence justification naming the specific cost driver] | [which subject tier most directly embodies this practice] |

Add rows for each distinct practice displaced. The PROFILE RELEVANCE vocabulary declared in this gate propagates to Phase 3 evidence item format and Phase 4 INERTIA PROFILE ACCOUNTING.

---

**PHASE 0B — VERDICT DECISION FUNCTION WITH MARGINS**

Phase 0B is decomposed into two independently-gated sub-sections (0B-I and 0B-II). Each carries its own prohibition-first exit gate. Completing 0B-I does not satisfy the 0B-II gate; completing 0B-II does not satisfy the 0B-I gate.

Entry gate (0B): Phase 0A exit gate passed.

---

**PHASE 0B-I — CONSTITUTIVE THRESHOLD DEFINITIONS**

Exit gate (0B-I):
PROHIBITED: if your Phase 0B-I content contains margin-boundary declarations (deciding factors at adjacent-level boundaries), tier sequence or adjacency reasoning, or per-tier predictions, it has exceeded 0B-I scope — margin content belongs in 0B-II; sequence and prediction content belongs in 0C. If a cell describes the deciding factor that tips a verdict from one adjacent level to another, it is margin content and belongs in 0B-II.
REQUIRED: every verdict level row carries a constitutive evidence-configuration definition naming types, tier sources, and re-weighting outcomes; no row restates the level name; all five rows populated; no margin or boundary-factor content present.

| Verdict level | Constitutive threshold — evidence configuration that produces this classification |
|---------------|-----------------------------------------------------------------------------------|
| STRONG VALIDATION | [evidence configuration — name types, tier sources, re-weighting outcomes] |
| VALIDATION | [evidence configuration] |
| MIXED | [evidence configuration] |
| INVALIDATION | [evidence configuration] |
| STRONG INVALIDATION | [evidence configuration] |

Replace bracketed cells with {topic}-specific constitutive definitions. Definitions that restate the level name fail the REQUIRED clause. Definitions that name a boundary-deciding factor rather than a central-case configuration belong in 0B-II and fail the PROHIBITED clause.

---

**PHASE 0B-II — MARGIN-BOUNDARY DECLARATIONS**

Entry gate (0B-II): Phase 0B-I exit gate passed.
Exit gate (0B-II):
PROHIBITED: if any margin cell in Phase 0B-II restates an adjacent level's constitutive definition from 0B-I — describing the central case of a level rather than the boundary-resolving factor between two adjacent levels — it has exceeded 0B-I scope; revise the cell to name the deciding evidence property at the boundary before returning to this gate. If your content contains inertia stickiness factor rows (Phase 0A scope), sequence adjacency blocks (Phase 0C scope), or tier prediction blocks (Phase 0C scope), remove them before returning to this gate.
REQUIRED: every boundary row carries a margin declaration identifying the evidence property decisive at that boundary when evidence configurations for two adjacent levels overlap; every margin cell is logically distinct from both adjacent levels' 0B-I constitutive definitions; all four boundary rows populated.

| Boundary | Margin — deciding evidence factor that tips the verdict from lower level to upper level |
|----------|----------------------------------------------------------------------------------------|
| STRONG INVALIDATION → INVALIDATION | [boundary-resolving factor — the property STRONG INVALIDATION lacks; must not restate either 0B-I definition] |
| INVALIDATION → MIXED | [deciding factor] |
| MIXED → VALIDATION | [deciding factor] |
| VALIDATION → STRONG VALIDATION | [deciding factor] |

Gate self-test: for each margin cell, ask "could this cell appear verbatim in the 0B-I constitutive threshold column?" If yes, revise. A passing margin cell names what is decisive when evidence is genuinely ambiguous between adjacent levels; a failing margin cell restates what makes one level the expected case.

---

**PHASE 0C — SEQUENCE BLUEPRINT + TIER PREDICTIONS**

Entry gate: Phase 0B-II exit gate passed.
Exit gate (0C):
PROHIBITED: if your Phase 0C content contains verdict threshold definitions or margin-boundary declarations (Phase 0B scope), or inertia stickiness factor rows (Phase 0A scope), it has exceeded Phase 0C scope — move that content before returning to this gate.
REQUIRED: (1) tier sequence declared; one adjacency block per consecutive pair — each block names what the preceding tier establishes, what the following tier's departure is measured against, and what contrast would be lost if reversed; (2) one prediction block per planned subject tier; each block names expected posture, evidence anchor, confirming signal, and surprising signal specific enough to be auditable in Phase 4; INCUMBENT anchor traces to a named Phase 0A practice row; predictions using "may" without committed direction fail this gate.

**0C-I: Sequence Blueprint**

Tier sequence: [list in order]

For each consecutive pair:

ADJACENCY [Tier A → Tier B]
Tier A establishes: [what posture, evidence type, or baseline Tier A's interview produces]
Tier B departure measured against: [what becomes interpretable in Tier B's evidence because Tier A ran first]
Contrast lost if reversed: [one sentence]

**0C-II: Tier Predictions**

For each planned subject tier:

TIER PREDICTION — [tier label]
Expected posture: [specific stance — name what they will anchor in; trace INCUMBENT anchors to a named Phase 0A practice row and stickiness factor]
Expected evidence anchor: [the specific practice, concern, or experience their answers will orbit]
Confirming signal: [what evidence would confirm this prediction — name type and content]
Surprising signal: [what departure would be diagnostic — specific enough to determine after the interview]

---

**PHASE 1 — SUBJECT DESIGN**

Entry gate: Phases 0A, 0B-I, 0B-II, and 0C exit gates all passed.
Exit gate:
PROHIBITED: if your Phase 1 content contains verdict definitions, margin declarations, sequence adjacency reasoning, or tier prediction blocks, it has exceeded Phase 1 scope.
REQUIRED: all subject card fields non-blank and specific; blind spots names a structural limitation, not a tautology; INCUMBENT's inertia anchor traces to a named Phase 0A practice row and a declared stickiness factor; subject tier labels match the Phase 0C-I sequence.

For each subject, in Phase 0C-I sequence order:

Subject tier: [matching Phase 0C-I sequence]
Role: [job title and organizational position]
Prior knowledge: [direct experience — specific domain and depth]
Blind spots: [structural limitation — not blank, not "none"]
Disposition: [expected posture toward {topic}]
Primary concern: [the one thing driving their responses]
[INCUMBENT only] Inertia anchor: [Phase 0A practice name and stickiness factor this subject's answers will orbit — must name a specific row from the Phase 0A table]

---

**PHASE 2 — TRANSCRIPT**

Entry gate: all Phase 1 subject cards complete.
Exit gate:
PROHIBITED: if your Phase 2 content contains evidence extraction items (bulleted evidence lines), synthesis section headers, or verdict classification terms, it has exceeded Phase 2 scope.
REQUIRED: all transcripts complete before any extraction begins; each transcript closes with a MOMENT line citing a Phase 0C-II tier prediction by content and — where applicable — the Phase 0C-I adjacency baseline that gives the departure its diagnostic value; INCUMBENT transcript contains at least one question naming the declared Phase 0A inertia anchor directly; answers are not interchangeable across subjects — register, vocabulary, and framing distinctly theirs.

For each subject, in Phase 0C-I sequence order:

[5–8 exchanges in the subject's distinct voice. Answers grounded in declared prior knowledge and primary concern. Not interchangeable across subjects.]

MOMENT: [SURPRISING or CONFIRMING] — [state which Phase 0C-II tier prediction this moment confirms or departs from, identified by content not position; where diagnostic value depends on a preceding tier's established baseline, name that baseline and the relevant Phase 0C-I adjacency block]

---

**PHASE 3 — EVIDENCE EXTRACTION**

Entry gate: all transcripts complete.
Exit gate:
PROHIBITED: if your Phase 3 content contains cross-subject synthesis statements, inertia/adoption partition section headers, or verdict classifications, it has exceeded Phase 3 scope — those belong in Phase 4.
REQUIRED: 3–5 items per subject; TYPE, STRENGTH, RATIONALE, and PROFILE RELEVANCE tag present for each; RATIONALE non-blank and non-self-referential; PROFILE RELEVANCE uses the vocabulary declared in Phase 0A (STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL); not merged with transcript or synthesis.

For each subject:

- [Evidence item] | TYPE: [RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION] | STRENGTH: [STRONG / MODERATE / WEAK] | RATIONALE: [non-blank, non-self-referential — name what makes this item robust or fragile as evidence] | PROFILE RELEVANCE: [STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL — from the vocabulary declared in Phase 0A]

PROFILE RELEVANCE tags which Phase 0A inertia profile dimension the evidence addresses. EXTERNAL marks items outside the declared profile scope. Tag vocabulary was defined in the Phase 0A exit gate; use that vocabulary verbatim.

---

**PHASE 4 — SYNTHESIS**

Entry gate: all extraction complete.
Exit gate: all seven synthesis sections present with content-level evidence references; none blank or marked "see above"; VERDICT MARGIN AUDIT table has both boundary rows populated.

**Cross-subject aggregation**

Convergence: [finding + subject names + evidence items]
Contradiction: [both subjects by name + both specific conflicting evidence items — assertion without named items fails this section]

**Inertia/adoption partition**

INERTIA SIGNALS: [subject names + evidence item references]
ADOPTION SIGNALS: [subject names + evidence item references]

**INERTIA PROFILE ACCOUNTING** (closes Phase 0A)

Return to Phase 0A. For each declared stickiness factor, close by PROFILE RELEVANCE tag:
- Factor name: [from Phase 0A practice row]
- PROFILE RELEVANCE tag: STICKINESS / LIMITATION / DISPLACEMENT (as applicable)
- Confirmed by: [subject name + specific evidence item carrying this tag from Phase 3]
- Absent: if no Phase 3 item carries this factor's tag, record the factor name and the absence as a finding — not an omission

**Epistemic re-weighting**

For each subject's declared blind spots: name which evidence items should be down-weighted and what evidence would resolve the gap.

**PREDICTION DELTA** (closes Phase 0C-II)

Return to Phase 0C-II. For each tier prediction:
- Tier: [label]
- Prediction: [restate from Phase 0C-II]
- Classification: [CONFIRMED / CONTRADICTED / ABSENT / PARTIAL]
- Evidence: [name specific items — ABSENT must name what was predicted and did not appear]

**SEQUENCE CONTRAST AUDIT** (closes Phase 0C-I)

Return to Phase 0C-I adjacency blocks. For each:
- Adjacency: [Tier A → Tier B]
- Predicted contrast: [restate from Phase 0C-I]
- Observed: [CONFIRMED / CONTRADICTED / ABSENT — name specific evidence items or record absence explicitly]

**VERDICT MARGIN AUDIT** (closes Phase 0B-I and 0B-II)

Return to Phase 0B-I for constitutive thresholds and Phase 0B-II for margin declarations.

Classification: [level name]
Threshold crossed: [restate the Phase 0B-I constitutive definition for the delivered classification; show which specific Phase 3 evidence items meet each threshold criterion]

| Boundary direction | Adjacent level | Margin factor (from Phase 0B-II) | Evidence status | Implication for this verdict |
|--------------------|---------------|----------------------------------|-----------------|-------------------------------|
| Upper boundary (this classification → level above) | [level above or "none" if STRONG VALIDATION] | [restate Phase 0B-II margin factor verbatim] | [FALLS SHORT of margin / MEETS margin — explain with named evidence items] | [FALLS SHORT: rules out reclassification upward; MEETS: explain why the verdict is held at this level despite reaching the upper margin] |
| Lower boundary (level below → this classification) | [level below or "none" if STRONG INVALIDATION] | [restate Phase 0B-II margin factor verbatim] | [EXCEEDS margin / JUST REACHES margin — explain with named evidence items] | [EXCEEDS: rules out reclassification downward; JUST REACHES: note the risk and state why the verdict is held at this level] |

Both rows must be populated. A verdict audit with one row left blank or marked "N/A" fails the Phase 4 exit gate — if the delivered classification is STRONG VALIDATION or STRONG INVALIDATION (no adjacent level on one side), state this explicitly in the adjacent level cell and complete the evidence status and implication cells for the one applicable boundary.

**Net verdict**

[One or two sentences. Classification must match the VERDICT MARGIN AUDIT classification above. Any reclassification challenge requires refutation of a named boundary statement from the margin audit table — assertion of a competing characterization without engaging the declared margin factors does not constitute a refutation.]
