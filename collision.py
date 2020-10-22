from manimlib.imports import *

class Collision(Scene):
    def construct(self):
        small_square, big_square = VGroup(
            Square(color=PURPLE, fill_color=PURPLE,
                   fill_opacity=0.5).scale(0.5).set_x(-4).set_y(-1.5),
            Square(color=BLUE, radius=2, fill_color=BLUE,
                   fill_opacity=0.5).set_x(4).set_y(-1)
        )
        ground = Line().scale(6).set_x(1).set_y(-2)
        wall = Line(start=UP, end=DOWN).scale(4).set_x(-5)


        # -- Composition Scene 1 --
        self.add(small_square, big_square, ground, wall)
        self.wait()
        # -- Composition Scene 1 --
