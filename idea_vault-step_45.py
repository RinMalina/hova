# === Stage 45: Добавь восстановление из резервной копии ===
# Project: IdeaVault
import base64, json, os

def save_backup(data, filename="backup.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_backup(filename="backup.json"):
    if not os.path.exists(filename):
        print(f"Резервная копия '{filename}' не найдена.")
        return None
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# Пример использования:
# backup = save_backup({"ideas": [101, 102, 103], "categories": ["tech", "design"]})
# restored = load_backup()
# if restored:
#     print(f"Восстановлено {len(restored.get('ideas', []))} идей.")
