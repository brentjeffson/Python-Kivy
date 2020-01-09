from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from manga.Manga import Manga
from manga.consts import Sources


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    """Adds seleection and focus to the view"""


class MangaItemButton(RecycleDataViewBehavior, Button):
    def on_press(self):
        print(f'Opening {self.text}')


class SearchedList(RecycleView):
    def __init__(self, **kwargs):
        super(SearchedList, self).__init__(**kwargs)


class MainScreen(BoxLayout):
    keyword_text_input = ObjectProperty()
    searched_list = ObjectProperty()

    def search(self):
        mangas = Manga.search(self.keyword_text_input.text, Sources.MANGAKAKALOT)

        manga_list = []
        for manga in mangas:
            manga_list.append({'text': manga['title']})

        self.searched_list.data = manga_list


class MangaSearchApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    app = MangaSearchApp()
    app.run()













