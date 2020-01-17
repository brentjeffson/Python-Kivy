from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class MainPage(BoxLayout):
    item_list = ListProperty(("Open", "Save", "Exit"))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SpinnerApp(App):

    def build(self):
        return MainPage()


if __name__ == "__main__":
    app = SpinnerApp()
    app.run()