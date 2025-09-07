import os
import subprocess
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QPoint, QTimer, QTime, QDateTime
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from utils import compile_ui_files


# --- Логика виджетов ---

class DraggableWidget(QWidget):
    """
    Базовый класс для всех виджетов, которые можно перетаскивать внутри родителя.
    """
    def __init__(self, ui_class, parent=None):
        super().__init__(parent)
        self.drag_position = None
        self._is_draggable = True # Флаг для контроля возможности перетаскивания

        # Инициализируем UI, переданный из дочернего класса
        self.ui = ui_class()
        self.ui.setupUi(self)

    def setDraggable(self, draggable):
        """Включает или выключает возможность перетаскивания."""
        self._is_draggable = draggable

    def mousePressEvent(self, event):
        """Вызывается при нажатии кнопки мыши."""
        if event.button() == Qt.MouseButton.LeftButton and self._is_draggable:
            # Запоминаем смещение курсора относительно левого верхнего угла виджета
            self.drag_position = event.position().toPoint()
            event.accept()

    def mouseMoveEvent(self, event):
        """Вызывается при движении мыши с зажатой кнопкой."""
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None and self._is_draggable:
            # Новая позиция = глобальная позиция курсора - смещение
            # mapToParent преобразует координаты из системы виджета в систему родителя
            new_pos = self.mapToParent(event.position().toPoint() - self.drag_position)
            self.move(new_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Вызывается при отпускании кнопки мыши."""
        self.drag_position = None
        event.accept()

class ClockWidget(DraggableWidget):
    def __init__(self, parent=None, settings=None):
        from resource.Bar_widget.ui_Clock_widget import Ui_Clock_widget
        super().__init__(Ui_Clock_widget, parent)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint
        )

        self.apply_settings(settings)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def apply_settings(self, settings):
        """Применяет настройки к виджету часов."""
        if settings is None:
            settings = {}

        # Настройки по умолчанию
        font_size = settings.get("font_size", 12)
        font_weight = settings.get("font_weight", "normal")
        alignment_str = settings.get("alignment", "center")
        
        # Установка выравнивания
        alignment_map = {
            "left": Qt.AlignLeft | Qt.AlignVCenter,
            "center": Qt.AlignCenter,
            "right": Qt.AlignRight | Qt.AlignVCenter,
        }
        alignment = alignment_map.get(alignment_str.lower(), Qt.AlignCenter)
        self.ui.Clock_timeLabel.setAlignment(alignment)

        # Установка стилей шрифта
        self.ui.Clock_timeLabel.setStyleSheet(f"""
            font-size: {font_size}pt;
            font-weight: {font_weight};
            padding-right: 5px;
        """)

    def update_time(self):
        """Обновляет время на виджете."""
        current_time = QTime.currentTime()
        time_text = current_time.toString("HH:mm:ss")
        self.ui.Clock_timeLabel.setText(time_text)

class VolumeWidget(DraggableWidget):
    def __init__(self, parent=None, settings=None):
        from resource.Bar_widget.ui_Volume_widget import Ui_Volume_widget
        super().__init__(Ui_Volume_widget, parent)

        self.audio_interface = None
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            self.audio_interface = cast(interface, POINTER(IAudioEndpointVolume))
        except Exception as e:
            print(f"Ошибка инициализации pycaw: {e}")
            self.ui.Volume_LevelLabel.setText("Error")

        self.update_volume()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_volume)
        self.timer.start(1000) # Обновление раз в секунду

    def update_volume(self):
        if not self.audio_interface:
            return
            
        try:
            volume_level = self.audio_interface.GetMasterVolumeLevelScalar()
            volume_percent = int(volume_level * 100)
            self.ui.Volume_LevelLabel.setText(f"{volume_percent}%")
        except Exception as e:
            print(f"Ошибка при получении громкости: {e}")
            self.ui.Volume_LevelLabel.setText("N/A")



class MusicWidget(DraggableWidget):
    def __init__(self, parent=None, settings=None):
        # Импортируем и передаем класс UI в родительский конструктор
        from resource.Bar_widget.ui_Music_widget import Ui_Music_widget
        super().__init__(Ui_Music_widget, parent)
        
        # Аналогично можно задать флаги, если потребуется
        # self.setWindowFlags(...)
        
        # Здесь может быть будущая логика именно для MusicWidget, использующая settings


class TestWidget(DraggableWidget):
    def __init__(self, parent=None, settings=None):
        # Импортируем и передаем класс UI в родительский конструктор
        from resource.Bar_widget.ui_Test_widget import Ui_test_widget
        super().__init__(Ui_test_widget, parent)


class TimerWidget(DraggableWidget):
    """Виджет таймера с обратным отсчётом и диалогом выбора длительности."""
    def __init__(self, parent=None, settings=None):
        from resource.Bar_widget.ui_Timer_widget import Ui_Timer_widget
        super().__init__(Ui_Timer_widget, parent)

        self._end_time: QDateTime | None = None
        self._tick_timer: QTimer = QTimer(self)
        self._tick_timer.setInterval(250)
        self._tick_timer.timeout.connect(self._update_countdown)
        self._dialog_is_open: bool = False

        # Привязки кнопок
        self.ui.Timer_button.clicked.connect(self._handle_timer_button_click)

        # Инициализация отображения
        self.ui.Timer_label.setText("")
        # Базовый стиль для лейбла таймера
        self._base_label_style = "color: white;"
        self.ui.Timer_label.setStyleSheet(self._base_label_style)

    # --- Публичные методы ---
    def start_countdown(self, minutes: int) -> None:
        if minutes is None or minutes <= 0:
            return
        self._end_time = QDateTime.currentDateTime().addSecs(int(minutes) * 60)
        if not self._tick_timer.isActive():
            self._tick_timer.start()
        self._update_countdown()  # мгновенное обновление
        self.ui.Timer_button.setText("Stop")
        self._set_label_emphasis(False)

    def stop_countdown(self) -> None:
        self._tick_timer.stop()
        self._end_time = None
        self.ui.Timer_label.setText("00:00")
        self.ui.Timer_button.setText("Timer")
        self._set_label_emphasis(False)

    # --- Вспомогательные методы ---
    def _handle_timer_button_click(self) -> None:
        """Обрабатывает нажатие на кнопку: запускает таймер или останавливает его."""
        # Если таймер активен, останавливаем его
        if self._tick_timer.isActive():
            self.stop_countdown()
            return

        # Если таймер неактивен, открываем диалог выбора времени
        from PySide6.QtWidgets import QDialog
        from resource.Bar_widget.ui_timer_dialog_window import Ui_Time_dialog

        if self._dialog_is_open:
            return
        self._dialog_is_open = True
        try:
            dialog = QDialog(self)
            ui = Ui_Time_dialog()
            ui.setupUi(dialog)

            selected_minutes: dict[str, int] = {"value": 0}

            def choose(minutes: int):
                selected_minutes["value"] = minutes
                dialog.accept()

            ui.Timer_buton_1.clicked.connect(lambda: choose(1))
            ui.Timer_buton_2.clicked.connect(lambda: choose(2))
            ui.Timer_buton_3.clicked.connect(lambda: choose(3))
            ui.Timer_buton_4.clicked.connect(lambda: choose(5))
            ui.Timer_buton_5.clicked.connect(lambda: choose(10))
            ui.Timer_buton_6.clicked.connect(lambda: choose(15))

            if dialog.exec() == QDialog.DialogCode.Accepted and selected_minutes["value"] > 0:
                self.start_countdown(selected_minutes["value"])
        finally:
            self._dialog_is_open = False

    def _update_countdown(self) -> None:
        if self._end_time is None:
            return
        now = QDateTime.currentDateTime()
        remaining_ms = now.msecsTo(self._end_time)
        if remaining_ms <= 0:
            self.ui.Timer_label.setText("00:00")
            self._tick_timer.stop()
            self._end_time = None
            self.ui.Timer_button.setText("Timer")
            try:
                QApplication.beep()
            except Exception:
                pass
            # Короткое визуальное выделение по завершении
            self._set_label_emphasis(True)
            QTimer.singleShot(1200, lambda: self._set_label_emphasis(False))
            return

        total_seconds = remaining_ms // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        self.ui.Timer_label.setText(f"{int(minutes):02d}:{int(seconds):02d}")
        # Подсветка, когда осталось <= 5 секунд
        self._set_label_emphasis(total_seconds <= 5)

    def _set_label_emphasis(self, highlight: bool) -> None:
        if highlight:
            self.ui.Timer_label.setStyleSheet("color: #ff5555; font-weight: bold;")
        else:
            self.ui.Timer_label.setStyleSheet(self._base_label_style)


if __name__ == "__main__":
    # --- Шаг 1: Компиляция ---
    print("Запуск скрипта компиляции UI файлов...")
    target_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resource", "Bar_widget")
    compile_ui_files(target_folder)
    print("\nКомпиляция завершена.")
    
    # --- Шаг 2: Тестовый запуск виджетов ---
    print("Запуск тестового окна...")
    app = QApplication(sys.argv)
    
    # Создаем контейнер для теста
    test_container = QWidget()
    test_container.setWindowTitle("Тестовый контейнер для виджетов")
    test_container.setFixedSize(600, 400)
    
    # Создаем и размещаем виджеты внутри контейнера
    clock = ClockWidget(test_container)
    clock.move(50, 50)
    # Сбрасываем флаги, чтобы он был дочерним в тесте
    clock.setWindowFlags(Qt.Widget) 

    volume = VolumeWidget(test_container)
    volume.move(300, 150)
    volume.setWindowFlags(Qt.Widget)

    music = MusicWidget(test_container)
    music.move(50, 250)
    music.setWindowFlags(Qt.Widget)

    timerw = TimerWidget(test_container)
    timerw.move(300, 50)
    timerw.setWindowFlags(Qt.Widget)

    test_container.show()
    
    # Показываем виджеты, так как они теперь дочерние
    clock.show()
    volume.show()
    music.show()
    timerw.show()

    sys.exit(app.exec())
