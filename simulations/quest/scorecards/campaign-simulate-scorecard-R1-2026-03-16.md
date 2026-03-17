## campaign-simulate — Round 1 Scoring

### V-01 (Output Format)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All five invoked | PASS | Execution Log table requires status per sub-skill; "no findings" must state why — silence structurally fails |
| C-02 Sequential order | PASS | Numbered 1–5 with explicit "do not reorder" instruction |
| C-03 Unified report | PASS | Single file with Findings Table + Ranked Findings + Cross-Skill Patterns |
| C-04 Blast radius sort | PASS | Blast Radius is a required column; Ranked Findings uses four explicit tiers |
| C-05 Spec anchoring | PASS | "Spec Location" is a required field; "the spec is unclear without a named location fails this field" |
| C-06 Source+Location+Impact | PASS | Sub-Skill, Spec Location, and Impact (if ignored) are all required table columns |
| C-07 Coverage breadth | PARTIAL | Execution Log tracks all 5 but no rule requires findings from ≥3 sub-skills |
| C-08 Remediation guidance | PASS | Remediation is required column; "'fix the spec' is not acceptable" with named target rule |
| C-09 Cross-skill patterns | PASS | Cross-Skill Patterns section with structured table required; empty-state defined |
| C-10 Blast radius rationale | PASS | Top-three positions require explicit rationale naming downstream scope |

**V-01 composite: 60 + (10+5+10) + (5+5) = 95**

---

### V-02 (Lifecycle Emphasis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All five invoked | PASS | Each sub-skill has a named 3-phase section; absent section = did not run |
| C-02 Sequential order | PASS | Numbered 1–5; phase protocol gates advancement before proceeding |
| C-03 Unified report | PASS | SYNTHESIS section produces single file |
| C-04 Blast radius sort | PASS | Synthesis table has Blast Radius column; "system-wide > cross-skill > component-wide > isolated" stated |
| C-05 Spec anchoring | PASS | Phase 3 requires "specific spec location (named section or boundary)" as non-optional extract field |
| C-06 Source+Location+Impact | PASS | Phase 3 format lists sub-skill source, spec location, and impact as required; synthesis table echoes all three |
| C-07 Coverage breadth | PARTIAL | All 5 must have Phase 3 output but no minimum findings-per-skill rule |
| C-08 Remediation guidance | PARTIAL | Remediation column present in synthesis table but no failure rule for vague entries; not required in Phase 3 extract format |
| C-09 Cross-skill patterns | PASS | Cross-Skill Patterns table required in synthesis |
| C-10 Blast radius rationale | PASS | Top-three findings require explicit downstream rationale immediately below each row |

**V-02 composite: 60 + (10+5+5) + (5+5) = 90**

---

### V-03 (Phrasing Register)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All five invoked | PASS | "Every check must appear in the report, even if it found nothing. A check that found nothing must say why." |
| C-02 Sequential order | PASS | Checks numbered 1–5 in defined order; gate-check framing implies sequential proof |
| C-03 Unified report | PASS | FINDINGS REPORT consolidates all checks into single file output |
| C-04 Blast radius sort | PASS | Dedicated RANKED BY BLAST RADIUS section; "System-wide first" explicit |
| C-05 Spec anchoring | PASS | "A finding without a spec location is not a finding, it is a guess" — strongest single anchoring statement of all variations |
| C-06 Source+Location+Impact | PASS | Findings report format names Sub-skill, Spec location, and What breaks if you ship it as required fields |
| C-07 Coverage breadth | PARTIAL | All checks must appear but no structural table enforcing breadth of findings |
| C-08 Remediation guidance | PASS | "What to fix" is a required field with a concrete anti-example naming target and described action |
| C-09 Cross-skill patterns | PASS | COMPOUNDING FINDINGS section required; root-cause-only test clearly stated |
| C-10 Blast radius rationale | PASS | Top-three findings require explicit scope rationale naming downstream breadth |

**V-03 composite: 60 + (10+5+10) + (5+5) = 95**

---

### V-04 (Combined: Output Format + Lifecycle Emphasis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All five invoked | PASS | 5 named execution sections + Phase 3 extract per sub-skill + Findings Table Sub-Skill column — triple enforcement |
| C-02 Sequential order | PASS | Numbered 1–5; 3-phase protocol gate; strongest sequential enforcement |
| C-03 Unified report | PASS | SYNTHESIS section: Findings Table + Ranked Findings + Cross-Skill Patterns as required sections |
| C-04 Blast radius sort | PASS | Blast radius is a required finding schema field with enumerated values; Ranked Findings table sorts by four explicit tiers |
| C-05 Spec anchoring | PASS | "Spec location: [required: ... vague references such as 'the spec does not cover this' fail this field]" — failure rule embedded in schema |
| C-06 Source+Location+Impact | PASS | Sub-skill, Spec location, and Impact are required schema fields with named failure conditions |
| C-07 Coverage breadth | PARTIAL | Strongest structural pressure via Phase 1 setup per sub-skill + Findings Table; but still no ≥3 findings rule |
| C-08 Remediation guidance | PASS | Remediation is required schema field; "not 'fix the spec' but the specific change" with named target rule |
| C-09 Cross-skill patterns | PASS | Cross-Skill Patterns required in synthesis; root-cause distinction explicitly drawn |
| C-10 Blast radius rationale | PASS | BR rationale built into finding schema itself (required for cross-skill and system-wide), not only in ranked section |

**V-04 composite: 60 + (10+5+10) + (5+5) = 95**

---

### V-05 (Combined: Phrasing Register + Blast Radius Prominence)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All five invoked | PASS | Checks numbered 1–5; Simulation Coverage Log at end confirms all five ran |
| C-02 Sequential order | PASS | Checks defined 1–5; Coverage Log confirms execution order (ranked output is synthesis, not reordering) |
| C-03 Unified report | PASS | Ranked Findings Report as primary artifact; single file output |
| C-04 Blast radius sort | PASS | Organizing principle from sentence one; four-tier system explicit throughout |
| C-05 Spec anchoring | PASS | "Spec Location: required; must name a specific spec section... not 'the spec is unclear'" |
| C-06 Source+Location+Impact | PARTIAL | Check (source) and Spec Location are required; "What is wrong" combines problem + impact into one field without explicit impact label; no standalone Impact column |
| C-07 Coverage breadth | PARTIAL | Coverage Log requires all 5; blast-radius-first framing actively risks authors skipping low-blast sub-skills (hypothesis-stated risk) |
| C-08 Remediation guidance | PASS | "name the target and describe the specific change -- not 'fix the spec' but the exact addition" |
| C-09 Cross-skill patterns | PASS | COMPOUNDING FINDINGS section required with structured block format; elevation rule ("Promoted to:") adds precision |
| C-10 Blast radius rationale | PASS | "Why this scope" is a required column for system-wide and cross-skill; Compounding Findings block has Rationale field |

**V-05 composite: 60 + (5+5+10) + (5+5) = 90**

---

## Ranking Summary

| Rank | Variation | Score | All Essential Pass | Notes |
|------|-----------|-------|--------------------|-------|
| 1 (tie) | V-01 | 95 | Yes | Clearest table-driven enforcement; schema defined before execution |
| 1 (tie) | V-03 | 95 | Yes | Strongest spec-anchoring language; best remediation exemplar |
| 1 (tie) | V-04 | 95 | Yes | Most complete rubric coverage; BR rationale in schema not just ranking |
| 4 (tie) | V-02 | 90 | Yes | Phase protocol is strong; remediation enforcement weaker |
| 4 (tie) | V-05 | 90 | Yes | Best C-04/C-10; blast-radius framing risks C-07 breadth |

---

## Excellence Signals

From the three co-leading variations (V-01, V-03, V-04), the patterns that made the difference:

1. **Schema-first definition** (V-01, V-04): Defining the mandatory finding schema before any execution instruction begins forces authors to write findings *into* the schema as they go, rather than retrofitting format after the fact. When schema follows execution instructions, authors treat it as optional.

2. **Failure rules on required fields** (V-01, V-04): Stating what makes a field FAIL ("the spec is unclear" fails this field; "fix the spec" fails remediation) is more powerful than stating what makes a field pass. Negative rules are harder to misread.

3. **BR rationale at finding level, not just ranking level** (V-04): Requiring blast radius rationale inside the finding schema itself (not only in the ranked-findings section) ensures rationale survives even when synthesis sections are produced carelessly.

4. **Gate-check framing for spec anchoring** (V-03): Casting the campaign as "before you write code, prove the spec holds" makes spec anchoring structurally natural — pointing to a spec section is the only way to prove the spec failed. This is a framing-as-enforcement pattern.

5. **Compounding empty-state rule** (V-01, V-03, V-04): Requiring an explicit "No cross-skill patterns detected" when none exist (rather than allowing omission) closes the silent-skip failure mode for C-09 without burdening the author when there are genuinely no patterns.

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["schema-first definition: mandatory finding schema defined before execution instructions forces authors to write findings into schema as they go, not retrofit format after the fact", "failure-rule enforcement: stating what makes a required field FAIL drives more reliable compliance than stating what makes it pass", "BR rationale at finding level: requiring blast radius rationale in the finding schema itself (not only in the ranked section) ensures rationale is captured even when synthesis is produced carelessly"]}
```
