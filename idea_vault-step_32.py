# === Stage 32: Добавь журнал действий пользователя ===
# Project: IdeaVault
import datetime, json

class ActionLog:
    """Журнал действий пользователя (IDVAULT_ACTION_LOG)."""
    def __init__(self):
        self.actions = []
    
    def log(self, action_type, description, user_id=None):
        entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'action_type': action_type,
            'description': description,
            'user_id': user_id or 'anonymous'
        }
        self.actions.append(entry)
    
    def get_recent(self, count=10):
        return self.actions[-count:]
    
    @classmethod
    def from_json(cls, path='data/action_log.json'):
        if not os.path.exists(path):
            return cls()
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        log = cls()
        log.actions = [ActionLogEntry(**a) for a in data]
        return log
    
    def save(self, path='data/action_log.json'):
        os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.actions], f, ensure_ascii=False, indent=2)
