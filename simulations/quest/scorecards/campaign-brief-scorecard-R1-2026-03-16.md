## Quest Score — campaign-brief / Round 1

**Rubric:** v1 (10 criteria, 3 tiers) · **Scoring:** PASS=10 · PARTIAL=5 · FAIL=0

---

### Scoring Scale

| Tier | Criteria | Points Each | Max |
|------|----------|-------------|-----|
| Essential | C-01–C-05 | 10 | 50 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-10 | 10 | 20 |
| **Total** | | | **100** |

---

### V-01 — Output format (dashboard skeleton declared before execution)

| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| C-01 | Sub-skills invoked in order | PARTIAL | Skeleton names sections but imposes no explicit execution sequence on the model |
| C-02 | Existing signals enumerated by namespace | PASS | Named "found signals" slot forces the model to fill it by namespace |
| C-03 | Missing signals explicitly named | PASS | Named gap slot — silence becomes visually obvious |
| C-04 | Narrative arc synthesizes signals together | PARTIAL | Narrative section exists in template; synthesis quality unguided — model may list |
| C-05 | Topic registered with name, date, intent | PARTIAL | Topic section present but registration-as-act not explicitly required |
| C-06 | Explicit readiness verdict | PASS | Verdict is a named terminal slot |
| C-07 | Gap list prioritized blocking vs. optional | PARTIAL | Gap table present; blocking/optional split not structurally demanded |
| C-08 | Scannable dashboard with visual hierarchy | PASS | Template is the hierarchy — highest C-08 compliance by construction |
| C-09 | Session delta | FAIL | No delta slot in skeleton |
| C-10 | Narrative confidence level | FAIL | No confidence slot |

**V-01 Total: 60/100**

---

### V-02 — Lifecycle emphasis (phase gates with `Required output:` checkpoints)

| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| C-01 | Sub-skills invoked in order | PASS | Each phase is a labeled gate — skipping produces obvious incompleteness; strongest C-01 enforcer |
| C-02 | Existing signals enumerated by namespace | PASS | `Required output:` block in signal-check phase mandates enumeration |
| C-03 | Missing signals explicitly named | PASS | `Required output:` block in gap phase — silence breaks the gate |
| C-04 | Narrative arc synthesizes signals together | PARTIAL | Synthesis phase exists but quality not structurally enforced; model can produce a list labeled "narrative" |
| C-05 | Topic registered with name, date, intent | PASS | Registration is its own labeled phase with a deliverable |
| C-06 | Explicit readiness verdict | PASS | Verdict phase is a terminal gate |
| C-07 | Gap list prioritized blocking vs. optional | PARTIAL | Gap phase present; blocking/optional split not in the gate spec |
| C-08 | Scannable dashboard with visual hierarchy | PARTIAL | Phase gates create structure, but no explicit dashboard template — visual shape is model-driven |
| C-09 | Session delta | FAIL | No delta mechanism in gate set |
| C-10 | Narrative confidence level | FAIL | No confidence gate |

**V-02 Total: 65/100**

---

### V-03 — Phrasing register (conversational narrator voice)

| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| C-01 | Sub-skills invoked in order | PARTIAL | Imperative instructions ("First: check…") imply sequence; not structurally enforced |
| C-02 | Existing signals enumerated by namespace | PARTIAL | Narrator may list signals but namespace-by-namespace enumeration is not demanded |
| C-03 | Missing signals explicitly named | PARTIAL | Narrator will mention gaps; explicit naming convention not enforced |
| C-04 | Narrative arc synthesizes signals together | PASS | "You are the narrator" cast is the strongest C-04 driver — ownership over synthesis is baked into the role |
| C-05 | Topic registered with name, date, intent | PARTIAL | "Check if registered" instruction present; act-of-registration not required output |
| C-06 | Explicit readiness verdict | PARTIAL | Verdict likely surfaces in prose; not a named, terminal block |
| C-07 | Gap list prioritized blocking vs. optional | FAIL | Prose register actively works against structured prioritization |
| C-08 | Scannable dashboard with visual hierarchy | PARTIAL | Dense prose helps signal density; visual hierarchy is model-invented |
| C-09 | Session delta | FAIL | No mechanism |
| C-10 | Narrative confidence level | PARTIAL | Narrator voice naturally tends toward hedging language — partial credit for likely emergence |

**V-03 Total: 45/100**

---

### V-04 — Role sequence + Inertia framing (status before story; gaps as commit-risk)

| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| C-01 | Sub-skills invoked in order | PASS | Explicit: status-check before narrative-write; sequence is the design axis |
| C-02 | Existing signals enumerated by namespace | PASS | Full coverage map required *before* narrative; enumeration is pre-condition for synthesis |
| C-03 | Missing signals explicitly named | PASS | Gaps must be known to apply inertia framing — they are inputs, not outputs |
| C-04 | Narrative arc synthesizes signals together | PASS | Gaps inform synthesis retrospectively forced by role sequence; coverage map is the input |
| C-05 | Topic registered with name, date, intent | PARTIAL | Not explicitly surfaced as a required step; may emerge but not guaranteed |
| C-06 | Explicit readiness verdict | PASS | Inertia anchor ("what happens if we commit without this signal?") demands a verdict in closing block |
| C-07 | Gap list prioritized blocking vs. optional | PASS | Blocking/optional split is grounded in real decision exposure — strongest C-07 of the set |
| C-08 | Scannable dashboard with visual hierarchy | PARTIAL | Structure implied by role sequence but no explicit visual template declared |
| C-09 | Session delta | FAIL | No mechanism |
| C-10 | Narrative confidence level | PARTIAL | Inertia framing implies confidence reasoning; likely to emerge but not required |

**V-04 Total: 75/100**

---

### V-05 — Output format + Lifecycle emphasis (terminal blocks; prose confined to STORY)

| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| C-01 | Sub-skills invoked in order | PASS | Five blocks (TOPIC → STRATEGY → STATUS → STORY → VERDICT) impose execution order structurally |
| C-02 | Existing signals enumerated by namespace | PASS | STATUS block is structured data — namespace enumeration is the expected fill pattern |
| C-03 | Missing signals explicitly named | PASS | STATUS block includes gaps as structured data; no room for silence |
| C-04 | Narrative arc synthesizes signals together | PASS | STORY section explicitly confined for prose synthesis; all data is extracted to STATUS first |
| C-05 | Topic registered with name, date, intent | PASS | TOPIC is the *first* named block — registration is the literal entry point |
| C-06 | Explicit readiness verdict | PASS | VERDICT is the terminal block; the eye lands there last — C-06 compliance by layout |
| C-07 | Gap list prioritized blocking vs. optional | PARTIAL | STRATEGY block likely surfaces this; blocking/optional split not explicitly demanded in block spec |
| C-08 | Scannable dashboard with visual hierarchy | PASS | Terminal-style compact blocks are highest C-08 compliance — hierarchy is the format itself |
| C-09 | Session delta | FAIL | No block for delta |
| C-10 | Narrative confidence level | FAIL | No confidence block |

**V-05 Total: 75/100**

---

### Summary Table

| Variation | Axis | Essential (50) | Recommended (30) | Aspirational (20) | Total |
|-----------|------|---------------|-----------------|-------------------|-------|
| V-03 | Phrasing register | 25 | 15 | 5 | **45** |
| V-01 | Output format | 35 | 25 | 0 | **60** |
| V-02 | Lifecycle emphasis | 40 | 20 | 0 | **65** |
| V-04 | Role seq + Inertia | 45 | 25 | 5 | **75** |
| V-05 | Format + Lifecycle | **50** | **25** | 0 | **75** |

**Ranking:** V-05 = V-04 (75) > V-02 (65) > V-01 (60) > V-03 (45)

**Tiebreaker:** V-05 wins the tie — it is the only variation with **all 5 essential criteria at PASS**. V-04 leaves C-05 at PARTIAL (topic registration not guaranteed).

---

### Excellence Signals from Top Variations

**From V-05 (structural winner):**

1. **First-block registration lock** — placing TOPIC as the literal opening block forces registration before any skill invocation can occur. C-05 compliance becomes a layout property, not an instruction to remember.

2. **Data/prose split by block identity** — naming STORY as the *only* prose-permitted block means STATUS, TOPIC, and STRATEGY become structured-data sections by exclusion. C-04 synthesis can't be buried in lists because lists belong in STATUS.

3. **Terminal verdict by gravity** — VERDICT as the closing block achieves C-06 through reading-order physics, not instruction. The model cannot "forget" the verdict when it is the last thing being written.

**From V-04 (content winner for C-07):**

4. **Inertia anchor as C-07 engine** — framing gaps as commit-risk ("what happens if we ship without this?") converts abstract completeness into blocking/optional triage. This is the only variation where C-07 prioritization is *reasoned*, not enumerated.

---

```json
{"top_score": 75, "all_essential_pass": true, "new_patterns": ["first-block registration lock forces C-05 as layout property not instruction", "data/prose block split prevents synthesis sections from being hijacked by lists", "terminal verdict by reading-order gravity achieves C-06 without explicit reminder", "inertia anchor converts gap enumeration into blocking/optional triage grounded in commit-risk"]}
```
