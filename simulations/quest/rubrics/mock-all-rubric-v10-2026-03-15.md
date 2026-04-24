**v10 written.** One new criterion extracted from V-04:

---

**C-23** — *Per-role headers contain explicit positive identity affirmation at each activation point*

The key distinction between V-02 (14/14) and V-04 (ceiling):
- V-02 per-role header: `"Writing an artifact body here means you are ROLE 2 — GENERATOR, which you are not yet."` — names the wrong entity (C-22 pass), but positive identity lives only in the preamble
- V-04 per-role header: `"You ARE the CLASSIFIER. Writing an artifact body here means you are no longer the CLASSIFIER — you have become the GENERATOR, which you are not yet."` — re-anchors positive identity at each activation point

C-23 requires the two-part per-role header: (1) `You ARE the [SPECIFIC ROLE]` + (2) entity-transition statement. A preamble that says "you are that role while it is active" satisfies C-18 but not C-23. The positive affirmation must fire at each boundary, not once generically.

**Denominator: 14 → 15**

The three-rung staircase is now explicit in the Design Notes:
- C-18: named role + any violation mechanism (minimum)
- C-22: violation mechanism must be ontological self-contradiction (not prohibition)
- C-23: positive identity affirmation must appear at each activation header (not just preamble)
tion
statement ("you have become the GENERATOR, which you are not yet"). V-02 passes C-22 via per-role
violation statement naming the wrong entity; V-04 is the ceiling because each activation header
re-anchors positive identity before stating the consequence. This informs C-23 as a distinct
criterion rather than a further annotation to C-22.

Denominator updated from 14 to 15.

---

## Criteria

### Essential (must all pass — 60% weight)

**C-01** — All nine namespaces present with MOCK ARTIFACT header blocks
- Weight: essential
- Category: correctness
- Pass condition: Output contains exactly 9 namespace sections (scout, draft, review, flow,
  trace, prove, listen, program, topic), each opening with a MOCK ARTIFACT block that includes
  Skill, Topic, Category, Date, and Status: MOCK fields. Any missing namespace or missing header
  field is a fail.

**C-02** — Category classification correct for every namespace
- Weight: essential
- Category: correctness
- Pass condition: prove-* and listen-* sections are classified EVIDENCE-HEAVY; scout, draft,
  review, flow, trace are classified HIGH-STRUCTURE; program and topic are classified MIXED or
  HIGH-STRUCTURE. No namespace may carry a category that contradicts the skill spec's
  HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED taxonomy.

**C-03** — REAL-REQUIRED flag applied to all EVIDENCE-HEAVY namespaces
- Weight: essential
- Category: behavior
- Pass condition: Every section whose Category is EVIDENCE-HEAVY (prove-*, listen-*) carries a
  REAL-REQUIRED flag — either in the header block or immediately beneath it. Absence of the flag
  in any EVIDENCE-HEAVY section is a fail.

**C-04** — Coverage summary table present with correct columns
- Weight: essential
- Category: format
- Pass condition: Output ends with a Markdown table whose columns are exactly: Namespace,
  Category, Flag, Recommended next step. Table contains one row per namespace (9 rows). Missing
  table, wrong column names, or fewer than 9 rows is a fail.

**C-05** — Final line follows the prescribed handoff pattern
- Weight: essential
- Category: format
- Pass condition: The very last line of the output is `Next: /mock:review {topic} {this-file}`
  where `{topic}` is the topic name supplied to the skill and `{this-file}` resolves to the
  artifact filename just produced. Literal placeholder tokens in the output are a fail.

*(unchanged from v1)*

---

### Recommended (raise output quality — 30% weight)

**C-06** — Tier 2/3 critical namespaces flagged in coverage summary
- Weight: recommended
- Category: coverage
- Pass condition: Rows for trace, scout-feasibility, and listen in the coverage summary table
  each carry a visible Tier-critical annotation (e.g., "TIER-2-CRITICAL" or "TIER-3-CRITICAL")
  in the Flag column. Absence of tier annotation on any of these three rows is a partial fail
  (each missing annotation reduces score proportionally across the recommended band).

**C-07** — Each namespace section contains a plausible synthetic artifact body
- Weight: recommended
- Category: depth
- Pass condition: Below the MOCK ARTIFACT header, each namespace section includes at least
  3 substantive content lines that represent realistic synthetic signal content for that
  namespace (not generic filler). Header-only sections with no artifact body are a fail for
  this criterion.

**C-08** — Compliance-tagged topics pre-flagged REAL-REQUIRED in summary
- Weight: recommended
- Category: behavior
- Pass condition: When the topic has scout-compliance or trace-permissions skills present (or
  the --compliance flag is passed), those rows in the coverage table carry REAL-REQUIRED in the
  Flag column regardless of the structural quality of the synthetic artifact. If the topic has
  no compliance-tagged skills, this criterion is skipped (auto-pass).

*(unchanged from v1)*

---

### Aspirational (raise the bar — 10% weight; denominator = 15)

**C-09** *(unchanged)* — Tier flag correctly scopes output when --tier is supplied
> When invoked with --tier 2 or --tier 3, the output only produces namespace sections and
> coverage rows for namespaces at or above that tier level. Tier 1 (default) must produce all 9
> namespaces. Output that ignores the --tier flag or produces wrong namespace sets fails this
> criterion.

**C-10** *(unchanged)* — Recommended next steps are actionable and namespace-specific
> Every row's "Recommended next step" cell names a concrete skill invocation (e.g.,
> `/scout:feasibility {topic}`, `/prove:prototype {topic}`) rather than generic advice such as
> "gather more data" or "run the skill". Rows with non-specific guidance fail this criterion.

**C-11** *(added v2)* — Category classification table generated before any artifact body
> Pre-classify-then-generate ordering: a table assigning every namespace its Category must
> appear before the first artifact body is written. Interleaved or per-section classification
> does not pass.

**C-12** *(added v2)* — Handoff instruction isolated in a dedicated, explicitly-labelled section
> The `Next: /mock:review` line must appear in its own numbered/labelled block (e.g. "FINAL
> LINE"), structurally separate from the coverage table, with explicit anti-placeholder language
> for `{this-file}`.

**C-13** *(added v2)* — REAL-REQUIRED flag accompanied by explanatory rationale
> Every REAL-REQUIRED application must include a one-line rationale ("A synthetic artifact
> cannot substitute for real signal..."). Rationale may appear once as a preamble rule scoped
> to all placements.

**C-14** *(added v3)* — Explicit stop-gate phrase at each phase boundary
> When the skill defines named phases, each boundary must include an explicit stop-gate phrase
> such as "Do not proceed to [Phase N+1] until [Phase N output] is complete." Implied ordering
> via phase names or step labels alone does not pass.

**C-15** *(added v3)* — Artifact body content matches the namespace's assigned category
> Each synthetic artifact body must use language appropriate to its assigned category:
> EVIDENCE-HEAVY namespaces (prove, listen) use study/data/interview language; HIGH-STRUCTURE
> namespaces (trace, flow) use interface/contract/specification language; SIGNAL-RICH namespaces
> use discovery/signal language. Positive guidance alone ("use X framing") is insufficient --
> explicit DO NOT prohibition clauses are required per category to prevent register drift.
> **A skill that provides MUST vocabulary without corresponding DO NOT prohibitions earns
> PARTIAL credit only.**

**C-16** *(added v4)* — Stop-gate phrases enumerate specific required output fields
> A stop-gate phrase must name the specific fields or rows the model must have produced before
> proceeding -- not just signal generic task completion. "Do not begin PHASE 2 until all nine
> namespaces have an assigned Category, Tier 2/3 Critical value, and Compliance-Tagged value"
> passes. "Do not begin PHASE 2 until PHASE 1 is complete" does not -- without enumerated
> completeness criteria, the model can satisfy the gate with a partially-filled table.

**C-17** *(added v4)* — Vocabulary rules anchored as columns in the classification table
> MUST/DO NOT vocabulary constraints must appear as columns in the classification table itself,
> co-located with the category assignment row -- not in a separate vocabulary section written
> after classification. A skill that places vocabulary rules in a downstream prose block does
> not pass, even if those rules are otherwise correct and complete.

**C-18** *(added v6)* — Named role-identity assignment per phase
> Each phase must assign a named role identity (e.g., CLASSIFIER, GENERATOR, SUMMARIZER,
> HANDOFF WRITER) rather than only step or phase numbers. The role name must make wrong-phase
> behavior an identity violation -- the model knows it *is* the CLASSIFIER, not merely *is in
> step 1*. Phase labels or STEP numbers alone do not pass. Role identity blocks cross-phase
> contamination (e.g., generating artifact bodies during classification) at the ontological
> level, beyond what stop-gate phrases (C-14) enforce.
>
> *R8 confirmation (V-01):* Per-role "You ARE" repetition is not the load-bearing element.
> A single preamble that establishes the identity-violation mechanism ("crossing role boundaries
> is an identity violation") combined with per-phase role-name headers (e.g., `## ROLE 1:
> CLASSIFIER`) is the minimum sufficient form. Per-role repetition is redundant amplification.
> The two load-bearing elements are: (1) named role at each phase boundary, and (2) the
> identity-violation mechanism established somewhere in the skill before the first phase begins.

**C-19** *(added v7; confirmed v8)* — Artifact template placeholder contains an inline depth anchor
> The template body placeholder must embed a length and depth constraint directly inside the
> placeholder token itself -- for example, `{3-5 sentence artifact body, written in MUST
> vocabulary for this namespace, grounded in {topic}}`. A depth instruction placed in prose
> before or after the placeholder, even within the same role block, does not pass. The
> constraint must be readable at the exact point of generation without requiring the model to
> scan surrounding text. Template-level co-location (depth inside the placeholder) is distinct
> from table-level co-location (C-17); each satisfies only its own criterion.
>
> *R7 confirmation (V-02, V-05):* The passing form is `{3-5 sentence artifact body -- register
> matches Category...}` -- sentence count as the first token element. `{artifact body --
> vocabulary-compliant...}` without a count fails.

**C-20** *(added v7; confirmed v8)* — Inertia question anchors artifact body semantic quality
> Each namespace section must pose an inertia question of the form "Without this signal,
> {topic}'s feature story would be missing: ___" that the model answers before writing the
> artifact body. The artifact body must be traceable to the inertia answer -- a body that could
> have been written without answering the question is too generic and must be revised.
> Additionally, recommended next steps for that namespace must address the specific gap named in
> the inertia answer; generic next steps derived solely from category assignment do not pass
> when an inertia answer is present. Vocabulary compliance alone (C-15) does not substitute for
> inertia-grounded specificity.
>
> *R7 confirmation (V-03, V-05):* The passing form for next-step derivation is an explicit
> bridge instruction in ROLE 3: "the skill call that closes the specific gap named in this
> namespace's inertia statement from ROLE 2 -- Derive from the inertia answer. A recommendation
> valid for any topic or namespace without reference to the inertia answer is not valid here."
> An explicit gate rejection is required: "inertia-disconnected next step fails this gate."

**C-21** *(added v9)* — Inertia gap skeleton pre-seeded in classification table
> The ROLE 1 classification table must include an "Inertia gap skeleton" column that pre-seeds
> the namespace-level epistemic cost before the topic is applied. The skeleton partial answer
> takes the form "Without this signal, {topic}'s story would be missing: ___" with the
> namespace-specific gap filled in (e.g., for `prove`: "...empirical validation of the core
> hypothesis"; for `trace`: "...the contract surface and failure modes of the integration
> boundary"). ROLE 2 then completes the blank with topic-specific content, making topic
> specificity additive rather than originating. A ROLE 2 inertia question posed free-form
> without a namespace-level skeleton in the ROLE 1 table does not pass this criterion, even if
> C-20 is otherwise satisfied. Pre-seeding in the classification table is the load-bearing
> element; the ROLE 2 free-form inertia question satisfies C-20 but not C-21.
>
> *R8 origin (V-02):* The passing form adds an eighth column to the ROLE 1 table: "Inertia gap
> skeleton: Without this signal, {topic}'s story would be missing: ___" with the
> namespace-specific blank pre-filled. ROLE 2 completes the blank with topic-specific content.
> Effect: ROLE 2 answers are namespace-pre-seeded, not free-form; namespace epistemic cost is
> anchored at classification time, not deferred to generation time.

**C-22** *(added v9)* — Role identity violation mechanism is ontological, not behavioral
> The identity-violation mechanism that makes wrong-phase behavior impossible must be framed as
> self-contradiction -- "You ARE the CLASSIFIER; generating artifact bodies makes you NOT the
> CLASSIFIER" -- rather than as rule violation -- "Generating artifact bodies is prohibited."
> Prohibition-forward framing names forbidden behaviors and earns PARTIAL credit; it does not
> establish the ontological self-contradiction that makes the violation an identity failure
> rather than a rule infraction. The diagnostic test: can the model conceive of itself as still
> being the CLASSIFIER while violating the instruction? Prohibition answers: no (rule violated).
> Identity answers: no (you have ceased to be who you are). Only the identity form satisfies
> this criterion. Prohibition-forward forms satisfy C-14 (behavioral stop-gate) but not C-22.
> Note: C-22 is a higher bar than C-18 along the same dimension -- a skill can pass C-18
> (named role + any violation mechanism) while failing C-22 (violation mechanism must be
> ontological specifically).
>
> *R8 origin (V-03):* V-03 replaced "You ARE the CLASSIFIER" with "CLASSIFIER: generate X
> only. Generating Y is prohibited." Role name present; identity mechanism absent. Verdict:
> PARTIAL on C-18. The scorecard finding: "the rubric's test is specifically about *identity*
> violation, not *behavioral* prohibition... prohibition says the behavior is forbidden; identity
> says the behavior is self-contradictory." The distinction warranted a dedicated criterion.
>
> *R9 confirmation (V-04):* V-04 demonstrates the ceiling form for C-22 at per-role headers
> ("Writing an artifact body here means you are no longer the CLASSIFIER -- you have become the
> GENERATOR, which you are not yet"). This per-role entity-transition form passes C-22. The
> ceiling combination -- positive affirmation at activation + entity-transition naming -- is
> captured by C-23.

**C-23** *(added v10)* — Per-role headers contain explicit positive identity affirmation at each activation point
> Each per-role boundary header must carry an explicit "You ARE the [ROLE]" positive identity
> statement at the activation point itself -- not deferred to a preamble that generically states
> "you are that role while it is active." The ceiling form combines two elements in a single
> per-role header: (1) positive identity affirmation ("You ARE the CLASSIFIER") and (2)
> entity-transition violation statement ("you have become the GENERATOR, which you are not
> yet"). Both elements must appear in the per-role header to pass. A generic preamble
> establishing identity-violation combined with per-role violation statements (naming the wrong
> entity) satisfies C-22 but not C-23 -- the positive affirmation must fire at each activation
> boundary, not only in the preamble. The diagnostic test: does each role-activation header
> contain "You ARE the [SPECIFIC ROLE]" (not "you are that role") as its first element?
>
> *R9 origin (V-04):* V-04 per-role header: "You ARE the CLASSIFIER. Writing an artifact body
> here means you are no longer the CLASSIFIER -- you have become the GENERATOR, which you are
> not yet." V-02 per-role header: "Writing an artifact body here means you are ROLE 2 --
> GENERATOR, which you are not yet." V-02 names the wrong entity (passes C-22); V-04 also
> re-anchors positive identity at activation (passes C-23). Effect: the model cannot enter a
> role without first receiving an explicit identity statement scoped to that specific role.
> C-23 is additive to C-22 -- passing C-22 is necessary but not sufficient for C-23.

---

## Composite Scoring

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 15 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite score >= 80.

| Band | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30% | C-06, C-07, C-08 |
| Aspirational | 10% | C-09 -- C-23 (denominator = 15) |

---

## Design Notes

The essential band focuses on structural completeness (C-01), classification accuracy (C-02),
automatic flag propagation (C-03, C-05), and the handoff contract (C-05) -- without these the
output cannot be used as a reliable coverage baseline. The REAL-REQUIRED mechanic (C-03, C-08)
is essential rather than recommended because an unflagged EVIDENCE-HEAVY or compliance-tagged
namespace would give a false sense of mock coverage sufficiency.

C-08 (compliance pre-flagging) is recommended rather than essential because it only activates
for compliance-tagged topics; the criterion cannot be graded on a topic with no such tags and
should not penalize the base case.

C-09 and C-10 are aspirational because they require either a specific flag invocation or richer
per-namespace knowledge of the skill catalog -- both raise quality once the foundation is stable.

C-11 -- C-17 (added v2 -- v4) codify structural ordering, isolation, and co-location patterns
discovered in progressive rounds.

C-18 (added v6) shifts the contamination-prevention mechanism from behavioral (stop-gates) to
ontological (role identity). C-22 (added v9) further refines this: the identity mechanism must
be expressed as self-contradiction, not prohibition. C-23 (added v10) raises the bar further:
the positive identity affirmation must fire at each role activation boundary, not only in the
preamble. C-18, C-22, and C-23 test the same dimension at ascending specificity -- a skill can
pass C-18 while failing C-22, and pass C-22 while failing C-23.

C-19 -- C-20 (added v7) anchor the artifact body to both depth (inline placeholder constraint)
and semantics (inertia-grounded specificity). C-21 (added v9) extends C-20 upward: inertia
must be namespace-pre-seeded in the classification table, not just posed free-form in ROLE 2.
The effect is that topic specificity becomes additive rather than originating -- namespace
epistemic cost is locked in at classification time.

The C-18/C-22/C-23 staircase:
- C-18: named role at each boundary + any identity-violation mechanism in the skill (minimum form)
- C-22: identity-violation mechanism must be ontological self-contradiction, not behavioral prohibition
- C-23: positive identity affirmation must appear at each per-role activation point, not only preamble
