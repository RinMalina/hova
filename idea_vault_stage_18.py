# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: IdeaVault
class TagManager:
    def __init__(self):
        self.tags = {}  # id -> {name, ideas}

    def add_tag(self, name, idea_ids=None):
        if not name.strip():
            raise ValueError("Tag name cannot be empty")
        tag_id = f"tag_{len(self.tags) + 1}"
        entry = {"id": tag_id, "name": name, "ideas": set()}
        if idea_ids:
            entry["ideas"] = set(idea_ids)
        self.tags[tag_id] = entry
        return tag_id

    def remove_tag(self, tag_id):
        removed = self.tags.pop(tag_id, None)
        if removed is None:
            raise KeyError(f"Tag {tag_id} not found")
        # detach from ideas
        for iid in list(removed.get("ideas", set())):
            try:
                self.tags[iid]["tags"].discard(tag_id)
            except (KeyError, AttributeError):
                pass
        return removed

    def get_tag(self, tag_id):
        return self.tags.get(tag_id)

    def list_tags(self):
        return [t for t in self.tags.values() if isinstance(t, dict)]

    def attach_tag_to_idea(self, idea_id, tag_id):
        try:
            idea = self.tags[idea_id]
        except KeyError:
            raise KeyError(f"Idea {idea_id} not found")
        if tag_id not in idea.get("tags", set()):
            idea.setdefault("tags", set()).add(tag_id)
