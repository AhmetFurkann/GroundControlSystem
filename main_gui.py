from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App

from kivy.core.window import Window
from gui import custom_widgets


class MainBackground(GridLayout):
    def __init__(self):
        super(MainBackground, self).__init__()
        self.cols = 2


class GroundStationGUI(App):
    def __init__(self, **kwargs):
        super(GroundStationGUI, self).__init__()
        self.video_stream_widget = custom_widgets.VideoStreamWidget()
        Window.bind(on_resize=self.video_stream_widget.update_video_border)
        Window.bind(on_show=self.video_stream_widget.update_video_border)

        self.main_window = MainBackground()
        self.main_window.add_widget(self.video_stream_widget)
        self.main_window.add_widget(Label(text="Deneme"))

    def print_window_size(self, dt):
        print(Window.size)

    def build(self):
        return self.main_window


if __name__ == "__main__":
    GroundStationGUI().run()
