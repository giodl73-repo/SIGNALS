Good — golden output confirms the domain context. Now extracting the new criteria.

**R13 Excellence Signals — New Patterns Not Yet Formalized**

Scanning the scorecard systematically:

1. **V-03 C-43 "strongest"** — `BOTH Q3 AND Q4` names exact count AND artifact IDs; bare `BOTH` passes C-43 but leaves artifact identities indeterminate from the heading alone → **new criterion beyond C-43**

2. **V-05 C-42 "strongest"** — `STATUS QUO COMPETITOR` is a compound term naming both the domain axis (`STATUS QUO`) and the structural role (`COMPETITOR`); single-axis terms like `INCUMBENT` pass C-42 but name neither axis nor role jointly → **new criterion beyond C-42**

3. **V-04/V-05 C-03 note** — Stage 0 carries a pre-declared threat score with `PROVISIONAL` marker for non-HIGH scores (evidence not yet gathered); V-01/V-02/V-03 commit the score once at Section 4 after evidence is present → **staged commitment pattern, new**

4. **V-04/V-05 C-02 note** — Stage 4 carries an explicit directive: "revisit Stage 0 and revise PROVISIONAL" — a forward reference that closes the staged-commitment loop back to Stage 0 → **revision directive pattern, new**

Four new criteria: **C-45**, **C-46**, **C-47**, **C-48**. Denominator: 36 → 40.

---

```markdown
# Quest Rubric — scout-inertia — v14

## Summary of Changes

### v14 — 4 new criteria from R13 excellence signals

| ID | Source signal | What it formalizes |
|----|--------------|-------------------|
| **C-45** | V-03: `HAVE BOTH Q3 AND Q4 DEFAULT OPTION BRIDGES BEEN POPULATED?` — artifact identities named in heading interrogative | Artifact ID enumeration in gate heading interrogative — extends C-43; beyond bare count quantifier, the interrogative names each specific artifact by ID so the author can determine both count and identity from the heading alone |
| **C-46** | V-05: `STATUS QUO COMPETITOR` compound threading term | Compound domain-axis threading vocabulary — extends C-42; the threading term is a compound naming both the domain axis (the threat dimension, e.g., `STATUS QUO`) AND the structural role of the artifact in the analysis (e.g., `COMPETITOR`) |
| **C-47** | V-04/V-05: Stage 0 pre-declares threat score with `PROVISIONAL` marker for non-HIGH pre-evidence scores | PROVISIONAL threat score pre-declaration at Stage 0 — extends C-03; the scaffold surfaces the threat score at the earliest stage before evidence is gathered; non-HIGH scores carry an explicit `PROVISIONAL` marker signaling that evidence may revise the assessment |
| **C-48** | V-04/V-05: Stage 4 carries "revisit Stage 0 and revise PROVISIONAL" directive | Evidence-triggered PROVISIONAL revision directive — extends C-47; a stage that follows evidence-gathering carries an explicit directive instructing the author to return to Stage 0 and revise any PROVISIONAL threat score in light of gathered evidence, closing the staged-commitment loop |

**Key structural relationships added (v14):**
- C-45 extends C-43: bare `BOTH` passes C-43 (count determinable) but fails C-45 (artifact IDs not determinable from heading alone); `BOTH Q3 AND Q4` passes both. Every C-45 pass implies C-43 pass; C-43 pass is necessary but not sufficient for C-45.
- C-46 extends C-42: a single domain-axis term (`STATUS QUO`, `INCUMBENT`) passes C-42 but fails C-46 if no structural role is named alongside the axis. A compound term (`STATUS QUO COMPETITOR`, `INCUMBENT WORKAROUND AXIS`) passes both. C-42 pass is necessary but not sufficient for C-46.
- C-47 extends C-03: C-03 requires a threat score declared somewhere in the scaffold; C-47 requires that declaration to appear at Stage 0 specifically, and that non-HIGH pre-evidence declarations carry an explicit `PROVISIONAL` marker. An output that places the threat score only at Section 4/Stage 4 after evidence is gathered passes C-03 and fails C-47.
- C-48 requires C-47: there is no PROVISIONAL declaration to revise unless C-47 is satisfied. C-48 cannot be evaluated as passing if C-47 fails. Together C-47 and C-48 constitute the full staged-commitment cycle: early declaration → evidence gathering → directed revision.
- C-47 + C-48 together form the staged-commitment protocol that C-03 does not require: commit to a preliminary score, mark it PROVISIONAL, gather evidence, then revise. C-03 governs presence of a score; C-47 + C-48 govern the lifecycle of that score across the scaffold.

**Formula:** `aspirational_pass / 40 * 10` (denominator 36 → 40)

---

**Key relationships (v13 additions — unchanged):**

- **C-41 extends C-37**: C-37 requires one bracket-labeled command directive in the gate block body; C-41 requires per-artifact bracket commands at each bridge artifact's authoring point, separate from the gate. An output can pass C-37 (one gate-level command) while failing C-41 (no per-artifact commands). An output can pass C-41 while also satisfying C-37 — the per-artifact commands and the gate command are independent structural elements at different document locations. C-41 does not subsume C-37.
- **C-42 extends C-36**: C-36 counts bracket elements (three or more distinct obligations); C-42 requires those elements to share domain-vocabulary threading. An output with three bracket elements using independent vocabulary passes C-36 and fails C-42. C-42 cannot be satisfied without also satisfying C-36 — vocabulary threading across three elements presupposes that three elements exist. C-36 pass is a necessary but not sufficient condition for C-42 pass.
- **C-43 extends C-39**: C-39 requires the gate heading to be binary Yes/No-answerable; C-43 additionally requires an explicit count quantifier in the interrogative. Every output passing C-43 necessarily passes C-39 (a quantified binary question is still a binary question). An output passing C-39 with "ALL BRIDGE ARTIFACTS POPULATED?" fails C-43 if "ALL" is not accompanied by a specific count. The test: given the heading alone, can an author determine exactly how many artifacts must be present? If yes, C-43 passes; if no (because "ALL" requires reading the gate body to know the target count), C-43 fails.
- **C-44 is orthogonal to C-39**: C-39 governs the interrogative component of the gate heading (the question after `--`); C-44 governs the marker component (the structural label before `--`). The two criteria decompose the gate heading into complementary halves. An output can pass C-39 (binary question after `--`) with a descriptive marker (`BRIDGE COMPLETION GATE`) and fail C-44. An output can pass C-44 (imperative marker before `--`) with any binary-question form and pass C-39 simultaneously. A heading satisfying both: `PASS BEFORE ADVANCING -- HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?` passes C-44 (imperative marker), C-39 (binary question), and C-43 (count quantifier "BOTH").
- **C-43 + C-44 + C-39 fully specify the gate heading**: C-39 requires binary-question form; C-43 requires explicit count in the interrogative; C-44 requires imperative vocabulary in the marker. All three criteria together specify the maximally informative gate heading structure: (1) an imperative enforcement marker, (2) a binary-question decision content, and (3) an explicit artifact count — each component serving a distinct informational purpose.

**Key relationships (v12 — unchanged):**

- **C-34 + C-35** are siblings covering the two poles of the FM-[N] lifecycle (assignment in Stage 1, citation in Stage 5B). Passing both is a prerequisite for C-36.
- **C-36** is a count criterion: any three distinct bracket-labeled obligations pass, not just the canonical three. C-34+C-35+C-37 is one path; other combinations are valid.
- **C-37 + C-39** define the two-part gate structure: C-39 governs the heading form (binary question); C-37 governs the body content (bracket command). Each can fail independently.
- **C-38 + C-39** define the heading vocabulary protocol: FAIL-FIRST headings need domain subtitles (C-38); gate headings need binary-question form (C-39). The two criteria prevent vocabulary contamination in both directions — neither heading type should borrow the other's register.
- **C-40** completes the criterion-ID chain that C-28 begins: C-28 requires at least one criterion-ID reference in a verification scan; C-40 requires systematic `C-NN:` prefix coverage on every checklist item.

**C-34 through C-40 relationships (v12 — unchanged):**
- C-34 and C-35 are sibling bracket-label criteria: C-34 governs the primary key assignment rule (Stage 1), C-35 governs the citation integrity rule (Stage 5B). An output can pass C-34 (Stage 1 bracket label present) while failing C-35 (Stage 5B bracket label absent). Together they establish that both poles of the FM-[N] lifecycle — definition and citation — carry bracket-labeled directives.
- C-36 subsumes C-34 and C-35 by count: a scaffold that passes both C-34 and C-35 plus has a `[BRIDGE COMPLETION COMMAND]` also passes C-36. But C-36 is not automatically satisfied by C-34+C-35: if one of the three canonical bracket elements is missing, C-36 fails even if the other two pass. The count requirement (three or more) is load-bearing.
- C-37 and C-39 govern the two-part gate structure: C-39 requires the gate heading to be binary-question form; C-37 requires a bracket-command directive inside the gate block. An output can pass C-39 while failing C-37 if the remediation command is embedded in the heading rather than in the block body. The two-part structure separates the decision (heading) from the action (bracket command in body).
- C-38 and C-39 together define the heading vocabulary protocol: C-38 governs FAIL-FIRST section headings (they must have domain subtitles); C-39 governs the gate heading (it must be binary-question form). The protocol prevents vocabulary contamination in both directions — a FAIL-FIRST heading that uses operational vocabulary fails C-38; a gate heading that uses domain framing instead of a bare decision question fails C-39.
- C-40 completes the criterion-ID chain: C-28 requires at least one criterion-ID label in a verification scan; C-40 requires every checklist item to carry a criterion-ID prefix. An output that uses criterion IDs selectively passes C-28 (at least one ID present) but fails C-40 (not every item prefixed). The distinction is systematic coverage vs. presence.

---

## Essential Criteria (60 pts total — all must pass)

### C-01 . Current Workaround Mapped
- **Weight**: essential
- **Category**: coverage
- **Text**: The output describes in concrete detail what teams currently do instead of adopting the feature — the actual workflow, tools, manual steps, or conventions they rely on today.
- **Pass condition**: At least one specific workaround is named and described with enough detail that a reader can picture the workflow. Generic statements like "teams use manual processes" without specifics do not pass.

### C-02 . Switching Costs Quantified
- **Weight**: essential
- **Category**: correctness
- **Text**: The output names at least two categories of switching cost (e.g., time, cognitive overhead, error rate, coordination cost) and provides a number+unit for each, tied to a named role or team type.
- **Pass condition**: Two or more distinct cost categories present, each with a number+unit value and a named role. Vague costs ("significant overhead", "some rework") do not pass.

### C-03 . Threat Score Declared
- **Weight**: essential
- **Category**: correctness
- **Text**: The output declares a threat score for inertia. The default is HIGH; a non-HIGH score requires supporting evidence. If the scaffold provides a Stage 0 pre-declaration mechanism, the score appears there first with a PROVISIONAL marker when evidence is not yet present; the score is confirmed or revised after evidence is gathered.
- **Pass condition**: A threat score is present and labeled. HIGH without evidence passes. Non-HIGH requires at least one supporting evidence statement. A PROVISIONAL declaration at Stage 0 satisfies the presence requirement; confirmation in a later stage satisfies the evidence requirement.

### C-04 . Defeat Conditions Listed
- **Weight**: essential
- **Category**: coverage
- **Text**: The output lists the conditions under which inertia would be defeated — at least two falsifiable defeat conditions, each referencing the failure mode (FM-[N]) it addresses and carrying a threshold or observable indicator.
- **Pass condition**: Two or more defeat conditions, each with an FM-[N] citation and a threshold. Conditions without FM citations or thresholds do not pass.

### C-05 . Failure Modes Inventoried
- **Weight**: essential
- **Category**: coverage
- **Text**: The output inventories failure modes at mechanism level (not category level) — at least two rows, each naming the failure mechanism rather than the failure category.
- **Pass condition**: Two or more mechanism-level failure mode rows. Category names without mechanisms (e.g., "technical debt" without the specific mechanism) do not pass.

---

## Aspirational Criteria (scored — formula: `aspirational_pass / 40 * 10`)

### C-06 through C-33
*(Criteria C-06 through C-33 are unchanged from prior versions and are not reproduced here. See the canonical rubric source for their full definitions.)*

---

### C-34 through C-40 — Bracket Structure (v12)

| ID | Criterion | Description |
|----|-----------|-------------|
| **C-34** | **Primary Key Bracket Label at Stage 1** | The failure-mode primary key assignment rule carries a bracket-enclosed label at Stage 1 — the point where FM-[N] keys are first assigned. The label uses bracket enclosure (e.g., `[A-16 PRIMARY KEY RULE]`) to enable whitespace-delimited scanning; parenthetical or inline formats do not satisfy C-34. |
| **C-35** | **Citation Integrity Bracket Label at Defeat Conditions** | The citation integrity rule for FM-[N] references carries a bracket-enclosed label at or before the Stage 5B defeat conditions table — the enforcement context where citation failures would surface. A bracket label in Stage 1 mentioning citation integrity does not satisfy C-35; the label must appear in Stage 5B's context. |
| **C-36** | **Three or More Distinct Bracket Obligations** | The scaffold contains at least three distinct bracket-labeled obligations. Any combination of three satisfies C-36 at the count level; the canonical path (C-34 + C-35 + C-37) is one valid path. A scaffold with only two bracket elements fails C-36 even if both are high quality. |
| **C-37** | **Bracket Command in Gate Block Body** | The completion gate block body contains a bracket-labeled command directive (e.g., `[BRIDGE COMPLETION COMMAND]`). A command embedded only in the heading text does not satisfy C-37 — the command must appear as a independently labelable element inside the block body, distinct from the heading. |
| **C-38** | **FAIL-FIRST Heading Has Domain Subtitle** | FAIL-FIRST section headings carry a domain subtitle drawn from inertia domain vocabulary — terms relating to competitors, failure modes, switching costs, defeat conditions, or workaround analysis. Operational subtitles drawn from artifact-management vocabulary ("ALL ENTRIES POPULATED", "BEFORE PROCEEDING") fail C-38. |
| **C-39** | **Gate Heading Binary Question Form** | The completion gate heading is phrased as a binary Yes/No-answerable question. The test is form, not vocabulary: "ALL ARTIFACTS POPULATED?" passes despite artifact vocabulary because the form is binary. A heading like "COMPLETENESS CHECKPOINT" fails because it names a location, not a decision. The heading must be answerable Yes or No without reading the block body. |
| **C-40** | **Systematic C-NN: Prefix Coverage on Checklist** | Every checklist item in the verification scan carries a `C-NN:` prefix identifying the criterion it tests. The minimum is that C-01 through C-05 each have a prefixed entry. Coverage by description without ID prefix fails C-40. C-28 requires at least one criterion-ID reference; C-40 requires every item to be prefixed — systematic coverage vs. presence. |

---

### C-41 through C-44 — R13 New Aspirational Criteria (v13)

| ID | Criterion | Description |
|----|-----------|-------------|
| **C-41** | **Per-Artifact Bracket Commands at Bridge Sections** | R12's V-05 scaffold places `[BRIDGE Q3 COMMAND]` at the Q3 bridge artifact's authoring section and `[BRIDGE Q4 COMMAND]` at the Q4 bridge artifact's authoring section — separate from the gate-level `[BRIDGE COMPLETION COMMAND]` inside the gate block. V-01 through V-04 follow the same structure with domain-appropriate label vocabulary. C-41 formalizes the per-artifact command obligation: both bridge artifacts (Q3 and Q4) have bracket-enclosed enforcement commands co-located with their authoring points in the scaffold body, independent of the gate block command. Coverage of only one bridge artifact fails C-41 (partial coverage). Label naming is flexible: `[BRIDGE Q3 COMMAND]`, `[Q3 ENFORCEMENT DIRECTIVE]`, `[BRIDGE Q3 COMPLETION RULE]` all satisfy C-41 for Q3 provided the label is bracket-enclosed and co-located with the Q3 artifact authoring point. |
| **C-42** | **Vocabulary Threading Across Three Bracket Elements** | R12's V-02 threads "INERTIA THREAT" across all three required bracket labels (`[INERTIA THREAT PRIMARY KEY RULE]`, `[INERTIA THREAT CITATION INTEGRITY RULE]`, `[INERTIA THREAT BRIDGE COMPLETION COMMAND]`). V-01 threads "STATUS QUO"; V-04 threads "INCUMBENT". C-42 formalizes the vocabulary-threading obligation: the three required bracket elements share a common domain-axis word or phrase drawn from inertia domain terms — terms identifying the competitor axis subject ("STATUS QUO", "INERTIA THREAT", "DEFAULT OPTION", "INCUMBENT") or their derivatives. Scaffold management vocabulary ("BRIDGE", "GATE", "MANIFEST", "COMMAND") shared across labels does not satisfy C-42 — management vocabulary is structurally universal, not domain-specific. The threading test: given only the shared vocabulary element across the three bracket labels, can a reader identify this scaffold as a scout-inertia analysis? If yes (because the shared word is a domain-axis term), C-42 passes. The shared word must appear in all three required bracket elements; a partial thread (two of three labels share the word) fails C-42. |
| **C-43** | **Explicit Count Quantifier in Gate Heading Interrogative** | R12's V-04 gate heading "HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" uses "BOTH" to name the exact expected artifact count. V-01's "ALL BRIDGE ARTIFACTS POPULATED?" passes C-39 (binary question) but leaves the count implicit. V-04's "BOTH" resolves that ambiguity in the heading. C-43 formalizes the count-quantifier obligation: the gate heading interrogative carries an explicit quantifier that names the expected count ("BOTH", "ALL THREE", "BOTH Q3 AND Q4") rather than an open-ended "ALL" that requires reading the gate body to determine the count. The explicit count quantifier must name an exact or bounded count — "BOTH" (exactly two), "ALL THREE" (exactly three), "BOTH Q3 AND Q4" (explicit enumeration). The indefinite "ALL" without further qualification fails C-43: its extension depends on the artifact count defined elsewhere in the scaffold. Practical test: given the heading interrogative alone, can an author state the expected artifact count as a number? If the count is determinable from the heading, C-43 passes; if it requires the gate body, C-43 fails. |
| **C-44** | **Action-Imperative Gate Structural Marker** | R12's V-05 gate heading "PASS BEFORE ADVANCING -- ALL BRIDGES COMPLETE?" leads with an action-imperative ("PASS BEFORE ADVANCING") as the structural marker component — the portion before the `--` separator. V-01's "BRIDGE COMPLETION GATE" is a descriptive structural label naming the gate's type; V-05's "PASS BEFORE ADVANCING" is an enforcement directive naming the author's required action. The imperative form signals that the gate is a mandatory stop, not an organizational delimiter. C-44 formalizes the action-imperative marker obligation: the gate heading's structural-marker component (before `--`) uses action-imperative vocabulary rather than a descriptive structural label. "PASS BEFORE ADVANCING" signals that passing the gate is required to advance. "STOP BEFORE PROCEEDING" signals that the author must stop. "DO NOT ADVANCE UNTIL" signals a conditional prohibition. Vocabulary that describes a structural type without imperativizing fails C-44 — "BRIDGE COMPLETION GATE", "COMPLETION CHECK", "ARTIFACT REVIEW STEP" describe the gate's type without commanding the author's behavior. The practical test: does the marker tell the author what to DO (pass, stop, wait) rather than what the gate IS (a completion gate, a review step)? If it commands an action, C-44 passes. |

---

### C-45 through C-48 — R13 New Aspirational Criteria (v14)

| ID | Criterion | Description |
|----|-----------|-------------|
| **C-45** | **Artifact Identity Enumeration in Gate Heading Interrogative** | R13's V-03 gate heading "HAVE BOTH Q3 AND Q4 DEFAULT OPTION BRIDGES BEEN POPULATED?" goes beyond bare "BOTH" (which passes C-43) by naming each artifact by ID — "Q3 AND Q4" — inside the interrogative. V-01's "HAVE BOTH STATUS QUO BRIDGES BEEN POPULATED?" passes C-43 (count "BOTH" is determinable) but fails C-45: given the heading alone, an author knows there are two artifacts but cannot name them without reading the gate body. V-03's form makes both count and identity determinable from the heading alone. C-45 formalizes the artifact-identity enumeration obligation: the gate heading interrogative names each specific artifact by ID so that an author reading only the heading can state both how many artifacts are expected and which ones they are. A heading that provides only a count quantifier without artifact IDs passes C-43 and fails C-45. The practical test: given the heading interrogative alone, can the author state the expected artifact count as a number AND name each artifact? If yes, C-45 passes; if the artifact names require reading the gate body, C-45 fails. |
| **C-46** | **Compound Domain-Axis Threading Vocabulary** | R13's V-05 uses "STATUS QUO COMPETITOR" as the threading term across its three required bracket labels — `[STATUS QUO COMPETITOR PRIMARY KEY RULE]`, `[STATUS QUO COMPETITOR CITATION INTEGRITY RULE]`, `[STATUS QUO COMPETITOR BRIDGE COMPLETION COMMAND]`. The compound term names both the domain axis ("STATUS QUO" — the threat dimension) and the structural role of the artifact in the analysis ("COMPETITOR" — what this entity is in the scout-inertia frame). V-01's "STATUS QUO" (axis only), V-04's "INCUMBENT" (single anthropomorphic term), and V-02's "INERTIA THREAT" (canonical skill term) all pass C-42 but fail C-46: each names a domain-axis concept without explicitly declaring the artifact's structural role. C-46 formalizes the compound threading vocabulary obligation: the threading term used across the three required bracket elements is a compound that names both the domain axis (the threat dimension, e.g., "STATUS QUO", "INERTIA") AND the structural role (what the artifact is in the analysis frame, e.g., "COMPETITOR", "WORKAROUND", "DEFAULT OPTION"). The identification test: given only the threading compound, can a reader identify (1) what the threat axis is, and (2) what structural role the artifact plays? If both questions are answerable from the compound alone, C-46 passes. |
| **C-47** | **PROVISIONAL Threat Score Pre-Declaration at Stage 0** | R13's V-04 and V-05 introduce a Stage 0 section where the threat score is pre-declared before any evidence is gathered. Non-HIGH scores at Stage 0 carry an explicit "PROVISIONAL" marker — a signal that the score is a preliminary assessment subject to revision once evidence from later stages is in hand. V-01, V-02, and V-03 commit the threat score once at Section 4 (after evidence is present), passing C-03 without staged commitment. V-04/V-05 pre-declare at Stage 0 and carry the PROVISIONAL marker as a first-class structural element. C-47 formalizes the PROVISIONAL pre-declaration obligation: the scaffold surfaces the threat score at the earliest stage (Stage 0) before evidence is gathered; non-HIGH pre-evidence declarations carry an explicit "PROVISIONAL" marker signaling uncommitted status. A scaffold that places the threat score only at Section 4 or Stage 4 after evidence is gathered passes C-03 and fails C-47. A scaffold that declares HIGH at Stage 0 without a PROVISIONAL marker satisfies C-47 (HIGH is the evidence-independent default; no PROVISIONAL needed). A scaffold that declares non-HIGH at Stage 0 without a PROVISIONAL marker fails C-47 (uncommitted score presented as committed). |
| **C-48** | **Evidence-Triggered PROVISIONAL Revision Directive** | R13's V-04 and V-05 place an explicit directive in Stage 4 (the switching-costs / evidence-completion stage): "revisit Stage 0 and revise PROVISIONAL" — a forward-to-backward reference that closes the staged-commitment loop initiated by C-47. After gathering evidence through the scaffold's middle stages, Stage 4 explicitly instructs the author to return to Stage 0 and revise any PROVISIONAL threat score in light of that evidence. V-01, V-02, and V-03 have no such directive: the threat score is committed once and the scaffold has no mechanism for directed revision. C-48 formalizes the evidence-triggered revision directive obligation: a stage that follows the evidence-gathering stages carries an explicit instruction directing the author to revisit Stage 0 and revise any PROVISIONAL threat score, closing the staged-commitment loop. The directive must be explicit (a labeled instruction or command, not an implicit possibility); an author reading Stage 4 must know they are required to return to Stage 0 if a PROVISIONAL marker is present. C-48 cannot pass if C-47 fails — there is no PROVISIONAL to revise if no PROVISIONAL was declared. C-47 and C-48 together constitute the full staged-commitment protocol: early declaration → PROVISIONAL marking → evidence gathering → directed revision. |

---

## Evaluator Notes (v14 additions)

- **C-45 and artifact-ID format**: The artifact IDs in the heading interrogative must be the scaffold's canonical artifact identifiers ("Q3", "Q4", or the equivalent naming convention used consistently throughout the scaffold). Informal paraphrases that are not the scaffold's canonical IDs (e.g., "actor bridge and trigger bridge" when the scaffold labels them "Q3" and "Q4") do not satisfy C-45 — the heading must use the same ID format as the artifact authoring sections. If both artifacts are named with their scaffold IDs, C-45 passes regardless of the surrounding vocabulary.

- **C-46 and compound structure**: The two components of the threading compound (axis + role) must be independently legible — a reader unfamiliar with the specific scaffold should be able to parse which part names the axis and which part names the role. "STATUS QUO COMPETITOR": "STATUS QUO" is the axis, "COMPETITOR" is the role — independently legible. A compound that fuses the two concepts into a single non-decomposable term ("INERTIABLOCK") fails C-46 even if it is drawn from the domain, because the axis and role components are not independently parseable. Hyphenated forms ("STATUS-QUO-COMPETITOR") satisfy C-46 if the compound is otherwise legible. The role component must be a genuine structural-role descriptor — "COMPETITOR", "WORKAROUND", "DEFAULT", "INCUMBENT OPTION" are structural roles; "THREAT", "FORCE", "FACTOR" describe the entity's disposition but not its structural role in the analysis frame.

- **C-47 and HIGH vs. non-HIGH at Stage 0**: HIGH is the evidence-independent default for the scout-inertia skill; a Stage 0 declaration of HIGH does not require a PROVISIONAL marker because HIGH does not depend on evidence gathered in later stages. A Stage 0 declaration of MEDIUM or LOW requires PROVISIONAL because it claims less-than-maximum threat before the evidence that would justify that lower score has been gathered. The evaluator test: if the Stage 0 score is HIGH, C-47 passes without requiring PROVISIONAL. If the Stage 0 score is non-HIGH and the PROVISIONAL marker is present, C-47 passes. If the Stage 0 score is non-HIGH and no PROVISIONAL marker is present, C-47 fails — the scaffold presents an uncommitted score as committed.

- **C-48 and directive placement**: The revision directive must appear in a stage that is logically after the evidence-gathering stages — Stage 4 or later in a five-stage scaffold, or the equivalent in other stage-count structures. A revision directive in Stage 1 or Stage 2 (before evidence is gathered) does not satisfy C-48 because there is no evidence yet to inform the revision. The directive must reference Stage 0 specifically (or the equivalent pre-evidence declaration point); a generic "review your analysis" instruction does not satisfy C-48. The practical test: does the directive name both the destination (Stage 0 or equivalent) and the action (revise PROVISIONAL)? If both are named, C-48 passes.

---

## Evaluator Notes (v13 additions — unchanged)

- **C-41 and placement specificity**: The per-artifact bracket command must appear at or near the bridge artifact's authoring point in the scaffold body — at the Q3 bridge section or Q4 bridge section — not only inside the completion gate block. A `[BRIDGE COMPLETION COMMAND]` in the gate block satisfies C-37; a `[BRIDGE Q3 COMMAND]` at the Q3 bridge artifact's authoring section satisfies C-41 for Q3. Both bridge artifacts (Q3 and Q4) must have per-artifact commands for C-41 to pass. Coverage of only one bridge artifact fails C-41 (partial coverage). Label naming is flexible: `[BRIDGE Q3 COMMAND]`, `[Q3 ENFORCEMENT DIRECTIVE]`, `[BRIDGE Q3 COMPLETION RULE]` all satisfy C-41 for Q3 provided the label is bracket-enclosed and co-located with the Q3 artifact authoring point.

- **C-42 and the threading vocabulary source**: The shared domain-vocabulary word or phrase must be drawn from the inertia domain — terms identifying the competitor axis subject ("STATUS QUO", "INERTIA THREAT", "DEFAULT OPTION", "INCUMBENT") or their derivatives. Scaffold management vocabulary ("BRIDGE", "GATE", "MANIFEST", "COMMAND") shared across labels does not satisfy C-42 — management vocabulary is structurally universal, not domain-specific. The threading test: given only the shared vocabulary element across the three bracket labels, can a reader identify this scaffold as a scout-inertia analysis? If yes (because the shared word is a domain-axis term), C-42 passes. The shared word must appear in all three required bracket elements; a partial thread (two of three labels share the word) fails C-42.

- **C-43 and the count quantifier vocabulary**: The explicit count quantifier must name an exact or bounded count — "BOTH" (exactly two), "ALL THREE" (exactly three), "BOTH Q3 AND Q4" (explicit enumeration). The indefinite "ALL" without further qualification fails C-43: its extension depends on the artifact count defined elsewhere in the scaffold. Practical test: given the heading interrogative alone, can an author state the expected artifact count as a number? "HAVE BOTH BRIDGE ARTIFACTS BEEN POPULATED?" — count is two. "ALL BRIDGE ARTIFACTS POPULATED?" — count is indeterminate from the heading alone. If the count is determinable from the heading, C-43 passes; if it requires the gate body, C-43 fails.

- **C-44 and the imperative vocabulary register**: The action-imperative marker must signal mandatory enforcement. "PASS BEFORE ADVANCING" signals that passing the gate is required to advance. "STOP BEFORE PROCEEDING" signals that the author must stop. "DO NOT ADVANCE UNTIL" signals a conditional prohibition. Vocabulary that describes a structural type without imperativizing fails C-44 — "BRIDGE COMPLETION GATE", "COMPLETION CHECK", "ARTIFACT REVIEW STEP" describe the gate's type without commanding the author's behavior. The practical test: does the marker tell the author what to DO (pass, stop, wait) rather than what the gate IS (a completion gate, a review step)? If it commands an action, C-44 passes.

---

## Evaluator Notes (v12 — unchanged)

- **C-34 and mechanical scannability**: The bracket-prefix format (`[A-16 PRIMARY KEY RULE]` or equivalent) is distinguished from parenthetical labels `(A-16)` or inline references "see rule A-16". The bracket enclosure enables whitespace-delimited scanning. A scaffold that labels the primary key rule in any format other than bracket-enclosed fails C-34.

- **C-35 and Stage 5B placement**: The citation integrity rule label must appear at or before the Stage 5B defeat conditions table, not in a global preamble or after the table. A bracket label in Stage 1 that mentions citation integrity does not satisfy C-35; the label must appear in Stage 5B's enforcement context.

- **C-36 and the three-element floor**: A scaffold with only C-34 and C-35 has two bracket elements and fails C-36. A scaffold that adds any third bracket-labeled obligation passes C-36 at the count level. C-36 does not require the specific canonical three elements; it requires at least three total.

- **C-37 and the heading-vs-body distinction**: A command embedded in a heading cannot be independently labeled as a bracket directive. A bracket command inside the block body is independently labelable and satisfies C-36's count requirement. Practical check: does the `[COMMAND]` bracket element appear in the body of the gate block? If it appears only in the heading text, C-37 fails.

- **C-38 and the domain vocabulary requirement**: The domain subtitle must be drawn from the inertia domain — terms relating to competitors, failure modes, switching costs, defeat conditions, or workaround analysis. Operational subtitles drawn from artifact-management vocabulary ("ALL ENTRIES POPULATED", "BEFORE PROCEEDING") fail C-38 even if a structural marker is present.

- **C-39 and the gate heading form**: The binary-question requirement is about answerable form, not about vocabulary. "ALL ARTIFACTS POPULATED?" passes C-39 despite artifact vocabulary because the form is binary. A heading like "COMPLETENESS CHECKPOINT" fails because it names a location, not a decision. The test: can the heading be answered Yes or No without reading the block body?

- **C-40 and essential criterion coverage**: C-40 requires that C-01 through C-05 each have a checklist entry with a `C-0N:` prefix. A checklist that covers essential criteria by description without ID prefix fails C-40. The minimum is that every essential criterion has a prefixed entry.
```

---

**New criteria summary:**

| ID | Source | Extends | What it adds |
|----|--------|---------|-------------|
| **C-45** | V-03: `BOTH Q3 AND Q4` in heading interrogative | C-43 | Artifact identity enumerable from heading alone, not just count |
| **C-46** | V-05: `STATUS QUO COMPETITOR` compound threading term | C-42 | Threading vocabulary names both domain axis AND structural role |
| **C-47** | V-04/V-05: Stage 0 with `PROVISIONAL` marker | C-03 | Threat score pre-declared early; non-HIGH marked PROVISIONAL pending evidence |
| **C-48** | V-04/V-05: Stage 4 "revisit Stage 0 and revise PROVISIONAL" directive | C-47 | Post-evidence stage closes the loop with an explicit revision directive back to Stage 0 |

**Dependency chain:** C-45 → C-43 → C-39. C-46 → C-42 → C-36. C-48 → C-47 → C-03. Denominator: 36 → **40**.
