# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: IdeaVault
def integrity_check(data):
    """Проверяет базовую целостность данных IdeaVault."""
    issues = []
    if not isinstance(data, dict):
        return ["Данные не являются словарём"]
    
    for key in ['vault', 'categories']:
        if key not in data:
            issues.append(f"Отсутствует ключ '{key}'")
            continue
    
    vault = data.get('vault', {})
    cats = data.get('categories', {})
    
    # Проверка идей в хранилище
    for idx, idea in enumerate(vault.get('ideas', [])):
        if not isinstance(idea, dict):
            issues.append(f"Идея {idx} не является словарём")
            continue
        
        required_keys = ['id', 'title', 'category']
        for rk in required_keys:
            if rk not in idea:
                issues.append(f"Идея {idea.get('id')} пропущена ключ '{rk}'")
        
        # Проверка, что ID категории существует в списке категорий
        cat_id = idea.get('category')
        if cat_id is not None and isinstance(cat_id, int):
            valid_cats = set(cats.keys()) if isinstance(cats, dict) else []
            if cat_id not in valid_cats:
                issues.append(f"Идея {idea['id']} ссылается на несуществующую категорию {cat_id}")
    
    # Проверка связей
    for idx, link in enumerate(vault.get('links', [])):
        if not isinstance(link, dict):
            issues.append(f"Связь {idx} не является словарём")
            continue
        
        src = link.get('source')
        dst = link.get('destination')
        if src is None or dst is None:
            issues.append(f"Связь {link.get('id')} пропущена ключ 'source' или 'destination'")
    
    return issues

def repair_data(data):
    """Исправляет простые проблемы в данных IdeaVault."""
    repaired = dict.copy(data)
    
    # Восстановление структуры vault, если она была повреждена
    if not isinstance(repaired.get('vault'), dict):
        repaired['vault'] = {}
    
    ideas = repaired['vault'].get('ideas', [])
    links = repaired['vault'].get('links', [])
    
    for idea in ideas:
        if not isinstance(idea, dict) or 'id' not in idea:
            continue
        
        # Восстановление missing keys
        if 'title' not in idea:
            idea['title'] = f"Без названия (ID {idea['id']})"
        
        if 'category' not in idea and isinstance(idea.get('id'), int):
            idea['category'] = 0
        
        # Восстановление связей
        for link in links:
            if not isinstance(link, dict) or 'source' not in link or 'destination' not in link:
                continue
            
            src_id = link.get('source')
            dst_id = link.get('destination')
            
            if isinstance(src_id, int):
                matching_ideas = [i for i in ideas if i.get('id') == src_id]
                if not matching_ideas and 'id' in link:
                    # Если источник не найден, удаляем связь (запись о несуществующей)
                    repaired['vault']['links'].remove(link)
    
    return repaired
