# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: IdeaVault
class IdeaVault:
    def __init__(self):
        self.ideas = {}
        self.categories = set()

    def add_idea(self, title, description, category=None, score=0):
        if not title or not description:
            raise ValueError("Заголовок и описание обязательны.")
        if category and category not in self.categories:
            self.categories.add(category)
        self.ideas[title] = {
            "description": description,
            "category": category,
            "score": score,
            "connections": []
        }

    def validate_input(self, title, description, category=None, score=0):
        if not isinstance(title, str) or not title.strip():
            return False, "Заголовок должен быть непустой строкой."
        if not isinstance(description, str) or not description.strip():
            return False, "Описание должно быть непустой строкой."
        if category is not None and (not isinstance(category, str) or not category.strip()):
            return False, "Категория должна быть непустой строкой или отсутствовать."
        if not isinstance(score, int) or score < 0:
            return False, "Оценка должна быть неотрицательным целым числом."
        return True, None

    def connect_ideas(self, idea1_title, idea2_title):
        if idea1_title in self.ideas and idea2_title in self.ideas:
            if idea2_title not in self.ideas[idea1_title]["connections"]:
                self.ideas[idea1_title]["connections"].append(idea2_title)
            return True
        return False, "Одна или обе идеи не найдены."

    def get_ideas_by_category(self, category):
        return [title for title, data in self.ideas.items() if data.get("category") == category]
