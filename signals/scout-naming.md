Generate and evaluate candidate names using multi-persona scoring. Supports --validate <name> to pin an existing name at row 1 and produce a validation summary alongside alternatives. Generate 10-15 candidates. Score across PM (memorability), Design (visual weight), UX (speakability), GTM (searchability), Strategy (positioning fit). Collision check against package registries and domains. Stock roles: PM, Design, UX, GTM, Strategy.

Write artifact to: signals/scout/naming/{topic}-naming-{date}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-[this-skill]-{date}.md). No namespace subdirectory.
