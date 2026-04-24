Written to `simulations/quest/golden/topic-echo-variate-R5-2026-03-16b.md`.

---

# Variations: `topic:echo` — Round 5

**Rubric:** v5 | **Date:** 2026-03-16

---

## Design Context

R4 V-05 scored 140/140 under v5 — first variation to pass all ten aspirational criteria. Two new criteria drove the jump:

- **C-17**: Enforcement mechanism strength classification — requires tier label (`structural > temporal`) + distinguishing property (role-scope exclusion vs. phase sequencing) + reviewer implication ("independence is enforced, not instructed"). R4 V-05 passed by embedding all three in PBI section prose.
- **C-18**: Per-entry attestation with evidentiary quotation — requires quoting actual PBI entry belief text and source finding sentence inline, not just identifiers. R4 V-05 passed by quoting substantive text in each Verified field.

**R5 structural questions remaining after R4:**

1. **C-17 navigability**: R4 V-05 declared the enforcement mechanism inside PBI prose. A dedicated headed section would let reviewers navigate to tier + property + implication without reading the full artifact. Does dedicated-section placement surface a new excellence signal (C-19 candidate)?

2. **C-18 self-evaluation**: R4 V-05 required "substantive" quotation — a reviewer judgment. Named pass/fail quality tests at production time would make C-18 self-certifying. Does this surface a new signal?

3. **Chain integrity post-production**: R4 V-05 enforces the chain [PBI-Ref → Handle → Source → Verified quotation] per-entry at production time but does not run a post-production audit with visible per-entry tokens. Three-layer enforcement (definition → attestation → audit) may surface a new criterion.

**R5 variation axes:**

| Variation | Axis | New mechanism | C-09 | C-10 | Predicted |
|-----------|------|---------------|------|------|-----------|
| V-01 | Lifecycle | Dedicated C-17 section | — | — | 130 |
| V-02 | Output format | Self-certifying C-18 quotation quality | — | — | 125 |
| V-03 | Lifecycle | Post-production chain integrity audit | + | + | 140 |
| V-04 | Lifecycle + format | V-01 + V-02 combined | — | — | 130 |
| V-05 | All | V-01 + V-02 + V-03 + Archaeologist + Rules | + | + | 140 |

V-02 intentionally omits the dedicated C-17 section (relies on inline declaration) to isolate whether C-17 navigability is an independent excellence signal from C-18 quotation quality.

---

## V-01 — Dedicated Enforcement Mechanism Section

**Variation axis:** Lifecycle emphasis — the enforcement mechanism classification is a standalone headed section (`## Provenance Enforcement Mechanism`) appearing immediately after the PBI and before the Handle Ledger. Contains a four-row structured table: mechanism type, tier, distinguishing property, reviewer implication. Builds on R4 V-01 chain (PBI + Handle Ledger + Typed Gate + "We believed:" field). Targets C-17 at full pass with dedicated-section placement.

**Hypothesis:** R4 V-01/V-05 embedded enforcement declaration in PBI section prose. A reviewer auditing C-17 must locate tier, property, and implication within text. C-17's practical requirement ("a reviewer unfamiliar with the hierarchy must immediately calibrate without re-deriving") is better served by a section navigable by heading. This may surface C-19 candidate: mechanism declaration is in a headed section independently locatable without full-artifact reading.

**Expected scores:** C-17 PASS, C-18 PASS (Verified field has three-pointer quotations), C-09 FAIL, C-10 FAIL → **130/140**

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not expect? It is institutional memory for the next team that walks this path. Each entry is a named surprise — sourced, contrasted with a named falsifiable prior belief, and assessed for specific design impact.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials for `{topic}` have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted an assumption.
*Test:* "Is this finding here because it overturned an assumption, or because it happened and seemed notable?" If the latter → cut.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft, review, flow, trace, prove, listen, program, topic). Note what each artifact was investigating. Internal scaffolding — do not include in output.

---

**Step 2 — Prior Belief Inventory.**

*Write this section before consulting any signal artifact content. You are in the belief-writing role: access only the original design materials for `{topic}` (spec, proposal, draft, stated assumptions). This is structural provenance isolation: role-scope exclusion prevents access to signal artifacts regardless of instruction.*

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X — a testable predicate that investigation could have confirmed} |
| PBI-02 | |
| PBI-03 | |

*Each belief must be falsifiable: "We believed X" where X is a proposition that could have been right. "We hadn't thought about X" is not a prior belief. Minimum 3 entries.*

**[COMMIT-PBI: Written in the belief-writing role, before signal artifacts were read.]**

---

**Step 3 — Enforcement Mechanism Declaration.**

*Write immediately after committing the PBI. This section classifies the provenance isolation mechanism. Appears as a headed section in the artifact so reviewers can navigate to it by heading without reading the full artifact.*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| **Mechanism type** | Structural provenance |
| **Tier** | Structural > temporal |
| **Distinguishing property** | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts regardless of instruction. Temporal provenance is enforced by phase sequencing — phases are ordered, but the same agent can reason across phases. Role-scope exclusion is stronger because it closes the cross-phase reasoning path that phase gates leave open. |
| **Reviewer implication** | Independence is enforced, not instructed. C-13 content analysis (PBI entries use belief language; Handle Ledger labels use finding language) is confirmatory rather than probative: the mechanism already ensures independence; content analysis confirms it holds. A reviewer unfamiliar with the hierarchy can calibrate from this section alone. |

*This table must appear as a headed section in the artifact. A reviewer auditing C-17 can navigate here and find tier, property, and reviewer implication without reading surrounding content.*

---

**Step 4 — Handle Ledger.**

*Write after reading signal artifacts. Do not consult the PBI section while writing Handle labels. Handle labels use finding language — what signals revealed — not belief language from the PBI.*

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check: does any Handle label echo PBI entry language verbatim? If yes, revise to use language specific to what signals showed.*

**[COMMIT-HANDLE-LEDGER]**

---

**Step 5 — Adversarial Gate.**

You are the **Gatekeeper**. For each candidate finding, apply the Anti-Pattern Catalog and issue a verdict:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: {Complete: "We believed {X}" — testable proposition.
  VALID: "We believed the migration endpoint was stateless between sessions."
  INVALID: "We hadn't considered reconnect behavior." (absence of consideration)
  INVALID: "This surprised the team." (reaction, not a proposition)
  INVALID: "We were uncertain about this area." (uncertainty is not a falsifiable belief)
  A SURPRISE verdict with an invalid "We believed:" is structurally incomplete.}
PBI-Ref: {PBI-NN — the entry this contradicts — required for SURPRISE verdicts}
H-Ref: {H-NN}
```

Valid verdicts: `SURPRISE`, `CUT — finding-as-surprise substitution`, `CUT — summary-in-disguise`, `CUT — orphan-attribution`. Bare `CUT` invalid. Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 6 — Write echo entries.**

For each SURPRISE candidate (minimum 2):

**[Surprise Name]**
*2-5 words, title case. Matches a Handle Ledger entry. Citable by a future team without reading this echo.*

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}` — specific artifact or skill type. Passes orphan-attribution test.
- **We believed**: The falsifiable prior belief from the Gatekeeper's verdict. One full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision this changes or constrains. One sentence. Must name something specific.
- **Verified**:
  - Handle confirmed: H-NN — "{quote the Handle Ledger label text for H-NN}"
  - PBI-Ref confirmed: PBI-NN — "{quote the full belief statement from PBI-NN, including the predicate — what the team staked on}"
  - Source confirmed: `{skill-type}` — "{quote the specific sentence from the source artifact that documents this finding — must name a component, behavior, or condition}"

---

**Step 7 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences: do 2+ share a root cause, reveal the same blind spot, or together indicate a design direction not previously visible? Name any pattern explicitly; state its absence if none is evident.

---

**Step 8 — Forward guidance.**

Write 1-3 sentences for the next team building `{topic}`. Register: "If you are about to build X, know that Y because we found Z." Specific to these surprises.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order: (1) Provenance Enforcement Mechanism table (Step 3, headed), (2) PBI table (Step 2), (3) Handle Ledger (Step 4), (4) individual entries (Step 6), (5) synthesis (Step 7), (6) forward guidance (Step 8). Steps 1, 5 are execution scaffolding.

---

## V-02 — Quotation Quality Template

**Variation axis:** Output format — the Verified field uses explicit named pass/fail quality tests for each quotation, stated at production time and applied before the field is committed. The enforcement mechanism declaration appears inline in the PBI preamble (no dedicated section). Builds on R4 V-02 structure (Pre-Write Prediction Sort with typed Route: labels). Targets C-18 at the highest self-evaluating pass level.

**Hypothesis:** R4 V-05 required "substantive" quotation — quality was a reviewer judgment after the fact. Named pass/fail criteria (predicate test, uniqueness test, length test, specificity test, locatability test) at production time make C-18 self-certifying: the author confirms each quotation passes before committing. Two effects: (1) borderline quotations that would pass casual review but don't confirm the citation become structurally unproducible; (2) the author's quality evaluation is visible in the output. Intentionally omits dedicated C-17 section to isolate whether C-18 self-certification is an independent excellence signal from C-17 navigability. Expected to fail C-17 per rubric (no tier label in dedicated section) and fail C-09/C-10.

**Expected scores:** C-17 N/A or FAIL (no tier), C-18 PASS (self-certifying quality tests), C-09 FAIL, C-10 FAIL → **125/140**

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect? Each entry is a named surprise — sourced, contrasted with a prior expectation, and assessed for specific design impact. Its audience is the next team that walks this path.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings for coverage, not because they contradicted an assumption.
*Test:* "Could this output be described as a summary of what the investigation found?" Yes → you have at least one of these.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces. Note what each was investigating. Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

This step runs before any candidates enter the gate pipeline. Every finding is assigned a typed destination — no finding is discarded without a named home.

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — required}
```

> "Before this investigation began — reading only the original design materials for `{topic}` — would we have predicted this finding?"

Valid routes:
- `topic-story` — YES: confirms what the design already assumed
- `topic-report` — YES (process/method finding): about how the investigation ran, not what `{topic}` does
- `gate-pipeline` — NO: proceeds to the adversarial gate

**Invalid routes — do not use:** "excluded from echo," blank, "not included." Every finding requires a named typed route. Collect at least 3 `gate-pipeline` findings before proceeding. Sort log is execution scaffolding.

---

**Step 3 — Prior Belief Inventory.**

*Write before returning to signal artifact content. Access only original design materials. Structural provenance isolation applies: the belief-writing role accesses only design materials, not signal artifacts (role-scope exclusion, stronger than phase-gate temporal provenance).*

| PBI-Ref | Prior Belief |
|---------|--------------|
| PBI-01 | We believed {falsifiable proposition} |
| PBI-02 | |
| PBI-03 | |

**[COMMIT-PBI]**

---

**Step 4 — Handle Ledger.**

*Written after reading signals. Handle labels use finding language.*

| Handle # | Handle Label (finding language, 2-5 words) | Source skill |
|----------|-------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

**[COMMIT-HANDLE-LEDGER]**

---

**Step 5 — Adversarial Gate.**

You are the **Gatekeeper**. Apply the Anti-Pattern Catalog to each `gate-pipeline` candidate:

```
Candidate: {description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: "We believed {X}" — testable proposition.
PBI-Ref: PBI-NN
H-Ref: H-NN
```

Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 6 — Write echo entries.**

For each SURPRISE candidate (minimum 2):

**[Surprise Name]**
*2-5 words, title case, matches a Handle entry, citable without reading this echo.*

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}`
- **We believed**: Falsifiable prior belief. One full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision. One sentence. Names something specific.
- **Verified** — apply these named quality tests before committing each quotation:

  *PBI quotation quality tests — all must pass before committing:*
  - **Predicate test**: Does the quoted text contain the full predicate of the belief — what the team specifically staked on? A topic word alone ("session tokens") fails; a belief sentence with predicate ("session tokens were preserved across reconnects") passes.
  - **Uniqueness test**: Would the quoted text distinguish PBI-NN from any other PBI entry in the table? If the same text could apply to another PBI entry, it fails.
  - **Length test**: Is the quotation 8+ words?

  *Finding quotation quality tests — all must pass before committing:*
  - **Specificity test**: Does the quoted text name a specific component, behavior, or condition? A general observation ("this was more complex than expected") fails; a specific finding ("the scheduler dispatches before deduplication at the ingestion boundary") passes.
  - **Locatability test**: Is the quoted text locatable in the source artifact? A reader navigating to `{skill-type}` would find this sentence.
  - **Length test**: Is the quotation 8+ words?

  PBI-Ref confirmed: PBI-NN — "{quoted PBI belief statement — passes all three PBI quality tests; confirm before committing}"
  Handle confirmed: H-NN — "{quoted Handle Ledger label text}"
  Source confirmed: `{skill-type}` — "{quoted source finding sentence — passes all three finding quality tests; confirm before committing}"

---

**Step 7 — Synthesize.**

Do the surprises cluster? 2-4 sentences. Do 2+ share a root cause, reveal the same blind spot, or together indicate a design direction not previously visible? Name any pattern; state its absence.

---

**Step 8 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Register: "If you are about to build X, know that Y."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections: PBI table (Step 3), Handle Ledger (Step 4), individual entries (Step 6), synthesis (Step 7), forward guidance (Step 8). Steps 1, 2, 5 are execution scaffolding.

---

## V-03 — Post-Production Chain Integrity Audit

**Variation axis:** Lifecycle emphasis — after all surprise entries are written, a Chain Integrity Audit step runs per entry, producing visible `CHAIN-COMPLETE-{N}` or `CHAIN-FLAG-{N}` tokens in the artifact. Includes full C-17 dedicated section, C-18 quotation quality template, impact ranking (C-09), and riskiest surprise flag (C-10). Targets potential v6 excellence signal.

**Hypothesis:** R4 V-05 enforced the chain [PBI-Ref → Handle → Source → Verified quotation] per entry at production time. It did not run a post-production audit confirming all four chain elements are internally consistent. A post-production audit adds a third enforcement layer: definition (field vocabulary prevents bad content) → attestation (Verified field confirms checks were performed at production time) → audit (chain integrity audit confirms attestations are correct post-production). Three-layer enforcement may surface C-19 candidate: the audit produces visible per-entry tokens in the artifact, making chain integrity auditable from the output alone.

**Expected scores:** All criteria pass including C-09, C-10, C-17, C-18 → **140/140**; potential v6 signal

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not expect? Each entry is a named surprise — sourced, contrasted with a falsifiable prior belief, ranked by design impact, and assessed for specific consequence. Its audience is the next team that walks this path.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings for coverage, not because they contradicted an assumption.
*Test:* "Is this here because it overturned an assumption, or because it happened?" Latter → cut.

**orphan-attribution** — a surprise with no traceable source artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.** Internal scaffolding.

---

**Step 2 — Prior Belief Inventory + Enforcement Mechanism Declaration.**

*Written before consulting signal artifact content. Structural provenance isolation applies.*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| **Mechanism type** | Structural provenance |
| **Tier** | Structural > temporal |
| **Distinguishing property** | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts, regardless of instruction. Temporal provenance is enforced by phase sequencing, which orders phases but does not block cross-phase reasoning by the same agent. Role-scope exclusion closes the cross-phase reasoning path. |
| **Reviewer implication** | Independence is enforced, not instructed. C-13 content analysis is confirmatory rather than probative. A reviewer unfamiliar with the hierarchy can calibrate the independence claim from this section alone. |

## Prior Belief Inventory

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X — testable predicate} |
| PBI-02 | |
| PBI-03 | |

**[COMMIT-PBI: Written in belief-writing role. Structural provenance confirmed per Enforcement Mechanism Declaration.]**

---

**Step 3 — Handle Ledger.**

*Written after reading signals. Finding language only — not belief language from PBI.*

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check: no Handle label echoes PBI language verbatim.*

**[COMMIT-HANDLE-LEDGER]**

---

**Step 4 — Adversarial Gate.**

You are the **Gatekeeper**. Apply the Anti-Pattern Catalog to each candidate:

```
Candidate: {description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: "We believed {X}" — testable proposition.
  VALID: "We believed the compliance check ran at write time, not read time."
  INVALID: "We hadn't considered this." (absence of consideration)
  INVALID: "This surprised the team." (reaction)
  A SURPRISE without a valid "We believed:" is structurally incomplete.
PBI-Ref: PBI-NN
H-Ref: H-NN
```

Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 5 — Impact triage (pre-write).**

Assign each SURPRISE candidate a tier before writing any entry:
- **HIGH**: Forces a design decision to change or invalidates a major assumption.
- **MEDIUM**: Requires adjustment to a specific component or flow.
- **LOW**: Informative; does not change design trajectory.

Order: HIGH → MEDIUM → LOW. Ties broken by specificity. Triage list is scaffolding.

---

**Step 6 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
*2-5 words, title case. Matches a Handle Ledger entry.*

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}` — specific artifact or skill type.
- **We believed**: Falsifiable prior belief. One full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision. One sentence. Names something specific.
- **Verified** — apply quality tests before committing:

  *PBI quality tests (all must pass):*
  - Predicate test: quoted text contains the full predicate of the belief (what the team staked on)
  - Uniqueness test: quoted text distinguishes PBI-NN from any other PBI entry
  - Length test: 8+ words

  *Finding quality tests (all must pass):*
  - Specificity test: quoted text names a specific component, behavior, or condition
  - Locatability test: text is locatable in the source artifact
  - Length test: 8+ words

  Handle confirmed: H-NN — "{Handle Ledger label text}"
  PBI-Ref confirmed: PBI-NN — "{quoted belief statement — passes all PBI quality tests}"
  Source confirmed: `{skill-type}` — "{quoted finding sentence — passes all finding quality tests}"

---

**Step 7 — Chain Integrity Audit.**

*Run after all entries are written. The audit confirms end-to-end chain consistency. Results appear in the artifact as visible tokens immediately after each entry.*

For each entry:

```
Entry: {Surprise Name}
Check A — Handle language: Is H-NN's label finding language, not belief language from PBI?
  Result: PASS | FAIL — {discrepancy if fail}
Check B — Tier consistency: Does the tier header match the Step 5 triage assignment?
  Result: PASS | FAIL
Check C — PBI quotation fidelity: Does the quoted PBI text appear verbatim in PBI-NN and pass all three PBI quality tests?
  Result: PASS | FAIL — {discrepancy if fail}
Check D — Finding quotation fidelity: Is the quoted source finding text locatable in the source artifact and does it pass all three finding quality tests?
  Result: PASS | FAIL — {discrepancy if fail}
CHAIN-COMPLETE-{N}: {Surprise Name} | CHAIN-FLAG-{N}: {checks failed — revise entry before proceeding}
```

On `CHAIN-FLAG`: revise the entry, re-commit, re-run the audit for that entry. Proceed only when all entries produce `CHAIN-COMPLETE`. Audit tokens appear in the artifact (not scaffolding).

---

**Step 8 — Synthesis.**

Do the surprises cluster? 2-4 sentences: do 2+ share a root cause, reveal the same blind spot, or together indicate a design direction not previously visible? Name any pattern; state its absence explicitly.

---

**Step 9 — Riskiest assumption.**

Flag the single surprise most likely to invalidate a core assumption. State: (a) the assumption at risk, (b) the signal that revealed it, (c) what would need to be true for the assumption to hold despite the surprise. One labeled paragraph.

---

**Step 10 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Register: "If you are about to build X, know that Y because we found Z."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order: (1) Provenance Enforcement Mechanism table, (2) PBI table, (3) Handle Ledger, (4) surprise entries with `CHAIN-COMPLETE` tokens, (5) synthesis, (6) riskiest assumption, (7) forward guidance. Steps 1, 4, 5 are execution scaffolding.

---

## V-04 — Combination: Dedicated C-17 Section + Quotation Quality Template

**Variation axis:** Lifecycle emphasis + output format — V-01's dedicated Enforcement Mechanism Declaration section combined with V-02's named quotation quality tests. Full chain (PBI + Handle Ledger + Typed Gate). Omits impact ranking and riskiest flag to isolate the V-01 + V-02 combination effect.

**Hypothesis:** V-01 tests dedicated-section C-17; V-02 tests self-certifying C-18. Combined, they create a two-layer audit architecture: section-level provenance calibration (C-17 navigable by heading) and entry-level evidence certification (C-18 quality tests confirmed at production time). If either alone reaches 130, the combination confirms both work together and still reaches 130 (ceiling unchanged without C-09/C-10). The structural interaction question: does having both in the same artifact produce a new signal — the mechanism declaration and per-entry quotation quality are mutually reinforcing, making independence auditable at section level AND evidence auditable at entry level simultaneously?

**Expected scores:** C-17 PASS (dedicated section), C-18 PASS (self-certifying quality), C-09 FAIL, C-10 FAIL → **130/140**

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not expect? Each entry is a named surprise — sourced, contrasted with a named falsifiable prior belief, and assessed for design impact. Its audience is the next team that walks this path.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings for coverage, not because they contradicted an assumption.
*Test:* "Is this here because it overturned an assumption, or because it happened?" Latter → cut.

**orphan-attribution** — a surprise with no traceable source artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.** Internal scaffolding.

---

**Step 2 — Prior Belief Inventory.**

*Written before consulting signal artifact content. Structural provenance isolation applies.*

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X} |
| PBI-02 | |
| PBI-03 | |

**[COMMIT-PBI: Written in belief-writing role before signal artifacts were read.]**

---

**Step 3 — Enforcement Mechanism Declaration.**

*Written immediately after COMMIT-PBI. Headed section in the artifact.*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| **Mechanism type** | Structural provenance |
| **Tier** | Structural > temporal |
| **Distinguishing property** | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts regardless of instruction. Temporal provenance is enforced by phase sequencing — phases are ordered but the same agent can reason across phases. Role-scope exclusion closes the cross-phase reasoning path that phase gates leave open. |
| **Reviewer implication** | Independence is enforced, not instructed. C-13 content analysis (belief language in PBI vs. finding language in Handle labels) is confirmatory rather than probative. A reviewer auditing C-17 can find tier, property, and implication here without reading surrounding content. |

---

**Step 4 — Handle Ledger.**

*Written after reading signals. Finding language only.*

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check: no Handle label echoes PBI language verbatim.*

**[COMMIT-HANDLE-LEDGER]**

---

**Step 5 — Adversarial Gate.**

You are the **Gatekeeper**. For each candidate:

```
Candidate: {description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: "We believed {X}" — testable proposition.
PBI-Ref: PBI-NN
H-Ref: H-NN
```

Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 6 — Write echo entries.**

For each SURPRISE candidate (minimum 2):

**[Surprise Name]**
*2-5 words, title case, matches a Handle entry.*

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}`
- **We believed**: Falsifiable prior belief. One full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision. One sentence.
- **Verified** — apply named quality tests before committing each quotation:

  *PBI quality tests (all must pass):*
  - **Predicate test**: Quoted text contains the full predicate — what the team staked on.
  - **Uniqueness test**: Quoted text distinguishes PBI-NN from any other PBI entry.
  - **Length test**: 8+ words.

  *Finding quality tests (all must pass):*
  - **Specificity test**: Quoted text names a specific component, behavior, or condition.
  - **Locatability test**: Text is locatable in the source artifact.
  - **Length test**: 8+ words.

  Handle confirmed: H-NN — "{Handle Ledger label text}"
  PBI-Ref confirmed: PBI-NN — "{quoted belief statement — passes all PBI quality tests}"
  Source confirmed: `{skill-type}` — "{quoted finding sentence — passes all finding quality tests}"

---

**Step 7 — Synthesize.**

2-4 sentences: do 2+ surprises share a root cause, reveal the same blind spot, or indicate a design direction not previously visible? Name any pattern; state its absence.

---

**Step 8 — Forward guidance.**

1-3 sentences for the next team. Register: "If you are about to build X, know that Y."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections: (1) Provenance Enforcement Mechanism table (Step 3, headed), (2) PBI table (Step 2), (3) Handle Ledger (Step 4), (4) entries (Step 6), (5) synthesis (Step 7), (6) forward guidance (Step 8). Steps 1, 5 are execution scaffolding.

---

## V-05 — Full Combination: All Criteria + All R5 Structural Innovations

**Variation axis:** All axes — V-01's dedicated C-17 section, V-02's self-certifying quotation quality template, V-03's post-production Chain Integrity Audit, Institutional Archaeologist role threading (frames entries as corrections for future teams), impact ranking with argued rationale (C-09), riskiest surprise flag (C-10), and impact-anchored Rules of Thumb. All ten aspirational criteria at structurally distinct moments.

**Hypothesis:** V-03 achieves 140/140 via a single structural path. V-05 combines all R5 innovations to test whether three-layer enforcement (definition → production-time attestation → post-production audit) plus the Institutional Archaeologist role creates a four-layer confirmation architecture: (1) field vocabulary prevents bad content at design time, (2) role-scope exclusion enforces independence at production time, (3) per-entry Verified fields attest checks were performed, (4) Chain Integrity Audit confirms attestations are correct. If all four layers are visible in the output, a reviewer has four independent confirmation mechanisms for the artifact's trustworthiness. This may surface C-19: the artifact's trustworthiness is multi-layer-confirmed — each layer is independently auditable and all four layers are visible in the output without navigation between sections.

**Expected scores:** All 18 criteria pass → **140/140**; potential v6 excellence signal

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**Your operating role: Institutional Archaeologist.**

An Institutional Archaeologist recovers false assumptions from a body of work — specifically the ones the current design materials still carry, that a new team would inherit and act on incorrectly without this artifact. You hold this identity throughout. Where a step or field is prefixed with **(Institutional Archaeologist:)**, your answer must come from that perspective: what would the next team get wrong?

The Institutional Archaeologist is distinct from the Gatekeeper role in Step 4. The Gatekeeper tests whether a finding qualifies as a surprise. The Institutional Archaeologist frames what that surprise means for a reader who was not present.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials for `{topic}` have predicted this?" Yes → cut.

**summary-in-disguise** — findings for coverage, not because they contradicted an assumption.
*Test:* "Could this output be described as a summary of what the investigation found?" Yes → you have at least one of these.

**orphan-attribution** — a surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft, review, flow, trace, prove, listen, program, topic). Note what each was investigating. Internal scaffolding.

---

**Step 2 — Prior Belief Inventory + Enforcement Mechanism Declaration.**

*Written before consulting signal artifact content. You are in the belief-writing role: access only original design materials. This is structural provenance isolation (role-scope exclusion).*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| **Mechanism type** | Structural provenance |
| **Tier** | Structural > temporal |
| **Distinguishing property** | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts regardless of instruction. Temporal provenance is enforced by phase sequencing — the same agent can still reason across phases even when reading order is controlled. Role-scope exclusion closes the cross-phase reasoning path that phase gates leave open. |
| **Reviewer implication** | Independence is enforced, not instructed. C-13 content analysis (PBI entries use belief language; Handle labels use finding language) is confirmatory rather than probative: the mechanism already ensures independence; content analysis confirms it holds. A reviewer unfamiliar with the hierarchy can calibrate the independence claim from this section alone without re-deriving it from content analysis. |

*This section is headed so reviewers can navigate directly to the mechanism classification without reading the full artifact.*

## Prior Belief Inventory

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X — testable predicate that investigation could have confirmed} |
| PBI-02 | |
| PBI-03 | |

*Each belief must be falsifiable. "We hadn't considered X" is an absence, not a prior belief. Minimum 3 entries.*

**[COMMIT-PBI: Written in the belief-writing role before signal artifacts were read. Structural provenance isolation confirmed per Enforcement Mechanism Declaration above.]**

---

**Step 3 — Handle Ledger.**

*Written after reading signals. Do not consult PBI while writing Handle labels. Finding language only — what signals revealed.*

**(Institutional Archaeologist:)** Encode what the current materials still carry wrong. Labels should name the correction the next team needs, not the discovery the original team made.

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check: does any Handle label echo PBI language verbatim? Revise if yes.*

**[COMMIT-HANDLE-LEDGER]**

---

**Step 4 — Adversarial Gate.**

You are the **Gatekeeper** (not the Institutional Archaeologist — the Gatekeeper's function is adversarial rejection, not future-reader framing). Apply the Anti-Pattern Catalog to each candidate:

```
Candidate: {description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: "We believed {X}" — testable proposition.
  VALID: "We believed the scheduler deduplicated events before dispatching callbacks."
  VALID: "We believed the compliance check ran at write time, not read time."
  INVALID: "We hadn't considered this edge case." (absence)
  INVALID: "This was surprising to the team." (reaction)
  INVALID: "We were uncertain about this area." (uncertainty is not a falsifiable belief)
  A SURPRISE without a valid "We believed:" is structurally incomplete.
PBI-Ref: PBI-NN
H-Ref: H-NN
```

Valid verdicts: `SURPRISE`, `CUT — finding-as-surprise substitution`, `CUT — summary-in-disguise`, `CUT — orphan-attribution`. Bare `CUT` invalid. Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 5 — Impact triage (pre-write).**

Before writing any entry, assign each SURPRISE candidate a tier:

- **HIGH**: Forces a design decision to change or invalidates a major assumption.
- **MEDIUM**: Requires adjustment to a specific component or flow.
- **LOW**: Informative; does not change design trajectory.

Order: HIGH → MEDIUM → LOW. Ties broken by specificity. Triage list is scaffolding.

---

**Step 6 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
**(Institutional Archaeologist:)** Encode the correction the next team needs, not the discovery the original team made. A name passes if a future reader can cite it without having been present.

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}` — specific artifact or skill type. Passes orphan-attribution test.
- **We believed**: The falsifiable prior belief from the Gatekeeper's verdict. One full sentence.
- **The correction**: What the signal showed instead. Directly contradicts "We believed." One sentence.
- **What the next team would get wrong**: **(Institutional Archaeologist:)** The specific decision, component, or flow the next team would mis-design if they carried the false assumption. Name the concrete mis-design — not "this would cause problems." One sentence.
- **Verified** — apply named quality tests before committing each quotation:

  *PBI quality tests — all must pass:*
  - **Predicate test**: Quoted text contains the full predicate of the belief (what the team staked on, not just the topic).
  - **Uniqueness test**: Quoted text distinguishes PBI-NN from any other PBI entry.
  - **Length test**: 8+ words.

  *Finding quality tests — all must pass:*
  - **Specificity test**: Quoted text names a specific component, behavior, or condition.
  - **Locatability test**: Text is locatable in the source artifact.
  - **Length test**: 8+ words.

  Handle confirmed: H-NN — "{quoted Handle Ledger label text}"
  PBI-Ref confirmed: PBI-NN — "{quoted belief statement — passes all PBI quality tests}"
  Source confirmed: `{skill-type}` — "{quoted finding sentence — passes all finding quality tests}"

---

**Step 7 — Chain Integrity Audit.**

*Run after all entries are written. Confirms end-to-end chain consistency for every entry. Results appear in the artifact as visible tokens immediately after each entry.*

For each entry:

```
Entry: {Surprise Name}
Check A — Handle language: Is H-NN's label finding language (not belief language from PBI)?
  Result: PASS | FAIL — {discrepancy if fail}
Check B — Tier consistency: Does the tier header match the Step 5 triage assignment?
  Result: PASS | FAIL
Check C — PBI quotation fidelity: Does the quoted PBI text appear verbatim in PBI-NN and pass all three PBI quality tests?
  Result: PASS | FAIL — {discrepancy if fail}
Check D — Finding quotation fidelity: Is the quoted source finding text locatable in the source artifact and does it pass all three finding quality tests?
  Result: PASS | FAIL — {discrepancy if fail}
CHAIN-COMPLETE-{N}: {Surprise Name} | CHAIN-FLAG-{N}: {which checks failed — revise entry}
```

On `CHAIN-FLAG`: revise the entry, re-run the audit. Proceed only when all entries are `CHAIN-COMPLETE`. Audit tokens appear in the artifact.

---

**Step 8 — Synthesis.**

**(Institutional Archaeologist:)** Look across the entries: do two or more corrections address the same category of misunderstanding — the same structural flaw in how the current materials frame the problem? Write 2-4 sentences. Look for a pattern in how materials mislead future teams, not the original team's discovery sequence. Name any pattern; state its absence explicitly if none.

---

**Step 9 — Riskiest assumption.**

Flag the single surprise most likely to invalidate a core assumption. State: (a) the assumption at risk, (b) the signal that revealed it, (c) what would need to be true for the assumption to hold despite the surprise. One labeled paragraph.

---

**Step 10 — Rules of Thumb (impact-anchored).**

Write <=3 rules encoding the highest-impact surprises in quotable form:

```
[{HIGH | MEDIUM}] {Rule — <=20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 6})
```

**Anchoring constraint**: The tier in each rule must match the tier in the surprise entry it encodes. LOW surprises do not generate rules.

**Traceability check**: After writing all rules, verify: does each rule's tier match the tier header of the surprise it names? Confirm with `RULES-ANCHORED: all tiers verified.`

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order:
1. Provenance Enforcement Mechanism table (Step 2, headed section)
2. Prior Belief Inventory table (Step 2)
3. Handle Ledger table (Step 3)
4. Individual surprise entries with `CHAIN-COMPLETE` audit tokens (Steps 6-7)
5. Synthesis (Step 8)
6. Riskiest assumption (Step 9)
7. Rules of Thumb (Step 10)

Steps 1, 4, 5 are execution scaffolding.
