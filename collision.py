from manimlib.imports import *

class Collision(Scene):
    def construct(self):
        small_square, big_square = VGroup(
            Square(color=PURPLE, fill_color=PURPLE,
                   fill_opacity=0.5).scale(0.5).set_x(-4).set_y(-0.5),
            Square(color=BLUE, radius=2, fill_color=BLUE,
                   fill_opacity=0.5).set_x(4)
        )


        # -- Composition Scene 1 --
        self.add(small_square, big_square)
        self.wait()
        # -- Composition Scene 1 --
