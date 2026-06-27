# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: IdeaVault
def search_ideas(query: str, fields: list[str] = None) -> list[dict]:
    if not query or not fields:
        return []
    query_lower = query.lower()
    results = []
    for idea in ideas_db.values():
        match_found = False
        for field_name in fields:
            value_str = str(idea.get(field_name, '')).lower()
            if query_lower in value_str:
                match_found = True
                break
        if match_found:
            results.append(idea)
    return results
