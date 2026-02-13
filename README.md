# A Pattern Language for DevOps

A pattern language for how software engineering organisations build, deliver, and operate software — from organisational culture down to individual tool practices. Following Christopher Alexander's methodology from *A Pattern Language* (1977).

AI is not a section. It is a force present at every level.

## Structure

- `patterns/` — one markdown file per pattern, with YAML frontmatter for metadata
- `scripts/` — build tools (graph generation, site preparation)
- `docs/` — MkDocs source for the website
- `mkdocs.yml` — site configuration

## Contributing

1. Clone the repo
2. Edit or create pattern files in `patterns/` using any text editor
3. Follow the pattern template in `patterns/_TEMPLATE.md`
4. Submit a PR

## Pattern format

Each pattern follows Alexander's structure:

- **Name and confidence rating** (`**` = invariant, `*` = likely true, no star = hypothesis)
- **Opening context** — links to larger patterns
- **Problem** — in bold
- **Discussion** — evidence, reasoning, trade-offs
- **Solution** — in bold
- **Diagram** — where helpful
- **Closing cross-references** — links to smaller patterns
- **References** — published sources

## Building the site

```bash
pip install mkdocs-material pyyaml
python scripts/build.py          # generates docs/ from patterns/
mkdocs serve                     # local preview at http://localhost:8000
mkdocs gh-deploy                 # deploy to GitHub Pages
```

## Generating the pattern graph

```bash
python scripts/generate_graph.py   # outputs docs/assets/pattern-graph.dot
dot -Tsvg docs/assets/pattern-graph.dot -o docs/assets/pattern-graph.svg
```

## Licence

Content: [CC0 1.0](https://creativecommons.org/public-domain/cc0/)
Code: [MIT](LICENSE-CODE)
