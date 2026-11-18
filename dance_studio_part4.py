# === Stage 4: Редактирование записей ===
# Project: DanceStudio
ALLOWED_GROUP_FIELDS = ("name", "style", "level", "hall")

VALID_STYLES = ("jazz", "hiphop", "contemporary", "latin", "ballet")

VALID_LEVELS = ("beginner", "intermediate", "advanced")


def can_edit_group_field(field_name):
    return field_name in ALLOWED_GROUP_FIELDS


def validate_group_style(style):
    return style in VALID_STYLES


def validate_group_level(level):
    return level in VALID_LEVELS


def edit_group(group, field_name, new_value):
    if field_name not in ALLOWED_GROUP_FIELDS:
        raise ValueError(f"Cannot edit unknown field: {field_name}")
    if field_name == "style":
        if not validate_group_style(new_value):
            raise ValueError(f"Invalid style: {new_value}")
    elif field_name == "level":
        if not validate_group_level(new_value):
            raise ValueError(f"Invalid level: {new_value}")
    setattr(group, field_name, new_value)
    return group
