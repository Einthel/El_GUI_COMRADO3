import os
import warnings
import copy
from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtCore import QSize, Qt, QObject, QEvent, QTimer, QTime, Signal, QThread
from PySide6.QtWidgets import QToolButton, QGraphicsDropShadowEffect, QFrame, QPushButton, QDialog, QVBoxLayout
from action_button import ButtonActions
from page_manager import PageManager
from Music_player import MusicPlayer
import constants
import control_audio
import LoadSave
from utils import apply_shadow, resource_path
from control_hwinfo import HwInfoReader
from save_message_dialog import SaveMessageDialog
from storage_widget import StorageWidget # <--- Импортируем новый виджет
# from utils import adjust_font_size - Больше не нужно




class ActionHandler(QObject):
    audio_device_changed = Signal() # Сигнал для оповещения о смене аудиоустройства

    def __init__(self, main_window):
        """
        Инициализирует обработчик действий.
        :param main_window: Экземпляр главного окна (MainWindow) для доступа к его элементам и состоянию.
        """
        super().__init__(main_window)
        self.main_window = main_window
        self.ui = main_window.ui
        self.staged_audio_settings = {} # Временное хранилище для настроек аудио
        self.staged_hwinfo_settings = {} # Временное хранилище для настроек HWINFO
        self.hwinfo_settings_dirty = False # Флаг для отслеживания несохраненных изменений
        
        # ======================================

        self.button_actions = ButtonActions(main_window, self) # Передаем self (ActionHandler)
        self.page_manager = PageManager(self)

        # === ПРОВЕРКА И ИНИЦИАЛИЗАЦИЯ НАСТРОЕК АУДИО И HWINFO ===
        self._initialize_audio_settings()
        self._initialize_hwinfo_settings()
        # =======================================================

        # === ИНИЦИАЛИЗАЦИЯ ПЛЕЕРА ===
        self.music_player = MusicPlayer(self.ui)
        # =============================
        
        # === ПОДКЛЮЧАЕМ СИГНАЛ СМЕНЫ АУДИОУСТРОЙСТВА К ПЛЕЕРУ ===
        self.audio_device_changed.connect(self.music_player.reinitialize_audio_output)
        # =======================================================

        # === ИНИЦИАЛИЗАЦИЯ ТАЙМЕРА ДЛЯ ЧАСОВ ===
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._update_time)
        self.clock_timer.start(1000)  # Обновление каждую секунду
        self._update_time() # Первоначальный вызов для отображения времени сразу
        # ======================================
        
        # === ИНИЦИАЛИЗАЦИЯ МОНИТОРИНГА СИСТЕМЫ ===
        self.hw_thread = QThread()
        self.hw_reader = HwInfoReader()
        self.hw_reader.moveToThread(self.hw_thread)
        # Подключаем сигналы
        self.hw_thread.started.connect(self.hw_reader.run_monitoring)
        self.hw_reader.cpu_data_updated.connect(self.update_cpu_display)
        self.hw_reader.gpu_data_updated.connect(self.update_gpu_display)
        self.hw_reader.memory_data_updated.connect(self.update_ram_display)
        self.hw_reader.storage_data_updated.connect(self.update_storage_display)
        self.hw_reader.available_gpus_found.connect(self._populate_hwinfo_selectors)
        # Подключаем сигналы для корректного завершения
        self.hw_thread.finished.connect(self.hw_thread.deleteLater)
        # Запускаем поток
        self.hw_thread.start()
        # =========================================

        # === КОНТЕЙНЕР ДЛЯ ДИНАМИЧЕСКИХ ВИДЖЕТОВ ХРАНИЛИЩА ===
        self.drive_widgets = [] # Список для хранения ссылок на созданные виджеты
        
        # Программно создаем layout для виджетов дисков, если он отсутствует.
        # Это делает код более устойчивым к проблемам с компиляцией .ui файла.
        if self.ui.storage_scrollAW.layout() is None:
            v_layout = QVBoxLayout(self.ui.storage_scrollAW)
            v_layout.setObjectName("storage_container_layout")
            # Устанавливаем отступы и интервалы, как на скриншоте
            v_layout.setContentsMargins(5, 5, 5, 5)
            v_layout.setSpacing(5)
            print("Layout для виджетов дисков был создан программно.")
        # ==========================================================

        self.page_manager.page_changed.connect(self.switch_to_page)
        self.current_page_index = 0
        self._page_keys = [] # Список для хранения отсортированных ключей страниц

        # === УСТАНОВКА ФИЛЬТРА СОБЫТИЙ ДЛЯ ВКЛАДОК ===
        self.ui._1Main_tab.installEventFilter(self)
        self.ui._2Button_tab.installEventFilter(self)
        self.ui._3Settings_tab.installEventFilter(self)
        self.ui._4Music_tab.installEventFilter(self)
        # ============================================

        # === ЗАПОЛНЕНИЕ ВЫПАДАЮЩИХ СПИСКОВ АУДИОУСТРОЙСТВ ===
        self._settings_audio_device_selectors()
        # ======================================================

        # === ПОДКЛЮЧЕНИЕ ОБРАБОТЧИКОВ ДЛЯ ЭЛЕМЕНТОВ НАСТРОЕК HWINFO ===
        if hasattr(self.ui, 'gpu_name_CB'):
            self.ui.gpu_name_CB.textActivated.connect(self._on_gpu_selection_changed)
        if hasattr(self.ui, 'Save_sett_HWINFO_tB'):
            self.ui.Save_sett_HWINFO_tB.clicked.connect(self._apply_hwinfo_settings)
        # ==============================================================

        # === ПОДКЛЮЧЕНИЕ ОБРАБОТЧИКОВ ДЛЯ КОМБОБОКСОВ АУДИО (ОДИН РАЗ) ===
        combo_boxes_to_connect = [
            self.ui.Main_AD_CB, self.ui.Second_AD_CB,
            self.ui.Third_AD_CB, self.ui.Fourth_AD_CB
        ]
        for i, combo_box in enumerate(combo_boxes_to_connect):
            if combo_box:
                combo_box.textActivated.connect(
                    lambda text, index=i: self._on_audio_device_changed(text, index)
                )
        # =================================================================
        
        # === ПОДКЛЮЧЕНИЕ КНОПКИ ПРИМЕНЕНИЯ НАСТРОЕК АУДИО ===
        accept_button = self.ui.Accept_AD_tB
        if accept_button:
            accept_button.clicked.connect(self._apply_audio_settings)
        # ======================================================

        # === ПОДКЛЮЧЕНИЕ КНОПКИ ПЕРЕКЛЮЧЕНИЯ АУДИО ===
        try:
            # Ищем кнопку правильного типа - QPushButton
            switch_button = self.ui.Settings_page.findChild(QPushButton, "switch_audio_butt")
            if switch_button:
                switch_button.clicked.connect(self.handle_audio_switch)
                print("Кнопка переключения аудиоустройств успешно подключена.")
            else:
                print("ВНИМАНИЕ: Кнопка 'switch_audio_butt' не найдена на странице настроек.")
        except Exception as e:
            print(f"Ошибка при подключении кнопки переключения аудио: {e}")
        # ============================================

        # Добавляем тень к фрейму редактора
        apply_shadow(self.ui.Editor_frame, blur_radius=25, color=(0, 0, 0, 200))

        # Добавляем тень к фрейму управления страницами
        apply_shadow(self.ui.Page_control_frame, blur_radius=25, color=(0, 0, 0, 200))

        # Добавляем легкую тень к кнопкам и меткам управления
        widgets_to_shadow = [
            self.ui.Change_Button,
            self.ui.Editor_button,
            self.ui.BackButton_main,
            self.ui.Current_page_label,
            self.ui.NextButton_main,
        ]
        for widget in widgets_to_shadow:
            apply_shadow(widget, blur_radius=15, x_offset=2, y_offset=2, color=(0, 0, 0, 80))

        # # === ТЕНИ ДЛЯ КНОПОК ПЛЕЕРА ===
        # player_buttons_to_shadow = [
        #     self.ui.Previous_ToolB,
        #     self.ui.Next_ToolB,
        #     self.ui.Random_ToolB,
        #     self.ui.Repeat_ToolB,
        #     self.ui.PlayPause_ToolB,
        #     self.ui.Like_ToolB,
        #     self.ui.Dis_ToolB,
        # ]
        # for button in player_buttons_to_shadow:
        #     apply_shadow(button, blur_radius=20, color=(243, 102, 168, 255)) # Используем RGBA для QColor

    def handle_audio_switch(self):
        """
        Обрабатывает нажатие на кнопку переключения аудио.
        Считывает устройства из конфига и вызывает toggle_devices.
        """
        print("="*10 + " Запрос на переключение аудио " + "="*10)
        audio_settings = self.main_window.config.get("audio_settings", {})
        
        main_device = audio_settings.get("main_device_id")
        second_device = audio_settings.get("second_device_id")

        if not main_device or not second_device:
            print("Ошибка: Не удалось найти имена основного и второго устройства в config.json.")
            print("Проверьте секцию 'audio_settings'.")
            return

        print(f"Переключение между: '{main_device}' <-> '{second_device}'")
        new_device = control_audio.toggle_devices(main_device, second_device)

        if new_device:
            print(f"Успешно переключено на: {new_device}")
        else:
            print("Переключение не удалось. Проверьте имена устройств и их доступность.")
        print("="*45)


    def _initialize_audio_settings(self):
        """
        Проверяет и обновляет конфигурацию аудио при каждом запуске.
        Заполняет пустые слоты доступными устройствами, не удаляя
        настроенные, но временно отключенные устройства.
        """
        config = self.main_window.config
        available_devices = control_audio.get_all_devices()

        # 1. Гарантируем наличие секции audio_settings
        if "audio_settings" not in config:
            config["audio_settings"] = {}
        
        audio_settings = config["audio_settings"]

        # 2. Загружаем текущие настройки из конфига (теперь 5 слотов)
        device_keys = ["main_device_id", "second_device_id", "third_device_id", "fourth_device_id", "fifth_device_id"]
        configured_devices = [audio_settings.get(key, "") for key in device_keys]

        # Создаем копию для сравнения, чтобы определить, были ли изменения
        original_configured_devices = list(configured_devices)

        # 3. Находим устройства, которые доступны, но еще не добавлены в конфиг
        configured_set = {dev for dev in configured_devices if dev}
        newly_available = [dev for dev in available_devices if dev not in configured_set]

        # 4. Заполняем пустые слоты новыми устройствами
        for i in range(len(configured_devices)):
            if not configured_devices[i] and newly_available:
                # Берем первое доступное новое устройство
                device_to_add = newly_available.pop(0)
                configured_devices[i] = device_to_add

        # 5. Обновляем конфиг новыми значениями
        for i, key in enumerate(device_keys):
            audio_settings[key] = configured_devices[i]

        # 6. Сохраняем, только если были реальные изменения
        if configured_devices != original_configured_devices:
            print("Обнаружены новые аудиоустройства. Обновление конфигурации...")
            LoadSave.save_config(config)
            print("Настройки аудио обновлены:")
            for i, dev in enumerate(configured_devices):
                print(f"  - {i+1}: '{dev}'")
        else:
            print("Аудиоустройства в норме. Обновление конфигурации не требуется.")

    def _settings_audio_device_selectors(self):
        """
        Заполняет комбобоксы на странице настроек списком доступных
        и сохраненных аудиоустройств из ВРЕМЕННОГО состояния.
        """
        # При первом запуске инициализируем временное хранилище из основного конфига
        if not self.staged_audio_settings:
            self.staged_audio_settings = copy.deepcopy(self.main_window.config.get("audio_settings", {}))

        # 1. Получаем все необходимые данные
        available_devices = control_audio.get_all_devices()
        # РАБОТАЕМ С ВРЕМЕННЫМИ НАСТРОЙКАМИ
        audio_settings = self.staged_audio_settings
        
        device_keys = ["main_device_id", "second_device_id", "third_device_id", "fourth_device_id", "fifth_device_id"]
        configured_devices = [audio_settings.get(key, "") for key in device_keys]

        # 2. Создаем уникальный список всех устройств (текущие + сохраненные, но оффлайн)
        all_known_devices = list(available_devices)
        for dev in configured_devices:
            if dev and dev not in all_known_devices:
                all_known_devices.append(f"{dev} (отключено)") # Помечаем отключенные
        
        # 3. Находим UI элементы комбобоксов
        combo_boxes = [
            self.ui.Main_AD_CB,
            self.ui.Second_AD_CB,
            self.ui.Third_AD_CB,
            self.ui.Fourth_AD_CB
        ]

        # 4. Заполняем каждый комбобокс
        for i, combo_box in enumerate(combo_boxes):
            if not combo_box:
                warnings.warn(f"Комбобокс с индексом {i} не найден в UI.")
                continue

            current_selection = configured_devices[i]

            combo_box.clear()
            combo_box.addItem("") # Добавляем пустой элемент для сброса
            combo_box.addItems(all_known_devices)

            # 5. Устанавливаем текущее значение из конфига
            # Ищем точное совпадение или помеченное как "отключено"
            index = combo_box.findText(current_selection)
            if index == -1:
                index = combo_box.findText(f"{current_selection} (отключено)")
            
            if index != -1:
                combo_box.setCurrentIndex(index)
            else:
                combo_box.setCurrentIndex(0) # Если не найдено, выбираем пустой элемент

    def _on_audio_device_changed(self, new_device_name, combo_box_index):
        """
        Обрабатывает выбор нового устройства, изменяя ВРЕМЕННОЕ состояние.
        Реализует логику "умного" обмена, если выбранное устройство
        уже используется в другом слоте.
        """
        print(f"Пользователь выбрал '{new_device_name}' для слота {combo_box_index + 1}")
        
        # Убираем суффикс "(отключено)", если он есть
        new_device_name = new_device_name.replace(" (отключено)", "").strip()

        # 1. Работаем с ВРЕМЕННЫМИ настройками
        audio_settings = self.staged_audio_settings
        device_keys = ["main_device_id", "second_device_id", "third_device_id", "fourth_device_id", "fifth_device_id"]
        
        # Получаем текущие значения из временного состояния
        current_devices = [audio_settings.get(key, "") for key in device_keys]
        
        # Старое значение, которое было в изменяемом слоте
        old_value_in_slot = current_devices[combo_box_index]
        
        # 2. Проверяем, есть ли новое устройство уже в списке (конфликт)
        conflict_index = -1
        if new_device_name: # Если выбрана не пустая строка
            try:
                conflict_index = current_devices.index(new_device_name)
            except ValueError:
                conflict_index = -1 # Конфликта нет

        # 3. Применяем логику
        if conflict_index != -1:
            # Конфликт найден! Меняем устройства местами.
            print(f"Конфликт: '{new_device_name}' уже используется в слоте {conflict_index + 1}. Меняем местами.")
            # В слот, где раньше было новое устройство, ставим старое значение из текущего слота
            current_devices[conflict_index] = old_value_in_slot
        
        # В любом случае, устанавливаем новое значение для текущего слота
        current_devices[combo_box_index] = new_device_name

        # 4. Обновляем ВРЕМЕННЫЙ словарь
        for i, key in enumerate(device_keys):
            self.staged_audio_settings[key] = current_devices[i]

        # 5. Обновляем интерфейс, чтобы показать временные изменения
        print("Временный порядок устройств:", current_devices)
        self._settings_audio_device_selectors()

    def _apply_audio_settings(self):
        """
        Применяет временные изменения настроек аудио и сохраняет их в config.json.
        """
        print("Применение настроек аудио...")
        self.main_window.config["audio_settings"] = self.staged_audio_settings
        LoadSave.save_config(self.main_window.config)
        print("Конфигурация аудио сохранена.")

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

    def eventFilter(self, watched_object, event):
        """
        Фильтрует события для отслеживаемых виджетов (вкладок).
        """
        # Проверяем, что событие - это нажатие левой кнопки мыши
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                # Проверяем, есть ли несохраненные изменения, ПЕРЕД переключением
                if watched_object != self.ui._3Settings_tab and self.ui.Main_stackW.currentWidget() == self.ui.Settings_page:
                    self._handle_unsaved_hwinfo_changes()

                # Определяем, по какому виджету кликнули, и вызываем соответствующий метод
                if watched_object == self.ui._1Main_tab:
                    self._show_main_page()
                    return True # Событие обработано
                elif watched_object == self.ui._2Button_tab:
                    self._show_button_page()
                    return True # Событие обработано
                elif watched_object == self.ui._3Settings_tab:
                    self._show_settings_page()
                    return True # Событие обработано
                elif watched_object == self.ui._4Music_tab:
                    self._show_music_page()
                    return True # Событие обработано
        
        # Для всех остальных событий вызываем стандартный обработчик
        return super().eventFilter(watched_object, event)

    def _update_time(self):
        """Обновляет LCD-дисплеи для отображения текущего времени."""
        current_time = QTime.currentTime()
        # Форматируем часы и минуты в строки
        hours = current_time.toString("hh")
        minutes = current_time.toString("mm")
        
        # Обновляем виджеты
        # Проверяем наличие виджетов перед обновлением
        if hasattr(self.ui, 'HH_lcdN') and hasattr(self.ui, 'MM_lcdN'):
            self.ui.HH_lcdN.display(hours)
            self.ui.MM_lcdN.display(minutes)

    def _show_main_page(self):
        """Переключает главный QStackedWidget на страницу 'Main_page'."""
        self.ui.Main_stackW.setCurrentWidget(self.ui.Main_page)

    def update_cpu_display(self, data: dict):
        """Обновляет метки с информацией о CPU на главной странице."""
        # Извлекаем значения, предоставляя "заглушки" на случай их отсутствия или значения None
        name = data.get('name') or 'N/A'
        clocks = data.get('clocks') or 0
        load = data.get('load') or 0
        power = data.get('power') or 0
        temp = data.get('temp') or 0

        # Обновляем текст в QLabel, форматируя значения
        if hasattr(self.ui, 'value_name_cpu'):
            self.ui.value_name_cpu.setText(name)
            self.ui.value_clocks_cpu.setText(f"{clocks:.0f} МГц")
            self.ui.value_load_cpu.setText(f"{load:.0f}%")
            self.ui.value_power_cpu.setText(f"{power:.1f} Вт")
            self.ui.value_temp_cpu.setText(f"{temp:.0f}°C")

    def update_ram_display(self, data: dict):
        """Обновляет метки и прогресс-бар с информацией о RAM на главной странице."""
        if not hasattr(self.ui, 'progressBar_ram'):
            return # Если виджетов нет, ничего не делаем

        # Извлекаем значения, предоставляя "заглушки"
        load = data.get('load', 0)
        total_gb = data.get('total', 0)
        available_gb = data.get('available', 0)

        # Обновляем виджеты
        self.ui.progressBar_ram.setValue(int(load))
        self.ui.value_totalGB_ram_lable.setText(f"{total_gb:.1f} GB")
        self.ui.value_freeGB_ram_label.setText(f"{available_gb:.1f} GB")

    def update_storage_display(self, drives_data: list):
        """
        Динамически обновляет отображение накопителей в ScrollArea.
        Очищает старые виджеты и создает новые на основе свежих данных.
        """
        # --- 1. Очистка старых виджетов ---
        # Удаляем виджеты из layout и помечаем их для удаления сборщиком мусора
        for widget in self.drive_widgets:
            self.ui.storage_scrollAW.layout().removeWidget(widget)
            widget.deleteLater()
        self.drive_widgets.clear() # Очищаем список ссылок

        # --- 2. Создание и добавление новых виджетов ---
        for data in drives_data:
            # Создаем новый экземпляр нашего "умного" виджета
            widget = StorageWidget()
            # Заполняем его данными
            widget.setData(data)
            # Добавляем его в layout внутри ScrollArea
            self.ui.storage_scrollAW.layout().addWidget(widget)
            # Сохраняем ссылку на него для последующей очистки
            self.drive_widgets.append(widget)

    def update_gpu_display(self, data: dict):
        """Обновляет метки с информацией о GPU на главной странице."""
        if not hasattr(self.ui, 'value_name_gpu'):
             return

        # Словарь для сопоставления имен виджетов и форматированных данных
        # Используем .get() для безопасного извлечения
        vram_total_gb = data.get('vram_total', 0) / 1024 if data.get('vram_total') else 0
        
        update_map = {
            'value_name_gpu': data.get('name', 'N/A'),
            'value_temp_gpu': f"{data.get('temp', 0):.0f}°C",
            'value_temHot_gpu': f"{data.get('temp_hotspot', 0):.0f}°C",
            'value_load_gpu': f"{data.get('load', 0):.0f}%",
            'value_clocks_gpu': f"{data.get('clocks', 0):.0f} МГц",
            'value_power_gpu': f"{data.get('power', 0):.1f} Вт",
            'value_fanRPM_gpu': f"{data.get('fan_rpm', 0):.0f} RPM",
            'value_fanPer_gpu': f"{data.get('fan_percent', 0):.0f}%",
            'value_vram_total_gpu': f"{vram_total_gb:.1f} ГБ",
            'value_vramUMb_gpu': f"{data.get('vram_used', 0):.0f} МБ",
            'value_vramUPer_gpu': f"{data.get('vram_percent', 0):.0f}%"
        }

        # Обновляем текст для каждого QLabel
        for widget_name, value in update_map.items():
            if hasattr(self.ui, widget_name):
                label = getattr(self.ui, widget_name)
                label.setText(str(value))

    def _show_button_page(self):
        """Переключает главный QStackedWidget на страницу 'Button_page'."""
        self.ui.Main_stackW.setCurrentWidget(self.ui.Button_page)

    def _show_settings_page(self):
        """Переключает главный QStackedWidget на страницу 'Settings_page'."""
        self.ui.Main_stackW.setCurrentWidget(self.ui.Settings_page)

    def _show_music_page(self):
        """Переключает главный QStackedWidget на страницу 'Music_page'."""
        self.ui.Main_stackW.setCurrentWidget(self.ui.Music_page)

    def _update_page_label(self):
        """Обновляет текстовую метку с номером текущей страницы."""
        self.ui.Current_page_label.setText(self.page_manager.get_page_label_text())


    def _initialize_hwinfo_settings(self):
        """Проверяет наличие и создаёт секцию hwinfo_settings в конфиге."""
        config = self.main_window.config
        if "hwinfo_settings" not in config:
            print("Секция 'hwinfo_settings' не найдена. Создание...")
            config["hwinfo_settings"] = {
                "selected_gpu_name": "",
                "fan_cpu_sensor": "",
                "pump_cpu_sensor": "",
                "storage_sensor": "",
                "system_drive_letter": ""
            }
        # Загружаем настройки во временное хранилище
        self.staged_hwinfo_settings = copy.deepcopy(config.get("hwinfo_settings", {}))
        self.hwinfo_settings_dirty = False
        print("Настройки HWINFO инициализированы.")

    def _populate_hwinfo_selectors(self, gpu_names):
        """Заполняет комбобокс выбора GPU и устанавливает начальное значение."""
        if not hasattr(self.ui, 'gpu_name_CB'):
            return
        #print(f"Найденные GPU: {gpu_names}")
        self.ui.gpu_name_CB.clear()
        self.ui.gpu_name_CB.addItems(gpu_names)

        # Определяем GPU для мониторинга
        saved_gpu = self.main_window.config.get("hwinfo_settings", {}).get("selected_gpu_name")
        target_gpu = ""

        if saved_gpu and saved_gpu in gpu_names:
            self.ui.gpu_name_CB.setCurrentText(saved_gpu)
            target_gpu = saved_gpu
            print(f"Загружен сохраненный GPU: {target_gpu}")
        elif gpu_names:
            target_gpu = gpu_names[0]
            self.ui.gpu_name_CB.setCurrentText(target_gpu)
            # Так как это выбор по умолчанию, сохраним его сразу, чтобы при следующем запуске он уже был.
            self._on_gpu_selection_changed(target_gpu) 
            self._apply_hwinfo_settings() # Сохраняем начальный выбор
            print(f"GPU не был выбран, установлен по умолчанию: {target_gpu}")
        
        # Сразу передаем имя в поток мониторинга
        if target_gpu:
            self.hw_reader.target_gpu_name = target_gpu
    
    def _on_gpu_selection_changed(self, gpu_name):
        """Обновляет временные настройки при выборе GPU в комбобоксе."""
        print(f"Временно выбран GPU: {gpu_name}")
        self.staged_hwinfo_settings["selected_gpu_name"] = gpu_name
        self.hwinfo_settings_dirty = True

    def _apply_hwinfo_settings(self):
        """Применяет и сохраняет настройки HWINFO."""
        print("Сохранение настроек HWINFO...")
        self.main_window.config["hwinfo_settings"] = self.staged_hwinfo_settings
        LoadSave.save_config(self.main_window.config)
        self.hwinfo_settings_dirty = False
        
        # Передаем новое имя в поток и сбрасываем флаг отладки
        new_gpu_name = self.staged_hwinfo_settings.get("selected_gpu_name")
        if new_gpu_name:
            self.hw_reader.target_gpu_name = new_gpu_name
            self.hw_reader._gpu_debug_printed = False # Сбрасываем для повторного вывода
            print(f"Мониторинг переключен на GPU: {new_gpu_name}")

        print("Настройки HWINFO сохранены.")

    def _handle_unsaved_hwinfo_changes(self):
        """Проверяет и обрабатывает несохраненные изменения в настройках HWINFO."""
        if not self.hwinfo_settings_dirty:
            return # Нет изменений, можно продолжать

        dialog = SaveMessageDialog(self.main_window)
        result = dialog.exec()

        if result == QDialog.Accepted:
            self._apply_hwinfo_settings()
        else: # Rejected
            # Откатываем изменения
            self.staged_hwinfo_settings = copy.deepcopy(self.main_window.config.get("hwinfo_settings", {}))
            # Обновляем UI до сохраненного значения
            saved_gpu = self.staged_hwinfo_settings.get("selected_gpu_name")
            if hasattr(self.ui, 'gpu_name_CB'):
                self.ui.gpu_name_CB.setCurrentText(saved_gpu)
            self.hwinfo_settings_dirty = False
            print("Изменения настроек HWINFO отменены.")


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
        apply_shadow(page_widget, blur_radius=25, color=(0, 0, 0, 200))

        for i in range(1, 13):
            button_name_config = f"{constants.BUTTON_PREFIX}{i}"
            button_name_ui = f"ToolButton_{i:02d}"
            
            button = page_widget.findChild(QToolButton, button_name_ui)
            if not button:
                continue

            # Создаем и применяем эффект тени, если его еще нет
            apply_shadow(button, blur_radius=15, x_offset=5, y_offset=5, color=(0, 0, 0, 160))

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

            if icon_path:
                # --- ИСПРАВЛЕНИЕ ПУТИ К ИКОНКАМ ---
                # 1. Проверяем, начинается ли путь со старого префикса "icons/"
                if icon_path.startswith("icons/"):
                    # Заменяем его на новый, правильный префикс
                    icon_path = icon_path.replace("icons/", "resources/icons/", 1)
                
                # 2. Оборачиваем путь в resource_path для корректной работы
                full_icon_path = resource_path(icon_path)

                # 3. Устанавливаем иконку, только если файл реально существует
                if os.path.exists(full_icon_path):
                    button.setIcon(QIcon(full_icon_path))
                else:
                    print(f"Предупреждение: Файл иконки не найден по пути: {full_icon_path}")
                    button.setIcon(QIcon()) # Устанавливаем пустую иконку
            else:
                button.setIcon(QIcon())
            # --- КОНЕЦ ИСПРАВЛЕНИЯ ---

            # Подключаем все кнопки к единому обработчику кликов мыши
            button.clicked.connect(self.on_button_clicked)
