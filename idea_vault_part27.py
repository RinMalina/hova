# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: IdeaVault
def reset_demo_data():
    """Сбросить все данные в дефолтные значения."""
    global vault, categories, idea_counter, next_idea_id
    
    vault = {
        "ideas": [
            {"id": 1, "title": "Идея #1", "description": "Описание идеи #1", 
             "category": "Разработка", "priority": 3, "votes": 0, "status": "active"},
            {"id": 2, "title": "Идея #2", "description": "Описание идеи #2", 
             "category": "Дизайн", "priority": 5, "votes": 1, "status": "review"}
        ],
        "categories": [
            {"id": 1, "name": "Разработка"},
            {"id": 2, "name": "Дизайн"},
            {"id": 3, "name": "Маркетинг"},
            {"id": 4, "name": "Продажи"}
        ],
        "connections": [
            {"from_id": 1, "to_id": 2}
        ]
    }
    
    categories = [
        {"id": 1, "name": "Разработка"},
        {"id": 2, "name": "Дизайн"},
        {"id": 3, "name": "Маркетинг"},
        {"id": 4, "name": "Продажи"}
    ]
    
    idea_counter = 100
    next_idea_id = 1
    
    print("✅ Демо-данные сброшены успешно!")

def clear_all_data():
    """Полная очистка всех данных."""
    global vault, categories, idea_counter, next_idea_id
    
    vault = {}
    categories = []
    idea_counter = 0
    next_idea_id = 1
    
    print("🧹 Все данные полностью очищены!")

def reset_and_clear():
    """Сброс демо-данных + полная очистка."""
    global vault, categories, idea_counter, next_idea_id
    
    vault = {}
    categories = []
    idea_counter = 0
    next_idea_id = 1
    
    print("💥 Полная перезагрузка: все данные сброшены и очищены!")

# Примеры использования
if __name__ == "__main__":
    reset_demo_data()
    # clear_all_data()  # Раскомментируйте для полной очистки
