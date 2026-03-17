Now I have the complete picture. Let me produce the full scorecard.

---

## mock-ns Round 20 Scorecard (rubric v19)

**Baseline**: R19 V-05 -- 162/162 under v19. All R20 variations start from this confirmed golden.

**Axis map**:
- Axis A (V-01): Priority row -- modal impossibility form ("No instruction in this step can precede this rule.")
- Axis B (V-02): Anti-bypass echo header -- bracket token "[P-0:ABD]:" as row header label; "Per [P-0:ABD]:" attribution removed from content cell
- Axis C (V-03): All-governed dual closure -- add "including paths that do not pass through prior steps in normal order"
- V-04 = Axis A + B; V-05 = Axis A + B + C

---

### Criterion-by-criterion evaluation

All five variations carry the R19 V-05 skeleton unchanged through S-0, S-1, S-2, S-3, and S-5. Changes are confined to the S-4 FLAG prohibition chain (Priority row text, Anti-bypass echo header/content, All-governed scope clause). No existing criterion (C-01 through C-49) reaches into that zone. The evaluation below records this uniformly.

#### Essential criteria (C-01 through C-05)

| Criterion | All 5 variations | Evidence |
|-----------|-----------------|----------|
| C-01 | PASS | 6-field header block present in all: skill, topic, tier, category, flag, date |
| C-02 | PASS | CATEGORY assignment table present and correct in S-2 for all |
| C-03 | PASS | 5-row FLAG table in S-3 with correct case rules; verbatim copy instruction in S-4 |
| C-04 | PASS | Fidelity warning block after header with all three CATEGORY-branch texts |
| C-05 | PASS | Mock body instruction requires golden structural pattern of {skill-id} -- skill-specific, not generic |

**All essential: PASS -- 50/50 in all five variations**

#### Recommended criteria (C-06 through C-08)

| Criterion | All 5 variations | Evidence |
|-----------|-----------------|----------|
| C-06 | PASS | S-0 TOPICS.md emit template present; S-1 generating-mock emit present; S-0 before S-1 in step sequence |
| C-07 | PASS | S-5.4 writes `Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md` (namespace, not skill-id) |
| C-08 | PASS | S-5.4 final write-line: `Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md` |

**All recommended: PASS -- 30/30 in all five variations**

#### Aspirational criteria (C-09 through C-49)

Grouped by zone. All five variations share identical S-0, S-1, S-2, S-3, S-5 text; only S-4 FLAG prohibition chain differs, and no existing criterion tests that zone.

**C-09 through C-11 (correctness -- FLAG and topic namespace)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-09 | PASS | S-1 exclusion table: `topic` -> `topic-plan`, NEVER `topic-status` |
| C-10 | PASS | S-3 compliance path explicitly includes COMPLIANCE-OVERRIDE; criterion passes by default absent input compliance tags |
| C-11 | PASS | 5-row FLAG table covers all cases; critical skills named as `trace-*`, `scout-feasibility`, `listen-*` |

**C-12 through C-14 (structure and behavior -- step separation)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-12 | PASS | S-0 step completes (emits status line) before S-1 begins; discrete step labels throughout |
| C-13 | PASS | S-2 category table is exhaustive; unrecognized skill-ids produce no match in any category row -- halt behavior implied |
| C-14 | PASS | Assembly expressed as discrete named steps: S-4 HEADER, FIDELITY WARNING, MOCK BODY sub-sections; S-5.0 through S-5.4 sub-steps |

**C-15 through C-16 (CONSTRAINT and FLAG table)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-15 | PASS | CONSTRAINT names: S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), S-3.3 (flag computation) -- 5 operation types |
| C-16 | PASS | FLAG table condition cell contains `trace-*`, `scout-feasibility`, `listen-*` wildcard patterns directly |

**C-17 through C-20 (S-0 gate and tier-carry)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-17 | PASS | "Before any other step begins, this step emits the TOPICS.md status line." -- advancement gate sentence names requirement |
| C-18 | PASS | Tier field downstream-action column: "Consumed at S-3.3 (flag computation)"; tier-source: "Consumed at S-3.1" -- handoff naming consumers |
| C-19 | PASS | Preamble gate: "Before any other step begins, this step emits..."; terminal gate: "Only this step emits the TOPICS.md status line." -- both present |
| C-20 | PASS | Table column entries name S-3.1/S-3.2/S-3.3 consumers; "Only this step emits..." as standalone terminal sentence |

**C-21 through C-24 (CONSTRAINT depth)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-21 | PASS | 5 operation types named: skill selection, category lookup, carry, compliance detection, flag computation (>= 4) |
| C-22 | PASS | FLAG table has separate rows for HS non-critical, HS critical tier=1, HS critical tier=2+, EVIDENCE-HEAVY, MIXED -- 5 rows |
| C-23 | PASS | CONSTRAINT block precedes the preamble gate; then "Before any other step begins..." is first content after CONSTRAINT -- gate is opening sentence of S-0 body |
| C-24 | PASS | 5 operation types including carry (S-3.1) and compliance detection (S-3.2) -- artifact-write operations at S-5.4 are beyond CONSTRAINT scope but 5 types present |

**C-25 through C-28 (S-0 declarative identity and emission grammar)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-25 | PASS | "Before any other step begins, this step emits the TOPICS.md status line." -- declarative form with step as subject preceding imperative bullets |
| C-26 | PASS | Identity sentence names output: "...emits the TOPICS.md status line" -- artifact explicitly named |
| C-27 | PASS | S-0 resolves tier; CONSTRAINT blocks S-1 until emit complete; tier is available input |
| C-28 | PASS | "Only this step emits the TOPICS.md status line." -- step as nominative subject, emission as main predicate, within S-0 |

**C-29 through C-37 (declarative failure mode prohibitions)**

All prohibited forms (possessive-nominal subject, artifact-as-subject in active voice, artifact-as-subject in passive voice, gerundive-as-subject, relative-clause-agent displacement, ordering predicate as main verb, possessive-NP action-abstraction) are absent. The emission sentence "Only this step emits the TOPICS.md status line." uses canonical form: focus-particle scoped step as nominative subject + emission main predicate.

| C | All 5 | Evidence |
|---|-------|----------|
| C-29 | PASS | No possessive-nominal subject form present |
| C-30 | PASS | No active-voice artifact-as-subject form present |
| C-31 | PASS | No modal-obligation form (must/shall/should) in S-0 role declaration; "emits" is declarative |
| C-32 | PASS | "Only this step emits the TOPICS.md status line." in closing position; tier-carry terminal sentence present as discrete prose sentence |
| C-33 | PASS | No passive artifact-as-subject form present |
| C-34 | PASS | No gerundive-as-subject form present |
| C-35 | PASS | No artifact-as-main-clause-subject with step-in-relative-clause form present |
| C-36 | PASS | No ordering predicate as main clause verb when step is subject |
| C-37 | PASS | No possessive-NP action-abstraction with gerundive emission |

**C-38 through C-42 (extended declarative failure modes and scope boundaries)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-38 | PASS | No it-cleft with expletive subject present |
| C-39 | PASS | No wh-pseudo-cleft with wh-nominalization subject present |
| C-40 | PASS | No existential-there negation ordering statement present |
| C-41 | PASS | Evaluator boundary criterion -- correct scoping applied (by-PP =/= relative clause); no C-35 over-application risk |
| C-42 | PASS | Emission sentence "Only this step emits..." appears within S-0 -- correct step scope |

**C-43 through C-47 (CONSTRAINT form and lifecycle annotation interaction)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-43 | PASS | Phase-grouped lifecycle appears AFTER "Only this step emits..." -- supplementation form; tier-carry terminal sentence retained as discrete prose |
| C-44 | PASS | Golden CONSTRAINT: S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), S-3.3 (flag computation) -- each step ID has inline parenthetical annotation |
| C-45 | PASS | S-3 sub-steps enumerated separately as S-3.1, S-3.2, S-3.3 -- not collapsed into parent "S-3" |
| C-46 | PASS | Per-ID annotated form -- no trailing-group separation |
| C-47 | PASS | C-44 scope boundary and C-45 cascade: correctly applied (5 types present, no cascade needed) |

**C-48 through C-49 (lifecycle phase structure)**

| C | All 5 | Evidence |
|---|-------|----------|
| C-48 | PASS | LIFECYCLE section organizes into 4 named execution phases (Phase 1 -- Protocol and topic resolution, Phase 2 -- Skill and category resolution, Phase 3 -- Flag computation, Phase 4 -- Artifact generation and finalization) |
| C-49 | PASS | Within each phase, each step entry carries Entry: and Exit: state annotations with named state variables |

---

### Composite scores

| Variation | Fails | v19 Score | v19 Max |
|-----------|-------|-----------|---------|
| V-01 (Priority: modal impossibility) | none | **162/162** | 162 |
| V-02 (Echo header: bracket token as label) | none | **162/162** | 162 |
| V-03 (All-governed: bypass-by-skip closure) | none | **162/162** | 162 |
| V-04 (A+B: modal impossibility + bracket token) | none | **162/162** | 162 |
| V-05 (A+B+C: all three axes composed) | none | **162/162** | 162 |

All five variations: **162/162**. All essential pass. Five-way tie at ceiling.

---

### Excellence signals

R20 introduces four independent prospective patterns not yet captured in v19. All four are present (in various combinations) across the five variations, with V-05 the only variation carrying all four.

**C-48\* -- Modal impossibility Priority form (Axis A)**
Present in: V-01, V-04, V-05

"No instruction in this step can precede this rule." replaces the positional-description form "This rule is first in this step -- it applies before any other instruction." The modal impossibility form forecloses a class of reordering arguments that the positional form leaves open: an executor could argue that a specific instruction is "effectively simultaneous" with the first rule or that there is no defined ordering within a step. The modal form closes this by making it a logical impossibility claim rather than a positional assertion. The word change is minimal (one sentence), but the enforcement semantics shift from descriptive to modal.

**C-49\* -- Bracket token as row header (Axis B)**
Present in: V-02, V-04, V-05

Placing "[P-0:ABD]:" as the row header label (left column) rather than as a prose attribution in the content cell ("Per [P-0:ABD]:") converts the row header itself into a bracket-token site. Under the two-phase lookup protocol, encountering [P-0:ABD] as a token requires Phase 1 locate + Phase 2 confirm before processing. In the baseline, "Per [P-0:ABD]:" in the content references the token after the row is already being processed; the header "Anti-bypass echo" creates no lookup obligation. In V-02, encountering the row header requires Phase 1 lookup on [P-0:ABD] before reading the row content -- the anti-bypass enforcement fires one level earlier.

**C-50\* -- Bypass-by-skip scope closure (Axis C)**
Present in: V-03, V-05

"All instructions in this step, named or unnamed, are subject to this rule, including paths that do not pass through prior steps in normal order" closes an exemption class absent in the baseline. The baseline "named or unnamed" qualifier prevents unlabeled-instruction bypass; it does not address bypass-by-skipping steps entirely. An executor could argue that arriving at S-4 via a non-standard path (resuming from a cache, skipping S-3 due to an error handler) falls outside "all instructions in this step" because the instruction sequence was interrupted. "Including paths that do not pass through prior steps in normal order" explicitly names this bypass class and brings it under the rule.

**C-51\* -- Dual scope qualifier composition at zero row cost (V-05 structural property)**
Present in: V-05

V-05 composes "named or unnamed" (unlabeled-instruction closure) and "including paths that do not pass through prior steps in normal order" (bypass-by-skip closure) into a single All-governed cell without adding a row. Both qualifiers address orthogonal exemption classes (unlabeled vs. out-of-order execution) and coexist grammatically as coordinate appositives within the same clause. The composition tightens both dimensions of the All-governed guarantee at zero syntactic overhead.

**Structural property of V-05**: Three independent axes (A, B, C) compose without interaction or grammatical conflict. No row count increases. The Priority change (A) is independent of the echo header change (B) because they target different rows. The All-governed change (C) is independent of both because it targets a third row. V-04 confirms A+B independence; V-05 confirms all three together.

---

### Ranking

| Rank | Variation | Score | Prospective criteria |
|------|-----------|-------|---------------------|
| 1 (gold) | V-05 (A+B+C) | 162/162 | C-48*, C-49*, C-50*, C-51* |
| 2 | V-04 (A+B) | 162/162 | C-48*, C-49* |
| 2 | V-01 (A) | 162/162 | C-48* |
| 2 | V-02 (B) | 162/162 | C-49* |
| 2 | V-03 (C) | 162/162 | C-50*, C-51* |

**V-05 is the prospective R20 golden.** All five reach ceiling under v19; the discrimination is in prospective criteria count. V-05 is the only variation that activates all four prospective excellence signals and demonstrates the full A+B+C composition property.

---

```json
{"top_score": 162, "all_essential_pass": true, "new_patterns": ["Modal impossibility Priority form: 'No instruction in this step can precede this rule.' -- converts positional description to logical impossibility, foreclosing path-specific reordering arguments", "Bracket token as row header label: placing [P-0:ABD]: in the left column makes the row header itself a lookup site, firing two-phase protocol before row content is processed", "Bypass-by-skip scope closure in All-governed: 'including paths that do not pass through prior steps in normal order' closes the out-of-order-arrival exemption class alongside the unlabeled-instruction closure", "Dual scope qualifier composition at zero row cost: 'named or unnamed...including paths...' composes both orthogonal exemption closures in a single cell without adding a row"]}
```
