# === Stage 11: Группировка ===
# Project: DanceStudio
from collections import Counter

GroupStyle = dict[str, list[str]]


def group_by_style(groups: list[dict]) -> GroupStyle:
    styles: GroupStyle = {}
    for group in groups:
        style = group["style"]
        styles.setdefault(style, []).append(group["title"])
    return styles


def count_by_style(groups: list[dict]) -> Counter:
    return Counter(group["style"] for group in groups)


def report_style_counts(groups: list[dict]) -> None:
    counts = count_by_style(groups)
    for style, total in counts.most_common():
        listed = ", ".join(sorted(counts[style]))
        print(f"{style}: {total} group(s) -> {listed}")


if __name__ == "__main__":
    sample = [
        {"title": "Groove", "style": "hiphop", "level": "intermediate", "hall": "A"},
        {"title": "Pump", "style": "hiphop", "level": "beginner", "hall": "B"},
        {"title": "Salsa Class", "style": "latin", "level": "advanced", "hall": "C"},
        {"title": "Jazz", "style": "jazz", "level": "intermediate", "hall": "A"},
        {"title": "Ballet", "style": "classical", "level": "beginner", "hall": "D"},
    ]
    report_style_counts(sample)
