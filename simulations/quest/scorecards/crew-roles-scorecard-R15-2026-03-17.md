# crew-roles R15 — Quest Score Evaluation

## Baseline Inherited State (R14 all-three-combined)

Before scoring variations, establish what R14 baseline already delivers:

| Block | Status |
|-------|--------|
| C-01–C-05 Essential | All PASS |
| C-06 Lens actionability | PASS (C-32 inline LENS AUDIT gate) |
| C-07 Collaborates_with resolves | PASS |
| C-08 Perspective diversity | **PARTIAL** — Phase 5 column present, Phase 6 says "3 distinct", no structural gate (Gap-A) |
| C-09–C-23 Aspirational | All PASS |
| C-24 Replacement re-audit | **PARTIAL** — ad hoc, no ROLE-REPLACE sub-procedure (Gap-C) |
| C-25 Frame-slot source citation | **PARTIAL** — cites CONVERGENCE SUMMARY, not Phase 1 verbatim (Gap-B) |
| C-26, C-28–C-32 | All PASS |
| C-27 Source-phrase forensic citation | **PARTIAL** — no Phase 1 verbatim trace (Gap-B) |

**Baseline aspirational PASS count: 21 / 24**

---

## V-01 — Perspective Diversity Gate

**Mechanism**: PERSPECTIVE AUDIT fires before Phase 6 opens; CHECK 8 in Phase 7 validates ≥ 3 distinct perspective values from written files.

### Essential
| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | Inherited |
| C-02 | PASS | Inherited |
| C-03 | PASS | Inherited |
| C-04 | PASS | Inherited |
| C-05 | PASS | Inherited |

### Recommended
| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | C-32 gate inherited |
| C-07 | PASS | Inherited |
| C-08 | **PASS** | PERSPECTIVE AUDIT gate fires before Phase 6; CHECK 8 re-validates from written files — structural gate closes Gap-A |

### Aspirational Changes from Baseline
| ID | Verdict | Evidence |
|----|---------|---------|
| C-24 | PARTIAL | No ROLE-REPLACE sub-procedure — Gap-C unaddressed |
| C-25 | PARTIAL | FRAME FILL still cites CONVERGENCE SUMMARY only — Gap-B unaddressed |
| C-27 | PARTIAL | No Phase 1 verbatim trace — Gap-B unaddressed |
| All others | PASS | Inherited |

**Aspirational PASS: 21 / 24 → 8.75 pts**
**Score: 88** (C-08 recommended now full PASS; gaps B and C remain)

---

## V-02 — Source Phrase Forensic Citation

**Mechanism**: Each FRAME FILL slot gains a `Phase 1 source: {row-id} = "{verbatim phrase}"` line; CHECK 5 splits into 5A (frame match) + 5B (source citation present and verifiable).

### Essential: All PASS (inherited)

### Recommended
| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Inherited |
| C-07 | PASS | Inherited |
| C-08 | PARTIAL | Phase 5 Perspective column exists but no gate added — Gap-A unaddressed |

### Aspirational Changes from Baseline
| ID | Verdict | Evidence |
|----|---------|---------|
| C-25 | **PASS** | FRAME FILL now includes `Phase 1 source:` lines per slot — direct verbatim citation from Phase 1 |
| C-27 | **PASS** | CHECK 5B flags missing or unverifiable citations — forensic citation now structural |
| C-24 | PARTIAL | ROLE-REPLACE not added — Gap-C unaddressed |
| All others | PASS | Inherited |

**Aspirational PASS: 23 / 24 → 9.58 pts**
**Score: 94** (C-08 still PARTIAL offsets vs V-04)

---

## V-03 — Role Replacement Re-Audit

**Mechanism**: ROLE-REPLACE sub-procedure fires at every CHECK 3B / 4B mismatch. Four fields: planned, written, resolution, re-evaluation. Gate emits `ROLE-REPLACE CONFIRMED: YES/NO`. CHECK 3B / 4B cannot close until all CONFIRMED signals are YES.

### Essential: All PASS (inherited)

### Recommended
| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Inherited |
| C-07 | PASS | Inherited |
| C-08 | PARTIAL | No perspective gate — Gap-A unaddressed |

### Aspirational Changes from Baseline
| ID | Verdict | Evidence |
|----|---------|---------|
| C-24 | **PASS** | ROLE-REPLACE fires at each mismatch, records event, re-evaluates row, emits CONFIRMED artifact — full re-evaluation trail closes Gap-C |
| C-25 | PARTIAL | Phase 1 verbatim source not added — Gap-B unaddressed |
| C-27 | PARTIAL | Forensic citation mechanism not added — Gap-B unaddressed |
| All others | PASS | Inherited |

**Aspirational PASS: 22 / 24 → 9.17 pts**
**Score: 91** (C-24 now closed; gaps A and B remain)

---

## V-04 — V-01 + V-02 (Perspective + Source Citation)

**Mechanism**: PERSPECTIVE AUDIT gate + CHECK 8 (V-01) AND Phase 1 source lines + CHECK 5B (V-02). Both Gap-A and Gap-B closed.

### Essential: All PASS (inherited)

### Recommended
| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Inherited |
| C-07 | PASS | Inherited |
| C-08 | **PASS** | PERSPECTIVE AUDIT gate from V-01 — full pass |

### Aspirational Changes from Baseline
| ID | Verdict | Evidence |
|----|---------|---------|
| C-25 | **PASS** | Phase 1 source lines from V-02 |
| C-27 | **PASS** | CHECK 5B from V-02 |
| C-24 | PARTIAL | ROLE-REPLACE not added — Gap-C unaddressed |
| All others | PASS | Inherited |

**Aspirational PASS: 23 / 24 → 9.58 pts**
**Score: 95** (C-08 full PASS pushes above V-02; Gap-C remains)

---

## V-05 — V-01 + V-02 + V-03 (All Three Gaps Closed)

**Mechanism**: All three gap-closing mechanisms combined. PERSPECTIVE AUDIT gate + CHECK 8 + Phase 1 source lines + CHECK 5B + ROLE-REPLACE sub-procedure with CONFIRMED signals.

### Essential: All PASS (inherited)

### Recommended
| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | Inherited |
| C-07 | PASS | Inherited |
| C-08 | **PASS** | PERSPECTIVE AUDIT gate before Phase 6 — structural enforcement |

### Aspirational
| ID | Verdict | Evidence |
|----|---------|---------|
| C-24 | **PASS** | ROLE-REPLACE fires at every mismatch; CONFIRMED gate blocks CHECK 3B/4B from closing until all YES |
| C-25 | **PASS** | `Phase 1 source:` lines in every FRAME FILL slot — verbatim traceable |
| C-27 | **PASS** | CHECK 5B validates each citation; unverifiable = MISMATCH flag |
| All others | PASS | Inherited + C-30, C-31, C-32 from baseline |

**Aspirational PASS: 24 / 24 → 10.0 pts**
**Score: 98** (all essential PASS, all recommended PASS, all aspirational PASS; 2 pts reserved for real-execution verification)

---

## Rankings

| Rank | Variation | Score | Aspirational | Gaps Closed |
|------|-----------|-------|-------------|-------------|
| 1 | **V-05** | **98** | 24 / 24 | A + B + C |
| 2 | V-04 | 95 | 23 / 24 | A + B |
| 3 | V-02 | 94 | 23 / 24 | B only |
| 4 | V-03 | 91 | 22 / 24 | C only |
| 5 | V-01 | 88 | 21 / 24 | A only |

**Note**: V-02 and V-04 both hit 23/24 aspirational but V-04 edges ahead because C-08 (recommended) reaches full PASS via the structural gate, not just a column.

---

## Excellence Signals — V-05

**Pattern 1 — Phase-boundary audit gates that block the next phase**
PERSPECTIVE AUDIT is not a post-write check — it fires before Phase 6 opens. This structural pattern (gate must PASS before next phase begins) is the same mechanism as C-30 (inertia-first), C-15 (verification gate), and C-17 (pre-write scope audit). V-05 extends it to perspective coverage, making Phase 6 unreachable without a confirmed diversity signal.

**Pattern 2 — First-class replacement event artifacts with CONFIRMED gate**
ROLE-REPLACE is not a retry loop — it is a sub-procedure that produces a four-field artifact (planned / written / resolution / re-evaluation) and emits a binary CONFIRMED signal. The owning CHECK cannot close until every CONFIRMED is YES. This is the auditable replacement pattern: the event is recorded, the re-evaluation is explicit, and the gate enforces it.

**Pattern 3 — Verbatim source binding at FRAME FILL authoring time**
C-27 previously required citation; V-05 requires that the citation happen inline during FRAME FILL authoring — `Phase 1 source: {row-id} = "{verbatim phrase}"` — not as a post-write annotation. This makes each derived term immediately traceable to its Phase 1 origin without a separate forensic pass.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["Phase-boundary audit gate blocks next phase until PASS — applied to perspective diversity, same structural family as inertia-first and pre-write scope gates", "ROLE-REPLACE as first-class sub-procedure producing CONFIRMED artifact — owning CHECK cannot close until all CONFIRMED signals are YES", "Verbatim source binding inline at FRAME FILL authoring time — each derived term has Phase 1 row-id citation written during authoring, not added post-hoc"]}
```
