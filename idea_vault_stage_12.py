# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: IdeaVault
import json, os

def load_from_file(file_path: str) -> list[dict]:
    if not file_path or not isinstance(file_path, str):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("Ошибка: JSON должен содержать массив идей.")
                return []
            for i, item in enumerate(data):
                if not isinstance(item, dict):
                    print(f"Предупреждение: Элемент {i} не является объектом и будет пропущен.")
                    continue
                # Базовая валидация структуры (пример)
                if 'id' not in item or 'title' not in item:
                    print(f"Ошибка: Элемент {i} отсутствует обязательные поля id или title.")
            return data
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
