# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: IdeaVault
def backup_file(filepath: str, backup_dir: str = "backups") -> str:
    """Создаёт резервную копию файла с timestamp-именем."""
    import os
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, os.path.basename(filepath).replace(".", f".{ts}"))
    shutil.copy2(filepath, backup_path)
    return backup_path
