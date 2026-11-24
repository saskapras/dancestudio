# === Stage 15: Статусы записей ===
# Project: DanceStudio
from enum import Enum


class GroupStatus(Enum):
    DRAFT = "draft"
    CREATED = "created"
    ACTIVE = "active"
    PAUSED = "paused"
    CANCELLED = "cancelled"

    @property
    def label(self):
        return f"status:{self.value}"


GROUP_TRANSITIONS = {
    GroupStatus.DRAFT: {GroupStatus.CREATED},
    GroupStatus.CREATED: {GroupStatus.ACTIVE, GroupStatus.CANCELLED},
    GroupStatus.ACTIVE: {GroupStatus.PAUSED, GroupStatus.CANCELLED},
    GroupStatus.PAUSED: {GroupStatus.ACTIVE},
    GroupStatus.CANCELLED: set(),
}


class InvalidTransitionError(ValueError):
    pass


class GroupLifecycle:
    def __init__(self, status=GroupStatus.DRAFT):
        self.status = status

    def can_transition_to(self, target):
        return target in GROUP_TRANSITIONS.get(self.status, set())

    def transition_to(self, target):
        if not self.can_transition_to(target):
            raise InvalidTransitionError(
                f"Cannot transition from {self.status.value} to {target.value}"
            )
        self.status = target
        return self.status


def build_initial_status():
    return GroupLifecycle()


def promote_to_active(lifecycle):
    if lifecycle.can_transition_to(GroupStatus.ACTIVE):
        lifecycle.transition_to(GroupStatus.ACTIVE)
        return True
    return False


def pause_group(lifecycle):
    if lifecycle.can_transition_to(GroupStatus.PAUSED):
        lifecycle.transition_to(GroupStatus.PAUSED)
        return True
    return False


def reactivate_group(lifecycle):
    if lifecycle.can_transition_to(GroupStatus.ACTIVE):
        lifecycle.transition_to(GroupStatus.ACTIVE)
        return True
    return False


def cancel_group(lifecycle):
    if lifecycle.can_transition_to(GroupStatus.CANCELLED):
        lifecycle.transition_to(GroupStatus.CANCELLED)
        return True
    return False
