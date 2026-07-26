# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: IdeaVault
class UserProfile:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role
        self.ideas = []

    def add_idea(self, idea):
        if idea.owner is None:
            idea.owner = self
        self.ideas.append(idea)

    def __repr__(self):
        return f"UserProfile(name={self.name!r}, role={self.role!r})"


class IdeaVaultApp:
    _profiles = {}
    _current_profile = None

    @classmethod
    def create_profile(cls, name="default", role="user"):
        profile = UserProfile(name, role)
        cls._profiles[name] = profile
        cls._current_profile = profile
        return profile

    @classmethod
    def switch_to(cls, name):
        if name not in cls._profiles:
            raise ValueError(f"Profile '{name}' does not exist")
        cls._current_profile = cls._profiles[name]

    @classmethod
    def get_current(cls):
        return cls._current_profile

    @classmethod
    def list_profiles(cls):
        return dict(cls._profiles)

    _ideas = []

    def add_idea(self, title, body="", category=None, score=0.5):
        idea = Idea(title=title, body=body, owner=self.get_current(), category=category, score=score)
        self._ideas.append(idea)
        if category is not None:
            CategoryStore.add(category, idea)
        return idea

    def get_idea(self, index):
        return self._ideas[index]

    def get_all(self):
        return list(self._ideas)

    @classmethod
    def reset(cls):
        cls._profiles = {}
        cls._current_profile = None
        cls._ideas = []


IdeaVaultApp.create_profile("default")
