from kivy.app import App
from kivy.uix.widget import Widget


class CustomWidget(Widget):
    pass


class CustomApp(App):

    def build(self):
        return CustomWidget()


if __name__ == '__main__':
    CustomApp().run()

