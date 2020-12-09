import scene
import datetime


class ResultScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.point: int = 0
        self.accuracy: float = 0

    def update(self, pyxel):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.app.scenes_manager.transition("main_scene")

    def draw(self, pyxel):
        pyxel.text(10, 10, "GAME RESULT", 1)
        pyxel.text(10, 20, "Your Score    : {}".format(self.point), 0)
        pyxel.text(10, 30, "Total Accuracy: {}%".format(self.accuracy), 0)
        pyxel.text(65, 190, "Press SPACE to back to main", 5)

    def before_render(self, pyxel, parameters):
        self.point = parameters["point"]  # get prev score
        self.accuracy = parameters["accuracy"]  # get prev accuracy
        self.app.store.push_to_store(self.point, self.accuracy)
