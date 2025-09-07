import sys
import os
import importlib
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QListWidget, QMenu, QWidget
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QIcon, QPixmap, QAction

# Импортируем сгенерированный класс интерфейса
from ui_Editor_bar import Ui_Editor_bar_Window
from Bar_widget import ClockWidget, VolumeWidget, MusicWidget, TimerWidget
from LoadSave import save_bar_config, load_bar_config
from widget_loader import load_and_display_widgets
import constants

class EditorBarWindow(QMainWindow):
    # Сигнал, который будет отправлен при сохранении конфигурации
    config_saved = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Создаем экземпляр UI
        self.ui = Ui_Editor_bar_Window()
        self.ui.setupUi(self)

        self._widget_to_move = None
        self._original_target_stylesheets = {}

        self._setup_ui_and_events()
        self._connect_signals()

        # Первоначальная загрузка конфигурации
        load_and_display_widgets(self.ui, is_editor=True)

    def _setup_ui_and_events(self):
        """Sets up UI components and connects event handlers."""
        # --- Настройка списка виджетов ---
        self.ui.Ready_Widget_list.setViewMode(QListWidget.ViewMode.IconMode)
        self.ui.Ready_Widget_list.setFlow(QListWidget.Flow.LeftToRight)
        self.ui.Ready_Widget_list.setDragDropMode(QListWidget.DragDropMode.DragOnly)
        self.ui.Ready_Widget_list.setIconSize(QSize(128, 64))
        self.ui.Ready_Widget_list.setWordWrap(True)

        # --- Заполнение списка виджетов ---
        from widget_registry import WIDGET_REGISTRY
        self.ui.Ready_Widget_list.clear()

        for class_name, WidgetClass in WIDGET_REGISTRY.items():
            try:
                widget_instance = WidgetClass()
                widget_instance.setAttribute(Qt.WA_DontShowOnScreen, True)
                widget_instance.show()

                pixmap = QPixmap(widget_instance.size())
                pixmap.fill(Qt.GlobalColor.transparent)
                widget_instance.render(pixmap)
                widget_instance.deleteLater()
                
                item = QListWidgetItem()
                item.setIcon(QIcon(pixmap))
                item.setText(class_name)
                item.setData(Qt.ItemDataRole.UserRole, class_name)
                self.ui.Ready_Widget_list.addItem(item)
            except Exception as e:
                print(f"Could not create preview for widget '{class_name}': {e}")
        
        # --- Настройка Drag & Drop и Контекстного меню ---
        self.drop_targets = [
            self.ui.Bar_editor_target_1,
            self.ui.Bar_editor_target_2,
            self.ui.Bar_editor_target_3,
            self.ui.Bar_editor_target_4,
            self.ui.Bar_editor_target_5,
        ]
        
        for target in self.drop_targets:
            self._original_target_stylesheets[target.objectName()] = target.styleSheet()
            
            target.setAcceptDrops(True)
            target.dragEnterEvent = self.bar_frame_dragEnterEvent
            target.dropEvent = lambda event, frame=target: self.on_widget_dropped(event, frame)
            
            target.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            target.customContextMenuRequested.connect(lambda pos, frame=target: self.show_target_context_menu(pos, frame))
            
            target.mousePressEvent = lambda event, frame=target: self.target_mouse_press_event(event, frame)

    def _connect_signals(self):
        """Connects button signals to their slots."""
        self.ui.save_bar_button.clicked.connect(self._save_bar_layout)
        self.ui.load_bar_button.clicked.connect(lambda: load_and_display_widgets(self.ui, is_editor=True))

    def bar_frame_dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def on_widget_dropped(self, event, target_frame):
        # Проверяем, что слот пуст
        if target_frame.findChild(QWidget):
             print("Этот слот уже занят. Выберите другой.")
             event.ignore()
             return

        class_name = event.source().currentItem().data(Qt.ItemDataRole.UserRole)
        if not class_name:
            return

        from widget_registry import get_widget_class
        WidgetClass = get_widget_class(class_name)
        if not WidgetClass:
            print(f"Ошибка: Не удалось найти класс '{class_name}' для создания виджета.")
            return
            
        parent_widget = target_frame
        new_widget = WidgetClass(parent_widget)
        new_widget.setWindowFlags(Qt.Widget)
        new_widget.move(0, 0)
        new_widget.show()
        
        if hasattr(new_widget, 'setDraggable'):
            new_widget.setDraggable(False)
            
        # Устанавливаем objectName для последующей идентификации
        new_widget.setObjectName(class_name)
        
        print(f"Виджет '{class_name}' создан внутри '{parent_widget.objectName()}'")
        event.accept()

    def target_mouse_press_event(self, event, frame):
        """Обрабатывает клик мыши по целевому фрейму."""
        # Если есть виджет для перемещения и кликнули левой кнопкой
        if self._widget_to_move and event.button() == Qt.MouseButton.LeftButton:
            # Сначала всегда сбрасываем подсветку
            self.reset_all_targets_stylesheet()
            
            # Проверяем, что целевой фрейм пуст
            if not frame.findChild(QWidget):
                # Перемещаем виджет
                self._widget_to_move.setParent(frame)
                self._widget_to_move.move(0, 0)
                self._widget_to_move.show()
                print(f"Виджет '{self._widget_to_move.objectName()}' перемещен в '{frame.objectName()}'")
            else:
                print("Этот слот уже занят. Выберите другой.")
                # Если слот занят, возвращаем виджет на место
                self._widget_to_move.parent().layout().addWidget(self._widget_to_move)

            # В любом случае сбрасываем состояние перемещения
            self._widget_to_move = None
            
            event.accept()
            return

        # Вызываем стандартный обработчик для других случаев
        super(type(frame), frame).mousePressEvent(event)



    def show_target_context_menu(self, position, frame):
        """Показывает контекстное меню для целевого фрейма."""
        # Ищем дочерний виджет в этом фрейме
        child_widget = frame.findChild(QWidget)
        
        # Если виджета нет, меню не показываем
        if not child_widget:
            return

        menu = QMenu(self)
        
        # --- Действие "Удалить" ---
        delete_action = QAction("Удалить", self)
        delete_action.triggered.connect(lambda: self._delete_widget(child_widget))
        menu.addAction(delete_action)
        
        # --- Действие "Переместить" ---
        move_action = QAction("Переместить", self)
        move_action.triggered.connect(lambda: self._prepare_to_move_widget(child_widget))
        menu.addAction(move_action)

        # Показываем меню в глобальных координатах
        menu.exec(frame.mapToGlobal(position))

    def _delete_widget(self, widget):
        """Удаляет указанный виджет."""
        if widget:
            print(f"Удаление виджета '{widget.objectName()}' из '{widget.parent().objectName()}'")
            widget.deleteLater()

    def _prepare_to_move_widget(self, widget):
        """Готовит виджет к перемещению."""
        if widget:
            print(f"Подготовка к перемещению виджета '{widget.objectName()}'. Кликните на новый пустой слот.")
            self._widget_to_move = widget
            # Визуально выделяем пустые слоты для перемещения
            self.set_targets_stylesheet("""
                QFrame {
                    border: 2px dashed #00FF00;
                    background-color: rgba(0, 255, 0, 50);
                }
            """)

    def set_targets_stylesheet(self, style):
        """Устанавливает стиль для всех ПУСТЫХ целевых фреймов."""
        for target in self.drop_targets:
            if not target.findChild(QWidget):
                target.setStyleSheet(style)

    def reset_all_targets_stylesheet(self):
        """Сбрасывает стиль для ВСЕХ целевых фреймов, восстанавливая исходный."""
        for target in self.drop_targets:
            original_style = self._original_target_stylesheets.get(target.objectName(), "")
            target.setStyleSheet(original_style)

    def _save_bar_layout(self):
        """Собирает и сохраняет текущую конфигурацию панели в новом формате."""
        layout_data = {}
        for target in self.drop_targets:
            # Ищем только прямых потомков QWidget
            child_widget = target.findChild(QWidget, options=Qt.FindDirectChildrenOnly)

            if child_widget:
                widget_type = child_widget.objectName()
                
                # Базовые настройки для всех виджетов
                settings = {
                    constants.KEY_WIDGET_POSITION: [child_widget.x(), child_widget.y()]
                }
                
                # Добавляем специфичные настройки для ClockWidget
                if widget_type == "ClockWidget":
                    # TODO: В будущем эти значения должны браться из элементов UI редактора
                    settings["font_size"] = 20
                    settings["font_weight"] = "bold"
                    settings["alignment"] = "right"

                # Собираем финальную структуру для виджета
                layout_data[target.objectName()] = {
                    constants.KEY_WIDGET_TYPE: widget_type,
                    constants.KEY_WIDGET_SETTINGS: settings
                }
        
        save_bar_config(layout_data)
        print(f"Конфигурация панели сохранена: {layout_data}")
        self.config_saved.emit()

    def _load_bar_layout(self):
        """Загружает и применяет конфигурацию панели, используя новый формат."""
        load_and_display_widgets(self.ui, is_editor=True)


# Этот блок нужен для возможности отдельного запуска и тестирования окна
if __name__ == '__main__':
    # Эта часть нужна, чтобы PyInstaller и другие сборщики "видели" эти классы
    # и включали их в финальную сборку. Без этого динамическое создание
    # по имени класса может не сработать после компиляции.
    _ = ClockWidget()
    _ = VolumeWidget()
    _ = MusicWidget()
    _ = TimerWidget()

    app = QApplication(sys.argv)
    window = EditorBarWindow()
    window.show()
    sys.exit(app.exec())
