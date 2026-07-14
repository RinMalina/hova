# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: IdeaVault
def check_expired_reminders():
    """Проверяет просроченные напоминания и выводит предупреждения."""
    now = datetime.now()
    expired = []
    for idea in ideas:
        if idea.reminder_date and idea.reminder_date < now:
            expired.append(idea)
    return expired

def notify_expired_reminders():
    """Выводит сообщения о просроченных напоминаниях."""
    expired = check_expired_reminders()
    if not expired:
        print("Все напомнения актуальны.")
    else:
        for idea in expired:
            print(f"⚠️ Напоминание просрочено для идеи: {idea.title}")

# Пример использования в конце файла
if __name__ == "__main__":
    notify_expired_reminders()
