from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import Line, Rectangle, Color, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel


class CustomWidget(FloatLayout):
    # back_circle_color = ListProperty([1, 1, 1, 0.5])
    # back_circle_size = NumericProperty(200)

    back_circle_color = ListProperty([1, 0, 0.1, 0.6])
    back_circle_start_angle = NumericProperty(0)
    back_circle_finish_angle = NumericProperty(180)
    back_circle_width = NumericProperty(0)

    front_circle_color = ListProperty([0, 1, 0.1, 0.6])
    front_circle_start_angle = NumericProperty(0)
    front_circle_finish_angle = NumericProperty(180)
    front_circle_width = NumericProperty(0)

    background_col = ListProperty([0, .6, .7, .5])

    def __init__(self):
        super(CustomWidget, self).__init__()

        """Attributes of the circle"""
        self.circle_width = 8
        self.circle_radius = min(self.size) - (self.circle_width * 2)
        self.circle_center_x = self.center_x - (self.circle_radius / 2)
        self.circle_center_y = self.center_y - (self.circle_radius / 2)

        self.back_circle_col = Color(rgba=self.back_circle_color)
        self.back_circle_line = Line(ellipsis=(self.circle_center_x,
                                               self.circle_center_y,
                                               self.circle_radius,
                                               self.circle_radius
                                               ))
        self.back_circle_line.width = self.circle_width

        self.front_circle_col = Color(rgba=self.front_circle_color)
        self.front_circle_line = Line(ellipsis=(self.circle_center_x,
                                                self.circle_center_y,
                                                self.circle_radius,
                                                self.circle_radius))
        self.front_circle_line.width = self.circle_width

        self.canvas.add(self.back_circle_col)
        self.canvas.add(self.back_circle_line)

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
        self.update_the_label()
        self.back_circle_col = self.back_circle_color
        self.front_circle_col = self.front_circle_color
        self.circle_radius = min(self.size) - (self.circle_width * 2)
        self.circle_center_x = self.center_x - (self.circle_radius / 2)
        self.circle_center_y = self.center_y - (self.circle_radius / 2)

        self.back_circle_line.ellipse = (self.circle_center_x,
                                         self.circle_center_y,
                                         self.circle_radius,
                                         self.circle_radius)
        self.back_circle_line.width = self.circle_width

    def update_the_label(self):
        self.numeric_indicator_label.color = [0.8, 0.8, 0.8, 1]
        self.numeric_indicator_label.pos_hint = {"center_x": .5, "center_y": .5}
