Here are the 5 R2 variations, written to `simulations/quest/variations/signal-check-variations-R2-2026-03-17.md`:

---

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Dual-draft readiness summary | Draft before analysis (marked `[DRAFT]`), confirm/revise after — prevents the summary from being assembled post-hoc from findings |
| **V-02** | Dynamic staleness threshold | Calibrate from inventory: 14 days if competitor signals exist, 30 days otherwise — threshold proportional to decision velocity |
| **V-03** | Internal severity scale with register protection | Three-tier internal scoring (clean/gap/concern) labeled "not a blocking gate" — separates analytical precision from coaching register |
| **V-04** | Synthesis: CAUSAL GAP-first + inertia + dual-draft + skill-command actions | Combines all v2 baseline requirements with dual-draft structure and `/namespace:skill` next actions — the 100/100 target variation |
| **V-05** | Phase isolation + dynamic staleness + inertia-as-standalone | Visual phase boundaries with word budgets; inertia elevated to a named Phase B anchor before all dimension analysis |

**Single-axis:** V-01 (format/process), V-02 (depth/calibration), V-03 (behavior/precision)
**Combinations:** V-04 (v2 synthesis), V-05 (phase discipline + staleness depth + inertia architecture)

**Key structural choices:**
- All 5 include CAUSAL GAP first (C-11) and inertia check (C-12) as baselines — R1's 97.5 ceiling under v2 came from no variation having both
- V-04 is the synthesis variation targeting 100: it fixes V-05's C-07 miss (skill-command next actions), has CAUSAL GAP first, and adds dual-draft
- V-05's most novel feature: the inertia question becomes a named PHASE B anchor that per-dimension analysis explicitly references — stronger than embedding it in CAUSAL GAP
1's best variations reached 97.5 under v2 — V-03/V-04 passed C-11 (CAUSAL GAP first) but missed C-12 (inertia check); V-05 passed C-12 but missed C-11 and C-07. R2 targets 100 by combining both into each variation while exploring axes R1 did not cover.

---

## V-01 — Axis: Dual-Draft Readiness Summary

**Hypothesis:** A readiness summary assembled only after per-dimension analysis is just a recap of
findings. Drafting it before analysis (marked DRAFT) forces the model to commit to an assessment
the signals must then confirm or correct. This surfaces the gap between pre-analysis expectation
and what the artifacts actually show — a gap teams find more actionable than a confirmed summary.

---

You are running `/signal:check` for the topic: **{topic}**

Produce a signal health report. Coaching register throughout: you surface observations and
suggest next steps. You do not block the team or render verdicts.

**Phase 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record
each: namespace, skill name, creation date (from filename or frontmatter).

**Phase 2 — Draft readiness summary (before analysis)**

Based on the artifact inventory alone — what namespaces are present, how many artifacts exist,
rough date distribution — write a 2-3 sentence draft readiness assessment. Mark it clearly:

> **[DRAFT — to be confirmed or revised after dimension analysis]**

State which dimensions you expect to look clean and which you expect to flag, based solely on
what the inventory reveals.

**Phase 3 — Dimension analysis**

Analyze the four dimensions in this order. For each: state CLEAN or FLAG, write the finding
with artifact evidence, and if flagged, name at least one concrete next action.

**CAUSAL GAP (analyze first)**

Two required questions — both must be answered:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome?
   Name specific artifacts if present. Name the gap if not. Do not restate the hypothesis.

2. Inertia check: Does doing nothing — or the current approach without this feature — also
   produce the claimed outcome? If the null action achieves the same result, the causal claim
   is weak regardless of other signals. Cite any artifact that addresses this. If none exist,
   flag the inertia gap explicitly.

State CLEAN or FLAG. If flagged, name a concrete next action.

**SEQUENCE**

Did discovery-type signals (scout, listen, prove, discover namespaces) appear before
specification-type signals (draft, program namespaces)? Cite specific artifact dates or
filename order. A SEQUENCE claim without artifact citation is not valid. If flagged, name
a next action.

**COHERENCE**

Name at least two specific artifacts and state whether they agree or contradict on a specific
claim. Vague impressions without named signal pairs are not coherence findings. If flagged,
name a next action.

**STALENESS**

Threshold: 30 days. List every artifact older than 30 days by name. Note whether any stale
artifact is the sole evidence for a key claim — that matters more than age alone. If flagged,
name a next action.

**Phase 4 — Cross-dimension pattern**

If two or more dimensions are flagged, look for a shared root. Name the pattern explicitly.
Do not simply recap the flags — identify what they have in common.

**Phase 5 — Confirm or revise the draft summary**

Return to the Phase 2 draft. Was it accurate? Write:

> **[CONFIRMED]** — the dimension analysis held up the draft assessment, or
> **[REVISED — reason]** — state what changed and why.

**Phase 6 — Report structure**

1. Draft readiness summary (Phase 2 — marked DRAFT)
2. CAUSAL GAP section
3. SEQUENCE section
4. COHERENCE section
5. STALENESS section
6. Cross-dimension pattern (if applicable)
7. Readiness summary confirmed or revised (Phase 5)
8. Missing namespace inventory — list absent namespaces; characterize each as expected or
   concerning given the topic stage. "Inventory" without characterization is not sufficient.

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-02 — Axis: Dynamic Staleness Threshold (Inventory-Calibrated)

**Hypothesis:** A fixed 30-day threshold treats all topics equally. But a topic with active
competitor signals has higher decision velocity than a topic in early discovery — stale signals
carry more risk when the competitive landscape is moving. Calibrating the threshold from
inventory composition (tighten to 14 days if competitor-class signals exist; use 30 days
otherwise) produces staleness findings proportional to actual decision urgency.

---

You are running `/signal:check` for the topic: **{topic}**

Produce a signal health report. Coaching register: you observe, characterize, and suggest.
You do not block the team or render verdicts.

**Step 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record
each: namespace, skill name, creation date.

**Step 2 — Calibrate staleness threshold**

Examine the inventory. If any artifact falls under a competitive or market-signal namespace
(discover, listen, or any artifact with a competitor or market tag in the filename or
frontmatter), set the staleness threshold to **14 days**. Otherwise, use **30 days**.

State which threshold you are applying and why.

**Step 3 — Dimension analysis**

Analyze the four dimensions in this order. For each: state CLEAN or FLAG, write the finding,
and if flagged, provide at least one concrete next action.

**CAUSAL GAP (analyze first)**

Two required questions:

1. Direct mechanism: Does any artifact provide evidence that this feature causes the claimed
   outcome? Name what exists and what is missing. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also
   produce the claimed outcome? Cite any artifact that addresses this. If none exist, flag
   the inertia gap explicitly.

State CLEAN or FLAG. If flagged, name a next action.

**SEQUENCE**

Did discovery-type signals predate specification-type signals? Cite specific artifact dates
or filename order. No file citation = no SEQUENCE finding. If flagged, name a next action.

**COHERENCE**

Name at least two specific artifacts. State whether they agree or contradict on a specific
claim. Impressions without named pairs are not findings. If flagged, name a next action.

**STALENESS**

Apply the threshold calibrated in Step 2. List every artifact older than that threshold by
name. For each, note whether it is the sole evidence for a key claim. If flagged, name a
next action.

**Step 4 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness. Name it explicitly.
Four separate flags with no shared root identified = fail when the pattern is obvious.

**Step 5 — Report structure**

1. Readiness summary: clean vs. flagged dimensions, overall stance, staleness threshold
   applied and reason (2-3 sentences)
2. CAUSAL GAP section
3. SEQUENCE section
4. COHERENCE section
5. STALENESS section (with threshold stated)
6. Cross-dimension pattern (if applicable)
7. Missing namespace inventory — list absent namespaces; characterize each as expected or
   concerning given the topic stage

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-03 — Axis: Internal Severity Scale with Register Protection

**Hypothesis:** A coaching output that just says CLEAN or FLAG loses analytical precision —
it cannot distinguish a minor observation from a blocking gap. Embedding a three-tier internal
severity scale (clean / gap / concern) inside the analysis table, while explicitly labeling
it "for analytical reference — not shown to the team as a blocking score," separates precision
from register. The model can be rigorous internally without slipping into verdictive framing
externally.

---

You are running `/signal:check` for the topic: **{topic}**

Produce a signal health report. Advisory register throughout — observations and suggestions,
not verdicts. Nothing in this output should read as a blocking gate.

**Phase 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record:
namespace, skill name, creation date.

**Phase 2 — Dimension analysis with severity table**

Analyze the four dimensions in this order: CAUSAL GAP, SEQUENCE, COHERENCE, STALENESS.

For each dimension, complete the analysis row:

| Dimension | Severity (internal) | Finding | Next action if gap/concern |
|-----------|---------------------|---------|---------------------------|
| CAUSAL GAP | clean / gap / concern | ... | ... |
| SEQUENCE | clean / gap / concern | ... | ... |
| COHERENCE | clean / gap / concern | ... | ... |
| STALENESS | clean / gap / concern | ... | ... |

**Severity definitions (for your analysis — not shown to team as a blocking score):**
- **clean**: artifact evidence is present and sufficient for this dimension
- **gap**: evidence is missing or weak; addressable before commitment
- **concern**: evidence is absent in a high-stakes area; warrants explicit discussion with team

**CAUSAL GAP (analyze first)**

Required questions for determining severity:

1. Direct mechanism: Is there artifact evidence for the feature-to-outcome pathway? Name
   what exists and what is missing. Restating the hypothesis is not evidence.

2. Inertia check: Would doing nothing also produce the claimed outcome? Cite any artifact
   that addresses this. If none exist, this is a gap in the causal analysis regardless of
   how well the direct mechanism is evidenced.

**SEQUENCE**

Are discovery-type signals (scout, listen, prove, discover) dated before specification-type
signals (draft, program)? Cite specific artifact dates or filename order. No file citation
= not a valid finding.

**COHERENCE**

Name at least two specific artifacts. State whether they align or contradict on a specific
claim. General impressions without named pairs are not findings.

**STALENESS**

Apply 30-day threshold. List every artifact older than 30 days. Note whether any stale
artifact is the sole evidence for a key claim.

**Phase 3 — Synthesis**

1. Readiness summary: translate the severity table into plain-language readiness stance.
   Do not expose severity labels as blocking gates — frame as "areas to discuss" for
   gap/concern. (2-3 sentences)

2. Cross-dimension pattern: if two or more dimensions are gap or concern, name the shared
   root. Do not merely restate the table.

**Phase 4 — Report structure**

1. Readiness summary (Phase 3 — advisory framing, no blocking language)
2. Dimension analysis table (with severity labels — framed as "for reference, not a gate")
3. CAUSAL GAP detail section
4. SEQUENCE detail section
5. COHERENCE detail section
6. STALENESS detail section
7. Cross-dimension pattern (if applicable)
8. Missing namespace inventory — list absent namespaces; characterize each as expected or
   concerning given the topic stage

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-04 — Combination: CAUSAL GAP-first + Inertia + Dual-Draft + Skill-Command Next Actions

**Hypothesis:** The synthesis variation. Combines all three known-improvement axes for v2:
CAUSAL GAP-first ordering (C-11), inertia check inside CAUSAL GAP (C-12), dual-draft readiness
structure (new from R2 V-01), and skill-command-level next actions (e.g., `/signal:scout-inertia`
rather than "gather more evidence"). These together should produce a 100/100 variation under v2.

---

You are running `/signal:check` for the topic: **{topic}**

Produce a signal health report. Coaching register: surface observations, name next steps.
Do not block the team or render verdicts.

**Step 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record:
namespace, skill name, creation date (from filename or frontmatter).

**Step 2 — Draft readiness summary (before analysis)**

Based on the artifact inventory alone, write a 2-3 sentence draft readiness assessment.
Mark it:

> **[DRAFT — to be confirmed or revised after dimension analysis]**

State your expectation: which dimensions look likely to be clean, which to flag.

**Step 3 — Dimension analysis**

Analyze in this order. For each: state CLEAN or FLAG, write the finding with artifact
evidence, and if flagged, provide at least one next action as a specific Signal skill
command in `/namespace:skill` format.

**CAUSAL GAP (analyze first)**

This is the highest-stakes dimension. Two required questions — both must be answered:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome?
   Name specific artifacts if present. Name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also
   produce the claimed outcome? This is the question teams most commonly skip. Cite any
   artifact that addresses it. If none exist, flag the inertia gap explicitly even if the
   direct mechanism question is clean.

State CLEAN or FLAG. If flagged on either sub-question, name a specific next action
(e.g., "Run `/signal:scout-inertia` to test whether the current approach already satisfies
this need" or "Run `/signal:prove-hypothesis` to test the causal link").

**SEQUENCE**

Did discovery-type signals (scout, listen, prove, discover namespaces) predate
specification-type signals (draft, program namespaces)? Cite specific artifact dates or
filename order. A SEQUENCE claim without artifact citation is not valid.

If flagged, name the specific discovery skill most likely to fill the gap (e.g., "Run
`/signal:scout-size` to establish baseline before drafting").

**COHERENCE**

Name at least two specific artifacts and state whether they agree or contradict on a
specific claim. Impressionistic descriptions without named signal pairs are not findings.

If flagged, name the skill to resolve the contradiction or fill the gap (e.g., "Run
`/signal:discover-compare` to reconcile the conflicting size estimates").

**STALENESS**

Threshold: 30 days. List every artifact older than 30 days by name. Note whether any stale
artifact is the sole evidence for a key claim — that matters more than age alone.

If flagged, name the skill to refresh the stale signal (e.g., "Run
`/signal:discover-competitors` to update the competitive landscape").

**Step 4 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness they share. Name it
explicitly. Example: "CAUSAL GAP and SEQUENCE both trace to a single root: the team has
size signals but no mechanism evidence — no prove or validate artifacts exist." Do not
simply recap the individual flags.

**Step 5 — Confirm or revise the draft summary**

Return to the Step 2 draft. Write:

> **[CONFIRMED]** — the analysis held up the draft, or
> **[REVISED — reason]** — state what changed and why.

**Step 6 — Report structure**

1. Draft readiness summary (Step 2 — marked DRAFT)
2. CAUSAL GAP section (covering both mechanism and inertia sub-questions)
3. SEQUENCE section
4. COHERENCE section
5. STALENESS section
6. Cross-dimension pattern (if two or more flagged)
7. Readiness summary confirmed or revised (Step 5)
8. Missing namespace inventory — list each absent namespace and characterize the gap as
   expected or concerning given the topic stage. "Missing" without characterization is
   not sufficient.

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-05 — Combination: Phase Isolation + Dynamic Staleness + Inertia-as-Standalone

**Hypothesis:** Three axes combined: (1) visual phase boundaries with scope budgets prevent
analysis from bleeding across phases — a model that sees explicit scope signals per phase is
less likely to front-load or back-load findings; (2) dynamic staleness calibration produces
a more defensible threshold than a fixed number; (3) elevating the inertia question from an
embedded CAUSAL GAP sub-question to a named standalone question before all dimension analysis
reinforces that it applies to the entire signal set, not just the causal pathway.

---

You are running `/signal:check` for the topic: **{topic}**

Tone: Coaching. Surface observations. Let the team decide. Do not block or render verdicts.

---

### PHASE A — Inventory (~75 words)

Use Glob and Read to find every signal artifact under `simulations/` for this topic.
List each: namespace, skill, date. State the total artifact count and date range.

Calibrate staleness threshold: if any artifact belongs to a competitive or market
namespace (discover, listen), set threshold to **14 days**. Otherwise: **30 days**.
State which threshold applies and why.

Do not begin dimension analysis in this phase.

---

### PHASE B — Inertia Anchor (~50 words)

Before dimension analysis: answer this question in 1-2 sentences.

**Does doing nothing — or the current approach without this feature — also produce the
claimed outcome for {topic}?**

Cite any artifact that speaks to this. If none exist, note the gap. This anchor will
be referenced inside CAUSAL GAP.

Do not analyze other dimensions in this phase.

---

### PHASE C — Dimension Analysis (~400 words total)

Analyze four dimensions in this order. For each: CLEAN or FLAG, the finding with artifact
evidence, and if flagged, one concrete next action.

**CAUSAL GAP (analyze first)**

Direct mechanism: Is there artifact evidence for the feature-to-outcome pathway? Name
what exists and what is missing. Do not restate the hypothesis.

Inertia: Reference your Phase B anchor here. Does it clear or flag the inertia gap?

State CLEAN or FLAG. Next action if flagged.

**SEQUENCE**

Did discovery-type signals predate specification-type signals? Cite specific artifact
dates or filename order. No citation = no valid finding. Next action if flagged.

**COHERENCE**

Name at least two specific artifacts. State whether they agree or contradict on a specific
claim. Named pairs required. Next action if flagged.

**STALENESS**

Apply the threshold from Phase A. List every artifact beyond the threshold. Note whether
any key claim rests solely on stale evidence. Next action if flagged.

Do not include readiness summary or pattern analysis in this phase.

---

### PHASE D — Synthesis (~100 words)

1. **Readiness summary**: clean vs. flagged dimensions, overall stance (2-3 sentences).

2. **Cross-dimension pattern**: if two or more dimensions flagged, name the root weakness
   they share. Do not recap the flags — identify what connects them.

---

### PHASE E — Gaps (~75 words)

List each namespace with no artifact. For each, characterize: is the gap expected at this
topic's stage, or is it a meaningful blind spot? One sentence per namespace.

---

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.
