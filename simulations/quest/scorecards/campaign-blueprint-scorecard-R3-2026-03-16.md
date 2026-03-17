# campaign-blueprint — Quest Score R3

**Rubric version:** v3 | **Date:** 2026-03-16
**Scoring formula:** Essential (5×12=60) + Recommended (30) + Aspirational (20) + Excellence bonus (8) = 118 ceiling

---

## Criterion Reference

| Tier | ID | Criterion | Weight |
|------|----|-----------|--------|
| Essential | C-01 | All three artifacts produced | 12 |
| Essential | C-02 | Canonical paths | 12 |
| Essential | C-03 | Topic identity consistency | 12 |
| Essential | C-04 | Execution order | 12 |
| Essential | C-05 | Minimum structure per sub-artifact | 12 |
| Recommended | C-06 | Proposal respects spec | 10 |
| Recommended | C-07 | Pitch crystallizes recommended option | 10 |
| Recommended | C-08 | Campaign framing | 10 |
| Aspirational | C-09 | Narrative arc | 5 |
| Aspirational | C-10 | Scout signal pull | 5 |
| Aspirational | C-15 | Artifact contract — all four fields pre-execution | 5 |
| Aspirational | C-16 | Post-execution FINDINGS block | 5 |
| Excellence | C-11 | Hard GATE per transition | 2 |
| Excellence | C-12 | Proactive scout inventory | 2 |
| Excellence | C-13 | Conviction audit in pitch | 2 |
| Excellence | C-14 | Signal consumption log | 2 |

---

## V-01 — Contract Matrix Axis

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Spec / Proposal / Pitch sections all present and executed |
| C-02 | PASS | All three canonical paths in contract matrix WRITE row and body |
| C-03 | PASS | Topic identity + inertia baseline established in CAMPAIGN SETUP step 1–2 before any artifact |
| C-04 | PASS | Hard GATE at Spec close; hard GATE at Proposal close |
| C-05 | PASS | Spec: 5 required sections; Proposal: 3+ options + do-nothing + per-option fields + recommendation; Pitch: 3 versions with Hook/What/Why/CTA + ANTI-POSITIONING |

Essential: **60/60** — all pass

### Recommended

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Contract matrix PRESERVE = "All spec design decisions and constraints"; body reinforces: "PRESERVES: do not re-open any design question the spec resolved" — both levels explicit |
| C-07 | PASS | Matrix CF for Proposal = "Recommended option name and rationale; do-nothing cost stated"; Pitch body: "CARRIES FORWARD: the recommended option from the proposal is the subject of all three versions"; DEV explicitly references spec design; MAKER: "plain language only. No spec terminology. No proposal jargon." All three sub-conditions met |
| C-08 | PASS | Setup names topic; close table: per-artifact path + scout signal consumed + open questions |

Recommended: **30/30**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | FINDINGS block instructs: "State what conviction each version establishes that the spec and proposal did not" + "Note any content you nearly duplicated — name it explicitly." Both conviction-separation mechanisms present |
| C-10 | PASS | Contract matrix READ row maps: scout-requirements → Spec, scout-feasibility → Proposal, scout-positioning → Pitch; unconditional inventory in setup step 3 |
| C-15 | PASS | Pre-execution matrix declares all four fields (READ/WRITE/PRESERVE/CARRIES FORWARD) for all three artifacts before Artifact 1 begins. WRITE row contains all three canonical paths. All fields present; matrix printed before execution clears |
| C-16 | PASS | "FINDINGS (write this block after the pitch file is written, not before)" — label present; explicit post-execution instruction; both conviction questions present: (1) "State what conviction each version establishes…" (2) "Note any content you nearly duplicated…" |

Aspirational: **20/20**

### Excellence

| ID | Result | Evidence |
|----|--------|----------|
| C-11 | PASS | "GATE: Do not begin Artifact 2 until simulations/draft/specs/…is written to disk." "GATE: Do not begin Artifact 3 until simulations/draft/proposals/…is written to disk." Both transitions gated |
| C-12 | PASS | "Scout inventory — glob simulations/scout/ for this topic now. List every file found, organized by namespace. This is not conditional on signal existence." Unconditional, setup phase, pre-Artifact 1 |
| C-13 | PASS | FINDINGS has both required checks: (1) per-version conviction delta; (2) near-duplicate naming. C-16 passes (post-execution block), so C-13 earns full credit |
| C-14 | PASS | Close table: columns for Artifact \| Path \| Scout signal consumed \| Open questions — per-artifact signal namespace logged |

Excellence: **+8**

**V-01 Composite: 60 + 30 + 20 + 8 = 118 — GOLDEN**

---

## V-02 — FINDINGS Template Axis

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All three artifact sections present |
| C-02 | PASS | Canonical paths in WRITE contract fields for all three artifacts |
| C-03 | PASS | CAMPAIGN SETUP establishes topic identity + inertia baseline before Artifact 1 |
| C-04 | PASS | Hard GATE at Spec close; hard GATE at Proposal close |
| C-05 | PASS | Spec: 5 sections; Proposal: 3+ options + do-nothing + recommendation; Pitch: 3 versions + ANTI-POSITIONING |

Essential: **60/60** — all pass

### Recommended

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Proposal inline: "PRESERVE: All spec design decisions and constraints — do not re-open anything the spec resolved." Labeled field, explicit instruction |
| C-07 | PASS | Pitch PRESERVE: "Recommended option from proposal — pitch crystallizes this choice, does not reopen it." DEV: "references technical design from spec explicitly." MAKER: "plain language only — no spec or proposal terminology." All three sub-conditions met |
| C-08 | PASS | CAMPAIGN SETUP opens with topic framing; close table with per-artifact paths and scout signals |

Recommended: **30/30**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | CONVICTION DELTA sub-field requires per-version conviction statement; NEAR-DUPLICATE CONTENT sub-field forces acknowledgment of duplication risk. Two-field template structurally enforces narrative separation |
| C-10 | PASS | Per-artifact READ fields map scout signals to consuming artifacts; unconditional inventory in CAMPAIGN SETUP |
| C-15 | PASS | Per-artifact inline headers: READ/WRITE/PRESERVE/CARRIES FORWARD declared before execution for Spec and Proposal. Pitch: CARRIES FORWARD = "(final artifact)" — field is present with null-value declaration appropriate to terminal artifact. All four fields present for all three artifacts |
| C-16 | PASS | "FINDINGS (write after the pitch file is complete):" — labeled; explicit post-execution timing. Template: CONVICTION DELTA per version (forces pitch to exist before writing); NEAR-DUPLICATE CONTENT; RESIDUAL QUESTIONS. Named sub-fields structurally enforce post-execution placement |

Aspirational: **20/20**

### Excellence

| ID | Result | Evidence |
|----|--------|----------|
| C-11 | PASS | Both GATEs present with explicit blocking language |
| C-12 | PASS | "Run this now — not conditionally." Unconditional, pre-Artifact 1 |
| C-13 | PASS | CONVICTION DELTA = check 1 (per-version conviction); NEAR-DUPLICATE CONTENT = check 2 (duplication audit). C-16 passes (post-execution block), so C-13 earns full credit |
| C-14 | PASS | Close table: per-artifact scout signal consumed column |

Excellence: **+8**

**V-02 Composite: 60 + 30 + 20 + 8 = 118 — GOLDEN**

---

## V-03 — Carries-Forward Cascade Axis

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All three artifact sections present |
| C-02 | PASS | Artifact paths declared in CAMPAIGN SETUP section; body write instructions use canonical form |
| C-03 | PASS | Topic identity + inertia baseline in CAMPAIGN SETUP steps 1–2 |
| C-04 | PASS | GATE at Spec close after CF declaration; GATE at Proposal close after CF declaration |
| C-05 | PASS | Spec: 5 sections; Proposal: 3+ options + do-nothing + recommendation; Pitch: 3 versions + ANTI-POSITIONING |

Essential: **60/60** — all pass

### Recommended

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | "PRESERVE: All spec design decisions and constraints — do not re-open anything the spec resolved; do not introduce new design work." Labeled field, explicit double prohibition |
| C-07 | PASS | Pitch reads "CARRIES FORWARD from Proposal" which contains "Recommended option: [name it]"; PRESERVE: "Recommended option — pitch crystallizes this choice and does not reopen it"; DEV: "references the technical design from the spec explicitly"; MAKER: "plain language only — no spec terminology, no proposal jargon." All three sub-conditions met |
| C-08 | PASS | Setup names topic; close table with per-artifact paths and scout signals |

Recommended: **30/30**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | FINDINGS block: "State what conviction each version establishes that the spec and proposal did not. Note any content you nearly duplicated — name it explicitly." Conviction-separation mechanism present |
| C-10 | PASS | Per-artifact READ fields declare scout signal pulls; unconditional inventory in setup step 3 |
| C-15 | **PARTIAL** | READ and PRESERVE declared pre-execution as labeled fields. CARRIES FORWARD declared post-execution at artifact close (cascade design). **WRITE is not a labeled contract field** — path appears only in body write instructions. Two field types out of four are incomplete relative to the pre-execution requirement: WRITE absent from contract; CF post-execution rather than pre-execution. Partial credit: one complete field type present as labeled pre-execution contract (READ, PRESERVE) but two missing from the pre-execution declaration (WRITE, CF). **2.5 pts** |
| C-16 | PASS | "FINDINGS (write this block after the pitch file is written, not before):" — label present; explicit post-execution placement instruction; both conviction questions present: (1) per-version conviction delta; (2) near-duplicate naming. Open-prompt format with labeled block and both questions earns full credit |

Aspirational: **5 + 5 + 2.5 + 5 = 17.5/20**

### Excellence

| ID | Result | Evidence |
|----|--------|----------|
| C-11 | PASS | Both GATEs present; each fires after the CF cascade declaration, preserving GATE integrity |
| C-12 | PASS | "Unconditional — run regardless of whether signals exist." Setup step 3, pre-Artifact 1 |
| C-13 | PASS | FINDINGS: per-version conviction delta (check 1) + near-duplicate naming (check 2). C-16 passes; C-13 earns full credit |
| C-14 | PASS | Close table: per-artifact scout signal consumed. Additionally, Proposal CF includes "Scout signal consumed: [namespace or none]" as an intermediate log |

Excellence: **+8**

**V-03 Composite: 60 + 30 + 17.5 + 8 = 115.5 — GOLDEN**

---

## V-04 — Contract Matrix + FINDINGS Template (V-01 + V-02)

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All three artifact sections present |
| C-02 | PASS | All three paths in contract matrix WRITE row and body |
| C-03 | PASS | CAMPAIGN SETUP establishes topic identity + inertia baseline before any artifact |
| C-04 | PASS | Hard GATE at Spec close; hard GATE at Proposal close |
| C-05 | PASS | Spec: 5 sections; Proposal: 3+ options + do-nothing + recommendation; Pitch: 3 versions + ANTI-POSITIONING |

Essential: **60/60** — all pass

### Recommended

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Matrix PRESERVE = "All spec design decisions — no re-opening, no new design work"; body reinforces: "PRESERVES: do not re-open any design question the spec resolved." Dual enforcement: matrix + body |
| C-07 | PASS | Matrix CF for Proposal = "Recommended option name and rationale; do-nothing cost"; Pitch body: "CARRIES FORWARD: the recommended option is the subject of all three versions"; DEV: "references the technical design from the spec explicitly"; MAKER: "no spec terminology, no proposal jargon." All three sub-conditions met |
| C-08 | PASS | Setup names topic; close table with per-artifact paths + scout signal consumed |

Recommended: **30/30**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | CONVICTION DELTA per version + NEAR-DUPLICATE CONTENT sub-field. Template structure enforces role differentiation |
| C-10 | PASS | Contract matrix READ row maps all three scout namespaces; "Not conditional. Run regardless of whether signals are found." |
| C-15 | PASS | Pre-execution matrix with all four fields (READ/WRITE/PRESERVE/CARRIES FORWARD) for all three artifacts. Matrix printed before Artifact 1 begins. Strongest pre-execution visibility of all five variations — all obligations declared at a glance before any execution |
| C-16 | PASS | "FINDINGS (write this block after the pitch file is complete — not before, not during):" — label + strengthened placement instruction ("not before, not during"). CONVICTION DELTA per version + NEAR-DUPLICATE CONTENT. Template sub-fields and explicit prohibition against pre-execution writing provide strongest C-16 structural guarantee |

Aspirational: **20/20**

### Excellence

| ID | Result | Evidence |
|----|--------|----------|
| C-11 | PASS | Both GATEs present with explicit blocking language |
| C-12 | PASS | "Not conditional. Run regardless of whether signals are found." Unconditional, setup phase |
| C-13 | PASS | CONVICTION DELTA per version (check 1) + NEAR-DUPLICATE CONTENT (check 2). C-16 passes; full credit |
| C-14 | PASS | Close table: per-artifact scout signal consumed |

Excellence: **+8**

**V-04 Composite: 60 + 30 + 20 + 8 = 118 — GOLDEN**

---

## V-05 — Cascade + FINDINGS Template + Minimal Density

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All three artifact sections present |
| C-02 | PASS | Canonical paths in artifact body write instructions |
| C-03 | PASS | SETUP: "Topic identity: one sentence. Inertia baseline: one sentence." Pre-Artifact 1 |
| C-04 | PASS | Both GATEs present |
| C-05 | PASS | Spec: 5 sections; Proposal: 3+ options + do-nothing + recommendation; Pitch: EXEC/DEV/MAKER + ANTI-POSITIONING |

Essential: **60/60** — all pass

### Recommended

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | "PRESERVE: all spec design decisions — do not re-open anything the spec resolved." Full instruction, labeled field |
| C-07 | PASS | CF from Proposal: "Recommended option: [name]; Rationale: [one sentence]"; Pitch PRESERVE: "recommended option — crystallize it, do not reopen the choice"; DEV: "references technical design from spec"; MAKER: "plain language only, no spec or proposal terminology." All three sub-conditions met |
| C-08 | PASS | SETUP names topic; CAMPAIGN CLOSE table with per-artifact paths + scout signal consumed |

Recommended: **30/30**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | CONVICTION DELTA per version + NEAR-DUPLICATE CONTENT. Template enforces separation even at minimal word count |
| C-10 | PASS | Per-artifact READ fields; "Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional." |
| C-15 | **PARTIAL** | READ and PRESERVE declared as labeled pre-execution fields. CARRIES FORWARD declared post-execution at artifact close (cascade design, same as V-03). **WRITE not a labeled contract field** — paths appear only in body write instructions ("Write simulations/draft/specs/…"). Same gap as V-03: WRITE absent from contract; CF post-execution. Minimal density compounds the gap by removing the path-listing setup block V-03 has. **2.5 pts** |
| C-16 | PASS | "FINDINGS (write after the pitch is written):" — label + post-execution instruction. Template: CONVICTION DELTA per version + NEAR-DUPLICATE CONTENT. Named sub-fields maintain structural C-16 guarantee at compressed word count. Minimal density does not regress C-16 — template carries full credit |

Aspirational: **5 + 5 + 2.5 + 5 = 17.5/20**

### Excellence

| ID | Result | Evidence |
|----|--------|----------|
| C-11 | PASS | Both GATEs present |
| C-12 | PASS | "Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional." |
| C-13 | PASS | CONVICTION DELTA per version (check 1) + NEAR-DUPLICATE CONTENT (check 2). C-16 passes; full credit |
| C-14 | PASS | Close table: per-artifact scout signal consumed. CF from Proposal also records "Scout signal consumed: [namespace or none]" as mid-campaign log |

Excellence: **+8**

**V-05 Composite: 60 + 30 + 17.5 + 8 = 115.5 — GOLDEN**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Excellence | Composite | Golden |
|-----------|-----------|-------------|--------------|------------|-----------|--------|
| V-01 — Contract Matrix | 60 | 30 | 20 | +8 | **118** | Yes |
| V-02 — FINDINGS Template | 60 | 30 | 20 | +8 | **118** | Yes |
| V-03 — CF Cascade | 60 | 30 | 17.5 | +8 | **115.5** | Yes |
| V-04 — Matrix + Template | 60 | 30 | 20 | +8 | **118** | Yes |
| V-05 — Cascade + Template + Density | 60 | 30 | 17.5 | +8 | **115.5** | Yes |

All five are Golden. Three reach the 118 ceiling.

---

## C-15 / C-16 Diagnostic — R3 Questions Answered

**Q1: Does contract matrix vs per-artifact inline affect C-15 partial vs full?**
Format does not determine the outcome — completeness does. Matrix (V-01, V-04) and per-artifact inline (V-02) both earn C-15 FULL because they declare all four fields pre-execution. The cascade variations (V-03, V-05) earn PARTIAL not because of format but because WRITE is absent as a labeled contract field and CARRIES FORWARD is post-execution rather than pre-execution. The differentiator is: are all four fields present and declared before execution begins?

**Q2: Does the FINDINGS template earn C-16 full credit more reliably?**
Both open prompt (V-01, V-03) and template (V-02, V-04, V-05) earn C-16 FULL in R3 — the label and post-execution placement instruction are sufficient. The template adds structural reliability for C-13 (named CONVICTION DELTA forces per-version reflection) and makes pre-execution placement harder to confuse, but is not required for C-16 full credit when both conviction questions are present and explicitly labeled.

**Q3: Does CF at close time vs upfront matrix change C-07 compliance?**
No. Both cascade (V-03, V-05) and matrix (V-01, V-04) pass C-07 at full credit. Proximity of the CF declaration to the consuming artifact does not hurt C-07 compliance. However, the cascade approach costs C-15 because the pre-execution contract is incomplete — WRITE is absent and CF is not declared before execution begins.

**Q4: Does minimal density (V-05) retain C-16 full credit?**
Yes. The FINDINGS template earns C-16 full credit even at compressed word count. Minimal density does not regress C-16. The structural template (labeled block + named sub-fields + post-execution trigger) carries full credit independent of surrounding density.

---

## Excellence Signals — Patterns from 118-Ceiling Variations

**Pattern 1: WRITE must be a labeled contract field, not just a write instruction in the body.**
V-03 and V-05 both have canonical paths in their body write instructions ("Write simulations/draft/specs/…") but not as a labeled `WRITE:` contract field. The rubric requires all four fields declared as a contract. The distinction between a write instruction and a WRITE contract declaration is structural — the label signals an obligation, not just an action.

**Pattern 2: Pre-execution CARRIES FORWARD is required for C-15 full credit — post-execution cascade earns PARTIAL.**
The cascade hypothesis (proximity to consumer improves C-07 compliance) is technically correct for C-07 but costs C-15. An upfront declaration that CARRIES FORWARD the recommended option makes the obligation visible before execution begins; the cascade puts it after execution when it is too late to serve as a pre-execution constraint. Both mechanisms pass C-07 — but only pre-execution CF passes C-15.

**Pattern 3: Open-prompt FINDINGS with explicit label + both conviction questions earns C-16 full — named sub-fields improve C-13 assurance but are not required for C-16 full credit.**
V-01 and V-03 use an open prompt; V-02, V-04, V-05 use a template. All earn C-16 FULL when the label and post-execution instruction are explicit. The template's advantage is C-13 reliability — named CONVICTION DELTA sub-fields make it structurally difficult to satisfy the audit with a pre-execution declaration.

**Pattern 4: The V-04 combination (matrix + template) closes both aspirational criteria with maximum structural guarantees.**
The matrix eliminates all C-15 ambiguity (all four fields, all three artifacts, printed before execution clears). The template eliminates C-16 ambiguity (labeled block, named sub-fields, explicit not-before-not-during instruction). Neither mechanism depends on the other, but combined they provide defense in depth against both aspirational partial patterns.

---

## R3 Ranking

1. **V-04** — 118 — Matrix + template combination. Dual structural mechanisms; strongest C-15 + C-16 guarantee; most explicit placement prohibition ("not before, not during").
2. **V-01** — 118 — Matrix alone with open-prompt FINDINGS. Hits ceiling; slightly less C-16 assurance than template format but fully passes.
3. **V-02** — 118 — Per-artifact inline contracts + template. Hits ceiling; C-13 sub-field structure is the strongest conviction audit formulation in R3.
4. **V-03** — 115.5 — CF cascade with open-prompt FINDINGS. WRITE field absent from contract; CF post-execution. Both cause C-15 PARTIAL. Cascade mechanism vindicated for C-07 but does not compensate for missing contract fields.
5. **V-05** — 115.5 — Cascade + template + minimal density. Confirms minimal density does not hurt C-16. Same C-15 gap as V-03 despite template addition.

---

```json
{"top_score": 118, "all_essential_pass": true, "new_patterns": ["WRITE must be a labeled contract field — a write instruction in the body does not satisfy C-15; the label signals an obligation, not just an action", "Pre-execution CARRIES FORWARD declaration is required for C-15 full credit — cascade CF at artifact close earns PARTIAL because the pre-execution contract is incomplete regardless of C-07 compliance", "Open-prompt FINDINGS with explicit label and both conviction questions earns C-16 full credit — named sub-fields improve C-13 assurance and placement reliability but are not required for C-16 full credit"]}
```
