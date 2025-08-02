import sys
import os
import subprocess
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QFrame, QToolButton
)
from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtGui import QIcon

# Импортируем наши сгенерированные классы и обработчик действий
from ui_comrado3 import Ui_MainWindow
from ui_Editor import Ui_Editor_Window
from comrado3 import ActionHandler
from LoadSave import load_config
from editor import EditorWindow





def compile_ui_files(ui_files):
    """Проверяет и компилирует список .ui файлов, если это необходимо."""
    for ui_file in ui_files:
        # Генерируем имя .py файла из имени .ui файла (например, comrado3.ui -> ui_comrado3.py)
        py_file = f"ui_{os.path.splitext(os.path.basename(ui_file))[0]}.py"

        if not os.path.exists(ui_file):
            print(f"Предупреждение: Файл {ui_file} не найден.")
            continue

        # Перекомпилируем, если .py файл отсутствует или .ui файл новее
        if not os.path.exists(py_file) or os.path.getmtime(ui_file) > os.path.getmtime(py_file):
            print(f"Обнаружены изменения в '{ui_file}'. Компиляция в '{py_file}'...")
            try:
                subprocess.run(['pyside6-uic', ui_file, '-o', py_file], check=True)
                print("Компиляция прошла успешно.")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"Ошибка: Не удалось скомпилировать '{ui_file}'.")
                print("Убедитесь, что 'pyside6-tools' установлены и доступны в системном PATH.")
                sys.exit(1)


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки")
        self.setGeometry(200, 200, 500, 300)
        self.setStyleSheet("background-color: #2b2b2b; color: white;")

        layout = QGridLayout(self)
        label = QLabel("Здесь будут настройки приложения.")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.config = load_config()

        self.setWindowTitle("El GUI COMRADO")

        self.settings_window = None
        self.editor_window = None

        # Перестраиваем страницы при запуске, чтобы UI соответствовал конфигу
        self.rebuild_pages()

        # Создаем экземпляр обработчика действий и передаем ему себя
        self.action_handler = ActionHandler(self)
        self.action_handler.setup_pages_and_controls()

    def show_editor_window(self):
        """Открывает модальное окно редактора."""
        if self.editor_window is None or not self.editor_window.isVisible():
            self.editor_window = EditorWindow()
            self.editor_window.setWindowModality(Qt.ApplicationModal) # Блокирует все окна
            # Подключаем сигнал к слоту для обновления кнопок
            self.editor_window.config_saved.connect(self.update_buttons)
            self.editor_window.show()

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

        # Точные координаты для кнопок из файла ui_comrado3.py
        button_geometries = [
            QRect(50, 20, 128, 128), QRect(220, 20, 128, 128),
            QRect(390, 20, 128, 128), QRect(560, 20, 128, 128),
            QRect(50, 160, 128, 128), QRect(220, 160, 128, 128),
            QRect(390, 160, 128, 128), QRect(560, 160, 128, 128),
            QRect(50, 300, 128, 128), QRect(220, 300, 128, 128),
            QRect(390, 300, 128, 128), QRect(560, 300, 128, 128)
        ]

        for page_key in page_keys:
            # Создаем виджет страницы
            page_widget = QWidget()
            page_widget.setObjectName(page_key)
            
            # Создаем фрейм для кнопок, используя точные размеры
            button_frame = QFrame(page_widget)
            button_frame.setObjectName(f"Button_frame_{page_key}")
            button_frame.setGeometry(QRect(10, 0, 730, 440))
            button_frame.setFrameShape(QFrame.Shape.StyledPanel)
            button_frame.setFrameShadow(QFrame.Shadow.Raised)

            # Создаем 12 кнопок на новой странице
            for i in range(1, 13):
                button = QToolButton(button_frame)
                button.setObjectName(f"ToolButton_{i:02d}")
                
                # Устанавливаем точную геометрию из списка
                button.setGeometry(button_geometries[i-1])
                
                button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                button.setIconSize(QSize(96, 96))
                button.setCheckable(False)
                button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            
            self.ui.Button_stackedWidget.addWidget(page_widget)


    def show_settings_window(self):
        """Открывает окно настроек."""
        if self.settings_window is None or not self.settings_window.isVisible():
            self.settings_window = SettingsWindow()
            self.settings_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Вызываем компиляцию здесь, чтобы она произошла до создания QApplication
    compile_ui_files(['comrado3.ui', 'Editor.ui'])
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 