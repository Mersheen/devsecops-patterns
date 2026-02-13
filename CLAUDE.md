# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A pattern language for DevOps following Christopher Alexander's methodology from *A Pattern Language* (1977). Content is prose, not code — 75 planned patterns organised across 10 scales (organisational philosophy down to operational excellence). AI is treated as a cross-cutting force, not a separate section.

## Build Commands

```bash
# Install dependencies
pip install mkdocs-material pyyaml

# Generate docs/ from patterns/ (must run before mkdocs)
python scripts/build.py

# Local preview
mkdocs serve    # http://localhost:8000

# Generate pattern relationship graph
python scripts/generate_graph.py
dot -Tsvg docs/assets/pattern-graph.dot -o docs/assets/pattern-graph.svg

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## Architecture

**Source of truth is `patterns/`** — one markdown file per pattern. The `docs/` directory is generated output; never edit it directly.

Build pipeline: `patterns/*.md` → `scripts/build.py` → `docs/` → `mkdocs build/serve`

### Pattern File Format

Files are named `NNN-kebab-case-name.md` (e.g., `001-generative-culture.md`). Each has YAML frontmatter:

```yaml
---
id: 28                          # unique integer, matches filename prefix
name: "Deployment Pipeline"
confidence: 2                   # 0 = hypothesis, 1 = likely true (*), 2 = invariant (**)
scale: 5                        # 1-10 per patterns/SCALES.md, 0 = cross-cutting
context_patterns: [6, 22, 21]   # IDs of larger patterns (upward links)
completion_patterns: [29, 30]   # IDs of smaller patterns (downward links)
ai_dimension: true              # whether AI meaningfully modifies this pattern's forces
tags: []
references: []
---
```

### Pattern Body Structure (Alexander's format)

1. `# Pattern Name` with confidence stars (e.g., `# Generative Culture **`)
2. Opening context — italic, links to larger patterns
3. Problem statement — **bold**
4. Discussion — evidence, reasoning, trade-offs, AI dimension if applicable
5. `Therefore:` followed by solution — **bold**
6. Closing cross-references — italic, links to smaller patterns
7. `## References` section

Template: `patterns/_TEMPLATE.md`. Scale definitions: `patterns/SCALES.md`.

### Scripts

- `scripts/build.py` — copies patterns into `docs/patterns/`, generates `docs/index.md` with patterns grouped by scale, outputs suggested mkdocs nav
- `scripts/generate_graph.py` — reads frontmatter `context_patterns`/`completion_patterns` to produce a Graphviz `.dot` file showing the cross-reference graph

## Key Conventions

- Pattern cross-references in prose use the format `**Pattern Name (ID)**` (e.g., `**Generative Culture (1)**`)
- British English spelling throughout (organisation, behaviour, colour, etc.)
- The `id` in frontmatter must match the numeric prefix of the filename
- Confidence stars in the heading use literal `**` characters, not markdown bold for the stars themselves
- `docs/` is regenerated from scratch by `build.py` — the script deletes and recreates `docs/patterns/` each run
