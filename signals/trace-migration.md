confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Trace before/after a schema change or version upgrade. For each changed entity: what data exists before, what the migration does to it, what the state is after. Identify: data loss paths, nullable violations, missing default values, performance cliffs from schema changes. Stock roles: Commerce / Finance / Operations migration expert.

Write artifact to: signals/trace/migration/{topic}-migration-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
