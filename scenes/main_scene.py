import scene
from .settings_scene import presets


class MainScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.tick = 0
        self.is_appear_title = True
        self.preset = presets[0]

    def update(self, pyxel):
        # define key actionsを
        if pyxel.btnp(pyxel.KEY_D):
            self.app.scenes_manager.transition("statistics_scene")
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.app.scenes_manager.transition("countdown_scene", preset=self.preset)  # プリセットを渡してゲーム開始 
        elif pyxel.btnp(pyxel.KEY_A):
            self.app.scenes_manager.transition("settings_scene")
        elif pyxel.btnp(pyxel.KEY_Q):  # ゲーム自体を終了する
            pyxel.quit()  # kill this process.

        self.tick +=1

        if self.tick % 10 == 0:
            self.is_appear_title = not self.is_appear_title

    def draw(self, pyxel):
        if self.is_appear_title:
            pyxel.text(50, 90, "Press space to start game.", 0)
        pyxel.text(57, 180, "Press D to view your stats for all.", 5)
        pyxel.text(5, 190, "Press A to view settings", 5)

    def before_render(self, pyxel, parameters, before):
        self.tick = 0

        if before == "settings_scene":  # Update preset.
            self.preset = parameters["preset"]
