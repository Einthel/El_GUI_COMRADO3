# -*- coding: utf-8 -*-

import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QButtonGroup, QToolButton, QFileDialog, 
    QComboBox, QWidget, QAbstractItemView, QListWidget, QMenu, QMessageBox, QInputDialog,
    QListWidgetItem, QFrame, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QIcon, QKeySequence, QFont, QDrag, QAction, QColor
from PySide6.QtCore import QSize, Signal, QEvent, QMimeData, Qt, QRect
from ui_Editor import Ui_Editor_Window
from LoadSave import load_config, save_config
from LoadSavePreset import load_custom_buttons, add_custom_button, save_custom_buttons
from preset_dialog import PresetNameDialog
from page_manager import PageManager
import constants
# from utils import adjust_font_size - Больше не нужно

# Список "безопасных" шрифтов, которые обычно есть в Windows
SAFE_FONTS = constants.SAFE_FONTS

# Словарь для сопоставления методов и их названий в UI
METHOD_ACTIONS = constants.METHOD_ACTIONS
# Обратный словарь для быстрого поиска названия по методу
REVERSED_METHOD_ACTIONS = constants.REVERSED_METHOD_ACTIONS


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

        self._initialize_state()
        self._setup_ui_components()
        self._connect_signals()
        self._load_initial_data()

    def _initialize_state(self):
        """Initializes instance variables and state managers."""
        self.config = load_config()
        self.page_manager = PageManager(self)
        self.current_icon_path = ""
        self.buttons = []
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)

    def _setup_ui_components(self):
        """Performs programmatic UI setup and modifications."""
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

        # Создаем и настраиваем наш собственный ComboBox для шрифтов
        self.font_combo_box = QComboBox(self.ui.Edit_ico_groupBox)
        self.font_combo_box.setGeometry(self.ui.fontComboBox.geometry()) # Копируем размеры и положение
        for font_name in sorted(SAFE_FONTS):
            self.font_combo_box.addItem(font_name)
        self.ui.fontComboBox.setVisible(False) # Скрываем оригинальный виджет
        
        # Заполняем ComboBox для выбора размера шрифта
        self.ui.Size_font_comboBox.addItems([str(i) for i in range(5, 16)])

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

        # Деактивируем группу редактирования, пока не выбрана ни одна кнопка
        self.ui.Edit_Button_groupBox.setEnabled(False)

        # Применяем тени к виджетам
        self._apply_shadow_effects()

    def _connect_signals(self):
        """Connects all signals to their respective slots."""
        self.page_manager.page_changed.connect(self.switch_to_page)
        self.button_group.buttonClicked.connect(self.on_button_group_clicked)

        # Live preview updates
        self.font_combo_box.currentTextChanged.connect(self.update_preview)
        self.ui.Size_font_comboBox.currentTextChanged.connect(self.update_preview)
        self.ui.Sign_button_lineEdit.textChanged.connect(self.update_preview)

        # Main buttons
        self.ui.Browse_custom_pushButton.clicked.connect(self.browse_custom_icon)
        self.ui.Browse_pushButton.clicked.connect(self.browse_program_file)
        self.ui.Save_Button_pushButton.clicked.connect(self.save_action)
        self.ui.Save_new_pushButton.clicked.connect(self.save_as_preset)

        # Preset list interactions
        self.ui.Ready_Button_listWidget.itemClicked.connect(self.on_preset_selected)
        self.ui.Ready_Button_listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.Ready_Button_listWidget.customContextMenuRequested.connect(self.show_preset_context_menu)

    def _apply_shadow_effects(self):
        """Создает и применяет тени к указанным виджетам."""
        widgets_to_shadow = [
            self.ui.Ready_Button_listWidget,
            self.ui.Button_example_layout,
            self.ui.Edit_Button_groupBox
        ]
        
        for widget in widgets_to_shadow:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(15)
            shadow.setColor(QColor(0, 0, 0, 160))
            shadow.setOffset(5, 5)
            widget.setGraphicsEffect(shadow)

    def _load_initial_data(self):
        """Loads presets and sets up the initial page."""
        self.load_presets_to_list()
        self.setup_page_controls()

    def _get_sorted_page_keys(self):
        """Возвращает отсортированный список ключей страниц (['page_1', 'page_2', ...])."""
        page_keys = [key for key in self.config.keys() if key.startswith(constants.PAGE_PREFIX)]
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
        
        # Добавляем все кнопки в существующую группу для отслеживания нажатий
        for button in self.buttons:
            self.button_group.addButton(button)
            # Включаем прием drop-событий и устанавливаем фильтр
            button.setAcceptDrops(True)
            button.installEventFilter(self)
            # Включаем кастомное контекстное меню
            button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            button.customContextMenuRequested.connect(self.show_button_context_menu)


    def setup_page_controls(self):
        """Настраивает элементы управления страницами и загружает первую страницу."""
        self._page_keys = self._get_sorted_page_keys()
        self.page_manager.set_page_keys(self._page_keys)
        
        # Если страниц нет, создаем первую
        if not self._page_keys:
            self.config[f"{constants.PAGE_PREFIX}1"] = {}
            self._page_keys = [f"{constants.PAGE_PREFIX}1"]
            save_config(self.config)

        # ПЕРЕСТРАИВАЕМ СТРАНИЦЫ ПРИ КАЖДОМ ЗАПУСКЕ
        # Это гарантирует, что stackedWidget соответствует config.json
        self._rebuild_editor_pages()

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
        self.ui.NextButton_editor.clicked.connect(self.page_manager.next)

        if self.ui.BackButton_editor.receivers("clicked()") > 0:
            self.ui.BackButton_editor.clicked.disconnect()
        self.ui.BackButton_editor.clicked.connect(self.page_manager.previous)

        # Загружаем начальную страницу
        self.page_manager.go_to_page(1)
        
    def next_page(self):
        """Переключает на следующую страницу с зацикливанием."""
        self.page_manager.next()

    def previous_page(self):
        """Переключает на предыдущую страницу с зацикливанием."""
        self.page_manager.previous()

    def _update_page_label(self):
        """Обновляет текстовую метку с номером текущей страницы."""
        self.ui.Current_page_label_editor.setText(self.page_manager.get_page_label_text())

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

        # Добавляем тень к фрейму, как в главном окне
        frame_shadow = QGraphicsDropShadowEffect(button_frame)
        frame_shadow.setBlurRadius(25)
        frame_shadow.setXOffset(0)
        frame_shadow.setYOffset(0)
        frame_shadow.setColor(QColor(0, 0, 0, 200))
        button_frame.setGraphicsEffect(frame_shadow)

        for i in range(1, 13):
            button = QToolButton(button_frame)
            button.setObjectName(f"{constants.EDITOR_BUTTON_PREFIX}{i:02d}")
            row = (i - 1) // 4
            col = (i - 1) % 4
            button.setGeometry(QRect(20 + col * 120, 10 + row * 110, 96, 96))
            button.setFixedSize(96, 96) # Фиксируем размер кнопки
            button.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            button.setIconSize(QSize(64, 64))
            button.setCheckable(True)
            button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

            # Добавляем тень к кнопке
            button_shadow = QGraphicsDropShadowEffect(button)
            button_shadow.setBlurRadius(15)
            button_shadow.setXOffset(5)
            button_shadow.setYOffset(5)
            button_shadow.setColor(QColor(0, 0, 0, 160))
            button.setGraphicsEffect(button_shadow)
        
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
        self.page_manager.set_page_keys(self._page_keys)

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
        
        new_page_key = f"{constants.PAGE_PREFIX}{new_index}"

        # Создаем новый виджет страницы с помощью хелпера
        new_page = self._create_new_page_widget(new_page_key)
        
        # Добавляем новую страницу в виджет и в конфиг
        new_widget_index = self.ui.Button_editor_stackedWidget.addWidget(new_page)
        self.config[new_page_key] = {}
        self._page_keys.append(new_page_key) # Обновляем список ключей
        self.page_manager.set_page_keys(self._page_keys)
        
        # Сохраняем конфиг и переключаемся на новую страницу
        save_config(self.config)
        self.page_manager.go_to_page(new_widget_index + 1)
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
            self.config[f"{constants.PAGE_PREFIX}{i+1}"] = page_data
        
        # 3. Полностью перестраиваем виджеты страниц в редакторе
        self._rebuild_editor_pages()

        # 4. Сохраняем обновленный конфиг
        save_config(self.config)

        # 5. Определяем, на какую страницу переключиться
        new_page_index = max(0, page_to_remove_index - 1)
        
        # 6. Переключаемся и отправляем сигнал
        self.page_manager.go_to_page(new_page_index + 1)
        self.config_saved.emit() # Отправляем сигнал, чтобы главное окно обновилось


    def switch_to_page(self, page_number):
        """Переключает редактор на указанную страницу (1-индексированную)."""
        page_index = page_number - 1
        
        # Проверяем, что индекс в допустимых пределах
        if not (0 <= page_index < self.page_manager.get_page_count()):
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
                selected_preset = next((p for p in presets if p.get(constants.KEY_NAME) == preset_name), None)

                if not selected_preset:
                    return False

                target_button = watched
                button_number = int(target_button.objectName().split('_')[-1])
                button_name = f"{constants.BUTTON_PREFIX}{button_number}"

                # Применяем настройки к текущей странице в конфигурации
                current_page_key = self.page_manager.get_key_for_index(self.current_page_index)
                if not current_page_key:
                    return False
                self.config[current_page_key][button_name] = selected_preset
                
                save_config(self.config)

                # Обновляем внешний вид кнопки в редакторе
                sign_text = selected_preset.get(constants.KEY_SIGN, "")
                target_button.setText(sign_text)
                
                # Устанавливаем шрифт и подгоняем размер
                font_name = selected_preset.get(constants.KEY_FONT, "")
                font_size = selected_preset.get(constants.KEY_FONT_SIZE)
                font = QFont(font_name)
                if font_size:
                    font.setPointSize(font_size)
                target_button.setFont(font)

                if sign_text:
                    target_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
                else:
                    target_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

                icon_path = selected_preset.get(constants.KEY_ICON_PATH, "")
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
        if any(p.get(constants.KEY_NAME) == new_name for p in presets):
            QMessageBox.warning(self, "Ошибка", f"Пресет с именем '{new_name}' уже существует.")
            return

        # Находим и обновляем пресет
        for preset in presets:
            if preset.get(constants.KEY_NAME) == old_name:
                preset[constants.KEY_NAME] = new_name
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
        updated_presets = [p for p in presets if p.get(constants.KEY_NAME) != preset_name]
        
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
        button_name = f"{constants.BUTTON_PREFIX}{button_number}"
        
        current_page_key = self.page_manager.get_key_for_index(self.current_page_index)
        if not current_page_key:
            return
        
        current_page_config = self.config[current_page_key]

        if button_name in current_page_config:
            # Сбрасываем конфигурацию для этой кнопки
            current_page_config[button_name] = {
                constants.KEY_ICON_PATH: "",
                constants.KEY_SIGN: "",
                constants.KEY_FONT: self.font_combo_box.itemText(0), # Шрифт по-умолчанию
                constants.KEY_FONT_SIZE: int(self.ui.Size_font_comboBox.currentText()), # Размер по-умолчанию
                constants.KEY_ACTION: {constants.KEY_ACTION_TYPE: "", constants.KEY_ACTION_VALUE: ""}
            }
            
            save_config(self.config)

            # Обновляем внешний вид кнопки
            button_to_clear.setIcon(QIcon())
            button_to_clear.setText("")
            button_to_clear.setFont(QFont(self.font_combo_box.itemText(0)))
            button_to_clear.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
            
            # Если эта кнопка была выбрана, очищаем панель редактора
            if button_to_clear.isChecked():
                self.clear_editor_fields()

            self.config_saved.emit()

    def load_presets_to_list(self):
        """Загружает сохраненные пресеты и отображает их в Ready_Button_listWidget."""
        self.ui.Ready_Button_listWidget.clear()
        presets = load_custom_buttons()
        for preset in presets:
            preset_name = preset.get(constants.KEY_NAME, "Без имени")
            icon_path = preset.get(constants.KEY_ICON_PATH, "")

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
            if preset.get(constants.KEY_NAME) == preset_name:
                selected_preset = preset
                break
        
        if not selected_preset:
            return

        # Применяем настройки пресета к текущим полям редактора
        self.current_icon_path = selected_preset.get(constants.KEY_ICON_PATH, "")
        self.ui.Sign_button_lineEdit.setText(selected_preset.get(constants.KEY_SIGN, ""))
        
        font_name = selected_preset.get(constants.KEY_FONT, "")
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
        action_config = selected_preset.get(constants.KEY_ACTION, {})
        action_type = action_config.get(constants.KEY_ACTION_TYPE)
        action_value = action_config.get(constants.KEY_ACTION_VALUE, "")

        # Сбрасываем все поля перед установкой новых значений
        self.ui.Edit_keySequenceEdit.clear()
        self.ui.Soft_lineEdit.clear()
        self.ui.Action_comboBox.setCurrentIndex(0)

        if action_type == constants.ACTION_TYPE_SHORTCUT:
            self.ui.Edit_keySequenceEdit.setKeySequence(QKeySequence.fromString(action_value))
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.shortcut_tab)
        elif action_type == constants.ACTION_TYPE_PROGRAM:
            self.ui.Soft_lineEdit.setText(action_value)
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.soft_tab)
        elif action_type == constants.ACTION_TYPE_METHOD:
            display_name = REVERSED_METHOD_ACTIONS.get(action_value, "")
            self.ui.Action_comboBox.setCurrentText(display_name)
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.action_tab)

        # Обновляем предпросмотр
        self.update_preview()

    def load_all_button_configs(self):
        """Загружает и устанавливает иконки и текст для всех кнопок на ТЕКУЩЕЙ странице."""
        # Получаем конфиг для текущей страницы
        current_page_key = self.page_manager.get_key_for_index(self.current_page_index)
        if not current_page_key:
            return
            
        page_config = self.config.get(current_page_key, {})

        for button in self.buttons:
            button_number = int(button.objectName().split('_')[-1])
            button_name = f"{constants.BUTTON_PREFIX}{button_number}"
            
            button_config = page_config.get(button_name, {})
            icon_path = button_config.get(constants.KEY_ICON_PATH, "")
            sign_text = button_config.get(constants.KEY_SIGN, "")
            font_name = button_config.get(constants.KEY_FONT, "")
            font_size = button_config.get(constants.KEY_FONT_SIZE)

            button.setText(sign_text)
            
            # Устанавливаем шрифт и его размер
            if font_name:
                font = QFont(font_name)
                if font_size:
                    font.setPointSize(font_size)
                button.setFont(font)
            
            if sign_text:
                button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            else:
                button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

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
        font_size_text = self.ui.Size_font_comboBox.currentText()
        
        # Создаем объект шрифта
        font = QFont(font_name)
        if font_size_text.isdigit():
            font.setPointSize(int(font_size_text))
        
        # Определяем стиль кнопки в зависимости от наличия текста
        style = Qt.ToolButtonStyle.ToolButtonTextUnderIcon if sign_text else Qt.ToolButtonStyle.ToolButtonIconOnly
        
        # Применяем к кнопке-примеру
        self.ui.Example_toolButton.setText(sign_text)
        self.ui.Example_toolButton.setFont(font)
        self.ui.Example_toolButton.setToolButtonStyle(style)
        
        # Применяем к выбранной кнопке в сетке
        selected_button = self.button_group.checkedButton()
        if selected_button:
            selected_button.setText(sign_text)
            selected_button.setFont(font)
            selected_button.setToolButtonStyle(style)

    def load_button_config(self, button):
        """Загружает настройки для выбранной кнопки с текущей страницы."""
        button_number = int(button.objectName().split('_')[-1])
        button_name = f"{constants.BUTTON_PREFIX}{button_number}"
        
        # Получаем конфиг для текущей страницы
        current_page_key = self.page_manager.get_key_for_index(self.current_page_index)
        if not current_page_key:
            return

        page_config = self.config[current_page_key]
        button_config = page_config.get(button_name, {})
        action_config = button_config.get(constants.KEY_ACTION, {})

        # Загружаем и отображаем иконку
        self.current_icon_path = button_config.get(constants.KEY_ICON_PATH, "")
        if self.current_icon_path and os.path.exists(self.current_icon_path):
            # QIcon в Qt поддерживает SVG нативно, просто передаем путь
            self.ui.Example_toolButton.setIcon(QIcon(self.current_icon_path))
        else:
            self.ui.Example_toolButton.setIcon(QIcon()) # Сбрасываем иконку, если путь не указан или неверен

        # Загружаем подпись
        sign_text = button_config.get(constants.KEY_SIGN, "")
        self.ui.Sign_button_lineEdit.setText(sign_text)

        # Загружаем шрифт
        font_name = button_config.get(constants.KEY_FONT, "")
        font_size = button_config.get(constants.KEY_FONT_SIZE)
        
        if font_name in SAFE_FONTS:
            self.font_combo_box.setCurrentText(font_name)
        else:
            # Если в конфиге шрифт, которого нет в списке, ставим первый по умолчанию
            self.font_combo_box.setCurrentIndex(0)

        # Загружаем размер шрифта
        if font_size:
            self.ui.Size_font_comboBox.setCurrentText(str(font_size))
        else:
            self.ui.Size_font_comboBox.setCurrentIndex(0) # или значение по умолчанию

        # Получаем настройки действия
        action_type = action_config.get(constants.KEY_ACTION_TYPE)
        action_value = action_config.get(constants.KEY_ACTION_VALUE, "")

        # В зависимости от типа действия переключаем вкладку и заполняем поля
        if action_type == constants.ACTION_TYPE_SHORTCUT:
            key_sequence = QKeySequence.fromString(action_value)
            self.ui.Edit_keySequenceEdit.setKeySequence(key_sequence)
            self.ui.Soft_lineEdit.clear() # Очищаем поле другой вкладки
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.shortcut_tab)
            self.ui.Action_comboBox.setCurrentIndex(0) # Сбрасываем выбор
        elif action_type == constants.ACTION_TYPE_PROGRAM:
            self.ui.Soft_lineEdit.setText(action_value)
            self.ui.Edit_keySequenceEdit.clear() # Очищаем поле другой вкладки
            self.ui.Edit_action_tabWidget.setCurrentWidget(self.ui.soft_tab)
            self.ui.Action_comboBox.setCurrentIndex(0) # Сбрасываем выбор
        elif action_type == constants.ACTION_TYPE_METHOD:
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
        self.ui.Size_font_comboBox.setCurrentIndex(0) # Сбрасываем размер
        self.current_icon_path = ""
        # Здесь нужно будет добавить очистку для полей других вкладок

    def browse_custom_icon(self):
        """Открывает диалог выбора файла и обновляет иконку-пример."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать иконку",
            "",
            "Изображения (*.png *.jpg *.jpeg *.ico *.bmp *.svg)"
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
        if any(p.get(constants.KEY_NAME) == preset_name for p in existing_presets):
            reply = QMessageBox.question(self, "Подтверждение", 
                                         f"Пресет с именем '{preset_name}' уже существует. Перезаписать?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.No:
                return # Пользователь отказался от перезаписи

        # Теперь собираем конфиг
        sign_text = self.ui.Sign_button_lineEdit.text() # Это подпись для кнопки

        preset_config = {
            constants.KEY_NAME: preset_name,
            constants.KEY_ICON_PATH: self.current_icon_path,
            constants.KEY_SIGN: sign_text,
            constants.KEY_FONT: self.font_combo_box.currentText(),
            constants.KEY_FONT_SIZE: int(self.ui.Size_font_comboBox.currentText()),
            constants.KEY_ACTION: {}
        }

        current_tab = self.ui.Edit_action_tabWidget.currentWidget()

        if current_tab == self.ui.shortcut_tab:
            preset_config[constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_SHORTCUT
            preset_config[constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = self.ui.Edit_keySequenceEdit.keySequence().toString(QKeySequence.NativeText)
        elif current_tab == self.ui.soft_tab:
            preset_config[constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_PROGRAM
            preset_config[constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = self.ui.Soft_lineEdit.text()
        elif current_tab == self.action_tab:
            selected_action_name = self.ui.Action_comboBox.currentText()
            if selected_action_name in METHOD_ACTIONS:
                preset_config[constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_METHOD
                preset_config[constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = METHOD_ACTIONS[selected_action_name]
            else: # Если ничего не выбрано, сохраняем как пустое
                preset_config[constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_EMPTY
                preset_config[constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = constants.ACTION_TYPE_EMPTY
        
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
        button_name = f"{constants.BUTTON_PREFIX}{button_number}"
        
        # Получаем ключ текущей страницы
        current_page_key = self.page_manager.get_key_for_index(self.current_page_index)
        if not current_page_key:
            return
        
        # Если для кнопки еще нет конфига, создаем его
        if button_name not in self.config[current_page_key]:
            self.config[current_page_key][button_name] = {}
        
        # Обновляем путь к иконке, подпись и шрифт
        self.config[current_page_key][button_name][constants.KEY_ICON_PATH] = self.current_icon_path
        self.config[current_page_key][button_name][constants.KEY_SIGN] = self.ui.Sign_button_lineEdit.text()
        self.config[current_page_key][button_name][constants.KEY_FONT] = self.font_combo_box.currentText()
        self.config[current_page_key][button_name][constants.KEY_FONT_SIZE] = int(self.ui.Size_font_comboBox.currentText())

        # Создаем словарь action, если его нет
        if constants.KEY_ACTION not in self.config[current_page_key][button_name]:
            self.config[current_page_key][button_name][constants.KEY_ACTION] = {}

        current_tab = self.ui.Edit_action_tabWidget.currentWidget()

        if current_tab == self.ui.shortcut_tab:
            # Сохраняем сочетание клавиш
            shortcut = self.ui.Edit_keySequenceEdit.keySequence().toString(QKeySequence.NativeText)
            self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_SHORTCUT
            self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = shortcut

        elif current_tab == self.ui.soft_tab:
            # Сохраняем путь к программе
            program_path = self.ui.Soft_lineEdit.text()
            self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_PROGRAM
            self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = program_path
        
        elif current_tab == self.action_tab:
            selected_action_name = self.ui.Action_comboBox.currentText()
            if selected_action_name in METHOD_ACTIONS:
                self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_METHOD
                self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = METHOD_ACTIONS[selected_action_name]
            else:
                self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_TYPE] = constants.ACTION_TYPE_EMPTY
                self.config[current_page_key][button_name][constants.KEY_ACTION][constants.KEY_ACTION_VALUE] = constants.ACTION_TYPE_EMPTY


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
