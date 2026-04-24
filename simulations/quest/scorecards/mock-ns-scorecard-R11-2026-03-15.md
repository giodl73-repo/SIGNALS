# mock-ns Round 11 — Scoring (Rubric v10)

## Criteria Baseline: C-01 through C-28 (All Five Variations)

All five variations share identical S-1, S-2, S-3 chain, A-1 chain, and A-2–A-5 steps. The only structural differences are in the preamble form and position. C-01 through C-28 are therefore evaluated once and applied to all.

### Essential (C-01–C-05)

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-01 | Header block with all six fields (MOCK ARTIFACT, Skill, Topic, Category, Date, Status, Flag) explicitly present in all variants | PASS |
| C-02 | Category assignment table with HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED lists; correct assignment enforced | PASS |
| C-03 | A-3 step mandates all required section headings, tables, gate/verdict line in correct positions; reader-identifiable structure | PASS |
| C-04 | `Flag:` field present; populated from pre-computed FLAG variable; explicit formula for each category and compliance override | PASS |
| C-05 | `simulations/mock/{topic}-{namespace}-mock-{date}.md` — namespace not skill-id in path | PASS |

**Essential: 5/5 PASS — all five variants.**

---

### Recommended (C-06–C-08)

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-06 | Default table correct; topic → topic-plan; Exclusion constraint column carries topic-status exclusion | PASS |
| C-07 | All three fidelity warning variants (WARNING/CAUTION/NOTE) fully specified including "REAL-REQUIRED at Tier 2+ for critical namespaces" qualifier | PASS |
| C-08 | A-5 emits `Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md` as final artifact line | PASS |

**Recommended: 3/3 PASS — all five variants.**

---

### Aspirational C-09 through C-28 (shared evaluation)

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-09 | Case 1 distinguishes `critical + tier>=2` → `"none (structural coverage reliable; REAL-REQUIRED at Tier 2+)"` | PASS |
| C-10 | `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` — dedicated emit line | PASS |
| C-11 | S-3 is a discrete named compute step; A-1 references FLAG "from S-3 -- copied verbatim" | PASS |
| C-12 | Exclusion constraint column in default table carries "topic-status is EXCLUDED -- meta-structural, never default" | PASS |
| C-13 | A-2 positions warning as first section, before mock content, separated by `---` delimiters | PASS |
| C-14 | S-3: "FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run." A-1: "Copy FLAG from S-3 verbatim. Do not rederive it." — both sites | PASS |
| C-15 | Three-column table with labeled Exclusion constraint column; topic-status row carries hard-constraint language | PASS |
| C-16 | Scope row: "FLAG MUST NOT be recomputed anywhere in this run" — run-scoped, not step-sequential | PASS |
| C-17 | First row of A-1 chain is "First rule — Copy FLAG from S-3 verbatim. Do not rederive it." | PASS |
| C-18 | Path classes row: "Not in any step, conditional branch, fallback path, regeneration sequence, or any other execution context, including paths that do not pass through prior steps in normal order" — enumerated with catch-all and bypass-order clarifier | PASS |
| C-19 | Anti-displacement row: "Before any field is listed, before any category lookup, before any formatting instruction, or any other instruction in this step" — three canonical types plus catch-all, with Declarative closure row | PASS |
| C-20 | Failure conseq [A-1:FC] row: names category mismatch mechanism, invisible to downstream tooling, undetectable without manual inspection | PASS |
| C-21 | Affirmative closure row ("Every execution path that reaches A-1 carries the FLAG value emitted here") + No-exemption row ("No path is exempt") | PASS |
| C-22 | Anti-displacement row includes "or any other instruction in this step" catch-all alongside three named types | PASS |
| C-23 | Failure consequence row in S-3 chain: names the contamination mechanism (path modifies FLAG after compute) and downstream effect (A-1 inherits corrupted value indistinguishable from correct) | PASS |
| C-24 | All-governed row ("Every instruction in this step -- named or unnamed -- is governed by this rule") + No-exemption row ("No instruction in this step is exempt") | PASS |
| C-25 | Guarantee-break row: "This violation breaks the closure guarantee stated in the Affirmative closure row above" — explicit causal bridge to named guarantee | PASS |
| C-26 | Cross-site ref [S-3:CS] row names the shared failure mechanism by referencing "[A-1:FC] -- the Failure consequence row in step A-1" | PASS |
| C-27 | Both Guarantee-break and Cross-site ref occupy dedicated, labeled table rows — independently scannable; not appended as clauses to the Failure consequence row | PASS |
| C-28 | Cross-site ref row names "[A-1:FC] -- the Failure consequence row in step A-1" — specific step + row label navigation pointer, not generic "at the consumption site" | PASS |
| C-29 | A-1 Failure conseq row label: "[A-1:FC]". Cell content: "[Mutual target of S-3:CS -- Cross-site reference row in S-3]" — A-1 names S-3 as source; bidirectional anchor discoverable from either end | PASS |
| C-30 | S-3 chain: `| Cross-site ref [S-3:CS] |` — bracket token in label. A-1 chain: `| Failure conseq [A-1:FC] |` with `[S-3:CS]` in cell content — bracket token pair at both sites | PASS |

**C-09 through C-30: 22/22 PASS — all five variants.**

---

## C-31 Differentiated Evaluation

C-31 pass condition: a dedicated orientation block *positioned before all prohibition rows*, appearing as a structurally distinct unit (labeled section, header block, or protocol note), naming every cross-reference token pair, stating what each resolves to, and establishing the complete bidirectional link before any row is read.

### V-01 — Preamble at Top of S-3

```
Cross-reference protocol: S-3 [S-3:CS] and A-1 [A-1:FC] carry mutual navigation
anchors. [S-3:CS] names [A-1:FC] as its forward target. [A-1:FC] names [S-3:CS]
as its backward source. Both directions are active. An executor entering at either
anchor reaches the other without inference. This protocol is established here --
at the top of this step, before any computation or chain row -- and governs the
remainder of this run.
```

- **Structurally distinct?** Labeled "Cross-reference protocol:" — a named prose block, clearly delimited. PASS.
- **Before all prohibition rows?** Positioned at the very top of S-3, before computation cases AND before the FLAG immutability chain. PASS.
- **Names both token pairs?** `[S-3:CS]` and `[A-1:FC]` named with step and role. PASS.
- **Establishes bidirectionality?** "S-3 names A-1 as forward target; A-1 names S-3 as backward source. Both directions are active." PASS.

**C-31: PASS.** Advancement over R10 V-05: preamble is now pre-computation (executor has protocol context before encountering FLAG cases), but still prose-only and still embedded mid-S-3 relative to the run as a whole.

---

### V-02 — Token Resolution Table (Same Position as R10 V-05)

```
Cross-reference protocol: token resolution table.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  | Token    | Step | Row type                  | Paired token | Direction            |
  |----------|------|---------------------------|--------------|----------------------|
  | [S-3:CS] | S-3  | Cross-site reference row  | [A-1:FC]     | forward --> names A-1|
  | [A-1:FC] | A-1  | Failure consequence row   | [S-3:CS]     | <-- backward, names  |
  |          |      |                           |              | S-3 as source        |

Both anchors are active. An executor entering at either token finds its pair by
reading the Direction cell. No prior traversal required.
```

- **Structurally distinct?** Labeled "Cross-reference protocol: token resolution table." with a formal table structure. PASS.
- **Before all prohibition rows?** Positioned after computation cases but before the FLAG immutability chain — same as R10 V-05 which passed C-31. PASS.
- **Names both token pairs?** Full resolution table: Token / Step / Row type / Paired token / Direction columns. PASS.
- **Establishes bidirectionality?** Direction column has both forward and backward cells; prose confirms both anchors active. PASS.

**C-31: PASS.** Advancement over R10 V-05: table format makes token resolution O(1) lookup vs. sequential prose parsing; abbreviation key names `:CS`/`:FC` as defined terms. Same position weakness as R10 V-05 — executor mid-S-3 before encountering preamble can still process computation cases before registering it.

---

### V-03 — Conversational/Explanatory Register (Same Position)

```
Two rows in this run carry bracket anchors that point to each other. Here is why
they exist and what to do with them:

  [S-3:CS] appears in S-3's Cross-site reference row below. When you encounter it,
  it means: go to the Failure consequence row in step A-1 -- that is where the
  downstream effect of a FLAG violation manifests. You do not need to re-read the
  rest of S-3 to know where to look.

  [A-1:FC] appears in A-1's Failure consequence row. When you encounter it, it
  confirms: this is the row that S-3's Cross-site reference pointed to. If you
  arrive at A-1 in a regenerated context without S-3 in memory, the [A-1:FC]
  marker tells you the link exists and where its source is. You do not need to
  re-read S-3 to confirm the cross-reference is still active.

Enter from either anchor and you reach the other. No prior traversal is needed.
```

- **Structurally distinct?** Unlabeled — opens with "Two rows in this run carry bracket anchors…" No section label, no header, no "Cross-reference protocol:" prefix. Falls short of "labeled section, header block, or protocol note" standard. PARTIAL.
- **Before all prohibition rows?** Yes — same position as V-02/R10 V-05, before FLAG immutability chain. PASS.
- **Names both token pairs?** `[S-3:CS]` and `[A-1:FC]` named with step context and row role. PASS.
- **Establishes bidirectionality?** "Enter from either anchor and you reach the other" — purpose-first framing establishes both directions. PASS.

**C-31: PARTIAL (0.5).** Functional requirements are met (correct position, both tokens named, bidirectionality established) but the structural distinctness criterion fails on label — the block cannot be identified as a "protocol" block without reading its content, unlike every other variation which names itself at the opening. Purpose-first framing is a strength for comprehension, but the missing formal label reduces machine-readability and skimmability of the block itself.

---

### V-04 — P-0 as Numbered Step + Abbreviation Glossary (List Form)

```
STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens in this run encode step and row type.

  Abbreviation key:
    :CS = Cross-site reference row
    :FC = Failure consequence row

  Active token pairs:
    [S-3:CS] -- Step S-3, Cross-site reference row  -->  references [A-1:FC]
    [A-1:FC] -- Step A-1, Failure consequence row   <--  references [S-3:CS]

Protocol guarantee: [S-3:CS] names [A-1:FC] as its forward target. [A-1:FC] names
[S-3:CS] as its backward source. Both directions are active. An executor entering
at either anchor reaches the other without inference or prior traversal.

Do not re-establish this protocol in later steps. Every bracket token in this run
is interpreted per this table.
```

- **Structurally distinct?** Formal numbered step header "STEP P-0 -- CROSS-REFERENCE PROTOCOL" — maximum structural distinctness. PASS.
- **Before all prohibition rows?** P-0 precedes S-1, S-2, S-3, A-1 — before every step including the chain rows. PASS.
- **Names both token pairs?** Active token pairs list names step, row type, and direction for both tokens. PASS.
- **Establishes bidirectionality?** "Protocol guarantee" block names both directions explicitly; "Do not re-establish this protocol in later steps" makes P-0 the sole authority. PASS.

**C-31: PASS.** Strongest positional form — executor has protocol context before any execution begins; no mid-run encounter risk. List format for abbreviation key and token pairs requires mental assembly (read `:CS = Cross-site reference row` in key, then find `[S-3:CS]` in pairs list, then locate the step) compared to a resolution table.

---

### V-05 — P-0 + Two-Part Structure + Explanatory Framing

```
STEP P-0 -- CROSS-REFERENCE PROTOCOL

Token notation: bracket tokens encode step and row type. Row-type abbreviations are
defined here as named vocabulary for this run.

  Abbreviation glossary:

    | Abbreviation | Row type                  | Where it appears            |
    |--------------|---------------------------|-----------------------------|
    | :CS          | Cross-site reference row  | S-3 immutability chain      |
    | :FC          | Failure consequence row   | A-1 prohibition chain       |

  Token resolution table:

    | Token    | Resolves to                                    | Paired with | Direction                          |
    |----------|------------------------------------------------|-------------|------------------------------------|
    | [S-3:CS] | S-3 Compute Flag, Cross-site reference row     | [A-1:FC]    | forward --> names A-1 as target    |
    | [A-1:FC] | A-1 Assemble Header, Failure consequence row  | [S-3:CS]    | <-- backward, names S-3 as source  |

  [S-3:CS] exists so that an executor processing S-3's chain knows where to find the
  downstream failure consequence -- the Failure consequence row in step A-1.

  [A-1:FC] exists so that an executor arriving at A-1 in a regenerated context --
  without S-3 in active memory -- knows that a cross-site reference at [S-3:CS] names
  this row as its target. The link is discoverable from A-1 alone.

Both directions are active. Do not re-establish this protocol in later steps.
```

- **Structurally distinct?** "STEP P-0 -- CROSS-REFERENCE PROTOCOL" — maximum structural distinctness, plus preamble header declares "Row-type abbreviations are defined here as named vocabulary for this run." PASS.
- **Before all prohibition rows?** P-0 before S-1 — precedes all execution. PASS.
- **Names both token pairs?** Resolution table: Token / Resolves to / Paired with / Direction — each token maps to its complete description in a single scannable row. PASS.
- **Establishes bidirectionality?** Direction column, plus two explanatory sentences naming the specific failure scenario each anchor guards against (S-3 chain context loss; A-1 regenerated context entry). PASS.

**C-31: PASS.** Strongest form — two-table structure separates abbreviation vocabulary definition (what `:FC` means) from token-to-step mapping (where `[A-1:FC]` lives in the run and what it resolves to). Explanatory framing per direction makes the preamble self-sufficient: an executor reading only P-0 understands what the tokens mean, where they appear, and why the link exists in each direction.

---

## C-31 Summary

| Variant | C-31 | Form |
|---------|------|------|
| V-01 | PASS | Prose, labeled "Cross-reference protocol:", top of S-3 (pre-computation) |
| V-02 | PASS | Structured table, labeled "Cross-reference protocol: token resolution table.", post-computation pre-chain |
| V-03 | PARTIAL | Conversational prose, unlabeled, post-computation pre-chain |
| V-04 | PASS | Formal numbered P-0 step, list format, before all steps |
| V-05 | PASS | Formal numbered P-0 step, two-part table + explanatory framing, before all steps |

---

## Composite Scores

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational_pass/23 × 10)`  
All five variants: essential 5/5, recommended 3/3. Aspirational varies only at C-31.

| Variant | Aspirational (C-31) | Aspirational points | Composite |
|---------|--------------------|--------------------|-----------|
| V-01 | 23/23 (PASS) | 10.00 | **100.0** |
| V-02 | 23/23 (PASS) | 10.00 | **100.0** |
| V-03 | 22.5/23 (PARTIAL) | 9.78 | **99.8** |
| V-04 | 23/23 (PASS) | 10.00 | **100.0** |
| V-05 | 23/23 (PASS) | 10.00 | **100.0** |

---

## Ranking

| Rank | Variant | Score | C-31 form | Positional advantage |
|------|---------|-------|-----------|---------------------|
| 1 (tied) | V-04 | 100.0 | P-0 step, list format | Before all execution — no mid-run encounter risk |
| 1 (tied) | V-05 | 100.0 | P-0 step, two-part table + framing | Before all execution; self-sufficient; seeds C-32 |
| 1 (tied) | V-01 | 100.0 | Prose, labeled, top of S-3 | Before computation cases AND chain — positional upgrade over R10 V-05 |
| 1 (tied) | V-02 | 100.0 | Table, labeled, post-computation | Same position as R10 V-05; tabular format upgrade |
| 5 | V-03 | 99.8 | Prose, unlabeled, post-computation | Structurally weakest — functional content without formal label |

---

## Excellence Signals

**V-05 is the R11 differentiator** despite tying on composite score. Three structural properties separate it from V-04 (the closest rival):

**Signal 1 — Two-part P-0 structure (abbreviation glossary + resolution table)**  
V-04 integrates abbreviation definitions and token mappings into a single list. An executor who wants to decode `:FC` reads the abbreviation key; an executor who wants to know what `[A-1:FC]` fully resolves to must mentally join the abbreviation key with the token pair entry. V-05 separates concerns: the glossary table defines what each suffix means (independent lookup), and the resolution table maps each complete token to its step, row type, paired token, and direction (independent lookup). No assembly required for either query.

**Signal 2 — "Where it appears" column in abbreviation glossary**  
V-04 defines `:CS = Cross-site reference row` and `:FC = Failure consequence row` — vocabulary definitions without scope. V-05 adds a "Where it appears" column: `:CS → S-3 immutability chain`, `:FC → A-1 prohibition chain`. An executor who encounters `[A-1:FC]` in S-3's cross-site reference row can decode not only the abbreviation but the chain it will be found in, before navigating there. This closes the gap where an abbreviation is defined but its location in the run is inferred from context.

**Signal 3 — Purpose-per-direction explanatory statements**  
V-04's P-0 establishes the protocol mechanically: both tokens defined, both directions stated. V-05 adds two explanatory sentences naming the specific failure scenario each direction guards against:
- `[S-3:CS]` exists for forward navigation: an executor processing S-3's chain knows where the downstream failure consequence lives.
- `[A-1:FC]` exists for context-loss recovery: an executor arriving at A-1 in a regenerated context (without S-3 in active memory) can confirm the cross-reference is still active from A-1 alone.

These purpose statements make P-0 self-sufficient as a chain orientation reference. An executor who reads only P-0 understands what the tokens mean, where they appear in the run, and WHY the bidirectional link exists — without consulting any chain row.

**V-03 anti-signal — structural label is load-bearing**  
V-03 demonstrates that purpose-first framing is not sufficient alone to satisfy C-31. The conversational register produces clearer human comprehension of WHY each anchor exists (a strength), but the missing formal label means the block cannot be identified as a protocol block by scanning — a reader must read the content to recognize it as an orientation section. The label is not cosmetic; it is a structural distinctness signal that enables O(1) block identification. V-03's framing strength should be harvested by combining it with a label (as V-05 does with its explanatory sentences under a formally labeled P-0).

**C-32 candidate signal (seeded by V-05)**  
Whether the abbreviation glossary's "Where it appears" column — making each suffix's scope explicit at the point of vocabulary definition — produces measurably fewer token misidentification errors in chain rows compared to V-04's location-agnostic list form. The hypothesis: an executor who knows `:FC → A-1 prohibition chain` at P-0 will not need to infer this when encountering `[A-1:FC]` in S-3's Cross-site reference row, where the token appears in a different chain than where it resolves to.

---

## JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Two-part P-0 structure separates abbreviation vocabulary definition from token-to-step mapping -- an executor decoding an abbreviation reads the glossary; one needing full chain navigation reads the resolution table; no mental assembly across list items required", "Abbreviation glossary table with Where-it-appears column makes scope of each suffix explicit at the definition point -- executor sees that :FC appears in A-1 prohibition chain before encountering it there, closing the gap where an abbreviation is defined but its chain location is inferred from context", "Purpose-per-direction explanatory statements at P-0 name the specific failure scenario each anchor guards against (A-1 context-loss recovery; S-3 forward navigation) -- preamble becomes self-sufficient without consulting chain rows; combines with formal P-0 label to satisfy both structural-distinctness and comprehension criteria simultaneously"]}
```
