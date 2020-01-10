from functools import partial

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class HomePage(BoxLayout):
    info_btn = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.info_btn.bind(on_press=partial(app.change_page, 'Info'))


class InfoPage(BoxLayout):
    home_btn = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.home_btn.bind(on_press=partial(app.change_page, 'Home'))


class Multi2App(App):

    def build(self):
        self.screen_manager = ScreenManager()

        # create home page
        self.home_page = HomePage()
        self.create_screen(self.home_page, "Home")

        # create info page
        self.info_page = InfoPage()
        self.create_screen(self.info_page, "Info")

        return self.screen_manager

    def create_screen(self, page, name):
        screen = Screen(name=name)
        screen.add_widget(page)
        self.screen_manager.add_widget(screen)

    def change_info(self, instance):
        print(instance)
        self.screen_manager.current = "Info"

    def change_page(self, name, instance):
        self.screen_manager.current = name


if __name__ == "__main__":
    app = Multi2App()
    app.run()