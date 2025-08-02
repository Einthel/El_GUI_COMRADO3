import json
import os

CONFIG_FILE = 'config.json'

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
    if not config_exists():
        # Создаем конфиг по умолчанию с одной пустой страницей
        default_config = {
            "page_1": {}
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
                config[f"page_{i+1}"] = page_data
            
            # После миграции можно сразу сохранить конфиг в новом формате
            save_config(config)
            print("Миграция завершена. Конфигурация сохранена в новом формате.")
        # --- Конец миграции ---

        # Если после миграции или при обычной загрузке нет ни одной страницы
        if not any(key.startswith("page_") for key in config):
            config["page_1"] = {}
            save_config(config)

        return config
    except (IOError, json.JSONDecodeError) as e:
        print(f"Ошибка при загрузке файла конфигурации: {e}")
        # Возвращаем базовый конфиг в случае серьезной ошибки
        return {"page_1": {}}
