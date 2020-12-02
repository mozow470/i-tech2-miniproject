import scene


class GameScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai

    def update(self, pyxel):
        if pyxel.btn(pyxel.KEY_Q):
            self.app.scenes_manager.transition("main_scene")

    def draw(self, pyxel):
        pyxel.text(10, 10, "This is a game scene!", 0)
