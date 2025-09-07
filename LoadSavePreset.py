import json
import os
import constants

CUSTOM_BUTTONS_FILE = 'CustomButtons.json'

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
