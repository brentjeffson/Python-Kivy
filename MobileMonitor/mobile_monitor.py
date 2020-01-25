import time
from threading import Thread
from functools import partial
from kivy.app import App
from kivy.properties import Clock, StringProperty
from kivy.uix.boxlayout import BoxLayout
from huawei import HuaweiApi, InvalidSessionIDError, TRAFFIC_API, STATUS_API


class InfoScreen(BoxLayout):
    battery_percentage = StringProperty()
    uploaded = StringProperty()
    downloaded = StringProperty()
    upload_rate = StringProperty()
    download_rate = StringProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Thread(target=self.fetch_data, daemon=True).start()
    
    def fetch_data(self, s=1):
        api = HuaweiApi('0fsh8d3UA1A1zWvJzENbB0QAhfCIgdRNFzJg2MHZoH6b2XzbSfrMT8qt5H0XxDxKWgEyo47qtdHcsJVtL0cc6Gbku2g2HURsXZHCadtbp4pZhubEkkZvbILK5D8fDfS4')
        while True:
            try:
                print('Fetching data...')
                sresp = api.get(STATUS_API)
                tresp = api.get(TRAFFIC_API)

            except InvalidSessionIDError:
                sresp = None
                print('Invalid Session ID')
            Clock.schedule_once(partial(self.refresh_data, sresp, tresp), 0)
            time.sleep(s)

    def refresh_data(self, sresp, tresp, _):
        '''fetches relevant data from pocket wifi'''
        battery = sresp.BatteryPercent if sresp is not None else '---'
        total_up = int(tresp.TotalUpload)
        total_down = int(tresp.TotalDownload)
        upload_rate = int(tresp.CurrentUploadRate)
        download_rate = int(tresp.CurrentDownloadRate)

        self.battery_percentage = battery
        self.upload_rate = self._process_length(upload_rate, extra="/s")
        self.download_rate = self._process_length(download_rate, extra="/s")
        self.uploaded = self._process_length(total_up)
        self.downloaded = self._process_length(total_down)

    def _process_length(self, number, choice=['B', 'MB', 'KB'], extra=''):

        dtype = choice[0]
        if len(str(number)) >= 7:
            number = number/1024/1024
            dtype = choice[1]
        elif len(str(number)) >= 4:
            number = number/1024
            dtype = choice[2]

        return f'{number:.2f}{dtype}{extra}'

class MonitorApp(App):

    def build(self):
        return InfoScreen()


if __name__ == '__main__':
    app = MonitorApp()
    app.run()