## quest-simulate Rubric v7

**Three new aspirational criteria added (C-29 through C-31):**

| ID | Criterion | Upgrades | Source |
|----|-----------|----------|--------|
| C-29 | Propagation Coverage Gate converts dependency map into auditable execution contract | C-24/C-28 (synthesis extracted + propagated → every dependency rule accounted for) | V-01 propagation gap logging; every declared rule either honored or logged as OPEN PROPAGATION GAP |
| C-30 | Confidence-Stratified Action List separates fix-immediately from confirm-spec-first tracks | C-02 (blast-radius rank → blast-radius × confidence quadrant) | V-02 confidence tiebreaker; HIGH-confidence/HIGH-blast vs LOW-confidence/HIGH-blast require different next actions |
| C-31 | Finding Type constrains Remediation Verb vocabulary, making remediation step self-auditing | C-26 (Verb/Target/Location table → type-constrained verb) | V-03 GAP/CONTRADICTION/ASSUMPTION typing; ASSUMPTION-typed findings must use "confirm", not "add" or "remove" |

**Three new structural pairs / extensions:**
- **C-24/C-28/C-29** — patterns extracted → propagated into ranked table → every dependency rule audited for execution
- **C-02/C-30** — blast-radius rank → blast-radius × confidence quadrant action tracks
- **C-26/C-31** — Verb/Target/Location decomposition → verb vocabulary constrained by finding type

**Audit closure now complete:** C-24 extracts named patterns; C-28 propagates them via ELEVATED annotations; C-29 requires every *dependency rule* declared in the cross-skill map to be either re-examined with a finding recorded or explicitly logged as an OPEN PROPAGATION GAP. A dependency map that silently drops rules after synthesis satisfies C-28 but not C-29.

**Confidence stratification now actionable:** C-02 requires blast-radius ranking; C-30 requires the ranked list to be split into two action tracks by confidence. Merging both tracks into a single action list satisfies C-02 but not C-30.

**Remediation self-audit now type-driven:** C-26 requires each remediation entry to decompose into Verb/Target/Location/Conformance columns; C-31 requires the Verb to be constrained by finding type — an ASSUMPTION finding using verb "add" fails C-31 even if the row is structurally complete.

Aspirational pool: 20 → 23 criteria, still capped at 10 pts. Max score 100 unchanged. All five R7 variations score 100/100 on v6; V-01 satisfies C-29; V-02 satisfies C-30; V-03 satisfies C-31; V-04 and V-05 inherit all three.

- **C-29** upgrades the synthesis feedback loop from C-24/C-28 to full auditable execution. C-28
  passes when ELEVATED annotations are present in the ranked findings table; C-29 passes only
  when every dependency rule declared in the cross-skill dependency map is accounted for — either
  re-examined (finding recorded) or explicitly logged as OPEN PROPAGATION GAP with rule ID cited.
  A dependency map that lists 8 rules but silently executes 5 and ignores 3 satisfies C-28
  (if the 5 generated ELEVATEDs) but fails C-29 (3 rules vanished without audit trail). The
  gate converts the dependency map from a planning artifact into a verifiable execution contract.

- **C-30** upgrades blast-radius ranking from C-02 to a two-dimensional triage grid. C-02 passes
  when findings are sorted by blast-radius tier with an explicit column; C-30 passes only when
  the final action list is split into two named tracks: (1) HIGH-confidence / HIGH-blast →
  implement fix immediately; (2) LOW-confidence / HIGH-blast → confirm spec interpretation first,
  then implement. Merging both tracks into a single ordered list satisfies C-02 but not C-30.
  The stratification prevents a LOW-confidence finding from triggering a code change that a
  spec clarification would have made unnecessary.

- **C-31** upgrades remediation quality from C-26 to type-enforced verb vocabulary. C-26 passes
  when every remediation row contains Verb/Target/Location/Conformance columns (no vague prose);
  C-31 passes only when the Verb is constrained by the finding's declared type: GAP-typed
  findings must use "add" or "remove"; CONTRADICTION-typed must use "resolve"; ASSUMPTION-typed
  must use "confirm". An ASSUMPTION-typed finding with Verb="add" fails C-31 even if the row is
  structurally complete. The constraint makes the remediation step self-auditing — an out-of-
  vocabulary verb is a detectable signal that the finding was mis-typed or the remediation was
  mis-planned.

- V-01 from Round 7 satisfies C-29. V-02 satisfies C-30. V-03 satisfies C-31. V-04 (A+B) and
  V-05 (A+B+C) inherit all three. The rubric caught up to the Round 7 gold standard.

---

## Essential Criteria (60 points)

### C-01 . All Five Sub-Skills Execute
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: The simulation must execute all five sub-skills: flow-lifecycle, flow-conversation,
  trace-state, trace-contract, and trace-permissions. Each must produce distinct findings, not
  be silently skipped or collapsed into one pass.
- **Pass condition**: Output contains a labeled section or findings block for each of the five
  sub-skills by name. Absence of any one sub-skill = fail.

---

### C-02 . Findings Ranked by Blast Radius
- **Weight**: essential
- **Category**: format
- **Points**: 12
- **Text**: The final findings report must present findings in ranked order using blast radius as
  the sort key. Blast radius must be explicit — not implied by placement — and must distinguish
  at minimum high / medium / low (or equivalent severity tiers).
- **Pass condition**: A ranked findings list exists with an explicit blast-radius or severity
  column/label. Unranked flat lists = fail.

---

### C-03 . System Boundary and Severity per Finding
- **Weight**: essential
- **Category**: correctness
- **Points**: 12
- **Text**: Every finding must identify (a) the system boundary where it was detected (e.g., state
  machine, contract surface, permission check, lifecycle phase) and (b) a severity rating. These
  must appear per finding, not as a summary average.
- **Pass condition**: Each finding entry includes both a boundary label and a severity. Findings
  missing either field = fail.

---

*(C-04 through C-25 — unchanged from v6)*

---

## Aspirational Criteria — Round 6 additions (C-26 through C-28)

### C-26 . Remediation Quality Gate: Verb/Target/Location Table
- **Weight**: aspirational
- **Category**: format
- **Text**: The Remediation Quality Gate must produce a per-row structured table decomposing each
  remediation entry into Verb / Target / Location / Conformance columns. A checklist checkbox
  is structurally non-falsifiable; a Verb=add / Target=permission check /
  Location=CallHandler.process() row is verifiable by column scan.
- **Pass condition**: Every remediation entry appears as a structured row with all four columns
  populated. Prose remediation entries or blank cells in any column = fail.

---

### C-27 . Entity Coverage Matrix: COVERED / CLEAN / SKIPPED
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every entity in the Topic Entity Manifest must appear in a named Entity Coverage Matrix
  with an explicit COVERED / CLEAN / SKIPPED status. A SKIPPED entity is treated as an execution
  gap, not a clean run — same disqualifying weight as a missing sub-skill sentinel row in C-16.
- **Pass condition**: Entity Coverage Matrix present; every manifest entity has a status; SKIPPED
  entities logged as execution gaps. Entities absent from the matrix = fail.

---

### C-28 . Blast Radius Re-Assessment Gate: ELEVATED Annotations
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-skill synthesis patterns must be propagated back into the ranked findings table
  via ELEVATED annotations citing the named pattern ID before the report is finalized. A
  synthesis gate that populates a P-ID table but leaves the ranked findings table unchanged
  satisfies C-24 but not C-28.
- **Pass condition**: At least one finding carries an ELEVATED annotation with a P-ID citation;
  the ranked table reflects re-ordering based on synthesis results. Synthesis section isolated
  from ranked table = fail.

---

## Aspirational Criteria — Round 7 additions (C-29 through C-31)

### C-29 . Propagation Coverage Gate: Dependency Rules Audited
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Every dependency rule declared in the cross-skill dependency map must be explicitly
  accounted for in the execution record: either honored (re-examined, finding recorded, rule ID
  cited) or logged as an OPEN PROPAGATION GAP with the rule ID and reason for non-execution.
  A dependency map that silently drops rules after synthesis satisfies C-28 but fails C-29.
- **Pass condition**: All declared dependency rule IDs appear in either the finding record or an
  OPEN PROPAGATION GAP log. Rules present in the map but absent from both = fail.

---

### C-30 . Confidence-Stratified Action List: Two Named Tracks
- **Weight**: aspirational
- **Category**: format
- **Text**: The final action list must be split into two named tracks by blast-radius × confidence
  quadrant: (1) HIGH-confidence / HIGH-blast → implement fix immediately; (2) LOW-confidence /
  HIGH-blast → confirm spec interpretation first, then implement. A single merged action list
  ordered only by blast radius satisfies C-02 but fails C-30.
- **Pass condition**: Two named action tracks present with findings assigned by quadrant. Merged
  single-track list, or tracks defined without confidence as a dimension = fail.

---

### C-31 . Finding Type Constrains Remediation Verb Vocabulary
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Each finding must be typed at detection as GAP / CONTRADICTION / ASSUMPTION. The
  remediation Verb must be constrained by type: GAP → "add" or "remove"; CONTRADICTION →
  "resolve"; ASSUMPTION → "confirm". An ASSUMPTION-typed finding with Verb="add" fails C-31
  even if the remediation row is otherwise structurally complete under C-26. The type-verb
  binding makes remediation self-auditing — an out-of-vocabulary verb signals mis-typing or
  mis-planning.
- **Pass condition**: All findings carry a type declaration; all remediation Verbs match the
  allowed vocabulary for that type. Out-of-vocabulary Verbs = fail. Untyped findings = fail.
