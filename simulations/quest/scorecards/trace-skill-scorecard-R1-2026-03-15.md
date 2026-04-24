## trace-skill — Round 1 Scoring

Rubric: v1 | Variations: V-01, V-02, V-03 (truncated)

---

### V-01 — Axis: Role Sequence

| Criterion | ID | Result | Evidence |
|-----------|-----|--------|----------|
| Four phases present in sequence | C-01 | PASS | Phase 1–4 headers present in order |
| Gather enumerates all inputs by name with source | C-02 | PASS | Three explicit input categories (spec / invocation / context), each with source field |
| Bind maps every input to resolved value | C-03 | PASS | Bind table requires name + source + resolved value; "No ranges, no ambiguity" |
| Execute produces artifact with correct naming/sections | C-04 | PASS | `{topic}-{signal}-{date}.md` naming stated; "no elision markers" enforced |
| Verdict declares PASS/FAIL with rationale | C-05 | PASS | Explicit "Overall: PASS / FAIL" row with evidence column |
| Phases carry exact schema labels | C-06 | PASS | "Phase 1: Gather", "Phase 2: Bind", "Phase 3: Execute", "Phase 4: Verdict" — exact |
| Verdict cites criterion IDs | C-07 | PASS | Verdict table enumerates C-01 through C-10 by ID |
| Artifact complete — no elision markers | C-08 | PASS | Explicitly forbidden: `[...], etc.` and placeholders |
| Gather includes Coverage Matrix with closed-world preamble | C-09 | PASS | Full Coverage Matrix table with "Closed-world assumption" preamble; BLOCKED halt if Gap=YES |
| Execute relays carry (role, signal, binding, status) evidence fields | C-10 | FAIL | Artifact delimiter markers present; carry evidence fields not explicitly named |

**Essential (C-01–C-05)**: 5/5 PASS → 60 pts  
**Recommended (C-06–C-08)**: 3/3 PASS → 30 pts  
**Aspirational (C-09–C-10)**: 1/2 PASS → 5 pts  
**Composite**: **95/100** — **PASS**

---

### V-02 — Axis: Output Format

| Criterion | ID | Result | Evidence |
|-----------|-----|--------|----------|
| Four phases present in sequence | C-01 | PASS | "Phase 1 — Gather" through "Phase 4 — Verdict" headers in order |
| Gather enumerates all inputs by name with source | C-02 | PASS | `**{name}** ({type}, required|optional): desc — sourced from {spec|invocation|context}` |
| Bind maps every input to resolved value | C-03 | PASS | `{name} = {exact value}` block; "Every name from Gather must appear here. No exceptions." |
| Execute produces artifact with correct naming/sections | C-04 | PASS | Naming convention stated; "No ellipsis, no '[content omitted]'" |
| Verdict declares PASS/FAIL with rationale | C-05 | PASS | "Close with a single line: PASS or FAIL, and one sentence stating why" |
| Phases carry exact schema labels | C-06 | PASS | All four phase labels present with em-dash separator format |
| Verdict cites criterion IDs | C-07 | PASS | Verdict lists `- **C-01** (four phases):` through C-10 explicitly |
| Artifact complete — no elision markers | C-08 | PASS | Explicit prohibition with three specific examples |
| Gather includes Coverage Matrix with closed-world preamble | C-09 | FAIL | Closed-world statement required ("in your own words") but no Coverage Matrix table |
| Execute relays carry evidence fields | C-10 | FAIL | Carry evidence fields not mentioned |

**Essential (C-01–C-05)**: 5/5 PASS → 60 pts  
**Recommended (C-06–C-08)**: 3/3 PASS → 30 pts  
**Aspirational (C-09–C-10)**: 0/2 PASS → 0 pts  
**Composite**: **90/100** — **PASS**

---

### V-03 — Axis: Lifecycle Emphasis

**Status: TRUNCATED** — prompt ends partway through Phase 1 Gather definition. Only the Gather gate framing and "No trace artifact available" note are visible. Phases 2–4, Bind/Execute/Verdict, and all completion criteria cannot be evaluated.

| Criterion | ID | Result | Evidence |
|-----------|-----|--------|----------|
| Four phases present in sequence | C-01 | FAIL | Only Phase 1 header defined; remaining phases absent |
| Gather enumerates all inputs by name with source | C-02 | INDETERMINATE | Gather setup visible but enumeration instructions cut off |
| Bind maps every input | C-03 | FAIL | Bind phase absent |
| Execute produces artifact | C-04 | FAIL | Execute phase absent |
| Verdict declares PASS/FAIL | C-05 | FAIL | Verdict phase absent |
| C-06–C-10 | — | FAIL | Not present in truncated fragment |

**Essential**: 0/5 → **CANNOT PASS** (prompt incomplete; cannot be used as-is)

---

### Rankings

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | V-01 | 95/100 | PASS | Only missing explicit carry field names in Execute |
| 2 | V-02 | 90/100 | PASS | Missing Coverage Matrix table (has prose substitute only) |
| 3 | V-03 | — | FAIL | Truncated; unusable |

**Excellence Signals from V-01:**

1. **Spec-first enumeration** — processing spec inputs before invocation inputs creates a reference frame before constraints are applied; this ordering prevents invocation values from prematurely narrowing the input space
2. **BLOCKED gate mechanism** — the explicit halt declaration (`Any Gap = YES → BLOCKED`) converts a soft warning into a hard gate; the trace either proceeds or stops, no ambiguous partial runs
3. **Artifact delimiter markers** — `[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]` frames the artifact as a discrete extractable unit, making post-trace artifact isolation unambiguous

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["spec-first enumeration: process spec inputs before invocation inputs to anchor the input space before constraints apply", "BLOCKED gate: explicit halt with BLOCKED declaration when Coverage Matrix shows any Gap=YES", "artifact delimiter markers: [ARTIFACT BEGINS HERE]/[ARTIFACT ENDS HERE] frames artifact as discrete extractable unit"]}
```
