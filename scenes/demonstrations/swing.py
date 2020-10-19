from manimlib.imports import *

class Swing(GraphScene):
    """Demonstrating a swing of a point across a graph"""
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
        bob = Dot(self.coords_to_point(1.5, self.func_to_graph(1.5))).scale(2)
        bob.save_state()

        def update_bob(bob, alpha):
            bob.restore()
            bob.move_to(func_graph.point_from_proportion(1-alpha))
            bob.rotate(3*PI*alpha)

        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.add(bob)
        self.play(
            UpdateFromAlphaFunc(bob, update_bob),
            run_time=10
        )
        self.wait()


    def func_to_graph(self, x):
        return(x**3)
