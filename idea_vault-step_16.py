# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: IdeaVault
def generate_monthly_stats(records, start_date=None):
    if not records:
        return {}
    
    from datetime import date
    
    today = date.today()
    months = []
    for year in range(today.year - 10, today.year + 2):
        month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
                       "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        for m in range(1, 13):
            months.append((year, m))
    
    stats = {str(m): {"count": 0, "avg_rating": None} for _, m in months}
    
    def parse_date_str(d_str):
        try:
            return date.fromisoformat(d_str)
        except ValueError:
            parts = d_str.split("-")
            if len(parts) == 3:
                return date(int(parts[0]), int(parts[1]), int(parts[2]))
            return None
    
    for rec in records:
        created_date = parse_date_str(rec.get("created_at", ""))
        if not created_date:
            continue
        
        key = f"{created_date.year}-{created_date.month:02d}"
        if key in stats:
            stats[key]["count"] += 1
            rating = rec.get("rating")
            if rating is not None and isinstance(rating, (int, float)):
                current_sum = stats[key].get("_sum_rating", 0) + rating
                stats[key]["_sum_rating"] = current_sum
    
    for key in stats:
        data = stats[key]
        count = data["count"]
        if "_sum_rating" in data and count > 0:
            data["avg_rating"] = round(data["_sum_rating"] / count, 2)
        del data["_sum_rating"]
    
    return stats
