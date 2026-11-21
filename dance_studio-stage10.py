# === Stage 10: Поиск по нескольким словам ===
# Project: DanceStudio
from collections.abc import Iterable


def _is_valid_token(token: str) -> bool:
    if not token:
        return False
    for char in token:
        if char in "-_":
            return False
    return True


def _split_query(query: str) -> list[str]:
    tokens = query.split()
    return [token for token in tokens if _is_valid_token(token)]


def search_group(
    group: "Group",
    query: str,
    *,
    include_prefix: str = "-",
    exclude_prefix: str = "-",
) -> bool:
    tokens = _split_query(query)
    if not tokens:
        return True

    positive_tokens: list[str] = []
    negative_tokens: set[str] = set()

    for token in tokens:
        prefix = token[: len(include_prefix)]
        if prefix == include_prefix:
            negative_tokens.add(token[len(prefix):].strip())
        elif prefix == exclude_prefix:
            negative_tokens.add(token[len(exclude_prefix):].strip())
        else:
            positive_tokens.append(token)

    if not positive_tokens:
        return True

    positive_tokens = [token.lower() for token in positive_tokens]
    negative_tokens = [token.lower() for token in negative_tokens]

    fields: Iterable[str] = (
        group.name,
        group.style,
        group.level,
        group.hall.name if group.hall is not None else "",
    )

    for field in fields:
        lowered_field = field.lower()
        for token in positive_tokens:
            if token not in lowered_field:
                return False
        for token in negative_tokens:
            if token in lowered_field:
                return False

    return True
