import concurrent.futures
import threading
from functools import partial

import io
import requests
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.app import App
from kivy.core.image import Image as CoreImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

Builder.load_file("layout.kv")


class MainPage(BoxLayout):
    image = ObjectProperty()
    image_byte = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_image()
        # t1 = threading.Thread(target=self.load_image, daemon=True)
        # t1.start()

    def image_ready(self, img_bytes):
        image = CoreImage(io.BytesIO(img_bytes), ext="jpg")
        self.image.texture = image.texture

    def load_image(self):
        print("Retrieving Image...")
        url = 'https://s6.mkklcdnv6.com/mangakakalot/s1/saikin_kono_sekai_wa_watashi_dake_no_mono_ni_narimashita/chapter_85_limited_to_one_end/9.jpg'
        resp = requests.get(url)
        split_url = url.split('/')
        filename = split_url[len(split_url)-1]

        self.image_ready(resp.content)


class MainApp(App):

    def build(self):
        return MainPage()


if __name__ == "__main__":
    app = MainApp()
    app.run()






