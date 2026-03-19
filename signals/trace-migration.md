Trace before/after a schema change or version upgrade. For each changed entity: what data exists before, what the migration does to it, what the state is after. Identify: data loss paths, nullable violations, missing default values, performance cliffs from schema changes. Stock roles: Commerce / Finance / Operations migration expert.

Write artifact to: signals/trace/migration/{topic}-migration-{date}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-[this-skill]-{date}.md). No namespace subdirectory.
