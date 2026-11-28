# === Stage 21: Топ записей ===
# Project: DanceStudio
from collections import Counter


def top_n_groups(groups, field, n):
    """Return the top-N groups ordered by the given field.

    Ties are broken by group name so the result is deterministic.
    Missing values are treated as the smallest possible and ignored
    from the ranking.
    """
    if n is None or n <= 0:
        return [group for group in groups]

    def sort_key(group):
        value = getattr(group, field, None)
        return (value if value is not None else float("-inf"), group.name)

    ranked = sorted(groups, key=sort_key, reverse=True)
    return ranked[:n]


if __name__ == "__main__":
    class Group:
        def __init__(self, name, style, level, hall):
            self.name = name
            self.style = style
            self.level = level
            self.hall = hall

    teams = [
        Group("Aurora", "Jazz", "Advanced", "Hall 1"),
        Group("Breeze", "Hip-Hop", "Beginner", "Hall 2"),
        Group("Comet", "Contemporary", "Intermediate", "Hall 1"),
        Group("Delta", "Salsa", "Advanced", "Hall 3"),
        Group("Echo", "Ballet", "Beginner", "Hall 2"),
    ]

    print("Top 2 most advanced groups:")
    for g in top_n_groups(teams, "level", 2):
        print(" -", g.name)

    print("Top 3 groups by hall:")
    for g in top_n_groups(teams, "hall", 3):
        print(" -", g.name)
