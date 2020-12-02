import math
import scene

from components.liner_graph import LinerGraph


class StaticScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai

        # data
        rad = 180 + 1
        data_x = [n for n in range(rad)]
        roc = [float(i) / 60.0 for i in range(rad)]
        data_y = [2 * roc[m] * math.sin(math.radians(m * 2 * (1 + roc[m]))) for m in range(rad)]

        self.zoom_on = 0.1

        self.graph = LinerGraph(data_x=data_x, data_y=data_y, zoom=0.1, graph_size=[150, 95])
        self.graph.calculate(zoom=self.zoom_on)

    def update(self, pyxel):
        if pyxel.btnp(pyxel.KEY_A):
            self.app.scenes_manager.transition("test_scene")
        elif pyxel.btnp(pyxel.KEY_S):
            self.app.scenes_manager.transition("main_scene")

        wheel_diff = pyxel.mouse_wheel
        if wheel_diff != 0:
            self.zoom_on -= wheel_diff / 10.0
            if self.zoom_on > 1.0:
                self.zoom_on = 1.0
            elif self.zoom_on < 0.05:
                self.zoom_on = 0.05
            self.graph.calculate(zoom=self.zoom_on)  # 再計算

    def draw(self, pyxel):
        self.graph.render(pyxel, x=30, y=120, title="Zoom on x{}".format(round(self.zoom_on, 1)))

    def before_transition(self, pyxel):
        self.zoom_on = 0.1  # set Default
