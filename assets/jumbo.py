from manimlib.imports import *
# from math import sin, cos, tan, pi

class Character(Scene):
    def __init__(self, radius=2, color_top=PINK, color_outer_eye=GREEN, color_inner_eye=WHITE):
        self.circle = Circle(radius=radius, color=color_top)
        self.left_eye = Circle(radius=radius*0.25, color=color_outer_eye)
        self.left_inner = Circle(radius=radius*0.05, color=color_inner_eye, fill_color=color_inner_eye, fill_opacity=1)
        self.right_eye = Circle(radius=radius*0.25, color=color_outer_eye)
        self.right_inner = Circle(radius=radius*0.05, color=color_inner_eye, fill_color=color_inner_eye, fill_opacity=1)
        self.left_eye.shift(LEFT*(radius*0.5))
        self.left_inner.shift(LEFT*(radius*0.5))
        self.right_eye.shift(RIGHT*(radius*0.5))
        self.right_inner.shift(RIGHT*(radius*0.5))
        self.radius = radius

    def create_jumbo(self):
        Jumbo = VGroup(*[self.circle, self.left_eye, self.right_eye, self.left_inner, self.right_inner])
        return Jumbo

    def look(self, target):
        Jumbo = VGroup(*[self.circle, self.left_eye, self.right_eye, self.left_inner, self.right_inner])
        for coord in target:
            self.left_inner.shift((self.radius*0.5)*0.1*coord)
            self.right_inner.shift((self.radius*0.5)*0.1*coord)
        return Jumbo
