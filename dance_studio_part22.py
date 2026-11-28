# === Stage 22: Текстовая гистограмма ===
# Project: DanceStudio
"""Level distribution histogram for dance studio groups.

Text-based histogram of the 'level' field values across all groups,
built with ASCII block characters. Standard library only.
"""

BLOCK = "-"
EMPTY_LINE = " "


def _count_levels(groups):
    """Return a mapping of level name to number of groups at that level."""
    counts = {}
    for group in groups:
        level = group.level
        counts[level] = counts.get(level, 0) + 1
    return counts


def _max_count(counts):
    """Return the highest count so the histogram scales to its length."""
    if not counts:
        return 0
    return max(counts.values())


def render_histogram(groups):
    """Render a text histogram of the 'level' field distribution.

    Each level appears on its own line, ordered by name. The count is
    shown as a number followed by that many BLOCK characters.
    """
    counts = _count_levels(groups)
    scale = _max_count(counts)
    lines = []
    for level in sorted(counts):
        bar = BLOCK * counts[level]
        lines.append(f"{level:<8} {counts[level]:<4} {bar}")
    return "\n".join(lines)


def display_histogram(groups):
    """Print the level histogram to standard output."""
    print(render_histogram(groups))


if __name__ == "__main__":
    demo = [
        {"name": "Salsa", "style": "Latin", "level": "intermediate", "hall": "A"},
        {"name": "Jazz", "style": "Jazz", "level": "beginner", "hall": "B"},
        {"name": "Ballet", "style": "Classical", "level": "advanced", "hall": "A"},
        {"name": "HipHop", "style": "Urban", "level": "beginner", "hall": "B"},
        {"name": "Tango", "style": "Latin", "level": "intermediate", "hall": "C"},
    ]
    display_histogram(demo)
