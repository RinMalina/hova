# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: IdeaVault
def run_cli_menu():
    print("=== IdeaVault CLI ===")
    while True:
        cmd = input("\nКоманда (1-5, q=выход): ").strip()
        if cmd == "q": break
        elif cmd in ("1", "2"): print(f"Действие {cmd}: функционал в разработке.")
        elif cmd == "3": print("Список идей: [пусто]")
        elif cmd == "4": print("Просмотр категорий: [пусто]")
        elif cmd == "5": print("Настройки интерфейса: шрифт 12, тема светлая")
        else: print("Неизвестная команда.")
