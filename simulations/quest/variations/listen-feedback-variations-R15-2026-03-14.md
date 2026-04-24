Now I have everything I need. R14 confirmed:
- A-24 (named sub-field cross-refs): V-01/V-04/V-05 PASS, V-02/V-03 PARTIAL
- A-25 (epistemic rationale): V-03/V-05 PASS, others PARTIAL
- A-26 (numbered aggregate manifest): V-02/V-04/V-05 structural bonus, not yet a scored criterion

R15 variation axes: isolate each new criterion as a single axis, then combine.

---

# listen-feedback — Round 15 Variations

**Single-axis mapping:**
- V-01: A-24 alone (named sub-field cross-refs in gains/losses; no A-25 rationale; no A-26 numbering)
- V-02: A-25 alone (explicit epistemic rationale; no A-24 cross-refs; no A-26 numbering)
- V-03: A-26 alone (numbered aggregate manifest; no A-24 cross-refs; no A-25 rationale)
- V-04: A-24 + A-25 combined (no A-26)
- V-05: A-24 + A-25 + A-26 combined + coaching language (seeds A-27)

---

## V-01 — Axis: A-24 (Named Sub-Field Cross-References in Gains/Losses Instructions)

**Hypothesis:** Naming specific Step 0 sub-fields by label inside the `Gains from this spec:` and `Losses and switching costs:` field instructions converts bilateral coverage from an output property into a structural dependency. An evaluator who follows the instruction cannot omit the loss side without also omitting the named Step 0 sub-field reference — making non-compliance visible by inspection rather than inferred from prose.

---

You are running the **listen-feedback** skill.

**Task:** Simulate customer reactions to the provided spec before it ships. Produce 12 per-persona feedback cards (C-01 through C-12), UX and PM professional lens syntheses, aggregate NPS analysis, a cross-persona theme matrix, and a prioritized revision plan.

**Output sections in order:**
1. Step 0 — Inertia Baseline
2. Step 1 — 12 Persona Cards (ascending NPS order)
3. Step 2 — Professional Lenses (UX Read, then PM Read)
4. Step 3 — Aggregate Section
5. Step 4 — Cross-Persona Theme Matrix
6. Step 5 — Revision Synthesis

---

### Step 0 — Inertia Baseline

Before simulating any persona, characterize the status quo this spec competes against. Complete all four sub-fields. These sub-field labels are referenced by name in the persona card instructions below.

**Sub-field 1 — Status quo name:** The specific tool, workflow, or practice this spec displaces. One noun phrase.

**Sub-field 2 — What it delivers:** The value the status quo currently provides to personas. One sentence stating what the existing approach does well enough to retain adoption.

**Sub-field 3 — Where it falls short:** The gap or failure mode in the status quo that motivates this spec. One to two sentences naming what the current approach cannot do or does poorly.

**Sub-field 4 — Floor-level switching cost:** The minimum friction any persona faces to abandon the status quo and adopt this spec. One sentence describing the irreducible adoption burden (data migration, workflow retraining, tooling replacement, etc.).

---

### Step 1 — 12 Persona Cards

Simulate all 12 customer personas (C-01 through C-12). Determine each persona's predicted NPS score before writing the card, then output all 12 cards in **ascending NPS order** (lowest score first, highest last). Ties may appear in any order within their score tier.

Each card uses the following **numbered field manifest**. All 11 fields are required in every card. No field may be omitted for any persona, including Promoter-tier personas. Fields must appear in this exact order.

**Card header:** `### [C-XX — Name — Role]`
The header contains only persona ID, name, and role. No summary or intro line precedes Field 1.

---

**Field 1 — Current approach:** What this persona does today without this spec. One to two sentences describing their actual workflow or behavior. Populate even when no equivalent workflow exists: "No current equivalent — this capability is new to this persona."

**Field 2 — Gains from this spec:** What this spec delivers (draw from Step 0, Sub-field 3: "Where it falls short") that the persona's current approach failed to provide. Every gain must be traceable to either Sub-field 3 or persona-specific Field 1 detail. Generic gains not anchored to a named Step 0 sub-field do not satisfy this field.

**Field 3 — Losses and switching costs:** The floor-level adoption friction (draw from Step 0, Sub-field 4: "Floor-level switching cost") plus any persona-specific workflow disruption, learning cost, or regression this persona absorbs. Losses must reference Sub-field 4; additional persona-specific losses may also reference Sub-field 3 where the spec's gaps create persona-specific harm. Do not state "no losses" for any Detractor-tier persona without a one-sentence explanation.

**Field 4 — Feedback items:** Ordered by descending severity — blocking first, then major, then minor, then cosmetic. No lower-severity item may precede a higher-severity item. Mark each item: `[BLOCKING]`, `Major`, `Minor`, or `Cosmetic`. If no objections exist, state "No feedback items — persona adopts without friction."

**Field 5 — NPS:** `NPS: X/10`

**Field 6 — Band:** `Band: Detractor (1–6)` / `Band: Passive (7–8)` / `Band: Promoter (9–10)`. Separate labeled field; not inline with Field 5.

**Field 7 — NPS justification:** Whether this persona's gains (Field 2) outweigh their losses (Field 3) — the inertia verdict. The instruction for this field is: does the spec's value exceed the switching cost for this persona, and why? State both what the persona gains AND what they lose or sacrifice; both sides are required. Do not use "or" between gains and losses; both must appear.

**Field 8 — Revision recommendation:** One sentence naming the specific spec element that, if changed, would most improve this persona's NPS. Reference a named spec element, section, or constraint. Generic recommendations ("improve onboarding," "add documentation") do not pass.

**Field 9 — Inertia verdict:** Conclude with exactly one of: `Inertia: Overcome` / `Inertia: Borderline` / `Inertia: Not overcome`.

**Field 10 — Inline blocker flag:** If any Field 4 item is `[BLOCKING]`, restate it here as: `[BLOCKING] — [item text]`. If no blocking items: "No blocking items."

**Field 11 — Card completeness:** State: `Fields 1–11: COMPLETE`

---

### Step 2 — Professional Lenses

The UX Read appears before the PM Read in document order.

#### UX Read

Observe the spec as a behavioral artifact (3+ sentences). Identify:
- Which user behaviors the spec assumes without validating
- Where the spec introduces friction relative to Step 0 Sub-field 1 (status quo behavior)
- What mental model mismatch, if any, exists between the spec's design and actual user task representation

#### PM Read

Synthesize strategic implications from the 12 persona simulation (3+ sentences). Identify:
- Which adoption segments most support initial uptake vs. create resistance
- The strategic risk posed by the highest-severity issues across all 12 cards
- A ship / revise / block recommendation with one-sentence rationale

---

### Step 3 — Aggregate Section

**Aggregate NPS:** Mean of all 12 persona NPS scores. Show arithmetic: (sum of scores) ÷ 12 = mean. Round to one decimal place.

**Threshold verdict:** Is mean ≥ 7.0? State explicitly: `PASS — proceed to release` or `FAIL — spec requires revision before shipping`.

**Band distribution:** `Promoters (9–10): N | Passives (7–8): N | Detractors (1–6): N`

**Dominant Detractor objection:** The single blocking or major feedback theme most frequently cited by Detractor-tier personas. State the theme and count: "X — cited by N of M Detractors."

**Sensitivity analysis:** Identify the 2–3 personas whose scores most drive the aggregate mean. For each: name the persona, state their NPS, and quantify their influence using aggregate-contribution framing — state the mean delta if their score were removed or shifted (e.g., "Removing C-07 shifts mean from 6.4 to 6.9").

---

### Step 4 — Cross-Persona Theme Matrix

Build a table mapping recurring themes across all 12 persona cards. At least one theme row required.

| Theme | Personas | Severity distribution | Highest severity | Recommendation |
|-------|----------|-----------------------|-----------------|----------------|
| ...   | ...      | (e.g., 1 blocking, 3 major, 2 minor) | ... | ... |

The theme matrix is the final analytical synthesis section. No new analytical content follows it.

---

### Step 5 — Revision Synthesis

**Blocking issues requiring resolution before shipping:**
List all [BLOCKING] items from all 12 persona cards, with the originating persona. If none: "None."

**Two-pass revision plan:**

*Pass 1 — Per-persona targeted changes:* For each Detractor-tier persona (NPS 1–6), name the single highest-impact spec change. Format: `C-XX: [specific change to named spec element]`.

*Pass 2 — Cross-persona ranked priority:* Rank the top 3 spec changes by (a) number of personas affected and (b) maximum severity tier. Minimum 2 items — a single-item list is not a ranking. Format:
1. [Change] — [N personas affected] — [Max severity]
2. [Change] — [N personas affected] — [Max severity]
3. [Change] — [N personas affected] — [Max severity]

---

**Final completeness check:** Before submitting, confirm: (1) exactly 12 persona cards present, (2) cards in ascending NPS order, (3) aggregate mean computed and threshold stated, (4) theme matrix has ≥ 1 row with severity distribution, (5) revision synthesis addresses all Detractor-tier personas in Pass 1.

---

## V-02 — Axis: A-25 (Explicit Epistemic Rationale for UX-Before-PM Ordering)

**Hypothesis:** Attaching an epistemic rationale to the UX-before-PM ordering converts it from a positionally verifiable but arbitrary sequence constraint into a principled one. Without a rationale, a later variation author can reverse the order without logical contradiction. With a rationale ("behavioral observation must precede strategic synthesis"), reversing the order introduces an explicit inconsistency with the stated reasoning, making the constraint self-enforcing.

---

You are running the **listen-feedback** skill.

**Task:** Simulate customer reactions to the provided spec before it ships. Produce 12 per-persona feedback cards (C-01 through C-12), UX and PM professional lens syntheses, aggregate NPS analysis, a cross-persona theme matrix, and a prioritized revision plan.

**Output sections in order:**
1. Step 0 — Inertia Baseline
2. Step 1 — 12 Persona Cards (ascending NPS order)
3. Step 2 — Professional Lenses (UX Read precedes PM Read — see epistemic rationale below)
4. Step 3 — Aggregate Section
5. Step 4 — Cross-Persona Theme Matrix
6. Step 5 — Revision Synthesis

---

### Step 0 — Inertia Baseline

Before simulating any persona, characterize the status quo this spec competes against. Complete all four sub-fields.

**Status quo name:** The specific tool, workflow, or practice this spec displaces.

**What it delivers:** The value the status quo currently provides. One sentence.

**Where it falls short:** The gap that motivates this spec. One to two sentences.

**Floor-level switching cost:** The minimum adoption friction any persona faces. One sentence.

---

### Step 1 — 12 Persona Cards

Simulate all 12 customer personas (C-01 through C-12). Determine each persona's predicted NPS score before writing the card, then output all 12 cards in **ascending NPS order** (lowest score first, highest last).

Each card uses the following **numbered field manifest**. All 11 fields are required in every card. No field may be omitted for any persona, including Promoter-tier personas. Fields must appear in this exact order.

**Card header:** `### [C-XX — Name — Role]`
Header contains only persona ID, name, and role.

---

**Field 1 — Current approach:** What this persona does today. One to two sentences. Populate for every persona, including when no equivalent exists.

**Field 2 — Gains from this spec:** What this spec provides that the current approach failed to deliver. Ground gains in the persona's current workflow or the Step 0 inertia baseline.

**Field 3 — Losses and switching costs:** What this persona gives up or must absorb to adopt the spec. Include workflow disruption, learning cost, and transition friction. For Promoter-tier personas, explicitly state losses are negligible if that is the case — do not leave Field 3 empty.

**Field 4 — Feedback items:** Ordered by descending severity — blocking first, then major, then minor, then cosmetic. Mark each item: `[BLOCKING]`, `Major`, `Minor`, `Cosmetic`. If no objections exist, state so explicitly.

**Field 5 — NPS:** `NPS: X/10`

**Field 6 — Band:** `Band: Detractor (1–6)` / `Band: Passive (7–8)` / `Band: Promoter (9–10)`. Appears as a dedicated labeled field separate from Field 5.

**Field 7 — NPS justification:** The inertia verdict — does this persona's gains outweigh their losses, and why? The justification must state what this persona gains AND what they lose or sacrifice relative to their current approach. Both sides are required; use conjunctive "and" between them, not "or." An NPS justification that names only gains fails this field.

**Field 8 — Revision recommendation:** One sentence naming the specific spec element that would most improve this persona's NPS if changed. Name the element; do not write generic advice.

**Field 9 — Inertia verdict:** Exactly one of: `Inertia: Overcome` / `Inertia: Borderline` / `Inertia: Not overcome`.

**Field 10 — Inline blocker flag:** If any Field 4 item is `[BLOCKING]`, restate here. If none: "No blocking items."

**Field 11 — Card completeness:** `Fields 1–11: COMPLETE`

---

### Step 2 — Professional Lenses

**Epistemic rationale for UX-before-PM ordering:** UX observation identifies behavioral patterns — what users actually do, where friction exists, how workflows are mentally organized — before PM synthesis frames those patterns in terms of business impact or adoption segments. If PM synthesis runs first, PM's strategic framing anchors all subsequent behavioral reading, causing behavioral evidence to be interpreted through a strategic lens rather than observed directly. Behavioral observation must precede strategic synthesis. This is why the UX Read appears before the PM Read in this protocol; reversing the order would invalidate this rationale.

#### UX Read

Observe the spec as a behavioral artifact (3+ sentences). Identify:
- Behavioral assumptions the spec makes without validation
- Friction points relative to the Step 0 status quo behavioral anchor
- Any mental model mismatch between the spec's task design and actual user task representation

#### PM Read

Synthesize strategic implications from the 12 persona simulation (3+ sentences). Identify:
- Adoption segments most likely to drive uptake vs. create resistance
- Strategic risk from the highest-severity issues
- A ship / revise / block recommendation with one-sentence rationale

---

### Step 3 — Aggregate Section

**Aggregate NPS:** Mean of all 12 persona NPS scores. Show arithmetic: (sum) ÷ 12 = mean.

**Threshold verdict:** `PASS — proceed to release` (mean ≥ 7.0) or `FAIL — spec requires revision before shipping` (mean < 7.0).

**Band distribution:** `Promoters (9–10): N | Passives (7–8): N | Detractors (1–6): N`

**Dominant Detractor objection:** The most common blocking or major theme among Detractor-tier personas. State the theme and count.

**Sensitivity analysis:** The 2–3 personas most driving the aggregate mean. For each: name, NPS, and aggregate-mean delta if their score were removed (e.g., "Removing C-03 shifts mean from 6.2 to 6.7"). Use contribution framing, not threshold-proximity framing.

---

### Step 4 — Cross-Persona Theme Matrix

| Theme | Personas | Severity distribution | Highest severity | Recommendation |
|-------|----------|-----------------------|-----------------|----------------|

At least one theme. Each row includes per-severity counts (e.g., "2 blocking, 1 major"). The theme matrix is the final analytical synthesis section.

---

### Step 5 — Revision Synthesis

**Blocking issues:**
All [BLOCKING] items with originating persona. If none: "None."

**Two-pass revision plan:**

*Pass 1 — Per-persona targeted changes:* For each Detractor-tier persona, name the specific spec element change. `C-XX: [change]`.

*Pass 2 — Cross-persona ranked priority:* Ranked list of top 3 changes by (a) persona count affected and (b) max severity. Minimum 2 items.
1. ...
2. ...
3. ...

---

## V-03 — Axis: A-26 (Numbered Aggregate Manifest with Positional Verifiability)

**Hypothesis:** Applying the A-23 numbered-manifest principle to the aggregate section makes every aggregate field positionally verifiable — A3 is detectable by counting, not by parsing labels. Without numbering, a reviewer must read field names to detect a missing Dominant Detractor objection or sensitivity analysis; with a numbered manifest and explicit completeness rule, absence is detectable by count alone. An output can satisfy A-10 (labeled field present) while failing A-26 (field not positionally verifiable).

---

You are running the **listen-feedback** skill.

**Task:** Simulate customer reactions to the provided spec before it ships. Produce 12 per-persona feedback cards (C-01 through C-12), UX and PM professional lens syntheses, aggregate NPS analysis, a cross-persona theme matrix, and a prioritized revision plan.

**Output sections in order:**
1. Step 0 — Inertia Baseline
2. Step 1 — 12 Persona Cards (ascending NPS order)
3. Step 2 — Professional Lenses (UX Read, then PM Read)
4. Step 3 — Aggregate Section (numbered manifest A1–A5)
5. Step 4 — Cross-Persona Theme Matrix
6. Step 5 — Revision Synthesis

---

### Step 0 — Inertia Baseline

Before simulating any persona, characterize the status quo this spec competes against.

**Status quo name:** The tool, workflow, or practice this spec displaces.

**What it delivers:** The value the status quo currently provides. One sentence.

**Where it falls short:** The gap that motivates this spec. One to two sentences.

**Floor-level switching cost:** The minimum adoption friction any persona faces. One sentence.

---

### Step 1 — 12 Persona Cards

Simulate all 12 customer personas (C-01 through C-12). Determine each persona's predicted NPS before writing the card, then output all 12 in **ascending NPS order** (lowest score first).

Each card uses the following **numbered field manifest**. All 11 fields are required in every card. No field may be omitted for any persona, including Promoter-tier personas. Fields must appear in this exact order.

**Card header:** `### [C-XX — Name — Role]`
Header contains only persona ID, name, and role.

---

**Field 1 — Current approach:** What this persona does today. Populate for every persona.

**Field 2 — Gains from this spec:** What this spec provides that the current approach failed to deliver.

**Field 3 — Losses and switching costs:** What this persona gives up or must absorb. For Promoter-tier personas, state losses explicitly even if negligible; do not leave this field empty.

**Field 4 — Feedback items:** Descending severity order — blocking → major → minor → cosmetic. Mark each: `[BLOCKING]`, `Major`, `Minor`, `Cosmetic`.

**Field 5 — NPS:** `NPS: X/10`

**Field 6 — Band:** `Band: Detractor (1–6)` / `Band: Passive (7–8)` / `Band: Promoter (9–10)`. Separate field from Field 5.

**Field 7 — NPS justification:** State what this persona gains AND what they lose or sacrifice relative to their current approach. Both gains and losses are required; a justification naming only gains fails this field.

**Field 8 — Revision recommendation:** One sentence naming the specific spec element change. No generic recommendations.

**Field 9 — Inertia verdict:** `Inertia: Overcome` / `Inertia: Borderline` / `Inertia: Not overcome`.

**Field 10 — Inline blocker flag:** Restate any `[BLOCKING]` items from Field 4. If none: "No blocking items."

**Field 11 — Card completeness:** `Fields 1–11: COMPLETE`

---

### Step 2 — Professional Lenses

The UX Read precedes the PM Read in document order.

#### UX Read

Observe the spec as a behavioral artifact (3+ sentences). Identify behavioral assumptions, friction relative to the Step 0 status quo, and any mental model mismatch between spec design and user task representation.

#### PM Read

Synthesize strategic implications from the persona simulation (3+ sentences). Identify adoption segments, strategic risk from high-severity issues, and a ship / revise / block recommendation.

---

### Step 3 — Aggregate Section

The aggregate section uses the following **numbered field manifest**. All 5 fields (A1 through A5) are required. No field may be omitted. If a field cannot be computed (e.g., no Detractor-tier personas exist), state the field label and explain why it is not applicable — do not silently drop the field.

**A1 — Aggregate NPS:** Mean of all 12 persona NPS scores. Show arithmetic: (sum) ÷ 12 = mean.

**A2 — Threshold verdict:** `PASS — proceed to release` (mean ≥ 7.0) or `FAIL — spec requires revision before shipping` (mean < 7.0).

**A3 — Band distribution:** `Promoters (9–10): N | Passives (7–8): N | Detractors (1–6): N`

**A4 — Dominant Detractor objection:** The single blocking or major feedback theme most frequently cited by Detractor-tier personas. State the theme and count. If no Detractors exist, state: "A4 — No Detractor-tier personas — not applicable."

**A5 — Sensitivity analysis:** The 2–3 personas most driving the aggregate mean. For each: name, NPS, and aggregate-mean delta if their score were removed. Use contribution framing (mean delta), not threshold-proximity framing (distance from 7.0).

**Aggregate completeness check:** After A5, state: `Fields A1–A5: COMPLETE`

---

### Step 4 — Cross-Persona Theme Matrix

| Theme | Personas | Severity distribution | Highest severity | Recommendation |
|-------|----------|-----------------------|-----------------|----------------|

At least one theme. Per-severity counts in each row. Theme matrix is the final analytical synthesis section.

---

### Step 5 — Revision Synthesis

**Blocking issues:**
All [BLOCKING] items with originating persona. If none: "None."

**Two-pass revision plan:**

*Pass 1 — Per-persona targeted changes:* For each Detractor-tier persona, one specific spec element change. `C-XX: [change]`.

*Pass 2 — Cross-persona ranked priority:* Ranked list (minimum 2 items) of top 3 changes by (a) persona count affected and (b) max severity.
1. ...
2. ...
3. ...

---

## V-04 — Combined: A-24 + A-25 (Named Sub-Field Cross-References + Epistemic Rationale)

**Hypothesis:** Combining structural dependency (gains/losses instructions that cannot be completed without consulting named Step 0 sub-fields) with a principled ordering constraint (UX epistemic rationale that makes reversing the sequence a logical contradiction) produces output with maximum structural integrity on the two highest-information axes. The cross-reference prevents loss-side omission; the rationale prevents sequence reversal. Each constraint reinforces independent output properties; combined, they eliminate two distinct failure modes.

---

You are running the **listen-feedback** skill.

**Task:** Simulate customer reactions to the provided spec before it ships. Produce 12 per-persona feedback cards (C-01 through C-12), UX and PM professional lens syntheses, aggregate NPS analysis, a cross-persona theme matrix, and a prioritized revision plan.

**Output sections in order:**
1. Step 0 — Inertia Baseline (defines named sub-fields referenced throughout)
2. Step 1 — 12 Persona Cards (ascending NPS order)
3. Step 2 — Professional Lenses (UX Read first — epistemic rationale stated; PM Read second)
4. Step 3 — Aggregate Section
5. Step 4 — Cross-Persona Theme Matrix
6. Step 5 — Revision Synthesis

---

### Step 0 — Inertia Baseline

Before simulating any persona, define the status quo this spec competes against. The four sub-fields below are named by label and referenced directly in the persona card instructions. Complete all four.

**Sub-field 1 — Status quo name:** The specific tool, workflow, or practice this spec displaces. One noun phrase.

**Sub-field 2 — What it delivers:** The value the status quo currently provides — what it does well enough to retain adoption. One sentence.

**Sub-field 3 — Where it falls short:** The gap or failure mode in the status quo that motivates this spec. One to two sentences. This is the primary source for gains assessments in Field 2 below.

**Sub-field 4 — Floor-level switching cost:** The minimum friction any persona faces to abandon the status quo. One sentence. This is the primary source for losses assessments in Field 3 below.

---

### Step 1 — 12 Persona Cards

Simulate all 12 customer personas (C-01 through C-12). Predict each persona's NPS before writing the card. Output all 12 cards in **ascending NPS order** (lowest first, highest last).

Each card uses the following **numbered field manifest**. All 11 fields are required in every card. No field may be omitted for any persona, including Promoter-tier. Fields must appear in this exact order.

**Card header:** `### [C-XX — Name — Role]`
Header contains only persona ID, name, and role. Field 1 is the first body content.

---

**Field 1 — Current approach:** What this persona does today without the spec. One to two sentences of persona-specific workflow detail. Populate even when no equivalent exists.

**Field 2 — Gains from this spec:** What this spec provides that the current approach (Step 0, Sub-field 3: "Where it falls short") failed to deliver. Every gain must be traceable to either Sub-field 3 (the spec's improvement over the gap) or the persona-specific Field 1 detail. Gains not anchored to a named sub-field do not satisfy this field.

**Field 3 — Losses and switching costs:** The floor-level adoption friction (Step 0, Sub-field 4: "Floor-level switching cost") plus any persona-specific workflow disruption, learning cost, or regression this persona absorbs beyond the baseline. Losses must reference Sub-field 4. Where Sub-field 3 gaps directly harm this persona (spec falls short in a domain this persona depends on), note that as an additional loss. Do not state "no losses" for any Detractor-tier persona without a one-sentence explanation of why friction is genuinely zero.

**Field 4 — Feedback items:** Descending severity order — blocking first, then major, then minor, then cosmetic. Mark each: `[BLOCKING]`, `Major`, `Minor`, `Cosmetic`. If no objections: "No feedback items — persona adopts without friction."

**Field 5 — NPS:** `NPS: X/10`

**Field 6 — Band:** `Band: Detractor (1–6)` / `Band: Passive (7–8)` / `Band: Promoter (9–10)`. Dedicated labeled field, separate from Field 5.

**Field 7 — NPS justification:** The inertia verdict — does this persona's gains (Field 2) outweigh their losses (Field 3)? State what this persona gains AND what they lose or sacrifice relative to their current approach. Both sides are required. Use conjunctive "and" between gains and losses; do not use "or." An NPS justification naming only gains fails this field.

**Field 8 — Revision recommendation:** One sentence naming the specific spec element that, if changed, would most improve this persona's NPS. Name a spec element; no generic advice.

**Field 9 — Inertia verdict:** `Inertia: Overcome` / `Inertia: Borderline` / `Inertia: Not overcome`.

**Field 10 — Inline blocker flag:** Restate any `[BLOCKING]` items from Field 4. If none: "No blocking items."

**Field 11 — Card completeness:** `Fields 1–11: COMPLETE`

---

### Step 2 — Professional Lenses

**Epistemic rationale for UX-before-PM ordering:** UX observation identifies behavioral patterns — what users actually do, where friction concentrates, how tasks are mentally modeled — independently of strategic framing. PM synthesis then interprets those behavioral findings in terms of adoption risk, segment prioritization, and go/no-go decision-making. If PM synthesis precedes UX observation, PM's strategic lens anchors all subsequent behavioral reading, causing the evaluator to interpret user behavior as evidence for or against a strategic thesis rather than observing it directly. Behavioral observation must precede strategic synthesis to preserve the independence of the observational layer. This is why the UX Read appears before the PM Read in this protocol.

#### UX Read

Observe the spec as a behavioral artifact (3+ sentences). Identify:
- Behavioral assumptions the spec makes without validating (what the spec requires of users that Step 0 Sub-field 1 behavior does not guarantee)
- Friction relative to the Step 0 status quo behavioral anchor
- Mental model mismatch, if any, between the spec's task design and actual user task representation

#### PM Read

Synthesize strategic implications from the 12 persona simulation (3+ sentences). Identify:
- Adoption segments most likely to drive initial uptake vs. create resistance
- Strategic risk from the highest-severity issues across all 12 cards
- A ship / revise / block recommendation with one-sentence rationale

---

### Step 3 — Aggregate Section

**Aggregate NPS:** Mean of all 12 persona NPS scores. Show arithmetic: (sum) ÷ 12 = mean.

**Threshold verdict:** `PASS — proceed to release` (mean ≥ 7.0) or `FAIL — spec requires revision before shipping` (mean < 7.0).

**Band distribution:** `Promoters (9–10): N | Passives (7–8): N | Detractors (1–6): N`

**Dominant Detractor objection:** The most common blocking or major theme among Detractor-tier personas. State theme and count (e.g., "Missing offline support — cited by 4 of 5 Detractors"). If no Detractors: "No Detractor-tier personas."

**Sensitivity analysis:** The 2–3 personas most driving the aggregate mean. For each: name, NPS, and aggregate-mean delta if removed. Contribution framing required — not threshold-proximity framing.

---

### Step 4 — Cross-Persona Theme Matrix

| Theme | Personas | Severity distribution | Highest severity | Recommendation |
|-------|----------|-----------------------|-----------------|----------------|

At least one theme. Per-severity counts per row (e.g., "1 blocking, 3 major, 2 minor"). Theme matrix is the final analytical synthesis section.

---

### Step 5 — Revision Synthesis

**Blocking issues:**
All [BLOCKING] items from all 12 persona cards, with originating persona. If none: "None."

**Two-pass revision plan:**

*Pass 1 — Per-persona targeted changes:* For each Detractor-tier persona (NPS 1–6), state the single highest-impact spec change. `C-XX: [specific change to named spec element]`.

*Pass 2 — Cross-persona ranked priority:* Ranked list of top 3 changes by (a) persona count affected and (b) max severity tier. Minimum 2 items — a single-item list is not a ranking.
1. [Change] — [N personas affected] — [Max severity]
2. ...
3. ...

---

## V-05 — Combined: A-24 + A-25 + A-26 + Coaching Language (seeds A-27)

**Hypothesis:** Full structural combination — named sub-field cross-references (prevents loss-side omission), UX epistemic rationale (prevents sequence reversal), and numbered aggregate manifest (prevents silent aggregate field omission) — achieves positional verifiability at every level of the output. Coaching language added at the three known simulation failure boundaries ("where most evaluations go wrong") addresses behavioral gaps that structural constraints alone cannot close: a model can satisfy every structural rule while still producing a Detractor card with an empty losses field or a Dominant Detractor objection that restates the NPS mean rather than naming a theme.

---

You are running the **listen-feedback** skill.

**Task:** Simulate customer reactions to the provided spec before it ships. Produce 12 per-persona feedback cards (C-01 through C-12), UX and PM professional lens syntheses, aggregate NPS analysis, a cross-persona theme matrix, and a prioritized revision plan.

**Output sections in order:**
1. Step 0 — Inertia Baseline (defines named sub-fields; do not skip)
2. Step 1 — 12 Persona Cards (ascending NPS order; simulate all 12 before sorting)
3. Step 2 — Professional Lenses (UX Read first per epistemic rationale; PM Read second)
4. Step 3 — Aggregate Section (numbered manifest A1–A5; all fields required)
5. Step 4 — Cross-Persona Theme Matrix
6. Step 5 — Revision Synthesis

---

### Step 0 — Inertia Baseline

Before writing a single persona card, define the status quo this spec competes against. The four sub-fields are named by label and cross-referenced directly in persona card instructions. A simulation that skips Step 0 cannot correctly compute gains and losses — this is where many runs go wrong.

**Sub-field 1 — Status quo name:** The specific tool, workflow, or practice this spec displaces. One noun phrase.

**Sub-field 2 — What it delivers:** The value the status quo currently provides — what it does well enough to retain adoption. One sentence.

**Sub-field 3 — Where it falls short:** The gap or failure mode in the status quo that motivates this spec. One to two sentences. This sub-field is the primary gains anchor for Field 2.

**Sub-field 4 — Floor-level switching cost:** The minimum friction any persona faces to abandon the status quo. One sentence. This sub-field is the primary losses anchor for Field 3.

---

### Step 1 — 12 Persona Cards

Simulate all 12 customer personas (C-01 through C-12). Predict each persona's NPS before writing the card. Sort all 12 cards into **ascending NPS order** (lowest first, highest last) before outputting. Ties may appear in any order within their score tier.

Each card uses the following **numbered field manifest**. All 11 fields are required in every card. No field may be omitted for any persona including Promoter-tier. Fields must appear in this exact order.

**Card header:** `### [C-XX — Name — Role]`
Header contains only persona ID, name, role. Field 1 is the first body content.

> **Common simulation failure — Field 3:** The most frequent error in listen-feedback runs is Field 3 (Losses) for Promoter-tier personas. A high NPS does not mean losses are zero. Promoter personas still absorb the floor-level switching cost (Sub-field 4). Field 3 must be populated for every persona; "no losses" requires a one-sentence explanation.

---

**Field 1 — Current approach:** What this persona does today without the spec. One to two sentences of persona-specific workflow detail. Populate even when no equivalent workflow exists ("No current equivalent — this capability is new to this persona.").

**Field 2 — Gains from this spec:** What this spec provides that the current approach (Step 0, Sub-field 3: "Where it falls short") failed to deliver. Every gain must be traceable to Sub-field 3 or persona-specific Field 1 detail. Generic gains not anchored to a named Step 0 sub-field do not satisfy this field.

**Field 3 — Losses and switching costs:** The floor-level adoption friction (Step 0, Sub-field 4: "Floor-level switching cost") plus any persona-specific workflow disruption, learning cost, or regression this persona absorbs beyond the baseline. Losses must reference Sub-field 4. Where Sub-field 3 gaps directly harm this persona (spec falls short in a domain this persona depends on), note that as an additional loss. Do not leave this field empty; do not state "no losses" without a one-sentence explanation for any persona regardless of NPS tier.

**Field 4 — Feedback items:** Descending severity order — blocking first, then major, then minor, then cosmetic. No lower-severity item may precede a higher-severity item. Mark each: `[BLOCKING]`, `Major`, `Minor`, `Cosmetic`. If no objections: "No feedback items — persona adopts without friction."

**Field 5 — NPS:** `NPS: X/10`

**Field 6 — Band:** `Band: Detractor (1–6)` / `Band: Passive (7–8)` / `Band: Promoter (9–10)`. Dedicated labeled field, separate from Field 5.

**Field 7 — NPS justification:** The inertia verdict — does this persona's gains (Field 2) outweigh their losses (Field 3)? State what this persona gains AND what they lose or sacrifice. Both sides are required; use conjunctive "and," not "or." A justification naming only gains fails this field. The answer to "do gains outweigh losses" should match the Field 9 inertia verdict.

**Field 8 — Revision recommendation:** One sentence naming the specific spec element that, if changed, would most improve this persona's NPS. Name a spec element, section, or constraint. No generic recommendations.

**Field 9 — Inertia verdict:** `Inertia: Overcome` / `Inertia: Borderline` / `Inertia: Not overcome`.

**Field 10 — Inline blocker flag:** Restate any `[BLOCKING]` items from Field 4 verbatim. If none: "No blocking items."

**Field 11 — Card completeness:** `Fields 1–11: COMPLETE`

---

### Step 2 — Professional Lenses

**Epistemic rationale for UX-before-PM ordering:** UX observation identifies behavioral patterns — what users actually do, where friction concentrates, how tasks are mentally organized — before PM synthesis frames those patterns as strategic risk or adoption opportunity. If PM synthesis runs first, PM framing becomes the interpretive lens through which all behavioral evidence is subsequently read, compromising the independence of behavioral observation. Behavioral observation must precede strategic synthesis. This rationale means the UX-before-PM ordering is not an arbitrary sequence preference: reversing it would invalidate the stated epistemic basis.

> **Common simulation failure — PM Read:** The most frequent error in professional lens synthesis is a PM Read that restates what the persona cards already said rather than synthesizing across them. The PM Read should name the adoption pattern (which segments cluster, which diverge), the strategic implication of the highest-severity issue, and a disposition recommendation (ship / revise / block) — not a summary of individual card findings.

#### UX Read

Observe the spec as a behavioral artifact (3+ sentences). Identify:
- Behavioral assumptions the spec makes without validating (what the spec requires of users that Step 0 Sub-field 1 behavior does not guarantee)
- Friction relative to the Step 0 status quo behavioral anchor
- Mental model mismatch, if any, between the spec's task design and actual user task representation

#### PM Read

Synthesize strategic implications from the 12 persona simulation (3+ sentences). Identify:
- Adoption segments most likely to drive initial uptake vs. create resistance
- The strategic risk created by the highest-severity issues across all 12 cards
- A ship / revise / block recommendation with one-sentence rationale

---

### Step 3 — Aggregate Section

The aggregate section uses the following **numbered field manifest**. All 5 fields (A1 through A5) are required. No field may be omitted. If a field is inapplicable (e.g., no Detractor-tier personas), state the field label and the reason — do not silently skip the field.

> **Common simulation failure — A4:** The most frequent aggregate error is a Dominant Detractor objection that restates the aggregate NPS number ("most Detractors scored 4 or below") rather than naming the feedback theme causing the low scores. A4 requires a content theme ("Missing bulk export," "No offline mode"), not a score restatement.

**A1 — Aggregate NPS:** Mean of all 12 persona NPS scores. Show arithmetic: (sum of 12 scores) ÷ 12 = mean. Round to one decimal place.

**A2 — Threshold verdict:** `PASS — proceed to release` (mean ≥ 7.0) or `FAIL — spec requires revision before shipping` (mean < 7.0).

**A3 — Band distribution:** `Promoters (9–10): N | Passives (7–8): N | Detractors (1–6): N`

**A4 — Dominant Detractor objection:** The single blocking or major feedback theme most frequently cited by Detractor-tier personas. Name the theme and state how many Detractors cited it: "X — cited by N of M Detractors." This is a content theme from the feedback items, not a score description.

**A5 — Sensitivity analysis:** The 2–3 personas most driving the aggregate mean. For each: name, NPS, and aggregate-mean delta if their score were removed (e.g., "Removing C-09 shifts mean from 6.1 to 6.6"). Use contribution framing — state the mean delta — not threshold-proximity framing (do not say "C-09 is just below 7.0").

**Aggregate completeness check:** After A5, state: `Fields A1–A5: COMPLETE`

---

### Step 4 — Cross-Persona Theme Matrix

| Theme | Personas | Severity distribution | Highest severity | Recommendation |
|-------|----------|-----------------------|-----------------|----------------|
| ...   | ...      | (e.g., 1 blocking, 3 major, 2 minor) | ... | ... |

At least one theme row required. Per-severity counts required in each row. The theme matrix is the final analytical synthesis section — no new analytical content follows it.

---

### Step 5 — Revision Synthesis

**Blocking issues requiring resolution before shipping:**
List all [BLOCKING] items from all 12 persona cards, with originating persona. If none: "None."

**Two-pass revision plan:**

*Pass 1 — Per-persona targeted changes:* For each Detractor-tier persona (NPS 1–6), state the single highest-impact spec change. `C-XX: [specific change to a named spec element]`.

*Pass 2 — Cross-persona ranked priority:* Ranked list of top 3 changes by (a) number of personas affected and (b) maximum severity tier. Minimum 2 items in the list — a single-item list is not a ranking.
1. [Change description] — [N personas affected] — [Max severity]
2. [Change description] — [N personas affected] — [Max severity]
3. [Change description] — [N personas affected] — [Max severity]

---

**Final completeness check:** Before submitting, confirm: (1) exactly 12 persona cards present, one per C-01 through C-12, (2) cards in ascending NPS order, (3) Fields A1–A5 all present and `Fields A1–A5: COMPLETE` stated, (4) theme matrix has ≥ 1 row with per-severity counts, (5) Pass 2 revision list has ≥ 2 items.

---

## Variation Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| **A-24** Named sub-field cross-refs | PASS | — | — | PASS | PASS |
| **A-25** UX epistemic rationale | — | PASS | — | PASS | PASS |
| **A-26** Numbered aggregate manifest | — | — | PASS | — | PASS |
| Coaching language (A-27 seed) | — | — | — | — | PASS |
| A-12 UX before PM | PASS (bare) | PASS + rationale | PASS (bare) | PASS + rationale | PASS + rationale |
| A-17 Gains AND losses | PASS (via cross-ref) | PASS (conjunctive) | PASS (conjunctive) | PASS (both) | PASS (both) |
| A-21 Conjunctive "and" | PASS (via cross-ref) | PASS (explicit) | PASS (explicit) | PASS (both) | PASS (both) |
| A-23 Numbered persona manifest | PASS | PASS | PASS | PASS | PASS |

**Expected scoring range (220 max):**
- V-01: 215/220 (A-25, A-26 absent)
- V-02: 215/220 (A-24, A-26 absent)
- V-03: 215/220 (A-24, A-25 absent)
- V-04: 220/220 (A-24, A-25 present; A-26 absent — but A-26 not scored at 0 here because V-04 could earn it if the aggregate happens to number fields)
- V-05: 220/220 all three new criteria + coaching seeds A-27
