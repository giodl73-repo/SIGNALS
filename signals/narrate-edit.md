# /narrate-edit — Structured Editorial Pass With Productive Tension

Run three dependency-ordered editorial passes on any prose artifact. Each pass pairs two editors with different loyalties, producing concrete editorial actions — not scores. Architecture first (is the structure right?), cut second (what can come out?), voice last (does it sound like one author?).

The dependency order is the point: no sense cutting sentences in a paragraph that should be moved; no sense polishing voice in a passage that should be removed.

## Usage

```
/narrate-edit <artifact> [--pass architecture|cut|voice|all]
```

Default: all three passes in order.

## The 6 Editors

Each pass pairs two editors who create productive tension. The named editors are real literary editors whose aesthetics are documented and distinct.

| ID | Editor | Pass | Tradeoff | What They Do |
|----|--------|------|----------|-------------|
| E-1 | **Robert Gottlieb** | Cut | Necessity vs affection | Cuts what serves the author but not the work |
| E-2 | **Gordon Lish** | Cut | Compression vs completeness | Removes explanation, leaves the moment |
| E-3 | **Nan Talese** | Voice | Authenticity vs accessibility | Protects the author's voice while ensuring the reader can follow |
| E-4 | **Maxwell Perkins** | Voice | Ambition vs discipline | Manages scope — each section gets its own diagnosis |
| E-5 | **Sonny Mehta** | Architecture | Sequence vs momentum | Rearranges structure so the reader never stops |
| E-6 | **Michael Korda** | Architecture | Depth vs reach | Ensures the specialist and the generalist both finish |

## Protocol

### Pass 1 — Architecture (E-5 Mehta leads, E-6 Korda supports)

**Question: Is the structure right?**

1. Read the full artifact
2. Map the artifact's beats (3-7 major beats with approximate word counts)
3. **Mehta asks:**
   - Are the beats in the right order? Would shuffling improve the reader's experience?
   - Where does the artifact peak? Too early, too late, or right?
   - Does each beat end with a question the next beat answers?
   - Is there a second-act sag — a stretch where the reader's motivation to continue drops?
4. **Korda asks:**
   - Can a non-specialist follow this artifact from start to finish?
   - Where does the reader fall off? (Mark the exact paragraph)
   - Is there a passage someone would send to a colleague? (The "gift passage")
   - Does technical language serve the argument or the author's credibility?
5. **Output:**
   - Structural verdict: reorder / restructure / leave as-is
   - Beat map (table of beats with word counts and pacing assessment)
   - Accessibility flags (0-3 specific passages where the general reader is lost)
   - The "gift passage" — the single best passage in the artifact
   - Korda's one-line assessment in Korda's voice

### Pass 2 — Cut (E-1 Gottlieb leads, E-2 Lish supports)

**Question: What can come out?**

1. Re-read the artifact after any Pass 1 restructuring
2. **Gottlieb asks (paragraph-level):**
   - Does this paragraph exist because the work needs it, or because the author needed to write it?
   - How many times does the artifact make the same point in different words?
   - Mark every paragraph that could be cut without the reader noticing
3. **Lish asks (sentence-level):**
   - Does this paragraph explain what the reader already understood?
   - Is the author standing between the evidence and the reader?
   - Is there a zero-commentary version of this passage?
   - Does the ending tell the reader what the artifact meant? (If so, cut it — the second-to-last paragraph is usually the real ending)
4. **Output:**
   - Cut list: specific passages to remove, with rationale per passage
   - Compression candidates: passages that can be tightened (e.g. 80 words to 30 words), with before/after word counts
   - Word count: current vs projected after cuts
   - **The Lish test:** one passage rewritten with all explanation removed (before/after)
   - Gottlieb's one-line assessment in Gottlieb's voice

### Pass 3 — Voice (E-3 Talese leads, E-4 Perkins supports)

**Question: Does it sound like one author, and can the reader follow?**

1. Re-read the artifact after Pass 1 + Pass 2
2. **Talese asks:**
   - Does every paragraph sound like the same author?
   - Where does the register shift without warning? (Mark each shift)
   - Is the technical depth calibrated to the reader the artifact claims to serve?
   - Does the author's presence disappear in technical sections?
3. **Perkins asks:**
   - Which sections are already right? (Leave them alone)
   - Which have strong openings and weak endings?
   - Which are circling an insight they haven't articulated? (Find the insight, state it, cut the circling)
   - Is the framework earning its keep or being carried as luggage?
4. **Output:**
   - Voice verdict: uniform / shifting / fractured
   - Register shifts marked with recommendations (intentional: keep; accidental: fix)
   - Weak endings identified with proposed replacements
   - The "circling" passages — where the author is reaching for something and hasn't found the sentence yet. Propose the sentence.
   - Talese's one-line assessment in Talese's voice

---

## Output Format

```markdown
# Editorial Pass: {artifact name}

## Pass 1: Architecture (Mehta + Korda)
**Structural verdict:** {reorder / restructure / leave as-is}
**Beat map:** {table of beats with word counts}
**Accessibility flags:** {0-3 specific passages}
**Gift passage:** "{the best passage in the artifact}"
**Korda:** "{one-line assessment in Korda's voice}"

## Pass 2: Cut (Gottlieb + Lish)
**Cut list:** {specific passages with rationale}
**Compression candidates:** {passages with before/after word counts}
**Word count:** {current} -> {projected}
**The Lish test:** {one passage, before and after}
**Gottlieb:** "{one-line assessment in Gottlieb's voice}"

## Pass 3: Voice (Talese + Perkins)
**Voice verdict:** {uniform / shifting / fractured}
**Register shifts:** {marked passages}
**Weak endings:** {identified with proposed replacements}
**The circling passage:** {where the author is reaching -- proposed sentence}
**Talese:** "{one-line assessment in Talese's voice}"

## Summary
**Total proposed cuts:** {N paragraphs, ~X words}
**Structural changes:** {Y}
**Voice fixes:** {Z}
**Priority fix:** {the single highest-impact change}
```

---

## Tension Rotation

The three passes run in order because each depends on the prior:
1. **Architecture first** — no point cutting sentences in a paragraph that should be moved
2. **Cut second** — no point polishing voice in a passage that should be removed
3. **Voice last** — polish what remains

Within each pass, the two editors create productive tension:
- Gottlieb (necessity) vs Lish (compression) — different thresholds for what to cut
- Talese (authenticity) vs Perkins (discipline) — different loyalties (author vs reader)
- Mehta (sequence) vs Korda (reach) — different audiences (committed reader vs browser)

Where the editors disagree, note both opinions — the author decides.

---

## Key Rules

- **No invented editors.** The 6 editors are real literary editors. Each voice must be consistent with that editor's actual aesthetic and critical priorities. If you do not know an editor's voice, research it before writing in it.
- **Dependency order is mandatory.** Do not run Pass 2 before Pass 1 output is finalized. Do not run Pass 3 before Pass 2 output is finalized.
- **Actions, not scores.** Unlike /narrate-editorial (which finds issues) and /narrate-rubric (which scores dimensions), this skill produces concrete editorial actions: what to move, what to cut, what to rewrite.
- **The Lish test is always included.** Pick the passage that most needs compression. Show the before (with all the author's explanation) and the after (with the explanation stripped). Let the contrast speak.
- **Word counts are exact.** Report actual word counts for the artifact, for proposed cuts, and for compression candidates. Vague claims ("could be shorter") are not actionable.

## Input

- **artifact**: Path to the prose artifact to edit
- **pass**: (optional) Which pass to run: architecture, cut, voice, or all (default: all)

## Output

Three-pass editorial report with concrete actions: structural changes, cut list with rationale, voice fixes with replacements.

Write artifact to: signals/narrate/{topic}-edit-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: narrate-edit, topic: {topic}, date: {date}, passes_run: [architecture, cut, voice], total_cuts: {n}, structural_verdict: {verdict}, voice_verdict: {verdict}, word_count_before: {n}, word_count_after: {n}
