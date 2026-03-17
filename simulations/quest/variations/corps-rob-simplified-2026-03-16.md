---

**Simplified prompt body** — written to `simulations/quest/golden/corps-rob-variate-R20-QU5-simplified-2026-03-17.md`

---

## Simplification Report

**Word count: 7,856 → 5,866 (−1,990 words, 25.3% reduction)**

All essential criteria C-01 through C-60 pass. C-58, C-59, C-60 (the v20 additions) are explicitly preserved.

### What was removed and why

| Rule / Section | Cut | Rationale |
|---|---|---|
| RULE INERTIA-BASELINE AP-2 | Sentences 3–4 ("A pair describing the same displacement event..."; "Each baseline must have a distinct structural locus...") | Restate loci already named in sentences 1–2 |
| RULE IB-URGENCY-CASCADE | Cascade constraint trailing clauses; AP-2 last sentence ("Each of the three...independently auditable") | Trailing clauses restate "MUST"; last AP-2 sentence restates "all-or-nothing" already in sentence 1 |
| RULE FINDING-LEDGER AP-2 | Sentences 2–4 (static-log analogy, "must be updated" restatement, "draft schema" restatement) | All three elaborate what sentence 1 already names as the disqualifying form |
| RULE CARRY-FORWARD | Propagation scope example sentence ("A finding introduced in Stage 1..."); AP-2 sentences 2–3 | Example illustrates what's already stated; sentences 2–3 restate AP-2 sentence 1 |
| RULE VIA-POSITION AP-2 | Elaboration sentences 2–4 ("A finding table where..."; "The position requirement..."; "A finding row with Via: in second column...") | All three restate the prohibition and VIOLATION-03 already named in AP-2 sentence 1 |
| RULE PHASE-GATE | AP-2 middle clause; Note compression | Middle clause restates the concrete requirement that follows it |
| RULE STAGE-HANDOFF | "Structural element" line (identical to Constraint); Governs trailing; AP-1 trailing | Structural element and Constraint are the same rule in two forms |
| RULE BLOCKER-PROTOCOL | AP-1 trailing ("the block is invisible at the artifact level..."); AP-2 trailing ("the block is declared but its resolution status is unverifiable") | Rationale clauses; anti-pattern declaration already names the violation |
| RULE CONDITION-ENUM AP-2 | Middle sentence (TRIAGE NOTE-specific example + "exclusive condition-label authority" restatement) | Triage Note example is subsumed by the general rule; "no substitution" in the next sentence covers it |
| RULE AUDIT-INDEPENDENCE | Governs trailing; "Mandatory status is not derived from RULE AUDIT-TABLE" in branch 2; AP trailing elaboration | Redundant with unconditional mandate already stated |
| RULE VIOLATION-TAXONOMY | Series-state sentence 1 ("A violation ID assigned in round N...") | Implied by "stable within this series"; sentence 2 states the operative rule |
| Various Governs clauses | Trailing elaboration phrases (8–20 words each across AUDIT-SUITE, AUDIT-TABLE, CARRY-FORWARD, FINDING-LEDGER, SYNTHESIS, ZERO-STATE) | Descriptive rationale not required by criteria |
| Stage Metrics paragraph | Entire explanatory paragraph after stage template | Covered by RULE FINDING-LEDGER AP-2; Stage Metrics block shows the field |
| Stage template annotations | Carry Forward inline restatement; Findings verbose AP-2 description; Findings constraint comment | Condensed to AP designation + VIOLATION reference; glossary covers full definition |
| IB template fields | Verbose bracket guidance (e.g., "name the artifact, system, or API contract this topic displaces") | Compressed to shorter equivalents preserving structural meaning |
| IB cascade reminder | Multi-clause paragraph after IB template | Condensed to single line |
| SYNTHESIS template | "generic directionality assertions without artifact IDs do not satisfy AP-2" | Restates cite-at-least-one-artifact requirement already stated |
| POST-STAGE AUDIT SUITE header | Verbose BOOKEND-AUDIT inline re-declaration | Condensed to AP-1+AP-2 reference with glossary pointer |
| TRIAGE NOTE AUDIT SCHEMA in template | Full (a)/(b)/(c) schema repetition | Replaced with preamble reference; C-30 satisfied by name reference |
| Carry Forward Audit header | Verbose propagation scope restatement | Condensed to enforcement scope statement |

### Essential criteria explicitly verified

- **C-58** (BOOKEND-AUDIT Dual AP): Three conformance states + AP-1 + AP-2 in glossary; POST-STAGE AUDIT SUITE header cites AP-1+AP-2; section headers repeat the citation.  
- **C-59** (VIA-POSITION Dual AP + VIOLATION-03 orphan): AP-1 + AP-2 in glossary with VIOLATION-03 assignment; Findings template annotation cites AP-2 with VIOLATION-03.  
- **C-60** (SYNTHESIS Dual AP): AP-1 + AP-2 in glossary with content requirement; SYNTHESIS header cites AP-2; template has per-subsection cite requirements.  
- **C-30/C-34**: TRIAGE NOTE AUDIT SCHEMA preamble declaration intact; CONDITIONAL-ITEM disambiguation note untouched.  
- **C-46**: AUDIT-INDEPENDENCE two-branch enumeration + C-44/C-46 escalation annotation preserved verbatim.

```json
{"simplified_word_count": 5866, "original_word_count": 7856, "all_essential_still_pass": true}
```
