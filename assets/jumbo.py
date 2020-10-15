from manimlib.imports import *
# from math import sin, cos, tan, pi

class Character(Scene):
    @staticmethod
    def create_jumbo():
        circle = Circle(radius=2, color=PINK)
        left_eye = Circle(radius=.5, color=GREEN)
        left_inner = Circle(radius=.1, color=WHITE, fill_color=WHITE, fill_opacity=1)
        right_eye = Circle(radius=.5, color=GREEN)
        right_inner = Circle(radius=.1, color=WHITE, fill_color=WHITE, fill_opacity=1)
        left_eye.shift(LEFT)
        left_inner.shift(LEFT)
        right_eye.shift(RIGHT)
        right_inner.shift(RIGHT)

        Jumbo = VGroup(*[circle, left_eye, right_eye, left_inner, right_inner])
        return Jumbo
