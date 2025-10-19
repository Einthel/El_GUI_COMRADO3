import json
import random
import sys
import traceback
from typing import Any

import requests

from PySide6.QtCore import (
    QUrl, Qt, QBuffer, QByteArray, QObject, Signal, QRunnable, QThreadPool, QEvent, QTimer
)
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QLabel, QVBoxLayout, QGraphicsOpacityEffect
from yandex_music import Client

# ui_MusicPlayer больше не нужен
from LoadSave import load_config


class WorkerSignals(QObject):
    """
    Определяет сигналы, доступные из рабочего потока.
    """
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)


class DownloaderWorker(QRunnable):
    """
    Рабочий поток для скачивания данных по URL.
    """
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.signals = WorkerSignals()

    def run(self):
        try:
            response = requests.get(self.url, timeout=15)
            response.raise_for_status()
            result = response.content
        except Exception as e:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MusicPlayer(QObject): # Изменено с QWidget на QObject
    """
    Класс-контроллер музыкального плеера, который использует API Яндекс.Музыки.
    """
    def __init__(self, ui, parent=None): # Конструктор теперь принимает ui главного окна
        """
        Инициализатор класса MusicPlayer.
        Загружает конфигурацию, инициализирует API клиент и плеер.
        """
        super().__init__(parent)
        self.ui = ui # Используем переданный ui

        # Пул потоков для выполнения фоновых задач
        self.threadpool = QThreadPool()
        print(f"Максимальное количество потоков: {self.threadpool.maxThreadCount()}")

        # API клиент для взаимодействия с Яндекс.Музыкой
        self.client = None
        # Медиа-плеер для воспроизведения аудио
        self.player = None
        # Объект для вывода звука
        self.audio_output = None

        # Список загруженных треков
        self.tracks = []
        # Индекс текущего трека в списке self.tracks
        self.current_track_index = -1
        # Буфер для хранения загруженного трека
        self.track_buffer = QBuffer()
        # Множество ID понравившихся треков для быстрого поиска
        self.liked_track_ids = set()
        # Храним оригинальный pixmap для качественного масштабирования
        self.cover_pixmap = None

        # Состояние плеера (играет / пауза)
        self.is_playing = False
        
        # Режим повтора треков ("off", "all", "one")
        self.repeat_mode = "off"
        # Режим случайного воспроизведения
        self.shuffle_mode = False

        # --- УПРОЩЕННЫЙ ПОДХОД ДЛЯ ФИКСИРОВАННОГО РАЗМЕРА ---
        # 1. Удаляем компоновку из Cover_Frame, если она была создана в Designer.
        current_layout = self.ui.Cover_Frame.layout()
        if current_layout is not None:
            while current_layout.count():
                item = current_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(self.ui.Cover_Frame)
            current_layout.deleteLater()

        # 2. Создаем QLabel для обложки.
        self.cover_label = QLabel(self.ui.Cover_Frame)
        self.cover_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 3. Вызываем метод для первоначальной расстановки виджетов.
        self._update_cover_widgets()
        
        # --- КОНЕЦ ИЗМЕНЕНИЙ ---

        self.load_config_and_init() # Заменяем старые вызовы на один

    def _update_cover_widgets(self):
        """
        Масштабирует обложку и центрирует кнопку Play/Pause для фиксированного размера.
        """
        # 1. QLabel с обложкой должен занимать все пространство фрейма
        self.cover_label.setGeometry(self.ui.Cover_Frame.rect())

        # 2. Масштабируем картинку, если она есть
        if self.cover_pixmap:
            scaled_pixmap = self.cover_pixmap.scaled(
                self.cover_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.cover_label.setPixmap(scaled_pixmap)

        # # 3. Центрируем кнопку
        # button = self.ui.PlayPause_ToolB
        # cover_size = self.ui.Cover_Frame.size()
        # button_size = button.size()
        # x = (cover_size.width() - button_size.width()) / 2
        # y = (cover_size.height() - button_size.height()) / 2
        # button.move(int(x), int(y))
        # 
        # # 4. Выдвигаем кнопку на передний план, чтобы она была поверх обложки
        # button.raise_()

    def load_config_and_init(self):
        """
        Загружает конфигурацию, используя централизованную функцию,
        инициализирует клиент и плеер, и запускает загрузку треков.
        """
        # 1. Загружаем конфиг через LoadSave.py
        config = load_config()
        self.token = config.get('yandex_music', {}).get('token')
        
        # 2. Инициализируем клиент
        self.init_yandex_music_client()
        
        # 3. Инициализируем плеер
        self.init_player()

        # 4. Настраиваем соединения
        self.setup_connections()

        # 5. Запускаем загрузку треков
        self.fetch_liked_tracks()

    def init_yandex_music_client(self):
        """
        Инициализирует клиент API Яндекс.Музыки с использованием токена.
        """
        if self.token and self.token != "YOUR_TOKEN_HERE":
            try:
                self.client = Client(self.token).init()
            except Exception as e:
                print(f"Не удалось инициализировать клиент Яндекс.Музыки: {e}")
                self.client = None
        else:
            print("Токен Яндекс.Музыки не найден в config.json. Функционал плеера будет ограничен.")
            self.client = None

    def init_player(self):
        """
        Инициализирует QMediaPlayer для воспроизведения аудио.
        """
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        self.ui.PlayPause_ToolB.setCheckable(True)
        self.ui.PlayPause_ToolB.setProperty("playMode", "off")

        # --- Анимация прозрачности для Play/Pause ---
        self.opacity_effect = QGraphicsOpacityEffect(self.ui.PlayPause_ToolB)
        self.ui.PlayPause_ToolB.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0.8) # 80% прозрачности

        self.opacity_timer = QTimer(self)
        self.opacity_timer.setSingleShot(True)
        self.opacity_timer.timeout.connect(self.reset_button_opacity)
        # ----------------------------------------
        
        # Устанавливаем начальное свойство для кнопки повтора
        self.ui.Repeat_ToolB.setProperty("repeatMode", self.repeat_mode)
        self.ui.Repeat_ToolB.setCheckable(True)
        # Делаем кнопку случайного выбора нажимаемой
        self.ui.Random_ToolB.setCheckable(True)
        # Устанавливаем начальное свойство для кнопки "Лайк"
        self.ui.Like_ToolB.setCheckable(True)
        self.ui.Like_ToolB.setProperty("likeMode", "off")


    def setup_connections(self):
        """
        Настраивает сигналы и слоты для элементов управления плеером.
        """
        # Кнопки управления воспроизведением
        self.ui.PlayPause_ToolB.clicked.connect(self.toggle_play_pause)
        self.ui.Next_ToolB.clicked.connect(self.next_track)
        self.ui.Previous_ToolB.clicked.connect(self.previous_track)
        self.ui.Repeat_ToolB.clicked.connect(self.toggle_repeat_mode)
        self.ui.Random_ToolB.clicked.connect(self.toggle_shuffle_mode)

        # Сигналы медиа-плеера
        self.player.positionChanged.connect(self.update_position)
        self.player.mediaStatusChanged.connect(self.on_media_status_changed)
        self.player.errorOccurred.connect(self.handle_player_error)
        self.player.playbackStateChanged.connect(self.handle_playback_state_changed)

        # Кнопка "Лайк"
        self.ui.Like_ToolB.clicked.connect(self.on_like_clicked)
        # Кнопка "Дизлайк"
        self.ui.Dis_ToolB.clicked.connect(self.on_dislike_clicked)

    def toggle_shuffle_mode(self):
        """
        Переключает режим случайного воспроизведения.
        """
        self.shuffle_mode = not self.shuffle_mode
        self.ui.Random_ToolB.setChecked(self.shuffle_mode)
        
        # Обновляем свойство для QSS
        self.ui.Random_ToolB.setProperty("randomMode", "on" if self.shuffle_mode else "off")

        # Перерисовываем кнопку, чтобы применились стили из QSS
        self.ui.Random_ToolB.style().unpolish(self.ui.Random_ToolB)
        self.ui.Random_ToolB.style().polish(self.ui.Random_ToolB)
        
        print(f"Режим случайного воспроизведения изменен на: {self.shuffle_mode}")

    def toggle_repeat_mode(self):
        """
        Переключает режим повтора: нет -> плейлист -> один трек.
        """
        if self.repeat_mode == "off":
            self.repeat_mode = "all"
        elif self.repeat_mode == "all":
            self.repeat_mode = "one"
        else:  # self.repeat_mode == "one"
            self.repeat_mode = "off"

        print(f"Режим повтора изменен на: {self.repeat_mode}")

        # Обновляем свойство для QSS
        self.ui.Repeat_ToolB.setProperty("repeatMode", self.repeat_mode)

        # Обновляем состояние checked
        is_checked = self.repeat_mode != "off"
        self.ui.Repeat_ToolB.setChecked(is_checked)

        # Перерисовываем кнопку, чтобы применились стили из QSS
        self.ui.Repeat_ToolB.style().unpolish(self.ui.Repeat_ToolB)
        self.ui.Repeat_ToolB.style().polish(self.ui.Repeat_ToolB)

    def fetch_liked_tracks(self):
        """
        Получает список понравившихся треков пользователя из Яндекс.Музыки
        и загружает первый трек, если список не пуст.
        """
        if not self.client:
            print("Клиент Яндекс.Музыки не инициализирован. Невозможно загрузить треки.")
            return

        try:
            print("Загрузка понравившихся треков...")
            liked_tracks_list = self.client.users_likes_tracks()
            if liked_tracks_list and liked_tracks_list.tracks:
                self.tracks = liked_tracks_list.tracks
                # Сохраняем ID всех понравившихся треков
                self.liked_track_ids = {t.id for t in self.tracks}
                self.current_track_index = 0
                self.load_track(self.current_track_index)
                print(f"Загружено {len(self.tracks)} треков. Текущий трек: {self.ui.Track_label.text()}")
            else:
                print("Понравившиеся треки не найдены.")
        except Exception as e:
            print(f"Ошибка при загрузке понравившихся треков: {e}")

    def load_track(self, track_index):
        """
        Загружает информацию о треке в UI (обложка, название, исполнитель)
        и подготавливает плеер к воспроизведению.

        :param track_index: Индекс трека в списке self.tracks.
        """
        if not self.tracks or not (0 <= track_index < len(self.tracks)):
            print("Ошибка: неверный индекс трека или список треков пуст.")
            return

        # Останавливаем воспроизведение и очищаем старые данные
        self.player.stop()
        self.cover_pixmap = None # Очищаем старую обложку
        self.cover_label.clear() # И из QLabel тоже
        if self.track_buffer.isOpen():
            self.track_buffer.close()
        
        self.current_track_index = track_index
        track_short = self.tracks[self.current_track_index]

        try:
            # Получаем полную информацию о треке
            track = track_short.fetch_track()

            # Обновляем имя исполнителя и название трека
            artists = ', '.join(artist.name for artist in track.artists)
            self.ui.Artist_label.setText(artists)
            self.ui.Track_label.setText(track.title)

            # Обновляем статус кнопки "Лайк"
            self.update_like_status(track)

            # Обновляем длительность
            duration_ms = track.duration_ms
            self.ui.Length_track_bar.setMaximum(duration_ms)
            self.ui.Right_Time_label.setText(self.format_duration(duration_ms))

            # Запускаем асинхронную загрузку обложки
            cover_url = track.get_cover_url(size='400x400')
            if cover_url:
                self.start_download(cover_url, self.set_cover)

            # Запускаем асинхронную загрузку трека
            download_info = track.get_download_info()
            direct_link = download_info[0].get_direct_link()
            self.start_download(direct_link, self.set_track_data)

        except Exception as e:
            print(f"Ошибка при загрузке информации о треке: {e}")

    def reinitialize_audio_output(self):
        """
        Переинициализирует аудиовыход плеера, чтобы подхватить
        измененное системное устройство по умолчанию.
        """
        print("Переинициализация аудиовыхода плеера...")
        
        # 1. Запоминаем текущее состояние
        current_position = self.player.position()
        was_playing = self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState
        
        # 2. Останавливаем и сбрасываем текущий вывод
        self.player.stop()
        
        # 3. Создаем и устанавливаем новый аудиовыход
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # 4. Восстанавливаем источник данных (буфер с треком)
        # setSourceDevice сам откроет буфер, если он закрыт
        if self.track_buffer.data():
             self.player.setSourceDevice(self.track_buffer)
        
        # 5. Восстанавливаем позицию
        self.player.setPosition(current_position)
        
        # 6. Возобновляем воспроизведение, если оно было активно
        if was_playing:
            self.player.play()
        
        print("Аудиовыход успешно переинициализирован.")

    def update_like_status(self, track):
        """
        Обновляет состояние кнопки "Лайк" в зависимости от статуса трека.
        :param track: Полный объект трека.
        """
        is_liked = track.id in self.liked_track_ids
        
        # Временно блокируем сигналы, чтобы избежать случайного срабатывания
        self.ui.Like_ToolB.blockSignals(True)
        self.ui.Like_ToolB.setChecked(is_liked)
        self.ui.Like_ToolB.blockSignals(False)

    def on_like_clicked(self):
        """
        Обрабатывает нажатие на кнопку "Лайк".
        Отправляет запрос на добавление/удаление трека из понравившихся.
        """
        if not self.client or self.current_track_index < 0:
            print("Клиент не инициализирован или трек не выбран.")
            # Вернуть кнопку в исходное состояние, если клик был случайным
            self.ui.Like_ToolB.setChecked(not self.ui.Like_ToolB.isChecked())
            return

        is_liked = self.ui.Like_ToolB.isChecked()
        track_id = self.tracks[self.current_track_index].id
        final_is_liked = is_liked

        try:
            if is_liked:
                print(f"Добавление трека {track_id} в понравившиеся...")
                self.client.users_likes_tracks_add(track_id)
                self.liked_track_ids.add(track_id)
                print("Трек успешно добавлен.")
            else:
                print(f"Удаление трека {track_id} из понравившихся...")
                self.client.users_likes_tracks_remove(track_id)
                self.liked_track_ids.remove(track_id)
                print("Трек успешно удален.")
        except Exception as e:
            print(f"Ошибка при обновлении статуса 'лайка': {e}")
            # В случае ошибки возвращаем кнопке ее предыдущее состояние
            final_is_liked = not is_liked
            self.ui.Like_ToolB.blockSignals(True)
            self.ui.Like_ToolB.setChecked(final_is_liked)
            self.ui.Like_ToolB.blockSignals(False)
        
        # Обновляем свойство и стиль в соответствии с финальным состоянием
        self.ui.Like_ToolB.setProperty("likeMode", "on" if final_is_liked else "off")
        self.ui.Like_ToolB.style().unpolish(self.ui.Like_ToolB)
        self.ui.Like_ToolB.style().polish(self.ui.Like_ToolB)

    def on_dislike_clicked(self):
        """
        Обрабатывает нажатие на кнопку "Дизлайк".
        Удаляет трек из понравившихся и переключает на следующий.
        """
        if not self.client or self.current_track_index < 0:
            print("Клиент не инициализирован или трек не выбран.")
            return

        track_id_to_remove = self.tracks[self.current_track_index].id
        index_to_remove = self.current_track_index

        try:
            print(f"Удаление трека {track_id_to_remove} из понравившихся...")
            self.client.users_likes_tracks_remove(track_id_to_remove)
            self.liked_track_ids.discard(track_id_to_remove) # Используем discard для безопасности
            print("Трек успешно удален с сервера.")

            # Удаляем трек из локального списка
            self.tracks.pop(index_to_remove)
            print("Трек удален из локального плейлиста.")

            if not self.tracks:
                print("Плейлист пуст.")
                # Тут можно добавить логику очистки UI
                self.player.stop()
                return

            # Переключаемся на следующий трек
            # Индекс остается тем же, так как список сдвинулся
            if self.current_track_index >= len(self.tracks):
                self.current_track_index = 0
            
            self.is_playing = True
            self.load_track(self.current_track_index)

        except Exception as e:
            print(f"Ошибка при 'дизлайке' трека: {e}")


    def start_download(self, url, callback):
        """
        Запускает воркер для скачивания URL в фоновом потоке.

        :param url: URL для скачивания.
        :param callback: Функция, которая будет вызвана с результатом.
        """
        worker = DownloaderWorker(url)
        worker.signals.result.connect(callback)
        worker.signals.error.connect(lambda err: print(f"Ошибка скачивания {url}: {err}"))
        self.threadpool.start(worker)

    def set_cover(self, image_data):
        """
        Слот для установки загруженной обложки в UI.
        """
        self.cover_pixmap = QPixmap()
        self.cover_pixmap.loadFromData(image_data)
        # Вызываем метод для масштабирования и установки картинки
        self._update_cover_widgets()

    def set_track_data(self, track_data_bytes):
        """
        Слот для установки загруженных данных трека в плеер.
        """
        # Устанавливаем данные в буфер
        byte_array = QByteArray(track_data_bytes)
        self.track_buffer.setData(byte_array)
        self.track_buffer.open(QBuffer.OpenModeFlag.ReadOnly)
        self.player.setSourceDevice(self.track_buffer)

        # Если трек был переключен кнопкой, запускаем воспроизведение
        if self.is_playing:
            self.player.play()

    def reset_button_opacity(self):
        """Возвращает кнопке Play/Pause исходную прозрачность."""
        if self.opacity_effect:
            self.opacity_effect.setOpacity(0.6)

    def toggle_play_pause(self):
        """
        Переключает состояние воспроизведения (play/pause) и запускает анимацию.
        """
        # Запускаем анимацию: делаем кнопку непрозрачной и ставим таймер
        if self.opacity_effect:
            self.opacity_effect.setOpacity(1.0)
        if self.opacity_timer:
            self.opacity_timer.start(2000)

        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.is_playing = False
        else:
            self.player.play()
            self.is_playing = True
        
    def next_track(self):
        """
        Переключает на следующий трек в списке.
        """
        self._change_track(1)

    def previous_track(self):
        """
        Переключает на предыдущий трек в списке.
        """
        self._change_track(-1)

    def _change_track(self, direction: int):
        """
        Изменяет текущий трек на следующий или предыдущий.

        :param direction: 1 для следующего трека, -1 для предыдущего.
        """
        if self.tracks:
            self.is_playing = True # Устанавливаем флаг, что нужно играть после загрузки
            
            if self.shuffle_mode:
                if len(self.tracks) > 1:
                    next_index = self.current_track_index
                    while next_index == self.current_track_index:
                        next_index = random.randint(0, len(self.tracks) - 1)
                    self.current_track_index = next_index
                # Если трек один, он просто перезагрузится
            else:
                self.current_track_index = (self.current_track_index + direction) % len(self.tracks)
            
            self.load_track(self.current_track_index)

    def update_position(self, position):
        """
        Обновляет положение ползунка и метку текущего времени.

        :param position: Текущая позиция воспроизведения в миллисекундах.
        """
        self.ui.Length_track_bar.setValue(position)
        self.ui.Left_Time_label.setText(self.format_duration(position))

    def on_media_status_changed(self, status):
        """
        Обрабатывает изменение статуса медиа.
        Автоматически переключает трек, когда текущий заканчивается,
        в зависимости от режима повтора.
        """
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.is_playing = True  # Чтобы следующий трек сразу играл

            if self.repeat_mode == "one":
                print("Повтор текущего трека.")
                self.player.setPosition(0)
                self.player.play()

            elif self.repeat_mode == "all":
                print("Переключение на следующий трек (повтор плейлиста).")
                self.next_track()
            
            elif self.repeat_mode == "off":
                # Проверяем, не последний ли это трек
                if self.current_track_index < len(self.tracks) - 1:
                    print("Переключение на следующий трек (повтор выключен).")
                    self.next_track()
                else:
                    print("Достигнут конец плейлиста. Воспроизведение остановлено.")
                    self.is_playing = False
                    self.player.pause()
                    self.player.setPosition(0)
                    self.update_position(0)
                    self.ui.PlayPause_ToolB.setChecked(False)

    def handle_player_error(self, error, error_string):
        """
        Обрабатывает ошибки, возникающие в QMediaPlayer.
        """
        print(f"Ошибка плеера: {error} - {error_string}")

    def handle_playback_state_changed(self, state):
        """
        Отслеживает изменение состояния воспроизведения плеера.
        """
        print(f"Состояние плеера изменилось: {state}")
        # Обновляем состояние кнопки Play/Pause в соответствии с состоянием плеера
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.ui.PlayPause_ToolB.setChecked(True)
            self.ui.PlayPause_ToolB.setProperty("playMode", "on")
        else:
            self.ui.PlayPause_ToolB.setChecked(False)
            self.ui.PlayPause_ToolB.setProperty("playMode", "off")

        # Перерисовываем кнопку, чтобы применились стили из QSS
        self.ui.PlayPause_ToolB.style().unpolish(self.ui.PlayPause_ToolB)
        self.ui.PlayPause_ToolB.style().polish(self.ui.PlayPause_ToolB)

    def format_duration(self, ms):
        """
        Форматирует длительность из миллисекунд в строку "М:СС".

        :param ms: Длительность в миллисекундах.
        :return: Строка в формате "минуты:секунды".
        """
        total_seconds = ms // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02}"
