# /skeleton-then-anchor — Build Wide, Validate Deep, Then Scale

A phasing strategy for any large content or architecture project. Build the full skeleton at low depth, validate one branch at full depth, then scale the learnings to every branch.

## Usage

```
/skeleton-then-anchor <domain> --principle <organizational-principle>
```

## Protocol

### Phase 1 — Define the Tree

Work with the user to establish:

1. **Domain**: What is the full scope? (e.g., "every human culture", "every microservice in the platform", "every chapter in the book")
2. **Organizational principle**: How is the tree structured? (e.g., by region, by function, by chronology)
3. **Depth levels**: How many levels does the tree have? Name each level. (e.g., L1: Region, L2: People, L3: Era, L4: Section)
4. **Leaf format**: What does a complete leaf look like? (e.g., a 3000-word narrative, an API spec, a compliance checklist)

### Phase 2 — Build the Skeleton (Wide, Shallow)

Enumerate the full tree at all levels. Do not go deep — go wide. Get the structure right.

For each node, capture:
- **Name**: What is this node called?
- **Scope**: What does it contain?
- **Count**: How many children does it have? (estimate if unknown)
- **Notes**: Any known challenges, gaps, or special considerations

Output the skeleton as an indented tree with node counts:

```
L1: {Category A} (N children)
  L2: {Subcategory A1} (N children)
  L2: {Subcategory A2} (N children)
L1: {Category B} (N children)
  ...
```

### Phase 3 — Review the Skeleton

Check the skeleton for:
- **Gaps**: Are any expected items missing?
- **Balance**: Are some branches much larger than others? Should fat branches be split?
- **Overlap**: Do any branches cover the same territory?
- **Bias**: Does the structure privilege certain perspectives over others?

If using /stress-test-taxonomy, run it against the skeleton now.

### Phase 4 — Select the Anchor

Pick one branch to take to full depth. The best anchor is the branch that:

1. **Has rich sources**: Enough material to build a complete leaf
2. **Is distinctive**: Not the easiest or most familiar — one that stress-tests the format
3. **Exercises the most dimensions**: Hits edge cases in the leaf format, the voice, the quality bar

Recommend an anchor with rationale. Get user agreement before proceeding.

### Phase 5 — Run the Anchor

Take the anchor branch to full depth:

1. Build the complete leaf (or leaves) for this branch
2. Run the full quality pipeline (scoring, editorial review, whatever the project uses)
3. Fix issues and iterate until the anchor meets the quality bar
4. Log what worked, what broke, what the skeleton didn't anticipate

Anchor deliverables:
- The completed leaf artifact
- A lessons-learned log: what to carry forward, what to change in the skeleton or format

### Phase 6 — Scale

Apply anchor learnings to the rest of the tree:

1. Revise the skeleton based on anchor findings (new levels, renamed categories, adjusted format)
2. Generate a **scaling checklist**: for each remaining branch, what must be true before it's marked complete?
3. Prioritize remaining branches (richest sources first, or highest user demand first — discuss with user)
4. Build remaining branches to full depth, using the anchor as the quality reference

## Input

- **domain**: The full scope of the project
- **principle**: The organizational principle for the tree (e.g., by region, by function, by time)

## Output

Phasing plan with skeleton at all levels and anchor selection rationale.

Write artifact to: signals/specify/{topic}-skeleton-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: skeleton-then-anchor, topic: {topic}, date: {date}, depth_levels: {n}, total_nodes: {n}, anchor: {branch-name}
