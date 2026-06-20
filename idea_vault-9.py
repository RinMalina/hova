# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: IdeaVault
def load_initial_data(json_string):
    import json
    from datetime import datetime
    
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None, None
    
    if not isinstance(data, dict):
        print("Неверный формат начальных данных")
        return None, None
    
    categories = data.get('categories', [])
    
    ideas_data = data.get('ideas', [])
    ideas = []
    for idea in ideas_data:
        try:
            created_at = datetime.fromisoformat(idea['created_at']) if 'created_at' in idea else datetime.now()
            new_idea = {
                **idea,
                'id': idea.get('id'),
                'title': idea.get('title', ''),
                'description': idea.get('description', ''),
                'category_id': idea.get('category_id'),
                'score': int(idea.get('score', 0)),
                'status': idea.get('status', 'draft'),
                'created_at': created_at,
                'updated_at': datetime.now()
            }
            ideas.append(new_idea)
        except (KeyError, ValueError) as e:
            print(f"Ошибка обработки идеи {idea}: {e}")
    
    if not categories and not ideas:
        return None, None
    
    return {
        'categories': categories,
        'ideas': ideas,
        'metadata': data.get('metadata', {})
    }, json_string
