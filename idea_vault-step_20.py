# === Stage 20: Добавь восстановление записей из архива ===
# Project: IdeaVault
def restore_from_archive():
    """Восстанавливает записи из временного архива, если он существует."""
    archive_path = "idea_vault/archive.json"
    if not os.path.exists(archive_path):
        return 0
    with open(archive_path, "r", encoding="utf-8") as f:
        archived_ids = json.load(f)
    restored_count = 0
    for item_id in archived_ids:
        original = vault_db[item_id]
        if not any(item["id"] == item_id for item in vault_db.values()):
            insert_record(original, vault_db)
            restored_count += 1
    with open(archive_path, "w", encoding="utf-8") as f:
        json.dump([], f)
    return restored_count
