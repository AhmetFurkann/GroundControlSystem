from kivy.graphics import Line, Color
from kivy.core.window import Window
from kivy.uix.image import Image


class VideoStreamWidget(Image):
    def __init__(self):
        super(VideoStreamWidget, self).__init__()
        self.source = r"C:\Users\Ahmet\PycharmProjects\GroundStation\images\video_stream.png"
        self.window_width = Window.size[0]
        self.window_height = Window.size[1]

    def update_video_border(self, dt, width, height):
        self.canvas.remove_group("border")

        bottom_line_x_1 = 0
        bottom_line_y_1 = 0

        bottom_line_x_2 = round(width / 2)
        bottom_line_y_2 = 0

        right_line_x_1 = bottom_line_x_2
        right_line_y_1 = bottom_line_y_2

        right_line_x_2 = bottom_line_x_2
        right_line_y_2 = height

        top_line_x_1 = right_line_x_2
        top_line_y_1 = right_line_y_2

        top_line_x_2 = bottom_line_x_1
        top_line_y_2 = right_line_y_2

        left_line_x_1 = top_line_x_2
        left_line_y_1 = top_line_y_2

        left_line_x_2 = bottom_line_x_1
        left_line_y_2 = bottom_line_y_2

        self.canvas.add(Color(0, 0.3, 0.3, 1, group="border"))
        self.canvas.add(Line(points=[bottom_line_x_1, bottom_line_y_1, bottom_line_x_2, bottom_line_y_2,
                                     right_line_x_1, right_line_y_1, right_line_x_2, right_line_y_2,
                                     top_line_x_1, top_line_y_1, top_line_x_2, top_line_y_2,
                                     left_line_x_1, left_line_y_1, left_line_x_2, left_line_y_2], width=5,
                             group="border"))
