# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: IdeaVault
import json, random, os

def suggest_next_action(vault):
    if not vault.get("ideas"): return "Добавить первую идею"
    ideas = vault["ideas"]
    scored = sorted(ideas.items(), key=lambda x: (x[1].get("votes",0), x[1].get("importance", 5)), reverse=True)
    top3 = [i for i, _ in scored[:3]]
    if not top3: return "Оценить идеи и назначить приоритеты"
    
    ideas_by_cat = {}
    for id_, d in ideas.items():
        cat = d.get("category", "general")
        ideas_by_cat.setdefault(cat, []).append(id_)
    
    suggestions = []
    if any(len(v) > 1 for v in ideas_by_cat.values()):
        suggestions.append("Создать ветку реализации для наиболее популярной категории")
    
    high_imp = [id_ for id_, d in scored if d.get("importance", 5) >= 7]
    if len(high_imp) < 3:
        suggestions.append(f"Повысить важность идей (текущих {len(high_imp)} из 3)")
    
    linked = sum(1 for _, d in ideas.items() if d.get("related_to"))
    if linked == 0 and any(i.get("has_plan") for i, _ in scored):
        suggestions.append("Связать идеи через поле related_to для группировки проектов")
    
    random.shuffle(suggestions)
    return suggestions[0] if suggestions else "Уточнить критерии оценки идей"

if __name__ == "__main__":
    vault = {}
    with open("idea_vault.json", "r", encoding="utf-8") as f:
        vault = json.load(f)
    
    suggestion = suggest_next_action(vault)
    print(f"\n🔮 Следующее действие: {suggestion}")
