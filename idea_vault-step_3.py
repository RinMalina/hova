# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: IdeaVault
class IdeaVault:
    def __init__(self):
        self.ideas = []
        self.categories = {}

    def add_idea(self, title, description, category=None, score=0, linked_to=None):
        idea_id = len(self.ideas) + 1
        new_idea = {
            'id': idea_id,
            'title': title,
            'description': description,
            'category': category,
            'score': score,
            'linked_to': linked_to
        }
        self.ideas.append(new_idea)
        if category:
            if category not in self.categories:
                self.categories[category] = []
            self.categories[category].append(idea_id)
        return new_idea

    def add_category(self, name):
        if name not in self.categories:
            self.categories[name] = []
            return True
        return False
