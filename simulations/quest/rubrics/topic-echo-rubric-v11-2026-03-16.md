Written to `simulations/quest/rubrics/topic-echo-rubric-v11-2026-03-16.md`.

---

# topic:echo Rubric -- v11

**Three key changes from v10:**
- Max composite: 215 -> 230
- Aspirational criteria: 25 -> 28
- New relationships: C-33/C-34, C-33/C-35, C-20/C-36

**Three new criteria (C-34, C-35, C-36):**

| ID | Gate | Pattern | What it adds |
|----|------|---------|--------------|
| C-34 | C-33 | BC-COVERAGE-RECORD | C-33 makes EF's invocation auditable; C-34 applies the identical standard to BC. Every exclusion-scoped role produces a parallel coverage record. Symmetric provenance: "EF is auditable" becomes "all exclusion-scoped roles are auditable." |
| C-35 | C-33 | PHASE-HANDOVER tokens at EF-exit and BC-exit | C-33 made role entry auditable at Step 0. C-35 makes role exit auditable: EF names what it produced before handing off to BC; BC names what it produced before handing off to the distillation phase. Role transitions are bookended -- entry record + exit token per role. |
| C-36 | C-20 | DISCARD LOG with typed entries + DISCARD-LOG-COMPLETE | C-20 makes accept decisions visible (accepted candidates appear in Rules of Thumb). C-36 makes reject decisions equally visible: each NO decision produces a DISCARD-[N] entry with route and reason; DISCARD-LOG-COMPLETE summarizes the full candidate set. The artifact accounts for every candidate, not just those it kept. |

**Score model:**

| Tier | Points | Criteria | Per-criterion |
|------|--------|----------|---------------|
| Essential | 60 | 5 | 12 |
| Recommended | 30 | 3 | 10 |
| Aspirational | **140** | **28** | 5 |
| **Max composite** | **230** | | |

**R10 scoring under v11:**

| Variation | C-34 | C-35 | C-36 | v10 | v11 | delta |
|-----------|:----:|:----:|:----:|:---:|:---:|:-----:|
| V-01 | PASS | FAIL | FAIL | 215 | 220 | +5 |
| V-02 | FAIL | PASS | FAIL | 215 | 220 | +5 |
| V-03 | FAIL | FAIL | PASS | 215 | 220 | +5 |
| V-04 | PASS | PASS | FAIL | 215 | 225 | +10 |
| **V-05** | PASS | PASS | PASS | 215 | **230** | +15 |

Same structural pattern as R9: single-axis +5, dual-axis +10, all-axes +15. V-05 alone reaches the ceiling.

**Round 10 progression layer:** ... -> role accountability / evidentiary phase tokens / invocation observability -> **symmetric provenance / phase-exit observability / selection transparency**. Each layer extends an existing auditability obligation to the cases it previously excluded.

**The unified R10 thesis:** Asymmetric auditability is a design defect, not a specification gap. The "auditable from output" standard must extend to (a) all roles with equivalent exclusion obligations, (b) both sides of every phase transition, and (c) both outcomes of every filtering decision.
oduce a BC-COVERAGE-RECORD block listing all three elements: signal artifacts processed, signal artifacts excluded by name, and coverage derivation basis. First appeared in Round 10 V-01.

**C-35 -- PHASE-HANDOVER tokens at EF-exit and BC-exit**
(behavior, gate: C-33)

C-33 makes EF's entry into Step 0 auditable at invocation time: the EF-INVOCATION-RECORD records what EF saw before acting. C-35 makes role exit auditable: EF emits a PHASE-HANDOVER-EF token immediately before handing off to BC, naming what EF produced; BC emits a PHASE-HANDOVER-BC token immediately before handing off to the distillation phase, naming what BC produced. Without PHASE-HANDOVER tokens, role transitions are entry-visible and exit-silent: a reviewer can confirm what each role started with (entry records from C-33/C-34) but cannot read from the artifact what each role delivered. With PHASE-HANDOVER tokens, every role transition is bookended -- the entry record names what was seen, the exit token names what was produced. A reviewer can reconstruct the full handoff chain: EF saw X (C-33), produced Y (PHASE-HANDOVER-EF), handed to BC; BC saw Y and Z (C-34), produced W (PHASE-HANDOVER-BC), handed to distillation. Pass requires both PHASE-HANDOVER-EF and PHASE-HANDOVER-BC tokens to appear at the respective role-exit points, each naming what the exiting role produced before transition. First appeared in Round 10 V-02.

**C-36 -- DISCARD LOG with typed entries and DISCARD-LOG-COMPLETE**
(behavior, gate: C-20)

C-20 requires the distillation layer to extract the highest-impact surprises into a Rules of Thumb section with tier annotations, confirmed by RULES-ANCHORED traceability check. The accept decisions made by the STILL-LIVE FILTER are visible in the output: accepted candidates appear as Rules of Thumb. C-36 requires reject decisions to be equally visible: each candidate that the STILL-LIVE FILTER does not accept produces a typed DISCARD-[N] entry containing the candidate identifier, the reject route, and the reason for rejection. When all candidates have been either accepted or discarded, DISCARD-LOG-COMPLETE is emitted, summarizing the full candidate set. Without a DISCARD LOG, the distillation phase accounts only for accepted candidates: a reviewer can read which surprises became Rules of Thumb but cannot determine how many candidates were considered, which were excluded, or on what basis. With a DISCARD LOG, the filter is fully transparent: accept and reject decisions are symmetrically visible, and DISCARD-LOG-COMPLETE confirms that every candidate is accounted for. This applies the same completeness discipline to distillation-phase filtering that CHAIN-COMPLETE (C-19) and RULES-ANCHORED-COMPLETE (C-28) apply to their respective phases. Pass requires typed DISCARD-[N] entries for every non-accepted candidate (containing candidate identifier, route, and reason) and a DISCARD-LOG-COMPLETE token confirming the full candidate set has been enumerated. First appeared in Round 10 V-03.

---

## Score model

| Tier | Points | Criteria | Per-criterion |
|------|--------|----------|---------------|
| Essential | 60 | 5 | 12 |
| Recommended | 30 | 3 | 10 |
| Aspirational | **140** | **28** | 5 |
| **Max composite** | **230** | | |

**Golden threshold:** All C-01 through C-05 pass AND composite >= 80. Unchanged.

---

## What the Round 10 variations score under v11

| Variation | C-34 | C-35 | C-36 | v10 score | v11 composite | vs v10 |
|-----------|------|------|------|-----------|---------------|--------|
| V-01 | **PASS** | FAIL | FAIL | 215 | 220 | +5 |
| V-02 | FAIL | **PASS** | FAIL | 215 | 220 | +5 |
| V-03 | FAIL | FAIL | **PASS** | 215 | 220 | +5 |
| V-04 | **PASS** | **PASS** | FAIL | 215 | 225 | +10 |
| **V-05** | **PASS** | **PASS** | **PASS** | 215 | **230** | +15 |

V-05 is the only R10 variation that reaches the v11 ceiling. The three new criteria are three independent axes -- no R10 variation holds more than two of them except V-05 (all-axes combination). Same structural pattern as R9: single-axis +5, dual-axis +10, all-axes +15.

**Three key changes from v10:**
- Max composite: 215 -> 230
- Aspirational criteria: 25 -> 28
- New relationships: C-33/C-34, C-33/C-35, C-20/C-36

**Round 10 progression layer:** visibility -> navigability -> primacy -> repairability / stakes / verifiability -> auditable closure / visual sovereignty / structural provenance -> role accountability / evidentiary phase tokens / invocation observability -> **symmetric provenance / phase-exit observability / selection transparency**. Each new layer extends an existing auditability obligation to the cases it previously excluded.

---

**Notes on Round 10 pattern:**

- C-33 made EF's Step 0 invocation auditable -> C-34 extends the same standard to BC (selective auditability -> symmetric auditability)
- C-33 made role entry auditable at invocation time -> C-35 makes role exit auditable via PHASE-HANDOVER tokens (entry-only observability -> bookended observability)
- C-20 made accept decisions visible in the distillation layer -> C-36 makes reject decisions equally visible via DISCARD LOG (one-sided visibility -> full selection transparency)

**The unified R10 thesis:** Asymmetric auditability is an artifact design defect, not a specification gap. The "auditable from output" standard R9 applied to EF's invocation must extend to (a) all roles with equivalent exclusion obligations, (b) both sides of every phase transition, and (c) both outcomes of every filtering decision. An artifact where EF is observable but BC is not, exits are invisible while entries are recorded, or rejected candidates are unaccounted while accepted candidates appear, satisfies the letter of prior criteria while violating their principle.

---

## Essential Criteria (weight: 60 points total, 12 pts each)

Five criteria. All must pass to qualify as golden or passing.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Named surprise with departure framing** | correctness | The artifact names at least one finding explicitly framed as a departure from expectation. The framing must be structural -- the surprise is labeled or marked as such, not merely described. A finding presented as a neutral observation that happens to be unexpected does not pass. Minimum acceptable framing: "We expected X to be negligible; it turned out to dominate" (surprise). |
| C-02 | **Signal tracing per surprise** | correctness | Every named surprise is traced to a specific source signal or artifact by name. Generic attribution is insufficient. Each surprise must name the artifact that produced it. A surprise without a traceable source cannot be audited by the next team and fails. |
| C-03 | **Design impact assessed per surprise** | depth | Every named surprise carries an explicit assessment of its impact on design direction. Impact may be confirming, redirecting, or destabilizing. An impact statement that does not identify which design decision is affected fails. "This changes things" without naming what changes is insufficient. |
| C-04 | **Synthesis not summary** | behavior | The artifact contains only surprises and their analysis. Expected findings are either absent or explicitly marked as context-only. An artifact that enumerates findings and labels some "interesting" fails -- the surprise/expected partition must be explicit and structural. |
| C-05 | **Surprise specificity** | correctness | Each surprise is specific to this investigation's signal set, not a generic observation that could appear in any investigation. "APIs are harder to design than expected" fails -- it applies universally. "The scout:competitors signal revealed that all three competitors treat X as a solved problem, contrary to our assumption that the space was unsolved" passes -- it is falsifiable against this investigation's artifacts. |

---

## Recommended Criteria (weight: 30 points total, 10 pts each)

Output is better with these. Golden typically requires at least 2 of 3.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Expectation counterfactual** | depth | Each surprise explicitly names what was expected versus what was found. The counterfactual structure is stated, not implied. A reader new to the topic can reconstruct the prior assumption from the surprise entry alone, without consulting the underlying signal artifacts. Surprises that omit the expected-state half are incomplete. |
| C-07 | **Institutional framing** | behavior | The artifact is explicitly addressed to a future team. At least one element signals forward-facing intent: surprises framed as things the next team would not predict, a closing note naming what to investigate first, or an opening institutional purpose declaration. An artifact that reads as a personal retrospective without forward framing fails. |
| C-08 | **Cross-signal pattern identification** | coverage | If two or more surprises share an underlying cause or implication, that relationship is named with a statement of what they have in common and what that implies for design. If all surprises are genuinely independent, the output explicitly states this. Omitting pattern analysis when multiple surprises exist is a fail. |

---

## Aspirational Criteria (weight: 140 points total, 5 pts each)

Raise the bar once essential and recommended criteria are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Surprise hierarchy by design impact** | depth | Surprises are ranked by design impact with an explicit rationale that is argued, not asserted. A ranked list without argument is insufficient -- the hierarchy must be defensible to a reader who disagrees with it. |
| C-10 | **Riskiest surprise flagged** | behavior | The single surprise most likely to invalidate a core assumption is explicitly flagged. The flag names the assumption at risk, the signal that revealed it, and what would need to be true for the assumption to hold despite the surprise. |
| C-11 | **Pre-committed prior belief inventory** | correctness | The artifact contains a Prior Belief Inventory produced before signal reading -- a discrete, labeled section predating surprise entries. Each surprise entry references a specific PB entry by identifier. Minimum bar: (a) discrete PBI section exists, (b) entries are addressable by identifier, (c) each surprise cites a specific PBI entry by that identifier. |
| C-12 | **Named surprise handles** | behavior | Each surprise carries a short named handle (2-5 words) specific enough to be cited by future signal artifacts without re-reading the echo. Test: could a teammate say "remember the [handle] surprise?" and be unambiguously understood? "API complexity surprise" fails. "competitor-treated-X-as-solved" passes. |
| C-13 | **Dual phase-locked pre-commitment integrity** | correctness | The PBI and Handle Ledger are demonstrably independent -- PBI entries use belief language; Handle Ledger titles use finding language specific to what signals revealed. Independence fails if a PBI entry names a handle label by its final form, or a Handle Ledger title echoes PBI entry language verbatim. Applicable only when both C-11 and C-12 are satisfied. |
| C-14 | **Single-entry audit trail completeness** | behavior | Each surprise entry contains all three pointers enabling provenance verification without consulting other sections: (1) Handle Ledger title, (2) PBI identifier, (3) source signal artifact. All three checks possible from the entry alone. Applicable only when both C-11 and C-12 are satisfied. |
| C-15 | **Pre-commitment enforcement mechanism declaration** | correctness | The artifact declares how its PBI was isolated from signal knowledge. A timestamped freeze declaration provides temporal provenance. A role-scope declaration provides structural provenance. Without a mechanism declaration a reviewer must infer pre-commitment quality from content analysis alone -- making C-13 independence unverifiable without re-deriving it from scratch. Note: temporal < structural because a phase gate sequences but does not block cross-phase reasoning. Applicable only when C-11 is satisfied. |
| C-16 | **Production-time per-entry verification attestation** | behavior | Each surprise entry includes an explicit statement confirming all three audit pointers were verified at production time: (1) handle confirmed in Handle Ledger, (2) PBI-Ref confirmed at cited identifier, (3) source artifact confirmed in signal set. An attestation naming each check explicitly is a pass; a generic "verified" without naming what was verified fails. Applicable only when C-14 is satisfied. |
| C-17 | **Enforcement mechanism strength classification with calibration rationale** | correctness | The artifact classifies its declared enforcement mechanism on the strength hierarchy (structural > temporal) and states the property that earns that classification. Pass bar requires two elements: (a) tier label stated ("structural provenance" or "temporal provenance"), and (b) the distinguishing property explained -- structural provenance is enforced by role-scope exclusion (the PBI-writing role cannot access signal artifacts regardless of instruction); temporal provenance is enforced by phase sequencing (phases are ordered but cross-phase reasoning is not blocked). Declaring "structural provenance" without explaining why it is structural rather than temporal fails C-17. Stating tier, distinguishing property, and reviewer implication ("independence is enforced, not instructed; C-13 content analysis is confirmatory rather than probative") passes at the highest level. Applicable only when C-15 is satisfied. |
| C-18 | **Per-entry attestation with evidentiary quotation** | behavior | Each surprise entry's production-time attestation quotes the actual text of the PBI entry and source finding being attested -- not just their identifiers. Pass condition: the Verified field quotes substantive text for both -- the actual belief statement and the relevant finding sentence -- sufficient to confirm that cited identifiers point to the right content. A fragment too short to confirm correct citation fails; a quoted sentence that uniquely identifies the prior belief and the finding passes. Converts the attestation from a declaration of action (checks were performed) into a disclosure of evidence (here is what was checked). Applicable only when C-16 is satisfied. |
| C-19 | **Post-production chain integrity audit with visible tokens** | behavior | After the artifact is written, a discrete Chain Integrity Audit re-verifies all four chain elements [PBI-Ref, Handle, Source, Verified quotation] for internal consistency. Each entry receives a visible CHAIN-COMPLETE token (or CHAIN-FLAG with description) produced by this audit step. The audit is distinct from the production-time attestation layer (C-16/C-18): C-16/C-18 attest that checks were performed; C-19 confirms those attestations are correct by re-running verification independently. An artifact with C-19 is auditable from output alone -- a reviewer reads CHAIN-COMPLETE and knows the chain was externally validated, not just self-reported. Applicable only when C-18 is satisfied. |
| C-20 | **Impact-anchored distillation layer with traceability verification** | behavior | The artifact includes a Rules of Thumb section encoding the highest-impact surprises in <=20-word quotable form. Each rule carries a tier annotation ([HIGH] or [MEDIUM]) matching its surprise entry; LOW-tier surprises are excluded. After all rules are written, a named traceability check (e.g., RULES-ANCHORED) confirms tier alignment between each rule and its parent surprise entry. Pass requires both: (1) the distillation layer with tier annotations, and (2) the named traceability check confirming alignment. Without the traceability check the distillation is a summary; with it the distillation is an auditable extract of the hierarchy, citable by future teams without re-reading full entries. Applicable only when C-09 is satisfied. |
| C-21 | **Enforcement mechanism declaration in independently navigable section** | behavior | The C-17 enforcement mechanism classification is placed in a discrete headed section or titled table that a reviewer can locate without reading the full artifact. Inline declaration embedded in a PBI preamble, narrative paragraph, or step description does not satisfy C-21 even if it satisfies C-17. Test: can a reviewer jump directly to the enforcement mechanism claim using section headings or table titles alone? If yes, C-21 passes. Applicable only when C-17 is satisfied. |
| C-22 | **Chain-flag progression gate** | behavior | The CHAIN-FLAG token produced by the Chain Integrity Audit (C-19) functions as a hard production gate: any CHAIN-FLAG on any entry blocks further artifact completion until the flag is resolved. Pass requires an explicit blocking condition in the PHASE 3B specification -- a statement that CHAIN-FLAG halts progression, not merely that it is emitted and visible. Without a blocking condition CHAIN-FLAG is advisory; with it chain integrity failure is a production stop that cannot be bypassed by continued writing. Applicable only when C-19 is satisfied. |
| C-23 | **Distillation phase blocking condition with named gate** | behavior | The RULES-ANCHORED traceability check (C-20) names an explicit blocking condition: production cannot proceed to the next phase until all rules show ALIGNED. Pass requires the blocking condition to be stated by name in the phase specification -- not implied by the check's existence. Without a named gate, misaligned tier annotations are observable but non-blocking; a reviewer can note them and the artifact can still be completed. With a named gate, the distillation layer enforces the same production-stop semantics as C-16 and C-18's per-entry attestation gates. Applicable only when C-20 is satisfied. |
| C-24 | **Enforcement mechanism section at artifact head position** | behavior | The C-21 independently navigable section containing the enforcement mechanism declaration is placed at position 1 of the artifact -- before PBI, before Handle Ledger, before any entries. C-21 ensures the section is findable via heading navigation; C-24 ensures a reader who opens the artifact encounters enforcement mechanism classification before any content. Without head positioning a reviewer must navigate to the section; with it, the enforcement frame is the first interpretive lens, not a findable annotation. Pass requires the ENFORCEMENT MECHANISM section (or equivalent titled section) to appear before all other major sections. Applicable only when C-21 is satisfied. |
| C-25 | **CHAIN-FLAG resolution protocol with named repair action per flag type** | behavior | The CHAIN-FLAG production gate (C-22) specifies not only that production stops but how it restarts. For each type of CHAIN-FLAG (e.g., PBI-Ref mismatch, Handle mismatch, Source absent, Verified quotation inaccurate), there is exactly one named repair action. Without a resolution protocol a reviewer who encounters a CHAIN-FLAG knows to stop but must infer the fix; two reviewers may take different actions, both of which technically clear the flag without resolving the underlying inconsistency. With a named protocol, the gate is reparable in exactly one valid way per flag type: clearing the gate proves the chain inconsistency was fixed, not merely that someone continued past it. Pass requires the PHASE 3B specification to name a RESOLUTION PROTOCOL section or equivalent listing at least one flag type with its corresponding repair action. Applicable only when C-22 is satisfied. |
| C-26 | **NO-ECHO COST declaration in head-position enforcement section** | behavior | The C-24 head-position enforcement section includes a NO-ECHO COST declaration: a statement naming the institutional cost of artifact absence -- what the next team inherits if this artifact is skipped or not produced. Without it, the section classifies the enforcement mechanism and its properties, but carries no stake; a reviewer reads what the artifact is, not what is lost by skipping it. With a NO-ECHO COST declaration, the reviewer encounters both mechanism classification and institutional consequences before any entries -- the first-interpretive-lens property of C-24 conveys mechanism-with-stakes rather than mechanism-with-properties alone. Pass requires a named declaration in the head-position section (e.g., "NO-ECHO COST: ...") that identifies a specific failure class inherited by the next team in the artifact's absence. Generic statements ("this artifact is important") fail; a named failure class ("the next team inherits false assumptions about X without the ability to distinguish which beliefs were pre-committed versus post-hoc") passes. Applicable only when C-24 is satisfied. |
| C-27 | **Forward Statement names the specific avoided failure** | behavior | The terminal Forward Statement (or equivalent closing section addressed to the next team) names the specific failure that was avoided by completing this artifact -- the concrete instantiation of what would have propagated if the artifact had been absent. Without it, the Forward Statement summarizes findings but the institutional purpose claim opened by the artifact's framing remains unverified: the artifact said it would prevent a specific failure class, but completion does not confirm it did. With a named avoided failure, the Forward Statement closes the loop -- the institutional framing becomes a verifiable commitment honored at completion rather than a declaration made at the start. When C-26 is also present, this criterion additionally closes the specific loop opened by the NO-ECHO COST declaration: the cost declared at head position is confirmed or denied at completion. Pass requires the Forward Statement to name a failure class or specific error that this artifact's existence prevented -- not a restatement of what the artifact found. "The next team should investigate X" fails (advisory); "This echo prevented the next team from inheriting the assumption that Y, which would have misdirected the flow:lifecycle investigation toward Z" passes (specific avoided failure). Applicable only when C-07 is satisfied. |
| C-28 | **RULES-ANCHORED-COMPLETE closure token in distillation phase** | behavior | The RULES-ANCHORED check that gates distillation-phase exit (C-23) emits a named RULES-ANCHORED-COMPLETE token when all rules confirm tier alignment. Without the token, a downstream reviewer must re-run the tier-alignment check to confirm the distillation phase closed correctly; the blocking condition (C-23) makes failure visible but success invisible. With the token, distillation-phase exit is auditable from output alone -- the same property that CHAIN-COMPLETE (C-19) provides for the chain audit phase. Pass requires a named RULES-ANCHORED-COMPLETE token (or equivalent) in the distillation phase output that is only emitted when all rules pass the ALIGNED check -- not present when any rule shows MISALIGNED. The two tokens together bracket the artifact's two major audit phases: CHAIN-COMPLETE closes the chain audit, RULES-ANCHORED-COMPLETE closes the distillation audit. Applicable only when C-23 is satisfied. |
| C-29 | **RESOLUTION PROTOCOL as peer-level standalone declaration block** | behavior | The RESOLUTION PROTOCOL containing the per-flag-type repair actions (C-25) is formatted as a standalone ALL-CAPS headed declaration block at peer register with the GATEKEEPER FUNCTION DECLARATION -- not embedded as inline gate text. Without peer-level formatting, the repair-per-flag-type structure is findable by a reviewer who reads the gate specification carefully, but may be read past by a reviewer scanning for the blocking condition alone. With peer-level formatting, the RESOLUTION PROTOCOL is visually sovereign: a reviewer cannot encounter the gate without simultaneously encountering the repair routing at equivalent structural prominence. Pass requires the RESOLUTION PROTOCOL to appear as an independently titled block at the same heading level as the GATEKEEPER FUNCTION DECLARATION or equivalent gate declaration, not as a subordinate clause or inline paragraph within gate text. Applicable only when C-25 is satisfied. |
| C-30 | **EF role-boundary protection for NO-ECHO COST declaration** | behavior | The NO-ECHO COST declaration required by C-26 is derived by a role-scoped function (Enforcement Framer, EF) at Step 0 -- before any signal artifacts are read. Without role-boundary protection, the cost declaration can be written after reviewing signal content, making it potentially retrospective: a writer who observes the signals first may write a cost declaration shaped by what the signals say rather than what pre-investigation materials indicate. With EF role-boundary protection, the role scope structurally excludes signal entry content during Step 0: the cost is declared from pre-investigation materials only, ensuring the declaration is genuinely prospective. This applies the same structural-versus-temporal distinction from C-15/C-17 to the cost declaration: temporal provenance (write-order sequencing) is weaker than structural provenance (role-scope exclusion that prevents cross-phase reasoning regardless of instruction). Pass requires an explicit EF role scoped to pre-investigation materials to derive the NO-ECHO COST before the signal-reading phase opens. Applicable only when C-26 is satisfied. |
| C-31 | **RESOLUTION PROTOCOL with named verifier role per flag type** | behavior | The RESOLUTION PROTOCOL (C-29) names, for each flag type, a verifier role: the specific role whose attestation is required before the CHAIN-FLAG of that type can be cleared. Without a named verifier, the repair action is specified (C-25) and the routing is visible (C-29), but clearing is uncontrolled -- any reviewer or writer can attest repair completion. With a named verifier per flag type, clearing is role-accountable: only the designated role can certify that the named repair was correctly applied. The practical effect is that self-certification is structurally blocked: a writer whose artifact has a PBI-Ref CHAIN-FLAG cannot self-certify its resolution because the RESOLUTION PROTOCOL designates the BC role (not IA) as the verifier for PBI-Ref repairs. Pass requires each flag type entry in the RESOLUTION PROTOCOL to carry a Verifier: field naming the role responsible for attesting repair completion. Applicable only when C-29 is satisfied. |
| C-32 | **Evidentiary tier quotation in RULES-ANCHORED-COMPLETE token** | behavior | The RULES-ANCHORED-COMPLETE closure token (C-28) quotes the actual tier annotation string ([HIGH] or [MEDIUM]) for each rule before asserting alignment. Without per-rule quotation, the token declares that all rules are ALIGNED but a downstream reviewer must re-run the RULES-ANCHORED check to confirm which tier annotation was verified for each rule. With per-rule quotation, the token is evidentiary: it shows exactly what was checked, not merely that checking occurred. This applies the same principle as C-18 (evidentiary quotation in per-entry attestations) to phase-close tokens -- the closure token becomes a disclosure of evidence rather than a declaration of action. Pass requires the RULES-ANCHORED-COMPLETE token to quote the actual tier annotation string per rule (e.g., R-01 "[HIGH]" ALIGNED, R-02 "[MEDIUM]" ALIGNED) before emitting the distillation-phase-closed declaration. Applicable only when C-28 is satisfied. |
| C-33 | **EF-INVOCATION-RECORD at Step 0** | behavior | The EF role-boundary established by C-30 produces an EF-INVOCATION-RECORD: a discrete block immediately following the ENFORCEMENT MECHANISM DECLARATION that lists (1) pre-investigation materials consulted, (2) signal artifacts excluded by name, and (3) the cost derivation basis. Without an INVOCATION-RECORD, C-30's structural boundary is a specification requirement that is not observable from the artifact: a reviewer can confirm the EF function is scoped, but cannot verify which materials were consulted or which were excluded during Step 0. With an INVOCATION-RECORD, the boundary is made observable -- the exact pre-investigation materials are named, the exclusions are enumerated, and the derivation basis is stated. The C-30 structural commitment becomes an auditable record of what the EF function saw and did not see. Pass requires the Step 0 output to include an EF-INVOCATION-RECORD block immediately after the ENFORCEMENT MECHANISM DECLARATION, naming all three elements: materials consulted, signal artifacts excluded by name, and cost derivation basis. Applicable only when C-30 is satisfied. |
| C-34 | **BC-COVERAGE-RECORD** | behavior | The EF-INVOCATION-RECORD established by C-33 makes EF's scope observable from output. C-34 applies the identical standard to BC (Belief Compiler): BC produces a BC-COVERAGE-RECORD listing (1) signal artifacts processed by BC, (2) signal artifacts excluded by BC by name, and (3) the coverage derivation basis. Without BC-COVERAGE-RECORD, provenance is role-selective: EF is auditable, BC is not. A reviewer can confirm EF's exclusions from the artifact alone but must infer BC's scope from specification. With BC-COVERAGE-RECORD, provenance is role-symmetric: every exclusion-scoped role produces an equivalent observable record, and a reviewer can independently audit any role's scope from the artifact alone. Pass requires BC to produce a BC-COVERAGE-RECORD block listing all three elements: signal artifacts processed, signal artifacts excluded by name, and coverage derivation basis. Applicable only when C-33 is satisfied. |
| C-35 | **PHASE-HANDOVER tokens at EF-exit and BC-exit** | behavior | C-33 makes role entry auditable at invocation time (EF-INVOCATION-RECORD records what EF saw before acting). C-35 makes role exit auditable: EF emits a PHASE-HANDOVER-EF token immediately before handing off to BC, naming what EF produced; BC emits a PHASE-HANDOVER-BC token immediately before handing off to the distillation phase, naming what BC produced. Without PHASE-HANDOVER tokens, role transitions are entry-visible and exit-silent: a reviewer can confirm what each role started with but cannot read what each role delivered. With PHASE-HANDOVER tokens, every role transition is bookended -- the entry record (C-33/C-34) names what was seen; the exit token names what was produced. A reviewer can reconstruct the full handoff chain from the artifact alone: EF saw X (C-33), produced Y (PHASE-HANDOVER-EF); BC saw Y+Z (C-34), produced W (PHASE-HANDOVER-BC). Pass requires both PHASE-HANDOVER-EF and PHASE-HANDOVER-BC tokens to appear at their respective role-exit points, each naming what the exiting role produced before transition. Applicable only when C-33 is satisfied. |
| C-36 | **DISCARD LOG with typed entries and DISCARD-LOG-COMPLETE** | behavior | C-20 requires the distillation layer to extract the highest-impact surprises into Rules of Thumb with tier annotations, confirmed by RULES-ANCHORED traceability. The accept decisions of the STILL-LIVE FILTER are visible in output (accepted candidates appear as Rules of Thumb). C-36 requires reject decisions to be equally visible: each candidate the STILL-LIVE FILTER does not accept produces a typed DISCARD-[N] entry containing the candidate identifier, the reject route, and the reason for rejection. DISCARD-LOG-COMPLETE is emitted when all candidates have been accepted or discarded, summarizing the full candidate set. Without a DISCARD LOG, the distillation phase accounts only for accepted candidates: a reviewer cannot determine how many candidates were considered, which were excluded, or why. With a DISCARD LOG, the filter is fully transparent: accept and reject decisions are symmetrically visible, and DISCARD-LOG-COMPLETE confirms every candidate is accounted for. This applies the same completeness discipline to distillation-phase filtering that CHAIN-COMPLETE (C-19) and RULES-ANCHORED-COMPLETE (C-28) apply to their respective phases. Pass requires typed DISCARD-[N] entries for every non-accepted candidate (containing candidate identifier, route, and reason) and a DISCARD-LOG-COMPLETE token confirming the full candidate set has been enumerated. Applicable only when C-20 is satisfied. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 80 |
| Passing | All essential pass, composite < 80 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 140 points total (28 criteria, 5 points each)
- Max composite: 230

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 1/28 pass -> 1/28 * 140 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall

### Golden path (baseline)

- Essential: 5/5 -> 60
- Recommended: 2/3 -> 20
- Aspirational: 0/28 -> 0
- **Composite = 80** -- golden (all essential + composite >= 80)

### Golden path (full)

- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 28/28 -> 140
- **Composite = 230** -- maximum

---

## Criterion Relationships

**C-01 / C-04**: C-01 requires at least one named surprise with departure framing. C-04 requires
the artifact to contain only surprises -- no unsegregated summary content. Both must pass together:
an artifact can have named surprises (C-01) while burying them in a summary (C-04 fail).

**C-02 / C-05**: C-02 requires tracing to a named source artifact. C-05 requires specificity to
this investigation. An artifact can cite a specific source (C-02 pass) but describe a generic
observation not derived from that source content (C-05 fail).

**C-06 / C-07 tension**: C-06 is oriented backward (reconstructing the prior state). C-07 is
oriented forward (addressing the next team). An artifact that does both anchors the surprise in
history and projects it into the future.

**C-09 / C-10**: C-09 requires ranking all surprises. C-10 requires flagging the most dangerous
one. C-09 can be satisfied without C-10, and C-10 without C-09.

**C-06 / C-11**: C-06 requires the expected-X-found-Y structure per entry. C-11 requires the
expected state to have been committed before signal reading via a discrete PBI. C-06 can be
satisfied post-hoc; C-11 cannot. C-11 automatically satisfies C-06 but not the reverse. C-11
is the structural enforcement of what C-06 asks for rhetorically.

**C-01 / C-12**: C-01 requires named surprises with departure framing. C-12 requires each
surprise to also carry a reusable handle citable by future artifacts. C-05 and C-12 reinforce
each other: a specific surprise is easier to name concisely.

**C-11 + C-12 / C-13**: C-13 is inapplicable if either C-11 or C-12 is absent. Given both,
C-13 tests whether the two pre-commitments are genuinely independent or co-constructed. PBI
entries must use belief language; Handle Ledger titles must use finding language that PBI
entries could not have anticipated.

**C-13 + C-14**: C-13 tests independence between sections (macro level). C-14 tests integration
within entries (micro level). Satisfying both establishes the pre-commitments are independent
at macro and composable at micro.

**C-11 / C-15**: C-11 is the structural minimum (PBI section exists, is addressable). C-15 is
the provenance layer (the isolation mechanism is declared and legible). An artifact can satisfy
C-11 while failing C-15 (no declaration of phase gate vs role boundary). With C-15 satisfied
the enforcement mechanism is stated; without it the reviewer must infer quality from content
analysis alone.

**C-13 / C-15**: C-13 tests independence via content evidence (language analysis). C-15 tests
independence via mechanism evidence (provenance declaration). Both target genuine pre-commitment
through different lenses. The strongest artifacts satisfy both: mechanism was sound (C-15) and
content confirms it (C-13).

**C-14 / C-16**: C-14 is the structural requirement (three pointers present). C-16 is the
evidence layer (pointers were checked at production time, not just present). Satisfying both
shifts audit burden from reviewer to producer and makes the audit chain both genuine and legible.

**C-15 / C-17**: C-15 is the identification layer (which mechanism). C-17 is the calibration
layer (how strong, and why). An artifact can satisfy C-15 (mechanism named) while failing C-17
(no tier, no distinguishing property). C-17 exists because a mechanism name alone requires a
reviewer to independently know the hierarchy to calibrate; a mechanism name plus tier plus
rationale makes calibration self-contained. Practical test: can a reviewer unfamiliar with the
hierarchy immediately know how much weight to place on the independence claim? C-15 alone: no.
C-15 + C-17: yes.

**C-16 / C-18**: C-16 is the attestation layer (checks were performed; here are their
identifiers). C-18 is the evidence layer (here is what was found at those identifiers). An
artifact can satisfy C-16 (Verified field names all three checks with identifiers) while failing
C-18 (no quotation of actual attested text). Without quotation a reviewer must navigate to PBI
and signal artifact to confirm identifiers point to the right content. With quotation, both
confirmations are possible from the entry alone. C-18 completes the self-containment goal:
the full evidentiary chain -- pointers, attestation, and actual texts -- is visible at the
surprise entry without navigation.

**C-18 / C-19**: C-18 is the evidence layer (attestations contain quotations). C-19 is the
audit layer (attestations were re-verified for correctness after production). An artifact can
satisfy C-18 (quotations present and substantive) while failing C-19 (no post-production
verification that the quotations accurately represent the source content). C-19 closes the
final gap in the chain: C-16 confirms checks happened, C-18 shows what was found, C-19
confirms what was found was correctly quoted. The three layers together make the chain
self-auditing without reviewer re-derivation.

**C-19 / C-22**: C-19 requires the Chain Integrity Audit to emit CHAIN-FLAG tokens. C-22
requires those tokens to gate production -- CHAIN-FLAG must halt further completion until
resolved. An artifact can satisfy C-19 (tokens are visible) while failing C-22 (no blocking
condition stated; reviewer can proceed past flags). C-22 converts the audit from a transparency
mechanism into an enforcement mechanism: the audit does not merely report chain state, it
controls whether production continues.

**C-09 / C-20**: C-09 requires a defensible impact hierarchy. C-20 requires the highest-impact
findings from that hierarchy to be distilled into a citable form and verified against the
hierarchy. C-20 cannot be satisfied without C-09 because the tier annotations and traceability
check are meaningless without a proven hierarchy to check against. C-09 produces the hierarchy;
C-20 extracts and verifies a distillation of it.

**C-20 / C-23**: C-20 requires the RULES-ANCHORED check to confirm tier alignment. C-23 requires
that check to name a blocking condition that halts production until alignment is confirmed. An
artifact can satisfy C-20 (check performed, alignment stated) while failing C-23 (no blocking
condition; artifact can be completed with misaligned rules). C-23 makes the distillation layer
structurally equivalent to the entry-level attestation gates (C-16, C-18): the phase cannot
close until the check passes.

**C-17 / C-21**: C-17 is the classification layer (tier, property, implication). C-21 is the
navigability layer (classification is discoverable without full-read). An artifact can satisfy
C-17 at highest level (tier + property + reviewer implication) while failing C-21 (classification
embedded inline). C-21 rewards design for reviewers: the enforcement mechanism claim is
independently auditable without re-parsing the prose. Inline C-17 pass: minimum bar, no C-21.
Dedicated section C-17 + C-21 pass: highest level.

**C-21 / C-24**: C-21 requires the enforcement mechanism section to be independently navigable
(reachable via section headings without full-artifact reading). C-24 requires that section to
be at position 1 -- before PBI, before any entries. An artifact can satisfy C-21 (section
exists and is headed) while failing C-24 (section appears mid-artifact after PBI or entries).
C-24 makes orientation structural rather than navigational: the reader does not choose to find
the enforcement frame -- it is the first thing encountered. The distinction matters for trust
calibration: a reviewer who encounters enforcement mechanism classification before reading any
entries brings a different prior to the content than one who finds it mid-read or after.

**C-22 / C-25**: C-22 is the gate layer (CHAIN-FLAG stops production). C-25 is the repair layer
(for each flag type, there is exactly one named repair action). An artifact can satisfy C-22
(blocking condition stated) while failing C-25 (no resolution protocol; reviewer must infer
the fix). Without C-25, the gate stops production but leaves repair ambiguous: two reviewers
may take different actions, both of which clear the flag without fixing the underlying chain
inconsistency. With C-25, clearing the gate is deterministic -- the flag type determines the
repair action, and only that action satisfies the gate. Practical test: given a CHAIN-FLAG on
entry HL-03, can a reviewer who has never encountered this flag before determine the exact
repair action from the artifact specification alone? C-22 alone: no. C-22 + C-25: yes.

**C-24 / C-26**: C-24 is the positioning layer (enforcement section at position 1, before all
entries). C-26 is the stakes layer (head-position section declares the institutional cost of
artifact absence). An artifact can satisfy C-24 (section at position 1) while failing C-26
(section classifies mechanism and properties but declares no cost). Without C-26, the
head-position section tells a reviewer what enforcement mechanism is in use; with C-26, it
also tells the reviewer what is lost by skipping. The distinction matters for reviewer
disposition: encountering mechanism-classification-only at position 1 establishes frame but
not urgency; encountering mechanism-with-stakes establishes both, changing how the reviewer
reads the entries that follow.

**C-26 / C-27**: C-26 opens an institutional claim (specific failure class avoided if artifact
is present). C-27 closes it (Forward Statement names the specific failure that was actually
avoided). An artifact can satisfy C-26 (NO-ECHO COST declared at head) while failing C-27
(Forward Statement does not confirm which failure was avoided). Without C-27, the NO-ECHO COST
declaration is a forward-looking warning that the artifact never confirms; with C-27, the cost
claim is a commitment the artifact must honor before completion. Note: C-27 can be satisfied
without C-26 (Forward Statement names avoided failure even when no head-position cost
declaration exists), but its verifiable-commitment property only fully applies when C-26 is
also present -- otherwise there is no prior claim for the Forward Statement to close against.

**C-07 / C-27**: C-07 requires forward-facing intent (artifact addresses a future team). C-27
requires the specific forward-facing claim to be a named avoided failure, not a recommendation
or summary. An artifact can satisfy C-07 (forward framing present) while failing C-27 (forward
statement is advisory rather than verifying). C-27 makes the forward framing falsifiable: the
artifact does not merely point the next team forward but demonstrates that the forward-facing
claim was honored.

**C-23 / C-28**: C-23 is the blocking layer (RULES-ANCHORED check gates distillation-phase exit;
misaligned rules halt production). C-28 is the closure-visibility layer (RULES-ANCHORED-COMPLETE
token makes successful exit observable from output). An artifact can satisfy C-23 (blocking
condition present; misalignment stops production) while failing C-28 (no closure token; a
downstream reviewer cannot determine from output alone whether the distillation phase completed
successfully). With C-28, the two audit phases are symmetrically bracketed: CHAIN-COMPLETE/
CHAIN-FLAG (C-19) for the chain audit, RULES-ANCHORED-COMPLETE for the distillation audit.
C-23 alone: blockage visible, success silent. C-23 + C-28: both states visible.

**C-25 / C-29**: C-25 is the content layer (repair actions per flag type exist and are named).
C-29 is the structure layer (those repair actions are in a visually sovereign standalone block
at peer register with the gate declaration). An artifact can satisfy C-25 (repair actions
present, one per flag type) while failing C-29 (repair actions embedded as inline gate text,
not a peer-level block). Without C-29, a reviewer scanning the gate specification for the
blocking condition may read past the repair routing -- the named actions are findable on careful
reading but not structurally unavoidable. With C-29, the RESOLUTION PROTOCOL block is at the
same visual level as the GATEKEEPER FUNCTION DECLARATION: encountering the gate means
encountering the repair routing, not finding it.

**C-26 / C-30**: C-26 is the requirement layer (NO-ECHO COST declaration must appear in the
head-position enforcement section). C-30 is the provenance layer (that declaration must be
derived by a role-scoped function before signal reading). An artifact can satisfy C-26 (cost
declaration present and specific) while failing C-30 (declaration was written by the same
function that reads signals, allowing retrospective construction). Without C-30, C-26 is a
temporal commitment: the writer is instructed to declare cost before reading signals, but cross-
phase reasoning is not structurally blocked. With C-30, C-26 becomes a structural commitment:
the EF role's scope prevents the cost-writing function from accessing signal content regardless
of instruction. Practical test: could a writer reconstruct the cost declaration from signal
content after observing it? C-26 alone: yes. C-26 + C-30: no.

**C-29 / C-31**: C-29 is the structure layer (RESOLUTION PROTOCOL at peer register with the gate
declaration, visually sovereign). C-31 is the accountability layer (each repair action names a
verifier role whose attestation is required to clear the flag). An artifact can satisfy C-29
(RESOLUTION PROTOCOL block is visually prominent, peer-level) while failing C-31 (no verifier
role named; clearing is uncontrolled). Without C-31, the repair routing is visible and
unavoidable but clearing is open to any actor. With C-31, the RESOLUTION PROTOCOL is both
structurally unavoidable (C-29) and role-accountable: only the designated role can certify
that the named repair was correctly applied. C-29 prevents the routing from being missed; C-31
prevents the resolution from being self-certified.

**C-28 / C-32**: C-28 is the token layer (RULES-ANCHORED-COMPLETE emitted when all rules pass,
making distillation-phase success observable from output). C-32 is the evidence layer (the
token quotes the actual tier annotation string per rule, making it evidentiary rather than
declarative). An artifact can satisfy C-28 (closure token present, only emitted on full ALIGNED)
while failing C-32 (token is a declaration of success without quoting what was checked per
rule). Without C-32, a reviewer reads the token and knows the phase closed -- but must re-run
the check to confirm which tier annotation was verified for each rule. With C-32, the token
contains the evidence: each rule's annotation string is quoted. C-32 applies the same principle
as C-18 (per-entry attestation with evidentiary quotation) to phase-close tokens.

**C-30 / C-33**: C-30 is the boundary layer (EF role scoped to pre-investigation materials only;
cost declaration is structurally prospective, not instructed-sequential). C-33 is the
observability layer (Step 0 produces an EF-INVOCATION-RECORD listing materials consulted,
signal artifacts excluded, and cost derivation basis). An artifact can satisfy C-30 (EF
function declaration present, role scope enforced by specification) while failing C-33 (no
INVOCATION-RECORD; the boundary is a specification property only, not an observable output).
Without C-33, a reviewer can confirm the EF role exists and is scoped -- but cannot read which
pre-investigation materials were consulted or which signal artifacts were named as excluded.
With C-33, the EF function's invocation is publicly observable. C-30 makes the boundary
structural; C-33 makes it auditable.

**C-33 / C-34**: C-33 is the EF-invocation layer (EF produces an EF-INVOCATION-RECORD at Step 0
listing materials consulted, exclusions, and cost derivation basis -- making EF's scope boundary
observable). C-34 is the symmetry layer (BC produces a BC-COVERAGE-RECORD applying the identical
standard to the BC role). An artifact can satisfy C-33 (EF's invocation is auditable) while
failing C-34 (BC's coverage is not auditable). Without C-34, auditability is role-selective: EF
is observable, BC is not. A reviewer can audit EF's scope exclusions from the artifact alone
but must infer BC's scope from specification rather than reading it from output. With C-34,
auditability is role-symmetric: every exclusion-scoped role produces an equivalent coverage
record. Practical test: could a reviewer audit BC's scope exclusions from the artifact without
consulting the specification? C-33 alone: no. C-33 + C-34: yes.

**C-33 / C-35**: C-33 is the entry observability layer (EF's invocation at Step 0 is recorded at
entry time -- which materials it saw, which it excluded). C-35 is the exit observability layer
(EF and BC each emit a PHASE-HANDOVER token at role-exit, naming what they produced before
handing off). An artifact can satisfy C-33 (EF's entry is recorded) while failing C-35 (no
exit tokens; role transitions are entry-only observable). Without C-35, role boundaries are
observable at entry but silent at exit: a reviewer knows what each role started with but not
what each role delivered. With C-35, both sides of every role transition are observable -- the
entry record (what was seen) and the exit token (what was produced). Role transitions are
bookended rather than entry-only. Practical test: can a reviewer confirm what EF delivered to
BC from the artifact alone? C-33 alone: no. C-33 + C-35: yes.

**C-34 / C-35**: C-34 is the BC-entry layer (BC produces a coverage record making its scope
observable at entry). C-35 is the BC-exit layer (BC emits a PHASE-HANDOVER-BC token at exit,
naming what it produced before handoff). An artifact can satisfy C-34 (BC's coverage is
observable at entry) while failing C-35 (BC's handoff is not observable at exit). Without C-35,
BC is auditable at entry but silent at exit -- the reviewer knows what BC started with but not
what it delivered. With C-34 and C-35, BC is bookended: coverage record at entry, handover
token at exit. The combined effect of C-33 + C-34 + C-35 fully bookends all role transitions:
EF entry (C-33), BC entry (C-34), EF exit (C-35, PHASE-HANDOVER-EF), BC exit (C-35,
PHASE-HANDOVER-BC).

**C-20 / C-36**: C-20 is the distillation layer (Rules of Thumb extracted from high-impact
surprises, with tier annotations and RULES-ANCHORED traceability confirming alignment). C-36
is the transparency layer (every candidate not selected produces a typed DISCARD-[N] entry with
route and reason, closed by DISCARD-LOG-COMPLETE). An artifact can satisfy C-20 (distillation
layer present, accepted candidates visible as Rules of Thumb) while failing C-36 (rejected
candidates invisible; reviewer cannot reconstruct the full candidate set). Without C-36, the
distillation phase accounts only for accepted candidates: the Rules of Thumb show what was kept,
but a reviewer cannot determine how many candidates were considered or what led to rejection.
With C-36, the distillation phase is fully transparent: accepted candidates appear in Rules of
Thumb, rejected candidates appear in the DISCARD LOG, and DISCARD-LOG-COMPLETE confirms all
candidates are accounted for. This applies the same completeness discipline to filtering that
CHAIN-COMPLETE (C-19) and RULES-ANCHORED-COMPLETE (C-28) apply to their respective phases.
Practical test: can a reviewer determine whether a surprise was excluded from the distillation
layer, and why? C-20 alone: no. C-20 + C-36: yes.

---

## Historical criterion notes

**v11 -- three new criteria from Round 10:**

C-34 (behavior, gate: C-33): BC-COVERAGE-RECORD. C-33 makes EF's Step 0 invocation auditable;
C-34 applies the identical standard to BC -- every exclusion-scoped role produces a parallel
coverage record, converting role-selective auditability (EF only) into role-symmetric auditability
(all exclusion-scoped roles).

C-35 (behavior, gate: C-33): PHASE-HANDOVER tokens at EF-exit and BC-exit. C-33 made role entry
auditable at Step 0; C-35 makes role exit auditable -- EF and BC each emit a PHASE-HANDOVER token
naming what they produced before handing off. Role transitions are bookended: entry record + exit
token per role.

C-36 (behavior, gate: C-20): DISCARD LOG with typed entries and DISCARD-LOG-COMPLETE. C-20 makes
accepted distillation candidates visible (Rules of Thumb); C-36 makes rejected candidates equally
visible -- typed DISCARD-[N] entries with route and reason, closed by DISCARD-LOG-COMPLETE,
accounting for every candidate the distillation phase considered.

**v10 -- three new criteria from Round 9:**

C-31 (behavior, gate: C-29): RESOLUTION PROTOCOL with named verifier role per flag type. C-29
makes the repair routing visually sovereign; C-31 makes clearing role-accountable -- only the
designated role can certify repair completion, blocking self-certification by the writing function.

C-32 (behavior, gate: C-28): Evidentiary tier quotation in RULES-ANCHORED-COMPLETE token. C-28
makes distillation-phase exit observable via closure token; C-32 makes the token evidentiary --
the token quotes the actual tier annotation string per rule, applying C-18's evidence-disclosure
principle to phase-close tokens.

C-33 (behavior, gate: C-30): EF-INVOCATION-RECORD at Step 0. C-30 makes the cost declaration
structurally prospective via role-scope exclusion; C-33 makes the invocation observable -- the
record names materials consulted, signal artifacts excluded, and cost derivation basis, converting
the structural boundary from a specification property into an auditable output.

**v9 -- three new criteria from Round 8:**

C-28 (behavior, gate: C-23): RULES-ANCHORED-COMPLETE closure token in distillation phase.
C-23 makes RULES-ANCHORED a blocking gate; C-28 makes successful gate exit observable from
output -- the same auditable-closure discipline that C-19/CHAIN-COMPLETE applies to the chain
audit phase, now extended to the distillation audit phase.

C-29 (behavior, gate: C-25): RESOLUTION PROTOCOL as peer-level standalone declaration block.
C-25 requires named repair actions per flag type; C-29 requires those actions to be in a
visually sovereign standalone block at peer register with the gate declaration -- making the
repair routing structurally unavoidable, not merely findable.

C-30 (behavior, gate: C-26): EF role-boundary protection for NO-ECHO COST declaration. C-26
requires the cost declaration to appear at head position; C-30 requires it to be derived by a
role-scoped function before signal reading, converting the temporal commitment of C-26 into
a structural one -- the same structural-vs-temporal distinction from C-15/C-17 applied to the
cost declaration.

**v8 -- three new criteria from Round 7:**

C-25 (behavior, gate: C-22): CHAIN-FLAG resolution protocol with named repair action per flag
type. C-22 makes the gate a production stop; C-25 makes the gate deterministically reparable --
one valid repair action per flag type, eliminating ambiguous fixes that clear the flag without
resolving the inconsistency.

C-26 (behavior, gate: C-24): NO-ECHO COST declaration in the head-position enforcement section.
C-24 makes the section primary (position 1); C-26 makes it consequential -- the reviewer
encounters mechanism-with-stakes, not just mechanism-with-properties.

C-27 (behavior, gate: C-07): Forward Statement names the specific avoided failure. C-07 makes
the artifact forward-facing; C-27 makes the forward claim verifiable -- the institutional
purpose stated at the start is confirmed or denied at completion.

**v7 -- three new criteria from Round 6:**

C-22 (behavior, gate: C-19): Chain-flag progression gate. CHAIN-FLAG token from C-19 functions
as hard production gate -- any CHAIN-FLAG blocks further completion until resolved.

C-23 (behavior, gate: C-20): Distillation phase blocking condition with named gate. RULES-ANCHORED
check must name an explicit blocking condition; production cannot proceed until all rules show ALIGNED.

C-24 (behavior, gate: C-21): Enforcement mechanism section at artifact head position (position 1,
before PBI, Handle Ledger, and all entries).

**v6 -- three new criteria from Round 5:**

C-19 (behavior, gate: C-18): Post-production Chain Integrity Audit with CHAIN-COMPLETE/CHAIN-FLAG
tokens per entry. Distinct from C-16/C-18 attestation layer: C-19 re-verifies correctness of
attestations after production rather than attesting at production time.

C-20 (behavior, gate: C-09): Rules of Thumb distillation with tier annotations ([HIGH]/[MEDIUM])
and RULES-ANCHORED traceability check. Distillation is auditable extract of hierarchy, not summary.

C-21 (behavior, gate: C-17): Enforcement mechanism declaration in a discrete headed section
independently navigable without full-artifact reading.

**v5 -- two new criteria from Round 4:**

C-17 (correctness, gate: C-15): Artifact classifies its declared enforcement mechanism on the
strength hierarchy (structural > temporal) and states the distinguishing property. C-15 is the
declaration (which mechanism); C-17 is the calibration layer (how strong, and why).

C-18 (behavior, gate: C-16): Each surprise entry's production-time attestation quotes the
actual text of the PBI entry and source finding -- not just their identifiers. C-16 is the
attestation (checks were performed); C-18 is the evidence layer (here is what was checked).

**v4 -- two new criteria from Round 3:**

C-15 (correctness, gate: C-11): Artifact declares how its PBI was isolated from signal
knowledge. Temporal provenance (phase gate freeze) < structural provenance (role-scope
exclusion). Without a mechanism declaration a reviewer must re-derive pre-commitment quality
from content analysis alone.

C-16 (behavior, gate: C-14): Each surprise entry includes a production-time attestation
confirming all three audit pointers were verified before writing. Shifts audit burden from
reviewer obligation (C-14) to producer evidence (C-16).
