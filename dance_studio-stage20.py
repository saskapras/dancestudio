# === Stage 20: Серии по дням ===
# Project: DanceStudio
from collections import namedtuple

Series = namedtuple("Series", ["start_day", "end_day", "count"])


def _is_active_day(schedule, group_id, day):
    for item in schedule:
        if item["group_id"] == group_id and item["day"] == day:
            return True
    return False


def find_series(schedule, group_id, min_count=1):
    days = sorted({item["day"] for item in schedule if item["group_id"] == group_id})
    series = []
    current = []
    for day in days:
        if _is_active_day(schedule, group_id, day):
            current.append(day)
        else:
            if len(current) >= min_count:
                series.append(Series(current[0], current[-1], len(current)))
            current = []
    if len(current) >= min_count:
        series.append(Series(current[0], current[-1], len(current)))
    return series
