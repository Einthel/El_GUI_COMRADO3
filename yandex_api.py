
import os
from yandex_music import Client
from yandex_music.exceptions import YandexMusicError

class YandexMusicApi:
    def __init__(self, token=None):
        self.client = None
        if token:
            self.init_client(token)

    def init_client(self, token):
        """Инициализирует клиент API Яндекс.Музыки с помощью токена."""
        try:
            self.client = Client(token).init()
        except YandexMusicError as e:
            print(f"Ошибка инициализации клиента Яндекс.Музыки: {e}")
            self.client = None

    def get_track_id(self, artist_name, track_title):
        """Ищет трек по исполнителю и названию и возвращает его ID."""
        if not self.client:
            return None
        
        query = f"{artist_name} - {track_title}"
        search_result = self.client.search(query, type_='track')
        
        if search_result.tracks and search_result.tracks.results:
            # Предполагаем, что первый результат наиболее релевантен
            track = search_result.tracks.results[0]
            return f"{track.id}:{track.albums[0].id}"
        return None

    def is_track_liked(self, track_id):
        """Проверяет, лайкнут ли трек."""
        if not self.client or not track_id:
            return False
        
        liked_tracks = self.client.users_likes_tracks().tracks
        track_ids = [t.track_id for t in liked_tracks]
        
        return track_id in track_ids

    def like_track(self, track_id):
        """Ставит лайк треку."""
        if not self.client or not track_id:
            return False
        
        try:
            self.client.users_likes_tracks_add(track_id)
            print(f"Трек {track_id} добавлен в 'Мне нравится'")
            return True
        except YandexMusicError as e:
            print(f"Ошибка при добавлении лайка: {e}")
            return False

    def dislike_track(self, track_id):
        """Убирает лайк с трека."""
        if not self.client or not track_id:
            return False
        
        try:
            self.client.users_likes_tracks_remove(track_id)
            print(f"Трек {track_id} удален из 'Мне нравится'")
            return True
        except YandexMusicError as e:
            print(f"Ошибка при удалении лайка: {e}")
            return False

# Пример использования:
if __name__ == '__main__':
    # TODO: Замените 'YOUR_TOKEN' на ваш реальный токен авторизации
    # Как получить токен: https://yandex-music.readthedocs.io/en/main/token.html
    YANDEX_MUSIC_TOKEN = 'YOUR_TOKEN'
    
    api = YandexMusicApi(YANDEX_MUSIC_TOKEN)
    
    if api.client:
        # Пример поиска трека
        artist = "Nirvana"
        title = "Smells Like Teen Spirit"
        
        track_id = api.get_track_id(artist, title)
        
        if track_id:
            print(f"Найден ID трека: {track_id}")
            
            # Проверяем, лайкнут ли трек
            is_liked = api.is_track_liked(track_id)
            print(f"Трек лайкнут: {is_liked}")
            
            # Ставим лайк (если еще не стоит)
            if not is_liked:
                api.like_track(track_id)
                print(f"Состояние лайка после добавления: {api.is_track_liked(track_id)}")
            
            # Убираем лайк
            api.dislike_track(track_id)
            print(f"Состояние лайка после удаления: {api.is_track_liked(track_id)}")
        else:
            print(f"Трек '{artist} - {title}' не найден.")
