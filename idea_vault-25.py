# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: IdeaVault
def parse_date_safe(value):
    if not isinstance(value, str) or not value.strip():
        return None
    for fmt in ("%Y-%m-%d", "%d.%m.%y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value.strip(), fmt).date()
        except ValueError:
            continue
    return None

def format_date(date_obj):
    if date_obj is None:
        return "не указана"
    return date_obj.strftime("%d.%m.%y")
