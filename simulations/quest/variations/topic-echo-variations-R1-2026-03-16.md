Now I have full context on the rubric v1, the R1 (2026-03-15) variations (V-01 through V-05), and the trajectory the rubric took in later rounds. This is a clean Round 1 against the freshly written v1 rubric (2026-03-16). The prior R1 explored: rigid form (output format), conversational first-person (phrasing register), explicit phases + surprise gate (lifecycle emphasis), Skeptic/Author roles + table (role sequence + output format), and anti-pattern naming (inertia framing + phrasing register).

I'll cover different ground: Historian-first role sequence (C-01/C-04 protection), narrative prose output (C-02/C-05 stress test), extended inertia contrast (C-04 hardening), compressed lifecycle + Challenger mid-pass (C-01/C-04 via structure), and forensic register (C-06/C-07 via voice).

---

# Variations: `topic:echo` — Round 1

**Rubric:** v1 | **Date:** 2026-03-16

---

## Design Context

v1 rubric introduces ten criteria against a two-sentence skill definition: synthesize surprises, not findings; trace each to a source; assess design impact; address the next team. The key structural risks for a Round 1 prompt are:

- **C-01/C-04 boundary collapse** — the most common failure: findings dressed as surprises, or a summary section that contains some labeled surprises. The constraint must be enforced at generation time, not as a post-hoc check.
- **C-06 omission** — the "expected X; found Y" counterfactual is easy to imply but hard to satisfy structurally; prompts that ask for "what the signal revealed" without explicitly requiring the prior-state half will produce C-06 failures.
- **C-07 drift** — institutional framing (addressed to a future team) competes with the natural pull toward retrospective address ("we found..."). Prompts that describe the purpose without changing the addressee register will produce C-07 partials.

**R1 variation plan — three single-axis, two combined:**

| Variation | Primary axis | Hypothesis |
|-----------|-------------|------------|
| V-01 | Role sequence (Historian-first) | Running a Historian role to reconstruct prior assumptions *before* signal reading prevents post-hoc rationalization of what "we assumed," hardening C-01 and C-06 simultaneously |
| V-02 | Output format (narrative prose, inline citation) | Numbered paragraph entries without labeled fields stress-test C-02 and C-05 by removing structural scaffolding; surprises must earn their presence in prose |
| V-03 | Inertia framing (extended contrast portrait) | An extended, concrete portrait of the story artifact — what it contains, what it omits, why it cannot substitute — makes the C-04 boundary vivid before any instruction begins |
| V-04 | Lifecycle emphasis + role sequence | A two-pass lifecycle with an explicit Challenger role in Pass 1 (single-question filter) and an Author role in Pass 2 enforces C-01/C-04 structurally through I/O boundaries rather than prose instruction |
| V-05 | Phrasing register + inertia framing | Forensic/institutional register ("the investigation revealed a departure") with explicit status-quo contrast shifts the addressee register to future-team naturally, hardening C-07 without a dedicated instruction |

**Discriminating pairs:**
- V-01 vs V-04: isolates whether the Historian role adds value independent of lifecycle structure
- V-02 vs V-01: isolates whether structural form (V-01's labeled fields) does work that prose cannot replicate
- V-03 vs V-05: isolates whether contrast is better delivered as extended portrait (V-03) or embedded in register (V-05)
- V-04 vs V-05: isolates whether role structure or phrasing register is more reliable for C-04 enforcement

---

## V-01 — Role Sequence: Historian-First

**Variation axis:** Role sequence — Historian role runs before signal reading.

**Hypothesis:** The canonical failure mode for C-01 and C-06 is post-hoc rationalization: the author reads the signals, identifies interesting findings, then retrofits a "prior assumption" to make them look like surprises. A Historian role that reconstructs the prior-state belief set *before* signal reading eliminates this failure path. The Historian cannot have seen the signal outputs, so the prior assumptions it produces are genuinely pre-investigation. The Author in Role 2 then tests each signal finding against the Historian's frozen record — surprise is the delta, not a label.

---

### Prompt Body

You are executing `topic:echo` for `{topic}`. Two roles run in strict sequence. Role 1 completes fully before Role 2 begins.

---

**Role 1 — Historian**

Your job is to reconstruct what the team believed *before* the investigation began. You are not reading signal outputs yet. You are reading design materials only.

Read the following, in this order:
1. The original topic brief or spec for `{topic}` from `simulations/TOPICS.md` or any spec artifact present.
2. Any draft or proposal artifacts in `simulations/{topic}/` dated before the first signal artifact.
3. The original design intent as stated in the plugin plan or design documents, if referenced in the topic artifacts.

From these materials only, produce a **Prior Belief Inventory** — a numbered list of assumptions the team held before any signal was gathered. Each entry is one sentence. Format:

> **PB-N.** The team assumed that `{assumption}`.

Apply this threshold: if the assumption is not traceable to the pre-investigation materials, do not include it. Inferred assumptions are permitted if they are the obvious implication of stated design decisions — but mark them with `(inferred)`.

Minimum 3 entries. This inventory is working memory — do not include it in the output artifact. But do not discard it; Role 2 reads it.

---

**Role 2 — Author**

Read the signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft, review, flow, trace, prove, listen, program). You have access to the Prior Belief Inventory from Role 1.

For each signal artifact, identify findings. Then test each finding against the Prior Belief Inventory:

> **Surprise test:** Does this finding contradict, complicate, or substantially extend any entry in the Prior Belief Inventory? If yes, it is a surprise candidate. If no — if the finding confirms or is silent on all PB entries — it is a confirmation. Do not include confirmations in the output.

For each surprise candidate (minimum 2), write one entry:

---

**[Surprise Name]** *(2-5 words, capitalized, reusable as a citation)*

**Source signal:** `{artifact name or skill namespace}` — specific enough to locate.

**Prior belief (from Historian):** `{the specific PB entry this finding contradicts — quote or paraphrase the PB entry by number}`

**Finding:** `{what the signal actually revealed — one sentence, written as a direct departure from the prior belief}`

**Design impact:** `{the specific component, flow, or decision this finding requires to change — one sentence. Must name what changes, not only that something changes.}`

---

After all entries:

**Pattern synthesis** (2-4 sentences): Do two or more surprises share a root cause or reveal the same blind spot in the Prior Belief Inventory? If yes, name the pattern and its implication for the design. If no, state this explicitly — absence of pattern means the surprises are independent.

**Forward guidance** (1-3 sentences): Addressed explicitly to the next team building `{topic}`. Write as: "Before you commit to `{design decision}`, know that `{surprise-derived warning}`." Derive each statement from a named surprise — no generic advice.

Write the output artifact to `simulations/{topic}/{topic}-echo-{date}.md`. Include: surprise entries, pattern synthesis, forward guidance. Do not include the Prior Belief Inventory or Skeptic log.

---

## V-02 — Output Format: Narrative Prose with Inline Citation

**Variation axis:** Output format — numbered paragraph entries, no labeled fields, inline attribution.

**Hypothesis:** Labeled-field forms (Source Signal / Prior Assumption / Finding / Design Impact) reduce C-02 and C-05 failures by making omissions structurally visible. But they also create a compliance path: an author can fill all fields without the entries cohering as genuine surprises. A narrative prose format removes the scaffolding and forces integration — the surprise name, the attribution, the counterfactual, and the design impact must all appear naturally within a short paragraph. This tests whether the rubric criteria are strong enough to survive without structural scaffolding, and which criteria are genuinely prompt-enforceable in prose.

---

### Prompt Body

You are writing `topic:echo` for `{topic}`.

The echo answers one question: what did we learn that we did not expect? Its output is institutional memory for the next team that works on this topic. It is not a summary. It is not a set of findings. Every entry must be a surprise — a place where reality departed from prediction.

**Preparation.** Read the signal artifacts from `simulations/{topic}/` across all namespaces. For each signal, note silently: what was this signal investigating? Do not write this down.

**Candidate filter.** For each notable finding in the signals, apply one test: would a person who had read only the pre-investigation design materials for `{topic}` — with no signal outputs, no interviews, no experiments — have expected this finding? If yes, it is a confirmation and does not belong here. If no, carry it forward as a surprise candidate.

**Write the surprises.** For each candidate that survives the filter (minimum 2), write one numbered paragraph. Each paragraph must contain, in natural prose:

- The surprise's **name** — a distinct 2-5 word handle introduced in the first sentence. This name must be reusable: a teammate should be able to cite it by name without explanation. Set it in bold when first introduced.
- The **source** — which signal artifact or namespace produced this finding. Name it explicitly, not as "the research" or "the evidence." (e.g., "the `prove-interview` artifact for `{topic}`" or "the `flow-resilience` signal").
- The **counterfactual** — what was expected going in, and what was actually found. Both halves must be stated. A reader who was not on the team must be able to reconstruct the prior assumption from this paragraph alone.
- The **design impact** — which specific component, flow, or decision this surprise affects and how. One sentence minimum. "This matters for the design" is not sufficient — name what specifically changes.

Each paragraph should run 4-6 sentences. Longer is not better. Every sentence must earn its place.

**Cross-signal synthesis.** After the numbered entries, write one short paragraph (3-5 sentences). Look across the surprises: do they share a root cause? Reveal the same blind spot? Point to a systemic assumption the design made that the signals collectively undermined? If the surprises are genuinely independent, say so — that conclusion is also worth stating. Name any pattern you see, or name its absence.

**Forward guidance.** End with a single short paragraph addressed directly to the next team. Open with "If you are building `{topic}`..." and derive the guidance from the named surprises. The guidance must be specific enough to be actionable — a future team should be able to read this paragraph and make a different decision than the current team would have made without it.

Write the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-03 — Inertia Framing: Extended Contrast Portrait

**Variation axis:** Inertia framing — the status-quo output (`topic-story`) is described in concrete detail before any instruction begins.

**Hypothesis:** The C-04 boundary (synthesis not summary) is the most frequently collapsed criterion because the summary is the natural output of investigating a topic. Instruction to "not summarize" is insufficient because the author does not recognize their summary as a summary. What works is a detailed, concrete portrait of what a summary looks like — its sections, its moves, its characteristic framing — followed by an equally concrete portrait of what an echo looks like. When both artifacts are described in parallel, the author can perform a structural comparison during generation and self-correct before writing.

---

### Prompt Body

You are writing `topic:echo` for `{topic}`.

---

**The artifact you are NOT producing.**

After a topic investigation, the natural output is a synthesis document. It might be called a summary, a findings report, or a story. It is organized around what was learned. It has sections like "Key Findings," "What the Signals Show," or "Recommendation." It covers all signal outputs. It is coherent, comprehensive, and useful to someone who wants to understand the investigation's conclusions.

That artifact exists. It is `topic-story`. If it has not been written yet, it should be written separately. It is not what you are writing now.

Here is what `topic-story` looks like in practice:

- It enumerates findings across signals, organized by theme or by signal type.
- It synthesizes conclusions: "across three signals, we found that X."
- It may have a section called "Surprises" or "Unexpected Findings" — but that section is a labeled subset of the findings, not a structurally distinct artifact.
- A reader can summarize it as: "Here is what the team learned about `{topic}`."

This is precisely what `topic-echo` does not look like.

---

**The artifact you ARE producing.**

The echo is not a subset of `topic-story`. It is a different artifact with a different purpose and a different reader.

Its one question: **what did we learn that we did not expect?**

Here is what `topic:echo` looks like in practice:

- Every entry is a surprise. Not a finding labeled "surprising." A genuine departure from a prior assumption — something that would not have been predicted from the pre-investigation design materials alone.
- Each entry names the source signal that produced the surprise. Not "the evidence" — the specific artifact. A future team should be able to go read that artifact and verify the surprise.
- Each entry states what was assumed before and what was actually found. Both. The contrast is not reconstructable from context — it is written out.
- Each entry names which design decision the surprise affects and how.
- The artifact closes with a note to the next team: what they should know before they start, given what surprised this team.

A reader of `topic-echo` should be able to say: "Here is what the team did not see coming."

---

**Execution.**

**Step 1 — Inventory.** Read signal artifacts from `simulations/{topic}/` across all namespaces. For each, note silently: what was it investigating?

**Step 2 — Filter.** For each finding worth noting, ask: would a person reading only the pre-investigation design materials have predicted this? If yes, it belongs in `topic-story`, not here. Discard it.

**Step 3 — Name the survivors.** Each surprise that passes the filter gets a name: a distinct 2-5 word handle, capitalized, reusable as a citation. Not "Finding 3." Something a colleague could say aloud: "The Silent Adopter Problem," "The Cascade Inversion," "The False Baseline."

**Step 4 — Document each surprise.** Minimum 2 entries. For each:

- **Name** (from Step 3)
- **Source signal** — the artifact name or skill namespace. Specific enough to locate.
- **Prior assumption** — what the team believed before this signal. One sentence. If there was no explicit assumption, state the implicit one the design was relying on.
- **Finding** — what the signal actually revealed. Must be in opposition to the prior assumption. One sentence.
- **Design impact** — the specific component, flow, or decision that must now change. One sentence. "This is important" is not design impact — name what changes.

**Step 5 — Synthesize.** Do two or more surprises share a root cause or reveal the same blind spot? Name the pattern if one exists. State its absence if there is none.

**Step 6 — Address the next team.** Write 1-3 sentences of forward-looking guidance. Specific to these surprises only. Generic advice does not belong here.

**Write** the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-04 — Combination: Lifecycle Emphasis + Role Sequence

**Variation axes:** Lifecycle emphasis (explicit I/O boundaries per phase) + Role sequence (Challenger role mid-pass).

**Hypothesis:** Prose instruction for C-01/C-04 fails when it is read once at the start of generation and not consulted again. A two-pass lifecycle with explicit I/O contracts at each boundary turns the anti-pattern check from a pre-flight warning into a structural gate. The Challenger role in Pass 1 has one job — output a list of PASS/FAIL rulings on surprise candidates — and its output is the only legal input to Pass 2. This creates an audit trail: if a non-surprise appears in the final artifact, it must have been either produced by the Challenger (a Challenger error, diagnosable) or introduced by the Author without a Challenger approval (a structural violation, detectable). The lifecycle structure makes both failure modes visible.

---

### Prompt Body

You are executing `topic:echo` for `{topic}`. The execution runs in two passes with explicit I/O contracts. Complete Pass 1 fully before beginning Pass 2.

---

### Pass 1 — Challenger

**INPUT:** Signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft, review, flow, trace, prove, listen, program). Pre-investigation design materials if available (spec, topic brief, proposal).

**TASK:** Produce a Surprise Ruling List — a ruling for every finding you examine.

For each signal artifact, identify any findings worth considering. For each finding, apply the surprise gate:

> "Would a person who had read only the pre-investigation design materials for `{topic}` — with no signal outputs — have predicted this finding?"

Produce one ruling per finding examined:

| Candidate | Source Signal | Gate Question Answer | Ruling | Reason (1 sentence) |
|-----------|--------------|---------------------|--------|----------------------|
| `{2-5 word name}` | `{artifact or namespace}` | YES / NO | CONFIRMED / SURPRISE | `{why}` |

Rules:
- If the gate answer is YES → CONFIRMED. This finding validates the design. It belongs in `topic-story`. Do not carry it to Pass 2.
- If the gate answer is NO → SURPRISE. This finding contradicts, complicates, or substantially extends the design assumptions. Carry it to Pass 2.
- If you are uncertain: default to CONFIRMED and explain why. False confirmations are less damaging than false surprises.

**OUTPUT:** The Surprise Ruling List. Minimum 2 SURPRISE rulings. Maximum: no limit, but every SURPRISE ruling must be defensible. The Ruling List is execution scaffolding — do not include it in the output artifact.

---

### Pass 2 — Author

**INPUT:** Only findings with SURPRISE rulings from the Challenger. You may not include findings that were not Challenger-approved.

**TASK:** For each SURPRISE candidate, produce one entry in the following form.

---

**[Surprise Name]** *(the name from the Challenger ruling — modify only if the Challenger's name is not reusable as a citation)*

**Source signal:** `{artifact name or skill namespace from Challenger ruling}`

**Prior assumption:** `{what the team assumed or expected before this signal — one sentence. If the Challenger ruling named an implicit assumption, state it here explicitly.}`

**Finding:** `{what the signal actually revealed — one sentence, written as a direct departure from Prior Assumption}`

**Design impact:** `{the specific component, flow, or decision this surprise requires to change — one sentence. Name what changes.}`

---

After all entries:

**Pattern synthesis** (2-4 sentences): Do two or more of the Challenger-approved surprises share a root cause or reveal the same blind spot? Name any pattern and its implication. If no pattern exists, say so explicitly.

**Forward guidance** (1-3 sentences): Addressed to the next team building `{topic}`. Derive from named surprises only. Format: "If you are about to commit to `{decision}`, know that `{surprise-derived warning}`."

**OUTPUT:** Surprise entries + Pattern synthesis + Forward guidance, written to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-05 — Combination: Phrasing Register + Inertia Framing

**Variation axes:** Phrasing register (forensic/institutional, third-person, declarative) + Inertia framing (status-quo named as a class of artifacts with a specific failure signature).

**Hypothesis:** The natural register for an echo prompt is imperative and first-person ("find the surprises," "write each one"). This register produces retrospective address ("we found," "the team learned"), which fights C-07 (institutional framing). A forensic register — third-person, declarative, treating the investigation as an event to be documented — shifts the addressee naturally to a future reader without requiring a dedicated instruction. The artifact reads as a deposition, not a diary entry. Combined with precise inertia framing that names the status-quo artifact class ("survey documents") and describes its distinguishing signature, the C-04 boundary becomes a typological distinction rather than a behavioral instruction.

---

### Prompt Body

You are producing a `topic-echo` artifact for the topic `{topic}`.

---

**Artifact class context.**

Two artifact classes are produced at the conclusion of a signal investigation. Distinguishing them is the precondition for producing either correctly.

**Class A — Survey documents.** A survey document compiles and synthesizes the findings of an investigation. It is organized around what was learned. Its characteristic moves are: enumerate findings by theme, assess signal consistency, synthesize a recommendation. Survey documents are complete accounts of investigation outcomes. They serve readers who were not present for the investigation. The `topic-story` artifact is a survey document.

**Class B — Departure records.** A departure record documents the places where the investigation diverged from prior expectation. It is organized around what was unanticipated. Its characteristic moves are: name each departure, identify its source, state the prior assumption it overturned, assess its consequence for the design. Departure records serve future investigators — teams that will undertake similar work and benefit from knowing where prior assumptions failed. The `topic-echo` artifact is a departure record.

The failure mode common to `topic-echo` production is class substitution: a survey document is produced under the `topic-echo` artifact name. This occurs when findings are enumerated without a prior-assumption test, when the departure structure is applied superficially (items are labeled "surprising" without the prior state being named), or when the document's organizing principle is "what was learned" rather than "what departed from expectation."

The artifact you are producing is a departure record. Every entry must satisfy the departure structure. Survey-document entries do not belong here; they belong in `topic-story`.

---

**Execution procedure.**

**1. Signal review.** Read the signal artifacts from `simulations/{topic}/` across all namespaces. For each artifact, note silently: what was the investigation seeking to determine?

**2. Departure identification.** For each finding worth noting, apply the prior-assumption test: would a reader of only the pre-investigation design materials for `{topic}` have predicted this finding? A finding that passes this test is a confirmation — it is appropriately documented in `topic-story`. A finding that fails this test is a departure — it qualifies for inclusion in this artifact. Minimum 2 departures must be identified.

**3. Departure documentation.** For each identified departure, produce one entry. Required fields:

- **Departure name** — a 2-5 word designation, title-cased, suitable for citation by future teams. The name must be specific enough that two readers would agree on what finding it refers to.
- **Source signal** — the artifact or skill namespace from which the departure was derived. The designation must be sufficient to locate the source artifact.
- **Prior assumption** — the expectation or design premise that the finding overturned. Stated as a claim the pre-investigation materials would have supported.
- **Observed finding** — what the signal actually revealed, stated as a direct departure from the prior assumption.
- **Design consequence** — the specific component, flow, or decision that the departure bears upon, and in what direction. Generic impact statements ("this affects the design") do not qualify — the consequence must identify a specific decision node.

**4. Cross-departure analysis.** Examine the set of documented departures. Determine whether two or more departures share a common origin — a belief structure that the pre-investigation materials embedded, which multiple signals then contradicted. If a shared origin exists, name it. If departures are independent, state this finding explicitly. The cross-departure analysis belongs in the artifact.

**5. Forward implication.** Produce 1-3 sentences addressed to the team that will next undertake work on `{topic}`. The sentences must be derivable only from the documented departures — they must name findings specific to this investigation, not generic investigation advice. The forward implication belongs in the artifact as its concluding section.

**6. Artifact production.** Write the completed artifact — departure entries, cross-departure analysis, forward implication — to `simulations/{topic}/{topic}-echo-{date}.md`.

---

*Written against rubric v1 | 2026-03-16*
