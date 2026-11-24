# === Stage 14: Избранное ===
# Project: DanceStudio
class FavoriteMixin:
    def __init__(self):
        self.is_favorite = False

    def toggle_favorite(self):
        self.is_favorite = not self.is_favorite

    def mark_favorite(self):
        self.is_favorite = True

    def unmark_favorite(self):
        self.is_favorite = False

    def is_favorited(self):
        return self.is_favorite

    def favorites(self, groups):
        return [group for group in groups if group.is_favorite]

    def __repr__(self):
        marker = " (favorite)" if self.is_favorite else ""
        return f"<{type(self).__name__} {self.name}{marker}>"


class Group(FavoriteMixin):
    def __init__(self, name, style, level, hall):
        self.name = name
        self.style = style
        self.level = level
        self.hall = hall
        super().__init__()

    def __str__(self):
        return f"{self.name} ({self.style}, level {self.level}, hall {self.hall})"


def add_favorite(groups, group_name):
    for group in groups:
        if group.name == group_name:
            group.mark_favorite()
            return group
    raise KeyError(f"Group '{group_name}' not found")


def remove_favorite(groups, group_name):
    for group in groups:
        if group.name == group_name:
            group.unmark_favorite()
            return group
    raise KeyError(f"Group '{group_name}' not found")


def list_favorites(groups):
    result = groups.favorites(groups)
    if not result:
        return []
    return sorted(result, key=lambda g: g.name)


def favorite_count(groups):
    return sum(1 for group in groups if group.is_favorite)


def toggle_favorite(groups, group_name):
    for group in groups:
        if group.name == group_name:
            group.toggle_favorite()
            return group
    raise KeyError(f"Group '{group_name}' not found")


if __name__ == "__main__":
    demo = [
        Group("Contemporary Flow", "Contemporary", 2, "Hall A"),
        Group("Jazz Fusion", "Jazz", 1, "Hall B"),
        Group("Hip Hop Crew", "Hip Hop", 3, "Hall A"),
    ]
    toggle_favorite(demo, "Contemporary Flow")
    for group in list_favorites(demo):
        print(group)
    print(f"Total favorites: {favorite_count(demo)}")
