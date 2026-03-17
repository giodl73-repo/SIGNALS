Written to `simulations/quest/variations/signal-check-variations-R4-2026-03-17.md`.

---

## R4 Variations — Summary

| # | Axis | Single/Combo | Key target |
|---|------|-------------|------------|
| **V-01** | Inventory-depth-gated census | Single | C-17 — census matrix only when ≥2 namespaces or ≥3 artifacts; inline list for sparse inventories |
| **V-02** | Bidirectional register firewall | Single | C-16 sharpened — prohibition declared at block exit AND at coaching step entry |
| **V-03** | Template-slot lifecycle | Single | C-13 sharpened — each dimension embeds PREDICTION/ANALYSIS/RESOLUTION as grammar; deferral is structurally impossible |
| **V-04** | Census + register firewall | Combo | C-17 + C-16 sharpened — tests clean layering of both axes |
| **V-05** | Full v4 synthesis | Combo | All five: C-17 conditional census, C-16 bidirectional, C-13 template-slot, C-14 /namespace:skill, C-15 calibrated threshold |

**Key design choices:**

- **V-01 vs V-05 (R3):** R3's census was unconditional — always ran. V-01 adds a gate check after inventory collection. The census appears iff `namespaces ≥ 2 OR total artifacts ≥ 3`.

- **V-02's insight:** The v4 C-16 sharpening requires the prohibition to be visible at two sites — where the internal block closes ("tier labels end here") AND where the coaching narrative opens ("tier labels do not appear in this step or after"). One declaration is v3; two declarations, one at each boundary, is v4.

- **V-03's structural move:** Instead of instructing "place the marker immediately after," V-03 makes the per-dimension lifecycle a fixed named template (PREDICTION → Analysis → RESOLUTION). A section missing the RESOLUTION slot is incomplete by its own structure — not a behavioral deviation from a cross-cutting rule.

- **V-05 chain:** Census → severity table (with Pre-analysis expectation column) → PREDICTION slot (drawn explicitly from that column) → RESOLUTION at each production site. The evidentiary chain is explicit end-to-end. **This is the 100/100 candidate under v4.**
eatures simultaneously. The census populates the severity table; the severity table populates the PREDICTION slot; the PREDICTION is resolved at each dimension's RESOLUTION slot. The chain is explicit end-to-end.

**V-05 is the 100/100 candidate under v4.**

---

## V-01 — Axis: Inventory-Depth-Gated Census

**Hypothesis:** C-17 requires the census only when the inventory is non-trivial — defined as artifacts spanning ≥2 namespaces or ≥3 artifacts total. R3 V-05 ran the census unconditionally, which satisfies C-17 for non-trivial inventories but adds overhead for sparse ones. V-01 makes the gating explicit: the prompt checks inventory depth after collection and applies the full matrix only when warranted. Sparse inventories (1–2 artifacts total across all namespaces) skip the matrix and use an inline list. This makes C-17's conditional pass condition structurally verifiable and prevents the census from becoming boilerplate overhead on thin topics.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register throughout — surface observations, suggest next steps, let the team decide. Do not block or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date (from filename or frontmatter). List all artifacts found.

---

**STEP 2 — Evidence census (inventory-depth-gated)**

Count total artifacts found and the number of distinct namespaces with at least one artifact.

**Gate check:**
- Artifacts span **2 or more namespaces**, OR **total artifact count ≥ 3** → build the census matrix.
- Total artifact count is **1 or 2 across all namespaces** → inline list only (census matrix exempt).

**Census matrix (when gate condition is met):**

| Namespace | Artifacts present | Dates | Count |
|-----------|-------------------|-------|-------|
| scout     | [list] or none    | ...   | n     |
| draft     | [list] or none    | ...   | n     |
| review    | [list] or none    | ...   | n     |
| flow      | [list] or none    | ...   | n     |
| trace     | [list] or none    | ...   | n     |
| prove     | [list] or none    | ...   | n     |
| listen    | [list] or none    | ...   | n     |
| program   | [list] or none    | ...   | n     |
| topic     | [list] or none    | ...   | n     |

After the matrix: state total artifact count, date range (oldest to newest), namespaces with zero artifacts.

The census is the shared reference for all dimension findings below. Dimension sections cite census entries directly.

**Inline list (when gate condition is NOT met):**

- `[artifact-name]` — namespace: X — date: YYYY-MM-DD

(Census matrix not required for inventories with 1–2 total artifacts.)

---

**STEP 3 — Staleness calibration with decision-velocity rationale**

Examine the inventory or census. If any artifact is competitive or market-facing (listen namespace, or filename containing "competitor" or "market"):

> **Threshold: 14 days**
> **Calibration rationale:** Inventory contains competitive or market signals, which track a moving landscape. Competitive positioning changes faster than structural signals (size, feasibility) — decisions on stale competitive data carry higher risk because the competitive environment can shift within days. 14 days reflects this higher decision velocity.

Otherwise:

> **Threshold: 30 days**
> **Calibration rationale:** No competitive or market signals in inventory. Evidence types present have lower time-sensitivity — they reflect stable structural facts rather than moving dynamics. 30 days is proportionate to the decision velocity at this topic stage.

---

**STEP 4 — Internal severity table**

Before writing any team-facing narrative, populate this internal analysis table.

> **--- INTERNAL ANALYSIS BLOCK ---**
> **Severity ratings below are for your analytical reference only — they are not team-facing output and not blocking gates.**
> **The coaching narrative in Step 6 is what the team reads.**
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

Severity labels from this block do not appear in the narrative below.

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 5 — Draft readiness summary (before analysis)**

Based on the census or inline list and the internal severity table, write a 2–3 sentence draft readiness assessment. State which dimensions you expect to confirm clean and which to flag. Mark it:

> **[DRAFT — to be confirmed or revised per dimension below]**

For each dimension, state the pre-analysis prediction:
- CAUSAL GAP: CLEAN or FLAG?
- SEQUENCE: CLEAN or FLAG?
- COHERENCE: CLEAN or FLAG?
- STALENESS: CLEAN or FLAG?

These predictions are what each dimension's inline lifecycle marker resolves.

---

**STEP 6 — Dimension analysis**

Analyze in this order. For each: write the finding with artifact evidence (cite census entries by name when a census matrix was built), state CLEAN or FLAG, and if flagged, provide at least one next action in `/namespace:skill` format. Immediately after each dimension's conclusion — before the next dimension begins — write the inline lifecycle marker:

> **[CONFIRMED]** — finding matches the Step 5 prediction for this dimension, or
> **[REVISED — reason]** — state what differed and why.

---

**CAUSAL GAP (analyze first)**

Two required sub-questions — both must be answered:

1. Direct mechanism: Is there artifact evidence (in the census or inventory) that this feature causes the claimed outcome? Name specific artifacts if present; name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly even if the mechanism question looks clean.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:scout-inertia` to test whether the current approach already satisfies this need" or "Run `/signal:prove-hypothesis` to establish the causal link").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**SEQUENCE**

Did discovery-type signals (scout, listen, prove namespaces) predate specification-type signals (draft, program namespaces)? Cite specific artifact dates or filename order. A SEQUENCE claim without artifact citation is not valid.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:scout-size` to establish a discovery baseline before advancing draft work").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

Name at least two specific artifacts and state whether they agree or contradict on a specific claim. Impressions without named signal pairs are not findings.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:discover-compare` to reconcile the conflicting signals").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

Apply the threshold from Step 3 — state it again here: **[X days]** (because [one-phrase rationale recap]). List every artifact older than this threshold by name. For each, note whether it is the sole evidence for a key claim — that matters more than age alone.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:discover-competitors` to update the competitive landscape").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 7 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness they share. Name it explicitly. Do not recap the individual flags.

---

**STEP 8 — Final readiness summary**

Review the four per-dimension lifecycle markers. Write a consolidated readiness summary that reflects the full analysis. If any dimension was REVISED, the summary must incorporate those revisions — it cannot repeat the Step 5 draft verbatim.

---

**STEP 9 — Namespace gap characterization**

List every namespace with no artifact. For each, characterize: expected at this topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Evidence census matrix (Step 2 — conditional on inventory depth) or inline artifact list
2. Staleness threshold block (Step 3 — threshold and calibration rationale declared together)
3. Internal severity table (Step 4 — bounded INTERNAL ANALYSIS BLOCK, not a gate)
4. Draft readiness summary (Step 5 — marked DRAFT with per-dimension predictions)
5. CAUSAL GAP section (with CONFIRMED/REVISED marker)
6. SEQUENCE section (with CONFIRMED/REVISED marker)
7. COHERENCE section (with CONFIRMED/REVISED marker)
8. STALENESS section (with CONFIRMED/REVISED marker, threshold restated)
9. Cross-dimension pattern (if two or more flagged)
10. Final readiness summary
11. Namespace gap characterization

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-02 — Axis: Bidirectional Register Firewall

**Hypothesis:** R3 V-04's C-16 enforcement was unidirectional — "severity labels from this block do not appear in the narrative below" was declared once, at the close of the INTERNAL ANALYSIS BLOCK. v4 sharpens C-16: the prohibition must be enforced throughout the full report, not only at the tier definition. V-02 makes the enforcement bidirectional by adding a second declaration at the coaching narrative step header — before writing any coaching section, the prompt explicitly states that severity tier labels do not appear here. The architectural separation is enforced at both production sites: the block exit and the coaching entry. Neither declaration alone satisfies v4; both together make the register boundary live at every transition point across the full report.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register throughout — surface observations, name next steps, let the team decide. Do not block the team or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date (from filename or frontmatter). List all artifacts found.

---

**STEP 2 — Staleness calibration with decision-velocity rationale**

Examine the inventory. If any artifact is competitive or market-facing (listen namespace, or filename containing "competitor" or "market"):

> **Threshold: 14 days**
> **Calibration rationale:** Inventory contains competitive or market signals, which track a moving landscape. Competitive positioning changes faster than structural signals (size, feasibility) — decisions on stale competitive data carry higher risk because the competitive environment can shift within days. 14 days reflects this higher decision velocity.

Otherwise:

> **Threshold: 30 days**
> **Calibration rationale:** No competitive or market signals in inventory. Evidence types present have lower time-sensitivity — they reflect stable structural facts rather than moving dynamics. 30 days is proportionate to the decision velocity at this topic stage.

Declare the threshold and rationale as a labeled block before proceeding.

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

> **The tier labels defined above (clean / gap / concern) do not cross into the coaching narrative.**
> **Their analytical role ends at this block boundary. The coaching step begins below.**

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 4 — Draft readiness summary (before analysis)**

Based on the inventory and the internal severity table, write a 2–3 sentence draft readiness assessment. State which dimensions you expect to confirm clean and which to flag. Mark it:

> **[DRAFT — to be confirmed or revised per dimension below]**

---

**STEP 5 — Dimension narrative (coaching register)**

> **Register notice — this step is team-facing coaching only.**
> **Severity tier labels (clean / gap / concern) from the INTERNAL ANALYSIS BLOCK do not appear in this step or anywhere after it.**
> **Translate severity findings into observation language: describe what you see in the evidence, not what tier you assigned it.**

Analyze in this order. For each: write the finding with artifact evidence, state CLEAN or FLAG as the dimension's outcome, and if flagged, provide at least one next action in `/namespace:skill` format. Immediately after each dimension's conclusion — before the next dimension begins — write the inline lifecycle marker:

> **[CONFIRMED]** — finding matches the Step 4 draft prediction for this dimension, or
> **[REVISED — reason]** — state what differed and why.

---

**CAUSAL GAP (analyze first)**

*Coaching narrative — observation language only.*

Two required sub-questions — both must be answered:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome? Name specific artifacts if present; name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly even if the mechanism question looks clean.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:scout-inertia` to test whether the current approach already satisfies this need" or "Run `/signal:prove-hypothesis` to establish the causal link").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**SEQUENCE**

*Coaching narrative — observation language only.*

Did discovery-type signals (scout, listen, prove namespaces) predate specification-type signals (draft, program namespaces)? Cite specific artifact dates or filename order. A SEQUENCE claim without artifact citation is not valid.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:scout-size` to establish a discovery baseline before advancing draft artifacts").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

*Coaching narrative — observation language only.*

Name at least two specific artifacts and state whether they agree or contradict on a specific claim. Impressions without named signal pairs are not findings.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:discover-compare` to reconcile the conflicting signals").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

*Coaching narrative — observation language only.*

Apply the threshold from Step 2 — state it again here: **[X days]** (because [one-phrase rationale recap]). List every artifact older than this threshold by name. For each, note whether it is the sole evidence for a key claim.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:discover-competitors` to refresh the competitive landscape").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 6 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness they share. Name it explicitly. Do not recap the individual flags.

---

**STEP 7 — Final readiness summary**

Review the four per-dimension lifecycle markers. Write a consolidated readiness summary that reflects the full analysis. If any dimension was REVISED, the summary must incorporate those revisions.

---

**STEP 8 — Missing namespace inventory**

List every namespace with no artifact. For each, characterize: expected at this topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Staleness threshold block (Step 2 — threshold and calibration rationale declared together)
2. Internal severity table (Step 3 — bounded INTERNAL ANALYSIS BLOCK with explicit exit declaration)
3. Draft readiness summary (Step 4 — marked DRAFT)
4. Register notice (Step 5 header — team-facing coaching only, tier labels prohibited)
5. CAUSAL GAP section — coaching narrative (with CONFIRMED/REVISED marker)
6. SEQUENCE section — coaching narrative (with CONFIRMED/REVISED marker)
7. COHERENCE section — coaching narrative (with CONFIRMED/REVISED marker)
8. STALENESS section — coaching narrative (with CONFIRMED/REVISED marker, threshold restated)
9. Cross-dimension pattern (if two or more flagged)
10. Final readiness summary
11. Missing namespace inventory

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-03 — Axis: Template-Slot Lifecycle

**Hypothesis:** v4 sharpens C-13 by explicitly declaring that "a single overall CONFIRMED/REVISED check appended after all dimensions = fail." R3 V-04's language ("immediately after each dimension's conclusion — before the next dimension begins") is correct but instructional — it tells the model where to place the marker without making the placement structurally enforced. V-03 embeds the lifecycle as a fixed three-part template slot within each dimension section: PREDICTION (drawn from the severity table, declared before the analysis) → Analysis (coaching narrative) → RESOLUTION (CONFIRMED or REVISED, placed immediately after). Deferral becomes structurally impossible: a dimension section with a missing PREDICTION or RESOLUTION slot is incomplete by grammar, not merely by instruction. The link between the severity table, the per-dimension prediction, and the per-dimension resolution is made explicit at the section level.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register throughout — surface observations, suggest next steps, let the team decide. Do not block the team or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date (from filename or frontmatter). List all artifacts found.

---

**STEP 2 — Staleness calibration with decision-velocity rationale**

Examine the inventory. If any artifact is competitive or market-facing (listen namespace, or filename containing "competitor" or "market"):

> **Threshold: 14 days**
> **Calibration rationale:** Inventory contains competitive or market signals, which track a moving landscape. Competitive positioning changes faster than structural signals (size, feasibility) — decisions on stale competitive data carry higher risk because the competitive environment can shift within days. 14 days reflects this higher decision velocity.

Otherwise:

> **Threshold: 30 days**
> **Calibration rationale:** No competitive or market signals in inventory. Evidence types present have lower time-sensitivity — they reflect stable structural facts rather than moving dynamics. 30 days is proportionate to the decision velocity at this topic stage.

---

**STEP 3 — Internal severity table**

Before writing any team-facing narrative, populate this internal analysis table.

> **--- INTERNAL ANALYSIS BLOCK ---**
> **Severity ratings below are for your analytical reference only — they are not team-facing output and not blocking gates.**
> **The coaching narrative in Step 5 is what the team reads.**
> **The PREDICTION slot in each dimension section below draws directly from this table.**

| Dimension | Severity (internal) | Evidence summary |
|-----------|---------------------|------------------|
| CAUSAL GAP | clean / gap / concern | ... |
| SEQUENCE | clean / gap / concern | ... |
| COHERENCE | clean / gap / concern | ... |
| STALENESS | clean / gap / concern | ... |

**Severity definitions — internal reference only:**
- **clean** — evidence is present and sufficient
- **gap** — evidence is missing or thin; addressable before commitment
- **concern** — evidence is absent in a high-stakes area; explicit team discussion warranted

Severity labels from this block do not appear in the narrative below.

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 4 — Draft readiness summary (before analysis)**

Based on the inventory and severity table, write a 2–3 sentence draft readiness assessment. Mark it:

> **[DRAFT — to be confirmed or revised per dimension below]**

---

**STEP 5 — Dimension lifecycle**

Each dimension below follows a fixed three-part structure. Complete all three parts in sequence — do not omit any:

```
[PREDICTION]  — declared before the analysis, drawn from the severity table
[ANALYSIS]    — coaching narrative with artifact evidence and CLEAN/FLAG outcome
[RESOLUTION]  — CONFIRMED or REVISED, placed immediately after the analysis ends
```

The RESOLUTION for each dimension must appear at that dimension's production site — before the next dimension begins. Post-hoc assembly of resolutions after all four dimensions is not valid.

---

**CAUSAL GAP (analyze first)**

> **[PREDICTION]** — From Step 3 severity table: expect CLEAN or FLAG? (State the severity rating's implication in one phrase.)

*Analysis:*

Two required sub-questions — both must be answered:

1. Direct mechanism: Is there artifact evidence that this feature causes the claimed outcome? Name specific artifacts if present; name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly even if the mechanism question looks clean.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:scout-inertia` to test whether the current approach already satisfies this need" or "Run `/signal:prove-hypothesis` to establish the causal link").

> **[RESOLUTION]** — **[CONFIRMED]** (prediction held) or **[REVISED — reason]** (state what differed and why)

---

**SEQUENCE**

> **[PREDICTION]** — From Step 3 severity table: expect CLEAN or FLAG?

*Analysis:*

Did discovery-type signals (scout, listen, prove namespaces) predate specification-type signals (draft, program namespaces)? Cite specific artifact dates or filename order. A SEQUENCE claim without artifact citation is not valid.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:scout-size` to establish a discovery baseline before advancing draft artifacts").

> **[RESOLUTION]** — **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

> **[PREDICTION]** — From Step 3 severity table: expect CLEAN or FLAG?

*Analysis:*

Name at least two specific artifacts and state whether they agree or contradict on a specific claim. Impressions without named signal pairs are not findings.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:discover-compare` to reconcile the conflicting signals").

> **[RESOLUTION]** — **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

> **[PREDICTION]** — From Step 3 severity table: expect CLEAN or FLAG?

*Analysis:*

Apply the threshold from Step 2 — state it here: **[X days]** (because [one-phrase rationale recap]). List every artifact older than this threshold by name. For each, note whether it is the sole evidence for a key claim.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:discover-competitors` to refresh the competitive landscape").

> **[RESOLUTION]** — **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 6 — Readiness summary**

Review the four RESOLUTION markers. Write a 3–4 sentence readiness summary grounded in the resolutions. If any dimension was REVISED, the summary must incorporate those revisions.

---

**STEP 7 — Cross-dimension pattern**

If two or more dimensions were flagged, identify the root weakness they share. Name it explicitly. Do not recap the individual flags.

---

**STEP 8 — Missing namespace inventory**

List every namespace with no artifact. For each, characterize: expected at this topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Staleness threshold block (Step 2 — threshold and calibration rationale declared together)
2. Internal severity table (Step 3 — bounded INTERNAL ANALYSIS BLOCK, not a gate)
3. Draft readiness summary (Step 4 — marked DRAFT)
4. CAUSAL GAP section — [PREDICTION] / Analysis / [RESOLUTION]
5. SEQUENCE section — [PREDICTION] / Analysis / [RESOLUTION]
6. COHERENCE section — [PREDICTION] / Analysis / [RESOLUTION]
7. STALENESS section — [PREDICTION] / Analysis / [RESOLUTION], threshold restated
8. Readiness summary (Step 6)
9. Cross-dimension pattern (if two or more flagged)
10. Missing namespace inventory

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-04 — Combo: Conditional Census + Bidirectional Register Firewall

**Hypothesis:** V-01's conditional census and V-02's bidirectional register firewall are independent structural additions. V-04 tests whether they layer cleanly — specifically, whether the census matrix (pre-analysis, gated on inventory depth) and the bidirectional prohibition (declared at block exit in Step 4 and at coaching entry in Step 6) create coherent report structure without visual noise or redundancy. The census provides the evidentiary foundation; the register firewall enforces clean separation between internal analysis and team-facing narrative. Both must operate simultaneously in a single report. If the combo is visually noisy or structurally awkward, V-05 will need to absorb it differently.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register throughout — surface observations, name next steps, let the team decide. Do not block the team or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date (from filename or frontmatter). List all artifacts found.

---

**STEP 2 — Evidence census (inventory-depth-gated)**

Count total artifacts found and the number of distinct namespaces with at least one artifact.

**Gate check:**
- Artifacts span **2 or more namespaces**, OR **total artifact count ≥ 3** → build the census matrix.
- Total artifact count is **1 or 2 across all namespaces** → inline list only (census matrix exempt).

**Census matrix (when gate condition is met):**

| Namespace | Artifacts present | Dates | Count |
|-----------|-------------------|-------|-------|
| scout     | [list] or none    | ...   | n     |
| draft     | [list] or none    | ...   | n     |
| review    | [list] or none    | ...   | n     |
| flow      | [list] or none    | ...   | n     |
| trace     | [list] or none    | ...   | n     |
| prove     | [list] or none    | ...   | n     |
| listen    | [list] or none    | ...   | n     |
| program   | [list] or none    | ...   | n     |
| topic     | [list] or none    | ...   | n     |

After the matrix: state total artifact count, date range, namespaces with zero artifacts.

The census is the shared reference for all dimension findings below. Dimension sections cite census entries directly.

**Inline list (when gate condition is NOT met):**

- `[artifact-name]` — namespace: X — date: YYYY-MM-DD

---

**STEP 3 — Staleness calibration with decision-velocity rationale**

Examine the census or inventory. If any artifact is competitive or market-facing (listen namespace, or filename containing "competitor" or "market"):

> **Threshold: 14 days**
> **Calibration rationale:** Inventory contains competitive or market signals, which track a moving landscape. Competitive positioning changes faster than structural signals (size, feasibility) — decisions on stale competitive data carry higher risk because the competitive environment can shift within days. 14 days reflects this higher decision velocity.

Otherwise:

> **Threshold: 30 days**
> **Calibration rationale:** No competitive or market signals in inventory. Evidence types present have lower time-sensitivity — they reflect stable structural facts rather than moving dynamics. 30 days is proportionate to the decision velocity at this topic stage.

---

**STEP 4 — Internal severity table**

Before writing any team-facing narrative, populate this internal analysis table from the census or inventory.

> **--- INTERNAL ANALYSIS BLOCK ---**
> **Severity ratings below are for your analytical reference only — they are not team-facing output and not blocking gates.**
> **The coaching narrative in Step 6 is what the team reads.**
> **This table structures your analysis before you write it.**

| Dimension | Severity (internal) | Census/inventory evidence summary | Pre-analysis expectation |
|-----------|---------------------|------------------------------------|--------------------------|
| CAUSAL GAP | clean / gap / concern | [key entries] | CLEAN / FLAG |
| SEQUENCE | clean / gap / concern | [key entries] | CLEAN / FLAG |
| COHERENCE | clean / gap / concern | [key entries] | CLEAN / FLAG |
| STALENESS | clean / gap / concern | [key entries] | CLEAN / FLAG |

**Severity definitions — internal reference only:**
- **clean** — evidence is present and sufficient
- **gap** — evidence is missing or thin; addressable before commitment
- **concern** — evidence is absent in a high-stakes area; explicit team discussion warranted

> **The tier labels (clean / gap / concern) end here.**
> **They informed your analysis above and do not cross into the coaching narrative below.**

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 5 — Draft readiness summary (before analysis)**

Based on the census or inventory and the internal severity table, write a 2–3 sentence draft readiness assessment. State which dimensions you expect to confirm clean and which to flag. Mark it:

> **[DRAFT — to be confirmed or revised per dimension below]**

For each dimension, state the pre-analysis prediction:
- CAUSAL GAP: CLEAN or FLAG?
- SEQUENCE: CLEAN or FLAG?
- COHERENCE: CLEAN or FLAG?
- STALENESS: CLEAN or FLAG?

---

**STEP 6 — Dimension narrative (coaching register)**

> **Register notice — this step is team-facing coaching only.**
> **Severity tier labels (clean / gap / concern) do not appear in this step or anywhere after it.**
> **Translate internal findings into observation language: describe the evidence, not the tier.**

Analyze in this order. For each: write the finding with artifact evidence (cite census entries by name when a matrix was built), state CLEAN or FLAG, and if flagged, provide at least one next action in `/namespace:skill` format. Immediately after each dimension's conclusion — before the next dimension begins — write the inline lifecycle marker:

> **[CONFIRMED]** — finding matches the Step 5 prediction for this dimension, or
> **[REVISED — reason]** — state what differed and why.

---

**CAUSAL GAP (analyze first)**

*Coaching narrative — observation language only.*

Two required sub-questions — both must be answered:

1. Direct mechanism: Is there artifact evidence (in the census or inventory) that this feature causes the claimed outcome? Name specific entries if present; name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? Cite any artifact addressing this. If none exist, flag the inertia gap explicitly even if the mechanism question looks clean.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:scout-inertia` to test whether the current approach already satisfies this need" or "Run `/signal:prove-hypothesis` to establish the causal link").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**SEQUENCE**

*Coaching narrative — observation language only.*

From the census or inventory: did discovery-namespace artifacts (scout, listen, prove) appear before specification-namespace artifacts (draft, program)? Cite artifact dates or filename order directly. No citation = no valid finding.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:scout-size` to establish a discovery baseline before advancing draft artifacts").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

*Coaching narrative — observation language only.*

From the census or inventory: identify at least two artifacts and state whether they agree or contradict on a specific claim. Impressions without named pairs are not findings.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:discover-compare` to reconcile the conflicting signals").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

*Coaching narrative — observation language only.*

Apply the threshold from Step 3 — state it here: **[X days]** (because [one-phrase rationale recap]). List every artifact older than the threshold by name. For each, note whether it is the sole evidence for a key claim.

State CLEAN or FLAG. If flagged, name a next action (e.g., "Run `/signal:discover-competitors` to refresh the competitive landscape").

> **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 7 — Cross-dimension pattern**

If two or more dimensions are flagged, identify the root weakness they share. Name it explicitly — reference specific census or inventory gaps to ground the diagnosis. Do not recap the individual flags.

---

**STEP 8 — Final readiness summary**

Review the four per-dimension lifecycle markers. Write a consolidated readiness summary. If any dimension was REVISED, the summary must incorporate those revisions.

---

**STEP 9 — Namespace gap characterization**

Take every namespace with zero artifacts from the census or inventory. For each, characterize: expected at this topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Evidence census matrix (Step 2 — conditional on inventory depth) or inline artifact list
2. Staleness threshold block (Step 3 — threshold and calibration rationale declared together)
3. Internal severity table (Step 4 — bounded INTERNAL ANALYSIS BLOCK, cross-step prohibition declared at block exit)
4. Draft readiness summary (Step 5 — marked DRAFT with per-dimension predictions)
5. Register notice (Step 6 header)
6. CAUSAL GAP section — coaching narrative (with CONFIRMED/REVISED marker)
7. SEQUENCE section — coaching narrative (with CONFIRMED/REVISED marker)
8. COHERENCE section — coaching narrative (with CONFIRMED/REVISED marker)
9. STALENESS section — coaching narrative (with CONFIRMED/REVISED marker, threshold restated)
10. Cross-dimension pattern (if two or more flagged)
11. Final readiness summary
12. Namespace gap characterization

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.

---

## V-05 — Full v4 Synthesis

**Hypothesis:** The synthesis variation for v4. Combines all five criteria that must simultaneously pass for a clean 100/100 under v4: conditional census gated by inventory depth (C-17), bidirectional register firewall with prohibition at block exit and coaching entry (C-16 sharpened), template-slot lifecycle with PREDICTION/ANALYSIS/RESOLUTION embedded in each dimension section grammar (C-13 sharpened), `/namespace:skill` command format for all next actions (C-14), and calibrated staleness threshold with decision-velocity mechanism (C-15). Builds on R3 V-04's baseline (the v3 100/100 synthesis) and adds the three new v4 axes. The severity table now populates both the PRE-ANALYSIS EXPECTATION column (feeding the PREDICTION slot in each dimension) and the census grounds the severity assessment — the evidentiary chain from inventory to severity to prediction to resolution is continuous and explicit at every step.

---

You are running `/signal:check` for the topic: **{topic}**

Coaching register throughout — surface observations, name next steps, let the team decide. Do not block the team or render verdicts.

---

**STEP 1 — Inventory**

Use Glob and Read to find every signal artifact under `simulations/` for this topic. Record each: namespace, skill name, creation date (from filename or frontmatter). List all artifacts found.

---

**STEP 2 — Evidence census (inventory-depth-gated)**

Count total artifacts found and the number of distinct namespaces with at least one artifact.

**Gate check:**
- Artifacts span **2 or more namespaces**, OR **total artifact count ≥ 3** → build the census matrix.
- Total artifact count is **1 or 2 across all namespaces** → inline list only (census matrix exempt).

**Census matrix (when gate condition is met):**

| Namespace | Artifacts present | Dates | Count |
|-----------|-------------------|-------|-------|
| scout     | [list] or none    | ...   | n     |
| draft     | [list] or none    | ...   | n     |
| review    | [list] or none    | ...   | n     |
| flow      | [list] or none    | ...   | n     |
| trace     | [list] or none    | ...   | n     |
| prove     | [list] or none    | ...   | n     |
| listen    | [list] or none    | ...   | n     |
| program   | [list] or none    | ...   | n     |
| topic     | [list] or none    | ...   | n     |

After the matrix: state total artifact count, date range (oldest to newest), namespaces with zero artifacts.

The census is the shared reference for all dimension findings below. Dimension sections cite census entries directly.

**Inline list (when gate condition is NOT met):**

- `[artifact-name]` — namespace: X — date: YYYY-MM-DD

---

**STEP 3 — Staleness calibration with decision-velocity rationale**

Examine the census or inventory. If any artifact is competitive or market-facing (listen namespace, or filename containing "competitor" or "market"):

> **Threshold: 14 days**
> **Calibration rationale:** Inventory contains competitive or market signals, which track a moving landscape. Competitive positioning changes faster than structural signals (size, feasibility) — decisions on stale competitive data carry higher risk because the competitive environment can shift within days. 14 days reflects this higher decision velocity.

Otherwise:

> **Threshold: 30 days**
> **Calibration rationale:** No competitive or market signals in inventory. Evidence types present have lower time-sensitivity — they reflect stable structural facts rather than moving dynamics. 30 days is proportionate to the decision velocity at this topic stage.

Declare the threshold and full rationale together as a labeled block before proceeding.

---

**STEP 4 — Internal severity table**

Before writing any team-facing narrative, populate this internal analysis table from the census or inventory.

> **--- INTERNAL ANALYSIS BLOCK ---**
> **Severity ratings below are for your analytical reference only — they are not team-facing output and not blocking gates.**
> **The coaching narrative in Step 6 is what the team reads.**
> **The PREDICTION slot in each dimension section draws directly from the Pre-analysis expectation column.**

| Dimension | Severity (internal) | Census/inventory evidence | Pre-analysis expectation |
|-----------|---------------------|---------------------------|--------------------------|
| CAUSAL GAP | clean / gap / concern | [key census or inventory entries] | CLEAN / FLAG |
| SEQUENCE | clean / gap / concern | [key census or inventory entries] | CLEAN / FLAG |
| COHERENCE | clean / gap / concern | [key census or inventory entries] | CLEAN / FLAG |
| STALENESS | clean / gap / concern | [key census or inventory entries] | CLEAN / FLAG |

**Severity definitions — internal reference only:**
- **clean** — evidence is present and sufficient
- **gap** — evidence is missing or thin; addressable before commitment
- **concern** — evidence is absent in a high-stakes area; explicit team discussion warranted

> **The tier labels (clean / gap / concern) end here.**
> **They inform the PREDICTION slot in each dimension section and do not cross into the coaching narrative.**

> **--- END INTERNAL ANALYSIS BLOCK ---**

---

**STEP 5 — Draft readiness summary (before analysis)**

Based on the census or inventory and the internal severity table, write a 2–3 sentence draft readiness assessment. Mark it:

> **[DRAFT — census-derived, to be confirmed or revised per dimension below]**

---

**STEP 6 — Dimension analysis**

Each dimension follows a fixed three-part structure: PREDICTION → Coaching narrative → RESOLUTION.

> **Register notice — the coaching narrative in each section is team-facing only.**
> **Severity tier labels (clean / gap / concern) do not appear in any coaching narrative section or anywhere after this notice.**
> **Translate internal findings into observation language: describe what the evidence shows, not what tier you assigned.**

The PREDICTION slot is drawn from the Pre-analysis expectation column in Step 4. The RESOLUTION slot is the per-dimension lifecycle marker — it must appear immediately after the analysis ends, before the next dimension begins. Post-hoc assembly of resolutions after all dimensions is not valid.

---

**CAUSAL GAP (analyze first)**

> **[PREDICTION]** — From Step 4 Pre-analysis expectation: CLEAN or FLAG? (State what the severity assessment implies in one phrase.)

*Coaching narrative — observation language only:*

This is the highest-stakes dimension. Two required sub-questions — both must be answered:

1. Direct mechanism: Is there artifact evidence (in the census or inventory) that this feature causes the claimed outcome? Name specific entries if present; name the gap if not. Do not restate the hypothesis.

2. Inertia check: Would doing nothing — or the current approach without this feature — also produce the claimed outcome? This is the question teams most commonly skip. Cite any artifact addressing this. If none exist, flag the inertia gap explicitly even if the mechanism question looks clean.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:scout-inertia` to test whether the current approach already satisfies this need" or "Run `/signal:prove-hypothesis` to establish the causal link").

> **[RESOLUTION]** — **[CONFIRMED]** (prediction held) or **[REVISED — reason]** (state what differed and why)

---

**SEQUENCE**

> **[PREDICTION]** — From Step 4 Pre-analysis expectation: CLEAN or FLAG?

*Coaching narrative — observation language only:*

From the census or inventory: did discovery-namespace artifacts (scout, listen, prove) predate specification-namespace artifacts (draft, program)? Cite artifact dates or filename order directly. No citation = no valid finding.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:scout-size` to establish a discovery baseline before advancing draft artifacts").

> **[RESOLUTION]** — **[CONFIRMED]** or **[REVISED — reason]**

---

**COHERENCE**

> **[PREDICTION]** — From Step 4 Pre-analysis expectation: CLEAN or FLAG?

*Coaching narrative — observation language only:*

From the census or inventory: identify at least two specific artifacts and state whether they agree or contradict on a specific claim. Impressions without named signal pairs are not findings.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:discover-compare` to reconcile the conflicting signals").

> **[RESOLUTION]** — **[CONFIRMED]** or **[REVISED — reason]**

---

**STALENESS**

> **[PREDICTION]** — From Step 4 Pre-analysis expectation: CLEAN or FLAG?

*Coaching narrative — observation language only:*

Apply the threshold from Step 3 — state it here: **[X days]** (because [one-phrase rationale recap]). List every artifact older than this threshold by name. For each, note whether it is the sole evidence for a key claim — that matters more than age alone.

State CLEAN or FLAG. If flagged, name a next action in `/namespace:skill` format (e.g., "Run `/signal:discover-competitors` to refresh the competitive landscape").

> **[RESOLUTION]** — **[CONFIRMED]** or **[REVISED — reason]**

---

**STEP 7 — Cross-dimension pattern**

If two or more dimensions were flagged, identify the root weakness they share. Name it explicitly — reference specific census or inventory gaps to ground the diagnosis. Example: "CAUSAL GAP and SEQUENCE both trace to a single root: the topic has size signals but no mechanism evidence — no prove or validate artifacts exist across any namespace." Do not recap the individual flags.

---

**STEP 8 — Final readiness summary**

Review the four per-dimension RESOLUTION markers. Write a consolidated readiness summary that reflects the full analysis. If any dimension was REVISED, the summary must incorporate those revisions — it cannot repeat the Step 5 draft verbatim.

---

**STEP 9 — Namespace gap characterization**

Take every namespace with zero artifacts from the census or inventory. For each, characterize: expected at this topic's stage, or a meaningful blind spot? One sentence per namespace.

---

**Report structure:**
1. Evidence census matrix (Step 2 — conditional on inventory depth) or inline artifact list
2. Staleness threshold block (Step 3 — threshold and calibration rationale declared together)
3. Internal severity table (Step 4 — bounded INTERNAL ANALYSIS BLOCK; tier labels end at block exit)
4. Draft readiness summary (Step 5 — marked DRAFT, census-derived)
5. Register notice (Step 6 header — coaching only, tier labels prohibited throughout)
6. CAUSAL GAP section — [PREDICTION] / coaching narrative / [RESOLUTION]
7. SEQUENCE section — [PREDICTION] / coaching narrative / [RESOLUTION]
8. COHERENCE section — [PREDICTION] / coaching narrative / [RESOLUTION]
9. STALENESS section — [PREDICTION] / coaching narrative / [RESOLUTION], threshold restated
10. Cross-dimension pattern (if two or more flagged)
11. Final readiness summary
12. Namespace gap characterization

Format: Markdown. Save to `simulations/signal/check/{topic}-check-{date}.md`.
