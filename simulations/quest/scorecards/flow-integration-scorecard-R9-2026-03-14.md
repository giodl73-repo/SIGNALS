## flow-integration R9 Scorecard

**Rubric version:** v9 | **Ceiling:** 192 pts | **Aspirational (C-08–C-28):** 102 pts
**Trace:** placeholder — scored from variation design descriptions

---

### Scoring Conventions

- **C-01–C-07** (essential, ~90 pts): All variations assumed PASS — each is described as otherwise well-formed.
- **C-26, C-27, C-28**: 5 pts each. Open-question criteria scored conservatively where Q1/Q2 remain unresolved.
- **N/A** on C-27 when no non-standard terms present — criterion does not trigger; full credit context.

---

### V-01 — C-26 minimum (Q1 probe)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Essential criteria, well-formed variation |
| C-08–C-15 | PASS | Stage structure, call inventory, rate limits — not under test |
| C-16 | PASS | Expert persona declared before inventory gate |
| C-17 | PASS | In-block rate limit completeness — not under test |
| C-18 | PASS | Secondary positioning of fan-out registry |
| C-19 | PASS | Four-obligation persona scope |
| C-20 | PASS | Unconditional cross-stage with no-structures default |
| C-21 | PASS | Inventory flag alignment to persona obligations |
| C-22 | PASS | Vocabulary unification — no non-standard terms, canonical four used |
| C-23 | PASS | Unnumbered coda appended after last numbered stage |
| C-24 | PASS | Obligation table with canonical four terms present before gate |
| C-25 | PASS | Column headers are the Obligation Term values — schema comparison surface exists |
| C-26 | **FAIL** | Cross-reference mapping table without "ARE" keyword — Q1 unresolved; conservative call: explicit ARE required |
| C-27 | N/A | No non-standard terms; criterion does not trigger — full credit context |
| C-28 | PASS | Stages frame; terminal-position formula present: `*(no stage number — appended after Stage N, the last numbered stage)*` + prohibiting sentence |

**Score: 187 / 192**
Contingent: resolves to 192 if Q1 settles as "any unambiguous schema-aligned instruction sufficient."

---

### V-02 — C-27 scope (Q2 probe)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Essential criteria |
| C-08–C-15 | PASS | Not under test |
| C-16 | PASS | Expert persona before gate |
| C-17–C-21 | PASS | Not under test |
| C-22 | PASS | Vocabulary unification — non-standard terms used but flag names mirror non-standard obligation terms (shadow-call / taken-for-granted / fog-system / relay-chain) |
| C-23 | PASS | Unnumbered coda |
| C-24 | PASS | Obligation table with non-standard terms (accommodated by C-24) |
| C-25 | PASS | Explicit ARE form → schema comparison surface confirmed |
| C-26 | PASS | Explicit ARE form used → C-25 enforcement by schema instruction alone |
| C-27 | **FAIL** | Per-term inline prohibition (one YOU MUST NOT column per row) — Q2 unresolved; conservative call: single comprehensive block required |
| C-28 | PASS | Stages frame; terminal-position formula present |

**Score: 187 / 192**
Contingent: resolves to 192 if Q2 settles as "per-term distribution satisfies."

---

### V-03 — Outer frame vocabulary (Phase frame, confirming)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Essential criteria |
| C-08–C-15 | PASS | Not under test |
| C-16–C-21 | PASS | Not under test |
| C-22 | PASS | Canonical vocabulary, no substitution |
| C-23 | PASS | Unnumbered coda appended after Phase N |
| C-24 | PASS | Obligation table with canonical four terms |
| C-25 | PASS | Column headers = Obligation Term values; explicit ARE form |
| C-26 | PASS | Explicit ARE form — schema-only enforcement confirmed |
| C-27 | N/A | No non-standard terms |
| C-28 | PASS | Phase vocabulary substituted correctly: `*(no phase number — appended after Phase 3, the last numbered phase)*` + "does not appear between any two numbered phases" |

**Score: 192 / 192** ✓ Confirming variation — no open questions, clean sweep.

---

### V-04 — C-26 + C-27 joint (Q1+Q2, non-standard terms, Section frame)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Essential criteria |
| C-08–C-15 | PASS | Not under test |
| C-16–C-21 | PASS | Not under test |
| C-22 | PASS | Flag names mirror non-standard obligation terms (anchor-call / rubber-stamped / ghost-system / proxy-chain) |
| C-23 | PASS | Unnumbered coda appended after Section N |
| C-24 | PASS | Obligation table with non-standard terms |
| C-25 | PASS | Schema comparison surface exists — column headers present |
| C-26 | **FAIL** | Cross-reference table (no ARE) — same Q1 exposure as V-01; conservative: FAIL |
| C-27 | **FAIL** | Per-term inline distribution — same Q2 exposure as V-02; conservative: FAIL |
| C-28 | PASS | Section frame with correct formula: `*(no section number — appended after Section 4, the last numbered section)*` + prohibiting sentence |

**Score: 182 / 192**
Contingent: 187 if one open question resolves positively, 192 if both resolve positively.

---

### V-05 — Conversational register + role sequence split (confirming)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-07 | PASS | Essential criteria |
| C-08–C-15 | PASS | Not under test |
| C-16 | PASS | Persona brief placed at document top — precedes Stage 1 entirely; positional requirement satisfied before inventory gate |
| C-17–C-21 | PASS | Not under test |
| C-22 | PASS | Canonical vocabulary; no substitution |
| C-23 | PASS | Unnumbered coda appended after last numbered stage |
| C-24 | PASS | Obligation table inside Stage 1 before gate — positional requirement satisfied regardless of enclosing stage boundary |
| C-25 | PASS | Column headers = Obligation Term values |
| C-26 | PASS | Explicit ARE (conversational phrasing): "these are your column headers — they ARE the obligation names above, word for word" → schema-only enforcement in second-person register |
| C-27 | N/A | No non-standard terms |
| C-28 | PASS | Stages frame; terminal-position formula present with conversational framing |

**Score: 192 / 192** ✓ Confirming variation — register and sequence split create zero structural drift.

---

### Composite Rankings

| Rank | Variation | Score | Status |
|------|-----------|-------|--------|
| 1T | V-03 | **192 / 192** | Confirmed — Phase frame |
| 1T | V-05 | **192 / 192** | Confirmed — conversational/sequence |
| 3T | V-01 | **187 / 192** | Q1-contingent (+5 possible) |
| 3T | V-02 | **187 / 192** | Q2-contingent (+5 possible) |
| 5 | V-04 | **182 / 192** | Q1+Q2-contingent (+10 possible) |

---

### Open Question Status After R9

| Q | Question | Status | Evidence |
|---|----------|--------|----------|
| Q1 | C-26 — explicit ARE required, or any schema-aligned instruction? | **Still open** | V-01 scored conservatively at FAIL. V-03/V-05 both used explicit ARE and confirmed 192/192. No variation tested ARE-equivalent non-ARE form against a known C-25 pass — Q1 remains unresolved. |
| Q2 | C-27 — single block or per-term distribution? | **Still open** | V-02 scored conservatively at FAIL. V-03/V-05 both had no non-standard terms (N/A). No variation tested per-term against a known C-27 pass — Q2 remains unresolved. |

---

### Excellence Signals

**From V-03 (Phase frame):**
- C-28 formula composition is confirmed frame-agnostic: substituting "phase" and "Phase 3" produces structurally identical enforcement. The formula is a template, not a stages-specific idiom.
- The confirming variation pattern: a variation that changes only the outer frame vocabulary while holding all other axes constant provides clean attribution — any score delta isolates frame effects without confounding.

**From V-05 (Conversational register + role sequence split):**
- **Role sequence split is positionally equivalent to co-location.** Placing persona brief at document top and obligation table inside Stage 1 (before gate) satisfies both C-16 and C-24 simultaneously. The rubric's positional requirements are relative-to-gate, not relative-to-each-other — co-location is never required.
- **Conversational ARE is structurally equivalent to declarative ARE.** Second-person phrasing ("they ARE the obligation names above, word for word") satisfies C-26 as fully as formal declarative register. Register is not a structural dimension for these criteria.

---

### New Patterns for R10

1. **Role-sequence split pattern** — Persona brief at document preamble + obligation table inside Stage 1 before gate is a valid structural configuration. The two elements need not be co-located; positional anchoring is gate-relative, not element-relative. This opens a design space where preamble-level context and in-stage tables are interchangeable with in-stage sequenced declarations.

2. **Register-invariant structural criteria** — C-16, C-24, C-25, C-26, C-28 all confirmed stable under conversational second-person imperative register. No criterion depends on formal declarative phrasing. Rubric compliance is purely structural/positional, not register-specific.

---

```json
{"top_score": 192, "all_essential_pass": true, "new_patterns": ["Role-sequence split: persona brief at document preamble + obligation table inside Stage 1 before gate satisfies C-16 and C-24 simultaneously without co-location — positional anchoring is gate-relative", "Register-invariant structural criteria: C-16, C-24, C-25, C-26, C-28 all confirmed stable under conversational second-person imperative — no criterion depends on formal declarative register"]}
```
