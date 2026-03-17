# Scoring Report — program-plan Round 2 (Rubric v2, 115 pts)

## Rubric quick-reference

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential | C-01 YAML, C-02 Echo, C-03 Skills, C-04 Gates | 15 | 60 |
| Recommended | C-05 Order, C-06 Names, C-07 Plan-identity | 10 | 30 |
| Aspirational | C-08 Quantified, C-09 Arc, C-10 Contrast, C-11 Structural, C-12 Dual-anchor | 5 | 25 |

PASS = full, PARTIAL = half (2.5 or 7.5 depending on tier), FAIL = 0.
Golden: all 4 essential PASS **and** composite ≥ 80.

---

## V-01 — Role Sequence

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| **C-01 Valid YAML** | PASS | Template has well-formed `program:/topic:/strategy:/stages:` structure. |
| **C-02 Echo contract** | PASS | Step 4 + template pre-positions echo with `# REQUIRED: must be last`, `# REQUIRED: empty`, `# REQUIRED: must be present`. |
| **C-03 Valid skills** | PASS | Step 1 role-catalog table lists all 9 namespaces; template: `# from Step 1 role catalog above — no invented names`. |
| **C-04 Evidence gates** | PASS | Step 3 BAD/GOOD/BETTER table + template gate comment `# name artifacts, NOT "done"/"complete"`. |
| **C-05 Dep. order** | PASS | Step 2 states `scout → draft → review/prove → flow/trace → listen/topic → echo` with explicit dep. rules. |
| **C-06 Stage names** | PASS | PASS/FAIL name examples given; template comment `# descriptive role-intent label, not namespace name`. |
| **C-07 Plan-not-exec** | PASS | Opening declaration `— a plan, not an executor.` + template comment `# This program is a plan, not an executor`. |
| **C-08 Quantified gate** | PASS | Step 3 requires `">=2 scout signals"`, `"0 P0 findings open"` etc.; BETTER example is quantified. |
| **C-09 Evidence arc** | PARTIAL | Arc chain stated in Step 2 and template comment; single stage shown in template with no layer headers — arc is declared, not visualized in scaffold structure. |
| **C-10 Contrast pair** | PASS | Step 3 BAD/GOOD/BETTER table with concrete `"all scout skills complete"` vs `"scout-feasibility and scout-requirements artifacts present"` — anchored to C-04. |
| **C-11 Structural** | PASS | Echo pre-positioned in template with 3 × `# REQUIRED` annotations; C-02 is structural. Gate inline `NOT "done"/"complete"` partially enforces C-04. |
| **C-12 Dual-anchor** | PARTIAL | C-02 (Step 4 prose + template), C-03 (catalog table + inline), C-04 (Step 3 table + inline) all have dual anchors — 3 of 4. C-01 has template only; no second worked YAML example. |

**Essential:** 4/4 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 5+2.5+5+5+2.5 = 20 pts
**Composite: 110 / 115** | Golden: YES (all essential PASS, composite ≥ 80)

---

## V-02 — Annotated Skeleton

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| **C-01 Valid YAML** | PASS | Full YAML skeleton with all required keys; no structural gaps. |
| **C-02 Echo contract** | PASS | Echo pre-positioned at final `# ---- FINAL STAGE ----` with 4 × `# REQUIRED` annotations including `# REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.` |
| **C-03 Valid skills** | PASS | Skill catalog table (anchor 1) + inline `# valid scout options listed in catalog table above` at every skill slot (anchor 2). |
| **C-04 Evidence gates** | PASS | `# BAD: / # GOOD: / # BEST:` inline at every gate slot; rules checklist item 2: `"Done" fails`. |
| **C-05 Dep. order** | PASS | `# DEPENDENCY:` comments at Stage 2 and Stage 3; Stage 4+ comment gives full chain. |
| **C-06 Stage names** | PASS | Template `# REQUIRED: descriptive intent label, not "stage1" or "scout"`; checklist item 5. |
| **C-07 Plan-not-exec** | PASS | Opening paragraph + `# REQUIRED: preserve — this program is a plan, not an executor` in template header. |
| **C-08 Quantified gate** | PASS | Stage 2 hint `">=2 scout signals reviewed"`; Stage 3 GOOD `"0 P0 findings open"`; checklist item 3. |
| **C-09 Evidence arc** | PARTIAL | Stages labeled Stage 1/2/3/4+ with dependency comments — ordering enforced but no layer headers; arc present in structure but not named in template scaffold. |
| **C-10 Contrast pair** | PASS | `# BAD:` / `# GOOD:` inline at every gate position throughout the skeleton — pervasive, anchored to C-04 (essential). |
| **C-11 Structural** | PASS | Echo pre-positioned with multi-`# REQUIRED` annotations (C-02 structural). Inline `# BAD:` / `# GOOD:` at every gate slot makes C-04 failure visible at the exact point of authoring (C-04 structural). Strongest C-11 implementation in the round. |
| **C-12 Dual-anchor** | PARTIAL | C-02 (rules checklist + template), C-03 (catalog table + per-slot inline), C-04 (per-slot inline + checklist) — 3 of 4. C-01 single anchor: template is the sole YAML structure reference; no separate worked example. |

**Essential:** 4/4 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 5+2.5+5+5+2.5 = 20 pts
**Composite: 110 / 115** | Golden: YES

---

## V-03 — Question Framing (Phrasing Register)

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| **C-01 Valid YAML** | PASS | Template shows `program:/topic:/strategy:/stages:` with correct echo at end. |
| **C-02 Echo contract** | PASS | Echo pre-positioned in template; "Echo has no skills. Echo is always last. `auto: true` is required." |
| **C-03 Valid skills** | PASS | Question bank maps every question to a namespace-qualified skill; template: `# from question bank above — no invented names`. |
| **C-04 Evidence gates** | PASS | Core framing: gate = "what evidence tells us this question has been answered?"; BAD/GOOD table `"We ran scout:feasibility"` vs `"scout-feasibility artifact present"`; Step 4 gate-writing rules. |
| **C-05 Dep. order** | PASS | Step 3 instruction: "discovery before design, design before validation…" — the namespace chain as question ordering rule. |
| **C-06 Stage names** | PASS | Step 5 names per cluster: `feasibility`, `design-commit`, `expert-validation`, `domain-simulation`, `feedback-preview`. |
| **C-07 Plan-not-exec** | PASS | "A program plan is a plan, not an executor. It does not run skills." + template comment. |
| **C-08 Quantified gate** | PASS | Step 4: "Make at least one gate quantified: `">=2 scout signals present"`"; Step 4 FAIL example for qualitative-only. |
| **C-09 Evidence arc** | PASS | Question bank organized by arc layer (Discovery → Design → Validation → Simulation → Feedback); the entire prompt structure embeds the arc as its organizing principle. |
| **C-10 Contrast pair** | PASS | BAD/GOOD table: `"We ran scout:feasibility"` (execution) vs `"scout-feasibility artifact present; no blocking concerns"` (evidence) — anchored to C-04. |
| **C-11 Structural** | PARTIAL | Echo pre-positioned in template at end (partially structural for C-02), but no `# REQUIRED` annotations — a model filling the template without reading prose could still move or delete echo without encountering structural resistance. Framing-first approach means structural enforcement is weaker than template-annotation approaches. |
| **C-12 Dual-anchor** | PARTIAL | C-03 (question bank + template inline), C-04 (BAD/GOOD table + framing principle) — strong dual anchors. C-02 has echo pre-positioned + prose rules but no `# REQUIRED` (weak anchor 2). C-01 template only. 2 of 4 strong, 2 weak → PARTIAL. |

**Essential:** 4/4 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 5+5+5+2.5+2.5 = 20 pts
**Composite: 112.5 / 115** | Golden: YES

---

## V-04 — Bands + Roles (Combined)

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| **C-01 Valid YAML** | PASS | BAD example YAML, GOOD equivalent YAML (described separately), and template — three valid YAML representations. |
| **C-02 Echo contract** | PASS | `# Echo — REQUIRED: must be last, no stage after this` + template: `# REQUIRED: empty`, `# REQUIRED: must be present and true`. Separate prose: "Echo must be last. `skills: []` and `auto: true` are hard requirements." |
| **C-03 Valid skills** | PASS | Per-band skill catalogs list every valid skill under each band (anchor 1); template: `# valid Band N skills listed above` at every skill slot (anchor 2). "Any skill name not in a band above is invalid." |
| **C-04 Evidence gates** | PASS | BAD plan: `gate: "all done"` + "names no evidence" (anchor 1); gate handoff-memo framing + 3 PASS examples (anchor 2); instruction 3: "Band 1 done → FAIL". |
| **C-05 Dep. order** | PASS | Four lifecycle bands (Prove It → Design It → Simulate It → Listen Ahead) embed namespace order as structural bands; template has band-separator comments. |
| **C-06 Stage names** | PASS | Per-band name examples: `market-research`, `design-commit`, `domain-simulation`, `feedback-preview`, etc. |
| **C-07 Plan-not-exec** | PASS | "This is a plan, not an executor: the program declares what evidence must exist…" + template `# This program is a plan, not an executor`. |
| **C-08 Quantified gate** | PASS | Gate examples: `">=3 flow simulations complete; trace:contract documented"` is the clearest R2 quantified gate. Instruction 3: "Make at least one gate quantified." |
| **C-09 Evidence arc** | PASS | Four named bands are the organizing principle of the prompt. Band names (Prove It / Design It / Simulate It / Listen Ahead) make the breadth→depth→synthesis arc structurally explicit. Template band-separator comments persist in output. |
| **C-10 Contrast pair** | PASS | Labeled `# BAD: flat plan` YAML block with `gate: "all done"` followed by "Nobody knows when it is safe to advance because `"all done"` names no evidence" — anchored to C-04 (essential). Full YAML structure visible. |
| **C-11 Structural** | PASS | Four lifecycle bands structurally enforce C-05 namespace ordering (C-05 recommended, but also enforces dependency implicitly). Echo pre-positioned with `# REQUIRED: empty`, `# REQUIRED: must be present and true` (C-02 essential, structural). Per-band skill lists make valid skills the visible options at authoring time (C-03 structural). |
| **C-12 Dual-anchor** | PASS | **C-01**: BAD YAML block (anchor 1) + template structure (anchor 2). **C-02**: Prose "hard requirements" statement (anchor 1) + template `# REQUIRED` echo (anchor 2). **C-03**: Per-band catalogs (anchor 1) + per-slot template inline (anchor 2). **C-04**: BAD flat plan contrast (anchor 1) + handoff-memo framing (anchor 2). All 4 of 4 essential criteria have dual anchors. |

**Essential:** 4/4 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 5+5+5+5+5 = 25 pts
**Composite: 115 / 115** | Golden: YES

---

## V-05 — BAD/GOOD YAML + Annotated Template + Checklist (Golden Synthesis)

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| **C-01 Valid YAML** | PASS | BAD YAML (anchor 1) + GOOD YAML full example (anchor 2) + template (anchor 3) — triple YAML representations. |
| **C-02 Echo contract** | PASS | Template: `# --- Final Stage: REQUIRED, must be last ---` header + 4 × `# REQUIRED` annotations + `# REQUIRED: DO NOT add skills here. DO NOT move this stage`. Checklist item 4 verifies echo. |
| **C-03 Valid skills** | PASS | Skill namespace catalog (anchor 1) + GOOD example using real skills + per-layer template comments (anchor 2). Checklist item 5 verifies. |
| **C-04 Evidence gates** | PASS | Full BAD (`gate: "all done"`) vs GOOD YAML pair (anchor 1) + per-gate template annotations `# name artifacts; NOT "done" / "complete" / "proceed"` + `# BAD:` / `# GOOD:` (anchor 2). Checklist items 1–2 verify. |
| **C-05 Dep. order** | PASS | `scout → draft → review/prove → flow/trace → listen → topic` stated; dependency rules explicit; layer dividers `# --- Layer 1/2/3 ---` in template reinforce ordering. |
| **C-06 Stage names** | PASS | GOOD example names: `discovery`, `design-commit`, `expert-review`, `simulation`, `feedback-preview`. Template placeholder: `# descriptive label, not "stage1" or "scout"`. Checklist item 6. |
| **C-07 Plan-not-exec** | PASS | Opening three-sentence identity paragraph distinguishing plan from task list. Template `# REQUIRED: this program is a plan, not an executor`. Uniquely: "a task list tells you what to do; a program plan tells you what evidence must exist." |
| **C-08 Quantified gate** | PASS | Template layer 2: `# REQUIRED: at least ONE gate in the plan must be quantified`; checklist item 3; GOOD example `">=0 P0 findings open"` is weak but instruction overrides. |
| **C-09 Evidence arc** | PASS | Layer dividers `# --- Layer 1: Breadth ---`, `# --- Layer 2: Depth ---`, `# --- Layer 3+: Synthesis ---` label the arc explicitly in the template; GOOD example demonstrates all three layers with commentary. Arc vocabulary (breadth/depth/synthesis) introduced at opening. |
| **C-10 Contrast pair** | PASS | Full labeled `# BAD: ad hoc run` YAML block vs `# GOOD: three-layer evidence arc` YAML block — most vivid contrast in the round; shows skill ordering failures, dependency violations, and execution-state gate in a single BAD example. Anchored to C-04 (essential). |
| **C-11 Structural** | PASS | Echo pre-positioned with `# REQUIRED` header + 4 × `# REQUIRED` annotations (C-02). Gate slots annotated with `# BAD:` / `# GOOD:` markers (C-04). Layer dividers enforce arc (C-05). Checklist as required output section forces model to verify C-02, C-04, C-03, C-06 structurally — verification checklist is the strongest C-11 mechanism in the round. |
| **C-12 Dual-anchor** | PASS | **C-01**: BAD YAML (anchor 1) + GOOD YAML (anchor 2). **C-02**: Template `# REQUIRED` (anchor 1) + checklist item 4 (anchor 2). **C-03**: Skill catalog (anchor 1) + checklist item 5 (anchor 2). **C-04**: BAD/GOOD YAML pair (anchor 1) + checklist items 1–2 (anchor 2). All 4 of 4 essential criteria dual-anchored; the verification checklist uniquely provides a universal second-anchor for every criterion simultaneously. |

**Essential:** 4/4 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 5+5+5+5+5 = 25 pts
**Composite: 115 / 115** | Golden: YES

---

## Composite Scorecard

| Variation | Essential | Recommended | Aspirational | **Total** | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 Role Sequence | 60 | 30 | 20.0 | **110.0** | YES |
| V-02 Annotated Skeleton | 60 | 30 | 20.0 | **110.0** | YES |
| V-03 Question Framing | 60 | 30 | 20.0 | **112.5** | YES |
| V-04 Bands + Roles | 60 | 30 | **25.0** | **115.0** | YES |
| V-05 BAD/GOOD + Checklist | 60 | 30 | **25.0** | **115.0** | YES |

**Ranking:** V-04 = V-05 (115) > V-03 (112.5) > V-01 = V-02 (110)

Every variation passes the golden threshold. R2 fully solved C-10/C-11/C-12 for the top two.

---

## Excellence Signals

### Why V-04 and V-05 reached 115 while V-01/V-02 reached 110

**C-12 (Dual-anchor) is the deciding gap.** V-01 and V-02 have no second anchor for C-01 — the YAML template is their only YAML structure reference. V-04/V-05 include a full worked YAML example (BAD plan in V-04, BAD+GOOD pair in V-05), which serves as a second independent mechanism for C-01.

**Key insight**: *A BAD plan example is never just a C-10 mechanism — it doubles as a C-01 second anchor by showing parseable YAML structure, and as a C-04 second anchor by showing the wrong output shape concretely.*

### Why V-05 is the stronger golden candidate (same score, better reliability)

V-05's verification checklist-as-output-section is a pattern V-04 lacks:
- It is a **universal second anchor** — one mechanism provides dual-anchoring for all 6 criteria simultaneously
- It **converts C-11 into self-verification** — the model must check its own output against the structural requirements before submitting
- It is **portable**: any future variation can add the checklist section without redesigning the prompt

### Why V-03 outperforms V-01/V-02 despite weaker C-11

Question framing achieves C-09 (evidence arc) as a natural byproduct of content organization — the question bank IS the arc. V-01/V-02 describe the arc in ordering rules but don't embed it as the prompt's organizing principle.

**Key insight**: *Framing stages as investigation questions makes C-04 compliance almost automatic — when the gate answers "what evidence proves the question is answered?", artifact-naming is the natural output format without requiring explicit rule recitation.*

### New R2 patterns not present in R1

1. **Worked YAML contrast completes C-12 for C-01**: Without a BAD or GOOD worked YAML example, the template is the sole C-01 anchor. The BAD plan example in V-04/V-05 closes this gap.

2. **Verification checklist as required output section**: Makes the model's self-verification part of the output contract. This is the lowest-cost path to full C-12 coverage — a single checklist section provides second anchors for all 4 essential criteria simultaneously.

3. **Layer vocabulary (breadth / depth / synthesis) is more generalizable than role vocabulary (PM / Architect / Dev)**: V-05's layer framing achieves C-09 equivalently to V-04's band framing while working for solo users and non-team contexts.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["Worked YAML contrast (BAD plan example) doubles as second anchor for C-01, completing C-12 full pass — without a separate YAML example the template is the sole C-01 anchor and C-12 stays PARTIAL", "Verification checklist as required output section provides a universal second anchor for all 4 essential criteria simultaneously at lower scaffolding cost than per-criterion inline annotations", "Question-framing approach achieves C-09 evidence arc as natural byproduct of content organization — the question bank is the arc — but trades structural enforcement (C-11 PARTIAL) for framing clarity"]}
```
