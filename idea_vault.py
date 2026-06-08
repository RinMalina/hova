# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: IdeaVault
import json
from datetime import datetime

# Базовая структура приложения IdeaVault (версия 0.1)
# Точка входа и демонстрационные данные

def init_vault():
    """Инициализация хранилища идей с демо-данными."""
    ideas = [
        {
            "id": 1,
            "title": "Мобильное приложение для учета привычек",
            "category": "Mobile App",
            "score": 8.5,
            "status": "idea",
            "created_at": datetime.now().isoformat(),
            "connections": []
        },
        {
            "id": 2,
            "title": "Автоматизация рутинных задач в Telegram",
            "category": "Automation",
            "score": 9.0,
            "status": "planning",
            "created_at": datetime.now().isoformat(),
            "connections": [1]
        }
    ]
    
    # Сохранение в файл (имитация базы данных)
    with open("ideavault_data.json", "w", encoding="utf-8") as f:
        json.dump({"ideas": ideas, "version": "0.1"}, f, ensure_ascii=False, indent=2)
    
    print(f"Инициализация IdeaVault v0.1 завершена. Демо-данные сохранены в ideavault_data.json")
    return ideas

if __name__ == "__main__":
    init_vault()
