import requests
import xml.dom.minidom as DOM
import xml.etree.ElementTree as ET
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

STATUS = 'status'
TRAFFIC = 'traffic'
APIS = {
    'status': '/api/monitoring/status',
    'traffic': '/api/monitoring/traffic-statistics'
}
HEADERS = {
    'Cookie': 'SessionID=joZngeuXG5GXk3zPbuqu3dXuyYJVLrDoqLmhSE7EEc1JKdVnXfIfT5YOe72Vh03y6CToNyjsmQYQ80exUCXl9kdY6Oxn94gs7pJP2JneSbRWjXW3aNG5Jp6SHh4nT1vm',
    # 'HOST': '192.168.8.1',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


class InfoScreen(BoxLayout):
    url = 'http://192.168.8.1'
    def refresh(self):
        '''fetches relevant data from pocket wifi'''
        resp = requests.get(self.url + APIS[STATUS], headers=HEADERS)
        if resp.ok:
            with open('status.xml', 'w+') as f:
                f.write(resp.text)
            doc = DOM.parse('status.xml')
            # node = doc.getElementsByTagName('code')[0]
            node = doc.getElementsByTagName('BatteryPercent')[0]

            if len(node.childNodes) > 0:
                print(str(node.childNodes[0]))


class MonitorApp(App):
    def build(self):
        return InfoScreen()


if __name__ == '__main__':
    app = MonitorApp()
    app.run()