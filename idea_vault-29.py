# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: IdeaVault
def get_config():
    config = {
        "app_name": "IdeaVault",
        "version": 29,
        "max_ideas_per_category": 100,
        "default_priority": 3,
        "priority_levels": ["Low", "Medium", "High", "Critical"],
        "min_rating": 1,
        "max_rating": 5,
        "allowed_categories": [
            "Programming", "Design", "Marketing", "Business"
        ],
        "features": {
            "categories": True,
            "ratings": True,
            "connections": True,
            "implementation_plan": True
        },
        "connection_types": ["depends_on", "related_to", "blocks", "extends"]
    }
    return config


def validate_config(config):
    errors = []
    if not isinstance(config.get("max_ideas_per_category"), int) or config["max_ideas_per_category"] < 1:
        errors.append("max_ideas_per_category must be a positive integer")
    if not all(isinstance(x, str) for x in config.get("allowed_categories", [])):
        errors.append("allowed_categories must contain only strings")
    if config.get("min_rating") > config.get("max_rating"):
        errors.append("min_rating cannot exceed max_rating")
    return errors


def load_config_from_env():
    env_overrides = {}
    for key in ["APP_NAME", "VERSION", "MAX_IDEAS_PER_CATEGORY"]:
        val = __import__("os").environ.get(key)
        if val is not None:
            try:
                env_overrides[key.lower().replace("_", "_")] = int(val)
            except ValueError:
                env_overrides[key.lower()] = val
    return env_overrides


def apply_env_overrides(config, overrides):
    for key, value in overrides.items():
        if isinstance(value, str) and "." not in key:
            config[key] = value
        elif isinstance(value, int):
            config[key] = value
    return config
