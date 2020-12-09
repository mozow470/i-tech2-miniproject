import scene

from components.liner_graph import LinerGraph


class StatisticsScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai

        # data
        self.data_x = []
        self.data_y = []
        self.graph = self.make_graph()
        self.zoom_on = 1.0

    def update(self, pyxel):
        if pyxel.btnp(pyxel.KEY_S):
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
        self.graph.render(pyxel, x=10, y=130, title="Your Score statics x{}".format(round(self.zoom_on, 1)))
        pyxel.text(5, 190, "Press S to back to main.", 5)

    def before_render(self, pyxel, parameters):
        data = self.app.store.records
        self.data_x = [i for i in range(len(data))]  # index
        self.data_y = [int(data[i][1]) for i in range(len(data))]  # score
        self.zoom_on = 1.0  # set Default
        self.graph = self.make_graph()
        self.graph.calculate(zoom=self.zoom_on)

    def make_graph(self):
        return LinerGraph(data_x=self.data_x, data_y=self.data_y, zoom=0.1, graph_size=[180, 100])
