from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


class ItemRow(BoxLayout):
    firstname = StringProperty()
    middlename = StringProperty()
    lastname = StringProperty()
    

class NameList(RecycleView):
    def __init__(self, **kwargs):
        super(NameList, self).__init__(**kwargs)
        self.data = [{'firstname': 'Brent Jeffson', 'middlename': 'Flores', 'lastname': 'Florendo'}]


class MainScreen(BoxLayout):
    pass



class MultiRowApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    app = MultiRowApp()
    app.run()


















