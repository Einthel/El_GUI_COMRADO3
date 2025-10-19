# utils.py
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

# Глобальная переменная для хранения корневого пути проекта
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def resource_path(relative_path):
    """
    Возвращает абсолютный путь к ресурсу, работая как из исходников,
    так и из собранного PyInstaller приложения.
    """
    try:
        # PyInstaller создает временную папку и сохраняет путь в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Если запускается из обычного Python, используем путь к корню проекта
        base_path = PROJECT_ROOT
    
    return os.path.join(base_path, relative_path)

def apply_shadow(widget, blur_radius=25, x_offset=0, y_offset=0, color=(0, 0, 0, 160)):
    """
    Применяет стандартизированный эффект тени к виджету.
    :param widget: Виджет, к которому применяется тень.
    :param blur_radius: Радиус размытия тени.
    :param x_offset: Смещение тени по оси X.
    :param y_offset: Смещение тени по оси Y.
    :param color: Цвет тени в формате (R, G, B, A).
    """
    if widget and not widget.graphicsEffect():
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(blur_radius)
        shadow.setXOffset(x_offset)
        shadow.setYOffset(y_offset)
        shadow.setColor(QColor(*color))
        widget.setGraphicsEffect(shadow)

def get_window_title_from_ui(ui_path):
    """
    Извлекает заголовок окна (windowTitle) из указанного .ui файла.
    :param ui_path: Путь к .ui файлу.
    :return: Строка с заголовком окна или None, если заголовок не найден.
    """
    try:
        tree = ET.parse(ui_path)
        root = tree.getroot()
        # Ищем элемент <widget class="QMainWindow">, а внутри него - нужный <property>
        main_window_widget = root.find(".//widget[@class='QMainWindow']")
        if main_window_widget is not None:
            property_element = main_window_widget.find("./property[@name='windowTitle']/string")
            if property_element is not None:
                return property_element.text
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Ошибка при парсинге файла '{ui_path}': {e}")
    return None

def compile_ui_files_recursively(ui_dir, output_dir):
    """
    Рекурсивно находит и компилирует все .ui файлы в .py,
    из директории ui_dir в директорию output_dir.
    Перекомпилирует, только если .py файл отсутствует или .ui файл новее.
    """
    if not os.path.isdir(ui_dir):
        print(f"ОШИБКА: Директория с UI-файлами не найдена: {ui_dir}")
        return
    if not os.path.isdir(output_dir):
        print(f"ОШИБКА: Директория для скомпилированных файлов не найдена: {output_dir}")
        return
        
    for root, _, files in os.walk(ui_dir):
        for ui_file in files:
            if not ui_file.endswith(".ui"):
                continue

            ui_path = os.path.join(root, ui_file)
            
            # Generate the name for the .py file (e.g., widget.ui -> ui_widget.py)
            base_name = os.path.splitext(ui_file)[0]
            py_file_name = f"ui_{base_name}.py"
            # Сохраняем .py файл в корневой директории вывода
            py_path = os.path.join(output_dir, py_file_name)

            # Recompile if .py file is missing or .ui is newer
            recompile = False
            if not os.path.exists(py_path):
                recompile = True
                print(f"Файл '{py_path}' не найден. Требуется компиляция.")
            elif os.path.getmtime(ui_path) > os.path.getmtime(py_path):
                recompile = True
                print(f"Изменения в '{ui_path}'. Требуется перекомпиляция.")

            if recompile:
                print(f"Компиляция '{ui_path}' -> '{py_path}'...")
                try:
                    # Using check=True to raise an exception on error
                    subprocess.run(
                        ['pyside6-uic', ui_path, '-o', py_path], 
                        check=True,
                        capture_output=True, # Hide verbose output unless there's an error
                        text=True
                    )
                    print("Компиляция прошла успешно.")
                except FileNotFoundError:
                    print("\n" + "="*50)
                    print("ОШИБКА: Команда 'pyside6-uic' не найдена.")
                    print("Пожалуйста, убедитесь, что 'pyside6-tools' установлен.")
                    print("Вы можете установить его командой: pip install pyside6-tools")
                    print("="*50)
                    sys.exit(1)
                except subprocess.CalledProcessError as e:
                    print(f"\n" + "="*50)
                    print(f"ОШИБКА: Не удалось скомпилировать '{ui_path}'.")
                    print(f"Детали:\n{e.stderr}")
                    print("="*50)
                    # We exit here because a failed UI compile is a critical error
                    sys.exit(1)
