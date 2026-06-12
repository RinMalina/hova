# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: IdeaVault
def edit_idea(idea_id: int, updates: dict) -> bool:
    if idea_id not in ideas_db:
        print(f"Идея #{idea_id} не найдена.")
        return False
    
    current = ideas_db[idea_id]
    
    # Обновляем только предоставленные поля, сохраняя остальные (например, timestamp создания)
    for key, value in updates.items():
        if hasattr(current, key):  # Проверка на существование атрибута для классов или ключа в словаре
            setattr(current, key, value)
    
    print(f"Идея #{idea_id} успешно обновлена.")
    return True
