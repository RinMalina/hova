# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: IdeaVault
import bisect
from dataclasses import field, replace
from typing import Optional

class IdeaVault:
    def __init__(self):
        self.ideas = []
        self.next_id = 1
        self.history = []  # stack of (action_type, target_index) for undo
        self._history_depth = 0
    
    def add_idea(self, title, description="", category="general", rating=5):
        idea = Idea(self.next_id, title, description, category, rating)
        self.ideas.append(idea)
        bisect.insort(self.index, (title, len(self.ideas)-1))
        self._history_depth += 1
        return idea
    
    def undo_last_edit(self):
        if not self.history:
            return False
        action_type, target_index = self.history.pop()
        if action_type == "add":
            del self.index[target_index]
            removed = self.ideas.pop(target_index)
            for i in range(len(self.ideas), 0, -1):
                bisect.insort(self.index, (self.ideas[i-1].title, target_index))
        elif action_type == "edit":
            target = self.ideas[target_index]
            target.title, target.description, target.category, target.rating = \
                target._saved_title, target._saved_description, target._saved_category, target._saved_rating
        return True
    
    def edit_idea(self, index, title=None, description=None, category=None, rating=None):
        if not (0 <= index < len(self.ideas)):
            return False
        idea = self.ideas[index]
        saved = (idea.title, idea.description, idea.category, idea.rating)
        idea._saved_title, idea._saved_description, idea._saved_category, idea._saved_rating = saved
        if title is not None: idea.title = title
        if description is not None: idea.description = description
        if category is not None: idea.category = category
        if rating is not None: idea.rating = rating
        
        old_title = (idea.title, index)
        self.index.remove(old_title)
        
        new_title = (idea.title, len(self.ideas)-1)
        bisect.insort(self.index, new_title)
        
        self._history_depth += 1
        return idea
    
    def get_indexed_ideas(self):
        result = []
        for title, idx in sorted(self.index):
            if idx < len(self.ideas):
                result.append(self.ideas[idx])
        return result
    
    @property
    def history_depth(self):
        return self._history_depth
    
    def get_history_summary(self):
        summary = {"total_undone": 0, "current_depth": self._history_depth}
        for action_type in reversed(self.history):
            if action_type == "add":
                summary["total_undone"] += 1
        return summary
    
    def get_stats(self):
        return {
            "total_ideas": len(self.ideas),
            "history_depth": self._history_depth,
            "history_summary": self.get_history_summary()
        }

# Пример использования отката последнего действия
if __name__ == "__main__":
    vault = IdeaVault()
    
    # Добавляем идеи
    idea1 = vault.add_idea("Создать API", "RESTful API для идей")
    idea2 = vault.add_idea("Добавить поиск", "Поиск по ключевым словам")
    
    print(f"Идеи: {vault.get_stats()['total_ideas']}")
    
    # Редактируем идею 1
    edited = vault.edit_idea(0, title="Создать REST API", description="RESTful API для идей с авторизацией")
    print(f"Редактированная идея: {edited.title}")
    
    # Откат последнего редактирования
    vault.undo_last_edit()
    print(f"После отката: {vault.get_stats()['total_ideas']} идеи, глубина истории: {vault.get_stats()['history_depth']}")
    
    # Добавляем еще одну идею и откатываем добавление
    idea3 = vault.add_idea("Оптимизация базы данных", "Использовать SQLite вместо PostgreSQL")
    print(f"Теперь идей: {vault.get_stats()['total_ideas']}")
    vault.undo_last_edit()
    
    # Проверка истории
    summary = vault.get_history_summary()
    print(f"Всего отменено операций: {summary['total_undone']}, текущая глубина: {summary['current_depth']}")
