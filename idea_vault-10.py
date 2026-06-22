# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: IdeaVault
def export_to_json():
    import json
    data = {
        "ideas": [
            {"id": i["id"], "title": i["title"], "category_id": i.get("category_id"), "rating": i.get("rating", 0), "connections": i.get("connections", []), "implementation_plan": i.get("implementation_plan")}
            for i in ideas_list
        ],
        "categories": [
            {"id": c["id"], "name": c["name"]}
            for c in categories_list
        ]
    }
    return json.dumps(data, ensure_ascii=False)

# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: IdeaVault
def export_to_json():
    import json
    from datetime import datetime
    
    def serialize(obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        raise TypeError(f"Unsupported type: {type(obj)}")
    
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "categories": [serialize(c) for c in categories],
        "ideas": [serialize(i) for i in ideas]
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
