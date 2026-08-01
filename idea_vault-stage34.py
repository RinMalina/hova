# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: IdeaVault
TEMPLATE_TYPES = {
    'idea': {'fields': ['title', 'description'], 'extra': {}},
    'feature': {'fields': ['title', 'description', 'priority'], 'extra': {'type': 'feature'}},
    'bug':   {'fields': ['title', 'description'], 'extra': {'type': 'bug'}},
}

def create_from_template(template_name, vault=None):
    if template_name not in TEMPLATE_TYPES:
        print(f"Unknown template: {template_name}")
        return None
    fields = TEMPLATE_TYPES[template_name]['fields']
    extra = TEMPLATE_TYPES[template_name].get('extra', {})
    data = {}
    for key in fields:
        value = input(f"Enter {key} for {template_name}: ")
        data[key] = value
    if 'type' in extra:
        data['type'] = extra['type']
    return Idea(data)
