# constants.py

"""
A central repository for constant values used across the application.
This helps prevent typos and makes maintenance easier.
"""

# --- Configuration Keys Prefixes ---
PAGE_PREFIX = "page_"
BUTTON_PREFIX = "toolButton_"
EDITOR_BUTTON_PREFIX = "Edit_toolButton_"

# --- Dictionary Keys for Button Configuration ---
KEY_ICON_PATH = "icon_path"
KEY_SIGN = "sign"
KEY_FONT = "font"
KEY_FONT_SIZE = "font_size"
KEY_ACTION = "action"
KEY_NAME = "name" # For presets

# --- Dictionary Keys for Action Configuration ---
KEY_ACTION_TYPE = "type"
KEY_ACTION_VALUE = "value"

# --- Action Types ---
ACTION_TYPE_METHOD = "method"
ACTION_TYPE_PROGRAM = "program"
ACTION_TYPE_SHORTCUT = "shortcut"
ACTION_TYPE_EMPTY = ""

# --- Widget Related ---
KEY_WIDGET_TYPE = "widget_type"
KEY_WIDGET_SETTINGS = "settings"
KEY_WIDGET_POSITION = "position"

# --- Built-in Method Actions ---
# This dictionary maps user-facing names to internal method names.
METHOD_ACTIONS = {
    "Открыть браузер": "open_browser",
    "Открыть калькулятор": "open_calculator",
    "Открыть блокнот": "open_notepad",
    "Громкость +": "sound_up",
    "Громкость -": "sound_down",
    "Продолжить воспроизведение": "media_play_pause",
    "Поставить на паузу": "media_play_pause",
    "Следующая страница": "next_page",
    "Предыдущая страница": "previous_page"
}

# A reversed version for quick lookups (method name -> user-facing name)
REVERSED_METHOD_ACTIONS = {v: k for k, v in METHOD_ACTIONS.items()}

# --- UI and Miscellaneous ---
SAFE_FONTS = [
    "Arial", "Arial Black", "Calibri", "Cambria", "Candara", "Comic Sans MS",
    "Consolas", "Constantia", "Corbel", "Courier New", "Georgia", "Impact",
    "Lucida Console", "Lucida Sans Unicode", "Microsoft Sans Serif",
    "Palatino Linotype", "Segoe UI", "Tahoma", "Times New Roman", "Trebuchet MS",
    "Verdana"
]
