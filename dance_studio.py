# === Stage 1: Каркас модуля ===
# Project: DanceStudio
from dataclasses import dataclass, field


@dataclass
class Group:
    """A dance group belonging to a particular style and level."""

    name: str
    style: str
    level: str
    hall: str
    members: list = field(default_factory=list)


def make_demo_groups() -> list:
    """Return a small set of demonstration groups."""
    return [
        Group(name="Nova", style="Jazz", level="Beginner", hall="Hall A"),
        Group(name="Pulse", style="Hip-Hop", level="Intermediate", hall="Hall B"),
        Group(name="Velvet", style="Contemporary", level="Advanced", hall="Hall A"),
    ]


def main() -> None:
    """Print a short overview of the demonstration data."""
    groups = make_demo_groups()
    for group in groups:
        print(f"{group.name} | {group.style} | {group.level} | {group.hall}")
    print(f"Total groups: {len(groups)}")


if __name__ == "__main__":
    main()
