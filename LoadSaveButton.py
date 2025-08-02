import json
import os

CUSTOM_BUTTONS_FILE = 'CustomButtons.json'

def load_custom_buttons():
    """Загружает список кастомных кнопок из файла CustomButtons.json."""
    if not os.path.exists(CUSTOM_BUTTONS_FILE):
        return []
    try:
        with open(CUSTOM_BUTTONS_FILE, 'r', encoding='utf-8') as f:
            # Если файл пустой, загрузка выдаст ошибку
            if os.path.getsize(CUSTOM_BUTTONS_FILE) == 0:
                return []
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_custom_buttons(buttons):
    """Сохраняет список кастомных кнопок в файл CustomButtons.json."""
    try:
        with open(CUSTOM_BUTTONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(buttons, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении файла кастомных кнопок: {e}")

def add_custom_button(preset_data):
    """
    Добавляет новую кнопку-пресет в CustomButtons.json.
    Если пресет с таким же именем уже существует, он будет обновлен.
    """
    presets = load_custom_buttons()
    preset_name = preset_data.get("name")

    # Ищем существующий пресет по имени
    for i, existing_preset in enumerate(presets):
        if existing_preset.get("name") == preset_name:
            presets[i] = preset_data  # Обновляем
            break
    else:
        # Если не нашли, добавляем новый
        presets.append(preset_data)

    save_custom_buttons(presets)
