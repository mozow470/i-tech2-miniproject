import scene
import datetime

print(datetime)


class TestScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.message = "TEST MSG!"

    def update(self, pyxel):
        self.message = "Hello World!:" + str(datetime.datetime.now().second) + "s"

    def draw(self, pyxel):
        pyxel.text(10, 10, self.message, 0)
