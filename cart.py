from manimlib.imports import *

class Cart(GraphScene):
    CONFIG = {
        "axes_color": BLUE,
        "function_color": PINK,
        "x_max": 5,
        "y_max": 2,
        "x_axis_width": 12,
        "x_tick_frequency": 0.5,
        "y_tick_frequency": 0.5,
        "y_axis_height": 8,
        "x_labeled_nums": range(0,6,1),
        "y_labeled_nums": range(0,3,1),
        "x_axis_label": "$\\text{t/s}$",
        "y_axis_label": "$\\text{s/m}$",
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
    }
    def construct(self):
        iterations = {
            "/aus/jo/Anim/tuts/Janim/c1t.csv": {"h": "4.5cm \\pm 0.4cm",
                                                "theta": "\\ang{1}",
                                                "m": "333g"},
            "/aus/jo/Anim/tuts/Janim/c2t.csv": {"h": "7.5cm \\pm 0.4cm",
                                                "theta": "\\ang{2}",
                                                "m": "333g"},
            "/aus/jo/Anim/tuts/Janim/c3t.csv": {"h": "10.8cm \\pm 0.4cm",
                                                "theta": "\\ang{3}",
                                                "m": "333g"},
        }
        i = 0
        for csvPath, values in iterations.items():
            print("Iteration {}".format(i))
            i += 1
            self.setup_axes(animate=True)

            path = VMobject()
            path_v = VMobject()
            coords = self.return_coords_from_csv(csvPath)
            coords_a = self.return_coords_from_csv(csvPath, options="a")
            dots = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y,z in coords])
            dots_v = VGroup(*[Dot().move_to(self.coords_to_point(x, z)) for x,y,z in coords])

            path.set_points_smoothly([*[self.coords_to_point(x,y) for x,y,z in coords]])
            path_v.set_points_smoothly([*[self.coords_to_point(x,z) for x,y,z in coords]])
            path_v.set_color(TEAL)
            path.set_color(TEAL)
            iteration = TextMobject("$\\text{Measurement {" + str(i) +"}}$")
            iteration.shift(2*UP)
            height = TextMobject("$h={}$".format(values["h"]))
            height.shift(UP)
            angle = TextMobject("$\\theta={}$".format(values["theta"]))
            angle.shift(DOWN*0.5)
            mass = TextMobject("$m={}$".format(values["m"]))
            mass.shift(UP*0.1)

            # -- Composition Scene 1 --
            self.play(Write(iteration), Write(height), Write(angle), Write(mass))
            self.play(
                iteration.shift, LEFT*2,
                height.shift, LEFT*1.5,
                angle.shift, LEFT*2.9,
                mass.shift, LEFT*2.6,
                ShowCreation(dots),
                ShowCreation(path),
                dots.set_opacity, 0,
                run_time=4
            )
            self.wait()
            self.play(
                FadeOut(dots),
                FadeOut(path),
                FadeOut(self.axes),
                FadeOut(iteration),
                FadeOut(height),
                FadeOut(angle),
                FadeOut(mass),
            )

            self.y_axis_label = "$\\text{v/ms}^{-1}$"
            self.setup_axes(animate=True)

            self.play(
                FadeIn(iteration),
                FadeIn(height),
                FadeIn(angle),
                FadeIn(mass),
                ShowCreation(dots_v),
                ShowCreation(path_v),
                dots_v.set_opacity, 0,
                run_time=4
            )
            self.wait()
            self.play(
                FadeOut(dots_v),
                FadeOut(path_v),
                FadeOut(self.axes),
                FadeOut(iteration),
                FadeOut(height),
                FadeOut(angle),
                FadeOut(mass),
            )

            self.y_axis_label = "$\\text{a/ms}^{-2}$"
            self.y_max = 1
            self.y_axis_height = 10
            self.y_labeled_nums = range(0,2,1)
            self.setup_axes(animate=True)

            path_a = VMobject()
            path_af = VMobject()
            dots_a = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y,z in coords_a])
            dots_af = VGroup(*[Dot().move_to(self.coords_to_point(x, z)) for x,y,z in coords_a])
            path_a.set_points_smoothly([*[self.coords_to_point(x,y) for x,y,z in coords_a]])
            path_af.set_points_smoothly([*[self.coords_to_point(x,z) for x,y,z in coords_a]])
            path_a.set_color(TEAL)
            path_af.set_color(PURPLE)

            if i == 3:
                self.play(
                    FadeIn(iteration),
                    FadeIn(height),
                    FadeIn(angle),
                    FadeIn(mass),
                    mass.shift, UP*1.9+RIGHT*4,
                    angle.shift, UP*2+RIGHT*4,
                    ShowCreation(dots_a),
                    ShowCreation(dots_af),
                    ShowCreation(path_a),
                    ShowCreation(path_af),
                    dots_a.set_opacity, 0,
                    dots_af.set_opacity, 0,
                    run_time=6
                )
            else:
                self.play(
                    FadeIn(iteration),
                    FadeIn(height),
                    FadeIn(angle),
                    FadeIn(mass),
                    ShowCreation(dots_a),
                    ShowCreation(dots_af),
                    ShowCreation(path_a),
                    ShowCreation(path_af),
                    dots_a.set_opacity, 0,
                    dots_af.set_opacity, 0,
                    run_time=6
                )
            self.wait(2)
            self.play(
                FadeOut(dots_a),
                FadeOut(dots_af),
                FadeOut(path_a),
                FadeOut(path_af),
                FadeOut(self.axes),
                FadeOut(iteration),
                FadeOut(height),
                FadeOut(angle),
                FadeOut(mass),
            )
            self.y_max = 2
            self.y_labeled_nums = range(0,3,1)
            self.y_axis_label = "$\\text{s/m}$"
            self.y_axis_height = 8
            # -- Composition Scene 1 --

        # -- Composition Scene 2 --
        self.setup_axes(animate=True)
        k = 0
        tmp = [TEAL, PINK, MAROON]
        paths = VGroup(*[VMobject(), VMobject(), VMobject()])
        n_group = VGroup(*[])
        dot_group = VGroup(*[])
        for csvPath, values in iterations.items():
            path = paths[k]
            coords = self.return_coords_from_csv(csvPath)
            dots = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y,z in coords])
            path.set_points_smoothly([*[self.coords_to_point(x,y) for x,y,z in coords]])
            path.set_color(tmp[k])
            n = TextMobject("$n_{}$".format(k+1))

            n_group.add(n)
            dot_group.add(dots)

            self.play(Write(n))
            self.play(
                n.shift, UP*2+RIGHT*(5.5-2*k),
                ShowCreation(dots),
                ShowCreation(path),
                dots.set_opacity, 0,
                run_time=4
            )
            self.wait()
            k += 1
        self.play(
            FadeOut(dot_group),
            FadeOut(paths),
            FadeOut(n_group),
            FadeOut(self.axes),
        )

        self.y_axis_label = "$\\text{v/ms}^{-1}$"
        self.setup_axes(animate=True)
        k = 0
        paths = VGroup(*[VMobject(), VMobject(), VMobject()])
        n_group = VGroup(*[])
        dot_group = VGroup(*[])

        for csvPath, values in iterations.items():
            path = paths[k]
            coords = self.return_coords_from_csv(csvPath)
            dots = VGroup(*[Dot().move_to(self.coords_to_point(x, z)) for x,y,z in coords])
            path.set_points_smoothly([*[self.coords_to_point(x,z) for x,y,z in coords]])
            path.set_color(tmp[k])
            n = TextMobject("$n_{}$".format(k+1))

            n_group.add(n)
            dot_group.add(dots)

            self.play(Write(n))
            self.play(
                n.shift, DOWN+RIGHT*(5.5-2*k)+UP*(0.2+k),
                ShowCreation(dots),
                ShowCreation(path),
                dots.set_opacity, 0,
                run_time=4
            )
            self.wait()
            k += 1

        self.play(
            FadeOut(dot_group),
            FadeOut(n_group),
            FadeOut(paths),
            FadeOut(self.axes),
        )

        self.y_axis_label = "$\\text{a/ms}^{-2}$"
        self.y_max = 1
        self.y_axis_height = 10
        self.y_labeled_nums = range(0,2,1)
        self.setup_axes(animate=True)
        k = 0
        paths = VGroup(*[VMobject(), VMobject(), VMobject()])
        n_group = VGroup(*[])
        dot_group = VGroup(*[])
        shift_value = [DOWN*1.8+RIGHT*5, DOWN*0.6+RIGHT*4, LEFT*2+UP*0.4]

        for csvPath, values in iterations.items():
            path = paths[k]
            coords = self.return_coords_from_csv(csvPath, options="a")
            dots = VGroup(*[Dot().move_to(self.coords_to_point(x, z)) for x,y,z in coords])
            path.set_points_smoothly([*[self.coords_to_point(x,z) for x,y,z in coords]])
            path.set_color(tmp[k])
            n = TextMobject("$n_{}$".format(k+1))

            n_group.add(n)
            dot_group.add(dots)

            self.play(Write(n))
            self.play(
                n.shift, shift_value[k],
                ShowCreation(dots),
                ShowCreation(path),
                dots.set_opacity, 0,
                run_time=4
            )
            self.wait()
            k += 1

        self.play(
            FadeOut(dot_group),
            FadeOut(n_group),
            FadeOut(paths),
            FadeOut(self.axes),
        )
        self.y_max = 2
        self.y_labeled_nums = range(0,3,1)
        self.y_axis_label = "$\\text{s/m}$"
        self.y_axis_height = 8


    def return_coords_from_csv(self,file_name, options="d"):
        import csv
        coords = []
        with open(file_name, 'r', encoding='utf-8-sig') as csvFile:
            reader = csv.reader(csvFile)
            if options == "d":
                for row in reader:
                    time, position, velocity, acceleration, curvefit = row
                    coord = [float(time),float(position), round(float(velocity), 3)]
                    coords.append(coord)
            if options == "a":
                for row in reader:
                    time, position, velocity, acceleration, curvefit = row
                    coord = [float(time),round(float(acceleration), 3), round(float(curvefit), 3)]
                    coords.append(coord)
            csvFile.close()
            return coords
