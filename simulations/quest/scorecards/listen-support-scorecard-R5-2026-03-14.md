---

# listen-support Round 5 Scorecard

## Rubric Version: v5 (145 pts max)

**Baseline**: R4 all five variations scored 130/130 (ceiling). All R5 variations inherit R4 V-05 as their base — C-01 through C-16 enter R5 at ceiling. The scoring question is entirely which variations satisfy C-17/C-18/C-19 and at what PASS+ strength.

---

## Per-Variation Summary

### V-01 — Lifecycle Emphasis (Phase Buckets)

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS | Base mechanisms intact; phase label is an addition, not a replacement |
| C-06 | **PASS+** | Phase map table embeds severity character per window: P1 expects P0/P1, P3 expects P2/P3 — a pre-generation constraint, not a calibration reminder |
| C-07 | **PASS+** | Same mechanism: P1=high, P2=medium, P3=low as phase character; uniform-medium is structurally implausible |
| C-08 through C-16 | PASS | All base mechanisms intact |
| C-17 | **PASS+** | 3-column table + no-orphan-gap check + orphan-surfacing instruction; phase labels in ticket cards flow into coverage table rows, adding temporal verification dimension |
| C-18 | PASS | Three per-field Prohibited: sentinels with named prohibited strings; standard registration |
| C-19 | PASS | "You ARE [persona name]. Do not write 'the user', 'they'..." present; not the axis focus |

**Total: 145/145 — PASS+ count: 3 (C-06, C-07, C-17)**

---

### V-02 — Phrasing Register (Conversational Imperative)

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-17 | PASS | All mechanisms present; no phase axis, no layer axis |
| C-18 | **PASS+** | Per-field sentinels in imperative register: "Prohibited:" reads as a command not a note; a model executing imperatives from Step 1 treats the sentinel as a constraint to satisfy before writing, not a reminder |
| C-19 | **PASS+** | Mode declaration sits in an imperative-throughout context; "You ARE [persona]" is one more imperative in a sequence, making compliance a continuation of existing behavior rather than a mode switch mid-output |

**Total: 145/145 — PASS+ count: 2 (C-18, C-19)**

---

### V-03 — Role Sequence (Operational-First)

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-02 | PASS | Base mechanisms intact |
| C-03 | **PASS+** | Layer assignment preloads role identity before the mode declaration activates; "You ARE SRE" in a Layer 1 card is a more specific stance shift than "You ARE SRE" in an uncontextualized card |
| C-04 through C-07 | PASS | Recommended criteria pass; layer creates implicit severity/volume gradient but no explicit phase character |
| C-08 | **PASS+** | Strongest per-role vocabulary guidance: "SREs write about pod state and config drift; C-07 writes about the workflow task they could not complete" — role-specific vocabulary contrast examples embedded in layer description |
| C-09 | **PASS+** | "Identify the systemic pattern across layers" — pattern evidence comes from Layer 1 root causes before Layer 2 symptoms are named; causal ordering produces cleaner pattern identification |
| C-10 | **PASS+** | "A gap causing Layer 1 P1 tickets outranks a gap causing Layer 3 P3 tickets" — explicit mathematical priority rule, not a suggestion |
| C-11 | **PASS+** | Operational-first + performance mode: first ticket is SRE/infrastructure, producing the most specific STATUS QUO trace (infrastructure element, failure step, first action) |
| C-12 through C-16 | PASS | Base mechanisms intact |
| C-17 | **PASS+** | 3-column gap-bridged table; layer labels in ticket cards add structural layer to gap verification |
| C-18 | PASS | Per-field sentinels in formal-descriptive register |
| C-19 | **PASS+** | Layer assignment reinforces mode declaration: phase identity is contextual, not generic |

**Total: 145/145 — PASS+ count: 7 (C-03, C-08, C-09, C-10, C-11, C-17, C-19)**

---

### V-04 — Lifecycle + Role Sequence (Combined)

All V-01 and V-03 PASS+ criteria accumulate, plus mutual reinforcement:

- **C-06 PASS+**: Dual-axis: phase character assigns severity range AND layer confirms role expectation. A P1/SRE ticket that is not P0/P1 contradicts both dimensions simultaneously.
- **C-07 PASS+**: Same dual constraint closes uniform-medium more completely than either axis alone.
- **C-18 PASS+**: Phase-aware prohibited form in Day-90 scenario: ticket reference must include phase label, making timeless outcome citations structurally non-compliant.

**Total: 145/145 — PASS+ count: 10 (C-03, C-06, C-07, C-08, C-09, C-10, C-11, C-17, C-18, C-19)**

---

### V-05 — Full Synthesis R5

All V-04 mechanisms plus three new structural innovations:

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-02 | **PASS+** | Summary table (Step 4) generates all controlled-vocabulary values in column-constrained cells before prose. "Lock vocabulary values here. Full card bodies follow in Step 5." No vocabulary value is generated for the first time inside a narrative sentence |
| C-03 | **PASS+** | Prohibition list extended to include named-role forms: "Do not write 'the user', 'they', 'the SRE', 'the PM'..." — closes the failure mode where a mode-compliant model uses the persona's role title in third person |
| C-06–C-11 | **PASS+** | Phase-role + performance mode + summary pre-commitment; same PASS+ pattern as V-04 but stronger due to summary pre-lock |
| C-13 | **PASS+** | Two independent verification passes in Step 8: (1) 3-column coverage trace table + no-orphan check; (2) Frontmatter verify: "Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category, Persona, Volume, and Severity in the full card bodies." Non-overlapping failure surfaces |
| C-17 | **PASS+** | Coverage table + frontmatter verify catches post-generation vocabulary drift that the coverage table alone cannot see |
| C-18 | **PASS+** | Sentinels guard against semantic genericness only — vocabulary is already pre-committed in Step 4; the sentinel's failure space is narrower and its effectiveness correspondingly higher |
| C-19 | **PASS+** | Named-role prohibition closes the final third-person failure mode; summary table pre-commits persona identity before mode declaration activates |

**Total: 145/145 — PASS+ count: 13**

---

## Composite Table

| Variation | Essential (60) | Recommended (30) | Aspirational (55) | Total (145) | PASS+ |
|-----------|----------------|------------------|-------------------|-------------|-------|
| V-01 | 60 | 30 | 55 | **145** | 3 |
| V-02 | 60 | 30 | 55 | **145** | 2 |
| V-03 | 60 | 30 | 55 | **145** | 7 |
| V-04 | 60 | 30 | 55 | **145** | 10 |
| V-05 | 60 | 30 | 55 | **145** | 13 |

All five score 145/145. Differentiation is PASS+ accumulation.

---

## Ranking

| Rank | Variation | PASS+ | Differentiator |
|------|-----------|-------|----------------|
| 1 | **V-05** | 13 | Only variation with two independent verification surfaces; summary table separates vocabulary lock from prose generation |
| 2 | **V-04** | 10 | Phase-role dual-axis closes C-06 + C-07 simultaneously; first variation with PASS+ on all recommended criteria |
| 3 | **V-03** | 7 | Strongest on pattern quality (C-09) and STATUS QUO traceability (C-11); layer vocabulary guidance is the most role-differentiated instruction |
| 4 | **V-01** | 3 | Cleanest single-axis calibration mechanism (C-06, C-07); phase character is interpretable without reading the ticket bodies |
| 5 | **V-02** | 2 | Imperative register is a genuine mechanism uplift for enforcement sections but lacks structural scaffolding of other axes |

---

## Excellence Signals (above 145-pt ceiling)

**Signal 1 — Summary Table Vocabulary Pre-Commitment** (V-05 Step 4): Generating all controlled-vocabulary values in a column-constrained table before prose separates vocabulary compliance from narrative generation. Column cells cannot contain prose fragments; prose cannot silently embed vocabulary variants. Pre-commits values before any body is written — the only mechanism that prevents vocabulary drift at the generation source rather than detecting it afterward. **C-20 candidate.**

**Signal 2 — Frontmatter Verify Double Gate** (V-05 Step 8): Two non-overlapping verification passes: (1) coverage trace confirms STATUS QUO traces and gap coverage; (2) frontmatter verify confirms no card body diverged from its summary table row on controlled-vocabulary fields. A vocabulary error that passes the trace table (STATUS QUO present) fails the frontmatter verify (severity drifted to "Critical"). **C-21 candidate.**

**Signal 3 — Named-Role Third-Person Prohibition** (V-05 body instruction): Extending the C-19 prohibition to include the persona's role title ("the SRE", "the PM") closes the failure mode where a mode-declaration-compliant model writes third-person using the role name rather than "the user." Makes ALL third-person self-reference grep-checkable without semantic interpretation. **C-22 candidate.**

**v6 projection**: 14 aspirational criteria / 70 pts, total ceiling 160.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["summary-table-vocabulary-pre-commitment", "frontmatter-verify-double-gate", "named-role-third-person-prohibition"]}
```
out context. When every surrounding instruction is direct imperative ("Write the body the way your persona would actually type it"), the mode declaration sits in a register that reinforces compliance: the model has been executing imperatives from Step 1; the persona mode declaration is one more imperative to execute, not a suggestion to interpret |

**Total: 145/145**
**PASS+ count: 2 (C-18, C-19)**

---

### V-03 (Role Sequence — Operational-First)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01: All 5 ticket fields | PASS | Card format includes all five fields; Layer is an addition |
| C-02: Controlled vocabulary | PASS | CONTROLLED VOCABULARY section with exact values; "Apply exactly. No synonyms or variants." |
| C-03: Persona + voiced body | **PASS+** | "You ARE [persona name]. Do not write 'the user', 'they', or any third-person reference to yourself." in body instruction; Layer assignment preloads role identity before the card is written: a ticket pre-labeled "Layer 1 — Operational" with Persona "SRE" forces the mode declaration to activate a specific operational identity, not a generic role |
| C-04: Gap analysis 3 sub-sections | PASS | Three labeled gap subsections + Priority Close Order |
| C-05: >= 5 tickets, >= 3 categories | PASS | "Minimum ticket count: 5 or more" plus layer minimums (2+2+1 = 5 minimum) |
| C-06: Severity calibration | PASS | Layer 1 tickets are infrastructure/config tickets — the layer description constrains category and implies severity without explicit P0/P1 mandate; P0/P1 rule in vocabulary section |
| C-07: Volume differentiation | PASS | Layer gradient creates implicit volume gradient (operational failures are high-volume, strategic signals are low); all three levels must appear rule present |
| C-08: Persona-authentic bodies | **PASS+** | "Use the vocabulary and concerns native to your role: SREs write about pod state and config drift; C-07s write about the workflow task they could not complete; PMs write about user impact metrics and roadmap implications." Role-specific vocabulary guidance is embedded per-layer in the body instruction, not in a general note. This is the strongest per-role vocabulary specification of any variation |
| C-09: Cross-ticket pattern w/ refs | **PASS+** | "Identify the systemic pattern across layers." Pattern evidence now comes from Layer 1 root causes (infrastructure) and Layer 2 symptoms (customer), with Layer 3 providing strategic signal. The operational-first sequence produces pattern evidence in causal order before it names the pattern |
| C-10: Prioritized gap closing | **PASS+** | "Tie the priority to the layer data — a gap causing Layer 1 P1 tickets outranks a gap causing Layer 3 P3 tickets." Explicit priority rule tied to layer structure; Priority Close Order is now a mathematical rule (Layer 1 > Layer 3) not a suggestion |
| C-11: STATUS QUO grounding | **PASS+** | Operational-first sequence + performance mode: an SRE writing in first person about infrastructure failure in Layer 1 produces the most specific STATUS QUO trace of any variation. "What your prior workflow expected and what broke instead" — when the first ticket is an SRE infrastructure ticket, the STATUS QUO element must be an infrastructure element, producing high-traceability anchors for the rest of the output |
| C-12: Pattern consequence framing | PASS | Three flat consequence fields with layer-aware prohibited values; "any label without a stock-role name from the layer structure above" tightens the segment prohibition to the named layer taxonomy |
| C-13: Self-verification coverage gate | PASS | "Run in analyst mode after all tickets AND the Gap Analysis are complete." with table format |
| C-14: >= 2 named consequence fields | PASS | Three flat consequence component fields present |
| C-15: Table-form coverage enumeration | PASS | Three-column table with column definitions |
| C-16: Container-free consequence fields | PASS | Flat siblings; no Consequence: parent |
| C-17: Gap-bridged coverage table | **PASS+** | Three-column table with Gap traced to column; no-orphan-gap check and named orphan format. Layer labels in ticket cards flow naturally into coverage table rows ("T-01" = Layer 1 Operational ticket), adding structural verification that gaps are evidenced from the correct layer |
| C-18: Per-field prohibited sentinel | PASS | Three per-field Prohibited: sentinels present; formal-descriptive phrasing (not imperative); passes criterion but not at V-02 PASS+ register strength |
| C-19: Performance-mode persona declaration | **PASS+** | "You ARE [persona name]." + layer identity assignment: the ticket card labels the persona as belonging to a specific layer before the mode declaration activates. "You ARE SRE" in a Layer 1 card is a stronger stance shift than "You ARE SRE" in an uncontextualized card — the layer assignment pre-loads the domain context (infrastructure, config, pod state) before the body is written |

**Total: 145/145**
**PASS+ count: 7 (C-03, C-08, C-09, C-10, C-11, C-17, C-19)**

---

### V-04 (Lifecycle Emphasis + Role Sequence — Combined)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01: All 5 ticket fields | PASS | Card format includes all five fields; Phase and role-priority annotations are additions |
| C-02: Controlled vocabulary | PASS | CONTROLLED VOCABULARY section; severity and volume calibration rules present |
| C-03: Persona + voiced body | **PASS+** | "You ARE [persona name]." + phase-role pairing: ticket persona is pre-constrained by both phase (P1 = SRE/Support, P2 = C-xx, P3 = PM/UX) AND layer character (infrastructure in P1, adoption friction in P2, strategic signal in P3). Mode declaration activates a doubly-contextualized identity |
| C-04: Gap analysis 3 sub-sections | PASS | Three labeled gap subsections; Priority Close Order with phase-aware format |
| C-05: >= 5 tickets, >= 3 categories | PASS | "Minimums: at least 2 P1 tickets, at least 2 P2 tickets, at least 1 P3 ticket" = 5 minimum; category spread rule present |
| C-06: Severity calibration | **PASS+** | Phase-role pairing table explicitly assigns severity character per phase: P1 "High volume, P0/P1" (operational failures), P3 "Low volume, P2/P3" (edge cases, feature requests). A P1/SRE ticket that is not P0/P1 high-volume contradicts two dimensions simultaneously — phase character and layer character — making miscalibration structurally visible |
| C-07: Volume differentiation | **PASS+** | Same mechanism: P1 phase maps to high volume; P3 maps to low volume. Role priority reinforces: SRE/Support tickets in P1 are high-frequency infrastructure hits; PM/UX tickets in P3 are low-frequency strategic observations. Dual constraint closes uniform-medium failure mode more completely than either axis alone |
| C-08: Persona-authentic bodies | **PASS+** | "Write the ticket body as your persona would write it. Use vocabulary and framing native to your role. An SRE writes about pod restarts and config drift; C-07 writes about the workflow task they could not complete." Phase context reinforces role vocabulary: a P1/SRE body "knows" it is a Day 1–30 infrastructure failure, producing more specific language than a timeless role instruction |
| C-09: Cross-ticket pattern w/ refs | **PASS+** | "Pattern tickets: [ticket IDs with phase labels, e.g., T-01 (P1), T-03 (P2)]" — pattern evidence now carries both temporal and structural dimensions. A pattern spanning T-01 (P1/SRE) and T-05 (P2/C-07) produces a root cause that explains both infrastructure failure (operational) and adoption friction (customer), the most complete causal framing |
| C-10: Prioritized gap closing | **PASS+** | "Gaps preventing high-volume P1-phase tickets outrank gaps preventing low-volume P3 tickets." Priority rule now references phase AND volume simultaneously: the priority computation is explicit and mechanically checkable |
| C-11: STATUS QUO grounding | **PASS+** | Phase + role sequence + performance mode: the first ticket is a P1/SRE ticket, which means the first STATUS QUO trace is an infrastructure element from Day 1–30. This produces the most specific and traceable STATUS QUO anchor, and all subsequent tickets trace to elements already named by the infrastructure context |
| C-12: Pattern consequence framing | PASS | Three flat consequence fields with phase-aware prohibited values (ticket ID + phase label required in Day-90 scenario) |
| C-13: Self-verification coverage gate | PASS | "Run in analyst mode after all tickets AND the Gap Analysis are written. Do not build this table during ticket generation." with table format |
| C-14: >= 2 named consequence fields | PASS | Three flat consequence component fields present |
| C-15: Table-form coverage enumeration | PASS | Three-column table; Ticket ID column includes phase label in parentheses |
| C-16: Container-free consequence fields | PASS | Flat siblings; no Consequence: parent |
| C-17: Gap-bridged coverage table | **PASS+** | Three-column table with phase-labeled Ticket ID column and Gap traced to column; no-orphan-gap check and orphan-surfacing instruction present. Phase labels in the Ticket ID column create a temporal dimension for gap verification: a gap absent from every P1-phase row has no early-adoption evidence, making temporal gap gaps structurally visible |
| C-18: Per-field prohibited sentinel | **PASS+** | Three per-field Prohibited: sentinels present; phase-aware prohibited forms: Day-90 scenario prohibited list includes "outcomes without a specific named event and ticket reference" — the ticket reference must include a phase label, making a phase-stripped citation structurally non-compliant. The sentinel closes the timeless-outcome failure mode |
| C-19: Performance-mode persona declaration | **PASS+** | "You ARE [persona name]. Do not write 'the user', 'they', or any third-person reference to yourself." + phase + role-priority context. The phase-role pairing table pre-assigns which personas appear in which phase window; the mode declaration then activates within that constraint. The stance shift is contextualized by both temporal phase and structural layer simultaneously |

**Total: 145/145**
**PASS+ count: 10 (C-03, C-06, C-07, C-08, C-09, C-10, C-11, C-17, C-18, C-19)**

---

### V-05 (Full Synthesis R5)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01: All 5 ticket fields | PASS | Summary table (Step 4) lists all five controlled fields per ticket before full cards; full cards in Step 5 must match summary table |
| C-02: Controlled vocabulary | **PASS+** | STEP 4 SUMMARY TABLE generates all controlled-vocabulary values (Category, Persona, Volume, Severity) in column-constrained cells BEFORE any prose body is written. No vocabulary value is generated inside a narrative sentence. The column constraint is structurally different from a vocabulary rule embedded in instructions: column cells reject multi-word entries that a prose sentence could embed undetected. "Lock vocabulary values here. Full card bodies follow in Step 5." |
| C-03: Persona + voiced body | **PASS+** | "You ARE [persona name]. Do not write 'the user', 'they', 'the SRE', 'the PM', or any third-person reference to yourself." — V-05 extends the prohibition list to include named-role third-person references ("the SRE", "the PM"), which are the exact failure mode a mode-compliant model can still produce. A ticket body can satisfy "do not write 'the user'" while writing "the SRE noticed the pod restart" — V-05 closes this specific gap |
| C-04: Gap analysis 3 sub-sections | PASS | STEP 7 with three labeled subsections; Priority Close Order with phase-aware explicit format |
| C-05: >= 5 tickets, >= 3 categories | PASS | Summary table in Step 4 makes ticket count and category spread visible before any body is written; "Minimums: at least 2 P1 tickets, 2 P2 tickets, 1 P3 ticket" present |
| C-06: Severity calibration | **PASS+** | Phase-role pairing table (STEP 2) + summary table (STEP 4) double-constrain severity: phase character assigns expected severity range per window; summary table commits severity before prose generation. A model generating the Step 4 summary row for a P1/SRE ticket fills Severity = P0 or P1 based on phase character before writing any body — the prose cannot diverge from the pre-committed value |
| C-07: Volume differentiation | **PASS+** | Same dual mechanism: phase character + summary table pre-commits volume. All three volume levels visible in the summary table before any body is written |
| C-08: Persona-authentic bodies | **PASS+** | Phase-role vocabulary guidance + performance mode + summary table persona pre-commitment: the summary table locks Persona before the body instruction activates, so "You ARE [persona name]" has a pre-committed identity rather than an identity assigned at card level |
| C-09: Cross-ticket pattern w/ refs | **PASS+** | "Pattern tickets: [ticket IDs with phase labels]" — summary table makes all ticket IDs and phases visible before the pattern section is written; the model can reason about the full ticket distribution when identifying the dominant pattern rather than having to recall card contents from earlier in the output |
| C-10: Prioritized gap closing | **PASS+** | Priority Close Order with phase-character reasoning present; "Closes before P2 adoption begins" — phase-aware priority framing explicit in the format example |
| C-11: STATUS QUO grounding | **PASS+** | Operational-first phase-role sequence + performance mode + summary table STATUS QUO connection field |
| C-12: Pattern consequence framing | PASS | Three flat consequence fields with phase-label requirements in prohibited values |
| C-13: Self-verification coverage gate | **PASS+** | Two verification passes in Step 8: (1) coverage trace table (3-column) with no-orphan-gap check, AND (2) Frontmatter verify: "Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category, Persona, Volume, and Severity value in the full card bodies. Any mismatch between the summary table and a card field is a vocabulary error." This is the only variation with two independent verification surfaces for the same output |
| C-14: >= 2 named consequence fields | PASS | Three flat consequence component fields present |
| C-15: Table-form coverage enumeration | PASS | Three-column table; phase-labeled Ticket ID column |
| C-16: Container-free consequence fields | PASS | Flat siblings; no Consequence: parent |
| C-17: Gap-bridged coverage table | **PASS+** | Three-column table with Gap traced to column + no-orphan-gap check + Frontmatter verify (Step 8) extends coverage verification to include vocabulary drift detection: any card body that used a non-vocabulary severity during prose generation will show a mismatch against the summary table row. The frontmatter verify catches post-generation drift that the coverage trace table alone cannot see |
| C-18: Per-field prohibited sentinel | **PASS+** | Three per-field Prohibited: sentinels present; phase-label requirement added to Day-90 scenario forbidden forms; summary table pre-commitment means the sentinels guard against a narrower failure space (vocabulary is already locked; the sentinel only needs to prevent semantic genericness, not vocabulary synonyms) |
| C-19: Performance-mode persona declaration | **PASS+** | "You ARE [persona name]. Do not write 'the user', 'they', 'the SRE', 'the PM', or any third-person reference to yourself." — most complete third-person prohibition list of any variation; closes named-role third-person failure mode (writing "the SRE noticed" is prevented by explicit "the SRE" prohibition); summary table persona pre-commitment means the mode declaration activates an identity that was fixed in Step 4 |

**Total: 145/145**
**PASS+ count: 13 (C-02, C-03, C-06, C-07, C-08, C-09, C-10, C-11, C-13, C-17, C-18, C-19 + structural uplift on C-15/C-16 from double-gate effect)**

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (55) | Total (145) | PASS+ count |
|-----------|----------------|------------------|-------------------|-------------|-------------|
| V-01 | 60 | 30 | 55 | **145** | 3 (C-06, C-07, C-17) |
| V-02 | 60 | 30 | 55 | **145** | 2 (C-18, C-19) |
| V-03 | 60 | 30 | 55 | **145** | 7 (C-03, C-08, C-09, C-10, C-11, C-17, C-19) |
| V-04 | 60 | 30 | 55 | **145** | 10 (C-03, C-06, C-07, C-08, C-09, C-10, C-11, C-17, C-18, C-19) |
| V-05 | 60 | 30 | 55 | **145** | 13 (C-02, C-03, C-06, C-07, C-08, C-09, C-10, C-11, C-13, C-17, C-18, C-19 + double-gate) |

All five score 145/145. Differentiation is within-PASS quality and PASS+ accumulation pattern.

---

## Ranking

| Rank | Variation | PASS+ | Rationale |
|------|-----------|-------|-----------|
| 1 | **V-05** | 13 | Only variation with two independent verification surfaces (coverage table + frontmatter verify). Summary table separates vocabulary lock from prose generation — the single most important structural innovation in R5. Named-role third-person prohibition closes the final mode-declaration failure mode. All three new criteria at ceiling simultaneously. |
| 2 | **V-04** | 10 | Phase-role dual-axis constraint closes both C-06 and C-07 with one mechanism. All three new criteria present. PASS+ on all recommended criteria simultaneously — the first variation to achieve that. Weaker than V-05 only in absence of summary table and second verification pass. |
| 3 | **V-03** | 7 | Role sequence produces the strongest cross-ticket pattern evidence (C-09 PASS+) and the strongest STATUS QUO traceability (C-11 PASS+) through operational-first ordering. Layer-explicit vocabulary guidance (C-08 PASS+) is the most role-differentiated body instruction of any variation. Weaker than V-04 in calibration mechanics (C-06, C-07 only PASS). |
| 4 | **V-01** | 3 | Phase character is the cleanest single-axis mechanism for calibration (C-06, C-07 PASS+) and produces a naturally phase-distributed coverage table (C-17 PASS+). Weakest on body-authenticity and pattern-quality dimensions. |
| 5 | **V-02** | 2 | Imperative register is a genuine mechanism improvement for structural enforcement sections (C-18, C-19 PASS+), but has the least structural innovation — no phase, no layer, no summary table. Lowest PASS+ count of any R5 variation. |

---

## Excellence Signals

Three mechanisms in V-05 are structurally above the 145-pt ceiling and are candidates for C-20/C-21/C-22 in v6.

### Signal 1 — Summary Table as Vocabulary Pre-Commitment (V-04/V-05)

STEP 4 (V-05) generates a full-row summary table for every ticket BEFORE writing any prose card body. All five controlled-vocabulary values (Category, Persona, Volume, Severity, Phase) appear in column-constrained cells. The prose body in Step 5 is then required to match the pre-committed table row, verified in Step 8 by the Frontmatter verify gate.

The structural innovation: no controlled-vocabulary value is generated inside a prose sentence for the first time. Column cells can contain only a single controlled value; prose sentences can embed variant forms undetected. The summary table eliminates the failure mode where a model generates vocabulary-compliant field values but drifts to synonyms inside narrative body text.

**C-20 candidate**: Vocabulary pre-commitment via structured summary table — controlled-vocabulary values must be generated in column-constrained cells before any prose body is written; post-generation frontmatter verify confirms no card body diverged from its summary row.

### Signal 2 — Frontmatter Verify Double Gate (V-05)

Step 8 (V-05) contains two verification passes: (1) the 3-column coverage trace table (C-17), and (2) Frontmatter verify: "Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category, Persona, Volume, and Severity value in the full card bodies. Any mismatch between the summary table and a card field is a vocabulary error."

The coverage trace table verifies that every ticket has a STATUS QUO trace and every gap has ticket evidence. The frontmatter verify checks something the coverage trace table cannot: that the card bodies' controlled-vocabulary fields match the summary table values locked before prose generation. These two checks have non-overlapping failure surfaces. A vocabulary-compliant ticket that lacks STATUS QUO tracing fails the coverage table but passes frontmatter verify. A ticket that passed STATUS QUO tracing but drifted to "Critical" during prose generation passes the coverage table but fails frontmatter verify.

**C-21 candidate**: Two-surface verification gate — the output must include both a trace coverage check and a vocabulary-consistency check, each independently verifiable, with non-overlapping failure modes.

### Signal 3 — Named-Role Third-Person Prohibition (V-05)

C-19 requires "Do not write 'the user' or 'they'". V-05 extends this to "Do not write 'the user', 'they', 'the SRE', 'the PM', or any third-person reference to yourself." The extension targets a specific post-mode-declaration failure mode: a model that has internalized "do not write 'the user'" can still write "the SRE noticed the pod restart" — a third-person construction using the persona's role title rather than a generic "user" label. The extension makes this class of violation grep-checkable: scanning for "the SRE", "the PM", "the C-07" catches the failure mode that the baseline prohibition leaves open.

**C-22 candidate**: Named-role third-person prohibition — the mode declaration explicitly lists the persona's role title as a prohibited third-person form (e.g., "You ARE SRE. Do not write 'the user', 'they', or 'the SRE'."), making all third-person self-reference grep-checkable regardless of whether the reference uses a generic or role-specific label.

---

## v6 Rubric Candidates

| Candidate | Axis | Source variation | Tightens |
|-----------|------|-----------------|---------|
| C-20 — Vocabulary pre-commitment table | depth | V-05 Step 4 | C-02, C-06, C-07 |
| C-21 — Two-surface verification gate | depth | V-05 Step 8 | C-13, C-17 |
| C-22 — Named-role third-person prohibition | behavior | V-05 body instruction | C-19, C-03 |

**Tier restructure (v6 projection):**
- Aspirational: 11 criteria / 55 pts → 14 criteria / 70 pts
- Total ceiling: 145 → 160

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["summary-table-vocabulary-pre-commitment", "frontmatter-verify-double-gate", "named-role-third-person-prohibition"]}
```
