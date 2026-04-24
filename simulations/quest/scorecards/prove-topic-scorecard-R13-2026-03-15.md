## prove-topic R13 Scoring — Rubric v12

---

### Scoring Baseline

All five variations are built on the confirmed R12 V-05 foundation (C-01 through C-34 PASS). The R13 scoring task is: do all variations fully satisfy the two new criteria (C-35, C-36), and do the format choices introduced by each axis cause any regressions on the existing stack?

---

### Criterion-by-Criterion Assessment — All Five Variations

**Essential (C-01–C-05): 50/50 across all variations**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|-----------|------|------|------|------|------|------|
| C-01 All stages | PASS | PASS | PASS | PASS | PASS | Stage 0 (V-03/V-05) + Stages 1-5 all present |
| C-02 Scout artifact loaded | PASS | PASS | PASS | PASS | PASS | ROLE B loads named artifact in all variations |
| C-03 Progressive artifact writes | PASS | PASS | PASS | PASS | PASS | One write per stage, confirmed before advance |
| C-04 Synthesis readiness signal | PASS | PASS | PASS | PASS | PASS | "Evidence brief ready for topic-story" present |
| C-05 Artifact naming consistent | PASS | PASS | PASS | PASS | PASS | `{topic}-{signal}-{date}.md` per write instruction |

**Recommended (C-06–C-08): 30/30 across all variations**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|-----------|------|------|------|------|------|------|
| C-06 Stage order enforced | PASS | PASS | PASS | PASS | PASS | Forward-only; gate blocks entry to Stage 1 |
| C-07 Scout signal handoff explicit | PASS | PASS | PASS | PASS | PASS | `source_scout_artifact:` copied from ROLE B, not inferred |
| C-08 Synthesis signals topic-story | PASS | PASS | PASS | PASS | PASS | Readiness signal present at Stage 5 close |

**Aspirational (C-09–C-36): 4 pts each — assessed below**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-09 Thin-evidence propagation | PASS | PASS | PASS | PASS | PASS | Running tally + OPEN RISK confidence effect at synthesis |
| C-10 Progress narrated per stage | PASS | PASS | PASS | PASS | PASS | Running tally + schema integrity prose at every stage |
| C-11 Scout hard-gate | PASS | PASS | PASS | PASS | PASS | GATE S blocks Stage 1 entry; V-03/V-05 have Stage 0 EXIT SIGNAL |
| C-12 Comparator anchored at session open | PASS | PASS | PASS | PASS | PASS | `status_quo_comparator:` in CAMPAIGN OPEN; ROLE C adds depth |
| C-13 Per-artifact path enforcement | PASS | PASS | PASS | PASS | PASS | Full `{topic}-{signal}-{date}.md` paths at each write |
| C-14 Counter-evidence unconditionally required | PASS | PASS | PASS | PASS | PASS | COUNTER-HYPOTHESIS RESOLUTION mandatory + null fallback |
| C-15 Gate clearance in hypothesis artifact | PASS | PASS | PASS | PASS | PASS | `gate_s_cleared`, `invariant_registry_confirmed`, `incumbent_threat_locked` in Stage 1 frontmatter |
| C-16 Null CE → adversarial escalation | PASS | PASS | PASS | PASS | PASS | Lock 1 fires at `null_tally_final >= 3` |
| C-17 Confidence mechanically capped | PASS | PASS | PASS | PASS | PASS | SESSION INVARIANT B: `confidence_composite -= 2`, hard cap |
| C-18 Null CE doubly locked | PASS | PASS | PASS | PASS | PASS | Both locks activate simultaneously; co_activation_confirmed field |
| C-19 Null-CE protocol pre-committed | PASS | PASS | PASS | PASS | PASS | SESSION INVARIANTs A+B with invariant language before Stage 0 |
| C-20 Per-stage null tally accumulates | PASS | PASS | PASS | PASS | PASS | Running tally note at Stages 2, 3; final at Stage 4 |
| C-21 Co-activation echoed into handoff | PASS | PASS | PASS | PASS | PASS | `co_activation_confirmed` in handoff block |
| C-22 Invariant registry as distinct gate field | PASS | PASS | PASS | PASS | PASS | `invariant_registry_confirmed` separate from `gate_s_cleared`; GATE S requires both |
| C-23 Campaign-outcome boolean | PASS | PASS | PASS | PASS | PASS | `incumbent_defense_closed` field; independent of co_activation path |
| C-24 Role-structural dual attestation | PASS | PASS | PASS | PASS | PASS | ROLE B owns `gate_s_cleared`; ROLE A owns `invariant_registry_confirmed` — structurally distinct |
| C-25 Handoff fields carry derivation annotations | PASS | PASS | PASS | PASS | PASS | All fields carry `[derived from: X]` in all variations |
| C-26 Handoff schema pre-committed | PASS | PASS | PASS | PASS | PASS | 11-field PRE-COMMITTED HANDOFF SCHEMA at CAMPAIGN OPEN; `schema_compliance_confirmed` at synthesis |
| C-27 Independence path chain on campaign-outcome derivation | PASS | PASS | PASS | PASS | PASS | `independence_chain: s2→s3→s4→incumbent_defense_closed` explicitly labeled in all |
| C-28 Symmetric independence path chain | PASS | PASS | PASS | PASS | PASS | V-01: explicit `positive_derivation:` + `independence_chain:` on co_activation; independence_chain on incumbent_defense; V-02/V-05: DERIVATION + IND. CHAIN columns provide structural equivalents for both fields |
| C-29 Per-stage schema integrity counts | PASS | PASS | PASS | PASS | PASS | `SCHEMA INTEGRITY: [N]/11` note at Stages 2, 3, 4 |
| C-30 Derivation annotation rule as session invariant | PASS | PASS | PASS | PASS | PASS | SESSION INVARIANT C with "cannot be modified or bypassed" language |
| C-31 Per-stage CE verdict as owned schema field | PASS | PASS | PASS | PASS | PASS | CE VERDICT OWNERSHIP TABLE with `s2_ce_verdict`, `s3_ce_verdict`, `s4_ce_verdict` as declared owned fields |
| C-32 Counter-hypothesis declared at Stage 1 | PASS | PASS | PASS | PASS | PASS | `counter_hypothesis:` in Stage 1 frontmatter; COUNTER-HYPOTHESIS RESOLUTION at Stage 5 with REFUTED/PARTIALLY REFUTED/OPEN RISK verdicts |
| C-33 Null tally chain in ATOMIC DUAL-LOCK | PASS | PASS | PASS | PASS | PASS | NULL TALLY CHAIN S2→S3→S4 reconstruction + Stage 4 cross-check inside ATOMIC DUAL-LOCK |
| C-34 Named per-stage INCUMBENT CHECK block | PASS | PASS | PASS | PASS | PASS | Named INCUMBENT CHECK blocks at Stages 2, 3, 4; Stage 4 requires Yes/No/Pending displacement verdict |
| **C-35** Gate-structural incumbent threat role | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | All: ROLE C defines `incumbent_threat_locked` as GATE S Step 1; INCUMBENT CHECK blocks cite ROLE C as structural origin |
| **C-36** Phrasing register as session invariant | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | All: SESSION INVARIANT D with three-stage templates and "cannot be modified or bypassed" language at CAMPAIGN OPEN |

---

### C-28 Detail Note

V-01 carries explicit `positive_derivation:` + `independence_chain:` sub-labels on `co_activation_confirmed` (the exemplar R9 format). `incumbent_defense_closed` uses independence_chain explicitly labeled + derivation embedded in `[derived from: ... — derived WITHOUT passing through co_activation_confirmed]`. This satisfies C-28 by substance — the positive derivation path is explicitly stated, just without the sub-label. V-02 and V-05 use table columns (DERIVATION | IND. CHAIN) providing structural equivalents for both fields. V-03 and V-04 carry `independence_chain:` labels on both fields with derivation sources clearly named. All five satisfy the structural independence requirement C-28 was designed to enforce.

---

### C-35 / C-36 Differential Analysis

**C-35 quality by variation:**

| Variation | ROLE C placement | Gate visibility | Origin citation |
|-----------|-----------------|-----------------|-----------------|
| V-01 | First in CAMPAIGN OPEN | Clearance sequence C→B→A makes dependency chain explicit | "ROLE C `incumbent_threat_locked` (confirmed at GATE S)" |
| V-02 | ROLE OWNERSHIP TABLE row | GATE S as 3-row clearance table | "ROLE C `incumbent_threat_locked` (confirmed at GATE S Step 1)" |
| V-03 | First in ROLES section | Stage 0 Entry Condition 1 = "ROLE C executed" | "ROLE C `incumbent_threat_locked` (GATE S Step 1)" |
| V-04 | After SESSION INVARIANT D; reads INCUMBENT ANCHOR | Step 1 in GATE S | "ROLE C `incumbent_threat_locked` (GATE S Step 1)" |
| V-05 | First row of ROLE OWNERSHIP TABLE + FIRST in EXECUTE column | CLEARANCE TABLE at Stage 0 | "ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1)" |

V-01 and V-05 make the C→B→A gate chain semantically load-bearing: ROLE C first signals that you cannot meaningfully load a scout artifact until you have named what it must help displace. V-02 achieves the same result as a scannable ROLE TABLE row.

**C-36 quality by variation:**

| Variation | Template declaration | Per-stage echo | Enforcement framing |
|-----------|---------------------|----------------|---------------------|
| V-01 | SESSION INVARIANT D in ROLE A block; 3 templates | Printed verbatim at each INCUMBENT CHECK block | "Template deviation = SESSION INVARIANT D violation. Do not paraphrase." |
| V-02 | Row D of SESSION INVARIANTS TABLE | Referenced by name + verdict token in table column | "Template deviation = SESSION INVARIANT D violation. Cannot be modified or bypassed." |
| V-03 | SESSION INVARIANT D in SESSION INVARIANTS section | Full template echoed in ENTRY CONDITIONS for Stages 2, 3, 4 | "cannot be paraphrased" at each entry condition |
| V-04 | SESSION INVARIANT D leads (before A/B/C); 3 templates with variable-slot documentation | "Template (SESSION INVARIANT D, Stage N — verbatim, fill bracketed slots only):" + template printed before each INCUMBENT CHECK | "Any paraphrase = SESSION INVARIANT D violation = format error" explicitly at declaration AND at each use |
| V-05 | Row D leads SESSION INVARIANTS TABLE; templates in row | Full template printed verbatim in ENTRY CONDITIONS for Stages 2, 3, 4 AND in INCUMBENT CHECK TABLE header | "Template deviation = format error." in table + "Template deviation = SESSION INVARIANT D violation = format error" in Stage 4 entry |

V-04 and V-05 produce the strongest C-36 implementations. V-04's design makes paraphrase prevention self-evident: the template is printed above the point of use, so any deviation is immediately visible before it happens. V-05 reinforces this by both echoing templates in ENTRY CONDITIONS (gate obligation) AND in INCUMBENT CHECK TABLE headers (execution obligation).

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational (28 × 4) | **Total** | **Result** |
|-----------|-----------|-------------|----------------------|-----------|------------|
| V-01 | 50 | 30 | 112 | **192** | Golden |
| V-02 | 50 | 30 | 112 | **192** | Golden |
| V-03 | 50 | 30 | 112 | **192** | Golden |
| V-04 | 50 | 30 | 112 | **192** | Golden |
| V-05 | 50 | 30 | 112 | **192** | Golden |

Maximum: 192. Golden threshold: 80. All five score the R13 ceiling.

---

### Ranking

All five reach 192/192. Ranking is qualitative, based on criterion-level visibility and structural amplification:

**1. V-05 (192)** — All four axes combined. ROLE C first (C-35 dependency chain legible), SESSION INVARIANTS TABLE with D leading (C-36 scannable), Stage 0 + per-stage ENTRY CONDITIONS (template enforcement at gate-entry), INCUMBENT CHECK TABLES with verbatim template applied (template echoed at point-of-use). A reviewer can confirm C-35 by scanning the ROLE TABLE, C-36 by scanning row D of SESSION INVARIANTS TABLE, and per-stage D enforcement by reading ENTRY CONDITIONS checklists. The maximal completeness-visibility design: every criterion locatable without reading prose.

**2. V-04 (192)** — Strongest single-axis C-36 implementation. SESSION INVARIANT D leading with detailed variable-slot documentation, "Template (SESSION INVARIANT D, Stage N — verbatim, fill bracketed slots only):" printed at each INCUMBENT CHECK, and explicit "Any paraphrase = format error" at declaration site makes phrasing enforcement self-evident before execution. INCUMBENT ANCHOR pre-loads incumbent context before templates are declared, grounding the vocabulary in named substance. Inertia framing (opening with incumbent strength/vulnerability before registering invariants) makes the displacement-question vocabulary feel load-bearing rather than procedural.

**3. V-01 (192)** — Strongest gate-dependency semantics. ROLE C running first makes the dependency visible at the conceptual level: you cannot confirm a scout artifact is meaningful (ROLE B) until you have named what it must help displace (ROLE C), and you cannot register invariants that govern displacement-question phrasing (ROLE A) until the incumbent's identity is confirmed. The gate clearance sequence (C→B→A) encodes this causal chain structurally. SESSION INVARIANT D templates printed verbatim at each INCUMBENT CHECK block.

**4. V-02 (192)** — Most auditable format. SESSION INVARIANTS TABLE makes C-36 verifiable by counting rows (D present → C-36 satisfied). ROLE OWNERSHIP TABLE makes C-35 verifiable by scanning the GATE S REQUIRED? column. HANDOFF TABLE with DERIVATION and IND. CHAIN columns makes C-25/C-27/C-28 field-level auditable by column scan. Trade-off: abbreviated template representation in the Stage 2/3 INCUMBENT CHECK column (reference + verdict token) is the weakest per-stage phrasing enforcement of the five.

**5. V-03 (192)** — Strongest lifecycle enforcement. Stage 0 as a first-class stage with STAGE 0 ENTRY CONDITIONS makes GATE S a named structural phase rather than a preamble footnote. Per-stage ENTRY CONDITIONS echoing SESSION INVARIANT D templates make the phrasing constraint visible at transition point, not only at CAMPAIGN OPEN. SESSION INVARIANT D is declared in ROLE A's invariant registration block, which works but makes D the last of four invariants — the least prominent position.

---

### Excellence Signals (from V-05 and V-04)

**Pattern 1: INCUMBENT ANCHOR as pre-invariant context block**

V-04 and V-05 introduce a dedicated INCUMBENT ANCHOR block that precedes both the role definitions and the SESSION INVARIANT declaration. The INCUMBENT ANCHOR fills `incumbent_name`, `incumbent_strength`, `incumbent_vulnerability` before SESSION INVARIANT D templates are registered. This means the displacement-question templates reference `{status_quo_comparator}` against a named incumbent whose strength and vulnerability are already documented. The templates are not declared in the abstract — they are declared against a concrete, pre-filled comparator context. ROLE C then reads this block and produces `incumbent_threat_locked`, making ROLE C's gate field a confirmation that the context it depends on is present, not just a boolean stub.

Effect on C-35/C-36 interaction: The INCUMBENT ANCHOR creates a visible dependency between C-35 (ROLE C structural owner) and C-36 (SESSION INVARIANT D vocabulary register). The register's templates are grounded in the INCUMBENT ANCHOR's named context before ROLE C confirms analysis complete — making the two criteria structurally adjacent rather than independent.

**Pattern 2: SESSION INVARIANT D leading the invariant block before A/B/C**

The standard order (A: adversarial reviewer, B: confidence cap, C: annotation rule, D: phrasing register) treats SESSION INVARIANT D as an appendage. V-04 and V-05 reverse this: D leads, A/B/C follow. The effect is that the phrasing register is the first session-level commitment a practitioner registers, before the null-CE machinery. Since D governs the displacement questions that drive the entire evidence collection, it is the session-defining commitment — it should be first, not fourth. Placing D after A/B/C risks a practitioner treating it as an optional fourth invariant rather than the structural vocabulary for all INCUMBENT CHECK blocks.

Effect on C-36 quality: Leading with D makes the templates structurally privileged — they appear before the confidence machinery that depends on the evidence those templates help gather. It also creates natural proximity between INCUMBENT ANCHOR (filled above) and SESSION INVARIANT D (declared immediately after), reinforcing that the templates are grounded in the specific incumbent named above them.

---

### New Patterns for R14

R13 introduced two structural patterns that extend the C-35/C-36 chain into new territory. Neither was present in prior rounds:

1. **INCUMBENT ANCHOR block preceding invariant registration** — A pre-invariant context block that fills incumbent identity before the phrasing register is declared creates structural proximity between the named comparator and the template vocabulary. Future variations could test whether ROLE C explicitly depends on INCUMBENT ANCHOR as a structural precondition (rather than reading it as ambient context), making the INCUMBENT ANCHOR → ROLE C → `incumbent_threat_locked` → GATE S chain fully traceable.

2. **SESSION INVARIANT D leading the invariant block** — Positioning D before A/B/C makes the phrasing register the first structural campaign commitment. A natural R14 extension: can SESSION INVARIANT D be declared before CAMPAIGN OPEN's other invariants while ROLE A still confirms all four as a bundle? Or should D's registration be a separate step from the null-CE invariants, producing a two-phase invariant registration (phrasing register first, null-CE machinery second)?

---

```json
{"top_score": 192, "all_essential_pass": true, "new_patterns": ["INCUMBENT ANCHOR as pre-invariant context block grounds SESSION INVARIANT D templates in named comparator context before registration", "SESSION INVARIANT D leading the invariant block before A/B/C establishes phrasing register as the first structural campaign commitment"]}
```
