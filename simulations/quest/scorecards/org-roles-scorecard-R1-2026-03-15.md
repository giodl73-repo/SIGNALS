---

## Round 1 Scorecard — org-roles

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-01 Context-first sequence | 5/5 | 2.5/3 | 0.5/2 | **87.5** | YES |

*V-02 through V-05 not provided in Round 1.*

---

### V-01 Criterion Breakdown

| ID | Result | Key Evidence |
|----|--------|--------------|
| C-01 | PASS* | All 6 fields + sub-fields present. *Risk: uses `verify`/`simplify` instead of rubric-spec `verify_questions`/`simplify_rules` — downstream skills reading by exact field name will miss content. |
| C-02 | PASS | Step 4 dedicated to `inertia-advocate`. Frame: "argues the case for doing nothing." Simplify: "burden of proof is on the feature." Unambiguous status-quo framing. |
| C-03 | PASS | Step 3: "always emitted regardless of domain." All three stock roles fully specified. |
| C-04 | PASS | Output path `.roles/{area}/` stated in opening line. Individual `.md` files named per-step. |
| C-05 | PASS | Steps 1-2 entirely devoted to context derivation. Domain expert `frame` must "reference the specific domain concern identified in Step 1." 2-4 domain experts mandated. |
| C-06 | PASS | Schema comment: "Must be a different statement from frame, not a paraphrase." Stock examples demonstrate clean separation. |
| C-07 | PASS* | Verify annotated "answerable by reading artifacts or running code"; simplify annotated "not a description; an opinion with consequences." Same naming risk as C-01. |
| C-08 | PARTIAL | Stock role graph sound and closed. Domain expert `collaborates_with` is a placeholder — instruction-dependent. |
| C-09 | PARTIAL | Stock roles clearly differentiated. Domain expert uniqueness is instruction-only ("no other role would ask this" in schema comment). |
| C-10 | FAIL | Step 5 heading exists; content is undefined. Caller must inspect every file to reconstruct coverage. |

```
composite = (5/5 × 60) + (2.5/3 × 30) + (0.5/2 × 10)
          = 60 + 25 + 2.5
          = 87.5
```

**Score: 87.5 — GOLDEN** (all essential pass, composite ≥ 80)

---

### Excellence Signals

**E-1 — Context-first ordering prevents template anchoring.** Deriving domain experts before loading stock roles forces the LLM to name domain-specific concerns before it sees PM/Architect/Strategy. It cannot retroactively fill a generic template — it must derive from what it read.

**E-2 — Non-paraphrase constraint names the failure mode, not just the rule.** "Must be a different statement from frame, not a paraphrase" is more precise than "frame and serves must differ." Naming what to avoid is stronger than stating the positive.

**E-3 — Step 5 stub is a recurring C-10-class failure pattern.** Heading-only registry summary steps appear consistently across multiple skills in early rounds. The fix is always the same: define the format fields explicitly (area, count, stock vs. derived breakdown, coverage gaps).

---

**Recommended V-02 delta**: (1) fix `verify`→`verify_questions`, `simplify`→`simplify_rules` throughout schema; (2) define Step 5 content — area, total count, stock roles, domain expert names + derivation source, detected gaps; (3) pre-populate domain expert `collaborates_with` with stock role IDs as defaults.

```json
{"top_score": 87.5, "all_essential_pass": true, "new_patterns": ["Context-first ordering (derive domain experts before loading stock templates) prevents LLM from anchoring on generic archetypes — domain-specific concerns are named before PM/Architect/Strategy templates are loaded", "Explicit non-paraphrase instruction ('Must be a different statement from frame, not a paraphrase') names the exact failure mode rather than stating the positive requirement — more precise than 'frame and serves must differ'", "Registry summary defined by heading only (Step 5 stub) — naming the step without specifying its format is a recurring C-10-class failure pattern across multiple skills; fix by defining format fields explicitly"]}
```
 referenced roles exist in output set. Domain expert `collaborates_with` uses a placeholder (`{area}:{role-id}   # other roles in this registry only`) — correct constraint stated in comment, but actual entries are instruction-dependent. Model must select valid IDs from generated set without structural enforcement. |
| C-09 | Each role's lens differentiated — unique questions no other role would catch | PARTIAL | Schema comment for domain experts: "domain-specific; no other role would ask this." Stock roles are clearly differentiated: PM asks about inertia case and commitment threshold; Architect about complexity estimation and dependency risks; Strategy about defensive positioning and competitive signals; Inertia-advocate about switching cost and non-adopters. Domain expert differentiation is instruction-only — model may produce overlapping questions without structural reinforcement. |
| C-10 | Registry summary artifact — single-glance stock vs. derived audit | FAIL | Step 5 is titled "Write the registry summary" but its content is not defined — heading is a structural stub only. No format, fields, or required summary elements are specified. Caller cannot reconstruct coverage without inspecting every file. |

**Essential**: 5/5 | **Recommended**: 2.5/3 (C-08 partial) | **Aspirational**: 0.5/2 (C-09 partial, C-10 fail)

```
composite = (5/5 * 60) + (2.5/3 * 30) + (0.5/2 * 10)
          = 60 + 25 + 2.5
          = 87.5
```

**Score: 87.5 / 100 — GOLDEN** (all essential pass, composite >= 80)

---

## Round 1 Summary

Only V-01 was provided in Round 1. All essential criteria pass. Score of 87.5 lands in the Gold band.

**Primary finding — C-01/C-07 naming risk**: The schema uses `verify`/`simplify` while the rubric specifies `verify_questions`/`simplify_rules`. If downstream skills (org-review, org-chart) read role files by exact field name, they will fail to find content. This is a schema contract issue that will not surface in manual review — it requires tracing the read path across skills.

**Secondary finding — C-10 gap**: Step 5 (registry summary) is a heading-only stub. This is the clearest omission to fill in V-02.

**Tertiary finding — C-08 domain expert collaborates_with**: Instruction-dependent. V-02 should pre-populate stock role IDs as defaults in the domain expert template.

---

## Excellence Signals — Round 1

### E-1: Context-first ordering prevents template anchoring

V-01's decision to derive domain experts (Steps 1-2) before loading stock roles (Step 3) is the key structural bet. If the LLM names domain concerns before it sees "PM / Architect / Strategy," it cannot retroactively fill a generic template — it must derive from what it read. This is the correct design for C-05 compliance. Alternative orderings (stock-first) risk the model satisfying the letter of the domain expert requirement with a domain-labeled generic archetype.

### E-2: Explicit non-paraphrase constraint for orientation coherence

The schema comment "Must be a different statement from frame, not a paraphrase" names the exact failure mode rather than stating the positive requirement ("frame and serves must differ"). Naming what not to do is more precise. The stock role examples reinforce by demonstration, not instruction alone. This pattern generalizes to any schema with sibling fields that tend to collapse into restatements.

### E-3: Registry summary stub — a recurring C-10-class failure pattern

V-01 names Step 5 but does not define its contents. This same pattern appeared in early rounds of other skills (scout-feasibility Step 4, draft-spec closing section). Heading-only stubs are not documentation omissions — they are the primary mechanism by which C-10-class criteria fail. V-02 should define the registry summary format explicitly: area name, total role count, stock roles listed by name, domain expert names with derivation source, any coverage gaps detected in Step 1.

---

## Recommended Delta for V-02

1. **Fix schema naming**: `verify` -> `verify_questions`, `simplify` -> `simplify_rules` to match rubric spec and downstream read paths
2. **Define Step 5 content**: registry summary format — area, total count, stock roles named, domain experts named with derivation source, detected coverage gaps
3. **Anchor domain expert collaborates_with**: pre-populate with stock role IDs as defaults (e.g., `- {area}:pm`, `- {area}:inertia-advocate`); eliminates instruction-dependency for most common cross-role relationships

```json
{"top_score": 87.5, "all_essential_pass": true, "new_patterns": ["Context-first ordering (derive domain experts before loading stock templates) prevents LLM from anchoring on generic archetypes — domain-specific concerns are named before PM/Architect/Strategy templates are loaded", "Explicit non-paraphrase instruction ('Must be a different statement from frame, not a paraphrase') names the exact failure mode rather than stating the positive requirement — more precise than 'frame and serves must differ'", "Registry summary defined by heading only (Step 5 stub) — naming the step without specifying its format is a recurring C-10-class failure pattern across multiple skills; fix by defining format fields explicitly"]}
```
