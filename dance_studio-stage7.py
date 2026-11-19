# === Stage 7: Связи между сущностями ===
# Project: DanceStudio
from datetime import date


def find_group_by_id(groups, group_id):
    for group in groups:
        if group["id"] == group_id:
            return group
    return None


def find_sessions_for_group(sessions, group_id):
    result = []
    for session in sessions:
        if session["group_id"] == group_id:
            result.append(session)
    return result


def verify_group_sessions_integrity(groups, sessions, group_id):
    group = find_group_by_id(groups, group_id)
    if group is None:
        return None
    referenced_group_ids = {session["group_id"] for session in sessions}
    orphaned_sessions = [
        session for session in sessions
        if session["group_id"] not in {g["id"] for g in groups}
    ]
    missing_group_refs = referenced_group_ids - {g["id"] for g in groups}
    return {
        "group": group,
        "sessions": find_sessions_for_group(sessions, group_id),
        "orphaned_sessions": orphaned_sessions,
        "missing_group_refs": sorted(missing_group_refs),
        "is_consistent": (
            not orphaned_sessions
            and not missing_group_refs
            and group_id in referenced_group_ids
        ),
    }


def main():
    sample_groups = [
        {"id": 1, "name": "Jazz", "style": "Jazz", "level": "intermediate", "hall": "A"},
        {"id": 2, "name": "HipHop", "style": "HipHop", "level": "beginner", "hall": "B"},
    ]
    sample_sessions = [
        {"id": 1, "group_id": 1, "date": date(2025, 1, 6), "time": "18:00"},
        {"id": 2, "group_id": 1, "date": date(2025, 1, 7), "time": "18:00"},
        {"id": 3, "group_id": 2, "date": date(2025, 1, 6), "time": "19:00"},
        {"id": 4, "group_id": 99, "date": date(2025, 1, 8), "time": "20:00"},
    ]
    target_group_id = 1
    integrity = verify_group_sessions_integrity(
        sample_groups, sample_sessions, target_group_id
    )
    print("Group:", integrity["group"]["name"])
    print("Sessions:", len(integrity["sessions"]))
    print("Orphaned sessions:", integrity["orphaned_sessions"])
    print("Missing group refs:", integrity["missing_group_refs"])
    print("Is consistent:", integrity["is_consistent"])


if __name__ == "__main__":
    main()
