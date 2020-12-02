import scene
import datetime


class Ball(object):

    def __init__(self, game, x, y, radius=10):
        self.game = game
        self.radius = radius
        self.xy = [x, y]

    def is_clicked(self, x, y):
        vec = self.xy[0] - x, self.xy[1] - y  # マウスの位置から、オブジェクトの中心座標に向いたベクトル
        vec_size = abs(vec[0]) + abs(vec[1])  # 単位を揃えたいので絶対値でベクトルの大きさを求める
        print(float(vec_size)/float(self.radius+2))
        return float(vec_size)/float(self.radius+2) <= 1  # ハズレ度合い 0<=x<=1 .. 円の中をクリックした、 1<x .. 円の外


class GameScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.point = 0
        self.balls = []
        self.test_ball = Ball(game=self, x=50, y=50)

    def update(self, pyxel):
        if pyxel.btn(pyxel.KEY_Q):
            self.app.scenes_manager.transition("main_scene")

        mouse_xy = pyxel.mouse_x, pyxel.mouse_y

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            print("Clicked !")
            if self.test_ball.is_clicked(mouse_xy[0], mouse_xy[1]):
                print("Get score!")

    def draw(self, pyxel):
        pyxel.text(10, 10, "This is a game scene!", 0)
        pyxel.circ(self.test_ball.xy[0], self.test_ball.xy[1], self.test_ball.radius, 2)

    def before_render(self, pyxel):
        self.point = 0  # reset point for next game.
