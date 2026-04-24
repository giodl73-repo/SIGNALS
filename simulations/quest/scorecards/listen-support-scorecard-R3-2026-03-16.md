## listen-support — Quest Score, Round 3

### Variation Evaluations

---

#### V-01 — Card Template Rigidity (C-14 target)

| Criterion | Type | Score | Evidence |
|-----------|------|-------|---------|
| C-01 Title named field | E | **12** | Card template: `## T-NN` heading + `- Title:` as explicit named field. Title rule states "T-NN heading does NOT satisfy Title field." |
| C-02 Vocabulary declared | E | **12** | Controlled values in planning table; TABLE CHECK enforces them. |
| C-03 First-person voice | E | **12** | Step 4 Performance Mode: "Every body: first person. Never 'the SRE'." Explicit constraint. |
| C-04 Gap analysis 3 sections | E | **12** | Step 8: Documentation / Design / Operational gaps + Migration friction subsection. All three present with artifact refs. |
| C-05 Min ticket count gate | E | **6 (PARTIAL)** | TABLE CHECK gates at >= 6, not >= 7. Structural gate present but wrong minimum. |
| C-06 Phase target declared | R | **10** | Step 1 declares Phase 1/2/3 targets before any ticket. |
| C-07 Role-phase matrix | R | **10** | Step 3A Role-Phase Cross-Matrix with 5 role rows and phase constraints. |
| C-08 Migration framing | R | **10** | Step 1B Status Quo Analysis + Step 4 embodies prior-system knowledge. |
| C-09 Cross-ticket pattern table | A | **5** | Step 7 table present. |
| C-10 Resolution paths | A | **5** | Step 7B table for high-volume or P0/P1 tickets. |
| C-11 Phase as card field | A | **5** | `Phase: Phase N (day X-Y)` on metadata line. |
| C-12 Fallback-grounded severity | A | **5** | Step 2 "severity norm" + explicit override rule. Phase-anchored inference. |
| C-13 Mid-output verification | A | **5** | Step 9 dual-pass verification block. |
| C-14 Phase+Title coexistence | A | **5** | Both `Title:` and `Phase:` as named fields on same card. Step 9 Pass 2 checks both + "both fields present" line. |
| C-15 Temporal severity model | A | **0** | Still uses "norm" inference language with override path — not mechanical. |
| C-16 Prior-tool 4th check | A | **0** | No prior-tool citation count in Step 9. |
| **Total** | | **114/130** | |

**all_essential_pass:** FALSE (C-05 PARTIAL)

---

#### V-02 — Mechanical Severity (C-15 target)

| Criterion | Type | Score | Evidence |
|-----------|------|-------|---------|
| C-01 Title named field | E | **0 (FAIL)** | Card template: `## T-NN — {Title}` — Title embedded in heading, not as a named field. C-01 definition is violated: "A ticket ID does not satisfy this criterion." |
| C-02 Vocabulary declared | E | **12** | Present. |
| C-03 First-person voice | E | **12** | Step 4 constraint present. |
| C-04 Gap analysis 3 sections | E | **12** | Step 8 complete. |
| C-05 Min ticket count gate | E | **6 (PARTIAL)** | Gate at >= 6, not >= 7. |
| C-06–C-10 (same as V-01) | R+A | **35** | All present. |
| C-11 Phase as card field | A | **5** | `Phase: Phase N (day X-Y)` on metadata line. |
| C-12 Fallback-grounded severity | A | **5** | Day-window lookup supersedes fallback; grounded by phase position — intent satisfied. |
| C-13 Mid-output verification | A | **5** | Step 9 present. |
| C-14 Phase+Title coexistence | A | **0** | Title still embedded in heading. Phase present as named field but Title is not — they cannot coexist as named fields. |
| C-15 Temporal severity model | A | **5** | Day-window lookup table: Phase 1 → P2/P3, Phase 2 → P1/P2, Phase 3 → P0/P1. No override path. Step 9 has mechanical compliance check. |
| C-16 Prior-tool 4th check | A | **0** | No prior-tool citation count. |
| **Total** | | **102/130** | |

**all_essential_pass:** FALSE (C-01 FAIL, C-05 PARTIAL)

---

#### V-03 — Prior-Tool Citation Mandate (C-16 target)

| Criterion | Type | Score | Evidence |
|-----------|------|-------|---------|
| C-01 Title named field | E | **0 (FAIL)** | Card template still uses `## T-NN — {Title}`. Same displacement regression as V-02. |
| C-02 Vocabulary declared | E | **12** | Present; `Prior-tool ref?` column added to vocabulary table. |
| C-03 First-person voice | E | **12** | Step 4 constraint enhanced — "name the prior tool exactly" added. |
| C-04 Gap analysis 3 sections | E | **12** | Step 8 complete. |
| C-05 Min ticket count gate | E | **6 (PARTIAL)** | Gate at >= 6. |
| C-06–C-10 | R+A | **35** | All present. |
| C-11 Phase as card field | A | **5** | Present. |
| C-12 Fallback-grounded severity | A | **5** | Norm inference language retained. |
| C-13 Mid-output verification | A | **5** | Step 9 present. |
| C-14 Phase+Title coexistence | A | **0** | Title still in heading; coexistence not achieved. |
| C-15 Temporal severity model | A | **0** | Norm inference retained — not mechanical. |
| C-16 Prior-tool 4th check | A | **5** | Step 1B: "Prior tool exact name:"; vocabulary table: Prior-tool ref? column with ≥2 Y required; Step 9: citation count with PASS/FAIL gate. Full C-16 by construction. |
| **Total** | | **102/130** | |

**all_essential_pass:** FALSE (C-01 FAIL, C-05 PARTIAL)

---

#### V-04 — Card Template + Mechanical Severity (C-14 + C-15)

| Criterion | Type | Score | Evidence |
|-----------|------|-------|---------|
| C-01 Title named field | E | **12** | `## T-NN` heading + `- Title:` as named field. Both fields required, rule explicit. |
| C-02 Vocabulary declared | E | **12** | Present. |
| C-03 First-person voice | E | **12** | Step 4 constraint present. |
| C-04 Gap analysis 3 sections | E | **12** | Step 8 complete. |
| C-05 Min ticket count gate | E | **6 (PARTIAL)** | Gate at >= 6. |
| C-06–C-10 | R+A | **35** | All present. |
| C-11 Phase as card field | A | **5** | Present; `Phase: Phase N (day X-Y)` on metadata line. |
| C-12 Fallback-grounded severity | A | **5** | Day-window lookup satisfies intent. |
| C-13 Mid-output verification | A | **5** | Step 9 present. |
| C-14 Phase+Title coexistence | A | **5** | Both fields as named fields. Step 9 Pass 2 C-14 check block. Note: Phase field now explicitly described as "lookup key for severity" — coupling with C-15. |
| C-15 Temporal severity model | A | **5** | Day-window lookup, no override path. Step 9 mechanical compliance check. Step 2: "No override path exists." |
| C-16 Prior-tool 4th check | A | **0** | No prior-tool citation check. |
| **Total** | | **119/130** | |

**all_essential_pass:** FALSE (C-05 PARTIAL)

---

#### V-05 — Full Synthesis (R3 Golden Candidate)

| Criterion | Type | Score | Evidence |
|-----------|------|-------|---------|
| C-01 Title named field | E | **12** | `## T-NN` + `- Title:` as named field. Title rule + Phase rule both explicit. "Both fields are required. One does not satisfy the other." |
| C-02 Vocabulary declared | E | **12** | Controlled vocabulary + `Prior-tool ref?` column in vocabulary table. |
| C-03 First-person voice | E | **12** | Step 4: "Where migration-relevant: name the prior tool exactly as recorded in Step 1B." Voice constraint strengthened. |
| C-04 Gap analysis 3 sections | E | **12** | Step 8: all three sections with "specific page or guide name" / "specific design decision" / "runbook, alert, or dashboard" requirements. |
| C-05 Min ticket count gate | E | **6 (PARTIAL)** | TABLE CHECK gates at >= 6 and <= 12 — same as all other variants. |
| C-06 Phase target declared | R | **10** | Step 1 phase distribution upfront. |
| C-07 Role-phase matrix | R | **10** | Step 3A with all five role constraints. |
| C-08 Migration framing | R | **10** | Step 1B: "Prior tool exact name: ___" + migration window frame (Phase 1 = habit disruption, Phase 2 = hybrid, Phase 3 = committed or churned). Richest migration framing of all variants. |
| C-09 Cross-ticket pattern table | A | **5** | Step 7 present. |
| C-10 Resolution paths | A | **5** | Step 7B: "All three fields required per qualifying ticket." |
| C-11 Phase as card field | A | **5** | `Phase: Phase N (day X-Y)` on metadata line. Phase rule: "it is the lookup key for severity — if it is missing, the severity cannot be verified." |
| C-12 Fallback-grounded severity | A | **5** | Mechanical lookup satisfies phase-grounded severity intent. "not an estimate or a norm" makes grounding explicit. |
| C-13 Mid-output verification | A | **5** | Step 9 Triple-Pass Verification — elevated from dual-pass. |
| C-14 Phase+Title coexistence | A | **5** | Both as named fields on every card. Pass 3 dedicated C-14 block: counts Title fields, Phase fields, and "both fields present on same card" separately. |
| C-15 Temporal severity model | A | **5** | Day-window lookup. No override path. Pass 3: counts violations per window with PASS/FAIL. Step 2 explicit: "Severity is a mechanical output of the ticket's Phase window — not an estimate or a norm." |
| C-16 Prior-tool 4th check | A | **5** | Step 1B "Prior tool exact name:"; Step 5 vocabulary "Prior-tool ref?" column; Pass 3: "Ticket bodies containing that exact string: ___ of ___ (required: >= 2) PASS / FAIL". |
| **Total** | | **124/130** | |

**all_essential_pass:** FALSE (C-05 PARTIAL — gate at >= 6, not >= 7)

---

### Variation Rankings

| Rank | ID | Composite | Essential Pass | Key delta |
|------|-----|-----------|----------------|-----------|
| 1 | V-05 | 124/130 | FALSE (C-05) | All 3 R3 criteria + triple-pass verification |
| 2 | V-04 | 119/130 | FALSE (C-05) | C-14 + C-15; Phase field as severity lookup anchor |
| 3 | V-01 | 114/130 | FALSE (C-05) | C-14 only; inherits R2 severity language |
| 4 (tie) | V-02 | 102/130 | FALSE (C-01, C-05) | C-15 only; C-01 regression (Title in heading) |
| 4 (tie) | V-03 | 102/130 | FALSE (C-01, C-05) | C-16 only; C-01 regression (Title in heading) |

**Blocking gap (universal):** C-05 — all variants gate at `>= 6` instead of `>= 7`. Single-axis fix for R4: change TABLE CHECK and Step 1 minimum to `>= 7`.

---

### Excellence Signals from V-05

**E-01 — Phase field as dual-purpose structural anchor:** The `Phase: Phase N (day X-Y)` named field on the card satisfies C-14 (Phase+Title coexistence) AND is declared the explicit lookup key for C-15 mechanical severity. Step 2 says "The Phase field on the card is the lookup key — it is required, not decorative." Step 9 Pass 3 verifies both. One structural element closes two criteria by design.

**E-02 — Versioned verification pass accumulation:** V-05 elevates STEP 9 to "Triple-Pass Verification" — Pass 1 covers content traces, Pass 2 covers structural properties from R1/R2, Pass 3 covers all three R3 criteria as a dedicated block. This creates a versioned accumulation pattern: each rubric generation adds a pass rather than rewriting earlier ones. R4 can add Pass 4 without disturbing Pass 1–3.

**E-03 — Prior-tool name as end-to-end citation artifact:** Recording the prior tool's exact name once in Step 1B as a citation target (not just description), then tracking it as Y/N in the vocabulary table per ticket, then verifying the exact string count in Pass 3 creates traceable coverage from intent → planning → output → verification. The traceability chain is: `Step 1B declaration → Step 2C body template anchor → Step 4 persona instructions → Step 5 Y/N column → Pass 3 count`.

---

```json
{"top_score": 124, "all_essential_pass": false, "new_patterns": ["Phase named field as dual-purpose structural anchor: declaring Phase: on the card as the explicit lookup key for C-15 mechanical severity couples C-14 coexistence compliance with C-15 mechanical compliance into a single required field", "Versioned verification pass accumulation: elevating STEP 9 to Triple-Pass and isolating R3 criteria in Pass 3 creates a generation-stable structure where each rubric version adds a pass block without rewriting earlier ones", "Prior-tool exact name as end-to-end citation artifact: recording the prior tool name once in Step 1B as a lookup string, tracking Y/N per ticket in vocabulary table, and verifying exact string count in Pass 3 creates full traceability from intent declaration through output verification"]}
```
