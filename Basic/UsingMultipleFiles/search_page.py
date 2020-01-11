from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class SearchPage(BoxLayout):
    keyword_input = ObjectProperty()

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        print()

    def search(self):
        print(f"Searching -> {self.keyword_input.text}")

