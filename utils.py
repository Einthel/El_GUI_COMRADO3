# utils.py
import os
import subprocess
import sys
import xml.etree.ElementTree as ET


def compile_ui_files():
    """
    Компилирует все .ui файлы в проекте.
    """
    # Вызываем рекурсивную компиляцию для всего проекта
    compile_ui_files_recursively(os.path.dirname(os.path.abspath(__file__)))

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

def compile_ui_files_recursively(start_dir):
    """
    Рекурсивно находит и компилирует все .ui файлы в .py,
    starting from the given directory.
    It only recompiles if the .py file is missing or the .ui file is newer.
    """
    for root, _, files in os.walk(start_dir):
        for ui_file in files:
            if not ui_file.endswith(".ui"):
                continue

            ui_path = os.path.join(root, ui_file)
            
            # Generate the name for the .py file (e.g., widget.ui -> ui_widget.py)
            base_name = os.path.splitext(ui_file)[0]
            py_file_name = f"ui_{base_name}.py"
            py_path = os.path.join(root, py_file_name)

            # Recompile if .py file is missing or .ui is newer
            if not os.path.exists(py_path) or os.path.getmtime(ui_path) > os.path.getmtime(py_path):
                print(f"Changes detected in '{ui_path}'. Compiling to '{py_path}'...")
                try:
                    # Using check=True to raise an exception on error
                    subprocess.run(
                        ['pyside6-uic', ui_path, '-o', py_path], 
                        check=True,
                        capture_output=True, # Hide verbose output unless there's an error
                        text=True
                    )
                    print("Compilation successful.")
                except FileNotFoundError:
                    print("\n" + "="*50)
                    print("ERROR: 'pyside6-uic' command not found.")
                    print("Please ensure 'pyside6-tools' is installed.")
                    print("You can install it with: pip install pyside6-tools")
                    print("="*50)
                    sys.exit(1)
                except subprocess.CalledProcessError as e:
                    print(f"\n" + "="*50)
                    print(f"ERROR: Failed to compile '{ui_path}'.")
                    print(f"Details:\n{e.stderr}")
                    print("="*50)
                    # We exit here because a failed UI compile is a critical error
                    sys.exit(1)
