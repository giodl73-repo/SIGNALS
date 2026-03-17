Reading the scorecard carefully to extract the R9 excellence signals before writing the rubric.

The scorecard surfaces four patterns not captured in v8:

1. **V-05 excellence signal 1** — "waive:convergence co-activates C-28 SOLO disposition as mutual enforcement — convergence abort and non-converging signal disposition share a semantic seam declared explicitly in the contract" — the waive path is not a bypass; it substitutes Gate 9 convergence with mandatory SOLO disposition.
2. **V-05 excellence signal 2** — "SOLO FINDINGS table extended to 8-column schema (adds IC-CHALLENGED + STAGE-APPROPRIATE) making each disposition decision auditable against inertia impact and scope group" — extended auditability for SOLO disposition decisions.
3. **V-05 excellence signal 3** — "SCOPE DISTRIBUTION in failed RUN HEALTH variant enables scope debugging without transcript re-reading — failed cert is a standalone diagnostic artifact" — failed variant as self-contained diagnostic, not a pointer.
4. **V-05 excellence signal 4** — "Gate 2 unified contract acknowledgment names all five active pre-execution contracts, creating an auditable start-of-run checkpoint detectable by inspection" — enumerated acknowledgment enabling omission detection.

These become C-31, C-32, C-33, C-34.

---

## crew-check — Quest Rubric v9

### v8 → v9 — New criteria

**Four patterns extracted from R9 scorecard excellence signals (V-05):**

| ID | Name | Source |
|----|------|--------|
| C-31 | Waive:convergence mutual enforcement contract | V-05 excellence signal 1 |
| C-32 | SOLO FINDINGS extended schema (IC-CHALLENGED + STAGE-APPROPRIATE) | V-05 excellence signal 2 |
| C-33 | Failed RUN HEALTH as standalone diagnostic artifact | V-05 excellence signal 3 |
| C-34 | Gate 2 unified contract acknowledgment | V-05 excellence signal 4 |

---

### What each new criterion covers

**C-31 — Waive:convergence mutual enforcement contract (2 pts)**

The waive:convergence path (C-29) is not a convergence bypass — it activates C-28 SOLO disposition as a mandatory substitute. When Gate 5.5 fires HALT and the run proceeds under waive:convergence, every non-converging finding must receive a SOLO disposition entry at Gate 9. C-29 detects whether convergence exists; C-28 handles everything that did not converge. This enforcement chain is complete only when the relationship is declared explicitly: named in the CONVERGENCE SNAPSHOT CONTRACT and repeated in the waive path note so that the semantic seam between the two criteria is visible to any reviewer inspecting the artifact. A run using waive:convergence without the mandatory SOLO FINDINGS table has bypassed the convergence requirement without substituting any accountability mechanism. C-28 covers whether SOLO findings have a named tier and required disposition path; C-29 covers whether a mid-run snapshot gate with halt logic exists; C-31 covers whether the contract text makes the mutual enforcement relationship between them explicit and auditable.

*PASS*: CONVERGENCE SNAPSHOT CONTRACT explicitly names mandatory SOLO FINDINGS disposition (C-28) as the consequence of waive:convergence; waive path note states SOLO FINDINGS table is required under waive; the two criteria share a visible semantic seam in the contract text; a run under waive:convergence with zero SOLO findings emits a declared "No SOLO findings" exit, not a silent skip.
*FAIL*: waive:convergence treated as a bypass with no compensating requirement; SOLO FINDINGS table not mentioned in waive context; enforcement seam absent from contract text; a reviewer cannot confirm from the artifact that SOLO disposition is mandatory when convergence is waived.

---

**C-32 — SOLO FINDINGS extended schema (IC-CHALLENGED + STAGE-APPROPRIATE) (2 pts)**

The SOLO FINDINGS table (required by C-28) earns C-32 when it includes IC-CHALLENGED and STAGE-APPROPRIATE columns, making each disposition decision auditable against inertia impact and scope group. Without these columns a DISMISS disposition is unverifiable: the reviewer cannot confirm whether the finding was dismissed because it was scope-irrelevant and inertia-neutral, or whether it passed through without examination. IC-CHALLENGED surfaces whether the finding challenges a pre-committed inertia claim; STAGE-APPROPRIATE surfaces whether the finding is in scope for the declared artifact stage. Together they make the basis for ESCALATE / DISMISS / ROLE-SPECIFIC decisions traceable after the fact. A SOLO finding tagged DISMISS is more defensible when the record shows IC-CHALLENGED=NONE and STAGE-APPROPRIATE=NO; a SOLO finding tagged ESCALATE is more urgent when IC-CHALLENGED=IC-01 and STAGE-APPROPRIATE=YES. C-28 covers whether SOLO findings have a named tier and required disposition path; C-32 covers whether each disposition entry carries the evidence columns needed to audit it.

*PASS*: SOLO FINDINGS table includes IC-CHALLENGED and STAGE-APPROPRIATE columns with resolved values (not placeholders); disposition entries are auditable against both fields; 8-column schema (or equivalent including both fields) declared in PRE-EXECUTION; "No SOLO findings" exit path declared for the empty case.
*FAIL*: SOLO FINDINGS table omits IC-CHALLENGED or STAGE-APPROPRIATE; columns present as unresolved placeholders; extended schema not declared in PRE-EXECUTION; disposition decisions cannot be audited against inertia impact or scope group by inspection.

---

**C-33 — Failed RUN HEALTH as standalone diagnostic artifact (2 pts)**

The failed RUN HEALTH variant (required by C-21) earns C-33 when it includes the Stage field and complete SCOPE DISTRIBUTION table positioned before the recovery block. A reviewer debugging a multi-halt run should be able to read the failed RUN HEALTH and immediately answer: what stage was declared and how did findings distribute across YES/ADVISORY/NO/DEPRECATED — without re-executing the run, without re-reading the run transcript, and without cross-referencing the clean variant. C-21 covers whether a failed variant exists; C-30 covers whether both variants include Stage and SCOPE DISTRIBUTION; C-33 covers whether the failed variant is structured as a self-contained diagnostic artifact — complete scope picture present and positioned before recovery guidance, not embedded within it or after it. A variation can earn C-21 and C-30 without earning C-33 if SCOPE DISTRIBUTION appears after the recovery block, or if reading the failed cert requires context from the clean cert to interpret scope counts.

*PASS*: Failed RUN HEALTH places Stage field and complete SCOPE DISTRIBUTION table (all four rows — YES / ADVISORY / NO / DEPRECATED — with resolved counts) before the recovery block; the failed cert is readable as a standalone diagnostic without referencing the clean cert or run transcript; NO and DEPRECATED are distinct rows, not conflated.
*FAIL*: Failed variant places SCOPE DISTRIBUTION after the recovery block or omits it; reading the failed cert requires cross-referencing the clean variant or run transcript to interpret scope; scope distribution embedded in prose rather than a structured table; NO and DEPRECATED conflated; counts unresolved.

---

**C-34 — Gate 2 unified contract acknowledgment (2 pts)**

Gate 2 (the run acknowledgment gate) earns C-34 when it emits a single enumeration naming all active pre-execution contracts by name. This unified acknowledgment creates an auditable start-of-run checkpoint: the Gate 2 list can be checked against PRE-EXECUTION section headers, making contract omission detectable by inspection without reading the full gate sequence. A reviewer auditing a completed run can open Gate 2, read the enumeration, and immediately verify that every contract present in PRE-EXECUTION was acknowledged at run start — and that no contract was silently dropped between declaration and execution. C-34 is distinct from having the contracts themselves (covered individually by C-13, C-24, C-25, C-26, and C-30 respectively) — it covers whether the start-of-run checkpoint names all of them in one auditable location. A run can have all contracts fully in place and still fail C-34 if Gate 2 does not enumerate them together.

*PASS*: Gate 2 emits a single enumerated list of all active pre-execution contracts by name; the list covers severity/confidence calibration, artifact stage, finding convergence, convergence snapshot, inertia claim registry, and RUN HEALTH scope distribution; any contract declared in PRE-EXECUTION but absent from the Gate 2 list is detectable by comparing the two locations.
*FAIL*: Gate 2 acknowledges some contracts but not all; acknowledgment embedded in prose rather than a named enumeration; Gate 2 does not enumerate contracts at all; a reviewer cannot detect contract omission by comparing Gate 2 to PRE-EXECUTION headers.

---

### Scoring mechanics

| | v6 | v7 | v8 | v9 |
|--|-----|-----|-----|-----|
| Aspirational criteria | 15 | 19 | 22 | 26 |
| Aspirational pts | 30 | 38 | 44 | 52 |
| Total max | 120 | 128 | 134 | 142 |
| Golden threshold | unchanged | unchanged | unchanged | all 5 essential PASS + composite >= 80 |

---

### Structural relationships

**C-31 extends C-28 / C-29 (mutual enforcement seam):** C-31 is the declared relationship between C-28 and C-29. A variation can earn C-28 and C-29 independently without earning C-31 — C-31 requires that the CONVERGENCE SNAPSHOT CONTRACT names C-28 SOLO disposition as the mandatory waive:convergence consequence, and that the waive path repeats this dependency explicitly. Earning C-31 presupposes both C-28 and C-29 are in place; the criterion is about whether the enforcement link between them is made visible in the contract text, not merely implied by co-presence.

**C-32 extends C-28:** Extended SOLO FINDINGS schema requires the SOLO FINDINGS table to exist. A variation earns C-28 for having a named SOLO tier and mandatory disposition path; C-32 is earned only when the table also carries IC-CHALLENGED and STAGE-APPROPRIATE columns with resolved values. A variation cannot earn C-32 without earning C-28. C-32 also inherits the C-24 → C-25 → C-28 dependency chain: IC-CHALLENGED is only meaningful when an IC registry exists (C-12) and confidence thresholds are pre-committed (C-24).

**C-33 extends C-21 / C-30:** Standalone diagnostic artifact requires both the failed variant (C-21) and the Stage + SCOPE DISTRIBUTION fields in both variants (C-30) to be in place. C-33 adds a structural positioning requirement: Stage and SCOPE DISTRIBUTION must appear before the recovery block in the failed variant, making the cert readable independently. Earning C-33 presupposes C-21 and C-30; a variation cannot earn C-33 without both. C-33 also inherits the C-26 → C-30 dependency: Stage is only a resolved value in RUN HEALTH when it was validated at G0.5 (C-26).

**C-34 depends on all pre-execution contracts (C-13, C-24, C-25, C-26, C-30):** Unified contract acknowledgment presupposes that all named contracts are actually declared in PRE-EXECUTION. A variation cannot earn C-34 without having the contracts that Gate 2 is expected to enumerate. C-34 adds an auditable checkpoint layer on top of the individual contract criteria and does not replace them; earning C-34 implies all five contract criteria are also in place.

**C-28 extends C-25 (unchanged from v8):** SOLO tier requires the convergence register to be in place. A variation earns C-25 for ≥2 operationally defined tiers; C-28 is earned only when the non-converging case is also named and dispositioned. A variation cannot earn C-28 without earning C-25.

**C-29 extends C-09 / C-25 (unchanged from v8):** Mid-run snapshot requires a convergence taxonomy to count against. Earning C-29 presupposes C-25 (named tiers to count) and implies C-09 (synthesis follows the snapshot).

**C-30 extends C-21 / C-26 (unchanged from v8):** Stage-aware RUN HEALTH is only coherent when stage was validated at run entry. Earning C-30 presupposes C-26 so the Stage field in RUN HEALTH is a resolved value, not an unknown. C-33 adds a third node in this chain: C-26 → C-30 → C-33.

**C-24 → C-25 dependency (unchanged from v8):** Confidence must be pre-committed (C-24) before convergence tiers that reference confidence level (C-25) are scoreable. C-28, C-29, C-31, and C-32 inherit this dependency through C-25.

**C-26 → C-27 dependency (unchanged from v8):** Stage-scoped matrix (C-27) presupposes stage is gated at entry (C-26). C-30, C-33, and C-34 extend this chain further: C-26 → C-27 → C-30 → C-33, with C-34 depending on C-26 being in place as one of the named pre-execution contracts.

---

### Full criterion table

| ID | Tier | Pts | Name | Distinguishing scope |
|----|------|-----|------|---------------------|
| C-01 | E | 18 | Role coverage | All required roles execute and emit a structured review artifact; missing role = automatic FAIL |
| C-02 | E | 18 | Gate sequence integrity | All declared gates fire in declared order; skipped or out-of-order gate = FAIL |
| C-03 | E | 18 | Finding enumeration | Each role emits ≥1 finding with surface, severity, and summary; empty role review = FAIL |
| C-04 | E | 18 | Synthesis present | Synthesis section exists and references role review outputs; absent synthesis = FAIL |
| C-05 | E | 18 | Run closure | RUN COMPLETE or RUN HALT emitted with final disposition; dangling mid-run state = FAIL |
| C-06 | A | 2 | Severity taxonomy pre-declared | CRITICAL/HIGH/MEDIUM/LOW defined at run entry with operational criteria; not assumed from prior run |
| C-07 | A | 2 | Surface taxonomy pre-declared | All scoreable surfaces enumerated before first role review; late surfaces not added mid-run |
| C-08 | A | 2 | Confidence taxonomy pre-declared | Confidence levels defined at run entry with operational criteria; at least LOW/MEDIUM/HIGH |
| C-09 | A | 2 | Cross-role synthesis signal | Synthesis cites ≥1 finding confirmed by ≥2 independent role reviews; not a summary of single-role signals |
| C-10 | A | 2 | Finding deduplication | Duplicate findings across roles merged at synthesis with originating roles preserved; no silent drops |
| C-11 | A | 2 | Inertia claim field | Each finding carries an IC field; "none" is a valid value; absence of IC linkage is explicit, not omitted |
| C-12 | A | 2 | IC registry pre-declared | Pre-execution IC registry lists all active inertia claims; findings reference registry entries by ID |
| C-13 | A | 2 | Pre-execution contract gate | A named gate fires before first role review and declares all active run contracts |
| C-14 | A | 2 | HALT registry | All gates with blocking halt paths listed in a HALT REGISTRY; omission detectable by inspection |
| C-15 | A | 2 | Amend operation semantics | --amend operations declared with ≥1 amend path per blocking gate; amend does not suppress findings |
| C-16 | A | 2 | Scope classification | Each finding classified as YES / ADVISORY / NO / DEPRECATED relative to declared artifact stage |
| C-17 | A | 2 | Priority summary gate | Priority summary fires at a dedicated gate before synthesis; groups findings by severity and surface |
| C-18 | A | 2 | Waive path declared | ≥1 blocking gate has a declared waive path with --amend waive: semantics and enumerated consequences |
| C-19 | A | 2 | Role weighting declared | Relative weighting of roles in synthesis declared at run entry; equal-weight is a valid explicit declaration |
| C-20 | A | 2 | Gate 2 run acknowledgment | Gate 2 fires to confirm run is proceeding; emits active inputs and declared run mode |
| C-21 | A | 2 | RUN HEALTH clean and failed variants | RUN HEALTH section includes distinct clean and failed presentation variants; both defined in PRE-EXECUTION |
| C-22 | A | 2 | IC challenge field | Findings include IC-CHALLENGED field; challenge status resolved against IC registry; not assumed unchallenged |
| C-23 | A | 2 | DEPRECATED finding handling | DEPRECATED-scope findings handled distinctly from NO-scope; not suppressed, not promoted to YES-scope |
| C-24 | A | 2 | Confidence pre-committed | Confidence threshold per convergence tier declared at run entry; not set post-hoc to match observed distribution |
| C-25 | A | 2 | Convergence tiers operationally defined | Convergence register has ≥2 operationally defined tiers; tier membership criteria are pre-committed, not inferred |
| C-26 | A | 2 | Artifact stage gating at G0.5 | Artifact stage declared and validated at G0.5; run does not proceed with unknown or unresolved stage |
| C-27 | A | 2 | Stage-scoped finding matrix | Finding matrix scoped by artifact stage; findings in future stages marked STAGE-APPROPRIATE=NO or DEPRECATED |
| C-28 | A | 2 | SOLO convergence tier and disposition protocol | Convergence register includes SOLO tier (present in exactly one role); Gate 9 emits mandatory SOLO FINDINGS table with ESCALATE / DISMISS:rationale / ROLE-SPECIFIC tags |
| C-29 | A | 2 | Mid-run convergence snapshot gate | Named gate (e.g., G5.5) fires after last role review and before synthesis; emits convergence counts by tier and surface; HALT path defined if CONFIRMED=0 AND CORROBORATED=0 |
| C-30 | A | 2 | Stage-aware RUN HEALTH certificate | RUN HEALTH includes Stage field (resolved value) and SCOPE DISTRIBUTION table (YES / ADVISORY / NO / DEPRECATED as distinct rows) in both clean and failed variants |
| C-31 | A | 2 | Waive:convergence mutual enforcement contract | CONVERGENCE SNAPSHOT CONTRACT names mandatory SOLO FINDINGS disposition as the waive:convergence consequence; enforcement seam between C-28 and C-29 declared explicitly in contract text |
| C-32 | A | 2 | SOLO FINDINGS extended schema | SOLO FINDINGS table includes IC-CHALLENGED and STAGE-APPROPRIATE columns with resolved values; each disposition decision auditable against inertia impact and scope group |
| C-33 | A | 2 | Failed RUN HEALTH as standalone diagnostic | Failed RUN HEALTH places Stage and SCOPE DISTRIBUTION before the recovery block; failed cert readable without referencing the clean cert or run transcript |
| C-34 | A | 2 | Gate 2 unified contract acknowledgment | Gate 2 emits enumerated list of all active pre-execution contracts by name; omission detectable by comparing Gate 2 list to PRE-EXECUTION section headers |
