# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: IdeaVault
def sort_ideas(criteria='date', reverse=False):
    if criteria == 'date':
        return sorted(idea_list, key=lambda x: x.get('created_at', ''), reverse=reverse)
    elif criteria == 'priority':
        return sorted(idea_list, key=lambda x: int(x.get('priority', 0)), reverse=True)
    elif criteria == 'name':
        return sorted(idea_list, key=lambda x: x.get('title', '').lower())
    else:
        raise ValueError(f"Неизвестный критерий сортировки: {criteria}")
