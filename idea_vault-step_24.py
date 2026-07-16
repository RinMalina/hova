# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: IdeaVault
def print_record(record):
    """Компактный вывод одной записи: ID, статус, оценка, категория, связи."""
    if not record:
        return "Нет данных"
    
    fields = []
    for key in ["id", "status", "score", "category", "relations"]:
        val = record.get(key)
        if val is not None:
            fields.append(f"{key}: {val}")
    
    # Добавляем дополнительные поля, если они есть
    extras = [k for k in record.keys() if k not in ["id", "status", "score", "category", "relations"]]
    for key in extras:
        val = record.get(key)
        if val is not None and isinstance(val, str):
            fields.append(f"{key}: {val}")
    
    print(" ─── Запись #" + str(record["id"]) + " ───")
    print(" | " + " | ".join(fields))
