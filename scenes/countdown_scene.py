import scene


class CountdownScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.counter = 3
        self.tick = 0

    def update(self, pyxel):
        if pyxel.btnp(pyxel.KEY_Q):
            self.app.scenes_manager.transition("main_scene")

        # process with any variables
        self.tick += 1
        if self.tick % 30 == 0:  # 30秒に一回
            self.counter -= 1
            if self.counter <= 0:  # カウントダウン終了
                self.app.scenes_manager.transition("game_scene")

    def draw(self, pyxel):
        pyxel.text(75, 90, "Stating in {}".format(self.counter), 1)

    def before_render(self, pyxel, parameters):
        self.tick = 0
        self.counter = 3
