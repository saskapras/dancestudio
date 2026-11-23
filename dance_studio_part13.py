# === Stage 13: Слияние записей ===
# Project: DanceStudio
"""Stage 13 module: merge two 'group' records with a winner chosen per field.

Self-contained helper for the DanceStudio project. Uses only the standard
library and does not depend on any other module.
"""

from __future__ import annotations

from typing import Any


class MergeResult:
    """Holds the merged record together with the winning value per field."""

    def __init__(self, merged: dict[str, Any], winners: dict[str, Any]) -> None:
        self.merged = merged
        self.winners = winners

    def __repr__(self) -> str:
        return f"MergeResult(merged={self.merged!r}, winners={self.winners!r})"


def merge_records(
    record_a: dict[str, Any],
    record_b: dict[str, Any],
    field_winners: dict[str, Any],
) -> MergeResult:
    """Merge two group records.

    The merged record is a copy of record_a. For every key, the value is taken
    from record_a unless a winning value is provided in field_winners, in which
    case that value overrides the merged one.
    """
    merged: dict[str, Any] = dict(record_a)
    merged.update(record_b)

    winners: dict[str, Any] = {}
    for field, value in field_winners.items():
        if field not in merged:
            raise KeyError(f"Field {field!r} not present in both records")
        winners[field] = value
        merged[field] = value

    return MergeResult(merged, winners)


def merge_records_by_rule(
    record_a: dict[str, Any],
    record_b: dict[str, Any],
    rule: str,
) -> MergeResult:
    """Merge two group records using a simple selection rule.

    Supported rules:
      - 'a'   keep record_a value for every field
      - 'b'   keep record_b value for every field
      - 'both' take record_b value only for fields present in both records
    """
    if rule not in ("a", "b", "both"):
        raise ValueError(f"Unknown merge rule: {rule!r}")

    field_winners: dict[str, Any] = {}
    for field in record_a.keys() & record_b.keys():
        if rule == "a":
            field_winners[field] = record_a[field]
        elif rule == "b":
            field_winners[field] = record_b[field]
        # rule == "both": both values are identical, pick either

    return merge_records(record_a, record_b, field_winners)


def main() -> None:
    group_a = {
        "name": "Rhythm Crew",
        "style": "Jazz",
        "level": "Beginner",
        "hall": "Hall A",
    }
    group_b = {
        "name": "Rhythm Crew",
        "style": "Hip Hop",
        "level": "Advanced",
        "hall": "Hall B",
    }

    chosen_winners = {
        "name": group_a["name"],
        "style": group_b["style"],
        "level": group_b["level"],
        "hall": group_a["hall"],
    }

    result = merge_records(group_a, group_b, chosen_winners)
    print("Merged record:", result.merged)
    print("Winners per field:", result.winners)


if __name__ == "__main__":
    main()
