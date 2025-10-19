from audio_manager import audioSwitch as switcher
from pycaw.pycaw import AudioUtilities
from audio_manager.audioController import getMasterVolume, setMasterVolume

def get_all_devices():
    """Возвращает список имен всех активных устройств вывода звука."""
    try:
        # Используем правильный метод getAllDevices из MyAudioUtilities
        devices = switcher.MyAudioUtilities.getAllDevices("output")
        return list(devices.keys())
    except Exception as e:
        print(f"Ошибка при получении списка аудиоустройств: {e}")
        return []

def get_current_device():
    """Возвращает имя текущего аудиоустройства по умолчанию."""
    try:
        # Используем стандартный метод GetSpeakers() из pycaw для получения устройства по умолчанию
        speakers_device = AudioUtilities.GetSpeakers()
        # "Распаковываем" COM-объект, чтобы получить доступ к его свойствам, таким как FriendlyName
        return AudioUtilities.CreateDevice(speakers_device).FriendlyName
    except Exception as e:
        print(f"Ошибка при получении текущего устройства: {e}")
        return None

def set_device(device_name: str):
    """
    Устанавливает устройство с указанным именем как устройство по умолчанию.

    :param device_name: Точное имя устройства, как оно отображается в системе.
    :return: True в случае успеха, False в случае ошибки.
    """
    try:
        # Получаем словарь {имя: id} всех устройств
        all_devices = switcher.MyAudioUtilities.getAllDevices("output")
        device_id = all_devices.get(device_name)

        if not device_id:
            print(f"Аудиоустройство с именем '{device_name}' не найдено.")
            return False

        # Устанавливаем устройство по умолчанию для всех ролей для надежности
        switcher.switchOutput(device_id, switcher.pc.ERole.eConsole)
        switcher.switchOutput(device_id, switcher.pc.ERole.eMultimedia)
        switcher.switchOutput(device_id, switcher.pc.ERole.eCommunications)
        
        print(f"Аудиоустройство переключено на: {device_name}")
        return True
    except Exception as e:
        print(f"Не удалось переключить аудиоустройство на '{device_name}': {e}")
        return False

def toggle_devices(primary_device: str, secondary_device: str):
    """
    Переключает звук между двумя указанными устройствами.

    Если активно основное устройство, переключает на вторичное.
    В противном случае (если активно вторичное или любое другое) — переключает на основное.

    :param primary_device: Имя основного устройства.
    :param secondary_device: Имя вторичного устройства.
    :return: Имя нового активного устройства или None в случае ошибки.
    """
    current = get_current_device()
    if not current:
        print("Не удалось определить текущее устройство. Переключение невозможно.")
        return None

    print(f"Текущее устройство: {current}")
    
    if current == primary_device:
        target_device = secondary_device
    else:
        target_device = primary_device
    
    if set_device(target_device):
        return target_device
    
    return None

def sound_up():
    """Увеличивает системную громкость на 10%."""
    try:
        current_volume = getMasterVolume()
        new_volume = min(100, current_volume + 10)
        setMasterVolume(new_volume)
        print(f"Sound Up: {new_volume}%")
    except Exception as e:
        print(f"Ошибка при увеличении громкости: {e}")

def sound_down():
    """Уменьшает системную громкость на 10%."""
    try:
        current_volume = getMasterVolume()
        new_volume = max(0, current_volume - 10)
        setMasterVolume(new_volume)
        print(f"Sound Down: {new_volume}%")
    except Exception as e:
        print(f"Ошибка при уменьшении громкости: {e}")


if __name__ == '__main__':
    # Этот блок для быстрой проверки и отладки.
    # Он покажет все ваши устройства и попробует переключиться.
    print("Доступные устройства вывода звука:")
    all_devices = get_all_devices()
    if all_devices:
        for i, device in enumerate(all_devices):
            print(f"{i + 1}. {device}")
    else:
        print("Не найдено ни одного активного устройства вывода.")

    print("-" * 20)
    current_dev = get_current_device()
    if current_dev:
        print(f"Текущее устройство по умолчанию: {current_dev}")
    else:
        print("Не удалось определить текущее устройство по умолчанию.")
    print("-" * 20)

    # --- Пример использования toggle_devices ---
    # !!!ВАЖНО!!! Замените эти имена на реальные имена ваших устройств из списка выше.
    # main_device = "Динамики (Realtek High Definition Audio)"
    # second_device = "Наушники (Arctis 5 Game)"
    #
    # print(f"Переключение между '{main_device}' и '{second_device}'...")
    # new_device = toggle_devices(main_device, second_device)
    # if new_device:
    #     print(f"Успешно переключено на: {new_device}")
    # else:
    #     print("Переключение не удалось.")
