# === Stage 9: Текстовый поиск ===
# Project: DanceStudio
def highlight_matches(text, pattern, highlight_char="*"):
    """Return text with every occurrence of the case-insensitive pattern
    wrapped in a pair of highlight characters. Matching is case-insensitive
    and every occurrence is replaced, even overlapping ones."""
    if not pattern:
        return text
    lowered = text.lower()
    pl = pattern.lower()
    if pl not in lowered:
        return text
    result = []
    start = 0
    index = 0
    while True:
        found = lowered.find(pl, start)
        if found == -1:
            break
        result.append(text[start:found])
        result.append(f"{highlight_char}{text[found:found + len(pl)]}{highlight_char}")
        start = found + 1
        index = found + 1
    result.append(text[start:])
    return "".join(result)


def search_groups_by_text(groups, query):
    """Search groups by any of their text fields (name, style, level, hall)
    case-insensitively. Returns a list of (group, highlighted_name) tuples
    where the group's name has the query highlighted. Matching is
    case-insensitive and every occurrence in the name is highlighted."""
    if not query:
        return []
    query_lower = query.lower()
    matches = []
    for group in groups:
        for field in ("name", "style", "level", "hall"):
            value = getattr(group, field)
            if value and query_lower in value.lower():
                highlighted = highlight_matches(value, query)
                matches.append((group, highlighted))
                break
    return matches


def format_search_result(match):
    """Format a single search match as a human-readable line."""
    group, highlighted_name = match
    style = getattr(group, "style", "")
    level = getattr(group, "level", "")
    hall = getattr(group, "hall", "")
    line = highlighted_name
    if style:
        line += f" | {style}"
    if level:
        line += f" | {level}"
    if hall:
        line += f" | {hall}"
    return line


def print_search_results(groups, query, max_results=10):
    """Print search results for the given query across all group text fields.
    The name is highlighted with the query. Results are limited to the first
    max_results matches."""
    matches = search_groups_by_text(groups, query)
    if query:
        print(f"Search for '{query}':")
    if not matches:
        print("No groups found.")
        return
    for index, match in enumerate(matches[:max_results], start=1):
        print(f"{index}. {format_search_result(match)}")
