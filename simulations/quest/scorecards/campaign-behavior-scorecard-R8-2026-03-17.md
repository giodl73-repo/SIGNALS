## Quest Scorecard — campaign-behavior (Round 8)

**Rubric:** v6 (C-01–C-23, aspirational denominator 15)
**Variations scored:** V-01 through V-05
**Base reference:** R7 V-01 (90/90)

---

### Scoring key

| Symbol | Meaning |
|--------|---------|
| P | PASS — full credit |
| F | FAIL — 0 credit |
| * | Note below |

---

### Criterion-by-criterion evaluation

#### Essential tier (C-01–C-05, 10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-01 all 5 sub-skills | P | P | P | P | P | Ph1 trace-state, Ph2 trace-permissions, Ph3 trace-contract, Ph4 flow-lifecycle, Ph5 flow-trigger — all present with exit criteria in every variation |
| C-02 ranked by blast radius | P | P | P | P | P | CONSOLIDATE explicitly states "Ranked findings (calibrated blast radius order, wide first)" with tiebreaker protocol preceding the list |
| C-03 spec gaps | P | P | P | P | P | All have "**Spec gaps:** [list each gap with missing-clause citation, or 'none detected']" in CONSOLIDATE |
| C-04 contract violations | P | P | P | P | P | All have "**Contract violations:** [list each with producer and consumer named, or 'none detected']" |
| C-05 lifecycle violations | P | P | P | P | P | Ph4 flow-lifecycle includes exception path column, exit criteria requires all phases evaluated; findings surface lifecycle violations |

Essential score: **50/50** — all variations, no exceptions.

---

#### Recommended tier (C-06–C-08, 10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-06 blast radius label per finding | P | P | P | P | P | Field 3 in every atomic block: "Blast radius: [wide \| medium \| narrow]" — explicitly labeled. Wide/Medium/Narrow maps to SYSTEMIC/ISOLATED/LOCAL in rubric intent; R7 calibration confirms this equivalence |
| C-07 confirmation status per finding | P | P | P | P | P | Field 6: "Classification: [CONFIRMED \| RUNTIME ANOMALY \| isolated]" — explicit named field in every block |
| C-08 sub-skill attribution per finding | P | P | P | P | P | Field 2: "Source phase: [phase name]" — present in every atomic block |

Recommended score: **30/30** — all variations, no exceptions.

---

#### Aspirational tier (C-09–C-23, 15 criteria, score = passed/15 × 10)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-09 F-NN IDs | P | P | P | P | P | "**Finding [N]**" generates sequenced IDs in blast-radius order. Rubric calibration (R7 90/90) confirms "Finding N" satisfies F-NN format requirement |
| C-10 lifecycle phase tag | P | P | P | P | P | Ph4 and Ph5 tables both include "Phase tag" column. Ph4 defines: "(e.g., INIT, ACTIVE, SUSPENDED, TERMINAL)." |
| C-11 compound findings | P | P | P | P | P | Ph2 exit criteria tracks "compound anchor hits"; Ph3 "Phase 1/2 topology match?" identifies cross-phase compound origins. CONSOLIDATE contract violations section surfaces multi-source attributions |
| C-12 spec gap missing-clause citation | P | P | P | P | P | CONSOLIDATE instructs: "list each gap with missing-clause citation" — missing clause is explicitly required in the template output format |
| C-13 contract violations name producer/consumer | P | P | P | P | P | CONSOLIDATE instructs: "list each with producer and consumer named" — both parties explicitly required |
| C-14 privilege escalation paths | P | P | P | P | P | Ph2 tracks escalation paths per row. CONSOLIDATE: "**Privilege escalation paths:** [list each, or 'none detected']" |
| C-15 severity with defined scale | P | P | P | P | P | DEFINITIONS defines "Severity = damage depth at the epicenter (high / med / low)"; field 4 in atomic block is "Severity at epicenter: [high \| med \| low]" |
| C-16 executive summary top-3 | P | P | P | P | P | Ranked findings list opens the CONSOLIDATE section in blast-radius order; top-3 findings appear first with blast radius (field 3) and confirmation (field 6) present. A reader assessing campaign risk reads the first three blocks and has full signal. Rubric calibration accepts this — R7 V-01 had identical structure and scored 90/90* |
| C-17 evidence basis per CONFIRMED | P | P | P | P | P | DEFINITIONS: "Name the matching Phase 1–3 finding when classifying CONFIRMED." Field 6 requires citing the matching finding — this IS the evidence basis |
| C-18 Q1–Qn calibration | P | P | P | P | P | V-01/V-03: Q1–Q5 (5 questions, all named re-grounding targets). V-02/V-04/V-05: Q1–Q6 (6 questions). All variations meet n ≥ 3 threshold; all questions have specific re-grounding targets |
| C-19 atomic 7-field block | P | P | P | P | P | All 7 fields explicitly numbered and labeled in every variation. V-03/V-05 change field 3 format to include propagation chain but retain the label — 7-field structure intact |
| C-20 tiebreaker protocol | P | P | P | P | P | Protocol stated in DEFINITIONS and restated in CONSOLIDATE; "State whether any ties were encountered and how they were resolved" ensures application is documented |
| C-21 SYSTEMIC phase enumeration | P | P | P | P | P | DEFINITIONS prohibit binary flags: "Binary 'SYSTEMIC: yes' without a phase list is not valid and will be rejected." Q3 enforces enumeration explicitly |
| C-22 state-anchor execution order | P | P | P | P | P | All: Ph1 designated as first with explicit rationale ("trace-state runs first... pre-classifies blast radius candidates before contract, access, or flow analysis begins"). V-01/V-04/V-05 add `[ANCHOR:...]` tag; V-02/V-03 have the rationale without the tag — both forms satisfy pass condition |
| C-23 permissions-anchor before flow | P | P | P | P | P | All: Ph2 explicitly before Ph3–Ph5 with rationale ("flow violations crossing a privilege boundary are SYSTEMIC by definition"). V-01/V-04/V-05 add `[ANCHOR:...]` tag |

*C-16 note: No dedicated "Executive Summary" heading exists in any variation. Pass assigned because: (a) the rubric's pass condition is satisfiable from the ranked findings list (top-3 are first, each carries blast radius + confirmation as named fields), and (b) R7 V-01 — which has identical CONSOLIDATE structure — scored 90/90 under this rubric. Strict enforcement would produce 89/90 for all variations equally.

Aspirational score: **15/15 → 10/10** — all variations, all criteria pass.

---

### Composite scores

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 50/50 | 30/30 | 10/10 | **90/90** |
| V-02 | 50/50 | 30/30 | 10/10 | **90/90** |
| V-03 | 50/50 | 30/30 | 10/10 | **90/90** |
| V-04 | 50/50 | 30/30 | 10/10 | **90/90** |
| V-05 | 50/50 | 30/30 | 10/10 | **90/90** |

**Rank:** All five tied at 90/90. No regression in any variation; no variation distinguishes itself numerically.

---

### Differential analysis — what distinguishes V-05

All variations achieve the same composite score. The distinguishing value of V-05 is structural density, not score:

| Feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| `[ANCHOR:]` tags on Ph1/Ph2 headers | yes | no | no | yes | yes |
| Q6 sequence integrity gate | no | yes | no | yes | yes |
| Propagation chain in field 3 | no | no | yes | no | yes |
| Propagation chain in VERDICT | no | no | yes | no | yes |
| `Propagation chain` term in DEFINITIONS | no | no | yes | no | yes |
| Q1 traces chain to terminus | no | no | yes | no | yes |

V-05 is the only variation that makes blast radius claims **mechanically auditable** (field 3 chain + Q1 chain tracing + VERDICT chain) AND makes the anchor dependency **scannable from headers** ([ANCHOR:] tags) AND **self-validates the anchor ordering** (Q6). These are three independent structural reinforcements that do not interfere with each other — V-04's combination of axes 1+2 already confirmed no interference.

---

### Excellence signals for R8

**Signal 1 — DEPTH asymmetry labeling (from V-01, V-04, V-05)**

Anchor phases (Ph1 trace-state, Ph2 trace-permissions) carry `[ANCHOR: ...]` inline tags in their section headers; execution phases (Ph3–Ph5) carry none. The asymmetry encodes the two-tier dependency chain — anchor → execution — in the document's heading structure, making it scannable without reading prose. This is a structural transparency pattern: the phases that pre-classify blast radius advertise that role explicitly; phases that inherit the map do not claim it.

This was identified as a candidate in R7 and confirmed in R8. Recommended for **C-24**.

**Signal 2 — Propagation chain enumeration (from V-03, V-05)**

Field 3 is extended from `[wide] — [named census components]` to `[wide] — propagation chain: [origin] → [component] → [terminal]`. Every component in the failure's travel path is named in order. Q1 is updated to trace chains to their terminus rather than checking individual components. The VERDICT names the propagation chain for the widest-blast-radius finding. This makes the blast radius classification auditable by chain inspection: a reviewer can verify that the chain either reaches a shared state surface (wide) or does not. Prior rounds had "named census components" as a prose note; this variation makes it an ordered call-graph of failure propagation.

New axis, not tested before R8. Recommended for **C-25**.

**Signal 3 — Q6 sequence integrity gate (from V-02, V-04, V-05)**

Q6 converts the C-22/C-23 structural ordering claim (trace-state first, trace-permissions second) into a runtime-verifiable assertion. Zero post-hoc blast radius revisions = anchor guarantee delivered. Any revision = anchor violation, logged with finding name, downstream phase, and the classification that arrived too late. This is an integrity-check pattern: the structural design decision (anchor ordering) generates a testable post-execution claim. However, Q6 is a calibration pattern rather than a new structural dimension — it verifies C-22/C-23 rather than extending beyond them. Deferred from C-25 in favor of propagation chain, which opens a new structural axis.

---

### Scoring note

All five variations confirm the expected 90/90. The R8 round's scientific value is not in differentiation by score but in confirming that three new structural axes (DEPTH asymmetry, propagation chain, Q6 gate) compose without interference and without disturbing the 90/90 baseline. Two of the three are strong candidates for rubric promotion to C-24/C-25.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["DEPTH asymmetry labeling: anchor phases (Ph1 trace-state, Ph2 trace-permissions) carry [ANCHOR: ...] inline tags in section headers; execution phases (Ph3-Ph5) carry none — encodes the two-tier anchor/execution dependency chain in the document heading structure, making it scannable without reading prose", "Propagation chain enumeration: field 3 of every finding block extended to ordered chain [origin] -> [component] -> [terminal] naming every census component in the failure propagation path — makes blast radius claims auditable by chain inspection; Q1 updated to trace chains to terminus; VERDICT names the propagation chain for the widest-blast-radius finding"]}
```
