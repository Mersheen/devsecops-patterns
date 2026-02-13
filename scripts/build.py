#!/usr/bin/env python3
"""
Build the MkDocs docs/ directory from pattern source files.

Copies pattern markdown into docs/patterns/, generates the nav structure,
and creates the index page. Run before `mkdocs serve` or `mkdocs build`.

Usage:
    python scripts/build.py
"""

import os
import re
import shutil
import yaml

PATTERNS_DIR = "patterns"
DOCS_DIR = "docs"
DOCS_PATTERNS_DIR = os.path.join(DOCS_DIR, "patterns")

SCALE_NAMES = {
    1: "Organisational Philosophy",
    2: "Organisational Structure",
    3: "Value and Architecture",
    4: "Development Practices",
    5: "Delivery Pipeline",
    6: "Infrastructure and Platform",
    7: "Security and Trust",
    8: "Observability, Feedback, and Operations",
}


def extract_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\n(.+?)\n---", content, re.DOTALL)
    if not match:
        return None, content
    try:
        meta = yaml.safe_load(match.group(1))
        body = content[match.end():].lstrip("\n")
        return meta, body
    except yaml.YAMLError:
        return None, content


def confidence_stars(level):
    if level == 2:
        return " \\*\\*"
    elif level == 1:
        return " \\*"
    return ""


def load_all_patterns():
    patterns = {}
    for filename in sorted(os.listdir(PATTERNS_DIR)):
        if not filename.endswith(".md") or filename.startswith("_") or filename == "SCALES.md":
            continue
        filepath = os.path.join(PATTERNS_DIR, filename)
        meta, body = extract_frontmatter(filepath)
        if meta and "id" in meta and meta["id"] != 0:
            patterns[meta["id"]] = {
                "meta": meta,
                "body": body,
                "filename": filename,
            }
    return patterns


def generate_index(patterns):
    """Generate the main index page."""
    lines = []
    lines.append("# A Pattern Language for DevOps")
    lines.append("")
    lines.append("A pattern language for how software engineering organisations build, deliver,")
    lines.append("and operate software. Following Christopher Alexander's methodology.")
    lines.append("")
    lines.append("AI is not a section. It is a force present at every level.")
    lines.append("")
    lines.append('![Pattern Graph](assets/pattern-graph.svg){ loading=lazy }')
    lines.append("")
    lines.append("## Patterns by Scale")
    lines.append("")

    by_scale = {}
    for pid, pdata in sorted(patterns.items()):
        scale = pdata["meta"].get("scale", 0)
        by_scale.setdefault(scale, []).append((pid, pdata))

    for scale in sorted(by_scale.keys()):
        scale_name = SCALE_NAMES.get(scale, f"Scale {scale}")
        lines.append(f"### {scale_name}")
        lines.append("")

        for pid, pdata in sorted(by_scale[scale]):
            name = pdata["meta"].get("name", f"Pattern {pid}")
            conf = pdata["meta"].get("confidence", 0)
            stars = " \\*\\*" if conf == 2 else " \\*" if conf == 1 else ""
            ai = " · AI" if pdata["meta"].get("ai_dimension") else ""
            doc_name = pdata["filename"].replace(".md", "")
            lines.append(f"- [{pid}. {name}{stars}](patterns/{doc_name}.md){ai}")

        lines.append("")

    lines.append("## About")
    lines.append("")
    lines.append("Confidence ratings follow Alexander's convention:")
    lines.append("")
    lines.append("- **\\*\\*** — the author believes this is an invariant")
    lines.append("- **\\*** — likely true but the form is uncertain")
    lines.append("- **no star** — a hypothesis")
    lines.append("")
    lines.append("Patterns marked **AI** have their forces meaningfully modified by AI.")

    return "\n".join(lines)


def main():
    patterns = load_all_patterns()
    print(f"Loaded {len(patterns)} patterns")

    # Clean and recreate docs/patterns/
    if os.path.exists(DOCS_PATTERNS_DIR):
        shutil.rmtree(DOCS_PATTERNS_DIR)
    os.makedirs(DOCS_PATTERNS_DIR, exist_ok=True)
    os.makedirs(os.path.join(DOCS_DIR, "assets"), exist_ok=True)

    # Copy pattern files into docs/patterns/
    for pid, pdata in patterns.items():
        src = os.path.join(PATTERNS_DIR, pdata["filename"])
        dst = os.path.join(DOCS_PATTERNS_DIR, pdata["filename"])
        shutil.copy2(src, dst)

    # Generate index
    index_content = generate_index(patterns)
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(index_content)

    print(f"Generated {DOCS_DIR}/index.md")
    print(f"Copied {len(patterns)} patterns to {DOCS_PATTERNS_DIR}/")

    # Generate nav for mkdocs.yml
    print("\nSuggested nav for mkdocs.yml:")
    print("nav:")
    print("  - Home: index.md")
    print("  - Patterns:")
    for pid, pdata in sorted(patterns.items()):
        name = pdata["meta"].get("name", f"Pattern {pid}")
        fname = pdata["filename"]
        print(f"    - '{pid}. {name}': patterns/{fname}")


if __name__ == "__main__":
    main()
