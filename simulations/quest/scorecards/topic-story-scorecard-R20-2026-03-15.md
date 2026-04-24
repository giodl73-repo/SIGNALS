## Round 20 Scoring — topic-story (v19 rubric)

### Scoring context

All 5 variations inherit the V-04 R19 base, which scored 195.0/197.5 against v19 (passing all 47 inherited criteria, failing only C-48). The delta available is 2.5 (C-48 PASS). R20's single engineering question: which C-48 mechanism reliably produces differentiated resolution path tags?

C-46 re-certification is not required — V-04 R19 labels (`Pattern necessity test (apply before finalizing this beat):`, `Proportionality audit (required final act before closing this beat):`, `Completeness gate (apply before finalizing this beat):`) already encode action name + positional marker as a single typographic unit.

---

### Per-criterion scoring — C-01 through C-47

All five variations inherit V-04 R19 base unchanged for criteria C-01 through C-47. All essential, recommended, and aspirational criteria pass as established in R19. Scoring below addresses only the differentiating criterion.

| ID | All 5 variants | Evidence |
|----|----------------|----------|
| C-01 | PASS | BLUF enforcement via editorial brief genre frame (C-42), verdict-first output |
| C-02 | PASS | Five named beats enforced in AUTHOR phase |
| C-03 | PASS | Beat 3 cross-signal scan + pattern necessity test |
| C-04 | PASS | Pattern necessity test label enforces relationship/tension/gap, not A+B list |
| C-05–C-07 | PASS | Signal attribution, uncertainty specificity, proportionality audit all present |
| C-08–C-47 | PASS | All 40 inherited aspirational criteria pass (V-04 R19 baseline) |

---

### C-48 evaluation per variation

**C-48 pass condition**: Each UNRESOLVED item in Beat 4 tagged with a resolution path type from `SIGNAL_PATH | EXPERIMENT_PATH | DECIDE_PATH`. Uniform tags across all items fail — the taxonomy earns its place only when it produces differentiated classifications.

---

#### V-01 — Output format: minimal one-line constraint

**C-48 mechanism**: `Resolution path:` format field per Beat 4 item + prose differentiation constraint: *"At least two distinct path types must appear across all items. Uniform tags (all items carrying the same type) indicate undifferentiated classification and fail the taxonomy check."*

**Assessment**: The constraint is explicit and states the failure consequence directly. It encodes the differentiation requirement as a declarative rule rather than a named action. The model reads the taxonomy instruction, the format field, and the rule. Weakness: the prose constraint does not include a recovery instruction — if a model generates uniform tags and hits the completeness gate, the gate does not direct what to do next. The completeness gate in V-01 only checks count match and fill, not differentiation.

**C-48**: **PASS** — explicit differentiation rule present and failure consequence named; weaker than named-label approaches because no recovery instruction for the uniform-tag case.

**Score**: 197.5

---

#### V-02 — Lifecycle: C-46-form differentiation audit sub-step

**C-48 mechanism**: Named sub-step `Differentiation audit (apply before finalizing this beat):` with three-class definitions embedded in the body + recovery instruction: *"If all items remain SIGNAL_PATH after review, state explicitly why EXPERIMENT_PATH and DECIDE_PATH do not apply."*

**Assessment**: This uses the same C-46 structural pattern that enforces necessity tests and proportionality audits in Beat 3. The label encodes the action (`Differentiation audit`) and positional marker (`apply before finalizing this beat`) as a single typographic unit — matching C-46 pass conditions. The body provides both a re-examination pathway and a fallback: "state explicitly why" serves as an escape hatch that forces visible acknowledgment rather than silent uniform tagging. This is the strongest AUTHOR-phase C-48 defense.

**C-48**: **PASS** — named action label + positional marker + three-class definitions + recovery instruction for uniform-tag case.

**Score**: 197.5

---

#### V-03 — Phrasing register: example-anchored conversational definitions

**C-48 mechanism**: Three-class definitions with concrete examples (e.g., *"a scout:competitors run would surface whether a rival has already solved this"* for SIGNAL_PATH; *"building a quick prototype"* for EXPERIMENT_PATH; *"whether to target enterprise or consumer first"* for DECIDE_PATH). Behavioral nudge: *"Not all items will resolve to the same type. If you look at your uncertainty list and every item maps to SIGNAL_PATH, pause..."* Differentiation check embedded in completeness gate: *"Not all items carry the same Resolution path type."*

**Assessment**: The example-anchored definitions are the clearest taxonomy instruction in any variation — a model reading V-03 understands the three types more concretely than from brief formal definitions. The completeness gate includes differentiation as a check condition. However, the gate condition *"Not all items carry the same Resolution path type"* is a check, not a recovery instruction. If a model produces uniform tags, the gate check fails — but V-03 provides no directive for what to do in that case. The prose nudge *"pause"* is behavioral, not structural. A model may acknowledge the uniform-tag failure without correcting it. The example definitions reduce the probability of mis-classification, but the lack of a recovery loop is the structural gap.

**C-48**: **PARTIAL** — differentiation check present in completeness gate, example-anchored definitions reduce mis-classification risk, but no recovery instruction for uniform-tag case; enforcement relies on register rather than structural compulsion.

**Score**: 195.0

---

#### V-04 — Role sequence: EVALUATOR pre-classifies in E-5

**C-48 mechanism**: `Resolution path:` column added to E-5 Conflict Register. EVALUATOR classifies each UNRESOLVED row before any narrative writing. Three-class definitions provided. **Path diversity check** after E-5 classification: *"After classifying all UNRESOLVED rows, verify the tags are not uniform. If all UNRESOLVED items carry the same tag, re-examine each: is the distinction between investigation-closable and decision-required genuinely absent, or has the classification collapsed due to insufficient attention to mechanism type?"* AUTHOR Beat 4 is pure transfer: *"Auto-transfer only from E-5 UNRESOLVED rows... No new items, no omissions, no tag changes."* Completeness gate verifies verbatim tag fidelity.

**Assessment**: This is the cleanest architecture for C-48. The EVALUATOR works analytically on the conflict register, not in narrative flow — classification happens before prose pressure. The path diversity check fires after classification, before sealing, and includes a mechanism-type re-examination framing. AUTHOR discretion over classification is eliminated entirely: the tags are frozen at E-5 and copied verbatim. A model cannot drift to uniform tags in narrative flow because the tags are pre-determined. The diversity check handles the re-examination; the auto-transfer handles the fidelity.

**C-48**: **PASS** — EVALUATOR-phase pre-classification with path diversity check eliminates AUTHOR-phase uniform-tagging risk; auto-transfer with verbatim fidelity requirement closes the transfer gap.

**Score**: 197.5

---

#### V-05 — Combination: E-5 pre-classify + AUTHOR named audit sub-step + axiom grammar

**C-48 mechanism**: Three mechanisms stacked:
1. **EVALUATOR E-5**: `Resolution path:` column + three-class definitions + **Path diversity check (complete before sealing E-5)** — *"Verify UNRESOLVED rows carry at least two distinct Resolution path types. If all items are SIGNAL_PATH: distinguish which items could be closed by further gathering vs which require a new test vs which require a commitment."*
2. **AUTHOR**: `Differentiation audit (apply before finalizing this beat):` sub-step — *"Verify the Resolution path tags across Beat 4 items are not uniform. If every item carries the same tag, the E-5 path diversity check did not prevent homogeneous classification. **Return to E-5 and revise before proceeding.**"*
3. **Axiom grammar** for C-38: constitutive framing throughout (C-38 AXIOM record, VECTOR-STATUS AXIOM in mid-draft protocol).

**Assessment**: V-05 addresses two distinct failure modes that single-phase approaches cannot: (1) EVALUATOR classifying uniformly before sealing E-5, caught by the path diversity check; (2) AUTHOR inadvertently changing tags during transfer, caught by the differentiation audit. The AUTHOR differentiation audit includes a **return-to-E-5** instruction — the only variation with an explicit correction loop that goes back to the classification source. This closes the gap that all other variations leave: a model that generates uniform tags has a named, directed recovery path. The axiom grammar ensures C-38/C-39 compliance is not disrupted by the taxonomy addition.

**C-48**: **PASS (strongest)** — dual-phase enforcement addresses both E-5 classification failure and AUTHOR transfer drift; return-to-E-5 recovery instruction is the only cross-phase correction loop present in any variation.

**Score**: 197.5

---

### Composite scores

| Variation | C-01–C-47 | C-48 | Score | Rank |
|-----------|-----------|------|-------|------|
| V-05 | 40/40 PASS | PASS (strongest — dual-phase + return loop) | **197.5** | 1 |
| V-04 | 40/40 PASS | PASS (EVALUATOR pre-classification + diversity check) | **197.5** | 2 |
| V-02 | 40/40 PASS | PASS (C-46-form AUTHOR audit + recovery instruction) | **197.5** | 3 |
| V-01 | 40/40 PASS | PASS (prose constraint, no recovery instruction) | **197.5** | 4 |
| V-03 | 40/40 PASS | PARTIAL (gate check present, no recovery, relies on register) | **195.0** | 5 |

Within-tier distinctions (all 197.5):

- **V-05 > V-04 > V-02 > V-01** in C-48 defense depth. V-05 is the only variation with a cross-phase recovery loop (return-to-E-5 from AUTHOR). V-04 has the cleanest architecture (EVALUATOR-only, no AUTHOR discretion). V-02 has the strongest AUTHOR-phase label. V-01 has the weakest recovery (no recovery instruction at all, just a failure statement).

---

### Excellence signals from V-05

**ES-01 — Cross-phase correction loop closes the taxonomy gap**: V-05's AUTHOR differentiation audit includes `"Return to E-5 and revise before proceeding"` — a direction to return to the classification source, not just acknowledge a gate failure. This is the only variation where uniform-tag failure has a named, directed recovery path that goes back to the analytical phase.

**ES-02 — Path diversity check positioned before sealing (not after)**: V-05's E-5 path diversity check reads *"complete before sealing E-5"* — a positional marker that forces re-examination before the classification is locked. V-04's check reads *"after classifying all UNRESOLVED rows"* without an explicit sealing gate anchor.

**ES-03 — Dual-phase addresses orthogonal failure modes**: EVALUATOR-phase uniform tagging (classification error at analysis) and AUTHOR-phase tag drift (fidelity error at transfer) are distinct failure modes. V-05 is the only variation that addresses both. V-04 addresses only the first; V-02 addresses only the second.

---

### Discriminator findings

- **V-03 < V-01**: Conversational register + example-anchored definitions are insufficient for reliable C-48 pass. A formal differentiation gate (even prose) outperforms register-based enforcement. Formal gate is load-bearing.
- **V-02 > V-01**: The C-46-form named sub-step label produces stronger enforcement than a prose constraint for the same requirement — the label encodes the action as an explicit structural act, while prose encodes it as a rule the model may honor or not.
- **V-05 > V-04**: The combination adds value over EVALUATOR-only pre-classification. The AUTHOR differentiation audit provides an independent second-check that catches E-5 diversity check failures that propagated through.

---

```json
{"top_score": 197.5, "all_essential_pass": true, "new_patterns": ["EVALUATOR-phase taxonomy pre-classification eliminates AUTHOR-phase uniform-tagging risk by separating classification from narrative flow", "Dual-phase differentiation enforcement (EVALUATOR path diversity check + AUTHOR differentiation audit) addresses orthogonal failure modes: classification error and transfer drift", "Recovery instruction in differentiation gate must direct return to classification source — a check-only gate without a named correction loop leaves the uniform-tag failure unresolvable"]}
```
