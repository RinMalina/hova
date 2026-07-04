# === Stage 17: Добавь группировку записей по категориям ===
# Project: IdeaVault
def group_by_category(records):
    groups = {}
    for rec in records:
        cat = rec.get('category', 'Uncategorized')
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(rec)
    return list(groups.items())
