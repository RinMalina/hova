# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: IdeaVault
def print_idea_table(ideas: list, cols=3) -> None:
    """Выводит идеи компактной таблицей в консоль."""
    if not ideas:
        print("Нет идей.")
        return
    max_t = 0
    for i in ideas:
        n = len(i.get('title', ''))
        if n > max_t:
            max_t = n
    max_t = min(max_t, 35)
    w_title = int(max_t * 1.4 + 2)
    w_score = max(8, len(str(ideas[0].get('score', ''))))
    w_cat = max(6, len(str(ideas[0].get('category', '').split('/')[-1] or 'N/A')))
    w_status = max(6, len(str(ideas[0].get('status', '').split()[0] or 'N/A')))
    header = f"{'ID':<4} {'Title':<{w_title}} {'Score':>{w_score}} {'Category':<{w_cat}} {'Status':<{w_status}}"
    print(header)
    print('-' * len(header))
    for i in ideas:
        row = f"{i['id']:<4}{i.get('title',''):<{w_title}}{str(i.get('score', 0)):>{w_score}}{str(i.get('category','')[-1] or 'N/A'):<{w_cat}}{str(i.get('status','').split()[0] or 'N/A'):<{w_status}}"
        print(row)
