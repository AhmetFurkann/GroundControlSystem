from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import Line, Rectangle, Color, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel


class CustomWidget(FloatLayout):
    back_circle_color = ListProperty([1, 1, 1, 0.5])
    back_circle_size = NumericProperty(200)

    front_circle_color = ListProperty([0, 1, 0.4, 0.5])

    front_circle_start_angle = NumericProperty(0)
    front_circle_finish_angle = NumericProperty(180)

    front_circle_width = NumericProperty(0)

    background_col = ListProperty([0, .6, .7, .5])

    def __init__(self):
        super(CustomWidget, self).__init__()
        self.front_circle_center_x = self.center_x
        self.front_circle_center_y = self.center_y

        self.front_circle_radius = max(self.size) / 2

        self.front_circle_col = Color(rgba=self.front_circle_color)
        self.front_circle_line = Line(circle=(self.front_circle_center_x,
                                              self.front_circle_center_y,
                                              self.front_circle_radius),
                                      width=8)

        self.background_rectangle = Rectangle(pos=(0, 0), size=(self.size[0], self.size[1]))

        self.canvas.add(self.front_circle_col)
        self.canvas.add(self.front_circle_line)

        self.bind(size=self.update_the_circle)
        self.bind(pos=self.update_the_circle)

        self.numeric_indicator_label = MDLabel(text="20%")
        self.numeric_indicator_label.color = [0.8, 0.8, 0.8, 1]
        self.numeric_indicator_label.font_style = "H5"
        self.numeric_indicator_label.halign = "center"
        self.numeric_indicator_label.valign = "center"

        self.add_widget(self.numeric_indicator_label)

    def update_the_circle(self, *args):
        self.update_the_rectangle()
        self.front_circle_col = self.front_circle_color
        self.front_circle_line.circle = (self.center_x,
                                         self.center_y,
                                         min(self.size) / 2 - self.front_circle_line.width)
        self.front_circle_line.width = 8

    def update_the_rectangle(self):
        self.background_rectangle.size = self.size
        self.background_rectangle.pos = self.pos
        self.numeric_indicator_label.color = [0.8, 0.8, 0.8, 1]
        self.numeric_indicator_label.pos_hint = {"center_x": .5, "center_y": .5}
