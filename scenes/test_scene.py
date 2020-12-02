import scene
import datetime


class TestScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.message = "TEST MSG!"

    def update(self, pyxel):
        self.message = "Hello World!:" + str(datetime.datetime.now().second) + "s"

        if pyxel.btnp(pyxel.KEY_D):
            self.app.scenes_manager.transition("static_scene")
        elif pyxel.btnp(pyxel.KEY_S):
            self.app.scenes_manager.transition("main_scene")

    def draw(self, pyxel):
        pyxel.text(10, 10, self.message, 0)
