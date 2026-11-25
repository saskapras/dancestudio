# === Stage 18: Месячный отчёт ===
# Project: DanceStudio
from datetime import datetime

def parse_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None

def format_month(date):
    return date.strftime("%B %Y")

def month_key(date):
    return date.strftime("%Y-%m")

def summarize_sessions(sessions):
    total_sessions = 0
    total_students = 0
    total_attendance = 0
    by_style = {}
    by_group = {}
    for session in sessions:
        total_sessions += 1
        total_students += session.get("students", 0)
        total_attendance += session.get("attendance", 0)
        style = session.get("style", "unknown")
        group = session.get("group", "unknown")
        by_style[style] = by_style.get(style, 0) + 1
        by_group[group] = by_group.get(group, 0) + 1
    return {
        "month": format_month(date),
        "sessions": total_sessions,
        "students": total_students,
        "attendance": total_attendance,
        "average_attendance": round(total_attendance / total_sessions, 2)
        if total_sessions else 0.0,
        "by_style": by_style,
        "by_group": by_group,
    }

def build_month_report(sessions, previous_month_sessions):
    current = summarize_sessions(sessions)
    previous = summarize_sessions(previous_month_sessions)
    if current["sessions"] and previous["sessions"]:
        sessions_delta = current["sessions"] - previous["sessions"]
        sessions_change = round(
            sessions_delta / previous["sessions"] * 100, 2
        )
        attendance_change = (
            round(
                (current["average_attendance"]
                 - previous["average_attendance"])
                / previous["average_attendance"]
                * 100,
                2,
            )
            if previous["average_attendance"] else 0.0
        )
    else:
        sessions_change = 0.0
        attendance_change = 0.0
    return {
        "month": current["month"],
        "sessions": current["sessions"],
        "students": current["students"],
        "attendance": current["attendance"],
        "average_attendance": current["average_attendance"],
        "sessions_change": sessions_change,
        "attendance_change": attendance_change,
        "by_style": current["by_style"],
        "by_group": current["by_group"],
    }

def render_month_report(report):
    lines = [
        "Monthly Report",
        "==============",
        f"Month: {report['month']}",
        f"Sessions: {report['sessions']}",
        f"Unique students: {report['students']}",
        f"Total attendance: {report['attendance']}",
        f"Average attendance: {report['average_attendance']}",
        f"Sessions change: {report['sessions_change']}%",
        f"Attendance change: {report['attendance_change']}%",
        "",
        "Sessions by style:",
    ]
    for style, count in report["by_style"].items():
        lines.append(f"  {style}: {count}")
    lines.append("")
    lines.append("Sessions by group:")
    for group, count in report["by_group"].items():
        lines.append(f"  {group}: {count}")
    return "\n".join(lines)
