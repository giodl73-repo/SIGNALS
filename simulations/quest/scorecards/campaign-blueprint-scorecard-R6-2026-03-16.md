Now I have complete content for all five R6 variants. Let me score each against the rubric.

---

## campaign-blueprint — Quest Score R6

**Rubric:** campaign-blueprint-rubric-v6-2026-03-16.md
**Ceiling:** 158 (150 base + 8 excellence)

---

### Scoring Framework

| Tier | Criteria | Max |
|------|----------|-----|
| Essential | C-01 through C-05 (×12 each) | 60 |
| Recommended | C-06, C-07, C-08 (×10 each) | 30 |
| Aspirational | C-09 through C-24 (×5 each, 12 criteria) | 60 |
| Excellence | C-11 through C-14 (×2 each) | 8 |

PARTIAL = 50% of weight.

---

## V-01 — C-23 Location Test: Matrix Inertia Grounding, Abstract Per-Site Labels

**Key structural feature:** Inertia-grounded CONVICTION TYPE labels in matrix; per-site reminders use *abstract* labels (Factual / Optionality / Emotional without inertia grounding). Retains C-24 traceability instruction. Three-field per-site reminders.

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | All three artifacts produced | PASS | SETUP + three full artifact sections + CAMPAIGN REFLECTION + CAMPAIGN CLOSE |
| C-02 | Canonical paths | PASS | All three paths match canonical form with `{topic}` and `{date}` variables |
| C-03 | Topic identity consistency | PASS | Identity established in SETUP step 1; inertia baseline locks topic; matrix CARRIES FORWARD field propagates to all artifacts |
| C-04 | Execution order | PASS | Spec → Proposal → Pitch with GATE at each transition; CAMPAIGN REFLECTION phases after pitch |
| C-05 | Minimum structure per sub-artifact | PASS | Spec: PURPOSE/REQUIREMENTS/DESIGN/CONSTRAINTS/OPEN QUESTIONS. Proposal: 3 options + do-nothing + per-option structure + recommendation with 3 reasons. Pitch: 3 versions (EXEC/DEV/MAKER) with Hook/What/Why/CTA + ANTI-POSITIONING |

**Essential: 5/5 PASS → 60/60**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-06 | Proposal respects spec | PASS | Per-site PRESERVE: "all spec design decisions — do not re-open anything the spec resolved." Explicit instruction present |
| C-07 | Pitch crystallizes recommended option | PASS | PRESERVE: "recommended option from proposal — crystallize, do not reconsider"; DEV explicitly: "references the technical design from the spec explicitly"; MAKER: "plain language only" |
| C-08 | Campaign framing | PASS | CAMPAIGN SETUP names topic and artifacts; CAMPAIGN CLOSE table lists all three artifact paths with scout signal consumed + open questions columns |

**Recommended: 3/3 PASS → 30/30**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-09 | Narrative arc | PASS | CONVICTION TYPE differentiation across all three artifacts enforces non-repetition; per-site reminder explicitly scopes each artifact's role; FINDINGS CONVICTION DELTA sub-field asks what each version establishes that prior artifacts could not make visceral |
| C-10 | Scout signal pull | PASS | READ field at each artifact names specific scout namespace (scout-requirements → spec; scout-feasibility → proposal; scout-positioning → pitch); REQUIREMENTS instruction "Pull scout-requirements if available"; inertia baseline links to traceability |
| C-15 | Artifact contract | PASS | Full contract matrix with all four required fields (READ/WRITE/PRESERVE/CARRIES FORWARD) + CONVICTION TYPE (superset, D4 rule) for all three artifacts |
| C-16 | Post-execution FINDINGS block | PASS | CAMPAIGN REFLECTION phase with labeled FINDINGS block and named sub-fields (CONVICTION DELTA, NEAR-DUPLICATE CONTENT, RESIDUAL QUESTIONS); phase gate ensures post-execution placement |
| C-17 | Dual-mechanism defense in depth | PASS | Pre-execution contract matrix (full four fields → C-15 FULL) AND named FINDINGS template with explicit sub-fields (CONVICTION DELTA / NEAR-DUPLICATE CONTENT / RESIDUAL QUESTIONS) |
| C-18 | Double-prohibition FINDINGS placement | PASS | "This phase begins only after the pitch file exists on disk — not before pitch production begins, not during pitch production." Both "not before" and "not during" explicitly stated |
| C-19 | Structural double-prohibition | PASS | CAMPAIGN REFLECTION is a named phase with its own section header; GATE before it: "Do not begin Campaign Reflection until [pitch file] is written to disk"; double-prohibition encoded as phase boundary + sequencing constraint |
| C-20 | Contract proximity anchoring | PASS | Per-artifact "Contract reminder" at each execution site with READ and PRESERVE labeled fields (implied by C-22 superset rule) |
| C-21 | Conviction typing | PASS | Each artifact carries declared CONVICTION TYPE label; FINDINGS CONVICTION DELTA block typed to pitch's emotional conviction role |
| C-22 | Per-site conviction type restatement | PASS | All three per-site reminders include READ + PRESERVE + CONVICTION TYPE. Spec: "Factual — assert what is true; do not argue or persuade." Proposal: "Optionality — evaluate trade-offs against spec facts; do not re-assert facts." Pitch: "Emotional — convert factual and optionality conviction into per-audience urgency." Three fields present at all three sites |
| C-23 | Inertia-anchored conviction arc | **PARTIAL** | Matrix CONVICTION TYPE row is fully inertia-grounded: "Factual — names the problem the inertia baseline creates," "Optionality — prices the cost of inertia against each alternative," "Emotional — makes the inertia cost visceral and per-audience-specific." D7 requires "an inertia model defined at the campaign level" — the matrix satisfies this structurally. However, per-site CONVICTION TYPE reminders restate abstract labels: "Factual — assert what is true" / "Optionality — evaluate trade-offs" / "Emotional — convert factual and optionality conviction." The per-site form severs the inertia grounding at execution proximity — the model executing Artifact 1 reads "assert what is true" rather than "name the problem the inertia baseline creates." The criterion tests whether the conviction arc is *grounded in the competitive baseline* — the matrix declares it but the per-site reminder, which is the proximal instruction at execution time, loses it. PARTIAL: inertia grounding present at campaign level but not at per-artifact execution sites |
| C-24 | Scout-to-must-have traceability | PASS | REQUIREMENTS instruction: "Each Must-have traces to a specific friction the inertia baseline creates." This is a general instruction form (same pattern as R5 V-05). C-24 requires "each spec Must-have explicitly cites its originating scout-requirements friction" — the instruction mandates this citation. FULL: instruction present and explicit |

**Aspirational: 11 PASS + 1 PARTIAL**
- 11 × 5 = 55
- 1 × 2.5 = 2.5
- **Aspirational total: 57.5/60**

### Excellence

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-11 | Hard GATE per transition | PASS | "GATE: Do not begin Artifact 2 until [spec file] is written to disk." "GATE: Do not begin Artifact 3 until [proposal file] is written to disk." "GATE: Do not begin Campaign Reflection until [pitch file] is written to disk." All three transitions gated |
| C-12 | Proactive scout inventory | PASS | "Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace. Unconditional. Do not gate on signal presence." |
| C-13 | Conviction audit in pitch | PASS | CONVICTION DELTA sub-field asks per version: "what emotional conviction about the inertia cost does this establish that the factual and optionality artifacts could not make visceral?" — covers conviction delta. NEAR-DUPLICATE CONTENT: "Name any passage you nearly copied from the spec or proposal. State what you changed to make it conviction-bearing rather than informational." — covers near-duplicate audit |
| C-14 | Signal consumption log | PASS | CAMPAIGN CLOSE table has per-artifact "Scout signal consumed" column |

**Excellence: 4/4 PASS → 8/8**

### V-01 Total

| Tier | Score |
|------|-------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational | 57.5 |
| Excellence | 8 |
| **Total** | **155.5** |

---

## V-02 — C-24 Mechanism: Scout Traceability Table

**Key structural feature:** SCOUT TRACEABILITY TABLE added to REQUIREMENTS section with per-must-have rows (Req-ID / Must-have / Originating Scout-Requirements Friction / Scout File). Retains all R5 V-05 mechanisms: inertia-grounded CONVICTION TYPE in matrix AND in per-site reminders, CAMPAIGN REFLECTION phase gate.

### Essential

All five essential criteria: PASS (same structure as V-01, confirmed: three artifacts, canonical paths, identity locked in SETUP, GATE ordering, full section structure). **60/60**

### Recommended

All three recommended criteria: PASS. Same PRESERVE instructions, CARRIES FORWARD chain, and CAMPAIGN CLOSE table. **30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09 | PASS | Conviction type differentiation retained; FINDINGS CONVICTION DELTA asks per-version inertia grounding question |
| C-10 | PASS | SCOUT TRACEABILITY TABLE makes scout-to-spec linkage explicitly labeled and bidirectionally auditable; scout namespaces in READ field; the table form *strengthens* C-10 quality |
| C-15 | PASS | Full contract matrix with all four fields + CONVICTION TYPE superset |
| C-16 | PASS | CAMPAIGN REFLECTION phase with named sub-fields; "not before pitch production begins, not during pitch production" |
| C-17 | PASS | Full contract matrix + named FINDINGS template |
| C-18 | PASS | Explicit double prohibition: "not before pitch production begins, not during pitch production" |
| C-19 | PASS | CAMPAIGN REFLECTION named phase with GATE before it; structural double-prohibition |
| C-20 | PASS | Per-site contract reminders at all three execution sites (READ + PRESERVE satisfied; C-22 superset) |
| C-21 | PASS | CONVICTION TYPE label at each artifact; FINDINGS typed to pitch's emotional conviction role |
| C-22 | PASS | Three-field per-site: READ + PRESERVE + CONVICTION TYPE at all three sites. Per-site CONVICTION TYPE includes inertia grounding (same as R5 V-05): "Factual — name the problem the inertia baseline creates," "Optionality — price the cost of inertia against each alternative," "Emotional — make the inertia cost visceral and per-audience-specific" |
| C-23 | PASS | Both matrix AND per-site reminders carry inertia-grounded CONVICTION TYPE labels. Matrix: "Factual — names the problem the inertia baseline creates" etc. Per-site Spec: "Factual — name the problem the inertia baseline creates; do not argue." Per-site Proposal: "Optionality — price the cost of inertia against each alternative; do not re-assert spec facts." Per-site Pitch: "Emotional — make the inertia cost visceral and per-audience-specific." Full inertia grounding at both campaign level (matrix) and execution-site level (per-site) |
| C-24 | PASS | SCOUT TRACEABILITY TABLE is a dedicated labeled structure with explicit per-must-have rows citing originating friction and scout file. This exceeds the general-instruction form: each must-have entry is individually traceable. Strongest C-24 implementation seen |

**Aspirational: 12/12 PASS → 60/60**

### Excellence

All four excellence criteria: PASS (hard GATE ×3, proactive scout inventory unconditional, CONVICTION DELTA + NEAR-DUPLICATE CONTENT, CAMPAIGN CLOSE signal log). **8/8**

### V-02 Total

| Tier | Score |
|------|-------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational | 60 |
| Excellence | 8 |
| **Total** | **158** |

---

## V-03 — Named INERTIA MODEL Entity: Campaign-Level Architecture

**Key structural feature:** INERTIA MODEL as named three-field entity (Name / Behavior / Cost) in SETUP. CONVICTION TYPE labels reference INERTIA MODEL fields by name in both matrix and per-site reminders. Explicit field mapping in SETUP (Factual → Cost field, Optionality → Cost against alternatives, Emotional → Cost visceral per audience).

### Essential

PASS ×5: three full artifacts, canonical paths, INERTIA MODEL declared in SETUP locks topic identity (CARRIES FORWARD "INERTIA MODEL (all fields)"), GATE ordering, full section structure. **60/60**

### Recommended

PASS ×3: PRESERVE at proposal site; CARRIES FORWARD propagates INERTIA MODEL; CAMPAIGN CLOSE table. **30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09 | PASS | INERTIA MODEL structural entity makes the campaign's "opponent" present at every decision point; CONVICTION DELTA per version asks about inertia cost viscerality; NEAR-DUPLICATE CONTENT audit present |
| C-10 | PASS | READ field lists scout namespaces; REQUIREMENTS "Each Must-have traces to a specific friction the INERTIA MODEL Cost creates"; scout pull is named and directional |
| C-15 | PASS | Full contract matrix: READ includes "INERTIA MODEL (all fields)" and "INERTIA MODEL Cost" appropriately per artifact; all four required fields present + CONVICTION TYPE superset |
| C-16 | PASS | CAMPAIGN REFLECTION phase with named FINDINGS sub-fields; phase gate enforces post-execution |
| C-17 | PASS | Full contract matrix + named FINDINGS template |
| C-18 | PASS | "not before pitch production begins, not during pitch production" |
| C-19 | PASS | CAMPAIGN REFLECTION named phase with hard GATE |
| C-20 | PASS | Three per-site reminders with READ + PRESERVE fields (C-22 superset) |
| C-21 | PASS | CONVICTION TYPE labeled per artifact; FINDINGS typed to conviction role |
| C-22 | PASS | Three-field per-site: READ includes "INERTIA MODEL (Name, Behavior, Cost)" / PRESERVE / CONVICTION TYPE referencing INERTIA MODEL fields. Spec: "CONVICTION TYPE: Factual — document the INERTIA MODEL Cost field as factual record; do not argue." Proposal: "Optionality — price the INERTIA MODEL Cost against each alternative; do not re-assert spec facts." Pitch: "Emotional — make the INERTIA MODEL Cost visceral per audience." All three fields at all three sites |
| C-23 | PASS | Named INERTIA MODEL entity is the strongest possible D7 implementation: campaign-level architectural choice explicitly named and declared before any artifact. CONVICTION TYPE labels reference INERTIA MODEL fields by name at both matrix and per-site levels. The field mapping in SETUP makes the grounding formally declared. Full inertia-anchored conviction arc |
| C-24 | PASS | REQUIREMENTS: "Each Must-have traces to a specific friction the INERTIA MODEL Cost creates." Same instruction form as R5 V-05 / V-02's general instruction. FULL (instruction explicit and present) |

**Aspirational: 12/12 PASS → 60/60**

### Excellence

PASS ×4: hard GATEs ×3, unconditional scout inventory, CONVICTION DELTA + NEAR-DUPLICATE CONTENT in FINDINGS, CAMPAIGN CLOSE signal log. **8/8**

### V-03 Total

| Tier | Score |
|------|-------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational | 60 |
| Excellence | 8 |
| **Total** | **158** |

---

## V-04 — Minimal Density: C-22 + C-23 + C-24 Compressed

**Key structural feature:** Skeleton form. Matrix CONVICTION TYPE entries: "Factual — names inertia problem" / "Optionality — prices inertia cost" / "Emotional — makes inertia cost visceral." Per-site reminders as compact labeled lines. C-24 as one-line tag instruction: "[friction: {specific inertia or scout-requirements finding}]" after each Must-have.

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | SETUP + three artifacts + CAMPAIGN REFLECTION + CAMPAIGN CLOSE |
| C-02 | PASS | Canonical paths in matrix and write instructions |
| C-03 | PASS | Topic identity in SETUP; matrix CARRIES FORWARD "Feature identity; inertia" |
| C-04 | PASS | GATE at each transition with hard "Do not begin" language |
| C-05 | PASS | Spec: "Sections: PURPOSE / REQUIREMENTS (MoSCoW) / DESIGN / CONSTRAINTS / OPEN QUESTIONS." Proposal: "Three options min. Option A: do-nothing — explicit inertia cost. Per option: Name / Description / Pros / Cons / Risk / Effort. Recommendation: chosen option + three reasons." Pitch: "EXEC / DEV / MAKER" with content requirements + "ANTI-POSITIONING." All minimum structural elements present even in compressed form |

**Essential: 60/60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | "PRESERVE: all spec design decisions — no re-opening." Explicit |
| C-07 | PASS | "PRESERVE: recommended option — crystallize, do not reopen." DEV: "references spec technical design explicitly." MAKER: "plain language only, no spec or proposal terminology." |
| C-08 | PASS | SETUP declares campaign; CAMPAIGN CLOSE table with artifact paths and scout signal columns |

**Recommended: 30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09 | PASS | CONVICTION TYPE differentiation at each artifact; CONVICTION DELTA in FINDINGS asks per-version inertia urgency; NEAR-DUPLICATE CONTENT present |
| C-10 | PASS | READ field cites scout namespaces; REQUIREMENTS "Anchor each Must-have to a specific friction the inertia baseline creates"; friction tag mechanism links scout findings |
| C-15 | PASS | Matrix has all four required fields (READ/WRITE/PRESERVE/CARRIES FORWARD) + CONVICTION TYPE superset. Note: compact label form ("inertia" not "inertia baseline") but the matrix is structurally complete |
| C-16 | PASS | "CAMPAIGN REFLECTION — begins only after the pitch file is on disk. Not before. Not during." FINDINGS with named sub-fields CONVICTION DELTA / NEAR-DUPLICATE CONTENT / RESIDUAL QUESTIONS |
| C-17 | PASS | Contract matrix (complete four fields) + named FINDINGS template with sub-fields |
| C-18 | PASS | "begins only after the pitch file is on disk. Not before. Not during." Both timing violations explicitly prohibited |
| C-19 | PASS | "CAMPAIGN REFLECTION" as section header; "GATE: Do not begin Campaign Reflection until this file is written to disk." Named phase + hard gate = structural double-prohibition |
| C-20 | PASS | Per-site: compact but labeled. Spec: "READ: ... PRESERVE: ... CONVICTION TYPE: ..." Proposal and Pitch same structure. All three fields present at three sites |
| C-21 | PASS | CONVICTION TYPE at each artifact; FINDINGS CONVICTION DELTA per-version inertia urgency audit |
| C-22 | PASS | Three-field per-site at all three artifacts: READ + PRESERVE + CONVICTION TYPE. Spec: "CONVICTION TYPE: Factual — names inertia problem." Proposal: "CONVICTION TYPE: Optionality — prices inertia cost." Pitch: "CONVICTION TYPE: Emotional — makes inertia cost visceral." Compact but all three fields present |
| C-23 | **PARTIAL** | Matrix CONVICTION TYPE compact labels: "Factual — names inertia problem" / "Optionality — prices inertia cost" / "Emotional — makes inertia cost visceral." These are inertia-grounded — they name the inertia connection — but at minimal elaboration. The criterion requires conviction types "grounded in the competitive baseline, naming what the status quo produces at each conviction stage." "Names inertia problem" names the connection; "prices inertia cost" prices it; "makes inertia cost visceral" makes it visceral. The labels satisfy the semantic requirement but at skeleton density — they reference inertia without elaborating what the inertia problem *is* (the status quo behavior). The D7 requirement is met (campaign-level declaration present). However, the per-site CONVICTION TYPE reminders carry the same compact form with no elaboration: the model executing Artifact 1 sees "CONVICTION TYPE: Factual — names inertia problem" which is a label pointing toward inertia grounding but not itself a grounded statement. PARTIAL: the inertia connection is named but not operationally defined at any level; the compact label is less clear than a full statement about what the inertia problem is |
| C-24 | **PARTIAL** | Instruction: "Each Must-have: tag the scout-requirements friction it addresses (format: '[friction: {specific inertia or scout-requirements finding}]' after each Must-have item)." This is a compact inline-tag approach vs. a dedicated table. The criterion requires "each spec Must-have explicitly cites its originating scout-requirements friction" — the inline tag instruction mandates this citation. However, the tag format ties the friction to "inertia or scout-requirements finding" which is broader than explicitly citing scout-requirements origin. The table form in V-02/V-05 makes the linkage auditable via a separate labeled structure; the inline tag in V-04 embeds it in the requirement bullet. This is functionally equivalent to an explicit citation — PARTIAL awarded because the format is compact and the scout-file origin citation is not explicit (no "Scout File" column or equivalent), making the linkage less auditable. PARTIAL |

**Aspirational: 10 PASS + 2 PARTIAL**
- 10 × 5 = 50
- 2 × 2.5 = 5
- **Aspirational total: 55/60**

### Excellence

| ID | Verdict | Evidence |
|----|---------|---------|
| C-11 | PASS | Hard GATE at all three transitions |
| C-12 | PASS | "Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional." |
| C-13 | PASS | CONVICTION DELTA per version asks inertia urgency; NEAR-DUPLICATE CONTENT requires naming near-copies |
| C-14 | PASS | CAMPAIGN CLOSE table with "Scout signal consumed" column |

**Excellence: 8/8**

### V-04 Total

| Tier | Score |
|------|-------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational | 55 |
| Excellence | 8 |
| **Total** | **153** |

---

## V-05 — Full Convergence: Named INERTIA MODEL + Traceability Table + Inertia-Anchored Per-Site

**Key structural feature:** Named INERTIA MODEL entity (V-03 form) + SCOUT TRACEABILITY TABLE (V-02 form) + per-site reminders referencing INERTIA MODEL fields by name (same as V-03). Maximum structural explicitness.

### Essential

PASS ×5. Full structure: SETUP with INERTIA MODEL declaration, three full artifacts, CAMPAIGN REFLECTION, CAMPAIGN CLOSE. All paths canonical. Identity locked in INERTIA MODEL. GATE ordering. Full section structure per artifact. **60/60**

### Recommended

PASS ×3. PRESERVE at proposal and pitch sites explicit. CARRIES FORWARD propagates INERTIA MODEL. CAMPAIGN CLOSE table. **30/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09 | PASS | INERTIA MODEL present at every execution site as named entity; conviction types differentiated and grounded; FINDINGS CONVICTION DELTA per-version; NEAR-DUPLICATE CONTENT. Maximum structural opponent presence reduces repetition risk |
| C-10 | PASS | SCOUT TRACEABILITY TABLE makes scout-to-spec linkage bidirectionally auditable (labeled table); READ field cites scout namespaces per artifact; table's "Scout File" column traces to specific evidence files |
| C-15 | PASS | Full contract matrix: READ explicitly names "INERTIA MODEL (all fields)" and "INERTIA MODEL Cost" appropriate to each artifact; all four required fields + CONVICTION TYPE superset |
| C-16 | PASS | CAMPAIGN REFLECTION named phase with labeled FINDINGS sub-fields; hard GATE; "not before... not during" placement |
| C-17 | PASS | Full contract matrix + named FINDINGS template with sub-fields |
| C-18 | PASS | "not before pitch production begins, not during pitch production" |
| C-19 | PASS | CAMPAIGN REFLECTION as named phase + GATE structural enforcement |
| C-20 | PASS | Three-field per-site READ + PRESERVE at all three sites (C-22 superset) |
| C-21 | PASS | CONVICTION TYPE labeled per artifact; FINDINGS typed to pitch's conviction role |
| C-22 | PASS | Three-field per-site with INERTIA MODEL field references: Spec: "CONVICTION TYPE: Factual — document the INERTIA MODEL Cost field as factual record; do not argue." Proposal: "Optionality — price the INERTIA MODEL Cost against each alternative; do not re-assert spec facts." Pitch: "Emotional — make the INERTIA MODEL Cost visceral per audience." All three fields, all three sites, INERTIA MODEL field-referenced |
| C-23 | PASS | Named INERTIA MODEL entity (Name/Behavior/Cost) declared in SETUP; explicit field mapping (Factual → Cost as record, Optionality → Cost against alternatives, Emotional → Cost visceral per audience); matrix CONVICTION TYPE references INERTIA MODEL fields; per-site reminders reference INERTIA MODEL fields. Maximum inertia-anchored conviction arc: every level of the instruction references the same named model fields |
| C-24 | PASS | SCOUT TRACEABILITY TABLE in REQUIREMENTS with per-must-have rows: Req-ID / Must-have / Originating Scout-Requirements Friction / Scout File. Table structure is labeled, one row per Must-have, friction column is explicit. Strongest C-24 implementation: both the instruction ("Each Must-have traces to a specific friction the INERTIA MODEL Cost creates") AND the dedicated table |

**Aspirational: 12/12 PASS → 60/60**

### Excellence

PASS ×4: hard GATEs ×3, unconditional scout inventory, CONVICTION DELTA + NEAR-DUPLICATE CONTENT, CAMPAIGN CLOSE signal log. **8/8**

### V-05 Total

| Tier | Score |
|------|-------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational | 60 |
| Excellence | 8 |
| **Total** | **158** |

---

## Scorecard Summary

| Variant | Essential | Recommended | Aspirational | Excellence | **Total** | All-Essential? |
|---------|-----------|-------------|--------------|------------|-----------|----------------|
| V-01 | 60 | 30 | 57.5 | 8 | **155.5** | YES |
| V-02 | 60 | 30 | 60 | 8 | **158** | YES |
| V-03 | 60 | 30 | 60 | 8 | **158** | YES |
| V-04 | 60 | 30 | 55 | 8 | **153** | YES |
| V-05 | 60 | 30 | 60 | 8 | **158** | YES |

**Rank:** V-02 = V-03 = V-05 at 158 > V-01 at 155.5 > V-04 at 153

---

## R6 Diagnostic Answers

**Q1: Does C-23 require inertia-grounded phrasing in per-site reminders, or is the matrix alone sufficient?**
**V-01 scores 155.5 (C-23 PARTIAL)** — the matrix-only inertia grounding is not sufficient. Per-site CONVICTION TYPE reminders that revert to abstract labels sever the inertia grounding at execution proximity. The model running Artifact 1 reads "Factual — assert what is true" rather than "Factual — name the problem the inertia baseline creates." D7's "campaign-level architectural choice" means the inertia model must be declared at campaign scope — it does not mean the matrix is the only location that must carry the grounding. Full C-23 requires inertia-grounded language at both the campaign-level matrix and per-site execution sites.

**Q2: Does a SCOUT TRACEABILITY TABLE earn C-24 more robustly than a general instruction?**
**V-02 confirms FULL C-24** — the table form earns full credit. C-10 quality is also improved: the table makes scout signal consumption bidirectionally auditable at the must-have level, stronger than R5 V-05's general instruction. The table is the stronger C-24 implementation.

**Q3: Does a named INERTIA MODEL entity sharpen C-23 scoring?**
**V-03 earns C-23 FULL** — the named entity form is the strongest C-23 implementation. Conviction labels referencing model fields by name makes the inertia grounding formally auditable: a scorer can verify each CONVICTION TYPE label against the declared INERTIA MODEL fields. C-23 scoring is not changed relative to R5 V-05's inline sentence form (both earn FULL), but V-03's named entity is more precisely satisfying.

**Q4: Can all three new v6 criteria hold at minimal density?**
**V-04 scores 153** — minimum density is insufficient for C-23 (compact label "names inertia problem" earns PARTIAL) and C-24 (inline tag format without explicit scout file citation earns PARTIAL). The ceiling is NOT density-independent: minimum-density inertia labels and compact traceability instructions fall to PARTIAL. There is a minimum elaboration threshold.

**Q5: Does maximum structural explicitness maintain 158 without degrading C-09?**
**V-05 scores 158** — full ceiling maintained. Maximum structural explicitness does not degrade C-09; the named INERTIA MODEL entity present at every execution site functions as a structural anchor that reduces repetition risk and strengthens narrative coherence. No instruction friction penalty.

---

## Excellence Signals from Top Variants (V-02, V-03, V-05)

**V-02 — SCOUT TRACEABILITY TABLE form for C-24:**
The table (Req-ID / Must-have / Originating Friction / Scout File) is the most auditable C-24 implementation. It makes the reverse linkage checkable row-by-row — a scorer, reviewer, or the executing model can verify each must-have against its originating evidence. General instructions require the model to remember to cite; the table requires it to fill in a column.

**V-03 — Named INERTIA MODEL entity as campaign-level architectural choice:**
Elevating the inertia baseline from a sentence to a named, three-field structural entity (Name / Behavior / Cost) with explicit field-to-conviction-type mapping creates a referenceable "opponent model." Every subsequent instruction references the model by field name, making the inertia grounding formally verifiable. This is the strongest C-23 form and the cleanest D7 satisfaction.

**V-05 — Full convergence without interference:**
Combining all three mechanisms simultaneously — named INERTIA MODEL + SCOUT TRACEABILITY TABLE + field-referenced per-site reminders — produces no criterion degradation. Maximum explicitness at all levels is safe. The key insight is that the three mechanisms are architecturally separable (SETUP entity ↔ REQUIREMENTS table ↔ per-site reminders) and do not compete for the same instruction space.

---

```json
{"top_score": 158, "all_essential_pass": true, "new_patterns": ["Per-site CONVICTION TYPE reminders must carry inertia-grounded phrasing to earn C-23 FULL — matrix-only inertia grounding at campaign level is insufficient; abstract labels at per-site execution sites earn PARTIAL", "SCOUT TRACEABILITY TABLE (labeled matrix with Req-ID / Must-have / Originating Friction / Scout File columns) is the strongest C-24 form — general instruction alone earns FULL but table form is more robustly auditable and improves C-10", "Minimum-density inertia labels ('Factual — names inertia problem') fall to PARTIAL on C-23 — elaboration threshold exists; compact friction-tag instruction without scout file citation falls to PARTIAL on C-24", "Named INERTIA MODEL entity (Name / Behavior / Cost) with explicit field-to-conviction-type mapping is the strongest C-23 form; field-referenced CONVICTION TYPE labels at per-site reminders make inertia grounding formally auditable at every execution site"]}
```
