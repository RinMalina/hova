# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: IdeaVault
import json, os

def switch_profile(profile_file="profiles.json", active_key="active_profile"):
    if not os.path.exists(profile_file):
        return None
    
    with open(profile_file, 'r', encoding='utf-8') as f:
        profiles = json.load(f)
    
    def get_active():
        val = profiles.get(active_key, {}).get("value", "default")
        if val not in profiles["profiles"]:
            return None
        return profiles["profiles"][val]

    def set_active(name):
        if name not in profiles["profiles"]:
            return False
        profiles[active_key]["value"] = name
        with open(profile_file, 'w', encoding='utf-8') as f:
            json.dump(profiles, f, indent=2, ensure_ascii=False)
        return True

    def list_profiles():
        return {k: v.get("name", k) for k, v in profiles["profiles"].items()}

    active = get_active()
    if not active:
        return {"error": "no active profile"}
    
    return {
        "active": active,
        "list": list_profiles(),
        "switch": set_active
    }
