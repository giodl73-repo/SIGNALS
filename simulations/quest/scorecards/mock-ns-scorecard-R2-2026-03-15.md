## /quest:score — mock-ns Round 2 Scoring

---

### Evaluation Matrix

#### C-01 through C-05 (Essential)

All five variations carry the complete 7-field header block, correct category table, skill-specific mock body spec, proper flag field, and `{namespace}`-based artifact path. All pass all essential criteria.

---

#### Per-Variation Detail

**V-01 — Flag-First Sequencing**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | 7-field header block with Flag: field specified |
| C-02 | PASS | Category table complete and canonical |
| C-03 | PASS | Step 8 specifies skill-specific headings, tables, gates |
| C-04 | PASS | Flag: in header references FLAG from Step 4 |
| C-05 | PASS | `{namespace}` in path, skill-id excluded, YYYY-MM-DD |
| C-06 | PASS | topic → topic-plan; Exclusion note column present |
| C-07 | PASS | Full HIGH-STRUCTURE warning with "REAL-REQUIRED at Tier 2+" |
| C-08 | PASS | Step 9 specifies next-step line |
| C-09 | PASS | Step 4 critical-namespace branch includes Tier 2+ qualifier |
| C-10 | PASS | Step 1 dedicated emit: `> TOPICS.md: {result}` |
| C-11 | PASS | Step 4 titled "Compute FLAG"; emits `> FLAG: {value}`; "do not modify FLAG after this point"; Step 6 "Do not re-derive" |
| C-12 | PASS | Exclusion note column in default table; "Do NOT use topic-status -- excluded as meta-structural" inline |
| C-13 | FAIL | Step 7 writes warning "immediately after header block" with no named section, no `---` delimiters |

**Essential 5/5 = 60 | Recommended 3/3 = 30 | Aspirational 4/5 = 8 → Total: 98**

---

**V-02 — Warning-Led Body**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "All seven fields required. No omissions. No reordering." |
| C-02 | PASS | Category table complete |
| C-03 | PASS | Section 3 specifies skill-specific headings and elements |
| C-04 | PASS | Flag: {flag} in header block; flag resolved in setup |
| C-05 | PASS | `{namespace}` in path, YYYY-MM-DD |
| C-06 | PASS | `topic -> topic-plan [NOT topic-status -- excluded as meta-structural]` |
| C-07 | PASS | Full HIGH-STRUCTURE warning in FIDELITY CONTEXT section |
| C-08 | PASS | Closing line is next-step invocation |
| C-09 | PASS | Flag table includes critical-namespace row with Tier 2+ |
| C-10 | PASS | Setup emits dedicated `> TOPICS.md: {result}` line |
| C-11 | FAIL | Flag determined via setup table; no named FLAG variable, no `> FLAG:` emit, no "do not rederive" reference in header section |
| C-12 | PASS | `[NOT topic-status -- excluded as meta-structural]` inline on same line as default; "NOT" + "excluded" meet language threshold |
| C-13 | PASS | `## FIDELITY CONTEXT` is Section 2, flanked by `---` delimiters, before mock body |

**Essential 5/5 = 60 | Recommended 3/3 = 30 | Aspirational 4/5 = 8 → Total: 98**

---

**V-03 — Inline Exclusion Row**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | 7-field header; Step 6 lists all fields |
| C-02 | PASS | Category table complete |
| C-03 | PASS | Step 8 specifies skill-specific golden structure |
| C-04 | PASS | Flag: {FLAG from Step 4}; "copy it exactly, do not rederive" |
| C-05 | PASS | `{namespace}` in path |
| C-06 | PASS | topic → topic-plan; Exclusion column enforced |
| C-07 | PASS | HIGH-STRUCTURE warning includes "REAL-REQUIRED at Tier 2+" |
| C-08 | PASS | Step 9 next-step line |
| C-09 | PASS | Step 4 flag table includes critical-namespace branch |
| C-10 | PASS | Step 1 dedicated TOPICS.md emit |
| C-11 | PASS | Step 4 titled "Compute the flag"; "Do not defer. Do not compute it again during header assembly."; emits `> FLAG:`; Step 6 "FLAG emitted in Step 4 -- copy it exactly" |
| C-12 | PASS | Three-column table; Exclusion column with "Do NOT use topic-status. It is excluded as meta-structural..."; "Exclusion column contains hard constraints" |
| C-13 | FAIL | Step 7 writes warning after header with no `---` delimiters and no section header; not a structural lead section |

**Essential 5/5 = 60 | Recommended 3/3 = 30 | Aspirational 4/5 = 8 → Total: 98**

---

**V-04 — Flag-First + Warning-Led Body**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | A-1 header block; all 7 fields; "No fields may be omitted" |
| C-02 | PASS | S-3 category table complete |
| C-03 | PASS | A-3 specifies skill-specific headings, tables, gates, role cards |
| C-04 | PASS | A-1: "Flag: {FLAG from S-4}"; "Copy FLAG from S-4 verbatim. Do not rederive." |
| C-05 | PASS | S-5 declares path with `{namespace}` |
| C-06 | PASS | S-2 table; topic → topic-plan; Exclusion column "Do NOT use topic-status" |
| C-07 | PASS | A-2 FIDELITY CONTEXT contains full HIGH-STRUCTURE warning with Tier 2+ qualifier |
| C-08 | PASS | A-4 closing line |
| C-09 | PASS | S-4 critical-namespace branch: `FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| C-10 | PASS | S-1 dedicated emit: `> TOPICS.md: {found -- topic {topic}, tier: {N}...}` |
| C-11 | PASS | S-4 "Compute FLAG" resolves to named variable; emits `> FLAG:`; "FLAG is now resolved. Do not re-evaluate or modify it after this emit."; A-1 "Copy FLAG from S-4 verbatim. Do not rederive." |
| C-12 | PASS | S-2 inline Exclusion column; "Do NOT use topic-status -- excluded as meta-structural" |
| C-13 | PASS | A-2 is `## FIDELITY CONTEXT` with `---` delimiters on both sides, positioned as first body section before A-3 |

**Essential 5/5 = 60 | Recommended 3/3 = 30 | Aspirational 5/5 = 10 → Total: 100**

---

**V-05 — Inline Exclusion + Inertia Framing**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | 7-field header; Step 6 lists all fields |
| C-02 | PASS | Category table complete |
| C-03 | PASS | Step 8 specifies skill-specific golden structure |
| C-04 | PASS | Flag: {FLAG from Step 4}; "Copy FLAG from Step 4 verbatim" |
| C-05 | PASS | `{namespace}` in path, YYYY-MM-DD |
| C-06 | PASS | topic → topic-plan; Exclusion column enforced as hard constraint |
| C-07 | PASS | HIGH-STRUCTURE warning includes "REAL-REQUIRED at Tier 2+ for critical namespaces" — inertia framing completes the Tier 2+ cost explanation that was truncated in R1 |
| C-08 | PASS | Step 9 next-step line |
| C-09 | PASS | Step 4 flag table includes critical-namespace branch |
| C-10 | PASS | Step 1 dedicated TOPICS.md emit |
| C-11 | PASS | Step 4 "Compute FLAG" discrete step; "Compute now. Do not defer."; emits `> FLAG:`; Step 6 "Flag: {FLAG from Step 4}" references by name |
| C-12 | PASS | Exclusion column with inertia cost: "Substituting topic-status for topic-plan means the mock run generates no forward readiness signal, defeating the purpose of /mock:ns" — strongest C-12 language |
| C-13 | PARTIAL | `---` delimiters present before and after each warning variant; warning positioned between header and mock body; but no named `## FIDELITY CONTEXT` section header — satisfies delimiter separation but not "first section" identity |

**Essential 5/5 = 60 | Recommended 3/3 = 30 | Aspirational 4.5/5 = 9 → Total: 99**

---

### Score Summary

| V | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Composite |
|---|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|
| V-01 | P | P | P | P | P | P | P | P | P | P | **P** | P | F | **98** |
| V-02 | P | P | P | P | P | P | P | P | P | P | F | P | **P** | **98** |
| V-03 | P | P | P | P | P | P | P | P | P | P | **P** | **P** | F | **98** |
| V-04 | P | P | P | P | P | P | P | P | P | P | **P** | P | **P** | **100** |
| V-05 | P | P | P | P | P | P | P | P | P | P | **P** | **P** | ~P | **99** |

**Rank: V-04 (100) > V-05 (99) > V-01 = V-02 = V-03 (98)**

All variations achieve Gold band. All essential criteria pass across all variations.

---

### Excellence Signals — V-04

**1. Phase-separated procedure (SETUP PHASE / ARTIFACT PHASE)**
Naming the two phases explicitly — before writing and after writing begins — makes the sequencing constraint structural rather than instructional. Any step in SETUP PHASE is computation; any step in ARTIFACT PHASE is output. FLAG cannot be computed during artifact construction because it lives in a different phase. This is stronger than "do this before that" because it changes where the model is in the procedure, not just when.

**2. Post-emit finality lock: "FLAG is now resolved. Do not re-evaluate or modify it after this emit."**
The emit is a gate, not a logging step. The sentence after the emit converts the named variable into a temporal invariant. V-01 and V-03 say "do not rederive" only at the header step; V-04 says it at the compute step, which is the earliest and strongest enforcement point.

**3. Artifact section manifest declared before section content**
"The artifact has three sections, in order: HEADER, FIDELITY CONTEXT, MOCK BODY." — the order is stated as a manifest before any section is described. Each section is then defined in that order. This makes section sequence a structural property of the artifact spec, not an incidental ordering of the instruction blocks.

**4. "Copy FLAG from S-4 verbatim. Do not rederive." at header assembly**
The double guard — finality at emit (S-4) and prohibition at use (A-1) — closes both ends of the recomputation window. V-03 only closes the use end.

---

### Round 3 Candidate

V-04 achieves 100/100 — all 13 criteria pass. The three single-axis variations (V-01, V-02, V-03) each pass 12/13. V-04 is the direct combination of V-01 and V-02's axes, with V-03's exclusion table carried implicitly (S-2 already has the inline Exclusion column).

If R3 is run, it should either: (a) validate V-04 as the final form by running it against a new topic/namespace pair and scoring the actual output, or (b) identify whether V-04's finality language is sufficient to prevent recomputation under adversarial conditions (long context, competing instructions).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-separated procedure (SETUP PHASE / ARTIFACT PHASE) enforces computation-before-output as a structural invariant rather than a sequential instruction", "Post-emit finality lock at the compute step — not at the use step — is the strongest guard against FLAG recomputation", "Artifact section manifest declared upfront before section definitions makes section ordering a structural property of the spec"]}
```
