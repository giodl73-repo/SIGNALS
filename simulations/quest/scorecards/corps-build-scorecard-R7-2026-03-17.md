# corps-build Scorecard — Round 7 (2026-03-17)

**Rubric**: v5 | **Max**: 155 | **Golden threshold**: 128 (all 5 essential + composite)

---

## Per-Criterion Evaluation

### Essential (12 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Role file completeness | PASS | PASS | PASS | PASS | PASS |
| C-02 | org-chart.md ASCII hierarchy | PASS | PASS | PASS | PASS | PASS |
| C-03 | Inertia Advocate in every team | PASS | PASS | PASS | PASS | PASS |
| C-04 | org.yaml structural fidelity | PASS | PASS | PASS | PASS | PASS |
| C-05 | Role file typed fields present | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**
- **C-01**: CROSS-REF checks `org.yaml slots: [n], files written: [n] — [MATCH|MISMATCH]` + `table fidelity: ARTIFACT-A Total [n] = ROLES-COMPLETE [n]` in all five. Verification mechanism is concrete and bilateral. V-05 also adds `dir check` listing all subdirs vs parse manifest.
- **C-02**: Step 8a explicitly states `+--` / `|`, "all names verbatim from org.yaml," "minimum two nesting levels visible," "every area from PARSE manifest must appear" across all variations.
- **C-03**: IA-WRITTEN per file with rewrite-on-NO, then IA-PHASE-COMPLETE gate before WRITE-ROLES begins. V-02/V-04/V-05 add a fourth IA-WRITTEN check that also enforces this.
- **C-04**: `.roles/{area-slug}/{role-slug}.md` path pattern explicit; VALIDATE checks area slug uniqueness; CROSS-REF dir check confirms subdirs match parse manifest slugs. V-05 adds STRUCTURAL-ERROR:IA-OUT-OF-ORDER.
- **C-05**: All five fields (orientation, lens, expertise, scope, collaboration-pattern) with substantive non-"TBD" body required in all variations; non-empty enforced by IA-WRITTEN checks and ROLES-COMPLETE gate.

Essential subtotals: **60 / 60** for all five variations.

---

### Recommended (10 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Headcount by group table + levels | PASS | PASS | PASS | PASS | PASS |
| C-07 | Standard vs specialized distinction | PASS | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-08 | AMEND section with three options | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**
- **C-06**: ARTIFACT-A schema `| Area | Standard | Specialized | Inertia-Adv | Total | Levels |` with explicit IA count column and `**Total**` footer row present in all variations.
- **C-07**: V-01 and V-05 state "Specialized roles... F-2 (lens) and F-3 (expertise) must name domain-specific systems that distinguish this role from the standard roles on the same team; a specialized lens identical to any standard lens on the same team fails distinctness and requires rewrite." V-02/V-03/V-04 WRITE-ROLES sections say only "standard then specialized, five non-empty fields" — sequence is stated but distinctness is not enforced. PARTIAL.
- **C-08**: All five AMEND sections have `--area`, `--levels`, `--restructure` with area option referencing IA-WRITTEN re-run (invariant re-checks). V-02/V-04/V-05 explicitly include "all four checks including non-transplantable" in the area regeneration option.

Recommended subtotals: V-01 = **30**, V-02 = **25**, V-03 = **25**, V-04 = **25**, V-05 = **30**

---

### Aspirational (5 pts each, PARTIAL = 2.5)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | IA team-contextualized | PASS | PASS | PARTIAL | PASS | PASS |
| C-10 | Cross-reference integrity chart/roles | PASS | PASS | PASS | PASS | PASS |
| C-11 | Named invariants block | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |
| C-12 | Auditable check-output | PASS | PASS | PASS | PASS | PASS |
| C-13 | Named failure modes per criterion | PASS | PASS | PARTIAL | PASS | PASS |
| C-14 | Dedicated pre-step FAILURE MODES block | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |
| C-15 | Named CHECK-OUTPUT PROTOCOL section | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |
| C-16 | Phase-exit guard tokens | PASS | PASS | PASS | PASS | PASS |
| C-17 | Per-artifact TRANSCRIPTION-RECEIPT | PASS | PASS | PASS | PASS | PASS |
| C-18 | BUILD-VERIFY single-purpose phase | PASS | PASS | PASS | PASS | PASS |
| C-19 | TRANSCRIPTION-RECEIPT in-phase remediation | PASS | PARTIAL | PASS | PARTIAL | PASS |
| C-20 | BUILD-VERIFY exclusion manifest | PASS | PASS | PASS | PASS | PASS |
| C-21 | TRANSCRIPTION-CLEAR all-artifact re-audit | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**
- **C-09**: V-02/V-04/V-05 earn PASS via named failure mode: "Any change to the existing architecture risks disrupting the team's current workflow" explicitly marked as transplantable (fail). V-03 has PROFILE domain enforcement but no named failure mode example. V-01 enforces domain vocabulary via PROFILE quality gate; no named failure mode example but DERIVATION-LOOP-CLOSED confirms chain. Scoring V-01 PASS (chain confirmed) vs V-03 PARTIAL (no example).
- **C-11**: V-03 and V-05 earn PASS via typed STRUCTURAL-ERROR code tables functioning as named, enumerable, binary invariants (STRUCTURAL-ERROR:PHASE-2-FILE-WRITE, BV-FILE-WRITE, etc.) — each entry is present/absent, machine-matchable by name. V-01/V-02/V-04 have distributed yes/no checks (IA-WRITTEN, VALIDATE) but no single named block. PARTIAL.
- **C-13**: V-03 PROFILE section only states "failure mode: defended-artifact names a category -> rewrite" — no named transplantable example. V-01/V-02/V-04/V-05 all name concrete failure examples. V-05 gives the most: category-naming failure (e.g., "the existing pipeline architecture" vs "the event-resequencing buffer...") plus transplantable lens example.
- **C-14**: V-03 and V-05 earn PASS via STRUCTURAL-ERROR codes placed at phase entry (before phase content begins): STRUCTURAL-ERROR:PHASE-2-FILE-WRITE at VALIDATE start, STRUCTURAL-ERROR:CONTRACT-FILE-WRITE and CONTRACT-RECALC at CONTRACT start, STRUCTURAL-ERROR:WRITE-CHART-RECALC/SPURIOUS-CLEAR/PREMATURE-EXIT at WRITE-CHART. V-01/V-02/V-04 lack these pre-step declarations.
- **C-15**: V-03 and V-05 have named protocol structures (EXCLUSION-MANIFEST table with typed error codes, named PATH-A/PATH-B output shapes). V-01/V-02/V-04 have named emit blocks but no dedicated protocol section label.
- **C-19**: V-01 explicitly states "A REVISED verdict may not remain outstanding when this phase closes." V-03 and V-05 add STRUCTURAL-ERROR:WRITE-CHART-PREMATURE-EXIT as a named error for emitting CHART-WRITTEN before TRANSCRIPTION-CLEAR. V-02 and V-04 describe the remediation loop but do not state "phase cannot close with REVISED outstanding." PARTIAL.
- **C-20**: All earn PASS. V-01 has prose "SINGLE-PURPOSE GATE -- The following are NOT outputs" list. V-02/V-04 have "EXCLUSION MANIFEST -- NOT outputs of this phase (presence is a build error)" bullet list. V-03/V-05 have typed EXCLUSION-MANIFEST table with error codes per excluded type (highest fidelity).
- **C-21**: All have TRANSCRIPTION-CLEAR block naming A, B, C individually. V-05 adds "it must name A, B, and C individually, including those VERBATIM before any rewrite" — addresses the pre-existing VERBATIM case explicitly. V-03 adds "A TRANSCRIPTION-CLEAR naming fewer than three artifacts is structurally incomplete."

Aspirational subtotals:
- V-01: 5+5+2.5+5+5+2.5+2.5+5+5+5+5+5+5 = **62.5**
- V-02: 5+5+2.5+5+5+2.5+2.5+5+5+5+2.5+5+5 = **60**
- V-03: 2.5+5+5+5+2.5+5+5+5+5+5+5+5+5 = **65**
- V-04: 5+5+2.5+5+5+2.5+2.5+5+5+5+2.5+5+5 = **60**
- V-05: 5+5+5+5+5+5+5+5+5+5+5+5+5 = **65**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-01 | 60 | 30 | 62.5 | **152.5** | YES |
| V-02 | 60 | 25 | 60 | **145** | YES |
| V-03 | 60 | 25 | 65 | **150** | YES |
| V-04 | 60 | 25 | 60 | **145** | YES |
| V-05 | 60 | 30 | 65 | **155** | YES (MAX) |

All five variations achieve golden (>= 128, all 5 essential PASS). V-05 achieves the theoretical maximum of 155.

---

## Variation Ranking

1. **V-05 — 155/155** — Full integration: DERIVATION-LOOP-CLOSED + non-transplantable gate + typed error taxonomy + complete baseline architecture
2. **V-01 — 152.5/155** — DERIVATION-LOOP-CLOSED alone; earns C-07 via specialized distinctness enforcement; loses 2.5 on C-11/C-14/C-15 for lacking typed error codes
3. **V-03 — 150/155** — Typed error taxonomy earns C-11/C-14/C-15 PASS; loses 5 on C-07 (no specialized distinctness), 2.5 on C-09/C-13 (no named transplantable failure mode)
4. **V-02 — 145/155** — Non-transplantable gate with named failure modes; misses C-07 distinctness, C-14/C-15 (no typed error codes), C-19 explicit "phase cannot close" language
5. **V-04 — 145/155** — Combines V-01 + V-02 but inherits V-02's weaknesses (no typed error codes); loses C-07 despite being the combination

---

## Excellence Signals (V-05)

Three patterns drove V-05 to maximum score:

**(++) C-22 primary: DERIVATION-LOOP-CLOSED as a named structural event**
After BUILD-VERIFY-COMPLETE, a dedicated block emits one line per team: `[team name]: PROFILE lens-phrase "[phrase]" -> IA lens opens "[phrase]" -- CLOSED`. The block closes with "Each resistance profile is fully recoverable from the built IA file's lens opening." This is not just a verification — it's a structural record. The derivation chain is no longer a rule that happens to be satisfied; it is a named, timestamped event in the phase output recoverable after the fact.

**(++) C-23 primary: Non-transplantable IA per-file gate with named examples**
The 4th IA-WRITTEN check `lens-team-specific (non-transplantable)` is a hard build gate. NO halts the build. Two named examples bracket the criterion: transplantable fail ("Any change to the existing architecture risks disrupting the team's current workflow" — applies to any team verbatim) vs team-specific pass ("The claim routing table's 847 active rule entries were audited manually every quarter because no automated validation existed" — cannot be transplanted without rewriting). This converts a quality aspiration into a binary structural enforcement.

**(++) C-24 candidate: Full per-team derivation audit trail**
V-05 is the only variation where the complete chain `PROFILE -> IA-WRITTEN non-transplantable YES -> BUILD-VERIFY VERBATIM -> DERIVATION-LOOP-CLOSED` is explicit and unbroken. Each team has: a profiled resistance context (PHASE 5) → a per-file write-time non-transplantability check (PHASE 6) → a BUILD-VERIFY lens comparison (PHASE 9) → a named CLOSED derivation record (PHASE 9). A reader can reconstruct the entire derivation story for any team from the phase output alone, without access to org.yaml or internal state.

**Structural error taxonomy as named invariants (C-11 lift):**
V-05 places STRUCTURAL-ERROR:X codes at the entry of every phase where out-of-scope behavior is most likely (VALIDATE, CONTRACT, WRITE-IA, WRITE-CHART, BUILD-VERIFY). Each code is a binary: present = build error, absent = compliant. The EXCLUSION-MANIFEST table in BUILD-VERIFY is the most complete expression: 6 error codes in a two-column table. This is the first variation where named invariants exist as a cross-phase taxonomy, not just per-phase checks.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": ["DERIVATION-LOOP-CLOSED: named per-team block emitted after BUILD-VERIFY-COMPLETE recording PROFILE lens-phrase -> IA lens opens -> CLOSED for every team; makes derivation recoverable from output alone without access to org.yaml (C-22 candidate)", "lens-team-specific (non-transplantable) as 4th IA-WRITTEN binary gate: NO verdict halts build before next team; named transplantable fail and team-specific pass examples anchor the criterion as a structural enforcement rather than a quality aspiration (C-23 candidate)", "Full per-team derivation audit trail: unbroken chain PROFILE -> IA-WRITTEN non-transplantable YES -> BUILD-VERIFY VERBATIM -> DERIVATION-LOOP-CLOSED makes each IA's complete derivation history recoverable from phase output alone (C-24 candidate)"]}
```
