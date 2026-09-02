# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: IdeaVault
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "reverse": "\033[7m",
    "hidden": "\033[8m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}

def colorize(text, color):
    if not color:
        return text
    return ANSI[color] + text + ANSI["reset"]

def log(msg, color="white"):
    print(colorize(msg, color))

def success(msg):
    return colorize(msg, "green")

def error(msg):
    return colorize(msg, "red")

def warning(msg):
    return colorize(msg, "yellow")

def info(msg):
    return colorize(msg, "cyan")

def debug(msg):
    return colorize(msg, "dim")

def print_header(title):
    return colorize(f"\n{ANSI['bold']}{ANSI['bright_white']}{'═'*40}", "white") + " " + colorize(f" {title} ", ANSI["bold"]) + f"{'═'*40}\n"

def print_subheader(title):
    return colorize(f"\n{ANSI['underline']}{title}{ANSI['reset']}\n", ANSI["cyan"])

def print_separator():
    return colorize("-" * 50, ANSI["bright_black"])
