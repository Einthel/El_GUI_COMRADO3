import os
import warnings
from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtCore import QSize, Qt, QObject
from PySide6.QtWidgets import QToolButton, QGraphicsDropShadowEffect, QFrame
from action_button import ButtonActions
from page_manager import PageManager
import constants
# from utils import adjust_font_size - Больше не нужно




class ActionHandler(QObject):
    def __init__(self, main_window):
        """
        Инициализирует обработчик действий.
        :param main_window: Экземпляр главного окна (MainWindow) для доступа к его элементам и состоянию.
        """
        super().__init__(main_window)
        self.main_window = main_window
        self.ui = main_window.ui
        self.button_actions = ButtonActions(main_window)
        self.page_manager = PageManager(self)
        self.page_manager.page_changed.connect(self.switch_to_page)
        self.current_page_index = 0
        self._page_keys = [] # Список для хранения отсортированных ключей страниц

        # Добавляем тень к панели виджетов
        bar_frame = self.ui.Widget_bar_frame
        if bar_frame and not bar_frame.graphicsEffect():
            bar_shadow = QGraphicsDropShadowEffect(bar_frame)
            bar_shadow.setBlurRadius(25)
            bar_shadow.setXOffset(0)
            bar_shadow.setYOffset(0)
            bar_shadow.setColor(QColor(0, 0, 0, 200))
            bar_frame.setGraphicsEffect(bar_shadow)

        # Добавляем тень к фрейму редактора
        editor_frame = self.ui.Editor_frame
        if editor_frame and not editor_frame.graphicsEffect():
            editor_shadow = QGraphicsDropShadowEffect(editor_frame)
            editor_shadow.setBlurRadius(25)
            editor_shadow.setXOffset(0)
            editor_shadow.setYOffset(0)
            editor_shadow.setColor(QColor(0, 0, 0, 200))
            editor_frame.setGraphicsEffect(editor_shadow)

        # Добавляем тень к фрейму управления страницами
        page_control_frame = self.ui.Page_control_frame
        if page_control_frame and not page_control_frame.graphicsEffect():
            page_control_shadow = QGraphicsDropShadowEffect(page_control_frame)
            page_control_shadow.setBlurRadius(25)
            page_control_shadow.setXOffset(0)
            page_control_shadow.setYOffset(0)
            page_control_shadow.setColor(QColor(0, 0, 0, 200))
            page_control_frame.setGraphicsEffect(page_control_shadow)

        # Добавляем легкую тень к кнопкам и меткам управления
        widgets_to_shadow = [
            self.ui.Editor_bar_button,
            self.ui.Change_Button,
            self.ui.Editor_button,
            self.ui.BackButton_main,
            self.ui.Current_page_label,
            self.ui.NextButton_main,
        ]
        for widget in widgets_to_shadow:
            if widget and not widget.graphicsEffect():
                shadow = QGraphicsDropShadowEffect(widget)
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80)) # Очень легкая тень
                widget.setGraphicsEffect(shadow)

        # Добавляем тень к целевым слотам для виджетов
        for i in range(1, 6):
            target_name = f"Bar_target_{i}"
            target_widget = getattr(self.ui, target_name, None)
            if target_widget and not target_widget.graphicsEffect():
                shadow = QGraphicsDropShadowEffect(target_widget)
                shadow.setBlurRadius(15)
                shadow.setXOffset(2)
                shadow.setYOffset(2)
                shadow.setColor(QColor(0, 0, 0, 80))
                target_widget.setGraphicsEffect(shadow)

    def setup_pages_and_controls(self):
        """Настраивает элементы управления страницами и загружает начальную страницу."""
        # Получаем и сохраняем отсортированные ключи страниц
        page_keys = sorted(
            [key for key in self.main_window.config if key.startswith(constants.PAGE_PREFIX)],
            key=lambda k: int(k.split('_')[1])
        )
        self.page_manager.set_page_keys(page_keys)
        
        # Подключаем кнопки навигации по страницам
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            try:
                self.ui.NextButton_main.clicked.disconnect()
            except (TypeError, RuntimeError):
                pass
        self.ui.NextButton_main.clicked.connect(self.page_manager.next)
        
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            try:
                self.ui.BackButton_main.clicked.disconnect()
            except (TypeError, RuntimeError):
                pass
        self.ui.BackButton_main.clicked.connect(self.page_manager.previous)

        self.page_manager.go_to_page(1)

        # Отключаем предыдущий обработчик, только если он был подключен
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            try:
                self.ui.Editor_button.clicked.disconnect()
            except (TypeError, RuntimeError):
                pass
        self.ui.Editor_button.clicked.connect(self.button_actions.open_editor)

        # Подключаем кнопку редактора бара
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            try:
                self.ui.Editor_bar_button.clicked.disconnect()
            except (TypeError, RuntimeError):
                pass
        self.ui.Editor_bar_button.clicked.connect(self.main_window.show_editor_bar_window)

        # === ПОДКЛЮЧЕНИЕ КНОПКИ ПЕРЕКЛЮЧЕНИЯ РЕЖИМА ===
        try:
            # Убедимся, что кнопка существует в UI
            change_button = self.ui.Change_Button
            change_button.clicked.disconnect()
        except (AttributeError, TypeError, RuntimeError):
             # AttributeError - если кнопки нет, остальное - для disconnect
            pass
        
        # Подключаем к новой функции в главном окне
        if 'change_button' in locals():
            change_button.clicked.connect(self.main_window.toggle_overlay_mode)
        # ===============================================



    def _update_page_label(self):
        """Обновляет текстовую метку с номером текущей страницы."""
        self.ui.Current_page_label.setText(self.page_manager.get_page_label_text())


    def next_page(self):
        """Переключает на следующую страницу с зацикливанием."""
        self.page_manager.next()
        print("Вперёд")

    def previous_page(self):
        """Переключает на предыдущую страницу с зацикливанием."""
        self.page_manager.previous()
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

        # Обновляем размеры иконок для новой страницы
        self.main_window.update_icon_sizes()



        self._update_page_label()
        
        self.load_page_config(page_index)

    def on_button_clicked(self):
        """Обрабатывает клик мыши по кнопке."""
        button = self.main_window.sender()
        if button:
            self.handle_button_action(button)

    def handle_button_action(self, button):
        """
        Извлекает и выполняет действие, назначенное на кнопку.
        :param button: Объект QToolButton, для которого нужно выполнить действие.
        """
        if not isinstance(button, QToolButton):
            return

        page_key = self.page_manager.get_key_for_index(self.page_manager.current_page_index)
        if not page_key:
            return
        
        page_config = self.main_window.config.get(page_key, {})
        
        button_number_str = ''.join(filter(str.isdigit, button.objectName()))
        if not button_number_str:
            return
        
        button_number = int(button_number_str)
        button_name_config = f"{constants.BUTTON_PREFIX}{button_number}"

        button_config = page_config.get(button_name_config, {})
        action_config = button_config.get(constants.KEY_ACTION, {})

        if isinstance(action_config, dict):
            action_type = action_config.get(constants.KEY_ACTION_TYPE)
            action_value = action_config.get(constants.KEY_ACTION_VALUE)

            if not action_value:
                return

            if action_type == constants.ACTION_TYPE_METHOD:
                action_method = getattr(self.button_actions, action_value, None)
                if not action_method:
                    action_method = getattr(self, action_value, None)
                if action_method and callable(action_method):
                    action_method()
            
            elif action_type == constants.ACTION_TYPE_PROGRAM:
                self.button_actions.run_program(action_value)

            elif action_type == constants.ACTION_TYPE_SHORTCUT:
                self.button_actions.send_shortcut(action_value)

    def load_page_config(self, page_index):
        """Загружает конфигурацию кнопок для указанной страницы."""
        page_key = self.page_manager.get_key_for_index(page_index)
        if not page_key:
            return # Выходим, если индекс страницы некорректен

        current_page_config = self.main_window.config.get(page_key, {})

        page_widget = self.ui.Button_stackedWidget.widget(page_index)
        if not page_widget:
            warnings.warn(f"Страница с индексом {page_index} не найдена в QStackedWidget.")
            return

        # Добавляем тень к самой странице, если ее еще нет
        if not page_widget.graphicsEffect():
            page_shadow = QGraphicsDropShadowEffect(page_widget)
            page_shadow.setBlurRadius(25)
            page_shadow.setXOffset(0)
            page_shadow.setYOffset(0)
            page_shadow.setColor(QColor(0, 0, 0, 200))
            page_widget.setGraphicsEffect(page_shadow)

        for i in range(1, 13):
            button_name_config = f"{constants.BUTTON_PREFIX}{i}"
            button_name_ui = f"ToolButton_{i:02d}"
            
            button = page_widget.findChild(QToolButton, button_name_ui)
            if not button:
                continue

            # Создаем и применяем эффект тени, если его еще нет
            if not button.graphicsEffect():
                shadow = QGraphicsDropShadowEffect(button)
                shadow.setBlurRadius(15)
                shadow.setXOffset(5)
                shadow.setYOffset(5)
                shadow.setColor(QColor(0, 0, 0, 160))
                button.setGraphicsEffect(shadow)

            button.setFixedSize(150, 150) # Фиксируем размер кнопки

            # Отключаем все предыдущие соединения, чтобы избежать задваивания обработчиков
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", RuntimeWarning)
                try:
                    button.clicked.disconnect()
                except TypeError:
                    pass

            button_config = current_page_config.get(button_name_config, {})
            icon_path = button_config.get(constants.KEY_ICON_PATH)
            sign_text = button_config.get(constants.KEY_SIGN, "")
            font_name = button_config.get(constants.KEY_FONT, "")
            font_size = button_config.get(constants.KEY_FONT_SIZE)
            
            button.setText(sign_text)
            
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
                # QIcon поддерживает SVG из коробки
                button.setIcon(QIcon(icon_path))
            else:
                button.setIcon(QIcon())

            # Подключаем все кнопки к единому обработчику кликов мыши
            button.clicked.connect(self.on_button_clicked)
