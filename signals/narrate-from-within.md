# /narrate-from-within — Write From Inside a Subject's Own Logic

Write about any subject from inside its own worldview — not as an outside observer analyzing it, but as someone standing within the system's own vocabulary, values, and self-understanding.

Applicable to: cultures, companies, communities, movements, scientific paradigms, technologies, user personas.

## Usage

```
/narrate-from-within <subject>
```

## Protocol

### Phase 1 — Immersion

Before writing a single sentence, establish the subject's internal frame:

1. **Vocabulary**: What does the subject call itself? What are its own names for its practices, roles, and values?
2. **Values**: What does the subject consider important? What does it reward, celebrate, protect?
3. **Self-understanding**: How does the subject explain its own existence and purpose?
4. **Sense of time**: Does the subject see itself as ancient, emergent, cyclical, progressing?
5. **What matters**: What does the subject itself consider its defining contribution or identity?

Let these answers set the frame. The subject's own sense of what matters leads the narrative.

### Phase 2 — Drafting

Write the narrative following these rules:

- Use the subject's own names and categories before any external labels
- Describe practices and beliefs BEFORE naming them with academic or analytical terms
- Never evaluate the subject against external standards
- Never express surprise at sophistication ("Remarkably...", "Surprisingly...")
- Never position the subject relative to an unstated default ("Unlike Western...", "Before modern...")
- Let the subject's internal logic provide the structure — not a template imposed from outside

### Phase 3 — The Insider Test

Apply this test: could a thoughtful member of this community read what you wrote and feel it was told with dignity, from inside?

If any passage fails, rewrite it from the subject's own perspective.

### Forbidden Patterns

These phrases signal an outsider's gaze. Never use them:

- "Interestingly..."
- "Remarkably..."
- "Surprisingly..."
- "What's notable is..."
- "Unlike [other subject]..."
- "Despite [assumed limitation]..."
- "Even [subject] managed to..."
- "Long before [external reference point]..."

## Input

- **subject**: The company, culture, movement, technology, paradigm, or community to narrate

## Output

Narrative artifact written entirely from inside the subject's worldview.

Write artifact to: signals/narrate/{topic}-from-within-{date}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: narrate-from-within, topic: {topic}, date: {date}, insider_test: pass|fail
