import os
import warnings
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QToolButton
from action_button import ButtonActions


class ActionHandler:
    def __init__(self, main_window):
        """
        Инициализирует обработчик действий.
        :param main_window: Экземпляр главного окна (MainWindow) для доступа к его элементам и состоянию.
        """
        self.main_window = main_window
        self.ui = main_window.ui
        self.button_actions = ButtonActions(main_window)
        self.current_page_index = 0
        self._page_keys = [] # Список для хранения отсортированных ключей страниц

    def setup_pages_and_controls(self):
        """Настраивает элементы управления страницами и загружает начальную страницу."""
        # Получаем и сохраняем отсортированные ключи страниц
        self._page_keys = sorted(
            [key for key in self.main_window.config if key.startswith("page_")],
            key=lambda k: int(k.split('_')[1])
        )
        
        # Подключаем кнопки навигации по страницам
        if self.ui.NextButton_main.receivers("clicked()") > 0:
            self.ui.NextButton_main.clicked.disconnect()
        self.ui.NextButton_main.clicked.connect(self.next_page)
        
        

        if self.ui.BackButton_main.receivers("clicked()") > 0:
            self.ui.BackButton_main.clicked.disconnect()
        self.ui.BackButton_main.clicked.connect(self.previous_page)

        self.switch_to_page(1)

        # Отключаем предыдущий обработчик, только если он был подключен
        if self.ui.Editor_button.receivers("clicked()") > 0:
            self.ui.Editor_button.clicked.disconnect()
        self.ui.Editor_button.clicked.connect(self.button_actions.open_editor)

    def _update_page_label(self):
        """Обновляет текстовую метку с номером текущей страницы."""
        page_count = len(self._page_keys)
        # Проверяем, что в главном окне есть страницы, чтобы избежать деления на ноль
        # и корректно отобразить состояние, если страницы были удалены в редакторе
        ui_page_count = self.ui.Button_stackedWidget.count()
        if page_count > 0 and ui_page_count > 0:
            self.ui.Current_page_label.setText(f"{self.current_page_index + 1}/{page_count}")
        else:
            self.ui.Current_page_label.setText("0/0")


    def next_page(self):
        """Переключает на следующую страницу с зацикливанием."""
        page_count = len(self._page_keys)
        if page_count == 0:
            return
        
        next_page_index = (self.current_page_index + 1) % page_count
        self.switch_to_page(next_page_index + 1)
        print("Вперёд")

    def previous_page(self):
        """Переключает на предыдущую страницу с зацикливанием."""
        page_count = len(self._page_keys)
        if page_count == 0:
            return
            
        prev_page_index = (self.current_page_index - 1 + page_count) % page_count
        self.switch_to_page(prev_page_index + 1)
        print("Назад")

    def switch_to_page(self, page_number):
        """Переключает QStackedWidget на указанную страницу (1-индексированную) и загружает ее конфигурацию."""
        page_index = page_number - 1
        
        # Проверяем, что такая страница существует в UI
        if not (0 <= page_index < self.ui.Button_stackedWidget.count()):
            # TODO: Здесь нужна логика динамического добавления/удаления страниц в главном окне
            # Пока просто выходим, чтобы избежать ошибки
            warnings.warn(f"Попытка переключиться на страницу {page_number}, которой нет в UI главного окна.")
            return

        self.current_page_index = page_index
        self.ui.Button_stackedWidget.setCurrentIndex(page_index)


        self._update_page_label()
        
        self.load_page_config(page_index)

    def load_page_config(self, page_index):
        """Загружает конфигурацию кнопок для указанной страницы."""
        if not (0 <= page_index < len(self._page_keys)):
            return # Выходим, если индекс страницы некорректен

        current_page_key = self._page_keys[page_index]
        current_page_config = self.main_window.config.get(current_page_key, {})

        page_widget = self.ui.Button_stackedWidget.widget(page_index)
        if not page_widget:
            warnings.warn(f"Страница с индексом {page_index} не найдена в QStackedWidget.")
            return

        for i in range(1, 13):
            button_name_config = f"toolButton_{i}"
            button_name_ui = f"ToolButton_{i:02d}"
            
            button = page_widget.findChild(QToolButton, button_name_ui)
            if not button:
                continue

            # Отключаем все предыдущие соединения, чтобы избежать задваивания обработчиков
            try:
                button.clicked.disconnect()
            except TypeError:
                pass

            button_config = current_page_config.get(button_name_config, {})
            icon_path = button_config.get("icon_path")
            action_config = button_config.get("action")
            sign_text = button_config.get("sign", "")
            font_name = button_config.get("font", "")
            
            button.setText(sign_text)
            
            if font_name:
                font = QFont(font_name)
                button.setFont(font)

            if sign_text:
                button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
            else:
                button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

            if icon_path and os.path.exists(icon_path):
                button.setIcon(QIcon(icon_path))
                button.setIconSize(QSize(96, 96))
            else:
                button.setIcon(QIcon())

            if isinstance(action_config, dict):
                action_type = action_config.get("type")
                action_value = action_config.get("value")

                if not action_value:
                    continue

                new_slot = None
                if action_type == "method":
                    action_method = getattr(self.button_actions, action_value, None)
                    if not action_method:
                        # Если метод не найден в ButtonActions, ищем его в самом ActionHandler
                        action_method = getattr(self, action_value, None)

                    if action_method and callable(action_method):
                        new_slot = action_method
                
                elif action_type == "program":
                    new_slot = lambda _, p=action_value: self.button_actions.run_program(p)

                elif action_type == "shortcut":
                    new_slot = lambda _, val=action_value: self.button_actions.send_shortcut(val)
                
                if new_slot:
                    button.clicked.connect(new_slot)
