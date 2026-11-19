# === Stage 5: Удаление и восстановление ===
# Project: DanceStudio
from datetime import datetime


class GroupDeletionError(Exception):
    """Raised when a group cannot be soft-deleted."""


class SoftDeletedGroup:
    """Represents a group marked as deleted, ready to be restored."""

    def __init__(self, group_id, title, style, level, hall, deleted_at):
        self.group_id = group_id
        self.title = title
        self.style = style
        self.level = level
        self.hall = hall
        self.deleted_at = deleted_at

    @property
    def is_deleted(self):
        return True

    def restore(self):
        return Group(self.group_id, self.title, self.style, self.level, self.hall)


class Group:
    def __init__(self, group_id, title, style, level, hall):
        self.group_id = group_id
        self.title = title
        self.style = style
        self.level = level
        self.hall = hall
        self.deleted_at = None

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def delete(self):
        if self.is_deleted:
            return
        self.deleted_at = datetime.now()

    def restore(self):
        if not self.is_deleted:
            raise GroupDeletionError("Group is not deleted")
        self.deleted_at = None


def build_group_store(groups):
    store = {}
    for group in groups:
        store[group.group_id] = group
    return store


def remove_group(store, group_id):
    if group_id not in store:
        raise KeyError(group_id)
    store[group_id].delete()


def restore_group(store, group_id):
    if group_id not in store:
        raise KeyError(group_id)
    store[group_id].restore()


def list_active_groups(store):
    return [g for g in store.values() if not g.is_deleted]


def list_deleted_groups(store):
    return [g for g in store.values() if g.is_deleted]


if __name__ == "__main__":
    store = build_group_store([
        Group("g1", "HipHop Crew", "hiphop", "intermediate", "hall_a"),
        Group("g2", "Jazz Ensemble", "jazz", "advanced", "hall_b"),
    ])

    remove_group(store, "g1")
    print("Active groups:", [g.title for g in list_active_groups(store)])
    print("Deleted groups:", [g.title for g in list_deleted_groups(store)])

    restore_group(store, "g1")
    print("Active groups after restore:", [g.title for g in list_active_groups(store)])
