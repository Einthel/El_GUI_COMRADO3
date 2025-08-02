import webbrowser
import subprocess
import keyboard
import os
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

class ButtonActions:
    def __init__(self, main_window):
        """
        Инициализирует обработчик действий кнопок.
        :param main_window: Экземпляр главного окна (MainWindow) для доступа к его элементам.
        """
        self.main_window = main_window
        self.audio_volume = self.get_audio_volume_interface()

    def get_audio_volume_interface(self):
        """Получает интерфейс для управления громкостью звука."""
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            return cast(interface, POINTER(IAudioEndpointVolume))
        except Exception as e:
            print(f"Не удалось получить доступ к устройствам звука: {e}")
            return None

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
        if self.audio_volume:
            current_volume = self.audio_volume.GetMasterVolumeLevelScalar()
            new_volume = min(1.0, current_volume + 0.1)
            self.audio_volume.SetMasterVolumeLevelScalar(new_volume, None)
            print(f"Sound Up: {new_volume:.2f}")

    def sound_down(self):
        if self.audio_volume:
            current_volume = self.audio_volume.GetMasterVolumeLevelScalar()
            new_volume = max(0.0, current_volume - 0.1)
            self.audio_volume.SetMasterVolumeLevelScalar(new_volume, None)
            print(f"Sound Down: {new_volume:.2f}")

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
