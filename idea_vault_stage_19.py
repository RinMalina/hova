# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: IdeaVault
def archive_ideas(idea_data, age_days=365, completed=True):
    """Archive old or completed ideas from the vault.

    idea_data: dict with keys 'id', 'title', 'content', 'created_date' (str date),
               'completed' (bool). Returns new record if archived and original otherwise.
    """
    import datetime

    now = datetime.datetime.now()
    created = datetime.datetime.strptime(idea_data['created_date'], '%Y-%m-%d')
    age = (now - created).days

    is_old = (age > age_days) or idea_data.get('completed', False)
    if is_old:
        return {
            **idea_data,
            'status': 'archived' if not idea_data['status'] else idea_data['status'],
            'archive_date': now.strftime('%Y-%m-%d'),
        }
    return idea_data
