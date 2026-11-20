# === Stage 8: Сортировка записей ===
# Project: DanceStudio
def sort_by_name(records):
    return sorted(records, key=lambda r: r["name"])


def sort_by_created_at(records):
    return sorted(records, key=lambda r: r["created_at"])


def sort_by_name_then_created_at(records):
    return sorted(
        records,
        key=lambda r: (r["name"], r["created_at"]),
    )


def sort_by_created_at_then_name(records):
    return sorted(
        records,
        key=lambda r: (r["created_at"], r["name"]),
    )


def sort_desc(records, key):
    return sorted(records, key=key, reverse=True)


def sort_desc_by_name(records):
    return sort_desc(records, lambda r: r["name"])


def sort_desc_by_created_at(records):
    return sort_desc(records, lambda r: r["created_at"])


def sort_desc_by_name_then_created_at(records):
    return sort_desc(
        records,
        lambda r: (r["name"], r["created_at"]),
    )


def sort_desc_by_created_at_then_name(records):
    return sort_desc(
        records,
        lambda r: (r["created_at"], r["name"]),
    )


def sort_stable(records, key, reverse=False):
    return sorted(records, key=key, reverse=reverse)


def sort_groups(records):
    return sort_stable(records, lambda r: r["name"])


def sort_groups_desc(records):
    return sort_stable(records, lambda r: r["name"], reverse=True)


def sort_groups_by_created_at(records):
    return sort_stable(records, lambda r: r["created_at"])


def sort_groups_by_created_at_desc(records):
    return sort_stable(records, lambda r: r["created_at"], reverse=True)
