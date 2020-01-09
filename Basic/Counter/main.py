from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

DEFAULT = -1


class AppRootLayout(BoxLayout):
    mCounter = 0

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     print("Initializing app...")

    def modify_counter(self, amount):
        self.mCounter += amount
        self.ids.counter.text = str(self.mCounter)

    def print(self, msg):
        print(msg)
        for id in self.ids:
            print(id)

# kivy(.kv) file must be the same as counterapp (case insensetive) with the
# 'app' part being disregarded


class CounterApp(App):
    def build(self):
        return AppRootLayout()


if __name__ == "__main__":
    CounterApp().run()

