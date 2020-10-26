from manimlib.imports import *

class CoE(GraphScene):
    CONFIG = {
        "axes_color": BLUE,
        "function_color": PINK,
        "x_max": 1,
        "y_max": 3,
        "x_axis_width": 18,
        "x_tick_frequency": 0.1,
        "y_tick_frequency": 0.5,
        "y_axis_height": 8,
        "x_labeled_nums": range(0,2,1),
        "y_labeled_nums": range(0,4,1),
        "x_axis_label": "$\\text{t/s}$",
        "y_axis_label": "$\\text{s/m}$",
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
    }
    def construct(self):
        self.setup_axes(animate=True)

        path = VMobject()
        coords = self.return_coords_from_csv("/Lab/Projects/Janim/coe.csv")
        dots = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y,z in coords])

        path.set_points_smoothly([*[self.coords_to_point(x,y) for x,y,z in coords]])
        path.set_color(PINK)

        label_kinetic = TextMobject("$E_k$").shift(2*UP)
        label_gravitational = TextMobject("$E_g$").shift(DOWN)

        # -- Composition Scene 1 --
        self.play(ShowCreation(dots))
        self.wait(2)
        self.play(ShowCreation(path), dots.set_opacity, 0.5)
        self.wait()
        self.play(FadeOut(dots))
        self.wait(2)
        self.play(FadeOut(path), FadeOut(self.axes))
        self.wait()
        # -- Composition Scene 1 --

        # -- Composition Scene 2 --
        self.y_max = 30
        self.y_min = -30
        # self.y_tick_frequency = 5
        self.y_bottom_tick = 30
        self.y_labeled_nums = range(-30,31,5)
        self.y_axis_height = 7
        self.y_axis_label = "$\\text{v/ms}^-1$"
        self.graph_origin = 4 * LEFT
        self.setup_axes(animate=True)

        coords_c = self.return_coords_from_csv("/Lab/Projects/Janim/coe.csv", option="c")
        path_v = VMobject()
        path_c = VMobject()
        dots_v = VGroup(*[Dot().move_to(self.coords_to_point(x, z)) for x,y,z in coords])

        path_v.set_points_smoothly([*[self.coords_to_point(x,z) for x,y,z in coords]])
        path_c.set_points_smoothly([*[self.coords_to_point(x,c) for x, c in coords_c]])
        path_v.set_color(PINK)
        path_c.set_color(GREEN)

        self.play(ShowCreation(dots_v))
        self.wait(2)
        self.play(ShowCreation(path_v), dots_v.set_opacity, 0.5)
        self.wait()
        self.play(FadeOut(dots_v))
        self.play(ShowCreation(path_c))
        self.wait(2)
        self.play(FadeOut(path_v), FadeOut(path_c), FadeOut(self.axes))
        self.wait()
        # -- Composition Scene 2 --

        # -- Composition Scene 3 --
        title = TextMobject("Conservation of Energy")
        eq = TextMobject("$mgh = \\frac{1}{2}mv^{2}$")
        eq1 = TextMobject("$\\frac{62}{1000}\\times 9.81\\times \\frac{42}{100} \
                          = \\frac{1}{2}\\times \\frac{62}{1000}\\times 2.87^{2}$")
        eq2 = TextMobject("$0.26J = 0.26J$")
        eq.set_color_by_gradient("#33ccff","#ff00ff")
        eq1.set_color_by_gradient("#33ccff","#ff00ff")
        eq2.set_color_by_gradient("#33ccff","#ff00ff")

        self.play(Write(title))
        self.play(title.shift, UP)
        self.wait()
        self.play(Write(eq))
        self.wait(2)
        self.play(ReplacementTransform(eq, eq1))
        self.wait(3)
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2)
        self.play(ShrinkToCenter(eq2), ShrinkToCenter(title))
        self.wait()
        # -- Composition Scene 3 --

        # -- Composition Scene 4 --
        self.y_max = 1
        self.y_min = 0
        self.y_bottom_tick = 0
        self.y_tick_frequency = 0.1
        self.y_labeled_nums = range(0,2,1)
        self.y_axis_height = 6
        self.y_axis_label = "$\\text{E/J}$"
        self.graph_origin = 2.5* DOWN + 4 * LEFT
        self.setup_axes(animate=True)

        path_p = VMobject()
        path_k = VMobject()
        path_t = VMobject()
        dots_p = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y in [[0, 0.26], [1, 0]]])
        dots_k = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y in [[0, 0], [1, 0.26]]])

        path_p.set_points_smoothly([*[self.coords_to_point(x,y) for x,y in [[0, 0.26], [1, 0]]]])
        path_k.set_points_smoothly([*[self.coords_to_point(x,y) for x,y in [[0, 0], [1, 0.26]]]])
        path_t.set_points_smoothly([*[self.coords_to_point(x,y) for x,y in [[0, 0.26], [1, 0.26]]]])
        path_k.set_color(PINK)
        path_t.set_color(WHITE)
        dots_k.set_color(PINK)
        path_p.set_color(BLUE)
        dots_p.set_color(BLUE)

        kinetic_lab = TextMobject("$E_k$")
        gravitational_lab = TextMobject("$E_p$")
        total_lab = TextMobject("$\\frac{1}{2}mv^2 + mgh$")

        total_lab.shift(RIGHT*2+DOWN*0.5)
        gravitational_lab.shift(DOWN+LEFT*4.5)
        kinetic_lab.shift(DOWN*2+LEFT*4.5)

        self.play(ShowCreation(dots_p), ShowCreation(dots_k))
        self.wait(2)
        self.play(ShowCreation(path_p), ShowCreation(path_k))
        self.play(Write(kinetic_lab), Write(gravitational_lab))
        self.wait(2)
        self.play(ShowCreation(path_t), Write(total_lab))
        self.wait(2)
        self.play(FadeOut(dots_p), FadeOut(dots_k), FadeOut(path_p),
                  FadeOut(path_k), FadeOut(kinetic_lab),
                  FadeOut(gravitational_lab), FadeOut(path_t),
                  FadeOut(total_lab), FadeOut(self.axes))
        # -- Composition Scene 4 --

        # -- Composition Scene 5 --
        eq = TextMobject("$E_k = \\frac{1}{2}mv^{2} + \\frac{1}{2}mr^2\\frac{V}{r}$")

        self.play(Write(eq))
        self.wait()
        # Spherical Shell  = 2/3 mR^2
        # Solid Sphere = 2/5 mR^2
        # Cylindrical Shell = mR^2
        # Solid Cylinder = 1/2 mR^2
        # -- Composition Scene 5 --


    def return_coords_from_csv(self,file_name, option="d"):
        import csv
        coords = []
        with open(file_name, 'r') as csvFile:
            reader = csv.reader(csvFile)
            if option == "d":
                for row in reader:
                    x,y,z,c = row
                    coord = [float(x),float(y), round(float(z), 2)]
                    coords.append(coord)
            if option == "c":
                for row in reader:
                    x,y,z,c = row
                    coord = [float(x),round(float(c), 2)]
                    coords.append(coord)
        csvFile.close()
        return coords
