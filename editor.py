# -*- coding: utf-8 -*-

import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QButtonGroup, QToolButton, QFileDialog, 
    QComboBox, QWidget, QAbstractItemView, QListWidget, QMenu, QMessageBox, QInputDialog,
    QListWidgetItem, QFrame
)
from PySide6.QtGui import QIcon, QKeySequence, QFont, QDrag, QAction
from PySide6.QtCore import QSize, Signal, QEvent, QMimeData, Qt, QRect
from ui_Editor import Ui_Editor_Window
from LoadSave import load_config, save_config
from LoadSaveButton import load_custom_buttons, add_custom_button, save_custom_buttons
from preset_dialog import PresetNameDialog

# Список "безопасных" шрифтов, которые обычно есть в Windows
SAFE_FONTS = [
    "Arial", "Arial Black", "Calibri", "Cambria", "Candara", "Comic Sans MS",
    "Consolas", "Constantia", "Corbel", "Courier New", "Georgia", "Impact",
    "Lucida Console", "Lucida Sans Unicode", "Microsoft Sans Serif",
    "Palatino Linotype", "Segoe UI", "Tahoma", "Times New Roman", "Trebuchet MS",
    "Verdana"
]

# Словарь для сопоставления методов и их названий в UI
METHOD_ACTIONS = {
    "Открыть браузер": "open_browser",
    "Открыть калькулятор": "open_calculator",
    "Открыть блокнот": "open_notepad",
    "Громкость +": "sound_up",
    "Громкость -": "sound_down",
    "Продолжить воспроизведение": "media_play_pause",
    "Поставить на паузу": "media_play_pause",
    "Следующая страница": "next_page",
    "Предыдущая страница": "previous_page"
    # "Открыть настройки" и "open_editor" не добавляем, так как они системные
}
# Обратный словарь для быстрого поиска названия по методу
REVERSED_METHOD_ACTIONS = {v: k for k, v in METHOD_ACTIONS.items()}


# Новый класс для списка с поддержкой Drag and Drop
class DraggableListWidget(QListWidget):
    """
    Кастомный QListWidget, который корректно создает QMimeData при начале
    операции перетаскивания (drag and drop).
    """
    def startDrag(self, supportedActions):
        item = self.currentItem()
        if item:
            mime_data = QMimeData()
            # Помещаем текст элемента в mime_data, чтобы его можно было прочитать
            mime_data.setText(item.text())
            
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            
            # Запускаем перетаскивание
            drag.exec(supportedActions)


class EditorWindow(QMainWindow):
    # Добавляем сигнал, который будет отправляться при сохранении конфига
    config_saved = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Editor_Window()
        self.ui.setupUi(self)

        # --- Программная замена QListWidget на наш кастомный ---
        original_widget = self.ui.Ready_Button_listWidget
        parent = original_widget.parentWidget()
        
        # Создаем экземпляр нашего нового виджета
        self.custom_list_widget = DraggableListWidget(parent)
        
        # Копируем важные свойства
        self.custom_list_widget.setObjectName(original_widget.objectName())
        self.custom_list_widget.setGeometry(original_widget.geometry())
        
        # Заменяем ссылку в self.ui, чтобы остальной код использовал новый виджет
        self.ui.Ready_Button_listWidget = self.custom_list_widget
        
        # Старый виджет больше не нужен, удаляем его
        original_widget.deleteLater()
        # --- Конец замены ---


        # Загружаем текущую конфигурацию при запуске окна
        self.config = load_config()
        self._page_keys = [] # Отсортированный список ключей страниц (page_1, page_2, ...)
        # Переменная для временного хранения пути к выбранной иконке
        self.current_icon_path = "" 
        self.current_page_index = 0 # Индекс текущей страницы
        self.buttons = [] # Список кнопок на текущей странице
        self.button_group = QButtonGroup(self) # Группа кнопок на текущей странице


        # Создаем и настраиваем наш собственный ComboBox для шрифтов
        self.font_combo_box = QComboBox(self.ui.Edit_ico_groupBox)
        self.font_combo_box.setGeometry(self.ui.fontComboBox.geometry()) # Копируем размеры и положение
        for font_name in sorted(SAFE_FONTS):
            self.font_combo_box.addItem(font_name)
        self.ui.fontComboBox.setVisible(False) # Скрываем оригинальный виджет

        # Заполняем ComboBox с готовыми действиями
        self.ui.Action_comboBox.addItem("") # Пустой элемент для сброса
        for action_name in sorted(METHOD_ACTIONS.keys()):
            self.ui.Action_comboBox.addItem(action_name)

        # Проверяем, есть ли третья вкладка. Если да - используем ее. Если нет - создаем.
        if self.ui.Edit_action_tabWidget.count() > 2:
            self.action_tab = self.ui.Edit_action_tabWidget.widget(2)
            self.ui.Edit_action_tabWidget.setTabText(2, "Действие")
        else:
            self.action_tab = QWidget()
            self.ui.Edit_action_tabWidget.addTab(self.action_tab, "Действие")
        
        # Перемещаем виджеты на вкладку "Действие"
        self.ui.Action_comboBox.setParent(self.action_tab)
        self.ui.Choose_action_label.setParent(self.action_tab)
        
        # Устанавливаем положение виджетов на новой вкладке
        self.ui.Choose_action_label.setGeometry(10, 10, 120, 30)
        self.ui.Action_comboBox.setGeometry(140, 10, 201, 30)

        # Настраиваем Drag and Drop для нашего нового виджета
        self.ui.Ready_Button_listWidget.setDragEnabled(True)
        self.ui.Ready_Button_listWidget.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)

        # Подключаем сигналы для живого обновления предпросмотра
        self.font_combo_box.currentTextChanged.connect(self.update_preview)
        self.ui.Sign_button_lineEdit.textChanged.connect(self.update_preview)

        # Деактивируем группу редактирования, пока не выбрана ни одна кнопка
        self.ui.Edit_Button_groupBox.setEnabled(False)

        # Подключение обработчиков сигналов
        self.ui.Browse_custom_pushButton.clicked.connect(self.browse_custom_icon)
        self.ui.Browse_pushButton.clicked.connect(self.browse_program_file)
        # Подключаем новую универсальную кнопку сохранения
        self.ui.Save_Button_pushButton.clicked.connect(self.save_action)
        # Подключаем кнопку сохранения пресета
        self.ui.Save_new_pushButton.clicked.connect(self.save_as_preset)
        # Подключаем обработчик выбора пресета из списка
        self.ui.Ready_Button_listWidget.itemClicked.connect(self.on_preset_selected)

        # Включаем кастомное контекстное меню для списка пресетов
        self.ui.Ready_Button_listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.Ready_Button_listWidget.customContextMenuRequested.connect(self.show_preset_context_menu)


        # Загружаем пресеты в список
        self.load_presets_to_list()
        # Настраиваем управление страницами
        self.setup_page_controls()

    def _get_sorted_page_keys(self):
        """Возвращает отсортированный список ключей страниц (['page_1', 'page_2', ...])."""
        page_keys = [key for key in self.config.keys() if key.startswith("page_")]
        # Сортируем по числовому индексу в ключе
        return sorted(page_keys, key=lambda k: int(k.split('_')[1]))

    def _setup_buttons_for_current_page(self):
        """Находит и настраивает кнопки для текущей активной страницы."""
        # Очищаем старую группу кнопок
        for button in self.button_group.buttons():
            self.button_group.removeButton(button)
        
        # Находим виджет текущей страницы
        current_page_widget = self.ui.Button_editor_stackedWidget.widget(self.current_page_index)
        if not current_page_widget:
            return

        # Находим все кнопки на этой странице
        all_buttons = current_page_widget.findChildren(QToolButton)
        self.buttons = sorted(all_buttons, key=lambda b: int(b.objectName().split('_')[-1]))
        
        # Создаем новую группу, чтобы управлять состоянием кнопок
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)
        
        # Добавляем все кнопки в группу для отслеживания нажатий
        for button in self.buttons:
            self.button_group.addButton(button)
            # Включаем прием drop-событий и устанавливаем фильтр
            button.setAcceptDrops(True)
            button.installEventFilter(self)
            # Включаем кастомное контекстное меню
            button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            button.customContextMenuRequested.connect(self.show_button_context_menu)

        # Переподключаем главный обработчик кликов
        if self.button_group.receivers("buttonClicked(QAbstractButton*)") > 0:
            self.button_group.buttonClicked.disconnect()
        self.button_group.buttonClicked.connect(self.on_button_group_clicked)


    def setup_page_controls(self):
        """Настраивает элементы управления страницами и загружает первую страницу."""
        self._page_keys = self._get_sorted_page_keys()
        
        # Если страниц нет, создаем первую
        if not self._page_keys:
            self.config["page_1"] = {}
            self._page_keys = ["page_1"]
            save_config(self.config)

        # Подключаем кнопки добавления/удаления страниц
        if self.ui.Add_page_button_editor.receivers("clicked()") > 0:
            self.ui.Add_page_button_editor.clicked.disconnect()
        self.ui.Add_page_button_editor.clicked.connect(self.add_page)
        
        if self.ui.Remove_page_button_editor.receivers("clicked()") > 0:
            self.ui.Remove_page_button_editor.clicked.disconnect()
        self.ui.Remove_page_button_editor.clicked.connect(self.delete_page)

        # Подключаем кнопки навигации next/back
        if self.ui.NextButton_editor.receivers("clicked()") > 0:
            self.ui.NextButton_editor.clicked.disconnect()
        self.ui.NextButton_editor.clicked.connect(self.next_page)

        if self.ui.BackButton_editor.receivers("clicked()") > 0:
            self.ui.BackButton_editor.clicked.disconnect()
        self.ui.BackButton_editor.clicked.connect(self.previous_page)

        # Загружаем начальную страницу
        self.switch_to_page(1)
        
    def next_page(self):
        """Переключает на следующую страницу с зацикливанием."""
        page_count = len(self._page_keys)
        if page_count == 0:
            return
        
        next_page_index = (self.current_page_index + 1) % page_count
        self.switch_to_page(next_page_index + 1)

    def previous_page(self):
        """Переключает на предыдущую страницу с зацикливанием."""
        page_count = len(self._page_keys)
        if page_count == 0:
            return
            
        prev_page_index = (self.current_page_index - 1 + page_count) % page_count
        self.switch_to_page(prev_page_index + 1)

    def _update_page_label(self):
        """Обновляет текстовую метку с номером текущей страницы."""
        page_count = len(self._page_keys)
        if page_count > 0:
            self.ui.Current_page_label_editor.setText(f"{self.current_page_index + 1}/{page_count}")
        else:
            self.ui.Current_page_label_editor.setText("0/0")

    def _create_new_page_widget(self, page_key):
        """
        Создает и возвращает виджет страницы (QWidget) с 12-ю кнопками.
        :param page_key: Ключ страницы, который будет использован как objectName.
        """
        new_page = QWidget()
        new_page.setObjectName(page_key)
        
        button_frame = QFrame(new_page)
        button_frame.setObjectName(u"Button_frame")
        button_frame.setGeometry(QRect(0, 10, 500, 340))
        button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        button_frame.setFrameShadow(QFrame.Shadow.Raised)

        for i in range(1, 13):
            button = QToolButton(button_frame)
            button.setObjectName(f"Edit_toolButton_{i:02d}")
            row = (i - 1) // 4
            col = (i - 1) % 4
            button.setGeometry(QRect(20 + col * 120, 10 + row * 110, 96, 96))
            button.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            button.setIconSize(QSize(64, 64))
            button.setCheckable(True)
            button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        return new_page

    def _rebuild_editor_pages(self):
        """
        Полностью перестраивает страницы в редакторе на основе текущего self.config.
        """
        # Очищаем старые страницы
        while self.ui.Button_editor_stackedWidget.count() > 0:
            widget = self.ui.Button_editor_stackedWidget.widget(0)
            self.ui.Button_editor_stackedWidget.removeWidget(widget)
            widget.deleteLater()
        
        # Получаем отсортированные ключи
        self._page_keys = self._get_sorted_page_keys()

        # Создаем и добавляем новые страницы
        for page_key in self._page_keys:
            page_widget = self._create_new_page_widget(page_key)
            self.ui.Button_editor_stackedWidget.addWidget(page_widget)

    def add_page(self):
        """Добавляет новую пустую страницу в редактор и в конфигурацию."""
        if len(self._page_keys) >= 10:
            QMessageBox.warning(self, "Ограничение", "Достигнуто максимальное количество страниц (10).")
            return

        # Находим максимальный существующий индекс, чтобы создать следующий
        if self._page_keys:
            last_key = self._page_keys[-1]
            new_index = int(last_key.split('_')[1]) + 1
        else:
            new_index = 1
        
        new_page_key = f"page_{new_index}"

        # Создаем новый виджет страницы с помощью хелпера
        new_page = self._create_new_page_widget(new_page_key)
        
        # Добавляем новую страницу в виджет и в конфиг
        new_widget_index = self.ui.Button_editor_stackedWidget.addWidget(new_page)
        self.config[new_page_key] = {}
        self._page_keys.append(new_page_key) # Обновляем список ключей
        
        # Сохраняем конфиг и переключаемся на новую страницу
        save_config(self.config)
        self.switch_to_page(new_widget_index + 1)
        self.config_saved.emit() # Отправляем сигнал, чтобы главное окно обновилось
        
    def delete_page(self):
        """Удаляет текущую страницу и переименовывает последующие."""
        if len(self._page_keys) <= 1:
            QMessageBox.warning(self, "Ошибка", "Нельзя удалить последнюю страницу.")
            return

        current_page_human = self.current_page_index + 1
        reply = QMessageBox.question(
            self, 
            "Подтверждение",
            f"Вы уверены, что хотите удалить страницу {current_page_human}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.No:
            return

        page_to_remove_index = self.current_page_index
        page_to_remove_key = self._page_keys[page_to_remove_index]
        
        # 1. Удаляем страницу из конфига
        del self.config[page_to_remove_key]

        # 2. Переименовываем оставшиеся страницы для сохранения последовательности
        pages_data = []
        # Собираем данные всех оставшихся страниц в отсортированном порядке
        sorted_keys = self._get_sorted_page_keys()
        for key in sorted_keys:
            pages_data.append(self.config.pop(key))

        # Добавляем их обратно с новыми ключами page_1, page_2, ...
        for i, page_data in enumerate(pages_data):
            self.config[f"page_{i+1}"] = page_data
        
        # 3. Полностью перестраиваем виджеты страниц в редакторе
        self._rebuild_editor_pages()

        # 4. Сохраняем обновленный конфиг
        save_config(self.config)

        # 5. Определяем, на какую страницу переключиться
        new_page_index = max(0, page_to_remove_index - 1)
        
        # 6. Переключаемся и отправляем сигнал
        self.switch_to_page(new_page_index + 1)
        self.config_saved.emit() # Отправляем сигнал, чтобы главное окно обновилось


    def switch_to_page(self, page_number):
        """Переключает редактор на указанную страницу (1-индексированную)."""
        page_index = page_number - 1
        
        # Проверяем, что индекс в допустимых пределах
        if not (0 <= page_index < len(self._page_keys)):
             return

        self.current_page_index = page_index
        
        # Переключаем QStackedWidget
        self.ui.Button_editor_stackedWidget.setCurrentIndex(page_index)
        
        # Обновляем метку с номером страницы
        self._update_page_label()
        
        # Настраиваем кнопки для этой страницы
        self._setup_buttons_for_current_page()
        # Загружаем их конфигурацию
        self.load_all_button_configs()
        # Сбрасываем панель редактора
        self.clear_editor_fields()
        self.ui.Edit_Button_groupBox.setEnabled(False)

    def eventFilter(self, watched, event):
        """Обрабатывает события Drag and Drop для кнопок в сетке."""
        if watched in self.buttons:
            if event.type() in [QEvent.Type.DragEnter, QEvent.Type.DragMove]:
                if event.mimeData().hasText():
                    event.acceptProposedAction()
                else:
                    event.ignore()
                return True
            elif event.type() == QEvent.Type.Drop:
                preset_name = event.mimeData().text()
                
                presets = load_custom_buttons()
                selected_preset = next((p for p in presets if p.get("name") == preset_name), None)

                if not selected_preset:
                    return False

                target_button = watched
                button_number = int(target_button.objectName().split('_')[-1])
                button_name = f"toolButton_{button_number}"

                # Применяем настройки к текущей странице в конфигурации
                current_page_key = self._page_keys[self.current_page_index]
                self.config[current_page_key][button_name] = selected_preset
                
                save_config(self.config)

                # Обновляем внешний вид кнопки в редакторе
                target_button.setText(selected_preset.get("sign", ""))
                font = QFont(selected_preset.get("font", ""))
                target_button.setFont(font)
                icon_path = selected_preset.get("icon_path", "")
                if icon_path and os.path.exists(icon_path):
                    target_button.setIcon(QIcon(icon_path))
                else:
                    target_button.setIcon(QIcon())

                self.config_saved.emit()
                
                event.acceptProposedAction()
                return True

        return super().eventFilter(watched, event)

    def show_preset_context_menu(self, pos):
        """Показывает контекстное меню для элемента в списке пресетов."""
        item = self.ui.Ready_Button_listWidget.itemAt(pos)
        if not item:
            return

        context_menu = QMenu(self)
        
        rename_action = QAction("Переименовать", self)
        rename_action.triggered.connect(lambda: self.rename_preset(item))
        context_menu.addAction(rename_action)

        delete_action = QAction("Удалить", self)
        delete_action.triggered.connect(lambda: self.delete_preset(item))
        context_menu.addAction(delete_action)

        context_menu.exec(self.ui.Ready_Button_listWidget.mapToGlobal(pos))

    def rename_preset(self, item):
        """Переименовывает выбранный пресет."""
        old_name = item.text()
        new_name, ok = QInputDialog.getText(self, "Переименовать пресет", "Новое имя:", text=old_name)

        if not ok or not new_name.strip() or new_name == old_name:
            return # Ничего не делаем, если пользователь отменил ввод или имя не изменилось

        presets = load_custom_buttons()
        
        # Проверяем, не занято ли новое имя
        if any(p.get("name") == new_name for p in presets):
            QMessageBox.warning(self, "Ошибка", f"Пресет с именем '{new_name}' уже существует.")
            return

        # Находим и обновляем пресет
        for preset in presets:
            if preset.get("name") == old_name:
                preset["name"] = new_name
                break
        
        save_custom_buttons(presets)
        self.load_presets_to_list() # Обновляем список в UI

    def delete_preset(self, item):
        """Удаляет выбранный пресет."""
        preset_name = item.text()
        reply = QMessageBox.question(self, "Подтверждение",
                                     f"Вы уверены, что хотите удалить пресет '{preset_name}'?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.No:
            return

        presets = load_custom_buttons()
        # Создаем новый список, исключая удаляемый пресет
        updated_presets = [p for p in presets if p.get("name") != preset_name]
        
        save_custom_buttons(updated_presets)
        self.load_presets_to_list() # Обновляем список

    def show_button_context_menu(self, pos):
        """Показывает контекстное меню для кнопки."""
        button = self.sender()
        if not isinstance(button, QToolButton):
            return

        context_menu = QMenu(self)
        clear_action = QAction("Очистить", self)
        clear_action.triggered.connect(lambda: self.clear_button_settings(button))
        context_menu.addAction(clear_action)

        context_menu.exec(button.mapToGlobal(pos))

    def clear_button_settings(self, button_to_clear):
        """Очищает все настройки для указанной кнопки на текущей странице."""
        button_number = int(button_to_clear.objectName().split('_')[-1])
        button_name = f"toolButton_{button_number}"
        
        current_page_key = self._page_keys[self.current_page_index]
        current_page_config = self.config[current_page_key]

        if button_name in current_page_config:
            # Сбрасываем конфигурацию для этой кнопки
            current_page_config[button_name] = {
                "icon_path": "",
                "sign": "",
                "font": self.font_combo_box.itemText(0), # Шрифт по-умолчанию
                "action": {"type": "", "value": ""}
            }
            
            save_config(self.config)

            # Обновляем внешний вид кнопки
            button_to_clear.setIcon(QIcon())
            button_to_clear.setText("")
            button_to_clear.setFont(QFont(self.font_combo_box.itemText(0)))
            
            # Если эта кнопка была выбрана, очищаем панель редактора
            if button_to_clear.isChecked():
                self.clear_editor_fields()

            self.config_saved.emit()

    def load_presets_to_list(self):
        """Загружает сохраненные пресеты и отображает их в Ready_Button_listWidget."""
        self.ui.Ready_Button_listWidget.clear()
        presets = load_custom_buttons()
        for preset in presets:
            preset_name = preset.get("name", "Без имени")
            icon_path = preset.get("icon_path", "")

            # Создаем элемент списка
            item = QListWidgetItem(preset_name)
            
            # Устанавливаем иконку, если она есть
            if icon_path and os.path.exists(icon_path):
                item.setIcon(QIcon(icon_path))
            
            # Добавляем готовый элемент в список
            self.ui.Ready_Button_listWidget.addItem(item)

    def on_preset_selected(self, item):
        """Обрабатывает выбор пресета из списка."""
        preset_name = item.text()
        presets = load_custom_buttons()
        
        selected_preset = None
        for preset in presets:
            if preset.get("name") == preset_name:
                selected_preset = preset
                break
        
        if not selected_preset:
            return

        # Применяем настройки пресета к текущим полям редактора
        self.current_icon_path = selected_preset.get("icon_path", "")
        self.ui.Sign_button_lineEdit.setText(selected_preset.get("sign", ""))
        
        font_name = selected_preset.get("font", "")
        if font_name in SAFE_FONTS:
            self.font_combo_box.setCurrentText(font_name)
        else:
            self.font_combo_box.setCurrentIndex(0)
            
        # Обновляем иконку-пример
        if self.current_icon_path and os.path.exists(self.current_icon_path):
            self.ui.Example_toolButton.setIcon(QIcon(self.current_icon_path))
        else:
            self.ui.Example_toolButton.setIcon(QIcon())

        # Загружаем действие
        action_config = selected_preset.get("action", {})
        action_type = action_config.get("type")
        action_value = action_config.get("value", "")

        # Сбрасываем все поля перед установкой новых значений
        self.ui.Edit_keySequenceEdit.clear()
        self.ui.Soft_lineEdit.clear()
        self.ui.Action_comboBox.setCurrentIndex(0)

        if action_type == "shortcut":
            self.ui.Edit_keySequenceEdit.setKeySequence(QKeySequence.fromString(action_value))
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.shortcut_tab)
        elif action_type == "program":
            self.ui.Soft_lineEdit.setText(action_value)
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.soft_tab)
        elif action_type == "method":
            display_name = REVERSED_METHOD_ACTIONS.get(action_value, "")
            self.ui.Action_comboBox.setCurrentText(display_name)
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.action_tab)

        # Обновляем предпросмотр
        self.update_preview()

    def load_all_button_configs(self):
        """Загружает и устанавливает иконки и текст для всех кнопок на ТЕКУЩЕЙ странице."""
        # Получаем конфиг для текущей страницы
        current_page_key = self._page_keys[self.current_page_index]
        page_config = self.config.get(current_page_key, {})

        for button in self.buttons:
            button_number = int(button.objectName().split('_')[-1])
            button_name = f"toolButton_{button_number}"
            
            button_config = page_config.get(button_name, {})
            icon_path = button_config.get("icon_path", "")
            sign_text = button_config.get("sign", "")
            font_name = button_config.get("font", "")

            button.setText(sign_text)
            if font_name:
                button.setFont(QFont(font_name))

            if icon_path and os.path.exists(icon_path):
                button.setIcon(QIcon(icon_path))
                button.setIconSize(QSize(64, 64))
            else:
                button.setIcon(QIcon())

    def on_button_group_clicked(self, clicked_button):
        """Обрабатывает нажатие на любую кнопку в сетке."""
        is_checked = clicked_button.isChecked()
        
        # Реализуем "quasi-exclusive" поведение:
        # если кнопка включается, все остальные выключаются.
        if is_checked:
            for button in self.buttons:
                if button is not clicked_button:
                    button.setChecked(False)

        # Активируем или деактивируем панель редактирования.
        self.ui.Edit_Button_groupBox.setEnabled(is_checked)
        
        if is_checked:
            # Если кнопка выбрана, загружаем ее настройки.
            self.load_button_config(clicked_button)
        else:
            # Если выбор снят, очищаем поля.
            self.clear_editor_fields()

    def update_preview(self):
        """Обновляет предпросмотр на кнопке-примере и на выбранной кнопке в сетке."""
        # Получаем текущие значения из полей редактора
        sign_text = self.ui.Sign_button_lineEdit.text()
        font_name = self.font_combo_box.currentText()
        
        # Создаем объект шрифта
        font = QFont(font_name)
        
        # Применяем к кнопке-примеру
        self.ui.Example_toolButton.setText(sign_text)
        self.ui.Example_toolButton.setFont(font)
        
        # Применяем к выбранной кнопке в сетке
        selected_button = self.button_group.checkedButton()
        if selected_button:
            selected_button.setText(sign_text)
            selected_button.setFont(font)

    def load_button_config(self, button):
        """Загружает настройки для выбранной кнопки с текущей страницы."""
        button_number = int(button.objectName().split('_')[-1])
        button_name = f"toolButton_{button_number}"
        
        # Получаем конфиг для текущей страницы
        current_page_key = self._page_keys[self.current_page_index]
        page_config = self.config[current_page_key]
        button_config = page_config.get(button_name, {})
        action_config = button_config.get("action", {})

        # Загружаем и отображаем иконку
        self.current_icon_path = button_config.get("icon_path", "")
        if self.current_icon_path and os.path.exists(self.current_icon_path):
            self.ui.Example_toolButton.setIcon(QIcon(self.current_icon_path))
        else:
            self.ui.Example_toolButton.setIcon(QIcon()) # Сбрасываем иконку, если путь не указан или неверен

        # Загружаем подпись
        sign_text = button_config.get("sign", "")
        self.ui.Sign_button_lineEdit.setText(sign_text)

        # Загружаем шрифт
        font_name = button_config.get("font", "")
        if font_name in SAFE_FONTS:
            self.font_combo_box.setCurrentText(font_name)
        else:
            # Если в конфиге шрифт, которого нет в списке, ставим первый по умолчанию
            self.font_combo_box.setCurrentIndex(0)

        # Получаем настройки действия
        action_type = action_config.get("type")
        action_value = action_config.get("value", "")

        # В зависимости от типа действия переключаем вкладку и заполняем поля
        if action_type == "shortcut":
            key_sequence = QKeySequence.fromString(action_value)
            self.ui.Edit_keySequenceEdit.setKeySequence(key_sequence)
            self.ui.Soft_lineEdit.clear() # Очищаем поле другой вкладки
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.shortcut_tab)
            self.ui.Action_comboBox.setCurrentIndex(0) # Сбрасываем выбор
        elif action_type == "program":
            self.ui.Soft_lineEdit.setText(action_value)
            self.ui.Edit_keySequenceEdit.clear() # Очищаем поле другой вкладки
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.soft_tab)
            self.ui.Action_comboBox.setCurrentIndex(0) # Сбрасываем выбор
        elif action_type == "method":
            # Ищем понятное имя для метода и устанавливаем его в комбо-боксе
            display_name = REVERSED_METHOD_ACTIONS.get(action_value, "")
            self.ui.Action_comboBox.setCurrentText(display_name)
            self.ui.Soft_lineEdit.clear() # Очищаем поле пути
            self.ui.Edit_keySequenceEdit.clear()
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.action_tab)
        else:
            # Если тип не задан, очищаем все поля
            self.ui.Edit_keySequenceEdit.clear()
            self.ui.Soft_lineEdit.clear()
            self.ui.Action_comboBox.setCurrentIndex(0)
            # Здесь можно добавить логику для других вкладок (soft_tab, script_tab)
    
    def clear_editor_fields(self):
        """Очищает поля редактора, когда ни одна кнопка не выбрана."""
        self.ui.Example_toolButton.setIcon(QIcon())
        self.ui.Edit_keySequenceEdit.clear()
        self.ui.Soft_lineEdit.clear()
        self.ui.Sign_button_lineEdit.clear()
        self.font_combo_box.setCurrentIndex(0) # Сбрасываем шрифт
        self.current_icon_path = ""
        # Здесь нужно будет добавить очистку для полей других вкладок

    def browse_custom_icon(self):
        """Открывает диалог выбора файла и обновляет иконку-пример."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать иконку",
            "",
            "Изображения (*.png *.jpg *.ico *.bmp)"
        )
        if file_path:
            # Отображаем выбранную иконку на примере
            self.ui.Example_toolButton.setIcon(QIcon(file_path))
            # Сохраняем путь для дальнейшего сохранения в config.json
            self.current_icon_path = file_path

    def save_as_preset(self):
        """Собирает текущие настройки из редактора и сохраняет их как пресет."""
        dialog = PresetNameDialog(self)
        if not dialog.exec():
            return

        preset_name = dialog.get_preset_name()
        if not preset_name:
            QMessageBox.warning(self, "Ошибка", "Имя пресета не может быть пустым.")
            return

        # Проверяем, существует ли уже пресет с таким именем
        existing_presets = load_custom_buttons()
        if any(p.get("name") == preset_name for p in existing_presets):
            reply = QMessageBox.question(self, "Подтверждение", 
                                         f"Пресет с именем '{preset_name}' уже существует. Перезаписать?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.No:
                return # Пользователь отказался от перезаписи

        # Теперь собираем конфиг
        sign_text = self.ui.Sign_button_lineEdit.text() # Это подпись для кнопки

        preset_config = {
            "name": preset_name,
            "icon_path": self.current_icon_path,
            "sign": sign_text,
            "font": self.font_combo_box.currentText(),
            "action": {}
        }

        current_tab = self.ui.Edit_action_tabWidget.currentWidget()

        if current_tab == self.ui.shortcut_tab:
            preset_config["action"]["type"] = "shortcut"
            preset_config["action"]["value"] = self.ui.Edit_keySequenceEdit.keySequence().toString(QKeySequence.NativeText)
        elif current_tab == self.ui.soft_tab:
            preset_config["action"]["type"] = "program"
            preset_config["action"]["value"] = self.ui.Soft_lineEdit.text()
        elif current_tab == self.action_tab:
            selected_action_name = self.ui.Action_comboBox.currentText()
            if selected_action_name in METHOD_ACTIONS:
                preset_config["action"]["type"] = "method"
                preset_config["action"]["value"] = METHOD_ACTIONS[selected_action_name]
            else: # Если ничего не выбрано, сохраняем как пустое
                preset_config["action"]["type"] = ""
                preset_config["action"]["value"] = ""
        
        add_custom_button(preset_config)
        # Обновляем список пресетов в UI
        self.load_presets_to_list()

    def save_action(self):
        """
        Сохраняет настройки для выбранной кнопки на текущей странице.
        """
        selected_button = self.button_group.checkedButton()
        if not selected_button:
            return

        button_number = int(selected_button.objectName().split('_')[-1])
        button_name = f"toolButton_{button_number}"
        
        # Получаем ключ текущей страницы
        current_page_key = self._page_keys[self.current_page_index]
        
        # Если для кнопки еще нет конфига, создаем его
        if button_name not in self.config[current_page_key]:
            self.config[current_page_key][button_name] = {}
        
        # Обновляем путь к иконке, подпись и шрифт
        self.config[current_page_key][button_name]["icon_path"] = self.current_icon_path
        self.config[current_page_key][button_name]["sign"] = self.ui.Sign_button_lineEdit.text()
        self.config[current_page_key][button_name]["font"] = self.font_combo_box.currentText()

        # Создаем словарь action, если его нет
        if "action" not in self.config[current_page_key][button_name]:
            self.config[current_page_key][button_name]["action"] = {}

        current_tab = self.ui.Edit_action_tabWidget.currentWidget()

        if current_tab == self.ui.shortcut_tab:
            # Сохраняем сочетание клавиш
            shortcut = self.ui.Edit_keySequenceEdit.keySequence().toString(QKeySequence.NativeText)
            self.config[current_page_key][button_name]["action"]["type"] = "shortcut"
            self.config[current_page_key][button_name]["action"]["value"] = shortcut

        elif current_tab == self.ui.soft_tab:
            # Сохраняем путь к программе
            program_path = self.ui.Soft_lineEdit.text()
            self.config[current_page_key][button_name]["action"]["type"] = "program"
            self.config[current_page_key][button_name]["action"]["value"] = program_path
        
        elif current_tab == self.action_tab:
            selected_action_name = self.ui.Action_comboBox.currentText()
            if selected_action_name in METHOD_ACTIONS:
                self.config[current_page_key][button_name]["action"]["type"] = "method"
                self.config[current_page_key][button_name]["action"]["value"] = METHOD_ACTIONS[selected_action_name]
            else:
                self.config[current_page_key][button_name]["action"]["type"] = ""
                self.config[current_page_key][button_name]["action"]["value"] = ""


        # Сохраняем изменения в файл config.json
        save_config(self.config)

        # Отправляем сигнал об успешном сохранении
        self.config_saved.emit()

        # Обновляем иконку на самой кнопке в сетке
        if self.current_icon_path and os.path.exists(self.current_icon_path):
            selected_button.setIcon(QIcon(self.current_icon_path))
        else:
            selected_button.setIcon(QIcon())

    def browse_program_file(self):
        """Открывает диалог для выбора исполняемого файла или ярлыка."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать программу",
            "",
            "Программы (*.exe *.lnk)"
        )
        if file_path:
            self.ui.Soft_lineEdit.setText(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EditorWindow()
    window.show()
    sys.exit(app.exec())
