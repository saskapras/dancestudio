# === Stage 6: Связанная сущность ===
# Project: DanceStudio
from typing import Dict, List, Optional

class Lesson:
    def __init__(self, lesson_id: str, group_id: str, day: str, start_time: str,
                 end_time: str, instructor: str):
        self.lesson_id = lesson_id
        self.group_id = group_id
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.instructor = instructor

    def to_dict(self) -> Dict:
        return {
            "lesson_id": self.lesson_id,
            "group_id": self.group_id,
            "day": self.day,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "instructor": self.instructor,
        }

    def __str__(self) -> str:
        return (
            f"Lesson {self.lesson_id}: group {self.group_id}, {self.day} "
            f"{self.start_time}-{self.end_time}, instructor {self.instructor}"
        )


class DanceStudioModel:
    def __init__(self):
        self._lessons: Dict[str, Lesson] = {}

    def add_lesson(self, lesson: Lesson) -> None:
        if not lesson.lesson_id:
            raise ValueError("lesson_id is required to add a lesson")
        if lesson.group_id not in self._lessons:
            raise KeyError(
                f"group_id {lesson.group_id} not found. "
                "Add the group before its lesson."
            )
        self._lessons[lesson.lesson_id] = lesson

    def get_lesson(self, lesson_id: str) -> Optional[Lesson]:
        return self._lessons.get(lesson_id)

    def get_lessons_for_group(self, group_id: str) -> List[Lesson]:
        return [lesson for lesson in self._lessons.values() if lesson.group_id == group_id]

    def get_lessons_on_day(self, day: str) -> List[Lesson]:
        return [lesson for lesson in self._lessons.values() if lesson.day == day]

    def list_lessons(self) -> List[Lesson]:
        return list(self._lessons.values())

    def remove_lesson(self, lesson_id: str) -> bool:
        return self._lessons.pop(lesson_id, None) is not None
