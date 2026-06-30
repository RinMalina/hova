# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: IdeaVault
def calculate_weekly_stats(data: list[dict], start_date: str) -> dict[str, int]:
    from datetime import datetime, timedelta
    
    stats = {}
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    
    while True:
        week_start = (current_date - timedelta(days=current_date.weekday())).date()
        week_end = week_start + timedelta(weeks=1) - timedelta(days=1)
        
        stats[week_start.strftime("%Y-%w")] = {
            "ideas": 0,
            "evaluations": 0,
            "categories": set(),
            "connections": 0
        }
        
        next_date = week_end + timedelta(days=1)
        if current_date >= datetime.strptime(next_date.strftime("%Y-%m-%d"), "%Y-%m-%d"):
            break
        
        for item in data:
            date_str = item.get("created_at", "")
            try:
                item_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if week_start <= item_date <= week_end:
                    stats[week_start.strftime("%Y-%w")]["ideas"] += 1
                    stats[week_start.strftime("%Y-%w")]["evaluations"] += len(item.get("evaluations", []))
                    for cat in item.get("categories", []):
                        stats[week_start.strftime("%Y-%w")]["categories"].add(cat)
                    stats[week_start.strftime("%Y-%w")]["connections"] += len(item.get("connections", []))
            except ValueError:
                continue
    
    return {k: v for k, v in sorted(stats.items())}
