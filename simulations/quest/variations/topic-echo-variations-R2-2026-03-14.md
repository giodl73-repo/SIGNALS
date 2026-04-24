Written to `simulations/quest/variations/topic-echo-variations-R2-2026-03-14.md`.

---

## topic-echo — Variations R2

| # | Axis | Target | Hypothesis |
|---|------|--------|-----------|
| **V-01** | Counterfactual as primary culling gate | C-10 | Making the inertia test the *inclusion criterion* — not a schema field — forces every surprise to justify why active sensing was required, not just that it was unexpected |
| **V-02** | Per-surprise word budget (120 words max) | C-11 | Document-level ceilings allow lopsided items to pass; item-level ceilings force synthesis inside each surprise, where transcription actually happens |
| **V-03** | Prohibited-language list | C-12 | Naming forbidden hedging constructs directly targets the mechanism without requiring a persona — tests whether explicit prohibition outperforms V-05's implicit identity framing |
| **V-04** | Counterfactual gate + Anti-hedging | C-10 + C-12 | The two criteria are naturally coupled — strong enough signals to pass the counterfactual test are strong enough to state as claims; tests mutual reinforcement |
| **V-05** | Per-surprise budget + Claim-first structure | C-11 + C-12 | Inverting the structure (claim before evidence) commits the author to a position before hedging is possible; 120-word cap leaves no room to walk it back |

---

### Design rationale

**Why R1's top variations don't satisfy R2's targets**: V-03 (R1) and V-05 (R1) both scored 100/100 but produced C-10/C-11/C-12 as *side effects* — the 800-word ceiling emerged from V-03's conversational brevity, authoritative voice emerged from V-05's persona. R2 tests whether *direct enforcement* (gate, per-item cap, prohibited list) outperforms emergent enforcement.

**Key structural bet in V-05**: The claim-first inversion (`Claim -> Source -> Expected -> Impact` instead of `Source -> Expected -> Found -> Impact`) makes hedging harder because the author commits to the finding before citing evidence. Evidence becomes support for a position, not the source of a tentative observation. This is the novel mechanism in R2 — no R1 variation tried it.
ncation and structural weaknesses. V-01 isolates and escalates: rather than asking the inertia question as a schema field, it makes that question the gating criterion for inclusion. A surprise does not pass because it was unexpected — it passes because a passive team would not have found it.

**C-11 strategy for R2**: V-03's 800-word ceiling operated at the document level. V-02 operates at the item level. The failure mode for document-level ceilings: one 300-word surprise paired with four 100-word items still passes. Per-item ceilings force synthesis where it matters — inside each surprise.

**C-12 strategy for R2**: V-05's Echo Archaeologist produced authoritative voice through identity (a named expert commits to claims). V-03 achieves the same end through prohibition (a list of banned hedging constructs). Testing whether explicit prohibition outperforms implicit identity framing for voice discipline.

**V-04 and V-05 as combination bets**: C-10 and C-12 are naturally coupled — a surprise that passes the counterfactual test has strong enough signals behind it to assert as a claim. V-04 tests whether combining the two creates mutual reinforcement. V-05 tests a structural mechanism: inverting claim before evidence forces commitment before hedging is possible, and a 120-word cap leaves no room to walk it back.

---

## V-01 — Single axis: Counterfactual as primary culling gate

**Axis**: The inertia test ("would a team doing nothing have discovered this?") replaces the standard surprise filter as the primary inclusion criterion. A surprise does not earn its place merely by being unexpected — it earns its place by requiring active signal-gathering to surface.

**Hypothesis**: Elevating the counterfactual from a schema field to a gate forces the author to reason about what the investigation actually produced, not just what was surprising. This is the sharpest form of C-10 and should also strengthen C-04 because surprises that justify active sensing tend to have direct design consequences.

---

You are running `/topic:echo` for topic `{topic}`.

The echo asks one question: **"What did we learn that we didn't expect?"**

Not a summary. Not a status update. A synthesis of surprises that only active signal-gathering could have surfaced — things that would not have appeared in a planning document, a kickoff review, or normal development feedback.

---

### The primary test

Every candidate surprise must pass this before it enters the echo:

> **Would a team that skipped all signal-gathering — that relied only on the initial strategy, standard planning, and normal development feedback — have eventually discovered this?**

- **No** — the discovery required active sensing to surface: the surprise belongs in the echo.
- **Yes** — a reasonable team would have found this through ordinary work: drop it. It is not evidence that gathering signals was worth doing.

This is stricter than "was it unexpected?" Teams can be surprised by things they would have found anyway. The echo is not about surprises in general — it is about what the investigation specifically made visible.

---

### Step 1 — Read all signals

Glob and read every artifact:
- `simulations/{topic}/` — strategy, story, prior echoes
- `simulations/{topic}/**/{topic}-*-{date}.md` — all namespace artifacts

As you read, note candidate surprises. For each, apply the primary test immediately: could a passive team have discovered this without running these signals? Record the verdict. Do not write yet.

---

### Step 2 — Cull with the primary test

From your candidates:
1. Fail anything that passes the primary test (a passive team would have found it).
2. Fail anything that confirms what was expected going in.
3. Fail anything you cannot trace to a named source signal.
4. Keep 3–6 surprises. Fewer strong items beat a longer list of weak ones.

---

### Step 3 — Name each surviving surprise

For every item that passed the cull, assign a **named label** — a specific phrase that crystallizes the insight for a future reader. Not "Finding 1." Not "Surprise A." Something content-specific and memorable: "The Phantom Dependency," "Compliance Unlocks Adoption," "The Inverted Adoption Curve." If the name could describe a finding from a different project, it is not specific enough.

---

### Step 4 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise uses this structure:

```markdown
## {Named Label}
**Source**: {namespace/skill — e.g., "scout/feasibility", "prove/interview Round 2"}
**Expected**: {what the team assumed before this signal existed}
**Found**: {what the signal actually revealed}
**Design impact**: {how this changes, challenges, or confirms the design direction — explicit, not implied}
**Why active sensing was required**: {what specific signal or method surfaced this, and why it would not have appeared through planning or normal feedback alone}
```

---

### Step 5 — Quality checks

Before closing:
- [ ] Every surprise fails the primary test — no passive team would have found it
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Why active sensing was required" cell is populated — not "N/A"
- [ ] At least one surprise is synthesized across two or more signals
- [ ] Surprises span at least three distinct namespaces
- [ ] Add a **Patterns** section if two or more surprises share a root cause

If any check fails, revise before outputting the artifact.

---

The echo is institutional memory. The next team that investigates this path will read it before they start. They will use it to understand not just what the signals found, but why the investigation was worth running.

---

## V-02 — Single axis: Per-surprise word budget (120 words maximum)

**Axis**: A hard word cap enforced at the individual surprise level — not just the total document. Each surprise body (not the label) must be 120 words or fewer.

**Hypothesis**: Document-level ceilings allow uneven distribution — one 300-word surprise paired with four 100-word items still passes. Per-item ceilings force synthesis where it matters: inside each surprise. The author cannot transcribe the finding; they must state the conclusion. This is the discipline that distinguishes an echo from a summary.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — named, sourced, and stated with impact.

---

### The budget rule

**Each surprise body is capped at 120 words** (not counting the `##` label line).

This is not a soft guideline. It is the mechanism that separates synthesis from transcription.

If you cannot state a surprise in 120 words — source, expectation, finding, and design impact — you have not synthesized it. You are still describing it. Stop, find the one thing the surprise actually claims, and write that.

What 120 words forces you to do:
- Decide what the surprise is claiming, then state the claim directly.
- Drop the setup, background context, hedged qualifications.
- Name the signal, not describe its contents.

The full echo (3–6 surprises) should come in under 800 words total. Readable end-to-end in under ten minutes by someone who was not on the team.

---

### Step 1 — Read all signals

Glob `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`. Read every artifact. Note anything that contradicts or significantly extends the initial strategy. Do not write yet.

---

### Step 2 — Cull

- Drop anything that confirms what was expected. Only surprises belong.
- Drop anything you cannot trace to a named source signal.
- Drop anything that could appear unchanged in a standard research summary.
- Keep 3–6 items.

---

### Step 3 — Name before you write

Assign a **specific named label** to each surprise before writing its body. The name must be content-specific and memorable. "The Missing Middle" passes. "Finding 2" fails. If the name could apply to a different project, it is not specific enough.

---

### Step 4 — Write within budget

`simulations/{topic}/{topic}-echo-{date}.md`

For each surprise:

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {what the team assumed going in}
**Found**: {what the signal revealed}
**Design impact**: {how this changes, challenges, or confirms the direction}
```

**After writing each surprise**: count the words in the body (everything from `**Source**` through the end of `**Design impact**`). If the count exceeds 120, cut until you have a claim, not a description.

---

### Step 5 — Quality checks

- [ ] Each surprise body is at or under 120 words
- [ ] Total document is at or under 800 words (excluding headers)
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated — if blank, the contrast is missing
- [ ] At least one surprise synthesizes two or more signals — cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add a **Patterns** section if two or more surprises share a root cause

If any budget check fails, revise that surprise before moving to the next.

---

## V-03 — Single axis: Anti-hedging enforcement (prohibited language)

**Axis**: An explicit list of prohibited hedging constructs, with a diagnostic for why hedging appears and how to eliminate it. Every surprise is stated as a claim the author stands behind.

**Hypothesis**: V-05's Echo Archaeologist persona produced authoritative voice as a side effect of the identity frame. Direct prohibition targets the same behavior without the persona — by naming the specific constructs that produce hedged output and instructing the author to rewrite them as assertions. If prohibition works as well as identity framing, it is a simpler and more portable mechanism for C-12.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — stated as the claims they are.

---

### The voice rule

Before you write a single word of the artifact: **the echo makes claims, not observations**.

Every surprise in the echo is a statement the author stands behind. A future reader should be able to quote any item and say "the team found X" — not "the team thought they might have found something that suggested X."

**Prohibited language** — these constructs are banned from all surprise entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "we think" | remove — state the finding |
| "suggests that" | state the claim directly |
| "arguably" | remove — state the finding |
| "may want to" | "should" |

**Diagnostic** — if you find yourself reaching for hedging language, one of three things is true:
1. You don't actually believe the surprise is real — drop it.
2. You don't have enough signal to support it — trace back to the source.
3. You are transcribing uncertainty from the source artifact instead of synthesizing a conclusion — form the conclusion, then write it as a claim.

An echo is not a log of signal contents. It is the author's judgment about what the signals reveal.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`. Note what contradicts or significantly extends the initial strategy. For each candidate, decide: do you believe this is true? If yes, commit to stating it as a claim.

---

### Step 2 — Cull

- Drop anything that confirms what was expected.
- Drop anything you cannot trace to a named source signal.
- Drop anything that could appear unchanged in a standard research summary.
- Keep 3–6 surprises.

---

### Step 3 — Name each surprise

Assign a specific named label before writing the body. Content-specific. Memorable. Not generic.

---

### Step 4 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {stated as a claim: "We assumed X" — not "teams may have assumed X"}
**Found**: {stated as a claim: "X is false / Y replaces Z / the constraint is W" — not "it seems X might be the case"}
**Design impact**: {stated as a claim: "This changes / confirms / invalidates..." — not "this may suggest a change"}
```

---

### Step 5 — Anti-hedging pass

Before outputting the artifact:
1. Scan every body paragraph for prohibited constructs.
2. For each occurrence: rewrite as a claim, or drop the item if you cannot assert it.
3. Read each `**Found**` field aloud as a statement of fact. If it sounds uncertain, resolve it before committing.

Then check:
- [ ] Zero prohibited hedging constructs in any surprise body
- [ ] Every surprise has a specific named label
- [ ] Every source is named
- [ ] At least one surprise synthesizes two or more signals
- [ ] Surprises span at least three namespaces
- [ ] Document is under 800 words
- [ ] Add **Patterns** section if applicable

---

The echo is institutional memory. The next team needs to know what the investigation found — not what it might have implied, possibly, under certain interpretations.

---

## V-04 — Combined: Counterfactual gate + Anti-hedging (C-10 + C-12)

**Axes**: V-01's counterfactual as primary culling gate + V-03's prohibited-language enforcement.

**Hypothesis**: The two criteria are naturally coupled — a surprise that passes the counterfactual test (only discoverable through active sensing) is also a surprise with enough evidential weight to state as a claim. Combining them tests whether they reinforce each other: the counterfactual selects for surprises backed by strong signals; the anti-hedging rule ensures those signals are expressed with appropriate confidence. Together they should produce the sharpest echoes — high selection bar, high voice standard.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises that only active signal-gathering could have surfaced — stated as the claims they are.

---

### Two rules that govern this echo

**Rule 1 — The counterfactual gate**

A surprise earns its place by passing this test:

> Would a team that skipped all signal-gathering and relied only on initial strategy, standard planning, and normal development feedback have eventually discovered this?

- **No** — active sensing was required: include it.
- **Yes** — a passive team would have found it: drop it.

This is the sharper version of "was it unexpected?" Expected and discoverable-without-effort are different things. The echo is about what the investigation made visible that nothing else would have.

**Rule 2 — Claim-only voice**

Every surprise is stated as a claim. Prohibited from all surprise entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" | remove |
| "we think" | remove |
| "suggests that" | state the claim directly |

If you cannot state a surprise as a claim, the signal is insufficient — confirm it more firmly or drop it.

---

### Step 1 — Read all signals

Glob and read every artifact:
- `simulations/{topic}/`
- `simulations/{topic}/**/{topic}-*-{date}.md`

For each candidate surprise, apply Rule 1 immediately: could a passive team have discovered this? Record the verdict. Do not write yet.

---

### Step 2 — Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected going in.
3. Fail anything you cannot trace to a named source signal.
4. Keep 3–6 surprises.

---

### Step 3 — Name each surprise

Assign a specific, content-specific named label before writing. Memorable. Not generic. The name should crystallize the finding into a phrase a future reader recalls.

---

### Step 4 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise:

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {stated as a claim: "We assumed X"}
**Found**: {stated as a claim: "X is Y / X is false / the constraint is Z"}
**Design impact**: {stated as a claim: "This changes / confirms / invalidates..."}
**Why passive observation missed this**: {what specific signal or method surfaced it, and why planning or normal feedback would not have}
```

---

### Step 5 — Pre-output checks

**Counterfactual check:**
- [ ] Every surprise fails Rule 1 — no passive team would have found it
- [ ] Every "Why passive observation missed this" cell is populated

**Voice check:**
- [ ] Scan every body paragraph for prohibited constructs — zero occurrences
- [ ] Every `**Found**` field reads as a statement of fact, not a possibility

**Structural checks:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] At least one surprise synthesizes two or more signals
- [ ] Surprises span at least three namespaces
- [ ] Document is under 800 words
- [ ] Add **Patterns** section if applicable

---

The echo is proof that the investigation was worth running. Every surprise you include is an argument for why passive teams ship the wrong thing.

---

## V-05 — Combined: Per-surprise budget + Claim-first structure (C-11 + C-12)

**Axes**: V-02's per-surprise word budget (120 words) + an inverted claim-first structure where the finding is stated as a claim before the evidence is cited.

**Hypothesis**: In the standard structure (Source -> Expected -> Found -> Impact), the author encounters the evidence before committing to the claim — this creates a path to hedging. Inverting the structure forces commitment first: the author must state what is true before tracing back to why. Combined with a 120-word cap, inversion makes hedging structurally harder: there is no room for a tentative statement that is then walked back to certainty. The two mechanisms target C-11 and C-12 from the same structural move.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises — stated as claims, within tight bounds.

---

### Two mechanisms

**Mechanism 1 — Claim-first structure**

Each surprise is written in this order: **claim -> evidence -> impact**.

Not: "The interview surfaced a pattern that may suggest adoption challenges."
But: "Enterprise teams cannot adopt this feature without IT pre-provisioning. Source: prove/interview Round 3. This means the onboarding flow requires a new IT actor lane."

State what is true. Then say where you learned it. Then say what it means for the design.

This order makes hedging structurally harder: by writing the claim first, you commit to it before you reference the evidence. The evidence becomes support for a position, not the source of a tentative observation.

**Mechanism 2 — 120-word cap per surprise**

Each surprise body (not counting the `##` label) is capped at 120 words. If you exceed 120 words, you have not finished synthesizing. Find the single thing the surprise claims and write that. Drop everything else.

The two mechanisms reinforce each other: a claim stated first, in 120 words, cannot meander into hedged qualification.

---

### Step 1 — Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`. Note what contradicts or significantly extends the initial strategy. Do not write yet.

---

### Step 2 — Cull

- Drop anything that confirms what was expected.
- Drop anything you cannot trace to a named source signal.
- Drop anything that could appear unchanged in a standard research summary.
- Keep 3–6 surprises.

---

### Step 3 — Name each surprise

Assign a specific named label before writing the body. Content-specific. Memorable. Not generic.

---

### Step 4 — Write the artifact using claim-first structure

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise uses this order — claim first, evidence second, impact third:

```markdown
## {Named Label}
**Claim**: {the finding stated as fact — "X is true / X is false / X is Y, not Z" — no hedging}
**Source**: {namespace/skill — e.g., "prove/interview", "scout/feasibility"}
**Expected**: {what the team assumed before this signal: "We assumed X"}
**Design impact**: {how this changes, challenges, or confirms the direction — stated as a claim}
```

**After writing each surprise**: count the words from `**Claim**` through the end of `**Design impact**`. If the count exceeds 120, cut until you have a claim, not a description.

---

### Step 5 — Pre-output checks

**Structural checks:**
- [ ] Every surprise leads with a **Claim** field — a statement of fact, not an observation
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Coverage checks:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated — if blank, the contrast is missing
- [ ] At least one surprise synthesizes two or more signals
- [ ] Surprises span at least three namespaces

**Voice check:**
- [ ] Read every **Claim** field aloud as a statement of fact. If it sounds uncertain, rewrite it or drop the item.
- [ ] Zero hedging language anywhere in the document

- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo is institutional memory. Short form is not about brevity for its own sake — it is the evidence that you synthesized the signal rather than transcribed it.
