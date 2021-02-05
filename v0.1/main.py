from kivy.graphics import Line, Rectangle, Color
from kivy.graphics.texture import Texture

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image

from kivy.core.window import Window
from kivy.config import Config
from kivymd.app import MDApp

from custom_widget_1 import CustomWidget
from PIL import Image as PILImage
import numpy as np
import cv2

Config.set('graphics', 'width', '1252')
Config.set('graphics', 'height', '556')
Config.write()


class CamStreamLayout(Image):
    def __init__(self, **kwargs):
        super(CamStreamLayout, self).__init__(**kwargs)
        self.size_hint_x = .6
        self.bind(size=self.update)

    def update(self, *args):
        frame = PILImage.open("image.png")
        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        width = int(self.size[0])
        height = int(self.size[1])
        dim = (width, height)
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        buffer = cv2.flip(frame, 0)
        buffer = buffer.tostring()
        image_texture = Texture.create(
            size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        print("Frame Shape: ", frame.shape[0])
        print("Frame Shape: ", frame.shape[1])
        image_texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.texture = image_texture


class IndicatorLayout(GridLayout):
    def __init__(self, **kwargs):
        super(IndicatorLayout, self).__init__(**kwargs)
        self.size_hint_x = .4
        self.cols = 2
        self.spacing = 15
        self.padding = [0, 10, 0, 10]

        self.bg_color = Color(rgba=(.4, .4, .4, .8))
        self.background = Rectangle(pos=(0, 0), size=self.size)
        self.canvas.add(self.bg_color)
        self.canvas.add(self.background)

        self.bind(size=self.update_background)

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size


class TopContainerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(TopContainerLayout, self).__init__(**kwargs)
        self.size_hint_y = .7
        self.padding = 10
        self.bg_color = Color(rgba=(.4, .4, .4, .8))
        self.background = Rectangle(pos=(0, 0), size=self.size)
        self.canvas.add(self.bg_color)
        self.canvas.add(self.background)

        self.bind(size=self.update)

    def update(self, *args):
        print("Window Size: ", Window.size)
        self.background.pos = self.pos
        self.background.size = self.size


class BottomContainerLayout(BoxLayout):
    def __init__(self):
        super(BottomContainerLayout, self).__init__()
        self.size_hint_y = .3

        self.bg_color = Color(rgba=(.4, .4, .4, 1))
        self.background = Rectangle(pos=(0, 0), size=self.size)
        self.canvas.add(self.bg_color)
        self.canvas.add(self.background)

        self.bind(size=self.update)

    def update(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size


class BackgroundLayout(BoxLayout):
    orientation = "vertical"


class FirstApp(MDApp):
    def build(self):
        background = BackgroundLayout()

        top_container = TopContainerLayout()
        bottom_container = BottomContainerLayout()

        information_label = MDLabel(text="Controller Field",
                                    theme_text_color="Primary",
                                    font_style="H2",
                                    halign="center")

        cam_stream_container = CamStreamLayout()

        indicator_container = IndicatorLayout()

        indicator_1 = CustomWidget()
        indicator_2 = CustomWidget()
        indicator_3 = CustomWidget()
        indicator_4 = CustomWidget()
        indicator_5 = CustomWidget()
        indicator_6 = CustomWidget()

        indicator_container.add_widget(indicator_1)
        indicator_container.add_widget(indicator_2)
        indicator_container.add_widget(indicator_3)
        indicator_container.add_widget(indicator_4)
        indicator_container.add_widget(indicator_5)
        indicator_container.add_widget(indicator_6)

        top_container.add_widget(cam_stream_container)
        top_container.add_widget(indicator_container)

        bottom_container.add_widget(information_label)

        background.add_widget(top_container)
        background.add_widget(bottom_container)

        return background


if __name__ == "__main__":
    FirstApp().run()
