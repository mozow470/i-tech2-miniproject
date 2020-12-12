import scene
from .game_scene import Preset

presets = [
    Preset(name="Easy", ball_count=4, limit_of_miss=5, rate_of_trick=0.1),  # Easy
    Preset(name="Normal", ball_count=5, limit_of_miss=5, rate_of_trick=0.075),  # Normal
    Preset(name="Advanced", ball_count=7, limit_of_miss=5, rate_of_trick=0.05),  # Hard
]


class SettingsScene(scene.Scene):

    def __init__(self, name):
        global presets
        super().__init__(name)  # スーパークラス Omajinai
        self.current_preset = presets[0]  # Most easiler
        self.flash_message = ""

    def apply_preset(self, preset: Preset):
        self.current_preset = preset
        self.flash_message = "Difficulty level has been changed {}.".format(preset.name)
        self.app.pyi.play(0, 1)

    def update(self, pyxel):
        global presets
        # define key actions
        if pyxel.btnp(pyxel.KEY_1):
            self.apply_preset(presets[0])
        elif pyxel.btnp(pyxel.KEY_2):
            self.apply_preset(presets[1])
        elif pyxel.btnp(pyxel.KEY_3):
            self.apply_preset(presets[2])
        elif pyxel.btnp(pyxel.KEY_S):  # back to main
            self.app.scenes_manager.transition("main_scene", preset=self.current_preset)

    def draw(self, pyxel):
        pyxel.text(10, 10, "Difficulty level: {}".format(self.current_preset.name), 9)
        pyxel.text(10, 20, " - Press 1 to change to Easy", 0)
        pyxel.text(10, 30, " - Press 2 to change to Normal", 0)
        pyxel.text(10, 40, " - Press 3 to change to Advanced", 0)
        pyxel.text(90, 190, " - Press S to back to main.", 5)

    def before_render(self, pyxel, parameters, before):
        self.flash_message = ""
