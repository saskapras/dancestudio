# === Stage 12: Постраничный вывод ===
# Project: DanceStudio
"""Pagination helper for the DanceStudio group list.

Provides the data structures and functions to page through the list of
dance groups, given a page number and a page size.
"""

from collections import namedtuple


Page = namedtuple("Page", ["groups", "page", "page_size", "total", "total_pages"])


def paginate_groups(groups, page=1, page_size=10):
    """Return a Page for the requested slice of the group list.

    Args:
        groups: an iterable of group records.
        page: one-based page number.
        page_size: number of groups to return per page.

    Returns:
        A Page namedtuple with the requested groups, the current page
        number, the page size, the total number of groups, and the total
        number of pages available.
    """
    page = max(1, page)
    page_size = max(1, page_size)
    total = len(groups)
    total_pages = (total + page_size - 1) // page_size
    total_pages = max(1, total_pages)
    start = (page - 1) * page_size
    end = start + page_size
    page_groups = list(groups)[start:end]
    return Page(page_groups, page, page_size, total, total_pages)


def has_next_page(page):
    """Return True if the given page has a following page."""
    return page < page.total_pages


def has_prev_page(page):
    """Return True if the given page has a preceding page."""
    return page.page > 1


def next_page(page):
    """Return the following Page, or None if already on the last page."""
    if has_next_page(page):
        return paginate_groups(page.groups, page.page + 1, page.page_size)
    return None


def prev_page(page):
    """Return the preceding Page, or None if already on the first page."""
    if has_prev_page(page):
        return paginate_groups(page.groups, page.page - 1, page.page_size)
    return None
