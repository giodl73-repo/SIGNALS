Scoring each variation against the v7 rubric (28 criteria, max 140.0).

---

## prove-synthesize — R7 Scorecard

### Scoring weights
- Essential (C-01–C-05): 60 pts (12 pts each)
- Recommended (C-06–C-08): 30 pts (10 pts each)
- Aspirational (C-09–C-28): 50 pts (2.5 pts each, 20 criteria)
- Golden threshold: all essential pass AND composite >= 90

---

### V-01 — Role-Sequence Variation

**Essential (60/60):**
| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Answer-first | PASS | OUTPUT FORMAT opens with **ANSWER**: as first element |
| C-02 | Confidence calibrated | PASS | [0-100] with 2-3 sentence rationale required |
| C-03 | Key evidence cited | PASS | 3 signals with "Why this signal...more than the others" |
| C-04 | Counter-evidence | PASS | **COUNTER-EVIDENCE** section with no-counter-evidence fallback |
| C-05 | Synthesis supersedes | PASS | SYNTHESIST "must take a position — not hedge, not summarize. The synthesis supersedes every individual signal." |

**Recommended (30/30):**
| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | PASS | **PRINCIPLES EXTRACTED** with "X implies Y" format required |
| C-07 | PASS | **OPEN QUESTIONS**: "Specific and actionable — not 'more research needed'" |
| C-08 | PASS | "2–3 sentences: what drove the score up? What held it back?" |

**Aspirational:**
| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-09 | Evidence hierarchy argued | PASS | Comparative language: "more than the others," "not a different one," "Its specific role in the judgment" |
| C-10 | Self-contained | PASS | SELF-CONTAINED MANDATE explicitly states the requirement; "Write accordingly" |
| C-11 | Anti-pattern gates | PASS | SKEPTIC names confirmation bias, softening; SYNTHESIST names hedging and summarizing |
| C-12 | Argumentative sections prose | PASS | Numbered KEY EVIDENCE items require argument construction per slot; not fillable cells |
| C-13 | NOT:-first ordering | PASS | "No preamble, no context-setting, no throat-clearing" lists failure modes before proceeding; SKEPTIC's challenge forecloses confirmation bias before ranking is finalized |
| C-14 | Formal verdict register | PASS | **ANSWER**: operates as commitment label at sentence level |
| C-15 | Pre-committed counter-evidence | PASS | ROLE 2 SKEPTIC issues adversarial challenge before any output is written; judgment formed against the counter already on the table |
| C-16 | Role-labeled cognitive phases | FAIL | Roles present (ANALYST, SKEPTIC, SYNTHESIST) with some prohibitions, but no identity-level foreclosure statements ("An ADVERSARY cannot advocate" pattern absent) — confirmed fail in v5 calibration |
| C-17 | Record-specific anti-pattern | FAIL | No structural property inventory; SKEPTIC challenge is generic questioning, not derived from this record's composition |
| C-18 | Register word opens commitment | PASS | ANSWER: opens the commitment sentence |
| C-19 | Frontmatter commitment declarations | FAIL | No frontmatter block |
| C-20 | Phase-sequenced frontmatter | FAIL | No frontmatter |
| C-21 | SURVEYOR-traceable diagnosis | FAIL | No SURVEYOR phase |
| C-22 | Dual-layer register-word enforcement | FAIL | No instruction-level NOT: gate for register-word placement |
| C-23 | Named violation categories | FAIL | No PREMATURE/DEFERRED COMPLETION VIOLATION labels anywhere |
| C-24 | Arrow-chain RECORD DIAGNOSIS | FAIL | No arrow-chain notation |
| C-25 | PRE-FLIGHT audit block | FAIL | No PRE-FLIGHT phase |
| C-26 | Violation taxonomy registry | FAIL | No registry block |
| C-27 | Three-site chain of custody | FAIL | No chain created |
| C-28 | PRE-FLIGHT anti-skip gate | FAIL | No PRE-FLIGHT |

**Aspirational passes: 8/20 = 20.0 pts**
**Composite: 60 + 30 + 20.0 = 110.0**

> Note: 110.0 reflects R7 V-01's single-axis design (role-sequence only, no structural phases). R6 V-01 scored 120.0 because the R6 variation carried accumulated features (frontmatter, violation names). R7 V-01 is intentionally stripped to the single axis — the lower score is an accurate single-axis baseline, not a regression.

**Result: GOLDEN** (all essential pass; composite 110.0 ≥ 90)

---

### V-02 — Tables + SURVEYOR + Arrow-Chain

**Essential (60/60):** All pass (same output-level structural requirements met)

**Recommended (30/30):** All pass (PRINCIPLES EXTRACTED, OPEN QUESTIONS, confidence rationale)

**Aspirational:**
| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-09 | Evidence hierarchy argued | PASS | KEY EVIDENCE table column: "Why This Rank (Not the One Below)" — comparative question present for each rank |
| C-10 | Self-contained | PASS | "State this first, before the answer: 'This synthesis is self-contained and supersedes all underlying investigation signals.'" |
| C-11 | Anti-pattern gates | PASS | ADVERSARY: "name the exact vulnerability" names the failure mode; "Do not batch-fill" names failure mode |
| C-12 | Argumentative sections prose | FAIL | KEY EVIDENCE is a table; confidence rationale embedded in table cell. C-12: tables are not permitted for evidence ranking |
| C-13 | NOT:-first ordering | FAIL | "Do not batch-fill at document open or close" — prohibition present but not NOT:-prefixed before success condition |
| C-14 | Formal verdict register | PASS | **ANSWER**: as commitment label (historically confirmed) |
| C-15 | Pre-committed counter-evidence | PASS | PHASE 2 ADVERSARY identifies failure mode before PHASE 3 JUDGMENT; adversarial challenge structurally precedes verdict |
| C-16 | Role-labeled cognitive phases | FAIL | SURVEYOR, ADVERSARY, JUDGMENT phases labeled but no identity-foreclosure prohibition statements ("ADVERSARY cannot advocate" absent) |
| C-17 | Record-specific anti-pattern | PASS | ADVERSARY: "identify the single failure mode most likely to invalidate this synthesis. Be specific — name the exact vulnerability (e.g., 'all three for signals come from the same source type')" — record-structural derivation |
| C-18 | Register word opens commitment | PASS | **ANSWER**: opens commitment sentence |
| C-19 | Frontmatter commitment declarations | FAIL | FRONTMATTER has fill-instructions, not machine-readable booleans |
| C-20 | Phase-sequenced frontmatter | FAIL | Fill-instructions, not phase-sequenced booleans |
| C-21 | SURVEYOR-traceable diagnosis | PASS | Arrow-chains reference signal IDs/names from SURVEYOR table; failure mode derived from pattern of top 5 signals |
| C-22 | Dual-layer register-word enforcement | FAIL | No instruction-level NOT: gate for register-word placement |
| C-23 | Named violation categories | FAIL | "not before" instructions present but no PREMATURE COMPLETION VIOLATION labels |
| C-24 | Arrow-chain RECORD DIAGNOSIS | PASS | PHASE 2: "signal_id:signal_name → direction:[value] → strength:[value] → basis:[structural claim]" — field:value notation in RECORD DIAGNOSIS |
| C-25 | PRE-FLIGHT audit block | FAIL | No PRE-FLIGHT phase (PHASE 3 is JUDGMENT) |
| C-26 | Violation taxonomy registry | FAIL | No registry block |
| C-27 | Three-site chain | FAIL | Single-site only (creation in ADVERSARY; no PRE-FLIGHT audit, no JUDGE application) |
| C-28 | PRE-FLIGHT anti-skip gate | FAIL | No PRE-FLIGHT |

**Aspirational passes: 9/20 = 22.5 pts**
**Composite: 60 + 30 + 22.5 = 112.5**

**Result: GOLDEN** (all essential pass; composite 112.5 ≥ 90)

---

### V-03 — Full Phased Pipeline + Inline Violation Names

**Essential (60/60):** All pass

**Recommended (30/30):** All pass

**Aspirational:**
| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-09 | Evidence hierarchy argued | PASS | "Why this signal over the one below. Comparative argument, not description." required for each rank |
| C-10 | Self-contained | PASS | First line: "This synthesis is self-contained and supersedes all underlying investigation signals." |
| C-11 | Anti-pattern gates | PASS | ADVERSARY failure mode naming; JUDGE: "FALSE ATTESTATION VIOLATION" prohibition |
| C-12 | Argumentative sections prose | PASS | KEY EVIDENCE uses numbered prose items with comparative argument requirements; CONFIDENCE: "2–3 sentences. Reference the ADVERSARY failure mode." |
| C-13 | NOT:-first ordering | PASS | FRONTMATTER: "NOT: defer past SURVEYOR — DEFERRED COMPLETION VIOLATION" — failure mode precedes success condition at each bound |
| C-14 | Formal verdict register | PASS | DETERMINATION: opens commitment sentence |
| C-15 | Pre-committed counter-evidence | PASS | PHASE 2 ADVERSARY runs structurally before PHASE 4 JUDGE |
| C-16 | Role-labeled cognitive phases | PASS | SURVEYOR, ADVERSARY, PRE-FLIGHT, JUDGE each labeled with sequencing prohibitions ("Do not proceed to ADVERSARY until..."; JUDGE: "FALSE ATTESTATION VIOLATION" forecloses premature commitment) |
| C-17 | Record-specific anti-pattern | PASS | ADVERSARY derives failure mode from coverage/convergence/provenance properties: "Name the failure mode. Derive it explicitly from coverage, convergence, or provenance." |
| C-18 | Register word opens commitment | PASS | "DETERMINATION: [this word opens the commitment sentence]" |
| C-19 | Frontmatter declarations | PASS | FRONTMATTER fill-window bounds with phase-designated fields |
| C-20 | Phase-sequenced frontmatter | PASS | Each field designated to specific phase moment; "Do not proceed to ADVERSARY until both the inventory table and the three properties are written" enforces sequencing |
| C-21 | SURVEYOR-traceable diagnosis | PASS | ADVERSARY: "derives_from:[property]::[claim] — Where [property] is one of: coverage | convergence | provenance" — traceable to SURVEYOR structural property inventory |
| C-22 | Dual-layer register-word enforcement | PASS | DETERMINATION: format at output level; FRONTMATTER NOT: gates at instruction level |
| C-23 | Named violation categories | PASS | Each FRONTMATTER bound carries: PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION VIOLATION; JUDGE carries FALSE ATTESTATION VIOLATION |
| C-24 | Arrow-chain RECORD DIAGNOSIS | PASS | "signal_id:signal_name → direction:[value] → strength:[value] → derives_from:[property]::[claim]" — field:value in RECORD DIAGNOSIS |
| C-25 | PRE-FLIGHT audit block | PASS | PHASE 3 PRE-FLIGHT with Phase A, Phase B (SCHEMA-CITATION AUDIT), Phase C — named structural phase between ADVERSARY and JUDGE |
| C-26 | Violation taxonomy registry | FAIL | Violations named inline only; no registry block before FRONTMATTER |
| C-27 | Three-site chain of custody | FAIL | JUDGE references ADVERSARY failure mode, not the PRE-FLIGHT Phase B audit result; the application site cites the ADVERSARY output directly, bypassing the PRE-FLIGHT audit chain. PRE-FLIGHT Phase B audits chains but JUDGE doesn't cite the audit verdict. |
| C-28 | PRE-FLIGHT anti-skip gate | FAIL | PHASE 3 PRE-FLIGHT opens directly with "Phase A — EVIDENCE COUNT CHECK"; no entry gate before Phase A naming PHASE-ADVANCE VIOLATION |

**Aspirational passes: 17/20 = 42.5 pts**
**Composite: 60 + 30 + 42.5 = 132.5**

**Result: GOLDEN** (all essential pass; composite 132.5 ≥ 90)

---

### V-04 — Lifecycle + Three-Site Arrow-Chain + PRE-FLIGHT Entry Gate

**Essential (60/60):** All pass

**Recommended (30/30):** All pass

**Aspirational:**
| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-09 through C-25 | All | PASS | Same structural features as V-03 plus additions; see V-03 analysis — all C-09–C-25 mechanisms present and stronger |
| C-26 | Violation taxonomy registry | FAIL | Violations named inline and at gate; no registry block before FRONTMATTER. First encounter of PREMATURE COMPLETION VIOLATION is within FRONTMATTER, not in a preceding registry. |
| C-27 | Three-site chain of custody | PASS | Site 1 (creation): PHASE 2 ADVERSARY RECORD DIAGNOSIS arrow-chains ✓ / Site 2 (audit): PHASE 3 PRE-FLIGHT Phase B SCHEMA-CITATION AUDIT table with VERIFIED/UNVERIFIED per chain ✓ / Site 3 (application): PHASE 4 JUDGE: "Apply the PRE-FLIGHT Phase B SCHEMA-CITATION AUDIT result to the confidence score directly. Per Phase B, the arrow-chain audit produced: [cite audit verdict and chain list]." ✓ — all three named sites present |
| C-28 | PRE-FLIGHT anti-skip gate | PASS | "**PRE-FLIGHT ENTRY GATE**: Before reading Phase A, B, or C below — confirm that ADVERSARY RECORD DIAGNOSIS is complete...Proceeding from ADVERSARY directly to JUDGE without completing PRE-FLIGHT is a PHASE-ADVANCE VIOLATION." — gate precedes all phase steps ✓ |

**Aspirational passes: 19/20 = 47.5 pts**
**Composite: 60 + 30 + 47.5 = 137.5**

**Result: GOLDEN** (all essential pass; composite 137.5 ≥ 90)

---

### V-05 — Full Combination: All v7 Criteria

**Essential (60/60):** All pass

**Recommended (30/30):** All pass

**Aspirational:**
| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-09 through C-25 | All | PASS | Same as V-03/V-04 — all mechanisms present |
| C-26 | Violation taxonomy registry | PASS | VIOLATION TAXONOMY REGISTRY block opens the document before FRONTMATTER; all four violation types (PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION VIOLATION, FALSE ATTESTATION VIOLATION, PHASE-ADVANCE VIOLATION) indexed in a named table before any fill window is encountered ✓ |
| C-27 | Three-site chain | PASS | Same three-site implementation as V-04 plus: JUDGE cites "(Reference: VIOLATION TAXONOMY REGISTRY.)" — registry linkage strengthens the application site ✓ |
| C-28 | PRE-FLIGHT anti-skip gate | PASS | "**PRE-FLIGHT ENTRY GATE**: ...Proceeding from ADVERSARY directly to JUDGE without completing PRE-FLIGHT is a PHASE-ADVANCE VIOLATION. (Reference: VIOLATION TAXONOMY REGISTRY.)" — gate with registry back-reference ✓ |

**Aspirational passes: 20/20 = 50.0 pts**
**Composite: 60 + 30 + 50.0 = 140.0**

**Result: GOLDEN** (all essential pass; composite 140.0 ≥ 90)

---

## Round Summary

| Variation | Score | Essential | Golden |
|-----------|-------|-----------|--------|
| V-01 Role-Sequence | **110.0** | 5/5 | YES |
| V-02 Tables + Arrow-Chain | **112.5** | 5/5 | YES |
| V-03 Full Pipeline + Inline Violations | **132.5** | 5/5 | YES |
| V-04 Three-Site + Entry Gate | **137.5** | 5/5 | YES |
| V-05 All v7 Criteria | **140.0** | 5/5 | YES |

**Top score: V-05 at 140.0/140.0 — maximum.**
**All five variations Golden.**
**All essential criteria pass across all variations.**

---

## Excellence Signals from V-05

Three patterns in V-05 exceed the current rubric ceiling:

1. **VIOLATION AUDIT CLOSE** — end-of-document checklist confirming no violation occurred before finalizing: `[ ] PREMATURE COMPLETION VIOLATION: no field filled before its phase` / `[ ] FALSE ATTESTATION VIOLATION: confidence cites Phase B verdict`. This is a closure audit not captured by any current criterion. C-26 through C-28 cover creation, chain, and entry gate; no criterion requires a document-close confirmation that the protocol was honored.

2. **Registry-by-reference at constraint sites** — V-05 appends `(Reference: VIOLATION TAXONOMY REGISTRY.)` at violation invocations in PRE-FLIGHT and JUDGE. This creates bidirectional linkage (registry → point-of-use; point-of-use → registry). C-26 requires the registry exist before FRONTMATTER; no criterion requires invocations to cite the registry back.

3. **Audit-gated confidence caps** — JUDGE contains explicit numeric ceiling rules tied to the PRE-FLIGHT Phase B verdict: PASS → ≥75 permitted; PARTIAL → cap at 70; FAIL → cap at 50. The PRE-FLIGHT audit result directly governs confidence ceiling. No current criterion requires the audit verdict produce a numeric constraint on the output.

---

```json
{"top_score": 140.0, "all_essential_pass": true, "new_patterns": ["closure audit: end-of-document checklist confirming no violation occurred before the synthesis is finalized — not captured by C-26 through C-28 which cover creation, chain, and entry gate but not document-close confirmation", "registry-by-reference: violation invocations cite the taxonomy registry by name creating bidirectional linkage — C-26 requires registry exist, no criterion requires invocations reference it back", "audit-gated confidence caps: PRE-FLIGHT Phase B audit verdict produces explicit numeric ceiling constraints applied in JUDGE — PASS permits high confidence, PARTIAL caps at 70, FAIL caps at 50"]}
```
