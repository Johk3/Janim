from manimlib.imports import *

class Swing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": PINK,
        "axes_color": BLUE
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label="x^{3}")
        bob = Dot(self.coords_to_point(1.5, self.func_to_graph(1.5)))

        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.add_foreground_mobject(bob)
        self.wait(2)

    def func_to_graph(self, x):
        return(x**3)

    def fall(self, bob):
        pass
