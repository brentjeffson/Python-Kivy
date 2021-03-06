import io
from functools import partial
import concurrent.futures

import requests
import threading
from kivy.app import App

from kivy.properties import ObjectProperty, Clock
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.image import Image as CoreImage
from manga.constants import Sources
from manga.manga import MangaScraper


class MangaItemButton(RecycleDataViewBehavior, Button):

    def on_press(self):
        print(f'Opening {self.text} -> {self.url}')
        app.info_page.load_info(self.url)
        app.screen_manager.current = "Info"


class ChapterItemButton(RecycleDataViewBehavior, Button):

    def on_press(self):
        print(f"Opening {self.text}")
        threading.Thread(target=app.image_page.retrieve_images, args=[self.chapter], daemon=True).start()
        app.screen_manager.current = "Chapter"


class SearchedList(RecycleView):

    def __init__(self, **kwargs):
        super(SearchedList, self).__init__(**kwargs)


class ChapterList(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ImageList(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ImagePage(BoxLayout):
    image_list = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def retrieve_images(self, chapter):
        resp = requests.get(chapter.url)
        if resp.ok:
            markup = resp.text

            list_dict_img_bytes = []
            image_urls = MangaScraper.find_images(markup, Sources.MANGAKAKALOT)

            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = [executor.submit(self.retrieve_image, url) for url in image_urls]

                for future in concurrent.futures.as_completed(results):
                    print("Complete")
                    Clock.schedule_once(partial(self.add_retrieved_image, future.result()[0], future.result()[1]), 0)

    def retrieve_image(self, url):
        split_url = url.split('/')
        filename = split_url[len(split_url)-1]
        resp = requests.get(url)
        return resp.content, filename

    def add_retrieved_image(self, image_byte, filename, *_):

        texture = CoreImage(io.BytesIO(image_byte), ext=f"{filename.split('.')[1]}").texture
        self.image_list.data.append({"texture": texture, "allow_stretch": True, "size": (600, 800)})


class InfoPage(BoxLayout):
    title_label = ObjectProperty()
    chapter_list = ObjectProperty()
    home_btn = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Info Page")

    def load_info(self, url):

        resp = requests.get(url)
        scraper = MangaScraper(resp.text, Sources.MANGAKAKALOT)
        manga = scraper.manga

        self.title_label.text = manga.title

        chapters = []
        for chapter in manga.chapters:
            chapters.append({"text": chapter.title, "chapter": chapter})
        self.chapter_list.data = chapters

    def home(self):
        app.screen_manager.current = "Main"


class MainPage(BoxLayout):
    keyword_text_input = ObjectProperty()
    searched_list = ObjectProperty()

    def search(self):
        print(f"Searching -> {self.keyword_text_input.text}")
        Clock.schedule_once(self.focus_search, 0.2)
        t1 = threading.Thread(target=self.s, daemon=True)
        t1.start()

    def focus_search(self, _):
        self.keyword_text_input.focus = True

    def s(self):
        mangas = MangaScraper.search(self.keyword_text_input.text, Sources.MANGAKAKALOT)

        manga_list = []
        for manga in mangas:
            if Sources.MANGAKAKALOT in manga.url:
                manga_list.append({'text': manga.title, 'url': manga.url})

        self.searched_list.data = manga_list
        print("Searched Done.")


class MangaSearchApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.main_page = MainPage()
        self.create_screen(self.main_page, "Main")

        self.info_page = InfoPage()
        self.create_screen(self.info_page, "Info")

        self.image_page = ImagePage()
        self.create_screen(self.image_page, "Chapter")

        return self.screen_manager

    def create_screen(self, page, name):
        screen = Screen(name=name)
        screen.add_widget(page)
        self.screen_manager.add_widget(screen)


if __name__ == '__main__':
    app = MangaSearchApp()
    app.run()













