import sys
import os

# --- Настройка путей для корректной работы из папки src ---
# 1. Получаем абсолютный путь к текущему файлу (main.py)
current_file_path = os.path.abspath(__file__)
# 2. Поднимаемся на один уровень вверх, чтобы получить путь к папке src/
src_dir = os.path.dirname(current_file_path)
# 3. Поднимаемся еще на один уровень, чтобы получить корневую папку проекта
project_root = os.path.dirname(src_dir)
# 3.1. Формируем путь к папке с библиотеками
libs_dir = os.path.join(project_root, 'libs')

# 4. Добавляем все необходимые папки в sys.path
sys.path.insert(0, project_root)
sys.path.insert(0, src_dir)
sys.path.insert(0, libs_dir)
# -------------------------------------------------------------

import subprocess
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QFrame, QToolButton, QSizePolicy,
    QVBoxLayout
)
from PySide6.QtCore import Qt, QRect, QSize, QEvent
from PySide6.QtGui import QIcon
import warnings

# Импорты для виджетов бара - добавляем сюда
from Music_player import MusicPlayer
# Убираем старый импорт, так как compile_ui_files_recursively будет вызвана в __main__
# from utils import compile_ui_files 
import icons_rc

def compile_ui_files_recursively_local_import(start_dir, output_dir):
    """
    Локальная версия функции, чтобы избежать проблем с импортом subprocess до main.
    """
    import subprocess
    if not os.path.isdir(start_dir):
        print(f"Ошибка: Директория '{start_dir}' не найдена.")
        sys.exit(1)

    for root, _, files in os.walk(start_dir):
        for ui_file in files:
            if not ui_file.endswith(".ui"):
                continue

            ui_path = os.path.join(root, ui_file)
            
            # Генерируем имя .py файла (например, comrado3.ui -> ui_comrado3.py)
            # или resource/Bar_widget/Clock_widget.ui -> resource/Bar_widget/ui_Clock_widget.py
            base_name = os.path.splitext(ui_file)[0]
            py_file_name = f"ui_{base_name}.py"
            py_path = os.path.join(root, py_file_name)

            # Перекомпилируем, если .py файл отсутствует или .ui файл новее
            if not os.path.exists(py_path) or os.path.getmtime(ui_path) > os.path.getmtime(py_path):
                print(f"Обнаружены изменения в '{ui_path}'. Компиляция в '{py_path}'...")
                try:
                    subprocess.run(['pyside6-uic', ui_path, '-o', py_path], check=True)
                    print("Компиляция прошла успешно.")
                except (subprocess.CalledProcessError, FileNotFoundError) as e:
                    print(f"Ошибка: Не удалось скомпилировать '{ui_path}'.")
                    print(f"Подробности: {e}")
                    print("Убедитесь, что 'pyside6-tools' установлены и доступны в системном PATH.")
                    sys.exit(1)

# Импортируем сгенерированные классы и обработчик действий уже ПОСЛЕ компиляции
# (Это объявление будет выполнено после блока if __name__ == '__main__')
# Но для ясности лучше оставить их здесь, а реальный импорт сделать после компиляции
# Однако Python выполняет импорты до основного кода, поэтому мы оставим это как есть,
# но будем помнить, что компиляция должна произойти до инициализации MainWindow.

# --- Переносим импорты, зависимые от UI, внутрь __main__ ---
# from ui_comrado3 import Ui_MainWindow
# from comrado3 import ActionHandler
# from LoadSave import load_config
# from editor import EditorWindow
# from utils import get_window_title_from_ui, resource_path

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("SettingsWindow") # Добавляем имя объекта для QSS
        self.setWindowTitle("Настройки")
        self.setGeometry(200, 200, 500, 300)
        # self.setStyleSheet("background-color: #2b2b2b; color: white;") # Убираем инлайновый стиль

        layout = QGridLayout(self)
        label = QLabel("Здесь будут настройки приложения.")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Сохраняем исходные флаги окна при инициализации
        self._is_overlay_mode = False
        self._original_flags = self.windowFlags()

        self.setAttribute(Qt.WA_AcceptTouchEvents)

        self.config = load_config()

        # self.setWindowTitle("El GUI COMRADO 5.1.2") # Удаляем эту строку

        self.settings_window = None
        self.editor_window = None
        self.music_player_window = None

        # Перестраиваем страницы при запуске, чтобы UI соответствовал конфигу
        self.rebuild_pages()

        # Создаем экземпляр обработчика действий и передаем ему себя
        self.action_handler = ActionHandler(self)
        self.action_handler.setup_pages_and_controls()

        # Подключаем кнопку к слоту
        self.ui.Music_bttn.clicked.connect(self.open_music_player)


    def closeEvent(self, event):
        """
        Перехватывает событие закрытия окна для корректного завершения
        фоновых потоков.
        """
        print("Запрос на закрытие приложения. Завершение фоновых потоков...")
        
        # 1. Даем команду на остановку цикла мониторинга
        if hasattr(self, 'action_handler') and hasattr(self.action_handler, 'hw_reader'):
            self.action_handler.hw_reader.stop()
        
        # 2. Завершаем поток и ждем его полной остановки
        if hasattr(self, 'action_handler') and hasattr(self.action_handler, 'hw_thread'):
            self.action_handler.hw_thread.quit()
            # Ожидаем до 5 секунд, чтобы избежать вечного зависания
            if not self.action_handler.hw_thread.wait(5000):
                print("ВНИМАНИЕ: Поток мониторинга не завершился вовремя. Возможно принудительное завершение.")

        print("Фоновые потоки завершены. Приложение закрывается.")
        
        # 3. Разрешаем закрытие окна
        super().closeEvent(event)


    def open_music_player(self):
        """
        ВРЕМЕННАЯ ФУНКЦИЯ ДЛЯ ДЕБАГА И ТЕСТА!
        Открывает окно музыкального плеера.
        В будущем будет заменен на вызов через систему виджетов/плагинов.
        """
        if self.music_player_window is None or not self.music_player_window.isVisible():
            self.music_player_window = MusicPlayer()
            self.music_player_window.show()

    def toggle_overlay_mode(self):
        """Переключает режим окна между обычным и полноэкранным."""
        self._is_overlay_mode = not self._is_overlay_mode

        if self._is_overlay_mode:
            print("Переключение в полноэкранный режим.")
            # Отключаем кнопки
            self.ui.Editor_button.setEnabled(False)
            # Устанавливаем кнопку в "нажатое" состояние
            self.ui.Change_Button.setChecked(True)
            # Показываем окно в полноэкранном режиме
            self.showFullScreen()
        else:
            print("Переключение в обычный режим.")
            # Включаем кнопки
            self.ui.Editor_button.setEnabled(True)
            # Возвращаем кнопку в обычное состояние
            self.ui.Change_Button.setChecked(False)
            # Возвращаем обычный размер окна
            self.showNormal()

    def event(self, event):
        """Перехватывает события, чтобы обработать касания."""
        if event.type() == QEvent.Type.TouchBegin:
            # Проверяем, есть ли точки касания
            if not event.points():
                return super().event(event)

            # Получаем первую точку касания
            touch_point = event.points()[0]
            
            # Находим виджет (кнопку) под точкой касания
            widget = self.childAt(touch_point.position().toPoint())
            
            # Проверяем, что это одна из наших кнопок ToolButton
            if isinstance(widget, QToolButton) and "ToolButton" in widget.objectName():
                # Вызываем наш универсальный обработчик
                self.action_handler.handle_button_action(widget)
                return True # Сообщаем, что событие обработано

        # Для всех остальных событий вызываем стандартный обработчик
        return super().event(event)

    def resizeEvent(self, event):
        """Перехватывает событие изменения размера окна для обновления иконок."""
        super().resizeEvent(event)
        self.update_icon_sizes()

    def show_editor_window(self):
        """Открывает модальное окно редактора."""
        if self.editor_window is None or not self.editor_window.isVisible():
            self.editor_window = EditorWindow()
            self.editor_window.setWindowModality(Qt.ApplicationModal) # Блокирует все окна
            # Подключаем сигнал к слоту для обновления кнопок
            self.editor_window.config_saved.connect(self.update_buttons)
            self.editor_window.show()

    def update_icon_sizes(self):
        """Обновляет размеры иконок кнопок на текущей видимой странице."""
        current_page = self.ui.Button_stackedWidget.currentWidget()
        if not current_page:
            return

        buttons = current_page.findChildren(QToolButton)
        for button in buttons:
            # Оставляем небольшой отступ (padding) вокруг иконки
            padding = 15
            # Рассчитываем размер иконки, чтобы она была чуть меньше кнопки
            icon_w = button.width() - padding
            icon_h = button.height() - padding
            
            # Используем меньшую из сторон, чтобы иконка была квадратной и вписывалась
            new_size = max(0, min(icon_w, icon_h)) 
            
            button.setIconSize(QSize(new_size, new_size))

    def update_buttons(self):
        """Перезагружает конфиг, перестраивает страницы и обновляет кнопки в главном окне."""
        print("Обновление кнопок и страниц после сохранения в редакторе...")
        self.config = load_config()
        self.rebuild_pages()
        # Полностью пересоздаем обработчик, чтобы гарантировать сброс его состояния
        self.action_handler = ActionHandler(self)
        self.action_handler.setup_pages_and_controls()

    def rebuild_pages(self):
        """Полностью перестраивает страницы в QStackedWidget на основе текущего конфига."""
        # Очищаем старые страницы
        while self.ui.Button_stackedWidget.count() > 0:
            widget = self.ui.Button_stackedWidget.widget(0)
            self.ui.Button_stackedWidget.removeWidget(widget)
            widget.deleteLater()

        # Получаем отсортированные ключи страниц
        page_keys = sorted(
            [key for key in self.config if key.startswith("page_")],
            key=lambda k: int(k.split('_')[1])
        )
        
        # Если страниц нет, создаем одну пустую для отображения
        if not page_keys:
            page_keys = ["page_1"]

        for page_key in page_keys:
            # Создаем ВНЕШНИЙ виджет-контейнер для тени
            page_widget = QWidget()
            page_widget.setObjectName(page_key)
            
            # Создаем компоновку для внешнего виджета, чтобы внутренний фрейм его заполнил
            container_layout = QVBoxLayout(page_widget)
            container_layout.setContentsMargins(10, 10, 10, 10) # Отступы для тени

            # Создаем ВНУТРЕННИЙ фрейм для фона и скругления
            page_container = QFrame()
            page_container.setObjectName("page_container") # Имя для QSS
            container_layout.addWidget(page_container)

            # Создаем сеточную компоновку уже для ВНУТРЕННЕГО фрейма
            grid_layout = QGridLayout(page_container)
            grid_layout.setSpacing(15) # Расстояние между кнопками
            
            # Создаем 12 кнопок и добавляем их в сетку 3x4
            button_index = 0
            for row in range(3):
                for col in range(4):
                    if button_index >= 12:
                        break
                    
                    button = QToolButton()
                    # Имя объекта теперь включает номер от 1 до 12
                    button.setObjectName(f"ToolButton_{button_index + 1:02d}")
                    
                    # Устанавливаем политику размеров, чтобы кнопка могла растягиваться
                    button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    
                    button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                    button.setCheckable(False)
                    button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
                    
                    # Добавляем кнопку в ячейку сетки
                    grid_layout.addWidget(button, row, col)
                    
                    button_index += 1
            
            self.ui.Button_stackedWidget.addWidget(page_widget)


    def show_settings_window(self):
        """Открывает окно настроек."""
        if self.settings_window is None or not self.settings_window.isVisible():
            self.settings_window = SettingsWindow()
            self.settings_window.show()


if __name__ == "__main__":
    # Импортируем утилиты здесь, после настройки пути
    from utils import compile_ui_files_recursively, get_window_title_from_ui, resource_path

    # Определяем пути для компиляции
    # Используем PROJECT_ROOT из utils, чтобы не дублировать логику
    from utils import PROJECT_ROOT
    ui_files_dir = os.path.join(PROJECT_ROOT, 'resources', 'ui')
    output_py_dir = os.path.join(PROJECT_ROOT, 'src')

    # Вызываем рекурсивную компиляцию для всего проекта ПЕРЕД импортами
    compile_ui_files_recursively(ui_files_dir, output_py_dir)
    
    # Теперь, когда все скомпилировано, можно безопасно импортировать модули,
    # которые зависят от сгенерированных файлов.
    from ui_comrado3 import Ui_MainWindow
    from comrado3 import ActionHandler
    from LoadSave import load_config
    from editor import EditorWindow

    app = QApplication(sys.argv)
    
    # --- ЗАГРУЗКА СТИЛЕЙ ИЗ ФАЙЛА ---
    try:
        style_path = resource_path("resources/styles/Style.qss")
        with open(style_path, "r", encoding="utf-8") as f:
            style = f.read()
        app.setStyleSheet(style)  
        print("Стили из Style.qss успешно загружены.")
    except FileNotFoundError:
        print("ПРЕДУПРЕЖДЕНИЕ: Файл Style.qss не найден. Приложение будет использовать стандартный стиль.")
    except Exception as e:
        print(f"Произошла ошибка при загрузке стилей: {e}")
    # ------------------------------------

    # --- Получаем заголовок окна из .ui файла ---
    ui_path = resource_path("resources/ui/comrado3.ui")
    window_title = get_window_title_from_ui(ui_path) or "El GUI COMRADO"

    # --- Запуск основного окна ---
    window = MainWindow()
    window.setWindowTitle(window_title) # Устанавливаем динамически загруженный заголовок

    # --- Убрана логика для автоматического позиционирования ---
    # Теперь окно всегда запускается в обычном режиме.
    window.show()
    # --------------------------------------------------------------------------
    
    sys.exit(app.exec())
