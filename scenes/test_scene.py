import scene
import datetime


class TestScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.message = "Hello World!"

    def update(self, pyxel):
        now = datetime.datetime.now()
        self.message = "Hello World at {}:{}:{}".format(now.hour, now.minute, "0" + str(now.second) if now.second < 10 else now.second)

        if pyxel.btnp(pyxel.KEY_D):
            self.app.scenes_manager.transition("static_scene")
        elif pyxel.btnp(pyxel.KEY_S):
            self.app.scenes_manager.transition("main_scene")

    def draw(self, pyxel):
        pyxel.text(10, 10, self.message, 0)
        pyxel.text(10, 30, "Author: Riku Mochizuki", 1)
        pyxel.text(10, 40, "Student: 72048095", 1)
        pyxel.text(10, 50, "E-Mail: t20809rm at sfc.keio.ac.jp", 1)

        pyxel.text(100, 190, "Press S to back to main.", 5)
