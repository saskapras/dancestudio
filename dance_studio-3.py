# === Stage 3: Хранилище в памяти ===
# Project: DanceStudio
"""In-memory storage for dance groups (DanceStudio stage 3).

Provides add, get-by-id and list operations on group entities.
"""

from __future__ import annotations


class Group:
    """A dance group with a name, style, level and hall."""

    def __init__(self, group_id: str, name: str, style: str, level: str, hall: str) -> None:
        self.group_id = group_id
        self.name = name
        self.style = style
        self.level = level
        self.hall = hall

    def __repr__(self) -> str:
        return (
            f"Group(group_id={self.group_id!r}, name={self.name!r}, "
            f"style={self.style!r}, level={self.level!r}, hall={self.hall!r})"
        )


class GroupStore:
    """A simple in-memory dictionary keyed by group id."""

    def __init__(self) -> None:
        self._groups: dict[str, Group] = {}

    def add(self, group: Group) -> None:
        """Insert a group, replacing any existing entry with the same id."""
        self._groups[group.group_id] = group

    def get(self, group_id: str) -> Group | None:
        """Return the group with the given id, or None if not found."""
        return self._groups.get(group_id)

    def list(self) -> list[Group]:
        """Return all stored groups as a new list."""
        return list(self._groups.values())

    def __len__(self) -> int:
        return len(self._groups)


def build_sample_store() -> GroupStore:
    """Create a GroupStore pre-populated with a few example groups."""
    store = GroupStore()
    store.add(Group("g1", "Jazz Crew", "Jazz", "Intermediate", "Hall A"))
    store.add(Group("g2", "Hip-Hop Squad", "Hip-Hop", "Beginner", "Hall B"))
    store.add(Group("g3", "Contemporary Flow", "Contemporary", "Advanced", "Hall A"))
    return store


if __name__ == "__main__":
    demo = build_sample_store()
    for group in demo.list():
        print(group)
    print("Total groups:", len(demo))
    found = demo.get("g2")
    print("Lookup g2:", found)
    missing = demo.get("nope")
    print("Lookup nope:", missing)
