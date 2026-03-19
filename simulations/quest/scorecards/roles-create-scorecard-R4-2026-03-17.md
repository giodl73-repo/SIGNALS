Now I have all 5 variations fully read. Let me score them.

---

# roles-create R4 — Scorecard (Rubric v3)

## Scoring Summary

| Criterion | Category | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|--------|------|------|------|------|------|
| C-01 Role file path | essential | 60/5 | PASS | PASS | PASS | PASS | PASS |
| C-02 All frontmatter fields | essential | 60/5 | PASS | PASS | PASS | PASS | PASS |
| C-03 Mode detection | essential | 60/5 | PASS | PASS | PASS | PASS | PASS |
| C-04 Domain-specific content | essential | 60/5 | PASS | PASS | PASS | PASS | PASS |
| C-05 Inertia-advocate surfaced | essential | 60/5 | PASS | PASS | PASS | PASS | PASS |
| C-06 Sharp verify items | recommended | 30/2 | PASS | PASS | PASS | PASS | PASS |
| C-07 Domain specializations table | recommended | 30/2 | PASS | PASS | PASS | PASS | PASS |
| C-08 Archetype calibrated | aspirational | 10/7 | PASS | PASS | PASS | PASS | PASS |
| C-09 Orientation register | aspirational | 10/7 | PASS | PASS | PASS | PASS | PASS |
| C-10 Domain column headers | aspirational | 10/7 | PASS | PASS | PASS | PASS | PASS |
| C-11 Inertia-advocate generated | aspirational | 10/7 | PASS | PASS | PASS | PASS | PASS |
| C-12 Interactive mode holds | aspirational | 10/7 | PASS | PASS | PASS | PASS | PASS |
| C-13 Pre-write self-certification | aspirational | 10/7 | PASS | PASS | PASS | PASS | PASS |
| C-14 Malformed-input routing | aspirational | 10/7 | PASS | PASS | PASS | PASS | PASS |

---

## Evidence Notes by Criterion

### Essential

**C-01** — All variations write to `.craft/roles/{area}/{subrole}.md` in the final write phase. Phase 6 in every variation explicitly states both the inertia-advocate path and the main role path. Audit item [A] in every variation confirms path before write.

**C-02** — All variations include a 12-field frontmatter template (name, version, archetype, orientation.frame/serves, lens.verify/simplify, expertise.depth/relevance, scope, collaborates_with, artifacts, workflow). Audit item [B] in every variation checks all fields by name.

**C-03** — All variations have Phase 0 (pre-detection) + Phase 1 (mode routing). Phase 0 handles malformed inputs before they reach Phase 1's clean three-way branch. NAME-ONLY, DESCRIPTION, INTERACTIVE each route to distinct generation paths. No variation silently cross-routes.

**C-04** — Phase 3 in every variation instructs "No placeholder text in the written output" / "Every field must be replaced with content specific to the {subrole} domain." Field-register rules (first-person observational, specific beneficiary, boolean verify checks) enforce domain specificity. Audit [C][D][E] check this explicitly.

**C-05** — Phase 2 in all variations checks whether `.craft/roles/{area}/inertia-advocate.md` exists, and if absent, generates a complete companion file with full frontmatter and body table. This exceeds the minimum (suggestion); satisfies C-05 by doing more.

### Recommended

**C-06** — Phase 3 in all variations specifies "Boolean check naming a specific artifact, state, or config — answerable yes/no — min 4 items." V-02 adds a FAIL/PASS column table with concrete examples ("Is the audit log retention period set to ≥ 6 years..."). Audit item [E] enforces this in all variations.

**C-07** — Phase 4 in all variations requires a `## {Subrole} Domain` section with a domain specializations table, minimum 3 rows. FAIL/PASS header examples are given in every variation (V-05 lifts these into CONTRACT: COLUMN-HEADER).

### Aspirational

**C-08** — All variations instruct "check existing roles in `{area}`; use their archetype value — `craft` for technical/builder areas, `process` for governance/ops areas; do not apply without checking." V-05 CONTRACT: FIELD-REGISTER reinforces this pattern.

**C-09** — All variations specify FIRST-PERSON OBSERVATIONAL for `orientation.frame` and THIRD-PERSON RECIPIENT with named beneficiary for `orientation.serves`. Audit items [C] and [D] enforce register compliance. V-05's FIELD-REGISTER contract gives the clearest anti-pattern examples.

**C-10** — All variations include explicit FAIL/PASS column header examples (Component/Purpose/Notes = FAIL; Regulation/Scope/Enforcement Body = PASS, etc.). Audit item [F] enforces domain vocabulary before write.

**C-11** — All variations generate a complete inertia-advocate companion file when absent — not a suggestion. Template includes all 12 fields and a body table. Audit item [H] verifies no literal `{area}` remains. PASS (as opposed to mere C-05 suggestion).

**C-12** — All variations include three explicit categorical prohibitions for interactive mode: (1) do not generate content after one or two answers, (2) do not produce draft/stub mid-conversation, (3) proceed only when all three answers confirmed. V-02 adds table-cell enforcement (all three rows must be filled). V-03/V-04/V-05 label these "categorical prohibitions, not preferences."

**C-13** — All variations include a structured YES/NO self-audit between generation (Phase 4) and file write (Phase 6):
- V-01: Phase 5 prose checklist (8 items A–H)
- V-02: Phase 5 table with YES/NO cells (8 rows)
- V-03: Distributed gates across phases (Gates 0, 1, 2a/b, 3a–3e, 4a–4c) + Phase 5 final confirmation
- V-04: Guard 1 pre-declared obligations + Phase 5 execution of declared checklist
- V-05: CONTRACT: AUDIT-CHECKLIST invoked by Phase 5; "The file written to disk is always the post-audit version"

**C-14** — All variations include a Phase 0 (or Guard 0) that classifies malformed inputs before mode detection. All four malformed cases covered: BARE AREA (ask which subrole), EXTRA COLONS (use first two tokens, notify), VAGUE PHRASE (ask for clarification), EMPTY (route to INTERACTIVE). Clean inputs pass through. Gate 0 (V-03) and audit item [G] (all others) confirm the routing was completed.

---

## Scoring Worksheets

**V-01: Minimal-Delta**
```
Essential:    5 / 5  =>  5 * 60 / 5  = 60
Recommended:  2 / 2  =>  2 * 30 / 2  = 30
Aspirational: 7 / 7  =>  7 * 10 / 7  = 10
Composite: 100   Golden: YES
```

**V-02: Checklist-Format**
```
Essential:    5 / 5  =>  60
Recommended:  2 / 2  =>  30
Aspirational: 7 / 7  =>  10
Composite: 100   Golden: YES
```

**V-03: Distributed-Audit**
```
Essential:    5 / 5  =>  60
Recommended:  2 / 2  =>  30
Aspirational: 7 / 7  =>  10
Composite: 100   Golden: YES
```

**V-04: Front-Loaded-Guard**
```
Essential:    5 / 5  =>  60
Recommended:  2 / 2  =>  30
Aspirational: 7 / 7  =>  10
Composite: 100   Golden: YES
```

**V-05: Full-Integration**
```
Essential:    5 / 5  =>  60
Recommended:  2 / 2  =>  30
Aspirational: 7 / 7  =>  10
Composite: 100   Golden: YES
```

---

## Final Rankings

| Rank | Variation | Score | Band | Differentiator |
|------|-----------|-------|------|----------------|
| T-1 | V-01 Minimal-Delta | 100 | Golden | Smallest surface area; mechanics alone load-bear |
| T-1 | V-02 Checklist-Format | 100 | Golden | Table-cell enforcement; skipping leaves visible gap |
| T-1 | V-03 Distributed-Audit | 100 | Golden | Phase-local gates; failures caught at point of occurrence |
| T-1 | V-04 Front-Loaded-Guard | 100 | Golden | Pre-commitment declaration before first content token |
| T-1 | V-05 Full-Integration | 100 | Golden | Single-source contracts; cleanest compositional structure |

**R4 goal achieved**: all 5 variations score 100 on v3. The rubric hypothesis that grafting Phase 0 + Phase 5 onto any well-structured R3 skeleton suffices to satisfy C-13 and C-14 is confirmed.

---

## Excellence Signals

**Signal from V-04: Pre-commitment architecture**
Declaring all audit obligations *before* any content generation forces the model to see its full responsibility before the first token. The execution phase becomes fill-in, not discovery. This prevents the failure mode where the model "forgets" an audit obligation under generation pressure — because the obligation was stated as a named list that must be satisfied, not as a tail instruction that can be deprioritized.

**Signal from V-03: Distributed-gate enforcement**
Spreading audit checks across phases — each phase certifying its own outputs before the next begins — catches errors at the phase where they arise, not deferred to a single batch. Gate 3b (orientation.frame register) fails at the end of Phase 3, not at the end of Phase 5, so the fix is local and immediate. This architecture also reduces the risk of a single-block audit being skipped under token pressure.

**Signal from V-05: Separation-of-Contracts**
Naming every constraint once, in an authoritative contracts section, and making phases thin referencing lines eliminates rule repetition and provides a single place to update. The two new contracts (INPUT-ROUTING-RULES, AUDIT-CHECKLIST) slot cleanly into the existing architecture. The categorical-prohibitions framing is preserved in CONTRACT: INTERACTIVE-HOLD without leaking into the execution phases.

**Signal from V-02: Table-cell enforcement**
Using markdown tables for both the Phase 0 classification and Phase 5 audit transforms each check into a visible cell. A model that fills in all cells must engage with each item; a model that skips a row leaves an obvious structural gap. The format provides external evidence of the audit step without requiring prose.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-commitment-architecture: declare all audit obligations before first content token so execution phases are fill-in not discovery", "distributed-gate-enforcement: certify each phase outputs before proceeding so failures are caught at point of occurrence not deferred to batch audit"]}
```
