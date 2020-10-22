from manimlib.imports import *

class CoE(GraphScene):
    CONFIG = {
        "axes_color": BLUE,
        "x_max": 2,
        "y_max": 6,
        "x_axis_width": 18,
        "x_tick_frequency": 0.5,
        "x_labeled_nums": range(0,2,1),
        "y_labeled_nums": range(0,6,1),
        "x_axis_label": "$\\text{t/s}$",
        "y_axis_label": "$\\text{s/m}$",
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
    }
    def construct(self):
        self.setup_axes(animate=True)

        path = VMobject(label="E_k")
        path_g = VMobject()
        coords = self.return_coords_from_csv("/aus/jo/Anim/tuts/Janim/ball.csv")
        print(coords)
        coords_f = []
        dots = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y in coords])

        for i in range(len(coords)):
            coords_f.append([coords[i][0], coords[len(coords)-i-1][1]])

        dots_g = VGroup(*[Dot().move_to(self.coords_to_point(x, y)) for x,y in coords_f])
        path.set_points_smoothly([*[self.coords_to_point(x,y) for x,y in coords]])
        path.set_color(BLUE)
        path_g.set_points_smoothly([*[self.coords_to_point(x,y) for x,y in coords_f]])
        path_g.set_color(PINK)

        label_kinetic = TextMobject("$E_k$").shift(2*UP)
        label_gravitational = TextMobject("$E_g$").shift(DOWN)

        # -- Composition Scene 1 --
        self.play(ShowCreation(dots))
        self.wait(2)
        self.play(ShowCreation(path), Write(label_kinetic), dots.set_opacity, 0.5)
        self.wait(2)
        self.play(ShowCreation(dots_g))
        self.wait(2)
        self.play(ShowCreation(path_g), Write(label_gravitational), dots_g.set_opacity, 0.5)
        # -- Composition Scene 1 --

    def return_coords_from_csv(self,file_name):
        import csv
        coords = []
        with open(file_name, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                x,y = row
                coord = [float(x),float(y)]
                coords.append(coord)
        csvFile.close()
        return coords
