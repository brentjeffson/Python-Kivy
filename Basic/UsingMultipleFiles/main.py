from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from Basic.UsingMultipleFiles.search_page import SearchPage


class LibraryPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BottomNavigator(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def page(self, page):
        app.screen_manager.current = page


class MainApp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        self.library_page = LibraryPage()
        screen = Screen(name="library")
        screen.add_widget(self.library_page)
        self.screen_manager.add_widget(screen)

        self.search_page = SearchPage(app=app)
        screen = Screen(name="search")
        screen.add_widget(self.search_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    app = MainApp()
    app.run()