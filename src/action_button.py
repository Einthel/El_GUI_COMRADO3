import webbrowser
import subprocess
import keyboard
import os
import LoadSave
import control_audio # Импортируем наш новый модуль


class ButtonActions:
    def __init__(self, main_window, action_handler):
        """
        Инициализирует обработчик действий кнопок.
        :param main_window: Экземпляр главного окна (MainWindow) для доступа к его элементам.
        :param action_handler: Экземпляр ActionHandler для доступа к сигналам.
        """
        self.main_window = main_window
        self.action_handler = action_handler

    def open_browser(self):
        webbrowser.open("https://www.google.com")

    def open_calculator(self):
        subprocess.run(["calc"])

    def open_notepad(self):
        subprocess.run(["notepad"])

    def open_editor(self):
        # Вызываем метод главного окна для отображения редактора
        self.main_window.show_editor_window()

    def open_settings(self):
        # Вызываем метод главного окна для отображения настроек
        self.main_window.show_settings_window()
    
    def sound_up(self):
        """Вызывает функцию увеличения громкости из control_audio."""
        control_audio.sound_up()

    def sound_down(self):
        """Вызывает функцию уменьшения громкости из control_audio."""
        control_audio.sound_down()

    def media_play_pause(self):
        """Отправляет команду Play/Pause для управления медиа."""
        try:
            keyboard.send("play/pause media")
            print("Отправлена команда Play/Pause")
        except Exception as e:
            print(f"Ошибка при отправке команды Play/Pause: {e}")

    def run_program(self, path):
        """Запускает программу по указанному пути."""
        if not path or not os.path.exists(path):
            print(f"Ошибка: Файл не найден по пути: {path}")
            return
        try:
            os.startfile(path)
            print(f"Запуск программы: {path}")
        except OSError as e:
            print(f"Не удалось запустить программу '{path}': {e}")

    def send_shortcut(self, keys_string):
        """Отправляет сочетание клавиш."""
        try:
            if not isinstance(keys_string, str):
                print(f"Ошибка: ожидалась строка, но получен {type(keys_string)} ({keys_string})")
                return
            keyboard.send(keys_string.lower())
            print(f"Отправлено сочетание клавиш: {keys_string}")
        except Exception as e:
            print(f"Ошибка при отправке сочетания клавиш '{keys_string}': {e}")

    # === УПРАВЛЕНИЕ АУДИОУСТРОЙСТВАМИ ===

    def _get_audio_device_name(self, device_key: str):
        """
        Вспомогательный метод для получения имени аудиоустройства из config.json.
        :param device_key: Ключ устройства (напр., "main_device_id").
        :return: Имя устройства или None, если не найдено.
        """
        try:
            config = LoadSave.load_config()
            device_name = config.get("audio_settings", {}).get(device_key)
            if not device_name:
                print(f"Предупреждение: Аудиоустройство для ключа '{device_key}' не найдено в config.json.")
                return None
            return device_name
        except Exception as e:
            print(f"Ошибка при чтении конфигурации для аудиоустройства '{device_key}': {e}")
            return None

    def toggle_main_second_audio(self):
        """Переключает звук между основным и вторичным аудиоустройствами."""
        print("Действие: Переключить Main/Second аудио")
        main_device = self._get_audio_device_name("main_device_id")
        second_device = self._get_audio_device_name("second_device_id")

        if main_device and second_device:
            new_device = control_audio.toggle_devices(main_device, second_device)
            if new_device:
                self.action_handler.audio_device_changed.emit()
        else:
            print("Ошибка: Основное или второе аудиоустройство не настроено в config.json.")

    def set_main_audio_device(self):
        """Устанавливает основное аудиоустройство как устройство по умолчанию."""
        print("Действие: Установить Main аудио")
        device = self._get_audio_device_name("main_device_id")
        if device:
            if control_audio.set_device(device):
                self.action_handler.audio_device_changed.emit()

    def set_second_audio_device(self):
        """Устанавливает вторичное аудиоустройство как устройство по умолчанию."""
        print("Действие: Установить Second аудио")
        device = self._get_audio_device_name("second_device_id")
        if device:
            if control_audio.set_device(device):
                self.action_handler.audio_device_changed.emit()

    def set_third_audio_device(self):
        """Устанавливает третье аудиоустройство как устройство по умолчанию."""
        print("Действие: Установить Third аудио")
        device = self._get_audio_device_name("third_device_id")
        if device:
            if control_audio.set_device(device):
                self.action_handler.audio_device_changed.emit()

    def set_fourth_audio_device(self):
        """Устанавливает четвертое аудиоустройство как устройство по умолчанию."""
        print("Действие: Установить Fourth аудио")
        device = self._get_audio_device_name("fourth_device_id")
        if device:
            if control_audio.set_device(device):
                self.action_handler.audio_device_changed.emit()
