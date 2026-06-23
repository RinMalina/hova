# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: IdeaVault
import json, os

DATA_FILE = "ideavault_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[ERROR] Не удалось сохранить данные в {DATA_FILE}: {e}")

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"ideas": [], "categories": {}, "connections": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстановление структуры по умолчанию, если файл повреждён или устарел
        if not isinstance(data.get("ideas"), list):
            return {"ideas": [], "categories": {}, "connections": []}
        return data
    except (json.JSONDecodeError, IOError):
        print("[WARN] Файл данных повреждён. Создан новый.")
        return {"ideas": [], "categories": {}, "connections": []}

def init_data_store():
    """Инициализация хранилища и загрузка существующих данных."""
    global ideas, categories, connections
    data = load_state()
    ideas = data.get("ideas", [])
    categories = data.get("categories", {})
    connections = data.get("connections", [])

def persist_data():
    """Сохранение текущего состояния всех сущностей в JSON-файл."""
    save_state({"ideas": ideas, "categories": categories, "connections": connections})
