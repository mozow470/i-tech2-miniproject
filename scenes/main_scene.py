import scene


class MainScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.is_countdown = False
        self.counter = 3
        self.tick = 0

    def update(self, pyxel):
        # define key actions
        if pyxel.btnp(pyxel.KEY_A):
            self.app.scenes_manager.transition("test_scene")
        elif pyxel.btnp(pyxel.KEY_D):
            self.app.scenes_manager.transition("static_scene")
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.is_countdown = True
        elif pyxel.btnp(pyxel.KEY_Q):  # ゲーム自体を終了する
            pyxel.quit()  # kill this process.

        # process with any variables
        if self.is_countdown:
            self.tick += 1
            if self.tick % 30 == 0:  # 30秒に一回
                self.counter -= 1
                if self.counter <= 0:  # カウントダウン終了
                    self.app.scenes_manager.transition("game_scene")

    def draw(self, pyxel):
        if self.is_countdown:
            pyxel.text(75, 90, "Stating in {}".format(self.counter), 0)
        else:
            pyxel.text(50, 90, "Press space to start game.", 0)
            pyxel.text(57, 180, "Press D to view your stats for all.", 5)
            pyxel.text(5, 190, "Press A to view Hello World!", 5)

    def before_render(self, pyxel):
        self.is_countdown = False
        self.tick = 0
        self.counter = 3
        print("Switch to", self.name)
