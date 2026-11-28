# === Stage 23: Ключевые метрики ===
# Project: DanceStudio
import datetime


class StudioMetrics:
    """Compute and report key metrics for the DanceStudio project."""

    def __init__(self, groups, sessions):
        self.groups = groups
        self.sessions = sessions

    def count_groups(self):
        return len(self.groups)

    def count_sessions(self):
        return len(self.sessions)

    def count_unique_styles(self):
        return len({group.style for group in self.groups})

    def count_unique_halls(self):
        return len({group.hall for group in self.groups})

    def avg_sessions_per_group(self):
        if not self.groups:
            return 0.0
        return round(sum(len(s) for s in self.sessions) / self.count_groups(), 2)

    def busiest_day(self):
        if not self.sessions:
            return None
        day_counts = {}
        for session in self.sessions:
            key = session.date.date()
            day_counts[key] = day_counts.get(key, 0) + 1
        busiest = max(day_counts, key=day_counts.get)
        return busiest.isoformat()

    def report(self):
        lines = [
            "=== DanceStudio Metrics ===",
            f"Total groups: {self.count_groups()}",
            f"Total sessions: {self.count_sessions()}",
            f"Unique styles: {self.count_unique_styles()}",
            f"Unique halls: {self.count_unique_halls()}",
            f"Average sessions per group: {self.avg_sessions_per_group()}",
        ]
        busiest = self.busiest_day()
        if busiest:
            lines.append(f"Busiest day: {busiest} ({day_counts[datetime.date.fromisoformat(busiest)]} sessions)")
        else:
            lines.append("Busiest day: N/A")
        return "\n".join(lines)
