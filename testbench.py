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

class EdgeAnimation(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                #            edge
            mob.scale, 0.5,
            # mob.shift can be used as well
            # mob.shift, LEFT, LEFT
            mob.to_edge, UP, {"buff":0},
            )
        self.wait()

class Arrange(Scene):
    def construct(self):
        vgroup = VGroup(
                    Square(),
                    Circle()
                )
        self.add(vgroup)
        self.wait()
        # {"buff": 0} can be used here as well
        self.play(vgroup.arrange,DOWN)
        self.wait()

class ShiftAnim(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
            mob.shift, LEFT, LEFT, LEFT,
            mob.set_color, TEAL,
            # Color, width, opacity as options here
            mob.set_stroke, None, 20,
            mob.scale, 2
        )

class VAnimation(Scene):
    def construct(self):
        rect, circ = Rectangle(), Circle()
        vgroup = VGroup(rect, circ)

        def modify(vg):
            r,c = vg
            r.set_height(1)
            vg.arrange(DOWN, buff=2)
            return vg

        self.add(vgroup)
        self.play(
            ApplyFunction(modify, vgroup)
        )
        self.wait()

# -- Rotation & Move --
class ShiftAndRotate(Animation):
    CONFIG = {
        "axis": OUT,
        "run_time": 5,
        "rate_func": smooth,
        "about_point": None,
        "about_edge": None,
    }
    def __init__(self, mobject, direction, radians, **kwargs):
        assert(isinstance(mobject, Mobject))
        digest_config(self, kwargs)
        self.mobject = mobject
        self.direction = direction
        self.radians = radians
    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.shift(alpha*self.direction)
        self.mobject.rotate(
            alpha * self.radians,
            axis = self.axis,
            about_point = self.about_point,
            about_edge = self.about_edge,
        )

class RotationAndMove(Scene):
    def construct(self):
        square1, square2 = VGroup(
            Square(color=RED), Square(color=BLUE)
        ).scale(0.5).set_x(-5)

        reference = DashedVMobject(Line(LEFT*5, RIGHT*5, color=GRAY))
        self.add(square1, square2, reference)

        self.play(
            # Red Square
            square1.rotate, 3*PI,
            square1.move_to, [5,0,0],
            # Blue Square
            ShiftAndRotate(square2, RIGHT*10, 3*PI),
            run_time = 4,
        )
        self.wait()
# -- Rotation & Move --
