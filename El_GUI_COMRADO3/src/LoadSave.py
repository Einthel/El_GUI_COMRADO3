import json
import os
import constants
from utils import PROJECT_ROOT # Импортируем путь к корню проекта

# Формируем абсолютные пути к файлам конфигурации
CONFIG_FILE = os.path.join(PROJECT_ROOT, 'configs', 'config.json')
CONFIG_BAR_FILE = os.path.join(PROJECT_ROOT, 'configs', 'config_bar.json')
CUSTOM_BUTTONS_FILE = os.path.join(PROJECT_ROOT, 'configs', 'CustomButtons.json')


def config_exists():
    """
    Проверяет, существует ли файл конфигурации.
    """
    return os.path.exists(CONFIG_FILE)

def save_config(data):
    """
    Сохраняет данные конфигурации в файл JSON.
    :param data: Словарь с данными для сохранения.
    """
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении файла конфигурации: {e}")

def load_config():
    """
    Загружает данные конфигурации из файла JSON.
    Если файл не существует, создает его со страницей по умолчанию.
    Также обрабатывает переход от старого формата (список pages) к новому (словари page_x).
    """
    import constants

    if not config_exists():
        # Создаем конфиг по умолчанию с одной пустой страницей
        default_config = {
            f"{constants.PAGE_PREFIX}1": {}
        }
        save_config(default_config)
        return default_config

    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # --- Миграция со старого формата ---
        if "pages" in config and isinstance(config["pages"], list):
            print("Обнаружен старый формат конфигурации. Выполняется миграция...")
            pages_list = config.pop("pages")
            for i, page_data in enumerate(pages_list):
                config[f"{constants.PAGE_PREFIX}{i+1}"] = page_data
            
            # После миграции можно сразу сохранить конфиг в новом формате
            save_config(config)
            print("Миграция завершена. Конфигурация сохранена в новом формате.")
        # --- Конец миграции ---

        # Если после миграции или при обычной загрузке нет ни одной страницы
        if not any(key.startswith(constants.PAGE_PREFIX) for key in config):
            config[f"{constants.PAGE_PREFIX}1"] = {}
            save_config(config)

        return config
    except (IOError, json.JSONDecodeError) as e:
        print(f"Ошибка при загрузке файла конфигурации: {e}")
        # Возвращаем базовый конфиг в случае серьезной ошибки
        return {f"{constants.PAGE_PREFIX}1": {}}

# --- Функции для конфигурации панели виджетов ---

def save_bar_config(data):
    """Сохраняет конфигурацию панели виджетов в файл config_bar.json."""
    try:
        with open(CONFIG_BAR_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении файла конфигурации панели: {e}")

def load_bar_config():
    """
    Загружает конфигурацию панели виджетов из файла config_bar.json.
    Если файл не существует или поврежден, создает и возвращает пустой словарь.
    """
    if not os.path.exists(CONFIG_BAR_FILE) or os.path.getsize(CONFIG_BAR_FILE) == 0:
        default_config = {}
        save_bar_config(default_config)
        return default_config

    try:
        with open(CONFIG_BAR_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Ошибка при загрузке или разборе файла {CONFIG_BAR_FILE}: {e}")
        # Создаем и возвращаем пустой конфиг в случае ошибки
        default_config = {}
        save_bar_config(default_config)
        return default_config

# --- Функции для конфигурации пресетов кнопок ---

def load_custom_buttons():
    """Загружает список кастомных кнопок (пресетов) из файла."""
    if not os.path.exists(CUSTOM_BUTTONS_FILE):
        return []
    
    try:
        with open(CUSTOM_BUTTONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Ошибка при загрузке файла пресетов: {e}")
        return []

def save_custom_buttons(presets):
    """Сохраняет список кастомных кнопок (пресетов) в файл."""
    try:
        with open(CUSTOM_BUTTONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(presets, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении файла пресетов: {e}")

def add_custom_button(new_preset):
    """
    Добавляет новый пресет в список. Если пресет с таким именем уже
    существует, он будет перезаписан.
    """
    presets = load_custom_buttons()
    preset_name = new_preset.get(constants.KEY_NAME)

    # Ищем существующий пресет и обновляем его, либо добавляем новый
    found = False
    for i, preset in enumerate(presets):
        if preset.get(constants.KEY_NAME) == preset_name:
            presets[i] = new_preset
            found = True
            break
    
    if not found:
        presets.append(new_preset)

    save_custom_buttons(presets)
