---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 5
rubric: v5
---

# Variations: `topic:echo` — Round 5 (v5 rubric targets)

**Rubric:** v5 | **Date:** 2026-03-16

---

## Design Context

R4 V-05 scored 140/140 under v5 — the first variation to pass all ten aspirational criteria.
Two rubric criteria drove the jump from R3:

- **C-17 — Enforcement mechanism strength classification with calibration rationale**: R4
  V-01/V-04 named the mechanism type ("structural provenance") but omitted the tier position
  (`structural > temporal`) and the distinguishing property (role-scope exclusion vs. phase
  sequencing). V-03 added tier + property. V-05 added tier + property + reviewer implication
  ("independence is enforced, not instructed; C-13 is confirmatory rather than probative").
  V-05 passed C-17 at the highest level by making the calibration rationale self-contained
  for a reviewer unfamiliar with the hierarchy.

- **C-18 — Per-entry attestation with evidentiary quotation**: R4 V-02/V-04 named each
  check in the `Verified:` field (handle confirmed, PBI-Ref confirmed, source artifact
  confirmed) but quoted only identifiers. V-05 quoted actual PBI entry belief text and
  actual source finding sentence inline, so a reviewer can confirm citation correctness from
  the entry alone without navigating to PBI or signal artifact. V-05 passed C-18 by making
  the Verified field a disclosure of evidence, not a declaration of action.

**What R5 targets:**

V-05 from R4 achieved 140/140 by embedding C-17 calibration rationale in PBI section prose
and embedding C-18 evidentiary quotation in per-entry Verified fields. Three structural
questions remain unanswered:

1. **Navigability of C-17**: The enforcement mechanism calibration rationale in R4 V-05 lives
   inside PBI section text. A reviewer auditing C-17 must search within prose. A standalone
   headed section would make tier + property + reviewer implication immediately locatable
   without full-artifact reading. Does dedicated-section placement surface a new excellence
   pattern (C-19 candidate: mechanism declaration is in a headed section, independently
   navigable)?

2. **Quotation quality in C-18**: R4 V-05 required quotation but defined quality as
   "substantive enough to confirm the citation is correct." No pass/fail criteria were stated
   at production time. A variation that adds explicit quotation quality criteria (minimum
   content, must uniquely identify the cited entry, must contain the key predicate) makes
   C-18 self-evaluating rather than reviewer-evaluated. Does self-evaluating quotation quality
   surface a new excellence pattern (C-19 or C-20 candidate)?

3. **Chain integrity post-production**: R4 V-05 enforces the chain [PBI-Ref → Handle → Source
   artifact → Verified quotation] at individual entry production time, but does not run a
   post-production audit confirming all four chain elements are internally consistent. A
   variation that adds a Chain Integrity Audit — verifying that each quoted PBI text matches
   the PBI-NN entry, each quoted finding text matches the source artifact, and Handle labels
   use finding language not belief language — might surface a new pattern (C-19 candidate:
   chain integrity audit is present and its results are visible in the output).

**R5 variation axes:**

- V-01: Single-axis — Dedicated Enforcement Mechanism Section (C-17 navigability axis)
- V-02: Single-axis — Quotation Quality Template (C-18 self-evaluation axis)
- V-03: Single-axis — Post-Production Chain Integrity Audit (potential v6 excellence signal)
- V-04: Combination (V-01 + V-02): Dedicated C-17 Section + Quotation Quality Template
- V-05: Full combination (V-01 + V-02 + V-03 + Institutional Archaeologist + impact ranking)

**Predicted scoring under v5:**

| Variation | C-17 | C-18 | C-09 | C-10 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 | PASS | PASS | FAIL | FAIL | 8/10 = 40 | 130 |
| V-02 | FAIL | PASS | FAIL | FAIL | 7/10 = 35 | 125 |
| V-03 | PASS | PASS | PASS | PASS | 10/10 = 50 | 140 |
| V-04 | PASS | PASS | FAIL | FAIL | 8/10 = 40 | 130 |
| V-05 | PASS | PASS | PASS | PASS | 10/10 = 50 | 140 |

V-02 fails C-17 (no dedicated section, inline prose only — testing whether navigability matters).
V-01 and V-04 reach 130 by omitting ranking/riskiest flag.
V-03 and V-05 target 140/140 via distinct structural paths.

---

## V-01 — Dedicated Enforcement Mechanism Section

**Variation axis:** Lifecycle emphasis — the enforcement mechanism classification is extracted
from PBI section prose into a standalone headed section appearing immediately after the PBI
and before the Handle Ledger. The section contains a structured table with tier, distinguishing
property, and reviewer implication as separate named rows. Builds on R4 V-01 structure
(PBI + Handle Ledger + Typed Gate + "We believed:" field). Targets C-17 at full pass level.

**Hypothesis:** R4 V-01/V-05 embedded the enforcement declaration in PBI section preamble
prose, requiring reviewers to search within text to locate tier, property, and implication.
C-17's practical requirement ("a reviewer unfamiliar with the hierarchy must immediately know
how much weight to place on the independence claim") is better served by a dedicated section
a reviewer can navigate to by heading. Structural placement may surface a new excellence
signal: can a reviewer audit C-17 from a single section without reading the rest of the
artifact? If yes, a new C-19 candidate emerges: the enforcement declaration is in a headed
section, independently navigable without full-artifact reading.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not
expect? It is institutional memory for the next team that walks this path. Each entry is
a named surprise — sourced, contrasted with a named falsifiable prior belief, and assessed
for specific design impact.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials for `{topic}` have predicted
this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption.
*Test:* "Is this finding included because it overturned an assumption, or because it happened
and seemed notable?" If the latter → cut.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each artifact was investigating
and its key findings. Internal scaffolding — do not include in the output artifact.

---

**Step 2 — Prior Belief Inventory.**

*Write this section before consulting any signal artifact content. You are in the
belief-writing role: access only the original design materials for `{topic}` (spec, proposal,
draft, stated assumptions). You do not have access to signal artifacts in this role. This
is structural provenance isolation: role-scope exclusion prevents access regardless of
instruction.*

State the team's prior beliefs about `{topic}` before investigation began. Each entry is
a belief that investigation could confirm or contradict.

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X} — a testable proposition that investigation could have confirmed. |
| PBI-02 | |
| PBI-03 | |

*PBI entries must be falsifiable: "We believed X" where X is a predicate that could have
been right. "We hadn't thought about X" is not a prior belief. "We were uncertain about X"
is not a falsifiable proposition. Minimum 3 entries.*

**[COMMIT-PBI: Written in the belief-writing role before signal artifacts were read.]**

---

**Step 3 — Enforcement Mechanism Declaration.**

*This section classifies the provenance isolation used to protect the PBI from signal
knowledge. Write it immediately after committing the PBI. It appears as a headed section
in the artifact so reviewers can locate it by heading without reading the full artifact.*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| **Mechanism type** | Structural provenance |
| **Tier** | Structural > temporal |
| **Distinguishing property** | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts regardless of instruction. Temporal provenance is enforced by phase sequencing — phases are ordered, but cross-phase reasoning by the same agent is not blocked. Role-scope exclusion is the stronger mechanism because it closes the cross-phase reasoning path that phase gates leave open. |
| **Reviewer implication** | Independence is enforced, not instructed. C-13 content-analysis evidence (PBI entries use belief language; Handle Ledger titles use finding language) is confirmatory rather than probative: the mechanism already ensures independence; content analysis confirms it holds. |

*Do not alter this table. It must be present in the artifact as a headed section. A reviewer
auditing C-17 can navigate to this section by heading and find all three elements — tier,
property, reviewer implication — without reading surrounding artifact content.*

---

**Step 4 — Handle Ledger.**

*Write this section after reading signal artifacts. Do not consult the PBI section while
writing Handle labels. Handle labels must use finding language — what signals revealed —
not belief language from the PBI.*

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check before committing: do any Handle labels echo PBI entry phrasing verbatim?
If yes, revise to use language the PBI could not have anticipated.*

**[COMMIT-HANDLE-LEDGER]**

---

**Step 5 — Adversarial Gate.**

You are the **Gatekeeper**. For each candidate finding from signal reading, apply the
Anti-Pattern Catalog and issue a verdict:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: {Complete: "We believed {X}" where X is a testable proposition.
  VALID: "We believed the session store was stateless between reconnects."
  INVALID: "We hadn't considered reconnect behavior." (absence, not a belief)
  INVALID: "This surprised the team." (reaction, not a proposition)
  INVALID: "We were uncertain about this." (uncertainty is not a falsifiable belief)
  A SURPRISE verdict with an invalid "We believed:" is structurally incomplete.}
PBI-Ref: {the specific PBI-NN this candidate contradicts — required for SURPRISE verdicts}
H-Ref: {the Handle Ledger entry this candidate corresponds to — H-NN}
```

Valid verdicts: `SURPRISE`, `CUT — finding-as-surprise substitution`, `CUT — summary-in-disguise`,
`CUT — orphan-attribution`. Bare `CUT` invalid. Minimum 2 SURPRISE verdicts required.
Gatekeeper log is execution scaffolding — do not include in output.

---

**Step 6 — Write echo entries.**

For each SURPRISE candidate (minimum 2), produce one entry. Write entries in any order;
sequence does not affect artifact structure.

**[Surprise Name]**
*2-5 words, title case. Must match a Handle Ledger entry. Citable by a future team without
reading this echo.*

- **Handle**: H-NN (from Handle Ledger)
- **PBI-Ref**: PBI-NN (the prior belief this contradicts)
- **Source signal**: `{skill-type}` — name the specific artifact or skill type. Must pass
  the orphan-attribution test.
- **We believed**: The falsifiable prior belief from the Gatekeeper's verdict. One full
  sentence preserving its testable form.
- **Finding**: What the signal actually revealed. Must directly contradict "We believed."
  One sentence.
- **Design impact**: The specific component, flow, or decision this changes, constrains,
  or challenges. Must name something specific — not "this affects the design." One sentence.
- **Verified**:
  - Handle confirmed: H-NN — "{quote the Handle Ledger label text for H-NN}"
  - PBI-Ref confirmed: PBI-NN — "{quote the full belief statement from PBI-NN entry — must
    include the predicate: what the team staked on}"
  - Source confirmed: `{skill-type}` — "{quote the specific sentence from the source artifact
    that documents this finding — must name a component, behavior, or condition, not a
    general statement}"

---

**Step 7 — Synthesize.**

Do the surprises cluster? Write 2-4 sentences: do 2+ share a root cause, reveal the same
blind spot, or together indicate a design direction not previously visible? Name any pattern
explicitly; state its absence if none is evident.

---

**Step 8 — Forward guidance.**

Write 1-3 sentences addressed to the next team building `{topic}`. Register: "If you are
about to build X, know that Y because we found Z." Specific to these surprises.

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact sections in order:
1. **Provenance Enforcement Mechanism** table (Step 3) — headed section, as written
2. **Prior Belief Inventory** table (Step 2) — as committed
3. **Handle Ledger** table (Step 4) — as committed
4. Individual surprise entries (Step 6)
5. Synthesis (Step 7)
6. Forward guidance (Step 8)

Steps 1, 5 are execution scaffolding — do not include.

---

## V-02 — Quotation Quality Template

**Variation axis:** Output format — the Verified field in each surprise entry uses a
structured quotation template with explicit pass/fail quality criteria for each quotation.
The criteria are stated at production time and must be applied before the field is committed.
Does not use a dedicated C-17 section; enforcement declaration appears inline in PBI preamble.
Builds on R4 V-02 structure (Pre-Write Prediction Sort with typed Route: labels). Targets
C-18 at the highest self-evaluating pass level.

**Hypothesis:** R4 V-05 required evidentiary quotation but defined quality as "substantive
enough to confirm the citation is correct" — a reviewer judgment, not a production-time
check. A variation that states quotation quality criteria at production time (minimum content
requirements, uniqueness requirement, predicate requirement) makes C-18 self-evaluating:
the author can test whether each quotation passes before committing the entry. This removes
reviewer guesswork about what "substantive" means. Two effects follow: (1) borderline
quotations that pass reviewer review but don't actually confirm the citation are structurally
unproducible; (2) the author must explicitly confirm each quotation's quality, making the
attestation more rigorous. This may surface a new excellence signal: the quotation quality
criteria are stated as named pass/fail tests, not narrative guidance (potential C-19:
quotation quality is self-certifying at production time via named pass/fail criteria).

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect?
It is institutional memory for the next team that walks this path. Each entry is a named
surprise — sourced, contrasted with a named falsifiable prior belief, and assessed for
specific design impact.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption.
*Test:* "Could this output be described as a summary of what the investigation found?"
Yes → you have at least one of these.

**orphan-attribution** — a genuine surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces. Note what
each was investigating and its key findings. Internal scaffolding.

---

**Step 2 — Pre-Write Prediction Sort (Routing Layer).**

This step runs before any candidates enter the gate pipeline. Every finding is assigned a
typed destination — no finding is discarded without a named home.

For each notable finding, record:

```
Finding: {one phrase}
Predicted? YES | NO
Route: {one named artifact type — required}
```

> "Before this investigation began — reading only the original design materials for
> `{topic}` — would we have predicted this finding?"

Route assignment:
- YES → `topic-story` (confirms what the design assumed)
- YES, process finding → `topic-report` (about how investigation ran, not what `{topic}` does)
- NO → `gate-pipeline` (proceeds to adversarial gate)

**Invalid routes — do not use:** "excluded from echo," blank, "not included." Every finding
requires a named typed route. Collect at least 3 `gate-pipeline` findings before proceeding.
Sort log is execution scaffolding — do not include in output.

---

**Step 3 — Prior Belief Inventory.**

*Write this section before returning to any signal artifact content. Access only original
design materials.*

This echo uses structural provenance isolation: the PBI was written in a role that accesses
only original design materials, not signal artifacts. Structural provenance (role-scope
exclusion) is stronger than temporal provenance (phase sequencing) because role-scope
exclusion prevents cross-phase reasoning, not only cross-phase reading.

| PBI-Ref | Prior Belief |
|---------|--------------|
| PBI-01 | We believed {falsifiable proposition} |
| PBI-02 | |
| PBI-03 | |

**[COMMIT-PBI]**

---

**Step 4 — Handle Ledger.**

*Written after reading signals. Handle labels use finding language — what signals revealed.*

| Handle # | Handle Label | Source skill |
|----------|-------------|-------------|
| H-01 | | |
| H-02 | | |

**[COMMIT-HANDLE-LEDGER]**

---

**Step 5 — Adversarial Gate.**

You are the **Gatekeeper**. Apply the Anti-Pattern Catalog to each `gate-pipeline` candidate:

```
Candidate: {description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: "We believed {X}" — testable proposition, not impression or absence.
PBI-Ref: PBI-NN
H-Ref: H-NN
```

Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 6 — Write echo entries.**

For each SURPRISE candidate (minimum 2):

**[Surprise Name]**
*2-5 words, title case, matches a Handle Ledger entry.*

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}`
- **We believed**: The falsifiable prior belief. One full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision. One sentence.
- **Verified** — apply the following quality tests before committing each quotation:

  *PBI quotation quality tests (all must pass):*
  - Does the quoted text contain the full predicate of the belief — what the team staked on?
    (Not just a topic word: "session tokens" fails; "session tokens were preserved across
    reconnects" passes — it names what the team believed about the topic.)
  - Is the quoted text unique to PBI-NN — would it distinguish PBI-NN from any other PBI entry?
  - Does the quotation contain 8+ words? (A fragment too short to confirm the correct entry fails.)

  *Finding quotation quality tests (all must pass):*
  - Does the quoted text name a specific component, behavior, or condition — not a general
    observation?
  - Is the quoted text locatable in the source artifact — a reader navigating there would
    find it?
  - Does the quotation contain 8+ words?

  PBI-Ref confirmed: PBI-NN — "{quoted PBI entry text — must pass all three PBI quality
    tests above before committing}"
  Handle confirmed: H-NN — "{Handle Ledger label text}"
  Source confirmed: `{skill-type}` — "{quoted source finding sentence — must pass all three
    finding quality tests above before committing}"

  *Quality self-certification: before committing this Verified field, confirm each quotation
  passes its named quality tests. A Verified field with a quotation that fails any named test
  is structurally incomplete.*

---

**Step 7 — Synthesize.**

Do the surprises cluster? 2-4 sentences. Do 2+ share a root cause, reveal the same blind
spot, or together indicate a design direction not previously visible? Name any pattern;
state its absence explicitly if none.

---

**Step 8 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Register: "If you are about to build X,
know that Y because we found Z."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact sections: PBI table (Step 3), Handle Ledger (Step 4), individual entries (Step 6),
synthesis (Step 7), forward guidance (Step 8). Steps 1, 2, 5 are execution scaffolding.

---

## V-03 — Post-Production Chain Integrity Audit

**Variation axis:** Lifecycle emphasis — after all surprise entries are written, a dedicated
Chain Integrity Audit step runs, verifying end-to-end consistency: for each entry, the quoted
PBI text matches PBI-NN, the quoted finding text is locatable in the source artifact, Handle
labels use finding language (not belief language from PBI), and all four chain elements are
internally consistent. Builds on the full R4 V-01 + C-17 + C-18 structure. Adds ranking
(C-09) and riskiest flag (C-10). Targets potential v6 excellence signal (C-19 candidate).

**Hypothesis:** R4 V-05 enforced the chain [PBI-Ref → Handle → Source artifact → Verified
quotation] at entry production time, but did not run post-production validation confirming
all four elements are internally consistent. A post-production audit that (1) re-checks each
quoted PBI text against the PBI table, (2) re-checks each quoted finding text against the
source artifact, (3) confirms Handle labels use finding language not belief language, and
(4) produces a visible CHAIN-COMPLETE or CHAIN-FLAG token per entry adds a third enforcement
layer: field definitions prohibit bad vocabulary at production time, per-entry Verified
fields attest checks were performed, and the chain audit confirms attestations are correct.
Three-layer enforcement (definition → attestation → audit) may surface a new criterion:
the audit produces visible per-entry tokens, making chain integrity auditable from the
output alone without re-running the production steps.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not
expect? It is institutional memory for the next team that walks this path. Each entry is
a named surprise — sourced, contrasted with a named falsifiable prior belief, ranked by
design impact, and assessed for specific consequence.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings for coverage, not because they contradicted an assumption.
*Test:* "Is this here because it overturned an assumption, or because it happened?" Latter → cut.

**orphan-attribution** — a surprise with no traceable source artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces. Note what each
was investigating. Internal scaffolding.

---

**Step 2 — Prior Belief Inventory.**

*Write before consulting any signal artifact content. You are in the belief-writing role:
access only original design materials. This is structural provenance isolation (role-scope
exclusion).*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| Mechanism type | Structural provenance |
| Tier | Structural > temporal |
| Distinguishing property | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts regardless of instruction. Temporal provenance is enforced by phase sequencing — phases are ordered, but the same agent can reason across phases. Role-scope exclusion closes the cross-phase reasoning path. |
| Reviewer implication | Independence is enforced, not instructed. C-13 content analysis (PBI entries use belief language; Handle labels use finding language) is confirmatory rather than probative. |

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X — testable predicate} |
| PBI-02 | |
| PBI-03 | |

**[COMMIT-PBI: Written in the belief-writing role, before signal artifacts were read.
Structural provenance isolation applied per the Enforcement Mechanism Declaration above.]**

---

**Step 3 — Handle Ledger.**

*Written after reading signals. Handle labels use finding language — what signals revealed,
not what the team believed.*

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check: does any Handle label echo PBI entry language verbatim? If yes, revise.*

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
  INVALID: "This was surprising." (reaction)
PBI-Ref: PBI-NN (the entry this contradicts)
H-Ref: H-NN
```

Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 5 — Impact triage (pre-write).**

Assign each SURPRISE candidate an impact tier before writing any entry:

- **HIGH**: Forces a design decision to change or invalidates a major assumption.
- **MEDIUM**: Requires adjustment to a specific component or flow.
- **LOW**: Informative; does not change design trajectory.

Order candidates: HIGH → MEDIUM → LOW. Ties broken by specificity of impact.
Triage list is execution scaffolding — do not include in output.

---

**Step 6 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
*2-5 words, title case. Must match a Handle Ledger entry. Citable without reading this echo.*

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}` — specific artifact or skill type.
- **We believed**: The falsifiable prior belief. One full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision. One sentence. Must name something
  specific.
- **Verified**:
  - Handle confirmed: H-NN — "{quoted Handle Ledger label text}"
  - PBI-Ref confirmed: PBI-NN — "{quoted full belief statement from PBI-NN, including the
    predicate — what the team staked on, 8+ words}"
  - Source confirmed: `{skill-type}` — "{quoted specific sentence from the source artifact
    that documents this finding, naming a component or behavior, 8+ words}"

---

**Step 7 — Chain Integrity Audit.**

*Run this audit after all entries are written. Do not skip. The audit confirms the
end-to-end chain [PBI-Ref → Handle → Source artifact → Verified quotation] is internally
consistent across all entries. Its results appear in the artifact as visible tokens.*

For each surprise entry, apply the following checks:

```
Entry: {Surprise Name}
Check 1 — Handle language: Does H-NN's label use finding language (what signals showed),
  not belief language (what the team assumed)? Compare H-NN text with PBI entries.
  Result: PASS | FAIL — {if fail: which PBI entry's language appears in H-NN}
Check 2 — PBI quotation match: Does the quoted PBI text in Verified actually appear in
  the PBI-NN entry? Does it contain the full predicate?
  Result: PASS | FAIL — {if fail: discrepancy between quoted text and PBI entry}
Check 3 — Finding quotation match: Is the quoted source finding text locatable in the
  source artifact? Does it name a specific component or behavior?
  Result: PASS | FAIL — {if fail: quoted text is generic or not locatable}
Check 4 — Tier consistency: Does the impact tier in the entry header match the triage
  assignment in Step 5?
  Result: PASS | FAIL
Audit verdict: CHAIN-COMPLETE-{N} | CHAIN-FLAG-{N}: {which checks failed}
```

If any entry produces `CHAIN-FLAG`, revise that entry before proceeding. Do not write the
artifact until all entries produce `CHAIN-COMPLETE`. The audit tokens appear in the artifact
after the entry they validate.

---

**Step 8 — Synthesis.**

Do the surprises cluster? Write 2-4 sentences: do 2+ share a root cause, reveal the same
blind spot, or indicate a design direction not previously visible? Name any pattern; state
its absence explicitly if none.

---

**Step 9 — Riskiest surprise.**

Flag the single surprise most likely to invalidate a core assumption. State: (a) the
assumption at risk, (b) the signal that revealed it, (c) what would need to be true for
the assumption to hold despite the surprise.

---

**Step 10 — Forward guidance.**

Write 1-3 sentences for the next team building `{topic}`. Register: "If you are about to
build X, know that Y because we found Z."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact sections in order:
1. Provenance Enforcement Mechanism table (from Step 2)
2. Prior Belief Inventory table (from Step 2)
3. Handle Ledger table (Step 3)
4. Individual surprise entries + Chain Integrity Audit tokens (Steps 6-7)
5. Synthesis (Step 8)
6. Riskiest surprise (Step 9)
7. Forward guidance (Step 10)

Steps 1, 4, 5 are execution scaffolding.

---

## V-04 — Combination: Dedicated C-17 Section + Quotation Quality Template

**Variation axis:** Lifecycle emphasis + output format — V-01's dedicated Enforcement
Mechanism Declaration section combined with V-02's quotation quality template (named pass/fail
criteria per quotation). Full gate chain from R4 V-04. Does not include impact ranking (C-09),
riskiest flag (C-10), or Chain Integrity Audit.

**Hypothesis:** V-01 tests whether dedicated section placement surfaces a C-19 signal for
C-17 navigability. V-02 tests whether self-certifying quotation quality surfaces a C-19 or
C-20 signal for C-18 rigor. V-04 combines both: if either structural innovation alone reaches
130, the combination should confirm both independently and achieve 130 (same ceiling, since
C-09 and C-10 are absent). The more interesting question: does combining dedicated-section
C-17 with self-certifying C-18 produce a qualitative interaction — does having both in the
same artifact surface a third excellence signal (C-19 candidate: the mechanism declaration
section and the per-entry quotation quality certification are mutually reinforcing, making
the independence claim auditable at section level AND at entry level simultaneously)?

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not
expect? Each entry is a named surprise — sourced, contrasted with a falsifiable prior belief,
and assessed for design impact. Its audience is the next team that walks this path.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" Yes → cut.

**summary-in-disguise** — findings included for coverage, not because they contradicted
an assumption. *Test:* "Is this here because it overturned an assumption?" No → cut.

**orphan-attribution** — a surprise with no traceable source artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/`. Internal scaffolding.

---

**Step 2 — Prior Belief Inventory.**

*Written before consulting signal artifact content. Structural provenance isolation applies:
belief-writing role accesses only original design materials.*

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X} |
| PBI-02 | |
| PBI-03 | |

**[COMMIT-PBI: Written in belief-writing role before signal artifacts were read.]**

---

**Step 3 — Enforcement Mechanism Declaration.**

*Written immediately after COMMIT-PBI. Appears as a headed section in the artifact.*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| Mechanism type | Structural provenance |
| Tier | Structural > temporal |
| Distinguishing property | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts regardless of instruction. Temporal provenance is enforced by phase sequencing, which orders phases but does not block cross-phase reasoning by the same agent. Role-scope exclusion is the stronger mechanism. |
| Reviewer implication | Independence is enforced, not instructed. C-13 content analysis (belief vs. finding language) is confirmatory rather than probative: the mechanism guarantees independence; content analysis confirms it holds. |

*This section is headed so reviewers can audit C-17 (tier, property, reviewer implication)
by navigating to this heading without reading the full artifact.*

---

**Step 4 — Handle Ledger.**

*Written after reading signals. Handle labels use finding language — not belief language.*

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check: does any Handle label echo PBI language verbatim? Revise if yes.*

**[COMMIT-HANDLE-LEDGER]**

---

**Step 5 — Adversarial Gate.**

You are the **Gatekeeper**. For each candidate, issue a verdict:

```
Candidate: {description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: "We believed {X}" — falsifiable proposition, not impression or absence.
PBI-Ref: PBI-NN
H-Ref: H-NN
```

Minimum 2 SURPRISE verdicts. Gate log is scaffolding.

---

**Step 6 — Write echo entries.**

For each SURPRISE candidate (minimum 2):

**[Surprise Name]**
*2-5 words, title case, matches Handle Ledger, citable without reading this echo.*

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}`
- **We believed**: Falsifiable prior belief. One full sentence.
- **Finding**: What the signal revealed. Directly contradicts "We believed." One sentence.
- **Design impact**: Specific component, flow, or decision. One sentence.
- **Verified** — apply these named quality tests before committing each quotation:

  *PBI quotation tests (all must pass before committing):*
  - **Predicate test**: Does the quoted text include the predicate of the belief — what the
    team specifically staked on? (Topic word alone fails; belief sentence with predicate passes.)
  - **Uniqueness test**: Would the quoted text distinguish PBI-NN from any other PBI entry in
    the table?
  - **Length test**: Is the quotation 8+ words?

  *Finding quotation tests (all must pass before committing):*
  - **Specificity test**: Does the quoted text name a specific component, behavior, or condition
    (not a general statement like "this was more complex than expected")?
  - **Locatability test**: Is the quoted text locatable in the source artifact — a reader
    navigating to `{skill-type}` would find this sentence?
  - **Length test**: Is the quotation 8+ words?

  PBI-Ref confirmed: PBI-NN — "{quoted PBI belief statement — passes all three PBI tests}"
  Handle confirmed: H-NN — "{quoted Handle Ledger label}"
  Source confirmed: `{skill-type}` — "{quoted source finding sentence — passes all three
    finding tests}"

---

**Step 7 — Synthesize.**

2-4 sentences: do 2+ surprises share a root cause, reveal the same blind spot, or together
indicate a design direction not previously visible? Name any pattern; state its absence.

---

**Step 8 — Forward guidance.**

1-3 sentences for the next team. Register: "If you are about to build X, know that Y."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact sections: Provenance Enforcement Mechanism (Step 3), PBI table (Step 2), Handle
Ledger (Step 4), entries (Step 6), synthesis (Step 7), forward guidance (Step 8).
Steps 1, 5 are execution scaffolding.

---

## V-05 — Full Combination: All Criteria + All R5 Structural Innovations

**Variation axis:** All axes — V-01's dedicated C-17 section, V-02's self-certifying
quotation quality template, V-03's post-production Chain Integrity Audit, plus Institutional
Archaeologist role (C-17 axis from R4), impact ranking with argued rationale (C-09), riskiest
surprise flag (C-10), and impact-annotated Rules of Thumb. All ten aspirational criteria
at structurally distinct moments.

**Hypothesis:** V-03 and V-04 each hit 140/140 via distinct structural paths. V-05
combines all R5 innovations to test whether three-layer enforcement (definition → production-
time attestation → post-production audit) produces a qualitative signal beyond 140/140. The
three-layer architecture creates a new property: the chain integrity is not only claimed
(C-15/C-17), not only attested per entry (C-16/C-18), but audited post-production with
visible tokens (potential C-19). Additionally, V-05 tests whether the Institutional
Archaeologist role + dedicated mechanism section creates a structural interaction: the
Archaeologist frames entries as corrections for future teams; the mechanism declaration
confirms independence was enforced; the chain audit confirms the entries' evidentiary
citations are correct. If all three work together, a reviewer has three independent
confirmation layers for the artifact's trustworthiness, not one. This three-layer structure
may surface C-19: the artifact contains a post-production audit layer, distinct from the
production-time attestation layer (C-16/C-18), with visible per-entry tokens confirming
chain integrity end-to-end.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**Your operating role: Institutional Archaeologist.**

An Institutional Archaeologist recovers false assumptions from a body of work — specifically
the ones the current design materials still carry, that a new team would inherit and act on
incorrectly without this artifact. You hold this identity throughout. Where a step or field
is prefixed with **(Institutional Archaeologist:)**, your answer must come from the position
of someone arriving cold to the materials and asking: what would the next team get wrong?

The Institutional Archaeologist is distinct from the Gatekeeper role in Step 4. The
Gatekeeper tests whether a finding qualifies as a surprise. The Institutional Archaeologist
frames what that surprise means for a reader who was not present.

---

**Anti-Pattern Catalog — read before executing. You will cite these labels by name.**

**finding-as-surprise substitution** — an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials for `{topic}` have predicted
this?" Yes → cut.

**summary-in-disguise** — findings for coverage, not because they contradicted an assumption.
*Test:* "Could this output be described as a summary of what the investigation found?"
Yes → you have at least one of these.

**orphan-attribution** — a surprise with no traceable signal artifact.
*Test:* "Can I name the specific artifact or skill type?" No → cut until you can.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Note what each was investigating.
Internal scaffolding.

---

**Step 2 — Prior Belief Inventory + Enforcement Mechanism Declaration.**

*Written before consulting signal artifact content. You are in the belief-writing role:
access only original design materials. This is structural provenance isolation (role-scope
exclusion).*

## Provenance Enforcement Mechanism

| Field | Declaration |
|-------|-------------|
| Mechanism type | Structural provenance |
| Tier | Structural > temporal |
| Distinguishing property | Structural provenance is enforced by role-scope exclusion: the belief-writing role cannot access signal artifacts, regardless of instruction. Temporal provenance is enforced by phase sequencing — the same agent can still reason across phases even when reading is ordered. Role-scope exclusion is the stronger mechanism because it closes the cross-phase reasoning path that phase gates leave open. |
| Reviewer implication | Independence is enforced, not instructed. C-13 content analysis (PBI entries use belief language; Handle labels use finding language) is confirmatory rather than probative: the mechanism already ensures independence; content analysis confirms it holds. A reviewer unfamiliar with the hierarchy can calibrate from this section alone without re-deriving the claim. |

*This section is headed so reviewers can navigate to it directly and confirm tier, property,
and reviewer implication without reading the full artifact.*

## Prior Belief Inventory

| PBI-Ref | Prior Belief (falsifiable proposition) |
|---------|----------------------------------------|
| PBI-01 | We believed {X — testable predicate that investigation could have confirmed} |
| PBI-02 | |
| PBI-03 | |

*Each belief must be falsifiable: a testable proposition, not an impression or absence of
consideration. Minimum 3 entries.*

**[COMMIT-PBI: Written in the belief-writing role, before signal artifacts were read.
Structural provenance isolation confirmed per Enforcement Mechanism Declaration above.]**

---

**Step 3 — Handle Ledger.**

*Written after reading signals. Do not consult PBI while writing Handle labels. Handle labels
use finding language — what signals revealed. (Institutional Archaeologist:) Encode what the
current materials still carry wrong, not what the original team discovered.*

| Handle # | Handle Label (finding language, 2-5 words, title case) | Source skill |
|----------|--------------------------------------------------------|-------------|
| H-01 | | |
| H-02 | | |

*Independence check: does any Handle label echo PBI entry language verbatim? If yes, revise
to use language specific to what signals showed — language the PBI could not have anticipated.*

**[COMMIT-HANDLE-LEDGER]**

---

**Step 4 — Adversarial Gate.**

You are the **Gatekeeper** (not the Institutional Archaeologist — the Gatekeeper's function
is adversarial rejection). Apply the Anti-Pattern Catalog to each candidate:

```
Candidate: {description}
Verdict: SURPRISE | CUT — {anti-pattern label}
We believed: "We believed {X}" — testable proposition.
  VALID: "We believed the scheduler deduplicated events before dispatching callbacks."
  VALID: "We believed the compliance check ran at write time, not read time."
  INVALID: "We hadn't considered this case." (absence)
  INVALID: "This was surprising to the team." (reaction)
  INVALID: "We were uncertain here." (uncertainty is not a falsifiable belief)
  A SURPRISE verdict with an invalid "We believed:" is structurally incomplete.
PBI-Ref: PBI-NN
H-Ref: H-NN
```

Valid verdicts: `SURPRISE`, `CUT — finding-as-surprise substitution`, `CUT — summary-in-disguise`,
`CUT — orphan-attribution`. Bare `CUT` invalid. Minimum 2 SURPRISE verdicts. Scaffolding.

---

**Step 5 — Impact triage (pre-write).**

Before writing any entry, assign each SURPRISE candidate an impact tier:

- **HIGH**: Forces a design decision to change or invalidates a major assumption. Cannot
  proceed as planned without addressing this.
- **MEDIUM**: Requires adjustment to a specific component or flow.
- **LOW**: Informative; does not change design trajectory.

Order: HIGH → MEDIUM → LOW. Ties broken by specificity. Triage list is scaffolding.

---

**Step 6 — Write echo entries (highest impact first).**

For each SURPRISE candidate in triage order:

**[Surprise Name]** — `{HIGH | MEDIUM | LOW}`
**(Institutional Archaeologist:)** Encode the correction the next team needs, not the
discovery the original team made. "The Cascade Inversion" — what the next team must correct
for — passes; "Unexpected Cascade Behavior" — what the original team experienced — does not.
A name passes if a future reader can cite it without having been present.

- **Handle**: H-NN
- **PBI-Ref**: PBI-NN
- **Source signal**: `{skill-type}` — specific artifact or skill type. Passes orphan-attribution.
- **We believed**: The falsifiable prior belief from the Gatekeeper's verdict. One full sentence.
- **The correction**: What the signal showed instead. Directly contradicts "We believed." One sentence.
- **What the next team would get wrong**: **(Institutional Archaeologist:)** The specific
  decision, component, or flow the next team would mis-design if they carried the false
  assumption. Name the concrete mis-design — not "this would cause problems." One sentence.
- **Verified** — apply these named quality tests before committing each quotation:

  *PBI quotation tests (all must pass):*
  - **Predicate test**: Does the quoted text include the full predicate — what the team staked on?
  - **Uniqueness test**: Does the quoted text distinguish PBI-NN from any other PBI entry?
  - **Length test**: Is the quotation 8+ words?

  *Finding quotation tests (all must pass):*
  - **Specificity test**: Does the quoted text name a specific component, behavior, or condition?
  - **Locatability test**: Is the quoted text locatable in the source artifact?
  - **Length test**: Is the quotation 8+ words?

  Handle confirmed: H-NN — "{quoted Handle Ledger label text}"
  PBI-Ref confirmed: PBI-NN — "{quoted PBI belief statement — passes all PBI quality tests}"
  Source confirmed: `{skill-type}` — "{quoted source finding sentence — passes all finding
    quality tests}"

---

**Step 7 — Chain Integrity Audit.**

*Run after all entries are written. Results appear in the artifact as CHAIN-COMPLETE or
CHAIN-FLAG tokens after each entry. Do not write the artifact until all entries are
CHAIN-COMPLETE.*

For each entry, run the following checks:

```
Entry: {Surprise Name}
Check A — Handle language: Is H-NN's label finding language, not belief language from PBI?
  Result: PASS | FAIL — {discrepancy if fail}
Check B — Impact tier consistency: Does the tier header ({HIGH | MEDIUM | LOW}) match the
  Step 5 triage assignment?
  Result: PASS | FAIL
Check C — PBI quotation fidelity: Does the quoted PBI text appear verbatim in PBI-NN? Does
  it contain the full predicate and pass all three PBI quality tests?
  Result: PASS | FAIL — {discrepancy if fail}
Check D — Finding quotation fidelity: Is the quoted source finding text locatable in the
  source artifact? Does it pass all three finding quality tests?
  Result: PASS | FAIL — {discrepancy if fail}
Audit verdict: CHAIN-COMPLETE-{N}: {Surprise Name} | CHAIN-FLAG-{N}: {checks failed, revise entry}
```

On CHAIN-FLAG: revise the flagged entry, re-commit, re-run the audit for that entry.
Proceed only when all entries produce CHAIN-COMPLETE. Audit log appears in the artifact
(audit tokens are part of the artifact, not scaffolding).

---

**Step 8 — Synthesis.**

**(Institutional Archaeologist:)** Look across the entries: do two or more corrections
address the same category of misunderstanding — the same structural flaw in how the current
materials frame the problem? Write 2-4 sentences. Look for a pattern in how the materials
mislead future teams, not the original team's discovery sequence. Name any pattern; state
its absence explicitly if none — absence is itself information for the next team.

---

**Step 9 — Riskiest assumption.**

Flag the single surprise most likely to invalidate a core assumption. State: (a) the
assumption at risk, (b) the signal that revealed it, (c) what would need to be true for
the assumption to hold despite the surprise. One labeled paragraph.

---

**Step 10 — Rules of Thumb (impact-anchored).**

Write <=3 rules encoding the highest-impact surprises in quotable form:

```
[{HIGH | MEDIUM}] {Rule — <=20 words, names a specific behavior or constraint}
(encodes: {Surprise Name from Step 6})
```

**Anchoring constraint**: The tier in each rule must match the tier in the surprise entry
it encodes. A rule annotated `[HIGH]` encoding a `MEDIUM` surprise is malformed — revise.
Only HIGH and MEDIUM surprises generate rules. LOW surprises are too peripheral.

**Traceability check**: After writing all rules, verify: does each rule's tier match the
tier header of the surprise entry it names? Confirm with "RULES-ANCHORED: all tiers verified."

---

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact sections in order:
1. Provenance Enforcement Mechanism table (from Step 2 — headed section)
2. Prior Belief Inventory table (from Step 2)
3. Handle Ledger table (Step 3)
4. Individual surprise entries with CHAIN-COMPLETE tokens (Steps 6-7)
5. Synthesis (Step 8)
6. Riskiest assumption (Step 9)
7. Rules of Thumb (Step 10)

Steps 1, 4, 5 are execution scaffolding.
