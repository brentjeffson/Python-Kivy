from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

ITEMS = [
    {'text': "Chicken Lauriat"},
    {'text': "SS Chicken Lauriat"},
    {'text': "SS Fish Lauriat"},
    {'text': "Beef Chaofan"},
]


class MainScreen(BoxLayout):
    order_name_input = ObjectProperty()
    order_amount_input = ObjectProperty()
    order_list_view = ObjectProperty()

    def add_order(self):
        self.order_list_view.data.append({'text': self.order_name_input.text})


class OrderList(RecycleView):
    def __init__(self, **kwargs):
        super(OrderList, self).__init__(**kwargs)
        self.data = ITEMS


class OrderApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    app = OrderApp()
    app.run()