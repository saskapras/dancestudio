# === Stage 17: Недельный отчёт ===
# Project: DanceStudio
from datetime import date, timedelta


def _format_group(group):
    return (
        f"{group.name:<16} | {group.style:<12} | "
        f"level {group.level:<3} | hall {group.hall}"
    )


def _format_lesson(lesson):
    return (
        f"{lesson.subject:<18} | {lesson.day:<10} | "
        f"{lesson.start_time:<8} | {lesson.hall}"
    )


def _compute_week(dates):
    if not dates:
        return []
    return [dates[0] + timedelta(days=d) for d in range(7)]


def _build_schedule_lines(group, lessons):
    lines = []
    for lesson in lessons:
        if lesson.group_id != group.id:
            continue
        week = _compute_week(lesson.week_dates)
        for day in week:
            if day.weekday() >= 5:
                continue
            line = _format_lesson(lesson)
            line += f" | {day.isoformat()}"
            lines.append(line)
    return lines


def weekly_report(group, lessons, reference_date=None):
    if reference_date is None:
        reference_date = date.today()
    week = _compute_week([reference_date])
    lines = [f"GROUP: {group.name}", f"STYLE: {group.style}",
             f"LEVEL: {group.level}", f"HALL: {group.hall}",
             f"WEEK: {week[0].isoformat()} - {week[6].isoformat()}"]
    lines.append(_format_group(group))
    lines.append("")
    lines.append("LESSONS:")
    lines.extend(_build_schedule_lines(group, lessons))
    return "\n".join(lines)


if __name__ == "__main__":
    sample_group = type("Group", (), {
        "id": 1, "name": "Hip-Hop Crew", "style": "Hip-Hop",
        "level": 3, "hall": "Hall A"
    })()
    sample_lessons = [
        type("Lesson", (), {
            "id": 10, "group_id": 1, "subject": "Technique",
            "day": "Monday", "start_time": "18:00", "hall": "Hall A",
            "week_dates": [date(2024, 7, 1)]
        })(),
        type("Lesson", (), {
            "id": 11, "group_id": 1, "subject": "Freestyle",
            "day": "Wednesday", "start_time": "19:30", "hall": "Hall A",
            "week_dates": [date(2024, 7, 1)]
        })(),
    ]
    print(weekly_report(sample_group, sample_lessons, date(2024, 6, 30)))
