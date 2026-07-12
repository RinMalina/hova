# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: IdeaVault
def add_reminders(ideas_db: dict) -> None:
    """Добавляет напоминания к идеям, у которых есть дата выполнения."""
    reminders = {}  # id_идеи -> {id_напоминания, текст, дата}
    for i, idea in ideas_db.items():
        if 'date' in idea:
            date_str = str(idea['date'])
            reminder_text = f"Напоминание по идее #{i}: выполнить до {date_str}"
            reminders[i] = {
                'id': len(reminders) + 1,
                'text': reminder_text,
                'due_date': date_str,
            }
    ideas_db['reminders'] = reminders
    return ideas_db

# Пример использования:
# ideas_db = {"idea_1": {"title": "Улучшить интерфейс", "date": "2024-12-31"}, ...}
# add_reminders(ideas_db)
