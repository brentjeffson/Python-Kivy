from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from manga.Manga import Manga
from manga.consts import Sources


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


class MangaContentApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    app = MangaContentApp()
    app.run()













