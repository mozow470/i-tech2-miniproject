import scene


class GameScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai

    def update(self, pyxel):
        pass

    def draw(self, pyxel):
        pyxel.text(10, 10, "This is a game scene!", 0)
