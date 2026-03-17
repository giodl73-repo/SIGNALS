**`simulations/quest/variations/signal-check-variations-R3-2026-03-17.md`** — written.

---

## R3 Variations Summary

| # | Axis | Single/Combo | Key target |
|---|------|-------------|------------|
| **V-01** | Per-dimension CONFIRMED/REVISED | Single | C-13 — lifecycle marker inline after each dimension, not deferred to summary |
| **V-02** | Calibrated threshold + decision-velocity rationale | Single | C-15 — threshold and mechanism declared together (why competitive signals → higher risk) |
| **V-03** | Severity table with named INTERNAL ANALYSIS BLOCK | Single | C-16 — register separation architectural, not just disclaimed inline |
| **V-04** | Full v3 synthesis | Combo | C-13 + C-14 + C-15 + C-16 — the 100/100 target |
| **V-05** | Evidence census foundation layer | Novel | All four criteria plus census matrix before analysis — novel axis not in R1/R2 |

**Gap analysis driving design choices:**

- R2 V-01 and V-04 had DRAFT summaries but per-dimension CONFIRMED/REVISED markers were absent → **V-01 fixes this** by placing the marker at each production site
- R2 V-02 declared the threshold and rationale but the rationale was a rule ("use 14 days if...") not a mechanism → **V-02 adds the causal chain** (why competitive signals cause higher staleness risk)
- R2 V-03 had "not shown to team as a blocking score" inside the severity definitions — a disclaim, not an architectural boundary → **V-03 creates a named INTERNAL ANALYSIS BLOCK** with header framing that precedes the table
- No R2 variation passed all four new criteria → **V-04 is the synthesis**

**V-04 is the 100/100 candidate under v3.** V-05's census layer adds a novel organizational axis but carries more structural risk (11-section report).
, V-05 (census foundation + v3 baseline)

**R2 gap analysis under v3:**
- V-01 (R2): DRAFT summary present, CONFIRMED/REVISED only at summary level — C-13 fails (per-dimension markers absent)
- V-02 (R2): Dynamic threshold with stated reason — C-15 passes; but no severity table (C-16 fails), no /namespace:skill format (C-14 fails), no per-dimension markers (C-13 fails)
- V-03 (R2): Severity table with explicit "not a gate" label — C-16 passes; but fixed threshold (C-15 fails), no per-dimension markers (C-13 fails), no /namespace:skill format (C-14 fails)
- V-04 (R2): /namespace:skill format — C-14 passes; fixed threshold (C-15 fails), no severity table (C-16 fails), per-dimension markers absent (C-13 fails)
- V-05 (R2): Dynamic threshold declared — C-15 passes; C-08 fails (summary after dimensions); C-13/C-14/C-16 all fail

R3 targets: close the remaining gaps. V-04 is the synthesis variation; all four new criteria must pass together.

---

## V-01 — Axis: Per-Dimension CONFIRMED/REVISED Lifecycle

**Hypothesis:** R2 introduced the DRAFT/CONFIRMED pattern at the summary level (Phase 5 or Step 5 post-hoc). C-13's requirement is stronger: each dimension must explicitly mark CONFIRMED or REVISED against the draft inline — not deferred to a final summary step. Embedding the lifecycle marker after each dimension's conclusion creates a structurally verifiable commitment: the CONFIRMED/REVISED appears at the production site of the finding, not assembled afterward from impressions.

---

You are running `/signal:check` for the topic: **{topic}**

Produce a signal health report. Coaching register throughout — surface observations, suggest next steps. Do not block the team or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date (from filename or frontmatter). List all artifacts found.

---

**STEP 2 — Draft readiness summary (before analysis)**

Based on the artifact inventory alone — what namespaces are present, how many artifacts, what date range — write a 2–3 sentence draft readiness assessment. Mark it:

> **[DRAFT — to be confirmed or revised per dimension below]**

For each of the four dimensions, state your pre-analysis expectation:
- CAUSAL GAP: expect CLEAN or FLAG?
- SEQUENCE: expect CLEAN or FLAG?
- COHERENCE: expect CLEAN or FLAG?
- STALENESS: expect CLEAN or FLAG?

These four predictions are what each dimension's CONFIRMED/REVISED marker resolves below. The per-dimension markers must appear inline — not in a summary step after analysis.

---

**STEP 3 — Dimension analysis**

Analyze in this order. For each dimension: write the finding with artifact evidence, state CLEAN or FLAG, and if flagged, name at least one concrete next action. Immediately after the conclusion — before the next dimension begins — write the lifecycle marker:

> **[CONFIRMED]** — finding matches the draft prediction for this dimension, or
> **[REVISED — reason]** — state what differed from the draft and why.

---

**CAUSAL GAP (analyze first)**

Two required sub-questions — both must be answered:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome? Name specific artifacts if present. Name the gap explicitly if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Cite any artifact addressing this. If no artifact exists for the inertia question, flag the gap explicitly even if the mechanism question looks clean.

State CLEAN or FLAG. If flagged on either sub-question, name a concrete next action (e.g., "Run `/signal:scout-inertia` to test whether the status quo satisfies this need" or "Run `/signal:prove-hypothesis` to establish the causal link").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**SEQUENCE**

Did discovery-type signals (scout, listen, prove, discover namespaces) appear before specification-type signals (draft, program namespaces)? Cite specific artifact dates or filename order. A SEQUENCE claim without artifact citation is not valid.

State CLEAN or FLAG. If flagged, name a concrete next action (e.g., "Run `/signal:scout-size` to establish a discovery baseline before draft artifacts").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

Name at least two specific artifacts and state whether they agree or contradict on a specific claim. Impressions without named signal pairs are not findings.

State CLEAN or FLAG. If flagged, name a concrete next action (e.g., "Run `/signal:discover-compare` to reconcile the conflicting signals").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

Threshold: 30 days. List every artifact older than 30 days by name. For each, note whether it is the sole evidence for a key claim — that matters more than age alone.

State CLEAN or FLAG. If flagged, name a concrete next action (e.g., "Run `/signal:discover-competitors` to refresh the competitive landscape").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 4 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness they share. Name it explicitly. Do not recap the individual flags — identify what connects them. If the pattern traces to a single missing evidence type or phase, name that directly.

---

**STEP 5 — Final readiness summary**

Review the four per-dimension lifecycle markers. Write a consolidated readiness summary that reflects the full analysis. If any dimension was REVISED, the summary must incorporate those revisions — it cannot repeat the Step 2 draft verbatim.

---

**STEP 6 — Missing namespace inventory**

List every namespace with no artifact for this topic. For each, characterize the gap: expected given the topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Draft readiness summary (Step 2 — marked DRAFT, with per-dimension predictions)
2. CAUSAL GAP section (with CONFIRMED/REVISED marker immediately after)
3. SEQUENCE section (with CONFIRMED/REVISED marker immediately after)
4. COHERENCE section (with CONFIRMED/REVISED marker immediately after)
5. STALENESS section (with CONFIRMED/REVISED marker immediately after)
6. Cross-dimension pattern (if two or more flagged)
7. Final readiness summary (Step 5)
8. Missing namespace inventory

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-02 — Axis: Calibrated Threshold with Decision-Velocity Rationale

**Hypothesis:** R2 V-02 calibrates the threshold based on inventory type and says "state which threshold and why." C-15 requires the calibration reason to be declared alongside the threshold — with the reason naming the mechanism, not just the conclusion. V-03 makes the causal chain explicit: competitive signals → moving landscape → higher decision velocity → higher staleness risk → tighter threshold. Declaring the mechanism makes the threshold defensible to a reader who disagrees with the calibration, not just traceable.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register: you observe, characterize, and suggest. You do not block or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date. List all found.

---

**STEP 2 — Staleness threshold: calibrate from inventory with decision-velocity rationale**

After reviewing the inventory, declare the staleness threshold using this logic:

**If the inventory contains artifacts from competitive or market-facing namespaces (discover, listen), or any filename contains "competitor", "market", or "competitive":**

> **Threshold: 14 days**
> **Calibration rationale:** This inventory contains competitive or market signals. These signal types track a moving landscape — the competitive environment can shift significantly within days, not months. Decisions made with stale competitive data carry higher risk than decisions made with stale size or feasibility estimates, because competitive positioning changes faster than underlying market structure. 14 days reflects this higher decision velocity.

**If the inventory contains no competitive or market signals:**

> **Threshold: 30 days**
> **Calibration rationale:** This inventory contains no competitive or market signals. The evidence types present (size, feasibility, coherence signals) have lower time-sensitivity — they reflect stable structural facts about the problem space rather than moving competitive dynamics. 30 days is proportionate to the decision velocity for this topic stage.

State the threshold and the full rationale together as a labeled block. The rationale must name the mechanism (what property of competitive signals causes higher staleness risk), not just the rule.

---

**STEP 3 — Draft readiness summary (before analysis)**

Based on the inventory and threshold calibration, write a 2–3 sentence draft readiness assessment. Mark it:

> **[DRAFT — to be confirmed or revised after dimension analysis]**

State which dimensions you expect to look clean and which to flag.

---

**STEP 4 — Dimension analysis**

Analyze in this order. For each: state CLEAN or FLAG, write the finding with artifact evidence, and if flagged, provide at least one concrete next action (use `/namespace:skill` format, e.g., "Run `/signal:scout-inertia`").

**CAUSAL GAP (analyze first)**

Two required questions — both must be answered:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome? Name specific artifacts if present; name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:scout-inertia`" or "Run `/signal:prove-hypothesis`").

**SEQUENCE**

Did discovery-type signals (scout, listen, prove, discover namespaces) predate specification-type signals (draft, program namespaces)? Cite specific artifact dates or filename order. A SEQUENCE claim without artifact citation is not valid.

If flagged, name a next action (e.g., "Run `/signal:scout-size` before advancing draft work").

**COHERENCE**

Name at least two specific artifacts. State whether they agree or contradict on a specific claim. Impressions without named pairs are not findings.

If flagged, name a next action (e.g., "Run `/signal:discover-compare` to reconcile the contradiction").

**STALENESS**

Apply the threshold from Step 2. Restate it here: **[X days]** — because [one-phrase rationale recap]. List every artifact beyond the threshold by name. For each, note whether it is the sole evidence for a key claim.

If flagged, name a next action (e.g., "Run `/signal:discover-competitors` to refresh the competitive landscape").

---

**STEP 5 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness they share. Name it explicitly. Do not simply recap the flags.

---

**STEP 6 — Confirm or revise the draft**

Return to Step 3. Write:

> **[CONFIRMED]** — the dimension analysis held up the draft assessment, or
> **[REVISED — reason]** — state what changed and why.

---

**STEP 7 — Missing namespace inventory**

List every namespace with no artifact. For each, characterize the gap: expected at this topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Staleness threshold block (Step 2 — threshold and calibration rationale declared together)
2. Draft readiness summary (Step 3 — marked DRAFT)
3. CAUSAL GAP section
4. SEQUENCE section
5. COHERENCE section
6. STALENESS section (with threshold restated)
7. Cross-dimension pattern (if two or more flagged)
8. Draft summary confirmed or revised (Step 6)
9. Missing namespace inventory

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-03 — Axis: Severity Table with Explicit Internal/External Register Architecture

**Hypothesis:** R2 V-03 embedded a severity table with "not shown to team as a blocking score" in the severity definition line. C-16's key constraint is architectural: the severity scale must be explicitly labeled as internal and decoupled from the coaching register — not just disclaimed inline. V-03 achieves this by naming the internal analysis as a distinct block with a header that makes the separation structural rather than instructional. The framing sentence appears before the table — not inside it — so the register boundary is declared at the block level, not at the row level.

---

You are running `/signal:check` for the topic: **{topic}**

Advisory register: surface observations, suggest next steps, let the team decide. Nothing in this output is a blocking gate.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date.

---

**STEP 2 — Draft readiness summary (before analysis)**

Based on the inventory alone, write a 2–3 sentence draft readiness assessment. Mark it:

> **[DRAFT — to be confirmed or revised after dimension analysis]**

---

**STEP 3 — Internal severity assessment**

Before writing any team-facing narrative, complete this internal analysis table.

> **--- INTERNAL ANALYSIS BLOCK ---**
> **The table below is for your reference only — it is not team-facing output.**
> **Severity ratings are internal analytical notation, not blocking gates.**
> **The coaching narrative in Step 4 is what the team reads.**
> **This block structures your analysis before you write it.**

| Dimension | Severity (internal) | Artifact evidence summary |
|-----------|---------------------|--------------------------|
| CAUSAL GAP | clean / gap / concern | ... |
| SEQUENCE | clean / gap / concern | ... |
| COHERENCE | clean / gap / concern | ... |
| STALENESS | clean / gap / concern | ... |

**Severity definitions — for your analysis only:**
- **clean** — evidence is present and adequate
- **gap** — evidence is missing or thin; addressable before commitment
- **concern** — evidence is absent in a high-stakes area; explicit team discussion warranted

Complete the table before writing the coaching narrative. Severity labels from this block do not appear in the narrative below.

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 4 — Dimension narrative (team-facing coaching)**

Write the coaching narrative for each dimension. Severity ratings from Step 3 inform your framing but do not appear verbatim in the narrative — the team sees observations and suggestions, not analytical tiers.

Analyze in this order. For each: write the finding with artifact evidence, and if the severity is gap or concern, provide at least one concrete next action (use `/namespace:skill` format, e.g., "Run `/signal:scout-inertia`").

**CAUSAL GAP (analyze first)**

Two required questions:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome? Name specific artifacts or name the gap. Do not restate the hypothesis.

2. Inertia check: Would doing nothing also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly.

If gap or concern, name a next action (e.g., "Run `/signal:prove-hypothesis`" or "Run `/signal:scout-inertia`").

**SEQUENCE**

Did discovery-type signals predate specification-type signals? Cite specific artifact dates or filename order. No citation = no valid finding.

If gap or concern, name a next action (e.g., "Run `/signal:scout-size`").

**COHERENCE**

Name at least two specific artifacts. State whether they agree or contradict on a specific claim. Named pairs required.

If gap or concern, name a next action (e.g., "Run `/signal:discover-compare`").

**STALENESS**

Threshold: 30 days. List every artifact older than 30 days by name. Note whether any stale artifact is the sole evidence for a key claim.

If gap or concern, name a next action (e.g., "Run `/signal:discover-competitors`").

---

**STEP 5 — Synthesis**

1. **Cross-dimension pattern**: if two or more dimensions are gap or concern in Step 3, name the root weakness they share. Translate from the severity table to a plain-language diagnosis — do not merely restate the table entries.

2. **Confirm or revise the draft**: return to Step 2. Write:
   > **[CONFIRMED]** — the analysis held up the draft, or
   > **[REVISED — reason]** — state what changed.

---

**STEP 6 — Missing namespace inventory**

List each namespace with no artifact. For each, characterize: expected given topic stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Draft readiness summary (Step 2 — marked DRAFT)
2. Internal severity table (Step 3 — clearly bounded "INTERNAL ANALYSIS BLOCK")
3. CAUSAL GAP narrative
4. SEQUENCE narrative
5. COHERENCE narrative
6. STALENESS narrative
7. Cross-dimension pattern (if applicable)
8. Draft summary confirmed or revised
9. Missing namespace inventory

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-04 — Synthesis: All Four v3 Criteria (C-13 per-dim + C-14 skill commands + C-15 calibration + C-16 severity)

**Hypothesis:** The synthesis variation for v3. Combines all four new criteria: per-dimension CONFIRMED/REVISED markers (C-13), `/namespace:skill` format for next actions (C-14), calibrated staleness threshold with decision-velocity rationale (C-15), and internal severity table with explicit architectural separation (C-16). Builds on R2 V-04's baseline (CAUSAL GAP first, inertia check, dual-draft summary, skill-command next actions) and adds the three new axes missed in R2. This is the 100/100 target under v3.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register throughout — surface observations, name next steps, let the team decide. Do not block the team or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date (from filename or frontmatter).

---

**STEP 2 — Staleness calibration with decision-velocity rationale**

Examine the inventory. If any artifact falls under a competitive or market-signal namespace (discover, listen), or any filename contains "competitor" or "market":

> **Threshold: 14 days**
> **Calibration rationale:** Competitive and market signals track a moving landscape. The competitive environment can shift significantly within days — decisions made with stale competitive data carry higher risk than decisions on stale structural signals (size, feasibility), because competitive positioning changes faster than underlying market structure. 14 days reflects this higher decision velocity.

Otherwise:

> **Threshold: 30 days**
> **Calibration rationale:** No competitive or market signals in inventory. Evidence types present have lower time-sensitivity — they reflect stable structural facts rather than moving dynamics. 30 days is proportionate to the decision velocity at this topic stage.

Declare the threshold and the full rationale together as a labeled block before proceeding.

---

**STEP 3 — Internal severity table**

Before writing any team-facing narrative, populate this internal analysis table.

> **--- INTERNAL ANALYSIS BLOCK ---**
> **Severity ratings below are for your analytical reference only — they are not team-facing output and not blocking gates.**
> **The coaching narrative in Step 5 is what the team reads.**
> **This table structures your analysis before you write it.**

| Dimension | Severity (internal) | Pre-analysis expectation |
|-----------|---------------------|--------------------------|
| CAUSAL GAP | clean / gap / concern | CLEAN / FLAG |
| SEQUENCE | clean / gap / concern | CLEAN / FLAG |
| COHERENCE | clean / gap / concern | CLEAN / FLAG |
| STALENESS | clean / gap / concern | CLEAN / FLAG |

**Severity definitions — internal reference only:**
- **clean** — evidence is present and sufficient
- **gap** — evidence is missing or thin; addressable before commitment
- **concern** — evidence is absent in a high-stakes area; explicit team discussion warranted

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 4 — Draft readiness summary (before analysis)**

Based on the inventory and the internal severity table, write a 2–3 sentence draft readiness assessment. State which dimensions you expect to confirm clean and which to flag. Mark it:

> **[DRAFT — to be confirmed or revised per dimension below]**

---

**STEP 5 — Dimension analysis**

Analyze in this order. For each: write the finding with artifact evidence, state CLEAN or FLAG, and if flagged, provide at least one next action in `/namespace:skill` format. Immediately after each dimension's conclusion — before the next dimension begins — write the lifecycle marker:

> **[CONFIRMED]** — finding matched the draft prediction, or
> **[REVISED — reason]** — state what differed and why.

---

**CAUSAL GAP (analyze first)**

This is the highest-stakes dimension. Two required sub-questions — both must be answered:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome? Name specific artifacts if present; name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? This is the question teams most commonly skip. Cite any artifact addressing this. If none exist, flag the inertia gap explicitly even if the mechanism question looks clean.

State CLEAN or FLAG. If flagged on either sub-question, name a next action in `/namespace:skill` format (e.g., "Run `/signal:scout-inertia` to test whether the current approach already satisfies this need" or "Run `/signal:prove-hypothesis` to establish the causal link").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**SEQUENCE**

Did discovery-type signals (scout, listen, prove, discover namespaces) predate specification-type signals (draft, program namespaces)? Cite specific artifact dates or filename order. A SEQUENCE claim without artifact citation is not valid.

State CLEAN or FLAG. If flagged, name the specific next action in `/namespace:skill` format (e.g., "Run `/signal:scout-size` to establish a discovery baseline before proceeding with draft artifacts").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

Name at least two specific artifacts and state whether they agree or contradict on a specific claim. Impressions without named signal pairs are not findings.

State CLEAN or FLAG. If flagged, name the next action in `/namespace:skill` format (e.g., "Run `/signal:discover-compare` to reconcile the conflicting signals").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

Apply the threshold from Step 2 — state it again here: **[X days]** (because [one-phrase rationale recap]). List every artifact older than this threshold by name. For each, note whether it is the sole evidence for a key claim — that matters more than age alone.

State CLEAN or FLAG. If flagged, name the next action in `/namespace:skill` format (e.g., "Run `/signal:discover-competitors` to update the competitive landscape").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 6 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness they share. Name it explicitly. Example: "CAUSAL GAP and SEQUENCE both trace to a single root: the team has size signals but no mechanism evidence — no prove or validate artifacts exist." Do not recap the individual flags.

---

**STEP 7 — Final readiness summary**

Review the four per-dimension CONFIRMED/REVISED markers. Write a consolidated readiness summary that reflects the full analysis. If any dimension was REVISED, the summary must incorporate that revision — it cannot simply repeat the Step 4 draft.

---

**STEP 8 — Missing namespace inventory**

List each namespace with no artifact. For each, characterize: expected at this topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Staleness threshold block (Step 2 — threshold and calibration rationale declared together)
2. Internal severity table (Step 3 — bounded "INTERNAL ANALYSIS BLOCK", not a gate)
3. Draft readiness summary (Step 4 — marked DRAFT with per-dimension predictions)
4. CAUSAL GAP section (with CONFIRMED/REVISED marker)
5. SEQUENCE section (with CONFIRMED/REVISED marker)
6. COHERENCE section (with CONFIRMED/REVISED marker)
7. STALENESS section (with CONFIRMED/REVISED marker, threshold restated)
8. Cross-dimension pattern (if two or more flagged)
9. Final readiness summary (Step 7)
10. Missing namespace inventory

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-05 — Novel Axis: Evidence Census Foundation Layer

**Hypothesis:** Running a structured evidence census before analysis — explicitly mapping every artifact to a namespace × date matrix — gives all dimension findings a shared reference base. Teams see the evidence inventory gap before reading any dimension flag, reframing the output from "here's what's wrong" to "here's what evidence you have and what it says together." Dimensions cite census entries directly rather than re-listing artifacts in each section. This novel organizational axis reduces per-section artifact repetition and makes gaps visible structurally before any diagnostic claim is made. Not tried in R1 or R2.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register: surface what the evidence shows, suggest next steps, let the team decide. No blocking language.

---

**STEP 1 — Evidence census**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Build a census matrix:

| Namespace | Artifacts present | Dates | Count |
|-----------|-------------------|-------|-------|
| discover  | [list] or none    | ...   | n     |
| specify   | [list] or none    | ...   | n     |
| validate  | [list] or none    | ...   | n     |
| simulate  | [list] or none    | ...   | n     |
| narrate   | [list] or none    | ...   | n     |
| govern    | [list] or none    | ...   | n     |
| signal    | [list] or none    | ...   | n     |
| tools     | [list] or none    | ...   | n     |

After the matrix, state: total artifact count, date range (oldest to newest), namespaces with zero artifacts.

The census is the reference base for all findings below. Dimension sections cite census entries directly — artifact names are not re-listed in each section.

---

**STEP 2 — Staleness calibration with rationale**

Examine the census. If any namespace with artifacts is competitive or market-facing (discover, listen) or any filename contains "competitor" or "market":

> **Threshold: 14 days**
> **Calibration rationale:** Census contains competitive or market signals, which track a moving landscape. Competitive positioning changes faster than structural signals (size, feasibility) — decisions on stale competitive data carry higher risk. 14 days reflects the higher decision velocity these evidence types demand.

Otherwise:

> **Threshold: 30 days**
> **Calibration rationale:** Census contains no competitive or market signals. Evidence types present have lower time-sensitivity. 30 days is proportionate to the decision velocity at this topic stage.

---

**STEP 3 — Internal severity table**

Before writing any narrative, assess severity from the census.

> **--- INTERNAL ANALYSIS BLOCK ---**
> **This table is for your reference only — not team-facing, not a blocking gate.**
> **The coaching narrative in Step 5 is the team-facing output.**

| Dimension | Severity (internal) | Census evidence |
|-----------|---------------------|-----------------|
| CAUSAL GAP | clean / gap / concern | [key census entries] |
| SEQUENCE | clean / gap / concern | [key census entries] |
| COHERENCE | clean / gap / concern | [key census entries] |
| STALENESS | clean / gap / concern | [key census entries] |

**Severity definitions — internal only:**
- **clean** — census shows adequate evidence
- **gap** — census shows missing or thin evidence; addressable
- **concern** — census shows absent evidence in a high-stakes area

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 4 — Draft readiness summary (before analysis)**

Based on the census and severity table, write a 2–3 sentence draft readiness assessment. Mark it:

> **[DRAFT — census-derived, to be confirmed or revised per dimension below]**

State per-dimension predictions: which dimensions you expect to confirm clean and which to flag.

---

**STEP 5 — Dimension analysis**

The census in Step 1 is your shared reference. Cite census entries directly. For each dimension: write the finding, state CLEAN or FLAG, and if flagged, provide a next action in `/namespace:skill` format. Then write the lifecycle marker:

> **[CONFIRMED]** — finding matches the draft prediction, or
> **[REVISED — reason]** — state what differed and why.

---

**CAUSAL GAP (analyze first)**

Using the census:

1. Direct mechanism: Do any census entries show artifact evidence that this feature causes the claimed outcome? Name specific census entries or name the gap if none exist. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Reference any census artifact that addresses this. If none exist, flag the inertia gap explicitly.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:prove-hypothesis` to generate mechanism evidence" or "Run `/signal:scout-inertia` to test the null-action alternative").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**SEQUENCE**

From the census: did discovery-namespace artifacts (discover, listen, signal) appear before specification-namespace artifacts (specify, govern)? Cite the census dates directly. No census date citation = no valid finding.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:scout-size` to build a discovery baseline before specifying").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

From the census: identify at least two artifacts and state whether they agree or contradict on a specific claim. Impressions without named census entries are not findings.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:discover-compare` to reconcile the contradiction").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

Apply the threshold from Step 2. From the census: list every artifact with a date older than the threshold. For each, note: is it the sole evidence for a key claim?

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:discover-competitors` to refresh the competitive signal").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 6 — Cross-dimension pattern**

If two or more dimensions are flagged, use the census and severity table to identify the root weakness. Name it explicitly — reference specific census gaps to ground the diagnosis. Do not recap the individual flags.

---

**STEP 7 — Final readiness summary**

Review the four per-dimension lifecycle markers. Write a consolidated readiness summary grounded in the census. If any dimension was REVISED, the summary must incorporate those revisions.

---

**STEP 8 — Namespace gap characterization**

Take every namespace with zero artifacts from the census. For each, characterize: is the absence expected at this topic's stage, or a notable blind spot? One sentence per namespace.

---

**Report structure:**
1. Evidence census matrix (Step 1 — shared reference for all findings)
2. Staleness threshold block (Step 2 — threshold and rationale declared together)
3. Internal severity table (Step 3 — bounded "INTERNAL ANALYSIS BLOCK", not a gate)
4. Draft readiness summary (Step 4 — marked DRAFT with per-dimension predictions)
5. CAUSAL GAP section (with CONFIRMED/REVISED marker)
6. SEQUENCE section (with CONFIRMED/REVISED marker)
7. COHERENCE section (with CONFIRMED/REVISED marker)
8. STALENESS section (with CONFIRMED/REVISED marker)
9. Cross-dimension pattern (if two or more flagged)
10. Final readiness summary (Step 7)
11. Namespace gap characterization (Step 8)

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.
