from manimlib.imports import *
from assets.jumbo import Character

class Shapes(Scene):
    def construct(self):
        jumbo = Character.create_jumbo()
        self.play(ShowCreation(jumbo))
