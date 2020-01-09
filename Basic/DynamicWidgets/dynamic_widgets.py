from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class RootLayout(BoxLayout):
    mCounter = 0

    def add_button(self):
        self.mCounter += 1
        self.add_widget(Button(text=str(self.mCounter)))


class DynamicApp(App):
    def build(self):
        return RootLayout()


if __name__ == '__main__':
    DynamicApp().run()
