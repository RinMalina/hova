# === Stage 43: Добавь пагинацию длинных списков ===
# Project: IdeaVault
def paginate(items, page=1, page_size=20):
    """Compact utility to paginate a list of items."""
    if not items:
        return {"items": [], "page": page, "page_size": page_size, "total": 0, "total_pages": 0}
    total = len(items)
    total_pages = (total + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = min(start + page_size, total)
    return {"items": items[start:end], "page": page, "page_size": page_size, "total": total, "total_pages": total_pages}
