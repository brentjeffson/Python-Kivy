from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'info'
        Button:
            text: 'Quit'

<InfoScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'main'
""")


class MainScreen(Screen):
    pass


class InfoScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name="main"))
sm.add_widget(InfoScreen(name="info"))


class MultiApp(App):

    def build(self):
        return sm


if __name__ == "__main__":
    app = MultiApp()
    app.run()