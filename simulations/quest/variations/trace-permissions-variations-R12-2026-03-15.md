complete, independently readable) + Verification line. Inline concatenation of anchors fails C-24.*

**CA-1.1 — C-01:**
- Registry anchor — TABLE_1: [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1. CRITERION-PHASE-MAP declared target: PHASE 2 SE-1.
- Verification — TABLE_1 present at SE-1? Tier column? Every cell filled? All roles included? Evidence at declared phase? -> PASS / FAIL / PHASE-LATE

**CA-1.2 — C-02:**
- Registry anchor — TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.
- Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2. CRITERION-PHASE-MAP declared target: PHASE 2 SE-2.
- Verification — TABLE_2 present at SE-2? All sensitive fields? Null case stated? Gap? YES rows in TABLE_5 with provenance? Evidence at declared phase? -> PASS / FAIL / PHASE-LATE

**CA-1.3 — C-03:**
- Registry anchor — TABLE_3: [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.
- Preamble anchor — C-03: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3. CRITERION-PHASE-MAP declared target: PHASE 2 SE-0 + SE-3.
- Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled? Tier populated? Evidence spans SE-0 and SE-3 as declared? -> PASS / FAIL / PHASE-LATE

**CA-1.4 — C-04:**
- Registry anchor — TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES, Finding never blank.
- Preamble anchor — C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4. CRITERION-PHASE-MAP declared target: PHASE 2 SE-0.
- Verification — TABLE_4 present at SE-0 (before SE-1)? All four vectors? Checked? = YES? Specific findings or rule-outs? Evidence at declared phase (not deferred past SE-0)? -> PASS / FAIL / PHASE-LATE

**CA-1.5 — C-05:**
- Registry anchor — TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation, Source Table, Source Row, Discovery Phase] — blank cells prohibited globally.
- Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5. CRITERION-PHASE-MAP declared target: PHASE 2 SE-5.
- Verification — TABLE_5 substantively populated? Named gap with specific field/role/rule? Provenance columns present on all rows? -> PASS / FAIL / PHASE-LATE

**CA-1.6 — SHALL-F three-field Remediation:**
- Registry anchor — TABLE_5 CS-EXPECTATION-VIOLATED Remediation block: CS-Expected / SE-Actual / Delta — all three required per SHALL-F declaration in Phase 0.
- Preamble anchor — SHALL-F: CONTRADICTED rows MUST carry complete three-field block. Incomplete rows MUST be reopened.
- Verification — Each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta carries exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G exact-label two-part blocks:**
- Registry anchor — CONTEXT section exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2), "Blind spot 2 — Cumulative privilege blind spot" (SE-1 + SE-3), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4). SHALL-G requires `MANUAL GAP [<exact label>]:` then `STRUCTURED CLOSE:`.
- Preamble anchor — SHALL-G: Line 1 `MANUAL GAP [<exact CONTEXT label>]:`; character-for-character match required; paraphrase or abbreviation fails.
- Verification — SE-1 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-0 Schema Registry acknowledgment:**
- Registry anchor — Schema Registry at Step 0.1: CS-2 declared with SE-updatable columns SE Cross-Reference and SE Confirmation and named SE-update protocol. CS-3 declared with SE-updatable columns SE Cross-Reference and SE Confirmation and named SE-update protocol.
- Preamble anchor — CS-0 MUST precede CS-1/CS-2/CS-3. CS-0 cites CS-2 and CS-3 by exact Schema ID label and lists SE-updatable columns for each.
- Verification — CS-0 present? Precedes CS-1? Cites Schema ID CS-2? Cites Schema ID CS-3? Lists SE-updatable columns for each? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA-1.9 — C-33 ANTI-PATTERN FIRING AUDIT:**
- Registry anchor — ANTI-PATTERN REGISTRY (Phase 0): AP-1 → FLS-BLIND-SPOT-RESOLVED → SE-2; AP-2 → PRIV-ACCUMULATION-RESOLVED → SE-1+SE-3; AP-3 → OWD-OVERRIDE-RESOLVED → SE-4. Two-endpoint execution record: Phase 0 declares identifiers and reactive markers; CA-1.9 closes with FIRED / NOT-FIRED.
- Preamble anchor — C-33: CA-1 FIRING AUDIT must close every declared AP-identifier. NOT-FIRED verdict without naming the exact SE section where the marker was expected = structural gap.
- Audit:

| AP-ID | Reactive Marker Token | Assigned Section | FIRED? | SE Location (if FIRED) / Expected Section (if NOT-FIRED) |
|-------|----------------------|-----------------|--------|----------------------------------------------------------|
| AP-1 | FLS-BLIND-SPOT-RESOLVED | SE-2 | [FIRED / NOT-FIRED] | |
| AP-2 | PRIV-ACCUMULATION-RESOLVED | SE-1 + SE-3 | [FIRED / NOT-FIRED] | |
| AP-3 | OWD-OVERRIDE-RESOLVED | SE-4 | [FIRED / NOT-FIRED] | |

- Verdict — All three AP-IDs carry FIRED? NOT-FIRED without naming exact SE section = fail. -> FIRING AUDIT: PASS / FAIL

**CA-1.10 — C-34 SOURCE-LINK AUDIT:**
- Registry anchor — TABLE_5 provenance columns declared at Step 0.1: Source Table / Source Row / Discovery Phase. Pattern: `PHASE 2 SE-N`. Non-conforming Discovery Phase = deferred-registration violation detectable by column scan without reading SE prose.
- Preamble anchor — SHALL-H: every TABLE_5 row carries all three provenance columns. Discovery Phase = `PHASE 2 SE-N`. CA-1.10 SOURCE-LINK AUDIT verifies.
- Audit — For each TABLE_5 row: (a) Discovery Phase matches `PHASE 2 SE-N` pattern? (b) Source Table references a valid source table? (c) Source Row populated with a row number?
- Verdict — All rows conform? No blank provenance cells? No Discovery Phase outside pattern? -> SOURCE-LINK AUDIT: PASS / FAIL [on FAIL: name TABLE_5 row number and non-conforming value]

**CA-1.11 — C-35 CRITERION-PHASE-MAP PHASE-LATE audit:**
- Registry anchor — CRITERION-PHASE-MAP at Step 0.3, Phase 0. Declared targets: C-01 → SE-1, C-02 → SE-2, C-03 → SE-0+SE-3, C-04 → SE-0, C-05 → SE-5. PHASE-LATE fires when criterion evidence first appears later than declared.
- Preamble anchor — C-35: PHASE-LATE is a third terminal verdict alongside PASS / FAIL. PHASE-LATE verdict names declared phase and actual phase.
- Verification per criterion:
  - C-01: TABLE_1 first complete at SE-1 (declared SE-1). -> PASS / FAIL / PHASE-LATE [if PHASE-LATE: declared PHASE 2 SE-1, actual PHASE 2 SE-N]
  - C-02: TABLE_2 first complete at SE-2 (declared SE-2). -> PASS / FAIL / PHASE-LATE
  - C-03: TABLE_3 evidence spans SE-0 and SE-3 (declared SE-0+SE-3). -> PASS / FAIL / PHASE-LATE
  - C-04: TABLE_4 first complete at SE-0 before TABLE_1 (declared SE-0). -> PASS / FAIL / PHASE-LATE
  - C-05: TABLE_5 substantively populated at SE-5 (declared SE-5; inline accumulation throughout is expected and does not trigger PHASE-LATE). -> PASS / FAIL / PHASE-LATE

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored ANTI-PATTERN REGISTRY (Phase 0), Schema Registry Step 0.1, preamble Step 0.2, CRITERION-PHASE-MAP Step 0.3.
[C-01–C-05 (CA-1.1–CA-1.5, with PHASE-LATE states). SHALL-F (CA-1.6). SHALL-G exact-label blocks (CA-1.7). CS-0 Registry acknowledgment (CA-1.8). C-33 AP FIRING AUDIT (CA-1.9). C-34 SOURCE-LINK AUDIT (CA-1.10). C-35 CRITERION-PHASE-MAP PHASE-LATE audit (CA-1.11). Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

*End of Round 12 variations. V-01 through V-05 are complete, standalone, runnable prompt bodies.*
