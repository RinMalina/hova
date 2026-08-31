# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: IdeaVault
def dry_run(operation, payload, *, dry=True):
    """Execute `operation` only if `dry` is False; otherwise return a dry-run report."""
    if not dry:
        return operation(payload)
    report = {
        "mode": "dry-run",
        "operation": operation.__name__,
        "payload": payload,
        "result": None,
        "error": None,
    }
    try:
        result = operation(payload)
        report["result"] = result
    except Exception as exc:
        report["error"] = f"{type(exc).__name__}: {exc}"
    return report
