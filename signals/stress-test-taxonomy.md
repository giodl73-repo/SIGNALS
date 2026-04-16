# /stress-test-taxonomy — Test Any Classification System Against Expected Coverage

Generate 100+ items that a user might look for, check whether each has an obvious home in the taxonomy, and identify coverage gaps, ambiguities, and category imbalances.

## Usage

```
/stress-test-taxonomy <taxonomy>
```

## Protocol

### Phase 1 — Load Taxonomy

Read the taxonomy: all categories with their descriptions, hierarchy, and any placement rules. Count categories and levels.

### Phase 2 — Generate Test Items

Generate 100+ test items across four classes:

| Class | Description | Target count |
|-------|------------|-------------|
| **Obvious** | Items that clearly belong in one category | 40+ |
| **Edge** | Items that sit near category boundaries | 25+ |
| **Popular** | Items a general user would look for first | 20+ |
| **Expert** | Items a domain expert would expect to find | 15+ |

Spread items across all categories. Do not cluster in familiar territory.

### Phase 3 — Placement Test

For each test item, attempt placement:

```markdown
| # | Item | Class | Category | Confidence | Notes |
|---|------|-------|----------|------------|-------|
| 1 | {item} | obvious | {category} | high | — |
| 2 | {item} | edge | {cat A} or {cat B} | low | ambiguous — could go in either |
| 3 | {item} | popular | — | none | homeless — no good category |
```

Confidence levels:
- **high**: One obvious category, no hesitation
- **medium**: One best category, but placement required thought
- **low**: Two or more plausible categories
- **none**: No good category exists (homeless item)

### Phase 4 — Diagnosis

From the placement results, identify:

#### Homeless Items
Items with no good category. Group by theme — if 3+ homeless items cluster around a missing concept, that's a gap in the taxonomy.

#### Ambiguous Items
Items that could go in 2+ categories. Group by the categories involved — if the same pair of categories keeps competing, their boundary is poorly defined.

#### Thin Categories
Categories that received fewer than 3 test items. Either the category is too narrow or the test items missed it — investigate which.

#### Fat Categories
Categories that received 15+ test items. Candidates for splitting.

### Phase 5 — Recommendations

For each finding, recommend a fix:

| Finding | Type | Recommendation |
|---------|------|---------------|
| {N} homeless items cluster around {theme} | Gap | Add category: "{name}" covering {scope} |
| {Cat A} and {Cat B} compete for {N} items | Ambiguity | Sharpen boundary: {Cat A} owns {criterion}, {Cat B} owns {criterion} |
| {Category} received only {N} items | Thin | Merge into {parent or sibling category} |
| {Category} received {N} items | Fat | Split into {sub-category A} and {sub-category B} |

## Input

- **taxonomy**: List of categories with descriptions (file path, inline, or reference to an existing taxonomy artifact)

## Output

Coverage report with placement results, diagnosis (homeless, ambiguous, thin, fat), and fix recommendations.

Write artifact to: signals/validate/{topic}-taxonomy-stress-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: stress-test-taxonomy, topic: {topic}, date: {date}, items_tested: {n}, homeless: {n}, ambiguous: {n}, thin_categories: {n}, fat_categories: {n}
