# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: IdeaVault
def filter_ideas(status=None, category=None, tags=None):
    filtered = []
    for idea in ideas:
        if status and idea.get('status') != status: continue
        if category and idea.get('category') != category: continue
        if tags:
            idea_tags = set(idea.get('tags', [])).union(set(idea.get('related_to_ids', [])))
            if not any(t in idea_tags for t in tags): continue
        filtered.append(idea)
    return filtered
