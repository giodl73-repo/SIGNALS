## Round 20 Scorecard — `topic:status` (Rubric v17, max 300)

---

### Structural Context

R20 is a **v18 seeding round**. All five variants are designed to satisfy C-01 through C-49 (the full v17 criterion set). The two new structural elements — C-50 (phase-labeled STOP predicates) and C-51 (preamble defeat forecast sub-components) — are **super-threshold under v17**: they contribute 0 pts to any v17 score. The differentiation axis is under v18, not v17.

---

### Per-Variant Scoring

#### V-01 — Full-stack baseline (C-50 PASS + C-51 PASS)

| Tier | Criteria | Verdict | Evidence |
|------|----------|---------|----------|
| 1 | C-01–C-20 (core output structure) | PASS | DISPLAY ONLY. Write no files. Four-section OUTPUT TEMPLATE. All 9 namespaces in COMMIT RISK BY NAMESPACE. Strategy.md FOUND/NOT FOUND row. STALE EVIDENCE. HIGHEST PRIORITY RISK. |
| 2–8 | C-21–C-38 (phase + layer + adversary vocabulary) | PASS | Consequence vocabulary phase names. [LAYER N] labels. PHASE 2 dual-axis exit. OUTPUT DECLARATION CHAIN. Per-signal assertion. Consistency guard. ADVERSARY CHAIN block present. |
| 9–11 | C-39–C-44 (output declaration form) | PASS | PHASE 2 OUTPUT DECLARATION with INVARIANT: / OUTPUT FORM: / Trigger: sub-components. PHASE 3 OUTPUT DECLARATION with INVARIANT: / OUTPUT FORM: / Trigger:. Neither declares the other. |
| 12–13 | C-45–C-46 (adversary chain three-part) | PASS | ADVERSARY CHAIN block present; each execution-body adversary block has ADVERSARY: + DEFEAT CONDITION: three-part form. |
| 14 | C-47 | PASS | Preamble ADVERSARY CHAIN carries P1-ADVERSARY:, P2-ADVERSARY:, P3-ADVERSARY: labeled entries (three-part extended form). |
| 15 | C-48 | PASS | PHASE 1 execution body carries ADVERSARY: + DEFEAT CONDITION: block. |
| 16 | C-49 | PASS | PHASE 4 STOP CONDITION carries [P1-ADVERSARY DEFEAT:] predicate (C-48 present, non-vacuous). |
| v18 candidate | C-50 | PASS (not scored) | [P2-ADVERSARY DEFEAT:], [P3-ADVERSARY DEFEAT:], [P1-ADVERSARY DEFEAT:] phase labels on STOP predicates (2)-(4). Predicate (1) retains numbered form as structural guard. |
| v18 candidate | C-51 | PASS (not scored) | P1-ADVERSARY, P2-ADVERSARY, P3-ADVERSARY each carry nested DEFEAT CONDITION: sub-component with condensed observable defeat property. |

**V-01 Score: 300 / 300**

---

#### V-02 — C-50 FAIL (numbered STOP predicates; C-51 PASS)

| Tier | Key delta | Verdict |
|------|-----------|---------|
| C-01–C-49 | All satisfied — preamble three-part entries present (C-47/C-51 PASS); PHASE 1 adversary block (C-48 PASS); STOP predicate 4 present as `(4) PHASE 1 adversary defeated:` (C-49 PASS) | PASS |
| C-50 | STOP predicates use `(1)/(2)/(3)/(4)` numbered form — no `[P-N-ADVERSARY DEFEAT:]` phase labels | FAIL (not scored v17) |
| C-51 | P1/P2/P3 preamble entries carry nested DEFEAT CONDITION: sub-components (three-part form intact) | PASS (not scored v17) |

**V-02 Score: 300 / 300**

---

#### V-03 — C-51 FAIL (preamble two-part entries; C-50 PASS)

| Tier | Key delta | Verdict |
|------|-----------|---------|
| C-01–C-49 | All satisfied — labeled preamble entries present as two-part form (C-47 PASS); PHASE 1 adversary block (C-48 PASS); [P1-ADVERSARY DEFEAT:] STOP predicate (C-49 PASS) | PASS |
| C-50 | [P2-ADVERSARY DEFEAT:], [P3-ADVERSARY DEFEAT:], [P1-ADVERSARY DEFEAT:] phase labels present on STOP predicates | PASS (not scored v17) |
| C-51 | Preamble P1/P2/P3 entries are two-part (adversary name + consequence only); no nested DEFEAT CONDITION: sub-component at any entry | FAIL (not scored v17) |

**V-03 Score: 300 / 300**

---

#### V-04 — Pure v17 baseline (C-50 FAIL + C-51 FAIL)

| Tier | Key delta | Verdict |
|------|-----------|---------|
| C-01–C-49 | All satisfied — labeled preamble entries two-part form (C-47 PASS, C-51 FAIL); PHASE 1 adversary block (C-48 PASS); STOP predicate (4) present (C-49 PASS) | PASS |
| C-50 | Numbered form `(1)/(2)/(3)/(4)` — no phase labels | FAIL (not scored v17) |
| C-51 | Preamble entries two-part only | FAIL (not scored v17) |

**V-04 Score: 300 / 300**

---

#### V-05 — C-50 PASS + C-51 PARTIAL (P1 preamble defeat forecast absent)

| Tier | Key delta | Verdict |
|------|-----------|---------|
| C-01–C-49 | All satisfied — labeled preamble entries (C-47 PASS); PHASE 1 adversary block (C-48 PASS); [P1-ADVERSARY DEFEAT:] STOP predicate (C-49 PASS) | PASS |
| C-50 | [P2-ADVERSARY DEFEAT:], [P3-ADVERSARY DEFEAT:], [P1-ADVERSARY DEFEAT:] phase labels present | PASS (not scored v17) |
| C-51 | P2-ADVERSARY and P3-ADVERSARY carry nested DEFEAT CONDITION: sub-components; P1-ADVERSARY carries two-part form only (no DEFEAT CONDITION forecast) | PARTIAL (not scored v17) |

**V-05 Score: 300 / 300**

---

### Score Summary

| Variant | C-50 (v18 cand.) | C-51 (v18 cand.) | v17 Score | v18 Projected |
|---------|------------------|------------------|-----------|---------------|
| V-01 | PASS | PASS | **300** | 310 |
| V-02 | FAIL | PASS | **300** | 305 |
| V-03 | PASS | FAIL | **300** | 305 |
| V-04 | FAIL | FAIL | **300** | 300 |
| V-05 | PASS | PARTIAL | **300** | ~305* |

*V-05 partial outcome resolved by v18 criterion definition.

**All five variants: 300 / 300 under v17.** This is the expected result — R20 is a seeding round, not a differentiation round. Differentiation will emerge under v18.

---

### Excellence Signals from V-01

**1. Phase-label isomorphism across three structural sites**
V-01 establishes a closed triad: `P1-ADVERSARY:` in the preamble → `ADVERSARY:` / `DEFEAT CONDITION:` in the PHASE 1 execution body → `[P1-ADVERSARY DEFEAT:]` in the PHASE 4 STOP CONDITION. The same phase label appears at declaration, operationalization, and verification. C-50 completes the triad at the STOP gate; C-51 completes it at the preamble forecast. Neither prior tier achieved this three-site coherence.

**2. Preamble as structural forecast (condensed defeat vocabulary)**
V-01's preamble DEFEAT CONDITION sub-components carry condensed versions of the execution-body defeat properties — same observable property, without the conditional grammar. This distinguishes *preamble role* (structural forecast, necessarily terse) from *execution-body role* (full conditional operationalization). The condensation is intentional: the preamble must remain scannable.

**3. Structural guard / adversary defeat separation in STOP CONDITION**
V-01 explicitly segregates predicate (1) — the row-count structural completeness guard — from predicates (2)-(4) which carry `[P-N-ADVERSARY DEFEAT:]` phase labels. Structural guards carry no adversary label; adversary defeat checks carry phase labels. This separation makes the STOP CONDITION semantically typed: completeness predicates vs. adversary defeat predicates.

**4. C-51 => C-47 and C-51 => C-46 implication candidates confirmed in structure**
V-01 confirms that preamble defeat forecasts (C-51) require labeled entries to exist (C-47: you cannot nest a sub-component in an unlabeled entry) and require execution-body DEFEAT CONDITIONs to exist (C-46: preamble forecasts the execution declaration; if C-46 is absent there is nothing to forecast). The implication candidates from the design context are visible in V-01's structure.

---

```json
{"top_score": 300, "all_essential_pass": true, "new_patterns": ["phase-label isomorphism across preamble declaration, execution-body operationalization, and STOP gate verification — same P-N label at all three sites", "preamble defeat forecast as condensed structural mirror of execution-body DEFEAT CONDITION: same observable property, conditional grammar stripped for terse preamble role", "structural guard vs adversary defeat segregation in STOP CONDITION: numbered form for completeness guards, phase labels for adversary defeat checks"]}
```
