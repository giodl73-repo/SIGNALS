Reading the R7 scorecard carefully before extracting signals.

**Excellence signals identified:**

1. **V-02 C-09 pass mechanism** — "KEY EVIDENCE table column: 'Why This Rank (Not the One Below)' — comparative question present for each rank." C-09 fires when comparative language exists; what V-02 adds is a *structurally required slot per rank position*, making bypass visible as a gap. This is a structural enforcement of C-09 that C-09 itself doesn't require.

2. **V-01 C-11 pass mechanism** — "SKEPTIC names confirmation bias, softening; SYNTHESIST names hedging and summarizing." C-11 fires when anti-pattern gates exist; what V-01 adds is each role *naming its own* failure mode at role definition — not a central list. The gate is owned by the role it constrains.

3. **V-02 C-21 pass mechanism** — "failure mode derived from pattern of top 5 signals." C-17 fires when challenge is record-structural; what V-02 adds is the challenge derived from *aggregate signal distribution* (N-of-M pattern) rather than a single signal's properties — a class of failure only visible by examining the inventory as a whole.

**Tension note:** C-29 can be satisfied via table column (V-02's method, which fails C-12) or via labeled prose subsection per rank entry. Both C-12 and C-29 can be satisfied simultaneously via per-rank prose slots; table-column implementation satisfies C-29 while failing C-12.

---

```markdown
# prove-synthesize-rubric-v8-2026-03-14.md

## prove-synthesize — Rubric v8

**Version**: v8 (2026-03-14)
**Predecessor**: v7 (2026-03-14)
**Golden threshold**: all essential pass AND composite >= 90
**Max composite**: 147.5

---

## New in v8 — Three Aspirational Criteria from R7 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-29 | Per-rank comparative slot | C-09 | Each rank position in the evidence section has a structurally required comparative assignment — a named column, labeled subsection, or enumerated sub-item that asks "why this rank, not the one below" for that position specifically. The slot appears at every rank; its absence at any rank is a visible structural gap. NOT: comparative language present only as prose commentary after the full ranking. NOT: single comparative note covering all rank positions without per-rank assignment. |
| C-30 | Role-native failure mode ownership | C-11 | Each cognitive role (or phase) explicitly names the failure mode characteristic of its own phase — the failure it is at risk of exhibiting — at role definition or role instruction. ANALYST names its collection-phase bias; SKEPTIC/ADVERSARY names its adversarial-phase failure (e.g., generic challenge instead of structural challenge); SYNTHESIST/JUDGMENT names its judgment-phase failure (e.g., hedging, summarizing). NOT: anti-patterns listed centrally without assignment to the role that exhibits them. NOT: role definitions that describe duties only; anti-pattern gates appear only at output level. |
| C-31 | Pattern-of-N adversarial input | C-17 | The adversarial challenge is derived from the aggregate pattern of multiple top signals, not a single signal in isolation. The record-specific failure mode names a distribution property (e.g., "N of the top M signals share the same source type," "the top K signals all point in the same direction without cross-type confirmation") that is only visible by examining the signal inventory as a whole. The count or range is stated. NOT: adversarial challenge targeting one signal's properties only. NOT: aggregate pattern claimed but signal count not stated or not cross-referenced to the inventory. |

---

## Scoring Delta

| | v7 | v8 |
|-|----|-----|
| Aspirational | 50.0 pts / 20 criteria | **57.5 pts / 23 criteria** |
| Max composite | 140.0 | **147.5** |
| Golden threshold | >= 90 | >= 90 (unchanged) |

---

## R7 Calibration Under v8

| Variation | v7 score | C-29 | C-30 | C-31 | v8 score |
|-----------|----------|------|------|------|----------|
| V-01 Role-Sequence | 110.0 | FAIL | **PASS** | FAIL | **112.5** |
| V-02 Tables + SURVEYOR + Arrow-Chain | 112.5 | **PASS** | FAIL | **PASS** | **117.5** |

**V-01 C-29 FAIL**: Comparative language in prose ("more than the others") without per-rank structural slots.
**V-01 C-30 PASS**: SKEPTIC names "confirmation bias, softening" — its own phase bias; SYNTHESIST names "hedging and summarizing" — its own phase failure. Role-native ownership at role instruction level.
**V-01 C-31 FAIL**: V-01 C-17 FAIL (no record-structural derivation); pattern-of-N requires C-17 as prerequisite.
**V-02 C-29 PASS**: TABLE COLUMN "Why This Rank (Not the One Below)" — forced per-rank comparative slot. Note: V-02 FAILS C-12 (table not permitted for evidence ranking); C-12 and C-29 are in tension — both can be satisfied simultaneously via per-rank labeled prose subsections rather than table columns.
**V-02 C-30 FAIL**: ADVERSARY phase describes its OUTPUT task ("name the exact vulnerability") but does not name the failure mode ADVERSARY is at risk of exhibiting (e.g., generic challenge instead of structural challenge). Role-native ownership requires the self-directed failure mode be stated at role definition.
**V-02 C-31 PASS**: "failure mode derived from pattern of top 5 signals" — adversarial input examines signal distribution; count stated.

---

## Criterion Dependency Relationships

**C-09/C-29**: C-09 requires comparative language for each rank — "why this signal over the one below it?" present in the output. C-29 requires that comparative question be assigned to a structurally required slot per rank position — the comparison is demanded by structure, not by instruction alone. A prose section with comparative language satisfies C-09; only a design where each rank position has a named comparative slot satisfies C-29. C-09 is necessary but not sufficient for C-29.

**C-11/C-30**: C-11 requires named anti-pattern gates that foreclose specific failure modes — gates present somewhere in the skill instruction. C-30 requires each gate be assigned to the cognitive role that exhibits the failure mode — each role owns its anti-pattern at role definition. Anti-patterns listed centrally satisfy C-11; only role-owned anti-patterns at role definition satisfy C-30. C-11 is necessary but not sufficient for C-30.

**C-17/C-31**: C-17 requires the adversarial challenge be derived from this record's structural properties — a record-specific, not generic, failure mode. C-31 requires the challenge be derived from the aggregate pattern of multiple signals — a distribution property not visible from any single signal. A single-signal structural derivation satisfies C-17; only a pattern-of-N derivation that names the signal count satisfies C-31. C-17 is necessary but not sufficient for C-31.

**C-12/C-29 tension**: C-12 prohibits table formatting for evidence ranking. C-29 rewards a per-rank comparative slot, which can be implemented as a table column (as in V-02) or as a labeled prose subsection per rank entry. Table-column implementation satisfies C-29 while failing C-12; labeled-prose implementation satisfies both. The tension is a feature — the highest-quality artifacts satisfy both via non-table per-rank slots.

**C-23/C-26**: C-23 requires named violation categories inline at each fill-window bound — the writer encounters the violation name when reading the constraint. C-26 requires all violation categories be indexed as a named registry block before FRONTMATTER begins — the violation taxonomy is visible before the first constraint is encountered. Inline naming satisfies C-23; front-indexing requires the additional registry block. C-23 is necessary but not sufficient for C-26.

**C-24/C-25/C-27**: C-24 requires arrow-chain field:value notation in RECORD DIAGNOSIS. C-25 requires a named PRE-FLIGHT structural phase between ADVERSARY and JUDGE. C-27 requires the arrow-chain propagate across all three named sites — RECORD DIAGNOSIS creates the chain, PRE-FLIGHT Phase B audits it, JUDGE confidence paragraph applies it. C-24 and C-25 are each necessary but not sufficient for C-27.

**C-25/C-28**: C-25 requires a named PRE-FLIGHT structural phase exist as a sequenced block between ADVERSARY and JUDGE. C-28 requires an explicit anti-skip gate at PRE-FLIGHT entry that names the bypass failure mode (PHASE-ADVANCE VIOLATION or equivalent) before any PRE-FLIGHT phase step is listed. PRE-FLIGHT that begins with its phase steps satisfies C-25; only PRE-FLIGHT that begins with a named entry gate satisfies C-28. C-25 is necessary but not sufficient for C-28.

**C-11/C-12 tension**: Confirmed across R2–R7. Both criteria remain; the tension is a feature.

**C-17/C-21**: C-17 requires the failure mode be derived from the record's structural properties. C-21 requires those properties be traceable to the SURVEYOR phase inventory — verifiable by cross-reference, not merely plausible. Both can be satisfied independently; the highest-quality artifacts satisfy both.

**C-18/C-22**: C-18 fires when the register word opens the commitment sentence at the output level. C-22 requires an explicit NOT: gate at the instruction level. C-18 is necessary but not sufficient for C-22.

**C-19/C-20**: C-19 requires the frontmatter block exist and prohibits retroactive completion. C-20 requires each field be filled at its individually correct structural moment — phase-sequenced, not batch-filled at start or end.

**C-20/C-23**: C-20 requires per-field NOT: gates bounding the fill window at both ends. C-23 requires each bound be expressed as a named violation category. Named violations create addressable failure types; unnamed prohibitions do not. C-20 is necessary but not sufficient for C-23.

**C-21/C-24**: C-21 requires the adversarial challenge cite structural properties cross-referenceable to the SURVEYOR inventory. C-24 requires that citation be expressed as field:value notation within the RECORD DIAGNOSIS text. C-21 is satisfied by prose derivation; C-24 requires the explicit field:value syntax. C-21 is necessary but not sufficient for C-24.

**C-22/C-25**: C-22 requires dual-layer register-word enforcement — output-level format plus instruction-level NOT: gate. C-25 requires the instruction-level gate be a named structural phase (PRE-FLIGHT or equivalent) positioned between ADVERSARY and JUDGE. A DETERMINATION SEAL gate (C-22) is encountered at the moment of commitment; a PRE-FLIGHT gate (C-25) is encountered before commitment begins. C-22 is necessary but not sufficient for C-25.

---

## R7 Q-Answer Confirmations

**(Q1) C-29**: Per-rank slot fires on V-02 TABLE COLUMN — "Why This Rank (Not the One Below)" is a structural per-rank slot. V-01 prose comparative language satisfies C-09 only; no per-rank slot present. The slot must be structurally assigned at each rank position; prose around the ranking does not satisfy.

**(Q2) C-30**: Role-native ownership fires on V-01 — SKEPTIC names "confirmation bias, softening" (SKEPTIC's own phase risk); SYNTHESIST names "hedging and summarizing" (SYNTHESIST's own phase risk). Role definition is the correct locus. Central anti-pattern list without role assignment satisfies C-11 only; V-02 phase descriptions name adversarial OUTPUT task, not adversarial phase risk.

**(Q3) C-31**: Pattern-of-N fires on V-02 — "failure mode derived from pattern of top 5 signals" names the count (5) and derives from distribution, not a single signal. C-17 is the prerequisite; V-01 fails C-17 therefore cannot reach C-31.

---

## Essential Criteria (weight: 60 points total — 12 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Answer-first** | format | The synthesis opens with a direct answer to the hypothesis before any evidence or reasoning. The answer is a complete declarative sentence, not a hedge or a restatement of the question. |
| C-02 | **Confidence score present and calibrated** | correctness | A numeric confidence score (0–100) is stated. It is calibrated: high confidence (>=75) only when evidence strongly converges; low confidence (<=40) when evidence is mixed or thin. |
| C-03 | **Key evidence cited** | coverage | Exactly or up to 3 signals are named as key evidence. Each named signal is traceable to an artifact produced during the investigation (not invented). Each signal is explained in terms of *why* it influenced the answer. |
| C-04 | **Counter-evidence present** | correctness | At least one piece of evidence arguing *against* the answer is explicitly named. If none exists, the output states "no counter-evidence found" with a brief rationale. Omitting this section entirely is a fail. |
| C-05 | **Synthesis supersedes signals** | behavior | The synthesis takes a position — it does not merely restate or list the investigation signals. The answer and confidence together constitute a judgment call, not a summary. |

---

## Recommended Criteria (weight: 30 points total — 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Principles extracted** | depth | At least one principle is stated — something learned beyond this specific hypothesis that generalizes to future investigations. Principles are declarative ("X implies Y") not restatements of the finding. |
| C-07 | **Open questions identified** | coverage | At least one question the investigation did not resolve is named. Questions are specific and actionable, not generic ("more research needed"). |
| C-08 | **Confidence is explained** | depth | The confidence score is accompanied by a brief rationale (1–3 sentences) explaining what drove it up or down. Score alone without rationale is a partial pass (counts as fail for this criterion). |

---

## Aspirational Criteria (weight: 57.5 points total — 2.5 pts each, 23 criteria)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Evidence hierarchy is argued** | depth | The output explains *why* the top signals outweighed the others — not just what they are. A comparative question is present for each rank: "why this signal over the one below it?" A ranked argument is present, not a ranked list. |
| C-10 | **Synthesis is self-contained** | behavior | A reader with no access to the underlying investigation signals can understand the answer, the reasoning, and what to do next from the synthesis alone. No unexplained references to prior artifacts. The standalone mandate is stated explicitly in the opening, not assumed to emerge from structure. |
| C-11 | **Anti-pattern gates** | structure | Named anti-pattern gates are present in the skill instruction that foreclose specific failure modes by name. Each gate names the failure mode (e.g., confirmation bias, hedging, generic challenge) and the phase or role where it applies. NOT: anti-patterns implied by role name without explicit prohibition. NOT: single instruction to "avoid bias" without naming the failure mode. |
| C-12 | **Argumentative sections prose** | format | The KEY EVIDENCE section uses prose or numbered argument slots — not tables or bullet lists. Each evidence slot requires argument construction (why this signal influenced the answer) at minimum one sentence. Table cells are not sufficient for argument construction. NOT: KEY EVIDENCE formatted as a table. NOT: evidence slots that can be filled with a single word or phrase. |
| C-13 | **NOT:-first ordering** | structure | At least one instruction in the skill opens with NOT: before any success condition for that instruction is stated — the failure mode is named before the target behavior. "NOT: [failure mode]. [success condition]" ordering appears at least once. NOT: prohibitions present but placed after the success condition. NOT: "avoid X" phrasing without NOT: prefix before the success condition. |
| C-14 | **Formal verdict register** | format | The output commitment is introduced by a formal register word (ANSWER, VERDICT, DETERMINATION, or equivalent) used as a section label or sentence-opening label at the boundary where commitment is issued. NOT: commitment sentence begins with "I think," "The evidence suggests," or similar hedging preamble. NOT: verdict present but register word absent or in lowercase. |
| C-15 | **Pre-committed counter-evidence** | structure | The adversarial challenge (counter-evidence identification) is structurally required to occur before the synthesis output is written. The adversarial phase or role precedes the judgment phase in the instruction sequence. NOT: adversarial challenge optional or post-hoc. NOT: counter-evidence section in the output with no corresponding instruction to generate it before the answer. |
| C-16 | **Role-labeled cognitive phases** | structure | Each cognitive phase is labeled by name AND includes an identity-level foreclosure statement that prohibits the phase from performing the function of another phase (e.g., "ADVERSARY cannot advocate for the answer," "SYNTHESIST cannot introduce new evidence"). The foreclosure is stated at role definition, not as a process step. NOT: roles/phases named without identity-level prohibition. NOT: prohibitions phrased as process steps rather than identity constraints. |
| C-17 | **Record-specific anti-pattern** | depth | The adversarial challenge instruction asks the adversary to identify a failure mode specific to the current evidence pattern — not a generic challenge applicable to any synthesis. The instruction specifies what structural properties to examine. A worked example of a structural failure mode is provided (e.g., "all three top signals come from the same source type"). NOT: adversarial challenge that applies identically to any synthesis regardless of evidence composition. NOT: "challenge the answer" without specifying structural properties to examine. |
| C-18 | **Register word opens commitment** | format | The register word (ANSWER, VERDICT, or equivalent) appears as the opening word of the commitment sentence in the output template — the first word of the sentence itself, not as a section header above a sentence that begins with a different word. NOT: register word as a section header where the commitment sentence begins with a different word. NOT: register word present but mid-sentence or after a preamble. |
| C-19 | **Frontmatter commitment declarations** | structure | A FRONTMATTER block exists with boolean (TRUE/FALSE or COMPLETE/INCOMPLETE) fields — not prose fill-instructions. Each field represents a commitment that must be set at a specific structural moment, not retroactively. The block is named FRONTMATTER or equivalent. NOT: no frontmatter block. NOT: frontmatter fields are fill-instructions rather than boolean completion states. |
| C-20 | **Phase-sequenced frontmatter** | structure | Each frontmatter field is assigned to the specific structural phase at which it becomes fillable — the fill instruction names the phase. Fields are not batch-fillable at document open or close; each field's phase assignment is explicit. NOT: frontmatter fields present without phase assignment. NOT: instruction to fill all fields at document open or close without per-field phase assignment. |
| C-21 | **SURVEYOR-traceable diagnosis** | depth | A named SURVEYOR phase (or equivalent inventory phase) precedes the adversarial phase and establishes the signal inventory. The adversarial failure mode is derived from and cross-referenceable to entries in the SURVEYOR inventory — the diagnostic challenge names specific signals or signal IDs from the inventory. NOT: adversarial challenge derived without reference to a prior named inventory. NOT: challenge plausibly structural but not cross-referenceable to a named inventory entry. |
| C-22 | **Dual-layer register-word enforcement** | structure | Register-word enforcement operates at two levels: (1) output level — the register word appears as the commitment sentence opener (C-18), AND (2) instruction level — an explicit NOT: gate at the instruction level prohibits completing the synthesis without the register word in the opening position, naming the failure mode. NOT: register word present at output level without a corresponding instruction-level NOT: gate. NOT: instruction directs use of register word but lacks a NOT: prohibition. |
| C-23 | **Named violation categories** | structure | Each fill-window bound for frontmatter fields is expressed as a named violation category (PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION VIOLATION, or equivalent) — not merely "NOT: fill before X." The violation name creates an addressable failure type a writer can cite. NOT: fill-window bounds expressed only as "not before"/"not after" instructions without named violation labels. NOT: violation names present at one bound only. |
| C-24 | **Arrow-chain RECORD DIAGNOSIS** | structure | The adversarial challenge (RECORD DIAGNOSIS or equivalent) is expressed using arrow-chain field:value notation — at minimum `signal_id:value → property:value → basis:value` — where each arrow represents a structural derivation step producing a one-lookup falsifiability guarantee. NOT: adversarial challenge in prose only without field:value syntax. NOT: field:value notation present but arrows absent (a list of fields is not a chain). |
| C-25 | **PRE-FLIGHT audit block** | structure | A named structural phase called PRE-FLIGHT (or equivalent) exists as a sequenced block between the adversarial phase and the judgment phase. The PRE-FLIGHT block is encountered before the commitment sentence can be written. NOT: dual-layer register-word enforcement present without a named PRE-FLIGHT phase. NOT: PRE-FLIGHT equivalent embedded within JUDGMENT rather than positioned before it. |
| C-26 | **Violation taxonomy registry at document open** | structure | All violation types (PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION VIOLATION, FALSE ATTESTATION VIOLATION, PHASE-ADVANCE VIOLATION, and any equivalents) are indexed in a named registry block **before FRONTMATTER** — the taxonomy is visible before any fill window is encountered. NOT: violation names appear only inline at each bound without a preceding registry. NOT: registry appears after FRONTMATTER. |
| C-27 | **Arrow-chain three-site chain of custody** | structure | Arrow-chain field:value notation is traceable at all three named sites: **creation** in RECORD DIAGNOSIS, **audit** in PRE-FLIGHT Phase B (SCHEMA-CITATION AUDIT), **application** in JUDGE confidence paragraph. Two-site presence does not satisfy. NOT: arrow-chain in RECORD DIAGNOSIS only. NOT: PRE-FLIGHT audits but JUDGE does not apply. NOT: JUDGE applies without PRE-FLIGHT having explicitly verified. |
| C-28 | **PRE-FLIGHT anti-skip gate** | structure | A named gate at **PRE-FLIGHT's entry** names PHASE-ADVANCE VIOLATION (or equivalent) before any PRE-FLIGHT phase step is listed — the bypass failure mode is encountered before the steps can be skipped. NOT: PRE-FLIGHT begins with phase steps without a preceding entry gate. NOT: bypass failure mode named only at end of PRE-FLIGHT or at JUDGE boundary (post-hoc). |
| C-29 | **Per-rank comparative slot** | structure | Each rank position in the evidence section has a structurally required comparative assignment — a named column, labeled subsection, or enumerated sub-item that asks "why this rank, not the one below" for that position specifically. The slot appears at every rank; its absence at any rank is a visible structural gap. NOT: comparative language present only as prose commentary after the full ranking. NOT: single comparative note covering all rank positions without per-rank assignment. |
| C-30 | **Role-native failure mode ownership** | structure | Each cognitive role (or phase) explicitly names the failure mode characteristic of its own phase — the failure it is at risk of exhibiting — at role definition or role instruction. ANALYST/SURVEYOR names its collection-phase bias; SKEPTIC/ADVERSARY names its adversarial-phase failure (e.g., generic challenge instead of structural challenge); SYNTHESIST/JUDGMENT names its judgment-phase failure (e.g., hedging, summarizing). NOT: anti-patterns listed centrally without assignment to the role that exhibits them. NOT: role definitions describe duties only; anti-pattern gates appear only at output level. |
| C-31 | **Pattern-of-N adversarial input** | depth | The adversarial challenge is derived from the aggregate pattern of multiple top signals, not a single signal in isolation. The record-specific failure mode names a distribution property (e.g., "N of the top M signals share the same source type," "the top K signals all converge without cross-type confirmation") visible only by examining the signal inventory as a whole. The count or range is stated. NOT: adversarial challenge targeting one signal's properties only. NOT: aggregate pattern claimed but signal count not stated or not cross-referenced to the inventory. |
```
