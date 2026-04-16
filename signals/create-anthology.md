# /create-anthology — Build a Narrative Anthology From Inside Every Subject

Scaffold and run a full anthology project: a comprehensive collection of narratives about a domain, where each entry is told from inside its own perspective. This is the master process — it orchestrates taxonomy design, infrastructure, quality systems, and phased content production.

Examples of anthologies this can build:
- Every human culture (told from inside each culture's worldview)
- Every major company's founding story (from inside each company's logic)
- Every scientific discipline's origin story (from inside each field's own terms)
- Every great city's story (from inside the city's self-understanding)
- Every social movement (from inside the movement's own vocabulary)

## Usage

```
/create-anthology <domain>
```

## Protocol

This skill runs seven steps. Each step has a gate — do not advance until the gate is met. The user drives pacing; the skill provides structure.

---

### Step 1 — Define Domain and Editorial Philosophy

Establish with the user:

1. **Domain**: What are we telling the story of? (e.g., "every human culture", "every great city")
2. **Inside-voice rule**: What does "from inside" mean for this domain? What perspective does the narrator take?
3. **Forbidden patterns**: What language or framings are banned? (Start with the defaults from /narrate-from-within and adapt for the domain.)
4. **Brand identity**: Does the anthology have a name, a mascot, a visual identity? (Optional but useful for consistency.)
5. **Target format**: What does a complete entry look like? (Word count, sections, depth.)

**Gate**: The user confirms the editorial philosophy before proceeding.

---

### Step 2 — Design the Organizational Taxonomy

Define the tree structure:

1. **Top-level categories**: What are the major groupings? (e.g., regions, eras, disciplines)
2. **Entries**: What are the individual subjects within each category? (e.g., peoples, companies, cities)
3. **Time/phase divisions**: Does each entry have temporal structure? (e.g., eras, chapters, periods)
4. **Depth**: How many levels does the tree have?

Output a full skeleton using the /skeleton-then-anchor format.

**Gate**: The skeleton covers the domain without major gaps.

---

### Step 3 — Stress-Test the Taxonomy

Run /stress-test-taxonomy against the skeleton:

1. Generate 100+ items people would look for in this anthology
2. Check coverage: any homeless items? Any ambiguous placements?
3. Fix gaps: add missing categories, merge thin ones, split fat ones
4. Re-verify after fixes

**Gate**: No more than 5 homeless items. No category with fewer than 2 entries.

---

### Step 4 — Build Infrastructure

Create the anthology's quality and production systems:

#### 4A — Style Guide
- Editorial principles (the inside-voice rule, forbidden patterns, before/after examples)
- Structural template for entries (sections, expected length, required elements)
- Voice reference: 2-3 paragraphs showing the target register

#### 4B — Scoring Rubric
- Dimensions to score each entry on (e.g., insider perspective, narrative flow, specificity, voice consistency)
- Scoring scale with anchored descriptions (what does a 3 vs. 5 look like?)
- Use /evolving-rubric format so the rubric can learn

#### 4C — Publishing Pipeline
- Stages from draft to locked (e.g., draft → scored → reviewed → revised → locked)
- Gate criteria for each stage
- Who (or what role) owns each stage

#### 4D — Review Panel
- 3-5 named reviewer personas, each with a distinct editorial lens
- Example: Insider Advocate (does it pass the insider test?), Voice Keeper (is the register consistent?), Compression Editor (is every sentence earning its place?), Domain Expert (are the facts right?), General Reader (is it engaging to a non-specialist?)

#### 4E — Editorial Lenses
- Configure /editorial-triple-pass for this anthology's specific needs
- Add any domain-specific lenses beyond the default three

**Gate**: Style guide, rubric, pipeline, and review panel all exist and are internally consistent.

---

### Step 5 — Build the Skeleton

Using /skeleton-then-anchor Phase 2:

1. Create all entries at the top 2-3 levels of depth (names, scopes, notes — not full content)
2. Review the skeleton for consistency, gaps, and bias
3. Fix findings and re-verify

**Gate**: Complete skeleton with no structural issues.

---

### Step 6 — Select and Run an Anchor

Using /skeleton-then-anchor Phase 4-5:

1. **Select**: Pick one entry that stress-tests the most dimensions — not the easiest or most familiar, but one that will reveal problems in the format, voice, and pipeline
2. **Draft**: Write the anchor entry using /narrate-from-within
3. **Score**: Run /evolving-rubric against the anchor
4. **Review**: Run /editorial-triple-pass on the anchor
5. **Revise**: Fix all P1 and P2 findings
6. **Lock**: Mark the anchor as complete — it becomes the quality reference for all future entries
7. **Log**: Record innovations, lessons learned, and any infrastructure changes needed

**Gate**: Anchor scores above the quality bar on all rubric dimensions. All P1 findings resolved.

---

### Step 7 — Scale

1. Run 3+ entries from different top-level categories in parallel
2. Cross-compare: do they feel like they belong in the same anthology? Same voice, same depth, same quality?
3. Evolve: update the rubric, style guide, and pipeline based on what the batch reveals
4. Continue: build remaining entries, scoring and reviewing each one
5. After every 10 entries: run a cross-anthology consistency check

**Gate per entry**: Passes rubric, passes editorial review, passes insider test.
**Gate per batch**: Cross-comparison confirms anthology coherence.

---

## Skills Used

This skill orchestrates:
- /narrate-from-within — for drafting entries
- /skeleton-then-anchor — for phasing and structure
- /stress-test-taxonomy — for taxonomy validation
- /evolving-rubric — for scoring with learning
- /editorial-triple-pass — for editorial review

## Input

- **domain**: Description of the anthology's scope and editorial philosophy

## Output

Full anthology project scaffold: editorial philosophy, taxonomy, infrastructure (style guide, rubric, pipeline, review panel), skeleton, anchor plan.

Write artifact to: signals/specify/{topic}-anthology-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: create-anthology, topic: {topic}, date: {date}, total_entries: {n}, categories: {n}, infrastructure: [style-guide, rubric, pipeline, review-panel, editorial-lenses]
