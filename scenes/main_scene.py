import scene


class MainScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.tick = 0
        self.is_appear_title = True

    def update(self, pyxel):
        # define key actions
        if pyxel.btnp(pyxel.KEY_D):
            self.app.scenes_manager.transition("static_scene")
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.app.scenes_manager.transition("countdown_scene")
        elif pyxel.btnp(pyxel.KEY_A):
            self.app.scenes_manager.transition("test_scene")
        elif pyxel.btnp(pyxel.KEY_Q):  # ゲーム自体を終了する
            pyxel.quit()  # kill this process.

        self.tick +=1

        if self.tick % 10 == 0:
            self.is_appear_title = not self.is_appear_title

    def draw(self, pyxel):
        if self.is_appear_title:
            pyxel.text(50, 90, "Press space to start game.", 0)
        pyxel.text(57, 180, "Press D to view your stats for all.", 5)
        pyxel.text(5, 190, "Press A to view details", 5)

    def before_render(self, pyxel, parameters):
        self.tick = 0
        print("Switch to", self.name)
