I have everything I need. The new v2 rubric (2026-03-16) adds C-11 (Pre-committed PBI with addressable identifiers) and C-12 (Portable named handles). Prior R2 (2026-03-15) targeted a different v2 with different criteria. This round targets the new C-11/C-12 specifically.

---

# Variations: `topic:echo` — Round 2

**Rubric:** v2 (2026-03-16) | **Date:** 2026-03-16

---

## Design Context

**New criteria in v2 (2026-03-16):**

| Criterion | What it requires | What previous rounds did |
|-----------|-----------------|--------------------------|
| C-11 — Pre-committed PBI | Discrete numbered section (PB-01, PB-02...) predating entries; each entry cites identifier | Prior rounds had "Prior Assumption" in-entry (satisfies C-06) but no independent PBI section with identifiers |
| C-12 — Named surprise handles | 2-5 word portable handle; citable without re-reading; must be investigation-specific | Prior rounds required handles but never tested portability or enforced specificity beyond "2-5 words, capitalized" |

**R2 strategy:**

- V-01 through V-03: single-axis. Each targets one criterion with one mechanism.
  - V-01 (Lifecycle Emphasis) → C-11: Phase 0 PBI lock with numbered identifiers; citation field in each entry
  - V-02 (Output Format) → C-12: Handle Ledger committed before entries; portability test explicit
  - V-03 (Phrasing Register) → C-11 + C-12 via concrete analogy ("bet slip"; "Slack citation test")
- V-04: Combination (Role Sequence + Lifecycle Emphasis) → Registrar pre-role produces numbered PBI and draft handles; Chronicler gates and writes entries with citations
- V-05: Combination (Lifecycle Emphasis + Output Format) → PBI lock at Phase 0 + Handle Ledger committed at Phase 2 before entries; both pre-commitments at structurally separate moments

**Discriminating pairs:**
- V-01 vs V-04: isolates whether role separation adds reliability over lifecycle phases alone for C-11
- V-02 vs V-05: isolates whether adding the PBI lock disrupts or reinforces C-12 Handle Ledger compliance
- V-03 vs V-01: isolates whether analogy-based instruction ("bet slip") produces equivalent C-11 compliance to structural phase-based enforcement
- V-03 vs V-04: isolates whether analogy register vs. role division is the stronger mechanism for both criteria simultaneously
- V-04 vs V-05: isolates whether role-based separation or phase-based sequencing better handles both criteria without collapsing into bureaucratic overhead

---

## V-01 — Lifecycle Emphasis axis

**Variation axis:** Lifecycle emphasis — explicit Phase 0 PBI production with numbered identifiers, structurally locked before signal reading, plus mandatory citation field in each entry.

**Hypothesis:** C-11 fails not because prior beliefs are absent but because they are documented alongside or after surprise writing — at which point the "expected" half is post-hoc. The mechanism fix is a phase checkpoint: Phase 0 produces a numbered PBI that is explicitly finalized before Phase 1 begins. The lock is not a reminder to be prior — it is a structural boundary in the prompt. The citation field (`PBI Reference: PB-NN`) in each entry then makes the connection auditable: a reviewer can verify that PB-02 was stated in Phase 0 before signals were read, not invented to frame the finding.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`. Execute phases in order. Do not proceed to the next phase until the current phase is complete.

---

**What the echo is.** It answers one question: what did we learn that we did not expect? It is institutional memory for the next team. It is not a summary of findings. Each entry is a named surprise — sourced, traced to a numbered prior belief, and assessed for design impact. The prior belief citation is not decorative: it is the mechanism that makes every "we expected X" statement auditable.

---

**Phase 0 — Prior Belief Inventory (before reading any signal).**

Read only the pre-investigation materials for `{topic}`: the original spec, design notes, or topic-plan. Do not open signal artifacts yet.

For each namespace that has signals (scout, draft, review, flow, trace, prove, listen, program), write one labeled entry:

```
PB-01  [namespace: scout]   "Before signals, we assumed: ___."
PB-02  [namespace: draft]   "Before signals, we assumed: ___."
PB-03  [namespace: review]  "Before signals, we assumed: ___."
...continue for each namespace with signals
```

Rules for PBI entries:
- Each entry must be specific enough to be falsifiable. "We expected the flow to work normally" cannot be overturned — it confirms under any signal outcome. Write the strongest falsifiable belief a reasonable team member would have held: "We assumed that scout signals would show at least two competitors had not solved the throttle visibility problem." That can lose.
- If no explicit assumption existed for a namespace, state the strongest implicit one the design materials imply.
- Number entries sequentially regardless of namespace order.

**Phase 0 checkpoint.** Write: "PBI frozen at [N] entries: PB-01 through PB-0N." After this statement, the PBI is locked. You may not add or revise entries after Phase 0. The PBI is execution scaffolding — do not include it in the output artifact, but you will cite its identifiers in Phase 3.

---

**Phase 1 — Signal Inventory.**

Read the signal artifacts from `simulations/{topic}/` across all namespaces. For each artifact, note in one phrase what it was investigating. Internal working memory only.

---

**Phase 2 — Gate Adjudication.**

For each notable finding across all signals, apply the surprise gate against the PBI:

> "Does this finding contradict, complicate, or overturn a specific PBI entry?"
>
> YES — note which PB-NN. Verdict: SURPRISE. Carry forward.
> NO — the finding confirms or extends a prior belief. Verdict: CONFIRMATION. Route to `topic-story`.

Issue a verdict for every notable finding. For each SURPRISE verdict, record which PB-NN entry it overturns. Minimum 2 SURPRISE verdicts. If fewer than 2 survive, check whether the PBI entries were too vague to lose against — if so, tighten the implicit beliefs and re-gate. Gate log is execution scaffolding — not included in the output artifact.

---

**Phase 3 — Surprise Entries.**

For each SURPRISE verdict (minimum 2), write one entry using the following form. Every field is required.

**[Surprise Name]**
*2-5 words, capitalized. Specific to this investigation — "API Complexity Surprise" applies to every investigation and fails. "Competitors-Treated-Throttle-As-Solved" is falsifiable against this artifact set and passes.*

- **Source signal**: Specific artifact name or skill type (e.g., `prove-interview`, `flow-resilience`). Traceable to one artifact, not "the signals."
- **PBI Reference**: `PB-NN — [the prior belief this finding overturns, verbatim or close summary of Phase 0 entry]`. Must cite the identifier. This field is what makes C-11 auditable: PB-NN existed before signals were read.
- **Finding**: What the signal actually revealed — must contradict or complicate the referenced PBI entry. One sentence.
- **Design impact**: The specific component, flow, or decision that must change as a result. One sentence. "This affects the design" does not pass — name the thing.

---

**Phase 4 — Synthesis.**

Examine the set of named surprises. Write 2-4 sentences: do two or more surprises overturn PBI entries in the same namespace or reveal the same gap in the original design thinking? If yes, name the pattern and state what it implies. If the surprises are independent, say so explicitly — absence of pattern is itself information.

---

**Phase 5 — Forward Guidance.**

Write 1-3 sentences for the next team building `{topic}`. The register: "If you are about to build X, the beliefs we held about Y (PB-NN) did not survive contact with Z — before you commit, verify ___." Must be derivable only from these surprises, not generic advice.

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure (in order):
1. Surprise Entries — each with PBI Reference field showing identifier
2. Synthesis
3. Forward Guidance

Do not include the PBI or gate log in the artifact. Their identifiers appear only in the PBI Reference fields of the entries.

---

## V-02 — Output Format axis

**Variation axis:** Output format — Handle Ledger committed as the first section of the output artifact, before full entries are written.

**Hypothesis:** C-12 fails when handles are written after entry prose — the handle becomes a label for completed prose rather than an independent citable artifact. The mechanism: require a Handle Ledger section at the top of the artifact, each entry a single line, committed before full entries begin. The one-line form forces the handle to carry meaning independently — if the handle plus one sentence is not sufficient to orient a teammate, the handle is not portable. The portability test is explicit and applied per handle before proceeding. Handles committed in the ledger may be narrowed during entry writing but not replaced wholesale: the committed form is the form that appears in downstream citations.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** It answers one question: what did we learn that we did not expect? It is institutional memory for the next team. It is not a summary of findings. Each surprise entry carries a named handle — a 2-5 word phrase that a future team member can cite without re-reading the entry and be unambiguously understood. The handles are the unit of institutional memory that flows forward into later namespaces.

---

**Step 1 — Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft, review, flow, trace, prove, listen, program, topic). For each artifact, note in one phrase what it was investigating. Internal working memory only.

---

**Step 2 — Identify surprise candidates.**

Scan the signals for findings not predictable from the original design materials. Apply the prediction test per finding:

> "Would a reader of only the pre-investigation design materials — before any signals were gathered — have predicted this?"
>
> YES — confirmation. Route to `topic-story`. Not an echo entry.
> NO — surprise candidate. Carry forward.

Collect at least 2 surprise candidates before proceeding.

---

**Step 3 — Write the Handle Ledger (before full entries).**

For each surprise candidate, commit one line to the Handle Ledger:

```
**[Handle]** — [One sentence: the departure this surprise captures]
```

Rules for handles:
- 2-5 words, capitalized.
- Investigation-specific. The handle must be falsifiable against this topic's signal artifacts — it cannot describe a finding that would appear in any investigation. Test: "Could this handle appear on a different topic's echo with a different sentence?" If yes, it is too generic. Revise until no.
- Apply the portability test before committing: "If a teammate dropped this handle in a message with no further context, would the full team know exactly which surprise?" If the answer is *no* or *maybe* — revise. The test must pass before the handle is committed.

The Handle Ledger is the first section of the output artifact. Write it now. You may narrow handles during full-entry writing (tighter specificity is acceptable). You may not replace the concept: the committed handle is the citation form.

---

**Step 4 — Write full entries (using committed handles).**

For each surprise candidate (minimum 2), write one full entry using the handle from the Handle Ledger:

**[Handle — exactly as committed in Step 3]**

- **Source signal**: Specific artifact name or skill type. Traceable to one artifact, not "the research" or "the signals."
- **Prior assumption**: What was expected before this signal. One sentence. If no explicit assumption existed, state the strongest implicit one the design materials imply.
- **Finding**: What the signal revealed — must oppose or significantly complicate the prior assumption. One sentence.
- **Design impact**: Specific component, flow, or decision affected. Must name something specific. "This affects the design" or "this changes things" do not pass.

---

**Step 5 — Synthesis.**

Do the surprises share a root cause or reveal a common blind spot? Write 2-4 sentences. If two or more surprises reveal the same gap in the original design thinking, name that pattern and state what it implies for the design. If the surprises are independent, say so explicitly.

---

**Step 6 — Forward guidance.**

1-3 sentences for the next team building `{topic}`. Specific to these surprises — not generic advice. Register: "If you are about to build X, know that Y because we found Z."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure (in order):
1. **Handle Ledger** — one line per handle (`**[Handle]** — [one-sentence departure]`)
2. Surprise Entries — full fields, using handles exactly as committed
3. Synthesis
4. Forward Guidance

The Handle Ledger leads the artifact. Its purpose: a downstream artifact (scout:story, program:plan) that needs to cite a surprise can find the portable handle in one section without reading the full entries.

---

## V-03 — Phrasing Register axis

**Variation axis:** Phrasing register — conversational, concrete analogy. PBI requirement framed as a "bet slip" (must be written before the game starts, specific enough to lose). Handle requirement framed as a "Slack citation test" (drop the handle with no context; does your team know which surprise?).

**Hypothesis:** The abstract formulations "prior belief inventory with addressable identifiers" and "portable named handle specific to this investigation" produce bureaucratic compliance — the model produces a PBI section and handles that are structurally present but behaviorally weak: vague priors that cannot lose, handles that are technically investigation-specific but practically inert. The mechanism: replace abstract requirement with concrete analogy that makes the failure mode visceral. A vague bet slip cannot lose; a vague handle cannot travel. The analogy converts a structural check into a lived test the model can apply immediately.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

Here is the frame. Before you read any signal, you are going to write a bet slip. After you read the signals, you will find the places the signals lost your bets — and each one will get a name short enough to text.

---

**The bet slip.** Read only the pre-investigation materials for `{topic}` — the spec, design notes, topic-plan. Do not open signal artifacts.

For each namespace that has signals (scout, draft, review, flow, trace, prove, listen, program), write one numbered bet:

```
PB-01  [scout]    "My bet: ___"
PB-02  [draft]    "My bet: ___"
...
```

A good bet is specific enough to lose. "I bet the flow works fine" cannot lose — it confirms under any outcome. "I bet the scout signals show at least two competitors have not solved throttle visibility" can lose. If a signal comes back and says all three competitors solved it, you lose the bet — and that is a surprise. Write bets that can lose.

Lock the bet slip once it is written. You may not revise it after you open the signal artifacts. Number the bets PB-01, PB-02, etc.

The bet slip is working memory — do not include it in the output artifact.

---

**Read the signals.** Open the signal artifacts from `simulations/{topic}/`. For each namespace, check: did the signals lose any of your bets?

A finding loses a bet if it contradicts or significantly complicates what PB-NN said. A finding confirms a bet if it is what PB-NN predicted — put it in `topic-story`, not here. You need at least 2 findings that lost bets.

---

**For each lost bet (minimum 2), write one entry.**

Start with the name. The name is a 2-5 word handle, capitalized. Here is the test: drop the handle into a message to your team with no other context. Does everyone on the team know exactly which surprise you mean, without clicking any links or reading any docs? "API Complexity" fails — that could be any investigation. "Competitors-Pre-Solved-Throttle" passes — it points to exactly one moment in exactly this investigation. If your handle doesn't pass the drop-in-Slack test, revise it until it does.

For each entry, once the handle is set:

- **Source signal**: Which signal artifact are you talking about? Specific enough that a reader could find it.
- **The bet it lost** (cite by number — PB-01, PB-02...): What did you bet going in? What did the signal actually say? The contrast is the surprise; both sides need to be in the entry.
- **What changes because of it**: Which specific component, flow, or decision in the design must now be revisited? Not "this is important" — name the thing that changes.

---

**After all entries.** Do the surprises cluster? Do multiple signals lose bets in the same direction — against the same assumption, in the same namespace, about the same design blind spot? If so, name the cluster. If they are genuinely independent, say so — that is also information worth passing forward.

**Close with 1-3 sentences for the next team.** Not general advice. Advice specific to which bets did not survive and what the next team should verify before committing to the same assumptions.

---

Write the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

Include: entries (each with bet reference and handle), synthesis, forward guidance. Do not include the bet slip.

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis

**Variation axes:**
- Role sequence: a Registrar pre-role runs before signal reading, producing both the numbered PBI and a Draft Handle List; a Chronicler role reads signals and writes entries
- Lifecycle emphasis: the handover between roles is an explicit checkpoint; handles may be narrowed by the Chronicler but not reinvented

**Hypothesis:** C-11 and C-12 both require artifacts that predate finding-writing. Assigning them to a pre-role (Registrar) enforces pre-commitment structurally — the Registrar cannot read findings because it runs before any signals are opened. The Draft Handle List is particularly valuable: handles drafted before reading are built from expectation, not from finding — they are "what would we call this surprise if namespace X turned out to be wrong?" When the Chronicler reads signals and finds that namespace X was indeed wrong, the handle exists to narrow against a real finding rather than to invent from scratch. The role handover also makes the lifecycle boundary explicit: the Registrar's artifacts are complete before the Chronicler begins, making Phase 0 pre-commitment auditable by design.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`. Two roles execute in sequence. Complete each role fully before beginning the next. Each role has a single output: do not bleed work from one role into the other.

---

**Role 1: Registrar**

The Registrar documents prior state. It runs before any signal artifact is read.

**Read only** the pre-investigation materials for `{topic}`: the spec, design notes, or topic-plan. Do not open any signal artifacts.

Produce two outputs:

**Output A — Prior Belief Inventory (PBI).**

For each namespace that has signals (scout, draft, review, flow, trace, prove, listen, program), write one numbered entry:

```
PB-01  [namespace: ___]  "Before signals, we assumed: ___."
PB-02  [namespace: ___]  "Before signals, we assumed: ___."
...
```

Each belief must be specific enough to be falsifiable. "We expected the flow to function as designed" cannot be overturned — revise until the belief has a concrete, testable prediction. If no explicit assumption existed for a namespace, state the strongest implicit one the design materials support.

**Output B — Draft Handle List.**

For each namespace, draft one handle that would name the surprise *if* the PBI entry for that namespace were overturned by signals:

```
[namespace]  Draft handle if PB-NN is overturned: "___"
```

Handles are 2-5 words, capitalized. These are drafts — built from expectation, not findings. The Chronicler will narrow them against actual signal content but will not replace the concept.

**Registrar handover checkpoint.** Write:
```
Registrar complete.
PBI entries: PB-01 through PB-0N ([N] total)
Draft handles: [N] entries
Chronicler may begin.
```

The PBI and Draft Handle List are execution scaffolding — do not include them in the output artifact.

---

**Role 2: Chronicler**

The Chronicler reads signals and writes the output.

**Receive** the Registrar's PBI and Draft Handle List.

**Gate adjudication.** Read the signal artifacts from `simulations/{topic}/` across all namespaces. For each namespace, compare what the signals revealed against the corresponding PBI entry. For each notable finding, issue a verdict:

> "Does this finding contradict or significantly complicate PB-NN?"
>
> YES → SURPRISE. Note which PB-NN. This finding enters the echo.
> NO → CONFIRMATION. Route to `topic-story`. Not in the echo.

Minimum 2 SURPRISE verdicts. Gate log is execution scaffolding — not in the output artifact.

**Handle narrowing.** For each SURPRISE verdict, take the Draft Handle from Output B. Review it against the actual finding. You may narrow it (increase specificity); you may not replace it with an unrelated concept. Apply the portability test: "Could a teammate cite this handle with no context and be unambiguously understood by the full team?" If not, narrow until yes.

**Entry writing.** For each SURPRISE verdict (minimum 2), using the narrowed handle:

**[Narrowed Handle]**
*From Draft Handle List, narrowed to the actual finding. 2-5 words, capitalized.*

- **Source signal**: Specific artifact name or skill type. Traceable to one artifact.
- **PBI Reference**: `PB-NN — [the prior belief this finding overturns, verbatim or close summary]`. Must cite the identifier from Output A.
- **Finding**: What the signal revealed — must contradict or complicate the referenced PBI entry. One sentence.
- **Design impact**: Specific component, flow, or decision that must change. One sentence. Must name something specific.

**Synthesis.** Do the surprises cluster? Do two or more overturn PBI entries in the same namespace or reveal the same design-level blind spot? Write 2-4 sentences. Name any pattern; state its absence if there is none.

**Forward guidance.** 1-3 sentences for the next team. Register: "If you are about to build X, the beliefs we held about Y (PB-NN) did not survive contact with Z — before you commit, verify ___."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure:
1. Surprise Entries — each with PBI Reference field citing an identifier from Output A
2. Synthesis
3. Forward Guidance

Do not include the PBI, Draft Handle List, or gate log. Their identifiers appear only in PBI Reference fields.

---

## V-05 — Combination: Lifecycle Emphasis + Output Format

**Variation axes:**
- Lifecycle emphasis: Phase 0 PBI production with numbered identifiers, structurally locked before Phase 1; phase boundary is an explicit checkpoint
- Output format: Handle Ledger committed as first output section at Phase 2, before full entries are written; handles committed before entry prose cannot be retroactively reconstructed from that prose

**Hypothesis:** C-11 and C-12 each require a different pre-commitment at a different moment in the production sequence. C-11 requires a frozen belief set *before signal reading* (Phase 0). C-12 requires frozen handles *before entry prose* (Phase 2). The combination assigns each pre-commitment to a structurally distinct phase, ensuring neither crowds the other out. The phase sequence is: lock beliefs → read signals → lock handles → write entries — four distinct operations, each with its own checkpoint. A fully-passing artifact has two pre-committed sections (PBI identifiers referenced in entries; Handle Ledger leading the artifact) that prove both criteria were satisfied structurally, not reconstructed.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`. Execute phases in order. Each phase has one output. Do not begin the next phase until the current phase output is complete.

---

**What the echo is.** It answers one question: what did we learn that we did not expect? It is institutional memory for the next team. It is not a summary of findings. Two structural requirements make this echo auditable and citable: (1) each surprise is traced to a numbered prior belief that was documented *before* signals were read; (2) each surprise carries a portable named handle committed *before* its full entry was written. Both requirements exist because post-hoc priors and post-hoc handles are indistinguishable from invented ones — the phase structure is the proof.

---

**Phase 0 — Prior Belief Inventory (before reading any signal).**

Read only the pre-investigation materials for `{topic}`: the spec, design notes, or topic-plan. Do not open signal artifacts.

For each namespace that has signals (scout, draft, review, flow, trace, prove, listen, program), write one labeled entry:

```
PB-01  [namespace: scout]   "Before signals, we assumed: ___."
PB-02  [namespace: draft]   "Before signals, we assumed: ___."
...
```

Each entry must be specific enough to be falsifiable — a belief that confirms under any outcome provides no gate leverage. If no explicit assumption existed, state the strongest implicit one the design materials support.

**Phase 0 checkpoint.** Write: "PBI frozen: PB-01 through PB-0N. Proceeding to Phase 1."

After this checkpoint, the PBI is locked. No additions or revisions. The PBI is execution scaffolding — not included in the output artifact, but its identifiers will be cited in Phase 3 entries.

---

**Phase 1 — Signal Reading + Gate.**

Read all signal artifacts from `simulations/{topic}/` across namespaces. For each notable finding, apply the gate against the PBI:

> "Does this finding contradict or significantly complicate a specific PBI entry?"
>
> YES — note which PB-NN. Verdict: SURPRISE.
> NO — Verdict: CONFIRMATION. Route to `topic-story`.

Issue a verdict for every notable finding. Minimum 2 SURPRISE verdicts required. Gate log is execution scaffolding — not in the output artifact.

**Phase 1 checkpoint.** Write: "Gate complete. [N] SURPRISE verdicts (PB-NN: ...), [M] CONFIRMATION verdicts. Proceeding to Phase 2."

---

**Phase 2 — Handle Ledger (committed before full entries).**

For each SURPRISE verdict, commit one line to the Handle Ledger:

```
**[Handle]** — [One sentence: the departure this surprise captures]
```

Handle rules:
- 2-5 words, capitalized.
- Investigation-specific. The handle must point to exactly this finding in this investigation. Test: "Would this handle appear on a different topic's echo?" YES — too generic, revise. "Would a teammate citing this handle with no context be unambiguously understood?" NO — too vague, revise.
- Both tests must pass before the handle is committed.

**Phase 2 checkpoint.** Write: "Handle Ledger committed: [N] handles. Proceeding to Phase 3."

The Handle Ledger is the first section of the output artifact. Handles committed here may be narrowed during entry writing; they may not be replaced.

---

**Phase 3 — Surprise Entries.**

For each SURPRISE verdict (minimum 2), write one full entry using the committed handle and the PBI identifier:

**[Handle — exactly as committed in Phase 2]**

- **Source signal**: Specific artifact name or skill type. Traceable to one artifact.
- **PBI Reference**: `PB-NN — [the prior belief this finding overturns, verbatim or close summary of Phase 0 entry]`. Must cite the identifier.
- **Finding**: What the signal actually revealed — must contradict or complicate PB-NN. One sentence.
- **Design impact**: Specific component, flow, or decision that must change. One sentence. Must name something specific — "this affects the design" does not pass.

---

**Phase 4 — Synthesis.**

Examine the set of named surprises. Write 2-4 sentences: do two or more surprises overturn PBI entries in the same namespace or reveal the same gap in the original design thinking? If yes, name the pattern and state its design implication. If the surprises are genuinely independent, state that explicitly.

---

**Phase 5 — Forward Guidance.**

1-3 sentences for the next team building `{topic}`. Must be derivable only from these surprises. Register: "If you are about to build X, the beliefs we held about Y (PB-NN, PB-NN) did not survive — before you commit, verify Z."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.

Artifact structure (in order):
1. **Handle Ledger** (Phase 2) — one line per handle with departure summary; this section leads the artifact
2. Surprise Entries (Phase 3) — each with PBI Reference citing a Phase 0 identifier
3. Synthesis (Phase 4)
4. Forward Guidance (Phase 5)

Execution scaffolding omitted from artifact: Phase 0 PBI, Phase 1 gate log, Phase 0/1/2 checkpoints.
