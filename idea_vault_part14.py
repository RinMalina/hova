# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: IdeaVault
def generate_summary():
    if not ideas: return "Нет идей."
    stats = {"total": len(ideas), "avg_score": sum(i.score for i in ideas) / max(len(ideas), 1)}
    categories = set()
    links_count = 0
    plans_count = 0
    for idea in ideas:
        if idea.category: categories.add(idea.category)
        if idea.links: links_count += len(idea.links)
        if idea.plans: plans_count += len(idea.plans)
    return f"Идей: {stats['total']}, Средний рейтинг: {stats['avg_score']:.1f}, Категории: {len(categories)}, Ссылки: {links_count}, Планы: {plans_count}"
