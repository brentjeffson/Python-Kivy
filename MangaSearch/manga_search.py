import requests
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from manga.constants import Sources
from manga.manga import MangaScraper


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    """Adds selection and focus to the view"""


class MangaItemButton(RecycleDataViewBehavior, Button):

    def on_press(self):
        print(f'Opening {self.text} -> {self.url}')
        app.info_page.load_info(self.url)
        app.screen_manager.current = "Info"


class SearchedList(RecycleView):
    def __init__(self, **kwargs):
        super(SearchedList, self).__init__(**kwargs)


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
            chapters.append({"text": chapter.title})
        self.chapter_list.data = chapters

    def home(self):
        app.screen_manager.current = "Main"


class ChapterList(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainPage(BoxLayout):
    keyword_text_input = ObjectProperty()
    searched_list = ObjectProperty()

    def search(self):
        mangas = MangaScraper.search(self.keyword_text_input.text, Sources.MANGAKAKALOT)

        manga_list = []
        for manga in mangas:
            if Sources.MANGAKAKALOT in manga['url']:
                manga_list.append({'text': manga['title'], 'url': manga['url']})

        self.searched_list.data = manga_list


class MangaSearchApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.main_page = MainPage()
        self.create_screen(self.main_page, "Main")

        self.info_page = InfoPage()
        self.create_screen(self.info_page, "Info")

        return self.screen_manager

    def create_screen(self, page, name):
        screen = Screen(name=name)
        screen.add_widget(page)
        self.screen_manager.add_widget(screen)


if __name__ == '__main__':
    app = MangaSearchApp()
    app.run()













