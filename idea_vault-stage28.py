# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: IdeaVault
def project_metrics():
    categories = vault.categories() if hasattr(vault, 'categories') else []
    ideas = vault.ideas() if hasattr(vault, 'ideas') else []
    connections = vault.connections() if hasattr(vault, 'connections') else []
    
    total_ideas = len(ideas)
    total_categories = len(categories)
    total_connections = len(connections)

    implemented_count = 0
    planned_count = 0
    rejected_count = 0
    for idea in ideas:
        status = idea.get('status', 'planned') if isinstance(idea, dict) else getattr(idea, 'status', 'planned')
        if status == 'implemented': implemented_count += 1
        elif status == 'rejected': rejected_count += 1
        else: planned_count += 1

    avg_rating = sum(idea.get('rating', 0) for idea in ideas if isinstance(idea, dict)) / max(total_ideas, 1)

    print(f"Total Ideas: {total_ideas}")
    print(f"Total Categories: {total_categories}")
    print(f"Total Connections: {total_connections}")
    print(f"Ideas by Status - Implemented: {implemented_count}, Planned: {planned_count}, Rejected: {rejected_count}")
    print(f"Avg Rating: {avg_rating:.2f}")

project_metrics()
