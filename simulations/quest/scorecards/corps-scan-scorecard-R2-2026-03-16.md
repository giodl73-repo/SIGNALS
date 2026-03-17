## corps-scan R2 — Quest Score

**Rubric**: v2, 110 pts (5E×12 + 3R×10 + 4A×5)
**Golden threshold**: 80 pts with all 5 essential passing

---

## Per-Variation Scoring

### V-01 — Constraint-First Architecture

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Step 3 produces a complete YAML block template with `org:`, `exec-office:`, `groups:`, `teams:`, `roles:` |
| C-02 | Team areas derived from repo | **PASS** | "Every team area name traceable to a signal in the Detected Signals table above. No invented names." Hard traceability rule enforced |
| C-03 | Group structure present | **PASS** | YAML template requires group container with `type: [division|tribe|pillar]` above teams |
| C-04 | Standard roles per team | **PASS** | "Every team area has 2+ named roles (not 'roles go here')" — named examples given: PM, Engineer, Tech Lead, Security Architect |
| C-05 | Does not write .craft/roles/ | **PASS** | First sentence literally: "This output is a draft org.yaml for human review. No role files will be created." Step 4 amend section closed with "All three options are required." |
| C-06 | Pivot mode declared with rationale | **PASS** | Dedicated `Pivot mode selected:` + `Rationale:` block required, citing "at least one specific signal from the table above" |
| C-07 | Exec office placeholder present | **PASS** | `exec-office:` section in YAML template, "placeholder name is fine" |
| C-08 | Amend options listed | **PASS** | AMEND-A/B/C all named with specific commands; "Let me know if you want changes does not pass" stated explicitly |
| C-09 | Detection rationale per area | **PASS** | `# detected from: [signal row reference]` required on "at least half the team areas" |
| C-10 | Inertia Advocate noted | **PASS** | `# Inertia Advocate: added automatically by corps-build` in YAML template |
| C-11 | Pre-YAML scan inventory listed | **PASS** | "Step 2 -- Detected Signals (required before YAML)" — structured table required, explicitly labeled "before YAML" |
| C-12 | Draft boundary front-loaded | **PASS** | Literally the first line of the variation: "**This output is a draft org.yaml for human review. No role files will be created.**" — before skill context, before instructions |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5 = 110/110**

---

### V-02 — Signal-Table Inventory

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Step 2 produces full YAML block with org structure |
| C-02 | Team areas derived from repo | **PASS** | "Every team area must appear as a 'Proposed team area' row in the Signal Inventory above. No team area may appear in the YAML that is not in the inventory." |
| C-03 | Group structure present | **PASS** | Group container with `type: [division|tribe|pillar]` in template |
| C-04 | Standard roles per team | **PASS** | "Every team has 2+ named roles" in constraint check |
| C-05 | Does not write .craft/roles/ | **PASS** | DRAFT-ONLY banner: "It does not write `.craft/roles/` files...does not include role file content." |
| C-06 | Pivot mode declared with rationale | **PASS** | Pivot mode + "one sentence citing a specific table row" + "Secondary mode considered" — stronger than minimum |
| C-07 | Exec office placeholder present | **PASS** | exec-office in YAML template, "mark PLACEHOLDER if unsure" |
| C-08 | Amend options listed | **PASS** | AMEND-A/B/C with commands; AMEND-A includes "what this alternative would reveal instead" — good rationale |
| C-09 | Detection rationale per area | **PASS** | Evidence column in Signal Inventory table provides rationale; `# signal:` comment in YAML references back |
| C-10 | Inertia Advocate noted | **PASS** | `# Inertia Advocate: auto-added by corps-build` in YAML template |
| C-11 | Pre-YAML scan inventory listed | **PASS** | "Build the Signal Inventory" is Step 1 — distinct 3-column table before YAML |
| C-12 | Draft boundary front-loaded | **PASS** | Blockquote banner appears immediately after the first sentence, before Step 1 scan. However: first sentence is "You are running `corps-scan`. Produce a draft `org.yaml` for human review." — the boundary blockquote follows on the very next line. This is close but not the *very first line* — it's effectively front-loaded but one sentence delayed. **PASS** (boundary appears before any structural content or YAML) |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5 = 110/110**

---

### V-03 — Minimal Instructions

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Item 3 explicitly requires the complete YAML block with all structural elements |
| C-02 | Team areas derived from repo | **PASS** | "Every team area name traceable to a signal in the inventory above" stated as YAML requirement |
| C-03 | Group structure present | **PASS** | "At least one group container (division, tribe, or pillar) above teams" required |
| C-04 | Standard roles per team | **PASS** | "Every team area lists 2+ named roles (Engineer, PM, Tech Lead, Security Architect, etc.)" |
| C-05 | Does not write .craft/roles/ | **PASS** | Closing: "Do not write `.craft/roles/` files. Do not include role file content." + item 1 states draft-only |
| C-06 | Pivot mode declared with rationale | **PASS** | Item 2 requires: "Include the pivot mode you selected and one sentence of rationale" |
| C-07 | Exec office placeholder present | **PASS** | "`exec-office` section with a name (placeholder is fine)" in YAML requirements |
| C-08 | Amend options listed | **PASS** | Item 4 names AMEND-A/B/C with specific commands required |
| C-09 | Detection rationale per area | **PASS** | "`# detected from:` comment on at least half the team areas" required in YAML |
| C-10 | Inertia Advocate noted | **PASS** | "`# Inertia Advocate: added automatically by corps-build` note in at least one team block" explicitly required |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Item 2 is "Repo signal inventory (before the YAML)" — "distinct section that appears before the YAML block" |
| C-12 | Draft boundary front-loaded | **PASS** | Item 1 is "Draft-only acknowledgment (one sentence, before anything else): State that this output is a draft...This must appear as the **first line** of your response before any scan, any inventory, and any YAML." — the strongest possible instruction for C-12 |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5 = 110/110**

---

### V-04 — Compliance Pre-Check + Signal Table

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Step 2 produces complete YAML; post-write checklist verifies |
| C-02 | Team areas derived from repo | **PASS** | "Traceability rule: every team area name must match a 'Team area candidate' cell in the Signal Table." Post-write checklist item 1 confirms |
| C-03 | Group structure present | **PASS** | "At least one group container" in post-write checklist |
| C-04 | Standard roles per team | **PASS** | PRE-CHECK item 4: "Every team area I draft will list at least 2 named roles." Checklist must be CONFIRMED before proceeding |
| C-05 | Does not write .craft/roles/ | **PASS** | PRE-CHECK item 1 explicitly confirmed: "I will NOT write .craft/roles/ files, include role file content, or instruct the user to create role files." Final gate confirms "Draft-only constraint: held -- no role files written" |
| C-06 | Pivot mode declared with rationale | **PASS** | Signal Table requires "Pivot mode" + "Rationale: one sentence citing a specific table row" |
| C-07 | Exec office placeholder present | **PASS** | PRE-CHECK item 5 confirmed; exec-office in YAML; "Exec office inference" in Signal Table |
| C-08 | Amend options listed | **PASS** | AMEND-A/B/C with commands; AMEND-A names "which rows favor this mode" and "what a different mode clusters differently" — excellent rationale |
| C-09 | Detection rationale per area | **PASS** | Signal Table has "Detection note" column (one sentence per signal); `# signal: [table row reference]` in YAML |
| C-10 | Inertia Advocate noted | **PASS** | `# Inertia Advocate: auto-added by corps-build -- expect it in role files` in YAML template |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Step 1 Signal Table is explicitly a pre-YAML inventory; PRE-CHECK item 2 confirms "I will produce a repo signal inventory as a distinct section BEFORE the YAML block begins" |
| C-12 | Draft boundary front-loaded | **PASS** | PRE-CHECK item 1 is the very first content after the opening sentence; the checklist must be completed before any output. C-12 also embedded as PRE-CHECK item 3: "The draft-only statement (above) appears before any YAML or structural content in this response. STATUS: CONFIRMED" — C-12 is *self-confirming* |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5 = 110/110**

---

### V-05 — Evidence Mandate + Anti-Debt Amend

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Draft org.yaml block present | **PASS** | Phase 2 produces complete YAML block |
| C-02 | Team areas derived from repo | **PASS** | "Every team area name must match a 'Maps to' value from the Evidence Inventory above. No names that do not appear in the inventory." |
| C-03 | Group structure present | **PASS** | Group container with `type: [division|tribe|pillar]` in template |
| C-04 | Standard roles per team | **PASS** | YAML template shows 2+ named roles per team; implied by template structure |
| C-05 | Does not write .craft/roles/ | **PASS** | DRAFT-ONLY CONSTRAINT banner: "It does not write `.craft/roles/` files. It does not instruct the user to create role files. It does not include role file content." Post-YAML verification states "No .craft/roles/ content produced" |
| C-06 | Pivot mode declared with rationale | **PASS** | "Pivot mode selected: ... Rationale: one sentence naming at least one Signal number above" |
| C-07 | Exec office placeholder present | **PASS** | exec-office in YAML; confirmation note included |
| C-08 | Amend options listed | **PASS** | AMEND-A/B/C present with commands; "Debt if skipped" adds substantive rationale well beyond C-08 minimum |
| C-09 | Detection rationale per area | **PASS** | "Evidence: one sentence" per signal in Evidence Inventory + `# evidence: [brief ref]` in YAML — strongest evidence mandate of all 5 variations |
| C-10 | Inertia Advocate noted | **PASS** | "Inertia Advocate note" in Phase 1 inventory: "corps-build will automatically add an Inertia Advocate role to each team's role files" — and `# Inertia Advocate: added at corps-build time` in YAML |
| C-11 | Pre-YAML scan inventory listed | **PASS** | Phase 1 Evidence Inventory is a distinct, structured, per-signal enumeration before Phase 2 YAML |
| C-12 | Draft boundary front-loaded | **PASS** | DRAFT-ONLY CONSTRAINT banner in a blockquote appears after the opening sentence "You are running `corps-scan`." — before any structural content, before Phase 1. Effectively front-loaded; the banner is the first substantive content |

**Score: 12+12+12+12+12 + 10+10+10 + 5+5+5+5 = 110/110**

---

## Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (20) | Total | All-E Pass | Golden |
|-----------|---------------|------------------|-------------------|-------|------------|--------|
| V-01 | 60 | 30 | 20 | **110** | Yes | Yes |
| V-02 | 60 | 30 | 20 | **110** | Yes | Yes |
| V-03 | 60 | 30 | 20 | **110** | Yes | Yes |
| V-04 | 60 | 30 | 20 | **110** | Yes | Yes |
| V-05 | 60 | 30 | 20 | **110** | Yes | Yes |

**All 5 variations score 110/110.**

---

## Ranking

R2 designed C-11 and C-12 as structural invariants across all variations — the design goal succeeded. Differentiating on execution quality within the 110/110 ceiling:

1. **V-04** — *Top* — Self-confirming compliance (C-12 appears in a checklist that must be confirmed AND as a checklist item verifying itself). Pre-check + signal table + post-write checklist + final gate = maximum defensive structure. Hardest to accidentally violate.
2. **V-01** — *Strong* — C-12 as literal first sentence (strongest timing), signal table with explicit "required before YAML" label, traceability hard rule. Elegant constraint-first architecture.
3. **V-05** — *Strong* — Best C-09 form (one evidence sentence per signal + YAML `# evidence:` ref). Debt-aware amend options are substantively richer than any other variation. Inertia Advocate note in prose (Phase 1) + YAML (Phase 2) — most prominent C-10.
4. **V-03** — *Solid* — Minimal but complete. Item 1 explicitly requires C-12 as "first line of your response" — strongest plain-English instruction. Lowest scaffolding risk if model follows numbered list faithfully.
5. **V-02** — *Solid* — Signal table with evidence column. C-12 is front-loaded but not the absolute first line (one sentence precedes the banner). AMEND-A secondary mode rationale is a nice depth touch.

---

## Excellence Signals (from top scorer V-04)

**Pattern 1: Self-referential compliance** — C-12 is not only stated before output; it appears as a checklist item (PRE-CHECK item 3) that explicitly confirms itself: "The draft-only statement (above) appears before any YAML or structural content in this response. STATUS: CONFIRMED." The model cannot satisfy the checklist without having already satisfied C-12.

**Pattern 2: Dual-stage verification** — PRE-CHECK (before any output) + post-write checklist (after YAML) creates a bracket: constraints are confirmed before and after the primary artifact. No other variation brackets the YAML with explicit verification on both sides.

**Pattern 3: Criterion embedding in instrument** — C-04, C-05, C-07, C-11, C-12 are all explicitly named as PRE-CHECK items. The rubric criteria become the instrument's own requirements, making the connection between skill design and scoring criteria transparent and enforceable.

**New pattern from V-05: Debt-framed amend options** — Naming what breaks downstream if an amend option is skipped ("Debt if skipped") converts C-08 amend options from navigation aids into decision-support tools. This is a stronger amend form and should be considered for adoption in future rubrics.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["self-referential compliance: checklist item that confirms itself satisfies the criterion it names", "dual-stage YAML bracketing: pre-check before + post-write checklist after the YAML artifact", "criterion embedding in instrument: rubric criteria explicitly named as the skill's own pre-check requirements", "debt-framed amend options: each option names the downstream organizational debt that accumulates if skipped"]}
```
