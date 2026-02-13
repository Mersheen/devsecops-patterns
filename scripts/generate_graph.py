#!/usr/bin/env python3
"""
Generate a Graphviz .dot file from pattern frontmatter.

Reads all pattern markdown files in patterns/, extracts YAML frontmatter,
and produces a directed graph showing cross-references between patterns.

Usage:
    python scripts/generate_graph.py
    dot -Tsvg docs/assets/pattern-graph.dot -o docs/assets/pattern-graph.svg
"""

import os
import re
import yaml

PATTERNS_DIR = "patterns"
OUTPUT_DOT = "docs/assets/pattern-graph.dot"

SCALE_COLOURS = {
    0: "#999999",   # Cross-cutting
    1: "#8B0000",   # Organisational Philosophy
    2: "#CC4400",   # Organisational Structure
    3: "#CC8800",   # Product and Value
    4: "#668800",   # Development Practices
    5: "#006644",   # Delivery Pipeline
    6: "#006688",   # Quality and Testing
    7: "#004488",   # Infrastructure and Platform
    8: "#440088",   # Security
    9: "#880044",   # Observability and Feedback
    10: "#444444",  # Operational Excellence
}

SCALE_NAMES = {
    0: "Cross-Cutting",
    1: "Organisational Philosophy",
    2: "Organisational Structure",
    3: "Product and Value",
    4: "Development Practices",
    5: "Delivery Pipeline",
    6: "Quality and Testing",
    7: "Infrastructure and Platform",
    8: "Security",
    9: "Observability and Feedback",
    10: "Operational Excellence",
}


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.+?)\n---", content, re.DOTALL)
    if not match:
        return None

    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        print(f"Warning: could not parse frontmatter in {filepath}")
        return None


def load_patterns():
    """Load all pattern files and return a dict of id -> metadata."""
    patterns = {}

    for filename in sorted(os.listdir(PATTERNS_DIR)):
        if not filename.endswith(".md"):
            continue
        if filename.startswith("_") or filename == "SCALES.md":
            continue

        filepath = os.path.join(PATTERNS_DIR, filename)
        meta = extract_frontmatter(filepath)

        if meta and "id" in meta and meta["id"] != 0:
            patterns[meta["id"]] = meta

    return patterns


def confidence_label(level):
    """Convert confidence number to Alexander's star notation."""
    if level == 2:
        return " **"
    elif level == 1:
        return " *"
    return ""


def generate_dot(patterns):
    """Generate the .dot file content."""
    lines = []
    lines.append("digraph PatternLanguage {")
    lines.append('    rankdir=TB;')
    lines.append('    node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=10];')
    lines.append('    edge [color="#666666", arrowsize=0.7];')
    lines.append("")

    # Group by scale using subgraphs
    scales_used = sorted(set(p.get("scale", 0) for p in patterns.values()))

    for scale in scales_used:
        scale_patterns = {pid: p for pid, p in patterns.items() if p.get("scale", 0) == scale}
        if not scale_patterns:
            continue

        colour = SCALE_COLOURS.get(scale, "#CCCCCC")
        scale_name = SCALE_NAMES.get(scale, f"Scale {scale}")

        lines.append(f"    subgraph cluster_{scale} {{")
        lines.append(f'        label="{scale_name}";')
        lines.append(f'        style=dashed;')
        lines.append(f'        color="{colour}";')
        lines.append(f'        fontname="Helvetica";')
        lines.append(f'        fontsize=11;')
        lines.append("")

        for pid, meta in sorted(scale_patterns.items()):
            name = meta.get("name", f"Pattern {pid}")
            conf = confidence_label(meta.get("confidence", 0))
            ai = " [AI]" if meta.get("ai_dimension") else ""
            label = f"{pid}. {name}{conf}{ai}"
            fill = colour + "33"  # Add transparency
            lines.append(f'        p{pid} [label="{label}", fillcolor="{fill}", color="{colour}"];')

        lines.append("    }")
        lines.append("")

    # Edges: context_patterns (upward links) drawn as dotted
    # completion_patterns (downward links) drawn as solid
    lines.append("    // Completion links (downward)")
    for pid, meta in sorted(patterns.items()):
        for target in meta.get("completion_patterns", []):
            if target in patterns:
                lines.append(f"    p{pid} -> p{target};")

    lines.append("")
    lines.append("    // Context links (upward, dashed)")
    for pid, meta in sorted(patterns.items()):
        for target in meta.get("context_patterns", []):
            if target in patterns:
                # Only draw context edges that aren't already captured
                # as a completion edge from the other side
                if pid not in patterns[target].get("completion_patterns", []):
                    lines.append(f"    p{target} -> p{pid} [style=dashed];")

    lines.append("}")
    return "\n".join(lines)


def main():
    patterns = load_patterns()
    print(f"Loaded {len(patterns)} patterns")

    os.makedirs(os.path.dirname(OUTPUT_DOT), exist_ok=True)

    dot_content = generate_dot(patterns)
    with open(OUTPUT_DOT, "w", encoding="utf-8") as f:
        f.write(dot_content)

    print(f"Generated {OUTPUT_DOT}")
    print(f"Run: dot -Tsvg {OUTPUT_DOT} -o docs/assets/pattern-graph.svg")


if __name__ == "__main__":
    main()
