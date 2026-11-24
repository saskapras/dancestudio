# === Stage 16: Общая сводка ===
# Project: DanceStudio
from collections import Counter


def summarize_groups(groups):
    """Return a summary of all groups: count, style distribution and newest records."""
    if not groups:
        return {
            "total": 0,
            "by_style": {},
            "newest": [],
        }

    style_counts = Counter(group["style"] for group in groups)
    newest = sorted(groups, key=lambda g: g["last_updated"], reverse=True)

    return {
        "total": len(groups),
        "by_style": dict(style_counts.most_common()),
        "newest": newest,
    }
