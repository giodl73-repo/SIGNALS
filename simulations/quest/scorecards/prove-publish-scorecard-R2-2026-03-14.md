Good — I have the format for multi-100 scorecards. Now I have everything needed to score R2.

---

## Quest Score — prove-publish R2

### Scoring Methodology

v2 rubric: 13 criteria. Essential (C-01–C-05) = 12 pts each (60 total). Recommended (C-06–C-08) = 10 pts each (30 total). Aspirational (C-09–C-13) = 2 pts each (10 total). Max = 100.

PARTIAL aspirational = 1 pt. Golden threshold: all 5 essential pass + composite >= 80.

---

### V-01: Status-Quo-Spine

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PASS** (12/12) | Phase 3 lists all sections explicitly with individual requirements: Abstract, Status Quo, Hypothesis, Method, Evidence, Findings, Principles, Limitations, Future Work — all 8 required sections present |
| C-02 | Hypothesis explicitly resolved | **PASS** (12/12) | `HYPOTHESIS VERDICT: [Confirmed | Refuted | Partially confirmed under X but not Y]` required as first Findings line; rationale citing E-IDs; evasion-proof structure |
| C-03 | Evidence traceable | **PASS** (12/12) | `E-[N]: [claim] [source: file-path.md, section or item ID]` format required per claim; uncitable claims routed to Limitations with `UNCITABLE:` tag — no laundering path |
| C-04 | Findings synthesized | **PASS** (12/12) | Findings explicitly answer "what does this mean?" not "what happened?"; conclusion required per finding; BASELINE MATCH / NEW SIGNAL classification forces interpretation mode |
| C-05 | Principles actionable | **PASS** (12/12) | "Always X", "When Y, do Z", "Prefer A over B" forms required; minimum 2 numbered; each tagged [EXTENDS BASELINE] or [REPLACES BASELINE] |
| C-06 | Panel review, 2+ named roles | **PASS** (10/10) | Phase 4: Domain Expert (critique + score N/10) + Practitioner (critique + score N/10); two named roles, substantive critique required |
| C-07 | Abstract standalone | **PASS** (10/10) | "<200 words. (a) question investigated, (b) method, (c) key finding, (d) practical implication. Do not describe structure. A reader who reads only this can state what was investigated, how, and what was found." |
| C-08 | Future Work concrete | **PASS** (10/10) | Min 2 questions; at least one targets Status Quo gap; failing form ("More research needed") and passing form ("Investigate whether [B-01] holds when [condition], using [method]") both given explicitly |
| C-09 | Principles cross-referenced | **PASS** (2/2) | "Each cites its finding: `P-01 [from F-02]: ...`" — explicit finding→principle traceability chain |
| C-10 | Cold-start readable | **PASS** (2/2) | Method: "Cold-start readable: define any domain-specific terms on first use" — explicit jargon gate absent in R1 V-01; Status Quo section pre-orients new readers |
| C-11 | Findings classified by novelty | **PASS** (2/2) | Every finding carries BASELINE MATCH or NEW SIGNAL tag citing B-ID; CONTRIBUTION block if any NEW SIGNAL; INERTIA FLAG if all BASELINE MATCH — structural, not decorative |
| C-12 | Status Quo section present | **PASS** (2/2) | Phase 2: Skeptic writes Status Quo first — before Lead Author writes anything; minimum 2 concrete prior beliefs (B-01, B-02, B-03); "this is the final text" — not a draft |
| C-13 | Citation audit precedes Findings | **PARTIAL** (1/2) | Citation format enforced and uncitable routing present, but no explicit CITATION AUDIT block or pass/fail gate. No "Evidence complete" marker. Ordering is implicit (Evidence section before Findings in template) but there is no structural stop that blocks Findings if uncited claims remain |

**V-01 Total: 99/100** — All essential pass. Golden. C-13 is the only gap: citation discipline is enforced by format but not by a named lifecycle gate.

---

### V-02: Citation-Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PASS** (12/12) | Phase 4 enumerates: Abstract, Status Quo, Hypothesis, Method, Evidence, Findings, Principles, Limitations, Future Work — all 8 explicitly listed with section requirements |
| C-02 | Hypothesis explicitly resolved | **PASS** (12/12) | Phase 3 HYPOTHESIS VERDICT block: accepted forms listed verbatim; "Not accepted: 'The evidence is mixed.' / 'Further investigation is needed.'" The verdict is "a commit with evidence basis, not a hedge." |
| C-03 | Evidence traceable | **PASS** (12/12) | `E-[N]: [claim text] [source: file-path.md, section or item ID]` format; uncitable claims recorded and excluded; minimum 3 cited claims; EVIDENCE COMPLETE marker required in paper |
| C-04 | Findings synthesized | **PASS** (12/12) | "conclusion answering 'what does this mean?' not 'what happened?'" required per finding; BASELINE MATCH / NEW SIGNAL classification enforced; minimum 3 implied by template |
| C-05 | Principles actionable | **PASS** (12/12) | "Always X", "When Y, do Z", "Prefer A over B because..." required; minimum 2 numbered; `P-01 [from F-02]` finding citation |
| C-06 | Panel review, 2+ named roles | **PASS** (10/10) | Phase 5: Domain Expert + Practitioner, each with one substantive critique or endorsement and N/10 score |
| C-07 | Abstract standalone | **PASS** (10/10) | "Written now that the verdict is known. State: question, method, key finding, implication. Do not describe paper structure. A reader who reads only this can act on it." |
| C-08 | Future Work concrete | **PASS** (10/10) | Min 2 specific investigable questions; form: "Investigate whether X holds when Y, using method Z."; failing form: "More research is needed." |
| C-09 | Principles cross-referenced | **PASS** (2/2) | "Each cites its finding: `P-01 [from F-02]: ...`" |
| C-10 | Cold-start readable | **PASS** (2/2) | Method: "Cold-start readable: define domain-specific terms on first use."; Status Quo with B-01/B-02 priors and "default action without this investigation" |
| C-11 | Findings classified by novelty | **PASS** (2/2) | `[BASELINE MATCH / NEW SIGNAL]` tag required on every finding; CONTRIBUTION block if NEW SIGNAL present; at least one NEW SIGNAL expected if evidence supports |
| C-12 | Status Quo section present | **PASS** (2/2) | Phase 4 Section 2 "Status Quo": minimum 2 concrete prior assumptions (B-01/B-02 format), default action without investigation; precedes Hypothesis (Section 3) |
| C-13 | Citation audit precedes Findings | **PASS** (2/2) | This is V-02's defining axis. Phase 2 CITATION AUDIT block: "Status: [PASS — proceed to Findings] or [BLOCKED — N uncited claims remain]." "Do not move to Phase 3 until the citation audit shows Status: PASS." Hard stop by structure |

**V-02 Total: 100/100** — All essential pass. Golden. C-13 is the strongest enforcement of any variation — the hard BLOCKED gate is machine-verifiable.

---

### V-03: Novelty-Pre-Classification

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PASS** (12/12) | Phase 5 explicitly lists: Abstract, Status Quo, Hypothesis, Method, Evidence, Findings, Principles, Limitations, Future Work — all 8 required sections with per-section guidance |
| C-02 | Hypothesis explicitly resolved | **PASS** (12/12) | Phase 3 HYPOTHESIS VERDICT block: "No evasive forms accepted. The verdict is a commit, not a hedge." Verdict with Rationale citing named artifacts |
| C-03 | Evidence traceable | **PASS** (12/12) | `E-[N]: [claim] [source: file-path.md, section or item ID]` format; uncitable claims moved to Limitations; minimum 3 cited claims |
| C-04 | Findings synthesized | **PASS** (12/12) | Phase 4 classification scaffold committed BEFORE prose: forces the author to decide "is this new?" before deciding what to say — the strongest C-04 enforcement of any variation; conclusion "what does this mean?" explicitly required |
| C-05 | Principles actionable | **PASS** (12/12) | "Action-oriented form required." "Always X", "When Y, do Z", "Prefer A over B." Minimum 2 numbered; each cites finding; [EXTENDS BASELINE] / [REPLACES BASELINE] tags |
| C-06 | Panel review, 2+ named roles | **PASS** (10/10) | Phase 6: Domain Expert (accuracy + Status Quo baseline check) + Practitioner (actionability) with N/10 scores; plus Lead Author NOVELTY AUDIT self-check |
| C-07 | Abstract standalone | **PASS** (10/10) | "<200 words: question, method, key finding, implication. Not structure." |
| C-08 | Future Work concrete | **PASS** (10/10) | "Minimum 2 specific investigable questions, specific enough to start." |
| C-09 | Principles cross-referenced | **PASS** (2/2) | "Each cites its finding: `P-01 [from F-02]: ...`" |
| C-10 | Cold-start readable | **PASS** (2/2) | Method: "Cold-start readable: define domain-specific terms on first use."; Status Quo formalized from prior belief inventory |
| C-11 | Findings classified by novelty | **PASS** (2/2) | This is V-03's defining axis. Classification scaffold committed in Phase 4 BEFORE any finding prose is written — inverts the usual sequence. NEW SIGNAL CHECK with explicit INERTIA FLAG if all are BASELINE MATCH |
| C-12 | Status Quo section present | **PASS** (2/2) | Phase 2 Prior Belief Inventory (B-01, B-02, B-03) formalized into Status Quo section in Phase 5 with minimum 2 concrete beliefs; precedes Hypothesis |
| C-13 | Citation audit precedes Findings | **PARTIAL** (1/2) | Citation format enforced throughout Evidence section; uncitable claims routed. But no explicit CITATION AUDIT block and no named gate before Findings. The NOVELTY AUDIT in Phase 6 is post-completion. No "Evidence complete" marker in the paper. Evidence ordering before Findings is structural but there is no stop-and-check step |

**V-03 Total: 99/100** — All essential pass. Golden. C-13 gap is the same as V-01: citation discipline enforced by format but not by a formal gate.

---

### V-04: Full Integration (V-01 Excellence + R2 Aspirationals)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PASS** (12/12) | Phase 5 lists all sections explicitly: Abstract, Status Quo, Hypothesis, Method, Evidence, Findings, Principles, Limitations, Future Work |
| C-02 | Hypothesis explicitly resolved | **PASS** (12/12) | Phase 4 HYPOTHESIS VERDICT with "Full verdict sentence: '[One quotable sentence]'"; "Not accepted: 'The evidence is mixed.'"; evidence basis citing E-IDs required |
| C-03 | Evidence traceable | **PASS** (12/12) | `E-[N]: [claim] [source: file-path.md, section or item ID]`; UNCITABLE routing; EVIDENCE COMPLETE marker with audit pass count required in paper |
| C-04 | Findings synthesized | **PASS** (12/12) | "conclusion answering 'what does this mean?' not 'what happened?'"; BASELINE MATCH/NEW SIGNAL classification; CONTRIBUTION/INERTIA FLAG structural blocks |
| C-05 | Principles actionable | **PASS** (12/12) | "Always X", "When Y, do Z", "Prefer A over B." Minimum 2 numbered; `P-01 [from F-02]`; [EXTENDS/REPLACES BASELINE] tags |
| C-06 | Panel review, 2+ named roles | **PASS** (10/10) | Phase 6: Domain Expert + Practitioner + Skeptic Post-Review (5-item checklist, prediction outcome, APPROVED/FLAG). Three roles — the most complete panel of any variation |
| C-07 | Abstract standalone | **PASS** (10/10) | "Written now that the verdict is known. State: question, method, key finding, implication. Not structure. Written as if it is the only thing a future researcher reads." |
| C-08 | Future Work concrete | **PASS** (10/10) | "Minimum 2 specific investigable questions. At least one targets a gap in the Status Quo baseline. Specific enough to start without clarification." |
| C-09 | Principles cross-referenced | **PASS** (2/2) | "Each cites its finding: `P-01 [from F-02]: ...`" |
| C-10 | Cold-start readable | **PASS** (2/2) | Method: "Cold-start readable: define domain-specific terms on first use."; Status Quo written as Skeptic pre-flight before authoring begins |
| C-11 | Findings classified by novelty | **PASS** (2/2) | "Three structural rules (non-negotiable): 3. Every finding carries a BASELINE MATCH or NEW SIGNAL tag (C-11)." Declared as rule #3 at prompt header before any phase |
| C-12 | Status Quo section present | **PASS** (2/2) | "Three structural rules (non-negotiable): 1. Status Quo section produced by Skeptic before any paper section is written (C-12)." Phase 2 Part B: final Status Quo text with minimum 2 concrete assumptions |
| C-13 | Citation audit precedes Findings | **PASS** (2/2) | "Three structural rules (non-negotiable): 2. CITATION AUDIT block with zero uncited claims must appear before Findings begins (C-13)." Phase 3 CITATION AUDIT block: "Status: [PASS — Findings unlocked] or [BLOCKED]." Hard stop. EVIDENCE COMPLETE marker required in paper |

**V-04 Total: 100/100** — All essential pass. Golden. All three R2 aspirationals declared as non-negotiable structural rules at the prompt header — the strongest forward-declaration of any variation.

---

### V-05: Dual-Skeptic (Split Intervention)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 8 sections present | **PASS** (12/12) | Phase 6 lists: Abstract, Status Quo, Hypothesis, Method, Evidence, Findings, Principles, Limitations, Future Work — all 8 with section-specific guidance |
| C-02 | Hypothesis explicitly resolved | **PASS** (12/12) | Phase 5 HYPOTHESIS VERDICT: "Full verdict sentence: '[Quotable committed sentence]'"; evidence basis E-IDs required; committed sentence format identical to V-04 |
| C-03 | Evidence traceable | **PASS** (12/12) | `E-[N]: [claim] [source: file-path.md, section or item ID]`; HOLD (uncitable) for uncitable claims; EVIDENCE COMPLETE marker: "Post-Skeptic citation audit passed" |
| C-04 | Findings synthesized | **PASS** (12/12) | Post-Skeptic provides novelty scaffold with evidence basis (E-IDs) BEFORE Lead Author writes findings — the strongest pre-classification setup of any variation; conclusion "what does this mean?" required |
| C-05 | Principles actionable | **PASS** (12/12) | "Minimum 2 numbered action-oriented rules." "Always X", "When Y, do Z", "Prefer A over B because..." Each cites finding `P-01 [from F-02]` |
| C-06 | Panel review, 2+ named roles | **PASS** (10/10) | Phase 7: Domain Expert + Practitioner + Pre-Skeptic Check-In (pre-flight items resolved, prediction outcome). Three named roles |
| C-07 | Abstract standalone | **PASS** (10/10) | "<200 words: question, method, key finding, implication. Not structure." |
| C-08 | Future Work concrete | **PASS** (10/10) | "Minimum 2 specific investigable questions. At least one targets a gap from the Status Quo." |
| C-09 | Principles cross-referenced | **PASS** (2/2) | "Each cites its finding: `P-01 [from F-02]: ...`" |
| C-10 | Cold-start readable | **PASS** (2/2) | Method: "Cold-start readable."; Pre-Skeptic writes Status Quo as first session output; orients Lead Author before a word is written |
| C-11 | Findings classified by novelty | **PASS** (2/2) | Post-Skeptic Phase 4 Task B produces NOVELTY SCAFFOLD with per-finding classifications AND evidence basis (E-IDs) committed BEFORE Lead Author writes. "Classifications are set. To reclassify: state reason." |
| C-12 | Status Quo section present | **PASS** (2/2) | Phase 2 Output B: Pre-Skeptic writes final Status Quo text before Lead Author writes anything — "minimum 2 concrete prior beliefs. Not background prose. This is the final Status Quo text — Lead Author inserts it verbatim." |
| C-13 | Citation audit precedes Findings | **PASS** (2/2) | Post-Skeptic Phase 4 Task A: line-by-line audit of every Evidence item as [CITED — source: file.md] or [UNCITED — move to Limitations]; "Total: [N] | Cited: [N] | Uncited (must be 0): [N] Status: [PASS] or [BLOCKED]". If BLOCKED: "Lead Author must fix before Phase 5." Performed by a separate named role |

**V-05 Total: 100/100** — All essential pass. Golden. C-13 is enforced by a separate named role (Post-Skeptic) performing a line-by-line item audit — the most structurally isolated C-13 enforcement of any variation.

---

### Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-02: Citation-Gate | 5/5 | 3/3 | 5/5 | **100** | YES |
| 1 | V-04: Full Integration | 5/5 | 3/3 | 5/5 | **100** | YES |
| 1 | V-05: Dual-Skeptic | 5/5 | 3/3 | 5/5 | **100** | YES |
| 4 | V-01: Status-Quo-Spine | 5/5 | 3/3 | 4.5/5 | **99** | YES |
| 4 | V-03: Novelty-Pre-Classification | 5/5 | 3/3 | 4.5/5 | **99** | YES |

All five variations are Golden. Three score 100. C-13 (citation audit gate) is the only discriminator — it is the exact criterion the R2 rubric added from R1 V-03's excellence signal, and it's the one criterion the R1 champion (V-01) still doesn't implement as a formal gate.

---

### Within-100 structural strength ranking

| Strength | Variation | Basis |
|----------|-----------|-------|
| Strongest | V-05 | Post-Skeptic performs C-13 audit as a separate named role with line-by-line output — role isolation prevents the audit from being skipped or collapsed |
| Strong | V-04 | All three R2 aspirationals declared as non-negotiable rules at the prompt header before any phase — forward declaration is the strongest intent signal |
| Moderate-strong | V-02 | Hard BLOCKED gate is machine-verifiable but no Skeptic pre-flight — loses the R1 excellence signal of risk naming before authoring begins |

---

### Excellence Signals from R2 (patterns that drove 99→100)

1. **Named citation gate with pass/fail output block** — V-02, V-04, V-05 each produce a `CITATION AUDIT` block with explicit Status: PASS/BLOCKED. This is a structured output the model cannot quietly omit; absence of the block is itself a visible failure. V-01 and V-03 rely on format discipline alone — no output block means no verifiable gate.

2. **Non-negotiable rule forward-declaration** — V-04 opens with "Three structural rules (non-negotiable):" naming C-11, C-12, C-13 explicitly before Phase 1. Declaring constraints at the header level rather than embedding them in a later phase makes them harder to ignore under drift.

3. **Role-split for lifecycle separation** — V-05's split into Pre-Skeptic (baseline + risk) and Post-Skeptic (audit + novelty scaffold) gives each role exactly one job with one output format. Single-role designs (V-04's combined Skeptic, V-01's single Skeptic) carry ambiguity about which job takes priority when time is constrained.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named-citation-audit-block-as-hard-gate-before-findings", "non-negotiable-rule-forward-declaration-at-prompt-header", "role-split-for-lifecycle-separation-pre-skeptic-vs-post-skeptic"]}
```
