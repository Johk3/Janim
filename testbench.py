from manimlib.imports import *
from assets.jumbo import Character

class Shapes(Scene):
    def construct(self):
        jumbo = Character(radius=0.8)
        target = np.array([DOWN, LEFT])
        jumbo_s = jumbo.create_jumbo()
        self.play(ShowCreation(jumbo_s))
        self.wait(2)
        self.play(ReplacementTransform(jumbo_s, jumbo.look(target)))
        self.wait(2)
