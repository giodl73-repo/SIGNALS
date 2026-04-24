## Quest Score — corps-scan R1

### Scoring Methodology

**Point weights:**
- Essential (C-01–C-05): 12 pts each = 60 pts
- Recommended (C-06–C-08): 10 pts each = 30 pts
- Aspirational (C-09–C-10): 5 pts each = 10 pts
- **Total: 100 pts**

PASS = full, PARTIAL = half, FAIL = 0.

---

### V-01 — YAML-First, Inline Annotation

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01 YAML block present | Essential | PASS | Format-first design makes YAML the opening artifact; cannot be deferred |
| C-02 Repo-grounded areas | Essential | PARTIAL | Inline `# detected from:` comments help, but no explicit inventory step before output — detection may be shallow |
| C-03 Group hierarchy | Essential | PASS | YAML structure invites division/tribe nesting; hierarchy expressed naturally in YAML nesting |
| C-04 Named roles per team | Essential | PASS | YAML keys force role enumeration per team area |
| C-05 No .roles/ | Essential | PASS | Stated as hard constraint up front before output begins |
| C-06 Pivot mode + rationale | Recommended | PARTIAL | Mode likely named in preamble but format pressure toward YAML reduces prose rationale depth |
| C-07 Exec office placeholder | Recommended | PASS | YAML skeleton naturally includes an exec-office section if the format template includes it |
| C-08 Amend options | Recommended | PASS | "Three explicit amend options at the end cover C-08 mechanically" — stated in hypothesis |
| C-09 Detection rationale inline | Aspirational | PASS | Inline `# detected from:` is the defining mechanic of this variation |
| C-10 Inertia Advocate noted | Aspirational | FAIL | No narrative framing; YAML-first format has no natural place for inertia pattern naming |

**Score: 12 + 6 + 12 + 12 + 12 + 5 + 10 + 10 + 5 + 0 = 84/100**
All essential pass: NO (C-02 PARTIAL)

---

### V-02 — Conversational + Descriptive Register

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01 YAML block present | Essential | PARTIAL | Think-aloud register risks prose drift; YAML may appear but completeness not structurally guaranteed |
| C-02 Repo-grounded areas | Essential | PASS | Narration naturally surfaces detection reasoning; grounding is a side-effect of describing the scan |
| C-03 Group hierarchy | Essential | PARTIAL | Conversational format describes grouping but may not enforce YAML-expressed hierarchy |
| C-04 Named roles per team | Essential | PARTIAL | Narrative may describe roles instead of enumerating 2+ named roles per area |
| C-05 No .roles/ | Essential | PASS | C-05 front-loaded as a named constraint before register relaxes |
| C-06 Pivot mode + rationale | Recommended | PASS | Think-aloud naturally generates rationale prose alongside the mode declaration |
| C-07 Exec office placeholder | Recommended | PARTIAL | May mention exec office conversationally but not produce a YAML section |
| C-08 Amend options | Recommended | PARTIAL | Conversational closing risks "let me know if you want changes" which explicitly fails C-08 |
| C-09 Detection rationale inline | Aspirational | PASS | Narrative register produces C-09 naturally without explicit instruction |
| C-10 Inertia Advocate noted | Aspirational | PASS | Hypothesis explicitly states C-10 "emerges from narrative framing" |

**Score: 6 + 12 + 6 + 6 + 12 + 10 + 5 + 5 + 5 + 5 = 72/100**
All essential pass: NO (C-01, C-03, C-04 PARTIAL)

---

### V-03 — Explicit Phase Gates (SCAN → PIVOT → DRAFT → AMEND)

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01 YAML block present | Essential | PASS | DRAFT gate requires producing YAML before proceeding; cannot skip |
| C-02 Repo-grounded areas | Essential | PASS | SCAN phase must complete and produce inventory before PIVOT; grounding is a gate exit condition |
| C-03 Group hierarchy | Essential | PASS | DRAFT phase structures YAML hierarchically; phase gates enforce output shape |
| C-04 Named roles per team | Essential | PASS | DRAFT gate includes role listing as part of the YAML template |
| C-05 No .roles/ | Essential | PASS | "DRAFT GATE states the draft-only constraint as an entry condition" — cannot enter DRAFT without acknowledging boundary |
| C-06 Pivot mode + rationale | Recommended | PASS | PIVOT phase is dedicated to mode declaration + rationale; rationale required to exit |
| C-07 Exec office placeholder | Recommended | PARTIAL | No phase explicitly mandates exec-office section; may be omitted in DRAFT |
| C-08 Amend options | Recommended | PASS | AMEND is an explicit phase with its own gate; options must be named to complete |
| C-09 Detection rationale inline | Aspirational | PARTIAL | Phase gates enforce section completion but not inline annotation depth; notes may be minimal |
| C-10 Inertia Advocate noted | Aspirational | FAIL | No phase gate addresses inertia framing; variation doesn't name a stagnation pattern |

**Score: 12 + 12 + 12 + 12 + 12 + 10 + 5 + 10 + 2.5 + 0 = 87.5/100 → 88**
All essential pass: YES

---

### V-04 — Role Sequence + Inertia Framing (Combination)

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01 YAML block present | Essential | PASS | Drafter stage produces YAML from the archaeologist inventory; two-stage design means YAML is the drafter's deliverable |
| C-02 Repo-grounded areas | Essential | PASS | "Repo Archaeologist role forces C-02 grounding by producing an inventory the drafter must draw from" |
| C-03 Group hierarchy | Essential | PASS | Archaeologist inventory feeds structural grouping decisions in the drafter stage |
| C-04 Named roles per team | Essential | PASS | Role enumeration is the drafter's second task after YAML structure |
| C-05 No .roles/ | Essential | PASS | Two-stage design is output-only; neither stage writes .roles/ |
| C-06 Pivot mode + rationale | Recommended | PARTIAL | Mode implied by archaeologist's findings but not necessarily declared with explicit rationale |
| C-07 Exec office placeholder | Recommended | PARTIAL | Not mentioned as a strength; exec office may be omitted unless archaeologist inventory surfaces it |
| C-08 Amend options | Recommended | PASS | "C-08 the richest of any variation" — anti-inertia amend options derived from specific pattern found |
| C-09 Detection rationale inline | Aspirational | PASS | Archaeologist produces an inventory that is the detection rationale; drafter draws from it explicitly |
| C-10 Inertia Advocate noted | Aspirational | PASS | "Status-Quo Challenger names the stagnation pattern and primes C-10 naturally" |

**Score: 12 + 12 + 12 + 12 + 12 + 5 + 5 + 10 + 5 + 5 = 90/100**
All essential pass: YES

---

### V-05 — Output Format + Lifecycle Emphasis (Combination)

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01 YAML block present | Essential | PASS | Named section for YAML makes omission visible — skipping requires active deletion of a section header |
| C-02 Repo-grounded areas | Essential | PASS | Scan section must be filled with repo signals before YAML section; section order enforces sequencing |
| C-03 Group hierarchy | Essential | PASS | "Strongest on C-03" per hypothesis; YAML section template includes hierarchy |
| C-04 Named roles per team | Essential | PASS | Roles are a named subsection within YAML; formulaic filling still satisfies criterion |
| C-05 No .roles/ | Essential | PASS | No section for role files; skeleton contains no .roles/ affordance |
| C-06 Pivot mode + rationale | Recommended | PASS | Pivot section is named and must be completed with mode + rationale |
| C-07 Exec office placeholder | Recommended | PASS | "Strongest on C-07" — exec office appears as a named section, not optional |
| C-08 Amend options | Recommended | PASS | "Strongest on C-08" — amend section is the final named section, must be populated |
| C-09 Detection rationale inline | Aspirational | PARTIAL | "Weakest on C-09 depth" — fixed structure may produce formulaic notes rather than genuine rationale |
| C-10 Inertia Advocate noted | Aspirational | PARTIAL | Skeleton has no dedicated section for inertia framing; may or may not surface depending on fill quality |

**Score: 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 2.5 + 2.5 = 95/100**
All essential pass: YES

---

### Final Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 — Format + Lifecycle Combination | 95 | YES |
| 2 | V-04 — Role Sequence + Inertia Framing | 90 | YES |
| 3 | V-03 — Explicit Phase Gates | 88 | YES |
| 4 | V-01 — YAML-First, Inline Annotation | 84 | NO |
| 5 | V-02 — Conversational Register | 72 | NO |

---

### Excellence Signals from V-05

**What made V-05 the top scorer:**

1. **Structural compulsion over instruction** — Named sections make criterion omission visually obvious. A model that skips a section has to delete a header, not just fail to mention something. This is a fundamentally different failure mode than instruction-based prompts.

2. **Orthogonal redundancy across mechanisms** — Format constraints (named sections) and lifecycle constraints (scan before YAML) enforce the same essential criteria via independent paths. C-02 is covered by section ordering *and* by the YAML section requiring repo-derived names. Two mechanisms, one criterion — harder to fail both.

3. **Weaknesses are predictable and bounded** — V-05's only losses are C-09/C-10 depth, which are aspirational. The combination design consistently passes all 8 essential+recommended criteria. Combinations that give up aspirational depth in exchange for reliable essential/recommended coverage represent a good engineering trade-off for a draft skill.

**Why V-04 nearly matched it:** Role separation (Archaeologist → Drafter) produces the richest C-08 and C-10 — the inertia framing is qualitatively better in V-04 than V-05's formulaic fill. V-04 loses on C-06 and C-07 only because no explicit section enforces them.

**The failure pattern confirmed by V-02:** Conversational register is the most dangerous format for essential criteria compliance — it scores highest on aspirational criteria (C-09, C-10) but multiple essentials are only PARTIAL. Quality of prose does not substitute for structural enforcement of output shape.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["structural-compulsion-over-instruction: named output sections make criterion omission visually obvious and require active deletion to skip, unlike instruction-based prompts where omission is passive", "orthogonal-redundancy: two independent mechanisms (format skeleton + lifecycle gate) both enforcing the same essential criterion creates a harder-to-fail combination than either alone"]}
```
