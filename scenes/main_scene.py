import scene


class MainScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai

    def update(self, pyxel):
        if pyxel.btn(pyxel.KEY_A):
            self.app.scenes_manager.transition("test_scene")
        elif pyxel.btn(pyxel.KEY_D):
            self.app.scenes_manager.transition("static_scene")

    def draw(self, pyxel):
        pyxel.text(10, 10, "Press space to start game.", 0)
        pyxel.text(10, 20, "Press D to view your stats for all.", 0)
        pyxel.text(10, 30, "Press A to view Hello World!", 0)
