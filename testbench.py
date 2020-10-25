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

class RotateWithPath(Scene):
    def construct(self):
        square1, square2 = VGroup(
            Square(color=PURPLE), Square(color=BLUE),
        ).scale(0.5).set_x(-5)

        path = Line(LEFT*5, RIGHT*5, stroke_opacity=0.5)
        path.points[1:3] += UP*2

        square2.save_state()

        def update_rotate_move(mob, alpha):
            square2.restore()
            square2.move_to(path.point_from_proportion(alpha))
            square2.rotate(3*PI*alpha)

        self.add(square1, square2, path)
        self.play(
            # Purple Square
            MoveAlongPath(square1, path),
            Rotate(square1, 2*PI/3, about_point=square1.get_center()),
            # Blue Square
            UpdateFromAlphaFunc(square2, update_rotate_move),
            run_time=10
        )

class UpdateValueTracker2(Scene):
    CONFIG={
        "line_1_color":ORANGE,
        "line_2_color":PINK,
        "lines_size":3.5,
        "theta":PI/2,
        "increment_theta":PI/2,
        "final_theta":PI,
        "radius":0.7,
        "radius_color":YELLOW,
    }
    def construct(self):
        # Set objets
        theta = ValueTracker(self.theta)
        line_1= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_1_color)
        line_2= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_2_color)

        line_2.rotate(theta.get_value(),about_point=ORIGIN)
        line_2.add_updater(
                lambda m: m.set_angle(
                                    theta.get_value()
                                )
            )

        angle= Arc(
                    radius=self.radius,
                    start_angle=line_1.get_angle(),
                    angle =line_2.get_angle(),
                    color=self.radius_color
            )

        # Show the objects

        self.play(*[
                ShowCreation(obj)for obj in [line_1,line_2,angle]
            ])

        # Set update function to angle

        angle.add_updater(
                    lambda m: m.become(
                            Arc(
                                radius=self.radius,
                                start_angle=line_1.get_angle(),
                                angle =line_2.get_angle(),
                                color=self.radius_color
                            )
                        )
            )
        # Remember to add the objects again to the screen
        # when you add the add_updater method.
        self.add(angle)

        self.play(theta.increment_value,self.increment_theta)
        # self.play(theta.set_value,self.final_theta)

        self.wait()

class UpdateFunctionWithDt1(Scene):
    CONFIG={
        "amp": 2.3,
        "t_offset": 0,
        "rate": TAU/4,
        "sine_graph_config":{
            "x_min": -TAU/2,
            "x_max": TAU/2,
            "color": RED,
            },
        "wait_time":15,
    }

    def construct(self):

        def update_curve(c, dt):
            rate = self.rate * dt
            c.become(self.get_sin_graph(self.t_offset + rate))
            # Every frame, the t_offset increase rate / fps
            self.t_offset += rate


        c = self.get_sin_graph(0)

        self.play(ShowCreation(c))
        print(f"fps: {self.camera.frame_rate}")
        print(f"dt: {1 / self.camera.frame_rate}")
        print(f"rate: {self.rate / self.camera.frame_rate}")
        print(f"cy_start: {c.points[0][1]}")
        print(f"cy_end:   {c.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

        c.add_updater(update_curve)
        self.add(c)

        # The animation begins
        self.wait(4)

        c.remove_updater(update_curve)
        self.wait()

        print(f"cy_start:  {c.points[0][1]}")
        print(f"cy_end:    {c.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

    def get_sin_graph(self, dx):
        c = FunctionGraph(
                lambda x: self.amp * np.sin(x - dx),
                **self.sine_graph_config
                )
        return c

class UpdateNumber(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-1,x_max=1)
        triangle = RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        decimal = DecimalNumber(
                0,
                num_decimal_places=3,
                include_sign=True,
                unit="\\rm cm", # Change this with None
            )

        decimal.add_updater(lambda d: d.next_to(triangle, UP*0.1))
        decimal.add_updater(lambda d: d.set_value(triangle.get_center()[0]))
        #       You can get the value of decimal with: .get_value()

        self.add(number_line,triangle,decimal)

        self.play(
                triangle.shift,RIGHT*2,
                rate_func=there_and_back, # Change this with: linear,smooth
                run_time=5
            )

        self.wait()

class UpdateCurve(Scene):
    def construct(self):
        def f(dx=1):
            return FunctionGraph(lambda x: 2*np.exp(-2 * (x - dx) ** 2))

        c = f()
        axes=Axes(y_min=-3, y_max=3)

        def update_curve(c, alpha):
            dx = interpolate(1, 4, alpha)
            c_c = f(dx)
            c.become(c_c)

        self.play(ShowCreation(axes), ShowCreation(c))
        self.wait()
        self.play(UpdateFromAlphaFunc(c,update_curve),rate_func=there_and_back,run_time=4)
        self.wait()

class InterpolateColorScene(Scene):
    def construct(self):
        shape = Square(fill_opacity=1).scale(2)
        shape.set_color(RED)

        def update_color(mob,alpha):
            dcolor = interpolate(0,mob.alpha_color,alpha)
            mob.set_color(self.interpolate_color_mob(mob.initial_state,shape.new_color,dcolor))

        self.add(shape)
        self.change_init_values(shape,TEAL,0.5)
        self.play(UpdateFromAlphaFunc(shape,update_color))

        self.change_init_values(shape,PINK,0.9)
        self.play(UpdateFromAlphaFunc(shape,update_color))
        self.wait()

    def interpolate_color_mob(self,mob,color,alpha):
        return interpolate_color(mob.get_color(),color,alpha)

    def change_init_values(self,mob,color,alpha):
        mob.initial_state = mob.copy()
        mob.new_color = color
        mob.alpha_color = alpha

class AddUpdaterFail(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        self.play(dot.shift,UP*2)
        self.wait()

# -- Transformations --
class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


class CoordScreen(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        dot = Dot([1, 1, 0])
        self.add(screen_grid)
        self.play(FadeIn(dot))
        self.wait()
# -- Transformations --
