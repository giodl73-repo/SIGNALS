# Scorecard: listen-adoption — Round 7

**Rubric:** v7 | **Max:** 165 | **Golden threshold:** 80

---

## Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01–C-05 | 12 ea | P | P | P | P | P |
| C-06–C-08 | 10 ea | P | P | P | P | P |
| C-09–C-18 | 5 ea | P | P | P | P | P |
| **C-19** | 5 | P | P | **X** | P | P |
| **C-20** | 5 | P | P | P | P | P |
| **C-21** | 5 | P | P | **X** | P | P |
| **C-22** | 5 | P | P | **X** | P | P |
| **C-23** | 5 | P | P | P* | P | P |
| **Total** | **165** | **165** | **165** | **150** | **165** | **165** |

*V-03 C-23: marginal PASS — "## Verification Stage" satisfies the label requirement but lacks explicit mode-shift instruction; weakest C-23 in the cohort.

---

## V-03 Failure Cluster

V-03 fails C-19, C-21, and C-22 from a single root cause: no named CORRECTION BLOCK header, no explicit negative rule on the terminal section, and no self-verifying invariant.

- **C-19 FAIL:** "Original: / Corrected:" embedded in conditional prose allows narrative substitution ("I revised the entry to include I-PM") without violating visible structure.
- **C-21 FAIL:** "Audit Outcomes" table has no rule preventing corrected content from appearing in it. The prose correction format does not name a separate destination, leaving the terminal table as the plausible landing zone.
- **C-22 FAIL:** Terminal section records state (initial/revision/final) but makes no verifiable claim about structural elements elsewhere. An evaluator cannot check the correction without trusting the model's assertion.
- **C-23 PASS (marginal):** "## Verification Stage" is a named header — passes the label requirement. Would be the first to fail if C-23 were tightened to require explicit mode-shift instruction.

---

## Ranking

| Rank | Variation | Score | Distinguishing Property |
|------|-----------|-------|------------------------|
| 1 | **V-04** | 165 | Names C-19/C-20/C-21/C-22/C-23 by criterion ID in structural contract; invariant includes falsification counter-example; phase headers lock Rogers sequence architecturally |
| 2 | **V-05** | 165 | Most explicit VERIFICATION MODE instruction; competitor framing expected to deepen inertia depth |
| 3 | **V-02** | 165 | Evaluability note in invariant; archetype-first locks Rogers ordering structurally |
| 4 | **V-01** | 165 | Complete structural contract; reference baseline |
| 5 | **V-03** | 150 | C-19 + C-21 + C-22 fail cluster |

---

## Excellence Signals (V-04)

1. **Rubric criteria named by ID in the structural contract** — V-04 embeds C-19/C-20/C-21/C-22/C-23 by ID at the top of the prompt, making the rubric-to-structure mapping explicit. A model following the contract is by construction following the rubric.

2. **Falsification counter-example in the self-verifying invariant** — extends R6 Pattern 4 into the invariant itself: states not just the pass condition but the exact failure mode ("a 'Yes' row whose CORRECTION BLOCK Location points to a section that contains no CORRECTION BLOCK falsifies this invariant"). Auditable from both directions.

3. **Phase-as-structural-lock for sequence-dependent output** — PHASE 1 through PHASE 6 headers (with PHASE 3 as a named CHASM non-adoption phase) enforce Rogers ordering architecturally; the model cannot populate a later-phase row without completing the prior-phase header.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["Naming rubric criteria by ID in the structural contract: embedding C-19/C-20/C-21/C-22/C-23 by criterion ID in the top-of-prompt contract makes the rubric-to-structure mapping explicit and verifiable at design time; a model following the contract is by construction following the rubric; generalizes to any rubric with structural invariants", "Falsification counter-example embedded in the self-verifying invariant: stating what falsifies the claim (a Yes-row pointing to an empty section or a block without a BEFORE field) rather than only what passes it makes the invariant auditable from both directions; stronger than pass-condition-only statements because it names the exact failure mode the evaluation must detect", "Phase-as-structural-lock for sequence-dependent output: named PHASE 1 through PHASE 6 headers (with PHASE 3 as a named CHASM non-adoption phase) enforce Rogers ordering architecturally -- the model cannot populate a later-phase row without completing the prior-phase header; structural compliance is stronger than instructed compliance for ordered sequences"]}
```
ign does not affect
the correction/gate-state separation architecture.

**V-03 — C-21: FAIL**

The "Audit Outcomes" table has no explicit rule against containing corrected content. The prose
correction format ("show the original content and the corrected content before continuing") does
not name a distinct structural block and does not prohibit the corrected row from appearing inside
the Outcomes table. The design notes confirm: "A model that fails a check and writes the corrected
row directly into the Audit Outcomes table would co-locate corrected content with gate state,
failing C-21." No named CORRECTION BLOCK + no negative rule on the terminal section = C-21
cannot be enforced at design time. FAIL (0 pts).

**V-04 — C-21: PASS**

The structural contract names C-21 explicitly by criterion ID: "C-21 rule: SECTION K does NOT
contain corrected content. SECTION K references CORRECTION BLOCK locations only. An evaluator
reading SECTION K reads gate state, not corrected rows." The negative rule is stated directly
against the criterion it enforces. Strongest C-21 design — there is no ambiguity about which
section holds which type of content.

**V-05 — C-21: PASS**

Structural contract states: "C-21 rule: SECTION K does NOT contain corrected content. SECTION K
references CORRECTION BLOCK locations only." The VERIFICATION MODE instruction adds: "Corrected
content lives in CORRECTION BLOCKS here in Sections H, I, J." Dual reinforcement: negative rule
on SECTION K + positive placement rule before SECTION K. PASS.

---

### C-22 — Terminal section contains a self-verifying cross-reference invariant (5 pts)

**Pass condition:** The terminal section includes at least one claim whose truth can be verified
by reading the rest of the document, naming a structural element and asserting a verifiable
property about it. Fails automatically if C-20 fails.

**V-01 — C-22: PASS**

SECTION K contains: "For every 'Revision Performed: Yes' entry in SECTION K, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK
Location column entry. An evaluator can confirm or refute this claim by inspection without trusting
the model's assertion." Names the structural element (CORRECTION BLOCK), asserts a verifiable
property (exists earlier, at the cited location, with BEFORE and AFTER fields). PASS.

**V-02 — C-22: PASS**

SECTION K contains the same invariant plus an explicit evaluability note: "This invariant is
evaluable: an evaluator reading this table can verify every Yes-row against the document and find
a CORRECTION BLOCK at the cited location." The evaluability note makes the verification procedure
explicit — it is the strongest simple-invariant design among the non-V-04 variations. PASS.

**V-03 — C-22: FAIL**

The "Audit Outcomes" table has Initial/Revision/Final columns but makes no verifiable claim about
the rest of the document. It records state; it does not assert a property about structural elements
elsewhere in the artifact. An evaluator reading only the Outcomes table has no basis to verify
whether the claimed revision occurred without trusting the model's assertion. The design notes
confirm: "terminal section has no named invariant." FAIL (0 pts).

**V-04 — C-22: PASS**

SECTION K contains the invariant with a counter-example of falsification: "For every 'Revision
Performed: Yes' entry in SECTION K, a CORRECTION BLOCK containing BEFORE and AFTER content exists
earlier in this document at the CORRECTION BLOCK Location cited. This claim is verifiable by
inspection — an evaluator can confirm or refute it without relying on this assertion. Failure mode:
a 'Yes' row whose CORRECTION BLOCK Location points to a section that contains no CORRECTION BLOCK,
or whose CORRECTION BLOCK contains no BEFORE field, falsifies this invariant."

Strongest C-22 design: the invariant names pass condition AND falsification condition. An evaluator
can check both directions. PASS.

**V-05 — C-22: PASS**

SECTION K contains: "For every 'Revision Performed: Yes' entry below, a CORRECTION BLOCK
containing BEFORE and AFTER content exists earlier in this document at the CORRECTION BLOCK
Location cited. An evaluator can verify this invariant by inspecting the cited location." Clean
invariant statement; evaluability is made explicit. PASS.

---

### C-23 — Named verification boundary separates content from audit stage (5 pts)

**Pass condition:** A named structural marker (section header or equivalent label) explicitly
signals the transition from content generation to the verification/audit stage. Content sections
appear before; audit sections (C-16 block, terminal section) appear after. Horizontal rule or
blank line without a label does not pass. Fails automatically if C-16 fails.

**V-01 — C-23: PASS**

"## VERIFICATION MODE" header appears between SECTION G and SECTION H. The header is immediately
followed by: "Content generation (Sections A–G) is complete. Sections H through K are the audit
stage. Do not generate new content — verify and correct existing content only." Named marker +
explicit mode-shift instruction. PASS.

**V-02 — C-23: PASS**

"## VERIFICATION MODE" header with "Content generation (Sections A–G) is complete. Sections H
through K are the audit stage. Do not generate new domain content. Verify and correct existing
content only." Same structure as V-01. PASS.

**V-03 — C-23: PASS (weakest implementation)**

"## Verification Stage" header appears before Check 1/2/3 and after Step 8. This is a named
section header — it satisfies the criterion's label requirement. The header name ("Verification
Stage") implies the transition from generation to verification. However, no explicit mode-shift
instruction accompanies the header ("do not generate new domain content after this point" is
absent), making this the weakest C-23 implementation. The criterion does not require a mode-shift
instruction — only a named marker. Per design notes: "PASS-RISK." Scored as PASS on the
basis that the named header satisfies the criterion's literal requirement, but the absence of an
explicit instruction reduces enforcement confidence. PASS (5 pts — minimum qualifying design).

**V-04 — C-23: PASS**

The structural contract pre-declares the boundary: "Verification boundary (C-23): The ##
VERIFICATION MODE header is a named boundary between content generation (Phases 1-6) and the
audit stage (Sections H through K). It signals an explicit mode shift. All domain content appears
before this header. No domain content appears after it." The boundary rule is named by criterion
ID before the artifact begins. PASS — strongest design with pre-declared boundary rule.

**V-05 — C-23: PASS**

"## VERIFICATION MODE" with the most explicit instruction of any variation: "You have finished
generating content (Sections A–G). This header marks the mode boundary. From this point forward,
you are auditing, not creating. Do not introduce new domain analysis, new inertia entries, or new
champion rationale after this point." The instruction specifies prohibited content types explicitly,
not just the mode label. PASS.

---

## Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-02 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-03 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-04 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-05 | 12 | 12 | 12 | 12 | 12 | 12 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-09 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-17 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-18 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-19 | 5 | 5 | 5 | **0** | 5 | 5 |
| C-20 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-21 | 5 | 5 | 5 | **0** | 5 | 5 |
| C-22 | 5 | 5 | 5 | **0** | 5 | 5 |
| C-23 | 5 | 5 | 5 | 5 | 5 | 5 |
| **Total** | **165** | **165** | **165** | **150** | **165** | **165** |

---

## V-03 Failure Analysis

V-03 fails C-19, C-21, and C-22 — the same three criteria that depend on a named structural
correction block and a self-verifying terminal invariant.

**Root cause:** V-03's verification stage uses conversational prose guidance ("show the original
content and the corrected content") without a named structural block header. The absence of a
named slot means:

1. **C-19:** The model can substitute narrative for content ("I revised the champion entry to
   include I-PM") without violating visible prompt structure.
2. **C-21:** The "Audit Outcomes" table has no negative rule preventing corrected content from
   appearing in it. The prose format does not name a separate destination for corrections, leaving
   the terminal table as the plausible landing zone.
3. **C-22:** The terminal section has no verifiable claim. The Initial/Revision/Final table records
   state; nothing in V-03 asserts a cross-document property an evaluator can check.

**C-23 PASS (marginal):** "## Verification Stage" is a named header, satisfying the criterion's
literal label requirement. V-03 avoids a fourth failure on C-23 only because the criterion does
not require a mode-shift instruction — only a named marker. V-03's C-23 design is the weakest
in the cohort; it would be the first to fail if C-23 were tightened to require explicit instruction.

**Causal path for V-03:** no structural contract + no named CORRECTION BLOCK + no negative rule
on terminal section + no self-verifying invariant = C-19 + C-21 + C-22 fail cluster.

---

## Ranking

| Rank | Variation | Score | Distinguishing Property |
|------|-----------|-------|------------------------|
| 1 | **V-04** | 165 | Names C-19/C-20/C-21/C-22/C-23 by criterion ID in structural contract; invariant includes falsification counter-example; phase headers lock Rogers sequence architecturally |
| 2 | **V-05** | 165 | Most explicit VERIFICATION MODE instruction ("you are auditing, not creating; do not introduce new domain analysis"); competitor framing expected to deepen inertia and chasm analysis |
| 3 | **V-02** | 165 | Evaluability note in invariant makes verification procedure explicit; archetype-first locks Rogers ordering structurally |
| 4 | **V-01** | 165 | Correct and complete structural contract; all C-21/C-22/C-23 requirements met; reference baseline |
| 5 | **V-03** | 150 | C-19 + C-21 + C-22 fail cluster from absent structural contract and named correction block; C-23 passes on minimum qualifying design |

---

## Excellence Signals (V-04)

**1. Naming rubric criteria by ID inside the structural contract**

V-04 references C-19, C-20, C-21, C-22, and C-23 by criterion ID at the top of the prompt:
"C-19 location: ...", "C-20 location: ...", "C-21 rule: ...", "C-22, asserted in SECTION K: ...",
"Verification boundary (C-23): ..." This is a new pattern not present in R6 variations. Prior
versions named structural locations and rules; V-04 names the *rubric criteria* those locations
serve. The effect is that the structural contract doubles as a rubric-to-structure mapping — a
model following the contract is, by construction, following the rubric. This pattern generalizes:
for any rubric with structural invariants, embedding criterion IDs into the prompt contract
makes the rubric-structure relationship explicit and verifiable at design time.

**2. Falsification counter-example embedded in the self-verifying invariant**

V-04's SECTION K invariant includes: "Failure mode: a 'Yes' row whose CORRECTION BLOCK Location
points to a section that contains no CORRECTION BLOCK, or whose CORRECTION BLOCK contains no
BEFORE field, falsifies this invariant." This extends R6's Pattern 4 (counter-example in template
cell) into the invariant statement itself. Prior rounds stated the pass condition; V-04 also states
the falsification condition. An evaluator can now approach the invariant from either direction —
confirm it by finding a CORRECTION BLOCK at every Yes-row location, or refute it by finding a
Yes-row that points to an empty section or a block without a BEFORE field. Stating what falsifies
a claim is stronger than stating only what passes it, because it names the exact failure mode the
evaluation is designed to detect.

**3. Phase-as-structural-lock enforces Rogers ordering architecturally**

V-04 uses PHASE 1 (INNOVATORS) through PHASE 6 (LAGGARDS) as document structure, with PHASE 3
named "CHASM" as a non-adoption phase between PHASE 2 and PHASE 4. This architectural approach
means Rogers sequence cannot be violated without violating document structure: the model must
complete PHASE 2 before opening PHASE 3/CHASM, and cannot populate PHASE 4 rows before writing
the PHASE 3 header. Prior variations instructed Rogers ordering; V-04 enforces it through phase
headers. This pattern generalizes to any sequence-dependent output: named phase boundaries are
stronger than sequence instructions because they require structural compliance rather than semantic
compliance.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["Naming rubric criteria by ID in the structural contract: embedding C-19/C-20/C-21/C-22/C-23 by criterion ID in the top-of-prompt contract makes the rubric-to-structure mapping explicit and verifiable at design time; a model following the contract is by construction following the rubric; generalizes to any rubric with structural invariants", "Falsification counter-example embedded in the self-verifying invariant: stating what falsifies the claim (a Yes-row pointing to an empty section or a block without a BEFORE field) rather than only what passes it makes the invariant auditable from both directions; stronger than pass-condition-only statements because it names the exact failure mode the evaluation must detect", "Phase-as-structural-lock for sequence-dependent output: named PHASE 1 through PHASE 6 headers (with PHASE 3 as a named CHASM non-adoption phase) enforce Rogers ordering architecturally -- the model cannot populate a later-phase row without completing the prior-phase header; structural compliance is stronger than instructed compliance for ordered sequences"]}
```
