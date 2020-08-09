from kivy.properties import Clock
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import win32gui, win32con

WINDOW_TITLE = 'AlwaysOnTop' 


class MainApp(App):

    def build(self):
        self.title = WINDOW_TITLE
        Clock.schedule_once(self.always_on_top, 1)
        return BoxLayout()

    def always_on_top(self, _):
        # find this window       
        def windowEnumHandler(hwnd, top_windows):
            # print((hwnd, win32gui.GetWindowText(hwnd)))
            top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

        top_windows = []
        win32gui.EnumWindows(windowEnumHandler, top_windows)
        for window in top_windows:
            
            if 'AlwaysOnTop'.lower() == window[1].lower():
                rect = win32gui.GetWindowRect(window[0])
                win32gui.SetWindowPos(window[0], win32con.HWND_TOPMOST, rect[0], rect[1], rect[2], rect[3], 0)
                break
        # hwnd = win23gui.FindWindow(WINDOW_TITLE)

if __name__ == '__main__':
    app = MainApp()
    app.run()
    