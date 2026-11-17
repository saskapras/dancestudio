# === Stage 2: Проверка полей ===
# Project: DanceStudio
import re

GROUP_NAME_MIN = 2
GROUP_NAME_MAX = 60
GROUP_NAME_FORBIDDEN = ("studio", "group", "the", "and", "of", "and")
VALID_STYLES = ("jazz", "hip-hop", "contemporary", "latin", "ballroom", "kpop")
VALID_LEVELS = ("beginner", "intermediate", "advanced")
VALID_HALLS = ("hall-a", "hall-b", "hall-c")


def normalize_input(value):
    if value is None:
        return ""
    if isinstance(value, (int, float)):
        return str(value).strip()
    text = value.strip()
    if not text:
        return ""
    return text.lower().strip()


def normalize_style(value):
    normalized = normalize_input(value)
    for style in VALID_STYLES:
        if normalized == style:
            return style
    return None


def normalize_level(value):
    normalized = normalize_input(value)
    for level in VALID_LEVELS:
        if normalized == level:
            return level
    return None


def normalize_hall(value):
    normalized = normalize_input(value)
    for hall in VALID_HALLS:
        if normalized == hall:
            return hall
    return None


def normalize_group_name(value):
    normalized = normalize_input(value)
    if not (GROUP_NAME_MIN <= len(normalized) <= GROUP_NAME_MAX):
        return None
    if any(forbidden in normalized for forbidden in GROUP_NAME_FORBIDDEN):
        return None
    if not re.fullmatch(r"[a-z0-9]+(?:\s[a-z0-9]+)*", normalized):
        return None
    return normalized


def validate_group(data):
    errors = []
    name = normalize_group_name(data.get("name"))
    if name is None:
        errors.append(
            "Group name must be 2-60 characters, letters or digits only"
        )
    style = normalize_style(data.get("style"))
    if style is None:
        errors.append(
            f"Style must be one of: {', '.join(VALID_STYLES)}"
        )
    level = normalize_level(data.get("level"))
    if level is None:
        errors.append(
            f"Level must be one of: {', '.join(VALID_LEVELS)}"
        )
    hall = normalize_hall(data.get("hall"))
    if hall is None:
        errors.append(
            f"Hall must be one of: {', '.join(VALID_HALLS)}"
        )
    return {
        "name": name,
        "style": style,
        "level": level,
        "hall": hall,
    }, errors
