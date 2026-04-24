---

## Scorecard: review-users Round 1

### Per-Variation Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-02 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-03 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-04 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-05 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-06 (recommended) | PASS | PASS | **FAIL** | PASS | PASS |
| C-07 (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-08 (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-09 (aspirational) | PASS | PASS | PASS | **FAIL** | PASS |
| C-10 (aspirational) | PASS | PASS | PASS | PASS | PASS |
| **Composite** | **100** | **100** | **90** | **95** | **100** |
| **Golden** | YES | YES | YES | YES | YES |

**All 5 variations are Golden.** No essential criterion failed in any variation.

---

### Ranking

1. **V-01, V-02, V-05** — tied at 100
2. **V-04** — 95 (C-09 only gap; no friction typing in conversational register)
3. **V-03** — 90 (C-06 fails; four-category sub-sections collapse first-person voice)

---

### Why V-03 Fails C-06

The per-category structure (`Confusion findings: "[quote]" — [analytical reason]`) produces analytical bullets, not first-person narrative. The Scenario field is one sentence. A model following V-03 writes *about* the persona's friction rather than *as* the persona. Trade-off: V-03 has the strongest C-03 and C-09 structural guarantees of any variation — verbatim quotes are required by the template format, and typing is structurally unavoidable — but it pays for this with C-06.

### Why V-04 Fails C-09

No mention of confusion/friction/fear/jargon anywhere. The conversational register is entirely type-agnostic. This is a clean isolation: V-04 proves the named-character + scenario mechanism drives C-06 and C-08 well without needing type tags; C-09 requires an explicit taxonomy to be introduced.

---

### Excellence Signals

**Pre-committed score table (V-02)** — printing the score table before narrative forces commitment before rationalization and makes C-01/C-02 structurally unfailable.

**Inertia fields make conflict detection mechanistic (V-05)** — "beats current process" / "loses to current process" per persona produces cross-persona conflicts by field comparison rather than by instruction alone. Strongest C-08 driver.

**Named characters drive first-person voice (V-04)** — "Sam has 10 minutes" produces naturalistic first-person output more reliably than generic instruction. Third-person narration feels unnatural when the model writes *as Sam*.

**R2 combination target:** V-02 score table + V-04 named characters + V-03 per-category quote *within* narrative prose + V-05 inertia field.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-committed score table forces score commitment before narrative, making C-01/C-02 structurally unfailable", "inertia fields (beats/loses per persona) make conflict detection mechanistic — conflicts emerge from field comparison rather than abstract instruction", "four-category friction sub-sections guarantee C-09 but collapse first-person voice — C-06 and C-09 are in structural tension and need a hybrid approach in R2"]}
```
s by name — structurally unfailable |
| C-02 | PASS | Score column in pre-printed table + "`**Score: [must match SCORE SUMMARY TABLE]**`" cross-reference — strongest C-02 guarantee |
| C-03 | PASS | "At least one verbatim quote from the artifact per persona (use quotation marks)" — per-persona walkthrough requirement |
| C-04 | PASS | "CROSS-PERSONA SYNTHESIS" section with `\| Finding \| Personas \| Type \|` table |
| C-05 | PASS | Aggregate row in score table: `\| **Aggregate** \| **(sum/5 = X)** \|` — committed in the first output block |
| C-06 | PASS | "First person throughout ('I read...', 'I tried...', 'I noticed...')" — explicit instruction per persona |
| C-07 | PASS | Separate synthesis tables for universal (3+ flagged) and role-specific (1-2 only) |
| C-08 | PASS | "Persona conflicts" section with "At least one conflict" requirement and explicit null-case fallback |
| C-09 | PASS | `[confusion] [friction] [fear] [jargon]` inline tags instructed per persona; synthesis table has Type column for universal findings |
| C-10 | PASS | "Check SCORE SUMMARY TABLE — if any score < 3: one amend proposal per sub-3 persona" |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 2/2 = 10

**Composite: 100 — GOLDEN**

**Notes:** Highest structural reliability of all variations. Pre-printed score table is the key mechanism: committing all 5 scores before any narrative prevents post-hoc score rationalization and makes C-01/C-02 structurally unfailable. The synthesis Type column adds a second layer of C-09 enforcement beyond inline tags. This is the safest variation for a model that might skip fields in free-form output.

---

## V-03: Lifecycle Emphasis (Friction-Typed First)

**Axis:** Friction typing as primary structure — four named category sub-sections per persona.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "STOCK PERSONAS (run all 5):" with all 5 role names |
| C-02 | PASS | `**Usability score: [1-5]**` with mandatory Rationale field per persona |
| C-03 | PASS | Template requires `"[exact quote from artifact]"` as the first element in each category finding — structural guarantee; strongest C-03 of all 5 variations |
| C-04 | PASS | "Cross-Persona Synthesis" with "Universal friction (3+ personas)" including friction type call-out |
| C-05 | PASS | "(Maker + Developer + Compliance + Supervisor + Operator) / 5 = X" |
| C-06 | FAIL | Per-category format `"[exact quote]" — [analytical reason for this persona]` produces analytical bullet output, not first-person narrative. Scenario field is one sentence; findings are not written as "I read... I tried..." walkthrough. |
| C-07 | PASS | Separate universal/role-specific sections with explicit type attribution |
| C-08 | PASS | "Persona conflicts" with "Be specific: name the personas and the artifact feature causing the trade-off" |
| C-09 | PASS | Four named sub-sections per persona (Confusion / Friction / Fear / Jargon) — structural guarantee, strongest C-09 of all 5 variations; criterion structurally unfailable |
| C-10 | PASS | "1. State persona name and score; 2. Quote artifact text; 3. Propose concrete change; 4. State expected new score" |

**Essential:** 5/5 = 60 | **Recommended:** 2/3 = 20 | **Aspirational:** 2/2 = 10

**Composite: 90 — GOLDEN**

**Key trade-off:** Best C-03 and C-09 guarantees of any variation. The per-category template makes verbatim quoting and friction typing structurally unavoidable. However, this structural rigidity collapses first-person narrative voice — C-06 fails because the format produces analytical bullets, not walkthrough prose. A model following V-03 narrates *about* the persona's friction rather than *as* the persona.

---

## V-04: Phrasing Register (Scenario-Driven Conversational)

**Axis:** Conversational register — named characters, concrete scenarios, natural first-person voice.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Section headers `### Sam (Maker)`, `### Dev (Developer)`, `### Casey (Compliance)`, `### Jordan (Supervisor)`, `### Alex (Operator)` — all 5 stock role names present in parentheses |
| C-02 | PASS | `**Score: [1-5]** — [one sentence]` per persona |
| C-03 | PASS | "Narrate what they actually found — quote at least one exact phrase from the artifact" — requirement #2 of 4 per persona |
| C-04 | PASS | "What did they all struggle with?" — requires listing anything that "came up for three or more people" with artifact quote |
| C-05 | PASS | "Average of the five scores: (Sam + Dev + Casey + Jordan + Alex) / 5 = X" |
| C-06 | PASS | "Use first person throughout" + named characters with concrete scenarios drive strongest natural first-person voice of all 5 variations; the named-character framing makes third-person narration feel unnatural |
| C-07 | PASS | "What was unique to one or two people?" section distinct from universal-friction section |
| C-08 | PASS | "Where did one person's needs work against another's?" — most direct conflict question of any variation; concrete scenario framing surfaces tensions naturally |
| C-09 | FAIL | No mention of confusion/friction/fear/jargon type categories anywhere in the prompt; conversational register does not use typed labels |
| C-10 | PASS | "If any person scored below 3/5, propose one specific change...quote the problem text, write the fix, estimate the new score" |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 1/2 = 5

**Composite: 95 — GOLDEN**

**Notes:** Best first-person voice driver. Best persona conflict driver. The named-character framing (Sam/Dev/Casey/Jordan/Alex) is the strongest mechanism for naturalistic first-person output — models write from inside the character rather than describing them. Single failure: C-09 is completely absent. No friction type taxonomy appears anywhere in the prompt. This is V-04's only gap and the cleanest isolation of the type-tagging mechanism across all variations.

---

## V-05: Inertia Framing (Status-Quo Competitor Explicit)

**Axis:** Inertia baseline — "What I do today instead" field per persona; adoption-risk synthesis.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "STOCK PERSONAS (run all 5 in this order): 1.Maker 2.Developer 3.Compliance 4.Supervisor 5.Operator" |
| C-02 | PASS | `**Usability score: [1-5]**` with Rationale field per persona |
| C-03 | PASS | "At least one verbatim quote from the artifact in quotation marks" in walkthrough instruction |
| C-04 | PASS | "Cross-Persona Synthesis" with "Universal friction (3+ personas)" and adoption-risk annotation |
| C-05 | PASS | "(P1 + P2 + P3 + P4 + P5) / 5 = X" |
| C-06 | PASS | "First person throughout" in walkthrough section |
| C-07 | PASS | Separate universal/role-specific sections in synthesis |
| C-08 | PASS | Strongest C-08 driver of all variations: "Persona conflicts" explicitly instructs to look for overlap between one persona's "beats current process" and another's "loses to current process" — conflicts emerge from the template fields, not from abstract instruction |
| C-09 | PASS | "(confusion) / (friction) / (fear) / (jargon)" inline flags stated in walkthrough instruction |
| C-10 | PASS | Amend loop adds workaround context: includes persona's current workaround in the amend proposal, driving more actionable fixes |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 2/2 = 10

**Composite: 100 — GOLDEN**

**Notes:** Distinct value proposition beyond pure usability review: adds adoption-risk dimension. The inertia template fields (beats/loses) make C-08 conflict detection mechanistic — conflicts are surfaced by comparing fields across personas rather than by instruction alone. The "Inertia summary" section adds rollout-sequencing insight not available in other variations. The amend loop benefits from workaround awareness: proposed changes are framed against "what the persona does today," producing more actionable amendments.

---

## Variation Rankings

| Rank | Variation | Composite | Golden | Key Strength |
|------|-----------|-----------|--------|--------------|
| 1 (tie) | V-01 | 100 | YES | Compliance-first norm-setting; comprehensive baseline |
| 1 (tie) | V-02 | 100 | YES | Strongest structural reliability; pre-committed score table |
| 1 (tie) | V-05 | 100 | YES | Strongest C-08; adoption-risk dimension; inertia mechanistic |
| 4 | V-04 | 95 | YES | Best first-person voice; best naturalistic conflict detection; only C-09 gap |
| 5 | V-03 | 90 | YES | Best C-03/C-09 structural guarantee; sacrifices first-person voice |

**All 5 variations are Golden** (all essential criteria pass, composite >= 80).

---

## Excellence Signals

Patterns from the top-scoring variations that drove the result:

**Signal 1 — Three-field synthesis structure prevents omission**
V-01/V-02/V-05 all use an explicitly named synthesis section with three required sub-fields: universal friction (3+), role-specific friction (1-2), persona conflicts. Labeling each sub-field independently (rather than one open synthesis block) prevents a model from writing only the most obvious finding. When all three are named, all three get written.

**Signal 2 — Pre-committed score table (V-02) makes C-01/C-02 structurally unfailable**
Printing the table with all 5 persona names and a score column before any narrative forces score commitment before rationalization. Scores committed in the table cannot be contradicted by narratives written after. The "`must match SCORE SUMMARY TABLE`" cross-reference adds a second structural lock. This is the strongest mechanism for reliable C-01/C-02 pass rates.

**Signal 3 — Inertia fields make conflict detection mechanistic (V-05)**
Asking "Where the artifact beats my current process" and "Where the artifact loses to my current process" per persona produces findings that can be compared across personas without an explicit conflict instruction. When Maker's "beats" entry overlaps with Compliance's "loses" entry, the conflict is structurally observable rather than instructed. The synthesis section then just needs to notice the overlap.

**Signal 4 — Named characters drive first-person voice (V-04)**
Naming personas (Sam/Dev/Casey/Jordan/Alex) with concrete scenarios ("Sam is trying to ship a feature this week. Sam has 10 minutes.") produces more reliable first-person output than generic instruction. A model writing "as Sam" resists third-person narration naturally. This is the mechanism for V-04's C-06 superiority.

**Trade-off observed — C-09 vs C-06 (V-03)**
The only way to structurally guarantee friction typing (C-09) in V-03 was to organize each persona section by category rather than by narrative flow. This categorization collapsed first-person voice (C-06 fails). The two mechanisms are in tension: typed structure produces analytical bullets; narrative structure produces first-person walkthrough. A combined approach is needed in R2 to capture both.

---

## R2 Hypothesis

The ceiling observation from R1: no single variation simultaneously achieves structural C-03/C-09 guarantee (V-03) AND first-person voice (V-04) AND pre-committed scores (V-02) AND inertia conflict detection (V-05). These mechanisms reinforce each other rather than conflict. A combined variation for R2 should:
1. Use V-02's pre-printed score table (structural C-02 guarantee)
2. Use V-04's named characters (naturalistic C-06)
3. Add V-03's per-category quote requirement within the narrative walkthrough rather than as a replacement for it (C-03 + C-09 without sacrificing C-06)
4. Add V-05's "What I do today instead" field (mechanistic C-08)

---

## Round Summary

| Metric | Value |
|--------|-------|
| Variations scored | 5 |
| Golden | 5 (all) |
| Top composite | 100 |
| All essential pass | YES |
| Failing essential criteria | None |
| Weakest criterion across round | C-09 (fails only in V-04); C-06 (fails only in V-03) |
| Best essential reliability | V-02 (pre-committed score table) |
| Best recommended reliability | V-04 (strongest C-06 and C-08) |
| Best aspirational reliability | V-03 (strongest C-09, structural sub-sections) |
