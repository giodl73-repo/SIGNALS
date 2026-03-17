## Scoring: program-plan Round 1 (v1 rubric)

### Scoring Key
| Tier | Criteria | Points each | Total |
|------|----------|-------------|-------|
| Essential | C-01–C-04 | 15 | 60 |
| Recommended | C-05–C-07 | 10 | 30 |
| Aspirational | C-08–C-09 | 5 | 10 |

PASS = full, PARTIAL = half, FAIL = 0

---

### V-01 — Role Sequence

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 YAML validity | PASS (15) | Format skeleton structures output |
| C-02 Echo contract | PASS (15) | Step 4 is an explicit dedicated echo step |
| C-03 Valid skill names | PASS (15) | Role table anchors skills before ordering |
| C-04 Evidence-state gates | PASS (15) | Good/bad gate examples contrast execution vs evidence state |
| C-05 Namespace order | PARTIAL (5) | Phase ordering by role, not explicitly namespace-dependency order |
| C-06 Descriptive names | PASS (10) | Explicit prohibition: "not 'scout' or 'stage1'" |
| C-07 Plan-not-executor | PASS (10) | Header + YAML comment dual reinforcement |
| C-08 Quantified gate | PASS (5) | "At least one quantified gate" is a hard requirement |
| C-09 Evidence arc | PARTIAL (2.5) | Breadth-to-depth implied by role phases but not named as arc |

**V-01 Total: 92.5**

---

### V-02 — Annotated YAML Skeleton

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 YAML validity | PASS (15) | Pre-structured template makes structural errors nearly impossible |
| C-02 Echo contract | PASS (15) | `# REQUIRED` inline at the echo field — structurally unforgettable |
| C-03 Valid skill names | PARTIAL (7.5) | Per-namespace hints help but no explicit catalog table |
| C-04 Evidence-state gates | PASS (15) | `# EXAMPLE` / `# BAD` inline at gate authoring point |
| C-05 Namespace order | PARTIAL (5) | Dependency rule is a comment, not structural enforcement |
| C-06 Descriptive names | PASS (10) | "descriptive label, not stage1" inline in template |
| C-07 Plan-not-executor | PARTIAL (5) | Header comment only, less prominent than dedicated section |
| C-08 Quantified gate | PARTIAL (2.5) | `# HINT` with example but not a hard requirement |
| C-09 Evidence arc | PARTIAL (2.5) | Namespace order rule present; arc not explicitly named |

**V-02 Total: 77.5**

---

### V-03 — Phrasing Register (Question Framing)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 YAML validity | PARTIAL (7.5) | "End instruction" for YAML — question framing may not enforce structure |
| C-02 Echo contract | PARTIAL (7.5) | "Closing section" — present but can be deprioritized |
| C-03 Valid skill names | PARTIAL (7.5) | Questions organized by phase, not an explicit skill-name catalog |
| C-04 Evidence-state gates | PASS (15) | "How will we know it's answered?" directly produces evidence-state language |
| C-05 Namespace order | PARTIAL (5) | "Keep questions in order" addresses ordering but loosely |
| C-06 Descriptive names | PASS (10) | Question-cluster naming is inherently descriptive |
| C-07 Plan-not-executor | PARTIAL (5) | Implicit in framing; not an explicit rule |
| C-08 Quantified gate | PARTIAL (2.5) | "Make at least one..." required but not emphasized by the axis |
| C-09 Evidence arc | PASS (5) | Question sequence catalog explicitly builds the arc |

**V-03 Total: 65**

---

### V-04 — Combined: Role Sequence + Lifecycle Bands

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 YAML validity | PASS (15) | Band diagram with format skeleton structures full output |
| C-02 Echo contract | PASS (15) | `# required` comments embedded in each band's YAML section |
| C-03 Valid skill names | PASS (15) | Per-band skill catalog is explicit and partitioned |
| C-04 Evidence-state gates | PASS (15) | Handoff memo framing: "what the next role needs to start" = artifact-referencing gates |
| C-05 Namespace order | PASS (10) | Bands (Prove It / Design It / Simulate It / Listen Ahead) encode namespace dependency structurally |
| C-06 Descriptive names | PASS (10) | Band-purpose naming guide drives stage labels; band names are concrete examples |
| C-07 Plan-not-executor | PASS (10) | Header sentence is explicit; `owner:` fields per band reinforce planner identity |
| C-08 Quantified gate | PARTIAL (2.5) | "Make at least one…" required but secondary to band framing |
| C-09 Evidence arc | PASS (5) | Four bands breadth→depth is the arc; explicitly labeled and sequenced |

**V-04 Total: 97.5**

---

### V-05 — Combined: Output Format + Inertia Contrast

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 YAML validity | PASS (15) | Template + GOOD example removes ambiguity |
| C-02 Echo contract | PASS (15) | Hard rules + shown in GOOD example — dual anchoring |
| C-03 Valid skill names | PASS (15) | Explicit skill catalog table — most direct approach of all five |
| C-04 Evidence-state gates | PASS (15) | BAD inertia YAML vs GOOD gated YAML makes the failure mode concrete at authoring time |
| C-05 Namespace order | PASS (10) | Dependency rule explicit; BAD example shows violation |
| C-06 Descriptive names | PASS (10) | "not 'stage1' or 'scout'" prohibition in rules; reinforced in GOOD example |
| C-07 Plan-not-executor | PASS (10) | Opening paragraph + YAML comment — dual reinforcement |
| C-08 Quantified gate | PARTIAL (2.5) | Gate checklist item present; not reinforced by a concrete BAD/GOOD contrast |
| C-09 Evidence arc | PARTIAL (2.5) | Dependency rule addresses sequence; no named arc narrative |

**V-05 Total: 95**

---

### Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-04 Role+Bands | **97.5** | YES |
| 2 | V-05 Format+Inertia | 95.0 | YES |
| 3 | V-01 Role Sequence | 92.5 | YES |
| 4 | V-02 Annotated Skeleton | 77.5 | NO (C-03 PARTIAL) |
| 5 | V-03 Phrasing Register | 65.0 | NO (C-01, C-02, C-03 PARTIAL) |

---

### Excellence Signals — V-04

**Why V-04 wins:**

1. **Named lifecycle bands encode namespace dependency structurally.** The four bands (Prove It / Design It / Simulate It / Listen Ahead) let the model reason about ordering from *purpose* rather than memorizing namespace rules. Correct order falls out naturally.

2. **Handoff memo framing produces evidence-state gates without reminding.** When each gate is framed as "what the next role needs to start," the output is artifact-referencing by construction — execution-state gates ("feature coded") can't answer the question.

3. **Per-band skill catalog eliminates invented names.** Partitioning the skill catalog by band makes it impossible to reach for a skill outside the allowed set without crossing a visible boundary.

4. **Owner fields per band make plan identity explicit without a dedicated rule.** Assigning an owner (PM / Architect / Dev / Lead) signals that the YAML describes *who orchestrates*, not *who executes* — C-07 compliance without a separate instruction.

The one gap: C-08 (quantified gates) is only weakly addressed. V-04's next iteration should embed a `# REQUIRED: at least one gate must include a count or threshold` annotation inside the band template.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["named lifecycle bands encode namespace dependency structurally — correct ordering falls out from band purpose without memorizing dependency rules", "handoff memo gate framing produces evidence-state language by construction — execution-state gates cannot answer what-the-next-role-needs", "per-band skill catalog partitioning eliminates invented skill names by making out-of-scope reach visible"]}
```
